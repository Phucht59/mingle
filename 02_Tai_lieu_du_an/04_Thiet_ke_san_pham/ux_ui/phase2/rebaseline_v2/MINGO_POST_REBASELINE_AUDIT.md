# Mingo post rebaseline audit — 2026-10-02

Scope: owner FINAL HUMAN RE-BASELINE DIRECTIVE, captured byte-for-byte in `03_Kiem_thu/QA_QC/phase2/evidence_gated_20261002/before/OWNER_DIRECTIVE_20261002.txt`. This audit precedes substantial UI changes. Phase3 HOLD. V3.2 remains authority ahead of this directive; no architecture reopening is justified by the visual finding.

## Current facts and provenance

| Claim | Evidence provenance | Audit result |
|---|---|---|
| Repository has five human-readable areas | RERUN NOW: physical inventory, Git status/log | Product1480 files; docs253; QA/evidence34394; operations36; archive204 at capture. Counts include generated builds/captured outputs and are not authored-source counts |
| Existing Git state | RERUN NOW | main, HEAD a112f762ab08f6fa688cc4857b21d95d1055ab5c;11456 status entries at first read; existing staged moves/user edits retained; no AGENTS.md found in active search |
| Existing source export | RERUN NOW: independent baseline check |472 source members match manifest/current files; ZIP CRC and original source ZIP hash match. Previous QA ZIP hash43d3e491… also captured |
| V3.2 originals | RERUN NOW: independent baseline check | expected102, actual102, missing0, extra0, SHA mismatch0; protected141 mismatch0, including105 source/provenance files |
| Original115 contracts /22 SQL | RERUN NOW |115/115 +22/22 PASS in fresh isolated copy. SQL is original PGlite, not native multi-connection PostgreSQL. New evidence: evidence_gated_20261002/baseline/original_suites_before/ |
| Phase1 regression | EXISTING EVIDENCE | prior local9 unit/6 nativePG/API/worker/storage PASS; must rerun after this candidate. Phase1 closure/gate dated26/09 says Phase2 not started: historical acceptance scope, not current project truth |
| Phase2 technical coverage | EXISTING EVIDENCE |61 screens,175 states,227 tests,195 comparisons,7 Chrome,2 Android. This proves only the recorded candidate/scope, not new visuals or product validity |
| P2-V2-UI-001 | RERUN NOW: owner/current image and source review | Confirmed presentation gap; no domain/state rewrite required. Image reference01/02 contains iOS chrome/features outside scope; only composition/identity are inputs |
| Human evidence | RERUN NOW: repository research/product search; EXISTING unsigned checklists | No supplied interview/diary/usability attendance/transcript/outcome dataset identified. E0–E3 HUMAN VALIDATION PENDING. Synthetic samples cannot close these levels |
| Physical performance/accessibility | RERUN NOW: tool/device inventory | SDK/Flutter exist; adb currently reports no devices. Old debug APK121215663B is size evidence only. No physical60/90/120Hz, battery, thermal or TalkBack result |

Initial baseline and full status: `03_Kiem_thu/QA_QC/phase2/evidence_gated_20261002/before/BASELINE.json`.96 authored files were copied and SHA-checked under `99_Luu_tru/Phase2_V2_before_evidence_gate_20261002/`. Original screenshots and both ZIPs remain intact. Independent check's first helper output had a duplicate-suffix source-member lookup mistake; corrected `baseline/before_integrity_checked.json` is authoritative, with the failed helper retained as such.

## Presentation findings before rework

Home: greeting, detached landscape, generic outlined lesson card, then a habit notice push the core action down and fragment the companion narrative. Course/Progress: textual card stacks carry status correctly but do not visually communicate a journey. Result: neutral schema-like facts need a quiet completion composition with honest evidence and one next action. Learn: practical search/topic distinctions exist; image/context hierarchy is weak. Profile/onboarding/recovery: the same mascot image is useful but currently sized uniformly without a defined per-use system.

Keep Android system Back/history, routes,61/175 catalogue, sample-data disclosure, unaided/assisted/skip distinctions, immutable sample/draft separation and staff task flow. Rework only learner composition, shared learner presentation components, image sizing and relevant accessibility. Staff must keep productivity focus.

## Technical debt and environment

Two raw PNGs total4571511B and1572864px each, with no cacheWidth/cacheHeight. Estimated RGBA decode is6MiB each before cache/GPU copies; this is arithmetic, not observed memory. No BackdropFilter/saveLayer/full-screen real-time blur was found. Short pages use eager Column inside scroll view; measure before replacing working layout. Profile/release instrumentation and bounded decoding are missing. Freeze SDK Flutter3.32.8/Dart3.8.1.

Sandbox Python venv launcher initially failed on the Unicode base path; bundled Python works. V3 suite succeeded with existing `.local/v32-venv` outside sandbox after approved escalation. Do not delete/repair user environment or describe a sandbox invocation failure as a failing contract. Existing NDK26/plugin27, SDK XML and optional icon-family warnings require Tech Lead disposition, not silent dependency/framework upgrades.

## Governance and product gaps

Current PROJECT_STATE/MEMORY/PHASE_STATUS agree on Phase2 TECHNICALLY_COMPLETE with HUMAN GATE PENDING. The newer directive adds visual/performance/evidence gates, so the former technical completion is an existing candidate claim, not proof that new requirements are complete. Current PROJECT_STATE must become the single current narrative; decision register holds frozen decisions; final gate holds acceptance/evidence. Dated Phase1/R1 packets remain historical.

P01–P25 need an eight-field resolution matrix with implementation/test/human dependency. Five minutes, target audience and differentiation remain hypotheses. Charter adult beginner wording has no observed discovery data. Existing content rubric's 'exact frozen' challenge wording exceeds the provisional product policy scope and must be clarified without changing fixtures or V3.2. No physiological/psychological state may be inferred from one behavioral event; no learning-style personalization or production ML is justified.

## Work authorization and stop conditions

The owner authorizes visual fidelity rework, conceptual model/research/measurement frameworks, instrumentation, accessibility refinements, tests, governance reconciliation and a new handoff. Human design approval cannot be generated. New goldens require recorded technical candidate checks first; they certify regression only. Physical devices absent means physical performance/accessibility PENDING, with emulator profile results separately labeled if collected. Keep Phase3 HOLD; no auth, real learning-domain service, durable offline/sync, curriculum, ML or production deployment.
