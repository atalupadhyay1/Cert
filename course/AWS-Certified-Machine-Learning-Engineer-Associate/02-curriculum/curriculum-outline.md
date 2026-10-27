# Curriculum outline — AWS Certified Machine Learning Engineer – Associate (MLA-C02) practice course

**Six 65-item mock exams · 390 original questions · a 130-minute rehearsal at published pace**

This outline turns the bank into a study sequence. Every exam is blueprint-weighted **18 / 16 / 16 / 15** against the published **28 / 24 / 24 / 24** percent, so the order below is about decision difficulty and topic reinforcement, not about weighting.

AWS publishes **65 questions in 130 minutes**, of which **50 are scored and 15 are unscored**, with **no case-study component**. While MLA-C02 is in beta it is delivered as 85 questions in 170 minutes with the extra items unscored and no pass/fail result; these sets follow the published 65-question form. Because each set is also 65 items, the clock gives the same **~120 seconds per item** as a scored sitting, which makes a timed run a real pacing rehearsal.

## Learning arc

| Phase | Exam | Scenario emphasis | Study goal |
|---|---|---|---|
| Get the data right | 1 | Retail and e-commerce | Choose the store from the access pattern before choosing a model |
| Protect the features | 2 | Financial services and insurance | Keep training and inference on the same feature definition |
| Handle sensitive data | 3 | Healthcare and life sciences | Let the constraint drive the pipeline, not the other way round |
| Keep the fleet fed | 4 | Manufacturing and IoT | Reason about throughput, checkpoints and provisioned capacity |
| Ground the answers | 5 | Media, search, and RAG assistants | Separate retrieval quality from model quality |
| Run it for real | 6 | Logistics and support agents | Answer with the operational control, not the product name |

## Exam-by-exam study plan

### Exam 1 — Retail and e-commerce scenarios (65 items)
- Official split: 18 data preparation, 16 model and FM development, 16 deployment, 15 operating.
- Focus: key-value versus object versus file versus vector storage; shared file systems for multi-node training; stream versus delivery-stream ingestion; Parquet, JSON and partitioning; Glue and EMR transforms; the Feature Store; scaling, encoding and splitting; embedding models and vector indexes; chunking strategies; data-quality rules and profiling; Ground Truth with automated labelling; bias metrics; imputation, clipping and class rebalancing.
- Target skill: turn an access pattern ("one row, thousands of times a minute") into a storage choice before touching the model.

### Exam 2 — Financial services and insurance scenarios (65 items)
- Focus: Kafka versus Kinesis; object lock and lifecycle policies; point-in-time feature history; scaler and encoder choices; pgvector beside relational rows; hybrid retrieval; tokenisation against the target model; pair validation; class weights versus synthetic sampling; anomaly algorithms; DeepAR forecasting; Bedrock model selection; LoRA versus full fine-tuning; continued pre-training with replay; RAG instead of retraining; managed AI services; script mode; tuning objectives; overfitting responses; precision-recall and confusion-matrix reporting; LLM-as-a-judge; Bedrock evaluation jobs.
- Target skill: state which error is expensive before choosing a metric, a sampler or a threshold.

### Exam 3 — Healthcare and life sciences scenarios (65 items)
- Focus: storage cost per terabyte; shared file systems; archive classes; multi-source normalisation; online versus offline feature reads; median imputation; scaling with stratification; S3-backed vector indexes; multimodal embeddings; redaction and metadata; quality rules with stored profiles; modality balance; outlier clipping; interpretable versus ensemble models; distillation; parent-child chunking; custom containers; early stopping; model parallelism with checkpoints; metric traps on rare conditions; human review of a judge; run tracking; serverless inference; knowledge-base sync; GPU-driven scaling; private subnets; build-and-test pipelines; model registry lineage; shadow deployment; approval gates; state-machine orchestration.
- Target skill: when a single wrong decision is expensive, name the control that prevents it rather than the one that detects it later.

### Exam 4 — Manufacturing and IoT scenarios (65 items)
- Focus: ordered telemetry with multiple consumers; immutable evidence; intelligent tiering; columnar and partitioned layouts; Glue versus EMR; Data Wrangler exploration; feature groups; binning, one-hot and shuffling; small-corpus in-process indexes; embedding fine-tuning with reranking; fixed versus semantic chunks; schema contracts; automated labelling; bias quantification; class weights with imputation; nearest-neighbour similarity; boosting versus linear models; prompt-first before training; hybrid retrieval; managed vision services; script mode; random search; managed tuning with early stopping; data and model parallelism with warm pools; precision-recall operating points; semantic similarity; baselines; real-time and asynchronous inference; multi-model endpoints; provisioned throughput and custom model import; break-even comparison; agent deployment; HyperPod; step scaling; target tracking on GPU; interface endpoints; pipelines with a managed repository; CodeDeploy rollback; registry; why a single switch is wrong; schedules; data and quality drift; attribution drift; alarms and dashboards; agent tracing; batch instead of idle endpoints; right-sizing with Savings Plans; embedding caches and token caps; execution roles scoped to a prefix; cross-account roles; open ingress; Secrets Manager; Guardrails; CloudTrail.
- Target skill: explain the cost and failure consequence of each infrastructure choice, not only its name.

### Exam 5 — Media, search, and RAG assistant scenarios (65 items)
- Focus: metadata lookup beside similarity search; Lustre for frame throughput; Firehose delivery; lifecycle expiry; Parquet with date prefixes; Glue with the catalog; DataBrew; online feature reads; one-hot encoding; scaling with stratification; pgvector; embeddings with hybrid retrieval; tokeniser-driven splitting; parent-child chunks; stored profiles; Ground Truth; group reweighting; deduplication; DeepAR; Random Cut Forest; long-context model choice; embedding models; continued pre-training; LoRA with replay; chunk metadata; Transcribe; JumpStart; tuning objective; managed tuning beside a manual grid; regularisation with more data; RMSE; AUC with a precision-recall cut-off; ROUGE; Bedrock evaluation; real-time inference; batch with multi-model; multi-container endpoints; provisioned throughput; on-demand with the recommender; knowledge-base sync; ECR; GPU scaling; target tracking with warm capacity; interface endpoints; build and pipeline services; quality gates; prompt management; canary; shadow with blue/green; SageMaker pipelines; quality and data drift; bias drift; Logs Insights; alarms; GenAI observability; Cost Explorer; batch and right-sizing; context trimming and routing; VPC-only bucket with prefix scoping; Bedrock API keys; security groups; customer managed keys; Guardrails; Config.
- Target skill: separate retrieval failure from model failure, and separate both from infrastructure failure.

### Exam 6 — Logistics and support agent scenarios (65 items)
- Focus: quota diagnosis; single-row lookups; shard capacity; archive classes; Parquet with depot prefixes; original-record preservation; EMR for a long replay; Glue with the catalog; point-in-time features; scaling and log transforms with stratification; managed vector indexes with hybrid retrieval; semantic chunking; automated labelling; modality balance; class weights; DeepAR and linear models; small-model economics; distillation; LoRA with replay; parent-child chunks; Textract; script mode; early stopping; objective metric with Bayesian search; checkpoints with warm pools; confusion matrix; AUC with RMSE; BERTScore; pinned versions; asynchronous inference; batch beside real-time; multi-container; custom model import; provisioned throughput with break-even comparison; agent state; EKS; scale-to-zero; GPU scaling with provisioned concurrency; private subnets; CodeConnections with CodeBuild; CodePipeline; model registry; arguing against an all-at-once switch; canary with shadow; Step Functions; attribution drift; quality and bias drift; X-Ray; dashboards; agent observability; Savings Plans; right-sizing with batch; embedding caches and routing; execution roles with prefix scoping; cross-account roles; VPC-only buckets; Secrets Manager; denied topics; Inspector.
- Target skill: answer with the smallest correct operational change, then say why the tempting alternative fails the constraint.

## Item formats and how to rehearse them

| Format | Per exam | How to practise |
|---|---:|---|
| Multiple choice | 50 | Decide before reading the options, then check which option matches your decision |
| Multiple response | 15 | Read the stated count first; treat each option as its own true/false question |

There are no sequencing, drag-and-drop or case-study items, because the published format has none.

## Suggested six-week schedule

| Week | Work | Time |
|---:|---|---|
| 1 | Read the landing page and curriculum; take Exam 1 untimed | ~3 h |
| 2 | Review every Exam 1 explanation; re-read the four domain maps; take Exam 2 untimed | ~3.5 h |
| 3 | Take Exam 3 untimed; start a one-page error log by domain | ~3 h |
| 4 | Take Exam 4 with a 145-minute clock; fix the two weakest domains | ~3.5 h |
| 5 | Take Exam 5 with a 135-minute clock; revise evaluation metrics and cost vocabulary | ~3.5 h |
| 6 | Take Exam 6 under the full 130 minutes; review the error log only | ~3 h |

## Scoring your own attempt

- Score one point per item; a multiple-response item scores a point only when every correct option is selected and nothing else is.
- Record the score per domain, not only overall: a 65% overall with 40% in data preparation is a different problem from an even 65%.
- AWS publishes a **minimum passing score of 720 on a scaled 100–1000 range**, applied to the 50 scored items with compensatory scoring and no per-domain pass mark. That 720 is a scaled score, not a percentage of 65, so no practice percentage here is an estimate of it.
- Treat any domain below 70% of its items as a study target, and treat a domain above 85% as something to re-verify once, not to skip.

## Time budget inside a 65-item exam

| Phase | Minutes | Notes |
|---|---:|---|
| Instructions and settling | 4 | Read the item-count and multiple-response rules once |
| First pass | 98 | ~90 seconds per item, answering everything; flag rather than stall |
| Second pass on flags | 18 | ~3 minutes for each of six flagged items |
| Final review | 10 | Check that multiple-response items have exactly the stated count |

At 65 items in 130 minutes the average allowance is **120 seconds**. A first pass at 90 seconds leaves a real review margin, which is how a scored sitting rewards discipline: unanswered items are marked incorrect and there is no penalty for guessing.

## What this course does not cover, on purpose

The guide lists **designing and architecting full end-to-end AI and ML solutions, setting ML strategy and best practice, integrating a wide array of new services and tools, and working deeply in two or more ML domains** as out of scope. No item asks you to architect a whole platform, write a strategy document, or compare tools this exam does not name. There are also **no case studies**, because the published format has none, and no lab or console walkthroughs, because the exam does not test them.
