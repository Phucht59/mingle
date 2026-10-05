# Implementation Issue / Change Request Policy

## When to open a change request

Open one when implementation reveals a concrete issue that cannot be resolved while preserving V3.2 semantics.

Typical triggers:

- contradictory invariants;
- impossible transaction boundary;
- security model gap;
- offline replay ambiguity;
- version-pinning ambiguity;
- data-integrity constraint that cannot be expressed or enforced;
- runtime behavior that makes a frozen rule unsafe or unimplementable.

## What is not a valid reason

- developer preference;
- desire to use a trendier technology;
- optimizing hypothetical scale;
- convenience that changes user-visible behavior;
- changing old rules merely to match the original thesis model or feature count.

## Required evidence

Every CR should capture reproduction evidence, scope, compatibility impact, migration needs, and new or changed tests.
