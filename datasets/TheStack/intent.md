# TheStack Dataset Intent

## Source
- **Link**: https://huggingface.co/datasets/bigcode/the-stack
- **Type**: Source code

## Metrics to Gather
- **Size (Overarching Metric):**
  - **Concrete Metric:** Number of lines of code per file (LOC)
  - **Extraction Strategy:** Stream files remotely, parse code content, and count non-empty lines of code per file.
  - **Downstream Comparison:** Normalized and compared against GitSkills token counts, visualized via distribution graphs.
- **Clone Coverage (Overarching Metric):**
  - **Concrete Metric:** Code duplication (% similarity / duplicate code per file)
  - **Extraction Strategy:** Use the `content` field to check for duplicate code for individual files, then aggregate across the dataset via average and/or median.
  - **Downstream Comparison:** Direct comparison of distributions against GitSkills duplication, visualized via distribution graphs for % similarity per file.
- **Readability (Overarching Metric):** To be specified
    - **Concrete Metric:** Composite readability score (0–1 scale per file, compared by dataset mean)
    - **Extraction Strategy:** Use the `content` field by normalizing and averaging three sub-metrics: mean line length (penalizing lines over 80 characters), alphanumeric character ratio (penalizing symbol clutter), and comment-to-code line ratio (rewarding documentation).
    - **Downstream Comparison:** Normalize both datasets and compare distributions for the cognitive complexity vs the reading difficulty and structural complexity

## Constraints
- Never download the files locally (stream remotely using `streaming=True`).
- Execute a test run of ~100 records first before running larger chunks for full analysis.
