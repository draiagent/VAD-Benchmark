from pathlib import Path
import json
import tempfile
import unittest

from scripts.build_pilot_matrix import build_matrix
from scripts.validate_task_packs import validate_task_packs


ROOT = Path(__file__).resolve().parents[1]
CONFIG = ROOT / "configs/study-v0.2.0.json"
SCHEMA = ROOT / "schemas/task-pack.schema.json"


class FivePackTaskTests(unittest.TestCase):
    def test_all_five_task_packs_validate(self):
        packs = validate_task_packs(CONFIG, SCHEMA, ROOT)
        self.assertEqual(len(packs), 5)
        self.assertEqual(
            [p["task_family"] for p in packs],
            ["video", "slides", "web", "data", "report"],
        )
        self.assertEqual(len({p["task_id"] for p in packs}), 5)

    def test_repo_fixtures_exist(self):
        packs = validate_task_packs(CONFIG, SCHEMA, ROOT)
        for pack in packs:
            for asset in pack["inputs"]:
                if asset["source"] == "repo_fixture":
                    self.assertTrue((ROOT / asset["path"]).exists(), asset["path"])

    def test_vad_matrix_size(self):
        config = json.loads(CONFIG.read_text(encoding="utf-8"))
        rows = build_matrix(config, ROOT, "vad", ["fixture:model:1:ci"], 2)
        self.assertEqual(len(rows), 5 * 6 * 1 * 2)
        self.assertEqual(len({row["run_plan_id"] for row in rows}), len(rows))

    def test_promptless_matrix_size(self):
        config = json.loads(CONFIG.read_text(encoding="utf-8"))
        rows = build_matrix(config, ROOT, "promptless", ["fixture:model:1:ci"], 1)
        self.assertEqual(len(rows), 5 * 3)


if __name__ == "__main__":
    unittest.main()
