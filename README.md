# The Impact of Backbone Evolution on LLM-Based Relevance Assessments

Code for paper ”The Impact of Backbone Evolution on LLM-Based Relevance Assessments“.

- **UMBRELA**: direct zero-shot prediction of the human relevance label (0–3).
- **EXAM**: indirect relevance estimation based on whether a passage contains
  enough information to answer query-specific questions.

The main questions are not only whether newer models improve aggregate scores,
but also whether they introduce regressions on examples that earlier models
judged correctly and whether those regressions persist across repeated runs.

## What is included

- Parallel, resumable inference with the Gemini and OpenAI APIs.
- Support for OpenAI-compatible endpoints, including local vLLM servers.
- TREC DL 2019 and 2020 evaluation.
- Exact match, mean absolute error (MAE), and Pearson correlation metrics.
- Pairwise agreement and directional regression analysis.
- Repeated-run stability and regression-overlap analysis.
- Export and analysis utilities for the EXAM pipeline.
- Saved annotations, generated reports, and EXAM intermediate data.

## Repository layout

```text
.
├── src/                       Evaluation, export, and analysis scripts
├── data/                      TREC/EXAM inputs and generated grading files
├── results/                   TREC DL 2019 UMBRELA annotations
├── results_2020/              TREC DL 2020 UMBRELA annotations
├── analysis/                  Generated comparison and regression reports
└── rubric-grading-workbench/  Local EXAM pipeline checkout with project patches
```

Large JSONL and JSONL.GZ files in `data/` and `results/` are research
artifacts. You do not need to regenerate them to run the analysis scripts.

## Installation

Python 3.10 or later is recommended. Create and activate a virtual environment,
then install the direct dependencies:

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install \
  datasets google-genai ir-datasets numpy openai pandas pyyaml tqdm
```

The default zero-shot prompt is loaded from the
[UMBRELA](https://github.com/castorini/umbrela) repository. Either clone it to
the default location:

```bash
git clone https://github.com/castorini/umbrela.git ~/github/umbrela
```

or pass another compatible YAML template with `--prompt_template`.

For EXAM experiments, use the bundled `rubric-grading-workbench/` directory.
It contains local changes required by this project, including Gemini support
and thinking-token handling.

## API configuration

Set the key for the provider you intend to use:

```bash
export GEMINI_API_KEY="..."
# or
export OPENAI_API_KEY="..."
```

Keys can also be supplied with `--gemini_key` or `--openai_key`, although
environment variables are safer for shell history and shared machines.

For a local or third-party OpenAI-compatible server, set `OPENAI_BASE_URL` or
use `--base_url`.

## Running zero-shot UMBRELA evaluation

Run all commands from the repository root.

### Gemini

```bash
python src/evaluate_trec_dl.py \
  --provider gemini \
  --model gemini-2.5-flash \
  --dataset trec-dl-2019 \
  --workers 16
```

To retain Gemini thought content in the output, enable thinking and optionally
set its budget:

```bash
python src/evaluate_trec_dl.py \
  --provider gemini \
  --model gemini-2.5-flash \
  --think \
  --think_budget 2048
```

### OpenAI

```bash
python src/evaluate_trec_dl.py \
  --provider openai \
  --model gpt-4o-mini \
  --dataset trec-dl-2019 \
  --workers 16
```

### TREC DL 2020

Select the 2020 benchmark and a separate output directory:

```bash
python src/evaluate_trec_dl.py \
  --provider openai \
  --model gpt-4o-mini \
  --dataset trec-dl-2020 \
  --output_dir results_2020
```

DL 2020 filenames receive a `_trec-dl-2020` suffix so resume logic cannot mix
the two datasets.

### OpenAI-compatible local models

```bash
python src/evaluate_trec_dl.py \
  --provider openai \
  --model Qwen/Qwen3-8B \
  --base_url http://localhost:8000/v1 \
  --disable_thinking
```

`--disable_thinking` sends the Qwen chat-template option
`enable_thinking=false`. The selected server must implement the OpenAI Chat
Completions API.

### Resuming and repeating runs

Results are appended as each request completes. Re-running the same command
skips query-document pairs already present in the output file.

Use `--run_id` to keep independent repeats separate:

```bash
python src/evaluate_trec_dl.py \
  --model gemini-2.5-flash \
  --run_id 1 \
  --output_dir results/repeats_no_thinking
```

Useful options include:

| Option | Default | Purpose |
| --- | --- | --- |
| `--provider` | `gemini` | `gemini` or `openai` |
| `--dataset` | `trec-dl-2019` | Select TREC DL 2019 or 2020 |
| `--workers` | `16` | Number of concurrent API requests |
| `--retries` | `5` | Attempts per query-document pair |
| `--output_dir` | `results` | Annotation output directory |
| `--run_id` | unset | Identifier for an independent repeat |
| `--prompt_template` | UMBRELA path | YAML prompt template |
| `--think` | off | Store returned thought content |
| `--think_budget` | `1024` | Gemini thinking-token budget |

The evaluator downloads qrels from Hugging Face, loads queries through
`ir_datasets`, and streams the BeIR MS MARCO corpus to retrieve only judged
passages. The first run therefore requires network access and may take several
minutes before inference starts.

## Analysis

### Compare two runs

```bash
python src/compare_models.py \
  --model1 results/gemini-2_5-flash_annotations.jsonl \
  --model2 results/gemini-3_8-flash_annotations.jsonl
```

This reports exact match, MAE, Pearson correlation, model agreement, and the
largest disagreements on the shared set of parsed examples.

### Find directional regressions

A regression is an example where model A exactly matches the human label and
model B does not.

```bash
python src/find_regressions.py \
  --model_a results/gemini-2_5-flash_annotations.jsonl \
  --model_b results/gemini-3_8-flash_annotations.jsonl \
  --output gemini_2_5_to_3_8
```

With `--output`, the script writes detailed JSONL and CSV exports containing
the passage text.

### Analyze every matching model pair

```bash
python src/analyze_all_pairs.py \
  --pattern 'results/gemini-*_annotations.jsonl'
```

The report is written to `analysis/`. Comparisons use the intersection of
successfully parsed query-document pairs, allowing incomplete runs to be
compared without treating missing predictions as errors.

### Analyze repeated-run stability

`src/analyze_stability.py` expects three runs for each configured Gemini model
under `results/repeats_no_thinking/`:

```bash
python src/analyze_stability.py
```

It reports the mean and standard deviation of the three evaluation metrics,
plus pairwise Jaccard similarity and three-run intersection sizes for
regression sets.

## EXAM pipeline

EXAM turns relevance assessment into a question-answering test. A question bank
is generated per query, then each passage is graded according to how many of
those questions a model can answer from the passage alone. The analysis code
maps question coverage back to the 0–3 TREC relevance scale.

Prepare the bundled workbench inputs with:

```bash
python src/export_trec_dl_19_for_exam.py
python src/export_trec_dl_20_for_exam.py
```

These commands produce query JSON and compressed `runs-with-text` files under
`data/`. Run question generation and grading using the modules and environment
defined in `rubric-grading-workbench/`; see its README and walkthrough for the
pipeline-specific commands.

The following project utilities support downstream EXAM work:

| Script | Purpose |
| --- | --- |
| `src/filter_exam_regressions.py` | Restrict EXAM files to regression examples |
| `src/analyze_exam_regression_thoughts.py` | Compare reasoning traces on EXAM regressions |
| `src/map_exam_categories_to_umbrela.py` | Relate EXAM error categories to UMBRELA outputs |
| `src/reformat_export.py` | Reformat exported pipeline data |
| `src/extract_failed.py` | Extract failed grading records for recovery |

`compare_models.py` and `analyze_all_pairs.py` accept both flat UMBRELA JSONL
and the grouped, compressed JSONL.GZ produced by the EXAM workflow.

## Results snapshot

All metrics below compare model-derived 0–3 labels with TREC human judgments.
Exact match is better when higher, MAE is better when lower, and Pearson's
correlation is better when higher. These are snapshots of the checked-in
artifacts; consult generated reports for pairwise and example-level details.

### UMBRELA: TREC DL 2019

| Model | Exact match | MAE | Pearson r |
| --- | ---: | ---: | ---: |
| `gemini-2.5-flash` | 42.70% | 0.704 | 0.580 |
| `gemini-3.5-flash` | 47.61% | 0.606 | 0.601 |
| `gemini-3.6-flash` | 48.34% | 0.598 | 0.592 |
| `gemini-3.7-flash` | 45.01% | 0.621 | 0.600 |
| `gemini-3.8-flash` | 46.65% | 0.604 | 0.594 |
| `gemini-2.5-flash-lite` | 45.12% | 0.672 | 0.587 |
| `gemini-3.1-flash-lite` | 46.80% | 0.643 | 0.591 |
| `gemini-3.5-flash-lite` | 54.10% | 0.552 | 0.600 |
| `gpt-4o-mini` | 55.80% | 0.556 | 0.609 |
| `gpt-4.1-mini` | 45.78% | 0.654 | 0.583 |
| `gpt-5-mini` | 35.63% | 0.821 | 0.557 |
| `gpt-5.4-mini` | 35.13% | 0.825 | 0.578 |
| `gpt-4.1-nano` | 39.44% | 0.748 | 0.402 |
| `gpt-5-nano` | 41.02% | 0.741 | 0.564 |
| `gpt-5.4-nano` | 51.09% | 0.668 | 0.560 |

### UMBRELA: TREC DL 2020

| Model | Exact match | MAE | Pearson r |
| --- | ---: | ---: | ---: |
| `gemini-2.5-flash` | 44.23% | 0.692 | 0.551 |
| `gemini-3.5-flash` | 53.31% | 0.549 | 0.602 |
| `gemini-3.6-flash` | 53.59% | 0.541 | 0.594 |
| `gemini-3.7-flash` | 51.64% | 0.553 | 0.596 |
| `gemini-3.8-flash` | 51.23% | 0.551 | 0.585 |
| `gemini-2.5-flash-lite` | 48.93% | 0.726 | 0.564 |
| `gemini-3.1-flash-lite` | 58.84% | 0.538 | 0.601 |
| `gemini-3.5-flash-lite` | 61.96% | 0.461 | 0.583 |
| `gpt-4o-mini` | 60.26% | 0.514 | 0.550 |
| `gpt-4.1-mini` | 49.57% | 0.630 | 0.560 |
| `gpt-5-mini` | 38.71% | 0.795 | 0.544 |
| `gpt-5.4-mini` | 37.16% | 0.822 | 0.536 |
| `gpt-4.1-nano` | 40.74% | 0.731 | 0.392 |
| `gpt-5-nano` | 44.15% | 0.702 | 0.558 |
| `gpt-5.4-nano` | 54.48% | 0.687 | 0.479 |

### EXAM: TREC DL 2019

| Model | Exact match | MAE | Pearson r |
| --- | ---: | ---: | ---: |
| `gemini-2.5-flash` | 44.81% | 0.730 | 0.324 |
| `gemini-3.5-flash` | 52.22% | 0.718 | 0.268 |
| `gemini-3.6-flash` | 49.78% | 0.716 | 0.262 |
| `gemini-3.7-flash` | 52.58% | 0.672 | 0.335 |
| `gemini-3.8-flash` | 52.31% | 0.693 | 0.322 |
| `gemini-2.5-flash-lite` | 44.57% | 0.728 | 0.321 |
| `gemini-3.1-flash-lite` | 52.10% | 0.720 | 0.255 |
| `gemini-3.5-flash-lite` | 52.66% | 0.721 | 0.233 |
| `gpt-4o-mini` | 38.95% | 0.996 | 0.420 |
| `gpt-4.1-mini` | 37.16% | 1.019 | 0.429 |
| `gpt-5-mini` | 45.06% | 0.798 | 0.366 |
| `gpt-5.4-mini` | 44.52% | 0.813 | 0.449 |
| `gpt-4.1-nano` | 47.83% | 0.715 | 0.353 |
| `gpt-5-nano` | 44.24% | 0.803 | 0.381 |
| `gpt-5.4-nano` | 49.30% | 0.673 | 0.422 |

### EXAM: TREC DL 2020

| Model | Exact match | MAE | Pearson r |
| --- | ---: | ---: | ---: |
| `gemini-2.5-flash` | 54.73% | 0.596 | 0.330 |
| `gemini-3.5-flash` | 62.38% | 0.529 | 0.219 |
| `gemini-3.6-flash` | 59.83% | 0.575 | 0.210 |
| `gemini-3.7-flash` | 62.63% | 0.509 | 0.298 |
| `gemini-3.8-flash` | 61.25% | 0.518 | 0.317 |
| `gemini-2.5-flash-lite` | 53.57% | 0.606 | 0.322 |
| `gemini-3.1-flash-lite` | 62.78% | 0.528 | 0.212 |
| `gemini-3.5-flash-lite` | 63.31% | 0.516 | 0.222 |
| `gpt-4o-mini` | 50.40% | 0.768 | 0.472 |
| `gpt-4.1-mini` | 46.51% | 0.843 | 0.467 |
| `gpt-5-mini` | 51.44% | 0.703 | 0.424 |
| `gpt-5.4-mini` | 47.96% | 0.785 | 0.428 |
| `gpt-4.1-nano` | 52.88% | 0.686 | 0.252 |
| `gpt-5-nano` | 48.41% | 0.726 | 0.451 |
| `gpt-5.4-nano` | 53.18% | 0.613 | 0.470 |

## Main findings

- Aggregate metrics are stable across repeated runs, but the identity of
  individual regressions is much less stable. Query-level regressions should
  therefore be interpreted across repeats rather than from a single run.
- Newer models do not consistently dominate their predecessors. Improvements
  in overall exact match can coexist with substantial directional regressions.
- Model tier matters as much as generation: Flash Lite and Nano variants can
  outperform larger models on this judging task.
- EXAM often raises exact match for newer Gemini models while producing lower
  Pearson correlation than direct UMBRELA judgments. The two methods capture
  different aspects of relevance behavior and should not be treated as
  interchangeable.

## Reproducibility notes

- API-hosted model behavior can change without a repository change. Record the
  provider's exact model identifier and run date with every experiment.
- Output parsing accepts only relevance scores in the range 0–3. Inspect
  unparsed outputs before comparing coverage across models.
- Pairwise reports operate on shared parsed examples; always compare the
  reported sample size (`N`) alongside the metric values.
- Repeated evaluations can incur substantial API cost. Start with a small
  worker count and monitor provider quotas before launching the full benchmark.
- Do not commit API keys or place them directly in scripts.

## License and citation

No project-level license or citation file is currently included. The bundled
`rubric-grading-workbench` retains its own license. If you use this repository
in published work, cite the TREC Deep Learning datasets, UMBRELA, and EXAM as
appropriate, and record the exact model versions used in your experiments.
