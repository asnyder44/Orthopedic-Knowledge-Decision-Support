"""Step 4a: collect raw source material into data/raw/<version>/<source>/.

Raw downloads are kept unmodified so cleaning (`orthoinfo build`) can be re-run
and audited without the network. Collection resumes: files already present are
not downloaded again, so `orthoinfo collect --version <same>` continues a run.
"""

from __future__ import annotations

import datetime as dt
from pathlib import Path

from .config import RAW_DIR, load_sources_config
from .http import BlockedError, Http
from .sources import SOURCES


def collect(version: str | None = None, only: list[str] | None = None) -> Path:
    cfg = load_sources_config()
    version = version or "v" + dt.date.today().isoformat()
    names = only or [n for n in SOURCES if cfg.get(n, {}).get("enabled")]
    unknown = set(names) - set(SOURCES)
    if unknown:
        raise SystemExit(f"Unknown source(s) {sorted(unknown)}; choose from {list(SOURCES)}")

    http = Http()
    for name in SOURCES:  # keep dependency order
        if name not in names:
            continue
        out = RAW_DIR / version / name
        out.mkdir(parents=True, exist_ok=True)
        print(f"[{name}]")
        try:
            SOURCES[name].collect(out, cfg[name], http)
        except (BlockedError, PermissionError) as exc:
            print(f"  stopped: {exc}")
    return RAW_DIR / version
