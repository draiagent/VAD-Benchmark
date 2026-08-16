#!/usr/bin/env python3
"""Aggregate VAD-Benchmark raw run records into transparent group summaries."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from statistics import mean, median
from typing import Any, Dict, Iterable, List, Tuple

try:
    from scripts.score import compute_metrics
except ModuleNotFoundError:  # direct execution: python scripts/aggregate.py
    from score import compute_metrics

NUMERIC_KEYS = [
    "completion_rate",
    "first_pass_yield",
    "revision_count",
    "weighted_error",
    "human_active_seconds",
    "agent_wait_seconds",
    "wall_clock_seconds",
    "prompt_chars",
    "prompt_turns",
    "clarification_turns",
    "tus_va_score",
    "hastu_score",
    "satisfaction_score",
    "routing_accuracy",
]


def load_records(folder: Path) -> Iterable[Dict[str, Any]]:
    for path in sorted(folder.glob("*.json")):
        yield json.loads(path.read_text(encoding="utf-8"))


def group_key(metrics: Dict[str, Any]) -> Tuple[str, str, str, str]:
    return (
        metrics["condition"],
        metrics["task_type"],
        metrics.get("provider", ""),
        metrics.get("model_fingerprint", ""),
    )


def aggregate(records: Iterable[Dict[str, Any]]) -> List[Dict[str, Any]]:
    buckets: Dict[Tuple[str, str, str, str], List[Dict[str, Any]]] = {}
    for record in records:
        metrics = compute_metrics(record)
        model = record.get("model", {})
        metrics["provider"] = model.get("provider", "")
        metrics["model_fingerprint"] = f"{model.get('name','')}@{model.get('version','')}"
        buckets.setdefault(group_key(metrics), []).append(metrics)

    output: List[Dict[str, Any]] = []
    for key, rows in sorted(buckets.items()):
        condition, task_type, provider, model_fingerprint = key
        summary: Dict[str, Any] = {
            "condition": condition,
            "task_type": task_type,
            "provider": provider,
            "model_fingerprint": model_fingerprint,
            "n": len(rows),
            "metrics": {},
        }
        for metric in NUMERIC_KEYS:
            values = [row[metric] for row in rows if isinstance(row.get(metric), (int, float))]
            if values:
                summary["metrics"][metric] = {
                    "mean": round(mean(values), 6),
                    "median": round(median(values), 6),
                }
        output.append(summary)
    return output


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("folder", type=Path)
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()

    summaries = aggregate(load_records(args.folder))
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(summaries, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote {len(summaries)} group summaries to {args.out}")


if __name__ == "__main__":
    main()
