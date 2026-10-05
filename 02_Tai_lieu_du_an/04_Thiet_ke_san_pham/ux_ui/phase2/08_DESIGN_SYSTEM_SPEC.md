# Design System Specification — Mingo UX Reference Theme v0.1

This is an implementation-ready UX theme, **not a permanent brand lock**. Semantic token names should remain stable even if brand colors evolve.

## Product feel

Friendly, calm, lightweight, supportive and clear. Learning integrity beats decoration. Avoid casino-like reward effects, childish visual noise, clinical diagnosis dashboards and “AI magic” framing.

## Foundations

- Canvas `#F6F8FC`; surface white; primary text `#0F172A`; muted text `#475569`.
- Primary `#3046C5`; accent `#0F766E`; semantic success/warning/danger/info tokens in `DESIGN_TOKENS.json`.
- System font stack; 16px body; concise titles; maximum learner content width 560px.
- Base spacing 4px; common spacing 8/12/16/24/32; radius 8/12/16/24.
- Learner tap targets target at least 48dp. Staff controls maintain clear keyboard focus.
- Motion is subtle 120–240ms; reduced-motion disables non-essential transform/scroll animation.

## Component rules

- Primary button: one dominant action where possible; loading prevents duplicate submit.
- Answer option: selection != submit; correctness uses text/icon + color, not color alone.
- Feedback: explanation first; retry state explicit; no “mastered” from one answer.
- Recommendation card: show one factual reason and optional details; never “because you are losing motivation.”
- Evidence card: “Building”, “Needs more evidence”, observed examples; no unsupported percentage.
- Sync banner: quiet persistent status; “Saved on this device” differs from “Synced.”
- Content status: Draft / In review / Approved / Published / Retired / Revoked are visually distinct; published action is create-new-draft, not edit.

## Icons and imagery

Use simple line/filled functional icons with text labels on critical actions. Decorative illustration is optional and must not carry essential meaning. Do not introduce a mascot/brand character as a Phase 2 dependency.

## Source of implementation values

`DESIGN_TOKENS.json` is the canonical machine-readable reference for this Phase 2 candidate.


## Rework R1 semantic focus token

All prototype/implementation focus indicators consume the semantic `color.focus` token (`--focus` in the HTML reference). Hard-coded alternate focus colors are not allowed unless a separately named/validated semantic token is introduced.
