# V3.2 Architecture / Contract Baseline Summary

## Authority

V3.2 is the implementation source of truth.

## Recorded validation state

- 115 contract checks passed.
- 22 SQL checks passed.
- Overall baseline after revision recorded as 9/10.

## Meaning of the baseline

V3.2 is not equivalent to a working product. It proves specification/contract consistency at the level covered by the checks. It does **not** prove runtime behavior such as:

- integration correctness;
- transactional/concurrency correctness;
- offline race handling;
- auth/security behavior;
- deployment behavior;
- operational resilience;
- end-to-end user flows.

## Change policy

Do not silently reinterpret business rules in implementation. If implementation exposes a contradiction, missing constraint, or blocker, create an Implementation Issue / Change Request that includes:

1. observed problem;
2. affected V3.2 rule/contract;
3. reproduction or implementation evidence;
4. proposed change;
5. compatibility/migration impact;
6. tests required to prove the resolution.

## Original source intake

On 2026-09-26 the owner supplied the completed V3.2 package. All 102 original files
are now preserved under `02_Tai_lieu_du_an/05_Kien_truc_he_thong/contracts/v3_2/source/`, with verified hashes
under `02_Tai_lieu_du_an/08_Ban_giao/provenance/v3_2/`. The original 115 contract and 22 PGlite SQL checks
have been rerun successfully; see current evidence under `03_Kiem_thu/Bang_chung/v3_2/`.
PGlite is not native multi-connection concurrency, and these checks do not constitute
full application or production acceptance.
