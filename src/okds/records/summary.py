"""Summaries of accepted records that work for any data model: counts, category breakdowns, averages.
Small counts are suppressed ("<5") and averages need at least 5 values, so no person stands out."""

from __future__ import annotations

from collections import Counter
from statistics import mean
from typing import Any

from .model import DataModel
from .store import MIN_CELL, small


def summarize(model: DataModel, tables: dict[str, list[dict[str, str]]]) -> dict[str, Any]:
    entities = []
    for name, ent in model.entities.items():
        rows = tables.get(name, [])
        cats, nums = [], []
        for f in ent.fields.values():
            values = [r.get(f.name, "") for r in rows if r.get(f.name, "")]
            if f.type in ("category", "boolean", "ko") and values:
                counts = Counter(values).most_common()
                cats.append({"field": f.name, "type": f.type,
                             "values": [{"value": v, "count": small(n), "n": n} for v, n in counts]})
            elif f.type in ("integer", "number", "day") and values:
                nums_v = [float(v) for v in values]
                if len(nums_v) >= MIN_CELL:
                    nums.append({"field": f.name, "unit": f.unit, "n": len(nums_v), "mean": round(mean(nums_v), 1),
                                 "min": round(min(nums_v), 1), "max": round(max(nums_v), 1)})
                else:
                    nums.append({"field": f.name, "unit": f.unit, "n": len(nums_v), "mean": None})
        entities.append({"name": name, "rows": len(rows), "rows_shown": small(len(rows)), "categories": cats,
                         "numbers": nums})
    return {"entities": entities, "people": len(tables.get(model.root, []))}
