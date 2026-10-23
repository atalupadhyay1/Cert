# Curriculum outline — AI-200 practice course

**Six 100-item mock exams · 600 original questions · 100 minutes pace drill or 150 minutes review**

Every exam is blueprint-weighted **24 / 30 / 24 / 22**. The sequence below is about scenario complexity and reinforcement, not weighting.

A 100-item exam is deliberately longer than the live 40–60 items. `6 × 50 = 300` became `6 × 100 = 600` so each blueprint can be drilled twice without repeating a question; the real 120-minute clock therefore does not map directly to a practice attempt.

## Learning arc

| Phase | Exam | What it stresses | Study goal |
|---|---|---|---|
| Foundation | 1 | Registry, App Service, Container Apps, AKS basics; Cosmos DB and pgvector fundamentals | Establish vocabulary for artifacts, replicas, partitions, and retrieval |
| Applied build | 2 | Warm capacity, private DNS, DiskANN, filters before selection, Durable Functions | Connect platform controls to concrete requirements |
| Judgment | 3 | Geo-replication, vector policy dimensions, index choice, idempotency, sampling | Decide between similar options using the deciding constraint |
| Reliability | 4 | Manifest reproducibility, RU charge, storage throughput, dead-lettering, trace joins | Diagnose rather than guess |
| Access and observation | 5 | Slots, cool-down, post-filtering pitfalls, purge protection, collector routing | Separate configuration, identity, and telemetry concerns |
| Integration | 6 | Everything, at global scale | Perform under time with mixed item formats |

## Exam-by-exam study plan

### Exam 1 — Retail recommendation platform (100 items)
- Focus: versioned images and ACR Tasks, App Service settings, Container Apps ingress and revisions, KEDA queue scaling, AKS manifests and probes, container connectivity.
- Data: Cosmos DB partition reads, indexing policy, session consistency, vector search, change feed; pgvector index and pooling; Redis caching and vectors.
- Messaging: Service Bus sessions, topics and filters, delivery limits, idempotency; Event Grid filters and retries; Functions triggers, bindings, plans.
- Operations: Key Vault references, App Configuration, OpenTelemetry, KQL time binning and joins.
- Target skill: explain why a correct answer can still be the expensive one.

### Exam 2 — Healthcare document intake (100 items)
- Focus: immutable artifacts, slot swaps, warm minimum replicas, private name resolution, readiness probes.
- Data: DiskANN at scale, change feed leases, IVFFlat, vacuum, work memory, filters before selection, external poolers, TTL and invalidation.
- Messaging: prefetch, topics, dead-lettering, system topics, Durable Functions with bindings, premium plans, managed identities.
- Operations: data-plane vault access, configuration refresh, time-bounded KQL, sampling.
- Target skill: place the control where the consequence happens.

### Exam 3 — Payments and fraud scoring (100 items)
- Focus: geo-replication, scaler identity, workload identity federation, environment networking, in-pod connectivity tests.
- Data: vector policy dimensions, distance function, transactional batches, HNSW versus IVFFlat, EXPLAIN ANALYZE, prepared statements, storage throughput, invalidation.
- Messaging: sessions, duplicate detection, scheduled messages, identity-based event delivery, durable dispute workflows.
- Operations: rotation, labels, Key Vault references, tail sampling, platform metric alerts, materialized aggregations.
- Target skill: choose the measurement that gates a release.

### Exam 4 — Factory quality inspection (100 items)
- Focus: retention policy, slots, scale-to-zero workers, manifest reproducibility, pod-level diagnosis.
- Data: RU charge per write, session scope, change feed, typed filter columns, HNSW, compute sizing, pooling, TTL.
- Messaging: queues with recovery, sessions per machine, topics, dead-lettering, Event Grid subject filters and retries, durable orchestration.
- Operations: vault access, refresh, trace connectivity across messaging, KQL aggregation.
- Target skill: separate describe, detect, and store in the extraction pipeline.

### Exam 5 — Citizen document services (100 items)
- Focus: App Service patterns, canaries, cool-down, private DNS, log and event correlation.
- Data: single-partition reads, indexing policy, eventual consistency, change feed, pgvector, IVFFlat, post-filtering pitfall, pooler, invalidation, session state.
- Messaging: peek-lock recovery, fan-out, idempotency, dead-lettering, system topics, consumption plans, deployment slots.
- Operations: purge protection, rotation, labels, Key Vault references, collector routing, request-to-dependency joins.
- Target skill: keep correctness, cost, and scope as three separate questions.

### Exam 6 — Global retail capstone (100 items)
- Focus: multi-region registries, per-workload identity, diagnostic routing, canary release, warm capacity.
- Data: DiskANN, per-request consistency relaxation, metadata-scoped retrieval, pooler sizing, TTL, Redis vectors.
- Messaging: fan-out with filters, idempotent consumers, custom events, durable workflows, premium hosting.
- Operations: rotation, labels, refresh, tail sampling, materialized aggregation, private endpoints, least privilege.
- Recommended: attempt under a 120-minute timer with no notes, then review every explanation.
- Target skill: hold many constraints at once without collapsing them into one "best practice".

## Item formats and how to rehearse them

| Format | Per exam | How to practise |
|---|---:|---|
| Single-choice | 38 | Decide the constraint first, then eliminate options that solve a different problem |
| Multi-select | 8 | Count the required selections before reading options; reject "true but not asked" statements |
| Ordering | 4 | Anchor on the step that cannot move: build before push, apply before ready, receive before complete, store before rotate |
| Case study | 2 × 3 | Read once, write the three or four hard constraints, then answer each item against them |

## Suggested eight-week schedule

| Week | Work | Deliverable |
|---|---|---|
| 1 | Container hosting objectives; Exam 1 in two halves | Mistake log by sub-domain |
| 2 | Cosmos DB objectives; Exam 2 untimed | Partition, RU, and consistency notes |
| 3 | PostgreSQL and pgvector objectives; retake Exams 1–2 timed | Two timed scores plus error categories |
| 4 | Redis and messaging objectives; Exam 3 | Filter-before versus filter-after examples |
| 5 | Functions and deployment objectives; Exam 4 | Trigger, binding, and plan comparison table |
| 6 | Key Vault, App Configuration, OpenTelemetry, KQL; Exam 5 | One KQL query per failure signature you met |
| 7 | Take Exam 6 timed | Timed score plus pace per item |
| 8 | Retake the weakest exam and review every explanation | Final readiness note, no score conversion |

## Scoring your own attempt

1. Score each item as correct or incorrect; multi-select has no partial credit.
2. Group misses by local skill ID, not by exam number.
3. Classify each miss: unknown service behaviour, misread constraint, plausible-but-wrong option, or rushed guess.
4. Only the last two categories improve with more practice exams; the first two need documentation study and hands-on work.
5. Re-attempt the same exam after a week before trusting an improvement.

A practice percentage is not a scaled exam score. Microsoft reports 700/1000 on a scaled scale and does not publish a raw percentage equivalent.

## Time budget inside a 100-item exam

| Segment | Items | Suggested time (pace drill: 100 min) |
|---|---:|---:|
| First pass, single-choice and multi-select | 60 | 55 minutes |
| Ordering items | 8 | 10 minutes |
| Case studies | 12 | 20 minutes |
| Remaining single-choice and review | 20 | 15 minutes |

The real appointment is 120 minutes for 40–60 items, so a 100-item attempt cannot reuse that clock directly. The pace drill above is deliberately tighter than the real per-item allowance; 150 minutes is the learning option rather than a timing rehearsal.
