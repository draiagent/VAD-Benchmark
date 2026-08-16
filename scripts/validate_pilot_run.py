#!/usr/bin/env python3
"""Cross-check a v0.2 Pilot run record against its canonical Task Pack."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def find_pack(config: dict[str, Any], root: Path, task_id: str) -> dict[str, Any]:
    for relative in config["task_packs"]:
        pack = load_json(root / relative)
        if pack["task_id"] == task_id:
            return pack
    raise ValueError(f"task_id not found in study config: {task_id}")


def validate_pilot_run(run: dict[str, Any], config: dict[str, Any], root: Path) -> None:
    if run.get("benchmark_version") != "0.2.0":
        raise ValueError("pilot run benchmark_version must be 0.2.0")
    if run.get("study_config_version") != config.get("study_config_version"):
        raise ValueError("study_config_version does not match config")

    pack = find_pack(config, root, run.get("task_id", ""))
    if run.get("task_type") != pack["task_family"]:
        raise ValueError("task_type does not match canonical Task Pack")
    if run.get("task_pack_version") != pack["version"]:
        raise ValueError("task_pack_version does not match canonical Task Pack")

    provenance = run.get("provenance", {})
    if provenance.get("vad_core_ref") != config["upstreams"]["vad_core_ref"]:
        raise ValueError("vad_core_ref does not match study config")
    if provenance.get("promptless_ref") != config["upstreams"]["promptless_ref"]:
        raise ValueError("promptless_ref does not match study config")

    valid_conditions = set(config["vad_conditions"] + config["promptless_conditions"])
    if run.get("condition") not in valid_conditions:
        raise ValueError("condition is not part of the study config")

    expected_ids = [item["id"] for item in pack["acceptance_criteria"]]
    acceptance = run.get("acceptance", {})
    if acceptance.get("total") != len(expected_ids):
        raise ValueError("acceptance.total must equal Task Pack acceptance criteria count")

    if "acceptance_items" in run:
        actual_ids = [item["id"] for item in run["acceptance_items"]]
        if actual_ids != expected_ids:
            raise ValueError("acceptance_items must preserve canonical Task Pack criterion order")
        passed = sum(1 for item in run["acceptance_items"] if item["passed"])
        if passed != acceptance.get("passed"):
            raise ValueError("acceptance.passed does not match acceptance_items")

    required_inputs = [asset["name"] for asset in pack["inputs"] if asset["required"]]
    hashes = run.get("input_hashes", {})
    missing_hashes = [name for name in required_inputs if name not in hashes]
    if missing_hashes:
        raise ValueError(f"missing required input hashes: {missing_hashes}")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("run", type=Path)
    parser.add_argument("--config", type=Path, default=Path("configs/study-v0.2.0.json"))
    parser.add_argument("--root", type=Path, default=Path("."))
    args = parser.parse_args()

    run = load_json(args.run)
    config = load_json(args.config)
    validate_pilot_run(run, config, args.root)
    print("Pilot run cross-check: OK")


if __name__ == "__main__":
    main()
