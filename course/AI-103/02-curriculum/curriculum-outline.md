# Curriculum outline — AI-103 practice course

**Six 100-item mock exams · 600 original questions · 100 minutes pace drill or 150 minutes review**

This outline turns the bank into a study sequence. Each exam is blueprint-weighted **28 / 33 / 13 / 13 / 13**, so the order below is about scenario complexity and topic reinforcement, not about weighting.

A 100-item exam is deliberately longer than the live 40–60 items. `60 × 50 = 300` became `6 × 100 = 600` so each blueprint can be drilled twice without repeating a question; the real 120-minute clock therefore does not map directly to a practice attempt.

## Learning arc

| Phase | Exam | What it stresses | Study goal |
|---|---|---|---|
| Foundation | 1 | Planning, generative app basics, first contact with vision/text/extraction items | Establish vocabulary for models, retrieval, deployment, security, and evaluation |
| Applied build | 2 | Memory, private networking, cost control, groundedness, agent tools | Connect platform controls to concrete application requirements |
| Judgment | 3 | Capacity planning, regression gates, red teaming, evaluation datasets, orchestration | Decide between similar-sounding options using the constraint in the stem |
| Multimodal | 4 | Vision, video, Content Understanding, enrichment, incident triage | Separate generation, editing, extraction, and analysis capabilities |
| Language and speech | 5 | Text analysis, translation, speech, accessibility, multilingual delivery | Choose the right language capability and keep terminology controlled |
| Integration | 6 | Everything, at group scale | Perform under time with mixed item formats |

## Exam-by-exam study plan

### Exam 1 — Planning and generative foundations (100 items)
- Official split: 28 / 33 / 13 / 13 / 13.
- Focus: model and service selection, retrieval and knowledge services, CI/CD and private endpoints, quota and cost, drift and groundedness monitoring, identity, responsible AI.
- Generative: RAG, staged workflows, structured output, project endpoints, SDKs, evaluation, fabrication, tool schemas, system messages, tool calls, manager agents, tuning.
- Multimodal, language, and extraction items are deliberately introductory so the exam is still a full mock.
- Target skill: explain why a retrieved passage is not the same thing as evidence.

### Exam 2 — Healthcare delivery (100 items)
- Scenario spine: ClinDoc (clinical documentation assistant) and BillingBot (claims and statements).
- Focus: conversation memory, prompt caching, private endpoints, managed identity with least privilege, content filters with approval gates, human review of high-risk summaries, groundedness measurement.
- Adds: OpenAPI versus function tools, handoff and manager orchestration, trace-based diagnosis, image editing versus generation, Content Understanding modes, custom speech, glossaries, prebuilt versus custom document models, field confidence.
- Target skill: place a human control where the consequence is irreversible.

### Exam 3 — Financial services and insurance (100 items)
- Scenario spine: FraudDesk (investigation assistant) and LoanDocs (lending documents).
- Focus: provisioned throughput, batch deployment, token analytics, alerts and regression gates, key vault and egress control, red teaming, router and few-shot prompting, golden datasets and A/B comparison, safety evaluation, strict tool schemas.
- Adds: parallel and reflective agents, deletion propagation, hybrid search with security filters, enrichment skillsets, context budgets, custom extraction.
- Target skill: choose the measurement that actually gates a release.

### Exam 4 — Manufacturing and supply chain (100 items)
- Scenario spine: LineSight (line-side inspection) and Fabrikam Plant (contractor portal).
- Focus: drift detection with alerting, provisioned capacity for continuous inference, guardrails and protected-material detection, staged validation before writes.
- Adds: image generation and inpainting, video event analysis, visual question answering and alt text, Content Understanding pro mode, multimodal injection through scanned text, custom speech in noisy environments, compliance summarization with a domain lexicon.
- Target skill: distinguish "describe", "locate", "extract", and "edit" in the vision family.

### Exam 5 — Public sector and education (100 items)
- Scenario spine: CityHelp (resident services) and CampusDesk (student records).
- Focus: data residency, seasonal quota peaks, caching, monitoring and evaluation as release evidence, human oversight of benefits decisions, red teaming, citation and structured output.
- Adds: refusal policy in the system message, governed records lookups, approval and bounded autonomy, handoff, accessibility, multilingual notices, speech translation order, security filters, custom extraction with confidence review.
- Target skill: keep faithfulness, safety, and authorization as three separate concerns.

### Exam 6 — Cross-industry capstone (100 items)
- Scenario spine: GroupAssist (group-wide assistant) and WarrantyDesk (warranty claims).
- Focus: shared standards across subsidiaries, per-subsidiary authorization, private networking, provisioned capacity, evaluation gates, governed tool calls, retrieval budgets, visual safety and watermarking, compliance framing.
- Recommended: attempt under a 120-minute timer with no notes, then review every explanation.
- Target skill: hold many constraints at once without collapsing them into one "best practice".

## Item formats and how to rehearse them

| Format | Per exam | How to practise |
|---|---:|---|
| Single-choice | 38 | Decide the constraint first, then eliminate options that solve a different problem |
| Multi-select | 8 | Count the required selections before reading options; reject "true but not asked" statements |
| Ordering | 4 | Find the step that cannot move (provisioning, authorization, evaluation, transcription) and anchor the rest |
| Case study | 2 × 3 | Read once, write the three or four hard constraints, then answer each item against them |

## Suggested eight-week schedule

| Week | Work | Deliverable |
|---|---|---|
| 1 | Study domain 1 objectives, take Exam 1 in two halves | Mistake log by sub-domain |
| 2 | Study domain 2 objectives, take Exam 2 untimed | Rewrite five missed items as your own scenario |
| 3 | Re-read missed explanations from Exams 1–2, retake both timed | Two timed scores plus error categories |
| 4 | Domain 3 and 4 objectives, take Exam 3 | Separate generation, edition, extraction, and analysis notes |
| 5 | Domain 5 objectives, take Exam 4 | Indexing and extraction pipeline sketch |
| 6 | Speech, translation, and text analysis review, take Exam 5 | Terminology and language capability table |
| 7 | Take Exam 6 timed | Timed score plus pace per item |
| 8 | Retake the weakest exam, review every explanation | Final readiness note, no score conversion |

## Scoring your own attempt

1. Score each item as correct or incorrect; there is no partial credit for multi-select.
2. Group misses by local skill ID, not by exam number.
3. Classify each miss: unknown capability, misread constraint, plausible-but-wrong option, or rushed guess.
4. Only the last two categories improve with more practice tests; the first two need documentation study.
5. Re-attempt the same exam after a week before trusting an improvement.

A practice percentage is not a scaled exam score. Microsoft reports 700/1000 on a scaled scale and does not publish a raw percentage equivalent.

## Time budget inside a 50-item exam

| Segment | Items | Suggested time (pace drill: 100 min) |
|---|---:|---:|
| First pass, single-choice and multi-select | 60 | 55 minutes |
| Ordering items | 8 | 10 minutes |
| Case studies | 12 | 20 minutes |
| Remaining single-choice and review | 20 | 15 minutes |

The real appointment is 120 minutes for 40–60 items, so a 100-item attempt cannot reuse that clock directly. The pace drill above is deliberately tighter than the real per-item allowance; the 150-minute option is for learning rather than timing.
