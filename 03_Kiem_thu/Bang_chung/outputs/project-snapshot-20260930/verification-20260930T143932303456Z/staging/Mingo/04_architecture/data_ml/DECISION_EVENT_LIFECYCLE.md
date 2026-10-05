# Prediction → Decision → Exposure → Execution → Outcome

The product treats these as separate layers:

1. **Prediction** — a model or rule produces an estimate.
2. **Recommendation Decision** — the system selects an action using available evidence, policy, constraints, and optional risk/mastery inputs.
3. **Exposure** — the learner is actually shown/offered the recommendation.
4. **Execution** — the learner performs or accepts the action.
5. **Outcome** — downstream learning/behavioral result is observed.

This separation is important for causal analysis, debugging, policy evaluation, and preventing the model output from being mistaken for an intervention outcome.
