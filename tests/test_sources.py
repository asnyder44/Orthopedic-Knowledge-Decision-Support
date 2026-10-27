from orthoinfo.search import BM25Retriever
from orthoinfo.sources.europepmc import parse_jats
from orthoinfo.sources.wikipedia import _sections as wiki_sections
from orthoinfo.text import chunk_text, html_sections

JATS = b"""<article xmlns:xlink="http://www.w3.org/1999/xlink"><front>
<journal-meta><journal-title-group><journal-title>J Hand Surg</journal-title></journal-title-group></journal-meta>
<article-meta><article-id pub-id-type="doi">10.1/x</article-id>
<title-group><article-title>Splinting for <italic>carpal</italic> tunnel</article-title></title-group>
<contrib-group><contrib contrib-type="author"><name><surname>Lee</surname><given-names>A</given-names></name></contrib></contrib-group>
<pub-date><year>2021</year></pub-date>
<permissions><license xlink:href="https://creativecommons.org/licenses/by/4.0/"><license-p>CC BY</license-p></license></permissions>
<abstract><p>Splints help.</p></abstract></article-meta></front>
<body><sec><title>Methods</title><p>We reviewed trials.</p>
<sec><title>Search</title><p>Five databases.</p></sec></sec>
<sec><title>Funding</title><p>None.</p></sec></body></article>"""


def test_parse_jats_extracts_metadata_and_sections():
    art = parse_jats(JATS)
    assert art["title"] == "Splinting for carpal tunnel"
    assert art["journal"] == "J Hand Surg" and art["year"] == "2021" and art["doi"] == "10.1/x"
    assert art["authors"] == ["A Lee"]
    assert "creativecommons.org/licenses/by" in art["license_text"]
    headings = [s["heading"] for s in art["sections"]]
    assert headings == ["Abstract", "Methods", "Methods — Search"]  # Funding skipped


def test_html_sections_split_at_headings():
    html = "<p>Intro.</p><h2>Symptoms</h2><p>Pain.</p><ul><li>Swelling</li></ul><h3>Causes</h3><p>Injury.</p>"
    assert html_sections(html, "Topic") == [
        {"heading": "Topic", "text": "Intro."},
        {"heading": "Symptoms", "text": "Pain.\n- Swelling"},
        {"heading": "Causes", "text": "Injury."},
    ]


def test_chunk_text_respects_word_limit():
    text = " ".join(f"Sentence {i} is here." for i in range(100))  # 400 words, one line
    chunks = chunk_text(text, max_words=50)
    assert len(chunks) > 1 and all(len(c.split()) <= 50 for c in chunks)
    assert " ".join(chunks).replace("\n", " ") == text


def test_wikipedia_sections_drop_reference_sections():
    extract = "Lead text.\n== Signs ==\nNumbness.\n== References ==\nRef 1\n=== Sub ===\nRef 2"
    assert wiki_sections(extract, "CTS") == [
        {"heading": "CTS", "text": "Lead text."},
        {"heading": "Signs", "text": "Numbness."},
    ]


def test_bm25_source_type_filter():
    chunks = [
        {"chunk_id": "a#0", "doc_id": "a", "title": "Carpal tunnel", "heading": "x", "text": "numb fingers",
         "source_type": "patient_education"},
        {"chunk_id": "b#0", "doc_id": "b", "title": "Carpal tunnel trial", "heading": "x",
         "text": "numb fingers numb fingers", "source_type": "research_article"},
    ]
    bm25 = BM25Retriever(chunks)
    assert set(bm25.search("numb fingers").ranked_doc_ids()) == {"a", "b"}
    assert bm25.search("numb fingers", source_types=["patient_education"]).ranked_doc_ids() == ["a"]
