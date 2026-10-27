from orthoinfo.text import html_to_lines, split_sections, strip_html, tokenize

SUMMARY = (
    'What is <span class="qt0">carpal</span> tunnel syndrome?<p>A nerve in your wrist\n'
    "becomes squeezed.</p>What causes it?<p>Causes include :</p><ul><li>Injury</li>"
    "<li>Diabetes &amp; arthritis</li></ul>"
)


def test_strip_html_removes_highlighting():
    assert strip_html('<span class="qt0">Carpal</span> Tunnel') == "Carpal Tunnel"


def test_html_to_lines_keeps_structure_and_joins_wrapped_text():
    assert html_to_lines(SUMMARY) == [
        "What is carpal tunnel syndrome?",
        "A nerve in your wrist becomes squeezed.",
        "What causes it?",
        "Causes include:",
        "- Injury",
        "- Diabetes & arthritis",
    ]


def test_split_sections_uses_question_headings():
    sections = split_sections(html_to_lines(SUMMARY), "About")
    assert [s["heading"] for s in sections] == ["What is carpal tunnel syndrome?", "What causes it?"]
    assert "- Injury" in sections[1]["text"]


def test_split_sections_default_heading_when_none():
    sections = split_sections(["Plain text."], "About X")
    assert sections == [{"heading": "About X", "text": "Plain text."}]


def test_tokenize_drops_stopwords_and_plurals():
    assert tokenize("Why do my Fingers hurt?") == ["finger", "hurt"]
    assert tokenize("injuries") == ["injury"]
