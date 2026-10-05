# 04 — Offline Content & Access Protocol

## 1. Three separate objects

### ContentReleaseManifest — immutable
Defines exact published learning content graph and immutable resource references.

### ReleaseAccessStatus — mutable
Defines current server access status:
- `published`
- `retired`
- `soft_revoked`
- `hard_revoked`

It is not included in the release content hash.

### OfflineDownloadGrant — account/enrollment scoped
Authorizes one learner/enrollment/device package to learn offline for a bounded period.

## 2. Manifest hashing

`release_manifest_sha256` is a detached SHA-256 over:
`JCS(manifest_content)`.

The digest field itself is **not** inside `manifest_content`.

Mutable access status and grants are outside the content hash.

## 3. Offline grant

Server-stored grant fields:
- grant ID;
- learner ID;
- enrollment ID;
- device installation ID;
- course release ID;
- release manifest SHA-256;
- package ID;
- issued_at;
- learn_until;
- upload_until;
- policy version;
- revoked_at if grant itself is revoked.

Pilot defaults:
- `learn_until = issued_at + 7 days`
- `upload_until = learn_until + 48 hours`

These are configurable protocol values, not scientific claims.

## 4. Submission mode

### Online
- `submission_mode=online`
- no offline grant required;
- learner must be authorized for pinned release/activity at request time.

### Offline
- `submission_mode=offline`
- `offline_grant_id` required;
- grant owner/enrollment/release/package must match.

## 5. Offline time semantics

Client `occurred_at` is not strong anti-cheat evidence.

Pilot practice acceptance primarily requires:
- grant was validly issued;
- command references its pinned release/activity;
- server receives **new command** no later than `upload_until`;
- access/revoke policy allows acceptance.

Client time is stored with clock-quality metadata and used for sequence/analytics, not as sole security proof.

Flutter UI should stop normal offline learning after `learn_until`, but a manipulated device clock cannot be treated as authoritative.

## 6. Revoke/expiry matrix for NEW commands

| Release status | Grant state | New offline command |
|---|---|---|
| published | received ≤ upload_until | accept if other validation passes |
| retired | received ≤ upload_until | accept for already-enrolled/granted release |
| soft_revoked | received ≤ upload_until | accept only if grant issued strictly before soft revoke; otherwise reject OFFLINE_GRANT_INVALID |
| hard_revoked | any | reject `CONTENT_HARD_REVOKED` |
| any | received > upload_until | reject `OFFLINE_UPLOAD_WINDOW_EXPIRED` |

## 7. Already committed commands

If a command already has any terminal receipt:
- later expiry/revoke does not erase history;
- retry/lookup returns the existing authorized learner's receipt;
- no new completion credit is created.

## 8. Hard revoke limitation

A device with no network cannot be remotely erased instantly.

Hard revoke is enforced:
- when access status refreshes;
- at submit/sync;
- at next online package validation.

The system does not claim instantaneous revocation while fully offline.

## 9. Hard-revoked activity and progress

Baseline policy:
- historical accepted attempts/credits remain audit history;
- no new attempts accepted;
- denominator/progress is **not silently changed**;
- if product owner needs a replacement activity, publish/migrate through an explicit course-release migration policy.

## 10. Offline package

Package manifest binds:
- package ID;
- grant ID;
- release manifest hash;
- immutable content-resource references;
- asset ID + revision/hash + size;
- package checksum.

Client verifies package/resource checksums before use.

## 11. Resource graph

Release content contains typed unit → lesson → release-activity references.
Activity revision references exact question revisions and media resources.

No mutable "latest question" resolution is permitted inside an offline package.

## V3.2 precedence, grant retry and learner package

Evaluation for NEW offline commands: authenticated object scope → grant/package/installation/release binding → current release status → grant revocation → server receipt deadline → content/answers. Hard revoke takes precedence over upload expiry; grant revoked at/before received_at rejects with OFFLINE_GRANT_REVOKED. Equality at upload_until is accepted. No acceptance before issued_at.

New grants are issued only for a published release. Retired/soft-revoked releases issue no new grant; existing eligible grants follow the matrix. Grant issuance is idempotent on `(learner_id, grant_request_id)`; a retry returns the same package, grant and deadlines, not a freshly extended entitlement. Changed input under the same request ID conflicts.

NEW online commands require published or retired release, active enrollment and current object permission. Soft/hard revocation blocks new online submissions. Offline and online mode remain practice semantics, not an anti-cheat boundary: the system does not claim proof that an action was performed without a network.

`offline_package_v1.schema.json` binds the account grant to the release and resource IDs. Package digest hashes the descriptor without `package_sha256`. Each resource hashes its delivered bytes; content is fetched through the authorized immutable resource endpoint. Revocation status and expiring access URLs are excluded from content hashes. Pending command history is retained locally when an asset expires.

Media quota: 250 MiB/account/device. Eviction can remove downloaded assets, never pending commands. Queue storage has its own configurable 20 MiB budget; warn/stop accepting new offline submissions when full, preserve already queued work. Logout isolates encrypted account queues and explains pending work. Foreground launch/resume/reconnect and manual refresh trigger sync; no promise of permanent background execution.

The grant/package fixtures have real calculable descriptor/content hashes; server-only answer keys and model fixtures are not downloadable learner resources.
