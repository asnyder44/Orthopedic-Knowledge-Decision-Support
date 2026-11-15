"""Data skeleton: the rehab model, upload checks (incl. the privacy screen), batches, review, summaries, pages."""

from __future__ import annotations

import io
import json
import shutil
import zipfile

import pytest
from conftest import ROOT

from okds import cli, network, records
from okds.config import get_settings
from okds.records.checks import find_identifiers
from okds.records.sample import make_sample
from okds.records.summary import summarize


@pytest.fixture
def model():
    return records.get_model("rehab")


def _kos(data_dir):
    shutil.copytree(ROOT / "data" / "kos", data_dir / "kos", dirs_exist_ok=True)


def test_rehab_model_follows_the_flow_diagram(model):
    edges = {(e["from"], e["predicate"], e["to"]) for e in model.edges()}
    for arrow in [("Patient", "SUBMITS", "PatientFeedback"), ("Patient", "PARTICIPATES_IN", "Rehabilitation"),
                  ("Rehabilitation", "HAS_SESSION", "RehabSession"), ("RehabSession", "PERFORMED_BY", "HealthcareProvider"),
                  ("RecoveryAssessment", "PRODUCES", "PainAssessment"), ("PainAssessment", "MEASURES", "PainLevel"),
                  ("TreatmentAdjustment", "MODIFIES", "RehabilitationPlan"),
                  ("RehabilitationPlan", "DEFINES", "TreatmentSchedule"),
                  ("DischargeAssessment", "DETERMINES", "FollowUpPlan")]:
        assert arrow in edges, arrow
    assert len(model.entities) == 29 and model.root == "Patient"
    assert not records.model_errors()


def test_synthetic_sample_passes_every_check(data_dir, model):
    s = get_settings()
    result = records.RecordStore(s, model).check(make_sample(12, seed=3), records.ko_types(s))
    assert result.ok, [str(i) for i in result.errors[:5]]
    assert set(result.counts) == set(model.entities)  # every box in the diagram has rows


@pytest.mark.parametrize("text,label", [("call 317-555-0123", "a phone number"), ("jane.doe@example.org", "an email address"),
                                        ("born 1958-04-12", "a full date"), ("MRN 445566", "a record number"),
                                        ("SSN 123-45-6789", "a Social Security number"), ("aged 93", "an age (use an age band)"),
                                        ("lives at 12 Oak Street", "a street address")])
def test_privacy_screen_finds_identifiers(text, label):
    assert label in find_identifiers(text)


def test_privacy_screen_leaves_normal_values_alone():
    for ok in ("NRS 0-10", "18-29", "tendon gliding", "P-0001", "KO-HAND-COND-001", "grip strength (kg)", "day 42"):
        assert not find_identifiers(ok), ok


def test_upload_refuses_identifiers_extra_columns_and_bad_links(data_dir, model):
    s = get_settings()
    tables = {"Patient": [{"patient_id": "P-1", "age_band": "45", "sex": "female", "condition_ko": "KO-HAND-COND-001",
                           "email": "a@b.org"},
                          {"patient_id": "12345678", "age_band": "30-39", "sex": "male", "condition_ko": "KO-HAND-PROC-001"}],
              "Rehabilitation": [{"rehab_id": "R-1", "patient_id": "P-404"}],
              "Secrets": [{"x": "1"}]}
    r = records.RecordStore(s, model).check(tables, records.ko_types(s))
    text = " | ".join(str(i) for i in r.errors)
    for expected in ("unknown column", "not one of", "email address", "record number", "Procedure KO",
                     "points to Patient 'P-404'", "'Secrets' is not part of"):
        assert expected in text, expected


def test_batch_review_flow_and_summaries(data_dir, model):
    s = get_settings()
    store = records.RecordStore(s, model)
    t = make_sample(10, seed=1)
    b = store.save(t, store.check(t, records.ko_types(s)), uploaded_by="Test", synthetic=True, agreement="synthetic")
    assert b.status == "pending" and not store.accepted_tables()  # nothing is used before review
    with pytest.raises(records.UploadError):
        store.decide(b.id, "rejected", "Reviewer", "")  # a rejection needs a reason
    store.decide(b.id, "accepted", "Reviewer")
    assert store.accepted_tables()["Patient"] and store.ko_usage()
    again = store.check(t, records.ko_types(s))
    assert any("already accepted" in str(i) for i in again.errors)  # the same ids can't be uploaded twice
    summ = summarize(model, store.accepted_tables())
    patient = next(e for e in summ["entities"] if e["name"] == "Patient")
    assert all(v["count"] == "<5" for c in patient["categories"] for v in c["values"] if v["n"] < 5)


def test_read_upload_accepts_zip_and_json():
    buf = io.BytesIO()
    with zipfile.ZipFile(buf, "w") as z:
        z.writestr("Patient.csv", "patient_id,age_band,sex\nP-1,30-39,female\n")
    tables = records.read_upload([("batch.zip", buf.getvalue()),
                                  ("more.json", json.dumps({"Patient": [{"patient_id": "P-2"}]}).encode())])
    assert [r["patient_id"] for r in tables["Patient"]] == ["P-1", "P-2"]
    with pytest.raises(records.UploadError):
        records.read_upload([("notes.docx", b"x")])


def test_accepted_records_show_in_the_discovery_network(data_dir, model):
    _kos(data_dir)
    s = get_settings()
    store = records.RecordStore(s, model)
    t = make_sample(20, seed=2)
    store.save(t, store.check(t, records.ko_types(s)), uploaded_by="T", synthetic=True, agreement="s", status="accepted")
    usage = network.build_network(s)["data_usage"]
    assert any(k.startswith("rehab:TherapeuticIntervention") for v in usage.values() for k in v)


def test_cli_template_sample_check(data_dir, tmp_path, capsys):
    assert cli.main(["data", "template", str(tmp_path / "t")]) == 0
    assert (tmp_path / "t" / "Patient.csv").read_text(encoding="utf-8").startswith("patient_id,")
    assert cli.main(["data", "sample", str(tmp_path / "s"), "--patients", "6"]) == 0
    assert cli.main(["data", "check", str(tmp_path / "s")]) == 0
    assert cli.main(["data", "upload", str(tmp_path / "s")]) == 1  # needs --name and --synthetic / agreement
    assert cli.main(["data", "upload", str(tmp_path / "s"), "--name", "T", "--synthetic"]) == 0
    assert "pending" in capsys.readouterr().out


# ---------------------------------------------------------------- pages

def test_data_page_and_downloads(client, data_dir):
    html = client.get("/ko/data").get_data(as_text=True)
    assert "Data Skeleton" in html and 'id="dm-svg"' in html and "Before you upload" in html
    z = zipfile.ZipFile(io.BytesIO(client.get("/ko/data/rehab/template").data))
    assert "Patient.csv" in z.namelist() and "DATA_DICTIONARY.csv" in z.namelist()
    z = zipfile.ZipFile(io.BytesIO(client.get("/ko/data/rehab/sample").data))
    assert len(z.namelist()) == 29
    assert client.get("/ko/data/rehab/model.json").get_json()["root"] == "Patient"


def test_upload_sample_then_accept_in_review(client, data_dir):
    _kos(data_dir)
    r = client.post("/ko/data/upload", data={"model": "rehab", "kind": "synthetic", "name": "Tester", "use_sample": "1",
                                             "csrf_token": "test-token"})
    assert r.status_code == 302
    store = records.RecordStore(get_settings(), records.get_model("rehab"))
    (b,) = store.batches("pending")
    html = client.get("/ko/review?tab=data").get_data(as_text=True)
    assert f"Batch {b.id}" in html and "Synthetic" in html
    r = client.post(f"/ko/data/{b.id}/decide", data={"model": "rehab", "name": "Reviewer", "decision": "accept",
                                                     "csrf_token": "test-token"})
    assert r.status_code == 302 and store.get(b.id).status == "accepted"
    html = client.get("/ko/data?tab=summary").get_data(as_text=True)
    assert "Accepted records only" in html


def test_real_data_needs_attestation_and_agreement(client, data_dir, tmp_path):
    data = {"model": "rehab", "kind": "real", "name": "T", "csrf_token": "test-token",
            "files": (io.BytesIO(b"patient_id,age_band,sex\nP-1,30-39,female\n"), "Patient.csv")}
    client.post("/ko/data/upload", data=data, content_type="multipart/form-data")
    assert not records.RecordStore(get_settings(), records.get_model("rehab")).batches()


def test_visitors_cannot_upload_or_decide(visitor, data_dir):
    assert visitor.post("/ko/data/upload", data={"model": "rehab", "use_sample": "1", "name": "x", "kind": "synthetic",
                                                 "csrf_token": "test-token"}).status_code == 302
    assert not records.RecordStore(get_settings(), records.get_model("rehab")).batches()
    assert visitor.get("/ko/data").status_code == 200
