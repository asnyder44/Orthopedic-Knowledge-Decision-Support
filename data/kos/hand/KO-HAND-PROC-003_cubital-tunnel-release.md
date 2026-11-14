---
schema_version: okds-ko-1.0
ko_id: KO-HAND-PROC-003
title: Cubital Tunnel Release
preferred_term: Cubital Tunnel Release
alternate_terms:
- in situ decompression of the ulnar nerve
- cubital tunnel decompression
- ulnar nerve decompression
- open in situ decompression
- endoscopic cubital tunnel release
- CuTS release
ko_type: Procedure
specialty: HAND
cluster: 5
audience:
- patient
- caregiver
reading_level: grade 6-8
difficulty: beginner
summary: Cubital tunnel release is surgery that frees the ulnar nerve where it is squeezed at the elbow
  in cubital tunnel syndrome [S1][S3]. In in situ decompression, the surgeon releases
  the tissue pressing on the nerve but leaves the nerve in its normal place [S5]. It can be done through
  an open cut or with a small camera (endoscopic release), and it is used when non-surgical care has not
  worked [S2][S3][S4].
codes:
  mesh: <verify>
  icd10cm: <verify>
tags:
- elbow surgery
- nerve surgery
- cubital tunnel syndrome treatment
- ulnar nerve
- in situ decompression
- endoscopic cubital tunnel release
- local anesthesia
relationships:
- predicate: TREATS
  target_id: KO-HAND-COND-002
  target_label: Cubital Tunnel Syndrome
  source_ids:
  - S1
  - S2
  - S3
  - S5
- predicate: ALTERNATIVE_TO
  target_id: KO-HAND-PROC-004
  target_label: Ulnar Nerve Transposition
  source_ids:
  - S1
  - S2
  - S5
- predicate: ALTERNATIVE_TO
  target_id: KO-HAND-TRT-004
  target_label: Elbow Splinting
  source_ids:
  - S3
proposed_concepts:
- term: Medial epicondylectomy
  suggested_type: Procedure
  predicate: ALTERNATIVE_TO
  reason: S1 and S2 describe removing part of the inner elbow bone, alone or with decompression, as a
    related operation.
- term: Endoscope (camera used in endoscopic cubital tunnel release)
  suggested_type: Device
  predicate: USES_DEVICE
  reason: S4 describes endoscopic release as a short-incision technique with camera visualization.
- term: Patient-Rated Ulnar Nerve Evaluation (PRUNE)
  suggested_type: OutcomeMeasure
  predicate: MEASURED_BY
  reason: S2 lists PRUNE and other scales (Bishop, McGowan, Wilson-Krout) used to measure results.
- term: Recovery after cubital tunnel release
  suggested_type: RehabProtocol
  predicate: FOLLOWED_BY
  reason: The pack gives no aftercare timeline; a recovery KO would hold timing and warning signs.
sources:
- id: S1
  title: Safety and Outcomes of Different Surgical Techniques for Cubital Tunnel Decompression
  publisher: JAMA Network Open
  url: https://pmc.ncbi.nlm.nih.gov/articles/PMC7686867/
  source_type: journal_article
  audience: clinician
  publication_date: '2020'
  retrieved_date: '2026-10-26'
  permitted_use: open_license
  notes: 'From the OrthoInfo dataset (pmc:PMC7686867). Licence: CC BY'
- id: S2
  title: Surgical Approaches and Their Outcomes in the Treatment of Cubital Tunnel Syndrome
  publisher: Frontiers in Surgery
  url: https://pmc.ncbi.nlm.nih.gov/articles/PMC6071516/
  source_type: journal_article
  audience: clinician
  publication_date: '2018'
  retrieved_date: '2026-10-26'
  permitted_use: open_license
  notes: 'From the OrthoInfo dataset (pmc:PMC6071516). Licence: CC BY'
- id: S3
  title: 'Cubital Tunnel Release Under Local and Regional Anesthesia: A Scoping Review'
  publisher: Plastic Surgery
  url: https://pmc.ncbi.nlm.nih.gov/articles/PMC12743009/
  source_type: journal_article
  audience: clinician
  publication_date: '2025'
  retrieved_date: '2026-10-26'
  permitted_use: open_license
  notes: 'From the OrthoInfo dataset (pmc:PMC12743009). Licence: CC BY'
- id: S4
  title: 'Endoscopic cubital tunnel release: a systematic review'
  publisher: Oxford University Press (OUP)
  url: https://doi.org/10.1093/bmb/ldv049
  source_type: systematic_review
  audience: clinician
  publication_date: '2015'
  retrieved_date: '2026-11-14'
  permitted_use: link_and_paraphrase
  notes: 'Found via openaire. Licence: Open Access. Type: systematic review. Text kept: abstract only.'
- id: S5
  title: 'Higher Revision Rates With In Situ Decompression as Compared to Ulnar Nerve Transposition for
    Cubital Tunnel Syndrome: A Meta-Regression Analysis'
  publisher: Cureus
  url: https://pmc.ncbi.nlm.nih.gov/articles/PMC11438553/
  source_type: journal_article
  audience: clinician
  publication_date: '2024'
  retrieved_date: '2026-10-26'
  permitted_use: open_license
  notes: 'From the OrthoInfo dataset (pmc:PMC11438553). Licence: CC BY'
review:
  status: draft
  author: KO Collector + Claude (Claude Code session)
  generated_by:
    model: claude-opus-5-5 (Claude Code session)
    prompt_version: okds-gen-1.1
  ai_check: null
  team_checker: null
  clinician_reviewer: null
  clinician_role: null
  review_date: null
  open_issues:
  - No patient-level page (MedlinePlus/NIAMS) on cubital tunnel release was found in the local dataset
    or the candidates; consider adding one (e.g. MedlinePlus 'Ulnar nerve dysfunction' or AAOS OrthoInfo
    'Cubital tunnel syndrome').
  - 'Clinician check: S1 (network meta-analysis) found open in situ decompression had the best outcomes
    and fewest reoperations, while S5 (meta-regression) found more revisions after in situ decompression
    than after transposition at 48+ months. The KO reports both; confirm the wording is balanced.'
  - 'Recovery timeline is thin: the pack has no week-by-week recovery plan; only S4 (faster return to work
    after endoscopic release) and S3 (overnight stay more often with general anesthesia). Ask a clinician
    / add a source with aftercare details.'
  - S4 is an abstract only with an unclear licence (link_and_paraphrase); paraphrase only.
  - The 'cubital tunnel release' term in S3 includes transposition as well as decompression; this KO uses
    it for decompression and keeps transposition in KO-HAND-PROC-004. Confirm the scope split.
  - codes.mesh and codes.icd10cm are <verify>. ICD-10-CM codes diagnoses, not procedures; a procedure
    code system may fit better.
safety:
  not_medical_advice: true
  scope_note: General education only. Not a diagnosis or treatment plan.
version: 0.1.0
created: '2026-11-14'
last_updated: '2026-11-14'
update_triggers:
- A new randomized trial or meta-analysis with long follow-up compares in situ decompression with ulnar
  nerve transposition.
- A guideline on surgical treatment of cubital tunnel syndrome is published or updated.
license: CC-BY-4.0
change_log:
- version: 0.1.0
  date: '2026-11-14'
  by: KO Collector + Claude (Claude Code session)
  change: Initial draft.
---

## Summary
Cubital tunnel release is an operation for cubital tunnel syndrome, a condition where the ulnar nerve is squeezed or stretched at the elbow [S3]. The ulnar nerve carries feeling to the ring and little fingers and helps control hand muscles [S2]. In this surgery, called in situ decompression, the surgeon frees the nerve but leaves it in its usual place [S5]. Surgery is used when non-surgical care has not worked, and studies show that most people improve after it [S1][S3].

## Key Facts (claim → source)
- Cubital tunnel syndrome is the second most common nerve squeezing problem in the arm, after carpal tunnel syndrome [S2][S3].
- Surgery to take pressure off the nerve is the most effective treatment, and about 15,000 people in the UK and US have it each year [S1].
- In a large review of 30 studies, 87% of patients improved after surgery [S1].
- That review found open in situ decompression was linked with the best results and the fewest repeat operations [S1].
- Another review found that, after 4 or more years, repeat surgery was more common after in situ decompression (about 12%) than after moving the nerve (about 3%) [S5].
- Endoscopic release uses a short cut and may allow a quicker return to work [S4].
- The surgery can be done with local or regional anesthesia (numbing only part of the body) about as safely as with general anesthesia [S3].

## Explanation
### What it is
The cubital tunnel is the path the ulnar nerve takes around the inside of the elbow [S3]. In cubital tunnel syndrome, the nerve is pressed or pulled in this area [S3]. Cubital tunnel release, also called in situ decompression, frees the nerve from the tissue pressing on it while leaving it in its normal position [S5]. This is different from ulnar nerve transposition, where the nerve is also moved to the front of the bony bump on the inner elbow (the medial epicondyle) [S5].

### Why it is done
The goal is to relieve pressure on the ulnar nerve [S1]. Symptoms of cubital tunnel syndrome often start as tingling or odd feelings in the inner forearm and the ring and little fingers [S2]. Over time, people may lose feeling, notice hand weakness or cramping, or have fingers that curl like a claw [S2]. Surgery is an option when non-surgical care, such as wearing an elbow splint at night, has not helped [S3].

### How it is done
- **Open decompression:** The surgeon usually makes one cut along the inner elbow to see the nerve directly [S2]. This lets the surgeon free the nerve at several places where it can be squeezed [S2]. The cut is often 8 to 10 cm long, or longer [S2].
- **Endoscopic release:** The surgeon uses a short cut and a camera to see where the nerve is trapped [S4].
- **Minimal incision release:** A smaller-cut method is also used [S2].
- **Anesthesia:** The surgery can be done with general anesthesia (fully asleep), regional anesthesia (a nerve block for the arm), or local anesthesia (numbing near the cut) [S3]. One local method, called WALANT, lets the patient stay fully awake without a tourniquet (a tight band that limits blood flow) [S3].

Some surgeons also remove part of the bony bump on the inner elbow, called medial epicondylectomy [S1]. This is generally done only when the bone shape is abnormal, such as after an injury [S2].

### Devices used
Endoscopic release uses a camera to see the nerve through a short cut [S4]. The sources here do not name specific instruments or brands.

### Risks
About 3% of patients had problems after surgery, such as bleeding, infection, or the wound opening [S1]. After open decompression, the most common problems were tenderness at the cut and numbness near the cut from injury to a small skin nerve [S2]. Longer cuts can raise the risk of injury to this skin nerve and may mean more pain and slower healing [S2]. With endoscopic release, this skin nerve is injured less often, and the most common problem is a hematoma (a pocket of blood under the skin) [S4]. Up to 30% of patients may not improve after surgery, and repeat surgery rarely cures the problem [S1]. Complication rates were similar with local, regional, and general anesthesia, at about 2% to 3% [S3].

### Recovery timeline
The sources here do not give a step-by-step recovery schedule, so ask your surgeon what to expect. Endoscopic release may shorten the time before a person can return to work [S4]. People who had general anesthesia more often needed to stay overnight in the hospital than people who had regional anesthesia [S3]. One study found less pain after surgery with local anesthesia than with general anesthesia [S3]. People with more severe nerve compression tended to have less good results [S4].

### Alternatives
- **Non-surgical care:** Wearing an elbow splint at night is one non-surgical treatment [S3].
- **Ulnar nerve transposition:** The nerve is freed and moved to the front of the inner elbow bone [S5]. Most experts prefer this when the nerve slips out of place (subluxes) during elbow movement [S2]. One review found fewer repeat surgeries over the long term with transposition [S5].
- **Medial epicondylectomy:** Part of the inner elbow bone is removed, with or without decompression [S1][S2].
- No one technique has been shown to be best for everyone, and all appear to be effective [S2].

## Common Misunderstandings
- **Myth:** There is one best operation for cubital tunnel syndrome. **Fact:** Reviews have not found one technique that is better than all others, and surgeons often use more than one [S1][S2].
- **Myth:** Surgery always fixes cubital tunnel syndrome. **Fact:** Most people improve, but up to 30% may not, and repeat surgery is rarely curative [S1].
- **Myth:** You must be fully asleep for this surgery. **Fact:** Local and regional anesthesia are safe options with similar complication rates [S3].
- **Myth:** Leaving the nerve in place is always the safest long-term choice. **Fact:** One review found more repeat surgeries after decompression than after transposition when patients were followed for 4 or more years [S5].

## Questions to Ask Your Doctor
1. Have I tried the non-surgical treatments that make sense for me?
2. Will you leave my nerve in place or move it, and why?
3. Would open or endoscopic surgery be better for me?
4. What kind of anesthesia will I have, and will I be awake?
5. What problems should I watch for after surgery?
6. When can I go back to work and my usual activities?

## Test Questions
1. Which nerve does cubital tunnel release free? - The ulnar nerve at the elbow [S3].
2. What does "in situ decompression" mean? - Freeing the nerve but leaving it in its normal place [S5].
3. In the review of 30 studies, about what share of patients improved after surgery? - About 87% [S1].
4. What is the most common complication of endoscopic release? - A hematoma (a pocket of blood) [S4].
5. When is moving the nerve (transposition) usually preferred? - When the nerve slips out of place [S2].
6. Name two types of anesthesia that can be used instead of general anesthesia. - Local and regional anesthesia [S3].

## Related Topics
- Treats: Cubital Tunnel Syndrome (KO-HAND-COND-002)
- Alternative to: Ulnar Nerve Transposition (KO-HAND-PROC-004), Elbow Splinting (KO-HAND-TRT-004)
- Proposed new topics: Medial epicondylectomy (procedure), Endoscope (device), PRUNE (outcome measure), Recovery after cubital tunnel release (rehab protocol)

## References
1. [S1] JAMA Network Open. *Safety and Outcomes of Different Surgical Techniques for Cubital Tunnel Decompression.* https://pmc.ncbi.nlm.nih.gov/articles/PMC7686867/ (retrieved 2026-10-26)
2. [S2] Frontiers in Surgery. *Surgical Approaches and Their Outcomes in the Treatment of Cubital Tunnel Syndrome.* https://pmc.ncbi.nlm.nih.gov/articles/PMC6071516/ (retrieved 2026-10-26)
3. [S3] Plastic Surgery. *Cubital Tunnel Release Under Local and Regional Anesthesia: A Scoping Review.* https://pmc.ncbi.nlm.nih.gov/articles/PMC12743009/ (retrieved 2026-10-26)
4. [S4] Oxford University Press (OUP). *Endoscopic cubital tunnel release: a systematic review.* https://doi.org/10.1093/bmb/ldv049 (retrieved 2026-11-14)
5. [S5] Cureus. *Higher Revision Rates With In Situ Decompression as Compared to Ulnar Nerve Transposition for Cubital Tunnel Syndrome: A Meta-Regression Analysis.* https://pmc.ncbi.nlm.nih.gov/articles/PMC11438553/ (retrieved 2026-10-26)
