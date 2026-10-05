# Independent verification protocol — IV&V-lite

Scope: Phase2 candidate interaction/presentation and preserved V3.2/Phase1 boundaries. Development tests, an agent challenge review, golden regression, independent human QA and Product Owner approval are separate evidence sources. This protocol is preparation; independent acceptance is **PENDING**. Phase3 **HOLD**.

## Reviewer authority and independence

Before opening implementation internals, a reviewer derives expected outcomes from the unchanged V3.2 contracts, [MVP_PRD](../../../MVP_PRD.md), the owner's current directive and the learner/staff task. Record a short oracle: action, expected observable outcome, forbidden outcome and authoritative source. Reading production code may help locate a defect later but must not define the expected product rule.

Use a candidate identified by source/asset manifest, build mode, Flutter version, OS/device/browser, viewport, font scale and evidence timestamp. Preserve the candidate and failures. A correction creates a new candidate and selective retest. Do not replace historical reports or regenerate their seals. Reviewers submit findings; they do not automatically edit production code, modify original contracts, self-sign a human gate or begin the next phase.

An agent assigned a different review task remains part of the development team. Its findings can challenge implementation assumptions; they cannot be labelled independent human acceptance. Human reviewer identity, real observations and signed dispositions are required for that gate.

## Five validation layers

| Layer | Required evidence | What it cannot prove |
|---|---|---|
| Behavior | Requirements-derived functional and adversarial cases | Ease of use or learning efficacy |
| Semantics/accessibility | Labels, traversal, 48dp, contrast, 200% text, keyboard and reduced-motion checks; actual TalkBack core journey | Automated semantics alone do not prove spoken output/traversal works on a device |
| Responsiveness | 360/common mid-size/larger Android and text scales 1/1.3/1.5/2; empty/offline/error/long Vietnamese copy | One screenshot is not every scroll/focus state |
| Visual regression | Reviewed technical candidate and explicit baseline update reason; captured source/asset hashes | Matching pixels do not approve art direction |
| Product/art direction | Product Owner and content reviewer inspect actual task flow and candidate; real usability observations | Liking the visuals does not prove reliability or delayed learning |

## Requirement-derived adversarial cases

The expected behaviors below were derived from PRD/V3.2 before checking implementation. Tests exercise exported app entry points and visible actions, not private fixture fields.

| ID / source | Attack or edge case | Expected observable outcome | Forbidden outcome | Execution |
|---|---|---|---|---|
| IV-01 / PRD-02/03 | Submit wrong Check answer, then tap a different answer after feedback | First outcome remains; no Check hint/retry/skip | Late tap converts first wrong into correct or unaided success | independent_test.dart; RERUN NOW PASS — candidate_tests_final.jsonl |
| IV-02 / PRD-04 + Android navigation | Skip Retrieve, explicitly Continue, then Android system Back | Honest skipped/unanswered state; sample boundary and safe navigation | Correct/incorrect first-response feedback invented from skip | independent_test.dart; RERUN NOW PASS — candidate_tests_final.jsonl |
| IV-03 / PRD-14 | Directly initialize publication confirmation without license/review evidence | Recover to source/review; no actionable confirmation | Caller-selected route bypasses sample prerequisites or implies real publication | independent_test.dart; RERUN NOW PASS; pre-fix FAIL preserved |
| IV-04 / V3 server authority + PRD-10 | Open no-evidence learner detail | Missing evidence explicitly stated; no sample answer promoted into evidence | Fabricated answer/score/mastery/risk displayed as real | independent_test.dart; RERUN NOW PASS — candidate_tests_final.jsonl |
| IV-05 / PRD-16 | Recommendation unavailable | Valid curriculum next action remains usable with sample boundary | Empty/broken cycle solely because ML/recommendation is off | independent_test.dart; RERUN NOW PASS — candidate_tests_final.jsonl |
| IV-06 / PRD-02/07 | Hint or wrong-first retry followed by success, then request step-up | Retain assistance and first response; insufficient threshold cannot authorize real unlock | Single/retried/assisted success becomes mastery or higher objective eligibility | Existing fixture checks plus human journey; production engine NOT IMPLEMENTED |
| IV-07 / V3 immutable revisions | Edit new draft after a published revision exists | Published old title/revision and pinned attempt retain prior content | Draft overwrites published revision or reinterprets old attempts | Existing fixture checks; production publication/pinning NOT IMPLEMENTED |
| IV-08 / V3 command != telemetry | Telemetry delivery precedes command acknowledgement | Separate states and explicit authority; unknown ack remains unknown | Telemetry/play/open authorizes canonical completion | Visual state review now; durable runtime fault test deferred Phase6 |
| IV-09 / V3 offline deadlines/pins | Submit, kill, restart offline, reconnect, duplicate retry; revision changes; oscillating network/delayed ack | Preserve durable command and exact revision; idempotent canonical result | Lost work, duplicate progress/reward, silently switched revision | Phase6 scenario specification; NOT RUN, runtime absent |
| IV-10 / V3 permission | Denied object access; untrusted learner/device/grant IDs | Hidden learner evidence; server identity/scope authority | UI navigation interpreted as auth or a grant ID grants access | Presentation denial test; real auth NOT IMPLEMENTED/Phase3 HOLD |
| IV-11 / PRD-01 + short-session hypothesis | Pause, abandon and resume longer than estimated duration | Estimate remains estimate; finite cycle and optional next step | Timer terminates unfinished answer or next session starts without opt-in | Human task, NOT RUN |
| IV-12 / accessibility | Full core journey with actual TalkBack, 200% text, reduced motion; staff keyboard/dialog focus | Usable names/order/error/offline announcements and recovery | Unreachable control, hidden focus, color-only state, misleading speech | Automation plus separate manual device evidence; human PENDING |
| IV-13 / performance | Profile/release cold/warm launch, scroll, answer/feedback/result, background resume | Actual device/build metrics and reported limitations | Debug emulator treated as physical 90/120Hz or energy PASS | Performance report/device matrix; physical device PENDING |
| IV-14 / E0–E3 | Evaluate 5-person usability/diary pack | Qualitative/descriptive evidence and explicit uncertainty | Five users prove statistical efficacy, delayed retention or ML superiority | Real pilot NOT RUN |

These challenges do not implement a future business engine to make a test green. If the expected behavior depends on a later service, report the unavailable service and retain a scoped presentation assertion instead.

## Actual development-team challenge execution

On 2026-10-02 the main execution ran the technical candidate; `candidate_tests_final.jsonl` reports49 non-hidden successful tests, including **IV-01..05 all successful, 0 skipped**, and final `done.success=true`. The challenge audit checked those exact named records and saved log/source hashes in `03_Kiem_thu/QA_QC/phase2/evidence_gated_20261002/baseline/IV_CHALLENGE_AND_SOURCE_REVIEW.json`. This is **RERUN NOW** for the current technical candidate; it is not independent human acceptance or a statement about all175 final golden states.

IV-03 was reproduced as a failing negative control in `iv03_before_fix.log`; the correction removes the initial-screen shortcut around the existing license/review prerequisite. This protects the sample workflow and implements no production authentication/publication. IV-02 initially used an incorrect harness assumption that Skip immediately advanced. Its corrected sequence follows the existing skipped feedback then explicit Continue before Android Back; production practice logic was unchanged. Failed/intermediate logs remain retained.

Catalog routes/states, PracticeFixture, task-specific lesson content/answer keys and SampleAudio remain byte-identical to the96-file pre-work archive at review. Learner/lesson changes concern presentation composition, selection icons and a review dark-mode initializer. Static journey widgets add no auth, canonical score/progress, ML or remote submission. Protected141/backend/schema/V3.2 preservation and fresh Phase1/original115+22 evidence remain separate checks. Human signatures below remain PENDING.

## Finding and closure format

For each finding record ID, requirement/source, candidate manifest, reproduction steps, expected/actual result, severity, screenshot/log, scope (presentation or future service), correction owner and retest evidence. Include negative controls: reproduce a forbidden action before the correction when practical and keep its failed log. A successful retest closes that technical finding only.

Every result uses one provenance label: **RERUN NOW**, **EXISTING EVIDENCE**, **HUMAN VERIFIED**, or **NOT RUN**. Tool-generated results cannot receive HUMAN VERIFIED. Readiness requires V3.2 expected/actual/missing/extra/hash report; original115/22; Phase1 regression; route/state trace; accessibility automation; visual and performance candidate evidence; and actual required human gates.

## Human signoff record — unsigned

| Role | Review | Result | Reviewer/date/evidence |
|---|---|---|---|
| Independent QA | Product rules, architecture invariants, edge cases, responsive/a11y, visual/performance regression | PENDING | — |
| Product Owner | Art direction, product/task comprehension, readback | PENDING | — |
| Content reviewer | Objective/task/feedback/source/accessibility correctness | PENDING | — |
| Accessibility tester | Real TalkBack core journey and staff keyboard/focus | PENDING | — |
| Tech Lead | Evidence limits, platform/performance and foundation regression | PENDING | — |

D021 Linux R1 and D022 workbook independent/visual dispositions retain separate records. New candidate automation cannot invent their closure. Neither technical nor product track certifies the other; Phase3 remains HOLD until the real human gate is explicitly satisfied.
