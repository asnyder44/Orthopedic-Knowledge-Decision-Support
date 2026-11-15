"""One shared OrthoBot index over the saved Knowledge Objects, rebuilt only when a KO file changes.

Used by the KO portal pages and by the hub's OrthoBot API, so both always search the same KOs.
"""

from __future__ import annotations

import hashlib
import threading

from .chatbot import KOIndex
from .config import Settings
from .ko import KODocument, as_dict
from .semantic import SemanticIndex
from .storage import LocalKOStore

_lock = threading.Lock()
_cache: dict[str, tuple[str, KOIndex]] = {}


def load_docs(settings: Settings) -> list[KODocument]:
    return [e.doc for e in LocalKOStore(settings).list_entries() if e.doc is not None]


STATUS_RANK = ["draft", "ai_checked", "team_checked", "clinician_reviewed", "published"]  # "retired" is never used


def status_ok(doc: KODocument, min_status: str) -> bool:
    status = str(as_dict(doc.front.get("review")).get("status", "draft"))
    if status not in STATUS_RANK:
        return False
    floor = STATUS_RANK.index(min_status) if min_status in STATUS_RANK else 0
    return STATUS_RANK.index(status) >= floor


def orthobot_docs(settings: Settings) -> list[KODocument]:
    """The KOs OrthoBot may answer from (OKDS_ORTHOBOT_MIN_STATUS; default: every draft or better)."""
    return [d for d in load_docs(settings) if status_ok(d, settings.orthobot_min_status)]


def _fingerprint(settings: Settings) -> str:
    """Changes whenever a KO file is added, removed or edited (path, size, modification time)."""
    h = hashlib.sha256(f"{settings.embedding_model}\x00{settings.orthobot_min_status}".encode())
    h.update(b"semantic" if settings.semantic_enabled else b"keyword")
    for path in sorted(settings.kos_dir.rglob("*.md")):
        st = path.stat()
        h.update(f"{path}\x00{st.st_size}\x00{st.st_mtime_ns}\x00".encode())
    return h.hexdigest()


def get_index(settings: Settings) -> KOIndex:
    """The current index (built on first use and after any KO change)."""
    key = str(settings.data_dir)
    fp = _fingerprint(settings)
    cached = _cache.get(key)
    if cached and cached[0] == fp:
        return cached[1]
    with _lock:
        cached = _cache.get(key)
        if cached and cached[0] == fp:
            return cached[1]
        semantic = SemanticIndex(settings.embedding_model, settings.cache_dir, enabled=settings.semantic_enabled)
        index = KOIndex(orthobot_docs(settings), semantic=semantic)
        _cache[key] = (fp, index)
        return index


def clear() -> None:
    with _lock:
        _cache.clear()
