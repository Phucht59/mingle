# M3.X Native Companion proof slice — implementation report

Run identity: 2026-10-07; handoff completed across the local date boundary into 2026-10-08, Asia/Saigon. Scope: owner-authorized Flutter/iPhone proof slice. Candidate: uncommitted work on `codex/m3x-proof-slice-native-companion`, based on `9baeffa43d02e9ff4eb1feb2b012a831dbbf72a9`. Repository had unrelated GĐ1 changes before this task; those are outside this candidate.

**Automated scope passes. Propagation remains HOLD because iOS compilation and physical iPhone acceptance have not been executed.** M3 remains NOT YET PASSED. This report does not close customer validation, Phase 3, production offline readiness or accessibility certification.

## What changed

Added an opt-in Native Companion entry, selected by `--dart-define=MINGO_M3X_PROOF=true`. Home has one deterministic Resume action and reason. A full-screen Cupertino route presents focused Practice without the tab bar; Close retains the originating shell, tab and scroll position. The answer keeps its revision/option key through selection, submission and inline explanation. No separate Feedback route is introduced.

The slice also includes isolated Independent Check, finite Result, Result Pending Sync, Sync Recovery and Welcome anchor fixtures. Result is explicitly a closed-cycle sample independent of the interactive single Practice item. Xong is primary. Học tiếp makes a fresh eligibility decision and offers an explicit return to the next action; it does not launch a lesson automatically.

F-M3X-004 is addressed: Bắt đầu primary, Khám phá trước secondary and functional; no decorative bookmark control; correct Retry is hidden under the default configurable proof policy; “Các lần trả lời” opens response history. Hint, explanation-assisted retry and independent evidence stay distinct.

## Why

The existing learner was a presentation review application with in-memory fixtures, an ID/history router and no durable command repository or submit service. It could not prove truthful saved state, process restoration, immutable evidence or ACK-controlled synchronization. The new entry keeps the existing ChangeNotifier approach and contains the proof within the learner package. Original review behavior remains the default entry and its build/test smoke still passes.

The owner supplied the missing four canonical M1/M2 exports before source changes. Reading order, source identities and the resolved intake gate are retained in [intake](M3X_PROOF_SLICE_INTAKE.md). Prototype appearance never overrode V3.2 or GĐ1. No baseline contradiction requiring an architecture amendment was found.

## Files changed

Paths below are relative to `01_San_pham/apps/learner/`; exact authored hashes are in [FINAL_SOURCE_MANIFEST.json](FINAL_SOURCE_MANIFEST.json).

| Files | Responsibility |
|---|---|
| `lib/main.dart` | Compile-time opt-in, default foundation entry retained |
| `pubspec.yaml`, `pubspec.lock` | Direct pins crypto 3.0.7, path_provider 2.1.5; Cupertino icon font 1.0.8 |
| `lib/m3x/learning_state.dart` | Immutable responses, assistance, exact cached content/revisions, queue bytes, IDs, configurable fixture policy |
| `lib/m3x/learning_store.dart` | One session/business-command snapshot boundary; checksum, flushed temp write, same-directory replacement |
| `lib/m3x/proof_controller.dart` | Serialized durable commits, submit guard, origin/Resume, ACK checks, anti-rollback and recovery states |
| `lib/m3x/proof_server.dart` | Explicit controlled server fixture with durable receipt/attempt ledger and idempotent replay |
| `lib/m3x/open_store_native.dart`, `open_store_unsupported.dart` | Native application-support location; honest unsupported browser boundary |
| `lib/m3x/proof_app.dart` | Native shell, focused flow, stable answer expansion, limited fixtures and semantics |
| `test/m3x_domain_test.dart`, `test/m3x_widget_test.dart` | Additive domain/widget acceptance and negative cases |
| `integration_test/m3x_proof_test.dart` | Native persistence/route/ACK integration scenario, authored but NOT EXECUTED |
| `tool/m3x_process_probe.dart` | Same-store host process-death probe and schema-valid wire export |

Evidence is additive in this directory; retained intake is in `02_Tai_lieu_du_an/08_Ban_giao/m3x_proof_slice_20261007`. Generated iOS host files are build inputs in the source ZIP, not a committed/signed iOS product. Governance records only the scoped result and open issues. Backend, staff, shared presentation source, frozen schemas, source ZIP bytes and sealed evidence were not modified by this implementation.

## Tests added

29 domain cases cover immutable first response; hint and assisted retry; configurable correct retry; Check evidence; Home Resume; actual file restoration; failed writes and checksum corruption; matching ACK; duplicate UI submission and replay; altered payload conflict; finalized/stale attempt rejection; anti-rollback; incompatible same-revision progress; account mismatch; re-auth across relaunch; and digest semantics.

14 widget cases cover the full Home/Practice/Close/Resume path at a nonzero origin offset; same answer Element and top position; selected/enabled semantics; one verdict announcement; inline explanation; Check without Hint; Result/Continue decision; sync wording; failed-save wording; reduced motion; 320-point/3.2× text; long Vietnamese/English content; dark appearance; Welcome actions; and 44-point essential controls. Some tests assert multiple related acceptance conditions. The existing learner smoke test is retained, making 44 total executed learner tests. Native integration is a separate unexecuted test.

## Automated results

| Check | Result | Evidence |
|---|---|---|
| Before-change shared baseline | 275 passed, 0 failed/skipped | `BASELINE_RESULTS.json`, `shared_test.log` |
| Before-change learner baseline | 1 passed | `BASELINE_RESULTS.json` |
| Original baseline inputs | 240 checked, 0 changed during baseline run | `BASELINE_SOURCE_PRESERVATION.json` |
| Final learner suite | 44 passed, 0 failed/skipped | `LEARNER_RELEASE_CANDIDATE_TEST_RESULTS.json`, raw JSONL |
| Scoped Dart format | 12 files, 0 changes | `formatter_handoff_final.log` |
| Learner analyzer, including native test source | No issues | `analyzer_handoff_final.log` |
| Default web build | PASS | `default_web_build.log`; this is a default-entry compilation smoke, not native proof |
| Original V3.2 suite | 115 contract + 22 SQL passed; 102 original files verified | [run.json](../../../v3_2/20261007T155115319732Z/run.json) |
| Generated wire fixtures | 8 schema validations + independent digest PASS | `WIRE_RELEASE_CANDIDATE_SCHEMA_RESULTS.json` |
| Same-store Windows process termination/relaunch | HOST_PROCESS_PASS, exact snapshot equal | `PROCESS_DEATH_HOST.json` |

V3.2 SQL here is the original PGlite suite, not native PostgreSQL concurrency evidence. Shared tests ran before implementation on an isolated byte copy because their harness writes evidence metadata; shared runtime source was unchanged. Final learner tests ran in the actual learner package. Failed intermediate runs remain preserved and are explained in the [change log](M3X_PROOF_SLICE_CHANGE_LOG.md).

## Device results

Owner-reported target: iPhone Air, iOS 27 beta. Exact beta/build is unknown. Mac/Xcode/signing access remains unconfirmed. The executing host is Windows; `flutter build ios` is unavailable. iOS build, simulator, native integration, gestures, physical app termination, haptics and performance: **NOT EXECUTED**. See [device evidence](M3X_PROOF_SLICE_DEVICE_EVIDENCE.md) and [numbered runbook](M3X_IPHONE_RUNBOOK.md).

## Accessibility results

Host tests verify semantic properties, logical answer/explanation adjacency, one announcement, text wrapping/reachability, non-color verdict/status and the animation-free path. Button + selected + mutually-exclusive-group is a **provisional** answer representation until VoiceOver validates the spoken role and focus behavior. No code requests focus at the top after submit.

Fourteen raw host captures are retained. Host tests substitute Inter for unavailable Cupertino system fonts; some isolated widget harnesses use the SDK default Cupertino theme/debug banner. They are structural evidence, not native SF typography or final color acceptance. The contact sheet is a labelled derivative; original PNGs remain unedited. Physical VoiceOver, Dynamic Type categories, increased contrast and Reduce Transparency remain NOT EXECUTED. See [accessibility report](M3X_PROOF_SLICE_ACCESSIBILITY.md).

## Persistence/offline results

There was no production queue to reuse. Every new proof scenario uses the same first `LearningStore` boundary: one account-scoped snapshot contains sessions, response history, origin and serialized business commands. A successful flushed write and replacement precedes “Đã lưu trên thiết bị”. Failed storage does not advance visible committed state. The separate fixture ledger represents server receipts, not a second client queue. No telemetry queue or scoring-as-telemetry path was added.

First response cannot be overwritten through the exposed model. Retry appends a response with assistance and a new attempt/command identity. Offline submit stores exact revision/grant/package/install IDs and original command bytes; no local feedback or canonical score is fabricated. Connectivity only permits transport. Only a valid matching accepted/duplicate ACK produces synced; denial/rejection/conflict remains explicit. Duplicate replay preserves its receipt and one server attempt. New scoring/completion credits are not invented: proof activities are optional and canonical completion remains zero.

The Dart process probe was actually terminated and relaunched on Windows; it restored exact content, pins, two distinct responses, pending commands and origin. This proves the common store under that host boundary. It does not prove iOS app termination, filesystem power-loss behavior, encrypted account storage, multi-writer safety, real grants/revocations or production networking. The in-process controlled server contains fixture answer keys; it must never be shipped as production scoring infrastructure. Production evidence transport for assistance remains integration debt; the frozen submit payload was not extended.

## Known defects

No failing automated case remains in the final learner suite. Device acceptance is unproven, and pinned Flutter 3.32.8 compatibility with the owner's exact iOS beta/Xcode combination is unknown. These are blocking verification gaps. The generated iOS target 12.0 is a template value, not a proven minimum. Result Pending is seeded once per installation/key; after its ACK, reopening that same fixture truthfully shows synced—use a fresh disposable fixture installation for another pending demonstration.

## Deferred debt

Physical acceptance and build compatibility; production server/auth/permission and assistance-evidence integration; broad offline failure/revocation testing; storage encryption/recovery/migrations/multi-writer behavior; external learner/staff usability; production accessibility certification; Android TalkBack; production ML/risk/recommendation; final blue/artwork/haptic freeze. Ownership and exit evidence are in [open debt](M3X_PROOF_SLICE_OPEN_DEBT.md).

## Design changes required, if any

Only the requested F-M3X-004 corrections and readable opaque platform fallback. No art-direction restart. The five signatures are represented behaviorally: reasoned Resume, situation/intention, answer-to-explanation continuity, distinct response evidence and one useful Result takeaway. Broader visual propagation remains gated.

## Architecture changes required, if any

None established. V3.2 remains frozen. Controlled server and deterministic eligibility/retry values are labelled proof infrastructure/configuration. No new backend, state-management framework or parallel command queue was introduced. No production architecture acceptance is inferred from this scoped storage implementation.

## Propagation Authorization recommendation

**HOLD.** The smallest next action is to resolve Mac/Xcode/signing access, build this exact source candidate, then execute the iPhone protocol with recorded VoiceOver, native Close/Resume, actual termination/relaunch, sync and performance evidence. Repair any observed blocker and rerun only affected checks before re-evaluating the gate. See [gate](M3X_PROOF_SLICE_GATE.md).
