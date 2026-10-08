# M3.X proof slice — change log

Run identity: 20261007. Source is on `codex/m3x-proof-slice-native-companion`; base commit `9baeffa43d02e9ff4eb1feb2b012a831dbbf72a9`. No commit, push or history rewrite was performed. Existing dirty GĐ1 changes predate this task.

## Intake and baseline

- Retained the supplied context ZIP and nested artifacts without rewriting bytes; verified CRC and all 41 supplied manifest entries.
- Initial intake correctly held source implementation for missing M1/M2 canonical documents. Owner supplied the canonical supplement; retained its bytes, verified all five manifest entries and read all four complete documents before editing source.
- Recorded source/state/contract mapping and planned files in intake. Ran shared 275-test and learner 1-test baselines in an isolated byte copy; 240 baseline inputs remained unchanged. Ran original V3.2 115+22 suite and checked 102 original hashes.

## Implementation

- Added opt-in Cupertino shell and focused Practice route with retained Home origin.
- Added immutable response records, exact cached content, assistance condition, new attempt/command identity on retry and a configurable proof policy.
- Added one account-bound session/command repository boundary with flushed file replacement, explicit storage errors and conservative size bound; no in-memory “saved” success.
- Added explicit controlled server boundary, durable receipt ledger, strict command identity/revision checks, idempotency and ACK reconciliation. Offline selection/submit cannot fabricate server feedback.
- Implemented inline answer expansion, independent Check, labelled closure fixtures, Sync Recovery and requested Welcome/affordance/microcopy fixes.
- Added native integration source, host process-death probe, additive tests and raw host captures.
- Promoted already-resolved crypto 3.0.7 and path_provider 2.1.5 to direct pins. Added cupertino_icons 1.0.8 because the required icon font was absent. The intake's proposed crypto 3.0.6 value is corrected in its addendum. Flutter/Dart and unrelated dependency versions are unchanged.

## Failed and corrected verification

Failures were development evidence, not hidden or rewritten as pass:

| Observation | Correction / retained evidence |
|---|---|
| Initial analyzer errors (Semantics construction, unused import/style) | Corrected; final analyzer reports no issues |
| Initial widget run did not finish after asynchronous tap/IO frame scheduling issues | Task-owned tester process was stopped; this terminal observation has no complete raw log and is not counted as a passing run |
| Follow-up widget attempts failed | Raw `widget_attempt_2.log`, `widget_attempt_3.log` retained; async test interactions/font loading and semantic containers corrected |
| Answer/explanation merged into one semantic label | Separate semantic containers; final selected/enabled/name/adjacency assertions pass |
| Zero-duration AnimatedSize produced layout mutation under Reduce Motion | Animation-free branch, with stable answer identity; final test passes |
| Large-text CTA test tapped before scrolling settled | Harness waits after ensureVisible and scrolls lazy children into view; `large_text_diagnostic.log` and `large_text_corrected.log` retained |
| Earlier suite still had one large-text failure | `learner_test_attempt_4.jsonl` retained; superseded by successful `learner_final_tests.jsonl` and final release-candidate log |
| Draft restore could otherwise resolve against current fixture content | Session caches exact authored TaskItem with revisions/options; stale draft test now rejects old content without repinning |
| Re-auth could otherwise be lost on relaunch | Derived re-auth requirement from durable queue on open; relaunch test passes |
| Welcome Explore originally only dismissed | It now selects/persists the Learn shell destination; final widget assertion passes |

Final executed learner run: **44 passed, 0 failed, 0 skipped**. Final formatter: zero changes. Final analyzer: no issues. Default web build: PASS. The native integration helper now waits for real file writes as well as animation settlement; it is analyzed but has not run on iOS.

## Build handoff

Generated a standard isolated iOS host with Flutter 3.32.8, inspected target 12.0 and placeholder bundle ID, synchronized authored source and verified matching hashes. Windows iOS build attempt remains unavailable (exit 64). Source ZIP is explicitly unbuilt; it contains no IPA, signing identity or credentials. Device protocol and evidence templates preserve this limitation.

No Native Companion redesign, V3.2 amendment, production auth/backend implementation, broad UI propagation or historical milestone closure was performed. The scoped gate remains HOLD.
