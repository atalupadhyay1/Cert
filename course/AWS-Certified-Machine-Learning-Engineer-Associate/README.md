# AWS Certified Machine Learning Engineer – Associate (MLA-C02) — practice course

**6 mock exams × 65 original questions = 390 · 50 multiple-choice + 15 multiple-response · every option explained · 130-minute paper length matched · no case studies, because the exam has none**

This package is an independent study aid for the **AWS Certified Machine Learning Engineer – Associate (MLA-C02)** exam. It is written for the engineer who has to choose a data store, a model, an inference pattern, a scaling metric and a monitoring signal for a stated production requirement — not for someone reciting service names.

> **Version notice.** Baseline: the AWS certification page and the MLA-C02 exam guide, retrieved **October 2026** — **130 minutes**, **150 USD**, **65 questions of which 50 are scored and 15 are unscored**, **multiple choice and multiple response**, Pearson VUE test centre or online proctoring, a **scaled score of 100–1000 with a minimum passing score of 720** under compensatory scoring, and **three-year validity**. AWS recommends at least one year of experience with SageMaker AI, Amazon Bedrock and other ML engineering services. The published format has **no case-study component**, so this bank contains **no case studies and no case-study documents**. **MLA-C02 replaced MLA-C01 in English on 29 September 2026**; while the updated exam is in beta it runs as 85 questions in 170 minutes for 75 USD in English only, with the extra items unscored and no pass/fail result. These sets follow the published 65-question, 130-minute form.

Independent educational content — not actual, recalled, or copied AWS exam items. No AWS endorsement, no import or publication guarantee, and no passing guarantee.

---

## What is inside

| Folder | Contents |
|---|---|
| `01-landing-page/` | Ready-to-paste course metadata, per-practice-test names and descriptions (full and trimmed), welcome and congratulations messages, allocation table, 45-skill map, FAQ |
| `02-curriculum/` | Study arc, exam-by-exam plan, six-week schedule, scoring method, 130-minute time budget |
| `03-practice-sets/set-1…6/` | Per exam: instructor CSV, Markdown review copy, and a set README |
| `04-resources/` | Authoring source (`bank.py`, `terms.py`, `sources.py`, `questions/`), tooling, format spec, publication checklist, source notes, `SUMMARY.md` |
| `05-sample-upload/` | One twelve-question mixed sample (three per domain: two multiple-choice and one multiple-response) to test how the platform renders the format |

## The six exams

| Exam | Scenario emphasis | Items |
|---:|---|---:|
| 1 | Retail and e-commerce | 65 |
| 2 | Financial services and insurance | 65 |
| 3 | Healthcare and life sciences | 65 |
| 4 | Manufacturing and IoT | 65 |
| 5 | Media, search, and RAG assistants | 65 |
| 6 | Logistics and support agents | 65 |

Every exam uses the same blueprint split (18 / 16 / 16 / 15) and the same 45-skill plan, so the emphasis column describes the industries used in that set's scenarios, not a different weighting. All four domains are examined in all six sets.

## No case studies

The published MLA-C02 format is multiple choice and multiple response with no case-study component. Accordingly:

- there is no `cases.py`, no `case-studies.md`, no case-embedded CSV variant, and no `case-study-upload-guide.md` in this folder;
- no stem begins `Case study —` and `validate.py` fails the export if one appears;
- `build.py`'s `check_source()` refuses to build if a case phrase reaches a stem or a rationale;
- `package.py` rejects the package if a case-study document is reintroduced.

The exam does include multiple-response items, so the CSV uses a five-option layout for those (two correct indices, three distractors) and a statement of the selection count in the stem — the same 17-column contract the Udemy importer expects.

## Implementation depth, not architecture breadth

The guide lists **designing and architecting full end-to-end AI and ML solutions, setting ML strategy and best practice, integrating a wide array of new services and tools, and working deeply in two or more ML domains** as out of scope. Items therefore ask about a decision inside an existing platform: which store, which model, which tuning objective, which endpoint type, which scaling metric, which monitor, which control. No item is a console recipe, none needs an AWS account, and the test suite rejects console-instruction phrasing outright.

## Blueprint allocation

| Official domain | Published weight | Per exam | Percent | Package total |
|---|---:|---:|---:|---:|
| 1. Data Preparation for ML and AI | 28% | 18 | 27.7% | 108 |
| 2. ML Model and Foundation Model (FM) Development | 24% | 16 | 24.6% | 96 |
| 3. Deployment and Orchestration of ML and AI Workflows | 24% | 16 | 24.6% | 96 |
| 4. Operating, Monitoring, and Securing ML and AI Solutions | 24% | 15 | 23.1% | 90 |

**The published weights total exactly 100%.** Applied to 65 items they give 18.2 / 15.6 / 15.6 / 15.6. Largest-remainder rounding would give 18 / 16 / 16 / 16, which overshoots the paper by one item, so the spare item is removed from Domain 4 and the per-exam counts are **18 / 16 / 16 / 15** — every count within 0.6 items of its published weight. The tests assert those exact counts, so a future weight change fails the build instead of being silently absorbed.

## Item mix

| Format | Per exam | Options | Notes |
|---|---:|---|---|
| Multiple choice (`multiple-choice`) | 50 | 4 | One correct index in slots 1–4, balanced across the bank |
| Multiple response (`multi-select`) | 15 | 5 | Two correct indices, three distractors, "Select two" in the stem; 4 / 4 / 4 / 3 across domains 1–4 |
| Sequencing or drag-and-drop | 0 | — | The published format is multiple choice and multiple response only |

**AWS publishes no split between multiple choice and multiple response**, so the 50 / 15 mix is an authoring choice. It is labelled as one in every set README, in the review copies, and on the landing page.

## Time pressure: this bank matches the published paper

| | Items | Clock | Seconds per item |
|---|---:|---:|---:|
| Published exam | 65 (50 scored + 15 unscored) | 130 minutes | ~120 |
| This bank | 65 | 130 minutes | ~120 |
| MLA-C02 beta sitting | 85 | 170 minutes | ~120 |

So a timed run here rehearses the published pacing. One difference is stated rather than hidden: 15 of the live 65 items are unscored and unidentified, so a practice percentage here measures all 65 items.

## Scoring: what 720 means

AWS publishes a **minimum passing score of 720 on a scaled range of 100–1000**, with compensatory scoring and no separate pass mark per domain. Because 720 is a scaled score rather than a percentage of 65, this course states it as published and never converts a practice percentage into it. A practice score of 80% means 52 of 65 items were correct; it is not an estimate of a scaled score. Beta sittings do not produce a pass or fail result.

## Claims discipline

- **The passing standard is stated exactly as published** — a scaled 720 on a 100–1000 range — and is never restated as a raw percentage.
- **65 items is the published length.** The beta's 85-item form is disclosed wherever the paper is described.
- **The multiple-choice and multiple-response split is disclosed as an authoring choice.**
- **No case studies are imitated.** The absence is documented rather than filled with plausible-looking scenarios.
- **Stems are unique beyond exact wording.** `build.py` rejects any pair of stems whose content-word overlap exceeds 0.72, so a reworded repeat of the same decision cannot ship.
- **Product names follow the MLA-C02 exam guide**: Amazon S3 with the Parquet, ORC, JSON and CSV formats and the Standard, Intelligent-Tiering, Standard-IA and Glacier storage classes, Amazon EBS, Amazon EFS, Amazon FSx for Lustre, Amazon RDS with pgvector, Amazon DynamoDB, Amazon OpenSearch Service, AWS Glue with the Data Catalog and Data Quality, AWS Glue DataBrew, SageMaker Data Wrangler, Amazon EMR, AWS Database Migration Service, Amazon Kinesis Data Streams, Amazon Data Firehose, Amazon MSK, AWS Lambda, SageMaker Feature Store, SageMaker Ground Truth with automated labelling, SageMaker Clarify, SageMaker AI training jobs with built-in algorithms, script mode, automatic model tuning, managed Spot training, warm pools, distributed training and training plan options, SageMaker Pipelines, SageMaker Model Registry, SageMaker Inference Recommender, SageMaker Neo, SageMaker HyperPod, real-time, serverless, asynchronous and batch inference, multi-model and multi-container endpoints, Amazon Bedrock with foundation models, embeddings, provisioned throughput, custom model import, Prompt Management, knowledge bases, Guardrails, model evaluation and AgentCore Observability, AWS AI services including Textract, Comprehend, Transcribe and Rekognition, Amazon CloudWatch with metrics, alarms, dashboards, Logs Insights and generative AI observability, AWS X-Ray, AWS CloudTrail, AWS Config, Amazon Inspector, Amazon CodeGuru, AWS CodeCommit, CodeBuild, CodeDeploy, CodePipeline and CodeConnections, Amazon ECR, Amazon ECS, Amazon EKS, AWS Batch, AWS Step Functions, Amazon EventBridge, AWS Secrets Manager, AWS KMS, IAM roles, policies and service control policies in AWS Organizations, VPC subnets, security groups, interface endpoints and NAT gateways, and Cost Explorer, AWS Budgets and Savings Plans.
- **No community statistics are borrowed.** Question counts, pass rates, and "same as the real exam" claims from question-sharing sites are not used as evidence, benchmarks, or marketing anywhere in this course.

## Verification

```bash
cd course/AWS-Certified-Machine-Learning-Engineer-Associate/04-resources
python3 build.py
python3 make_sample.py
python3 validate.py --report validation-report.json   # PASS: 6 sets / 390 questions
python3 -m unittest test_course                       # structural and artifact tests
python3 package.py                                    # reproducible ZIP
cd ../../.. && python3 course/check_csv_upload.py --all
```

Current status: **390 items, 6 sets, all structural checks passing**. Accurate to the best of our review, but not independently fact-checked, not psychometrically calibrated, and not a substitute for hands-on work in an AWS account.

## Rights and attribution

All 390 questions and all documentation in this folder are original work for this repository. Amazon Web Services, AWS, Amazon SageMaker, Amazon Bedrock and the certification names are trademarks of Amazon.com, Inc. or its affiliates; this package is independent and makes no claim of affiliation or endorsement.
