# Google Cloud Professional Cloud Database Engineer — Full-Length Mock Exam 6

Professional Cloud Database Engineer · 100 questions · expanded practice bank · passing score not published

Blueprint-weighted mock exam. Item mix: 84 multiple-choice and 16 multiple-select items (the selection count is stated in each multi-select stem). The live exam publishes 50-60 multiple-choice and multiple-select questions and has no case-study component, so this set is larger on purpose and no case-study item is reproduced. The live paper allows two hours for 50-60 items, so this 100-item set is a slower-per-item rehearsal: about 72 seconds per item here against roughly 120-144 seconds live. Use it to build a habit of finishing with time to review. See the README for the exact fidelity boundary.

Original educational content, not actual, recalled, or copied Google exam items.

## Questions

---

## Domain 1 — Design Innovative, Scalable, and Highly Available Cloud Database Solutions (Sizing, Availability Design, and Database Selection)

### 1. A design review asks how the team will size its database at launch, and one year of a comparable service's metrics is available. What should the answer be?

- A. Commit to the steady baseline capacity
- B. Reserve headroom above the measured peak
- C. Load-test the workload to derive the size
- D. Size the instance from the observed peak metrics

### 2. A seasonal retailer's traffic quadruples for six weeks each year, and the rest of the year is flat. What must the chosen shape cover?

- A. Size the instance from the observed peak metrics
- B. Reduce the machine type to match observed use
- C. Reserve headroom above the measured peak
- D. Stop or delete the idle instance

### 3. A review finds the same instance short of memory and short of disk throughput at peak. Which two changes address both? Select two.

- A. Increase the machine type of the instance
- B. Add a read replica for the read traffic
- C. Move the data to SSD storage
- D. Put a session pooler in front of the instance
- E. Increase the disk size to raise throughput

### 4. A review finds a Bigtable cluster's p99 misses its target on HDD while the key distribution is balanced. What should the team change?

- A. Move the data to SSD storage
- B. Add nodes to the Bigtable cluster
- C. Move the data to HDD storage
- D. Set the garbage-collection policy on the column family

### 5. A design review wants database compute that follows a weekly curve automatically instead of a fixed size. What should the team enable?

- A. Add processing units to the Spanner instance
- B. Enable autoscaling on the instance
- C. Increase the machine type of the instance
- D. Add nodes to the Bigtable cluster

### 6. A Bigtable cluster shows rising CPU as data grows, and its access pattern is already well distributed. What should the team do?

- A. Move the data to SSD storage
- B. Add processing units to the Spanner instance
- C. Change the row-key design
- D. Add nodes to the Bigtable cluster

### 7. A design review asks for automatic recovery from the loss of one zone with no cross-region requirement. Which choice fits?

- A. Add a cross-region read replica
- B. Choose a multi-region instance configuration
- C. Run a single zonal instance
- D. Enable regional high availability with a standby zone

### 8. A review requires Spanner writes to continue when a region is lost, without an operator promoting anything. Which choice fits?

- A. Enable regional high availability with a standby zone
- B. Add a cross-region read replica
- C. Restore the backup into the second region
- D. Choose a multi-region instance configuration

### 9. A review wants AlloyDB reads served in a second region today and a promotion path for later. Which choice fits?

- A. Run a single zonal instance
- B. Add a secondary cluster in the second region
- C. Add nodes to the read pool
- D. Restore the backup into the second region

### 10. A review asks how patching will be scheduled and how one protected week will be kept clear. Which two controls deliver that? Select two.

- A. Schedule the maintenance window in the low-traffic period
- B. Perform an in-place major version upgrade
- C. Run a controlled failover test
- D. Set a deny maintenance period over the peak event
- E. Take a backup before the upgrade

### 11. A review asks which hour the monthly engine patch will land in, and when users will be told. Which setting answers that?

- A. Set a deny maintenance period over the peak event
- B. Take a backup before the upgrade
- C. Perform an in-place major version upgrade
- D. Schedule the maintenance window in the low-traffic period

### 12. A security review requires no public database address and no stored database passwords. Which two controls are needed? Select two.

- A. Keep a database password in the connection string
- B. Enable IAM database authentication
- C. Add the client range to authorized networks
- D. Connect over private IP inside the VPC
- E. Use the public IP with enforced SSL

### 13. A review must let engineers connect from home without a public address and without a site-to-site link. Which option fits?

- A. Add the client range to authorized networks
- B. Publish the instance behind Private Service Connect
- C. Use the public IP with enforced SSL
- D. Connect through the Cloud SQL Auth Proxy

### 14. A review requires that the company be able to destroy the key protecting a database on demand. Which control fits?

- A. Encrypt with a customer-managed key in Cloud KMS
- B. Rely on Google-managed encryption keys
- C. Route the audit logs to a locked log bucket
- D. Enable Data Access audit logs

### 15. A review requires annual key rotation while older backups remain restorable. What should the team configure?

- A. Rely on Google-managed encryption keys
- B. Rotate the customer-managed key on a schedule
- C. Add the projects to a VPC Service Controls perimeter
- D. Encrypt with a customer-managed key in Cloud KMS

### 16. A review must stop connection refusals this quarter while a pooling rollout finishes next quarter. Which two actions fit? Select two.

- A. Increase the machine type of the instance
- B. Fix the connection leak in the application
- C. Raise the max_connections database flag
- D. Increase the machine tier to allow more connections
- E. Put a session pooler in front of the instance

### 17. A review finds sessions abandoned on error paths, so the count climbs until new connections fail. What should the team fix?

- A. Raise the max_connections database flag
- B. Fix the connection leak in the application
- C. Put a session pooler in front of the instance
- D. Increase the machine type of the instance

### 18. A review asks how the team will show who read sensitive rows last month. Which control provides that?

- A. Route the audit logs to a locked log bucket
- B. Rely on Admin Activity audit logs
- C. Enable Data Access audit logs
- D. Build a log-based metric from the error entries

### 19. A review requires audit evidence that no project owner can delete for three years. What should the team configure?

- A. Review the fleet in Database Center
- B. Route the audit logs to a locked log bucket
- C. Rely on Admin Activity audit logs
- D. Enable Data Access audit logs

### 20. A review compares operational burden for a 150-gigabyte relational workload with no cross-region need. Which choice is lightest?

- A. Run the database on Compute Engine yourself
- B. Use Cloud SQL for the relational workload
- C. Use Spanner for the globally distributed relational workload
- D. Use AlloyDB for the demanding relational workload

### 21. A review must keep an engine operated by the vendor that already supports it, on Google Cloud infrastructure. Which deployment fits?

- A. Run the database on bare metal solution
- B. Use Cloud SQL for the relational workload
- C. Use a partner-managed database offering
- D. Run the database on Compute Engine yourself

### 22. A review covers an event stream that needs very high key-based write throughput and analysts who need the same data in the warehouse. Which two choices fit? Select two.

- A. Use Bigtable for the high-throughput wide-column workload
- B. Use Firestore for the document workload
- C. Use Cloud SQL for the relational workload
- D. Export the table into BigQuery
- E. Use Memorystore as the caching tier

### 23. A review requires globally consistent transactions with horizontal write scaling and no application sharding. Which database fits?

- A. Use Spanner for the globally distributed relational workload
- B. Use Cloud SQL for the relational workload
- C. Use Firestore for the document workload
- D. Use Bigtable for the high-throughput wide-column workload

### 24. A review covers a mobile product needing offline edits, per-document queries, and managed replication. Which database fits?

- A. Use Memorystore as the caching tier
- B. Use Bigtable for the high-throughput wide-column workload
- C. Use Cloud SQL for the relational workload
- D. Use Firestore for the document workload

### 25. A review must serve filtered similarity search over sixty million embeddings at low latency on AlloyDB. Which choice fits?

- A. Enable the vector extension on PostgreSQL
- B. Add the composite index for the query
- C. Use AlloyDB vector search with a ScaNN index
- D. Cache the hot read path in Memorystore

### 26. A review wants similarity search inside the existing Cloud SQL for PostgreSQL service with three million embeddings. Which choice fits?

- A. Use AlloyDB vector search with a ScaNN index
- B. Export the table into BigQuery
- C. Enable the vector extension on PostgreSQL
- D. Query the source through BigQuery federated queries

### 27. A review finds a fixed estate running at constant load and paid on demand all year. What should the team do?

- A. Scale down outside business hours
- B. Stop or delete the idle instance
- C. Commit to the steady baseline capacity
- D. Rely on sustained-use discounts

### 28. A review finds estate traffic drops eighty percent overnight while every shape stays constant. What should the team do?

- A. Reduce the machine type to match observed use
- B. Scale down outside business hours
- C. Reserve capacity for the peak season
- D. Stop or delete the idle instance

### 29. A review finds three hundred queries relying on vendor-specific behaviour and a delivery date eight weeks away. What should it recommend?

- A. Use Database Migration Service with schema conversion
- B. Choose the target engine with the cheapest conversion
- C. Keep the current engine and version
- D. Write to both systems from the application

### 30. A review must keep data inside one country and block copying it into unapproved projects. Which two controls are needed? Select two.

- A. Place the instance in the required region
- B. Rely on Google-managed encryption keys
- C. Enforce the location with an organization policy
- D. Add the projects to a VPC Service Controls perimeter
- E. Cache the hot read path in Memorystore

### 31. A review must place a single Cloud SQL instance inside the required country for a regulator. What should the team do?

- A. Encrypt with a customer-managed key in Cloud KMS
- B. Place the instance in the required region
- C. Enforce the location with an organization policy
- D. Add the projects to a VPC Service Controls perimeter

### 32. A review must keep a contracted on-premises system for four years while new services query it. Which approach fits?

- A. Keep part of the estate on-premises with a hybrid link
- B. Query the source through BigQuery federated queries
- C. Export the table into BigQuery
- D. Decommission the source after a parallel period

---

## Domain 2 — Manage a Solution That Can Span Multiple Database Technologies (Operations, Access, Backup, and Performance)

### 33. A review must authorize an application through identity and end access by removing a group membership. Which two controls achieve that? Select two.

- A. Enable IAM database authentication
- B. Grant the basic editor role
- C. Share one application database user
- D. Keep a database password in the connection string
- E. Bind access to a Google group

### 34. A review finds a read-only reporting bot holding the instance administrator role. What should the team change?

- A. Grant the predefined database role
- B. Grant a custom role limited to the needed permissions
- C. Grant the basic editor role
- D. Create one database user per person

### 35. A review requires each analyst's queries to be attributable to them personally. What should the team do?

- A. Share one application database user
- B. Keep a database password in the connection string
- C. Create one database user per person
- D. Have the application authenticate as a service account

### 36. A review finds a lookup on a selective column scanning four million rows and returning two. What should the team do?

- A. Partition the large table
- B. Raise the per-operation memory flag
- C. Add the index the slow query needs
- D. Refresh the table statistics

### 37. A review must establish why a statement changed plan after a schema edit. What should the team examine?

- A. Read the query plan for the statement
- B. Refresh the table statistics
- C. Drop the unused index
- D. Add the index the slow query needs

### 38. A review covers both an unexplained stall and a batch that locks a table for minutes. Which two actions address them? Select two.

- A. Terminate the session that holds the lock
- B. Inspect lock waits and blocking sessions
- C. Add the index the slow query needs
- D. Refresh the table statistics
- E. Batch the writes into fewer round trips

### 39. A review finds one idle transaction holding locks for half an hour while every write queues. What should the team do?

- A. Inspect lock waits and blocking sessions
- B. Terminate the session that holds the lock
- C. Send reporting queries to the read replica
- D. Batch the writes into fewer round trips

### 40. A review must separate a memory shortage from a storage wait during a benchmark. Which view answers that?

- A. Use Query Insights to find the heavy statements
- B. Review the fleet in Database Center
- C. Read the slow query log
- D. Watch CPU, memory, disk, and IOPS together

### 41. A review needs per-statement wait categories rather than a single latency number. Which tool provides that?

- A. Watch CPU, memory, disk, and IOPS together
- B. Read the slow query log
- C. Build a log-based metric from the error entries
- D. Use Query Insights to find the heavy statements

### 42. A review finds six jobs starting at midnight and colliding on a concurrency limit they do not need to share. What should the team do?

- A. Retry the failed operation with exponential backoff
- B. Export the table to CSV in Cloud Storage
- C. Move the job outside the contention window
- D. Request a quota increase for the project

### 43. A review finds pages firing on resource thresholds while failed statements go unreported. What should the team add?

- A. Use Query Insights to find the heavy statements
- B. Create an alerting policy on the metric
- C. Alert on replication lag
- D. Alert on the database error rate

### 44. A review finds a recurring error message in the log that nobody counts or charts. What should the team build?

- A. Build a log-based metric from the error entries
- B. Alert when the instance is unreachable
- C. Route the audit logs to a locked log bucket
- D. Read the slow query log

### 45. A review requires both a recovery point measured in minutes and a managed backup schedule. Which two capabilities does it need? Select two.

- A. Clone the instance for the test
- B. Enable automated backups with a retention window
- C. Enable point-in-time recovery
- D. Extend the backup retention window
- E. Take an on-demand backup before the change

### 46. A review wants a risky schema change tested against production data without touching production. What should the team do?

- A. Export a logical dump to Cloud Storage
- B. Clone the instance for the test
- C. Take an on-demand backup before the change
- D. Restore to the timestamp before the bad change

### 47. A review requires a portable export that can be restored into another instance of the same engine. What should the team take?

- A. Export a logical dump to Cloud Storage
- B. Export the table to CSV in Cloud Storage
- C. Query the source through BigQuery federated queries
- D. Import the dump into the target instance

### 48. A review cannot approve a recovery design until the acceptable data loss is written down. What should the team produce?

- A. Enable point-in-time recovery
- B. Clone the instance for the test
- C. Design the restore path to the stated RTO and RPO
- D. Enable automated backups with a retention window

### 49. A review must confirm the platform can return an instance to eleven minutes ago after a faulty batch. Which capability fits?

- A. Clone the instance for the test
- B. Restore to the timestamp before the bad change
- C. Run a controlled failover test
- D. Export a logical dump to Cloud Storage

### 50. A review must bound the versions each Bigtable row keeps while preserving thirteen months of history. What should the team configure?

- A. Set the garbage-collection policy on the column family
- B. Set a time-to-live policy on the collection
- C. Apply a row-level retention policy
- D. Archive closed rows to cheaper storage

### 51. A review must scale read capacity and route the read traffic to it. Which two actions deliver that? Select two.

- A. Send reporting queries to the read replica
- B. Shard the data across several instances
- C. Add a read replica for the read traffic
- D. Add processing units to the Spanner instance
- E. Increase the machine type of the instance

### 52. A review finds a write-heavy instance saturated, and the application cannot change for two quarters. What should the team do?

- A. Increase the machine type of the instance
- B. Add a read replica for the read traffic
- C. Send reporting queries to the read replica
- D. Cache the hot read path in Memorystore

### 53. A review accepts a read-mostly second region, provided the copy stays current enough to promote inside the hour. What should the team add?

- A. Add a secondary cluster in the second region
- B. Restore the backup into the second region
- C. Choose a multi-region instance configuration
- D. Add a cross-region read replica

### 54. A review finds six indexes on an order table that no query uses, while insert latency grows. What should the team do?

- A. Partition the large table
- B. Raise the per-operation memory flag
- C. Add the index the slow query needs
- D. Drop the unused index

### 55. A review must guarantee monthly maintenance runs with nobody present. What should the team configure?

- A. Provision the instance once by hand
- B. Run a controlled failover test
- C. Take an on-demand backup before the change
- D. Run the task on a managed schedule

### 56. A review must confirm an engine upgrade will not break the application before production sees it. What should the team do?

- A. Perform an in-place major version upgrade
- B. Watch the error rate after the change
- C. Test the upgrade on a clone first
- D. Take a backup before the upgrade

### 57. A review asks how the team will show that availability met the committed objective each month. What should it track?

- A. Create an alerting policy on the metric
- B. Review the fleet in Database Center
- C. Track the availability signal against the agreed objective
- D. Watch CPU, memory, disk, and IOPS together

---

## Domain 3 — Migrate Data Solutions (Migration Strategy, Conversion, and Cutover)

### 58. A review of a 900 GB MySQL migration requires minutes of downtime and a documented decision path. Select two.

- A. Dump, restore, then replay the changes
- B. Accept a scheduled extended outage
- C. Use Database Migration Service for the same engine
- D. Follow a cutover runbook with a rollback step
- E. Write to both systems from the application

### 59. A review accepts a full weekend outage for an internal tool holding eleven gigabytes. Which strategy is simplest?

- A. Follow a cutover runbook with a rollback step
- B. Write to both systems from the application
- C. Accept a scheduled extended outage
- D. Use Database Migration Service for the same engine

### 60. A review finds the source cannot publish its change stream, yet writes must continue during the move. Which approach fits?

- A. Accept a scheduled extended outage
- B. Write to both systems from the application
- C. Freeze writes during the cutover
- D. Use Database Migration Service for the same engine

### 61. A review must convert an Oracle schema and its procedural code into PostgreSQL while moving the data. Which tool fits?

- A. Use Database Migration Service for the same engine
- B. Stream changes with Datastream
- C. Use Database Migration Service with schema conversion
- D. Dump, restore, then replay the changes

### 62. A review needs MySQL changes in BigQuery continuously with the source left in production. Which tool fits?

- A. Export a logical dump to Cloud Storage
- B. Use Database Migration Service with schema conversion
- C. Export the table into BigQuery
- D. Stream changes with Datastream

### 63. A review needs a one-time copy of a twelve-gigabyte database into a test project. Which approach fits?

- A. Apply the captured change backlog before cutover
- B. Use Database Migration Service with schema conversion
- C. Write to both systems from the application
- D. Dump, restore, then replay the changes

### 64. A review wants converted DDL reviewed and edited before anything is applied. Where should that happen?

- A. Replay read traffic against the target
- B. Reset the sequences after the bulk load
- C. Build the schema in a conversion workspace
- D. Rewrite the stored procedures and DML by hand

### 65. A review finds converted identity columns starting at one, so new inserts collide with loaded keys. What should the team do?

- A. Build the schema in a conversion workspace
- B. Reset the sequences after the bulk load
- C. Rewrite the stored procedures and DML by hand
- D. Reconcile row counts and checksums

### 66. A review covers engine-specific statements and a need to compare answers between engines. Which two actions are needed? Select two.

- A. Replay read traffic against the target
- B. Reset the sequences after the bulk load
- C. Rewrite the stored procedures and DML by hand
- D. Build the schema in a conversion workspace
- E. Write to both systems from the application

### 67. A review wants the application's busiest statements executed against the target before cutover. Which activity fits?

- A. Reconcile row counts and checksums
- B. Replay read traffic against the target
- C. Rewrite the stored procedures and DML by hand
- D. Follow a cutover runbook with a rollback step

### 68. A review must keep a target current during an eleven-hour load without stopping the source. What should the team use?

- A. Use the engine native logical replication
- B. Accept a scheduled extended outage
- C. Export a logical dump to Cloud Storage
- D. Write to both systems from the application

### 69. A review finds rows written during the bulk load missing on the target. What must happen before the switch?

- A. Repoint the connection string at the target
- B. Reconcile row counts and checksums
- C. Freeze writes during the cutover
- D. Apply the captured change backlog before cutover

### 70. A review finds matching row counts but a 0.4 percent difference in daily totals between source and target. Which activity locates it?

- A. Repoint the connection string at the target
- B. Replay read traffic against the target
- C. Reset the sequences after the bulk load
- D. Reconcile row counts and checksums

### 71. A review wants the target's report output compared with the source's before cutover. Which check fits?

- A. Follow a cutover runbook with a rollback step
- B. Replay read traffic against the target
- C. Reconcile row counts and checksums
- D. Write to both systems from the application

### 72. A review covers the last two steps of a cutover: stopping writes and moving clients. Which two actions complete it? Select two.

- A. Freeze writes during the cutover
- B. Repoint the connection string at the target
- C. Decommission the source after a parallel period
- D. Follow a cutover runbook with a rollback step
- E. Measure the catch-up rate before choosing the window

### 73. A review asks what the team does if validation fails with ten minutes left in the window. What should exist beforehand?

- A. Freeze writes during the cutover
- B. Follow a cutover runbook with a rollback step
- C. Repoint the connection string at the target
- D. Write to both systems from the application

### 74. A review must show that the catch-up increment fits inside the approved cutover window. What should the team measure?

- A. Accept a scheduled extended outage
- B. Repoint the connection string at the target
- C. Measure the catch-up rate before choosing the window
- D. Freeze writes during the cutover

### 75. A review requires the old system to keep receiving writes after cutover for its remaining users. What should be configured?

- A. Set up reverse replication to the source
- B. Decommission the source after a parallel period
- C. Repoint the connection string at the target
- D. Write to both systems from the application

### 76. A review asks when the fallback ends and the old system is removed. What should the team define?

- A. Decommission the source after a parallel period
- B. Repoint the connection string at the target
- C. Set up reverse replication to the source
- D. Confirm no client still uses the old endpoint

### 77. A review of a 5 TB migration must avoid a second full load and prove the window is achievable. Select two.

- A. Use the engine native logical replication
- B. Write to both systems from the application
- C. Measure the catch-up rate before choosing the window
- D. Dump, restore, then replay the changes
- E. Accept a scheduled extended outage

### 78. A review finds the source's change rate spikes every Monday morning, and the cutover window is short. What should the team do?

- A. Measure the catch-up rate before choosing the window
- B. Accept a scheduled extended outage
- C. Write to both systems from the application
- D. Move the job outside the contention window

### 79. A review requires proof that nothing still connects to the source before it is deleted. What should the team check?

- A. Confirm no client still uses the old endpoint
- B. Reconcile row counts and checksums
- C. Decommission the source after a parallel period
- D. Repoint the connection string at the target

### 80. A review requires eight years of history to stay queryable after the source is removed. What should the team do?

- A. Keep part of the estate on-premises with a hybrid link
- B. Set up reverse replication to the source
- C. Decommission the source after a parallel period
- D. Export the table into BigQuery

---

## Domain 4 — Deploy Scalable and Highly Available Databases in Google Cloud (Deployment, High Availability, and Disaster Recovery)

### 81. A review requires a full database estate to be reproducible in another region after a disaster. What makes that possible?

- A. Clone the instance for the test
- B. Stand up a parallel instance and switch over
- C. Provision the instance with a Terraform module
- D. Provision the instance once by hand

### 82. A review finds database changes reaching production with no approval record. What should the team adopt?

- A. Provision the instance once by hand
- B. Test the upgrade on a clone first
- C. Review the fleet in Database Center
- D. Apply the change through the infrastructure pipeline

### 83. A review requires the same configuration applied to forty instances without manual edits. What should the team use?

- A. Stand up a parallel instance and switch over
- B. Take a backup before the upgrade
- C. Provision the instance once by hand
- D. Provision the instance with a Terraform module

### 84. A review must show both zone failover and regional promotion working before go-live. Select two.

- A. Rehearse the promotion in a test project
- B. Run a controlled failover test
- C. Take a backup before the upgrade
- D. Restore the backup into the second region
- E. Watch the error rate after the change

### 85. A review wants proof that the team can rebuild from backup in a second region, not only fail over. What should it rehearse?

- A. Rehearse the promotion in a test project
- B. Run a controlled failover test
- C. Restore the backup into the second region
- D. Take a backup before the upgrade

### 86. A review finds the promoted replica cannot carry production writes because it was sized for reporting. What should change?

- A. Reserve headroom above the measured peak
- B. Restore the backup into the second region
- C. Pre-size the promoted replica for the full load
- D. Add a read replica for the read traffic

### 87. A review requires Spanner writes to continue when a region is lost, with no manual promotion. Which choice fits?

- A. Add a cross-region read replica
- B. Choose a multi-region instance configuration
- C. Enable regional high availability with a standby zone
- D. Restore the backup into the second region

### 88. A review requires AlloyDB reads in a second region with a promotion path. Which choice fits?

- A. Add a secondary cluster in the second region
- B. Run a single zonal instance
- C. Restore the backup into the second region
- D. Add nodes to the read pool

### 89. A review requires a Bigtable client to survive losing one cluster without configuration change. Which setting fits?

- A. Add a secondary cluster in the second region
- B. Route the app profile across both clusters
- C. Add a cross-region read replica
- D. Pin the app profile to one cluster

### 90. A review finds the read tier of an AlloyDB cluster saturated while the primary still has spare capacity. What should the team do?

- A. Send reporting queries to the read replica
- B. Add nodes to the read pool
- C. Increase the machine type of the instance
- D. Cache the hot read path in Memorystore

### 91. A review finds a Cloud SQL replica idle while the primary runs reporting queries at ninety percent. What should the team change?

- A. Send reporting queries to the read replica
- B. Cache the hot read path in Memorystore
- C. Add a read replica for the read traffic
- D. Increase the machine type of the instance

### 92. A review requires seventy tenant instances with identical settings and per-tenant labels. What should the team use?

- A. Provision the instance with a Terraform module
- B. Provision the instance once by hand
- C. Test the upgrade on a clone first
- D. Review the fleet in Database Center

### 93. A review requires provisioning to fail when a required label is missing. What should the team use?

- A. Apply the change through the infrastructure pipeline
- B. Clone the instance for the test
- C. Provision the instance once by hand
- D. Take a backup before the upgrade

### 94. A review requires automatic notice of a failover and confirmation that queries still succeed afterwards. Select two.

- A. Use Query Insights to find the heavy statements
- B. Create an alerting policy on the metric
- C. Review the fleet in Database Center
- D. Watch CPU, memory, disk, and IOPS together
- E. Alert when the instance is unreachable

### 95. A review asks for a single inventory listing every database, its engine version, and its current health. Which view fits?

- A. Read the slow query log
- B. Review the fleet in Database Center
- C. Use Query Insights to find the heavy statements
- D. Watch CPU, memory, disk, and IOPS together

### 96. A review accepts an hour of recovery time and five minutes of data loss, and a current remote copy exists. What should the team plan to do?

- A. Restore to the timestamp before the bad change
- B. Run a controlled failover test
- C. Promote the cross-region replica during the outage
- D. Restore the backup into the second region

### 97. A review notes the failed region may return while the promoted instance is serving. What must the runbook include?

- A. Set up reverse replication to the source
- B. Fence the old primary before promotion
- C. Freeze writes during the cutover
- D. Follow a cutover runbook with a rollback step

### 98. A review finds clients caching a database address and reconnecting to a failed instance. What should the team adopt?

- A. Use the language connector with IAM credentials
- B. Add the client range to authorized networks
- C. Repoint the connection string at the target
- D. Put a session pooler in front of the instance

### 99. A review must budget capacity for the instance that will take over, not just for today's read overflow. What should that budget include?

- A. Reserve headroom above the measured peak
- B. Add a read replica for the read traffic
- C. Scale down outside business hours
- D. Reduce the machine type to match observed use

### 100. A review finds the standby at forty percent of production and resizing takes longer than the recovery window. What should change?

- A. Pre-size the promoted replica for the full load
- B. Scale down outside business hours
- C. Add a read replica for the read traffic
- D. Reserve headroom above the measured peak

---

## Answer key and explanations

### Question 1 — D

Answer: Size the instance from the observed peak metrics. The comparable service's measured peaks are the strongest available evidence for the new shape. Choose a shape from measured CPU, memory, and IOPS rather than from a guess. Local study-map skill 1.1 (Workload Sizing From Current Metrics), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 1 (design innovative, scalable, and highly available cloud database solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A one- or three-year commitment that discounts the capacity always in use. Why the correct answer wins: The comparable service's measured peaks are the strongest available evidence for the new shape.
- **B:** Incorrect for this question. Keep spare capacity so a failover or a traffic spike does not saturate the instance. Why the correct answer wins: The comparable service's measured peaks are the strongest available evidence for the new shape.
- **C:** Incorrect for this question. Generate representative traffic and read the resource curve before choosing a shape. Why the correct answer wins: The comparable service's measured peaks are the strongest available evidence for the new shape.
- **D:** Correct. Choose a shape from measured CPU, memory, and IOPS rather than from a guess. In this case: The comparable service's measured peaks are the strongest available evidence for the new shape.

### Question 2 — C

Answer: Reserve headroom above the measured peak. The shape has to hold the seasonal peak, so headroom above the ordinary level is the sizing requirement. Keep spare capacity so a failover or a traffic spike does not saturate the instance. Local study-map skill 1.1 (Workload Sizing From Current Metrics), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 1 (design innovative, scalable, and highly available cloud database solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Choose a shape from measured CPU, memory, and IOPS rather than from a guess. Why the correct answer wins: The shape has to hold the seasonal peak, so headroom above the ordinary level is the sizing requirement.
- **B:** Incorrect for this question. Shrink an instance whose peak fits a smaller shape. Why the correct answer wins: The shape has to hold the seasonal peak, so headroom above the ordinary level is the sizing requirement.
- **C:** Correct. Keep spare capacity so a failover or a traffic spike does not saturate the instance. In this case: The shape has to hold the seasonal peak, so headroom above the ordinary level is the sizing requirement.
- **D:** Incorrect for this question. Remove capacity that serves no traffic. Why the correct answer wins: The shape has to hold the seasonal peak, so headroom above the ordinary level is the sizing requirement.

### Question 3 — A, E

Answers: Increase the disk size to raise throughput; Increase the machine type of the instance. A larger shape supplies the memory, and more disk raises the throughput ceiling, which a replica or a pooler does not. Buy more storage so the attached disk also yields more IOPS and throughput. Move the instance to a larger shape so more vCPU and memory serve the same data. Local study-map skill 1.2 (Compute and Storage Sizing Tradeoffs), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 1 (design innovative, scalable, and highly available cloud database solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Correct. Move the instance to a larger shape so more vCPU and memory serve the same data. In this case: A larger shape supplies the memory, and more disk raises the throughput ceiling, which a replica or a pooler does not.
- **B:** Incorrect for this question. Send reads to a copy so the primary keeps its capacity for writes. Why the correct answer wins: A larger shape supplies the memory, and more disk raises the throughput ceiling, which a replica or a pooler does not.
- **C:** Incorrect for this question. Trade a higher price per gigabyte for lower latency on random reads. Why the correct answer wins: A larger shape supplies the memory, and more disk raises the throughput ceiling, which a replica or a pooler does not.
- **D:** Incorrect for this question. A pooler that multiplexes many application connections onto few database sessions. Why the correct answer wins: A larger shape supplies the memory, and more disk raises the throughput ceiling, which a replica or a pooler does not.
- **E:** Correct. Buy more storage so the attached disk also yields more IOPS and throughput. In this case: A larger shape supplies the memory, and more disk raises the throughput ceiling, which a replica or a pooler does not.

### Question 4 — A

Answer: Move the data to SSD storage. SSD lowers the read latency that is causing the miss. Trade a higher price per gigabyte for lower latency on random reads. Local study-map skill 1.2 (Compute and Storage Sizing Tradeoffs), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 1 (design innovative, scalable, and highly available cloud database solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Correct. Trade a higher price per gigabyte for lower latency on random reads. In this case: SSD lowers the read latency that is causing the miss.
- **B:** Incorrect for this question. Increase the cluster size so more tablet servers absorb the request rate. Why the correct answer wins: SSD lowers the read latency that is causing the miss.
- **C:** Incorrect for this question. Trade latency for a lower price on large, throughput-oriented scans. Why the correct answer wins: SSD lowers the read latency that is causing the miss.
- **D:** Incorrect for this question. A rule that drops versions by age or count, which also bounds recovery. Why the correct answer wins: SSD lowers the read latency that is causing the miss.

### Question 5 — B

Answer: Enable autoscaling on the instance. Autoscaling adjusts provisioned compute to the curve, while fixed increments need an operator. Let compute follow a target utilization instead of a fixed size. Local study-map skill 1.3 (Machine Type and Storage Type Selection), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 1 (design innovative, scalable, and highly available cloud database solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Raise provisioned compute in 1000-unit node steps or 100-unit increments. Why the correct answer wins: Autoscaling adjusts provisioned compute to the curve, while fixed increments need an operator.
- **B:** Correct. Let compute follow a target utilization instead of a fixed size. In this case: Autoscaling adjusts provisioned compute to the curve, while fixed increments need an operator.
- **C:** Incorrect for this question. Move the instance to a larger shape so more vCPU and memory serve the same data. Why the correct answer wins: Autoscaling adjusts provisioned compute to the curve, while fixed increments need an operator.
- **D:** Incorrect for this question. Increase the cluster size so more tablet servers absorb the request rate. Why the correct answer wins: Autoscaling adjusts provisioned compute to the curve, while fixed increments need an operator.

### Question 6 — D

Answer: Add nodes to the Bigtable cluster. Adding nodes raises serving capacity for a healthy access pattern. Increase the cluster size so more tablet servers absorb the request rate. Local study-map skill 1.3 (Machine Type and Storage Type Selection), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 1 (design innovative, scalable, and highly available cloud database solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Trade a higher price per gigabyte for lower latency on random reads. Why the correct answer wins: Adding nodes raises serving capacity for a healthy access pattern.
- **B:** Incorrect for this question. Raise provisioned compute in 1000-unit node steps or 100-unit increments. Why the correct answer wins: Adding nodes raises serving capacity for a healthy access pattern.
- **C:** Incorrect for this question. Fix the access pattern that concentrates load on a narrow key range. Why the correct answer wins: Adding nodes raises serving capacity for a healthy access pattern.
- **D:** Correct. Increase the cluster size so more tablet servers absorb the request rate. In this case: Adding nodes raises serving capacity for a healthy access pattern.

### Question 7 — D

Answer: Enable regional high availability with a standby zone. A regional instance keeps a standby in another zone and fails over automatically. A primary and standby in two zones of one region with automatic failover. Local study-map skill 1.4 (Zonal, Regional, and Multi-Regional Tradeoffs), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 1 (design innovative, scalable, and highly available cloud database solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A copy in a second region that serves reads and can be promoted. Why the correct answer wins: A regional instance keeps a standby in another zone and fails over automatically.
- **B:** Incorrect for this question. A topology that places replicas in separate regions for regional-failure tolerance. Why the correct answer wins: A regional instance keeps a standby in another zone and fails over automatically.
- **C:** Incorrect for this question. One instance in one zone with no standby, so a zone failure stops writes. Why the correct answer wins: A regional instance keeps a standby in another zone and fails over automatically.
- **D:** Correct. A primary and standby in two zones of one region with automatic failover. In this case: A regional instance keeps a standby in another zone and fails over automatically.

### Question 8 — D

Answer: Choose a multi-region instance configuration. A multi-region configuration keeps quorum across regions automatically. A topology that places replicas in separate regions for regional-failure tolerance. Local study-map skill 1.4 (Zonal, Regional, and Multi-Regional Tradeoffs), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 1 (design innovative, scalable, and highly available cloud database solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A primary and standby in two zones of one region with automatic failover. Why the correct answer wins: A multi-region configuration keeps quorum across regions automatically.
- **B:** Incorrect for this question. A copy in a second region that serves reads and can be promoted. Why the correct answer wins: A multi-region configuration keeps quorum across regions automatically.
- **C:** Incorrect for this question. Rebuild the database in the surviving region from the latest backup. Why the correct answer wins: A multi-region configuration keeps quorum across regions automatically.
- **D:** Correct. A topology that places replicas in separate regions for regional-failure tolerance. In this case: A multi-region configuration keeps quorum across regions automatically.

### Question 9 — B

Answer: Add a secondary cluster in the second region. A secondary cluster serves reads and can be promoted. An AlloyDB cross-region copy that can be promoted to a primary cluster. Local study-map skill 1.4 (Zonal, Regional, and Multi-Regional Tradeoffs), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 1 (design innovative, scalable, and highly available cloud database solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. One instance in one zone with no standby, so a zone failure stops writes. Why the correct answer wins: A secondary cluster serves reads and can be promoted.
- **B:** Correct. An AlloyDB cross-region copy that can be promoted to a primary cluster. In this case: A secondary cluster serves reads and can be promoted.
- **C:** Incorrect for this question. Grow the AlloyDB read pool that serves read-only connections. Why the correct answer wins: A secondary cluster serves reads and can be promoted.
- **D:** Incorrect for this question. Rebuild the database in the surviving region from the latest backup. Why the correct answer wins: A secondary cluster serves reads and can be promoted.

### Question 10 — A, D

Answers: Schedule the maintenance window in the low-traffic period; Set a deny maintenance period over the peak event. The maintenance window sets the permitted hours, and the deny period removes the protected week. Choose the weekly window when patching may interrupt the instance. Block maintenance during a period when an interruption is unacceptable. Local study-map skill 1.5 (Maintenance Windows and Notification), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 1 (design innovative, scalable, and highly available cloud database solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Correct. Choose the weekly window when patching may interrupt the instance. In this case: The maintenance window sets the permitted hours, and the deny period removes the protected week.
- **B:** Incorrect for this question. Change the engine version on the running instance during the window. Why the correct answer wins: The maintenance window sets the permitted hours, and the deny period removes the protected week.
- **C:** Incorrect for this question. Trigger a switchover in a test window and observe how long writes are unavailable. Why the correct answer wins: The maintenance window sets the permitted hours, and the deny period removes the protected week.
- **D:** Correct. Block maintenance during a period when an interruption is unacceptable. In this case: The maintenance window sets the permitted hours, and the deny period removes the protected week.
- **E:** Incorrect for this question. A recovery point that makes the upgrade reversible in practice. Why the correct answer wins: The maintenance window sets the permitted hours, and the deny period removes the protected week.

### Question 11 — D

Answer: Schedule the maintenance window in the low-traffic period. The maintenance window defines the permitted hour, which is what the notification describes. Choose the weekly window when patching may interrupt the instance. Local study-map skill 1.5 (Maintenance Windows and Notification), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 1 (design innovative, scalable, and highly available cloud database solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Block maintenance during a period when an interruption is unacceptable. Why the correct answer wins: The maintenance window defines the permitted hour, which is what the notification describes.
- **B:** Incorrect for this question. A recovery point that makes the upgrade reversible in practice. Why the correct answer wins: The maintenance window defines the permitted hour, which is what the notification describes.
- **C:** Incorrect for this question. Change the engine version on the running instance during the window. Why the correct answer wins: The maintenance window defines the permitted hour, which is what the notification describes.
- **D:** Correct. Choose the weekly window when patching may interrupt the instance. In this case: The maintenance window defines the permitted hour, which is what the notification describes.

### Question 12 — B, D

Answers: Connect over private IP inside the VPC; Enable IAM database authentication. A private address removes the public surface, and IAM database authentication removes the credential. A private address reachable only from the VPC and connected networks. Map an IAM principal to a database user so no password is stored. Local study-map skill 1.6 (Network Connectivity and Private Access), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 1 (design innovative, scalable, and highly available cloud database solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A native database user whose credential must be rotated and stored. Why the correct answer wins: A private address removes the public surface, and IAM database authentication removes the credential.
- **B:** Correct. Map an IAM principal to a database user so no password is stored. In this case: A private address removes the public surface, and IAM database authentication removes the credential.
- **C:** Incorrect for this question. A public-IP allowlist that admits the caller range. Why the correct answer wins: A private address removes the public surface, and IAM database authentication removes the credential.
- **D:** Correct. A private address reachable only from the VPC and connected networks. In this case: A private address removes the public surface, and IAM database authentication removes the credential.
- **E:** Incorrect for this question. A public address that requires encrypted connections from any client. Why the correct answer wins: A private address removes the public surface, and IAM database authentication removes the credential.

### Question 13 — D

Answer: Connect through the Cloud SQL Auth Proxy. The proxy authorizes the session with IAM over TLS from any location. A local proxy that adds IAM authorization and TLS without opening a network path. Local study-map skill 1.6 (Network Connectivity and Private Access), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 1 (design innovative, scalable, and highly available cloud database solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A public-IP allowlist that admits the caller range. Why the correct answer wins: The proxy authorizes the session with IAM over TLS from any location.
- **B:** Incorrect for this question. A private endpoint in the consumer VPC that reaches the service without peering. Why the correct answer wins: The proxy authorizes the session with IAM over TLS from any location.
- **C:** Incorrect for this question. A public address that requires encrypted connections from any client. Why the correct answer wins: The proxy authorizes the session with IAM over TLS from any location.
- **D:** Correct. A local proxy that adds IAM authorization and TLS without opening a network path. In this case: The proxy authorizes the session with IAM over TLS from any location.

### Question 14 — A

Answer: Encrypt with a customer-managed key in Cloud KMS. A customer-managed key gives the company that ability, which a Google-managed key does not. A key the customer owns and can rotate or revoke. Local study-map skill 1.7 (Key Management and Encryption), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 1 (design innovative, scalable, and highly available cloud database solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Correct. A key the customer owns and can rotate or revoke. In this case: A customer-managed key gives the company that ability, which a Google-managed key does not.
- **B:** Incorrect for this question. Default encryption at rest with keys the customer neither sees nor manages. Why the correct answer wins: A customer-managed key gives the company that ability, which a Google-managed key does not.
- **C:** Incorrect for this question. Export entries to storage whose retention cannot be shortened. Why the correct answer wins: A customer-managed key gives the company that ability, which a Google-managed key does not.
- **D:** Incorrect for this question. Record reads and writes, which are not captured by default. Why the correct answer wins: A customer-managed key gives the company that ability, which a Google-managed key does not.

### Question 15 — B

Answer: Rotate the customer-managed key on a schedule. Rotation adds versions for new writes and leaves existing ciphertext decryptable. Produce new key versions so an old version stops encrypting new data. Local study-map skill 1.7 (Key Management and Encryption), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 1 (design innovative, scalable, and highly available cloud database solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Default encryption at rest with keys the customer neither sees nor manages. Why the correct answer wins: Rotation adds versions for new writes and leaves existing ciphertext decryptable.
- **B:** Correct. Produce new key versions so an old version stops encrypting new data. In this case: Rotation adds versions for new writes and leaves existing ciphertext decryptable.
- **C:** Incorrect for this question. A boundary that blocks data exfiltration even from an authorized identity. Why the correct answer wins: Rotation adds versions for new writes and leaves existing ciphertext decryptable.
- **D:** Incorrect for this question. A key the customer owns and can rotate or revoke. Why the correct answer wins: Rotation adds versions for new writes and leaves existing ciphertext decryptable.

### Question 16 — C, E

Answers: Put a session pooler in front of the instance; Raise the max_connections database flag. The raised ceiling prevents refusals during the transition, and the pooler reduces sessions as it lands. A pooler that multiplexes many application connections onto few database sessions. Increase the database-level connection ceiling on the instance. Local study-map skill 1.8 (Session Pooling and Connection Management), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 1 (design innovative, scalable, and highly available cloud database solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Move the instance to a larger shape so more vCPU and memory serve the same data. Why the correct answer wins: The raised ceiling prevents refusals during the transition, and the pooler reduces sessions as it lands.
- **B:** Incorrect for this question. Close sessions that the application opens and never returns to the pool. Why the correct answer wins: The raised ceiling prevents refusals during the transition, and the pooler reduces sessions as it lands.
- **C:** Correct. Increase the database-level connection ceiling on the instance. In this case: The raised ceiling prevents refusals during the transition, and the pooler reduces sessions as it lands.
- **D:** Incorrect for this question. Buy a larger shape because the connection limit scales with memory. Why the correct answer wins: The raised ceiling prevents refusals during the transition, and the pooler reduces sessions as it lands.
- **E:** Correct. A pooler that multiplexes many application connections onto few database sessions. In this case: The raised ceiling prevents refusals during the transition, and the pooler reduces sessions as it lands.

### Question 17 — B

Answer: Fix the connection leak in the application. Closing sessions on the error path removes the leak at its source. Close sessions that the application opens and never returns to the pool. Local study-map skill 1.8 (Session Pooling and Connection Management), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 1 (design innovative, scalable, and highly available cloud database solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Increase the database-level connection ceiling on the instance. Why the correct answer wins: Closing sessions on the error path removes the leak at its source.
- **B:** Correct. Close sessions that the application opens and never returns to the pool. In this case: Closing sessions on the error path removes the leak at its source.
- **C:** Incorrect for this question. A pooler that multiplexes many application connections onto few database sessions. Why the correct answer wins: Closing sessions on the error path removes the leak at its source.
- **D:** Incorrect for this question. Move the instance to a larger shape so more vCPU and memory serve the same data. Why the correct answer wins: Closing sessions on the error path removes the leak at its source.

### Question 18 — C

Answer: Enable Data Access audit logs. Row reads appear only once Data Access audit logs are enabled. Record reads and writes, which are not captured by default. Local study-map skill 1.9 (Auditing Policies for Managed Services), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 1 (design innovative, scalable, and highly available cloud database solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Export entries to storage whose retention cannot be shortened. Why the correct answer wins: Row reads appear only once Data Access audit logs are enabled.
- **B:** Incorrect for this question. Record configuration changes only, leaving row-level reads unaudited. Why the correct answer wins: Row reads appear only once Data Access audit logs are enabled.
- **C:** Correct. Record reads and writes, which are not captured by default. In this case: Row reads appear only once Data Access audit logs are enabled.
- **D:** Incorrect for this question. Turn a recurring log pattern into a metric that can be charted and alerted on. Why the correct answer wins: Row reads appear only once Data Access audit logs are enabled.

### Question 19 — B

Answer: Route the audit logs to a locked log bucket. Routing entries to locked storage prevents the retention from being shortened. Export entries to storage whose retention cannot be shortened. Local study-map skill 1.9 (Auditing Policies for Managed Services), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 1 (design innovative, scalable, and highly available cloud database solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A single view of health, security, and version posture across database instances. Why the correct answer wins: Routing entries to locked storage prevents the retention from being shortened.
- **B:** Correct. Export entries to storage whose retention cannot be shortened. In this case: Routing entries to locked storage prevents the retention from being shortened.
- **C:** Incorrect for this question. Record configuration changes only, leaving row-level reads unaudited. Why the correct answer wins: Routing entries to locked storage prevents the retention from being shortened.
- **D:** Incorrect for this question. Record reads and writes, which are not captured by default. Why the correct answer wins: Routing entries to locked storage prevents the retention from being shortened.

### Question 20 — B

Answer: Use Cloud SQL for the relational workload. A managed relational instance handles patching and backups for this size. A managed MySQL, PostgreSQL, or SQL Server instance with Google-operated backups, patching, and failover. Local study-map skill 1.10 (Managed, Self-Managed, and Partner Offerings), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 1 (design innovative, scalable, and highly available cloud database solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A self-managed engine on virtual machines where the team owns patching, backups, and failover. Why the correct answer wins: A managed relational instance handles patching and backups for this size.
- **B:** Correct. A managed MySQL, PostgreSQL, or SQL Server instance with Google-operated backups, patching, and failover. In this case: A managed relational instance handles patching and backups for this size.
- **C:** Incorrect for this question. A horizontally scalable relational database with strong consistency across regions and no manual sharding. Why the correct answer wins: A managed relational instance handles patching and backups for this size.
- **D:** Incorrect for this question. A managed PostgreSQL-compatible database with a separate read pool and columnar acceleration for mixed transactional and analytical load. Why the correct answer wins: A managed relational instance handles patching and backups for this size.

### Question 21 — C

Answer: Use a partner-managed database offering. A partner-managed offering keeps that operating relationship. A third-party database operated by its vendor on Google Cloud infrastructure. Local study-map skill 1.10 (Managed, Self-Managed, and Partner Offerings), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 1 (design innovative, scalable, and highly available cloud database solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Dedicated hardware for engines that cannot be virtualized or licensed for a managed service. Why the correct answer wins: A partner-managed offering keeps that operating relationship.
- **B:** Incorrect for this question. A managed MySQL, PostgreSQL, or SQL Server instance with Google-operated backups, patching, and failover. Why the correct answer wins: A partner-managed offering keeps that operating relationship.
- **C:** Correct. A third-party database operated by its vendor on Google Cloud infrastructure. In this case: A partner-managed offering keeps that operating relationship.
- **D:** Incorrect for this question. A self-managed engine on virtual machines where the team owns patching, backups, and failover. Why the correct answer wins: A partner-managed offering keeps that operating relationship.

### Question 22 — A, D

Answers: Use Bigtable for the high-throughput wide-column workload; Export the table into BigQuery. A wide-column store carries the write load, and exporting into the warehouse serves the analysts. A wide-column NoSQL service built for very high write and read rates over a sparse, row-key-ordered model. Copy the analytical slice into the warehouse on a schedule. Local study-map skill 1.11 (SQL and NoSQL Data Model Fit), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 1 (design innovative, scalable, and highly available cloud database solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Correct. A wide-column NoSQL service built for very high write and read rates over a sparse, row-key-ordered model. In this case: A wide-column store carries the write load, and exporting into the warehouse serves the analysts.
- **B:** Incorrect for this question. A document database with automatic multi-region replication, offline client support, and index-driven queries. Why the correct answer wins: A wide-column store carries the write load, and exporting into the warehouse serves the analysts.
- **C:** Incorrect for this question. A managed MySQL, PostgreSQL, or SQL Server instance with Google-operated backups, patching, and failover. Why the correct answer wins: A wide-column store carries the write load, and exporting into the warehouse serves the analysts.
- **D:** Correct. Copy the analytical slice into the warehouse on a schedule. In this case: A wide-column store carries the write load, and exporting into the warehouse serves the analysts.
- **E:** Incorrect for this question. A managed Redis-compatible in-memory store placed in front of the system of record. Why the correct answer wins: A wide-column store carries the write load, and exporting into the warehouse serves the analysts.

### Question 23 — A

Answer: Use Spanner for the globally distributed relational workload. Spanner provides external consistency with horizontal scale. A horizontally scalable relational database with strong consistency across regions and no manual sharding. Local study-map skill 1.11 (SQL and NoSQL Data Model Fit), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 1 (design innovative, scalable, and highly available cloud database solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Correct. A horizontally scalable relational database with strong consistency across regions and no manual sharding. In this case: Spanner provides external consistency with horizontal scale.
- **B:** Incorrect for this question. A managed MySQL, PostgreSQL, or SQL Server instance with Google-operated backups, patching, and failover. Why the correct answer wins: Spanner provides external consistency with horizontal scale.
- **C:** Incorrect for this question. A document database with automatic multi-region replication, offline client support, and index-driven queries. Why the correct answer wins: Spanner provides external consistency with horizontal scale.
- **D:** Incorrect for this question. A wide-column NoSQL service built for very high write and read rates over a sparse, row-key-ordered model. Why the correct answer wins: Spanner provides external consistency with horizontal scale.

### Question 24 — D

Answer: Use Firestore for the document workload. Firestore supplies the document model with offline clients and managed replication. A document database with automatic multi-region replication, offline client support, and index-driven queries. Local study-map skill 1.11 (SQL and NoSQL Data Model Fit), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 1 (design innovative, scalable, and highly available cloud database solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A managed Redis-compatible in-memory store placed in front of the system of record. Why the correct answer wins: Firestore supplies the document model with offline clients and managed replication.
- **B:** Incorrect for this question. A wide-column NoSQL service built for very high write and read rates over a sparse, row-key-ordered model. Why the correct answer wins: Firestore supplies the document model with offline clients and managed replication.
- **C:** Incorrect for this question. A managed MySQL, PostgreSQL, or SQL Server instance with Google-operated backups, patching, and failover. Why the correct answer wins: Firestore supplies the document model with offline clients and managed replication.
- **D:** Correct. A document database with automatic multi-region replication, offline client support, and index-driven queries. In this case: Firestore supplies the document model with offline clients and managed replication.

### Question 25 — C

Answer: Use AlloyDB vector search with a ScaNN index. A purpose-built vector index handles that scale with filters applied in the engine. A vector index tuned for large embedding sets on AlloyDB. Local study-map skill 1.12 (Vector and Generative AI Requirements), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 1 (design innovative, scalable, and highly available cloud database solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Store embeddings beside relational rows and search them in the same engine. Why the correct answer wins: A purpose-built vector index handles that scale with filters applied in the engine.
- **B:** Incorrect for this question. An index ordered so the filter and sort both resolve without a scan. Why the correct answer wins: A purpose-built vector index handles that scale with filters applied in the engine.
- **C:** Correct. A vector index tuned for large embedding sets on AlloyDB. In this case: A purpose-built vector index handles that scale with filters applied in the engine.
- **D:** Incorrect for this question. Absorb repeated reads in memory so the database sees fewer of them. Why the correct answer wins: A purpose-built vector index handles that scale with filters applied in the engine.

### Question 26 — C

Answer: Enable the vector extension on PostgreSQL. Enabling the vector extension keeps the search beside the existing rows. Store embeddings beside relational rows and search them in the same engine. Local study-map skill 1.12 (Vector and Generative AI Requirements), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 1 (design innovative, scalable, and highly available cloud database solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A vector index tuned for large embedding sets on AlloyDB. Why the correct answer wins: Enabling the vector extension keeps the search beside the existing rows.
- **B:** Incorrect for this question. Copy the analytical slice into the warehouse on a schedule. Why the correct answer wins: Enabling the vector extension keeps the search beside the existing rows.
- **C:** Correct. Store embeddings beside relational rows and search them in the same engine. In this case: Enabling the vector extension keeps the search beside the existing rows.
- **D:** Incorrect for this question. Read the operational table from BigQuery without copying it first. Why the correct answer wins: Enabling the vector extension keeps the search beside the existing rows.

### Question 27 — C

Answer: Commit to the steady baseline capacity. A commitment discounts capacity that runs continuously. A one- or three-year commitment that discounts the capacity always in use. Local study-map skill 1.13 (Comparative Cost Analysis Across Databases), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 1 (design innovative, scalable, and highly available cloud database solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Match capacity to the daily traffic shape. Why the correct answer wins: A commitment discounts capacity that runs continuously.
- **B:** Incorrect for this question. Remove capacity that serves no traffic. Why the correct answer wins: A commitment discounts capacity that runs continuously.
- **C:** Correct. A one- or three-year commitment that discounts the capacity always in use. In this case: A commitment discounts capacity that runs continuously.
- **D:** Incorrect for this question. The automatic discount that applies to long-running Compute Engine usage. Why the correct answer wins: A commitment discounts capacity that runs continuously.

### Question 28 — B

Answer: Scale down outside business hours. Matching capacity to the daily traffic shape removes the idle overnight spend. Match capacity to the daily traffic shape. Local study-map skill 1.13 (Comparative Cost Analysis Across Databases), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 1 (design innovative, scalable, and highly available cloud database solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Shrink an instance whose peak fits a smaller shape. Why the correct answer wins: Matching capacity to the daily traffic shape removes the idle overnight spend.
- **B:** Correct. Match capacity to the daily traffic shape. In this case: Matching capacity to the daily traffic shape removes the idle overnight spend.
- **C:** Incorrect for this question. Hold capacity ahead of a known surge rather than waiting for autoscaling. Why the correct answer wins: Matching capacity to the daily traffic shape removes the idle overnight spend.
- **D:** Incorrect for this question. Remove capacity that serves no traffic. Why the correct answer wins: Matching capacity to the daily traffic shape removes the idle overnight spend.

### Question 29 — C

Answer: Keep the current engine and version. Keeping the engine avoids the rewrites the date cannot absorb. A lift of the existing engine with no conversion work, retaining its behaviour and licensing. Local study-map skill 1.14 (Application and Database Dependencies), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 1 (design innovative, scalable, and highly available cloud database solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A managed path that converts schema and code from a different source engine. Why the correct answer wins: Keeping the engine avoids the rewrites the date cannot absorb.
- **B:** Incorrect for this question. Weigh engine compatibility and code rewrite effort before selecting a destination. Why the correct answer wins: Keeping the engine avoids the rewrites the date cannot absorb.
- **C:** Correct. A lift of the existing engine with no conversion work, retaining its behaviour and licensing. In this case: Keeping the engine avoids the rewrites the date cannot absorb.
- **D:** Incorrect for this question. Keep two databases current from application code during the transition. Why the correct answer wins: Keeping the engine avoids the rewrites the date cannot absorb.

### Question 30 — A, D

Answers: Place the instance in the required region; Add the projects to a VPC Service Controls perimeter. The in-country placement settles location, and the service perimeter blocks the copy path. A location choice that keeps data inside the regulated boundary. A boundary that blocks data exfiltration even from an authorized identity. Local study-map skill 1.15 (Regulatory, Compliance, and Organization Policy), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 1 (design innovative, scalable, and highly available cloud database solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Correct. A location choice that keeps data inside the regulated boundary. In this case: The in-country placement settles location, and the service perimeter blocks the copy path.
- **B:** Incorrect for this question. Default encryption at rest with keys the customer neither sees nor manages. Why the correct answer wins: The in-country placement settles location, and the service perimeter blocks the copy path.
- **C:** Incorrect for this question. A constraint that keeps database resources inside the approved regions. Why the correct answer wins: The in-country placement settles location, and the service perimeter blocks the copy path.
- **D:** Correct. A boundary that blocks data exfiltration even from an authorized identity. In this case: The in-country placement settles location, and the service perimeter blocks the copy path.
- **E:** Incorrect for this question. Absorb repeated reads in memory so the database sees fewer of them. Why the correct answer wins: The in-country placement settles location, and the service perimeter blocks the copy path.

### Question 31 — B

Answer: Place the instance in the required region. Choosing the in-country region puts the data where the regulator requires. A location choice that keeps data inside the regulated boundary. Local study-map skill 1.15 (Regulatory, Compliance, and Organization Policy), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 1 (design innovative, scalable, and highly available cloud database solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A key the customer owns and can rotate or revoke. Why the correct answer wins: Choosing the in-country region puts the data where the regulator requires.
- **B:** Correct. A location choice that keeps data inside the regulated boundary. In this case: Choosing the in-country region puts the data where the regulator requires.
- **C:** Incorrect for this question. A constraint that keeps database resources inside the approved regions. Why the correct answer wins: Choosing the in-country region puts the data where the regulator requires.
- **D:** Incorrect for this question. A boundary that blocks data exfiltration even from an authorized identity. Why the correct answer wins: Choosing the in-country region puts the data where the regulator requires.

### Question 32 — A

Answer: Keep part of the estate on-premises with a hybrid link. A hybrid link keeps the system in place and gives new services a supported path. Interconnect the remaining on-premises system rather than moving it. Local study-map skill 1.16 (Federation, Exports, and Hybrid Spans), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 1 (design innovative, scalable, and highly available cloud database solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Correct. Interconnect the remaining on-premises system rather than moving it. In this case: A hybrid link keeps the system in place and gives new services a supported path.
- **B:** Incorrect for this question. Read the operational table from BigQuery without copying it first. Why the correct answer wins: A hybrid link keeps the system in place and gives new services a supported path.
- **C:** Incorrect for this question. Copy the analytical slice into the warehouse on a schedule. Why the correct answer wins: A hybrid link keeps the system in place and gives new services a supported path.
- **D:** Incorrect for this question. Keep the old system read-only for a defined period, then remove it. Why the correct answer wins: A hybrid link keeps the system in place and gives new services a supported path.

### Question 33 — A, E

Answers: Bind access to a Google group; Enable IAM database authentication. IAM database authentication removes the stored password, and group binding makes revocation a membership change. Manage membership in a group rather than editing bindings per person. Map an IAM principal to a database user so no password is stored. Local study-map skill 2.1 (IAM for Database Connectivity), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 2 (manage a solution that can span multiple database technologies): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Correct. Map an IAM principal to a database user so no password is stored. In this case: IAM database authentication removes the stored password, and group binding makes revocation a membership change.
- **B:** Incorrect for this question. A broad legacy role that can change most resources in the project. Why the correct answer wins: IAM database authentication removes the stored password, and group binding makes revocation a membership change.
- **C:** Incorrect for this question. A single credential used by every workload that touches the database. Why the correct answer wins: IAM database authentication removes the stored password, and group binding makes revocation a membership change.
- **D:** Incorrect for this question. A native database user whose credential must be rotated and stored. Why the correct answer wins: IAM database authentication removes the stored password, and group binding makes revocation a membership change.
- **E:** Correct. Manage membership in a group rather than editing bindings per person. In this case: IAM database authentication removes the stored password, and group binding makes revocation a membership change.

### Question 34 — A

Answer: Grant the predefined database role. A narrower predefined role supplies the reads without administrative control. A Google-managed role that carries the permissions the operator needs. Local study-map skill 2.1 (IAM for Database Connectivity), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 2 (manage a solution that can span multiple database technologies): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Correct. A Google-managed role that carries the permissions the operator needs. In this case: A narrower predefined role supplies the reads without administrative control.
- **B:** Incorrect for this question. A role built from an explicit permission list. Why the correct answer wins: A narrower predefined role supplies the reads without administrative control.
- **C:** Incorrect for this question. A broad legacy role that can change most resources in the project. Why the correct answer wins: A narrower predefined role supplies the reads without administrative control.
- **D:** Incorrect for this question. Individual accountability at the engine layer rather than a shared login. Why the correct answer wins: A narrower predefined role supplies the reads without administrative control.

### Question 35 — C

Answer: Create one database user per person. Separate database users give each analyst a named identity in the audit trail. Individual accountability at the engine layer rather than a shared login. Local study-map skill 2.2 (Database Users and Authentication), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 2 (manage a solution that can span multiple database technologies): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A single credential used by every workload that touches the database. Why the correct answer wins: Separate database users give each analyst a named identity in the audit trail.
- **B:** Incorrect for this question. A native database user whose credential must be rotated and stored. Why the correct answer wins: Separate database users give each analyst a named identity in the audit trail.
- **C:** Correct. Individual accountability at the engine layer rather than a shared login. In this case: Separate database users give each analyst a named identity in the audit trail.
- **D:** Incorrect for this question. A workload identity that can be authorized by IAM without a stored password. Why the correct answer wins: Separate database users give each analyst a named identity in the audit trail.

### Question 36 — C

Answer: Add the index the slow query needs. An index on the predicate turns the scan into a lookup. Local study-map skill 2.3 (Slow Queries and Missing Indexes), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 2 (manage a solution that can span multiple database technologies): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Split one table into ranges so pruning and maintenance act on less data. Why the correct answer wins: An index on the predicate turns the scan into a lookup.
- **B:** Incorrect for this question. Give sorts and joins more working memory on the instance. Why the correct answer wins: An index on the predicate turns the scan into a lookup.
- **C:** Correct. In this case: An index on the predicate turns the scan into a lookup.
- **D:** Incorrect for this question. Give the planner current cardinality so it stops choosing a poor plan. Why the correct answer wins: An index on the predicate turns the scan into a lookup.

### Question 37 — A

Answer: Read the query plan for the statement. The plan shows the access path the planner chose, which explains the change. Inspect the chosen scan and join order before changing anything. Local study-map skill 2.3 (Slow Queries and Missing Indexes), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 2 (manage a solution that can span multiple database technologies): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Correct. Inspect the chosen scan and join order before changing anything. In this case: The plan shows the access path the planner chose, which explains the change.
- **B:** Incorrect for this question. Give the planner current cardinality so it stops choosing a poor plan. Why the correct answer wins: The plan shows the access path the planner chose, which explains the change.
- **C:** Incorrect for this question. Remove write amplification from an index nothing reads. Why the correct answer wins: The plan shows the access path the planner chose, which explains the change.
- **D:** Incorrect for this question. Create an index that turns a scan into a lookup for the predicate. Why the correct answer wins: The plan shows the access path the planner chose, which explains the change.

### Question 38 — B, E

Answers: Inspect lock waits and blocking sessions; Batch the writes into fewer round trips. The lock graph explains the stall, and shorter transactions reduce the time the batch holds locks. Find the transaction that holds the lock others wait on. Cut per-row network and commit overhead in the application. Local study-map skill 2.4 (Locking and Resource Contention), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 2 (manage a solution that can span multiple database technologies): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. End the blocking transaction so the queue drains. Why the correct answer wins: The lock graph explains the stall, and shorter transactions reduce the time the batch holds locks.
- **B:** Correct. Find the transaction that holds the lock others wait on. In this case: The lock graph explains the stall, and shorter transactions reduce the time the batch holds locks.
- **C:** Incorrect for this question. Create an index that turns a scan into a lookup for the predicate. Why the correct answer wins: The lock graph explains the stall, and shorter transactions reduce the time the batch holds locks.
- **D:** Incorrect for this question. Give the planner current cardinality so it stops choosing a poor plan. Why the correct answer wins: The lock graph explains the stall, and shorter transactions reduce the time the batch holds locks.
- **E:** Correct. Cut per-row network and commit overhead in the application. In this case: The lock graph explains the stall, and shorter transactions reduce the time the batch holds locks.

### Question 39 — B

Answer: Terminate the session that holds the lock. Ending that transaction releases the queue. End the blocking transaction so the queue drains. Local study-map skill 2.4 (Locking and Resource Contention), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 2 (manage a solution that can span multiple database technologies): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Find the transaction that holds the lock others wait on. Why the correct answer wins: Ending that transaction releases the queue.
- **B:** Correct. End the blocking transaction so the queue drains. In this case: Ending that transaction releases the queue.
- **C:** Incorrect for this question. Separate analytical reads from the write path. Why the correct answer wins: Ending that transaction releases the queue.
- **D:** Incorrect for this question. Cut per-row network and commit overhead in the application. Why the correct answer wins: Ending that transaction releases the queue.

### Question 40 — D

Answer: Watch CPU, memory, disk, and IOPS together. The instance view shows both signals together. Read the instance-level signals before attributing the symptom to the query. Local study-map skill 2.5 (Database Vitals Monitoring), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 2 (manage a solution that can span multiple database technologies): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A per-query view of latency, load, and wait events on the instance. Why the correct answer wins: The instance view shows both signals together.
- **B:** Incorrect for this question. A single view of health, security, and version posture across database instances. Why the correct answer wins: The instance view shows both signals together.
- **C:** Incorrect for this question. The engine log of statements that exceeded the long-query threshold. Why the correct answer wins: The instance view shows both signals together.
- **D:** Correct. Read the instance-level signals before attributing the symptom to the query. In this case: The instance view shows both signals together.

### Question 41 — D

Answer: Use Query Insights to find the heavy statements. Per-query wait breakdown attributes time to a category. A per-query view of latency, load, and wait events on the instance. Local study-map skill 2.5 (Database Vitals Monitoring), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 2 (manage a solution that can span multiple database technologies): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Read the instance-level signals before attributing the symptom to the query. Why the correct answer wins: Per-query wait breakdown attributes time to a category.
- **B:** Incorrect for this question. The engine log of statements that exceeded the long-query threshold. Why the correct answer wins: Per-query wait breakdown attributes time to a category.
- **C:** Incorrect for this question. Turn a recurring log pattern into a metric that can be charted and alerted on. Why the correct answer wins: Per-query wait breakdown attributes time to a category.
- **D:** Correct. A per-query view of latency, load, and wait events on the instance. In this case: Per-query wait breakdown attributes time to a category.

### Question 42 — C

Answer: Move the job outside the contention window. Spacing the jobs apart keeps each inside the limit without changing the quota. Stagger the work so concurrent operations stop colliding on the same limit. Local study-map skill 2.6 (Quotas and Limits), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 2 (manage a solution that can span multiple database technologies): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Repeat the call after a growing delay so a transient refusal clears. Why the correct answer wins: Spacing the jobs apart keeps each inside the limit without changing the quota.
- **B:** Incorrect for this question. A flat-file extract for a downstream loader rather than a restore. Why the correct answer wins: Spacing the jobs apart keeps each inside the limit without changing the quota.
- **C:** Correct. Stagger the work so concurrent operations stop colliding on the same limit. In this case: Spacing the jobs apart keeps each inside the limit without changing the quota.
- **D:** Incorrect for this question. Raise the project-level ceiling so the operation is no longer refused. Why the correct answer wins: Spacing the jobs apart keeps each inside the limit without changing the quota.

### Question 43 — D

Answer: Alert on the database error rate. Alerting on the error rate surfaces the failures users actually experience. Page on failed statements rather than on resource saturation alone. Local study-map skill 2.7 (Alerts for Errors and Performance), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 2 (manage a solution that can span multiple database technologies): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A per-query view of latency, load, and wait events on the instance. Why the correct answer wins: Alerting on the error rate surfaces the failures users actually experience.
- **B:** Incorrect for this question. A condition that pages a human when the threshold is crossed. Why the correct answer wins: Alerting on the error rate surfaces the failures users actually experience.
- **C:** Incorrect for this question. Page when the copy falls behind the primary by more than the budget. Why the correct answer wins: Alerting on the error rate surfaces the failures users actually experience.
- **D:** Correct. Page on failed statements rather than on resource saturation alone. In this case: Alerting on the error rate surfaces the failures users actually experience.

### Question 44 — A

Answer: Build a log-based metric from the error entries. A metric derived from the log pattern makes the occurrences visible. Turn a recurring log pattern into a metric that can be charted and alerted on. Local study-map skill 2.7 (Alerts for Errors and Performance), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 2 (manage a solution that can span multiple database technologies): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Correct. Turn a recurring log pattern into a metric that can be charted and alerted on. In this case: A metric derived from the log pattern makes the occurrences visible.
- **B:** Incorrect for this question. A liveness signal that fires before users report the outage. Why the correct answer wins: A metric derived from the log pattern makes the occurrences visible.
- **C:** Incorrect for this question. Export entries to storage whose retention cannot be shortened. Why the correct answer wins: A metric derived from the log pattern makes the occurrences visible.
- **D:** Incorrect for this question. The engine log of statements that exceeded the long-query threshold. Why the correct answer wins: A metric derived from the log pattern makes the occurrences visible.

### Question 45 — B, C

Answers: Enable point-in-time recovery; Enable automated backups with a retention window. Point-in-time recovery reaches a moment minutes old, and automated backups keep the scheduled recovery points. Continuous log capture that lets the instance return to an arbitrary moment. Scheduled backups kept for a chosen number of days. Local study-map skill 2.8 (Backup and Recovery Option Selection), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 2 (manage a solution that can span multiple database technologies): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A copy of the current data created without touching the source. Why the correct answer wins: Point-in-time recovery reaches a moment minutes old, and automated backups keep the scheduled recovery points.
- **B:** Correct. Scheduled backups kept for a chosen number of days. In this case: Point-in-time recovery reaches a moment minutes old, and automated backups keep the scheduled recovery points.
- **C:** Correct. Continuous log capture that lets the instance return to an arbitrary moment. In this case: Point-in-time recovery reaches a moment minutes old, and automated backups keep the scheduled recovery points.
- **D:** Incorrect for this question. Keep backups longer so an older restore point remains available. Why the correct answer wins: Point-in-time recovery reaches a moment minutes old, and automated backups keep the scheduled recovery points.
- **E:** Incorrect for this question. A manual checkpoint taken immediately before a risky operation. Why the correct answer wins: Point-in-time recovery reaches a moment minutes old, and automated backups keep the scheduled recovery points.

### Question 46 — B

Answer: Clone the instance for the test. A clone gives a production copy to test against while the original serves users. A copy of the current data created without touching the source. Local study-map skill 2.8 (Backup and Recovery Option Selection), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 2 (manage a solution that can span multiple database technologies): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A portable SQL dump taken with the engine tooling. Why the correct answer wins: A clone gives a production copy to test against while the original serves users.
- **B:** Correct. A copy of the current data created without touching the source. In this case: A clone gives a production copy to test against while the original serves users.
- **C:** Incorrect for this question. A manual checkpoint taken immediately before a risky operation. Why the correct answer wins: A clone gives a production copy to test against while the original serves users.
- **D:** Incorrect for this question. A point-in-time restore that discards the later writes on the same instance. Why the correct answer wins: A clone gives a production copy to test against while the original serves users.

### Question 47 — A

Answer: Export a logical dump to Cloud Storage. A logical dump carries schema and data in restorable form. A portable SQL dump taken with the engine tooling. Local study-map skill 2.9 (Export and Import Configuration), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 2 (manage a solution that can span multiple database technologies): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Correct. A portable SQL dump taken with the engine tooling. In this case: A logical dump carries schema and data in restorable form.
- **B:** Incorrect for this question. A flat-file extract for a downstream loader rather than a restore. Why the correct answer wins: A logical dump carries schema and data in restorable form.
- **C:** Incorrect for this question. Read the operational table from BigQuery without copying it first. Why the correct answer wins: A logical dump carries schema and data in restorable form.
- **D:** Incorrect for this question. Load a logical dump file into the database through the managed import path. Why the correct answer wins: A logical dump carries schema and data in restorable form.

### Question 48 — C

Answer: Design the restore path to the stated RTO and RPO. The recovery point and time objectives state the acceptable loss and duration. Choose mechanisms by how much data and time the business can lose. Local study-map skill 2.10 (RTO, RPO, and Point-in-Time Recovery), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 2 (manage a solution that can span multiple database technologies): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Continuous log capture that lets the instance return to an arbitrary moment. Why the correct answer wins: The recovery point and time objectives state the acceptable loss and duration.
- **B:** Incorrect for this question. A copy of the current data created without touching the source. Why the correct answer wins: The recovery point and time objectives state the acceptable loss and duration.
- **C:** Correct. Choose mechanisms by how much data and time the business can lose. In this case: The recovery point and time objectives state the acceptable loss and duration.
- **D:** Incorrect for this question. Scheduled backups kept for a chosen number of days. Why the correct answer wins: The recovery point and time objectives state the acceptable loss and duration.

### Question 49 — B

Answer: Restore to the timestamp before the bad change. Point-in-time recovery replays the log to that moment. A point-in-time restore that discards the later writes on the same instance. Local study-map skill 2.10 (RTO, RPO, and Point-in-Time Recovery), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 2 (manage a solution that can span multiple database technologies): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A copy of the current data created without touching the source. Why the correct answer wins: Point-in-time recovery replays the log to that moment.
- **B:** Correct. A point-in-time restore that discards the later writes on the same instance. In this case: Point-in-time recovery replays the log to that moment.
- **C:** Incorrect for this question. Trigger a switchover in a test window and observe how long writes are unavailable. Why the correct answer wins: Point-in-time recovery replays the log to that moment.
- **D:** Incorrect for this question. A portable SQL dump taken with the engine tooling. Why the correct answer wins: Point-in-time recovery replays the log to that moment.

### Question 50 — A

Answer: Set the garbage-collection policy on the column family. A garbage-collection policy drops superseded versions by age. A rule that drops versions by age or count, which also bounds recovery. Local study-map skill 2.11 (Data Retention Management), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 2 (manage a solution that can span multiple database technologies): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Correct. A rule that drops versions by age or count, which also bounds recovery. In this case: A garbage-collection policy drops superseded versions by age.
- **B:** Incorrect for this question. Expire documents once their usefulness ends. Why the correct answer wins: A garbage-collection policy drops superseded versions by age.
- **C:** Incorrect for this question. Delete or expire records once the legal hold period ends. Why the correct answer wins: A garbage-collection policy drops superseded versions by age.
- **D:** Incorrect for this question. Move aged, rarely read rows out of the hot table into Cloud Storage or BigQuery. Why the correct answer wins: A garbage-collection policy drops superseded versions by age.

### Question 51 — A, C

Answers: Add a read replica for the read traffic; Send reporting queries to the read replica. The replica supplies the capacity, and routing moves the reads onto it. Send reads to a copy so the primary keeps its capacity for writes. Separate analytical reads from the write path. Local study-map skill 2.12 (Scaling Up Versus Scaling Out), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 2 (manage a solution that can span multiple database technologies): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Correct. Separate analytical reads from the write path. In this case: The replica supplies the capacity, and routing moves the reads onto it.
- **B:** Incorrect for this question. Split rows by a key so each instance owns a subset of the workload. Why the correct answer wins: The replica supplies the capacity, and routing moves the reads onto it.
- **C:** Correct. Send reads to a copy so the primary keeps its capacity for writes. In this case: The replica supplies the capacity, and routing moves the reads onto it.
- **D:** Incorrect for this question. Raise provisioned compute in 1000-unit node steps or 100-unit increments. Why the correct answer wins: The replica supplies the capacity, and routing moves the reads onto it.
- **E:** Incorrect for this question. Move the instance to a larger shape so more vCPU and memory serve the same data. Why the correct answer wins: The replica supplies the capacity, and routing moves the reads onto it.

### Question 52 — A

Answer: Increase the machine type of the instance. A larger shape carries the existing load until the application can change. Move the instance to a larger shape so more vCPU and memory serve the same data. Local study-map skill 2.12 (Scaling Up Versus Scaling Out), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 2 (manage a solution that can span multiple database technologies): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Correct. Move the instance to a larger shape so more vCPU and memory serve the same data. In this case: A larger shape carries the existing load until the application can change.
- **B:** Incorrect for this question. Send reads to a copy so the primary keeps its capacity for writes. Why the correct answer wins: A larger shape carries the existing load until the application can change.
- **C:** Incorrect for this question. Separate analytical reads from the write path. Why the correct answer wins: A larger shape carries the existing load until the application can change.
- **D:** Incorrect for this question. Absorb repeated reads in memory so the database sees fewer of them. Why the correct answer wins: A larger shape carries the existing load until the application can change.

### Question 53 — D

Answer: Add a cross-region read replica. A cross-region replica keeps that copy current and can be promoted when the primary is lost. A copy in a second region that serves reads and can be promoted. Local study-map skill 2.13 (Replication Strategies), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 2 (manage a solution that can span multiple database technologies): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. An AlloyDB cross-region copy that can be promoted to a primary cluster. Why the correct answer wins: A cross-region replica keeps that copy current and can be promoted when the primary is lost.
- **B:** Incorrect for this question. Rebuild the database in the surviving region from the latest backup. Why the correct answer wins: A cross-region replica keeps that copy current and can be promoted when the primary is lost.
- **C:** Incorrect for this question. A topology that places replicas in separate regions for regional-failure tolerance. Why the correct answer wins: A cross-region replica keeps that copy current and can be promoted when the primary is lost.
- **D:** Correct. A copy in a second region that serves reads and can be promoted. In this case: A cross-region replica keeps that copy current and can be promoted when the primary is lost.

### Question 54 — D

Answer: Drop the unused index. Removing unused indexes cuts the maintenance cost on every write. Remove write amplification from an index nothing reads. Local study-map skill 2.14 (Query Optimization for Cost and Performance), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 2 (manage a solution that can span multiple database technologies): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Split one table into ranges so pruning and maintenance act on less data. Why the correct answer wins: Removing unused indexes cuts the maintenance cost on every write.
- **B:** Incorrect for this question. Give sorts and joins more working memory on the instance. Why the correct answer wins: Removing unused indexes cuts the maintenance cost on every write.
- **C:** Incorrect for this question. Create an index that turns a scan into a lookup for the predicate. Why the correct answer wins: Removing unused indexes cuts the maintenance cost on every write.
- **D:** Correct. Remove write amplification from an index nothing reads. In this case: Removing unused indexes cuts the maintenance cost on every write.

### Question 55 — D

Answer: Run the task on a managed schedule. A managed schedule performs the recurring work unattended. A recurring trigger that performs the work with nobody present. Local study-map skill 2.15 (Automated Maintenance and Scheduled Exports), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 2 (manage a solution that can span multiple database technologies): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Create the resource interactively with no stored definition. Why the correct answer wins: A managed schedule performs the recurring work unattended.
- **B:** Incorrect for this question. Trigger a switchover in a test window and observe how long writes are unavailable. Why the correct answer wins: A managed schedule performs the recurring work unattended.
- **C:** Incorrect for this question. A manual checkpoint taken immediately before a risky operation. Why the correct answer wins: A managed schedule performs the recurring work unattended.
- **D:** Correct. A recurring trigger that performs the work with nobody present. In this case: A managed schedule performs the recurring work unattended.

### Question 56 — C

Answer: Test the upgrade on a clone first. Testing on a clone exposes the failure while production is untouched. Rehearse the change against a copy before touching production. Local study-map skill 2.15 (Automated Maintenance and Scheduled Exports), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 2 (manage a solution that can span multiple database technologies): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Change the engine version on the running instance during the window. Why the correct answer wins: Testing on a clone exposes the failure while production is untouched.
- **B:** Incorrect for this question. Compare the signal after cutover against the pre-change baseline. Why the correct answer wins: Testing on a clone exposes the failure while production is untouched.
- **C:** Correct. Rehearse the change against a copy before touching production. In this case: Testing on a clone exposes the failure while production is untouched.
- **D:** Incorrect for this question. A recovery point that makes the upgrade reversible in practice. Why the correct answer wins: Testing on a clone exposes the failure while production is untouched.

### Question 57 — C

Answer: Track the availability signal against the agreed objective. Comparing the availability signal with the objective answers the question. Compare observed service levels with the commitment rather than watching raw resource metrics. Local study-map skill 2.16 (Managed Upgrades and SLA Monitoring), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 2 (manage a solution that can span multiple database technologies): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A condition that pages a human when the threshold is crossed. Why the correct answer wins: Comparing the availability signal with the objective answers the question.
- **B:** Incorrect for this question. A single view of health, security, and version posture across database instances. Why the correct answer wins: Comparing the availability signal with the objective answers the question.
- **C:** Correct. Compare observed service levels with the commitment rather than watching raw resource metrics. In this case: Comparing the availability signal with the objective answers the question.
- **D:** Incorrect for this question. Read the instance-level signals before attributing the symptom to the query. Why the correct answer wins: Comparing the availability signal with the objective answers the question.

### Question 58 — C, D

Answers: Use Database Migration Service for the same engine; Follow a cutover runbook with a rollback step. Continuous replication keeps the outage to the switch, and the runbook fixes who approves and what happens if validation fails. A managed migration that moves a supported engine to the same engine on Google Cloud. A rehearsed sequence with a named decision point and a way back. Local study-map skill 3.1 (Migration Strategy and Downtime Budget), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 3 (migrate data solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A bulk load followed by a catch-up pass for the writes made during the load. Why the correct answer wins: Continuous replication keeps the outage to the switch, and the runbook fixes who approves and what happens if validation fails.
- **B:** Incorrect for this question. Stop the source, load everything, and start the target in one window. Why the correct answer wins: Continuous replication keeps the outage to the switch, and the runbook fixes who approves and what happens if validation fails.
- **C:** Correct. A managed migration that moves a supported engine to the same engine on Google Cloud. In this case: Continuous replication keeps the outage to the switch, and the runbook fixes who approves and what happens if validation fails.
- **D:** Correct. A rehearsed sequence with a named decision point and a way back. In this case: Continuous replication keeps the outage to the switch, and the runbook fixes who approves and what happens if validation fails.
- **E:** Incorrect for this question. Keep two databases current from application code during the transition. Why the correct answer wins: Continuous replication keeps the outage to the switch, and the runbook fixes who approves and what happens if validation fails.

### Question 59 — C

Answer: Accept a scheduled extended outage. A stop, load, and start in an accepted window needs no replication topology. Stop the source, load everything, and start the target in one window. Local study-map skill 3.1 (Migration Strategy and Downtime Budget), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 3 (migrate data solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A rehearsed sequence with a named decision point and a way back. Why the correct answer wins: A stop, load, and start in an accepted window needs no replication topology.
- **B:** Incorrect for this question. Keep two databases current from application code during the transition. Why the correct answer wins: A stop, load, and start in an accepted window needs no replication topology.
- **C:** Correct. Stop the source, load everything, and start the target in one window. In this case: A stop, load, and start in an accepted window needs no replication topology.
- **D:** Incorrect for this question. A managed migration that moves a supported engine to the same engine on Google Cloud. Why the correct answer wins: A stop, load, and start in an accepted window needs no replication topology.

### Question 60 — B

Answer: Write to both systems from the application. Writing to both systems from the application keeps them aligned when no engine-level stream exists. Keep two databases current from application code during the transition. Local study-map skill 3.1 (Migration Strategy and Downtime Budget), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 3 (migrate data solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Stop the source, load everything, and start the target in one window. Why the correct answer wins: Writing to both systems from the application keeps them aligned when no engine-level stream exists.
- **B:** Correct. Keep two databases current from application code during the transition. In this case: Writing to both systems from the application keeps them aligned when no engine-level stream exists.
- **C:** Incorrect for this question. Stop application writes so the last increment can be applied cleanly. Why the correct answer wins: Writing to both systems from the application keeps them aligned when no engine-level stream exists.
- **D:** Incorrect for this question. A managed migration that moves a supported engine to the same engine on Google Cloud. Why the correct answer wins: Writing to both systems from the application keeps them aligned when no engine-level stream exists.

### Question 61 — C

Answer: Use Database Migration Service with schema conversion. The heterogeneous managed path pairs conversion with the move. A managed path that converts schema and code from a different source engine. Local study-map skill 3.2 (Migration Tool Selection), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 3 (migrate data solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A managed migration that moves a supported engine to the same engine on Google Cloud. Why the correct answer wins: The heterogeneous managed path pairs conversion with the move.
- **B:** Incorrect for this question. Change data capture from the source into a Google Cloud target. Why the correct answer wins: The heterogeneous managed path pairs conversion with the move.
- **C:** Correct. A managed path that converts schema and code from a different source engine. In this case: The heterogeneous managed path pairs conversion with the move.
- **D:** Incorrect for this question. A bulk load followed by a catch-up pass for the writes made during the load. Why the correct answer wins: The heterogeneous managed path pairs conversion with the move.

### Question 62 — D

Answer: Stream changes with Datastream. Change data capture publishes every committed change to the warehouse. Change data capture from the source into a Google Cloud target. Local study-map skill 3.2 (Migration Tool Selection), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 3 (migrate data solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A portable SQL dump taken with the engine tooling. Why the correct answer wins: Change data capture publishes every committed change to the warehouse.
- **B:** Incorrect for this question. A managed path that converts schema and code from a different source engine. Why the correct answer wins: Change data capture publishes every committed change to the warehouse.
- **C:** Incorrect for this question. Copy the analytical slice into the warehouse on a schedule. Why the correct answer wins: Change data capture publishes every committed change to the warehouse.
- **D:** Correct. Change data capture from the source into a Google Cloud target. In this case: Change data capture publishes every committed change to the warehouse.

### Question 63 — D

Answer: Dump, restore, then replay the changes. A dump and restore copies the database once. A bulk load followed by a catch-up pass for the writes made during the load. Local study-map skill 3.2 (Migration Tool Selection), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 3 (migrate data solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Replay the writes made during the bulk load so the target is current at the switch. Why the correct answer wins: A dump and restore copies the database once.
- **B:** Incorrect for this question. A managed path that converts schema and code from a different source engine. Why the correct answer wins: A dump and restore copies the database once.
- **C:** Incorrect for this question. Keep two databases current from application code during the transition. Why the correct answer wins: A dump and restore copies the database once.
- **D:** Correct. A bulk load followed by a catch-up pass for the writes made during the load. In this case: A dump and restore copies the database once.

### Question 64 — C

Answer: Build the schema in a conversion workspace. The conversion workspace holds the generated schema for review. Convert DDL and code with reviewable, editable output before the load starts. Local study-map skill 3.3 (Heterogeneous Schema and DDL Conversion), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 3 (migrate data solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Compare the target answers with production before the switch. Why the correct answer wins: The conversion workspace holds the generated schema for review.
- **B:** Incorrect for this question. Set generated-key counters past the highest value so inserts do not collide. Why the correct answer wins: The conversion workspace holds the generated schema for review.
- **C:** Correct. Convert DDL and code with reviewable, editable output before the load starts. In this case: The conversion workspace holds the generated schema for review.
- **D:** Incorrect for this question. Port procedural code the conversion tool flags as unsupported. Why the correct answer wins: The conversion workspace holds the generated schema for review.

### Question 65 — B

Answer: Reset the sequences after the bulk load. The counters must be advanced past the highest loaded value. Set generated-key counters past the highest value so inserts do not collide. Local study-map skill 3.3 (Heterogeneous Schema and DDL Conversion), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 3 (migrate data solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Convert DDL and code with reviewable, editable output before the load starts. Why the correct answer wins: The counters must be advanced past the highest loaded value.
- **B:** Correct. Set generated-key counters past the highest value so inserts do not collide. In this case: The counters must be advanced past the highest loaded value.
- **C:** Incorrect for this question. Port procedural code the conversion tool flags as unsupported. Why the correct answer wins: The counters must be advanced past the highest loaded value.
- **D:** Incorrect for this question. Prove the target holds the same rows as the source before cutover. Why the correct answer wins: The counters must be advanced past the highest loaded value.

### Question 66 — A, C

Answers: Rewrite the stored procedures and DML by hand; Replay read traffic against the target. Incompatible statements must be rewritten for the target, and replaying real queries shows whether the rewrite behaves the same. Port procedural code the conversion tool flags as unsupported. Compare the target answers with production before the switch. Local study-map skill 3.4 (DML and Application Code Conversion), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 3 (migrate data solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Correct. Compare the target answers with production before the switch. In this case: Incompatible statements must be rewritten for the target, and replaying real queries shows whether the rewrite behaves the same.
- **B:** Incorrect for this question. Set generated-key counters past the highest value so inserts do not collide. Why the correct answer wins: Incompatible statements must be rewritten for the target, and replaying real queries shows whether the rewrite behaves the same.
- **C:** Correct. Port procedural code the conversion tool flags as unsupported. In this case: Incompatible statements must be rewritten for the target, and replaying real queries shows whether the rewrite behaves the same.
- **D:** Incorrect for this question. Convert DDL and code with reviewable, editable output before the load starts. Why the correct answer wins: Incompatible statements must be rewritten for the target, and replaying real queries shows whether the rewrite behaves the same.
- **E:** Incorrect for this question. Keep two databases current from application code during the transition. Why the correct answer wins: Incompatible statements must be rewritten for the target, and replaying real queries shows whether the rewrite behaves the same.

### Question 67 — B

Answer: Replay read traffic against the target. Replaying those statements exercises the real query paths. Compare the target answers with production before the switch. Local study-map skill 3.4 (DML and Application Code Conversion), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 3 (migrate data solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Prove the target holds the same rows as the source before cutover. Why the correct answer wins: Replaying those statements exercises the real query paths.
- **B:** Correct. Compare the target answers with production before the switch. In this case: Replaying those statements exercises the real query paths.
- **C:** Incorrect for this question. Port procedural code the conversion tool flags as unsupported. Why the correct answer wins: Replaying those statements exercises the real query paths.
- **D:** Incorrect for this question. A rehearsed sequence with a named decision point and a way back. Why the correct answer wins: Replaying those statements exercises the real query paths.

### Question 68 — A

Answer: Use the engine native logical replication. Replicating the source's change stream keeps the target current throughout. Replicate row changes from the source using the engine feature itself. Local study-map skill 3.5 (Initial Load and Change Replication), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 3 (migrate data solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Correct. Replicate row changes from the source using the engine feature itself. In this case: Replicating the source's change stream keeps the target current throughout.
- **B:** Incorrect for this question. Stop the source, load everything, and start the target in one window. Why the correct answer wins: Replicating the source's change stream keeps the target current throughout.
- **C:** Incorrect for this question. A portable SQL dump taken with the engine tooling. Why the correct answer wins: Replicating the source's change stream keeps the target current throughout.
- **D:** Incorrect for this question. Keep two databases current from application code during the transition. Why the correct answer wins: Replicating the source's change stream keeps the target current throughout.

### Question 69 — D

Answer: Apply the captured change backlog before cutover. The captured backlog must be applied so every change is present. Replay the writes made during the bulk load so the target is current at the switch. Local study-map skill 3.5 (Initial Load and Change Replication), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 3 (migrate data solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Move clients to the new endpoint as the final cutover action. Why the correct answer wins: The captured backlog must be applied so every change is present.
- **B:** Incorrect for this question. Prove the target holds the same rows as the source before cutover. Why the correct answer wins: The captured backlog must be applied so every change is present.
- **C:** Incorrect for this question. Stop application writes so the last increment can be applied cleanly. Why the correct answer wins: The captured backlog must be applied so every change is present.
- **D:** Correct. Replay the writes made during the bulk load so the target is current at the switch. In this case: The captured backlog must be applied so every change is present.

### Question 70 — D

Answer: Reconcile row counts and checksums. Comparing the same aggregates on both systems localises the difference. Prove the target holds the same rows as the source before cutover. Local study-map skill 3.6 (Validation and Reconciliation), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 3 (migrate data solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Move clients to the new endpoint as the final cutover action. Why the correct answer wins: Comparing the same aggregates on both systems localises the difference.
- **B:** Incorrect for this question. Compare the target answers with production before the switch. Why the correct answer wins: Comparing the same aggregates on both systems localises the difference.
- **C:** Incorrect for this question. Set generated-key counters past the highest value so inserts do not collide. Why the correct answer wins: Comparing the same aggregates on both systems localises the difference.
- **D:** Correct. Prove the target holds the same rows as the source before cutover. In this case: Comparing the same aggregates on both systems localises the difference.

### Question 71 — B

Answer: Replay read traffic against the target. Running the report statements on both systems and comparing output tests behaviour. Compare the target answers with production before the switch. Local study-map skill 3.6 (Validation and Reconciliation), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 3 (migrate data solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A rehearsed sequence with a named decision point and a way back. Why the correct answer wins: Running the report statements on both systems and comparing output tests behaviour.
- **B:** Correct. Compare the target answers with production before the switch. In this case: Running the report statements on both systems and comparing output tests behaviour.
- **C:** Incorrect for this question. Prove the target holds the same rows as the source before cutover. Why the correct answer wins: Running the report statements on both systems and comparing output tests behaviour.
- **D:** Incorrect for this question. Keep two databases current from application code during the transition. Why the correct answer wins: Running the report statements on both systems and comparing output tests behaviour.

### Question 72 — A, B

Answers: Freeze writes during the cutover; Repoint the connection string at the target. Stopping writes creates a stable point for the final increment, and repointing the connection string moves the clients. Stop application writes so the last increment can be applied cleanly. Move clients to the new endpoint as the final cutover action. Local study-map skill 3.7 (Cutover and Fallback Planning), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 3 (migrate data solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Correct. Stop application writes so the last increment can be applied cleanly. In this case: Stopping writes creates a stable point for the final increment, and repointing the connection string moves the clients.
- **B:** Correct. Move clients to the new endpoint as the final cutover action. In this case: Stopping writes creates a stable point for the final increment, and repointing the connection string moves the clients.
- **C:** Incorrect for this question. Keep the old system read-only for a defined period, then remove it. Why the correct answer wins: Stopping writes creates a stable point for the final increment, and repointing the connection string moves the clients.
- **D:** Incorrect for this question. A rehearsed sequence with a named decision point and a way back. Why the correct answer wins: Stopping writes creates a stable point for the final increment, and repointing the connection string moves the clients.
- **E:** Incorrect for this question. Size the cutover from how fast changes replay, not from the data volume alone. Why the correct answer wins: Stopping writes creates a stable point for the final increment, and repointing the connection string moves the clients.

### Question 73 — B

Answer: Follow a cutover runbook with a rollback step. A runbook with an abort condition and rollback steps answers that question in advance. A rehearsed sequence with a named decision point and a way back. Local study-map skill 3.7 (Cutover and Fallback Planning), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 3 (migrate data solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Stop application writes so the last increment can be applied cleanly. Why the correct answer wins: A runbook with an abort condition and rollback steps answers that question in advance.
- **B:** Correct. A rehearsed sequence with a named decision point and a way back. In this case: A runbook with an abort condition and rollback steps answers that question in advance.
- **C:** Incorrect for this question. Move clients to the new endpoint as the final cutover action. Why the correct answer wins: A runbook with an abort condition and rollback steps answers that question in advance.
- **D:** Incorrect for this question. Keep two databases current from application code during the transition. Why the correct answer wins: A runbook with an abort condition and rollback steps answers that question in advance.

### Question 74 — C

Answer: Measure the catch-up rate before choosing the window. The observed replay rate against the backlog shows whether the window holds. Size the cutover from how fast changes replay, not from the data volume alone. Local study-map skill 3.7 (Cutover and Fallback Planning), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 3 (migrate data solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Stop the source, load everything, and start the target in one window. Why the correct answer wins: The observed replay rate against the backlog shows whether the window holds.
- **B:** Incorrect for this question. Move clients to the new endpoint as the final cutover action. Why the correct answer wins: The observed replay rate against the backlog shows whether the window holds.
- **C:** Correct. Size the cutover from how fast changes replay, not from the data volume alone. In this case: The observed replay rate against the backlog shows whether the window holds.
- **D:** Incorrect for this question. Stop application writes so the last increment can be applied cleanly. Why the correct answer wins: The observed replay rate against the backlog shows whether the window holds.

### Question 75 — A

Answer: Set up reverse replication to the source. Replication from the target back to the source publishes those writes. Keep writing back to the original system so a rollback loses nothing. Local study-map skill 3.8 (Reverse Replication to the Source), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 3 (migrate data solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Correct. Keep writing back to the original system so a rollback loses nothing. In this case: Replication from the target back to the source publishes those writes.
- **B:** Incorrect for this question. Keep the old system read-only for a defined period, then remove it. Why the correct answer wins: Replication from the target back to the source publishes those writes.
- **C:** Incorrect for this question. Move clients to the new endpoint as the final cutover action. Why the correct answer wins: Replication from the target back to the source publishes those writes.
- **D:** Incorrect for this question. Keep two databases current from application code during the transition. Why the correct answer wins: Replication from the target back to the source publishes those writes.

### Question 76 — A

Answer: Decommission the source after a parallel period. A parallel period with exit criteria sets that boundary. Keep the old system read-only for a defined period, then remove it. Local study-map skill 3.8 (Reverse Replication to the Source), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 3 (migrate data solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Correct. Keep the old system read-only for a defined period, then remove it. In this case: A parallel period with exit criteria sets that boundary.
- **B:** Incorrect for this question. Move clients to the new endpoint as the final cutover action. Why the correct answer wins: A parallel period with exit criteria sets that boundary.
- **C:** Incorrect for this question. Keep writing back to the original system so a rollback loses nothing. Why the correct answer wins: A parallel period with exit criteria sets that boundary.
- **D:** Incorrect for this question. Check the connection and traffic evidence before retiring an instance. Why the correct answer wins: A parallel period with exit criteria sets that boundary.

### Question 77 — A, C

Answers: Use the engine native logical replication; Measure the catch-up rate before choosing the window. Keeping replication running preserves the retry path, and a measured catch-up rate proves the window. Replicate row changes from the source using the engine feature itself. Size the cutover from how fast changes replay, not from the data volume alone. Local study-map skill 3.9 (Minimizing Downtime During Migration), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 3 (migrate data solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Correct. Replicate row changes from the source using the engine feature itself. In this case: Keeping replication running preserves the retry path, and a measured catch-up rate proves the window.
- **B:** Incorrect for this question. Keep two databases current from application code during the transition. Why the correct answer wins: Keeping replication running preserves the retry path, and a measured catch-up rate proves the window.
- **C:** Correct. Size the cutover from how fast changes replay, not from the data volume alone. In this case: Keeping replication running preserves the retry path, and a measured catch-up rate proves the window.
- **D:** Incorrect for this question. A bulk load followed by a catch-up pass for the writes made during the load. Why the correct answer wins: Keeping replication running preserves the retry path, and a measured catch-up rate proves the window.
- **E:** Incorrect for this question. Stop the source, load everything, and start the target in one window. Why the correct answer wins: Keeping replication running preserves the retry path, and a measured catch-up rate proves the window.

### Question 78 — D

Answer: Move the job outside the contention window. Scheduling away from the known surge keeps the catch-up inside the window. Stagger the work so concurrent operations stop colliding on the same limit. Local study-map skill 3.9 (Minimizing Downtime During Migration), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 3 (migrate data solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Size the cutover from how fast changes replay, not from the data volume alone. Why the correct answer wins: Scheduling away from the known surge keeps the catch-up inside the window.
- **B:** Incorrect for this question. Stop the source, load everything, and start the target in one window. Why the correct answer wins: Scheduling away from the known surge keeps the catch-up inside the window.
- **C:** Incorrect for this question. Keep two databases current from application code during the transition. Why the correct answer wins: Scheduling away from the known surge keeps the catch-up inside the window.
- **D:** Correct. Stagger the work so concurrent operations stop colliding on the same limit. In this case: Scheduling away from the known surge keeps the catch-up inside the window.

### Question 79 — A

Answer: Confirm no client still uses the old endpoint. Connection and traffic evidence shows whether any client remains. Check the connection and traffic evidence before retiring an instance. Local study-map skill 3.10 (Source Decommissioning), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 3 (migrate data solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Correct. Check the connection and traffic evidence before retiring an instance. In this case: Connection and traffic evidence shows whether any client remains.
- **B:** Incorrect for this question. Prove the target holds the same rows as the source before cutover. Why the correct answer wins: Connection and traffic evidence shows whether any client remains.
- **C:** Incorrect for this question. Keep the old system read-only for a defined period, then remove it. Why the correct answer wins: Connection and traffic evidence shows whether any client remains.
- **D:** Incorrect for this question. Move clients to the new endpoint as the final cutover action. Why the correct answer wins: Connection and traffic evidence shows whether any client remains.

### Question 80 — D

Answer: Export the table into BigQuery. Copying the history into the warehouse keeps it queryable. Copy the analytical slice into the warehouse on a schedule. Local study-map skill 3.10 (Source Decommissioning), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 3 (migrate data solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Interconnect the remaining on-premises system rather than moving it. Why the correct answer wins: Copying the history into the warehouse keeps it queryable.
- **B:** Incorrect for this question. Keep writing back to the original system so a rollback loses nothing. Why the correct answer wins: Copying the history into the warehouse keeps it queryable.
- **C:** Incorrect for this question. Keep the old system read-only for a defined period, then remove it. Why the correct answer wins: Copying the history into the warehouse keeps it queryable.
- **D:** Correct. Copy the analytical slice into the warehouse on a schedule. In this case: Copying the history into the warehouse keeps it queryable.

### Question 81 — C

Answer: Provision the instance with a Terraform module. A declared module reproduces the estate from one definition. Declare the database so the same definition creates every environment. Local study-map skill 4.1 (Provisioning Highly Available Instances), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 4 (deploy scalable and highly available databases in Google Cloud): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A copy of the current data created without touching the source. Why the correct answer wins: A declared module reproduces the estate from one definition.
- **B:** Incorrect for this question. Run the new version beside the old one and move traffic when it is proven. Why the correct answer wins: A declared module reproduces the estate from one definition.
- **C:** Correct. Declare the database so the same definition creates every environment. In this case: A declared module reproduces the estate from one definition.
- **D:** Incorrect for this question. Create the resource interactively with no stored definition. Why the correct answer wins: A declared module reproduces the estate from one definition.

### Question 82 — D

Answer: Apply the change through the infrastructure pipeline. Applying changes through the pipeline records approval and change together. Send database changes through review and version control like any other code. Local study-map skill 4.1 (Provisioning Highly Available Instances), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 4 (deploy scalable and highly available databases in Google Cloud): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Create the resource interactively with no stored definition. Why the correct answer wins: Applying changes through the pipeline records approval and change together.
- **B:** Incorrect for this question. Rehearse the change against a copy before touching production. Why the correct answer wins: Applying changes through the pipeline records approval and change together.
- **C:** Incorrect for this question. A single view of health, security, and version posture across database instances. Why the correct answer wins: Applying changes through the pipeline records approval and change together.
- **D:** Correct. Send database changes through review and version control like any other code. In this case: Applying changes through the pipeline records approval and change together.

### Question 83 — D

Answer: Provision the instance with a Terraform module. A module applies one definition across every instance. Declare the database so the same definition creates every environment. Local study-map skill 4.1 (Provisioning Highly Available Instances), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 4 (deploy scalable and highly available databases in Google Cloud): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Run the new version beside the old one and move traffic when it is proven. Why the correct answer wins: A module applies one definition across every instance.
- **B:** Incorrect for this question. A recovery point that makes the upgrade reversible in practice. Why the correct answer wins: A module applies one definition across every instance.
- **C:** Incorrect for this question. Create the resource interactively with no stored definition. Why the correct answer wins: A module applies one definition across every instance.
- **D:** Correct. Declare the database so the same definition creates every environment. In this case: A module applies one definition across every instance.

### Question 84 — A, B

Answers: Run a controlled failover test; Rehearse the promotion in a test project. A controlled failover proves the standby takeover, and a promotion drill proves the regional path. Trigger a switchover in a test window and observe how long writes are unavailable. Practise the failover that the runbook would perform for real. Local study-map skill 4.2 (Testing High Availability and Disaster Recovery), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 4 (deploy scalable and highly available databases in Google Cloud): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Correct. Practise the failover that the runbook would perform for real. In this case: A controlled failover proves the standby takeover, and a promotion drill proves the regional path.
- **B:** Correct. Trigger a switchover in a test window and observe how long writes are unavailable. In this case: A controlled failover proves the standby takeover, and a promotion drill proves the regional path.
- **C:** Incorrect for this question. A recovery point that makes the upgrade reversible in practice. Why the correct answer wins: A controlled failover proves the standby takeover, and a promotion drill proves the regional path.
- **D:** Incorrect for this question. Rebuild the database in the surviving region from the latest backup. Why the correct answer wins: A controlled failover proves the standby takeover, and a promotion drill proves the regional path.
- **E:** Incorrect for this question. Compare the signal after cutover against the pre-change baseline. Why the correct answer wins: A controlled failover proves the standby takeover, and a promotion drill proves the regional path.

### Question 85 — C

Answer: Restore the backup into the second region. Restoring the backup in the second region tests the rebuild path. Rebuild the database in the surviving region from the latest backup. Local study-map skill 4.2 (Testing High Availability and Disaster Recovery), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 4 (deploy scalable and highly available databases in Google Cloud): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Practise the failover that the runbook would perform for real. Why the correct answer wins: Restoring the backup in the second region tests the rebuild path.
- **B:** Incorrect for this question. Trigger a switchover in a test window and observe how long writes are unavailable. Why the correct answer wins: Restoring the backup in the second region tests the rebuild path.
- **C:** Correct. Rebuild the database in the surviving region from the latest backup. In this case: Restoring the backup in the second region tests the rebuild path.
- **D:** Incorrect for this question. A recovery point that makes the upgrade reversible in practice. Why the correct answer wins: Restoring the backup in the second region tests the rebuild path.

### Question 86 — C

Answer: Pre-size the promoted replica for the full load. The standby must be sized for the load it will inherit. Give the standby enough capacity to carry production alone. Local study-map skill 4.2 (Testing High Availability and Disaster Recovery), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 4 (deploy scalable and highly available databases in Google Cloud): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Keep spare capacity so a failover or a traffic spike does not saturate the instance. Why the correct answer wins: The standby must be sized for the load it will inherit.
- **B:** Incorrect for this question. Rebuild the database in the surviving region from the latest backup. Why the correct answer wins: The standby must be sized for the load it will inherit.
- **C:** Correct. Give the standby enough capacity to carry production alone. In this case: The standby must be sized for the load it will inherit.
- **D:** Incorrect for this question. Send reads to a copy so the primary keeps its capacity for writes. Why the correct answer wins: The standby must be sized for the load it will inherit.

### Question 87 — B

Answer: Choose a multi-region instance configuration. A multi-region configuration keeps quorum across regions. A topology that places replicas in separate regions for regional-failure tolerance. Local study-map skill 4.3 (Multi-Regional Replication Setup), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 4 (deploy scalable and highly available databases in Google Cloud): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A copy in a second region that serves reads and can be promoted. Why the correct answer wins: A multi-region configuration keeps quorum across regions.
- **B:** Correct. A topology that places replicas in separate regions for regional-failure tolerance. In this case: A multi-region configuration keeps quorum across regions.
- **C:** Incorrect for this question. A primary and standby in two zones of one region with automatic failover. Why the correct answer wins: A multi-region configuration keeps quorum across regions.
- **D:** Incorrect for this question. Rebuild the database in the surviving region from the latest backup. Why the correct answer wins: A multi-region configuration keeps quorum across regions.

### Question 88 — A

Answer: Add a secondary cluster in the second region. A secondary cluster serves reads and can be promoted. An AlloyDB cross-region copy that can be promoted to a primary cluster. Local study-map skill 4.3 (Multi-Regional Replication Setup), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 4 (deploy scalable and highly available databases in Google Cloud): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Correct. An AlloyDB cross-region copy that can be promoted to a primary cluster. In this case: A secondary cluster serves reads and can be promoted.
- **B:** Incorrect for this question. One instance in one zone with no standby, so a zone failure stops writes. Why the correct answer wins: A secondary cluster serves reads and can be promoted.
- **C:** Incorrect for this question. Rebuild the database in the surviving region from the latest backup. Why the correct answer wins: A secondary cluster serves reads and can be promoted.
- **D:** Incorrect for this question. Grow the AlloyDB read pool that serves read-only connections. Why the correct answer wins: A secondary cluster serves reads and can be promoted.

### Question 89 — B

Answer: Route the app profile across both clusters. Multi-cluster routing performs the failover for the client. A Bigtable app profile that fails over between clusters without a client change. Local study-map skill 4.3 (Multi-Regional Replication Setup), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 4 (deploy scalable and highly available databases in Google Cloud): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. An AlloyDB cross-region copy that can be promoted to a primary cluster. Why the correct answer wins: Multi-cluster routing performs the failover for the client.
- **B:** Correct. A Bigtable app profile that fails over between clusters without a client change. In this case: Multi-cluster routing performs the failover for the client.
- **C:** Incorrect for this question. A copy in a second region that serves reads and can be promoted. Why the correct answer wins: Multi-cluster routing performs the failover for the client.
- **D:** Incorrect for this question. A Bigtable app profile that keeps a workload on one cluster for predictable latency. Why the correct answer wins: Multi-cluster routing performs the failover for the client.

### Question 90 — B

Answer: Add nodes to the read pool. Adding read-pool nodes adds capacity in the tier the review found saturated. Grow the AlloyDB read pool that serves read-only connections. Local study-map skill 4.4 (Read Replicas and Read Pools), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 4 (deploy scalable and highly available databases in Google Cloud): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Separate analytical reads from the write path. Why the correct answer wins: Adding read-pool nodes adds capacity in the tier the review found saturated.
- **B:** Correct. Grow the AlloyDB read pool that serves read-only connections. In this case: Adding read-pool nodes adds capacity in the tier the review found saturated.
- **C:** Incorrect for this question. Move the instance to a larger shape so more vCPU and memory serve the same data. Why the correct answer wins: Adding read-pool nodes adds capacity in the tier the review found saturated.
- **D:** Incorrect for this question. Absorb repeated reads in memory so the database sees fewer of them. Why the correct answer wins: Adding read-pool nodes adds capacity in the tier the review found saturated.

### Question 91 — A

Answer: Send reporting queries to the read replica. Routing the reports to the idle replica uses capacity already paid for. Separate analytical reads from the write path. Local study-map skill 4.4 (Read Replicas and Read Pools), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 4 (deploy scalable and highly available databases in Google Cloud): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Correct. Separate analytical reads from the write path. In this case: Routing the reports to the idle replica uses capacity already paid for.
- **B:** Incorrect for this question. Absorb repeated reads in memory so the database sees fewer of them. Why the correct answer wins: Routing the reports to the idle replica uses capacity already paid for.
- **C:** Incorrect for this question. Send reads to a copy so the primary keeps its capacity for writes. Why the correct answer wins: Routing the reports to the idle replica uses capacity already paid for.
- **D:** Incorrect for this question. Move the instance to a larger shape so more vCPU and memory serve the same data. Why the correct answer wins: Routing the reports to the idle replica uses capacity already paid for.

### Question 92 — A

Answer: Provision the instance with a Terraform module. A parameterised module creates each instance from one definition. Declare the database so the same definition creates every environment. Local study-map skill 4.5 (Automating Database Provisioning), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 4 (deploy scalable and highly available databases in Google Cloud): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Correct. Declare the database so the same definition creates every environment. In this case: A parameterised module creates each instance from one definition.
- **B:** Incorrect for this question. Create the resource interactively with no stored definition. Why the correct answer wins: A parameterised module creates each instance from one definition.
- **C:** Incorrect for this question. Rehearse the change against a copy before touching production. Why the correct answer wins: A parameterised module creates each instance from one definition.
- **D:** Incorrect for this question. A single view of health, security, and version posture across database instances. Why the correct answer wins: A parameterised module creates each instance from one definition.

### Question 93 — A

Answer: Apply the change through the infrastructure pipeline. Validation in the pipeline refuses the change before creation. Send database changes through review and version control like any other code. Local study-map skill 4.5 (Automating Database Provisioning), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 4 (deploy scalable and highly available databases in Google Cloud): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Correct. Send database changes through review and version control like any other code. In this case: Validation in the pipeline refuses the change before creation.
- **B:** Incorrect for this question. A copy of the current data created without touching the source. Why the correct answer wins: Validation in the pipeline refuses the change before creation.
- **C:** Incorrect for this question. Create the resource interactively with no stored definition. Why the correct answer wins: Validation in the pipeline refuses the change before creation.
- **D:** Incorrect for this question. A recovery point that makes the upgrade reversible in practice. Why the correct answer wins: Validation in the pipeline refuses the change before creation.

### Question 94 — B, E

Answers: Create an alerting policy on the metric; Alert when the instance is unreachable. An alert on the failover signal reports the event, and a query probe confirms the instance still serves. A condition that pages a human when the threshold is crossed. A liveness signal that fires before users report the outage. Local study-map skill 4.6 (Monitoring Highly Available Databases), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 4 (deploy scalable and highly available databases in Google Cloud): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A per-query view of latency, load, and wait events on the instance. Why the correct answer wins: An alert on the failover signal reports the event, and a query probe confirms the instance still serves.
- **B:** Correct. A condition that pages a human when the threshold is crossed. In this case: An alert on the failover signal reports the event, and a query probe confirms the instance still serves.
- **C:** Incorrect for this question. A single view of health, security, and version posture across database instances. Why the correct answer wins: An alert on the failover signal reports the event, and a query probe confirms the instance still serves.
- **D:** Incorrect for this question. Read the instance-level signals before attributing the symptom to the query. Why the correct answer wins: An alert on the failover signal reports the event, and a query probe confirms the instance still serves.
- **E:** Correct. A liveness signal that fires before users report the outage. In this case: An alert on the failover signal reports the event, and a query probe confirms the instance still serves.

### Question 95 — B

Answer: Review the fleet in Database Center. The fleet inventory reports engine versions and health across all instances in one place. A single view of health, security, and version posture across database instances. Local study-map skill 4.6 (Monitoring Highly Available Databases), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 4 (deploy scalable and highly available databases in Google Cloud): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. The engine log of statements that exceeded the long-query threshold. Why the correct answer wins: The fleet inventory reports engine versions and health across all instances in one place.
- **B:** Correct. A single view of health, security, and version posture across database instances. In this case: The fleet inventory reports engine versions and health across all instances in one place.
- **C:** Incorrect for this question. A per-query view of latency, load, and wait events on the instance. Why the correct answer wins: The fleet inventory reports engine versions and health across all instances in one place.
- **D:** Incorrect for this question. Read the instance-level signals before attributing the symptom to the query. Why the correct answer wins: The fleet inventory reports engine versions and health across all instances in one place.

### Question 96 — C

Answer: Promote the cross-region replica during the outage. Promoting the current copy meets both targets and avoids a restore. Turn the replica into an independent primary so the application can resume writes. Local study-map skill 4.7 (Regional Failover Mechanics), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 4 (deploy scalable and highly available databases in Google Cloud): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A point-in-time restore that discards the later writes on the same instance. Why the correct answer wins: Promoting the current copy meets both targets and avoids a restore.
- **B:** Incorrect for this question. Trigger a switchover in a test window and observe how long writes are unavailable. Why the correct answer wins: Promoting the current copy meets both targets and avoids a restore.
- **C:** Correct. Turn the replica into an independent primary so the application can resume writes. In this case: Promoting the current copy meets both targets and avoids a restore.
- **D:** Incorrect for this question. Rebuild the database in the surviving region from the latest backup. Why the correct answer wins: Promoting the current copy meets both targets and avoids a restore.

### Question 97 — B

Answer: Fence the old primary before promotion. The returning instance must be prevented from accepting writes. Stop the former primary from accepting writes so two instances cannot both claim the role. Local study-map skill 4.7 (Regional Failover Mechanics), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 4 (deploy scalable and highly available databases in Google Cloud): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Keep writing back to the original system so a rollback loses nothing. Why the correct answer wins: The returning instance must be prevented from accepting writes.
- **B:** Correct. Stop the former primary from accepting writes so two instances cannot both claim the role. In this case: The returning instance must be prevented from accepting writes.
- **C:** Incorrect for this question. Stop application writes so the last increment can be applied cleanly. Why the correct answer wins: The returning instance must be prevented from accepting writes.
- **D:** Incorrect for this question. A rehearsed sequence with a named decision point and a way back. Why the correct answer wins: The returning instance must be prevented from accepting writes.

### Question 98 — A

Answer: Use the language connector with IAM credentials. The language connector resolves the instance on each connection. A client library that resolves the instance and authorizes the connection with IAM. Local study-map skill 4.8 (Connection Routing and Load Balancing), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 4 (deploy scalable and highly available databases in Google Cloud): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Correct. A client library that resolves the instance and authorizes the connection with IAM. In this case: The language connector resolves the instance on each connection.
- **B:** Incorrect for this question. A public-IP allowlist that admits the caller range. Why the correct answer wins: The language connector resolves the instance on each connection.
- **C:** Incorrect for this question. Move clients to the new endpoint as the final cutover action. Why the correct answer wins: The language connector resolves the instance on each connection.
- **D:** Incorrect for this question. A pooler that multiplexes many application connections onto few database sessions. Why the correct answer wins: The language connector resolves the instance on each connection.

### Question 99 — A

Answer: Reserve headroom above the measured peak. Spare capacity above the combined peak is what lets the promoted instance hold the latency objective. Keep spare capacity so a failover or a traffic spike does not saturate the instance. Local study-map skill 4.9 (Failover Capacity Headroom), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 4 (deploy scalable and highly available databases in Google Cloud): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Correct. Keep spare capacity so a failover or a traffic spike does not saturate the instance. In this case: Spare capacity above the combined peak is what lets the promoted instance hold the latency objective.
- **B:** Incorrect for this question. Send reads to a copy so the primary keeps its capacity for writes. Why the correct answer wins: Spare capacity above the combined peak is what lets the promoted instance hold the latency objective.
- **C:** Incorrect for this question. Match capacity to the daily traffic shape. Why the correct answer wins: Spare capacity above the combined peak is what lets the promoted instance hold the latency objective.
- **D:** Incorrect for this question. Shrink an instance whose peak fits a smaller shape. Why the correct answer wins: Spare capacity above the combined peak is what lets the promoted instance hold the latency objective.

### Question 100 — A

Answer: Pre-size the promoted replica for the full load. The standby must be provisioned for production load in advance. Give the standby enough capacity to carry production alone. Local study-map skill 4.9 (Failover Capacity Headroom), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 4 (deploy scalable and highly available databases in Google Cloud): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Correct. Give the standby enough capacity to carry production alone. In this case: The standby must be provisioned for production load in advance.
- **B:** Incorrect for this question. Match capacity to the daily traffic shape. Why the correct answer wins: The standby must be provisioned for production load in advance.
- **C:** Incorrect for this question. Send reads to a copy so the primary keeps its capacity for writes. Why the correct answer wins: The standby must be provisioned for production load in advance.
- **D:** Incorrect for this question. Keep spare capacity so a failover or a traffic spike does not saturate the instance. Why the correct answer wins: The standby must be provisioned for production load in advance.
