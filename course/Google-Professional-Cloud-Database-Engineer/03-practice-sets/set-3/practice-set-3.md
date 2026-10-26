# Google Cloud Professional Cloud Database Engineer — Full-Length Mock Exam 3

Professional Cloud Database Engineer · 100 questions · expanded practice bank · passing score not published

Blueprint-weighted mock exam. Item mix: 84 multiple-choice and 16 multiple-select items (the selection count is stated in each multi-select stem). The live exam publishes 50-60 multiple-choice and multiple-select questions and has no case-study component, so this set is larger on purpose and no case-study item is reproduced. The live paper allows two hours for 50-60 items, so this 100-item set is a slower-per-item rehearsal: about 72 seconds per item here against roughly 120-144 seconds live. Use it to build a habit of finishing with time to review. See the README for the exact fidelity boundary.

Original educational content, not actual, recalled, or copied Google exam items.

## Questions

---

## Domain 1 — Design Innovative, Scalable, and Highly Available Cloud Database Solutions (Sizing, Availability Design, and Database Selection)

### 1. A hospital's imaging database must absorb a merger that doubles patient volume within six months, and today's metrics are known. How should the instance be sized now?

- A. Reserve headroom above the measured peak
- B. Commit to the steady baseline capacity
- C. Reduce the machine type to match observed use
- D. Size the instance from the observed peak metrics

### 2. A team inherits an instance sized by guesswork three years ago and wants an objective basis for the resize decision next quarter. What should it use?

- A. Size the instance from the observed peak metrics
- B. Commit to the steady baseline capacity
- C. Reserve headroom above the measured peak
- D. Load-test the workload to derive the size

### 3. A Cloud SQL for MySQL instance hits its disk throughput ceiling during bulk loads while compute stays at thirty-five percent. Which change removes the ceiling?

- A. Move the data to SSD storage
- B. Increase the disk size to raise throughput
- C. Add a read replica for the read traffic
- D. Increase the machine type of the instance

### 4. A Bigtable cluster behind a live feed runs on HDD and misses its p99 target while CPU sits at forty percent. What should the team change?

- A. Move the data to HDD storage
- B. Set the garbage-collection policy on the column family
- C. Add nodes to the Bigtable cluster
- D. Move the data to SSD storage

### 5. A Cloud SQL for PostgreSQL instance has four vCPUs and fifteen gigabytes of memory for a forty-gigabyte working set, and the cache hit ratio is sixty percent. What should the team do?

- A. Increase the disk size to raise throughput
- B. Put a session pooler in front of the instance
- C. Add a read replica for the read traffic
- D. Increase the machine type of the instance

### 6. A Spanner workload follows a predictable weekday pattern and the team wants compute to follow it with no manual resize. What should they enable?

- A. Add nodes to the Bigtable cluster
- B. Enable autoscaling on the instance
- C. Add processing units to the Spanner instance
- D. Increase the machine type of the instance

### 7. A team wants automatic zone failover and, for a regional loss, a recovery path that needs no continuously running second copy. Select two.

- A. Add a cross-region read replica
- B. Restore the backup into the second region
- C. Set a deny maintenance period over the peak event
- D. Enable regional high availability with a standby zone
- E. Choose a multi-region instance configuration

### 8. A service needs a copy of its Cloud SQL data in another region for a thirty-minute recovery objective but cannot run a second writable primary. What should the team add?

- A. Add a cross-region read replica
- B. Choose a multi-region instance configuration
- C. Restore the backup into the second region
- D. Run a single zonal instance

### 9. A globally used session store on Spanner must keep accepting writes when any single region is lost. Which choice provides that?

- A. Add a cross-region read replica
- B. Restore the backup into the second region
- C. Enable regional high availability with a standby zone
- D. Choose a multi-region instance configuration

### 10. A database serves three time zones, and the team must pick a weekly patch slot while keeping one peak week completely clear. Select two.

- A. Schedule the maintenance window in the low-traffic period
- B. Set a deny maintenance period over the peak event
- C. Run a controlled failover test
- D. Perform an in-place major version upgrade
- E. Take a backup before the upgrade

### 11. A two-day regulatory audit must not be interrupted by any database maintenance, and patching can resume afterwards. What should the team set?

- A. Take a backup before the upgrade
- B. Restart the instance in the window
- C. Set a deny maintenance period over the peak event
- D. Schedule the maintenance window in the low-traffic period

### 12. An application inside the same VPC must reach Cloud SQL without traversing the internet and without running an extra proxy process. Which option fits?

- A. Connect over private IP inside the VPC
- B. Use the public IP with enforced SSL
- C. Add the client range to authorized networks
- D. Publish the instance behind Private Service Connect

### 13. A team must reach a Cloud SQL instance from a network that has no peering with the instance's VPC, using a private address only. Which option fits?

- A. Place the instance in a Shared VPC service project
- B. Publish the instance behind Private Service Connect
- C. Add the client range to authorized networks
- D. Connect over private IP inside the VPC

### 14. An audit requires that the data at rest in Cloud SQL be protected by a key the company controls and can revoke. Which control fits?

- A. Route the audit logs to a locked log bucket
- B. Rely on Google-managed encryption keys
- C. Encrypt with a customer-managed key in Cloud KMS
- D. Rotate the customer-managed key on a schedule

### 15. A control requires an annual key-version rotation while backups written under earlier versions stay restorable. What should the team configure?

- A. Rotate the customer-managed key on a schedule
- B. Encrypt with a customer-managed key in Cloud KMS
- C. Rely on Google-managed encryption keys
- D. Add the projects to a VPC Service Controls perimeter

### 16. A serverless workload opens three thousand short-lived sessions a minute and exhausts the instance's connection budget at peak. What should the team add?

- A. Add a read replica for the read traffic
- B. Increase the machine tier to allow more connections
- C. Raise the max_connections database flag
- D. Put a session pooler in front of the instance

### 17. An ORM configuration opens two sessions per request and releases neither when a request fails. What should be fixed?

- A. Increase the machine type of the instance
- B. Raise the max_connections database flag
- C. Put a session pooler in front of the instance
- D. Fix the connection leak in the application

### 18. An audit must attribute every write to a table to a principal and keep the evidence for a year. Select two.

- A. Rely on Admin Activity audit logs
- B. Build a log-based metric from the error entries
- C. Route the audit logs to a locked log bucket
- D. Review the fleet in Database Center
- E. Enable Data Access audit logs

### 19. An investigator must find who changed the backup retention setting on an instance last week. Which log answers that?

- A. Use Query Insights to find the heavy statements
- B. Review the fleet in Database Center
- C. Enable Data Access audit logs
- D. Rely on Admin Activity audit logs

### 20. A team wants a managed relational database for a one-hundred-gigabyte application with the least operational work and predictable single-region latency. Which choice fits?

- A. Use Spanner for the globally distributed relational workload
- B. Run the database on Compute Engine yourself
- C. Use AlloyDB for the demanding relational workload
- D. Use Cloud SQL for the relational workload

### 21. An engine licence requires direct hardware access with no hypervisor, and the workload cannot move to another engine. Which deployment fits?

- A. Use Cloud SQL for the relational workload
- B. Use a partner-managed database offering
- C. Run the database on bare metal solution
- D. Run the database on Compute Engine yourself

### 22. A catalogue needs flexible attributes and very high key-based read throughput, while analysts also need warehouse scans of the same data. Select two.

- A. Use Firestore for the document workload
- B. Use Bigtable for the high-throughput wide-column workload
- C. Export the table into BigQuery
- D. Use Memorystore as the caching tier
- E. Use Cloud SQL for the relational workload

### 23. A field-service application needs offline edits that synchronise when connectivity returns, with per-document queries. Which database fits?

- A. Use Firestore for the document workload
- B. Use Memorystore as the caching tier
- C. Use Bigtable for the high-throughput wide-column workload
- D. Use Cloud SQL for the relational workload

### 24. A regional SaaS needs relational semantics over two terabytes with the lowest operational overhead and no cross-region requirement. Which database fits?

- A. Use Cloud SQL for the relational workload
- B. Use Bigtable for the high-throughput wide-column workload
- C. Use Memorystore as the caching tier
- D. Use Spanner for the globally distributed relational workload

### 25. A search team needs filtered vector search over one hundred million embeddings with a low p99. Which approach fits?

- A. Export the table into BigQuery
- B. Query the source through BigQuery federated queries
- C. Enable the vector extension on PostgreSQL
- D. Use AlloyDB vector search with a ScaNN index

### 26. A team wants to prototype semantic search this sprint on an existing Cloud SQL for PostgreSQL instance holding half a million embeddings. Which approach fits?

- A. Use AlloyDB vector search with a ScaNN index
- B. Enable the vector extension on PostgreSQL
- C. Cache the hot read path in Memorystore
- D. Create a vector index for the embeddings

### 27. Development and production share one large instance whose baseline never varies, and the company pays month to month. Which two cost actions should it take? Select two.

- A. Split development workloads onto their own instance
- B. Commit to the steady baseline capacity
- C. Stop or delete the idle instance
- D. Rely on sustained-use discounts
- E. Let the disk grow automatically

### 28. A Bigtable archive holds eighty terabytes read rarely in large scans, and latency is not a requirement. Which change lowers cost?

- A. Move the data to HDD storage
- B. Set the garbage-collection policy on the column family
- C. Add nodes to the Bigtable cluster
- D. Move the data to SSD storage

### 29. Two hundred queries depend on database-specific behaviour, and the business needs the new platform live in six weeks. What should the team decide?

- A. Keep the current engine and version
- B. Choose the target engine with the cheapest conversion
- C. Write to both systems from the application
- D. Use Database Migration Service with schema conversion

### 30. A team must keep database data inside the European Union and stop it being copied into a non-approved project. Which two controls are needed? Select two.

- A. Choose a multi-region instance configuration
- B. Cache the hot read path in Memorystore
- C. Rely on Google-managed encryption keys
- D. Add the projects to a VPC Service Controls perimeter
- E. Place the instance in the required region

### 31. A team must prevent any future project in the organization from creating a database outside the approved regions. What should it apply?

- A. Place the instance in the required region
- B. Encrypt with a customer-managed key in Cloud KMS
- C. Enforce the location with an organization policy
- D. Route the audit logs to a locked log bucket

### 32. Analysts need to join a live Spanner table with BigQuery history and are not allowed to copy the Spanner rows. Which approach fits?

- A. Export the table into BigQuery
- B. Keep part of the estate on-premises with a hybrid link
- C. Stream changes into BigQuery
- D. Query the source through BigQuery federated queries

---

## Domain 2 — Manage a Solution That Can Span Multiple Database Technologies (Operations, Access, Backup, and Performance)

### 33. A BI tool must read one schema with no stored password and must not see any other schema on the instance. Select two.

- A. Keep a database password in the connection string
- B. Grant the basic editor role
- C. Share one application database user
- D. Enable IAM database authentication
- E. Limit the user to the required schema

### 34. An operator only needs to view instance metrics, but the binding currently grants the administrator role on the project. What should the team change?

- A. Grant the basic editor role
- B. Grant the predefined database role
- C. Grant a custom role limited to the needed permissions
- D. Create one database user per person

### 35. An application must authenticate to the database as a workload identity that security can revoke without touching the code. Which approach fits?

- A. Share one application database user
- B. Have the application authenticate as a service account
- C. Create one database user per person
- D. Keep a database password in the connection string

### 36. A slow query must be understood before it is changed. Which two steps should the team take? Select two.

- A. Partition the large table
- B. Refresh the table statistics
- C. Cache the hot read path in Memorystore
- D. Add the index the slow query needs
- E. Read the query plan for the statement

### 37. Statistics show four indexes on a write-heavy table have never served a query, and insert latency keeps rising. What should the team do?

- A. Add the index the slow query needs
- B. Drop the unused index
- C. Partition the large table
- D. Raise the per-operation memory flag

### 38. A nightly job updates two million rows inside a single transaction, and reads queue behind it for fifteen minutes. What should change?

- A. Put a session pooler in front of the instance
- B. Batch the writes into fewer round trips
- C. Terminate the session that holds the lock
- D. Inspect lock waits and blocking sessions

### 39. Users report intermittent stalls, and the team must identify which transaction is blocking the others. What should it do?

- A. Batch the writes into fewer round trips
- B. Refresh the table statistics
- C. Add the index the slow query needs
- D. Inspect lock waits and blocking sessions

### 40. A release tripled p99 latency and the team must show what changed. Which two sources should it compare against the pre-release baseline? Select two.

- A. Read the slow query log
- B. Watch CPU, memory, disk, and IOPS together
- C. Use Query Insights to find the heavy statements
- D. Review the fleet in Database Center
- E. Build a log-based metric from the error entries

### 41. Application errors spike in bursts but no metric counts them, and the pattern is visible only in the log. What should the team create?

- A. Read the slow query log
- B. Build a log-based metric from the error entries
- C. Route the audit logs to a locked log bucket
- D. Alert when the instance is unreachable

### 42. During a real incident a restore job is refused because the project has reached its concurrent-operation limit. What should the team do?

- A. Request a quota increase for the project
- B. Move the job outside the contention window
- C. Retry the failed operation with exponential backoff
- D. Export the table to CSV in Cloud Storage

### 43. Reporting reads stale data for several minutes after each bulk load, and nobody is told. What should the team add?

- A. Create an alerting policy on the metric
- B. Alert on the database error rate
- C. Alert on replication lag
- D. Watch CPU, memory, disk, and IOPS together

### 44. A team wants pages on failed statements rather than on CPU spikes that may be harmless. Which alert fits?

- A. Alert on the database error rate
- B. Alert on replication lag
- C. Use Query Insights to find the heavy statements
- D. Create an alerting policy on the metric

### 45. A team must recover from a bad change twenty minutes old and must also be able to restore one table on its own. Which two capabilities does it need? Select two.

- A. Export a logical dump to Cloud Storage
- B. Extend the backup retention window
- C. Clone the instance for the test
- D. Take an on-demand backup before the change
- E. Enable point-in-time recovery

### 46. A team relies on weekly manual dumps and has no scheduled backup at all. What should it enable?

- A. Export the table to CSV in Cloud Storage
- B. Take an on-demand backup before the change
- C. Enable automated backups with a retention window
- D. Clone the instance for the test

### 47. A downstream loader needs a flat file extract of one table every night. Which export format fits?

- A. Export a logical dump to Cloud Storage
- B. Export the table into BigQuery
- C. Export the table to CSV in Cloud Storage
- D. Import the dump into the target instance

### 48. A team keeps thirty-five days of backups but cannot say how much data an outage would lose. What should it define first?

- A. Clone the instance for the test
- B. Enable point-in-time recovery
- C. Design the restore path to the stated RTO and RPO
- D. Enable automated backups with a retention window

### 49. A migration deleted rows twenty minutes ago and the instance must return to that state. Which capability restores it?

- A. Export a logical dump to Cloud Storage
- B. Restore to the timestamp before the bad change
- C. Clone the instance for the test
- D. Run a controlled failover test

### 50. A regulator requires customer records to be deleted ninety days after account closure, and the database must enforce it. What should the team apply?

- A. Apply a row-level retention policy
- B. Set a time-to-live policy on the collection
- C. Set the garbage-collection policy on the column family
- D. Archive closed rows to cheaper storage

### 51. An analytics dashboard queries the production primary directly and drives CPU to ninety percent every morning. What should the team add?

- A. Add a read replica for the read traffic
- B. Add processing units to the Spanner instance
- C. Shard the data across several instances
- D. Increase the machine type of the instance

### 52. A single table holds six years of orders, and every purge has to delete rows one at a time from the middle of the table. What should change?

- A. Add the index the slow query needs
- B. Partition the large table
- C. Add a read replica for the read traffic
- D. Increase the machine type of the instance

### 53. Analysts need Cloud SQL changes to appear in BigQuery within a minute, continuously, without querying the production instance. Which approach fits?

- A. Export the table to CSV in Cloud Storage
- B. Dump, restore, then replay the changes
- C. Query the source through BigQuery federated queries
- D. Stream changes with Datastream

### 54. After a bulk load the planner keeps choosing a nested loop that returns nine hundred thousand rows, although the index exists. What should the team do?

- A. Add the index the slow query needs
- B. Drop the unused index
- C. Raise the per-operation memory flag
- D. Refresh the table statistics

### 55. Weekly index maintenance on a Cloud SQL for SQL Server instance must run whether or not a person is working. What should the team configure?

- A. Provision the instance once by hand
- B. Run a controlled failover test
- C. Take an on-demand backup before the change
- D. Run the task on a managed schedule

### 56. Exports pile up in a bucket month after month, and only the newest seven are ever restored. What should the team add?

- A. Take an on-demand backup before the change
- B. Run the task on a managed schedule
- C. Add a lifecycle rule to the export bucket
- D. Export a logical dump to Cloud Storage

### 57. A team must report monthly whether the database met the 99.9 percent availability it committed to in its service description. What should it track?

- A. Review the fleet in Database Center
- B. Watch CPU, memory, disk, and IOPS together
- C. Track the availability signal against the agreed objective
- D. Create an alerting policy on the metric

---

## Domain 3 — Migrate Data Solutions (Migration Strategy, Conversion, and Cutover)

### 58. A one-terabyte PostgreSQL database must move to Cloud SQL with a fifteen-minute window, and the application cannot be changed. Which strategy fits?

- A. Dump, restore, then replay the changes
- B. Write to both systems from the application
- C. Accept a scheduled extended outage
- D. Use Database Migration Service for the same engine

### 59. A two-hundred-gigabyte database can be offline on a Sunday for twelve hours, and the team wants no replication complexity. Which strategy fits?

- A. Write to both systems from the application
- B. Set up reverse replication to the source
- C. Use Database Migration Service for the same engine
- D. Accept a scheduled extended outage

### 60. A team has never performed a database cutover and must state who decides, what is checked, and when to abandon. What should it produce?

- A. Accept a scheduled extended outage
- B. Freeze writes during the cutover
- C. Follow a cutover runbook with a rollback step
- D. Write to both systems from the application

### 61. A PostgreSQL 11 database on Compute Engine must move to AlloyDB with conversion of engine-specific functions. Which path fits?

- A. Dump, restore, then replay the changes
- B. Use Database Migration Service with schema conversion
- C. Stream changes with Datastream
- D. Use Database Migration Service for the same engine

### 62. A team must publish MySQL changes into BigQuery and Cloud Storage continuously while the source stays in service. Which tool fits?

- A. Write to both systems from the application
- B. Dump, restore, then replay the changes
- C. Stream changes with Datastream
- D. Use Database Migration Service with schema conversion

### 63. A forty-gigabyte MySQL database can be rebuilt during a weekend window, and the team wants the fewest moving parts. Which approach fits?

- A. Use Database Migration Service with schema conversion
- B. Write to both systems from the application
- C. Dump, restore, then replay the changes
- D. Apply the captured change backlog before cutover

### 64. A heterogeneous conversion reports unsupported procedural code and identity columns that restart at one. Which two fixes are required? Select two.

- A. Reset the sequences after the bulk load
- B. Build the schema in a conversion workspace
- C. Reconcile row counts and checksums
- D. Repoint the connection string at the target
- E. Rewrite the stored procedures and DML by hand

### 65. A team wants to review and edit each converted statement before it reaches the target database. Where should that work happen?

- A. Rewrite the stored procedures and DML by hand
- B. Build the schema in a conversion workspace
- C. Replay read traffic against the target
- D. Reset the sequences after the bulk load

### 66. A Node service uses an insert-or-update statement that PostgreSQL does not accept, and the statement is on the hot path. What must the team do?

- A. Rewrite the stored procedures and DML by hand
- B. Write to both systems from the application
- C. Reset the sequences after the bulk load
- D. Replay read traffic against the target

### 67. A team wants production queries replayed against the target to catch behaviour differences before any user arrives. Which activity fits?

- A. Reconcile row counts and checksums
- B. Rewrite the stored procedures and DML by hand
- C. Replay read traffic against the target
- D. Repoint the connection string at the target

### 68. A two-terabyte load runs while writes continue, and the target must end up current and proven. Select two.

- A. Write to both systems from the application
- B. Dump, restore, then replay the changes
- C. Apply the captured change backlog before cutover
- D. Reconcile row counts and checksums
- E. Use the engine native logical replication

### 69. A team must keep a target current during a sixteen-hour initial load without changing the source application. What should it use?

- A. Accept a scheduled extended outage
- B. Write to both systems from the application
- C. Use the engine native logical replication
- D. Export a logical dump to Cloud Storage

### 70. After a full load the target's daily totals differ by 0.2 percent although every table's row count matches. What should the team run?

- A. Replay read traffic against the target
- B. Reconcile row counts and checksums
- C. Reset the sequences after the bulk load
- D. Repoint the connection string at the target

### 71. A team must confirm that the target returns the same answers for the application's one hundred most frequent queries. Which check fits?

- A. Reconcile row counts and checksums
- B. Follow a cutover runbook with a rollback step
- C. Write to both systems from the application
- D. Replay read traffic against the target

### 72. A cutover must follow a known sequence and must stop new writes at the right moment. Select two.

- A. Freeze writes during the cutover
- B. Measure the catch-up rate before choosing the window
- C. Decommission the source after a parallel period
- D. Follow a cutover runbook with a rollback step
- E. Repoint the connection string at the target

### 73. Everything is validated and writes are frozen, but the application still points at the old host. What completes the switch?

- A. Freeze writes during the cutover
- B. Set up reverse replication to the source
- C. Follow a cutover runbook with a rollback step
- D. Repoint the connection string at the target

### 74. After writes were frozen the target fails its smoke test with twenty minutes left in the window. What should decide the next action?

- A. Freeze writes during the cutover
- B. Write to both systems from the application
- C. Repoint the connection string at the target
- D. Follow a cutover runbook with a rollback step

### 75. Analysts on the old system must see the writes made on the new database after cutover. What must be configured?

- A. Decommission the source after a parallel period
- B. Repoint the connection string at the target
- C. Set up reverse replication to the source
- D. Write to both systems from the application

### 76. A team needs a stated point at which the fallback stops being available and the old system is removed. What should it define?

- A. Decommission the source after a parallel period
- B. Confirm no client still uses the old endpoint
- C. Set up reverse replication to the source
- D. Repoint the connection string at the target

### 77. An Oracle to Cloud SQL for PostgreSQL migration must hold downtime to minutes without changing the application's write path. Which approach fits?

- A. Dump, restore, then replay the changes
- B. Use Database Migration Service with schema conversion
- C. Write to both systems from the application
- D. Accept a scheduled extended outage

### 78. The source's change rate quadruples during month-end close, and the cutover must land inside a thirty-minute window. What should the team do?

- A. Move the job outside the contention window
- B. Accept a scheduled extended outage
- C. Write to both systems from the application
- D. Measure the catch-up rate before choosing the window

### 79. A migrated source is ready to retire. Which two closing actions should the team take? Select two.

- A. Set up reverse replication to the source
- B. Decommission the source after a parallel period
- C. Write to both systems from the application
- D. Repoint the connection string at the target
- E. Confirm no client still uses the old endpoint

### 80. Nine years of source history must remain queryable after the engine is retired. What should the team do first?

- A. Keep part of the estate on-premises with a hybrid link
- B. Decommission the source after a parallel period
- C. Export the table into BigQuery
- D. Set up reverse replication to the source

---

## Domain 4 — Deploy Scalable and Highly Available Databases in Google Cloud (Deployment, High Availability, and Disaster Recovery)

### 81. A new database environment must be created from a definition and validated before anyone uses it. Select two.

- A. Take a backup before the upgrade
- B. Stand up a parallel instance and switch over
- C. Provision the instance with a Terraform module
- D. Test the upgrade on a clone first
- E. Provision the instance once by hand

### 82. A team must show an auditor that every database configuration change was reviewed before it took effect. What should it adopt?

- A. Review the fleet in Database Center
- B. Provision the instance once by hand
- C. Apply the change through the infrastructure pipeline
- D. Test the upgrade on a clone first

### 83. An estate of forty instances must be rebuilt after a regional loss with identical flags and labels. What makes that reliable?

- A. Provision the instance with a Terraform module
- B. Take a backup before the upgrade
- C. Stand up a parallel instance and switch over
- D. Provision the instance once by hand

### 84. A team must confirm that the standby takes over when the active zone disappears, without waiting for a real outage. What should it run?

- A. Alert when the instance is unreachable
- B. Watch the error rate after the change
- C. Run a controlled failover test
- D. Take a backup before the upgrade

### 85. A recovery objective covers a whole region, and the team must prove the promotion path meets it. Which exercise fits?

- A. Take a backup before the upgrade
- B. Run a controlled failover test
- C. Pre-size the promoted replica for the full load
- D. Rehearse the promotion in a test project

### 86. A team wants to prove it can rebuild from backup in a second region, not just fail over to a replica. What should it rehearse?

- A. Restore the backup into the second region
- B. Rehearse the promotion in a test project
- C. Take a backup before the upgrade
- D. Run a controlled failover test

### 87. A Spanner deployment must keep writing through the loss of any single region. Which configuration delivers that?

- A. Add a cross-region read replica
- B. Choose a multi-region instance configuration
- C. Enable regional high availability with a standby zone
- D. Restore the backup into the second region

### 88. An AlloyDB deployment needs a second region that serves reads immediately and can become primary later. Which choice fits?

- A. Restore the backup into the second region
- B. Add nodes to the read pool
- C. Add a secondary cluster in the second region
- D. Run a single zonal instance

### 89. A Bigtable client must keep working when one regional cluster becomes unavailable, with no client-side change. What should the app profile do?

- A. Add a cross-region read replica
- B. Route the app profile across both clusters
- C. Add a secondary cluster in the second region
- D. Pin the app profile to one cluster

### 90. A read-heavy Cloud SQL workload must scale reads without changing the schema or the shape. Select two.

- A. Send reporting queries to the read replica
- B. Increase the machine type of the instance
- C. Partition the large table
- D. Add a read replica for the read traffic
- E. Put a session pooler in front of the instance

### 91. A reporting dashboard opens long-lived sessions on the AlloyDB primary while the read pool sits idle. What should the team change?

- A. Send reporting queries to the read replica
- B. Increase the machine type of the instance
- C. Cache the hot read path in Memorystore
- D. Add nodes to the read pool

### 92. A platform team wants an unlabelled database to be rejected before creation rather than found in an audit later. What should it use?

- A. Clone the instance for the test
- B. Apply the change through the infrastructure pipeline
- C. Take a backup before the upgrade
- D. Provision the instance once by hand

### 93. A team must create fifty identical AlloyDB clusters for tenants with consistent settings. What should it use?

- A. Review the fleet in Database Center
- B. Provision the instance with a Terraform module
- C. Test the upgrade on a clone first
- D. Provision the instance once by hand

### 94. A team must learn within a minute that a failover occurred and which instance is now primary. What should it configure?

- A. Use Query Insights to find the heavy statements
- B. Watch CPU, memory, disk, and IOPS together
- C. Review the fleet in Database Center
- D. Create an alerting policy on the metric

### 95. A database is reported healthy while the application sees connection timeouts. What should the team add?

- A. Alert when the instance is unreachable
- B. Read the slow query log
- C. Watch CPU, memory, disk, and IOPS together
- D. Use Query Insights to find the heavy statements

### 96. A region goes dark without warning, the remote copy is only seconds behind, and leadership asks how writes resume within the hour. What should the team do?

- A. Promote the cross-region replica during the outage
- B. Restore the backup into the second region
- C. Restore to the timestamp before the bad change
- D. Run a controlled failover test

### 97. The old region recovers and its former primary starts accepting writes while the promoted instance is live. What must happen?

- A. Freeze writes during the cutover
- B. Set up reverse replication to the source
- C. Follow a cutover runbook with a rollback step
- D. Fence the old primary before promotion

### 98. Applications reconnect to the old instance after failover because they cached its address. What should the team adopt?

- A. Add the client range to authorized networks
- B. Use the language connector with IAM credentials
- C. Repoint the connection string at the target
- D. Put a session pooler in front of the instance

### 99. A team must decide how much spare capacity a standby needs so a peak-hour failover keeps its latency target. What is the basis?

- A. Scale down outside business hours
- B. Reserve headroom above the measured peak
- C. Add a read replica for the read traffic
- D. Reduce the machine type to match observed use

### 100. A recovery plan assumes the standby can grow during a failover, but resizing takes forty minutes. What should change?

- A. Reserve headroom above the measured peak
- B. Scale down outside business hours
- C. Pre-size the promoted replica for the full load
- D. Add a read replica for the read traffic

---

## Answer key and explanations

### Question 1 — A

Answer: Reserve headroom above the measured peak. Sizing the current peak plus the committed growth keeps the database inside its shape when the volume arrives, which shrinking or guessing would not. Keep spare capacity so a failover or a traffic spike does not saturate the instance. Local study-map skill 1.1 (Workload Sizing From Current Metrics), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 1 (design innovative, scalable, and highly available cloud database solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Correct. Keep spare capacity so a failover or a traffic spike does not saturate the instance. In this case: Sizing the current peak plus the committed growth keeps the database inside its shape when the volume arrives, which shrinking or guessing would not.
- **B:** Incorrect for this question. A one- or three-year commitment that discounts the capacity always in use. Why the correct answer wins: Sizing the current peak plus the committed growth keeps the database inside its shape when the volume arrives, which shrinking or guessing would not.
- **C:** Incorrect for this question. Shrink an instance whose peak fits a smaller shape. Why the correct answer wins: Sizing the current peak plus the committed growth keeps the database inside its shape when the volume arrives, which shrinking or guessing would not.
- **D:** Incorrect for this question. Choose a shape from measured CPU, memory, and IOPS rather than from a guess. Why the correct answer wins: Sizing the current peak plus the committed growth keeps the database inside its shape when the volume arrives, which shrinking or guessing would not.

### Question 2 — A

Answer: Size the instance from the observed peak metrics. The measured CPU, memory, and throughput peaks give the resize an evidence base, which another guess, a synthetic test, or a commitment cannot. Choose a shape from measured CPU, memory, and IOPS rather than from a guess. Local study-map skill 1.1 (Workload Sizing From Current Metrics), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 1 (design innovative, scalable, and highly available cloud database solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Correct. Choose a shape from measured CPU, memory, and IOPS rather than from a guess. In this case: The measured CPU, memory, and throughput peaks give the resize an evidence base, which another guess, a synthetic test, or a commitment cannot.
- **B:** Incorrect for this question. A one- or three-year commitment that discounts the capacity always in use. Why the correct answer wins: The measured CPU, memory, and throughput peaks give the resize an evidence base, which another guess, a synthetic test, or a commitment cannot.
- **C:** Incorrect for this question. Keep spare capacity so a failover or a traffic spike does not saturate the instance. Why the correct answer wins: The measured CPU, memory, and throughput peaks give the resize an evidence base, which another guess, a synthetic test, or a commitment cannot.
- **D:** Incorrect for this question. Generate representative traffic and read the resource curve before choosing a shape. Why the correct answer wins: The measured CPU, memory, and throughput peaks give the resize an evidence base, which another guess, a synthetic test, or a commitment cannot.

### Question 3 — B

Answer: Increase the disk size to raise throughput. Disk size governs the throughput limit on the instance, so more storage raises the ceiling without paying for compute the workload does not use. Buy more storage so the attached disk also yields more IOPS and throughput. Local study-map skill 1.2 (Compute and Storage Sizing Tradeoffs), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 1 (design innovative, scalable, and highly available cloud database solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Trade a higher price per gigabyte for lower latency on random reads. Why the correct answer wins: Disk size governs the throughput limit on the instance, so more storage raises the ceiling without paying for compute the workload does not use.
- **B:** Correct. Buy more storage so the attached disk also yields more IOPS and throughput. In this case: Disk size governs the throughput limit on the instance, so more storage raises the ceiling without paying for compute the workload does not use.
- **C:** Incorrect for this question. Send reads to a copy so the primary keeps its capacity for writes. Why the correct answer wins: Disk size governs the throughput limit on the instance, so more storage raises the ceiling without paying for compute the workload does not use.
- **D:** Incorrect for this question. Move the instance to a larger shape so more vCPU and memory serve the same data. Why the correct answer wins: Disk size governs the throughput limit on the instance, so more storage raises the ceiling without paying for compute the workload does not use.

### Question 4 — D

Answer: Move the data to SSD storage. SSD storage lowers random-read latency, which is the constraint the CPU figures rule out as the cause. Trade a higher price per gigabyte for lower latency on random reads. Local study-map skill 1.2 (Compute and Storage Sizing Tradeoffs), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 1 (design innovative, scalable, and highly available cloud database solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Trade latency for a lower price on large, throughput-oriented scans. Why the correct answer wins: SSD storage lowers random-read latency, which is the constraint the CPU figures rule out as the cause.
- **B:** Incorrect for this question. A rule that drops versions by age or count, which also bounds recovery. Why the correct answer wins: SSD storage lowers random-read latency, which is the constraint the CPU figures rule out as the cause.
- **C:** Incorrect for this question. Increase the cluster size so more tablet servers absorb the request rate. Why the correct answer wins: SSD storage lowers random-read latency, which is the constraint the CPU figures rule out as the cause.
- **D:** Correct. Trade a higher price per gigabyte for lower latency on random reads. In this case: SSD storage lowers random-read latency, which is the constraint the CPU figures rule out as the cause.

### Question 5 — D

Answer: Increase the machine type of the instance. The working set does not fit in memory, so a larger shape adds the cache the engine needs before any other tuning will help. Move the instance to a larger shape so more vCPU and memory serve the same data. Local study-map skill 1.3 (Machine Type and Storage Type Selection), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 1 (design innovative, scalable, and highly available cloud database solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Buy more storage so the attached disk also yields more IOPS and throughput. Why the correct answer wins: The working set does not fit in memory, so a larger shape adds the cache the engine needs before any other tuning will help.
- **B:** Incorrect for this question. A pooler that multiplexes many application connections onto few database sessions. Why the correct answer wins: The working set does not fit in memory, so a larger shape adds the cache the engine needs before any other tuning will help.
- **C:** Incorrect for this question. Send reads to a copy so the primary keeps its capacity for writes. Why the correct answer wins: The working set does not fit in memory, so a larger shape adds the cache the engine needs before any other tuning will help.
- **D:** Correct. Move the instance to a larger shape so more vCPU and memory serve the same data. In this case: The working set does not fit in memory, so a larger shape adds the cache the engine needs before any other tuning will help.

### Question 6 — B

Answer: Enable autoscaling on the instance. Autoscaling adjusts provisioned compute to the pattern, whereas fixed increments need an operator and Bigtable nodes belong to another service. Let compute follow a target utilization instead of a fixed size. Local study-map skill 1.3 (Machine Type and Storage Type Selection), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 1 (design innovative, scalable, and highly available cloud database solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Increase the cluster size so more tablet servers absorb the request rate. Why the correct answer wins: Autoscaling adjusts provisioned compute to the pattern, whereas fixed increments need an operator and Bigtable nodes belong to another service.
- **B:** Correct. Let compute follow a target utilization instead of a fixed size. In this case: Autoscaling adjusts provisioned compute to the pattern, whereas fixed increments need an operator and Bigtable nodes belong to another service.
- **C:** Incorrect for this question. Raise provisioned compute in 1000-unit node steps or 100-unit increments. Why the correct answer wins: Autoscaling adjusts provisioned compute to the pattern, whereas fixed increments need an operator and Bigtable nodes belong to another service.
- **D:** Incorrect for this question. Move the instance to a larger shape so more vCPU and memory serve the same data. Why the correct answer wins: Autoscaling adjusts provisioned compute to the pattern, whereas fixed increments need an operator and Bigtable nodes belong to another service.

### Question 7 — B, D

Answers: Enable regional high availability with a standby zone; Restore the backup into the second region. A regional instance covers the zone case automatically, and restoring a backup into the second region provides the regional path without a standby to pay for. A primary and standby in two zones of one region with automatic failover. Rebuild the database in the surviving region from the latest backup. Local study-map skill 1.4 (Zonal, Regional, and Multi-Regional Tradeoffs), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 1 (design innovative, scalable, and highly available cloud database solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A copy in a second region that serves reads and can be promoted. Why the correct answer wins: A regional instance covers the zone case automatically, and restoring a backup into the second region provides the regional path without a standby to pay for.
- **B:** Correct. Rebuild the database in the surviving region from the latest backup. In this case: A regional instance covers the zone case automatically, and restoring a backup into the second region provides the regional path without a standby to pay for.
- **C:** Incorrect for this question. Block maintenance during a period when an interruption is unacceptable. Why the correct answer wins: A regional instance covers the zone case automatically, and restoring a backup into the second region provides the regional path without a standby to pay for.
- **D:** Correct. A primary and standby in two zones of one region with automatic failover. In this case: A regional instance covers the zone case automatically, and restoring a backup into the second region provides the regional path without a standby to pay for.
- **E:** Incorrect for this question. A topology that places replicas in separate regions for regional-failure tolerance. Why the correct answer wins: A regional instance covers the zone case automatically, and restoring a backup into the second region provides the regional path without a standby to pay for.

### Question 8 — A

Answer: Add a cross-region read replica. A cross-region replica ships changes continuously and can be promoted, which a restore would be too slow for and a multi-region topology forbids. A copy in a second region that serves reads and can be promoted. Local study-map skill 1.4 (Zonal, Regional, and Multi-Regional Tradeoffs), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 1 (design innovative, scalable, and highly available cloud database solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Correct. A copy in a second region that serves reads and can be promoted. In this case: A cross-region replica ships changes continuously and can be promoted, which a restore would be too slow for and a multi-region topology forbids.
- **B:** Incorrect for this question. A topology that places replicas in separate regions for regional-failure tolerance. Why the correct answer wins: A cross-region replica ships changes continuously and can be promoted, which a restore would be too slow for and a multi-region topology forbids.
- **C:** Incorrect for this question. Rebuild the database in the surviving region from the latest backup. Why the correct answer wins: A cross-region replica ships changes continuously and can be promoted, which a restore would be too slow for and a multi-region topology forbids.
- **D:** Incorrect for this question. One instance in one zone with no standby, so a zone failure stops writes. Why the correct answer wins: A cross-region replica ships changes continuously and can be promoted, which a restore would be too slow for and a multi-region topology forbids.

### Question 9 — D

Answer: Choose a multi-region instance configuration. A multi-region configuration places replicas so that a lost region does not remove write availability, which a regional instance cannot. A topology that places replicas in separate regions for regional-failure tolerance. Local study-map skill 1.4 (Zonal, Regional, and Multi-Regional Tradeoffs), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 1 (design innovative, scalable, and highly available cloud database solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A copy in a second region that serves reads and can be promoted. Why the correct answer wins: A multi-region configuration places replicas so that a lost region does not remove write availability, which a regional instance cannot.
- **B:** Incorrect for this question. Rebuild the database in the surviving region from the latest backup. Why the correct answer wins: A multi-region configuration places replicas so that a lost region does not remove write availability, which a regional instance cannot.
- **C:** Incorrect for this question. A primary and standby in two zones of one region with automatic failover. Why the correct answer wins: A multi-region configuration places replicas so that a lost region does not remove write availability, which a regional instance cannot.
- **D:** Correct. A topology that places replicas in separate regions for regional-failure tolerance. In this case: A multi-region configuration places replicas so that a lost region does not remove write availability, which a regional instance cannot.

### Question 10 — A, B

Answers: Schedule the maintenance window in the low-traffic period; Set a deny maintenance period over the peak event. The window names the hours when patching may run, and the deny period removes the protected week from that schedule. Choose the weekly window when patching may interrupt the instance. Block maintenance during a period when an interruption is unacceptable. Local study-map skill 1.5 (Maintenance Windows and Notification), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 1 (design innovative, scalable, and highly available cloud database solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Correct. Choose the weekly window when patching may interrupt the instance. In this case: The window names the hours when patching may run, and the deny period removes the protected week from that schedule.
- **B:** Correct. Block maintenance during a period when an interruption is unacceptable. In this case: The window names the hours when patching may run, and the deny period removes the protected week from that schedule.
- **C:** Incorrect for this question. Trigger a switchover in a test window and observe how long writes are unavailable. Why the correct answer wins: The window names the hours when patching may run, and the deny period removes the protected week from that schedule.
- **D:** Incorrect for this question. Change the engine version on the running instance during the window. Why the correct answer wins: The window names the hours when patching may run, and the deny period removes the protected week from that schedule.
- **E:** Incorrect for this question. A recovery point that makes the upgrade reversible in practice. Why the correct answer wins: The window names the hours when patching may run, and the deny period removes the protected week from that schedule.

### Question 11 — C

Answer: Set a deny maintenance period over the peak event. A deny period protects exactly those days and lapses afterwards, whereas a normal window would still permit the interruption. Block maintenance during a period when an interruption is unacceptable. Local study-map skill 1.5 (Maintenance Windows and Notification), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 1 (design innovative, scalable, and highly available cloud database solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A recovery point that makes the upgrade reversible in practice. Why the correct answer wins: A deny period protects exactly those days and lapses afterwards, whereas a normal window would still permit the interruption.
- **B:** Incorrect for this question. Apply the configuration change with a brief restart. Why the correct answer wins: A deny period protects exactly those days and lapses afterwards, whereas a normal window would still permit the interruption.
- **C:** Correct. Block maintenance during a period when an interruption is unacceptable. In this case: A deny period protects exactly those days and lapses afterwards, whereas a normal window would still permit the interruption.
- **D:** Incorrect for this question. Choose the weekly window when patching may interrupt the instance. Why the correct answer wins: A deny period protects exactly those days and lapses afterwards, whereas a normal window would still permit the interruption.

### Question 12 — A

Answer: Connect over private IP inside the VPC. A private address in the VPC removes both the public path and the extra process, while an allowlist keeps the public route and a proxy adds the process. A private address reachable only from the VPC and connected networks. Local study-map skill 1.6 (Network Connectivity and Private Access), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 1 (design innovative, scalable, and highly available cloud database solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Correct. A private address reachable only from the VPC and connected networks. In this case: A private address in the VPC removes both the public path and the extra process, while an allowlist keeps the public route and a proxy adds the process.
- **B:** Incorrect for this question. A public address that requires encrypted connections from any client. Why the correct answer wins: A private address in the VPC removes both the public path and the extra process, while an allowlist keeps the public route and a proxy adds the process.
- **C:** Incorrect for this question. A public-IP allowlist that admits the caller range. Why the correct answer wins: A private address in the VPC removes both the public path and the extra process, while an allowlist keeps the public route and a proxy adds the process.
- **D:** Incorrect for this question. A private endpoint in the consumer VPC that reaches the service without peering. Why the correct answer wins: A private address in the VPC removes both the public path and the extra process, while an allowlist keeps the public route and a proxy adds the process.

### Question 13 — B

Answer: Publish the instance behind Private Service Connect. Private Service Connect publishes an endpoint into the consumer network without peering, which a private address alone or an allowlist cannot. A private endpoint in the consumer VPC that reaches the service without peering. Local study-map skill 1.6 (Network Connectivity and Private Access), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 1 (design innovative, scalable, and highly available cloud database solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A centrally managed network that lends subnets to the database project. Why the correct answer wins: Private Service Connect publishes an endpoint into the consumer network without peering, which a private address alone or an allowlist cannot.
- **B:** Correct. A private endpoint in the consumer VPC that reaches the service without peering. In this case: Private Service Connect publishes an endpoint into the consumer network without peering, which a private address alone or an allowlist cannot.
- **C:** Incorrect for this question. A public-IP allowlist that admits the caller range. Why the correct answer wins: Private Service Connect publishes an endpoint into the consumer network without peering, which a private address alone or an allowlist cannot.
- **D:** Incorrect for this question. A private address reachable only from the VPC and connected networks. Why the correct answer wins: Private Service Connect publishes an endpoint into the consumer network without peering, which a private address alone or an allowlist cannot.

### Question 14 — C

Answer: Encrypt with a customer-managed key in Cloud KMS. A customer-managed key gives the company custody and revocation, while a Google-managed key does not and rotation or a log sink does not encrypt at all. A key the customer owns and can rotate or revoke. Local study-map skill 1.7 (Key Management and Encryption), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 1 (design innovative, scalable, and highly available cloud database solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Export entries to storage whose retention cannot be shortened. Why the correct answer wins: A customer-managed key gives the company custody and revocation, while a Google-managed key does not and rotation or a log sink does not encrypt at all.
- **B:** Incorrect for this question. Default encryption at rest with keys the customer neither sees nor manages. Why the correct answer wins: A customer-managed key gives the company custody and revocation, while a Google-managed key does not and rotation or a log sink does not encrypt at all.
- **C:** Correct. A key the customer owns and can rotate or revoke. In this case: A customer-managed key gives the company custody and revocation, while a Google-managed key does not and rotation or a log sink does not encrypt at all.
- **D:** Incorrect for this question. Produce new key versions so an old version stops encrypting new data. Why the correct answer wins: A customer-managed key gives the company custody and revocation, while a Google-managed key does not and rotation or a log sink does not encrypt at all.

### Question 15 — A

Answer: Rotate the customer-managed key on a schedule. Rotation adds a new version for new writes while older ciphertext remains decryptable, which switching key ownership or adding a perimeter does not achieve. Produce new key versions so an old version stops encrypting new data. Local study-map skill 1.7 (Key Management and Encryption), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 1 (design innovative, scalable, and highly available cloud database solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Correct. Produce new key versions so an old version stops encrypting new data. In this case: Rotation adds a new version for new writes while older ciphertext remains decryptable, which switching key ownership or adding a perimeter does not achieve.
- **B:** Incorrect for this question. A key the customer owns and can rotate or revoke. Why the correct answer wins: Rotation adds a new version for new writes while older ciphertext remains decryptable, which switching key ownership or adding a perimeter does not achieve.
- **C:** Incorrect for this question. Default encryption at rest with keys the customer neither sees nor manages. Why the correct answer wins: Rotation adds a new version for new writes while older ciphertext remains decryptable, which switching key ownership or adding a perimeter does not achieve.
- **D:** Incorrect for this question. A boundary that blocks data exfiltration even from an authorized identity. Why the correct answer wins: Rotation adds a new version for new writes while older ciphertext remains decryptable, which switching key ownership or adding a perimeter does not achieve.

### Question 16 — D

Answer: Put a session pooler in front of the instance. A pooler multiplexes those short sessions onto a small set of database connections, so the instance stops running out. A pooler that multiplexes many application connections onto few database sessions. Local study-map skill 1.8 (Session Pooling and Connection Management), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 1 (design innovative, scalable, and highly available cloud database solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Send reads to a copy so the primary keeps its capacity for writes. Why the correct answer wins: A pooler multiplexes those short sessions onto a small set of database connections, so the instance stops running out.
- **B:** Incorrect for this question. Buy a larger shape because the connection limit scales with memory. Why the correct answer wins: A pooler multiplexes those short sessions onto a small set of database connections, so the instance stops running out.
- **C:** Incorrect for this question. Increase the database-level connection ceiling on the instance. Why the correct answer wins: A pooler multiplexes those short sessions onto a small set of database connections, so the instance stops running out.
- **D:** Correct. A pooler that multiplexes many application connections onto few database sessions. In this case: A pooler multiplexes those short sessions onto a small set of database connections, so the instance stops running out.

### Question 17 — D

Answer: Fix the connection leak in the application. The error path leaks sessions, so correcting it stops the growth that a pooler or a larger shape would only absorb. Close sessions that the application opens and never returns to the pool. Local study-map skill 1.8 (Session Pooling and Connection Management), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 1 (design innovative, scalable, and highly available cloud database solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Move the instance to a larger shape so more vCPU and memory serve the same data. Why the correct answer wins: The error path leaks sessions, so correcting it stops the growth that a pooler or a larger shape would only absorb.
- **B:** Incorrect for this question. Increase the database-level connection ceiling on the instance. Why the correct answer wins: The error path leaks sessions, so correcting it stops the growth that a pooler or a larger shape would only absorb.
- **C:** Incorrect for this question. A pooler that multiplexes many application connections onto few database sessions. Why the correct answer wins: The error path leaks sessions, so correcting it stops the growth that a pooler or a larger shape would only absorb.
- **D:** Correct. Close sessions that the application opens and never returns to the pool. In this case: The error path leaks sessions, so correcting it stops the growth that a pooler or a larger shape would only absorb.

### Question 18 — C, E

Answers: Enable Data Access audit logs; Route the audit logs to a locked log bucket. Writes to table data appear only in Data Access logs, and routing them to retained storage keeps the evidence available for the required period. Record reads and writes, which are not captured by default. Export entries to storage whose retention cannot be shortened. Local study-map skill 1.9 (Auditing Policies for Managed Services), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 1 (design innovative, scalable, and highly available cloud database solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Record configuration changes only, leaving row-level reads unaudited. Why the correct answer wins: Writes to table data appear only in Data Access logs, and routing them to retained storage keeps the evidence available for the required period.
- **B:** Incorrect for this question. Turn a recurring log pattern into a metric that can be charted and alerted on. Why the correct answer wins: Writes to table data appear only in Data Access logs, and routing them to retained storage keeps the evidence available for the required period.
- **C:** Correct. Export entries to storage whose retention cannot be shortened. In this case: Writes to table data appear only in Data Access logs, and routing them to retained storage keeps the evidence available for the required period.
- **D:** Incorrect for this question. A single view of health, security, and version posture across database instances. Why the correct answer wins: Writes to table data appear only in Data Access logs, and routing them to retained storage keeps the evidence available for the required period.
- **E:** Correct. Record reads and writes, which are not captured by default. In this case: Writes to table data appear only in Data Access logs, and routing them to retained storage keeps the evidence available for the required period.

### Question 19 — D

Answer: Rely on Admin Activity audit logs. Configuration changes are recorded as administrative activity by default, while data-access and query views do not record the setting change. Record configuration changes only, leaving row-level reads unaudited. Local study-map skill 1.9 (Auditing Policies for Managed Services), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 1 (design innovative, scalable, and highly available cloud database solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A per-query view of latency, load, and wait events on the instance. Why the correct answer wins: Configuration changes are recorded as administrative activity by default, while data-access and query views do not record the setting change.
- **B:** Incorrect for this question. A single view of health, security, and version posture across database instances. Why the correct answer wins: Configuration changes are recorded as administrative activity by default, while data-access and query views do not record the setting change.
- **C:** Incorrect for this question. Record reads and writes, which are not captured by default. Why the correct answer wins: Configuration changes are recorded as administrative activity by default, while data-access and query views do not record the setting change.
- **D:** Correct. Record configuration changes only, leaving row-level reads unaudited. In this case: Configuration changes are recorded as administrative activity by default, while data-access and query views do not record the setting change.

### Question 20 — D

Answer: Use Cloud SQL for the relational workload. A managed relational instance covers that size with patching and backups handled, while self-management adds work and the distributed options add complexity. A managed MySQL, PostgreSQL, or SQL Server instance with Google-operated backups, patching, and failover. Local study-map skill 1.10 (Managed, Self-Managed, and Partner Offerings), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 1 (design innovative, scalable, and highly available cloud database solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A horizontally scalable relational database with strong consistency across regions and no manual sharding. Why the correct answer wins: A managed relational instance covers that size with patching and backups handled, while self-management adds work and the distributed options add complexity.
- **B:** Incorrect for this question. A self-managed engine on virtual machines where the team owns patching, backups, and failover. Why the correct answer wins: A managed relational instance covers that size with patching and backups handled, while self-management adds work and the distributed options add complexity.
- **C:** Incorrect for this question. A managed PostgreSQL-compatible database with a separate read pool and columnar acceleration for mixed transactional and analytical load. Why the correct answer wins: A managed relational instance covers that size with patching and backups handled, while self-management adds work and the distributed options add complexity.
- **D:** Correct. A managed MySQL, PostgreSQL, or SQL Server instance with Google-operated backups, patching, and failover. In this case: A managed relational instance covers that size with patching and backups handled, while self-management adds work and the distributed options add complexity.

### Question 21 — C

Answer: Run the database on bare metal solution. Bare metal provides that hardware access, whereas a self-managed virtual machine, a partner service, or a managed database each place a hypervisor in the path. Dedicated hardware for engines that cannot be virtualized or licensed for a managed service. Local study-map skill 1.10 (Managed, Self-Managed, and Partner Offerings), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 1 (design innovative, scalable, and highly available cloud database solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A managed MySQL, PostgreSQL, or SQL Server instance with Google-operated backups, patching, and failover. Why the correct answer wins: Bare metal provides that hardware access, whereas a self-managed virtual machine, a partner service, or a managed database each place a hypervisor in the path.
- **B:** Incorrect for this question. A third-party database operated by its vendor on Google Cloud infrastructure. Why the correct answer wins: Bare metal provides that hardware access, whereas a self-managed virtual machine, a partner service, or a managed database each place a hypervisor in the path.
- **C:** Correct. Dedicated hardware for engines that cannot be virtualized or licensed for a managed service. In this case: Bare metal provides that hardware access, whereas a self-managed virtual machine, a partner service, or a managed database each place a hypervisor in the path.
- **D:** Incorrect for this question. A self-managed engine on virtual machines where the team owns patching, backups, and failover. Why the correct answer wins: Bare metal provides that hardware access, whereas a self-managed virtual machine, a partner service, or a managed database each place a hypervisor in the path.

### Question 22 — B, C

Answers: Use Bigtable for the high-throughput wide-column workload; Export the table into BigQuery. A wide-column store carries the key-based read load, and exporting into the warehouse serves the analytical scans without loading the operational system. A wide-column NoSQL service built for very high write and read rates over a sparse, row-key-ordered model. Copy the analytical slice into the warehouse on a schedule. Local study-map skill 1.11 (SQL and NoSQL Data Model Fit), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 1 (design innovative, scalable, and highly available cloud database solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A document database with automatic multi-region replication, offline client support, and index-driven queries. Why the correct answer wins: A wide-column store carries the key-based read load, and exporting into the warehouse serves the analytical scans without loading the operational system.
- **B:** Correct. A wide-column NoSQL service built for very high write and read rates over a sparse, row-key-ordered model. In this case: A wide-column store carries the key-based read load, and exporting into the warehouse serves the analytical scans without loading the operational system.
- **C:** Correct. Copy the analytical slice into the warehouse on a schedule. In this case: A wide-column store carries the key-based read load, and exporting into the warehouse serves the analytical scans without loading the operational system.
- **D:** Incorrect for this question. A managed Redis-compatible in-memory store placed in front of the system of record. Why the correct answer wins: A wide-column store carries the key-based read load, and exporting into the warehouse serves the analytical scans without loading the operational system.
- **E:** Incorrect for this question. A managed MySQL, PostgreSQL, or SQL Server instance with Google-operated backups, patching, and failover. Why the correct answer wins: A wide-column store carries the key-based read load, and exporting into the warehouse serves the analytical scans without loading the operational system.

### Question 23 — A

Answer: Use Firestore for the document workload. The document model with offline client support and index-driven queries matches the requirement, which the other options do not provide together. A document database with automatic multi-region replication, offline client support, and index-driven queries. Local study-map skill 1.11 (SQL and NoSQL Data Model Fit), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 1 (design innovative, scalable, and highly available cloud database solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Correct. A document database with automatic multi-region replication, offline client support, and index-driven queries. In this case: The document model with offline client support and index-driven queries matches the requirement, which the other options do not provide together.
- **B:** Incorrect for this question. A managed Redis-compatible in-memory store placed in front of the system of record. Why the correct answer wins: The document model with offline client support and index-driven queries matches the requirement, which the other options do not provide together.
- **C:** Incorrect for this question. A wide-column NoSQL service built for very high write and read rates over a sparse, row-key-ordered model. Why the correct answer wins: The document model with offline client support and index-driven queries matches the requirement, which the other options do not provide together.
- **D:** Incorrect for this question. A managed MySQL, PostgreSQL, or SQL Server instance with Google-operated backups, patching, and failover. Why the correct answer wins: The document model with offline client support and index-driven queries matches the requirement, which the other options do not provide together.

### Question 24 — A

Answer: Use Cloud SQL for the relational workload. A managed relational instance provides exactly those semantics at that size, while the distributed option adds cost and the NoSQL options change the model. A managed MySQL, PostgreSQL, or SQL Server instance with Google-operated backups, patching, and failover. Local study-map skill 1.11 (SQL and NoSQL Data Model Fit), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 1 (design innovative, scalable, and highly available cloud database solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Correct. A managed MySQL, PostgreSQL, or SQL Server instance with Google-operated backups, patching, and failover. In this case: A managed relational instance provides exactly those semantics at that size, while the distributed option adds cost and the NoSQL options change the model.
- **B:** Incorrect for this question. A wide-column NoSQL service built for very high write and read rates over a sparse, row-key-ordered model. Why the correct answer wins: A managed relational instance provides exactly those semantics at that size, while the distributed option adds cost and the NoSQL options change the model.
- **C:** Incorrect for this question. A managed Redis-compatible in-memory store placed in front of the system of record. Why the correct answer wins: A managed relational instance provides exactly those semantics at that size, while the distributed option adds cost and the NoSQL options change the model.
- **D:** Incorrect for this question. A horizontally scalable relational database with strong consistency across regions and no manual sharding. Why the correct answer wins: A managed relational instance provides exactly those semantics at that size, while the distributed option adds cost and the NoSQL options change the model.

### Question 25 — D

Answer: Use AlloyDB vector search with a ScaNN index. A purpose-built vector index inside AlloyDB handles that volume with filters in place, which an unindexed extension or a copy into another system does not. A vector index tuned for large embedding sets on AlloyDB. Local study-map skill 1.12 (Vector and Generative AI Requirements), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 1 (design innovative, scalable, and highly available cloud database solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Copy the analytical slice into the warehouse on a schedule. Why the correct answer wins: A purpose-built vector index inside AlloyDB handles that volume with filters in place, which an unindexed extension or a copy into another system does not.
- **B:** Incorrect for this question. Read the operational table from BigQuery without copying it first. Why the correct answer wins: A purpose-built vector index inside AlloyDB handles that volume with filters in place, which an unindexed extension or a copy into another system does not.
- **C:** Incorrect for this question. Store embeddings beside relational rows and search them in the same engine. Why the correct answer wins: A purpose-built vector index inside AlloyDB handles that volume with filters in place, which an unindexed extension or a copy into another system does not.
- **D:** Correct. A vector index tuned for large embedding sets on AlloyDB. In this case: A purpose-built vector index inside AlloyDB handles that volume with filters in place, which an unindexed extension or a copy into another system does not.

### Question 26 — B

Answer: Enable the vector extension on PostgreSQL. Enabling the vector extension adds the capability to the engine already in use, which is the shortest path for a prototype at that size. Store embeddings beside relational rows and search them in the same engine. Local study-map skill 1.12 (Vector and Generative AI Requirements), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 1 (design innovative, scalable, and highly available cloud database solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A vector index tuned for large embedding sets on AlloyDB. Why the correct answer wins: Enabling the vector extension adds the capability to the engine already in use, which is the shortest path for a prototype at that size.
- **B:** Correct. Store embeddings beside relational rows and search them in the same engine. In this case: Enabling the vector extension adds the capability to the engine already in use, which is the shortest path for a prototype at that size.
- **C:** Incorrect for this question. Absorb repeated reads in memory so the database sees fewer of them. Why the correct answer wins: Enabling the vector extension adds the capability to the engine already in use, which is the shortest path for a prototype at that size.
- **D:** Incorrect for this question. An approximate-nearest-neighbour index over embedding columns. Why the correct answer wins: Enabling the vector extension adds the capability to the engine already in use, which is the shortest path for a prototype at that size.

### Question 27 — A, B

Answers: Commit to the steady baseline capacity; Split development workloads onto their own instance. Committing the steady baseline lowers its unit price, and splitting development onto its own instance stops test work from driving production's shape. A one- or three-year commitment that discounts the capacity always in use. Keep experimentation off the production shape and budget. Local study-map skill 1.13 (Comparative Cost Analysis Across Databases), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 1 (design innovative, scalable, and highly available cloud database solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Correct. Keep experimentation off the production shape and budget. In this case: Committing the steady baseline lowers its unit price, and splitting development onto its own instance stops test work from driving production's shape.
- **B:** Correct. A one- or three-year commitment that discounts the capacity always in use. In this case: Committing the steady baseline lowers its unit price, and splitting development onto its own instance stops test work from driving production's shape.
- **C:** Incorrect for this question. Remove capacity that serves no traffic. Why the correct answer wins: Committing the steady baseline lowers its unit price, and splitting development onto its own instance stops test work from driving production's shape.
- **D:** Incorrect for this question. The automatic discount that applies to long-running Compute Engine usage. Why the correct answer wins: Committing the steady baseline lowers its unit price, and splitting development onto its own instance stops test work from driving production's shape.
- **E:** Incorrect for this question. Avoid a full-disk outage at the cost of unplanned storage growth. Why the correct answer wins: Committing the steady baseline lowers its unit price, and splitting development onto its own instance stops test work from driving production's shape.

### Question 28 — A

Answer: Move the data to HDD storage. HDD storage costs less per gigabyte for throughput-oriented access, while SSD, more nodes, or a garbage-collection rule do not reduce the storage price. Trade latency for a lower price on large, throughput-oriented scans. Local study-map skill 1.13 (Comparative Cost Analysis Across Databases), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 1 (design innovative, scalable, and highly available cloud database solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Correct. Trade latency for a lower price on large, throughput-oriented scans. In this case: HDD storage costs less per gigabyte for throughput-oriented access, while SSD, more nodes, or a garbage-collection rule do not reduce the storage price.
- **B:** Incorrect for this question. A rule that drops versions by age or count, which also bounds recovery. Why the correct answer wins: HDD storage costs less per gigabyte for throughput-oriented access, while SSD, more nodes, or a garbage-collection rule do not reduce the storage price.
- **C:** Incorrect for this question. Increase the cluster size so more tablet servers absorb the request rate. Why the correct answer wins: HDD storage costs less per gigabyte for throughput-oriented access, while SSD, more nodes, or a garbage-collection rule do not reduce the storage price.
- **D:** Incorrect for this question. Trade a higher price per gigabyte for lower latency on random reads. Why the correct answer wins: HDD storage costs less per gigabyte for throughput-oriented access, while SSD, more nodes, or a garbage-collection rule do not reduce the storage price.

### Question 29 — A

Answer: Keep the current engine and version. Keeping the engine avoids rewriting behaviour that cannot be delivered in the timeline, whereas a heterogeneous move takes on exactly that work. A lift of the existing engine with no conversion work, retaining its behaviour and licensing. Local study-map skill 1.14 (Application and Database Dependencies), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 1 (design innovative, scalable, and highly available cloud database solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Correct. A lift of the existing engine with no conversion work, retaining its behaviour and licensing. In this case: Keeping the engine avoids rewriting behaviour that cannot be delivered in the timeline, whereas a heterogeneous move takes on exactly that work.
- **B:** Incorrect for this question. Weigh engine compatibility and code rewrite effort before selecting a destination. Why the correct answer wins: Keeping the engine avoids rewriting behaviour that cannot be delivered in the timeline, whereas a heterogeneous move takes on exactly that work.
- **C:** Incorrect for this question. Keep two databases current from application code during the transition. Why the correct answer wins: Keeping the engine avoids rewriting behaviour that cannot be delivered in the timeline, whereas a heterogeneous move takes on exactly that work.
- **D:** Incorrect for this question. A managed path that converts schema and code from a different source engine. Why the correct answer wins: Keeping the engine avoids rewriting behaviour that cannot be delivered in the timeline, whereas a heterogeneous move takes on exactly that work.

### Question 30 — D, E

Answers: Place the instance in the required region; Add the projects to a VPC Service Controls perimeter. Choosing the in-country region settles where the data lives, and a service perimeter blocks the copying path even for an authorized identity. A location choice that keeps data inside the regulated boundary. A boundary that blocks data exfiltration even from an authorized identity. Local study-map skill 1.15 (Regulatory, Compliance, and Organization Policy), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 1 (design innovative, scalable, and highly available cloud database solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A topology that places replicas in separate regions for regional-failure tolerance. Why the correct answer wins: Choosing the in-country region settles where the data lives, and a service perimeter blocks the copying path even for an authorized identity.
- **B:** Incorrect for this question. Absorb repeated reads in memory so the database sees fewer of them. Why the correct answer wins: Choosing the in-country region settles where the data lives, and a service perimeter blocks the copying path even for an authorized identity.
- **C:** Incorrect for this question. Default encryption at rest with keys the customer neither sees nor manages. Why the correct answer wins: Choosing the in-country region settles where the data lives, and a service perimeter blocks the copying path even for an authorized identity.
- **D:** Correct. A boundary that blocks data exfiltration even from an authorized identity. In this case: Choosing the in-country region settles where the data lives, and a service perimeter blocks the copying path even for an authorized identity.
- **E:** Correct. A location choice that keeps data inside the regulated boundary. In this case: Choosing the in-country region settles where the data lives, and a service perimeter blocks the copying path even for an authorized identity.

### Question 31 — C

Answer: Enforce the location with an organization policy. An organization-level constraint blocks the creation regardless of who creates the project, which a per-instance choice or an encryption setting does not. A constraint that keeps database resources inside the approved regions. Local study-map skill 1.15 (Regulatory, Compliance, and Organization Policy), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 1 (design innovative, scalable, and highly available cloud database solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A location choice that keeps data inside the regulated boundary. Why the correct answer wins: An organization-level constraint blocks the creation regardless of who creates the project, which a per-instance choice or an encryption setting does not.
- **B:** Incorrect for this question. A key the customer owns and can rotate or revoke. Why the correct answer wins: An organization-level constraint blocks the creation regardless of who creates the project, which a per-instance choice or an encryption setting does not.
- **C:** Correct. A constraint that keeps database resources inside the approved regions. In this case: An organization-level constraint blocks the creation regardless of who creates the project, which a per-instance choice or an encryption setting does not.
- **D:** Incorrect for this question. Export entries to storage whose retention cannot be shortened. Why the correct answer wins: An organization-level constraint blocks the creation regardless of who creates the project, which a per-instance choice or an encryption setting does not.

### Question 32 — D

Answer: Query the source through BigQuery federated queries. A federated query reads the Spanner table in place, whereas an export, a stream, or a hybrid link duplicates or moves the rows. Read the operational table from BigQuery without copying it first. Local study-map skill 1.16 (Federation, Exports, and Hybrid Spans), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 1 (design innovative, scalable, and highly available cloud database solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Copy the analytical slice into the warehouse on a schedule. Why the correct answer wins: A federated query reads the Spanner table in place, whereas an export, a stream, or a hybrid link duplicates or moves the rows.
- **B:** Incorrect for this question. Interconnect the remaining on-premises system rather than moving it. Why the correct answer wins: A federated query reads the Spanner table in place, whereas an export, a stream, or a hybrid link duplicates or moves the rows.
- **C:** Incorrect for this question. Keep an analytics copy current by applying change data capture. Why the correct answer wins: A federated query reads the Spanner table in place, whereas an export, a stream, or a hybrid link duplicates or moves the rows.
- **D:** Correct. Read the operational table from BigQuery without copying it first. In this case: A federated query reads the Spanner table in place, whereas an export, a stream, or a hybrid link duplicates or moves the rows.

### Question 33 — D, E

Answers: Enable IAM database authentication; Limit the user to the required schema. IAM database authentication removes the stored credential, and a schema-scoped grant keeps the tool away from every other object. Map an IAM principal to a database user so no password is stored. Grant access to named objects instead of the whole instance. Local study-map skill 2.1 (IAM for Database Connectivity), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 2 (manage a solution that can span multiple database technologies): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A native database user whose credential must be rotated and stored. Why the correct answer wins: IAM database authentication removes the stored credential, and a schema-scoped grant keeps the tool away from every other object.
- **B:** Incorrect for this question. A broad legacy role that can change most resources in the project. Why the correct answer wins: IAM database authentication removes the stored credential, and a schema-scoped grant keeps the tool away from every other object.
- **C:** Incorrect for this question. A single credential used by every workload that touches the database. Why the correct answer wins: IAM database authentication removes the stored credential, and a schema-scoped grant keeps the tool away from every other object.
- **D:** Correct. Map an IAM principal to a database user so no password is stored. In this case: IAM database authentication removes the stored credential, and a schema-scoped grant keeps the tool away from every other object.
- **E:** Correct. Grant access to named objects instead of the whole instance. In this case: IAM database authentication removes the stored credential, and a schema-scoped grant keeps the tool away from every other object.

### Question 34 — B

Answer: Grant the predefined database role. A narrower predefined role supplies the read access actually needed, while the administrator and editor roles keep permissions the task never uses. A Google-managed role that carries the permissions the operator needs. Local study-map skill 2.1 (IAM for Database Connectivity), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 2 (manage a solution that can span multiple database technologies): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A broad legacy role that can change most resources in the project. Why the correct answer wins: A narrower predefined role supplies the read access actually needed, while the administrator and editor roles keep permissions the task never uses.
- **B:** Correct. A Google-managed role that carries the permissions the operator needs. In this case: A narrower predefined role supplies the read access actually needed, while the administrator and editor roles keep permissions the task never uses.
- **C:** Incorrect for this question. A role built from an explicit permission list. Why the correct answer wins: A narrower predefined role supplies the read access actually needed, while the administrator and editor roles keep permissions the task never uses.
- **D:** Incorrect for this question. Individual accountability at the engine layer rather than a shared login. Why the correct answer wins: A narrower predefined role supplies the read access actually needed, while the administrator and editor roles keep permissions the task never uses.

### Question 35 — B

Answer: Have the application authenticate as a service account. A service account gives the workload its own revocable identity, which a stored password or a shared login cannot provide. A workload identity that can be authorized by IAM without a stored password. Local study-map skill 2.2 (Database Users and Authentication), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 2 (manage a solution that can span multiple database technologies): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A single credential used by every workload that touches the database. Why the correct answer wins: A service account gives the workload its own revocable identity, which a stored password or a shared login cannot provide.
- **B:** Correct. A workload identity that can be authorized by IAM without a stored password. In this case: A service account gives the workload its own revocable identity, which a stored password or a shared login cannot provide.
- **C:** Incorrect for this question. Individual accountability at the engine layer rather than a shared login. Why the correct answer wins: A service account gives the workload its own revocable identity, which a stored password or a shared login cannot provide.
- **D:** Incorrect for this question. A native database user whose credential must be rotated and stored. Why the correct answer wins: A service account gives the workload its own revocable identity, which a stored password or a shared login cannot provide.

### Question 36 — D, E

Answers: Read the query plan for the statement; Add the index the slow query needs. Reading the plan shows which access path costs the time, and the index addresses that path once it is known. Inspect the chosen scan and join order before changing anything. Create an index that turns a scan into a lookup for the predicate. Local study-map skill 2.3 (Slow Queries and Missing Indexes), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 2 (manage a solution that can span multiple database technologies): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Split one table into ranges so pruning and maintenance act on less data. Why the correct answer wins: Reading the plan shows which access path costs the time, and the index addresses that path once it is known.
- **B:** Incorrect for this question. Give the planner current cardinality so it stops choosing a poor plan. Why the correct answer wins: Reading the plan shows which access path costs the time, and the index addresses that path once it is known.
- **C:** Incorrect for this question. Absorb repeated reads in memory so the database sees fewer of them. Why the correct answer wins: Reading the plan shows which access path costs the time, and the index addresses that path once it is known.
- **D:** Correct. Create an index that turns a scan into a lookup for the predicate. In this case: Reading the plan shows which access path costs the time, and the index addresses that path once it is known.
- **E:** Correct. Inspect the chosen scan and join order before changing anything. In this case: Reading the plan shows which access path costs the time, and the index addresses that path once it is known.

### Question 37 — B

Answer: Drop the unused index. Removing indexes nothing reads cuts the maintenance cost on every write, while another index, more memory, or partitioning adds work instead. Remove write amplification from an index nothing reads. Local study-map skill 2.3 (Slow Queries and Missing Indexes), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 2 (manage a solution that can span multiple database technologies): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Create an index that turns a scan into a lookup for the predicate. Why the correct answer wins: Removing indexes nothing reads cuts the maintenance cost on every write, while another index, more memory, or partitioning adds work instead.
- **B:** Correct. Remove write amplification from an index nothing reads. In this case: Removing indexes nothing reads cuts the maintenance cost on every write, while another index, more memory, or partitioning adds work instead.
- **C:** Incorrect for this question. Split one table into ranges so pruning and maintenance act on less data. Why the correct answer wins: Removing indexes nothing reads cuts the maintenance cost on every write, while another index, more memory, or partitioning adds work instead.
- **D:** Incorrect for this question. Give sorts and joins more working memory on the instance. Why the correct answer wins: Removing indexes nothing reads cuts the maintenance cost on every write, while another index, more memory, or partitioning adds work instead.

### Question 38 — B

Answer: Batch the writes into fewer round trips. Committing in smaller batches shortens the lock window, whereas killing the session or inspecting locks leaves the single long transaction in place. Cut per-row network and commit overhead in the application. Local study-map skill 2.4 (Locking and Resource Contention), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 2 (manage a solution that can span multiple database technologies): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A pooler that multiplexes many application connections onto few database sessions. Why the correct answer wins: Committing in smaller batches shortens the lock window, whereas killing the session or inspecting locks leaves the single long transaction in place.
- **B:** Correct. Cut per-row network and commit overhead in the application. In this case: Committing in smaller batches shortens the lock window, whereas killing the session or inspecting locks leaves the single long transaction in place.
- **C:** Incorrect for this question. End the blocking transaction so the queue drains. Why the correct answer wins: Committing in smaller batches shortens the lock window, whereas killing the session or inspecting locks leaves the single long transaction in place.
- **D:** Incorrect for this question. Find the transaction that holds the lock others wait on. Why the correct answer wins: Committing in smaller batches shortens the lock window, whereas killing the session or inspecting locks leaves the single long transaction in place.

### Question 39 — D

Answer: Inspect lock waits and blocking sessions. The lock graph names the blocking transaction, which no batching or statistics change can identify. Find the transaction that holds the lock others wait on. Local study-map skill 2.4 (Locking and Resource Contention), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 2 (manage a solution that can span multiple database technologies): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Cut per-row network and commit overhead in the application. Why the correct answer wins: The lock graph names the blocking transaction, which no batching or statistics change can identify.
- **B:** Incorrect for this question. Give the planner current cardinality so it stops choosing a poor plan. Why the correct answer wins: The lock graph names the blocking transaction, which no batching or statistics change can identify.
- **C:** Incorrect for this question. Create an index that turns a scan into a lookup for the predicate. Why the correct answer wins: The lock graph names the blocking transaction, which no batching or statistics change can identify.
- **D:** Correct. Find the transaction that holds the lock others wait on. In this case: The lock graph names the blocking transaction, which no batching or statistics change can identify.

### Question 40 — B, C

Answers: Use Query Insights to find the heavy statements; Watch CPU, memory, disk, and IOPS together. Per-query data shows which statements became expensive, and resource vitals show whether a new ceiling was hit, together separating cause from coincidence. A per-query view of latency, load, and wait events on the instance. Read the instance-level signals before attributing the symptom to the query. Local study-map skill 2.5 (Database Vitals Monitoring), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 2 (manage a solution that can span multiple database technologies): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. The engine log of statements that exceeded the long-query threshold. Why the correct answer wins: Per-query data shows which statements became expensive, and resource vitals show whether a new ceiling was hit, together separating cause from coincidence.
- **B:** Correct. Read the instance-level signals before attributing the symptom to the query. In this case: Per-query data shows which statements became expensive, and resource vitals show whether a new ceiling was hit, together separating cause from coincidence.
- **C:** Correct. A per-query view of latency, load, and wait events on the instance. In this case: Per-query data shows which statements became expensive, and resource vitals show whether a new ceiling was hit, together separating cause from coincidence.
- **D:** Incorrect for this question. A single view of health, security, and version posture across database instances. Why the correct answer wins: Per-query data shows which statements became expensive, and resource vitals show whether a new ceiling was hit, together separating cause from coincidence.
- **E:** Incorrect for this question. Turn a recurring log pattern into a metric that can be charted and alerted on. Why the correct answer wins: Per-query data shows which statements became expensive, and resource vitals show whether a new ceiling was hit, together separating cause from coincidence.

### Question 41 — B

Answer: Build a log-based metric from the error entries. A metric derived from the log pattern makes the bursts measurable and alertable, which reading entries by hand cannot sustain. Turn a recurring log pattern into a metric that can be charted and alerted on. Local study-map skill 2.5 (Database Vitals Monitoring), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 2 (manage a solution that can span multiple database technologies): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. The engine log of statements that exceeded the long-query threshold. Why the correct answer wins: A metric derived from the log pattern makes the bursts measurable and alertable, which reading entries by hand cannot sustain.
- **B:** Correct. Turn a recurring log pattern into a metric that can be charted and alerted on. In this case: A metric derived from the log pattern makes the bursts measurable and alertable, which reading entries by hand cannot sustain.
- **C:** Incorrect for this question. Export entries to storage whose retention cannot be shortened. Why the correct answer wins: A metric derived from the log pattern makes the bursts measurable and alertable, which reading entries by hand cannot sustain.
- **D:** Incorrect for this question. A liveness signal that fires before users report the outage. Why the correct answer wins: A metric derived from the log pattern makes the bursts measurable and alertable, which reading entries by hand cannot sustain.

### Question 42 — A

Answer: Request a quota increase for the project. The ceiling has to be raised so the recovery can proceed, since retrying or waiting would not serve the incident. Raise the project-level ceiling so the operation is no longer refused. Local study-map skill 2.6 (Quotas and Limits), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 2 (manage a solution that can span multiple database technologies): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Correct. Raise the project-level ceiling so the operation is no longer refused. In this case: The ceiling has to be raised so the recovery can proceed, since retrying or waiting would not serve the incident.
- **B:** Incorrect for this question. Stagger the work so concurrent operations stop colliding on the same limit. Why the correct answer wins: The ceiling has to be raised so the recovery can proceed, since retrying or waiting would not serve the incident.
- **C:** Incorrect for this question. Repeat the call after a growing delay so a transient refusal clears. Why the correct answer wins: The ceiling has to be raised so the recovery can proceed, since retrying or waiting would not serve the incident.
- **D:** Incorrect for this question. A flat-file extract for a downstream loader rather than a restore. Why the correct answer wins: The ceiling has to be raised so the recovery can proceed, since retrying or waiting would not serve the incident.

### Question 43 — C

Answer: Alert on replication lag. An alert on replication lag reports the staleness when it exceeds the tolerated window. Page when the copy falls behind the primary by more than the budget. Local study-map skill 2.7 (Alerts for Errors and Performance), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 2 (manage a solution that can span multiple database technologies): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A condition that pages a human when the threshold is crossed. Why the correct answer wins: An alert on replication lag reports the staleness when it exceeds the tolerated window.
- **B:** Incorrect for this question. Page on failed statements rather than on resource saturation alone. Why the correct answer wins: An alert on replication lag reports the staleness when it exceeds the tolerated window.
- **C:** Correct. Page when the copy falls behind the primary by more than the budget. In this case: An alert on replication lag reports the staleness when it exceeds the tolerated window.
- **D:** Incorrect for this question. Read the instance-level signals before attributing the symptom to the query. Why the correct answer wins: An alert on replication lag reports the staleness when it exceeds the tolerated window.

### Question 44 — A

Answer: Alert on the database error rate. Alerting on the error rate reflects what users experience, while a resource threshold pages on load that may not affect them. Page on failed statements rather than on resource saturation alone. Local study-map skill 2.7 (Alerts for Errors and Performance), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 2 (manage a solution that can span multiple database technologies): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Correct. Page on failed statements rather than on resource saturation alone. In this case: Alerting on the error rate reflects what users experience, while a resource threshold pages on load that may not affect them.
- **B:** Incorrect for this question. Page when the copy falls behind the primary by more than the budget. Why the correct answer wins: Alerting on the error rate reflects what users experience, while a resource threshold pages on load that may not affect them.
- **C:** Incorrect for this question. A per-query view of latency, load, and wait events on the instance. Why the correct answer wins: Alerting on the error rate reflects what users experience, while a resource threshold pages on load that may not affect them.
- **D:** Incorrect for this question. A condition that pages a human when the threshold is crossed. Why the correct answer wins: Alerting on the error rate reflects what users experience, while a resource threshold pages on load that may not affect them.

### Question 45 — A, E

Answers: Enable point-in-time recovery; Export a logical dump to Cloud Storage. Point-in-time recovery returns the instance to the moment before the change, and a logical dump supports loading a single table. Continuous log capture that lets the instance return to an arbitrary moment. A portable SQL dump taken with the engine tooling. Local study-map skill 2.8 (Backup and Recovery Option Selection), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 2 (manage a solution that can span multiple database technologies): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Correct. A portable SQL dump taken with the engine tooling. In this case: Point-in-time recovery returns the instance to the moment before the change, and a logical dump supports loading a single table.
- **B:** Incorrect for this question. Keep backups longer so an older restore point remains available. Why the correct answer wins: Point-in-time recovery returns the instance to the moment before the change, and a logical dump supports loading a single table.
- **C:** Incorrect for this question. A copy of the current data created without touching the source. Why the correct answer wins: Point-in-time recovery returns the instance to the moment before the change, and a logical dump supports loading a single table.
- **D:** Incorrect for this question. A manual checkpoint taken immediately before a risky operation. Why the correct answer wins: Point-in-time recovery returns the instance to the moment before the change, and a logical dump supports loading a single table.
- **E:** Correct. Continuous log capture that lets the instance return to an arbitrary moment. In this case: Point-in-time recovery returns the instance to the moment before the change, and a logical dump supports loading a single table.

### Question 46 — C

Answer: Enable automated backups with a retention window. Automated backups give a managed schedule and retention, which a manual dump or a clone does not provide. Scheduled backups kept for a chosen number of days. Local study-map skill 2.8 (Backup and Recovery Option Selection), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 2 (manage a solution that can span multiple database technologies): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A flat-file extract for a downstream loader rather than a restore. Why the correct answer wins: Automated backups give a managed schedule and retention, which a manual dump or a clone does not provide.
- **B:** Incorrect for this question. A manual checkpoint taken immediately before a risky operation. Why the correct answer wins: Automated backups give a managed schedule and retention, which a manual dump or a clone does not provide.
- **C:** Correct. Scheduled backups kept for a chosen number of days. In this case: Automated backups give a managed schedule and retention, which a manual dump or a clone does not provide.
- **D:** Incorrect for this question. A copy of the current data created without touching the source. Why the correct answer wins: Automated backups give a managed schedule and retention, which a manual dump or a clone does not provide.

### Question 47 — C

Answer: Export the table to CSV in Cloud Storage. A CSV extract is what a loader consumes, whereas a logical dump is for database restore and the other options move data elsewhere. A flat-file extract for a downstream loader rather than a restore. Local study-map skill 2.9 (Export and Import Configuration), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 2 (manage a solution that can span multiple database technologies): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A portable SQL dump taken with the engine tooling. Why the correct answer wins: A CSV extract is what a loader consumes, whereas a logical dump is for database restore and the other options move data elsewhere.
- **B:** Incorrect for this question. Copy the analytical slice into the warehouse on a schedule. Why the correct answer wins: A CSV extract is what a loader consumes, whereas a logical dump is for database restore and the other options move data elsewhere.
- **C:** Correct. A flat-file extract for a downstream loader rather than a restore. In this case: A CSV extract is what a loader consumes, whereas a logical dump is for database restore and the other options move data elsewhere.
- **D:** Incorrect for this question. Load a logical dump file into the database through the managed import path. Why the correct answer wins: A CSV extract is what a loader consumes, whereas a logical dump is for database restore and the other options move data elsewhere.

### Question 48 — C

Answer: Design the restore path to the stated RTO and RPO. The recovery point and recovery time objectives state the acceptable loss and duration, which the existing backups alone do not express. Choose mechanisms by how much data and time the business can lose. Local study-map skill 2.10 (RTO, RPO, and Point-in-Time Recovery), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 2 (manage a solution that can span multiple database technologies): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A copy of the current data created without touching the source. Why the correct answer wins: The recovery point and recovery time objectives state the acceptable loss and duration, which the existing backups alone do not express.
- **B:** Incorrect for this question. Continuous log capture that lets the instance return to an arbitrary moment. Why the correct answer wins: The recovery point and recovery time objectives state the acceptable loss and duration, which the existing backups alone do not express.
- **C:** Correct. Choose mechanisms by how much data and time the business can lose. In this case: The recovery point and recovery time objectives state the acceptable loss and duration, which the existing backups alone do not express.
- **D:** Incorrect for this question. Scheduled backups kept for a chosen number of days. Why the correct answer wins: The recovery point and recovery time objectives state the acceptable loss and duration, which the existing backups alone do not express.

### Question 49 — B

Answer: Restore to the timestamp before the bad change. A point-in-time restore returns the instance to the moment before the deletion, which a dump or a clone of the current state would not. A point-in-time restore that discards the later writes on the same instance. Local study-map skill 2.10 (RTO, RPO, and Point-in-Time Recovery), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 2 (manage a solution that can span multiple database technologies): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A portable SQL dump taken with the engine tooling. Why the correct answer wins: A point-in-time restore returns the instance to the moment before the deletion, which a dump or a clone of the current state would not.
- **B:** Correct. A point-in-time restore that discards the later writes on the same instance. In this case: A point-in-time restore returns the instance to the moment before the deletion, which a dump or a clone of the current state would not.
- **C:** Incorrect for this question. A copy of the current data created without touching the source. Why the correct answer wins: A point-in-time restore returns the instance to the moment before the deletion, which a dump or a clone of the current state would not.
- **D:** Incorrect for this question. Trigger a switchover in a test window and observe how long writes are unavailable. Why the correct answer wins: A point-in-time restore returns the instance to the moment before the deletion, which a dump or a clone of the current state would not.

### Question 50 — A

Answer: Apply a row-level retention policy. A row-level retention rule enforces the deletion on the operational data, while a document TTL or a column-family policy applies elsewhere. Delete or expire records once the legal hold period ends. Local study-map skill 2.11 (Data Retention Management), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 2 (manage a solution that can span multiple database technologies): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Correct. Delete or expire records once the legal hold period ends. In this case: A row-level retention rule enforces the deletion on the operational data, while a document TTL or a column-family policy applies elsewhere.
- **B:** Incorrect for this question. Expire documents once their usefulness ends. Why the correct answer wins: A row-level retention rule enforces the deletion on the operational data, while a document TTL or a column-family policy applies elsewhere.
- **C:** Incorrect for this question. A rule that drops versions by age or count, which also bounds recovery. Why the correct answer wins: A row-level retention rule enforces the deletion on the operational data, while a document TTL or a column-family policy applies elsewhere.
- **D:** Incorrect for this question. Move aged, rarely read rows out of the hot table into Cloud Storage or BigQuery. Why the correct answer wins: A row-level retention rule enforces the deletion on the operational data, while a document TTL or a column-family policy applies elsewhere.

### Question 51 — A

Answer: Add a read replica for the read traffic. A read replica takes that query load off the primary, which a larger shape or sharding does not separate. Send reads to a copy so the primary keeps its capacity for writes. Local study-map skill 2.12 (Scaling Up Versus Scaling Out), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 2 (manage a solution that can span multiple database technologies): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Correct. Send reads to a copy so the primary keeps its capacity for writes. In this case: A read replica takes that query load off the primary, which a larger shape or sharding does not separate.
- **B:** Incorrect for this question. Raise provisioned compute in 1000-unit node steps or 100-unit increments. Why the correct answer wins: A read replica takes that query load off the primary, which a larger shape or sharding does not separate.
- **C:** Incorrect for this question. Split rows by a key so each instance owns a subset of the workload. Why the correct answer wins: A read replica takes that query load off the primary, which a larger shape or sharding does not separate.
- **D:** Incorrect for this question. Move the instance to a larger shape so more vCPU and memory serve the same data. Why the correct answer wins: A read replica takes that query load off the primary, which a larger shape or sharding does not separate.

### Question 52 — B

Answer: Partition the large table. Partitioning by time turns a wide delete into a partition drop, which an index or a bigger instance does not. Split one table into ranges so pruning and maintenance act on less data. Local study-map skill 2.12 (Scaling Up Versus Scaling Out), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 2 (manage a solution that can span multiple database technologies): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Create an index that turns a scan into a lookup for the predicate. Why the correct answer wins: Partitioning by time turns a wide delete into a partition drop, which an index or a bigger instance does not.
- **B:** Correct. Split one table into ranges so pruning and maintenance act on less data. In this case: Partitioning by time turns a wide delete into a partition drop, which an index or a bigger instance does not.
- **C:** Incorrect for this question. Send reads to a copy so the primary keeps its capacity for writes. Why the correct answer wins: Partitioning by time turns a wide delete into a partition drop, which an index or a bigger instance does not.
- **D:** Incorrect for this question. Move the instance to a larger shape so more vCPU and memory serve the same data. Why the correct answer wins: Partitioning by time turns a wide delete into a partition drop, which an index or a bigger instance does not.

### Question 53 — D

Answer: Stream changes with Datastream. Change data capture publishes the changes to the warehouse continuously, which periodic dumps or direct queries cannot match. Change data capture from the source into a Google Cloud target. Local study-map skill 2.13 (Replication Strategies), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 2 (manage a solution that can span multiple database technologies): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A flat-file extract for a downstream loader rather than a restore. Why the correct answer wins: Change data capture publishes the changes to the warehouse continuously, which periodic dumps or direct queries cannot match.
- **B:** Incorrect for this question. A bulk load followed by a catch-up pass for the writes made during the load. Why the correct answer wins: Change data capture publishes the changes to the warehouse continuously, which periodic dumps or direct queries cannot match.
- **C:** Incorrect for this question. Read the operational table from BigQuery without copying it first. Why the correct answer wins: Change data capture publishes the changes to the warehouse continuously, which periodic dumps or direct queries cannot match.
- **D:** Correct. Change data capture from the source into a Google Cloud target. In this case: Change data capture publishes the changes to the warehouse continuously, which periodic dumps or direct queries cannot match.

### Question 54 — D

Answer: Refresh the table statistics. Fresh statistics give the planner the real cardinality so it can choose the better plan with the index it already has. Give the planner current cardinality so it stops choosing a poor plan. Local study-map skill 2.14 (Query Optimization for Cost and Performance), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 2 (manage a solution that can span multiple database technologies): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Create an index that turns a scan into a lookup for the predicate. Why the correct answer wins: Fresh statistics give the planner the real cardinality so it can choose the better plan with the index it already has.
- **B:** Incorrect for this question. Remove write amplification from an index nothing reads. Why the correct answer wins: Fresh statistics give the planner the real cardinality so it can choose the better plan with the index it already has.
- **C:** Incorrect for this question. Give sorts and joins more working memory on the instance. Why the correct answer wins: Fresh statistics give the planner the real cardinality so it can choose the better plan with the index it already has.
- **D:** Correct. Give the planner current cardinality so it stops choosing a poor plan. In this case: Fresh statistics give the planner the real cardinality so it can choose the better plan with the index it already has.

### Question 55 — D

Answer: Run the task on a managed schedule. A managed schedule performs the recurring maintenance without an operator present. A recurring trigger that performs the work with nobody present. Local study-map skill 2.15 (Automated Maintenance and Scheduled Exports), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 2 (manage a solution that can span multiple database technologies): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Create the resource interactively with no stored definition. Why the correct answer wins: A managed schedule performs the recurring maintenance without an operator present.
- **B:** Incorrect for this question. Trigger a switchover in a test window and observe how long writes are unavailable. Why the correct answer wins: A managed schedule performs the recurring maintenance without an operator present.
- **C:** Incorrect for this question. A manual checkpoint taken immediately before a risky operation. Why the correct answer wins: A managed schedule performs the recurring maintenance without an operator present.
- **D:** Correct. A recurring trigger that performs the work with nobody present. In this case: A managed schedule performs the recurring maintenance without an operator present.

### Question 56 — C

Answer: Add a lifecycle rule to the export bucket. A lifecycle rule removes the older objects, which the export process or a schedule does not control. Move or delete aged exports so the bucket does not grow without limit. Local study-map skill 2.15 (Automated Maintenance and Scheduled Exports), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 2 (manage a solution that can span multiple database technologies): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A manual checkpoint taken immediately before a risky operation. Why the correct answer wins: A lifecycle rule removes the older objects, which the export process or a schedule does not control.
- **B:** Incorrect for this question. A recurring trigger that performs the work with nobody present. Why the correct answer wins: A lifecycle rule removes the older objects, which the export process or a schedule does not control.
- **C:** Correct. Move or delete aged exports so the bucket does not grow without limit. In this case: A lifecycle rule removes the older objects, which the export process or a schedule does not control.
- **D:** Incorrect for this question. A portable SQL dump taken with the engine tooling. Why the correct answer wins: A lifecycle rule removes the older objects, which the export process or a schedule does not control.

### Question 57 — C

Answer: Track the availability signal against the agreed objective. Comparing the availability signal with the committed objective measures the promise itself. Compare observed service levels with the commitment rather than watching raw resource metrics. Local study-map skill 2.16 (Managed Upgrades and SLA Monitoring), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 2 (manage a solution that can span multiple database technologies): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A single view of health, security, and version posture across database instances. Why the correct answer wins: Comparing the availability signal with the committed objective measures the promise itself.
- **B:** Incorrect for this question. Read the instance-level signals before attributing the symptom to the query. Why the correct answer wins: Comparing the availability signal with the committed objective measures the promise itself.
- **C:** Correct. Compare observed service levels with the commitment rather than watching raw resource metrics. In this case: Comparing the availability signal with the committed objective measures the promise itself.
- **D:** Incorrect for this question. A condition that pages a human when the threshold is crossed. Why the correct answer wins: Comparing the availability signal with the committed objective measures the promise itself.

### Question 58 — D

Answer: Use Database Migration Service for the same engine. Continuous replication with a managed migration fits the window without application work, while a bulk outage or dual writes exceed the constraint. A managed migration that moves a supported engine to the same engine on Google Cloud. Local study-map skill 3.1 (Migration Strategy and Downtime Budget), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 3 (migrate data solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A bulk load followed by a catch-up pass for the writes made during the load. Why the correct answer wins: Continuous replication with a managed migration fits the window without application work, while a bulk outage or dual writes exceed the constraint.
- **B:** Incorrect for this question. Keep two databases current from application code during the transition. Why the correct answer wins: Continuous replication with a managed migration fits the window without application work, while a bulk outage or dual writes exceed the constraint.
- **C:** Incorrect for this question. Stop the source, load everything, and start the target in one window. Why the correct answer wins: Continuous replication with a managed migration fits the window without application work, while a bulk outage or dual writes exceed the constraint.
- **D:** Correct. A managed migration that moves a supported engine to the same engine on Google Cloud. In this case: Continuous replication with a managed migration fits the window without application work, while a bulk outage or dual writes exceed the constraint.

### Question 59 — D

Answer: Accept a scheduled extended outage. A scheduled window with a stop, load, and start needs no replication topology when the business accepts the outage. Stop the source, load everything, and start the target in one window. Local study-map skill 3.1 (Migration Strategy and Downtime Budget), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 3 (migrate data solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Keep two databases current from application code during the transition. Why the correct answer wins: A scheduled window with a stop, load, and start needs no replication topology when the business accepts the outage.
- **B:** Incorrect for this question. Keep writing back to the original system so a rollback loses nothing. Why the correct answer wins: A scheduled window with a stop, load, and start needs no replication topology when the business accepts the outage.
- **C:** Incorrect for this question. A managed migration that moves a supported engine to the same engine on Google Cloud. Why the correct answer wins: A scheduled window with a stop, load, and start needs no replication topology when the business accepts the outage.
- **D:** Correct. Stop the source, load everything, and start the target in one window. In this case: A scheduled window with a stop, load, and start needs no replication topology when the business accepts the outage.

### Question 60 — C

Answer: Follow a cutover runbook with a rollback step. A rehearsed runbook naming each step, its owner, and the abort condition turns the cutover into a repeatable procedure. A rehearsed sequence with a named decision point and a way back. Local study-map skill 3.1 (Migration Strategy and Downtime Budget), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 3 (migrate data solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Stop the source, load everything, and start the target in one window. Why the correct answer wins: A rehearsed runbook naming each step, its owner, and the abort condition turns the cutover into a repeatable procedure.
- **B:** Incorrect for this question. Stop application writes so the last increment can be applied cleanly. Why the correct answer wins: A rehearsed runbook naming each step, its owner, and the abort condition turns the cutover into a repeatable procedure.
- **C:** Correct. A rehearsed sequence with a named decision point and a way back. In this case: A rehearsed runbook naming each step, its owner, and the abort condition turns the cutover into a repeatable procedure.
- **D:** Incorrect for this question. Keep two databases current from application code during the transition. Why the correct answer wins: A rehearsed runbook naming each step, its owner, and the abort condition turns the cutover into a repeatable procedure.

### Question 61 — B

Answer: Use Database Migration Service with schema conversion. The cross-engine migration path pairs conversion with managed replication, while a same-engine move or a dump leaves the conversion undone. A managed path that converts schema and code from a different source engine. Local study-map skill 3.2 (Migration Tool Selection), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 3 (migrate data solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A bulk load followed by a catch-up pass for the writes made during the load. Why the correct answer wins: The cross-engine migration path pairs conversion with managed replication, while a same-engine move or a dump leaves the conversion undone.
- **B:** Correct. A managed path that converts schema and code from a different source engine. In this case: The cross-engine migration path pairs conversion with managed replication, while a same-engine move or a dump leaves the conversion undone.
- **C:** Incorrect for this question. Change data capture from the source into a Google Cloud target. Why the correct answer wins: The cross-engine migration path pairs conversion with managed replication, while a same-engine move or a dump leaves the conversion undone.
- **D:** Incorrect for this question. A managed migration that moves a supported engine to the same engine on Google Cloud. Why the correct answer wins: The cross-engine migration path pairs conversion with managed replication, while a same-engine move or a dump leaves the conversion undone.

### Question 62 — C

Answer: Stream changes with Datastream. Change data capture feeds multiple destinations from one stream, whereas migration and dump tools move a database once. Change data capture from the source into a Google Cloud target. Local study-map skill 3.2 (Migration Tool Selection), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 3 (migrate data solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Keep two databases current from application code during the transition. Why the correct answer wins: Change data capture feeds multiple destinations from one stream, whereas migration and dump tools move a database once.
- **B:** Incorrect for this question. A bulk load followed by a catch-up pass for the writes made during the load. Why the correct answer wins: Change data capture feeds multiple destinations from one stream, whereas migration and dump tools move a database once.
- **C:** Correct. Change data capture from the source into a Google Cloud target. In this case: Change data capture feeds multiple destinations from one stream, whereas migration and dump tools move a database once.
- **D:** Incorrect for this question. A managed path that converts schema and code from a different source engine. Why the correct answer wins: Change data capture feeds multiple destinations from one stream, whereas migration and dump tools move a database once.

### Question 63 — C

Answer: Dump, restore, then replay the changes. A dump and restore uses no replication machinery, which is the simplest path when the window is acceptable. A bulk load followed by a catch-up pass for the writes made during the load. Local study-map skill 3.2 (Migration Tool Selection), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 3 (migrate data solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A managed path that converts schema and code from a different source engine. Why the correct answer wins: A dump and restore uses no replication machinery, which is the simplest path when the window is acceptable.
- **B:** Incorrect for this question. Keep two databases current from application code during the transition. Why the correct answer wins: A dump and restore uses no replication machinery, which is the simplest path when the window is acceptable.
- **C:** Correct. A bulk load followed by a catch-up pass for the writes made during the load. In this case: A dump and restore uses no replication machinery, which is the simplest path when the window is acceptable.
- **D:** Incorrect for this question. Replay the writes made during the bulk load so the target is current at the switch. Why the correct answer wins: A dump and restore uses no replication machinery, which is the simplest path when the window is acceptable.

### Question 64 — A, E

Answers: Rewrite the stored procedures and DML by hand; Reset the sequences after the bulk load. Unsupported procedural code has to be rewritten by hand, and the identity counters must be advanced past the loaded maximum. Port procedural code the conversion tool flags as unsupported. Set generated-key counters past the highest value so inserts do not collide. Local study-map skill 3.3 (Heterogeneous Schema and DDL Conversion), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 3 (migrate data solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Correct. Set generated-key counters past the highest value so inserts do not collide. In this case: Unsupported procedural code has to be rewritten by hand, and the identity counters must be advanced past the loaded maximum.
- **B:** Incorrect for this question. Convert DDL and code with reviewable, editable output before the load starts. Why the correct answer wins: Unsupported procedural code has to be rewritten by hand, and the identity counters must be advanced past the loaded maximum.
- **C:** Incorrect for this question. Prove the target holds the same rows as the source before cutover. Why the correct answer wins: Unsupported procedural code has to be rewritten by hand, and the identity counters must be advanced past the loaded maximum.
- **D:** Incorrect for this question. Move clients to the new endpoint as the final cutover action. Why the correct answer wins: Unsupported procedural code has to be rewritten by hand, and the identity counters must be advanced past the loaded maximum.
- **E:** Correct. Port procedural code the conversion tool flags as unsupported. In this case: Unsupported procedural code has to be rewritten by hand, and the identity counters must be advanced past the loaded maximum.

### Question 65 — B

Answer: Build the schema in a conversion workspace. The conversion workspace holds the generated schema and code for review, so edits are applied before the load rather than afterwards. Convert DDL and code with reviewable, editable output before the load starts. Local study-map skill 3.3 (Heterogeneous Schema and DDL Conversion), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 3 (migrate data solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Port procedural code the conversion tool flags as unsupported. Why the correct answer wins: The conversion workspace holds the generated schema and code for review, so edits are applied before the load rather than afterwards.
- **B:** Correct. Convert DDL and code with reviewable, editable output before the load starts. In this case: The conversion workspace holds the generated schema and code for review, so edits are applied before the load rather than afterwards.
- **C:** Incorrect for this question. Compare the target answers with production before the switch. Why the correct answer wins: The conversion workspace holds the generated schema and code for review, so edits are applied before the load rather than afterwards.
- **D:** Incorrect for this question. Set generated-key counters past the highest value so inserts do not collide. Why the correct answer wins: The conversion workspace holds the generated schema and code for review, so edits are applied before the load rather than afterwards.

### Question 66 — A

Answer: Rewrite the stored procedures and DML by hand. The statement has to be rewritten for the target dialect, since no data or validation step changes what the engine accepts. Port procedural code the conversion tool flags as unsupported. Local study-map skill 3.4 (DML and Application Code Conversion), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 3 (migrate data solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Correct. Port procedural code the conversion tool flags as unsupported. In this case: The statement has to be rewritten for the target dialect, since no data or validation step changes what the engine accepts.
- **B:** Incorrect for this question. Keep two databases current from application code during the transition. Why the correct answer wins: The statement has to be rewritten for the target dialect, since no data or validation step changes what the engine accepts.
- **C:** Incorrect for this question. Set generated-key counters past the highest value so inserts do not collide. Why the correct answer wins: The statement has to be rewritten for the target dialect, since no data or validation step changes what the engine accepts.
- **D:** Incorrect for this question. Compare the target answers with production before the switch. Why the correct answer wins: The statement has to be rewritten for the target dialect, since no data or validation step changes what the engine accepts.

### Question 67 — C

Answer: Replay read traffic against the target. Replaying real statements against the target exercises the actual code paths and shows where answers differ. Compare the target answers with production before the switch. Local study-map skill 3.4 (DML and Application Code Conversion), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 3 (migrate data solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Prove the target holds the same rows as the source before cutover. Why the correct answer wins: Replaying real statements against the target exercises the actual code paths and shows where answers differ.
- **B:** Incorrect for this question. Port procedural code the conversion tool flags as unsupported. Why the correct answer wins: Replaying real statements against the target exercises the actual code paths and shows where answers differ.
- **C:** Correct. Compare the target answers with production before the switch. In this case: Replaying real statements against the target exercises the actual code paths and shows where answers differ.
- **D:** Incorrect for this question. Move clients to the new endpoint as the final cutover action. Why the correct answer wins: Replaying real statements against the target exercises the actual code paths and shows where answers differ.

### Question 68 — C, D

Answers: Apply the captured change backlog before cutover; Reconcile row counts and checksums. Applying the captured backlog makes the target current, and reconciling rows and totals proves that the catch-up was complete. Replay the writes made during the bulk load so the target is current at the switch. Prove the target holds the same rows as the source before cutover. Local study-map skill 3.5 (Initial Load and Change Replication), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 3 (migrate data solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Keep two databases current from application code during the transition. Why the correct answer wins: Applying the captured backlog makes the target current, and reconciling rows and totals proves that the catch-up was complete.
- **B:** Incorrect for this question. A bulk load followed by a catch-up pass for the writes made during the load. Why the correct answer wins: Applying the captured backlog makes the target current, and reconciling rows and totals proves that the catch-up was complete.
- **C:** Correct. Replay the writes made during the bulk load so the target is current at the switch. In this case: Applying the captured backlog makes the target current, and reconciling rows and totals proves that the catch-up was complete.
- **D:** Correct. Prove the target holds the same rows as the source before cutover. In this case: Applying the captured backlog makes the target current, and reconciling rows and totals proves that the catch-up was complete.
- **E:** Incorrect for this question. Replicate row changes from the source using the engine feature itself. Why the correct answer wins: Applying the captured backlog makes the target current, and reconciling rows and totals proves that the catch-up was complete.

### Question 69 — C

Answer: Use the engine native logical replication. Replicating the source's own change stream keeps the target current throughout the load with no application change. Replicate row changes from the source using the engine feature itself. Local study-map skill 3.5 (Initial Load and Change Replication), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 3 (migrate data solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Stop the source, load everything, and start the target in one window. Why the correct answer wins: Replicating the source's own change stream keeps the target current throughout the load with no application change.
- **B:** Incorrect for this question. Keep two databases current from application code during the transition. Why the correct answer wins: Replicating the source's own change stream keeps the target current throughout the load with no application change.
- **C:** Correct. Replicate row changes from the source using the engine feature itself. In this case: Replicating the source's own change stream keeps the target current throughout the load with no application change.
- **D:** Incorrect for this question. A portable SQL dump taken with the engine tooling. Why the correct answer wins: Replicating the source's own change stream keeps the target current throughout the load with no application change.

### Question 70 — B

Answer: Reconcile row counts and checksums. A value-level comparison of the same aggregates on both systems locates a discrepancy that row counts cannot show. Prove the target holds the same rows as the source before cutover. Local study-map skill 3.6 (Validation and Reconciliation), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 3 (migrate data solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Compare the target answers with production before the switch. Why the correct answer wins: A value-level comparison of the same aggregates on both systems locates a discrepancy that row counts cannot show.
- **B:** Correct. Prove the target holds the same rows as the source before cutover. In this case: A value-level comparison of the same aggregates on both systems locates a discrepancy that row counts cannot show.
- **C:** Incorrect for this question. Set generated-key counters past the highest value so inserts do not collide. Why the correct answer wins: A value-level comparison of the same aggregates on both systems locates a discrepancy that row counts cannot show.
- **D:** Incorrect for this question. Move clients to the new endpoint as the final cutover action. Why the correct answer wins: A value-level comparison of the same aggregates on both systems locates a discrepancy that row counts cannot show.

### Question 71 — D

Answer: Replay read traffic against the target. Replaying those statements and comparing results tests behaviour, which a row-count comparison does not. Compare the target answers with production before the switch. Local study-map skill 3.6 (Validation and Reconciliation), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 3 (migrate data solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Prove the target holds the same rows as the source before cutover. Why the correct answer wins: Replaying those statements and comparing results tests behaviour, which a row-count comparison does not.
- **B:** Incorrect for this question. A rehearsed sequence with a named decision point and a way back. Why the correct answer wins: Replaying those statements and comparing results tests behaviour, which a row-count comparison does not.
- **C:** Incorrect for this question. Keep two databases current from application code during the transition. Why the correct answer wins: Replaying those statements and comparing results tests behaviour, which a row-count comparison does not.
- **D:** Correct. Compare the target answers with production before the switch. In this case: Replaying those statements and comparing results tests behaviour, which a row-count comparison does not.

### Question 72 — A, D

Answers: Follow a cutover runbook with a rollback step; Freeze writes during the cutover. The runbook fixes the order and the abort rule, and the write freeze creates the stable point the final increment needs. A rehearsed sequence with a named decision point and a way back. Stop application writes so the last increment can be applied cleanly. Local study-map skill 3.7 (Cutover and Fallback Planning), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 3 (migrate data solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Correct. Stop application writes so the last increment can be applied cleanly. In this case: The runbook fixes the order and the abort rule, and the write freeze creates the stable point the final increment needs.
- **B:** Incorrect for this question. Size the cutover from how fast changes replay, not from the data volume alone. Why the correct answer wins: The runbook fixes the order and the abort rule, and the write freeze creates the stable point the final increment needs.
- **C:** Incorrect for this question. Keep the old system read-only for a defined period, then remove it. Why the correct answer wins: The runbook fixes the order and the abort rule, and the write freeze creates the stable point the final increment needs.
- **D:** Correct. A rehearsed sequence with a named decision point and a way back. In this case: The runbook fixes the order and the abort rule, and the write freeze creates the stable point the final increment needs.
- **E:** Incorrect for this question. Move clients to the new endpoint as the final cutover action. Why the correct answer wins: The runbook fixes the order and the abort rule, and the write freeze creates the stable point the final increment needs.

### Question 73 — D

Answer: Repoint the connection string at the target. Repointing the connection string moves clients onto the validated target. Move clients to the new endpoint as the final cutover action. Local study-map skill 3.7 (Cutover and Fallback Planning), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 3 (migrate data solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Stop application writes so the last increment can be applied cleanly. Why the correct answer wins: Repointing the connection string moves clients onto the validated target.
- **B:** Incorrect for this question. Keep writing back to the original system so a rollback loses nothing. Why the correct answer wins: Repointing the connection string moves clients onto the validated target.
- **C:** Incorrect for this question. A rehearsed sequence with a named decision point and a way back. Why the correct answer wins: Repointing the connection string moves clients onto the validated target.
- **D:** Correct. Move clients to the new endpoint as the final cutover action. In this case: Repointing the connection string moves clients onto the validated target.

### Question 74 — D

Answer: Follow a cutover runbook with a rollback step. The runbook's abort condition names the rollback steps, so the team restores service on a defined path rather than improvising. A rehearsed sequence with a named decision point and a way back. Local study-map skill 3.7 (Cutover and Fallback Planning), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 3 (migrate data solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Stop application writes so the last increment can be applied cleanly. Why the correct answer wins: The runbook's abort condition names the rollback steps, so the team restores service on a defined path rather than improvising.
- **B:** Incorrect for this question. Keep two databases current from application code during the transition. Why the correct answer wins: The runbook's abort condition names the rollback steps, so the team restores service on a defined path rather than improvising.
- **C:** Incorrect for this question. Move clients to the new endpoint as the final cutover action. Why the correct answer wins: The runbook's abort condition names the rollback steps, so the team restores service on a defined path rather than improvising.
- **D:** Correct. A rehearsed sequence with a named decision point and a way back. In this case: The runbook's abort condition names the rollback steps, so the team restores service on a defined path rather than improvising.

### Question 75 — C

Answer: Set up reverse replication to the source. Replication from the target back to the source publishes those writes where the old system can read them. Keep writing back to the original system so a rollback loses nothing. Local study-map skill 3.8 (Reverse Replication to the Source), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 3 (migrate data solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Keep the old system read-only for a defined period, then remove it. Why the correct answer wins: Replication from the target back to the source publishes those writes where the old system can read them.
- **B:** Incorrect for this question. Move clients to the new endpoint as the final cutover action. Why the correct answer wins: Replication from the target back to the source publishes those writes where the old system can read them.
- **C:** Correct. Keep writing back to the original system so a rollback loses nothing. In this case: Replication from the target back to the source publishes those writes where the old system can read them.
- **D:** Incorrect for this question. Keep two databases current from application code during the transition. Why the correct answer wins: Replication from the target back to the source publishes those writes where the old system can read them.

### Question 76 — A

Answer: Decommission the source after a parallel period. A parallel period with exit criteria gives the fallback a known end and the retirement a trigger. Keep the old system read-only for a defined period, then remove it. Local study-map skill 3.8 (Reverse Replication to the Source), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 3 (migrate data solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Correct. Keep the old system read-only for a defined period, then remove it. In this case: A parallel period with exit criteria gives the fallback a known end and the retirement a trigger.
- **B:** Incorrect for this question. Check the connection and traffic evidence before retiring an instance. Why the correct answer wins: A parallel period with exit criteria gives the fallback a known end and the retirement a trigger.
- **C:** Incorrect for this question. Keep writing back to the original system so a rollback loses nothing. Why the correct answer wins: A parallel period with exit criteria gives the fallback a known end and the retirement a trigger.
- **D:** Incorrect for this question. Move clients to the new endpoint as the final cutover action. Why the correct answer wins: A parallel period with exit criteria gives the fallback a known end and the retirement a trigger.

### Question 77 — B

Answer: Use Database Migration Service with schema conversion. A managed heterogeneous migration with continuous replication limits the outage to the switch. A managed path that converts schema and code from a different source engine. Local study-map skill 3.9 (Minimizing Downtime During Migration), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 3 (migrate data solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A bulk load followed by a catch-up pass for the writes made during the load. Why the correct answer wins: A managed heterogeneous migration with continuous replication limits the outage to the switch.
- **B:** Correct. A managed path that converts schema and code from a different source engine. In this case: A managed heterogeneous migration with continuous replication limits the outage to the switch.
- **C:** Incorrect for this question. Keep two databases current from application code during the transition. Why the correct answer wins: A managed heterogeneous migration with continuous replication limits the outage to the switch.
- **D:** Incorrect for this question. Stop the source, load everything, and start the target in one window. Why the correct answer wins: A managed heterogeneous migration with continuous replication limits the outage to the switch.

### Question 78 — A

Answer: Move the job outside the contention window. Moving the cutover away from the predictable surge keeps the catch-up inside the window. Stagger the work so concurrent operations stop colliding on the same limit. Local study-map skill 3.9 (Minimizing Downtime During Migration), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 3 (migrate data solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Correct. Stagger the work so concurrent operations stop colliding on the same limit. In this case: Moving the cutover away from the predictable surge keeps the catch-up inside the window.
- **B:** Incorrect for this question. Stop the source, load everything, and start the target in one window. Why the correct answer wins: Moving the cutover away from the predictable surge keeps the catch-up inside the window.
- **C:** Incorrect for this question. Keep two databases current from application code during the transition. Why the correct answer wins: Moving the cutover away from the predictable surge keeps the catch-up inside the window.
- **D:** Incorrect for this question. Size the cutover from how fast changes replay, not from the data volume alone. Why the correct answer wins: Moving the cutover away from the predictable surge keeps the catch-up inside the window.

### Question 79 — B, E

Answers: Decommission the source after a parallel period; Confirm no client still uses the old endpoint. A defined end to the parallel period releases the system, and confirming that nothing still connects prevents an outage after removal. Keep the old system read-only for a defined period, then remove it. Check the connection and traffic evidence before retiring an instance. Local study-map skill 3.10 (Source Decommissioning), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 3 (migrate data solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Keep writing back to the original system so a rollback loses nothing. Why the correct answer wins: A defined end to the parallel period releases the system, and confirming that nothing still connects prevents an outage after removal.
- **B:** Correct. Keep the old system read-only for a defined period, then remove it. In this case: A defined end to the parallel period releases the system, and confirming that nothing still connects prevents an outage after removal.
- **C:** Incorrect for this question. Keep two databases current from application code during the transition. Why the correct answer wins: A defined end to the parallel period releases the system, and confirming that nothing still connects prevents an outage after removal.
- **D:** Incorrect for this question. Move clients to the new endpoint as the final cutover action. Why the correct answer wins: A defined end to the parallel period releases the system, and confirming that nothing still connects prevents an outage after removal.
- **E:** Correct. Check the connection and traffic evidence before retiring an instance. In this case: A defined end to the parallel period releases the system, and confirming that nothing still connects prevents an outage after removal.

### Question 80 — C

Answer: Export the table into BigQuery. Copying the history into the warehouse keeps it queryable once the engine is gone. Copy the analytical slice into the warehouse on a schedule. Local study-map skill 3.10 (Source Decommissioning), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 3 (migrate data solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Interconnect the remaining on-premises system rather than moving it. Why the correct answer wins: Copying the history into the warehouse keeps it queryable once the engine is gone.
- **B:** Incorrect for this question. Keep the old system read-only for a defined period, then remove it. Why the correct answer wins: Copying the history into the warehouse keeps it queryable once the engine is gone.
- **C:** Correct. Copy the analytical slice into the warehouse on a schedule. In this case: Copying the history into the warehouse keeps it queryable once the engine is gone.
- **D:** Incorrect for this question. Keep writing back to the original system so a rollback loses nothing. Why the correct answer wins: Copying the history into the warehouse keeps it queryable once the engine is gone.

### Question 81 — C, D

Answers: Provision the instance with a Terraform module; Test the upgrade on a clone first. The module creates the environment from one reviewed definition, and a clone lets the team prove the configuration before real traffic. Declare the database so the same definition creates every environment. Rehearse the change against a copy before touching production. Local study-map skill 4.1 (Provisioning Highly Available Instances), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 4 (deploy scalable and highly available databases in Google Cloud): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A recovery point that makes the upgrade reversible in practice. Why the correct answer wins: The module creates the environment from one reviewed definition, and a clone lets the team prove the configuration before real traffic.
- **B:** Incorrect for this question. Run the new version beside the old one and move traffic when it is proven. Why the correct answer wins: The module creates the environment from one reviewed definition, and a clone lets the team prove the configuration before real traffic.
- **C:** Correct. Declare the database so the same definition creates every environment. In this case: The module creates the environment from one reviewed definition, and a clone lets the team prove the configuration before real traffic.
- **D:** Correct. Rehearse the change against a copy before touching production. In this case: The module creates the environment from one reviewed definition, and a clone lets the team prove the configuration before real traffic.
- **E:** Incorrect for this question. Create the resource interactively with no stored definition. Why the correct answer wins: The module creates the environment from one reviewed definition, and a clone lets the team prove the configuration before real traffic.

### Question 82 — C

Answer: Apply the change through the infrastructure pipeline. Applying changes through the pipeline records the review and the change together, which manual edits cannot show. Send database changes through review and version control like any other code. Local study-map skill 4.1 (Provisioning Highly Available Instances), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 4 (deploy scalable and highly available databases in Google Cloud): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A single view of health, security, and version posture across database instances. Why the correct answer wins: Applying changes through the pipeline records the review and the change together, which manual edits cannot show.
- **B:** Incorrect for this question. Create the resource interactively with no stored definition. Why the correct answer wins: Applying changes through the pipeline records the review and the change together, which manual edits cannot show.
- **C:** Correct. Send database changes through review and version control like any other code. In this case: Applying changes through the pipeline records the review and the change together, which manual edits cannot show.
- **D:** Incorrect for this question. Rehearse the change against a copy before touching production. Why the correct answer wins: Applying changes through the pipeline records the review and the change together, which manual edits cannot show.

### Question 83 — A

Answer: Provision the instance with a Terraform module. A single declared module reproduces the estate exactly, whereas manual creation would introduce drift under pressure. Declare the database so the same definition creates every environment. Local study-map skill 4.1 (Provisioning Highly Available Instances), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 4 (deploy scalable and highly available databases in Google Cloud): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Correct. Declare the database so the same definition creates every environment. In this case: A single declared module reproduces the estate exactly, whereas manual creation would introduce drift under pressure.
- **B:** Incorrect for this question. A recovery point that makes the upgrade reversible in practice. Why the correct answer wins: A single declared module reproduces the estate exactly, whereas manual creation would introduce drift under pressure.
- **C:** Incorrect for this question. Run the new version beside the old one and move traffic when it is proven. Why the correct answer wins: A single declared module reproduces the estate exactly, whereas manual creation would introduce drift under pressure.
- **D:** Incorrect for this question. Create the resource interactively with no stored definition. Why the correct answer wins: A single declared module reproduces the estate exactly, whereas manual creation would introduce drift under pressure.

### Question 84 — C

Answer: Run a controlled failover test. A controlled failover removes the active zone and observes the takeover. Trigger a switchover in a test window and observe how long writes are unavailable. Local study-map skill 4.2 (Testing High Availability and Disaster Recovery), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 4 (deploy scalable and highly available databases in Google Cloud): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A liveness signal that fires before users report the outage. Why the correct answer wins: A controlled failover removes the active zone and observes the takeover.
- **B:** Incorrect for this question. Compare the signal after cutover against the pre-change baseline. Why the correct answer wins: A controlled failover removes the active zone and observes the takeover.
- **C:** Correct. Trigger a switchover in a test window and observe how long writes are unavailable. In this case: A controlled failover removes the active zone and observes the takeover.
- **D:** Incorrect for this question. A recovery point that makes the upgrade reversible in practice. Why the correct answer wins: A controlled failover removes the active zone and observes the takeover.

### Question 85 — D

Answer: Rehearse the promotion in a test project. Promoting the cross-region copy is the only rehearsed path that proves a regional recovery. Practise the failover that the runbook would perform for real. Local study-map skill 4.2 (Testing High Availability and Disaster Recovery), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 4 (deploy scalable and highly available databases in Google Cloud): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A recovery point that makes the upgrade reversible in practice. Why the correct answer wins: Promoting the cross-region copy is the only rehearsed path that proves a regional recovery.
- **B:** Incorrect for this question. Trigger a switchover in a test window and observe how long writes are unavailable. Why the correct answer wins: Promoting the cross-region copy is the only rehearsed path that proves a regional recovery.
- **C:** Incorrect for this question. Give the standby enough capacity to carry production alone. Why the correct answer wins: Promoting the cross-region copy is the only rehearsed path that proves a regional recovery.
- **D:** Correct. Practise the failover that the runbook would perform for real. In this case: Promoting the cross-region copy is the only rehearsed path that proves a regional recovery.

### Question 86 — A

Answer: Restore the backup into the second region. Restoring the backup in the second region tests the rebuild path that a replica promotion would skip. Rebuild the database in the surviving region from the latest backup. Local study-map skill 4.2 (Testing High Availability and Disaster Recovery), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 4 (deploy scalable and highly available databases in Google Cloud): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Correct. Rebuild the database in the surviving region from the latest backup. In this case: Restoring the backup in the second region tests the rebuild path that a replica promotion would skip.
- **B:** Incorrect for this question. Practise the failover that the runbook would perform for real. Why the correct answer wins: Restoring the backup in the second region tests the rebuild path that a replica promotion would skip.
- **C:** Incorrect for this question. A recovery point that makes the upgrade reversible in practice. Why the correct answer wins: Restoring the backup in the second region tests the rebuild path that a replica promotion would skip.
- **D:** Incorrect for this question. Trigger a switchover in a test window and observe how long writes are unavailable. Why the correct answer wins: Restoring the backup in the second region tests the rebuild path that a replica promotion would skip.

### Question 87 — B

Answer: Choose a multi-region instance configuration. A multi-region configuration keeps quorum across regions, so one lost region does not stop writes. A topology that places replicas in separate regions for regional-failure tolerance. Local study-map skill 4.3 (Multi-Regional Replication Setup), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 4 (deploy scalable and highly available databases in Google Cloud): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A copy in a second region that serves reads and can be promoted. Why the correct answer wins: A multi-region configuration keeps quorum across regions, so one lost region does not stop writes.
- **B:** Correct. A topology that places replicas in separate regions for regional-failure tolerance. In this case: A multi-region configuration keeps quorum across regions, so one lost region does not stop writes.
- **C:** Incorrect for this question. A primary and standby in two zones of one region with automatic failover. Why the correct answer wins: A multi-region configuration keeps quorum across regions, so one lost region does not stop writes.
- **D:** Incorrect for this question. Rebuild the database in the surviving region from the latest backup. Why the correct answer wins: A multi-region configuration keeps quorum across regions, so one lost region does not stop writes.

### Question 88 — C

Answer: Add a secondary cluster in the second region. A secondary cluster serves reads and can be promoted. An AlloyDB cross-region copy that can be promoted to a primary cluster. Local study-map skill 4.3 (Multi-Regional Replication Setup), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 4 (deploy scalable and highly available databases in Google Cloud): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Rebuild the database in the surviving region from the latest backup. Why the correct answer wins: A secondary cluster serves reads and can be promoted.
- **B:** Incorrect for this question. Grow the AlloyDB read pool that serves read-only connections. Why the correct answer wins: A secondary cluster serves reads and can be promoted.
- **C:** Correct. An AlloyDB cross-region copy that can be promoted to a primary cluster. In this case: A secondary cluster serves reads and can be promoted.
- **D:** Incorrect for this question. One instance in one zone with no standby, so a zone failure stops writes. Why the correct answer wins: A secondary cluster serves reads and can be promoted.

### Question 89 — B

Answer: Route the app profile across both clusters. Multi-cluster routing moves traffic to the surviving cluster automatically. A Bigtable app profile that fails over between clusters without a client change. Local study-map skill 4.3 (Multi-Regional Replication Setup), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 4 (deploy scalable and highly available databases in Google Cloud): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A copy in a second region that serves reads and can be promoted. Why the correct answer wins: Multi-cluster routing moves traffic to the surviving cluster automatically.
- **B:** Correct. A Bigtable app profile that fails over between clusters without a client change. In this case: Multi-cluster routing moves traffic to the surviving cluster automatically.
- **C:** Incorrect for this question. An AlloyDB cross-region copy that can be promoted to a primary cluster. Why the correct answer wins: Multi-cluster routing moves traffic to the surviving cluster automatically.
- **D:** Incorrect for this question. A Bigtable app profile that keeps a workload on one cluster for predictable latency. Why the correct answer wins: Multi-cluster routing moves traffic to the surviving cluster automatically.

### Question 90 — A, D

Answers: Add a read replica for the read traffic; Send reporting queries to the read replica. Adding a replica provides the read capacity, and directing reads to it moves the load off the primary. Send reads to a copy so the primary keeps its capacity for writes. Separate analytical reads from the write path. Local study-map skill 4.4 (Read Replicas and Read Pools), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 4 (deploy scalable and highly available databases in Google Cloud): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Correct. Separate analytical reads from the write path. In this case: Adding a replica provides the read capacity, and directing reads to it moves the load off the primary.
- **B:** Incorrect for this question. Move the instance to a larger shape so more vCPU and memory serve the same data. Why the correct answer wins: Adding a replica provides the read capacity, and directing reads to it moves the load off the primary.
- **C:** Incorrect for this question. Split one table into ranges so pruning and maintenance act on less data. Why the correct answer wins: Adding a replica provides the read capacity, and directing reads to it moves the load off the primary.
- **D:** Correct. Send reads to a copy so the primary keeps its capacity for writes. In this case: Adding a replica provides the read capacity, and directing reads to it moves the load off the primary.
- **E:** Incorrect for this question. A pooler that multiplexes many application connections onto few database sessions. Why the correct answer wins: Adding a replica provides the read capacity, and directing reads to it moves the load off the primary.

### Question 91 — A

Answer: Send reporting queries to the read replica. Moving those sessions to the idle pool uses capacity that already exists, where growing either tier adds cost the workload does not need. Separate analytical reads from the write path. Local study-map skill 4.4 (Read Replicas and Read Pools), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 4 (deploy scalable and highly available databases in Google Cloud): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Correct. Separate analytical reads from the write path. In this case: Moving those sessions to the idle pool uses capacity that already exists, where growing either tier adds cost the workload does not need.
- **B:** Incorrect for this question. Move the instance to a larger shape so more vCPU and memory serve the same data. Why the correct answer wins: Moving those sessions to the idle pool uses capacity that already exists, where growing either tier adds cost the workload does not need.
- **C:** Incorrect for this question. Absorb repeated reads in memory so the database sees fewer of them. Why the correct answer wins: Moving those sessions to the idle pool uses capacity that already exists, where growing either tier adds cost the workload does not need.
- **D:** Incorrect for this question. Grow the AlloyDB read pool that serves read-only connections. Why the correct answer wins: Moving those sessions to the idle pool uses capacity that already exists, where growing either tier adds cost the workload does not need.

### Question 92 — B

Answer: Apply the change through the infrastructure pipeline. Validation inside the pipeline refuses the change before it reaches the database. Send database changes through review and version control like any other code. Local study-map skill 4.5 (Automating Database Provisioning), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 4 (deploy scalable and highly available databases in Google Cloud): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A copy of the current data created without touching the source. Why the correct answer wins: Validation inside the pipeline refuses the change before it reaches the database.
- **B:** Correct. Send database changes through review and version control like any other code. In this case: Validation inside the pipeline refuses the change before it reaches the database.
- **C:** Incorrect for this question. A recovery point that makes the upgrade reversible in practice. Why the correct answer wins: Validation inside the pipeline refuses the change before it reaches the database.
- **D:** Incorrect for this question. Create the resource interactively with no stored definition. Why the correct answer wins: Validation inside the pipeline refuses the change before it reaches the database.

### Question 93 — B

Answer: Provision the instance with a Terraform module. A parameterised module produces each cluster from one definition. Declare the database so the same definition creates every environment. Local study-map skill 4.5 (Automating Database Provisioning), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 4 (deploy scalable and highly available databases in Google Cloud): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A single view of health, security, and version posture across database instances. Why the correct answer wins: A parameterised module produces each cluster from one definition.
- **B:** Correct. Declare the database so the same definition creates every environment. In this case: A parameterised module produces each cluster from one definition.
- **C:** Incorrect for this question. Rehearse the change against a copy before touching production. Why the correct answer wins: A parameterised module produces each cluster from one definition.
- **D:** Incorrect for this question. Create the resource interactively with no stored definition. Why the correct answer wins: A parameterised module produces each cluster from one definition.

### Question 94 — D

Answer: Create an alerting policy on the metric. An alerting policy on the failover signal notifies the team without anyone watching a dashboard. A condition that pages a human when the threshold is crossed. Local study-map skill 4.6 (Monitoring Highly Available Databases), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 4 (deploy scalable and highly available databases in Google Cloud): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A per-query view of latency, load, and wait events on the instance. Why the correct answer wins: An alerting policy on the failover signal notifies the team without anyone watching a dashboard.
- **B:** Incorrect for this question. Read the instance-level signals before attributing the symptom to the query. Why the correct answer wins: An alerting policy on the failover signal notifies the team without anyone watching a dashboard.
- **C:** Incorrect for this question. A single view of health, security, and version posture across database instances. Why the correct answer wins: An alerting policy on the failover signal notifies the team without anyone watching a dashboard.
- **D:** Correct. A condition that pages a human when the threshold is crossed. In this case: An alerting policy on the failover signal notifies the team without anyone watching a dashboard.

### Question 95 — A

Answer: Alert when the instance is unreachable. A probe that executes a query detects the failure the resource view misses. A liveness signal that fires before users report the outage. Local study-map skill 4.6 (Monitoring Highly Available Databases), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 4 (deploy scalable and highly available databases in Google Cloud): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Correct. A liveness signal that fires before users report the outage. In this case: A probe that executes a query detects the failure the resource view misses.
- **B:** Incorrect for this question. The engine log of statements that exceeded the long-query threshold. Why the correct answer wins: A probe that executes a query detects the failure the resource view misses.
- **C:** Incorrect for this question. Read the instance-level signals before attributing the symptom to the query. Why the correct answer wins: A probe that executes a query detects the failure the resource view misses.
- **D:** Incorrect for this question. A per-query view of latency, load, and wait events on the instance. Why the correct answer wins: A probe that executes a query detects the failure the resource view misses.

### Question 96 — A

Answer: Promote the cross-region replica during the outage. Promoting the current copy keeps every acknowledged write and restores service in minutes rather than through a rebuild. Turn the replica into an independent primary so the application can resume writes. Local study-map skill 4.7 (Regional Failover Mechanics), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 4 (deploy scalable and highly available databases in Google Cloud): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Correct. Turn the replica into an independent primary so the application can resume writes. In this case: Promoting the current copy keeps every acknowledged write and restores service in minutes rather than through a rebuild.
- **B:** Incorrect for this question. Rebuild the database in the surviving region from the latest backup. Why the correct answer wins: Promoting the current copy keeps every acknowledged write and restores service in minutes rather than through a rebuild.
- **C:** Incorrect for this question. A point-in-time restore that discards the later writes on the same instance. Why the correct answer wins: Promoting the current copy keeps every acknowledged write and restores service in minutes rather than through a rebuild.
- **D:** Incorrect for this question. Trigger a switchover in a test window and observe how long writes are unavailable. Why the correct answer wins: Promoting the current copy keeps every acknowledged write and restores service in minutes rather than through a rebuild.

### Question 97 — D

Answer: Fence the old primary before promotion. The former primary has to be stopped from accepting writes so only one primary exists. Stop the former primary from accepting writes so two instances cannot both claim the role. Local study-map skill 4.7 (Regional Failover Mechanics), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 4 (deploy scalable and highly available databases in Google Cloud): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Stop application writes so the last increment can be applied cleanly. Why the correct answer wins: The former primary has to be stopped from accepting writes so only one primary exists.
- **B:** Incorrect for this question. Keep writing back to the original system so a rollback loses nothing. Why the correct answer wins: The former primary has to be stopped from accepting writes so only one primary exists.
- **C:** Incorrect for this question. A rehearsed sequence with a named decision point and a way back. Why the correct answer wins: The former primary has to be stopped from accepting writes so only one primary exists.
- **D:** Correct. Stop the former primary from accepting writes so two instances cannot both claim the role. In this case: The former primary has to be stopped from accepting writes so only one primary exists.

### Question 98 — B

Answer: Use the language connector with IAM credentials. The language connector resolves the instance on each connection, so clients follow the current primary. A client library that resolves the instance and authorizes the connection with IAM. Local study-map skill 4.8 (Connection Routing and Load Balancing), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 4 (deploy scalable and highly available databases in Google Cloud): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A public-IP allowlist that admits the caller range. Why the correct answer wins: The language connector resolves the instance on each connection, so clients follow the current primary.
- **B:** Correct. A client library that resolves the instance and authorizes the connection with IAM. In this case: The language connector resolves the instance on each connection, so clients follow the current primary.
- **C:** Incorrect for this question. Move clients to the new endpoint as the final cutover action. Why the correct answer wins: The language connector resolves the instance on each connection, so clients follow the current primary.
- **D:** Incorrect for this question. A pooler that multiplexes many application connections onto few database sessions. Why the correct answer wins: The language connector resolves the instance on each connection, so clients follow the current primary.

### Question 99 — B

Answer: Reserve headroom above the measured peak. The standby must carry the peak plus the load it inherits, so headroom above that peak is the basis. Keep spare capacity so a failover or a traffic spike does not saturate the instance. Local study-map skill 4.9 (Failover Capacity Headroom), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 4 (deploy scalable and highly available databases in Google Cloud): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Match capacity to the daily traffic shape. Why the correct answer wins: The standby must carry the peak plus the load it inherits, so headroom above that peak is the basis.
- **B:** Correct. Keep spare capacity so a failover or a traffic spike does not saturate the instance. In this case: The standby must carry the peak plus the load it inherits, so headroom above that peak is the basis.
- **C:** Incorrect for this question. Send reads to a copy so the primary keeps its capacity for writes. Why the correct answer wins: The standby must carry the peak plus the load it inherits, so headroom above that peak is the basis.
- **D:** Incorrect for this question. Shrink an instance whose peak fits a smaller shape. Why the correct answer wins: The standby must carry the peak plus the load it inherits, so headroom above that peak is the basis.

### Question 100 — C

Answer: Pre-size the promoted replica for the full load. The standby must be sized in advance for the load it will inherit. Give the standby enough capacity to carry production alone. Local study-map skill 4.9 (Failover Capacity Headroom), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 4 (deploy scalable and highly available databases in Google Cloud): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Keep spare capacity so a failover or a traffic spike does not saturate the instance. Why the correct answer wins: The standby must be sized in advance for the load it will inherit.
- **B:** Incorrect for this question. Match capacity to the daily traffic shape. Why the correct answer wins: The standby must be sized in advance for the load it will inherit.
- **C:** Correct. Give the standby enough capacity to carry production alone. In this case: The standby must be sized in advance for the load it will inherit.
- **D:** Incorrect for this question. Send reads to a copy so the primary keeps its capacity for writes. Why the correct answer wins: The standby must be sized in advance for the load it will inherit.
