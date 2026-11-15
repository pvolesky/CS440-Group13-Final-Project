
import argparse
import csv
import subprocess
from datetime import datetime, timezone
from pathlib import Path


def git_output(repo, *args):
    result = subprocess.run(
        ["git", "-C", str(repo), *args],
        capture_output=True,
        text=True,
        check=True,
    )
    return result.stdout.strip()


def measure_file(repo, file_path, snapshot_date):
    history = git_output(
        repo,
        "log",
        "--follow",
        "--format=%H|%cI",
        "--",
        file_path,
    )

    if not history:
        return None

    commits = history.splitlines()
    latest_date = max(
        datetime.fromisoformat(line.rsplit("|", 1)[1])
        for line in commits
    )

    age_days = (
        snapshot_date - latest_date
    ).total_seconds() / 86400

    return {
        "file": file_path,
        "revision_count": len(commits),
        "days_since_last_edit": round(age_days, 2),
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("repo", type=Path)
    parser.add_argument("--output", default="history_metrics.csv")
    args = parser.parse_args()

    repo = args.repo.resolve()
    snapshot_date = datetime.now(timezone.utc)

    files = git_output(
        repo, "ls-files"
    ).splitlines()

    results = []
    for file_path in files:
        result = measure_file(repo, file_path, snapshot_date)
        if result:
            results.append(result)

    with open(args.output, "w", newline="") as output:
        writer = csv.DictWriter(
            output,
            fieldnames=[
                "file",
                "revision_count",
                "days_since_last_edit",
            ],
        )
        writer.writeheader()
        writer.writerows(results)

    print(f"Analyzed {len(results)} files.")
    print(f"Results saved to {args.output}")


if __name__ == "__main__":
    main()
