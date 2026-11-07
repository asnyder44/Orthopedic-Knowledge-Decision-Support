"""One shared OrthoBot index over the saved Knowledge Objects, rebuilt only when a KO file changes.

Used by the KO portal pages and by the hub's OrthoBot API, so both always search the same KOs.
"""

from __future__ import annotations

import hashlib
import threading

from .chatbot import KOIndex
from .config import Settings
from .ko import KODocument
from .semantic import SemanticIndex
from .storage import LocalKOStore

_lock = threading.Lock()
_cache: dict[str, tuple[str, KOIndex]] = {}


def load_docs(settings: Settings) -> list[KODocument]:
    return [e.doc for e in LocalKOStore(settings).list_entries() if e.doc is not None]


def _fingerprint(settings: Settings) -> str:
    """Changes whenever a KO file is added, removed or edited (path, size, modification time)."""
    h = hashlib.sha256(settings.embedding_model.encode())
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
        index = KOIndex(load_docs(settings), semantic=semantic)
        _cache[key] = (fp, index)
        return index


def clear() -> None:
    with _lock:
        _cache.clear()
