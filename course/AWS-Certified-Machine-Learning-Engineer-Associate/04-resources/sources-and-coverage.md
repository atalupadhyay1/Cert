# Sources and coverage — AWS Certified Machine Learning Engineer – Associate (MLA-C02)

Every factual claim about the exam in this course is traceable to two AWS pages, both read in **October 2026**. Nothing here is drawn from question-sharing sites, forums, or recalled exam content.

## Primary sources

| Source | What it establishes |
|---|---|
| AWS Certified Machine Learning Engineer – Associate certification page — <https://aws.amazon.com/certification/certified-machine-learning-engineer-associate/> | 130-minute appointment, 150 USD fee, 65 questions, question types, delivery through Pearson VUE or online proctoring, the beta of the updated exam (85 questions, 170 minutes, 75 USD, English only, extra items unscored, no pass/fail), the MLA-C01 to MLA-C02 transition dates, candidate experience, three-year validity, recertification, and the Machine Learning – Specialty as the recommended next certification |
| MLA-C02 exam guide — <https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02.html> | The four content domains and their weights (28 / 24 / 24 / 24 percent), the 50 scored and 15 unscored split, multiple choice and multiple response formats, compensatory scoring on a 100–1000 scale with a minimum passing score of 720, the out-of-scope job tasks, and the tasks and skills behind the study map (domains 1–4 pages) |

The exam guide comparison page (<https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/mla-02-comparison.html>) was also read: it records that Domain 2 moved from 26 to 24 percent while Domains 3 and 4 each moved to 24 percent, and it lists the generative-AI additions (foundation-model selection, RAG patterns, vector databases, prompt management, agentic workflows, guardrails) that MLA-C01 did not carry.

## Verified exam facts

| Fact | Value used in this course |
|---|---|
| Appointment length | 130 minutes (published form); 170 minutes for the beta |
| Fee | 150 USD; 75 USD for the beta |
| Questions | 65, of which 50 are scored and 15 are unscored; AWS does not identify the unscored items. The beta adds 20 unscored items for 85 in total |
| Item types | Multiple choice (one correct answer, three distractors) and multiple response (two or more correct answers from five or more options) |
| Split between item types | **Not published by AWS** — the 50 / 15 mix here is an authoring choice |
| Delivery | Pearson VUE test centre or online proctoring; the beta is English only |
| Scoring | Compensatory, 100–1000 scale, minimum passing score 720; beta sittings do not carry a pass/fail result |
| Recommended experience | At least one year using SageMaker AI, Amazon Bedrock and other ML engineering services, plus a year in a related role |
| Validity | Three years |
| Case studies | None in the published format |
| Out of scope | Designing end-to-end AI/ML solutions, ML strategy and best practice, wide new-tool integration, depth in two or more ML domains |

## Domain weights and the per-exam allocation

The published weights total exactly 100 percent. Applied to 65 items they give 18.2 / 15.6 / 15.6 / 15.6 items. Largest-remainder rounding gives 18 / 16 / 16 / 16, which is 66 items and one more than the paper, so the spare item is removed from Domain 4 and the per-exam counts are **18 / 16 / 16 / 15**. Every count is within 0.6 items of its published weight, and the allocation is asserted in the tests, so a change to any published weight fails the build rather than being absorbed silently.

## Coverage mapping

Local study-map identifiers are this course's own numbering, not AWS objective numbers: AWS publishes task statements and skills inside each domain page rather than as numbered objectives. Every skill is exercised in every set.

| Local skill | Official domain | Items per exam | Bank total |
|---|---|---:|---:|
| **1. Data Preparation for ML and AI** | **28%** | **18** | **108** |
| 1.1 Ingestion Sources and Storage Choice | | 2 | 12 |
| 1.2 Streaming Ingestion | | 1 | 6 |
| 1.3 Storage Class and Retention | | 1 | 6 |
| 1.4 Data Formats and Partitioning | | 2 | 12 |
| 1.5 Merge and Transform Tooling | | 2 | 12 |
| 1.6 Feature Store | | 1 | 6 |
| 1.7 Feature Engineering and Scaling | | 2 | 12 |
| 1.8 Vector Stores and Embeddings | | 2 | 12 |
| 1.9 Text Pre-processing and Chunking | | 1 | 6 |
| 1.10 Data Quality Validation | | 1 | 6 |
| 1.11 Labelling and Annotation | | 1 | 6 |
| 1.12 Bias Detection and Mitigation | | 1 | 6 |
| 1.13 Cleaning and Class Imbalance | | 1 | 6 |
| **2. ML Model and Foundation Model (FM) Development** | **24%** | **16** | **96** |
| 2.1 Model and Algorithm Selection | | 2 | 12 |
| 2.2 Foundation Model Selection | | 2 | 12 |
| 2.3 Fine-tuning and Customisation | | 2 | 12 |
| 2.4 RAG Architecture Patterns | | 1 | 6 |
| 2.5 Managed AI Services | | 1 | 6 |
| 2.6 Built-in Algorithms and Script Mode | | 1 | 6 |
| 2.7 Hyperparameter Tuning | | 2 | 12 |
| 2.8 Training Efficiency and Regularisation | | 1 | 6 |
| 2.9 Classic Model Evaluation | | 2 | 12 |
| 2.10 GenAI and NLP Evaluation | | 1 | 6 |
| 2.11 Experiment Tracking and Baselines | | 1 | 6 |
| **3. Deployment and Orchestration of ML and AI Workflows** | **24%** | **16** | **96** |
| 3.1 Inference Strategy | | 2 | 12 |
| 3.2 Endpoint Architecture | | 1 | 6 |
| 3.3 Foundation Model Deployment | | 2 | 12 |
| 3.4 Agents and Retrieval Runtime | | 1 | 6 |
| 3.5 Containers and Compute Provisioning | | 1 | 6 |
| 3.6 Autoscaling and Concurrency | | 2 | 12 |
| 3.7 VPC Networking for Endpoints | | 1 | 6 |
| 3.8 CI/CD Pipelines | | 2 | 12 |
| 3.9 Model Registry and Versioning | | 1 | 6 |
| 3.10 Deployment Strategy and Rollback | | 2 | 12 |
| 3.11 Orchestration and Retraining | | 1 | 6 |
| **4. Operating, Monitoring, and Securing ML and AI Solutions** | **24%** | **15** | **90** |
| 4.1 Drift and Model Monitoring | | 2 | 12 |
| 4.2 Metrics and Dashboards | | 2 | 12 |
| 4.3 GenAI Observability | | 1 | 6 |
| 4.4 Cost Optimisation and Purchasing | | 2 | 12 |
| 4.5 Inference Cost and Token Usage | | 2 | 12 |
| 4.6 IAM and Credentials | | 2 | 12 |
| 4.7 Network Isolation | | 1 | 6 |
| 4.8 Encryption and Secrets | | 1 | 6 |
| 4.9 Guardrails and Responsible AI | | 1 | 6 |
| 4.10 Audit and Vulnerability Scanning | | 1 | 6 |
| | **Total** | **65** | **390** |

## What is deliberately not covered

- **Case studies.** The published format has none.
- **Sequencing, drag-and-drop and interactive item types.** Not part of the published format, and not expressible in a CSV.
- **Lab tasks and console walkthroughs.** The items test the decision, not the click path, and nothing here needs an AWS account.
- **End-to-end solution architecture and ML strategy.** The guide places both out of scope.
- **Wide tool-integration and multi-domain depth.** Also out of scope; the bank stays inside the services the guide names.
- **Passing-score prediction.** The published 720 is a scaled score; no practice percentage in this course is converted into it, and the beta does not report pass or fail at all.

## Source discipline

- The two AWS pages above are the only exam-fact sources. Where AWS does not publish something — the item-type split above all — this course says so instead of estimating.
- Service behaviour is described from AWS's own service documentation and the MLA-C02 in-scope service list, not from third-party summaries.
- No examtopics, exam-collection, braindump or forum content was read, copied, paraphrased or used as a topic checklist. The bank is original work.
- Product names are checked against the current AWS service names at the time of writing. AWS renames services, and the guide names SageMaker AI and Amazon Bedrock specifically, so re-check names before publishing.
- No vendor endorsement is claimed or implied, and no result is guaranteed.
