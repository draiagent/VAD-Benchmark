#!/usr/bin/env python3
"""Validate study configuration and a run record."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

EXPECTED_VAD = ["A", "B", "C", "D", "E", "F"]
EXPECTED_PROMPTLESS = ["P0", "P1", "P2"]
EXPECTED_TASKS = ["video", "slides", "web", "data", "report"]


def validate_config(config: dict) -> None:
    if config.get("vad_conditions") != EXPECTED_VAD:
        raise ValueError("vad_conditions must preserve canonical A-F order")
    if config.get("promptless_conditions") != EXPECTED_PROMPTLESS:
        raise ValueError("promptless_conditions must preserve canonical P0-P2 order")
    if config.get("task_families") != EXPECTED_TASKS:
        raise ValueError("task_families must preserve the VAD Five-Pack")
    if not config.get("primary_metrics"):
        raise ValueError("primary_metrics must not be empty")
    upstreams = config.get("upstreams", {})
    for key in ("vad_core_ref", "promptless_ref"):
        ref = upstreams.get(key, "")
        if len(ref) != 40 or any(c not in "0123456789abcdef" for c in ref.lower()):
            raise ValueError(f"{key} must be a 40-character commit SHA")
    if config.get("raw_results_are_immutable") is not True:
        raise ValueError("raw_results_are_immutable must be true")


def validate_run(run: dict, schema_path: Path) -> None:
    try:
        import jsonschema
    except ImportError as exc:
        raise SystemExit("Install jsonschema: python -m pip install jsonschema") from exc
    schema = json.loads(schema_path.read_text(encoding="utf-8"))
    jsonschema.validate(run, schema)
    passed = run["acceptance"]["passed"]
    total = run["acceptance"]["total"]
    if passed > total:
        raise ValueError("acceptance.passed cannot exceed acceptance.total")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", type=Path, required=True)
    parser.add_argument("--run", type=Path)
    parser.add_argument("--schema", type=Path, default=Path("schemas/run-record.schema.json"))
    args = parser.parse_args()

    config = json.loads(args.config.read_text(encoding="utf-8"))
    validate_config(config)
    if args.run:
        run = json.loads(args.run.read_text(encoding="utf-8"))
        validate_run(run, args.schema)
    print("VAD-Benchmark validation: OK")


if __name__ == "__main__":
    main()
