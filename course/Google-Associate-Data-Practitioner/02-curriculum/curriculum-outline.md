# Curriculum outline — Associate Data Practitioner practice course

**Six 100-item mock exams · 600 original questions · 2-hour rehearsal or untimed first pass**

This outline turns the bank into a study sequence. Every exam is blueprint-weighted **30 / 27 / 18 / 25** — the published weights themselves, which total exactly 100% — so the order below is about scenario complexity and topic reinforcement, not about weighting.

Google publishes a **50–60 question range**, a **2-hour** length, **no prerequisites**, and **no case-study component**. A 100-item exam is deliberately larger, so treat the clock as a rehearsal of the published duration rather than a model of the live item count.

## Learning arc

| Phase | Exam | What it stresses | Study goal |
|---|---|---|---|
| Foundation | 1 | ETL/ELT/ETLT, cleaning, transfers, formats, extraction and storage choice, locations, loading | Establish the vocabulary: batch or streaming, which transfer tool, which storage service, which location |
| Reporting | 2 | BigQuery SQL, Colab Enterprise, Looker and LookML, BQML, AutoML, remote models, Model Registry | Connect a presentation choice to the decision it makes possible downstream |
| Pipelines | 3 | Dataform, Dataflow, Dataproc, Data Fusion, Composer, scheduling, monitoring, recovery | Separate *what* must run from *what* must run it, and know what a failure leaves behind |
| Warehouse and keys | 4 | Analytics SQL, shared measures, BQML evaluation, dependency graphs, IAM, lifecycle, KMS | Hold analytics and governance in one decision instead of two |
| Landing zones | 5 | Storage and location choice, DTS and DMS, Data Fusion, Analytics Hub, VPC-SC, roles, classes | Justify where data lands and who may see it with one argument |
| Integration | 6 | Streaming ingestion, transfer schedules, remote models, split design, Dataform tests, retries, KMS | Defend an end-to-end choice when four constraints arrive at once |

## Exam-by-exam study plan

### Exam 1 — Ingestion, reporting, pipelines, and access (100 items)
- Official split: 30 / 27 / 18 / 25.
- Focus: ETL versus ELT versus ETLT, data quality assessment and cleaning, Storage Transfer Service and Transfer Appliance, CSV, JSON, Parquet and Avro, Dataflow, BigQuery Data Transfer Service, Database Migration Service, Data Fusion, storage choice among Cloud Storage, BigQuery, Cloud SQL, Firestore, Bigtable and Spanner, regional, dual-regional, multi-regional and zonal locations, structured versus semi-structured versus unstructured data, `gcloud` and `bq` loading, client libraries, reporting SQL, Looker, Dataform, Composer, IAM least privilege, storage classes, CMEK.
- Target skill: name the constraint in the stem before reading the options.

### Exam 2 — Files, formats, dashboards, and governance (100 items)
- Focus: BigQuery SQL for joins, windows and date filters, Colab Enterprise runtimes and the BigQuery magic, business-question framing, Looker dashboards and scheduled delivery, Looker versus Looker Studio, LookML explores, measures and parameters, BigQuery ML versus AutoML, remote Gemini models in BigQuery, ML project planning, `ML.EVALUATE` and `ML.PREDICT`, Model Registry, and the governance items that decide who reads the output.
- Target skill: decide where a number must be computed once so two teams cannot disagree.

### Exam 3 — Streaming, scheduling, modelling, and recovery (100 items)
- Focus: transformation-tool selection, ELT and ETL pipeline shapes, windows and watermarks, backfills and missed windows, Cloud Scheduler, the Dataflow job interface, Cloud Logging and Cloud Monitoring, Dataproc Workflow Templates, Pub/Sub to BigQuery, Eventarc triggers, and backup, replication and recovery for Cloud SQL and Cloud Storage.
- Target skill: diagnose the failure class first — data, dependency, permission, or capacity — then choose the fix.

### Exam 4 — Warehouse analytics, orchestration, and key management (100 items)
- Focus: retention, cohort and funnel SQL, shared LookML measures, BQML training, evaluation and inference, Dataform dependency graphs, Airflow DAG dependencies and retries, scheduled queries with backfills, IAM least privilege and role granularity, uniform bucket-level access, Analytics Hub exchanges, storage classes, lifecycle rules, backup and replication, CMEK, CSEK and GMEK with Cloud KMS key rings.
- Target skill: prove a governance change with a mechanism rather than a promise.

### Exam 5 — Landing zones, visualisation, and data sharing (100 items)
- Focus: Cloud Storage versus BigQuery versus Cloud SQL for a stated access pattern, regional, dual-regional, multi-regional and zonal locations, Data Transfer Service, Database Migration Service, Data Fusion, Analytics Hub, VPC Service Controls perimeters, predefined versus custom roles, storage classes and autoclass, expiry and archive rules, Looker Studio versus Looker, encryption in transit and at rest.
- Target skill: justify a landing zone with one sentence about who needs the bytes and when.

### Exam 6 — Integration, machine learning, and lifecycle control (100 items)
- Focus: raw landing plus in-warehouse transformation, streaming ingestion, transfer schedules, remote Gemini models, model evaluation and inference, grouped and time-based split design, Dataform tests before promotion, Composer retries, Dataproc monitoring, model version approval, key rings per environment, customer-managed key revocation, recovery objectives, retention rules.
- Recommended: attempt under a 2-hour timer with no notes, then review every explanation.
- Target skill: hold many constraints at once without collapsing them into one "best practice".

## Item formats and how to rehearse them

| Format | Per exam | How to practise |
|---|---:|---|
| Single-answer | 84 | Decide the constraint first, then eliminate options that solve a different problem |
| Multi-select | 16 | Count the required selections before reading options; reject "true but not asked" statements |
| Case study | 0 | Not part of this exam's published format, so not practised here |
| Sequencing | 0 | Not part of this exam's published format, so not practised here |

## Suggested eight-week schedule

| Week | Work | Deliverable |
|---|---|---|
| 1 | Study domain 1 objectives, take Exam 1 in two halves | Mistake log by local skill |
| 2 | Study domain 2 objectives, take Exam 2 untimed | One diagram: source → landing zone → warehouse |
| 3 | Re-read missed explanations from Exams 1–2, retake both timed | Two timed scores plus error categories |
| 4 | Domain 3, take Exam 3 | A pipeline sheet: tool, trigger, retry, evidence of failure |
| 5 | Domain 4, take Exam 4 | A governance sheet: identity, role, key, retention |
| 6 | Domain 5, take Exam 5, then Exam 6 under a 2-hour clock | Timed score plus pace per item |
| 7 | Retake the weakest exam, re-read its explanations cold | A storage and sharing decision you can defend |
| 8 | Final pass over the 42-skill map | Readiness note, no score conversion |

## Scoring your own attempt

1. Score each item correct or incorrect; there is no partial credit for multi-select.
2. Group misses by local skill ID, not by exam number.
3. Classify each miss: unknown capability, misread constraint, plausible-but-wrong option, or rushed guess.
4. Only the last two categories improve with more practice tests; the first two need documentation study or hands-on work.
5. Re-attempt the same exam after a week before trusting an improvement.

Google does not publish a passing score for the Associate Data Practitioner exam, so no percentage here converts to a pass mark and a practice percentage is not a scaled score.

## Time budget inside a 100-item exam

| Segment | Items | Suggested time (2-hour rehearsal) |
|---|---:|---:|
| First pass, single-answer | 84 | 75 minutes |
| Multi-select | 16 | 25 minutes |
| Review of flagged items | — | 20 minutes |

The live exam delivers 50–60 questions in 2 hours, which is a slower pace per item than this bank requires: 100 items in 2 hours is about 72 seconds each. Use the rehearsal to practise finishing early enough to review, not to model the real appointment minute for minute.
