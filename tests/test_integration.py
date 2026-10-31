"""Integration tests: website + OrthoBot API + library, against the real committed dataset."""

import functools
import os

os.environ["ORTHOINFO_RATE_LIMIT"] = "0"  # rate limiting has its own test below

from orthoinfo.app import RateLimiter, create_app  # noqa: E402


@functools.lru_cache(maxsize=1)
def client():
    return create_app().test_client()


def ask(question, **extra):
    return client().post("/api/ask", json={"question": question, **extra})


# ---- website is served and keeps its OrthoBot hooks -------------------------------------
def test_website_served_at_root_with_security_headers():
    r = client().get("/")
    html = r.get_data(as_text=True)
    assert r.status_code == 200 and "Exclusive Orthopedics Hub" in html
    assert 'id="orthobot"' in html and "/api/ask" in html
    assert "OrthoBot is not connected yet" not in html  # placeholder is gone
    assert r.headers["X-Content-Type-Options"] == "nosniff"
    assert "frame-ancestors 'none'" in r.headers["Content-Security-Policy"]


def test_medical_disclaimer_on_every_page():
    for path in ("/", "/library", "/search?q=carpal+tunnel", "/doc/mplus:carpaltunnelsyndrome",
                 "/browse/research_article", "/about"):
        html = client().get(path).get_data(as_text=True)
        assert 'class="disclaimer"' in html, path
        assert "does not give medical advice and does not diagnose" in html, path


def test_orthobot_reminds_to_consult_a_physician_and_about_section():
    html = client().get("/").get_data(as_text=True)
    assert "Always consult your physician." in html  # permanent box in the chat
    assert "DOCTOR_REMINDER" in html  # repeated at the top of every answer
    assert 'id="about"' in html and 'href="#about"' in html
    for part in ("Search bar", "Specialties", "Explore", "OrthoBot", "Resources", "Source library"):
        assert part in html.split('id="about"', 1)[1], part


def test_existing_site_features_still_present():
    html = client().get("/").get_data(as_text=True)
    for marker in ("function doSearch()", "function pick(", 'id="tiles"', "Orthopedic subspecialties", "Trusted sources"):
        assert marker in html, marker


# ---- API ---------------------------------------------------------------------------------
def test_health_and_info():
    h = client().get("/api/health").get_json()
    assert h["status"] == "ok" and h["documents"] > 0 and h["chunks"] > 0
    assert "patient_education" in client().get("/api/info").get_json()["source_types_available"]


def test_answer_has_cited_sources_and_notices():
    j = ask("Why do my fingers feel numb and tingly at night?").get_json()
    assert j["found"] and j["passages"]
    src = j["passages"][0]["source"]
    assert src["url"].startswith("https://") and src["license"] and src["retrieved"]
    assert j["passages"][0]["sections"][0]["lines"]
    assert "seek medical care" in j["emergency_notice"]
    assert j["appointment_questions"]["items"]
    assert j["meta"]["dataset_version"]


def test_scope_notice_for_personal_advice():
    j = ask("Should I stop taking ibuprofen before my wrist surgery?").get_json()
    assert j["scope_notice"] and "clinician" in j["scope_notice"]


def test_no_match_is_reported_not_invented():
    j = ask("qwertyuiop zxcvbnm").get_json()
    assert j["found"] is False and j["passages"] == []


def test_website_chrome_headings_are_never_returned():
    for q in ("arthritis diagnosis", "psoriatic arthritis", "lupus"):
        for p in ask(q, all_sources=True).get_json()["passages"]:
            for sec in p["sections"]:
                assert sec["heading"] not in ("Related Information", "Learn About Research")


def test_all_sources_flag_widens_search():
    j = ask("how do bones heal after a fracture", all_sources=True).get_json()
    assert j["meta"]["all_sources"] is True


def test_validation_errors_are_json():
    for body, status in (({}, 400), ({"question": ""}, 400), ({"question": 5}, 400), ({"question": "x" * 501}, 400)):
        r = client().post("/api/ask", json=body)
        assert r.status_code == status and "error" in r.get_json(), body
    r = client().post("/api/ask", data="not json", content_type="text/plain")
    assert r.status_code == 400 and "error" in r.get_json()
    assert client().get("/api/ask").status_code == 405
    assert "error" in client().get("/api/nope").get_json()


def test_html_is_not_interpreted_server_side():
    j = ask("<script>alert(1)</script> carpal tunnel").get_json()
    assert j["question"].startswith("<script>")  # echoed as data; the page renders it with textContent


def test_cors_only_for_configured_origins():
    r = client().post("/api/ask", json={"question": "carpal tunnel"}, headers={"Origin": "https://evil.example"})
    assert "Access-Control-Allow-Origin" not in r.headers


def test_rate_limiter_blocks_after_limit():
    rl = RateLimiter(3)
    assert [rl.allow("a") for _ in range(4)] == [True, True, True, False]
    assert rl.allow("b") is True
    assert RateLimiter(0).allow("a") is True


# ---- Anna's library pages still work, now under /library --------------------------------
def test_library_pages_still_work():
    c = client()
    assert c.get("/library").status_code == 200
    r = c.get("/search?q=carpal+tunnel+symptoms")
    assert r.status_code == 200 and "Questions to ask at your appointment" in r.get_data(as_text=True)
    assert c.get("/doc/mplus:carpaltunnelsyndrome").status_code == 200
    assert c.get("/doc/does-not-exist").status_code == 404
    assert c.get("/about").status_code == 200


def test_browse_lists_non_patient_sources():
    c = client()
    library = c.get("/library").get_data(as_text=True)
    assert "/browse/research_article" in library and "/browse/textbook" in library
    html = c.get("/browse/research_article").get_data(as_text=True)
    assert "of 2220, most cited first" in html and html.count('href="/doc/pmc:') == 50
    html = c.get("/browse/research_article?topic=carpal+tunnel+syndrome&q=surgery").get_data(as_text=True)
    assert "/doc/pmc:" in html and "Showing 1–" in html
    assert "No research articles match" in c.get("/browse/research_article?q=zzzz").get_data(as_text=True)
    assert c.get("/browse/textbook").status_code == 200
    assert c.get("/browse/patient_education").status_code == 404  # already listed on /library
    assert c.get("/browse/nonsense").status_code == 404
