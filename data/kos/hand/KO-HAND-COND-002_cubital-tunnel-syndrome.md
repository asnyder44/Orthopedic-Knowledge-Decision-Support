---
schema_version: okds-ko-1.0
ko_id: KO-HAND-COND-002
title: Cubital Tunnel Syndrome
preferred_term: Cubital Tunnel Syndrome
alternate_terms:
- ulnar nerve entrapment at the elbow
- ulnar neuropathy at the elbow
- UNE
- ulnar nerve compression at the elbow
ko_type: Condition
specialty: HAND
cluster: 2
audience:
- patient
- caregiver
- student
reading_level: grade 6-8
difficulty: beginner
summary: Cubital tunnel syndrome happens when the ulnar nerve is squeezed or irritated where it passes
  behind the inside of the elbow [S2]. It often causes numbness and tingling in the ring and little fingers,
  and it is the second most common trapped nerve in the arm after carpal tunnel syndrome [S1][S2][S3].
codes:
  mesh: <verify>
  icd10cm: <verify>
tags:
- elbow
- ulnar nerve
- funny bone
- numb ring finger
- numb little finger
- pinky tingling
- nerve entrapment
- hand weakness
relationships:
- predicate: DIAGNOSED_BY
  target_id: KO-HAND-DX-001
  target_label: Nerve Conduction Study
  source_ids:
  - S1
  - S2
- predicate: CONTRASTS_WITH
  target_id: KO-HAND-COND-001
  target_label: Carpal Tunnel Syndrome
  source_ids:
  - S1
  - S3
- predicate: AFFECTS
  target_id: KO-HAND-ANAT-003
  target_label: Ulnar Nerve
  source_ids:
  - S2
- predicate: AFFECTS
  target_id: KO-HAND-ANAT-004
  target_label: Cubital Tunnel
  source_ids:
  - S2
- predicate: DIAGNOSED_BY
  target_id: KO-HAND-DX-004
  target_label: Tinel's Sign
  source_ids:
  - S1
  - S2
proposed_concepts:
- term: Cubital Tunnel Release (in situ decompression)
  suggested_type: Procedure
  predicate: TREATS
  reason: Main surgery for this condition [S1][S2]; the link would point from the procedure to this KO.
- term: Ulnar Nerve Transposition
  suggested_type: Procedure
  predicate: TREATS
  reason: Surgery that moves the nerve in front of the elbow bump [S2][S3].
- term: Elbow Splinting (night elbow brace)
  suggested_type: Treatment
  predicate: TREATS
  reason: Common non-surgical treatment [S1][S2]. Wrist Splinting (KO-HAND-TRT-001) is a different treatment.
sources:
- id: S1
  title: 'Ulnar Neuropathy at the Elbow: From Ultrasound Scanning to Treatment'
  publisher: Frontiers in Neurology, via PubMed Central
  url: https://pmc.ncbi.nlm.nih.gov/articles/PMC8160369/
  source_type: journal_article
  audience: clinician
  publication_date: '2021-05-14'
  retrieved_date: '2026-11-01'
  permitted_use: open_license
  notes: Mezian K, Jacisko J, Kaiser R, et al. CC BY. Clinician review; pack keeps the abstract, introduction,
    risk factors, causes, diagnosis, non-surgical care, injection evidence, and surgery sections (anatomy
    detail, ultrasound technique, and figures removed). Accepted 2021-03-23.
- id: S2
  title: Ulnar Nerve Entrapment at the Elbow (Cubital Tunnel Syndrome)
  publisher: AAOS OrthoInfo
  url: https://www.orthoinfo.org/en/diseases--conditions/ulnar-nerve-entrapment-at-the-elbow/
  source_type: patient_education
  audience: patient
  publication_date: <verify>
  retrieved_date: '2026-11-01'
  permitted_use: link_and_paraphrase
  notes: Copyrighted. Paraphrased only. No review date shown on the page. Pack text is for internal review
    only; do not publish the pack.
- id: S3
  title: Surgical Approaches and Their Outcomes in the Treatment of Cubital Tunnel Syndrome
  publisher: Frontiers in Surgery, via PubMed Central
  url: https://pmc.ncbi.nlm.nih.gov/articles/PMC6071516/
  source_type: journal_article
  audience: clinician
  publication_date: '2018-07-26'
  retrieved_date: '2026-11-01'
  permitted_use: open_license
  notes: Carlton A, Khalid SI. CC BY. Pack keeps the abstract, introduction, and conclusions. Accepted
    2018-07-05.
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
  - Two of three sources are clinician-level research reviews (S1, S3). A clinician should check that
    the plain-language rewrites of research findings (risk factors, splint and injection evidence, surgery
    comparisons, up to 30% not improving after surgery) are accurate and not overstated.
  - S2 (AAOS OrthoInfo) is copyrighted (link_and_paraphrase). Its trimmed text is stored in the source
    pack for review only; do not publish the pack. Check that no sentence in the KO is copied from S2.
  - S2 shows no review date, so publication_date is '<verify>'.
  - MeSH ID and ICD-10-CM code are unknown ('<verify>'). Not stated in the sources.
  - 'S1 (research) and S2 (patient page) differ in tone on steroid injections: S2 says they are generally
    not used because of nerve risk; S1 reviews small studies with mixed results. A clinician should confirm
    the KO presents this fairly.'
  - Registry has no Ulnar Nerve, Cubital Tunnel, elbow splinting, or cubital tunnel surgery KOs, so AFFECTS
    and TREATS links are only in proposed_concepts.
safety:
  not_medical_advice: true
  scope_note: General education only. Not a diagnosis or treatment plan.
version: 0.1.1
created: '2026-11-01'
last_updated: '2026-11-14'
update_triggers:
- AAOS OrthoInfo updates its ulnar nerve entrapment (cubital tunnel syndrome) page.
- A new guideline or systematic review changes advice on splinting, injections, or surgery choice for
  cubital tunnel syndrome.
- Any cited page shows a new 'last reviewed' date.
license: CC-BY-4.0
change_log:
- version: 0.1.0
  date: '2026-11-01'
  by: OKDS agent (Claude)
  change: Initial AI draft written by the agent from source pack SP-KO-HAND-COND-002 (claude-opus-5-5,
    okds-gen-1.0).
- version: 0.1.1
  date: '2026-11-14'
  by: KO Collector + Claude (Claude Code session)
  change: 'Proposed concepts that now have KOs became relationships (same sources): affects → Ulnar Nerve
    (KO-HAND-ANAT-003); affects → Cubital Tunnel (KO-HAND-ANAT-004); diagnosed by → Tinel''s Sign (KO-HAND-DX-004)'
---

## Summary
Cubital tunnel syndrome happens when the ulnar nerve, one of the three main nerves in the arm, is squeezed or irritated behind the inside of the elbow [S2]. Doctors also call it ulnar neuropathy at the elbow, and it is the second most common trapped nerve in the arm, after carpal tunnel syndrome [S1][S3]. Most people can manage symptoms without surgery, but surgery may help when other care does not work [S2].

## Key Facts (claim → source)
- The most common place for the ulnar nerve to be squeezed is behind the inside of the elbow, near the spot people call the "funny bone" [S2].
- Typical symptoms are numbness and tingling in the ring finger and little finger [S1][S2].
- Bending the elbow stretches the nerve and lowers its blood supply, so symptoms are often worse with the elbow bent [S2].
- Treatment usually starts without surgery, for example changing activities and wearing a brace at night [S2].
- If the nerve is squeezed very hard or for a long time, hand muscles can waste away, and this cannot be undone [S2].
- Research has not shown that one type of surgery is clearly best for everyone [S1][S3].

## Explanation
### What it is
The cubital tunnel is a tunnel of tissue on the inside of the elbow that runs under a bony bump called the medial epicondyle [S2]. The nerve lies close to the skin there, which is why bumping your "funny bone" gives a shock-like feeling [S2]. The ulnar nerve gives feeling to the little finger and half of the ring finger, and it controls many small hand muscles used for fine movements and grip [S2]. The nerve is easy to squeeze at the elbow because it passes through a narrow space with little soft padding around it [S2].

### Causes and risk factors
Things that can put pressure on the nerve include:
- Keeping the elbow bent for a long time or bending it again and again, such as sleeping with bent elbows [S2].
- Leaning on the elbow for long periods [S2].
- The nerve sliding out from behind the bony bump each time the elbow bends [S2].
- Swelling in the elbow, cysts near the joint, bone spurs, arthritis, or a past broken or dislocated elbow [S2].
- Throwing sports such as baseball pitching [S2].

In many cases, the exact cause is not known [S2]. A research review also reports links with smoking, older age, being male, and work with vibrating hand tools [S1].

### Symptoms
- Numbness, tingling, or a "falling asleep" feeling in the ring and little fingers, often when the elbow is bent, such as while driving or holding a phone [S2].
- Symptoms that come and go, and waking at night with numb fingers [S2].
- An aching pain on the inside of the elbow [S2].
- Trouble with tasks like typing or doing up buttons [S1].
- In more severe cases, a weaker grip, clumsy fingers, and shrinking (wasting) of hand muscles [S1][S2].

### How it is diagnosed
A doctor asks about your health, work, and activities, then examines your elbow and hand to find which nerve is squeezed and where [S2]. The neck may be checked too, because a pinched nerve there can cause similar symptoms [S2]. The exam may include tapping over the nerve at the funny bone (Tinel's sign), but tapping can cause a shock feeling even in a normal nerve, so it is not proof by itself [S2].

Tests may include:
- **Nerve conduction studies**, which send a small electric signal along the nerve and look for spots where it slows down [S2]. They help show where the problem is, how bad it is, and rule out look-alikes such as carpal tunnel syndrome or a pinched nerve in the neck [S1].
- **X-rays**, which cannot show most causes but can find bone spurs or arthritis [S2].
- **Ultrasound**, which shows the nerve and nearby tissue, especially when the diagnosis is unclear [S1].

### Treatment options
**Without surgery.** Unless the nerve problem has already caused disability or muscle wasting, doctors usually suggest non-surgical care first [S2].
- **Changing habits:** avoid keeping the arm bent for long, avoid leaning on the elbow, and keep the elbow straight at night [S2]. In one trial, clear advice alone worked about as well as adding a night brace or nerve exercises [S1].
- **A padded brace or splint at night** to keep the elbow straight [S2]. A review found that advice plus splinting may help mild or moderate cases [S1].
- **Nerve gliding exercises**, which help the nerve slide; their benefit for this condition is not proven [S1][S2].
- **Steroid shots** are generally not used because they could harm the nerve [S2]. In one trial, a steroid shot did no better than a placebo (fake) shot [S1].

**Surgery.** Surgery may be suggested if other care has not helped, the nerve is badly squeezed, or the hand muscles are weak or damaged [S2]. People usually go home the same day [S2].
- **Cubital tunnel release** (also called in situ decompression): the surgeon cuts the tissue roof of the tunnel to give the nerve more room [S1][S2].
- **Ulnar nerve transposition**: the nerve is moved to the front of the bony bump so it does not stretch when the elbow bends [S2]. Experts tend to prefer this when the nerve slips out of place [S3].

Reviews found that the main surgery types all seem to work, and none is clearly better for everyone [S1][S3]. One large review found that simple release had fewer complications than moving the nerve [S1]. Nerves heal slowly, and some symptoms may remain if the nerve was badly damaged [S2]. Up to 30% of patients may not improve after surgery [S1].

### When to seek care
See a doctor if your symptoms are severe, or if milder symptoms have lasted more than 6 weeks [S2]. This matters because long-lasting pressure can cause permanent muscle loss in the hand [S2]. Without timely care, the condition can lead to lasting loss of feeling and weakness [S1].

## Common Misunderstandings
- **Myth:** Hitting your "funny bone" hurts a bone. **Fact:** The shock feeling comes from bumping the ulnar nerve, which lies close to the skin at that spot [S2].
- **Myth:** Cubital tunnel syndrome is just another name for carpal tunnel syndrome. **Fact:** They are different conditions, and doctors use nerve tests to tell them apart [S1][S3].
- **Myth:** A steroid shot is the usual fix. **Fact:** Steroid shots are generally not used for this condition because of a risk to the nerve, and one trial found they worked no better than a placebo shot [S1][S2].
- **Myth:** Surgery always makes the hand normal again. **Fact:** If the nerve was badly squeezed or muscles have wasted, some symptoms may stay after surgery [S2].

## Questions to Ask Your Doctor
1. Is my nerve being squeezed at the elbow, or could the problem be in my wrist or neck?
2. Do I need a nerve conduction study, X-ray, or ultrasound?
3. Which daily habits or sleep positions should I change?
4. Would a night brace help me, and how long should I wear it?
5. What signs would mean it is time to think about surgery, and which type would you suggest?

## Test Questions
1. Which nerve is squeezed in cubital tunnel syndrome, and where? - The ulnar nerve, behind the inside of the elbow [S2].
2. Which fingers usually feel numb or tingly? - The ring finger and the little finger [S1][S2].
3. Why are symptoms often worse when the elbow is bent? - Bending stretches the nerve and lowers its blood supply [S2].
4. What test sends a small electric signal along the nerve to find where it is squeezed? - A nerve conduction study [S2].
5. Why are steroid shots generally not used for cubital tunnel syndrome? - Because they carry a risk of harming the nerve [S2].
6. When should someone see a doctor? - If symptoms are severe, or if milder symptoms last more than 6 weeks [S2].

## Related Topics
- Diagnosed by: Nerve Conduction Study (KO-HAND-DX-001)
- Often confused with: Carpal Tunnel Syndrome (KO-HAND-COND-001)
- Proposed topics (not in the registry yet): Ulnar Nerve; Cubital Tunnel; Cubital Tunnel Release; Ulnar Nerve Transposition; Elbow Splinting; Tinel's Sign
- affects → Ulnar Nerve (KO-HAND-ANAT-003)
- affects → Cubital Tunnel (KO-HAND-ANAT-004)
- diagnosed by → Tinel's Sign (KO-HAND-DX-004)

## References
1. [S1] Frontiers in Neurology, via PubMed Central. *Ulnar Neuropathy at the Elbow: From Ultrasound Scanning to Treatment.* https://pmc.ncbi.nlm.nih.gov/articles/PMC8160369/ (retrieved 2026-11-01)
2. [S2] AAOS OrthoInfo. *Ulnar Nerve Entrapment at the Elbow (Cubital Tunnel Syndrome).* https://www.orthoinfo.org/en/diseases--conditions/ulnar-nerve-entrapment-at-the-elbow/ (retrieved 2026-11-01)
3. [S3] Frontiers in Surgery, via PubMed Central. *Surgical Approaches and Their Outcomes in the Treatment of Cubital Tunnel Syndrome.* https://pmc.ncbi.nlm.nih.gov/articles/PMC6071516/ (retrieved 2026-11-01)
