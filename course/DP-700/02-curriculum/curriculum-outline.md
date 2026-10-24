# Curriculum outline — DP-700 practice course

**Six 100-item mock exams · 600 original questions · 100-minute rehearsal or untimed first pass**

This outline turns the bank into a study sequence. Each exam is blueprint-weighted **33 / 33 / 34**, so the order below is about scenario complexity and topic reinforcement, not about weighting.

Microsoft publishes a **100-minute** duration but no item count for DP-700, and a 100-item exam is deliberately larger than a comfortable sitting. `6 × 100 = 600` lets each blueprint be drilled twice without repeating a question, so treat the clock as a rehearsal of the published duration rather than a model of the live item count.

## Learning arc

| Phase | Exam | What it stresses | Study goal |
|---|---|---|---|
| Foundation | 1 | Workspace settings, lifecycle, security, lakehouse ingestion | Establish the vocabulary: workspace, capacity, lakehouse, shortcut, deployment pipeline, OneLake role |
| Governance | 2 | Deployment rules, masking, labels, star schema, type 2 history | Connect a design decision to the failure it prevents |
| Real time | 3 | Eventstreams, structured streaming, KQL windows, monitoring | Decide between similar-sounding controls using the constraint in the stem |
| Modelling | 4 | Domains at scale, catalogue history, conforming, reject rows | Choose the pattern that survives an audit and a schema change |
| Performance | 5 | Delta optimization, Spark skew, warehouse plans, capacity | Make a measured improvement instead of a hopeful one |
| Integration | 6 | Everything, across four industries | Perform under a 100-minute clock with mixed item formats |

## Exam-by-exam study plan

### Exam 1 — Lakehouse foundations and ingestion (100 items)
- Official split: 33 / 33 / 34.
- Case studies: Adventure Works Cycles, Contoso Energy, Fabrikam Logistics, Litware Retail.
- Focus: Spark pools, environments and library pinning, domains, region and capacity choices, Apache Airflow jobs, Git and database projects, deployment pipelines, workspace and item access, row, column, object and file-level security, dynamic data masking, sensitivity labels, endorsement, audit logs, OneLake security, the Dataflow Gen2 versus pipeline versus notebook decision, schedules, event triggers and dynamic parameters, bronze to gold loading, shortcuts, mirroring, Get Metadata, and a first streaming path.
- Target skill: name the constraint in the stem before reading the options.

### Exam 2 — Governance, lifecycle, and the warehouse (100 items)
- Case studies: Woodgrove Bank, Alpine Ski House, Northwind Traders, Proseware Media.
- Focus: default environments, stage comparison and deployment rules, feature branches and conflict resolution, DACPAC deployment with SQLCMD variables, folder grants, masking exemptions, default and inherited labels, audit export windows, OneLake roles and groups, star schemas, surrogate keys, type 2 dimensions, merge patterns, conformed unions, checkpoints, watermarks, and a no-code streaming path.
- Target skill: decide where a control must sit so the failure it prevents cannot happen elsewhere.

### Exam 3 — Real-time intelligence and operational monitoring (100 items)
- Case studies: Beacon Health, Riverside Transit, Tailspin Toys, Consolidated Courier.
- Focus: eventstream sources and destinations, native tables versus OneLake shortcuts, query acceleration, structured streaming, KQL update policies, checkpoints and watermarks, tumbling, hopping and sliding windows, materialized views, ingestion failure tables, eventstream runtime metrics, Monitoring hub and activity logs, alerts and Data Activator rules, retry and error branches, and retention against cost.
- Target skill: choose the control that makes the failure visible rather than silent.

### Exam 4 — Dimensional modelling, history, and multi-workspace governance (100 items)
- Case studies: Coho Winery, Trey Research, Nod Publishers, Fourth Coffee Roasters.
- Focus: domains across forty trial workspaces, folder-scoped OneLake roles, certification and promotion, type 2 dimensions that reconstruct an old catalogue, surrogate keys after a rekey, pivot and grouping, conformed columns before a union, reject tables, duplicate and late-data rules, and a null default that quietly changes an average.
- Target skill: separate "what a consumer must be able to prove" from "what is easiest to build".

### Exam 5 — Performance, scale, and reproducible reporting (100 items)
- Case studies: Lakeshore Retail Group, Margie Travel, Wide World Importers, VanArsdel Manufacturing.
- Focus: 240,000 small files, V-Order, OPTIMIZE, VACUUM, partitioning and Z-Order, broadcast joins, salting a hot key, shuffle partitions, coalesce and repartition, warehouse statistics and distribution keys, batched inserts, capacity scaling and smoothing, eventhouse retention and caching, and proving a revenue figure from the gold layer.
- Target skill: keep cost, latency, and correctness as three separate arguments.

### Exam 6 — Cross-industry capstone (100 items)
- Case studies: Bellows College, Munson Sporting Goods, Relecloud Telecom, Granite Peak Outfitters.
- Focus: one governed platform across suppliers, colleges and networks, multi-channel ingestion, streaming alerts inside two minutes, peak-season capacity, classification and audit evidence, and the full design-build-release-observe loop.
- Recommended: attempt under a 100-minute timer with no notes, then review every explanation.
- Target skill: hold many constraints at once without collapsing them into one "best practice".

## Item formats and how to rehearse them

| Format | Per exam | How to practise |
|---|---:|---|
| Single-choice | 76 | Decide the constraint first, then eliminate options that solve a different problem |
| Multi-select | 16 | Count the required selections before reading options; reject "true but not asked" statements |
| Sequencing (exported as multiple-choice) | 8 | Find the step that cannot move — land before validate, transform before publish, measure before tune — and anchor the rest |
| Case study | 4 × 3 | Read once, write the three or four hard constraints, then answer each item against them |

## Suggested eight-week schedule

| Week | Work | Deliverable |
|---|---|---|
| 1 | Study domain 1 objectives, take Exam 1 in two halves | Mistake log by local skill |
| 2 | Study domain 2 objectives, take Exam 2 untimed | A one-page diagram of one load: source, landing, curated, published |
| 3 | Re-read missed explanations from Exams 1–2, retake both timed | Two timed scores plus error categories |
| 4 | Domain 3, streaming half: take Exam 3 | A real-time checklist: source, destination, window, retention, alert |
| 5 | Domain 3, monitoring half: take Exam 4 | A monitoring plan naming the evidence for each failure mode |
| 6 | Take Exam 5; review optimization items | A tuning log: plan read, change made, measurement after |
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

| Segment | Items | Suggested time (100-minute clock) |
|---|---:|---:|
| First pass, multiple-choice and multi-select | 76 | 66 minutes |
| Sequencing items (multiple-choice) | 8 | 9 minutes |
| Case studies | 12 | 17 minutes |
| Review of flagged items | 4 | 8 minutes |

Microsoft publishes a 100-minute duration for DP-700 but no item count, so a 100-item attempt already exceeds the live item count in principle. The budget above is a deliberate per-item discipline for practice, not a claim about how long the real appointment will feel. Confirm the current appointment length on the certification page before you book.
