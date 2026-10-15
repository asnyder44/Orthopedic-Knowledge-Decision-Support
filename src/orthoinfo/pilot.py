"""Steps 6 and 9: summarise usability sessions (baseline prototype vs new tool).

Session logs are CSV files in data/pilot/ with the columns in
data/pilot/sessions_template.csv — one row per participant x scenario.
"""

from __future__ import annotations

import csv
import statistics
from collections import defaultdict
from pathlib import Path

from .config import PILOT_DIR

COLUMNS = [
    "participant_id", "version", "order", "scenario_id", "completed", "seconds",
    "comprehension_0to3", "checked_source", "unsupported_statements", "notes",
]


def load_sessions(paths: list[Path] | None = None) -> list[dict]:
    paths = paths or sorted(p for p in PILOT_DIR.glob("*.csv") if "template" not in p.name)
    rows = []
    for path in paths:
        with path.open(newline="", encoding="utf-8") as fh:
            rows += list(csv.DictReader(fh))
    return rows


def _stats(rows: list[dict]) -> dict:
    def nums(col):
        return [float(r[col]) for r in rows if r.get(col, "").strip()]

    seconds = [float(r["seconds"]) for r in rows if r.get("seconds") and r.get("completed") == "1"]
    return {
        "sessions": len(rows),
        "participants": len({r["participant_id"] for r in rows}),
        "completion_rate": round(statistics.fmean(nums("completed")), 2) if rows else None,
        "median_seconds_completed": statistics.median(seconds) if seconds else None,
        "mean_comprehension_0to3": round(statistics.fmean(nums("comprehension_0to3")), 2) if nums("comprehension_0to3") else None,
        "checked_source_rate": round(statistics.fmean(nums("checked_source")), 2) if nums("checked_source") else None,
        "unsupported_statements": int(sum(nums("unsupported_statements"))),
    }


def summarise(rows: list[dict]) -> str:
    by_version, by_order = defaultdict(list), defaultdict(list)
    for r in rows:
        by_version[r["version"]].append(r)
        by_order[(r["version"], r["order"])].append(r)

    keys = list(_stats([]).keys())
    lines = ["| version | " + " | ".join(keys) + " |", "|---" * (len(keys) + 1) + "|"]
    for version, rs in sorted(by_version.items()):
        s = _stats(rs)
        lines.append(f"| {version} | " + " | ".join(str(s[k]) for k in keys) + " |")
    lines += ["", "Order effects (was this version tried first or second?):", "",
              "| version | order | sessions | completion_rate | median_seconds_completed |",
              "|---|---|---|---|---|"]
    for (version, order), rs in sorted(by_order.items()):
        s = _stats(rs)
        lines.append(f"| {version} | {order} | {s['sessions']} | {s['completion_rate']} | {s['median_seconds_completed']} |")
    lines += ["", "With 6-10 participants these are descriptive results, not statistical proof."]
    return "\n".join(lines)
