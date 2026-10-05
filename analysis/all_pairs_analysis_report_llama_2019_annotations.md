# All-Pairs Model Comparison

## Baseline Performance (vs. Human)

| Model | N | Exact Match | MAE | Pearson r |
| :--- | :--- | :--- | :--- | :--- |
| meta-llama.Llama-2-7b-chat-hf | 8451 | 21.99% | 1.219 | 0.250 |
| meta-llama.Llama-3.1-8B-Instruct | 9097 | 36.01% | 1.127 | 0.455 |
| meta-llama.Meta-Llama-3-8B-Instruct | 9260 | 22.95% | 1.186 | 0.425 |

## Model-to-Model Agreement (Exact Match %)

|  | meta-llama.Llama-2-7b-chat-hf | meta-llama.Llama-3.1-8B-Instruct | meta-llama.Meta-Llama-3-8B-Instruct |
| :--- | :--- | :--- | :--- |
| meta-llama.Llama-2-7b-chat-hf | - | 30.4% | 45.6% |
| meta-llama.Llama-3.1-8B-Instruct | 30.4% | - | 49.8% |
| meta-llama.Meta-Llama-3-8B-Instruct | 45.6% | 49.8% | - |

## Regression Rates (Row=Baseline, Col=New Model)
*Percentage of times the Baseline got the EXACT human score, but the New Model got it wrong.*

| Baseline \ New  | meta-llama.Llama-2-7b-chat-hf | meta-llama.Llama-3.1-8B-Instruct | meta-llama.Meta-Llama-3-8B-Instruct |
| :--- | :--- | :--- | :--- |
| meta-llama.Llama-2-7b-chat-hf | - | 13.1% (1088) | 11.7% (986) |
| meta-llama.Llama-3.1-8B-Instruct | 27.0% (2239) | - | 21.0% (1912) |
| meta-llama.Meta-Llama-3-8B-Instruct | 12.2% (1028) | 8.0% (726) | - |
