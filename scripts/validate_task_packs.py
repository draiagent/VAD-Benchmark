#!/usr/bin/env python3
"""Validate Five-Pack pilot task definitions and repository fixture references."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

EXPECTED_FAMILIES = ["video", "slides", "web", "data", "report"]


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def validate_task_packs(config_path: Path, schema_path: Path, root: Path) -> list[dict[str, Any]]:
    try:
        import jsonschema
    except ImportError as exc:
        raise SystemExit("Install jsonschema: python -m pip install jsonschema") from exc

    config = load_json(config_path)
    schema = load_json(schema_path)
    task_paths = config.get("task_packs", [])
    if len(task_paths) != 5:
        raise ValueError("v0.2.0 Pilot Lab requires exactly five task packs")

    packs: list[dict[str, Any]] = []
    seen_ids: set[str] = set()
    families: list[str] = []
    upstream_ref = config["upstreams"]["vad_core_ref"]

    for relative in task_paths:
        path = root / relative
        if not path.exists():
            raise ValueError(f"missing task pack: {relative}")
        pack = load_json(path)
        jsonschema.validate(pack, schema)

        task_id = pack["task_id"]
        if task_id in seen_ids:
            raise ValueError(f"duplicate task_id: {task_id}")
        seen_ids.add(task_id)
        families.append(pack["task_family"])

        if pack["upstream_card"]["ref"] != upstream_ref:
            raise ValueError(f"{task_id}: upstream ref differs from study config")

        acceptance_ids = [item["id"] for item in pack["acceptance_criteria"]]
        if len(acceptance_ids) != len(set(acceptance_ids)):
            raise ValueError(f"{task_id}: duplicate acceptance criterion id")

        required_critical = [
            item for item in pack["acceptance_criteria"]
            if item["required"] and item["severity"] == "critical"
        ]
        if not required_critical:
            raise ValueError(f"{task_id}: must define at least one required critical criterion")

        for asset in pack["inputs"]:
            if asset["source"] == "repo_fixture":
                fixture_path = asset.get("path")
                if not fixture_path or not (root / fixture_path).exists():
                    raise ValueError(f"{task_id}: missing repo fixture {fixture_path!r}")

        packs.append(pack)

    if families != EXPECTED_FAMILIES:
        raise ValueError(f"task pack order must be {EXPECTED_FAMILIES}, got {families}")

    return packs


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", type=Path, default=Path("configs/study-v0.2.0.json"))
    parser.add_argument("--schema", type=Path, default=Path("schemas/task-pack.schema.json"))
    parser.add_argument("--root", type=Path, default=Path("."))
    args = parser.parse_args()

    packs = validate_task_packs(args.config, args.schema, args.root)
    print(f"Five-Pack task validation: OK ({len(packs)} packs)")


if __name__ == "__main__":
    main()
