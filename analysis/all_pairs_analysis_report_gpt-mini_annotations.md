# All-Pairs Model Comparison

## Baseline Performance (vs. Human)

| Model | N | Exact Match | MAE | Pearson r |
| :--- | :--- | :--- | :--- | :--- |
| gpt-4.1-mini | 9260 | 45.78% | 0.654 | 0.583 |
| gpt-4o-mini | 9260 | 55.80% | 0.556 | 0.609 |
| gpt-5-mini | 9260 | 35.63% | 0.821 | 0.557 |
| gpt-5.4-mini | 9260 | 35.13% | 0.825 | 0.578 |

## Model-to-Model Agreement (Exact Match %)

|  | gpt-4.1-mini | gpt-4o-mini | gpt-5-mini | gpt-5.4-mini |
| :--- | :--- | :--- | :--- | :--- |
| gpt-4.1-mini | - | 68.1% | 68.5% | 64.0% |
| gpt-4o-mini | 68.1% | - | 52.4% | 50.7% |
| gpt-5-mini | 68.5% | 52.4% | - | 69.1% |
| gpt-5.4-mini | 64.0% | 50.7% | 69.1% | - |

## Regression Rates (Row=Baseline, Col=New Model)
*Percentage of times the Baseline got the EXACT human score, but the New Model got it wrong.*

| Baseline \ New  | gpt-4.1-mini | gpt-4o-mini | gpt-5-mini | gpt-5.4-mini |
| :--- | :--- | :--- | :--- | :--- |
| gpt-4.1-mini | - | 7.8% (720) | 15.7% (1450) | 17.5% (1618) |
| gpt-4o-mini | 17.8% (1648) | - | 28.1% (2599) | 29.1% (2697) |
| gpt-5-mini | 5.5% (510) | 7.9% (731) | - | 9.5% (877) |
| gpt-5.4-mini | 6.8% (632) | 8.5% (783) | 9.0% (831) | - |
