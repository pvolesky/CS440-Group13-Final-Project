---
name: remote-dataset-mining
description: >-
  Use this skill when authoring, reviewing, or executing Python scripts to query, stream, or mine datasets remotely
  from Hugging Face (huggingface.co) or external repositories without downloading complete datasets locally.
---

# Remote Dataset Mining & Querying

This skill provides guidelines and general procedures for building and executing Python scripts that discover, query, stream, and extract data from remote datasets (such as Hugging Face, GitHub, Zenodo, and public archives) while adhering to strict resource limits and guard rails.

---

## 1. Core Guidelines & Script Guard Rails

* **No Full Dataset Downloads:** Datasets such as `bigcode/the-stack` or large parquet collections are massive (gigabytes to terabytes). Scripts must never attempt a full download or clone of raw dataset files to the local environment.
* **Remote Streaming First:** Always access data using streaming interfaces, remote pagination, cursor-based APIs, or HTTP range requests (e.g. `datasets.load_dataset(..., streaming=True)`).
* **Two-Stage Mining Workflow (Test Run First):** Always validate data collection scripts with a small test run (~100 records/lines) to verify streaming connectivity, metric extraction, and schema alignment before executing on a larger chunk for actual analysis.
* **Bounded In-Memory Processing:** Consume and process items in small streaming buffers or batches, releasing memory immediately after extracting target fields.
* **Deterministic Sampling:** When evaluating subsets, use fixed sample sizes ($N$) and explicit random seeds (e.g., `--seed 42`) via CLI arguments to ensure reproducibility.
* **Fault Tolerance:** Handle network timeouts, HTTP 429 rate limits, and connection drops with exponential backoff and retry logic.
* **CLI Standards:** Scripts should accept parameters via `argparse` (e.g., `--samples`, `--split`, `--output`) and output lightweight tabular summaries (CSV/JSON), not raw text dumps.

---

## 2. Two-Stage Mining Strategy

To avoid wasting time or hitting unexpected schema/parsing issues on massive datasets, mining scripts must implement a two-stage approach:

```
+-------------------------------------------------------------------------+
| Stage 1: Validation Test Run (~100 lines/records)                       |
| - Stream only ~100 records using --samples 100                          |
| - Verify: Remote connection succeeds without authentication blocks     |
| - Verify: Key attributes (content, path, tokens, LOC) parse correctly   |
| - Verify: Output CSV/JSON contains expected columns and valid values    |
+------------------------------------+------------------------------------+
                                     |
                                     v (Validate output looks good)
+-------------------------------------------------------------------------+
| Stage 2: Production Analysis Chunk (Large sample)                       |
| - Scale to full target sample (e.g. 5,000 - 10,000+ records)           |
| - Run complete metric extraction for statistical comparison             |
+-------------------------------------------------------------------------+
```

### Implementing in Python Scripts
Ensure every extraction script defaults or supports passing a small sample limit for dry runs:
```python
parser.add_argument(
    "--samples",
    type=int,
    default=100,
    help="Number of records to sample (default: 100 for test run, increase for full analysis)"
)
```

---

## 3. Working with Hugging Face (`huggingface.co`)

Hugging Face hosts open datasets formatted as Parquet, Arrow, JSON, or CSV files.

### Key Concepts for Python Scripts
* **Streaming Mode:** Stream records sequentially over HTTP without saving backing files to disk (`streaming=True`).
* **Subsets and Configurations:** Datasets often contain multiple language configurations or subdirectories (e.g., `the-stack` has subsets per programming language). Query only the specific subset needed via `data_dir` or dataset sub-configurations.
* **Field Projection:** Only extract the columns required for the metric computation (e.g., `content`, `path`, `repository_name`), discarding irrelevant metadata.
* **Reservoir / Buffer Sampling:** When sampling rows from an infinite or large stream, use a fixed-size shuffle buffer (`.shuffle(seed=seed, buffer_size=1000).take(N)`) to obtain an unbiased random sample.

---

## 4. Working with Alternative Platforms & Sources

Scripts should apply similar remote querying principles when working with other data repositories:

* **GitHub & Code Repositories:**
  * Use the GitHub REST / GraphQL API to query metadata, commit history, and specific files rather than full repository clones.
  * When Git history is strictly required, use blobless (`--filter=blob:none`) or shallow (`--depth N`) checkouts to fetch commit logs without file content.
* **Zenodo, Figshare & Dataverse:**
  * Access records via public REST endpoints using record IDs and query parameters.
  * Download only the specific target metadata files or summary artifacts.
* **Remote Parquet & SQL Endpoints:**
  * Query remote Parquet files directly via HTTP range requests using DuckDB or PyArrow without downloading the backing storage files.

---

## 5. General Script Mining Workflow

1. **Inspect Metadata & Schema:** Examine the remote dataset card, available configurations/subsets, splits (`train`, `test`, `validation`), and column names before pulling data.
2. **Define CLI Parameters:** Provide `--dataset`, `--split`, `--samples`, `--seed`, and `--output` options.
3. **Execute Test Run:** Run with `--samples 100` and inspect the generated output file to verify correct metrics.
4. **Execute Production Chunk:** Run with the full target sample size for comparative analysis.
5. **Output Standardized Summary:** Save only the aggregated tabular results (e.g. CSV or JSON Lines of extracted metrics) locally, never raw source files.
