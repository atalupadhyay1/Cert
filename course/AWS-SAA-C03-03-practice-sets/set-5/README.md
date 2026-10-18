# AWS SAA-C03 Practice Set 5 — Domain 4 Cost-Optimized + GlobalBank

**200 questions** focused on **Design Cost-Optimized Architectures** with the GlobalBank case study.

## Stats
- **Total questions:** 200
- **Multi-select:** 40 (20%)
- **Domain coverage:**
  - Design Cost-Optimized Architectures: 200 (100%)
- **Case study:** GlobalBank (21 questions, see `case-study.md`)

## Topics covered
- **Pricing models & Reserved Instances** — Standard RIs, Convertible RIs, payment options, RI Marketplace, Zonal vs Regional, Zonal RIs, EC2 Capacity Blocks for ML, Scheduled RIs, Compute vs EC2 Instance Savings Plans, Savings Plan recommendations.
- **Spot Instances** — up to 90% discount, Spot Fleet diversification, interruption behaviors (stop/terminate/hibernate), Capacity Rebalancing, Spot mixed instances policies, suitable workloads.
- **S3 storage classes & lifecycle** — S3 Standard, Standard-IA, One Zone-IA, Glacier Instant Retrieval, Glacier Flexible Retrieval (Standard/Bulk/Expedited), Glacier Deep Archive, Intelligent-Tiering, Storage Class Analysis, lifecycle transitions, NoncurrentVersionExpiration, AbortIncompleteMultipartUpload, S3 Multi-Region Access Point, Requester Pays.
- **EBS cost optimization** — gp3 vs gp2, sc1/st1 for cold, EBS Snapshot Archive tier, Compute Optimizer, instance store for temp data.
- **Compute & serverless cost** — Lambda memory 128 MB-10,240 MB, GB-second billing, ARM/Graviton2, Compute SPs, Provisioned Concurrency trade-offs, SnapStart, Fargate Spot, Fargate vCPU/memory billing, AWS Batch, EKS pricing.
- **Database cost** — Aurora Serverless v2 ACU-second, DynamoDB On-Demand vs Provisioned+Reserved, DynamoDB Standard-IA, TTL, DAX, ElastiCache Memcached, RDS RIs, RDS Stop/Start, Redshift Serverless, Redshift RIs, Aurora Read Replicas.
- **Networking & data transfer** — free in, cross-AZ, cross-region, DX lower per-GB, VPC Endpoints (free for S3/DynamoDB), CloudFront, S3 Transfer Acceleration, NAT Gateway consolidation, DataSync, Snowball.
- **Cost management tools** — Cost Explorer (analysis, forecast, RI/SP recommendations), CUR, Budgets (Cost, Usage, Reservation, Savings Plans), Budget actions, Cost Anomaly Detection, Compute Optimizer, Cost Allocation Tags (activation), Pricing Calculator, Organizations Consolidated Billing, Tag Policies, SCPs.
- **Architecture patterns** — steady vs bursty traffic patterns, serverless vs provisioned, serverless event bus (EventBridge), Step Functions, SQS, SNS, Well-Architected Cost Optimization pillar.
- **GlobalBank case study** — CloudFront+S3 for static, Lambda for email, Aurora Serverless v2, Spot for daily jobs, S3 Lifecycle for 200 TB, Consolidated Billing for SPs, Budget actions to stop EC2, Cost Allocation Tags activation, ElastiCache offload, Compute Optimizer rightsizing, SCPs to restrict regions, S3 Lifecycle archive, Direct Connect for hybrid, DynamoDB On-Demand for sessions, Lambda Power Tuning.

## Files
- `practice-set-5.csv` — Udemy v2 bulk uploader template (200 rows, 17 cols).
- `set5_builder.py` — Python builder with the question bank, assertions (200 rows, 40 multi-select, 200 CostOptimized), and CSV writer.
- `case-study.md` — GlobalBank scenario (multinational bank, mainframe migration over 3 waves, FFIEC/PCI/SOX/GDPR, RTO 4 hr / RPO 15 min).

## How to rebuild
```bash
cd course/AWS-SAA-C03-03-practice-sets/set-5
python set5_builder.py
python ../../AWS-SAA-C03-04-resources/validate_csv.py practice-set-5.csv
```

## Format
- Header matches `AWS-SAA-C03-04-resources/udemy-v2-template.csv` exactly.
- All fields QUOTE_ALL with `\n` line terminator.
- Multi-select `Correct Answers` use 1-based comma-separated option ids.
- Per-option inline `Explanation N` and `Overall Explanation` end with an AWS docs reference URL.
- Domain string is exactly `Design Cost-Optimized Architectures` (case-sensitive).
