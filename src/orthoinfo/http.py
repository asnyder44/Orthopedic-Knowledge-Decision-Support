"""A small, polite HTTP client shared by all source collectors.

* identifies the project in the User-Agent
* waits between requests to the same host
* honours robots.txt for web pages (APIs are called as documented by their owners)
* retries temporary failures, and stops with a clear message on CAPTCHA or
  network-filter pages instead of trying to get around them
"""

from __future__ import annotations

import json
import time
import urllib.error
import urllib.parse
import urllib.request
import urllib.robotparser

USER_AGENT = "orthoinfo-student-project/0.2 (educational; Data Science in Practice)"


class BlockedError(RuntimeError):
    """The site or network refused automated access (CAPTCHA, filter page)."""


def _use_os_certificates() -> None:
    # Networks that inspect TLS (campus/corporate filters) re-sign traffic with a
    # certificate only the operating system trusts.
    try:
        import truststore

        truststore.inject_into_ssl()
    except ImportError:  # pragma: no cover
        pass


class Http:
    def __init__(self, delay: float = 1.0, user_agent: str = USER_AGENT):
        _use_os_certificates()
        self.delay, self.user_agent = delay, user_agent
        self._last: dict[str, float] = {}
        self._robots: dict[str, urllib.robotparser.RobotFileParser] = {}

    def allowed(self, url: str) -> bool:
        parts = urllib.parse.urlsplit(url)
        root = f"{parts.scheme}://{parts.netloc}"
        if root not in self._robots:
            rp = urllib.robotparser.RobotFileParser(root + "/robots.txt")
            try:
                rp.parse(self.get(root + "/robots.txt", robots=False, retries=1).decode("utf-8", "replace").splitlines())
            except (urllib.error.URLError, BlockedError):
                rp.parse([])  # no readable robots.txt: everything allowed
            self._robots[root] = rp
        return self._robots[root].can_fetch(self.user_agent, url)

    def get(self, url: str, *, robots: bool = False, delay: float | None = None, retries: int = 3) -> bytes:
        if robots and not self.allowed(url):
            raise PermissionError(f"robots.txt disallows {url}")
        host = urllib.parse.urlsplit(url).netloc
        for attempt in range(retries):
            wait = (self.delay if delay is None else delay) - (time.monotonic() - self._last.get(host, 0.0))
            if wait > 0:
                time.sleep(wait)
            try:
                req = urllib.request.Request(url, headers={"User-Agent": self.user_agent})
                with urllib.request.urlopen(req, timeout=60) as resp:
                    data = resp.read()
                self._last[host] = time.monotonic()
                if b"recaptcha/challengepage" in data[:3000]:
                    raise BlockedError(f"{host} answered with a CAPTCHA; not collecting from it")
                return data
            except urllib.error.HTTPError as exc:
                self._last[host] = time.monotonic()
                body = exc.read()[:5000]
                if b"Zscaler" in body:
                    raise BlockedError(f"{host} is blocked by the network filter (Zscaler)") from exc
                if exc.code in (429, 500, 502, 503, 504) and attempt < retries - 1:
                    time.sleep(5 * 2**attempt)
                    continue
                raise
            except (urllib.error.URLError, TimeoutError, ConnectionError):
                self._last[host] = time.monotonic()
                if attempt < retries - 1:
                    time.sleep(5 * 2**attempt)
                    continue
                raise
        raise AssertionError("unreachable")

    def text(self, url: str, **kwargs) -> str:
        return self.get(url, **kwargs).decode("utf-8", "replace")

    def json(self, url: str, params: dict | None = None, **kwargs):
        if params:
            url = f"{url}?{urllib.parse.urlencode(params)}"
        return json.loads(self.get(url, **kwargs))
