# Google Cloud Professional Cloud Architect — Full-Length Mock Exam 2

Professional Cloud Architect · 100 questions · expanded practice bank · passing score not published

Blueprint-weighted mock exam. Item mix: 84 multiple-choice (selection count stated where needed), 16 multi-select, and 4 case studies of 5 questions. 8 of the multiple-choice items ask you to choose the correct candidate sequence. The live exam publishes 50-60 questions and two case studies worth 20-30 per cent of the score; this set is larger on purpose and cannot reproduce the split-screen case-study panel, drag-and-drop ordering, or lab tasks. See the README for the exact fidelity boundary.

Original educational content, not actual, recalled, or copied Google exam items.

## Questions

### 1. A platform programme will run for eighteen months and the sponsor wants an exit test. What should be agreed now?

Domain: Designing and planning a cloud solution architecture

- A. Define the baseline and target as a KPI with an owner
- B. Build a three-year total cost of ownership model
- C. Export billing to BigQuery and review it per label
- D. Publish a shared dashboard

### 2. A framework agreement requires that the workload can move to another provider. What must the design include?

Domain: Designing and planning a cloud solution architecture

- A. Document the exit plan and data portability
- B. Set a budget with alert thresholds
- C. Tag the resources with labels for cost reporting
- D. Build a three-year total cost of ownership model

### 3. Two subsidiaries argue about acceptable downtime for the shared platform. Which two artefacts settle it? Select two.

Domain: Designing and planning a cloud solution architecture

- A. Put the recovery commitment in the contract
- B. Tag the resources with labels for cost reporting
- C. Publish a shared dashboard
- D. Set the RPO and RTO with the business owner
- E. Act on the Recommender suggestions

### 4. A shared platform must keep scheduling pods when one zone is unavailable. What should be created?

Domain: Designing and planning a cloud solution architecture

- A. Use a managed instance group with autoscaling
- B. Create a regional GKE cluster
- C. Deploy the service on Cloud Run
- D. Create a zonal GKE cluster

### 5. A provisioning database has a five-minute recovery objective and a standby in another region. Which two pieces are required? Select two.

Domain: Designing and planning a cloud solution architecture

- A. Replicate the data to the second region
- B. Enable Cloud SQL high availability with a standby
- C. Use Memorystore
- D. Enable Cloud CDN on the backend
- E. Create a materialized view for the repeated aggregate

### 6. Thirty subsidiary networks must reach a shared services network through one routing domain. What should be built?

Domain: Designing and planning a cloud solution architecture

- A. Peer the two VPC networks
- B. Build a Network Connectivity Center hub
- C. Deploy Cloud NAT for outbound traffic
- D. Create a DNS peering zone

### 7. A subsidiary must call a shared service privately without leaving the organisation's network. Which two designs allow that? Select two.

Domain: Designing and planning a cloud solution architecture

- A. Deploy Cloud NAT for outbound traffic
- B. Publish the service through Private Service Connect
- C. Enable Cloud CDN on the backend
- D. Peer the two VPC networks
- E. Issue a short-lived signed URL

### 8. A subsidiary needs a predictable 10 Gbps private path from its own data centre. What should be ordered?

Domain: Designing and planning a cloud solution architecture

- A. Order Partner Interconnect
- B. Use HA VPN with two tunnels
- C. Deploy Cloud NAT for outbound traffic
- D. Order a Dedicated Interconnect

### 9. A session store needs millions of key reads per second with millisecond latency. What should be used?

Domain: Designing and planning a cloud solution architecture

- A. Use Bigtable
- B. Load the data into BigQuery
- C. Use Firestore
- D. Use Cloud SQL

### 10. Object access patterns are unpredictable, and anything untouched for two years must be deleted. Which two settings apply? Select two.

Domain: Designing and planning a cloud solution architecture

- A. Mount a Filestore instance for the shared file path
- B. Use local SSD for the scratch space
- C. Store the objects in Nearline storage class
- D. Add a lifecycle rule that transitions and then deletes
- E. Enable Autoclass on the bucket

### 11. An internal tool is used for two hours a day and must cost nothing at night. What should be used?

Domain: Designing and planning a cloud solution architecture

- A. Run the legacy stack on Google Cloud VMware Engine
- B. Use a managed instance group with autoscaling
- C. Deploy the service on Cloud Run
- D. Use GKE Standard with a node pool per workload shape

### 12. A team wants the Kubernetes API but has no capacity to manage nodes. What should be chosen?

Domain: Designing and planning a cloud solution architecture

- A. Use GKE Standard with a node pool per workload shape
- B. Submit the work as a Batch job
- C. Deploy the service on Cloud Run
- D. Use GKE Autopilot

### 13. A nightly simulation needs 4,000 cores for ninety minutes and nothing afterwards. What should be used?

Domain: Designing and planning a cloud solution architecture

- A. Use GKE Standard with a node pool per workload shape
- B. Use a managed instance group with autoscaling
- C. Submit the work as a Batch job
- D. Deploy the service on Cloud Run

### 14. A Spark job runs twice a week and nobody wants to size a cluster. What should be used?

Domain: Designing and planning a cloud solution architecture

- A. Use a Dataproc cluster
- B. Use Managed Service for Apache Airflow
- C. Use Dataproc Serverless
- D. Use Dataflow

### 15. One pipeline must run the same transformations in batch tonight and in streaming next quarter. What should be used?

Domain: Designing and planning a cloud solution architecture

- A. Use the BigQuery Data Transfer Service
- B. Use a Dataproc cluster
- C. Use Dataflow
- D. Trigger the job with Cloud Scheduler

### 16. A regulated client requires regional processing and audit logging for every model call. What should be used?

Domain: Designing and planning a cloud solution architecture

- A. Call Gemini through Agent Platform
- B. Use the Vision API for the images
- C. Index the corpus with Vertex AI Search
- D. Use Gemini Enterprise for the knowledge assistant

### 17. Training and serving must use one feature definition, and drift must be visible in production. Which two components apply? Select two.

Domain: Designing and planning a cloud solution architecture

- A. Select the model from Model Garden
- B. Build the agent with the Agent Development Kit
- C. Use Gemini Cloud Assist for the investigation
- D. Enable model monitoring on the endpoint
- E. Serve features from Agent Platform Feature Store

### 18. The estate must be inventoried and sized before an eighteen-month programme is approved. What should be used?

Domain: Designing and planning a cloud solution architecture

- A. Copy the files with Storage Transfer Service
- B. Assess the estate in Migration Center
- C. Use Database Migration Service
- D. Convert the VMs with Migrate to Containers

### 19. A subsidiary must meet a recovery objective that its board will audit. Which sequence is correct?

Domain: Designing and planning a cloud solution architecture

- A. Choose the DR pattern → fail over in a game day → set the RTO and RPO targets → build the standby environment
- B. Fail over in a game day → set the RTO and RPO targets → choose the DR pattern → build the standby environment
- C. Set the RTO and RPO targets → choose the DR pattern that meets them → build and replicate the standby environment → fail over in a game day and record the result
- D. Build and replicate the standby environment → choose the DR pattern → set the RTO and RPO targets → fail over in a game day

### 20. A site has one internet provider and still needs a resilient private path. What should be used?

Domain: Managing and provisioning a solution infrastructure

- A. Deploy Cloud NAT for outbound traffic
- B. Allocate private services access for the peered services
- C. Use HA VPN with two tunnels
- D. Enable Cloud CDN on the backend

### 21. A dedicated circuit is ordered and the on-premises router must exchange routes with Google Cloud. What should be added?

Domain: Managing and provisioning a solution infrastructure

- A. Build a Network Connectivity Center hub
- B. Add a VLAN attachment with a Cloud Router
- C. Order a Dedicated Interconnect
- D. Use HA VPN with two tunnels

### 22. Private instances must reach the internet for updates and reach Google APIs without a proxy. Which two settings apply? Select two.

Domain: Managing and provisioning a solution infrastructure

- A. Enable Private Google Access on the subnet
- B. Attach a Cloud Armor security policy
- C. Put Identity-Aware Proxy in front of the application
- D. Deploy Cloud NAT for outbound traffic
- E. Enable Cloud CDN on the backend

### 23. Statements must be immutable for seven years to satisfy the regulator. What should be applied?

Domain: Managing and provisioning a solution infrastructure

- A. Enable object versioning
- B. Apply a bucket retention policy with a locked period
- C. Add a lifecycle rule that transitions and then deletes
- D. Enable Autoclass on the bucket

### 24. A nightly copy from an S3 bucket must be filtered and repeated. What should be used?

Domain: Managing and provisioning a solution infrastructure

- A. Use a Transfer Appliance for the one-off bulk move
- B. Copy the files with Storage Transfer Service
- C. Use Storage Transfer Service for the recurring copy
- D. Issue a short-lived signed URL

### 25. A fact table is always filtered by date and by customer, and queries scan too much. Which two physical design choices apply? Select two.

Domain: Managing and provisioning a solution infrastructure

- A. Partition the table on the date column
- B. Cluster the table on the filter columns
- C. Create a materialized view for the repeated aggregate
- D. Build the dashboard in Looker Studio
- E. Leave the project on on-demand pricing

### 26. Plant servers must receive operating system patches on a published schedule. What should be used?

Domain: Managing and provisioning a solution infrastructure

- A. Manage the resources with Config Connector
- B. Run the build in Cloud Build
- C. Run the batch tier on Spot VMs
- D. Use VM Manager for OS patch compliance

### 27. A rendering tier runs constantly at a low level and bursts for two days a month. Which two purchasing choices apply? Select two.

Domain: Managing and provisioning a solution infrastructure

- A. Move the steady services to E2 machine types
- B. Run the batch tier on Spot VMs
- C. Use local SSD for the scratch space
- D. Buy committed use discounts for the steady baseline
- E. Share the cost view with the engineering teams

### 28. A workload needs 96 GB of memory but only four vCPUs. What should be used?

Domain: Managing and provisioning a solution infrastructure

- A. Run the batch tier on Spot VMs
- B. Use a custom machine type sized to the workload
- C. Use local SSD for the scratch space
- D. Use sole-tenant nodes

### 29. Teams submit pods with wildly different resource requests and nodes are always the wrong size. What should be enabled?

Domain: Managing and provisioning a solution infrastructure

- A. Register the clusters in a fleet
- B. Pin a release channel and a maintenance window
- C. Enable network policy enforcement
- D. Enable node auto-provisioning

### 30. A regulated cluster may not give any node an external address. What should be configured?

Domain: Managing and provisioning a solution infrastructure

- A. Create private nodes with no external IP addresses
- B. Use sole-tenant nodes
- C. Deploy Cloud NAT for outbound traffic
- D. Create a zonal GKE cluster

### 31. A new regulated cluster must be built with private nodes and attested images. Which sequence is correct?

Domain: Managing and provisioning a solution infrastructure

- A. Build a Shared VPC → deploy through Binary Authorization → create the project → create the cluster
- B. Deploy through Binary Authorization → create the cluster → build the Shared VPC → create the project
- C. Create the project and enable APIs → build a Shared VPC with private subnets → create a regional private cluster with Workload Identity Federation for GKE → deploy through Binary Authorization
- D. Create a regional private cluster → build a Shared VPC with private subnets → enable APIs → deploy through Binary Authorization

### 32. Each Cloud Run instance handles one request at a time and the bill is far too high. What should be changed?

Domain: Managing and provisioning a solution infrastructure

- A. Raise the request concurrency setting
- B. Set a minimum instance count on the Cloud Run service
- C. Deploy on App Engine flexible environment
- D. Deploy the workload on Cloud Run with a GPU

### 33. A single small handler must react to a bucket event. What should be used?

Domain: Managing and provisioning a solution infrastructure

- A. Use a managed instance group with autoscaling
- B. Submit the work as a Batch job
- C. Use Cloud Run functions
- D. Deploy the service on Cloud Run

### 34. A subsidiary is adopting Terraform under a reviewed change process. Which sequence is correct?

Domain: Managing and provisioning a solution infrastructure

- A. Run a plan in CI → apply through the pipeline → define modules → create the remote state bucket
- B. Create a remote state bucket with versioning → define modules per environment → run a plan in CI and require review → apply through the pipeline with a scoped service account
- C. Define modules → apply through the pipeline → run a plan in CI → create the remote state bucket
- D. Apply through the pipeline → create the remote state bucket → define modules → run a plan in CI

### 35. A team needs the standard permissions for one job and no more. What should be granted?

Domain: Designing for security and compliance

- A. Grant a predefined role at the narrowest resource
- B. Run a bastion host with a public address
- C. Define a custom role with only the required permissions
- D. Authenticate the call with an API key

### 36. A leaked credential must affect one workload rather than the whole platform. What should be done?

Domain: Designing for security and compliance

- A. Create a separate project per environment
- B. Create a service account key file for the pipeline
- C. Give each service its own service account
- D. Tag the resources with labels for cost reporting

### 37. Support access must be time-limited, and one departing contractor must lose access immediately. Which two controls apply? Select two.

Domain: Designing for security and compliance

- A. Tag the resources with labels for cost reporting
- B. Grant a predefined role at the narrowest resource
- C. Apply an IAM deny policy
- D. Add an IAM condition on the binding
- E. Run a bastion host with a public address

### 38. A new subsidiary project must inherit the right access without a ticket. Where should the roles be bound?

Domain: Designing for security and compliance

- A. Grant a predefined role at the narrowest resource
- B. Create a folder per environment and bind roles there
- C. Tag the resources with labels for cost reporting
- D. Create a separate project per environment

### 39. Residency must hold for every future project, and each environment needs its own quota boundary. Which two constructs provide that? Select two.

Domain: Designing for security and compliance

- A. Create a separate project per environment
- B. Tag the resources with labels for cost reporting
- C. Enforce the control with an organization policy constraint
- D. Create a folder per environment and bind roles there
- E. Add an IAM condition on the binding

### 40. A regulator requires that key material never leaves the country. What should be configured?

Domain: Designing for security and compliance

- A. Supply a customer-supplied encryption key
- B. Use Cloud HSM for the key
- C. Store the credential in Secret Manager
- D. Create the key ring in the same region as the data

### 41. The bank must control its own keys and change them on a published schedule. Which two settings apply? Select two.

Domain: Designing for security and compliance

- A. Supply a customer-supplied encryption key
- B. Encrypt with a customer-managed key in Cloud KMS
- C. Use Cloud HSM for the key
- D. Set an automatic rotation period on the key
- E. Put the credential in an environment variable on the instance

### 42. Data must not move to a project outside the approved set, even for an owner. What should be applied?

Domain: Designing for security and compliance

- A. Apply an IAM deny policy
- B. Tag the resources with labels for cost reporting
- C. Apply a hierarchical firewall policy at the organization or folder
- D. Put the projects inside a VPC Service Controls perimeter

### 43. A managed database must take an internal address inside the subsidiary network. What should be allocated?

Domain: Designing for security and compliance

- A. Deploy Cloud NAT for outbound traffic
- B. Publish the service through Private Service Connect
- C. Enable Private Google Access on the subnet
- D. Allocate private services access for the peered services

### 44. A pipeline in another cloud must call the API without any key leaving that cloud. What should be used?

Domain: Designing for security and compliance

- A. Authenticate the call with an API key
- B. Use Workload Identity Federation for the external pipeline
- C. Put the credential in an environment variable on the instance
- D. Create a service account key file for the pipeline

### 45. Contractors must reach an internal tool with no VPN and no public address. What should be used?

Domain: Designing for security and compliance

- A. Run a bastion host with a public address
- B. Put Identity-Aware Proxy in front of the application
- C. Deploy Cloud NAT for outbound traffic
- D. Enable Private Google Access on the subnet

### 46. Built images must be stored where IAM and vulnerability metadata apply. Where should they go?

Domain: Designing for security and compliance

- A. Use Cloud Shell for the one-off task
- B. Enable Artifact Analysis scanning on the repository
- C. Store the objects in Standard storage class
- D. Store the images in Artifact Registry

### 47. Support tickets contain identifiers that must be removed before analytics ingest. What should be used?

Domain: Designing for security and compliance

- A. Require an access level in the perimeter
- B. Turn on Security Command Center findings
- C. De-identify the data with Sensitive Data Protection
- D. Screen prompts and responses with Model Armor

### 48. A perimeter will be enforced across forty subsidiary projects. Which sequence is correct?

Domain: Designing for security and compliance

- A. Enforce the perimeter → create the service perimeter in dry-run mode → inventory projects → enable audit logs
- B. Enable audit logs → enforce the perimeter → inventory projects → review violations
- C. Create the service perimeter in dry-run mode → enforce the perimeter → enable audit logs → inventory projects
- D. Inventory projects and data flows → enable the audit logs needed for the perimeter → create the service perimeter in dry-run mode → review violations and enforce the perimeter

### 49. Subsidiary teams keep branches open for weeks and merge painfully. What should change?

Domain: Analyzing and optimizing technical and business processes

- A. Adopt trunk-based development with short-lived branches
- B. Roll the change out instance by instance
- C. Put the change behind a feature flag
- D. Rebuild the artifact separately for each environment

### 50. The platform team needs reviewed changes and the same tested build in every environment. Which two practices apply? Select two.

Domain: Analyzing and optimizing technical and business processes

- A. Promote the same tested artifact between environments
- B. Roll the change out instance by instance
- C. Rebuild the artifact separately for each environment
- D. Require a reviewed pull request and a passing plan
- E. Set a budget with alert thresholds

### 51. One checkout request spends 900 ms across four services and nobody knows where. What should be inspected?

Domain: Analyzing and optimizing technical and business processes

- A. Add an uptime check from several regions
- B. Publish a shared dashboard
- C. Act on the Recommender suggestions
- D. Inspect the trace waterfall in Cloud Trace

### 52. A deployment failed silently and the team must find both the exception and its frequency. Which two tools apply? Select two.

Domain: Analyzing and optimizing technical and business processes

- A. Query the entries in Cloud Logging
- B. Group the exceptions in Error Reporting
- C. Define an SLO with an error budget
- D. Publish a runbook per alert
- E. Publish a shared dashboard

### 53. A subsidiary platform is down and the response must follow the agreed order. Which sequence is correct?

Domain: Analyzing and optimizing technical and business processes

- A. Detect the symptom through an alert → contain the impact and restore service → isolate the root cause from logs, traces, and metrics → apply the permanent fix and write the postmortem
- B. Isolate the root cause → detect the symptom → write the postmortem → restore service
- C. Write the postmortem → detect the symptom → isolate the root cause → restore service
- D. Restore service → detect the symptom → write the postmortem → isolate the root cause

### 54. A service has hundreds of end-to-end tests that take four hours. What should change?

Domain: Analyzing and optimizing technical and business processes

- A. Cover the change with unit, integration, and a few end-to-end tests
- B. Run a load test at the expected peak
- C. Run a chaos experiment against a zone
- D. Commission a penetration test

### 55. Integration tests must run locally without touching a billable project. What should be used?

Domain: Analyzing and optimizing technical and business processes

- A. Use Cloud Shell for the one-off task
- B. Automate the step with the gcloud CLI
- C. Use the bq command-line tool
- D. Run the emulator in the pipeline

### 56. A subsidiary is paying for resources that nobody uses. What should be reviewed first?

Domain: Analyzing and optimizing technical and business processes

- A. Act on the Recommender suggestions
- B. Set a budget with alert thresholds
- C. Export billing to BigQuery and review it per label
- D. Tag the resources with labels for cost reporting

### 57. Finance needs cost per subsidiary and per environment, not one group bill. What should be configured?

Domain: Analyzing and optimizing technical and business processes

- A. Export billing to BigQuery and review it per label
- B. Set a budget with alert thresholds
- C. Tag the resources with labels for cost reporting
- D. Share the cost view with the engineering teams

### 58. A subsidiary warehouse bill must fall without breaking dashboards. Which sequence is correct?

Domain: Analyzing and optimizing technical and business processes

- A. Partition and cluster the table → measure slot time → inspect the plan → rewrite the query
- B. Rewrite the query → partition the table → measure slot time → inspect the plan
- C. Measure slot time → rewrite the query → inspect the plan → partition the table
- D. Inspect the query plan and bytes processed → partition and cluster the table on the filter columns → rewrite the query to prune partitions → measure the new slot time and bytes scanned

### 59. A change affects a regulated subsidiary and must be reviewed for risk and timing. What should it go through?

Domain: Analyzing and optimizing technical and business processes

- A. Publish a service catalog entry with an approved template
- B. Define an on-call rotation with an escalation path
- C. Route the change through a change advisory board
- D. Publish a runbook per alert

### 60. Subsidiary teams need a compliant environment without waiting for the platform team. What should be published?

Domain: Analyzing and optimizing technical and business processes

- A. Manage the resources with Terraform
- B. Publish a service catalog entry with an approved template
- C. Tag the resources with labels for cost reporting
- D. Enforce the control with an organization policy constraint

### 61. A new release must be proven on live traffic before the whole estate gets it. What should be used?

Domain: Managing implementation

- A. Put the change behind a feature flag
- B. Deploy blue/green with a traffic switch
- C. Roll out a canary to a small share of traffic
- D. Roll the change out instance by instance

### 62. A feature must ship dark and be switched off instantly without a deployment. What should be used?

Domain: Managing implementation

- A. Put the change behind a feature flag
- B. Deploy blue/green with a traffic switch
- C. Roll out a canary to a small share of traffic
- D. Roll the change out instance by instance

### 63. Two identical environments must allow an instant reversal, and the previous build must be exactly restorable. Which two practices apply? Select two.

Domain: Managing implementation

- A. Set a budget with alert thresholds
- B. Promote the same tested artifact between environments
- C. Rebuild the artifact separately for each environment
- D. Keep the previous image digest ready for rollback
- E. Deploy blue/green with a traffic switch

### 64. Subsidiaries need per-consumer quotas, keys, and mediation. What should be used?

Domain: Managing implementation

- A. Use Cloud Endpoints
- B. Attach a Cloud Armor security policy
- C. Use API Gateway
- D. Publish the API through Apigee

### 65. A single internal API on Cloud Run needs a managed OpenAPI front door. What should be used?

Domain: Managing implementation

- A. Use API Gateway
- B. Use Cloud Endpoints
- C. Attach a Cloud Armor security policy
- D. Publish the API through Apigee

### 66. A 12 TB Oracle database must move with less than four hours of downtime. What should be used?

Domain: Managing implementation

- A. Migrate the database with Database Migration Service
- B. Copy the files with Storage Transfer Service
- C. Use Datastream for change data capture
- D. Use the BigQuery Data Transfer Service

### 67. A legacy application must run on GKE but its installation cannot be rebuilt this year. What should be used?

Domain: Managing implementation

- A. Copy the files with Storage Transfer Service
- B. Assess the estate in Migration Center
- C. Convert the VMs with Migrate to Containers
- D. Run the legacy stack on Google Cloud VMware Engine

### 68. A subsidiary migration must be sequenced so dependencies move together. Which sequence is correct?

Domain: Managing implementation

- A. Inventory the estate in Migration Center → group servers into dependency-based waves → validate a pilot wave in the target landing zone → cut over wave by wave and decommission the source
- B. Cut over and decommission → validate a pilot wave → inventory the estate → group servers into waves
- C. Validate a pilot wave → inventory the estate → group servers into waves → cut over and decommission
- D. Group servers into waves → inventory the estate → cut over and decommission → validate a pilot wave

### 69. Every subsidiary environment must be reproducible from code with a reviewable diff. What should be used?

Domain: Managing implementation

- A. Automate the step with the gcloud CLI
- B. Manage the resources with Terraform
- C. Manage the resources with Config Connector
- D. Use Deployment Manager templates

### 70. The plan and the apply must run the same way for every subsidiary. Where should they run?

Domain: Managing implementation

- A. Use Cloud Code in the IDE
- B. Automate the step with the gcloud CLI
- C. Use Cloud Shell for the one-off task
- D. Run the build in Cloud Build

### 71. A service must handle quota errors with the recommended backoff. What should it use?

Domain: Managing implementation

- A. Automate the step with the gcloud CLI
- B. Authenticate the call with an API key
- C. Impersonate a service account for a curl test
- D. Use the Google API client library with retries

### 72. Host metrics and application logs must reach Google Cloud from plant servers. What should be installed?

Domain: Ensuring solution and operations excellence

- A. Group the exceptions in Error Reporting
- B. Install the Ops Agent on the instances
- C. Inspect the trace waterfall in Cloud Trace
- D. Attach Cloud Profiler to the service

### 73. A subsidiary needs external availability evidence and a per-service breakdown of one slow call. Which two tools apply? Select two.

Domain: Ensuring solution and operations excellence

- A. Publish a shared dashboard
- B. Act on the Recommender suggestions
- C. Define an SLO with an error budget
- D. Inspect the trace waterfall in Cloud Trace
- E. Add an uptime check from several regions

### 74. A subsidiary wants its alert expressed as user-visible success rather than processor load. What should be defined?

Domain: Ensuring solution and operations excellence

- A. Create an alerting policy on the metric
- B. Publish a shared dashboard
- C. Define an SLO with an error budget
- D. Add an uptime check from several regions

### 75. A specific error string must be counted and alerted on. What should be created first?

Domain: Ensuring solution and operations excellence

- A. Create an alerting policy on the metric
- B. Define an SLO with an error budget
- C. Create a log-based metric
- D. Publish a shared dashboard

### 76. A subsidiary engineer spent four hours guessing which commands to run during an outage. What should be published?

Domain: Ensuring solution and operations excellence

- A. Match the support plan to the recovery commitment
- B. Publish a shared dashboard
- C. Publish a runbook per alert
- D. Define an on-call rotation with an escalation path

### 77. An alert has no named person who answers it at 03:00. What should be established?

Domain: Ensuring solution and operations excellence

- A. Publish a runbook per alert
- B. Define an on-call rotation with an escalation path
- C. Put the recovery commitment in the contract
- D. Match the support plan to the recovery commitment

### 78. A subsidiary inherited a claim that a zone loss is survivable, but no one has verified it. What should be run?

Domain: Ensuring solution and operations excellence

- A. Roll out a canary to a small share of traffic
- B. Commission a penetration test
- C. Run a load test at the expected peak
- D. Run a chaos experiment against a zone

### 79. The same outage has happened twice this quarter. What should be produced after each incident?

Domain: Ensuring solution and operations excellence

- A. Publish a shared dashboard
- B. Write a blameless postmortem with actions
- C. Publish a runbook per alert
- D. Match the support plan to the recovery commitment

### 80. A subsidiary must release during business hours with a reversible step. Which sequence is correct?

Domain: Ensuring solution and operations excellence

- A. Build an immutable image and record its digest → deploy the new revision without traffic → shift a small traffic percentage and watch error and latency signals → promote to full traffic or roll back to the pinned digest
- B. Shift full traffic to the new revision → build the image → watch the error rate → promote or roll back
- C. Deploy the new revision → promote to full traffic → shift a small percentage → build the image
- D. Watch the error rate → deploy the new revision → shift traffic → build the image

---

## Case study — Kestrel Airlines

Kestrel Airlines sells seats through a booking service that must stay available during the sale that opens twice a year. A sale can produce 40,000 seat requests per second for the first ten minutes, and two seats must never be sold twice even when the requests land in different regions. The booking database currently runs on PostgreSQL on premises and the loyalty programme runs on a separate mainframe that cannot be changed this year. The airline operates in twelve countries and each country has a currency and a tax rule that must be applied at the moment of booking rather than in a nightly batch.

The next 5 questions refer to it. Read the scenario once, then answer all 5; each item restates the constraint it tests and is scored individually.

### 81. Two seats must never be sold twice across two regions during a sale. What should hold the inventory?

Domain: Designing and planning a cloud solution architecture

- A. Use Cloud SQL
- B. Use Spanner
- C. Use Bigtable
- D. Use Firestore

### 82. Currency and tax must be applied at the moment of booking rather than overnight. What should the design use?

Domain: Designing and planning a cloud solution architecture

- A. Use Dataflow
- B. Trigger the job with Cloud Scheduler
- C. Use a Dataproc cluster
- D. Use Managed Service for Apache Airflow

### 83. The airline must show who changed a fare and when. What should be enabled?

Domain: Designing for security and compliance

- A. Rely on Admin Activity audit logs
- B. Create a log-based metric
- C. Review Access Transparency logs
- D. Enable Data Access audit logs

### 84. The twice-yearly sale must not fail on concurrency. What should be run beforehand?

Domain: Analyzing and optimizing technical and business processes

- A. Cover the change with unit, integration, and a few end-to-end tests
- B. Run a chaos experiment against a zone
- C. Run a load test at the expected peak
- D. Commission a penetration test

### 85. The sale opens at midnight and the response must not depend on who is awake. What should be published?

Domain: Ensuring solution and operations excellence

- A. Publish a runbook per alert
- B. Define an on-call rotation with an escalation path
- C. Match the support plan to the recovery commitment
- D. Publish a shared dashboard

---

## Case study — Lumen Analytics

Lumen Analytics sells a multi-tenant analytics product to 300 customers. Each customer expects its data to be isolated and its queries to run in under two seconds against a 40 GB dataset. The engineering team wants a single deployment that serves every tenant, with a per-tenant cost figure the sales team can quote. Customers are onboarding at roughly twenty a month, and the team has four engineers who are already on call for the serving layer. Tenants range from a five-person startup to a bank that requires a signed data-processing agreement and a named region.

The next 5 questions refer to it. Read the scenario once, then answer all 5; each item restates the constraint it tests and is scored individually.

### 86. 300 tenants must share one deployment and idle tenants must cost nothing. What should be used?

Domain: Designing and planning a cloud solution architecture

- A. Use a managed instance group with autoscaling
- B. Use GKE Standard with a node pool per workload shape
- C. Deploy the service on Cloud Run
- D. Run the legacy stack on Google Cloud VMware Engine

### 87. One tenant requires a signed agreement naming the region. What must the design fix?

Domain: Designing and planning a cloud solution architecture

- A. Define the baseline and target as a KPI with an owner
- B. Keep the data in the region the regulator requires
- C. Document the exit plan and data portability
- D. Build a three-year total cost of ownership model

### 88. Each new tenant needs an isolated environment created the same way every time. What should be used?

Domain: Managing and provisioning a solution infrastructure

- A. Manage the resources with Config Connector
- B. Automate the step with the gcloud CLI
- C. Use Deployment Manager templates
- D. Manage the resources with Terraform

### 89. A bank tenant must reach the service privately from its own network. What should be published?

Domain: Designing for security and compliance

- A. Publish the service through Private Service Connect
- B. Create a DNS peering zone
- C. Enable Private Google Access on the subnet
- D. Deploy Cloud NAT for outbound traffic

### 90. The sales team quotes a two-second query target per tenant. How should it be monitored?

Domain: Ensuring solution and operations excellence

- A. Create an alerting policy on the metric
- B. Define an SLO with an error budget
- C. Publish a shared dashboard
- D. Add an uptime check from several regions

---

## Case study — Quarry Manufacturing

Quarry Manufacturing runs twelve plants that each host a historian, a manufacturing execution system, and a local file share. Plant engineers need the telemetry from the plant floor inside Google Cloud within a second to drive a predictive maintenance model, and the plants have unreliable internet links that drop for minutes at a time. Corporate policy forbids any inbound connection from the internet to a plant network. The company wants the same architecture in every plant, deployed from one template, and it needs an operator at each site to see plant status even when the wide-area link is down.

The next 5 questions refer to it. Read the scenario once, then answer all 5; each item restates the constraint it tests and is scored individually.

### 91. Twelve plants must be assessed before a single template is written. What should be used?

Domain: Designing and planning a cloud solution architecture

- A. Use Database Migration Service
- B. Copy the files with Storage Transfer Service
- C. Convert the VMs with Migrate to Containers
- D. Assess the estate in Migration Center

### 92. Plant servers must stay patched although nobody is on site at night. What should be used?

Domain: Managing and provisioning a solution infrastructure

- A. Use a custom machine type sized to the workload
- B. Run the batch tier on Spot VMs
- C. Use VM Manager for OS patch compliance
- D. Manage the resources with Config Connector

### 93. A plant collector stopped at 02:14 and nobody knows why. Where should the team look first?

Domain: Analyzing and optimizing technical and business processes

- A. Publish a shared dashboard
- B. Act on the Recommender suggestions
- C. Query the entries in Cloud Logging
- D. Add an uptime check from several regions

### 94. The same stack must be deployed identically at twelve sites from one template. What should be used?

Domain: Managing implementation

- A. Automate the step with the gcloud CLI
- B. Manage the resources with Terraform
- C. Use Deployment Manager templates
- D. Manage the resources with Config Connector

### 95. Operators must see plant status even when the wide-area link is down. What should the design include?

Domain: Ensuring solution and operations excellence

- A. Define dashboards and metrics in Cloud Monitoring
- B. Act on the Recommender suggestions
- C. Publish a shared dashboard
- D. Inspect the trace waterfall in Cloud Trace

---

## Case study — Sable Financial

Sable Financial Group has 40 subsidiaries, 300 projects, and a regulator who requires that production data cannot leave the European Union. Each subsidiary has its own engineering team, and last year one team created a public bucket that held customer statements for eleven days. The group wants a resource structure where a new project inherits the network, the logging destination, and the security controls without a ticket. Network address space is managed centrally, and subsidiaries must not be able to create their own routes to the internet. Terraform is the standard tool, and the platform team wants every environment change to be reviewed before it is applied.

The next 5 questions refer to it. Read the scenario once, then answer all 5; each item restates the constraint it tests and is scored individually.

### 96. A subsidiary published customer statements in a public bucket last year. What should prevent a repeat in every future project?

Domain: Designing for security and compliance

- A. Tag the resources with labels for cost reporting
- B. Enforce the control with an organization policy constraint
- C. Create a separate project per environment
- D. Create a folder per environment and bind roles there

### 97. Subsidiaries need isolated environments but one centrally managed network. Which two constructs provide that? Select two.

Domain: Managing and provisioning a solution infrastructure

- A. Deploy Cloud NAT for outbound traffic
- B. Create a separate project per environment
- C. Create a DNS peering zone
- D. Use Shared VPC with host and service projects
- E. Peer the two VPC networks

### 98. No subsidiary may create its own route to the internet. What should be applied above the projects?

Domain: Designing and planning a cloud solution architecture

- A. Enable Cloud CDN on the backend
- B. Peer the two VPC networks
- C. Deploy Cloud NAT for outbound traffic
- D. Apply a hierarchical firewall policy at the organization or folder

### 99. Every environment change must be reviewed before it is applied. What should the pipeline enforce?

Domain: Analyzing and optimizing technical and business processes

- A. Roll the change out instance by instance
- B. Require a reviewed pull request and a passing plan
- C. Adopt trunk-based development with short-lived branches
- D. Rebuild the artifact separately for each environment

### 100. The public bucket was found eleven days later by an external researcher. What should follow the fix?

Domain: Ensuring solution and operations excellence

- A. Match the support plan to the recovery commitment
- B. Publish a runbook per alert
- C. Publish a shared dashboard
- D. Write a blameless postmortem with actions

---

## Answer key and explanations

### Question 1 — A

Answer: Define the baseline and target as a KPI with an owner. A measured baseline and a named owner make the outcome testable after the programme. Local study-map skill 1.1 (Business Requirements and Success Metrics), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 1 (designing and planning): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Correct. In this case: A measured baseline and a named owner make the outcome testable after the programme.
- **B:** Incorrect for this question. The model compares run cost, people cost, and exit cost rather than the monthly bill alone. Why the correct answer wins: A measured baseline and a named owner make the outcome testable after the programme.
- **C:** Incorrect for this question. The export attributes cost to the team and service that caused it. Why the correct answer wins: A measured baseline and a named owner make the outcome testable after the programme.
- **D:** Incorrect for this question. The dashboard gives the team one view of the same signals during an incident. Why the correct answer wins: A measured baseline and a named owner make the outcome testable after the programme.

### Question 2 — A

Answer: Document the exit plan and data portability. An exit plan and data portability keep the migration reversible and bound how proprietary the design may become. The exit plan keeps the migration reversible and constrains how proprietary the design may become. Local study-map skill 1.2 (Non-Functional Requirements and Trade-offs), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 1 (designing and planning): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Correct. The exit plan keeps the migration reversible and constrains how proprietary the design may become. In this case: An exit plan and data portability keep the migration reversible and bound how proprietary the design may become.
- **B:** Incorrect for this question. A budget alerts on spend but does not stop it. Why the correct answer wins: An exit plan and data portability keep the migration reversible and bound how proprietary the design may become.
- **C:** Incorrect for this question. Labels attribute spend in billing export; they do not grant or restrict access. Why the correct answer wins: An exit plan and data portability keep the migration reversible and bound how proprietary the design may become.
- **D:** Incorrect for this question. The model compares run cost, people cost, and exit cost rather than the monthly bill alone. Why the correct answer wins: An exit plan and data portability keep the migration reversible and bound how proprietary the design may become.

### Question 3 — A, D

Answers: Set the RPO and RTO with the business owner; Put the recovery commitment in the contract. The targets quantify the acceptable loss, and the contract attaches a consequence to missing them. The targets come from the business impact of data loss and downtime, not from the technology. The contract converts an internal target into an obligation with a consequence. Local study-map skill 1.2 (Non-Functional Requirements and Trade-offs), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 1 (designing and planning): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Correct. The contract converts an internal target into an obligation with a consequence. In this case: The targets quantify the acceptable loss, and the contract attaches a consequence to missing them.
- **B:** Incorrect for this question. Labels attribute spend in billing export; they do not grant or restrict access. Why the correct answer wins: The targets quantify the acceptable loss, and the contract attaches a consequence to missing them.
- **C:** Incorrect for this question. The dashboard gives the team one view of the same signals during an incident. Why the correct answer wins: The targets quantify the acceptable loss, and the contract attaches a consequence to missing them.
- **D:** Correct. The targets come from the business impact of data loss and downtime, not from the technology. In this case: The targets quantify the acceptable loss, and the contract attaches a consequence to missing them.
- **E:** Incorrect for this question. Recommender reports idle and over-provisioned resources with the estimated saving. Why the correct answer wins: The targets quantify the acceptable loss, and the contract attaches a consequence to missing them.

### Question 4 — B

Answer: Create a regional GKE cluster. A regional cluster replicates the control plane across zones, so a zone loss does not stop scheduling. Local study-map skill 1.3 (High Availability and Failover Design), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 1 (designing and planning): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. The group replaces unhealthy instances and adds capacity from a template as load rises. Why the correct answer wins: A regional cluster replicates the control plane across zones, so a zone loss does not stop scheduling.
- **B:** Correct. In this case: A regional cluster replicates the control plane across zones, so a zone loss does not stop scheduling.
- **C:** Incorrect for this question. Cloud Run runs a stateless container per request and scales to zero when idle. Why the correct answer wins: A regional cluster replicates the control plane across zones, so a zone loss does not stop scheduling.
- **D:** Incorrect for this question. A zonal cluster keeps its control plane in one zone, so that zone loss takes the cluster with it. Why the correct answer wins: A regional cluster replicates the control plane across zones, so a zone loss does not stop scheduling.

### Question 5 — A, B

Answers: Enable Cloud SQL high availability with a standby; Replicate the data to the second region. The standby takes over the database, and the data must already exist in the region where it takes over. A regional standby takes over automatically when the primary zone fails. The data must exist in the second region before any compute there can serve it. Local study-map skill 1.3 (High Availability and Failover Design), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 1 (designing and planning): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Correct. The data must exist in the second region before any compute there can serve it. In this case: The standby takes over the database, and the data must already exist in the region where it takes over.
- **B:** Correct. A regional standby takes over automatically when the primary zone fails. In this case: The standby takes over the database, and the data must already exist in the region where it takes over.
- **C:** Incorrect for this question. Memorystore provides managed Redis or Memcached for sub-millisecond cache lookups. Why the correct answer wins: The standby takes over the database, and the data must already exist in the region where it takes over.
- **D:** Incorrect for this question. CDN caches responses at edge locations, which cuts origin load and latency for repeat reads. Why the correct answer wins: The standby takes over the database, and the data must already exist in the region where it takes over.
- **E:** Incorrect for this question. The view stores the aggregate result and refreshes incrementally as base data arrives. Why the correct answer wins: The standby takes over the database, and the data must already exist in the region where it takes over.

### Question 6 — B

Answer: Build a Network Connectivity Center hub. Peering is not transitive, so a hub provides the routing the spokes cannot provide themselves. The hub gives transitive routing between spokes, which peering alone cannot provide. Local study-map skill 1.4 (Network Design), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 1 (designing and planning): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. Peering joins two networks at layer three but does not share firewalls or transitive routes. Why the correct answer wins: Peering is not transitive, so a hub provides the routing the spokes cannot provide themselves.
- **B:** Correct. The hub gives transitive routing between spokes, which peering alone cannot provide. In this case: Peering is not transitive, so a hub provides the routing the spokes cannot provide themselves.
- **C:** Incorrect for this question. Cloud NAT lets private instances reach the internet without an external address. Why the correct answer wins: Peering is not transitive, so a hub provides the routing the spokes cannot provide themselves.
- **D:** Incorrect for this question. DNS peering resolves names across networks without transferring zone ownership. Why the correct answer wins: Peering is not transitive, so a hub provides the routing the spokes cannot provide themselves.

### Question 7 — B, D

Answers: Publish the service through Private Service Connect; Peer the two VPC networks. A published endpoint gives a private address, and peering joins the two networks at layer three. A PSC endpoint gives a private IP in the consumer VPC without peering or exposing the service publicly. Peering joins two networks at layer three but does not share firewalls or transitive routes. Local study-map skill 1.4 (Network Design), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 1 (designing and planning): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. Cloud NAT lets private instances reach the internet without an external address. Why the correct answer wins: A published endpoint gives a private address, and peering joins the two networks at layer three.
- **B:** Correct. A PSC endpoint gives a private IP in the consumer VPC without peering or exposing the service publicly. In this case: A published endpoint gives a private address, and peering joins the two networks at layer three.
- **C:** Incorrect for this question. CDN caches responses at edge locations, which cuts origin load and latency for repeat reads. Why the correct answer wins: A published endpoint gives a private address, and peering joins the two networks at layer three.
- **D:** Correct. Peering joins two networks at layer three but does not share firewalls or transitive routes. In this case: A published endpoint gives a private address, and peering joins the two networks at layer three.
- **E:** Incorrect for this question. A signed URL grants one object for a fixed time without exposing credentials or making the bucket public. Why the correct answer wins: A published endpoint gives a private address, and peering joins the two networks at layer three.

### Question 8 — D

Answer: Order a Dedicated Interconnect. A dedicated circuit gives predictable bandwidth over a private path at a colocation facility. Local study-map skill 1.4 (Network Design), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 1 (designing and planning): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. A partner circuit reaches Google Cloud through a provider when the site is not in a colocation facility. Why the correct answer wins: A dedicated circuit gives predictable bandwidth over a private path at a colocation facility.
- **B:** Incorrect for this question. Two tunnels across two interfaces survive one path failing, and the SLA depends on that. Why the correct answer wins: A dedicated circuit gives predictable bandwidth over a private path at a colocation facility.
- **C:** Incorrect for this question. Cloud NAT lets private instances reach the internet without an external address. Why the correct answer wins: A dedicated circuit gives predictable bandwidth over a private path at a colocation facility.
- **D:** Correct. In this case: A dedicated circuit gives predictable bandwidth over a private path at a colocation facility.

### Question 9 — A

Answer: Use Bigtable. Bigtable is the wide-column store built for high-throughput key access at low latency. Bigtable is a wide-column store for high-throughput key reads and writes at low latency. Local study-map skill 1.5 (Storage and Data Store Selection), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 1 (designing and planning): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Correct. Bigtable is a wide-column store for high-throughput key reads and writes at low latency. In this case: Bigtable is the wide-column store built for high-throughput key access at low latency.
- **B:** Incorrect for this question. BigQuery is serverless, columnar, and separates storage from compute, so a scan pays for the bytes read. Why the correct answer wins: Bigtable is the wide-column store built for high-throughput key access at low latency.
- **C:** Incorrect for this question. Firestore is a document store with real-time listeners and per-document transactions. Why the correct answer wins: Bigtable is the wide-column store built for high-throughput key access at low latency.
- **D:** Incorrect for this question. Cloud SQL is a managed MySQL, PostgreSQL, or SQL Server instance with a familiar connection model. Why the correct answer wins: Bigtable is the wide-column store built for high-throughput key access at low latency.

### Question 10 — D, E

Answers: Enable Autoclass on the bucket; Add a lifecycle rule that transitions and then deletes. Autoclass moves objects between classes as access changes, and the lifecycle rule deletes on age. Autoclass moves each object between classes as its access pattern changes, with no lifecycle rules to maintain. A lifecycle rule acts on object age or class, so retention stops depending on a person. Local study-map skill 1.5 (Storage and Data Store Selection), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 1 (designing and planning): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. Filestore provides a managed NFS export that many clients can mount at once. Why the correct answer wins: Autoclass moves objects between classes as access changes, and the lifecycle rule deletes on age.
- **B:** Incorrect for this question. Local SSD is the fastest ephemeral option and loses its data when the VM stops. Why the correct answer wins: Autoclass moves objects between classes as access changes, and the lifecycle rule deletes on age.
- **C:** Incorrect for this question. Nearline suits data read about once a month and charges for early deletion. Why the correct answer wins: Autoclass moves objects between classes as access changes, and the lifecycle rule deletes on age.
- **D:** Correct. A lifecycle rule acts on object age or class, so retention stops depending on a person. In this case: Autoclass moves objects between classes as access changes, and the lifecycle rule deletes on age.
- **E:** Correct. Autoclass moves each object between classes as its access pattern changes, with no lifecycle rules to maintain. In this case: Autoclass moves objects between classes as access changes, and the lifecycle rule deletes on age.

### Question 11 — C

Answer: Deploy the service on Cloud Run. Cloud Run scales to zero and bills per request, which suits an intermittent internal tool. Cloud Run runs a stateless container per request and scales to zero when idle. Local study-map skill 1.6 (Compute Platform Selection), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 1 (designing and planning): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. VMware Engine keeps the existing hypervisor and operations model while moving the hardware into Google Cloud. Why the correct answer wins: Cloud Run scales to zero and bills per request, which suits an intermittent internal tool.
- **B:** Incorrect for this question. The group replaces unhealthy instances and adds capacity from a template as load rises. Why the correct answer wins: Cloud Run scales to zero and bills per request, which suits an intermittent internal tool.
- **C:** Correct. Cloud Run runs a stateless container per request and scales to zero when idle. In this case: Cloud Run scales to zero and bills per request, which suits an intermittent internal tool.
- **D:** Incorrect for this question. Standard exposes node configuration and patching, which the team must then run itself. Why the correct answer wins: Cloud Run scales to zero and bills per request, which suits an intermittent internal tool.

### Question 12 — D

Answer: Use GKE Autopilot. Autopilot manages nodes, scaling, and patching, so the team owns only its workloads. Local study-map skill 1.6 (Compute Platform Selection), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 1 (designing and planning): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. Standard exposes node configuration and patching, which the team must then run itself. Why the correct answer wins: Autopilot manages nodes, scaling, and patching, so the team owns only its workloads.
- **B:** Incorrect for this question. Batch schedules containerised jobs onto managed or existing capacity and retires it when done. Why the correct answer wins: Autopilot manages nodes, scaling, and patching, so the team owns only its workloads.
- **C:** Incorrect for this question. Cloud Run runs a stateless container per request and scales to zero when idle. Why the correct answer wins: Autopilot manages nodes, scaling, and patching, so the team owns only its workloads.
- **D:** Correct. In this case: Autopilot manages nodes, scaling, and patching, so the team owns only its workloads.

### Question 13 — C

Answer: Submit the work as a Batch job. Batch schedules containerised jobs onto managed capacity and retires it when the work is done. Local study-map skill 1.6 (Compute Platform Selection), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 1 (designing and planning): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. Standard exposes node configuration and patching, which the team must then run itself. Why the correct answer wins: Batch schedules containerised jobs onto managed capacity and retires it when the work is done.
- **B:** Incorrect for this question. The group replaces unhealthy instances and adds capacity from a template as load rises. Why the correct answer wins: Batch schedules containerised jobs onto managed capacity and retires it when the work is done.
- **C:** Correct. In this case: Batch schedules containerised jobs onto managed capacity and retires it when the work is done.
- **D:** Incorrect for this question. Cloud Run runs a stateless container per request and scales to zero when idle. Why the correct answer wins: Batch schedules containerised jobs onto managed capacity and retires it when the work is done.

### Question 14 — C

Answer: Use Dataproc Serverless. Serverless Spark runs the batch without cluster sizing or idle cost between jobs. Local study-map skill 1.7 (Data Processing and Analytics Selection), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 1 (designing and planning): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. A Dataproc cluster runs open-source Spark and Hadoop with jobs that need a persistent cluster. Why the correct answer wins: Serverless Spark runs the batch without cluster sizing or idle cost between jobs.
- **B:** Incorrect for this question. Airflow expresses dependencies between scheduled jobs and retries a failed task without rerunning the rest. Why the correct answer wins: Serverless Spark runs the batch without cluster sizing or idle cost between jobs.
- **C:** Correct. In this case: Serverless Spark runs the batch without cluster sizing or idle cost between jobs.
- **D:** Incorrect for this question. Dataflow runs an Apache Beam pipeline with autoscaling and a single programming model for batch and streaming. Why the correct answer wins: Serverless Spark runs the batch without cluster sizing or idle cost between jobs.

### Question 15 — C

Answer: Use Dataflow. Dataflow runs one Apache Beam pipeline with autoscaling in both batch and streaming modes. Local study-map skill 1.7 (Data Processing and Analytics Selection), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 1 (designing and planning): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. The service runs scheduled loads from SaaS sources and other clouds into BigQuery. Why the correct answer wins: Dataflow runs one Apache Beam pipeline with autoscaling in both batch and streaming modes.
- **B:** Incorrect for this question. A Dataproc cluster runs open-source Spark and Hadoop with jobs that need a persistent cluster. Why the correct answer wins: Dataflow runs one Apache Beam pipeline with autoscaling in both batch and streaming modes.
- **C:** Correct. In this case: Dataflow runs one Apache Beam pipeline with autoscaling in both batch and streaming modes.
- **D:** Incorrect for this question. Scheduler fires a job on a cron or App Engine schedule and retries on failure. Why the correct answer wins: Dataflow runs one Apache Beam pipeline with autoscaling in both batch and streaming modes.

### Question 16 — A

Answer: Call Gemini through Agent Platform. The managed endpoint adds IAM, audit logging, and regional processing terms. Local study-map skill 1.8 (AI and ML Solution Design), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 1 (designing and planning): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Correct. In this case: The managed endpoint adds IAM, audit logging, and regional processing terms.
- **B:** Incorrect for this question. The prebuilt Vision model labels, detects, and reads text without training a model. Why the correct answer wins: The managed endpoint adds IAM, audit logging, and regional processing terms.
- **C:** Incorrect for this question. Vertex AI Search returns grounded, cited results over private documents without a custom index. Why the correct answer wins: The managed endpoint adds IAM, audit logging, and regional processing terms.
- **D:** Incorrect for this question. Gemini Enterprise adds enterprise search, agents, and governance over the connected corpus. Why the correct answer wins: The managed endpoint adds IAM, audit logging, and regional processing terms.

### Question 17 — D, E

Answers: Serve features from Agent Platform Feature Store; Enable model monitoring on the endpoint. Feature Store keeps one definition for training and serving, and monitoring compares live traffic with the baseline. Feature Store keeps one definition for training and serving, which prevents training-serving skew. Monitoring compares live traffic against the training baseline and reports skew and drift. Local study-map skill 1.8 (AI and ML Solution Design), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 1 (designing and planning): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. Model Garden lists first-party and open models with deployment options and licensing. Why the correct answer wins: Feature Store keeps one definition for training and serving, and monitoring compares live traffic with the baseline.
- **B:** Incorrect for this question. The kit gives code-first control over tools and state when a low-code builder is not enough. Why the correct answer wins: Feature Store keeps one definition for training and serving, and monitoring compares live traffic with the baseline.
- **C:** Incorrect for this question. Cloud Assist explains configurations and proposes changes inside the console with your permissions. Why the correct answer wins: Feature Store keeps one definition for training and serving, and monitoring compares live traffic with the baseline.
- **D:** Correct. Monitoring compares live traffic against the training baseline and reports skew and drift. In this case: Feature Store keeps one definition for training and serving, and monitoring compares live traffic with the baseline.
- **E:** Correct. Feature Store keeps one definition for training and serving, which prevents training-serving skew. In this case: Feature Store keeps one definition for training and serving, and monitoring compares live traffic with the baseline.

### Question 18 — B

Answer: Assess the estate in Migration Center. Migration Center inventories the estate and estimates target size and cost before a plan is funded. Migration Center inventories the servers and estimates the target size and cost. Local study-map skill 1.9 (Migration Planning and Future Improvement), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 1 (designing and planning): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. The service moves object data between buckets or clouds on a schedule. Why the correct answer wins: Migration Center inventories the estate and estimates target size and cost before a plan is funded.
- **B:** Correct. Migration Center inventories the servers and estimates the target size and cost. In this case: Migration Center inventories the estate and estimates target size and cost before a plan is funded.
- **C:** Incorrect for this question. The service moves a database with continuous replication and a short cutover window. Why the correct answer wins: Migration Center inventories the estate and estimates target size and cost before a plan is funded.
- **D:** Incorrect for this question. The tool rewrites a VM workload into a container image so it can run on GKE. Why the correct answer wins: Migration Center inventories the estate and estimates target size and cost before a plan is funded.

### Question 19 — C

Answer: Set the RTO and RPO targets → choose the DR pattern that meets them → build and replicate the standby environment → fail over in a game day and record the result. Targets drive the pattern, the pattern drives the build, and only a rehearsal proves the numbers. Local study-map skill 1.9 (Migration Planning and Future Improvement), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 1 (designing and planning): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. The pattern has no basis until the targets exist, and the drill cannot precede the build. Why the correct answer wins: Targets drive the pattern, the pattern drives the build, and only a rehearsal proves the numbers.
- **B:** Incorrect for this question. A failover drill with no targets or standby environment proves nothing. Why the correct answer wins: Targets drive the pattern, the pattern drives the build, and only a rehearsal proves the numbers.
- **C:** Correct. In this case: Targets drive the pattern, the pattern drives the build, and only a rehearsal proves the numbers.
- **D:** Incorrect for this question. Building before the targets and pattern are chosen risks an environment that cannot meet either. Why the correct answer wins: Targets drive the pattern, the pattern drives the build, and only a rehearsal proves the numbers.

### Question 20 — C

Answer: Use HA VPN with two tunnels. Two tunnels across two interfaces survive one path failing, and the SLA depends on that. Local study-map skill 2.1 (Hybrid and Multicloud Connectivity), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 2 (managing and provisioning): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. Cloud NAT lets private instances reach the internet without an external address. Why the correct answer wins: Two tunnels across two interfaces survive one path failing, and the SLA depends on that.
- **B:** Incorrect for this question. The allocated range lets managed services such as Cloud SQL use internal addresses in your network. Why the correct answer wins: Two tunnels across two interfaces survive one path failing, and the SLA depends on that.
- **C:** Correct. In this case: Two tunnels across two interfaces survive one path failing, and the SLA depends on that.
- **D:** Incorrect for this question. CDN caches responses at edge locations, which cuts origin load and latency for repeat reads. Why the correct answer wins: Two tunnels across two interfaces survive one path failing, and the SLA depends on that.

### Question 21 — B

Answer: Add a VLAN attachment with a Cloud Router. The attachment terminates the circuit, and the router exchanges routes with the on-premises network. Local study-map skill 2.1 (Hybrid and Multicloud Connectivity), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 2 (managing and provisioning): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. The hub gives transitive routing between spokes, which peering alone cannot provide. Why the correct answer wins: The attachment terminates the circuit, and the router exchanges routes with the on-premises network.
- **B:** Correct. In this case: The attachment terminates the circuit, and the router exchanges routes with the on-premises network.
- **C:** Incorrect for this question. A dedicated circuit gives predictable bandwidth and a private path at a colocation facility. Why the correct answer wins: The attachment terminates the circuit, and the router exchanges routes with the on-premises network.
- **D:** Incorrect for this question. Two tunnels across two interfaces survive one path failing, and the SLA depends on that. Why the correct answer wins: The attachment terminates the circuit, and the router exchanges routes with the on-premises network.

### Question 22 — A, D

Answers: Deploy Cloud NAT for outbound traffic; Enable Private Google Access on the subnet. Cloud NAT carries outbound internet traffic, and Private Google Access reaches the APIs from an internal address. Cloud NAT lets private instances reach the internet without an external address. Private Google Access reaches Google APIs from an internal address without a proxy or a NAT gateway. Local study-map skill 2.1 (Hybrid and Multicloud Connectivity), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 2 (managing and provisioning): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Correct. Private Google Access reaches Google APIs from an internal address without a proxy or a NAT gateway. In this case: Cloud NAT carries outbound internet traffic, and Private Google Access reaches the APIs from an internal address.
- **B:** Incorrect for this question. Cloud Armor filters requests at the edge with allow and deny rules and adaptive protection. Why the correct answer wins: Cloud NAT carries outbound internet traffic, and Private Google Access reaches the APIs from an internal address.
- **C:** Incorrect for this question. IAP authenticates and authorises each request before it reaches the backend, with no VPN. Why the correct answer wins: Cloud NAT carries outbound internet traffic, and Private Google Access reaches the APIs from an internal address.
- **D:** Correct. Cloud NAT lets private instances reach the internet without an external address. In this case: Cloud NAT carries outbound internet traffic, and Private Google Access reaches the APIs from an internal address.
- **E:** Incorrect for this question. CDN caches responses at edge locations, which cuts origin load and latency for repeat reads. Why the correct answer wins: Cloud NAT carries outbound internet traffic, and Private Google Access reaches the APIs from an internal address.

### Question 23 — B

Answer: Apply a bucket retention policy with a locked period. A locked retention policy prevents deletion or a shorter period, which is the evidence an auditor tests. Local study-map skill 2.2 (Storage Configuration and Lifecycle), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 2 (managing and provisioning): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. Versioning keeps a noncurrent copy when an object is overwritten or deleted. Why the correct answer wins: A locked retention policy prevents deletion or a shorter period, which is the evidence an auditor tests.
- **B:** Correct. In this case: A locked retention policy prevents deletion or a shorter period, which is the evidence an auditor tests.
- **C:** Incorrect for this question. A lifecycle rule acts on object age or class, so retention stops depending on a person. Why the correct answer wins: A locked retention policy prevents deletion or a shorter period, which is the evidence an auditor tests.
- **D:** Incorrect for this question. Autoclass moves each object between classes as its access pattern changes, with no lifecycle rules to maintain. Why the correct answer wins: A locked retention policy prevents deletion or a shorter period, which is the evidence an auditor tests.

### Question 24 — C

Answer: Use Storage Transfer Service for the recurring copy. The service runs scheduled, filtered transfers from another cloud into a bucket. Local study-map skill 2.2 (Storage Configuration and Lifecycle), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 2 (managing and provisioning): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. The appliance ships the data physically when the network would take months to carry it. Why the correct answer wins: The service runs scheduled, filtered transfers from another cloud into a bucket.
- **B:** Incorrect for this question. The service moves object data between buckets or clouds on a schedule. Why the correct answer wins: The service runs scheduled, filtered transfers from another cloud into a bucket.
- **C:** Correct. In this case: The service runs scheduled, filtered transfers from another cloud into a bucket.
- **D:** Incorrect for this question. A signed URL grants one object for a fixed time without exposing credentials or making the bucket public. Why the correct answer wins: The service runs scheduled, filtered transfers from another cloud into a bucket.

### Question 25 — A, B

Answers: Partition the table on the date column; Cluster the table on the filter columns. Partitioning limits each query to the dates it names, and clustering sorts within the partition on the filter column. Partitioning limits a query to the date ranges it names, so it scans less. Clustering sorts within partitions so a filtered query reads fewer blocks. Local study-map skill 2.2 (Storage Configuration and Lifecycle), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 2 (managing and provisioning): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Correct. Partitioning limits a query to the date ranges it names, so it scans less. In this case: Partitioning limits each query to the dates it names, and clustering sorts within the partition on the filter column.
- **B:** Correct. Clustering sorts within partitions so a filtered query reads fewer blocks. In this case: Partitioning limits each query to the dates it names, and clustering sorts within the partition on the filter column.
- **C:** Incorrect for this question. The view stores the aggregate result and refreshes incrementally as base data arrives. Why the correct answer wins: Partitioning limits each query to the dates it names, and clustering sorts within the partition on the filter column.
- **D:** Incorrect for this question. Looker Studio renders the visualisation but inherits whatever query and permissions sit beneath it. Why the correct answer wins: Partitioning limits each query to the dates it names, and clustering sorts within the partition on the filter column.
- **E:** Incorrect for this question. On-demand bills per byte scanned, which is cheap for sparse use and unpredictable at scale. Why the correct answer wins: Partitioning limits each query to the dates it names, and clustering sorts within the partition on the filter column.

### Question 26 — D

Answer: Use VM Manager for OS patch compliance. VM Manager inventories and applies patches across the fleet instead of relying on manual runs. Local study-map skill 2.3 (Compute Provisioning and Patch Management), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 2 (managing and provisioning): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. Config Connector reconciles Google Cloud resources from Kubernetes manifests alongside the workloads. Why the correct answer wins: VM Manager inventories and applies patches across the fleet instead of relying on manual runs.
- **B:** Incorrect for this question. Cloud Build executes the pipeline steps in a managed, isolated worker with recorded provenance. Why the correct answer wins: VM Manager inventories and applies patches across the fleet instead of relying on manual runs.
- **C:** Incorrect for this question. Spot capacity costs far less but can be reclaimed with 30 seconds of notice. Why the correct answer wins: VM Manager inventories and applies patches across the fleet instead of relying on manual runs.
- **D:** Correct. In this case: VM Manager inventories and applies patches across the fleet instead of relying on manual runs.

### Question 27 — B, D

Answers: Run the batch tier on Spot VMs; Buy committed use discounts for the steady baseline. Spot capacity covers the burst, and a commitment discounts the capacity that runs constantly. Spot capacity costs far less but can be reclaimed with 30 seconds of notice. A one- or three-year commitment discounts the capacity that runs constantly, not the peaks. Local study-map skill 2.3 (Compute Provisioning and Patch Management), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 2 (managing and provisioning): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. E2 shapes trade peak performance for a lower price on workloads that do not need it. Why the correct answer wins: Spot capacity covers the burst, and a commitment discounts the capacity that runs constantly.
- **B:** Correct. Spot capacity costs far less but can be reclaimed with 30 seconds of notice. In this case: Spot capacity covers the burst, and a commitment discounts the capacity that runs constantly.
- **C:** Incorrect for this question. Local SSD is the fastest ephemeral option and loses its data when the VM stops. Why the correct answer wins: Spot capacity covers the burst, and a commitment discounts the capacity that runs constantly.
- **D:** Correct. A one- or three-year commitment discounts the capacity that runs constantly, not the peaks. In this case: Spot capacity covers the burst, and a commitment discounts the capacity that runs constantly.
- **E:** Incorrect for this question. Showing owners their own spend changes behaviour more reliably than a central report. Why the correct answer wins: Spot capacity covers the burst, and a commitment discounts the capacity that runs constantly.

### Question 28 — B

Answer: Use a custom machine type sized to the workload. Custom vCPU and memory avoid paying for a fixed shape that over-provisions one dimension. Local study-map skill 2.3 (Compute Provisioning and Patch Management), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 2 (managing and provisioning): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. Spot capacity costs far less but can be reclaimed with 30 seconds of notice. Why the correct answer wins: Custom vCPU and memory avoid paying for a fixed shape that over-provisions one dimension.
- **B:** Correct. In this case: Custom vCPU and memory avoid paying for a fixed shape that over-provisions one dimension.
- **C:** Incorrect for this question. Local SSD is the fastest ephemeral option and loses its data when the VM stops. Why the correct answer wins: Custom vCPU and memory avoid paying for a fixed shape that over-provisions one dimension.
- **D:** Incorrect for this question. Sole tenancy keeps the physical host dedicated, which matters for licensing or isolation rules. Why the correct answer wins: Custom vCPU and memory avoid paying for a fixed shape that over-provisions one dimension.

### Question 29 — D

Answer: Enable node auto-provisioning. Auto-provisioning adds node pools on demand for pending pods instead of pre-sizing them. Local study-map skill 2.4 (Container Orchestration), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 2 (managing and provisioning): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. A fleet gives one policy and identity plane across clusters without merging their networks. Why the correct answer wins: Auto-provisioning adds node pools on demand for pending pods instead of pre-sizing them.
- **B:** Incorrect for this question. The channel bounds the version drift and the window bounds when automatic upgrades may run. Why the correct answer wins: Auto-provisioning adds node pools on demand for pending pods instead of pre-sizing them.
- **C:** Incorrect for this question. Network policy restricts pod-to-pod traffic inside the cluster, which a firewall rule cannot see. Why the correct answer wins: Auto-provisioning adds node pools on demand for pending pods instead of pre-sizing them.
- **D:** Correct. In this case: Auto-provisioning adds node pools on demand for pending pods instead of pre-sizing them.

### Question 30 — A

Answer: Create private nodes with no external IP addresses. Private nodes reach Google APIs through Private Google Access from an internal address. Local study-map skill 2.4 (Container Orchestration), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 2 (managing and provisioning): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Correct. In this case: Private nodes reach Google APIs through Private Google Access from an internal address.
- **B:** Incorrect for this question. Sole tenancy keeps the physical host dedicated, which matters for licensing or isolation rules. Why the correct answer wins: Private nodes reach Google APIs through Private Google Access from an internal address.
- **C:** Incorrect for this question. Cloud NAT lets private instances reach the internet without an external address. Why the correct answer wins: Private nodes reach Google APIs through Private Google Access from an internal address.
- **D:** Incorrect for this question. A zonal cluster keeps its control plane in one zone, so that zone loss takes the cluster with it. Why the correct answer wins: Private nodes reach Google APIs through Private Google Access from an internal address.

### Question 31 — C

Answer: Create the project and enable APIs → build a Shared VPC with private subnets → create a regional private cluster with Workload Identity Federation for GKE → deploy through Binary Authorization. Network and identity exist before the cluster, and the admission policy is enforceable only once the cluster is running. Local study-map skill 2.4 (Container Orchestration), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 2 (managing and provisioning): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. The project precedes its network, and the deploy step belongs after the cluster rather than in the middle. Why the correct answer wins: Network and identity exist before the cluster, and the admission policy is enforceable only once the cluster is running.
- **B:** Incorrect for this question. Admission control cannot run before a cluster exists, and no resource can be created before its project. Why the correct answer wins: Network and identity exist before the cluster, and the admission policy is enforceable only once the cluster is running.
- **C:** Correct. In this case: Network and identity exist before the cluster, and the admission policy is enforceable only once the cluster is running.
- **D:** Incorrect for this question. A private cluster needs the shared network first, and the APIs must be enabled before any resource is created. Why the correct answer wins: Network and identity exist before the cluster, and the admission policy is enforceable only once the cluster is running.

### Question 32 — A

Answer: Raise the request concurrency setting. Concurrency packs more simultaneous requests into each instance before another is started. Local study-map skill 2.5 (Serverless Configuration), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 2 (managing and provisioning): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Correct. In this case: Concurrency packs more simultaneous requests into each instance before another is started.
- **B:** Incorrect for this question. Keeping warm instances removes cold starts at the cost of paying for idle capacity. Why the correct answer wins: Concurrency packs more simultaneous requests into each instance before another is started.
- **C:** Incorrect for this question. The flexible environment runs a custom runtime on managed VMs but does not scale to zero. Why the correct answer wins: Concurrency packs more simultaneous requests into each instance before another is started.
- **D:** Incorrect for this question. Serverless GPU attachment suits bursty inference where a reserved node would idle. Why the correct answer wins: Concurrency packs more simultaneous requests into each instance before another is started.

### Question 33 — C

Answer: Use Cloud Run functions. Functions bind one small handler to an event source and are the lightest way to react to one. Local study-map skill 2.5 (Serverless Configuration), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 2 (managing and provisioning): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. The group replaces unhealthy instances and adds capacity from a template as load rises. Why the correct answer wins: Functions bind one small handler to an event source and are the lightest way to react to one.
- **B:** Incorrect for this question. Batch schedules containerised jobs onto managed or existing capacity and retires it when done. Why the correct answer wins: Functions bind one small handler to an event source and are the lightest way to react to one.
- **C:** Correct. In this case: Functions bind one small handler to an event source and are the lightest way to react to one.
- **D:** Incorrect for this question. Cloud Run runs a stateless container per request and scales to zero when idle. Why the correct answer wins: Functions bind one small handler to an event source and are the lightest way to react to one.

### Question 34 — B

Answer: Create a remote state bucket with versioning → define modules per environment → run a plan in CI and require review → apply through the pipeline with a scoped service account. State is centralised before modules depend on it, plan review gates the apply, and the pipeline uses the least-privileged identity. Local study-map skill 2.6 (Infrastructure as Code), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 2 (managing and provisioning): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. Nothing can be planned before the modules and the state bucket exist. Why the correct answer wins: State is centralised before modules depend on it, plan review gates the apply, and the pipeline uses the least-privileged identity.
- **B:** Correct. In this case: State is centralised before modules depend on it, plan review gates the apply, and the pipeline uses the least-privileged identity.
- **C:** Incorrect for this question. State must be created before the first apply, and review must precede it as well. Why the correct answer wins: State is centralised before modules depend on it, plan review gates the apply, and the pipeline uses the least-privileged identity.
- **D:** Incorrect for this question. Applying before state exists duplicates infrastructure, and a plan cannot gate an apply that already happened. Why the correct answer wins: State is centralised before modules depend on it, plan review gates the apply, and the pipeline uses the least-privileged identity.

### Question 35 — A

Answer: Grant a predefined role at the narrowest resource. A predefined role grants the curated permission set for one job at the level it is bound to. Local study-map skill 3.1 (IAM and Least Privilege), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 3 (security and compliance): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Correct. In this case: A predefined role grants the curated permission set for one job at the level it is bound to.
- **B:** Incorrect for this question. A bastion is still an internet-facing host that must be patched and watched. Why the correct answer wins: A predefined role grants the curated permission set for one job at the level it is bound to.
- **C:** Incorrect for this question. A custom role expresses least privilege when no predefined role matches the job exactly. Why the correct answer wins: A predefined role grants the curated permission set for one job at the level it is bound to.
- **D:** Incorrect for this question. An API key identifies a project and does not authorise a user, so it cannot express least privilege. Why the correct answer wins: A predefined role grants the curated permission set for one job at the level it is bound to.

### Question 36 — C

Answer: Give each service its own service account. A per-service identity keeps the blast radius of a leaked credential to one workload. Local study-map skill 3.1 (IAM and Least Privilege), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 3 (security and compliance): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. A project is the boundary for quota, billing, and most IAM inheritance. Why the correct answer wins: A per-service identity keeps the blast radius of a leaked credential to one workload.
- **B:** Incorrect for this question. A key file is a long-lived credential that works until it is noticed and revoked. Why the correct answer wins: A per-service identity keeps the blast radius of a leaked credential to one workload.
- **C:** Correct. In this case: A per-service identity keeps the blast radius of a leaked credential to one workload.
- **D:** Incorrect for this question. Labels attribute spend in billing export; they do not grant or restrict access. Why the correct answer wins: A per-service identity keeps the blast radius of a leaked credential to one workload.

### Question 37 — C, D

Answers: Add an IAM condition on the binding; Apply an IAM deny policy. The condition narrows when the grant applies, and the deny policy overrides every allow beneath it. A condition narrows when a grant applies, for example to a time window or a resource prefix. A deny policy overrides every allow beneath it, which is how an exception is made impossible. Local study-map skill 3.1 (IAM and Least Privilege), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 3 (security and compliance): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. Labels attribute spend in billing export; they do not grant or restrict access. Why the correct answer wins: The condition narrows when the grant applies, and the deny policy overrides every allow beneath it.
- **B:** Incorrect for this question. A predefined role grants the curated permission set for one job at the level it is bound to. Why the correct answer wins: The condition narrows when the grant applies, and the deny policy overrides every allow beneath it.
- **C:** Correct. A deny policy overrides every allow beneath it, which is how an exception is made impossible. In this case: The condition narrows when the grant applies, and the deny policy overrides every allow beneath it.
- **D:** Correct. A condition narrows when a grant applies, for example to a time window or a resource prefix. In this case: The condition narrows when the grant applies, and the deny policy overrides every allow beneath it.
- **E:** Incorrect for this question. A bastion is still an internet-facing host that must be patched and watched. Why the correct answer wins: The condition narrows when the grant applies, and the deny policy overrides every allow beneath it.

### Question 38 — B

Answer: Create a folder per environment and bind roles there. A folder binding inherits to every project beneath it, so new projects start with the right access. Local study-map skill 3.2 (Resource Hierarchy and Organization Policy), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 3 (security and compliance): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. A predefined role grants the curated permission set for one job at the level it is bound to. Why the correct answer wins: A folder binding inherits to every project beneath it, so new projects start with the right access.
- **B:** Correct. In this case: A folder binding inherits to every project beneath it, so new projects start with the right access.
- **C:** Incorrect for this question. Labels attribute spend in billing export; they do not grant or restrict access. Why the correct answer wins: A folder binding inherits to every project beneath it, so new projects start with the right access.
- **D:** Incorrect for this question. A project is the boundary for quota, billing, and most IAM inheritance. Why the correct answer wins: A folder binding inherits to every project beneath it, so new projects start with the right access.

### Question 39 — A, C

Answers: Enforce the control with an organization policy constraint; Create a separate project per environment. The policy blocks the action across every project, and a project is the boundary for quota and billing. An organization policy blocks the action across every project regardless of who holds the role. A project is the boundary for quota, billing, and most IAM inheritance. Local study-map skill 3.2 (Resource Hierarchy and Organization Policy), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 3 (security and compliance): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Correct. A project is the boundary for quota, billing, and most IAM inheritance. In this case: The policy blocks the action across every project, and a project is the boundary for quota and billing.
- **B:** Incorrect for this question. Labels attribute spend in billing export; they do not grant or restrict access. Why the correct answer wins: The policy blocks the action across every project, and a project is the boundary for quota and billing.
- **C:** Correct. An organization policy blocks the action across every project regardless of who holds the role. In this case: The policy blocks the action across every project, and a project is the boundary for quota and billing.
- **D:** Incorrect for this question. A folder binding inherits to every project beneath it, so new projects start with the right access. Why the correct answer wins: The policy blocks the action across every project, and a project is the boundary for quota and billing.
- **E:** Incorrect for this question. A condition narrows when a grant applies, for example to a time window or a resource prefix. Why the correct answer wins: The policy blocks the action across every project, and a project is the boundary for quota and billing.

### Question 40 — D

Answer: Create the key ring in the same region as the data. A regional key ring keeps the key material in the region where the data lives. A regional key cannot encrypt a resource in another region, which is why residency drives key placement. Local study-map skill 3.3 (Encryption, CMEK, and Secrets), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 3 (security and compliance): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. CSEK is held by the caller and never stored by Google, so losing it loses the object. Why the correct answer wins: A regional key ring keeps the key material in the region where the data lives.
- **B:** Incorrect for this question. Cloud HSM keeps the key material in a hardware module that meets FIPS 140-2 level 3. Why the correct answer wins: A regional key ring keeps the key material in the region where the data lives.
- **C:** Incorrect for this question. Secret Manager versions the secret, controls access by IAM, and can rotate it. Why the correct answer wins: A regional key ring keeps the key material in the region where the data lives.
- **D:** Correct. A regional key cannot encrypt a resource in another region, which is why residency drives key placement. In this case: A regional key ring keeps the key material in the region where the data lives.

### Question 41 — B, D

Answers: Encrypt with a customer-managed key in Cloud KMS; Set an automatic rotation period on the key. A customer-managed key gives the bank control, and automatic rotation issues a new version on schedule. CMEK lets you control the key lifecycle, rotation, and the ability to revoke access to the data. Rotation issues a new key version on schedule and keeps old versions for decryption. Local study-map skill 3.3 (Encryption, CMEK, and Secrets), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 3 (security and compliance): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. CSEK is held by the caller and never stored by Google, so losing it loses the object. Why the correct answer wins: A customer-managed key gives the bank control, and automatic rotation issues a new version on schedule.
- **B:** Correct. CMEK lets you control the key lifecycle, rotation, and the ability to revoke access to the data. In this case: A customer-managed key gives the bank control, and automatic rotation issues a new version on schedule.
- **C:** Incorrect for this question. Cloud HSM keeps the key material in a hardware module that meets FIPS 140-2 level 3. Why the correct answer wins: A customer-managed key gives the bank control, and automatic rotation issues a new version on schedule.
- **D:** Correct. Rotation issues a new key version on schedule and keeps old versions for decryption. In this case: A customer-managed key gives the bank control, and automatic rotation issues a new version on schedule.
- **E:** Incorrect for this question. An environment variable is visible to anything that can read the instance metadata or the process list. Why the correct answer wins: A customer-managed key gives the bank control, and automatic rotation issues a new version on schedule.

### Question 42 — D

Answer: Put the projects inside a VPC Service Controls perimeter. A service perimeter blocks data movement out of the covered services even for a principal with the role. Local study-map skill 3.4 (VPC Service Controls and Network Security), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 3 (security and compliance): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. A deny policy overrides every allow beneath it, which is how an exception is made impossible. Why the correct answer wins: A service perimeter blocks data movement out of the covered services even for a principal with the role.
- **B:** Incorrect for this question. Labels attribute spend in billing export; they do not grant or restrict access. Why the correct answer wins: A service perimeter blocks data movement out of the covered services even for a principal with the role.
- **C:** Incorrect for this question. A policy above the project applies to every current and future network beneath it. Why the correct answer wins: A service perimeter blocks data movement out of the covered services even for a principal with the role.
- **D:** Correct. In this case: A service perimeter blocks data movement out of the covered services even for a principal with the role.

### Question 43 — D

Answer: Allocate private services access for the peered services. The allocated range lets managed services use internal addresses in your network. Local study-map skill 3.4 (VPC Service Controls and Network Security), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 3 (security and compliance): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. Cloud NAT lets private instances reach the internet without an external address. Why the correct answer wins: The allocated range lets managed services use internal addresses in your network.
- **B:** Incorrect for this question. A PSC endpoint gives a private IP in the consumer VPC without peering or exposing the service publicly. Why the correct answer wins: The allocated range lets managed services use internal addresses in your network.
- **C:** Incorrect for this question. Private Google Access reaches Google APIs from an internal address without a proxy or a NAT gateway. Why the correct answer wins: The allocated range lets managed services use internal addresses in your network.
- **D:** Correct. In this case: The allocated range lets managed services use internal addresses in your network.

### Question 44 — B

Answer: Use Workload Identity Federation for the external pipeline. Federation exchanges an external token for short-lived credentials, so no key leaves the provider. Local study-map skill 3.5 (Secure Remote Access and Zero Trust), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 3 (security and compliance): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. An API key identifies a project and does not authorise a user, so it cannot express least privilege. Why the correct answer wins: Federation exchanges an external token for short-lived credentials, so no key leaves the provider.
- **B:** Correct. In this case: Federation exchanges an external token for short-lived credentials, so no key leaves the provider.
- **C:** Incorrect for this question. An environment variable is visible to anything that can read the instance metadata or the process list. Why the correct answer wins: Federation exchanges an external token for short-lived credentials, so no key leaves the provider.
- **D:** Incorrect for this question. A key file is a long-lived credential that works until it is noticed and revoked. Why the correct answer wins: Federation exchanges an external token for short-lived credentials, so no key leaves the provider.

### Question 45 — B

Answer: Put Identity-Aware Proxy in front of the application. Identity-Aware Proxy authenticates and authorises each request before it reaches the backend. Local study-map skill 3.5 (Secure Remote Access and Zero Trust), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 3 (security and compliance): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. A bastion is still an internet-facing host that must be patched and watched. Why the correct answer wins: Identity-Aware Proxy authenticates and authorises each request before it reaches the backend.
- **B:** Correct. In this case: Identity-Aware Proxy authenticates and authorises each request before it reaches the backend.
- **C:** Incorrect for this question. Cloud NAT lets private instances reach the internet without an external address. Why the correct answer wins: Identity-Aware Proxy authenticates and authorises each request before it reaches the backend.
- **D:** Incorrect for this question. Private Google Access reaches Google APIs from an internal address without a proxy or a NAT gateway. Why the correct answer wins: Identity-Aware Proxy authenticates and authorises each request before it reaches the backend.

### Question 46 — D

Answer: Store the images in Artifact Registry. Artifact Registry holds the image with IAM-scoped access and vulnerability metadata. Local study-map skill 3.6 (Software Supply Chain Security), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 3 (security and compliance): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. Cloud Shell provides an authenticated terminal and editor with no local installation. Why the correct answer wins: Artifact Registry holds the image with IAM-scoped access and vulnerability metadata.
- **B:** Incorrect for this question. Scanning reports known vulnerabilities in the image layers before deployment. Why the correct answer wins: Artifact Registry holds the image with IAM-scoped access and vulnerability metadata.
- **C:** Incorrect for this question. Standard is for data read frequently and has no retrieval fee. Why the correct answer wins: Artifact Registry holds the image with IAM-scoped access and vulnerability metadata.
- **D:** Correct. In this case: Artifact Registry holds the image with IAM-scoped access and vulnerability metadata.

### Question 47 — C

Answer: De-identify the data with Sensitive Data Protection. Sensitive Data Protection finds and redacts or tokenizes the sensitive fields before they are stored. Sensitive Data Protection finds and redacts, tokenizes, or format-preservingly encrypts sensitive fields. Local study-map skill 3.7 (Securing AI Workloads), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 3 (security and compliance): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. The access level adds device and network conditions to the perimeter rule. Why the correct answer wins: Sensitive Data Protection finds and redacts or tokenizes the sensitive fields before they are stored.
- **B:** Incorrect for this question. Security Command Center aggregates misconfiguration and threat findings across the organization. Why the correct answer wins: Sensitive Data Protection finds and redacts or tokenizes the sensitive fields before they are stored.
- **C:** Correct. Sensitive Data Protection finds and redacts, tokenizes, or format-preservingly encrypts sensitive fields. In this case: Sensitive Data Protection finds and redacts or tokenizes the sensitive fields before they are stored.
- **D:** Incorrect for this question. Model Armor detects prompt injection, jailbreak attempts, and unsafe content before and after the model call. Why the correct answer wins: Sensitive Data Protection finds and redacts or tokenizes the sensitive fields before they are stored.

### Question 48 — D

Answer: Inventory projects and data flows → enable the audit logs needed for the perimeter → create the service perimeter in dry-run mode → review violations and enforce the perimeter. The inventory defines the boundary, dry run surfaces legitimate flows, and enforcement follows the review. Local study-map skill 3.8 (Compliance, Residency, and Audit Logging), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 3 (security and compliance): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. Enforcing before a dry run breaks legitimate traffic that was never catalogued. Why the correct answer wins: The inventory defines the boundary, dry run surfaces legitimate flows, and enforcement follows the review.
- **B:** Incorrect for this question. Reviewing after enforcement means the breakage has already happened. Why the correct answer wins: The inventory defines the boundary, dry run surfaces legitimate flows, and enforcement follows the review.
- **C:** Incorrect for this question. Enforcement in the second step leaves no review window, and the inventory is the first step. Why the correct answer wins: The inventory defines the boundary, dry run surfaces legitimate flows, and enforcement follows the review.
- **D:** Correct. In this case: The inventory defines the boundary, dry run surfaces legitimate flows, and enforcement follows the review.

### Question 49 — A

Answer: Adopt trunk-based development with short-lived branches. Short-lived branches reduce merge conflict and keep the mainline deployable. Local study-map skill 4.1 (SDLC and CI/CD Design), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 4 (analyzing and optimizing): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Correct. In this case: Short-lived branches reduce merge conflict and keep the mainline deployable.
- **B:** Incorrect for this question. A rolling replacement keeps capacity but exposes the whole fleet before the signal is trusted. Why the correct answer wins: Short-lived branches reduce merge conflict and keep the mainline deployable.
- **C:** Incorrect for this question. The flag separates deployment from release, so the code can ship dark and be turned off instantly. Why the correct answer wins: Short-lived branches reduce merge conflict and keep the mainline deployable.
- **D:** Incorrect for this question. A rebuild produces a different artifact, so the test result no longer applies to production. Why the correct answer wins: Short-lived branches reduce merge conflict and keep the mainline deployable.

### Question 50 — A, D

Answers: Require a reviewed pull request and a passing plan; Promote the same tested artifact between environments. The gate makes review mandatory, and promotion keeps one immutable artifact. The gate makes a second person check the change and its plan before it can apply. Promotion moves one immutable artifact forward, so what was tested is what runs. Local study-map skill 4.1 (SDLC and CI/CD Design), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 4 (analyzing and optimizing): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Correct. Promotion moves one immutable artifact forward, so what was tested is what runs. In this case: The gate makes review mandatory, and promotion keeps one immutable artifact.
- **B:** Incorrect for this question. A rolling replacement keeps capacity but exposes the whole fleet before the signal is trusted. Why the correct answer wins: The gate makes review mandatory, and promotion keeps one immutable artifact.
- **C:** Incorrect for this question. A rebuild produces a different artifact, so the test result no longer applies to production. Why the correct answer wins: The gate makes review mandatory, and promotion keeps one immutable artifact.
- **D:** Correct. The gate makes a second person check the change and its plan before it can apply. In this case: The gate makes review mandatory, and promotion keeps one immutable artifact.
- **E:** Incorrect for this question. A budget alerts on spend but does not stop it. Why the correct answer wins: The gate makes review mandatory, and promotion keeps one immutable artifact.

### Question 51 — D

Answer: Inspect the trace waterfall in Cloud Trace. Trace shows how one request spent its time across services and calls. Local study-map skill 4.2 (Root Cause Analysis), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 4 (analyzing and optimizing): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. The check measures availability from outside, which no internal metric can prove. Why the correct answer wins: Trace shows how one request spent its time across services and calls.
- **B:** Incorrect for this question. The dashboard gives the team one view of the same signals during an incident. Why the correct answer wins: Trace shows how one request spent its time across services and calls.
- **C:** Incorrect for this question. Recommender reports idle and over-provisioned resources with the estimated saving. Why the correct answer wins: Trace shows how one request spent its time across services and calls.
- **D:** Correct. In this case: Trace shows how one request spent its time across services and calls.

### Question 52 — A, B

Answers: Query the entries in Cloud Logging; Group the exceptions in Error Reporting. Logging holds the event text, and Error Reporting clusters the recurring stack traces. Logging holds the event text and structured fields that explain what happened at a moment. Error Reporting clusters recurring stack traces so a new failure is not lost in the log volume. Local study-map skill 4.2 (Root Cause Analysis), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 4 (analyzing and optimizing): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Correct. Logging holds the event text and structured fields that explain what happened at a moment. In this case: Logging holds the event text, and Error Reporting clusters the recurring stack traces.
- **B:** Correct. Error Reporting clusters recurring stack traces so a new failure is not lost in the log volume. In this case: Logging holds the event text, and Error Reporting clusters the recurring stack traces.
- **C:** Incorrect for this question. An SLO ties the alert to the promise the users care about rather than to a raw resource threshold. Why the correct answer wins: Logging holds the event text, and Error Reporting clusters the recurring stack traces.
- **D:** Incorrect for this question. The runbook records the diagnostic steps so the response does not depend on who is awake. Why the correct answer wins: Logging holds the event text, and Error Reporting clusters the recurring stack traces.
- **E:** Incorrect for this question. The dashboard gives the team one view of the same signals during an incident. Why the correct answer wins: Logging holds the event text, and Error Reporting clusters the recurring stack traces.

### Question 53 — A

Answer: Detect the symptom through an alert → contain the impact and restore service → isolate the root cause from logs, traces, and metrics → apply the permanent fix and write the postmortem. Service recovery comes before deep analysis, and the postmortem follows the fix. Local study-map skill 4.2 (Root Cause Analysis), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 4 (analyzing and optimizing): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Correct. In this case: Service recovery comes before deep analysis, and the postmortem follows the fix.
- **B:** Incorrect for this question. Detection precedes analysis, and the postmortem follows restoration rather than preceding it. Why the correct answer wins: Service recovery comes before deep analysis, and the postmortem follows the fix.
- **C:** Incorrect for this question. A postmortem cannot be written before the incident has happened and been resolved. Why the correct answer wins: Service recovery comes before deep analysis, and the postmortem follows the fix.
- **D:** Incorrect for this question. Service cannot be restored before the alert fires, and the root cause is isolated before the postmortem. Why the correct answer wins: Service recovery comes before deep analysis, and the postmortem follows the fix.

### Question 54 — A

Answer: Cover the change with unit, integration, and a few end-to-end tests. The pyramid puts volume where it is cheap and keeps end-to-end tests for the critical paths. Local study-map skill 4.3 (Testing and Validation), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 4 (analyzing and optimizing): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Correct. In this case: The pyramid puts volume where it is cheap and keeps end-to-end tests for the critical paths.
- **B:** Incorrect for this question. The load test measures the system at the concurrency the business expects, before launch. Why the correct answer wins: The pyramid puts volume where it is cheap and keeps end-to-end tests for the critical paths.
- **C:** Incorrect for this question. The experiment proves the failover path works while the impact is controlled. Why the correct answer wins: The pyramid puts volume where it is cheap and keeps end-to-end tests for the critical paths.
- **D:** Incorrect for this question. An independent test attempts the attack the design claims to prevent. Why the correct answer wins: The pyramid puts volume where it is cheap and keeps end-to-end tests for the critical paths.

### Question 55 — D

Answer: Run the emulator in the pipeline. The emulator provides a local endpoint for tests without a billable cloud resource. Local study-map skill 4.3 (Testing and Validation), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 4 (analyzing and optimizing): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. Cloud Shell provides an authenticated terminal and editor with no local installation. Why the correct answer wins: The emulator provides a local endpoint for tests without a billable cloud resource.
- **B:** Incorrect for this question. The CLI exposes every API as a command that can be scripted and logged. Why the correct answer wins: The emulator provides a local endpoint for tests without a billable cloud resource.
- **C:** Incorrect for this question. The bq tool runs jobs and manages datasets from a terminal or a script. Why the correct answer wins: The emulator provides a local endpoint for tests without a billable cloud resource.
- **D:** Correct. In this case: The emulator provides a local endpoint for tests without a billable cloud resource.

### Question 56 — A

Answer: Act on the Recommender suggestions. Recommender reports idle and over-provisioned resources with the estimated saving for each. Local study-map skill 4.5 (Cost Optimization), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 4 (analyzing and optimizing): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Correct. In this case: Recommender reports idle and over-provisioned resources with the estimated saving for each.
- **B:** Incorrect for this question. A budget alerts on spend but does not stop it. Why the correct answer wins: Recommender reports idle and over-provisioned resources with the estimated saving for each.
- **C:** Incorrect for this question. The export attributes cost to the team and service that caused it. Why the correct answer wins: Recommender reports idle and over-provisioned resources with the estimated saving for each.
- **D:** Incorrect for this question. Labels attribute spend in billing export; they do not grant or restrict access. Why the correct answer wins: Recommender reports idle and over-provisioned resources with the estimated saving for each.

### Question 57 — A

Answer: Export billing to BigQuery and review it per label. The export attributes spend to the labels and projects that caused it. The export attributes cost to the team and service that caused it. Local study-map skill 4.5 (Cost Optimization), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 4 (analyzing and optimizing): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Correct. The export attributes cost to the team and service that caused it. In this case: The export attributes spend to the labels and projects that caused it.
- **B:** Incorrect for this question. A budget alerts on spend but does not stop it. Why the correct answer wins: The export attributes spend to the labels and projects that caused it.
- **C:** Incorrect for this question. Labels attribute spend in billing export; they do not grant or restrict access. Why the correct answer wins: The export attributes spend to the labels and projects that caused it.
- **D:** Incorrect for this question. Showing owners their own spend changes behaviour more reliably than a central report. Why the correct answer wins: The export attributes spend to the labels and projects that caused it.

### Question 58 — D

Answer: Inspect the query plan and bytes processed → partition and cluster the table on the filter columns → rewrite the query to prune partitions → measure the new slot time and bytes scanned. The plan identifies the problem, the physical design supports pruning, and only a measurement proves improvement. Local study-map skill 4.5 (Cost Optimization), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 4 (analyzing and optimizing): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. Measuring before any change establishes no baseline against the plan. Why the correct answer wins: The plan identifies the problem, the physical design supports pruning, and only a measurement proves improvement.
- **B:** Incorrect for this question. The plan is the evidence that drives both the rewrite and the physical design. Why the correct answer wins: The plan identifies the problem, the physical design supports pruning, and only a measurement proves improvement.
- **C:** Incorrect for this question. Partitioning last ignores what the plan and the rewrite revealed. Why the correct answer wins: The plan identifies the problem, the physical design supports pruning, and only a measurement proves improvement.
- **D:** Correct. In this case: The plan identifies the problem, the physical design supports pruning, and only a measurement proves improvement.

### Question 59 — C

Answer: Route the change through a change advisory board. The board reviews risk and timing for changes that affect regulated or shared systems. Local study-map skill 4.6 (Stakeholder and Change Management), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 4 (analyzing and optimizing): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. A catalog entry gives teams a pre-approved, policy-compliant way to request the resource. Why the correct answer wins: The board reviews risk and timing for changes that affect regulated or shared systems.
- **B:** Incorrect for this question. A named rotation turns an alert into a person who is already accountable for it. Why the correct answer wins: The board reviews risk and timing for changes that affect regulated or shared systems.
- **C:** Correct. In this case: The board reviews risk and timing for changes that affect regulated or shared systems.
- **D:** Incorrect for this question. The runbook records the diagnostic steps so the response does not depend on who is awake. Why the correct answer wins: The board reviews risk and timing for changes that affect regulated or shared systems.

### Question 60 — B

Answer: Publish a service catalog entry with an approved template. A catalog entry gives teams a pre-approved, policy-compliant way to request the resource. Local study-map skill 4.7 (Service Catalog and Provisioning), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 4 (analyzing and optimizing): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. Terraform holds desired state in code, plans the diff, and applies it through a provider. Why the correct answer wins: A catalog entry gives teams a pre-approved, policy-compliant way to request the resource.
- **B:** Correct. In this case: A catalog entry gives teams a pre-approved, policy-compliant way to request the resource.
- **C:** Incorrect for this question. Labels attribute spend in billing export; they do not grant or restrict access. Why the correct answer wins: A catalog entry gives teams a pre-approved, policy-compliant way to request the resource.
- **D:** Incorrect for this question. An organization policy blocks the action across every project regardless of who holds the role. Why the correct answer wins: A catalog entry gives teams a pre-approved, policy-compliant way to request the resource.

### Question 61 — C

Answer: Roll out a canary to a small share of traffic. A canary limits the blast radius while the error and latency signals are compared. Local study-map skill 5.1 (Deployment and Release Strategy), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 5 (managing implementation): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. The flag separates deployment from release, so the code can ship dark and be turned off instantly. Why the correct answer wins: A canary limits the blast radius while the error and latency signals are compared.
- **B:** Incorrect for this question. Two identical environments let the switch be reversed instantly if the new one misbehaves. Why the correct answer wins: A canary limits the blast radius while the error and latency signals are compared.
- **C:** Correct. In this case: A canary limits the blast radius while the error and latency signals are compared.
- **D:** Incorrect for this question. A rolling replacement keeps capacity but exposes the whole fleet before the signal is trusted. Why the correct answer wins: A canary limits the blast radius while the error and latency signals are compared.

### Question 62 — A

Answer: Put the change behind a feature flag. The flag separates deployment from release, so the code can ship dark and be turned off instantly. Local study-map skill 5.1 (Deployment and Release Strategy), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 5 (managing implementation): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Correct. In this case: The flag separates deployment from release, so the code can ship dark and be turned off instantly.
- **B:** Incorrect for this question. Two identical environments let the switch be reversed instantly if the new one misbehaves. Why the correct answer wins: The flag separates deployment from release, so the code can ship dark and be turned off instantly.
- **C:** Incorrect for this question. A canary limits the blast radius while the error and latency signals are compared. Why the correct answer wins: The flag separates deployment from release, so the code can ship dark and be turned off instantly.
- **D:** Incorrect for this question. A rolling replacement keeps capacity but exposes the whole fleet before the signal is trusted. Why the correct answer wins: The flag separates deployment from release, so the code can ship dark and be turned off instantly.

### Question 63 — D, E

Answers: Deploy blue/green with a traffic switch; Keep the previous image digest ready for rollback. Two environments let the switch be reversed instantly, and a pinned digest restores the exact artifact. Two identical environments let the switch be reversed instantly if the new one misbehaves. A pinned digest restores the exact artifact that was known good, not a rebuild of it. Local study-map skill 5.1 (Deployment and Release Strategy), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 5 (managing implementation): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. A budget alerts on spend but does not stop it. Why the correct answer wins: Two environments let the switch be reversed instantly, and a pinned digest restores the exact artifact.
- **B:** Incorrect for this question. Promotion moves one immutable artifact forward, so what was tested is what runs. Why the correct answer wins: Two environments let the switch be reversed instantly, and a pinned digest restores the exact artifact.
- **C:** Incorrect for this question. A rebuild produces a different artifact, so the test result no longer applies to production. Why the correct answer wins: Two environments let the switch be reversed instantly, and a pinned digest restores the exact artifact.
- **D:** Correct. A pinned digest restores the exact artifact that was known good, not a rebuild of it. In this case: Two environments let the switch be reversed instantly, and a pinned digest restores the exact artifact.
- **E:** Correct. Two identical environments let the switch be reversed instantly if the new one misbehaves. In this case: Two environments let the switch be reversed instantly, and a pinned digest restores the exact artifact.

### Question 64 — D

Answer: Publish the API through Apigee. Apigee adds quotas, keys, mediation, and analytics at the gateway for each consumer. Local study-map skill 5.2 (API Management), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 5 (managing implementation): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. Endpoints validates and monitors an API described by an OpenAPI or gRPC spec. Why the correct answer wins: Apigee adds quotas, keys, mediation, and analytics at the gateway for each consumer.
- **B:** Incorrect for this question. Cloud Armor filters requests at the edge with allow and deny rules and adaptive protection. Why the correct answer wins: Apigee adds quotas, keys, mediation, and analytics at the gateway for each consumer.
- **C:** Incorrect for this question. API Gateway fronts a Cloud Run or functions backend with a managed OpenAPI definition. Why the correct answer wins: Apigee adds quotas, keys, mediation, and analytics at the gateway for each consumer.
- **D:** Correct. In this case: Apigee adds quotas, keys, mediation, and analytics at the gateway for each consumer.

### Question 65 — A

Answer: Use API Gateway. API Gateway fronts a Cloud Run or functions backend with a managed OpenAPI definition. Local study-map skill 5.2 (API Management), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 5 (managing implementation): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Correct. In this case: API Gateway fronts a Cloud Run or functions backend with a managed OpenAPI definition.
- **B:** Incorrect for this question. Endpoints validates and monitors an API described by an OpenAPI or gRPC spec. Why the correct answer wins: API Gateway fronts a Cloud Run or functions backend with a managed OpenAPI definition.
- **C:** Incorrect for this question. Cloud Armor filters requests at the edge with allow and deny rules and adaptive protection. Why the correct answer wins: API Gateway fronts a Cloud Run or functions backend with a managed OpenAPI definition.
- **D:** Incorrect for this question. Apigee adds quotas, keys, mediation, and analytics at the gateway. Why the correct answer wins: API Gateway fronts a Cloud Run or functions backend with a managed OpenAPI definition.

### Question 66 — A

Answer: Migrate the database with Database Migration Service. The service replicates continuously and cuts over in a short window with the source still running. Local study-map skill 5.3 (Data and System Migration Tooling), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 5 (managing implementation): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Correct. In this case: The service replicates continuously and cuts over in a short window with the source still running.
- **B:** Incorrect for this question. The service moves object data between buckets or clouds on a schedule. Why the correct answer wins: The service replicates continuously and cuts over in a short window with the source still running.
- **C:** Incorrect for this question. Datastream reads the source log and streams inserts, updates, and deletes with ordering preserved. Why the correct answer wins: The service replicates continuously and cuts over in a short window with the source still running.
- **D:** Incorrect for this question. The service runs scheduled loads from SaaS sources and other clouds into BigQuery. Why the correct answer wins: The service replicates continuously and cuts over in a short window with the source still running.

### Question 67 — C

Answer: Convert the VMs with Migrate to Containers. The tool rewrites a VM workload into a container image so it can run on GKE. Local study-map skill 5.3 (Data and System Migration Tooling), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 5 (managing implementation): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. The service moves object data between buckets or clouds on a schedule. Why the correct answer wins: The tool rewrites a VM workload into a container image so it can run on GKE.
- **B:** Incorrect for this question. Migration Center inventories the servers and estimates the target size and cost. Why the correct answer wins: The tool rewrites a VM workload into a container image so it can run on GKE.
- **C:** Correct. In this case: The tool rewrites a VM workload into a container image so it can run on GKE.
- **D:** Incorrect for this question. VMware Engine keeps the existing hypervisor and operations model while moving the hardware into Google Cloud. Why the correct answer wins: The tool rewrites a VM workload into a container image so it can run on GKE.

### Question 68 — A

Answer: Inventory the estate in Migration Center → group servers into dependency-based waves → validate a pilot wave in the target landing zone → cut over wave by wave and decommission the source. Inventory precedes grouping, a pilot proves the landing zone, and decommissioning follows a completed cutover. Local study-map skill 5.3 (Data and System Migration Tooling), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 5 (managing implementation): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Correct. In this case: Inventory precedes grouping, a pilot proves the landing zone, and decommissioning follows a completed cutover.
- **B:** Incorrect for this question. Decommissioning first removes the evidence and the rollback option for every later step. Why the correct answer wins: Inventory precedes grouping, a pilot proves the landing zone, and decommissioning follows a completed cutover.
- **C:** Incorrect for this question. A pilot cannot be chosen before the inventory and the wave grouping. Why the correct answer wins: Inventory precedes grouping, a pilot proves the landing zone, and decommissioning follows a completed cutover.
- **D:** Incorrect for this question. Waves cannot be grouped before the inventory, and decommissioning before validation destroys the rollback path. Why the correct answer wins: Inventory precedes grouping, a pilot proves the landing zone, and decommissioning follows a completed cutover.

### Question 69 — B

Answer: Manage the resources with Terraform. Terraform holds the desired state and produces a plan that a reviewer can read before apply. Terraform holds desired state in code, plans the diff, and applies it through a provider. Local study-map skill 5.4 (Programmatic Access and Emulators), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 5 (managing implementation): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. The CLI exposes every API as a command that can be scripted and logged. Why the correct answer wins: Terraform holds the desired state and produces a plan that a reviewer can read before apply.
- **B:** Correct. Terraform holds desired state in code, plans the diff, and applies it through a provider. In this case: Terraform holds the desired state and produces a plan that a reviewer can read before apply.
- **C:** Incorrect for this question. Config Connector reconciles Google Cloud resources from Kubernetes manifests alongside the workloads. Why the correct answer wins: Terraform holds the desired state and produces a plan that a reviewer can read before apply.
- **D:** Incorrect for this question. Deployment Manager is the native but older templating service with no plan step. Why the correct answer wins: Terraform holds the desired state and produces a plan that a reviewer can read before apply.

### Question 70 — D

Answer: Run the build in Cloud Build. Cloud Build executes the pipeline steps in a managed, isolated worker with recorded provenance. Local study-map skill 5.4 (Programmatic Access and Emulators), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 5 (managing implementation): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. Cloud Code gives the editor run, debug, and deploy targets for the cluster without leaving it. Why the correct answer wins: Cloud Build executes the pipeline steps in a managed, isolated worker with recorded provenance.
- **B:** Incorrect for this question. The CLI exposes every API as a command that can be scripted and logged. Why the correct answer wins: Cloud Build executes the pipeline steps in a managed, isolated worker with recorded provenance.
- **C:** Incorrect for this question. Cloud Shell provides an authenticated terminal and editor with no local installation. Why the correct answer wins: Cloud Build executes the pipeline steps in a managed, isolated worker with recorded provenance.
- **D:** Correct. In this case: Cloud Build executes the pipeline steps in a managed, isolated worker with recorded provenance.

### Question 71 — D

Answer: Use the Google API client library with retries. The client library applies the recommended retry and backoff behaviour for the API. Local study-map skill 5.5 (Client Libraries and API Practices), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 5 (managing implementation): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. The CLI exposes every API as a command that can be scripted and logged. Why the correct answer wins: The client library applies the recommended retry and backoff behaviour for the API.
- **B:** Incorrect for this question. An API key identifies a project and does not authorise a user, so it cannot express least privilege. Why the correct answer wins: The client library applies the recommended retry and backoff behaviour for the API.
- **C:** Incorrect for this question. Impersonation issues a short-lived token so the test runs as the real workload identity. Why the correct answer wins: The client library applies the recommended retry and backoff behaviour for the API.
- **D:** Correct. In this case: The client library applies the recommended retry and backoff behaviour for the API.

### Question 72 — B

Answer: Install the Ops Agent on the instances. The Ops Agent ships host metrics and application logs to Monitoring and Logging. Local study-map skill 6.1 (Observability Design), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 6 (solution and operations excellence): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. Error Reporting clusters recurring stack traces so a new failure is not lost in the log volume. Why the correct answer wins: The Ops Agent ships host metrics and application logs to Monitoring and Logging.
- **B:** Correct. In this case: The Ops Agent ships host metrics and application logs to Monitoring and Logging.
- **C:** Incorrect for this question. Trace shows how one request spent its time across services and calls. Why the correct answer wins: The Ops Agent ships host metrics and application logs to Monitoring and Logging.
- **D:** Incorrect for this question. Profiler samples the running code and attributes CPU and heap to the functions responsible. Why the correct answer wins: The Ops Agent ships host metrics and application logs to Monitoring and Logging.

### Question 73 — D, E

Answers: Add an uptime check from several regions; Inspect the trace waterfall in Cloud Trace. The uptime check measures availability externally, and the trace shows where the request spent its time. The check measures availability from outside, which no internal metric can prove. Trace shows how one request spent its time across services and calls. Local study-map skill 6.1 (Observability Design), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 6 (solution and operations excellence): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. The dashboard gives the team one view of the same signals during an incident. Why the correct answer wins: The uptime check measures availability externally, and the trace shows where the request spent its time.
- **B:** Incorrect for this question. Recommender reports idle and over-provisioned resources with the estimated saving. Why the correct answer wins: The uptime check measures availability externally, and the trace shows where the request spent its time.
- **C:** Incorrect for this question. An SLO ties the alert to the promise the users care about rather than to a raw resource threshold. Why the correct answer wins: The uptime check measures availability externally, and the trace shows where the request spent its time.
- **D:** Correct. Trace shows how one request spent its time across services and calls. In this case: The uptime check measures availability externally, and the trace shows where the request spent its time.
- **E:** Correct. The check measures availability from outside, which no internal metric can prove. In this case: The uptime check measures availability externally, and the trace shows where the request spent its time.

### Question 74 — C

Answer: Define an SLO with an error budget. An SLO ties the alert to the user promise rather than to a raw resource threshold. Local study-map skill 6.2 (Alerting and Service Level Objectives), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 6 (solution and operations excellence): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. The policy fires when the series crosses the condition for the stated duration. Why the correct answer wins: An SLO ties the alert to the user promise rather than to a raw resource threshold.
- **B:** Incorrect for this question. The dashboard gives the team one view of the same signals during an incident. Why the correct answer wins: An SLO ties the alert to the user promise rather than to a raw resource threshold.
- **C:** Correct. In this case: An SLO ties the alert to the user promise rather than to a raw resource threshold.
- **D:** Incorrect for this question. The check measures availability from outside, which no internal metric can prove. Why the correct answer wins: An SLO ties the alert to the user promise rather than to a raw resource threshold.

### Question 75 — C

Answer: Create a log-based metric. The metric turns a log pattern into a series that can be alerted on and charted. Local study-map skill 6.2 (Alerting and Service Level Objectives), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 6 (solution and operations excellence): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. The policy fires when the series crosses the condition for the stated duration. Why the correct answer wins: The metric turns a log pattern into a series that can be alerted on and charted.
- **B:** Incorrect for this question. An SLO ties the alert to the promise the users care about rather than to a raw resource threshold. Why the correct answer wins: The metric turns a log pattern into a series that can be alerted on and charted.
- **C:** Correct. In this case: The metric turns a log pattern into a series that can be alerted on and charted.
- **D:** Incorrect for this question. The dashboard gives the team one view of the same signals during an incident. Why the correct answer wins: The metric turns a log pattern into a series that can be alerted on and charted.

### Question 76 — C

Answer: Publish a runbook per alert. The runbook records the diagnostic steps so the response does not depend on who is awake. Local study-map skill 6.3 (Release Management and Support), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 6 (solution and operations excellence): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. The support tier sets the response time and the escalation path the business expects. Why the correct answer wins: The runbook records the diagnostic steps so the response does not depend on who is awake.
- **B:** Incorrect for this question. The dashboard gives the team one view of the same signals during an incident. Why the correct answer wins: The runbook records the diagnostic steps so the response does not depend on who is awake.
- **C:** Correct. In this case: The runbook records the diagnostic steps so the response does not depend on who is awake.
- **D:** Incorrect for this question. A named rotation turns an alert into a person who is already accountable for it. Why the correct answer wins: The runbook records the diagnostic steps so the response does not depend on who is awake.

### Question 77 — B

Answer: Define an on-call rotation with an escalation path. A named rotation turns an alert into a person who is already accountable for it. Local study-map skill 6.3 (Release Management and Support), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 6 (solution and operations excellence): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. The runbook records the diagnostic steps so the response does not depend on who is awake. Why the correct answer wins: A named rotation turns an alert into a person who is already accountable for it.
- **B:** Correct. In this case: A named rotation turns an alert into a person who is already accountable for it.
- **C:** Incorrect for this question. The contract converts an internal target into an obligation with a consequence. Why the correct answer wins: A named rotation turns an alert into a person who is already accountable for it.
- **D:** Incorrect for this question. The support tier sets the response time and the escalation path the business expects. Why the correct answer wins: A named rotation turns an alert into a person who is already accountable for it.

### Question 78 — D

Answer: Run a chaos experiment against a zone. The experiment proves the failover path works while the impact is controlled. Local study-map skill 6.4 (Reliability Testing), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 6 (solution and operations excellence): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. A canary limits the blast radius while the error and latency signals are compared. Why the correct answer wins: The experiment proves the failover path works while the impact is controlled.
- **B:** Incorrect for this question. An independent test attempts the attack the design claims to prevent. Why the correct answer wins: The experiment proves the failover path works while the impact is controlled.
- **C:** Incorrect for this question. The load test measures the system at the concurrency the business expects, before launch. Why the correct answer wins: The experiment proves the failover path works while the impact is controlled.
- **D:** Correct. In this case: The experiment proves the failover path works while the impact is controlled.

### Question 79 — B

Answer: Write a blameless postmortem with actions. The postmortem records cause and follow-up work, which is how the same failure is prevented. Local study-map skill 6.5 (Operational Excellence and Quality Control), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 6 (solution and operations excellence): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. The dashboard gives the team one view of the same signals during an incident. Why the correct answer wins: The postmortem records cause and follow-up work, which is how the same failure is prevented.
- **B:** Correct. In this case: The postmortem records cause and follow-up work, which is how the same failure is prevented.
- **C:** Incorrect for this question. The runbook records the diagnostic steps so the response does not depend on who is awake. Why the correct answer wins: The postmortem records cause and follow-up work, which is how the same failure is prevented.
- **D:** Incorrect for this question. The support tier sets the response time and the escalation path the business expects. Why the correct answer wins: The postmortem records cause and follow-up work, which is how the same failure is prevented.

### Question 80 — A

Answer: Build an immutable image and record its digest → deploy the new revision without traffic → shift a small traffic percentage and watch error and latency signals → promote to full traffic or roll back to the pinned digest. The artifact is fixed before traffic moves, and the decision to promote follows observed signals. Local study-map skill 6.5 (Operational Excellence and Quality Control), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 6 (solution and operations excellence): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Correct. In this case: The artifact is fixed before traffic moves, and the decision to promote follows observed signals.
- **B:** Incorrect for this question. Full traffic before any canary step turns the first failure into an outage. Why the correct answer wins: The artifact is fixed before traffic moves, and the decision to promote follows observed signals.
- **C:** Incorrect for this question. Promoting before the canary step skips the signal that justifies promotion. Why the correct answer wins: The artifact is fixed before traffic moves, and the decision to promote follows observed signals.
- **D:** Incorrect for this question. Nothing can be watched before the revision exists, and the image precedes the deployment. Why the correct answer wins: The artifact is fixed before traffic moves, and the decision to promote follows observed signals.

### Question 81 — B

Answer: Use Spanner. Spanner gives strongly consistent reads and writes across regions with a 99.999% multi-region target. Local study-map skill 1.3 (High Availability and Failover Design), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 1 (designing and planning): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. Cloud SQL is a managed MySQL, PostgreSQL, or SQL Server instance with a familiar connection model. Why the correct answer wins: Spanner gives strongly consistent reads and writes across regions with a 99.999% multi-region target.
- **B:** Correct. In this case: Spanner gives strongly consistent reads and writes across regions with a 99.999% multi-region target.
- **C:** Incorrect for this question. Bigtable is a wide-column store for high-throughput key reads and writes at low latency. Why the correct answer wins: Spanner gives strongly consistent reads and writes across regions with a 99.999% multi-region target.
- **D:** Incorrect for this question. Firestore is a document store with real-time listeners and per-document transactions. Why the correct answer wins: Spanner gives strongly consistent reads and writes across regions with a 99.999% multi-region target.

### Question 82 — A

Answer: Use Dataflow. A streaming Beam pipeline applies the rule per event instead of waiting for a nightly batch. Dataflow runs an Apache Beam pipeline with autoscaling and a single programming model for batch and streaming. Local study-map skill 1.7 (Data Processing and Analytics Selection), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 1 (designing and planning): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Correct. Dataflow runs an Apache Beam pipeline with autoscaling and a single programming model for batch and streaming. In this case: A streaming Beam pipeline applies the rule per event instead of waiting for a nightly batch.
- **B:** Incorrect for this question. Scheduler fires a job on a cron or App Engine schedule and retries on failure. Why the correct answer wins: A streaming Beam pipeline applies the rule per event instead of waiting for a nightly batch.
- **C:** Incorrect for this question. A Dataproc cluster runs open-source Spark and Hadoop with jobs that need a persistent cluster. Why the correct answer wins: A streaming Beam pipeline applies the rule per event instead of waiting for a nightly batch.
- **D:** Incorrect for this question. Airflow expresses dependencies between scheduled jobs and retries a failed task without rerunning the rest. Why the correct answer wins: A streaming Beam pipeline applies the rule per event instead of waiting for a nightly batch.

### Question 83 — D

Answer: Enable Data Access audit logs. Data Access logging is off by default and must be enabled before reads and writes are recorded. Local study-map skill 3.8 (Compliance, Residency, and Audit Logging), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 3 (security and compliance): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. Admin Activity records configuration changes and cannot be disabled. Why the correct answer wins: Data Access logging is off by default and must be enabled before reads and writes are recorded.
- **B:** Incorrect for this question. The metric turns a log pattern into a series that can be alerted on and charted. Why the correct answer wins: Data Access logging is off by default and must be enabled before reads and writes are recorded.
- **C:** Incorrect for this question. Access Transparency records when Google staff access your content, which is evidence of oversight, not of user activity. Why the correct answer wins: Data Access logging is off by default and must be enabled before reads and writes are recorded.
- **D:** Correct. In this case: Data Access logging is off by default and must be enabled before reads and writes are recorded.

### Question 84 — C

Answer: Run a load test at the expected peak. The load test measures the system at the concurrency the business expects, before the peak. Local study-map skill 4.3 (Testing and Validation), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 4 (analyzing and optimizing): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. The pyramid puts volume where it is cheap and keeps end-to-end tests for the critical paths. Why the correct answer wins: The load test measures the system at the concurrency the business expects, before the peak.
- **B:** Incorrect for this question. The experiment proves the failover path works while the impact is controlled. Why the correct answer wins: The load test measures the system at the concurrency the business expects, before the peak.
- **C:** Correct. In this case: The load test measures the system at the concurrency the business expects, before the peak.
- **D:** Incorrect for this question. An independent test attempts the attack the design claims to prevent. Why the correct answer wins: The load test measures the system at the concurrency the business expects, before the peak.

### Question 85 — A

Answer: Publish a runbook per alert. The runbook records the diagnostic steps so the response does not depend on who is awake. Local study-map skill 6.3 (Release Management and Support), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 6 (solution and operations excellence): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Correct. In this case: The runbook records the diagnostic steps so the response does not depend on who is awake.
- **B:** Incorrect for this question. A named rotation turns an alert into a person who is already accountable for it. Why the correct answer wins: The runbook records the diagnostic steps so the response does not depend on who is awake.
- **C:** Incorrect for this question. The support tier sets the response time and the escalation path the business expects. Why the correct answer wins: The runbook records the diagnostic steps so the response does not depend on who is awake.
- **D:** Incorrect for this question. The dashboard gives the team one view of the same signals during an incident. Why the correct answer wins: The runbook records the diagnostic steps so the response does not depend on who is awake.

### Question 86 — C

Answer: Deploy the service on Cloud Run. Cloud Run scales to zero per tenant and bills per request, which suits a shared multi-tenant service. Cloud Run runs a stateless container per request and scales to zero when idle. Local study-map skill 1.6 (Compute Platform Selection), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 1 (designing and planning): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. The group replaces unhealthy instances and adds capacity from a template as load rises. Why the correct answer wins: Cloud Run scales to zero per tenant and bills per request, which suits a shared multi-tenant service.
- **B:** Incorrect for this question. Standard exposes node configuration and patching, which the team must then run itself. Why the correct answer wins: Cloud Run scales to zero per tenant and bills per request, which suits a shared multi-tenant service.
- **C:** Correct. Cloud Run runs a stateless container per request and scales to zero when idle. In this case: Cloud Run scales to zero per tenant and bills per request, which suits a shared multi-tenant service.
- **D:** Incorrect for this question. VMware Engine keeps the existing hypervisor and operations model while moving the hardware into Google Cloud. Why the correct answer wins: Cloud Run scales to zero per tenant and bills per request, which suits a shared multi-tenant service.

### Question 87 — B

Answer: Keep the data in the region the regulator requires. Residency fixes where storage and processing may happen, which then constrains every service choice. Local study-map skill 1.2 (Non-Functional Requirements and Trade-offs), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 1 (designing and planning): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. A measured baseline and a named owner make the outcome testable after the migration. Why the correct answer wins: Residency fixes where storage and processing may happen, which then constrains every service choice.
- **B:** Correct. In this case: Residency fixes where storage and processing may happen, which then constrains every service choice.
- **C:** Incorrect for this question. The exit plan keeps the migration reversible and constrains how proprietary the design may become. Why the correct answer wins: Residency fixes where storage and processing may happen, which then constrains every service choice.
- **D:** Incorrect for this question. The model compares run cost, people cost, and exit cost rather than the monthly bill alone. Why the correct answer wins: Residency fixes where storage and processing may happen, which then constrains every service choice.

### Question 88 — D

Answer: Manage the resources with Terraform. Terraform holds the desired state and produces a plan that a reviewer can read before apply. Terraform holds desired state in code, plans the diff, and applies it through a provider. Local study-map skill 2.6 (Infrastructure as Code), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 2 (managing and provisioning): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. Config Connector reconciles Google Cloud resources from Kubernetes manifests alongside the workloads. Why the correct answer wins: Terraform holds the desired state and produces a plan that a reviewer can read before apply.
- **B:** Incorrect for this question. The CLI exposes every API as a command that can be scripted and logged. Why the correct answer wins: Terraform holds the desired state and produces a plan that a reviewer can read before apply.
- **C:** Incorrect for this question. Deployment Manager is the native but older templating service with no plan step. Why the correct answer wins: Terraform holds the desired state and produces a plan that a reviewer can read before apply.
- **D:** Correct. Terraform holds desired state in code, plans the diff, and applies it through a provider. In this case: Terraform holds the desired state and produces a plan that a reviewer can read before apply.

### Question 89 — A

Answer: Publish the service through Private Service Connect. A PSC endpoint gives a private IP in the consumer VPC without peering or exposing the service publicly. Local study-map skill 3.4 (VPC Service Controls and Network Security), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 3 (security and compliance): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Correct. In this case: A PSC endpoint gives a private IP in the consumer VPC without peering or exposing the service publicly.
- **B:** Incorrect for this question. DNS peering resolves names across networks without transferring zone ownership. Why the correct answer wins: A PSC endpoint gives a private IP in the consumer VPC without peering or exposing the service publicly.
- **C:** Incorrect for this question. Private Google Access reaches Google APIs from an internal address without a proxy or a NAT gateway. Why the correct answer wins: A PSC endpoint gives a private IP in the consumer VPC without peering or exposing the service publicly.
- **D:** Incorrect for this question. Cloud NAT lets private instances reach the internet without an external address. Why the correct answer wins: A PSC endpoint gives a private IP in the consumer VPC without peering or exposing the service publicly.

### Question 90 — B

Answer: Define an SLO with an error budget. An SLO ties the alert to the user promise rather than to a raw resource threshold. Local study-map skill 6.2 (Alerting and Service Level Objectives), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 6 (solution and operations excellence): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. The policy fires when the series crosses the condition for the stated duration. Why the correct answer wins: An SLO ties the alert to the user promise rather than to a raw resource threshold.
- **B:** Correct. In this case: An SLO ties the alert to the user promise rather than to a raw resource threshold.
- **C:** Incorrect for this question. The dashboard gives the team one view of the same signals during an incident. Why the correct answer wins: An SLO ties the alert to the user promise rather than to a raw resource threshold.
- **D:** Incorrect for this question. The check measures availability from outside, which no internal metric can prove. Why the correct answer wins: An SLO ties the alert to the user promise rather than to a raw resource threshold.

### Question 91 — D

Answer: Assess the estate in Migration Center. Migration Center inventories the estate and estimates target size and cost before the design is fixed. Migration Center inventories the servers and estimates the target size and cost. Local study-map skill 1.9 (Migration Planning and Future Improvement), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 1 (designing and planning): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. The service moves a database with continuous replication and a short cutover window. Why the correct answer wins: Migration Center inventories the estate and estimates target size and cost before the design is fixed.
- **B:** Incorrect for this question. The service moves object data between buckets or clouds on a schedule. Why the correct answer wins: Migration Center inventories the estate and estimates target size and cost before the design is fixed.
- **C:** Incorrect for this question. The tool rewrites a VM workload into a container image so it can run on GKE. Why the correct answer wins: Migration Center inventories the estate and estimates target size and cost before the design is fixed.
- **D:** Correct. Migration Center inventories the servers and estimates the target size and cost. In this case: Migration Center inventories the estate and estimates target size and cost before the design is fixed.

### Question 92 — C

Answer: Use VM Manager for OS patch compliance. VM Manager inventories and applies patches across the fleet instead of relying on manual runs. Local study-map skill 2.3 (Compute Provisioning and Patch Management), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 2 (managing and provisioning): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. Custom vCPU and memory avoid paying for a fixed shape that over-provisions one dimension. Why the correct answer wins: VM Manager inventories and applies patches across the fleet instead of relying on manual runs.
- **B:** Incorrect for this question. Spot capacity costs far less but can be reclaimed with 30 seconds of notice. Why the correct answer wins: VM Manager inventories and applies patches across the fleet instead of relying on manual runs.
- **C:** Correct. In this case: VM Manager inventories and applies patches across the fleet instead of relying on manual runs.
- **D:** Incorrect for this question. Config Connector reconciles Google Cloud resources from Kubernetes manifests alongside the workloads. Why the correct answer wins: VM Manager inventories and applies patches across the fleet instead of relying on manual runs.

### Question 93 — C

Answer: Query the entries in Cloud Logging. Logging holds the event text and structured fields that explain what happened at that moment. Local study-map skill 4.2 (Root Cause Analysis), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 4 (analyzing and optimizing): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. The dashboard gives the team one view of the same signals during an incident. Why the correct answer wins: Logging holds the event text and structured fields that explain what happened at that moment.
- **B:** Incorrect for this question. Recommender reports idle and over-provisioned resources with the estimated saving. Why the correct answer wins: Logging holds the event text and structured fields that explain what happened at that moment.
- **C:** Correct. In this case: Logging holds the event text and structured fields that explain what happened at that moment.
- **D:** Incorrect for this question. The check measures availability from outside, which no internal metric can prove. Why the correct answer wins: Logging holds the event text and structured fields that explain what happened at that moment.

### Question 94 — B

Answer: Manage the resources with Terraform. Terraform holds the desired state and produces a plan that a reviewer can read before apply. Terraform holds desired state in code, plans the diff, and applies it through a provider. Local study-map skill 5.4 (Programmatic Access and Emulators), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 5 (managing implementation): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. The CLI exposes every API as a command that can be scripted and logged. Why the correct answer wins: Terraform holds the desired state and produces a plan that a reviewer can read before apply.
- **B:** Correct. Terraform holds desired state in code, plans the diff, and applies it through a provider. In this case: Terraform holds the desired state and produces a plan that a reviewer can read before apply.
- **C:** Incorrect for this question. Deployment Manager is the native but older templating service with no plan step. Why the correct answer wins: Terraform holds the desired state and produces a plan that a reviewer can read before apply.
- **D:** Incorrect for this question. Config Connector reconciles Google Cloud resources from Kubernetes manifests alongside the workloads. Why the correct answer wins: Terraform holds the desired state and produces a plan that a reviewer can read before apply.

### Question 95 — A

Answer: Define dashboards and metrics in Cloud Monitoring. Monitoring collects the platform metrics that the first alert and the local display will use. Local study-map skill 6.1 (Observability Design), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 6 (solution and operations excellence): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Correct. In this case: Monitoring collects the platform metrics that the first alert and the local display will use.
- **B:** Incorrect for this question. Recommender reports idle and over-provisioned resources with the estimated saving. Why the correct answer wins: Monitoring collects the platform metrics that the first alert and the local display will use.
- **C:** Incorrect for this question. The dashboard gives the team one view of the same signals during an incident. Why the correct answer wins: Monitoring collects the platform metrics that the first alert and the local display will use.
- **D:** Incorrect for this question. Trace shows how one request spent its time across services and calls. Why the correct answer wins: Monitoring collects the platform metrics that the first alert and the local display will use.

### Question 96 — B

Answer: Enforce the control with an organization policy constraint. An organization policy blocks the action across every project regardless of who holds the role. Local study-map skill 3.2 (Resource Hierarchy and Organization Policy), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 3 (security and compliance): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. Labels attribute spend in billing export; they do not grant or restrict access. Why the correct answer wins: An organization policy blocks the action across every project regardless of who holds the role.
- **B:** Correct. In this case: An organization policy blocks the action across every project regardless of who holds the role.
- **C:** Incorrect for this question. A project is the boundary for quota, billing, and most IAM inheritance. Why the correct answer wins: An organization policy blocks the action across every project regardless of who holds the role.
- **D:** Incorrect for this question. A folder binding inherits to every project beneath it, so new projects start with the right access. Why the correct answer wins: An organization policy blocks the action across every project regardless of who holds the role.

### Question 97 — B, D

Answers: Use Shared VPC with host and service projects; Create a separate project per environment. The host project owns the subnets, and each subsidiary keeps its own project boundary. One host project owns the subnets and firewall rules while each team keeps its own service project. A project is the boundary for quota, billing, and most IAM inheritance. Local study-map skill 2.1 (Hybrid and Multicloud Connectivity), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 2 (managing and provisioning): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. Cloud NAT lets private instances reach the internet without an external address. Why the correct answer wins: The host project owns the subnets, and each subsidiary keeps its own project boundary.
- **B:** Correct. A project is the boundary for quota, billing, and most IAM inheritance. In this case: The host project owns the subnets, and each subsidiary keeps its own project boundary.
- **C:** Incorrect for this question. DNS peering resolves names across networks without transferring zone ownership. Why the correct answer wins: The host project owns the subnets, and each subsidiary keeps its own project boundary.
- **D:** Correct. One host project owns the subnets and firewall rules while each team keeps its own service project. In this case: The host project owns the subnets, and each subsidiary keeps its own project boundary.
- **E:** Incorrect for this question. Peering joins two networks at layer three but does not share firewalls or transitive routes. Why the correct answer wins: The host project owns the subnets, and each subsidiary keeps its own project boundary.

### Question 98 — D

Answer: Apply a hierarchical firewall policy at the organization or folder. A policy above the project applies to every current and future network beneath it. Local study-map skill 1.4 (Network Design), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 1 (designing and planning): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. CDN caches responses at edge locations, which cuts origin load and latency for repeat reads. Why the correct answer wins: A policy above the project applies to every current and future network beneath it.
- **B:** Incorrect for this question. Peering joins two networks at layer three but does not share firewalls or transitive routes. Why the correct answer wins: A policy above the project applies to every current and future network beneath it.
- **C:** Incorrect for this question. Cloud NAT lets private instances reach the internet without an external address. Why the correct answer wins: A policy above the project applies to every current and future network beneath it.
- **D:** Correct. In this case: A policy above the project applies to every current and future network beneath it.

### Question 99 — B

Answer: Require a reviewed pull request and a passing plan. The gate makes a second person check the change and its plan before it can apply. Local study-map skill 4.1 (SDLC and CI/CD Design), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 4 (analyzing and optimizing): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. A rolling replacement keeps capacity but exposes the whole fleet before the signal is trusted. Why the correct answer wins: The gate makes a second person check the change and its plan before it can apply.
- **B:** Correct. In this case: The gate makes a second person check the change and its plan before it can apply.
- **C:** Incorrect for this question. Short branches reduce merge conflict and keep the mainline deployable. Why the correct answer wins: The gate makes a second person check the change and its plan before it can apply.
- **D:** Incorrect for this question. A rebuild produces a different artifact, so the test result no longer applies to production. Why the correct answer wins: The gate makes a second person check the change and its plan before it can apply.

### Question 100 — D

Answer: Write a blameless postmortem with actions. The postmortem records cause and follow-up work, which is how the same failure is prevented. Local study-map skill 6.5 (Operational Excellence and Quality Control), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 6 (solution and operations excellence): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. The support tier sets the response time and the escalation path the business expects. Why the correct answer wins: The postmortem records cause and follow-up work, which is how the same failure is prevented.
- **B:** Incorrect for this question. The runbook records the diagnostic steps so the response does not depend on who is awake. Why the correct answer wins: The postmortem records cause and follow-up work, which is how the same failure is prevented.
- **C:** Incorrect for this question. The dashboard gives the team one view of the same signals during an incident. Why the correct answer wins: The postmortem records cause and follow-up work, which is how the same failure is prevented.
- **D:** Correct. In this case: The postmortem records cause and follow-up work, which is how the same failure is prevented.
