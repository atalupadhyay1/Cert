# Official sources and coverage notes

Reviewed October 2026 against the exam guide (v1.2) and the certification page. Product names, preview status, and prices change, and the certification page warns that the exam will soon be updated for recent branding changes, so re-check the guide before publishing or scheduling.

## Primary references

| Purpose | URL |
|---|---|
| Certification page (length, fee, format, languages, prerequisites, renewal pointer) | https://cloud.google.com/learn/certification/cloud-database-engineer |
| Exam guide (four sections and their weights) | https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf |
| Database services overview | https://cloud.google.com/products/databases |
| Cloud SQL documentation | https://cloud.google.com/sql/docs |
| Cloud SQL high availability | https://cloud.google.com/sql/docs/mysql/high-availability |
| Cloud SQL backups and point-in-time recovery | https://cloud.google.com/sql/docs/mysql/backup-recovery/backups |
| Cloud SQL Auth Proxy and connectors | https://cloud.google.com/sql/docs/mysql/connect-auth-proxy |
| Cloud SQL IAM database authentication | https://cloud.google.com/sql/docs/mysql/authentication |
| AlloyDB overview | https://cloud.google.com/alloydb/docs/overview |
| AlloyDB read pool | https://cloud.google.com/alloydb/docs/read-pool-overview |
| AlloyDB cross-region replication | https://cloud.google.com/alloydb/docs/cross-region-replication |
| AlloyDB vector search | https://cloud.google.com/alloydb/docs/ai/vector-search-overview |
| Spanner overview | https://cloud.google.com/spanner/docs/overview |
| Spanner multi-region configurations | https://cloud.google.com/spanner/docs/instance-configurations |
| Spanner backups and point-in-time recovery | https://cloud.google.com/spanner/docs/backup |
| Spanner processing units and autoscaling | https://cloud.google.com/spanner/docs/compute-capacity |
| Bigtable overview | https://cloud.google.com/bigtable/docs/overview |
| Bigtable app profiles and routing | https://cloud.google.com/bigtable/docs/app-profiles |
| Bigtable replication | https://cloud.google.com/bigtable/docs/replication-overview |
| Bigtable garbage collection | https://cloud.google.com/bigtable/docs/garbage-collection |
| Firestore overview | https://cloud.google.com/firestore/docs/overview |
| Memorystore overview | https://cloud.google.com/memorystore/docs/redis/redis-overview |
| Database Migration Service | https://cloud.google.com/database-migration/docs |
| Database Migration Service conversion workspaces | https://cloud.google.com/database-migration/docs/oracle-to-postgresql/quickstart-guide |
| Datastream | https://cloud.google.com/datastream/docs |
| Private Service Connect | https://cloud.google.com/vpc/docs/private-service-connect |
| Cloud KMS and CMEK | https://cloud.google.com/kms/docs/cmek |
| Cloud Audit Logs | https://cloud.google.com/logging/docs/audit |
| Log routing and locked buckets | https://cloud.google.com/logging/docs/routing/overview |
| Cloud Monitoring alerting | https://cloud.google.com/monitoring/alerts |
| Query Insights | https://cloud.google.com/sql/docs/mysql/using-query-insights |
| Database Center | https://cloud.google.com/database-center/docs/overview |
| VPC Service Controls | https://cloud.google.com/vpc-service-controls/docs/overview |
| Organization policy constraints | https://cloud.google.com/resource-manager/docs/organization-policy/overview |
| BigQuery federated queries | https://cloud.google.com/bigquery/docs/federated-queries-intro |
| BigQuery export from operational databases | https://cloud.google.com/bigquery/docs/loading-data-cloud-sql |

## Verified exam facts

| Fact | Value |
|---|---|
| Domains and weights | 1) Design innovative, scalable, and highly available cloud database solutions ~32%; 2) Manage a solution that can span multiple database technologies ~25%; 3) Migrate data solutions ~23%; 4) Deploy scalable and highly available databases in Google Cloud ~20% |
| Length | Two hours |
| Fee | $200 USD plus applicable tax |
| Question count | 50–60 multiple-choice and multiple-select questions (Google's published range) |
| Languages | English, Japanese |
| Prerequisites | None; Google recommends 5+ years of overall database and IT experience including 2 years of hands-on Google Cloud database solutions |
| Case studies | None — the published format has no case-study component |
| Passing score | Not published by Google |
| Renewal | Described by Google only by reference to its Renewal FAQs; no duration or fee is restated here |
| Configuration objective | Present — the guide asks about HA and DR topology, connection and security configuration, backup and recovery design, replication, and provisioning automation |

## Coverage mapping

| Official section | Local domain | Local skills | Items per exam | Items in bank |
|---|---|---:|---:|---:|
| 1. Design innovative, scalable, and highly available cloud database solutions (~32%) | 1 | 1.1–1.16 | 32 | 192 |
| 2. Manage a solution that can span multiple database technologies (~25%) | 2 | 2.1–2.16 | 25 | 150 |
| 3. Migrate data solutions (~23%) | 3 | 3.1–3.10 | 23 | 138 |
| 4. Deploy scalable and highly available databases in Google Cloud (~20%) | 4 | 4.1–4.9 | 20 | 120 |
| **Total** | | **51 skills** | **100** | **600** |

The weights are approximate in Google's wording but total exactly 100%, so the item counts are the weights themselves. No rounding correction was applied and no tolerance band exists in the build: a revision that breaks the 100% total fails the build.

Sections 3 and 4 publish only one objective each, so the local study map subdivides them into decision-level areas — migration strategy, tool selection, conversion, load and catch-up, validation, cutover, fallback, and decommissioning for section 3; provisioning, testing, replication, read scaling, automation, monitoring, failover mechanics, routing, and headroom for section 4. Those local IDs are study aids, not Google objective numbers.

## What is deliberately not covered

- **Case studies.** Not part of the published format.
- **Console walkthroughs.** Configuration judgement is tested, but as a decision and its consequence, never as a click path. Nothing here needs a live project.
- **Hands-on labs and interactive item formats.** Not representable in a CSV, and not part of the published format.
- **Renewal-exam calibration.** This bank targets the standard exam; Google's renewal instrument is a separate paper with its own scope.
- **Engine-internals trivia.** Very deep query-planner or storage-format detail is out of scope; the guide's objectives are about design, management, migration and deployment decisions.

## Source discipline

- No question, option, or explanation is copied from any question-sharing site, braindump collection, or community forum. The ExamTopics listing for this exam was checked only for how items are *presented* — scenario length, "which should the team do" phrasing, and the multiple-select convention — never as a source of item text.
- Community statistics from such sites — question counts, self-reported pass rates, "same as the real exam" claims — are **not** used as evidence, benchmarks, or marketing claims anywhere in this course.
- The frequently repeated third-party claim that this exam requires "about 70%" to pass is **not** Google's and does not appear in this package. Google does not publish a passing score.
- Where Google publishes a range (50–60 questions) or declines to publish a value (the passing score), this course repeats the range or says the value is unpublished. It never fills the gap with an estimate of its own.
- Product names follow the October 2026 guide. Terms were not invented for products that do not exist, and older names were not carried forward in place of current ones.
