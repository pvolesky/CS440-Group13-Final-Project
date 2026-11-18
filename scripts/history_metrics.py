
import argparse
import csv
import subprocess
import sys
from datetime import datetime, timezone, timedelta
from pathlib import Path


def parse_date(value):
    try:
        date = datetime.fromisoformat(
            value.replace("Z", "+00:00")
        )
    except ValueError as exc:
        raise argparse.ArgumentTypeError(
            "Use ISO 8601, e.g. 2026-11-15T00:00:00Z"
        ) from exc

    if date.tzinfo is None:
        raise argparse.ArgumentTypeError(
            "Snapshot date must include a timezone"
        )
    return date.astimezone(timezone.utc)


def git_output(repo, *args):
    result = subprocess.run(
        ["git", "-C", str(repo), *args],
        capture_output=True,
        text=True,
        check=False,
    )
    if result.returncode:
        raise RuntimeError(
            f"Git command failed: {result.stderr.strip()}"
        )
    return result.stdout


def measure_file(repo, file_path, snapshot_date, window_days=None):
    history = git_output(
        repo, "log", "--follow", "--format=%H|%cI",
        "--", file_path
    )

    dates = []
    for line in history.splitlines():
        if "|" not in line:
            continue
        commit_date = datetime.fromisoformat(
            line.rsplit("|", 1)[1]
        ).astimezone(timezone.utc)
        if commit_date <= snapshot_date:
            dates.append(commit_date)

    if not dates:
        return None

    latest = max(dates)
    cutoff = (
        snapshot_date - timedelta(days=window_days)
        if window_days is not None else None
    )
    revision_count = (
        sum(date >= cutoff for date in dates)
        if cutoff else len(dates)
    )

    return {
        "file": file_path,
        "revision_count": revision_count,
        "days_since_last_edit": round(
            (snapshot_date - latest).total_seconds() / 86400, 2
        ),
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("repo", type=Path)
    parser.add_argument(
        "--output", default="history_metrics.csv"
    )
    parser.add_argument(
        "--snapshot-date",
        type=parse_date,
        default=datetime.now(timezone.utc),
        help="ISO 8601 timestamp, e.g. 2026-11-15T00:00:00Z",
    )
    parser.add_argument(
        "--window-days", type=int, default=None
    )
    args = parser.parse_args()

    if args.window_days is not None and args.window_days <= 0:
        parser.error("--window-days must be positive")

    try:
        files = git_output(
            args.repo.resolve(), "ls-files", "-z"
        ).split("\0")

        results = []
        for file_path in files:
            if file_path:
                metric = measure_file(
                    args.repo.resolve(),
                    file_path,
                    args.snapshot_date,
                    args.window_days,
                )
                if metric is not None:
                    results.append(metric)

        with open(
            args.output, "w", newline="", encoding="utf-8"
        ) as output:
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

    except (RuntimeError, OSError) as exc:
        print(f"Error: {exc}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
