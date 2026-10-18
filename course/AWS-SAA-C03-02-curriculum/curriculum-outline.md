# AWS SAA-C03 Practice Test Course — Curriculum Outline & Strategy

> **Complete curriculum blueprint for all 6 practice test sets.** Each set is 200 questions, mapped to the official AWS SAA-C03 exam guide domains (skills measured as of 2026).

## 📊 OFFICIAL SAA-C03 EXAM DOMAIN BREAKDOWN

| Domain | Exam Weight | Practice Coverage |
|---|---|---|
| **Design Secure Architectures** | 30% | Sets 1, 2, 6 |
| **Design Resilient Architectures** | 26% | Sets 1, 3, 6 |
| **Design High-Performing Architectures** | 24% | Sets 1, 4, 6 |
| **Design Cost-Optimized Architectures** | 20% | Sets 1, 5, 6 |

> ℹ️ **Question Pool Logic:** Because Design Secure Architectures is 30% of the real exam, every set has **at least 40 Secure questions** (20% of 200). Sets 2-5 are domain deep dives; Set 6 is a full exam simulation at the real 30/26/24/20 weighting.

## 🗂️ PRACTICE TEST CURRICULUM OVERVIEW

```
📦 SAA-C03 Practice Test Suite (1200 Questions Total)
│
├── 🟦 SET 1 — Diagnostic Mixed (200q) + RetailCo Case Study
│
├── 🟩 SET 2 — Domain 1 Deep Dive: Secure Architectures (200q) + HealthFirst Case Study
│
├── 🟧 SET 3 — Domain 2 Deep Dive: Resilient Architectures (200q) + Streamify Case Study
│
├── 🟪 SET 4 — Domain 3 Deep Dive: High-Performing Architectures (200q) + StartupFast Case Study
│
├── 🟫 SET 5 — Domain 4 Deep Dive: Cost-Optimized Architectures (200q) + GlobalBank Case Study
│
└── 🟥 SET 6 — Full-Length Exam Simulation (200q, 30/26/24/20) + GameDay Case Study
```

## 📈 RECOMMENDED STUDY PATH

```
Day 1  →  Set 1 (Diagnostic + RetailCo)        →  200q, untimed, 130 min
Day 2  →  Set 2 (Secure + HealthFirst)          →  200q
Day 3  →  Set 3 (Resilient + Streamify)         →  200q
Day 4  →  Set 4 (High-Performing + StartupFast)  →  200q
Day 5  →  Set 5 (Cost-Optimized + GlobalBank)   →  200q
Day 6  →  Set 6 (Full Sim + GameDay)             →  200q, timed, 130 min
Day 7  →  Review all flagged questions          →  Re-take Sets with score < 80%
```

## 🎯 SET-BY-SET DETAIL

### 🟦 SET 1 — Diagnostic Mixed (200q) + RetailCo Case Study

**Purpose:** Establish a baseline score across all 4 SAA-C03 domains. Use this to identify your weak domains before drilling.

| Domain | Q Count | Real-exam weight |
|---|---|---|
| Design Secure Architectures | 60 | 30% |
| Design Resilient Architectures | 52 | 26% |
| Design High-Performing Architectures | 48 | 24% |
| Design Cost-Optimized Architectures | 40 | 20% |
| **Total** | **200** | **100%** |

**Case study:** RetailCo — a global online retailer migrating from a single-region to a multi-region architecture. Covers DynamoDB Global Tables, S3 cross-region replication, CloudFront, WAF, Shield, KMS, IAM, RDS Multi-AZ, Aurora Global Database, Route 53, and cost optimization with Savings Plans.

**Style:** 80% multiple-choice, 20% multi-select. Mix of definitional, comparative, and scenario-based.

---

### 🟩 SET 2 — Domain 1 Deep Dive: Secure Architectures (200q) + HealthFirst Case Study

**Purpose:** Drill the entire Security domain.

| Sub-Topic | Q Count |
|---|---|
| IAM users, groups, roles, policies (managed vs inline, JSON policy evaluation) | 20 |
| IAM cross-account access (role assumption, Organizations, SCPs) | 12 |
| AWS KMS (envelope encryption, customer-managed vs AWS-managed keys, key rotation) | 18 |
| S3 security (bucket policies, ACLs, Block Public Access, presigned URLs) | 16 |
| VPC security (security groups, NACLs, flow logs, PrivateLink, VPC endpoints) | 22 |
| AWS WAF and AWS Shield (Standard vs Advanced) | 12 |
| AWS Secrets Manager and Parameter Store | 10 |
| Amazon Cognito, AWS Directory Service, IAM Identity Center (SSO) | 14 |
| AWS CloudTrail, AWS Config, GuardDuty, Macie, Inspector | 22 |
| Encryption at rest vs in transit, TLS, mTLS, ACM | 12 |
| AWS network firewall, Route 53 Resolver DNS firewall | 8 |
| Cross-cutting security (Shared Responsibility, compliance) | 14 |
| Case study questions (HealthFirst) | 20 |

**Case study:** HealthFirst — a HIPAA-compliant patient portal. Covers HIPAA-eligible services, encryption at rest/in transit, KMS key policies, audit logging with CloudTrail + S3 Object Lock, VPC isolation, IAM Identity Center for clinician SSO, WAF for the patient portal, and DR with cross-region backup.

**Recommended time:** 130 minutes.

---

### 🟧 SET 3 — Domain 2 Deep Dive: Resilient Architectures (200q) + Streamify Case Study

**Purpose:** Drill the entire Resiliency domain.

| Sub-Topic | Q Count |
|---|---|
| Multi-AZ design patterns (RDS Multi-AZ, EFS, ALB, ASG) | 22 |
| Multi-Region design patterns (active-active, active-passive, pilot light) | 20 |
| DR strategies (backup-restore, pilot light, warm standby, multi-site) and RTO/RPO | 18 |
| S3 cross-region replication, S3 same-region replication, S3 Batch Replication | 14 |
| RDS read replicas, Multi-AZ, Aurora Global Database, DynamoDB Global Tables | 20 |
| Route 53 routing policies (latency, failover, weighted, geolocation, geoproximity) | 14 |
| Decoupling: SQS, SNS, EventBridge, Kinesis | 18 |
| Auto Scaling, ELB, target tracking, scheduled scaling | 12 |
| AWS Backup, snapshots, point-in-time recovery | 10 |
| AWS Global Accelerator, CloudFront failover | 8 |
| Well-Architected Reliability pillar | 6 |
| Cross-cutting: monitoring, recovery testing | 8 |
| Case study questions (Streamify) | 30 |

**Case study:** Streamify — real-time video analytics. Covers Kinesis for ingestion, Lambda vs ECS for inference, multi-AZ processing, S3 lifecycle for raw video, DynamoDB for metrics, CloudFront for live dashboard, Route 53 for global failover, and cost optimization with Spot for spiky GPU workload.

**Recommended time:** 130 minutes.

---

### 🟪 SET 4 — Domain 3 Deep Dive: High-Performing Architectures (200q) + StartupFast Case Study

**Purpose:** Drill the entire High-Performance domain.

| Sub-Topic | Q Count |
|---|---|
| EC2 instance families (general, compute, memory, storage, accelerated) and placement groups | 22 |
| AWS Lambda, AWS Fargate, AWS Batch, Amazon EKS | 20 |
| EBS volume types (gp3, io2, st1, sc1) and RAID | 14 |
| S3 performance (multipart, transfer acceleration, request rate) and storage class selection | 14 |
| EFS, FSx (Windows, Lustre, NetApp ONTAP), Instance Store | 12 |
| RDS performance, Aurora, Aurora Serverless, read replicas | 14 |
| DynamoDB (partition keys, DAX, adaptive capacity, streams, global tables) | 18 |
| ElastiCache (Redis vs Memcached), DAX, CloudFront caching | 14 |
| CloudFront, Global Accelerator, Route 53 latency-based routing | 14 |
| Redshift, Athena, EMR, Kinesis Data Analytics, OpenSearch | 14 |
| Networking (VPC design, hybrid connectivity, Transit Gateway) | 12 |
| Generative AI services (Bedrock, Q, SageMaker) — 2026 refresh | 6 |
| Case study questions (StartupFast) | 26 |

**Case study:** StartupFast — a cost-optimized SaaS. Covers right-sizing, Compute Optimizer, Savings Plans, S3 Intelligent-Tiering, NAT gateway alternatives, multi-AZ vs single-AZ trade-offs, and cost-performance trade-offs.

**Recommended time:** 130 minutes.

---

### 🟫 SET 5 — Domain 4 Deep Dive: Cost-Optimized Architectures (200q) + GlobalBank Case Study

**Purpose:** Drill the entire Cost Optimization domain.

| Sub-Topic | Q Count |
|---|---|
| EC2 pricing models (On-Demand, Reserved, Savings Plans, Spot, Dedicated, Capacity Reservations) | 26 |
| Savings Plans vs Reserved Instances trade-offs | 16 |
| Spot Fleet, Spot Instances, EC2 Auto Scaling with Spot | 16 |
| S3 storage classes, lifecycle policies, Intelligent-Tiering, Glacier | 22 |
| Data transfer cost optimization (CloudFront, VPC endpoints, PrivateLink) | 16 |
| Right-sizing with Compute Optimizer, Cost Explorer, Trusted Advisor | 14 |
| Managed service cost trade-offs (RDS vs DynamoDB, Lambda vs EC2, Fargate vs EC2) | 14 |
| AWS Cost Explorer, Cost Allocation Tags, AWS Budgets, Cost Anomaly Detection | 16 |
| Multi-account cost allocation, AWS Organizations, consolidated billing | 12 |
| Cost optimization for containers (Fargate Spot, EKS), serverless (Lambda), databases (Aurora Serverless) | 12 |
| Storage cost optimization (EBS gp3, EFS IA, S3 Glacier) | 10 |
| Networking cost optimization (NAT gateway, VPC endpoint, CloudFront) | 6 |
| Case study questions (GlobalBank) | 20 |

**Case study:** GlobalBank — a hybrid cloud migration of core banking. Covers Direct Connect vs VPN, Transit Gateway, hybrid DNS, multi-account strategy with AWS Organizations, cost allocation across business units, and DR cost trade-offs.

**Recommended time:** 130 minutes.

---

### 🟥 SET 6 — Full-Length Exam Simulation (200q) + GameDay Case Study

**Purpose:** Mirror the real SAA-C03 exam. Complete in 130 minutes under exam conditions.

| Domain | Q Count | Real-exam weight |
|---|---|---|
| Design Secure Architectures | 60 | 30% |
| Design Resilient Architectures | 52 | 26% |
| Design High-Performing Architectures | 48 | 24% |
| Design Cost-Optimized Architectures | 40 | 20% |
| **Total** | **200** | **100%** |

**Case study:** GameDay — a serverless live sports platform. Covers CloudFront for HLS, API Gateway WebSocket for chat, Lambda for real-time processing, DynamoDB for scores, S3 + CloudFront for VOD, Cognito for auth, Global Accelerator, and Lambda + Fargate Spot for batch processing.

**Difficulty profile:** 80% multiple-choice, 20% multi-select. 40% scenario-based. 30% comparison questions. 30% definitional.

**Recommended time:** 130 minutes (set a timer — pacing matters for the real exam).

---

## ✅ What makes these questions exam-grade

- **All distractors are real AWS services, features, or pricing models** — no fictional answers
- **Per-option inline explanations** explain *why* each distractor is wrong
- **Comprehensive Overall Explanations** link to AWS documentation URLs
- **Domain strings** match the official AWS SAA-C03 exam guide exactly
- **Multi-select questions** at 20% per set, matching the real exam
- **6 case studies** with 20-30 case-study questions per set, exactly like the real exam
- **Udemy v2 Bulk Question Uploader compatible** — drop the CSV straight in

## 🎯 Suggested pre-study before taking these tests

1. Complete AWS Cloud Practitioner essentials (if you are new to AWS): <https://aws.amazon.com/getting-started/cloud-essentials/>
2. Review the official SAA-C03 exam guide: <https://docs.aws.amazon.com/aws-certification/latest/solutions-architect-associate-03/solutions-architect-associate-03.html>
3. Read the AWS Well-Architected Framework: <https://aws.amazon.com/architecture/well-architected/>
4. Hands-on with the AWS Free Tier: <https://aws.amazon.com/free/>

---

**Source:** Official AWS SAA-C03 exam guide, as of 2026. Validate at <https://docs.aws.amazon.com/aws-certification/latest/solutions-architect-associate-03/solutions-architect-associate-03.html>.
