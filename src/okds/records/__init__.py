"""Data skeleton: data models, upload checks (incl. a privacy screen), record batches, summaries, sample data."""

from __future__ import annotations

from ..config import Settings
from .model import DataModel, ModelError, get_model, model_errors, models
from .store import RecordStore, UploadError, read_upload

__all__ = ["DataModel", "ModelError", "RecordStore", "UploadError", "get_model", "ko_types", "ko_usage", "model_errors",
           "models", "read_upload"]


def ko_types(settings: Settings) -> dict[str, str]:
    """KO ID -> ko_type for every topic (ko fields in records must point to a real topic)."""
    from ..registry import load_registry

    return {c.ko_id: c.ko_type for c in load_registry(settings.registry_path).values()}


def ko_usage(settings: Settings) -> dict[str, dict[str, int]]:
    """KO ID -> {"model:Entity.field": rows} across every model's accepted batches."""
    out: dict[str, dict[str, int]] = {}
    for m in models().values():
        for ko, fields in RecordStore(settings, m).ko_usage().items():
            for k, n in fields.items():
                out.setdefault(ko, {})[f"{m.name}:{k}"] = n
    return out
