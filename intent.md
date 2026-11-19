# Comparison of Software Engineering Metrics: Source Code vs. Agent Skills

## 1. Project Overview & Research Question
- **Context:** MSR 2027 Mining Challenge (CS 440 Group 13 Final Project).
- **Core Research Question:** Which established software engineering metrics (Size, Churn, Age, Clone Coverage, Readability) have meaningful equivalents for AI agent skills, and how do their empirical distributions compare with those of traditional source code?

## 2. Datasets Breakdown
We gather data across four remote datasets to compare corresponding metrics:
- **Dataset 1 — GitSkills (Skills):** Gather Size, Clone Coverage, and Readability for agent skills. (Source: https://huggingface.co/datasets/mvaccargiu/gitskills)
- **Dataset 2 — TheStack (Source Code):** Gather Size, Clone Coverage, and Readability for traditional source code. (Source: https://huggingface.co/datasets/bigcode/the-stack)
- **Dataset 3 — Placeholder (TBD):** Gather Churn and Age for agent skills histories.
- **Dataset 4 — Placeholder (TBD):** Gather Churn and Age for source code histories.

## 3. Overarching Metrics Breakdown

### Metric 1: Size
- **Source Code (TheStack):** Number of lines of code (LOC) per file.
- **Agent Skills (GitSkills):** Token count per skill file.
- **Comparison Strategy:** Normalize both datasets (e.g., log-scaling, min-max scaling, percentile ranking) and compare their empirical distributions using non-parametric statistics.
- **Visualization Strategy:** Create distribution graphs for both lines of code per file and tokens per file, and compare their distributions.

### Metric 2: Churn
- *To be specified*

### Metric 3: Age
- *To be specified*

### Metric 4: Clone Coverage
- **Source Code (TheStack):** Code duplication (% similarity / duplicate code per file)
- **Agent Skills (GitSkills):** Exact and near duplication
- **Comparison Strategy:** Direct comparison of distributions
- **Visualization Strategy:** Create distribution graphs for the code duplication per file and exact and near duplication per file.

### Metric 5: Readability
- **Source Code (TheStack):** Cognitive complexity
- **Agent Skills (GitSkills):** Reading difficulty and structural complexity 
- **Comparison Strategy:** Normalize both datasets and compare the distributions
- **Visualization Strategy:** Create distribution graphs for the cognitive complexity per file and reading difficulty/structural complexity per file.

## 4. Project Approach & Workflow
- **Script-Driven Pipeline:** All data gathering, calculation, comparison, and plotting are implemented as modular, executable Python scripts in `scripts/` (no autonomous subagents).
- **Prioritize Existing Scripts:** Build upon and integrate foundational scripts already created by teammates (such as `scripts/history_metrics.py` and `scripts/compare_history.py`) rather than replacing them.
- **Two-Stage Mining Process:**
  1. *Validation Test Run:* Stream and sample ~100 lines/records to ensure remote connectivity, field parsing, and output formatting are working properly.
  2. *Production Analysis Chunk:* Scale up to the full sample size for the actual statistical analysis.

## 5. Proposed Outcomes & Deliverables
- **Standardized Tabular Data:** Consistent CSV/JSON files containing extracted metrics for both source code and skills.
- **Cross-Domain Statistical Comparisons:** Summary tables reporting central tendencies (medians, means), spreads (IQR, standard deviation), and non-parametric statistical tests (Mann-Whitney U, Cliff's Delta effect size).
- **Publication-Ready Distribution Graphs:** Clear visualizations (log-scaled violin/box plots, ECDFs, and KDEs) illustrating the distributional comparisons between source code and skills.

## 6. Constraints & Guard Rails
- **No Full Dataset Downloads:** Datasets are too large. Access data remotely through streaming (`streaming=True`), range queries, or blobless Git clones.
- **Deterministic & Reproducible:** Scripts must support CLI parameters (`--samples`, `--seed`, `--output`, `--snapshot-date`) so results can be reliably reproduced.
