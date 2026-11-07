import json

import pytest

from okds import chatbot, generator, registry, vocab
from okds.config import get_settings
from okds.fetch import FetchError, fetch_page
from okds.ko import parse_ko, render_ko
from okds.storage import LocalKOStore
from okds.validator import validate_text


def test_vocab_loads_and_clusters_follow_rule():
    assert vocab.cluster_for("Condition") == 2
    assert vocab.type_code("DiagnosticTest") == "DX"
    assert vocab.predicate_allows("DIAGNOSED_BY", "Condition", "DiagnosticTest") is True
    assert vocab.predicate_allows("DIAGNOSED_BY", "Treatment", "DiagnosticTest") is False
    assert vocab.predicate_allows("CONTRASTS_WITH", "Condition", "Procedure") is False


def test_registry_assigns_next_id_and_blocks_duplicates(data_dir):
    path = get_settings().registry_path  # a copy of the real registry, which grows over time
    before = registry.load_registry(path)
    expected = registry.next_id(before, "HAND", "Condition")
    c = registry.add_concept(path, "Test Zebra Finger", "Condition", "HAND", ["zebra digit"])
    assert c.ko_id == expected and expected not in before
    with pytest.raises(ValueError):
        registry.add_concept(path, "test zebra finger", "Condition", "HAND")
    with pytest.raises(ValueError):
        registry.add_concept(path, "CTS", "Condition", "HAND")  # alternate term of KO-HAND-COND-001
    assert registry.next_id(registry.load_registry(path), "JOINT", "Procedure") == "KO-JOINT-PROC-001"


def test_example_ko_is_valid(data_dir, example_text):
    result = validate_text(example_text, registry.load_registry(get_settings().registry_path))
    assert result.ok, [i.message for i in result.errors]
    assert any(i.check == "14 open values" for i in result.warnings)


def test_round_trip_keeps_content(example_text):
    doc = parse_ko(example_text)
    again = parse_ko(render_ko(doc))
    assert again.front == doc.front
    assert again.body == doc.body


@pytest.mark.parametrize("mutate, check", [
    (lambda t: t.replace("cluster: 2", "cluster: 5"), "5 cluster"),
    (lambda t: t.replace("predicate: DIAGNOSED_BY", "predicate: RELATED_TO"), "7 forbidden link"),
    (lambda t: t.replace("target_id: KO-HAND-DX-001", "target_id: KO-HAND-DX-099"), "6 links"),
    (lambda t: t.replace("Symptoms are often worse at night [S3].", "Symptoms are often worse at night."), "8 source markers"),
    (lambda t: t.replace("[S3]", "[S9]"), "8 source markers"),
    (lambda t: t.replace("### When to seek care", "### Other"), "11 headings"),
    (lambda t: t.replace("status: draft", "status: published"), "13 review status"),
    (lambda t: t.replace("permitted_use: link_and_paraphrase", "permitted_use: restricted", 1), "10 permitted use"),
])
def test_validator_catches_problems(data_dir, example_text, mutate, check):
    result = validate_text(mutate(example_text), registry.load_registry(get_settings().registry_path))
    assert not result.ok
    assert any(i.check == check for i in result.errors), [(i.check, i.message) for i in result.errors]


def test_plain_english_related_to_is_not_an_error(data_dir, example_text):
    text = example_text.replace("Many things can add pressure", "Problems related to the wrist can add pressure")
    assert validate_text(text, registry.load_registry(get_settings().registry_path)).ok


def _request(data_dir, n_sources=2):
    concept = registry.load_registry(get_settings().registry_path)["KO-HAND-DX-001"]
    sources = [{"id": f"S{i}", "title": f"Page {i}", "publisher": "NIH", "url": f"https://example.org/{i}",
                "source_type": "government_health_page", "audience": "patient", "publication_date": "<verify>",
                "retrieved_date": "2026-10-24", "permitted_use": "public_domain", "text": "Some source text."}
               for i in range(1, n_sources + 1)]
    return generator.KORequest(concept=concept, audience=["patient"], reading_level="grade 6-8",
                               difficulty="beginner", sources=sources, author="Tester")


def test_template_draft_has_structure_but_needs_content(data_dir):
    req = _request(data_dir)
    md = generator.template_draft(req)
    doc = parse_ko(md)
    assert doc.front["ko_id"] == "KO-HAND-DX-001" and doc.front["cluster"] == 3
    assert "text" not in doc.front["sources"][0]  # pack text stays in the source pack
    result = validate_text(md, registry.load_registry(get_settings().registry_path))
    checks = {i.check for i in result.errors}
    assert "11 headings" not in checks  # every required heading is there
    assert "8 source markers" in checks  # but the TODOs still need sourced content


def test_finalize_restores_script_owned_fields(data_dir):
    req = _request(data_dir)
    fake = generator.template_draft(req)
    fake = (fake.replace("ko_id: KO-HAND-DX-001", "ko_id: KO-HAND-DX-777")
                .replace("status: draft", "status: published")
                .replace("cluster: 3", "cluster: 7"))
    md, notes = generator.finalize(f"```markdown\n{fake}\n```", req, "claude-opus-5-5")
    front = parse_ko(md).front
    assert front["ko_id"] == "KO-HAND-DX-001"
    assert front["review"]["status"] == "draft"
    assert front["cluster"] == 3
    assert front["review"]["generated_by"] == {"model": "claude-opus-5-5", "prompt_version": "okds-gen-1.1"}
    assert len(notes) == 2


def test_finalize_passes_through_source_pack_needed(data_dir):
    md, notes = generator.finalize("SOURCE PACK NEEDED\nMissing: x", _request(data_dir), "m")
    assert md.startswith("SOURCE PACK NEEDED") and notes


def test_check_pack_needs_two_sources_with_text(data_dir):
    assert generator.check_pack(_request(data_dir, 1))
    assert not generator.check_pack(_request(data_dir, 2))


def test_store_saves_markdown_json_and_pack(data_dir, example_text):
    store = LocalKOStore(get_settings())
    saved = store.save(parse_ko(example_text), source_pack="# pack")
    assert saved.markdown_path == "kos/hand/KO-HAND-COND-001_carpal-tunnel-syndrome.md"
    record = json.loads((data_dir / saved.json_path).read_text(encoding="utf-8"))
    assert record["ko_id"] == "KO-HAND-COND-001"
    assert "what_it_is" in record["sections"]["explanation"]["subsections"]
    assert (data_dir / "sources" / "packs" / "SP-KO-HAND-COND-001.md").is_file()
    assert [e.ko_id for e in store.list_entries()] == ["KO-HAND-COND-001"]


def test_orthobot_retrieval_and_no_answer(example_text):
    index = chatbot.KOIndex([parse_ko(example_text)])
    hits = index.search("Which nerve is squeezed in carpal tunnel syndrome?")
    assert hits and hits[0].chunk.ko_id == "KO-HAND-COND-001"
    ans = chatbot.answer_retrieval_only("Which nerve is squeezed in carpal tunnel syndrome?", index)
    assert ans.citations and ans.citations[0]["sources"]
    assert chatbot.answer_retrieval_only("rotator cuff shoulder surgery", index).text == chatbot.NO_ANSWER


@pytest.mark.parametrize("url", ["file:///etc/passwd", "http://127.0.0.1:8501/", "http://localhost/", "ftp://x.org"])
def test_fetch_blocks_local_and_non_web_addresses(url):
    with pytest.raises(FetchError):
        fetch_page(url)


def test_content_demote_keeps_code_blocks():
    from okds import web as content
    md = "# Title\n## Sub\n```\n# not a heading\n```\ntext"
    out = content.demote(content.without_title(md), 2)
    assert out.startswith("#### Sub") and "\n# not a heading\n" in out
    for name in ("knowledge-objects.md", "ko-generator-prompt.md"):
        assert content.load_content(name).startswith("# ")


def test_article_is_an_exact_copy_of_the_original():
    """The Full article must be the user's knowledge-objects.md, unchanged (checksum of the original, 2026-11-01)."""
    import hashlib

    from okds import web as content
    digest = hashlib.sha256((content.CONTENT_DIR / "knowledge-objects.md").read_bytes()).hexdigest()
    original = "f423e05c33d4d72e6ba62bbf684792e56ca2fd7b0db3c22e322a671666e75e44"
    assert digest == original, "The article was changed. Copy the original knowledge-objects.md again."


def test_robot_check_text_is_caught(data_dir):
    from okds.fetch import looks_like_bot_check

    junk = "Checking your browser - reCAPTCHA\nPlease wait while we verify your browser."
    assert looks_like_bot_check(junk)
    assert not looks_like_bot_check("Carpal tunnel syndrome is pressure on the median nerve. " * 60 + "reCAPTCHA")
    concept = registry.load_registry(data_dir / "registry.csv")["KO-HAND-COND-001"]
    src = {"url": "https://example.org", "publisher": "P", "title": "T"}
    req = generator.KORequest(concept, ["patient"], "grade 8", "intro",
                              [{**src, "id": "S1", "text": junk}, {**src, "id": "S2", "text": "Real text."}], "me")
    assert any("robot-check" in p for p in generator.check_pack(req))


def test_cli_validate_relative_path_is_not_a_duplicate(data_dir, example_text, monkeypatch, capsys):
    from okds import cli

    (data_dir / "kos" / "hand").mkdir(parents=True)
    (data_dir / "kos" / "hand" / "ko.md").write_text(example_text, encoding="utf-8")
    monkeypatch.chdir(data_dir)
    assert cli.main(["validate", "kos/hand/ko.md"]) == 0
    assert "unique ID" not in capsys.readouterr().out
