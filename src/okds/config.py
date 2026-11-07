"""Settings and paths. Everything is relative to the repo, so the portal runs on any machine."""

from __future__ import annotations

import os
from dataclasses import dataclass
from pathlib import Path
from urllib.parse import urlsplit

from dotenv import load_dotenv

PACKAGE_DIR = Path(__file__).resolve().parent
SCHEMA_DIR = PACKAGE_DIR / "schema"
PROMPTS_DIR = PACKAGE_DIR / "prompts"


def find_repo_root() -> Path:
    """ORTHOINFO_ROOT if set (Docker), else the folder that holds pyproject.toml (works for
    `pip install -e .`), else the current folder."""
    if os.environ.get("ORTHOINFO_ROOT"):
        return Path(os.environ["ORTHOINFO_ROOT"])
    for parent in PACKAGE_DIR.parents:
        if (parent / "pyproject.toml").is_file():
            return parent
    return Path.cwd()


REPO_ROOT = find_repo_root()
load_dotenv(REPO_ROOT / ".env")

DEFAULT_MODEL = "claude-sonnet-5-5"
DEFAULT_OPENAI_MODEL = "gpt-6.1-sol"
DEFAULT_EMBEDDING_MODEL = "BAAI/bge-small-en-v1.5"
AI_PROVIDERS = ("claude", "openai")
SEARCH_METHODS = ("keyword", "semantic", "hybrid")
LOCAL_HOSTS = {"localhost", "127.0.0.1", "::1"}


@dataclass(frozen=True)
class Settings:
    data_dir: Path
    model: str  # Claude model
    generator_effort: str
    chat_effort: str
    storage_backend: str  # "local" now; "s3" / "mongodb" are planned
    s3_bucket: str
    s3_prefix: str
    ai_provider: str = "none"  # "claude", "openai" (OpenAI or a local OpenAI-compatible server), or "none"
    openai_model: str = DEFAULT_OPENAI_MODEL
    search_method: str = "hybrid"  # OrthoBot: keyword | semantic | hybrid (falls back to keyword)
    embedding_model: str = DEFAULT_EMBEDDING_MODEL
    semantic_enabled: bool = True  # needs the "semantic" extra; otherwise OrthoBot uses keyword search

    @property
    def ai_ready(self) -> bool:
        return self.ai_provider in AI_PROVIDERS

    @property
    def ai_model(self) -> str:
        """The model the chosen provider uses."""
        return self.openai_model if self.ai_provider == "openai" else self.model

    @property
    def ai_label(self) -> str:
        """Plain name of the AI for the UI: Claude, OpenAI, or Local model."""
        if self.ai_provider == "claude":
            return "Claude"
        if self.ai_provider == "openai":
            return "Local model" if openai_is_local() else "OpenAI"
        return "AI"

    @property
    def cache_dir(self) -> Path:
        """Embedding model + vectors for OrthoBot semantic search (git-ignored, rebuilt when KOs change)."""
        return self.data_dir / "build" / "cache"

    @property
    def kos_dir(self) -> Path:
        return self.data_dir / "kos"

    @property
    def packs_dir(self) -> Path:
        return self.data_dir / "sources" / "packs"

    @property
    def json_dir(self) -> Path:
        return self.data_dir / "build" / "json"

    @property
    def registry_path(self) -> Path:
        return self.data_dir / "registry.csv"

    @property
    def catalog_path(self) -> Path:
        return self.data_dir / "sources" / "source_catalog.csv"

    def ensure_dirs(self) -> None:
        for d in (self.kos_dir, self.packs_dir, self.json_dir):
            d.mkdir(parents=True, exist_ok=True)


def get_settings() -> Settings:
    """Read settings from environment variables (or `.env`). Read at call time so tests can override."""
    data_dir = Path(os.environ.get("OKDS_DATA_DIR") or (REPO_ROOT / "data")).expanduser().resolve()
    return Settings(
        data_dir=data_dir,
        model=os.environ.get("OKDS_MODEL", DEFAULT_MODEL),
        generator_effort=os.environ.get("OKDS_GENERATOR_EFFORT", "medium"),
        chat_effort=os.environ.get("OKDS_CHAT_EFFORT", "medium"),
        storage_backend=os.environ.get("OKDS_STORAGE", "local").lower(),
        s3_bucket=os.environ.get("OKDS_S3_BUCKET", ""),
        s3_prefix=os.environ.get("OKDS_S3_PREFIX", "okds/"),
        ai_provider=detect_provider(),
        openai_model=os.environ.get("OKDS_OPENAI_MODEL", DEFAULT_OPENAI_MODEL),
        search_method=os.environ.get("OKDS_SEARCH", "hybrid").lower(),
        embedding_model=os.environ.get("OKDS_EMBEDDING_MODEL", DEFAULT_EMBEDDING_MODEL),
        semantic_enabled=os.environ.get("OKDS_SEMANTIC", "true").strip().lower() not in {"0", "false", "no", "off"},
    )


def anthropic_key_configured() -> bool:
    """True if an API key or token is in the environment. (An `ant auth login` profile also works.)"""
    return bool(os.environ.get("ANTHROPIC_API_KEY") or os.environ.get("ANTHROPIC_AUTH_TOKEN"))


def openai_key_configured() -> bool:
    return bool(os.environ.get("OPENAI_API_KEY"))


def openai_is_local() -> bool:
    """True when OPENAI_BASE_URL points at this computer (for example Ollama). No API billing then."""
    return urlsplit(os.environ.get("OPENAI_BASE_URL", "")).hostname in LOCAL_HOSTS


def detect_provider() -> str:
    """OKDS_AI_PROVIDER = claude | openai | auto (default). Auto picks Claude if its key is set, then OpenAI.
    Returns "none" when the chosen provider has no key, so the UI can say "AI is off"."""
    choice = os.environ.get("OKDS_AI_PROVIDER", "auto").strip().lower()
    has = {"claude": anthropic_key_configured(), "openai": openai_key_configured()}
    if choice in has:
        return choice if has[choice] else "none"
    return next((p for p in AI_PROVIDERS if has[p]), "none")
