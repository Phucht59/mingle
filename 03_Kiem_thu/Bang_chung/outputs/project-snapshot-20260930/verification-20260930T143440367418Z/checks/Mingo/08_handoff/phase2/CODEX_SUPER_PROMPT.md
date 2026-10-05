# CODEX SUPER PROMPT — Execute Mingo Phase 2 Rework R1 and hand off to independent QC/QA

You are the execution engineer for **Mingo Phase 2 Rework R1**. Work directly on this supplied repository/package.

## Non-negotiable current state

- Phase 0: DONE. Canonical architecture/contract baseline = **V3.2.0**.
- Phase 1: DONE / GATE PASSED.
- Phase 2: ACTIVE / **GATE NOT PASSED**.
- Candidate v1 failed independent QC/QA with 16 defects (P2-D001..P2-D016).
- Rework R1 contains source/spec/handoff fixes for all 16 findings, but **none is independently closed yet**.
- Phase 3: DEFERRED. Do not implement Phase 3.

Do not reopen architecture. Do not edit original V3.2 semantics or production Phase 1 `05_code/` to make Phase 2 tests pass. If evidence exposes a true frozen-contract conflict, stop that path and record an Implementation Issue / Change Request instead of silently changing the rule.

## Your mission

Execute and verify R1 in a clean environment, fix only concrete Phase 2 defects discovered during execution, collect reproducible evidence, update the canonical 94-case QA control truthfully, then create a **QA RETEST CANDIDATE** and hand it to independent QC/QA. You are not the final gate owner and must not mark Phase 2 DONE.

## Read first

1. `08_handoff/phase2/CODEX_EXECUTION_HANDOFF.md`
2. `06_quality/phase2/PHASE2_REWORK_R1_FIX_REGISTER.md`
3. `06_quality/phase2/PHASE_2_GATE.md`
4. `06_quality/phase2/Mingo_Phase2_Rework_R1_QA_Control_2026-09-27.xlsx`
5. `06_quality/phase2/audits/2026-09-27_independent/`
6. `02_product/ux_ui/phase2/15_COMPLEX_SCREEN_INTERACTION_CONTRACTS.md`
7. `02_product/ux_ui/phase2/SCREEN_STATE_QA_TRACEABILITY.csv`

## Execute, do not merely review

From repository root first run:

```bash
python 07_operations/scripts/verify_phase2_rework.py
node --check 02_product/ux_ui/phase2/prototype/app.js
```

Save actual stdout/environment details under `06_quality/phase2/evidence/codex/`.

Serve the self-contained prototype from `02_product/ux_ui/phase2/prototype/` in a fresh browser profile. Prefer a real local HTTP server and browser automation/manual browser evidence. Do not use external CDN/network dependencies.

### P0 mandatory regressions first

Reproduce at minimum:

- P2-D001: “I’m good, thanks.” is correct for “How are you?”; “Go to school.” never passes.
- P2-D002: Review/Transfer/Check cannot submit/advance blank; Check cannot fabricate cycle completion.
- P2-D003: hint use persists as assisted after submit/result/summary semantics.
- QA-OFF-007 / P2-D004: restoring connectivity alone never becomes Synced; queued → syncing → server acknowledgement → synced.
- P2-D005: one bounded retry; first response preserved; retry exhaustion visible.
- P2-D013: locked Preview works but creates no progress/unlock.

Then execute:

- first-use Welcome → optional Goal → Placement take/skip → provisional result → Home;
- representative Grammar cycle;
- representative Listening Practice + Check, 2 offered Check plays, media-unavailable state;
- Staff Draft → Preview → Review blocked by license → fix license → Approve → Publish confirmation → immutable Published → New Draft;
- accessibility: programmatic names, keyboard/focus, modal focus restore, targeted live regions, 200% zoom/reflow, learner/staff viewports, reduced motion; use screen reader/TalkBack if environment supports it.

## QA control rules

The canonical suite has **94 cases**. Execute P0 first, then full suite. In the workbook/CSV evidence:

- PASS only from actual evidence;
- NOT RUN/BLOCKED never counts as PASS;
- never edit Expected to make a failure disappear;
- for every failure add/retain defect ID and evidence;
- retest all P2-D001..P2-D016;
- do not close a defect solely because source contains a fix.

If a defect remains, apply the smallest Phase 2 prototype/spec/handoff fix, rerun the affected case plus surrounding P0/P1 regressions, and record the exact change/evidence.

## Required Codex output

Before handoff create/fill:

- `06_quality/phase2/evidence/codex/` with commands, environment, screenshots/logs/accessibility evidence;
- updated `Mingo_Phase2_Rework_R1_QA_Control_2026-09-27.xlsx` with actual run statuses;
- actual defect retest results;
- `08_handoff/phase2/QA_RETEST_HANDOFF.md` copied/filled from the template;
- exact package `Mingo_Phase2_UXUI_QA_Retest_R1_<YYYYMMDD>_<revision>.zip`;
- SHA-256 and package manifest.

Verify package integrity and make sure no plaintext credentials, `.venv`, caches, generated build junk or unrelated secrets are included.

## Mandatory handoff to QC/QA

When execution is complete, your final action is **not** to declare Phase 2 DONE. Hand the exact retest package, hash, updated workbook and evidence to independent QC/QA and include `08_handoff/phase2/QA_QC_RETEST_PROMPT.md`.

Independent QC/QA owns the gate recommendation. Gate criteria remain:

- 100% P0 PASS;
- zero open P0/P1;
- at least 95% of executed cases PASS, with any remaining P2/P3 explicitly accepted/deferred;
- mandatory accessibility PASS;
- developer handoff accepted;
- Tech Lead + Product/Owner signoff.

Only after independent QC/QA and signoff may project governance mark Phase 2 DONE and Phase 3 ELIGIBLE.

Start now. Do the execution, evidence collection and handoff. Do not stop at a plan unless an external environment limitation genuinely prevents a required test; in that case mark the exact case BLOCKED and continue everything else.
