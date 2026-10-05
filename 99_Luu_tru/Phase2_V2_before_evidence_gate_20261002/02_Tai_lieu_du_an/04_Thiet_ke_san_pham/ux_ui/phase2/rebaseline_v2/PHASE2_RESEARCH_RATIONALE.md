# Phase2 research rationale

Sources checked2026-10-01. Primary platform documents, original papers/reviews and author-origin HCI guidance. Each implication below is a Mingo design inference, not a causal result for this app. No participant data collected. Some Apple pages expose JavaScript shells; the typography limitation is explicitly recorded.

## R01

CLAIM: Hierarchy and a clear task aid understandable interfaces.

SOURCE: [Original source](https://developer.apple.com/design/human-interface-guidelines/design-principles).

EVIDENCE TYPE: Platform design guidance.

POPULATION: Apple-platform users; no controlled Mingo study.

IMPLICATION: One primary task, visible recovery.

LIMITATION: Guideline, not measured efficacy for Mingo.

WHAT MINGO DOES: Prioritize lesson action; optional onboarding.

WHAT MINGO DOES NOT CLAIM: Apple UI clone or certification.

## R02

CLAIM: Consistent adaptive layout preserves relationships.

SOURCE: [Original source](https://developer.apple.com/design/human-interface-guidelines/layout?changes=lat_3__1_2).

EVIDENCE TYPE: Platform guidance.

POPULATION: Multiple Apple device/window sizes.

IMPLICATION: Align elements, adapt and scroll.

LIMITATION: Platform scope differs from Android.

WHAT MINGO DOES: Responsive Flutter constraints and large text.

WHAT MINGO DOES NOT CLAIM: Liquid Glass required on Android.

## R03

CLAIM: Legible scalable type matters.

SOURCE: [Original source](https://developer.apple.com/design/human-interface-guidelines/accessibility?changes=latest_maj_6_3&language=objc).

EVIDENCE TYPE: Platform accessibility guidance; Typography linked by source.

POPULATION: Users with diverse vision/text-size needs.

IMPLICATION: Enlarge text to200% with layout recovery.

LIMITATION: Typography page itself exposes JS-only shell on this fetch; evidence here is the accessible related guidance.

WHAT MINGO DOES: Licensed Vietnamese Inter, native text scale, no clipping.

WHAT MINGO DOES NOT CLAIM: SF Pro licensing or typography-page quotation not retrieved.

## R04

CLAIM: Color should encode meaning consistently with contrast.

SOURCE: [Original source](https://developer.apple.com/design/human-interface-guidelines/color?changes=_5_2).

EVIDENCE TYPE: Platform guidance.

POPULATION: Apple UI contexts.

IMPLICATION: Semantic color and additional labels.

LIMITATION: Color depends on display/theme; verify actual surfaces.

WHAT MINGO DOES: Blue action plus text/icon state.

WHAT MINGO DOES NOT CLAIM: Color alone identifies correct/error.

## R05

CLAIM: Branding should serve the content.

SOURCE: [Original source](https://developer.apple.com/design/human-interface-guidelines/branding?changes=__8%2C__8).

EVIDENCE TYPE: Platform guidance.

POPULATION: Apple app users.

IMPLICATION: Sparse mascot/wordmark.

LIMITATION: No evidence mascot improves learning retention.

WHAT MINGO DOES: Original capybara on welcoming/quiet surfaces.

WHAT MINGO DOES NOT CLAIM: Brand art on every quiz.

## R06

CLAIM: Materials create hierarchy but can affect legibility.

SOURCE: [Original source](https://developer.apple.com/design/human-interface-guidelines/materials).

EVIDENCE TYPE: Platform guidance.

POPULATION: Apple material rendering.

IMPLICATION: Separate controls and readable content.

LIMITATION: Not portable prescription for FlutterAndroid.

WHAT MINGO DOES: Opaque readable surfaces.

WHAT MINGO DOES NOT CLAIM: Glass rendering or platform certification.

## R07

CLAIM: Purposeful optional brief motion avoids distraction.

SOURCE: [Original source](https://developer.apple.com/design/human-interface-guidelines/motion?changes=l_9_3).

EVIDENCE TYPE: Platform guidance.

POPULATION: People including motion-sensitive users.

IMPLICATION: Static decoration; reduced motion.

LIMITATION: Device behavior still needs manual testing.

WHAT MINGO DOES: Immediate navigation cut, no confetti.

WHAT MINGO DOES NOT CLAIM: Motion causes higher learning outcomes.

## R08

CLAIM: Android focusable touch targets should be at least48dp.

SOURCE: [Original source](https://developer.android.com/guide/topics/ui/accessibility/views/apps-views?hl=en).

EVIDENCE TYPE: Official engineering guidance.

POPULATION: Android touch and accessibility use.

IMPLICATION: 48 logical-pixel minimum.

LIMITATION: Flutter dp mapping/real device still need validation.

WHAT MINGO DOES: 48+ components, automated target tests.

WHAT MINGO DOES NOT CLAIM: WCAG AA certification from target size.

## R09

CLAIM: Screen reader behavior needs manual and user tests.

SOURCE: [Original source](https://developer.android.com/guide/topics/ui/accessibility/testing?hl=en).

EVIDENCE TYPE: Official engineering guidance.

POPULATION: Android TalkBack/Switch Access users.

IMPLICATION: Read focus/announcements and controls on device.

LIMITATION: Semantics tree or emulator boot is not audible TalkBack evidence.

WHAT MINGO DOES: Semantics tests plus an unsigned manual checklist.

WHAT MINGO DOES NOT CLAIM: TalkBack PASS without listening/use.

## R10

CLAIM: Offline-first requires deliberate data and synchronization handling.

SOURCE: [Original source](https://developer.android.com/topic/architecture/data-layer/offline-first).

EVIDENCE TYPE: Official architecture guidance.

POPULATION: Android intermittent connectivity.

IMPLICATION: Distinguish local state from acknowledged remote state.

LIMITATION: Mingo frozen queues remain authoritative; UI cannot provide durability.

WHAT MINGO DOES: Honest pending/partial/revision states.

WHAT MINGO DOES NOT CLAIM: Phase2 implements durable sync.

## R11

CLAIM: Adaptive design responds to available window space.

SOURCE: [Original source](https://developer.android.com/develop/adaptive-apps/guides/get-started-with-adaptive-apps).

EVIDENCE TYPE: Official engineering guidance.

POPULATION: Android varied screens/windows.

IMPLICATION: Reflow instead of shrinking text.

LIMITATION: Web staff also requires keyboard/browser review.

WHAT MINGO DOES: Scrollable learner, drawer staff at narrow/large text.

WHAT MINGO DOES NOT CLAIM: One layout fit is enough.

## R12

CLAIM: Accessibility requirements include contrast, resizing and operable controls.

SOURCE: [Original source](https://www.w3.org/TR/WCAG22/).

EVIDENCE TYPE: Normative web standard.

POPULATION: Web users with visual/motor/cognitive needs.

IMPLICATION: Normal text4.5:1, large3:1, resize200%; keyboard/focus;24CSS target criterion exceptions.

LIMITATION: WCAG24CSS minimum differs from Android48dp; automated tests cover only a subset.

WHAT MINGO DOES: Use stricter48dp and test contrast/scale.

WHAT MINGO DOES NOT CLAIM: Full conformance from widget tests.

## R13

CLAIM: Progressive disclosure exposes common tasks before rare detail.

SOURCE: [Original source](https://www.nngroup.com/articles/progressive-disclosure/).

EVIDENCE TYPE: Practitioner HCI guidance.

POPULATION: General application users.

IMPLICATION: Primary task visible; details have explicit labeled entry.

LIMITATION: Must verify grouping/findability with real users.

WHAT MINGO DOES: Home next lesson; evidence through row.

WHAT MINGO DOES NOT CLAIM: Every hidden feature remains discoverable without testing.

## R14

CLAIM: Contextual help can be preferable to a forced long tutorial.

SOURCE: [Original source](https://www.nngroup.com/articles/onboarding-tutorials/?lm=cloud-storage&pt=article).

EVIDENCE TYPE: Practitioner HCI guidance.

POPULATION: General software onboarding.

IMPLICATION: Skip onboarding and help at task.

LIMITATION: Target learner research still pending.

WHAT MINGO DOES: Optional goal/placement and in-context explanation.

WHAT MINGO DOES NOT CLAIM: Onboarding skip increases retention by a proven percentage.

## R15

CLAIM: Small iterative usability studies can find actionable problems.

SOURCE: [Original source](https://www.nngroup.com/articles/why-you-only-need-to-test-with-5-users/).

EVIDENCE TYPE: Practitioner model, not power analysis.

POPULATION: Qualitative usability sessions in reasonably similar groups.

IMPLICATION: Begin with about5, fix then retest.

LIMITATION: Not guarantee85% for Mingo; heterogeneous groups need additional sampling.

WHAT MINGO DOES: Think-aloud protocol with behavior notes.

WHAT MINGO DOES NOT CLAIM: Five people prove statistical success.

## R16

CLAIM: Retrieval can improve delayed retention relative to restudy.

SOURCE: [Original source](https://www.psychologicalscience.org/journals/psychological-science/j.1467-9280.2006.01693.x/).

EVIDENCE TYPE: Controlled experiments, Roediger/Karpicke2006.

POPULATION: Students learning prose;5min,2day,1week tests.

IMPLICATION: Include recall opportunities distinct from teaching.

LIMITATION: Immediate and delayed effects differ; not a Vietnamese mobile efficacy trial.

WHAT MINGO DOES: Separate Learn/Retrieve/Check semantics.

WHAT MINGO DOES NOT CLAIM: Every quiz automatically causes durable language mastery.

## R17

CLAIM: Spacing benefits depend on retention interval.

SOURCE: [Original source](https://pubmed.ncbi.nlm.nih.gov/16719566/).

EVIDENCE TYPE: Meta-analysis, Cepeda et al2006.

POPULATION: Verbal recall experiments; varied participants/tasks.

IMPLICATION: Review across time, preserve delay/context evidence.

LIMITATION: No universal optimal interval or session duration.

WHAT MINGO DOES: Explain due review; avoid invented skill score.

WHAT MINGO DOES NOT CLAIM: Five minutes is optimal for everyone.

## R18

CLAIM: L2 spacing findings vary by target and method.

SOURCE: [Original source](https://onlinelibrary.wiley.com/doi/10.1111/lang.12479).

EVIDENCE TYPE: Meta-analysis, Kim/Webb2022.

POPULATION: 48L2 experiments,N3411.

IMPLICATION: Plan delayed L2 evidence and pilot.

LIMITATION: Heterogeneity and different contexts prevent direct causal product claim.

WHAT MINGO DOES: Due-review rationale; delayed diary observation.

WHAT MINGO DOES NOT CLAIM: Universal vocabulary/grammar/pronunciation effect.

## R19

CLAIM: Feedback can support learning when tied to task information.

SOURCE: [Original source](https://journals.sagepub.com/doi/10.3102/0034654307313795).

EVIDENCE TYPE: Research review, Shute2008.

POPULATION: Varied educational/assessment settings.

IMPLICATION: Explain answer and next action without ego punishment.

LIMITATION: Timing/detail depend on learner/task; no single optimal recipe.

WHAT MINGO DOES: Specific calm explanation, bounded practice retry.

WHAT MINGO DOES NOT CLAIM: Immediate feedback is always superior.

## R20

CLAIM: Repeated testing can transfer to new inferential questions.

SOURCE: [Original source](https://pubmed.ncbi.nlm.nih.gov/20804289/).

EVIDENCE TYPE: Four experiments, Butler2010.

POPULATION: Adults learning prose facts/concepts, delayed1week test.

IMPLICATION: Use new contexts rather than duplicate question.

LIMITATION: Near/far inference tasks are not proof of fluent conversation.

WHAT MINGO DOES: Distinct Transfer context; future delayed evaluation.

WHAT MINGO DOES NOT CLAIM: OneMCQ measures real-world speaking transfer.

## R21

CLAIM: Problem-solving demands can consume capacity needed for schema acquisition.

SOURCE: [Original source](https://onlinelibrary.wiley.com/doi/10.1207/s15516709cog1202_4).

EVIDENCE TYPE: Model and experiments, Sweller1988.

POPULATION: Novice/expert problem-solving instructional tasks.

IMPLICATION: Avoid irrelevant interface decisions during learning.

LIMITATION: Cognitive theory is not direct app layout experiment.

WHAT MINGO DOES: One activity, brief instruction and no mascot motion in quiz.

WHAT MINGO DOES NOT CLAIM: Removing buttons proves reduced cognitive load.

## R22

CLAIM: Autonomy and competence-supportive contexts can support motivation.

SOURCE: [Original source](https://selfdeterminationtheory.org/SDT/documents/2000_RyanDeci_SDT.pdf).

EVIDENCE TYPE: Theory and research synthesis.

POPULATION: Multiple educational/social contexts.

IMPLICATION: Choice, non-controlling feedback and realistic competence cues.

LIMITATION: Cannot establish product retention gains without field data.

WHAT MINGO DOES: Goal choice, skip/defer, no punitive streak/XP pressure.

WHAT MINGO DOES NOT CLAIM: Capybara/streak predicts long-term motivation.

## R23

CLAIM: Microlearning duration and evidence are heterogeneous.

SOURCE: [Original source](https://www.sciencedirect.com/science/article/pii/S2405844024174440).

EVIDENCE TYPE: Systematic review.

POPULATION: Varied disciplines, content types and study designs.

IMPLICATION: Treat short session as testable product constraint.

LIMITATION: No agreed ideal length; engagement is not delayed retention.

WHAT MINGO DOES: Around5min metadata estimate and7–14day exploratory diary.

WHAT MINGO DOES NOT CLAIM: Universal scientifically optimal5min session.
