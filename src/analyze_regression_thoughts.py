import json
import csv
import argparse
import os
import sys
import urllib.request
import urllib.error
import time

try:
    from dotenv import load_dotenv
    load_dotenv(os.path.expanduser('~/.env'))
except ImportError:
    pass

def load_annotations(filepath):
    print(f"Loading annotations from {filepath}...")
    annotations = {}
    with open(filepath, 'rt') as f:
        for line in f:
            if not line.strip(): continue
            try:
                data = json.loads(line)
                qid = str(data.get('query_id'))
                cid = str(data.get('corpus_id'))
                thought = data.get('gemini_thought', '')
                output = data.get('gemini_output', '')
                annotations[(qid, cid)] = {
                    'thought': thought,
                    'output': output
                }
            except json.JSONDecodeError:
                pass
    return annotations

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
            parsed = json.loads(text_response)
            return parsed.get('error_category', ''), parsed.get('explanation', '')
    except Exception as e:
        print(f"Error during LLM analysis: {e}")
        return "Error", str(e)

def main():
    parser = argparse.ArgumentParser(description="Analyze regressions between two models by comparing their thinking trajectories.")
    parser.add_argument("--regressions", required=True, help="Path to the regressions JSONL file (e.g. analysis/regressions_...jsonl)")
    parser.add_argument("--annotations-a", required=True, help="Path to annotations JSONL for Model A (the better one)")
    parser.add_argument("--annotations-b", required=True, help="Path to annotations JSONL for Model B (the regressed one)")
    parser.add_argument("--output", required=True, help="Path to the output CSV file")
    
    args = parser.parse_args()
    
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        print("Error: GEMINI_API_KEY environment variable not set.")
        sys.exit(1)
        
    annotations_a = load_annotations(args.annotations_a)
    annotations_b = load_annotations(args.annotations_b)
    
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
    
    # Open file in append mode
    with open(args.output, 'a', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        # If file didn't exist or is empty, write header
        if not file_exists or os.path.getsize(args.output) == 0:
            writer.writeheader()
            
        for i, line in enumerate(lines):
            data = json.loads(line)
            qid = str(data['query_id'])
            cid = str(data['corpus_id'])
            
            if (qid, cid) in processed:
                continue
                
            if i % 10 == 0:
                print(f"Processing regression {i}/{len(lines)}...")
                
            query_text = data.get('query_text', '')
            doc_text = data.get('document_text', '')
            human_score = data.get('human_score', '')
            score_a = data.get('model_a_assessment', '')
            score_b = data.get('model_b_assessment', '')
            
            thought_a = annotations_a.get((qid, cid), {}).get('thought', 'N/A')
            thought_b = annotations_b.get((qid, cid), {}).get('thought', 'N/A')
            
            category, explanation = analyze_regression(
                api_key, query_text, doc_text, human_score, score_a, score_b, thought_a, thought_b
            )
            
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
            
            writer.writerow(row)
            csvfile.flush() # Ensure it gets written to disk immediately
            processed.add((qid, cid))
            
            # Sleep slightly to respect rate limits if needed
            time.sleep(1.0)
            
    print("Done!")

if __name__ == "__main__":
    main()
