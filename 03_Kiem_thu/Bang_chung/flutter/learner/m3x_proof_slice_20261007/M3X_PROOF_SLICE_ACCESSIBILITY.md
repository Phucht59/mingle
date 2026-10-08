# M3.X proof slice — accessibility evidence

**Physical accessibility acceptance: NOT EXECUTED.** Host assertions below are engineering evidence only. The answer role remains provisional until real VoiceOver behavior is checked on the owner's iPhone Air/iOS 27 beta (exact build unknown).

| Acceptance | Implementation / executed evidence | Remaining acceptance |
|---|---|---|
| Answer name/role/state | Each answer exposes its full text, button role, selected, enabled and mutually-exclusive-group. Decorative children excluded from duplicate semantics. Widget assertions pass. | Hear each state/role in Vietnamese/English VoiceOver; verify activation and disabled state |
| Reading order | Prompt → intent → answer units; evaluated verdict/explanation/correction live within the selected unit, followed by remaining content and actions. Separate semantic containers prevent explanation merging into the answer label. | Real swipe traversal and rotor behavior; explanation must be adjacent and complete |
| Focus continuity | Stable key uses exact question revision/option; no navigation to Feedback or explicit focus-to-top call. Widget keeps the same Element/top. | VoiceOver focus must remain meaningful after submit/ACK and after sheet dismissal |
| Verdict announcement | One explicit announcement per newly ACKed command; stored feedback on reopening is not announced as a new event. Host message test passes. | Count actual spoken verdict; ensure no duplicate announcement from native semantics changes |
| Large text | Answer content has no fixed height. At large scale, actions join the scrollable flow. 320×568 at 3.2× and long bilingual text at 2× pass; essential CTA reachable. | Largest iOS accessibility text categories, bold text, safe areas, actual font metrics and orientation |
| Non-color meaning | Selection has an explicit circle state; verdict has text/icon; sync status states “chờ”, “đang”, “đã”, conflict/reauth. No checkmark before ACK. | Device appearance and perceived differentiation |
| Reduce Motion | A static content branch removes AnimatedSize entirely for disableAnimations or accessibleNavigation. Meaning and answer identity persist. | Verify iOS setting maps correctly and transition/focus remains usable |
| Reduce Transparency | Bars, tabs and answer surfaces are opaque. Standard action sheet is backed by an opaque surface; content never depends on blur. Pinned SDK has no dedicated Reduce Transparency signal in this slice. | Observe system preference on device, including sheets and contrast |
| Dark / increased contrast | Explicit light/dark candidate colors; opaque dark capture inspected. Verdict does not depend on color. | Device increased-contrast and dark appearance; no color freeze |
| Touch | Task answer/action controls meet ≥44×44 in host layout test; Close uses CupertinoButton. | Audit shell ellipsis, tab items, all sheets and large-text hit regions on phone |
| Haptics | Selection haptic experiment only, opt-in `MINGO_M3X_HAPTICS`; default off; no incorrect-answer haptic. | Physical evaluation before choosing a default |

## Semantics decision

Single-choice answers are selectable Cupertino buttons with selected state and `inMutuallyExclusiveGroup`. This is a Flutter-native candidate, not an `aria-pressed` translation. It avoids claiming radio behavior before iOS runtime evidence exists. If VoiceOver does not convey selection/grouping clearly, adjust only the affected semantic representation after recording the defect, then rerun semantic/widget and device checks. Do not infer accessibility from the presence of `Semantics` widgets.

## Repairs made during verification

- The initial semantic tree merged answer and feedback. Separate answer/verdict/explanation containers now keep the answer label stable and explanation adjacent.
- A zero-duration AnimatedSize path triggered a layout mutation assertion under the pinned SDK. Reduced motion now removes the animated wrapper rather than setting its duration to zero.
- Large-text test interaction initially tapped while `ensureVisible` was still scrolling. The harness now waits for scroll settlement and locates lazy children before interaction. A corrected run passes without changing content or hiding a failing frame.

Raw failed logs and corrected runs remain available. Inspecting host screenshots found no visible horizontal clipping in the sampled long-text/large-text states; vertical scrolling is intentional and tested. These captures use a test font substitution and cannot establish native Dynamic Type quality. No WCAG/production certification claim is made. Use the exact [device protocol](M3X_IPHONE_RUNBOOK.md) before closing accessibility acceptance.
