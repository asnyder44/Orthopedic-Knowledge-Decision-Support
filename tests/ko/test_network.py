"""Discovery Network (prototype): the graph built from the KOs, and its page."""

from __future__ import annotations

import shutil

from conftest import ROOT

from okds import network
from okds.config import get_settings


def _seed(data_dir) -> None:
    shutil.copytree(ROOT / "data" / "kos", data_dir / "kos", dirs_exist_ok=True)


def test_network_has_kos_links_with_sources_and_proposed_topics(data_dir):
    _seed(data_dir)
    net = network.build_network(get_settings())
    kinds = {n["kind"] for n in net["nodes"]}
    assert kinds >= {"ko", "proposed"}
    real = [e for e in net["edges"] if not e["proposed"]]
    assert real and all(e["evidence"] for e in real)  # every starter-KO link names its sources
    ids = {n["id"] for n in net["nodes"]}
    assert all(e["source"] in ids and e["target"] in ids for e in net["edges"])


def test_duplicate_proposals_are_merged(data_dir):
    _seed(data_dir)
    net = network.build_network(get_settings())
    bctq = [n for n in net["nodes"] if "boston carpal tunnel" in n["label"].lower()]
    assert len(bctq) == 1 and len(bctq[0]["proposed_by"]) == 2
    assert network.concept_key("Tinel's Sign") == network.concept_key("Tinel’s sign (tapping test)")


def test_proposed_links_follow_the_vocabulary_direction(data_dir):
    _seed(data_dir)
    net = network.build_network(get_settings())
    # "Cubital Tunnel Release TREATS Cubital Tunnel Syndrome": the procedure is the subject
    e = next(e for e in net["edges"] if e["proposed"] and e["predicate"] == "TREATS" and "cubital-tunnel-release" in e["source"])
    assert e["target"] == "KO-HAND-COND-002"


def test_journey_and_insights(data_dir):
    _seed(data_dir)
    net = network.build_network(get_settings())
    stages = {s["key"]: s for s in network.journey(net, "KO-HAND-COND-001")}
    assert {i["id"] for i in stages["diagnosis"]["items"]} >= {"KO-HAND-DX-001", "KO-HAND-DX-002"}
    assert stages["technology"]["items"] and all(i["kind"] == "proposed" for i in stages["technology"]["items"])
    ins = network.insights(net)
    assert ins["most_connected"][0]["id"] == "KO-HAND-COND-001"
    assert ins["counts"]["kos"] == 9 and ins["merged"]


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
