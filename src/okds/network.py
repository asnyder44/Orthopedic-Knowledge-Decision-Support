"""Information Discovery Network: the Knowledge Objects as one connected dataset.

PROTOTYPE. This turns the saved KOs into a graph that the Discovery Network pages (/ko/network) show:

  nodes  written KOs ("ko"), registry topics with no KO yet ("planned"), and concepts that KOs propose
         in `proposed_concepts` but nobody has written yet ("proposed"; duplicates are merged).
  edges  each KO `relationship` (predicate + target + the KO sources that support it), plus the
         links proposed concepts would add ("proposed": True).

Everything is computed from the KO Markdown files on each request, so it is always current. When the
team moves the graph to a database (e.g. Neo4j, see Kyle's knowledge vision), `build_network` is the
one place to replace: the pages only use its JSON shape.
"""

from __future__ import annotations

import re
from collections import Counter, defaultdict
from dataclasses import asdict, dataclass, field
from typing import Any

from . import vocab
from .config import Settings
from .kindex import load_docs
from .ko import KODocument, as_dict, as_list
from .registry import load_registry

# The "knowledge journey" from the original proposal: condition → diagnosis → evidence → treatment →
# procedure → technology → outcomes and recovery. Each stage collects one KO type.
JOURNEY = [
    ("anatomy", "Body basics", ["AnatomicalStructure"]),
    ("signs", "Symptoms and risks", ["Concept"]),
    ("diagnosis", "Diagnosis", ["DiagnosticTest"]),
    ("treatment", "Treatment without surgery", ["Treatment"]),
    ("surgery", "Surgery", ["Procedure"]),
    ("technology", "Devices and technology", ["Device"]),
    ("outcomes", "Outcomes", ["OutcomeMeasure"]),
    ("recovery", "Recovery", ["RehabProtocol"]),
    ("related", "Related conditions", ["Condition"]),
]
# Not built yet: kinds of objects the vision adds beyond KOs (shown as "coming" in the UI).
PLANNED_OBJECT_TYPES = [
    ("Research study", "PubMed / Europe PMC publications linked with STUDIED_IN"),
    ("Clinical trial", "ClinicalTrials.gov studies: conditions, interventions, outcomes"),
    ("Guideline", "AAOS and other clinical practice guidelines (RECOMMENDED_BY)"),
    ("Organization", "Device makers, hospitals, IMPACT partners (MANUFACTURED_BY)"),
]


@dataclass
class Node:
    id: str
    label: str
    kind: str                  # "ko" | "planned" | "proposed"
    ko_type: str
    cluster: int = 0
    status: str = ""           # KO review status, registry status, or "proposed"
    summary: str = ""
    proposed_by: list[str] = field(default_factory=list)   # KO IDs that propose this concept
    sources: list[dict[str, Any]] = field(default_factory=list)


@dataclass
class Edge:
    source: str
    target: str
    predicate: str
    proposed: bool = False
    source_ids: list[str] = field(default_factory=list)
    evidence: list[dict[str, Any]] = field(default_factory=list)   # the KO sources behind this link
    reason: str = ""
    stated_in: str = ""        # the KO that states (or proposes) this link


def concept_key(term: str) -> str:
    """'Boston Carpal Tunnel Questionnaire (BCTQ)' and 'Boston Carpal Tunnel Questionnaire' -> one key.
    A deliberately simple form of entity resolution; the team can replace it with a better matcher."""
    term = re.sub(r"\([^)]*\)", " ", term.lower())
    term = term.replace("’", "'").replace("'s", "")
    return " ".join(re.findall(r"[a-z0-9]+", term))


def _summary(doc: KODocument) -> str:
    return re.sub(r"\s*\[S\d+\]", "", str(doc.front.get("summary") or "")).strip()


def _orient(predicate: str, ko_type: str, other_type: str) -> bool:
    """True when a proposed link should point from the proposed concept to the KO (e.g. a Procedure TREATS
    this Condition), judged by which direction the vocabulary allows."""
    forward = vocab.predicate_allows(predicate, ko_type, other_type)
    backward = vocab.predicate_allows(predicate, other_type, ko_type)
    return forward is False and backward is True


def build_network(settings: Settings) -> dict[str, Any]:
    docs = load_docs(settings)
    registry = load_registry(settings.registry_path)
    types = vocab.load_vocab()["ko_types"]
    nodes: dict[str, Node] = {}
    for d in docs:
        f = d.front
        nodes[d.ko_id] = Node(
            id=d.ko_id, label=str(f.get("title", d.ko_id)), kind="ko", ko_type=str(f.get("ko_type", "")),
            cluster=int(f.get("cluster") or 0) if str(f.get("cluster") or "0").isdigit() else 0,
            status=str(as_dict(f.get("review")).get("status", "draft")), summary=_summary(d),
            sources=[{k: s.get(k) for k in ("id", "title", "publisher", "url")}
                     for s in as_list(f.get("sources")) if isinstance(s, dict)])
    for c in registry.values():
        if c.ko_id not in nodes:
            nodes[c.ko_id] = Node(id=c.ko_id, label=c.preferred_term, kind="planned", ko_type=c.ko_type,
                                  cluster=int(types.get(c.ko_type, {}).get("cluster", 0)), status=c.status)

    # A proposal whose name matches a topic that already exists points at that topic instead of a new node.
    known: dict[str, str] = {}
    for c in registry.values():
        for name in (c.preferred_term, *c.alternate_terms):
            known.setdefault(concept_key(name), c.ko_id)
    for n in list(nodes.values()):
        known.setdefault(concept_key(n.label), n.id)

    edges: list[Edge] = []
    real_pairs: set[tuple[str, str]] = set()
    for d in docs:
        for r in as_list(d.front.get("relationships")):
            if isinstance(r, dict) and r.get("target_id"):
                real_pairs.update({(d.ko_id, str(r["target_id"])), (str(r["target_id"]), d.ko_id)})
    for d in docs:
        by_sid = {str(s.get("id")): s for s in as_list(d.front.get("sources")) if isinstance(s, dict)}
        for r in as_list(d.front.get("relationships")):
            if not isinstance(r, dict) or not r.get("target_id"):
                continue
            target = str(r["target_id"])
            if target not in nodes:  # points at something we don't have: show it as planned
                nodes[target] = Node(id=target, label=str(r.get("target_label") or target), kind="planned",
                                     ko_type="", status="not in registry")
            sids = [str(s) for s in as_list(r.get("source_ids"))]
            edges.append(Edge(source=d.ko_id, target=target, predicate=str(r.get("predicate", "")), source_ids=sids,
                              evidence=[{k: by_sid[s].get(k) for k in ("id", "title", "publisher", "url")}
                                        for s in sids if s in by_sid], stated_in=d.ko_id))
        for p in as_list(d.front.get("proposed_concepts")):
            if not isinstance(p, dict) or not p.get("term"):
                continue
            existing = known.get(concept_key(str(p["term"])))
            if existing and existing != d.ko_id:
                if (d.ko_id, existing) in real_pairs:
                    continue  # already linked for real
                pred = str(p.get("predicate") or "RELATED")
                src, dst = ((existing, d.ko_id) if _orient(pred, nodes[d.ko_id].ko_type, nodes[existing].ko_type)
                            else (d.ko_id, existing))
                edges.append(Edge(source=src, target=dst, predicate=pred, proposed=True,
                                  reason=str(p.get("reason") or ""), stated_in=d.ko_id))
                real_pairs.update({(d.ko_id, existing), (existing, d.ko_id)})
                continue
            pid = "proposed:" + concept_key(str(p["term"])).replace(" ", "-")
            node = nodes.get(pid)
            if node is None:
                node = nodes[pid] = Node(id=pid, label=str(p["term"]), kind="proposed",
                                         ko_type=str(p.get("suggested_type") or "Concept"),
                                         cluster=int(types.get(str(p.get("suggested_type")), {}).get("cluster", 0)),
                                         status="proposed")
            elif len(str(p["term"])) < len(node.label):
                node.label = str(p["term"])  # keep the shorter name
            if d.ko_id not in node.proposed_by:
                node.proposed_by.append(d.ko_id)
            pred = str(p.get("predicate") or "RELATED")
            src, dst = (pid, d.ko_id) if _orient(pred, nodes[d.ko_id].ko_type, node.ko_type) else (d.ko_id, pid)
            edges.append(Edge(source=src, target=dst, predicate=pred, proposed=True, reason=str(p.get("reason") or ""),
                              stated_in=d.ko_id))

    return {
        "nodes": [asdict(n) for n in nodes.values()],
        "edges": [asdict(e) for e in edges],
        "predicates": {p: d["meaning"] for p, d in vocab.predicates().items()},
        "types": {t: d["description"] for t, d in types.items()},
        "clusters": vocab.load_vocab().get("clusters", {}),
        "data_usage": _data_usage(settings),
    }


def _data_usage(settings: Settings) -> dict[str, dict[str, str]]:
    """KO ID -> {"model:Entity.field": count} from accepted record batches (counts under 5 shown as "<5")."""
    try:
        from .records import ko_usage
        from .records.store import small
    except Exception:  # the data skeleton is optional for the network
        return {}
    try:
        return {ko: {k: small(n) for k, n in fields.items()} for ko, fields in ko_usage(settings).items()}
    except Exception:
        return {}


# ---------------------------------------------------------------- views of the network

def neighbors(net: dict[str, Any], node_id: str) -> list[tuple[dict, dict, str]]:
    """(edge, other node, direction 'out'|'in') for every link touching node_id."""
    by_id = {n["id"]: n for n in net["nodes"]}
    out = []
    for e in net["edges"]:
        if e["source"] == node_id and e["target"] in by_id:
            out.append((e, by_id[e["target"]], "out"))
        elif e["target"] == node_id and e["source"] in by_id:
            out.append((e, by_id[e["source"]], "in"))
    return out


def journey(net: dict[str, Any], condition_id: str) -> list[dict[str, Any]]:
    """The knowledge journey for one condition: everything up to 2 links away, by stage.
    Paths don't pass through other conditions, so one condition's journey stays its own."""
    by_id = {n["id"]: n for n in net["nodes"]}
    found: dict[str, tuple[int, str]] = {}   # node id -> (hops, via)
    frontier = [condition_id]
    for hops in (1, 2):
        nxt = []
        for nid in frontier:
            for _e, other, _dir in neighbors(net, nid):
                oid = other["id"]
                if oid == condition_id or oid in found:
                    continue
                found[oid] = (hops, by_id[nid]["label"] if nid != condition_id else "")
                if other["ko_type"] != "Condition":
                    nxt.append(oid)
        frontier = nxt
    stages = []
    for key, title, ko_types in JOURNEY:
        items = sorted(({**by_id[i], "hops": h, "via": via} for i, (h, via) in found.items() if by_id[i]["ko_type"] in ko_types),
                       key=lambda n: (n["kind"] != "ko", n["hops"], n["label"].lower()))
        stages.append({"key": key, "title": title, "items": items})
    return stages


def insights(net: dict[str, Any]) -> dict[str, Any]:
    """Simple network analysis of the KO dataset (Kyle's 'apply data science to the KOs themselves')."""
    nodes, edges = net["nodes"], net["edges"]
    real = [e for e in edges if not e["proposed"]]
    degree: Counter[str] = Counter()
    for e in real:
        degree[e["source"]] += 1
        degree[e["target"]] += 1
    by_id = {n["id"]: n for n in nodes}
    kos = [n for n in nodes if n["kind"] == "ko"]
    proposed = sorted((n for n in nodes if n["kind"] == "proposed"), key=lambda n: (-len(n["proposed_by"]), n["label"]))
    used_predicates = Counter(e["predicate"] for e in real)
    stage_counts = []
    for _key, title, ko_types in JOURNEY:
        stage_counts.append({"title": title,
                             "written": sum(1 for n in kos if n["ko_type"] in ko_types),
                             "proposed": sum(1 for n in proposed if n["ko_type"] in ko_types)})
    statuses = Counter(n["status"] for n in kos)
    unsupported = [e for e in real if not e["source_ids"]]
    return {
        "counts": {"kos": len(kos), "links": len(real), "proposed_concepts": len(proposed),
                   "proposed_links": len(edges) - len(real),
                   "planned": sum(1 for n in nodes if n["kind"] == "planned"),
                   "predicates_used": len(used_predicates), "predicates_available": len(net["predicates"])},
        "most_connected": [{"id": i, "label": by_id[i]["label"], "ko_type": by_id[i]["ko_type"], "links": n}
                           for i, n in degree.most_common(6) if i in by_id],
        "unconnected": [n["label"] for n in kos if degree[n["id"]] == 0],
        "predicates": used_predicates.most_common(),
        "unused_predicates": [p for p in net["predicates"] if p not in used_predicates],
        "stages": stage_counts,
        "statuses": statuses.most_common(),
        "top_gaps": [{"label": n["label"], "ko_type": n["ko_type"], "proposed_by": n["proposed_by"]} for n in proposed[:8]],
        "merged": [n["label"] for n in proposed if len(n["proposed_by"]) > 1],
        "unsupported_links": len(unsupported),
        "planned_object_types": PLANNED_OBJECT_TYPES,
    }


def conditions(net: dict[str, Any]) -> list[dict[str, Any]]:
    return sorted((n for n in net["nodes"] if n["ko_type"] == "Condition" and n["kind"] == "ko"),
                  key=lambda n: n["label"].lower())


def by_type(net: dict[str, Any]) -> dict[str, list[dict]]:
    out: dict[str, list[dict]] = defaultdict(list)
    for n in net["nodes"]:
        out[n["ko_type"]].append(n)
    return out
