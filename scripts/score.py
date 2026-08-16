#!/usr/bin/env python3
"""Compute deterministic VAD-Benchmark metrics from one run record."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any, Dict


def completion_rate(passed: int, total: int) -> float:
    if total <= 0:
        raise ValueError("total acceptance items must be > 0")
    if passed < 0 or passed > total:
        raise ValueError("passed must be between 0 and total")
    return round((passed / total) * 100.0, 4)


def weighted_error(critical: int, major: int, minor: int) -> int:
    values = (critical, major, minor)
    if any(v < 0 for v in values):
        raise ValueError("error counts must be non-negative")
    return critical * 5 + major * 3 + minor


def prompt_reduction(baseline_chars: int, condition_chars: int) -> float:
    if baseline_chars <= 0:
        raise ValueError("baseline prompt chars must be > 0")
    if condition_chars < 0:
        raise ValueError("condition prompt chars must be >= 0")
    return round(1.0 - (condition_chars / baseline_chars), 6)


def compute_metrics(record: Dict[str, Any]) -> Dict[str, Any]:
    acceptance = record["acceptance"]
    errors = record["errors"]
    interaction = record["interaction"]
    timing = record["timing"]

    metrics: Dict[str, Any] = {
        "study_id": record["study_id"],
        "run_id": record["run_id"],
        "condition": record["condition"],
        "task_type": record["task_type"],
        "completion_rate": completion_rate(acceptance["passed"], acceptance["total"]),
        "first_pass_yield": 1 if acceptance["first_pass"] else 0,
        "revision_count": interaction["revision_count"],
        "weighted_error": weighted_error(errors["critical"], errors["major"], errors["minor"]),
        "human_active_seconds": timing["human_active_seconds"],
        "agent_wait_seconds": timing["agent_wait_seconds"],
        "wall_clock_seconds": timing["wall_clock_seconds"],
        "prompt_chars": interaction["prompt_chars"],
        "prompt_turns": interaction["prompt_turns"],
        "clarification_turns": interaction["clarification_turns"],
        "final_status": record["final_status"],
    }

    for key in ("tus_va_score", "hastu_score", "satisfaction_score", "routing_accuracy"):
        if key in record.get("ratings", {}):
            metrics[key] = record["ratings"][key]

    return metrics


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("run", type=Path)
    parser.add_argument("--out", type=Path)
    args = parser.parse_args()

    record = json.loads(args.run.read_text(encoding="utf-8"))
    metrics = compute_metrics(record)
    payload = json.dumps(metrics, ensure_ascii=False, indent=2) + "\n"

    if args.out:
        args.out.parent.mkdir(parents=True, exist_ok=True)
        args.out.write_text(payload, encoding="utf-8")
    else:
        print(payload, end="")


if __name__ == "__main__":
    main()
