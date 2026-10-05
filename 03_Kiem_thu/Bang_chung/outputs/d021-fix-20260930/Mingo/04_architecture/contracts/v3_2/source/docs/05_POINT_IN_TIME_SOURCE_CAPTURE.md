# 05 — Point-in-Time Source Capture & Availability

## 1. Why `available_at` cannot be a transaction `now()`

The system does not define `available_at` as a guessed database commit timestamp.

Instead it introduces an analytical **EvidencePublication** layer.

## 2. EvidencePublication

Authoritative/telemetry transactions emit outbox records.

A worker can only consume source rows after their transactions are committed.

The worker then publishes an immutable `evidence_publication` record:
- publication ID;
- learner/enrollment;
- source type + source primary key/revision;
- source occurred time;
- `published_available_at = clock time during publication transaction`;
- publication sequence/revision;
- payload/reference hash.

Therefore analytical availability cannot predate source commit visibility to the worker.

It may be later than the source commit, which is acceptable and conservative for leakage prevention.

## 3. Feature builder source transaction

Serving feature construction begins a PostgreSQL **REPEATABLE READ** transaction.

Inside that same consistent DB snapshot it:
1. reads eligible evidence publications with `published_available_at <= knowledge_cutoff_at`;
2. reads pinned profile/progress/content/scoring revisions;
3. writes/builds an exact SourceCapture manifest reference;
4. computes feature payload from that captured set.

## 4. SourceCapture

A SourceCapture is immutable and contains/references:
- learner/enrollment;
- serving mode (`serving` or `research_restatement`);
- event cutoff;
- knowledge cutoff;
- exact evidence publication IDs or immutable manifest file containing them;
- profile/progress/content/scoring revisions;
- manifest SHA-256;
- source count;
- generated time.

For large evidence sets, IDs are stored in immutable object storage; DB stores URI/reference + hash.

## 5. Replayability

`replayability_status=replayable` requires:
- non-null `source_capture_id`;
- source capture manifest hash;
- referenced source objects/revisions still retained or archived.

If retention/deletion makes exact replay impossible:
- status changes in metadata to `partially_replayable` or `not_replayable_due_to_retention_or_deletion`;
- historical feature/prediction output itself is not silently rewritten.

## 6. Serving vs research

`serving`:
- models what was actually analytically available.

`research_restatement`:
- may incorporate later-arriving evidence;
- has separate scope;
- never updates serving latest pointer.

## 7. Latest pointer

Scope key:
`(learner_id, enrollment_id, artifact_kind, serving_mode, computation_family, computation_version)`.

Within the same scope:
- `source_revision` is numeric;
- publish uses row lock/CAS;
- higher `source_revision` may advance latest;
- lower/stale worker result cannot.

`computation_version` strings are never lexically ordered (no v2/v10 comparison).

Active computation version is selected by a separate versioned rollout/config record.

## 8. Long transaction example

Source transaction starts 09:59 and commits 10:01.
Its evidence publication can only occur after commit visibility, so publication availability is >10:01.
Serving replay for knowledge cutoff 10:00 cannot include it.

## 9. Mutable state

Profile/progress is not read as unversioned "current row" for replay.

SourceCapture pins:
- profile revision if used;
- progress revision if used;
- relevant content/scoring versions.

## V3.2 correction: publication transaction visibility

`published_available_at` is a recorded publication timestamp, NOT its transaction commit time. A publication transaction may itself start before cutoff and commit after cutoff. Timestamp filtering alone cannot reconstruct historical visibility, even though it never precedes the earlier source commit.

For a NEW serving capture, `knowledge_cutoff_at = capture_started_at`, assigned at acquisition of the actual REPEATABLE READ read view; the captured member IDs are the authority. All reads of evidence and mutable-state revisions use that same view. State revisions must come from eligible published evidence in the captured set, not a newer operational current row. The capture manifest records the exact selected IDs plus their source revisions/content hashes. A late publication excluded by that read view remains excluded from that capture forever.

A REPLAY uses the original SourceCapture and retained immutable payloads. It must never re-query current publications with an old wall-clock cutoff and claim that this recovers historical MVCC visibility. If no original capture exists, label any reconstruction research_restatement. Preserve source_count, detached JCS manifest hash and source_capture_sha256 in the feature snapshot.

For large captures, materialize the selected IDs/revisions into a DB capture staging record within the consistent transaction, then export immutable bytes and publish the capture only after checksum validation. Do not keep a database transaction open during model inference or large uploads. Unpublished staging artifacts are cleaned on failure; snapshots reference only fully published captures.

`source_revision` is allocated per learner/enrollment/computation scope while creating the original capture. Allocation/publish uses serialized scope access; later-finishing older jobs cannot allocate themselves a newer source revision. Version rollout selects a scope; version strings are never compared. Capture membership and hashes, not sequence maxima, establish replay provenance.

Replayability metadata may later mark sources deleted; the original feature payload and published prediction remain immutable history for the permitted retention period. A schema reference alone cannot prove data still exists; the resolver must check it.
