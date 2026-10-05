# Codex Phase 2 R1 evidence

Execution engineer: Codex. Independent approval: pending.

- `execution_summary.json`: canonical results and separate assistive-technology blocker.
- `ordered_execution_commands.json`: stdout/stderr/exit codes; all P0 before P1.
- `environment.json`: Windows, Python, Node, Chrome and server details.
- `browser/`: 74 UI cases, each with clicks, observed text/state, requests/errors and screenshot. Fresh non-persistent context per case.
- `review/`: 20 artifact review cases with inspected sources/calculations. These are not browser cases.
- `supplemental/`: 30 checks for 200% text, ancestor clipping, AX names, audio conditions and answer keys.
- `defect_retest_results.json` and `../../DEFECT_RETEST_RESULTS.csv`: 16 original + 4 new findings; no independent closure.
- `intake.json`: input ZIP hash, starting commit and hashes of tracked protected files.
- `workbook_preservation.json`: expectation/history/native feature preservation and rendering limitation.
- `initial-browser-findings.json`, `browser-first-run.json`, `supplemental-first-run.json`, `text200-before-nav-fix.json`: earlier failures, retained honestly.

## Reproduce

From repository root:

```text
python 07_operations/scripts/verify_phase2_rework.py
node --check 02_product/ux_ui/phase2/prototype/app.js
python -m http.server 8765 --bind 127.0.0.1 --directory 02_product/ux_ui/phase2/prototype
```

In a second terminal make installed Playwright available through Node module resolution (`NODE_PATH` if needed), set `MINGO_CHROME` to the local Chrome executable if different, then:

```text
python -X utf8 07_operations/scripts/run_phase2_qa.py
```

Run from a copy to preserve this evidence: runners intentionally replace their results. Independent audit files are never rewritten. No external CDN/backend is used; offered speech-synthesis playback is mock client telemetry, not physical-listening or score evidence.

## Limits

AX names, focus, keyboard and reduced motion passed. No interactive speech/TalkBack session was available through the enabled browser-only automation surface: **BLOCKED**, not PASS. This is outside the 94-case count and remains a mandatory gate blocker.

Text scaling doubles each element's computed font size, a reproducible 200% text-size proxy in QA-ACC-005. It is not a native Android font-setting or physical-device claim.

Workbook CX-14 points to the external release sidecar. Final ZIP hash/integrity is recorded after the workbook is sealed into that ZIP, avoiding a circular self-checksum.
