# Mingo — Independent QC/QA Audit for Phase 2 UX/UI Product System

**Audit date:** 2026-09-27  
**Role:** Independent QC/QA Lead  
**Candidate:** `Mingo_Phase2_UXUI_QA_Candidate_20260927.zip`  
**Architecture authority:** V3.2.0 — unchanged  
**Gate decision:** **NOT PASSED — REWORK REQUIRED**

---

## 1. Executive conclusion

The Phase 2 package is **well organized and substantially stronger as a specification/handoff package than a typical design-only delivery**. Its checksum/provenance discipline, 57-screen inventory, 18 shared component/state definitions, PRD-01..PRD-16 traceability, design tokens, offline terminology, accessibility intent, QA workbook, and explicit gate rules are all valuable foundations.

However, the candidate **cannot pass Phase 2** in its current state. The reason is not cosmetic quality. Independent audit found defects that affect **learning correctness, evidence semantics, server-authority semantics, testability, accessibility, MVP content coverage, and developer handoff completeness**.

The most serious examples are deterministic from the supplied prototype source:

- The Retrieve example for **“How are you?”** treats the distractor **“Go to school.”** as the successful answer while the natural answer **“I’m good, thanks.”** is not the success key.
- Review, Transfer and Check can advance with **no answer selected**; therefore the learner can reach **“Cycle complete”** without completing required response steps.
- A hint changes `feedback` to a hint state, but submitting an answer overwrites that state; the resulting feedback no longer preserves that the answer was **assisted**.
- Restoring connectivity changes the UI to **“Synced / All caught up”** solely because `offline=false`; there is no modeled server acknowledgement/canonical receipt.

These conflict with the product’s core integrity rules and with the Phase 2 candidate’s own gate definition. They must be fixed before Phase 2 can be signed off.

**Architecture should not be reopened.** The defects are Phase 2 UX/prototype/handoff defects. V3.2’s server-authority, evidence and offline boundaries are useful precisely because they make these failures identifiable.

---

## 2. Evidence integrity and package verification

Independent package integrity checks succeeded.

| Check | Result |
|---|---|
| Supplied ZIP SHA-256 | `9391445286c753c9d32a92a17d1f19c77dd8bea48472c7588e6bdf9f0614dd3c` |
| Supplied `.sha256` matches ZIP | PASS |
| Internal `MANIFEST_SHA256.txt` | PASS for all listed files |
| Standalone QA workbook equals workbook inside ZIP | PASS; SHA-256 `b8166016b2eefc0b596c2aae0e5858202a938cc979904d89028df7226f59fd74` |
| Candidate artifact verifier | PASS |
| Static verifier inventory | 57 screens, 18 components, 16 PRDs, 87 original QA cases |
| V3.2 provenance/boundary | PASS; no architecture mutation detected |

The supplied Phase 2 README correctly says **“DESIGN COMPLETE — READY FOR QC/QA; GATE NOT PASSED YET.”** Therefore this audit does not downgrade a previously accepted Phase 2; it performs the missing gate review.

The package also contains `PHASE1_CLOSURE_20260926.md`, which states **Phase 1 DONE / GATE PASSED**. This is newer evidence than the earlier project baseline that still described Phase 1 as ACTIVE. The progress snapshot at the end of this report reconciles that discrepancy.

---

## 3. Audit method and limitation

The audit used six evidence layers:

1. Package hashes, manifest and provenance.
2. Phase 2 contracts, screen/state specifications, PRD traceability, design system, accessibility/offline specs and handoff documents.
3. QA workbook and all original 87 QA cases.
4. Existing candidate screenshots/smoke evidence.
5. Deterministic source/state inspection of the self-contained prototype (`app.js`, `index.html`, `styles.css`).
6. External evidence benchmark: learning science, adult L2 learning, microlearning, motivation/autonomy, Android UI/accessibility and WCAG 2.2.

A fresh browser-driven runtime run could not be re-executed in the audit environment because local browser navigation was blocked by the execution environment. This does **not** invalidate source-deterministic findings such as the wrong answer key, missing click handlers, blank-submit transitions or online→Synced state logic. Cases that require genuine interaction, assistive technology or responsive runtime validation remain **NOT RUN/BLOCKED** rather than being falsely marked PASS.

---

## 4. Data analysis of the QA control

### 4.1 Candidate state at handoff

| Metric | Candidate at handoff |
|---|---:|
| Screens | 57 |
| Shared components | 18 |
| PRDs mapped | 16/16 |
| Original QA cases | 87 |
| P0 cases | 42 |
| P1 cases | 45 |
| PASS | 0 |
| FAIL | 0 |
| BLOCKED | 0 |
| NOT RUN | 87 |
| Signoffs | Pending |

The candidate therefore arrived **prepared for testing, not tested**. A dashboard value of “0 open defects” in that state must not be interpreted as defect-free; no defects had yet been logged.

### 4.2 Traceability analysis

The PRD table covers all 16 PRDs, which is a real strength. However, the coverage chain is too coarse for gate-level QA:

| Traceability signal | Observed |
|---|---:|
| Screen IDs in inventory | 57 |
| Screen IDs explicitly referenced by PRD traceability | 34/57 = 59.6% |
| Screen IDs explicitly present in original QA case file | 0/57 = 0% |
| Original QA cases with direct Screen→State identifiers | effectively none |

The 23 screens absent from PRD screen references are not automatically defects — some are supporting/system screens — but the present model makes it impossible to prove which are intentionally supporting-only versus accidentally untested. This is a **traceability control gap**, not merely documentation style.

### 4.3 Independent audit extension

Seven additional QA cases were added to the independent workbook because the original suite did not explicitly catch important failure classes:

- blank required-response submission,
- restored connectivity falsely treated as authoritative sync,
- representative Grammar flow,
- representative Listening flow,
- end-to-end staff publish lifecycle,
- programmatic accessible names on critical form fields,
- Screen/State→QA traceability.

The independent workbook therefore contains **94 live cases: 87 original + 7 audit-added regression/coverage cases**.

Current independent classification after artifact/source audit:

| Status | Count |
|---|---:|
| PASS | 10 |
| FAIL | 10 |
| BLOCKED | 7 |
| NOT RUN | 67 |
| Total | 94 |

There are **16 logged defects: 3 P0, 11 P1, 2 P2**. Thus **14 open P0/P1 defects** currently block the gate.

---

## 5. Detailed defect assessment

### P2-D001 — P0 — Retrieve answer key is wrong

**Evidence:** `submitRetrieve()` uses `selected==='go' ? 'good' : 'bad'`. In the item options, value `go` is attached to **“Go to school.”** while **“I’m good, thanks.”** uses value `good`.

**Impact:** The prototype rewards incorrect English and rejects the intended correct answer. This is a direct learning-integrity failure and invalidates QA-LRN-006.

**Required fix:** Move answer correctness into item data rather than hard-coded conditional logic. Add regression tests that assert both the correct key and each distractor for every executable prototype item.

### P2-D002 — P0 — Blank submissions can complete the cycle

**Evidence:** Review, Transfer and Check submit controls call `nextCycle()` without checking whether an answer is selected.

**Impact:** A learner can reach Cycle Complete without evidence from required response steps. This creates false completion semantics and makes the prototype unable to demonstrate the intended finite learning cycle faithfully.

**Required fix:** Separate `selection`, `submit`, `result`, `continue` and `skip` transitions. A required-response Submit must be disabled or return accessible validation until a response exists; Skip must be an explicit recorded path.

### P2-D003 — P0 — Hint-assisted evidence is not preserved

**Evidence:** `useHint()` sets `feedback='hint'`; `submitRetrieve()` then overwrites `feedback` with `good` or `bad`.

**Impact:** After a hint, the visible outcome can look like ordinary unaided recall. This violates the frozen distinction **assisted != unaided** and undermines future evidence semantics.

**Required fix:** Model `assisted` as a persistent independent flag, not as a transient feedback view. Carry it through result, evidence and telemetry semantics.

### P2-D004 — P1 — Connectivity is conflated with authoritative sync

**Evidence:** UI text switches to “Synced/All caught up” directly from the local `offline` Boolean.

**Impact:** Network availability is not proof that a durable command has been accepted by the server. This conflicts with server-authoritative progress/scoring and the Phase 2 offline state model.

**Required fix:** Prototype at minimum `LOCAL_QUEUED → SYNCING → SYNCED` with an explicit simulated server acknowledgement; separately support retryable failure, partial sync and canonical refresh.

### P2-D005 — P1 — Retry does not terminate

**Evidence:** “Try once more” resets state indefinitely and no attempt counter exists.

**Impact:** The candidate cannot demonstrate its own one-retry hypothesis or a bounded final-feedback state. It may also distort evidence semantics if copied literally into implementation.

**Required fix:** Represent first response, retry count, retry result and exhausted state separately. Keep the retry threshold configurable.

### P2-D006 — P1 — Mandatory offline recovery states are non-executable

**Evidence:** Documents define Sync Error and Canonical Refresh, but the click prototype exposes only offline waiting versus all-caught-up.

**Impact:** P0 QA-OFF-003 and QA-OFF-004 cannot be performed as written. A paper state is not enough when the Phase 2 exit gate requires review/testability.

**Required fix:** Add state switches/routes for retryable error, partial sync, re-auth, canonical refresh and media unavailable.

### P2-D007 — P1 — Onboarding/placement cannot be exercised

**Evidence:** specs define Welcome → Goal → optional Placement → provisional result → Home, but the prototype starts at Home and has no route to the first-use flow.

**Impact:** QA-NAV-002, QA-LRN-015 and first-use UAT cannot be executed. Placement is appropriately optional, but optional does not mean “design-only if it is in the MVP contract.”

**Required fix:** Add executable first-use and skip-placement branches, including provisional/missing-evidence result copy.

### P2-D008 — P1 — Listening UX is not concretely demonstrated

**Evidence:** AudioControl and play-policy rules exist in specs; the core click prototype has no Listening item.

**Impact:** Listening is an MVP domain. Developers would still have to invent key interaction behavior: loading, offered plays, replay state, Check restriction, offline media unavailable and telemetry wording.

**Required fix:** Add one representative Listening Practice and one Listening Check, plus media-unavailable state.

### P2-D009 — P1 — Staff publishing lifecycle is incomplete

**Evidence:** editor Preview has no action; provenance/license blocking is shown but lacks an end-to-end resolution path; publish confirmation is missing.

**Impact:** Staff cannot demonstrate Draft → Review → Fix → Approve → Publish Confirmation → Published → New Draft. That lifecycle is central to immutable/versioned content.

**Required fix:** Make all transitions executable, including immutable revision confirmation and create-new-draft behavior.

### P2-D010 — P1 — Critical staff inputs lack programmatic accessible names

**Evidence:** prototype form uses `<label>Prompt</label><input ...>` and `<label>Source / license</label><input ...>` without `for/id` association; inputs have no explicit ARIA naming mechanism.

**Impact:** Visible text does not reliably equal an accessible programmatic name. Content-authoring fields may be unclear to screen-reader users.

**Required fix:** Bind labels correctly and verify the accessibility tree/TalkBack or screen-reader output.

### P2-D011 — P1 — Screen specs are not deep enough for “implementation-ready” on complex screens

**Evidence:** screen inventory describes purpose, entry, actions, states and rules, but complex assessment/content-authoring screens do not consistently define component anatomy, field-level contracts, validation, state transitions, permission/data dependencies and exact test hooks.

**Impact:** A Flutter/Flutter Web team would still make product decisions while coding. That contradicts Phase 2’s stated goal that developers should not invent missing interaction semantics.

**Required fix:** Add per-screen anatomy/action/state contracts for high-complexity surfaces rather than expanding every simple screen equally.

### P2-D012 — P1 — Screen/State→QA traceability is missing

**Impact:** Defect leakage is likely because a PRD can appear “covered” while a particular state has never been tested.

**Required fix:** Add a matrix: `Screen ID → State ID → PRD/Rule → QA Case → Priority → Evidence`. Mark intentionally supporting-only screens explicitly.

### P2-D013 — P1 — Locked-objective Preview has no behavior

**Evidence:** button is rendered without an action handler.

**Impact:** QA-LRN-018 cannot verify that Preview is non-progressing and cannot bypass prerequisites.

**Required fix:** Implement preview route/modal with no evidence, progress or unlock mutation.

### P2-D014 — P2 — Accessibility focus/live-region strategy is underspecified

**Evidence:** whole SPA `<main>` uses `aria-live="polite"`; no explicit route-change focus behavior, modal focus trap or focus restore rule is defined.

**Impact:** Large SPA re-renders may generate noisy announcements, while focus movement on route/dialog changes is ambiguous.

**Required fix:** Use targeted status/error live regions; define route-heading focus and modal/sheet trap/restore behavior; validate with assistive technology.

### P2-D015 — P2 — Focus ring bypasses the semantic token

**Evidence:** CSS defines `--focus:#7C3AED` but `:focus-visible` hard-codes `#C4B5FD`.

**Impact:** Design-token drift and less reliable accessibility governance.

**Required fix:** consume a validated semantic focus-ring token consistently.

### P2-D016 — P1 — Grammar UX is not concretely demonstrated

**Evidence:** core click prototype demonstrates a simple greeting/choice flow but no representative Grammar scaffold/practice/transfer/check interaction.

**Impact:** Vocabulary/Grammar/Listening are MVP content domains, so Phase 2 should demonstrate the interaction families developers need to implement.

**Required fix:** Add one representative Grammar objective with scaffold, guided practice/retrieval, changed-context transfer and independent Check.

---

## 6. Product and learning-science analysis

### 6.1 The overall learning-cycle concept is directionally strong

The structure Review → Learn → Retrieve → Transfer → Check is defensible. Retrieval-practice literature consistently shows that retrieving information can improve delayed retention compared with additional study, while Butler’s experiments support transfer benefits from repeated testing. For adult L2 vocabulary specifically, the review by Rice & Tokowicz argues that massed repetition alone is generally weak and that spacing, retrieval and semantic elaboration/user-generated responses strengthen learning.

**Implication for Mingo:** Keep Retrieve and Check genuinely meaningful. A “correct answer” bug or blank Check is therefore not just UI malfunction; it damages the mechanism the product is relying on.

### 6.2 Five minutes should remain a UX hypothesis, not a pedagogical constant

The 2024 systematic review of microlearning describes targeted, action-oriented, bite-sized activity completed within seconds or minutes, but also notes that conceptualization and learning-outcome evidence are still not sufficiently settled to justify a universal exact duration.

Mingo’s current stance — approximately five minutes as a low-friction product hypothesis — is better than claiming that five minutes is scientifically optimal.

**Recommendation:** instrument and pilot `time_to_first_learning_action`, `cycle_duration`, `step_abandonment`, `answer_actions_per_cycle`, `optional_continue_rate`, `return_within_24h/7d`, and qualitative “too short / about right / too long” feedback. Optimize the session from product evidence, not from an arbitrary target.

### 6.3 Reduce transition overhead inside a short cycle

The current prototype has Cycle Intro, Review, Learn, Retrieve, Transfer, Check Intro, Check and Summary. This is coherent, but in a ~5-minute product, two intro transitions can consume a material fraction of attention and taps.

This is **not a gate blocker**. It is a product experiment: measure time-to-first-action and abandonment by step. If Check Intro adds little understanding, merge its explanation into the Check header. Preserve the conceptual distinction even if one transition screen disappears.

### 6.4 Multiple-choice is useful, but should not become the whole learning model

Recognition items are fast and mobile-friendly, but the L2 literature supports retrieval and user-generated responses when appropriate. Kang et al. found retrieval practice superior to imitation for foreign spoken vocabulary learning in their experiments, without a pronunciation-quality penalty.

**Recommendation:** Phase 2 should establish an interaction taxonomy, not just one MCQ template: recognition, cued recall/constructed response, listening discrimination/comprehension, contextual application and Grammar-specific structured production. Not every item needs free text, but the product should not accidentally equate tapping a distractor list with all forms of retrieval.

### 6.5 Spaced/due review is justified; exact schedule remains an intelligence-phase question

Cepeda et al.’s meta-analysis found a robust distributed-practice effect and showed that optimal spacing depends jointly on the interstudy and retention intervals. That supports Mingo’s “due review” idea while arguing against prematurely freezing one universal spacing formula.

The current architecture decision to postpone final mastery/adaptive path/risk logic is therefore sound.

### 6.6 Optional goal/placement and reason transparency are good product choices

A 2023 meta-analysis across 153 studies/179 samples found positive associations between autonomy support and learning outcomes, especially autonomous motivation, engagement and self-beliefs. A MALL systematic review likewise emphasizes learner autonomy, explicit objectives and feedback, while also acknowledging limitations in the evidence base.

**Implication:** optional goal setting, optional placement, understandable recommendation reasons and the ability to stop after a finite cycle fit the product direction. Do not turn optionality into prerequisite bypass: autonomy support and learning-integrity constraints can coexist.

### 6.7 Gamification should remain supportive rather than authoritative

A 2026 systematic review of adult ESL/EFL vocabulary gamification reports generally positive learning/motivation/engagement findings but also highlights context dependence, short-lived effects in some cases, technical issues and unhealthy competition. There is no evidence basis for assuming a leaderboard is always better.

The current decision to keep streak/rewards separate from mastery is therefore sensible. Mingo can use goals, streak continuity, gentle completion feedback and optional progress celebration without turning ranking, XP or rewards into skill truth.

### 6.8 Consumer tone needs one more editorial pass

Some copy successfully avoids false claims, but phrases such as “We’ll still use more evidence before making broader claims” sound like research governance rather than a learning companion.

The semantic rule should remain, but the learner-facing expression can be lighter. For example, a short feedback surface can say “Nice — we’ll check it again later.” Detailed evidence methodology can live under an Evidence/Why section.

This is not permission to hide uncertainty. It is a recommendation to put scientific precision in the right layer of the interface.

---

## 7. UX and visual-system assessment

### What is working

The calm visual direction is appropriate for an adult learning product. The palette has strong contrast for major text/action combinations, tap targets are designed around a 48dp baseline, learner width is bounded, the four-item learner navigation is compatible with Android guidance for three-to-five peer destinations, and staff navigation scales down at narrower widths.

The prototype also avoids casino-style gamification, fake mastery percentages, AI-as-oracle language and excessive decorative complexity. These are positives.

### What is still weak

The screens are visually clean but generic and sometimes sparse. That is acceptable for a gate candidate, but not yet a distinctive product identity. More importantly, the candidate needs richer **competence feedback and state expression**, not merely decoration: correct/incorrect/assisted/review-due/offline-queued/acknowledged states should feel immediately understandable.

A mascot, points economy or leaderboard is **not required** to solve this. Visual identity can come from typography, illustration language, motion, progress rhythm, contextual examples and warm microcopy while preserving accessibility and adult tone.

---

## 8. Accessibility assessment

The specification targets WCAG 2.2 AA-oriented behavior, 200% text scaling, keyboard access, reduced motion, non-color-only semantics and 48dp mobile touch targets. Those are appropriate targets. Android explicitly recommends 48×48dp interactive areas, while WCAG 2.2 requires 4.5:1 minimum contrast for normal text, 200% text resizing without loss of content/functionality, and at least 24×24 CSS pixels for pointer targets at AA with defined exceptions.

However, **an accessibility specification is not an accessibility pass**. All original accessibility cases arrived NOT RUN. Before gate approval, Phase 2 needs actual evidence for keyboard order, focus visibility, accessible names, error semantics, text scaling/reflow, learner mobile widths, staff compact widths and screen-reader behavior.

For Flutter implementation, translate the intent into Flutter `Semantics`, logical traversal/focus order, scalable text behavior, route/dialog announcements and tested TalkBack behavior — do not assume HTML prototype ARIA maps automatically to Flutter.

---

## 9. Feasibility for Flutter / Flutter Web implementation

### Learner Flutter Android-first

The top-level information architecture, finite-cycle concept, component sizing, design tokens and state names are readily implementable in Flutter. The main implementation risk is **underspecified interaction state**, not technical feasibility.

Before implementation, every assessment item family should have a small state machine that distinguishes at least: unselected, selected-local, submitting, result-accepted, assisted, skipped, retry-available/exhausted, queued-offline, server-confirmed and canonical-refresh-required where applicable.

### Staff Flutter Web

The six-domain staff IA is feasible, but content authoring is currently too shallow. A real content editor will need field-level UX for item type, objective/domain, level/band metadata where applicable, prompt/stimulus, answer key/distractors, feedback, hint, audio/media, attribution/source/license, validation, revision state and reviewer comments. These are Phase 2 interaction contracts even if the backend is Phase 4.

### Offline UX

The state catalog is conceptually strong and maps well to a durable command queue. The candidate must simply stop collapsing the state machine in the prototype. Network connectivity, local durability, upload attempt, server acknowledgement and canonical state are separate facts.

### Analytics readiness

Phase 2 should define **interaction/event hooks**, not production analytics infrastructure. At minimum, screen/action IDs should be stable enough to support later events such as cycle_started, item_selected, item_submitted, hint_used, item_skipped, retry_started, audio_play_requested, sync_state_presented and cycle_ended. Event semantics remain subject to the architecture’s command/telemetry separation.

---

## 10. Gate decision against the candidate’s own exit criteria

| Exit criterion | Audit status | Rationale |
|---|---|---|
| Required artifacts/provenance | PASS | Complete package, hashes and verifier are strong. |
| No contradiction with V3.2 | **FAIL at prototype behavior level** | Source documents preserve V3.2, but UI behavior conflates connectivity with sync and loses assisted state. Architecture itself remains unchanged. |
| PRD-01..16 traceability | PARTIAL | 16/16 PRDs mapped, but Screen/State→QA traceability is insufficient. |
| Learner core prototype mandatory QA | FAIL | Wrong answer key, blank progression, retry/hint issues. |
| Staff content lifecycle prototype | FAIL | End-to-end publishing is not executable. |
| Offline/loading/empty/error states | FAIL | Key error/canonical states are design-only and network→sync behavior is incorrect. |
| Accessibility P0 | FAIL/PENDING | One accessible-name defect found; mandatory real tests remain. |
| Zero open P0/P1 | FAIL | 14 open P0/P1 defects in independent log. |
| 100% P0 PASS | FAIL | Multiple P0 failures/blocked/not-run cases. |
| ≥95% executed pass | NOT ELIGIBLE | Full run has not been completed and current independent evidence contains failures. |
| Tech Lead handoff acceptance | PENDING | Must follow rework. |
| Product/Owner signoff | PENDING | Must follow rework/UAT. |
| Final verification + snapshot | PENDING | This report is the independent audit input, not final gate pass. |

**Decision: Phase 2 remains ACTIVE but BLOCKED AT QC/QA GATE. Phase 3 remains DEFERRED.**

---

## 11. Required rework sequence

### Rework wave A — learning-integrity blockers

Close P2-D001..D003 first. Add regression cases for answer keys, blank submission and hint-assisted evidence. Do not proceed to visual polishing while these remain open.

**Acceptance:** wrong distractors never receive success; required steps cannot silently pass empty; assisted evidence remains assisted after submit/retry/summary.

### Rework wave B — authoritative offline state machine

Close P2-D004 and P2-D006. Prototype queued, syncing, acknowledged synced, retryable failure, partial/canonical refresh, re-auth and media unavailable.

**Acceptance:** turning the network back on by itself never produces “Synced”.

### Rework wave C — MVP content completeness

Close P2-D007, D008 and D016. Add first-use/placement, a representative Grammar flow and representative Listening Practice/Check.

**Acceptance:** QA can execute the three MVP content-domain interaction patterns without developers inventing core behavior.

### Rework wave D — staff publishing

Close P2-D009 and D013 where relevant. Make Preview and full review/publish flow executable.

**Acceptance:** Draft → Review → provenance resolution → Approve → Confirm Publish → Published immutable → New Draft works in the prototype.

### Rework wave E — accessibility and implementation handoff

Close P2-D010..D012; resolve or explicitly accept P2-D014/D015 after mandatory defects close.

**Acceptance:** Screen→State→QA matrix exists; critical inputs have programmatic names; keyboard/screen reader/TalkBack, 200% scaling and viewport tests have evidence; complex screen contracts are sufficient to implement without product invention.

### Re-test gate

Run all P0 first. Do not count skipped/unexecuted P0 as success. Then execute the full independent suite. Gate can be considered only after 100% P0 PASS, no open P0/P1, ≥95% executed overall PASS under the project’s existing rule, Tech Lead acceptance and Product/Owner signoff.

---

## 12. Recommended pilot/product metrics after Phase 2

These are **not Phase 2 pass criteria** and should not freeze Learning Intelligence rules early. They are measurements that will help validate Phase 2’s product hypotheses in later pilot phases:

- time to first learning action;
- actual cycle duration distribution, not only mean;
- abandonment per cycle step;
- optional continue rate after summary;
- first-response accuracy vs assisted/retry accuracy kept separately;
- skip rate by item/domain;
- hint-use rate and post-hint success;
- listening play-request count as telemetry only, never proof of physical listening;
- due-review completion and delayed retrieval performance;
- offline queued commands, sync latency, retry/failure and canonical refresh rate;
- accessibility-related support failures;
- first-use placement skip rate;
- next-day / 7-day return as engagement metrics, not mastery.

These metrics give the team evidence to decide whether “~5 minutes”, one retry, placement length and other current hypotheses should stay, change or segment by learner context.

---

## 13. Project progress snapshot — 2026-09-27 after independent Phase 2 audit

### Phase status

| Phase | Status |
|---|---|
| Phase 0 — Architecture & Contract Baseline | DONE |
| Phase 1 — Implementation Foundation / Product Build Kickoff | **DONE / GATE PASSED according to supplied 2026-09-26 closure evidence** |
| Phase 2 — UX/UI Product System | **ACTIVE — BLOCKED AT QC/QA GATE** |
| Phase 3 — Identity/Auth/Authorization | DEFERRED / NOT ELIGIBLE |
| Phase 4+ | DEFERRED per roadmap |

### Frozen decisions preserved

- V3.2 remains architecture/source-of-truth authority.
- Flutter Android-first learner; Flutter Web staff/admin.
- FastAPI/Python + PostgreSQL + object storage; modular monolith.
- Server-authoritative scoring/progress/permissions.
- Command and telemetry remain separate.
- Offline durable command queue + telemetry queue.
- Published content immutable/versioned; attempts/enrollment pin exact revisions.
- Completion != mastery; mastery != risk; risk optional to recommendation.
- ML/recommendation-disabled fallback remains mandatory.
- ~5-minute session, retry/replay/placement thresholds remain hypotheses rather than hard scientific truths.

### New Phase 2 issues

`P2-D001` through `P2-D016` are recorded in the independent QA workbook. Three are P0, eleven P1, two P2.

### Change Requests

**No architecture Change Request is required from this audit.** Fixes should conform to existing V3.2 and Phase 2 contract. If the team chooses to change a frozen product decision rather than fix an implementation/design defect, that change should go through the project’s normal decision/change process rather than being silently folded into code.

---

## 14. Research references used for the product benchmark

1. Roediger, H. L., & Karpicke, J. D. (2006). *Test-enhanced learning: taking memory tests improves long-term retention.* Psychological Science. PMID 16507066. https://pubmed.ncbi.nlm.nih.gov/16507066/
2. Cepeda, N. J., et al. (2006). *Distributed practice in verbal recall tasks: A review and quantitative synthesis.* Psychological Bulletin. PMID 16719566. https://pubmed.ncbi.nlm.nih.gov/16719566/
3. Butler, A. C. (2010). *Repeated testing produces superior transfer of learning relative to repeated studying.* Journal of Experimental Psychology: Learning, Memory, and Cognition. PMID 20804289. https://pubmed.ncbi.nlm.nih.gov/20804289/
4. Rice, C. A., & Tokowicz, N. (2020). *A Review of Laboratory Studies of Adult Second Language Vocabulary Training.* Studies in Second Language Acquisition. DOI 10.1017/S0272263119000500. https://www.cambridge.org/core/journals/studies-in-second-language-acquisition/article/review-of-laboratory-studies-of-adult-second-language-vocabulary-training/18F0A5D1FFC829CE05931B2EEE83124A
5. Kang, S. H. K., Gollan, T. H., & Pashler, H. (2013). *Don't just repeat after me: retrieval practice is better than imitation for foreign vocabulary learning.* PMID 23681928. https://pubmed.ncbi.nlm.nih.gov/23681928/
6. *Microlearning beyond boundaries: A systematic review and a novel framework for improving learning outcomes.* Heliyon (2024), DOI 10.1016/j.heliyon.2024.e41413. https://www.sciencedirect.com/science/article/pii/S2405844024174440
7. *A meta-analytic review of the relationships between autonomy support and positive learning outcomes.* Contemporary Educational Psychology (2023), DOI 10.1016/j.cedpsych.2023.102235. https://www.sciencedirect.com/science/article/pii/S0361476X23000899
8. *Self-directed learning for optimizing sustainable language learning via mobile assisted language learning: a systematic review.* Frontiers in Education (2024). https://www.frontiersin.org/journals/education/articles/10.3389/feduc.2024.1463721/full
9. Ameen, F. (2026). *Individual and group competitive digital gamification in ESL adult classrooms: a systematic review of effects on vocabulary retention, motivation, and engagement.* Smart Learning Environments. DOI 10.1186/s40561-026-00447-z. https://link.springer.com/article/10.1186/s40561-026-00447-z
10. Android Developers — Navigation bar: https://developer.android.com/develop/ui/compose/components/navigation-bar
11. Android Developers — Accessibility / 48dp targets: https://developer.android.com/guide/topics/ui/accessibility/apps
12. W3C — WCAG 2.2: https://www.w3.org/TR/WCAG22/
13. W3C — WAI-ARIA live region behavior: https://www.w3.org/TR/wai-aria/

---

## Final QC/QA statement

**Phase 2 has a strong documentation skeleton and sound architectural alignment, but it is not yet an acceptable implementation-ready UX/UI product system.** The correct action is targeted rework, not a redesign from scratch and not an architecture review. Fix learning-integrity and server-authority defects first; then complete executable MVP-domain/staff states, accessibility evidence and fine-grained traceability; finally rerun the gate.
