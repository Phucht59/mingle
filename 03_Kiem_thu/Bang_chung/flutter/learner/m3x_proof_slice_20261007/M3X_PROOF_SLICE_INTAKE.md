# M3.X proof slice intake — 2026-10-07

**COMPLETE FOR SCOPED SOURCE IMPLEMENTATION after owner-supplied M1/M2 supplement. iOS/device acceptance remains pending.** The initial incomplete assessment below is retained as dated intake history and superseded by the addendum.

## Repository and execution provenance

- Repository: `C:\Mingo`, Git remote `https://github.com/Phucht59/mingle.git`.
- Starting branch: `main`; starting commit: `9baeffa43d02e9ff4eb1feb2b012a831dbbf72a9`.
- Dedicated evidence/work branch: `codex/m3x-proof-slice-native-companion`.
- Starting tree: DIRTY. Existing GĐ1 documents, `.gitignore`, closure packages, governance and scripts were already changed/untracked. They are preserved; no task commit includes them.
- Host: Windows x64. Flutter 3.32.8, framework `edada7c56e`, engine `ef0cd00091`; Dart 3.8.1. SDK/CI pin remains unchanged.
- iOS deployment target: **NOT CONFIGURED / NOT VERIFIED**. `apps/learner/ios` does not exist. The current bootstrap generates Android/Web only. No Xcode, simulator or attached iPhone is available in this Windows execution boundary.
- Available Flutter surfaces reported by `flutter devices --machine`: Windows, Chrome, Edge. No iOS device/simulator.

## Retained intake

Received context ZIP is retained byte-for-byte under `02_Tai_lieu_du_an/08_Ban_giao/m3x_proof_slice_20261007/`; SHA256 `2f0cd75154779de0274a32d0f7a4734b4bfee828dfc5732b5b92b0e6c10172e6`. ZIP CRC passes; 43 members extracted with traversal validation; 41 supplied manifest entries match. Nested original ZIPs and original MP4 remain unchanged. The user's pasted request is the instruction; prompts within the context pack are reference material.

Frozen V3.2 source is `02_Tai_lieu_du_an/05_Kien_truc_he_thong/contracts/v3_2/source/`, indexed by `V3.2/README.md` and original provenance `SHA256SUMS.txt`. Fresh integrity check verified all 102 files. Source manifests are never regenerated.

## Required source reading and its limits

Read before mapping implementation:

1. Root `AGENTS.md`, `REPO_RULES.md`, `PROJECT_STATE.md`, `PROJECT_MEMORY.md`, `GD1_FINAL_LOCK_MEMORY_20261005.md`, detailed FINAL BA README.
2. V3.2 master, MVP invariants, receipt/sync protocol, offline content/access protocol, normative submit algorithm; source index, original manifest and verification runbook.
3. Canonical local FINAL BA DOCX: extracted all 3,587 paragraphs to `BA_FINAL_EXTRACT.txt`; inspected Home/evidence/assistance/Check/Result/Resume/offline/sync sections and relevant UC/BR/trigger/acceptance references. This is content inspection, not a new visual DOCX acceptance or reopening of sealed GĐ1 closure.
4. ZIP's `M1_M2_CANONICAL_IMPLEMENTATION_CONTEXT.md`: an explicitly **extracted implementation context**, not the four original accepted documents.
5. M3.X implementation contract v1.0, review README, PO summary, doctrine, signatures, native mapping, accessibility stress review and storyboard.
6. Anchor overview inspected. Supplied MP4 decoded successfully and sampled in timestamp order at 2 fps; contact sheet inspected. It depicts selection B, busy state, then explanation growing within B without answer reorder. This is review of supplied browser motion reference, not a Flutter/device motion measurement or real-time playback claim.
7. Only after those reads/reference inspections: current Flutter entry, learner shell, lesson widgets, fixtures, exports, pubspecs, existing tests, bootstrap/CI, backend API surface.

**Missing:** M1 Experience Architecture; M2 Behavioral UX Specification; M2 P0 Screen-State Matrix; M2 UX Traceability/Gate. File-name and content searches of active local product/progress trees did not locate the originals. Connected Drive search found Mingo BA/governance sources but no matching M1/M2 documents. A source-location question is pending with the owner. The M3.X accessibility review independently identifies missing M1/M2 route/state documents as an integration blocker. No substitute is promoted to canonical.

## Existing implementation map

| Concern | Observed implementation | Gap for this proof |
|---|---|---|
| State management | StatefulWidget, ChangeNotifier, ListenableBuilder; `PracticeFixture`, `ReviewPreferences` | Presentation-only objects; no durable session/evidence repository |
| Routing | `LearnerApp.id`, `history` of `(screen ID, LessonDomain)`, `go/back`; MaterialApp/PopScope | No retained native tab stacks or focused modal Close; Home scroll/context persistence unproven |
| Local persistence | No persistence dependency or local repository in learner/shared pubspec/lib | No durable write success/failure boundary; no process-death restoration |
| Command queue | None in current Flutter runtime | No reusable production queue abstraction to bind fixtures to |
| Telemetry queue | None in current Flutter runtime | Future separate queue required by V3.2; must not implement learning as telemetry |
| Sync | Presentation notices/catalogue states | No command transport, matching receipt reconciliation, anti-rollback/history |
| Practice/evidence | `fixtures.dart`: mutable selection/firstResponse, retry count, hint/submitted/skip; first submit uses `??=` | First response is public mutable; no immutable response records, pinned identities or receipt-linked evaluation |
| Feedback | `lesson.dart`: Notice after all answer rows | Explanation detached from selected answer; no stable answer-unit key or runtime announcement/focus proof |
| Check | Fixture guards Hint/Retry/Skip; widget omits Hint | Stronger condition currently presentation-only; no durable exact item/revision/session restore |
| Result | `L-032` sample closure with next-step primary | Does not prove requested Done primary/explicit eligibility decision or sync truth |
| Backend | `all_foundation/api.py`: health live/ready only | No existing submit/sync dev endpoint; allowed fake server boundary would need an actual shared queue/repository boundary |
| Platform hosts | Generated Android/Web | iOS host, deployment target, signing/build/runtime unavailable |

Relevant files: `01_San_pham/apps/learner/lib/main.dart`; shared `mingo_ui/lib/src/{learner,lesson,fixtures,lesson_content,design,audio,journey,catalog}.dart`; `mingo_ui.dart`; learner/shared pubspecs and tests; backend `src/all_foundation/api.py`; `04_Van_hanh/Scripts/bootstrap_clients.sh`; `.github/workflows/foundation.yaml`.

## Contracts to preserve

- BA UC-L06/L07/L09/L10/L11/L13/L16/L19/L23 and UC-SYS01; BR-001/002/004/006/008/009/011/012/013/016/017/018/024/026/033/035. Home priority remains Resume → Due Review → Next Path → Goal Match → Fallback.
- Extracted M1/M2 owners: L-S04 Home, L-S08 Task, L-S09 inline Feedback, L-S10 Check, L-S11 Result, L-S15 Sync, L-S16 Account Gate. These IDs are **not verified route bindings** to existing `L-xxx` catalogue IDs.
- Extracted acceptance IDs: UXA-P0-003/004/006/007/008/009/011/012/013. Original matrix/gate traceability remains unverified.
- V3.2: server alone scores/grants canonical progress/permissions; correct keys server-only; offline pilot remains submitted/pending until scoring ACK. A proof server may evaluate explicitly; a client must not silently evaluate offline using downloaded answer keys.
- First response is preserved; supported retry is a new immutable response and, for a new finalized command, a **new attempt ID**. Retry does not edit a finalized attempt or payload under its original command ID.
- Commands and telemetry remain separate. Account-bound durable command bytes/IDs/revision/grant/package/installation survive replay and failure. Network restoration permits retry, never ACK.
- Accepted/duplicate receipts reconcile their scoped current state with anti-rollback; rejected/conflict/denied/reauth are not success. Conflict does not silently repin. Terminal history survives reconciliation.
- Protected learning requires authenticated eligibility; a clearly marked authenticated proof fixture cannot be represented as production auth.
- Result fixture cannot imply that one Practice item completed Transfer/Check/the canonical finite cycle.

## Exact planned modifications and decision

**Approved now:** additive intake/evidence documents and raw logs in this evidence directory; retained context bytes/manifest in the handoff intake directory; isolated baseline execution under ignored `.local/m3x-baseline/`. No existing runtime, backend, frozen contracts, historical test output or governance status is edited.

**Runtime source files planned for this run: NONE while the required canonical input gate is incomplete.** A later source change list must be explicit after canonical M1/M2 are read and route/state bindings reconciled. Candidate existing touchpoints are learner entry, shared `learner.dart`, `lesson.dart`, `fixtures.dart`, export, pubspec and executable project tests; these are mapping candidates, not an approved implementation plan. Durable queue design cannot be fabricated as an extra proof-only persistence path.

Risks: missing accepted routes/policy; no durable queue/repository; no real submit service; missing iOS target/signing/runtime; false local-save/scoring/sync claims from a mock; changing existing 61-screen review behavior; baseline suites writing historical evidence. Full presentation baseline therefore runs on an isolated byte copy with matching golden inputs.

**Can proceed safely?** Read-only mapping, baseline checks and honest evidence preparation: YES. Contract-compliant source implementation: **HOLD pending four canonical sources**. Propagation/device/accessibility/durability acceptance: **NOT EXECUTED**. No design restart or V3.2 amendment is required by observed evidence.

## Resolved input gate and implementation plan — same-day addendum

Owner supplied `C:\Users\Phúc\Downloads\MINGO_M1_M2_CANONICAL_SUPPLEMENT_2026-10-07.zip` in response to the source question. Retained ZIP SHA256 `4bd912fa6a2fc0ba87d57cbfd392b6f6bf5356e5c7c361a38527de285952b994`; CRC PASS; six members, all five manifest entries PASS. Read the complete M1 v0.1, M2 behavioral v0.1, P0 matrix v0.2 and UX traceability/gate v0.3 before source changes. The supplied source-link file records Linear export provenance; this is owner-supplied source evidence, not an independently rechecked live Linear gate.

Mapped scope: HOME-01/10 → TASK-02/03/04/05/06/07/08/09/10/14/15/16 → FB-01/02/03/04, CHK-02..08, RES-01/03/04/05/07, SYNC-01..09; UXA-P0-003/004/006/007/008/009/011/012/013. Welcome limited anchor fixture WLC-01/02 retains Start primary, Explore secondary. No full onboarding/Auth flow is implemented. The new opt-in proof uses these exact screen owners; it does not reinterpret historical `L-xxx` catalogue IDs as new canonical route IDs.

The repository has no existing persistence/queue implementation to reuse. Build its **first shared session/command repository boundary**, used by every proof scenario, rather than a second path around an existing queue. One account-scoped snapshot atomically contains immutable response history, pinned commands, reconciliation history and origin. File writes flush before atomic replacement; injected write failures do not advance the visible saved state. This proves ordinary successful-write/process termination behavior; power-loss guarantees, encrypted production account storage and multi-process writers remain explicit debt. Telemetry is not added or mixed into commands. Keep the existing ChangeNotifier approach. Use the already-resolved path_provider 2.1.5 for native application support location and crypto 3.0.6 for command/snapshot digests, without broad dependency upgrades.

Planned source changes (exact):

- `01_San_pham/apps/learner/lib/main.dart`: compile-time opt-in entry only.
- `01_San_pham/apps/learner/pubspec.yaml`, `pubspec.lock`: pin direct dependencies already present transitively.
- `01_San_pham/apps/learner/lib/m3x/learning_state.dart`: immutable response/queue/session/domain types.
- `01_San_pham/apps/learner/lib/m3x/learning_store.dart`: common persistence abstraction and atomic native snapshot store.
- `01_San_pham/apps/learner/lib/m3x/proof_server.dart`: clearly marked deterministic server boundary and durable idempotency ledger.
- `01_San_pham/apps/learner/lib/m3x/proof_controller.dart`: existing-style ChangeNotifier orchestrator and ACK validation/recovery.
- `01_San_pham/apps/learner/lib/m3x/proof_app.dart`: native shell and narrow content widgets/fixtures.
- `01_San_pham/apps/learner/lib/m3x/open_store_native.dart`, `open_store_unsupported.dart`: platform boundary; unsupported browsers fail honestly.
- `01_San_pham/apps/learner/test/m3x_domain_test.dart`, `m3x_widget_test.dart`: required domain/widget/scoped flow checks.
- `01_San_pham/apps/learner/tool/m3x_process_probe.dart`: actual process termination/relaunch probe using the same store.
- `01_San_pham/apps/learner/integration_test/m3x_proof_test.dart`: native integration flow for supported devices.

Build-host preparation, if generated on Windows, stays task-local and clearly unbuilt. No signed iOS binary or simulator/device pass will be claimed. No broad shared-library edit, router replacement, staff change, production scoring/auth implementation or architecture amendment is planned.

**Source implementation may now proceed safely within this plan.** Propagation authorization remains evidence-gated.

## Handoff addendum — 2026-10-07

Actual dependency resolution is **crypto 3.0.7**, correcting the planning value 3.0.6 above. It and path_provider 2.1.5 were already transitive dependencies; both are now direct pinned dependencies. Added cupertino_icons 1.0.8 supplies the icon font required by the Cupertino controls. No Flutter/Dart or unrelated dependency upgrade was made.

Owner reports an **iPhone Air with iOS 27 beta**. Exact beta/build, Xcode version and access to a Mac are not yet verified. This device is not attached to the executing Windows host. The report is device availability information, not a test result.

Generated an isolated standard iOS host with the pinned Flutter 3.32.8 SDK under `.local/m3x-ios-preparation`. Its template deployment target is **12.0** and placeholder bundle identifier is `com.example.adaptiveLearner`. These are inspected template values, not a tested minimum OS or shipping identifier. The source export preserves this generated host separately from authored source; local paths, registrants, IDE metadata, caches and signing material are excluded. `IOS_BUILD_INPUT_SOURCE_MATCH.json` verifies the authored copy. The Mac must resolve plugins and generate its own local configuration/registrants.

Windows `flutter build ios` exits 64: the host has no `ios` build subcommand. No iOS compilation, simulator run, signed binary or device execution occurred. Device instructions and the unbuilt source package are handoff inputs only.
