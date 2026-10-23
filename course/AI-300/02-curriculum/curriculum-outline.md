# Curriculum outline — AI-300 practice course

**Six 100-item mock exams · 600 original questions · 100-minute pace drill or 150-minute review**

This outline turns the bank into a study sequence. Each exam is blueprint-weighted **18 / 29 / 23 / 15 / 15**, so the order below is about scenario complexity and topic reinforcement, not about weighting.

Microsoft does not publish an item count for AI-300, and a 100-item exam is deliberately larger than a comfortable sitting. `6 × 100 = 600` lets each blueprint be drilled twice without repeating a question, so treat any timer as your own convention rather than a model of the live appointment.

## Learning arc

| Phase | Exam | What it stresses | Study goal |
|---|---|---|---|
| Foundation | 1 | Workspaces, infrastructure as code, declarative jobs, pipelines, endpoints | Establish the vocabulary: environment, asset, job, deployment, traffic split |
| Applied operations | 2 | Multi-tenant delivery, approval gates, canary and rollback, grounded retrieval | Connect a configuration decision to the failure it prevents |
| Judgment | 3 | Private networking, evaluation gates, chunking, injection, tracing, cost levers | Decide between similar-sounding controls using the constraint in the stem |
| Accountability | 4 | Least-privilege identity, audit provenance, autoscaling, sampled evaluation | Choose the control that survives an auditor's question |
| Optimization | 5 | Hub capacity, right-sizing, routing, streaming, compression | Cut cost and latency without quietly lowering quality |
| Integration | 6 | Everything, at group scale | Perform under a 100-minute clock with mixed item formats |

## Exam-by-exam study plan

### Exam 1 — Platform, pipelines, and endpoints (100 items)
- Official split: 18 / 29 / 23 / 15 / 15.
- Case studies: Fabrikam Retail AI, Contoso Foundry, Tailwind Logistics, Meridian Bank.
- Focus: workspace and datastore separation, curated environments, components and registries, Bicep modules and parameter files, deployment stacks, `az ml` job YAML, federated identity, GitHub Actions environments, pipelines and sweeps, MLflow tracking, model cards and tags, online and batch endpoints, probes, traffic splits, rollback, autoscale, drift alerts.
- Target skill: name the constraint in the stem before reading the options.

### Exam 2 — Professional services and regulated delivery (100 items)
- Case studies: Northwind MLOps, Harborview Health, Alpine Manufacturing, Woodgrove Insurance.
- Focus: multi-tenant delivery, pinned environments for reproducibility, deployment stacks against drift, approval-gated releases, canary with a retained deployment, grounding over clinical records, document-level access, index refresh, provenance for a seven-year audit.
- Target skill: place the human or policy control where an error becomes an unauthorised deployment or an unsupported answer.

### Exam 3 — Healthcare, manufacturing, utilities, media, financial (100 items)
- Case studies: Solstice Energy, Redwood Manufacturing, Cobalt Retail, Beacon Financial.
- Focus: private endpoints for clinical data, per-environment service principals, evaluation gates on summarization prompts, section-level chunking, hybrid retrieval for identifiers, indirect injection, tracing disputed answers, prompt logging, caching with TTL, routing, provisioned throughput.
- Target skill: choose the measurement or control that actually gates a release.

### Exam 4 — Financial services, insurance, public sector, pharma (100 items)
- Case studies: Granite University, Fairhaven Mutual, Cedar Ridge Health, Northgate Bank.
- Focus: least privilege per environment, model cards and audit rebuilds, month-end autoscaling, groundedness and relevance as separate metrics, retrieval recall before prompt rewrites, continuous evaluation on sampled traffic, federated retrieval that respects a licence, batch inference off the interactive path.
- Target skill: distinguish "supported by the passage" from "answers the question" before choosing a metric.

### Exam 5 — Utilities, retail, manufacturing, higher education (100 items)
- Case studies: Kestrel Group, Atlas Distribution, Brightwater Water, Skyline Media.
- Focus: brand-isolated projects on shared hub capacity, alias-based promotion, right-sizing and routing, streaming first token, prompt compression, fine-tuning to shorten prompts, re-evaluation after a cost trade, provisioned capacity, and a cost sequence that keeps quality measurable.
- Target skill: keep cost, latency, and quality as three separate arguments.

### Exam 6 — Cross-industry capstone (100 items)
- Case studies: Evergreen Pharma, Lakeshore Council, Litware Analytics, Portside Utilities.
- Focus: one platform standard across subsidiaries, aliases for promotion, evaluation sets authored independently of the prompt, honest degradation detection, and the full build-measure-release-observe loop.
- Recommended: attempt under a 100-minute timer with no notes, then review every explanation.
- Target skill: hold many constraints at once without collapsing them into one "best practice".

## Item formats and how to rehearse them

| Format | Per exam | How to practise |
|---|---:|---|
| Single-choice | 76 | Decide the constraint first, then eliminate options that solve a different problem |
| Multi-select | 16 | Count the required selections before reading options; reject "true but not asked" statements |
| Sequencing (exported as multiple-choice) | 8 | Find the step that cannot move — measure before tune, deploy before split, publish before reference — and anchor the rest |
| Case study | 4 × 3 | Read once, write the three or four hard constraints, then answer each item against them |

## Suggested eight-week schedule

| Week | Work | Deliverable |
|---|---|---|
| 1 | Study domain 1 objectives, take Exam 1 in two halves | Mistake log by local skill |
| 2 | Study domain 2 objectives, take Exam 2 untimed | A one-page diagram of one release path, from commit to canary |
| 3 | Re-read missed explanations from Exams 1–2, retake both timed | Two timed scores plus error categories |
| 4 | Domain 3 objectives, take Exam 3 | A grounded-retrieval checklist: curate, chunk, index, bind, evaluate |
| 5 | Domain 4 objectives, take Exam 4 | An evaluation plan naming the metric for each failure mode |
| 6 | Domain 5 objectives, take Exam 5; review cost and latency items | A cost lever table with its quality risk |
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

Microsoft does not publish an AI-300 duration or item count, so a 100-item attempt cannot reuse the live clock even in principle. The pace drill above is a deliberate per-item budget for practice; the 150-minute option is for learning rather than timing. Confirm the current appointment length on the certification page before you book.
