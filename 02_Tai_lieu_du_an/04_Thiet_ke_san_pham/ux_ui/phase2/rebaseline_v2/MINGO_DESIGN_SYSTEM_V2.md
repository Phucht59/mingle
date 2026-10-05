# Mingo Design System V2 — Quiet Exploration

CURRENT technical presentation candidate; human approval PENDING. Owner chooses Apple design discipline with Mingo's own blue, capybara and exploration identity. Apple guidance is a design input for hierarchy and clarity; Android/Flutter behavior and accessibility remain the runtime baseline. Human aesthetic approval pending.

| Token | Value / use |
|---|---|
| primary / onPrimary | #2459D3 / white; one main action |
| ink | #172B4D; body/headings |
| muted | #52627A; secondary explanation |
| paper / surface | #FAF9F6 / white |
| mist / line | #EDF3FF / #D7DFEB; grouping/dividers, never sole status cue |
| success | #226645; correct/acknowledged with text/icon |
| error | #AD3434; local issue, recoverable explanation |
| warm accent | #AF4B0D; optional small warmth, never primary CTA |
| spacing | 4/8/12/16/24/32/40 logical pixels |
| corner | 16 controls, 18 primary buttons, 24 content surfaces |
| type | Inter variable OFL; Vietnamese supported; body 16/1.5, secondary 14/1.5, title 21, heading 26, display 32 |
| targets | >=48×48 logical pixels; primary minimum height56; wrapping text increases height |

One font family. Wordmark uses a restrained custom typographic treatment. No Apple fonts/assets or SF Symbols bundled. Material icons provide standard meanings. Inter's OFL and source hash are in ASSET_PROVENANCE.json and assets/fonts/OFL.txt. The primary font is loaded locally, no network dependency.

Learner viewport uses 24px horizontal padding, scrollable content, max width760. Hero is decoration on Home/Welcome, separate from text. One lesson activity and no bottom navigation in a lesson; primary action appears after the answer/explanation and remains reachable by scrolling at200%. Home contains greeting, hero, today's one lesson/action, then compact habit evidence. Learn uses topic/objective/time/difficulty; time is a content estimate. Course distinguishes current/completed/preview/locked with words. Profile contains preferences and offline entry. Result explains practiced evidence and one next step without mastery percentage or rewards.

Staff: task navigation, content max1100, sidebar240 at >=1000px with modest text scale; drawer at narrower widths or large text. Flow: work queue → learner/evidence/activity or draft → preview → source/license → review → publish confirmation → immutable read view → separate draft. Future analytics/interventions/admin remain labeled reference screens. No production authentication is simulated.

Components: Wordmark, ExplorationHero, Mascot, Surface, PageBody, ActionRow, Notice, StateNotice, ReviewLabel. Full-width actions wrap text; rows expand; no fixed text height, clipped ellipsis or gesture-only action. Native focus, button state, semantics heading, live notice and explicit icon tooltips. Dark mode adapts theme; do not assume all light palette tokens work on dark surfaces (see accessibility evidence).

Presentation law: one primary task/action, detailed information after an explicit row/action, visible recovery, no QA toolbar in the product viewport, no predictive risk badge on learners, no false promise of “saved to server”. Red/green never encode a state alone. Missing audio blocks listening checks. Empty/permission/revision/worker states explain a next safe action. Individual state render coverage is not a production service implementation.

Verification matrix and captures are in SCREEN_STATE_TRACEABILITY.csv and the final gate report. Golden generation creates a review baseline, repeat comparison checks deterministic regression; neither is human visual approval.

## Verified type/rendering adjustment

Body text is16px; secondary labels14px with sufficient weight. Interactive text buttons use16px/600 and the foreground surface color. Staff captions use14px/600. Initial thin14px labels failed rendered contrast checks and were fixed; see final six representative semantics/target/contrast tests. Local Inter is registered with the package font family so goldens and compiled apps render Vietnamese instead of the test fallback font. Asset capture explicitly waits for the mascot/hero decode before comparing.

At large text scales or320px width, the selected navigation label spans the full bar width, with four64dp icons retaining their accessible names. Normal-size navigation still displays all four labels. This prevents letter-by-letter wrapping while preserving scalable text and touch targets.

## Evidence-gated composition / 2026-10-02

Welcome/Home place hierarchy, opaque readable greeting, scenery and next lesson in one CompanionCard. TopicCard pairs topic art with clear task/meta; large text uses a vertical arrangement. Course uses static scenic islands and a decorative trail, with words for current/practiced/preview status; the trail is excluded from semantics. CompletionMoment groups the companion with a quiet reflection, without XP/percent mastery. EvidenceFact separates observations from interpretations. Staff retains task-oriented layout; only the direct-confirmation bypass is removed from its sample prerequisite guard.

One canonical world is reused; topic-specific poses remain pending rather than invented. Decorative images have bounded DPR decoding. Bright blue remains the primary action. Critical text is never over art; dark Home label uses onSurfaceVariant rather than the light-only muted token. See [CAPYBARA_ASSET_MANIFEST.md](CAPYBARA_ASSET_MANIFEST.md), [SCREEN_SCOPE_REGISTER.csv](SCREEN_SCOPE_REGISTER.csv) and [PHASE2_FINAL_GATE_REPORT.md](PHASE2_FINAL_GATE_REPORT.md). Technical golden approval is recorded before new golden generation. That record does not approve visual taste.
