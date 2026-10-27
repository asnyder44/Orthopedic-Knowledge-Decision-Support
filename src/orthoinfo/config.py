"""Project paths and configuration loading."""

from __future__ import annotations

import os
import tomllib
from pathlib import Path

ROOT = Path(os.environ.get("ORTHOINFO_ROOT", Path(__file__).resolve().parents[2]))
CONFIG_DIR = ROOT / "config"
DATA_DIR = ROOT / "data"
RAW_DIR = DATA_DIR / "raw"
PROCESSED_DIR = DATA_DIR / "processed"
EVAL_DIR = DATA_DIR / "eval"
PILOT_DIR = DATA_DIR / "pilot"
LOG_DIR = DATA_DIR / "logs"
RESULTS_DIR = ROOT / "results"


def _load_toml(name: str) -> dict:
    return tomllib.loads((CONFIG_DIR / name).read_text(encoding="utf-8"))


def load_scope() -> dict:
    return _load_toml("scope.toml")


def load_sources_config() -> dict:
    return _load_toml("sources.toml")


def load_search_config() -> dict:
    return _load_toml("search.toml")


def load_appointment_questions() -> dict:
    return _load_toml("appointment_questions.toml")


def latest_version(base: Path) -> str:
    """Return the newest dataset version directory name under `base`."""
    versions = sorted(p.name for p in base.glob("*") if p.is_dir())
    if not versions:
        raise FileNotFoundError(
            f"No dataset versions in {base}. Run `orthoinfo collect` then `orthoinfo build`."
        )
    return versions[-1]
