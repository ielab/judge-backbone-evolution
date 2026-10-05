import json
import os
import sys
import yaml
import time
import socket
import threading
import argparse
import re
from tqdm import tqdm
from datasets import load_dataset
from concurrent.futures import ThreadPoolExecutor, as_completed
import ir_datasets

# Conditional imports for providers
try:
    from google import genai
    from google.genai import types
except ImportError:
    genai = None

try:
    import openai
except ImportError:
    openai = None

def process_item(row, client, provider, model_name, doc_dict, query_dict, prefix_user, system_message, file_lock, output_file, retries, think, think_budget, disable_thinking):
    qid = str(row['query-id'])
    docid = str(row['corpus-id'])
    original_score = row['score']
    
    passage = doc_dict.get(docid, "")
    query_text = query_dict.get(qid, "")
    
    if not passage or not query_text:
        return False
        
    prompt_text = prefix_user.replace("{query}", query_text).replace("{passage}", passage)
    
    OPENAI_THINKING_MODELS = ["o1-mini", "o3-mini", "o1", "o3", "gpt-4.1", "gpt-5"]
    
    # Exponential Backoff Retry Loop
    for attempt in range(retries):
        try:
            final_text = ""
            thought_text = ""
            
            if provider == "gemini":
                config_kwargs = {
                    "temperature": 0.0
                }
                if system_message:
                    config_kwargs["system_instruction"] = system_message
                    
                if think:
                    config_kwargs["thinking_config"] = types.ThinkingConfig(
                        include_thoughts=True,
                        thinking_budget=think_budget
                    )
                
                response = client.models.generate_content(
                    model=model_name,
                    contents=prompt_text,
                    config=types.GenerateContentConfig(**config_kwargs)
                )
                
                if response.candidates and response.candidates[0].content and response.candidates[0].content.parts:
                    for part in response.candidates[0].content.parts:
                        if getattr(part, 'thought', False):
                            thought_text += part.text
                        elif part.text:
                            final_text += part.text
                else:
                    final_text = response.text if response.text else ""
                    
            elif provider == "openai":
                messages = []
                # NOTE: o1 models do not currently support system messages or temperature=0.0 natively via API without developer tier,
                # but for standard models we pass them.
                is_o_model = any(model_name.startswith(m) for m in OPENAI_THINKING_MODELS)
                
                if system_message:
                    if is_o_model:
                        # Append system message to user for o1 models if needed, or pass as user
                        messages.append({"role": "user", "content": f"System Instruction: {system_message}\n\n{prompt_text}"})
                    else:
                        messages.append({"role": "system", "content": system_message})
                        messages.append({"role": "user", "content": prompt_text})
                else:
                    messages.append({"role": "user", "content": prompt_text})
                
                kwargs = {
                    "model": model_name,
                    "messages": messages,
                }

                # Qwen3-family chat templates support an explicit switch.  vLLM
                # accepts it through the OpenAI-compatible request's extra_body.
                if disable_thinking:
                    kwargs["extra_body"] = {
                        "chat_template_kwargs": {"enable_thinking": False}
                    }
                
                if not is_o_model:
                    kwargs["temperature"] = 0.0
                
                try:
                    response = client.chat.completions.create(**kwargs)
                except openai.BadRequestError as e:
                    if "temperature" in str(e).lower():
                        if "temperature" in kwargs:
                            del kwargs["temperature"]
                        response = client.chat.completions.create(**kwargs)
                    else:
                        raise e
                
                final_text = response.choices[0].message.content or ""
                
                if think:
                    if hasattr(response.choices[0].message, 'reasoning_content') and response.choices[0].message.reasoning_content:
                        thought_text = response.choices[0].message.reasoning_content
            
            result_entry = {
                "query_id": qid,
                "corpus_id": docid,
                "original_qrel_score": original_score,
                "query_text": query_text,
                "model_output": final_text
            }
            if think:
                result_entry["model_thought"] = thought_text
            
            # Thread-safe writing
            with file_lock:
                with open(output_file, "a") as f:
                    f.write(json.dumps(result_entry) + "\n")
                    f.flush()
            
            return True
            
        except Exception as e:
            if attempt < retries - 1:
                wait_time = 2 ** attempt * 5  # 5, 10, 20, 40 seconds
                time.sleep(wait_time)
            else:
                print(f"Failed {qid}-{docid} after {retries} attempts. Error: {e}")
                return False

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--provider", type=str, choices=["gemini", "openai"], default="gemini", help="API provider to use")
    parser.add_argument("--model", type=str, default="gemini-3.8-flash")
    parser.add_argument("--gemini_key", type=str, default="", help="Gemini API Key")
    parser.add_argument("--openai_key", type=str, default="", help="OpenAI API Key")
    parser.add_argument("--base_url", type=str, default="", help="OpenAI-compatible API base URL (for example, a local vLLM server)")
    parser.add_argument("--workers", type=int, default=16)
    parser.add_argument("--retries", type=int, default=5)
    parser.add_argument("--think", action="store_true", help="Enable thinking tokens extraction")
    parser.add_argument("--think_budget", type=int, default=1024, help="Budget for thinking tokens (Gemini only)")
    parser.add_argument("--disable_thinking", action="store_true", help="Disable thinking through Qwen3-family vLLM chat-template kwargs")
    parser.add_argument(
        "--dataset",
        choices=["trec-dl-2019", "trec-dl-2020"],
        default="trec-dl-2019",
        help="TREC Deep Learning passage dataset to evaluate",
    )
    parser.add_argument("--prompt_template", type=str, default="~/github/umbrela/src/umbrela/prompts/prompt_templates/qrel_zeroshot_bing.yaml", help="Path to the UMBRELA YAML prompt")
    parser.add_argument("--run_id", type=int, default=None, help="Optional run ID for repeat stability analysis")
    parser.add_argument("--output_dir", type=str, default="results", help="Directory to save the outputs")
    args = parser.parse_args()
    
    # Initialize client based on provider
    client = None
    if args.provider == "gemini":
        if genai is None:
            print("google-genai package is not installed. Please install it.")
            sys.exit(1)
        api_key = args.gemini_key or os.environ.get("GEMINI_API_KEY")
        if not api_key:
            print("Please provide a Gemini API key via --gemini_key or GEMINI_API_KEY environment variable.")
            sys.exit(1)
        client = genai.Client(api_key=api_key)
    elif args.provider == "openai":
        if openai is None:
            print("openai package is not installed. Please install it.")
            sys.exit(1)
        api_key = args.openai_key or os.environ.get("OPENAI_API_KEY")
        if not api_key:
            print("Please provide an OpenAI API key via --openai_key or OPENAI_API_KEY environment variable.")
            sys.exit(1)
        base_url = args.base_url or os.environ.get("OPENAI_BASE_URL")
        client_kwargs = {"api_key": api_key}
        if base_url:
            client_kwargs["base_url"] = base_url
        client = openai.OpenAI(**client_kwargs)
    
    model_name = args.model
    os.makedirs(args.output_dir, exist_ok=True)
    model_slug = re.sub(r"[^A-Za-z0-9_-]+", "_", model_name)
    # Preserve existing DL19 filenames, but keep DL20 results separate so that
    # resume logic cannot accidentally combine two datasets.
    dataset_suffix = "" if args.dataset == "trec-dl-2019" else "_trec-dl-2020"
    if args.run_id is not None:
        output_file = os.path.join(args.output_dir, f"{model_slug}{dataset_suffix}_run{args.run_id}_annotations.jsonl")
    else:
        output_file = os.path.join(args.output_dir, f"{model_slug}{dataset_suffix}_annotations.jsonl")
    
    # --- RESUME LOGIC ---
    processed_set = set()
    if os.path.exists(output_file):
        with open(output_file, "r") as f:
            for line in f:
                if not line.strip(): continue
                try:
                    data = json.loads(line)
                    processed_set.add(f"{data['query_id']}_{data['corpus_id']}")
                except:
                    pass
        print(f"Found {len(processed_set)} existing annotations in {output_file}. Resuming...")
    
    cache_root = os.environ.get("HF_HOME", os.path.expanduser("~/.cache/huggingface"))
    dataset_slug = args.dataset.replace("-", "_")
    if args.run_id is not None:
        custom_cache_dir = os.path.join(cache_root, f"datasets_{dataset_slug}_{model_slug}_run{args.run_id}")
    else:
        custom_cache_dir = os.path.join(cache_root, f"datasets_{dataset_slug}_{model_slug}")
    print(f"Loading {args.dataset} qrels from whybe-choi/{args.dataset}...")
    ds = load_dataset(f"whybe-choi/{args.dataset}", split="test", cache_dir=custom_cache_dir)
    
    # Filter dataset for what's remaining
    remaining_rows = []
    for row in ds:
        q_doc_key = f"{row['query-id']}_{row['corpus-id']}"
        if q_doc_key not in processed_set:
            remaining_rows.append(row)
            
    print(f"Loaded {len(ds)} query-document pairs. {len(remaining_rows)} remaining to process.")
    
    if not remaining_rows:
        print("All documents already processed!")
        return
    
    needed_qids = set([str(row['query-id']) for row in remaining_rows])
    needed_docids = set([str(row['corpus-id']) for row in remaining_rows])
    
    ir_dataset_id = f"msmarco-passage/{args.dataset}/judged"
    print(f"Loading queries from ir_datasets ({ir_dataset_id})...")
    dataset = ir_datasets.load(ir_dataset_id)
    query_dict = {}
    for query in dataset.queries_iter():
        if query.query_id in needed_qids:
            query_dict[query.query_id] = query.text
            
    print(f"Fetching {len(needed_docids)} passages by streaming BeIR/msmarco corpus (this may take a few minutes)...")
    corpus_ds = load_dataset("BeIR/msmarco", "corpus", split="corpus", streaming=True)
    doc_dict = {}
    
    pbar = tqdm(total=len(needed_docids), desc="Finding passages")
    for row in corpus_ds:
        doc_id = str(row['_id'])
        if doc_id in needed_docids:
            doc_dict[doc_id] = row['text']
            pbar.update(1)
            if len(doc_dict) == len(needed_docids):
                break
    pbar.close()
    
    print(f"Found {len(doc_dict)} passages.")

    template_path = os.path.expanduser(args.prompt_template)
    if not os.path.isfile(template_path):
        parser.error(f"UMBRELA prompt template not found: {template_path}")
    with open(template_path, 'r') as f:
        template_yaml = yaml.safe_load(f)
        
    prefix_user = template_yaml.get("prefix_user", "")
    system_message = template_yaml.get("system_message", "")
    
    print(f"Annotating remaining {len(remaining_rows)} documents with {args.workers} workers. Results will be saved to {output_file}...")
    
    file_lock = threading.Lock()
    
    with ThreadPoolExecutor(max_workers=args.workers) as executor:
        futures = {executor.submit(process_item, row, client, args.provider, model_name, doc_dict, query_dict, prefix_user, system_message, file_lock, output_file, args.retries, args.think, args.think_budget, args.disable_thinking): row for row in remaining_rows}
        
        for future in tqdm(as_completed(futures), total=len(remaining_rows), desc="Annotating"):
            future.result()

    print(f"Done! Results saved to {output_file}.")

if __name__ == "__main__":
    main()
