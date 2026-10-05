import json
import csv
import glob
import os
import sys
import urllib.request
from collections import defaultdict
import re

try:
    from dotenv import load_dotenv
    load_dotenv(os.path.expanduser('~/.env'))
except ImportError:
    pass

UMBRELA_CATEGORIES = [
    "Over-weighted topical overlap",
    "Hallucinated Requirement",
    "Superficial Keyword Matching",
    "Overly Strict Interpretation",
    "Over-crediting tangential relevance",
    "Missing Reasoning",
    "Ignored Nuance",
    "Over-weighted specific aspect",
    "Overly Strict Relevance Threshold",
    "Over-weighted keyword match"
]

def map_categories_via_llm_batch(api_key, exam_categories_batch):
    prompt = f"""You are an expert AI evaluator analyzing error categories from a relevance judgment task.
We have a set of established error categories from a previous prompt (UMBRELA):
{json.dumps(UMBRELA_CATEGORIES, indent=2)}

We have generated a new set of error categories from a different prompt (EXAM):
{json.dumps(exam_categories_batch, indent=2)}

Your task is to map each EXAM category to the most semantically equivalent UMBRELA category.
If an EXAM category describes a completely new type of error that does not fit into any of the UMBRELA categories, you should map it to itself (meaning it is a NEW category).

Output your response strictly as a JSON object where the keys are the EXAM categories and the values are either the exact string of the matching UMBRELA category, or the exact string of the EXAM category if it is new.
"""
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash:generateContent?key={api_key}"
    headers = {'Content-Type': 'application/json'}
    data = {
        "contents": [{"parts": [{"text": prompt}]}],
        "generationConfig": {"responseMimeType": "application/json"}
    }
    
    req = urllib.request.Request(url, data=json.dumps(data).encode('utf-8'), headers=headers)
    for attempt in range(3):
        try:
            with urllib.request.urlopen(req) as response:
                result = json.loads(response.read().decode('utf-8'))
                text_response = result['candidates'][0]['content']['parts'][0]['text']
                if text_response.startswith("```json"):
                    text_response = text_response.strip("```json").strip("```").strip()
                return json.loads(text_response)
        except Exception as e:
            if attempt == 2:
                print(f"Error during LLM mapping batch: {e}")
                return {}
            import time; time.sleep(1)

def map_categories_via_llm(api_key, exam_categories):
    print(f"Mapping {len(exam_categories)} unique EXAM categories to UMBRELA categories in batches...")
    
    import concurrent.futures
    batch_size = 50
    batches = [exam_categories[i:i + batch_size] for i in range(0, len(exam_categories), batch_size)]
    
    full_mapping = {}
    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        futures = {executor.submit(map_categories_via_llm_batch, api_key, batch): batch for batch in batches}
        for future in concurrent.futures.as_completed(futures):
            res = future.result()
            if res:
                full_mapping.update(res)
                
    return full_mapping

def main():
    api_key = os.environ.get("GEMINI_API_KEY")
    # For standalone bash testing, might have export instead of load_dotenv working perfectly
    if not api_key:
        # Fallback to direct reading of .env for export syntax
        env_path = os.path.expanduser('~/.env')
        if os.path.exists(env_path):
            with open(env_path, 'r') as f:
                for line in f:
                    if line.startswith('export GEMINI_API_KEY='):
                        api_key = line.split('=')[1].strip().strip('"').strip("'")
    if not api_key:
        print("Error: GEMINI_API_KEY environment variable not set.")
        sys.exit(1)

    csv_files = glob.glob("analysis/thoughts_comparison_*_exam.csv")
    if not csv_files:
        print("No EXAM thought comparison CSV files found.")
        sys.exit(1)
        
    print(f"Found {len(csv_files)} EXAM thought comparison CSVs.")
    
    unique_exam_categories = set()
    all_regressions = [] # list of dicts with full row data + source model pair
    
    for fpath in csv_files:
        # Extract model pair from filename e.g. thoughts_comparison_gemini-2.5-flash_vs_gemini-3.5-flash_exam.csv
        match = re.search(r'thoughts_comparison_(.+)_vs_(.+)_exam\.csv', os.path.basename(fpath))
        model_a = match.group(1) if match else "unknown_a"
        model_b = match.group(2) if match else "unknown_b"
        
        with open(fpath, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                cat = row.get('error_category', '').strip()
                if cat:
                    unique_exam_categories.add(cat)
                    
                row['model_a'] = model_a
                row['model_b'] = model_b
                all_regressions.append(row)
                
    mapping = map_categories_via_llm(api_key, list(unique_exam_categories))
    
    if not mapping:
        print("Mapping failed. Exiting.")
        sys.exit(1)
        
    # Apply mapping
    mapped_counts = defaultdict(int)
    mapped_by_pair = defaultdict(lambda: defaultdict(int))
    
    mapped_regressions = []
    
    for row in all_regressions:
        orig_cat = row.get('error_category', '').strip()
        if not orig_cat: continue
        
        mapped_cat = mapping.get(orig_cat, orig_cat) # fallback to orig if missing
        
        mapped_counts[mapped_cat] += 1
        mapped_by_pair[f"{row['model_a']} vs {row['model_b']}"][mapped_cat] += 1
        
        row['mapped_category'] = mapped_cat
        mapped_regressions.append(row)
        
    # Output Statistical Summary
    summary_path = "analysis/exam_thought_categories_summary.md"
    print(f"Writing summary to {summary_path}...")
    
    with open(summary_path, 'w', encoding='utf-8') as f:
        f.write("# EXAM Thought Analysis Category Mapping\n\n")
        f.write("This document summarizes the error categories generated for the EXAM prompt regressions, and their mapping to the standard UMBRELA categories.\n\n")
        
        f.write("## Overall Category Distribution\n\n")
        f.write("| Category | Count | Is UMBRELA Category? |\n")
        f.write("|---|---|---|\n")
        
        for cat, count in sorted(mapped_counts.items(), key=lambda x: x[1], reverse=True):
            is_umbrela = "Yes" if cat in UMBRELA_CATEGORIES else "No (New)"
            f.write(f"| {cat} | {count} | {is_umbrela} |\n")
            
        f.write("\n## Breakdown by Model Pair\n\n")
        for pair, counts in mapped_by_pair.items():
            f.write(f"### {pair}\n")
            f.write("| Category | Count |\n")
            f.write("|---|---|\n")
            for cat, count in sorted(counts.items(), key=lambda x: x[1], reverse=True):
                f.write(f"| {cat} | {count} |\n")
            f.write("\n")
            
        f.write("## Raw Mapping Details\n\n")
        f.write("```json\n")
        f.write(json.dumps(mapping, indent=2))
        f.write("\n```\n")
        
    print("Done! Summary written.")

if __name__ == "__main__":
    main()
