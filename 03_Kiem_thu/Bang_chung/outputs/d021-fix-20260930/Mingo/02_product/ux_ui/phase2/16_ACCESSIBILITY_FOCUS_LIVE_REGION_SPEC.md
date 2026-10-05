# Accessibility / Focus / Live Region Addendum — Rework R1

This addendum is normative for Phase 2 and supplements `09_ACCESSIBILITY_RESPONSIVE_SPEC.md`.

## Route/page focus

- On a full route/screen change, move programmatic focus to the new screen H1/title with `tabindex=-1` (or Flutter semantic focus equivalent).
- Selecting an answer or updating inline feedback must **not** reset focus to the page heading.
- Restored navigation returns focus to a logical trigger when possible.

## Dialog / sheet focus

- Use modal semantics for publish confirmation and locked-objective preview.
- Focus enters the modal at a meaningful control/title.
- Keyboard focus cannot escape the modal while it is open.
- Escape/Cancel closes when safe.
- On close/cancel, restore focus to the invoking control.

## Live regions

Do **not** put the entire SPA/page container in a live region. Use small targeted regions only for:
- form validation/errors (`alert` where interruption is necessary),
- sync/status updates,
- result/feedback status,
- non-visual confirmations.

Avoid re-announcing full screens after every selection/rerender.

## Programmatic names

Every form control has one stable accessible name through native `<label for>` / `id` or equivalent Flutter Semantics. Placeholder text is not a label. Icon-only actions require semantic labels.

## Keyboard and touch

- Logical DOM/focus order follows visual/task order.
- All actionable controls are keyboard operable on Web.
- Mobile touch target baseline remains 48dp; WCAG pointer-target checks are validated separately.

## Scaling and reflow

- Learner surfaces must remain functional at 200% text scaling and 320/360/412/480px representative widths.
- Staff essential workflows must remain usable at 1024px and 1440px; 768px is fallback, not mobile-admin parity.
- No critical action may disappear solely due to text scaling or compact layout.

## Flutter translation

HTML ARIA is prototype evidence only. Flutter implementation must map intent to `Semantics`, focus traversal, `FocusNode`/route focus behavior, modal focus management and TalkBack/keyboard tests.
