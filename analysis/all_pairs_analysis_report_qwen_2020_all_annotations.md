# All-Pairs Model Comparison

## Baseline Performance (vs. Human)

| Model | N | Exact Match | MAE | Pearson r |
| :--- | :--- | :--- | :--- | :--- |
| Qwen.Qwen1.5-7B-Chat.trec-dl-2020 | 11364 | 33.21% | 1.559 | 0.280 |
| Qwen.Qwen2-7B-Instruct.trec-dl-2020 | 11358 | 49.06% | 0.767 | 0.442 |
| Qwen.Qwen2.5-7B-Instruct.trec-dl-2020 | 11386 | 59.45% | 0.535 | 0.445 |
| Qwen.Qwen3-8B.trec-dl-2020 | 11386 | 48.76% | 0.685 | 0.532 |
| Qwen.Qwen3.5-9B.trec-dl-2020 | 11386 | 44.03% | 0.790 | 0.523 |

## Model-to-Model Agreement (Exact Match %)

|  | Qwen.Qwen1.5-7B-Chat.trec-dl-2020 | Qwen.Qwen2-7B-Instruct.trec-dl-2020 | Qwen.Qwen2.5-7B-Instruct.trec-dl-2020 | Qwen.Qwen3-8B.trec-dl-2020 | Qwen.Qwen3.5-9B.trec-dl-2020 |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Qwen.Qwen1.5-7B-Chat.trec-dl-2020 | - | 38.5% | 32.7% | 34.2% | 40.2% |
| Qwen.Qwen2-7B-Instruct.trec-dl-2020 | 38.5% | - | 58.0% | 61.6% | 53.6% |
| Qwen.Qwen2.5-7B-Instruct.trec-dl-2020 | 32.7% | 58.0% | - | 58.0% | 49.7% |
| Qwen.Qwen3-8B.trec-dl-2020 | 34.2% | 61.6% | 58.0% | - | 63.2% |
| Qwen.Qwen3.5-9B.trec-dl-2020 | 40.2% | 53.6% | 49.7% | 63.2% | - |

## Regression Rates (Row=Baseline, Col=New Model)
*Percentage of times the Baseline got the EXACT human score, but the New Model got it wrong.*

| Baseline \ New  | Qwen.Qwen1.5-7B-Chat.trec-dl-2020 | Qwen.Qwen2-7B-Instruct.trec-dl-2020 | Qwen.Qwen2.5-7B-Instruct.trec-dl-2020 | Qwen.Qwen3-8B.trec-dl-2020 | Qwen.Qwen3.5-9B.trec-dl-2020 |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Qwen.Qwen1.5-7B-Chat.trec-dl-2020 | - | 6.7% (757) | 5.3% (600) | 7.6% (863) | 9.7% (1105) |
| Qwen.Qwen2-7B-Instruct.trec-dl-2020 | 22.5% (2549) | - | 8.0% (909) | 11.7% (1333) | 16.5% (1877) |
| Qwen.Qwen2.5-7B-Instruct.trec-dl-2020 | 31.5% (3584) | 18.4% (2089) | - | 20.3% (2315) | 24.8% (2826) |
| Qwen.Qwen3-8B.trec-dl-2020 | 23.2% (2632) | 11.5% (1301) | 9.6% (1098) | - | 13.9% (1584) |
| Qwen.Qwen3.5-9B.trec-dl-2020 | 20.5% (2333) | 11.5% (1310) | 9.4% (1070) | 9.2% (1045) | - |
