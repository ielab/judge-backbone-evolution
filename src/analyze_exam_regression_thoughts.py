import json
import csv
import argparse
import os
import sys
import urllib.request
import urllib.error
import time
import gzip

try:
    from dotenv import load_dotenv
    load_dotenv(os.path.expanduser('~/.env'))
except ImportError:
    pass

def load_exam_outputs(filepath):
    print(f"Loading EXAM outputs from {filepath}...")
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
                        
                        grades = item['exam_grades']
                        if not grades: continue
                        
                        thought = grades[0].get('llm_thought_text', '')
                        output = grades[0].get('llm_response_text', '')
                        
                        key = f"{qid}_{docid}"
                        data[key] = {
                            'thought': thought,
                            'output': output
                        }
            except Exception as e:
                pass
    return data

def analyze_regression(api_key, query_text, doc_text, human_score, score_a, score_b, thought_a, thought_b):
    prompt = f"""You are an expert AI evaluator analyzing the regression in judgment between two versions of an LLM.

Query: "{query_text}"
Document: "{doc_text}"
Human Relevance Score: {human_score}

Model A (Correct/Better Model) gave score: {score_a}
Model A's Reasoning:
{thought_a}

Model B (Worse/Regressed Model) gave score: {score_b}
Model B's Reasoning:
{thought_b}

Please analyze the difference in reasoning trajectories. Why did Model B regress and give a worse judgment compared to Model A?
Categorize the primary error made by Model B (e.g., "Hallucinated Requirement", "Ignored Nuance", "Over-weighted specific aspect", "Formatting issue", etc.) and provide a brief explanation.

Output your response strictly as a JSON object with two keys:
{{
  "error_category": "Short phrase categorizing the error",
  "explanation": "Brief explanation of why the reasoning diverged"
}}
"""
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash:generateContent?key={api_key}"
    headers = {'Content-Type': 'application/json'}
    data = {
        "contents": [{"parts": [{"text": prompt}]}],
        "generationConfig": {"responseMimeType": "application/json"}
    }
    
    req = urllib.request.Request(url, data=json.dumps(data).encode('utf-8'), headers=headers)
    try:
        with urllib.request.urlopen(req) as response:
            result = json.loads(response.read().decode('utf-8'))
            text_response = result['candidates'][0]['content']['parts'][0]['text']
            # Clean up markdown JSON blocks if present
            if text_response.startswith("```json"):
                text_response = text_response.strip("```json").strip("```").strip()
            parsed = json.loads(text_response)
            return parsed.get('error_category', ''), parsed.get('explanation', '')
    except Exception as e:
        print(f"Error during LLM analysis: {e}")
        return "Error", str(e)

def main():
    parser = argparse.ArgumentParser(description="Analyze regressions between two EXAM models by comparing their thinking trajectories.")
    parser.add_argument("--regressions", required=True, help="Path to the regressions JSONL file (e.g. analysis/regressions_...exam.jsonl)")
    parser.add_argument("--exam-output-a", required=True, help="Path to EXAM output JSONL.GZ for Model A (the better one)")
    parser.add_argument("--exam-output-b", required=True, help="Path to EXAM output JSONL.GZ for Model B (the regressed one)")
    parser.add_argument("--output", required=True, help="Path to the output CSV file")
    
    args = parser.parse_args()
    
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        print("Error: GEMINI_API_KEY environment variable not set.")
        sys.exit(1)
        
    outputs_a = load_exam_outputs(args.exam_output_a)
    outputs_b = load_exam_outputs(args.exam_output_b)
    
    # Check for existing progress
    processed = set()
    file_exists = os.path.exists(args.output)
    if file_exists:
        try:
            with open(args.output, 'r', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    if 'query_id' in row and 'corpus_id' in row:
                        processed.add((str(row['query_id']), str(row['corpus_id'])))
        except Exception as e:
            print(f"Warning: could not read existing output file: {e}")
            
    print(f"Loading regressions from {args.regressions}...")
    with open(args.regressions, 'rt') as f:
        lines = [line for line in f if line.strip()]
        
    print(f"Analyzing {len(lines)} regressions... ({len(processed)} already processed)")
    
    fieldnames = [
        'query_id', 'corpus_id', 'query_text', 'document_text', 'human_score',
        'score_model_a', 'score_model_b', 'thought_model_a', 'thought_model_b',
        'error_category', 'explanation'
    ]
    
    import threading
    from concurrent.futures import ThreadPoolExecutor, as_completed
    csv_lock = threading.Lock()
    
    # Pre-filter lines that are already processed
    tasks = []
    for line in lines:
        data = json.loads(line)
        qid = str(data['query_id'])
        cid = str(data['corpus_id'])
        if (qid, cid) not in processed:
            tasks.append((data, qid, cid))
            
    print(f"Remaining tasks to process: {len(tasks)}")

    with open(args.output, 'a', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        if not file_exists or os.path.getsize(args.output) == 0:
            writer.writeheader()
            
        def process_task(task):
            data, qid, cid = task
            query_text = data.get('query_text', '')
            doc_text = data.get('document_text', '')
            human_score = data.get('human_score', '')
            score_a = data.get('model_a_assessment', '')
            score_b = data.get('model_b_assessment', '')
            
            key = f"{qid}_{cid}"
            thought_a = outputs_a.get(key, {}).get('thought', 'N/A')
            thought_b = outputs_b.get(key, {}).get('thought', 'N/A')
            
            # Retry logic in case of rate limits
            for attempt in range(3):
                category, explanation = analyze_regression(
                    api_key, query_text, doc_text, human_score, score_a, score_b, thought_a, thought_b
                )
                if category != "Error" or attempt == 2:
                    break
                time.sleep(2)
            
            row = {
                'query_id': qid,
                'corpus_id': cid,
                'query_text': query_text,
                'document_text': doc_text,
                'human_score': human_score,
                'score_model_a': score_a,
                'score_model_b': score_b,
                'thought_model_a': thought_a,
                'thought_model_b': thought_b,
                'error_category': category,
                'explanation': explanation
            }
            
            with csv_lock:
                writer.writerow(row)
                csvfile.flush()
                
        with ThreadPoolExecutor(max_workers=30) as executor:
            futures = {executor.submit(process_task, task): task for task in tasks}
            for i, future in enumerate(as_completed(futures)):
                if (i+1) % 50 == 0:
                    print(f"Processed {i+1}/{len(tasks)} regressions...")
            
    print("Done!")

if __name__ == "__main__":
    main()
