# MINGO R03 — Customer Visual Review / Design-to-Code Fidelity

**Status:** CANDIDATE — awaiting customer's explicit visual decision.
**Branch:** design/m3x-visual-fidelity-po-review-r03
**Technical base:** e31951a (Flutter proof slice + evidence).
**Binding authority:** V3.2 > GĐ1 business > M1 > M2 > M3.X contract > approved Native Companion design masters > this visual revision.

## Customer-facing concept

**A quiet, capable language-learning companion.** Native where familiarity matters; branded where learning has meaning; quiet during cognitive work; warm at Welcome/Return/Result. Never just default Cupertino tinted blue, and never a mascot-heavy game.

### Visual signature
- Contextual everyday scenes, in warm restrained editorial illustrations, at Home/Explore only.
- One meaningful Resume action with truthful reason. No misleading mastery/AI confidence.
- Situation → language intention → answer choices on the learning surface.
- Selected answer expands into verdict, reason and correction in the SAME object; no separate Feedback page.
- First answer remains separate from assisted retry; Independent Check has no pre-submit hint.
- Finite closure: one useful takeaway, **Xong** primary, **Học tiếp** optional.
- Sync state is honest: durable locally saved ≠ server ACK.

## Proposed 9 review surfaces
1. Welcome (Bắt đầu primary, Khám phá trước secondary).
2. Today/Home Resume.
3. Return after absence (non-punitive).
4. Learn/Explore (user agency).
5. Practice selected/correct/incorrect/pending/retry.
6. Independent Check without Hint.
7. Result (normal/pending).
8. Progress (evidence-safe, no made-up mastery).
9. Sync Recovery (pending/net-restored/ACK/conflict honest).
Staff web remains a later composition and is not approved through this learner review.

## Design candidate tokens — NOT FROZEN
- Canvas: #FAFBF8, Surface: #FFFFFF, Ink: #202C35, Secondary: #687781.
- Mingo Blue candidate: #2857C7; large accent never bleeds into native tab/navigation chrome.
- Brand support: restrained parchment #F6EDDF, sage #E6F0E9 and contextual scene blue/cream.
- Root title 32–34, prompt 23–25, section heading 17–19, body 15–17 (adaptive/scalable).
- Stable 4-tab architecture Today/Learn/Progress/Profile; focused learning hides global tabs.
- Illustration: adult everyday context, no mascot on active Practice/Check/corrective Feedback.
- Motion: only causal same-object answer expansion, reduced-motion static equivalent.
- Rounded shapes distinguish content groups only; avoid card stacking.

## Prior audit / rationale
R02/M3.X doctrine remains accepted; R03 is **visual translation refinement**, not a restart.
The existing Flutter M3.X screenshots are proof/structural evidence, **not visual masters**.
F-M3X-005 (unconditional opening write) and F-M3X-006 (feedback visibility in short viewport) remain open.
F-M3X-007 (visual fidelity gap) owns this revision.
Do not update Flutter implementation until PO sees/accepts visual candidate.

## Acceptance for design-to-code handoff
- Customer can distinguish Mingo from a stock Cupertino sample without logo/mascot alone.
- Home communicates why this action and preserves Explore.
- Practice keeps task, options and CTA legible; context scene recedes.
- Wrong feedback correction is in view or strongly discoverable before exit; action density constrained.
- Result has relief/closure without false reward.
- Large text, dark theme, motion reduction and hit areas have explicit prototype behavior.
- Native behavior remains plausible in Flutter; no glass shader or false native claim.
- PO visual signoff is separate from iOS VoiceOver, process-death, sync runtime gates.

## Explicit decision needed
Customer reviews the candidate screens and chooses:
**APPROVE DIRECTION**, **REVISE with annotated comments**, or **REJECT AND RETURN TO VISUAL WORK**.
Approval freezes only the agreed R03 layout/visual direction; exact artwork/timing/haptics and production accessibility remain candidate or verification debt.

## Handoff to Codex (after visual approval)
Preserve all domain/store/controller/server fixture contracts and 44 recorded tests.
Implement visual mapping as a small patch on a fresh code branch, screenshot comparison at 393/320 width + dark + scaled text, and run existing tests plus device tests. No full propagation before independent QC/PO acceptance.
