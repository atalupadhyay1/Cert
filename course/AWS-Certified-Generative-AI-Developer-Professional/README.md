# AWS Certified Generative AI Developer - Professional (AIP-C01) — practice course

**6 mock exams × 75 original questions = 450 · 60 multiple-choice + 15 multiple-response · every option explained · 180-minute paper length matched · no case studies, because the exam has none**

This package is an independent study aid for the **AWS Certified Generative AI Developer - Professional (AIP-C01)** exam. It is written for the engineer who has to choose a vector store, a chunking strategy, a retrieval pattern, a model, a guardrail, an evaluation metric and a cost lever for a stated production requirement — not for someone reciting service names.

> **Version notice.** Baseline: the AWS certification page and the AIP-C01 exam guide, retrieved **October 2026** — **180 minutes**, **300 USD**, **75 questions of which 65 are scored and 10 are unscored**, **multiple choice and multiple response**, Pearson VUE test centre or online proctoring, **English, Japanese, Korean and Simplified Chinese**, a **scaled score of 100–1000 with a minimum passing score of 750** under compensatory scoring, and **three-year validity**. AWS recommends two or more years building production-grade applications plus one year of hands-on generative AI work. The published format has **no case-study component**, so this bank contains **no case studies and no case-study documents**.

Independent educational content — not actual, recalled, or copied AWS exam items. No AWS endorsement, no import or publication guarantee, and no passing guarantee.

---

## What is inside

| Folder | Contents |
|---|---|
| `01-landing-page/` | Ready-to-paste course metadata, per-practice-test names and descriptions (full and trimmed), welcome and congratulations messages, allocation table, 45-skill map, FAQ |
| `02-curriculum/` | Study arc, exam-by-exam plan, six-week schedule, scoring method, 180-minute time budget |
| `03-practice-sets/set-1…6/` | Per exam: instructor CSV, Markdown review copy, and a set README |
| `04-resources/` | Authoring source (`bank.py`, `terms.py`, `sources.py`, `questions/`), tooling, format spec, publication checklist, source notes, `SUMMARY.md` |
| `05-sample-upload/` | One fifteen-question mixed sample (three per domain: two multiple-choice and one multiple-response) to test how the platform renders the format |

## The six exams

| Exam | Scenario emphasis | Items |
|---:|---|---:|
| 1 | Retail and customer service | 75 |
| 2 | Financial services and insurance | 75 |
| 3 | Healthcare and life sciences | 75 |
| 4 | Media, publishing, and marketing | 75 |
| 5 | Manufacturing and field operations | 75 |
| 6 | Software delivery and internal platform | 75 |

Every exam uses the same blueprint split (23 / 20 / 15 / 9 / 8) and the same 45-skill plan, so the emphasis column describes the industries used in that set's scenarios, not a different weighting. All five domains are examined in all six sets.

## No case studies

The published AIP-C01 format is multiple choice and multiple response with no case-study component. Accordingly:

- there is no `cases.py`, no `case-studies.md`, no case-embedded CSV variant, and no `case-study-upload-guide.md` in this folder;
- no stem begins `Case study —` and `validate.py` fails the export if one appears;
- `build.py`'s `check_source()` refuses to build if a case phrase reaches a stem or a rationale;
- `package.py` rejects the package if a case-study document is reintroduced.

The exam does include multiple-response items, so the CSV uses a five-option layout for those (two correct indices, three distractors) and a statement of the selection count in the stem — the same 17-column contract the Udemy importer expects.

## Integration depth, not model training

The guide lists **model development and training, advanced ML techniques, and data engineering and feature engineering** as out of scope. Items therefore ask about a decision inside an existing GenAI platform: which store, which chunk split, which retrieval control, which model, which agent pattern, which guardrail, which metric, which cost lever. No item is a console recipe, none needs an AWS account, and the test suite rejects console-instruction phrasing outright.

## Blueprint allocation

| Official domain | Published weight | Per exam | Percent | Package total |
|---|---:|---:|---:|---:|
| 1. Foundation Model Integration, Data Management, and Compliance | 31% | 23 | 30.7% | 138 |
| 2. Implementation and Integration | 26% | 20 | 26.7% | 120 |
| 3. AI Safety, Security, and Governance | 20% | 15 | 20.0% | 90 |
| 4. Operational Efficiency and Optimization for GenAI Applications | 12% | 9 | 12.0% | 54 |
| 5. Testing, Validation, and Troubleshooting | 11% | 8 | 10.7% | 48 |

**The published weights total exactly 100%.** Applied to 75 items they give 23.25 / 19.5 / 15 / 9 / 8.25. Largest-remainder rounding gives the surplus item to Domain 2, whose exact share is the half item, so the per-exam counts are **23 / 20 / 15 / 9 / 8** — every count within 0.5 items of its published weight. The tests assert those exact counts, so a future weight change fails the build instead of being silently absorbed.

## Item mix

| Format | Per exam | Options | Notes |
|---|---:|---|---|
| Multiple choice (`multiple-choice`) | 60 | 4 | One correct index in slots 1–4, balanced across the bank |
| Multiple response (`multi-select`) | 15 | 5 | Two correct indices, three distractors, "Select two" in the stem; 3 / 3 / 3 / 3 / 3 across domains 1–5 |
| Sequencing or drag-and-drop | 0 | — | The published format is multiple choice and multiple response only |

**AWS publishes no split between multiple choice and multiple response**, so the 60 / 15 mix is an authoring choice. It is labelled as one in every set README, in the review copies, and on the landing page.

## Time pressure: this bank matches the published paper

| | Items | Clock | Seconds per item |
|---|---:|---:|---:|
| Published exam | 75 (65 scored + 10 unscored) | 180 minutes | ~144 |
| This bank | 75 | 180 minutes | ~144 |

So a timed run here rehearses the published pacing. One difference is stated rather than hidden: 10 of the live 75 items are unscored and unidentified, so a practice percentage here measures all 75 items.

## Scoring: what 750 means

AWS publishes a **minimum passing score of 750 on a scaled range of 100–1000**, with compensatory scoring and no separate pass mark per domain. Because 750 is a scaled score rather than a percentage of 75, this course states it as published and never converts a practice percentage into it. A practice score of 80% means 60 of 75 items were correct; it is not an estimate of a scaled score.

## Claims discipline

- **The passing standard is stated exactly as published** — a scaled 750 on a 100–1000 range — and is never restated as a raw percentage.
- **75 items is the published length**, including the published 65 scored / 10 unscored proportion.
- **The multiple-choice and multiple-response split is disclosed as an authoring choice.**
- **No case studies are imitated.** The absence is documented rather than filled with plausible-looking scenarios.
- **Stems are unique beyond exact wording.** `build.py` rejects any pair of stems whose content-word overlap exceeds 0.72, so a reworded repeat of the same decision cannot ship.
- **Product names follow the AIP-C01 in-scope service list**: Amazon Bedrock and its knowledge bases, prompt management, prompt flows, guardrails, model evaluation, provisioned throughput, cross-Region inference, batch inference and AgentCore; Strands Agents, AWS Agent Squad and the Model Context Protocol; Amazon OpenSearch Service, Amazon Aurora with pgvector, Amazon Neptune, Amazon DocumentDB, Amazon DynamoDB, Amazon ElastiCache, Amazon RDS and Amazon S3; AWS Glue and Glue Data Quality, Amazon Kinesis, Amazon MSK, Amazon Athena, Amazon EMR and Amazon Quick Sight; AWS Lambda, Lambda@Edge, Amazon EC2, AWS App Runner, AWS Outposts and AWS Wavelength; Amazon ECS, Amazon EKS, AWS Fargate and Amazon ECR; Amazon API Gateway, AWS AppSync, Amazon CloudFront, Elastic Load Balancing, AWS Global Accelerator, Route 53, AWS PrivateLink and Amazon VPC; AWS Step Functions, Amazon EventBridge, Amazon SQS, Amazon SNS, Amazon AppFlow and AWS AppConfig; AWS CloudFormation, AWS CDK, AWS CodePipeline, CodeBuild, CodeDeploy, CodeArtifact, X-Ray and Amazon Q Developer; Amazon Comprehend, Kendra, Lex, Q Business, Rekognition, Transcribe, Textract, Titan, Augmented AI, SageMaker AI with Model Registry, Model Monitor, Clarify, Processing, Ground Truth, JumpStart, Neo and Unified Studio; CloudWatch with metrics, logs, Logs Insights and Synthetics, Managed Grafana, CloudTrail, Cost Explorer, Cost Anomaly Detection, Systems Manager, Service Catalog, Chatbot and the Well-Architected Tool; IAM with Access Analyzer and Identity Center, Cognito, AWS KMS, Secrets Manager, Macie, WAF and the AWS Encryption SDK; Amazon S3 Intelligent-Tiering and Lifecycle policies; and AWS DataSync and Transfer Family.
- **No community statistics are borrowed.** Question counts, pass rates, and "same as the real exam" claims from question-sharing sites are not used as evidence, benchmarks, or marketing anywhere in this course.

## Verification

```bash
cd course/AWS-Certified-Generative-AI-Developer-Professional/04-resources
python3 build.py
python3 make_sample.py
python3 validate.py --report validation-report.json   # PASS: 6 sets / 450 questions
python3 -m unittest test_course                       # structural and artifact tests
python3 package.py                                    # reproducible ZIP
cd ../../.. && python3 course/check_csv_upload.py --all
```

Current status: **450 items, 6 sets, all structural checks passing**. Accurate to the best of our review, but not independently fact-checked, not psychometrically calibrated, and not a substitute for hands-on work in an AWS account.

## Rights and attribution

All 450 questions and all documentation in this folder are original work for this repository. Amazon Web Services, AWS, Amazon Bedrock and the certification names are trademarks of Amazon.com, Inc. or its affiliates; this package is independent and makes no claim of affiliation or endorsement.
