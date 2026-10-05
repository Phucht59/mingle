# The 18 Decisions to Resolve Scientifically

The agent should NOT merely ask the user to choose these. For each, research the evidence and recommend the strongest default policy for the MVP.

1. Error interpretation
When a learner answers incorrectly, how deeply should the system attempt to distinguish the cause?
Examples: vocabulary knowledge gap, grammar confusion, listening/perception failure, careless mistake.
Should the MVP infer causes or mainly log observable evidence across repeated attempts?

2. Response time
Should response latency affect learner-state interpretation?
Example: correct in 2 seconds vs correct after 25 seconds.
How should latency be used without equating speed with intelligence or proficiency?

3. Hints
Should hints be available?
Which hint types are appropriate for vocabulary, grammar and listening?
Should a correct answer after hints count as weaker evidence than an unaided correct response?

4. Retry policy
If the learner answers incorrectly, should immediate retry be allowed?
How should first-attempt evidence be preserved versus eventual-correct evidence?

5. Skip policy
Should skipping influence the scheduler?
How should one skip versus repeated skips be interpreted?
How should the design avoid treating skip as mastery?

6. Listening replay
Should audio replay be unlimited during learning?
Should CHECK/assessment items limit replay?
How should replay count be interpreted?

7. Vocabulary representation
Should vocabulary learning be centered on isolated word ↔ translation flashcards or on meaning + pronunciation + contextual sentence + varied retrieval?
What is the best default for beginners?

8. Grammar teaching sequence
Should grammar be taught rule-first, pattern/context-first, attempt-first, or a hybrid?
What is best for weak-foundation learners?

9. Difficulty progression
When the learner performs well, should difficulty increase within the same objective?
Example progression: recognition → recall → listening → contextual application.
Or should difficulty only change at lesson boundaries?

10. User focus vs system need
If the learner chooses "Listening focus" but the system detects overdue review / prerequisite gaps, how much control should the learner have versus the scheduler?

11. Placement test scope
Should initial placement test Vocabulary + Grammar + Listening together?
Should it be short/adaptive?
Should listening be calibrated progressively after onboarding?
How should the product avoid a long 30–40 minute onboarding?

12. User-facing learner model
Should learners see the system's interpretation of their state?
Examples: "Grammar needs review", "Listening improving", "You often confuse do/does".
Should the product avoid false precision such as "Mastery = 71%" before the model is validated?

13. Learning goals
Should onboarding ask why the learner is learning?
Examples: rebuild foundation, work, TOEIC, daily learning.
How strongly should goals influence sequencing versus curriculum prerequisites?

14. Daily target
Should the default daily target be one ~5-minute cycle?
Should users be able to choose 5/10/15+ minutes while the internal feed remains composed in ~5-minute cycles?

15. Streak rule
What should preserve a streak?
Opening the app?
One review?
One completed meaningful cycle?
How can streak support consistency without degrading into empty engagement?

16. Reward design
What reward mechanics are appropriate for this MVP?
XP, badges, milestones, unlockable visuals/themes, progress feedback, or a combination?
Which mechanics risk undermining intrinsic motivation or gaming the system?

17. Learner control over course map
Should users be able to browse and manually choose lessons outside recommendations?
Should prerequisites be hard-locked, soft-locked, or warning-based?
How should agency and curricular validity be balanced?

18. Recommendation explanations
Should the system explain why it selected review/remedial content?
Examples: "Due for review", "You struggled with this yesterday".
What level of explanation is useful without overwhelming the learner?
