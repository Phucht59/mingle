# MASTER MEMORY TRANSFER

## Trần Hoàng Phúc

### Cross-Account Context Migration Pack

### Snapshot: 23 September 2026

---

# 0. INSTRUCTION FOR THE NEW CHATGPT ACCOUNT

This document contains persistent context transferred from another ChatGPT account.

Use it as background context when assisting this user.

Priority order:

1. Current explicit user instruction.
2. Latest dated decision in this document.
3. Latest project state.
4. Earlier project decisions.
5. General preferences.

If an old decision conflicts with a newer decision, use the newer one.

Do not force the user to repeat information already contained here.

Do not silently redesign systems that have already been approved.

When a project has an explicit source of truth, preserve it unless the user explicitly authorizes a change.

When there are conflicting historical figures in this document, do not guess. Use the project source files or latest implementation artifact to resolve them.

---

# 1. USER PROFILE

Name:

**Trần Hoàng Phúc / Tran Hoang Phuc**

Primary language in conversation:

**Vietnamese**

English is frequently used for:

- technical terminology;
- portfolio copy;
- code;
- CV;
- product documentation;
- interview preparation.

Academic background:

**Data Science**

University context:

**HUFLIT — Trường Đại học Ngoại ngữ – Tin học TP.HCM**

Current general direction:

- transition from university into employment;
- Data Analyst is primary technical career direction;
- Data Engineer is a secondary/upskilling direction;
- Data Science / machine learning remains relevant because of the graduation thesis.

The user has also worked in F&B and has considered operational/QC jobs while transitioning into the data field.

---

# 2. COMMUNICATION PREFERENCES

The user prefers answers that are:

- direct;
- concise;
- actionable;
- not padded with generic explanations.

Default behavior:

**Answer the actual question first.**

If more detail is necessary for a technical decision, then explain.

The user will normally ask follow-up questions if more detail is needed.

Do not repeatedly summarize things the user already knows.

The user often speaks informally using:

- tao;
- mày;
- má;
- etc.

It is acceptable to mirror this informal register when appropriate.

Do not become excessively formal unless:

- writing emails;
- CVs;
- professional documents;
- academic materials;
- interview answers.

---

# 3. HOW THE USER EXPECTS AN AI AGENT TO WORK

The user does not want endless trial-and-error without diagnosis.

Preferred workflow:

1. Inspect current state.
2. Identify the actual root cause.
3. Separate technical failure from visual/product failure.
4. Propose a method.
5. Define deliverables.
6. Define acceptance criteria.
7. Implement.
8. Produce evidence.
9. PASS or FAIL the gate.
10. If FAIL, return to root cause rather than polishing the wrong solution.

The user especially dislikes:

- endlessly patching a fundamentally incorrect approach;
- claiming progress because code runs when the actual output is poor;
- forcing the user to run many packages that the AI already suspects will fail;
- pretending a limitation does not exist;
- asking the same questions repeatedly;
- restarting project discovery from zero.

If a proposed approach has been explicitly rejected, do not quietly revive it.

---

# 4. USER'S PROJECT QUALITY PHILOSOPHY

The user generally values:

- actual product quality over demo completeness;
- coherent visual/system design over adding features;
- realistic engineering constraints;
- reproducibility;
- evidence-based decisions;
- clear phase gates.

For visual projects:

**static quality must be correct before animation polish.**

For data/ML projects:

**data leakage prevention and realistic evaluation matter more than impressive metrics.**

For product design:

**learning/product mechanics must solve an actual problem, not exist because they are fashionable.**

---

# 5. EDUCATION / CURRENT LEARNING

User is/was studying Data Science at HUFLIT.

Graduation thesis has been completed academically.

Around late August 2026, the user's priorities shifted toward:

- CV;
- portfolio;
- job/internship applications;
- Google Data Analytics learning;
- English;
- practical data projects.

---

# 6. GOOGLE DATA ANALYTICS

The user is taking:

**Google Data Analytics Professional Certificate — Coursera**

Known progress around 1 September 2026:

- Course 2;
- around mid Module 1.

Topics discussed included:

- SMART questions;
- Ask phase;
- learning efficiently;
- microlearning;
- applying the course rather than merely completing videos.

The user is interested in learning English in parallel with data skills.

---

# 7. CAREER DIRECTION

Primary target:

**Data Analyst**

Secondary longer-term direction:

**Data Engineer**

Relevant Data Science / ML skills should remain visible but should not make the user's positioning unclear.

Preferred positioning:

Data Analyst first, with the ability to grow into Data Engineering / Data Science.

The user does not want the portfolio to consist only of:

- simple notebooks;
- generic Kaggle analysis;
- shallow case studies.

Preferred projects:

- end-to-end;
- realistic;
- business-driven;
- technically defensible;
- capable of being discussed in interviews.

---

# 8. DATA PORTFOLIO PROJECT DIRECTION

An earlier proposed core portfolio project was:

**Digital Product Growth & Monetization Analytics Platform**

Possible methodology:

Ask → Prepare → Process → Analyze → Share → Act

Potential stack discussed:

- SQL;
- PostgreSQL;
- Power BI;
- dbt;
- Python;
- ETL;
- data quality;
- later Airflow;
- Docker.

The user prefers building a realistic data platform instead of just a dashboard.

Possible DA → DE bridge project direction:

**E-commerce Analytics Data Platform**

Potential components:

- ingestion;
- database;
- ETL;
- data cleaning;
- dimensional/analytics modeling;
- dbt;
- orchestration;
- BI;
- Docker;
- data quality checks.

Important historical decision:

For an initial analytics MVP, avoid unnecessarily adding:

- machine learning;
- React/FastAPI product UI;
- forecasting;
- recommendation systems

unless they actually solve the selected business problem.

---

# 9. CV STRATEGY — DATA

Preferred:

- one page when possible;
- ATS-friendly;
- clear Data Analyst positioning.

KLTN should be one of the strongest technical items.

Useful thesis talking points:

- UCI + OULAD;
- early warning;
- temporal data;
- hybrid architecture;
- leakage prevention;
- recommendation/intervention;
- realistic train/validation methodology.

Older software skills such as:

- C#;
- Java;
- React;
- Vite;
- ASP.NET MVC

may remain but should be subordinate to data skills.

Avoid making the user appear primarily:

- QC;
- Data Annotation;
- generic software engineer

when applying for Data Analyst positions.

---

# 10. GRADUATION THESIS — IDENTITY

Vietnamese thesis title:

**“Xây dựng mô hình học kết hợp để dự đoán thành tích học tập sinh viên”**

Core problem:

Use a hybrid machine-learning architecture to predict student academic risk early enough to support intervention.

The project includes two major functions:

1. Early student-risk prediction.
2. Support/recommendation for intervention.

---

# 11. THESIS DATASETS — UCI

Dataset:

**UCI Student Performance**

Two source datasets:

### Mathematics

Approximately:

**395 records**

### Portuguese

Approximately:

**649 records**

Combined records:

**1,044**

Historical thesis notes indicate approximately:

**662 student groups**

after identifying/merging students.

Original dataset attributes:

approximately **33 variables** per dataset.

---

# 12. UCI LABEL

Final grade:

**G3**

is used to construct the prediction target.

G3 must then be removed from model inputs.

Known risk rule used in thesis context:

**Risk if G3 < 10**

Otherwise:

**Non-risk**

Critical rule:

G3 is ground truth only.

**Never include G3 in X/features.**

---

# 13. UCI EARLY PREDICTION

Information becomes available incrementally.

A simplified explanation used during defense preparation:

### S0

Context/background data only.

No G1/G2.

### S1

Context + **G1**

### S2

Context + **G1 + G2**

A temporal interface used for UCI:

`[B, 2, 1]`

where the two temporal positions represent:

- G1
- G2

At an early stage where grades are unavailable:

- mask indicates unavailable values;
- sequence length may be zero.

Example:

`mask = [0,0]`

`len = 0`

The architecture should handle feature availability rather than pretending future grades already exist.

---

# 14. THESIS OBSERVATION CUTPOINTS

Another representation used in thesis experiments includes observation cutpoints:

- 20%
- 35%
- 50%
- 75%
- 100%

Progress values must be represented numerically as fractions when passed into the model.

Example:

20% → **0.20**

35% → **0.35**

Do not write 20 where the model contract expects 0.20.

---

# 15. THESIS DATASETS — OULAD

Dataset:

**Open University Learning Analytics Dataset — OULAD**

Important tables:

1. studentInfo
2. studentAssessment
3. studentRegistration
4. studentVLE
5. assessments
6. courses
7. vle

Dataset characteristics:

- tens of thousands of registrations;
- approximately 28,785 unique students;
- more than 10 million VLE interaction events.

Historical notes contain two registration counts:

- approximately **32,539**
- approximately **32,593**

Do not silently choose one for formal reporting.

Use the actual thesis/database source query when an exact number is required.

Unique student count consistently referenced:

approximately **28,785**.

---

# 16. OULAD TARGET

Target derived from:

`final_result`

Mapping:

### Non-risk

- Distinction
- Pass

### Risk

- Fail
- Withdrawn

`final_result` must be used to create y and then excluded from prediction features.

---

# 17. OULAD EARLY PREDICTION

Only information available up to the observation cutoff may be used.

Example previously discussed:

Course/module presentation length:

approximately **241 days**

35% cutoff:

approximately first **84 days**

Events after the cutoff cannot influence features at that cutoff.

This is a fundamental thesis requirement.

---

# 18. WITHDRAWAL HANDLING

The thesis includes explicit logic around withdrawals and cutoffs.

Records/events must be handled carefully so the model does not learn future withdrawal information.

Historical implementation notes mention excluding cases where withdrawal had already occurred relative to an observation cutoff when required by the experiment design.

When implementing or defending the exact rule, use the thesis source code/specification rather than reconstructing it from memory.

---

# 19. LEAKAGE PREVENTION — NON-NEGOTIABLE

Both datasets must avoid:

### Label leakage

Example:

- G3;
- final_result.

### Temporal leakage

Future activity must not appear in an earlier cutoff.

### Identity leakage

The same learner should not leak across train/validation/test groups in a way that makes performance unrealistic.

Split should therefore be learner/group-aware.

---

# 20. PREPROCESSING

Transformations must be fit only on training data.

Numeric:

- median imputation.

Categorical:

- one-hot encoding.

Validation/test:

- transform using parameters learned on training;
- never independently fit transformations.

This rule is important during thesis defense.

---

# 21. THESIS MODEL INPUTS

Hybrid model receives multiple feature families.

## Static branch

Historical UCI input:

`[B, 57]`

OULAD static dimension appears in historical notes as both:

- 47
- 49

The later defense material frequently referenced:

`[B, 49]`

Therefore:

**Do not treat 47 vs 49 as resolved from memory.**

Use the final preprocessing artifact/model configuration if exact implementation dimensions are required.

## Temporal branch

UCI:

`[B, 2, 1]`

OULAD:

`[B, T, 11]`

## Aggregate branch

UCI:

`[B, 5]`

OULAD:

`[B, 13]`

Additional control signals include:

- mask;
- sequence lengths;
- feature availability;
- progress/cutoff.

---

# 22. HYBRID MODEL ARCHITECTURE

Core architecture:

three parallel representations.

### Tabular / Static branch

Learns background/contextual information.

### CNN branch

1D CNN is used to capture local patterns in temporal data.

### BiLSTM branch

Captures sequential/temporal evolution.

Each branch is projected/adapted toward a common latent size.

Historical defense architecture used:

approximately **128-dimensional branch embeddings**.

---

# 23. GATED FUSION

A gating mechanism learns the contribution of each branch.

Historical implementation:

- gate receives concatenated branch/control information;
- softmax produces three weights;
- branch representations are combined as a weighted fusion.

Fusion representation remains approximately:

**128 dimensions**

rather than concatenating everything indefinitely.

The key conceptual point:

The system can dynamically adjust reliance on branches depending on available information and learning stage.

---

# 24. MODEL OUTPUT

Main output:

student risk probability.

Conceptually:

`P(risk)`

then compared against a threshold.

Threshold should not be selected using the final reporting set.

---

# 25. FIT / STOP / VALID

The thesis used a three-way conceptual split terminology:

### FIT

Used to learn model parameters.

### STOP

Used for:

- model selection;
- early stopping/checkpoint;
- threshold selection.

### VALID

Used for final reporting/evaluation.

The important methodological idea:

**Do not optimize threshold or model decisions on the final reporting set.**

---

# 26. TRAINING DETAILS

Historical thesis notes include:

Optimizer:

**AdamW**

Loss:

**BCEWithLogitsLoss**

with class imbalance handling such as:

`pos_weight`

Experiment repeat design:

**3 splits × 3 seeds = 9 runs**

Known seeds used in defense notes:

- 42
- 1201
- 2026

Results should therefore be summarized using:

**mean ± standard deviation**

where applicable.

---

# 27. EVALUATION

Because risk classes may be imbalanced, a major metric was:

**Average Precision / AP**

rather than relying only on accuracy.

Historical baselines included models such as:

- Logistic Regression
- Decision Tree
- Random Forest
- SVM
- MLP
- XGBoost

Ablation experiments are also relevant to demonstrate the contribution of architecture/components.

---

# 28. THESIS RECOMMENDATION MODULE

The project also contains an intervention/recommendation component.

OULAD is the more relevant dataset for behavioral intervention because it contains VLE activity.

Historical recommendation context:

- approximately 17 interpretable VLE-related features;
- multiple recommendation/action models.

A previous thesis specification used:

**five independent EBM rankers**

and ranking quality such as:

**NDCG\@3**

Important scientific limitation:

Weak/synthetic/observational recommendation labels do **not** prove that an intervention causally improves student outcomes.

Do not claim causal effectiveness if the thesis did not run a controlled intervention experiment.

---

# 29. THESIS PARAMETER COUNTS

Historical architecture notes referenced model sizes around:

OULAD:

**\~482,116 trainable parameters**

UCI:

**\~480,836 trainable parameters**

These should be verified from the final model if exact reporting is necessary.

---

# 30. THESIS COMPUTE CONSTRAINT

Architecture/training was designed to be practical on modest hardware.

A reference environment included a GPU around:

**RTX 2060 6 GB**

This influenced model scale and batching decisions.

---

# 31. THESIS DEFENSE PREPARATION

A large amount of prior work involved preparing explanations for defense slides.

Recurring concepts the user needed to explain clearly:

- what each input branch receives;
- why UCI temporal shape is `[B,2,1]`;
- why OULAD temporal input is `[B,T,11]`;
- static vs temporal vs aggregate;
- why early prediction matters;
- S0/S1/S2;
- information availability;
- progress;
- mask;
- lengths;
- gating;
- FIT/STOP/VALID;
- recommendation flow;
- data leakage.

The user prefers explanations that can be spoken naturally rather than purely mathematical explanations.

---

# 32. KLTN DOCUMENT FORMATTING — SOURCE

HUFLIT formatting work used an official/reference template such as:

**04-MẪU-HÌNH-THỨC-KLTN-T9-2024.docx**

A separate student's thesis was also used as a visual reference for pagination/header/TOC behavior.

Do not treat that other student's content as the user's thesis.

---

# 33. KLTN BODY FORMATTING

Body text target:

**Times New Roman**

Size:

**13 pt**

Line spacing:

**1.5**

This also applies to normal text inside tables when requested.

Chapter titles and subsection titles may use their own required formatting.

---

# 34. KLTN PAGE NUMBERING

Final desired logic:

Acknowledgement / commitment pages:

**no Roman numeral shown**

Roman numbering begins from:

**Table of Contents**

Main content begins at:

**Chapter 1**

and resets/starts Arabic numbering at:

**1**

Then continues:

2, 3, 4, ...

---

# 35. KLTN HEADERS

Header begins with main content / Chapter 1.

Every page in a chapter should display that chapter's correct title.

Example:

Pages belonging to Chapter 1 → Chapter 1 header.

Pages belonging to Chapter 2 → Chapter 2 header.

It is not enough to put a header only on the chapter-opening page.

The user also requested that the header look cleaner/more professional rather than being visually crude.

---

# 36. KLTN TABLE OF CONTENTS

TOC requirements:

- update page references;
- page numbers aligned consistently;
- dot leaders aligned;
- no page numbers shifted left/right randomly;
- hierarchy should visually match the reference.

The user specifically complained when page numbers in the TOC were not vertically aligned.

---

# 37. KLTN COVER PAGES

Two cover/title pages were checked against the official HUFLIT template.

At one point a corrected version targeted title/font sizes such as:

- 14;
- 18;
- 24

depending on the field/title hierarchy.

Important principle:

When the user asks to change only cover pages or only tables, do not reformat unrelated parts of the thesis.

The user strongly dislikes unnecessary changes outside the requested scope.

---

# 38. KLTN STATUS

By around mid-September 2026:

KLTN content was essentially finished.

Later work focused on formatting:

- cover pages;
- page numbers;
- headers;
- TOC;
- font consistency.

The project is no longer the main active development priority.

---

# 39. ADAPTIVE LANGUAGE LEARNING PROJECT — OVERVIEW

After the thesis/system work, the user began developing a separate language-learning product.

This is intended as a real product/startup-style project rather than another academic paper.

Working concept:

An adaptive English learning system that understands the learner and decides what they should learn/review next.

---

# 40. ADAPTIVE PROJECT — SOURCE OF TRUTH

As of **15 September 2026**:

**V3.2 is the official baseline / source of truth.**

Architecture review status:

- approximately 9/10;
- **115 contract checks passed**;
- **22 SQL checks passed**.

Important:

V3.2 is primarily:

- specification;
- data contracts;
- architecture;
- verification logic.

It is **not** a fully implemented application.

---

# 41. ADAPTIVE PROJECT — PHASE STATUS

### Phase 0

Architecture & Contract Baseline

**DONE**

### Phase 1

Implementation Foundation / Product Build Kickoff

**ACTIVE**

Phase 1 was explicitly not considered complete as of around 17 September 2026.

---

# 42. ADAPTIVE PROJECT — CHANGE MANAGEMENT

Do not casually modify V3.2 business rules.

Architecture/spec changes should be deliberate.

Conceptually:

V3.2 remains frozen unless a new requirement triggers a formal change/decision.

Do not restart architecture analysis from scratch unless there is new evidence.

---

# 43. ADAPTIVE TECH STACK

Frozen/accepted stack:

### Client

**Flutter**

Priority:

**Android-first**

### Backend

**FastAPI**

### Database

**PostgreSQL**

Additional infrastructure may include:

**object storage**

where content/media requires it.

---

# 44. ADAPTIVE TARGET USERS

Initial users include:

- English beginners;
- people who lost their English foundation;
- people who study but feel ineffective;
- learners needing systematic vocabulary review;
- learners who do not know what they should study next.

---

# 45. ADAPTIVE PROBLEM HYPOTHESIS

User problem:

Learners often:

- study inconsistently;
- consume random content;
- forget vocabulary;
- do not know their real level;
- do not know what to review;
- do not know the correct learning sequence;
- lose motivation because progress is unclear.

The system should:

- observe behavior;
- maintain learner state;
- choose appropriate material;
- schedule review;
- adapt difficulty;
- recommend next actions.

---

# 46. PRODUCT POSITIONING

The goal is not to merge every feature from:

- Duolingo;
- Quizlet;
- Coursera;
- Anki;
- generic AI chatbots.

The goal is to find a focused gap and solve it well.

Initial approach:

small cohort → validate → beta → expand.

---

# 47. COMMERCIALIZATION

Initial product:

**free-first**

Potential future model:

- Free;
- Premium.

Monetization is not the first MVP priority.

---

# 48. PILOT

Initial pilot size:

approximately **5 users**

Reason:

limited development/testing resources.

The product should therefore prioritize depth of feedback over artificial scale.

---

# 49. LEARNING SCOPE — MVP

MVP learning areas:

1. Vocabulary
2. Grammar
3. Listening

Not initial MVP priorities:

- Speaking;
- unrestricted AI conversation;
- broad language social features.

---

# 50. LEVEL SYSTEM

Internal learning progression:

- A0
- A1
- A2
- B1
- B2

External goals such as:

- TOEIC

should map onto the learner profile/goals but should not replace the internal competency progression.

---

# 51. PLACEMENT

Initial learner level should be estimated from:

- diagnostic test;
- learner background;
- stated goals.

The system may allow:

- re-placement;
- manual level override.

However:

manual override should have constraints.

The learner should not be able to arbitrarily break progression without consequences or guidance.

---

# 52. CORE EXPERIENCE — ADAPTIVE LEARNING FEED

Core interaction concept:

**Adaptive Learning Feed**

Default session length:

approximately **5 minutes**

This is not intended to mimic endless TikTok consumption.

It is a finite, objective-driven learning cycle.

---

# 53. FIVE FUNCTIONAL ROLES

Accepted cycle:

### 1. Review

Recall previously learned knowledge.

### 2. Learn

Introduce a small amount of new material.

### 3. Retrieve

Require active recall / attempt.

### 4. Transfer

Use knowledge in a different context.

### 5. Check

Assess whether the learner can actually perform the objective.

These are functional roles.

Not every screen needs to visually announce the role.

---

# 54. FINITE SESSION RULE

The learning feed must have:

- a defined session;
- explicit objective;
- clear endpoint.

**No infinite scrolling.**

After completion:

the user may explicitly choose to continue.

Continuation is not the same as an endless feed.

---

# 55. SESSION COMPLETION

Session completion can use a hybrid concept of:

- approximate time target;
- objective completion.

The five-minute target is a default consumption unit, not a hard rule that overrides pedagogical completion.

---

# 56. SKIPPING

Skipping is allowed only as an explicit learner action.

Skip must be logged.

A skip is behavioral evidence.

A skip must **not** automatically mean:

- learned;
- mastered;
- understood.

Avoid unlimited frictionless skipping that lets the learner bypass the learning objective.

---

# 57. ATTEMPT-FIRST DESIGN

When appropriate:

show the learner a task/problem before explaining everything.

Then provide:

- feedback;
- micro-explanation;
- correction.

Benefits:

- retrieval;
- diagnostic evidence;
- reduced passive consumption.

However:

for genuinely new knowledge, a small explanation may be necessary before the first attempt.

Do not apply attempt-first dogmatically.

---

# 58. MODERN CONTENT CONSUMPTION PRINCIPLE

Modern content mechanics may be used for:

- fast start;
- short interactions;
- varied modality;
- immediate feedback;
- smooth continuation;
- relevance.

They must **not** determine pedagogy.

The learning engine should remain controlled by:

- curriculum;
- prerequisites;
- retrieval practice;
- spacing;
- feedback;
- difficulty progression;
- transfer;
- delayed reassessment.

---

# 59. VOCABULARY MODULE

Core approach:

**Spaced Repetition System — SRS**

Should include:

- active recall;
- review scheduling;
- contextual use;
- learner evidence.

Vocabulary mastery cannot be based solely on having seen a word.

---

# 60. GRAMMAR MODULE

Should combine:

- concise rule explanation;
- retrieval;
- application;
- contextual usage.

Avoid a design where grammar consists mainly of reading long theory.

---

# 61. LISTENING MODULE

Preferred:

- short clips;
- learner attempt;
- comprehension task;
- immediate feedback;
- replay/re-exposure when appropriate.

---

# 62. ENGAGEMENT

Potential mechanics:

- streaks;
- targets;
- rewards.

But:

**learning quality has priority over gamification.**

Gamification exists to support consistent behavior, not to replace learning.

---

# 63. CONTENT STRATEGY

Initial content should come from:

- OER;
- open-license materials;
- appropriately licensed sources.

Critical rule:

**publicly accessible does not mean legally reusable.**

Track:

- source;
- license;
- provenance;
- content version.

---

# 64. CONTENT VERSIONING

Attempts must be traceable to the exact content version used.

This matters because:

- exercises change;
- scoring logic changes;
- explanations change.

Historical learner evidence must remain interpretable.

---

# 65. SCORING / PROGRESS

Backend must consistently store:

- submission;
- attempt;
- score;
- progress;
- learner events.

Authoritative fields should be server-validated.

Do not trust the client to define its own final progress or score.

---

# 66. OFFLINE SUPPORT

Client architecture includes:

- local event queue;
- retries;
- delayed synchronization.

Retries must be:

**idempotent**

and must not:

- duplicate rewards;
- duplicate progress;
- regress learner state.

---

# 67. MULTI-DEVICE CONSISTENCY

The system should support consistent state when learners use more than one device.

Conflicts require deterministic resolution.

Do not assume event arrival order equals real learner action order.

---

# 68. LATE EVENTS

Late/offline events must preserve enough timestamps/context to reconstruct learner state at a past decision point.

This is especially important if ML later predicts risk or knowledge state.

Future events must not leak backward into an earlier prediction.

---

# 69. RECOMMENDATION FALLBACK

Recommendation must not completely fail when the ML model is unavailable.

There must be a deterministic/rule-based fallback.

States such as:

- model available;
- model unavailable;
- uncertainty

should be explicitly represented rather than silently substituting nonsense values.

---

# 70. PRODUCT PROMISE DIRECTION

A recurring positioning idea:

The app behaves like a learning companion that:

- studies with the learner;
- understands them;
- knows what they should review next;
- adjusts the path.

The exact marketing sentence is not permanently locked.

---

# 71. PRODUCT NAME STATUS

Several names have been explored.

Examples:

- BONGO
- Mingo
- MING
- PALS

BONGO was considered memorable phonetically but had concerns about existing usage/brand conflict.

Mingo/MING was explored as short and easy to pronounce.

PALS was liked because it feels friendly and expandable.

**No final product name is currently considered permanently locked.**

Do not assume any one candidate is final without a newer explicit decision.

---

# 72. PHUC SPATIAL PORTFOLIO — PURPOSE

Current major design project:

**PHUC Spatial Portfolio**

Owner:

**Tran Hoang Phuc**

Purpose:

a recruiter-facing Data Science/Data Analyst portfolio with a strong spatial 3D identity.

It is not intended to look like:

- a generic developer template;
- a technical documentation site;
- a toy WebGL demo;
- an online CV with a random 3D background.

---

# 73. PORTFOLIO CORE VISUAL SYSTEM — LATEST

Latest accepted identity:

### Textile

Ivory / off-white linen cloth.

### Architecture

Warm concrete / lime plaster / mineral architecture.

### Lighting

Natural architectural lighting.

### Typography

Editorial HTML typography.

### Spatial behavior

Continuous spatial transitions.

The cloth is the primary visual actor.

Architecture is the stage.

HTML/UI carries information.

---

# 74. PORTFOLIO AESTHETIC

Desired feel:

- minimal;
- premium;
- architectural;
- editorial;
- physical;
- calm but expressive;
- spatial;
- tactile.

Avoid:

- generic dark developer UI;
- excessive cards;
- cheap glassmorphism;
- random floating boxes;
- game-like 3D;
- 2.5D fake depth;
- overly decorative WebGL.

Older experiments involving lighter SaaS/glassmorphism directions are superseded where they conflict with the current textile + mineral architectural system.

---

# 75. PORTFOLIO MATERIAL — CLOTH

Cloth should look like actual textile:

- broad;
- flexible;
- fabric-like;
- soft;
- physically believable;
- capable of folding/draping.

It must not look like:

- a glossy plastic ribbon;
- an extruded spline;
- a procedural strip;
- a thin decorative banner.

---

# 76. PORTFOLIO ARCHITECTURE

Architecture should feel:

- intentional;
- inhabitable;
- sculptural;
- coherent;
- designed as one world.

Avoid:

- disconnected primitive cubes;
- blocks placed only to fill space;
- different unrelated backgrounds per route.

---

# 77. PERSISTENT WORLD PRINCIPLE

Important realization from previous iterations:

**persistent canvas ≠ persistent world**

A single Three.js canvas is not enough.

The actual composition, spatial logic, materials, architecture and transitions must create the feeling of one continuous world.

---

# 78. SITE STRUCTURE

Major sections/routes have included:

1. Home
2. Featured Work
3. Work / Projects
4. Project Detail
5. About
6. Resume
7. Contact

The world should transition between states rather than feel like separate unrelated websites.

---

# 79. CASE STUDIES

Project detail pages should be designed for recruiter comprehension.

A useful compact structure:

- Hero
- approximately 3 major chapters
- evidence/results
- technologies/repository references

Do not expose every implementation detail directly in the page.

GitHub can hold deeper technical detail.

KLTN is a flagship project.

Smaller projects should not be artificially expanded to equal size.

Flight project context:

**team of 4**

when that project is described.

---

# 80. PORTFOLIO INTERACTION

Cloth interaction concepts include:

### Idle

subtle sway.

### Pointer

local force / disturbance.

### Click

impulse.

### Scroll

can affect:

- camera;
- architecture state;
- cloth state.

Cloth should have physical inertia/delay.

It should not behave as a cursor follower.

---

# 81. CLOTH / 3D TEXT INTERACTION

An explored visual direction:

cloth interacts with 3D name letters.

Possible behaviors:

- drape;
- snag;
- contact;
- drag;
- wind;
- collision.

Important:

contact must support an authored composition.

Physics must not randomly determine the main silhouette.

---

# 82. BLENDER ENVIRONMENT

User's machine:

Windows.

Blender version:

**Blender 5.2.1 LTS**

Known successful command pattern:

`powershell -ExecutionPolicy Bypass -File .\run_blender_windows.ps1 -Fresh`

Local Blender execution has been successfully achieved in later work.

---

# 83. BLENDER ISSUES ALREADY SOLVED/ENCOUNTERED

Historical technical issues:

- incorrect/changed Eevee API;
- EEVEE_NEXT incompatibility assumptions;
- compositor problems;
- active scene issues;
- PowerShell script paths;
- Blender 5.2 API differences.

Do not interpret an old package where Blender execution failed as proof that Blender currently cannot run.

Different handoff packages/runs captured different states.

---

# 84. IMPORTANT PORTFOLIO STATUS DISTINCTION

There have been two kinds of failure:

### Technical execution failure

Example:
Blender/script did not run.

### Visual failure

Example:
scene rendered successfully, but looked wrong.

The later project problem is primarily the second category.

Running code successfully does not mean the phase passed.

---

# 85. PORTFOLIO ITERATIONS

Multiple iterations/packages were produced, roughly across:

R03 → R16 and later audit/masterplan work.

Some versions successfully generated:

- `.blend`;
- clay renders;
- beauty renders;
- diagnostics;
- checkpoints;
- contact sheets.

Many were still visually rejected.

---

# 86. MAJOR FAILURE — CAMERA

Earlier scenes did not reproduce the intended spatial composition.

Issues included:

- incorrect perspective;
- incorrect camera distance;
- wrong compression;
- failure to design composition from camera view first.

Camera must be treated as a core design variable.

---

# 87. MAJOR FAILURE — RIBBON

Older ribbon construction relied too much on:

- procedural curves;
- spline/extrusion;
- displacement;
- tightly authored synthetic forms.

Result:

- looked procedural;
- looked like ribbon/plastic;
- lacked broad fabric masses;
- lacked front/back layering;
- did not read as linen cloth.

---

# 88. MAJOR FAILURE — ARCHITECTURE

Earlier architecture often consisted of simple disconnected primitives.

Result:

- composition felt assembled rather than designed;
- cloth and architecture did not share one spatial logic.

Architecture must be designed around the camera/state composition.

---

# 89. MAJOR FAILURE — ANIMATION-FIRST

Animation was developed before the still art direction was correct.

This caused:

- wasted implementation;
- polished movement around incorrect forms;
- harder debugging.

New rule:

**static frame first.**

---

# 90. R06 / R07 LESSONS

Historical experiments with passive cloth / support systems were rejected.

Problems included:

- cloth being too constrained;
- over-authored support structure;
- one pose reused across too many camera states;
- insufficient deformation;
- still reading as a ribbon rather than broad textile.

One audit recorded displacement around only a few millimeters in an experiment, making the motion visually insignificant.

Do not reproduce those support-heavy strategies as the main solution.

---

# 91. R08 STATUS

R08 was technically useful but visually not approved.

Audit observations included:

- cloth appearing compressed/crumpled;
- insufficient broad sail-like masses;
- weak front/back layering;
- architecture still reading as blockout.

One possible diagnostic suggested a long textile span being compressed into a shorter architectural distance.

That was a hypothesis/diagnostic clue, not a final proven explanation.

---

# 92. PORTFOLIO QUALITY ASSESSMENT

At one point the user estimated the visual/animation quality at roughly:

**40%**

Meaning:

technically present but far from the intended artistic quality.

The solution is not incremental polish alone.

---

# 93. PORTFOLIO PIPELINE — CURRENT

Latest required workflow:

**Audit**
**→ Visual Analysis**
**→ Visual System**
**→ Spatial World**
**→ Camera/State Storyboard**
**→ Ribbon Spec**
**→ Architecture Spec**
**→ Materials**
**→ Blender Handoff**

The purpose is to lock visual thinking before heavy implementation.

---

# 94. PHASE STRATEGY

General phase model used:

### Phase 1

Scope & flow lock.

Includes:

- sitemap;
- recruiter journey;
- purpose of sections.

### Phase 2

UI/UX foundation.

Includes:

- wireframes;
- grid;
- typography;
- desktop/mobile.

No dependency on 3D.

### Phase 3

High-fidelity UI.

Major pages designed statically.

### Phase 4

Blender world.

Includes:

- architecture;
- cloth;
- 3D text;
- materials;
- lighting;
- cameras;
- states.

Later phases:

- asset preparation;
- GLB;
- LOD;
- proxies;
- WebGL integration;
- interactions;
- optimization;
- QA.

Key principle:

**UI/UX approval before full Blender world build.**

---

# 95. METHOD D — REJECTED

A previous approach built the cloth from multiple pieces/patches and then attempted to connect them.

Problems:

- topology discontinuity;
- bad silhouette;
- patch boundaries;
- connector artifacts;
- poor macro continuity.

This approach is rejected.

Do not revive it.

---

# 96. METHOD E — CURRENT REQUIRED CLOTH METHOD

Latest chosen approach:

# METHOD E

## SINGLE CONTINUOUS RIBBON + 3D GUIDE SPINE + STATE SHAPE KEYS

Pipeline:

`3D guide spine  
→ width / roll / twist controls  
→ continuous quad ribbon  
→ camera-first macro shaping  
→ state shape keys  
→ explicit contact zones  
→ secondary cloth relaxation  
→ material`

---

# 97. METHOD E — TOPOLOGY RULE

Use:

**one continuous quad sheet**

for the entire cloth/ribbon.

Do not divide into:

- A;
- B;
- C;
- D

separate patches.

Do not use point-only connectors.

Do not copy separate cloth meshes per section just to fake continuity.

---

# 98. METHOD E — MASTER TOPOLOGY

Use one master topology.

Indicative longitudinal resolution discussed:

approximately:

**60–100 segments**

Exact value can change based on scene scale and deformation needs.

The important constraint is continuous topology, not the exact segment count.

---

# 99. METHOD E — MACRO SHAPE

Primary shape comes from:

- 3D guide spine;
- width variation;
- roll;
- twist;
- authored macro shaping.

Do not build a flat coarse grid and then randomly use Grab strokes hoping to discover the composition.

Silhouette must be intentional.

---

# 100. METHOD E — CAMERA-FIRST

Every major cloth state should be designed relative to the target camera.

Priorities:

1. silhouette;
2. negative space;
3. readability;
4. contact;
5. architecture relationship;
6. depth layering.

Only after these work should micro folds matter.

---

# 101. METHOD E — STATE SHAPE KEYS

Macro states should be authored.

Shape keys/state deformation can encode transitions.

Known state names from project planning include:

- HOME_PRE
- HOME_SNAG
- FEATURED_01
- FEATURED_02
- WORK
- PROJECT
- ABOUT
- CONTACT

Not every state requires an entirely unrelated mesh.

They should derive from the same continuous topology.

---

# 102. METHOD E — CONTACT ZONES

Important contacts must be designed explicitly.

Examples:

- cloth ↔ architecture;
- cloth ↔ 3D letters;
- cloth ↔ ledges/forms.

Do not expect a physics engine to discover aesthetically correct contacts automatically.

---

# 103. METHOD E — PHYSICS

Physics is a secondary layer.

Use it for:

- small relaxation;
- secondary folds;
- subtle motion;
- natural response.

Do not use simulation to create the primary art-directed silhouette.

Rule:

**author macro → simulate secondary.**

---

# 104. PORTFOLIO STATIC VISUAL GATE

Before moving to:

- WebGL integration;
- interaction polish;
- advanced animation;
- export optimization;

the static scene must pass.

Evaluate:

- silhouette;
- composition;
- continuity;
- cloth readability;
- architecture coherence;
- camera;
- material;
- lighting;
- desktop crop;
- mobile crop.

If static frames fail:

**STOP.**

Do not polish downstream systems.

---

# 105. PORTFOLIO — DO NOT REPEAT

Do not:

- return to Method D;
- make separate cloth patches;
- use point-only connectors;
- rely on spline extrusion as final textile;
- let simulation design macro form;
- create random primitive architecture;
- polish material while silhouette is wrong;
- build animation before static approval;
- claim success only because Blender rendered;
- ask user to run endless packages with no visual hypothesis.

---

# 106. PORTFOLIO — CURRENT BLOCKER

The key blocker is not primarily:

- Blender installation;
- PowerShell;
- render automation.

The key blocker is:

**art direction / macro spatial composition / cloth form.**

Specifically:

- continuous textile silhouette;
- architecture relationship;
- camera framing;
- state composition.

---

# 107. PORTFOLIO TARGET QUALITY

User wants production-quality presentation.

Informal internal references such as “R10 quality” mean:

- coherent;
- intentional;
- visually premium;
- not merely functional.

A technically working render is not sufficient.

---

# 108. PORTFOLIO HANDOFF BEHAVIOR

When another agent receives the project:

First read:

- latest audit;
- visual evidence;
- method decision;
- state definitions.

Do not begin by regenerating an old handoff/package if the latest handoff already exists.

Continue from the latest visual gate.

---

# 109. F&B EXPERIENCE

User has practical F&B experience.

### Phúc Long

Approximately:

**6 months**

### Katinat

Approximately:

**2 years**

roughly:

**10/2024 – 09/2026**

One known workplace context:

**Katinat Takashimaya**

User has worked across multiple F&B positions/tasks rather than only one narrow station.

---

# 110. STARBUCKS INTERVIEW CONTEXT

User previously prepared for a Starbucks interview.

Needed:

- short English self-introduction;
- simple explanation of experience;
- mention approximately two years at Katinat;
- ability to work across multiple positions.

The user did not want an overly long English speech.

---

# 111. QC JOB CONTEXT

User applied/considered a QC position.

One opportunity had approximate hours:

**08:30–17:30**

There was some referral/internal connection.

The user believed there was a reasonably good chance but understood the position was not guaranteed.

CV was adjusted at one point to include/target QC.

---

# 112. BUFFET JOB CONTEXT

Another job considered:

buffet / charcoal-related work.

Approximate schedule:

**10:00–16:00**

Frequency:

**6 days/week**

Pay discussed:

approximately **45,000 VND/hour**

Location:

relatively close to home.

The user initially accepted and then reconsidered.

Main concerns:

- physical fatigue;
- conflict with QC opportunity;
- uncertainty about whether short training/work would be paid;
- not wanting to join and immediately leave.

User ultimately wanted to decline cleanly rather than waste both sides' time.

---

# 113. PROFESSIONAL WRITING PREFERENCE

For messages such as:

- declining interview;
- cancelling a job;
- HR email;
- complaint;
- application;

user usually wants:

- natural Vietnamese;
- not robotic;
- polite;
- concise;
- appropriate for Zalo/email.

Do not make ordinary Zalo messages excessively formal.

---

# 114. CV — F&B

Preferred style:

- simple;
- clean;
- energetic;
- recruiter-friendly.

Avoid:

- overly technical sections;
- visually complicated layouts;
- unnecessary decorative graphics.

When using a user's photo:

do not regenerate their face unless explicitly requested.

---

# 115. PHOTO EDITING PREFERENCE

When editing the user's portrait:

preserve facial identity.

If asked to:

- remove background;
- remove glasses;
- change hairstyle;
- prepare CV image;

do not invent a different face.

The user has previously complained when an image edit changed the face instead of only performing the requested transformation.

---

# 116. HAIRSTYLE PREFERENCE CONTEXT

A style previously requested:

- short Korean male hairstyle;
- very short/tapered/tomboy-like cut;
- remove glasses;
- preserve original face.

This is context, not a permanent personal appearance requirement.

---

# 117. WINDOWS / DEVELOPMENT ENVIRONMENT

User works primarily on:

**Windows**

Common tools:

- VS Code;
- Chrome;
- Microsoft Office;
- Zalo;
- Discord;
- Git;
- Node.js;
- PowerShell;
- Blender.

User prefers a relatively minimal setup.

Do not suggest installing large amounts of unnecessary software.

---

# 118. POWERSHELL

The user has encountered execution policy issues.

Common workaround used:

`powershell -ExecutionPolicy Bypass ...`

Node/npm scripts have also previously been affected by PowerShell execution policy.

---

# 119. GIT

User has configured Git identity/settings in the past.

No need to explain Git installation from zero unless the environment has changed.

---

# 120. SQL SERVER

User has previously had SQL Server installation/setup issues.

Do not assume SQL Server is the preferred database for newer projects.

Current Adaptive Learning project uses:

**PostgreSQL**

---

# 121. PHONE

Device previously discussed:

**Samsung Galaxy S21**

Problem encountered:

black/broken screen.

The user attempted USB/ADB access.

Commands used included:

`.\adb kill-server`

`.\adb start-server`

`.\adb devices`

Result at the time:

no device appeared.

PnP search for:

- Samsung;
- Android;
- MTP

also returned nothing.

Therefore the failure was likely occurring before normal ADB authorization/communication.

Do not assume the device was successfully connected.

---

# 122. CAMERA

Camera:

**Fujifilm A800**

The user bought/uses a Japanese-language unit and initially did not know the controls well.

Relevant help topics:

- menu navigation;
- exposure/settings;
- basic shooting;
- getting the most out of the old compact-camera look.

---

# 123. KEYBOARD

Keyboard context:

**Razer BlackWidow Ultimate**

Model referenced:

**RZ03-0170**

---

# 124. MOTORBIKE

Motorbike:

**Honda Vision 2016**

User previously asked about:

- tubeless vs tube tires;
- flat/soft tire;
- repair/replacement cost.

Do not assume a specific repair has already been completed.

---

# 125. TRAVEL STYLE

User is generally price-sensitive.

Preference:

maximize the experience while minimizing unnecessary accommodation costs.

If the user spends most of the day outside:

cheap but acceptable accommodation is fine.

Spend more on accommodation only where:

- location;
- comfort;
- actual usage

justify it.

---

# 126. VIETNAM BEACH TRAVEL

One earlier domestic trip request had budget around:

**2 million VND**

Wanted:

- beach/island;
- not Vũng Tàu.

Places considered:

- Nam Du;
- Hòn Sơn.

---

# 127. MALAYSIA / SINGAPORE TRIP

User planned a Malaysia trip combined with Singapore.

Important fixed activity:

**The Weeknd show on 4 November**

in Kuala Lumpur according to the user's itinerary context.

One accommodation referenced:

**Axon**

The user planned to use the nicer stay selectively rather than throughout the trip.

Travel priorities:

- logical geographic route;
- low transport waste;
- cheap accommodation on exploration-heavy days;
- reasonable access to key areas.

Bukit Bintang was discussed as a central Kuala Lumpur area.

---

# 128. LOCAL FOOD / PLACE SEARCH PREFERENCE

When requesting local recommendations, the user cares about:

- distance;
- real price;
- value;
- actual user sentiment.

The user does not want recommendations based only on star ratings.

Preferred evidence may include:

- recent reviews;
- community discussion;
- social-media sentiment;
- repeated complaints/praise.

The user is aware that ratings/reviews can be spammed or manipulated.

---

# 129. FOOD CONTEXT EXAMPLES

Past searches/comparisons included:

- Korean food;
- Dookki;
- Spicy Box;
- Moongo;
- bánh mì nướng muối ớt;
- other affordable local food.

The user often asks:

“which one is actually better?” rather than merely “which one has the highest rating?”

---

# 130. SWIMMING / LOCAL ACTIVITY SEARCH

The user has also searched for:

- swimming pools in Ho Chi Minh City;
- session times;
- pricing;
- nearby locations.

Examples discussed historically included pools such as:

- Cộng Hòa;
- Tân Bình;
- Tô Ký;
- Phú Lâm.

Treat schedule/price as time-sensitive and verify when asked again.

---

# 131. PRODUCT NAMING STYLE

User likes names that:

- are short;
- pronounce easily;
- are memorable;
- can be semantically loose or invented;
- work reasonably in Vietnamese and English;
- feel friendly rather than corporate.

The user is willing to use meaningless names if the phonetics are strong.

---

# 132. PROJECT / FILE WORKFLOW

When the user uploads:

- ZIP;
- DOCX;
- PDF;
- code;
- Blender package;

the user often expects direct inspection.

Do not respond only with generic instructions if the file can be analyzed.

For a ZIP project:

inspect:

- structure;
- relevant code;
- reports;
- screenshots/renders;
- current state.

Then identify what actually needs changing.

---

# 133. DOCUMENT EDITING SCOPE RULE

If the user says:

“only change X”

then only change X.

Examples:

- only table typography;
- only cover pages;
- only headers;
- only page numbering.

Do not opportunistically reformat the whole document.

This has previously caused frustration.

---

# 134. DELIVERABLE EXPECTATION

When asking to “làm” something, the user often expects an actual artifact when tooling permits:

- PDF;
- DOCX;
- ZIP;
- prompt;
- report;
- Blender package;
- image;
- code.

The user generally does not want a long tutorial instead of the requested deliverable.

---

# 135. PROMPT / AGENT HANDOFF STYLE

When creating a prompt for another agent, include:

### Background

What the project is.

### Current state

Exactly where work stopped.

### Evidence

What works and what fails.

### Rejected methods

What must not be repeated.

### Required method

What should be implemented.

### Constraints

Technical and visual restrictions.

### Acceptance gate

What constitutes success.

### Deliverables

Exact expected files/output.

Avoid vague prompts such as:

“make it better.”

---

# 136. DECISION PRECEDENCE — PORTFOLIO

The following latest decisions override older ones:

### OLD

Decorative procedural ribbon / generic 3D SaaS feel.

### NEW

Real linen textile as primary visual actor.

---

### OLD

Disconnected per-page scenes.

### NEW

One coherent persistent spatial world.

---

### OLD

Animation-first experimentation.

### NEW

Static art-direction gate first.

---

### OLD

Method D patch assembly.

### NEW

Method E continuous master topology.

---

### OLD

Physics discovers form.

### NEW

Authored macro pose + secondary physics.

---

# 137. DECISION PRECEDENCE — ADAPTIVE LEARNING

The following rules are currently stronger than earlier generic ideas:

### No infinite social feed.

Use a finite learning cycle.

### Five roles:

Review
Learn
Retrieve
Transfer
Check

### Skip is evidence.

Not mastery.

### Attempt first when appropriate.

Not blindly.

### Curriculum controls validity.

Engagement UI cannot decide curriculum.

### ML is not mandatory for every recommendation.

Fallback must exist.

---

# 138. DECISION PRECEDENCE — KLTN

Use final thesis/source files when exact figures conflict.

Known historical conflicts:

### OULAD registration count

32,539 vs 32,593.

### OULAD static feature count

47 vs 49.

For conceptual explanations these differences normally do not change the model design.

For formal thesis reporting or implementation:

**verify the actual final artifact.**

Do not silently pick one.

---

# 139. CURRENT PROJECT PRIORITY SNAPSHOT — 23 SEPTEMBER 2026

## KLTN

Status:

**Essentially completed**

Remaining work, if any, is formatting/archival rather than research architecture.

---

## Career

Status:

**Active transition into employment**

Primary technical target:

**Data Analyst**

---

## Google Data Analytics

Status:

**In progress**

---

## Adaptive Language Learning

Status:

**Phase 1 active**

Architecture baseline:

**V3.2 frozen/source of truth**

---

## PHUC Spatial Portfolio

Status:

**Active**

Technical Blender execution:

generally working.

Main unresolved issue:

**visual art direction / continuous textile form / spatial composition**

Current required ribbon solution:

**Method E**

---

# 140. WHAT A NEW ACCOUNT SHOULD NOT ASK AGAIN

Unless the project context has changed, avoid repeatedly asking:

- What is your thesis about?
- What datasets did you use?
- What is your target career?
- What is your portfolio visual style?
- What Blender version do you use?
- What stack is the language app using?
- Do you want infinite scroll?
- What is the 5-minute learning cycle?
- Do you want Data Analyst or Data Engineer?
- Should the cloth be procedural ribbon or fabric?
- Should Method D be tried again?

Those answers already exist here.

---

# 141. WHAT SHOULD BE RE-VERIFIED WHEN NECESSARY

Some things should not be treated as permanently fixed:

- exact job currently being pursued;
- current CV version;
- current Google course progress;
- product name;
- travel schedule;
- local restaurant prices;
- local business opening status;
- current Blender package/run;
- current source file version;
- exact thesis figures where historical notes conflict.

Use the newest data available.

---

# 142. PRIVACY / INTENTIONALLY OMITTED ITEMS

This transfer intentionally does not preserve:

- passwords;
- login credentials;
- API keys;
- authentication tokens;
- banking details;
- recovery codes.

Contact details and identifying numbers that may have existed in CV/thesis conversations should be obtained from the user's current files when actually needed rather than treated as general conversational memory.

Sensitive health or similarly private information is not part of this persistent project profile.

---

# 143. GENERAL RULE FOR THE NEW ACCOUNT

The user has already invested substantial time in developing these systems.

Do not treat every conversation as greenfield.

Use prior decisions.

Challenge them only when there is actual evidence that they are wrong.

When changing direction:

state clearly:

- why;
- what evidence caused the change;
- what previous decision is being superseded.

The user is receptive to changing a plan when the root cause is demonstrated.

The user is not receptive to random iteration without evidence.

---

# 144. ONE-PARAGRAPH USER SUMMARY

Trần Hoàng Phúc is a HUFLIT Data Science graduate/student transitioning toward Data Analyst roles with a longer-term Data Engineering direction. His major academic project is a hybrid early-warning system using UCI Student Performance and OULAD with strict leakage prevention, multi-branch static/CNN/BiLSTM modeling and an intervention/recommendation component. His current major projects are an adaptive English-learning product whose V3.2 architecture baseline is complete and whose Phase 1 uses Flutter + FastAPI + PostgreSQL with a finite five-minute Review/Learn/Retrieve/Transfer/Check learning cycle, and the PHUC Spatial Portfolio, a premium recruiter-facing spatial website centered on continuous ivory linen cloth, warm mineral architecture and editorial typography. The portfolio is currently blocked by visual form rather than Blender execution, and the latest required solution is Method E: one continuous quad cloth driven by a 3D guide spine, camera-first authored states, explicit contacts and only secondary cloth simulation. He prefers concise communication, actual deliverables, root-cause analysis, strict change scope, phase gates and evidence rather than endless trial-and-error.

---

# END OF MASTER MEMORY TRANSFER

Snapshot date: 23 September 2026