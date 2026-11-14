"""The KO Portal pages (Flask, /ko) and the Hub OrthoBot's KO + AI additions."""

from __future__ import annotations

import json
import shutil

import pytest
from conftest import EXAMPLE, ROOT

from okds import chatbot, llm

PAGES = ["/ko/", "/ko/generator", "/ko/library", "/ko/manage", "/ko/topics", "/ko/sources", "/ko/orthobot", "/ko/login"]


def _seed(data_dir) -> None:
    shutil.copytree(ROOT / "data" / "kos", data_dir / "kos", dirs_exist_ok=True)


def _lines(resp) -> list[dict]:
    return [json.loads(line) for line in resp.get_data(as_text=True).splitlines() if line.strip()]


SOURCES = [
    {"url": "https://medlineplus.gov/carpaltunnelsyndrome.html", "title": "Carpal Tunnel Syndrome",
     "publisher": "MedlinePlus", "text": "The median nerve is squeezed at the wrist."},
    {"url": "https://www.ninds.nih.gov/cts", "title": "CTS", "publisher": "NINDS", "text": "Numbness and tingling."},
]


# ---------------------------------------------------------------- pages render

@pytest.mark.parametrize("path", PAGES)
def test_pages_render_with_empty_library(client, path):
    r = client.get(path)
    html = r.get_data(as_text=True)
    assert r.status_code == 200, path
    assert 'class="disclaimer"' in html and "KO Portal" in html


@pytest.mark.parametrize("path", PAGES)
def test_pages_render_with_the_starter_kos(client, data_dir, path):
    _seed(data_dir)
    assert client.get(path).status_code == 200, path


def test_hub_links_to_the_portal(client):
    assert 'href="/ko/"' in client.get("/").get_data(as_text=True)
    assert "/ko/" in client.get("/library").get_data(as_text=True)


def test_home_has_both_tabs_and_the_article(client):
    html = client.get("/ko/").get_data(as_text=True)
    assert "At a glance" in html and "Full article" in html and "Words to know" in html
    assert client.get("/ko/article.md").status_code == 200


def test_library_browse_open_search_and_filter(client, data_dir):
    _seed(data_dir)
    html = client.get("/ko/library").get_data(as_text=True)
    n = len(list((data_dir / "kos").rglob("*.md")))
    assert f"{n} Knowledge Objects about orthopedics" in html
    html = client.get("/ko/library?ko=KO-HAND-COND-001").get_data(as_text=True)
    assert "Carpal Tunnel Syndrome" in html and "Ask about this" in html and "Practice questions" in html
    html = client.get("/ko/library?q=nerve+conduction").get_data(as_text=True)
    assert f" of {n} Knowledge Objects" in html and f"0 of {n}" not in html and f"{n} of {n}" not in html
    assert "Nerve Conduction Study" in html
    assert client.get("/ko/library/KO-HAND-COND-001.md").status_code == 200
    assert client.get("/ko/library/KO-NOPE-COND-001.md").status_code == 404


def test_markdown_in_a_ko_cannot_inject_html(client, data_dir, example_text):
    evil = example_text.replace("## Summary", "## Summary\n\n<script>alert(1)</script> [x](javascript:alert(1))", 1)
    (data_dir / "kos" / "hand").mkdir(parents=True)
    (data_dir / "kos" / "hand" / "evil.md").write_text(evil, encoding="utf-8")
    html = client.get("/ko/library?ko=KO-HAND-COND-001").get_data(as_text=True)
    assert "<script>alert(1)</script>" not in html and 'href="javascript:' not in html


# ---------------------------------------------------------------- generator flow (template, no AI)

def test_generator_template_check_and_save(client, data_dir):
    body = {"ko_id": "KO-HAND-COND-001", "audience": ["patient"], "sources": SOURCES, "mode": "template"}
    j = client.post("/ko/api/draft", json=body).get_json()
    assert "TODO" in j["markdown"] and j["pack"].startswith("# Source pack SP-KO-HAND-COND-001")
    check = client.post("/ko/api/check", json={"text": j["markdown"]}).get_json()
    assert check["ko_id"] == "KO-HAND-COND-001" and check["preview"] and check["warnings"]
    r = client.post("/ko/api/save", json={"text": j["markdown"], "pack": j["pack"]})
    if not check["ok"]:  # a template still has problems: it needs "save anyway"
        assert r.status_code == 400
        r = client.post("/ko/api/save", json={"text": j["markdown"], "pack": j["pack"], "force": True})
    assert r.status_code == 200, r.get_json()
    assert list((data_dir / "kos").rglob("KO-HAND-COND-001_*.md"))
    assert (data_dir / "sources" / "packs" / "SP-KO-HAND-COND-001.md").is_file()


def test_generator_needs_two_sources_and_a_topic(client):
    r = client.post("/ko/api/draft", json={"ko_id": "KO-HAND-COND-001", "audience": ["patient"], "sources": SOURCES[:1]})
    assert r.status_code == 400 and "2 sources" in r.get_json()["error"]
    r = client.post("/ko/api/draft", json={"ko_id": "nope", "audience": ["patient"], "sources": SOURCES})
    assert r.status_code == 400 and "topic" in r.get_json()["error"]


def test_ai_draft_streams_and_is_finalized(client, monkeypatch):
    monkeypatch.setenv("ANTHROPIC_API_KEY", "test")

    def fake_stream(**kw):
        kw["result"].chunks.append("---\nko_id: KO-WRONG\n---\n## Summary\nHi")
        kw["result"].finish = "end_turn"
        yield "---\n"
    monkeypatch.setattr(llm, "stream_text", fake_stream)
    body = {"ko_id": "KO-HAND-COND-001", "audience": ["patient"], "sources": SOURCES, "mode": "ai"}
    items = _lines(client.post("/ko/api/draft", json=body))
    assert items[0] == {"t": "---\n"}
    done = items[-1]
    assert done["done"] and "ko_id: KO-HAND-COND-001" in done["markdown"]
    assert any("reset" in n for n in done["notes"])


def test_add_topic_from_the_wizard_and_the_topics_page(client, data_dir):
    topic = {"term": "Trigger Finger Test X", "ko_type": "Condition", "specialty": "HAND"}
    j = client.post("/ko/api/topic", json=topic).get_json()
    assert j["topic"]["ko_id"].startswith("KO-HAND-COND-")
    r = client.post("/ko/topics", data={"term": "Mallet Finger X", "ko_type": "Condition", "specialty": "HAND",
                                        "csrf_token": "test-token"})
    assert r.status_code == 302
    assert "Mallet Finger X" in (data_dir / "registry.csv").read_text(encoding="utf-8")


# ---------------------------------------------------------------- manage: import, delete, export

def test_import_delete_and_export(client, data_dir, example_text):
    up = {"file": (EXAMPLE.open("rb"), EXAMPLE.name), "csrf_token": "test-token"}
    assert client.post("/ko/manage/import", data=up, content_type="multipart/form-data").status_code == 302
    assert list((data_dir / "kos").rglob("*.md"))
    assert client.get("/ko/export.zip").headers["Content-Type"] == "application/zip"
    r = client.post("/ko/manage/KO-HAND-COND-001/delete", data={"confirm": "KO-HAND-COND-001", "csrf_token": "test-token"})
    assert r.status_code == 302 and not list((data_dir / "kos").rglob("*.md"))


# ---------------------------------------------------------------- who may edit

def test_visitors_from_other_computers_are_read_only(visitor, data_dir):
    _seed(data_dir)
    assert visitor.get("/ko/library").status_code == 200
    body = {"ko_id": "KO-HAND-COND-001", "audience": ["patient"], "sources": SOURCES}
    assert visitor.post("/ko/api/draft", json=body).status_code == 403
    assert visitor.post("/ko/api/save", json={"text": "x", "force": True}).status_code == 403
    assert visitor.post("/ko/api/fetch", json={"url": "https://example.org"}).status_code == 403
    assert visitor.get("/ko/export.zip").status_code == 302  # to the sign-in page
    delete = {"confirm": "KO-HAND-COND-001", "csrf_token": "test-token"}
    assert visitor.post("/ko/manage/KO-HAND-COND-001/delete", data=delete).status_code == 302
    assert list((data_dir / "kos").rglob("KO-HAND-COND-001_*.md"))  # not deleted


def test_proxied_requests_are_not_local(client):
    r = client.post("/ko/api/save", json={"text": "x"}, headers={"X-Forwarded-For": "203.0.113.9"})
    assert r.status_code == 403


def test_editor_password_sign_in(visitor, monkeypatch):
    monkeypatch.setenv("OKDS_EDIT_PASSWORD", "s3cret-pass")
    assert visitor.post("/ko/login", data={"password": "wrong", "csrf_token": "test-token"}).status_code == 200
    r = visitor.post("/ko/login", data={"password": "s3cret-pass", "csrf_token": "test-token"})
    assert r.status_code == 302
    j = visitor.post("/ko/api/topic", json={"term": "Signed In Topic", "ko_type": "Condition", "specialty": "HAND"})
    assert j.status_code == 200
    monkeypatch.setenv("OKDS_EDIT_PASSWORD", "changed")  # a changed password ends old sign-ins
    assert visitor.post("/ko/api/topic", json={"term": "Another", "ko_type": "Condition", "specialty": "HAND"}).status_code == 403


def test_posts_need_the_form_token(client):
    r = client.post("/ko/api/check", json={"text": ""}, headers={"X-CSRF-Token": "wrong"})
    assert r.status_code == 400 and "out of date" in r.get_json()["error"]


# ---------------------------------------------------------------- KO OrthoBot

def test_ko_orthobot_quick_answer(client, data_dir):
    _seed(data_dir)
    items = _lines(client.post("/ko/api/ask", json={"question": "Which nerve is affected in carpal tunnel syndrome?",
                                                   "mode": "quick", "method": "keyword"}))
    ans = items[-1]["answer"]
    assert ans["citations"] and "median" in ans["html"].lower() and 'class="cite"' in ans["html"]


def test_ko_orthobot_ai_is_for_editors_only(visitor, data_dir, monkeypatch):
    _seed(data_dir)
    monkeypatch.setenv("ANTHROPIC_API_KEY", "test")
    r = visitor.post("/ko/api/ask", json={"question": "What is carpal tunnel syndrome?", "mode": "ai"})
    assert r.status_code == 403


# ---------------------------------------------------------------- Hub OrthoBot (/api/ask)

def test_hub_orthobot_also_quotes_knowledge_objects(client, data_dir):
    _seed(data_dir)
    j = client.post("/api/ask", json={"question": "Which nerve is squeezed in carpal tunnel syndrome?"}).get_json()
    assert j["knowledge_objects"] and j["found_any"]
    k = j["knowledge_objects"][0]
    assert k["path"].startswith("/ko/library?ko=") and k["review_status"] and k["lines"]
    assert "ai" not in j
    info = client.get("/api/info").get_json()
    assert info["knowledge_objects"] == len(list((data_dir / "kos").rglob("*.md"))) and info["ai_answers"] is False


def test_hub_ai_answer_is_off_unless_enabled(client, data_dir, monkeypatch):
    monkeypatch.setenv("ANTHROPIC_API_KEY", "test")
    j = client.post("/api/ask", json={"question": "What is carpal tunnel syndrome?", "mode": "ai"}).get_json()
    assert "not turned on" in j["ai"]["error"]


def test_hub_ai_answer_cites_passages(client, data_dir, monkeypatch):
    _seed(data_dir)
    monkeypatch.setenv("ANTHROPIC_API_KEY", "test")
    from orthoinfo import app as app_module
    seen = {}

    def fake_stream(**kw):
        seen["user"] = kw["user"]
        kw["result"].chunks.append("The median nerve is squeezed at the wrist [1]. See also [99]. ![x](https://e.x/i.png)")
        kw["result"].finish = "end_turn"
        yield ""
    monkeypatch.setattr(llm, "stream_text", fake_stream)
    # the app is shared between tests: turn its public AI answers on for this test only
    monkeypatch.setattr(client.application.extensions["orthobot_assistant"], "public_ai", True)
    j = client.post("/api/ask", json={"question": "Which nerve is affected in carpal tunnel syndrome?", "mode": "ai"}).get_json()
    ai = j["ai"]
    assert ai["found"] and "[99]" not in ai["text"] and "![" not in ai["text"]
    assert ai["citations"][0]["n"] == 1 and any("removed" in w for w in ai["warnings"])
    assert '<passage n="1">' in seen["user"]
    assert app_module.MAX_API_BODY == 16 * 1024


def test_hub_api_still_limits_request_size(client):
    r = client.post("/api/ask", data="x" * (17 * 1024), content_type="application/json")
    assert r.status_code == 413


def test_no_answer_text_is_shared():
    assert chatbot.NO_ANSWER.startswith("I couldn't find")
