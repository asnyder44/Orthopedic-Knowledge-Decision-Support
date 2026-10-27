"""Scope guard: spot requests for personal diagnosis or treatment decisions.

This is a simple, transparent pattern list — not a classifier. Its recall is
measured by the experiment on `out_of_scope` questions; extend the patterns from
pilot logs, and have the reviewer check the notice wording.
"""

from __future__ import annotations

import re

_PERSONAL_ADVICE = [
    r"\bshould i\b",
    r"\bdo i (have|need)\b",
    r"\bam i\b",
    r"\b(my|the) (dose|dosage)\b",
    r"\bhow (much|many) .* (take|pills?)\b",
    r"\b(stop|start|keep) taking\b",
    r"\bis it safe for me\b",
    r"\bdiagnos(e|is) me\b",
    r"\bwhat('s| is) wrong with me\b",
]
_PATTERN = re.compile("|".join(_PERSONAL_ADVICE), re.I)

SCOPE_NOTICE = (
    "This tool explains general information from public sources. It can't tell you "
    "what is wrong or what you personally should do. Please ask your clinician — "
    "the suggested appointment questions may help."
)
EMERGENCY_NOTICE = (
    "If you have severe pain, a visibly deformed limb, numbness that comes on suddenly, "
    "or signs of infection, seek medical care now."
)


def needs_scope_notice(query: str) -> bool:
    return bool(_PATTERN.search(query))
