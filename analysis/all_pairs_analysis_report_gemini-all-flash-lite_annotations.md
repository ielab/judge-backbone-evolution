# All-Pairs Model Comparison

## Baseline Performance (vs. Human)

| Model | N | Exact Match | MAE | Pearson r |
| :--- | :--- | :--- | :--- | :--- |
| gemini-2.5-flash-lite | 9260 | 45.12% | 0.672 | 0.587 |
| gemini-3.1-flash-lite | 9260 | 46.80% | 0.643 | 0.591 |
| gemini-3.5-flash-lite | 9260 | 54.10% | 0.552 | 0.600 |

## Model-to-Model Agreement (Exact Match %)

|  | gemini-2.5-flash-lite | gemini-3.1-flash-lite | gemini-3.5-flash-lite |
| :--- | :--- | :--- | :--- |
| gemini-2.5-flash-lite | - | 76.9% | 71.6% |
| gemini-3.1-flash-lite | 76.9% | - | 78.3% |
| gemini-3.5-flash-lite | 71.6% | 78.3% | - |

## Regression Rates (Row=Baseline, Col=New Model)
*Percentage of times the Baseline got the EXACT human score, but the New Model got it wrong.*

| Baseline \ New  | gemini-2.5-flash-lite | gemini-3.1-flash-lite | gemini-3.5-flash-lite |
| :--- | :--- | :--- | :--- |
| gemini-2.5-flash-lite | - | 7.4% (686) | 6.0% (558) |
| gemini-3.1-flash-lite | 9.1% (842) | - | 4.8% (441) |
| gemini-3.5-flash-lite | 15.0% (1390) | 12.1% (1117) | - |
