import json
import numpy as np
import os
import re
from itertools import combinations
from collections import defaultdict

def extract_score(text):
    text = str(text).strip()
    match = re.search(r"final\s*score:?\s*[*]*([0-3])[*]*", text, re.IGNORECASE)
    if match: return int(match.group(1))
    matches = re.findall(r"\b([0-3])\b", text)
    if matches: return int(matches[-1])
    return None

import gzip

def load_annotations(filepath):
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
                        if not ratings: continue
                        
                        covered = sum(1 for r in ratings if r >= 4)
                        total = len(ratings)
                        model_score = round((covered / total) * 3) if total > 0 else 0
                        
                        data[f"{qid}_{docid}"] = {
                            'human_score': human_score,
                            'model_score': model_score,
                        }
                    else:
                        qid = item['query_id']
                        docid = item['corpus_id']
                        human_score = int(item['original_qrel_score'])
                        model_score = extract_score(item.get('model_output', item.get('gemini_output', '')))
                        
                        data[f"{qid}_{docid}"] = {
                            'human_score': human_score,
                            'model_score': model_score,
                        }
            except Exception:
                pass
    return data

def calc_metrics(data):
    exact = 0
    m_scores = []
    h_scores = []
    
    for key, val in data.items():
        if val['model_score'] is None: continue
        m_scores.append(val['model_score'])
        h_scores.append(val['human_score'])
        if val['model_score'] == val['human_score']:
            exact += 1
            
    n = len(m_scores)
    if n == 0: return None
    
    exact_pct = exact / n * 100
    mae = np.mean([abs(a - b) for a, b in zip(m_scores, h_scores)])
    
    pearson = 0
    if np.std(m_scores) > 0 and np.std(h_scores) > 0:
        pearson = np.corrcoef(m_scores, h_scores)[0, 1]
        
    return exact_pct, mae, pearson

def jaccard(set1, set2):
    if len(set1) == 0 and len(set2) == 0: return 1.0
    return len(set1.intersection(set2)) / len(set1.union(set2))

def main():
    models = ["gemini-2.5-flash", "gemini-3.5-flash", "gemini-3.6-flash", "gemini-3.7-flash", "gemini-3.8-flash"]
    runs = [1, 2, 3]
    output_dir = "results/repeats_no_thinking"
    
    print("="*60)
    print("METRIC VARIANCE ACROSS REPEATS")
    print("="*60)
    
    model_data = defaultdict(dict)
    
    for model in models:
        metrics = []
        for run_id in runs:
            filepath = os.path.join(output_dir, f"{model.replace('.', '_')}_run{run_id}_annotations.jsonl")
            if not os.path.exists(filepath):
                print(f"Warning: {filepath} not found.")
                continue
            
            data = load_annotations(filepath)
            model_data[model][run_id] = data
            
            res = calc_metrics(data)
            if res: metrics.append(res)
            
        if metrics:
            exacts = [m[0] for m in metrics]
            maes = [m[1] for m in metrics]
            pearsons = [m[2] for m in metrics]
            
            print(f"[{model}]")
            print(f"  Exact Match: {np.mean(exacts):.2f}% (±{np.std(exacts):.3f}%)")
            print(f"  MAE:         {np.mean(maes):.3f} (±{np.std(maes):.4f})")
            print(f"  Pearson r:   {np.mean(pearsons):.3f} (±{np.std(pearsons):.4f})")
            print()
            
    print("="*60)
    print("REGRESSION CONSISTENCY (Generational Pairs)")
    print("="*60)
    
    for i in range(len(models)):
        for j in range(i+1, len(models)):
            baseline_model = models[i]
            new_model = models[j]
            
            # Ensure we have data for all 3 runs for both models
            if len(model_data.get(baseline_model, {})) < 3 or len(model_data.get(new_model, {})) < 3:
                continue
                
            regression_sets = []
            
            for run_id in runs:
                data_b = model_data[baseline_model][run_id]
                data_n = model_data[new_model][run_id]
                
                common = set(data_b.keys()).intersection(set(data_n.keys()))
                
                run_regressions = set()
                for key in common:
                    h = data_b[key]['human_score']
                    mb = data_b[key]['model_score']
                    mn = data_n[key]['model_score']
                    if mb == h and mn != h:
                        run_regressions.add(key)
                
                regression_sets.append(run_regressions)
                
            r1, r2, r3 = regression_sets
            sizes = [len(r1), len(r2), len(r3)]
            
            # Intersection across all 3
            inter_all = r1.intersection(r2).intersection(r3)
            union_all = r1.union(r2).union(r3)
            
            j12 = jaccard(r1, r2)
            j13 = jaccard(r1, r3)
            j23 = jaccard(r2, r3)
            mean_jaccard = np.mean([j12, j13, j23])
            
            print(f"[{baseline_model} -> {new_model}]")
            print(f"  Regression Counts across 3 runs: {sizes[0]}, {sizes[1]}, {sizes[2]} (Mean: {np.mean(sizes):.1f} ±{np.std(sizes):.1f})")
            print(f"  Intersection of all 3 sets: {len(inter_all)} items ({(len(inter_all)/np.mean(sizes)*100) if np.mean(sizes) > 0 else 0:.1f}% of mean size)")
            print(f"  Mean Pairwise Jaccard Similarity: {mean_jaccard:.3f}")
            print()
            
if __name__ == "__main__":
    main()
