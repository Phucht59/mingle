# Legacy KLTN Research Context

The product originated from thesis work involving educational data mining / early risk prediction and recommendation concepts.

Shared history references work around:

- UCI dataset;
- OULAD dataset;
- static feature branch;
- aggregate feature branch;
- temporal sequence branch;
- neural sequence components such as CNN/BiLSTM in the research system;
- progress / early-prediction timing;
- recommendation logic;
- model evaluation discussions.

## Productization rule

This legacy pipeline is **research context, not a production architecture mandate**.

Do not preserve:

- original feature counts solely for compatibility;
- original model weights as production truth;
- dataset-specific assumptions that do not match product telemetry;
- thesis-specific preprocessing if it conflicts with real product semantics.

Production learning intelligence is redesigned around actual product data and the V3.2 domain/analytics contracts.
