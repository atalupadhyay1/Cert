# Official sources and coverage notes

Reviewed October 2026. All facts below were checked against the pages listed; product names, preview status, quotas, and prices change, so re-check before publishing or scheduling.

## Primary references

| Purpose | URL |
|---|---|
| AI-300 study guide (skills measured as of October 15, 2026) | https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-300 |
| Machine Learning Operations Engineer Associate certification page | https://learn.microsoft.com/en-us/credentials/certifications/operationalizing-machine-learning-and-generative-ai-solutions/ |
| Azure Machine Learning workspace concepts | https://learn.microsoft.com/en-us/azure/machine-learning/concept-workspace |
| Model management and deployment | https://learn.microsoft.com/en-us/azure/machine-learning/concept-model-management-and-deployment |
| Azure AI Foundry architecture | https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/architecture |
| Evaluation approach for generative AI | https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/evaluation-approach-gen-ai |
| Provisioned throughput | https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/provisioned-throughput |
| Azure AI Search | https://learn.microsoft.com/en-us/azure/search/ |
| MLflow tracking in Azure Machine Learning | https://learn.microsoft.com/en-us/azure/machine-learning/how-to-track-experiments-mlflow |
| GitHub Actions with OpenID Connect | https://learn.microsoft.com/en-us/azure/developer/github/connect-from-azure-openid-connect |
| Exam sandbox | https://aka.ms/examdemo |

## Verified exam facts

| Fact | Value |
|---|---|
| Domains and weights | 1) Design and implement an MLOps infrastructure 15–20%; 2) Implement machine learning model lifecycle and operations 25–30%; 3) Design and implement a GenAIOps infrastructure 20–25%; 4) Implement generative AI quality assurance and observability 10–15%; 5) Optimize generative AI systems and model performance 10–15% |
| Passing score | 700 / 1000 scaled |
| Delivery | Proctored |
| Prerequisites | None stated; the audience operates ML and generative AI workloads on Azure |
| Audience skill statement | Python, Azure Machine Learning, Azure AI Foundry, GitHub Actions, Bicep, and the Azure CLI |
| Study aids | Microsoft publishes an exam sandbox and a separate practice assessment in AI Skills Navigator |
| Study guide baseline | Skills measured as of October 15, 2026 |
| Item count | Not published by Microsoft |
| Duration | Not published on the study guide; confirm on the certification page |
| Language | English only, per the certification page |
| Renewal | Annual free renewal assessment, per the certification page |

Third-party sources report a 120-minute appointment, a $165 USD regional price, and a 40–60 item range. **These are reported, not Microsoft-published on the study guide**, so the package does not build any claim on them and does not present a practice exam as matching them. Confirm on the certification page before publishing or scheduling.

Not claimed anywhere in this package: that the practice exams contain the live item count, that they reproduce drag-and-drop or lab formats, that a practice percentage maps to 700/1000, or that completing the course earns the credential.

## Domain coverage and package weights

| Domain | Official range | Per exam | Percent | Package total |
|---|---:|---:|---:|---:|
| 1. Design and implement an MLOps infrastructure | 15–20% | 18 | 18% | 108 |
| 2. Implement machine learning model lifecycle and operations | 25–30% | 29 | 29% | 174 |
| 3. Design and implement a GenAIOps infrastructure | 20–25% | 23 | 23% | 138 |
| 4. Implement generative AI quality assurance and observability | 10–15% | 15 | 15% | 90 |
| 5. Optimize generative AI systems and model performance | 10–15% | 15 | 15% | 90 |

Because all six exams share the same allocation, every exam sits inside all five published ranges and the aggregate is exactly 18 / 29 / 23 / 15 / 15. A 100-item exam is deliberately large: the volume covers every sub-objective and lets the blueprint be drilled twice without repeating a question.

## Coverage against the published sub-objectives

The study guide's skill bullets were read directly and mapped into 36 local study areas. The table records practice emphasis across all 600 items; counts describe this bank, not official weighting.

| Local ID | Study area | Domain | Items | Official bullets it supports |
|---|---|---|---:|---|
| 1.1 | Workspace, compute, and datastore provisioning | 1 | 15 | Design workspaces, compute, and data access for ML workloads |
| 1.2 | Data assets, environments, and component reuse | 1 | 16 | Manage data assets, environments, and reusable components |
| 1.3 | Infrastructure as code with Bicep | 1 | 25 | Provision and maintain ML infrastructure declaratively |
| 1.4 | Azure CLI and declarative job automation | 1 | 11 | Automate jobs and deployments with the CLI and declarative definitions |
| 1.5 | GitHub Actions CI/CD and workload identity federation | 1 | 19 | Build CI/CD for ML with secret-free authentication |
| 1.6 | Model registry and environment promotion | 1 | 12 | Register, version, and promote models and environments |
| 1.7 | Network isolation, secrets, and pipeline identity | 1 | 10 | Apply network isolation, secret management, and least privilege |
| 2.1 | Training pipeline authoring and orchestration | 2 | 19 | Author pipelines and orchestrate multi-step training |
| 2.2 | Job configuration, compute targets, and sweeps | 2 | 24 | Configure jobs, compute targets, and hyperparameter sweeps |
| 2.3 | Experiment tracking with MLflow | 2 | 22 | Track experiments, parameters, metrics, and artifacts |
| 2.4 | Model registration, versioning, and metadata | 2 | 24 | Register models with versions, tags, and documentation |
| 2.5 | Managed online endpoint deployment | 2 | 23 | Deploy and configure managed online endpoints |
| 2.6 | Batch endpoints and controlled traffic rollout | 2 | 27 | Run batch scoring and roll out versions with controlled traffic |
| 2.7 | Autoscaling, health probes, and rollback | 2 | 13 | Scale, probe, and roll back a deployment |
| 2.8 | Data and model drift monitoring | 2 | 22 | Monitor data and model drift and act on it |
| 3.1 | Foundry hub, project, and shared capacity | 3 | 19 | Design hub and project structure and shared capacity |
| 3.2 | Model catalog selection and deployment capacity | 3 | 14 | Select models and choose deployment capacity and filtering |
| 3.3 | Prompt flow authoring and DAG composition | 3 | 14 | Author flows, variants, and batch runs |
| 3.4 | Flow connections, secrets, and runtime identity | 3 | 13 | Configure connections, secrets, and runtime identity |
| 3.5 | Retrieval-augmented grounding with Azure AI Search | 3 | 27 | Ground generative responses in indexed content |
| 3.6 | Chunking, embeddings, and index refresh | 3 | 22 | Chunk, embed, and refresh an index |
| 3.7 | Prompt and flow versioning with evaluation gates | 3 | 19 | Version prompts and flows behind evaluation gates |
| 3.8 | Agent orchestration and tool binding | 3 | 10 | Orchestrate agents, state, and tool scopes |
| 4.1 | Evaluation dataset and ground-truth design | 4 | 17 | Design evaluation datasets and ground truth |
| 4.2 | Groundedness and relevance evaluation | 4 | 22 | Evaluate groundedness, relevance, and retrieval quality |
| 4.3 | Coherence, fluency, and similarity metrics | 4 | 6 | Apply coherence, fluency, and similarity metrics |
| 4.4 | Safety, jailbreak, and content filter evaluation | 4 | 18 | Evaluate safety, jailbreak resistance, and content filters |
| 4.5 | Tracing, logging, and Application Insights observability | 4 | 15 | Trace, log, and instrument generative applications |
| 4.6 | Online feedback loops and continuous evaluation | 4 | 12 | Collect feedback and evaluate continuously in production |
| 5.1 | Token cost, caching, and throughput planning | 5 | 19 | Measure and control token cost; plan throughput |
| 5.2 | Model routing, distillation, and right-sizing | 5 | 18 | Route, right-size, and distill models |
| 5.3 | Latency budgets and streaming design | 5 | 13 | Design for latency budgets and streaming |
| 5.4 | Retrieval tuning for relevance and cost | 5 | 10 | Tune retrieval depth and ranking |
| 5.5 | Prompt compression and context discipline | 5 | 9 | Compress prompts and control context |
| 5.6 | Fine-tuning and distillation for quality | 5 | 7 | Fine-tune and distill to improve quality or shorten prompts |
| 5.7 | Batch inference and provisioned capacity optimization | 5 | 14 | Move bulk work to batch; optimize provisioned capacity |

Numeric IDs are local study aids. Microsoft names objectives without this numbering.

## Item-type fidelity boundary

| Real-exam format | Included here | How |
|---|---|---|
| Single-answer scenario item | Yes | `multiple-choice` with four options and one key (76 per exam) |
| Multi-select | Yes | `multi-select` with five options, two keys, and a stated selection count (16 per exam) |
| Drag-and-drop / sequencing | Partially | Four candidate sequences as multiple-choice options (8 per exam) |
| Case studies | Yes | Four per exam, three scored items each, shared scenario |
| Configuration reading | Yes | Bicep, `az ml` job YAML, GitHub Actions, MLflow, prompt-flow, traffic splits, evaluation settings |
| Hot-area | No | Requires image hotspots; cannot be scored in CSV |
| Live labs | No | Requires a provisioned subscription environment |
| Adaptive problem-solution sets | No | Changes item order by prior answer; not representable as a fixed set |
| Live item count | Not published | The package does not assert one |

## Editorial standards used while authoring

- Every item states one deciding constraint and one defensible best answer.
- Distractors are real capabilities that solve a different problem, not nonsense: a stored secret where federation is required, a fixed count where autoscale is required, fine-tuning where an index is required.
- Configuration items are written so the judgement is visible: what the change makes possible, what it prevents, and what it costs. No item turns on remembering a flag name.
- Multi-select items name the required count so the learner cannot under- or over-select by accident.
- Sequencing items anchor on a step that cannot move: define before deploy, deploy an endpoint before attaching a deployment, publish an asset before referencing it, measure before optimizing.
- Case-study items restate their specific constraint so they still read correctly outside the shared preamble.
- Terminology follows current naming (Azure Machine Learning, Azure AI Foundry, Azure AI Search, managed online endpoint, batch endpoint, deployment alias, prompt flow, workload identity federation), with older names acknowledged where they still appear in the product.
- No quota, pricing figure, regional availability, or preview status is asserted as permanent; items test the reasoning behind the choice.
- No Microsoft sample, sandbox, or recall-derived item text is used. The sandbox link was consulted only to understand item formats.

## Known limitations

- Automated checks verify structure, allocation, source parity, explanations, and reproducibility; they do not certify factual accuracy or difficulty.
- Counts reflect authoring emphasis, not official sub-objective weighting, which Microsoft does not publish per bullet.
- Preview and generative AI capabilities move quickly; an item about a preview feature can age faster than one about a design principle.
- Quotas, regional availability, and licensing change frequently, so an item about a specific limit can age faster than one about the decision behind it.
- Duration, price, and item count for AI-300 are not published on the study guide; third-party figures are labelled as reported and are not relied on anywhere in the items.
- No Udemy account import, preview, or publication has been performed.
