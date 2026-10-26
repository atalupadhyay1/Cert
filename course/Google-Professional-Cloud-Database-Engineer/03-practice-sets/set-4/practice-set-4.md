# Google Cloud Professional Cloud Database Engineer — Full-Length Mock Exam 4

Professional Cloud Database Engineer · 100 questions · expanded practice bank · passing score not published

Blueprint-weighted mock exam. Item mix: 84 multiple-choice and 16 multiple-select items (the selection count is stated in each multi-select stem). The live exam publishes 50-60 multiple-choice and multiple-select questions and has no case-study component, so this set is larger on purpose and no case-study item is reproduced. The live paper allows two hours for 50-60 items, so this 100-item set is a slower-per-item rehearsal: about 72 seconds per item here against roughly 120-144 seconds live. Use it to build a habit of finishing with time to review. See the README for the exact fidelity boundary.

Original educational content, not actual, recalled, or copied Google exam items.

## Questions

---

## Domain 1 — Design Innovative, Scalable, and Highly Available Cloud Database Solutions (Sizing, Availability Design, and Database Selection)

### 1. A new multi-tenant service has no production history, but its staging environment can take representative traffic. How should the team size the database?

- A. Commit to the steady baseline capacity
- B. Load-test the workload to derive the size
- C. Reserve headroom above the measured peak
- D. Size the instance from the observed peak metrics

### 2. Finance asks a team to justify a proposed resize with evidence rather than opinion. What should the proposal rest on?

- A. Load-test the workload to derive the size
- B. Commit to the steady baseline capacity
- C. Size the instance from the observed peak metrics
- D. Reduce the machine type to match observed use

### 3. A Bigtable cluster behind a live feed must serve more read throughput at lower latency. Which two changes should the team make? Select two.

- A. Move the data to HDD storage
- B. Add nodes to the Bigtable cluster
- C. Set the garbage-collection policy on the column family
- D. Move the data to SSD storage
- E. Change the row-key design

### 4. A Cloud SQL instance reaches its disk throughput ceiling during nightly loads while compute stays at thirty percent. What should the team do?

- A. Let the disk grow automatically
- B. Increase the machine type of the instance
- C. Add a read replica for the read traffic
- D. Increase the disk size to raise throughput

### 5. A Cloud SQL for PostgreSQL instance has a sixty-gigabyte working set and twenty gigabytes of memory, and cache misses dominate latency. What should the team do?

- A. Put a session pooler in front of the instance
- B. Increase the disk size to raise throughput
- C. Add a read replica for the read traffic
- D. Increase the machine type of the instance

### 6. A Spanner instance at three nodes shows sustained CPU above eighty percent with a fixed, predictable workload. What should the team do?

- A. Enable autoscaling on the instance
- B. Add processing units to the Spanner instance
- C. Add nodes to the Bigtable cluster
- D. Increase the machine type of the instance

### 7. A service must survive a single zone failure with automatic failover and has no cross-region requirement. Which topology fits?

- A. Restore the backup into the second region
- B. Choose a multi-region instance configuration
- C. Add a cross-region read replica
- D. Enable regional high availability with a standby zone

### 8. A Spanner-backed service must keep accepting writes when one region is lost. Which configuration provides that?

- A. Run a single zonal instance
- B. Add a cross-region read replica
- C. Enable regional high availability with a standby zone
- D. Choose a multi-region instance configuration

### 9. A team has no cross-region replica but must document how it would recover in a second region within four hours. Which approach fits?

- A. Set a deny maintenance period over the peak event
- B. Restore the backup into the second region
- C. Promote the cross-region replica during the outage
- D. Enable regional high availability with a standby zone

### 10. A team must schedule weekly patching in the quietest hour for a service used across two continents. What should it configure?

- A. Schedule the maintenance window in the low-traffic period
- B. Set a deny maintenance period over the peak event
- C. Run a controlled failover test
- D. Perform an in-place major version upgrade

### 11. A product launch week must be free of any database interruption, and patching can resume the week after. What should the team set?

- A. Set a deny maintenance period over the peak event
- B. Take a backup before the upgrade
- C. Schedule the maintenance window in the low-traffic period
- D. Restart the instance in the window

### 12. A team must reach a Cloud SQL instance from a project with no VPC peering, privately and with identity-based authorization. Select two.

- A. Publish the instance behind Private Service Connect
- B. Enable IAM database authentication
- C. Use the public IP with enforced SSL
- D. Add the client range to authorized networks
- E. Connect over private IP inside the VPC

### 13. A developer laptop outside the VPC must reach a Cloud SQL instance without a public address and without a site-to-site link. Which option fits?

- A. Connect over private IP inside the VPC
- B. Add the client range to authorized networks
- C. Connect through the Cloud SQL Auth Proxy
- D. Use the public IP with enforced SSL

### 14. A contract requires that the customer hold and be able to destroy the key protecting its database. Which control satisfies that?

- A. Enable Data Access audit logs
- B. Encrypt with a customer-managed key in Cloud KMS
- C. Rotate the customer-managed key on a schedule
- D. Rely on Google-managed encryption keys

### 15. A small team wants encryption at rest on a Bigtable instance with no key lifecycle to operate. Which choice fits?

- A. Rely on Google-managed encryption keys
- B. Rotate the customer-managed key on a schedule
- C. Add the projects to a VPC Service Controls perimeter
- D. Encrypt with a customer-managed key in Cloud KMS

### 16. A team must stop connection refusals this quarter while a pooling rollout is still being planned. Select two.

- A. Put a session pooler in front of the instance
- B. Fix the connection leak in the application
- C. Raise the max_connections database flag
- D. Increase the machine type of the instance
- E. Increase the machine tier to allow more connections

### 17. An instance refuses new sessions at the platform's per-tier limit, and every session in flight is genuinely needed. What should the team do?

- A. Increase the machine tier to allow more connections
- B. Put a session pooler in front of the instance
- C. Raise the max_connections database flag
- D. Fix the connection leak in the application

### 18. An auditor needs a record of which principal read a customer table last month. Which logging control provides it?

- A. Enable Data Access audit logs
- B. Review the fleet in Database Center
- C. Rely on Admin Activity audit logs
- D. Route the audit logs to a locked log bucket

### 19. A team must keep audit evidence for three years even if the project's default bucket is emptied. What should it configure?

- A. Build a log-based metric from the error entries
- B. Rely on Admin Activity audit logs
- C. Enable Data Access audit logs
- D. Route the audit logs to a locked log bucket

### 20. A team must replace a self-managed MySQL instance and a self-run Redis cache with managed equivalents that keep the same access patterns. Select two.

- A. Run the database on bare metal solution
- B. Run the database on Compute Engine yourself
- C. Use Cloud SQL for the relational workload
- D. Use Memorystore as the caching tier
- E. Use Bigtable for the high-throughput wide-column workload

### 21. A regulated workload must stay on an engine that only its vendor operates, under an existing support contract. Which deployment fits?

- A. Run the database on Compute Engine yourself
- B. Run the database on bare metal solution
- C. Use a partner-managed database offering
- D. Use Cloud SQL for the relational workload

### 22. A settlement system needs globally consistent transactions and horizontal write scaling without application sharding. Which database fits?

- A. Use Cloud SQL for the relational workload
- B. Use Spanner for the globally distributed relational workload
- C. Use Bigtable for the high-throughput wide-column workload
- D. Use Firestore for the document workload

### 23. A telemetry pipeline must absorb two hundred thousand writes per second keyed by device and time, with cost per write as the constraint. Which database fits?

- A. Use Spanner for the globally distributed relational workload
- B. Use Bigtable for the high-throughput wide-column workload
- C. Use Cloud SQL for the relational workload
- D. Use Memorystore as the caching tier

### 24. A consumer app needs per-document queries, offline sync on mobile, and managed global replication. Which database fits?

- A. Use Memorystore as the caching tier
- B. Use Cloud SQL for the relational workload
- C. Use Firestore for the document workload
- D. Use Bigtable for the high-throughput wide-column workload

### 25. A team must add semantic search to an existing Cloud SQL for PostgreSQL service without introducing another database. Which two steps are required? Select two.

- A. Create a vector index for the embeddings
- B. Enable the vector extension on PostgreSQL
- C. Use AlloyDB vector search with a ScaNN index
- D. Query the source through BigQuery federated queries
- E. Export the table into BigQuery

### 26. A retrieval service must search one hundred fifty million embeddings with metadata filters and hold p99 under one hundred milliseconds. Which choice fits?

- A. Add the composite index for the query
- B. Cache the hot read path in Memorystore
- C. Use AlloyDB vector search with a ScaNN index
- D. Enable the vector extension on PostgreSQL

### 27. A company runs a fixed Cloud SQL estate at constant load all year and wants a lower unit price for that predictable usage. Which action fits?

- A. Rely on sustained-use discounts
- B. Commit to the steady baseline capacity
- C. Scale down outside business hours
- D. Stop or delete the idle instance

### 28. A migration project's staging database has had no connections for six weeks and continues to be billed. What should the team do?

- A. Stop or delete the idle instance
- B. Reserve capacity for the peak season
- C. Commit to the steady baseline capacity
- D. Reduce the machine type to match observed use

### 29. An application depends on database features that no candidate target supports without rewrites, and the roadmap gives four weeks. What should the team decide?

- A. Write to both systems from the application
- B. Keep the current engine and version
- C. Choose the target engine with the cheapest conversion
- D. Use Database Migration Service with schema conversion

### 30. A bank must keep a database in its home country and must retain tamper-resistant access records for seven years. Select two.

- A. Rely on Google-managed encryption keys
- B. Cache the hot read path in Memorystore
- C. Route the audit logs to a locked log bucket
- D. Enforce the location with an organization policy
- E. Place the instance in the required region

### 31. A platform team must make it impossible for a newly created project to place a database outside the three approved regions. What should it apply?

- A. Route the audit logs to a locked log bucket
- B. Place the instance in the required region
- C. Enforce the location with an organization policy
- D. Encrypt with a customer-managed key in Cloud KMS

### 32. A regulated system must stay on-premises for four more years while new services on Cloud SQL read some of its tables. Which approach fits?

- A. Keep part of the estate on-premises with a hybrid link
- B. Decommission the source after a parallel period
- C. Export the table into BigQuery
- D. Query the source through BigQuery federated queries

---

## Domain 2 — Manage a Solution That Can Span Multiple Database Technologies (Operations, Access, Backup, and Performance)

### 33. A support engineer needs read-only visibility of instance metrics, but the current binding grants the project editor role. What should the team change?

- A. Create one database user per person
- B. Grant the basic editor role
- C. Grant a custom role limited to the needed permissions
- D. Grant the predefined database role

### 34. A marketing tool must write to one schema and read another, and the reviewer rejects an instance-wide grant. What should the team request?

- A. Grant the basic editor role
- B. Share one application database user
- C. Limit the user to the required schema
- D. Grant a custom role limited to the needed permissions

### 35. A team must remove stored database passwords from both its application and its analysts. Select two.

- A. Enable IAM database authentication
- B. Keep a database password in the connection string
- C. Share one application database user
- D. Have the application authenticate as a service account
- E. Grant the basic editor role

### 36. A query filters one column and returns nine rows from six million, and the plan shows a full scan. What should the team do?

- A. Refresh the table statistics
- B. Raise the per-operation memory flag
- C. Partition the large table
- D. Add the index the slow query needs

### 37. A statement is slow after a schema change, and the team must see which access path the planner chose before altering anything. What should it do?

- A. Refresh the table statistics
- B. Add the index the slow query needs
- C. Read the query plan for the statement
- D. Drop the unused index

### 38. A session has held an exclusive lock for forty minutes with no statement running, and every write is queued behind it. What should the team do?

- A. Inspect lock waits and blocking sessions
- B. Send reporting queries to the read replica
- C. Batch the writes into fewer round trips
- D. Terminate the session that holds the lock

### 39. Writes stall intermittently, and the team must identify the chain of transactions holding each other. What should it do?

- A. Inspect lock waits and blocking sessions
- B. Add the index the slow query needs
- C. Terminate the session that holds the lock
- D. Refresh the table statistics

### 40. A team must show whether a slow database is short of memory or waiting on storage during a benchmark. Which view answers that?

- A. Review the fleet in Database Center
- B. Use Query Insights to find the heavy statements
- C. Watch CPU, memory, disk, and IOPS together
- D. Read the slow query log

### 41. A review needs per-statement time broken down by wait category rather than a single total. Which tool provides it?

- A. Watch CPU, memory, disk, and IOPS together
- B. Build a log-based metric from the error entries
- C. Use Query Insights to find the heavy statements
- D. Read the slow query log

### 42. A legitimate month-end burst trips a project quota while the rest of the month is quiet. Which two responses fit? Select two.

- A. Let the disk grow automatically
- B. Retry the failed operation with exponential backoff
- C. Export the table to CSV in Cloud Storage
- D. Move the job outside the contention window
- E. Request a quota increase for the project

### 43. A team must be told when replica state changes to a role it did not expect. What should it configure?

- A. Create an alerting policy on the metric
- B. Alert on the database error rate
- C. Build a log-based metric from the error entries
- D. Watch CPU, memory, disk, and IOPS together

### 44. Pages fire on memory utilization while users see failed statements during a traffic spike. What should the team alert on instead?

- A. Create an alerting policy on the metric
- B. Alert on the database error rate
- C. Alert on replication lag
- D. Use Query Insights to find the heavy statements

### 45. A team has no scheduled backups and relies on an occasional manual dump. What should it enable first?

- A. Export the table to CSV in Cloud Storage
- B. Clone the instance for the test
- C. Take an on-demand backup before the change
- D. Enable automated backups with a retention window

### 46. A service must return to the state it held eight minutes ago after a faulty script, with no standby available. Which capability fits?

- A. Enable point-in-time recovery
- B. Export a logical dump to Cloud Storage
- C. Enable automated backups with a retention window
- D. Extend the backup retention window

### 47. A team must take a portable copy of a database that can be restored into another engine of the same family. Which export fits?

- A. Export a logical dump to Cloud Storage
- B. Import the dump into the target instance
- C. Query the source through BigQuery federated queries
- D. Export the table to CSV in Cloud Storage

### 48. An application owner cannot say how much data loss is acceptable, and the team must pick a recovery mechanism. What should it settle first?

- A. Enable point-in-time recovery
- B. Clone the instance for the test
- C. Enable automated backups with a retention window
- D. Design the restore path to the stated RTO and RPO

### 49. A bad deployment corrupted rows for twenty minutes before it was stopped. What restores the pre-deployment state?

- A. Run a controlled failover test
- B. Clone the instance for the test
- C. Export a logical dump to Cloud Storage
- D. Restore to the timestamp before the bad change

### 50. A Bigtable table accumulates versions, and the team also exports nightly snapshots that pile up. Which two retention controls does it need? Select two.

- A. Let the disk grow automatically
- B. Add a lifecycle rule to the export bucket
- C. Apply a row-level retention policy
- D. Set a time-to-live policy on the collection
- E. Set the garbage-collection policy on the column family

### 51. A reporting replica is at fifteen percent CPU while the primary is at ninety percent with reporting queries still running there. What should the team change?

- A. Send reporting queries to the read replica
- B. Add a read replica for the read traffic
- C. Cache the hot read path in Memorystore
- D. Increase the machine type of the instance

### 52. A table holds five years of events, and every retention job deletes a day of rows from the middle of it. What should change?

- A. Add the index the slow query needs
- B. Shard the data across several instances
- C. Increase the machine type of the instance
- D. Partition the large table

### 53. A team needs a continuously updated copy in a second region for reporting and promotion, on Cloud SQL. What should it add?

- A. Add a secondary cluster in the second region
- B. Choose a multi-region instance configuration
- C. Add a cross-region read replica
- D. Restore the backup into the second region

### 54. Write cost on an order table is dominated by index maintenance and per-row commits. Which two actions reduce it? Select two.

- A. Drop the unused index
- B. Batch the writes into fewer round trips
- C. Cache the hot read path in Memorystore
- D. Raise the per-operation memory flag
- E. Add the index the slow query needs

### 55. Monthly index rebuilds must run on a fixed date without anyone present. What should the team configure?

- A. Run a controlled failover test
- B. Take an on-demand backup before the change
- C. Run the task on a managed schedule
- D. Provision the instance once by hand

### 56. A team must know whether a minor version change breaks a stored procedure before production traffic sees it. What should they do?

- A. Take a backup before the upgrade
- B. Test the upgrade on a clone first
- C. Watch the error rate after the change
- D. Perform an in-place major version upgrade

### 57. A quarterly review asks whether the database met the availability it promised in its service description. Which practice answers that?

- A. Create an alerting policy on the metric
- B. Track the availability signal against the agreed objective
- C. Watch CPU, memory, disk, and IOPS together
- D. Review the fleet in Database Center

---

## Domain 3 — Migrate Data Solutions (Migration Strategy, Conversion, and Cutover)

### 58. A two-hundred-gigabyte MySQL database must move with minutes of downtime and a same-week rollback option. Select two.

- A. Dump, restore, then replay the changes
- B. Use Database Migration Service for the same engine
- C. Accept a scheduled extended outage
- D. Set up reverse replication to the source
- E. Write to both systems from the application

### 59. A small internal tool can be offline for a full weekend and its database is twelve gigabytes. Which strategy is simplest?

- A. Use Database Migration Service for the same engine
- B. Accept a scheduled extended outage
- C. Write to both systems from the application
- D. Follow a cutover runbook with a rollback step

### 60. A team must define who approves the switch, what evidence is required, and when to abort. What should it write?

- A. Write to both systems from the application
- B. Accept a scheduled extended outage
- C. Freeze writes during the cutover
- D. Follow a cutover runbook with a rollback step

### 61. A team must move Oracle 12c to Cloud SQL for PostgreSQL and convert its schema in a reviewable way. Which path fits?

- A. Stream changes with Datastream
- B. Use Database Migration Service for the same engine
- C. Use Database Migration Service with schema conversion
- D. Dump, restore, then replay the changes

### 62. A retailer needs continuous change capture from MySQL into BigQuery while keeping the source in production. Which tool fits?

- A. Use Database Migration Service with schema conversion
- B. Export the table into BigQuery
- C. Export a logical dump to Cloud Storage
- D. Stream changes with Datastream

### 63. A twenty-gigabyte database must be copied once into a test environment with no ongoing replication. Which approach fits?

- A. Write to both systems from the application
- B. Apply the captured change backlog before cutover
- C. Dump, restore, then replay the changes
- D. Use Database Migration Service with schema conversion

### 64. A conversion produces DDL the team must edit and stored procedures with no target equivalent. Which two actions are needed? Select two.

- A. Reset the sequences after the bulk load
- B. Build the schema in a conversion workspace
- C. Replay read traffic against the target
- D. Repoint the connection string at the target
- E. Rewrite the stored procedures and DML by hand

### 65. After a converted schema loads, new inserts collide with existing primary keys because the identity counters start at one. What should the team do?

- A. Reconcile row counts and checksums
- B. Rewrite the stored procedures and DML by hand
- C. Build the schema in a conversion workspace
- D. Reset the sequences after the bulk load

### 66. A team wants production read queries replayed on the target to compare answers with the source. Which activity fits?

- A. Replay read traffic against the target
- B. Follow a cutover runbook with a rollback step
- C. Reconcile row counts and checksums
- D. Rewrite the stored procedures and DML by hand

### 67. A service's batch jobs use engine-specific date arithmetic that the target rejects. What must happen?

- A. Build the schema in a conversion workspace
- B. Write to both systems from the application
- C. Rewrite the stored procedures and DML by hand
- D. Reset the sequences after the bulk load

### 68. A ten-hour initial load must not stop the source from taking writes. How should the target stay current during the load?

- A. Use the engine native logical replication
- B. Accept a scheduled extended outage
- C. Write to both systems from the application
- D. Export a logical dump to Cloud Storage

### 69. The bulk copy finished, but rows written during it are missing on the target. What has to happen before the switch?

- A. Freeze writes during the cutover
- B. Apply the captured change backlog before cutover
- C. Repoint the connection string at the target
- D. Reconcile row counts and checksums

### 70. A team must prove the target is complete before switching traffic. Which two actions are needed? Select two.

- A. Apply the captured change backlog before cutover
- B. Replay read traffic against the target
- C. Repoint the connection string at the target
- D. Reset the sequences after the bulk load
- E. Reconcile row counts and checksums

### 71. A team wants to confirm that the target answers the application's reporting queries identically. Which check fits?

- A. Write to both systems from the application
- B. Replay read traffic against the target
- C. Reconcile row counts and checksums
- D. Follow a cutover runbook with a rollback step

### 72. A scheduled job continues inserting rows during the final increment and the target falls behind. What must the team do?

- A. Set up reverse replication to the source
- B. Repoint the connection string at the target
- C. Accept a scheduled extended outage
- D. Freeze writes during the cutover

### 73. The target passed validation but application traffic still reaches the old instance through its hostname. What completes the cutover?

- A. Use the language connector with IAM credentials
- B. Repoint the connection string at the target
- C. Follow a cutover runbook with a rollback step
- D. Freeze writes during the cutover

### 74. Twenty minutes into the window the target's error rate exceeds the threshold, and the team must act. What should guide the decision?

- A. Follow a cutover runbook with a rollback step
- B. Freeze writes during the cutover
- C. Write to both systems from the application
- D. Repoint the connection string at the target

### 75. The old on-premises system must show the writes made on the new database after cutover. What makes that possible?

- A. Write to both systems from the application
- B. Set up reverse replication to the source
- C. Decommission the source after a parallel period
- D. Repoint the connection string at the target

### 76. A team must state how long the fallback stays available before the old system is removed. What should it define?

- A. Decommission the source after a parallel period
- B. Confirm no client still uses the old endpoint
- C. Set up reverse replication to the source
- D. Repoint the connection string at the target

### 77. A three-terabyte migration must finish inside a twenty-minute window. Which two preparations make that possible? Select two.

- A. Accept a scheduled extended outage
- B. Dump, restore, then replay the changes
- C. Measure the catch-up rate before choosing the window
- D. Use Database Migration Service for the same engine
- E. Write to both systems from the application

### 78. A source's change rate spikes every Friday afternoon, and the cutover must stay inside a short window. What should the team do?

- A. Accept a scheduled extended outage
- B. Measure the catch-up rate before choosing the window
- C. Move the job outside the contention window
- D. Write to both systems from the application

### 79. The parallel period has ended with no incidents, and the contract for the old hardware is expiring. What should the team do?

- A. Set up reverse replication to the source
- B. Decommission the source after a parallel period
- C. Repoint the connection string at the target
- D. Write to both systems from the application

### 80. A team must confirm that no batch job still connects to the source before it is deleted. What should they do?

- A. Decommission the source after a parallel period
- B. Reconcile row counts and checksums
- C. Repoint the connection string at the target
- D. Confirm no client still uses the old endpoint

---

## Domain 4 — Deploy Scalable and Highly Available Databases in Google Cloud (Deployment, High Availability, and Disaster Recovery)

### 81. A team must rebuild twelve instances after a disaster with identical flags, labels, and network settings. What makes that reliable?

- A. Stand up a parallel instance and switch over
- B. Provision the instance with a Terraform module
- C. Clone the instance for the test
- D. Provision the instance once by hand

### 82. A team must show that every database change passed review before it was applied. What should it adopt?

- A. Provision the instance once by hand
- B. Apply the change through the infrastructure pipeline
- C. Review the fleet in Database Center
- D. Test the upgrade on a clone first

### 83. A platform team must add the same read replica to twenty-five instances this week. What should it use?

- A. Provision the instance with a Terraform module
- B. Stand up a parallel instance and switch over
- C. Take a backup before the upgrade
- D. Provision the instance once by hand

### 84. A team must show that its zone failover and its regional promotion both work. Which two exercises prove them? Select two.

- A. Take a backup before the upgrade
- B. Rehearse the promotion in a test project
- C. Run a controlled failover test
- D. Set a deny maintenance period over the peak event
- E. Watch the error rate after the change

### 85. A team must prove that applications reconnect without human action when the active zone is removed. What should it run?

- A. Restore the backup into the second region
- B. Watch the error rate after the change
- C. Take a backup before the upgrade
- D. Run a controlled failover test

### 86. A drill shows the promoted replica cannot handle production write volume because it was sized for reporting. What should change?

- A. Reserve headroom above the measured peak
- B. Pre-size the promoted replica for the full load
- C. Restore the backup into the second region
- D. Add a read replica for the read traffic

### 87. A Spanner service must keep writes available through the loss of any one region. Which configuration fits?

- A. Restore the backup into the second region
- B. Enable regional high availability with a standby zone
- C. Add a cross-region read replica
- D. Choose a multi-region instance configuration

### 88. An AlloyDB deployment must serve reads in a second region today and be promotable later. Which choice fits?

- A. Restore the backup into the second region
- B. Add nodes to the read pool
- C. Add a secondary cluster in the second region
- D. Run a single zonal instance

### 89. A Bigtable client must survive the loss of one cluster without a configuration change. Which app profile setting fits?

- A. Route the app profile across both clusters
- B. Add a secondary cluster in the second region
- C. Add a cross-region read replica
- D. Pin the app profile to one cluster

### 90. An AlloyDB read pool is at ninety percent CPU while the primary is at thirty-five percent. What should the team do?

- A. Cache the hot read path in Memorystore
- B. Add nodes to the read pool
- C. Send reporting queries to the read replica
- D. Increase the machine type of the instance

### 91. A Cloud SQL primary is at ninety percent CPU because of read traffic, and the application can be pointed at a second endpoint. What should the team add?

- A. Increase the machine type of the instance
- B. Shard the data across several instances
- C. Add a read replica for the read traffic
- D. Add nodes to the read pool

### 92. A team wants database provisioning that is reviewed, repeatable, and validated before use. Which two practices deliver that? Select two.

- A. Provision the instance once by hand
- B. Test the upgrade on a clone first
- C. Apply the change through the infrastructure pipeline
- D. Provision the instance with a Terraform module
- E. Take a backup before the upgrade

### 93. A team must create sixty tenant instances with identical settings and per-tenant labels. What should it use?

- A. Provision the instance once by hand
- B. Review the fleet in Database Center
- C. Clone the instance for the test
- D. Provision the instance with a Terraform module

### 94. A team must know immediately when a failover moves the primary to another zone. What should it configure?

- A. Watch CPU, memory, disk, and IOPS together
- B. Use Query Insights to find the heavy statements
- C. Create an alerting policy on the metric
- D. Review the fleet in Database Center

### 95. A team wants one place to review version posture and health across a large database fleet. Which view fits?

- A. Read the slow query log
- B. Use Query Insights to find the heavy statements
- C. Review the fleet in Database Center
- D. Watch CPU, memory, disk, and IOPS together

### 96. A region is unavailable, the remote copy is seconds behind, and the objective allows one hour to resume writes. What should the team do?

- A. Promote the cross-region replica during the outage
- B. Restore to the timestamp before the bad change
- C. Restore the backup into the second region
- D. Run a controlled failover test

### 97. After a regional failover the original primary returns and begins accepting writes. What must the team do?

- A. Freeze writes during the cutover
- B. Follow a cutover runbook with a rollback step
- C. Fence the old primary before promotion
- D. Set up reverse replication to the source

### 98. Clients keep reconnecting to the failed instance because the address is cached in the pool. What should the team adopt?

- A. Put a session pooler in front of the instance
- B. Repoint the connection string at the target
- C. Add the client range to authorized networks
- D. Use the language connector with IAM credentials

### 99. A team must set the standby's spare capacity so a peak-hour failover keeps the latency objective. What is the basis?

- A. Reserve headroom above the measured peak
- B. Reduce the machine type to match observed use
- C. Scale down outside business hours
- D. Add a read replica for the read traffic

### 100. A recovery plan assumes the standby can be resized during a failover, but resizing takes thirty-five minutes. What should change?

- A. Pre-size the promoted replica for the full load
- B. Scale down outside business hours
- C. Reserve headroom above the measured peak
- D. Add a read replica for the read traffic

---

## Answer key and explanations

### Question 1 — B

Answer: Load-test the workload to derive the size. Driving comparable traffic through staging produces the resource curve the sizing decision needs, which no historical metric exists to provide. Generate representative traffic and read the resource curve before choosing a shape. Local study-map skill 1.1 (Workload Sizing From Current Metrics), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 1 (design innovative, scalable, and highly available cloud database solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A one- or three-year commitment that discounts the capacity always in use. Why the correct answer wins: Driving comparable traffic through staging produces the resource curve the sizing decision needs, which no historical metric exists to provide.
- **B:** Correct. Generate representative traffic and read the resource curve before choosing a shape. In this case: Driving comparable traffic through staging produces the resource curve the sizing decision needs, which no historical metric exists to provide.
- **C:** Incorrect for this question. Keep spare capacity so a failover or a traffic spike does not saturate the instance. Why the correct answer wins: Driving comparable traffic through staging produces the resource curve the sizing decision needs, which no historical metric exists to provide.
- **D:** Incorrect for this question. Choose a shape from measured CPU, memory, and IOPS rather than from a guess. Why the correct answer wins: Driving comparable traffic through staging produces the resource curve the sizing decision needs, which no historical metric exists to provide.

### Question 2 — C

Answer: Size the instance from the observed peak metrics. Measured CPU, memory, and throughput peaks make the case auditable, whereas a synthetic assumption or a discount does not. Choose a shape from measured CPU, memory, and IOPS rather than from a guess. Local study-map skill 1.1 (Workload Sizing From Current Metrics), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 1 (design innovative, scalable, and highly available cloud database solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Generate representative traffic and read the resource curve before choosing a shape. Why the correct answer wins: Measured CPU, memory, and throughput peaks make the case auditable, whereas a synthetic assumption or a discount does not.
- **B:** Incorrect for this question. A one- or three-year commitment that discounts the capacity always in use. Why the correct answer wins: Measured CPU, memory, and throughput peaks make the case auditable, whereas a synthetic assumption or a discount does not.
- **C:** Correct. Choose a shape from measured CPU, memory, and IOPS rather than from a guess. In this case: Measured CPU, memory, and throughput peaks make the case auditable, whereas a synthetic assumption or a discount does not.
- **D:** Incorrect for this question. Shrink an instance whose peak fits a smaller shape. Why the correct answer wins: Measured CPU, memory, and throughput peaks make the case auditable, whereas a synthetic assumption or a discount does not.

### Question 3 — B, D

Answers: Add nodes to the Bigtable cluster; Move the data to SSD storage. More nodes raise the serving capacity, and SSD lowers the read latency, while storage class alone, garbage collection, or key design does not add throughput. Increase the cluster size so more tablet servers absorb the request rate. Trade a higher price per gigabyte for lower latency on random reads. Local study-map skill 1.2 (Compute and Storage Sizing Tradeoffs), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 1 (design innovative, scalable, and highly available cloud database solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Trade latency for a lower price on large, throughput-oriented scans. Why the correct answer wins: More nodes raise the serving capacity, and SSD lowers the read latency, while storage class alone, garbage collection, or key design does not add throughput.
- **B:** Correct. Increase the cluster size so more tablet servers absorb the request rate. In this case: More nodes raise the serving capacity, and SSD lowers the read latency, while storage class alone, garbage collection, or key design does not add throughput.
- **C:** Incorrect for this question. A rule that drops versions by age or count, which also bounds recovery. Why the correct answer wins: More nodes raise the serving capacity, and SSD lowers the read latency, while storage class alone, garbage collection, or key design does not add throughput.
- **D:** Correct. Trade a higher price per gigabyte for lower latency on random reads. In this case: More nodes raise the serving capacity, and SSD lowers the read latency, while storage class alone, garbage collection, or key design does not add throughput.
- **E:** Incorrect for this question. Fix the access pattern that concentrates load on a narrow key range. Why the correct answer wins: More nodes raise the serving capacity, and SSD lowers the read latency, while storage class alone, garbage collection, or key design does not add throughput.

### Question 4 — D

Answer: Increase the disk size to raise throughput. More disk raises the throughput ceiling, which additional compute or a replica does not. Buy more storage so the attached disk also yields more IOPS and throughput. Local study-map skill 1.2 (Compute and Storage Sizing Tradeoffs), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 1 (design innovative, scalable, and highly available cloud database solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Avoid a full-disk outage at the cost of unplanned storage growth. Why the correct answer wins: More disk raises the throughput ceiling, which additional compute or a replica does not.
- **B:** Incorrect for this question. Move the instance to a larger shape so more vCPU and memory serve the same data. Why the correct answer wins: More disk raises the throughput ceiling, which additional compute or a replica does not.
- **C:** Incorrect for this question. Send reads to a copy so the primary keeps its capacity for writes. Why the correct answer wins: More disk raises the throughput ceiling, which additional compute or a replica does not.
- **D:** Correct. Buy more storage so the attached disk also yields more IOPS and throughput. In this case: More disk raises the throughput ceiling, which additional compute or a replica does not.

### Question 5 — D

Answer: Increase the machine type of the instance. A larger shape adds the memory the working set needs, which disk, a replica, or a pooler cannot supply. Move the instance to a larger shape so more vCPU and memory serve the same data. Local study-map skill 1.3 (Machine Type and Storage Type Selection), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 1 (design innovative, scalable, and highly available cloud database solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A pooler that multiplexes many application connections onto few database sessions. Why the correct answer wins: A larger shape adds the memory the working set needs, which disk, a replica, or a pooler cannot supply.
- **B:** Incorrect for this question. Buy more storage so the attached disk also yields more IOPS and throughput. Why the correct answer wins: A larger shape adds the memory the working set needs, which disk, a replica, or a pooler cannot supply.
- **C:** Incorrect for this question. Send reads to a copy so the primary keeps its capacity for writes. Why the correct answer wins: A larger shape adds the memory the working set needs, which disk, a replica, or a pooler cannot supply.
- **D:** Correct. Move the instance to a larger shape so more vCPU and memory serve the same data. In this case: A larger shape adds the memory the working set needs, which disk, a replica, or a pooler cannot supply.

### Question 6 — B

Answer: Add processing units to the Spanner instance. Adding processing units raises provisioned compute for that steady load, while node counts, machine types, and autoscaling apply to other services or other needs. Raise provisioned compute in 1000-unit node steps or 100-unit increments. Local study-map skill 1.3 (Machine Type and Storage Type Selection), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 1 (design innovative, scalable, and highly available cloud database solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Let compute follow a target utilization instead of a fixed size. Why the correct answer wins: Adding processing units raises provisioned compute for that steady load, while node counts, machine types, and autoscaling apply to other services or other needs.
- **B:** Correct. Raise provisioned compute in 1000-unit node steps or 100-unit increments. In this case: Adding processing units raises provisioned compute for that steady load, while node counts, machine types, and autoscaling apply to other services or other needs.
- **C:** Incorrect for this question. Increase the cluster size so more tablet servers absorb the request rate. Why the correct answer wins: Adding processing units raises provisioned compute for that steady load, while node counts, machine types, and autoscaling apply to other services or other needs.
- **D:** Incorrect for this question. Move the instance to a larger shape so more vCPU and memory serve the same data. Why the correct answer wins: Adding processing units raises provisioned compute for that steady load, while node counts, machine types, and autoscaling apply to other services or other needs.

### Question 7 — D

Answer: Enable regional high availability with a standby zone. A regional instance keeps a standby in another zone and fails over automatically, which avoids the cost of regional replication. A primary and standby in two zones of one region with automatic failover. Local study-map skill 1.4 (Zonal, Regional, and Multi-Regional Tradeoffs), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 1 (design innovative, scalable, and highly available cloud database solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Rebuild the database in the surviving region from the latest backup. Why the correct answer wins: A regional instance keeps a standby in another zone and fails over automatically, which avoids the cost of regional replication.
- **B:** Incorrect for this question. A topology that places replicas in separate regions for regional-failure tolerance. Why the correct answer wins: A regional instance keeps a standby in another zone and fails over automatically, which avoids the cost of regional replication.
- **C:** Incorrect for this question. A copy in a second region that serves reads and can be promoted. Why the correct answer wins: A regional instance keeps a standby in another zone and fails over automatically, which avoids the cost of regional replication.
- **D:** Correct. A primary and standby in two zones of one region with automatic failover. In this case: A regional instance keeps a standby in another zone and fails over automatically, which avoids the cost of regional replication.

### Question 8 — D

Answer: Choose a multi-region instance configuration. A multi-region configuration keeps quorum across regions so writes continue, which a regional or zonal topology cannot. A topology that places replicas in separate regions for regional-failure tolerance. Local study-map skill 1.4 (Zonal, Regional, and Multi-Regional Tradeoffs), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 1 (design innovative, scalable, and highly available cloud database solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. One instance in one zone with no standby, so a zone failure stops writes. Why the correct answer wins: A multi-region configuration keeps quorum across regions so writes continue, which a regional or zonal topology cannot.
- **B:** Incorrect for this question. A copy in a second region that serves reads and can be promoted. Why the correct answer wins: A multi-region configuration keeps quorum across regions so writes continue, which a regional or zonal topology cannot.
- **C:** Incorrect for this question. A primary and standby in two zones of one region with automatic failover. Why the correct answer wins: A multi-region configuration keeps quorum across regions so writes continue, which a regional or zonal topology cannot.
- **D:** Correct. A topology that places replicas in separate regions for regional-failure tolerance. In this case: A multi-region configuration keeps quorum across regions so writes continue, which a regional or zonal topology cannot.

### Question 9 — B

Answer: Restore the backup into the second region. Restoring the latest backup into the second region is the available path when no copy exists. Rebuild the database in the surviving region from the latest backup. Local study-map skill 1.4 (Zonal, Regional, and Multi-Regional Tradeoffs), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 1 (design innovative, scalable, and highly available cloud database solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Block maintenance during a period when an interruption is unacceptable. Why the correct answer wins: Restoring the latest backup into the second region is the available path when no copy exists.
- **B:** Correct. Rebuild the database in the surviving region from the latest backup. In this case: Restoring the latest backup into the second region is the available path when no copy exists.
- **C:** Incorrect for this question. Turn the replica into an independent primary so the application can resume writes. Why the correct answer wins: Restoring the latest backup into the second region is the available path when no copy exists.
- **D:** Incorrect for this question. A primary and standby in two zones of one region with automatic failover. Why the correct answer wins: Restoring the latest backup into the second region is the available path when no copy exists.

### Question 10 — A

Answer: Schedule the maintenance window in the low-traffic period. The maintenance window names the hour when patching runs, which a deny period, an upgrade, or a test does not. Choose the weekly window when patching may interrupt the instance. Local study-map skill 1.5 (Maintenance Windows and Notification), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 1 (design innovative, scalable, and highly available cloud database solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Correct. Choose the weekly window when patching may interrupt the instance. In this case: The maintenance window names the hour when patching runs, which a deny period, an upgrade, or a test does not.
- **B:** Incorrect for this question. Block maintenance during a period when an interruption is unacceptable. Why the correct answer wins: The maintenance window names the hour when patching runs, which a deny period, an upgrade, or a test does not.
- **C:** Incorrect for this question. Trigger a switchover in a test window and observe how long writes are unavailable. Why the correct answer wins: The maintenance window names the hour when patching runs, which a deny period, an upgrade, or a test does not.
- **D:** Incorrect for this question. Change the engine version on the running instance during the window. Why the correct answer wins: The maintenance window names the hour when patching runs, which a deny period, an upgrade, or a test does not.

### Question 11 — A

Answer: Set a deny maintenance period over the peak event. A deny period covers the launch week and then expires, whereas a normal window would still permit an interruption. Block maintenance during a period when an interruption is unacceptable. Local study-map skill 1.5 (Maintenance Windows and Notification), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 1 (design innovative, scalable, and highly available cloud database solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Correct. Block maintenance during a period when an interruption is unacceptable. In this case: A deny period covers the launch week and then expires, whereas a normal window would still permit an interruption.
- **B:** Incorrect for this question. A recovery point that makes the upgrade reversible in practice. Why the correct answer wins: A deny period covers the launch week and then expires, whereas a normal window would still permit an interruption.
- **C:** Incorrect for this question. Choose the weekly window when patching may interrupt the instance. Why the correct answer wins: A deny period covers the launch week and then expires, whereas a normal window would still permit an interruption.
- **D:** Incorrect for this question. Apply the configuration change with a brief restart. Why the correct answer wins: A deny period covers the launch week and then expires, whereas a normal window would still permit an interruption.

### Question 12 — A, B

Answers: Publish the instance behind Private Service Connect; Enable IAM database authentication. A published private endpoint crosses the network boundary without peering, and IAM authentication removes the stored database credential. A private endpoint in the consumer VPC that reaches the service without peering. Map an IAM principal to a database user so no password is stored. Local study-map skill 1.6 (Network Connectivity and Private Access), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 1 (design innovative, scalable, and highly available cloud database solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Correct. A private endpoint in the consumer VPC that reaches the service without peering. In this case: A published private endpoint crosses the network boundary without peering, and IAM authentication removes the stored database credential.
- **B:** Correct. Map an IAM principal to a database user so no password is stored. In this case: A published private endpoint crosses the network boundary without peering, and IAM authentication removes the stored database credential.
- **C:** Incorrect for this question. A public address that requires encrypted connections from any client. Why the correct answer wins: A published private endpoint crosses the network boundary without peering, and IAM authentication removes the stored database credential.
- **D:** Incorrect for this question. A public-IP allowlist that admits the caller range. Why the correct answer wins: A published private endpoint crosses the network boundary without peering, and IAM authentication removes the stored database credential.
- **E:** Incorrect for this question. A private address reachable only from the VPC and connected networks. Why the correct answer wins: A published private endpoint crosses the network boundary without peering, and IAM authentication removes the stored database credential.

### Question 13 — C

Answer: Connect through the Cloud SQL Auth Proxy. The proxy authorizes the connection with IAM over TLS from anywhere, so no public address or network link is needed. A local proxy that adds IAM authorization and TLS without opening a network path. Local study-map skill 1.6 (Network Connectivity and Private Access), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 1 (design innovative, scalable, and highly available cloud database solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A private address reachable only from the VPC and connected networks. Why the correct answer wins: The proxy authorizes the connection with IAM over TLS from anywhere, so no public address or network link is needed.
- **B:** Incorrect for this question. A public-IP allowlist that admits the caller range. Why the correct answer wins: The proxy authorizes the connection with IAM over TLS from anywhere, so no public address or network link is needed.
- **C:** Correct. A local proxy that adds IAM authorization and TLS without opening a network path. In this case: The proxy authorizes the connection with IAM over TLS from anywhere, so no public address or network link is needed.
- **D:** Incorrect for this question. A public address that requires encrypted connections from any client. Why the correct answer wins: The proxy authorizes the connection with IAM over TLS from anywhere, so no public address or network link is needed.

### Question 14 — B

Answer: Encrypt with a customer-managed key in Cloud KMS. A customer-managed key puts custody and destruction in the customer's hands, which a Google-managed key cannot. A key the customer owns and can rotate or revoke. Local study-map skill 1.7 (Key Management and Encryption), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 1 (design innovative, scalable, and highly available cloud database solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Record reads and writes, which are not captured by default. Why the correct answer wins: A customer-managed key puts custody and destruction in the customer's hands, which a Google-managed key cannot.
- **B:** Correct. A key the customer owns and can rotate or revoke. In this case: A customer-managed key puts custody and destruction in the customer's hands, which a Google-managed key cannot.
- **C:** Incorrect for this question. Produce new key versions so an old version stops encrypting new data. Why the correct answer wins: A customer-managed key puts custody and destruction in the customer's hands, which a Google-managed key cannot.
- **D:** Incorrect for this question. Default encryption at rest with keys the customer neither sees nor manages. Why the correct answer wins: A customer-managed key puts custody and destruction in the customer's hands, which a Google-managed key cannot.

### Question 15 — A

Answer: Rely on Google-managed encryption keys. Default Google-managed encryption protects the data without the team running a key process. Default encryption at rest with keys the customer neither sees nor manages. Local study-map skill 1.7 (Key Management and Encryption), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 1 (design innovative, scalable, and highly available cloud database solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Correct. Default encryption at rest with keys the customer neither sees nor manages. In this case: Default Google-managed encryption protects the data without the team running a key process.
- **B:** Incorrect for this question. Produce new key versions so an old version stops encrypting new data. Why the correct answer wins: Default Google-managed encryption protects the data without the team running a key process.
- **C:** Incorrect for this question. A boundary that blocks data exfiltration even from an authorized identity. Why the correct answer wins: Default Google-managed encryption protects the data without the team running a key process.
- **D:** Incorrect for this question. A key the customer owns and can rotate or revoke. Why the correct answer wins: Default Google-managed encryption protects the data without the team running a key process.

### Question 16 — A, C

Answers: Put a session pooler in front of the instance; Raise the max_connections database flag. The pooler reduces the number of database sessions over time, and the raised ceiling prevents refusals during the transition. A pooler that multiplexes many application connections onto few database sessions. Increase the database-level connection ceiling on the instance. Local study-map skill 1.8 (Session Pooling and Connection Management), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 1 (design innovative, scalable, and highly available cloud database solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Correct. A pooler that multiplexes many application connections onto few database sessions. In this case: The pooler reduces the number of database sessions over time, and the raised ceiling prevents refusals during the transition.
- **B:** Incorrect for this question. Close sessions that the application opens and never returns to the pool. Why the correct answer wins: The pooler reduces the number of database sessions over time, and the raised ceiling prevents refusals during the transition.
- **C:** Correct. Increase the database-level connection ceiling on the instance. In this case: The pooler reduces the number of database sessions over time, and the raised ceiling prevents refusals during the transition.
- **D:** Incorrect for this question. Move the instance to a larger shape so more vCPU and memory serve the same data. Why the correct answer wins: The pooler reduces the number of database sessions over time, and the raised ceiling prevents refusals during the transition.
- **E:** Incorrect for this question. Buy a larger shape because the connection limit scales with memory. Why the correct answer wins: The pooler reduces the number of database sessions over time, and the raised ceiling prevents refusals during the transition.

### Question 17 — A

Answer: Increase the machine tier to allow more connections. The connection ceiling scales with the machine tier, so moving to a larger tier is the available route when the demand is real. Buy a larger shape because the connection limit scales with memory. Local study-map skill 1.8 (Session Pooling and Connection Management), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 1 (design innovative, scalable, and highly available cloud database solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Correct. Buy a larger shape because the connection limit scales with memory. In this case: The connection ceiling scales with the machine tier, so moving to a larger tier is the available route when the demand is real.
- **B:** Incorrect for this question. A pooler that multiplexes many application connections onto few database sessions. Why the correct answer wins: The connection ceiling scales with the machine tier, so moving to a larger tier is the available route when the demand is real.
- **C:** Incorrect for this question. Increase the database-level connection ceiling on the instance. Why the correct answer wins: The connection ceiling scales with the machine tier, so moving to a larger tier is the available route when the demand is real.
- **D:** Incorrect for this question. Close sessions that the application opens and never returns to the pool. Why the correct answer wins: The connection ceiling scales with the machine tier, so moving to a larger tier is the available route when the demand is real.

### Question 18 — A

Answer: Enable Data Access audit logs. Row-level reads appear only once Data Access audit logs are enabled for the service. Record reads and writes, which are not captured by default. Local study-map skill 1.9 (Auditing Policies for Managed Services), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 1 (design innovative, scalable, and highly available cloud database solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Correct. Record reads and writes, which are not captured by default. In this case: Row-level reads appear only once Data Access audit logs are enabled for the service.
- **B:** Incorrect for this question. A single view of health, security, and version posture across database instances. Why the correct answer wins: Row-level reads appear only once Data Access audit logs are enabled for the service.
- **C:** Incorrect for this question. Record configuration changes only, leaving row-level reads unaudited. Why the correct answer wins: Row-level reads appear only once Data Access audit logs are enabled for the service.
- **D:** Incorrect for this question. Export entries to storage whose retention cannot be shortened. Why the correct answer wins: Row-level reads appear only once Data Access audit logs are enabled for the service.

### Question 19 — D

Answer: Route the audit logs to a locked log bucket. Routing the entries to retained storage preserves the evidence beyond the default bucket's life. Export entries to storage whose retention cannot be shortened. Local study-map skill 1.9 (Auditing Policies for Managed Services), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 1 (design innovative, scalable, and highly available cloud database solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Turn a recurring log pattern into a metric that can be charted and alerted on. Why the correct answer wins: Routing the entries to retained storage preserves the evidence beyond the default bucket's life.
- **B:** Incorrect for this question. Record configuration changes only, leaving row-level reads unaudited. Why the correct answer wins: Routing the entries to retained storage preserves the evidence beyond the default bucket's life.
- **C:** Incorrect for this question. Record reads and writes, which are not captured by default. Why the correct answer wins: Routing the entries to retained storage preserves the evidence beyond the default bucket's life.
- **D:** Correct. Export entries to storage whose retention cannot be shortened. In this case: Routing the entries to retained storage preserves the evidence beyond the default bucket's life.

### Question 20 — C, D

Answers: Use Cloud SQL for the relational workload; Use Memorystore as the caching tier. A managed relational instance covers the system of record, and a managed in-memory store covers the cache, both without self-operated hosts. A managed MySQL, PostgreSQL, or SQL Server instance with Google-operated backups, patching, and failover. A managed Redis-compatible in-memory store placed in front of the system of record. Local study-map skill 1.10 (Managed, Self-Managed, and Partner Offerings), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 1 (design innovative, scalable, and highly available cloud database solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Dedicated hardware for engines that cannot be virtualized or licensed for a managed service. Why the correct answer wins: A managed relational instance covers the system of record, and a managed in-memory store covers the cache, both without self-operated hosts.
- **B:** Incorrect for this question. A self-managed engine on virtual machines where the team owns patching, backups, and failover. Why the correct answer wins: A managed relational instance covers the system of record, and a managed in-memory store covers the cache, both without self-operated hosts.
- **C:** Correct. A managed MySQL, PostgreSQL, or SQL Server instance with Google-operated backups, patching, and failover. In this case: A managed relational instance covers the system of record, and a managed in-memory store covers the cache, both without self-operated hosts.
- **D:** Correct. A managed Redis-compatible in-memory store placed in front of the system of record. In this case: A managed relational instance covers the system of record, and a managed in-memory store covers the cache, both without self-operated hosts.
- **E:** Incorrect for this question. A wide-column NoSQL service built for very high write and read rates over a sparse, row-key-ordered model. Why the correct answer wins: A managed relational instance covers the system of record, and a managed in-memory store covers the cache, both without self-operated hosts.

### Question 21 — C

Answer: Use a partner-managed database offering. A partner-managed offering keeps the vendor operating the engine on Google Cloud infrastructure. A third-party database operated by its vendor on Google Cloud infrastructure. Local study-map skill 1.10 (Managed, Self-Managed, and Partner Offerings), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 1 (design innovative, scalable, and highly available cloud database solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A self-managed engine on virtual machines where the team owns patching, backups, and failover. Why the correct answer wins: A partner-managed offering keeps the vendor operating the engine on Google Cloud infrastructure.
- **B:** Incorrect for this question. Dedicated hardware for engines that cannot be virtualized or licensed for a managed service. Why the correct answer wins: A partner-managed offering keeps the vendor operating the engine on Google Cloud infrastructure.
- **C:** Correct. A third-party database operated by its vendor on Google Cloud infrastructure. In this case: A partner-managed offering keeps the vendor operating the engine on Google Cloud infrastructure.
- **D:** Incorrect for this question. A managed MySQL, PostgreSQL, or SQL Server instance with Google-operated backups, patching, and failover. Why the correct answer wins: A partner-managed offering keeps the vendor operating the engine on Google Cloud infrastructure.

### Question 22 — B

Answer: Use Spanner for the globally distributed relational workload. Spanner supplies external consistency across regions with horizontal scale, which the other options do not. A horizontally scalable relational database with strong consistency across regions and no manual sharding. Local study-map skill 1.11 (SQL and NoSQL Data Model Fit), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 1 (design innovative, scalable, and highly available cloud database solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A managed MySQL, PostgreSQL, or SQL Server instance with Google-operated backups, patching, and failover. Why the correct answer wins: Spanner supplies external consistency across regions with horizontal scale, which the other options do not.
- **B:** Correct. A horizontally scalable relational database with strong consistency across regions and no manual sharding. In this case: Spanner supplies external consistency across regions with horizontal scale, which the other options do not.
- **C:** Incorrect for this question. A wide-column NoSQL service built for very high write and read rates over a sparse, row-key-ordered model. Why the correct answer wins: Spanner supplies external consistency across regions with horizontal scale, which the other options do not.
- **D:** Incorrect for this question. A document database with automatic multi-region replication, offline client support, and index-driven queries. Why the correct answer wins: Spanner supplies external consistency across regions with horizontal scale, which the other options do not.

### Question 23 — B

Answer: Use Bigtable for the high-throughput wide-column workload. A wide-column store handles that write shape at the lowest cost, while the relational and transactional options add overhead the workload does not use. A wide-column NoSQL service built for very high write and read rates over a sparse, row-key-ordered model. Local study-map skill 1.11 (SQL and NoSQL Data Model Fit), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 1 (design innovative, scalable, and highly available cloud database solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A horizontally scalable relational database with strong consistency across regions and no manual sharding. Why the correct answer wins: A wide-column store handles that write shape at the lowest cost, while the relational and transactional options add overhead the workload does not use.
- **B:** Correct. A wide-column NoSQL service built for very high write and read rates over a sparse, row-key-ordered model. In this case: A wide-column store handles that write shape at the lowest cost, while the relational and transactional options add overhead the workload does not use.
- **C:** Incorrect for this question. A managed MySQL, PostgreSQL, or SQL Server instance with Google-operated backups, patching, and failover. Why the correct answer wins: A wide-column store handles that write shape at the lowest cost, while the relational and transactional options add overhead the workload does not use.
- **D:** Incorrect for this question. A managed Redis-compatible in-memory store placed in front of the system of record. Why the correct answer wins: A wide-column store handles that write shape at the lowest cost, while the relational and transactional options add overhead the workload does not use.

### Question 24 — C

Answer: Use Firestore for the document workload. The document model with client libraries and managed replication meets all three requirements together. A document database with automatic multi-region replication, offline client support, and index-driven queries. Local study-map skill 1.11 (SQL and NoSQL Data Model Fit), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 1 (design innovative, scalable, and highly available cloud database solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A managed Redis-compatible in-memory store placed in front of the system of record. Why the correct answer wins: The document model with client libraries and managed replication meets all three requirements together.
- **B:** Incorrect for this question. A managed MySQL, PostgreSQL, or SQL Server instance with Google-operated backups, patching, and failover. Why the correct answer wins: The document model with client libraries and managed replication meets all three requirements together.
- **C:** Correct. A document database with automatic multi-region replication, offline client support, and index-driven queries. In this case: The document model with client libraries and managed replication meets all three requirements together.
- **D:** Incorrect for this question. A wide-column NoSQL service built for very high write and read rates over a sparse, row-key-ordered model. Why the correct answer wins: The document model with client libraries and managed replication meets all three requirements together.

### Question 25 — A, B

Answers: Enable the vector extension on PostgreSQL; Create a vector index for the embeddings. Enabling the extension puts the embeddings next to the existing rows, and the vector index makes the similarity search efficient at that size. Store embeddings beside relational rows and search them in the same engine. An approximate-nearest-neighbour index over embedding columns. Local study-map skill 1.12 (Vector and Generative AI Requirements), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 1 (design innovative, scalable, and highly available cloud database solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Correct. An approximate-nearest-neighbour index over embedding columns. In this case: Enabling the extension puts the embeddings next to the existing rows, and the vector index makes the similarity search efficient at that size.
- **B:** Correct. Store embeddings beside relational rows and search them in the same engine. In this case: Enabling the extension puts the embeddings next to the existing rows, and the vector index makes the similarity search efficient at that size.
- **C:** Incorrect for this question. A vector index tuned for large embedding sets on AlloyDB. Why the correct answer wins: Enabling the extension puts the embeddings next to the existing rows, and the vector index makes the similarity search efficient at that size.
- **D:** Incorrect for this question. Read the operational table from BigQuery without copying it first. Why the correct answer wins: Enabling the extension puts the embeddings next to the existing rows, and the vector index makes the similarity search efficient at that size.
- **E:** Incorrect for this question. Copy the analytical slice into the warehouse on a schedule. Why the correct answer wins: Enabling the extension puts the embeddings next to the existing rows, and the vector index makes the similarity search efficient at that size.

### Question 26 — C

Answer: Use AlloyDB vector search with a ScaNN index. A purpose-built vector index on AlloyDB meets that scale and latency with filters in place. A vector index tuned for large embedding sets on AlloyDB. Local study-map skill 1.12 (Vector and Generative AI Requirements), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 1 (design innovative, scalable, and highly available cloud database solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. An index ordered so the filter and sort both resolve without a scan. Why the correct answer wins: A purpose-built vector index on AlloyDB meets that scale and latency with filters in place.
- **B:** Incorrect for this question. Absorb repeated reads in memory so the database sees fewer of them. Why the correct answer wins: A purpose-built vector index on AlloyDB meets that scale and latency with filters in place.
- **C:** Correct. A vector index tuned for large embedding sets on AlloyDB. In this case: A purpose-built vector index on AlloyDB meets that scale and latency with filters in place.
- **D:** Incorrect for this question. Store embeddings beside relational rows and search them in the same engine. Why the correct answer wins: A purpose-built vector index on AlloyDB meets that scale and latency with filters in place.

### Question 27 — B

Answer: Commit to the steady baseline capacity. A commitment discounts capacity that runs continuously, which is exactly this estate. A one- or three-year commitment that discounts the capacity always in use. Local study-map skill 1.13 (Comparative Cost Analysis Across Databases), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 1 (design innovative, scalable, and highly available cloud database solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. The automatic discount that applies to long-running Compute Engine usage. Why the correct answer wins: A commitment discounts capacity that runs continuously, which is exactly this estate.
- **B:** Correct. A one- or three-year commitment that discounts the capacity always in use. In this case: A commitment discounts capacity that runs continuously, which is exactly this estate.
- **C:** Incorrect for this question. Match capacity to the daily traffic shape. Why the correct answer wins: A commitment discounts capacity that runs continuously, which is exactly this estate.
- **D:** Incorrect for this question. Remove capacity that serves no traffic. Why the correct answer wins: A commitment discounts capacity that runs continuously, which is exactly this estate.

### Question 28 — A

Answer: Stop or delete the idle instance. An instance with no traffic should be stopped or removed rather than committed or resized. Remove capacity that serves no traffic. Local study-map skill 1.13 (Comparative Cost Analysis Across Databases), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 1 (design innovative, scalable, and highly available cloud database solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Correct. Remove capacity that serves no traffic. In this case: An instance with no traffic should be stopped or removed rather than committed or resized.
- **B:** Incorrect for this question. Hold capacity ahead of a known surge rather than waiting for autoscaling. Why the correct answer wins: An instance with no traffic should be stopped or removed rather than committed or resized.
- **C:** Incorrect for this question. A one- or three-year commitment that discounts the capacity always in use. Why the correct answer wins: An instance with no traffic should be stopped or removed rather than committed or resized.
- **D:** Incorrect for this question. Shrink an instance whose peak fits a smaller shape. Why the correct answer wins: An instance with no traffic should be stopped or removed rather than committed or resized.

### Question 29 — B

Answer: Keep the current engine and version. Keeping the engine avoids the rewrites the timeline cannot absorb. A lift of the existing engine with no conversion work, retaining its behaviour and licensing. Local study-map skill 1.14 (Application and Database Dependencies), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 1 (design innovative, scalable, and highly available cloud database solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Keep two databases current from application code during the transition. Why the correct answer wins: Keeping the engine avoids the rewrites the timeline cannot absorb.
- **B:** Correct. A lift of the existing engine with no conversion work, retaining its behaviour and licensing. In this case: Keeping the engine avoids the rewrites the timeline cannot absorb.
- **C:** Incorrect for this question. Weigh engine compatibility and code rewrite effort before selecting a destination. Why the correct answer wins: Keeping the engine avoids the rewrites the timeline cannot absorb.
- **D:** Incorrect for this question. A managed path that converts schema and code from a different source engine. Why the correct answer wins: Keeping the engine avoids the rewrites the timeline cannot absorb.

### Question 30 — C, E

Answers: Place the instance in the required region; Route the audit logs to a locked log bucket. The in-country placement settles where the data sits, and retained audit storage keeps the access evidence beyond the default retention. A location choice that keeps data inside the regulated boundary. Export entries to storage whose retention cannot be shortened. Local study-map skill 1.15 (Regulatory, Compliance, and Organization Policy), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 1 (design innovative, scalable, and highly available cloud database solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Default encryption at rest with keys the customer neither sees nor manages. Why the correct answer wins: The in-country placement settles where the data sits, and retained audit storage keeps the access evidence beyond the default retention.
- **B:** Incorrect for this question. Absorb repeated reads in memory so the database sees fewer of them. Why the correct answer wins: The in-country placement settles where the data sits, and retained audit storage keeps the access evidence beyond the default retention.
- **C:** Correct. Export entries to storage whose retention cannot be shortened. In this case: The in-country placement settles where the data sits, and retained audit storage keeps the access evidence beyond the default retention.
- **D:** Incorrect for this question. A constraint that keeps database resources inside the approved regions. Why the correct answer wins: The in-country placement settles where the data sits, and retained audit storage keeps the access evidence beyond the default retention.
- **E:** Correct. A location choice that keeps data inside the regulated boundary. In this case: The in-country placement settles where the data sits, and retained audit storage keeps the access evidence beyond the default retention.

### Question 31 — C

Answer: Enforce the location with an organization policy. An organization-level constraint blocks such creation regardless of who owns the project. A constraint that keeps database resources inside the approved regions. Local study-map skill 1.15 (Regulatory, Compliance, and Organization Policy), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 1 (design innovative, scalable, and highly available cloud database solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Export entries to storage whose retention cannot be shortened. Why the correct answer wins: An organization-level constraint blocks such creation regardless of who owns the project.
- **B:** Incorrect for this question. A location choice that keeps data inside the regulated boundary. Why the correct answer wins: An organization-level constraint blocks such creation regardless of who owns the project.
- **C:** Correct. A constraint that keeps database resources inside the approved regions. In this case: An organization-level constraint blocks such creation regardless of who owns the project.
- **D:** Incorrect for this question. A key the customer owns and can rotate or revoke. Why the correct answer wins: An organization-level constraint blocks such creation regardless of who owns the project.

### Question 32 — A

Answer: Keep part of the estate on-premises with a hybrid link. A hybrid link keeps the existing system in place and connects the new services to it. Interconnect the remaining on-premises system rather than moving it. Local study-map skill 1.16 (Federation, Exports, and Hybrid Spans), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 1 (design innovative, scalable, and highly available cloud database solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Correct. Interconnect the remaining on-premises system rather than moving it. In this case: A hybrid link keeps the existing system in place and connects the new services to it.
- **B:** Incorrect for this question. Keep the old system read-only for a defined period, then remove it. Why the correct answer wins: A hybrid link keeps the existing system in place and connects the new services to it.
- **C:** Incorrect for this question. Copy the analytical slice into the warehouse on a schedule. Why the correct answer wins: A hybrid link keeps the existing system in place and connects the new services to it.
- **D:** Incorrect for this question. Read the operational table from BigQuery without copying it first. Why the correct answer wins: A hybrid link keeps the existing system in place and connects the new services to it.

### Question 33 — D

Answer: Grant the predefined database role. A narrower predefined role gives the needed visibility without the write capability the editor role carries. A Google-managed role that carries the permissions the operator needs. Local study-map skill 2.1 (IAM for Database Connectivity), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 2 (manage a solution that can span multiple database technologies): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Individual accountability at the engine layer rather than a shared login. Why the correct answer wins: A narrower predefined role gives the needed visibility without the write capability the editor role carries.
- **B:** Incorrect for this question. A broad legacy role that can change most resources in the project. Why the correct answer wins: A narrower predefined role gives the needed visibility without the write capability the editor role carries.
- **C:** Incorrect for this question. A role built from an explicit permission list. Why the correct answer wins: A narrower predefined role gives the needed visibility without the write capability the editor role carries.
- **D:** Correct. A Google-managed role that carries the permissions the operator needs. In this case: A narrower predefined role gives the needed visibility without the write capability the editor role carries.

### Question 34 — C

Answer: Limit the user to the required schema. Grants scoped to the two named schemas give exactly the access the tool needs. Grant access to named objects instead of the whole instance. Local study-map skill 2.1 (IAM for Database Connectivity), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 2 (manage a solution that can span multiple database technologies): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A broad legacy role that can change most resources in the project. Why the correct answer wins: Grants scoped to the two named schemas give exactly the access the tool needs.
- **B:** Incorrect for this question. A single credential used by every workload that touches the database. Why the correct answer wins: Grants scoped to the two named schemas give exactly the access the tool needs.
- **C:** Correct. Grant access to named objects instead of the whole instance. In this case: Grants scoped to the two named schemas give exactly the access the tool needs.
- **D:** Incorrect for this question. A role built from an explicit permission list. Why the correct answer wins: Grants scoped to the two named schemas give exactly the access the tool needs.

### Question 35 — A, D

Answers: Have the application authenticate as a service account; Enable IAM database authentication. The service account authenticates the workload without a password, and IAM database authentication covers the human users through their Google identities. A workload identity that can be authorized by IAM without a stored password. Map an IAM principal to a database user so no password is stored. Local study-map skill 2.2 (Database Users and Authentication), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 2 (manage a solution that can span multiple database technologies): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Correct. Map an IAM principal to a database user so no password is stored. In this case: The service account authenticates the workload without a password, and IAM database authentication covers the human users through their Google identities.
- **B:** Incorrect for this question. A native database user whose credential must be rotated and stored. Why the correct answer wins: The service account authenticates the workload without a password, and IAM database authentication covers the human users through their Google identities.
- **C:** Incorrect for this question. A single credential used by every workload that touches the database. Why the correct answer wins: The service account authenticates the workload without a password, and IAM database authentication covers the human users through their Google identities.
- **D:** Correct. A workload identity that can be authorized by IAM without a stored password. In this case: The service account authenticates the workload without a password, and IAM database authentication covers the human users through their Google identities.
- **E:** Incorrect for this question. A broad legacy role that can change most resources in the project. Why the correct answer wins: The service account authenticates the workload without a password, and IAM database authentication covers the human users through their Google identities.

### Question 36 — D

Answer: Add the index the slow query needs. An index on the selective predicate turns the scan into a lookup. Local study-map skill 2.3 (Slow Queries and Missing Indexes), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 2 (manage a solution that can span multiple database technologies): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Give the planner current cardinality so it stops choosing a poor plan. Why the correct answer wins: An index on the selective predicate turns the scan into a lookup.
- **B:** Incorrect for this question. Give sorts and joins more working memory on the instance. Why the correct answer wins: An index on the selective predicate turns the scan into a lookup.
- **C:** Incorrect for this question. Split one table into ranges so pruning and maintenance act on less data. Why the correct answer wins: An index on the selective predicate turns the scan into a lookup.
- **D:** Correct. In this case: An index on the selective predicate turns the scan into a lookup.

### Question 37 — C

Answer: Read the query plan for the statement. The plan shows the chosen path, which tells the team what to change rather than guessing. Inspect the chosen scan and join order before changing anything. Local study-map skill 2.3 (Slow Queries and Missing Indexes), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 2 (manage a solution that can span multiple database technologies): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Give the planner current cardinality so it stops choosing a poor plan. Why the correct answer wins: The plan shows the chosen path, which tells the team what to change rather than guessing.
- **B:** Incorrect for this question. Create an index that turns a scan into a lookup for the predicate. Why the correct answer wins: The plan shows the chosen path, which tells the team what to change rather than guessing.
- **C:** Correct. Inspect the chosen scan and join order before changing anything. In this case: The plan shows the chosen path, which tells the team what to change rather than guessing.
- **D:** Incorrect for this question. Remove write amplification from an index nothing reads. Why the correct answer wins: The plan shows the chosen path, which tells the team what to change rather than guessing.

### Question 38 — D

Answer: Terminate the session that holds the lock. Ending that idle transaction releases the queue, which no batching or inspection does on its own. End the blocking transaction so the queue drains. Local study-map skill 2.4 (Locking and Resource Contention), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 2 (manage a solution that can span multiple database technologies): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Find the transaction that holds the lock others wait on. Why the correct answer wins: Ending that idle transaction releases the queue, which no batching or inspection does on its own.
- **B:** Incorrect for this question. Separate analytical reads from the write path. Why the correct answer wins: Ending that idle transaction releases the queue, which no batching or inspection does on its own.
- **C:** Incorrect for this question. Cut per-row network and commit overhead in the application. Why the correct answer wins: Ending that idle transaction releases the queue, which no batching or inspection does on its own.
- **D:** Correct. End the blocking transaction so the queue drains. In this case: Ending that idle transaction releases the queue, which no batching or inspection does on its own.

### Question 39 — A

Answer: Inspect lock waits and blocking sessions. The lock graph exposes the chain, which is what a fix has to break. Find the transaction that holds the lock others wait on. Local study-map skill 2.4 (Locking and Resource Contention), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 2 (manage a solution that can span multiple database technologies): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Correct. Find the transaction that holds the lock others wait on. In this case: The lock graph exposes the chain, which is what a fix has to break.
- **B:** Incorrect for this question. Create an index that turns a scan into a lookup for the predicate. Why the correct answer wins: The lock graph exposes the chain, which is what a fix has to break.
- **C:** Incorrect for this question. End the blocking transaction so the queue drains. Why the correct answer wins: The lock graph exposes the chain, which is what a fix has to break.
- **D:** Incorrect for this question. Give the planner current cardinality so it stops choosing a poor plan. Why the correct answer wins: The lock graph exposes the chain, which is what a fix has to break.

### Question 40 — C

Answer: Watch CPU, memory, disk, and IOPS together. The instance view presents memory and storage signals side by side, which separates the two causes. Read the instance-level signals before attributing the symptom to the query. Local study-map skill 2.5 (Database Vitals Monitoring), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 2 (manage a solution that can span multiple database technologies): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A single view of health, security, and version posture across database instances. Why the correct answer wins: The instance view presents memory and storage signals side by side, which separates the two causes.
- **B:** Incorrect for this question. A per-query view of latency, load, and wait events on the instance. Why the correct answer wins: The instance view presents memory and storage signals side by side, which separates the two causes.
- **C:** Correct. Read the instance-level signals before attributing the symptom to the query. In this case: The instance view presents memory and storage signals side by side, which separates the two causes.
- **D:** Incorrect for this question. The engine log of statements that exceeded the long-query threshold. Why the correct answer wins: The instance view presents memory and storage signals side by side, which separates the two causes.

### Question 41 — C

Answer: Use Query Insights to find the heavy statements. Per-query wait breakdown attributes time to a category at the statement level. A per-query view of latency, load, and wait events on the instance. Local study-map skill 2.5 (Database Vitals Monitoring), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 2 (manage a solution that can span multiple database technologies): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Read the instance-level signals before attributing the symptom to the query. Why the correct answer wins: Per-query wait breakdown attributes time to a category at the statement level.
- **B:** Incorrect for this question. Turn a recurring log pattern into a metric that can be charted and alerted on. Why the correct answer wins: Per-query wait breakdown attributes time to a category at the statement level.
- **C:** Correct. A per-query view of latency, load, and wait events on the instance. In this case: Per-query wait breakdown attributes time to a category at the statement level.
- **D:** Incorrect for this question. The engine log of statements that exceeded the long-query threshold. Why the correct answer wins: Per-query wait breakdown attributes time to a category at the statement level.

### Question 42 — D, E

Answers: Request a quota increase for the project; Move the job outside the contention window. Raising the ceiling covers the genuine peak, and spreading the jobs reduces how much of the limit the burst needs. Raise the project-level ceiling so the operation is no longer refused. Stagger the work so concurrent operations stop colliding on the same limit. Local study-map skill 2.6 (Quotas and Limits), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 2 (manage a solution that can span multiple database technologies): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Avoid a full-disk outage at the cost of unplanned storage growth. Why the correct answer wins: Raising the ceiling covers the genuine peak, and spreading the jobs reduces how much of the limit the burst needs.
- **B:** Incorrect for this question. Repeat the call after a growing delay so a transient refusal clears. Why the correct answer wins: Raising the ceiling covers the genuine peak, and spreading the jobs reduces how much of the limit the burst needs.
- **C:** Incorrect for this question. A flat-file extract for a downstream loader rather than a restore. Why the correct answer wins: Raising the ceiling covers the genuine peak, and spreading the jobs reduces how much of the limit the burst needs.
- **D:** Correct. Stagger the work so concurrent operations stop colliding on the same limit. In this case: Raising the ceiling covers the genuine peak, and spreading the jobs reduces how much of the limit the burst needs.
- **E:** Correct. Raise the project-level ceiling so the operation is no longer refused. In this case: Raising the ceiling covers the genuine peak, and spreading the jobs reduces how much of the limit the burst needs.

### Question 43 — A

Answer: Create an alerting policy on the metric. An alerting policy on the state signal notifies the team without anyone watching a dashboard. A condition that pages a human when the threshold is crossed. Local study-map skill 2.7 (Alerts for Errors and Performance), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 2 (manage a solution that can span multiple database technologies): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Correct. A condition that pages a human when the threshold is crossed. In this case: An alerting policy on the state signal notifies the team without anyone watching a dashboard.
- **B:** Incorrect for this question. Page on failed statements rather than on resource saturation alone. Why the correct answer wins: An alerting policy on the state signal notifies the team without anyone watching a dashboard.
- **C:** Incorrect for this question. Turn a recurring log pattern into a metric that can be charted and alerted on. Why the correct answer wins: An alerting policy on the state signal notifies the team without anyone watching a dashboard.
- **D:** Incorrect for this question. Read the instance-level signals before attributing the symptom to the query. Why the correct answer wins: An alerting policy on the state signal notifies the team without anyone watching a dashboard.

### Question 44 — B

Answer: Alert on the database error rate. Alerting on the error rate reflects the failure users experience rather than a resource that may still be healthy. Page on failed statements rather than on resource saturation alone. Local study-map skill 2.7 (Alerts for Errors and Performance), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 2 (manage a solution that can span multiple database technologies): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A condition that pages a human when the threshold is crossed. Why the correct answer wins: Alerting on the error rate reflects the failure users experience rather than a resource that may still be healthy.
- **B:** Correct. Page on failed statements rather than on resource saturation alone. In this case: Alerting on the error rate reflects the failure users experience rather than a resource that may still be healthy.
- **C:** Incorrect for this question. Page when the copy falls behind the primary by more than the budget. Why the correct answer wins: Alerting on the error rate reflects the failure users experience rather than a resource that may still be healthy.
- **D:** Incorrect for this question. A per-query view of latency, load, and wait events on the instance. Why the correct answer wins: Alerting on the error rate reflects the failure users experience rather than a resource that may still be healthy.

### Question 45 — D

Answer: Enable automated backups with a retention window. Automated backups give a managed schedule and retention that manual dumps do not. Scheduled backups kept for a chosen number of days. Local study-map skill 2.8 (Backup and Recovery Option Selection), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 2 (manage a solution that can span multiple database technologies): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A flat-file extract for a downstream loader rather than a restore. Why the correct answer wins: Automated backups give a managed schedule and retention that manual dumps do not.
- **B:** Incorrect for this question. A copy of the current data created without touching the source. Why the correct answer wins: Automated backups give a managed schedule and retention that manual dumps do not.
- **C:** Incorrect for this question. A manual checkpoint taken immediately before a risky operation. Why the correct answer wins: Automated backups give a managed schedule and retention that manual dumps do not.
- **D:** Correct. Scheduled backups kept for a chosen number of days. In this case: Automated backups give a managed schedule and retention that manual dumps do not.

### Question 46 — A

Answer: Enable point-in-time recovery. Point-in-time recovery replays the log to that moment, which scheduled backups or a dump cannot reach. Continuous log capture that lets the instance return to an arbitrary moment. Local study-map skill 2.8 (Backup and Recovery Option Selection), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 2 (manage a solution that can span multiple database technologies): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Correct. Continuous log capture that lets the instance return to an arbitrary moment. In this case: Point-in-time recovery replays the log to that moment, which scheduled backups or a dump cannot reach.
- **B:** Incorrect for this question. A portable SQL dump taken with the engine tooling. Why the correct answer wins: Point-in-time recovery replays the log to that moment, which scheduled backups or a dump cannot reach.
- **C:** Incorrect for this question. Scheduled backups kept for a chosen number of days. Why the correct answer wins: Point-in-time recovery replays the log to that moment, which scheduled backups or a dump cannot reach.
- **D:** Incorrect for this question. Keep backups longer so an older restore point remains available. Why the correct answer wins: Point-in-time recovery replays the log to that moment, which scheduled backups or a dump cannot reach.

### Question 47 — A

Answer: Export a logical dump to Cloud Storage. A logical dump carries schema and data in a restorable form, which a flat file or a federated query does not. A portable SQL dump taken with the engine tooling. Local study-map skill 2.9 (Export and Import Configuration), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 2 (manage a solution that can span multiple database technologies): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Correct. A portable SQL dump taken with the engine tooling. In this case: A logical dump carries schema and data in a restorable form, which a flat file or a federated query does not.
- **B:** Incorrect for this question. Load a logical dump file into the database through the managed import path. Why the correct answer wins: A logical dump carries schema and data in a restorable form, which a flat file or a federated query does not.
- **C:** Incorrect for this question. Read the operational table from BigQuery without copying it first. Why the correct answer wins: A logical dump carries schema and data in a restorable form, which a flat file or a federated query does not.
- **D:** Incorrect for this question. A flat-file extract for a downstream loader rather than a restore. Why the correct answer wins: A logical dump carries schema and data in a restorable form, which a flat file or a federated query does not.

### Question 48 — D

Answer: Design the restore path to the stated RTO and RPO. The recovery point and time objectives define the acceptable loss and duration the mechanism must meet. Choose mechanisms by how much data and time the business can lose. Local study-map skill 2.10 (RTO, RPO, and Point-in-Time Recovery), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 2 (manage a solution that can span multiple database technologies): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Continuous log capture that lets the instance return to an arbitrary moment. Why the correct answer wins: The recovery point and time objectives define the acceptable loss and duration the mechanism must meet.
- **B:** Incorrect for this question. A copy of the current data created without touching the source. Why the correct answer wins: The recovery point and time objectives define the acceptable loss and duration the mechanism must meet.
- **C:** Incorrect for this question. Scheduled backups kept for a chosen number of days. Why the correct answer wins: The recovery point and time objectives define the acceptable loss and duration the mechanism must meet.
- **D:** Correct. Choose mechanisms by how much data and time the business can lose. In this case: The recovery point and time objectives define the acceptable loss and duration the mechanism must meet.

### Question 49 — D

Answer: Restore to the timestamp before the bad change. A point-in-time restore returns the instance to the moment before the deployment. A point-in-time restore that discards the later writes on the same instance. Local study-map skill 2.10 (RTO, RPO, and Point-in-Time Recovery), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 2 (manage a solution that can span multiple database technologies): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Trigger a switchover in a test window and observe how long writes are unavailable. Why the correct answer wins: A point-in-time restore returns the instance to the moment before the deployment.
- **B:** Incorrect for this question. A copy of the current data created without touching the source. Why the correct answer wins: A point-in-time restore returns the instance to the moment before the deployment.
- **C:** Incorrect for this question. A portable SQL dump taken with the engine tooling. Why the correct answer wins: A point-in-time restore returns the instance to the moment before the deployment.
- **D:** Correct. A point-in-time restore that discards the later writes on the same instance. In this case: A point-in-time restore returns the instance to the moment before the deployment.

### Question 50 — B, E

Answers: Set the garbage-collection policy on the column family; Add a lifecycle rule to the export bucket. The garbage-collection policy bounds versions inside the table, and a lifecycle rule purges the exported snapshots. A rule that drops versions by age or count, which also bounds recovery. Move or delete aged exports so the bucket does not grow without limit. Local study-map skill 2.11 (Data Retention Management), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 2 (manage a solution that can span multiple database technologies): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Avoid a full-disk outage at the cost of unplanned storage growth. Why the correct answer wins: The garbage-collection policy bounds versions inside the table, and a lifecycle rule purges the exported snapshots.
- **B:** Correct. Move or delete aged exports so the bucket does not grow without limit. In this case: The garbage-collection policy bounds versions inside the table, and a lifecycle rule purges the exported snapshots.
- **C:** Incorrect for this question. Delete or expire records once the legal hold period ends. Why the correct answer wins: The garbage-collection policy bounds versions inside the table, and a lifecycle rule purges the exported snapshots.
- **D:** Incorrect for this question. Expire documents once their usefulness ends. Why the correct answer wins: The garbage-collection policy bounds versions inside the table, and a lifecycle rule purges the exported snapshots.
- **E:** Correct. A rule that drops versions by age or count, which also bounds recovery. In this case: The garbage-collection policy bounds versions inside the table, and a lifecycle rule purges the exported snapshots.

### Question 51 — A

Answer: Send reporting queries to the read replica. Routing those queries to the idle replica moves the load to capacity already paid for. Separate analytical reads from the write path. Local study-map skill 2.12 (Scaling Up Versus Scaling Out), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 2 (manage a solution that can span multiple database technologies): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Correct. Separate analytical reads from the write path. In this case: Routing those queries to the idle replica moves the load to capacity already paid for.
- **B:** Incorrect for this question. Send reads to a copy so the primary keeps its capacity for writes. Why the correct answer wins: Routing those queries to the idle replica moves the load to capacity already paid for.
- **C:** Incorrect for this question. Absorb repeated reads in memory so the database sees fewer of them. Why the correct answer wins: Routing those queries to the idle replica moves the load to capacity already paid for.
- **D:** Incorrect for this question. Move the instance to a larger shape so more vCPU and memory serve the same data. Why the correct answer wins: Routing those queries to the idle replica moves the load to capacity already paid for.

### Question 52 — D

Answer: Partition the large table. Partitioning by day turns the delete into dropping a partition. Split one table into ranges so pruning and maintenance act on less data. Local study-map skill 2.12 (Scaling Up Versus Scaling Out), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 2 (manage a solution that can span multiple database technologies): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Create an index that turns a scan into a lookup for the predicate. Why the correct answer wins: Partitioning by day turns the delete into dropping a partition.
- **B:** Incorrect for this question. Split rows by a key so each instance owns a subset of the workload. Why the correct answer wins: Partitioning by day turns the delete into dropping a partition.
- **C:** Incorrect for this question. Move the instance to a larger shape so more vCPU and memory serve the same data. Why the correct answer wins: Partitioning by day turns the delete into dropping a partition.
- **D:** Correct. Split one table into ranges so pruning and maintenance act on less data. In this case: Partitioning by day turns the delete into dropping a partition.

### Question 53 — C

Answer: Add a cross-region read replica. A cross-region replica ships changes continuously and can be promoted. A copy in a second region that serves reads and can be promoted. Local study-map skill 2.13 (Replication Strategies), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 2 (manage a solution that can span multiple database technologies): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. An AlloyDB cross-region copy that can be promoted to a primary cluster. Why the correct answer wins: A cross-region replica ships changes continuously and can be promoted.
- **B:** Incorrect for this question. A topology that places replicas in separate regions for regional-failure tolerance. Why the correct answer wins: A cross-region replica ships changes continuously and can be promoted.
- **C:** Correct. A copy in a second region that serves reads and can be promoted. In this case: A cross-region replica ships changes continuously and can be promoted.
- **D:** Incorrect for this question. Rebuild the database in the surviving region from the latest backup. Why the correct answer wins: A cross-region replica ships changes continuously and can be promoted.

### Question 54 — A, B

Answers: Drop the unused index; Batch the writes into fewer round trips. Removing indexes that nothing reads cuts maintenance, and batching the commits reduces the per-write overhead. Remove write amplification from an index nothing reads. Cut per-row network and commit overhead in the application. Local study-map skill 2.14 (Query Optimization for Cost and Performance), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 2 (manage a solution that can span multiple database technologies): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Correct. Remove write amplification from an index nothing reads. In this case: Removing indexes that nothing reads cuts maintenance, and batching the commits reduces the per-write overhead.
- **B:** Correct. Cut per-row network and commit overhead in the application. In this case: Removing indexes that nothing reads cuts maintenance, and batching the commits reduces the per-write overhead.
- **C:** Incorrect for this question. Absorb repeated reads in memory so the database sees fewer of them. Why the correct answer wins: Removing indexes that nothing reads cuts maintenance, and batching the commits reduces the per-write overhead.
- **D:** Incorrect for this question. Give sorts and joins more working memory on the instance. Why the correct answer wins: Removing indexes that nothing reads cuts maintenance, and batching the commits reduces the per-write overhead.
- **E:** Incorrect for this question. Create an index that turns a scan into a lookup for the predicate. Why the correct answer wins: Removing indexes that nothing reads cuts maintenance, and batching the commits reduces the per-write overhead.

### Question 55 — C

Answer: Run the task on a managed schedule. A managed schedule executes the recurring maintenance unattended. A recurring trigger that performs the work with nobody present. Local study-map skill 2.15 (Automated Maintenance and Scheduled Exports), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 2 (manage a solution that can span multiple database technologies): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Trigger a switchover in a test window and observe how long writes are unavailable. Why the correct answer wins: A managed schedule executes the recurring maintenance unattended.
- **B:** Incorrect for this question. A manual checkpoint taken immediately before a risky operation. Why the correct answer wins: A managed schedule executes the recurring maintenance unattended.
- **C:** Correct. A recurring trigger that performs the work with nobody present. In this case: A managed schedule executes the recurring maintenance unattended.
- **D:** Incorrect for this question. Create the resource interactively with no stored definition. Why the correct answer wins: A managed schedule executes the recurring maintenance unattended.

### Question 56 — B

Answer: Test the upgrade on a clone first. Testing on a clone exposes the failure while production is untouched. Rehearse the change against a copy before touching production. Local study-map skill 2.15 (Automated Maintenance and Scheduled Exports), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 2 (manage a solution that can span multiple database technologies): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A recovery point that makes the upgrade reversible in practice. Why the correct answer wins: Testing on a clone exposes the failure while production is untouched.
- **B:** Correct. Rehearse the change against a copy before touching production. In this case: Testing on a clone exposes the failure while production is untouched.
- **C:** Incorrect for this question. Compare the signal after cutover against the pre-change baseline. Why the correct answer wins: Testing on a clone exposes the failure while production is untouched.
- **D:** Incorrect for this question. Change the engine version on the running instance during the window. Why the correct answer wins: Testing on a clone exposes the failure while production is untouched.

### Question 57 — B

Answer: Track the availability signal against the agreed objective. Comparing the availability signal against the committed objective measures the promise. Compare observed service levels with the commitment rather than watching raw resource metrics. Local study-map skill 2.16 (Managed Upgrades and SLA Monitoring), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 2 (manage a solution that can span multiple database technologies): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A condition that pages a human when the threshold is crossed. Why the correct answer wins: Comparing the availability signal against the committed objective measures the promise.
- **B:** Correct. Compare observed service levels with the commitment rather than watching raw resource metrics. In this case: Comparing the availability signal against the committed objective measures the promise.
- **C:** Incorrect for this question. Read the instance-level signals before attributing the symptom to the query. Why the correct answer wins: Comparing the availability signal against the committed objective measures the promise.
- **D:** Incorrect for this question. A single view of health, security, and version posture across database instances. Why the correct answer wins: Comparing the availability signal against the committed objective measures the promise.

### Question 58 — B, D

Answers: Use Database Migration Service for the same engine; Set up reverse replication to the source. Continuous replication keeps the outage to the switch, and replication back to the source keeps the rollback lossless. A managed migration that moves a supported engine to the same engine on Google Cloud. Keep writing back to the original system so a rollback loses nothing. Local study-map skill 3.1 (Migration Strategy and Downtime Budget), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 3 (migrate data solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A bulk load followed by a catch-up pass for the writes made during the load. Why the correct answer wins: Continuous replication keeps the outage to the switch, and replication back to the source keeps the rollback lossless.
- **B:** Correct. A managed migration that moves a supported engine to the same engine on Google Cloud. In this case: Continuous replication keeps the outage to the switch, and replication back to the source keeps the rollback lossless.
- **C:** Incorrect for this question. Stop the source, load everything, and start the target in one window. Why the correct answer wins: Continuous replication keeps the outage to the switch, and replication back to the source keeps the rollback lossless.
- **D:** Correct. Keep writing back to the original system so a rollback loses nothing. In this case: Continuous replication keeps the outage to the switch, and replication back to the source keeps the rollback lossless.
- **E:** Incorrect for this question. Keep two databases current from application code during the transition. Why the correct answer wins: Continuous replication keeps the outage to the switch, and replication back to the source keeps the rollback lossless.

### Question 59 — B

Answer: Accept a scheduled extended outage. A stop, load, and start in one accepted window needs no replication machinery at that size. Stop the source, load everything, and start the target in one window. Local study-map skill 3.1 (Migration Strategy and Downtime Budget), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 3 (migrate data solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A managed migration that moves a supported engine to the same engine on Google Cloud. Why the correct answer wins: A stop, load, and start in one accepted window needs no replication machinery at that size.
- **B:** Correct. Stop the source, load everything, and start the target in one window. In this case: A stop, load, and start in one accepted window needs no replication machinery at that size.
- **C:** Incorrect for this question. Keep two databases current from application code during the transition. Why the correct answer wins: A stop, load, and start in one accepted window needs no replication machinery at that size.
- **D:** Incorrect for this question. A rehearsed sequence with a named decision point and a way back. Why the correct answer wins: A stop, load, and start in one accepted window needs no replication machinery at that size.

### Question 60 — D

Answer: Follow a cutover runbook with a rollback step. A runbook with owners, evidence, and an abort condition makes the cutover a controlled procedure. A rehearsed sequence with a named decision point and a way back. Local study-map skill 3.1 (Migration Strategy and Downtime Budget), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 3 (migrate data solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Keep two databases current from application code during the transition. Why the correct answer wins: A runbook with owners, evidence, and an abort condition makes the cutover a controlled procedure.
- **B:** Incorrect for this question. Stop the source, load everything, and start the target in one window. Why the correct answer wins: A runbook with owners, evidence, and an abort condition makes the cutover a controlled procedure.
- **C:** Incorrect for this question. Stop application writes so the last increment can be applied cleanly. Why the correct answer wins: A runbook with owners, evidence, and an abort condition makes the cutover a controlled procedure.
- **D:** Correct. A rehearsed sequence with a named decision point and a way back. In this case: A runbook with owners, evidence, and an abort condition makes the cutover a controlled procedure.

### Question 61 — C

Answer: Use Database Migration Service with schema conversion. The heterogeneous managed path includes schema conversion with reviewable output. A managed path that converts schema and code from a different source engine. Local study-map skill 3.2 (Migration Tool Selection), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 3 (migrate data solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Change data capture from the source into a Google Cloud target. Why the correct answer wins: The heterogeneous managed path includes schema conversion with reviewable output.
- **B:** Incorrect for this question. A managed migration that moves a supported engine to the same engine on Google Cloud. Why the correct answer wins: The heterogeneous managed path includes schema conversion with reviewable output.
- **C:** Correct. A managed path that converts schema and code from a different source engine. In this case: The heterogeneous managed path includes schema conversion with reviewable output.
- **D:** Incorrect for this question. A bulk load followed by a catch-up pass for the writes made during the load. Why the correct answer wins: The heterogeneous managed path includes schema conversion with reviewable output.

### Question 62 — D

Answer: Stream changes with Datastream. Change data capture publishes the changes to the warehouse without a cutover. Change data capture from the source into a Google Cloud target. Local study-map skill 3.2 (Migration Tool Selection), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 3 (migrate data solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A managed path that converts schema and code from a different source engine. Why the correct answer wins: Change data capture publishes the changes to the warehouse without a cutover.
- **B:** Incorrect for this question. Copy the analytical slice into the warehouse on a schedule. Why the correct answer wins: Change data capture publishes the changes to the warehouse without a cutover.
- **C:** Incorrect for this question. A portable SQL dump taken with the engine tooling. Why the correct answer wins: Change data capture publishes the changes to the warehouse without a cutover.
- **D:** Correct. Change data capture from the source into a Google Cloud target. In this case: Change data capture publishes the changes to the warehouse without a cutover.

### Question 63 — C

Answer: Dump, restore, then replay the changes. A dump and restore copies the data once, which is all a test environment needs. A bulk load followed by a catch-up pass for the writes made during the load. Local study-map skill 3.2 (Migration Tool Selection), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 3 (migrate data solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Keep two databases current from application code during the transition. Why the correct answer wins: A dump and restore copies the data once, which is all a test environment needs.
- **B:** Incorrect for this question. Replay the writes made during the bulk load so the target is current at the switch. Why the correct answer wins: A dump and restore copies the data once, which is all a test environment needs.
- **C:** Correct. A bulk load followed by a catch-up pass for the writes made during the load. In this case: A dump and restore copies the data once, which is all a test environment needs.
- **D:** Incorrect for this question. A managed path that converts schema and code from a different source engine. Why the correct answer wins: A dump and restore copies the data once, which is all a test environment needs.

### Question 64 — B, E

Answers: Build the schema in a conversion workspace; Rewrite the stored procedures and DML by hand. The workspace holds the generated schema for review and editing, and the unsupported procedures must be rewritten by hand. Convert DDL and code with reviewable, editable output before the load starts. Port procedural code the conversion tool flags as unsupported. Local study-map skill 3.3 (Heterogeneous Schema and DDL Conversion), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 3 (migrate data solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Set generated-key counters past the highest value so inserts do not collide. Why the correct answer wins: The workspace holds the generated schema for review and editing, and the unsupported procedures must be rewritten by hand.
- **B:** Correct. Convert DDL and code with reviewable, editable output before the load starts. In this case: The workspace holds the generated schema for review and editing, and the unsupported procedures must be rewritten by hand.
- **C:** Incorrect for this question. Compare the target answers with production before the switch. Why the correct answer wins: The workspace holds the generated schema for review and editing, and the unsupported procedures must be rewritten by hand.
- **D:** Incorrect for this question. Move clients to the new endpoint as the final cutover action. Why the correct answer wins: The workspace holds the generated schema for review and editing, and the unsupported procedures must be rewritten by hand.
- **E:** Correct. Port procedural code the conversion tool flags as unsupported. In this case: The workspace holds the generated schema for review and editing, and the unsupported procedures must be rewritten by hand.

### Question 65 — D

Answer: Reset the sequences after the bulk load. The counters must be advanced past the highest loaded value. Set generated-key counters past the highest value so inserts do not collide. Local study-map skill 3.3 (Heterogeneous Schema and DDL Conversion), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 3 (migrate data solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Prove the target holds the same rows as the source before cutover. Why the correct answer wins: The counters must be advanced past the highest loaded value.
- **B:** Incorrect for this question. Port procedural code the conversion tool flags as unsupported. Why the correct answer wins: The counters must be advanced past the highest loaded value.
- **C:** Incorrect for this question. Convert DDL and code with reviewable, editable output before the load starts. Why the correct answer wins: The counters must be advanced past the highest loaded value.
- **D:** Correct. Set generated-key counters past the highest value so inserts do not collide. In this case: The counters must be advanced past the highest loaded value.

### Question 66 — A

Answer: Replay read traffic against the target. Replaying the statements exercises the real query paths and shows where answers differ. Compare the target answers with production before the switch. Local study-map skill 3.4 (DML and Application Code Conversion), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 3 (migrate data solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Correct. Compare the target answers with production before the switch. In this case: Replaying the statements exercises the real query paths and shows where answers differ.
- **B:** Incorrect for this question. A rehearsed sequence with a named decision point and a way back. Why the correct answer wins: Replaying the statements exercises the real query paths and shows where answers differ.
- **C:** Incorrect for this question. Prove the target holds the same rows as the source before cutover. Why the correct answer wins: Replaying the statements exercises the real query paths and shows where answers differ.
- **D:** Incorrect for this question. Port procedural code the conversion tool flags as unsupported. Why the correct answer wins: Replaying the statements exercises the real query paths and shows where answers differ.

### Question 67 — C

Answer: Rewrite the stored procedures and DML by hand. The statements have to be rewritten for the target dialect. Port procedural code the conversion tool flags as unsupported. Local study-map skill 3.4 (DML and Application Code Conversion), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 3 (migrate data solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Convert DDL and code with reviewable, editable output before the load starts. Why the correct answer wins: The statements have to be rewritten for the target dialect.
- **B:** Incorrect for this question. Keep two databases current from application code during the transition. Why the correct answer wins: The statements have to be rewritten for the target dialect.
- **C:** Correct. Port procedural code the conversion tool flags as unsupported. In this case: The statements have to be rewritten for the target dialect.
- **D:** Incorrect for this question. Set generated-key counters past the highest value so inserts do not collide. Why the correct answer wins: The statements have to be rewritten for the target dialect.

### Question 68 — A

Answer: Use the engine native logical replication. Replicating the source's change stream keeps the target current throughout. Replicate row changes from the source using the engine feature itself. Local study-map skill 3.5 (Initial Load and Change Replication), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 3 (migrate data solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Correct. Replicate row changes from the source using the engine feature itself. In this case: Replicating the source's change stream keeps the target current throughout.
- **B:** Incorrect for this question. Stop the source, load everything, and start the target in one window. Why the correct answer wins: Replicating the source's change stream keeps the target current throughout.
- **C:** Incorrect for this question. Keep two databases current from application code during the transition. Why the correct answer wins: Replicating the source's change stream keeps the target current throughout.
- **D:** Incorrect for this question. A portable SQL dump taken with the engine tooling. Why the correct answer wins: Replicating the source's change stream keeps the target current throughout.

### Question 69 — B

Answer: Apply the captured change backlog before cutover. The captured backlog must be applied so the target includes every change. Replay the writes made during the bulk load so the target is current at the switch. Local study-map skill 3.5 (Initial Load and Change Replication), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 3 (migrate data solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Stop application writes so the last increment can be applied cleanly. Why the correct answer wins: The captured backlog must be applied so the target includes every change.
- **B:** Correct. Replay the writes made during the bulk load so the target is current at the switch. In this case: The captured backlog must be applied so the target includes every change.
- **C:** Incorrect for this question. Move clients to the new endpoint as the final cutover action. Why the correct answer wins: The captured backlog must be applied so the target includes every change.
- **D:** Incorrect for this question. Prove the target holds the same rows as the source before cutover. Why the correct answer wins: The captured backlog must be applied so the target includes every change.

### Question 70 — A, E

Answers: Reconcile row counts and checksums; Apply the captured change backlog before cutover. Confirming the backlog is fully applied shows nothing is missing, and comparing counts and checksums shows the values match. Prove the target holds the same rows as the source before cutover. Replay the writes made during the bulk load so the target is current at the switch. Local study-map skill 3.6 (Validation and Reconciliation), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 3 (migrate data solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Correct. Replay the writes made during the bulk load so the target is current at the switch. In this case: Confirming the backlog is fully applied shows nothing is missing, and comparing counts and checksums shows the values match.
- **B:** Incorrect for this question. Compare the target answers with production before the switch. Why the correct answer wins: Confirming the backlog is fully applied shows nothing is missing, and comparing counts and checksums shows the values match.
- **C:** Incorrect for this question. Move clients to the new endpoint as the final cutover action. Why the correct answer wins: Confirming the backlog is fully applied shows nothing is missing, and comparing counts and checksums shows the values match.
- **D:** Incorrect for this question. Set generated-key counters past the highest value so inserts do not collide. Why the correct answer wins: Confirming the backlog is fully applied shows nothing is missing, and comparing counts and checksums shows the values match.
- **E:** Correct. Prove the target holds the same rows as the source before cutover. In this case: Confirming the backlog is fully applied shows nothing is missing, and comparing counts and checksums shows the values match.

### Question 71 — B

Answer: Replay read traffic against the target. Replaying those queries and comparing answers tests behaviour rather than row counts. Compare the target answers with production before the switch. Local study-map skill 3.6 (Validation and Reconciliation), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 3 (migrate data solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Keep two databases current from application code during the transition. Why the correct answer wins: Replaying those queries and comparing answers tests behaviour rather than row counts.
- **B:** Correct. Compare the target answers with production before the switch. In this case: Replaying those queries and comparing answers tests behaviour rather than row counts.
- **C:** Incorrect for this question. Prove the target holds the same rows as the source before cutover. Why the correct answer wins: Replaying those queries and comparing answers tests behaviour rather than row counts.
- **D:** Incorrect for this question. A rehearsed sequence with a named decision point and a way back. Why the correct answer wins: Replaying those queries and comparing answers tests behaviour rather than row counts.

### Question 72 — D

Answer: Freeze writes during the cutover. Stopping writes on the source gives the final increment a stable point to complete against. Stop application writes so the last increment can be applied cleanly. Local study-map skill 3.7 (Cutover and Fallback Planning), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 3 (migrate data solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Keep writing back to the original system so a rollback loses nothing. Why the correct answer wins: Stopping writes on the source gives the final increment a stable point to complete against.
- **B:** Incorrect for this question. Move clients to the new endpoint as the final cutover action. Why the correct answer wins: Stopping writes on the source gives the final increment a stable point to complete against.
- **C:** Incorrect for this question. Stop the source, load everything, and start the target in one window. Why the correct answer wins: Stopping writes on the source gives the final increment a stable point to complete against.
- **D:** Correct. Stop application writes so the last increment can be applied cleanly. In this case: Stopping writes on the source gives the final increment a stable point to complete against.

### Question 73 — B

Answer: Repoint the connection string at the target. Repointing the connection string moves the clients to the validated target. Move clients to the new endpoint as the final cutover action. Local study-map skill 3.7 (Cutover and Fallback Planning), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 3 (migrate data solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A client library that resolves the instance and authorizes the connection with IAM. Why the correct answer wins: Repointing the connection string moves the clients to the validated target.
- **B:** Correct. Move clients to the new endpoint as the final cutover action. In this case: Repointing the connection string moves the clients to the validated target.
- **C:** Incorrect for this question. A rehearsed sequence with a named decision point and a way back. Why the correct answer wins: Repointing the connection string moves the clients to the validated target.
- **D:** Incorrect for this question. Stop application writes so the last increment can be applied cleanly. Why the correct answer wins: Repointing the connection string moves the clients to the validated target.

### Question 74 — A

Answer: Follow a cutover runbook with a rollback step. The runbook's abort condition and rollback steps define the action to take. A rehearsed sequence with a named decision point and a way back. Local study-map skill 3.7 (Cutover and Fallback Planning), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 3 (migrate data solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Correct. A rehearsed sequence with a named decision point and a way back. In this case: The runbook's abort condition and rollback steps define the action to take.
- **B:** Incorrect for this question. Stop application writes so the last increment can be applied cleanly. Why the correct answer wins: The runbook's abort condition and rollback steps define the action to take.
- **C:** Incorrect for this question. Keep two databases current from application code during the transition. Why the correct answer wins: The runbook's abort condition and rollback steps define the action to take.
- **D:** Incorrect for this question. Move clients to the new endpoint as the final cutover action. Why the correct answer wins: The runbook's abort condition and rollback steps define the action to take.

### Question 75 — B

Answer: Set up reverse replication to the source. Replication from the target back to the source publishes those writes. Keep writing back to the original system so a rollback loses nothing. Local study-map skill 3.8 (Reverse Replication to the Source), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 3 (migrate data solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Keep two databases current from application code during the transition. Why the correct answer wins: Replication from the target back to the source publishes those writes.
- **B:** Correct. Keep writing back to the original system so a rollback loses nothing. In this case: Replication from the target back to the source publishes those writes.
- **C:** Incorrect for this question. Keep the old system read-only for a defined period, then remove it. Why the correct answer wins: Replication from the target back to the source publishes those writes.
- **D:** Incorrect for this question. Move clients to the new endpoint as the final cutover action. Why the correct answer wins: Replication from the target back to the source publishes those writes.

### Question 76 — A

Answer: Decommission the source after a parallel period. A parallel period with exit criteria sets the end of the fallback. Keep the old system read-only for a defined period, then remove it. Local study-map skill 3.8 (Reverse Replication to the Source), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 3 (migrate data solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Correct. Keep the old system read-only for a defined period, then remove it. In this case: A parallel period with exit criteria sets the end of the fallback.
- **B:** Incorrect for this question. Check the connection and traffic evidence before retiring an instance. Why the correct answer wins: A parallel period with exit criteria sets the end of the fallback.
- **C:** Incorrect for this question. Keep writing back to the original system so a rollback loses nothing. Why the correct answer wins: A parallel period with exit criteria sets the end of the fallback.
- **D:** Incorrect for this question. Move clients to the new endpoint as the final cutover action. Why the correct answer wins: A parallel period with exit criteria sets the end of the fallback.

### Question 77 — C, D

Answers: Use Database Migration Service for the same engine; Measure the catch-up rate before choosing the window. Continuous replication makes the target nearly current, and a measured catch-up rate shows the increment fits the window. A managed migration that moves a supported engine to the same engine on Google Cloud. Size the cutover from how fast changes replay, not from the data volume alone. Local study-map skill 3.9 (Minimizing Downtime During Migration), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 3 (migrate data solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Stop the source, load everything, and start the target in one window. Why the correct answer wins: Continuous replication makes the target nearly current, and a measured catch-up rate shows the increment fits the window.
- **B:** Incorrect for this question. A bulk load followed by a catch-up pass for the writes made during the load. Why the correct answer wins: Continuous replication makes the target nearly current, and a measured catch-up rate shows the increment fits the window.
- **C:** Correct. Size the cutover from how fast changes replay, not from the data volume alone. In this case: Continuous replication makes the target nearly current, and a measured catch-up rate shows the increment fits the window.
- **D:** Correct. A managed migration that moves a supported engine to the same engine on Google Cloud. In this case: Continuous replication makes the target nearly current, and a measured catch-up rate shows the increment fits the window.
- **E:** Incorrect for this question. Keep two databases current from application code during the transition. Why the correct answer wins: Continuous replication makes the target nearly current, and a measured catch-up rate shows the increment fits the window.

### Question 78 — C

Answer: Move the job outside the contention window. Scheduling the cutover away from the known surge keeps the catch-up inside the window. Stagger the work so concurrent operations stop colliding on the same limit. Local study-map skill 3.9 (Minimizing Downtime During Migration), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 3 (migrate data solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Stop the source, load everything, and start the target in one window. Why the correct answer wins: Scheduling the cutover away from the known surge keeps the catch-up inside the window.
- **B:** Incorrect for this question. Size the cutover from how fast changes replay, not from the data volume alone. Why the correct answer wins: Scheduling the cutover away from the known surge keeps the catch-up inside the window.
- **C:** Correct. Stagger the work so concurrent operations stop colliding on the same limit. In this case: Scheduling the cutover away from the known surge keeps the catch-up inside the window.
- **D:** Incorrect for this question. Keep two databases current from application code during the transition. Why the correct answer wins: Scheduling the cutover away from the known surge keeps the catch-up inside the window.

### Question 79 — B

Answer: Decommission the source after a parallel period. Retiring the source once the parallel period is complete releases the hardware. Keep the old system read-only for a defined period, then remove it. Local study-map skill 3.10 (Source Decommissioning), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 3 (migrate data solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Keep writing back to the original system so a rollback loses nothing. Why the correct answer wins: Retiring the source once the parallel period is complete releases the hardware.
- **B:** Correct. Keep the old system read-only for a defined period, then remove it. In this case: Retiring the source once the parallel period is complete releases the hardware.
- **C:** Incorrect for this question. Move clients to the new endpoint as the final cutover action. Why the correct answer wins: Retiring the source once the parallel period is complete releases the hardware.
- **D:** Incorrect for this question. Keep two databases current from application code during the transition. Why the correct answer wins: Retiring the source once the parallel period is complete releases the hardware.

### Question 80 — D

Answer: Confirm no client still uses the old endpoint. Connection and traffic evidence shows whether any client still uses the endpoint. Check the connection and traffic evidence before retiring an instance. Local study-map skill 3.10 (Source Decommissioning), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 3 (migrate data solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Keep the old system read-only for a defined period, then remove it. Why the correct answer wins: Connection and traffic evidence shows whether any client still uses the endpoint.
- **B:** Incorrect for this question. Prove the target holds the same rows as the source before cutover. Why the correct answer wins: Connection and traffic evidence shows whether any client still uses the endpoint.
- **C:** Incorrect for this question. Move clients to the new endpoint as the final cutover action. Why the correct answer wins: Connection and traffic evidence shows whether any client still uses the endpoint.
- **D:** Correct. Check the connection and traffic evidence before retiring an instance. In this case: Connection and traffic evidence shows whether any client still uses the endpoint.

### Question 81 — B

Answer: Provision the instance with a Terraform module. A declared module reproduces the estate exactly from one definition. Declare the database so the same definition creates every environment. Local study-map skill 4.1 (Provisioning Highly Available Instances), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 4 (deploy scalable and highly available databases in Google Cloud): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Run the new version beside the old one and move traffic when it is proven. Why the correct answer wins: A declared module reproduces the estate exactly from one definition.
- **B:** Correct. Declare the database so the same definition creates every environment. In this case: A declared module reproduces the estate exactly from one definition.
- **C:** Incorrect for this question. A copy of the current data created without touching the source. Why the correct answer wins: A declared module reproduces the estate exactly from one definition.
- **D:** Incorrect for this question. Create the resource interactively with no stored definition. Why the correct answer wins: A declared module reproduces the estate exactly from one definition.

### Question 82 — B

Answer: Apply the change through the infrastructure pipeline. Applying changes through the pipeline records review and change together. Send database changes through review and version control like any other code. Local study-map skill 4.1 (Provisioning Highly Available Instances), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 4 (deploy scalable and highly available databases in Google Cloud): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Create the resource interactively with no stored definition. Why the correct answer wins: Applying changes through the pipeline records review and change together.
- **B:** Correct. Send database changes through review and version control like any other code. In this case: Applying changes through the pipeline records review and change together.
- **C:** Incorrect for this question. A single view of health, security, and version posture across database instances. Why the correct answer wins: Applying changes through the pipeline records review and change together.
- **D:** Incorrect for this question. Rehearse the change against a copy before touching production. Why the correct answer wins: Applying changes through the pipeline records review and change together.

### Question 83 — A

Answer: Provision the instance with a Terraform module. A parameterised module applies one replica definition everywhere. Declare the database so the same definition creates every environment. Local study-map skill 4.1 (Provisioning Highly Available Instances), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 4 (deploy scalable and highly available databases in Google Cloud): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Correct. Declare the database so the same definition creates every environment. In this case: A parameterised module applies one replica definition everywhere.
- **B:** Incorrect for this question. Run the new version beside the old one and move traffic when it is proven. Why the correct answer wins: A parameterised module applies one replica definition everywhere.
- **C:** Incorrect for this question. A recovery point that makes the upgrade reversible in practice. Why the correct answer wins: A parameterised module applies one replica definition everywhere.
- **D:** Incorrect for this question. Create the resource interactively with no stored definition. Why the correct answer wins: A parameterised module applies one replica definition everywhere.

### Question 84 — B, C

Answers: Run a controlled failover test; Rehearse the promotion in a test project. A controlled zone failover tests the standby takeover, and a promotion drill tests the regional path. Trigger a switchover in a test window and observe how long writes are unavailable. Practise the failover that the runbook would perform for real. Local study-map skill 4.2 (Testing High Availability and Disaster Recovery), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 4 (deploy scalable and highly available databases in Google Cloud): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A recovery point that makes the upgrade reversible in practice. Why the correct answer wins: A controlled zone failover tests the standby takeover, and a promotion drill tests the regional path.
- **B:** Correct. Practise the failover that the runbook would perform for real. In this case: A controlled zone failover tests the standby takeover, and a promotion drill tests the regional path.
- **C:** Correct. Trigger a switchover in a test window and observe how long writes are unavailable. In this case: A controlled zone failover tests the standby takeover, and a promotion drill tests the regional path.
- **D:** Incorrect for this question. Block maintenance during a period when an interruption is unacceptable. Why the correct answer wins: A controlled zone failover tests the standby takeover, and a promotion drill tests the regional path.
- **E:** Incorrect for this question. Compare the signal after cutover against the pre-change baseline. Why the correct answer wins: A controlled zone failover tests the standby takeover, and a promotion drill tests the regional path.

### Question 85 — D

Answer: Run a controlled failover test. A controlled failover exercises the reconnect path in the application. Trigger a switchover in a test window and observe how long writes are unavailable. Local study-map skill 4.2 (Testing High Availability and Disaster Recovery), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 4 (deploy scalable and highly available databases in Google Cloud): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Rebuild the database in the surviving region from the latest backup. Why the correct answer wins: A controlled failover exercises the reconnect path in the application.
- **B:** Incorrect for this question. Compare the signal after cutover against the pre-change baseline. Why the correct answer wins: A controlled failover exercises the reconnect path in the application.
- **C:** Incorrect for this question. A recovery point that makes the upgrade reversible in practice. Why the correct answer wins: A controlled failover exercises the reconnect path in the application.
- **D:** Correct. Trigger a switchover in a test window and observe how long writes are unavailable. In this case: A controlled failover exercises the reconnect path in the application.

### Question 86 — B

Answer: Pre-size the promoted replica for the full load. The standby must be sized for the load it will inherit. Give the standby enough capacity to carry production alone. Local study-map skill 4.2 (Testing High Availability and Disaster Recovery), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 4 (deploy scalable and highly available databases in Google Cloud): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Keep spare capacity so a failover or a traffic spike does not saturate the instance. Why the correct answer wins: The standby must be sized for the load it will inherit.
- **B:** Correct. Give the standby enough capacity to carry production alone. In this case: The standby must be sized for the load it will inherit.
- **C:** Incorrect for this question. Rebuild the database in the surviving region from the latest backup. Why the correct answer wins: The standby must be sized for the load it will inherit.
- **D:** Incorrect for this question. Send reads to a copy so the primary keeps its capacity for writes. Why the correct answer wins: The standby must be sized for the load it will inherit.

### Question 87 — D

Answer: Choose a multi-region instance configuration. A multi-region configuration keeps quorum across regions. A topology that places replicas in separate regions for regional-failure tolerance. Local study-map skill 4.3 (Multi-Regional Replication Setup), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 4 (deploy scalable and highly available databases in Google Cloud): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Rebuild the database in the surviving region from the latest backup. Why the correct answer wins: A multi-region configuration keeps quorum across regions.
- **B:** Incorrect for this question. A primary and standby in two zones of one region with automatic failover. Why the correct answer wins: A multi-region configuration keeps quorum across regions.
- **C:** Incorrect for this question. A copy in a second region that serves reads and can be promoted. Why the correct answer wins: A multi-region configuration keeps quorum across regions.
- **D:** Correct. A topology that places replicas in separate regions for regional-failure tolerance. In this case: A multi-region configuration keeps quorum across regions.

### Question 88 — C

Answer: Add a secondary cluster in the second region. A secondary cluster serves reads and can be promoted. An AlloyDB cross-region copy that can be promoted to a primary cluster. Local study-map skill 4.3 (Multi-Regional Replication Setup), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 4 (deploy scalable and highly available databases in Google Cloud): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Rebuild the database in the surviving region from the latest backup. Why the correct answer wins: A secondary cluster serves reads and can be promoted.
- **B:** Incorrect for this question. Grow the AlloyDB read pool that serves read-only connections. Why the correct answer wins: A secondary cluster serves reads and can be promoted.
- **C:** Correct. An AlloyDB cross-region copy that can be promoted to a primary cluster. In this case: A secondary cluster serves reads and can be promoted.
- **D:** Incorrect for this question. One instance in one zone with no standby, so a zone failure stops writes. Why the correct answer wins: A secondary cluster serves reads and can be promoted.

### Question 89 — A

Answer: Route the app profile across both clusters. Multi-cluster routing fails over for the client automatically. A Bigtable app profile that fails over between clusters without a client change. Local study-map skill 4.3 (Multi-Regional Replication Setup), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 4 (deploy scalable and highly available databases in Google Cloud): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Correct. A Bigtable app profile that fails over between clusters without a client change. In this case: Multi-cluster routing fails over for the client automatically.
- **B:** Incorrect for this question. An AlloyDB cross-region copy that can be promoted to a primary cluster. Why the correct answer wins: Multi-cluster routing fails over for the client automatically.
- **C:** Incorrect for this question. A copy in a second region that serves reads and can be promoted. Why the correct answer wins: Multi-cluster routing fails over for the client automatically.
- **D:** Incorrect for this question. A Bigtable app profile that keeps a workload on one cluster for predictable latency. Why the correct answer wins: Multi-cluster routing fails over for the client automatically.

### Question 90 — B

Answer: Add nodes to the read pool. Adding read-pool nodes adds capacity where the load is concentrated. Grow the AlloyDB read pool that serves read-only connections. Local study-map skill 4.4 (Read Replicas and Read Pools), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 4 (deploy scalable and highly available databases in Google Cloud): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Absorb repeated reads in memory so the database sees fewer of them. Why the correct answer wins: Adding read-pool nodes adds capacity where the load is concentrated.
- **B:** Correct. Grow the AlloyDB read pool that serves read-only connections. In this case: Adding read-pool nodes adds capacity where the load is concentrated.
- **C:** Incorrect for this question. Separate analytical reads from the write path. Why the correct answer wins: Adding read-pool nodes adds capacity where the load is concentrated.
- **D:** Incorrect for this question. Move the instance to a larger shape so more vCPU and memory serve the same data. Why the correct answer wins: Adding read-pool nodes adds capacity where the load is concentrated.

### Question 91 — C

Answer: Add a read replica for the read traffic. A read replica provides the extra read capacity the workload needs. Send reads to a copy so the primary keeps its capacity for writes. Local study-map skill 4.4 (Read Replicas and Read Pools), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 4 (deploy scalable and highly available databases in Google Cloud): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Move the instance to a larger shape so more vCPU and memory serve the same data. Why the correct answer wins: A read replica provides the extra read capacity the workload needs.
- **B:** Incorrect for this question. Split rows by a key so each instance owns a subset of the workload. Why the correct answer wins: A read replica provides the extra read capacity the workload needs.
- **C:** Correct. Send reads to a copy so the primary keeps its capacity for writes. In this case: A read replica provides the extra read capacity the workload needs.
- **D:** Incorrect for this question. Grow the AlloyDB read pool that serves read-only connections. Why the correct answer wins: A read replica provides the extra read capacity the workload needs.

### Question 92 — C, D

Answers: Apply the change through the infrastructure pipeline; Provision the instance with a Terraform module. Declaring the database in a module makes it repeatable, and applying it through the pipeline adds review and validation. Send database changes through review and version control like any other code. Declare the database so the same definition creates every environment. Local study-map skill 4.5 (Automating Database Provisioning), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 4 (deploy scalable and highly available databases in Google Cloud): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Create the resource interactively with no stored definition. Why the correct answer wins: Declaring the database in a module makes it repeatable, and applying it through the pipeline adds review and validation.
- **B:** Incorrect for this question. Rehearse the change against a copy before touching production. Why the correct answer wins: Declaring the database in a module makes it repeatable, and applying it through the pipeline adds review and validation.
- **C:** Correct. Send database changes through review and version control like any other code. In this case: Declaring the database in a module makes it repeatable, and applying it through the pipeline adds review and validation.
- **D:** Correct. Declare the database so the same definition creates every environment. In this case: Declaring the database in a module makes it repeatable, and applying it through the pipeline adds review and validation.
- **E:** Incorrect for this question. A recovery point that makes the upgrade reversible in practice. Why the correct answer wins: Declaring the database in a module makes it repeatable, and applying it through the pipeline adds review and validation.

### Question 93 — D

Answer: Provision the instance with a Terraform module. A parameterised module creates each instance from one definition. Declare the database so the same definition creates every environment. Local study-map skill 4.5 (Automating Database Provisioning), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 4 (deploy scalable and highly available databases in Google Cloud): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Create the resource interactively with no stored definition. Why the correct answer wins: A parameterised module creates each instance from one definition.
- **B:** Incorrect for this question. A single view of health, security, and version posture across database instances. Why the correct answer wins: A parameterised module creates each instance from one definition.
- **C:** Incorrect for this question. A copy of the current data created without touching the source. Why the correct answer wins: A parameterised module creates each instance from one definition.
- **D:** Correct. Declare the database so the same definition creates every environment. In this case: A parameterised module creates each instance from one definition.

### Question 94 — C

Answer: Create an alerting policy on the metric. An alerting policy on the failover signal notifies the team automatically. A condition that pages a human when the threshold is crossed. Local study-map skill 4.6 (Monitoring Highly Available Databases), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 4 (deploy scalable and highly available databases in Google Cloud): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Read the instance-level signals before attributing the symptom to the query. Why the correct answer wins: An alerting policy on the failover signal notifies the team automatically.
- **B:** Incorrect for this question. A per-query view of latency, load, and wait events on the instance. Why the correct answer wins: An alerting policy on the failover signal notifies the team automatically.
- **C:** Correct. A condition that pages a human when the threshold is crossed. In this case: An alerting policy on the failover signal notifies the team automatically.
- **D:** Incorrect for this question. A single view of health, security, and version posture across database instances. Why the correct answer wins: An alerting policy on the failover signal notifies the team automatically.

### Question 95 — C

Answer: Review the fleet in Database Center. The fleet view aggregates posture and health across instances. A single view of health, security, and version posture across database instances. Local study-map skill 4.6 (Monitoring Highly Available Databases), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 4 (deploy scalable and highly available databases in Google Cloud): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. The engine log of statements that exceeded the long-query threshold. Why the correct answer wins: The fleet view aggregates posture and health across instances.
- **B:** Incorrect for this question. A per-query view of latency, load, and wait events on the instance. Why the correct answer wins: The fleet view aggregates posture and health across instances.
- **C:** Correct. A single view of health, security, and version posture across database instances. In this case: The fleet view aggregates posture and health across instances.
- **D:** Incorrect for this question. Read the instance-level signals before attributing the symptom to the query. Why the correct answer wins: The fleet view aggregates posture and health across instances.

### Question 96 — A

Answer: Promote the cross-region replica during the outage. Promotion uses the current copy and restores service quickly. Turn the replica into an independent primary so the application can resume writes. Local study-map skill 4.7 (Regional Failover Mechanics), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 4 (deploy scalable and highly available databases in Google Cloud): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Correct. Turn the replica into an independent primary so the application can resume writes. In this case: Promotion uses the current copy and restores service quickly.
- **B:** Incorrect for this question. A point-in-time restore that discards the later writes on the same instance. Why the correct answer wins: Promotion uses the current copy and restores service quickly.
- **C:** Incorrect for this question. Rebuild the database in the surviving region from the latest backup. Why the correct answer wins: Promotion uses the current copy and restores service quickly.
- **D:** Incorrect for this question. Trigger a switchover in a test window and observe how long writes are unavailable. Why the correct answer wins: Promotion uses the current copy and restores service quickly.

### Question 97 — C

Answer: Fence the old primary before promotion. The old primary must be prevented from accepting writes so only one primary exists. Stop the former primary from accepting writes so two instances cannot both claim the role. Local study-map skill 4.7 (Regional Failover Mechanics), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 4 (deploy scalable and highly available databases in Google Cloud): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Stop application writes so the last increment can be applied cleanly. Why the correct answer wins: The old primary must be prevented from accepting writes so only one primary exists.
- **B:** Incorrect for this question. A rehearsed sequence with a named decision point and a way back. Why the correct answer wins: The old primary must be prevented from accepting writes so only one primary exists.
- **C:** Correct. Stop the former primary from accepting writes so two instances cannot both claim the role. In this case: The old primary must be prevented from accepting writes so only one primary exists.
- **D:** Incorrect for this question. Keep writing back to the original system so a rollback loses nothing. Why the correct answer wins: The old primary must be prevented from accepting writes so only one primary exists.

### Question 98 — D

Answer: Use the language connector with IAM credentials. The language connector resolves the instance on each connection. A client library that resolves the instance and authorizes the connection with IAM. Local study-map skill 4.8 (Connection Routing and Load Balancing), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 4 (deploy scalable and highly available databases in Google Cloud): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A pooler that multiplexes many application connections onto few database sessions. Why the correct answer wins: The language connector resolves the instance on each connection.
- **B:** Incorrect for this question. Move clients to the new endpoint as the final cutover action. Why the correct answer wins: The language connector resolves the instance on each connection.
- **C:** Incorrect for this question. A public-IP allowlist that admits the caller range. Why the correct answer wins: The language connector resolves the instance on each connection.
- **D:** Correct. A client library that resolves the instance and authorizes the connection with IAM. In this case: The language connector resolves the instance on each connection.

### Question 99 — A

Answer: Reserve headroom above the measured peak. The standby must carry the peak plus the load it inherits, so headroom above that peak is the basis. Keep spare capacity so a failover or a traffic spike does not saturate the instance. Local study-map skill 4.9 (Failover Capacity Headroom), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 4 (deploy scalable and highly available databases in Google Cloud): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Correct. Keep spare capacity so a failover or a traffic spike does not saturate the instance. In this case: The standby must carry the peak plus the load it inherits, so headroom above that peak is the basis.
- **B:** Incorrect for this question. Shrink an instance whose peak fits a smaller shape. Why the correct answer wins: The standby must carry the peak plus the load it inherits, so headroom above that peak is the basis.
- **C:** Incorrect for this question. Match capacity to the daily traffic shape. Why the correct answer wins: The standby must carry the peak plus the load it inherits, so headroom above that peak is the basis.
- **D:** Incorrect for this question. Send reads to a copy so the primary keeps its capacity for writes. Why the correct answer wins: The standby must carry the peak plus the load it inherits, so headroom above that peak is the basis.

### Question 100 — A

Answer: Pre-size the promoted replica for the full load. The standby must be sized in advance for the load it will inherit. Give the standby enough capacity to carry production alone. Local study-map skill 4.9 (Failover Capacity Headroom), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 4 (deploy scalable and highly available databases in Google Cloud): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Correct. Give the standby enough capacity to carry production alone. In this case: The standby must be sized in advance for the load it will inherit.
- **B:** Incorrect for this question. Match capacity to the daily traffic shape. Why the correct answer wins: The standby must be sized in advance for the load it will inherit.
- **C:** Incorrect for this question. Keep spare capacity so a failover or a traffic spike does not saturate the instance. Why the correct answer wins: The standby must be sized in advance for the load it will inherit.
- **D:** Incorrect for this question. Send reads to a copy so the primary keeps its capacity for writes. Why the correct answer wins: The standby must be sized in advance for the load it will inherit.
