# All-Pairs Model Comparison

## Baseline Performance (vs. Human)

| Model | N | Exact Match | MAE | Pearson r |
| :--- | :--- | :--- | :--- | :--- |
| questions-rate-dl19-gemini-2.5-flash-lite.jsonl.gz | 9260 | 44.57% | 0.728 | 0.321 |
| questions-rate-dl19-gemini-2.5-flash.jsonl.gz | 9260 | 44.81% | 0.730 | 0.324 |
| questions-rate-dl19-gemini-3.1-flash-lite.jsonl.gz | 9260 | 52.10% | 0.720 | 0.255 |
| questions-rate-dl19-gemini-3.5-flash-lite.jsonl.gz | 9037 | 52.66% | 0.721 | 0.233 |
| questions-rate-dl19-gemini-3.5-flash.jsonl.gz | 9260 | 52.22% | 0.718 | 0.268 |
| questions-rate-dl19-gemini-3.6-flash.jsonl.gz | 8918 | 49.78% | 0.716 | 0.262 |
| questions-rate-dl19-gemini-3.7-flash.jsonl.gz | 8825 | 52.58% | 0.672 | 0.335 |
| questions-rate-dl19-gemini-3.8-flash.jsonl.gz | 9260 | 52.31% | 0.693 | 0.322 |

## Model-to-Model Agreement (Exact Match %)

|  | questions-rate-dl19-gemini-2.5-flash-lite.jsonl.gz | questions-rate-dl19-gemini-2.5-flash.jsonl.gz | questions-rate-dl19-gemini-3.1-flash-lite.jsonl.gz | questions-rate-dl19-gemini-3.5-flash-lite.jsonl.gz | questions-rate-dl19-gemini-3.5-flash.jsonl.gz | questions-rate-dl19-gemini-3.6-flash.jsonl.gz | questions-rate-dl19-gemini-3.7-flash.jsonl.gz | questions-rate-dl19-gemini-3.8-flash.jsonl.gz |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| questions-rate-dl19-gemini-2.5-flash-lite.jsonl.gz | - | 70.7% | 50.7% | 49.7% | 48.5% | 50.4% | 51.7% | 51.7% |
| questions-rate-dl19-gemini-2.5-flash.jsonl.gz | 70.7% | - | 50.9% | 50.4% | 48.9% | 50.3% | 51.5% | 51.5% |
| questions-rate-dl19-gemini-3.1-flash-lite.jsonl.gz | 50.7% | 50.9% | - | 89.3% | 85.6% | 79.3% | 84.3% | 83.3% |
| questions-rate-dl19-gemini-3.5-flash-lite.jsonl.gz | 49.7% | 50.4% | 89.3% | - | 87.8% | 80.4% | 85.1% | 83.7% |
| questions-rate-dl19-gemini-3.5-flash.jsonl.gz | 48.5% | 48.9% | 85.6% | 87.8% | - | 84.0% | 86.1% | 85.5% |
| questions-rate-dl19-gemini-3.6-flash.jsonl.gz | 50.4% | 50.3% | 79.3% | 80.4% | 84.0% | - | 83.1% | 84.0% |
| questions-rate-dl19-gemini-3.7-flash.jsonl.gz | 51.7% | 51.5% | 84.3% | 85.1% | 86.1% | 83.1% | - | 91.6% |
| questions-rate-dl19-gemini-3.8-flash.jsonl.gz | 51.7% | 51.5% | 83.3% | 83.7% | 85.5% | 84.0% | 91.6% | - |

## Regression Rates (Row=Baseline, Col=New Model)
*Percentage of times the Baseline got the EXACT human score, but the New Model got it wrong.*

| Baseline \ New  | questions-rate-dl19-gemini-2.5-flash-lite.jsonl.gz | questions-rate-dl19-gemini-2.5-flash.jsonl.gz | questions-rate-dl19-gemini-3.1-flash-lite.jsonl.gz | questions-rate-dl19-gemini-3.5-flash-lite.jsonl.gz | questions-rate-dl19-gemini-3.5-flash.jsonl.gz | questions-rate-dl19-gemini-3.6-flash.jsonl.gz | questions-rate-dl19-gemini-3.7-flash.jsonl.gz | questions-rate-dl19-gemini-3.8-flash.jsonl.gz |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| questions-rate-dl19-gemini-2.5-flash-lite.jsonl.gz | - | 9.5% (879) | 11.9% (1102) | 12.3% (1112) | 12.8% (1181) | 13.4% (1196) | 12.2% (1073) | 12.1% (1118) |
| questions-rate-dl19-gemini-2.5-flash.jsonl.gz | 9.7% (901) | - | 12.1% (1119) | 12.2% (1101) | 12.9% (1190) | 13.7% (1222) | 12.3% (1085) | 12.4% (1147) |
| questions-rate-dl19-gemini-3.1-flash-lite.jsonl.gz | 19.4% (1799) | 19.4% (1794) | - | 2.9% (260) | 4.0% (372) | 7.6% (678) | 4.2% (373) | 4.5% (419) |
| questions-rate-dl19-gemini-3.5-flash-lite.jsonl.gz | 19.7% (1784) | 19.6% (1771) | 3.2% (291) | - | 3.6% (326) | 7.6% (663) | 4.2% (367) | 4.7% (424) |
| questions-rate-dl19-gemini-3.5-flash.jsonl.gz | 20.4% (1890) | 20.3% (1877) | 4.1% (384) | 3.3% (297) | - | 6.4% (575) | 3.8% (335) | 4.0% (374) |
| questions-rate-dl19-gemini-3.6-flash.jsonl.gz | 18.8% (1681) | 18.9% (1689) | 5.3% (476) | 4.9% (422) | 4.0% (361) | - | 4.0% (343) | 4.0% (355) |
| questions-rate-dl19-gemini-3.7-flash.jsonl.gz | 19.5% (1724) | 19.6% (1727) | 4.4% (390) | 4.1% (354) | 3.9% (344) | 6.8% (576) | - | 2.6% (228) |
| questions-rate-dl19-gemini-3.8-flash.jsonl.gz | 19.8% (1835) | 19.9% (1842) | 4.7% (439) | 4.5% (405) | 4.1% (382) | 6.6% (589) | 2.5% (225) | - |
