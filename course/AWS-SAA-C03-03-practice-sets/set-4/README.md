# AWS SAA-C03 Practice Set 4 — Domain 3 High-Performing + StartupFast

**200 questions** focused on **Design High-Performing Architectures** with the StartupFast case study.

## Stats
- **Total questions:** 200
- **Multi-select:** 40 (20%)
- **Domain coverage:**
  - Design High-Performing Architectures: 200 (100%)
- **Case study:** StartupFast (20 questions, see `case-study.md`)

## Topics covered
- **EC2 instance families & placement** — R, C, M, T, P, I, X; placement groups (cluster, spread, partition); Nitro System; Graviton; IMDSv2; EFA; ENA; Dedicated Hosts; instance store; capacity reservations; Spot Fleet; hibernation; scheduled scaling.
- **Serverless & containers** — Lambda SnapStart, reserved/provisioned concurrency, layers, function URLs, event source mappings; ECS launch types (EC2, Fargate, External), task placement strategies, service auto scaling, Service Connect, Cloud Map integration; EKS managed node groups, self-managed nodes, Fargate, EKS Anywhere; ECR; AWS Batch managed compute environments.
- **EBS & instance storage** — gp2, gp3, io1, io2, io2 Block Express, st1, sc1; Multi-Attach; Fast Snapshot Restore; Elastic Volumes; RAID 0; snapshots; placement groups.
- **S3 performance & storage classes** — multipart upload, byte-range fetches, Transfer Acceleration, S3 Select, S3 Inventory, Glacier tiers, Intelligent-Tiering, Storage Class Analysis, lifecycle, request rate scaling per prefix, SSE-C.
- **EFS & FSx** — EFS Standard / IA / Archive, throughput modes (bursting, provisioned, elastic), performance modes (general purpose, max I/O); FSx for Windows File Server, Lustre (persistent, scratch), ONTAP, OpenZFS; FSx for Lustre S3 integration.
- **Databases** — DynamoDB DAX, hot partitions, adaptive capacity, partition keys, global tables; Aurora Serverless v2; Neptune (graph); Timestream (time-series); MemoryDB for Redis; RDS read replicas; Aurora Global Database.
- **Caching / CDN / Networking** — ElastiCache Redis / Memcached / Valkey; CloudFront behaviors, origins, Origin Shield, OAC, price classes, invalidation; AWS Global Accelerator; Direct Connect; DataSync; VPC performance; Kinesis Data Streams, Kinesis Data Analytics (managed Flink), MSK (managed Kafka), enhanced fan-out.
- **Analytics & GenAI** — Redshift, Athena, EMR, KDA, OpenSearch / OpenSearch Serverless, Bedrock (FMs, RAG, fine-tuning), Amazon Q, SageMaker, MWAA, Lake Formation, Glue, Textract, Rekognition, Comprehend.
- **StartupFast case study** — Compute Optimizer, Aurora Serverless, ElastiCache, S3 lifecycle, CloudFront, Savings Plans, Spot, Lambda billing, DynamoDB on-demand, Cost Explorer, Budgets, Cost Anomaly Detection, cost allocation tags, RDS read replicas, EKS, Bedrock, OpenSearch, plus scenario-driven high-performance optimizations.

## Files
- `practice-set-4.csv` — Udemy v2 bulk uploader template (200 rows, 17 cols).
- `set4_builder.py` — Python builder with the question bank, assertions (200 rows, 40 multi-select, 200 HighPerforming), and CSV writer.
- `case-study.md` — StartupFast scenario (40% AWS cost reduction, 99.9% target SLA, 200 customers, over-provisioned EC2/RDS).

## How to rebuild
```bash
cd course/AWS-SAA-C03-03-practice-sets/set-4
python set4_builder.py
python ../../AWS-SAA-C03-04-resources/validate_csv.py practice-set-4.csv
```

## Format
- Header matches `AWS-SAA-C03-04-resources/udemy-v2-template.csv` exactly.
- All fields QUOTE_ALL with `\n` line terminator.
- Multi-select `Correct Answers` use 1-based comma-separated option ids.
- Per-option inline `Explanation N` and `Overall Explanation` end with an AWS docs reference URL.
- Domain string is exactly `Design High-Performing Architectures` (case-sensitive).
