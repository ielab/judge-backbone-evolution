#!/usr/bin/env python3
"""Retry unparseable Llama UMBRELA annotations through a running vLLM server."""

import argparse
import json
import os
import re
import shutil
import tempfile
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

def extract_score(text, allow_floor=True):
    text = str(text).strip()

    match = re.search(
        r"final\s*score\s*(?:for\s+this\s+passage\s*)?(?:is\s*)?:?\s*[*]*([0-3](?:\.\d+)?)(?![\d.])[*]*",
        text,
        re.IGNORECASE,
    )
    if match:
        score = float(match.group(1))
        return int(score) if allow_floor or score.is_integer() else None

    match = re.search(
        r"overall(?:\s*score)?\s*(?:\(O\))?\s*[:=]\s*[*]*([0-3](?:\.\d+)?)(?![\d.])[*]*",
        text,
        re.IGNORECASE,
    )
    if match:
        score = float(match.group(1))
        return int(score) if allow_floor or score.is_integer() else None

    matches = re.findall(
        r"(?:^|\n)\s*O\s*[:=]\s*([0-3](?:\.\d+)?)(?![\d.])",
        text,
        re.IGNORECASE,
    )
    if matches:
        score = float(matches[-1])
        return int(score) if allow_floor or score.is_integer() else None

    return None


def load_records(path):
    records = []
    with path.open(encoding="utf-8") as stream:
        for line_number, line in enumerate(stream, 1):
            if not line.strip():
                continue
            try:
                records.append(json.loads(line))
            except json.JSONDecodeError as error:
                raise SystemExit(f"Invalid JSON at {path}:{line_number}: {error}") from error
    return records


def fetch_passages(doc_ids, cache_dir):
    from datasets import load_dataset
    from tqdm import tqdm

    passages = {}
    corpus = load_dataset("BeIR/msmarco", "corpus", split="corpus", streaming=True, cache_dir=cache_dir)
    progress = tqdm(total=len(doc_ids), desc="Finding passages")
    for row in corpus:
        doc_id = str(row["_id"])
        if doc_id in doc_ids:
            passages[doc_id] = row["text"]
            progress.update(1)
            if len(passages) == len(doc_ids):
                break
    progress.close()
    return passages


def retry_record(record, passage, client, model, prefix_user, system_message, attempts):
    prompt = prefix_user.replace("{query}", str(record["query_text"])).replace("{passage}", passage)
    messages = []
    if system_message:
        messages.append({"role": "system", "content": system_message})
    messages.append({"role": "user", "content": prompt})

    for attempt in range(1, attempts + 1):
        try:
            response = client.chat.completions.create(
                model=model,
                messages=messages,
                temperature=0.0,
            )
            output = response.choices[0].message.content or ""
            score = extract_score(output, allow_floor=False)
            if score is not None:
                updated = dict(record)
                updated["model_output"] = output
                return updated, True
            if attempt == attempts:
                score = extract_score(output, allow_floor=True)
                if score is not None:
                    updated = dict(record)
                    updated["original_output"] = output
                    updated["model_output"] = f"Final score: {score}"
                    return updated, True
            print(
                f"Unparseable response for {record['query_id']}-{record['corpus_id']} "
                f"(attempt {attempt}/{attempts})"
            )
        except Exception as error:
            print(
                f"Request failed for {record['query_id']}-{record['corpus_id']} "
                f"(attempt {attempt}/{attempts}): {error}"
            )
        if attempt < attempts:
            time.sleep(min(2 ** (attempt - 1), 8))
    return record, False


def write_atomically(path, records):
    backup = path.with_suffix(path.suffix + ".before-unparsed-retry")
    if not backup.exists():
        shutil.copy2(path, backup)

    fd, temp_name = tempfile.mkstemp(prefix=path.name + ".", suffix=".tmp", dir=path.parent)
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as stream:
            for record in records:
                stream.write(json.dumps(record, ensure_ascii=False) + "\n")
            stream.flush()
            os.fsync(stream.fileno())
        os.replace(temp_name, path)
    except BaseException:
        if os.path.exists(temp_name):
            os.unlink(temp_name)
        raise
    return backup


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("input", type=Path, help="Annotation JSONL file to repair in place")
    parser.add_argument("--model", required=True)
    parser.add_argument("--base-url", default=os.getenv("OPENAI_BASE_URL", "http://127.0.0.1:8100/v1"))
    parser.add_argument("--prompt-template", required=True, type=Path)
    parser.add_argument("--attempts", type=int, default=5)
    parser.add_argument("--workers", type=int, default=16)
    parser.add_argument("--cache-dir", default=os.getenv("HF_DATASETS_CACHE"))
    args = parser.parse_args()

    if args.attempts < 1:
        parser.error("--attempts must be at least 1")
    records = load_records(args.input)
    failed_indices = [
        i
        for i, record in enumerate(records)
        if extract_score(record.get("model_output"), allow_floor=False) is None
    ]
    print(f"{args.input}: {len(failed_indices)} unparseable of {len(records)} records")
    if not failed_indices:
        print(f"JSONL summary: replaced 0; parseable {len(records)}/{len(records)}")
        return

    import openai
    import yaml
    from tqdm import tqdm

    with args.prompt_template.open(encoding="utf-8") as stream:
        template = yaml.safe_load(stream)
    passages = fetch_passages(
        {str(records[i]["corpus_id"]) for i in failed_indices},
        args.cache_dir,
    )
    client = openai.OpenAI(api_key="EMPTY", base_url=args.base_url)
    repaired = skipped = missing = 0

    with ThreadPoolExecutor(max_workers=args.workers) as pool:
        futures = {}
        for index in failed_indices:
            record = records[index]
            passage = passages.get(str(record["corpus_id"]))
            if not passage:
                missing += 1
                continue
            future = pool.submit(
                retry_record,
                record,
                passage,
                client,
                args.model,
                template.get("prefix_user", ""),
                template.get("system_message", ""),
                args.attempts,
            )
            futures[future] = index

        for future in tqdm(as_completed(futures), total=len(futures), desc="Retrying"):
            index = futures[future]
            record, success = future.result()
            if success:
                records[index] = record
                repaired += 1
            else:
                skipped += 1

    backup = write_atomically(args.input, records)
    parseable = sum(extract_score(record.get("model_output")) is not None for record in records)
    print(f"Repaired: {repaired}; skipped after {args.attempts} attempts: {skipped}; missing passages: {missing}")
    print(f"JSONL summary: replaced {repaired}; parseable {parseable}/{len(records)}")
    print(f"Original backup: {backup}")


if __name__ == "__main__":
    main()
