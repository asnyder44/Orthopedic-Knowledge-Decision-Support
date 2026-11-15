"""KO pipeline tests. Fake Europe PMC / NCBI responses and a fake AI, so no network or key is needed."""

from __future__ import annotations

import json

import pytest
from test_ai import FakeClaude

from okds import generator, llm
from okds import registry as reg
from okds.config import get_settings
from okds.ko import parse_ko
from okds.pipeline import jobs, sources
from okds.pipeline.store import PipelineBusy, PipelineStore
from okds.storage import LocalKOStore

TOPIC = "KO-HAND-COND-001"


def _result(pmcid, license_, types, title="A review about carpal tunnel syndrome"):
    return {"pmcid": pmcid, "title": title, "doi": f"10.1/{pmcid}", "firstPublicationDate": "2025-01-02",
            "license": license_, "pubTypeList": {"pubType": types}, "journalInfo": {"journal": {"title": "Test Journal"}}}


SEARCH = {"resultList": {"result": [
    _result("PMC111", "cc by", ["review-article", "Review"]),
    _result("PMC222", "cc by-nc-nd", ["review-article"]),
    _result("PMC333", "cc by", ["case-report", "Case Reports"]),
    _result("PMC444", "cc0", ["Systematic Review", "systematic-review"]),
]}}

JATS = b"""<?xml version="1.0"?><pmc-articleset><article><front><article-meta><abstract><p>Carpal tunnel syndrome
is common. It squeezes the median nerve.</p></abstract></article-meta></front><body>
<sec><title>Introduction</title><p>""" + b"The median nerve passes through the carpal tunnel. " * 20 + b"""</p>
<table-wrap><table><tr><td><p>TABLE TEXT</p></td></tr></table></table-wrap></sec>
<sec><title>References</title><p>REFERENCE LIST</p></sec></body></article></pmc-articleset>"""


@pytest.fixture
def fake_web(monkeypatch):
    calls = []

    def fake_get(url, accept, allowed, *a, **k):
        calls.append(url)
        if "search" in url:
            return json.dumps(SEARCH).encode(), "application/json", "utf-8", url
        return JATS, "text/xml", "utf-8", url

    monkeypatch.setattr(sources, "http_get", fake_get)
    monkeypatch.setattr(sources, "NCBI_PAUSE", 0)
    return calls


def test_checks_give_plain_reasons():
    def cand(pmcid, lic, types):
        return sources.Candidate(pmcid, "t", "j", "", "2025", lic, types)
    assert sources.check_candidate(cand("PMC1", "cc by", ["Review"]), set()).ok
    assert "CC BY-NC-ND" in sources.check_candidate(cand("PMC1", "cc by-nc-nd", ["Review"]), set()).reason
    assert "case" in sources.check_candidate(cand("PMC1", "cc by", ["Case Reports"]), set()).reason
    assert "already" in sources.check_candidate(cand("PMC1", "cc by", ["Review"]), {"PMC1"}).reason
    assert "preprint" in sources.check_candidate(cand("PMC1", "cc by", ["preprint"]), set()).reason
    assert "retracted" in sources.check_candidate(cand("PMC1", "cc by", ["Retracted Publication"]), set()).reason


def test_full_text_keeps_abstract_and_sections_but_not_references_or_tables():
    text = sources.jats_to_text(JATS, 10_000)
    assert text.startswith("## Abstract") and "## Introduction" in text
    assert "REFERENCE LIST" not in text and "TABLE TEXT" not in text
    assert len(sources.jats_to_text(JATS, 200)) <= 210


def test_short_alternate_terms_are_not_searched():
    assert sources.topic_terms("Carpal Tunnel Syndrome", ["CTS", "median nerve compression"]) == [
        "Carpal Tunnel Syndrome", "median nerve compression"]


def test_fetch_job_saves_good_articles_and_records_skips(data_dir, fake_web):
    rep = jobs.fetch_job(get_settings(), [TOPIC])
    assert rep.status == "ok", rep.messages
    store = PipelineStore(get_settings())
    by_id = {a.pmcid: a for a in store.articles(TOPIC)}
    assert by_id["PMC111"].status == "new" and by_id["PMC444"].status == "new"
    assert by_id["PMC444"].meta["permitted_use"] == "public_domain"
    assert by_id["PMC222"].status == "skipped" and "NC-ND" in by_id["PMC222"].meta["skip_reason"]
    assert "## Abstract" in by_id["PMC111"].text
    # Running again does not fetch the same articles twice.
    jobs.fetch_job(get_settings(), [TOPIC])
    assert len(store.articles(TOPIC)) == len(by_id)
    assert store.runs()[0]["job"] == "fetch"


def test_generate_job_makes_one_ko_into_the_queue(data_dir, fake_web, monkeypatch):
    jobs.fetch_job(get_settings(), [TOPIC])
    monkeypatch.setenv("ANTHROPIC_API_KEY", "test")
    s = get_settings()
    concept = reg.load_registry(s.registry_path)[TOPIC]
    draft = generator.template_draft(jobs.build_request(concept, PipelineStore(s).articles(TOPIC, "new")))
    fake = FakeClaude(chunks=(draft,))
    monkeypatch.setattr(llm, "make_client", lambda: fake)
    rep = jobs.generate_job(s)
    assert rep.status == "ok", rep.messages
    store = PipelineStore(s)
    items = store.queue_items()
    assert [i.ko_id for i in items] == [TOPIC]
    assert items[0].doc.front["review"]["status"] == "draft" and items[0].doc.front["review"]["author"] == "KO Pipeline"
    assert store.source_pack(TOPIC) and items[0].notes["articles"]
    assert all(a.status == "used" for a in store.articles(TOPIC) if a.pmcid in items[0].notes["articles"])
    assert "PMC" in items[0].doc.front["sources"][0]["notes"]
    assert jobs.generate_job(s).status == "nothing to do"  # the topic is in the queue now; 1 KO per run


def test_generate_job_needs_the_ai(data_dir):
    rep = jobs.generate_job(get_settings())
    assert rep.status == "error" and "AI is off" in rep.messages[0]


def test_accept_moves_ko_to_library_as_team_checked(data_dir, example_text):
    s = get_settings()
    store = PipelineStore(s)
    store.add_to_queue(TOPIC, example_text, "# pack", {"created": "today"})
    with pytest.raises(ValueError):
        jobs.accept_ko(s, TOPIC, "")  # a name is needed
    jobs.accept_ko(s, TOPIC, "Allen")
    lib = {e.ko_id: e for e in LocalKOStore(s).list_entries()}
    review = lib[TOPIC].doc.front["review"]
    assert review["status"] == "team_checked" and review["team_checker"] == "Allen"
    assert not store.in_queue(TOPIC) and store.decisions()[0]["decision"] == "accepted"
    assert reg.load_registry(s.registry_path)[TOPIC].status == "drafted"


def test_reject_keeps_a_copy_and_the_reason(data_dir, example_text):
    s = get_settings()
    store = PipelineStore(s)
    store.add_to_queue(TOPIC, example_text, "# pack", {})
    path = store.reject(TOPIC, "Allen", "Facts not in the sources")
    assert path.is_file() and not store.in_queue(TOPIC)
    assert store.decisions()[0]["reason"] == "Facts not in the sources"


def test_suggested_topics_come_from_proposed_concepts(data_dir, example_text):
    s = get_settings()
    doc = parse_ko(example_text)
    doc.front["proposed_concepts"] = [{"term": "Brachial Plexus", "suggested_type": "AnatomicalStructure", "predicate": "X"},
                                      {"term": "Median Nerve", "suggested_type": "AnatomicalStructure", "predicate": "X"}]
    LocalKOStore(s).save(doc)
    terms = [t["term"] for t in jobs.suggested_topics(s)]
    assert "Brachial Plexus" in terms and "Median Nerve" not in terms  # already a topic


def test_only_one_run_at_a_time(data_dir):
    store = PipelineStore(get_settings())
    with store.lock(), pytest.raises(PipelineBusy), store.lock():
        pass
    with store.lock():  # a job started while another runs reports it instead of crashing
        rep = jobs.generate_job(get_settings())
    assert rep.status == "error" and "still working" in rep.messages[0]


def test_finalize_cleans_links_and_fills_labels(data_dir):
    s = get_settings()
    r = reg.load_registry(s.registry_path)
    req = generator.KORequest(r["KO-HAND-COND-001"], ["patient"], "grade 6-8", "beginner", [], "x", registry=r)
    raw = [{"predicate": "AFFECTS", "target_id": "KO-HAND-ANAT-001", "source_ids": ["S1"]},              # label missing
           {"predicate": "TREATS", "subject_id": "KO-HAND-TRT-001", "target_id": "KO-HAND-COND-001"},  # points INTO this KO
           {"predicate": "AFFECTS", "target_id": "KO-HAND-COND-001"},                                  # to itself
           {"predicate": "TREATS", "target_id": "KO-HAND-COND-002"},                                   # wrong types
           {"predicate": "AFFECTS", "target_id": "KO-NOPE-ANAT-001"}]                                  # unknown target
    kept, moved = generator._clean_links(raw, req, r)
    assert kept == [{"predicate": "AFFECTS", "target_id": "KO-HAND-ANAT-001", "target_label": "Median Nerve",
                     "source_ids": ["S1"]}]
    assert len(moved) == 4 and "KO-HAND-TRT-001's KO" in moved[0]


def test_cost_counts_cached_prompt_tokens():
    usage = {"input_tokens": 4, "output_tokens": 1_000_000, "cache_creation_input_tokens": 1_000_000}
    assert jobs._cost("claude-sonnet-5-5", usage) == pytest.approx(2.5 + 10.0, abs=0.01)


def test_fetchable_topics_leave_out_topics_with_a_ko(data_dir, example_text):
    s = get_settings()
    LocalKOStore(s).save(parse_ko(example_text))  # TOPIC now has a KO in the library
    ids = {c.ko_id for c in jobs.fetchable_topics(s, PipelineStore(s))}
    assert TOPIC not in ids and ids
    assert jobs.fetch_targets(s, PipelineStore(s), [TOPIC]) == []
