"""AI provider + OrthoBot RAG tests. Fake clients stand in for Claude and OpenAI, so no key or network is needed."""

from __future__ import annotations

import shutil
from types import SimpleNamespace

import pytest
from conftest import EXAMPLE

from okds import chatbot, llm
from okds.config import get_settings
from okds.ko import parse_ko

# ---------------------------------------------------------------- fakes


class FakeClaudeStream:
    def __init__(self, chunks, stop_reason):
        self.text_stream = iter(chunks)
        self._final = SimpleNamespace(
            stop_reason=stop_reason, model="claude-opus-5-5",
            content=[SimpleNamespace(type="text", text="".join(chunks))],
            usage=SimpleNamespace(input_tokens=100, output_tokens=20))

    def __enter__(self):
        return self

    def __exit__(self, *exc):
        return False

    def get_final_message(self):
        return self._final


class FakeClaude:
    def __init__(self, chunks=("The median nerve ", "is squeezed [1]."), stop_reason="end_turn"):
        self.calls = []
        outer = self

        class Messages:
            def stream(self, **kwargs):
                outer.calls.append(kwargs)
                return FakeClaudeStream(chunks, stop_reason)

        self.beta = SimpleNamespace(messages=Messages())


def _openai_chunk(text=None, finish=None, usage=None):
    choices = [] if text is None and finish is None else [
        SimpleNamespace(delta=SimpleNamespace(content=text), finish_reason=finish)]
    return SimpleNamespace(model="gpt-test", choices=choices, usage=usage)


class FakeOpenAI:
    def __init__(self, chunks=("The median nerve ", "is squeezed [1]."), finish="stop"):
        self.calls = []
        outer = self

        class Completions:
            def create(self, **kwargs):
                outer.calls.append(kwargs)
                parts = [_openai_chunk(t) for t in chunks]
                parts.append(_openai_chunk(finish=finish))
                parts.append(_openai_chunk(usage=SimpleNamespace(prompt_tokens=90, completion_tokens=12)))
                return iter(parts)

        self.chat = SimpleNamespace(completions=Completions())


@pytest.fixture
def index(example_text):
    return chatbot.KOIndex([parse_ko(example_text)])


# ---------------------------------------------------------------- provider choice


def test_provider_auto_detects_from_keys(data_dir, monkeypatch):
    assert get_settings().ai_provider == "none" and not get_settings().ai_ready
    monkeypatch.setenv("OPENAI_API_KEY", "sk-test")
    s = get_settings()
    assert (s.ai_provider, s.ai_label, s.ai_model) == ("openai", "OpenAI", "gpt-6.1-sol")
    monkeypatch.setenv("ANTHROPIC_API_KEY", "sk-ant-test")
    monkeypatch.delenv("OKDS_MODEL", raising=False)
    assert (get_settings().ai_provider, get_settings().ai_model) == ("claude", "claude-sonnet-5-5")  # Claude wins
    monkeypatch.setenv("OKDS_AI_PROVIDER", "openai")
    assert get_settings().ai_provider == "openai"
    monkeypatch.setenv("OPENAI_BASE_URL", "http://127.0.0.1:11434/v1")
    assert get_settings().ai_label == "Local model"


def test_chosen_provider_without_key_is_off(data_dir, monkeypatch):
    monkeypatch.setenv("OPENAI_API_KEY", "sk-test")
    monkeypatch.setenv("OKDS_AI_PROVIDER", "claude")
    assert get_settings().ai_provider == "none"


def test_no_provider_raises_friendly_error():
    with pytest.raises(llm.LLMError, match="AI is off"):
        list(llm.stream_text(provider="none", model="x", system="s", user="u", effort="low", result=llm.StreamResult()))


# ---------------------------------------------------------------- llm streaming


def test_claude_stream_sends_no_sampling_params(monkeypatch):
    fake = FakeClaude()
    monkeypatch.setattr(llm, "make_client", lambda: fake)
    result = llm.StreamResult()
    text = "".join(llm.stream_text(provider="claude", model="claude-opus-5-5", system="s", user="u",
                                   effort="medium", result=result))
    assert text == result.text == "The median nerve is squeezed [1]."
    call = fake.calls[0]
    assert call["output_config"] == {"effort": "medium"} and call["fallbacks"] == "default"
    assert not {"temperature", "top_p", "top_k"} & call.keys()
    assert result.usage["output_tokens"] == 20


def test_claude_refusal_and_missing_credentials(monkeypatch):
    monkeypatch.setattr(llm, "make_client", lambda: FakeClaude(stop_reason="refusal"))
    with pytest.raises(llm.LLMError, match="declined"):
        list(llm.stream_text(model="m", system="s", user="u", effort="low", result=llm.StreamResult()))

    def no_creds():
        raise TypeError("Could not resolve authentication method. Expected api_key")

    monkeypatch.setattr(llm, "make_client", no_creds)
    with pytest.raises(llm.LLMError, match="ANTHROPIC_API_KEY"):
        list(llm.stream_text(model="m", system="s", user="u", effort="low", result=llm.StreamResult()))


def test_openai_stream(monkeypatch):
    fake = FakeOpenAI()
    monkeypatch.setattr(llm, "make_openai_client", lambda: fake)
    result = llm.StreamResult()
    text = "".join(llm.stream_text(provider="openai", model="gpt-test", system="s", user="u",
                                   effort="medium", result=result))
    assert text == "The median nerve is squeezed [1]."
    assert result.stop_reason == "end_turn" and result.usage == {"input_tokens": 90, "output_tokens": 12}
    call = fake.calls[0]
    assert call["messages"][0] == {"role": "system", "content": "s"} and call["stream"] is True
    assert "temperature" not in call


def test_openai_content_filter_and_missing_key(monkeypatch):
    real_client = llm.make_openai_client
    monkeypatch.setattr(llm, "make_openai_client", lambda: FakeOpenAI(finish="content_filter"))
    with pytest.raises(llm.LLMError, match="declined"):
        list(llm.stream_text(provider="openai", model="m", system="s", user="u", effort="low", result=llm.StreamResult()))
    monkeypatch.delenv("OPENAI_API_KEY", raising=False)
    monkeypatch.setattr(llm, "make_openai_client", real_client)
    with pytest.raises(llm.LLMError, match="OPENAI_API_KEY"):
        list(llm.stream_text(provider="openai", model="m", system="s", user="u", effort="low", result=llm.StreamResult()))


# ---------------------------------------------------------------- OrthoBot RAG


def test_tokenize_folds_unicode_dashes_and_possessives():
    assert chatbot.tokenize("Phalen’s test") == ["phalen", "test"]
    assert "ray" in chatbot.tokenize("an X‑ray")


def test_long_sections_are_split_with_overlap():
    text = "\n".join(f"Line {i} " + "word " * 30 for i in range(20))
    parts = chatbot._windows(text)
    assert len(parts) > 1 and all(len(p.split()) <= chatbot.MAX_WORDS + 40 for p in parts)
    assert parts[0].splitlines()[-1].strip() == parts[1].splitlines()[0].strip()  # overlap


@pytest.mark.parametrize("provider,attr,fake", [("claude", "make_client", FakeClaude),
                                                ("openai", "make_openai_client", FakeOpenAI)])
def test_ai_answer_cites_passages(data_dir, monkeypatch, index, provider, attr, fake):
    monkeypatch.setenv("ANTHROPIC_API_KEY" if provider == "claude" else "OPENAI_API_KEY", "test")
    client = fake()
    monkeypatch.setattr(llm, attr, lambda: client)
    ans = chatbot.answer_with_ai("Which nerve is squeezed in carpal tunnel syndrome?", index, get_settings())
    assert ans.text.endswith("[1].") and [c["n"] for c in ans.citations] == [1]
    assert ans.citations[0]["ko_id"] == "KO-HAND-COND-001"
    sent = client.calls[0]
    user = sent["messages"][-1]["content"]
    assert user.startswith('Sources:\n\n<passage n="1">\n[1] ') and "Question: Which nerve" in user


def test_unrelated_question_skips_the_ai(data_dir, monkeypatch, index):
    monkeypatch.setenv("ANTHROPIC_API_KEY", "test")
    client = FakeClaude()
    monkeypatch.setattr(llm, "make_client", lambda: client)
    ans = chatbot.answer_with_ai("rotator cuff shoulder surgery", index, get_settings())
    assert ans.text == chatbot.NO_ANSWER and ans.suggestions and not client.calls


def test_model_no_answer_drops_citations(index):
    r = chatbot.retrieve("Which nerve is squeezed in carpal tunnel syndrome?", index)
    ans = chatbot.finish_ai_answer(chatbot.NO_ANSWER + " It covers carpal tunnel syndrome [1].", r, index)
    assert not ans.citations and ans.suggestions


def test_cited_numbers_ignores_out_of_range():
    assert chatbot.cited_numbers("a [2] b [1][2] c [9]", 3) == [2, 1]


def test_semantic_falls_back_to_keyword(index):
    assert index.resolve_method("hybrid")[0] == "keyword"
    with pytest.raises(ValueError):
        index.resolve_method("magic")


def test_orthobot_page_ai_answer(client, data_dir, monkeypatch):
    import json

    (data_dir / "kos" / "hand").mkdir(parents=True)
    shutil.copy(EXAMPLE, data_dir / "kos" / "hand" / EXAMPLE.name)
    monkeypatch.setenv("ANTHROPIC_API_KEY", "test")
    monkeypatch.setattr(llm, "make_client", lambda: FakeClaude())
    html = client.get("/ko/orthobot").get_data(as_text=True)
    assert 'value="ai" checked' in html and "AI answer (Claude)" in html
    r = client.post("/ko/api/ask", json={"question": "Which nerve is squeezed in carpal tunnel syndrome?", "mode": "ai"})
    items = [json.loads(line) for line in r.get_data(as_text=True).splitlines() if line.strip()]
    ans = items[-1]["answer"]
    assert ans["citations"] and ans["citations"][0]["sources"]
    assert ans["meta"].startswith("AI answer (Claude")


def test_starter_questions_come_from_test_questions(example_text):
    qs = chatbot.starter_questions([parse_ko(example_text)])
    assert qs == ["Which nerve is affected in CTS?"]


def test_small_talk_and_follow_ups(index):
    assert chatbot.small_talk("Hello!", index).mode == "chat"
    assert "Carpal Tunnel Syndrome" in chatbot.small_talk("help", index).text
    assert chatbot.small_talk("What is CTS?", index) is None


def test_quick_answer_cites_sentences(index):
    ans = chatbot.answer_retrieval_only("Which nerve is squeezed in carpal tunnel syndrome?", index)
    assert ans.text.startswith("Here's what I found") and "[S" not in ans.text
    assert ans.citations and all(c["quote"] for c in ans.citations) and ans.passages_read >= len(ans.citations)


def test_word_endings_fold_together():
    assert chatbot.tokenize("treated treatment treating") == ["treat"] * 3
