"""The open-access source collector (offline: every API answer is faked)."""

from __future__ import annotations

import json

import pytest

from okds import collect

EPMC = {"resultList": {"result": [
    {"id": "PMC1", "source": "PMC", "pmcid": "PMC1", "doi": "10.1/a", "title": "Trigger finger: a systematic review.",
     "pubYear": "2024", "license": "cc by", "abstractText": "Trigger finger is " + "common. " * 60,
     "journalInfo": {"journal": {"title": "J Hand Surg"}}, "pubTypeList": {"pubType": ["review"]}},
    {"id": "PPR9", "source": "PPR", "title": "A rare case of trigger finger", "pubYear": "2025", "license": "",
     "abstractText": "We describe trigger finger " + "in a patient. " * 40, "pubTypeList": {"pubType": ["Preprint"]}},
    {"id": "PMC2", "source": "PMC", "pmcid": "PMC2", "title": "Knee bracing in skiers", "pubYear": "2024",
     "license": "cc by", "abstractText": "Not about the topic. " * 30},
]}}
PLOS = {"response": {"docs": [{"id": "10.1/a", "title_display": "Trigger finger: a systematic review",
                               "abstract": ["Same paper, shorter."], "journal": "PLOS ONE", "publication_date": "2024"}]}}
MEDLINE = """<nlmSearchResult><list><document url="https://medlineplus.gov/fingerinjuriesanddisorders.html">
<content name="title">Finger Injuries</content>
<content name="FullSummary">&lt;p&gt;Trigger finger makes a finger catch.&lt;/p&gt;</content>
</document></list></nlmSearchResult>"""


@pytest.fixture
def fake_net(monkeypatch):
    def fake_get(url, headers=None, retries=3):
        if "europepmc" in url:
            return json.dumps(EPMC)
        if "plos.org" in url:
            return json.dumps(PLOS)
        if "medlineplus" in url or "nlm.nih.gov" in url:
            return MEDLINE
        raise OSError("offline")
    monkeypatch.setattr(collect, "_get", fake_get)


def test_collect_filters_dedupes_and_ranks(fake_net):
    logs = []
    cands = collect.collect("trigger finger", per_provider=5, providers=["medlineplus", "europepmc", "plos", "doaj"],
                            log=logs.append)
    titles = [c.title for c in cands]
    assert "Knee bracing in skiers" not in titles                 # not about the topic
    review = next(c for c in cands if c.doi == "10.1/a")
    assert sorted(review.providers) == ["europepmc", "plos"]      # same DOI from two providers: one record
    assert review.kind == "systematic review" and review.permitted_use == "open_license"
    case = next(c for c in cands if "rare case" in c.title)
    assert case.kind == "case report" and case.score < review.score
    assert any("doaj: skipped" in line for line in logs)          # a provider that fails is skipped, not fatal


def test_pack_starts_with_the_patient_page_and_keeps_licences(fake_net):
    cands = collect.collect("trigger finger", per_provider=5, providers=["medlineplus", "europepmc"], log=lambda _: None)
    pack = collect.pick_pack(cands, patient=True, size=3)
    assert pack[0].provider == "medlineplus" and pack[0].permitted_use == "public_domain"
    src = collect.as_source(pack[1], "S2", today="2026-11-14")
    assert src["id"] == "S2" and src["retrieved_date"] == "2026-11-14" and src["text"]
    assert src["permitted_use"] in ("open_license", "link_and_paraphrase", "public_domain")
    text = collect.render_pack("KO-HAND-COND-003", "Trigger Finger", [src])
    assert text.startswith("# Source pack SP-KO-HAND-COND-003") and "text: |" in text


@pytest.mark.parametrize("licence,expected", [("cc by", "open_license"), ("CC0", "open_license"),
                                              ("cc by-nc-nd", "link_and_paraphrase"), ("", "link_and_paraphrase")])
def test_licences(licence, expected):
    assert collect.classify_licence(licence) == expected


def test_collected_sources_endpoint(client, data_dir, fake_net):
    cands = collect.collect("trigger finger", providers=["medlineplus", "europepmc"], log=lambda _: None)
    collect.save_candidates(data_dir / "sources" / "candidates" / "KO-HAND-COND-003.json", "Trigger Finger", cands)
    j = client.get("/ko/api/collected/KO-HAND-COND-003").get_json()
    assert j["count"] == len(cands) and j["sources"][0]["permitted_use"] == "public_domain"
    assert client.get("/ko/api/collected/KO-NOPE-COND-009").status_code == 404
