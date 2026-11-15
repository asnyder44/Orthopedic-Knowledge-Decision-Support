"""One TLS setting for every outgoing request (page fetch, source collector, pipeline)."""

from __future__ import annotations

import ssl

import certifi


def tls_context() -> ssl.SSLContext:
    """The operating system's certificate store when `truststore` is installed (needed on campus and corporate
    networks that inspect TLS), else certifi's bundle (works the same on every OS)."""
    try:
        import truststore

        return truststore.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
    except ImportError:
        return ssl.create_default_context(cafile=certifi.where())
