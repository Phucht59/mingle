# CODEX EXECUTION HANDOFF — Mingo Phase 2 Rework R1

## Mission

You are the execution/verification operator for **Phase 2 Rework R1**. The independent QC/QA audit rejected the first candidate. R1 has source/spec/handoff fixes for all 16 logged defects. Your job is **not to redesign Phase 2 and not to mark it DONE**. Your job is to execute the candidate in a clean environment, collect evidence, fix only implementation defects discovered in R1, and produce the exact package that goes to independent QC/QA retest.

Architecture authority: **V3.2.0 unchanged**. Production `01_San_pham/` is not part of Phase 2 rework. Do not change frozen business/architecture rules. If a real conflict is discovered, open an Implementation Issue / Change Request; do not silently reinterpret the contract.

## Inputs

- `02_Tai_lieu_du_an/04_Thiet_ke_san_pham/ux_ui/phase2/` — R1 UX system + prototype.
- `03_Kiem_thu/QA_QC/phase2/PHASE2_REWORK_R1_FIX_REGISTER.md` — all 16 defects and fix locations.
- `03_Kiem_thu/QA_QC/phase2/audits/2026-09-27_independent/` — immutable audit evidence.
- `03_Kiem_thu/QA_QC/phase2/QA_TEST_CASES.csv` — canonical **94-case** retest suite.
- `02_Tai_lieu_du_an/04_Thiet_ke_san_pham/ux_ui/phase2/SCREEN_STATE_QA_TRACEABILITY.csv` — screen/state coverage chain.

## Step 1 — Verify package basis

From repository root:

```bash
python 04_Van_hanh/Scripts/verify_phase2_rework.py
node --check 02_Tai_lieu_du_an/04_Thiet_ke_san_pham/ux_ui/phase2/prototype/app.js
```

Both must PASS. Record stdout in `03_Kiem_thu/QA_QC/phase2/evidence/codex/`.

Verify that `01_San_pham/` and `02_Tai_lieu_du_an/05_Kien_truc_he_thong/contracts/v3_2/source/` have not been modified relative to the supplied R1 package/baseline. Do not make Phase 2 fixes there.

## Step 2 — Serve the prototype

Serve, do not depend on external network/CDN:

```bash
cd 02_Tai_lieu_du_an/04_Thiet_ke_san_pham/ux_ui/phase2/prototype
python -m http.server 8765
```

Open `http://127.0.0.1:8765/` in a fresh browser profile.

## Step 3 — Mandatory browser regression (P0 first)

Execute and capture screenshot/console evidence for at least:

1. **P2-D001 / QA-LRN-006**: Vocabulary Retrieve: “I’m good, thanks.” succeeds; “Go to school.” does not.
2. **P2-D002 / QA-LRN-021**: Review/Transfer/Check cannot advance with no answer. Check cannot reach summary blank.
3. **P2-D003 / QA-LRN-008**: use Hint → submit correct answer → result still explicitly Assisted; summary/evidence context does not call it unaided.
4. **P2-D004 / QA-OFF-007**: while offline create queued action → restore network → status remains queued; start sync → syncing; only explicit mock server acknowledgement may become synced.
5. **P2-D005 / QA-LRN-007**: wrong Retrieve → one retry only → retry exhausted; first response context preserved.
6. **P2-D013 / QA-LRN-018**: locked preview opens/closes, prerequisite remains locked, no progress mutation.

A source diff is not evidence for these cases; execute them.

## Step 4 — Coverage flows

Execute representative flows:

- First use: Welcome → optional Goal → Placement take/skip → provisional result → Home.
- Grammar: Learn → Retrieve (+ hint path) → Transfer → independent Check.
- Listening: Practice replay; independent Check max offered plays; offline media unavailable blocks safely.
- Staff: Draft → Preview → Review blocked by license → Source & License verified → Approve → Publish Confirmation → immutable Published → New Draft.

## Step 5 — Accessibility/runtime checks

At minimum collect evidence for:

- Keyboard traversal and visible focus on prototype Staff and modal dialogs.
- Publish/Preview dialog focus containment + focus restoration.
- Programmatic names for Prompt/answer/source-license fields using accessibility tree.
- Targeted live-region behavior: selecting options must not announce/re-read whole page; relevant feedback/status is announced.
- 200% browser text zoom/reflow on learner width and staff 1024/1440 viewports.
- Reduced-motion preference smoke.

If your environment supports screen reader/TalkBack, run it. If not, mark the corresponding QA case BLOCKED with exact environment limitation; do not call it PASS.

## Step 6 — Execute QA workbook/suite

Use the R1 QA control workbook and `QA_TEST_CASES.csv`. Execute all P0 first, then full suite. Do not count NOT RUN/BLOCKED as PASS.

For each case set:
- Status
- Evidence path
- Defect ID if failed
- Retest note

For each P2-D001..P2-D016 set `Retest result` only from actual execution/review evidence.

## Step 7 — Defect handling

If an R1 defect remains:
- fix the smallest Phase 2 source/spec issue;
- do not weaken the test expectation;
- rerun affected regression + surrounding P0/P1 cases;
- record file/commit/evidence.

If a new defect changes a frozen V3.2/business rule, STOP and open the project change process instead of changing architecture.

## Step 8 — Codex exit condition

Codex may create a **QA RETEST CANDIDATE** only when:
- static verifier PASS;
- mandatory browser P0 regression executed;
- no known source-level P0/P1 defect remains without a retest result;
- evidence package is complete enough for independent QA to reproduce.

Codex does **not** sign Phase 2 DONE.

## Step 9 — Package for QC/QA

Create:

`Mingo_Phase2_UXUI_QA_Retest_R1_<YYYYMMDD>_<revision>.zip`

Include the complete canonical project plus fresh evidence/workbook. Generate SHA-256 and manifest. Update `02_Tai_lieu_du_an/08_Ban_giao/phase2/QA_RETEST_HANDOFF.md` from the supplied template with exact revision, test counts, environment and remaining BLOCKED cases.

Then hand off to independent QC/QA. QC/QA owns the gate decision under `PHASE_2_GATE.md`.
