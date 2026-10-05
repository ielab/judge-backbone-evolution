import json
import glob
import re
import os
import itertools
import numpy as np
import argparse

def extract_score(text):
    text = str(text).strip()

    match = re.search(
        r"final\s*score\s*(?:for\s+this\s+passage\s*)?(?:is\s*)?:?\s*[*]*([0-3](?:\.\d+)?)[*]*",
        text,
        re.IGNORECASE
    )
    if match:
        score = float(match.group(1))
        return int(score) if score.is_integer() else None

    match = re.search(
        r"overall(?:\s*score)?\s*(?:\(O\))?\s*[:=]\s*[*]*([0-3](?:\.\d+)?)[*]*",
        text,
        re.IGNORECASE
    )
    if match:
        score = float(match.group(1))
        return int(score) if score.is_integer() else None

    matches = re.findall(
        r"(?:^|\n)\s*#{0,6}\s*O\s*"
        r"(?:\(\s*Final\s+Score\s*\))?\s*[:=]\s*"
        r"\**([0-3](?:\.\d+)?)\**",
        text,
        re.IGNORECASE
    )
    if matches:
        score = float(matches[-1])
        return int(score) if score.is_integer() else None

    return None

import gzip

def load_annotations(filepath):
    data = {}
    opener = gzip.open if str(filepath).endswith('.gz') else open
    with opener(filepath, 'rt') as f:
        try:
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
                                model_score = round((covered / total) * 3) if total > 0 else 0
                            elif ratings and all(isinstance(r, (int, float)) for r in ratings):
                                covered = sum(1 for r in ratings if r >= 4)
                                total = len(ratings)
                                model_score = round((covered / total) * 3) if total > 0 else 0
                            else:
                                continue
                            
                            data[f"{qid}_{docid}"] = {
                                'human_score': human_score,
                                'model_score': model_score,
                            }
                        else:
                            qid = item['query_id']
                            docid = item['corpus_id']
                            human_score = int(item['original_qrel_score'])
                            
                            output = item.get('model_output', item.get('gemini_output', ''))
                            model_score = extract_score(output)
                            
                            if model_score is not None:
                                data[f"{qid}_{docid}"] = {
                                    'human_score': human_score,
                                    'model_score': model_score,
                                }
                except Exception:
                    pass
        except EOFError:
            pass
    return data

def main():
    parser = argparse.ArgumentParser(description="Analyze all pairs of model annotations.")
    parser.add_argument("--pattern", type=str, default="results/gemini-*-flash_annotations.jsonl", help="Glob pattern for finding annotation files to compare.")
    args = parser.parse_args()

    files = glob.glob(args.pattern)
    if not files:
        print(f"No annotation files found matching pattern: {args.pattern}")
        return

    models = {}
    model_names = []
    
    for f in sorted(files):
        name = os.path.basename(f).replace('_annotations.jsonl', '').replace('_', '.')
        print(f"Loading {name}...")
        models[name] = load_annotations(f)
        model_names.append(name)
        
    print(f"\nDiscovered {len(model_names)} models: {', '.join(model_names)}")
    
    print("\n" + "="*60)
    print("BASELINE PERFORMANCE (Vs. Human)")
    print("="*60)
    
    baseline_metrics = {}
    for name in model_names:
        data = models[name]
        human_scores = []
        model_scores = []
        exact_matches = 0
        
        for key, val in data.items():
            h_score = val['human_score']
            m_score = val['model_score']
            human_scores.append(h_score)
            model_scores.append(m_score)
            if h_score == m_score:
                exact_matches += 1
                
        n = len(human_scores)
        if n == 0: continue
        
        mae = np.mean([abs(a - b) for a, b in zip(model_scores, human_scores)])
        corr = 0
        if np.std(model_scores) > 0 and np.std(human_scores) > 0:
            corr = np.corrcoef(model_scores, human_scores)[0, 1]
            
        exact_pct = exact_matches / n * 100
        baseline_metrics[name] = {
            "n": n,
            "exact": exact_pct,
            "mae": mae,
            "corr": corr
        }
        print(f"[{name}] (N={n})")
        print(f"  Exact Match: {exact_pct:.2f}%")
        print(f"  MAE:         {mae:.3f}")
        print(f"  Pearson r:   {corr:.3f}\n")
        
    print("\n" + "="*60)
    print("ALL-PAIRS AGREEMENT (Exact Match %)")
    print("="*60)
    
    pairs = list(itertools.combinations(model_names, 2))
    
    for name1, name2 in pairs:
        d1 = models[name1]
        d2 = models[name2]
        
        shared_keys = set(d1.keys()).intersection(set(d2.keys()))
        if not shared_keys: continue
        
        exact = sum(1 for k in shared_keys if d1[k]['model_score'] == d2[k]['model_score'])
        pct = exact / len(shared_keys) * 100
        
        mae = np.mean([abs(d1[k]['model_score'] - d2[k]['model_score']) for k in shared_keys])
        
        m1_scores = [d1[k]['model_score'] for k in shared_keys]
        m2_scores = [d2[k]['model_score'] for k in shared_keys]
        corr = 0
        if np.std(m1_scores) > 0 and np.std(m2_scores) > 0:
            corr = np.corrcoef(m1_scores, m2_scores)[0, 1]
            
        print(f"{name1} <--> {name2} (N={len(shared_keys)})")
        print(f"  Exact Match: {pct:.2f}%")
        print(f"  MAE:         {mae:.3f}")
        print(f"  Pearson r:   {corr:.3f}\n")
        
    print("\n" + "="*60)
    print("ALL-PAIRS REGRESSIONS (Baseline Correct -> New Model Wrong)")
    print("="*60)
    
    for name1 in model_names:
        for name2 in model_names:
            if name1 == name2: continue
            
            d1 = models[name1]
            d2 = models[name2]
            
            shared_keys = set(d1.keys()).intersection(set(d2.keys()))
            if not shared_keys: continue
            
            regressions = sum(1 for k in shared_keys if d1[k]['model_score'] == d1[k]['human_score'] and d2[k]['model_score'] != d2[k]['human_score'])
            reg_rate = regressions / len(shared_keys) * 100
            
            print(f"Baseline: {name1} | New: {name2}")
            print(f"  Regressions: {regressions} ({reg_rate:.2f}% of N={len(shared_keys)})\n")
            
    # Generate Report Name
    pattern_name = os.path.basename(args.pattern).replace('.jsonl', '').replace('*', 'all')
    os.makedirs("analysis", exist_ok=True)
    output_filename = os.path.join("analysis", f"all_pairs_analysis_report_{pattern_name}.md")
    
    print(f"\nGenerating {output_filename}...")
    with open(output_filename, 'w') as f:
        f.write("# All-Pairs Model Comparison\n\n")
        
        f.write("## Baseline Performance (vs. Human)\n\n")
        f.write("| Model | N | Exact Match | MAE | Pearson r |\n")
        f.write("| :--- | :--- | :--- | :--- | :--- |\n")
        for name in model_names:
            m = baseline_metrics[name]
            f.write(f"| {name} | {m['n']} | {m['exact']:.2f}% | {m['mae']:.3f} | {m['corr']:.3f} |\n")
            
        f.write("\n## Model-to-Model Agreement (Exact Match %)\n\n")
        f.write("| " + " | ".join([""] + model_names) + " |\n")
        f.write("| " + " | ".join([":---"] * (len(model_names) + 1)) + " |\n")
        for name1 in model_names:
            row = [name1]
            for name2 in model_names:
                if name1 == name2:
                    row.append("-")
                else:
                    d1 = models[name1]
                    d2 = models[name2]
                    shared = set(d1.keys()).intersection(set(d2.keys()))
                    if shared:
                        exact = sum(1 for k in shared if d1[k]['model_score'] == d2[k]['model_score'])
                        row.append(f"{exact/len(shared)*100:.1f}%")
                    else:
                        row.append("N/A")
            f.write("| " + " | ".join(row) + " |\n")
            
        f.write("\n## Regression Rates (Row=Baseline, Col=New Model)\n")
        f.write("*Percentage of times the Baseline got the EXACT human score, but the New Model got it wrong.*\n\n")
        f.write("| Baseline \\ New " + " | ".join([""] + model_names) + " |\n")
        f.write("| " + " | ".join([":---"] * (len(model_names) + 1)) + " |\n")
        for name1 in model_names:
            row = [name1]
            for name2 in model_names:
                if name1 == name2:
                    row.append("-")
                else:
                    d1 = models[name1]
                    d2 = models[name2]
                    shared = set(d1.keys()).intersection(set(d2.keys()))
                    if shared:
                        reg = sum(1 for k in shared if d1[k]['model_score'] == d1[k]['human_score'] and d2[k]['model_score'] != d2[k]['human_score'])
                        row.append(f"{reg/len(shared)*100:.1f}% ({reg})")
                    else:
                        row.append("N/A")
            f.write("| " + " | ".join(row) + " |\n")
            
    print(f"Done! Report saved to {output_filename}")

if __name__ == "__main__":
    main()
