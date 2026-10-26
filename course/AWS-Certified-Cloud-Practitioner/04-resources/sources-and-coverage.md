# Sources and coverage — AWS Certified Cloud Practitioner (CLF-C02)

Every factual claim about the exam in this course is traceable to one of two AWS pages, both read in **October 2026**. Nothing here is drawn from question-sharing sites, forums, or recalled exam content.

## Primary sources

| Source | What it establishes |
|---|---|
| AWS Certified Cloud Practitioner certification page — <https://aws.amazon.com/certification/certified-cloud-practitioner/> | 90-minute appointment, 100 USD fee, 65 questions, question types, delivery through Pearson VUE or online proctoring, 12 languages with German and Italian retiring after 31 December 2026, no prerequisites, typical candidate profile, three-year validity, recertification paths, and the 50 percent discount on a later AWS exam |
| CLF-C02 exam guide — <https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html> | The four content domains and their weights (24 / 30 / 34 / 12 percent), the 50 scored and 15 unscored split, multiple choice and multiple response formats, compensatory scoring on a 100–1000 scale with a minimum passing score of 700, the out-of-scope job tasks, and the in-scope services and technologies list behind the study map |

## Verified exam facts

| Fact | Value used in this course |
|---|---|
| Appointment length | 90 minutes |
| Fee | 100 USD |
| Questions | 65, of which 50 are scored and 15 are unscored; AWS does not identify the unscored items |
| Item types | Multiple choice (one correct answer, three distractors) and multiple response (two or more correct answers from five or more options) |
| Split between item types | **Not published by AWS** — the 55 / 10 mix here is an authoring choice |
| Delivery | Pearson VUE test centre or online proctoring |
| Languages | 12; German and Italian retire after 31 December 2026 |
| Prerequisites | None published; typical candidate has up to six months of AWS exposure and no IT background is required |
| Scoring | Compensatory, 100–1000 scale, minimum passing score 700 |
| Validity | Three years; recertification by Cloud Quest, retake, or passing an Associate or Professional exam |
| Case studies | None in the published format |
| Out of scope | Coding, architecture design, troubleshooting, implementation, and load and performance testing |

## Domain weights and the per-exam allocation

The published weights total exactly 100 percent. Applied to 65 items they give 15.6, 19.5, 22.1 and 7.8 items. The per-exam counts are **16 / 19 / 22 / 8**, which resolves the two exact halves towards a total of 65: cloud concepts rounds up from 15.6, security rounds down from 19.5, technology rounds down from 22.1, and billing rounds up from 7.8. The allocation is asserted in the tests, so a change to any published weight fails the build rather than being absorbed silently.

## Coverage mapping

Local study-map identifiers are this course's own numbering, not AWS objective numbers: AWS publishes task statements inside each domain page rather than as numbered objectives. Every skill is exercised in every set.

| Local skill | Official domain | Items per exam | Bank total |
|---|---|---:|---:|
| **1. Cloud Concepts** | **24%** | **16** | **96** |
| 1.1 Cloud Value Proposition | | 2 | 12 |
| 1.2 Cloud Economics and Total Cost of Ownership | | 2 | 12 |
| 1.3 Cloud Architecture Design Principles | | 2 | 12 |
| 1.4 Well-Architected Framework | | 2 | 12 |
| 1.5 Cloud Adoption Framework | | 2 | 12 |
| 1.6 Migration Strategies | | 2 | 12 |
| 1.7 Global Infrastructure | | 1 | 6 |
| 1.8 Resiliency and Availability | | 2 | 12 |
| 1.9 Shared Responsibility Model | | 1 | 6 |
| **2. Security and Compliance** | **30%** | **19** | **114** |
| 2.1 Identity and Access Management | | 2 | 12 |
| 2.2 Root User and Credential Hygiene | | 2 | 12 |
| 2.3 IAM Roles and Federation | | 2 | 12 |
| 2.4 Network Security Controls | | 2 | 12 |
| 2.5 Encryption and Key Management | | 2 | 12 |
| 2.6 Secrets and Certificate Handling | | 1 | 6 |
| 2.7 Threat Detection and Monitoring | | 2 | 12 |
| 2.8 Data Protection and Classification | | 2 | 12 |
| 2.9 Compliance and Audit Evidence | | 2 | 12 |
| 2.10 Shared Responsibility Boundaries | | 1 | 6 |
| 2.11 Governance Guardrails | | 1 | 6 |
| **3. Cloud Technology and Services** | **34%** | **22** | **132** |
| 3.1 Compute Services | | 2 | 12 |
| 3.2 Storage Services | | 2 | 12 |
| 3.3 Database Services | | 2 | 12 |
| 3.4 Networking and Content Delivery | | 2 | 12 |
| 3.5 Management and Governance Services | | 2 | 12 |
| 3.6 Integration and Messaging | | 2 | 12 |
| 3.7 Analytics and Machine Learning | | 2 | 12 |
| 3.8 Developer Tooling | | 2 | 12 |
| 3.9 Deployment and Provisioning | | 2 | 12 |
| 3.10 Monitoring and Observability | | 2 | 12 |
| 3.11 Hybrid and Edge Services | | 2 | 12 |
| **4. Billing, Pricing, and Support** | **12%** | **8** | **48** |
| 4.1 Pricing Models | | 2 | 12 |
| 4.2 Cost Management Tools | | 2 | 12 |
| 4.3 Billing and Account Structures | | 1 | 6 |
| 4.4 Support Plans | | 1 | 6 |
| 4.5 Guidance and Self-Service Resources | | 1 | 6 |
| 4.6 Free Tier and Discounts | | 1 | 6 |
| | **Total** | **65** | **390** |

## What is deliberately not covered

- **Case studies.** The published format has none.
- **Sequencing, drag-and-drop and interactive item types.** Not part of the published format, and not expressible in a CSV.
- **Lab tasks, console walkthroughs and configuration recipes.** AWS places implementation and troubleshooting out of scope for this exam.
- **Coding and architecture design questions.** Also out of scope: no item asks for code, a schema, a network design or a multi-account architecture.
- **Load and performance testing.** Out of scope, and it would need a live environment rather than a written item.
- **Passing-score prediction.** The published 700 is a scaled score; no practice percentage in this course is converted into it.

## Source discipline

- The two AWS pages are the only exam-fact sources. Where AWS does not publish something — the item-type split above all — this course says so instead of estimating.
- Service descriptions are written from AWS's own service documentation and the CLF-C02 in-scope service list, not from third-party summaries.
- No examtopics, exam-collection, braindump or forum content was read, copied, paraphrased or used as a topic checklist. The bank is original work.
- Product names are checked against the current AWS service names at the time of writing. AWS renames services, so re-check names before publishing.
- No vendor endorsement is claimed or implied, and no result is guaranteed.
