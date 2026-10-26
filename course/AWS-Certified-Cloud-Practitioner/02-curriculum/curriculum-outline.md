# Curriculum outline — AWS Certified Cloud Practitioner (CLF-C02) practice course

**Six 65-item mock exams · 390 original questions · a 90-minute rehearsal at live pace**

This outline turns the bank into a study sequence. Every exam is blueprint-weighted **16 / 19 / 22 / 8** against the published **24 / 30 / 34 / 12** percent, so the order below is about concept difficulty and topic reinforcement, not about weighting.

AWS publishes **65 questions in 90 minutes**, of which **50 are scored and 15 are unscored**, with **no case-study component** and **no prerequisites**. Because each set here is also 65 items, the clock gives the same **~83 seconds per item** as the appointment, which makes a timed run a genuine pacing rehearsal rather than a slowed-down one.

## Learning arc

| Phase | Exam | Scenario emphasis | Study goal |
|---|---|---|---|
| Recognise value | 1 | Retail and media | Say what the cloud changes about money, speed and risk before naming a product |
| Secure it | 2 | Healthcare and insurance | Separate the identity decision from the network decision from the encryption decision |
| Operate it | 3 | Logistics and manufacturing | Choose the service from the workload's shape, not from habit |
| Govern it | 4 | Public sector and financial services | Read a constraint from a regulator and name the control that satisfies it |
| Account for it | 5 | Education and travel | Know which tool answers a cost question and which plan answers a support question |
| Defend the choices | 6 | Startups, gaming, and energy | Answer in one sentence why the near-miss option fails the stated requirement |

## Exam-by-exam study plan

### Exam 1 — Retail and media scenarios (65 items)
- Official split: 16 cloud concepts, 19 security and compliance, 22 technology and services, 8 billing.
- Focus: elasticity and global reach as business benefits; capital versus operating expense and total cost of ownership; design principles including loose coupling and serverless handling of short work; the six Well-Architected pillars; Cloud Adoption Framework perspectives; migration strategies from rehost through retire; Regions, Availability Zones and edge locations; multi-Availability-Zone design; who patches an EC2 guest operating system.
- Target skill: convert a business statement ("we sold out in 36 hours") into the cloud property that addresses it.

### Exam 2 — Healthcare and insurance scenarios (65 items)
- Focus: least privilege and groups; root user protection and key rotation; roles for workloads and federation for staff; security groups and network ACLs; WAF, Shield and Network Firewall; KMS and customer managed keys; server-side encryption and TLS in transit; Secrets Manager and Certificate Manager; GuardDuty, Inspector, Macie, Security Hub and Detective; data classification, lifecycle and retention; Artifact, Config, CloudTrail, Audit Manager and Trusted Advisor; the shared responsibility model; service control policies and Control Tower.
- Target skill: for a stated risk, name the control and the layer it acts on — identity, network, data or detection.

### Exam 3 — Logistics and manufacturing scenarios (65 items)
- Focus: EC2, Lambda, containers, Beanstalk, Lightsail, Batch and App Runner; S3 storage classes, EBS, EFS, FSx, Storage Gateway and Snowball; RDS, Aurora, DynamoDB, Redshift, ElastiCache, Neptune and DocumentDB; VPC, Route 53, CloudFront, Direct Connect, Site-to-Site VPN, Elastic Load Balancing, API Gateway, Transit Gateway, PrivateLink and Global Accelerator; CloudWatch, CloudFormation, Systems Manager, Trusted Advisor, Service Catalog, Control Tower and the Health Dashboard; SQS, SNS, EventBridge, Step Functions, Kinesis and Amazon MQ; Athena, Glue, EMR, QuickSight, SageMaker and Bedrock; CodePipeline, CodeBuild, CodeDeploy and X-Ray; Local Zones, Wavelength and Outposts.
- Target skill: given a workload shape — bursty, steady, archival, analytical, event-driven — pick the service family, then the service.

### Exam 4 — Public sector and financial services scenarios (65 items)
- Focus: least privilege under audit; explicit denies; root versus everyday administration; federation for staff and customer identity for citizens; subnet-level filtering and instance-level filtering together; key custody and revocation; secret rotation; compromise detection and aggregation; public snapshots and bucket policies; configuration history and API trails as evidence; shared responsibility boundaries for managed services; guardrails that cap rather than grant.
- Target skill: distinguish what AWS evidences from what the customer must evidence, and which service produces each.

### Exam 5 — Education and travel scenarios (65 items)
- Focus: benefits and economics again, now with per-second billing and data-transfer-out in the business case; reliability and agility for term start and booking peaks; microservices, automation and loose coupling; Well-Architected performance and sustainability; Cloud Adoption Framework business and security perspectives; migration choices; edge locations; disaster recovery objectives; EC2, Lambda, containers and managed platforms; storage tiers and lifecycle; databases for lookup, reporting and caching; load balancing, anycast and DNS failover; integration, analytics and developer tooling; monitoring and hybrid connectivity; pricing options, cost tools, billing structures, support plans, self-service resources and the Free Tier.
- Target skill: read the whole requirement before answering — several items turn on a clause such as "instantly available" or "no commitment".

### Exam 6 — Startup, gaming, and energy scenarios (65 items)
- Focus: launch-night elasticity; pay-as-you-go for pre-revenue teams; coupling and independent deploys; operational excellence and performance efficiency; platform and operations perspectives; replatform versus repurchase; Outposts for on-site control loops; recovery objectives at regional scope; shared patch awareness; grouped permissions and explicit denies; shared root as an anti-pattern; hardware MFA; federation and player identity; security groups, Shield and WAF; KMS and customer managed keys; certificate renewal; detection and vulnerability scanning; backups and lifecycle expiry; configuration and API evidence; service catalogues; containers and functions; shared file systems and intelligent tiering; key-value and in-memory stores; anycast and edge caching; fleet patching and health events; streams, queues and fan-out; foundation models and custom models; pipelines and tracing; templates and simple bundles; alarms and configuration history; dedicated links and central routing; Spot, Savings Plans, budgets, anomaly detection, consolidated billing, Business Support, the Solutions Library and the Free Tier.
- Target skill: answer with the smallest correct choice, then explain why the tempting alternative fails the constraint.

## Item formats and how to rehearse them

| Format | Per exam | How to practise |
|---|---:|---|
| Multiple choice | 55 | Decide before reading the options, then check which option matches your decision |
| Multiple response | 10 | Read the stated count first; treat each option as its own true/false question |

There are no sequencing, drag-and-drop or case-study items, because the published format has none.

## Suggested six-week schedule

| Week | Work | Time |
|---:|---|---|
| 1 | Read the landing page and curriculum; take Exam 1 untimed | ~2.5 h |
| 2 | Review every Exam 1 explanation; re-read the four domain maps; take Exam 2 untimed | ~3 h |
| 3 | Take Exam 3 untimed; start a one-page error log by domain | ~2.5 h |
| 4 | Take Exam 4 with a 100-minute clock; fix the two weakest domains | ~3 h |
| 5 | Take Exam 5 with a 95-minute clock; revise pricing and support vocabulary | ~3 h |
| 6 | Take Exam 6 under the full 90 minutes; review the error log only | ~2.5 h |

## Scoring your own attempt

- Score one point per item; a multiple-response item scores a point only when every correct option is selected and nothing else is.
- Record the score per domain, not only overall: a 60% overall with 40% in Billing is a different problem from an even 60%.
- AWS publishes a **minimum passing score of 700 on a scaled 100–1000 range**, applied to the 50 scored items with compensatory scoring. That 700 is a scaled score, not a percentage of 65, so no practice percentage here is an estimate of it.
- Treat any domain below 70% of its items as a study target, and treat a domain above 85% as something to re-verify once, not to skip.

## Time budget inside a 65-item exam

| Phase | Minutes | Notes |
|---|---:|---|
| Instructions and settling | 3 | Read the item-count and multiple-response rules once |
| First pass | 68 | ~63 seconds per item, answering everything; flag rather than stall |
| Second pass on flags | 12 | ~2 minutes for each of six flagged items |
| Final review | 7 | Check that multi-response items have exactly the stated count |

At 65 items in 90 minutes the average allowance is **83 seconds**. A first pass at 63 seconds leaves a real review margin, which is how the live appointment rewards discipline: unanswered items are marked incorrect and there is no penalty for guessing.

## What this course does not cover, on purpose

AWS lists **coding, architecture design, troubleshooting, implementation, and load and performance testing** as out of scope for CLF-C02. No item asks you to write code, design a multi-account architecture, debug a failing deployment, configure a service step by step, or run a performance test. There are also **no case studies**, because the published format has none.
