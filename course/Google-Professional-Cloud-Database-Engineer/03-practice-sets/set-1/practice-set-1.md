# Google Cloud Professional Cloud Database Engineer — Full-Length Mock Exam 1

Professional Cloud Database Engineer · 100 questions · expanded practice bank · passing score not published

Blueprint-weighted mock exam. Item mix: 84 multiple-choice and 16 multiple-select items (the selection count is stated in each multi-select stem). The live exam publishes 50-60 multiple-choice and multiple-select questions and has no case-study component, so this set is larger on purpose and no case-study item is reproduced. The live paper allows two hours for 50-60 items, so this 100-item set is a slower-per-item rehearsal: about 72 seconds per item here against roughly 120-144 seconds live. Use it to build a habit of finishing with time to review. See the README for the exact fidelity boundary.

Original educational content, not actual, recalled, or copied Google exam items.

## Questions

---

## Domain 1 — Design Innovative, Scalable, and Highly Available Cloud Database Solutions (Sizing, Availability Design, and Database Selection)

### 1. A payments team must pick a Cloud SQL for PostgreSQL shape for a new ledger service and holds three weeks of peak CPU, memory, and disk throughput from a pilot on comparable hardware. Which action should come first?

- A. Add a read replica for the read traffic
- B. Commit to the steady baseline capacity
- C. Size the instance from the observed peak metrics
- D. Let the disk grow automatically

### 2. A ticketing platform's Cloud SQL primary sits at 55 percent CPU on a normal day, and the team knows the on-sale weekend triples write volume. What should the chosen shape account for?

- A. Send reporting queries to the read replica
- B. Stop or delete the idle instance
- C. Reduce the machine type to match observed use
- D. Reserve headroom above the measured peak

### 3. An AlloyDB analytics job scans two terabytes nightly, and profiling shows seventy percent of query time waiting on random reads rather than on compute or locking. Which change addresses the measured bottleneck?

- A. Add a read replica for the read traffic
- B. Partition the large table
- C. Move the data to SSD storage
- D. Increase the machine type of the instance

### 4. A Bigtable cluster stores forty terabytes of clickstream events read once a day in large sequential ranges, and the team has no latency requirement for those scans. Which storage choice keeps the cost lowest?

- A. Add nodes to the Bigtable cluster
- B. Move the data to HDD storage
- C. Set the garbage-collection policy on the column family
- D. Move the data to SSD storage

### 5. A Cloud SQL for SQL Server instance is memory-bound: the buffer pool hit ratio collapses during month-end reporting while CPU stays under forty percent. Which change adds the resource that is actually short?

- A. Increase the disk size to raise throughput
- B. Increase the machine type of the instance
- C. Add a read replica for the read traffic
- D. Add the index the slow query needs

### 6. A Cloud SQL for PostgreSQL instance on a latency-sensitive checkout path runs short of IOPS at peak, and the platform team cannot change the machine type this quarter. Which change raises throughput within that limit?

- A. Move the data to HDD storage
- B. Add processing units to the Spanner instance
- C. Add nodes to the read pool
- D. Increase the disk size to raise throughput

### 7. A European bank needs its Cloud SQL for PostgreSQL ledger to survive the loss of a whole region and to accept writes again within an hour. Select two.

- A. Add a cross-region read replica
- B. Promote the cross-region replica during the outage
- C. Enable regional high availability with a standby zone
- D. Place the replica in the same region as the primary
- E. Set a deny maintenance period over the peak event

### 8. A team running Cloud SQL for MySQL in a single zone wants automatic recovery from a zone failure with no application change, and it has no cross-region requirement. Which choice fits?

- A. Restore the backup into the second region
- B. Add a cross-region read replica
- C. Choose a multi-region instance configuration
- D. Enable regional high availability with a standby zone

### 9. An AlloyDB deployment must tolerate a regional outage with a promotion path, and the team also wants reads served in the second region before any failover happens. Which topology provides both?

- A. Restore the backup into the second region
- B. Add nodes to the read pool
- C. Add a secondary cluster in the second region
- D. Enable regional high availability with a standby zone

### 10. A retailer's Cloud SQL for PostgreSQL cannot be interrupted during a two-week peak trading period, and patching must still complete that quarter. What should the team configure?

- A. Set a deny maintenance period over the peak event
- B. Restart the instance in the window
- C. Perform an in-place major version upgrade
- D. Schedule the maintenance window in the low-traffic period

### 11. A SaaS provider accepts a short restart, but only between 02:00 and 04:00 on Sunday, and patching currently arrives mid-afternoon. What should change?

- A. Schedule the maintenance window in the low-traffic period
- B. Take a backup before the upgrade
- C. Set a deny maintenance period over the peak event
- D. Run a controlled failover test

### 12. A security review requires that application pods reach a Cloud SQL for PostgreSQL instance with no public address and no distributed database password, and that access be revocable through identity. Select two.

- A. Connect over private IP inside the VPC
- B. Use the public IP with enforced SSL
- C. Add the client range to authorized networks
- D. Keep a database password in the connection string
- E. Enable IAM database authentication

### 13. Clients in a partner VPC must reach a Cloud SQL instance without VPC peering, and the partner refuses any route exchange between the networks. Which connectivity option works?

- A. Add the client range to authorized networks
- B. Connect over private IP inside the VPC
- C. Place the instance in a Shared VPC service project
- D. Publish the instance behind Private Service Connect

### 14. A regulator requires that the bank hold the keys protecting its Spanner database and be able to revoke access by disabling a key version. Which control satisfies that requirement?

- A. Enable Data Access audit logs
- B. Rely on Google-managed encryption keys
- C. Encrypt with a customer-managed key in Cloud KMS
- D. Add the projects to a VPC Service Controls perimeter

### 15. A team runs Cloud SQL with CMEK, and a quarterly control requires that a new key version protect new writes while previously encrypted backups stay readable. Which practice meets the control?

- A. Rely on Google-managed encryption keys
- B. Enable Data Access audit logs
- C. Extend the backup retention window
- D. Rotate the customer-managed key on a schedule

### 16. A Cloud SQL for PostgreSQL instance refuses connections at three hundred application pods, each holding an idle session between requests, while CPU stays under thirty percent. Which change fixes the exhaustion?

- A. Raise the max_connections database flag
- B. Increase the machine tier to allow more connections
- C. Put a session pooler in front of the instance
- D. Increase the machine type of the instance

### 17. An application opens a database connection per request and never closes it, so the session count climbs until new connections are refused while the pool reports no idle sessions. What should be fixed first?

- A. Add a read replica for the read traffic
- B. Put a session pooler in front of the instance
- C. Raise the max_connections database flag
- D. Fix the connection leak in the application

### 18. An audit finding requires that every read of patient records in Cloud SQL be attributable to a person, and that the evidence survive deletion of the project's default log bucket. Select two.

- A. Route the audit logs to a locked log bucket
- B. Build a log-based metric from the error entries
- C. Review the fleet in Database Center
- D. Enable Data Access audit logs
- E. Rely on Admin Activity audit logs

### 19. A team believes reads of a Firestore collection are already audited because the project shows audit entries for database changes. Which gap should they close?

- A. Rely on Admin Activity audit logs
- B. Set a time-to-live policy on the collection
- C. Enable Data Access audit logs
- D. Schedule a Firestore export

### 20. A workload runs an engine that Google does not offer as a managed service, and the licence permits only dedicated hardware with no hypervisor underneath. Which deployment fits?

- A. Use Cloud SQL for the relational workload
- B. Run the database on bare metal solution
- C. Use a partner-managed database offering
- D. Run the database on Compute Engine yourself

### 21. A startup needs the lowest operational burden for a twenty-gigabyte relational workload with nightly batch jobs and no dedicated database administrator. Which choice fits best?

- A. Run the database on bare metal solution
- B. Use Spanner for the globally distributed relational workload
- C. Run the database on Compute Engine yourself
- D. Use Cloud SQL for the relational workload

### 22. A mobile application needs offline document sync and automatic multi-region replication, and the analytics team also needs to query the same data without touching the operational store. Select two.

- A. Export the table into BigQuery
- B. Use Memorystore as the caching tier
- C. Use Firestore for the document workload
- D. Use Bigtable for the high-throughput wide-column workload
- E. Use Cloud SQL for the relational workload

### 23. An IoT platform writes three hundred thousand readings per second keyed by device and timestamp and reads the last hour per device, with cost per write as the deciding constraint. Which database fits?

- A. Use Bigtable for the high-throughput wide-column workload
- B. Use Cloud SQL for the relational workload
- C. Use AlloyDB for the demanding relational workload
- D. Use Spanner for the globally distributed relational workload

### 24. A financial ledger needs serializable transactions across accounts, strong consistency on two continents, and no application-level sharding. Which database meets all three?

- A. Use Spanner for the globally distributed relational workload
- B. Use Bigtable for the high-throughput wide-column workload
- C. Use Cloud SQL for the relational workload
- D. Use Firestore for the document workload

### 25. A support assistant must return the ten nearest documentation embeddings for each question, and the corpus already sits in Cloud SQL for PostgreSQL beside relational metadata that filters the search. Which approach keeps the filter and the search together?

- A. Use Memorystore as the caching tier
- B. Add the composite index for the query
- C. Enable the vector extension on PostgreSQL
- D. Query the source through BigQuery federated queries

### 26. A product team needs semantic search over two hundred million embeddings on AlloyDB with sub-100 millisecond p99 latency and expects the index to grow weekly. Which choice fits?

- A. Enable the vector extension on PostgreSQL
- B. Use AlloyDB vector search with a ScaNN index
- C. Cache the hot read path in Memorystore
- D. Add the composite index for the query

### 27. An estate holds one Cloud SQL instance with no connections for thirty days and another whose shape is four times its observed peak. Select two actions that cut spend without changing behaviour. Select two.

- A. Reduce the machine type to match observed use
- B. Commit to the steady baseline capacity
- C. Rely on sustained-use discounts
- D. Let the disk grow automatically
- E. Stop or delete the idle instance

### 28. A bank runs a Spanner workload on a stable baseline of forty nodes that never drops, and finance wants the lowest unit price for that always-on capacity. Which action fits?

- A. Scale down outside business hours
- B. Rely on sustained-use discounts
- C. Commit to the steady baseline capacity
- D. Stop or delete the idle instance

### 29. A team is deciding whether an application can change engines; the code uses an ORM but also forty hand-written stored procedures built on vendor-specific syntax. Which decision removes the largest dependency risk?

- A. Keep the current engine and version
- B. Rewrite the stored procedures and DML by hand
- C. Use Database Migration Service with schema conversion
- D. Choose the target engine with the cheapest conversion

### 30. A hospital must keep its Cloud SQL for PostgreSQL data inside Germany even if another team later creates a project in the same organization. Select two.

- A. Enforce the location with an organization policy
- B. Place the instance in the required region
- C. Cache the hot read path in Memorystore
- D. Rely on Google-managed encryption keys
- E. Choose a multi-region instance configuration

### 31. A retail group forbids database data leaving its approved projects, and analysts want to read a Bigtable table from BigQuery without moving the rows anywhere unapproved. Which control enforces that boundary?

- A. Query the source through BigQuery federated queries
- B. Export the table into BigQuery
- C. Add the projects to a VPC Service Controls perimeter
- D. Stream changes into BigQuery

### 32. The finance team needs a nightly join of three tables held in an on-premises Oracle database with BigQuery history, and copying the Oracle tables is not permitted. Which approach fits?

- A. Query the source through BigQuery federated queries
- B. Keep part of the estate on-premises with a hybrid link
- C. Stream changes into BigQuery
- D. Export the table into BigQuery

---

## Domain 2 — Manage a Solution That Can Span Multiple Database Technologies (Operations, Access, Backup, and Performance)

### 33. A team must give an application read-only access to one Cloud SQL for PostgreSQL schema and keep that access independent of any individual employee leaving. Select two.

- A. Bind access to a Google group
- B. Create one database user per person
- C. Limit the user to the required schema
- D. Share one application database user
- E. Grant the basic editor role

### 34. A review finds the application's service account holds the Cloud SQL administrator role so that it can connect, which would also let it delete the instance. Which change removes the excess?

- A. Grant a custom role limited to the needed permissions
- B. Share one application database user
- C. Grant the predefined database role
- D. Grant the basic editor role

### 35. Three analytics engineers share one database login today, and audit now requires each read to be attributable to a named person. What should change?

- A. Have the application authenticate as a service account
- B. Keep a database password in the connection string
- C. Create one database user per person
- D. Share one application database user

### 36. A Cloud SQL for PostgreSQL report takes forty seconds; Query Insights shows a sequential scan of four million rows to return twelve, filtered on a highly selective column. What should the team do?

- A. Add the index the slow query needs
- B. Cache the hot read path in Memorystore
- C. Refresh the table statistics
- D. Partition the large table

### 37. A query plan changes every morning after the overnight load: the planner estimates fifty rows, but the join actually returns nine hundred thousand. Which action addresses the cause?

- A. Drop the unused index
- B. Refresh the table statistics
- C. Add the index the slow query needs
- D. Raise the per-operation memory flag

### 38. A nightly batch updates every row of a large table inside one transaction and holds locks for eleven minutes while other sessions queue behind it. Which change removes the contention?

- A. Put a session pooler in front of the instance
- B. Batch the writes into fewer round trips
- C. Terminate the session that holds the lock
- D. Add a read replica for the read traffic

### 39. One session has held an exclusive lock for twenty minutes and every other write queues behind it; the session shows as idle in transaction with no statement running. What should the team do first?

- A. Refresh the table statistics
- B. Terminate the session that holds the lock
- C. Batch the writes into fewer round trips
- D. Add the index the slow query needs

### 40. A database slows down at 09:00 every weekday and the team must explain why. Which two sources should the team correlate? Select two.

- A. Review the fleet in Database Center
- B. Ask Gemini in databases to explain the plan
- C. Use Query Insights to find the heavy statements
- D. Watch CPU, memory, disk, and IOPS together
- E. Route the audit logs to a locked log bucket

### 41. An operator needs one view of CPU, memory, disk, and IOPS for a Cloud SQL instance during an incident. Which view fits?

- A. Review the fleet in Database Center
- B. Watch CPU, memory, disk, and IOPS together
- C. Use Query Insights to find the heavy statements
- D. Read the slow query log

### 42. Four nightly export jobs start at the same minute and the project hits a concurrent-operations quota, so three of them fail. What should the team do?

- A. Request a quota increase for the project
- B. Retry the failed operation with exponential backoff
- C. Export the table to CSV in Cloud Storage
- D. Move the job outside the contention window

### 43. A team wants a page when the database starts returning failed statements rather than only when CPU is high. Which alert should they add?

- A. Alert on the database error rate
- B. Alert on replication lag
- C. Watch CPU, memory, disk, and IOPS together
- D. Create an alerting policy on the metric

### 44. Deadlocks appear in the database log as a repeated message but no metric exists, so nobody notices the trend. What should the team build?

- A. Read the slow query log
- B. Route the audit logs to a locked log bucket
- C. Build a log-based metric from the error entries
- D. Use Query Insights to find the heavy statements

### 45. A table was truncated forty minutes ago and the team must get back to that moment, but first wants to prove the recovery on a copy. Select two.

- A. Extend the backup retention window
- B. Restore to the timestamp before the bad change
- C. Export a logical dump to Cloud Storage
- D. Create a Bigtable backup
- E. Clone the instance for the test

### 46. Compliance requires the ability to restore the database to any second within the past seven days. Which capability provides that?

- A. Enable automated backups with a retention window
- B. Enable point-in-time recovery
- C. Extend the backup retention window
- D. Export a logical dump to Cloud Storage

### 47. A team must refresh a 200 GB analytical table from Cloud SQL every month with the least operational effort. Which approach fits?

- A. Stream changes into BigQuery
- B. Query the source through BigQuery federated queries
- C. Export a logical dump to Cloud Storage
- D. Export the table into BigQuery

### 48. A logistics system can lose at most one minute of committed orders and must be writing again within ten minutes of losing its primary zone. Which design meets both targets?

- A. Enable automated backups with a retention window
- B. Restore the backup into the second region
- C. Add a cross-region read replica
- D. Enable regional high availability with a standby zone

### 49. A finance system can tolerate four hours of downtime but no more than fifteen minutes of lost data, and no standby capacity is permitted in the region. Which mechanism fits?

- A. Add a cross-region read replica
- B. Enable regional high availability with a standby zone
- C. Enable point-in-time recovery
- D. Run a controlled failover test

### 50. A privacy rule requires order rows to be deleted one hundred twenty days after fulfilment, and auditors check that nothing older is present. Which control satisfies the rule?

- A. Set a time-to-live policy on the collection
- B. Set the garbage-collection policy on the column family
- C. Apply a row-level retention policy
- D. Archive closed rows to cheaper storage

### 51. A read-heavy catalogue saturates its primary's CPU while write volume stays low, and the application tolerates a few seconds of replica lag. Which change fits?

- A. Add a read replica for the read traffic
- B. Add processing units to the Spanner instance
- C. Increase the machine type of the instance
- D. Shard the data across several instances

### 52. One table has grown to eight billion rows, every query filters by tenant and date, and maintenance on the whole table can no longer finish in the window. What should change?

- A. Add the index the slow query needs
- B. Partition the large table
- C. Add a read replica for the read traffic
- D. Increase the machine type of the instance

### 53. A team needs a read-only copy of a Cloud SQL database in a second region but is not allowed to run a second primary. Which option fits?

- A. Choose a multi-region instance configuration
- B. Add a cross-region read replica
- C. Enable regional high availability with a standby zone
- D. Add a secondary cluster in the second region

### 54. An order table carries fourteen indexes, and index usage statistics show six of them have never served a query while insert latency keeps climbing. What should the team do?

- A. Drop the unused index
- B. Add the index the slow query needs
- C. Raise the per-operation memory flag
- D. Partition the large table

### 55. A small team must run weekly maintenance exports and keep recovery points without anyone present. Select two.

- A. Take an on-demand backup before the change
- B. Provision the instance once by hand
- C. Enable automated backups with a retention window
- D. Run a controlled failover test
- E. Run the task on a managed schedule

### 56. A team must upgrade a Cloud SQL for MySQL instance by a major version and needs to know whether the application breaks before real traffic arrives. What should they do first?

- A. Perform an in-place major version upgrade
- B. Take a backup before the upgrade
- C. Watch the error rate after the change
- D. Test the upgrade on a clone first

### 57. A team must be told when observed monthly availability falls below the level it promised its own customers. Which practice fits?

- A. Watch CPU, memory, disk, and IOPS together
- B. Review the fleet in Database Center
- C. Track the availability signal against the agreed objective
- D. Create an alerting policy on the metric

---

## Domain 3 — Migrate Data Solutions (Migration Strategy, Conversion, and Cutover)

### 58. A two-terabyte MySQL database must move to Cloud SQL with under five minutes of write downtime. Select two.

- A. Write to both systems from the application
- B. Use Database Migration Service for the same engine
- C. Follow a cutover runbook with a rollback step
- D. Accept a scheduled extended outage
- E. Dump, restore, then replay the changes

### 59. The business accepts a six-hour Saturday outage for a forty-gigabyte database and wants the least engineering effort. Which strategy fits?

- A. Accept a scheduled extended outage
- B. Write to both systems from the application
- C. Set up reverse replication to the source
- D. Use Database Migration Service for the same engine

### 60. The source database cannot expose a replication slot, yet writes must continue during the transition. Which approach keeps both systems current?

- A. Write to both systems from the application
- B. Freeze writes during the cutover
- C. Accept a scheduled extended outage
- D. Use Database Migration Service for the same engine

### 61. An Oracle 19c database must move to AlloyDB, including conversion of PL/SQL packages and triggers. Which path fits?

- A. Use Database Migration Service for the same engine
- B. Dump, restore, then replay the changes
- C. Stream changes with Datastream
- D. Use Database Migration Service with schema conversion

### 62. Analysts need Oracle changes to appear in BigQuery continuously, and no database is being cut over. Which tool fits?

- A. Dump, restore, then replay the changes
- B. Stream changes with Datastream
- C. Use Database Migration Service with schema conversion
- D. Accept a scheduled extended outage

### 63. A thirty-gigabyte SQL Server database can be offline for a weekend and the team wants the simplest reliable path. Which approach fits?

- A. Dump, restore, then replay the changes
- B. Use Database Migration Service with schema conversion
- C. Set up reverse replication to the source
- D. Apply the captured change backlog before cutover

### 64. An Oracle to PostgreSQL assessment reports three hundred conversion issues, forty of them inside procedural packages. Which two actions should the team take before loading data? Select two.

- A. Repoint the connection string at the target
- B. Build the schema in a conversion workspace
- C. Rewrite the stored procedures and DML by hand
- D. Reset the sequences after the bulk load
- E. Freeze writes during the cutover

### 65. A converted schema loads successfully, but the first application inserts collide with existing keys because identity columns restart at one. What should the team do?

- A. Reset the sequences after the bulk load
- B. Repoint the connection string at the target
- C. Build the schema in a conversion workspace
- D. Reconcile row counts and checksums

### 66. Application code calls MySQL-specific functions such as IFNULL and DATE_FORMAT, and the target is PostgreSQL. What must the team do?

- A. Reset the sequences after the bulk load
- B. Build the schema in a conversion workspace
- C. Rewrite the stored procedures and DML by hand
- D. Write to both systems from the application

### 67. A team wants to find application paths that still use syntax the target rejects, without exposing users to the new database. Which approach fits?

- A. Repoint the connection string at the target
- B. Replay read traffic against the target
- C. Reconcile row counts and checksums
- D. Freeze writes during the cutover

### 68. A three-terabyte source must be loaded while writes continue, and the initial dump takes nine hours. How should the team keep the target current during that load?

- A. Use the engine native logical replication
- B. Export a logical dump to Cloud Storage
- C. Accept a scheduled extended outage
- D. Write to both systems from the application

### 69. The initial load finished, but writes made during the nine hours are not present on the target. What must happen before cutover?

- A. Repoint the connection string at the target
- B. Export a logical dump to Cloud Storage
- C. Apply the captured change backlog before cutover
- D. Reconcile row counts and checksums

### 70. A team must prove the target matches the source before switching traffic. Which two checks should it run? Select two.

- A. Follow a cutover runbook with a rollback step
- B. Reset the sequences after the bulk load
- C. Replay read traffic against the target
- D. Repoint the connection string at the target
- E. Reconcile row counts and checksums

### 71. After a full load the target reports a daily revenue total 0.3 percent lower than the source, although every table's row count matches. Which activity finds the difference?

- A. Follow a cutover runbook with a rollback step
- B. Write to both systems from the application
- C. Replay read traffic against the target
- D. Reconcile row counts and checksums

### 72. A cutover must be decided inside a thirty-minute window with a defined way back. Which two preparations matter most? Select two.

- A. Repoint the connection string at the target
- B. Measure the catch-up rate before choosing the window
- C. Accept a scheduled extended outage
- D. Follow a cutover runbook with a rollback step
- E. Write to both systems from the application

### 73. The target has passed validation and writes are frozen on the source, but application clients still open connections to the old endpoint. What remains?

- A. Repoint the connection string at the target
- B. Follow a cutover runbook with a rollback step
- C. Freeze writes during the cutover
- D. Set up reverse replication to the source

### 74. A team must guarantee that no new rows land on the source while the final increment is applied. What should they do?

- A. Repoint the connection string at the target
- B. Accept a scheduled extended outage
- C. Set up reverse replication to the source
- D. Freeze writes during the cutover

### 75. A team must be able to roll back after cutover without losing the writes that were made on the new database. What has to be in place?

- A. Freeze writes during the cutover
- B. Set up reverse replication to the source
- C. Decommission the source after a parallel period
- D. Repoint the connection string at the target

### 76. Six weeks after cutover, analysts still query the old database and expect the new writes to be visible there. What must be in place?

- A. Decommission the source after a parallel period
- B. Set up reverse replication to the source
- C. Repoint the connection string at the target
- D. Write to both systems from the application

### 77. A one-terabyte Oracle source must move to Cloud SQL for PostgreSQL with downtime under two minutes. Which approach fits?

- A. Write to both systems from the application
- B. Use Database Migration Service with schema conversion
- C. Accept a scheduled extended outage
- D. Dump, restore, then replay the changes

### 78. Month-end batch load pushes the source change rate to five thousand rows per second, and the cutover must still fit its window. What should the team do?

- A. Move the job outside the contention window
- B. Accept a scheduled extended outage
- C. Write to both systems from the application
- D. Measure the catch-up rate before choosing the window

### 79. The source hardware lease expires next month and the migration has been stable for six weeks. What should the team plan?

- A. Write to both systems from the application
- B. Repoint the connection string at the target
- C. Decommission the source after a parallel period
- D. Set up reverse replication to the source

### 80. The source must be retired, but its historical rows have to stay queryable for seven years. What should the team do first?

- A. Set up reverse replication to the source
- B. Decommission the source after a parallel period
- C. Keep part of the estate on-premises with a hybrid link
- D. Export the table into BigQuery

---

## Domain 4 — Deploy Scalable and Highly Available Databases in Google Cloud (Deployment, High Availability, and Disaster Recovery)

### 81. A new Cloud SQL instance must exist identically in development, staging, and production. Select two.

- A. Test the upgrade on a clone first
- B. Provision the instance with a Terraform module
- C. Apply the change through the infrastructure pipeline
- D. Provision the instance once by hand
- E. Stand up a parallel instance and switch over

### 82. Cloud SQL instances were created by hand in each environment, and staging now runs different flags from production. What should change?

- A. Provision the instance once by hand
- B. Test the upgrade on a clone first
- C. Provision the instance with a Terraform module
- D. Take a backup before the upgrade

### 83. A regulated workload must be created with a customer-managed key, private addressing, and high availability in every new project without a human checklist. What should the team use?

- A. Provision the instance once by hand
- B. Review the fleet in Database Center
- C. Watch the error rate after the change
- D. Apply the change through the infrastructure pipeline

### 84. A team has never exercised its recovery plan and must show that the design survives losing a whole region. Which exercise builds that evidence?

- A. Run a controlled failover test
- B. Take a backup before the upgrade
- C. Rehearse the promotion in a test project
- D. Watch the error rate after the change

### 85. A team must confirm that the standby in the second zone really assumes the primary role when the active zone disappears. What should they run?

- A. Run a controlled failover test
- B. Watch the error rate after the change
- C. Restart the instance in the window
- D. Set a deny maintenance period over the peak event

### 86. A drill promotes the cross-region replica and finds the promoted instance too small to carry production traffic. What should change before the next drill?

- A. Run a controlled failover test
- B. Add a read replica for the read traffic
- C. Reserve headroom above the measured peak
- D. Pre-size the promoted replica for the full load

### 87. A team must serve reads close to users in three regions while keeping strongly consistent writes. Select two.

- A. Add a read-only region to the configuration
- B. Add a secondary cluster in the second region
- C. Choose a multi-region instance configuration
- D. Enable regional high availability with a standby zone
- E. Add a cross-region read replica

### 88. A Spanner deployment must keep accepting writes and preserving strong consistency when a whole region is lost. Which choice fits?

- A. Restore the backup into the second region
- B. Enable regional high availability with a standby zone
- C. Add a cross-region read replica
- D. Choose a multi-region instance configuration

### 89. A Bigtable table must keep serving if one cluster's zone fails, and client applications cannot be changed. Which setting provides that?

- A. Add a cross-region read replica
- B. Route the app profile across both clusters
- C. Restore the backup into the second region
- D. Pin the app profile to one cluster

### 90. Reporting queries consume seventy percent of an AlloyDB primary's CPU, and the read pool still has idle capacity. What should the team do?

- A. Send reporting queries to the read replica
- B. Increase the machine type of the instance
- C. Add nodes to the read pool
- D. Cache the hot read path in Memorystore

### 91. Reporting queries consume seventy percent of a Cloud SQL primary's CPU, and the application tolerates three seconds of replica lag. What should the team do?

- A. Send reporting queries to the read replica
- B. Increase the disk size to raise throughput
- C. Partition the large table
- D. Cache the hot read path in Memorystore

### 92. A platform team wants database changes reviewed and applied by the same pipeline as application code. Which practice delivers that?

- A. Review the fleet in Database Center
- B. Test the upgrade on a clone first
- C. Apply the change through the infrastructure pipeline
- D. Provision the instance with a Terraform module

### 93. A team must create one database instance per customer, each with consistent flags and labels, without repeating manual steps. What should they use?

- A. Take a backup before the upgrade
- B. Provision the instance once by hand
- C. Stand up a parallel instance and switch over
- D. Provision the instance with a Terraform module

### 94. A high availability instance failed over last night, and the team learned about it from user complaints. What was missing?

- A. Review the fleet in Database Center
- B. Alert when the instance is unreachable
- C. Take a backup before the upgrade
- D. Run a controlled failover test

### 95. A team must know within a minute when a zone failover happens and which instance is now primary. What should they configure?

- A. Review the fleet in Database Center
- B. Create an alerting policy on the metric
- C. Use Query Insights to find the heavy statements
- D. Watch CPU, memory, disk, and IOPS together

### 96. A region is unavailable, the recovery time objective is one hour, the recovery point objective is five minutes, and a cross-region replica exists. What should the team do?

- A. Enable regional high availability with a standby zone
- B. Promote the cross-region replica during the outage
- C. Restore the backup into the second region
- D. Restore to the timestamp before the bad change

### 97. During a failover the old primary may still be reachable and could accept writes after the replica is promoted. What must the team do?

- A. Set up reverse replication to the source
- B. Fence the old primary before promotion
- C. Follow a cutover runbook with a rollback step
- D. Freeze writes during the cutover

### 98. An application's connection pool keeps reconnecting to the old primary's address after a failover. Which change makes reconnection follow the current primary?

- A. Put a session pooler in front of the instance
- B. Repoint the connection string at the target
- C. Add the client range to authorized networks
- D. Use the language connector with IAM credentials

### 99. A cross-region replica runs at thirty percent of the primary's size because it only serves some reads today. What must change for disaster recovery?

- A. Reserve headroom above the measured peak
- B. Add processing units to the Spanner instance
- C. Add nodes to the read pool
- D. Pre-size the promoted replica for the full load

### 100. A team must decide how much spare capacity a standby needs so that a zone failover keeps the current p99 latency. What is the right basis?

- A. Reserve headroom above the measured peak
- B. Reduce the machine type to match observed use
- C. Add a read replica for the read traffic
- D. Scale down outside business hours

---

## Answer key and explanations

### Question 1 — C

Answer: Size the instance from the observed peak metrics. Sizing from measured peak values produces a defensible shape, while autogrow, commitments, and replicas all assume that a shape decision already exists. Choose a shape from measured CPU, memory, and IOPS rather than from a guess. Local study-map skill 1.1 (Workload Sizing From Current Metrics), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 1 (design innovative, scalable, and highly available cloud database solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Send reads to a copy so the primary keeps its capacity for writes. Why the correct answer wins: Sizing from measured peak values produces a defensible shape, while autogrow, commitments, and replicas all assume that a shape decision already exists.
- **B:** Incorrect for this question. A one- or three-year commitment that discounts the capacity always in use. Why the correct answer wins: Sizing from measured peak values produces a defensible shape, while autogrow, commitments, and replicas all assume that a shape decision already exists.
- **C:** Correct. Choose a shape from measured CPU, memory, and IOPS rather than from a guess. In this case: Sizing from measured peak values produces a defensible shape, while autogrow, commitments, and replicas all assume that a shape decision already exists.
- **D:** Incorrect for this question. Avoid a full-disk outage at the cost of unplanned storage growth. Why the correct answer wins: Sizing from measured peak values produces a defensible shape, while autogrow, commitments, and replicas all assume that a shape decision already exists.

### Question 2 — D

Answer: Reserve headroom above the measured peak. The known spike has to fit inside the shape the team selects, so headroom above the ordinary peak is the sizing input rather than a smaller or cheaper configuration. Keep spare capacity so a failover or a traffic spike does not saturate the instance. Local study-map skill 1.1 (Workload Sizing From Current Metrics), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 1 (design innovative, scalable, and highly available cloud database solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Separate analytical reads from the write path. Why the correct answer wins: The known spike has to fit inside the shape the team selects, so headroom above the ordinary peak is the sizing input rather than a smaller or cheaper configuration.
- **B:** Incorrect for this question. Remove capacity that serves no traffic. Why the correct answer wins: The known spike has to fit inside the shape the team selects, so headroom above the ordinary peak is the sizing input rather than a smaller or cheaper configuration.
- **C:** Incorrect for this question. Shrink an instance whose peak fits a smaller shape. Why the correct answer wins: The known spike has to fit inside the shape the team selects, so headroom above the ordinary peak is the sizing input rather than a smaller or cheaper configuration.
- **D:** Correct. Keep spare capacity so a failover or a traffic spike does not saturate the instance. In this case: The known spike has to fit inside the shape the team selects, so headroom above the ordinary peak is the sizing input rather than a smaller or cheaper configuration.

### Question 3 — C

Answer: Move the data to SSD storage. Waiting on random reads is a storage latency symptom, so moving the data to SSD attacks the measured wait instead of adding compute or another copy. Trade a higher price per gigabyte for lower latency on random reads. Local study-map skill 1.2 (Compute and Storage Sizing Tradeoffs), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 1 (design innovative, scalable, and highly available cloud database solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Send reads to a copy so the primary keeps its capacity for writes. Why the correct answer wins: Waiting on random reads is a storage latency symptom, so moving the data to SSD attacks the measured wait instead of adding compute or another copy.
- **B:** Incorrect for this question. Split one table into ranges so pruning and maintenance act on less data. Why the correct answer wins: Waiting on random reads is a storage latency symptom, so moving the data to SSD attacks the measured wait instead of adding compute or another copy.
- **C:** Correct. Trade a higher price per gigabyte for lower latency on random reads. In this case: Waiting on random reads is a storage latency symptom, so moving the data to SSD attacks the measured wait instead of adding compute or another copy.
- **D:** Incorrect for this question. Move the instance to a larger shape so more vCPU and memory serve the same data. Why the correct answer wins: Waiting on random reads is a storage latency symptom, so moving the data to SSD attacks the measured wait instead of adding compute or another copy.

### Question 4 — B

Answer: Move the data to HDD storage. HDD storage is the cheaper option for throughput-oriented sequential scans, and node count or garbage collection does not change the price per gigabyte. Trade latency for a lower price on large, throughput-oriented scans. Local study-map skill 1.2 (Compute and Storage Sizing Tradeoffs), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 1 (design innovative, scalable, and highly available cloud database solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Increase the cluster size so more tablet servers absorb the request rate. Why the correct answer wins: HDD storage is the cheaper option for throughput-oriented sequential scans, and node count or garbage collection does not change the price per gigabyte.
- **B:** Correct. Trade latency for a lower price on large, throughput-oriented scans. In this case: HDD storage is the cheaper option for throughput-oriented sequential scans, and node count or garbage collection does not change the price per gigabyte.
- **C:** Incorrect for this question. A rule that drops versions by age or count, which also bounds recovery. Why the correct answer wins: HDD storage is the cheaper option for throughput-oriented sequential scans, and node count or garbage collection does not change the price per gigabyte.
- **D:** Incorrect for this question. Trade a higher price per gigabyte for lower latency on random reads. Why the correct answer wins: HDD storage is the cheaper option for throughput-oriented sequential scans, and node count or garbage collection does not change the price per gigabyte.

### Question 5 — B

Answer: Increase the machine type of the instance. A larger machine type adds memory as well as compute, which is the resource the buffer pool is missing, whereas disk, an index, or a replica leaves memory unchanged. Move the instance to a larger shape so more vCPU and memory serve the same data. Local study-map skill 1.3 (Machine Type and Storage Type Selection), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 1 (design innovative, scalable, and highly available cloud database solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Buy more storage so the attached disk also yields more IOPS and throughput. Why the correct answer wins: A larger machine type adds memory as well as compute, which is the resource the buffer pool is missing, whereas disk, an index, or a replica leaves memory unchanged.
- **B:** Correct. Move the instance to a larger shape so more vCPU and memory serve the same data. In this case: A larger machine type adds memory as well as compute, which is the resource the buffer pool is missing, whereas disk, an index, or a replica leaves memory unchanged.
- **C:** Incorrect for this question. Send reads to a copy so the primary keeps its capacity for writes. Why the correct answer wins: A larger machine type adds memory as well as compute, which is the resource the buffer pool is missing, whereas disk, an index, or a replica leaves memory unchanged.
- **D:** Incorrect for this question. Create an index that turns a scan into a lookup for the predicate. Why the correct answer wins: A larger machine type adds memory as well as compute, which is the resource the buffer pool is missing, whereas disk, an index, or a replica leaves memory unchanged.

### Question 6 — D

Answer: Increase the disk size to raise throughput. Disk size on the instance governs its IOPS and throughput ceiling, so growing the disk adds the missing capability without touching the machine type. Buy more storage so the attached disk also yields more IOPS and throughput. Local study-map skill 1.3 (Machine Type and Storage Type Selection), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 1 (design innovative, scalable, and highly available cloud database solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Trade latency for a lower price on large, throughput-oriented scans. Why the correct answer wins: Disk size on the instance governs its IOPS and throughput ceiling, so growing the disk adds the missing capability without touching the machine type.
- **B:** Incorrect for this question. Raise provisioned compute in 1000-unit node steps or 100-unit increments. Why the correct answer wins: Disk size on the instance governs its IOPS and throughput ceiling, so growing the disk adds the missing capability without touching the machine type.
- **C:** Incorrect for this question. Grow the AlloyDB read pool that serves read-only connections. Why the correct answer wins: Disk size on the instance governs its IOPS and throughput ceiling, so growing the disk adds the missing capability without touching the machine type.
- **D:** Correct. Buy more storage so the attached disk also yields more IOPS and throughput. In this case: Disk size on the instance governs its IOPS and throughput ceiling, so growing the disk adds the missing capability without touching the machine type.

### Question 7 — A, B

Answers: Add a cross-region read replica; Promote the cross-region replica during the outage. Regional high availability and a same-region replica both survive only a zone, so a cross-region copy plus a rehearsed promotion is the pair that restores writes after a regional loss. A copy in a second region that serves reads and can be promoted. Turn the replica into an independent primary so the application can resume writes. Local study-map skill 1.4 (Zonal, Regional, and Multi-Regional Tradeoffs), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 1 (design innovative, scalable, and highly available cloud database solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Correct. A copy in a second region that serves reads and can be promoted. In this case: Regional high availability and a same-region replica both survive only a zone, so a cross-region copy plus a rehearsed promotion is the pair that restores writes after a regional loss.
- **B:** Correct. Turn the replica into an independent primary so the application can resume writes. In this case: Regional high availability and a same-region replica both survive only a zone, so a cross-region copy plus a rehearsed promotion is the pair that restores writes after a regional loss.
- **C:** Incorrect for this question. A primary and standby in two zones of one region with automatic failover. Why the correct answer wins: Regional high availability and a same-region replica both survive only a zone, so a cross-region copy plus a rehearsed promotion is the pair that restores writes after a regional loss.
- **D:** Incorrect for this question. A same-region copy that protects against a zone failure, not a regional one. Why the correct answer wins: Regional high availability and a same-region replica both survive only a zone, so a cross-region copy plus a rehearsed promotion is the pair that restores writes after a regional loss.
- **E:** Incorrect for this question. Block maintenance during a period when an interruption is unacceptable. Why the correct answer wins: Regional high availability and a same-region replica both survive only a zone, so a cross-region copy plus a rehearsed promotion is the pair that restores writes after a regional loss.

### Question 8 — D

Answer: Enable regional high availability with a standby zone. A regional instance keeps a standby in a second zone and fails over automatically, which satisfies the requirement without paying for cross-region replication or a restore. A primary and standby in two zones of one region with automatic failover. Local study-map skill 1.4 (Zonal, Regional, and Multi-Regional Tradeoffs), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 1 (design innovative, scalable, and highly available cloud database solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Rebuild the database in the surviving region from the latest backup. Why the correct answer wins: A regional instance keeps a standby in a second zone and fails over automatically, which satisfies the requirement without paying for cross-region replication or a restore.
- **B:** Incorrect for this question. A copy in a second region that serves reads and can be promoted. Why the correct answer wins: A regional instance keeps a standby in a second zone and fails over automatically, which satisfies the requirement without paying for cross-region replication or a restore.
- **C:** Incorrect for this question. A topology that places replicas in separate regions for regional-failure tolerance. Why the correct answer wins: A regional instance keeps a standby in a second zone and fails over automatically, which satisfies the requirement without paying for cross-region replication or a restore.
- **D:** Correct. A primary and standby in two zones of one region with automatic failover. In this case: A regional instance keeps a standby in a second zone and fails over automatically, which satisfies the requirement without paying for cross-region replication or a restore.

### Question 9 — C

Answer: Add a secondary cluster in the second region. A secondary cluster is a promotable cross-region copy that also serves reads, while a read pool is same-region and regional high availability stops at the region boundary. An AlloyDB cross-region copy that can be promoted to a primary cluster. Local study-map skill 1.4 (Zonal, Regional, and Multi-Regional Tradeoffs), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 1 (design innovative, scalable, and highly available cloud database solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Rebuild the database in the surviving region from the latest backup. Why the correct answer wins: A secondary cluster is a promotable cross-region copy that also serves reads, while a read pool is same-region and regional high availability stops at the region boundary.
- **B:** Incorrect for this question. Grow the AlloyDB read pool that serves read-only connections. Why the correct answer wins: A secondary cluster is a promotable cross-region copy that also serves reads, while a read pool is same-region and regional high availability stops at the region boundary.
- **C:** Correct. An AlloyDB cross-region copy that can be promoted to a primary cluster. In this case: A secondary cluster is a promotable cross-region copy that also serves reads, while a read pool is same-region and regional high availability stops at the region boundary.
- **D:** Incorrect for this question. A primary and standby in two zones of one region with automatic failover. Why the correct answer wins: A secondary cluster is a promotable cross-region copy that also serves reads, while a read pool is same-region and regional high availability stops at the region boundary.

### Question 10 — A

Answer: Set a deny maintenance period over the peak event. A deny maintenance period blocks the maintenance event across the protected window so the patch lands later in the quarter, while a normal window or an upgrade would still risk an interruption. Block maintenance during a period when an interruption is unacceptable. Local study-map skill 1.5 (Maintenance Windows and Notification), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 1 (design innovative, scalable, and highly available cloud database solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Correct. Block maintenance during a period when an interruption is unacceptable. In this case: A deny maintenance period blocks the maintenance event across the protected window so the patch lands later in the quarter, while a normal window or an upgrade would still risk an interruption.
- **B:** Incorrect for this question. Apply the configuration change with a brief restart. Why the correct answer wins: A deny maintenance period blocks the maintenance event across the protected window so the patch lands later in the quarter, while a normal window or an upgrade would still risk an interruption.
- **C:** Incorrect for this question. Change the engine version on the running instance during the window. Why the correct answer wins: A deny maintenance period blocks the maintenance event across the protected window so the patch lands later in the quarter, while a normal window or an upgrade would still risk an interruption.
- **D:** Incorrect for this question. Choose the weekly window when patching may interrupt the instance. Why the correct answer wins: A deny maintenance period blocks the maintenance event across the protected window so the patch lands later in the quarter, while a normal window or an upgrade would still risk an interruption.

### Question 11 — A

Answer: Schedule the maintenance window in the low-traffic period. Setting the maintenance window moves the patching event into the tolerated hours, whereas a deny period blocks patching entirely and neither a test nor a backup changes when it runs. Choose the weekly window when patching may interrupt the instance. Local study-map skill 1.5 (Maintenance Windows and Notification), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 1 (design innovative, scalable, and highly available cloud database solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Correct. Choose the weekly window when patching may interrupt the instance. In this case: Setting the maintenance window moves the patching event into the tolerated hours, whereas a deny period blocks patching entirely and neither a test nor a backup changes when it runs.
- **B:** Incorrect for this question. A recovery point that makes the upgrade reversible in practice. Why the correct answer wins: Setting the maintenance window moves the patching event into the tolerated hours, whereas a deny period blocks patching entirely and neither a test nor a backup changes when it runs.
- **C:** Incorrect for this question. Block maintenance during a period when an interruption is unacceptable. Why the correct answer wins: Setting the maintenance window moves the patching event into the tolerated hours, whereas a deny period blocks patching entirely and neither a test nor a backup changes when it runs.
- **D:** Incorrect for this question. Trigger a switchover in a test window and observe how long writes are unavailable. Why the correct answer wins: Setting the maintenance window moves the patching event into the tolerated hours, whereas a deny period blocks patching entirely and neither a test nor a backup changes when it runs.

### Question 12 — A, E

Answers: Connect over private IP inside the VPC; Enable IAM database authentication. Private IP removes the public surface and IAM database authentication removes the stored password, while an allowlist, public SSL, and a native password all keep a credential or an internet path. A private address reachable only from the VPC and connected networks. Map an IAM principal to a database user so no password is stored. Local study-map skill 1.6 (Network Connectivity and Private Access), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 1 (design innovative, scalable, and highly available cloud database solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Correct. A private address reachable only from the VPC and connected networks. In this case: Private IP removes the public surface and IAM database authentication removes the stored password, while an allowlist, public SSL, and a native password all keep a credential or an internet path.
- **B:** Incorrect for this question. A public address that requires encrypted connections from any client. Why the correct answer wins: Private IP removes the public surface and IAM database authentication removes the stored password, while an allowlist, public SSL, and a native password all keep a credential or an internet path.
- **C:** Incorrect for this question. A public-IP allowlist that admits the caller range. Why the correct answer wins: Private IP removes the public surface and IAM database authentication removes the stored password, while an allowlist, public SSL, and a native password all keep a credential or an internet path.
- **D:** Incorrect for this question. A native database user whose credential must be rotated and stored. Why the correct answer wins: Private IP removes the public surface and IAM database authentication removes the stored password, while an allowlist, public SSL, and a native password all keep a credential or an internet path.
- **E:** Correct. Map an IAM principal to a database user so no password is stored. In this case: Private IP removes the public surface and IAM database authentication removes the stored password, while an allowlist, public SSL, and a native password all keep a credential or an internet path.

### Question 13 — D

Answer: Publish the instance behind Private Service Connect. Private Service Connect gives the partner a local endpoint into a published service with no peering or route exchange, which private IP alone and an address allowlist both require. A private endpoint in the consumer VPC that reaches the service without peering. Local study-map skill 1.6 (Network Connectivity and Private Access), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 1 (design innovative, scalable, and highly available cloud database solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A public-IP allowlist that admits the caller range. Why the correct answer wins: Private Service Connect gives the partner a local endpoint into a published service with no peering or route exchange, which private IP alone and an address allowlist both require.
- **B:** Incorrect for this question. A private address reachable only from the VPC and connected networks. Why the correct answer wins: Private Service Connect gives the partner a local endpoint into a published service with no peering or route exchange, which private IP alone and an address allowlist both require.
- **C:** Incorrect for this question. A centrally managed network that lends subnets to the database project. Why the correct answer wins: Private Service Connect gives the partner a local endpoint into a published service with no peering or route exchange, which private IP alone and an address allowlist both require.
- **D:** Correct. A private endpoint in the consumer VPC that reaches the service without peering. In this case: Private Service Connect gives the partner a local endpoint into a published service with no peering or route exchange, which private IP alone and an address allowlist both require.

### Question 14 — C

Answer: Encrypt with a customer-managed key in Cloud KMS. Customer-managed keys place key custody and revocation with the bank, while Google-managed keys, audit logs, and a service perimeter do not give the customer control of the key. A key the customer owns and can rotate or revoke. Local study-map skill 1.7 (Key Management and Encryption), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 1 (design innovative, scalable, and highly available cloud database solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Record reads and writes, which are not captured by default. Why the correct answer wins: Customer-managed keys place key custody and revocation with the bank, while Google-managed keys, audit logs, and a service perimeter do not give the customer control of the key.
- **B:** Incorrect for this question. Default encryption at rest with keys the customer neither sees nor manages. Why the correct answer wins: Customer-managed keys place key custody and revocation with the bank, while Google-managed keys, audit logs, and a service perimeter do not give the customer control of the key.
- **C:** Correct. A key the customer owns and can rotate or revoke. In this case: Customer-managed keys place key custody and revocation with the bank, while Google-managed keys, audit logs, and a service perimeter do not give the customer control of the key.
- **D:** Incorrect for this question. A boundary that blocks data exfiltration even from an authorized identity. Why the correct answer wins: Customer-managed keys place key custody and revocation with the bank, while Google-managed keys, audit logs, and a service perimeter do not give the customer control of the key.

### Question 15 — D

Answer: Rotate the customer-managed key on a schedule. Rotation creates a fresh key version for new writes while existing ciphertext stays decryptable under the old version, unlike switching key ownership or changing retention and logging. Produce new key versions so an old version stops encrypting new data. Local study-map skill 1.7 (Key Management and Encryption), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 1 (design innovative, scalable, and highly available cloud database solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Default encryption at rest with keys the customer neither sees nor manages. Why the correct answer wins: Rotation creates a fresh key version for new writes while existing ciphertext stays decryptable under the old version, unlike switching key ownership or changing retention and logging.
- **B:** Incorrect for this question. Record reads and writes, which are not captured by default. Why the correct answer wins: Rotation creates a fresh key version for new writes while existing ciphertext stays decryptable under the old version, unlike switching key ownership or changing retention and logging.
- **C:** Incorrect for this question. Keep backups longer so an older restore point remains available. Why the correct answer wins: Rotation creates a fresh key version for new writes while existing ciphertext stays decryptable under the old version, unlike switching key ownership or changing retention and logging.
- **D:** Correct. Produce new key versions so an old version stops encrypting new data. In this case: Rotation creates a fresh key version for new writes while existing ciphertext stays decryptable under the old version, unlike switching key ownership or changing retention and logging.

### Question 16 — C

Answer: Put a session pooler in front of the instance. A session pooler multiplexes many idle application connections onto few database sessions, so the ceiling is no longer reached and no larger shape is needed. A pooler that multiplexes many application connections onto few database sessions. Local study-map skill 1.8 (Session Pooling and Connection Management), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 1 (design innovative, scalable, and highly available cloud database solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Increase the database-level connection ceiling on the instance. Why the correct answer wins: A session pooler multiplexes many idle application connections onto few database sessions, so the ceiling is no longer reached and no larger shape is needed.
- **B:** Incorrect for this question. Buy a larger shape because the connection limit scales with memory. Why the correct answer wins: A session pooler multiplexes many idle application connections onto few database sessions, so the ceiling is no longer reached and no larger shape is needed.
- **C:** Correct. A pooler that multiplexes many application connections onto few database sessions. In this case: A session pooler multiplexes many idle application connections onto few database sessions, so the ceiling is no longer reached and no larger shape is needed.
- **D:** Incorrect for this question. Move the instance to a larger shape so more vCPU and memory serve the same data. Why the correct answer wins: A session pooler multiplexes many idle application connections onto few database sessions, so the ceiling is no longer reached and no larger shape is needed.

### Question 17 — D

Answer: Fix the connection leak in the application. The leak is the cause of the exhaustion, so closing sessions in the application removes the pressure that a pooler or a higher limit would only delay. Close sessions that the application opens and never returns to the pool. Local study-map skill 1.8 (Session Pooling and Connection Management), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 1 (design innovative, scalable, and highly available cloud database solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Send reads to a copy so the primary keeps its capacity for writes. Why the correct answer wins: The leak is the cause of the exhaustion, so closing sessions in the application removes the pressure that a pooler or a higher limit would only delay.
- **B:** Incorrect for this question. A pooler that multiplexes many application connections onto few database sessions. Why the correct answer wins: The leak is the cause of the exhaustion, so closing sessions in the application removes the pressure that a pooler or a higher limit would only delay.
- **C:** Incorrect for this question. Increase the database-level connection ceiling on the instance. Why the correct answer wins: The leak is the cause of the exhaustion, so closing sessions in the application removes the pressure that a pooler or a higher limit would only delay.
- **D:** Correct. Close sessions that the application opens and never returns to the pool. In this case: The leak is the cause of the exhaustion, so closing sessions in the application removes the pressure that a pooler or a higher limit would only delay.

### Question 18 — A, D

Answers: Enable Data Access audit logs; Route the audit logs to a locked log bucket. Row reads appear only in Data Access audit logs, and routing those entries to a locked destination keeps the evidence after the default bucket is gone. Record reads and writes, which are not captured by default. Export entries to storage whose retention cannot be shortened. Local study-map skill 1.9 (Auditing Policies for Managed Services), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 1 (design innovative, scalable, and highly available cloud database solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Correct. Export entries to storage whose retention cannot be shortened. In this case: Row reads appear only in Data Access audit logs, and routing those entries to a locked destination keeps the evidence after the default bucket is gone.
- **B:** Incorrect for this question. Turn a recurring log pattern into a metric that can be charted and alerted on. Why the correct answer wins: Row reads appear only in Data Access audit logs, and routing those entries to a locked destination keeps the evidence after the default bucket is gone.
- **C:** Incorrect for this question. A single view of health, security, and version posture across database instances. Why the correct answer wins: Row reads appear only in Data Access audit logs, and routing those entries to a locked destination keeps the evidence after the default bucket is gone.
- **D:** Correct. Record reads and writes, which are not captured by default. In this case: Row reads appear only in Data Access audit logs, and routing those entries to a locked destination keeps the evidence after the default bucket is gone.
- **E:** Incorrect for this question. Record configuration changes only, leaving row-level reads unaudited. Why the correct answer wins: Row reads appear only in Data Access audit logs, and routing those entries to a locked destination keeps the evidence after the default bucket is gone.

### Question 19 — C

Answer: Enable Data Access audit logs. Admin Activity logs capture configuration changes only, so reads stay invisible until Data Access audit logs are enabled for the service. Record reads and writes, which are not captured by default. Local study-map skill 1.9 (Auditing Policies for Managed Services), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 1 (design innovative, scalable, and highly available cloud database solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Record configuration changes only, leaving row-level reads unaudited. Why the correct answer wins: Admin Activity logs capture configuration changes only, so reads stay invisible until Data Access audit logs are enabled for the service.
- **B:** Incorrect for this question. Expire documents once their usefulness ends. Why the correct answer wins: Admin Activity logs capture configuration changes only, so reads stay invisible until Data Access audit logs are enabled for the service.
- **C:** Correct. Record reads and writes, which are not captured by default. In this case: Admin Activity logs capture configuration changes only, so reads stay invisible until Data Access audit logs are enabled for the service.
- **D:** Incorrect for this question. A managed export of documents used as the restore point. Why the correct answer wins: Admin Activity logs capture configuration changes only, so reads stay invisible until Data Access audit logs are enabled for the service.

### Question 20 — B

Answer: Run the database on bare metal solution. Bare metal solution provides dedicated hardware without a hypervisor, whereas a self-managed virtual machine, a partner service, and a managed database all place a hypervisor or another operator in the path. Dedicated hardware for engines that cannot be virtualized or licensed for a managed service. Local study-map skill 1.10 (Managed, Self-Managed, and Partner Offerings), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 1 (design innovative, scalable, and highly available cloud database solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A managed MySQL, PostgreSQL, or SQL Server instance with Google-operated backups, patching, and failover. Why the correct answer wins: Bare metal solution provides dedicated hardware without a hypervisor, whereas a self-managed virtual machine, a partner service, and a managed database all place a hypervisor or another operator in the path.
- **B:** Correct. Dedicated hardware for engines that cannot be virtualized or licensed for a managed service. In this case: Bare metal solution provides dedicated hardware without a hypervisor, whereas a self-managed virtual machine, a partner service, and a managed database all place a hypervisor or another operator in the path.
- **C:** Incorrect for this question. A third-party database operated by its vendor on Google Cloud infrastructure. Why the correct answer wins: Bare metal solution provides dedicated hardware without a hypervisor, whereas a self-managed virtual machine, a partner service, and a managed database all place a hypervisor or another operator in the path.
- **D:** Incorrect for this question. A self-managed engine on virtual machines where the team owns patching, backups, and failover. Why the correct answer wins: Bare metal solution provides dedicated hardware without a hypervisor, whereas a self-managed virtual machine, a partner service, and a managed database all place a hypervisor or another operator in the path.

### Question 21 — D

Answer: Use Cloud SQL for the relational workload. Cloud SQL is managed at that scale with backups and patching handled for the team, while self-managed and bare metal add operations and Spanner is sized for a much larger, distributed need. A managed MySQL, PostgreSQL, or SQL Server instance with Google-operated backups, patching, and failover. Local study-map skill 1.10 (Managed, Self-Managed, and Partner Offerings), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 1 (design innovative, scalable, and highly available cloud database solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Dedicated hardware for engines that cannot be virtualized or licensed for a managed service. Why the correct answer wins: Cloud SQL is managed at that scale with backups and patching handled for the team, while self-managed and bare metal add operations and Spanner is sized for a much larger, distributed need.
- **B:** Incorrect for this question. A horizontally scalable relational database with strong consistency across regions and no manual sharding. Why the correct answer wins: Cloud SQL is managed at that scale with backups and patching handled for the team, while self-managed and bare metal add operations and Spanner is sized for a much larger, distributed need.
- **C:** Incorrect for this question. A self-managed engine on virtual machines where the team owns patching, backups, and failover. Why the correct answer wins: Cloud SQL is managed at that scale with backups and patching handled for the team, while self-managed and bare metal add operations and Spanner is sized for a much larger, distributed need.
- **D:** Correct. A managed MySQL, PostgreSQL, or SQL Server instance with Google-operated backups, patching, and failover. In this case: Cloud SQL is managed at that scale with backups and patching handled for the team, while self-managed and bare metal add operations and Spanner is sized for a much larger, distributed need.

### Question 22 — A, C

Answers: Use Firestore for the document workload; Export the table into BigQuery. Firestore supplies the document model with device sync and managed replication, and exporting to BigQuery keeps analytical reads off the operational database. A document database with automatic multi-region replication, offline client support, and index-driven queries. Copy the analytical slice into the warehouse on a schedule. Local study-map skill 1.11 (SQL and NoSQL Data Model Fit), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 1 (design innovative, scalable, and highly available cloud database solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Correct. Copy the analytical slice into the warehouse on a schedule. In this case: Firestore supplies the document model with device sync and managed replication, and exporting to BigQuery keeps analytical reads off the operational database.
- **B:** Incorrect for this question. A managed Redis-compatible in-memory store placed in front of the system of record. Why the correct answer wins: Firestore supplies the document model with device sync and managed replication, and exporting to BigQuery keeps analytical reads off the operational database.
- **C:** Correct. A document database with automatic multi-region replication, offline client support, and index-driven queries. In this case: Firestore supplies the document model with device sync and managed replication, and exporting to BigQuery keeps analytical reads off the operational database.
- **D:** Incorrect for this question. A wide-column NoSQL service built for very high write and read rates over a sparse, row-key-ordered model. Why the correct answer wins: Firestore supplies the document model with device sync and managed replication, and exporting to BigQuery keeps analytical reads off the operational database.
- **E:** Incorrect for this question. A managed MySQL, PostgreSQL, or SQL Server instance with Google-operated backups, patching, and failover. Why the correct answer wins: Firestore supplies the document model with device sync and managed replication, and exporting to BigQuery keeps analytical reads off the operational database.

### Question 23 — A

Answer: Use Bigtable for the high-throughput wide-column workload. Bigtable's row-key-ordered wide-column model handles that write rate at the lowest cost per write, while the relational options carry transaction and query overhead the workload does not use. A wide-column NoSQL service built for very high write and read rates over a sparse, row-key-ordered model. Local study-map skill 1.11 (SQL and NoSQL Data Model Fit), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 1 (design innovative, scalable, and highly available cloud database solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Correct. A wide-column NoSQL service built for very high write and read rates over a sparse, row-key-ordered model. In this case: Bigtable's row-key-ordered wide-column model handles that write rate at the lowest cost per write, while the relational options carry transaction and query overhead the workload does not use.
- **B:** Incorrect for this question. A managed MySQL, PostgreSQL, or SQL Server instance with Google-operated backups, patching, and failover. Why the correct answer wins: Bigtable's row-key-ordered wide-column model handles that write rate at the lowest cost per write, while the relational options carry transaction and query overhead the workload does not use.
- **C:** Incorrect for this question. A managed PostgreSQL-compatible database with a separate read pool and columnar acceleration for mixed transactional and analytical load. Why the correct answer wins: Bigtable's row-key-ordered wide-column model handles that write rate at the lowest cost per write, while the relational options carry transaction and query overhead the workload does not use.
- **D:** Incorrect for this question. A horizontally scalable relational database with strong consistency across regions and no manual sharding. Why the correct answer wins: Bigtable's row-key-ordered wide-column model handles that write rate at the lowest cost per write, while the relational options carry transaction and query overhead the workload does not use.

### Question 24 — A

Answer: Use Spanner for the globally distributed relational workload. Spanner provides externally consistent transactions with horizontal scale and managed multi-region placement, which the single-machine options cannot offer and the wide-column store does not transact across rows. A horizontally scalable relational database with strong consistency across regions and no manual sharding. Local study-map skill 1.11 (SQL and NoSQL Data Model Fit), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 1 (design innovative, scalable, and highly available cloud database solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Correct. A horizontally scalable relational database with strong consistency across regions and no manual sharding. In this case: Spanner provides externally consistent transactions with horizontal scale and managed multi-region placement, which the single-machine options cannot offer and the wide-column store does not transact across rows.
- **B:** Incorrect for this question. A wide-column NoSQL service built for very high write and read rates over a sparse, row-key-ordered model. Why the correct answer wins: Spanner provides externally consistent transactions with horizontal scale and managed multi-region placement, which the single-machine options cannot offer and the wide-column store does not transact across rows.
- **C:** Incorrect for this question. A managed MySQL, PostgreSQL, or SQL Server instance with Google-operated backups, patching, and failover. Why the correct answer wins: Spanner provides externally consistent transactions with horizontal scale and managed multi-region placement, which the single-machine options cannot offer and the wide-column store does not transact across rows.
- **D:** Incorrect for this question. A document database with automatic multi-region replication, offline client support, and index-driven queries. Why the correct answer wins: Spanner provides externally consistent transactions with horizontal scale and managed multi-region placement, which the single-machine options cannot offer and the wide-column store does not transact across rows.

### Question 25 — C

Answer: Enable the vector extension on PostgreSQL. Enabling the vector extension lets the similarity search run in the same engine as the metadata filter, avoiding a copy into another system or an index that cannot express the predicate. Store embeddings beside relational rows and search them in the same engine. Local study-map skill 1.12 (Vector and Generative AI Requirements), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 1 (design innovative, scalable, and highly available cloud database solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A managed Redis-compatible in-memory store placed in front of the system of record. Why the correct answer wins: Enabling the vector extension lets the similarity search run in the same engine as the metadata filter, avoiding a copy into another system or an index that cannot express the predicate.
- **B:** Incorrect for this question. An index ordered so the filter and sort both resolve without a scan. Why the correct answer wins: Enabling the vector extension lets the similarity search run in the same engine as the metadata filter, avoiding a copy into another system or an index that cannot express the predicate.
- **C:** Correct. Store embeddings beside relational rows and search them in the same engine. In this case: Enabling the vector extension lets the similarity search run in the same engine as the metadata filter, avoiding a copy into another system or an index that cannot express the predicate.
- **D:** Incorrect for this question. Read the operational table from BigQuery without copying it first. Why the correct answer wins: Enabling the vector extension lets the similarity search run in the same engine as the metadata filter, avoiding a copy into another system or an index that cannot express the predicate.

### Question 26 — B

Answer: Use AlloyDB vector search with a ScaNN index. An AlloyDB vector index is built for that scale and latency target, while the generic extension, a composite index, and a cache do not provide approximate nearest-neighbour search at this size. A vector index tuned for large embedding sets on AlloyDB. Local study-map skill 1.12 (Vector and Generative AI Requirements), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 1 (design innovative, scalable, and highly available cloud database solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Store embeddings beside relational rows and search them in the same engine. Why the correct answer wins: An AlloyDB vector index is built for that scale and latency target, while the generic extension, a composite index, and a cache do not provide approximate nearest-neighbour search at this size.
- **B:** Correct. A vector index tuned for large embedding sets on AlloyDB. In this case: An AlloyDB vector index is built for that scale and latency target, while the generic extension, a composite index, and a cache do not provide approximate nearest-neighbour search at this size.
- **C:** Incorrect for this question. Absorb repeated reads in memory so the database sees fewer of them. Why the correct answer wins: An AlloyDB vector index is built for that scale and latency target, while the generic extension, a composite index, and a cache do not provide approximate nearest-neighbour search at this size.
- **D:** Incorrect for this question. An index ordered so the filter and sort both resolve without a scan. Why the correct answer wins: An AlloyDB vector index is built for that scale and latency target, while the generic extension, a composite index, and a cache do not provide approximate nearest-neighbour search at this size.

### Question 27 — A, E

Answers: Stop or delete the idle instance; Reduce the machine type to match observed use. Removing an instance with no traffic and shrinking one that never uses its shape both reduce the bill without touching the workload, whereas a commitment locks in spend and the other options do not address over-provisioning. Remove capacity that serves no traffic. Shrink an instance whose peak fits a smaller shape. Local study-map skill 1.13 (Comparative Cost Analysis Across Databases), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 1 (design innovative, scalable, and highly available cloud database solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Correct. Shrink an instance whose peak fits a smaller shape. In this case: Removing an instance with no traffic and shrinking one that never uses its shape both reduce the bill without touching the workload, whereas a commitment locks in spend and the other options do not address over-provisioning.
- **B:** Incorrect for this question. A one- or three-year commitment that discounts the capacity always in use. Why the correct answer wins: Removing an instance with no traffic and shrinking one that never uses its shape both reduce the bill without touching the workload, whereas a commitment locks in spend and the other options do not address over-provisioning.
- **C:** Incorrect for this question. The automatic discount that applies to long-running Compute Engine usage. Why the correct answer wins: Removing an instance with no traffic and shrinking one that never uses its shape both reduce the bill without touching the workload, whereas a commitment locks in spend and the other options do not address over-provisioning.
- **D:** Incorrect for this question. Avoid a full-disk outage at the cost of unplanned storage growth. Why the correct answer wins: Removing an instance with no traffic and shrinking one that never uses its shape both reduce the bill without touching the workload, whereas a commitment locks in spend and the other options do not address over-provisioning.
- **E:** Correct. Remove capacity that serves no traffic. In this case: Removing an instance with no traffic and shrinking one that never uses its shape both reduce the bill without touching the workload, whereas a commitment locks in spend and the other options do not address over-provisioning.

### Question 28 — C

Answer: Commit to the steady baseline capacity. A commitment discounts capacity that runs continuously, which is exactly this baseline, while scaling schedules and stopping instances apply to variable or idle workloads and sustained-use discounts cover Compute Engine rather than this service. A one- or three-year commitment that discounts the capacity always in use. Local study-map skill 1.13 (Comparative Cost Analysis Across Databases), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 1 (design innovative, scalable, and highly available cloud database solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Match capacity to the daily traffic shape. Why the correct answer wins: A commitment discounts capacity that runs continuously, which is exactly this baseline, while scaling schedules and stopping instances apply to variable or idle workloads and sustained-use discounts cover Compute Engine rather than this service.
- **B:** Incorrect for this question. The automatic discount that applies to long-running Compute Engine usage. Why the correct answer wins: A commitment discounts capacity that runs continuously, which is exactly this baseline, while scaling schedules and stopping instances apply to variable or idle workloads and sustained-use discounts cover Compute Engine rather than this service.
- **C:** Correct. A one- or three-year commitment that discounts the capacity always in use. In this case: A commitment discounts capacity that runs continuously, which is exactly this baseline, while scaling schedules and stopping instances apply to variable or idle workloads and sustained-use discounts cover Compute Engine rather than this service.
- **D:** Incorrect for this question. Remove capacity that serves no traffic. Why the correct answer wins: A commitment discounts capacity that runs continuously, which is exactly this baseline, while scaling schedules and stopping instances apply to variable or idle workloads and sustained-use discounts cover Compute Engine rather than this service.

### Question 29 — A

Answer: Keep the current engine and version. Keeping the current engine avoids rewriting the forty procedures whose vendor-specific behaviour is the real dependency, whereas a heterogeneous path and a manual rewrite take on exactly that risk. A lift of the existing engine with no conversion work, retaining its behaviour and licensing. Local study-map skill 1.14 (Application and Database Dependencies), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 1 (design innovative, scalable, and highly available cloud database solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Correct. A lift of the existing engine with no conversion work, retaining its behaviour and licensing. In this case: Keeping the current engine avoids rewriting the forty procedures whose vendor-specific behaviour is the real dependency, whereas a heterogeneous path and a manual rewrite take on exactly that risk.
- **B:** Incorrect for this question. Port procedural code the conversion tool flags as unsupported. Why the correct answer wins: Keeping the current engine avoids rewriting the forty procedures whose vendor-specific behaviour is the real dependency, whereas a heterogeneous path and a manual rewrite take on exactly that risk.
- **C:** Incorrect for this question. A managed path that converts schema and code from a different source engine. Why the correct answer wins: Keeping the current engine avoids rewriting the forty procedures whose vendor-specific behaviour is the real dependency, whereas a heterogeneous path and a manual rewrite take on exactly that risk.
- **D:** Incorrect for this question. Weigh engine compatibility and code rewrite effort before selecting a destination. Why the correct answer wins: Keeping the current engine avoids rewriting the forty procedures whose vendor-specific behaviour is the real dependency, whereas a heterogeneous path and a manual rewrite take on exactly that risk.

### Question 30 — A, B

Answers: Place the instance in the required region; Enforce the location with an organization policy. Placing the instance in the required region settles today's data location, and an organization policy constraint prevents a future project from choosing a different one. A location choice that keeps data inside the regulated boundary. A constraint that keeps database resources inside the approved regions. Local study-map skill 1.15 (Regulatory, Compliance, and Organization Policy), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 1 (design innovative, scalable, and highly available cloud database solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Correct. A constraint that keeps database resources inside the approved regions. In this case: Placing the instance in the required region settles today's data location, and an organization policy constraint prevents a future project from choosing a different one.
- **B:** Correct. A location choice that keeps data inside the regulated boundary. In this case: Placing the instance in the required region settles today's data location, and an organization policy constraint prevents a future project from choosing a different one.
- **C:** Incorrect for this question. Absorb repeated reads in memory so the database sees fewer of them. Why the correct answer wins: Placing the instance in the required region settles today's data location, and an organization policy constraint prevents a future project from choosing a different one.
- **D:** Incorrect for this question. Default encryption at rest with keys the customer neither sees nor manages. Why the correct answer wins: Placing the instance in the required region settles today's data location, and an organization policy constraint prevents a future project from choosing a different one.
- **E:** Incorrect for this question. A topology that places replicas in separate regions for regional-failure tolerance. Why the correct answer wins: Placing the instance in the required region settles today's data location, and an organization policy constraint prevents a future project from choosing a different one.

### Question 31 — C

Answer: Add the projects to a VPC Service Controls perimeter. A VPC Service Controls perimeter blocks data movement outside the approved projects even for an authorized identity, while the copy-based options create exactly the exposure the policy forbids. A boundary that blocks data exfiltration even from an authorized identity. Local study-map skill 1.15 (Regulatory, Compliance, and Organization Policy), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 1 (design innovative, scalable, and highly available cloud database solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Read the operational table from BigQuery without copying it first. Why the correct answer wins: A VPC Service Controls perimeter blocks data movement outside the approved projects even for an authorized identity, while the copy-based options create exactly the exposure the policy forbids.
- **B:** Incorrect for this question. Copy the analytical slice into the warehouse on a schedule. Why the correct answer wins: A VPC Service Controls perimeter blocks data movement outside the approved projects even for an authorized identity, while the copy-based options create exactly the exposure the policy forbids.
- **C:** Correct. A boundary that blocks data exfiltration even from an authorized identity. In this case: A VPC Service Controls perimeter blocks data movement outside the approved projects even for an authorized identity, while the copy-based options create exactly the exposure the policy forbids.
- **D:** Incorrect for this question. Keep an analytics copy current by applying change data capture. Why the correct answer wins: A VPC Service Controls perimeter blocks data movement outside the approved projects even for an authorized identity, while the copy-based options create exactly the exposure the policy forbids.

### Question 32 — A

Answer: Query the source through BigQuery federated queries. A federated query reads the Oracle tables in place and joins them to BigQuery data without a copy, whereas streaming, export, and a hybrid link all rely on moving or duplicating the source rows. Read the operational table from BigQuery without copying it first. Local study-map skill 1.16 (Federation, Exports, and Hybrid Spans), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 1 (design innovative, scalable, and highly available cloud database solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Correct. Read the operational table from BigQuery without copying it first. In this case: A federated query reads the Oracle tables in place and joins them to BigQuery data without a copy, whereas streaming, export, and a hybrid link all rely on moving or duplicating the source rows.
- **B:** Incorrect for this question. Interconnect the remaining on-premises system rather than moving it. Why the correct answer wins: A federated query reads the Oracle tables in place and joins them to BigQuery data without a copy, whereas streaming, export, and a hybrid link all rely on moving or duplicating the source rows.
- **C:** Incorrect for this question. Keep an analytics copy current by applying change data capture. Why the correct answer wins: A federated query reads the Oracle tables in place and joins them to BigQuery data without a copy, whereas streaming, export, and a hybrid link all rely on moving or duplicating the source rows.
- **D:** Incorrect for this question. Copy the analytical slice into the warehouse on a schedule. Why the correct answer wins: A federated query reads the Oracle tables in place and joins them to BigQuery data without a copy, whereas streaming, export, and a hybrid link all rely on moving or duplicating the source rows.

### Question 33 — A, C

Answers: Bind access to a Google group; Limit the user to the required schema. Binding to a Google group removes the joiners and leavers problem, and restricting the grant to the named schema keeps the access read-only where it is needed. Manage membership in a group rather than editing bindings per person. Grant access to named objects instead of the whole instance. Local study-map skill 2.1 (IAM for Database Connectivity), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 2 (manage a solution that can span multiple database technologies): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Correct. Manage membership in a group rather than editing bindings per person. In this case: Binding to a Google group removes the joiners and leavers problem, and restricting the grant to the named schema keeps the access read-only where it is needed.
- **B:** Incorrect for this question. Individual accountability at the engine layer rather than a shared login. Why the correct answer wins: Binding to a Google group removes the joiners and leavers problem, and restricting the grant to the named schema keeps the access read-only where it is needed.
- **C:** Correct. Grant access to named objects instead of the whole instance. In this case: Binding to a Google group removes the joiners and leavers problem, and restricting the grant to the named schema keeps the access read-only where it is needed.
- **D:** Incorrect for this question. A single credential used by every workload that touches the database. Why the correct answer wins: Binding to a Google group removes the joiners and leavers problem, and restricting the grant to the named schema keeps the access read-only where it is needed.
- **E:** Incorrect for this question. A broad legacy role that can change most resources in the project. Why the correct answer wins: Binding to a Google group removes the joiners and leavers problem, and restricting the grant to the named schema keeps the access read-only where it is needed.

### Question 34 — C

Answer: Grant the predefined database role. The predefined client role carries permission to connect without administrative control, whereas an editor-level role or a broad custom grant keeps the destructive capability. A Google-managed role that carries the permissions the operator needs. Local study-map skill 2.1 (IAM for Database Connectivity), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 2 (manage a solution that can span multiple database technologies): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A role built from an explicit permission list. Why the correct answer wins: The predefined client role carries permission to connect without administrative control, whereas an editor-level role or a broad custom grant keeps the destructive capability.
- **B:** Incorrect for this question. A single credential used by every workload that touches the database. Why the correct answer wins: The predefined client role carries permission to connect without administrative control, whereas an editor-level role or a broad custom grant keeps the destructive capability.
- **C:** Correct. A Google-managed role that carries the permissions the operator needs. In this case: The predefined client role carries permission to connect without administrative control, whereas an editor-level role or a broad custom grant keeps the destructive capability.
- **D:** Incorrect for this question. A broad legacy role that can change most resources in the project. Why the correct answer wins: The predefined client role carries permission to connect without administrative control, whereas an editor-level role or a broad custom grant keeps the destructive capability.

### Question 35 — C

Answer: Create one database user per person. Separate database users give each engineer a named identity in the audit trail, which a shared login or a single application account cannot provide. Individual accountability at the engine layer rather than a shared login. Local study-map skill 2.2 (Database Users and Authentication), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 2 (manage a solution that can span multiple database technologies): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A workload identity that can be authorized by IAM without a stored password. Why the correct answer wins: Separate database users give each engineer a named identity in the audit trail, which a shared login or a single application account cannot provide.
- **B:** Incorrect for this question. A native database user whose credential must be rotated and stored. Why the correct answer wins: Separate database users give each engineer a named identity in the audit trail, which a shared login or a single application account cannot provide.
- **C:** Correct. Individual accountability at the engine layer rather than a shared login. In this case: Separate database users give each engineer a named identity in the audit trail, which a shared login or a single application account cannot provide.
- **D:** Incorrect for this question. A single credential used by every workload that touches the database. Why the correct answer wins: Separate database users give each engineer a named identity in the audit trail, which a shared login or a single application account cannot provide.

### Question 36 — A

Answer: Add the index the slow query needs. An index on the selective predicate turns the scan into a lookup, which partitioning, caching, or fresh statistics would not fix for this access pattern. Create an index that turns a scan into a lookup for the predicate. Local study-map skill 2.3 (Slow Queries and Missing Indexes), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 2 (manage a solution that can span multiple database technologies): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Correct. Create an index that turns a scan into a lookup for the predicate. In this case: An index on the selective predicate turns the scan into a lookup, which partitioning, caching, or fresh statistics would not fix for this access pattern.
- **B:** Incorrect for this question. Absorb repeated reads in memory so the database sees fewer of them. Why the correct answer wins: An index on the selective predicate turns the scan into a lookup, which partitioning, caching, or fresh statistics would not fix for this access pattern.
- **C:** Incorrect for this question. Give the planner current cardinality so it stops choosing a poor plan. Why the correct answer wins: An index on the selective predicate turns the scan into a lookup, which partitioning, caching, or fresh statistics would not fix for this access pattern.
- **D:** Incorrect for this question. Split one table into ranges so pruning and maintenance act on less data. Why the correct answer wins: An index on the selective predicate turns the scan into a lookup, which partitioning, caching, or fresh statistics would not fix for this access pattern.

### Question 37 — B

Answer: Refresh the table statistics. The estimate is wrong because the planner's statistics are stale, so refreshing them lets it choose a plan that matches the real row counts. Give the planner current cardinality so it stops choosing a poor plan. Local study-map skill 2.3 (Slow Queries and Missing Indexes), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 2 (manage a solution that can span multiple database technologies): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Remove write amplification from an index nothing reads. Why the correct answer wins: The estimate is wrong because the planner's statistics are stale, so refreshing them lets it choose a plan that matches the real row counts.
- **B:** Correct. Give the planner current cardinality so it stops choosing a poor plan. In this case: The estimate is wrong because the planner's statistics are stale, so refreshing them lets it choose a plan that matches the real row counts.
- **C:** Incorrect for this question. Create an index that turns a scan into a lookup for the predicate. Why the correct answer wins: The estimate is wrong because the planner's statistics are stale, so refreshing them lets it choose a plan that matches the real row counts.
- **D:** Incorrect for this question. Give sorts and joins more working memory on the instance. Why the correct answer wins: The estimate is wrong because the planner's statistics are stale, so refreshing them lets it choose a plan that matches the real row counts.

### Question 38 — B

Answer: Batch the writes into fewer round trips. Committing in smaller batches shortens the lock hold time, while killing the session or adding read capacity leaves the single long transaction in place. Cut per-row network and commit overhead in the application. Local study-map skill 2.4 (Locking and Resource Contention), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 2 (manage a solution that can span multiple database technologies): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A pooler that multiplexes many application connections onto few database sessions. Why the correct answer wins: Committing in smaller batches shortens the lock hold time, while killing the session or adding read capacity leaves the single long transaction in place.
- **B:** Correct. Cut per-row network and commit overhead in the application. In this case: Committing in smaller batches shortens the lock hold time, while killing the session or adding read capacity leaves the single long transaction in place.
- **C:** Incorrect for this question. End the blocking transaction so the queue drains. Why the correct answer wins: Committing in smaller batches shortens the lock hold time, while killing the session or adding read capacity leaves the single long transaction in place.
- **D:** Incorrect for this question. Send reads to a copy so the primary keeps its capacity for writes. Why the correct answer wins: Committing in smaller batches shortens the lock hold time, while killing the session or adding read capacity leaves the single long transaction in place.

### Question 39 — B

Answer: Terminate the session that holds the lock. An idle transaction that holds the lock must be ended before the queue can drain, and no query or index change affects a session that is not executing anything. End the blocking transaction so the queue drains. Local study-map skill 2.4 (Locking and Resource Contention), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 2 (manage a solution that can span multiple database technologies): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Give the planner current cardinality so it stops choosing a poor plan. Why the correct answer wins: An idle transaction that holds the lock must be ended before the queue can drain, and no query or index change affects a session that is not executing anything.
- **B:** Correct. End the blocking transaction so the queue drains. In this case: An idle transaction that holds the lock must be ended before the queue can drain, and no query or index change affects a session that is not executing anything.
- **C:** Incorrect for this question. Cut per-row network and commit overhead in the application. Why the correct answer wins: An idle transaction that holds the lock must be ended before the queue can drain, and no query or index change affects a session that is not executing anything.
- **D:** Incorrect for this question. Create an index that turns a scan into a lookup for the predicate. Why the correct answer wins: An idle transaction that holds the lock must be ended before the queue can drain, and no query or index change affects a session that is not executing anything.

### Question 40 — C, D

Answers: Watch CPU, memory, disk, and IOPS together; Use Query Insights to find the heavy statements. Instance vitals show which resource saturates at that hour, and per-query data shows which statements create the load, which together separate cause from correlation. Read the instance-level signals before attributing the symptom to the query. A per-query view of latency, load, and wait events on the instance. Local study-map skill 2.5 (Database Vitals Monitoring), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 2 (manage a solution that can span multiple database technologies): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A single view of health, security, and version posture across database instances. Why the correct answer wins: Instance vitals show which resource saturates at that hour, and per-query data shows which statements create the load, which together separate cause from correlation.
- **B:** Incorrect for this question. Use the assistant to interpret a query plan and propose a change to test. Why the correct answer wins: Instance vitals show which resource saturates at that hour, and per-query data shows which statements create the load, which together separate cause from correlation.
- **C:** Correct. A per-query view of latency, load, and wait events on the instance. In this case: Instance vitals show which resource saturates at that hour, and per-query data shows which statements create the load, which together separate cause from correlation.
- **D:** Correct. Read the instance-level signals before attributing the symptom to the query. In this case: Instance vitals show which resource saturates at that hour, and per-query data shows which statements create the load, which together separate cause from correlation.
- **E:** Incorrect for this question. Export entries to storage whose retention cannot be shortened. Why the correct answer wins: Instance vitals show which resource saturates at that hour, and per-query data shows which statements create the load, which together separate cause from correlation.

### Question 41 — B

Answer: Watch CPU, memory, disk, and IOPS together. The instance monitoring view presents the resource signals together, while query data, fleet posture, and the slow log each answer a narrower question. Read the instance-level signals before attributing the symptom to the query. Local study-map skill 2.5 (Database Vitals Monitoring), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 2 (manage a solution that can span multiple database technologies): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A single view of health, security, and version posture across database instances. Why the correct answer wins: The instance monitoring view presents the resource signals together, while query data, fleet posture, and the slow log each answer a narrower question.
- **B:** Correct. Read the instance-level signals before attributing the symptom to the query. In this case: The instance monitoring view presents the resource signals together, while query data, fleet posture, and the slow log each answer a narrower question.
- **C:** Incorrect for this question. A per-query view of latency, load, and wait events on the instance. Why the correct answer wins: The instance monitoring view presents the resource signals together, while query data, fleet posture, and the slow log each answer a narrower question.
- **D:** Incorrect for this question. The engine log of statements that exceeded the long-query threshold. Why the correct answer wins: The instance monitoring view presents the resource signals together, while query data, fleet posture, and the slow log each answer a narrower question.

### Question 42 — D

Answer: Move the job outside the contention window. Staggering the jobs keeps each operation inside the existing limit, while a quota increase or retries leave the collision that causes the failures. Stagger the work so concurrent operations stop colliding on the same limit. Local study-map skill 2.6 (Quotas and Limits), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 2 (manage a solution that can span multiple database technologies): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Raise the project-level ceiling so the operation is no longer refused. Why the correct answer wins: Staggering the jobs keeps each operation inside the existing limit, while a quota increase or retries leave the collision that causes the failures.
- **B:** Incorrect for this question. Repeat the call after a growing delay so a transient refusal clears. Why the correct answer wins: Staggering the jobs keeps each operation inside the existing limit, while a quota increase or retries leave the collision that causes the failures.
- **C:** Incorrect for this question. A flat-file extract for a downstream loader rather than a restore. Why the correct answer wins: Staggering the jobs keeps each operation inside the existing limit, while a quota increase or retries leave the collision that causes the failures.
- **D:** Correct. Stagger the work so concurrent operations stop colliding on the same limit. In this case: Staggering the jobs keeps each operation inside the existing limit, while a quota increase or retries leave the collision that causes the failures.

### Question 43 — A

Answer: Alert on the database error rate. Alerting on the error rate catches user-visible failure even when resources look healthy, which a generic resource policy or a lag signal would miss. Page on failed statements rather than on resource saturation alone. Local study-map skill 2.7 (Alerts for Errors and Performance), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 2 (manage a solution that can span multiple database technologies): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Correct. Page on failed statements rather than on resource saturation alone. In this case: Alerting on the error rate catches user-visible failure even when resources look healthy, which a generic resource policy or a lag signal would miss.
- **B:** Incorrect for this question. Page when the copy falls behind the primary by more than the budget. Why the correct answer wins: Alerting on the error rate catches user-visible failure even when resources look healthy, which a generic resource policy or a lag signal would miss.
- **C:** Incorrect for this question. Read the instance-level signals before attributing the symptom to the query. Why the correct answer wins: Alerting on the error rate catches user-visible failure even when resources look healthy, which a generic resource policy or a lag signal would miss.
- **D:** Incorrect for this question. A condition that pages a human when the threshold is crossed. Why the correct answer wins: Alerting on the error rate catches user-visible failure even when resources look healthy, which a generic resource policy or a lag signal would miss.

### Question 44 — C

Answer: Build a log-based metric from the error entries. A log-based metric converts the recurring message into a countable signal that can be charted and alerted on. Turn a recurring log pattern into a metric that can be charted and alerted on. Local study-map skill 2.7 (Alerts for Errors and Performance), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 2 (manage a solution that can span multiple database technologies): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. The engine log of statements that exceeded the long-query threshold. Why the correct answer wins: A log-based metric converts the recurring message into a countable signal that can be charted and alerted on.
- **B:** Incorrect for this question. Export entries to storage whose retention cannot be shortened. Why the correct answer wins: A log-based metric converts the recurring message into a countable signal that can be charted and alerted on.
- **C:** Correct. Turn a recurring log pattern into a metric that can be charted and alerted on. In this case: A log-based metric converts the recurring message into a countable signal that can be charted and alerted on.
- **D:** Incorrect for this question. A per-query view of latency, load, and wait events on the instance. Why the correct answer wins: A log-based metric converts the recurring message into a countable signal that can be charted and alerted on.

### Question 45 — B, E

Answers: Clone the instance for the test; Restore to the timestamp before the bad change. A clone validates the recovery path without touching production, and the point-in-time restore then returns the instance to just before the truncation. A copy of the current data created without touching the source. A point-in-time restore that discards the later writes on the same instance. Local study-map skill 2.8 (Backup and Recovery Option Selection), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 2 (manage a solution that can span multiple database technologies): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Keep backups longer so an older restore point remains available. Why the correct answer wins: A clone validates the recovery path without touching production, and the point-in-time restore then returns the instance to just before the truncation.
- **B:** Correct. A point-in-time restore that discards the later writes on the same instance. In this case: A clone validates the recovery path without touching production, and the point-in-time restore then returns the instance to just before the truncation.
- **C:** Incorrect for this question. A portable SQL dump taken with the engine tooling. Why the correct answer wins: A clone validates the recovery path without touching production, and the point-in-time restore then returns the instance to just before the truncation.
- **D:** Incorrect for this question. A snapshot of a table that survives a bad schema or data change. Why the correct answer wins: A clone validates the recovery path without touching production, and the point-in-time restore then returns the instance to just before the truncation.
- **E:** Correct. A copy of the current data created without touching the source. In this case: A clone validates the recovery path without touching production, and the point-in-time restore then returns the instance to just before the truncation.

### Question 46 — B

Answer: Enable point-in-time recovery. Point-in-time recovery replays the log to an arbitrary moment, whereas scheduled backups, dumps, and a longer retention only offer the points where a backup was taken. Continuous log capture that lets the instance return to an arbitrary moment. Local study-map skill 2.8 (Backup and Recovery Option Selection), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 2 (manage a solution that can span multiple database technologies): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Scheduled backups kept for a chosen number of days. Why the correct answer wins: Point-in-time recovery replays the log to an arbitrary moment, whereas scheduled backups, dumps, and a longer retention only offer the points where a backup was taken.
- **B:** Correct. Continuous log capture that lets the instance return to an arbitrary moment. In this case: Point-in-time recovery replays the log to an arbitrary moment, whereas scheduled backups, dumps, and a longer retention only offer the points where a backup was taken.
- **C:** Incorrect for this question. Keep backups longer so an older restore point remains available. Why the correct answer wins: Point-in-time recovery replays the log to an arbitrary moment, whereas scheduled backups, dumps, and a longer retention only offer the points where a backup was taken.
- **D:** Incorrect for this question. A portable SQL dump taken with the engine tooling. Why the correct answer wins: Point-in-time recovery replays the log to an arbitrary moment, whereas scheduled backups, dumps, and a longer retention only offer the points where a backup was taken.

### Question 47 — D

Answer: Export the table into BigQuery. A managed export into BigQuery refreshes the table on a schedule, while a logical dump needs a loader, federation reads the live system, and change capture is built for continuous flow. Copy the analytical slice into the warehouse on a schedule. Local study-map skill 2.9 (Export and Import Configuration), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 2 (manage a solution that can span multiple database technologies): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Keep an analytics copy current by applying change data capture. Why the correct answer wins: A managed export into BigQuery refreshes the table on a schedule, while a logical dump needs a loader, federation reads the live system, and change capture is built for continuous flow.
- **B:** Incorrect for this question. Read the operational table from BigQuery without copying it first. Why the correct answer wins: A managed export into BigQuery refreshes the table on a schedule, while a logical dump needs a loader, federation reads the live system, and change capture is built for continuous flow.
- **C:** Incorrect for this question. A portable SQL dump taken with the engine tooling. Why the correct answer wins: A managed export into BigQuery refreshes the table on a schedule, while a logical dump needs a loader, federation reads the live system, and change capture is built for continuous flow.
- **D:** Correct. Copy the analytical slice into the warehouse on a schedule. In this case: A managed export into BigQuery refreshes the table on a schedule, while a logical dump needs a loader, federation reads the live system, and change capture is built for continuous flow.

### Question 48 — D

Answer: Enable regional high availability with a standby zone. A regional instance replicates synchronously to a standby in another zone and fails over automatically, which satisfies the tight recovery point and recovery time together. A primary and standby in two zones of one region with automatic failover. Local study-map skill 2.10 (RTO, RPO, and Point-in-Time Recovery), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 2 (manage a solution that can span multiple database technologies): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Scheduled backups kept for a chosen number of days. Why the correct answer wins: A regional instance replicates synchronously to a standby in another zone and fails over automatically, which satisfies the tight recovery point and recovery time together.
- **B:** Incorrect for this question. Rebuild the database in the surviving region from the latest backup. Why the correct answer wins: A regional instance replicates synchronously to a standby in another zone and fails over automatically, which satisfies the tight recovery point and recovery time together.
- **C:** Incorrect for this question. A copy in a second region that serves reads and can be promoted. Why the correct answer wins: A regional instance replicates synchronously to a standby in another zone and fails over automatically, which satisfies the tight recovery point and recovery time together.
- **D:** Correct. A primary and standby in two zones of one region with automatic failover. In this case: A regional instance replicates synchronously to a standby in another zone and fails over automatically, which satisfies the tight recovery point and recovery time together.

### Question 49 — C

Answer: Enable point-in-time recovery. Restoring from a point in time within the log window bounds the data loss without standing up a second copy, which the standby-based options require. Continuous log capture that lets the instance return to an arbitrary moment. Local study-map skill 2.10 (RTO, RPO, and Point-in-Time Recovery), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 2 (manage a solution that can span multiple database technologies): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A copy in a second region that serves reads and can be promoted. Why the correct answer wins: Restoring from a point in time within the log window bounds the data loss without standing up a second copy, which the standby-based options require.
- **B:** Incorrect for this question. A primary and standby in two zones of one region with automatic failover. Why the correct answer wins: Restoring from a point in time within the log window bounds the data loss without standing up a second copy, which the standby-based options require.
- **C:** Correct. Continuous log capture that lets the instance return to an arbitrary moment. In this case: Restoring from a point in time within the log window bounds the data loss without standing up a second copy, which the standby-based options require.
- **D:** Incorrect for this question. Trigger a switchover in a test window and observe how long writes are unavailable. Why the correct answer wins: Restoring from a point in time within the log window bounds the data loss without standing up a second copy, which the standby-based options require.

### Question 50 — C

Answer: Apply a row-level retention policy. A row-level retention rule deletes records once the period elapses, while a document TTL, a column-family policy, and archiving each apply to a different product or keep the rows. Delete or expire records once the legal hold period ends. Local study-map skill 2.11 (Data Retention Management), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 2 (manage a solution that can span multiple database technologies): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Expire documents once their usefulness ends. Why the correct answer wins: A row-level retention rule deletes records once the period elapses, while a document TTL, a column-family policy, and archiving each apply to a different product or keep the rows.
- **B:** Incorrect for this question. A rule that drops versions by age or count, which also bounds recovery. Why the correct answer wins: A row-level retention rule deletes records once the period elapses, while a document TTL, a column-family policy, and archiving each apply to a different product or keep the rows.
- **C:** Correct. Delete or expire records once the legal hold period ends. In this case: A row-level retention rule deletes records once the period elapses, while a document TTL, a column-family policy, and archiving each apply to a different product or keep the rows.
- **D:** Incorrect for this question. Move aged, rarely read rows out of the hot table into Cloud Storage or BigQuery. Why the correct answer wins: A row-level retention rule deletes records once the period elapses, while a document TTL, a column-family policy, and archiving each apply to a different product or keep the rows.

### Question 51 — A

Answer: Add a read replica for the read traffic. Serving reads from a replica removes that load from the primary, whereas a bigger primary or sharding pays for capacity the write path does not need. Send reads to a copy so the primary keeps its capacity for writes. Local study-map skill 2.12 (Scaling Up Versus Scaling Out), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 2 (manage a solution that can span multiple database technologies): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Correct. Send reads to a copy so the primary keeps its capacity for writes. In this case: Serving reads from a replica removes that load from the primary, whereas a bigger primary or sharding pays for capacity the write path does not need.
- **B:** Incorrect for this question. Raise provisioned compute in 1000-unit node steps or 100-unit increments. Why the correct answer wins: Serving reads from a replica removes that load from the primary, whereas a bigger primary or sharding pays for capacity the write path does not need.
- **C:** Incorrect for this question. Move the instance to a larger shape so more vCPU and memory serve the same data. Why the correct answer wins: Serving reads from a replica removes that load from the primary, whereas a bigger primary or sharding pays for capacity the write path does not need.
- **D:** Incorrect for this question. Split rows by a key so each instance owns a subset of the workload. Why the correct answer wins: Serving reads from a replica removes that load from the primary, whereas a bigger primary or sharding pays for capacity the write path does not need.

### Question 52 — B

Answer: Partition the large table. Partitioning splits the table so maintenance and pruning act on smaller ranges, while an index or a larger instance leaves one indivisible object to maintain. Split one table into ranges so pruning and maintenance act on less data. Local study-map skill 2.12 (Scaling Up Versus Scaling Out), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 2 (manage a solution that can span multiple database technologies): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Create an index that turns a scan into a lookup for the predicate. Why the correct answer wins: Partitioning splits the table so maintenance and pruning act on smaller ranges, while an index or a larger instance leaves one indivisible object to maintain.
- **B:** Correct. Split one table into ranges so pruning and maintenance act on less data. In this case: Partitioning splits the table so maintenance and pruning act on smaller ranges, while an index or a larger instance leaves one indivisible object to maintain.
- **C:** Incorrect for this question. Send reads to a copy so the primary keeps its capacity for writes. Why the correct answer wins: Partitioning splits the table so maintenance and pruning act on smaller ranges, while an index or a larger instance leaves one indivisible object to maintain.
- **D:** Incorrect for this question. Move the instance to a larger shape so more vCPU and memory serve the same data. Why the correct answer wins: Partitioning splits the table so maintenance and pruning act on smaller ranges, while an index or a larger instance leaves one indivisible object to maintain.

### Question 53 — B

Answer: Add a cross-region read replica. A cross-region replica serves reads from the second region without accepting writes, whereas a secondary cluster belongs to AlloyDB and a multi-region configuration changes the primary topology. A copy in a second region that serves reads and can be promoted. Local study-map skill 2.13 (Replication Strategies), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 2 (manage a solution that can span multiple database technologies): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A topology that places replicas in separate regions for regional-failure tolerance. Why the correct answer wins: A cross-region replica serves reads from the second region without accepting writes, whereas a secondary cluster belongs to AlloyDB and a multi-region configuration changes the primary topology.
- **B:** Correct. A copy in a second region that serves reads and can be promoted. In this case: A cross-region replica serves reads from the second region without accepting writes, whereas a secondary cluster belongs to AlloyDB and a multi-region configuration changes the primary topology.
- **C:** Incorrect for this question. A primary and standby in two zones of one region with automatic failover. Why the correct answer wins: A cross-region replica serves reads from the second region without accepting writes, whereas a secondary cluster belongs to AlloyDB and a multi-region configuration changes the primary topology.
- **D:** Incorrect for this question. An AlloyDB cross-region copy that can be promoted to a primary cluster. Why the correct answer wins: A cross-region replica serves reads from the second region without accepting writes, whereas a secondary cluster belongs to AlloyDB and a multi-region configuration changes the primary topology.

### Question 54 — A

Answer: Drop the unused index. Removing indexes nothing reads cuts the write-side maintenance cost, which adding another index or tuning memory would not address. Remove write amplification from an index nothing reads. Local study-map skill 2.14 (Query Optimization for Cost and Performance), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 2 (manage a solution that can span multiple database technologies): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Correct. Remove write amplification from an index nothing reads. In this case: Removing indexes nothing reads cuts the write-side maintenance cost, which adding another index or tuning memory would not address.
- **B:** Incorrect for this question. Create an index that turns a scan into a lookup for the predicate. Why the correct answer wins: Removing indexes nothing reads cuts the write-side maintenance cost, which adding another index or tuning memory would not address.
- **C:** Incorrect for this question. Give sorts and joins more working memory on the instance. Why the correct answer wins: Removing indexes nothing reads cuts the write-side maintenance cost, which adding another index or tuning memory would not address.
- **D:** Incorrect for this question. Split one table into ranges so pruning and maintenance act on less data. Why the correct answer wins: Removing indexes nothing reads cuts the write-side maintenance cost, which adding another index or tuning memory would not address.

### Question 55 — C, E

Answers: Run the task on a managed schedule; Enable automated backups with a retention window. A managed schedule performs the recurring work unattended, and automated backups maintain recovery points without an operator triggering each one. A recurring trigger that performs the work with nobody present. Scheduled backups kept for a chosen number of days. Local study-map skill 2.15 (Automated Maintenance and Scheduled Exports), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 2 (manage a solution that can span multiple database technologies): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A manual checkpoint taken immediately before a risky operation. Why the correct answer wins: A managed schedule performs the recurring work unattended, and automated backups maintain recovery points without an operator triggering each one.
- **B:** Incorrect for this question. Create the resource interactively with no stored definition. Why the correct answer wins: A managed schedule performs the recurring work unattended, and automated backups maintain recovery points without an operator triggering each one.
- **C:** Correct. Scheduled backups kept for a chosen number of days. In this case: A managed schedule performs the recurring work unattended, and automated backups maintain recovery points without an operator triggering each one.
- **D:** Incorrect for this question. Trigger a switchover in a test window and observe how long writes are unavailable. Why the correct answer wins: A managed schedule performs the recurring work unattended, and automated backups maintain recovery points without an operator triggering each one.
- **E:** Correct. A recurring trigger that performs the work with nobody present. In this case: A managed schedule performs the recurring work unattended, and automated backups maintain recovery points without an operator triggering each one.

### Question 56 — D

Answer: Test the upgrade on a clone first. Running the upgrade against a clone exposes application failures while production is untouched, which an in-place upgrade, a backup, or post-change monitoring cannot do. Rehearse the change against a copy before touching production. Local study-map skill 2.15 (Automated Maintenance and Scheduled Exports), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 2 (manage a solution that can span multiple database technologies): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Change the engine version on the running instance during the window. Why the correct answer wins: Running the upgrade against a clone exposes application failures while production is untouched, which an in-place upgrade, a backup, or post-change monitoring cannot do.
- **B:** Incorrect for this question. A recovery point that makes the upgrade reversible in practice. Why the correct answer wins: Running the upgrade against a clone exposes application failures while production is untouched, which an in-place upgrade, a backup, or post-change monitoring cannot do.
- **C:** Incorrect for this question. Compare the signal after cutover against the pre-change baseline. Why the correct answer wins: Running the upgrade against a clone exposes application failures while production is untouched, which an in-place upgrade, a backup, or post-change monitoring cannot do.
- **D:** Correct. Rehearse the change against a copy before touching production. In this case: Running the upgrade against a clone exposes application failures while production is untouched, which an in-place upgrade, a backup, or post-change monitoring cannot do.

### Question 57 — C

Answer: Track the availability signal against the agreed objective. Comparing the availability signal with the agreed objective shows a breached commitment, whereas resource alerts and inventory views do not express the promise. Compare observed service levels with the commitment rather than watching raw resource metrics. Local study-map skill 2.16 (Managed Upgrades and SLA Monitoring), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 2 (manage a solution that can span multiple database technologies): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Read the instance-level signals before attributing the symptom to the query. Why the correct answer wins: Comparing the availability signal with the agreed objective shows a breached commitment, whereas resource alerts and inventory views do not express the promise.
- **B:** Incorrect for this question. A single view of health, security, and version posture across database instances. Why the correct answer wins: Comparing the availability signal with the agreed objective shows a breached commitment, whereas resource alerts and inventory views do not express the promise.
- **C:** Correct. Compare observed service levels with the commitment rather than watching raw resource metrics. In this case: Comparing the availability signal with the agreed objective shows a breached commitment, whereas resource alerts and inventory views do not express the promise.
- **D:** Incorrect for this question. A condition that pages a human when the threshold is crossed. Why the correct answer wins: Comparing the availability signal with the agreed objective shows a breached commitment, whereas resource alerts and inventory views do not express the promise.

### Question 58 — B, C

Answers: Use Database Migration Service for the same engine; Follow a cutover runbook with a rollback step. Continuous replication keeps the target close to the source while the migration runs, and a rehearsed runbook controls the brief freeze and the switch that follow. A managed migration that moves a supported engine to the same engine on Google Cloud. A rehearsed sequence with a named decision point and a way back. Local study-map skill 3.1 (Migration Strategy and Downtime Budget), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 3 (migrate data solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Keep two databases current from application code during the transition. Why the correct answer wins: Continuous replication keeps the target close to the source while the migration runs, and a rehearsed runbook controls the brief freeze and the switch that follow.
- **B:** Correct. A managed migration that moves a supported engine to the same engine on Google Cloud. In this case: Continuous replication keeps the target close to the source while the migration runs, and a rehearsed runbook controls the brief freeze and the switch that follow.
- **C:** Correct. A rehearsed sequence with a named decision point and a way back. In this case: Continuous replication keeps the target close to the source while the migration runs, and a rehearsed runbook controls the brief freeze and the switch that follow.
- **D:** Incorrect for this question. Stop the source, load everything, and start the target in one window. Why the correct answer wins: Continuous replication keeps the target close to the source while the migration runs, and a rehearsed runbook controls the brief freeze and the switch that follow.
- **E:** Incorrect for this question. A bulk load followed by a catch-up pass for the writes made during the load. Why the correct answer wins: Continuous replication keeps the target close to the source while the migration runs, and a rehearsed runbook controls the brief freeze and the switch that follow.

### Question 59 — A

Answer: Accept a scheduled extended outage. A single scheduled window with a stop, load, and start needs no replication machinery, whereas the continuous paths exist to remove downtime the business has already accepted. Stop the source, load everything, and start the target in one window. Local study-map skill 3.1 (Migration Strategy and Downtime Budget), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 3 (migrate data solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Correct. Stop the source, load everything, and start the target in one window. In this case: A single scheduled window with a stop, load, and start needs no replication machinery, whereas the continuous paths exist to remove downtime the business has already accepted.
- **B:** Incorrect for this question. Keep two databases current from application code during the transition. Why the correct answer wins: A single scheduled window with a stop, load, and start needs no replication machinery, whereas the continuous paths exist to remove downtime the business has already accepted.
- **C:** Incorrect for this question. Keep writing back to the original system so a rollback loses nothing. Why the correct answer wins: A single scheduled window with a stop, load, and start needs no replication machinery, whereas the continuous paths exist to remove downtime the business has already accepted.
- **D:** Incorrect for this question. A managed migration that moves a supported engine to the same engine on Google Cloud. Why the correct answer wins: A single scheduled window with a stop, load, and start needs no replication machinery, whereas the continuous paths exist to remove downtime the business has already accepted.

### Question 60 — A

Answer: Write to both systems from the application. Writing to both systems from the application is the remaining way to keep them aligned when the engine cannot publish its change stream. Keep two databases current from application code during the transition. Local study-map skill 3.1 (Migration Strategy and Downtime Budget), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 3 (migrate data solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Correct. Keep two databases current from application code during the transition. In this case: Writing to both systems from the application is the remaining way to keep them aligned when the engine cannot publish its change stream.
- **B:** Incorrect for this question. Stop application writes so the last increment can be applied cleanly. Why the correct answer wins: Writing to both systems from the application is the remaining way to keep them aligned when the engine cannot publish its change stream.
- **C:** Incorrect for this question. Stop the source, load everything, and start the target in one window. Why the correct answer wins: Writing to both systems from the application is the remaining way to keep them aligned when the engine cannot publish its change stream.
- **D:** Incorrect for this question. A managed migration that moves a supported engine to the same engine on Google Cloud. Why the correct answer wins: Writing to both systems from the application is the remaining way to keep them aligned when the engine cannot publish its change stream.

### Question 61 — D

Answer: Use Database Migration Service with schema conversion. Database Migration Service handles the cross-engine move with schema conversion, which a same-engine migration, a change stream, or a dump cannot provide. A managed path that converts schema and code from a different source engine. Local study-map skill 3.2 (Migration Tool Selection), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 3 (migrate data solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A managed migration that moves a supported engine to the same engine on Google Cloud. Why the correct answer wins: Database Migration Service handles the cross-engine move with schema conversion, which a same-engine migration, a change stream, or a dump cannot provide.
- **B:** Incorrect for this question. A bulk load followed by a catch-up pass for the writes made during the load. Why the correct answer wins: Database Migration Service handles the cross-engine move with schema conversion, which a same-engine migration, a change stream, or a dump cannot provide.
- **C:** Incorrect for this question. Change data capture from the source into a Google Cloud target. Why the correct answer wins: Database Migration Service handles the cross-engine move with schema conversion, which a same-engine migration, a change stream, or a dump cannot provide.
- **D:** Correct. A managed path that converts schema and code from a different source engine. In this case: Database Migration Service handles the cross-engine move with schema conversion, which a same-engine migration, a change stream, or a dump cannot provide.

### Question 62 — B

Answer: Stream changes with Datastream. Change data capture streams source changes into BigQuery, while migration tools and dumps are built for moving a database rather than feeding a warehouse. Change data capture from the source into a Google Cloud target. Local study-map skill 3.2 (Migration Tool Selection), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 3 (migrate data solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A bulk load followed by a catch-up pass for the writes made during the load. Why the correct answer wins: Change data capture streams source changes into BigQuery, while migration tools and dumps are built for moving a database rather than feeding a warehouse.
- **B:** Correct. Change data capture from the source into a Google Cloud target. In this case: Change data capture streams source changes into BigQuery, while migration tools and dumps are built for moving a database rather than feeding a warehouse.
- **C:** Incorrect for this question. A managed path that converts schema and code from a different source engine. Why the correct answer wins: Change data capture streams source changes into BigQuery, while migration tools and dumps are built for moving a database rather than feeding a warehouse.
- **D:** Incorrect for this question. Stop the source, load everything, and start the target in one window. Why the correct answer wins: Change data capture streams source changes into BigQuery, while migration tools and dumps are built for moving a database rather than feeding a warehouse.

### Question 63 — A

Answer: Dump, restore, then replay the changes. A dump and restore needs no replication topology when an outage is acceptable, while conversion and reverse replication add work that buys downtime the business does not need. A bulk load followed by a catch-up pass for the writes made during the load. Local study-map skill 3.2 (Migration Tool Selection), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 3 (migrate data solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Correct. A bulk load followed by a catch-up pass for the writes made during the load. In this case: A dump and restore needs no replication topology when an outage is acceptable, while conversion and reverse replication add work that buys downtime the business does not need.
- **B:** Incorrect for this question. A managed path that converts schema and code from a different source engine. Why the correct answer wins: A dump and restore needs no replication topology when an outage is acceptable, while conversion and reverse replication add work that buys downtime the business does not need.
- **C:** Incorrect for this question. Keep writing back to the original system so a rollback loses nothing. Why the correct answer wins: A dump and restore needs no replication topology when an outage is acceptable, while conversion and reverse replication add work that buys downtime the business does not need.
- **D:** Incorrect for this question. Replay the writes made during the bulk load so the target is current at the switch. Why the correct answer wins: A dump and restore needs no replication topology when an outage is acceptable, while conversion and reverse replication add work that buys downtime the business does not need.

### Question 64 — B, C

Answers: Build the schema in a conversion workspace; Rewrite the stored procedures and DML by hand. The conversion workspace produces editable DDL and code for review, and the unsupported procedural code still has to be rewritten by hand before it runs. Convert DDL and code with reviewable, editable output before the load starts. Port procedural code the conversion tool flags as unsupported. Local study-map skill 3.3 (Heterogeneous Schema and DDL Conversion), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 3 (migrate data solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Move clients to the new endpoint as the final cutover action. Why the correct answer wins: The conversion workspace produces editable DDL and code for review, and the unsupported procedural code still has to be rewritten by hand before it runs.
- **B:** Correct. Convert DDL and code with reviewable, editable output before the load starts. In this case: The conversion workspace produces editable DDL and code for review, and the unsupported procedural code still has to be rewritten by hand before it runs.
- **C:** Correct. Port procedural code the conversion tool flags as unsupported. In this case: The conversion workspace produces editable DDL and code for review, and the unsupported procedural code still has to be rewritten by hand before it runs.
- **D:** Incorrect for this question. Set generated-key counters past the highest value so inserts do not collide. Why the correct answer wins: The conversion workspace produces editable DDL and code for review, and the unsupported procedural code still has to be rewritten by hand before it runs.
- **E:** Incorrect for this question. Stop application writes so the last increment can be applied cleanly. Why the correct answer wins: The conversion workspace produces editable DDL and code for review, and the unsupported procedural code still has to be rewritten by hand before it runs.

### Question 65 — A

Answer: Reset the sequences after the bulk load. Generated-key counters must continue past the highest loaded value, which no schema edit, validation run, or traffic switch addresses on its own. Set generated-key counters past the highest value so inserts do not collide. Local study-map skill 3.3 (Heterogeneous Schema and DDL Conversion), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 3 (migrate data solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Correct. Set generated-key counters past the highest value so inserts do not collide. In this case: Generated-key counters must continue past the highest loaded value, which no schema edit, validation run, or traffic switch addresses on its own.
- **B:** Incorrect for this question. Move clients to the new endpoint as the final cutover action. Why the correct answer wins: Generated-key counters must continue past the highest loaded value, which no schema edit, validation run, or traffic switch addresses on its own.
- **C:** Incorrect for this question. Convert DDL and code with reviewable, editable output before the load starts. Why the correct answer wins: Generated-key counters must continue past the highest loaded value, which no schema edit, validation run, or traffic switch addresses on its own.
- **D:** Incorrect for this question. Prove the target holds the same rows as the source before cutover. Why the correct answer wins: Generated-key counters must continue past the highest loaded value, which no schema edit, validation run, or traffic switch addresses on its own.

### Question 66 — C

Answer: Rewrite the stored procedures and DML by hand. Those calls have to be rewritten for the target engine, whereas sequence handling, schema conversion, and dual writes leave the incompatible statements in place. Port procedural code the conversion tool flags as unsupported. Local study-map skill 3.4 (DML and Application Code Conversion), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 3 (migrate data solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Set generated-key counters past the highest value so inserts do not collide. Why the correct answer wins: Those calls have to be rewritten for the target engine, whereas sequence handling, schema conversion, and dual writes leave the incompatible statements in place.
- **B:** Incorrect for this question. Convert DDL and code with reviewable, editable output before the load starts. Why the correct answer wins: Those calls have to be rewritten for the target engine, whereas sequence handling, schema conversion, and dual writes leave the incompatible statements in place.
- **C:** Correct. Port procedural code the conversion tool flags as unsupported. In this case: Those calls have to be rewritten for the target engine, whereas sequence handling, schema conversion, and dual writes leave the incompatible statements in place.
- **D:** Incorrect for this question. Keep two databases current from application code during the transition. Why the correct answer wins: Those calls have to be rewritten for the target engine, whereas sequence handling, schema conversion, and dual writes leave the incompatible statements in place.

### Question 67 — B

Answer: Replay read traffic against the target. Replaying production read traffic against the target exercises the real statements and exposes failures before any user depends on the result. Compare the target answers with production before the switch. Local study-map skill 3.4 (DML and Application Code Conversion), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 3 (migrate data solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Move clients to the new endpoint as the final cutover action. Why the correct answer wins: Replaying production read traffic against the target exercises the real statements and exposes failures before any user depends on the result.
- **B:** Correct. Compare the target answers with production before the switch. In this case: Replaying production read traffic against the target exercises the real statements and exposes failures before any user depends on the result.
- **C:** Incorrect for this question. Prove the target holds the same rows as the source before cutover. Why the correct answer wins: Replaying production read traffic against the target exercises the real statements and exposes failures before any user depends on the result.
- **D:** Incorrect for this question. Stop application writes so the last increment can be applied cleanly. Why the correct answer wins: Replaying production read traffic against the target exercises the real statements and exposes failures before any user depends on the result.

### Question 68 — A

Answer: Use the engine native logical replication. Replicating the engine's own change stream lets the target catch up on writes made during the load, which a dump alone or an unplanned outage cannot do. Replicate row changes from the source using the engine feature itself. Local study-map skill 3.5 (Initial Load and Change Replication), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 3 (migrate data solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Correct. Replicate row changes from the source using the engine feature itself. In this case: Replicating the engine's own change stream lets the target catch up on writes made during the load, which a dump alone or an unplanned outage cannot do.
- **B:** Incorrect for this question. A portable SQL dump taken with the engine tooling. Why the correct answer wins: Replicating the engine's own change stream lets the target catch up on writes made during the load, which a dump alone or an unplanned outage cannot do.
- **C:** Incorrect for this question. Stop the source, load everything, and start the target in one window. Why the correct answer wins: Replicating the engine's own change stream lets the target catch up on writes made during the load, which a dump alone or an unplanned outage cannot do.
- **D:** Incorrect for this question. Keep two databases current from application code during the transition. Why the correct answer wins: Replicating the engine's own change stream lets the target catch up on writes made during the load, which a dump alone or an unplanned outage cannot do.

### Question 69 — C

Answer: Apply the captured change backlog before cutover. The captured backlog has to be applied so the target reflects every change made after the dump started. Replay the writes made during the bulk load so the target is current at the switch. Local study-map skill 3.5 (Initial Load and Change Replication), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 3 (migrate data solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Move clients to the new endpoint as the final cutover action. Why the correct answer wins: The captured backlog has to be applied so the target reflects every change made after the dump started.
- **B:** Incorrect for this question. A portable SQL dump taken with the engine tooling. Why the correct answer wins: The captured backlog has to be applied so the target reflects every change made after the dump started.
- **C:** Correct. Replay the writes made during the bulk load so the target is current at the switch. In this case: The captured backlog has to be applied so the target reflects every change made after the dump started.
- **D:** Incorrect for this question. Prove the target holds the same rows as the source before cutover. Why the correct answer wins: The captured backlog has to be applied so the target reflects every change made after the dump started.

### Question 70 — C, E

Answers: Reconcile row counts and checksums; Replay read traffic against the target. Row and checksum comparison establishes data equality, and replaying production statements establishes that the target answers them the same way. Prove the target holds the same rows as the source before cutover. Compare the target answers with production before the switch. Local study-map skill 3.6 (Validation and Reconciliation), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 3 (migrate data solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A rehearsed sequence with a named decision point and a way back. Why the correct answer wins: Row and checksum comparison establishes data equality, and replaying production statements establishes that the target answers them the same way.
- **B:** Incorrect for this question. Set generated-key counters past the highest value so inserts do not collide. Why the correct answer wins: Row and checksum comparison establishes data equality, and replaying production statements establishes that the target answers them the same way.
- **C:** Correct. Compare the target answers with production before the switch. In this case: Row and checksum comparison establishes data equality, and replaying production statements establishes that the target answers them the same way.
- **D:** Incorrect for this question. Move clients to the new endpoint as the final cutover action. Why the correct answer wins: Row and checksum comparison establishes data equality, and replaying production statements establishes that the target answers them the same way.
- **E:** Correct. Prove the target holds the same rows as the source before cutover. In this case: Row and checksum comparison establishes data equality, and replaying production statements establishes that the target answers them the same way.

### Question 71 — D

Answer: Reconcile row counts and checksums. A value-level comparison of the same aggregates on both systems localises the discrepancy that identical row counts hide. Prove the target holds the same rows as the source before cutover. Local study-map skill 3.6 (Validation and Reconciliation), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 3 (migrate data solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A rehearsed sequence with a named decision point and a way back. Why the correct answer wins: A value-level comparison of the same aggregates on both systems localises the discrepancy that identical row counts hide.
- **B:** Incorrect for this question. Keep two databases current from application code during the transition. Why the correct answer wins: A value-level comparison of the same aggregates on both systems localises the discrepancy that identical row counts hide.
- **C:** Incorrect for this question. Compare the target answers with production before the switch. Why the correct answer wins: A value-level comparison of the same aggregates on both systems localises the discrepancy that identical row counts hide.
- **D:** Correct. Prove the target holds the same rows as the source before cutover. In this case: A value-level comparison of the same aggregates on both systems localises the discrepancy that identical row counts hide.

### Question 72 — B, D

Answers: Follow a cutover runbook with a rollback step; Measure the catch-up rate before choosing the window. A rehearsed sequence names each step and its rollback, and a measured catch-up rate proves the window can actually hold the final increment. A rehearsed sequence with a named decision point and a way back. Size the cutover from how fast changes replay, not from the data volume alone. Local study-map skill 3.7 (Cutover and Fallback Planning), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 3 (migrate data solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Move clients to the new endpoint as the final cutover action. Why the correct answer wins: A rehearsed sequence names each step and its rollback, and a measured catch-up rate proves the window can actually hold the final increment.
- **B:** Correct. Size the cutover from how fast changes replay, not from the data volume alone. In this case: A rehearsed sequence names each step and its rollback, and a measured catch-up rate proves the window can actually hold the final increment.
- **C:** Incorrect for this question. Stop the source, load everything, and start the target in one window. Why the correct answer wins: A rehearsed sequence names each step and its rollback, and a measured catch-up rate proves the window can actually hold the final increment.
- **D:** Correct. A rehearsed sequence with a named decision point and a way back. In this case: A rehearsed sequence names each step and its rollback, and a measured catch-up rate proves the window can actually hold the final increment.
- **E:** Incorrect for this question. Keep two databases current from application code during the transition. Why the correct answer wins: A rehearsed sequence names each step and its rollback, and a measured catch-up rate proves the window can actually hold the final increment.

### Question 73 — A

Answer: Repoint the connection string at the target. Repointing the connection string moves the clients to the validated target, which is the step that completes the switch. Move clients to the new endpoint as the final cutover action. Local study-map skill 3.7 (Cutover and Fallback Planning), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 3 (migrate data solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Correct. Move clients to the new endpoint as the final cutover action. In this case: Repointing the connection string moves the clients to the validated target, which is the step that completes the switch.
- **B:** Incorrect for this question. A rehearsed sequence with a named decision point and a way back. Why the correct answer wins: Repointing the connection string moves the clients to the validated target, which is the step that completes the switch.
- **C:** Incorrect for this question. Stop application writes so the last increment can be applied cleanly. Why the correct answer wins: Repointing the connection string moves the clients to the validated target, which is the step that completes the switch.
- **D:** Incorrect for this question. Keep writing back to the original system so a rollback loses nothing. Why the correct answer wins: Repointing the connection string moves the clients to the validated target, which is the step that completes the switch.

### Question 74 — D

Answer: Freeze writes during the cutover. Stopping application writes on the source leaves a stable point from which the last increment can be applied cleanly. Stop application writes so the last increment can be applied cleanly. Local study-map skill 3.7 (Cutover and Fallback Planning), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 3 (migrate data solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Move clients to the new endpoint as the final cutover action. Why the correct answer wins: Stopping application writes on the source leaves a stable point from which the last increment can be applied cleanly.
- **B:** Incorrect for this question. Stop the source, load everything, and start the target in one window. Why the correct answer wins: Stopping application writes on the source leaves a stable point from which the last increment can be applied cleanly.
- **C:** Incorrect for this question. Keep writing back to the original system so a rollback loses nothing. Why the correct answer wins: Stopping application writes on the source leaves a stable point from which the last increment can be applied cleanly.
- **D:** Correct. Stop application writes so the last increment can be applied cleanly. In this case: Stopping application writes on the source leaves a stable point from which the last increment can be applied cleanly.

### Question 75 — B

Answer: Set up reverse replication to the source. Replicating the new writes back to the source keeps the fallback lossless, while retiring or repointing the source removes the path the rollback needs. Keep writing back to the original system so a rollback loses nothing. Local study-map skill 3.8 (Reverse Replication to the Source), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 3 (migrate data solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Stop application writes so the last increment can be applied cleanly. Why the correct answer wins: Replicating the new writes back to the source keeps the fallback lossless, while retiring or repointing the source removes the path the rollback needs.
- **B:** Correct. Keep writing back to the original system so a rollback loses nothing. In this case: Replicating the new writes back to the source keeps the fallback lossless, while retiring or repointing the source removes the path the rollback needs.
- **C:** Incorrect for this question. Keep the old system read-only for a defined period, then remove it. Why the correct answer wins: Replicating the new writes back to the source keeps the fallback lossless, while retiring or repointing the source removes the path the rollback needs.
- **D:** Incorrect for this question. Move clients to the new endpoint as the final cutover action. Why the correct answer wins: Replicating the new writes back to the source keeps the fallback lossless, while retiring or repointing the source removes the path the rollback needs.

### Question 76 — B

Answer: Set up reverse replication to the source. Replication from the target back to the source is the only way the old system sees writes made after the switch. Keep writing back to the original system so a rollback loses nothing. Local study-map skill 3.8 (Reverse Replication to the Source), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 3 (migrate data solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Keep the old system read-only for a defined period, then remove it. Why the correct answer wins: Replication from the target back to the source is the only way the old system sees writes made after the switch.
- **B:** Correct. Keep writing back to the original system so a rollback loses nothing. In this case: Replication from the target back to the source is the only way the old system sees writes made after the switch.
- **C:** Incorrect for this question. Move clients to the new endpoint as the final cutover action. Why the correct answer wins: Replication from the target back to the source is the only way the old system sees writes made after the switch.
- **D:** Incorrect for this question. Keep two databases current from application code during the transition. Why the correct answer wins: Replication from the target back to the source is the only way the old system sees writes made after the switch.

### Question 77 — B

Answer: Use Database Migration Service with schema conversion. A managed cross-engine migration with continuous replication keeps the window to the final switch, which bulk load or an accepted outage cannot achieve. A managed path that converts schema and code from a different source engine. Local study-map skill 3.9 (Minimizing Downtime During Migration), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 3 (migrate data solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Keep two databases current from application code during the transition. Why the correct answer wins: A managed cross-engine migration with continuous replication keeps the window to the final switch, which bulk load or an accepted outage cannot achieve.
- **B:** Correct. A managed path that converts schema and code from a different source engine. In this case: A managed cross-engine migration with continuous replication keeps the window to the final switch, which bulk load or an accepted outage cannot achieve.
- **C:** Incorrect for this question. Stop the source, load everything, and start the target in one window. Why the correct answer wins: A managed cross-engine migration with continuous replication keeps the window to the final switch, which bulk load or an accepted outage cannot achieve.
- **D:** Incorrect for this question. A bulk load followed by a catch-up pass for the writes made during the load. Why the correct answer wins: A managed cross-engine migration with continuous replication keeps the window to the final switch, which bulk load or an accepted outage cannot achieve.

### Question 78 — A

Answer: Move the job outside the contention window. Moving the cutover away from the predictable surge keeps the catch-up rate inside the window without redesigning the replication path. Stagger the work so concurrent operations stop colliding on the same limit. Local study-map skill 3.9 (Minimizing Downtime During Migration), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 3 (migrate data solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Correct. Stagger the work so concurrent operations stop colliding on the same limit. In this case: Moving the cutover away from the predictable surge keeps the catch-up rate inside the window without redesigning the replication path.
- **B:** Incorrect for this question. Stop the source, load everything, and start the target in one window. Why the correct answer wins: Moving the cutover away from the predictable surge keeps the catch-up rate inside the window without redesigning the replication path.
- **C:** Incorrect for this question. Keep two databases current from application code during the transition. Why the correct answer wins: Moving the cutover away from the predictable surge keeps the catch-up rate inside the window without redesigning the replication path.
- **D:** Incorrect for this question. Size the cutover from how fast changes replay, not from the data volume alone. Why the correct answer wins: Moving the cutover away from the predictable surge keeps the catch-up rate inside the window without redesigning the replication path.

### Question 79 — C

Answer: Decommission the source after a parallel period. Ending the source once the parallel period has proven stable closes the migration and releases the hardware obligation. Keep the old system read-only for a defined period, then remove it. Local study-map skill 3.10 (Source Decommissioning), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 3 (migrate data solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Keep two databases current from application code during the transition. Why the correct answer wins: Ending the source once the parallel period has proven stable closes the migration and releases the hardware obligation.
- **B:** Incorrect for this question. Move clients to the new endpoint as the final cutover action. Why the correct answer wins: Ending the source once the parallel period has proven stable closes the migration and releases the hardware obligation.
- **C:** Correct. Keep the old system read-only for a defined period, then remove it. In this case: Ending the source once the parallel period has proven stable closes the migration and releases the hardware obligation.
- **D:** Incorrect for this question. Keep writing back to the original system so a rollback loses nothing. Why the correct answer wins: Ending the source once the parallel period has proven stable closes the migration and releases the hardware obligation.

### Question 80 — D

Answer: Export the table into BigQuery. Moving the retained history into a warehouse keeps the records queryable after the engine is removed, which the source-side options cannot do once it is gone. Copy the analytical slice into the warehouse on a schedule. Local study-map skill 3.10 (Source Decommissioning), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 3 (migrate data solutions): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Keep writing back to the original system so a rollback loses nothing. Why the correct answer wins: Moving the retained history into a warehouse keeps the records queryable after the engine is removed, which the source-side options cannot do once it is gone.
- **B:** Incorrect for this question. Keep the old system read-only for a defined period, then remove it. Why the correct answer wins: Moving the retained history into a warehouse keeps the records queryable after the engine is removed, which the source-side options cannot do once it is gone.
- **C:** Incorrect for this question. Interconnect the remaining on-premises system rather than moving it. Why the correct answer wins: Moving the retained history into a warehouse keeps the records queryable after the engine is removed, which the source-side options cannot do once it is gone.
- **D:** Correct. Copy the analytical slice into the warehouse on a schedule. In this case: Moving the retained history into a warehouse keeps the records queryable after the engine is removed, which the source-side options cannot do once it is gone.

### Question 81 — B, C

Answers: Provision the instance with a Terraform module; Apply the change through the infrastructure pipeline. Declaring the instance in a module makes the three environments the same artifact, and applying it through the pipeline gives that definition review and history. Declare the database so the same definition creates every environment. Send database changes through review and version control like any other code. Local study-map skill 4.1 (Provisioning Highly Available Instances), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 4 (deploy scalable and highly available databases in Google Cloud): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Rehearse the change against a copy before touching production. Why the correct answer wins: Declaring the instance in a module makes the three environments the same artifact, and applying it through the pipeline gives that definition review and history.
- **B:** Correct. Declare the database so the same definition creates every environment. In this case: Declaring the instance in a module makes the three environments the same artifact, and applying it through the pipeline gives that definition review and history.
- **C:** Correct. Send database changes through review and version control like any other code. In this case: Declaring the instance in a module makes the three environments the same artifact, and applying it through the pipeline gives that definition review and history.
- **D:** Incorrect for this question. Create the resource interactively with no stored definition. Why the correct answer wins: Declaring the instance in a module makes the three environments the same artifact, and applying it through the pipeline gives that definition review and history.
- **E:** Incorrect for this question. Run the new version beside the old one and move traffic when it is proven. Why the correct answer wins: Declaring the instance in a module makes the three environments the same artifact, and applying it through the pipeline gives that definition review and history.

### Question 82 — C

Answer: Provision the instance with a Terraform module. A declared module removes the drift by creating every environment from one definition, which repeated manual creation cannot guarantee. Declare the database so the same definition creates every environment. Local study-map skill 4.1 (Provisioning Highly Available Instances), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 4 (deploy scalable and highly available databases in Google Cloud): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Create the resource interactively with no stored definition. Why the correct answer wins: A declared module removes the drift by creating every environment from one definition, which repeated manual creation cannot guarantee.
- **B:** Incorrect for this question. Rehearse the change against a copy before touching production. Why the correct answer wins: A declared module removes the drift by creating every environment from one definition, which repeated manual creation cannot guarantee.
- **C:** Correct. Declare the database so the same definition creates every environment. In this case: A declared module removes the drift by creating every environment from one definition, which repeated manual creation cannot guarantee.
- **D:** Incorrect for this question. A recovery point that makes the upgrade reversible in practice. Why the correct answer wins: A declared module removes the drift by creating every environment from one definition, which repeated manual creation cannot guarantee.

### Question 83 — D

Answer: Apply the change through the infrastructure pipeline. Applying the definition through the pipeline enforces the required settings on every creation instead of relying on a person to remember them. Send database changes through review and version control like any other code. Local study-map skill 4.1 (Provisioning Highly Available Instances), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 4 (deploy scalable and highly available databases in Google Cloud): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Create the resource interactively with no stored definition. Why the correct answer wins: Applying the definition through the pipeline enforces the required settings on every creation instead of relying on a person to remember them.
- **B:** Incorrect for this question. A single view of health, security, and version posture across database instances. Why the correct answer wins: Applying the definition through the pipeline enforces the required settings on every creation instead of relying on a person to remember them.
- **C:** Incorrect for this question. Compare the signal after cutover against the pre-change baseline. Why the correct answer wins: Applying the definition through the pipeline enforces the required settings on every creation instead of relying on a person to remember them.
- **D:** Correct. Send database changes through review and version control like any other code. In this case: Applying the definition through the pipeline enforces the required settings on every creation instead of relying on a person to remember them.

### Question 84 — C

Answer: Rehearse the promotion in a test project. Promoting the cross-region copy is the only exercise that proves a regional recovery, where a zone failover, a backup, or a dashboard leaves that path untested. Practise the failover that the runbook would perform for real. Local study-map skill 4.2 (Testing High Availability and Disaster Recovery), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 4 (deploy scalable and highly available databases in Google Cloud): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Trigger a switchover in a test window and observe how long writes are unavailable. Why the correct answer wins: Promoting the cross-region copy is the only exercise that proves a regional recovery, where a zone failover, a backup, or a dashboard leaves that path untested.
- **B:** Incorrect for this question. A recovery point that makes the upgrade reversible in practice. Why the correct answer wins: Promoting the cross-region copy is the only exercise that proves a regional recovery, where a zone failover, a backup, or a dashboard leaves that path untested.
- **C:** Correct. Practise the failover that the runbook would perform for real. In this case: Promoting the cross-region copy is the only exercise that proves a regional recovery, where a zone failover, a backup, or a dashboard leaves that path untested.
- **D:** Incorrect for this question. Compare the signal after cutover against the pre-change baseline. Why the correct answer wins: Promoting the cross-region copy is the only exercise that proves a regional recovery, where a zone failover, a backup, or a dashboard leaves that path untested.

### Question 85 — A

Answer: Run a controlled failover test. A controlled failover removes the active zone and observes the takeover, which a restart or a monitoring review does not test. Trigger a switchover in a test window and observe how long writes are unavailable. Local study-map skill 4.2 (Testing High Availability and Disaster Recovery), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 4 (deploy scalable and highly available databases in Google Cloud): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Correct. Trigger a switchover in a test window and observe how long writes are unavailable. In this case: A controlled failover removes the active zone and observes the takeover, which a restart or a monitoring review does not test.
- **B:** Incorrect for this question. Compare the signal after cutover against the pre-change baseline. Why the correct answer wins: A controlled failover removes the active zone and observes the takeover, which a restart or a monitoring review does not test.
- **C:** Incorrect for this question. Apply the configuration change with a brief restart. Why the correct answer wins: A controlled failover removes the active zone and observes the takeover, which a restart or a monitoring review does not test.
- **D:** Incorrect for this question. Block maintenance during a period when an interruption is unacceptable. Why the correct answer wins: A controlled failover removes the active zone and observes the takeover, which a restart or a monitoring review does not test.

### Question 86 — D

Answer: Pre-size the promoted replica for the full load. The standby has to be sized for the full production load, because a replica built for read overflow cannot absorb the write path it inherits. Give the standby enough capacity to carry production alone. Local study-map skill 4.2 (Testing High Availability and Disaster Recovery), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 4 (deploy scalable and highly available databases in Google Cloud): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Trigger a switchover in a test window and observe how long writes are unavailable. Why the correct answer wins: The standby has to be sized for the full production load, because a replica built for read overflow cannot absorb the write path it inherits.
- **B:** Incorrect for this question. Send reads to a copy so the primary keeps its capacity for writes. Why the correct answer wins: The standby has to be sized for the full production load, because a replica built for read overflow cannot absorb the write path it inherits.
- **C:** Incorrect for this question. Keep spare capacity so a failover or a traffic spike does not saturate the instance. Why the correct answer wins: The standby has to be sized for the full production load, because a replica built for read overflow cannot absorb the write path it inherits.
- **D:** Correct. Give the standby enough capacity to carry production alone. In this case: The standby has to be sized for the full production load, because a replica built for read overflow cannot absorb the write path it inherits.

### Question 87 — A, C

Answers: Add a read-only region to the configuration; Choose a multi-region instance configuration. A multi-region configuration provides the placement and consistency, and the read-only region serves nearby reads without taking write leadership. Serve reads near users without making the region a write leader. A topology that places replicas in separate regions for regional-failure tolerance. Local study-map skill 4.3 (Multi-Regional Replication Setup), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 4 (deploy scalable and highly available databases in Google Cloud): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Correct. Serve reads near users without making the region a write leader. In this case: A multi-region configuration provides the placement and consistency, and the read-only region serves nearby reads without taking write leadership.
- **B:** Incorrect for this question. An AlloyDB cross-region copy that can be promoted to a primary cluster. Why the correct answer wins: A multi-region configuration provides the placement and consistency, and the read-only region serves nearby reads without taking write leadership.
- **C:** Correct. A topology that places replicas in separate regions for regional-failure tolerance. In this case: A multi-region configuration provides the placement and consistency, and the read-only region serves nearby reads without taking write leadership.
- **D:** Incorrect for this question. A primary and standby in two zones of one region with automatic failover. Why the correct answer wins: A multi-region configuration provides the placement and consistency, and the read-only region serves nearby reads without taking write leadership.
- **E:** Incorrect for this question. A copy in a second region that serves reads and can be promoted. Why the correct answer wins: A multi-region configuration provides the placement and consistency, and the read-only region serves nearby reads without taking write leadership.

### Question 88 — D

Answer: Choose a multi-region instance configuration. A multi-region configuration places voting replicas so a lost region does not stop writes, while a regional instance or a promoted copy would change the consistency model. A topology that places replicas in separate regions for regional-failure tolerance. Local study-map skill 4.3 (Multi-Regional Replication Setup), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 4 (deploy scalable and highly available databases in Google Cloud): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Rebuild the database in the surviving region from the latest backup. Why the correct answer wins: A multi-region configuration places voting replicas so a lost region does not stop writes, while a regional instance or a promoted copy would change the consistency model.
- **B:** Incorrect for this question. A primary and standby in two zones of one region with automatic failover. Why the correct answer wins: A multi-region configuration places voting replicas so a lost region does not stop writes, while a regional instance or a promoted copy would change the consistency model.
- **C:** Incorrect for this question. A copy in a second region that serves reads and can be promoted. Why the correct answer wins: A multi-region configuration places voting replicas so a lost region does not stop writes, while a regional instance or a promoted copy would change the consistency model.
- **D:** Correct. A topology that places replicas in separate regions for regional-failure tolerance. In this case: A multi-region configuration places voting replicas so a lost region does not stop writes, while a regional instance or a promoted copy would change the consistency model.

### Question 89 — B

Answer: Route the app profile across both clusters. A multi-cluster app profile moves traffic when a cluster becomes unavailable, which pinning clients to one cluster would prevent. A Bigtable app profile that fails over between clusters without a client change. Local study-map skill 4.3 (Multi-Regional Replication Setup), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 4 (deploy scalable and highly available databases in Google Cloud): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A copy in a second region that serves reads and can be promoted. Why the correct answer wins: A multi-cluster app profile moves traffic when a cluster becomes unavailable, which pinning clients to one cluster would prevent.
- **B:** Correct. A Bigtable app profile that fails over between clusters without a client change. In this case: A multi-cluster app profile moves traffic when a cluster becomes unavailable, which pinning clients to one cluster would prevent.
- **C:** Incorrect for this question. Rebuild the database in the surviving region from the latest backup. Why the correct answer wins: A multi-cluster app profile moves traffic when a cluster becomes unavailable, which pinning clients to one cluster would prevent.
- **D:** Incorrect for this question. A Bigtable app profile that keeps a workload on one cluster for predictable latency. Why the correct answer wins: A multi-cluster app profile moves traffic when a cluster becomes unavailable, which pinning clients to one cluster would prevent.

### Question 90 — A

Answer: Send reporting queries to the read replica. Moving the reporting reads to the existing pool uses capacity that is already paid for, whereas growing the pool or the primary adds cost the workload does not need. Separate analytical reads from the write path. Local study-map skill 4.4 (Read Replicas and Read Pools), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 4 (deploy scalable and highly available databases in Google Cloud): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Correct. Separate analytical reads from the write path. In this case: Moving the reporting reads to the existing pool uses capacity that is already paid for, whereas growing the pool or the primary adds cost the workload does not need.
- **B:** Incorrect for this question. Move the instance to a larger shape so more vCPU and memory serve the same data. Why the correct answer wins: Moving the reporting reads to the existing pool uses capacity that is already paid for, whereas growing the pool or the primary adds cost the workload does not need.
- **C:** Incorrect for this question. Grow the AlloyDB read pool that serves read-only connections. Why the correct answer wins: Moving the reporting reads to the existing pool uses capacity that is already paid for, whereas growing the pool or the primary adds cost the workload does not need.
- **D:** Incorrect for this question. Absorb repeated reads in memory so the database sees fewer of them. Why the correct answer wins: Moving the reporting reads to the existing pool uses capacity that is already paid for, whereas growing the pool or the primary adds cost the workload does not need.

### Question 91 — A

Answer: Send reporting queries to the read replica. Sending reporting reads to a replica moves that load off the primary, while caching, partitioning, or more disk leaves the queries on the same instance. Separate analytical reads from the write path. Local study-map skill 4.4 (Read Replicas and Read Pools), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 4 (deploy scalable and highly available databases in Google Cloud): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Correct. Separate analytical reads from the write path. In this case: Sending reporting reads to a replica moves that load off the primary, while caching, partitioning, or more disk leaves the queries on the same instance.
- **B:** Incorrect for this question. Buy more storage so the attached disk also yields more IOPS and throughput. Why the correct answer wins: Sending reporting reads to a replica moves that load off the primary, while caching, partitioning, or more disk leaves the queries on the same instance.
- **C:** Incorrect for this question. Split one table into ranges so pruning and maintenance act on less data. Why the correct answer wins: Sending reporting reads to a replica moves that load off the primary, while caching, partitioning, or more disk leaves the queries on the same instance.
- **D:** Incorrect for this question. Absorb repeated reads in memory so the database sees fewer of them. Why the correct answer wins: Sending reporting reads to a replica moves that load off the primary, while caching, partitioning, or more disk leaves the queries on the same instance.

### Question 92 — C

Answer: Apply the change through the infrastructure pipeline. Applying database changes through the existing pipeline gives them review, history, and the same promotion path as the rest of the system. Send database changes through review and version control like any other code. Local study-map skill 4.5 (Automating Database Provisioning), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 4 (deploy scalable and highly available databases in Google Cloud): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A single view of health, security, and version posture across database instances. Why the correct answer wins: Applying database changes through the existing pipeline gives them review, history, and the same promotion path as the rest of the system.
- **B:** Incorrect for this question. Rehearse the change against a copy before touching production. Why the correct answer wins: Applying database changes through the existing pipeline gives them review, history, and the same promotion path as the rest of the system.
- **C:** Correct. Send database changes through review and version control like any other code. In this case: Applying database changes through the existing pipeline gives them review, history, and the same promotion path as the rest of the system.
- **D:** Incorrect for this question. Declare the database so the same definition creates every environment. Why the correct answer wins: Applying database changes through the existing pipeline gives them review, history, and the same promotion path as the rest of the system.

### Question 93 — D

Answer: Provision the instance with a Terraform module. A module parameterised per customer produces identical instances from one definition, which manual creation cannot sustain at that volume. Declare the database so the same definition creates every environment. Local study-map skill 4.5 (Automating Database Provisioning), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 4 (deploy scalable and highly available databases in Google Cloud): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A recovery point that makes the upgrade reversible in practice. Why the correct answer wins: A module parameterised per customer produces identical instances from one definition, which manual creation cannot sustain at that volume.
- **B:** Incorrect for this question. Create the resource interactively with no stored definition. Why the correct answer wins: A module parameterised per customer produces identical instances from one definition, which manual creation cannot sustain at that volume.
- **C:** Incorrect for this question. Run the new version beside the old one and move traffic when it is proven. Why the correct answer wins: A module parameterised per customer produces identical instances from one definition, which manual creation cannot sustain at that volume.
- **D:** Correct. Declare the database so the same definition creates every environment. In this case: A module parameterised per customer produces identical instances from one definition, which manual creation cannot sustain at that volume.

### Question 94 — B

Answer: Alert when the instance is unreachable. An alert on the database's reachability would have reported the failover before users did, whereas the other options are tests, backups, and inventory views. A liveness signal that fires before users report the outage. Local study-map skill 4.6 (Monitoring Highly Available Databases), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 4 (deploy scalable and highly available databases in Google Cloud): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A single view of health, security, and version posture across database instances. Why the correct answer wins: An alert on the database's reachability would have reported the failover before users did, whereas the other options are tests, backups, and inventory views.
- **B:** Correct. A liveness signal that fires before users report the outage. In this case: An alert on the database's reachability would have reported the failover before users did, whereas the other options are tests, backups, and inventory views.
- **C:** Incorrect for this question. A recovery point that makes the upgrade reversible in practice. Why the correct answer wins: An alert on the database's reachability would have reported the failover before users did, whereas the other options are tests, backups, and inventory views.
- **D:** Incorrect for this question. Trigger a switchover in a test window and observe how long writes are unavailable. Why the correct answer wins: An alert on the database's reachability would have reported the failover before users did, whereas the other options are tests, backups, and inventory views.

### Question 95 — B

Answer: Create an alerting policy on the metric. An alerting policy on the failover and instance-state signals notifies the team automatically, which dashboards and query views require someone to look. A condition that pages a human when the threshold is crossed. Local study-map skill 4.6 (Monitoring Highly Available Databases), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 4 (deploy scalable and highly available databases in Google Cloud): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A single view of health, security, and version posture across database instances. Why the correct answer wins: An alerting policy on the failover and instance-state signals notifies the team automatically, which dashboards and query views require someone to look.
- **B:** Correct. A condition that pages a human when the threshold is crossed. In this case: An alerting policy on the failover and instance-state signals notifies the team automatically, which dashboards and query views require someone to look.
- **C:** Incorrect for this question. A per-query view of latency, load, and wait events on the instance. Why the correct answer wins: An alerting policy on the failover and instance-state signals notifies the team automatically, which dashboards and query views require someone to look.
- **D:** Incorrect for this question. Read the instance-level signals before attributing the symptom to the query. Why the correct answer wins: An alerting policy on the failover and instance-state signals notifies the team automatically, which dashboards and query views require someone to look.

### Question 96 — B

Answer: Promote the cross-region replica during the outage. Promoting the existing replica preserves the recent writes and meets the hour, while a restore loses more data and takes longer. Turn the replica into an independent primary so the application can resume writes. Local study-map skill 4.7 (Regional Failover Mechanics), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 4 (deploy scalable and highly available databases in Google Cloud): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A primary and standby in two zones of one region with automatic failover. Why the correct answer wins: Promoting the existing replica preserves the recent writes and meets the hour, while a restore loses more data and takes longer.
- **B:** Correct. Turn the replica into an independent primary so the application can resume writes. In this case: Promoting the existing replica preserves the recent writes and meets the hour, while a restore loses more data and takes longer.
- **C:** Incorrect for this question. Rebuild the database in the surviving region from the latest backup. Why the correct answer wins: Promoting the existing replica preserves the recent writes and meets the hour, while a restore loses more data and takes longer.
- **D:** Incorrect for this question. A point-in-time restore that discards the later writes on the same instance. Why the correct answer wins: Promoting the existing replica preserves the recent writes and meets the hour, while a restore loses more data and takes longer.

### Question 97 — B

Answer: Fence the old primary before promotion. The former primary has to be stopped from accepting writes so two instances cannot both claim to be the primary. Local study-map skill 4.7 (Regional Failover Mechanics), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 4 (deploy scalable and highly available databases in Google Cloud): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Keep writing back to the original system so a rollback loses nothing. Why the correct answer wins: The former primary has to be stopped from accepting writes so two instances cannot both claim to be the primary.
- **B:** Correct. In this case: The former primary has to be stopped from accepting writes so two instances cannot both claim to be the primary.
- **C:** Incorrect for this question. A rehearsed sequence with a named decision point and a way back. Why the correct answer wins: The former primary has to be stopped from accepting writes so two instances cannot both claim to be the primary.
- **D:** Incorrect for this question. Stop application writes so the last increment can be applied cleanly. Why the correct answer wins: The former primary has to be stopped from accepting writes so two instances cannot both claim to be the primary.

### Question 98 — D

Answer: Use the language connector with IAM credentials. Use of the language connector resolves the instance to its current location, whereas a fixed address, an allowlist, or a pooler leaves the stale endpoint. A client library that resolves the instance and authorizes the connection with IAM. Local study-map skill 4.8 (Connection Routing and Load Balancing), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 4 (deploy scalable and highly available databases in Google Cloud): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A pooler that multiplexes many application connections onto few database sessions. Why the correct answer wins: Use of the language connector resolves the instance to its current location, whereas a fixed address, an allowlist, or a pooler leaves the stale endpoint.
- **B:** Incorrect for this question. Move clients to the new endpoint as the final cutover action. Why the correct answer wins: Use of the language connector resolves the instance to its current location, whereas a fixed address, an allowlist, or a pooler leaves the stale endpoint.
- **C:** Incorrect for this question. A public-IP allowlist that admits the caller range. Why the correct answer wins: Use of the language connector resolves the instance to its current location, whereas a fixed address, an allowlist, or a pooler leaves the stale endpoint.
- **D:** Correct. A client library that resolves the instance and authorizes the connection with IAM. In this case: Use of the language connector resolves the instance to its current location, whereas a fixed address, an allowlist, or a pooler leaves the stale endpoint.

### Question 99 — D

Answer: Pre-size the promoted replica for the full load. A standby that cannot carry the full write load is not a recovery plan, so it has to be sized for production before it is needed. Give the standby enough capacity to carry production alone. Local study-map skill 4.9 (Failover Capacity Headroom), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 4 (deploy scalable and highly available databases in Google Cloud): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Keep spare capacity so a failover or a traffic spike does not saturate the instance. Why the correct answer wins: A standby that cannot carry the full write load is not a recovery plan, so it has to be sized for production before it is needed.
- **B:** Incorrect for this question. Raise provisioned compute in 1000-unit node steps or 100-unit increments. Why the correct answer wins: A standby that cannot carry the full write load is not a recovery plan, so it has to be sized for production before it is needed.
- **C:** Incorrect for this question. Grow the AlloyDB read pool that serves read-only connections. Why the correct answer wins: A standby that cannot carry the full write load is not a recovery plan, so it has to be sized for production before it is needed.
- **D:** Correct. Give the standby enough capacity to carry production alone. In this case: A standby that cannot carry the full write load is not a recovery plan, so it has to be sized for production before it is needed.

### Question 100 — A

Answer: Reserve headroom above the measured peak. Headroom above the measured peak is what lets the surviving instance absorb the failed one's traffic at the same latency. Keep spare capacity so a failover or a traffic spike does not saturate the instance. Local study-map skill 4.9 (Failover Capacity Headroom), mapped to the official guide: Google Cloud Professional Cloud Database Engineer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Database Engineer exam guide section 4 (deploy scalable and highly available databases in Google Cloud): https://services.google.com/fh/files/misc/professional_cloud_database_engineer_exam_guide_english.pdf.

- **A:** Correct. Keep spare capacity so a failover or a traffic spike does not saturate the instance. In this case: Headroom above the measured peak is what lets the surviving instance absorb the failed one's traffic at the same latency.
- **B:** Incorrect for this question. Shrink an instance whose peak fits a smaller shape. Why the correct answer wins: Headroom above the measured peak is what lets the surviving instance absorb the failed one's traffic at the same latency.
- **C:** Incorrect for this question. Send reads to a copy so the primary keeps its capacity for writes. Why the correct answer wins: Headroom above the measured peak is what lets the surviving instance absorb the failed one's traffic at the same latency.
- **D:** Incorrect for this question. Match capacity to the daily traffic shape. Why the correct answer wins: Headroom above the measured peak is what lets the surviving instance absorb the failed one's traffic at the same latency.
