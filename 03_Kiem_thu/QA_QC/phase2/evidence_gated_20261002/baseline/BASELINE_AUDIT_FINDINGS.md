# Baseline and evidence audit — 2026-10-02

This is the pre-change audit for the evidence-gated directive. It is an audit by the implementation team, not independent QA acceptance. Current truth must be read from PROJECT_STATE and the new directive; dated acceptance packets remain historical evidence.

## RERUN NOW

| Check | Actual result | Evidence |
|---|---|---|
| Canonical V3.2 source inventory/hash | expected 102; actual 102; missing 0; extra 0; hash mismatch 0 | before_integrity_checked.json |
| Provenance | all 3 files match the protected baseline; original source + provenance = 105 | before_integrity_checked.json |
| Protected backend/foundation/V3.2 boundary | 141 files; mismatch 0 | before_integrity_checked.json |
| Source export against current tree at pre-change capture | 472 entries; current mismatch 0; internal mismatch 0; CRC valid | before_integrity_checked.json |
| Original contract checks | 115 passed, 0 failed | original_suites_before/validation_results.json; contract.log |
| Original SQL checks | 22 passed, 0 failed | original_suites_before/SQL_VALIDATION_REPORT.json; sql.log |

Original manifest SHA256: `617245605096b3b9cc5f141dda352abc180d97f11738297949c3195711cc0e6d`.

The unchanged original programs ran on a new copy under `.local/evidence_gated_v3_2_runs`. The adapter's `verify_source` and `validate_report` validated inventories and actual individual results. Existing pinned PGlite 0.5.8 was copied into that disposable workspace; no registry download or dependency upgrade was needed. Source reports were untouched. SQL evidence is the original PostgreSQL WASM/PGlite suite and cannot prove native multi-connection concurrency.

Branch `main`, HEAD `a112f762ab08f6fa688cc4857b21d95d1055ab5c`. This audit did not modify Git, canonical originals, backend, Flutter, governance, old packages or old evidence.

## EXISTING EVIDENCE

The old 14-entry REGRESSION_COMMANDS ledger has no missing log and no hash mismatch. Inspection is current; execution dates remain those of the retained logs. See existing_evidence_checked.json.

| Claim in retained evidence | Inspected result | Interpretation |
|---|---|---|
| Shared Flutter regression | 227 successful visible tests, 0 skipped, 0 failed; final done.success=true | Existing local execution; not rerun by this audit |
| Screenshot trace | 195 rows map to passing tests and existing captures | Existing visual regression; not art-direction acceptance |
| Compiled browser flows | retained 7 results | Existing Chrome execution; not human usability |
| Android integration | retained 2-case successful log | Existing emulator execution; not physical audio/TalkBack evidence |
| Backend focused tests | 9 passed, 7 skipped | Existing log; 6 PostgreSQL cases ran separately; 1 Windows privileged symlink test skipped |
| Native PostgreSQL | 6 passed | Existing native foundation integration/concurrency; not production domain submit/scoring |
| API/worker/storage | existing 200/200 readiness, durable probe completion/heartbeat, immutable local storage smoke | Foundation only |
| Hosted CI | dated Phase1 acceptance packet describes prior CI run | Not proof of the new visual candidate |

Both current PROJECT_STATE and PHASE_STATUS agree on Phase0 DONE, Phase1 DONE, Phase2 TECHNICALLY_COMPLETE / HUMAN GATE PENDING / NOT_PASSED, and Phase3 HOLD/eligible=false. The latest directive explicitly recognizes a visual fidelity gap and additional technical evidence obligations; old technical completion cannot certify the new gate.

## Reconciliation findings

1. `03_Kiem_thu/Gate/PHASE_1_GATE.md` is dated 2026-09-26 but labels its table “Current mandatory checks” and says Phase2 has not started. Preserve its dated Phase1 acceptance; add navigation/status context in current governance instead of changing historical acceptance into a new result.
2. `SOURCE_PACKAGE_STATUS.md` describes the 472-file source ZIP as excluding generated platform hosts and local environments. Its inventory includes application `.idea` metadata and generated project metadata. These are not credentials, but its wording is broader than the actual inventory. New packaging must use an explicit inventory and a truthful scope statement.
3. Old R1 QC-002 fails the prior authored-Flutter hash seal after authorized V2 source changes. The organization-only verifier likewise fails its old UI/doc preservation boundary. Those assertions must remain intact; their scope failures must not be reported as new-candidate test failures or hidden as PASS.
4. D021 V2 narrow layout checks do not close the historical Linux R1 retest. D022 byte preservation does not validate Excel visual acceptance. Independent disposition remains pending.
5. E0 interviews, E1 moderated usability, E2 valid learning/delayed checks and E3 longitudinal value have no real participant result in the current handoff. Protocols are preparation, not validation. Existing sample answers/feedback cannot substantiate learner efficacy.
6. No current physical profile/release performance benchmark, high-refresh hardware result, manual TalkBack journey or independent art-direction signoff appears in the inspected evidence. They remain NOT RUN / PENDING.
7. Prior runtime warnings include Android NDK declaration mismatch, SDK XML mismatch, optional Cupertino icon lookup, and Starlette/httpx deprecation. Retained builds passed; warnings require technical disposition and do not justify architecture/dependency changes without a concrete defect.
8. Existing MVP_PRD authority text and PROJECT_MEMORY put explicit owner instruction before V3.2. The latest directive explicitly orders V3.2, approved Change Request, current prompt, canonical current docs, then history. Current navigation/governance should reconcile that precedence while preserving V3.2 and dated source evidence. No original contract change is implied.

## Environment and audit limitations

The sandbox could not launch `.venv/Scripts/python.exe` because its base interpreter path contains the account name Phúc. Approved outside-sandbox read-only dependency check worked but found no jsonschema in the backend virtual environment. This is not a V3.2 dependency regression: the existing `.local/v32-venv/Scripts/python.exe` contains the sealed-suite dependencies and ran the 115+22 unchanged programs successfully. No user virtual environment was moved, deleted or repaired.

`before_integrity.json` is retained as an intermediate audit record with a helper defect: suffix matching treated multiple nested README/.gitignore files as ambiguous. `before_integrity_checked.json` uses exact root member paths first and is authoritative; it finds zero ZIP/internal mismatch. `existing_evidence_inspection.json` also retains a naive “golden” name count; `existing_evidence_checked.json` instead verifies actual 195 trace rows against passing test names and is authoritative. Neither intermediate helper error changes product evidence or original hashes.

## NOT RUN / remaining gate

This agent did not rerun Flutter, native PostgreSQL foundation regression, hosted CI, physical device profiling, TalkBack, real-user interviews/usability/diary studies, content review or Product Owner approval during pre-work audit. The parent execution must rerun Phase1 and V3.2 after implementation, update evidence and preserve all historical artifacts. Phase3 remains HOLD.
