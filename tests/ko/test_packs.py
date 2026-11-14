"""`okds sources`: search the OrthoInfo dataset and set a KO's sources (pack + front matter + References)."""

from __future__ import annotations

import shutil

from conftest import EXAMPLE

from okds import cli, collect, packs
from okds.config import get_settings
from okds.ko import parse_ko


def test_local_search_finds_patient_pages_first():
    hits = packs.search_local("carpal tunnel syndrome")
    assert hits and hits[0][1]["source"] in ("medlineplus", "niams")


def test_set_sources_rewrites_pack_and_ko(data_dir, monkeypatch):
    (data_dir / "kos" / "hand").mkdir(parents=True)
    shutil.copy(EXAMPLE, data_dir / "kos" / "hand" / EXAMPLE.name)
    doc_id = packs.search_local("carpal tunnel syndrome")[0][1]["doc_id"]
    cand = collect.Candidate("plos", "CTS trial", "https://doi.org/10.1/x", publisher="PLOS ONE", year="2024",
                             abstract="Carpal tunnel " * 40, licence="CC BY", kind="trial", permitted_use="open_license")
    collect.save_candidates(packs.candidates_path(get_settings(), "KO-HAND-COND-001"), "Carpal Tunnel Syndrome", [cand])
    assert cli.main(["sources", "set", "KO-HAND-COND-001", f"local:{doc_id}", "c1"]) == 0
    pack = (data_dir / "sources" / "packs" / "SP-KO-HAND-COND-001.md").read_text(encoding="utf-8")
    assert "## S1" in pack and "## S2" in pack and "CTS trial" in pack
    ko = parse_ko(next((data_dir / "kos").rglob("KO-HAND-COND-001_*.md")).read_text(encoding="utf-8"))
    assert [s["id"] for s in ko.front["sources"]] == ["S1", "S2"]
    assert ko.front["sources"][0]["permitted_use"] == "public_domain" and "text" not in ko.front["sources"][0]
    assert "CTS trial" in ko.body.split("## References", 1)[1]
    assert cli.main(["sources", "set", "KO-HAND-COND-001", "c9"]) == 1  # no such candidate: nothing changed
