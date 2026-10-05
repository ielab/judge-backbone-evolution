import json
import argparse
import re
from collections import defaultdict
import numpy as np

def extract_score(text):
    text = str(text).strip()
    match = re.search(r"final\s*score:?\s*[*]*([0-3])[*]*", text, re.IGNORECASE)
    if match:
        return int(match.group(1))
    # Some smaller models reproduce UMBRELA's intermediate M/T/O notation
    # instead of emitting "final score". O is the overall relevance score;
    # M and T are only component assessments.
    match = re.search(r"(?im)^\s*#{0,2}\s*O\s*:\s*\**([0-3])\b\**", text)
    if match:
        return int(match.group(1))
    matches = re.findall(r"\b([0-3])\b", text)
    if matches:
        return int(matches[-1])
    return None

import gzip

def load_annotations(filepath):
    data = {}
    opener = gzip.open if str(filepath).endswith('.gz') else open
    with opener(filepath, 'rt') as f:
        for line in f:
            if not line.strip():
                continue
            try:
                line_data = json.loads(line)
                
                # Support both flat jsonl and grouped [query_id, [paragraphs]] format
                if isinstance(line_data, list) and len(line_data) == 2 and isinstance(line_data[1], list):
                    items = line_data[1]
                else:
                    items = [line_data]
                    
                for item in items:
                    # EXAM format
                    if 'exam_grades' in item:
                        docid = str(item['paragraph_id'])
                        judgments = item.get('paragraph_data', {}).get('judgments', [])
                        if not judgments:
                            continue
                        qid = str(judgments[0]['query'])
                        human_score = int(judgments[0]['relevance'])
                        
                        grades = item['exam_grades']
                        if not grades: continue
                        ratings = grades[0].get('self_ratings', [])
                        if not ratings: continue
                        
                        covered = sum(1 for r in ratings if r >= 4)
                        total = len(ratings)
                        model_score = round((covered / total) * 3) if total > 0 else 0
                        
                        data[f"{qid}_{docid}"] = {
                            'human_score': human_score,
                            'model_score': model_score,
                            'query_text': qid,
                            'raw_output': json.dumps(grades[0])
                        }
                    else:
                        qid = str(item['query_id'])
                        docid = str(item['corpus_id'])
                        human_score = int(item['original_qrel_score'])
                        model_score = extract_score(item.get('model_output', item.get('gemini_output', '')))
                        
                        data[f"{qid}_{docid}"] = {
                            'human_score': human_score,
                            'model_score': model_score,
                            'query_text': item.get('query_text', ''),
                            'raw_output': item.get('model_output', item.get('gemini_output', ''))
                        }
            except Exception:
                pass
    return data

def compare_models(file1, file2):
    print(f"Loading Model 1: {file1}")
    data1 = load_annotations(file1)
    print(f"Loading Model 2: {file2}")
    data2 = load_annotations(file2)
    
    # Find intersection of query-doc pairs
    common_keys = set(data1.keys()).intersection(set(data2.keys()))
    print(f"\nFound {len(common_keys)} shared judgments between the two files.\n")
    
    if not common_keys:
        print("No common data points to compare.")
        return

    m1_vs_human_exact = 0
    m2_vs_human_exact = 0
    m1_vs_m2_exact = 0
    
    m1_human_errors = []
    m2_human_errors = []
    m1_m2_errors = []

    m1_scores = []
    m2_scores = []
    human_scores = []
    
    for key in common_keys:
        h_score = data1[key]['human_score']
        m1_score = data1[key]['model_score']
        m2_score = data2[key]['model_score']
        
        if m1_score is None or m2_score is None:
            continue
            
        m1_scores.append(m1_score)
        m2_scores.append(m2_score)
        human_scores.append(h_score)
        
        # M1 vs Human
        if m1_score == h_score:
            m1_vs_human_exact += 1
        else:
            m1_human_errors.append(abs(m1_score - h_score))
            
        # M2 vs Human
        if m2_score == h_score:
            m2_vs_human_exact += 1
        else:
            m2_human_errors.append(abs(m2_score - h_score))
            
        # M1 vs M2
        if m1_score == m2_score:
            m1_vs_m2_exact += 1
        else:
            m1_m2_errors.append(abs(m1_score - m2_score))

    n = len(m1_scores)
    if n == 0:
        print("No valid scores to compare (could not parse scores).")
        return

    print("=" * 50)
    print("AGREEMENT METRICS")
    print("=" * 50)
    print(f"Model 1 vs Human Exact Match: {m1_vs_human_exact / n * 100:.2f}% ({m1_vs_human_exact}/{n})")
    print(f"Model 2 vs Human Exact Match: {m2_vs_human_exact / n * 100:.2f}% ({m2_vs_human_exact}/{n})")
    print(f"Model 1 vs Model 2 Exact Match: {m1_vs_m2_exact / n * 100:.2f}% ({m1_vs_m2_exact}/{n})")
    print()
    
    print("=" * 50)
    print("MEAN ABSOLUTE ERROR (MAE)")
    print("=" * 50)
    print(f"Model 1 vs Human MAE: {np.mean([abs(a - b) for a, b in zip(m1_scores, human_scores)]):.3f}")
    print(f"Model 2 vs Human MAE: {np.mean([abs(a - b) for a, b in zip(m2_scores, human_scores)]):.3f}")
    print(f"Model 1 vs Model 2 MAE: {np.mean([abs(a - b) for a, b in zip(m1_scores, m2_scores)]):.3f}")
    print()

    # Calculate Pearson Correlation
    print("=" * 50)
    print("PEARSON CORRELATION")
    print("=" * 50)
    # Handle cases with zero variance
    if np.std(m1_scores) > 0 and np.std(human_scores) > 0:
        print(f"Model 1 vs Human Correlation: {np.corrcoef(m1_scores, human_scores)[0, 1]:.3f}")
    if np.std(m2_scores) > 0 and np.std(human_scores) > 0:
        print(f"Model 2 vs Human Correlation: {np.corrcoef(m2_scores, human_scores)[0, 1]:.3f}")
    if np.std(m1_scores) > 0 and np.std(m2_scores) > 0:
        print(f"Model 1 vs Model 2 Correlation: {np.corrcoef(m1_scores, m2_scores)[0, 1]:.3f}")
    print()

    # Detailed Disagreements
    print("=" * 50)
    print("TOP DISAGREEMENTS (Model 1 vs Model 2)")
    print("=" * 50)
    disagreements = []
    for key in common_keys:
        m1_score = data1[key]['model_score']
        m2_score = data2[key]['model_score']
        if m1_score is not None and m2_score is not None and m1_score != m2_score:
            diff = abs(m1_score - m2_score)
            disagreements.append((diff, key, m1_score, m2_score, data1[key]['human_score']))
            
    # Sort by largest difference
    disagreements.sort(reverse=True, key=lambda x: x[0])
    
    for i, (diff, key, m1, m2, h) in enumerate(disagreements[:5]):
        qid, docid = key.split('_')
        print(f"Rank {i+1}: Query {qid} / Doc {docid}")
        print(f"  Query text: {data1[key]['query_text']}")
        print(f"  Human Score: {h}")
        print(f"  Model 1 Score: {m1}")
        print(f"  Model 2 Score: {m2}")
        print("-" * 30)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Compare two Gemini model annotation outputs.")
    parser.add_argument("--model1", type=str, default="results/gemini-3_8-flash_annotations.jsonl", help="Path to first model's JSONL")
    parser.add_argument("--model2", type=str, default="results/gemini-3_7-flash_annotations.jsonl", help="Path to second model's JSONL")
    
    args = parser.parse_args()
    compare_models(args.model1, args.model2)
