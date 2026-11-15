"""One small wrapper for the AI model, used by the KO Generator and OrthoBot.

Providers (pick with OKDS_AI_PROVIDER, or let it auto-detect from the keys in .env):
- claude: the Claude API (Anthropic Python SDK), needs ANTHROPIC_API_KEY.
- openai: the OpenAI API (ChatGPT models), needs OPENAI_API_KEY. The same code also talks to a
  local OpenAI-compatible server such as Ollama when OPENAI_BASE_URL points at it.
"""

from __future__ import annotations

from collections.abc import Iterator
from dataclasses import dataclass, field
from typing import Any

import anthropic

# On a safety-classifier decline, the API retries on Anthropic's recommended fallback model.
FALLBACK_BETA = "server-side-fallback-2026-07-01"


class LLMError(RuntimeError):
    pass


@dataclass
class StreamResult:
    """Collects the text and the end state after a streamed call finishes."""

    message: Any = None  # Claude's final message (None for OpenAI)
    chunks: list[str] = field(default_factory=list)
    finish: str | None = None  # stop reason in Claude terms: end_turn | max_tokens | refusal
    model: str | None = None
    usage: dict[str, Any] = field(default_factory=dict)

    @property
    def text(self) -> str:
        if self.message is None:
            return "".join(self.chunks)
        return "".join(b.text for b in self.message.content if b.type == "text")

    @property
    def stop_reason(self) -> str | None:
        return getattr(self.message, "stop_reason", None) or self.finish


def make_client() -> anthropic.Anthropic:
    # Credentials come from ANTHROPIC_API_KEY, ANTHROPIC_AUTH_TOKEN, or an `ant auth login` profile.
    return anthropic.Anthropic()


def make_openai_client() -> Any:
    import openai  # reads OPENAI_API_KEY and OPENAI_BASE_URL from the environment

    return openai.OpenAI()


# ---------------------------------------------------------------- errors

def describe_error(e: Exception) -> str:
    if isinstance(e, TypeError) and "authentication" in str(e).lower():
        return "No Claude credentials found. Set ANTHROPIC_API_KEY in your .env file (see .env.example)."
    if isinstance(e, anthropic.AuthenticationError):
        return "Claude API key is missing or invalid. Set ANTHROPIC_API_KEY in your .env file."
    if isinstance(e, anthropic.PermissionDeniedError):
        return "This API key cannot use the requested model."
    if isinstance(e, anthropic.NotFoundError):
        return "Model not found. Check OKDS_MODEL in your .env file."
    if isinstance(e, anthropic.RateLimitError):
        return "Rate limited by the Claude API. Wait a minute and try again."
    if isinstance(e, anthropic.BadRequestError):
        return f"The Claude API rejected the request: {e.message}"
    if isinstance(e, anthropic.APIStatusError):
        return f"Claude API error {e.status_code}: {e.message}"
    if isinstance(e, anthropic.APIConnectionError):
        return "Could not reach the Claude API. Check your internet connection."
    if isinstance(e, anthropic.AnthropicError) and "api_key" in str(e).lower():
        return "No Claude credentials found. Set ANTHROPIC_API_KEY in your .env file (see .env.example)."
    return f"{type(e).__name__}: {e}"


def describe_openai_error(e: Exception, model: str) -> str:
    import openai

    if isinstance(e, openai.AuthenticationError):
        return "OpenAI rejected the API key. Check OPENAI_API_KEY in your .env file."
    if isinstance(e, openai.PermissionDeniedError):
        return "This OpenAI key cannot use this model."
    if isinstance(e, openai.NotFoundError):
        return f"OpenAI model '{model}' was not found. Check OKDS_OPENAI_MODEL in your .env file."
    if isinstance(e, openai.RateLimitError):
        return "OpenAI rate limit or quota reached. Check your API billing, then try again."
    if isinstance(e, openai.BadRequestError):
        return f"OpenAI rejected the request: {e.message}"
    if isinstance(e, openai.APIStatusError):
        return f"OpenAI API error {e.status_code}: {e.message}"
    if isinstance(e, openai.APIConnectionError):
        return "Could not reach the OpenAI API (or the local model server). Check the connection."
    if "credential" in str(e).lower() or "api_key" in str(e).lower():
        return "No OpenAI API key found. Set OPENAI_API_KEY in your .env file (see .env.example)."
    return f"{type(e).__name__}: {e}"


# ---------------------------------------------------------------- streaming

def stream_text(
    *,
    model: str,
    system: str,
    user: str,
    effort: str,
    result: StreamResult,
    max_tokens: int = 32000,
    provider: str = "claude",
) -> Iterator[str]:
    """Yield text as it arrives. When done, `result` holds the full text and stop reason.
    Raises LLMError with a plain-English message on any API problem or a refusal."""
    if provider == "openai":
        yield from _stream_openai(model=model, system=system, user=user, result=result)
    elif provider == "claude":
        yield from _stream_claude(model=model, system=system, user=user, effort=effort,
                                  max_tokens=max_tokens, result=result)
    else:
        raise LLMError("AI is off. Add a Claude or OpenAI API key to your .env file (see .env.example).")
    if result.stop_reason == "refusal":
        raise LLMError("The model declined this request. Try a different question or source text.")


def _stream_claude(*, model: str, system: str, user: str, effort: str, max_tokens: int,
                   result: StreamResult) -> Iterator[str]:
    try:
        client = make_client()
        with client.beta.messages.stream(
            model=model,
            max_tokens=max_tokens,
            betas=[FALLBACK_BETA],
            fallbacks="default",
            output_config={"effort": effort},
            cache_control={"type": "ephemeral"},
            system=system,
            messages=[{"role": "user", "content": user}],
        ) as stream:
            for text in stream.text_stream:
                result.chunks.append(text)
                yield text
            result.message = stream.get_final_message()
    except TypeError as e:  # the SDK raises TypeError when it finds no credentials at all
        if "authentication" not in str(e).lower():
            raise
        raise LLMError(describe_error(e)) from e
    except anthropic.AnthropicError as e:
        raise LLMError(describe_error(e)) from e
    usage = getattr(result.message, "usage", None)
    result.model = getattr(result.message, "model", model)
    result.usage = {"input_tokens": getattr(usage, "input_tokens", None),
                    "output_tokens": getattr(usage, "output_tokens", None),
                    # with prompt caching, most of the prompt is counted here instead of input_tokens
                    "cache_creation_input_tokens": getattr(usage, "cache_creation_input_tokens", None) or 0,
                    "cache_read_input_tokens": getattr(usage, "cache_read_input_tokens", None) or 0}


OPENAI_FINISH = {"stop": "end_turn", "length": "max_tokens", "content_filter": "refusal"}


def _stream_openai(*, model: str, system: str, user: str, result: StreamResult) -> Iterator[str]:
    """Chat Completions streaming. No temperature or token limit is sent, so the same call
    works with OpenAI reasoning models and with local servers like Ollama."""
    try:
        import openai
    except ImportError as e:
        raise LLMError('OpenAI support is not installed. Run: pip install -e "."') from e
    try:
        client = make_openai_client()
        stream = client.chat.completions.create(
            model=model,
            messages=[{"role": "system", "content": system}, {"role": "user", "content": user}],
            stream=True,
            stream_options={"include_usage": True},
        )
        for chunk in stream:
            result.model = getattr(chunk, "model", None) or result.model or model
            usage = getattr(chunk, "usage", None)
            if usage:
                result.usage = {"input_tokens": getattr(usage, "prompt_tokens", None),
                                "output_tokens": getattr(usage, "completion_tokens", None)}
            for choice in chunk.choices or []:
                text = getattr(choice.delta, "content", None)
                if text:
                    result.chunks.append(text)
                    yield text
                if choice.finish_reason:
                    result.finish = OPENAI_FINISH.get(choice.finish_reason, choice.finish_reason)
    except openai.OpenAIError as e:
        raise LLMError(describe_openai_error(e, model)) from e
