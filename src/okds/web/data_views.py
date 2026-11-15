"""KO Portal pages for the data skeleton (structured records that follow a data model).

  /ko/data                    the model (flow diagram + data dictionary), upload, batches, summaries
  /ko/data/<model>/template   empty CSV templates + data dictionary (.zip)
  /ko/data/<model>/sample     the synthetic sample as a .zip (same format as an upload)
  POST /ko/data/upload        check a batch (automatic checks + privacy screen) and send it to review
  POST /ko/data/<batch>/decide  accept / reject in the Review queue
"""

from __future__ import annotations

import csv
import io
import json
import zipfile

from flask import abort, flash, redirect, render_template, request, send_file, session, url_for

from .. import records
from ..config import get_settings
from ..records.sample import make_sample
from ..records.summary import summarize
from . import bp, can_edit, editor_required

PREVIEW_ROWS = 8
MAX_ISSUES_SHOWN = 40


def _model(name: str | None):
    ms = records.models()
    if not ms:
        abort(404)
    return ms.get(name or "") or ms.get("rehab") or next(iter(ms.values()))


def pending_batches(s) -> list:
    out = []
    for m in records.models().values():
        out += records.RecordStore(s, m).batches("pending")
    return out


def batch_detail(s, batch_id: str | None) -> dict | None:
    pending = pending_batches(s)
    if not pending:
        return None
    b = next((x for x in pending if x.id == batch_id), pending[0])
    tables = b.tables()
    return {"batch": b, "preview": {e: rows[:PREVIEW_ROWS] for e, rows in tables.items()},
            "counts": {e: len(rows) for e, rows in tables.items()}}


def _ko_titles(s) -> dict[str, str]:
    from ..registry import load_registry

    return {c.ko_id: c.preferred_term for c in load_registry(s.registry_path).values()}


@bp.get("/data")
def data_page():
    s = get_settings()
    m = _model(request.args.get("model"))
    store = records.RecordStore(s, m)
    batches = store.batches()
    summary = summarize(m, store.accepted_tables())
    usage = store.ko_usage()
    return render_template(
        "ko/data.html", active="data", model=m, models=records.models(), model_errors=records.model_errors(),
        model_json=m.to_json(), batches=batches, summary=summary, usage=usage, ko_titles=_ko_titles(s),
        tab=request.args.get("tab", "model"), check=session.pop("data_check", None), name=session.get("reviewer_name", ""))


@bp.get("/data/<model_name>/model.json")
def data_model_json(model_name: str):
    return _model(model_name).to_json()


def _zip(files: dict[str, str], name: str):
    buf = io.BytesIO()
    with zipfile.ZipFile(buf, "w", zipfile.ZIP_DEFLATED) as z:
        for fname, text in files.items():
            z.writestr(fname, text)
    buf.seek(0)
    return send_file(buf, mimetype="application/zip", as_attachment=True, download_name=name)


def _csv(fields: list[str], rows: list[dict]) -> str:
    out = io.StringIO()
    w = csv.DictWriter(out, fieldnames=fields, extrasaction="ignore")
    w.writeheader()
    w.writerows(rows)
    return out.getvalue()


def dictionary_csv(m) -> str:
    rows = []
    for e in m.entities.values():
        for f in e.fields.values():
            lo, hi = ("" if f.min is None else f"{f.min:g}"), ("" if f.max is None else f"{f.max:g}")
            rows.append({"entity": e.name, "field": f.name, "type": f.type,
                         "required": "yes" if f.required or f.type == "id" else "",
                         "points_to": f.ref or ("KO: " + "/".join(f.ko_types) if f.type == "ko" else ""),
                         "arrow_label": f.predicate, "allowed_values": "; ".join(f.values),
                         "range": f"{lo}-{hi}" if lo or hi else "", "description": f.description})
    cols = ["entity", "field", "type", "required", "points_to", "arrow_label", "allowed_values", "range", "description"]
    return _csv(cols, rows)


@bp.get("/data/<model_name>/template")
def data_template(model_name: str):
    m = _model(model_name)
    files = {f"{e.name}.csv": _csv(list(e.fields), []) for e in m.entities.values()}
    files["DATA_DICTIONARY.csv"] = dictionary_csv(m)
    files["README.txt"] = (f"{m.title} (model '{m.name}' v{m.version})\n\n{m.description}\n\n"
                           "Fill one CSV per entity (keep the file names and column names). Leave unused files out.\n"
                           "People are study codes, ages are bands, time is 'day N' since the rehabilitation started.\n"
                           "No names, contact details, record numbers or full dates. See DATA_DICTIONARY.csv.\n")
    return _zip(files, f"{m.name}-template.zip")


@bp.get("/data/<model_name>/sample")
def data_sample(model_name: str):
    m = _model(model_name)
    if m.name != "rehab":
        abort(404)
    t = make_sample()
    files = {f"{e}.csv": _csv(list(m.entities[e].fields), [{k: _fmt(v) for k, v in r.items()} for r in rows])
             for e, rows in t.items()}
    return _zip(files, "rehab-synthetic-sample.zip")


def _fmt(v):
    if isinstance(v, bool):
        return "yes" if v else "no"
    return "" if v is None else v


@bp.post("/data/upload")
@editor_required
def data_upload():
    s = get_settings()
    m = _model(request.form.get("model"))
    synthetic = request.form.get("kind") == "synthetic"
    agreement = " ".join(request.form.get("agreement", "").split())[:200]
    name = " ".join(request.form.get("name", "").split())[:80]
    if name:
        session["reviewer_name"] = name
    back = redirect(url_for("ko.data_page", model=m.name, tab="upload"))
    if not name:
        flash("Type your name (it is saved with the batch).", "error")
        return back
    if not synthetic and (request.form.get("deidentified") != "yes" or not agreement):
        flash("For real data, tick that it is de-identified and give the data agreement or approval it is shared under.",
              "error")
        return back
    files = [(f.filename, f.read()) for f in request.files.getlist("files") if f and f.filename]
    if request.form.get("use_sample") == "1" and m.name == "rehab":
        t = make_sample()
        tables = {e: [{k: _fmt(v) for k, v in r.items()} for r in rows] for e, rows in t.items()}
        synthetic = True
    elif not files:
        flash("Choose the CSV files (or a .zip or .json) to upload.", "error")
        return back
    else:
        try:
            tables = records.read_upload(files)
        except (records.UploadError, zipfile.BadZipFile) as e:
            flash(f"Not uploaded: {e}", "error")
            return back
    store = records.RecordStore(s, m)
    result = store.check(tables, records.ko_types(s))
    report = {"ok": result.ok, "counts": result.counts, "errors": [str(i) for i in result.errors[:MAX_ISSUES_SHOWN]],
              "n_errors": len(result.errors), "warnings": [str(i) for i in result.warnings[:MAX_ISSUES_SHOWN]],
              "n_warnings": len(result.warnings)}
    if result.ok:
        b = store.save(tables, result, uploaded_by=name, synthetic=synthetic,
                       agreement="synthetic sample (no real people)" if synthetic else agreement,
                       note=" ".join(request.form.get("note", "").split())[:300])
        report["batch"] = b.id
        flash(f"Batch {b.id} passed the automatic checks ({sum(result.counts.values())} rows). It is waiting in the "
              f"Review queue; it is used only after a person accepts it.", "success")
    else:
        flash(f"Not saved: {len(result.errors)} problem(s). Nothing was stored; fix the files and upload again.", "error")
    session["data_check"] = report
    return back


@bp.post("/data/<batch_id>/decide")
@editor_required
def data_decide(batch_id: str):
    s = get_settings()
    m = _model(request.form.get("model"))
    name = " ".join(request.form.get("name", "").split())[:80]
    if name:
        session["reviewer_name"] = name
    decision = "accepted" if request.form.get("decision") == "accept" else "rejected"
    try:
        records.RecordStore(s, m).decide(batch_id, decision, name, request.form.get("reason", ""))
    except records.UploadError as e:
        flash(f"Not changed: {e}", "error")
        return redirect(url_for("ko.review_page", tab="data", batch=batch_id))
    flash(f"Batch {batch_id} {decision}." + (" Its records now count in the summaries and the Discovery Network."
                                             if decision == "accepted" else ""), "success")
    return redirect(url_for("ko.review_page", tab="data"))


__all__ = ["batch_detail", "can_edit", "data_page", "json", "pending_batches"]
