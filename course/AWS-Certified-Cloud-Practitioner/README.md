# AWS Certified Cloud Practitioner (CLF-C02) — practice course

**6 mock exams × 65 original questions = 390 · 55 multiple-choice + 10 multiple-response · every option explained · 90-minute paper length matched · no case studies, because the exam has none**

This package is an independent study aid for the **AWS Certified Cloud Practitioner (CLF-C02)** exam. It is written for the candidate who has to recognise *which* AWS service or *which* cloud concept answers a stated business requirement — sales, marketing, product and project staff included, not only engineers.

> **Version notice.** Baseline: the AWS certification page and the official CLF-C02 exam guide, retrieved **October 2026** — **90 minutes**, **100 USD**, **65 questions of which 50 are scored and 15 are unscored**, **multiple choice and multiple response**, Pearson VUE test centre or online proctoring, **12 languages** (German and Italian retire after 31 December 2026), **no prerequisites**, and a **scaled score of 100–1000 with a minimum passing score of 700**. Certification is valid for **three years**. The published format has **no case-study component**, so this bank contains **no case studies and no case-study documents**. Each practice exam is 65 items, the same length as the live paper, so the 90-minute clock gives the same ~83 seconds per item you will have on exam day.

Independent educational content — not actual, recalled, or copied AWS exam items. No AWS endorsement, no import or publication guarantee, and no passing guarantee.

---

## What is inside

| Folder | Contents |
|---|---|
| `01-landing-page/` | Ready-to-paste course metadata, per-practice-test names and descriptions (full and trimmed), welcome and congratulations messages, allocation table, 37-skill map, FAQ |
| `02-curriculum/` | Study arc, exam-by-exam plan, six-week schedule, scoring method, 90-minute time budget |
| `03-practice-sets/set-1…6/` | Per exam: instructor CSV, Markdown review copy, and a set README |
| `04-resources/` | Authoring source (`bank.py`, `terms.py`, `sources.py`, `questions/`), tooling, format spec, publication checklist, source notes, `SUMMARY.md` |
| `05-sample-upload/` | One twelve-question mixed sample (three per domain: two multiple-choice and one multiple-response) to test how the platform renders the format |

## The six exams

| Exam | Scenario emphasis | Items |
|---:|---|---:|
| 1 | Retail and media | 65 |
| 2 | Healthcare and insurance | 65 |
| 3 | Logistics and manufacturing | 65 |
| 4 | Public sector and financial services | 65 |
| 5 | Education and travel | 65 |
| 6 | Startups, gaming, and energy | 65 |

Every exam uses the same blueprint split (16 / 19 / 22 / 8) and the same 37-skill plan, so the emphasis column describes the industries used in that set's scenarios, not a different weighting. All four domains are examined in all six sets.

## No case studies

AWS's published CLF-C02 format is multiple choice and multiple response with no case-study component. Accordingly:

- there is no `cases.py`, no `case-studies.md`, no case-embedded CSV variant, and no `case-study-upload-guide.md` in this folder;
- no stem begins `Case study —` and `validate.py` fails the export if one appears;
- `build.py`'s `check_source()` refuses to build if a case phrase reaches a stem or a rationale;
- `package.py` rejects the package if a case-study document is reintroduced.

The exam does include multiple-response items, so the CSV uses a five-option layout for those (two correct indices, three distractors) and a statement of the selection count in the stem — the same 17-column contract the Udemy importer expects.

## Concept and service recognition, not configuration

AWS lists coding, architecture design, troubleshooting, implementation, and load and performance testing as **out of scope** for this exam. Items therefore describe a business requirement and ask which concept or service fits, or which choice would fail it. No item is a console recipe, none needs an AWS account, and the test suite rejects console-instruction phrasing outright, so the bank cannot drift into click-path trivia.

## Blueprint allocation

| Official domain | Published weight | Per exam | Percent | Package total |
|---|---:|---:|---:|---:|
| 1. Cloud Concepts | 24% | 16 | 24.6% | 96 |
| 2. Security and Compliance | 30% | 19 | 29.2% | 114 |
| 3. Cloud Technology and Services | 34% | 22 | 33.8% | 132 |
| 4. Billing, Pricing, and Support | 12% | 8 | 12.3% | 48 |

**The published weights total exactly 100%.** Applied to 65 items they give 15.6, 19.5, 22.1 and 7.8. The per-exam counts are **16 / 19 / 22 / 8**: the two exact halves are resolved towards a total of 65, so security rounds down to 19 and billing rounds up to 8. The tests assert those exact counts, so a future AWS revision that changes the weights fails the build instead of being silently absorbed.

## Item mix

| Format | Per exam | Options | Notes |
|---|---:|---|---|
| Multiple choice (`multiple-choice`) | 55 | 4 | One correct index in slots 1–4, balanced across the bank |
| Multiple response (`multi-select`) | 10 | 5 | Two correct indices, three distractors, "Select two" in the stem; 2 / 3 / 4 / 1 across domains 1–4 |
| Sequencing or drag-and-drop | 0 | — | The published format is multiple choice and multiple response only |

**AWS publishes no split between multiple choice and multiple response**, so the 55 / 10 mix is an authoring choice. It is labelled as one in every set README, in the review copies, and on the landing page.

## Time pressure: this bank matches the live paper

| | Items | Clock | Seconds per item |
|---|---:|---:|---:|
| Live exam | 65 (50 scored + 15 unscored) | 90 minutes | ~83 |
| This bank | 65 | 90 minutes | ~83 |

So a timed run here is a genuine rehearsal of the appointment pacing. One difference is stated rather than hidden: 15 of the live 65 items are unscored and unidentified, so a practice percentage here measures all 65 items.

## Scoring: what 700 means

AWS publishes a **minimum passing score of 700 on a scaled range of 100–1000**, with compensatory scoring and no separate pass mark per domain. Because 700 is a scaled score rather than 70% of 65, this course states it as published and never converts a practice percentage into it. A practice score of 80% means 52 of 65 items were correct; it is not an estimate of a scaled score.

## Claims discipline

- **The passing standard is stated exactly as published** — a scaled 700 on a 100–1000 range — and is never restated as a raw percentage.
- **65 items is the live length.** No expanded-bank caveat is needed, and none is implied.
- **The multiple-choice and multiple-response split is disclosed as an authoring choice.**
- **No case studies are imitated.** The absence is documented rather than filled with plausible-looking scenarios.
- **Stems are unique beyond exact wording.** `build.py` rejects any pair of stems whose content-word overlap exceeds 0.72, so a reworded repeat of the same decision cannot ship.
- **Product names follow the CLF-C02 exam guide**: Regions and Availability Zones, edge locations, Local Zones, Wavelength, Outposts, IAM users, groups, roles, policies and Identity Center, federation with Cognito for customers, security groups and network ACLs, WAF, Shield, Network Firewall, KMS and customer managed keys, S3 server-side encryption, Certificate Manager, Secrets Manager, GuardDuty, Inspector, Macie, Security Hub, Detective, Artifact, Config, CloudTrail, Audit Manager, Trusted Advisor, Organizations service control policies, Control Tower, Service Catalog, EC2, Lambda, ECS and EKS with Fargate, Elastic Beanstalk, Lightsail, Batch, App Runner, S3 storage classes, EBS, EFS, FSx, Storage Gateway, Snowball, Backup, RDS, Aurora, DynamoDB, Redshift, ElastiCache, Neptune, DocumentDB, VPC, Route 53, CloudFront, Direct Connect, Site-to-Site VPN, Elastic Load Balancing, API Gateway, Transit Gateway, PrivateLink, Global Accelerator, CloudWatch, CloudFormation, Systems Manager, Health Dashboard, SQS, SNS, EventBridge, Step Functions, Kinesis, Amazon MQ, SageMaker, Bedrock, Athena, Glue, EMR, QuickSight, CodePipeline, CodeBuild, CodeDeploy, Cloud9, X-Ray, On-Demand, Reserved Instances, Spot Instances, Savings Plans, Dedicated Hosts, Cost Explorer, Budgets, the Cost and Usage Report, Pricing Calculator, Cost Anomaly Detection, cost allocation tags, consolidated billing, Basic, Developer, Business and Enterprise Support, the Free Tier, and the AWS Partner Network.
- **No community statistics are borrowed.** Question counts, pass rates, and "same as the real exam" claims from question-sharing sites are not used as evidence, benchmarks, or marketing anywhere in this course.

## Verification

```bash
cd course/AWS-Certified-Cloud-Practitioner/04-resources
python3 build.py
python3 make_sample.py
python3 validate.py --report validation-report.json   # PASS: 6 sets / 390 questions
python3 -m unittest test_course                       # structural and artifact tests
python3 package.py                                    # reproducible ZIP
cd ../../.. && python3 course/check_csv_upload.py --all
```

Current status: **390 items, 6 sets, all structural checks passing**. Accurate to the best of our review, but not independently fact-checked, not psychometrically calibrated, and not a substitute for hands-on work in an AWS account.

## Rights and attribution

All 390 questions and all documentation in this folder are original work for this repository. Amazon Web Services, AWS, and the certification names are trademarks of Amazon.com, Inc. or its affiliates; this package is independent and makes no claim of affiliation or endorsement.
