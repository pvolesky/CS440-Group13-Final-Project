
# Churn and Age Analysis

## CS 440 Group 13 Final Project

### Research Question

Which established software engineering metrics have meaningful
equivalents for AI agent skills, and how do their distributions
compare with traditional source code?

This section focuses on two metrics: churn and age.

## 1. Objective

The goal of this analysis is to compare how frequently AI agent
skills and traditional source-code files are modified and how
recently they were updated.

We developed a Python script that examines Git commit history
and calculates churn and age for individual files.

We then compared the results using descriptive statistics and
distribution graphs.

## 2. Datasets

We used two publicly available GitHub repositories:

**Agent Skills**
- Repository: https://github.com/anthropics/skills
- Files analyzed: 20 SKILL.md files

**Traditional Source Code**
- Repository: https://github.com/pallets/click
- Files analyzed: 17 Python files from the src directory

These repositories were selected as initial examples to test
our approach using real Git history.

They are not the complete GitSkills and TheStack datasets.

## 3. Methodology

### Churn

Churn measures how often a file has been revised.

For this analysis, we counted the number of commits affecting
each file during a 365-day observation window.

A higher revision count indicates that the file appeared in
more commits during that period.

This measures commit frequency, not the number of lines added
or deleted.

### Age

Age measures the number of days between the snapshot date and
the most recent recorded commit affecting a file.

A lower age means the file was edited more recently.

### Measurement Settings

- Snapshot date: November 15, 2026, at 23:59:59 UTC
- Churn observation window: 365 days
- Measurement unit: Individual files
- History source: Git commit history
- Output format: CSV

Both repositories were analyzed using the same snapshot date
and observation window.

### Implementation

The analysis uses:

- scripts/history_metrics.py
- scripts/compare_history.py
- tests/test_history_metrics.py
- tests/test_compare_history.py
- .github/workflows/compare-history.yml

The history script calculates metrics from Git commits.

The comparison script calculates descriptive statistics and
generates distribution graphs using Matplotlib.

Automated tests verify the calculations and output generation.

## 4. Results

### Churn Comparison

| Statistic | Agent Skills | Source Code |
|---|---:|---:|
| Files analyzed | 20 | 17 |
| Mean revisions | 3.600 | 11.353 |
| Median revisions | 2 | 6 |
| Standard deviation | 5.398 | 11.762 |
| Minimum revisions | 1 | 0 |
| Maximum revisions | 26 | 50 |

The source-code files had a higher average revision count
than the agent skills.

Source code averaged 11.353 revisions, while agent skills
averaged 3.600 revisions.

The median revision count was also higher for source code,
with 6 revisions compared with 2 for agent skills.

In this sample, source-code files experienced more frequent
revisions during the observation period.

### Age Comparison

| Statistic | Agent Skills | Source Code |
|---|---:|---:|
| Mean age (days) | 203.258 | 99.824 |
| Median age (days) | 300.225 | 9.690 |
| Standard deviation | 154.810 | 217.713 |
| Minimum age (days) | 1.360 | 1.540 |
| Maximum age (days) | 349.250 | 935.240 |

The agent skills had a higher average age than the source-code
files.

Agent skills averaged 203.258 days since their last edit,
compared with 99.824 days for source code.

The difference was especially noticeable in the medians.

The median skill age was 300.225 days, while the median
source-code age was only 9.690 days.

This suggests that the source-code files in our sample
were generally updated more recently.

## 5. Visualizations

The comparison workflow generates two figures:

**Figure 1: Churn Distribution**
- File: results/revision_count_comparison.png
- Compares revision-count distributions for agent skills
  and source code.

**Figure 2: Age Distribution**
- File: results/days_since_last_edit_comparison.png
- Compares days since the last edit for both datasets.

Each figure displays separate histograms for the two
file categories.

These graphs help illustrate differences in the frequency
and recency of file modifications.

## 6. Discussion

The initial results suggest that traditional source-code
files may undergo more frequent revisions than AI agent skills.

The source-code files had higher mean and median revision
counts.

Agent skills also had a much higher median age, suggesting
that many skills in this sample had not been modified recently.

One possible explanation is that source code often changes
as software is maintained, while some agent skills may remain
stable after their initial development.

However, our results cannot establish why these differences
occur.

The two repositories may have different development practices,
project histories, and maintenance schedules.

Additional datasets would be necessary to determine whether
these patterns are common across software projects.

## 7. Limitations

Several limitations should be considered.

1. The sample includes only 20 agent skills and 17 source-code
   files from two repositories.

2. These results may not represent the broader population of
   AI agent skills or traditional source code.

3. Revision count measures commits affecting a file, rather
   than the number of lines modified.

4. The repositories have different development histories,
   which may influence the results.

5. The age calculation uses the most recent recorded commit
   affecting each file, rather than the file's creation date.

6. The source-code dataset contains an older file with an age
   of 935.240 days, which affects the mean.

7. The analysis uses descriptive statistics and does not
   establish statistical significance.

8. The current implementation analyzes files present in the
   checked-out repositories, rather than a historical snapshot
   of the complete file tree.

These limitations mean that our findings should be considered
preliminary.

## 8. Conclusion

Our proof-of-concept analysis demonstrates that churn and age
can be measured for AI agent skills using methods similar to
those applied to traditional source code.

In our sample, source-code files had higher revision counts
and were generally modified more recently than agent skills.

The results support using Git history as a practical way to
compare maintenance-related characteristics across these
two types of files.

Future work should expand the analysis to more repositories
and larger datasets, including historical data relevant to
GitSkills and TheStack.

A larger and more representative sample would help determine
whether the observed differences persist across projects.

## 9. Reproducibility

The analysis can be reproduced using the GitHub Actions
workflow:

.github/workflows/compare-history.yml

The workflow:

1. Runs automated tests.
2. Clones the two example repositories.
3. Extracts churn and age measurements.
4. Filters agent skills and Python source files.
5. Generates descriptive statistics and comparison graphs.
6. Uploads the results as downloadable artifacts.

The generated output includes:

- skills_results.csv
- source_results.csv
- history_summary.csv
- revision_count_comparison.png
- days_since_last_edit_comparison.png

All numerical results in this document come from the
generated history_summary.csv file.
