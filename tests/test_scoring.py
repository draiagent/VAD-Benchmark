import json
import unittest
from pathlib import Path

from scripts.score import completion_rate, compute_metrics, prompt_reduction, weighted_error
from scripts.validate_study import validate_config


ROOT = Path(__file__).resolve().parents[1]


class ScoringTests(unittest.TestCase):
    def test_completion_rate(self):
        self.assertEqual(completion_rate(8, 10), 80.0)

    def test_completion_rate_rejects_invalid(self):
        with self.assertRaises(ValueError):
            completion_rate(11, 10)

    def test_weighted_error(self):
        self.assertEqual(weighted_error(1, 2, 3), 14)

    def test_prompt_reduction(self):
        self.assertEqual(prompt_reduction(100, 25), 0.75)

    def test_sample_run_metrics(self):
        record = json.loads((ROOT / "examples/sample-run.json").read_text(encoding="utf-8"))
        metrics = compute_metrics(record)
        self.assertEqual(metrics["completion_rate"], 80.0)
        self.assertEqual(metrics["weighted_error"], 5)
        self.assertEqual(metrics["first_pass_yield"], 0)

    def test_canonical_study_config(self):
        config = json.loads((ROOT / "configs/study-v0.1.0.json").read_text(encoding="utf-8"))
        validate_config(config)


if __name__ == "__main__":
    unittest.main()
