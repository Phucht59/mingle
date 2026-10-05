# Product Information Architecture

## Learner — Android-first

Top-level navigation is deliberately limited to **Home | Learn | Course | Profile**.

- **Home — What should I do now?** Next action, factual reason, approximate duration, target/streak kept lightweight, and sync/offline status when relevant.
- **Learn — Start or resume learning.** Finite learning cycle; never an infinite feed.
- **Course — Where am I in the broader learning structure?** Open/current/due/locked objectives and preview-only locked content.
- **Profile — What has the system observed and what can I configure?** Goal, qualitative evidence, preferences, accessibility/offline settings and later account actions.

Onboarding sits outside the main shell: Welcome → optional Goal → optional Placement → provisional result/state → Home.

Learning flow is a focused sub-flow where bottom navigation may be visually suppressed to reduce accidental exits: Cycle Intro → Review → Learn → Retrieve → Transfer → Check → Summary. Explicit exit/resume behavior is specified rather than pretending the cycle is a feed.

Not top-level: AI, Risk, Mastery, Rewards, Streak, Review, Offline, Settings. They are capabilities, evidence or states—not product destinations.

## Staff/Admin — desktop Web

Sidebar: **Dashboard | Learners | Content | Interventions | Analytics | Administration**.

- Publishing is part of **Content** lifecycle, not a separate product domain.
- Interventions and Analytics are future-ready shells; their business logic belongs to later phases.
- Navigation visibility is convenience only. Backend authorization remains mandatory in Phase 3+.

## Cross-surface rule

Deep links must re-check access/eligibility and must not bypass prerequisite, permission, revision or canonical state. Back navigation must never resubmit a command or duplicate progress.
