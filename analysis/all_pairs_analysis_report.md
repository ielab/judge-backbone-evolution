# All-Pairs Model Comparison

## Baseline Performance (vs. Human)

| Model | N | Exact Match | MAE | Pearson r |
| :--- | :--- | :--- | :--- | :--- |
| gemini-2.5-flash | 9260 | 42.14% | 0.724 | 0.559 |
| gemini-3.7-flash | 3730 | 42.09% | 0.629 | 0.658 |
| gemini-3.8-flash | 9260 | 46.38% | 0.602 | 0.598 |

## Model-to-Model Agreement (Exact Match %)

|  | gemini-2.5-flash | gemini-3.7-flash | gemini-3.8-flash |
| :--- | :--- | :--- | :--- |
| gemini-2.5-flash | - | 73.0% | 71.8% |
| gemini-3.7-flash | 73.0% | - | 93.4% |
| gemini-3.8-flash | 71.8% | 93.4% | - |

## Regression Rates (Row=Baseline, Col=New Model)
*Percentage of times the Baseline got the EXACT human score, but the New Model got it wrong.*

| Baseline \ New  | gemini-2.5-flash | gemini-3.7-flash | gemini-3.8-flash |
| :--- | :--- | :--- | :--- |
| gemini-2.5-flash | - | 8.3% (310) | 7.3% (672) |
| gemini-3.7-flash | 10.5% (392) | - | 2.3% (87) |
| gemini-3.8-flash | 11.5% (1065) | 3.1% (116) | - |
