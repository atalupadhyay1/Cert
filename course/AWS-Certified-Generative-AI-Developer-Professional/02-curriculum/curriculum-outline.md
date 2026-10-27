# Curriculum outline — AWS Certified Generative AI Developer - Professional (AIP-C01) practice course

**Six 75-item mock exams · 450 original questions · a 180-minute rehearsal at published pace**

This outline turns the bank into a study sequence. Every exam is blueprint-weighted **23 / 20 / 15 / 9 / 8** against the published **31 / 26 / 20 / 12 / 11** percent, so the order below is about decision difficulty and topic reinforcement, not about weighting.

AWS publishes **75 questions in 180 minutes**, of which **65 are scored and 10 are unscored**, with **no case-study component**. Because each set is also 75 items, the clock gives the same **~144 seconds per item** as a scored sitting, which makes a timed run a real pacing rehearsal.

## Learning arc

| Phase | Exam | Scenario emphasis | Study goal |
|---|---|---|---|
| Get retrieval right | 1 | Retail and customer service | Separate a retrieval failure from a prompt failure |
| Version and constrain | 2 | Financial services and insurance | Make every answer traceable to a source and a version |
| Protect the data | 3 | Healthcare and life sciences | Let the privacy constraint pick the control point |
| Ship prompts safely | 4 | Media, publishing, and marketing | Treat prompts as released artefacts with tests |
| Run it on real hardware | 5 | Manufacturing and field operations | Reason about capacity, latency and approval gates |
| Operate it for teams | 6 | Software delivery and internal platform | Answer with the operational control, not the product name |

## Exam-by-exam study plan

### Exam 1 — Retail and customer service scenarios (75 items)
- Official split: 23 model integration, 20 implementation, 15 safety, 9 efficiency, 8 testing.
- Focus: proving value with an on-demand proof of concept; a shared gateway and versioned prompts; model evaluation jobs; right-sizing; cross-Region inference; paging or falling back; pinning a version; Glue Data Quality and entity extraction; OCR for warranty scans; JSON bodies and dialog formatting; DynamoDB vectors; metadata filters and S3-event sync; hierarchical chunking; hybrid search and reranking; parent-child retrieval; history-aware query rewriting; system prompts and JSON-schema output; agent memory in DynamoDB; AgentCore; Strands; loop limits; tool-argument validation and timeouts; provisioned throughput; rate limits and queues; EventBridge and SQS; task roles; gateways; pipelines with evaluation; server-sent events; backoff and circuit breakers; API Gateway and Amplify; Q Developer; X-Ray; content filters; denied topics; grounding citations; injection defence; masking; private endpoints; CloudTrail and lineage; model cards and escalation; drift alerts; context pruning and summarisation; semantic and exact caching; streaming and parallel calls; invocation logs; token metrics; tagging; faithfulness; A/B; regression suites; retrieval and agent metrics; truncation checks.
- Target skill: turn a symptom ("the answer is wrong") into the retrieval, prompt, model or infrastructure decision that caused it.

### Exam 2 — Financial services and insurance scenarios (75 items)
- Focus: two business lines on one platform; managed knowledge bases; human rubrics; JumpStart for in-VPC hosting; evaluation jobs; tiered routing; cross-Region and fallback; custom model import; data quality and reformatting; Transcribe for call archives; pgvector beside relational rows; metadata filters and scheduled rebuilds; semantic chunking; reranking with thresholds; hybrid search; query decomposition; structured prompt sections and approval; durable agent memory; summarisation; Agent Squad; state machines with loop limits; tool schemas and scoped roles; provisioned throughput with batch; EventBridge and queues; Cognito; gateways; canary with evaluation; asynchronous processing; backoff and circuit breakers; API Gateway and AppSync; Q Developer; Logs Insights; content filters, denied topics and reasoning checks; grounding citations and text-to-SQL; injection filters and adversarial suites; masking with PII detection; private endpoints and WAF; CloudTrail, lineage and invocation logs; model cards and confidence scores; segment fairness metrics; pruning and response caps; exact and semantic caching; tiered routing; precomputation and capacity planning; Grafana and canaries; cost anomaly detection; token budgets; human rubrics; judges with agreement checks; shadow traffic; golden sets, gates and diffs; tool accuracy and completion; reasoning traces.
- Target skill: state which error is expensive before choosing a metric, a guardrail or a threshold.

### Exam 3 — Healthcare and life sciences scenarios (75 items)
- Focus: one assistant across website, phone and tablet; gateway with tiered routing; human rubrics; evaluation jobs; right-sizing; config-driven model switches; cross-Region and fallback; pinned versions; data quality and entity extraction; OCR for scanned reports; dialog formatting and JSON bodies; OpenSearch for a 40-million-chunk index; per-tenant namespaces; event-driven re-indexing; structural chunking; expansion with reranking; hybrid search; history-aware rewriting; system prompts and schema output; AgentCore memory; summarisation; Agent Squad; loop limits with state machines; tool schemas and timeouts; provisioned capacity plus on-demand overflow; EventBridge and queues; task roles; gateways; canary with regression suites; WebSockets; backoff and circuit breakers; API Gateway and App Runner; Q Developer; Logs Insights; content filters, denied topics and PII filters; citations and grounding checks; injection filters and sanitisation; masking with Comprehend and Macie; private endpoints and subnets; CloudTrail and lineage; model cards and escalation; drift alerts; pruning and retrieval caps; semantic and exact caching; streaming and parallel calls; invocation logs and token metrics; tagging; faithfulness; ROUGE and BERTScore; canary releases; prompt regression suites and synthetic journeys; recall; agent accuracy and completion; truncation.
- Target skill: when a single wrong answer is expensive, name the control that prevents it rather than the one that detects it later.

### Exam 4 — Media, publishing, and marketing scenarios (75 items)
- Focus: gateway with shared guardrails; evaluation plus cost-quality ratio; human rubrics; right-sizing and evaluation jobs; config-driven switching; cross-Region and fallback; distillation as lifecycle management; data quality and entity extraction; multimodal embeddings; dialog formatting and JSON bodies; OpenSearch at 80 million chunks; rights metadata filters; incremental indexing; semantic chunking; hybrid search with thresholds; reranking; decomposition; system prompts and few-shot examples; DynamoDB memory; summarisation; Strands; loop and timeout limits; tool schemas and tool scopes; provisioned capacity with batch; EventBridge and SNS; task roles; gateways; pipelines with regression suites; server-sent events; backoff and circuit breakers; API Gateway and CloudFront; Q Developer; X-Ray; content filters and denied topics; citations and text-to-SQL; injection filters and adversarial suites; masking and PII filters; private endpoints and WAF; CloudTrail with lineage; model cards and confidence; drift alerts; pruning and response caps; prompt caching with tiered routing; latency models, streaming and precomputation; canaries and anomaly detection; Savings Plans; relevance; judges with rubrics; A/B tests; golden sets, gates and diffs; precision; tool accuracy and completion; context overflow.
- Target skill: separate retrieval quality, prompt quality and infrastructure cost, and answer each with the control that owns it.

### Exam 5 — Manufacturing and field operations scenarios (75 items)
- Focus: Outposts with a shared gateway; managed knowledge bases; human rubrics; evaluation jobs; right-sizing; config-driven switches; cross-Region and fallback; LoRA adapters; data quality and entity extraction; Transcribe for voice notes; JSON bodies and dialog formatting; Neptune for asset relationships; metadata filters and scheduled rebuilds; fixed-size chunking; hybrid search with reranking; query expansion for trade slang; history-aware rewriting; chain-of-thought and Prompt Flows; DynamoDB memory and summarisation; specialist agents; approval gates with loop limits; timeouts and Lambda tools; on-demand pricing with SageMaker endpoints; ECS-hosted MCP servers; DataSync; task roles; gateways; CDK with pipelines; asynchronous jobs; backoff and circuit breakers; API Gateway and Fargate; Q Developer; X-Ray; content filters, denied topics and reasoning checks; citations and grounding checks; injection filters and sanitisation; masking with PII detection; private endpoints and subnets; log retention and lineage; model cards and escalation; segment fairness; pruning and retrieval caps; exact caching, tiered routing and prompt caching; precomputation with capacity planning; latency alarms and anomaly detection; tagging; faithfulness; judges with agreement checks; shadow traffic; golden sets and gates; tool accuracy and completion; reasoning traces.
- Target skill: explain the cost and failure consequence of each infrastructure choice, not only its name.

### Exam 6 — Software delivery and internal platform scenarios (75 items)
- Focus: a shared gateway with versioned prompts; evaluation plus cost-quality; human rubrics; evaluation jobs; right-sizing; config-driven switching; cross-Region and fallback; pinned versions; data quality and reformatting; OCR for screenshots; dialog formatting and JSON bodies; S3 as the authoritative corpus; per-team namespaces; re-embedding on model change; Titan embeddings; hybrid search with reranking; score thresholds; decomposition; schema output and low temperature; AgentCore memory and summarisation; ensemble aggregation with approval gates; tool schemas and timeouts; provisioned capacity with batch; EventBridge and queues; task roles; gateways with pipelines; server-sent events; backoff and circuit breakers; AppSync and Lambda@Edge; Q Developer; Logs Insights; content filters, denied topics and PII filters; citations and grounding checks; injection filters and adversarial suites; masking with Macie and Comprehend; private endpoints and subnets; CloudTrail and lineage; model cards and confidence; drift alerts; pruning and response caps; prompt caching with tiered routing; parallel calls with latency models and streaming; invocation logs with token metrics and alarms; Savings Plans; relevance; BERTScore with faithfulness; canary releases; golden sets; gates with per-template suites; precision; tool accuracy and completion; truncation.
- Target skill: answer with the smallest correct operational change, then say why the tempting alternative fails the constraint.

## Item formats and how to rehearse them

| Format | Per exam | How to practise |
|---|---:|---|
| Multiple choice | 60 | Decide before reading the options, then check which option matches your decision |
| Multiple response | 15 | Read the stated count first; treat each option as its own true/false question |

There are no sequencing, drag-and-drop or case-study items, because the published format has none.

## Suggested six-week schedule

| Week | Work | Time |
|---:|---|---|
| 1 | Read the landing page and curriculum; take Exam 1 untimed | ~3.5 h |
| 2 | Review every Exam 1 explanation; re-read the five domain maps; take Exam 2 untimed | ~4 h |
| 3 | Take Exam 3 untimed; start a one-page error log by domain | ~3.5 h |
| 4 | Take Exam 4 with a 200-minute clock; fix the two weakest domains | ~4 h |
| 5 | Take Exam 5 with a 190-minute clock; revise evaluation metrics and cost vocabulary | ~4 h |
| 6 | Take Exam 6 under the full 180 minutes; review the error log only | ~3.5 h |

## Scoring your own attempt

- Score one point per item; a multiple-response item scores a point only when every correct option is selected and nothing else is.
- Record the score per domain, not only overall: 70% overall with 50% in domain 5 is a different problem from an even 70%.
- AWS publishes a **minimum passing score of 750 on a scaled 100–1000 range**, applied to the 65 scored items with compensatory scoring and no per-domain pass mark. That 750 is a scaled score, not a percentage of 75, so no practice percentage here is an estimate of it.
- Treat any domain below 70% of its items as a study target, and treat a domain above 85% as something to re-verify once, not to skip.

## Time budget inside a 75-item exam

| Phase | Minutes | Notes |
|---|---:|---|
| Instructions and settling | 5 | Read the item-count and multiple-response rules once |
| First pass | 135 | ~108 seconds per item, answering everything; flag rather than stall |
| Second pass on flags | 25 | ~4 minutes for each of six flagged items |
| Final review | 15 | Check that multiple-response items have exactly the stated count |

At 75 items in 180 minutes the average allowance is **144 seconds**. A first pass at 108 seconds leaves a real review margin, which is how a scored sitting rewards discipline: unanswered items are marked incorrect and there is no penalty for guessing.

## What this course does not cover, on purpose

The guide lists **model development and training, advanced ML techniques, and data engineering and feature engineering** as out of scope. No item asks you to train a model, tune hyperparameters for a classical algorithm, or build a feature pipeline. There are also **no case studies**, because the published format has none, and no lab or console walkthroughs, because the exam does not test them.
