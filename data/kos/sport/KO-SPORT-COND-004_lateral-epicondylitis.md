---
schema_version: okds-ko-1.0
ko_id: KO-SPORT-COND-004
title: Lateral Epicondylitis
preferred_term: Lateral Epicondylitis
alternate_terms:
- tennis elbow
- lateral elbow tendinopathy
- lateral elbow pain (LEP)
- lateral epicondylalgia
- lateral epicondylosis
ko_type: Condition
specialty: SPORT
cluster: 2
audience:
- patient
- caregiver
reading_level: grade 6-8
difficulty: beginner
summary: Lateral epicondylitis, often called tennis elbow, is pain and tenderness on the outside of the
  elbow where forearm tendons attach to a bony bump called the lateral epicondyle [S3][S5]. It mostly
  comes from repeated gripping or bending the wrist back, in sports like tennis and in many jobs and hobbies
  [S2][S3][S5]. Most cases get better on their own, and treatment usually starts with rest and physical
  therapy exercises [S3][S5].
codes:
  mesh: <verify>
  icd10cm: <verify>
tags:
- elbow pain
- tennis elbow
- tendinopathy
- overuse injury
- repetitive strain
- physical therapy
- eccentric exercise
relationships:
- predicate: PREREQUISITE_FOR
  target_id: KO-HAND-TRT-002
  target_label: Corticosteroid Injection
  source_ids:
  - S1
  - S4
proposed_concepts:
- term: Lateral epicondyle and common extensor tendon (ECRB)
  suggested_type: AnatomicalStructure
  predicate: AFFECTS
  reason: S5 says the extensor carpi radialis brevis (ECRB) tendon at the lateral epicondyle is affected
    in nearly 90% of cases.
- term: Cozen test
  suggested_type: DiagnosticTest
  predicate: DIAGNOSED_BY
  reason: S4 lists the Cozen test as one of the most common tests used in studies of lateral elbow pain.
- term: Mill's test and Maudsley test
  suggested_type: DiagnosticTest
  predicate: DIAGNOSED_BY
  reason: S4 and S5 describe these pain-provoking exam tests for tennis elbow.
- term: Eccentric exercise / physiotherapy for tennis elbow
  suggested_type: Treatment
  predicate: PREREQUISITE_FOR
  reason: S4 and S5 describe exercise and physiotherapy as main conservative treatments.
- term: Counterforce brace (elbow strap)
  suggested_type: Device
  predicate: PREREQUISITE_FOR
  reason: S5 mentions taping and bracing as complementary treatments.
- term: Golfer's elbow (medial epicondylitis)
  suggested_type: Condition
  predicate: CONTRASTS_WITH
  reason: S1 and S2 name golfer's elbow as a separate form of elbow tendinitis.
sources:
- id: S1
  title: Tendinitis
  publisher: MedlinePlus, U.S. National Library of Medicine
  url: https://medlineplus.gov/tendinitis.html
  source_type: government_health_page
  audience: patient
  publication_date: '2026-09-01'
  retrieved_date: '2026-10-26'
  permitted_use: public_domain
  notes: 'From the OrthoInfo dataset (mplus:tendinitis). Licence: Public domain (NLM-authored MedlinePlus
    summary); credit MedlinePlus'
- id: S2
  title: Elbow Injuries and Disorders
  publisher: MedlinePlus, U.S. National Library of Medicine
  url: https://medlineplus.gov/elbowinjuriesanddisorders.html
  source_type: government_health_page
  audience: patient
  publication_date: '2025-09-23'
  retrieved_date: '2026-10-26'
  permitted_use: public_domain
  notes: 'From the OrthoInfo dataset (mplus:elbowinjuriesanddisorders). Licence: Public domain (NLM-authored
    MedlinePlus summary); credit MedlinePlus'
- id: S3
  title: 'Management of Lateral Epicondylitis: A Narrative Literature Review'
  publisher: Pain research & management
  url: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7222600/
  source_type: journal_article
  audience: clinician
  publication_date: '2020'
  retrieved_date: '2026-11-14'
  permitted_use: open_license
  notes: 'Found via europepmc. Licence: cc by. Type: review. Text kept: abstract only.'
- id: S4
  title: 'Treatment, Diagnostic Criteria and Variability of Terminology for Lateral Elbow Pain: Findings
    from an Overview of Systematic Reviews'
  publisher: Healthcare
  url: https://pmc.ncbi.nlm.nih.gov/articles/PMC9222841/
  source_type: journal_article
  audience: clinician
  publication_date: '2022'
  retrieved_date: '2026-10-26'
  permitted_use: open_license
  notes: 'From the OrthoInfo dataset (pmc:PMC9222841). Licence: CC BY'
- id: S5
  title: A Review of Physiotherapy Techniques Used in the Treatment of Tennis Elbow
  publisher: Cureus
  url: https://pmc.ncbi.nlm.nih.gov/articles/PMC10674892/
  source_type: journal_article
  audience: clinician
  publication_date: '2023'
  retrieved_date: '2026-10-26'
  permitted_use: open_license
  notes: 'From the OrthoInfo dataset (pmc:PMC10674892). Licence: CC BY'
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
  - 'Link check: the only registry link is PREREQUISITE_FOR Corticosteroid Injection (KO-HAND-TRT-002),
    a HAND-specialty KO. Confirm it covers elbow injections; otherwise remove the link.'
  - 'Source conflict: S1/S2 (MedlinePlus) call it tendinitis (inflammation), while S3 and S5 say it is
    mostly tendinosis (tendon breakdown). The KO explains both; confirm the wording.'
  - 'Source conflict: prevalence and age figures differ (S4: 1-3% prevalence, mostly ages 35-54; S5: 1-2%
    in studies, peak 35-55, also 10-30 per 1,000 adults per year). Confirm which to show.'
  - 'Source gap: no source gives specific "when to seek care" warning signs; the section says to ask a
    clinician.'
  - 'Source quality: S5 is a narrative review in Cureus with some unclear wording; S3 is abstract-only.'
  - MeSH ID and ICD-10-CM code are unknown and left as <verify>.
  - Plain-language definitions (tendon, tendinosis) were written partly by the drafter; check them.
safety:
  not_medical_advice: true
  scope_note: General education only. Not a diagnosis or treatment plan.
version: 0.1.0
created: '2026-11-14'
last_updated: '2026-11-14'
update_triggers:
- Any cited page shows a new 'last reviewed' date.
- A new systematic review or guideline on lateral elbow tendinopathy treatment or diagnostic criteria is
  published.
license: CC-BY-4.0
change_log:
- version: 0.1.0
  date: '2026-11-14'
  by: KO Collector + Claude (Claude Code session)
  change: Initial draft.
---

## Summary
Lateral epicondylitis, often called tennis elbow, is pain and tenderness on the outside of the elbow where forearm tendons attach to a bony bump called the lateral epicondyle [S3][S5]. It mostly comes from repeated gripping or bending the wrist back, in sports like tennis and in many jobs and hobbies [S2][S3][S5]. Most cases get better on their own, and treatment usually starts with rest and physical therapy exercises [S3][S5].

## Key Facts (claim → source)
- Tennis elbow is the most common cause of elbow pain and trouble using the elbow [S3].
- It affects the tendons that attach the forearm muscles to the outside of the elbow, most often one called the ECRB tendon [S5].
- It is named after tennis, but painters, plumbers, carpenters, gardeners, and people who type a lot can also get it [S1][S5].
- It most often starts between about ages 35 and 55 [S4][S5].
- It is usually diagnosed with a physical exam, and imaging is sometimes added to rule out other problems [S3][S4].
- Most cases heal on their own, but about 1 in 3 people still have pain after 12 months despite rehab [S3][S4].
- Steroid shots and platelet-rich plasma helped in the short term but led to worse long-term results than exercise [S4].
- Researchers use more than 10 names for this condition, which can make the research confusing [S4].

## Explanation
### What it is
Tendons are flexible bands of tissue that connect muscles to bones [S1]. In tennis elbow, the tendons of the forearm that attach at the lateral epicondyle, the bony bump on the outside of the elbow, become painful [S5]. In nearly 9 out of 10 cases, the affected tendon belongs to a wrist muscle called the extensor carpi radialis brevis (ECRB) [S5]. Health pages often describe it as tendinitis, meaning a swollen or injured tendon [S1][S2]. Research reviews say it is mostly tendinosis, a slow breakdown of the tendon with tiny tears, rather than simple swelling [S3][S5].

### Causes and risk factors
- **Repeated motions:** Overuse and repeated strain cause tiny tears or breakdown where the tendon attaches to the bone [S5]. Repeated gripping and bending the wrist back are the main triggers [S3].
- **Sports:** Elbow tendinitis is a sports injury, often from tennis or golf [S2].
- **Work and hobbies:** Repeated elbow bending and straightening, turning the forearm, lifting heavy loads, and bending the wrist back against force all play a part [S4]. Manual labor, typing, gardening, painting, woodwork, and heavy computer mouse use are linked to it [S5].
- **Age:** It mainly affects working adults between about 35 and 54 years old [S4].

### Symptoms
- Pain and tenderness on the outside of the elbow [S5].
- Pain that may spread down the forearm [S5].
- A weaker grip and trouble with tasks that use the wrist and hand [S5].
- Everyday actions, like lifting a coffee cup or shaking hands, can become very uncomfortable [S5].

The pain can last a long time and can make it hard to work [S4][S5].

### How it is diagnosed
Doctors diagnose tendon problems with a health history, a physical exam, and sometimes imaging tests [S1]. Tennis elbow is usually diagnosed by a clinical exam [S3][S5]. Common exam checks include pressing on the painful spot and tests that bring on the pain, such as the Cozen, Mill's, and Maudsley tests, along with a grip-strength test [S4][S5]. In the Maudsley test, the person straightens the middle finger against the examiner's push, and the test is positive if pain returns near the outer elbow [S5]. Ultrasound or MRI can help tell tennis elbow apart from other problems [S4]. There is not yet a proven set of tests that reliably sorts people with this condition [S4].

### Treatment options
Most cases can heal on their own, but the best treatment for long-lasting tennis elbow is still debated [S3].
- **First steps:** Rest, wrapping, raising the area, and medicines can help reduce pain and swelling, and ice helps for recent, severe injuries [S1].
- **Physical therapy:** Rest and strengthening exercises should be the main treatments [S5]. Common options include eccentric exercises (slowly lengthening the muscle under load), manual therapy, and treatments such as ultrasound [S4][S5].
- **Bracing and taping:** A splint is advised early on because it has few side effects, and taping and bracing can be added to therapy [S5].
- **Injections:** Steroid shots and platelet-rich plasma worked in the short term but led to worse long-term results than exercise [S4].
- **Surgery:** Surgery is an option for some people, and up to 5% of patients consider it [S1][S4].

### When to seek care
The sources here do not give specific warning signs, so ask a health care provider if elbow pain does not get better. They do show that tennis elbow can last a long time and make work and daily tasks hard, and that about 1 in 3 people still have symptoms after a year [S4][S5].

## Common Misunderstandings
- **Myth:** Only tennis players get tennis elbow. **Fact:** Anyone who grips and twists with the forearm a lot can get it, including manual workers, gardeners, and people who type [S5].
- **Myth:** Tennis elbow is just a swollen tendon. **Fact:** Reviews describe it mostly as tendon breakdown (tendinosis) with tiny tears, not only swelling [S3][S5].
- **Myth:** A steroid shot is the best long-term fix. **Fact:** Steroid shots helped short-term but had worse long-term results than exercise [S4].
- **Myth:** Tennis elbow always clears up quickly. **Fact:** About 1 in 3 people still had painful symptoms 12 months later despite rehab [S4].

## Questions to Ask Your Doctor
1. Is my elbow pain tennis elbow, or could it be something else?
2. Do I need an ultrasound or MRI?
3. Which exercises should I do, and how often?
4. Would a brace, strap, or tape help me?
5. What are the short-term and long-term pros and cons of a steroid shot?
6. What changes at work or in my hobbies could ease the strain on my elbow?

## Test Questions
1. Where is the pain in tennis elbow? - On the outside of the elbow, near the lateral epicondyle [S5].
2. Which tendon is most often affected? - The tendon of the extensor carpi radialis brevis (ECRB) muscle [S5].
3. Name two activities besides tennis linked to tennis elbow. - Examples: gardening, painting, carpentry, typing, or heavy mouse use [S1][S5].
4. How is tennis elbow usually diagnosed? - By a clinical exam, sometimes with imaging [S3][S4].
5. How did steroid shots compare with exercise over the long term? - Steroid shots led to worse long-term results [S4].
6. What does the Maudsley test check? - Whether straightening the middle finger against resistance brings back pain at the outer elbow [S5].

## Related Topics
- Read next: Corticosteroid Injection (KO-HAND-TRT-002)

## References
1. [S1] MedlinePlus, U.S. National Library of Medicine. *Tendinitis.* https://medlineplus.gov/tendinitis.html (retrieved 2026-10-26)
2. [S2] MedlinePlus, U.S. National Library of Medicine. *Elbow Injuries and Disorders.* https://medlineplus.gov/elbowinjuriesanddisorders.html (retrieved 2026-10-26)
3. [S3] Pain research & management. *Management of Lateral Epicondylitis: A Narrative Literature Review.* https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7222600/ (retrieved 2026-11-14)
4. [S4] Healthcare. *Treatment, Diagnostic Criteria and Variability of Terminology for Lateral Elbow Pain: Findings from an Overview of Systematic Reviews.* https://pmc.ncbi.nlm.nih.gov/articles/PMC9222841/ (retrieved 2026-10-26)
5. [S5] Cureus. *A Review of Physiotherapy Techniques Used in the Treatment of Tennis Elbow.* https://pmc.ncbi.nlm.nih.gov/articles/PMC10674892/ (retrieved 2026-10-26)
