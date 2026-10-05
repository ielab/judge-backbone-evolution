# All-Pairs Model Comparison

## Baseline Performance (vs. Human)

| Model | N | Exact Match | MAE | Pearson r |
| :--- | :--- | :--- | :--- | :--- |
| Qwen.Qwen1.5-7B-Chat | 9252 | 26.92% | 1.568 | 0.304 |
| Qwen.Qwen2-7B-Instruct | 9172 | 45.91% | 0.805 | 0.483 |
| Qwen.Qwen2.5-7B-Instruct | 9260 | 58.12% | 0.553 | 0.535 |
| Qwen.Qwen3-8B | 9260 | 42.76% | 0.749 | 0.547 |
| Qwen.Qwen3.5-9B | 9260 | 36.09% | 0.871 | 0.544 |

## Model-to-Model Agreement (Exact Match %)

|  | Qwen.Qwen1.5-7B-Chat | Qwen.Qwen2-7B-Instruct | Qwen.Qwen2.5-7B-Instruct | Qwen.Qwen3-8B | Qwen.Qwen3.5-9B |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Qwen.Qwen1.5-7B-Chat | - | 35.6% | 26.7% | 33.4% | 41.4% |
| Qwen.Qwen2-7B-Instruct | 35.6% | - | 53.3% | 57.2% | 50.0% |
| Qwen.Qwen2.5-7B-Instruct | 26.7% | 53.3% | - | 53.4% | 42.5% |
| Qwen.Qwen3-8B | 33.4% | 57.2% | 53.4% | - | 62.3% |
| Qwen.Qwen3.5-9B | 41.4% | 50.0% | 42.5% | 62.3% | - |

## Regression Rates (Row=Baseline, Col=New Model)
*Percentage of times the Baseline got the EXACT human score, but the New Model got it wrong.*

| Baseline \ New  | Qwen.Qwen1.5-7B-Chat | Qwen.Qwen2-7B-Instruct | Qwen.Qwen2.5-7B-Instruct | Qwen.Qwen3-8B | Qwen.Qwen3.5-9B |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Qwen.Qwen1.5-7B-Chat | - | 6.4% (590) | 6.4% (592) | 7.6% (701) | 9.5% (876) |
| Qwen.Qwen2-7B-Instruct | 25.3% (2323) | - | 9.7% (886) | 15.2% (1394) | 20.6% (1887) |
| Qwen.Qwen2.5-7B-Instruct | 37.6% (3478) | 21.9% (2012) | - | 25.3% (2346) | 32.2% (2984) |
| Qwen.Qwen3-8B | 23.4% (2167) | 12.1% (1112) | 10.0% (924) | - | 15.3% (1420) |
| Qwen.Qwen3.5-9B | 18.7% (1727) | 10.8% (992) | 10.2% (944) | 8.7% (802) | - |
