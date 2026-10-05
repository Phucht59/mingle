# 09 — Recommendation Audit V3

## Decision

Stores:
- evidence references;
- candidate set reference;
- policy version;
- decision source;
- optional prediction ID;
- exact target resource revision;
- validity window.

For rule/statistical/model/experiment decision:
- candidate set reference required.
For staff decision:
- candidate set may be absent, but evidence/reason is still auditable.

## Exposure

Exposure has unique `exposure_id`.

Both UI API and telemetry use the same exposure ID.
Server deduplicates by `(learner_id, exposure_id)`.

A decision can have multiple distinct exposures.

## Action execution

Separate record:
- started;
- completed;
- dismissed;
- failed.

Completion comes from authoritative action contract, e.g. a canonical activity completion credit.

## Outcome

Outcome links directly to `decision_id`.
`action_execution_id` is optional because an outcome can be:
- censored;
- not eligible;
- observed after no execution;
- insufficient evidence.

Outcome defines:
- metric version;
- observation window;
- event/knowledge cutoff;
- eligibility state;
- competing intervention references where available.

Association is not claimed as causality without experimental/causal design.
