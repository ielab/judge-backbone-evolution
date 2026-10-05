import json
import argparse
import os
import re

import gzip

def load_jsonl(filepath):
    data = {}
    opener = gzip.open if str(filepath).endswith('.gz') else open
    with opener(filepath, 'rt') as f:
        for line in f:
            if not line.strip(): continue
            try:
                line_data = json.loads(line)
                
                # Support both flat jsonl and grouped [query_id, [paragraphs]] format
                if isinstance(line_data, list) and len(line_data) == 2 and isinstance(line_data[1], list):
                    items = line_data[1]
                else:
                    items = [line_data]
                    
                for item in items:
                    if 'exam_grades' in item:
                        docid = str(item['paragraph_id'])
                        judgments = item.get('paragraph_data', {}).get('judgments', [])
                        if not judgments: continue
                        qid = str(judgments[0]['query'])
                        human_score = int(judgments[0]['relevance'])
                        
                        grades = item['exam_grades']
                        if not grades: continue
                        
                        ratings = grades[0].get('self_ratings', [])
                        correct_answered = grades[0].get('correctAnswered', [])
                        wrong_answered = grades[0].get('wrongAnswered', [])
                        
                        if correct_answered or wrong_answered:
                            covered = len(correct_answered)
                            total = len(correct_answered) + len(wrong_answered)
                            score = round((covered / total) * 3) if total > 0 else 0
                        elif ratings and all(isinstance(r, (int, float)) for r in ratings):
                            covered = sum(1 for r in ratings if r >= 4)
                            total = len(ratings)
                            score = round((covered / total) * 3) if total > 0 else 0
                        else:
                            continue

                        
                        key = f"{qid}_{docid}"
                        data[key] = {
                            "model_score": score,
                            "human_score": human_score,
                            "query_text": qid,
                            "raw_output": json.dumps(grades[0]),
                            "query_id": qid,
                            "corpus_id": docid
                        }
                    else:
                        row = item
                        key = f"{row['query_id']}_{row['corpus_id']}"
                        
                        # Extract numeric score from output
                        raw_output = row.get('model_output', row.get('gemini_output', ''))
                        output = raw_output.strip()
                        score = None
                        match = re.search(r"final\s*score:?\s*[*]*([0-3])[*]*", output, re.IGNORECASE)
                        if match:
                            score = int(match.group(1))
                        else:
                            matches = re.findall(r'\b([0-3])\b', output)
                            if matches:
                                score = int(matches[-1])
                        
                        if score is not None:
                            data[key] = {
                                "model_score": score,
                                "human_score": int(row['original_qrel_score']),
                                "query_text": row.get('query_text', ''),
                                "raw_output": raw_output,
                                "query_id": row['query_id'],
                                "corpus_id": row['corpus_id']
                            }
            except Exception as e:
                pass
    return data

def main():
    parser = argparse.ArgumentParser(description="Find regressions between two models compared to human ground truth.")
    parser.add_argument("--model_a", required=True, help="Path to the baseline model (e.g., 2.5 Flash) JSONL")
    parser.add_argument("--model_b", required=True, help="Path to the new model (e.g., 3.8 Flash) JSONL")
    parser.add_argument("--output", type=str, default=None, help="Optional base filename (without extension) to export full regression data. Generates both .jsonl and .csv files.")
    args = parser.parse_args()
    
    print(f"Loading Model A (Baseline): {args.model_a}")
    data_a = load_jsonl(args.model_a)
    
    print(f"Loading Model B (New): {args.model_b}")
    data_b = load_jsonl(args.model_b)
    
    shared_keys = set(data_a.keys()).intersection(set(data_b.keys()))
    print(f"\nFound {len(shared_keys)} shared judgments between the two files.\n")
    
    regressions = []
    
    for key in shared_keys:
        a = data_a[key]
        b = data_b[key]
        
        human_score = a["human_score"]
        score_a = a["model_score"]
        score_b = b["model_score"]
        
        # Regression condition: Model A was correct, Model B was wrong.
        if score_a == human_score and score_b != human_score:
            error_magnitude = abs(score_b - human_score)
            regressions.append({
                "query_id": a["query_id"],
                "corpus_id": a["corpus_id"],
                "query_text": a["query_text"],
                "human_score": human_score,
                "score_a": score_a,
                "score_b": score_b,
                "output_b": b["raw_output"],
                "error_magnitude": error_magnitude
            })
            
    print("==================================================")
    print(f"REGRESSIONS SUMMARY")
    print("==================================================")
    print(f"Total Regressions: {len(regressions)}")
    if len(shared_keys) > 0:
        print(f"Regression Rate: {len(regressions) / len(shared_keys) * 100:.2f}%")
        
    # Sort regressions by error magnitude descending
    regressions.sort(key=lambda x: x["error_magnitude"], reverse=True)
    
    print("\n==================================================")
    print("TOP REGRESSIONS (Model A correct, Model B wrong)")
    print("==================================================")
    
    limit = min(10, len(regressions))
    for i in range(limit):
        reg = regressions[i]
        print(f"Rank {i+1}: Query {reg['query_id']} / Doc {reg['corpus_id']}")
        print(f"  Query text: {reg['query_text']}")
        print(f"  Human Score: {reg['human_score']}")
        print(f"  Model A Score: {reg['score_a']} (Correct)")
        print(f"  Model B Score: {reg['score_b']} (Wrong, error size {reg['error_magnitude']})")
        print(f"  Model B Output: {reg['output_b'].strip()}")
        print("-" * 30)

    # Output detailed regression data to file
    if args.output:
        output_dir = os.path.dirname(args.output)
        if output_dir:
            os.makedirs(output_dir, exist_ok=True)
        base_name = args.output
        # Strip extension if user accidentally provided one
        if base_name.endswith('.jsonl') or base_name.endswith('.csv'):
            base_name = base_name.rsplit('.', 1)[0]
            
        jsonl_output = f"{base_name}.jsonl"
        csv_output = f"{base_name}.csv"
        
        print(f"\nExporting detailed regression data to {jsonl_output} and {csv_output}...")
        from datasets import load_dataset
        from tqdm import tqdm
        
        needed_docids = set([r["corpus_id"] for r in regressions])
        doc_dict = {}
        
        print("Fetching document texts from local data (this will be instant)...")
        pbar = tqdm(total=len(needed_docids), desc="Finding passages")
        
        with gzip.open("data/trecDL2019-qrels-runs-with-text.jsonl.gz", "rt") as f:
            for line in f:
                data = json.loads(line)
                if isinstance(data, list) and len(data) == 2 and isinstance(data[1], list):
                    for item in data[1]:
                        doc_id = str(item.get("paragraph_id", ""))
                        if doc_id in needed_docids and doc_id not in doc_dict:
                            doc_dict[doc_id] = item.get("text", "")
                            pbar.update(1)
                if len(doc_dict) >= len(needed_docids):
                    break
        pbar.close()
        
        import csv
        with open(jsonl_output, 'w') as f_jsonl, open(csv_output, 'w', newline='', encoding='utf-8') as f_csv:
            fieldnames = ["query_id", "query_text", "corpus_id", "document_text", "human_score", "model_a_assessment", "model_b_assessment", "model_b_raw_output"]
            writer = csv.DictWriter(f_csv, fieldnames=fieldnames)
            writer.writeheader()
            
            for reg in regressions:
                reg_data = {
                    "query_id": reg["query_id"],
                    "query_text": reg["query_text"],
                    "corpus_id": reg["corpus_id"],
                    "document_text": doc_dict.get(reg["corpus_id"], ""),
                    "human_score": reg["human_score"],
                    "model_a_assessment": reg["score_a"],
                    "model_b_assessment": reg["score_b"],
                    "model_b_raw_output": reg["output_b"]
                }
                f_jsonl.write(json.dumps(reg_data) + "\n")
                writer.writerow(reg_data)
        print(f"Successfully saved {len(regressions)} full regression records.")

if __name__ == "__main__":
    main()
