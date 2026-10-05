import gzip
import json
from exam_pp.data_model import parseQueryWithFullParagraphs, dumpQueryWithFullParagraphList, QueryWithFullParagraphList

def extract_failed():
    queries = parseQueryWithFullParagraphs("data/questions-rate-dl19-gpt-5-mini.jsonl.gz")
    
    with gzip.open("data/trecDL2019-qrels-runs-with-text-failed-gpt-5-mini.jsonl.gz", "wt", encoding='utf-8') as f_out:
        total_failed_paras = 0
        for q in queries:
            failed_paras = []
            for p in q.paragraphs:
                failed = False
                
                # Check for errors in exam_grades (QuestionPrompt)
                if p.exam_grades:
                    for eg in p.exam_grades:
                        if eg.llm_response_errors and len(eg.llm_response_errors) > 0:
                            failed = True
                else:
                    failed = True
                    
                # Check direct grading if present
                if p.grades:
                    for g in p.grades:
                        if g.llm_response_error is not None:
                            failed = True
                            
                if failed:
                    # Reset grades so it can be re-run cleanly
                    p.exam_grades = None
                    p.grades = None
                    failed_paras.append(p)
                    total_failed_paras += 1
                    
            if failed_paras:
                new_q = QueryWithFullParagraphList(queryId=q.queryId, paragraphs=failed_paras)
                f_out.write(dumpQueryWithFullParagraphList(new_q))
                
        print(f"Extracted {total_failed_paras} failed paragraphs for retry.")

if __name__ == "__main__":
    extract_failed()
