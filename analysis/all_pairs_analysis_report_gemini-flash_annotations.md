# All-Pairs Model Comparison

## Baseline Performance (vs. Human)

| Model | N | Exact Match | MAE | Pearson r |
| :--- | :--- | :--- | :--- | :--- |
| gemini-2.5-flash | 9260 | 42.70% | 0.704 | 0.580 |
| gemini-3.5-flash | 9260 | 47.61% | 0.606 | 0.601 |
| gemini-3.6-flash | 9260 | 48.28% | 1.306 | 0.030 |
| gemini-3.7-flash | 9260 | 45.01% | 0.621 | 0.600 |
| gemini-3.8-flash | 9260 | 46.65% | 0.604 | 0.594 |

## Model-to-Model Agreement (Exact Match %)

|  | gemini-2.5-flash | gemini-3.5-flash | gemini-3.6-flash | gemini-3.7-flash | gemini-3.8-flash |
| :--- | :--- | :--- | :--- | :--- | :--- |
| gemini-2.5-flash | - | 76.0% | 74.5% | 75.4% | 73.9% |
| gemini-3.5-flash | 76.0% | - | 90.8% | 89.3% | 88.1% |
| gemini-3.6-flash | 74.5% | 90.8% | - | 89.5% | 88.7% |
| gemini-3.7-flash | 75.4% | 89.3% | 89.5% | - | 93.1% |
| gemini-3.8-flash | 73.9% | 88.1% | 88.7% | 93.1% | - |

## Regression Rates (Row=Baseline, Col=New Model)
*Percentage of times the Baseline got the EXACT human score, but the New Model got it wrong.*

| Baseline \ New  | gemini-2.5-flash | gemini-3.5-flash | gemini-3.6-flash | gemini-3.7-flash | gemini-3.8-flash |
| :--- | :--- | :--- | :--- | :--- | :--- |
| gemini-2.5-flash | - | 5.8% (541) | 6.0% (558) | 7.2% (668) | 7.0% (652) |
| gemini-3.5-flash | 10.8% (996) | - | 3.4% (316) | 5.5% (513) | 5.2% (483) |
| gemini-3.6-flash | 11.6% (1075) | 4.1% (378) | - | 5.7% (532) | 5.3% (487) |
| gemini-3.7-flash | 9.5% (882) | 2.9% (272) | 2.5% (229) | - | 2.0% (184) |
| gemini-3.8-flash | 11.0% (1018) | 4.3% (394) | 3.6% (336) | 3.6% (336) | - |
