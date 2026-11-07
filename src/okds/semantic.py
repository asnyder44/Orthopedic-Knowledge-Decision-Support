"""Semantic search with text embeddings (optional; install with `pip install -e ".[semantic]"`).

An embedding model turns each passage into a list of numbers that captures its meaning, so a
question can match a passage even when they use different words. This uses `fastembed`
(a small ONNX model, about 70 MB, CPU only). The model is downloaded once and the vectors are
cached on disk; any change to the KOs rebuilds them. Design taken from the PQC RAG portal.
"""

from __future__ import annotations

import hashlib
import logging
import threading
from pathlib import Path

log = logging.getLogger(__name__)


class SemanticIndex:
    def __init__(self, model_name: str, cache_dir: Path, enabled: bool = True) -> None:
        self.model_name = model_name
        self.cache_dir = Path(cache_dir)
        self.enabled = enabled
        self.status = "disabled" if not enabled else "not built"
        self.error: str | None = None
        self._model = None
        self._matrix = None
        self._lock = threading.Lock()

    @property
    def ready(self) -> bool:
        return self.status == "ready"

    def _load_model(self):
        from fastembed import TextEmbedding  # optional dependency

        return TextEmbedding(self.model_name, cache_dir=str(self.cache_dir / "models"))

    def build(self, texts: list[str]) -> None:
        if not self.enabled or not texts:
            return
        with self._lock:
            self.status = "building"
            try:
                import numpy as np

                digest = hashlib.sha256(
                    (self.model_name + "\x00" + "\x00".join(texts)).encode("utf-8")
                ).hexdigest()[:16]
                cache_file = self.cache_dir / f"embeddings-{digest}.npy"
                self._model = self._load_model()
                if cache_file.is_file():
                    matrix = np.load(cache_file)
                else:
                    embed = getattr(self._model, "passage_embed", self._model.embed)
                    matrix = np.array(list(embed(texts)), dtype="float32")
                    self.cache_dir.mkdir(parents=True, exist_ok=True)
                    np.save(cache_file, matrix)
                    for old in self.cache_dir.glob("embeddings-*.npy"):  # vectors for older KO versions
                        if old != cache_file:
                            old.unlink(missing_ok=True)
                norms = np.linalg.norm(matrix, axis=1, keepdims=True)
                self._matrix = matrix / np.maximum(norms, 1e-12)
                self.status = "ready"
                self.error = None
            except ImportError:
                self.status = "unavailable"
                self.error = 'Install the semantic extra: pip install -e ".[semantic]"'
            except Exception as exc:  # model download or runtime errors
                log.exception("Semantic index build failed")
                self.status = "error"
                self.error = f"{type(exc).__name__}: {exc}"

    def search(self, query: str, k: int = 10) -> list[tuple[int, float]]:
        if not self.ready:
            return []
        import numpy as np

        embed = getattr(self._model, "query_embed", self._model.embed)
        q = np.array(list(embed([query])), dtype="float32")[0]
        q = q / max(float(np.linalg.norm(q)), 1e-12)
        sims = self._matrix @ q
        top = np.argsort(-sims)[:k]
        return [(int(i), float(sims[i])) for i in top]
