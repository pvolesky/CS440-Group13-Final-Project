---
name: distribution-visualization
description: >-
  Use this skill when authoring, reviewing, or executing Python scripts to design, generate, and export
  distribution graphs and figures (such as box plots, violin plots, KDEs, and ECDFs) comparing metric distributions between source code and agent skills.
---

# Metric Distribution Visualization & Graphing

This skill provides guidelines and general procedures for building and executing Python scripts that create, format, and export publication-ready distribution graphs comparing software engineering metrics across different representations (such as source code vs. agent skills).

---

## 1. Selecting the Appropriate Distribution Plot

Software and prompt metrics exhibit high variance, extreme right-skew, and outliers. Scripts should select the plot that best reveals the underlying data distribution:

| Plot Type | Best Suited For | Key Analytical Strengths |
| :--- | :--- | :--- |
| **Log-Scaled Violin & Box Plots** | Size (LOC/Tokens), Churn (Revisions), Age (Days) | Shows median, interquartile range (IQR), multi-modal density shapes, and outlier spread in one view. |
| **Empirical Cumulative Distribution Function (ECDF)** | Direct percentile comparison across domains | Free of arbitrary binning; demonstrates stochastic dominance and exact quantile shifts between Code and Skills. |
| **Kernel Density Estimation (KDE)** | Readability scores, lexical density, normalized $[0, 1]$ indices | Provides smooth probability density curves for continuous metrics. |
| **Grouped Histograms / Bar Charts** | Clone coverage percentages, discrete section/instruction counts | Highlights categorical proportions and frequency bins clearly. |

---

## 2. Visualization Standards & Script Best Practices

To ensure generated figures are clean, accessible, and suitable for technical research papers:

1. **Logarithmic Scaling for Skewed Metrics:**
   * When data spans multiple orders of magnitude (e.g., sizes from 10 to 100,000 tokens), configure plot axes logarithmically (`yscale="log"` or `xscale="log"`).
   * Protect against zero values using pseudo-log scaling or offset variables ($\log_{10}(x + 1)$).
   * Use readable tick formatting ($10^1, 10^2, 10^3, 10^4$).
2. **Accessible, Distinct Color Palettes:**
   * Use colorblind-friendly color schemes with distinct contrast for the compared domains (e.g., deep slate blue for `source_code` and warm rust/orange for `agent_skill`).
3. **Statistical Annotations:**
   * Explicitly display medians and quartiles.
   * Annotate plots with statistical test results: sample size ($N$), Mann-Whitney U test p-value, and Cliff's Delta ($\delta$) effect size.
4. **Dual Export Formats:**
   * Export both vector formats (`.pdf` or `.svg`) for LaTeX paper inclusion and high-DPI raster images (`.png` at 300+ DPI) for quick inspection.
5. **Headless Execution:**
   * Configure matplotlib to use the non-interactive Agg backend (`matplotlib.use("Agg")`) so scripts run reliably in automated environments and CI pipelines.

---

## 3. General Plot Layouts for Metric Comparisons

### Multi-Metric Comparative Dashboard
When visualizing the full five-metric analysis (Size, Churn, Age, Clone Coverage, Readability), scripts should generate a structured multi-panel figure:
* **Panel A (Size):** Log-scaled side-by-side violin/box plot comparing code tokens vs. skill tokens.
* **Panel B (Churn):** ECDF curve comparing revisions in window between code and skills.
* **Panel C (Age):** ECDF or survival curve showing days since last modification.
* **Panel D (Clone Coverage):** Density histogram of duplicate token percentages.
* **Panel E (Readability):** Overlapping KDE curves for readability grade levels.
* **Panel F (Summary):** Statistical summary table listing medians, IQRs, and effect sizes.

---

## 4. Script Execution Workflow

1. **Parse CLI Arguments:** Accept input CSV/JSON path, output figure directory, and format choices.
2. **Inspect Input Distribution:** Check minimums, maximums, zeros, and skewness of the input data.
3. **Apply Axis Transformations:** Enable log scaling for heavy-tailed counts (size, revisions, days).
4. **Render Figures:** Generate plots with consistent fonts, labels, legends, and high-contrast color mappings.
5. **Save to Artifacts:** Output vector (`.pdf`) and raster (`.png`) files into the specified directory (e.g., `results/figures/`).
---
name: distribution-visualization
description: >-
  Use this skill when authoring, reviewing, or executing Python scripts to design, generate, and export
  distribution graphs and figures (such as box plots, violin plots, KDEs, and ECDFs) comparing metric distributions between source code and agent skills.
---

# Metric Distribution Visualization & Graphing

This skill provides guidelines and general procedures for building and executing Python scripts that create, format, and export publication-ready distribution graphs comparing software engineering metrics across different representations (such as source code vs. agent skills).

---

## 1. Selecting the Appropriate Distribution Plot

Software and prompt metrics exhibit high variance, extreme right-skew, and outliers. Scripts should select the plot that best reveals the underlying data distribution:

| Plot Type | Best Suited For | Key Analytical Strengths |
| :--- | :--- | :--- |
| **Log-Scaled Violin & Box Plots** | Size (LOC/Tokens), Churn (Revisions), Age (Days) | Shows median, interquartile range (IQR), multi-modal density shapes, and outlier spread in one view. |
| **Empirical Cumulative Distribution Function (ECDF)** | Direct percentile comparison across domains | Free of arbitrary binning; demonstrates stochastic dominance and exact quantile shifts between Code and Skills. |
| **Kernel Density Estimation (KDE)** | Readability scores, lexical density, normalized $[0, 1]$ indices | Provides smooth probability density curves for continuous metrics. |
| **Grouped Histograms / Bar Charts** | Clone coverage percentages, discrete section/instruction counts | Highlights categorical proportions and frequency bins clearly. |

---

## 2. Visualization Standards & Script Best Practices

To ensure generated figures are clean, accessible, and suitable for technical research papers:

1. **Logarithmic Scaling for Skewed Metrics:**
   * When data spans multiple orders of magnitude (e.g., sizes from 10 to 100,000 tokens), configure plot axes logarithmically (`yscale="log"` or `xscale="log"`).
   * Protect against zero values using pseudo-log scaling or offset variables ($\log_{10}(x + 1)$).
   * Use readable tick formatting ($10^1, 10^2, 10^3, 10^4$).
2. **Accessible, Distinct Color Palettes:**
   * Use colorblind-friendly color schemes with distinct contrast for the compared domains (e.g., deep slate blue for `source_code` and warm rust/orange for `agent_skill`).
3. **Statistical Annotations:**
   * Explicitly display medians and quartiles.
   * Annotate plots with statistical test results: sample size ($N$), Mann-Whitney U test p-value, and Cliff's Delta ($\delta$) effect size.
4. **Dual Export Formats:**
   * Export both vector formats (`.pdf` or `.svg`) for LaTeX paper inclusion and high-DPI raster images (`.png` at 300+ DPI) for quick inspection.
5. **Headless Execution:**
   * Configure matplotlib to use the non-interactive Agg backend (`matplotlib.use("Agg")`) so scripts run reliably in automated environments and CI pipelines.

---

## 3. General Plot Layouts for Metric Comparisons

### Multi-Metric Comparative Dashboard
When visualizing the full five-metric analysis (Size, Churn, Age, Clone Coverage, Readability), scripts should generate a structured multi-panel figure:
* **Panel A (Size):** Log-scaled side-by-side violin/box plot comparing code tokens vs. skill tokens.
* **Panel B (Churn):** ECDF curve comparing revisions in window between code and skills.
* **Panel C (Age):** ECDF or survival curve showing days since last modification.
* **Panel D (Clone Coverage):** Density histogram of duplicate token percentages.
* **Panel E (Readability):** Overlapping KDE curves for readability grade levels.
* **Panel F (Summary):** Statistical summary table listing medians, IQRs, and effect sizes.

---

## 4. Script Execution Workflow

1. **Parse CLI Arguments:** Accept input CSV/JSON path, output figure directory, and format choices.
2. **Inspect Input Distribution:** Check minimums, maximums, zeros, and skewness of the input data.
3. **Apply Axis Transformations:** Enable log scaling for heavy-tailed counts (size, revisions, days).
4. **Render Figures:** Generate plots with consistent fonts, labels, legends, and high-contrast color mappings.
5. **Save to Artifacts:** Output vector (`.pdf`) and raster (`.png`) files into the specified directory (e.g., `results/figures/`).

