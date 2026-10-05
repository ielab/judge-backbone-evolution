# Utility & Scratch Scripts

This directory contains temporary scratch scripts and utilities that were used to experiment with APIs, SDKs, or data formats before integrating them into the main evaluation pipeline. 

They do not directly impact the evaluation runs.

### `test_thinking.py`
A basic sanity-check script using the older `google.generativeai` SDK. It sends a simple "what is 2+2" prompt to `gemini-3.8-flash` to verify API connectivity and check if the model responds correctly to "Think step by step" prompts.

### `test_genai.py`
A more advanced test script utilizing the newer `google.genai` SDK. This was used to figure out the exact syntax required to pass `types.ThinkingConfig()` and properly parse the `response.candidates[0].content.parts` array to separate the hidden reasoning `thought` from the final `text` answer.

### `test_beir.py`
A small benchmarking script used to test the fastest way to load the massive 1.6GB `BeIR/msmarco` corpus from Hugging Face. It compares loading the entire corpus into a Pandas DataFrame index for `doc_id` lookups versus other methods. (Ultimately, the main pipeline uses dataset streaming to save memory).

### `parse_form.py`
A lightweight local HTML parsing script using `BeautifulSoup`. It was used to read an HTML artifact from a completely unrelated conversation (NCI Gadi Allocation Application) to extract headings and `M7eMe` div classes, likely parsing web content or a Google Form.
