import json
import gzip
import glob
import os

def main():
    regression_files = glob.glob("analysis/regressions_gemini-*_exam.jsonl")
    print(f"Found {len(regression_files)} regression files.")
    
    regression_pairs = set()
    
    for fpath in regression_files:
        with open(fpath, "r") as f:
            for line in f:
                data = json.loads(line)
                q_id = str(data.get("query_id"))
                c_id = str(data.get("corpus_id"))
                regression_pairs.add((q_id, c_id))
                
    print(f"Total unique regression (query_id, corpus_id) pairs: {len(regression_pairs)}")
    
    input_file = "data/trecDL2019-qrels-runs-with-text.jsonl.gz"
    out_dir = "data/dl19-exam-thoughts-regressions"
    os.makedirs(out_dir, exist_ok=True)
    
    output_file = os.path.join(out_dir, "trecDL2019-regressions-only-runs-with-text.jsonl.gz")
    
    retained_paragraphs = 0
    total_paragraphs = 0
    
    with gzip.open(input_file, "rt", encoding="utf-8") as fin:
        with gzip.open(output_file, "wt", encoding="utf-8") as fout:
            for line in fin:
                data = json.loads(line)
                query_id = str(data[0])
                paragraphs = data[1]
                
                filtered_paragraphs = []
                for p_dict in paragraphs:
                    total_paragraphs += 1
                    p_id = str(p_dict.get("paragraph_id"))
                    
                    if (query_id, p_id) in regression_pairs:
                        # Keep this paragraph, filter judgments and rankings to just this query
                        if p_dict.get("paragraph_data"):
                            p_dict["paragraph_data"]["judgments"] = [
                                j for j in p_dict["paragraph_data"].get("judgments", [])
                                if str(j.get("query")) == query_id
                            ]
                            p_dict["paragraph_data"]["rankings"] = [
                                r for r in p_dict["paragraph_data"].get("rankings", [])
                                if str(r.get("queryId")) == query_id
                            ]
                        filtered_paragraphs.append(p_dict)
                        retained_paragraphs += 1
                        
                if filtered_paragraphs:
                    # Write out the query and its filtered paragraphs
                    fout.write(json.dumps([query_id, filtered_paragraphs]) + "\n")

                    
    print(f"Filtered {input_file}")
    print(f"Retained {retained_paragraphs} out of {total_paragraphs} paragraphs.")
    print(f"Output saved to {output_file}")

if __name__ == "__main__":
    main()
