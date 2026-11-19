# GitSkills Dataset Intent

## Source
- **Link**: https://huggingface.co/datasets/mvaccargiu/gitskills
- **Type**: Skills (Natural Language)

## Metrics to Gather
- **Size (Overarching Metric):**
  - **Concrete Metric:** Token count per skill
  - **Extraction Strategy:** Stream skills remotely, tokenize skill content, and compute total token count per skill file.
  - **Downstream Comparison:** Normalized and compared against TheStack lines of code, visualized via distribution graphs.
- **Clone Coverage (Overarching Metric):** 
    - **Concrete Metric:** Exact and near duplication
    - **Extraction Strategy:** Use “entry_sha” field from GitSkills to find exact matches and evaluate the Jaccard similarity of the dataset to find near-duplicates.
    - **Downstream Comparison:** Direct comparison of distributions. visualized via distribution graphs for percent similarity per file
- **Readability (Overarching Metric):** 
    - **Concrete Metric:** Reading difficulty and structural complexity
    - **Extraction Strategy:** Deduplicate by content hash. build representative stratified sample (N=~5,000-10,000). Count conditional words, “if”, “unless”, “otherwise”, “when”, “depends on”, etc. for cognitive complexity. Count constraint density with imperative words, “must”, “shall”, “required”, “do not”, “never”, etc. Find a way to quantify conditional and constraint terminology.
    - **Downstream Comparison:** Normalize both datasets and compare distributions. visualized via distribution graphs for score per file

## Constraints
- Never download the files locally (stream remotely using `streaming=True`).
- Execute a test run of ~100 records first before running larger chunks for full analysis.
