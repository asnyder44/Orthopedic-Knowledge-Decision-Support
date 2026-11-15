"""Where the KO pipeline keeps its work. Local files now; S3 later (same functions).

data/pipeline/
  articles/<KO-ID>/<PMCID>.md   article inbox: front matter (status new | used | skipped) + trimmed text
  articles/<KO-ID>/UP-<id>.md   documents people uploaded (same format; checked the same way)
  queue/<KO-ID>.md              KOs waiting for review (+ SP-<KO-ID>.md source pack, <KO-ID>.json notes)
  rejected/<KO-ID>_<time>.md    rejected KOs (kept for learning)
  runs.jsonl                    one line per job run (what happened, tokens, cost)
  decisions.jsonl               one line per accept / reject
  .lock                         stops two runs at the same time
"""

from __future__ import annotations

import datetime as dt
import json
import os
import re
import time
from collections.abc import Iterator
from contextlib import contextmanager
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

import yaml

from ..config import Settings
from ..ko import KODocument, KOFormatError, as_dict, parse_ko, render_ko
from ..storage import check_ko_id

LOCK_STALE_SECONDS = 2 * 60 * 60
UPLOAD_ID_RE = re.compile(r"UP-[0-9a-f]{12}")


def now_iso() -> str:
    return dt.datetime.now().replace(microsecond=0).isoformat()


class PipelineBusy(RuntimeError):
    pass


@dataclass
class Article:
    meta: dict[str, Any]
    text: str
    path: Path | None = None

    @property
    def pmcid(self) -> str:
        return str(self.meta.get("article_id", ""))

    @property
    def topic_id(self) -> str:
        return str(self.meta.get("topic_id", ""))

    @property
    def status(self) -> str:
        return str(self.meta.get("status", "new"))


@dataclass
class QueueItem:
    ko_id: str
    path: Path
    doc: KODocument | None
    notes: dict[str, Any] = field(default_factory=dict)
    error: str | None = None

    @property
    def text(self) -> str:
        return self.path.read_text(encoding="utf-8")


class PipelineStore:
    def __init__(self, settings: Settings):
        self.s = settings
        self.root = settings.pipeline_dir
        self.articles_dir = self.root / "articles"
        self.queue_dir = self.root / "queue"
        self.rejected_dir = self.root / "rejected"
        for d in (self.articles_dir, self.queue_dir, self.rejected_dir):
            d.mkdir(parents=True, exist_ok=True)

    # ------------------------------------------------------------ lock
    @contextmanager
    def lock(self) -> Iterator[None]:
        path = self.root / ".lock"
        if path.is_file() and time.time() - path.stat().st_mtime >= LOCK_STALE_SECONDS:
            path.unlink(missing_ok=True)  # a run that crashed long ago
        stamp = f"{os.getpid()} {now_iso()}"
        if hasattr(path, "create_exclusive"):  # S3: an atomic "create only if missing" write
            if not path.create_exclusive(stamp):
                raise PipelineBusy("Another pipeline run is still working. Try again in a few minutes.")
        elif path.exists():
            raise PipelineBusy("Another pipeline run is still working. Try again in a few minutes.")
        else:
            path.write_text(stamp, encoding="utf-8")
        try:
            yield
        finally:
            path.unlink(missing_ok=True)

    # ------------------------------------------------------------ articles
    def _article_path(self, topic_id: str, pmcid: str) -> Path:
        check_ko_id(topic_id)
        if not (pmcid.startswith("PMC") and pmcid[3:].isdigit()) and not UPLOAD_ID_RE.fullmatch(pmcid):
            raise ValueError(f"Bad article ID: {pmcid}")
        return self.articles_dir / topic_id / f"{pmcid}.md"

    def save_article(self, a: Article) -> Path:
        path = self._article_path(a.topic_id, a.pmcid)
        path.parent.mkdir(parents=True, exist_ok=True)
        front = yaml.safe_dump(a.meta, sort_keys=False, allow_unicode=True, width=100)
        path.write_text(f"---\n{front}---\n\n{a.text.strip()}\n", encoding="utf-8", newline="\n")
        a.path = path
        return path

    def articles(self, topic_id: str | None = None, status: str | None = None) -> list[Article]:
        out = []
        for path in sorted(self.articles_dir.glob(f"{topic_id or '*'}/*.md")):
            try:
                raw = path.read_text(encoding="utf-8")
                _, front, body = raw.split("---", 2)
                meta = yaml.safe_load(front) or {}
            except (ValueError, yaml.YAMLError):
                continue
            a = Article(meta if isinstance(meta, dict) else {}, body.strip(), path)
            if status is None or a.status == status:
                out.append(a)
        return out

    def seen_ids(self) -> set[str]:
        return {a.pmcid for a in self.articles()}

    def mark_articles(self, articles: list[Article], status: str, **extra: Any) -> None:
        for a in articles:
            a.meta["status"] = status
            a.meta.update(extra)
            self.save_article(a)

    # ------------------------------------------------------------ review queue
    def queue_items(self) -> list[QueueItem]:
        items = []
        for path in sorted(self.queue_dir.glob("KO-*.md")):
            ko_id = path.stem
            notes_path = self.queue_dir / f"{ko_id}.json"
            notes = json.loads(notes_path.read_text(encoding="utf-8")) if notes_path.is_file() else {}
            try:
                items.append(QueueItem(ko_id, path, parse_ko(path.read_text(encoding="utf-8")), notes))
            except KOFormatError as e:
                items.append(QueueItem(ko_id, path, None, notes, str(e)))
        return items

    def in_queue(self, ko_id: str) -> bool:
        return (self.queue_dir / f"{ko_id}.md").is_file()

    def add_to_queue(self, ko_id: str, markdown: str, source_pack: str, notes: dict[str, Any]) -> Path:
        check_ko_id(ko_id)
        path = self.queue_dir / f"{ko_id}.md"
        path.write_text(markdown, encoding="utf-8", newline="\n")
        (self.queue_dir / f"SP-{ko_id}.md").write_text(source_pack, encoding="utf-8", newline="\n")
        (self.queue_dir / f"{ko_id}.json").write_text(json.dumps(notes, indent=2, ensure_ascii=False), encoding="utf-8")
        return path

    def update_queue_text(self, ko_id: str, markdown: str) -> None:
        check_ko_id(ko_id)
        (self.queue_dir / f"{ko_id}.md").write_text(markdown, encoding="utf-8", newline="\n")

    def source_pack(self, ko_id: str) -> str | None:
        path = self.queue_dir / f"SP-{ko_id}.md"
        return path.read_text(encoding="utf-8") if path.is_file() else None

    def remove_from_queue(self, ko_id: str) -> None:
        check_ko_id(ko_id)
        for name in (f"{ko_id}.md", f"SP-{ko_id}.md", f"{ko_id}.json"):
            (self.queue_dir / name).unlink(missing_ok=True)

    def reject(self, ko_id: str, reviewer: str, reason: str) -> Path:
        check_ko_id(ko_id)
        stamp = dt.datetime.now().strftime("%Y%m%d-%H%M%S")
        target = self.rejected_dir / f"{ko_id}_{stamp}.md"
        target.write_text((self.queue_dir / f"{ko_id}.md").read_text(encoding="utf-8"), encoding="utf-8")
        self.log_decision({"ko_id": ko_id, "decision": "rejected", "reviewer": reviewer, "reason": reason,
                           "file": f"rejected/{target.name}"})
        self.remove_from_queue(ko_id)
        return target

    # ------------------------------------------------------------ logs
    def log_run(self, record: dict[str, Any]) -> None:
        with (self.root / "runs.jsonl").open("a", encoding="utf-8") as f:
            f.write(json.dumps(record, ensure_ascii=False) + "\n")

    def runs(self, limit: int = 20) -> list[dict[str, Any]]:
        path = self.root / "runs.jsonl"
        if not path.is_file():
            return []
        lines = path.read_text(encoding="utf-8").splitlines()[-limit:]
        return [json.loads(line) for line in reversed(lines) if line.strip()]

    def log_decision(self, record: dict[str, Any]) -> None:
        with (self.root / "decisions.jsonl").open("a", encoding="utf-8") as f:
            f.write(json.dumps({"time": now_iso(), **record}, ensure_ascii=False) + "\n")

    def decisions(self, limit: int = 50) -> list[dict[str, Any]]:
        path = self.root / "decisions.jsonl"
        if not path.is_file():
            return []
        lines = path.read_text(encoding="utf-8").splitlines()[-limit:]
        return [json.loads(line) for line in reversed(lines) if line.strip()]


def mark_accepted(doc: KODocument, reviewer: str) -> KODocument:
    """The reviewer's acceptance: status team_checked with their name (the validator requires it)."""
    front = dict(doc.front)
    review = dict(as_dict(front.get("review")))
    review.update({"status": "team_checked", "team_checker": reviewer, "review_date": dt.date.today().isoformat()})
    front["review"] = review
    log = list(front.get("change_log") or [])
    log.append({"version": str(front.get("version", "0.1.0")), "date": dt.date.today().isoformat(), "by": reviewer,
                "change": "Accepted in the KO pipeline review queue (team checked)."})
    front["change_log"] = log
    front["last_updated"] = dt.date.today().isoformat()
    return KODocument(front=front, body=doc.body)


__all__ = ["Article", "PipelineBusy", "PipelineStore", "QueueItem", "mark_accepted", "now_iso", "render_ko"]
