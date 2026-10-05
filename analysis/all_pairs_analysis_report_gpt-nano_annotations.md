# All-Pairs Model Comparison

## Baseline Performance (vs. Human)

| Model | N | Exact Match | MAE | Pearson r |
| :--- | :--- | :--- | :--- | :--- |
| gpt-4.1-nano | 9259 | 35.87% | 3.517 | 0.023 |
| gpt-5-nano | 9260 | 41.02% | 0.741 | 0.564 |
| gpt-5.4-nano | 9260 | 51.09% | 0.668 | 0.560 |

## Model-to-Model Agreement (Exact Match %)

|  | gpt-4.1-nano | gpt-5-nano | gpt-5.4-nano |
| :--- | :--- | :--- | :--- |
| gpt-4.1-nano | - | 49.7% | 42.3% |
| gpt-5-nano | 49.7% | - | 55.9% |
| gpt-5.4-nano | 42.3% | 55.9% | - |

## Regression Rates (Row=Baseline, Col=New Model)
*Percentage of times the Baseline got the EXACT human score, but the New Model got it wrong.*

| Baseline \ New  | gpt-4.1-nano | gpt-5-nano | gpt-5.4-nano |
| :--- | :--- | :--- | :--- |
| gpt-4.1-nano | - | 14.8% (1372) | 13.1% (1215) |
| gpt-5-nano | 20.0% (1848) | - | 11.3% (1049) |
| gpt-5.4-nano | 28.3% (2624) | 21.4% (1982) | - |
