# Official sources and coverage notes

Reviewed October 2026 against the **exam guide as of June 1, 2026** and the certification page. Product names, preview status, and prices change, so re-check before publishing or scheduling.

## Primary references

| Purpose | URL |
|---|---|
| Certification page (length, fee, format, languages) | https://cloud.google.com/learn/certification/machine-learning-engineer |
| Exam guide, June 1, 2026 revision (six sections and their weights) | https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf |
| BigQuery ML introduction | https://cloud.google.com/bigquery/docs/bqml-introduction |
| BigQuery ML `ML.TRANSFORM` and preprocessing | https://cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-transform |
| Gemini Enterprise Agent Platform, AutoML | https://cloud.google.com/vertex-ai/docs/start/automl-api |
| Agent Platform Pipelines | https://cloud.google.com/vertex-ai/docs/pipelines/introduction |
| Feature Store | https://cloud.google.com/vertex-ai/docs/featurestore/overview |
| Model Registry | https://cloud.google.com/vertex-ai/docs/model-registry/introduction |
| Model Garden | https://cloud.google.com/vertex-ai/docs/model-garden/explore-models |
| Prediction and endpoints | https://cloud.google.com/vertex-ai/docs/predictions/overview |
| Custom containers for prediction | https://cloud.google.com/vertex-ai/docs/predictions/custom-container-requirements |
| Model Monitoring | https://cloud.google.com/vertex-ai/docs/model-monitoring/overview |
| Model Armor | https://cloud.google.com/security-command-center/docs/model-armor-overview |
| Sensitive Data Protection | https://cloud.google.com/sensitive-data-protection/docs |
| Vertex AI Experiments | https://cloud.google.com/vertex-ai/docs/experiments/intro-vertex-ai-experiments |
| ML Metadata | https://cloud.google.com/vertex-ai/docs/ml-metadata/introduction |
| Tabular Workflows | https://cloud.google.com/vertex-ai/docs/tabular-data/tabular-workflows/overview |
| Ray on Google Cloud | https://cloud.google.com/vertex-ai/docs/open-source/ray-on-vertex-ai/overview |
| Cloud Build | https://cloud.google.com/build/docs/overview |
| Workbench and Colab Enterprise | https://cloud.google.com/vertex-ai/docs/workbench/introduction |

## Verified exam facts

| Fact | Value |
|---|---|
| Domains and weights | 1) Architecting low-code AI solutions ~13%; 2) Collaborating within and across teams to manage data and models ~16%; 3) Scaling prototypes into ML models ~21%; 4) Serving and scaling models ~20%; 5) Automating and orchestrating ML pipelines ~18%; 6) Monitoring AI solutions ~13% |
| Length | 2 hours |
| Fee | $200 USD plus applicable tax |
| Format | 50–60 multiple choice and multiple select questions |
| Case studies | **None.** The certification page and the guide describe no case-study component and no case-study weighting |
| Passing score | **Not published** — the exam reports pass or fail |
| Languages | English and Japanese |
| Validity | 2 years |
| Delivery | Online proctored or at a test centre |
| Prerequisites | None; 3+ years of industry experience including 1+ year designing and managing ML solutions on Google Cloud is recommended |
| Renewal | Recertification is a separate instrument with its own scope |

The length, fee, question range, and languages above are Google-published; the **passing score is not published**, and this package therefore never states a target percentage or converts a practice score into a pass mark.

Not claimed anywhere in this package: that the practice exams contain the live item count, that they reproduce lab tasks or any interactive console component, that they reproduce case studies (there are none to reproduce), or that completing the course earns the certification.

## Domain coverage and package weights

| Domain | Official weight | Per exam | Percent | Package total |
|---|---:|---:|---:|---:|
| 1. Architecting low-code AI solutions | ~13% | 12 | 12% | 72 |
| 2. Collaborating to manage data and models | ~16% | 16 | 16% | 96 |
| 3. Scaling prototypes into ML models | ~21% | 21 | 21% | 126 |
| 4. Serving and scaling models | ~20% | 20 | 20% | 120 |
| 5. Automating and orchestrating ML pipelines | ~18% | 18 | 18% | 108 |
| 6. Monitoring AI solutions | ~13% | 13 | 13% | 78 |

Google publishes one approximate weight per domain. The six published values total **101%**, so they cannot be copied straight into a 100-item exam; the one-point overshoot is removed from the smallest section, giving **12 / 16 / 21 / 20 / 18 / 13**. Every exam uses the identical allocation.

## Coverage against the published sections

The guide's bullets were read directly and mapped into 47 local study areas. The table records practice emphasis across all 600 items; counts describe this bank, not official weighting.

| Local ID | Study area | Items | Official bullets it supports |
|---|---|---:|---|
| 1.1 | BigQuery ML Model Building | 12 | 1.1 build models with BigQuery ML; choose the algorithm for the task |
| 1.2 | BigQuery ML Feature Engineering and Prediction | 12 | 1.1 `ML.TRANSFORM`, prediction and evaluation functions |
| 1.3 | Agent Platform AutoML | 12 | 1.1 AutoML on Gemini Enterprise Agent Platform; training budget and export |
| 1.4 | Gemini Fine-Tuning with BigQuery | 6 | 1.1 fine-tune a Gemini model from data that stays in BigQuery |
| 1.5 | Model Garden Model Selection | 6 | 1.1 first-party and open models in Model Garden; licensing and deployment |
| 1.6 | Industry AI APIs | 12 | 1.2 prebuilt vision, speech, language, video, and document APIs |
| 1.7 | Gemini Application Optimization | 12 | 1.3 cost, latency, availability, caching, grounding, and fallbacks |
| 2.1 | Preprocessing Tool Selection | 18 | 2.1 choose BigQuery, Dataflow, Dataproc, or in-memory preprocessing |
| 2.2 | Feature Store | 12 | 2.1 feature definitions, online and offline stores, bucketing and crossing |
| 2.3 | PII Handling and Data Privacy | 12 | 2.1 Sensitive Data Protection; drop, hash, bucket, or de-identify |
| 2.4 | Notebook Environments and Security | 12 | 2.1 Workbench, Colab Enterprise, private IP, shared VPC, idle shutdown |
| 2.5 | Experiment Tracking | 12 | 2.2 Vertex AI Experiments; parameters, metrics, seeds, comparison |
| 2.6 | Development Environment Selection | 12 | 2.2 Kubeflow, Pipelines, templates, Airflow, and Ray |
| 2.7 | Evaluation Metrics and LLM-as-a-Judge | 12 | 2.2 metric choice, LLM-as-a-judge, human review, AUC-PR, MAPE |
| 2.8 | Metadata and Lineage | 6 | 2.2 ML Metadata; dataset and code lineage for an artifact |
| 3.1 | Model Type Selection | 12 | 3.1 tabular, time series, DNN, and foundation model choice |
| 3.2 | Product Selection | 12 | 3.1 BigQuery ML, AutoML, or custom training for a constraint |
| 3.3 | Deployment Strategy Choice | 12 | 3.1 canary, shadow, blue/green, rolling, and A/B |
| 3.4 | Interpretability | 12 | 3.1 interpretable models and attribution methods |
| 3.5 | Training Data Organization | 12 | 3.2 Parquet, TFRecord, BigQuery source, and shard layout |
| 3.6 | Ingestion into Training Pipelines | 12 | 3.2 streaming and batch ingestion, dedup, schema validation |
| 3.7 | Custom Training and SDKs | 12 | 3.2 Python package on a prebuilt container versus a custom container |
| 3.8 | Training Failure Troubleshooting | 12 | 3.2 out-of-memory, quota, permission, and version failures |
| 3.9 | Hyperparameter Tuning | 12 | 3.2 tuning service, budget, early stopping, custom metric |
| 3.10 | Fine-Tuning Decisions | 6 | 3.2 full fine-tuning, LoRA, RAG, and prompting |
| 3.11 | Hardware and Accelerator Selection | 6 | 3.2 CPU, L4 and A100 GPUs, TPU slices |
| 3.12 | Distributed Training | 6 | 3.2 data and model parallelism, multi-worker, batch scaling |
| 4.1 | Batch and Online Inference | 18 | 4.1 batch prediction, online endpoints, streaming, request batching |
| 4.2 | Packaging and Custom Containers | 12 | 4.1 prebuilt containers, prediction routines, Artifact Registry |
| 4.3 | Model Registry and Versioning | 12 | 4.1 registry versions, aliases, rollback by pointer |
| 4.4 | Model Rollout Strategies | 12 | 4.1 A/B, canary, shadow, blue/green, rolling with traffic splits |
| 4.5 | Inference Preprocessing and Postprocessing | 12 | 4.1 train-serve transform parity, preprocessing inside the artifact |
| 4.6 | Endpoint Types and Access | 12 | 4.1 shared, dedicated, and private endpoints |
| 4.7 | Serving Hardware | 12 | 4.1 GPU selection and CPU-only serving |
| 4.8 | Serving Throughput and Scaling | 18 | 4.2 autoscaling, min and max replicas, concurrency |
| 4.9 | Production Tuning | 12 | 4.2 cost per request, latency targets, explanation metadata |
| 5.1 | Data and Model Validation | 18 | 5.1 validation steps, model gates, locked test sets, thresholds |
| 5.2 | Pipeline Orchestration Choice | 29 | 5.1 Pipelines, Airflow, Ray, Cloud Build, templates |
| 5.3 | Train and Serve Consistency | 24 | 5.1 shared transforms, Feature Store reads, cached steps |
| 5.4 | Retraining Policy | 18 | 5.2 schedule, drift, metric drop, and manual policies |
| 5.5 | CI/CD/CT with Cloud Build | 19 | 5.2 continuous training, event triggers, gated promotion |
| 6.1 | Secure AI and Prompt Protection | 19 | 6.1 Model Armor, safety filters, regex redaction, schemas, system instructions |
| 6.2 | Responsible AI and Bias | 12 | 6.1 responsible AI, bias slicing, data and model cards |
| 6.3 | Explainability | 13 | 6.2 Shapley, sampled Shapley, integrated gradients, interpretable models |
| 6.4 | Model Monitoring Configuration | 12 | 6.2 baselines, thresholds, alerts, latency and token tracking |
| 6.5 | Skew and Drift Types | 12 | 6.2 training-serving skew, data, concept, prediction, and attribution drift |
| 6.6 | Generative AI Monitoring | 10 | 6.2 generative quality evaluation and prompt/response logging |

These IDs are internal study aids. Google names objectives without this numbering, and no claim is made that the bank is psychometrically calibrated against the live exam.

## Deliberate omissions and disclosures

| Excluded element | Why it is excluded | How the package compensates |
|---|---|---|
| Case studies | The published PMLE format has no case-study component | Nothing is imitated; the absence is stated in the README, landing page, curriculum, and package checks |
| Sequencing items | The published format is multiple choice and multiple select only | No sequencing stems, no `→` options, and `validate.py` rejects them |
| Lab and interactive console tasks | Require a live project | Configuration is presented as text and read, not typed |
| Live item count | The live exam samples 50–60 questions | Each exam is labelled a 100-item expanded bank |
| Passing score | Google does not publish one | No target percentage is stated anywhere |

## Licensing, capability, and pricing statements

Every item is answerable without a project. Where a scenario depends on a capability that requires a paid edition, a specific region, or an allowlisted feature, the explanation names that dependency rather than implying the capability is free or universal. No item asserts a current price, quota, or regional availability; the only price in the package is the published $200 registration fee, cited as published and subject to change.
