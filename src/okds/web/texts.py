"""Fixed text for the KO portal pages (ported from the Streamlit portal: page_home.py and guide.py)."""

from __future__ import annotations

# ---------------------------------------------------------------- What is a KO (At a glance)

JOBS = [
    {"title": "For people", "text": "A clear explanation to learn from.",
     "gets": ["Plain words (grade 6–8 for patients), with medical terms explained",
              "A source marker on every fact, so you can check it",
              "Myths vs. facts, questions to ask your doctor, and when to seek care"],
     "sample_label": "What a reader sees",
     "sample": "Carpal tunnel syndrome happens when the median nerve\nis squeezed inside the wrist [S2].",
     "used_by": "patients, caregivers, students, and clinicians, in the KO Library and OrthoBot answers"},
    {"title": "For computers",
     "text": "Labels and links that search, OrthoBot, and the knowledge graph can follow.",
     "gets": ["Fixed labels (ID, type, body area, readers) for search and filters",
              "Named links (like “diagnosed by” and “treats”) to build the knowledge graph",
              "Sources and test questions, so OrthoBot can cite answers and be tested"],
     "sample_label": "What a computer reads",
     "sample": "ko_id: KO-HAND-COND-001\nko_type: Condition\nrelationships:\n  - DIAGNOSED_BY: KO-HAND-DX-001",
     "used_by": "search, OrthoBot (our AI helper), the knowledge graph, and learning paths"},
]
# (a recipe card..., a Knowledge Object..., example)
ANALOGY = [
    ("is about **one** dish", "is about **one** topic", "Carpal tunnel syndrome"),
    ("always has the **same layout**", "always has the **same labels and sections**", "ID, type, readers, summary…"),
    ("lists its **ingredients**", "lists its **sources**, and marks each fact with [S1]", "[S1] MedlinePlus"),
    ("says **“see also”**", "**links** to related topics", "diagnosed by → Nerve Conduction Study"),
    ("is **tested** before it goes in the cookbook", "is **checked by people** before it is shared",
     "draft → team checked → published"),
]
MAKE_STEPS = [
    ("Pick a topic", "Choose one topic. It gets a permanent ID, like KO-HAND-COND-001."),
    ("Gather sources", "Find 2 or more trusted pages, like MedlinePlus or AAOS."),
    ("Write a draft", "AI drafts it from those sources only, or a person writes it."),
    ("Check every fact", "A person compares each [S#] with its source and fixes mistakes."),
    ("Save and share", "People can read it, and OrthoBot and the knowledge graph can use it."),
]
GLOSSARY = [
    ("Knowledge Object (KO)", "A short, trusted note about one topic."),
    ("Topic", "The one thing a KO explains, like a condition, a test, or a surgery."),
    ("ID", "A permanent code for a KO, like KO-HAND-COND-001. It never changes."),
    ("Source marker [S1]", "A tag after a fact that points to the source it came from."),
    ("<verify>", "A placeholder that means “not checked yet”."),
    ("Link", "A named connection between two KOs, like “diagnosed by”."),
    ("Knowledge graph", "All the KOs and their links together, like a map."),
    ("OrthoBot", "Our helper. It answers only from its sources and shows them."),
    ("Draft → checked → published", "The steps a KO goes through before people rely on it."),
]
SHARED_LABELS = ["ID", "Title", "Type", "Body area", "Readers", "Reading level", "Sources", "Review status", "Version",
                 "Dates"]
SHARED_SECTIONS = ["Summary", "Key facts", "Explanation", "Common misunderstandings", "Questions to ask your doctor",
                   "Test questions", "Related topics", "References"]
OPTIONAL_SECTION = "Questions to ask your doctor"  # only for patient and caregiver readers
# (ko_type, name shown, links in plain words, example topic)
TYPES = [
    ("Condition", "Condition", "affects → body part · diagnosed by → test", "Carpal Tunnel Syndrome"),
    ("DiagnosticTest", "Diagnostic test", "used to diagnose → condition · recommended by → guideline",
     "Nerve Conduction Study"),
    ("Treatment", "Treatment", "treats → condition · alternative to → other treatment", "Wrist Splinting"),
    ("Procedure", "Procedure (surgery)", "treats → condition · uses → device · followed by → rehab plan",
     "Carpal Tunnel Release"),
]
OTHER_TYPES = "Anatomy, Device, Rehab plan, Outcome measure, and General concept"
RULES = [
    {"title": "One topic per KO", "rule": "Each KO explains exactly one thing.",
     "do": "Meniscus tear", "dont": "Knee problems",
     "why": "A small topic can be reused, linked, and cited by its ID.",
     "portal": "Every topic gets one ID in the Topics list. Duplicate names are blocked."},
    {"title": "Sourced, never made up", "rule": "Every fact ends with a source marker like [S1].",
     "do": "“…squeezed in the wrist [S2].”", "dont": "A fact with no source",
     "why": "Anyone can check each fact. Use 2+ trusted sources, rewrite them in your own words, and write <verify> "
            "when unsure.",
     "portal": "The checks flag facts without a marker and sources that are never cited."},
    {"title": "AI drafts, people approve",
     "rule": "AI can help write a KO, but only people can approve it.",
     "do": "A person checks every [S#]", "dont": "Publishing an AI draft as-is",
     "why": "AI can sound sure and still be wrong. Health information needs a human check.",
     "portal": "Every new KO is saved as a draft. A checked status needs a checker's name."},
]
STATUS_PATH = [("draft", True), ("ai_checked", True), ("team_checked", False), ("clinician_reviewed", False),
               ("published", False)]

# ---------------------------------------------------------------- Generator help

FIELD_HELP = {
    "topic": "The one thing this KO explains. The list comes from the Concept Registry.",
    "main_name": "The usual name of the topic, e.g. Trigger Finger.",
    "other_names": "Other words for the same thing. Split them with ;",
    "ko_type": "What kind of topic: Condition, DiagnosticTest, Treatment, Procedure (surgery), Device...",
    "specialty": "The body area, e.g. Hand, Spine, Sports. It becomes part of the ID.",
    "mesh": "Optional medical code. Leave empty if you are not sure.",
    "readers": "Who will read this KO. Put the main reader first.",
    "author": "Your name, so the team knows who made the draft.",
    "reading_level": "How simple the words are. 'grade 6-8' is good for patients.",
    "difficulty": "How hard the topic is for the reader.",
    "license": "The license for our own text. Keep CC-BY-4.0 unless told otherwise.",
    "known_source": "Optional. Pick a trusted site from our Data Sources list to fill in some boxes.",
    "url": "The link to the exact page about your topic (not the home page).",
    "fetch": "Copies the page text into the Source text box.",
    "title": "The name of the page.",
    "publisher": "Who published the page, e.g. MedlinePlus (National Library of Medicine).",
    "text": "The only facts the KO may use. Delete menus, ads, and other topics.",
    "source_type": "What kind of page it is, e.g. government health page, guideline, journal article.",
    "source_audience": "Who the page was written for.",
    "permitted_use": "Can we reuse it? public_domain = yes. link_and_paraphrase = rewrite in your own words only. "
                     "restricted = do not use. <verify> = not checked yet.",
    "publication_date": "The date on the page ('last reviewed' or 'updated'). Keep <verify> if there is none.",
    "retrieved_date": "The day you copied the text.",
    "evidence_strength": "Only for guidelines, e.g. 'Strong'. Leave empty otherwise.",
    "notes": "Anything the team should know about this source.",
    "draft_mode": "With AI: the AI writes a draft from your sources only. Empty template: you write it yourself.",
}

FIELD_TABLE = [
    ("1 · Topic", "Topic", FIELD_HELP["topic"]),
    ("1 · Topic", "Main name", FIELD_HELP["main_name"]),
    ("1 · Topic", "Other names", FIELD_HELP["other_names"]),
    ("1 · Topic", "KO type", FIELD_HELP["ko_type"]),
    ("1 · Topic", "Body area", FIELD_HELP["specialty"]),
    ("2 · Readers", "Readers", FIELD_HELP["readers"]),
    ("2 · Readers", "Your name", FIELD_HELP["author"]),
    ("2 · Readers", "More options", "Reading level, difficulty, license. The defaults are fine."),
    ("3 · Sources", "Known source", FIELD_HELP["known_source"]),
    ("3 · Sources", "Page link + Fetch", FIELD_HELP["url"] + " " + FIELD_HELP["fetch"]),
    ("3 · Sources", "Page title, Publisher", "The page name and who published it."),
    ("3 · Sources", "Source text", FIELD_HELP["text"]),
    ("3 · Sources", "More details", "Source type, reuse rules (permitted use), and dates."),
    ("4 · Draft", "Draft mode", FIELD_HELP["draft_mode"]),
    ("5 · Save", "Status", "Green = ready. Blue = can save, some facts say <verify>. Red = fix problems first."),
    ("5 · Save", "Preview / Edit / Checks", "Read it, change it, see what to fix."),
    ("5 · Save", "Save to library", "Saves it in the library. Find it in the KO Library."),
]

STEPS = {
    1: {"short": "Topic", "title": "Pick a topic", "sub": "What will this KO explain?",
        "intro": "Every KO explains <b>one</b> topic, like a condition, a test, or a surgery. First, choose your topic.",
        "help": [("Topic", FIELD_HELP["topic"]),
                 ("Add a new one", "Topic missing? Fill in 4 boxes: main name, other names, KO type, body area. "
                                   "The portal makes the ID.")],
        "example": "Carpal Tunnel Syndrome · KO-HAND-COND-001"},
    2: {"short": "Readers", "title": "Who will read it?", "sub": "This sets how simple the words are.",
        "intro": "Pick the readers. Put the <b>main reader first</b>. For patients, the KO uses simple words.",
        "help": [("Readers", FIELD_HELP["readers"]), ("Your name", FIELD_HELP["author"]),
                 ("More options", "Reading level, difficulty, and license. The defaults are fine.")],
        "example": "patient, caregiver"},
    3: {"short": "Sources", "title": "Add your sources",
        "sub": "At least 2 trusted pages. The KO may only use facts from them.",
        "intro": "Add <b>at least 2</b> trusted pages. These are the <b>only facts</b> the KO may use.",
        "help": [("Known source", FIELD_HELP["known_source"]),
                 ("Page link + Fetch", FIELD_HELP["url"] + " " + FIELD_HELP["fetch"]),
                 ("Page title, Publisher", "The page name and who published it."),
                 ("Source text", FIELD_HELP["text"]),
                 ("More details", "Type, reuse rules, and dates. link_and_paraphrase = rewrite in your own words.")],
        "example": "https://medlineplus.gov/carpaltunnelsyndrome.html"},
    4: {"short": "Draft", "title": "Make a draft", "sub": "Let AI write it, or write it yourself.",
        "intro": "<b>With AI:</b> the AI (Claude or OpenAI) writes a draft using only your sources.<br>"
                 "<b>Empty template:</b> you write it yourself.",
        "help": [("With AI", "The AI writes a draft using only your sources. It takes about a minute."),
                 ("Empty template", "You write the KO yourself. Replace every TODO."),
                 ("Generate draft", "Makes the draft, then opens step 5.")],
        "example": None},
    5: {"short": "Check & save", "title": "Check and save", "sub": "Read it, fix it, save it.",
        "intro": "Read the draft, fix what the checks find, then save it to your library.",
        "help": [("Status", "Green = ready. Blue = you can save, some facts say <verify>. Red = fix the problems first."),
                 ("Preview · Edit · Checks", "Read the KO, change the text, see what to fix."),
                 ("Save to library", "Saves it in the library. Find it in the KO Library.")],
        "example": None},
}
