# Google Cloud Professional Cloud Architect — Full-Length Mock Exam 4

Professional Cloud Architect · 100 questions · expanded practice bank · passing score not published

Blueprint-weighted mock exam. Item mix: 84 multiple-choice (selection count stated where needed), 16 multi-select, and 4 case studies of 5 questions. 8 of the multiple-choice items ask you to choose the correct candidate sequence. The live exam publishes 50-60 questions and two case studies worth 20-30 per cent of the score; this set is larger on purpose and cannot reproduce the split-screen case-study panel, drag-and-drop ordering, or lab tasks. See the README for the exact fidelity boundary.

Original educational content, not actual, recalled, or copied Google exam items.

## Questions

### 1. A cost-reduction programme needs a number that proves it worked. What should be fixed first?

Domain: Designing and planning a cloud solution architecture

- A. Act on the Recommender suggestions
- B. Publish a shared dashboard
- C. Define the baseline and target as a KPI with an owner
- D. Export billing to BigQuery and review it per label

### 2. The board compares two designs with different staffing models. What should be produced?

Domain: Designing and planning a cloud solution architecture

- A. Build a three-year total cost of ownership model
- B. Set a budget with alert thresholds
- C. Export billing to BigQuery and review it per label
- D. Buy committed use discounts for the steady baseline

### 3. A three-year commitment is proposed and the board asks what happens afterwards. What must the design include?

Domain: Designing and planning a cloud solution architecture

- A. Build a three-year total cost of ownership model
- B. Tag the resources with labels for cost reporting
- C. Set a budget with alert thresholds
- D. Document the exit plan and data portability

### 4. A retailer must state the acceptable loss during a regional failure and who owns it. Which two artefacts settle that? Select two.

Domain: Designing and planning a cloud solution architecture

- A. Set the RPO and RTO with the business owner
- B. Tag the resources with labels for cost reporting
- C. Put the recovery commitment in the contract
- D. Publish a shared dashboard
- E. Act on the Recommender suggestions

### 5. The order database must fail over without an operator restarting it. What should be enabled?

Domain: Designing and planning a cloud solution architecture

- A. Add a read replica and route reads to it
- B. Enable Cloud SQL high availability with a standby
- C. Use Bigtable
- D. Use Memorystore

### 6. The storefront must keep selling during a regional loss with no failover decision. Which two pieces are required? Select two.

Domain: Designing and planning a cloud solution architecture

- A. Run active-active across two regions
- B. Use backup and restore
- C. Enable Cloud CDN on the backend
- D. Replicate the data to the second region
- E. Run a pilot-light standby

### 7. Marketing, fulfilment, and data each run their own network and must reach a shared hub. What should be built?

Domain: Designing and planning a cloud solution architecture

- A. Deploy Cloud NAT for outbound traffic
- B. Build a Network Connectivity Center hub
- C. Peer the two VPC networks
- D. Create a DNS peering zone

### 8. A payment provider must reach an internal service privately. Which two designs allow that? Select two.

Domain: Designing and planning a cloud solution architecture

- A. Deploy Cloud NAT for outbound traffic
- B. Issue a short-lived signed URL
- C. Publish the service through Private Service Connect
- D. Peer the two VPC networks
- E. Enable Cloud CDN on the backend

### 9. Product images are stored once and fetched from four continents. What should sit in front of the bucket?

Domain: Designing and planning a cloud solution architecture

- A. Deploy Cloud NAT for outbound traffic
- B. Enable Cloud CDN on the backend
- C. Use an internal passthrough load balancer
- D. Use gcloud storage commands

### 10. Catalogue images are hot at launch and cold a month later, unpredictably. What should be enabled?

Domain: Designing and planning a cloud solution architecture

- A. Store the objects in Standard storage class
- B. Enable Autoclass on the bucket
- C. Add a lifecycle rule that transitions and then deletes
- D. Store the objects in Nearline storage class

### 11. Object temperature is unpredictable, and anything older than three years must go. Which two settings apply? Select two.

Domain: Designing and planning a cloud solution architecture

- A. Mount a Filestore instance for the shared file path
- B. Enable Autoclass on the bucket
- C. Use local SSD for the scratch space
- D. Store the objects in Archive storage class
- E. Add a lifecycle rule that transitions and then deletes

### 12. A storefront service is idle overnight and must scale to zero. What should be used?

Domain: Designing and planning a cloud solution architecture

- A. Use GKE Standard with a node pool per workload shape
- B. Run the legacy stack on Google Cloud VMware Engine
- C. Use a managed instance group with autoscaling
- D. Deploy the service on Cloud Run

### 13. A price-comparison job needs 2,000 cores for an hour each morning. What should be used?

Domain: Designing and planning a cloud solution architecture

- A. Use a managed instance group with autoscaling
- B. Deploy the service on Cloud Run
- C. Submit the work as a Batch job
- D. Use GKE Standard with a node pool per workload shape

### 14. Analysts must scan a 300 TB event table with no infrastructure to size. What should be used?

Domain: Designing and planning a cloud solution architecture

- A. Use Bigtable
- B. Use Firestore
- C. Use Cloud SQL
- D. Load the data into BigQuery

### 15. Dashboards must answer in under a second, and the query volume is steady all day. Which two choices apply? Select two.

Domain: Designing and planning a cloud solution architecture

- A. Reserve BigQuery BI Engine capacity
- B. Buy BigQuery slot commitments with autoscaling
- C. Stream rows with the legacy insertAll call
- D. Leave the project on on-demand pricing
- E. Build the dashboard in Looker Studio

### 16. A weekly Spark aggregation is the only Spark workload and nobody wants to size a cluster. What should be used?

Domain: Designing and planning a cloud solution architecture

- A. Use Dataproc Serverless
- B. Use a Dataproc cluster
- C. Use Managed Service for Apache Airflow
- D. Use Dataflow

### 17. A churn score is needed for 12 million readers once a night. What should be used?

Domain: Designing and planning a cloud solution architecture

- A. Enable model monitoring on the endpoint
- B. Size the training on AI Hypercomputer with TPUs
- C. Deploy to an online prediction endpoint
- D. Run batch prediction

### 18. Product pages must answer shopper questions from the catalogue with citations. What should be used?

Domain: Designing and planning a cloud solution architecture

- A. Index the corpus with Vertex AI Search
- B. Use Document AI with a specialised processor
- C. Use the Translation API
- D. Use the Vision API for the images

### 19. The estate must be sized before a cost model can be trusted. What should be used?

Domain: Designing and planning a cloud solution architecture

- A. Convert the VMs with Migrate to Containers
- B. Use Database Migration Service
- C. Assess the estate in Migration Center
- D. Copy the files with Storage Transfer Service

### 20. A retailer must meet a recovery objective it has promised to its board. Which sequence is correct?

Domain: Designing and planning a cloud solution architecture

- A. Choose the DR pattern → fail over in a game day → set the RTO and RPO targets → build the standby environment
- B. Set the RTO and RPO targets → choose the DR pattern that meets them → build and replicate the standby environment → fail over in a game day and record the result
- C. Build and replicate the standby environment → choose the DR pattern → set the RTO and RPO targets → fail over in a game day
- D. Fail over in a game day → set the RTO and RPO targets → choose the DR pattern → build the standby environment

### 21. A fulfilment centre has one fibre provider and needs a path that survives one tunnel. What should be used?

Domain: Managing and provisioning a solution infrastructure

- A. Enable Cloud CDN on the backend
- B. Order a Dedicated Interconnect
- C. Use HA VPN with two tunnels
- D. Deploy Cloud NAT for outbound traffic

### 22. Private instances must fetch updates from the internet and reach Google APIs without a proxy. Which two settings apply? Select two.

Domain: Managing and provisioning a solution infrastructure

- A. Attach a Cloud Armor security policy
- B. Put Identity-Aware Proxy in front of the application
- C. Enable Cloud CDN on the backend
- D. Enable Private Google Access on the subnet
- E. Deploy Cloud NAT for outbound traffic

### 23. A bucket receives 6 TB a day and only the last fourteen days are read. What should be configured?

Domain: Managing and provisioning a solution infrastructure

- A. Use a Transfer Appliance for the one-off bulk move
- B. Store the objects in Nearline storage class
- C. Add a lifecycle rule that transitions and then deletes
- D. Enable Autoclass on the bucket

### 24. An events table is always filtered by date and the query bill is rising. What should be applied first?

Domain: Managing and provisioning a solution infrastructure

- A. Partition the table on the date column
- B. Cluster the table on the filter columns
- C. Leave the project on on-demand pricing
- D. Create a materialized view for the repeated aggregate

### 25. The catalogue must survive a region loss and must not lose an overwritten image. Which two settings apply? Select two.

Domain: Managing and provisioning a solution infrastructure

- A. Use a dual-region bucket
- B. Store the objects in Archive storage class
- C. Mount a Filestore instance for the shared file path
- D. Use local SSD for the scratch space
- E. Enable object versioning

### 26. A service needs 64 GB of memory but only two vCPUs. What should be used?

Domain: Managing and provisioning a solution infrastructure

- A. Use sole-tenant nodes
- B. Use a custom machine type sized to the workload
- C. Use local SSD for the scratch space
- D. Run the batch tier on Spot VMs

### 27. A recommendation tier runs constantly at a low level and bursts for a sale. Which two purchasing choices apply? Select two.

Domain: Managing and provisioning a solution infrastructure

- A. Run the batch tier on Spot VMs
- B. Buy committed use discounts for the steady baseline
- C. Use local SSD for the scratch space
- D. Share the cost view with the engineering teams
- E. Move the steady services to E2 machine types

### 28. Pods ask for wildly different resources and nodes are always the wrong size. What should be enabled?

Domain: Managing and provisioning a solution infrastructure

- A. Register the clusters in a fleet
- B. Enable node auto-provisioning
- C. Enable network policy enforcement
- D. Pin a release channel and a maintenance window

### 29. An upgrade broke production last month and the team wants bounded version drift. What should be configured?

Domain: Managing and provisioning a solution infrastructure

- A. Enable network policy enforcement
- B. Register the clusters in a fleet
- C. Enable node auto-provisioning
- D. Pin a release channel and a maintenance window

### 30. A new regional cluster must be built with pod identity and attested images. Which sequence is correct?

Domain: Managing and provisioning a solution infrastructure

- A. Build a Shared VPC → deploy through Binary Authorization → create the project → create the cluster
- B. Create a regional private cluster → build a Shared VPC with private subnets → enable APIs → deploy through Binary Authorization
- C. Create the project and enable APIs → build a Shared VPC with private subnets → create a regional private cluster with Workload Identity Federation for GKE → deploy through Binary Authorization
- D. Deploy through Binary Authorization → create the cluster → build the Shared VPC → create the project

### 31. Each Cloud Run instance serves one request at a time and the bill is ten times the estimate. What should be changed?

Domain: Managing and provisioning a solution infrastructure

- A. Deploy on App Engine flexible environment
- B. Set a minimum instance count on the Cloud Run service
- C. Raise the request concurrency setting
- D. Deploy the workload on Cloud Run with a GPU

### 32. A seasonal environment has to be created identically every year from code. What should be used?

Domain: Managing and provisioning a solution infrastructure

- A. Automate the step with the gcloud CLI
- B. Manage the resources with Terraform
- C. Manage the resources with Config Connector
- D. Use Deployment Manager templates

### 33. Weekly retraining must rerun reproducibly and record lineage for each step. What should be used?

Domain: Managing and provisioning a solution infrastructure

- A. Trigger the job with Cloud Scheduler
- B. Use a Dataproc cluster
- C. Orchestrate the workflow in Agent Platform Pipelines
- D. Run batch prediction

### 34. Catalogue images must be labelled automatically without training a model. What should be used?

Domain: Managing and provisioning a solution infrastructure

- A. Use the Speech-to-Text API
- B. Use the Translation API
- C. Use the Vision API for the images
- D. Use Document AI with a specialised processor

### 35. A clickstream pipeline must be deployed with a dead-letter path and windowing. Which sequence is correct?

Domain: Managing and provisioning a solution infrastructure

- A. Deploy the streaming job → create the Pub/Sub topic → design the windowing → monitor watermark lag
- B. Design the windowing → monitor watermark lag → create the Pub/Sub topic → deploy the job
- C. Create the Pub/Sub topic and subscription → design the Dataflow windowing and allowed lateness → deploy the streaming job with a dead-letter path → monitor watermark lag and backfill from the raw archive
- D. Monitor watermark lag → deploy the streaming job → create the topic → design the windowing

### 36. A seasonal squad needs the curated permission set for one job and nothing else. What should be granted?

Domain: Designing for security and compliance

- A. Authenticate the call with an API key
- B. Grant a predefined role at the narrowest resource
- C. Run a bastion host with a public address
- D. Define a custom role with only the required permissions

### 37. Support access must be time-limited, and a suspended vendor must lose access immediately. Which two controls apply? Select two.

Domain: Designing for security and compliance

- A. Run a bastion host with a public address
- B. Grant a predefined role at the narrowest resource
- C. Tag the resources with labels for cost reporting
- D. Apply an IAM deny policy
- E. Add an IAM condition on the binding

### 38. A new seasonal project must inherit the right access on the day it is created. Where should the roles be bound?

Domain: Designing for security and compliance

- A. Create a folder per environment and bind roles there
- B. Create a separate project per environment
- C. Grant a predefined role at the narrowest resource
- D. Tag the resources with labels for cost reporting

### 39. No project may create a bucket with public access. What should be enforced?

Domain: Designing for security and compliance

- A. Create a folder per environment and bind roles there
- B. Tag the resources with labels for cost reporting
- C. Enforce the control with an organization policy constraint
- D. Create a separate project per environment

### 40. Keys must never leave the region where the catalogue data lives. What should be configured?

Domain: Designing for security and compliance

- A. Create the key ring in the same region as the data
- B. Use Cloud HSM for the key
- C. Store the credential in Secret Manager
- D. Supply a customer-supplied encryption key

### 41. The retailer must control its own keys and change them on a published schedule. Which two settings apply? Select two.

Domain: Designing for security and compliance

- A. Use Cloud HSM for the key
- B. Supply a customer-supplied encryption key
- C. Put the credential in an environment variable on the instance
- D. Encrypt with a customer-managed key in Cloud KMS
- E. Set an automatic rotation period on the key

### 42. Catalogue data must not be copied to a project outside the approved set. What should be applied?

Domain: Designing for security and compliance

- A. Put the projects inside a VPC Service Controls perimeter
- B. Apply a hierarchical firewall policy at the organization or folder
- C. Apply an IAM deny policy
- D. Tag the resources with labels for cost reporting

### 43. Merchandise partners must reach an internal tool with no VPN and no public address. What should be used?

Domain: Designing for security and compliance

- A. Run a bastion host with a public address
- B. Put Identity-Aware Proxy in front of the application
- C. Enable Private Google Access on the subnet
- D. Deploy Cloud NAT for outbound traffic

### 44. Known vulnerabilities must be reported on every image before deployment. What should be enabled?

Domain: Designing for security and compliance

- A. Store the images in Artifact Registry
- B. Record build provenance for the artifact
- C. Require Binary Authorization attestations
- D. Enable Artifact Analysis scanning on the repository

### 45. Only pipeline-built images may run, and the build itself must be attributable. Which two controls apply? Select two.

Domain: Designing for security and compliance

- A. Enable network policy enforcement
- B. Record build provenance for the artifact
- C. Store the images in Artifact Registry
- D. Enable Artifact Analysis scanning on the repository
- E. Require Binary Authorization attestations

### 46. A shopper-facing assistant must resist prompt injection. What should be added?

Domain: Designing for security and compliance

- A. Require an access level in the perimeter
- B. De-identify the data with Sensitive Data Protection
- C. Screen prompts and responses with Model Armor
- D. Turn on Security Command Center findings

### 47. The retailer must show who ran a price change and when. What should be enabled?

Domain: Designing for security and compliance

- A. Enable Data Access audit logs
- B. Rely on Admin Activity audit logs
- C. Review Access Transparency logs
- D. Create a log-based metric

### 48. Evidence must be collected from every project into one place an auditor can query. What should be built?

Domain: Designing for security and compliance

- A. Publish a runbook per alert
- B. Publish a shared dashboard
- C. Create a log-based metric
- D. Route the logs with an aggregated sink

### 49. A retail audit needs read evidence retained for six years. Which sequence is correct?

Domain: Designing for security and compliance

- A. Route the logs with a sink → query the evidence → enable audit logs → create a locked bucket
- B. Create a locked log bucket → enable data access audit logs → query the evidence → route the logs with a sink
- C. Enable data access audit logs for the services in scope → create a locked log bucket with the required retention → route the logs with an aggregated sink → query and export the evidence for the auditor
- D. Query the evidence → create a locked log bucket → enable audit logs → route the logs

### 50. Two feature teams keep branches open for weeks and merge painfully. What should change?

Domain: Analyzing and optimizing technical and business processes

- A. Adopt trunk-based development with short-lived branches
- B. Put the change behind a feature flag
- C. Rebuild the artifact separately for each environment
- D. Roll the change out instance by instance

### 51. Every change must be reviewed, and production must run exactly what was tested. Which two practices apply? Select two.

Domain: Analyzing and optimizing technical and business processes

- A. Promote the same tested artifact between environments
- B. Require a reviewed pull request and a passing plan
- C. Roll the change out instance by instance
- D. Set a budget with alert thresholds
- E. Rebuild the artifact separately for each environment

### 52. A product page takes 1.4 seconds across five services. What should be inspected first?

Domain: Analyzing and optimizing technical and business processes

- A. Act on the Recommender suggestions
- B. Add an uptime check from several regions
- C. Publish a shared dashboard
- D. Inspect the trace waterfall in Cloud Trace

### 53. A price update failed silently and the team must find both the error text and its frequency. Which two tools apply? Select two.

Domain: Analyzing and optimizing technical and business processes

- A. Query the entries in Cloud Logging
- B. Publish a shared dashboard
- C. Publish a runbook per alert
- D. Define an SLO with an error budget
- E. Group the exceptions in Error Reporting

### 54. A November peak must be proven before the code freeze. What should be run?

Domain: Analyzing and optimizing technical and business processes

- A. Run a load test at the expected peak
- B. Run a chaos experiment against a zone
- C. Cover the change with unit, integration, and a few end-to-end tests
- D. Commission a penetration test

### 55. A catalogue can accept an hour to recover but must not pay for a running copy. What fits?

Domain: Analyzing and optimizing technical and business processes

- A. Use backup and restore
- B. Run active-active across two regions
- C. Run a warm standby at reduced capacity
- D. Run a pilot-light standby

### 56. Analysts suspect the warehouse is paying for idle capacity. What should be reviewed first?

Domain: Analyzing and optimizing technical and business processes

- A. Set a budget with alert thresholds
- B. Tag the resources with labels for cost reporting
- C. Export billing to BigQuery and review it per label
- D. Act on the Recommender suggestions

### 57. Each product team must see the cost it caused this month. What should be configured?

Domain: Analyzing and optimizing technical and business processes

- A. Export billing to BigQuery and review it per label
- B. Tag the resources with labels for cost reporting
- C. Set a budget with alert thresholds
- D. Share the cost view with the engineering teams

### 58. The warehouse bill must fall and the top queries must be identified first. Which sequence is correct?

Domain: Analyzing and optimizing technical and business processes

- A. Measure slot time → rewrite the query → inspect the plan → partition the table
- B. Inspect the query plan and bytes processed → partition and cluster the table on the filter columns → rewrite the query to prune partitions → measure the new slot time and bytes scanned
- C. Partition and cluster the table → measure slot time → inspect the plan → rewrite the query
- D. Rewrite the query → partition the table → measure slot time → inspect the plan

### 59. A price change affects the regulated storefront and must be reviewed for timing. What should it go through?

Domain: Analyzing and optimizing technical and business processes

- A. Publish a runbook per alert
- B. Define an on-call rotation with an escalation path
- C. Publish a service catalog entry with an approved template
- D. Route the change through a change advisory board

### 60. Seasonal teams need a compliant environment without waiting for the platform team. What should be published?

Domain: Analyzing and optimizing technical and business processes

- A. Enforce the control with an organization policy constraint
- B. Publish a service catalog entry with an approved template
- C. Manage the resources with Terraform
- D. Tag the resources with labels for cost reporting

### 61. A new checkout must be proven on five per cent of live traffic. What should be used?

Domain: Managing implementation

- A. Put the change behind a feature flag
- B. Deploy blue/green with a traffic switch
- C. Roll out a canary to a small share of traffic
- D. Roll the change out instance by instance

### 62. Two identical environments exist, and the previous build must be exactly restorable. Which two practices apply? Select two.

Domain: Managing implementation

- A. Keep the previous image digest ready for rollback
- B. Rebuild the artifact separately for each environment
- C. Deploy blue/green with a traffic switch
- D. Promote the same tested artifact between environments
- E. Set a budget with alert thresholds

### 63. A storefront release must be reversible within one minute during trading hours. Which sequence is correct?

Domain: Managing implementation

- A. Deploy the new revision → promote to full traffic → shift a small percentage → build the image
- B. Watch the error rate → deploy the new revision → shift traffic → build the image
- C. Build an immutable image and record its digest → deploy the new revision without traffic → shift a small traffic percentage and watch error and latency signals → promote to full traffic or roll back to the pinned digest
- D. Shift full traffic to the new revision → build the image → watch the error rate → promote or roll back

### 64. Marketplace sellers need per-consumer quotas and mediation. What should be used?

Domain: Managing implementation

- A. Use Cloud Endpoints
- B. Attach a Cloud Armor security policy
- C. Use API Gateway
- D. Publish the API through Apigee

### 65. One internal service needs a managed OpenAPI front door with no policy engine. What should be used?

Domain: Managing implementation

- A. Use Cloud Endpoints
- B. Publish the API through Apigee
- C. Attach a Cloud Armor security policy
- D. Use API Gateway

### 66. An 8 TB order database must move with less than three hours of downtime. What should be used?

Domain: Managing implementation

- A. Copy the files with Storage Transfer Service
- B. Migrate the database with Database Migration Service
- C. Use the BigQuery Data Transfer Service
- D. Use Datastream for change data capture

### 67. Twelve terabytes of catalogue images must be copied from another cloud every week. What should be used?

Domain: Managing implementation

- A. Assess the estate in Migration Center
- B. Use a Transfer Appliance for the one-off bulk move
- C. Convert the VMs with Migrate to Containers
- D. Copy the files with Storage Transfer Service

### 68. A seasonal platform must migrate without breaking order dependencies. Which sequence is correct?

Domain: Managing implementation

- A. Group servers into waves → inventory the estate → cut over and decommission → validate a pilot wave
- B. Inventory the estate in Migration Center → group servers into dependency-based waves → validate a pilot wave in the target landing zone → cut over wave by wave and decommission the source
- C. Validate a pilot wave → inventory the estate → group servers into waves → cut over and decommission
- D. Cut over and decommission → validate a pilot wave → inventory the estate → group servers into waves

### 69. A pricing pipeline must be tested locally with no billable resource. What should be used?

Domain: Managing implementation

- A. Manage the resources with Terraform
- B. Run the build in Cloud Build
- C. Automate the step with the gcloud CLI
- D. Run the emulator in the pipeline

### 70. A monthly cost export must be scripted so the command is recorded. What should be used?

Domain: Managing implementation

- A. Automate the step with the gcloud CLI
- B. Use Cloud Code in the IDE
- C. Use Cloud Shell for the one-off task
- D. Use the bq command-line tool

### 71. A new pricing service must retry quota errors with the vendor's recommended backoff. What should it use?

Domain: Managing implementation

- A. Impersonate a service account for a curl test
- B. Use the Google API client library with retries
- C. Authenticate the call with an API key
- D. Automate the step with the gcloud CLI

### 72. Host metrics and application logs must reach Google Cloud from the storefront fleet. What should be installed?

Domain: Ensuring solution and operations excellence

- A. Inspect the trace waterfall in Cloud Trace
- B. Attach Cloud Profiler to the service
- C. Install the Ops Agent on the instances
- D. Group the exceptions in Error Reporting

### 73. The storefront needs external availability evidence and a per-service breakdown of one slow call. Which two tools apply? Select two.

Domain: Ensuring solution and operations excellence

- A. Inspect the trace waterfall in Cloud Trace
- B. Add an uptime check from several regions
- C. Act on the Recommender suggestions
- D. Publish a shared dashboard
- E. Define an SLO with an error budget

### 74. The team wants an alert tied to successful checkouts rather than to CPU. What should be defined?

Domain: Ensuring solution and operations excellence

- A. Create an alerting policy on the metric
- B. Define an SLO with an error budget
- C. Publish a shared dashboard
- D. Add an uptime check from several regions

### 75. A metric exists and someone must be told when it stays above the limit for ten minutes. What should be created?

Domain: Ensuring solution and operations excellence

- A. Create an alerting policy on the metric
- B. Create a log-based metric
- C. Define an SLO with an error budget
- D. Publish a shared dashboard

### 76. The last peak took forty minutes to diagnose because nobody knew the steps. What should be published?

Domain: Ensuring solution and operations excellence

- A. Match the support plan to the recovery commitment
- B. Define an on-call rotation with an escalation path
- C. Publish a shared dashboard
- D. Publish a runbook per alert

### 77. The design claims a zone loss is survivable, and no one has tested it. What should be run?

Domain: Ensuring solution and operations excellence

- A. Run a load test at the expected peak
- B. Commission a penetration test
- C. Roll out a canary to a small share of traffic
- D. Run a chaos experiment against a zone

### 78. A price bug recurred because the follow-up work was never recorded. What should be produced after each incident?

Domain: Ensuring solution and operations excellence

- A. Publish a runbook per alert
- B. Write a blameless postmortem with actions
- C. Publish a shared dashboard
- D. Match the support plan to the recovery commitment

### 79. The business expects a thirty-minute response during trading hours. What should be aligned?

Domain: Ensuring solution and operations excellence

- A. Match the support plan to the recovery commitment
- B. Define an on-call rotation with an escalation path
- C. Publish a runbook per alert
- D. Put the recovery commitment in the contract

### 80. The storefront is down during a sale and the response must follow the agreed order. Which sequence is correct?

Domain: Ensuring solution and operations excellence

- A. Detect the symptom through an alert → contain the impact and restore service → isolate the root cause from logs, traces, and metrics → apply the permanent fix and write the postmortem
- B. Write the postmortem → detect the symptom → isolate the root cause → restore service
- C. Isolate the root cause → detect the symptom → write the postmortem → restore service
- D. Restore service → detect the symptom → write the postmortem → isolate the root cause

---

## Case study — Harborline Shipping

Harborline Shipping runs its booking and tracking platform in a single region and has a recovery objective of fifteen minutes for the booking service and four hours for the analytics warehouse. A fire in the primary data centre last year stopped bookings for nine hours. The board has approved a budget for resilience but not for running the entire estate twice. The booking database is 4 TB and the warehouse is 300 TB, and the network team has said a second region can be reached only through a new interconnect. The company must prove the recovery time in a rehearsal before the next board meeting.

The next 5 questions refer to it. Read the scenario once, then answer all 5; each item restates the constraint it tests and is scored individually.

### 81. Booking can accept fifteen minutes of downtime and a smaller running copy. What fits?

Domain: Analyzing and optimizing technical and business processes

- A. Run a pilot-light standby
- B. Run active-active across two regions
- C. Use backup and restore
- D. Run a warm standby at reduced capacity

### 82. The document archive must stay readable if the primary region is lost. Which bucket configuration meets that?

Domain: Managing and provisioning a solution infrastructure

- A. Use a dual-region bucket
- B. Store the objects in Standard storage class
- C. Store the objects in Archive storage class
- D. Store the objects in Nearline storage class

### 83. Recovery of the booking service depends on the data being available in the second region. What must the design provide?

Domain: Designing and planning a cloud solution architecture

- A. Replicate the data to the second region
- B. Run a pilot-light standby
- C. Enable Cloud CDN on the backend
- D. Use backup and restore

### 84. The board expects a proven recovery time, not a promise. What must be aligned with the vendor?

Domain: Ensuring solution and operations excellence

- A. Define an on-call rotation with an escalation path
- B. Put the recovery commitment in the contract
- C. Publish a runbook per alert
- D. Match the support plan to the recovery commitment

### 85. The 4 TB booking database must move with a short cutover. What should be used?

Domain: Managing implementation

- A. Copy the files with Storage Transfer Service
- B. Migrate the database with Database Migration Service
- C. Use the BigQuery Data Transfer Service
- D. Use Datastream for change data capture

---

## Case study — Orchid Commerce

Orchid Commerce runs a marketplace with 12 million monthly shoppers. The analytics team spends EUR 90,000 a month on BigQuery and cannot explain which team or dashboard causes the spend. Dashboards refresh every ten minutes and scan the same three large tables each time, while a nightly machine learning job scans the same tables again for training. The finance team wants each product team to see its own cost, and the platform team wants the top ten queries by bytes scanned identified before any commitment is purchased. Traffic doubles in November, and the chief technology officer has refused a three-year commitment until the waste is removed.

The next 5 questions refer to it. Read the scenario once, then answer all 5; each item restates the constraint it tests and is scored individually.

### 86. Dashboards refresh every ten minutes and rescan three large tables. What should absorb the repeated reads?

Domain: Designing and planning a cloud solution architecture

- A. Build the dashboard in Looker Studio
- B. Leave the project on on-demand pricing
- C. Reserve BigQuery BI Engine capacity
- D. Stream rows with the legacy insertAll call

### 87. The nightly job scans the same table as the dashboards. What should reduce that scan first?

Domain: Managing and provisioning a solution infrastructure

- A. Leave the project on on-demand pricing
- B. Create a materialized view for the repeated aggregate
- C. Cluster the table on the filter columns
- D. Partition the table on the date column

### 88. Nobody can say which team caused the EUR 90,000 bill. What should be configured?

Domain: Analyzing and optimizing technical and business processes

- A. Export billing to BigQuery and review it per label
- B. Tag the resources with labels for cost reporting
- C. Set a budget with alert thresholds
- D. Share the cost view with the engineering teams

### 89. The team must know when checkout slows before customers complain. What should be defined?

Domain: Ensuring solution and operations excellence

- A. Define an SLO with an error budget
- B. Publish a shared dashboard
- C. Add an uptime check from several regions
- D. Create an alerting policy on the metric

### 90. Each marketplace seller may read only its own order rows. What should be applied?

Domain: Designing for security and compliance

- A. Expose the data through an authorized view
- B. Apply column-level data masking policies
- C. Add row-level access policies to the table
- D. Build the dashboard in Looker Studio

---

## Case study — Pinecrest University

Pinecrest University has 200 developers across nine faculties who deploy research applications to a shared cluster. Each faculty currently creates projects by hand, and a review found that forty per cent of the projects had no owner and that several had public buckets. The university wants a paved road: a new project should arrive with the right folder placement, budget label, logging destination, and network attachment, and it must be impossible to create a public bucket. Deployments must be reproducible, and a faculty must not be able to change another faculty environment. The security team wants to see every environment change before it happens.

The next 5 questions refer to it. Read the scenario once, then answer all 5; each item restates the constraint it tests and is scored individually.

### 91. A faculty must self-serve a compliant project without the platform team. What should be published?

Domain: Analyzing and optimizing technical and business processes

- A. Manage the resources with Terraform
- B. Publish a service catalog entry with an approved template
- C. Tag the resources with labels for cost reporting
- D. Enforce the control with an organization policy constraint

### 92. Forty per cent of projects had no owner and several buckets were public. What should prevent that in future projects?

Domain: Designing for security and compliance

- A. Create a separate project per environment
- B. Enforce the control with an organization policy constraint
- C. Tag the resources with labels for cost reporting
- D. Create a folder per environment and bind roles there

### 93. The programme must show whether the paved road actually reduced incidents. What should be recorded now?

Domain: Designing and planning a cloud solution architecture

- A. Export billing to BigQuery and review it per label
- B. Build a three-year total cost of ownership model
- C. Define the baseline and target as a KPI with an owner
- D. Publish a shared dashboard

### 94. A public bucket was found and fixed, and the same mistake recurred. What is missing?

Domain: Ensuring solution and operations excellence

- A. Publish a runbook per alert
- B. Match the support plan to the recovery commitment
- C. Publish a shared dashboard
- D. Write a blameless postmortem with actions

### 95. Nine faculties must be inventoried before environments are standardized. What should be used?

Domain: Designing and planning a cloud solution architecture

- A. Convert the VMs with Migrate to Containers
- B. Copy the files with Storage Transfer Service
- C. Assess the estate in Migration Center
- D. Use Database Migration Service

---

## Case study — Vertex Insurance

Vertex Insurance prices motor policies from telematics, claims history, and vehicle data. The pricing team retrains a gradient-boosted model every week, and the current process runs a notebook on an engineer laptop. Regulators require that any price quoted to a customer can be reproduced with the exact model version and input data that produced it. The claims stream arrives continuously and the pricing features must be refreshed daily. Two models run in production at once during a migration, and the team must be able to send five per cent of traffic to the new model before committing to it.

The next 5 questions refer to it. Read the scenario once, then answer all 5; each item restates the constraint it tests and is scored individually.

### 96. Weekly retraining and daily scoring must use one feature definition. What should be used?

Domain: Managing and provisioning a solution infrastructure

- A. Orchestrate the workflow in Agent Platform Pipelines
- B. Deploy to an online prediction endpoint
- C. Serve features from Agent Platform Feature Store
- D. Enable model monitoring on the endpoint

### 97. Claims notes contain sensitive data, and the pricing assistant must resist manipulation. Which two controls apply? Select two.

Domain: Designing for security and compliance

- A. Screen prompts and responses with Model Armor
- B. De-identify the data with Sensitive Data Protection
- C. Turn on Security Command Center findings
- D. Apply an IAM deny policy
- E. Require an access level in the perimeter

### 98. A price change may be caused by drift in the input data. What should be enabled?

Domain: Designing and planning a cloud solution architecture

- A. Serve features from Agent Platform Feature Store
- B. Enable model monitoring on the endpoint
- C. Run batch prediction
- D. Deploy to an online prediction endpoint

### 99. A quote took nine seconds and the team needs the call chain. What should be inspected?

Domain: Analyzing and optimizing technical and business processes

- A. Inspect the trace waterfall in Cloud Trace
- B. Publish a shared dashboard
- C. Act on the Recommender suggestions
- D. Query the entries in Cloud Logging

### 100. The team must see training and serving metrics in one place. What should be built first?

Domain: Ensuring solution and operations excellence

- A. Define dashboards and metrics in Cloud Monitoring
- B. Act on the Recommender suggestions
- C. Publish a shared dashboard
- D. Inspect the trace waterfall in Cloud Trace

---

## Answer key and explanations

### Question 1 — C

Answer: Define the baseline and target as a KPI with an owner. A measured baseline and a named owner make the saving testable after the programme. Local study-map skill 1.1 (Business Requirements and Success Metrics), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 1 (designing and planning): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. Recommender reports idle and over-provisioned resources with the estimated saving. Why the correct answer wins: A measured baseline and a named owner make the saving testable after the programme.
- **B:** Incorrect for this question. The dashboard gives the team one view of the same signals during an incident. Why the correct answer wins: A measured baseline and a named owner make the saving testable after the programme.
- **C:** Correct. In this case: A measured baseline and a named owner make the saving testable after the programme.
- **D:** Incorrect for this question. The export attributes cost to the team and service that caused it. Why the correct answer wins: A measured baseline and a named owner make the saving testable after the programme.

### Question 2 — A

Answer: Build a three-year total cost of ownership model. The model compares run cost, people cost, and exit cost rather than the monthly bill alone. Local study-map skill 1.1 (Business Requirements and Success Metrics), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 1 (designing and planning): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Correct. In this case: The model compares run cost, people cost, and exit cost rather than the monthly bill alone.
- **B:** Incorrect for this question. A budget alerts on spend but does not stop it. Why the correct answer wins: The model compares run cost, people cost, and exit cost rather than the monthly bill alone.
- **C:** Incorrect for this question. The export attributes cost to the team and service that caused it. Why the correct answer wins: The model compares run cost, people cost, and exit cost rather than the monthly bill alone.
- **D:** Incorrect for this question. A one- or three-year commitment discounts the capacity that runs constantly, not the peaks. Why the correct answer wins: The model compares run cost, people cost, and exit cost rather than the monthly bill alone.

### Question 3 — D

Answer: Document the exit plan and data portability. An exit plan and data portability keep the migration reversible and bound how proprietary the design may become. The exit plan keeps the migration reversible and constrains how proprietary the design may become. Local study-map skill 1.2 (Non-Functional Requirements and Trade-offs), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 1 (designing and planning): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. The model compares run cost, people cost, and exit cost rather than the monthly bill alone. Why the correct answer wins: An exit plan and data portability keep the migration reversible and bound how proprietary the design may become.
- **B:** Incorrect for this question. Labels attribute spend in billing export; they do not grant or restrict access. Why the correct answer wins: An exit plan and data portability keep the migration reversible and bound how proprietary the design may become.
- **C:** Incorrect for this question. A budget alerts on spend but does not stop it. Why the correct answer wins: An exit plan and data portability keep the migration reversible and bound how proprietary the design may become.
- **D:** Correct. The exit plan keeps the migration reversible and constrains how proprietary the design may become. In this case: An exit plan and data portability keep the migration reversible and bound how proprietary the design may become.

### Question 4 — A, C

Answers: Set the RPO and RTO with the business owner; Put the recovery commitment in the contract. The targets quantify the acceptable loss, and the contract attaches a consequence to missing them. The targets come from the business impact of data loss and downtime, not from the technology. The contract converts an internal target into an obligation with a consequence. Local study-map skill 1.2 (Non-Functional Requirements and Trade-offs), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 1 (designing and planning): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Correct. The targets come from the business impact of data loss and downtime, not from the technology. In this case: The targets quantify the acceptable loss, and the contract attaches a consequence to missing them.
- **B:** Incorrect for this question. Labels attribute spend in billing export; they do not grant or restrict access. Why the correct answer wins: The targets quantify the acceptable loss, and the contract attaches a consequence to missing them.
- **C:** Correct. The contract converts an internal target into an obligation with a consequence. In this case: The targets quantify the acceptable loss, and the contract attaches a consequence to missing them.
- **D:** Incorrect for this question. The dashboard gives the team one view of the same signals during an incident. Why the correct answer wins: The targets quantify the acceptable loss, and the contract attaches a consequence to missing them.
- **E:** Incorrect for this question. Recommender reports idle and over-provisioned resources with the estimated saving. Why the correct answer wins: The targets quantify the acceptable loss, and the contract attaches a consequence to missing them.

### Question 5 — B

Answer: Enable Cloud SQL high availability with a standby. A regional standby takes over automatically when the primary zone fails. Local study-map skill 1.3 (High Availability and Failover Design), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 1 (designing and planning): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. A replica offloads read traffic but lags the primary, so it is not a failover target. Why the correct answer wins: A regional standby takes over automatically when the primary zone fails.
- **B:** Correct. In this case: A regional standby takes over automatically when the primary zone fails.
- **C:** Incorrect for this question. Bigtable is a wide-column store for high-throughput key reads and writes at low latency. Why the correct answer wins: A regional standby takes over automatically when the primary zone fails.
- **D:** Incorrect for this question. Memorystore provides managed Redis or Memcached for sub-millisecond cache lookups. Why the correct answer wins: A regional standby takes over automatically when the primary zone fails.

### Question 6 — A, D

Answers: Run active-active across two regions; Replicate the data to the second region. Both regions serve traffic, and the data must already be in the second region when it is needed. Both regions serve traffic, so a regional loss is absorbed without a failover decision. The data must exist in the second region before any compute there can serve it. Local study-map skill 1.3 (High Availability and Failover Design), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 1 (designing and planning): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Correct. Both regions serve traffic, so a regional loss is absorbed without a failover decision. In this case: Both regions serve traffic, and the data must already be in the second region when it is needed.
- **B:** Incorrect for this question. Restoring from backup is the cheapest option and the slowest to recover. Why the correct answer wins: Both regions serve traffic, and the data must already be in the second region when it is needed.
- **C:** Incorrect for this question. CDN caches responses at edge locations, which cuts origin load and latency for repeat reads. Why the correct answer wins: Both regions serve traffic, and the data must already be in the second region when it is needed.
- **D:** Correct. The data must exist in the second region before any compute there can serve it. In this case: Both regions serve traffic, and the data must already be in the second region when it is needed.
- **E:** Incorrect for this question. Only the core data and configuration stay warm, so recovery starts the compute and takes minutes. Why the correct answer wins: Both regions serve traffic, and the data must already be in the second region when it is needed.

### Question 7 — B

Answer: Build a Network Connectivity Center hub. Peering is not transitive, so a hub provides the routing the spokes cannot provide themselves. The hub gives transitive routing between spokes, which peering alone cannot provide. Local study-map skill 1.4 (Network Design), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 1 (designing and planning): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. Cloud NAT lets private instances reach the internet without an external address. Why the correct answer wins: Peering is not transitive, so a hub provides the routing the spokes cannot provide themselves.
- **B:** Correct. The hub gives transitive routing between spokes, which peering alone cannot provide. In this case: Peering is not transitive, so a hub provides the routing the spokes cannot provide themselves.
- **C:** Incorrect for this question. Peering joins two networks at layer three but does not share firewalls or transitive routes. Why the correct answer wins: Peering is not transitive, so a hub provides the routing the spokes cannot provide themselves.
- **D:** Incorrect for this question. DNS peering resolves names across networks without transferring zone ownership. Why the correct answer wins: Peering is not transitive, so a hub provides the routing the spokes cannot provide themselves.

### Question 8 — C, D

Answers: Publish the service through Private Service Connect; Peer the two VPC networks. A published endpoint gives a private address, and peering joins the two networks at layer three. A PSC endpoint gives a private IP in the consumer VPC without peering or exposing the service publicly. Peering joins two networks at layer three but does not share firewalls or transitive routes. Local study-map skill 1.4 (Network Design), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 1 (designing and planning): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. Cloud NAT lets private instances reach the internet without an external address. Why the correct answer wins: A published endpoint gives a private address, and peering joins the two networks at layer three.
- **B:** Incorrect for this question. A signed URL grants one object for a fixed time without exposing credentials or making the bucket public. Why the correct answer wins: A published endpoint gives a private address, and peering joins the two networks at layer three.
- **C:** Correct. A PSC endpoint gives a private IP in the consumer VPC without peering or exposing the service publicly. In this case: A published endpoint gives a private address, and peering joins the two networks at layer three.
- **D:** Correct. Peering joins two networks at layer three but does not share firewalls or transitive routes. In this case: A published endpoint gives a private address, and peering joins the two networks at layer three.
- **E:** Incorrect for this question. CDN caches responses at edge locations, which cuts origin load and latency for repeat reads. Why the correct answer wins: A published endpoint gives a private address, and peering joins the two networks at layer three.

### Question 9 — B

Answer: Enable Cloud CDN on the backend. CDN caches responses at edge locations, which cuts origin load and latency for repeat reads. Local study-map skill 1.4 (Network Design), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 1 (designing and planning): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. Cloud NAT lets private instances reach the internet without an external address. Why the correct answer wins: CDN caches responses at edge locations, which cuts origin load and latency for repeat reads.
- **B:** Correct. In this case: CDN caches responses at edge locations, which cuts origin load and latency for repeat reads.
- **C:** Incorrect for this question. An internal load balancer distributes traffic inside the VPC without exposing it to the internet. Why the correct answer wins: CDN caches responses at edge locations, which cuts origin load and latency for repeat reads.
- **D:** Incorrect for this question. The storage commands copy and sync objects with resumable, parallel transfers. Why the correct answer wins: CDN caches responses at edge locations, which cuts origin load and latency for repeat reads.

### Question 10 — B

Answer: Enable Autoclass on the bucket. Autoclass moves each object between classes as its access pattern changes, with no rules to maintain. Local study-map skill 1.5 (Storage and Data Store Selection), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 1 (designing and planning): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. Standard is for data read frequently and has no retrieval fee. Why the correct answer wins: Autoclass moves each object between classes as its access pattern changes, with no rules to maintain.
- **B:** Correct. In this case: Autoclass moves each object between classes as its access pattern changes, with no rules to maintain.
- **C:** Incorrect for this question. A lifecycle rule acts on object age or class, so retention stops depending on a person. Why the correct answer wins: Autoclass moves each object between classes as its access pattern changes, with no rules to maintain.
- **D:** Incorrect for this question. Nearline suits data read about once a month and charges for early deletion. Why the correct answer wins: Autoclass moves each object between classes as its access pattern changes, with no rules to maintain.

### Question 11 — B, E

Answers: Enable Autoclass on the bucket; Add a lifecycle rule that transitions and then deletes. Autoclass handles the changing temperature, and the lifecycle rule deletes on age. Autoclass moves each object between classes as its access pattern changes, with no lifecycle rules to maintain. A lifecycle rule acts on object age or class, so retention stops depending on a person. Local study-map skill 1.5 (Storage and Data Store Selection), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 1 (designing and planning): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. Filestore provides a managed NFS export that many clients can mount at once. Why the correct answer wins: Autoclass handles the changing temperature, and the lifecycle rule deletes on age.
- **B:** Correct. Autoclass moves each object between classes as its access pattern changes, with no lifecycle rules to maintain. In this case: Autoclass handles the changing temperature, and the lifecycle rule deletes on age.
- **C:** Incorrect for this question. Local SSD is the fastest ephemeral option and loses its data when the VM stops. Why the correct answer wins: Autoclass handles the changing temperature, and the lifecycle rule deletes on age.
- **D:** Incorrect for this question. Archive is cheapest to hold and slowest and most expensive to retrieve. Why the correct answer wins: Autoclass handles the changing temperature, and the lifecycle rule deletes on age.
- **E:** Correct. A lifecycle rule acts on object age or class, so retention stops depending on a person. In this case: Autoclass handles the changing temperature, and the lifecycle rule deletes on age.

### Question 12 — D

Answer: Deploy the service on Cloud Run. Cloud Run scales to zero and bills per request, which suits an intermittent storefront service. Cloud Run runs a stateless container per request and scales to zero when idle. Local study-map skill 1.6 (Compute Platform Selection), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 1 (designing and planning): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. Standard exposes node configuration and patching, which the team must then run itself. Why the correct answer wins: Cloud Run scales to zero and bills per request, which suits an intermittent storefront service.
- **B:** Incorrect for this question. VMware Engine keeps the existing hypervisor and operations model while moving the hardware into Google Cloud. Why the correct answer wins: Cloud Run scales to zero and bills per request, which suits an intermittent storefront service.
- **C:** Incorrect for this question. The group replaces unhealthy instances and adds capacity from a template as load rises. Why the correct answer wins: Cloud Run scales to zero and bills per request, which suits an intermittent storefront service.
- **D:** Correct. Cloud Run runs a stateless container per request and scales to zero when idle. In this case: Cloud Run scales to zero and bills per request, which suits an intermittent storefront service.

### Question 13 — C

Answer: Submit the work as a Batch job. Batch schedules containerised jobs onto managed capacity and retires it when the work is done. Local study-map skill 1.6 (Compute Platform Selection), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 1 (designing and planning): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. The group replaces unhealthy instances and adds capacity from a template as load rises. Why the correct answer wins: Batch schedules containerised jobs onto managed capacity and retires it when the work is done.
- **B:** Incorrect for this question. Cloud Run runs a stateless container per request and scales to zero when idle. Why the correct answer wins: Batch schedules containerised jobs onto managed capacity and retires it when the work is done.
- **C:** Correct. In this case: Batch schedules containerised jobs onto managed capacity and retires it when the work is done.
- **D:** Incorrect for this question. Standard exposes node configuration and patching, which the team must then run itself. Why the correct answer wins: Batch schedules containerised jobs onto managed capacity and retires it when the work is done.

### Question 14 — D

Answer: Load the data into BigQuery. BigQuery is serverless and separates storage from compute, so a scan pays for the bytes read. Local study-map skill 1.7 (Data Processing and Analytics Selection), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 1 (designing and planning): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. Bigtable is a wide-column store for high-throughput key reads and writes at low latency. Why the correct answer wins: BigQuery is serverless and separates storage from compute, so a scan pays for the bytes read.
- **B:** Incorrect for this question. Firestore is a document store with real-time listeners and per-document transactions. Why the correct answer wins: BigQuery is serverless and separates storage from compute, so a scan pays for the bytes read.
- **C:** Incorrect for this question. Cloud SQL is a managed MySQL, PostgreSQL, or SQL Server instance with a familiar connection model. Why the correct answer wins: BigQuery is serverless and separates storage from compute, so a scan pays for the bytes read.
- **D:** Correct. In this case: BigQuery is serverless and separates storage from compute, so a scan pays for the bytes read.

### Question 15 — A, B

Answers: Reserve BigQuery BI Engine capacity; Buy BigQuery slot commitments with autoscaling. BI Engine holds the working set in memory, and slot commitments price steady query volume. BI Engine holds a working set in memory so dashboards answer without scanning the table each time. Slots are the unit of compute, and autoscaling adds them only while queries queue. Local study-map skill 1.7 (Data Processing and Analytics Selection), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 1 (designing and planning): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Correct. BI Engine holds a working set in memory so dashboards answer without scanning the table each time. In this case: BI Engine holds the working set in memory, and slot commitments price steady query volume.
- **B:** Correct. Slots are the unit of compute, and autoscaling adds them only while queries queue. In this case: BI Engine holds the working set in memory, and slot commitments price steady query volume.
- **C:** Incorrect for this question. InsertAll is best-effort and only deduplicates on a provided insert ID, so duplicates can land. Why the correct answer wins: BI Engine holds the working set in memory, and slot commitments price steady query volume.
- **D:** Incorrect for this question. On-demand bills per byte scanned, which is cheap for sparse use and unpredictable at scale. Why the correct answer wins: BI Engine holds the working set in memory, and slot commitments price steady query volume.
- **E:** Incorrect for this question. Looker Studio renders the visualisation but inherits whatever query and permissions sit beneath it. Why the correct answer wins: BI Engine holds the working set in memory, and slot commitments price steady query volume.

### Question 16 — A

Answer: Use Dataproc Serverless. Serverless Spark runs the batch without cluster sizing or idle cost between jobs. Local study-map skill 1.7 (Data Processing and Analytics Selection), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 1 (designing and planning): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Correct. In this case: Serverless Spark runs the batch without cluster sizing or idle cost between jobs.
- **B:** Incorrect for this question. A Dataproc cluster runs open-source Spark and Hadoop with jobs that need a persistent cluster. Why the correct answer wins: Serverless Spark runs the batch without cluster sizing or idle cost between jobs.
- **C:** Incorrect for this question. Airflow expresses dependencies between scheduled jobs and retries a failed task without rerunning the rest. Why the correct answer wins: Serverless Spark runs the batch without cluster sizing or idle cost between jobs.
- **D:** Incorrect for this question. Dataflow runs an Apache Beam pipeline with autoscaling and a single programming model for batch and streaming. Why the correct answer wins: Serverless Spark runs the batch without cluster sizing or idle cost between jobs.

### Question 17 — D

Answer: Run batch prediction. Batch prediction reads a file and writes predictions without holding serving capacity. Local study-map skill 1.8 (AI and ML Solution Design), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 1 (designing and planning): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. Monitoring compares live traffic against the training baseline and reports skew and drift. Why the correct answer wins: Batch prediction reads a file and writes predictions without holding serving capacity.
- **B:** Incorrect for this question. AI Hypercomputer pairs accelerators with a scheduling stack tuned for large distributed training. Why the correct answer wins: Batch prediction reads a file and writes predictions without holding serving capacity.
- **C:** Incorrect for this question. An endpoint keeps capacity ready for low-latency per-request predictions. Why the correct answer wins: Batch prediction reads a file and writes predictions without holding serving capacity.
- **D:** Correct. In this case: Batch prediction reads a file and writes predictions without holding serving capacity.

### Question 18 — A

Answer: Index the corpus with Vertex AI Search. Vertex AI Search returns grounded, cited results over private documents without a custom index. Local study-map skill 1.8 (AI and ML Solution Design), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 1 (designing and planning): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Correct. In this case: Vertex AI Search returns grounded, cited results over private documents without a custom index.
- **B:** Incorrect for this question. A Document AI processor extracts structured fields from forms and invoices with layout awareness. Why the correct answer wins: Vertex AI Search returns grounded, cited results over private documents without a custom index.
- **C:** Incorrect for this question. The translation model handles 100 or more languages without custom training. Why the correct answer wins: Vertex AI Search returns grounded, cited results over private documents without a custom index.
- **D:** Incorrect for this question. The prebuilt Vision model labels, detects, and reads text without training a model. Why the correct answer wins: Vertex AI Search returns grounded, cited results over private documents without a custom index.

### Question 19 — C

Answer: Assess the estate in Migration Center. Migration Center inventories the estate and estimates target size and cost before a plan is funded. Migration Center inventories the servers and estimates the target size and cost. Local study-map skill 1.9 (Migration Planning and Future Improvement), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 1 (designing and planning): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. The tool rewrites a VM workload into a container image so it can run on GKE. Why the correct answer wins: Migration Center inventories the estate and estimates target size and cost before a plan is funded.
- **B:** Incorrect for this question. The service moves a database with continuous replication and a short cutover window. Why the correct answer wins: Migration Center inventories the estate and estimates target size and cost before a plan is funded.
- **C:** Correct. Migration Center inventories the servers and estimates the target size and cost. In this case: Migration Center inventories the estate and estimates target size and cost before a plan is funded.
- **D:** Incorrect for this question. The service moves object data between buckets or clouds on a schedule. Why the correct answer wins: Migration Center inventories the estate and estimates target size and cost before a plan is funded.

### Question 20 — B

Answer: Set the RTO and RPO targets → choose the DR pattern that meets them → build and replicate the standby environment → fail over in a game day and record the result. Targets drive the pattern, the pattern drives the build, and only a rehearsal proves the numbers. Local study-map skill 1.9 (Migration Planning and Future Improvement), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 1 (designing and planning): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. The pattern has no basis until the targets exist, and the drill cannot precede the build. Why the correct answer wins: Targets drive the pattern, the pattern drives the build, and only a rehearsal proves the numbers.
- **B:** Correct. In this case: Targets drive the pattern, the pattern drives the build, and only a rehearsal proves the numbers.
- **C:** Incorrect for this question. Building before the targets and pattern are chosen risks an environment that cannot meet either. Why the correct answer wins: Targets drive the pattern, the pattern drives the build, and only a rehearsal proves the numbers.
- **D:** Incorrect for this question. A failover drill with no targets or standby environment proves nothing. Why the correct answer wins: Targets drive the pattern, the pattern drives the build, and only a rehearsal proves the numbers.

### Question 21 — C

Answer: Use HA VPN with two tunnels. Two tunnels across two interfaces survive one path failing, and the SLA depends on that. Local study-map skill 2.1 (Hybrid and Multicloud Connectivity), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 2 (managing and provisioning): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. CDN caches responses at edge locations, which cuts origin load and latency for repeat reads. Why the correct answer wins: Two tunnels across two interfaces survive one path failing, and the SLA depends on that.
- **B:** Incorrect for this question. A dedicated circuit gives predictable bandwidth and a private path at a colocation facility. Why the correct answer wins: Two tunnels across two interfaces survive one path failing, and the SLA depends on that.
- **C:** Correct. In this case: Two tunnels across two interfaces survive one path failing, and the SLA depends on that.
- **D:** Incorrect for this question. Cloud NAT lets private instances reach the internet without an external address. Why the correct answer wins: Two tunnels across two interfaces survive one path failing, and the SLA depends on that.

### Question 22 — D, E

Answers: Deploy Cloud NAT for outbound traffic; Enable Private Google Access on the subnet. Cloud NAT carries outbound internet traffic, and Private Google Access reaches the APIs from an internal address. Cloud NAT lets private instances reach the internet without an external address. Private Google Access reaches Google APIs from an internal address without a proxy or a NAT gateway. Local study-map skill 2.1 (Hybrid and Multicloud Connectivity), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 2 (managing and provisioning): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. Cloud Armor filters requests at the edge with allow and deny rules and adaptive protection. Why the correct answer wins: Cloud NAT carries outbound internet traffic, and Private Google Access reaches the APIs from an internal address.
- **B:** Incorrect for this question. IAP authenticates and authorises each request before it reaches the backend, with no VPN. Why the correct answer wins: Cloud NAT carries outbound internet traffic, and Private Google Access reaches the APIs from an internal address.
- **C:** Incorrect for this question. CDN caches responses at edge locations, which cuts origin load and latency for repeat reads. Why the correct answer wins: Cloud NAT carries outbound internet traffic, and Private Google Access reaches the APIs from an internal address.
- **D:** Correct. Private Google Access reaches Google APIs from an internal address without a proxy or a NAT gateway. In this case: Cloud NAT carries outbound internet traffic, and Private Google Access reaches the APIs from an internal address.
- **E:** Correct. Cloud NAT lets private instances reach the internet without an external address. In this case: Cloud NAT carries outbound internet traffic, and Private Google Access reaches the APIs from an internal address.

### Question 23 — C

Answer: Add a lifecycle rule that transitions and then deletes. A lifecycle rule transitions and then deletes on age, so retention stops depending on a person. A lifecycle rule acts on object age or class, so retention stops depending on a person. Local study-map skill 2.2 (Storage Configuration and Lifecycle), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 2 (managing and provisioning): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. The appliance ships the data physically when the network would take months to carry it. Why the correct answer wins: A lifecycle rule transitions and then deletes on age, so retention stops depending on a person.
- **B:** Incorrect for this question. Nearline suits data read about once a month and charges for early deletion. Why the correct answer wins: A lifecycle rule transitions and then deletes on age, so retention stops depending on a person.
- **C:** Correct. A lifecycle rule acts on object age or class, so retention stops depending on a person. In this case: A lifecycle rule transitions and then deletes on age, so retention stops depending on a person.
- **D:** Incorrect for this question. Autoclass moves each object between classes as its access pattern changes, with no lifecycle rules to maintain. Why the correct answer wins: A lifecycle rule transitions and then deletes on age, so retention stops depending on a person.

### Question 24 — A

Answer: Partition the table on the date column. Partitioning limits each query to the date ranges it names, so it scans less. Local study-map skill 2.2 (Storage Configuration and Lifecycle), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 2 (managing and provisioning): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Correct. In this case: Partitioning limits each query to the date ranges it names, so it scans less.
- **B:** Incorrect for this question. Clustering sorts within partitions so a filtered query reads fewer blocks. Why the correct answer wins: Partitioning limits each query to the date ranges it names, so it scans less.
- **C:** Incorrect for this question. On-demand bills per byte scanned, which is cheap for sparse use and unpredictable at scale. Why the correct answer wins: Partitioning limits each query to the date ranges it names, so it scans less.
- **D:** Incorrect for this question. The view stores the aggregate result and refreshes incrementally as base data arrives. Why the correct answer wins: Partitioning limits each query to the date ranges it names, so it scans less.

### Question 25 — A, E

Answers: Use a dual-region bucket; Enable object versioning. The dual-region bucket survives one region loss, and versioning keeps a noncurrent copy on overwrite. A dual-region bucket keeps two replicas in a chosen pair of regions and survives one region loss. Versioning keeps a noncurrent copy when an object is overwritten or deleted. Local study-map skill 2.2 (Storage Configuration and Lifecycle), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 2 (managing and provisioning): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Correct. A dual-region bucket keeps two replicas in a chosen pair of regions and survives one region loss. In this case: The dual-region bucket survives one region loss, and versioning keeps a noncurrent copy on overwrite.
- **B:** Incorrect for this question. Archive is cheapest to hold and slowest and most expensive to retrieve. Why the correct answer wins: The dual-region bucket survives one region loss, and versioning keeps a noncurrent copy on overwrite.
- **C:** Incorrect for this question. Filestore provides a managed NFS export that many clients can mount at once. Why the correct answer wins: The dual-region bucket survives one region loss, and versioning keeps a noncurrent copy on overwrite.
- **D:** Incorrect for this question. Local SSD is the fastest ephemeral option and loses its data when the VM stops. Why the correct answer wins: The dual-region bucket survives one region loss, and versioning keeps a noncurrent copy on overwrite.
- **E:** Correct. Versioning keeps a noncurrent copy when an object is overwritten or deleted. In this case: The dual-region bucket survives one region loss, and versioning keeps a noncurrent copy on overwrite.

### Question 26 — B

Answer: Use a custom machine type sized to the workload. Custom vCPU and memory avoid paying for a fixed shape that over-provisions one dimension. Local study-map skill 2.3 (Compute Provisioning and Patch Management), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 2 (managing and provisioning): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. Sole tenancy keeps the physical host dedicated, which matters for licensing or isolation rules. Why the correct answer wins: Custom vCPU and memory avoid paying for a fixed shape that over-provisions one dimension.
- **B:** Correct. In this case: Custom vCPU and memory avoid paying for a fixed shape that over-provisions one dimension.
- **C:** Incorrect for this question. Local SSD is the fastest ephemeral option and loses its data when the VM stops. Why the correct answer wins: Custom vCPU and memory avoid paying for a fixed shape that over-provisions one dimension.
- **D:** Incorrect for this question. Spot capacity costs far less but can be reclaimed with 30 seconds of notice. Why the correct answer wins: Custom vCPU and memory avoid paying for a fixed shape that over-provisions one dimension.

### Question 27 — A, B

Answers: Run the batch tier on Spot VMs; Buy committed use discounts for the steady baseline. Spot capacity covers the burst, and a commitment discounts the capacity that runs constantly. Spot capacity costs far less but can be reclaimed with 30 seconds of notice. A one- or three-year commitment discounts the capacity that runs constantly, not the peaks. Local study-map skill 2.3 (Compute Provisioning and Patch Management), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 2 (managing and provisioning): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Correct. Spot capacity costs far less but can be reclaimed with 30 seconds of notice. In this case: Spot capacity covers the burst, and a commitment discounts the capacity that runs constantly.
- **B:** Correct. A one- or three-year commitment discounts the capacity that runs constantly, not the peaks. In this case: Spot capacity covers the burst, and a commitment discounts the capacity that runs constantly.
- **C:** Incorrect for this question. Local SSD is the fastest ephemeral option and loses its data when the VM stops. Why the correct answer wins: Spot capacity covers the burst, and a commitment discounts the capacity that runs constantly.
- **D:** Incorrect for this question. Showing owners their own spend changes behaviour more reliably than a central report. Why the correct answer wins: Spot capacity covers the burst, and a commitment discounts the capacity that runs constantly.
- **E:** Incorrect for this question. E2 shapes trade peak performance for a lower price on workloads that do not need it. Why the correct answer wins: Spot capacity covers the burst, and a commitment discounts the capacity that runs constantly.

### Question 28 — B

Answer: Enable node auto-provisioning. Auto-provisioning adds node pools on demand for pending pods instead of pre-sizing them. Local study-map skill 2.4 (Container Orchestration), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 2 (managing and provisioning): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. A fleet gives one policy and identity plane across clusters without merging their networks. Why the correct answer wins: Auto-provisioning adds node pools on demand for pending pods instead of pre-sizing them.
- **B:** Correct. In this case: Auto-provisioning adds node pools on demand for pending pods instead of pre-sizing them.
- **C:** Incorrect for this question. Network policy restricts pod-to-pod traffic inside the cluster, which a firewall rule cannot see. Why the correct answer wins: Auto-provisioning adds node pools on demand for pending pods instead of pre-sizing them.
- **D:** Incorrect for this question. The channel bounds the version drift and the window bounds when automatic upgrades may run. Why the correct answer wins: Auto-provisioning adds node pools on demand for pending pods instead of pre-sizing them.

### Question 29 — D

Answer: Pin a release channel and a maintenance window. The channel bounds the version drift and the maintenance window bounds when upgrades may run. Local study-map skill 2.4 (Container Orchestration), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 2 (managing and provisioning): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. Network policy restricts pod-to-pod traffic inside the cluster, which a firewall rule cannot see. Why the correct answer wins: The channel bounds the version drift and the maintenance window bounds when upgrades may run.
- **B:** Incorrect for this question. A fleet gives one policy and identity plane across clusters without merging their networks. Why the correct answer wins: The channel bounds the version drift and the maintenance window bounds when upgrades may run.
- **C:** Incorrect for this question. Auto-provisioning adds node pools on demand for pending pods instead of pre-sizing them. Why the correct answer wins: The channel bounds the version drift and the maintenance window bounds when upgrades may run.
- **D:** Correct. In this case: The channel bounds the version drift and the maintenance window bounds when upgrades may run.

### Question 30 — C

Answer: Create the project and enable APIs → build a Shared VPC with private subnets → create a regional private cluster with Workload Identity Federation for GKE → deploy through Binary Authorization. Network and identity exist before the cluster, and the admission policy is enforceable only once the cluster is running. Local study-map skill 2.4 (Container Orchestration), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 2 (managing and provisioning): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. The project precedes its network, and the deploy step belongs after the cluster rather than in the middle. Why the correct answer wins: Network and identity exist before the cluster, and the admission policy is enforceable only once the cluster is running.
- **B:** Incorrect for this question. A private cluster needs the shared network first, and the APIs must be enabled before any resource is created. Why the correct answer wins: Network and identity exist before the cluster, and the admission policy is enforceable only once the cluster is running.
- **C:** Correct. In this case: Network and identity exist before the cluster, and the admission policy is enforceable only once the cluster is running.
- **D:** Incorrect for this question. Admission control cannot run before a cluster exists, and no resource can be created before its project. Why the correct answer wins: Network and identity exist before the cluster, and the admission policy is enforceable only once the cluster is running.

### Question 31 — C

Answer: Raise the request concurrency setting. Concurrency packs more simultaneous requests into each instance before another is started. Local study-map skill 2.5 (Serverless Configuration), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 2 (managing and provisioning): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. The flexible environment runs a custom runtime on managed VMs but does not scale to zero. Why the correct answer wins: Concurrency packs more simultaneous requests into each instance before another is started.
- **B:** Incorrect for this question. Keeping warm instances removes cold starts at the cost of paying for idle capacity. Why the correct answer wins: Concurrency packs more simultaneous requests into each instance before another is started.
- **C:** Correct. In this case: Concurrency packs more simultaneous requests into each instance before another is started.
- **D:** Incorrect for this question. Serverless GPU attachment suits bursty inference where a reserved node would idle. Why the correct answer wins: Concurrency packs more simultaneous requests into each instance before another is started.

### Question 32 — B

Answer: Manage the resources with Terraform. Terraform holds the desired state and produces a plan that a reviewer can read before apply. Terraform holds desired state in code, plans the diff, and applies it through a provider. Local study-map skill 2.6 (Infrastructure as Code), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 2 (managing and provisioning): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. The CLI exposes every API as a command that can be scripted and logged. Why the correct answer wins: Terraform holds the desired state and produces a plan that a reviewer can read before apply.
- **B:** Correct. Terraform holds desired state in code, plans the diff, and applies it through a provider. In this case: Terraform holds the desired state and produces a plan that a reviewer can read before apply.
- **C:** Incorrect for this question. Config Connector reconciles Google Cloud resources from Kubernetes manifests alongside the workloads. Why the correct answer wins: Terraform holds the desired state and produces a plan that a reviewer can read before apply.
- **D:** Incorrect for this question. Deployment Manager is the native but older templating service with no plan step. Why the correct answer wins: Terraform holds the desired state and produces a plan that a reviewer can read before apply.

### Question 33 — C

Answer: Orchestrate the workflow in Agent Platform Pipelines. Pipelines runs each step as a container with lineage and caching, so a rerun is reproducible. Local study-map skill 2.7 (Agent Platform ML Workflows), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 2 (managing and provisioning): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. Scheduler fires a job on a cron or App Engine schedule and retries on failure. Why the correct answer wins: Pipelines runs each step as a container with lineage and caching, so a rerun is reproducible.
- **B:** Incorrect for this question. A Dataproc cluster runs open-source Spark and Hadoop with jobs that need a persistent cluster. Why the correct answer wins: Pipelines runs each step as a container with lineage and caching, so a rerun is reproducible.
- **C:** Correct. In this case: Pipelines runs each step as a container with lineage and caching, so a rerun is reproducible.
- **D:** Incorrect for this question. Batch prediction reads a file and writes predictions without holding serving capacity. Why the correct answer wins: Pipelines runs each step as a container with lineage and caching, so a rerun is reproducible.

### Question 34 — C

Answer: Use the Vision API for the images. The prebuilt Vision model labels, detects, and reads text without training a model. Local study-map skill 2.8 (Prebuilt AI APIs and Model Garden), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 2 (managing and provisioning): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. The prebuilt speech model transcribes audio including domain phrases through adaptation. Why the correct answer wins: The prebuilt Vision model labels, detects, and reads text without training a model.
- **B:** Incorrect for this question. The translation model handles 100 or more languages without custom training. Why the correct answer wins: The prebuilt Vision model labels, detects, and reads text without training a model.
- **C:** Correct. In this case: The prebuilt Vision model labels, detects, and reads text without training a model.
- **D:** Incorrect for this question. A Document AI processor extracts structured fields from forms and invoices with layout awareness. Why the correct answer wins: The prebuilt Vision model labels, detects, and reads text without training a model.

### Question 35 — C

Answer: Create the Pub/Sub topic and subscription → design the Dataflow windowing and allowed lateness → deploy the streaming job with a dead-letter path → monitor watermark lag and backfill from the raw archive. The source exists before the job, the window policy is chosen before deployment, and monitoring follows the running pipeline. Local study-map skill 2.8 (Prebuilt AI APIs and Model Garden), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 2 (managing and provisioning): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. A job cannot start without its topic, and the window policy belongs in the design, not after deployment. Why the correct answer wins: The source exists before the job, the window policy is chosen before deployment, and monitoring follows the running pipeline.
- **B:** Incorrect for this question. Monitoring before deployment observes nothing, and the topic is created before the job. Why the correct answer wins: The source exists before the job, the window policy is chosen before deployment, and monitoring follows the running pipeline.
- **C:** Correct. In this case: The source exists before the job, the window policy is chosen before deployment, and monitoring follows the running pipeline.
- **D:** Incorrect for this question. There is nothing to monitor before the job runs, and the job needs a topic. Why the correct answer wins: The source exists before the job, the window policy is chosen before deployment, and monitoring follows the running pipeline.

### Question 36 — B

Answer: Grant a predefined role at the narrowest resource. A predefined role grants the curated permission set for one job at the level it is bound to. Local study-map skill 3.1 (IAM and Least Privilege), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 3 (security and compliance): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. An API key identifies a project and does not authorise a user, so it cannot express least privilege. Why the correct answer wins: A predefined role grants the curated permission set for one job at the level it is bound to.
- **B:** Correct. In this case: A predefined role grants the curated permission set for one job at the level it is bound to.
- **C:** Incorrect for this question. A bastion is still an internet-facing host that must be patched and watched. Why the correct answer wins: A predefined role grants the curated permission set for one job at the level it is bound to.
- **D:** Incorrect for this question. A custom role expresses least privilege when no predefined role matches the job exactly. Why the correct answer wins: A predefined role grants the curated permission set for one job at the level it is bound to.

### Question 37 — D, E

Answers: Add an IAM condition on the binding; Apply an IAM deny policy. The condition narrows when the grant applies, and the deny policy overrides every allow beneath it. A condition narrows when a grant applies, for example to a time window or a resource prefix. A deny policy overrides every allow beneath it, which is how an exception is made impossible. Local study-map skill 3.1 (IAM and Least Privilege), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 3 (security and compliance): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. A bastion is still an internet-facing host that must be patched and watched. Why the correct answer wins: The condition narrows when the grant applies, and the deny policy overrides every allow beneath it.
- **B:** Incorrect for this question. A predefined role grants the curated permission set for one job at the level it is bound to. Why the correct answer wins: The condition narrows when the grant applies, and the deny policy overrides every allow beneath it.
- **C:** Incorrect for this question. Labels attribute spend in billing export; they do not grant or restrict access. Why the correct answer wins: The condition narrows when the grant applies, and the deny policy overrides every allow beneath it.
- **D:** Correct. A deny policy overrides every allow beneath it, which is how an exception is made impossible. In this case: The condition narrows when the grant applies, and the deny policy overrides every allow beneath it.
- **E:** Correct. A condition narrows when a grant applies, for example to a time window or a resource prefix. In this case: The condition narrows when the grant applies, and the deny policy overrides every allow beneath it.

### Question 38 — A

Answer: Create a folder per environment and bind roles there. A folder binding inherits to every project beneath it, so new projects start with the right access. Local study-map skill 3.2 (Resource Hierarchy and Organization Policy), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 3 (security and compliance): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Correct. In this case: A folder binding inherits to every project beneath it, so new projects start with the right access.
- **B:** Incorrect for this question. A project is the boundary for quota, billing, and most IAM inheritance. Why the correct answer wins: A folder binding inherits to every project beneath it, so new projects start with the right access.
- **C:** Incorrect for this question. A predefined role grants the curated permission set for one job at the level it is bound to. Why the correct answer wins: A folder binding inherits to every project beneath it, so new projects start with the right access.
- **D:** Incorrect for this question. Labels attribute spend in billing export; they do not grant or restrict access. Why the correct answer wins: A folder binding inherits to every project beneath it, so new projects start with the right access.

### Question 39 — C

Answer: Enforce the control with an organization policy constraint. An organization policy blocks the action across every project regardless of who holds the role. Local study-map skill 3.2 (Resource Hierarchy and Organization Policy), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 3 (security and compliance): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. A folder binding inherits to every project beneath it, so new projects start with the right access. Why the correct answer wins: An organization policy blocks the action across every project regardless of who holds the role.
- **B:** Incorrect for this question. Labels attribute spend in billing export; they do not grant or restrict access. Why the correct answer wins: An organization policy blocks the action across every project regardless of who holds the role.
- **C:** Correct. In this case: An organization policy blocks the action across every project regardless of who holds the role.
- **D:** Incorrect for this question. A project is the boundary for quota, billing, and most IAM inheritance. Why the correct answer wins: An organization policy blocks the action across every project regardless of who holds the role.

### Question 40 — A

Answer: Create the key ring in the same region as the data. A regional key ring keeps the key material in the region where the data lives. A regional key cannot encrypt a resource in another region, which is why residency drives key placement. Local study-map skill 3.3 (Encryption, CMEK, and Secrets), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 3 (security and compliance): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Correct. A regional key cannot encrypt a resource in another region, which is why residency drives key placement. In this case: A regional key ring keeps the key material in the region where the data lives.
- **B:** Incorrect for this question. Cloud HSM keeps the key material in a hardware module that meets FIPS 140-2 level 3. Why the correct answer wins: A regional key ring keeps the key material in the region where the data lives.
- **C:** Incorrect for this question. Secret Manager versions the secret, controls access by IAM, and can rotate it. Why the correct answer wins: A regional key ring keeps the key material in the region where the data lives.
- **D:** Incorrect for this question. CSEK is held by the caller and never stored by Google, so losing it loses the object. Why the correct answer wins: A regional key ring keeps the key material in the region where the data lives.

### Question 41 — D, E

Answers: Encrypt with a customer-managed key in Cloud KMS; Set an automatic rotation period on the key. A customer-managed key gives the retailer control, and automatic rotation issues a new version on schedule. CMEK lets you control the key lifecycle, rotation, and the ability to revoke access to the data. Rotation issues a new key version on schedule and keeps old versions for decryption. Local study-map skill 3.3 (Encryption, CMEK, and Secrets), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 3 (security and compliance): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. Cloud HSM keeps the key material in a hardware module that meets FIPS 140-2 level 3. Why the correct answer wins: A customer-managed key gives the retailer control, and automatic rotation issues a new version on schedule.
- **B:** Incorrect for this question. CSEK is held by the caller and never stored by Google, so losing it loses the object. Why the correct answer wins: A customer-managed key gives the retailer control, and automatic rotation issues a new version on schedule.
- **C:** Incorrect for this question. An environment variable is visible to anything that can read the instance metadata or the process list. Why the correct answer wins: A customer-managed key gives the retailer control, and automatic rotation issues a new version on schedule.
- **D:** Correct. CMEK lets you control the key lifecycle, rotation, and the ability to revoke access to the data. In this case: A customer-managed key gives the retailer control, and automatic rotation issues a new version on schedule.
- **E:** Correct. Rotation issues a new key version on schedule and keeps old versions for decryption. In this case: A customer-managed key gives the retailer control, and automatic rotation issues a new version on schedule.

### Question 42 — A

Answer: Put the projects inside a VPC Service Controls perimeter. A service perimeter blocks data movement out of the covered services even for a principal with the role. Local study-map skill 3.4 (VPC Service Controls and Network Security), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 3 (security and compliance): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Correct. In this case: A service perimeter blocks data movement out of the covered services even for a principal with the role.
- **B:** Incorrect for this question. A policy above the project applies to every current and future network beneath it. Why the correct answer wins: A service perimeter blocks data movement out of the covered services even for a principal with the role.
- **C:** Incorrect for this question. A deny policy overrides every allow beneath it, which is how an exception is made impossible. Why the correct answer wins: A service perimeter blocks data movement out of the covered services even for a principal with the role.
- **D:** Incorrect for this question. Labels attribute spend in billing export; they do not grant or restrict access. Why the correct answer wins: A service perimeter blocks data movement out of the covered services even for a principal with the role.

### Question 43 — B

Answer: Put Identity-Aware Proxy in front of the application. Identity-Aware Proxy authenticates and authorises each request before it reaches the backend. Local study-map skill 3.5 (Secure Remote Access and Zero Trust), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 3 (security and compliance): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. A bastion is still an internet-facing host that must be patched and watched. Why the correct answer wins: Identity-Aware Proxy authenticates and authorises each request before it reaches the backend.
- **B:** Correct. In this case: Identity-Aware Proxy authenticates and authorises each request before it reaches the backend.
- **C:** Incorrect for this question. Private Google Access reaches Google APIs from an internal address without a proxy or a NAT gateway. Why the correct answer wins: Identity-Aware Proxy authenticates and authorises each request before it reaches the backend.
- **D:** Incorrect for this question. Cloud NAT lets private instances reach the internet without an external address. Why the correct answer wins: Identity-Aware Proxy authenticates and authorises each request before it reaches the backend.

### Question 44 — D

Answer: Enable Artifact Analysis scanning on the repository. Scanning reports known vulnerabilities in the image layers before deployment. Local study-map skill 3.6 (Software Supply Chain Security), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 3 (security and compliance): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. Artifact Registry holds the image with IAM-scoped access and vulnerability metadata. Why the correct answer wins: Scanning reports known vulnerabilities in the image layers before deployment.
- **B:** Incorrect for this question. Provenance states what built the artifact from which source, which is the evidence a supply-chain audit asks for. Why the correct answer wins: Scanning reports known vulnerabilities in the image layers before deployment.
- **C:** Incorrect for this question. Only images with a valid attestation from a trusted builder may deploy. Why the correct answer wins: Scanning reports known vulnerabilities in the image layers before deployment.
- **D:** Correct. In this case: Scanning reports known vulnerabilities in the image layers before deployment.

### Question 45 — B, E

Answers: Require Binary Authorization attestations; Record build provenance for the artifact. Admission control rejects unattested images, and provenance records what built the artifact from which source. Only images with a valid attestation from a trusted builder may deploy. Provenance states what built the artifact from which source, which is the evidence a supply-chain audit asks for. Local study-map skill 3.6 (Software Supply Chain Security), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 3 (security and compliance): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. Network policy restricts pod-to-pod traffic inside the cluster, which a firewall rule cannot see. Why the correct answer wins: Admission control rejects unattested images, and provenance records what built the artifact from which source.
- **B:** Correct. Provenance states what built the artifact from which source, which is the evidence a supply-chain audit asks for. In this case: Admission control rejects unattested images, and provenance records what built the artifact from which source.
- **C:** Incorrect for this question. Artifact Registry holds the image with IAM-scoped access and vulnerability metadata. Why the correct answer wins: Admission control rejects unattested images, and provenance records what built the artifact from which source.
- **D:** Incorrect for this question. Scanning reports known vulnerabilities in the image layers before deployment. Why the correct answer wins: Admission control rejects unattested images, and provenance records what built the artifact from which source.
- **E:** Correct. Only images with a valid attestation from a trusted builder may deploy. In this case: Admission control rejects unattested images, and provenance records what built the artifact from which source.

### Question 46 — C

Answer: Screen prompts and responses with Model Armor. Model Armor detects prompt injection and unsafe content before and after the model call. Local study-map skill 3.7 (Securing AI Workloads), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 3 (security and compliance): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. The access level adds device and network conditions to the perimeter rule. Why the correct answer wins: Model Armor detects prompt injection and unsafe content before and after the model call.
- **B:** Incorrect for this question. Sensitive Data Protection finds and redacts, tokenizes, or format-preservingly encrypts sensitive fields. Why the correct answer wins: Model Armor detects prompt injection and unsafe content before and after the model call.
- **C:** Correct. In this case: Model Armor detects prompt injection and unsafe content before and after the model call.
- **D:** Incorrect for this question. Security Command Center aggregates misconfiguration and threat findings across the organization. Why the correct answer wins: Model Armor detects prompt injection and unsafe content before and after the model call.

### Question 47 — A

Answer: Enable Data Access audit logs. Data Access logging is off by default and must be enabled before reads and writes are recorded. Local study-map skill 3.8 (Compliance, Residency, and Audit Logging), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 3 (security and compliance): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Correct. In this case: Data Access logging is off by default and must be enabled before reads and writes are recorded.
- **B:** Incorrect for this question. Admin Activity records configuration changes and cannot be disabled. Why the correct answer wins: Data Access logging is off by default and must be enabled before reads and writes are recorded.
- **C:** Incorrect for this question. Access Transparency records when Google staff access your content, which is evidence of oversight, not of user activity. Why the correct answer wins: Data Access logging is off by default and must be enabled before reads and writes are recorded.
- **D:** Incorrect for this question. The metric turns a log pattern into a series that can be alerted on and charted. Why the correct answer wins: Data Access logging is off by default and must be enabled before reads and writes are recorded.

### Question 48 — D

Answer: Route the logs with an aggregated sink. An aggregated sink collects logs from every project into one destination. Local study-map skill 3.8 (Compliance, Residency, and Audit Logging), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 3 (security and compliance): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. The runbook records the diagnostic steps so the response does not depend on who is awake. Why the correct answer wins: An aggregated sink collects logs from every project into one destination.
- **B:** Incorrect for this question. The dashboard gives the team one view of the same signals during an incident. Why the correct answer wins: An aggregated sink collects logs from every project into one destination.
- **C:** Incorrect for this question. The metric turns a log pattern into a series that can be alerted on and charted. Why the correct answer wins: An aggregated sink collects logs from every project into one destination.
- **D:** Correct. In this case: An aggregated sink collects logs from every project into one destination.

### Question 49 — C

Answer: Enable data access audit logs for the services in scope → create a locked log bucket with the required retention → route the logs with an aggregated sink → query and export the evidence for the auditor. Logs must be enabled before they can be routed, and retention is fixed on the bucket before the sink writes to it. Local study-map skill 3.8 (Compliance, Residency, and Audit Logging), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 3 (security and compliance): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. A sink without a destination bucket or enabled logs captures nothing. Why the correct answer wins: Logs must be enabled before they can be routed, and retention is fixed on the bucket before the sink writes to it.
- **B:** Incorrect for this question. A sink that is created last is needed before any evidence can be queried from the destination. Why the correct answer wins: Logs must be enabled before they can be routed, and retention is fixed on the bucket before the sink writes to it.
- **C:** Correct. In this case: Logs must be enabled before they can be routed, and retention is fixed on the bucket before the sink writes to it.
- **D:** Incorrect for this question. There is no evidence to query before logging and routing exist. Why the correct answer wins: Logs must be enabled before they can be routed, and retention is fixed on the bucket before the sink writes to it.

### Question 50 — A

Answer: Adopt trunk-based development with short-lived branches. Short-lived branches reduce merge conflict and keep the mainline deployable. Local study-map skill 4.1 (SDLC and CI/CD Design), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 4 (analyzing and optimizing): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Correct. In this case: Short-lived branches reduce merge conflict and keep the mainline deployable.
- **B:** Incorrect for this question. The flag separates deployment from release, so the code can ship dark and be turned off instantly. Why the correct answer wins: Short-lived branches reduce merge conflict and keep the mainline deployable.
- **C:** Incorrect for this question. A rebuild produces a different artifact, so the test result no longer applies to production. Why the correct answer wins: Short-lived branches reduce merge conflict and keep the mainline deployable.
- **D:** Incorrect for this question. A rolling replacement keeps capacity but exposes the whole fleet before the signal is trusted. Why the correct answer wins: Short-lived branches reduce merge conflict and keep the mainline deployable.

### Question 51 — A, B

Answers: Require a reviewed pull request and a passing plan; Promote the same tested artifact between environments. The gate makes review mandatory, and promotion keeps one immutable artifact. The gate makes a second person check the change and its plan before it can apply. Promotion moves one immutable artifact forward, so what was tested is what runs. Local study-map skill 4.1 (SDLC and CI/CD Design), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 4 (analyzing and optimizing): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Correct. Promotion moves one immutable artifact forward, so what was tested is what runs. In this case: The gate makes review mandatory, and promotion keeps one immutable artifact.
- **B:** Correct. The gate makes a second person check the change and its plan before it can apply. In this case: The gate makes review mandatory, and promotion keeps one immutable artifact.
- **C:** Incorrect for this question. A rolling replacement keeps capacity but exposes the whole fleet before the signal is trusted. Why the correct answer wins: The gate makes review mandatory, and promotion keeps one immutable artifact.
- **D:** Incorrect for this question. A budget alerts on spend but does not stop it. Why the correct answer wins: The gate makes review mandatory, and promotion keeps one immutable artifact.
- **E:** Incorrect for this question. A rebuild produces a different artifact, so the test result no longer applies to production. Why the correct answer wins: The gate makes review mandatory, and promotion keeps one immutable artifact.

### Question 52 — D

Answer: Inspect the trace waterfall in Cloud Trace. Trace shows how one request spent its time across services and calls. Local study-map skill 4.2 (Root Cause Analysis), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 4 (analyzing and optimizing): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. Recommender reports idle and over-provisioned resources with the estimated saving. Why the correct answer wins: Trace shows how one request spent its time across services and calls.
- **B:** Incorrect for this question. The check measures availability from outside, which no internal metric can prove. Why the correct answer wins: Trace shows how one request spent its time across services and calls.
- **C:** Incorrect for this question. The dashboard gives the team one view of the same signals during an incident. Why the correct answer wins: Trace shows how one request spent its time across services and calls.
- **D:** Correct. In this case: Trace shows how one request spent its time across services and calls.

### Question 53 — A, E

Answers: Query the entries in Cloud Logging; Group the exceptions in Error Reporting. Logging holds the event text, and Error Reporting clusters the recurring stack traces. Logging holds the event text and structured fields that explain what happened at a moment. Error Reporting clusters recurring stack traces so a new failure is not lost in the log volume. Local study-map skill 4.2 (Root Cause Analysis), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 4 (analyzing and optimizing): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Correct. Logging holds the event text and structured fields that explain what happened at a moment. In this case: Logging holds the event text, and Error Reporting clusters the recurring stack traces.
- **B:** Incorrect for this question. The dashboard gives the team one view of the same signals during an incident. Why the correct answer wins: Logging holds the event text, and Error Reporting clusters the recurring stack traces.
- **C:** Incorrect for this question. The runbook records the diagnostic steps so the response does not depend on who is awake. Why the correct answer wins: Logging holds the event text, and Error Reporting clusters the recurring stack traces.
- **D:** Incorrect for this question. An SLO ties the alert to the promise the users care about rather than to a raw resource threshold. Why the correct answer wins: Logging holds the event text, and Error Reporting clusters the recurring stack traces.
- **E:** Correct. Error Reporting clusters recurring stack traces so a new failure is not lost in the log volume. In this case: Logging holds the event text, and Error Reporting clusters the recurring stack traces.

### Question 54 — A

Answer: Run a load test at the expected peak. The load test measures the system at the concurrency the business expects, before the peak. Local study-map skill 4.3 (Testing and Validation), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 4 (analyzing and optimizing): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Correct. In this case: The load test measures the system at the concurrency the business expects, before the peak.
- **B:** Incorrect for this question. The experiment proves the failover path works while the impact is controlled. Why the correct answer wins: The load test measures the system at the concurrency the business expects, before the peak.
- **C:** Incorrect for this question. The pyramid puts volume where it is cheap and keeps end-to-end tests for the critical paths. Why the correct answer wins: The load test measures the system at the concurrency the business expects, before the peak.
- **D:** Incorrect for this question. An independent test attempts the attack the design claims to prevent. Why the correct answer wins: The load test measures the system at the concurrency the business expects, before the peak.

### Question 55 — D

Answer: Run a pilot-light standby. Only core data and configuration stay warm, so recovery starts the compute and takes minutes. Local study-map skill 4.4 (Disaster Recovery and Business Continuity), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 4 (analyzing and optimizing): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. Restoring from backup is the cheapest option and the slowest to recover. Why the correct answer wins: Only core data and configuration stay warm, so recovery starts the compute and takes minutes.
- **B:** Incorrect for this question. Both regions serve traffic, so a regional loss is absorbed without a failover decision. Why the correct answer wins: Only core data and configuration stay warm, so recovery starts the compute and takes minutes.
- **C:** Incorrect for this question. A running but smaller copy recovers in a short window at a continuous cost. Why the correct answer wins: Only core data and configuration stay warm, so recovery starts the compute and takes minutes.
- **D:** Correct. In this case: Only core data and configuration stay warm, so recovery starts the compute and takes minutes.

### Question 56 — D

Answer: Act on the Recommender suggestions. Recommender reports idle and over-provisioned resources with the estimated saving for each. Local study-map skill 4.5 (Cost Optimization), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 4 (analyzing and optimizing): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. A budget alerts on spend but does not stop it. Why the correct answer wins: Recommender reports idle and over-provisioned resources with the estimated saving for each.
- **B:** Incorrect for this question. Labels attribute spend in billing export; they do not grant or restrict access. Why the correct answer wins: Recommender reports idle and over-provisioned resources with the estimated saving for each.
- **C:** Incorrect for this question. The export attributes cost to the team and service that caused it. Why the correct answer wins: Recommender reports idle and over-provisioned resources with the estimated saving for each.
- **D:** Correct. In this case: Recommender reports idle and over-provisioned resources with the estimated saving for each.

### Question 57 — A

Answer: Export billing to BigQuery and review it per label. The export attributes spend to the labels and projects that caused it. The export attributes cost to the team and service that caused it. Local study-map skill 4.5 (Cost Optimization), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 4 (analyzing and optimizing): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Correct. The export attributes cost to the team and service that caused it. In this case: The export attributes spend to the labels and projects that caused it.
- **B:** Incorrect for this question. Labels attribute spend in billing export; they do not grant or restrict access. Why the correct answer wins: The export attributes spend to the labels and projects that caused it.
- **C:** Incorrect for this question. A budget alerts on spend but does not stop it. Why the correct answer wins: The export attributes spend to the labels and projects that caused it.
- **D:** Incorrect for this question. Showing owners their own spend changes behaviour more reliably than a central report. Why the correct answer wins: The export attributes spend to the labels and projects that caused it.

### Question 58 — B

Answer: Inspect the query plan and bytes processed → partition and cluster the table on the filter columns → rewrite the query to prune partitions → measure the new slot time and bytes scanned. The plan identifies the problem, the physical design supports pruning, and only a measurement proves improvement. Local study-map skill 4.5 (Cost Optimization), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 4 (analyzing and optimizing): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. Partitioning last ignores what the plan and the rewrite revealed. Why the correct answer wins: The plan identifies the problem, the physical design supports pruning, and only a measurement proves improvement.
- **B:** Correct. In this case: The plan identifies the problem, the physical design supports pruning, and only a measurement proves improvement.
- **C:** Incorrect for this question. Measuring before any change establishes no baseline against the plan. Why the correct answer wins: The plan identifies the problem, the physical design supports pruning, and only a measurement proves improvement.
- **D:** Incorrect for this question. The plan is the evidence that drives both the rewrite and the physical design. Why the correct answer wins: The plan identifies the problem, the physical design supports pruning, and only a measurement proves improvement.

### Question 59 — D

Answer: Route the change through a change advisory board. The board reviews risk and timing for changes that affect regulated or shared systems. Local study-map skill 4.6 (Stakeholder and Change Management), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 4 (analyzing and optimizing): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. The runbook records the diagnostic steps so the response does not depend on who is awake. Why the correct answer wins: The board reviews risk and timing for changes that affect regulated or shared systems.
- **B:** Incorrect for this question. A named rotation turns an alert into a person who is already accountable for it. Why the correct answer wins: The board reviews risk and timing for changes that affect regulated or shared systems.
- **C:** Incorrect for this question. A catalog entry gives teams a pre-approved, policy-compliant way to request the resource. Why the correct answer wins: The board reviews risk and timing for changes that affect regulated or shared systems.
- **D:** Correct. In this case: The board reviews risk and timing for changes that affect regulated or shared systems.

### Question 60 — B

Answer: Publish a service catalog entry with an approved template. A catalog entry gives teams a pre-approved, policy-compliant way to request the resource. Local study-map skill 4.7 (Service Catalog and Provisioning), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 4 (analyzing and optimizing): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. An organization policy blocks the action across every project regardless of who holds the role. Why the correct answer wins: A catalog entry gives teams a pre-approved, policy-compliant way to request the resource.
- **B:** Correct. In this case: A catalog entry gives teams a pre-approved, policy-compliant way to request the resource.
- **C:** Incorrect for this question. Terraform holds desired state in code, plans the diff, and applies it through a provider. Why the correct answer wins: A catalog entry gives teams a pre-approved, policy-compliant way to request the resource.
- **D:** Incorrect for this question. Labels attribute spend in billing export; they do not grant or restrict access. Why the correct answer wins: A catalog entry gives teams a pre-approved, policy-compliant way to request the resource.

### Question 61 — C

Answer: Roll out a canary to a small share of traffic. A canary limits the blast radius while the error and latency signals are compared. Local study-map skill 5.1 (Deployment and Release Strategy), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 5 (managing implementation): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. The flag separates deployment from release, so the code can ship dark and be turned off instantly. Why the correct answer wins: A canary limits the blast radius while the error and latency signals are compared.
- **B:** Incorrect for this question. Two identical environments let the switch be reversed instantly if the new one misbehaves. Why the correct answer wins: A canary limits the blast radius while the error and latency signals are compared.
- **C:** Correct. In this case: A canary limits the blast radius while the error and latency signals are compared.
- **D:** Incorrect for this question. A rolling replacement keeps capacity but exposes the whole fleet before the signal is trusted. Why the correct answer wins: A canary limits the blast radius while the error and latency signals are compared.

### Question 62 — A, C

Answers: Deploy blue/green with a traffic switch; Keep the previous image digest ready for rollback. Two environments let the switch be reversed instantly, and a pinned digest restores the exact artifact. Two identical environments let the switch be reversed instantly if the new one misbehaves. A pinned digest restores the exact artifact that was known good, not a rebuild of it. Local study-map skill 5.1 (Deployment and Release Strategy), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 5 (managing implementation): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Correct. A pinned digest restores the exact artifact that was known good, not a rebuild of it. In this case: Two environments let the switch be reversed instantly, and a pinned digest restores the exact artifact.
- **B:** Incorrect for this question. A rebuild produces a different artifact, so the test result no longer applies to production. Why the correct answer wins: Two environments let the switch be reversed instantly, and a pinned digest restores the exact artifact.
- **C:** Correct. Two identical environments let the switch be reversed instantly if the new one misbehaves. In this case: Two environments let the switch be reversed instantly, and a pinned digest restores the exact artifact.
- **D:** Incorrect for this question. Promotion moves one immutable artifact forward, so what was tested is what runs. Why the correct answer wins: Two environments let the switch be reversed instantly, and a pinned digest restores the exact artifact.
- **E:** Incorrect for this question. A budget alerts on spend but does not stop it. Why the correct answer wins: Two environments let the switch be reversed instantly, and a pinned digest restores the exact artifact.

### Question 63 — C

Answer: Build an immutable image and record its digest → deploy the new revision without traffic → shift a small traffic percentage and watch error and latency signals → promote to full traffic or roll back to the pinned digest. The artifact is fixed before traffic moves, and the decision to promote follows observed signals. Local study-map skill 5.1 (Deployment and Release Strategy), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 5 (managing implementation): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. Promoting before the canary step skips the signal that justifies promotion. Why the correct answer wins: The artifact is fixed before traffic moves, and the decision to promote follows observed signals.
- **B:** Incorrect for this question. Nothing can be watched before the revision exists, and the image precedes the deployment. Why the correct answer wins: The artifact is fixed before traffic moves, and the decision to promote follows observed signals.
- **C:** Correct. In this case: The artifact is fixed before traffic moves, and the decision to promote follows observed signals.
- **D:** Incorrect for this question. Full traffic before any canary step turns the first failure into an outage. Why the correct answer wins: The artifact is fixed before traffic moves, and the decision to promote follows observed signals.

### Question 64 — D

Answer: Publish the API through Apigee. Apigee adds quotas, keys, mediation, and analytics at the gateway for each consumer. Local study-map skill 5.2 (API Management), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 5 (managing implementation): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. Endpoints validates and monitors an API described by an OpenAPI or gRPC spec. Why the correct answer wins: Apigee adds quotas, keys, mediation, and analytics at the gateway for each consumer.
- **B:** Incorrect for this question. Cloud Armor filters requests at the edge with allow and deny rules and adaptive protection. Why the correct answer wins: Apigee adds quotas, keys, mediation, and analytics at the gateway for each consumer.
- **C:** Incorrect for this question. API Gateway fronts a Cloud Run or functions backend with a managed OpenAPI definition. Why the correct answer wins: Apigee adds quotas, keys, mediation, and analytics at the gateway for each consumer.
- **D:** Correct. In this case: Apigee adds quotas, keys, mediation, and analytics at the gateway for each consumer.

### Question 65 — D

Answer: Use API Gateway. API Gateway fronts a Cloud Run or functions backend with a managed OpenAPI definition. Local study-map skill 5.2 (API Management), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 5 (managing implementation): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. Endpoints validates and monitors an API described by an OpenAPI or gRPC spec. Why the correct answer wins: API Gateway fronts a Cloud Run or functions backend with a managed OpenAPI definition.
- **B:** Incorrect for this question. Apigee adds quotas, keys, mediation, and analytics at the gateway. Why the correct answer wins: API Gateway fronts a Cloud Run or functions backend with a managed OpenAPI definition.
- **C:** Incorrect for this question. Cloud Armor filters requests at the edge with allow and deny rules and adaptive protection. Why the correct answer wins: API Gateway fronts a Cloud Run or functions backend with a managed OpenAPI definition.
- **D:** Correct. In this case: API Gateway fronts a Cloud Run or functions backend with a managed OpenAPI definition.

### Question 66 — B

Answer: Migrate the database with Database Migration Service. The service replicates continuously and cuts over in a short window with the source still running. Local study-map skill 5.3 (Data and System Migration Tooling), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 5 (managing implementation): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. The service moves object data between buckets or clouds on a schedule. Why the correct answer wins: The service replicates continuously and cuts over in a short window with the source still running.
- **B:** Correct. In this case: The service replicates continuously and cuts over in a short window with the source still running.
- **C:** Incorrect for this question. The service runs scheduled loads from SaaS sources and other clouds into BigQuery. Why the correct answer wins: The service replicates continuously and cuts over in a short window with the source still running.
- **D:** Incorrect for this question. Datastream reads the source log and streams inserts, updates, and deletes with ordering preserved. Why the correct answer wins: The service replicates continuously and cuts over in a short window with the source still running.

### Question 67 — D

Answer: Copy the files with Storage Transfer Service. The service runs scheduled, filtered transfers from another cloud into a bucket. The service moves object data between buckets or clouds on a schedule. Local study-map skill 5.3 (Data and System Migration Tooling), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 5 (managing implementation): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. Migration Center inventories the servers and estimates the target size and cost. Why the correct answer wins: The service runs scheduled, filtered transfers from another cloud into a bucket.
- **B:** Incorrect for this question. The appliance ships the data physically when the network would take months to carry it. Why the correct answer wins: The service runs scheduled, filtered transfers from another cloud into a bucket.
- **C:** Incorrect for this question. The tool rewrites a VM workload into a container image so it can run on GKE. Why the correct answer wins: The service runs scheduled, filtered transfers from another cloud into a bucket.
- **D:** Correct. The service moves object data between buckets or clouds on a schedule. In this case: The service runs scheduled, filtered transfers from another cloud into a bucket.

### Question 68 — B

Answer: Inventory the estate in Migration Center → group servers into dependency-based waves → validate a pilot wave in the target landing zone → cut over wave by wave and decommission the source. Inventory precedes grouping, a pilot proves the landing zone, and decommissioning follows a completed cutover. Local study-map skill 5.3 (Data and System Migration Tooling), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 5 (managing implementation): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. Waves cannot be grouped before the inventory, and decommissioning before validation destroys the rollback path. Why the correct answer wins: Inventory precedes grouping, a pilot proves the landing zone, and decommissioning follows a completed cutover.
- **B:** Correct. In this case: Inventory precedes grouping, a pilot proves the landing zone, and decommissioning follows a completed cutover.
- **C:** Incorrect for this question. A pilot cannot be chosen before the inventory and the wave grouping. Why the correct answer wins: Inventory precedes grouping, a pilot proves the landing zone, and decommissioning follows a completed cutover.
- **D:** Incorrect for this question. Decommissioning first removes the evidence and the rollback option for every later step. Why the correct answer wins: Inventory precedes grouping, a pilot proves the landing zone, and decommissioning follows a completed cutover.

### Question 69 — D

Answer: Run the emulator in the pipeline. The emulator provides a local endpoint for tests without a billable cloud resource. Local study-map skill 5.4 (Programmatic Access and Emulators), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 5 (managing implementation): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. Terraform holds desired state in code, plans the diff, and applies it through a provider. Why the correct answer wins: The emulator provides a local endpoint for tests without a billable cloud resource.
- **B:** Incorrect for this question. Cloud Build executes the pipeline steps in a managed, isolated worker with recorded provenance. Why the correct answer wins: The emulator provides a local endpoint for tests without a billable cloud resource.
- **C:** Incorrect for this question. The CLI exposes every API as a command that can be scripted and logged. Why the correct answer wins: The emulator provides a local endpoint for tests without a billable cloud resource.
- **D:** Correct. In this case: The emulator provides a local endpoint for tests without a billable cloud resource.

### Question 70 — A

Answer: Automate the step with the gcloud CLI. The CLI exposes the API as commands that can be scripted and captured in a log. The CLI exposes every API as a command that can be scripted and logged. Local study-map skill 5.4 (Programmatic Access and Emulators), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 5 (managing implementation): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Correct. The CLI exposes every API as a command that can be scripted and logged. In this case: The CLI exposes the API as commands that can be scripted and captured in a log.
- **B:** Incorrect for this question. Cloud Code gives the editor run, debug, and deploy targets for the cluster without leaving it. Why the correct answer wins: The CLI exposes the API as commands that can be scripted and captured in a log.
- **C:** Incorrect for this question. Cloud Shell provides an authenticated terminal and editor with no local installation. Why the correct answer wins: The CLI exposes the API as commands that can be scripted and captured in a log.
- **D:** Incorrect for this question. The bq tool runs jobs and manages datasets from a terminal or a script. Why the correct answer wins: The CLI exposes the API as commands that can be scripted and captured in a log.

### Question 71 — B

Answer: Use the Google API client library with retries. The client library applies the recommended retry and backoff behaviour for the API. Local study-map skill 5.5 (Client Libraries and API Practices), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 5 (managing implementation): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. Impersonation issues a short-lived token so the test runs as the real workload identity. Why the correct answer wins: The client library applies the recommended retry and backoff behaviour for the API.
- **B:** Correct. In this case: The client library applies the recommended retry and backoff behaviour for the API.
- **C:** Incorrect for this question. An API key identifies a project and does not authorise a user, so it cannot express least privilege. Why the correct answer wins: The client library applies the recommended retry and backoff behaviour for the API.
- **D:** Incorrect for this question. The CLI exposes every API as a command that can be scripted and logged. Why the correct answer wins: The client library applies the recommended retry and backoff behaviour for the API.

### Question 72 — C

Answer: Install the Ops Agent on the instances. The Ops Agent ships host metrics and application logs to Monitoring and Logging. Local study-map skill 6.1 (Observability Design), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 6 (solution and operations excellence): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. Trace shows how one request spent its time across services and calls. Why the correct answer wins: The Ops Agent ships host metrics and application logs to Monitoring and Logging.
- **B:** Incorrect for this question. Profiler samples the running code and attributes CPU and heap to the functions responsible. Why the correct answer wins: The Ops Agent ships host metrics and application logs to Monitoring and Logging.
- **C:** Correct. In this case: The Ops Agent ships host metrics and application logs to Monitoring and Logging.
- **D:** Incorrect for this question. Error Reporting clusters recurring stack traces so a new failure is not lost in the log volume. Why the correct answer wins: The Ops Agent ships host metrics and application logs to Monitoring and Logging.

### Question 73 — A, B

Answers: Add an uptime check from several regions; Inspect the trace waterfall in Cloud Trace. The uptime check measures availability externally, and the trace shows where the request spent its time. The check measures availability from outside, which no internal metric can prove. Trace shows how one request spent its time across services and calls. Local study-map skill 6.1 (Observability Design), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 6 (solution and operations excellence): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Correct. Trace shows how one request spent its time across services and calls. In this case: The uptime check measures availability externally, and the trace shows where the request spent its time.
- **B:** Correct. The check measures availability from outside, which no internal metric can prove. In this case: The uptime check measures availability externally, and the trace shows where the request spent its time.
- **C:** Incorrect for this question. Recommender reports idle and over-provisioned resources with the estimated saving. Why the correct answer wins: The uptime check measures availability externally, and the trace shows where the request spent its time.
- **D:** Incorrect for this question. The dashboard gives the team one view of the same signals during an incident. Why the correct answer wins: The uptime check measures availability externally, and the trace shows where the request spent its time.
- **E:** Incorrect for this question. An SLO ties the alert to the promise the users care about rather than to a raw resource threshold. Why the correct answer wins: The uptime check measures availability externally, and the trace shows where the request spent its time.

### Question 74 — B

Answer: Define an SLO with an error budget. An SLO ties the alert to the user promise rather than to a raw resource threshold. Local study-map skill 6.2 (Alerting and Service Level Objectives), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 6 (solution and operations excellence): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. The policy fires when the series crosses the condition for the stated duration. Why the correct answer wins: An SLO ties the alert to the user promise rather than to a raw resource threshold.
- **B:** Correct. In this case: An SLO ties the alert to the user promise rather than to a raw resource threshold.
- **C:** Incorrect for this question. The dashboard gives the team one view of the same signals during an incident. Why the correct answer wins: An SLO ties the alert to the user promise rather than to a raw resource threshold.
- **D:** Incorrect for this question. The check measures availability from outside, which no internal metric can prove. Why the correct answer wins: An SLO ties the alert to the user promise rather than to a raw resource threshold.

### Question 75 — A

Answer: Create an alerting policy on the metric. The policy fires when the series crosses the condition for the stated duration. Local study-map skill 6.2 (Alerting and Service Level Objectives), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 6 (solution and operations excellence): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Correct. In this case: The policy fires when the series crosses the condition for the stated duration.
- **B:** Incorrect for this question. The metric turns a log pattern into a series that can be alerted on and charted. Why the correct answer wins: The policy fires when the series crosses the condition for the stated duration.
- **C:** Incorrect for this question. An SLO ties the alert to the promise the users care about rather than to a raw resource threshold. Why the correct answer wins: The policy fires when the series crosses the condition for the stated duration.
- **D:** Incorrect for this question. The dashboard gives the team one view of the same signals during an incident. Why the correct answer wins: The policy fires when the series crosses the condition for the stated duration.

### Question 76 — D

Answer: Publish a runbook per alert. The runbook records the diagnostic steps so the response does not depend on who is awake. Local study-map skill 6.3 (Release Management and Support), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 6 (solution and operations excellence): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. The support tier sets the response time and the escalation path the business expects. Why the correct answer wins: The runbook records the diagnostic steps so the response does not depend on who is awake.
- **B:** Incorrect for this question. A named rotation turns an alert into a person who is already accountable for it. Why the correct answer wins: The runbook records the diagnostic steps so the response does not depend on who is awake.
- **C:** Incorrect for this question. The dashboard gives the team one view of the same signals during an incident. Why the correct answer wins: The runbook records the diagnostic steps so the response does not depend on who is awake.
- **D:** Correct. In this case: The runbook records the diagnostic steps so the response does not depend on who is awake.

### Question 77 — D

Answer: Run a chaos experiment against a zone. The experiment proves the failover path works while the impact is controlled. Local study-map skill 6.4 (Reliability Testing), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 6 (solution and operations excellence): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. The load test measures the system at the concurrency the business expects, before launch. Why the correct answer wins: The experiment proves the failover path works while the impact is controlled.
- **B:** Incorrect for this question. An independent test attempts the attack the design claims to prevent. Why the correct answer wins: The experiment proves the failover path works while the impact is controlled.
- **C:** Incorrect for this question. A canary limits the blast radius while the error and latency signals are compared. Why the correct answer wins: The experiment proves the failover path works while the impact is controlled.
- **D:** Correct. In this case: The experiment proves the failover path works while the impact is controlled.

### Question 78 — B

Answer: Write a blameless postmortem with actions. The postmortem records cause and follow-up work, which is how the same failure is prevented. Local study-map skill 6.5 (Operational Excellence and Quality Control), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 6 (solution and operations excellence): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. The runbook records the diagnostic steps so the response does not depend on who is awake. Why the correct answer wins: The postmortem records cause and follow-up work, which is how the same failure is prevented.
- **B:** Correct. In this case: The postmortem records cause and follow-up work, which is how the same failure is prevented.
- **C:** Incorrect for this question. The dashboard gives the team one view of the same signals during an incident. Why the correct answer wins: The postmortem records cause and follow-up work, which is how the same failure is prevented.
- **D:** Incorrect for this question. The support tier sets the response time and the escalation path the business expects. Why the correct answer wins: The postmortem records cause and follow-up work, which is how the same failure is prevented.

### Question 79 — A

Answer: Match the support plan to the recovery commitment. The support tier sets the response time and the escalation path the business expects. Local study-map skill 6.5 (Operational Excellence and Quality Control), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 6 (solution and operations excellence): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Correct. In this case: The support tier sets the response time and the escalation path the business expects.
- **B:** Incorrect for this question. A named rotation turns an alert into a person who is already accountable for it. Why the correct answer wins: The support tier sets the response time and the escalation path the business expects.
- **C:** Incorrect for this question. The runbook records the diagnostic steps so the response does not depend on who is awake. Why the correct answer wins: The support tier sets the response time and the escalation path the business expects.
- **D:** Incorrect for this question. The contract converts an internal target into an obligation with a consequence. Why the correct answer wins: The support tier sets the response time and the escalation path the business expects.

### Question 80 — A

Answer: Detect the symptom through an alert → contain the impact and restore service → isolate the root cause from logs, traces, and metrics → apply the permanent fix and write the postmortem. Service recovery comes before deep analysis, and the postmortem follows the fix. Local study-map skill 6.5 (Operational Excellence and Quality Control), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 6 (solution and operations excellence): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Correct. In this case: Service recovery comes before deep analysis, and the postmortem follows the fix.
- **B:** Incorrect for this question. A postmortem cannot be written before the incident has happened and been resolved. Why the correct answer wins: Service recovery comes before deep analysis, and the postmortem follows the fix.
- **C:** Incorrect for this question. Detection precedes analysis, and the postmortem follows restoration rather than preceding it. Why the correct answer wins: Service recovery comes before deep analysis, and the postmortem follows the fix.
- **D:** Incorrect for this question. Service cannot be restored before the alert fires, and the root cause is isolated before the postmortem. Why the correct answer wins: Service recovery comes before deep analysis, and the postmortem follows the fix.

### Question 81 — D

Answer: Run a warm standby at reduced capacity. A running but smaller copy recovers in a short window at a continuous cost. Local study-map skill 4.4 (Disaster Recovery and Business Continuity), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 4 (analyzing and optimizing): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. Only the core data and configuration stay warm, so recovery starts the compute and takes minutes. Why the correct answer wins: A running but smaller copy recovers in a short window at a continuous cost.
- **B:** Incorrect for this question. Both regions serve traffic, so a regional loss is absorbed without a failover decision. Why the correct answer wins: A running but smaller copy recovers in a short window at a continuous cost.
- **C:** Incorrect for this question. Restoring from backup is the cheapest option and the slowest to recover. Why the correct answer wins: A running but smaller copy recovers in a short window at a continuous cost.
- **D:** Correct. In this case: A running but smaller copy recovers in a short window at a continuous cost.

### Question 82 — A

Answer: Use a dual-region bucket. A dual-region bucket keeps two replicas in a chosen pair of regions and survives one region loss. Local study-map skill 2.2 (Storage Configuration and Lifecycle), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 2 (managing and provisioning): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Correct. In this case: A dual-region bucket keeps two replicas in a chosen pair of regions and survives one region loss.
- **B:** Incorrect for this question. Standard is for data read frequently and has no retrieval fee. Why the correct answer wins: A dual-region bucket keeps two replicas in a chosen pair of regions and survives one region loss.
- **C:** Incorrect for this question. Archive is cheapest to hold and slowest and most expensive to retrieve. Why the correct answer wins: A dual-region bucket keeps two replicas in a chosen pair of regions and survives one region loss.
- **D:** Incorrect for this question. Nearline suits data read about once a month and charges for early deletion. Why the correct answer wins: A dual-region bucket keeps two replicas in a chosen pair of regions and survives one region loss.

### Question 83 — A

Answer: Replicate the data to the second region. The data must exist in the second region before any compute there can serve it. Local study-map skill 1.3 (High Availability and Failover Design), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 1 (designing and planning): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Correct. In this case: The data must exist in the second region before any compute there can serve it.
- **B:** Incorrect for this question. Only the core data and configuration stay warm, so recovery starts the compute and takes minutes. Why the correct answer wins: The data must exist in the second region before any compute there can serve it.
- **C:** Incorrect for this question. CDN caches responses at edge locations, which cuts origin load and latency for repeat reads. Why the correct answer wins: The data must exist in the second region before any compute there can serve it.
- **D:** Incorrect for this question. Restoring from backup is the cheapest option and the slowest to recover. Why the correct answer wins: The data must exist in the second region before any compute there can serve it.

### Question 84 — D

Answer: Match the support plan to the recovery commitment. The support tier sets the response time and the escalation path the business expects. Local study-map skill 6.3 (Release Management and Support), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 6 (solution and operations excellence): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. A named rotation turns an alert into a person who is already accountable for it. Why the correct answer wins: The support tier sets the response time and the escalation path the business expects.
- **B:** Incorrect for this question. The contract converts an internal target into an obligation with a consequence. Why the correct answer wins: The support tier sets the response time and the escalation path the business expects.
- **C:** Incorrect for this question. The runbook records the diagnostic steps so the response does not depend on who is awake. Why the correct answer wins: The support tier sets the response time and the escalation path the business expects.
- **D:** Correct. In this case: The support tier sets the response time and the escalation path the business expects.

### Question 85 — B

Answer: Migrate the database with Database Migration Service. The service replicates continuously and cuts over in a short window with the source still running. Local study-map skill 5.3 (Data and System Migration Tooling), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 5 (managing implementation): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. The service moves object data between buckets or clouds on a schedule. Why the correct answer wins: The service replicates continuously and cuts over in a short window with the source still running.
- **B:** Correct. In this case: The service replicates continuously and cuts over in a short window with the source still running.
- **C:** Incorrect for this question. The service runs scheduled loads from SaaS sources and other clouds into BigQuery. Why the correct answer wins: The service replicates continuously and cuts over in a short window with the source still running.
- **D:** Incorrect for this question. Datastream reads the source log and streams inserts, updates, and deletes with ordering preserved. Why the correct answer wins: The service replicates continuously and cuts over in a short window with the source still running.

### Question 86 — C

Answer: Reserve BigQuery BI Engine capacity. BI Engine holds a working set in memory so dashboards answer without scanning the table each time. Local study-map skill 1.7 (Data Processing and Analytics Selection), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 1 (designing and planning): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. Looker Studio renders the visualisation but inherits whatever query and permissions sit beneath it. Why the correct answer wins: BI Engine holds a working set in memory so dashboards answer without scanning the table each time.
- **B:** Incorrect for this question. On-demand bills per byte scanned, which is cheap for sparse use and unpredictable at scale. Why the correct answer wins: BI Engine holds a working set in memory so dashboards answer without scanning the table each time.
- **C:** Correct. In this case: BI Engine holds a working set in memory so dashboards answer without scanning the table each time.
- **D:** Incorrect for this question. InsertAll is best-effort and only deduplicates on a provided insert ID, so duplicates can land. Why the correct answer wins: BI Engine holds a working set in memory so dashboards answer without scanning the table each time.

### Question 87 — D

Answer: Partition the table on the date column. Partitioning limits each query to the date ranges it names, so it scans less. Local study-map skill 2.2 (Storage Configuration and Lifecycle), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 2 (managing and provisioning): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. On-demand bills per byte scanned, which is cheap for sparse use and unpredictable at scale. Why the correct answer wins: Partitioning limits each query to the date ranges it names, so it scans less.
- **B:** Incorrect for this question. The view stores the aggregate result and refreshes incrementally as base data arrives. Why the correct answer wins: Partitioning limits each query to the date ranges it names, so it scans less.
- **C:** Incorrect for this question. Clustering sorts within partitions so a filtered query reads fewer blocks. Why the correct answer wins: Partitioning limits each query to the date ranges it names, so it scans less.
- **D:** Correct. In this case: Partitioning limits each query to the date ranges it names, so it scans less.

### Question 88 — A

Answer: Export billing to BigQuery and review it per label. The export attributes spend to the labels and projects that caused it. The export attributes cost to the team and service that caused it. Local study-map skill 4.5 (Cost Optimization), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 4 (analyzing and optimizing): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Correct. The export attributes cost to the team and service that caused it. In this case: The export attributes spend to the labels and projects that caused it.
- **B:** Incorrect for this question. Labels attribute spend in billing export; they do not grant or restrict access. Why the correct answer wins: The export attributes spend to the labels and projects that caused it.
- **C:** Incorrect for this question. A budget alerts on spend but does not stop it. Why the correct answer wins: The export attributes spend to the labels and projects that caused it.
- **D:** Incorrect for this question. Showing owners their own spend changes behaviour more reliably than a central report. Why the correct answer wins: The export attributes spend to the labels and projects that caused it.

### Question 89 — A

Answer: Define an SLO with an error budget. An SLO ties the alert to the user promise rather than to a raw resource threshold. Local study-map skill 6.2 (Alerting and Service Level Objectives), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 6 (solution and operations excellence): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Correct. In this case: An SLO ties the alert to the user promise rather than to a raw resource threshold.
- **B:** Incorrect for this question. The dashboard gives the team one view of the same signals during an incident. Why the correct answer wins: An SLO ties the alert to the user promise rather than to a raw resource threshold.
- **C:** Incorrect for this question. The check measures availability from outside, which no internal metric can prove. Why the correct answer wins: An SLO ties the alert to the user promise rather than to a raw resource threshold.
- **D:** Incorrect for this question. The policy fires when the series crosses the condition for the stated duration. Why the correct answer wins: An SLO ties the alert to the user promise rather than to a raw resource threshold.

### Question 90 — C

Answer: Add row-level access policies to the table. Row-level policies filter which rows each principal sees inside BigQuery itself. Local study-map skill 3.4 (VPC Service Controls and Network Security), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 3 (security and compliance): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. The view runs with its own identity, so a consumer reads columns without table access. Why the correct answer wins: Row-level policies filter which rows each principal sees inside BigQuery itself.
- **B:** Incorrect for this question. The policy replaces the column value for unauthorised principals while leaving the column queryable. Why the correct answer wins: Row-level policies filter which rows each principal sees inside BigQuery itself.
- **C:** Correct. In this case: Row-level policies filter which rows each principal sees inside BigQuery itself.
- **D:** Incorrect for this question. Looker Studio renders the visualisation but inherits whatever query and permissions sit beneath it. Why the correct answer wins: Row-level policies filter which rows each principal sees inside BigQuery itself.

### Question 91 — B

Answer: Publish a service catalog entry with an approved template. A catalog entry gives teams a pre-approved, policy-compliant way to request the resource. Local study-map skill 4.7 (Service Catalog and Provisioning), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 4 (analyzing and optimizing): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. Terraform holds desired state in code, plans the diff, and applies it through a provider. Why the correct answer wins: A catalog entry gives teams a pre-approved, policy-compliant way to request the resource.
- **B:** Correct. In this case: A catalog entry gives teams a pre-approved, policy-compliant way to request the resource.
- **C:** Incorrect for this question. Labels attribute spend in billing export; they do not grant or restrict access. Why the correct answer wins: A catalog entry gives teams a pre-approved, policy-compliant way to request the resource.
- **D:** Incorrect for this question. An organization policy blocks the action across every project regardless of who holds the role. Why the correct answer wins: A catalog entry gives teams a pre-approved, policy-compliant way to request the resource.

### Question 92 — B

Answer: Enforce the control with an organization policy constraint. An organization policy blocks the action across every project regardless of who holds the role. Local study-map skill 3.2 (Resource Hierarchy and Organization Policy), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 3 (security and compliance): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. A project is the boundary for quota, billing, and most IAM inheritance. Why the correct answer wins: An organization policy blocks the action across every project regardless of who holds the role.
- **B:** Correct. In this case: An organization policy blocks the action across every project regardless of who holds the role.
- **C:** Incorrect for this question. Labels attribute spend in billing export; they do not grant or restrict access. Why the correct answer wins: An organization policy blocks the action across every project regardless of who holds the role.
- **D:** Incorrect for this question. A folder binding inherits to every project beneath it, so new projects start with the right access. Why the correct answer wins: An organization policy blocks the action across every project regardless of who holds the role.

### Question 93 — C

Answer: Define the baseline and target as a KPI with an owner. A measured baseline and a named owner make the outcome testable after the programme. Local study-map skill 1.1 (Business Requirements and Success Metrics), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 1 (designing and planning): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. The export attributes cost to the team and service that caused it. Why the correct answer wins: A measured baseline and a named owner make the outcome testable after the programme.
- **B:** Incorrect for this question. The model compares run cost, people cost, and exit cost rather than the monthly bill alone. Why the correct answer wins: A measured baseline and a named owner make the outcome testable after the programme.
- **C:** Correct. In this case: A measured baseline and a named owner make the outcome testable after the programme.
- **D:** Incorrect for this question. The dashboard gives the team one view of the same signals during an incident. Why the correct answer wins: A measured baseline and a named owner make the outcome testable after the programme.

### Question 94 — D

Answer: Write a blameless postmortem with actions. The postmortem records cause and follow-up work, which is how the same failure is prevented. Local study-map skill 6.5 (Operational Excellence and Quality Control), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 6 (solution and operations excellence): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. The runbook records the diagnostic steps so the response does not depend on who is awake. Why the correct answer wins: The postmortem records cause and follow-up work, which is how the same failure is prevented.
- **B:** Incorrect for this question. The support tier sets the response time and the escalation path the business expects. Why the correct answer wins: The postmortem records cause and follow-up work, which is how the same failure is prevented.
- **C:** Incorrect for this question. The dashboard gives the team one view of the same signals during an incident. Why the correct answer wins: The postmortem records cause and follow-up work, which is how the same failure is prevented.
- **D:** Correct. In this case: The postmortem records cause and follow-up work, which is how the same failure is prevented.

### Question 95 — C

Answer: Assess the estate in Migration Center. Migration Center inventories the estate and estimates target size and cost before a plan is funded. Migration Center inventories the servers and estimates the target size and cost. Local study-map skill 1.9 (Migration Planning and Future Improvement), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 1 (designing and planning): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. The tool rewrites a VM workload into a container image so it can run on GKE. Why the correct answer wins: Migration Center inventories the estate and estimates target size and cost before a plan is funded.
- **B:** Incorrect for this question. The service moves object data between buckets or clouds on a schedule. Why the correct answer wins: Migration Center inventories the estate and estimates target size and cost before a plan is funded.
- **C:** Correct. Migration Center inventories the servers and estimates the target size and cost. In this case: Migration Center inventories the estate and estimates target size and cost before a plan is funded.
- **D:** Incorrect for this question. The service moves a database with continuous replication and a short cutover window. Why the correct answer wins: Migration Center inventories the estate and estimates target size and cost before a plan is funded.

### Question 96 — C

Answer: Serve features from Agent Platform Feature Store. Feature Store keeps one definition for training and serving, which prevents training-serving skew. Local study-map skill 2.7 (Agent Platform ML Workflows), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 2 (managing and provisioning): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. Pipelines runs each step as a container with lineage and caching, so the run is reproducible. Why the correct answer wins: Feature Store keeps one definition for training and serving, which prevents training-serving skew.
- **B:** Incorrect for this question. An endpoint keeps capacity ready for low-latency per-request predictions. Why the correct answer wins: Feature Store keeps one definition for training and serving, which prevents training-serving skew.
- **C:** Correct. In this case: Feature Store keeps one definition for training and serving, which prevents training-serving skew.
- **D:** Incorrect for this question. Monitoring compares live traffic against the training baseline and reports skew and drift. Why the correct answer wins: Feature Store keeps one definition for training and serving, which prevents training-serving skew.

### Question 97 — A, B

Answers: Screen prompts and responses with Model Armor; De-identify the data with Sensitive Data Protection. Sensitive Data Protection removes the sensitive fields, and Model Armor screens the prompts and responses. Model Armor detects prompt injection, jailbreak attempts, and unsafe content before and after the model call. Sensitive Data Protection finds and redacts, tokenizes, or format-preservingly encrypts sensitive fields. Local study-map skill 3.7 (Securing AI Workloads), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 3 (security and compliance): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Correct. Model Armor detects prompt injection, jailbreak attempts, and unsafe content before and after the model call. In this case: Sensitive Data Protection removes the sensitive fields, and Model Armor screens the prompts and responses.
- **B:** Correct. Sensitive Data Protection finds and redacts, tokenizes, or format-preservingly encrypts sensitive fields. In this case: Sensitive Data Protection removes the sensitive fields, and Model Armor screens the prompts and responses.
- **C:** Incorrect for this question. Security Command Center aggregates misconfiguration and threat findings across the organization. Why the correct answer wins: Sensitive Data Protection removes the sensitive fields, and Model Armor screens the prompts and responses.
- **D:** Incorrect for this question. A deny policy overrides every allow beneath it, which is how an exception is made impossible. Why the correct answer wins: Sensitive Data Protection removes the sensitive fields, and Model Armor screens the prompts and responses.
- **E:** Incorrect for this question. The access level adds device and network conditions to the perimeter rule. Why the correct answer wins: Sensitive Data Protection removes the sensitive fields, and Model Armor screens the prompts and responses.

### Question 98 — B

Answer: Enable model monitoring on the endpoint. Monitoring compares live traffic against the training baseline and reports skew and drift. Local study-map skill 1.8 (AI and ML Solution Design), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 1 (designing and planning): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. Feature Store keeps one definition for training and serving, which prevents training-serving skew. Why the correct answer wins: Monitoring compares live traffic against the training baseline and reports skew and drift.
- **B:** Correct. In this case: Monitoring compares live traffic against the training baseline and reports skew and drift.
- **C:** Incorrect for this question. Batch prediction reads a file and writes predictions without holding serving capacity. Why the correct answer wins: Monitoring compares live traffic against the training baseline and reports skew and drift.
- **D:** Incorrect for this question. An endpoint keeps capacity ready for low-latency per-request predictions. Why the correct answer wins: Monitoring compares live traffic against the training baseline and reports skew and drift.

### Question 99 — A

Answer: Inspect the trace waterfall in Cloud Trace. Trace shows how one request spent its time across services and calls. Local study-map skill 4.2 (Root Cause Analysis), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 4 (analyzing and optimizing): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Correct. In this case: Trace shows how one request spent its time across services and calls.
- **B:** Incorrect for this question. The dashboard gives the team one view of the same signals during an incident. Why the correct answer wins: Trace shows how one request spent its time across services and calls.
- **C:** Incorrect for this question. Recommender reports idle and over-provisioned resources with the estimated saving. Why the correct answer wins: Trace shows how one request spent its time across services and calls.
- **D:** Incorrect for this question. Logging holds the event text and structured fields that explain what happened at a moment. Why the correct answer wins: Trace shows how one request spent its time across services and calls.

### Question 100 — A

Answer: Define dashboards and metrics in Cloud Monitoring. Monitoring collects the platform and application metrics that the first alert will use. Local study-map skill 6.1 (Observability Design), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 6 (solution and operations excellence): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Correct. In this case: Monitoring collects the platform and application metrics that the first alert will use.
- **B:** Incorrect for this question. Recommender reports idle and over-provisioned resources with the estimated saving. Why the correct answer wins: Monitoring collects the platform and application metrics that the first alert will use.
- **C:** Incorrect for this question. The dashboard gives the team one view of the same signals during an incident. Why the correct answer wins: Monitoring collects the platform and application metrics that the first alert will use.
- **D:** Incorrect for this question. Trace shows how one request spent its time across services and calls. Why the correct answer wins: Monitoring collects the platform and application metrics that the first alert will use.
