"""Discovery Network (prototype): the graph built from the KOs, and its page."""

from __future__ import annotations

import shutil

from conftest import ROOT

from okds import network
from okds.config import get_settings
from okds.ko import parse_ko, render_ko


def _seed(data_dir) -> None:
    shutil.copytree(ROOT / "data" / "kos", data_dir / "kos", dirs_exist_ok=True)


def _two_kos(data_dir, example_text) -> None:
    """Two small KOs (the example and a copy) with their own registry, so the proposals are predictable:
    both propose 'Electromyography (EMG)'; the copy also proposes a procedure that would TREAT it."""
    folder = data_dir / "kos" / "hand"
    folder.mkdir(parents=True)
    first = parse_ko(example_text)
    first.front["proposed_concepts"] = [{"term": "Electromyography (EMG)", "suggested_type": "DiagnosticTest",
                                         "predicate": "DIAGNOSED_BY", "reason": "[S1]"}]
    (folder / "a.md").write_text(render_ko(first), encoding="utf-8")
    doc = parse_ko(example_text)
    doc.front.update(ko_id="KO-HAND-COND-009", title="Test Condition", preferred_term="Test Condition")
    doc.front["proposed_concepts"] = [
        {"term": "Electromyography", "suggested_type": "DiagnosticTest", "predicate": "DIAGNOSED_BY", "reason": "[S1]"},
        {"term": "Test Release Surgery", "suggested_type": "Procedure", "predicate": "TREATS", "reason": "[S2]"}]
    (folder / "b.md").write_text(render_ko(doc), encoding="utf-8")
    (data_dir / "registry.csv").write_text(
        "ko_id,preferred_term,alternate_terms,ko_type,specialty,mesh_id,icd10cm,status\n"
        "KO-HAND-COND-001,Carpal Tunnel Syndrome,CTS,Condition,HAND,,,drafted\n"
        "KO-HAND-COND-009,Test Condition,,Condition,HAND,,,drafted\n", encoding="utf-8")


def test_network_has_kos_links_with_sources_and_proposed_topics(data_dir):
    _seed(data_dir)
    net = network.build_network(get_settings())
    kinds = {n["kind"] for n in net["nodes"]}
    assert kinds >= {"ko", "proposed"}
    real = [e for e in net["edges"] if not e["proposed"]]
    assert real and all(e["evidence"] for e in real)  # every KO link names its sources
    ids = {n["id"] for n in net["nodes"]}
    assert all(e["source"] in ids and e["target"] in ids for e in net["edges"])


def test_duplicate_proposals_are_merged(data_dir, example_text):
    _two_kos(data_dir, example_text)
    net = network.build_network(get_settings())
    emg = [n for n in net["nodes"] if n["label"].lower().startswith("electromyography")]
    assert len(emg) == 1 and sorted(emg[0]["proposed_by"]) == ["KO-HAND-COND-001", "KO-HAND-COND-009"]
    assert emg[0]["label"] == "Electromyography"  # the shorter name is kept
    assert network.concept_key("Tinel's Sign") == network.concept_key("Tinel’s sign (tapping test)")
    assert network.insights(net)["merged"] == ["Electromyography"]


def test_proposed_links_follow_the_vocabulary_direction(data_dir, example_text):
    _two_kos(data_dir, example_text)
    net = network.build_network(get_settings())
    # "Test Release Surgery TREATS Test Condition": a Procedure is the subject of TREATS
    e = next(e for e in net["edges"] if e["proposed"] and e["predicate"] == "TREATS")
    assert e["source"] == "proposed:test-release-surgery" and e["target"] == "KO-HAND-COND-009"


def test_proposals_point_at_topics_that_exist(data_dir):
    """A proposed topic that is on the KO Topics list links to that topic instead of a new node."""
    _seed(data_dir)
    net = network.build_network(get_settings())
    labels = {n["label"].lower() for n in net["nodes"] if n["kind"] == "proposed"}
    assert not any(label.startswith("boston carpal tunnel") for label in labels)
    # Cubital Tunnel Release TREATS Cubital Tunnel Syndrome: stated by the procedure (or proposed by the condition)
    assert any(e["predicate"] == "TREATS" and e["source"] == "KO-HAND-PROC-003" and e["target"] == "KO-HAND-COND-002"
               for e in net["edges"])


def test_journey_and_insights(data_dir):
    _seed(data_dir)
    net = network.build_network(get_settings())
    stages = {s["key"]: s for s in network.journey(net, "KO-HAND-COND-001")}
    assert {i["id"] for i in stages["diagnosis"]["items"]} >= {"KO-HAND-DX-001", "KO-HAND-DX-002", "KO-HAND-DX-003"}
    assert "KO-HAND-DEV-001" in {i["id"] for i in stages["technology"]["items"]}  # via Wrist Splinting
    ins = network.insights(net)
    assert ins["counts"]["kos"] == len(list((data_dir / "kos").rglob("*.md")))
    assert ins["most_connected"][0]["links"] >= ins["most_connected"][-1]["links"]


def test_network_page_and_api(client, data_dir):
    _seed(data_dir)
    html = client.get("/ko/network").get_data(as_text=True)
    assert "Information Discovery Network" in html and "Prototype layout" in html and 'id="net-svg"' in html
    for tab in ("Explore the network", "Knowledge journey", "Research discovery", "Network insights"):
        assert tab in html
    assert client.get("/ko/network?tab=journey&condition=KO-HAND-COND-002").status_code == 200
    j = client.get("/ko/api/network").get_json()
    assert j["nodes"] and j["edges"] and "TREATS" in j["predicates"]
    assert "Discovery Network" in client.get("/library").get_data(as_text=True)


def test_network_page_with_an_empty_library(client):
    html = client.get("/ko/network").get_data(as_text=True)
    assert "No condition KOs yet" in html
