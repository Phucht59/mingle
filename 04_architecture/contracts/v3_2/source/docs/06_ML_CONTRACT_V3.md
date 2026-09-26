# 06 — Feature / Model / Prediction Contract V3

## 1. Feature shapes

- Static `[B, D_s]`
- Temporal `[B, T, D_t]`
- Aggregate `[B, D_a]`

Dimensions are properties of a feature schema version, not product constants.

## 2. Every feature definition includes

- name;
- unique contiguous position within its branch;
- dtype;
- unit;
- semantic definition;
- source/evidence class;
- missingness policy;
- valid range or explicit unbounded declaration;
- time-window definition/reference;
- preprocessing reference.

Temporal schema additionally defines:
- time bin;
- sequence order;
- padding;
- length;
- mask behavior.

JSON Schema validates shape.  
Semantic validator validates cross-feature uniqueness/contiguity.

## 3. Model bundle

A bundle pins:
- immutable bundle ID;
- model version;
- model artifact hash;
- feature schema version/hash;
- preprocessing artifact hash;
- target version;
- horizon version;
- calibration;
- threshold version/value;
- uncertainty method/version;
- runtime framework/library versions;
- validation record ID/hash;
- release status.

## 4. Deployment gate

For `shadow`, `staff_only`, `controlled`, or `production`:
- target/horizon cannot be placeholders;
- artifact hashes must resolve;
- runtime contract must be complete;
- validation record must exist;
- feature schema hash must match registered schema;
- semantic validator must pass;
- shadow/offline gate required according to rollout stage.

Candidate bundles may contain unresolved placeholders but cannot be promoted.

## 5. Prediction status

### `available`
Must contain:
- bundle ID/hash;
- feature snapshot ID;
- target/horizon;
- probability;
- threshold value/version;
- label;
- margin + definition;
- uncertainty value/method/version;
- generated/as-of.

### Non-available
One of:
- `insufficient_data`
- `model_unavailable`
- `schema_mismatch`
- `out_of_scope`
- `expired`

Must **not** carry numeric probability/threshold/label/margin/uncertainty values.

There is no fake `p=0`.

## 6. Uncertainty

If binary entropy:
`H2(p) = -p log2 p - (1-p) log2(1-p)`.

For `p=0.73`, `H2≈0.8415`.

Entropy is only the named uncertainty statistic; it is not automatically equivalent to epistemic confidence/OOD detection.

## 7. Cross-record validation

Inference service verifies:
- prediction target/horizon = bundle target/horizon;
- bundle feature schema = snapshot feature schema;
- artifact hashes match registry;
- feature dimensions/order/missingness fit schema;
- threshold used matches bundle/threshold version.

Mismatch → abstain/error state, never implicit conversion.

## 8. Dataset/training gate

Before training:
- target/horizon;
- observation unit;
- eligibility/cohort;
- label maturity;
- censoring;
- source capture policy;
- split;
- preprocessing fit boundary;
- dataset manifest;
- delete/tombstone exclusions.

Unmatured outcomes are not negative labels.

## V3.2 executable validation boundaries

The reference checker now verifies actual JCS bundle hashes, label = probability >= threshold, margin, entropy and uncertainty/calibration versions, schema/preprocess/snapshot links and capture/payload hashes. Feature array order must equal positions 0..N−1; an unordered contiguous set is insufficient.

Every hash has declared encoding: JSON contract hashes use RFC8785 JCS; media/resource bytes use raw SHA-256. `json.dumps(sort_keys=True)` is not the JCS algorithm. The bundled Python implementation uses rfc8785 and rejects duplicate raw JSON keys.

All sample model/target/horizon/validation files are explicit fixtures, NOT trained weights or a research conclusion. The sample bundle remains candidate. For shadow/staff_only/controlled/production the gate requires a trusted artifact-registry snapshot, actual resolved bytes/hashes, exact runtime versions, non-fixture target/horizon marked ready, and a validation record that approves the requested stage for the same model and schema. A user-supplied registry or the sample fixture registry is never authority for production promotion.

This registry validation verifies supplied metadata and files; it does not run training/evaluate scientific quality or certify the signer/approval process. The deployment system authenticates registry provenance and approvals; runtime model-loading/accuracy/latency and security tests remain release gates.

Predictions may have null feature_snapshot_id when no feature snapshot could be produced, but available predictions require it. Expiry is a serving response state computed from immutable prediction validity; never rewrite an available historical record to erase its original outputs.

Only REVIEW_ACTIVITY is in the reference action contract. Expanding the catalog requires a new typed action contract. The sample recommendation is optional practice based on completed activity evidence; it does not claim listening decline from unvalidated data.

The sample feature payload contains raw semantic feature values before model preprocessing: `answered_count=2` is a count, not `log1p(2)`. The declared `preprocessing_ref` identifies the transform to run when constructing model input; fitted transforms must be fit on the training partition only and applied exactly once. This fixture does not include or validate a preprocessing runner, tensor generation, or trained inference. Raw-value ranges apply before that transform.
