# Curriculum outline — PCA practice course

**Six 100-item mock exams · 600 original questions · 2-hour rehearsal or untimed first pass**

This outline turns the bank into a study sequence. Every exam is blueprint-weighted **25 / 18 / 17 / 15 / 12 / 13**, which is the published weighting rounded to whole items, so the order below is about scenario complexity and topic reinforcement, not about weighting.

Google publishes a **50–60 question range** and a **2-hour** length, plus **two case studies worth 20–30% of the score**. A 100-item exam is deliberately larger, so treat the clock as a rehearsal of the published duration rather than a model of the live item count.

## Learning arc

| Phase | Exam | What it stresses | Study goal |
|---|---|---|---|
| Foundation | 1 | Requirements, availability, networks, storage, compute, analytics, AI, migration | Establish the vocabulary: Shared VPC, Private Service Connect, CMK, Autoclass, Autopilot, Model Garden |
| Platform | 2 | Hybrid connectivity, lifecycle, patching, GKE operations, serverless, Terraform, ML workflows | Connect a provisioning choice to the operational burden it creates |
| Security | 3 | IAM, hierarchy, encryption, perimeters, zero trust, supply chain, AI safety, audit | Decide where a control must sit so the failure it prevents cannot happen elsewhere |
| Optimisation | 4 | Cost, performance, continuity, attribution, paved road | Separate cost, latency, and correctness into three distinct arguments |
| Delivery | 5 | Release strategy, APIs, migration waves, tooling, launch readiness | Sequence a change so every step is reversible |
| Capstone | 6 | SLOs, observability, late data, cross-industry constraints | Hold many constraints at once without collapsing them into one "best practice" |

## Exam-by-exam study plan

### Exam 1 — Design foundations and workload placement (100 items)
- Official split: 25 / 18 / 17 / 15 / 12 / 13.
- Case studies: Helios Broadcasting, Cobalt Retail Group, Meridian Health Systems, Vantage Logistics.
- Focus: business and non-functional requirements, KPI baselines and total cost, availability and failover, Shared VPC, peering, Network Connectivity Center, Private Service Connect, storage class choice, compute placement across GKE, Cloud Run, Batch and Compute Engine, analytics and AI solution design, and migration assessment.
- Target skill: name the constraint in the stem before reading the options.

### Exam 2 — Provisioning, networking, and platform engineering (100 items)
- Case studies: Sable Financial, Quarry Manufacturing, Lumen Analytics, Kestrel Airlines.
- Focus: HA VPN and Interconnect, Cloud NAT and Private Google Access, bucket retention, lifecycle and Transfer Service, partitioning and clustering, patch management, Spot versus commitments, custom machine types, node auto-provisioning, private nodes, serverless connectors, Terraform and Cloud Build, Agent Platform Pipelines.
- Target skill: decide where a control must sit so it applies to future resources, not just today's.

### Exam 3 — Security, compliance, and AI safety (100 items)
- Case studies: Ironvale Bank, Beacon Genomics, Summit Public Sector, Fable Media Group.
- Focus: custom roles, conditions and deny policies, folders and organization policy, Cloud HSM, CMEK and rotation, VPC Service Controls and dry run, Identity-Aware Proxy, context-aware access, Binary Authorization and provenance, Model Armor, Sensitive Data Protection, audit logging, locked buckets.
- Target skill: choose the control that makes a failure impossible rather than merely detectable.

### Exam 4 — Optimization, cost, and continuity (100 items)
- Case studies: Orchid Commerce, Vertex Insurance, Harborline Shipping, Pinecrest University.
- Focus: BI Engine and slots, partition and cluster design, Autoclass, dual-region buckets, Spot and commitments, custom shapes, cluster autoscaling, Terraform, DR patterns from pilot light to active-active, Recommender, billing export, service catalog provisioning.
- Target skill: prove a change with a measurement rather than an intuition.

### Exam 5 — Implementation, delivery, and migration (100 items)
- Case studies: Zephyr Payments, Atlas Retail Cloud, Nimbus Games, Cedar Health Cloud.
- Focus: canary and blue/green releases, feature flags, pinned digests, Apigee and API Gateway, migration waves with Migration Center, Database Migration Service and Migrate to Containers, Terraform and Cloud Build, emulators, client libraries, quota planning, launch-day observability.
- Target skill: keep every step reversible, and know what "reversible" costs.

### Exam 6 — Reliability, operations, and cross-industry capstone (100 items)
- Case studies: Everline Media, Granite Utilities, Solstice Travel, Union Foundry.
- Focus: SLOs and error budgets, Ops Agent and Profiler, traces and error grouping, windowing and late data, audit evidence, acquisition-scale migration, feature parity between training and serving, and a capstone across two countries with different residency rules.
- Recommended: attempt under a 2-hour timer with no notes, then review every explanation.
- Target skill: hold many constraints at once without collapsing them into one "best practice".

## Item formats and how to rehearse them

| Format | Per exam | How to practise |
|---|---:|---|
| Single-answer | 76 | Decide the constraint first, then eliminate options that solve a different problem |
| Multi-select | 16 | Count the required selections before reading options; reject "true but not asked" statements |
| Sequencing (exported as multiple-choice) | 8 | Find the step that cannot move — inventory before waves, keys before encryption, plan before apply — and anchor the rest |
| Case study | 4 × 5 | Read once, write the three or four hard constraints, then answer each item against them |

## Suggested eight-week schedule

| Week | Work | Deliverable |
|---|---|---|
| 1 | Study domain 1 objectives, take Exam 1 in two halves | Mistake log by local skill |
| 2 | Study domain 2 objectives, take Exam 2 untimed | One diagram: network, project, and identity layout |
| 3 | Re-read missed explanations from Exams 1–2, retake both timed | Two timed scores plus error categories |
| 4 | Domain 3, take Exam 3 | A control map: identity, encryption, perimeter, audit |
| 5 | Domains 4–5, take Exams 4 and 5 | A cost model and a release checklist |
| 6 | Take Exam 6 under a 2-hour clock | Timed score plus pace per item |
| 7 | Re-read the case studies cold, retake the weakest exam | Case-constraint notes for all 24 scenarios |
| 8 | Final pass over the 42-skill map | Readiness note, no score conversion |

## Scoring your own attempt

1. Score each item correct or incorrect; there is no partial credit for multi-select.
2. Group misses by local skill ID, not by exam number.
3. Classify each miss: unknown capability, misread constraint, plausible-but-wrong option, or rushed guess.
4. Only the last two categories improve with more practice tests; the first two need documentation study or hands-on work.
5. Re-attempt the same exam after a week before trusting an improvement.

Google does not publish a passing score for the Professional Cloud Architect exam, so no percentage here converts to a pass mark.

## Time budget inside a 100-item exam

| Segment | Items | Suggested time (2-hour rehearsal) |
|---|---:|---:|
| First pass, single-answer and multi-select | 76 | 70 minutes |
| Sequencing items (multiple-choice) | 8 | 10 minutes |
| Case studies | 20 | 25 minutes |
| Review of flagged items | 4 | 15 minutes |

The live exam gives you two case studies on a split screen; this bank gives you four per exam so every blueprint is drilled twice. Budget more time per case-study item than the pattern above suggests until the scenarios feel familiar.
