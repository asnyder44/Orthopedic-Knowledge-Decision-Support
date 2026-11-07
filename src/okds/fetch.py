"""Fetch the readable text of a public web page, to paste into a source pack.

Only public http(s) addresses are allowed, so the tool cannot be used to reach
services on your own machine or private network. The address is checked again at the
moment of connecting, and the connection goes to the checked IP (no DNS-rebinding trick),
for the first request and every redirect. Proxies are not used, so the check covers the
real connection.
"""

from __future__ import annotations

import codecs
import http.client
import ipaddress
import re
import socket
import ssl
import time
import urllib.request
from dataclasses import dataclass
from html.parser import HTMLParser
from urllib.parse import urljoin, urlparse

import certifi

MAX_BYTES = 3_000_000
TIMEOUT = 20          # per network step (connect, each read)
TOTAL_TIMEOUT = 45    # the whole download
USER_AGENT = "OKDS-portal/0.1 (student research project; source text for paraphrasing)"


class FetchError(RuntimeError):
    pass


@dataclass
class FetchResult:
    url: str
    title: str
    text: str


class _TextExtractor(HTMLParser):
    SKIP = {"script", "style", "noscript", "nav", "header", "footer", "aside", "form", "svg", "button", "template"}
    BLOCK = {"p", "li", "h1", "h2", "h3", "h4", "h5", "h6", "tr", "dd", "dt", "blockquote", "section", "div", "br"}
    MAIN = {"main", "article"}

    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.parts: list[str] = []
        self.main_parts: list[str] = []  # text inside <main>/<article>, preferred when present
        self.title = ""
        self._skip = 0
        self._main = 0
        self._in_title = False

    def _emit(self, text: str) -> None:
        self.parts.append(text)
        if self._main:
            self.main_parts.append(text)

    def handle_starttag(self, tag: str, attrs) -> None:
        if tag in self.SKIP:
            self._skip += 1
        elif tag == "title" and not self._skip and not self.title:
            self._in_title = True
        elif tag in self.MAIN:
            self._main += 1
        elif tag in self.BLOCK:
            self._emit("\n")
        if tag == "li" and not self._skip:
            self._emit("- ")

    def handle_endtag(self, tag: str) -> None:
        if tag in self.SKIP and self._skip:
            self._skip -= 1
        elif tag == "title":
            self._in_title = False
        elif tag in self.MAIN and self._main:
            self._main -= 1
        elif tag in self.BLOCK:
            self._emit("\n")

    def handle_data(self, data: str) -> None:
        if self._in_title:
            self.title += data
        elif not self._skip:
            self._emit(data)

    def text(self) -> str:
        main = clean_text("".join(self.main_parts))
        return main if len(main) >= 400 else clean_text("".join(self.parts))


def _public_addresses(host: str, port: int) -> list[str]:
    """All IPs of `host`; FetchError if any of them is private, local, or reserved."""
    try:
        infos = socket.getaddrinfo(host, port, type=socket.SOCK_STREAM)
    except (socket.gaierror, UnicodeError, ValueError) as e:
        raise FetchError(f"Cannot find the host '{host}'.") from e
    addresses = []
    for info in infos:
        ip = ipaddress.ip_address(info[4][0])
        if not ip.is_global:
            raise FetchError("This address points to a private or local network, so it is blocked.")
        addresses.append(info[4][0])
    if not addresses:
        raise FetchError(f"Cannot find the host '{host}'.")
    return addresses


def _check_public(url: str) -> None:
    parsed = urlparse(url)
    if parsed.scheme not in ("http", "https") or not parsed.hostname:
        raise FetchError("Only http:// or https:// web addresses can be fetched.")
    try:
        port = parsed.port
    except ValueError as e:
        raise FetchError("The page link has a bad port number.") from e
    _public_addresses(parsed.hostname, port or (443 if parsed.scheme == "https" else 80))


def _connect(host: str, port: int, timeout: float | None) -> socket.socket:
    """Connect to a checked public IP of `host` (the check and the connection use the same IP)."""
    last: OSError | None = None
    for ip in _public_addresses(host, port):
        try:
            return socket.create_connection((ip, port), timeout)
        except OSError as e:
            last = e
    raise FetchError(f"Could not connect to {host}.") from last


class _PinnedHTTPConnection(http.client.HTTPConnection):
    def connect(self) -> None:
        self.sock = _connect(self.host, self.port, self.timeout)


class _PinnedHTTPSConnection(http.client.HTTPSConnection):
    def connect(self) -> None:
        sock = _connect(self.host, self.port, self.timeout)
        self.sock = self._context.wrap_socket(sock, server_hostname=self.host)


class _PinnedHTTPHandler(urllib.request.HTTPHandler):
    def http_open(self, req):
        return self.do_open(_PinnedHTTPConnection, req)


class _PinnedHTTPSHandler(urllib.request.HTTPSHandler):
    def https_open(self, req):
        return self.do_open(_PinnedHTTPSConnection, req, context=self._context)


class _SafeRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        _check_public(urljoin(req.full_url, newurl))
        return super().redirect_request(req, fp, code, msg, headers, newurl)


def clean_text(raw: str) -> str:
    lines = [" ".join(line.split()) for line in raw.split("\n")]
    out: list[str] = []
    for line in lines:
        if line in ("", "-"):
            if out and out[-1] != "":
                out.append("")
        else:
            out.append(line)
    return "\n".join(out).strip()


# Some sites (e.g. NCBI Bookshelf / StatPearls) answer scripts with a robot-check page instead of the article.
BOT_CHECK_RE = re.compile(r"checking your browser|recaptcha|verify (that )?you are (a )?human|are you a robot|"
                          r"enable javascript and cookies|access denied", re.I)
BOT_CHECK_MSG = ("This site shows a robot check ('checking your browser') instead of the page. "
                 "Open the page in your browser, copy the text, and paste it into Source text.")
MIN_TEXT_CHARS = 200


def looks_like_bot_check(text: str) -> bool:
    """True for short robot-check pages. Long articles that only mention these words are fine."""
    return len(text) < 2000 and bool(BOT_CHECK_RE.search(text))


def fetch_page(url: str) -> FetchResult:
    url = url.strip()
    _check_public(url)
    # certifi's CA bundle: works the same on every OS (python.org macOS builds ship without root certificates).
    tls = ssl.create_default_context(cafile=certifi.where())
    opener = urllib.request.build_opener(urllib.request.ProxyHandler({}), _SafeRedirect, _PinnedHTTPHandler(),
                                         _PinnedHTTPSHandler(context=tls))
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT, "Accept": "text/html,text/plain"})
    deadline = time.monotonic() + TOTAL_TIMEOUT
    try:
        with opener.open(req, timeout=TIMEOUT) as resp:
            ctype = resp.headers.get("Content-Type", "")
            if "html" not in ctype and "text/plain" not in ctype:
                raise FetchError(f"This page is '{ctype or 'unknown type'}'. Only HTML or plain text is supported.")
            parts, size = [], 0
            while chunk := resp.read(65536):
                size += len(chunk)
                if size > MAX_BYTES:
                    raise FetchError("The page is too large to fetch.")
                if time.monotonic() > deadline:
                    raise FetchError("The page took too long to load. Copy the text by hand instead.")
                parts.append(chunk)
            data = b"".join(parts)
            charset = resp.headers.get_content_charset() or "utf-8"
            final_url = resp.geturl()
    except FetchError:
        raise
    except Exception as e:
        raise FetchError(f"Could not fetch the page: {e}") from e
    try:
        codecs.lookup(charset)
    except LookupError:
        charset = "utf-8"  # the page names an unknown character set
    html = data.decode(charset, errors="replace")
    if "text/plain" in ctype:
        return FetchResult(final_url, "", clean_text(html))
    try:
        parser = _TextExtractor()
        parser.feed(html)
        title, text = " ".join(parser.title.split()), parser.text()
    except Exception as e:
        raise FetchError(f"Could not read the page text: {e}") from e
    if looks_like_bot_check(f"{title}\n{text}"):
        raise FetchError(BOT_CHECK_MSG)
    if len(text) < MIN_TEXT_CHARS:
        raise FetchError("The page has almost no text (it may need JavaScript). "
                         "Open it in your browser, copy the text, and paste it into Source text.")
    return FetchResult(final_url, title, text)
