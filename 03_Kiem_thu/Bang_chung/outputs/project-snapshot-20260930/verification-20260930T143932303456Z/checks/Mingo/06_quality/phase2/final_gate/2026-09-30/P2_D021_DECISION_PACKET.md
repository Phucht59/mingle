# P2-D021 — Owner decision packet

**Owner decision: FIX NOW (explicit user message, 2026-09-30).** Severity P2, non-production prototype QA toolbar. D020 remains CLOSED. Fix implemented; Linux and independent retest remain pending.

Independent Linux Chromium evidence (2026-09-29): 320px viewport, 200% text scale, document scrollWidth **328px**, learner `#app` and `.phone` **320px**, zero overflowing learner descendants. Overflow was attributed to `.prototype-bar/.prototype-controls`.

New Windows Chrome measurement (2026-09-30): Home/Learn/Course/Profile all document **320px**, `#app` **320px**, zero learner and toolbar overflowing descendants. See `D021-runtime.json` for exact browser version and geometry, and four screenshots. Same computed-font-size doubling method as the candidate supplemental script. This Windows result does not invalidate the Linux observation and does not close D021.

## Option A — DEFER / ACCEPT AS NON-PRODUCTION TOOLING

- Independent evidence isolates the problem from the learner product surface.
- Keep R1 source and candidate identity intact; no D020 reopen.
- Record a deferred maintenance task: constrain QA toolbar/chips at 320px with 200% text, then verify Home/Learn/Course/Profile on Linux and Windows, document width <= viewport + 1px, no learner clipping.
- Tradeoff: the known Linux QA-toolbar overflow remains until maintenance is completed. No owner acceptance is inferred from the recommendation.

## Option B — FIX NOW

- Change only QA-toolbar styling; do not change learner UI, product behavior or frozen rules.
- Investigate min-width, chip wrapping and text overflow constraints, then rerun four 320px/200% measurements, relevant QA-ACC regression and full static/review checks.
- Tradeoff: creates a new source revision requiring targeted regression evidence; a Windows-only pass cannot prove the known Linux issue is fixed. No general R2.

Decision: **FIX NOW**. Decision-maker: project owner (user). Date: 2026-09-30. Explicit message: “fix now với sao tao k run máy ảo trên android studio dc v mày fix dùm tao đi”. No Tech Lead or Product Owner UAT acceptance is inferred.

Implementation: `02_product/ux_ui/phase2/prototype/styles.css` constrains only `.prototype-bar` and `.prototype-controls` flex children/chips, allowing wrapping at enlarged text. The learner `#app` rules and product behavior were not changed. See `d021-fix/verification.json`: rework 16/16, review 20/20, browser canonical 74/74, supplemental 30/30, JavaScript syntax PASS. Four Windows Chrome routes at 320px/200% measured document and `#app` at 320px with no overflow. The exact Linux Chromium 328px reproduction has not been rerun because this host has no Linux runtime. D021 targeted fix is implemented, but independent closure is pending.

Separate finding P2-D022 concerns the supplied workbook Dashboard. No D022 disposition is implied by a D021 choice.
