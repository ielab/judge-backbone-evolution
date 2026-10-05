import gzip
import json
import sys
from pathlib import Path

# Add rubric-grading-workbench to path
sys.path.append(str(Path('../rubric-grading-workbench').resolve()))

from exam_pp.data_model import parseQueryWithFullParagraphs, writeQueryWithFullParagraphs, QueryWithFullParagraphList

def main():
    original_file = Path("data/questions-rate-dl19-gpt-5-mini.jsonl.gz")
    backup_file = Path("data/questions-rate-dl19-gpt-5-mini-backup.jsonl.gz")
    out_file = Path("data/questions-rate-dl19-gpt-5-mini-merged.jsonl.gz")
    
    print("Loading backup...")
    backup_queries = list(parseQueryWithFullParagraphs(backup_file))
    
    backup_dict = {}
    for q in backup_queries:
        if q.queryId not in backup_dict:
            backup_dict[q.queryId] = {}
        for p in q.paragraphs:
            backup_dict[q.queryId][p.paragraph_id] = p
            
    print("Loading original...")
    original_queries = list(parseQueryWithFullParagraphs(original_file))
    
    replaced = 0
    for q in original_queries:
        for p in q.paragraphs:
            if q.queryId in backup_dict and p.paragraph_id in backup_dict[q.queryId]:
                backup_p = backup_dict[q.queryId][p.paragraph_id]
                # If backup has grades, use them
                if backup_p.exam_grades is not None and len(backup_p.exam_grades) > 0:
                    p.exam_grades = backup_p.exam_grades
                    p.grades = backup_p.grades
                    replaced += 1
                    
    print(f"Replaced {replaced} paragraphs with backup grades.")
    
    print("Writing merged file...")
    writeQueryWithFullParagraphs(out_file, original_queries)
    print("Done.")

if __name__ == "__main__":
    main()
