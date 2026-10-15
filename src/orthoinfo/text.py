"""HTML cleaning, sectioning and tokenization."""

from __future__ import annotations

import html
import re

_SPAN = re.compile(r"</?span[^>]*>", re.I)
_LI = re.compile(r"<li[^>]*>", re.I)
_BLOCK = re.compile(r"</?(p|ul|ol|div|h\d)[^>]*>|</li>|<br\s*/?>", re.I)
_TAG = re.compile(r"<[^>]+>")
_WS = re.compile(r"\s+")


def strip_html(fragment: str) -> str:
    """Plain text with search-hit highlighting removed (used for titles)."""
    text = _TAG.sub("", _SPAN.sub("", fragment))
    return _WS.sub(" ", html.unescape(text)).strip()


def html_to_lines(fragment: str) -> list[str]:
    """Convert a MedlinePlus summary to lines; list items start with '- '."""
    # Raw newlines in the source are formatting only; structure comes from tags.
    s = _WS.sub(" ", _SPAN.sub("", fragment))
    s = _LI.sub("\n- ", s)
    s = _BLOCK.sub("\n", s)
    s = html.unescape(_TAG.sub("", s))
    lines = (re.sub(r"\s+([:;,.])", r"\1", _WS.sub(" ", line)).strip() for line in s.split("\n"))
    return [line for line in lines if line and line != "-"]


def is_heading(line: str) -> bool:
    # MedlinePlus summaries use question-style subheadings ("What causes X?").
    return not line.startswith("- ") and line.endswith("?") and len(line) <= 120


def split_sections(lines: list[str], default_heading: str, max_words: int = 220) -> list[dict]:
    """Group lines under their headings; split very long sections."""
    sections: list[dict] = []
    heading, buf = default_heading, []

    def flush():
        chunk: list[str] = []
        for line in buf:
            chunk.append(line)
            if sum(len(x.split()) for x in chunk) >= max_words:
                sections.append({"heading": heading, "text": "\n".join(chunk)})
                chunk = []
        if chunk:
            sections.append({"heading": heading, "text": "\n".join(chunk)})

    for line in lines:
        if is_heading(line):
            flush()
            heading, buf = line, []
        else:
            buf.append(line)
    flush()
    return sections


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
