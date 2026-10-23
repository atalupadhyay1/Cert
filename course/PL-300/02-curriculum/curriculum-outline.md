# Curriculum outline — PL-300 practice course

**Six 100-item mock exams · 600 original questions · 100-minute pace drill or 150-minute review**

This outline turns the bank into a study sequence. Each exam is blueprint-weighted **28 / 28 / 28 / 16**, so the order below is about scenario complexity and topic reinforcement, not about weighting.

A 100-item exam is deliberately longer than the live 40–60 items. `6 × 100 = 600` lets each blueprint be drilled twice without repeating a question, so the real 100-minute clock does not map item-for-item onto a practice attempt.

## Learning arc

| Phase | Exam | What it stresses | Study goal |
|---|---|---|---|
| Foundation | 1 | Storage modes, profiling, shaping, first contact with DAX and visuals | Establish the vocabulary: folding, cardinality, filter context, measure |
| Applied model | 2 | Relationships, date tables, time intelligence, refresh and security | Connect a model decision to the report behaviour it produces |
| Judgment | 3 | Calculation groups, role-playing dates, dynamic security, deployment | Decide between similar-sounding options using the constraint in the stem |
| Operating context | 4 | Grain reduction, hierarchies, accessibility, mobile, export governance | Choose the fix that matches who consumes the report and where |
| Accountability | 5 | Consolidation, audiences, governed reuse, procurement of licences | Keep security, freshness, and usability as three separate arguments |
| Integration | 6 | Everything, at group scale | Perform under a 100-minute clock with mixed item formats |

## Exam-by-exam study plan

### Exam 1 — Cross-industry and retail (100 items)
- Official split: 28 / 28 / 28 / 16.
- Case studies: Wingfield Retail, Proseware Health, Litware Financial, Thornbury Consulting.
- Focus: Import versus DirectQuery versus DirectLake, parameters and credentials, profiling before shaping, nulls and de-duplication, custom columns and grouping, unpivot and JSON, merge versus append, star schema, filter context, visual selection, workspace roles, refresh, row-level security.
- Target skill: name the constraint in the stem before reading the options.

### Exam 2 — Healthcare, grocery, insurance, and energy (100 items)
- Case studies: Harborline Grocers, Pinecrest Clinics, Cambria Insurance, Solstice Energy.
- Focus: privacy levels, clinical extract cleaning, relationship direction, role-playing dates, semi-additive balances, incremental refresh, gateway choices, sensitivity labels, accessibility for public dashboards.
- Target skill: place the human or policy control where an error becomes a disclosure or a wrong decision.

### Exam 3 — Banking, insurance, utilities, and logistics (100 items)
- Case studies: Northgate Bank, Fairmont Assurance, Brightwater Utilities, Coastline Logistics.
- Focus: foldable transformations on very large sources, composite models with Dual tables, calculation groups, dynamic row-level security, deployment between workspaces, impact analysis before schema changes.
- Target skill: choose the measurement or control that actually gates a release.

### Exam 4 — Manufacturing, transport, higher education, and libraries (100 items)
- Case studies: Redwood Mills, Skyline Transit, Evergreen University, Lakeshore Library.
- Focus: grain reduction for sensor data, asset hierarchies, static RLS per plant, mobile layouts for field staff, export governance for public content, lineage and impact analysis.
- Target skill: distinguish "identify", "read", "reconcile", and "author" before choosing a workspace role.

### Exam 5 — Retail group, healthcare network, public works, and schools (100 items)
- Case studies: Summit Retail Group, Willow Creek Health, Granite Public Works, Aurora Schools.
- Focus: multi-brand consolidation, snowflake for a shared dimension, app audiences, subscriptions and tile alerts, USERPRINCIPALNAME dynamic security, Build permission for reuse.
- Target skill: keep freshness, security, and usability as three separate arguments.

### Exam 6 — Cross-industry capstone (100 items)
- Case studies: Atlas Holdings, Beacon Mutual, Cedarline Foods, Pinnacle Services.
- Focus: shared standards across subsidiaries, permission-aware reuse of a certified model, one governance pattern, group-wide distribution, refresh at group scale.
- Recommended: attempt under a 100-minute timer with no notes, then review every explanation.
- Target skill: hold many constraints at once without collapsing them into one "best practice".

## Item formats and how to rehearse them

| Format | Per exam | How to practise |
|---|---:|---|
| Single-choice | 76 | Decide the constraint first, then eliminate options that solve a different problem |
| Multi-select | 16 | Count the required selections before reading options; reject "true but not asked" statements |
| Sequencing (exported as multiple-choice) | 8 | Find the step that cannot move — profile, type, shape, load — and anchor the rest |
| Case study | 4 × 3 | Read once, write the three or four hard constraints, then answer each item against them |

## Suggested eight-week schedule

| Week | Work | Deliverable |
|---|---|---|
| 1 | Study domain 1 objectives, take Exam 1 in two halves | Mistake log by local skill |
| 2 | Study domain 2 objectives, take Exam 2 untimed | A one-page star-schema sketch for your own data |
| 3 | Re-read missed explanations from Exams 1–2, retake both timed | Two timed scores plus error categories |
| 4 | Domain 3 objectives, take Exam 3 | A visual-choice cheat sheet for five business questions |
| 5 | Domain 4 objectives, take Exam 4 | Workspace, role, and refresh checklist |
| 6 | Take Exam 5; review DAX and security items | A filter-context note you can explain aloud |
| 7 | Take Exam 6 under a 100-minute clock | Timed score plus pace per item |
| 8 | Retake the weakest exam, review every explanation | Final readiness note, no score conversion |

## Scoring your own attempt

1. Score each item as correct or incorrect; there is no partial credit for multi-select.
2. Group misses by local skill ID, not by exam number.
3. Classify each miss: unknown capability, misread constraint, plausible-but-wrong option, or rushed guess.
4. Only the last two categories improve with more practice tests; the first two need documentation study or hands-on work.
5. Re-attempt the same exam after a week before trusting an improvement.

A practice percentage is not a scaled exam score. Microsoft reports 700/1000 on a scaled scale and does not publish a raw percentage equivalent.

## Time budget inside a 100-item exam

| Segment | Items | Suggested time (pace drill: 100 min) |
|---|---:|---:|
| First pass, multiple-choice and multi-select | 76 | 65 minutes |
| Sequencing items (multiple-choice) | 8 | 10 minutes |
| Case studies | 12 | 15 minutes |
| Review of flagged items | 4 | 10 minutes |

The real appointment is 100 minutes for a typical 40–60 items, so a 100-item attempt cannot reuse that clock directly. The pace drill above is deliberately tighter than the real per-item allowance; the 150-minute option is for learning rather than timing.
