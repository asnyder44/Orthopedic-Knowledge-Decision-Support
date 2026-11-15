"""Pipeline and Review pages (Flask versions of the okds repo's Streamlit pages), document upload, OrthoBot rule."""

from __future__ import annotations

import shutil

from conftest import ROOT
from test_pipeline import TOPIC, fake_web  # noqa: F401  (pytest fixture)

from okds import kindex
from okds.config import get_settings
from okds.ko import as_dict, parse_ko
from okds.pipeline import jobs
from okds.pipeline.store import PipelineStore
from okds.storage import LocalKOStore

LONG_TEXT = "Carpal tunnel syndrome squeezes the median nerve at the wrist. " * 20


def test_pages_render(client, data_dir):
    for path in ("/ko/pipeline", "/ko/review", "/ko/review?tab=library", "/ko/review?tab=data",
                 "/ko/pipeline/diagram", "/ko/pipeline/guide"):
        assert client.get(path).status_code == 200, path
    assert client.get("/ko/pipeline/diagram").headers["X-Frame-Options"] == "SAMEORIGIN"


def test_run_job1_from_the_page_for_chosen_topics(client, data_dir, fake_web):  # noqa: F811
    r = client.post("/ko/pipeline/run", data={"job": "fetch", "mode": "chosen", "topic": [TOPIC], "csrf_token": "test-token"})
    assert r.status_code == 302
    assert {a.topic_id for a in PipelineStore(get_settings()).articles()} == {TOPIC}
    html = client.get("/ko/pipeline").get_data(as_text=True)
    assert "Fetch: ok" in html


def test_template_draft_then_accept_from_the_review_page(client, data_dir, fake_web):  # noqa: F811
    s = get_settings()
    jobs.fetch_job(s, [TOPIC])
    client.post("/ko/pipeline/run", data={"job": "template", "csrf_token": "test-token"})
    store = PipelineStore(s)
    assert store.in_queue(TOPIC)
    html = client.get("/ko/review").get_data(as_text=True)
    assert "Your decision" in html and TOPIC in html
    # a template still has TODOs (problems), so accepting it unchanged is refused
    client.post(f"/ko/review/{TOPIC}/accept", data={"name": "Allen", "mode": "queue", "csrf_token": "test-token"})
    assert store.in_queue(TOPIC)
    client.post(f"/ko/review/{TOPIC}/reject", data={"name": "Allen", "reason": "Needs writing", "csrf_token": "test-token"})
    assert not store.in_queue(TOPIC) and store.decisions()[0]["decision"] == "rejected"


def test_accept_a_good_draft_from_the_queue(client, data_dir, example_text):
    store = PipelineStore(get_settings())
    store.add_to_queue(TOPIC, example_text, "# pack", {"created": "2026-11-14", "model": "m"})
    r = client.post(f"/ko/review/{TOPIC}/accept", data={"name": "Allen", "mode": "queue", "text": example_text,
                                                        "csrf_token": "test-token"})
    assert r.status_code == 302
    doc = next(e.doc for e in LocalKOStore(get_settings()).list_entries() if e.ko_id == TOPIC)
    assert as_dict(doc.front["review"])["status"] == "team_checked" and doc.front["review"]["team_checker"] == "Allen"


def test_library_drafts_can_be_accepted(client, data_dir):
    shutil.copy(next((ROOT / "data" / "kos" / "hand").glob("KO-HAND-COND-001_*.md")), _hand(data_dir))
    assert "Library drafts (1)" in client.get("/ko/review?tab=library").get_data(as_text=True)
    client.post("/ko/review/KO-HAND-COND-001/accept", data={"name": "Pat", "mode": "library", "csrf_token": "test-token"})
    doc = parse_ko(next((data_dir / "kos").rglob("KO-HAND-COND-001_*.md")).read_text(encoding="utf-8"))
    assert doc.front["review"]["status"] == "team_checked"


def test_upload_a_document_to_the_inbox(client, data_dir):
    r = client.post("/ko/pipeline/upload", data={"topic": TOPIC, "title": "Partner hand clinic handout", "text": LONG_TEXT,
                                                 "permitted_use": "link_and_paraphrase", "name": "Kim",
                                                 "csrf_token": "test-token"})
    assert r.status_code == 302
    (a,) = PipelineStore(get_settings()).articles(TOPIC, "new")
    assert a.pmcid.startswith("UP-") and a.meta["uploaded_by"] == "Kim" and a.meta["found_in"] == "upload"
    client.post("/ko/pipeline/upload", data={"topic": TOPIC, "title": "Again", "text": LONG_TEXT,
                                             "permitted_use": "link_and_paraphrase", "name": "Kim", "csrf_token": "test-token"})
    assert len(PipelineStore(get_settings()).articles(TOPIC)) == 1  # the same text is not added twice


def test_restricted_or_short_documents_are_refused(data_dir):
    import pytest

    s = get_settings()
    with pytest.raises(ValueError, match="restricted"):
        jobs.upload_document(s, topic_id=TOPIC, title="t", text=LONG_TEXT, permitted_use="restricted")
    with pytest.raises(ValueError, match="characters"):
        jobs.upload_document(s, topic_id=TOPIC, title="t", text="short", permitted_use="open_license")


def test_visitors_cannot_run_jobs(visitor, data_dir):
    assert visitor.post("/ko/pipeline/run", data={"job": "fetch", "csrf_token": "test-token"}).status_code == 302
    assert not PipelineStore(get_settings()).runs()


def test_orthobot_can_be_limited_to_checked_kos(data_dir, monkeypatch):
    shutil.copy(next((ROOT / "data" / "kos" / "hand").glob("KO-HAND-COND-001_*.md")), _hand(data_dir))
    assert len(kindex.orthobot_docs(get_settings())) == 1
    monkeypatch.setenv("OKDS_ORTHOBOT_MIN_STATUS", "team_checked")
    assert kindex.orthobot_docs(get_settings()) == []  # the draft is left out
    jobs.accept_library_ko(get_settings(), "KO-HAND-COND-001", "Pat")
    assert len(kindex.orthobot_docs(get_settings())) == 1


def _hand(data_dir):
    d = data_dir / "kos" / "hand"
    d.mkdir(parents=True, exist_ok=True)
    return d
