import functools
import os
import shutil
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[2]
EXAMPLE = ROOT / "examples" / "KO-HAND-COND-001_carpal-tunnel-syndrome.md"
os.environ.setdefault("ORTHOINFO_RATE_LIMIT", "0")


@pytest.fixture
def data_dir(tmp_path, monkeypatch):
    """A fresh data folder with the seed registry and catalog; settings point to it."""
    d = tmp_path / "data"
    (d / "sources").mkdir(parents=True)
    shutil.copy(ROOT / "data" / "registry.csv", d / "registry.csv")
    catalog = ROOT / "data" / "sources" / "source_catalog.csv"
    if catalog.is_file():
        shutil.copy(catalog, d / "sources" / "source_catalog.csv")
    monkeypatch.setenv("OKDS_DATA_DIR", str(d))
    monkeypatch.delenv("ANTHROPIC_API_KEY", raising=False)
    monkeypatch.delenv("ANTHROPIC_AUTH_TOKEN", raising=False)
    monkeypatch.delenv("OPENAI_API_KEY", raising=False)
    monkeypatch.delenv("OKDS_AI_PROVIDER", raising=False)
    monkeypatch.delenv("OKDS_EDIT_PASSWORD", raising=False)
    monkeypatch.delenv("OKDS_EDIT_LOCAL", raising=False)
    monkeypatch.delenv("ORTHOBOT_AI", raising=False)
    monkeypatch.setenv("OKDS_SEMANTIC", "false")  # tests stay offline and fast
    return d


@pytest.fixture
def example_text():
    return EXAMPLE.read_text(encoding="utf-8")


@functools.lru_cache(maxsize=1)
def _app():
    """One app for all tests: the KO Portal reads OKDS_DATA_DIR on every request, so data_dir still applies."""
    from orthoinfo.app import create_app

    app = create_app()
    app.config["TESTING"] = True
    return app


@pytest.fixture
def client(data_dir):
    """A browser on this computer (127.0.0.1), so editing is allowed. Its form token is set."""
    c = _app().test_client()
    with c.session_transaction() as s:
        s["csrf"] = "test-token"
    c.environ_base["HTTP_X_CSRF_TOKEN"] = "test-token"
    return c


@pytest.fixture
def visitor(data_dir):
    """A visitor from another computer: read only."""
    c = _app().test_client()
    with c.session_transaction() as s:
        s["csrf"] = "test-token"
    c.environ_base.update(HTTP_X_CSRF_TOKEN="test-token", REMOTE_ADDR="203.0.113.9")
    return c
