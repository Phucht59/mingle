# Path migration for owner-authorized Phase 2 V2

The human-readable repository layout already exists and has verified prior mapping. No new physical move is necessary. Existing staged git mv operations are retained. See preceding Tai_cau_truc_20261001 baseline/plan for full old-folder mapping.

| Old path | New path | Reason | References to update |
|---|---|---|---|
| 01_San_pham/apps/learner | Same | Keep tooling/Android project conventions | pubspec adds shared presentation package |
| 01_San_pham/apps/staff | Same | Keep web/CI paths | pubspec adds shared presentation package |
| Shared presentation code absent | 01_San_pham/cong_cu_phat_trien/mingo_ui | One token/component/type law for both apps | Local Dart package dependency |
| Phase2 R1 UX and shell | 99_Luu_tru/Phase2_R1_before_rebaseline_20261001 copy | Preserve historical bytes before authorized rework | Explicit HISTORICAL label; original captured evidence retained |
| V2 design artifacts absent | ux_ui/phase2/rebaseline_v2 | Current owner-authorized design/handoff | Root/governance/current phase2 README |
| V2 machine evidence absent | 03_Kiem_thu/QA_QC/phase2/rebaseline_v2_20261001 | Fresh run/evidence, no overwrite | QA reports and final gate |
| Research rationale absent | rebaseline_v2/PHASE2_RESEARCH_RATIONALE.md | Source-backed design decisions | Design docs and current scope decisions |

Backend/worker/migrations/V3.2/provenance remain at their verified current paths. No microservice/DB split. .git/.github/local env/IDE/cache stay root; .gitignore continues excluding generated hosts/builds/runtime cache. No destructive move/delete/overwrite of unrelated user changes.
