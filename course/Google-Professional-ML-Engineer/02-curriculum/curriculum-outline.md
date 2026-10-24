# Curriculum outline — PMLE practice course

**Six 100-item mock exams · 600 original questions · 2-hour rehearsal or untimed first pass**

This outline turns the bank into a study sequence. Every exam is blueprint-weighted **12 / 16 / 21 / 20 / 18 / 13**, the published weighting rounded to whole items, so the order below is about scenario complexity and topic reinforcement, not about weighting.

Google publishes a **50–60 question range**, a **2-hour** length, and **no case-study component**. A 100-item exam is deliberately larger, so treat the clock as a rehearsal of the published duration rather than a model of the live item count.

## Learning arc

| Phase | Exam | What it stresses | Study goal |
|---|---|---|---|
| Foundation | 1 | BigQuery ML, AutoML, Gemini cost and latency, features, notebooks, experiments, endpoints, drift | Establish the vocabulary: TRANSFORM, remote models, node-hour budgets, Feature Store, experiments, endpoint types |
| Data | 2 | Preprocessing parity, PII, Dataplex, notebook runtimes, experiment hygiene, evaluation metrics | Connect a data-handling choice to the failure it prevents downstream |
| Training | 3 | Model type, product, data layout, containers, troubleshooting, tuning, fine-tuning, accelerators | Read an error message and name the smallest change that fixes it |
| Serving | 4 | Batch, online and streaming inference, packaging, rollout strategy, endpoint access, scaling | Separate latency, throughput, cost, and blast radius into four distinct arguments |
| Automation | 5 | Validation gates, orchestration choice, train-serve consistency, retraining policy, CI/CD/CT | Make every promotion reversible and every trigger defensible |
| Governance | 6 | Model Armor, safety filters, bias, explainability, monitoring, drift types | Distinguish the four drift types and the evidence each one produces |

## Exam-by-exam study plan

### Exam 1 — Low-code AI, data tooling, and the serving baseline (100 items)
- Official split: 12 / 16 / 21 / 20 / 18 / 13.
- Focus: forecasting, clustering and classification in BigQuery ML, TRANSFORM, remote Gemini models, AutoML budgets and export, Model Garden, industry APIs, token cost and latency, preprocessing tool choice, Feature Store, PII handling, notebook environments, experiments and metadata, model and product selection, storage formats, containers, endpoint types, pipeline orchestration, retraining triggers, drift.
- Target skill: name the constraint in the stem before reading the options.

### Exam 2 — Features, notebooks, experiments, and model choice (100 items)
- Focus: streaming and batch preprocessing parity, grouped and time-based splits, Dataplex discovery, online and offline feature reads, Sensitive Data Protection and hashing, Workbench, Colab Enterprise and private-IP runtimes, experiment comparison and seeds, Kubeflow and template pipelines, logistic and ARIMA baselines, AutoML versus custom training, precision-recall and LLM-as-a-judge, batch versus online inference, feature serving, monitoring without fresh labels.
- Target skill: decide where a value must be computed once so two paths cannot disagree.

### Exam 3 — Training at scale, accelerators, and troubleshooting (100 items)
- Focus: model type and product selection, canary, shadow, blue/green and A/B, interpretability by construction, Parquet and TFRecord layout, BigQuery and streaming ingestion, custom and prebuilt containers, out-of-memory and quota failures, framework version mismatch, hyperparameter search with a custom metric and a budget, LoRA versus full fine-tuning, TPU slices and L4 GPUs, data versus model parallelism.
- Target skill: diagnose the failure class first — memory, quota, version, data — then choose the fix.

### Exam 4 — Serving, rollout, endpoints, and latency (100 items)
- Focus: batch, online and streaming inference, request batching, prebuilt containers and prediction routines, Artifact Registry and Model Registry, aliases for rollback, A/B, canary, blue/green and shadow, feature-store reads at prediction time, private, shared and dedicated endpoints, GPU and TPU choices, autoscaling bounds, concurrency and minimum replicas, explanation metadata.
- Target skill: prove a serving change with a measurement rather than an intuition.

### Exam 5 — Pipelines, retraining policy, and CI/CD/CT (100 items)
- Focus: validation steps that stop a bad batch, model gates, locked test sets, Pipelines, Airflow, Ray and Cloud Build, cached steps, offline and online feature reads, train-serve parity, drift, schedule, metric and manual retraining policies, event triggers, continuous training, monitoring controls that keep a retrained model honest.
- Target skill: keep every promotion reversible, and know what "reversible" costs.

### Exam 6 — Secure AI, explainability, and drift monitoring (100 items)
- Focus: prompt injection and Model Armor, safety filters, output schemas, regex redaction, bias slicing, data and model cards, Shapley, sampled Shapley and integrated gradients, monitoring thresholds and alerts, baseline comparison, data drift, concept drift, training-serving skew, attribution drift, generative quality evaluation.
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
| 2 | Study domain 2 objectives, take Exam 2 untimed | One diagram: where features are computed and stored |
| 3 | Re-read missed explanations from Exams 1–2, retake both timed | Two timed scores plus error categories |
| 4 | Domain 3, take Exam 3 | A troubleshooting table: symptom, cause, first fix |
| 5 | Domain 4, take Exam 4 | A serving sheet: batch or online, endpoint type, scaling bounds |
| 6 | Domain 5, take Exam 5, then Exam 6 under a 2-hour clock | Timed score plus pace per item |
| 7 | Retake the weakest exam, re-read its explanations cold | A retraining policy you can defend |
| 8 | Final pass over the 47-skill map | Readiness note, no score conversion |

## Scoring your own attempt

1. Score each item correct or incorrect; there is no partial credit for multi-select.
2. Group misses by local skill ID, not by exam number.
3. Classify each miss: unknown capability, misread constraint, plausible-but-wrong option, or rushed guess.
4. Only the last two categories improve with more practice tests; the first two need documentation study or hands-on work.
5. Re-attempt the same exam after a week before trusting an improvement.

Google does not publish a passing score for the Professional Machine Learning Engineer exam, so no percentage here converts to a pass mark and a practice percentage is not a scaled score.

## Time budget inside a 100-item exam

| Segment | Items | Suggested time (2-hour rehearsal) |
|---|---:|---:|
| First pass, single-answer | 84 | 75 minutes |
| Multi-select | 16 | 25 minutes |
| Review of flagged items | — | 20 minutes |

The live exam delivers 50–60 questions in 2 hours, which is a slower pace per item than this bank requires: 100 items in 2 hours is about 72 seconds each. Use the rehearsal to practise finishing early enough to review, not to model the real appointment minute for minute.
