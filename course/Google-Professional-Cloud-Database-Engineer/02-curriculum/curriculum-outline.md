# Curriculum outline — Professional Cloud Database Engineer practice course

**Six 100-item mock exams · 600 original questions · a two-hour rehearsal that runs slower than the live paper**

This outline turns the bank into a study sequence. Every exam is blueprint-weighted **32 / 25 / 23 / 20** — the published weights themselves, which total exactly 100% — so the order below is about decision difficulty and topic reinforcement, not about weighting.

Google publishes a **50–60 question range**, a **two-hour** length, **no prerequisites**, and **no case-study component**. A 100-item exam is deliberately larger, which has one consequence worth stating plainly: **the bank runs slower than the live exam per item.** 100 items in two hours is about **72 seconds per item**; the live 50–60 item paper allows roughly **120–144 seconds** each. Practise here under the two-hour clock and you will be training at a more generous pace than the appointment itself — useful for building explanation habits, not for simulating time pressure.

## Learning arc

| Phase | Exam | What it stresses | Study goal |
|---|---|---|---|
| Foundation | 1 | Sizing, availability topology, connectivity, encryption, database selection, cost | State the requirement before naming a product |
| Operations | 2 | IAM, users, diagnosis, vitals, backups, retention, scaling | Separate the symptom from the mechanism |
| Migration | 3 | Strategy, tool selection, conversion, validation, cutover, fallback | Name the downtime budget before choosing a tool |
| Deployment | 4 | Provisioning from code, failover testing, replication, read scaling | Prove the recovery path instead of assuming it |
| Integration | 5 | Mixed operations and cost control | Hold reliability and cost in the same answer |
| Review | 6 | All four sections in design-review form | Decide out of topic order, under time |

## Exam-by-exam study plan

### Exam 1 — Sizing, availability design, and database selection (100 items)
- Official split: 32 / 25 / 23 / 20.
- Focus: sizing from measured peaks rather than guesses, compute and storage trade-offs, machine and storage classes across Cloud SQL, Bigtable, Spanner and AlloyDB, zonal versus regional versus multi-regional topologies, maintenance windows and deny periods, private connectivity, Cloud SQL Auth Proxy and PSC, IAM database authentication, session pooling, customer-managed keys and rotation, audit logging and sinks, managed versus self-managed versus partner offerings, SQL versus NoSQL versus vector workloads, comparative cost, application dependencies, residency and organization policy, and federation or hybrid spans.
- Target skill: for every scenario, write the requirement as a constraint — availability, latency, residency, budget — before naming a service.

### Exam 2 — Operations, access, backup, and performance (100 items)
- Focus: IAM roles and database users, passwordless authentication, slow queries and missing indexes, lock contention, instance vitals and quota limits, alerting on symptoms rather than on resources, backup and point-in-time recovery against stated RTO and RPO, export and import, retention, scaling up versus out, replication strategy, query optimization, scheduled maintenance, and upgrade testing.
- Target skill: distinguish "what changed" from "what saturated", then choose the smallest change that restores the objective.

### Exam 3 — Migration strategy, conversion, and cutover (100 items)
- Focus: continuous replication versus an accepted outage, Database Migration Service for same-engine and cross-engine moves, change data capture for warehouse feeds, conversion workspaces, unsupported procedural code, sequence resets, keeping a target current during a long load, reconciliation and replay, cutover runbooks with abort conditions, connection-string switching, reverse replication, and decommissioning the source.
- Target skill: state the downtime budget and the fallback requirement first; the tool follows from those two numbers.

### Exam 4 — Deployment, high availability, and disaster recovery (100 items)
- Focus: provisioning from a reviewed definition, failover and promotion drills, multi-regional configurations and secondary clusters, read replicas and read pools, fleet monitoring, promotion mechanics, fencing an old primary, connection routing that follows the current primary, and the standby capacity a real failover needs.
- Target skill: treat every availability claim as untested until a drill has measured it.

### Exam 5 — Mixed operations and cost control (100 items)
- Focus: cost levers (commitments, right-sizing, idle instances, storage class, retention) interleaved with availability, diagnosis and migration decisions, so the workload mix resembles a normal week rather than a single topic.
- Target skill: attribute a cost change to a design decision, and a saving to a risk that was accepted.

### Exam 6 — Integrated review across all four sections (100 items)
- Focus: design-review questions that pair constraints — residency with least privilege, availability with cost, migration speed with a lossless rollback, observability with audit evidence.
- Recommended: attempt under a two-hour timer with no notes, then review every explanation.
- Target skill: keep four constraints in one answer without collapsing one into another.

## Item formats and how to rehearse them

| Format | Per exam | How to practise |
|---|---:|---|
| Single-answer | 84 | Name the constraint first, then eliminate options that solve a different problem |
| Multi-select | 16 | Count the required selections before reading options; reject "true but not asked" statements |
| Case study | 0 | Not part of this exam's published format, so not practised here |
| Sequencing or drag-and-drop | 0 | Not part of this exam's published format, so not practised here |

## Suggested eight-week schedule

| Week | Work | Deliverable |
|---|---|---|
| 1 | Study section 1 objectives, take Exam 1 untimed | Mistake log by local study area |
| 2 | Sections 2 and 3, take Exams 2 and 3 untimed | One table: downtime budget versus migration tool |
| 3 | Re-read missed explanations from Exams 1–3, retake Exam 2 timed | Timed score plus error categories |
| 4 | Section 4, take Exam 4 | A recovery sheet: objective → mechanism → cost |
| 5 | Take Exam 5 | A cost sheet: change → saving → accepted risk |
| 6 | Take Exam 6 under the two-hour clock | Timed score plus pace per item |
| 7 | Retake the weakest exam, then re-read its explanations cold | One page of the decisions that settle most questions |
| 8 | Final pass over the 51-study-area map | Readiness note, no score conversion |

## Scoring your own attempt

1. Score each item correct or incorrect; there is no partial credit for multi-select.
2. Group misses by local study area, not by exam number.
3. Classify each miss: unknown product, misread constraint, plausible-but-wrong option, or rushed guess.
4. Only the last two categories improve with more practice tests; the first two need documentation study or hands-on work.
5. Re-attempt the same exam after a week before trusting an improvement.

Google does not publish a passing score for the Professional Cloud Database Engineer exam, so no percentage here converts to a pass mark and a practice percentage is not a scaled score.

## Time budget inside a 100-item exam

| Segment | Items | Suggested time (two-hour clock) |
|---|---:|---:|
| First pass, single-answer | 84 | 80 minutes |
| Multi-select | 16 | 22 minutes |
| Review of flagged items | — | 18 minutes |

The live exam delivers 50–60 questions in two hours, which is 120–144 seconds per item — noticeably more generous than this bank's 72 seconds. A comfortable finish here therefore does **not** prove you would finish the live paper quickly; it proves you can reason steadily. If you want time pressure, shorten the clock deliberately rather than assuming the bank provides it.

## What this course does not cover, on purpose

- **No case studies.** The published format has no case-study component.
- **No console recipes.** Configuration judgement is in scope and is tested as a decision — which mechanism, why, and what it costs — not as a click path. The test suite rejects console-instruction phrasing.
- **No labs or interactive items.** They cannot exist in a CSV and are not part of the published format.
- **No passing score.** Google does not publish one, so none is stated.
