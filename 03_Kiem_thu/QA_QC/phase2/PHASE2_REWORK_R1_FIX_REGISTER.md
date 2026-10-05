# Phase 2 Rework R1 — Defect Fix Register

All 16 independent-audit defects have been addressed in Phase 2 source/spec/handoff. **Status here means implemented/fixed in candidate, not independently QA-passed.** Codex must execute and QC/QA must retest.

| Defect | Sev | Finding | R1 status | Evidence files | Fix summary |
| --- | --- | --- | --- | --- | --- |
| P2-D001 | P0 | Wrong Retrieve answer key | FIXED IN SOURCE | prototype/app.js | Data-driven item answer; correct reply value good is canonical. |
| P2-D002 | P0 | Blank required-response progression | FIXED IN SOURCE | prototype/app.js; 15_COMPLEX_SCREEN_INTERACTION_CONTRACTS.md | Submit disabled until selection; explicit Skip separate; Check cannot blank-complete. |
| P2-D003 | P0 | Hint-assisted state lost | FIXED IN SOURCE | prototype/app.js | assisted is persistent independent state and rendered through result/summary. |
| P2-D004 | P1 | Connectivity conflated with sync | FIXED IN SOURCE | prototype/app.js; 11_OFFLINE_SYNC_UX_SPEC.md | Online restoration leaves LOCAL_QUEUED until explicit sync + acknowledgement. |
| P2-D005 | P1 | Unlimited retry loop | FIXED IN SOURCE | prototype/app.js | One retry in current policy; first response preserved; exhausted branch. |
| P2-D006 | P1 | Offline recovery not executable | FIXED IN SOURCE | prototype/app.js | Failure, partial, reauth, canonical refresh and media unavailable are executable. |
| P2-D007 | P1 | Onboarding/placement not executable | FIXED IN SOURCE | prototype/app.js | Welcome→Goal→Placement offer→questions/skip→provisional result→Home. |
| P2-D008 | P1 | Listening flow absent | FIXED IN SOURCE | prototype/app.js | Representative Listening cycle, practice replay, Check play cap, media unavailable. |
| P2-D009 | P1 | Staff publishing lifecycle incomplete | FIXED IN SOURCE | prototype/app.js | Full Draft→Preview→Review→provenance→Approve→Confirm→Published→New Draft. |
| P2-D010 | P1 | Form controls lack accessible names | FIXED IN SOURCE | prototype/app.js | Native label for/id and descriptions for critical fields. |
| P2-D011 | P1 | Complex screen spec too shallow | FIXED IN HANDOFF | 15_COMPLEX_SCREEN_INTERACTION_CONTRACTS.md | Anatomy/state/validation/dependency/test hooks defined. |
| P2-D012 | P1 | Screen/state→QA traceability missing | FIXED IN HANDOFF | SCREEN_STATE_QA_TRACEABILITY.csv | Every screen/state classified and mapped to QA. |
| P2-D013 | P1 | Locked preview non-functional | FIXED IN SOURCE | prototype/app.js | Modal preview works and explicitly creates no progress/unlock. |
| P2-D014 | P2 | Focus/live-region strategy weak | FIXED IN SOURCE/SPEC | index.html; app.js; 16_ACCESSIBILITY_FOCUS_LIVE_REGION_SPEC.md | Targeted live region, route focus, native modal focus containment/restore. |
| P2-D015 | P2 | Focus token bypassed | FIXED IN SOURCE | prototype/styles.css | All focus outlines consume var(--focus). |
| P2-D016 | P1 | Grammar flow absent | FIXED IN SOURCE | prototype/app.js | Representative Grammar cycle with scaffold/retrieve/transfer/independent Check. |

## Gate rule

Codex execution on 2026-09-27 retested all 16 original findings. See `DEFECT_RETEST_RESULTS.csv` and `PHASE_2_VERIFICATION_REPORT.md`. Four additional findings D017–D020 are in `CODEX_EXECUTION_DEFECTS.md`. All are READY FOR INDEPENDENT RETEST, not CLOSED.

No defect is considered CLOSED merely from this register. After Codex execution, affected cases are retested by independent QC/QA. P0/P1 close only on accepted evidence.
