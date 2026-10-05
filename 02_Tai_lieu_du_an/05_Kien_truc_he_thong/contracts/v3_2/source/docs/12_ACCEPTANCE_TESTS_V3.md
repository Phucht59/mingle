# 12 — Acceptance / Adversarial Tests V3.2

This is the implementation acceptance plan, not a list of tests already executed. Only named checks in `validation_results.json` and `SQL_VALIDATION_REPORT.json` have measured PASS results. Native concurrency, client, auth, worker integration and restore scenarios below remain NOT RUN until the application exists.

## C1

- 20 concurrent identical requests same command → one accepted receipt, others duplicate.
- same command ID different answer → conflict.
- two different command IDs same attempt ID after finalization → second rejected `ATTEMPT_ALREADY_FINALIZED`.
- two devices submit different attempts same required activity → two attempts, one completion credit.
- duplicate/missing/foreign question ID → rejected.
- invalid option → rejected.
- repeat attempt cannot make completion fraction >1.
- release with zero required activities → publish rejected.

## C2

- accepted transport includes terminal receipt + current canonical progress.
- duplicate accepted transport includes original receipt + current canonical progress; duplicate rejected retains rejection and may have null current state.
- denied access creates no business receipt and exposes no foreign receipt or progress.
- optional activity receives a score but creates no required completion credit.
- old duplicate receipt revision 5 when local revision 7 does not roll client back.
- unknown commit outcome retry same command ID resolves to accepted/duplicate without new attempt.
- temporary server failure creates no terminal rejected receipt.
- accepted historical receipt still lookup-able after content later retires/revokes.

## C3

- two learners on same release have distinct grants.
- same immutable release hash remains unchanged when access status changes.
- offline new command received after upload deadline is rejected.
- hard revoke rejects new command but not historical receipt lookup.
- soft retire/revoke follows deterministic matrix.
- package/resource checksum corruption detected.
- grant owner/device/enrollment mismatch rejected.

## C4

- source or publication transaction committing after the original capture read view cannot enter that capture, even when its stored timestamp is earlier than the cutoff.
- a new serving capture cannot impersonate an older read view by filtering current rows; replay loads the original exact captured membership.
- unpublished progress/scoring revisions cannot enter a capture through a current-state side query.
- feature builder under concurrent commits sees one consistent repeatable-read view.
- `replayable` snapshot without source capture rejected.
- research restatement cannot advance serving latest.
- computation version v10 vs v2 is not lexically compared.
- stale worker source revision cannot overwrite newer latest pointer.

## C5

- prediction status available without p/model/bundle/threshold/uncertainty rejected.
- model_unavailable with p=0 rejected.
- duplicate feature name or position rejected by semantic validator.
- noncontiguous positions rejected.
- production/staff bundle with placeholder target/horizon or incomplete runtime rejected.
- prediction/bundle target or horizon mismatch rejected.
- schema mismatch results in abstention/error, not implicit reshape.

## Worker

- lease expires, worker B reacquires, worker A late effect write AND completion are fenced out in the same transaction.
- relay crash after job insert does not create duplicate logical job.
- manual replay retains effect idempotency.

## Security

- learner cannot read another grant/receipt/attempt.
- instructor outside assignment denied.
- client learner ID ignored/forbidden.
- content admin cannot read raw learner risk by default.

## Delete/restore

- long-running export publication and deletion serialize on the same subject gate lock; generation mismatch aborts publication. A check followed by an unlocked write is insufficient.
- restored DB has deletion ledger reapplied before normal service resume.
