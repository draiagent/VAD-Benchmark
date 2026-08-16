#!/usr/bin/env python3
"""Build a deterministic Five-Pack pilot run matrix without executing models."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def build_matrix(config: dict[str, Any], root: Path, track: str, models: list[str], replicates: int) -> list[dict[str, Any]]:
    if track not in config["tracks"]:
        raise ValueError(f"unknown track: {track}")
    if replicates < 1:
        raise ValueError("replicates must be >= 1")
    if not models:
        raise ValueError("at least one --model is required")

    conditions = config["tracks"][track]["conditions"]
    upstreams = config["upstreams"]
    rows: list[dict[str, Any]] = []

    for task_path in config["task_packs"]:
        pack = load_json(root / task_path)
        for condition in conditions:
            for model in models:
                for replicate in range(1, replicates + 1):
                    run_plan_id = f"{track}-{pack['task_id']}-{condition}-{model}-{replicate:02d}"
                    rows.append({
                        "run_plan_id": run_plan_id,
                        "track": track,
                        "task_id": pack["task_id"],
                        "task_pack": task_path,
                        "condition": condition,
                        "model_slot": model,
                        "replicate": replicate,
                        "vad_core_ref": upstreams["vad_core_ref"],
                        "promptless_ref": upstreams["promptless_ref"]
                    })
    return rows


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", type=Path, default=Path("configs/study-v0.2.0.json"))
    parser.add_argument("--root", type=Path, default=Path("."))
    parser.add_argument("--track", choices=["vad", "promptless"], required=True)
    parser.add_argument("--model", action="append", default=[], help="Stable operator label, e.g. provider:model:version:platform")
    parser.add_argument("--replicates", type=int)
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()

    config = load_json(args.config)
    replicates = args.replicates or config["tracks"][args.track]["default_replicates"]
    matrix = build_matrix(config, args.root, args.track, args.model, replicates)
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(matrix, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote {len(matrix)} planned runs to {args.out}")


if __name__ == "__main__":
    main()
