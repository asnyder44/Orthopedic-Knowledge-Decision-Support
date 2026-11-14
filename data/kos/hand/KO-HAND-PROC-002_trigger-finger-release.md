---
schema_version: okds-ko-1.0
ko_id: KO-HAND-PROC-002
title: Trigger Finger Release
preferred_term: Trigger Finger Release
alternate_terms:
- A1 pulley release
- percutaneous trigger finger release
- trigger finger surgery
- open A1 pulley release
- percutaneous A1 pulley release (PAP)
- trigger thumb release
ko_type: Procedure
specialty: HAND
cluster: 5
audience:
- patient
- caregiver
reading_level: grade 6-8
difficulty: beginner
summary: Trigger finger release is surgery for trigger finger. The surgeon cuts a small band of tissue
  called the A1 pulley so the finger's tendon can glide freely again [S3]. It can be done through a small
  skin cut (open release) or with a small instrument passed through the skin (percutaneous release), and
  it is usually used when other treatments have not worked [S2][S3].
codes:
  mesh: <verify>
  icd10cm: <verify>
tags:
- hand surgery
- finger surgery
- trigger finger treatment
- A1 pulley
- open release
- percutaneous release
- outpatient surgery
- children's hand conditions
relationships:
- predicate: TREATS
  target_id: KO-HAND-COND-003
  target_label: Trigger Finger
  source_ids:
  - S1
  - S2
  - S3
  - S5
- predicate: ALTERNATIVE_TO
  target_id: KO-HAND-TRT-002
  target_label: Corticosteroid Injection
  source_ids:
  - S2
  - S3
proposed_concepts:
- term: A1 pulley
  suggested_type: AnatomicalStructure
  predicate: PREREQUISITE_FOR
  reason: S2 and S3 explain that trigger finger happens at the A1 pulley and that release surgery cuts
    it; an anatomy KO would help readers.
- term: Finger splinting for trigger finger
  suggested_type: Treatment
  predicate: ALTERNATIVE_TO
  reason: S2 and S3 list splinting of the finger joint as a non-surgical option; the registry only has
    Wrist Splinting (KO-HAND-TRT-001), which is a different treatment.
- term: Disabilities of the Arm, Shoulder and Hand (DASH) score
  suggested_type: OutcomeMeasure
  predicate: MEASURED_BY
  reason: S4 and S5 use DASH / QuickDASH scores to measure results after release.
- term: Recovery after trigger finger release
  suggested_type: RehabProtocol
  predicate: FOLLOWED_BY
  reason: The pack gives little detail on aftercare; a recovery KO would hold timing and warning signs.
sources:
- id: S1
  title: Trigger Thumb, Trigger Finger and Clasped Thumb
  publisher: Children
  url: https://pmc.ncbi.nlm.nih.gov/articles/PMC10969764/
  source_type: journal_article
  audience: clinician
  publication_date: '2024'
  retrieved_date: '2026-10-26'
  permitted_use: open_license
  notes: 'From the OrthoInfo dataset (pmc:PMC10969764). Licence: CC BY'
- id: S2
  title: 'Clinical Review of Trigger Finger in Pediatric and Adult Patients: Evaluation and Management
    Strategies'
  publisher: Cureus
  url: https://pmc.ncbi.nlm.nih.gov/articles/PMC12476290/
  source_type: journal_article
  audience: clinician
  publication_date: '2025'
  retrieved_date: '2026-10-26'
  permitted_use: open_license
  notes: 'From the OrthoInfo dataset (pmc:PMC12476290). Licence: CC BY'
- id: S3
  title: 'Percutaneous A1 pulley with corticosteroid injection for trigger finger release: a systematic
    review'
  publisher: Journal of Orthopaedic Surgery and Research
  url: https://pmc.ncbi.nlm.nih.gov/articles/PMC12042385/
  source_type: journal_article
  audience: clinician
  publication_date: '2025'
  retrieved_date: '2026-10-26'
  permitted_use: open_license
  notes: 'From the OrthoInfo dataset (pmc:PMC12042385). Licence: CC BY'
- id: S4
  title: Comparison of three different incision techniques in A1 pulley release on scar tissue formation
    and postoperative rehabilitation
  publisher: Archives of orthopaedic and trauma surgery
  url: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4842220/
  source_type: journal_article
  audience: clinician
  publication_date: '2016'
  retrieved_date: '2026-11-14'
  permitted_use: open_license
  notes: 'Found via europepmc. Licence: cc by. Type: trial. Text kept: abstract only.'
- id: S5
  title: 'Formation of multiple ganglion cysts along the flexor tendon after open A1 pulley release for
    trigger finger: A case report'
  publisher: Medicine
  url: https://pmc.ncbi.nlm.nih.gov/articles/PMC9302314/
  source_type: journal_article
  audience: clinician
  publication_date: '2022'
  retrieved_date: '2026-10-26'
  permitted_use: open_license
  notes: 'From the OrthoInfo dataset (pmc:PMC9302314). Licence: CC BY'
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
  - No patient-level page (MedlinePlus/NIAMS) on trigger finger release was found in the local dataset
    or the candidates; consider adding one (e.g. a MedlinePlus or AAOS OrthoInfo trigger finger page).
  - Only two relationships could be made to registry targets. Proposed concepts (A1 pulley, finger splinting,
    DASH score, recovery after trigger finger release) would allow more links.
  - 'Recovery timeline is thin: only S4 (DASH at 1, 3 and 12 months, 30 patients) and S3 (return to activity)
    give timing. No source gives a typical week-by-week aftercare plan; ask a clinician.'
  - Endoscopic and ultrasound-guided release are only named in S2's abstract; no details on how they are
    done or their results are in the pack.
  - S1 is mainly about children (trigger thumb); its statements that percutaneous release has more recurrence
    and nerve injury refer to children and must not be applied to adults. Clinician check of wording.
  - S3's 96.2% satisfaction figure is for percutaneous release combined with a steroid injection, from
    non-randomized studies; S2's '>90% success' is a narrative review summary. Clinician check that success
    rates are not overstated.
  - codes.mesh and codes.icd10cm are <verify>. ICD-10-CM codes diagnoses, not procedures; a procedure
    code system may fit better.
safety:
  not_medical_advice: true
  scope_note: General education only. Not a diagnosis or treatment plan.
version: 0.1.0
created: '2026-11-14'
last_updated: '2026-11-14'
update_triggers:
- A new systematic review or randomized trial compares open, percutaneous, or endoscopic trigger finger
  release.
- AAOS or another hand surgery body publishes or updates a trigger finger treatment guideline.
license: CC-BY-4.0
change_log:
- version: 0.1.0
  date: '2026-11-14'
  by: KO Collector + Claude (Claude Code session)
  change: Initial draft.
---

## Summary
Trigger finger release is an operation for trigger finger, a condition where a finger catches, locks, or hurts when it bends [S2]. The problem happens at the A1 pulley, a band of tissue near the base of the finger that holds the bending tendon (a cord linking muscle to bone) close to the bone [S2][S3]. During release, the surgeon cuts the A1 pulley so the tendon has more room to slide [S3]. Surgery is often seen as the last step, after other treatments have not worked [S3].

## Key Facts (claim → source)
- Trigger finger affects about 2% to 3% of people, most often women in their 50s and 60s [S2].
- Repeated hand tasks, diabetes, and rheumatoid arthritis raise the risk of trigger finger [S2].
- Open release, which uses a skin cut, is called the gold standard; it works in 90% to 100% of people, and the problem returns in 3% to 9% [S3].
- In percutaneous release, a small instrument is put through the skin to cut the pulley without an open cut [S3].
- Percutaneous release works about as well as open release and has a lower infection risk, but nerve damage is a possible problem [S3].
- In children with trigger thumb, open surgery gives the most reliable results [S1].
- Surgical options generally succeed in more than 90% of adults, with low rates of the problem coming back [S2].

## Explanation
### What it is
Trigger finger, also called stenosing tenosynovitis, happens when the covering around a finger's bending tendon becomes narrow and inflamed, most often at the A1 pulley [S2]. The A1 pulley sits near the palm side of the big knuckle at the base of the finger [S3]. Trigger finger release is surgery that cuts this pulley to widen the space the tendon passes through [S3]. The same idea is used for trigger thumb in children, where the operation releases the A1 pulley of the thumb [S1][S2].

### Why it is done
The goal is to stop the painful catching and locking so the finger can move smoothly again [S2][S3]. Many people first try non-surgical care such as splints, pain medicine, or a steroid shot [S3]. Surgery is usually offered when these treatments have not helped [S3]. Without treatment, trigger finger can get worse and make it hard to use the hand [S2]. In young children with trigger thumb, many cases get better on their own, so doctors may watch and wait first [S1]. Surgery is more likely to be advised when the thumb stays stiffly bent [S1].

### How it is done
- **Open release:** The surgeon makes a small cut in the skin, which can run across or along the finger [S3]. The surgeon moves the nearby nerves and blood vessels out of the way and then cuts the A1 pulley [S3]. A small study of 30 patients found no clear winner among three cut positions, though a lengthwise cut over the knuckle gave the fastest early recovery [S4].
- **Percutaneous release:** A small instrument is passed through the skin to cut the A1 pulley, with no open cut [S3]. Some doctors give a steroid shot at the same time [S3].
- **Other methods:** Ultrasound-guided and endoscopic (camera-guided) releases are also used [S2]. The sources here do not describe these methods in detail.

### Devices used
Percutaneous release uses a small cutting instrument put in through the skin [S3]. The sources here do not name specific devices.

### Risks
Open release is considered simple and has a very low rate of problems [S5]. Even so, it is not free of complications [S1]. Reported problems after open release in children include the pulley not being fully cut, wound problems, bowstringing (the tendon pulling away from the bone), nerve injury, and trouble fully bending or straightening the thumb [S1]. Percutaneous release can damage a nerve [S3]. In children, percutaneous release has a higher risk of the problem coming back and of nerve or tendon injury than open surgery [S1]. One rare case report described fluid-filled lumps (ganglion cysts) and a partly torn tendon in a finger after open release; these were treated with another operation [S5].

### Recovery timeline
In a small trial, people's hand function scores improved at 3 months and 12 months after surgery compared with before [S4]. In a review of release combined with a steroid shot, all patients in three studies returned to activity, sports, or work [S3]. The sources here do not give a detailed recovery schedule, so ask your surgeon what to expect.

### Alternatives
- Splinting the base of the finger can resolve symptoms in up to 65% of people after a year, but works less well for severe or long-lasting cases [S3].
- A steroid shot into the A1 pulley area reduces inflammation, but the problem can come back in up to half of people [S3].
- Steroid shots work less well in people with diabetes, long-standing trigger finger, or several fingers affected [S3].
- Other non-surgical options include anti-inflammatory pain medicines and shock wave therapy [S2].
- In children, watching and waiting, exercises, or splints may help some cases [S1][S2].

## Common Misunderstandings
- **Myth:** Trigger finger release is a big, risky operation. **Fact:** Open release is described as a simple procedure with a very low complication rate, though problems can still happen [S5][S1].
- **Myth:** If a steroid shot worked once, the trigger finger is gone for good. **Fact:** The problem can return in up to half of people after a steroid shot [S3].
- **Myth:** Every child with a bent thumb needs surgery right away. **Fact:** Many cases of trigger thumb in children get better on their own over time [S1].
- **Myth:** Percutaneous release has no downsides because there is no open cut. **Fact:** It has a lower infection risk, but nerve damage is a possible complication [S3].

## Questions to Ask Your Doctor
1. Have I tried the non-surgical treatments that make sense for me?
2. Would open or percutaneous release be better for me, and why?
3. What problems should I watch for after surgery?
4. When can I use my hand for work, sports, and daily tasks?
5. Does having diabetes or arthritis change my treatment options?
6. For a child: should we wait and watch before thinking about surgery?

## Test Questions
1. What structure is cut in trigger finger release? - The A1 pulley [S3].
2. How is percutaneous release different from open release? - A small instrument is put through the skin instead of making an open cut [S3].
3. How often does open release work, according to one review? - In about 90% to 100% of people [S3].
4. Name one possible complication of percutaneous release. - Nerve damage [S3].
5. Why might a doctor wait before operating on a young child's trigger thumb? - Many cases get better on their own [S1].
6. Name two non-surgical treatments for trigger finger. - Splinting, steroid shots, or anti-inflammatory pain medicines [S2][S3].

## Related Topics
- Treats: Trigger Finger (KO-HAND-COND-003)
- Alternative to: Corticosteroid Injection (KO-HAND-TRT-002)
- Proposed new topics: A1 pulley (anatomy), Finger splinting for trigger finger (treatment), DASH score (outcome measure), Recovery after trigger finger release (rehab protocol)

## References
1. [S1] Children. *Trigger Thumb, Trigger Finger and Clasped Thumb.* https://pmc.ncbi.nlm.nih.gov/articles/PMC10969764/ (retrieved 2026-10-26)
2. [S2] Cureus. *Clinical Review of Trigger Finger in Pediatric and Adult Patients: Evaluation and Management Strategies.* https://pmc.ncbi.nlm.nih.gov/articles/PMC12476290/ (retrieved 2026-10-26)
3. [S3] Journal of Orthopaedic Surgery and Research. *Percutaneous A1 pulley with corticosteroid injection for trigger finger release: a systematic review.* https://pmc.ncbi.nlm.nih.gov/articles/PMC12042385/ (retrieved 2026-10-26)
4. [S4] Archives of orthopaedic and trauma surgery. *Comparison of three different incision techniques in A1 pulley release on scar tissue formation and postoperative rehabilitation.* https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4842220/ (retrieved 2026-11-14)
5. [S5] Medicine. *Formation of multiple ganglion cysts along the flexor tendon after open A1 pulley release for trigger finger: A case report.* https://pmc.ncbi.nlm.nih.gov/articles/PMC9302314/ (retrieved 2026-10-26)
