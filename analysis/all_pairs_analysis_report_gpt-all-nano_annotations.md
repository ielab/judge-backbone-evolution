# All-Pairs Model Comparison

## Baseline Performance (vs. Human)

| Model | N | Exact Match | MAE | Pearson r |
| :--- | :--- | :--- | :--- | :--- |
| gpt-4.1-nano | 9256 | 39.44% | 0.748 | 0.402 |
| gpt-5-nano | 9260 | 41.02% | 0.741 | 0.564 |
| gpt-5.4-nano | 9260 | 51.09% | 0.668 | 0.560 |

## Model-to-Model Agreement (Exact Match %)

|  | gpt-4.1-nano | gpt-5-nano | gpt-5.4-nano |
| :--- | :--- | :--- | :--- |
| gpt-4.1-nano | - | 51.4% | 45.7% |
| gpt-5-nano | 51.4% | - | 55.9% |
| gpt-5.4-nano | 45.7% | 55.9% | - |

## Regression Rates (Row=Baseline, Col=New Model)
*Percentage of times the Baseline got the EXACT human score, but the New Model got it wrong.*

| Baseline \ New  | gpt-4.1-nano | gpt-5-nano | gpt-5.4-nano |
| :--- | :--- | :--- | :--- |
| gpt-4.1-nano | - | 16.1% (1490) | 13.6% (1259) |
| gpt-5-nano | 17.7% (1635) | - | 11.3% (1049) |
| gpt-5.4-nano | 25.2% (2337) | 21.4% (1982) | - |
