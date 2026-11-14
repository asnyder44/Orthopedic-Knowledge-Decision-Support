---
schema_version: okds-ko-1.0
ko_id: KO-HAND-PROC-004
title: Ulnar Nerve Transposition
preferred_term: Ulnar Nerve Transposition
alternate_terms:
- anterior transposition of the ulnar nerve
- anterior ulnar nerve transposition
- subcutaneous anterior transposition (SAT)
- submuscular transposition
- intramuscular transposition
ko_type: Procedure
specialty: HAND
cluster: 5
audience:
- patient
- caregiver
reading_level: grade 6-8
difficulty: beginner
summary: Ulnar nerve transposition is surgery for cubital tunnel syndrome in which the surgeon frees the
  ulnar nerve at the elbow and moves it to the front of the bony bump on the inner elbow [S3]. The nerve
  can be placed under the skin (subcutaneous) or under a muscle (submuscular), and studies have not shown
  that one placement works better than the other [S1][S2]. It is generally preferred when the nerve slips
  out of place as the elbow moves [S5].
codes:
  mesh: <verify>
  icd10cm: <verify>
tags:
- elbow surgery
- nerve surgery
- cubital tunnel syndrome treatment
- ulnar nerve
- subcutaneous transposition
- submuscular transposition
- revision surgery
relationships:
- predicate: TREATS
  target_id: KO-HAND-COND-002
  target_label: Cubital Tunnel Syndrome
  source_ids:
  - S1
  - S2
  - S3
  - S4
- predicate: ALTERNATIVE_TO
  target_id: KO-HAND-PROC-003
  target_label: Cubital Tunnel Release
  source_ids:
  - S3
  - S4
  - S5
proposed_concepts:
- term: Medial epicondylectomy
  suggested_type: Procedure
  predicate: ALTERNATIVE_TO
  reason: S4 and S5 list medial epicondylectomy as one of the three common operations for cubital tunnel
    syndrome.
- term: Medial epicondyle
  suggested_type: AnatomicalStructure
  predicate: PREREQUISITE_FOR
  reason: S3 and S5 define transposition as moving the nerve in front of the medial epicondyle.
- term: Ulnar nerve subluxation
  suggested_type: Condition
  predicate: TREATS
  reason: S3 and S5 say transposition is generally preferred when the nerve slips out of place (subluxates).
- term: Recovery after ulnar nerve transposition
  suggested_type: RehabProtocol
  predicate: FOLLOWED_BY
  reason: The pack gives no aftercare timeline; a recovery KO would hold timing and warning signs.
sources:
- id: S1
  title: Subcutaneous Versus Submuscular Anterior Transposition of the Ulnar Nerve for Cubital Tunnel
    Syndrome
  publisher: Medicine
  url: https://pmc.ncbi.nlm.nih.gov/articles/PMC4602994/
  source_type: journal_article
  audience: clinician
  publication_date: '2015'
  retrieved_date: '2026-10-26'
  permitted_use: open_license
  notes: 'From the OrthoInfo dataset (pmc:PMC4602994). Licence: CC BY'
- id: S2
  title: 'Anterior Subcutaneous versus Submuscular Transposition of the Ulnar Nerve for Cubital Tunnel
    Syndrome: A Systematic Review and Meta-Analysis'
  publisher: PLoS ONE
  url: https://pmc.ncbi.nlm.nih.gov/articles/PMC4482721/
  source_type: journal_article
  audience: clinician
  publication_date: '2015'
  retrieved_date: '2026-10-26'
  permitted_use: open_license
  notes: 'From the OrthoInfo dataset (pmc:PMC4482721). Licence: CC BY'
- id: S3
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
- id: S4
  title: 'Simple decompression vs. subcutaneous anterior transposition of the ulnar nerve: the 2025 update
    on the optimal treatment for cubital tunnel syndrome'
  publisher: JSES Reviews, Reports, and Techniques
  url: https://pmc.ncbi.nlm.nih.gov/articles/PMC12966733/
  source_type: journal_article
  audience: clinician
  publication_date: '2025'
  retrieved_date: '2026-10-26'
  permitted_use: open_license
  notes: 'From the OrthoInfo dataset (pmc:PMC12966733). Licence: CC BY'
- id: S5
  title: Surgical Approaches and Their Outcomes in the Treatment of Cubital Tunnel Syndrome
  publisher: Frontiers in Surgery
  url: https://pmc.ncbi.nlm.nih.gov/articles/PMC6071516/
  source_type: journal_article
  audience: clinician
  publication_date: '2018'
  retrieved_date: '2026-10-26'
  permitted_use: open_license
  notes: 'From the OrthoInfo dataset (pmc:PMC6071516). Licence: CC BY'
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
  - No patient-level page (MedlinePlus/NIAMS) on ulnar nerve transposition was found in the local dataset
    or the candidates; consider adding one (e.g. AAOS OrthoInfo 'Cubital tunnel syndrome').
  - 'How it is done and Devices used are thin: the pack does not describe the operation step by step or
    name instruments. Ask a clinician / add a surgical technique source.'
  - 'Recovery timeline: the pack only says transposition can mean a later return to work (S4); no week-by-week
    timeline. Add a source with aftercare details.'
  - 'Clinician check: S3 finds fewer revisions after transposition at 48+ months, while S4 cites Wade et
    al. (open in situ decompression safest with best outcomes) and S3 cites studies with more morbidity
    after transposition. The KO reports both sides; confirm the wording is balanced.'
  - S1 and S2 are 2015 meta-analyses based on few, mostly observational studies with low-to-moderate evidence
    quality; S4 is a systematic review without meta-analysis. Newer RCT evidence may exist.
  - codes.mesh and codes.icd10cm are <verify>. ICD-10-CM codes diagnoses, not procedures; a procedure
    code system may fit better.
safety:
  not_medical_advice: true
  scope_note: General education only. Not a diagnosis or treatment plan.
version: 0.1.0
created: '2026-11-14'
last_updated: '2026-11-14'
update_triggers:
- A new randomized trial or meta-analysis with long follow-up compares ulnar nerve transposition with in
  situ decompression, or subcutaneous with submuscular transposition.
- A guideline on surgical treatment of cubital tunnel syndrome is published or updated.
license: CC-BY-4.0
change_log:
- version: 0.1.0
  date: '2026-11-14'
  by: KO Collector + Claude (Claude Code session)
  change: Initial draft.
---

## Summary
Ulnar nerve transposition is an operation for cubital tunnel syndrome, a condition where the ulnar nerve is squeezed at the elbow [S2][S3]. The surgeon frees the nerve and then moves it to the front of the medial epicondyle, the bony bump on the inner side of the elbow [S3]. The nerve can be placed just under the skin (subcutaneous), inside a muscle (intramuscular), or under a muscle (submuscular) [S2]. It is one of the most common operations for this condition, along with simple decompression, which frees the nerve but leaves it in place [S4].

## Key Facts (claim → source)
- Cubital tunnel syndrome is the second most common nerve entrapment (trapped nerve) problem after carpal tunnel syndrome [S2][S4].
- Surgery is generally used when non-surgical treatment has not worked [S4].
- Transposition is generally preferred when the ulnar nerve slips out of its groove (subluxes) before or during surgery [S5].
- Reviews found no clear difference in improvement between placing the nerve under the skin or under a muscle [S1][S2].
- Side effects were less common with the under-the-skin (subcutaneous) method than with the under-the-muscle (submuscular) method [S1].
- In studies with 4 or more years of follow-up, repeat surgery was needed after about 3% of transpositions, compared with about 12% of in situ decompressions [S3].
- Subcutaneous transposition has a low rate of symptoms coming back, but it leaves a larger scar and can delay return to work [S4].

## Explanation
### What it is
The ulnar nerve runs past the inner side of the elbow [S3]. In cubital tunnel syndrome, it is squeezed there, causing pain, numbness or tingling, and weakness or shrinking of the hand muscles it controls [S2]. In ulnar nerve transposition, the surgeon frees the nerve from the tissue pressing on it and moves it to the front of the medial epicondyle [S3]. There are three main versions [S2]:
- **Subcutaneous:** the nerve is placed just under the skin [S2].
- **Intramuscular:** the nerve is placed inside a muscle [S2].
- **Submuscular:** the nerve is placed under a muscle [S2].

### Why it is done
The goal is to relieve numbness and tingling, weakness or muscle loss, and pain caused by the squeezed nerve [S1]. Surgery is generally used when non-surgical treatment has failed [S4]. Transposition may be the better choice for some people, such as those whose symptoms started after an injury or whose nerve clearly slips out of place before surgery [S3]. For other people, there is no single best operation, and the choice often depends on the surgeon's preference and experience [S4][S5].

### How it is done
After the nerve is freed, it is moved in front of the inner elbow bone [S3]. Supporters of the under-the-skin method say it causes less pain after surgery, allows earlier movement, and lowers tension on the nerve [S2]. Supporters of the under-the-muscle method say the new spot has a healthy blood supply and protects the nerve with soft tissue [S2]. The sources here do not describe the steps of the operation in more detail, so ask your surgeon.

### Devices used
The sources here do not describe specific devices or instruments for this operation; ask your surgeon.

### Risks
In a review of 605 patients, side effects were about half as common with the under-the-skin method as with the under-the-muscle method [S1]. Subcutaneous transposition leaves a larger scar than simple decompression [S4]. One study found more health problems, more use of strong pain medicines, and more reported disability after transposition than after decompression [S3]. Other studies have found fewer complications with in situ decompression [S3]. On the other hand, repeat surgery seems less likely over the long term after transposition [S3].

### Recovery timeline
The sources here do not give a recovery schedule, so ask your surgeon what to expect. Subcutaneous transposition can mean a later return to work than simple decompression [S4]. The under-the-skin method is said to allow earlier movement after surgery than the under-the-muscle method [S2].

### Alternatives
- **Simple (in situ) decompression:** The nerve is freed but left in its normal place [S3]. It is gaining popularity because it leaves a smaller scar, takes less time, and allows an earlier return to work [S4]. A 2025 review found no clear difference in results between simple decompression and subcutaneous transposition, though decompression may lead to more recurrences and repeat surgeries [S4].
- **Medial epicondylectomy:** Part of the inner elbow bone is removed; this is generally only done when the bone shape is abnormal, such as after an injury [S5].
- **Non-surgical treatment:** Surgery is usually considered only after non-surgical treatment has not worked [S4].
- No technique has been shown to be better than all the others for everyone [S5].

## Common Misunderstandings
- **Myth:** Placing the nerve under a muscle always gives better results. **Fact:** Reviews found no clear difference in improvement between the under-the-muscle and under-the-skin methods [S1][S2].
- **Myth:** Moving the nerve is always better than leaving it in place. **Fact:** No clear winner has been found; transposition may need fewer repeat surgeries over time, but it can mean a bigger scar and a later return to work [S3][S4].
- **Myth:** Every person with cubital tunnel syndrome needs the nerve moved. **Fact:** Transposition is mainly preferred when the nerve slips out of place, and otherwise the choice depends on the surgeon and patient [S5][S4].

## Questions to Ask Your Doctor
1. Have I tried the non-surgical treatments that make sense for me?
2. Does my nerve slip out of place when I bend my elbow?
3. Why do you suggest moving the nerve instead of leaving it in place?
4. Will the nerve go under the skin or under a muscle, and why?
5. What problems should I watch for after surgery?
6. When can I go back to work and my usual activities?

## Test Questions
1. Where is the ulnar nerve moved during transposition? - To the front of the medial epicondyle (inner elbow bone) [S3].
2. Name the three main types of ulnar nerve transposition. - Subcutaneous, intramuscular, and submuscular [S2].
3. When is transposition generally preferred? - When the ulnar nerve slips out of place (subluxes) [S5].
4. Which method had fewer side effects in one review: subcutaneous or submuscular? - Subcutaneous [S1].
5. After 4 or more years, which operation needed repeat surgery more often? - In situ decompression (about 12%, vs about 3% for transposition) [S3].
6. Name one downside of subcutaneous transposition. - A bigger scar or a later return to work [S4].

## Related Topics
- Treats: Cubital Tunnel Syndrome (KO-HAND-COND-002)
- Alternative to: Cubital Tunnel Release (KO-HAND-PROC-003)
- Proposed new topics: Medial epicondylectomy (procedure), Medial epicondyle (anatomy), Ulnar nerve subluxation (condition), Recovery after ulnar nerve transposition (rehab protocol)

## References
1. [S1] Medicine. *Subcutaneous Versus Submuscular Anterior Transposition of the Ulnar Nerve for Cubital Tunnel Syndrome.* https://pmc.ncbi.nlm.nih.gov/articles/PMC4602994/ (retrieved 2026-10-26)
2. [S2] PLoS ONE. *Anterior Subcutaneous versus Submuscular Transposition of the Ulnar Nerve for Cubital Tunnel Syndrome: A Systematic Review and Meta-Analysis.* https://pmc.ncbi.nlm.nih.gov/articles/PMC4482721/ (retrieved 2026-10-26)
3. [S3] Cureus. *Higher Revision Rates With In Situ Decompression as Compared to Ulnar Nerve Transposition for Cubital Tunnel Syndrome: A Meta-Regression Analysis.* https://pmc.ncbi.nlm.nih.gov/articles/PMC11438553/ (retrieved 2026-10-26)
4. [S4] JSES Reviews, Reports, and Techniques. *Simple decompression vs. subcutaneous anterior transposition of the ulnar nerve: the 2025 update on the optimal treatment for cubital tunnel syndrome.* https://pmc.ncbi.nlm.nih.gov/articles/PMC12966733/ (retrieved 2026-10-26)
5. [S5] Frontiers in Surgery. *Surgical Approaches and Their Outcomes in the Treatment of Cubital Tunnel Syndrome.* https://pmc.ncbi.nlm.nih.gov/articles/PMC6071516/ (retrieved 2026-10-26)
