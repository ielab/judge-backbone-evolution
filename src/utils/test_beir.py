import time
from datasets import load_dataset

start = time.time()
print("Loading BeIR corpus...")
corpus = load_dataset("BeIR/msmarco", "corpus", split="corpus")
print(f"Corpus loaded in {time.time() - start:.2f}s. Number of docs: {len(corpus)}")

print("Loading BeIR queries...")
queries = load_dataset("BeIR/msmarco", "queries", split="queries")
print(f"Queries loaded in {time.time() - start:.2f}s. Number of queries: {len(queries)}")

# Try to find a document
doc_id = "2674124" # An example corpus id
print(f"Finding doc {doc_id}...")
# Fast lookup using HuggingFace dataset dictionary / index
corpus = corpus.to_pandas().set_index('_id')
print("Pandas index built.")
if doc_id in corpus.index:
    print(corpus.loc[doc_id]['text'])
