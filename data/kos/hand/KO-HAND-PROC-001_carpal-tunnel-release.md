---
schema_version: okds-ko-1.0
ko_id: KO-HAND-PROC-001
title: Carpal Tunnel Release
preferred_term: Carpal Tunnel Release
alternate_terms:
- CTR
- open release
- endoscopic release
- carpal tunnel surgery
- open carpal tunnel release (OCTR)
- endoscopic carpal tunnel release (ECTR)
ko_type: Procedure
specialty: HAND
cluster: 5
audience:
- patient
- caregiver
- student
reading_level: grade 6-8
difficulty: beginner
summary: Carpal tunnel release is surgery for carpal tunnel syndrome. The surgeon cuts a ligament at the
  wrist so the carpal tunnel gets bigger and the median nerve is no longer squeezed [S1]. It can be done
  as open surgery or with a tiny camera (endoscopic surgery), and it is usually saved for severe symptoms
  or for symptoms that did not get better with other treatment [S1][S2].
codes:
  mesh: <verify>
  icd10cm: <verify>
tags:
- hand surgery
- wrist surgery
- carpal tunnel syndrome treatment
- median nerve
- open carpal tunnel release
- endoscopic carpal tunnel release
- outpatient surgery
- recovery after surgery
relationships:
- predicate: TREATS
  target_id: KO-HAND-COND-001
  target_label: Carpal Tunnel Syndrome
  source_ids:
  - S1
  - S2
  - S3
- predicate: ALTERNATIVE_TO
  target_id: KO-HAND-TRT-001
  target_label: Wrist Splinting
  source_ids:
  - S1
  - S2
- predicate: ALTERNATIVE_TO
  target_id: KO-HAND-TRT-002
  target_label: Corticosteroid Injection
  source_ids:
  - S1
  - S2
  - S4
- predicate: FOLLOWED_BY
  target_id: KO-HAND-REHAB-001
  target_label: Recovery After Carpal Tunnel Release
  source_ids:
  - S1
- predicate: MEASURED_BY
  target_id: KO-HAND-OUT-001
  target_label: Boston Carpal Tunnel Questionnaire
  source_ids:
  - S2
proposed_concepts:
- term: Endoscope (camera tube used in endoscopic carpal tunnel release)
  suggested_type: Device
  predicate: USES_DEVICE
  reason: S1 describes a camera attached to a tube and a small knife passed through it.
sources:
- id: S1
  title: 'Carpal Tunnel Syndrome: Diagnosis, Treatment, and Steps to Take'
  publisher: NIAMS (NIH)
  url: https://www.niams.nih.gov/health-topics/carpal-tunnel-syndrome/diagnosis-treatment-and-steps-to-take
  source_type: government_health_page
  audience: patient
  publication_date: 2023-12
  retrieved_date: '2026-11-01'
  permitted_use: public_domain
  notes: Page says "Last Reviewed December 2023". Pack keeps the treatment and self-care sections.
- id: S2
  title: 'Open versus endoscopic carpal tunnel release: a systematic review and meta-analysis of randomized
    controlled trials (Li et al.)'
  publisher: BMC Musculoskeletal Disorders, via PubMed Central
  url: https://pmc.ncbi.nlm.nih.gov/articles/PMC7187537/
  source_type: systematic_review
  audience: clinician
  publication_date: '2020-04-27'
  retrieved_date: '2026-11-01'
  permitted_use: open_license
  notes: CC BY 4.0. Li Y, Luo W, Wu G, Cui S, Zhang Z, Gu X. BMC Musculoskelet Disord. 2020;21:272. Accepted
    2020-04-21. Meta-analysis of 28 RCTs.
- id: S3
  title: 'Carpal Tunnel Syndrome: Pathophysiology and Comprehensive Guidelines for Clinical Evaluation
    and Treatment (Joshi et al.)'
  publisher: Cureus, via PubMed Central
  url: https://pmc.ncbi.nlm.nih.gov/articles/PMC9389835/
  source_type: journal_article
  audience: clinician
  publication_date: '2022-07-20'
  retrieved_date: '2026-11-01'
  permitted_use: open_license
  notes: CC BY. Joshi A, et al. Cureus. 2022;14(7):e27053. Narrative review; pack keeps the 'Treatment
    options' section only. One figure is CC BY-NC (not used).
- id: S4
  title: Update on Efficacy of Conservative Treatments for Carpal Tunnel Syndrome (Karjalanen et al.)
  publisher: Journal of Clinical Medicine, via PubMed Central
  url: https://pmc.ncbi.nlm.nih.gov/articles/PMC8877380/
  source_type: journal_article
  audience: clinician
  publication_date: '2022-02-11'
  retrieved_date: '2026-11-01'
  permitted_use: open_license
  notes: CC BY. Karjalanen T, Raatikainen S, Jaatinen K, Lusa V. J Clin Med. 2022;11(4):950. Accepted
    2022-02-09. Used for the non-surgical alternatives.
review:
  status: draft
  author: OKDS agent (Claude)
  generated_by:
    model: claude-opus-5-5
    prompt_version: okds-gen-1.0
  ai_check: null
  team_checker: null
  clinician_reviewer: null
  clinician_role: null
  review_date: null
  open_issues:
  - 'Clinician check: S1 (NIAMS) says endoscopic release has a higher risk of complications and repeat
    surgery, while S2 (meta-analysis of 28 RCTs) found more temporary nerve injury but no difference in
    permanent nerve injury and fewer scar problems. The KO reports both; confirm the wording is balanced.'
  - 'Clinician check: return-to-work, pinch strength, and satisfaction results come from one meta-analysis
    (S2, searched to 2019); confirm they still reflect current evidence.'
  - 'Clinician check: the statement that guidelines recommend surgery for people at risk of muscle wasting,
    lasting nerve damage, or job loss, and electrodiagnostic tests before surgery, is S3''s summary of
    the AAOS guideline, not the guideline itself. Consider adding the AAOS 2024 guideline (OrthoGuidelines)
    as a source.'
  - No public-domain source gives a detailed week-by-week recovery timeline; the Recovery timeline section
    is general. The A.D.A.M. MedlinePlus page (link_and_paraphrase) could add aftercare detail.
  - codes.mesh and codes.icd10cm are <verify>. ICD-10-CM codes diagnoses, not procedures; a procedure
    code system (e.g. CPT or ICD-10-PCS) may fit better. Do not fill without checking an official code
    source.
  - 'S1 publication_date is the month only (2023-12) because the page shows ''Last Reviewed: December
    2023''.'
safety:
  not_medical_advice: true
  scope_note: General education only. Not a diagnosis or treatment plan.
version: 0.1.1
created: '2026-11-01'
last_updated: '2026-11-14'
update_triggers:
- AAOS publishes or updates its carpal tunnel syndrome clinical practice guideline (surgery recommendations).
- The NIAMS carpal tunnel treatment page shows a new "Last Reviewed" date.
- A new systematic review or large trial compares open and endoscopic carpal tunnel release.
license: CC-BY-4.0
change_log:
- version: 0.1.0
  date: '2026-11-01'
  by: OKDS agent (Claude)
  change: Initial draft written by OKDS agent (Claude) (claude-opus-5-5, okds-gen-1.0) from source pack
    SP-KO-HAND-PROC-001.
- version: 0.1.1
  date: '2026-11-14'
  by: KO Collector + Claude (Claude Code session)
  change: 'Proposed concepts that now have KOs became relationships (same sources): followed by → Recovery
    After Carpal Tunnel Release (KO-HAND-REHAB-001); measured by → Boston Carpal Tunnel Questionnaire
    (KO-HAND-OUT-001)'
---

## Summary
Carpal tunnel release (CTR) is an operation for carpal tunnel syndrome (CTS) [S1]. In CTS, the median nerve, a nerve that gives feeling to the thumb side of the hand, is squeezed at the wrist [S2]. During CTR, the surgeon cuts a band of tissue called the carpal ligament so the tunnel gets bigger and the nerve has more room [S1]. There are two main ways to do it: open release and endoscopic release [S1][S2]. Doctors usually save surgery for severe symptoms or for people whose symptoms did not get better with non-surgical care [S2].

## Key Facts (claim → source)
- Carpal tunnel release is one of the most common surgeries in the United States [S1].
- The operation cuts a ligament at the wrist to take pressure off the median nerve [S1][S3].
- Open release uses one cut (incision) in the wrist; endoscopic release uses one or two small cuts and a tiny camera [S1].
- Open release is usually done with local anesthesia (medicine that numbs only the area being treated) as an outpatient procedure, so people usually go home the same day [S1].
- Symptoms may get better quickly, but full recovery can take months to years, depending on how severe the CTS was [S1].
- Possible risks include infection, nerve damage, stiffness, and pain at the scar [S1].

## Explanation
### What it is
The carpal tunnel is a narrow space at the wrist. The median nerve and the tendons that bend the fingers pass through it [S4]. Carpal tunnel release is surgery that makes this space larger by cutting the carpal ligament (also called the transverse carpal ligament), a tough band of tissue that holds joints together [S1][S2].

### Why it is done
The goal is to relieve the pressure on the median nerve [S1]. Surgery is generally saved for people with severe symptoms or for people whose symptoms did not improve with non-surgical treatment [S2]. A review explains that guidelines recommend surgery for people at risk of long-term problems, such as shrinking hand muscles (atrophy), lasting nerve damage, or not being able to keep doing their job [S3]. The same review says guidelines recommend nerve tests (electrodiagnostic studies) before surgery to confirm the diagnosis [S3]. Most people with mild to moderate symptoms try non-surgical treatment first, even though surgery may give stronger and longer-lasting relief [S4].

### How it is done
- **Open release:** This is the traditional method [S1]. The surgeon makes a cut in the wrist and then cuts the carpal ligament to enlarge the tunnel [S1]. It is generally done with local anesthesia as an outpatient procedure, which means you do not stay overnight in the hospital [S1].
- **Endoscopic release:** The surgeon makes one or two small cuts in the wrist and palm [S1]. A thin tube with a camera is put in so the surgeon can see the nerve, ligament, and tendons on a screen [S1]. Guided by that picture, the surgeon cuts the ligament with a small knife passed through the tube [S1]. Earlier studies described it as technically hard and linked it to the ligament sometimes not being fully cut [S2].

### Devices used
Endoscopic release uses an endoscope, which is a tube with a camera attached [S1]. The camera sends a picture to a monitor, and a small knife is passed through the tube to cut the ligament [S1].

### Risks
All surgeries carry risks [S1]. After carpal tunnel release, some people get an infection, nerve damage, stiffness, or pain at the scar [S1]. Open release has been linked to lasting weakness, pillar pain (one kind of pain after this surgery), thick or tender scars, slow recovery, and pain that lasts [S2]. NIAMS says endoscopic release carries a higher risk of complications and of needing repeat surgery [S1]. A review of 28 randomized trials found that endoscopic release caused more temporary (short-term) nerve injuries but fewer scar problems than open release [S2]. That review found no clear difference between the two methods in permanent nerve injury, and most nerve injuries got better [S2].

### Recovery timeline
Symptoms may ease soon after surgery [S1]. Full recovery depends on how severe the CTS was and can take months to years [S1]. Endoscopic release may allow faster recovery and less discomfort than open release [S1]. In the review of trials, people who had endoscopic release went back to work about one week sooner on average [S2]. They also had stronger pinch strength at 3 months and were more satisfied [S2]. In most people, surgery solves the problem for good [S1].

### Alternatives
- Wearing a splint on the hand and wrist at night is a common first treatment [S1].
- A steroid shot into the carpal tunnel can ease symptoms for a while [S1].
- These non-surgical treatments can help in the short term, but they do not fix the underlying problem with the median nerve [S1].
- Steroid shots may help some people put off surgery, but over several years many people still have surgery [S4].
- Health problems that can cause CTS, such as diabetes or arthritis, should be treated first [S1].

## Common Misunderstandings
- **Myth:** You are fully healed a few days after surgery. **Fact:** Symptoms may improve quickly, but full recovery can take months to years [S1].
- **Myth:** Endoscopic surgery has no downsides because the cuts are smaller. **Fact:** It can mean a faster return to work and fewer scar problems, but it has more temporary nerve injuries and, according to NIAMS, more complications and repeat surgeries [S1][S2].
- **Myth:** Everyone with carpal tunnel syndrome needs surgery right away. **Fact:** Non-surgical care is usually tried first for mild or moderate CTS, and surgery is mostly for severe symptoms or symptoms that do not improve [S2][S4].
- **Myth:** Carpal tunnel syndrome usually comes back after surgery. **Fact:** It is very rare for CTS to come back after surgery [S1].

## Questions to Ask Your Doctor
1. Have I tried the non-surgical treatments that make sense for me?
2. Do I need nerve tests before surgery?
3. Is open or endoscopic release a better fit for me, and why?
4. What problems should I watch for after surgery, and when should I call you?
5. When can I expect to go back to work and my usual activities?

## Test Questions
1. What does the surgeon cut during carpal tunnel release, and why? - The carpal (transverse carpal) ligament, to take pressure off the median nerve [S1][S2].
2. What are the two main types of carpal tunnel release? - Open release and endoscopic release [S1].
3. Who is carpal tunnel release usually for? - People with severe symptoms or whose symptoms did not improve with non-surgical treatment [S2].
4. Name two possible risks of carpal tunnel release. - Infection, nerve damage, stiffness, or pain at the scar [S1].
5. How long can full recovery take after carpal tunnel release? - Months to years, depending on how severe the CTS was [S1].
6. Compared with open release, what is one benefit of endoscopic release found in the review of trials? - Earlier return to work, higher satisfaction, better pinch strength, or fewer scar problems [S2].

## Related Topics
- Treats: Carpal Tunnel Syndrome (KO-HAND-COND-001)
- Alternative to: Wrist Splinting (KO-HAND-TRT-001), Corticosteroid Injection (KO-HAND-TRT-002)
- Proposed new topics: Endoscope (device), Recovery after carpal tunnel release (rehab protocol), Boston Carpal Tunnel Questionnaire (outcome measure)
- Background reading: Carpal Tunnel (KO-HAND-ANAT-002), Median Nerve (KO-HAND-ANAT-001), Nerve Conduction Study (KO-HAND-DX-001)
- followed by → Recovery After Carpal Tunnel Release (KO-HAND-REHAB-001)
- measured by → Boston Carpal Tunnel Questionnaire (KO-HAND-OUT-001)

## References
1. [S1] NIAMS (NIH). *Carpal Tunnel Syndrome: Diagnosis, Treatment, and Steps to Take.* https://www.niams.nih.gov/health-topics/carpal-tunnel-syndrome/diagnosis-treatment-and-steps-to-take (retrieved 2026-11-01)
2. [S2] BMC Musculoskeletal Disorders, via PubMed Central. *Open versus endoscopic carpal tunnel release: a systematic review and meta-analysis of randomized controlled trials (Li et al.).* https://pmc.ncbi.nlm.nih.gov/articles/PMC7187537/ (retrieved 2026-11-01)
3. [S3] Cureus, via PubMed Central. *Carpal Tunnel Syndrome: Pathophysiology and Comprehensive Guidelines for Clinical Evaluation and Treatment (Joshi et al.).* https://pmc.ncbi.nlm.nih.gov/articles/PMC9389835/ (retrieved 2026-11-01)
4. [S4] Journal of Clinical Medicine, via PubMed Central. *Update on Efficacy of Conservative Treatments for Carpal Tunnel Syndrome (Karjalanen et al.).* https://pmc.ncbi.nlm.nih.gov/articles/PMC8877380/ (retrieved 2026-11-01)
