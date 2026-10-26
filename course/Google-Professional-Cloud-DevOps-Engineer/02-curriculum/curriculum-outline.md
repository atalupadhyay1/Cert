# Curriculum outline — Professional Cloud DevOps Engineer practice course

**Six 100-item mock exams · 600 original questions · a two-hour rehearsal that runs slower than the live paper**

This outline turns the bank into a study sequence. Every exam is blueprint-weighted **20 / 25 / 18 / 25 / 12** — the published weights themselves, which total exactly 100% — so the order below is about scenario complexity and topic reinforcement, not about weighting.

Google publishes a **50–60 question range**, a **two-hour** length, **no prerequisites**, and **no case-study component**. A 100-item exam is deliberately larger, which has one consequence worth stating plainly: **the bank runs slower than the live exam per item.** 100 items in two hours is about **72 seconds per item**; the live 50–60 item paper allows roughly **120–144 seconds** each. Practise here under the two-hour clock and you will be training at a more generous pace than the appointment itself — useful for building explanation habits, not for simulating time pressure.

## Learning arc

| Phase | Exam | What it stresses | Study goal |
|---|---|---|---|
| Foundation | 1 | Hierarchy, Shared VPC, IAM, IaC tooling, Cloud Build and Cloud Deploy, fleets, dev environments | Say where a resource belongs and who may change it before reading options |
| Delivery | 2 | Triggers, artifacts, targets, approvals, release strategies, secrets, supply chain | Decide which control proves the artifact is trustworthy |
| Reliability | 3 | SLIs, SLOs, error budgets, capacity, autoscaling, incident traffic, rollback | Name the objective and the cost of the next nine |
| Observability | 4 | Logs, metrics, traces, alerting, dashboards, diagnosis | Ask which signal answers the question, then pick the source |
| FinOps | 5 | APM, recommenders, observability cost, Spot, commitments, right-sizing | Explain a cost change as a consequence of a design choice |
| Integration | 6 | Mixed design-review scenarios across all five sections | Hold a reliability, cost and delivery constraint at once |

## Exam-by-exam study plan

### Exam 1 — Hierarchy, infrastructure as code, and pipeline foundations (100 items)
- Official split: 20 / 25 / 18 / 25 / 12.
- Focus: organization, folder and project layout including application-centric and environment-centric designs; Shared VPC, peering and Private Service Connect; multi-project log sinks and metrics scopes; IAM roles, custom roles, organization policy constraints and deny policies; service accounts per environment and per workload, impersonation and Workload Identity Federation; data residency; Terraform modules, Infrastructure Manager, Config Connector, the Cloud Foundation Toolkit, kpt, Helm, GitOps and drift plans; scripting automation; Cloud Build with Cloud Deploy and Artifact Registry against Jenkins and Argo CD and Packer; Kustomize overlays, ephemeral projects and shared staging; GKE fleets, release channels and maintenance windows; Cloud Workstations, approved images, and the three Gemini assistants.
- Target skill: for every scenario, decide where the resource belongs in the hierarchy and which control enforces the intent.

### Exam 2 — Delivery pipelines and software supply chain (100 items)
- Focus: triggers on pull requests, branches and tags; Artifact Registry repositories and immutable tags; Cloud Deploy targets for GKE, attached clusters and Cloud Run; approval gates and automatic promotion; deployment audit logs, provenance attestations and supply-chain levels; canary, blue/green, rolling, mesh traffic splitting and feature flags; rollout gates driven by the SLI rather than by CPU; failed steps, idempotent re-runs and rollback; Cloud KMS, Secret Manager, Certificate Manager and Parameter Manager; build-time versus runtime secret injection; Artifact Analysis, critical-finding gates and Binary Authorization; per-environment IAM boundaries.
- Target skill: separate "the artifact is trustworthy" from "the change is safe to expose", then choose the control for each.

### Exam 3 — Reliability engineering in practice (100 items)
- Focus: SLIs and SLOs and SLAs as three different documents; error budgets, burn-rate alerting and release freezes; the opportunity cost of the next nine; service catalogues and retirement plans; capacity planning with quotas, reservations and Dynamic Workload Scheduler; autoscaling on CPU, queue depth and concurrency; draining connections, DNS routing policies and load-balancer failover during incidents; adding capacity in a second region; redeploying the last good build and testing down migrations.
- Target skill: state the objective, the budget, and the acceptable blast radius before choosing a mechanism.

### Exam 4 — Telemetry, alerting, and diagnosis (100 items)
- Focus: the Ops Agent, OpenTelemetry collectors, mesh telemetry, flow logs and Data Access audit logs; log exclusions, sampling, cardinality and ingest measurement; Logging query language and Logs Explorer pivots; BigQuery, Cloud Storage and Pub/Sub sinks with locked retention; redaction of sensitive fields; custom and log-based metrics; managed Prometheus collection; uptime checks; dashboards and attached playbooks; burn-rate against threshold alerting; webhook and email channels; spans, trace waterfalls and trace-to-log correlation; Gemini Cloud Assist for logs, metrics and traces; diagnosis of image pulls, readiness probes, NAT port exhaustion, firewall rules, DNS TTLs and saturation.
- Target skill: choose the telemetry source that answers the question being asked, rather than the one that is easiest to switch on.

### Exam 5 — FinOps and performance tuning (100 items)
- Focus: application performance monitoring by endpoint and against the objective; Active Assist and the cost, reliability and other recommenders; observability cost control through ingest measurement, exclusions and cardinality; Spot VMs for batch and node pools, and why reclaimable capacity cannot hold state; committed-use and sustained-use discounts; network tiers for bulk versus interactive traffic; right-sizing node pools; warm minimums versus scale to zero; scheduled shutdowns for idle environments.
- Target skill: attribute every cost change to a design decision, and every saving to a risk that was accepted.

### Exam 6 — Integrated review across all five sections (100 items)
- Focus: mixed scenarios that pair decisions the way a design review does — the hierarchy choice with the guardrail, the trigger with the supply-chain control, the SLO with the rollout gate, the log route with the retention lock, and Spot capacity with a stateful workload.
- Recommended: attempt under a two-hour timer with no notes, then review every explanation.
- Target skill: keep delivery speed, reliability and cost in the same answer without collapsing one into another.

## Item formats and how to rehearse them

| Format | Per exam | How to practise |
|---|---:|---|
| Single-answer | 84 | Identify the constraint first, then eliminate options that solve a different problem |
| Multi-select | 16 | Count the required selections before reading options; reject "true but not asked" statements |
| Case study | 0 | Not part of this exam's published format, so not practised here |
| Sequencing or drag-and-drop | 0 | Not part of this exam's published format, so not practised here |

## Suggested eight-week schedule

| Week | Work | Deliverable |
|---|---|---|
| 1 | Study section 1 objectives, take Exam 1 untimed | Mistake log by local skill ID |
| 2 | Sections 2 and 3, take Exams 2 and 3 untimed | One table: artifact trust versus change exposure |
| 3 | Re-read missed explanations from Exams 1–3, retake Exam 2 timed | Timed score plus error categories |
| 4 | Section 4, take Exam 4 untimed | A telemetry sheet: question → signal → source |
| 5 | Section 5, take Exam 5 | A cost sheet: change → saving → accepted risk |
| 6 | Take Exam 6 under the two-hour clock | Timed score plus pace per item |
| 7 | Retake the weakest exam, then re-read its explanations cold | One page of the five decisions that settle most questions |
| 8 | Final pass over the 59-skill map | Readiness note, no score conversion |

## Scoring your own attempt

1. Score each item correct or incorrect; there is no partial credit for multi-select.
2. Group misses by local skill ID, not by exam number.
3. Classify each miss: unknown product, misread constraint, plausible-but-wrong option, or rushed guess.
4. Only the last two categories improve with more practice tests; the first two need documentation study or hands-on work.
5. Re-attempt the same exam after a week before trusting an improvement.

Google does not publish a passing score for the Professional Cloud DevOps Engineer exam, so no percentage here converts to a pass mark and a practice percentage is not a scaled score.

## Time budget inside a 100-item exam

| Segment | Items | Suggested time (two-hour clock) |
|---|---:|---:|
| First pass, single-answer | 84 | 80 minutes |
| Multi-select | 16 | 22 minutes |
| Review of flagged items | — | 18 minutes |

The live exam delivers 50–60 questions in two hours, which is 120–144 seconds per item — noticeably more generous than this bank's 72 seconds. A comfortable finish here therefore does **not** prove you would finish the live paper quickly; it proves you can reason steadily. If you want time pressure, shorten the clock deliberately rather than assuming the bank provides it.

## What this course does not cover, on purpose

- **No case studies.** The published format has no case-study component.
- **No console recipes.** Configuration judgement is in scope and is tested as a decision — which control, why, and what it costs — not as a click path. The test suite rejects console-instruction phrasing.
- **No labs or interactive items.** They cannot exist in a CSV and are not part of the published format.
- **No passing score.** Google does not publish one, so none is stated.
