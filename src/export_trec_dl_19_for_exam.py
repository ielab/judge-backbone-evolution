import json
import gzip
import ir_datasets
from pathlib import Path

def main():
    dataset_id = "msmarco-passage/trec-dl-2019/judged"
    print(f"Loading {dataset_id}...")
    dataset = ir_datasets.load(dataset_id)
    
    out_dir = Path("data")
    out_dir.mkdir(exist_ok=True)
    
    queries_file = out_dir / "dl19-queries.json"
    runs_file = out_dir / "trecDL2019-qrels-runs-with-text.jsonl.gz"
    
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
    with gzip.open(runs_file, 'wt') as f:
        for qrel in qrels:
            query_id = qrel.query_id
            doc_id = qrel.doc_id
            score = qrel.relevance
            
            text = docs_dict.get(doc_id, "")
            
            # Construct a ParagraphData containing Judgments
            judgment = {
                "paragraphId": doc_id,
                "query": query_id,
                "relevance": score,
                "titleQuery": query_id
            }
            
            # And a dummy ranking entry since EXAM might need it
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
            
            f.write(json.dumps(data) + '\n')
            
    print(f"Done. Files saved to {out_dir}")

if __name__ == "__main__":
    main()
