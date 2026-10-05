# Five-user qualitative pilot protocol — NOT RUN

Updated 2026-10-02. Canonical equivalent of requested **FIVE_USER_PILOT_PROTOCOL.md**; retains this existing filename and combines diary/first-use/final-check planning without a second protocol. **E0–E3 HUMAN VALIDATION PENDING.** No actual participants, consent, interviews, diaries, learning results, retention values or owner approval exist from this task. Phase 3 HOLD.

Purpose: understand circumstances, first-use comprehension, natural routine, useful return, estimated vs actual effort, support dependence, interruptions and progress trust. Five people can supply qualitative/descriptive cases, journey friction, terminology and bug discovery. They cannot establish statistical retention, learning efficacy, A/B superiority, ML validity or population outcome. Literature rationale: [RE18–RE20](MINGO_RESEARCH_EVIDENCE_REGISTER.md); definitions: [measurement framework](MINGO_PRODUCT_MEASUREMENT_FRAMEWORK.md).

## Readiness and scope gate

1. Real organizer approves recruitment/consent/contact, recording if any, coded storage/access, retention/deletion and voluntary withdrawal/redaction. Use five adults with relevant recent circumstances and variation described in the [discovery pack](INITIAL_WEDGE_RESEARCH_PLAN.md); no final target is frozen.
2. Day 0 fixture first-use/usability can study current presentation after human scheduling approval and clear disclosure. **Current Phase 2 fixtures cannot support natural product retention, durable offline reliability or real accepted learning outcomes.** Scripted fixture activity remains E1; repeated visits to a script are not E3.
3. Days 1–14 natural-use study requires an appropriately approved usable build, reviewed content/parallel tasks, safe actual save/assessment behavior, access/privacy procedures and reliable optional capture where used. Relevant later runtime gates must be satisfied without bypassing Phase 3 HOLD. Do not start Auth, sync, telemetry or production to make the pilot look ready.
4. E2 checks require independently reviewed claim/task/evidence, fresh items and conditions/provenance. Manual content checks can be a separately consented research task; they must not be reported as a product-scored outcome or product-caused gain. Stop/adjust if core integrity, access or participant safety problems occur.

Current disposition: protocol PREPARED; scheduling/consent/content review PENDING; current fixture walkthrough available for E1 only; natural-use E2/E3 run NOT RUN, dependent on appropriate future readiness. No recruitments or messages were sent.

## Study schedule — proposed, not memory optimum

| Time | Activities | Evidence and limitations |
|---|---|---|
| **Day 0** | Consent and context interview; recent goal/alternatives; first-use/core-loop think-aloud; optional baseline fresh task before relevant exposure | Use [usability protocol](PHASE2_USABILITY_TEST_PROTOCOL.md). Record prior knowledge/exposure, moderator help and fixture boundary. Baseline/check tasks need content review |
| **Days 1–14** | Voluntary natural use when appropriate; purpose-approved optional telemetry if reliable/implemented later; very brief optional diary after an attempt | No daily quota, forced five-minute duration, streak penalty or coaching to return. Capture attempted/blocked/not used and alternatives; missing entry stays missing |
| **Midpoint, around Day 7** | Case review and optional neutral follow-up on unexplained behavior/technical issues; optional fresh delayed check only if predeclared and consented | Ask for context, not “why are you unmotivated?” Record researcher contact/reminder because it can affect return. Day 7 is a protocol occasion, not an optimal spacing claim |
| **Final, around Day 14** | Reviewed fresh delayed independent tasks; changed-context tasks; interview on useful value, return/abandonment, support, progress and save/sync understanding | Record actual elapsed intervals, assessment conditions and missing tasks. Parallel-item equivalence/transfer scope require review. Day 14 is not a universal memory optimum |

Avoid daily recall drills disguised as diary prompts: repeated assessment itself changes exposure/learning. Predeclare which tasks and delays are evaluated; record any unscheduled practice or assistance. If a participant never returns or withdraws, record coverage and any voluntarily supplied reason; do not invent a final score.

## Minimal diary prompts — optional, approximately 1–2 minutes

After a real attempted use: What did you want to do? What happened or blocked you? Roughly how much active time did it take, and was there an interruption? Did you use support or replay? Was anything about saved/pending/confirmed status unclear? Why did you return or choose another alternative? One optional note about usefulness/effort; no health/emotion diagnosis or required sensitive free text.

No entry required when there was no use. If asking about non-use, ask neutrally at a scheduled check-in and record the intervention. Do not send pressure notifications or teach participants the desired answers. Participant time estimates and reliable runtime active/wall durations remain different sources.

Blank diary CSV header, with no populated participant rows:

```csv
day,participant_code,entry_source,attempted_goal,coarse_context,task_or_stage,minutes_estimate,interruption,completed_or_blocked,assistance_used,offline_or_media_issue,save_status_understood,return_or_alternative_reason,optional_usefulness_note,missing_reason_if_volunteered,build_content_revision
```

Separate learning-check sheet: `participant_code | objective | reviewed_item/revision | occasion | actual_elapsed_interval | prior_exposure | task/context/modality | assistance/replay_condition | first_response_evidence | accepted/manual_source | outcome | unavailable/missing_reason | reviewer_ref`. Do not put raw answers, voice or sensitive diary text into telemetry. No speaking-recording feature is introduced.

## Final interview and readback

Ask for a concrete useful/not useful case; what improved or remained difficult; what prompted return and what caused stopping; actual alternatives; any pressure or unnecessary time; how support helped and whether the later fresh task felt independent; what progress means; and local saved versus server acknowledged. Use neutral examples from actual observed cases, including counterexamples. Optional opinion does not prove learning; correct post-check does not prove gain caused by Mingo.

## Data handling and analysis

Keep coded participation/contact/consent separate, minimize fields, restrict access and implement the organizer-approved deletion schedule before collection. Participant can decline optional recording/telemetry, redact notes and withdraw according to the stated process. TTL is PENDING; no claim that a deletion system exists. Record telemetry-disabled/offline/late-capture circumstances so missing data is not scored as failure. [Purpose register](TELEMETRY_PURPOSE_REGISTER.md) is a proposal, not a runtime collector.

Analyze individual trajectories and themes with counts of observed/assisted/failed/not attempted occasions, exact denominators, missingness, quotations if consented and counterexamples. Separate human observation, self-report, authoritative runtime and fixture source. Include self-selection, small sample, researcher contact, prior knowledge, repeated testing, content validity and fixture-vs-natural-use confounds. Do not use p-values, population percentages or claims of retention/efficacy/ML success.

Handoff after a real study: attendance/consent references; case timeline; task evidence; diary and fresh-check coverage; findings/severity; technical/content/context alternatives; correction owner and retest; limitations; actual Product Owner decision. All participant/result/signoff fields remain **PENDING** today.
