"""HTML cleaning, sectioning, chunking and tokenization."""

from __future__ import annotations

import html
import re

_SPAN = re.compile(r"</?span[^>]*>", re.I)
_LI = re.compile(r"<li[^>]*>", re.I)
_BLOCK = re.compile(r"</?(p|ul|ol|div|section|header|h\d|table|tr|dd|dt|blockquote)[^>]*>|</li>|<br\s*/?>", re.I)
_TAG = re.compile(r"<[^>]+>")
_WS = re.compile(r"\s+")
_NOISE = re.compile(r"<(script|style|nav|figure|noscript|svg|button|form)\b.*?</\1>", re.I | re.S)
_HEADING = re.compile(r"(<h([2-4])\b[^>]*>.*?</h\2>)", re.I | re.S)
_SENTENCE = re.compile(r"(?<=[.!?])\s+(?=[A-Z0-9\"(])")


def strip_html(fragment: str) -> str:
    """Plain text with search-hit highlighting removed (used for titles)."""
    text = _TAG.sub("", _SPAN.sub("", fragment))
    return _WS.sub(" ", html.unescape(text)).strip()


def html_to_lines(fragment: str) -> list[str]:
    """Convert an HTML fragment to lines; list items start with '- '."""
    # Raw newlines in the source are formatting only; structure comes from tags.
    s = _WS.sub(" ", _SPAN.sub("", _NOISE.sub(" ", fragment)))
    s = _LI.sub("\n- ", s)
    s = _BLOCK.sub("\n", s)
    s = html.unescape(_TAG.sub("", s)).replace("\xa0", " ")
    lines = (re.sub(r"\s+([:;,.])", r"\1", _WS.sub(" ", line)).strip() for line in s.split("\n"))
    return [line for line in lines if line and line != "-"]


def is_heading(line: str) -> bool:
    # MedlinePlus summaries use question-style subheadings ("What causes X?").
    return not line.startswith("- ") and line.endswith("?") and len(line) <= 120


def split_sections(lines: list[str], default_heading: str) -> list[dict]:
    """Group lines under question-style headings (MedlinePlus summaries)."""
    sections: list[dict] = []
    heading, buf = default_heading, []
    for line in lines:
        if is_heading(line):
            if buf:
                sections.append({"heading": heading, "text": "\n".join(buf)})
            heading, buf = line, []
        else:
            buf.append(line)
    if buf:
        sections.append({"heading": heading, "text": "\n".join(buf)})
    return sections


def html_sections(fragment: str, default_heading: str) -> list[dict]:
    """Split HTML into sections at <h2>-<h4> tags."""
    fragment = _NOISE.sub(" ", fragment)
    sections: list[dict] = []
    heading, start = default_heading, 0

    def add(body: str) -> None:
        lines = html_to_lines(body)
        if lines:
            sections.append({"heading": heading, "text": "\n".join(lines)})

    for match in _HEADING.finditer(fragment):
        add(fragment[start:match.start()])
        heading = strip_html(match.group(1)) or heading
        start = match.end()
    add(fragment[start:])
    return sections


def chunk_text(text: str, max_words: int = 220) -> list[str]:
    """Split text into pieces of about `max_words`, at line then sentence boundaries."""
    units: list[str] = []
    for line in text.split("\n"):
        if len(line.split()) <= max_words:
            units.append(line)
        else:
            units.extend(_SENTENCE.split(line))
    chunks, buf, count = [], [], 0
    for unit in units:
        n = len(unit.split())
        if buf and count + n > max_words:
            chunks.append("\n".join(buf))
            buf, count = [], 0
        buf.append(unit)
        count += n
    if buf:
        chunks.append("\n".join(buf))
    return chunks


STOPWORDS = frozenset(
    """a an and are as at be been but by can could do does did for from had has have how
    i if in into is it its me my of on or our should so that the their them then there
    these they this to was we were what when where which who why will with would you your
    about after before get got any also just than too very""".split()
)


def _stem(token: str) -> str:
    # Deliberately tiny: handles plurals so "fingers" matches "finger".
    if len(token) > 4 and token.endswith("ies"):
        return token[:-3] + "y"
    if len(token) > 3 and token.endswith("s") and not token.endswith(("ss", "us", "is")):
        return token[:-1]
    return token


def tokenize(text: str) -> list[str]:
    return [_stem(t) for t in re.findall(r"[a-z0-9]+", text.lower()) if t not in STOPWORDS]
