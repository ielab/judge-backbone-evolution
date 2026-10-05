# All-Pairs Model Comparison

## Baseline Performance (vs. Human)

| Model | N | Exact Match | MAE | Pearson r |
| :--- | :--- | :--- | :--- | :--- |
| questions-rate-dl19-gpt-4.1-mini.jsonl.gz | 9260 | 37.16% | 1.019 | 0.429 |
| questions-rate-dl19-gpt-4.1-nano.jsonl.gz | 8905 | 47.83% | 0.715 | 0.353 |
| questions-rate-dl19-gpt-4o-mini.jsonl.gz | 9260 | 38.95% | 0.996 | 0.420 |
| questions-rate-dl19-gpt-5-mini-backup.jsonl.gz | 535 | 35.14% | 1.006 | 0.253 |
| questions-rate-dl19-gpt-5-mini.jsonl.gz | 9260 | 45.06% | 0.798 | 0.366 |
| questions-rate-dl19-gpt-5-nano.jsonl.gz | 6636 | 44.24% | 0.803 | 0.381 |
| questions-rate-dl19-gpt-5.4-mini.jsonl.gz | 9260 | 44.52% | 0.813 | 0.449 |
| questions-rate-dl19-gpt-5.4-nano.jsonl.gz | 9260 | 49.30% | 0.673 | 0.422 |

## Model-to-Model Agreement (Exact Match %)

|  | questions-rate-dl19-gpt-4.1-mini.jsonl.gz | questions-rate-dl19-gpt-4.1-nano.jsonl.gz | questions-rate-dl19-gpt-4o-mini.jsonl.gz | questions-rate-dl19-gpt-5-mini-backup.jsonl.gz | questions-rate-dl19-gpt-5-mini.jsonl.gz | questions-rate-dl19-gpt-5-nano.jsonl.gz | questions-rate-dl19-gpt-5.4-mini.jsonl.gz | questions-rate-dl19-gpt-5.4-nano.jsonl.gz |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| questions-rate-dl19-gpt-4.1-mini.jsonl.gz | - | 39.6% | 64.8% | 38.9% | 52.3% | 54.8% | 59.1% | 42.4% |
| questions-rate-dl19-gpt-4.1-nano.jsonl.gz | 39.6% | - | 42.1% | 41.8% | 53.5% | 54.7% | 50.9% | 57.7% |
| questions-rate-dl19-gpt-4o-mini.jsonl.gz | 64.8% | 42.1% | - | 36.8% | 50.0% | 52.7% | 58.1% | 45.1% |
| questions-rate-dl19-gpt-5-mini-backup.jsonl.gz | 38.9% | 41.8% | 36.8% | - | 100.0% | 66.7% | 51.0% | 51.6% |
| questions-rate-dl19-gpt-5-mini.jsonl.gz | 52.3% | 53.5% | 50.0% | 100.0% | - | 68.5% | 61.8% | 60.2% |
| questions-rate-dl19-gpt-5-nano.jsonl.gz | 54.8% | 54.7% | 52.7% | 66.7% | 68.5% | - | 62.9% | 58.5% |
| questions-rate-dl19-gpt-5.4-mini.jsonl.gz | 59.1% | 50.9% | 58.1% | 51.0% | 61.8% | 62.9% | - | 55.7% |
| questions-rate-dl19-gpt-5.4-nano.jsonl.gz | 42.4% | 57.7% | 45.1% | 51.6% | 60.2% | 58.5% | 55.7% | - |

## Regression Rates (Row=Baseline, Col=New Model)
*Percentage of times the Baseline got the EXACT human score, but the New Model got it wrong.*

| Baseline \ New  | questions-rate-dl19-gpt-4.1-mini.jsonl.gz | questions-rate-dl19-gpt-4.1-nano.jsonl.gz | questions-rate-dl19-gpt-4o-mini.jsonl.gz | questions-rate-dl19-gpt-5-mini-backup.jsonl.gz | questions-rate-dl19-gpt-5-mini.jsonl.gz | questions-rate-dl19-gpt-5-nano.jsonl.gz | questions-rate-dl19-gpt-5.4-mini.jsonl.gz | questions-rate-dl19-gpt-5.4-nano.jsonl.gz |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| questions-rate-dl19-gpt-4.1-mini.jsonl.gz | - | 12.2% (1087) | 8.3% (773) | 5.4% (29) | 9.3% (859) | 9.6% (640) | 7.3% (677) | 10.9% (1011) |
| questions-rate-dl19-gpt-4.1-nano.jsonl.gz | 23.1% (2053) | - | 21.2% (1887) | 22.5% (120) | 16.4% (1460) | 16.5% (1093) | 17.4% (1551) | 13.5% (1205) |
| questions-rate-dl19-gpt-4o-mini.jsonl.gz | 10.1% (939) | 12.2% (1085) | - | 8.6% (46) | 11.1% (1030) | 11.8% (780) | 8.7% (808) | 10.9% (1009) |
| questions-rate-dl19-gpt-5-mini-backup.jsonl.gz | 21.9% (117) | 14.8% (79) | 22.2% (119) | - | 0.0% (0) | 11.3% (17) | 15.3% (82) | 10.5% (56) |
| questions-rate-dl19-gpt-5-mini.jsonl.gz | 17.2% (1591) | 13.1% (1164) | 17.2% (1596) | 0.0% (0) | - | 9.3% (620) | 11.4% (1058) | 10.4% (964) |
| questions-rate-dl19-gpt-5-nano.jsonl.gz | 15.3% (1012) | 11.7% (776) | 15.1% (1003) | 8.0% (12) | 9.8% (648) | - | 11.0% (729) | 10.7% (708) |
| questions-rate-dl19-gpt-5.4-mini.jsonl.gz | 14.7% (1359) | 13.7% (1216) | 14.3% (1324) | 9.3% (50) | 10.9% (1008) | 11.4% (758) | - | 11.6% (1077) |
| questions-rate-dl19-gpt-5.4-nano.jsonl.gz | 23.1% (2135) | 14.7% (1308) | 21.2% (1967) | 17.9% (96) | 14.6% (1356) | 15.7% (1039) | 16.4% (1519) | - |
