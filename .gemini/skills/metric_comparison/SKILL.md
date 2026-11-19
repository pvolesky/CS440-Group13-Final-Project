---
name: metric-comparison
description: >-
  Use this skill when authoring, reviewing, or executing Python scripts to compare concrete metrics
  representing the same overarching construct (such as comparing Lines of Code vs. Tokens under Size, or commit revisions vs. prompt edits under Churn)
  across heterogeneous domains like source code and agent skills.
---

# Cross-Domain Metric Comparison & Equivalency

This skill provides guidelines and general procedures for building and executing Python scripts that map, normalize, and statistically compare diverse concrete metrics representing the same overarching software engineering construct across heterogeneous artifacts (such as traditional source code and natural-language LLM agent skills).

---

## 1. Overarching Construct Architecture

Different software representations employ different native measurement units to express the same fundamental attribute. Comparative scripts must map specific variables to their overarching category before running comparisons.

```
                  +-----------------------------------------+
                  |           Overarching Metric            |
                  |               (e.g., SIZE)              |
                  +--------------------+--------------------+
                                       |
                   +-------------------+-------------------+
                   |                                       |
                   v                                       v
         +--------------------+                  +--------------------+
         |    Source Code     |                  |    Agent Skills    |
         |  Concrete Metrics  |                  |  Concrete Metrics  |
         +--------------------+                  +--------------------+
         | - Physical LOC     |                  | - Markdown LOC     |
         | - Source SLOC      |                  | - Token Count      |
         | - Token Count      |                  | - Section Count    |
         | - AST Node Count   |                  | - Instruction Qty  |
         +--------------------+                  +--------------------+
```

### Core Metric Mappings

* **Size (Informational Volume):**
  * *Source Code:* Lines of Code (LOC / SLOC), lexer tokens, AST nodes, byte count.
  * *Agent Skills:* Formatted lines of text, BPE token counts (`tiktoken`/`cl100k`), header/section counts, instruction bullet counts.
  * *Equivalency Strategy:* BPE token counts provide a universal baseline across both code and natural language text.
* **Churn (Evolutionary Volatility):**
  * *Source Code:* Commit frequency, revision counts over a time window, lines added/deleted.
  * *Agent Skills:* Revision counts over a time window, prompt update frequency, instruction replacement churn.
  * *Equivalency Strategy:* Standardize by measuring revisions within a fixed observation window (e.g. 180 or 365 days) up to a common snapshot date.
* **Age (Temporal Lifecycle):**
  * *Source Code:* Days since last edit (staleness/recency), total days from initial commit to snapshot (longevity).
  * *Agent Skills:* Days since last prompt modification, total days since skill introduction.
  * *Equivalency Strategy:* Measure both staleness and longevity relative to a fixed evaluation timestamp.
* **Clone Coverage (Redundancy & Duplication):**
  * *Source Code:* Type-1 (exact), Type-2 (parameterized), Type-3 (gapped) code clones.
  * *Agent Skills:* Exact prompt matches, template variable substitutions, boilerplate scaffolding reuse.
  * *Equivalency Strategy:* Token n-gram shingling, MinHash, and Jaccard similarity ($\ge 80\%$).
* **Readability (Comprehension & Cognitive Load):**
  * *Source Code:* Readability models (Buse-Weimer, Posnett), cyclomatic complexity, comment-to-code ratios.
  * *Agent Skills:* Natural language readability indices (Flesch-Kincaid Grade Level, Flesch Reading Ease, Gunning Fog).
  * *Equivalency Strategy:* Evaluate text/comment readability and cross-domain lexical entropy.

---

## 2. Normalization & Standardization Methods

Because raw units are rarely on the same scale (e.g., 200 lines of code vs. 1,500 tokens of prompt text), comparison scripts should apply appropriate transformations:

1. **Logarithmic Scaling (for Heavy Tails):**
   * Software metrics typically follow power-law or skewed distributions. Use $\log_{10}(x + 1)$ to stabilize variance and allow proportional comparisons across orders of magnitude.
2. **Min-Max Scaling (Bounded 0 to 1):**
   * $x_{\text{norm}} = \frac{x - x_{\min}}{x_{\max} - x_{\min}}$, useful when bounding scores within a normalized $[0.0, 1.0]$ range.
3. **Percentile / Quantile Rank Transformation:**
   * Convert each observation to its percentile within its respective domain. This answers: *"Is this skill at the 90th percentile of skill size just as this function is at the 90th percentile of code size?"*
4. **Conversion Ratio Analysis:**
   * Calculate empirical conversion factors (e.g., median ratio of $\text{Tokens} / \text{Lines}$) to understand structural density across domains.

---

## 3. Statistical Comparison Principles for Scripts

When comparing distributions across domains:

* **Do Not Assume Normality:** Software metrics and text metrics almost always violate normal distribution assumptions; avoid standard Student's t-tests or Pearson correlations without validation.
* **Implement Non-Parametric Tests:**
  * **Mann-Whitney U Test:** Determines whether values from one domain are stochastically greater than the other.
  * **Kolmogorov-Smirnov Test:** Assesses whether the cumulative distribution shapes differ significantly.
* **Quantify Effect Size (Cliff's Delta):**
  * Calculate Cliff's Delta ($\delta$) alongside p-values to measure practical magnitude:
    * $|\delta| < 0.147$: Negligible
    * $0.147 \le |\delta| < 0.330$: Small
    * $0.330 \le |\delta| < 0.474$: Medium
    * $|\delta| \ge 0.474$: Large
* **Report Robust Summaries:** Always output Median and Interquartile Range (IQR) alongside Mean and Standard Deviation into output JSON or CSV summaries.

