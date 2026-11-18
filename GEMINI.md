# MSR 2027 Mining Challenge

## Datasets
GitSkills - https://huggingface.co/datasets/mvaccargiu/gitskills
TheStack - https://huggingface.co/datasets/bigcode/the-stack
undetermined -
undetermined -

## Objectives
- using a certain number of datasets we will analyze which established metrics, such as size, churn, age, clone coverage, and readability, have meaningful equivalents for skills, and how do their distributions compare with those of source code.
-use (4 change if number changes) datasets each with their associated sub agent to to gather certain of these variables from their respective dataset
-Use the GitSkills and TheStack databases to gather info for size, clone average, and readability
-Use undetermined to gather info for churn and age
-Once all of the info is gathered compare the variables of the source code metrics to those of the GitSkills metrics

## Guard rails
-never attempt to download the entire dataset as they are incredibly large. Instead we should query, stream, or aggregate them remotely

## Subagents