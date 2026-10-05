# Repository inventory before migration

Audit: 2026-10-01 Asia/Saigon. No files moved. No AGENTS.md found in repository search.

| Path | Purpose | Classification / authority | Files | Bytes | Tracked | Untracked nonignored | Ignored/local | Junctions skipped |
|---|---|---|---:|---:|---:|---:|---:|---:|
| .git | Git object database | LOCAL ONLY | 370 | 38806698 | 0 | 0 | 370 | 0 |
| .gitattributes | Root navigation/configuration | CURRENT | 1 | 440 | 1 | 0 | 0 | 0 |
| .github | CI configuration | CURRENT | 1 | 2992 | 1 | 0 | 0 | 0 |
| .gitignore | Root navigation/configuration | CURRENT | 1 | 390 | 1 | 0 | 0 | 0 |
| .idea | Ignored local IDE metadata | LOCAL ONLY | 9 | 121756 | 0 | 0 | 9 | 0 |
| .local | Runtime object storage, scratch scripts, copied reproductions, verification environments and cache junction; keep in place | LOCAL ONLY | 58479 | 8528305365 | 0 | 0 | 58479 | 1 |
| .ruff_cache | Generated lint cache | GENERATED | 4 | 478 | 0 | 0 | 4 | 0 |
| .venv | User Python environment; keep in place | LOCAL ONLY | 3724 | 87163319 | 0 | 0 | 3724 | 0 |
| 01_governance | Plans, frozen decisions, status and dated snapshots; classify by file | CURRENT / HISTORICAL | 13 | 28512 | 13 | 0 | 0 | 0 |
| 02_product | Product charter, PRD, learning design, UX specifications and reference prototype | CURRENT | 34 | 276181 | 34 | 0 | 0 | 0 |
| 03_research | Scientific basis and original research inputs; not contract authority | CURRENT / HISTORICAL | 9 | 144544 | 9 | 0 | 0 | 0 |
| 04_architecture | Frozen V3.2 originals, baseline summaries and architecture guardrails | CURRENT | 115 | 328164 | 115 | 0 | 0 | 0 |
| 05_code | Runtime modular monolith with worker/migrations, Flutter apps and stack configuration | CURRENT / GENERATED / LOCAL ONLY | 1034 | 2539001977 | 35 | 0 | 999 | 0 |
| 06_quality | QA controls, gates, immutable execution evidence and newer untracked final-gate packets | CURRENT / EVIDENCE | 674 | 19171727 | 455 | 219 | 0 | 0 |
| 07_operations | Runbooks, configuration instructions and executable verification/setup tools | CURRENT | 30 | 114021 | 25 | 0 | 5 | 0 |
| 08_handoff | Handoff instructions plus immutable provenance and historical release manifests | CURRENT / HISTORICAL / EVIDENCE | 30 | 694095 | 30 | 0 | 0 | 0 |
| 99_archive | Historical deliveries and snapshots; never current authority | HISTORICAL | 57 | 602024 | 57 | 0 | 0 | 0 |
| Manage Project.xlsx | Owner project tracking workbook; move bytes without editing | CURRENT (owner managed) | 1 | 133595 | 0 | 1 | 0 | 0 |
| outputs | Untracked UX/QA derivatives, workbook exports, Android diagnostics and copied repository snapshots; preserve as generated review evidence | GENERATED / EVIDENCE | 9096 | 298452539 | 0 | 9096 | 0 | 3 |
| PROJECT_MAP.md | Root navigation/configuration | CURRENT | 1 | 2215 | 1 | 0 | 0 | 0 |
| README.md | Root navigation/configuration | CURRENT | 1 | 6229 | 1 | 0 | 0 | 0 |
| REPO_RULES.md | Root navigation/configuration | CURRENT | 1 | 1785 | 1 | 0 | 0 | 0 |
| START_HERE.md | Root navigation/configuration | CURRENT | 1 | 4297 | 1 | 0 | 0 | 0 |

Counts include hidden files but do not traverse junctions/symlinks. Git metadata is counted separately; generated host/build/cache files are not canonical source. Full per-artifact old path, new path, byte size and SHA256 are in RESTRUCTURE_BASELINE.json. Local runtime data is neither read into reports nor removed.

Initial dirty state:
```text
M 02_product/ux_ui/phase2/prototype/styles.css
?? 06_quality/phase2/final_gate/
?? "Manage Project.xlsx"
?? outputs/
```
