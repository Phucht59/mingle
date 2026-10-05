# Learning Intelligence Guardrails

## Separation of concepts

- **Mastery**: estimate/state about what the learner knows or can do.
- **Risk**: estimate of an undesirable future learning outcome or disengagement/failure condition.
- **Recommendation**: decision about what action/content/intervention to present.

These must not be collapsed into one score.

## Production learning-intelligence sequencing

Do not freeze curriculum logic, mastery logic, adaptive paths, or final risk labels before Phase 9.

## Production ML

Historical UCI/OULAD models are research references only.

Production models must:

- be trained/evaluated on actual product data;
- use product-defined labels;
- be tested for temporal leakage;
- respect knowledge/availability time;
- have a non-ML fallback path;
- not become a mandatory dependency for core learning.
