# Accessibility — current candidate 2026-10-02

**RERUN NOW / automated scoped PASS; HUMAN VALIDATION PENDING.** Current shared run has275 tests/0 failures/0 skips and205 compared PNGs. Six inherited and ten new critical theme cases exercise Flutter Android minimum48dp targets, labeled targets and rendered text contrast (4.5:1 normal,3:1 large). New cases cover Home/Learn/Summary/Course/Progress in light and dark. That sampled contrast coverage does not certify every dynamic pixel in every state.

Responsive execution: 175states×5viewports×4textscales=3500;16domain variants×3viewports×2scales=96; four320px/200% recoverycases; new ten core surfaces×3widths×4scales×2themes=240. Total3840 final-run observations without framework exceptions. A separate320px200% long-Vietnamese topic test wraps; Home action is visible above navigation at360×800 default scale without scrolling. At enlarged text, actions remain reachable by scrolling. Native button/focus semantics, semantic headings and live notices remain; art and decorative trail are excluded from semantics. Reduced-motion preference and preserved200% scale are verified by an inherited behavior case.

Initial new test harness failures (undisposed semantics handles) were corrected in the test itself, not by relaxing a guideline. Final cases pass. Android native-back/actual focus/audio execution is separately recorded; automated labels never certify speech quality. See [INDEPENDENT_VERIFICATION_PROTOCOL.md](INDEPENDENT_VERIFICATION_PROTOCOL.md) and [ACCESSIBILITY_MANUAL_CHECKLIST.md](ACCESSIBILITY_MANUAL_CHECKLIST.md).

**NOT RUN / pending humans:** physical TalkBack Vietnamese/English speech, reading/focus/announcement order, focus return after navigation, magnification, switch/keyboard user acceptance, real color-vision/high-contrast use, physical touch/audio experience. The manual checklist remains unsigned. No simulated tester, participant or HUMAN VERIFIED result exists.

Source of actual machine counts: current evidence `candidate_tests_final.jsonl`, `shared_final.jsonl`; canonical final provenance: [PHASE2_FINAL_GATE_REPORT.md](PHASE2_FINAL_GATE_REPORT.md).
