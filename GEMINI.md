# MSR 2027 Mining Challenge

## Architecture & Project Approach
- **Script-Driven Pipeline (No Autonomous Agents):** We do not use autonomous subagents. All data collection, metric computation, comparison, and visualization must be implemented as standalone, executable Python scripts in `scripts/`.
- **Gemini's Role:** Assist developers in building, refining, testing, and documenting modular Python scripts and files using the project skills. All code must be runnable via CLI on demand by team members or CI workflows.

## Existing Scripts & Modification Policy
- **Prioritize and Reuse Existing Scripts:** Teammates have already authored foundational scripts in `scripts/` (e.g., `scripts/history_metrics.py`, `scripts/compare_history.py`). Gemini must leverage and integrate these existing scripts for producing final outputs rather than replacing or rewriting them from scratch.
- **Allowed Minor Enhancements:** Minor, backward-compatible improvements (such as adding CLI arguments, improving error handling, or minor formatting/output adjustments) are permitted if they benefit the overall pipeline.
- **Major Changes Require User Approval:** Any major structural overhaul, algorithmic rewrite, or breaking change to existing scripts must be explicitly explained and brought to the user's attention for approval before making changes.

## Datasets
1. **GitSkills:** https://huggingface.co/datasets/mvaccargiu/gitskills (Agent skills: Size [Tokens], Clone Coverage, Readability)
2. **TheStack:** https://huggingface.co/datasets/bigcode/the-stack (Source code: Size [LOC], Clone Coverage, Readability)
3. **Dataset 3 (TBD):** Placeholder - To be determined (Churn, Age)
4. **Dataset 4 (TBD):** Placeholder - To be determined (Churn, Age)

## Metric Specifications
1. **Size:**
   - **Source Code (TheStack):** Number of lines of code per file (LOC).
   - **Agent Skills (GitSkills):** Token count per skill file.
   - **Comparison:** Normalize both datasets and compare empirical distributions.
   - **Visualization:** Distribution graph for both lines of code per file and tokens per file.
2. **Churn:** TBD
3. **Age:** TBD
4. **Clone Coverage:** 
- **Source Code (TheStack):** Code duplication (% similarity / duplicate code per file)
- **Agent Skills (GitSkills):** Exact and near duplication
- **Comparison Strategy:** Direct comparison of distributions
- **Visualization Strategy:** Create distribution graphs for the code duplication per file and exact and near duplication per file.
5. **Readability:** 
- **Source Code (TheStack):** Cognitive complexity
- **Agent Skills (GitSkills):** Reading difficulty and structural complexity 
- **Comparison Strategy:** Normalize both datasets and compare the distributions
- **Visualization Strategy:** Create distribution graphs for the cognitive complexity per file and reading difficulty/structural complexity per file.

## Objectives
- Analyze which established software engineering metrics (Size, Churn, Age, Clone Coverage, Readability) have meaningful equivalents for agent skills, and compare their empirical distributions against source code.
- Build modular Python extraction scripts for each dataset to gather target variables into standardized tabular formats.
- Gather Size (Tokens for GitSkills, LOC for TheStack), Clone Coverage, and Readability from GitSkills and TheStack using remote streaming.
- Gather Churn and Age from TBD datasets (Datasets 3 and 4) using history analysis scripts.
- Run statistical comparisons across representations representing the same overarching metric (Lines of Code vs. Tokens for Size).
- Generate publication-quality distribution graphs (violin/box plots, ECDFs, KDEs) comparing source code distributions to skill distributions.

## Guard Rails & Script Standards
- **Never Download Full Datasets:** Datasets are too large. Scripts must query, stream (`streaming=True`), or aggregate remotely.
- **Two-Stage Mining Workflow (Test Run First):** Always perform a small test run first (sampling ~100 records/lines of data) to verify streaming connectivity, schema alignment, metric calculations, and output formatting before scaling up to larger chunks for full analysis.
- **VCS Mining:** Use blobless (`--filter=blob:none`) or shallow clones for Git history mining.
- **CLI Interface:** All scripts in `scripts/` must be executable from the command line, accept arguments via `argparse` (e.g., `--output`, `--snapshot-date`, `--samples`, `--seed`), and output standardized CSV/JSON files.
- **Reference Skills:** When authoring scripts, Gemini must adhere to the instructions and guidelines in `.gemini/skills/`:
  - `.gemini/skills/remote_dataset_mining/SKILL.md`: For streaming and remote querying.
  - `.gemini/skills/metric_comparison/SKILL.md`: For metric normalization and statistical testing.
  - `.gemini/skills/distribution_visualization/SKILL.md`: For graph formatting and distribution plotting.
