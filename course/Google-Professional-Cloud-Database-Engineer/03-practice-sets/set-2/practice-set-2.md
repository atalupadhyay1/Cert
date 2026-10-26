# Google Cloud Professional Cloud Database Engineer — Full-Length Mock Exam 2

Professional Cloud Database Engineer · 100 questions · expanded practice bank · passing score not published

Blueprint-weighted mock exam. Item mix: 84 multiple-choice and 16 multiple-select items (the selection count is stated in each multi-select stem). The live exam publishes 50-60 multiple-choice and multiple-select questions and has no case-study component, so this set is larger on purpose and no case-study item is reproduced. The live paper allows two hours for 50-60 items, so this 100-item set is a slower-per-item rehearsal: about 72 seconds per item here against roughly 120-144 seconds live. Use it to build a habit of finishing with time to review. See the README for the exact fidelity boundary.

Original educational content, not actual, recalled, or copied Google exam items.

## Questions

---

## Domain 1 — Design Innovative, Scalable, and Highly Available Cloud Database Solutions (Sizing, Availability Design, and Database Selection)

### 1. A media company's Cloud SQL for MySQL primary runs at twelve percent CPU and fifteen percent memory around the clock, sized for a launch that never happened. Which action cuts the bill without risking the current load?

- A. Add a read replica for the read traffic
- B. Reduce the machine type to match observed use
- C. Commit to the steady baseline capacity
- D. Reserve headroom above the measured peak

### 2. A team must size a database for a product launching in three months, and it has a working prototype but no production telemetry at all. What should the team do?

- A. Reserve headroom above the measured peak
- B. Load-test the workload to derive the size
- C. Commit to the steady baseline capacity
- D. Size the instance from the observed peak metrics

### 3. A Cloud SQL warehouse application shows high IOPS waits and memory pressure during the nightly batch. Which two changes each address one bottleneck? Select two.

- A. Move the data to HDD storage
- B. Increase the disk size to raise throughput
- C. Put a session pooler in front of the instance
- D. Increase the machine type of the instance
- E. Add a read replica for the read traffic

### 4. A team provisioning a Cloud SQL instance knows the dataset starts at four hundred gigabytes and grows twenty gigabytes a month for three years. How should storage be chosen?

- A. Archive closed rows to cheaper storage
- B. Increase the disk size to raise throughput
- C. Add a lifecycle rule to the export bucket
- D. Let the disk grow automatically

### 5. A Bigtable cluster runs at ninety-five percent CPU under simple key lookups, and the tablet count is rising with the data volume. What should the team do?

- A. Set the garbage-collection policy on the column family
- B. Change the row-key design
- C. Move the data to SSD storage
- D. Add nodes to the Bigtable cluster

### 6. A Spanner instance reports sustained high CPU on three nodes, growth is steady, and there are no traffic spikes to absorb. Which change fits?

- A. Add nodes to the read pool
- B. Add processing units to the Spanner instance
- C. Add nodes to the Bigtable cluster
- D. Increase the machine type of the instance

### 7. A retail platform wants zone-failure protection now and a regional recovery path next quarter. Which two components provide both? Select two.

- A. Add a cross-region read replica
- B. Run a single zonal instance
- C. Enable regional high availability with a standby zone
- D. Restore the backup into the second region
- E. Choose a multi-region instance configuration

### 8. A development database can be rebuilt from seed data in ten minutes, and the team wants the cheapest topology that still meets the test schedule. Which choice fits?

- A. Run a single zonal instance
- B. Add a cross-region read replica
- C. Choose a multi-region instance configuration
- D. Enable regional high availability with a standby zone

### 9. An AlloyDB deployment must survive losing its region and must serve analytics reads from the second region continuously. Which topology fits?

- A. Run a single zonal instance
- B. Add a secondary cluster in the second region
- C. Add nodes to the read pool
- D. Restore the backup into the second region

### 10. A global SaaS must decide when database maintenance may interrupt service. Which two controls shape that timing? Select two.

- A. Set a deny maintenance period over the peak event
- B. Schedule the maintenance window in the low-traffic period
- C. Take a backup before the upgrade
- D. Run a controlled failover test
- E. Restart the instance in the window

### 11. Patching interrupted a customer demonstration last quarter, and the team must protect that same week this year without stopping patching altogether. What should they configure?

- A. Set a deny maintenance period over the peak event
- B. Perform an in-place major version upgrade
- C. Run a controlled failover test
- D. Schedule the maintenance window in the low-traffic period

### 12. An on-premises Java service reaches Cloud SQL through a static allowlisted public address, and security wants no public surface and no static IP management. Which change fits?

- A. Add the client range to authorized networks
- B. Publish the instance behind Private Service Connect
- C. Connect through the Cloud SQL Auth Proxy
- D. Use the public IP with enforced SSL

### 13. Two hundred Cloud Run services must reach Cloud SQL without a VPC connector and without certificate files in each container. What should the team use?

- A. Use the language connector with IAM credentials
- B. Publish the instance behind Private Service Connect
- C. Connect over private IP inside the VPC
- D. Add the client range to authorized networks

### 14. A security team must control and audit the key that protects a new Firestore database, and must be able to disable it independently. Which control fits?

- A. Route the audit logs to a locked log bucket
- B. Add the projects to a VPC Service Controls perimeter
- C. Encrypt with a customer-managed key in Cloud KMS
- D. Rely on Google-managed encryption keys

### 15. A startup wants encryption at rest for a Spanner database with no key-management process to operate. Which choice fits?

- A. Rotate the customer-managed key on a schedule
- B. Add the projects to a VPC Service Controls perimeter
- C. Rely on Google-managed encryption keys
- D. Encrypt with a customer-managed key in Cloud KMS

### 16. A nightly batch leaves sessions open after each job, so the instance refuses connections before the run finishes. Which two changes reduce that pressure? Select two.

- A. Raise the max_connections database flag
- B. Increase the machine tier to allow more connections
- C. Increase the machine type of the instance
- D. Put a session pooler in front of the instance
- E. Fix the connection leak in the application

### 17. An instance returns too-many-connections while memory sits at forty percent, and every session is legitimately in use at peak. Which change fits?

- A. Increase the machine tier to allow more connections
- B. Fix the connection leak in the application
- C. Put a session pooler in front of the instance
- D. Raise the max_connections database flag

### 18. An investigator must identify which identity changed an instance's configuration flags last Tuesday. Which log source answers that?

- A. Enable Data Access audit logs
- B. Review the fleet in Database Center
- C. Rely on Admin Activity audit logs
- D. Route the audit logs to a locked log bucket

### 19. A financial audit requires that database configuration-change evidence survive for three years even if someone empties the project's log bucket. What should the team configure?

- A. Build a log-based metric from the error entries
- B. Enable Data Access audit logs
- C. Rely on Admin Activity audit logs
- D. Route the audit logs to a locked log bucket

### 20. A workload runs an engine whose vendor offers a managed service through Google Cloud Marketplace, and the company already holds a support contract with that vendor. Which deployment fits?

- A. Run the database on bare metal solution
- B. Use a partner-managed database offering
- C. Run the database on Compute Engine yourself
- D. Use Cloud SQL for the relational workload

### 21. An application needs a managed PostgreSQL-compatible service but depends on an extension that the standard managed offering does not support. Which Google Cloud option should the team evaluate?

- A. Use Spanner for the globally distributed relational workload
- B. Use Cloud SQL for the relational workload
- C. Run the database on Compute Engine yourself
- D. Use AlloyDB for the demanding relational workload

### 22. A fraud-detection service needs multi-row ACID transactions over two terabytes with predictable single-region latency and minimal operations. Which database fits?

- A. Use Firestore for the document workload
- B. Use Bigtable for the high-throughput wide-column workload
- C. Use Spanner for the globally distributed relational workload
- D. Use Cloud SQL for the relational workload

### 23. A user-profile store needs flexible per-document schema, mobile SDKs with offline support, and replication handled by the service. Which database fits?

- A. Use Bigtable for the high-throughput wide-column workload
- B. Use Memorystore as the caching tier
- C. Use Firestore for the document workload
- D. Use Cloud SQL for the relational workload

### 24. A leaderboard needs sub-millisecond reads for ten million users, and its contents can be rebuilt from an event log if lost. Which choice fits?

- A. Use Memorystore as the caching tier
- B. Use Bigtable for the high-throughput wide-column workload
- C. Use Firestore for the document workload
- D. Use Cloud SQL for the relational workload

### 25. A retrieval service must search fifty million embedding chunks with metadata filters and stay inside one PostgreSQL-compatible database. Which approach fits?

- A. Enable the vector extension on PostgreSQL
- B. Use AlloyDB vector search with a ScaNN index
- C. Export the table into BigQuery
- D. Query the source through BigQuery federated queries

### 26. A startup with five million embeddings and a tight budget wants semantic search added to its existing Cloud SQL for PostgreSQL application. Which approach fits?

- A. Create a vector index for the embeddings
- B. Use AlloyDB vector search with a ScaNN index
- C. Cache the hot read path in Memorystore
- D. Enable the vector extension on PostgreSQL

### 27. A finance review must cut database spend by twenty percent without changing availability or latency. Which two actions meet that constraint? Select two.

- A. Commit to the steady baseline capacity
- B. Stop or delete the idle instance
- C. Let the disk grow automatically
- D. Rely on sustained-use discounts
- E. Reduce the machine type to match observed use

### 28. A Cloud SQL instance supports quarter-end reporting, sits idle for eleven weeks at a time, and is billed continuously. What should the team do?

- A. Commit to the steady baseline capacity
- B. Reduce the machine type to match observed use
- C. Stop or delete the idle instance
- D. Reserve capacity for the peak season

### 29. Two candidate target engines are both acceptable to the business, and the application uses a mixture of portable SQL and engine-specific features. How should the team decide?

- A. Keep the current engine and version
- B. Write to both systems from the application
- C. Choose the target engine with the cheapest conversion
- D. Use Database Migration Service with schema conversion

### 30. A public-sector agency must keep citizen data inside its country and must ensure that only the payments team can read the payments table. Which two controls are needed? Select two.

- A. Limit the user to the required schema
- B. Add the projects to a VPC Service Controls perimeter
- C. Place the instance in the required region
- D. Rely on Google-managed encryption keys
- E. Cache the hot read path in Memorystore

### 31. A team must stop database data from being copied into consumer projects outside the approved set, even by an authorized engineer. Which control fits?

- A. Add the projects to a VPC Service Controls perimeter
- B. Query the source through BigQuery federated queries
- C. Export the table into BigQuery
- D. Stream changes into BigQuery

### 32. A ten-year outsourcing contract keeps an Oracle system on-premises, while new applications move to Cloud SQL and must query some of its tables. Which approach fits?

- A. Query the source through BigQuery federated queries
- B. Export the table into BigQuery
- C. Keep part of the estate on-premises with a hybrid link
- D. Decommission the source after a parallel period

---

## Domain 2 — Manage a Solution That Can Span Multiple Database Technologies (Operations, Access, Backup, and Performance)

### 33. An analyst must query one table read-only with no database password, and access must end when the analyst leaves the team. Select two.

- A. Keep a database password in the connection string
- B. Grant the basic editor role
- C. Share one application database user
- D. Enable IAM database authentication
- E. Bind access to a Google group

### 34. An application needs to read one schema and write another inside the same database, and the reviewer objects to a single grant covering the whole instance. What should the team request?

- A. Grant a custom role limited to the needed permissions
- B. Grant the basic editor role
- C. Create one database user per person
- D. Limit the user to the required schema

### 35. A policy requires the application's database credential to be rotated every ninety days without redeploying code or storing a secret. Which approach fits?

- A. Keep a database password in the connection string
- B. Enable IAM database authentication
- C. Create one database user per person
- D. Share one application database user

### 36. A read-only reporting query on Cloud SQL takes ninety seconds and the team must understand why before changing anything. Which two diagnostic steps come first? Select two.

- A. Add the index the slow query needs
- B. Read the query plan for the statement
- C. Refresh the table statistics
- D. Use Query Insights to find the heavy statements
- E. Cache the hot read path in Memorystore

### 37. A join filters on a date range and sorts by timestamp, and the plan shows a scan of sixty million rows followed by a sort. What should the team do?

- A. Raise the per-operation memory flag
- B. Refresh the table statistics
- C. Partition the large table
- D. Add the index the slow query needs

### 38. Two application threads update the same account rows in opposite orders, and deadlock victims appear whenever load rises. What should the team inspect first?

- A. Add the index the slow query needs
- B. Inspect lock waits and blocking sessions
- C. Terminate the session that holds the lock
- D. Batch the writes into fewer round trips

### 39. A schema change has been waiting twenty-five minutes because a reporting transaction opened earlier still holds its locks. What should the team do to unblock the change?

- A. Terminate the session that holds the lock
- B. Inspect lock waits and blocking sessions
- C. Send reporting queries to the read replica
- D. Refresh the table statistics

### 40. A team must decide whether a slow database is short of CPU or waiting on storage during a controlled load test. Which view answers that?

- A. Review the fleet in Database Center
- B. Watch CPU, memory, disk, and IOPS together
- C. Use Query Insights to find the heavy statements
- D. Read the slow query log

### 41. A database engineer wants per-statement wait events to see whether time goes to locks, IO, or CPU. Which tool provides them?

- A. Build a log-based metric from the error entries
- B. Read the slow query log
- C. Watch CPU, memory, disk, and IOPS together
- D. Use Query Insights to find the heavy statements

### 42. Sixty export jobs must run inside a two-hour month-end window and all of them genuinely need to run concurrently, but the project refuses the calls. What should the team do?

- A. Request a quota increase for the project
- B. Export the table to CSV in Cloud Storage
- C. Move the job outside the contention window
- D. Retry the failed operation with exponential backoff

### 43. A team is woken nightly by a CPU alert caused by a harmless batch job, while a lagging replica goes unnoticed. Which two changes fix the paging? Select two.

- A. Alert on replication lag
- B. Watch CPU, memory, disk, and IOPS together
- C. Build a log-based metric from the error entries
- D. Create an alerting policy on the metric
- E. Alert on the database error rate

### 44. Repeated deadlock messages appear in the database log but no metric counts them, so the trend is invisible. What should the team create?

- A. Read the slow query log
- B. Build a log-based metric from the error entries
- C. Alert when the instance is unreachable
- D. Route the audit logs to a locked log bucket

### 45. A team must retain thirty-five days of recovery points and must be able to restore one table without disturbing the instance. Which two capabilities does it need? Select two.

- A. Enable point-in-time recovery
- B. Take an on-demand backup before the change
- C. Clone the instance for the test
- D. Export a logical dump to Cloud Storage
- E. Enable automated backups with a retention window

### 46. Compliance requires four hundred days of recoverable backups, and the managed retention window currently stops well short of that. What should the team change?

- A. Take an on-demand backup before the change
- B. Enable point-in-time recovery
- C. Extend the backup retention window
- D. Add a lifecycle rule to the export bucket

### 47. A team must load a fifty-gigabyte dump file from Cloud Storage into a Cloud SQL for PostgreSQL instance once. What should they use?

- A. Import the dump into the target instance
- B. Stream changes into BigQuery
- C. Query the source through BigQuery federated queries
- D. Export a logical dump to Cloud Storage

### 48. A service must be able to return to a five-minute-old state after a bad deployment, with no standby capacity available. Which capability provides that?

- A. Enable point-in-time recovery
- B. Enable automated backups with a retention window
- C. Run a controlled failover test
- D. Export a logical dump to Cloud Storage

### 49. A two-terabyte instance needs an eight-hour recovery time objective, but a full restore currently takes six hours before any validation begins. Which change meets the objective?

- A. Restore to the timestamp before the bad change
- B. Take a backup before the upgrade
- C. Extend the backup retention window
- D. Add a cross-region read replica

### 50. Analysts must keep thirteen months of Bigtable history, but each row's superseded versions must disappear after thirty days. What should the team configure?

- A. Set the garbage-collection policy on the column family
- B. Apply a row-level retention policy
- C. Archive closed rows to cheaper storage
- D. Set a time-to-live policy on the collection

### 51. A Spanner workload is read-dominated, and the team wants nearby read capacity without changing where writes are accepted. What should they add?

- A. Add a read-only region to the configuration
- B. Add a cross-region read replica
- C. Add processing units to the Spanner instance
- D. Add nodes to the read pool

### 52. A MySQL primary runs at ninety percent CPU because of reporting queries, and the application cannot change its read routing this quarter. Which action fits the constraint?

- A. Add a read replica for the read traffic
- B. Cache the hot read path in Memorystore
- C. Increase the machine type of the instance
- D. Send reporting queries to the read replica

### 53. A Bigtable table is replicated across two regions, and clients must fail over to the surviving cluster without a configuration change. Which setting fits?

- A. Add a secondary cluster in the second region
- B. Route the app profile across both clusters
- C. Add a cross-region read replica
- D. Pin the app profile to one cluster

### 54. A monthly report joins twelve tables and re-scans two hundred gigabytes five times a day on the production instance. What should the team do?

- A. Export the table into BigQuery
- B. Partition the large table
- C. Raise the per-operation memory flag
- D. Cache the hot read path in Memorystore

### 55. Fragmented indexes on a Cloud SQL for SQL Server instance must be rebuilt monthly with nobody present. What should the team configure?

- A. Run the task on a managed schedule
- B. Run a controlled failover test
- C. Provision the instance once by hand
- D. Take an on-demand backup before the change

### 56. Nightly exports accumulate in a bucket, and only the last fourteen files are ever restored. What should the team add?

- A. Take an on-demand backup before the change
- B. Export a logical dump to Cloud Storage
- C. Add a lifecycle rule to the export bucket
- D. Run the task on a managed schedule

### 57. A team must show whether the database met the 99.95 percent availability it publishes to its own customers each month. Which practice answers that?

- A. Track the availability signal against the agreed objective
- B. Create an alerting policy on the metric
- C. Review the fleet in Database Center
- D. Watch CPU, memory, disk, and IOPS together

---

## Domain 3 — Migrate Data Solutions (Migration Strategy, Conversion, and Cutover)

### 58. A five-hundred-gigabyte PostgreSQL database must move with under ten minutes of downtime and must allow a same-day rollback. Select two.

- A. Write to both systems from the application
- B. Set up reverse replication to the source
- C. Dump, restore, then replay the changes
- D. Use Database Migration Service for the same engine
- E. Accept a scheduled extended outage

### 59. Sixty small tenant databases must each migrate inside a thirty-minute window, and weekend outages are acceptable. Which approach fits?

- A. Write to both systems from the application
- B. Use Database Migration Service for the same engine
- C. Dump, restore, then replay the changes
- D. Freeze writes during the cutover

### 60. A cutover attempt fails at 02:00 with no engineer awake to decide what to do next. What should have existed beforehand?

- A. Follow a cutover runbook with a rollback step
- B. Write to both systems from the application
- C. Accept a scheduled extended outage
- D. Freeze writes during the cutover

### 61. A SQL Server 2019 database must move to Cloud SQL for SQL Server while applications keep writing. Select two.

- A. Build the schema in a conversion workspace
- B. Use Database Migration Service for the same engine
- C. Apply the captured change backlog before cutover
- D. Dump, restore, then replay the changes
- E. Write to both systems from the application

### 62. A team must replicate MySQL changes into BigQuery and Cloud Storage at the same time, with no database being retired. Which tool fits?

- A. Export a logical dump to Cloud Storage
- B. Stream changes with Datastream
- C. Export the table into BigQuery
- D. Use Database Migration Service for the same engine

### 63. A team wants a managed path from Oracle to PostgreSQL with the least custom tooling and a repeatable cutover. Which service fits?

- A. Dump, restore, then replay the changes
- B. Use Database Migration Service with schema conversion
- C. Use Database Migration Service for the same engine
- D. Write to both systems from the application

### 64. An Oracle package uses autonomous transactions that the PostgreSQL target does not support, and the behaviour must be preserved. What must the team do?

- A. Reset the sequences after the bulk load
- B. Build the schema in a conversion workspace
- C. Write to both systems from the application
- D. Rewrite the stored procedures and DML by hand

### 65. Converted DDL creates child tables before their parents, so every foreign key fails during the load. Where should the team fix this?

- A. Rewrite the stored procedures and DML by hand
- B. Build the schema in a conversion workspace
- C. Reconcile row counts and checksums
- D. Repoint the connection string at the target

### 66. A reporting job uses Oracle outer-join syntax that the PostgreSQL target rejects outright. What has to happen?

- A. Write to both systems from the application
- B. Reset the sequences after the bulk load
- C. Rewrite the stored procedures and DML by hand
- D. Replay read traffic against the target

### 67. Before cutover, a team wants two hundred application queries compared row by row between the source and the target. Which activity fits?

- A. Replay read traffic against the target
- B. Repoint the connection string at the target
- C. Rewrite the stored procedures and DML by hand
- D. Reconcile row counts and checksums

### 68. A four-terabyte load runs for fourteen hours while the source keeps taking writes. How should the target stay current during that load?

- A. Use the engine native logical replication
- B. Accept a scheduled extended outage
- C. Export a logical dump to Cloud Storage
- D. Write to both systems from the application

### 69. A team must confirm that a fourteen-hour load plus its catch-up will fit inside a thirty-minute cutover. What should they measure?

- A. Measure the catch-up rate before choosing the window
- B. Freeze writes during the cutover
- C. Reconcile row counts and checksums
- D. Apply the captured change backlog before cutover

### 70. A validation plan must catch both missing rows and a text column truncated during conversion. Which two checks should it include? Select two.

- A. Replay read traffic against the target
- B. Reconcile row counts and checksums
- C. Repoint the connection string at the target
- D. Reset the sequences after the bulk load
- E. Follow a cutover runbook with a rollback step

### 71. A team wants validation to run automatically after every rehearsal instead of being repeated by hand. What should they add?

- A. Reconcile row counts and checksums
- B. Repoint the connection string at the target
- C. Replay read traffic against the target
- D. Run the task on a managed schedule

### 72. At minute twenty of a thirty-minute window the replica is still twelve minutes behind, and the team must decide now. What should govern the decision?

- A. Freeze writes during the cutover
- B. Write to both systems from the application
- C. Repoint the connection string at the target
- D. Follow a cutover runbook with a rollback step

### 73. A batch job ignores the maintenance flag and keeps inserting rows during the final increment. What must the team ensure?

- A. Accept a scheduled extended outage
- B. Repoint the connection string at the target
- C. Freeze writes during the cutover
- D. Set up reverse replication to the source

### 74. Clients still resolve the old database hostname because the record has a three-hundred-second cache lifetime. What completes the cutover?

- A. Freeze writes during the cutover
- B. Use the language connector with IAM credentials
- C. Repoint the connection string at the target
- D. Follow a cutover runbook with a rollback step

### 75. Writes made on the new database after cutover must appear on the on-premises source for a month. What must be configured?

- A. Write to both systems from the application
- B. Repoint the connection string at the target
- C. Set up reverse replication to the source
- D. Decommission the source after a parallel period

### 76. Leadership asks when the old database can be shut down after a successful cutover. What should the team define?

- A. Decommission the source after a parallel period
- B. Repoint the connection string at the target
- C. Confirm no client still uses the old endpoint
- D. Set up reverse replication to the source

### 77. A six-terabyte warehouse migration must cut downtime from two days to minutes. Select two.

- A. Use the engine native logical replication
- B. Write to both systems from the application
- C. Apply the captured change backlog before cutover
- D. Accept a scheduled extended outage
- E. Dump, restore, then replay the changes

### 78. A team wants to avoid repeating a fourteen-hour load if the cutover has to be abandoned. What should stay in place?

- A. Apply the captured change backlog before cutover
- B. Freeze writes during the cutover
- C. Export a logical dump to Cloud Storage
- D. Set up reverse replication to the source

### 79. A source must be retired, but eleven years of history must remain queryable by auditors. What should the team do before removal?

- A. Keep part of the estate on-premises with a hybrid link
- B. Decommission the source after a parallel period
- C. Export the table into BigQuery
- D. Set up reverse replication to the source

### 80. Before deleting the old instance, a team must be sure nothing still connects to it. What should they check?

- A. Reconcile row counts and checksums
- B. Repoint the connection string at the target
- C. Confirm no client still uses the old endpoint
- D. Decommission the source after a parallel period

---

## Domain 4 — Deploy Scalable and Highly Available Databases in Google Cloud (Deployment, High Availability, and Disaster Recovery)

### 81. A twelve-instance estate must be recreated in a new region after a disaster with exactly the same settings. What makes that practical?

- A. Restore the backup into the second region
- B. Clone the instance for the test
- C. Provision the instance once by hand
- D. Provision the instance with a Terraform module

### 82. Production and staging Cloud SQL flags diverged because both were edited by hand last quarter. What should the team adopt?

- A. Review the fleet in Database Center
- B. Apply the change through the infrastructure pipeline
- C. Test the upgrade on a clone first
- D. Provision the instance once by hand

### 83. A team must add a read replica to thirty instances this week with identical settings and no per-instance work. What should they use?

- A. Provision the instance with a Terraform module
- B. Provision the instance once by hand
- C. Stand up a parallel instance and switch over
- D. Take a backup before the upgrade

### 84. A drill must show that a promoted cross-region replica serves writes within the stated recovery time. Which exercise proves it?

- A. Watch the error rate after the change
- B. Run a controlled failover test
- C. Take a backup before the upgrade
- D. Rehearse the promotion in a test project

### 85. A team must prove that applications reconnect after a failover without a human restarting pods. What should they run?

- A. Alert when the instance is unreachable
- B. Run a controlled failover test
- C. Take a backup before the upgrade
- D. Watch the error rate after the change

### 86. A disaster plan has never been rehearsed against a full region loss, and the team wants to test the restore path safely. What should they do?

- A. Rehearse the promotion in a test project
- B. Take a backup before the upgrade
- C. Run a controlled failover test
- D. Restore the backup into the second region

### 87. A Spanner database must keep strongly consistent writes while serving reads from two additional regions. Select two.

- A. Add a read-only region to the configuration
- B. Enable regional high availability with a standby zone
- C. Add a cross-region read replica
- D. Choose a multi-region instance configuration
- E. Add a secondary cluster in the second region

### 88. A Cloud SQL primary must feed a reporting system in a second region with less than a minute of lag. What should the team add?

- A. Restore the backup into the second region
- B. Add a cross-region read replica
- C. Choose a multi-region instance configuration
- D. Add a secondary cluster in the second region

### 89. An AlloyDB deployment needs a second region that can both serve reads today and be promoted later. Which choice fits?

- A. Restore the backup into the second region
- B. Add nodes to the read pool
- C. Add a secondary cluster in the second region
- D. Run a single zonal instance

### 90. An AlloyDB read pool runs at ninety percent CPU while the primary sits at forty percent. What should the team do?

- A. Increase the machine type of the instance
- B. Send reporting queries to the read replica
- C. Cache the hot read path in Memorystore
- D. Add nodes to the read pool

### 91. A Cloud SQL replica is at twenty percent CPU while the primary is at ninety percent, both serving the same application. What should the team change?

- A. Increase the machine type of the instance
- B. Cache the hot read path in Memorystore
- C. Add a read replica for the read traffic
- D. Send reporting queries to the read replica

### 92. A team must create two hundred tenant Spanner instances with enforced quotas and identical configuration. What should they use?

- A. Review the fleet in Database Center
- B. Provision the instance once by hand
- C. Test the upgrade on a clone first
- D. Provision the instance with a Terraform module

### 93. A platform team wants provisioning to fail before it starts when a required data-classification label is missing. What should they use?

- A. Provision the instance once by hand
- B. Take a backup before the upgrade
- C. Clone the instance for the test
- D. Apply the change through the infrastructure pipeline

### 94. A team must learn about a failover immediately and confirm afterwards that the database still answers queries. Select two.

- A. Review the fleet in Database Center
- B. Alert when the instance is unreachable
- C. Watch CPU, memory, disk, and IOPS together
- D. Use Query Insights to find the heavy statements
- E. Create an alerting policy on the metric

### 95. A team wants one view of replication state, version posture, and failover history across two hundred instances. Which view fits?

- A. Watch CPU, memory, disk, and IOPS together
- B. Read the slow query log
- C. Review the fleet in Database Center
- D. Use Query Insights to find the heavy statements

### 96. A region is lost, a cross-region replica is current, and the recovery point objective is five minutes. What should the team do?

- A. Promote the cross-region replica during the outage
- B. Restore the backup into the second region
- C. Restore to the timestamp before the bad change
- D. Fence the old primary before promotion

### 97. The failed region comes back and its old primary begins accepting writes again while the promoted instance serves traffic. What must happen?

- A. Freeze writes during the cutover
- B. Fence the old primary before promotion
- C. Follow a cutover runbook with a rollback step
- D. Set up reverse replication to the source

### 98. Half the application fleet reconnects to the old instance after a failover because it cached the address. What should the team adopt?

- A. Repoint the connection string at the target
- B. Use the language connector with IAM credentials
- C. Put a session pooler in front of the instance
- D. Add the client range to authorized networks

### 99. A team must size a standby so that failing over at the daily peak keeps the published latency target. What is the right basis?

- A. Reduce the machine type to match observed use
- B. Reserve headroom above the measured peak
- C. Add a read replica for the read traffic
- D. Scale down outside business hours

### 100. A disaster plan assumes the standby can be enlarged at failover, but resizing takes forty minutes. What should change?

- A. Scale down outside business hours
- B. Add a read replica for the read traffic
- C. Pre-size the promoted replica for the full load
- D. Reserve headroom above the measured peak

---

## Answer key and explanations

### Question 1 — B

Answer: Reduce the machine type to match observed use. Shrinking to a shape that still covers the measured peak removes idle capacity, while headroom, replicas, and a commitment all preserve or add cost. Shrink an instance whose peak fits a smaller shape. Local study-map skill 1.1 (Workload Sizing From Current Metrics), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 1 (design innovative, scalable, and highly available cloud database solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Send reads to a copy so the primary keeps its capacity for writes. Why the correct answer wins: Shrinking to a shape that still covers the measured peak removes idle capacity, while headroom, replicas, and a commitment all preserve or add cost.
- **B:** Correct. Shrink an instance whose peak fits a smaller shape. In this case: Shrinking to a shape that still covers the measured peak removes idle capacity, while headroom, replicas, and a commitment all preserve or add cost.
- **C:** Incorrect for this question. A one- or three-year commitment that discounts the capacity always in use. Why the correct answer wins: Shrinking to a shape that still covers the measured peak removes idle capacity, while headroom, replicas, and a commitment all preserve or add cost.
- **D:** Incorrect for this question. Keep spare capacity so a failover or a traffic spike does not saturate the instance. Why the correct answer wins: Shrinking to a shape that still covers the measured peak removes idle capacity, while headroom, replicas, and a commitment all preserve or add cost.

### Question 2 — B

Answer: Load-test the workload to derive the size. Generating representative traffic on the prototype produces the resource curve that no historical metric can supply, so the size is derived rather than guessed. Generate representative traffic and read the resource curve before choosing a shape. Local study-map skill 1.1 (Workload Sizing From Current Metrics), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 1 (design innovative, scalable, and highly available cloud database solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Keep spare capacity so a failover or a traffic spike does not saturate the instance. Why the correct answer wins: Generating representative traffic on the prototype produces the resource curve that no historical metric can supply, so the size is derived rather than guessed.
- **B:** Correct. Generate representative traffic and read the resource curve before choosing a shape. In this case: Generating representative traffic on the prototype produces the resource curve that no historical metric can supply, so the size is derived rather than guessed.
- **C:** Incorrect for this question. A one- or three-year commitment that discounts the capacity always in use. Why the correct answer wins: Generating representative traffic on the prototype produces the resource curve that no historical metric can supply, so the size is derived rather than guessed.
- **D:** Incorrect for this question. Choose a shape from measured CPU, memory, and IOPS rather than from a guess. Why the correct answer wins: Generating representative traffic on the prototype produces the resource curve that no historical metric can supply, so the size is derived rather than guessed.

### Question 3 — B, D

Answers: Increase the disk size to raise throughput; Increase the machine type of the instance. More disk raises the throughput ceiling and a larger shape adds the memory the batch needs, while a replica, a pooler, or slower storage fixes neither bottleneck. Buy more storage so the attached disk also yields more IOPS and throughput. Move the instance to a larger shape so more vCPU and memory serve the same data. Local study-map skill 1.2 (Compute and Storage Sizing Tradeoffs), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 1 (design innovative, scalable, and highly available cloud database solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Trade latency for a lower price on large, throughput-oriented scans. Why the correct answer wins: More disk raises the throughput ceiling and a larger shape adds the memory the batch needs, while a replica, a pooler, or slower storage fixes neither bottleneck.
- **B:** Correct. Buy more storage so the attached disk also yields more IOPS and throughput. In this case: More disk raises the throughput ceiling and a larger shape adds the memory the batch needs, while a replica, a pooler, or slower storage fixes neither bottleneck.
- **C:** Incorrect for this question. A pooler that multiplexes many application connections onto few database sessions. Why the correct answer wins: More disk raises the throughput ceiling and a larger shape adds the memory the batch needs, while a replica, a pooler, or slower storage fixes neither bottleneck.
- **D:** Correct. Move the instance to a larger shape so more vCPU and memory serve the same data. In this case: More disk raises the throughput ceiling and a larger shape adds the memory the batch needs, while a replica, a pooler, or slower storage fixes neither bottleneck.
- **E:** Incorrect for this question. Send reads to a copy so the primary keeps its capacity for writes. Why the correct answer wins: More disk raises the throughput ceiling and a larger shape adds the memory the batch needs, while a replica, a pooler, or slower storage fixes neither bottleneck.

### Question 4 — B

Answer: Increase the disk size to raise throughput. Sizing for the projected three-year volume avoids an outage or an emergency resize, which automatic growth, a bucket rule, or archiving does not plan for. Buy more storage so the attached disk also yields more IOPS and throughput. Local study-map skill 1.2 (Compute and Storage Sizing Tradeoffs), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 1 (design innovative, scalable, and highly available cloud database solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Move aged, rarely read rows out of the hot table into Cloud Storage or BigQuery. Why the correct answer wins: Sizing for the projected three-year volume avoids an outage or an emergency resize, which automatic growth, a bucket rule, or archiving does not plan for.
- **B:** Correct. Buy more storage so the attached disk also yields more IOPS and throughput. In this case: Sizing for the projected three-year volume avoids an outage or an emergency resize, which automatic growth, a bucket rule, or archiving does not plan for.
- **C:** Incorrect for this question. Move or delete aged exports so the bucket does not grow without limit. Why the correct answer wins: Sizing for the projected three-year volume avoids an outage or an emergency resize, which automatic growth, a bucket rule, or archiving does not plan for.
- **D:** Incorrect for this question. Avoid a full-disk outage at the cost of unplanned storage growth. Why the correct answer wins: Sizing for the projected three-year volume avoids an outage or an emergency resize, which automatic growth, a bucket rule, or archiving does not plan for.

### Question 5 — D

Answer: Add nodes to the Bigtable cluster. Adding nodes adds the tablet-serving capacity the workload needs, whereas storage type, key design, and garbage collection do not increase throughput for a healthy access pattern. Increase the cluster size so more tablet servers absorb the request rate. Local study-map skill 1.3 (Machine Type and Storage Type Selection), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 1 (design innovative, scalable, and highly available cloud database solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A rule that drops versions by age or count, which also bounds recovery. Why the correct answer wins: Adding nodes adds the tablet-serving capacity the workload needs, whereas storage type, key design, and garbage collection do not increase throughput for a healthy access pattern.
- **B:** Incorrect for this question. Fix the access pattern that concentrates load on a narrow key range. Why the correct answer wins: Adding nodes adds the tablet-serving capacity the workload needs, whereas storage type, key design, and garbage collection do not increase throughput for a healthy access pattern.
- **C:** Incorrect for this question. Trade a higher price per gigabyte for lower latency on random reads. Why the correct answer wins: Adding nodes adds the tablet-serving capacity the workload needs, whereas storage type, key design, and garbage collection do not increase throughput for a healthy access pattern.
- **D:** Correct. Increase the cluster size so more tablet servers absorb the request rate. In this case: Adding nodes adds the tablet-serving capacity the workload needs, whereas storage type, key design, and garbage collection do not increase throughput for a healthy access pattern.

### Question 6 — B

Answer: Add processing units to the Spanner instance. Raising provisioned compute matches steady growth, while node counts for Bigtable, machine types, and read pools belong to different services. Raise provisioned compute in 1000-unit node steps or 100-unit increments. Local study-map skill 1.3 (Machine Type and Storage Type Selection), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 1 (design innovative, scalable, and highly available cloud database solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Grow the AlloyDB read pool that serves read-only connections. Why the correct answer wins: Raising provisioned compute matches steady growth, while node counts for Bigtable, machine types, and read pools belong to different services.
- **B:** Correct. Raise provisioned compute in 1000-unit node steps or 100-unit increments. In this case: Raising provisioned compute matches steady growth, while node counts for Bigtable, machine types, and read pools belong to different services.
- **C:** Incorrect for this question. Increase the cluster size so more tablet servers absorb the request rate. Why the correct answer wins: Raising provisioned compute matches steady growth, while node counts for Bigtable, machine types, and read pools belong to different services.
- **D:** Incorrect for this question. Move the instance to a larger shape so more vCPU and memory serve the same data. Why the correct answer wins: Raising provisioned compute matches steady growth, while node counts for Bigtable, machine types, and read pools belong to different services.

### Question 7 — A, C

Answers: Enable regional high availability with a standby zone; Add a cross-region read replica. A regional instance covers the zone case with automatic failover, and a cross-region replica adds the promotion path that the region case requires. A primary and standby in two zones of one region with automatic failover. A copy in a second region that serves reads and can be promoted. Local study-map skill 1.4 (Zonal, Regional, and Multi-Regional Tradeoffs), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 1 (design innovative, scalable, and highly available cloud database solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Correct. A copy in a second region that serves reads and can be promoted. In this case: A regional instance covers the zone case with automatic failover, and a cross-region replica adds the promotion path that the region case requires.
- **B:** Incorrect for this question. One instance in one zone with no standby, so a zone failure stops writes. Why the correct answer wins: A regional instance covers the zone case with automatic failover, and a cross-region replica adds the promotion path that the region case requires.
- **C:** Correct. A primary and standby in two zones of one region with automatic failover. In this case: A regional instance covers the zone case with automatic failover, and a cross-region replica adds the promotion path that the region case requires.
- **D:** Incorrect for this question. Rebuild the database in the surviving region from the latest backup. Why the correct answer wins: A regional instance covers the zone case with automatic failover, and a cross-region replica adds the promotion path that the region case requires.
- **E:** Incorrect for this question. A topology that places replicas in separate regions for regional-failure tolerance. Why the correct answer wins: A regional instance covers the zone case with automatic failover, and a cross-region replica adds the promotion path that the region case requires.

### Question 8 — A

Answer: Run a single zonal instance. Paying for redundancy on data that can be rebuilt wastes money, so a single zonal instance is the economical fit for this workload. One instance in one zone with no standby, so a zone failure stops writes. Local study-map skill 1.4 (Zonal, Regional, and Multi-Regional Tradeoffs), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 1 (design innovative, scalable, and highly available cloud database solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Correct. One instance in one zone with no standby, so a zone failure stops writes. In this case: Paying for redundancy on data that can be rebuilt wastes money, so a single zonal instance is the economical fit for this workload.
- **B:** Incorrect for this question. A copy in a second region that serves reads and can be promoted. Why the correct answer wins: Paying for redundancy on data that can be rebuilt wastes money, so a single zonal instance is the economical fit for this workload.
- **C:** Incorrect for this question. A topology that places replicas in separate regions for regional-failure tolerance. Why the correct answer wins: Paying for redundancy on data that can be rebuilt wastes money, so a single zonal instance is the economical fit for this workload.
- **D:** Incorrect for this question. A primary and standby in two zones of one region with automatic failover. Why the correct answer wins: Paying for redundancy on data that can be rebuilt wastes money, so a single zonal instance is the economical fit for this workload.

### Question 9 — B

Answer: Add a secondary cluster in the second region. A secondary cluster is both a promotable copy and a read target, while a read pool stays in one region and a restore cannot serve live reads. An AlloyDB cross-region copy that can be promoted to a primary cluster. Local study-map skill 1.4 (Zonal, Regional, and Multi-Regional Tradeoffs), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 1 (design innovative, scalable, and highly available cloud database solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. One instance in one zone with no standby, so a zone failure stops writes. Why the correct answer wins: A secondary cluster is both a promotable copy and a read target, while a read pool stays in one region and a restore cannot serve live reads.
- **B:** Correct. An AlloyDB cross-region copy that can be promoted to a primary cluster. In this case: A secondary cluster is both a promotable copy and a read target, while a read pool stays in one region and a restore cannot serve live reads.
- **C:** Incorrect for this question. Grow the AlloyDB read pool that serves read-only connections. Why the correct answer wins: A secondary cluster is both a promotable copy and a read target, while a read pool stays in one region and a restore cannot serve live reads.
- **D:** Incorrect for this question. Rebuild the database in the surviving region from the latest backup. Why the correct answer wins: A secondary cluster is both a promotable copy and a read target, while a read pool stays in one region and a restore cannot serve live reads.

### Question 10 — A, B

Answers: Schedule the maintenance window in the low-traffic period; Set a deny maintenance period over the peak event. The window sets when patching may occur and the deny period blocks it outright, whereas tests, backups, and restarts do not change when maintenance is scheduled. Choose the weekly window when patching may interrupt the instance. Block maintenance during a period when an interruption is unacceptable. Local study-map skill 1.5 (Maintenance Windows and Notification), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 1 (design innovative, scalable, and highly available cloud database solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Correct. Block maintenance during a period when an interruption is unacceptable. In this case: The window sets when patching may occur and the deny period blocks it outright, whereas tests, backups, and restarts do not change when maintenance is scheduled.
- **B:** Correct. Choose the weekly window when patching may interrupt the instance. In this case: The window sets when patching may occur and the deny period blocks it outright, whereas tests, backups, and restarts do not change when maintenance is scheduled.
- **C:** Incorrect for this question. A recovery point that makes the upgrade reversible in practice. Why the correct answer wins: The window sets when patching may occur and the deny period blocks it outright, whereas tests, backups, and restarts do not change when maintenance is scheduled.
- **D:** Incorrect for this question. Trigger a switchover in a test window and observe how long writes are unavailable. Why the correct answer wins: The window sets when patching may occur and the deny period blocks it outright, whereas tests, backups, and restarts do not change when maintenance is scheduled.
- **E:** Incorrect for this question. Apply the configuration change with a brief restart. Why the correct answer wins: The window sets when patching may occur and the deny period blocks it outright, whereas tests, backups, and restarts do not change when maintenance is scheduled.

### Question 11 — A

Answer: Set a deny maintenance period over the peak event. A deny period covers the protected days and then expires, while a normal window would still allow the interruption and an upgrade is the very event being deferred. Block maintenance during a period when an interruption is unacceptable. Local study-map skill 1.5 (Maintenance Windows and Notification), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 1 (design innovative, scalable, and highly available cloud database solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Correct. Block maintenance during a period when an interruption is unacceptable. In this case: A deny period covers the protected days and then expires, while a normal window would still allow the interruption and an upgrade is the very event being deferred.
- **B:** Incorrect for this question. Change the engine version on the running instance during the window. Why the correct answer wins: A deny period covers the protected days and then expires, while a normal window would still allow the interruption and an upgrade is the very event being deferred.
- **C:** Incorrect for this question. Trigger a switchover in a test window and observe how long writes are unavailable. Why the correct answer wins: A deny period covers the protected days and then expires, while a normal window would still allow the interruption and an upgrade is the very event being deferred.
- **D:** Incorrect for this question. Choose the weekly window when patching may interrupt the instance. Why the correct answer wins: A deny period covers the protected days and then expires, while a normal window would still allow the interruption and an upgrade is the very event being deferred.

### Question 12 — C

Answer: Connect through the Cloud SQL Auth Proxy. The proxy authorizes each connection with IAM and TLS from wherever it runs, so no public address or allowlist maintenance is required. A local proxy that adds IAM authorization and TLS without opening a network path. Local study-map skill 1.6 (Network Connectivity and Private Access), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 1 (design innovative, scalable, and highly available cloud database solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A public-IP allowlist that admits the caller range. Why the correct answer wins: The proxy authorizes each connection with IAM and TLS from wherever it runs, so no public address or allowlist maintenance is required.
- **B:** Incorrect for this question. A private endpoint in the consumer VPC that reaches the service without peering. Why the correct answer wins: The proxy authorizes each connection with IAM and TLS from wherever it runs, so no public address or allowlist maintenance is required.
- **C:** Correct. A local proxy that adds IAM authorization and TLS without opening a network path. In this case: The proxy authorizes each connection with IAM and TLS from wherever it runs, so no public address or allowlist maintenance is required.
- **D:** Incorrect for this question. A public address that requires encrypted connections from any client. Why the correct answer wins: The proxy authorizes each connection with IAM and TLS from wherever it runs, so no public address or allowlist maintenance is required.

### Question 13 — A

Answer: Use the language connector with IAM credentials. The language connector resolves the instance and authorizes it with the runtime identity, while private addressing needs a connector path and certificates need files. A client library that resolves the instance and authorizes the connection with IAM. Local study-map skill 1.6 (Network Connectivity and Private Access), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 1 (design innovative, scalable, and highly available cloud database solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Correct. A client library that resolves the instance and authorizes the connection with IAM. In this case: The language connector resolves the instance and authorizes it with the runtime identity, while private addressing needs a connector path and certificates need files.
- **B:** Incorrect for this question. A private endpoint in the consumer VPC that reaches the service without peering. Why the correct answer wins: The language connector resolves the instance and authorizes it with the runtime identity, while private addressing needs a connector path and certificates need files.
- **C:** Incorrect for this question. A private address reachable only from the VPC and connected networks. Why the correct answer wins: The language connector resolves the instance and authorizes it with the runtime identity, while private addressing needs a connector path and certificates need files.
- **D:** Incorrect for this question. A public-IP allowlist that admits the caller range. Why the correct answer wins: The language connector resolves the instance and authorizes it with the runtime identity, while private addressing needs a connector path and certificates need files.

### Question 14 — C

Answer: Encrypt with a customer-managed key in Cloud KMS. A customer-managed key gives the team custody and a disable switch, while a Google-managed key offers neither and a perimeter or a sink does not encrypt data. A key the customer owns and can rotate or revoke. Local study-map skill 1.7 (Key Management and Encryption), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 1 (design innovative, scalable, and highly available cloud database solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Export entries to storage whose retention cannot be shortened. Why the correct answer wins: A customer-managed key gives the team custody and a disable switch, while a Google-managed key offers neither and a perimeter or a sink does not encrypt data.
- **B:** Incorrect for this question. A boundary that blocks data exfiltration even from an authorized identity. Why the correct answer wins: A customer-managed key gives the team custody and a disable switch, while a Google-managed key offers neither and a perimeter or a sink does not encrypt data.
- **C:** Correct. A key the customer owns and can rotate or revoke. In this case: A customer-managed key gives the team custody and a disable switch, while a Google-managed key offers neither and a perimeter or a sink does not encrypt data.
- **D:** Incorrect for this question. Default encryption at rest with keys the customer neither sees nor manages. Why the correct answer wins: A customer-managed key gives the team custody and a disable switch, while a Google-managed key offers neither and a perimeter or a sink does not encrypt data.

### Question 15 — C

Answer: Rely on Google-managed encryption keys. Default Google-managed encryption protects the data without the customer running a key lifecycle, which customer keys and rotation would require. Default encryption at rest with keys the customer neither sees nor manages. Local study-map skill 1.7 (Key Management and Encryption), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 1 (design innovative, scalable, and highly available cloud database solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Produce new key versions so an old version stops encrypting new data. Why the correct answer wins: Default Google-managed encryption protects the data without the customer running a key lifecycle, which customer keys and rotation would require.
- **B:** Incorrect for this question. A boundary that blocks data exfiltration even from an authorized identity. Why the correct answer wins: Default Google-managed encryption protects the data without the customer running a key lifecycle, which customer keys and rotation would require.
- **C:** Correct. Default encryption at rest with keys the customer neither sees nor manages. In this case: Default Google-managed encryption protects the data without the customer running a key lifecycle, which customer keys and rotation would require.
- **D:** Incorrect for this question. A key the customer owns and can rotate or revoke. Why the correct answer wins: Default Google-managed encryption protects the data without the customer running a key lifecycle, which customer keys and rotation would require.

### Question 16 — D, E

Answers: Put a session pooler in front of the instance; Fix the connection leak in the application. Returning sessions to the pool stops the accumulation, and a pooler keeps the remaining load inside a smaller number of database sessions. A pooler that multiplexes many application connections onto few database sessions. Close sessions that the application opens and never returns to the pool. Local study-map skill 1.8 (Session Pooling and Connection Management), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 1 (design innovative, scalable, and highly available cloud database solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Increase the database-level connection ceiling on the instance. Why the correct answer wins: Returning sessions to the pool stops the accumulation, and a pooler keeps the remaining load inside a smaller number of database sessions.
- **B:** Incorrect for this question. Buy a larger shape because the connection limit scales with memory. Why the correct answer wins: Returning sessions to the pool stops the accumulation, and a pooler keeps the remaining load inside a smaller number of database sessions.
- **C:** Incorrect for this question. Move the instance to a larger shape so more vCPU and memory serve the same data. Why the correct answer wins: Returning sessions to the pool stops the accumulation, and a pooler keeps the remaining load inside a smaller number of database sessions.
- **D:** Correct. A pooler that multiplexes many application connections onto few database sessions. In this case: Returning sessions to the pool stops the accumulation, and a pooler keeps the remaining load inside a smaller number of database sessions.
- **E:** Correct. Close sessions that the application opens and never returns to the pool. In this case: Returning sessions to the pool stops the accumulation, and a pooler keeps the remaining load inside a smaller number of database sessions.

### Question 17 — D

Answer: Raise the max_connections database flag. When sessions are genuinely concurrent and memory is spare, the connection ceiling itself is the limit that has to move. Increase the database-level connection ceiling on the instance. Local study-map skill 1.8 (Session Pooling and Connection Management), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 1 (design innovative, scalable, and highly available cloud database solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Buy a larger shape because the connection limit scales with memory. Why the correct answer wins: When sessions are genuinely concurrent and memory is spare, the connection ceiling itself is the limit that has to move.
- **B:** Incorrect for this question. Close sessions that the application opens and never returns to the pool. Why the correct answer wins: When sessions are genuinely concurrent and memory is spare, the connection ceiling itself is the limit that has to move.
- **C:** Incorrect for this question. A pooler that multiplexes many application connections onto few database sessions. Why the correct answer wins: When sessions are genuinely concurrent and memory is spare, the connection ceiling itself is the limit that has to move.
- **D:** Correct. Increase the database-level connection ceiling on the instance. In this case: When sessions are genuinely concurrent and memory is spare, the connection ceiling itself is the limit that has to move.

### Question 18 — C

Answer: Rely on Admin Activity audit logs. Administrative configuration changes are recorded by default in Admin Activity logs, while Data Access logs cover row reads and writes rather than settings. Record configuration changes only, leaving row-level reads unaudited. Local study-map skill 1.9 (Auditing Policies for Managed Services), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 1 (design innovative, scalable, and highly available cloud database solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Record reads and writes, which are not captured by default. Why the correct answer wins: Administrative configuration changes are recorded by default in Admin Activity logs, while Data Access logs cover row reads and writes rather than settings.
- **B:** Incorrect for this question. A single view of health, security, and version posture across database instances. Why the correct answer wins: Administrative configuration changes are recorded by default in Admin Activity logs, while Data Access logs cover row reads and writes rather than settings.
- **C:** Correct. Record configuration changes only, leaving row-level reads unaudited. In this case: Administrative configuration changes are recorded by default in Admin Activity logs, while Data Access logs cover row reads and writes rather than settings.
- **D:** Incorrect for this question. Export entries to storage whose retention cannot be shortened. Why the correct answer wins: Administrative configuration changes are recorded by default in Admin Activity logs, while Data Access logs cover row reads and writes rather than settings.

### Question 19 — D

Answer: Route the audit logs to a locked log bucket. Routing the entries to locked storage keeps the evidence beyond the default bucket's life, which enabling more log types alone does not provide. Export entries to storage whose retention cannot be shortened. Local study-map skill 1.9 (Auditing Policies for Managed Services), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 1 (design innovative, scalable, and highly available cloud database solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Turn a recurring log pattern into a metric that can be charted and alerted on. Why the correct answer wins: Routing the entries to locked storage keeps the evidence beyond the default bucket's life, which enabling more log types alone does not provide.
- **B:** Incorrect for this question. Record reads and writes, which are not captured by default. Why the correct answer wins: Routing the entries to locked storage keeps the evidence beyond the default bucket's life, which enabling more log types alone does not provide.
- **C:** Incorrect for this question. Record configuration changes only, leaving row-level reads unaudited. Why the correct answer wins: Routing the entries to locked storage keeps the evidence beyond the default bucket's life, which enabling more log types alone does not provide.
- **D:** Correct. Export entries to storage whose retention cannot be shortened. In this case: Routing the entries to locked storage keeps the evidence beyond the default bucket's life, which enabling more log types alone does not provide.

### Question 20 — B

Answer: Use a partner-managed database offering. A partner-managed offering keeps the vendor's support relationship while running on Google Cloud infrastructure, unlike a self-managed or bare-metal deployment. A third-party database operated by its vendor on Google Cloud infrastructure. Local study-map skill 1.10 (Managed, Self-Managed, and Partner Offerings), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 1 (design innovative, scalable, and highly available cloud database solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Dedicated hardware for engines that cannot be virtualized or licensed for a managed service. Why the correct answer wins: A partner-managed offering keeps the vendor's support relationship while running on Google Cloud infrastructure, unlike a self-managed or bare-metal deployment.
- **B:** Correct. A third-party database operated by its vendor on Google Cloud infrastructure. In this case: A partner-managed offering keeps the vendor's support relationship while running on Google Cloud infrastructure, unlike a self-managed or bare-metal deployment.
- **C:** Incorrect for this question. A self-managed engine on virtual machines where the team owns patching, backups, and failover. Why the correct answer wins: A partner-managed offering keeps the vendor's support relationship while running on Google Cloud infrastructure, unlike a self-managed or bare-metal deployment.
- **D:** Incorrect for this question. A managed MySQL, PostgreSQL, or SQL Server instance with Google-operated backups, patching, and failover. Why the correct answer wins: A partner-managed offering keeps the vendor's support relationship while running on Google Cloud infrastructure, unlike a self-managed or bare-metal deployment.

### Question 21 — D

Answer: Use AlloyDB for the demanding relational workload. AlloyDB provides PostgreSQL compatibility with a broader extension set, while the other managed option lacks the extension and the remaining choices add operations. A managed PostgreSQL-compatible database with a separate read pool and columnar acceleration for mixed transactional and analytical load. Local study-map skill 1.10 (Managed, Self-Managed, and Partner Offerings), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 1 (design innovative, scalable, and highly available cloud database solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A horizontally scalable relational database with strong consistency across regions and no manual sharding. Why the correct answer wins: AlloyDB provides PostgreSQL compatibility with a broader extension set, while the other managed option lacks the extension and the remaining choices add operations.
- **B:** Incorrect for this question. A managed MySQL, PostgreSQL, or SQL Server instance with Google-operated backups, patching, and failover. Why the correct answer wins: AlloyDB provides PostgreSQL compatibility with a broader extension set, while the other managed option lacks the extension and the remaining choices add operations.
- **C:** Incorrect for this question. A self-managed engine on virtual machines where the team owns patching, backups, and failover. Why the correct answer wins: AlloyDB provides PostgreSQL compatibility with a broader extension set, while the other managed option lacks the extension and the remaining choices add operations.
- **D:** Correct. A managed PostgreSQL-compatible database with a separate read pool and columnar acceleration for mixed transactional and analytical load. In this case: AlloyDB provides PostgreSQL compatibility with a broader extension set, while the other managed option lacks the extension and the remaining choices add operations.

### Question 22 — D

Answer: Use Cloud SQL for the relational workload. A managed relational instance supplies the transactions and predictable latency at that size, while the distributed and NoSQL options impose models the workload does not need. A managed MySQL, PostgreSQL, or SQL Server instance with Google-operated backups, patching, and failover. Local study-map skill 1.11 (SQL and NoSQL Data Model Fit), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 1 (design innovative, scalable, and highly available cloud database solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A document database with automatic multi-region replication, offline client support, and index-driven queries. Why the correct answer wins: A managed relational instance supplies the transactions and predictable latency at that size, while the distributed and NoSQL options impose models the workload does not need.
- **B:** Incorrect for this question. A wide-column NoSQL service built for very high write and read rates over a sparse, row-key-ordered model. Why the correct answer wins: A managed relational instance supplies the transactions and predictable latency at that size, while the distributed and NoSQL options impose models the workload does not need.
- **C:** Incorrect for this question. A horizontally scalable relational database with strong consistency across regions and no manual sharding. Why the correct answer wins: A managed relational instance supplies the transactions and predictable latency at that size, while the distributed and NoSQL options impose models the workload does not need.
- **D:** Correct. A managed MySQL, PostgreSQL, or SQL Server instance with Google-operated backups, patching, and failover. In this case: A managed relational instance supplies the transactions and predictable latency at that size, while the distributed and NoSQL options impose models the workload does not need.

### Question 23 — C

Answer: Use Firestore for the document workload. The document model with client libraries and managed replication matches the requirement, which a wide-column store, a relational instance, or a cache does not provide together. A document database with automatic multi-region replication, offline client support, and index-driven queries. Local study-map skill 1.11 (SQL and NoSQL Data Model Fit), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 1 (design innovative, scalable, and highly available cloud database solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A wide-column NoSQL service built for very high write and read rates over a sparse, row-key-ordered model. Why the correct answer wins: The document model with client libraries and managed replication matches the requirement, which a wide-column store, a relational instance, or a cache does not provide together.
- **B:** Incorrect for this question. A managed Redis-compatible in-memory store placed in front of the system of record. Why the correct answer wins: The document model with client libraries and managed replication matches the requirement, which a wide-column store, a relational instance, or a cache does not provide together.
- **C:** Correct. A document database with automatic multi-region replication, offline client support, and index-driven queries. In this case: The document model with client libraries and managed replication matches the requirement, which a wide-column store, a relational instance, or a cache does not provide together.
- **D:** Incorrect for this question. A managed MySQL, PostgreSQL, or SQL Server instance with Google-operated backups, patching, and failover. Why the correct answer wins: The document model with client libraries and managed replication matches the requirement, which a wide-column store, a relational instance, or a cache does not provide together.

### Question 24 — A

Answer: Use Memorystore as the caching tier. An in-memory cache serves that latency from a rebuildable dataset, whereas the durable databases answer the latency question at higher cost and complexity. A managed Redis-compatible in-memory store placed in front of the system of record. Local study-map skill 1.11 (SQL and NoSQL Data Model Fit), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 1 (design innovative, scalable, and highly available cloud database solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Correct. A managed Redis-compatible in-memory store placed in front of the system of record. In this case: An in-memory cache serves that latency from a rebuildable dataset, whereas the durable databases answer the latency question at higher cost and complexity.
- **B:** Incorrect for this question. A wide-column NoSQL service built for very high write and read rates over a sparse, row-key-ordered model. Why the correct answer wins: An in-memory cache serves that latency from a rebuildable dataset, whereas the durable databases answer the latency question at higher cost and complexity.
- **C:** Incorrect for this question. A document database with automatic multi-region replication, offline client support, and index-driven queries. Why the correct answer wins: An in-memory cache serves that latency from a rebuildable dataset, whereas the durable databases answer the latency question at higher cost and complexity.
- **D:** Incorrect for this question. A managed MySQL, PostgreSQL, or SQL Server instance with Google-operated backups, patching, and failover. Why the correct answer wins: An in-memory cache serves that latency from a rebuildable dataset, whereas the durable databases answer the latency question at higher cost and complexity.

### Question 25 — B

Answer: Use AlloyDB vector search with a ScaNN index. A purpose-built vector index inside AlloyDB handles that scale with filters in the same engine, while the plain extension and the copy-based options do not meet the size or the locality requirement. A vector index tuned for large embedding sets on AlloyDB. Local study-map skill 1.12 (Vector and Generative AI Requirements), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 1 (design innovative, scalable, and highly available cloud database solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Store embeddings beside relational rows and search them in the same engine. Why the correct answer wins: A purpose-built vector index inside AlloyDB handles that scale with filters in the same engine, while the plain extension and the copy-based options do not meet the size or the locality requirement.
- **B:** Correct. A vector index tuned for large embedding sets on AlloyDB. In this case: A purpose-built vector index inside AlloyDB handles that scale with filters in the same engine, while the plain extension and the copy-based options do not meet the size or the locality requirement.
- **C:** Incorrect for this question. Copy the analytical slice into the warehouse on a schedule. Why the correct answer wins: A purpose-built vector index inside AlloyDB handles that scale with filters in the same engine, while the plain extension and the copy-based options do not meet the size or the locality requirement.
- **D:** Incorrect for this question. Read the operational table from BigQuery without copying it first. Why the correct answer wins: A purpose-built vector index inside AlloyDB handles that scale with filters in the same engine, while the plain extension and the copy-based options do not meet the size or the locality requirement.

### Question 26 — D

Answer: Enable the vector extension on PostgreSQL. Enabling the vector extension adds similarity search to the engine already in use, avoiding both a migration and a specialised index service. Store embeddings beside relational rows and search them in the same engine. Local study-map skill 1.12 (Vector and Generative AI Requirements), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 1 (design innovative, scalable, and highly available cloud database solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. An approximate-nearest-neighbour index over embedding columns. Why the correct answer wins: Enabling the vector extension adds similarity search to the engine already in use, avoiding both a migration and a specialised index service.
- **B:** Incorrect for this question. A vector index tuned for large embedding sets on AlloyDB. Why the correct answer wins: Enabling the vector extension adds similarity search to the engine already in use, avoiding both a migration and a specialised index service.
- **C:** Incorrect for this question. Absorb repeated reads in memory so the database sees fewer of them. Why the correct answer wins: Enabling the vector extension adds similarity search to the engine already in use, avoiding both a migration and a specialised index service.
- **D:** Correct. Store embeddings beside relational rows and search them in the same engine. In this case: Enabling the vector extension adds similarity search to the engine already in use, avoiding both a migration and a specialised index service.

### Question 27 — A, E

Answers: Reduce the machine type to match observed use; Commit to the steady baseline capacity. Shrinking over-provisioned shapes and committing the remaining steady baseline both lower cost while preserving the service level, whereas removing a live instance or relying on a discount that does not apply changes nothing. Shrink an instance whose peak fits a smaller shape. A one- or three-year commitment that discounts the capacity always in use. Local study-map skill 1.13 (Comparative Cost Analysis Across Databases), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 1 (design innovative, scalable, and highly available cloud database solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Correct. A one- or three-year commitment that discounts the capacity always in use. In this case: Shrinking over-provisioned shapes and committing the remaining steady baseline both lower cost while preserving the service level, whereas removing a live instance or relying on a discount that does not apply changes nothing.
- **B:** Incorrect for this question. Remove capacity that serves no traffic. Why the correct answer wins: Shrinking over-provisioned shapes and committing the remaining steady baseline both lower cost while preserving the service level, whereas removing a live instance or relying on a discount that does not apply changes nothing.
- **C:** Incorrect for this question. Avoid a full-disk outage at the cost of unplanned storage growth. Why the correct answer wins: Shrinking over-provisioned shapes and committing the remaining steady baseline both lower cost while preserving the service level, whereas removing a live instance or relying on a discount that does not apply changes nothing.
- **D:** Incorrect for this question. The automatic discount that applies to long-running Compute Engine usage. Why the correct answer wins: Shrinking over-provisioned shapes and committing the remaining steady baseline both lower cost while preserving the service level, whereas removing a live instance or relying on a discount that does not apply changes nothing.
- **E:** Correct. Shrink an instance whose peak fits a smaller shape. In this case: Shrinking over-provisioned shapes and committing the remaining steady baseline both lower cost while preserving the service level, whereas removing a live instance or relying on a discount that does not apply changes nothing.

### Question 28 — C

Answer: Stop or delete the idle instance. An instance that serves no traffic for most of the year should not run continuously, and a commitment or a rightsizing would still pay for idle capacity. Remove capacity that serves no traffic. Local study-map skill 1.13 (Comparative Cost Analysis Across Databases), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 1 (design innovative, scalable, and highly available cloud database solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A one- or three-year commitment that discounts the capacity always in use. Why the correct answer wins: An instance that serves no traffic for most of the year should not run continuously, and a commitment or a rightsizing would still pay for idle capacity.
- **B:** Incorrect for this question. Shrink an instance whose peak fits a smaller shape. Why the correct answer wins: An instance that serves no traffic for most of the year should not run continuously, and a commitment or a rightsizing would still pay for idle capacity.
- **C:** Correct. Remove capacity that serves no traffic. In this case: An instance that serves no traffic for most of the year should not run continuously, and a commitment or a rightsizing would still pay for idle capacity.
- **D:** Incorrect for this question. Hold capacity ahead of a known surge rather than waiting for autoscaling. Why the correct answer wins: An instance that serves no traffic for most of the year should not run continuously, and a commitment or a rightsizing would still pay for idle capacity.

### Question 29 — C

Answer: Choose the target engine with the cheapest conversion. Comparing conversion effort across the candidates chooses on evidence rather than preference, while keeping the engine or starting the migration skips the comparison entirely. Weigh engine compatibility and code rewrite effort before selecting a destination. Local study-map skill 1.14 (Application and Database Dependencies), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 1 (design innovative, scalable, and highly available cloud database solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A lift of the existing engine with no conversion work, retaining its behaviour and licensing. Why the correct answer wins: Comparing conversion effort across the candidates chooses on evidence rather than preference, while keeping the engine or starting the migration skips the comparison entirely.
- **B:** Incorrect for this question. Keep two databases current from application code during the transition. Why the correct answer wins: Comparing conversion effort across the candidates chooses on evidence rather than preference, while keeping the engine or starting the migration skips the comparison entirely.
- **C:** Correct. Weigh engine compatibility and code rewrite effort before selecting a destination. In this case: Comparing conversion effort across the candidates chooses on evidence rather than preference, while keeping the engine or starting the migration skips the comparison entirely.
- **D:** Incorrect for this question. A managed path that converts schema and code from a different source engine. Why the correct answer wins: Comparing conversion effort across the candidates chooses on evidence rather than preference, while keeping the engine or starting the migration skips the comparison entirely.

### Question 30 — A, C

Answers: Place the instance in the required region; Limit the user to the required schema. Choosing the in-country region settles where the data lives, and a schema-scoped grant limits who can read the table, while the other options address neither requirement. A location choice that keeps data inside the regulated boundary. Grant access to named objects instead of the whole instance. Local study-map skill 1.15 (Regulatory, Compliance, and Organization Policy), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 1 (design innovative, scalable, and highly available cloud database solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Correct. Grant access to named objects instead of the whole instance. In this case: Choosing the in-country region settles where the data lives, and a schema-scoped grant limits who can read the table, while the other options address neither requirement.
- **B:** Incorrect for this question. A boundary that blocks data exfiltration even from an authorized identity. Why the correct answer wins: Choosing the in-country region settles where the data lives, and a schema-scoped grant limits who can read the table, while the other options address neither requirement.
- **C:** Correct. A location choice that keeps data inside the regulated boundary. In this case: Choosing the in-country region settles where the data lives, and a schema-scoped grant limits who can read the table, while the other options address neither requirement.
- **D:** Incorrect for this question. Default encryption at rest with keys the customer neither sees nor manages. Why the correct answer wins: Choosing the in-country region settles where the data lives, and a schema-scoped grant limits who can read the table, while the other options address neither requirement.
- **E:** Incorrect for this question. Absorb repeated reads in memory so the database sees fewer of them. Why the correct answer wins: Choosing the in-country region settles where the data lives, and a schema-scoped grant limits who can read the table, while the other options address neither requirement.

### Question 31 — A

Answer: Add the projects to a VPC Service Controls perimeter. A service perimeter blocks the exfiltration path regardless of identity, while the copy and query options create the movement the policy forbids. A boundary that blocks data exfiltration even from an authorized identity. Local study-map skill 1.15 (Regulatory, Compliance, and Organization Policy), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 1 (design innovative, scalable, and highly available cloud database solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Correct. A boundary that blocks data exfiltration even from an authorized identity. In this case: A service perimeter blocks the exfiltration path regardless of identity, while the copy and query options create the movement the policy forbids.
- **B:** Incorrect for this question. Read the operational table from BigQuery without copying it first. Why the correct answer wins: A service perimeter blocks the exfiltration path regardless of identity, while the copy and query options create the movement the policy forbids.
- **C:** Incorrect for this question. Copy the analytical slice into the warehouse on a schedule. Why the correct answer wins: A service perimeter blocks the exfiltration path regardless of identity, while the copy and query options create the movement the policy forbids.
- **D:** Incorrect for this question. Keep an analytics copy current by applying change data capture. Why the correct answer wins: A service perimeter blocks the exfiltration path regardless of identity, while the copy and query options create the movement the policy forbids.

### Question 32 — C

Answer: Keep part of the estate on-premises with a hybrid link. A hybrid link keeps the contracted system in place and gives the new applications a supported path to it, whereas retiring it or copying it breaks the contract or duplicates data. Interconnect the remaining on-premises system rather than moving it. Local study-map skill 1.16 (Federation, Exports, and Hybrid Spans), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 1 (design innovative, scalable, and highly available cloud database solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Read the operational table from BigQuery without copying it first. Why the correct answer wins: A hybrid link keeps the contracted system in place and gives the new applications a supported path to it, whereas retiring it or copying it breaks the contract or duplicates data.
- **B:** Incorrect for this question. Copy the analytical slice into the warehouse on a schedule. Why the correct answer wins: A hybrid link keeps the contracted system in place and gives the new applications a supported path to it, whereas retiring it or copying it breaks the contract or duplicates data.
- **C:** Correct. Interconnect the remaining on-premises system rather than moving it. In this case: A hybrid link keeps the contracted system in place and gives the new applications a supported path to it, whereas retiring it or copying it breaks the contract or duplicates data.
- **D:** Incorrect for this question. Keep the old system read-only for a defined period, then remove it. Why the correct answer wins: A hybrid link keeps the contracted system in place and gives the new applications a supported path to it, whereas retiring it or copying it breaks the contract or duplicates data.

### Question 33 — D, E

Answers: Enable IAM database authentication; Bind access to a Google group. IAM database authentication removes the stored password, and binding the grant to a group means removing the person from the group ends the access. Map an IAM principal to a database user so no password is stored. Manage membership in a group rather than editing bindings per person. Local study-map skill 2.1 (IAM for Database Connectivity), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 2 (manage a solution that can span multiple database technologies): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A native database user whose credential must be rotated and stored. Why the correct answer wins: IAM database authentication removes the stored password, and binding the grant to a group means removing the person from the group ends the access.
- **B:** Incorrect for this question. A broad legacy role that can change most resources in the project. Why the correct answer wins: IAM database authentication removes the stored password, and binding the grant to a group means removing the person from the group ends the access.
- **C:** Incorrect for this question. A single credential used by every workload that touches the database. Why the correct answer wins: IAM database authentication removes the stored password, and binding the grant to a group means removing the person from the group ends the access.
- **D:** Correct. Map an IAM principal to a database user so no password is stored. In this case: IAM database authentication removes the stored password, and binding the grant to a group means removing the person from the group ends the access.
- **E:** Correct. Manage membership in a group rather than editing bindings per person. In this case: IAM database authentication removes the stored password, and binding the grant to a group means removing the person from the group ends the access.

### Question 34 — D

Answer: Limit the user to the required schema. Scoping the grant to the two named schemas gives exactly the access the application needs without widening it to every object on the instance. Grant access to named objects instead of the whole instance. Local study-map skill 2.1 (IAM for Database Connectivity), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 2 (manage a solution that can span multiple database technologies): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A role built from an explicit permission list. Why the correct answer wins: Scoping the grant to the two named schemas gives exactly the access the application needs without widening it to every object on the instance.
- **B:** Incorrect for this question. A broad legacy role that can change most resources in the project. Why the correct answer wins: Scoping the grant to the two named schemas gives exactly the access the application needs without widening it to every object on the instance.
- **C:** Incorrect for this question. Individual accountability at the engine layer rather than a shared login. Why the correct answer wins: Scoping the grant to the two named schemas gives exactly the access the application needs without widening it to every object on the instance.
- **D:** Correct. Grant access to named objects instead of the whole instance. In this case: Scoping the grant to the two named schemas gives exactly the access the application needs without widening it to every object on the instance.

### Question 35 — B

Answer: Enable IAM database authentication. Authentication through IAM issues short-lived tokens from the workload identity, so there is no long-lived secret to rotate or redeploy. Map an IAM principal to a database user so no password is stored. Local study-map skill 2.2 (Database Users and Authentication), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 2 (manage a solution that can span multiple database technologies): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A native database user whose credential must be rotated and stored. Why the correct answer wins: Authentication through IAM issues short-lived tokens from the workload identity, so there is no long-lived secret to rotate or redeploy.
- **B:** Correct. Map an IAM principal to a database user so no password is stored. In this case: Authentication through IAM issues short-lived tokens from the workload identity, so there is no long-lived secret to rotate or redeploy.
- **C:** Incorrect for this question. Individual accountability at the engine layer rather than a shared login. Why the correct answer wins: Authentication through IAM issues short-lived tokens from the workload identity, so there is no long-lived secret to rotate or redeploy.
- **D:** Incorrect for this question. A single credential used by every workload that touches the database. Why the correct answer wins: Authentication through IAM issues short-lived tokens from the workload identity, so there is no long-lived secret to rotate or redeploy.

### Question 36 — B, D

Answers: Use Query Insights to find the heavy statements; Read the query plan for the statement. Per-query load identifies which statement and wait dominate, and the plan shows the access path that produced the time, which together justify a fix. A per-query view of latency, load, and wait events on the instance. Inspect the chosen scan and join order before changing anything. Local study-map skill 2.3 (Slow Queries and Missing Indexes), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 2 (manage a solution that can span multiple database technologies): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Create an index that turns a scan into a lookup for the predicate. Why the correct answer wins: Per-query load identifies which statement and wait dominate, and the plan shows the access path that produced the time, which together justify a fix.
- **B:** Correct. Inspect the chosen scan and join order before changing anything. In this case: Per-query load identifies which statement and wait dominate, and the plan shows the access path that produced the time, which together justify a fix.
- **C:** Incorrect for this question. Give the planner current cardinality so it stops choosing a poor plan. Why the correct answer wins: Per-query load identifies which statement and wait dominate, and the plan shows the access path that produced the time, which together justify a fix.
- **D:** Correct. A per-query view of latency, load, and wait events on the instance. In this case: Per-query load identifies which statement and wait dominate, and the plan shows the access path that produced the time, which together justify a fix.
- **E:** Incorrect for this question. Absorb repeated reads in memory so the database sees fewer of them. Why the correct answer wins: Per-query load identifies which statement and wait dominate, and the plan shows the access path that produced the time, which together justify a fix.

### Question 37 — D

Answer: Add the index the slow query needs. An index ordered by the filter and the sort resolves both parts without scanning or sorting the whole table. Create an index that turns a scan into a lookup for the predicate. Local study-map skill 2.3 (Slow Queries and Missing Indexes), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 2 (manage a solution that can span multiple database technologies): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Give sorts and joins more working memory on the instance. Why the correct answer wins: An index ordered by the filter and the sort resolves both parts without scanning or sorting the whole table.
- **B:** Incorrect for this question. Give the planner current cardinality so it stops choosing a poor plan. Why the correct answer wins: An index ordered by the filter and the sort resolves both parts without scanning or sorting the whole table.
- **C:** Incorrect for this question. Split one table into ranges so pruning and maintenance act on less data. Why the correct answer wins: An index ordered by the filter and the sort resolves both parts without scanning or sorting the whole table.
- **D:** Correct. Create an index that turns a scan into a lookup for the predicate. In this case: An index ordered by the filter and the sort resolves both parts without scanning or sorting the whole table.

### Question 38 — B

Answer: Inspect lock waits and blocking sessions. The lock graph shows which transactions block each other, which is what a fix has to change; batching or killing sessions would not explain the cycle. Find the transaction that holds the lock others wait on. Local study-map skill 2.4 (Locking and Resource Contention), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 2 (manage a solution that can span multiple database technologies): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Create an index that turns a scan into a lookup for the predicate. Why the correct answer wins: The lock graph shows which transactions block each other, which is what a fix has to change; batching or killing sessions would not explain the cycle.
- **B:** Correct. Find the transaction that holds the lock others wait on. In this case: The lock graph shows which transactions block each other, which is what a fix has to change; batching or killing sessions would not explain the cycle.
- **C:** Incorrect for this question. End the blocking transaction so the queue drains. Why the correct answer wins: The lock graph shows which transactions block each other, which is what a fix has to change; batching or killing sessions would not explain the cycle.
- **D:** Incorrect for this question. Cut per-row network and commit overhead in the application. Why the correct answer wins: The lock graph shows which transactions block each other, which is what a fix has to change; batching or killing sessions would not explain the cycle.

### Question 39 — A

Answer: Terminate the session that holds the lock. Ending the session that holds the locks releases the schema change, while inspection, routing, or statistics leave that transaction running. End the blocking transaction so the queue drains. Local study-map skill 2.4 (Locking and Resource Contention), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 2 (manage a solution that can span multiple database technologies): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Correct. End the blocking transaction so the queue drains. In this case: Ending the session that holds the locks releases the schema change, while inspection, routing, or statistics leave that transaction running.
- **B:** Incorrect for this question. Find the transaction that holds the lock others wait on. Why the correct answer wins: Ending the session that holds the locks releases the schema change, while inspection, routing, or statistics leave that transaction running.
- **C:** Incorrect for this question. Separate analytical reads from the write path. Why the correct answer wins: Ending the session that holds the locks releases the schema change, while inspection, routing, or statistics leave that transaction running.
- **D:** Incorrect for this question. Give the planner current cardinality so it stops choosing a poor plan. Why the correct answer wins: Ending the session that holds the locks releases the schema change, while inspection, routing, or statistics leave that transaction running.

### Question 40 — B

Answer: Watch CPU, memory, disk, and IOPS together. The instance view shows CPU, memory, disk, and IOPS side by side, which is what separates a compute ceiling from a storage wait. Read the instance-level signals before attributing the symptom to the query. Local study-map skill 2.5 (Database Vitals Monitoring), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 2 (manage a solution that can span multiple database technologies): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A single view of health, security, and version posture across database instances. Why the correct answer wins: The instance view shows CPU, memory, disk, and IOPS side by side, which is what separates a compute ceiling from a storage wait.
- **B:** Correct. Read the instance-level signals before attributing the symptom to the query. In this case: The instance view shows CPU, memory, disk, and IOPS side by side, which is what separates a compute ceiling from a storage wait.
- **C:** Incorrect for this question. A per-query view of latency, load, and wait events on the instance. Why the correct answer wins: The instance view shows CPU, memory, disk, and IOPS side by side, which is what separates a compute ceiling from a storage wait.
- **D:** Incorrect for this question. The engine log of statements that exceeded the long-query threshold. Why the correct answer wins: The instance view shows CPU, memory, disk, and IOPS side by side, which is what separates a compute ceiling from a storage wait.

### Question 41 — D

Answer: Use Query Insights to find the heavy statements. Per-query wait breakdown attributes latency to a cause at the statement level, while the other options give resource totals or raw log text. A per-query view of latency, load, and wait events on the instance. Local study-map skill 2.5 (Database Vitals Monitoring), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 2 (manage a solution that can span multiple database technologies): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Turn a recurring log pattern into a metric that can be charted and alerted on. Why the correct answer wins: Per-query wait breakdown attributes latency to a cause at the statement level, while the other options give resource totals or raw log text.
- **B:** Incorrect for this question. The engine log of statements that exceeded the long-query threshold. Why the correct answer wins: Per-query wait breakdown attributes latency to a cause at the statement level, while the other options give resource totals or raw log text.
- **C:** Incorrect for this question. Read the instance-level signals before attributing the symptom to the query. Why the correct answer wins: Per-query wait breakdown attributes latency to a cause at the statement level, while the other options give resource totals or raw log text.
- **D:** Correct. A per-query view of latency, load, and wait events on the instance. In this case: Per-query wait breakdown attributes latency to a cause at the statement level, while the other options give resource totals or raw log text.

### Question 42 — A

Answer: Request a quota increase for the project. When the schedule truly requires the concurrency, the project ceiling has to be raised, since staggering delays the delivery and retries hit the same limit. Raise the project-level ceiling so the operation is no longer refused. Local study-map skill 2.6 (Quotas and Limits), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 2 (manage a solution that can span multiple database technologies): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Correct. Raise the project-level ceiling so the operation is no longer refused. In this case: When the schedule truly requires the concurrency, the project ceiling has to be raised, since staggering delays the delivery and retries hit the same limit.
- **B:** Incorrect for this question. A flat-file extract for a downstream loader rather than a restore. Why the correct answer wins: When the schedule truly requires the concurrency, the project ceiling has to be raised, since staggering delays the delivery and retries hit the same limit.
- **C:** Incorrect for this question. Stagger the work so concurrent operations stop colliding on the same limit. Why the correct answer wins: When the schedule truly requires the concurrency, the project ceiling has to be raised, since staggering delays the delivery and retries hit the same limit.
- **D:** Incorrect for this question. Repeat the call after a growing delay so a transient refusal clears. Why the correct answer wins: When the schedule truly requires the concurrency, the project ceiling has to be raised, since staggering delays the delivery and retries hit the same limit.

### Question 43 — A, E

Answers: Alert on the database error rate; Alert on replication lag. Alerting on failed statements and on replication lag pages on symptoms users feel, so the harmless batch no longer wakes anyone. Page on failed statements rather than on resource saturation alone. Page when the copy falls behind the primary by more than the budget. Local study-map skill 2.7 (Alerts for Errors and Performance), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 2 (manage a solution that can span multiple database technologies): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Correct. Page when the copy falls behind the primary by more than the budget. In this case: Alerting on failed statements and on replication lag pages on symptoms users feel, so the harmless batch no longer wakes anyone.
- **B:** Incorrect for this question. Read the instance-level signals before attributing the symptom to the query. Why the correct answer wins: Alerting on failed statements and on replication lag pages on symptoms users feel, so the harmless batch no longer wakes anyone.
- **C:** Incorrect for this question. Turn a recurring log pattern into a metric that can be charted and alerted on. Why the correct answer wins: Alerting on failed statements and on replication lag pages on symptoms users feel, so the harmless batch no longer wakes anyone.
- **D:** Incorrect for this question. A condition that pages a human when the threshold is crossed. Why the correct answer wins: Alerting on failed statements and on replication lag pages on symptoms users feel, so the harmless batch no longer wakes anyone.
- **E:** Correct. Page on failed statements rather than on resource saturation alone. In this case: Alerting on failed statements and on replication lag pages on symptoms users feel, so the harmless batch no longer wakes anyone.

### Question 44 — B

Answer: Build a log-based metric from the error entries. A metric derived from the log pattern makes the occurrences countable and chartable, which reading the log by hand cannot sustain. Turn a recurring log pattern into a metric that can be charted and alerted on. Local study-map skill 2.7 (Alerts for Errors and Performance), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 2 (manage a solution that can span multiple database technologies): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. The engine log of statements that exceeded the long-query threshold. Why the correct answer wins: A metric derived from the log pattern makes the occurrences countable and chartable, which reading the log by hand cannot sustain.
- **B:** Correct. Turn a recurring log pattern into a metric that can be charted and alerted on. In this case: A metric derived from the log pattern makes the occurrences countable and chartable, which reading the log by hand cannot sustain.
- **C:** Incorrect for this question. A liveness signal that fires before users report the outage. Why the correct answer wins: A metric derived from the log pattern makes the occurrences countable and chartable, which reading the log by hand cannot sustain.
- **D:** Incorrect for this question. Export entries to storage whose retention cannot be shortened. Why the correct answer wins: A metric derived from the log pattern makes the occurrences countable and chartable, which reading the log by hand cannot sustain.

### Question 45 — D, E

Answers: Enable automated backups with a retention window; Export a logical dump to Cloud Storage. Managed backups hold the retention window, and a logical dump can be loaded selectively into a scratch database for a single-table recovery. Scheduled backups kept for a chosen number of days. A portable SQL dump taken with the engine tooling. Local study-map skill 2.8 (Backup and Recovery Option Selection), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 2 (manage a solution that can span multiple database technologies): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Continuous log capture that lets the instance return to an arbitrary moment. Why the correct answer wins: Managed backups hold the retention window, and a logical dump can be loaded selectively into a scratch database for a single-table recovery.
- **B:** Incorrect for this question. A manual checkpoint taken immediately before a risky operation. Why the correct answer wins: Managed backups hold the retention window, and a logical dump can be loaded selectively into a scratch database for a single-table recovery.
- **C:** Incorrect for this question. A copy of the current data created without touching the source. Why the correct answer wins: Managed backups hold the retention window, and a logical dump can be loaded selectively into a scratch database for a single-table recovery.
- **D:** Correct. A portable SQL dump taken with the engine tooling. In this case: Managed backups hold the retention window, and a logical dump can be loaded selectively into a scratch database for a single-table recovery.
- **E:** Correct. Scheduled backups kept for a chosen number of days. In this case: Managed backups hold the retention window, and a logical dump can be loaded selectively into a scratch database for a single-table recovery.

### Question 46 — C

Answer: Extend the backup retention window. Extending the retention window makes the managed backups cover the required period, which a bucket rule, a manual backup, or a log window cannot. Keep backups longer so an older restore point remains available. Local study-map skill 2.8 (Backup and Recovery Option Selection), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 2 (manage a solution that can span multiple database technologies): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A manual checkpoint taken immediately before a risky operation. Why the correct answer wins: Extending the retention window makes the managed backups cover the required period, which a bucket rule, a manual backup, or a log window cannot.
- **B:** Incorrect for this question. Continuous log capture that lets the instance return to an arbitrary moment. Why the correct answer wins: Extending the retention window makes the managed backups cover the required period, which a bucket rule, a manual backup, or a log window cannot.
- **C:** Correct. Keep backups longer so an older restore point remains available. In this case: Extending the retention window makes the managed backups cover the required period, which a bucket rule, a manual backup, or a log window cannot.
- **D:** Incorrect for this question. Move or delete aged exports so the bucket does not grow without limit. Why the correct answer wins: Extending the retention window makes the managed backups cover the required period, which a bucket rule, a manual backup, or a log window cannot.

### Question 47 — A

Answer: Import the dump into the target instance. The managed import path loads a logical dump into the instance, whereas export, federation, and change capture all move data the other way. Load a logical dump file into the database through the managed import path. Local study-map skill 2.9 (Export and Import Configuration), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 2 (manage a solution that can span multiple database technologies): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Correct. Load a logical dump file into the database through the managed import path. In this case: The managed import path loads a logical dump into the instance, whereas export, federation, and change capture all move data the other way.
- **B:** Incorrect for this question. Keep an analytics copy current by applying change data capture. Why the correct answer wins: The managed import path loads a logical dump into the instance, whereas export, federation, and change capture all move data the other way.
- **C:** Incorrect for this question. Read the operational table from BigQuery without copying it first. Why the correct answer wins: The managed import path loads a logical dump into the instance, whereas export, federation, and change capture all move data the other way.
- **D:** Incorrect for this question. A portable SQL dump taken with the engine tooling. Why the correct answer wins: The managed import path loads a logical dump into the instance, whereas export, federation, and change capture all move data the other way.

### Question 48 — A

Answer: Enable point-in-time recovery. Replaying the transaction log to a chosen moment reaches a state minutes old without a second copy, which nightly backups or a dump cannot. Continuous log capture that lets the instance return to an arbitrary moment. Local study-map skill 2.10 (RTO, RPO, and Point-in-Time Recovery), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 2 (manage a solution that can span multiple database technologies): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Correct. Continuous log capture that lets the instance return to an arbitrary moment. In this case: Replaying the transaction log to a chosen moment reaches a state minutes old without a second copy, which nightly backups or a dump cannot.
- **B:** Incorrect for this question. Scheduled backups kept for a chosen number of days. Why the correct answer wins: Replaying the transaction log to a chosen moment reaches a state minutes old without a second copy, which nightly backups or a dump cannot.
- **C:** Incorrect for this question. Trigger a switchover in a test window and observe how long writes are unavailable. Why the correct answer wins: Replaying the transaction log to a chosen moment reaches a state minutes old without a second copy, which nightly backups or a dump cannot.
- **D:** Incorrect for this question. A portable SQL dump taken with the engine tooling. Why the correct answer wins: Replaying the transaction log to a chosen moment reaches a state minutes old without a second copy, which nightly backups or a dump cannot.

### Question 49 — D

Answer: Add a cross-region read replica. A replica that can be promoted avoids the restore entirely, which no retention or backup change shortens enough to meet eight hours. A copy in a second region that serves reads and can be promoted. Local study-map skill 2.10 (RTO, RPO, and Point-in-Time Recovery), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 2 (manage a solution that can span multiple database technologies): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A point-in-time restore that discards the later writes on the same instance. Why the correct answer wins: A replica that can be promoted avoids the restore entirely, which no retention or backup change shortens enough to meet eight hours.
- **B:** Incorrect for this question. A recovery point that makes the upgrade reversible in practice. Why the correct answer wins: A replica that can be promoted avoids the restore entirely, which no retention or backup change shortens enough to meet eight hours.
- **C:** Incorrect for this question. Keep backups longer so an older restore point remains available. Why the correct answer wins: A replica that can be promoted avoids the restore entirely, which no retention or backup change shortens enough to meet eight hours.
- **D:** Correct. A copy in a second region that serves reads and can be promoted. In this case: A replica that can be promoted avoids the restore entirely, which no retention or backup change shortens enough to meet eight hours.

### Question 50 — A

Answer: Set the garbage-collection policy on the column family. A garbage-collection policy on the column family drops old versions by age while leaving the current values and the retained history intact. A rule that drops versions by age or count, which also bounds recovery. Local study-map skill 2.11 (Data Retention Management), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 2 (manage a solution that can span multiple database technologies): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Correct. A rule that drops versions by age or count, which also bounds recovery. In this case: A garbage-collection policy on the column family drops old versions by age while leaving the current values and the retained history intact.
- **B:** Incorrect for this question. Delete or expire records once the legal hold period ends. Why the correct answer wins: A garbage-collection policy on the column family drops old versions by age while leaving the current values and the retained history intact.
- **C:** Incorrect for this question. Move aged, rarely read rows out of the hot table into Cloud Storage or BigQuery. Why the correct answer wins: A garbage-collection policy on the column family drops old versions by age while leaving the current values and the retained history intact.
- **D:** Incorrect for this question. Expire documents once their usefulness ends. Why the correct answer wins: A garbage-collection policy on the column family drops old versions by age while leaving the current values and the retained history intact.

### Question 51 — A

Answer: Add a read-only region to the configuration. A read-only region serves reads locally while write leadership stays where it is, which more compute or another service's replica would not provide. Serve reads near users without making the region a write leader. Local study-map skill 2.12 (Scaling Up Versus Scaling Out), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 2 (manage a solution that can span multiple database technologies): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Correct. Serve reads near users without making the region a write leader. In this case: A read-only region serves reads locally while write leadership stays where it is, which more compute or another service's replica would not provide.
- **B:** Incorrect for this question. A copy in a second region that serves reads and can be promoted. Why the correct answer wins: A read-only region serves reads locally while write leadership stays where it is, which more compute or another service's replica would not provide.
- **C:** Incorrect for this question. Raise provisioned compute in 1000-unit node steps or 100-unit increments. Why the correct answer wins: A read-only region serves reads locally while write leadership stays where it is, which more compute or another service's replica would not provide.
- **D:** Incorrect for this question. Grow the AlloyDB read pool that serves read-only connections. Why the correct answer wins: A read-only region serves reads locally while write leadership stays where it is, which more compute or another service's replica would not provide.

### Question 52 — C

Answer: Increase the machine type of the instance. A larger shape carries the existing query mix until routing can change, whereas a replica or a cache requires the application change that is not available yet. Move the instance to a larger shape so more vCPU and memory serve the same data. Local study-map skill 2.12 (Scaling Up Versus Scaling Out), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 2 (manage a solution that can span multiple database technologies): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Send reads to a copy so the primary keeps its capacity for writes. Why the correct answer wins: A larger shape carries the existing query mix until routing can change, whereas a replica or a cache requires the application change that is not available yet.
- **B:** Incorrect for this question. Absorb repeated reads in memory so the database sees fewer of them. Why the correct answer wins: A larger shape carries the existing query mix until routing can change, whereas a replica or a cache requires the application change that is not available yet.
- **C:** Correct. Move the instance to a larger shape so more vCPU and memory serve the same data. In this case: A larger shape carries the existing query mix until routing can change, whereas a replica or a cache requires the application change that is not available yet.
- **D:** Incorrect for this question. Separate analytical reads from the write path. Why the correct answer wins: A larger shape carries the existing query mix until routing can change, whereas a replica or a cache requires the application change that is not available yet.

### Question 53 — B

Answer: Route the app profile across both clusters. A multi-cluster app profile performs the failover for the client, while pinning a profile or using another service's replication leaves the client fixed. A Bigtable app profile that fails over between clusters without a client change. Local study-map skill 2.13 (Replication Strategies), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 2 (manage a solution that can span multiple database technologies): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. An AlloyDB cross-region copy that can be promoted to a primary cluster. Why the correct answer wins: A multi-cluster app profile performs the failover for the client, while pinning a profile or using another service's replication leaves the client fixed.
- **B:** Correct. A Bigtable app profile that fails over between clusters without a client change. In this case: A multi-cluster app profile performs the failover for the client, while pinning a profile or using another service's replication leaves the client fixed.
- **C:** Incorrect for this question. A copy in a second region that serves reads and can be promoted. Why the correct answer wins: A multi-cluster app profile performs the failover for the client, while pinning a profile or using another service's replication leaves the client fixed.
- **D:** Incorrect for this question. A Bigtable app profile that keeps a workload on one cluster for predictable latency. Why the correct answer wins: A multi-cluster app profile performs the failover for the client, while pinning a profile or using another service's replication leaves the client fixed.

### Question 54 — A

Answer: Export the table into BigQuery. Moving the analytical workload to the warehouse removes the repeated scans from production, whereas partitioning, caching, or more memory keeps them on the same instance. Copy the analytical slice into the warehouse on a schedule. Local study-map skill 2.14 (Query Optimization for Cost and Performance), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 2 (manage a solution that can span multiple database technologies): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Correct. Copy the analytical slice into the warehouse on a schedule. In this case: Moving the analytical workload to the warehouse removes the repeated scans from production, whereas partitioning, caching, or more memory keeps them on the same instance.
- **B:** Incorrect for this question. Split one table into ranges so pruning and maintenance act on less data. Why the correct answer wins: Moving the analytical workload to the warehouse removes the repeated scans from production, whereas partitioning, caching, or more memory keeps them on the same instance.
- **C:** Incorrect for this question. Give sorts and joins more working memory on the instance. Why the correct answer wins: Moving the analytical workload to the warehouse removes the repeated scans from production, whereas partitioning, caching, or more memory keeps them on the same instance.
- **D:** Incorrect for this question. Absorb repeated reads in memory so the database sees fewer of them. Why the correct answer wins: Moving the analytical workload to the warehouse removes the repeated scans from production, whereas partitioning, caching, or more memory keeps them on the same instance.

### Question 55 — A

Answer: Run the task on a managed schedule. A managed schedule executes the recurring rebuild without an operator, which a one-off backup, a manual creation, or a test cannot do. A recurring trigger that performs the work with nobody present. Local study-map skill 2.15 (Automated Maintenance and Scheduled Exports), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 2 (manage a solution that can span multiple database technologies): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Correct. A recurring trigger that performs the work with nobody present. In this case: A managed schedule executes the recurring rebuild without an operator, which a one-off backup, a manual creation, or a test cannot do.
- **B:** Incorrect for this question. Trigger a switchover in a test window and observe how long writes are unavailable. Why the correct answer wins: A managed schedule executes the recurring rebuild without an operator, which a one-off backup, a manual creation, or a test cannot do.
- **C:** Incorrect for this question. Create the resource interactively with no stored definition. Why the correct answer wins: A managed schedule executes the recurring rebuild without an operator, which a one-off backup, a manual creation, or a test cannot do.
- **D:** Incorrect for this question. A manual checkpoint taken immediately before a risky operation. Why the correct answer wins: A managed schedule executes the recurring rebuild without an operator, which a one-off backup, a manual creation, or a test cannot do.

### Question 56 — C

Answer: Add a lifecycle rule to the export bucket. A lifecycle rule removes the older files automatically, whereas the export itself, a schedule, or a manual backup does not control accumulation. Move or delete aged exports so the bucket does not grow without limit. Local study-map skill 2.15 (Automated Maintenance and Scheduled Exports), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 2 (manage a solution that can span multiple database technologies): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A manual checkpoint taken immediately before a risky operation. Why the correct answer wins: A lifecycle rule removes the older files automatically, whereas the export itself, a schedule, or a manual backup does not control accumulation.
- **B:** Incorrect for this question. A portable SQL dump taken with the engine tooling. Why the correct answer wins: A lifecycle rule removes the older files automatically, whereas the export itself, a schedule, or a manual backup does not control accumulation.
- **C:** Correct. Move or delete aged exports so the bucket does not grow without limit. In this case: A lifecycle rule removes the older files automatically, whereas the export itself, a schedule, or a manual backup does not control accumulation.
- **D:** Incorrect for this question. A recurring trigger that performs the work with nobody present. Why the correct answer wins: A lifecycle rule removes the older files automatically, whereas the export itself, a schedule, or a manual backup does not control accumulation.

### Question 57 — A

Answer: Track the availability signal against the agreed objective. Comparing the availability signal against the stated objective measures the promise, which resource alerts or inventory views do not express. Compare observed service levels with the commitment rather than watching raw resource metrics. Local study-map skill 2.16 (Managed Upgrades and SLA Monitoring), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 2 (manage a solution that can span multiple database technologies): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Correct. Compare observed service levels with the commitment rather than watching raw resource metrics. In this case: Comparing the availability signal against the stated objective measures the promise, which resource alerts or inventory views do not express.
- **B:** Incorrect for this question. A condition that pages a human when the threshold is crossed. Why the correct answer wins: Comparing the availability signal against the stated objective measures the promise, which resource alerts or inventory views do not express.
- **C:** Incorrect for this question. A single view of health, security, and version posture across database instances. Why the correct answer wins: Comparing the availability signal against the stated objective measures the promise, which resource alerts or inventory views do not express.
- **D:** Incorrect for this question. Read the instance-level signals before attributing the symptom to the query. Why the correct answer wins: Comparing the availability signal against the stated objective measures the promise, which resource alerts or inventory views do not express.

### Question 58 — B, D

Answers: Use Database Migration Service for the same engine; Set up reverse replication to the source. Continuous replication keeps the outage to the final switch, and replicating back to the source makes the same-day rollback lossless. A managed migration that moves a supported engine to the same engine on Google Cloud. Keep writing back to the original system so a rollback loses nothing. Local study-map skill 3.1 (Migration Strategy and Downtime Budget), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 3 (migrate data solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Keep two databases current from application code during the transition. Why the correct answer wins: Continuous replication keeps the outage to the final switch, and replicating back to the source makes the same-day rollback lossless.
- **B:** Correct. Keep writing back to the original system so a rollback loses nothing. In this case: Continuous replication keeps the outage to the final switch, and replicating back to the source makes the same-day rollback lossless.
- **C:** Incorrect for this question. A bulk load followed by a catch-up pass for the writes made during the load. Why the correct answer wins: Continuous replication keeps the outage to the final switch, and replicating back to the source makes the same-day rollback lossless.
- **D:** Correct. A managed migration that moves a supported engine to the same engine on Google Cloud. In this case: Continuous replication keeps the outage to the final switch, and replicating back to the source makes the same-day rollback lossless.
- **E:** Incorrect for this question. Stop the source, load everything, and start the target in one window. Why the correct answer wins: Continuous replication keeps the outage to the final switch, and replicating back to the source makes the same-day rollback lossless.

### Question 59 — C

Answer: Dump, restore, then replay the changes. Repeated dump and restore per tenant suits short accepted windows, while replication machinery or dual writes add complexity the schedule does not require. A bulk load followed by a catch-up pass for the writes made during the load. Local study-map skill 3.1 (Migration Strategy and Downtime Budget), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 3 (migrate data solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Keep two databases current from application code during the transition. Why the correct answer wins: Repeated dump and restore per tenant suits short accepted windows, while replication machinery or dual writes add complexity the schedule does not require.
- **B:** Incorrect for this question. A managed migration that moves a supported engine to the same engine on Google Cloud. Why the correct answer wins: Repeated dump and restore per tenant suits short accepted windows, while replication machinery or dual writes add complexity the schedule does not require.
- **C:** Correct. A bulk load followed by a catch-up pass for the writes made during the load. In this case: Repeated dump and restore per tenant suits short accepted windows, while replication machinery or dual writes add complexity the schedule does not require.
- **D:** Incorrect for this question. Stop application writes so the last increment can be applied cleanly. Why the correct answer wins: Repeated dump and restore per tenant suits short accepted windows, while replication machinery or dual writes add complexity the schedule does not require.

### Question 60 — A

Answer: Follow a cutover runbook with a rollback step. A rehearsed runbook with named decision points and a rollback step tells whoever is on call exactly what to do without judgement in the moment. A rehearsed sequence with a named decision point and a way back. Local study-map skill 3.1 (Migration Strategy and Downtime Budget), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 3 (migrate data solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Correct. A rehearsed sequence with a named decision point and a way back. In this case: A rehearsed runbook with named decision points and a rollback step tells whoever is on call exactly what to do without judgement in the moment.
- **B:** Incorrect for this question. Keep two databases current from application code during the transition. Why the correct answer wins: A rehearsed runbook with named decision points and a rollback step tells whoever is on call exactly what to do without judgement in the moment.
- **C:** Incorrect for this question. Stop the source, load everything, and start the target in one window. Why the correct answer wins: A rehearsed runbook with named decision points and a rollback step tells whoever is on call exactly what to do without judgement in the moment.
- **D:** Incorrect for this question. Stop application writes so the last increment can be applied cleanly. Why the correct answer wins: A rehearsed runbook with named decision points and a rollback step tells whoever is on call exactly what to do without judgement in the moment.

### Question 61 — B, C

Answers: Use Database Migration Service for the same engine; Apply the captured change backlog before cutover. A same-engine managed migration moves the data, and applying the captured backlog brings the target level with the writes made during the load. A managed migration that moves a supported engine to the same engine on Google Cloud. Replay the writes made during the bulk load so the target is current at the switch. Local study-map skill 3.2 (Migration Tool Selection), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 3 (migrate data solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Convert DDL and code with reviewable, editable output before the load starts. Why the correct answer wins: A same-engine managed migration moves the data, and applying the captured backlog brings the target level with the writes made during the load.
- **B:** Correct. A managed migration that moves a supported engine to the same engine on Google Cloud. In this case: A same-engine managed migration moves the data, and applying the captured backlog brings the target level with the writes made during the load.
- **C:** Correct. Replay the writes made during the bulk load so the target is current at the switch. In this case: A same-engine managed migration moves the data, and applying the captured backlog brings the target level with the writes made during the load.
- **D:** Incorrect for this question. A bulk load followed by a catch-up pass for the writes made during the load. Why the correct answer wins: A same-engine managed migration moves the data, and applying the captured backlog brings the target level with the writes made during the load.
- **E:** Incorrect for this question. Keep two databases current from application code during the transition. Why the correct answer wins: A same-engine managed migration moves the data, and applying the captured backlog brings the target level with the writes made during the load.

### Question 62 — B

Answer: Stream changes with Datastream. Change data capture streams the changes into multiple destinations, while migration tools and one-off exports are built for a single move. Change data capture from the source into a Google Cloud target. Local study-map skill 3.2 (Migration Tool Selection), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 3 (migrate data solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A portable SQL dump taken with the engine tooling. Why the correct answer wins: Change data capture streams the changes into multiple destinations, while migration tools and one-off exports are built for a single move.
- **B:** Correct. Change data capture from the source into a Google Cloud target. In this case: Change data capture streams the changes into multiple destinations, while migration tools and one-off exports are built for a single move.
- **C:** Incorrect for this question. Copy the analytical slice into the warehouse on a schedule. Why the correct answer wins: Change data capture streams the changes into multiple destinations, while migration tools and one-off exports are built for a single move.
- **D:** Incorrect for this question. A managed migration that moves a supported engine to the same engine on Google Cloud. Why the correct answer wins: Change data capture streams the changes into multiple destinations, while migration tools and one-off exports are built for a single move.

### Question 63 — B

Answer: Use Database Migration Service with schema conversion. The cross-engine migration path pairs schema conversion with managed replication, which a same-engine move or a manual dump cannot provide. A managed path that converts schema and code from a different source engine. Local study-map skill 3.2 (Migration Tool Selection), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 3 (migrate data solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A bulk load followed by a catch-up pass for the writes made during the load. Why the correct answer wins: The cross-engine migration path pairs schema conversion with managed replication, which a same-engine move or a manual dump cannot provide.
- **B:** Correct. A managed path that converts schema and code from a different source engine. In this case: The cross-engine migration path pairs schema conversion with managed replication, which a same-engine move or a manual dump cannot provide.
- **C:** Incorrect for this question. A managed migration that moves a supported engine to the same engine on Google Cloud. Why the correct answer wins: The cross-engine migration path pairs schema conversion with managed replication, which a same-engine move or a manual dump cannot provide.
- **D:** Incorrect for this question. Keep two databases current from application code during the transition. Why the correct answer wins: The cross-engine migration path pairs schema conversion with managed replication, which a same-engine move or a manual dump cannot provide.

### Question 64 — D

Answer: Rewrite the stored procedures and DML by hand. Procedural code with no target equivalent has to be rewritten by hand, which no conversion setting or sequence fix can substitute. Port procedural code the conversion tool flags as unsupported. Local study-map skill 3.3 (Heterogeneous Schema and DDL Conversion), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 3 (migrate data solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Set generated-key counters past the highest value so inserts do not collide. Why the correct answer wins: Procedural code with no target equivalent has to be rewritten by hand, which no conversion setting or sequence fix can substitute.
- **B:** Incorrect for this question. Convert DDL and code with reviewable, editable output before the load starts. Why the correct answer wins: Procedural code with no target equivalent has to be rewritten by hand, which no conversion setting or sequence fix can substitute.
- **C:** Incorrect for this question. Keep two databases current from application code during the transition. Why the correct answer wins: Procedural code with no target equivalent has to be rewritten by hand, which no conversion setting or sequence fix can substitute.
- **D:** Correct. Port procedural code the conversion tool flags as unsupported. In this case: Procedural code with no target equivalent has to be rewritten by hand, which no conversion setting or sequence fix can substitute.

### Question 65 — B

Answer: Build the schema in a conversion workspace. Editing the conversion output lets the team reorder objects and apply the corrected script, rather than patching the live database afterwards. Convert DDL and code with reviewable, editable output before the load starts. Local study-map skill 3.3 (Heterogeneous Schema and DDL Conversion), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 3 (migrate data solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Port procedural code the conversion tool flags as unsupported. Why the correct answer wins: Editing the conversion output lets the team reorder objects and apply the corrected script, rather than patching the live database afterwards.
- **B:** Correct. Convert DDL and code with reviewable, editable output before the load starts. In this case: Editing the conversion output lets the team reorder objects and apply the corrected script, rather than patching the live database afterwards.
- **C:** Incorrect for this question. Prove the target holds the same rows as the source before cutover. Why the correct answer wins: Editing the conversion output lets the team reorder objects and apply the corrected script, rather than patching the live database afterwards.
- **D:** Incorrect for this question. Move clients to the new endpoint as the final cutover action. Why the correct answer wins: Editing the conversion output lets the team reorder objects and apply the corrected script, rather than patching the live database afterwards.

### Question 66 — C

Answer: Rewrite the stored procedures and DML by hand. The statement must be rewritten into a form the target accepts, since no replication or validation step changes the syntax itself. Port procedural code the conversion tool flags as unsupported. Local study-map skill 3.4 (DML and Application Code Conversion), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 3 (migrate data solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Keep two databases current from application code during the transition. Why the correct answer wins: The statement must be rewritten into a form the target accepts, since no replication or validation step changes the syntax itself.
- **B:** Incorrect for this question. Set generated-key counters past the highest value so inserts do not collide. Why the correct answer wins: The statement must be rewritten into a form the target accepts, since no replication or validation step changes the syntax itself.
- **C:** Correct. Port procedural code the conversion tool flags as unsupported. In this case: The statement must be rewritten into a form the target accepts, since no replication or validation step changes the syntax itself.
- **D:** Incorrect for this question. Compare the target answers with production before the switch. Why the correct answer wins: The statement must be rewritten into a form the target accepts, since no replication or validation step changes the syntax itself.

### Question 67 — A

Answer: Replay read traffic against the target. Replaying the real statements and comparing answers exercises the code paths the application actually uses. Compare the target answers with production before the switch. Local study-map skill 3.4 (DML and Application Code Conversion), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 3 (migrate data solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Correct. Compare the target answers with production before the switch. In this case: Replaying the real statements and comparing answers exercises the code paths the application actually uses.
- **B:** Incorrect for this question. Move clients to the new endpoint as the final cutover action. Why the correct answer wins: Replaying the real statements and comparing answers exercises the code paths the application actually uses.
- **C:** Incorrect for this question. Port procedural code the conversion tool flags as unsupported. Why the correct answer wins: Replaying the real statements and comparing answers exercises the code paths the application actually uses.
- **D:** Incorrect for this question. Prove the target holds the same rows as the source before cutover. Why the correct answer wins: Replaying the real statements and comparing answers exercises the code paths the application actually uses.

### Question 68 — A

Answer: Use the engine native logical replication. Replicating the engine's own change stream lets the target catch up continuously, which a dump or a planned outage does not. Replicate row changes from the source using the engine feature itself. Local study-map skill 3.5 (Initial Load and Change Replication), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 3 (migrate data solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Correct. Replicate row changes from the source using the engine feature itself. In this case: Replicating the engine's own change stream lets the target catch up continuously, which a dump or a planned outage does not.
- **B:** Incorrect for this question. Stop the source, load everything, and start the target in one window. Why the correct answer wins: Replicating the engine's own change stream lets the target catch up continuously, which a dump or a planned outage does not.
- **C:** Incorrect for this question. A portable SQL dump taken with the engine tooling. Why the correct answer wins: Replicating the engine's own change stream lets the target catch up continuously, which a dump or a planned outage does not.
- **D:** Incorrect for this question. Keep two databases current from application code during the transition. Why the correct answer wins: Replicating the engine's own change stream lets the target catch up continuously, which a dump or a planned outage does not.

### Question 69 — A

Answer: Measure the catch-up rate before choosing the window. The observed replay rate against the backlog shows whether the window can hold, which the other options assume rather than measure. Size the cutover from how fast changes replay, not from the data volume alone. Local study-map skill 3.5 (Initial Load and Change Replication), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 3 (migrate data solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Correct. Size the cutover from how fast changes replay, not from the data volume alone. In this case: The observed replay rate against the backlog shows whether the window can hold, which the other options assume rather than measure.
- **B:** Incorrect for this question. Stop application writes so the last increment can be applied cleanly. Why the correct answer wins: The observed replay rate against the backlog shows whether the window can hold, which the other options assume rather than measure.
- **C:** Incorrect for this question. Prove the target holds the same rows as the source before cutover. Why the correct answer wins: The observed replay rate against the backlog shows whether the window can hold, which the other options assume rather than measure.
- **D:** Incorrect for this question. Replay the writes made during the bulk load so the target is current at the switch. Why the correct answer wins: The observed replay rate against the backlog shows whether the window can hold, which the other options assume rather than measure.

### Question 70 — A, B

Answers: Reconcile row counts and checksums; Replay read traffic against the target. Comparing row counts and checksums catches missing or altered data, and replaying production statements catches behaviour that changed even when the data matches. Prove the target holds the same rows as the source before cutover. Compare the target answers with production before the switch. Local study-map skill 3.6 (Validation and Reconciliation), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 3 (migrate data solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Correct. Compare the target answers with production before the switch. In this case: Comparing row counts and checksums catches missing or altered data, and replaying production statements catches behaviour that changed even when the data matches.
- **B:** Correct. Prove the target holds the same rows as the source before cutover. In this case: Comparing row counts and checksums catches missing or altered data, and replaying production statements catches behaviour that changed even when the data matches.
- **C:** Incorrect for this question. Move clients to the new endpoint as the final cutover action. Why the correct answer wins: Comparing row counts and checksums catches missing or altered data, and replaying production statements catches behaviour that changed even when the data matches.
- **D:** Incorrect for this question. Set generated-key counters past the highest value so inserts do not collide. Why the correct answer wins: Comparing row counts and checksums catches missing or altered data, and replaying production statements catches behaviour that changed even when the data matches.
- **E:** Incorrect for this question. A rehearsed sequence with a named decision point and a way back. Why the correct answer wins: Comparing row counts and checksums catches missing or altered data, and replaying production statements catches behaviour that changed even when the data matches.

### Question 71 — D

Answer: Run the task on a managed schedule. A managed schedule repeats the validation without an operator, which no single comparison or switch action provides. A recurring trigger that performs the work with nobody present. Local study-map skill 3.6 (Validation and Reconciliation), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 3 (migrate data solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Prove the target holds the same rows as the source before cutover. Why the correct answer wins: A managed schedule repeats the validation without an operator, which no single comparison or switch action provides.
- **B:** Incorrect for this question. Move clients to the new endpoint as the final cutover action. Why the correct answer wins: A managed schedule repeats the validation without an operator, which no single comparison or switch action provides.
- **C:** Incorrect for this question. Compare the target answers with production before the switch. Why the correct answer wins: A managed schedule repeats the validation without an operator, which no single comparison or switch action provides.
- **D:** Correct. A recurring trigger that performs the work with nobody present. In this case: A managed schedule repeats the validation without an operator, which no single comparison or switch action provides.

### Question 72 — D

Answer: Follow a cutover runbook with a rollback step. The rehearsed runbook states the threshold and the rollback step, so the call is made on the documented rule rather than under pressure. A rehearsed sequence with a named decision point and a way back. Local study-map skill 3.7 (Cutover and Fallback Planning), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 3 (migrate data solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Stop application writes so the last increment can be applied cleanly. Why the correct answer wins: The rehearsed runbook states the threshold and the rollback step, so the call is made on the documented rule rather than under pressure.
- **B:** Incorrect for this question. Keep two databases current from application code during the transition. Why the correct answer wins: The rehearsed runbook states the threshold and the rollback step, so the call is made on the documented rule rather than under pressure.
- **C:** Incorrect for this question. Move clients to the new endpoint as the final cutover action. Why the correct answer wins: The rehearsed runbook states the threshold and the rollback step, so the call is made on the documented rule rather than under pressure.
- **D:** Correct. A rehearsed sequence with a named decision point and a way back. In this case: The rehearsed runbook states the threshold and the rollback step, so the call is made on the documented rule rather than under pressure.

### Question 73 — C

Answer: Freeze writes during the cutover. Application and batch writes have to stop on the source so the last increment is complete and stable before the switch. Stop application writes so the last increment can be applied cleanly. Local study-map skill 3.7 (Cutover and Fallback Planning), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 3 (migrate data solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Stop the source, load everything, and start the target in one window. Why the correct answer wins: Application and batch writes have to stop on the source so the last increment is complete and stable before the switch.
- **B:** Incorrect for this question. Move clients to the new endpoint as the final cutover action. Why the correct answer wins: Application and batch writes have to stop on the source so the last increment is complete and stable before the switch.
- **C:** Correct. Stop application writes so the last increment can be applied cleanly. In this case: Application and batch writes have to stop on the source so the last increment is complete and stable before the switch.
- **D:** Incorrect for this question. Keep writing back to the original system so a rollback loses nothing. Why the correct answer wins: Application and batch writes have to stop on the source so the last increment is complete and stable before the switch.

### Question 74 — C

Answer: Repoint the connection string at the target. Repointing the connection string at the validated target moves the clients, and the cached record then expires on its own. Move clients to the new endpoint as the final cutover action. Local study-map skill 3.7 (Cutover and Fallback Planning), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 3 (migrate data solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Stop application writes so the last increment can be applied cleanly. Why the correct answer wins: Repointing the connection string at the validated target moves the clients, and the cached record then expires on its own.
- **B:** Incorrect for this question. A client library that resolves the instance and authorizes the connection with IAM. Why the correct answer wins: Repointing the connection string at the validated target moves the clients, and the cached record then expires on its own.
- **C:** Correct. Move clients to the new endpoint as the final cutover action. In this case: Repointing the connection string at the validated target moves the clients, and the cached record then expires on its own.
- **D:** Incorrect for this question. A rehearsed sequence with a named decision point and a way back. Why the correct answer wins: Repointing the connection string at the validated target moves the clients, and the cached record then expires on its own.

### Question 75 — C

Answer: Set up reverse replication to the source. Replication from the target back to the source publishes the new writes where the old system can see them. Keep writing back to the original system so a rollback loses nothing. Local study-map skill 3.8 (Reverse Replication to the Source), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 3 (migrate data solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Keep two databases current from application code during the transition. Why the correct answer wins: Replication from the target back to the source publishes the new writes where the old system can see them.
- **B:** Incorrect for this question. Move clients to the new endpoint as the final cutover action. Why the correct answer wins: Replication from the target back to the source publishes the new writes where the old system can see them.
- **C:** Correct. Keep writing back to the original system so a rollback loses nothing. In this case: Replication from the target back to the source publishes the new writes where the old system can see them.
- **D:** Incorrect for this question. Keep the old system read-only for a defined period, then remove it. Why the correct answer wins: Replication from the target back to the source publishes the new writes where the old system can see them.

### Question 76 — A

Answer: Decommission the source after a parallel period. A parallel period with an end date and exit criteria tells everyone when the fallback stops being needed. Keep the old system read-only for a defined period, then remove it. Local study-map skill 3.8 (Reverse Replication to the Source), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 3 (migrate data solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Correct. Keep the old system read-only for a defined period, then remove it. In this case: A parallel period with an end date and exit criteria tells everyone when the fallback stops being needed.
- **B:** Incorrect for this question. Move clients to the new endpoint as the final cutover action. Why the correct answer wins: A parallel period with an end date and exit criteria tells everyone when the fallback stops being needed.
- **C:** Incorrect for this question. Check the connection and traffic evidence before retiring an instance. Why the correct answer wins: A parallel period with an end date and exit criteria tells everyone when the fallback stops being needed.
- **D:** Incorrect for this question. Keep writing back to the original system so a rollback loses nothing. Why the correct answer wins: A parallel period with an end date and exit criteria tells everyone when the fallback stops being needed.

### Question 77 — A, C

Answers: Use the engine native logical replication; Apply the captured change backlog before cutover. Replicating changes continuously and applying the remaining backlog is what reduces the outage to the final switch, which a dump or an accepted window cannot. Replicate row changes from the source using the engine feature itself. Replay the writes made during the bulk load so the target is current at the switch. Local study-map skill 3.9 (Minimizing Downtime During Migration), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 3 (migrate data solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Correct. Replicate row changes from the source using the engine feature itself. In this case: Replicating changes continuously and applying the remaining backlog is what reduces the outage to the final switch, which a dump or an accepted window cannot.
- **B:** Incorrect for this question. Keep two databases current from application code during the transition. Why the correct answer wins: Replicating changes continuously and applying the remaining backlog is what reduces the outage to the final switch, which a dump or an accepted window cannot.
- **C:** Correct. Replay the writes made during the bulk load so the target is current at the switch. In this case: Replicating changes continuously and applying the remaining backlog is what reduces the outage to the final switch, which a dump or an accepted window cannot.
- **D:** Incorrect for this question. Stop the source, load everything, and start the target in one window. Why the correct answer wins: Replicating changes continuously and applying the remaining backlog is what reduces the outage to the final switch, which a dump or an accepted window cannot.
- **E:** Incorrect for this question. A bulk load followed by a catch-up pass for the writes made during the load. Why the correct answer wins: Replicating changes continuously and applying the remaining backlog is what reduces the outage to the final switch, which a dump or an accepted window cannot.

### Question 78 — D

Answer: Set up reverse replication to the source. Replication back to the source keeps the rollback path alive, so an abandoned cutover does not force a second full load. Keep writing back to the original system so a rollback loses nothing. Local study-map skill 3.9 (Minimizing Downtime During Migration), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 3 (migrate data solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Replay the writes made during the bulk load so the target is current at the switch. Why the correct answer wins: Replication back to the source keeps the rollback path alive, so an abandoned cutover does not force a second full load.
- **B:** Incorrect for this question. Stop application writes so the last increment can be applied cleanly. Why the correct answer wins: Replication back to the source keeps the rollback path alive, so an abandoned cutover does not force a second full load.
- **C:** Incorrect for this question. A portable SQL dump taken with the engine tooling. Why the correct answer wins: Replication back to the source keeps the rollback path alive, so an abandoned cutover does not force a second full load.
- **D:** Correct. Keep writing back to the original system so a rollback loses nothing. In this case: Replication back to the source keeps the rollback path alive, so an abandoned cutover does not force a second full load.

### Question 79 — C

Answer: Export the table into BigQuery. Copying the retained history into the warehouse keeps it queryable after the engine is gone, which source-side options cannot do. Copy the analytical slice into the warehouse on a schedule. Local study-map skill 3.10 (Source Decommissioning), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 3 (migrate data solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Interconnect the remaining on-premises system rather than moving it. Why the correct answer wins: Copying the retained history into the warehouse keeps it queryable after the engine is gone, which source-side options cannot do.
- **B:** Incorrect for this question. Keep the old system read-only for a defined period, then remove it. Why the correct answer wins: Copying the retained history into the warehouse keeps it queryable after the engine is gone, which source-side options cannot do.
- **C:** Correct. Copy the analytical slice into the warehouse on a schedule. In this case: Copying the retained history into the warehouse keeps it queryable after the engine is gone, which source-side options cannot do.
- **D:** Incorrect for this question. Keep writing back to the original system so a rollback loses nothing. Why the correct answer wins: Copying the retained history into the warehouse keeps it queryable after the engine is gone, which source-side options cannot do.

### Question 80 — C

Answer: Confirm no client still uses the old endpoint. Connection and traffic evidence shows whether any client still uses the endpoint, which the retirement step itself would assume. Check the connection and traffic evidence before retiring an instance. Local study-map skill 3.10 (Source Decommissioning), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 3 (migrate data solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Prove the target holds the same rows as the source before cutover. Why the correct answer wins: Connection and traffic evidence shows whether any client still uses the endpoint, which the retirement step itself would assume.
- **B:** Incorrect for this question. Move clients to the new endpoint as the final cutover action. Why the correct answer wins: Connection and traffic evidence shows whether any client still uses the endpoint, which the retirement step itself would assume.
- **C:** Correct. Check the connection and traffic evidence before retiring an instance. In this case: Connection and traffic evidence shows whether any client still uses the endpoint, which the retirement step itself would assume.
- **D:** Incorrect for this question. Keep the old system read-only for a defined period, then remove it. Why the correct answer wins: Connection and traffic evidence shows whether any client still uses the endpoint, which the retirement step itself would assume.

### Question 81 — D

Answer: Provision the instance with a Terraform module. The declared module reproduces the estate from one definition, while manual creation, a restore, or a clone covers only part of the problem. Declare the database so the same definition creates every environment. Local study-map skill 4.1 (Provisioning Highly Available Instances), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 4 (deploy scalable and highly available databases in Google Cloud): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Rebuild the database in the surviving region from the latest backup. Why the correct answer wins: The declared module reproduces the estate from one definition, while manual creation, a restore, or a clone covers only part of the problem.
- **B:** Incorrect for this question. A copy of the current data created without touching the source. Why the correct answer wins: The declared module reproduces the estate from one definition, while manual creation, a restore, or a clone covers only part of the problem.
- **C:** Incorrect for this question. Create the resource interactively with no stored definition. Why the correct answer wins: The declared module reproduces the estate from one definition, while manual creation, a restore, or a clone covers only part of the problem.
- **D:** Correct. Declare the database so the same definition creates every environment. In this case: The declared module reproduces the estate from one definition, while manual creation, a restore, or a clone covers only part of the problem.

### Question 82 — B

Answer: Apply the change through the infrastructure pipeline. Applying database configuration through the pipeline removes hand edits and records every change, so the environments cannot drift silently. Send database changes through review and version control like any other code. Local study-map skill 4.1 (Provisioning Highly Available Instances), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 4 (deploy scalable and highly available databases in Google Cloud): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A single view of health, security, and version posture across database instances. Why the correct answer wins: Applying database configuration through the pipeline removes hand edits and records every change, so the environments cannot drift silently.
- **B:** Correct. Send database changes through review and version control like any other code. In this case: Applying database configuration through the pipeline removes hand edits and records every change, so the environments cannot drift silently.
- **C:** Incorrect for this question. Rehearse the change against a copy before touching production. Why the correct answer wins: Applying database configuration through the pipeline removes hand edits and records every change, so the environments cannot drift silently.
- **D:** Incorrect for this question. Create the resource interactively with no stored definition. Why the correct answer wins: Applying database configuration through the pipeline removes hand edits and records every change, so the environments cannot drift silently.

### Question 83 — A

Answer: Provision the instance with a Terraform module. A parameterised module applies the same replica definition everywhere, which repeated manual work cannot sustain at that volume. Declare the database so the same definition creates every environment. Local study-map skill 4.1 (Provisioning Highly Available Instances), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 4 (deploy scalable and highly available databases in Google Cloud): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Correct. Declare the database so the same definition creates every environment. In this case: A parameterised module applies the same replica definition everywhere, which repeated manual work cannot sustain at that volume.
- **B:** Incorrect for this question. Create the resource interactively with no stored definition. Why the correct answer wins: A parameterised module applies the same replica definition everywhere, which repeated manual work cannot sustain at that volume.
- **C:** Incorrect for this question. Run the new version beside the old one and move traffic when it is proven. Why the correct answer wins: A parameterised module applies the same replica definition everywhere, which repeated manual work cannot sustain at that volume.
- **D:** Incorrect for this question. A recovery point that makes the upgrade reversible in practice. Why the correct answer wins: A parameterised module applies the same replica definition everywhere, which repeated manual work cannot sustain at that volume.

### Question 84 — D

Answer: Rehearse the promotion in a test project. Promoting the replica and timing the write path demonstrates the recovery objective for a regional loss. Practise the failover that the runbook would perform for real. Local study-map skill 4.2 (Testing High Availability and Disaster Recovery), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 4 (deploy scalable and highly available databases in Google Cloud): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Compare the signal after cutover against the pre-change baseline. Why the correct answer wins: Promoting the replica and timing the write path demonstrates the recovery objective for a regional loss.
- **B:** Incorrect for this question. Trigger a switchover in a test window and observe how long writes are unavailable. Why the correct answer wins: Promoting the replica and timing the write path demonstrates the recovery objective for a regional loss.
- **C:** Incorrect for this question. A recovery point that makes the upgrade reversible in practice. Why the correct answer wins: Promoting the replica and timing the write path demonstrates the recovery objective for a regional loss.
- **D:** Correct. Practise the failover that the runbook would perform for real. In this case: Promoting the replica and timing the write path demonstrates the recovery objective for a regional loss.

### Question 85 — B

Answer: Run a controlled failover test. A controlled failover exercises the application's reconnect path, which an alert, a dashboard, or a backup cannot prove. Trigger a switchover in a test window and observe how long writes are unavailable. Local study-map skill 4.2 (Testing High Availability and Disaster Recovery), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 4 (deploy scalable and highly available databases in Google Cloud): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A liveness signal that fires before users report the outage. Why the correct answer wins: A controlled failover exercises the application's reconnect path, which an alert, a dashboard, or a backup cannot prove.
- **B:** Correct. Trigger a switchover in a test window and observe how long writes are unavailable. In this case: A controlled failover exercises the application's reconnect path, which an alert, a dashboard, or a backup cannot prove.
- **C:** Incorrect for this question. A recovery point that makes the upgrade reversible in practice. Why the correct answer wins: A controlled failover exercises the application's reconnect path, which an alert, a dashboard, or a backup cannot prove.
- **D:** Incorrect for this question. Compare the signal after cutover against the pre-change baseline. Why the correct answer wins: A controlled failover exercises the application's reconnect path, which an alert, a dashboard, or a backup cannot prove.

### Question 86 — D

Answer: Restore the backup into the second region. Restoring into the second region exercises the recovery path without waiting for a real outage, and it measures the time the plan claims. Rebuild the database in the surviving region from the latest backup. Local study-map skill 4.2 (Testing High Availability and Disaster Recovery), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 4 (deploy scalable and highly available databases in Google Cloud): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Practise the failover that the runbook would perform for real. Why the correct answer wins: Restoring into the second region exercises the recovery path without waiting for a real outage, and it measures the time the plan claims.
- **B:** Incorrect for this question. A recovery point that makes the upgrade reversible in practice. Why the correct answer wins: Restoring into the second region exercises the recovery path without waiting for a real outage, and it measures the time the plan claims.
- **C:** Incorrect for this question. Trigger a switchover in a test window and observe how long writes are unavailable. Why the correct answer wins: Restoring into the second region exercises the recovery path without waiting for a real outage, and it measures the time the plan claims.
- **D:** Correct. Rebuild the database in the surviving region from the latest backup. In this case: Restoring into the second region exercises the recovery path without waiting for a real outage, and it measures the time the plan claims.

### Question 87 — A, D

Answers: Choose a multi-region instance configuration; Add a read-only region to the configuration. The multi-region configuration provides the replicated write placement, and a read-only region adds local read capacity without touching write leadership. A topology that places replicas in separate regions for regional-failure tolerance. Serve reads near users without making the region a write leader. Local study-map skill 4.3 (Multi-Regional Replication Setup), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 4 (deploy scalable and highly available databases in Google Cloud): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Correct. Serve reads near users without making the region a write leader. In this case: The multi-region configuration provides the replicated write placement, and a read-only region adds local read capacity without touching write leadership.
- **B:** Incorrect for this question. A primary and standby in two zones of one region with automatic failover. Why the correct answer wins: The multi-region configuration provides the replicated write placement, and a read-only region adds local read capacity without touching write leadership.
- **C:** Incorrect for this question. A copy in a second region that serves reads and can be promoted. Why the correct answer wins: The multi-region configuration provides the replicated write placement, and a read-only region adds local read capacity without touching write leadership.
- **D:** Correct. A topology that places replicas in separate regions for regional-failure tolerance. In this case: The multi-region configuration provides the replicated write placement, and a read-only region adds local read capacity without touching write leadership.
- **E:** Incorrect for this question. An AlloyDB cross-region copy that can be promoted to a primary cluster. Why the correct answer wins: The multi-region configuration provides the replicated write placement, and a read-only region adds local read capacity without touching write leadership.

### Question 88 — B

Answer: Add a cross-region read replica. A cross-region replica continuously ships changes to the second region, where reporting can read them. A copy in a second region that serves reads and can be promoted. Local study-map skill 4.3 (Multi-Regional Replication Setup), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 4 (deploy scalable and highly available databases in Google Cloud): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Rebuild the database in the surviving region from the latest backup. Why the correct answer wins: A cross-region replica continuously ships changes to the second region, where reporting can read them.
- **B:** Correct. A copy in a second region that serves reads and can be promoted. In this case: A cross-region replica continuously ships changes to the second region, where reporting can read them.
- **C:** Incorrect for this question. A topology that places replicas in separate regions for regional-failure tolerance. Why the correct answer wins: A cross-region replica continuously ships changes to the second region, where reporting can read them.
- **D:** Incorrect for this question. An AlloyDB cross-region copy that can be promoted to a primary cluster. Why the correct answer wins: A cross-region replica continuously ships changes to the second region, where reporting can read them.

### Question 89 — C

Answer: Add a secondary cluster in the second region. A secondary cluster serves reads and can become the primary, which a read pool or a restore cannot do. An AlloyDB cross-region copy that can be promoted to a primary cluster. Local study-map skill 4.3 (Multi-Regional Replication Setup), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 4 (deploy scalable and highly available databases in Google Cloud): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Rebuild the database in the surviving region from the latest backup. Why the correct answer wins: A secondary cluster serves reads and can become the primary, which a read pool or a restore cannot do.
- **B:** Incorrect for this question. Grow the AlloyDB read pool that serves read-only connections. Why the correct answer wins: A secondary cluster serves reads and can become the primary, which a read pool or a restore cannot do.
- **C:** Correct. An AlloyDB cross-region copy that can be promoted to a primary cluster. In this case: A secondary cluster serves reads and can become the primary, which a read pool or a restore cannot do.
- **D:** Incorrect for this question. One instance in one zone with no standby, so a zone failure stops writes. Why the correct answer wins: A secondary cluster serves reads and can become the primary, which a read pool or a restore cannot do.

### Question 90 — D

Answer: Add nodes to the read pool. Adding read-pool nodes adds capacity exactly where the load is concentrated. Grow the AlloyDB read pool that serves read-only connections. Local study-map skill 4.4 (Read Replicas and Read Pools), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 4 (deploy scalable and highly available databases in Google Cloud): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Move the instance to a larger shape so more vCPU and memory serve the same data. Why the correct answer wins: Adding read-pool nodes adds capacity exactly where the load is concentrated.
- **B:** Incorrect for this question. Separate analytical reads from the write path. Why the correct answer wins: Adding read-pool nodes adds capacity exactly where the load is concentrated.
- **C:** Incorrect for this question. Absorb repeated reads in memory so the database sees fewer of them. Why the correct answer wins: Adding read-pool nodes adds capacity exactly where the load is concentrated.
- **D:** Correct. Grow the AlloyDB read pool that serves read-only connections. In this case: Adding read-pool nodes adds capacity exactly where the load is concentrated.

### Question 91 — D

Answer: Send reporting queries to the read replica. Directing read traffic to the idle replica uses capacity that is already provisioned and paid for. Separate analytical reads from the write path. Local study-map skill 4.4 (Read Replicas and Read Pools), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 4 (deploy scalable and highly available databases in Google Cloud): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Move the instance to a larger shape so more vCPU and memory serve the same data. Why the correct answer wins: Directing read traffic to the idle replica uses capacity that is already provisioned and paid for.
- **B:** Incorrect for this question. Absorb repeated reads in memory so the database sees fewer of them. Why the correct answer wins: Directing read traffic to the idle replica uses capacity that is already provisioned and paid for.
- **C:** Incorrect for this question. Send reads to a copy so the primary keeps its capacity for writes. Why the correct answer wins: Directing read traffic to the idle replica uses capacity that is already provisioned and paid for.
- **D:** Correct. Separate analytical reads from the write path. In this case: Directing read traffic to the idle replica uses capacity that is already provisioned and paid for.

### Question 92 — D

Answer: Provision the instance with a Terraform module. A parameterised module creates each instance from one reviewed definition, which manual creation cannot do reliably at that scale. Declare the database so the same definition creates every environment. Local study-map skill 4.5 (Automating Database Provisioning), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 4 (deploy scalable and highly available databases in Google Cloud): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A single view of health, security, and version posture across database instances. Why the correct answer wins: A parameterised module creates each instance from one reviewed definition, which manual creation cannot do reliably at that scale.
- **B:** Incorrect for this question. Create the resource interactively with no stored definition. Why the correct answer wins: A parameterised module creates each instance from one reviewed definition, which manual creation cannot do reliably at that scale.
- **C:** Incorrect for this question. Rehearse the change against a copy before touching production. Why the correct answer wins: A parameterised module creates each instance from one reviewed definition, which manual creation cannot do reliably at that scale.
- **D:** Correct. Declare the database so the same definition creates every environment. In this case: A parameterised module creates each instance from one reviewed definition, which manual creation cannot do reliably at that scale.

### Question 93 — D

Answer: Apply the change through the infrastructure pipeline. Validation inside the pipeline blocks the change before it reaches the database, which manual checks and one-off tools cannot guarantee. Send database changes through review and version control like any other code. Local study-map skill 4.5 (Automating Database Provisioning), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 4 (deploy scalable and highly available databases in Google Cloud): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Create the resource interactively with no stored definition. Why the correct answer wins: Validation inside the pipeline blocks the change before it reaches the database, which manual checks and one-off tools cannot guarantee.
- **B:** Incorrect for this question. A recovery point that makes the upgrade reversible in practice. Why the correct answer wins: Validation inside the pipeline blocks the change before it reaches the database, which manual checks and one-off tools cannot guarantee.
- **C:** Incorrect for this question. A copy of the current data created without touching the source. Why the correct answer wins: Validation inside the pipeline blocks the change before it reaches the database, which manual checks and one-off tools cannot guarantee.
- **D:** Correct. Send database changes through review and version control like any other code. In this case: Validation inside the pipeline blocks the change before it reaches the database, which manual checks and one-off tools cannot guarantee.

### Question 94 — B, E

Answers: Create an alerting policy on the metric; Alert when the instance is unreachable. An alert on the failover signal reports the event, and a query probe confirms that the instance actually serves traffic after it. A condition that pages a human when the threshold is crossed. A liveness signal that fires before users report the outage. Local study-map skill 4.6 (Monitoring Highly Available Databases), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 4 (deploy scalable and highly available databases in Google Cloud): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A single view of health, security, and version posture across database instances. Why the correct answer wins: An alert on the failover signal reports the event, and a query probe confirms that the instance actually serves traffic after it.
- **B:** Correct. A liveness signal that fires before users report the outage. In this case: An alert on the failover signal reports the event, and a query probe confirms that the instance actually serves traffic after it.
- **C:** Incorrect for this question. Read the instance-level signals before attributing the symptom to the query. Why the correct answer wins: An alert on the failover signal reports the event, and a query probe confirms that the instance actually serves traffic after it.
- **D:** Incorrect for this question. A per-query view of latency, load, and wait events on the instance. Why the correct answer wins: An alert on the failover signal reports the event, and a query probe confirms that the instance actually serves traffic after it.
- **E:** Correct. A condition that pages a human when the threshold is crossed. In this case: An alert on the failover signal reports the event, and a query probe confirms that the instance actually serves traffic after it.

### Question 95 — C

Answer: Review the fleet in Database Center. The fleet view aggregates health and posture across instances, which single-instance dashboards and query tools do not. A single view of health, security, and version posture across database instances. Local study-map skill 4.6 (Monitoring Highly Available Databases), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 4 (deploy scalable and highly available databases in Google Cloud): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Read the instance-level signals before attributing the symptom to the query. Why the correct answer wins: The fleet view aggregates health and posture across instances, which single-instance dashboards and query tools do not.
- **B:** Incorrect for this question. The engine log of statements that exceeded the long-query threshold. Why the correct answer wins: The fleet view aggregates health and posture across instances, which single-instance dashboards and query tools do not.
- **C:** Correct. A single view of health, security, and version posture across database instances. In this case: The fleet view aggregates health and posture across instances, which single-instance dashboards and query tools do not.
- **D:** Incorrect for this question. A per-query view of latency, load, and wait events on the instance. Why the correct answer wins: The fleet view aggregates health and posture across instances, which single-instance dashboards and query tools do not.

### Question 96 — A

Answer: Promote the cross-region replica during the outage. Promotion keeps the replica's recent writes and avoids the data loss a restore would introduce. Turn the replica into an independent primary so the application can resume writes. Local study-map skill 4.7 (Regional Failover Mechanics), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 4 (deploy scalable and highly available databases in Google Cloud): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Correct. Turn the replica into an independent primary so the application can resume writes. In this case: Promotion keeps the replica's recent writes and avoids the data loss a restore would introduce.
- **B:** Incorrect for this question. Rebuild the database in the surviving region from the latest backup. Why the correct answer wins: Promotion keeps the replica's recent writes and avoids the data loss a restore would introduce.
- **C:** Incorrect for this question. A point-in-time restore that discards the later writes on the same instance. Why the correct answer wins: Promotion keeps the replica's recent writes and avoids the data loss a restore would introduce.
- **D:** Incorrect for this question. Stop the former primary from accepting writes so two instances cannot both claim the role. Why the correct answer wins: Promotion keeps the replica's recent writes and avoids the data loss a restore would introduce.

### Question 97 — B

Answer: Fence the old primary before promotion. The old primary has to be prevented from accepting writes so the deployment does not end up with two primaries. Stop the former primary from accepting writes so two instances cannot both claim the role. Local study-map skill 4.7 (Regional Failover Mechanics), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 4 (deploy scalable and highly available databases in Google Cloud): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Stop application writes so the last increment can be applied cleanly. Why the correct answer wins: The old primary has to be prevented from accepting writes so the deployment does not end up with two primaries.
- **B:** Correct. Stop the former primary from accepting writes so two instances cannot both claim the role. In this case: The old primary has to be prevented from accepting writes so the deployment does not end up with two primaries.
- **C:** Incorrect for this question. A rehearsed sequence with a named decision point and a way back. Why the correct answer wins: The old primary has to be prevented from accepting writes so the deployment does not end up with two primaries.
- **D:** Incorrect for this question. Keep writing back to the original system so a rollback loses nothing. Why the correct answer wins: The old primary has to be prevented from accepting writes so the deployment does not end up with two primaries.

### Question 98 — B

Answer: Use the language connector with IAM credentials. The language connector resolves the instance on each connection, so clients follow the current primary instead of a cached address. A client library that resolves the instance and authorizes the connection with IAM. Local study-map skill 4.8 (Connection Routing and Load Balancing), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 4 (deploy scalable and highly available databases in Google Cloud): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Move clients to the new endpoint as the final cutover action. Why the correct answer wins: The language connector resolves the instance on each connection, so clients follow the current primary instead of a cached address.
- **B:** Correct. A client library that resolves the instance and authorizes the connection with IAM. In this case: The language connector resolves the instance on each connection, so clients follow the current primary instead of a cached address.
- **C:** Incorrect for this question. A pooler that multiplexes many application connections onto few database sessions. Why the correct answer wins: The language connector resolves the instance on each connection, so clients follow the current primary instead of a cached address.
- **D:** Incorrect for this question. A public-IP allowlist that admits the caller range. Why the correct answer wins: The language connector resolves the instance on each connection, so clients follow the current primary instead of a cached address.

### Question 99 — B

Answer: Reserve headroom above the measured peak. The standby has to hold the peak plus the load of the instance it replaces, so headroom above that peak is the sizing basis. Keep spare capacity so a failover or a traffic spike does not saturate the instance. Local study-map skill 4.9 (Failover Capacity Headroom), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 4 (deploy scalable and highly available databases in Google Cloud): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Shrink an instance whose peak fits a smaller shape. Why the correct answer wins: The standby has to hold the peak plus the load of the instance it replaces, so headroom above that peak is the sizing basis.
- **B:** Correct. Keep spare capacity so a failover or a traffic spike does not saturate the instance. In this case: The standby has to hold the peak plus the load of the instance it replaces, so headroom above that peak is the sizing basis.
- **C:** Incorrect for this question. Send reads to a copy so the primary keeps its capacity for writes. Why the correct answer wins: The standby has to hold the peak plus the load of the instance it replaces, so headroom above that peak is the sizing basis.
- **D:** Incorrect for this question. Match capacity to the daily traffic shape. Why the correct answer wins: The standby has to hold the peak plus the load of the instance it replaces, so headroom above that peak is the sizing basis.

### Question 100 — C

Answer: Pre-size the promoted replica for the full load. The standby has to be sized in advance for the load it will inherit, since resizing inside the recovery window does not fit. Give the standby enough capacity to carry production alone. Local study-map skill 4.9 (Failover Capacity Headroom), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 4 (deploy scalable and highly available databases in Google Cloud): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Match capacity to the daily traffic shape. Why the correct answer wins: The standby has to be sized in advance for the load it will inherit, since resizing inside the recovery window does not fit.
- **B:** Incorrect for this question. Send reads to a copy so the primary keeps its capacity for writes. Why the correct answer wins: The standby has to be sized in advance for the load it will inherit, since resizing inside the recovery window does not fit.
- **C:** Correct. Give the standby enough capacity to carry production alone. In this case: The standby has to be sized in advance for the load it will inherit, since resizing inside the recovery window does not fit.
- **D:** Incorrect for this question. Keep spare capacity so a failover or a traffic spike does not saturate the instance. Why the correct answer wins: The standby has to be sized in advance for the load it will inherit, since resizing inside the recovery window does not fit.
