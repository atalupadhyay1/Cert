# Curriculum outline — Professional Cloud Developer practice course

**Six 100-item mock exams · 600 original questions · a two-hour rehearsal that runs slower than the live paper**

This outline turns the bank into a study sequence. Every exam is blueprint-weighted **32 / 23 / 24 / 21** — the published weights themselves, which total exactly 100% — so the order below is about decision difficulty and topic reinforcement, not about weighting.

Google publishes a **50–60 question range**, a **two-hour** length, **no prerequisites**, and **no case-study component**. A 100-item exam is deliberately larger, which has one consequence worth stating plainly: **the bank runs slower than the live exam per item.** 100 items in two hours is about **72 seconds per item**; the live 50–60 item paper allows roughly **120–144 seconds** each. Practise here under the two-hour clock and you will be training at a more generous pace than the appointment itself — useful for building explanation habits, not for simulating time pressure.

## Learning arc

| Phase | Exam | What it stresses | Study goal |
|---|---|---|---|
| Foundation | 1 | Compute choice, API contracts, security, datastores, failure domains | State the constraint before naming a product |
| Build | 2 | Local emulation, developer tooling, pipelines, provenance, tests | Decide what evidence a release needs |
| Deploy | 3 | Cloud Run and GKE settings, probes, autoscaling, exposure | Predict a symptom from a setting |
| Integrate | 4 | Connectivity, messaging, Cloud API calls, identity, observability | Choose the call pattern that survives failure |
| Mixed | 5 | Constraints arriving out of topic order | Hold two constraints in one answer |
| Review | 6 | All four sections in design-review form | Decide out of topic order, under time |

## Exam-by-exam study plan

### Exam 1 — Compute choice, APIs, and secure design (100 items)
- Official split: 32 / 23 / 24 / 21.
- Focus: choosing among Cloud Run, GKE, Compute Engine, Cloud Functions and App Engine from workload shape; containerising stateful code; zone, region and multi-region failure domains; load balancing and affinity; Memorystore and invalidation; REST, gRPC and gRPC-web; rate limits, quotas and versioning; Pub/Sub, Eventarc, Workflows, Cloud Tasks and Cloud Scheduler; right-sizing and commitments; traffic splitting, canary and flags; a service mesh for policy; lifecycle rules and retention locks; secret versions, rotation and customer-managed keys; Identity Platform, IAP and Application Default Credentials; least privilege and private connectivity; datastore selection by consistency and access pattern; signed URLs; analytics handoff.
- Target skill: for every scenario, write the requirement as a constraint — availability, latency, residency, budget — before naming a service.

### Exam 2 — Development environments, builds, and tests (100 items)
- Focus: emulators instead of a live project, Cloud Workstations and Cloud Shell, Gemini Cloud Assist, AI coding assistants and MCP servers as reviewed tools, Cloud Build steps and triggers, Artifact Registry versus the legacy registry, image scanning, Binary Authorization, supply-chain levels and provenance, unit tests, flaky-test quarantine, release gates, integration runs, load tests, profilers and debuggers.
- Target skill: separate "the pipeline is convenient" from "the pipeline produces evidence a reviewer accepts".

### Exam 3 — Cloud Run and GKE deployment configuration (100 items)
- Focus: source versus image deployment, concurrency, minimum and maximum instances, CPU outside the request, startup boost, ingress, unauthenticated access, request versus instance billing, jobs, Eventarc triggers, push and pull delivery, invoker grants, deferred and scheduled work, gateway versus full API platform, rolling updates and unavailable bounds, Autopilot, Workload Identity, node and pod autoscaling, startup, readiness and liveness probes, disruption budgets, backend health checks.
- Target skill: read a symptom, name the setting behind it, and state what the setting protects.

### Exam 4 — Datastore connectivity, messaging, APIs, and observability (100 items)
- Focus: Auth Proxy, language connectors, private endpoints and pools, topics and subscriptions, dead-letter handling and idempotency, BigQuery subscriptions and exports, backoff, pagination, field masks, batching and caching for Cloud APIs, service accounts, Workload Identity Federation and ADC, structured logs, custom and log-based metrics, alert policies, SLO burn, error grouping and trace correlation.
- Target skill: choose the call or delivery pattern that stays correct when something downstream is slow or repeats.

### Exam 5 — Mixed application delivery scenarios (100 items)
- Focus: constraints interleaved the way a normal week delivers them — a latency target that forces a cache decision, a compliance rule that turns a connectivity question into a private-endpoint question, a flaky suite that blocks a release a canary would have judged.
- Target skill: satisfy two constraints at once instead of optimising the one that was named first.

### Exam 6 — Integrated review across all four sections (100 items)
- Focus: design-review questions that pair constraints — residency with least privilege, availability with cost, provenance with delivery speed, observability with the evidence an auditor expects.
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
| 2 | Sections 2 and 3, take Exams 2 and 3 untimed | One table: symptom → setting → what it protects |
| 3 | Re-read missed explanations from Exams 1–3, retake Exam 2 timed | Timed score plus error categories |
| 4 | Section 4, take Exam 4 | A call-pattern sheet: failure → pattern → cost |
| 5 | Take Exam 5 | A constraint sheet: two requirements → one decision |
| 6 | Take Exam 6 under the two-hour clock | Timed score plus pace per item |
| 7 | Retake the weakest exam, then re-read its explanations cold | One page of the decisions that settle most questions |
| 8 | Final pass over the 39-study-area map | Readiness note, no score conversion |

## Scoring your own attempt

1. Score each item correct or incorrect; there is no partial credit for multi-select.
2. Group misses by local study area, not by exam number.
3. Classify each miss: unknown product, misread constraint, plausible-but-wrong option, or rushed guess.
4. Only the last two categories improve with more practice tests; the first two need documentation study or hands-on work.
5. Re-attempt the same exam after a week before trusting an improvement.

Google does not publish a passing score for the Professional Cloud Developer exam, so no percentage here converts to a pass mark and a practice percentage is not a scaled score.

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
