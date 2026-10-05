# All-Pairs Model Comparison

## Baseline Performance (vs. Human)

| Model | N | Exact Match | MAE | Pearson r |
| :--- | :--- | :--- | :--- | :--- |
| questions-rate-dl20-gemini-2.5-flash.jsonl.gz | 10928 | 54.73% | 0.596 | 0.330 |
| questions-rate-dl20-gemini-3.5-flash.jsonl.gz | 11386 | 62.38% | 0.529 | 0.219 |
| questions-rate-dl20-gemini-3.6-flash.jsonl.gz | 11386 | 59.20% | 0.542 | 0.275 |
| questions-rate-dl20-gemini-3.7-flash.jsonl.gz | 11386 | 62.63% | 0.509 | 0.298 |
| questions-rate-dl20-gpt-4.1-mini.jsonl.gz | 9900 | 46.51% | 0.843 | 0.467 |
| questions-rate-dl20-gpt-4.1-nano.jsonl.gz | 11246 | 54.92% | 0.592 | 0.412 |
| questions-rate-dl20-gpt-4o-mini.jsonl.gz | 11013 | 50.40% | 0.768 | 0.472 |
| questions-rate-dl20-gpt-5-mini.jsonl.gz | 11386 | 51.44% | 0.703 | 0.424 |
| questions-rate-dl20-gpt-5.4-mini.jsonl.gz | 11386 | 53.58% | 0.670 | 0.489 |

## Model-to-Model Agreement (Exact Match %)

|  | questions-rate-dl20-gemini-2.5-flash.jsonl.gz | questions-rate-dl20-gemini-3.5-flash.jsonl.gz | questions-rate-dl20-gemini-3.6-flash.jsonl.gz | questions-rate-dl20-gemini-3.7-flash.jsonl.gz | questions-rate-dl20-gpt-4.1-mini.jsonl.gz | questions-rate-dl20-gpt-4.1-nano.jsonl.gz | questions-rate-dl20-gpt-4o-mini.jsonl.gz | questions-rate-dl20-gpt-5-mini.jsonl.gz | questions-rate-dl20-gpt-5.4-mini.jsonl.gz |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| questions-rate-dl20-gemini-2.5-flash.jsonl.gz | - | 60.2% | 61.5% | 63.1% | 45.6% | 56.7% | 48.8% | 53.5% | 52.6% |
| questions-rate-dl20-gemini-3.5-flash.jsonl.gz | 60.2% | - | 83.5% | 86.5% | 39.5% | 53.6% | 43.3% | 46.3% | 46.6% |
| questions-rate-dl20-gemini-3.6-flash.jsonl.gz | 61.5% | 83.5% | - | 84.2% | 41.0% | 55.1% | 44.2% | 47.9% | 48.0% |
| questions-rate-dl20-gemini-3.7-flash.jsonl.gz | 63.1% | 86.5% | 84.2% | - | 40.7% | 56.0% | 44.9% | 47.9% | 48.5% |
| questions-rate-dl20-gpt-4.1-mini.jsonl.gz | 45.6% | 39.5% | 41.0% | 40.7% | - | 51.3% | 68.1% | 59.2% | 65.5% |
| questions-rate-dl20-gpt-4.1-nano.jsonl.gz | 56.7% | 53.6% | 55.1% | 56.0% | 51.3% | - | 54.9% | 55.3% | 58.0% |
| questions-rate-dl20-gpt-4o-mini.jsonl.gz | 48.8% | 43.3% | 44.2% | 44.9% | 68.1% | 54.9% | - | 58.3% | 65.8% |
| questions-rate-dl20-gpt-5-mini.jsonl.gz | 53.5% | 46.3% | 47.9% | 47.9% | 59.2% | 55.3% | 58.3% | - | 66.1% |
| questions-rate-dl20-gpt-5.4-mini.jsonl.gz | 52.6% | 46.6% | 48.0% | 48.5% | 65.5% | 58.0% | 65.8% | 66.1% | - |

## Regression Rates (Row=Baseline, Col=New Model)
*Percentage of times the Baseline got the EXACT human score, but the New Model got it wrong.*

| Baseline \ New  | questions-rate-dl20-gemini-2.5-flash.jsonl.gz | questions-rate-dl20-gemini-3.5-flash.jsonl.gz | questions-rate-dl20-gemini-3.6-flash.jsonl.gz | questions-rate-dl20-gemini-3.7-flash.jsonl.gz | questions-rate-dl20-gpt-4.1-mini.jsonl.gz | questions-rate-dl20-gpt-4.1-nano.jsonl.gz | questions-rate-dl20-gpt-4o-mini.jsonl.gz | questions-rate-dl20-gpt-5-mini.jsonl.gz | questions-rate-dl20-gpt-5.4-mini.jsonl.gz |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| questions-rate-dl20-gemini-2.5-flash.jsonl.gz | - | 10.3% (1123) | 11.8% (1286) | 9.2% (1002) | 21.7% (2065) | 15.5% (1667) | 18.8% (1989) | 17.2% (1884) | 16.2% (1774) |
| questions-rate-dl20-gemini-3.5-flash.jsonl.gz | 18.1% (1974) | - | 7.3% (835) | 4.4% (496) | 28.3% (2804) | 20.5% (2302) | 25.4% (2793) | 24.3% (2769) | 22.7% (2580) |
| questions-rate-dl20-gemini-3.6-flash.jsonl.gz | 16.1% (1756) | 4.2% (473) | - | 3.8% (436) | 25.9% (2567) | 18.3% (2056) | 23.3% (2564) | 21.9% (2489) | 20.5% (2331) |
| questions-rate-dl20-gemini-3.7-flash.jsonl.gz | 17.1% (1869) | 4.6% (524) | 7.3% (826) | - | 27.9% (2767) | 19.7% (2220) | 24.9% (2738) | 23.8% (2711) | 22.0% (2509) |
| questions-rate-dl20-gpt-4.1-mini.jsonl.gz | 12.6% (1203) | 12.2% (1208) | 12.9% (1274) | 11.4% (1133) | - | 10.1% (984) | 7.0% (692) | 9.3% (923) | 5.9% (582) |
| questions-rate-dl20-gpt-4.1-nano.jsonl.gz | 15.5% (1676) | 12.9% (1452) | 13.9% (1567) | 12.0% (1347) | 19.1% (1868) | - | 16.6% (1809) | 16.7% (1881) | 14.2% (1594) |
| questions-rate-dl20-gpt-4o-mini.jsonl.gz | 13.8% (1461) | 12.9% (1420) | 14.0% (1539) | 12.0% (1327) | 10.6% (1044) | 11.2% (1220) | - | 11.7% (1294) | 8.1% (892) |
| questions-rate-dl20-gpt-5-mini.jsonl.gz | 13.7% (1493) | 13.4% (1523) | 14.1% (1605) | 12.6% (1437) | 14.8% (1465) | 13.4% (1512) | 13.7% (1507) | - | 9.6% (1091) |
| questions-rate-dl20-gpt-5.4-mini.jsonl.gz | 14.8% (1619) | 13.9% (1578) | 14.9% (1691) | 13.0% (1479) | 13.8% (1368) | 13.0% (1459) | 12.2% (1340) | 11.7% (1335) | - |
