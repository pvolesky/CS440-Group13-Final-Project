
import os
import subprocess
import tempfile
import unittest
from pathlib import Path
from sys import path

path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

from history_metrics import measure_file, parse_date


class HistoryMetricsTests(unittest.TestCase):

    def test_two_commits_and_fixed_age(self):
        with tempfile.TemporaryDirectory() as temp:
            repo = Path(temp)

            subprocess.run(
                ["git", "init", "-q", str(repo)], check=True
            )
            subprocess.run(
                ["git", "-C", str(repo), "config",
                 "user.name", "Test"], check=True
            )
            subprocess.run(
                ["git", "-C", str(repo), "config",
                 "user.email", "test@example.com"], check=True
            )

            sample = repo / "sample.txt"

            for day in (10, 12):
                sample.write_text(f"updated {day}\n")
                subprocess.run(
                    ["git", "-C", str(repo), "add", "sample.txt"],
                    check=True,
                )

                env = os.environ.copy()
                timestamp = f"2026-11-{day}T12:00:00+00:00"
                env["GIT_AUTHOR_DATE"] = timestamp
                env["GIT_COMMITTER_DATE"] = timestamp

                subprocess.run(
                    ["git", "-C", str(repo), "commit",
                     "-qm", f"update {day}"],
                    env=env,
                    check=True,
                )

            snapshot = parse_date("2026-11-15T12:00:00Z")

            metrics = measure_file(
                repo, "sample.txt", snapshot
            )

            self.assertEqual(metrics["revision_count"], 2)
            self.assertEqual(
                metrics["days_since_last_edit"], 3.0
            )

            recent = measure_file(
                repo, "sample.txt", snapshot, window_days=4
            )
            self.assertEqual(recent["revision_count"], 1)

    def test_requires_timezone(self):
        with self.assertRaises(Exception):
            parse_date("2026-11-15")


if __name__ == "__main__":
    unittest.main()
