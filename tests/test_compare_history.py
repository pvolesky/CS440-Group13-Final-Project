
import csv
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch
import sys

sys.path.insert(
    0, str(Path(__file__).resolve().parents[1] / "scripts")
)

from compare_history import (
    load_results,
    summarize,
    save_summary,
    create_graph,
    main,
)


class CompareHistoryTests(unittest.TestCase):

    def setUp(self):
        self.skills = [
            {
                "file": "skill1/SKILL.md",
                "revision_count": 2,
                "days_since_last_edit": 5.0,
            },
            {
                "file": "skill2/SKILL.md",
                "revision_count": 4,
                "days_since_last_edit": 15.0,
            },
        ]

        self.source = [
            {
                "file": "src/main.py",
                "revision_count": 6,
                "days_since_last_edit": 10.0,
            },
            {
                "file": "src/utils.py",
                "revision_count": 8,
                "days_since_last_edit": 20.0,
            },
        ]

    def write_csv(self, path, rows):
        with open(path, "w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(
                file,
                fieldnames=[
                    "file",
                    "revision_count",
                    "days_since_last_edit",
                ],
            )
            writer.writeheader()
            writer.writerows(rows)

    def test_load_results(self):
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / "skills.csv"
            self.write_csv(path, self.skills)

            loaded = load_results(path)

            self.assertEqual(loaded, self.skills)

    def test_summary_statistics(self):
        summary = summarize(self.skills, "Agent Skills")

        churn = next(
            row for row in summary
            if row["metric"] == "revision_count"
        )

        age = next(
            row for row in summary
            if row["metric"] == "days_since_last_edit"
        )

        self.assertEqual(churn["count"], 2)
        self.assertEqual(churn["mean"], 3)
        self.assertEqual(churn["median"], 3)
        self.assertEqual(churn["minimum"], 2)
        self.assertEqual(churn["maximum"], 4)

        self.assertEqual(age["mean"], 10)
        self.assertEqual(age["median"], 10)

    def test_invalid_csv(self):
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / "invalid.csv"
            path.write_text(
                "file,revision_count\nskill1,2\n",
                encoding="utf-8",
            )

            with self.assertRaises(ValueError):
                load_results(path)

    def test_graph_creation(self):
        with tempfile.TemporaryDirectory() as temp:
            output = Path(temp) / "churn.png"

            create_graph(
                self.skills,
                self.source,
                "revision_count",
                output,
            )

            self.assertTrue(output.exists())
            self.assertGreater(output.stat().st_size, 0)

    def test_full_comparison(self):
        with tempfile.TemporaryDirectory() as temp:
            temp = Path(temp)

            skills_csv = temp / "skills.csv"
            source_csv = temp / "source.csv"
            output_dir = temp / "results"

            self.write_csv(skills_csv, self.skills)
            self.write_csv(source_csv, self.source)

            with patch.object(
                sys,
                "argv",
                [
                    "compare_history.py",
                    "--skills", str(skills_csv),
                    "--source", str(source_csv),
                    "--output-dir", str(output_dir),
                ],
            ):
                main()

            self.assertTrue(
                (output_dir / "history_summary.csv").exists()
            )
            self.assertTrue(
                (output_dir / "revision_count_comparison.png").exists()
            )
            self.assertTrue(
                (output_dir / "days_since_last_edit_comparison.png").exists()
            )


if __name__ == "__main__":
    unittest.main()
