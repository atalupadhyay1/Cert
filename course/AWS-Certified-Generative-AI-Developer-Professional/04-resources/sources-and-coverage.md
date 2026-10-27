# Sources and coverage — AWS Certified Generative AI Developer - Professional (AIP-C01)

Every factual claim about the exam in this course is traceable to two AWS pages, both read in **October 2026**. Nothing here is drawn from question-sharing sites, forums, or recalled exam content.

## Primary sources

| Source | What it establishes |
|---|---|
| AWS Certified Generative AI Developer - Professional certification page — <https://aws.amazon.com/certification/certified-generative-ai-developer-professional/> | 180-minute appointment, 300 USD fee, 75 questions, question types, delivery through Pearson VUE or online proctoring, the four offered languages, the recommended experience, related credentials, and the suggested predecessor certifications |
| AIP-C01 exam guide — <https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01.html> | The five content domains and their weights (31 / 26 / 20 / 12 / 11 percent), the 65 scored and 10 unscored split, multiple choice and multiple response formats, compensatory scoring on a 100–1000 scale with a minimum passing score of 750, the out-of-scope job tasks, and the tasks and skills behind the study map (domains 1–5 pages) |

Two further pages of the same guide were read for vocabulary: the in-scope service list (`aip-01-in-scope-services.html`) and the technologies and concepts list (`ai-professional-01-technologies-concepts.html`). The service list is what the product names in this course are checked against; anything outside it is avoided as a correct answer.

## Verified exam facts

| Fact | Value used in this course |
|---|---|
| Appointment length | 180 minutes |
| Fee | 300 USD |
| Questions | 75, of which 65 are scored and 10 are unscored; AWS does not identify the unscored items |
| Item types | Multiple choice (one correct answer, three distractors) and multiple response (two or more correct answers from five or more options) |
| Split between item types | **Not published by AWS** — the 60 / 15 mix here is an authoring choice |
| Delivery | Pearson VUE test centre or online proctoring |
| Languages | English, Japanese, Korean and Simplified Chinese |
| Scoring | Compensatory, 100–1000 scale, minimum passing score 750 |
| Recommended experience | Two or more years building production-grade applications on AWS or with open-source technologies, general AI/ML or data engineering experience, and one year of hands-on generative AI implementation |
| Validity | Three years |
| Case studies | None in the published format |
| Out of scope | Model development and training, advanced ML techniques, data engineering and feature engineering |

## Domain weights and the per-exam allocation

The published weights total exactly 100 percent. Applied to 75 items they give 23.25 / 19.5 / 15 / 9 / 8.25 items. Largest-remainder rounding gives the surplus item to Domain 2, whose exact share is the half item, so the per-exam counts are **23 / 20 / 15 / 9 / 8**. Every count is within 0.5 items of its published weight, and the allocation is asserted in the tests, so a change to any published weight fails the build rather than being absorbed silently.

## Coverage mapping

Local study-map identifiers are this course's own numbering, not AWS objective numbers: AWS publishes task statements and skills inside each domain page rather than as numbered objectives. Every skill is exercised in every set.

| Local skill | Official domain | Items per exam | Bank total |
|---|---|---:|---:|
| **1. Foundation Model Integration, Data Management, and Compliance** | **31%** | **23** | **138** |
| 1.1 GenAI Solution Architecture | | 2 | 12 |
| 1.2 Proof-of-Concept Validation | | 1 | 6 |
| 1.3 Foundation Model Selection and Benchmarking | | 2 | 12 |
| 1.4 Model Routing and Provider Abstraction | | 1 | 6 |
| 1.5 Resilience and Cross-Region Inference | | 2 | 12 |
| 1.6 Customisation Lifecycle and Rollback | | 1 | 6 |
| 1.7 Data Validation for Model Inputs | | 2 | 12 |
| 1.8 Multimodal Ingestion and Processing | | 1 | 6 |
| 1.9 Request Formatting and Enrichment | | 2 | 12 |
| 1.10 Vector Store Architecture | | 1 | 6 |
| 1.11 Metadata Frameworks and Index Maintenance | | 2 | 12 |
| 1.12 Chunking and Embedding Strategy | | 1 | 6 |
| 1.13 Hybrid Retrieval and Reranking | | 2 | 12 |
| 1.14 Query Transformation and Handling | | 1 | 6 |
| 1.15 Prompt Engineering and Governance | | 2 | 12 |
| **2. Implementation and Integration** | **26%** | **20** | **120** |
| 2.1 Agent Memory and State | | 2 | 12 |
| 2.2 Agent Orchestration Patterns | | 2 | 12 |
| 2.3 Tool Reliability and Safeguards | | 2 | 12 |
| 2.4 Foundation Model Deployment and Capacity | | 2 | 12 |
| 2.5 Enterprise Integration Patterns | | 2 | 12 |
| 2.6 Identity for Model Access | | 1 | 6 |
| 2.7 CI/CD and GenAI Gateway | | 2 | 12 |
| 2.8 Streaming and Asynchronous APIs | | 1 | 6 |
| 2.9 API Resilience and Backoff | | 2 | 12 |
| 2.10 Application Integration and Low Code | | 2 | 12 |
| 2.11 Developer Productivity Tooling | | 1 | 6 |
| 2.12 Integration Troubleshooting | | 1 | 6 |
| **3. AI Safety, Security, and Governance** | **20%** | **15** | **90** |
| 3.1 Content Safety Controls | | 2 | 12 |
| 3.2 Grounding and Hallucination Reduction | | 2 | 12 |
| 3.3 Prompt Injection Defence | | 2 | 12 |
| 3.4 Privacy and PII Protection | | 2 | 12 |
| 3.5 Network and Data Isolation | | 2 | 12 |
| 3.6 Governance, Lineage, and Audit | | 2 | 12 |
| 3.7 Responsible AI and Transparency | | 2 | 12 |
| 3.8 Fairness and Compliance Monitoring | | 1 | 6 |
| **4. Operational Efficiency and Optimization for GenAI Applications** | **12%** | **9** | **54** |
| 4.1 Token Cost Efficiency | | 2 | 12 |
| 4.2 Model Tiering and Caching | | 2 | 12 |
| 4.3 Throughput and Latency Optimisation | | 2 | 12 |
| 4.4 GenAI Observability | | 2 | 12 |
| 4.5 Cost Attribution and Governance | | 1 | 6 |
| **5. Testing, Validation, and Troubleshooting** | **11%** | **8** | **48** |
| 5.1 GenAI Evaluation Metrics | | 2 | 12 |
| 5.2 Model Comparison and Traffic Testing | | 1 | 6 |
| 5.3 Regression Testing and Quality Gates | | 2 | 12 |
| 5.4 Retrieval and Agent Evaluation | | 2 | 12 |
| 5.5 GenAI Troubleshooting | | 1 | 6 |
| | **Total** | **75** | **450** |

## What is deliberately not covered

- **Case studies.** The published format has none.
- **Sequencing, drag-and-drop and interactive item types.** Not part of the published format, and not expressible in a CSV.
- **Lab tasks and console walkthroughs.** The items test the decision, not the click path, and nothing here needs an AWS account.
- **Model training and advanced ML techniques.** The guide places both out of scope.
- **Data and feature engineering.** Also out of scope; the bank stays on the application side of the model.
- **Passing-score prediction.** The published 750 is a scaled score; no practice percentage in this course is converted into it.

## Source discipline

- The AWS pages above are the only exam-fact sources. Where AWS does not publish something — the item-type split above all — this course says so instead of estimating.
- Service behaviour is described from AWS's own service documentation and the AIP-C01 in-scope service list, not from third-party summaries.
- No examtopics, exam-collection, braindump or forum content was read, copied, paraphrased or used as a topic checklist. The bank is original work.
- Product names are checked against the current AWS service names at the time of writing. AWS renames services, so re-check names before publishing.
- No vendor endorsement is claimed or implied, and no result is guaranteed.
