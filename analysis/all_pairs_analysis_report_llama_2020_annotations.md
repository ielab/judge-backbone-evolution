# All-Pairs Model Comparison

## Baseline Performance (vs. Human)

| Model | N | Exact Match | MAE | Pearson r |
| :--- | :--- | :--- | :--- | :--- |
| meta-llama.Llama-2-7b-chat-hf.trec-dl-2020 | 10634 | 17.65% | 1.348 | 0.239 |
| meta-llama.Llama-3.1-8B-Instruct.trec-dl-2020 | 11231 | 40.76% | 1.131 | 0.411 |
| meta-llama.Meta-Llama-3-8B-Instruct.trec-dl-2020 | 11382 | 23.75% | 1.241 | 0.399 |

## Model-to-Model Agreement (Exact Match %)

|  | meta-llama.Llama-2-7b-chat-hf.trec-dl-2020 | meta-llama.Llama-3.1-8B-Instruct.trec-dl-2020 | meta-llama.Meta-Llama-3-8B-Instruct.trec-dl-2020 |
| :--- | :--- | :--- | :--- |
| meta-llama.Llama-2-7b-chat-hf.trec-dl-2020 | - | 30.0% | 43.2% |
| meta-llama.Llama-3.1-8B-Instruct.trec-dl-2020 | 30.0% | - | 48.4% |
| meta-llama.Meta-Llama-3-8B-Instruct.trec-dl-2020 | 43.2% | 48.4% | - |

## Regression Rates (Row=Baseline, Col=New Model)
*Percentage of times the Baseline got the EXACT human score, but the New Model got it wrong.*

| Baseline \ New  | meta-llama.Llama-2-7b-chat-hf.trec-dl-2020 | meta-llama.Llama-3.1-8B-Instruct.trec-dl-2020 | meta-llama.Meta-Llama-3-8B-Instruct.trec-dl-2020 |
| :--- | :--- | :--- | :--- |
| meta-llama.Llama-2-7b-chat-hf.trec-dl-2020 | - | 8.8% (927) | 9.5% (1011) |
| meta-llama.Llama-3.1-8B-Instruct.trec-dl-2020 | 31.3% (3283) | - | 22.7% (2547) |
| meta-llama.Meta-Llama-3-8B-Instruct.trec-dl-2020 | 15.2% (1620) | 5.6% (629) | - |
