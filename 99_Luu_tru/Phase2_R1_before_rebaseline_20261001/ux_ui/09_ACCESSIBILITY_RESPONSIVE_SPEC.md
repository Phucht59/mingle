# Accessibility and Responsive Specification

Target: WCAG 2.2 AA-oriented product baseline; later production audit remains Phase 13 responsibility.

## Learner Android-first

Primary design range 360–480 CSS/dp-equivalent width; content max 560px. Critical touch targets target ≥48dp. Text scaling must not hide primary actions or create horizontal scrolling. Learning cards stack vertically; answer text wraps; bottom actions remain reachable without relying on fixed tiny controls.

## Staff Web

Wide desktop ≥1280: persistent 248px sidebar. Compact laptop around 1024: collapsible/compact sidebar; tables remain usable. 768 is fallback for essential staff access, not a commitment to full mobile-admin parity.

## Accessibility requirements

- Visible keyboard focus for staff and web prototype.
- Logical focus order and semantic headings/landmarks.
- Controls have meaningful accessible names; icon-only critical actions require labels/tooltips.
- Semantic status is never color-only.
- Errors identify problem + recovery text.
- Audio-dependent tasks expose availability/assessment condition without pretending equivalence when unavailable.
- Reduced-motion preference respected.
- Target contrast is AA for normal text/controls; visual QA must test actual rendered combinations.
- Time is not used to auto-cut an unfinished learner response in the default cycle.

## Accessibility-specific learning integrity

Accessibility accommodations/preferences must be recorded as context where they affect assessment conditions; they do not silently transform assisted evidence into unaided evidence.


## Rework R1 focus/live-region contract

Detailed route focus, modal focus containment/restore, targeted live-region behavior, programmatic accessible names and 200% scaling requirements are normative in `16_ACCESSIBILITY_FOCUS_LIVE_REGION_SPEC.md`. Whole-app live regions are prohibited.
