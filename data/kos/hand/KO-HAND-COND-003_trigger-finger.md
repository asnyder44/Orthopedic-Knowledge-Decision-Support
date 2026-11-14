---
schema_version: okds-ko-1.0
ko_id: KO-HAND-COND-003
title: Trigger Finger
preferred_term: Trigger Finger
alternate_terms:
- stenosing tenosynovitis
- stenosing flexor tenosynovitis
ko_type: Condition
specialty: HAND
cluster: 2
audience:
- patient
- caregiver
reading_level: grade 6-8
difficulty: beginner
summary: Trigger finger is a common hand problem in which a tendon that bends a finger catches or locks
  as it slides through its tunnel-like sheath, so the finger may click, lock, or hurt when it bends and
  straightens [S1][S2][S3]. It is more common in women, in middle age, and in people with diabetes [S2][S4].
  Treatment ranges from splints and steroid shots to a small surgery that frees the tendon [S2][S4].
codes:
  mesh: <verify>
  icd10cm: <verify>
tags:
- finger locking
- finger clicking
- flexor tendon
- A1 pulley
- diabetes
- steroid injection
relationships:
- predicate: PREREQUISITE_FOR
  target_id: KO-HAND-PROC-002
  target_label: Trigger Finger Release
  source_ids:
  - S2
  - S4
  - S5
- predicate: PREREQUISITE_FOR
  target_id: KO-HAND-TRT-002
  target_label: Corticosteroid Injection
  source_ids:
  - S2
  - S5
- predicate: CONTRASTS_WITH
  target_id: KO-HAND-COND-005
  target_label: Dupuytren Contracture
  source_ids:
  - S1
proposed_concepts:
- term: A1 pulley (flexor tendon sheath)
  suggested_type: AnatomicalStructure
  predicate: AFFECTS
  reason: S2, S3, and S4 name the A1 pulley of the flexor tendon sheath as the usual site of trigger finger;
    it is not in the registry.
- term: Finger splinting for trigger finger
  suggested_type: Treatment
  predicate: PREREQUISITE_FOR
  reason: S2 and S4 list splinting as a non-surgical treatment; Wrist Splinting (KO-HAND-TRT-001) is about
    the wrist, not the finger.
- term: Finger locking or catching
  suggested_type: Concept
  predicate: HAS_SYMPTOM
  reason: Main symptom in S1-S4; needs a Concept KO before a HAS_SYMPTOM link can be made.
sources:
- id: S1
  title: Finger Injuries and Disorders
  publisher: MedlinePlus, U.S. National Library of Medicine
  url: https://medlineplus.gov/fingerinjuriesanddisorders.html
  source_type: government_health_page
  audience: patient
  publication_date: '2025-12-03'
  retrieved_date: '2026-10-26'
  permitted_use: public_domain
  notes: 'From the OrthoInfo dataset (mplus:fingerinjuriesanddisorders). Licence: Public domain (NLM-authored
    MedlinePlus summary); credit MedlinePlus'
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
  title: 'Misconceptions about trigger finger: a scoping review. Definition, pathophysiology, site of
    lesion, etiology. Trigger finger solving a maze'
  publisher: Advances in Rheumatology
  url: https://pmc.ncbi.nlm.nih.gov/articles/PMC13488632/
  source_type: journal_article
  audience: clinician
  publication_date: '2024'
  retrieved_date: '2026-10-26'
  permitted_use: open_license
  notes: 'From the OrthoInfo dataset (pmc:PMC13488632). Licence: CC BY'
- id: S4
  title: 'Trigger finger: etiology, evaluation, and treatment'
  publisher: Current reviews in musculoskeletal medicine
  url: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2684207/
  source_type: journal_article
  audience: clinician
  publication_date: '2008'
  retrieved_date: '2026-11-14'
  permitted_use: link_and_paraphrase
  notes: 'Found via europepmc. Licence: cc by-nc. Type: article. Text kept: abstract only.'
- id: S5
  title: 'Conservative management of trigger finger with steroid injections: A narrative literature review'
  publisher: Journal of Orthopaedic Reports
  url: http://www.sciencedirect.com/science/article/pii/S2773157X25003029
  source_type: journal_article
  audience: clinician
  publication_date: '2026'
  retrieved_date: '2026-11-14'
  permitted_use: link_and_paraphrase
  notes: 'Found via doaj. Licence: open access journal (licence per article: <verify>). Type: review.
    Text kept: abstract only.'
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
  - No patient-level page (MedlinePlus/NIAMS) in the dataset is dedicated to trigger finger; S1 has only
    a one-line definition. Consider adding a MedlinePlus or NIAMS trigger finger page.
  - 'Clinician check: success figures for a first steroid shot differ between sources (S2: 70%-90% in people
    without diabetes; S5: 45%-80%). The KO states both as ranges; confirm the wording.'
  - The sources do not give clear 'when to seek care' warning signs; that section is written from S2 and
    S4 (untreated disease can worsen; other problems must be ruled out). Clinician should review.
  - S4 is from 2008 and S5 is abstract-only with an unconfirmed licence (link_and_paraphrase); S2 and S3
    are full-text CC BY but only the first sections were kept in the pack.
  - MeSH ID and ICD-10-CM code are not stated in any source; left as verify.
  - Short plain-language definitions of terms (e.g., 'sheath', 'pulley') were written by the drafter; check
    they match the sources.
safety:
  not_medical_advice: true
  scope_note: General education only. Not a diagnosis or treatment plan.
version: 0.1.0
created: '2026-11-14'
last_updated: '2026-11-14'
update_triggers:
- MedlinePlus publishes a new 'last updated' date for its Finger Injuries and Disorders page.
- A new systematic review or guideline compares steroid injection, splinting, and surgery for adult trigger
  finger.
license: CC-BY-4.0
change_log:
- version: 0.1.0
  date: '2026-11-14'
  by: KO Collector + Claude (Claude Code session)
  change: Initial draft.
---

## Summary
Trigger finger is a common hand problem in which a tendon that bends a finger catches or locks as it slides through its tunnel-like sheath, so the finger may click, lock, or hurt when it bends and straightens [S1][S2][S3]. It is more common in women, in middle age, and in people with diabetes [S2][S4]. Treatment ranges from splints and steroid shots to a small surgery that frees the tendon [S2][S4].

## Key Facts (claim → source)
- Trigger finger happens when the flexor tendon (the cord that bends the finger) cannot slide smoothly through its sheath, most often at a band called the A1 pulley [S1][S2][S3].
- The finger may pop, click, catch, or lock when it bends and straightens, and it can be painful [S3][S4].
- About 2% to 3% of people get trigger finger, and the chance is much higher in people with diabetes [S2][S3].
- It is seen more often in women and in people in the fifth and sixth decades of life (about ages 40 to 60) [S2][S4].
- Diagnosis is usually based on the history and exam, but other problems such as a broken bone or a growth must be ruled out [S4].
- Non-surgical options include anti-inflammatory medicines, splints, and steroid shots, and how well they work depends on how severe the problem is [S2][S5].
- Surgery to release the pulley is the most definitive treatment, and one review reports success rates above 90% [S2][S5].

## Explanation
### What it is
The flexor tendons are the cords that bend the fingers, and each one glides through a tunnel of tissue called a sheath [S1][S2]. The A1 pulley is a firm band that forms part of this sheath at the base of the finger [S2][S3]. In trigger finger, the tendon and its tunnel no longer fit well, because the pulley gets thicker or the tendon swells [S2][S3]. The tendon then catches and releases like the trigger of a gun [S1]. The first band at the base of the finger, the A1 pulley, is the most common trouble spot, but other places can be involved [S2][S3].

Trigger finger is also called stenosing tenosynovitis, which means a narrowed and swollen tendon sheath [S2]. One review notes that swelling from inflammation is not found in every case, so this name may not fit everyone [S3].

### Causes and risk factors
Trigger finger usually has more than one cause [S3]. Factors linked to it include [S2][S4]:
- Doing the same hand and finger motions over and over [S2].
- Diabetes, which raises the chance of trigger finger to about 5% to 20% in some estimates [S3].
- Rheumatoid arthritis and other types of inflammatory arthritis (diseases where the immune system inflames joints) [S2].
- Being a woman, and being in the fifth or sixth decade of life [S2][S4].

In children, trigger finger is uncommon and usually shows up in babies or young children, sometimes along with other health conditions [S2].

### Symptoms
- Pain in the affected finger [S2][S4].
- Popping, clicking, or catching when the finger bends and straightens [S3][S4].
- A finger that locks, and loss of motion [S2][S4].

Mild symptoms can stay mild, but if trigger finger is not treated it can get worse and make it hard to use the hand [S2].

### How it is diagnosed
The diagnosis is usually fairly simple, because most people describe clicking or locking of the finger [S4]. A health care provider also needs to rule out other causes, such as a fracture (broken bone), a tumor, or another injury to the soft tissues [S4]. One review advises checking all the places along the tendon where catching can happen, not only the A1 pulley [S3]. Ultrasound imaging has been used in studies to look for a thick pulley, a swollen tendon, or fluid in the sheath [S3].

### Treatment options
Treatment depends on how severe the problem is and how long it has lasted [S4].
- **Non-surgical care:** options include anti-inflammatory medicines, splinting, and shock wave therapy (sound-wave treatment) [S2]. How well they work varies with the severity of the disease and other health problems [S2].
- **Steroid shot:** a corticosteroid injection near the tendon is the most widely used non-surgical treatment [S5]. Reported success after a first shot ranges from about 45% to 80% in one review, and 70% to 90% in people without diabetes in another [S2][S5]. The problem can come back, and the chance of it returning goes up with repeated shots [S2][S5]. Involvement of several fingers or more advanced disease makes a shot less likely to work [S5].
- **Surgery (trigger finger release):** a surgeon cuts the tight pulley so the tendon can glide, through an open cut, a needle (percutaneous), a small camera (endoscopic), or with ultrasound guidance [S2]. Surgery is the most definitive treatment, with success rates above 90% and a low chance of coming back [S2][S5].

In children, watching and waiting or splinting helps in some cases, and surgery to release the A1 pulley resolves most cases [S2].

### When to seek care
The sources here do not list specific warning signs, so ask a clinician which symptoms need prompt attention. A finger that clicks, catches, or locks is worth checking with a health care provider, because untreated trigger finger can get worse and other problems, such as a broken bone or a growth, need to be ruled out [S2][S4].

## Common Misunderstandings
- **Myth:** Trigger finger is always caused by inflammation. **Fact:** One review found that signs of inflammation are not present in every case, and a size mismatch between the tendon and its pulley is the common problem [S3].
- **Myth:** Trigger finger only happens at the base of the finger. **Fact:** The A1 pulley is the most common site, but catching can happen at other points along the tendon [S3].
- **Myth:** One steroid shot always fixes trigger finger for good. **Fact:** Many people improve after a shot, but symptoms can return, especially after repeated shots [S2][S5].
- **Myth:** Only adults get trigger finger. **Fact:** It is uncommon in children, but it does happen, usually in babies or young children [S2].

## Questions to Ask Your Doctor
1. Is my finger problem trigger finger, or could something else be causing it?
2. Do I need an ultrasound or any other test?
3. Would a splint or a steroid shot be a reasonable first step for me?
4. Could my diabetes or arthritis affect how well treatment works?
5. When would trigger finger release surgery make sense, and what would recovery involve?

## Test Questions
1. What happens to the tendon in trigger finger? - It catches as it slides through a narrowed sheath, often at the A1 pulley, and then releases like a trigger [S1][S2].
2. Name two groups of people who are more likely to get trigger finger. - Examples: women, people with diabetes, and people about 40 to 60 years old [S2][S4].
3. What other problems should a provider rule out? - Fractures, tumors, and other soft tissue injuries [S4].
4. What is the most widely used non-surgical treatment for adult trigger finger? - A corticosteroid (steroid) injection [S5].
5. What does trigger finger release surgery do? - It cuts the tight pulley so the tendon can glide again [S2].

## Related Topics
- Read next: Trigger Finger Release (KO-HAND-PROC-002), Corticosteroid Injection (KO-HAND-TRT-002)
- Often confused with: Dupuytren Contracture (KO-HAND-COND-005)

## References
1. [S1] MedlinePlus, U.S. National Library of Medicine. *Finger Injuries and Disorders.* https://medlineplus.gov/fingerinjuriesanddisorders.html (retrieved 2026-10-26)
2. [S2] Cureus. *Clinical Review of Trigger Finger in Pediatric and Adult Patients: Evaluation and Management Strategies.* https://pmc.ncbi.nlm.nih.gov/articles/PMC12476290/ (retrieved 2026-10-26)
3. [S3] Advances in Rheumatology. *Misconceptions about trigger finger: a scoping review. Definition, pathophysiology, site of lesion, etiology. Trigger finger solving a maze.* https://pmc.ncbi.nlm.nih.gov/articles/PMC13488632/ (retrieved 2026-10-26)
4. [S4] Current reviews in musculoskeletal medicine. *Trigger finger: etiology, evaluation, and treatment.* https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2684207/ (retrieved 2026-11-14)
5. [S5] Journal of Orthopaedic Reports. *Conservative management of trigger finger with steroid injections: A narrative literature review.* http://www.sciencedirect.com/science/article/pii/S2773157X25003029 (retrieved 2026-11-14)
