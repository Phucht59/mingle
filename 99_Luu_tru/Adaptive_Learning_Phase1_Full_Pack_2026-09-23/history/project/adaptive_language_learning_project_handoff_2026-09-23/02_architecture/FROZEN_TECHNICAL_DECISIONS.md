# Frozen Technical Decisions

1. Flutter is Android-first for the learner app.
2. Flutter Web is used for staff/admin.
3. iOS compatibility is retained, but public release comes later.
4. FastAPI/Python is the backend stack.
5. PostgreSQL is the primary database.
6. Object storage is used for media/binary artifacts.
7. System architecture is a modular monolith.
8. API and durable worker are separate processes from one codebase.
9. Server is authoritative for scoring, progress, and permissions.
10. Command ingestion and telemetry ingestion are separated.
11. Offline clients have durable command and telemetry queues.
12. Published content is immutable/versioned.
13. Enrollment and attempts pin exact content revisions.
14. Analytics separates event time from knowledge/availability time and preserves source capture.
15. Mastery and risk are separate concepts.
16. Risk may influence recommendation, but recommendation cannot be reduced to risk prediction.
17. UCI/OULAD are research baselines only; their historical modeling choices are not production defaults.
18. Prediction, recommendation decision, exposure, execution, and outcome are separate lifecycle layers.
19. Product functionality must not depend on ML/recommendation being enabled.
20. Premature distributed architecture is explicitly avoided without evidence.
