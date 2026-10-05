# QC Review Checklist

QC is conformity/completeness review before behavior QA.

- [ ] Handoff index matches actual files.
- [ ] V3.2 original directory unchanged by Phase 2 work.
- [ ] Phase status clearly says REWORK R1 READY FOR CODEX / INDEPENDENT QA RETEST, not DONE.
- [ ] Screen inventory IDs/routes unique.
- [ ] Independent Candidate-v1 audit is preserved unchanged under `audits/2026-09-27_independent`.
- [ ] Canonical retest inventory is 94 cases and includes QA-LRN-021/022/023, QA-STF-011, QA-ACC-013, QA-HO-006 and QA-OFF-007.
- [ ] Screen→State→Rule→QA traceability covers all 57 screen IDs.
- [ ] All 16 P2-D001..P2-D016 fixes are listed READY FOR RETEST, not falsely CLOSED.
- [ ] PRD-01..16 all mapped.
- [ ] Locked rules vs hypotheses clearly differentiated.
- [ ] No production-risk/mastery/efficacy overclaim.
- [ ] No plaintext secret/token/credential in Phase 2 artifacts.
- [ ] Prototype is self-contained and labelled non-production.
- [ ] Design token JSON parses and matches design-system semantics.
- [ ] Learner and staff navigation match IA spec.
- [ ] Developer handoff references canonical files.
- [ ] QA workbook contains test cases, defect log and signoff.
- [ ] SHA-256 manifest validates after handoff packaging.
