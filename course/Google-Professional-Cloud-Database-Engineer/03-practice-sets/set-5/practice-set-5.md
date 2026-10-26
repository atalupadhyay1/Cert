# Google Cloud Professional Cloud Database Engineer — Full-Length Mock Exam 5

Professional Cloud Database Engineer · 100 questions · expanded practice bank · passing score not published

Blueprint-weighted mock exam. Item mix: 84 multiple-choice and 16 multiple-select items (the selection count is stated in each multi-select stem). The live exam publishes 50-60 multiple-choice and multiple-select questions and has no case-study component, so this set is larger on purpose and no case-study item is reproduced. The live paper allows two hours for 50-60 items, so this 100-item set is a slower-per-item rehearsal: about 72 seconds per item here against roughly 120-144 seconds live. Use it to build a habit of finishing with time to review. See the README for the exact fidelity boundary.

Original educational content, not actual, recalled, or copied Google exam items.

## Questions

---

## Domain 1 — Design Innovative, Scalable, and Highly Available Cloud Database Solutions (Sizing, Availability Design, and Database Selection)

### 1. A logistics platform must size a replacement database, and it has a year of metrics plus a signed contract for thirty percent growth. Which two inputs should drive the choice? Select two.

- A. Commit to the steady baseline capacity
- B. Load-test the workload to derive the size
- C. Size the instance from the observed peak metrics
- D. Stop or delete the idle instance
- E. Reserve headroom above the measured peak

### 2. A pre-launch product has a prototype but no traffic history, and the team must choose a shape this week. What should it do?

- A. Reserve headroom above the measured peak
- B. Load-test the workload to derive the size
- C. Size the instance from the observed peak metrics
- D. Commit to the steady baseline capacity

### 3. A Cloud SQL for PostgreSQL instance stalls on writes when its disk throughput ceiling is reached at 09:00, and CPU is at twenty-eight percent. What should the team change?

- A. Add a read replica for the read traffic
- B. Increase the machine type of the instance
- C. Move the data to SSD storage
- D. Increase the disk size to raise throughput

### 4. A Bigtable cluster behind a recommendation feed runs on HDD and misses its p99 objective while CPU stays near thirty-five percent. What should the team change?

- A. Move the data to SSD storage
- B. Set the garbage-collection policy on the column family
- C. Add nodes to the Bigtable cluster
- D. Move the data to HDD storage

### 5. A Cloud SQL instance reports ninety-five percent memory utilization with heavy page faults while CPU holds at forty percent. What should the team do?

- A. Increase the machine type of the instance
- B. Put a session pooler in front of the instance
- C. Increase the disk size to raise throughput
- D. Add a read replica for the read traffic

### 6. A Bigtable cluster's CPU sits above ninety percent with a balanced key distribution and simple row lookups. What should the team do?

- A. Change the row-key design
- B. Add nodes to the Bigtable cluster
- C. Set the garbage-collection policy on the column family
- D. Move the data to SSD storage

### 7. A billing service must survive a zone failure automatically and must be promotable in another region within the hour. Select two.

- A. Choose a multi-region instance configuration
- B. Restore the backup into the second region
- C. Enable regional high availability with a standby zone
- D. Run a single zonal instance
- E. Add a cross-region read replica

### 8. A Spanner service must keep accepting writes through the loss of any single region without operator action. Which topology fits?

- A. Choose a multi-region instance configuration
- B. Restore the backup into the second region
- C. Add a cross-region read replica
- D. Enable regional high availability with a standby zone

### 9. A team has no replica outside its region and must document a four-hour regional recovery using backups. Which action fits?

- A. Promote the cross-region replica during the outage
- B. Set a deny maintenance period over the peak event
- C. Restore the backup into the second region
- D. Enable regional high availability with a standby zone

### 10. A team must pick the weekly hour with the least user impact for engine patching across two continents. What should it configure?

- A. Perform an in-place major version upgrade
- B. Schedule the maintenance window in the low-traffic period
- C. Run a controlled failover test
- D. Set a deny maintenance period over the peak event

### 11. A freeze on changes covers the last week of the quarter, and patching must not land inside it. What should the team set?

- A. Restart the instance in the window
- B. Schedule the maintenance window in the low-traffic period
- C. Take a backup before the upgrade
- D. Set a deny maintenance period over the peak event

### 12. An application in the same VPC must reach Cloud SQL with no internet path and no extra process in the container. Which option fits?

- A. Add the client range to authorized networks
- B. Connect through the Cloud SQL Auth Proxy
- C. Connect over private IP inside the VPC
- D. Use the public IP with enforced SSL

### 13. A contractor laptop must reach a Cloud SQL instance with no site-to-site link and no public address. Which option fits?

- A. Connect over private IP inside the VPC
- B. Add the client range to authorized networks
- C. Connect through the Cloud SQL Auth Proxy
- D. Use the public IP with enforced SSL

### 14. A contract requires customer-held keys with a scheduled rotation that keeps old backups readable. Which two controls are required? Select two.

- A. Enable Data Access audit logs
- B. Encrypt with a customer-managed key in Cloud KMS
- C. Rely on Google-managed encryption keys
- D. Route the audit logs to a locked log bucket
- E. Rotate the customer-managed key on a schedule

### 15. A small team wants encryption at rest on a Cloud SQL instance with no key process to run. Which choice fits?

- A. Add the projects to a VPC Service Controls perimeter
- B. Encrypt with a customer-managed key in Cloud KMS
- C. Rely on Google-managed encryption keys
- D. Rotate the customer-managed key on a schedule

### 16. A function platform opens four thousand short sessions per minute and the instance refuses connections at peak. What should the team add?

- A. Put a session pooler in front of the instance
- B. Increase the machine tier to allow more connections
- C. Add a read replica for the read traffic
- D. Raise the max_connections database flag

### 17. A service's error path abandons sessions without closing them, and the count climbs all day. What should the team fix?

- A. Raise the max_connections database flag
- B. Increase the machine type of the instance
- C. Fix the connection leak in the application
- D. Put a session pooler in front of the instance

### 18. An auditor asks which principal queried a customer table last quarter. Which control provides that record?

- A. Build a log-based metric from the error entries
- B. Route the audit logs to a locked log bucket
- C. Rely on Admin Activity audit logs
- D. Enable Data Access audit logs

### 19. A retention rule requires five years of audit evidence that the project owner cannot shorten. What should the team configure?

- A. Enable Data Access audit logs
- B. Rely on Admin Activity audit logs
- C. Review the fleet in Database Center
- D. Route the audit logs to a locked log bucket

### 20. A two-hundred-gigabyte application needs relational semantics with patching and backups handled by the provider. Which choice fits?

- A. Use Cloud SQL for the relational workload
- B. Run the database on Compute Engine yourself
- C. Use Spanner for the globally distributed relational workload
- D. Use AlloyDB for the demanding relational workload

### 21. An engine requires a kernel module the managed services do not expose, and the team accepts running it. Which deployment fits?

- A. Run the database on bare metal solution
- B. Run the database on Compute Engine yourself
- C. Use a partner-managed database offering
- D. Use Cloud SQL for the relational workload

### 22. A portfolio needs globally consistent transactions for one product and document storage with offline mobile access for another. Which two databases fit? Select two.

- A. Use Cloud SQL for the relational workload
- B. Use Memorystore as the caching tier
- C. Use Spanner for the globally distributed relational workload
- D. Use Bigtable for the high-throughput wide-column workload
- E. Use Firestore for the document workload

### 23. An advertising platform must ingest one million rows per second keyed by campaign and minute and read recent windows by range. Which database fits?

- A. Use Spanner for the globally distributed relational workload
- B. Use Cloud SQL for the relational workload
- C. Use Memorystore as the caching tier
- D. Use Bigtable for the high-throughput wide-column workload

### 24. A workload mixes transactional writes with analytical scans over the same live tables and needs PostgreSQL compatibility. Which service fits?

- A. Use AlloyDB for the demanding relational workload
- B. Use Cloud SQL for the relational workload
- C. Use Bigtable for the high-throughput wide-column workload
- D. Use Spanner for the globally distributed relational workload

### 25. A team wants semantic search added to its existing Cloud SQL for PostgreSQL service with two million embeddings and no new system. What should it use?

- A. Enable the vector extension on PostgreSQL
- B. Export the table into BigQuery
- C. Use AlloyDB vector search with a ScaNN index
- D. Query the source through BigQuery federated queries

### 26. A search product must query eighty million embeddings with metadata filters at low latency on AlloyDB. What should the team build?

- A. Use AlloyDB vector search with a ScaNN index
- B. Add the composite index for the query
- C. Enable the vector extension on PostgreSQL
- D. Cache the hot read path in Memorystore

### 27. An estate runs at constant load, but half the instances are twice the size their peaks require. Which two cost actions fit? Select two.

- A. Rely on sustained-use discounts
- B. Stop or delete the idle instance
- C. Scale down outside business hours
- D. Commit to the steady baseline capacity
- E. Reduce the machine type to match observed use

### 28. A decommissioned product's database still runs with no connections and no owner. What should the team do?

- A. Reduce the machine type to match observed use
- B. Stop or delete the idle instance
- C. Commit to the steady baseline capacity
- D. Reserve capacity for the peak season

### 29. A dependency audit finds two hundred queries relying on engine-specific behaviour, and the release window is five weeks. What should the team decide?

- A. Keep the current engine and version
- B. Write to both systems from the application
- C. Choose the target engine with the cheapest conversion
- D. Use Database Migration Service with schema conversion

### 30. A team must guarantee that no project created next year can place a database outside the approved regions. What should it apply?

- A. Enforce the location with an organization policy
- B. Route the audit logs to a locked log bucket
- C. Encrypt with a customer-managed key in Cloud KMS
- D. Place the instance in the required region

### 31. A team must prevent database rows from being copied into consumer projects, even by an engineer with access. Which control fits?

- A. Export the table into BigQuery
- B. Stream changes into BigQuery
- C. Add the projects to a VPC Service Controls perimeter
- D. Query the source through BigQuery federated queries

### 32. Analysts need live reads of an on-premises warehouse over a private path, and the system itself must stay where it is. Select two.

- A. Stream changes into BigQuery
- B. Decommission the source after a parallel period
- C. Export the table into BigQuery
- D. Query the source through BigQuery federated queries
- E. Keep part of the estate on-premises with a hybrid link

---

## Domain 2 — Manage a Solution That Can Span Multiple Database Technologies (Operations, Access, Backup, and Performance)

### 33. A monitoring integration needs to read instance metrics and nothing else, but it holds the editor role. What should the team change?

- A. Grant the basic editor role
- B. Create one database user per person
- C. Grant the predefined database role
- D. Grant a custom role limited to the needed permissions

### 34. A partner's service must write to a single schema, and the reviewer rejects any grant covering the instance. What should the team request?

- A. Grant a custom role limited to the needed permissions
- B. Grant the basic editor role
- C. Limit the user to the required schema
- D. Share one application database user

### 35. A team must make every analyst's queries attributable and must be able to revoke access when someone changes teams. Select two.

- A. Share one application database user
- B. Grant the basic editor role
- C. Create one database user per person
- D. Bind access to a Google group
- E. Keep a database password in the connection string

### 36. A lookup by email scans five million rows to return one, and the plan confirms a full table scan. What should the team do?

- A. Partition the large table
- B. Refresh the table statistics
- C. Raise the per-operation memory flag
- D. Add the index the slow query needs

### 37. After a nightly reload the planner estimates two hundred rows for a join that returns six hundred thousand. What should the team do?

- A. Raise the per-operation memory flag
- B. Refresh the table statistics
- C. Drop the unused index
- D. Add the index the slow query needs

### 38. A single transaction updates nine hundred thousand rows and blocks writes for twelve minutes. What should change?

- A. Terminate the session that holds the lock
- B. Put a session pooler in front of the instance
- C. Batch the writes into fewer round trips
- D. Inspect lock waits and blocking sessions

### 39. Two reports of stalls need a root cause, and the team must identify which session blocks the others. What should it do?

- A. Refresh the table statistics
- B. Inspect lock waits and blocking sessions
- C. Batch the writes into fewer round trips
- D. Add the index the slow query needs

### 40. A database slowed after a configuration change, and the team must show which resource and which statement changed. Select two.

- A. Watch CPU, memory, disk, and IOPS together
- B. Review the fleet in Database Center
- C. Build a log-based metric from the error entries
- D. Use Query Insights to find the heavy statements
- E. Read the slow query log

### 41. Repeated timeout messages appear in the log but no chart exists, so nobody sees the trend. What should the team create?

- A. Build a log-based metric from the error entries
- B. Alert when the instance is unreachable
- C. Read the slow query log
- D. Route the audit logs to a locked log bucket

### 42. An incident response needs eight parallel exports, and the project refuses the fifth call. What should the team do?

- A. Retry the failed operation with exponential backoff
- B. Request a quota increase for the project
- C. Move the job outside the contention window
- D. Export the table to CSV in Cloud Storage

### 43. A team is paged by a memory alert during a harmless batch, while replica lag goes unreported. Which two changes fix the paging? Select two.

- A. Create an alerting policy on the metric
- B. Alert on the database error rate
- C. Build a log-based metric from the error entries
- D. Alert on replication lag
- E. Watch CPU, memory, disk, and IOPS together

### 44. A team must be told when an instance's replication role changes unexpectedly. What should it configure?

- A. Alert on replication lag
- B. Use Query Insights to find the heavy statements
- C. Create an alerting policy on the metric
- D. Alert on the database error rate

### 45. A bad script deleted rows nine minutes ago and the instance must return to that state. Which capability fits?

- A. Enable automated backups with a retention window
- B. Enable point-in-time recovery
- C. Extend the backup retention window
- D. Export a logical dump to Cloud Storage

### 46. A team's only recovery point is a manual dump from three weeks ago. What should it enable?

- A. Enable automated backups with a retention window
- B. Export the table to CSV in Cloud Storage
- C. Take an on-demand backup before the change
- D. Clone the instance for the test

### 47. A nightly extract feeds a loader, and the bucket that holds it grows without limit. Which two controls are needed? Select two.

- A. Add a lifecycle rule to the export bucket
- B. Export the table to CSV in Cloud Storage
- C. Run the task on a managed schedule
- D. Export a logical dump to Cloud Storage
- E. Import the dump into the target instance

### 48. Two teams disagree about acceptable data loss after an outage, and no objective is written down. What should be agreed first?

- A. Enable automated backups with a retention window
- B. Clone the instance for the test
- C. Enable point-in-time recovery
- D. Design the restore path to the stated RTO and RPO

### 49. A two-terabyte instance must recover in under an hour, but a restore takes six. Which change meets the objective?

- A. Restore to the timestamp before the bad change
- B. Add a cross-region read replica
- C. Extend the backup retention window
- D. Take a backup before the upgrade

### 50. A policy requires deleting support records one hundred eighty days after closure, enforced by the database. What should the team apply?

- A. Set a time-to-live policy on the collection
- B. Archive closed rows to cheaper storage
- C. Set the garbage-collection policy on the column family
- D. Apply a row-level retention policy

### 51. A primary is at ninety-two percent CPU from read traffic, and the application can use a separate read endpoint. What should the team add?

- A. Shard the data across several instances
- B. Add a read replica for the read traffic
- C. Increase the machine type of the instance
- D. Add nodes to the read pool

### 52. A write-heavy instance is at ninety percent CPU, and the application cannot be changed this quarter. What should the team do?

- A. Cache the hot read path in Memorystore
- B. Add a read replica for the read traffic
- C. Increase the machine type of the instance
- D. Send reporting queries to the read replica

### 53. A fraud team wants every new order to appear in BigQuery within seconds while the transactional database keeps serving users. Which approach fits?

- A. Query the source through BigQuery federated queries
- B. Dump, restore, then replay the changes
- C. Stream changes with Datastream
- D. Export the table to CSV in Cloud Storage

### 54. A dashboard repeats the same fifty queries against data that changes hourly and overwhelms the database. What should the team add?

- A. Cache the hot read path in Memorystore
- B. Add the index the slow query needs
- C. Partition the large table
- D. Raise the per-operation memory flag

### 55. A weekly statistics refresh must run at a fixed hour with nobody watching. What should the team configure?

- A. Run the task on a managed schedule
- B. Provision the instance once by hand
- C. Run a controlled failover test
- D. Take an on-demand backup before the change

### 56. A team must see whether a new engine minor version breaks an application before upgrading production. What should it do?

- A. Watch the error rate after the change
- B. Test the upgrade on a clone first
- C. Perform an in-place major version upgrade
- D. Take a backup before the upgrade

### 57. An operations review asks whether the database met the availability it promised customers this month. What should the team track?

- A. Review the fleet in Database Center
- B. Create an alerting policy on the metric
- C. Track the availability signal against the agreed objective
- D. Watch CPU, memory, disk, and IOPS together

---

## Domain 3 — Migrate Data Solutions (Migration Strategy, Conversion, and Cutover)

### 58. A one-terabyte MySQL database must move with a fifteen-minute outage and no application change. Which strategy fits?

- A. Dump, restore, then replay the changes
- B. Accept a scheduled extended outage
- C. Write to both systems from the application
- D. Use Database Migration Service for the same engine

### 59. A team can take a ten-hour outage on a holiday and wants no replication machinery. Which strategy fits?

- A. Follow a cutover runbook with a rollback step
- B. Accept a scheduled extended outage
- C. Write to both systems from the application
- D. Use Database Migration Service for the same engine

### 60. A team must document each cutover step, its owner, and the condition for abandoning it. What should it produce?

- A. Freeze writes during the cutover
- B. Write to both systems from the application
- C. Accept a scheduled extended outage
- D. Follow a cutover runbook with a rollback step

### 61. A program needs Oracle cut over to PostgreSQL and Oracle changes published to BigQuery during the transition. Which two tools fit? Select two.

- A. Dump, restore, then replay the changes
- B. Stream changes with Datastream
- C. Apply the captured change backlog before cutover
- D. Use Database Migration Service with schema conversion
- E. Write to both systems from the application

### 62. A team must clone a fifteen-gigabyte database into a test project once, with no ongoing replication. Which approach fits?

- A. Set up reverse replication to the source
- B. Use Database Migration Service with schema conversion
- C. Write to both systems from the application
- D. Dump, restore, then replay the changes

### 63. An eight-gigabyte MariaDB instance must move to Cloud SQL for MySQL inside a one-hour window. Which approach fits?

- A. Dump, restore, then replay the changes
- B. Write to both systems from the application
- C. Stream changes with Datastream
- D. Use Database Migration Service for the same engine

### 64. A team must review and correct each converted statement before it is applied to the target. Where does that happen?

- A. Rewrite the stored procedures and DML by hand
- B. Build the schema in a conversion workspace
- C. Replay read traffic against the target
- D. Reset the sequences after the bulk load

### 65. A converted schema runs, but two triggers behave differently from the source and no target equivalent exists. What must the team do?

- A. Reset the sequences after the bulk load
- B. Write to both systems from the application
- C. Rewrite the stored procedures and DML by hand
- D. Build the schema in a conversion workspace

### 66. A team wants to compare the target's answers with the source's for the busiest fifty statements. Which activity fits?

- A. Replay read traffic against the target
- B. Rewrite the stored procedures and DML by hand
- C. Follow a cutover runbook with a rollback step
- D. Reconcile row counts and checksums

### 67. A reporting job relies on engine-specific string functions that the target rejects. What must happen?

- A. Write to both systems from the application
- B. Rewrite the stored procedures and DML by hand
- C. Build the schema in a conversion workspace
- D. Reset the sequences after the bulk load

### 68. A twelve-hour load must leave the target current without stopping the source. Which two actions achieve that? Select two.

- A. Write to both systems from the application
- B. Accept a scheduled extended outage
- C. Apply the captured change backlog before cutover
- D. Use the engine native logical replication
- E. Export a logical dump to Cloud Storage

### 69. A team must prove that the twelve-hour load plus catch-up fits a twenty-minute window. What should it measure?

- A. Repoint the connection string at the target
- B. Freeze writes during the cutover
- C. Measure the catch-up rate before choosing the window
- D. Reconcile row counts and checksums

### 70. A team must validate every rehearsal repeatably and prove data equality. Select two.

- A. Follow a cutover runbook with a rollback step
- B. Run the task on a managed schedule
- C. Repoint the connection string at the target
- D. Replay read traffic against the target
- E. Reconcile row counts and checksums

### 71. A team must confirm that report totals produced on the target match those produced on the source. Which check fits?

- A. Write to both systems from the application
- B. Reconcile row counts and checksums
- C. Replay read traffic against the target
- D. Follow a cutover runbook with a rollback step

### 72. A scheduled loader keeps writing to the source while the final increment is being applied. What must happen?

- A. Repoint the connection string at the target
- B. Accept a scheduled extended outage
- C. Set up reverse replication to the source
- D. Freeze writes during the cutover

### 73. The target is validated and writes are stopped, but clients still reach the old address. What completes the cutover?

- A. Use the language connector with IAM credentials
- B. Freeze writes during the cutover
- C. Follow a cutover runbook with a rollback step
- D. Repoint the connection string at the target

### 74. The target's error rate crosses the threshold with fifteen minutes left in the window. What should determine the next action?

- A. Repoint the connection string at the target
- B. Freeze writes during the cutover
- C. Write to both systems from the application
- D. Follow a cutover runbook with a rollback step

### 75. A team needs a lossless rollback path after cutover and a defined end to the fallback. Select two.

- A. Accept a scheduled extended outage
- B. Freeze writes during the cutover
- C. Decommission the source after a parallel period
- D. Repoint the connection string at the target
- E. Set up reverse replication to the source

### 76. The old system's users must see writes made on the new database after the switch. What makes that work?

- A. Set up reverse replication to the source
- B. Repoint the connection string at the target
- C. Decommission the source after a parallel period
- D. Write to both systems from the application

### 77. A four-terabyte migration must avoid a second full load if the cutover fails. What should stay in place?

- A. Write to both systems from the application
- B. Use the engine native logical replication
- C. Accept a scheduled extended outage
- D. Dump, restore, then replay the changes

### 78. The source's change rate quadruples on the first business day of each month, and the cutover window is short. What should the team do?

- A. Move the job outside the contention window
- B. Write to both systems from the application
- C. Measure the catch-up rate before choosing the window
- D. Accept a scheduled extended outage

### 79. Ten years of source history must stay queryable after the engine is removed. What should the team do first?

- A. Set up reverse replication to the source
- B. Keep part of the estate on-premises with a hybrid link
- C. Export the table into BigQuery
- D. Decommission the source after a parallel period

### 80. A team must be certain no scheduled job still connects to the source before deletion. What should it check?

- A. Confirm no client still uses the old endpoint
- B. Decommission the source after a parallel period
- C. Reconcile row counts and checksums
- D. Repoint the connection string at the target

---

## Domain 4 — Deploy Scalable and Highly Available Databases in Google Cloud (Deployment, High Availability, and Disaster Recovery)

### 81. A team must recreate a nine-instance estate in a new region after a disaster with identical settings. What makes that reliable?

- A. Provision the instance once by hand
- B. Clone the instance for the test
- C. Stand up a parallel instance and switch over
- D. Provision the instance with a Terraform module

### 82. An audit finding says database changes reach production with no approval trail at all. What should the team adopt?

- A. Review the fleet in Database Center
- B. Test the upgrade on a clone first
- C. Apply the change through the infrastructure pipeline
- D. Provision the instance once by hand

### 83. A platform team must apply the same configuration to thirty existing instances without manual edits. What should it use?

- A. Provision the instance once by hand
- B. Provision the instance with a Terraform module
- C. Stand up a parallel instance and switch over
- D. Take a backup before the upgrade

### 84. A team must show that the standby takes over when its zone disappears. What should it run?

- A. Run a controlled failover test
- B. Take a backup before the upgrade
- C. Watch the error rate after the change
- D. Restore the backup into the second region

### 85. Before promising a regional recovery time in its service description, a team must measure how long a promotion really takes. Which exercise provides that?

- A. Pre-size the promoted replica for the full load
- B. Run a controlled failover test
- C. Take a backup before the upgrade
- D. Rehearse the promotion in a test project

### 86. A team must prove it can rebuild from backup in a second region rather than fail over. What should it rehearse?

- A. Run a controlled failover test
- B. Take a backup before the upgrade
- C. Rehearse the promotion in a test project
- D. Restore the backup into the second region

### 87. An estate runs Spanner and AlloyDB, and both must survive a regional loss. Which two choices fit? Select two.

- A. Add a cross-region read replica
- B. Restore the backup into the second region
- C. Choose a multi-region instance configuration
- D. Add a secondary cluster in the second region
- E. Enable regional high availability with a standby zone

### 88. A Bigtable client must keep serving when one cluster is lost, with no change to the client. What should the app profile do?

- A. Add a cross-region read replica
- B. Route the app profile across both clusters
- C. Pin the app profile to one cluster
- D. Add a secondary cluster in the second region

### 89. A reporting team on another continent needs a continuously updated Cloud SQL copy that could also be promoted. What should the team add?

- A. Add a cross-region read replica
- B. Choose a multi-region instance configuration
- C. Restore the backup into the second region
- D. Add a secondary cluster in the second region

### 90. An AlloyDB read pool is at eighty-eight percent CPU while the primary is at thirty percent. What should the team do?

- A. Cache the hot read path in Memorystore
- B. Add nodes to the read pool
- C. Send reporting queries to the read replica
- D. Increase the machine type of the instance

### 91. A Cloud SQL replica is at eighteen percent CPU while the primary runs at ninety percent on the same application. What should the team change?

- A. Send reporting queries to the read replica
- B. Cache the hot read path in Memorystore
- C. Add a read replica for the read traffic
- D. Increase the machine type of the instance

### 92. A team must create one hundred tenant instances with identical flags and per-tenant labels. What should it use?

- A. Review the fleet in Database Center
- B. Provision the instance once by hand
- C. Provision the instance with a Terraform module
- D. Test the upgrade on a clone first

### 93. A platform team wants a missing classification label to block provisioning before any resource exists. What should it use?

- A. Clone the instance for the test
- B. Take a backup before the upgrade
- C. Apply the change through the infrastructure pipeline
- D. Provision the instance once by hand

### 94. A team must know within a minute that a failover moved the primary. What should it configure?

- A. Use Query Insights to find the heavy statements
- B. Watch CPU, memory, disk, and IOPS together
- C. Review the fleet in Database Center
- D. Create an alerting policy on the metric

### 95. A resource dashboard shows the instance as healthy while the application reports timeouts. What should the team add?

- A. Watch CPU, memory, disk, and IOPS together
- B. Use Query Insights to find the heavy statements
- C. Read the slow query log
- D. Alert when the instance is unreachable

### 96. A region is lost and later returns while the promoted instance is serving. Which two actions are needed? Select two.

- A. Restore the backup into the second region
- B. Fence the old primary before promotion
- C. Run a controlled failover test
- D. Restore to the timestamp before the bad change
- E. Promote the cross-region replica during the outage

### 97. A team must show that an application reconnects on its own after the active zone is removed. What should it run?

- A. Take a backup before the upgrade
- B. Run a controlled failover test
- C. Restore the backup into the second region
- D. Watch the error rate after the change

### 98. A connection pool keeps using a cached address after a failover. What should the team adopt?

- A. Repoint the connection string at the target
- B. Put a session pooler in front of the instance
- C. Use the language connector with IAM credentials
- D. Add the client range to authorized networks

### 99. A standby currently handles only overflow reads, yet after a failover it must absorb the full write load. What should its capacity include?

- A. Add a read replica for the read traffic
- B. Reserve headroom above the measured peak
- C. Scale down outside business hours
- D. Reduce the machine type to match observed use

### 100. A drill reveals the standby runs at forty percent of production and cannot be enlarged inside the recovery window. What should change?

- A. Reserve headroom above the measured peak
- B. Scale down outside business hours
- C. Add a read replica for the read traffic
- D. Pre-size the promoted replica for the full load

---

## Answer key and explanations

### Question 1 — C, E

Answers: Size the instance from the observed peak metrics; Reserve headroom above the measured peak. The measured peaks give the current requirement, and the contracted growth is the only forward input the team can defend. Choose a shape from measured CPU, memory, and IOPS rather than from a guess. Keep spare capacity so a failover or a traffic spike does not saturate the instance. Local study-map skill 1.1 (Workload Sizing From Current Metrics), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 1 (design innovative, scalable, and highly available cloud database solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A one- or three-year commitment that discounts the capacity always in use. Why the correct answer wins: The measured peaks give the current requirement, and the contracted growth is the only forward input the team can defend.
- **B:** Incorrect for this question. Generate representative traffic and read the resource curve before choosing a shape. Why the correct answer wins: The measured peaks give the current requirement, and the contracted growth is the only forward input the team can defend.
- **C:** Correct. Choose a shape from measured CPU, memory, and IOPS rather than from a guess. In this case: The measured peaks give the current requirement, and the contracted growth is the only forward input the team can defend.
- **D:** Incorrect for this question. Remove capacity that serves no traffic. Why the correct answer wins: The measured peaks give the current requirement, and the contracted growth is the only forward input the team can defend.
- **E:** Correct. Keep spare capacity so a failover or a traffic spike does not saturate the instance. In this case: The measured peaks give the current requirement, and the contracted growth is the only forward input the team can defend.

### Question 2 — B

Answer: Load-test the workload to derive the size. Driving representative load through the prototype produces the curve the decision needs before launch. Generate representative traffic and read the resource curve before choosing a shape. Local study-map skill 1.1 (Workload Sizing From Current Metrics), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 1 (design innovative, scalable, and highly available cloud database solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Keep spare capacity so a failover or a traffic spike does not saturate the instance. Why the correct answer wins: Driving representative load through the prototype produces the curve the decision needs before launch.
- **B:** Correct. Generate representative traffic and read the resource curve before choosing a shape. In this case: Driving representative load through the prototype produces the curve the decision needs before launch.
- **C:** Incorrect for this question. Choose a shape from measured CPU, memory, and IOPS rather than from a guess. Why the correct answer wins: Driving representative load through the prototype produces the curve the decision needs before launch.
- **D:** Incorrect for this question. A one- or three-year commitment that discounts the capacity always in use. Why the correct answer wins: Driving representative load through the prototype produces the curve the decision needs before launch.

### Question 3 — D

Answer: Increase the disk size to raise throughput. The disk ceiling is the constraint, so more storage raises it without buying compute the workload does not need. Buy more storage so the attached disk also yields more IOPS and throughput. Local study-map skill 1.2 (Compute and Storage Sizing Tradeoffs), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 1 (design innovative, scalable, and highly available cloud database solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Send reads to a copy so the primary keeps its capacity for writes. Why the correct answer wins: The disk ceiling is the constraint, so more storage raises it without buying compute the workload does not need.
- **B:** Incorrect for this question. Move the instance to a larger shape so more vCPU and memory serve the same data. Why the correct answer wins: The disk ceiling is the constraint, so more storage raises it without buying compute the workload does not need.
- **C:** Incorrect for this question. Trade a higher price per gigabyte for lower latency on random reads. Why the correct answer wins: The disk ceiling is the constraint, so more storage raises it without buying compute the workload does not need.
- **D:** Correct. Buy more storage so the attached disk also yields more IOPS and throughput. In this case: The disk ceiling is the constraint, so more storage raises it without buying compute the workload does not need.

### Question 4 — A

Answer: Move the data to SSD storage. SSD lowers the read latency that is missing the objective. Trade a higher price per gigabyte for lower latency on random reads. Local study-map skill 1.2 (Compute and Storage Sizing Tradeoffs), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 1 (design innovative, scalable, and highly available cloud database solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Correct. Trade a higher price per gigabyte for lower latency on random reads. In this case: SSD lowers the read latency that is missing the objective.
- **B:** Incorrect for this question. A rule that drops versions by age or count, which also bounds recovery. Why the correct answer wins: SSD lowers the read latency that is missing the objective.
- **C:** Incorrect for this question. Increase the cluster size so more tablet servers absorb the request rate. Why the correct answer wins: SSD lowers the read latency that is missing the objective.
- **D:** Incorrect for this question. Trade latency for a lower price on large, throughput-oriented scans. Why the correct answer wins: SSD lowers the read latency that is missing the objective.

### Question 5 — A

Answer: Increase the machine type of the instance. A larger shape adds the memory the engine is short of, which storage, a replica, or a pooler does not. Move the instance to a larger shape so more vCPU and memory serve the same data. Local study-map skill 1.3 (Machine Type and Storage Type Selection), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 1 (design innovative, scalable, and highly available cloud database solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Correct. Move the instance to a larger shape so more vCPU and memory serve the same data. In this case: A larger shape adds the memory the engine is short of, which storage, a replica, or a pooler does not.
- **B:** Incorrect for this question. A pooler that multiplexes many application connections onto few database sessions. Why the correct answer wins: A larger shape adds the memory the engine is short of, which storage, a replica, or a pooler does not.
- **C:** Incorrect for this question. Buy more storage so the attached disk also yields more IOPS and throughput. Why the correct answer wins: A larger shape adds the memory the engine is short of, which storage, a replica, or a pooler does not.
- **D:** Incorrect for this question. Send reads to a copy so the primary keeps its capacity for writes. Why the correct answer wins: A larger shape adds the memory the engine is short of, which storage, a replica, or a pooler does not.

### Question 6 — B

Answer: Add nodes to the Bigtable cluster. Adding nodes raises serving capacity when the access pattern is already healthy. Increase the cluster size so more tablet servers absorb the request rate. Local study-map skill 1.3 (Machine Type and Storage Type Selection), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 1 (design innovative, scalable, and highly available cloud database solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Fix the access pattern that concentrates load on a narrow key range. Why the correct answer wins: Adding nodes raises serving capacity when the access pattern is already healthy.
- **B:** Correct. Increase the cluster size so more tablet servers absorb the request rate. In this case: Adding nodes raises serving capacity when the access pattern is already healthy.
- **C:** Incorrect for this question. A rule that drops versions by age or count, which also bounds recovery. Why the correct answer wins: Adding nodes raises serving capacity when the access pattern is already healthy.
- **D:** Incorrect for this question. Trade a higher price per gigabyte for lower latency on random reads. Why the correct answer wins: Adding nodes raises serving capacity when the access pattern is already healthy.

### Question 7 — C, E

Answers: Enable regional high availability with a standby zone; Add a cross-region read replica. A regional instance covers the zone case automatically, and the cross-region copy provides the promotion path. A primary and standby in two zones of one region with automatic failover. A copy in a second region that serves reads and can be promoted. Local study-map skill 1.4 (Zonal, Regional, and Multi-Regional Tradeoffs), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 1 (design innovative, scalable, and highly available cloud database solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A topology that places replicas in separate regions for regional-failure tolerance. Why the correct answer wins: A regional instance covers the zone case automatically, and the cross-region copy provides the promotion path.
- **B:** Incorrect for this question. Rebuild the database in the surviving region from the latest backup. Why the correct answer wins: A regional instance covers the zone case automatically, and the cross-region copy provides the promotion path.
- **C:** Correct. A primary and standby in two zones of one region with automatic failover. In this case: A regional instance covers the zone case automatically, and the cross-region copy provides the promotion path.
- **D:** Incorrect for this question. One instance in one zone with no standby, so a zone failure stops writes. Why the correct answer wins: A regional instance covers the zone case automatically, and the cross-region copy provides the promotion path.
- **E:** Correct. A copy in a second region that serves reads and can be promoted. In this case: A regional instance covers the zone case automatically, and the cross-region copy provides the promotion path.

### Question 8 — A

Answer: Choose a multi-region instance configuration. A multi-region configuration keeps quorum across regions so writes continue automatically. A topology that places replicas in separate regions for regional-failure tolerance. Local study-map skill 1.4 (Zonal, Regional, and Multi-Regional Tradeoffs), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 1 (design innovative, scalable, and highly available cloud database solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Correct. A topology that places replicas in separate regions for regional-failure tolerance. In this case: A multi-region configuration keeps quorum across regions so writes continue automatically.
- **B:** Incorrect for this question. Rebuild the database in the surviving region from the latest backup. Why the correct answer wins: A multi-region configuration keeps quorum across regions so writes continue automatically.
- **C:** Incorrect for this question. A copy in a second region that serves reads and can be promoted. Why the correct answer wins: A multi-region configuration keeps quorum across regions so writes continue automatically.
- **D:** Incorrect for this question. A primary and standby in two zones of one region with automatic failover. Why the correct answer wins: A multi-region configuration keeps quorum across regions so writes continue automatically.

### Question 9 — C

Answer: Restore the backup into the second region. Restoring the latest backup into the second region is the path available when no copy exists. Rebuild the database in the surviving region from the latest backup. Local study-map skill 1.4 (Zonal, Regional, and Multi-Regional Tradeoffs), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 1 (design innovative, scalable, and highly available cloud database solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Turn the replica into an independent primary so the application can resume writes. Why the correct answer wins: Restoring the latest backup into the second region is the path available when no copy exists.
- **B:** Incorrect for this question. Block maintenance during a period when an interruption is unacceptable. Why the correct answer wins: Restoring the latest backup into the second region is the path available when no copy exists.
- **C:** Correct. Rebuild the database in the surviving region from the latest backup. In this case: Restoring the latest backup into the second region is the path available when no copy exists.
- **D:** Incorrect for this question. A primary and standby in two zones of one region with automatic failover. Why the correct answer wins: Restoring the latest backup into the second region is the path available when no copy exists.

### Question 10 — B

Answer: Schedule the maintenance window in the low-traffic period. The maintenance window sets when patching may run. Choose the weekly window when patching may interrupt the instance. Local study-map skill 1.5 (Maintenance Windows and Notification), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 1 (design innovative, scalable, and highly available cloud database solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Change the engine version on the running instance during the window. Why the correct answer wins: The maintenance window sets when patching may run.
- **B:** Correct. Choose the weekly window when patching may interrupt the instance. In this case: The maintenance window sets when patching may run.
- **C:** Incorrect for this question. Trigger a switchover in a test window and observe how long writes are unavailable. Why the correct answer wins: The maintenance window sets when patching may run.
- **D:** Incorrect for this question. Block maintenance during a period when an interruption is unacceptable. Why the correct answer wins: The maintenance window sets when patching may run.

### Question 11 — D

Answer: Set a deny maintenance period over the peak event. A deny period removes that week from the patching schedule and then lapses. Block maintenance during a period when an interruption is unacceptable. Local study-map skill 1.5 (Maintenance Windows and Notification), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 1 (design innovative, scalable, and highly available cloud database solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Apply the configuration change with a brief restart. Why the correct answer wins: A deny period removes that week from the patching schedule and then lapses.
- **B:** Incorrect for this question. Choose the weekly window when patching may interrupt the instance. Why the correct answer wins: A deny period removes that week from the patching schedule and then lapses.
- **C:** Incorrect for this question. A recovery point that makes the upgrade reversible in practice. Why the correct answer wins: A deny period removes that week from the patching schedule and then lapses.
- **D:** Correct. Block maintenance during a period when an interruption is unacceptable. In this case: A deny period removes that week from the patching schedule and then lapses.

### Question 12 — C

Answer: Connect over private IP inside the VPC. A private address stays inside the VPC and needs no sidecar or proxy. A private address reachable only from the VPC and connected networks. Local study-map skill 1.6 (Network Connectivity and Private Access), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 1 (design innovative, scalable, and highly available cloud database solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A public-IP allowlist that admits the caller range. Why the correct answer wins: A private address stays inside the VPC and needs no sidecar or proxy.
- **B:** Incorrect for this question. A local proxy that adds IAM authorization and TLS without opening a network path. Why the correct answer wins: A private address stays inside the VPC and needs no sidecar or proxy.
- **C:** Correct. A private address reachable only from the VPC and connected networks. In this case: A private address stays inside the VPC and needs no sidecar or proxy.
- **D:** Incorrect for this question. A public address that requires encrypted connections from any client. Why the correct answer wins: A private address stays inside the VPC and needs no sidecar or proxy.

### Question 13 — C

Answer: Connect through the Cloud SQL Auth Proxy. The proxy authorizes the session with IAM over TLS, so no public address or network link is required. A local proxy that adds IAM authorization and TLS without opening a network path. Local study-map skill 1.6 (Network Connectivity and Private Access), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 1 (design innovative, scalable, and highly available cloud database solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A private address reachable only from the VPC and connected networks. Why the correct answer wins: The proxy authorizes the session with IAM over TLS, so no public address or network link is required.
- **B:** Incorrect for this question. A public-IP allowlist that admits the caller range. Why the correct answer wins: The proxy authorizes the session with IAM over TLS, so no public address or network link is required.
- **C:** Correct. A local proxy that adds IAM authorization and TLS without opening a network path. In this case: The proxy authorizes the session with IAM over TLS, so no public address or network link is required.
- **D:** Incorrect for this question. A public address that requires encrypted connections from any client. Why the correct answer wins: The proxy authorizes the session with IAM over TLS, so no public address or network link is required.

### Question 14 — B, E

Answers: Encrypt with a customer-managed key in Cloud KMS; Rotate the customer-managed key on a schedule. Customer-managed keys give the customer custody, and rotation adds new versions while existing ciphertext stays decryptable. A key the customer owns and can rotate or revoke. Produce new key versions so an old version stops encrypting new data. Local study-map skill 1.7 (Key Management and Encryption), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 1 (design innovative, scalable, and highly available cloud database solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Record reads and writes, which are not captured by default. Why the correct answer wins: Customer-managed keys give the customer custody, and rotation adds new versions while existing ciphertext stays decryptable.
- **B:** Correct. A key the customer owns and can rotate or revoke. In this case: Customer-managed keys give the customer custody, and rotation adds new versions while existing ciphertext stays decryptable.
- **C:** Incorrect for this question. Default encryption at rest with keys the customer neither sees nor manages. Why the correct answer wins: Customer-managed keys give the customer custody, and rotation adds new versions while existing ciphertext stays decryptable.
- **D:** Incorrect for this question. Export entries to storage whose retention cannot be shortened. Why the correct answer wins: Customer-managed keys give the customer custody, and rotation adds new versions while existing ciphertext stays decryptable.
- **E:** Correct. Produce new key versions so an old version stops encrypting new data. In this case: Customer-managed keys give the customer custody, and rotation adds new versions while existing ciphertext stays decryptable.

### Question 15 — C

Answer: Rely on Google-managed encryption keys. Default Google-managed encryption protects the data without the team owning a key lifecycle. Default encryption at rest with keys the customer neither sees nor manages. Local study-map skill 1.7 (Key Management and Encryption), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 1 (design innovative, scalable, and highly available cloud database solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A boundary that blocks data exfiltration even from an authorized identity. Why the correct answer wins: Default Google-managed encryption protects the data without the team owning a key lifecycle.
- **B:** Incorrect for this question. A key the customer owns and can rotate or revoke. Why the correct answer wins: Default Google-managed encryption protects the data without the team owning a key lifecycle.
- **C:** Correct. Default encryption at rest with keys the customer neither sees nor manages. In this case: Default Google-managed encryption protects the data without the team owning a key lifecycle.
- **D:** Incorrect for this question. Produce new key versions so an old version stops encrypting new data. Why the correct answer wins: Default Google-managed encryption protects the data without the team owning a key lifecycle.

### Question 16 — A

Answer: Put a session pooler in front of the instance. A pooler multiplexes the sessions onto a small number of database connections. A pooler that multiplexes many application connections onto few database sessions. Local study-map skill 1.8 (Session Pooling and Connection Management), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 1 (design innovative, scalable, and highly available cloud database solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Correct. A pooler that multiplexes many application connections onto few database sessions. In this case: A pooler multiplexes the sessions onto a small number of database connections.
- **B:** Incorrect for this question. Buy a larger shape because the connection limit scales with memory. Why the correct answer wins: A pooler multiplexes the sessions onto a small number of database connections.
- **C:** Incorrect for this question. Send reads to a copy so the primary keeps its capacity for writes. Why the correct answer wins: A pooler multiplexes the sessions onto a small number of database connections.
- **D:** Incorrect for this question. Increase the database-level connection ceiling on the instance. Why the correct answer wins: A pooler multiplexes the sessions onto a small number of database connections.

### Question 17 — C

Answer: Fix the connection leak in the application. Closing sessions on the error path removes the growth at its source. Close sessions that the application opens and never returns to the pool. Local study-map skill 1.8 (Session Pooling and Connection Management), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 1 (design innovative, scalable, and highly available cloud database solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Increase the database-level connection ceiling on the instance. Why the correct answer wins: Closing sessions on the error path removes the growth at its source.
- **B:** Incorrect for this question. Move the instance to a larger shape so more vCPU and memory serve the same data. Why the correct answer wins: Closing sessions on the error path removes the growth at its source.
- **C:** Correct. Close sessions that the application opens and never returns to the pool. In this case: Closing sessions on the error path removes the growth at its source.
- **D:** Incorrect for this question. A pooler that multiplexes many application connections onto few database sessions. Why the correct answer wins: Closing sessions on the error path removes the growth at its source.

### Question 18 — D

Answer: Enable Data Access audit logs. Row-level reads are recorded only when Data Access audit logs are enabled. Record reads and writes, which are not captured by default. Local study-map skill 1.9 (Auditing Policies for Managed Services), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 1 (design innovative, scalable, and highly available cloud database solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Turn a recurring log pattern into a metric that can be charted and alerted on. Why the correct answer wins: Row-level reads are recorded only when Data Access audit logs are enabled.
- **B:** Incorrect for this question. Export entries to storage whose retention cannot be shortened. Why the correct answer wins: Row-level reads are recorded only when Data Access audit logs are enabled.
- **C:** Incorrect for this question. Record configuration changes only, leaving row-level reads unaudited. Why the correct answer wins: Row-level reads are recorded only when Data Access audit logs are enabled.
- **D:** Correct. Record reads and writes, which are not captured by default. In this case: Row-level reads are recorded only when Data Access audit logs are enabled.

### Question 19 — D

Answer: Route the audit logs to a locked log bucket. Routing the entries to locked storage prevents the retention from being reduced. Export entries to storage whose retention cannot be shortened. Local study-map skill 1.9 (Auditing Policies for Managed Services), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 1 (design innovative, scalable, and highly available cloud database solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Record reads and writes, which are not captured by default. Why the correct answer wins: Routing the entries to locked storage prevents the retention from being reduced.
- **B:** Incorrect for this question. Record configuration changes only, leaving row-level reads unaudited. Why the correct answer wins: Routing the entries to locked storage prevents the retention from being reduced.
- **C:** Incorrect for this question. A single view of health, security, and version posture across database instances. Why the correct answer wins: Routing the entries to locked storage prevents the retention from being reduced.
- **D:** Correct. Export entries to storage whose retention cannot be shortened. In this case: Routing the entries to locked storage prevents the retention from being reduced.

### Question 20 — A

Answer: Use Cloud SQL for the relational workload. A managed relational instance covers that size with the operational work handled. A managed MySQL, PostgreSQL, or SQL Server instance with Google-operated backups, patching, and failover. Local study-map skill 1.10 (Managed, Self-Managed, and Partner Offerings), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 1 (design innovative, scalable, and highly available cloud database solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Correct. A managed MySQL, PostgreSQL, or SQL Server instance with Google-operated backups, patching, and failover. In this case: A managed relational instance covers that size with the operational work handled.
- **B:** Incorrect for this question. A self-managed engine on virtual machines where the team owns patching, backups, and failover. Why the correct answer wins: A managed relational instance covers that size with the operational work handled.
- **C:** Incorrect for this question. A horizontally scalable relational database with strong consistency across regions and no manual sharding. Why the correct answer wins: A managed relational instance covers that size with the operational work handled.
- **D:** Incorrect for this question. A managed PostgreSQL-compatible database with a separate read pool and columnar acceleration for mixed transactional and analytical load. Why the correct answer wins: A managed relational instance covers that size with the operational work handled.

### Question 21 — B

Answer: Run the database on Compute Engine yourself. A self-managed deployment on virtual machines lets the team install what the engine needs. A self-managed engine on virtual machines where the team owns patching, backups, and failover. Local study-map skill 1.10 (Managed, Self-Managed, and Partner Offerings), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 1 (design innovative, scalable, and highly available cloud database solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Dedicated hardware for engines that cannot be virtualized or licensed for a managed service. Why the correct answer wins: A self-managed deployment on virtual machines lets the team install what the engine needs.
- **B:** Correct. A self-managed engine on virtual machines where the team owns patching, backups, and failover. In this case: A self-managed deployment on virtual machines lets the team install what the engine needs.
- **C:** Incorrect for this question. A third-party database operated by its vendor on Google Cloud infrastructure. Why the correct answer wins: A self-managed deployment on virtual machines lets the team install what the engine needs.
- **D:** Incorrect for this question. A managed MySQL, PostgreSQL, or SQL Server instance with Google-operated backups, patching, and failover. Why the correct answer wins: A self-managed deployment on virtual machines lets the team install what the engine needs.

### Question 22 — C, E

Answers: Use Spanner for the globally distributed relational workload; Use Firestore for the document workload. Spanner supplies the globally consistent transactions, and Firestore supplies the document model with offline client support. A horizontally scalable relational database with strong consistency across regions and no manual sharding. A document database with automatic multi-region replication, offline client support, and index-driven queries. Local study-map skill 1.11 (SQL and NoSQL Data Model Fit), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 1 (design innovative, scalable, and highly available cloud database solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A managed MySQL, PostgreSQL, or SQL Server instance with Google-operated backups, patching, and failover. Why the correct answer wins: Spanner supplies the globally consistent transactions, and Firestore supplies the document model with offline client support.
- **B:** Incorrect for this question. A managed Redis-compatible in-memory store placed in front of the system of record. Why the correct answer wins: Spanner supplies the globally consistent transactions, and Firestore supplies the document model with offline client support.
- **C:** Correct. A horizontally scalable relational database with strong consistency across regions and no manual sharding. In this case: Spanner supplies the globally consistent transactions, and Firestore supplies the document model with offline client support.
- **D:** Incorrect for this question. A wide-column NoSQL service built for very high write and read rates over a sparse, row-key-ordered model. Why the correct answer wins: Spanner supplies the globally consistent transactions, and Firestore supplies the document model with offline client support.
- **E:** Correct. A document database with automatic multi-region replication, offline client support, and index-driven queries. In this case: Spanner supplies the globally consistent transactions, and Firestore supplies the document model with offline client support.

### Question 23 — D

Answer: Use Bigtable for the high-throughput wide-column workload. A wide-column store with row-key ordering handles that write rate and range read pattern at low cost. A wide-column NoSQL service built for very high write and read rates over a sparse, row-key-ordered model. Local study-map skill 1.11 (SQL and NoSQL Data Model Fit), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 1 (design innovative, scalable, and highly available cloud database solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A horizontally scalable relational database with strong consistency across regions and no manual sharding. Why the correct answer wins: A wide-column store with row-key ordering handles that write rate and range read pattern at low cost.
- **B:** Incorrect for this question. A managed MySQL, PostgreSQL, or SQL Server instance with Google-operated backups, patching, and failover. Why the correct answer wins: A wide-column store with row-key ordering handles that write rate and range read pattern at low cost.
- **C:** Incorrect for this question. A managed Redis-compatible in-memory store placed in front of the system of record. Why the correct answer wins: A wide-column store with row-key ordering handles that write rate and range read pattern at low cost.
- **D:** Correct. A wide-column NoSQL service built for very high write and read rates over a sparse, row-key-ordered model. In this case: A wide-column store with row-key ordering handles that write rate and range read pattern at low cost.

### Question 24 — A

Answer: Use AlloyDB for the demanding relational workload. AlloyDB provides PostgreSQL compatibility with a separate read pool and columnar acceleration for that mix. A managed PostgreSQL-compatible database with a separate read pool and columnar acceleration for mixed transactional and analytical load. Local study-map skill 1.11 (SQL and NoSQL Data Model Fit), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 1 (design innovative, scalable, and highly available cloud database solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Correct. A managed PostgreSQL-compatible database with a separate read pool and columnar acceleration for mixed transactional and analytical load. In this case: AlloyDB provides PostgreSQL compatibility with a separate read pool and columnar acceleration for that mix.
- **B:** Incorrect for this question. A managed MySQL, PostgreSQL, or SQL Server instance with Google-operated backups, patching, and failover. Why the correct answer wins: AlloyDB provides PostgreSQL compatibility with a separate read pool and columnar acceleration for that mix.
- **C:** Incorrect for this question. A wide-column NoSQL service built for very high write and read rates over a sparse, row-key-ordered model. Why the correct answer wins: AlloyDB provides PostgreSQL compatibility with a separate read pool and columnar acceleration for that mix.
- **D:** Incorrect for this question. A horizontally scalable relational database with strong consistency across regions and no manual sharding. Why the correct answer wins: AlloyDB provides PostgreSQL compatibility with a separate read pool and columnar acceleration for that mix.

### Question 25 — A

Answer: Enable the vector extension on PostgreSQL. Enabling the vector extension keeps the embeddings beside the existing rows. Store embeddings beside relational rows and search them in the same engine. Local study-map skill 1.12 (Vector and Generative AI Requirements), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 1 (design innovative, scalable, and highly available cloud database solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Correct. Store embeddings beside relational rows and search them in the same engine. In this case: Enabling the vector extension keeps the embeddings beside the existing rows.
- **B:** Incorrect for this question. Copy the analytical slice into the warehouse on a schedule. Why the correct answer wins: Enabling the vector extension keeps the embeddings beside the existing rows.
- **C:** Incorrect for this question. A vector index tuned for large embedding sets on AlloyDB. Why the correct answer wins: Enabling the vector extension keeps the embeddings beside the existing rows.
- **D:** Incorrect for this question. Read the operational table from BigQuery without copying it first. Why the correct answer wins: Enabling the vector extension keeps the embeddings beside the existing rows.

### Question 26 — A

Answer: Use AlloyDB vector search with a ScaNN index. A purpose-built vector index meets that scale with filters applied in the engine. A vector index tuned for large embedding sets on AlloyDB. Local study-map skill 1.12 (Vector and Generative AI Requirements), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 1 (design innovative, scalable, and highly available cloud database solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Correct. A vector index tuned for large embedding sets on AlloyDB. In this case: A purpose-built vector index meets that scale with filters applied in the engine.
- **B:** Incorrect for this question. An index ordered so the filter and sort both resolve without a scan. Why the correct answer wins: A purpose-built vector index meets that scale with filters applied in the engine.
- **C:** Incorrect for this question. Store embeddings beside relational rows and search them in the same engine. Why the correct answer wins: A purpose-built vector index meets that scale with filters applied in the engine.
- **D:** Incorrect for this question. Absorb repeated reads in memory so the database sees fewer of them. Why the correct answer wins: A purpose-built vector index meets that scale with filters applied in the engine.

### Question 27 — D, E

Answers: Commit to the steady baseline capacity; Reduce the machine type to match observed use. Committing the steady baseline discounts capacity that never varies, and shrinking the oversized instances matches spend to observed use. A one- or three-year commitment that discounts the capacity always in use. Shrink an instance whose peak fits a smaller shape. Local study-map skill 1.13 (Comparative Cost Analysis Across Databases), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 1 (design innovative, scalable, and highly available cloud database solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. The automatic discount that applies to long-running Compute Engine usage. Why the correct answer wins: Committing the steady baseline discounts capacity that never varies, and shrinking the oversized instances matches spend to observed use.
- **B:** Incorrect for this question. Remove capacity that serves no traffic. Why the correct answer wins: Committing the steady baseline discounts capacity that never varies, and shrinking the oversized instances matches spend to observed use.
- **C:** Incorrect for this question. Match capacity to the daily traffic shape. Why the correct answer wins: Committing the steady baseline discounts capacity that never varies, and shrinking the oversized instances matches spend to observed use.
- **D:** Correct. A one- or three-year commitment that discounts the capacity always in use. In this case: Committing the steady baseline discounts capacity that never varies, and shrinking the oversized instances matches spend to observed use.
- **E:** Correct. Shrink an instance whose peak fits a smaller shape. In this case: Committing the steady baseline discounts capacity that never varies, and shrinking the oversized instances matches spend to observed use.

### Question 28 — B

Answer: Stop or delete the idle instance. An instance with no traffic and no owner should be stopped or removed rather than committed or resized. Remove capacity that serves no traffic. Local study-map skill 1.13 (Comparative Cost Analysis Across Databases), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 1 (design innovative, scalable, and highly available cloud database solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Shrink an instance whose peak fits a smaller shape. Why the correct answer wins: An instance with no traffic and no owner should be stopped or removed rather than committed or resized.
- **B:** Correct. Remove capacity that serves no traffic. In this case: An instance with no traffic and no owner should be stopped or removed rather than committed or resized.
- **C:** Incorrect for this question. A one- or three-year commitment that discounts the capacity always in use. Why the correct answer wins: An instance with no traffic and no owner should be stopped or removed rather than committed or resized.
- **D:** Incorrect for this question. Hold capacity ahead of a known surge rather than waiting for autoscaling. Why the correct answer wins: An instance with no traffic and no owner should be stopped or removed rather than committed or resized.

### Question 29 — A

Answer: Keep the current engine and version. Keeping the engine avoids rewrites the window cannot absorb. A lift of the existing engine with no conversion work, retaining its behaviour and licensing. Local study-map skill 1.14 (Application and Database Dependencies), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 1 (design innovative, scalable, and highly available cloud database solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Correct. A lift of the existing engine with no conversion work, retaining its behaviour and licensing. In this case: Keeping the engine avoids rewrites the window cannot absorb.
- **B:** Incorrect for this question. Keep two databases current from application code during the transition. Why the correct answer wins: Keeping the engine avoids rewrites the window cannot absorb.
- **C:** Incorrect for this question. Weigh engine compatibility and code rewrite effort before selecting a destination. Why the correct answer wins: Keeping the engine avoids rewrites the window cannot absorb.
- **D:** Incorrect for this question. A managed path that converts schema and code from a different source engine. Why the correct answer wins: Keeping the engine avoids rewrites the window cannot absorb.

### Question 30 — A

Answer: Enforce the location with an organization policy. An organization-level constraint blocks such creation regardless of project ownership. A constraint that keeps database resources inside the approved regions. Local study-map skill 1.15 (Regulatory, Compliance, and Organization Policy), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 1 (design innovative, scalable, and highly available cloud database solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Correct. A constraint that keeps database resources inside the approved regions. In this case: An organization-level constraint blocks such creation regardless of project ownership.
- **B:** Incorrect for this question. Export entries to storage whose retention cannot be shortened. Why the correct answer wins: An organization-level constraint blocks such creation regardless of project ownership.
- **C:** Incorrect for this question. A key the customer owns and can rotate or revoke. Why the correct answer wins: An organization-level constraint blocks such creation regardless of project ownership.
- **D:** Incorrect for this question. A location choice that keeps data inside the regulated boundary. Why the correct answer wins: An organization-level constraint blocks such creation regardless of project ownership.

### Question 31 — C

Answer: Add the projects to a VPC Service Controls perimeter. A service perimeter blocks the copying path regardless of identity. A boundary that blocks data exfiltration even from an authorized identity. Local study-map skill 1.15 (Regulatory, Compliance, and Organization Policy), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 1 (design innovative, scalable, and highly available cloud database solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Copy the analytical slice into the warehouse on a schedule. Why the correct answer wins: A service perimeter blocks the copying path regardless of identity.
- **B:** Incorrect for this question. Keep an analytics copy current by applying change data capture. Why the correct answer wins: A service perimeter blocks the copying path regardless of identity.
- **C:** Correct. A boundary that blocks data exfiltration even from an authorized identity. In this case: A service perimeter blocks the copying path regardless of identity.
- **D:** Incorrect for this question. Read the operational table from BigQuery without copying it first. Why the correct answer wins: A service perimeter blocks the copying path regardless of identity.

### Question 32 — D, E

Answers: Query the source through BigQuery federated queries; Keep part of the estate on-premises with a hybrid link. A federated query reads the rows in place, and a hybrid link provides the private connectivity that path needs. Read the operational table from BigQuery without copying it first. Interconnect the remaining on-premises system rather than moving it. Local study-map skill 1.16 (Federation, Exports, and Hybrid Spans), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 1 (design innovative, scalable, and highly available cloud database solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Keep an analytics copy current by applying change data capture. Why the correct answer wins: A federated query reads the rows in place, and a hybrid link provides the private connectivity that path needs.
- **B:** Incorrect for this question. Keep the old system read-only for a defined period, then remove it. Why the correct answer wins: A federated query reads the rows in place, and a hybrid link provides the private connectivity that path needs.
- **C:** Incorrect for this question. Copy the analytical slice into the warehouse on a schedule. Why the correct answer wins: A federated query reads the rows in place, and a hybrid link provides the private connectivity that path needs.
- **D:** Correct. Read the operational table from BigQuery without copying it first. In this case: A federated query reads the rows in place, and a hybrid link provides the private connectivity that path needs.
- **E:** Correct. Interconnect the remaining on-premises system rather than moving it. In this case: A federated query reads the rows in place, and a hybrid link provides the private connectivity that path needs.

### Question 33 — C

Answer: Grant the predefined database role. A narrower predefined role supplies the read access without the write capability. A Google-managed role that carries the permissions the operator needs. Local study-map skill 2.1 (IAM for Database Connectivity), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 2 (manage a solution that can span multiple database technologies): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A broad legacy role that can change most resources in the project. Why the correct answer wins: A narrower predefined role supplies the read access without the write capability.
- **B:** Incorrect for this question. Individual accountability at the engine layer rather than a shared login. Why the correct answer wins: A narrower predefined role supplies the read access without the write capability.
- **C:** Correct. A Google-managed role that carries the permissions the operator needs. In this case: A narrower predefined role supplies the read access without the write capability.
- **D:** Incorrect for this question. A role built from an explicit permission list. Why the correct answer wins: A narrower predefined role supplies the read access without the write capability.

### Question 34 — C

Answer: Limit the user to the required schema. A grant scoped to that one schema gives exactly the access required. Grant access to named objects instead of the whole instance. Local study-map skill 2.1 (IAM for Database Connectivity), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 2 (manage a solution that can span multiple database technologies): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A role built from an explicit permission list. Why the correct answer wins: A grant scoped to that one schema gives exactly the access required.
- **B:** Incorrect for this question. A broad legacy role that can change most resources in the project. Why the correct answer wins: A grant scoped to that one schema gives exactly the access required.
- **C:** Correct. Grant access to named objects instead of the whole instance. In this case: A grant scoped to that one schema gives exactly the access required.
- **D:** Incorrect for this question. A single credential used by every workload that touches the database. Why the correct answer wins: A grant scoped to that one schema gives exactly the access required.

### Question 35 — C, D

Answers: Create one database user per person; Bind access to a Google group. Individual database users make each query attributable, and group membership makes revocation a single change. Individual accountability at the engine layer rather than a shared login. Manage membership in a group rather than editing bindings per person. Local study-map skill 2.2 (Database Users and Authentication), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 2 (manage a solution that can span multiple database technologies): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A single credential used by every workload that touches the database. Why the correct answer wins: Individual database users make each query attributable, and group membership makes revocation a single change.
- **B:** Incorrect for this question. A broad legacy role that can change most resources in the project. Why the correct answer wins: Individual database users make each query attributable, and group membership makes revocation a single change.
- **C:** Correct. Individual accountability at the engine layer rather than a shared login. In this case: Individual database users make each query attributable, and group membership makes revocation a single change.
- **D:** Correct. Manage membership in a group rather than editing bindings per person. In this case: Individual database users make each query attributable, and group membership makes revocation a single change.
- **E:** Incorrect for this question. A native database user whose credential must be rotated and stored. Why the correct answer wins: Individual database users make each query attributable, and group membership makes revocation a single change.

### Question 36 — D

Answer: Add the index the slow query needs. An index on the predicate turns the scan into a lookup. Local study-map skill 2.3 (Slow Queries and Missing Indexes), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 2 (manage a solution that can span multiple database technologies): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Split one table into ranges so pruning and maintenance act on less data. Why the correct answer wins: An index on the predicate turns the scan into a lookup.
- **B:** Incorrect for this question. Give the planner current cardinality so it stops choosing a poor plan. Why the correct answer wins: An index on the predicate turns the scan into a lookup.
- **C:** Incorrect for this question. Give sorts and joins more working memory on the instance. Why the correct answer wins: An index on the predicate turns the scan into a lookup.
- **D:** Correct. In this case: An index on the predicate turns the scan into a lookup.

### Question 37 — B

Answer: Refresh the table statistics. Refreshing statistics corrects the estimate that produces the poor plan. Give the planner current cardinality so it stops choosing a poor plan. Local study-map skill 2.3 (Slow Queries and Missing Indexes), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 2 (manage a solution that can span multiple database technologies): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Give sorts and joins more working memory on the instance. Why the correct answer wins: Refreshing statistics corrects the estimate that produces the poor plan.
- **B:** Correct. Give the planner current cardinality so it stops choosing a poor plan. In this case: Refreshing statistics corrects the estimate that produces the poor plan.
- **C:** Incorrect for this question. Remove write amplification from an index nothing reads. Why the correct answer wins: Refreshing statistics corrects the estimate that produces the poor plan.
- **D:** Incorrect for this question. Create an index that turns a scan into a lookup for the predicate. Why the correct answer wins: Refreshing statistics corrects the estimate that produces the poor plan.

### Question 38 — C

Answer: Batch the writes into fewer round trips. Committing in batches shortens the lock window. Cut per-row network and commit overhead in the application. Local study-map skill 2.4 (Locking and Resource Contention), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 2 (manage a solution that can span multiple database technologies): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. End the blocking transaction so the queue drains. Why the correct answer wins: Committing in batches shortens the lock window.
- **B:** Incorrect for this question. A pooler that multiplexes many application connections onto few database sessions. Why the correct answer wins: Committing in batches shortens the lock window.
- **C:** Correct. Cut per-row network and commit overhead in the application. In this case: Committing in batches shortens the lock window.
- **D:** Incorrect for this question. Find the transaction that holds the lock others wait on. Why the correct answer wins: Committing in batches shortens the lock window.

### Question 39 — B

Answer: Inspect lock waits and blocking sessions. The lock graph names the blocking session. Find the transaction that holds the lock others wait on. Local study-map skill 2.4 (Locking and Resource Contention), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 2 (manage a solution that can span multiple database technologies): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Give the planner current cardinality so it stops choosing a poor plan. Why the correct answer wins: The lock graph names the blocking session.
- **B:** Correct. Find the transaction that holds the lock others wait on. In this case: The lock graph names the blocking session.
- **C:** Incorrect for this question. Cut per-row network and commit overhead in the application. Why the correct answer wins: The lock graph names the blocking session.
- **D:** Incorrect for this question. Create an index that turns a scan into a lookup for the predicate. Why the correct answer wins: The lock graph names the blocking session.

### Question 40 — A, D

Answers: Watch CPU, memory, disk, and IOPS together; Use Query Insights to find the heavy statements. Resource vitals show the ceiling that moved, and per-query data shows the statements affected. Read the instance-level signals before attributing the symptom to the query. A per-query view of latency, load, and wait events on the instance. Local study-map skill 2.5 (Database Vitals Monitoring), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 2 (manage a solution that can span multiple database technologies): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Correct. Read the instance-level signals before attributing the symptom to the query. In this case: Resource vitals show the ceiling that moved, and per-query data shows the statements affected.
- **B:** Incorrect for this question. A single view of health, security, and version posture across database instances. Why the correct answer wins: Resource vitals show the ceiling that moved, and per-query data shows the statements affected.
- **C:** Incorrect for this question. Turn a recurring log pattern into a metric that can be charted and alerted on. Why the correct answer wins: Resource vitals show the ceiling that moved, and per-query data shows the statements affected.
- **D:** Correct. A per-query view of latency, load, and wait events on the instance. In this case: Resource vitals show the ceiling that moved, and per-query data shows the statements affected.
- **E:** Incorrect for this question. The engine log of statements that exceeded the long-query threshold. Why the correct answer wins: Resource vitals show the ceiling that moved, and per-query data shows the statements affected.

### Question 41 — A

Answer: Build a log-based metric from the error entries. A metric derived from the log pattern makes the trend measurable. Turn a recurring log pattern into a metric that can be charted and alerted on. Local study-map skill 2.5 (Database Vitals Monitoring), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 2 (manage a solution that can span multiple database technologies): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Correct. Turn a recurring log pattern into a metric that can be charted and alerted on. In this case: A metric derived from the log pattern makes the trend measurable.
- **B:** Incorrect for this question. A liveness signal that fires before users report the outage. Why the correct answer wins: A metric derived from the log pattern makes the trend measurable.
- **C:** Incorrect for this question. The engine log of statements that exceeded the long-query threshold. Why the correct answer wins: A metric derived from the log pattern makes the trend measurable.
- **D:** Incorrect for this question. Export entries to storage whose retention cannot be shortened. Why the correct answer wins: A metric derived from the log pattern makes the trend measurable.

### Question 42 — B

Answer: Request a quota increase for the project. The project ceiling has to be raised so the response can run in parallel, since retries would hit the same limit. Raise the project-level ceiling so the operation is no longer refused. Local study-map skill 2.6 (Quotas and Limits), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 2 (manage a solution that can span multiple database technologies): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Repeat the call after a growing delay so a transient refusal clears. Why the correct answer wins: The project ceiling has to be raised so the response can run in parallel, since retries would hit the same limit.
- **B:** Correct. Raise the project-level ceiling so the operation is no longer refused. In this case: The project ceiling has to be raised so the response can run in parallel, since retries would hit the same limit.
- **C:** Incorrect for this question. Stagger the work so concurrent operations stop colliding on the same limit. Why the correct answer wins: The project ceiling has to be raised so the response can run in parallel, since retries would hit the same limit.
- **D:** Incorrect for this question. A flat-file extract for a downstream loader rather than a restore. Why the correct answer wins: The project ceiling has to be raised so the response can run in parallel, since retries would hit the same limit.

### Question 43 — B, D

Answers: Alert on the database error rate; Alert on replication lag. Alerting on failed statements pages on what users feel, and alerting on lag reports the staleness nobody currently sees. Page on failed statements rather than on resource saturation alone. Page when the copy falls behind the primary by more than the budget. Local study-map skill 2.7 (Alerts for Errors and Performance), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 2 (manage a solution that can span multiple database technologies): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A condition that pages a human when the threshold is crossed. Why the correct answer wins: Alerting on failed statements pages on what users feel, and alerting on lag reports the staleness nobody currently sees.
- **B:** Correct. Page on failed statements rather than on resource saturation alone. In this case: Alerting on failed statements pages on what users feel, and alerting on lag reports the staleness nobody currently sees.
- **C:** Incorrect for this question. Turn a recurring log pattern into a metric that can be charted and alerted on. Why the correct answer wins: Alerting on failed statements pages on what users feel, and alerting on lag reports the staleness nobody currently sees.
- **D:** Correct. Page when the copy falls behind the primary by more than the budget. In this case: Alerting on failed statements pages on what users feel, and alerting on lag reports the staleness nobody currently sees.
- **E:** Incorrect for this question. Read the instance-level signals before attributing the symptom to the query. Why the correct answer wins: Alerting on failed statements pages on what users feel, and alerting on lag reports the staleness nobody currently sees.

### Question 44 — C

Answer: Create an alerting policy on the metric. An alerting policy on the role signal notifies the team automatically. A condition that pages a human when the threshold is crossed. Local study-map skill 2.7 (Alerts for Errors and Performance), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 2 (manage a solution that can span multiple database technologies): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Page when the copy falls behind the primary by more than the budget. Why the correct answer wins: An alerting policy on the role signal notifies the team automatically.
- **B:** Incorrect for this question. A per-query view of latency, load, and wait events on the instance. Why the correct answer wins: An alerting policy on the role signal notifies the team automatically.
- **C:** Correct. A condition that pages a human when the threshold is crossed. In this case: An alerting policy on the role signal notifies the team automatically.
- **D:** Incorrect for this question. Page on failed statements rather than on resource saturation alone. Why the correct answer wins: An alerting policy on the role signal notifies the team automatically.

### Question 45 — B

Answer: Enable point-in-time recovery. Point-in-time recovery returns the instance to the moment before the deletion. Continuous log capture that lets the instance return to an arbitrary moment. Local study-map skill 2.8 (Backup and Recovery Option Selection), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 2 (manage a solution that can span multiple database technologies): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Scheduled backups kept for a chosen number of days. Why the correct answer wins: Point-in-time recovery returns the instance to the moment before the deletion.
- **B:** Correct. Continuous log capture that lets the instance return to an arbitrary moment. In this case: Point-in-time recovery returns the instance to the moment before the deletion.
- **C:** Incorrect for this question. Keep backups longer so an older restore point remains available. Why the correct answer wins: Point-in-time recovery returns the instance to the moment before the deletion.
- **D:** Incorrect for this question. A portable SQL dump taken with the engine tooling. Why the correct answer wins: Point-in-time recovery returns the instance to the moment before the deletion.

### Question 46 — A

Answer: Enable automated backups with a retention window. Automated backups give a managed schedule and retention. Scheduled backups kept for a chosen number of days. Local study-map skill 2.8 (Backup and Recovery Option Selection), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 2 (manage a solution that can span multiple database technologies): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Correct. Scheduled backups kept for a chosen number of days. In this case: Automated backups give a managed schedule and retention.
- **B:** Incorrect for this question. A flat-file extract for a downstream loader rather than a restore. Why the correct answer wins: Automated backups give a managed schedule and retention.
- **C:** Incorrect for this question. A manual checkpoint taken immediately before a risky operation. Why the correct answer wins: Automated backups give a managed schedule and retention.
- **D:** Incorrect for this question. A copy of the current data created without touching the source. Why the correct answer wins: Automated backups give a managed schedule and retention.

### Question 47 — A, B

Answers: Export the table to CSV in Cloud Storage; Add a lifecycle rule to the export bucket. A flat-file export is what the loader consumes, and a lifecycle rule bounds how long the files remain. A flat-file extract for a downstream loader rather than a restore. Move or delete aged exports so the bucket does not grow without limit. Local study-map skill 2.9 (Export and Import Configuration), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 2 (manage a solution that can span multiple database technologies): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Correct. Move or delete aged exports so the bucket does not grow without limit. In this case: A flat-file export is what the loader consumes, and a lifecycle rule bounds how long the files remain.
- **B:** Correct. A flat-file extract for a downstream loader rather than a restore. In this case: A flat-file export is what the loader consumes, and a lifecycle rule bounds how long the files remain.
- **C:** Incorrect for this question. A recurring trigger that performs the work with nobody present. Why the correct answer wins: A flat-file export is what the loader consumes, and a lifecycle rule bounds how long the files remain.
- **D:** Incorrect for this question. A portable SQL dump taken with the engine tooling. Why the correct answer wins: A flat-file export is what the loader consumes, and a lifecycle rule bounds how long the files remain.
- **E:** Incorrect for this question. Load a logical dump file into the database through the managed import path. Why the correct answer wins: A flat-file export is what the loader consumes, and a lifecycle rule bounds how long the files remain.

### Question 48 — D

Answer: Design the restore path to the stated RTO and RPO. The recovery point and time objectives state the acceptable loss and duration. Choose mechanisms by how much data and time the business can lose. Local study-map skill 2.10 (RTO, RPO, and Point-in-Time Recovery), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 2 (manage a solution that can span multiple database technologies): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Scheduled backups kept for a chosen number of days. Why the correct answer wins: The recovery point and time objectives state the acceptable loss and duration.
- **B:** Incorrect for this question. A copy of the current data created without touching the source. Why the correct answer wins: The recovery point and time objectives state the acceptable loss and duration.
- **C:** Incorrect for this question. Continuous log capture that lets the instance return to an arbitrary moment. Why the correct answer wins: The recovery point and time objectives state the acceptable loss and duration.
- **D:** Correct. Choose mechanisms by how much data and time the business can lose. In this case: The recovery point and time objectives state the acceptable loss and duration.

### Question 49 — B

Answer: Add a cross-region read replica. A promotable remote copy avoids the restore entirely. A copy in a second region that serves reads and can be promoted. Local study-map skill 2.10 (RTO, RPO, and Point-in-Time Recovery), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 2 (manage a solution that can span multiple database technologies): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A point-in-time restore that discards the later writes on the same instance. Why the correct answer wins: A promotable remote copy avoids the restore entirely.
- **B:** Correct. A copy in a second region that serves reads and can be promoted. In this case: A promotable remote copy avoids the restore entirely.
- **C:** Incorrect for this question. Keep backups longer so an older restore point remains available. Why the correct answer wins: A promotable remote copy avoids the restore entirely.
- **D:** Incorrect for this question. A recovery point that makes the upgrade reversible in practice. Why the correct answer wins: A promotable remote copy avoids the restore entirely.

### Question 50 — D

Answer: Apply a row-level retention policy. A row-level retention rule enforces the deletion on the operational rows. Delete or expire records once the legal hold period ends. Local study-map skill 2.11 (Data Retention Management), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 2 (manage a solution that can span multiple database technologies): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Expire documents once their usefulness ends. Why the correct answer wins: A row-level retention rule enforces the deletion on the operational rows.
- **B:** Incorrect for this question. Move aged, rarely read rows out of the hot table into Cloud Storage or BigQuery. Why the correct answer wins: A row-level retention rule enforces the deletion on the operational rows.
- **C:** Incorrect for this question. A rule that drops versions by age or count, which also bounds recovery. Why the correct answer wins: A row-level retention rule enforces the deletion on the operational rows.
- **D:** Correct. Delete or expire records once the legal hold period ends. In this case: A row-level retention rule enforces the deletion on the operational rows.

### Question 51 — B

Answer: Add a read replica for the read traffic. A read replica supplies the extra read capacity. Send reads to a copy so the primary keeps its capacity for writes. Local study-map skill 2.12 (Scaling Up Versus Scaling Out), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 2 (manage a solution that can span multiple database technologies): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Split rows by a key so each instance owns a subset of the workload. Why the correct answer wins: A read replica supplies the extra read capacity.
- **B:** Correct. Send reads to a copy so the primary keeps its capacity for writes. In this case: A read replica supplies the extra read capacity.
- **C:** Incorrect for this question. Move the instance to a larger shape so more vCPU and memory serve the same data. Why the correct answer wins: A read replica supplies the extra read capacity.
- **D:** Incorrect for this question. Grow the AlloyDB read pool that serves read-only connections. Why the correct answer wins: A read replica supplies the extra read capacity.

### Question 52 — C

Answer: Increase the machine type of the instance. A larger shape carries the existing write load until the application can change. Move the instance to a larger shape so more vCPU and memory serve the same data. Local study-map skill 2.12 (Scaling Up Versus Scaling Out), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 2 (manage a solution that can span multiple database technologies): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Absorb repeated reads in memory so the database sees fewer of them. Why the correct answer wins: A larger shape carries the existing write load until the application can change.
- **B:** Incorrect for this question. Send reads to a copy so the primary keeps its capacity for writes. Why the correct answer wins: A larger shape carries the existing write load until the application can change.
- **C:** Correct. Move the instance to a larger shape so more vCPU and memory serve the same data. In this case: A larger shape carries the existing write load until the application can change.
- **D:** Incorrect for this question. Separate analytical reads from the write path. Why the correct answer wins: A larger shape carries the existing write load until the application can change.

### Question 53 — C

Answer: Stream changes with Datastream. Change data capture publishes each committed change to the warehouse without touching the transactional path. Change data capture from the source into a Google Cloud target. Local study-map skill 2.13 (Replication Strategies), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 2 (manage a solution that can span multiple database technologies): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Read the operational table from BigQuery without copying it first. Why the correct answer wins: Change data capture publishes each committed change to the warehouse without touching the transactional path.
- **B:** Incorrect for this question. A bulk load followed by a catch-up pass for the writes made during the load. Why the correct answer wins: Change data capture publishes each committed change to the warehouse without touching the transactional path.
- **C:** Correct. Change data capture from the source into a Google Cloud target. In this case: Change data capture publishes each committed change to the warehouse without touching the transactional path.
- **D:** Incorrect for this question. A flat-file extract for a downstream loader rather than a restore. Why the correct answer wins: Change data capture publishes each committed change to the warehouse without touching the transactional path.

### Question 54 — A

Answer: Cache the hot read path in Memorystore. Caching the repeated reads absorbs the load before it reaches the database. Absorb repeated reads in memory so the database sees fewer of them. Local study-map skill 2.14 (Query Optimization for Cost and Performance), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 2 (manage a solution that can span multiple database technologies): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Correct. Absorb repeated reads in memory so the database sees fewer of them. In this case: Caching the repeated reads absorbs the load before it reaches the database.
- **B:** Incorrect for this question. Create an index that turns a scan into a lookup for the predicate. Why the correct answer wins: Caching the repeated reads absorbs the load before it reaches the database.
- **C:** Incorrect for this question. Split one table into ranges so pruning and maintenance act on less data. Why the correct answer wins: Caching the repeated reads absorbs the load before it reaches the database.
- **D:** Incorrect for this question. Give sorts and joins more working memory on the instance. Why the correct answer wins: Caching the repeated reads absorbs the load before it reaches the database.

### Question 55 — A

Answer: Run the task on a managed schedule. A managed schedule performs the recurring work unattended. A recurring trigger that performs the work with nobody present. Local study-map skill 2.15 (Automated Maintenance and Scheduled Exports), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 2 (manage a solution that can span multiple database technologies): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Correct. A recurring trigger that performs the work with nobody present. In this case: A managed schedule performs the recurring work unattended.
- **B:** Incorrect for this question. Create the resource interactively with no stored definition. Why the correct answer wins: A managed schedule performs the recurring work unattended.
- **C:** Incorrect for this question. Trigger a switchover in a test window and observe how long writes are unavailable. Why the correct answer wins: A managed schedule performs the recurring work unattended.
- **D:** Incorrect for this question. A manual checkpoint taken immediately before a risky operation. Why the correct answer wins: A managed schedule performs the recurring work unattended.

### Question 56 — B

Answer: Test the upgrade on a clone first. Testing on a clone exposes the breakage while production is untouched. Rehearse the change against a copy before touching production. Local study-map skill 2.15 (Automated Maintenance and Scheduled Exports), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 2 (manage a solution that can span multiple database technologies): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Compare the signal after cutover against the pre-change baseline. Why the correct answer wins: Testing on a clone exposes the breakage while production is untouched.
- **B:** Correct. Rehearse the change against a copy before touching production. In this case: Testing on a clone exposes the breakage while production is untouched.
- **C:** Incorrect for this question. Change the engine version on the running instance during the window. Why the correct answer wins: Testing on a clone exposes the breakage while production is untouched.
- **D:** Incorrect for this question. A recovery point that makes the upgrade reversible in practice. Why the correct answer wins: Testing on a clone exposes the breakage while production is untouched.

### Question 57 — C

Answer: Track the availability signal against the agreed objective. Comparing the availability signal against the committed objective answers the question. Compare observed service levels with the commitment rather than watching raw resource metrics. Local study-map skill 2.16 (Managed Upgrades and SLA Monitoring), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 2 (manage a solution that can span multiple database technologies): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A single view of health, security, and version posture across database instances. Why the correct answer wins: Comparing the availability signal against the committed objective answers the question.
- **B:** Incorrect for this question. A condition that pages a human when the threshold is crossed. Why the correct answer wins: Comparing the availability signal against the committed objective answers the question.
- **C:** Correct. Compare observed service levels with the commitment rather than watching raw resource metrics. In this case: Comparing the availability signal against the committed objective answers the question.
- **D:** Incorrect for this question. Read the instance-level signals before attributing the symptom to the query. Why the correct answer wins: Comparing the availability signal against the committed objective answers the question.

### Question 58 — D

Answer: Use Database Migration Service for the same engine. Continuous replication with a managed migration fits the window without application work. A managed migration that moves a supported engine to the same engine on Google Cloud. Local study-map skill 3.1 (Migration Strategy and Downtime Budget), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 3 (migrate data solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A bulk load followed by a catch-up pass for the writes made during the load. Why the correct answer wins: Continuous replication with a managed migration fits the window without application work.
- **B:** Incorrect for this question. Stop the source, load everything, and start the target in one window. Why the correct answer wins: Continuous replication with a managed migration fits the window without application work.
- **C:** Incorrect for this question. Keep two databases current from application code during the transition. Why the correct answer wins: Continuous replication with a managed migration fits the window without application work.
- **D:** Correct. A managed migration that moves a supported engine to the same engine on Google Cloud. In this case: Continuous replication with a managed migration fits the window without application work.

### Question 59 — B

Answer: Accept a scheduled extended outage. A stop, load, and start in an accepted window needs no replication topology. Stop the source, load everything, and start the target in one window. Local study-map skill 3.1 (Migration Strategy and Downtime Budget), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 3 (migrate data solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A rehearsed sequence with a named decision point and a way back. Why the correct answer wins: A stop, load, and start in an accepted window needs no replication topology.
- **B:** Correct. Stop the source, load everything, and start the target in one window. In this case: A stop, load, and start in an accepted window needs no replication topology.
- **C:** Incorrect for this question. Keep two databases current from application code during the transition. Why the correct answer wins: A stop, load, and start in an accepted window needs no replication topology.
- **D:** Incorrect for this question. A managed migration that moves a supported engine to the same engine on Google Cloud. Why the correct answer wins: A stop, load, and start in an accepted window needs no replication topology.

### Question 60 — D

Answer: Follow a cutover runbook with a rollback step. A runbook with owners and an abort condition makes the cutover repeatable. A rehearsed sequence with a named decision point and a way back. Local study-map skill 3.1 (Migration Strategy and Downtime Budget), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 3 (migrate data solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Stop application writes so the last increment can be applied cleanly. Why the correct answer wins: A runbook with owners and an abort condition makes the cutover repeatable.
- **B:** Incorrect for this question. Keep two databases current from application code during the transition. Why the correct answer wins: A runbook with owners and an abort condition makes the cutover repeatable.
- **C:** Incorrect for this question. Stop the source, load everything, and start the target in one window. Why the correct answer wins: A runbook with owners and an abort condition makes the cutover repeatable.
- **D:** Correct. A rehearsed sequence with a named decision point and a way back. In this case: A runbook with owners and an abort condition makes the cutover repeatable.

### Question 61 — B, D

Answers: Use Database Migration Service with schema conversion; Stream changes with Datastream. The heterogeneous migration handles the cutover, and change data capture feeds the warehouse while the source stays live. A managed path that converts schema and code from a different source engine. Change data capture from the source into a Google Cloud target. Local study-map skill 3.2 (Migration Tool Selection), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 3 (migrate data solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A bulk load followed by a catch-up pass for the writes made during the load. Why the correct answer wins: The heterogeneous migration handles the cutover, and change data capture feeds the warehouse while the source stays live.
- **B:** Correct. Change data capture from the source into a Google Cloud target. In this case: The heterogeneous migration handles the cutover, and change data capture feeds the warehouse while the source stays live.
- **C:** Incorrect for this question. Replay the writes made during the bulk load so the target is current at the switch. Why the correct answer wins: The heterogeneous migration handles the cutover, and change data capture feeds the warehouse while the source stays live.
- **D:** Correct. A managed path that converts schema and code from a different source engine. In this case: The heterogeneous migration handles the cutover, and change data capture feeds the warehouse while the source stays live.
- **E:** Incorrect for this question. Keep two databases current from application code during the transition. Why the correct answer wins: The heterogeneous migration handles the cutover, and change data capture feeds the warehouse while the source stays live.

### Question 62 — D

Answer: Dump, restore, then replay the changes. A dump and restore copies the data once. A bulk load followed by a catch-up pass for the writes made during the load. Local study-map skill 3.2 (Migration Tool Selection), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 3 (migrate data solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Keep writing back to the original system so a rollback loses nothing. Why the correct answer wins: A dump and restore copies the data once.
- **B:** Incorrect for this question. A managed path that converts schema and code from a different source engine. Why the correct answer wins: A dump and restore copies the data once.
- **C:** Incorrect for this question. Keep two databases current from application code during the transition. Why the correct answer wins: A dump and restore copies the data once.
- **D:** Correct. A bulk load followed by a catch-up pass for the writes made during the load. In this case: A dump and restore copies the data once.

### Question 63 — D

Answer: Use Database Migration Service for the same engine. A same-engine managed migration with continuous replication fits an hour even at that size. A managed migration that moves a supported engine to the same engine on Google Cloud. Local study-map skill 3.2 (Migration Tool Selection), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 3 (migrate data solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A bulk load followed by a catch-up pass for the writes made during the load. Why the correct answer wins: A same-engine managed migration with continuous replication fits an hour even at that size.
- **B:** Incorrect for this question. Keep two databases current from application code during the transition. Why the correct answer wins: A same-engine managed migration with continuous replication fits an hour even at that size.
- **C:** Incorrect for this question. Change data capture from the source into a Google Cloud target. Why the correct answer wins: A same-engine managed migration with continuous replication fits an hour even at that size.
- **D:** Correct. A managed migration that moves a supported engine to the same engine on Google Cloud. In this case: A same-engine managed migration with continuous replication fits an hour even at that size.

### Question 64 — B

Answer: Build the schema in a conversion workspace. The conversion workspace holds the generated schema and code for review and editing. Convert DDL and code with reviewable, editable output before the load starts. Local study-map skill 3.3 (Heterogeneous Schema and DDL Conversion), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 3 (migrate data solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Port procedural code the conversion tool flags as unsupported. Why the correct answer wins: The conversion workspace holds the generated schema and code for review and editing.
- **B:** Correct. Convert DDL and code with reviewable, editable output before the load starts. In this case: The conversion workspace holds the generated schema and code for review and editing.
- **C:** Incorrect for this question. Compare the target answers with production before the switch. Why the correct answer wins: The conversion workspace holds the generated schema and code for review and editing.
- **D:** Incorrect for this question. Set generated-key counters past the highest value so inserts do not collide. Why the correct answer wins: The conversion workspace holds the generated schema and code for review and editing.

### Question 65 — C

Answer: Rewrite the stored procedures and DML by hand. Procedural logic with no target equivalent has to be rewritten by hand. Port procedural code the conversion tool flags as unsupported. Local study-map skill 3.3 (Heterogeneous Schema and DDL Conversion), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 3 (migrate data solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Set generated-key counters past the highest value so inserts do not collide. Why the correct answer wins: Procedural logic with no target equivalent has to be rewritten by hand.
- **B:** Incorrect for this question. Keep two databases current from application code during the transition. Why the correct answer wins: Procedural logic with no target equivalent has to be rewritten by hand.
- **C:** Correct. Port procedural code the conversion tool flags as unsupported. In this case: Procedural logic with no target equivalent has to be rewritten by hand.
- **D:** Incorrect for this question. Convert DDL and code with reviewable, editable output before the load starts. Why the correct answer wins: Procedural logic with no target equivalent has to be rewritten by hand.

### Question 66 — A

Answer: Replay read traffic against the target. Replaying those statements and comparing answers tests behaviour directly. Compare the target answers with production before the switch. Local study-map skill 3.4 (DML and Application Code Conversion), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 3 (migrate data solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Correct. Compare the target answers with production before the switch. In this case: Replaying those statements and comparing answers tests behaviour directly.
- **B:** Incorrect for this question. Port procedural code the conversion tool flags as unsupported. Why the correct answer wins: Replaying those statements and comparing answers tests behaviour directly.
- **C:** Incorrect for this question. A rehearsed sequence with a named decision point and a way back. Why the correct answer wins: Replaying those statements and comparing answers tests behaviour directly.
- **D:** Incorrect for this question. Prove the target holds the same rows as the source before cutover. Why the correct answer wins: Replaying those statements and comparing answers tests behaviour directly.

### Question 67 — B

Answer: Rewrite the stored procedures and DML by hand. The statements have to be rewritten for the target dialect. Port procedural code the conversion tool flags as unsupported. Local study-map skill 3.4 (DML and Application Code Conversion), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 3 (migrate data solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Keep two databases current from application code during the transition. Why the correct answer wins: The statements have to be rewritten for the target dialect.
- **B:** Correct. Port procedural code the conversion tool flags as unsupported. In this case: The statements have to be rewritten for the target dialect.
- **C:** Incorrect for this question. Convert DDL and code with reviewable, editable output before the load starts. Why the correct answer wins: The statements have to be rewritten for the target dialect.
- **D:** Incorrect for this question. Set generated-key counters past the highest value so inserts do not collide. Why the correct answer wins: The statements have to be rewritten for the target dialect.

### Question 68 — C, D

Answers: Use the engine native logical replication; Apply the captured change backlog before cutover. Replicating changes during the load keeps the target close, and applying the remaining backlog finishes the catch-up. Replicate row changes from the source using the engine feature itself. Replay the writes made during the bulk load so the target is current at the switch. Local study-map skill 3.5 (Initial Load and Change Replication), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 3 (migrate data solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Keep two databases current from application code during the transition. Why the correct answer wins: Replicating changes during the load keeps the target close, and applying the remaining backlog finishes the catch-up.
- **B:** Incorrect for this question. Stop the source, load everything, and start the target in one window. Why the correct answer wins: Replicating changes during the load keeps the target close, and applying the remaining backlog finishes the catch-up.
- **C:** Correct. Replay the writes made during the bulk load so the target is current at the switch. In this case: Replicating changes during the load keeps the target close, and applying the remaining backlog finishes the catch-up.
- **D:** Correct. Replicate row changes from the source using the engine feature itself. In this case: Replicating changes during the load keeps the target close, and applying the remaining backlog finishes the catch-up.
- **E:** Incorrect for this question. A portable SQL dump taken with the engine tooling. Why the correct answer wins: Replicating changes during the load keeps the target close, and applying the remaining backlog finishes the catch-up.

### Question 69 — C

Answer: Measure the catch-up rate before choosing the window. The observed replay rate against the backlog shows whether the window can hold. Size the cutover from how fast changes replay, not from the data volume alone. Local study-map skill 3.5 (Initial Load and Change Replication), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 3 (migrate data solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Move clients to the new endpoint as the final cutover action. Why the correct answer wins: The observed replay rate against the backlog shows whether the window can hold.
- **B:** Incorrect for this question. Stop application writes so the last increment can be applied cleanly. Why the correct answer wins: The observed replay rate against the backlog shows whether the window can hold.
- **C:** Correct. Size the cutover from how fast changes replay, not from the data volume alone. In this case: The observed replay rate against the backlog shows whether the window can hold.
- **D:** Incorrect for this question. Prove the target holds the same rows as the source before cutover. Why the correct answer wins: The observed replay rate against the backlog shows whether the window can hold.

### Question 70 — B, E

Answers: Reconcile row counts and checksums; Run the task on a managed schedule. A managed schedule repeats the validation without an operator, and row and checksum comparison proves the data matches. Prove the target holds the same rows as the source before cutover. A recurring trigger that performs the work with nobody present. Local study-map skill 3.6 (Validation and Reconciliation), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 3 (migrate data solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A rehearsed sequence with a named decision point and a way back. Why the correct answer wins: A managed schedule repeats the validation without an operator, and row and checksum comparison proves the data matches.
- **B:** Correct. A recurring trigger that performs the work with nobody present. In this case: A managed schedule repeats the validation without an operator, and row and checksum comparison proves the data matches.
- **C:** Incorrect for this question. Move clients to the new endpoint as the final cutover action. Why the correct answer wins: A managed schedule repeats the validation without an operator, and row and checksum comparison proves the data matches.
- **D:** Incorrect for this question. Compare the target answers with production before the switch. Why the correct answer wins: A managed schedule repeats the validation without an operator, and row and checksum comparison proves the data matches.
- **E:** Correct. Prove the target holds the same rows as the source before cutover. In this case: A managed schedule repeats the validation without an operator, and row and checksum comparison proves the data matches.

### Question 71 — C

Answer: Replay read traffic against the target. Running the report statements on both systems and comparing totals tests the behaviour. Compare the target answers with production before the switch. Local study-map skill 3.6 (Validation and Reconciliation), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 3 (migrate data solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Keep two databases current from application code during the transition. Why the correct answer wins: Running the report statements on both systems and comparing totals tests the behaviour.
- **B:** Incorrect for this question. Prove the target holds the same rows as the source before cutover. Why the correct answer wins: Running the report statements on both systems and comparing totals tests the behaviour.
- **C:** Correct. Compare the target answers with production before the switch. In this case: Running the report statements on both systems and comparing totals tests the behaviour.
- **D:** Incorrect for this question. A rehearsed sequence with a named decision point and a way back. Why the correct answer wins: Running the report statements on both systems and comparing totals tests the behaviour.

### Question 72 — D

Answer: Freeze writes during the cutover. Stopping writes on the source gives the increment a stable target. Stop application writes so the last increment can be applied cleanly. Local study-map skill 3.7 (Cutover and Fallback Planning), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 3 (migrate data solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Move clients to the new endpoint as the final cutover action. Why the correct answer wins: Stopping writes on the source gives the increment a stable target.
- **B:** Incorrect for this question. Stop the source, load everything, and start the target in one window. Why the correct answer wins: Stopping writes on the source gives the increment a stable target.
- **C:** Incorrect for this question. Keep writing back to the original system so a rollback loses nothing. Why the correct answer wins: Stopping writes on the source gives the increment a stable target.
- **D:** Correct. Stop application writes so the last increment can be applied cleanly. In this case: Stopping writes on the source gives the increment a stable target.

### Question 73 — D

Answer: Repoint the connection string at the target. Repointing the connection string moves the clients to the target. Move clients to the new endpoint as the final cutover action. Local study-map skill 3.7 (Cutover and Fallback Planning), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 3 (migrate data solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A client library that resolves the instance and authorizes the connection with IAM. Why the correct answer wins: Repointing the connection string moves the clients to the target.
- **B:** Incorrect for this question. Stop application writes so the last increment can be applied cleanly. Why the correct answer wins: Repointing the connection string moves the clients to the target.
- **C:** Incorrect for this question. A rehearsed sequence with a named decision point and a way back. Why the correct answer wins: Repointing the connection string moves the clients to the target.
- **D:** Correct. Move clients to the new endpoint as the final cutover action. In this case: Repointing the connection string moves the clients to the target.

### Question 74 — D

Answer: Follow a cutover runbook with a rollback step. The runbook's abort condition and rollback steps define what happens next. A rehearsed sequence with a named decision point and a way back. Local study-map skill 3.7 (Cutover and Fallback Planning), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 3 (migrate data solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Move clients to the new endpoint as the final cutover action. Why the correct answer wins: The runbook's abort condition and rollback steps define what happens next.
- **B:** Incorrect for this question. Stop application writes so the last increment can be applied cleanly. Why the correct answer wins: The runbook's abort condition and rollback steps define what happens next.
- **C:** Incorrect for this question. Keep two databases current from application code during the transition. Why the correct answer wins: The runbook's abort condition and rollback steps define what happens next.
- **D:** Correct. A rehearsed sequence with a named decision point and a way back. In this case: The runbook's abort condition and rollback steps define what happens next.

### Question 75 — C, E

Answers: Set up reverse replication to the source; Decommission the source after a parallel period. Replication back to the source keeps the rollback lossless, and a parallel period with exit criteria ends it. Keep writing back to the original system so a rollback loses nothing. Keep the old system read-only for a defined period, then remove it. Local study-map skill 3.8 (Reverse Replication to the Source), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 3 (migrate data solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Stop the source, load everything, and start the target in one window. Why the correct answer wins: Replication back to the source keeps the rollback lossless, and a parallel period with exit criteria ends it.
- **B:** Incorrect for this question. Stop application writes so the last increment can be applied cleanly. Why the correct answer wins: Replication back to the source keeps the rollback lossless, and a parallel period with exit criteria ends it.
- **C:** Correct. Keep the old system read-only for a defined period, then remove it. In this case: Replication back to the source keeps the rollback lossless, and a parallel period with exit criteria ends it.
- **D:** Incorrect for this question. Move clients to the new endpoint as the final cutover action. Why the correct answer wins: Replication back to the source keeps the rollback lossless, and a parallel period with exit criteria ends it.
- **E:** Correct. Keep writing back to the original system so a rollback loses nothing. In this case: Replication back to the source keeps the rollback lossless, and a parallel period with exit criteria ends it.

### Question 76 — A

Answer: Set up reverse replication to the source. Replication from the target back to the source publishes those writes. Keep writing back to the original system so a rollback loses nothing. Local study-map skill 3.8 (Reverse Replication to the Source), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 3 (migrate data solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Correct. Keep writing back to the original system so a rollback loses nothing. In this case: Replication from the target back to the source publishes those writes.
- **B:** Incorrect for this question. Move clients to the new endpoint as the final cutover action. Why the correct answer wins: Replication from the target back to the source publishes those writes.
- **C:** Incorrect for this question. Keep the old system read-only for a defined period, then remove it. Why the correct answer wins: Replication from the target back to the source publishes those writes.
- **D:** Incorrect for this question. Keep two databases current from application code during the transition. Why the correct answer wins: Replication from the target back to the source publishes those writes.

### Question 77 — B

Answer: Use the engine native logical replication. Keeping replication running to the target preserves the path to retry without a reload. Replicate row changes from the source using the engine feature itself. Local study-map skill 3.9 (Minimizing Downtime During Migration), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 3 (migrate data solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Keep two databases current from application code during the transition. Why the correct answer wins: Keeping replication running to the target preserves the path to retry without a reload.
- **B:** Correct. Replicate row changes from the source using the engine feature itself. In this case: Keeping replication running to the target preserves the path to retry without a reload.
- **C:** Incorrect for this question. Stop the source, load everything, and start the target in one window. Why the correct answer wins: Keeping replication running to the target preserves the path to retry without a reload.
- **D:** Incorrect for this question. A bulk load followed by a catch-up pass for the writes made during the load. Why the correct answer wins: Keeping replication running to the target preserves the path to retry without a reload.

### Question 78 — A

Answer: Move the job outside the contention window. Scheduling away from the predictable surge keeps the catch-up inside the window. Stagger the work so concurrent operations stop colliding on the same limit. Local study-map skill 3.9 (Minimizing Downtime During Migration), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 3 (migrate data solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Correct. Stagger the work so concurrent operations stop colliding on the same limit. In this case: Scheduling away from the predictable surge keeps the catch-up inside the window.
- **B:** Incorrect for this question. Keep two databases current from application code during the transition. Why the correct answer wins: Scheduling away from the predictable surge keeps the catch-up inside the window.
- **C:** Incorrect for this question. Size the cutover from how fast changes replay, not from the data volume alone. Why the correct answer wins: Scheduling away from the predictable surge keeps the catch-up inside the window.
- **D:** Incorrect for this question. Stop the source, load everything, and start the target in one window. Why the correct answer wins: Scheduling away from the predictable surge keeps the catch-up inside the window.

### Question 79 — C

Answer: Export the table into BigQuery. Copying the history into the warehouse keeps it queryable afterwards. Copy the analytical slice into the warehouse on a schedule. Local study-map skill 3.10 (Source Decommissioning), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 3 (migrate data solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Keep writing back to the original system so a rollback loses nothing. Why the correct answer wins: Copying the history into the warehouse keeps it queryable afterwards.
- **B:** Incorrect for this question. Interconnect the remaining on-premises system rather than moving it. Why the correct answer wins: Copying the history into the warehouse keeps it queryable afterwards.
- **C:** Correct. Copy the analytical slice into the warehouse on a schedule. In this case: Copying the history into the warehouse keeps it queryable afterwards.
- **D:** Incorrect for this question. Keep the old system read-only for a defined period, then remove it. Why the correct answer wins: Copying the history into the warehouse keeps it queryable afterwards.

### Question 80 — A

Answer: Confirm no client still uses the old endpoint. Connection and traffic evidence shows whether any client still uses the endpoint. Check the connection and traffic evidence before retiring an instance. Local study-map skill 3.10 (Source Decommissioning), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 3 (migrate data solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Correct. Check the connection and traffic evidence before retiring an instance. In this case: Connection and traffic evidence shows whether any client still uses the endpoint.
- **B:** Incorrect for this question. Keep the old system read-only for a defined period, then remove it. Why the correct answer wins: Connection and traffic evidence shows whether any client still uses the endpoint.
- **C:** Incorrect for this question. Prove the target holds the same rows as the source before cutover. Why the correct answer wins: Connection and traffic evidence shows whether any client still uses the endpoint.
- **D:** Incorrect for this question. Move clients to the new endpoint as the final cutover action. Why the correct answer wins: Connection and traffic evidence shows whether any client still uses the endpoint.

### Question 81 — D

Answer: Provision the instance with a Terraform module. A declared module reproduces the estate from one definition. Declare the database so the same definition creates every environment. Local study-map skill 4.1 (Provisioning Highly Available Instances), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 4 (deploy scalable and highly available databases in Google Cloud): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Create the resource interactively with no stored definition. Why the correct answer wins: A declared module reproduces the estate from one definition.
- **B:** Incorrect for this question. A copy of the current data created without touching the source. Why the correct answer wins: A declared module reproduces the estate from one definition.
- **C:** Incorrect for this question. Run the new version beside the old one and move traffic when it is proven. Why the correct answer wins: A declared module reproduces the estate from one definition.
- **D:** Correct. Declare the database so the same definition creates every environment. In this case: A declared module reproduces the estate from one definition.

### Question 82 — C

Answer: Apply the change through the infrastructure pipeline. Applying changes through the pipeline records who approved what and when, which manual edits never do. Send database changes through review and version control like any other code. Local study-map skill 4.1 (Provisioning Highly Available Instances), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 4 (deploy scalable and highly available databases in Google Cloud): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A single view of health, security, and version posture across database instances. Why the correct answer wins: Applying changes through the pipeline records who approved what and when, which manual edits never do.
- **B:** Incorrect for this question. Rehearse the change against a copy before touching production. Why the correct answer wins: Applying changes through the pipeline records who approved what and when, which manual edits never do.
- **C:** Correct. Send database changes through review and version control like any other code. In this case: Applying changes through the pipeline records who approved what and when, which manual edits never do.
- **D:** Incorrect for this question. Create the resource interactively with no stored definition. Why the correct answer wins: Applying changes through the pipeline records who approved what and when, which manual edits never do.

### Question 83 — B

Answer: Provision the instance with a Terraform module. A module applies one definition across every instance. Declare the database so the same definition creates every environment. Local study-map skill 4.1 (Provisioning Highly Available Instances), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 4 (deploy scalable and highly available databases in Google Cloud): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Create the resource interactively with no stored definition. Why the correct answer wins: A module applies one definition across every instance.
- **B:** Correct. Declare the database so the same definition creates every environment. In this case: A module applies one definition across every instance.
- **C:** Incorrect for this question. Run the new version beside the old one and move traffic when it is proven. Why the correct answer wins: A module applies one definition across every instance.
- **D:** Incorrect for this question. A recovery point that makes the upgrade reversible in practice. Why the correct answer wins: A module applies one definition across every instance.

### Question 84 — A

Answer: Run a controlled failover test. A controlled failover observes the takeover. Trigger a switchover in a test window and observe how long writes are unavailable. Local study-map skill 4.2 (Testing High Availability and Disaster Recovery), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 4 (deploy scalable and highly available databases in Google Cloud): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Correct. Trigger a switchover in a test window and observe how long writes are unavailable. In this case: A controlled failover observes the takeover.
- **B:** Incorrect for this question. A recovery point that makes the upgrade reversible in practice. Why the correct answer wins: A controlled failover observes the takeover.
- **C:** Incorrect for this question. Compare the signal after cutover against the pre-change baseline. Why the correct answer wins: A controlled failover observes the takeover.
- **D:** Incorrect for this question. Rebuild the database in the surviving region from the latest backup. Why the correct answer wins: A controlled failover observes the takeover.

### Question 85 — D

Answer: Rehearse the promotion in a test project. Promoting the remote copy and timing the write path measures the regional recovery the promise depends on. Practise the failover that the runbook would perform for real. Local study-map skill 4.2 (Testing High Availability and Disaster Recovery), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 4 (deploy scalable and highly available databases in Google Cloud): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Give the standby enough capacity to carry production alone. Why the correct answer wins: Promoting the remote copy and timing the write path measures the regional recovery the promise depends on.
- **B:** Incorrect for this question. Trigger a switchover in a test window and observe how long writes are unavailable. Why the correct answer wins: Promoting the remote copy and timing the write path measures the regional recovery the promise depends on.
- **C:** Incorrect for this question. A recovery point that makes the upgrade reversible in practice. Why the correct answer wins: Promoting the remote copy and timing the write path measures the regional recovery the promise depends on.
- **D:** Correct. Practise the failover that the runbook would perform for real. In this case: Promoting the remote copy and timing the write path measures the regional recovery the promise depends on.

### Question 86 — D

Answer: Restore the backup into the second region. Restoring in the second region tests the rebuild path. Rebuild the database in the surviving region from the latest backup. Local study-map skill 4.2 (Testing High Availability and Disaster Recovery), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 4 (deploy scalable and highly available databases in Google Cloud): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Trigger a switchover in a test window and observe how long writes are unavailable. Why the correct answer wins: Restoring in the second region tests the rebuild path.
- **B:** Incorrect for this question. A recovery point that makes the upgrade reversible in practice. Why the correct answer wins: Restoring in the second region tests the rebuild path.
- **C:** Incorrect for this question. Practise the failover that the runbook would perform for real. Why the correct answer wins: Restoring in the second region tests the rebuild path.
- **D:** Correct. Rebuild the database in the surviving region from the latest backup. In this case: Restoring in the second region tests the rebuild path.

### Question 87 — C, D

Answers: Choose a multi-region instance configuration; Add a secondary cluster in the second region. A multi-region Spanner configuration keeps quorum across regions, and an AlloyDB secondary cluster provides a promotable copy. A topology that places replicas in separate regions for regional-failure tolerance. An AlloyDB cross-region copy that can be promoted to a primary cluster. Local study-map skill 4.3 (Multi-Regional Replication Setup), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 4 (deploy scalable and highly available databases in Google Cloud): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A copy in a second region that serves reads and can be promoted. Why the correct answer wins: A multi-region Spanner configuration keeps quorum across regions, and an AlloyDB secondary cluster provides a promotable copy.
- **B:** Incorrect for this question. Rebuild the database in the surviving region from the latest backup. Why the correct answer wins: A multi-region Spanner configuration keeps quorum across regions, and an AlloyDB secondary cluster provides a promotable copy.
- **C:** Correct. A topology that places replicas in separate regions for regional-failure tolerance. In this case: A multi-region Spanner configuration keeps quorum across regions, and an AlloyDB secondary cluster provides a promotable copy.
- **D:** Correct. An AlloyDB cross-region copy that can be promoted to a primary cluster. In this case: A multi-region Spanner configuration keeps quorum across regions, and an AlloyDB secondary cluster provides a promotable copy.
- **E:** Incorrect for this question. A primary and standby in two zones of one region with automatic failover. Why the correct answer wins: A multi-region Spanner configuration keeps quorum across regions, and an AlloyDB secondary cluster provides a promotable copy.

### Question 88 — B

Answer: Route the app profile across both clusters. Multi-cluster routing moves the client to the surviving cluster automatically, while pinning it to one cluster leaves the outage visible to users. A Bigtable app profile that fails over between clusters without a client change. Local study-map skill 4.3 (Multi-Regional Replication Setup), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 4 (deploy scalable and highly available databases in Google Cloud): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A copy in a second region that serves reads and can be promoted. Why the correct answer wins: Multi-cluster routing moves the client to the surviving cluster automatically, while pinning it to one cluster leaves the outage visible to users.
- **B:** Correct. A Bigtable app profile that fails over between clusters without a client change. In this case: Multi-cluster routing moves the client to the surviving cluster automatically, while pinning it to one cluster leaves the outage visible to users.
- **C:** Incorrect for this question. A Bigtable app profile that keeps a workload on one cluster for predictable latency. Why the correct answer wins: Multi-cluster routing moves the client to the surviving cluster automatically, while pinning it to one cluster leaves the outage visible to users.
- **D:** Incorrect for this question. An AlloyDB cross-region copy that can be promoted to a primary cluster. Why the correct answer wins: Multi-cluster routing moves the client to the surviving cluster automatically, while pinning it to one cluster leaves the outage visible to users.

### Question 89 — A

Answer: Add a cross-region read replica. A cross-region replica ships every change to the second region and can take over if the primary is lost. A copy in a second region that serves reads and can be promoted. Local study-map skill 4.3 (Multi-Regional Replication Setup), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 4 (deploy scalable and highly available databases in Google Cloud): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Correct. A copy in a second region that serves reads and can be promoted. In this case: A cross-region replica ships every change to the second region and can take over if the primary is lost.
- **B:** Incorrect for this question. A topology that places replicas in separate regions for regional-failure tolerance. Why the correct answer wins: A cross-region replica ships every change to the second region and can take over if the primary is lost.
- **C:** Incorrect for this question. Rebuild the database in the surviving region from the latest backup. Why the correct answer wins: A cross-region replica ships every change to the second region and can take over if the primary is lost.
- **D:** Incorrect for this question. An AlloyDB cross-region copy that can be promoted to a primary cluster. Why the correct answer wins: A cross-region replica ships every change to the second region and can take over if the primary is lost.

### Question 90 — B

Answer: Add nodes to the read pool. Adding read-pool nodes adds capacity where the load is concentrated. Grow the AlloyDB read pool that serves read-only connections. Local study-map skill 4.4 (Read Replicas and Read Pools), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 4 (deploy scalable and highly available databases in Google Cloud): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Absorb repeated reads in memory so the database sees fewer of them. Why the correct answer wins: Adding read-pool nodes adds capacity where the load is concentrated.
- **B:** Correct. Grow the AlloyDB read pool that serves read-only connections. In this case: Adding read-pool nodes adds capacity where the load is concentrated.
- **C:** Incorrect for this question. Separate analytical reads from the write path. Why the correct answer wins: Adding read-pool nodes adds capacity where the load is concentrated.
- **D:** Incorrect for this question. Move the instance to a larger shape so more vCPU and memory serve the same data. Why the correct answer wins: Adding read-pool nodes adds capacity where the load is concentrated.

### Question 91 — A

Answer: Send reporting queries to the read replica. Routing reads to the idle replica uses capacity already paid for. Separate analytical reads from the write path. Local study-map skill 4.4 (Read Replicas and Read Pools), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 4 (deploy scalable and highly available databases in Google Cloud): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Correct. Separate analytical reads from the write path. In this case: Routing reads to the idle replica uses capacity already paid for.
- **B:** Incorrect for this question. Absorb repeated reads in memory so the database sees fewer of them. Why the correct answer wins: Routing reads to the idle replica uses capacity already paid for.
- **C:** Incorrect for this question. Send reads to a copy so the primary keeps its capacity for writes. Why the correct answer wins: Routing reads to the idle replica uses capacity already paid for.
- **D:** Incorrect for this question. Move the instance to a larger shape so more vCPU and memory serve the same data. Why the correct answer wins: Routing reads to the idle replica uses capacity already paid for.

### Question 92 — C

Answer: Provision the instance with a Terraform module. A parameterised module creates each instance from one definition. Declare the database so the same definition creates every environment. Local study-map skill 4.5 (Automating Database Provisioning), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 4 (deploy scalable and highly available databases in Google Cloud): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A single view of health, security, and version posture across database instances. Why the correct answer wins: A parameterised module creates each instance from one definition.
- **B:** Incorrect for this question. Create the resource interactively with no stored definition. Why the correct answer wins: A parameterised module creates each instance from one definition.
- **C:** Correct. Declare the database so the same definition creates every environment. In this case: A parameterised module creates each instance from one definition.
- **D:** Incorrect for this question. Rehearse the change against a copy before touching production. Why the correct answer wins: A parameterised module creates each instance from one definition.

### Question 93 — C

Answer: Apply the change through the infrastructure pipeline. Validation in the pipeline refuses the change before creation. Send database changes through review and version control like any other code. Local study-map skill 4.5 (Automating Database Provisioning), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 4 (deploy scalable and highly available databases in Google Cloud): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A copy of the current data created without touching the source. Why the correct answer wins: Validation in the pipeline refuses the change before creation.
- **B:** Incorrect for this question. A recovery point that makes the upgrade reversible in practice. Why the correct answer wins: Validation in the pipeline refuses the change before creation.
- **C:** Correct. Send database changes through review and version control like any other code. In this case: Validation in the pipeline refuses the change before creation.
- **D:** Incorrect for this question. Create the resource interactively with no stored definition. Why the correct answer wins: Validation in the pipeline refuses the change before creation.

### Question 94 — D

Answer: Create an alerting policy on the metric. An alerting policy on the failover signal notifies the team. A condition that pages a human when the threshold is crossed. Local study-map skill 4.6 (Monitoring Highly Available Databases), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 4 (deploy scalable and highly available databases in Google Cloud): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A per-query view of latency, load, and wait events on the instance. Why the correct answer wins: An alerting policy on the failover signal notifies the team.
- **B:** Incorrect for this question. Read the instance-level signals before attributing the symptom to the query. Why the correct answer wins: An alerting policy on the failover signal notifies the team.
- **C:** Incorrect for this question. A single view of health, security, and version posture across database instances. Why the correct answer wins: An alerting policy on the failover signal notifies the team.
- **D:** Correct. A condition that pages a human when the threshold is crossed. In this case: An alerting policy on the failover signal notifies the team.

### Question 95 — D

Answer: Alert when the instance is unreachable. A probe that runs a query detects failures the resource view misses. A liveness signal that fires before users report the outage. Local study-map skill 4.6 (Monitoring Highly Available Databases), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 4 (deploy scalable and highly available databases in Google Cloud): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Read the instance-level signals before attributing the symptom to the query. Why the correct answer wins: A probe that runs a query detects failures the resource view misses.
- **B:** Incorrect for this question. A per-query view of latency, load, and wait events on the instance. Why the correct answer wins: A probe that runs a query detects failures the resource view misses.
- **C:** Incorrect for this question. The engine log of statements that exceeded the long-query threshold. Why the correct answer wins: A probe that runs a query detects failures the resource view misses.
- **D:** Correct. A liveness signal that fires before users report the outage. In this case: A probe that runs a query detects failures the resource view misses.

### Question 96 — B, E

Answers: Promote the cross-region replica during the outage; Fence the old primary before promotion. Promoting the current copy restores writes quickly, and fencing the returning instance prevents two primaries. Turn the replica into an independent primary so the application can resume writes. Stop the former primary from accepting writes so two instances cannot both claim the role. Local study-map skill 4.7 (Regional Failover Mechanics), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 4 (deploy scalable and highly available databases in Google Cloud): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Rebuild the database in the surviving region from the latest backup. Why the correct answer wins: Promoting the current copy restores writes quickly, and fencing the returning instance prevents two primaries.
- **B:** Correct. Stop the former primary from accepting writes so two instances cannot both claim the role. In this case: Promoting the current copy restores writes quickly, and fencing the returning instance prevents two primaries.
- **C:** Incorrect for this question. Trigger a switchover in a test window and observe how long writes are unavailable. Why the correct answer wins: Promoting the current copy restores writes quickly, and fencing the returning instance prevents two primaries.
- **D:** Incorrect for this question. A point-in-time restore that discards the later writes on the same instance. Why the correct answer wins: Promoting the current copy restores writes quickly, and fencing the returning instance prevents two primaries.
- **E:** Correct. Turn the replica into an independent primary so the application can resume writes. In this case: Promoting the current copy restores writes quickly, and fencing the returning instance prevents two primaries.

### Question 97 — B

Answer: Run a controlled failover test. A controlled failover exercises the reconnect path. Trigger a switchover in a test window and observe how long writes are unavailable. Local study-map skill 4.7 (Regional Failover Mechanics), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 4 (deploy scalable and highly available databases in Google Cloud): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A recovery point that makes the upgrade reversible in practice. Why the correct answer wins: A controlled failover exercises the reconnect path.
- **B:** Correct. Trigger a switchover in a test window and observe how long writes are unavailable. In this case: A controlled failover exercises the reconnect path.
- **C:** Incorrect for this question. Rebuild the database in the surviving region from the latest backup. Why the correct answer wins: A controlled failover exercises the reconnect path.
- **D:** Incorrect for this question. Compare the signal after cutover against the pre-change baseline. Why the correct answer wins: A controlled failover exercises the reconnect path.

### Question 98 — C

Answer: Use the language connector with IAM credentials. The language connector resolves the instance on each connection. A client library that resolves the instance and authorizes the connection with IAM. Local study-map skill 4.8 (Connection Routing and Load Balancing), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 4 (deploy scalable and highly available databases in Google Cloud): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Move clients to the new endpoint as the final cutover action. Why the correct answer wins: The language connector resolves the instance on each connection.
- **B:** Incorrect for this question. A pooler that multiplexes many application connections onto few database sessions. Why the correct answer wins: The language connector resolves the instance on each connection.
- **C:** Correct. A client library that resolves the instance and authorizes the connection with IAM. In this case: The language connector resolves the instance on each connection.
- **D:** Incorrect for this question. A public-IP allowlist that admits the caller range. Why the correct answer wins: The language connector resolves the instance on each connection.

### Question 99 — B

Answer: Reserve headroom above the measured peak. Spare capacity above the combined peak is what lets the standby hold the latency target once it takes over. Keep spare capacity so a failover or a traffic spike does not saturate the instance. Local study-map skill 4.9 (Failover Capacity Headroom), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 4 (deploy scalable and highly available databases in Google Cloud): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Send reads to a copy so the primary keeps its capacity for writes. Why the correct answer wins: Spare capacity above the combined peak is what lets the standby hold the latency target once it takes over.
- **B:** Correct. Keep spare capacity so a failover or a traffic spike does not saturate the instance. In this case: Spare capacity above the combined peak is what lets the standby hold the latency target once it takes over.
- **C:** Incorrect for this question. Match capacity to the daily traffic shape. Why the correct answer wins: Spare capacity above the combined peak is what lets the standby hold the latency target once it takes over.
- **D:** Incorrect for this question. Shrink an instance whose peak fits a smaller shape. Why the correct answer wins: Spare capacity above the combined peak is what lets the standby hold the latency target once it takes over.

### Question 100 — D

Answer: Pre-size the promoted replica for the full load. The standby has to be provisioned for production load beforehand, because resizing does not fit inside the window. Give the standby enough capacity to carry production alone. Local study-map skill 4.9 (Failover Capacity Headroom), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 4 (deploy scalable and highly available databases in Google Cloud): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Keep spare capacity so a failover or a traffic spike does not saturate the instance. Why the correct answer wins: The standby has to be provisioned for production load beforehand, because resizing does not fit inside the window.
- **B:** Incorrect for this question. Match capacity to the daily traffic shape. Why the correct answer wins: The standby has to be provisioned for production load beforehand, because resizing does not fit inside the window.
- **C:** Incorrect for this question. Send reads to a copy so the primary keeps its capacity for writes. Why the correct answer wins: The standby has to be provisioned for production load beforehand, because resizing does not fit inside the window.
- **D:** Correct. Give the standby enough capacity to carry production alone. In this case: The standby has to be provisioned for production load beforehand, because resizing does not fit inside the window.
