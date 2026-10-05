import json
import gzip
import ir_datasets
from pathlib import Path

def main():
    dataset_id = "msmarco-passage/trec-dl-2020/judged"
    print(f"Loading {dataset_id}...")
    dataset = ir_datasets.load(dataset_id)
    
    out_dir = Path("data")
    out_dir.mkdir(exist_ok=True)
    
    queries_file = out_dir / "dl20-queries.json"
    runs_file = out_dir / "trecDL2020-qrels-runs-with-text.jsonl.gz"
    
    print("Exporting queries...")
    queries_dict = {}
    for query in dataset.queries_iter():
        queries_dict[query.query_id] = query.text
        
    with open(queries_file, 'w') as f:
        json.dump(queries_dict, f, indent=2)
        
    print("Exporting qrels as runs-with-text...")
    # EXAM expects FullParagraphData format
    
    # Preload passages needed
    qrels = list(dataset.qrels_iter())
    doc_ids = {qrel.doc_id for qrel in qrels}
    
    docs_dict = {}
    print("Loading required passages from corpus (this may take a bit)...")
    for doc in dataset.docs_iter():
        if doc.doc_id in doc_ids:
            docs_dict[doc.doc_id] = doc.text
            if len(docs_dict) % 1000 == 0:
                print(f"Loaded {len(docs_dict)} passages...")
            if len(docs_dict) == len(doc_ids):
                break
                
    # Generate FullParagraphData
    print("Writing FullParagraphData...")
    
    from collections import defaultdict
    qrels_by_query = defaultdict(list)
    for qrel in qrels:
        qrels_by_query[qrel.query_id].append(qrel)
        
    with gzip.open(runs_file, 'wt') as f:
        for query_id, query_qrels in qrels_by_query.items():
            paragraphs_list = []
            for qrel in query_qrels:
                doc_id = qrel.doc_id
                score = qrel.relevance
                text = docs_dict.get(doc_id, "")
                
                judgment = {
                    "paragraphId": doc_id,
                    "query": query_id,
                    "relevance": score,
                    "titleQuery": query_id
                }
                
                ranking = {
                    "method": "qrels",
                    "paragraphId": doc_id,
                    "queryId": query_id,
                    "rank": 1,
                    "score": float(score)
                }
                
                data = {
                    "paragraph_id": doc_id,
                    "text": text,
                    "paragraph": None,
                    "paragraph_data": {
                        "judgments": [judgment],
                        "rankings": [ranking]
                    },
                    "exam_grades": None,
                    "grades": None
                }
                paragraphs_list.append(data)
                
            line_data = [query_id, paragraphs_list]
            f.write(json.dumps(line_data) + '\n')
            
    print(f"Done. Files saved to {out_dir}")

if __name__ == "__main__":
    main()
