# Repository rules

1. **Do not code from `99_archive/`.** Use active folders; archive is provenance only.
2. **Do not change frozen rules silently.** Log an Implementation Issue. Use a Change Request for foundational/business-rule changes.
3. **Do not call Phase 1 DONE without gate evidence.** Use `06_quality/gates/PHASE_1_GATE.md`.
4. **Do not replace the original V3.2 115+22 suite with new tests.** New tests are additive.
5. **Keep domain authority on the server.** Client telemetry is not authoritative scoring/progress/permission state.
6. **Keep commands and telemetry separate.** Offline support must preserve this boundary.
7. **Keep published content immutable/versioned.** Pin exact revisions where specified.
8. **Avoid premature distributed infrastructure.** Modular monolith + durable worker is the current baseline.
9. **Every new important decision updates governance.** At minimum: decision register/issue/CR as applicable and progress snapshot at major milestones.
10. **Evidence is append-only in spirit.** Never rewrite a failed/blocked historical run into a pass; record a new run.
