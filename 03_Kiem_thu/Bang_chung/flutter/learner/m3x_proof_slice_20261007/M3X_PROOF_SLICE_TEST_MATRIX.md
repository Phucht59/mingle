# M3.X proof slice — test matrix

Run identity: 20261007. AUTOMATED PASS and DEVICE PASS are separate columns. Canonical state/UXA mapping follows the owner-supplied M1/M2 supplement. A mapping is not a new live Linear acceptance.

| Concern / canonical scope | Executed automated evidence | Automated result | Device result |
|---|---|---|---|
| HOME-01/10, UXA-P0-003/004: one Resume and reason | Domain deterministic Resume; widget Home at nonzero scroll → Practice → Close → Resume; tab hidden in focus and origin preserved | PASS | NOT EXECUTED: native gestures/origin |
| TASK-02..05, UXA-P0-006: selection → submit | Durable submit, duplicate tap guard, late selection rejected; selected/enabled semantics; required selection | PASS | NOT EXECUTED: VoiceOver and input latency |
| TASK-06..10, FB-01..04, UXA-P0-007 | Same keyed answer Element/top; verdict/correction/explanation inside answer; first response immutable; retry separate/new attempt; hint assistance persistent | PASS | NOT EXECUTED: perceived continuity/focus |
| Correct retry policy, F-M3X-004 | Default hides correct Retry; explicit configuration can allow; response history action | PASS | NOT EXECUTED: action reading |
| CHK-02..08, UXA-P0-008 | No Hint control; domain rejects hint/retry; independent condition and exact content restored from native-file store on host | PASS | NOT EXECUTED: iOS interrupted Check |
| RES-01/03/04/05/07, UXA-P0-009 | Finite labelled fixture, Xong primary, Học tiếp invokes new eligibility decision; no auto-launch | PASS | NOT EXECUTED: native sheet/focus |
| TASK-14..16, SYNC-01..09, UXA-P0-011/012/013 | Pending/syncing/ACK, connectivity without ACK, failed save, re-auth, stale/conflict/rejection and explicit recovery | PASS | NOT EXECUTED: physical interruption/network conditions |
| Evidence integrity | First response immutable, assisted retry, independent condition, exposed histories deep-frozen, exact cached prompt/revision and serialized command retained | PASS | NOT EXECUTED: physical container readback |
| ACK integrity | Wrong owner/digest/attempt/scope denied; old ACK cannot roll back current progress; incompatible same revision requires refetch | PASS | NOT EXECUTED: real server integration (out of slice) |
| Idempotency | Duplicate replay has identical receipt and one attempt; altered same-ID payload conflicts; new command on finalized attempt rejected; ACK-local-write failure replay recovers | PASS | NOT EXECUTED: device replay/container ledger |
| Durability | Real FileLearningStore reopen; corrupt file retained; host process terminated/relaunched with exact snapshot; injected write failures show no save success | HOST PASS | NOT EXECUTED: native app kill/relaunch and OS storage behavior |
| WLC-01/02, F-M3X-004 | Bắt đầu primary, Explore secondary opens Learn shell; bookmark false affordance absent | PASS | NOT EXECUTED: native presentation |
| Large text/narrow width | 320×568 at 3.2×; long Vietnamese/English at 2×; expanded rows and reachable CTA; no framework exception | PASS | NOT EXECUTED: actual accessibility text categories |
| Answer accessibility | Button + selected/enabled + mutually-exclusive-group; verdict announcement once; separate adjacent explanation semantics | HOST SEMANTICS PASS | NOT EXECUTED: VoiceOver role/focus/traversal |
| Reduce Motion | Animation-free branch with identity/meaning preserved | PASS | NOT EXECUTED: system setting |
| Dark/non-color states | Dark capture; text/icon/state distinction; opaque surfaces | HOST PASS | NOT EXECUTED: device contrast/increased contrast/transparency |
| Touch targets | Essential answer/action Cupertino controls ≥44×44 logical points in task test | SCOPED PASS | NOT EXECUTED: full shell/trailing/sheet hit areas on phone |
| Performance/haptics | No blur/shader answer stack; selection haptic opt-in default off | SOURCE REVIEW ONLY | NOT EXECUTED: frame timings/physical haptic |

## Executed runs

| Run | Boundary | Outcome |
|---|---|---|
| Original baseline | Byte-copy shared/learner; hashes checked before/after | 275 shared + 1 learner pass; no skipped/failed; 240 original inputs unchanged |
| Intermediate widget attempts | Windows Flutter test harness | Failures retained in logs; see change log |
| Final learner tests | Actual learner package | 44 passed, 0 failed/skipped; `learner_release_candidate_tests.jsonl` |
| Final formatter/analyzer | 12 scoped Dart files / learner including integration source | Zero format changes; no analyzer issues |
| Default build web | Existing default entry | PASS; no native claim |
| Original V3.2 | Canonical 115 contract + 22 SQL, original 102 hashes | PASS; PGlite SQL scope |
| Generated wire validation | Command; accepted, duplicate accepted, rejected, duplicate rejected, conflict, denied, retryable | 8 schema checks PASS; independent Python digest PASS |
| Host process termination | Dart VM + identical FileLearningStore; Windows TerminateProcess | Exact snapshot restored; HOST_PROCESS_PASS |
| Generated iOS host | `flutter create --no-pub --platforms=ios`, Flutter 3.32.8 | Generation succeeds; authored copy hashes match |
| iOS build attempt | Windows Flutter CLI | Unavailable; exit 64, `ios` subcommand absent |
| iOS simulator integration | No accessible Xcode runtime | NOT EXECUTED |
| Real iPhone Air | Owner-reported iOS 27 beta; no execution access | NOT EXECUTED |

## Reproduction

From `01_San_pham/apps/learner`, using pinned Flutter 3.32.8/Dart 3.8.1:

```powershell
dart format --output=none --set-exit-if-changed lib/main.dart lib/m3x test/m3x_domain_test.dart test/m3x_widget_test.dart integration_test/m3x_proof_test.dart tool/m3x_process_probe.dart
flutter analyze --no-pub
flutter test --no-pub --reporter json
flutter build web --no-pub
```

Run `flutter pub get` first on a fresh source export. The final test JSON contains every executed case name and source. Raw screenshots were collected by the widget harness with `M3X_EVIDENCE_DIR` set to a new output directory; do not overwrite this run's originals. The native integration test requires a generated iOS host and Mac/Xcode; its source being analyzable does not count as execution. [Device runbook](M3X_IPHONE_RUNBOOK.md) describes the missing acceptance.
