import json
import gzip
from collections import defaultdict
from pathlib import Path

def main():
    runs_file = Path("data/trecDL2019-qrels-runs-with-text.jsonl.gz")
    out_file = Path("data/trecDL2019-qrels-runs-with-text-grouped.jsonl.gz")
    
    query_to_docs = defaultdict(list)
    
    print(f"Reading {runs_file}...")
    with gzip.open(runs_file, 'rt') as f:
        for line in f:
            if not line.strip(): continue
            data = json.loads(line)
            # Find query ID
            query_id = None
            if data.get('paragraph_data') and data['paragraph_data'].get('judgments'):
                query_id = data['paragraph_data']['judgments'][0]['query']
                
            if query_id:
                query_to_docs[query_id].append(data)
                
    print(f"Writing to {out_file}...")
    with gzip.open(out_file, 'wt') as f:
        for query_id, docs in query_to_docs.items():
            f.write(json.dumps([query_id, docs]) + '\n')
            
    print("Done formatting.")

if __name__ == "__main__":
    main()
