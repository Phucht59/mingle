# Mingo Phase 2 R1 — Independent QC/QA Retest Report

**Audit date:** 2026-09-29  
**Candidate:** `Mingo_Phase2_UXUI_QA_Retest_R1_20260927_codex-r1.zip`  
**Candidate Git commit:** `a112f762ab08f6fa688cc4857b21d95d1055ab5c`  
**Candidate SHA-256:** `a1221923834cfeb84fd245e93694df2b78b85daf8f23eb6908b04cabe802be10`  
**Architecture baseline:** V3.2.0 unchanged  
**Independent QC/QA verdict:** **TECHNICAL RETEST PASS / PHASE 2 GATE HOLD**  
**Project gate:** **NOT PASSED**  
**Phase 3:** **DEFERRED**

## Executive conclusion

R1 materially resolves the defects found in the first independent audit. The package hash matches the supplied sidecar and manifest, clean-extraction manifest verification passes, the Phase 2 static rework verifier passes all 16 targeted rework invariants, JavaScript syntax passes, and the artifact-review suite passes.

Independent browser reproduction was then executed against the exact R1 `index.html`, `styles.css`, and `app.js`. The execution environment blocks navigation to `localhost` and `file://` with `ERR_BLOCKED_BY_ADMINISTRATOR`, so the exact assets were loaded directly into fresh headless Chromium contexts in memory. Only transport/loading was adapted; the candidate source and interaction assertions were not modified. This independently reproduced all **74 browser canonical cases as PASS**. Together with **20 artifact-review cases PASS**, the canonical suite is independently reproduced as **94/94 PASS**, including **44/44 P0 PASS**.

The 20 findings P2-D001..P2-D020 are therefore **accepted as independently retested and functionally closed** at QC/QA level. This does **not** make the Phase 2 gate pass, because the project’s own exit criteria still require a real interactive screen-reader/TalkBack session, Tech Lead developer-handoff acceptance, and Product/Owner UAT/signoff. Those conditions remain unresolved.

## Integrity and provenance

- ZIP SHA-256 independently recomputed: **MATCH**.
- Supplied `.sha256`: **MATCH**.
- External manifest candidate identity/hash: **MATCH**.
- `verify_phase2_package_manifest.py`: **PASS — 779 manifest-covered files, no unmanifested package files**.
- `verify_phase2_rework.py`: **PASS — 57 screens, 18 components, 94 QA cases, 166 traceability rows, all 16 rework static checks true**.
- `verify_phase2_review.py`: **20/20 review/QC checks PASS**.
- `node --check prototype/app.js`: **PASS**.
- V3.2 architectural baseline: no change request required by R1 findings.

## Independent canonical execution

| Layer | Independent result | Notes |
|---|---:|---|
| Artifact/QC review cases | 20/20 PASS | Clean-extraction rerun |
| Browser interaction cases | 74/74 PASS | Fresh Chromium context per case; exact candidate HTML/CSS/JS loaded in memory because local URL navigation is policy-blocked |
| Canonical total | **94/94 PASS** | **100%** |
| P0 | **44/44 PASS** | **100%** |
| Canonical FAIL | 0 | None reproduced |
| Canonical BLOCKED | 0 | Interactive AT session is tracked outside canonical 94 per candidate gate definition |

The independent run reproduced the gate-critical behavior for answer correctness, blank-submit prevention, persistent assisted state, bounded retry, offline queue/ack authority, recovery states, onboarding/placement, Grammar, Listening, locked preview, staff publication lifecycle, accessible names, keyboard/focus behavior, live-region targeting, and the added D017–D020 regressions.

## Defect closure decision

**P2-D001..P2-D020: CLOSED — INDEPENDENT RETEST PASS.**

Important separation: closing these findings means the defects themselves are no longer open after independent retest. It does not replace mandatory gate signoffs or the dedicated interactive assistive-technology requirement.

## Responsive/accessibility nuance discovered independently

The candidate’s supplemental script reports 30/30 PASS in its original Windows/Chrome evidence. On Linux Chromium, the same 200% text-scaling logic produced document width **328px at a 320px viewport** on Home/Learn/Course/Profile. Diagnosis shows the overflow comes only from the **non-production prototype toolbar** (`.prototype-bar/.prototype-controls`); the actual learner `#app` remains 320px wide, the `.phone` remains 320px, all learner routes have zero overflowing descendants, and bottom-nav actions stay within the viewport.

This is recorded as **P2-D021 — prototype QA-toolbar 320px/200% cross-environment overflow**. Severity: **P2 / non-production tooling**. Recommended disposition: **ACCEPT/DEFER for Phase 2 product gate**, or fix the prototype toolbar with `min-width:0`, constrained chips, and overflow-wrap so the QA harness itself is portable. It does not reopen P2-D020 because the learner product surface satisfies the D020 acceptance behavior in the independent run.

## Remaining gate blockers

1. **Interactive screen-reader/TalkBack session — BLOCKED.** Keyboard navigation, programmatic names, targeted live region, focus containment/restore and Chromium AX tree checks pass, but the project explicitly states that an AX tree is not a substitute for actual speech/TalkBack review.
2. **Tech Lead developer-handoff acceptance — PENDING.** QA can verify handoff completeness, but the designated Tech Lead must record acceptance.
3. **Product/Owner UAT/signoff — PENDING.** Product acceptance must be recorded by the Product/Owner.

Because all three are explicit exit criteria, the correct project status remains:

- Phase 0: DONE
- Phase 1: DONE / GATE PASSED
- Phase 2: ACTIVE — TECHNICAL RETEST PASS, GATE HOLD
- Phase 3: DEFERRED

## Gate recommendation

Do **not** send R1 back to Codex for another general rework cycle. The original functional/UX defects are independently reproduced as fixed. The next work is narrow and procedural:

1. Run one real TalkBack (Android-first) or equivalent interactive screen-reader session against the representative learner and staff critical flows and record evidence.
2. If that session finds no blocking defect, obtain Tech Lead acceptance of the Phase 2 developer handoff.
3. Run Product/Owner UAT and record signoff.
4. Accept/defer P2-D021 explicitly or patch the non-production prototype toolbar and rerun the four 320px supplemental checks.
5. Only then update `PHASE_2_GATE.md`, progress snapshot and project memory to **Phase 2 DONE / GATE PASSED**, making Phase 3 eligible.

## Independent environment limitation

Local HTTP and `file://` navigation were blocked by the execution environment. This was treated as an environment restriction rather than a product failure. Exact candidate assets were injected into fresh Chromium documents so application behavior, DOM, keyboard, AX-tree and reflow assertions could still be executed independently. No candidate source file was edited for the retest.
