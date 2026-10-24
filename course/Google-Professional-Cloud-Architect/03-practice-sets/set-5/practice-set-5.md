# Google Cloud Professional Cloud Architect — Full-Length Mock Exam 5

Professional Cloud Architect · 100 questions · expanded practice bank · passing score not published

Blueprint-weighted mock exam. Item mix: 84 multiple-choice (selection count stated where needed), 16 multi-select, and 4 case studies of 5 questions. 8 of the multiple-choice items ask you to choose the correct candidate sequence. The live exam publishes 50-60 questions and two case studies worth 20-30 per cent of the score; this set is larger on purpose and cannot reproduce the split-screen case-study panel, drag-and-drop ordering, or lab tasks. See the README for the exact fidelity boundary.

Original educational content, not actual, recalled, or copied Google exam items.

## Questions

### 1. A delivery programme reports weekly but nobody agrees what counts as success. What should be fixed first?

Domain: Designing and planning a cloud solution architecture

- A. Build a three-year total cost of ownership model
- B. Define the baseline and target as a KPI with an owner
- C. Export billing to BigQuery and review it per label
- D. Publish a shared dashboard

### 2. Two delivery designs differ in staffing and licence cost. What should be produced to compare them?

Domain: Designing and planning a cloud solution architecture

- A. Buy committed use discounts for the steady baseline
- B. Set a budget with alert thresholds
- C. Build a three-year total cost of ownership model
- D. Export billing to BigQuery and review it per label

### 3. The programme will hand the platform to another supplier in two years. What must the design include?

Domain: Designing and planning a cloud solution architecture

- A. Set a budget with alert thresholds
- B. Build a three-year total cost of ownership model
- C. Tag the resources with labels for cost reporting
- D. Document the exit plan and data portability

### 4. Two countries join the programme and neither will accept processing abroad. What must the design fix?

Domain: Designing and planning a cloud solution architecture

- A. Keep the data in the region the regulator requires
- B. Build a three-year total cost of ownership model
- C. Define the baseline and target as a KPI with an owner
- D. Document the exit plan and data portability

### 5. The business must state the tolerable outage and who answers for it. Which two artefacts settle that? Select two.

Domain: Designing and planning a cloud solution architecture

- A. Publish a shared dashboard
- B. Act on the Recommender suggestions
- C. Put the recovery commitment in the contract
- D. Tag the resources with labels for cost reporting
- E. Set the RPO and RTO with the business owner

### 6. The booking database must survive a zone failure with no operator action. What should be enabled?

Domain: Designing and planning a cloud solution architecture

- A. Add a read replica and route reads to it
- B. Enable Cloud SQL high availability with a standby
- C. Use Memorystore
- D. Use Bigtable

### 7. The payment API must keep serving during a regional loss with no failover decision. Which two pieces are required? Select two.

Domain: Designing and planning a cloud solution architecture

- A. Use backup and restore
- B. Enable Cloud CDN on the backend
- C. Replicate the data to the second region
- D. Run active-active across two regions
- E. Run a pilot-light standby

### 8. Four delivery teams run their own networks and must reach a shared services hub. What should be built?

Domain: Designing and planning a cloud solution architecture

- A. Deploy Cloud NAT for outbound traffic
- B. Peer the two VPC networks
- C. Build a Network Connectivity Center hub
- D. Create a DNS peering zone

### 9. A merchant must reach the payment service privately from its own network. Which two designs allow that? Select two.

Domain: Designing and planning a cloud solution architecture

- A. Publish the service through Private Service Connect
- B. Deploy Cloud NAT for outbound traffic
- C. Peer the two VPC networks
- D. Enable Cloud CDN on the backend
- E. Issue a short-lived signed URL

### 10. A fraud-scoring service needs millions of key lookups per second at millisecond latency. What should be used?

Domain: Designing and planning a cloud solution architecture

- A. Use Cloud SQL
- B. Load the data into BigQuery
- C. Use Firestore
- D. Use Bigtable

### 11. Dispute evidence has unpredictable access and must be deleted after seven years. Which two settings apply? Select two.

Domain: Designing and planning a cloud solution architecture

- A. Enable Autoclass on the bucket
- B. Use local SSD for the scratch space
- C. Store the objects in Nearline storage class
- D. Add a lifecycle rule that transitions and then deletes
- E. Mount a Filestore instance for the shared file path

### 12. The delivery team is four engineers and cannot patch nodes. What should be chosen?

Domain: Designing and planning a cloud solution architecture

- A. Deploy the service on Cloud Run
- B. Use GKE Autopilot
- C. Submit the work as a Batch job
- D. Use GKE Standard with a node pool per workload shape

### 13. A webhook receiver is idle most of the day and must return to zero. What should be used?

Domain: Designing and planning a cloud solution architecture

- A. Use a managed instance group with autoscaling
- B. Run the legacy stack on Google Cloud VMware Engine
- C. Use GKE Standard with a node pool per workload shape
- D. Deploy the service on Cloud Run

### 14. Settlement runs must handle both backfill and late events with one codebase. What should be used?

Domain: Designing and planning a cloud solution architecture

- A. Use a Dataproc cluster
- B. Trigger the job with Cloud Scheduler
- C. Use the BigQuery Data Transfer Service
- D. Use Dataflow

### 15. A payment event must reach several services, and one poison message must not block the queue. Which two features apply? Select two.

Domain: Designing and planning a cloud solution architecture

- A. Queue the work in Cloud Tasks
- B. Attach a dead-letter topic
- C. Route the event with Eventarc
- D. Publish events to Pub/Sub
- E. Trigger the job with Cloud Scheduler

### 16. A fraud model must run with regional processing and audit logging. What should be used?

Domain: Designing and planning a cloud solution architecture

- A. Index the corpus with Vertex AI Search
- B. Call Gemini through Agent Platform
- C. Use Gemini Enterprise for the knowledge assistant
- D. Use the Vision API for the images

### 17. A team must select a model and then serve it with low latency. Which two components apply? Select two.

Domain: Designing and planning a cloud solution architecture

- A. Deploy to an online prediction endpoint
- B. Use Gemini Cloud Assist for the investigation
- C. Build the agent with the Agent Development Kit
- D. Select the model from Model Garden
- E. Model the metrics in Looker

### 18. 1,800 virtual machines must be sized before a nine-month plan is signed. What should be used?

Domain: Designing and planning a cloud solution architecture

- A. Copy the files with Storage Transfer Service
- B. Convert the VMs with Migrate to Containers
- C. Assess the estate in Migration Center
- D. Use Database Migration Service

### 19. A 300 TB archive sits on a site whose uplink would take a year. What should be used?

Domain: Designing and planning a cloud solution architecture

- A. Copy the files with Storage Transfer Service
- B. Use gcloud storage commands
- C. Use Storage Transfer Service for the recurring copy
- D. Use a Transfer Appliance for the one-off bulk move

### 20. A delivery programme must prove the recovery objective it promised. Which sequence is correct?

Domain: Designing and planning a cloud solution architecture

- A. Set the RTO and RPO targets → choose the DR pattern that meets them → build and replicate the standby environment → fail over in a game day and record the result
- B. Fail over in a game day → set the RTO and RPO targets → choose the DR pattern → build the standby environment
- C. Choose the DR pattern → fail over in a game day → set the RTO and RPO targets → build the standby environment
- D. Build and replicate the standby environment → choose the DR pattern → set the RTO and RPO targets → fail over in a game day

### 21. A merchant integration needs a private path that survives one tunnel failing. What should be used?

Domain: Managing and provisioning a solution infrastructure

- A. Deploy Cloud NAT for outbound traffic
- B. Enable Cloud CDN on the backend
- C. Order a Dedicated Interconnect
- D. Use HA VPN with two tunnels

### 22. Private instances must fetch patches from the internet and reach Google APIs without a proxy. Which two settings apply? Select two.

Domain: Managing and provisioning a solution infrastructure

- A. Enable Private Google Access on the subnet
- B. Deploy Cloud NAT for outbound traffic
- C. Attach a Cloud Armor security policy
- D. Enable Cloud CDN on the backend
- E. Put Identity-Aware Proxy in front of the application

### 23. Settlement records must be immutable for the period the regulator specifies. What should be applied?

Domain: Managing and provisioning a solution infrastructure

- A. Add a lifecycle rule that transitions and then deletes
- B. Apply a bucket retention policy with a locked period
- C. Enable object versioning
- D. Enable Autoclass on the bucket

### 24. A settlement fact table is always filtered by date and by merchant. Which two physical design choices apply? Select two.

Domain: Managing and provisioning a solution infrastructure

- A. Build the dashboard in Looker Studio
- B. Cluster the table on the filter columns
- C. Create a materialized view for the repeated aggregate
- D. Partition the table on the date column
- E. Leave the project on on-demand pricing

### 25. Four hundred delivery VMs must be patched on a published schedule. What should be used?

Domain: Managing and provisioning a solution infrastructure

- A. Run the batch tier on Spot VMs
- B. Run the build in Cloud Build
- C. Manage the resources with Config Connector
- D. Use VM Manager for OS patch compliance

### 26. A settlement service needs 128 GB of memory and four vCPUs. What should be used?

Domain: Managing and provisioning a solution infrastructure

- A. Run the batch tier on Spot VMs
- B. Use local SSD for the scratch space
- C. Use a custom machine type sized to the workload
- D. Use sole-tenant nodes

### 27. Pods must call the payment API without any key on disk. What should be enabled?

Domain: Managing and provisioning a solution infrastructure

- A. Enable Workload Identity Federation for GKE
- B. Create a service account key file for the pipeline
- C. Use Workload Identity Federation for the external pipeline
- D. Put the credential in an environment variable on the instance

### 28. No node may have an external address, but pods must still reach Google APIs. What should be configured?

Domain: Managing and provisioning a solution infrastructure

- A. Create private nodes with no external IP addresses
- B. Use sole-tenant nodes
- C. Create a zonal GKE cluster
- D. Deploy Cloud NAT for outbound traffic

### 29. A payment cluster must be built with pod identity and attested images. Which sequence is correct?

Domain: Managing and provisioning a solution infrastructure

- A. Create a regional private cluster → build a Shared VPC with private subnets → enable APIs → deploy through Binary Authorization
- B. Deploy through Binary Authorization → create the cluster → build the Shared VPC → create the project
- C. Create the project and enable APIs → build a Shared VPC with private subnets → create a regional private cluster with Workload Identity Federation for GKE → deploy through Binary Authorization
- D. Build a Shared VPC → deploy through Binary Authorization → create the project → create the cluster

### 30. A webhook receiver must answer within 300 ms after a quiet period. What should be configured?

Domain: Managing and provisioning a solution infrastructure

- A. Deploy the workload on Cloud Run with a GPU
- B. Deploy on App Engine flexible environment
- C. Set a minimum instance count on the Cloud Run service
- D. Raise the request concurrency setting

### 31. A Cloud Run service is slow on cold start and its instances sit idle under load. Which two settings address that? Select two.

Domain: Managing and provisioning a solution infrastructure

- A. Use Cloud Run functions
- B. Raise the request concurrency setting
- C. Deploy on App Engine flexible environment
- D. Set a minimum instance count on the Cloud Run service
- E. Deploy the workload on Cloud Run with a GPU

### 32. Every environment must be reproducible from code with a reviewable diff. What should be used?

Domain: Managing and provisioning a solution infrastructure

- A. Manage the resources with Terraform
- B. Manage the resources with Config Connector
- C. Automate the step with the gcloud CLI
- D. Use Deployment Manager templates

### 33. Weekly fraud-model retraining must be reproducible and record lineage. What should be used?

Domain: Managing and provisioning a solution infrastructure

- A. Orchestrate the workflow in Agent Platform Pipelines
- B. Trigger the job with Cloud Scheduler
- C. Use a Dataproc cluster
- D. Run batch prediction

### 34. The team must compare two open models before choosing a licence. Where should it look?

Domain: Managing and provisioning a solution infrastructure

- A. Build the agent with the Agent Development Kit
- B. Select the model from Model Garden
- C. Use Gemini Cloud Assist for the investigation
- D. Index the corpus with Vertex AI Search

### 35. A payment event stream must be deployed with windowing and a dead-letter path. Which sequence is correct?

Domain: Managing and provisioning a solution infrastructure

- A. Monitor watermark lag → deploy the streaming job → create the topic → design the windowing
- B. Design the windowing → monitor watermark lag → create the Pub/Sub topic → deploy the job
- C. Create the Pub/Sub topic and subscription → design the Dataflow windowing and allowed lateness → deploy the streaming job with a dead-letter path → monitor watermark lag and backfill from the raw archive
- D. Deploy the streaming job → create the Pub/Sub topic → design the windowing → monitor watermark lag

### 36. A settlement role must allow exactly six permissions across two datasets. What should be created?

Domain: Designing for security and compliance

- A. Grant a predefined role at the narrowest resource
- B. Authenticate the call with an API key
- C. Define a custom role with only the required permissions
- D. Run a bastion host with a public address

### 37. A leaked credential must affect one settlement job, not the platform. What should be done?

Domain: Designing for security and compliance

- A. Tag the resources with labels for cost reporting
- B. Create a separate project per environment
- C. Give each service its own service account
- D. Create a service account key file for the pipeline

### 38. A new country project must inherit the payment access set immediately. Where should the roles be bound?

Domain: Designing for security and compliance

- A. Create a folder per environment and bind roles there
- B. Grant a predefined role at the narrowest resource
- C. Tag the resources with labels for cost reporting
- D. Create a separate project per environment

### 39. No project may create an external address, and one terminated vendor must keep no access. Which two controls apply? Select two.

Domain: Designing for security and compliance

- A. Apply an IAM deny policy
- B. Add an IAM condition on the binding
- C. Enforce the control with an organization policy constraint
- D. Create a folder per environment and bind roles there
- E. Tag the resources with labels for cost reporting

### 40. Settlement data must become unreadable the moment the bank disables a key. What should be used?

Domain: Designing for security and compliance

- A. Store the credential in Secret Manager
- B. Use Cloud HSM for the key
- C. Supply a customer-supplied encryption key
- D. Encrypt with a customer-managed key in Cloud KMS

### 41. Key material must stay in the settlement region and must change on schedule. Which two settings apply? Select two.

Domain: Designing for security and compliance

- A. Use Cloud HSM for the key
- B. Supply a customer-supplied encryption key
- C. Create the key ring in the same region as the data
- D. Put the credential in an environment variable on the instance
- E. Set an automatic rotation period on the key

### 42. Settlement data must not be copied outside the approved projects. What should be applied?

Domain: Designing for security and compliance

- A. Apply an IAM deny policy
- B. Put the projects inside a VPC Service Controls perimeter
- C. Tag the resources with labels for cost reporting
- D. Apply a hierarchical firewall policy at the organization or folder

### 43. Merchants must reach an internal support console with no VPN. What should be used?

Domain: Designing for security and compliance

- A. Deploy Cloud NAT for outbound traffic
- B. Put Identity-Aware Proxy in front of the application
- C. Enable Private Google Access on the subnet
- D. Run a bastion host with a public address

### 44. A pipeline in another cloud must call the API with no key, and administrators must not hold public addresses. Which two controls apply? Select two.

Domain: Designing for security and compliance

- A. Use OS Login for administrative SSH
- B. Put the credential in an environment variable on the instance
- C. Create a service account key file for the pipeline
- D. Use Workload Identity Federation for the external pipeline
- E. Authenticate the call with an API key

### 45. Only images signed by the payment pipeline may run. What should be enforced?

Domain: Designing for security and compliance

- A. Require Binary Authorization attestations
- B. Enable network policy enforcement
- C. Store the images in Artifact Registry
- D. Enable Artifact Analysis scanning on the repository

### 46. Merchant statements contain card numbers that must not reach analytics. What should be used?

Domain: Designing for security and compliance

- A. Require an access level in the perimeter
- B. Screen prompts and responses with Model Armor
- C. Turn on Security Command Center findings
- D. De-identify the data with Sensitive Data Protection

### 47. The scheme must show which employee read a settlement file. What should be enabled?

Domain: Designing for security and compliance

- A. Enable Data Access audit logs
- B. Rely on Admin Activity audit logs
- C. Review Access Transparency logs
- D. Create a log-based metric

### 48. Evidence must be readable for seven years and cannot be shortened. What should be used?

Domain: Designing for security and compliance

- A. Apply a bucket retention policy with a locked period
- B. Create a log-based metric
- C. Use a locked log bucket with a fixed retention
- D. Rely on Admin Activity audit logs

### 49. A scheme audit needs read evidence retained and queryable. Which sequence is correct?

Domain: Designing for security and compliance

- A. Query the evidence → create a locked log bucket → enable audit logs → route the logs
- B. Enable data access audit logs for the services in scope → create a locked log bucket with the required retention → route the logs with an aggregated sink → query and export the evidence for the auditor
- C. Route the logs with a sink → query the evidence → enable audit logs → create a locked bucket
- D. Create a locked log bucket → enable data access audit logs → query the evidence → route the logs with a sink

### 50. A delivery team must never apply an unreviewed change to production. What should the pipeline enforce?

Domain: Analyzing and optimizing technical and business processes

- A. Rebuild the artifact separately for each environment
- B. Require a reviewed pull request and a passing plan
- C. Adopt trunk-based development with short-lived branches
- D. Roll the change out instance by instance

### 51. Three squads keep branches open for a month and merge painfully. What should change?

Domain: Analyzing and optimizing technical and business processes

- A. Put the change behind a feature flag
- B. Adopt trunk-based development with short-lived branches
- C. Rebuild the artifact separately for each environment
- D. Roll the change out instance by instance

### 52. A deployment failed at 02:40 and the team needs the exact error text. Where should it look?

Domain: Analyzing and optimizing technical and business processes

- A. Act on the Recommender suggestions
- B. Publish a shared dashboard
- C. Inspect the trace waterfall in Cloud Trace
- D. Query the entries in Cloud Logging

### 53. A settlement request is slow, and the same exception keeps recurring. Which two tools apply? Select two.

Domain: Analyzing and optimizing technical and business processes

- A. Inspect the trace waterfall in Cloud Trace
- B. Group the exceptions in Error Reporting
- C. Publish a shared dashboard
- D. Publish a runbook per alert
- E. Define an SLO with an error budget

### 54. The launch must be proven at two million concurrent players. What should be run?

Domain: Analyzing and optimizing technical and business processes

- A. Run a load test at the expected peak
- B. Commission a penetration test
- C. Run a chaos experiment against a zone
- D. Cover the change with unit, integration, and a few end-to-end tests

### 55. A game client and a payment API are versioned independently. What stops a breaking change?

Domain: Analyzing and optimizing technical and business processes

- A. Run a load test at the expected peak
- B. Add a contract test on the API
- C. Cover the change with unit, integration, and a few end-to-end tests
- D. Commission a penetration test

### 56. The service needs a fifteen-minute recovery objective and can fund a smaller running copy. What fits?

Domain: Analyzing and optimizing technical and business processes

- A. Use backup and restore
- B. Run active-active across two regions
- C. Run a warm standby at reduced capacity
- D. Run a pilot-light standby

### 57. The launch is approved for one week of spend only. What should be reviewed before it starts?

Domain: Analyzing and optimizing technical and business processes

- A. Tag the resources with labels for cost reporting
- B. Set a budget with alert thresholds
- C. Export billing to BigQuery and review it per label
- D. Act on the Recommender suggestions

### 58. The launch budget must be protected without guessing what to change. Which sequence is correct?

Domain: Analyzing and optimizing technical and business processes

- A. Inspect the query plan and bytes processed → partition and cluster the table on the filter columns → rewrite the query to prune partitions → measure the new slot time and bytes scanned
- B. Rewrite the query → partition the table → measure slot time → inspect the plan
- C. Partition and cluster the table → measure slot time → inspect the plan → rewrite the query
- D. Measure slot time → rewrite the query → inspect the plan → partition the table

### 59. Marketing, engineering, and finance disagree about the launch criteria. What should the architect do?

Domain: Analyzing and optimizing technical and business processes

- A. Publish a runbook per alert
- B. Route the change through a change advisory board
- C. Publish a service catalog entry with an approved template
- D. Agree the decision rights with the stakeholders

### 60. A new region must be provisioned the same way as the others without a ticket. What should be published?

Domain: Analyzing and optimizing technical and business processes

- A. Tag the resources with labels for cost reporting
- B. Manage the resources with Terraform
- C. Enforce the control with an organization policy constraint
- D. Publish a service catalog entry with an approved template

### 61. The launch date cannot move and one region is not yet approved. What should the architect do?

Domain: Analyzing and optimizing technical and business processes

- A. Route the change through a change advisory board
- B. Publish a service catalog entry with an approved template
- C. Publish a runbook per alert
- D. Record the risk and its owner in a risk register

### 62. The launch date is fixed but one service may need to be disabled instantly. What should be used?

Domain: Managing implementation

- A. Put the change behind a feature flag
- B. Deploy blue/green with a traffic switch
- C. Roll out a canary to a small share of traffic
- D. Roll the change out instance by instance

### 63. Launch requires two identical environments and an exact restore of the previous build. Which two practices apply? Select two.

Domain: Managing implementation

- A. Set a budget with alert thresholds
- B. Rebuild the artifact separately for each environment
- C. Keep the previous image digest ready for rollback
- D. Promote the same tested artifact between environments
- E. Deploy blue/green with a traffic switch

### 64. A launch-day release must be reversible within one minute. Which sequence is correct?

Domain: Managing implementation

- A. Build an immutable image and record its digest → deploy the new revision without traffic → shift a small traffic percentage and watch error and latency signals → promote to full traffic or roll back to the pinned digest
- B. Deploy the new revision → promote to full traffic → shift a small percentage → build the image
- C. Shift full traffic to the new revision → build the image → watch the error rate → promote or roll back
- D. Watch the error rate → deploy the new revision → shift traffic → build the image

### 65. Nine hundred merchants need per-consumer quotas and mediation. What should be used?

Domain: Managing implementation

- A. Publish the API through Apigee
- B. Attach a Cloud Armor security policy
- C. Use Cloud Endpoints
- D. Use API Gateway

### 66. A single service needs a managed OpenAPI front door without a policy engine. What should be used?

Domain: Managing implementation

- A. Use Cloud Endpoints
- B. Attach a Cloud Armor security policy
- C. Use API Gateway
- D. Publish the API through Apigee

### 67. A 12 TB ordering database must cut over with less than four hours of downtime. What should be used?

Domain: Managing implementation

- A. Use the BigQuery Data Transfer Service
- B. Migrate the database with Database Migration Service
- C. Use Datastream for change data capture
- D. Copy the files with Storage Transfer Service

### 68. A legacy ordering application must run on GKE without being rewritten. What should be used?

Domain: Managing implementation

- A. Convert the VMs with Migrate to Containers
- B. Copy the files with Storage Transfer Service
- C. Run the legacy stack on Google Cloud VMware Engine
- D. Assess the estate in Migration Center

### 69. A nine-month migration must move dependencies together and stay reversible. Which sequence is correct?

Domain: Managing implementation

- A. Cut over and decommission → validate a pilot wave → inventory the estate → group servers into waves
- B. Validate a pilot wave → inventory the estate → group servers into waves → cut over and decommission
- C. Inventory the estate in Migration Center → group servers into dependency-based waves → validate a pilot wave in the target landing zone → cut over wave by wave and decommission the source
- D. Group servers into waves → inventory the estate → cut over and decommission → validate a pilot wave

### 70. The ordering pipeline must be tested locally with no billable resource. What should be used?

Domain: Managing implementation

- A. Run the build in Cloud Build
- B. Run the emulator in the pipeline
- C. Automate the step with the gcloud CLI
- D. Manage the resources with Terraform

### 71. A merchant client must handle quota errors with the recommended backoff. What should it use?

Domain: Managing implementation

- A. Automate the step with the gcloud CLI
- B. Use the Google API client library with retries
- C. Impersonate a service account for a curl test
- D. Authenticate the call with an API key

### 72. Host metrics and application logs must reach Google Cloud from the game fleet. What should be installed?

Domain: Ensuring solution and operations excellence

- A. Inspect the trace waterfall in Cloud Trace
- B. Install the Ops Agent on the instances
- C. Group the exceptions in Error Reporting
- D. Attach Cloud Profiler to the service

### 73. The launch promise is measured in successful sessions, not in CPU. What should be defined?

Domain: Ensuring solution and operations excellence

- A. Define an SLO with an error budget
- B. Publish a shared dashboard
- C. Add an uptime check from several regions
- D. Create an alerting policy on the metric

### 74. A specific payment error must be counted and then reported to the on-call engineer. Which two steps apply? Select two.

Domain: Ensuring solution and operations excellence

- A. Create an alerting policy on the metric
- B. Act on the Recommender suggestions
- C. Define an SLO with an error budget
- D. Publish a shared dashboard
- E. Create a log-based metric

### 75. Launch night must not depend on which engineer is awake. What should be published?

Domain: Ensuring solution and operations excellence

- A. Match the support plan to the recovery commitment
- B. Define an on-call rotation with an escalation path
- C. Publish a shared dashboard
- D. Publish a runbook per alert

### 76. No named person currently answers a payment alert at night. What should be established?

Domain: Ensuring solution and operations excellence

- A. Put the recovery commitment in the contract
- B. Publish a runbook per alert
- C. Match the support plan to the recovery commitment
- D. Define an on-call rotation with an escalation path

### 77. A regional failover has never carried real traffic. What should be run before launch?

Domain: Ensuring solution and operations excellence

- A. Commission a penetration test
- B. Run a load test at the expected peak
- C. Run a chaos experiment against a zone
- D. Roll out a canary to a small share of traffic

### 78. A failed cutover recurred because the follow-up work was never recorded. What should be produced after each incident?

Domain: Ensuring solution and operations excellence

- A. Publish a runbook per alert
- B. Publish a shared dashboard
- C. Write a blameless postmortem with actions
- D. Match the support plan to the recovery commitment

### 79. The business expects a thirty-minute response during the launch window. What should be aligned?

Domain: Ensuring solution and operations excellence

- A. Match the support plan to the recovery commitment
- B. Put the recovery commitment in the contract
- C. Publish a runbook per alert
- D. Define an on-call rotation with an escalation path

### 80. The payment API is failing during the launch and the response must follow the agreed order. Which sequence is correct?

Domain: Ensuring solution and operations excellence

- A. Isolate the root cause → detect the symptom → write the postmortem → restore service
- B. Detect the symptom through an alert → contain the impact and restore service → isolate the root cause from logs, traces, and metrics → apply the permanent fix and write the postmortem
- C. Restore service → detect the symptom → write the postmortem → isolate the root cause
- D. Write the postmortem → detect the symptom → isolate the root cause → restore service

---

## Case study — Atlas Retail Cloud

Atlas Retail Cloud is moving 1,800 virtual machines and 60 databases from two data centres into Google Cloud over nine months. The estate includes a 12 TB Oracle database that supports the ordering system and a set of Windows file servers used by 400 stores. The business cannot accept more than a four-hour outage per application, and the migration must be sequenced so that dependencies move together. The team has three engineers who have never run a migration, and the chief information officer wants a plan that shows what moves in each wave and how a failed wave is reversed.

The next 5 questions refer to it. Read the scenario once, then answer all 5; each item restates the constraint it tests and is scored individually.

### 81. 1,800 virtual machines must be sized before the nine-month plan is signed. What should be used?

Domain: Designing and planning a cloud solution architecture

- A. Use Database Migration Service
- B. Copy the files with Storage Transfer Service
- C. Convert the VMs with Migrate to Containers
- D. Assess the estate in Migration Center

### 82. Store file servers must stay patched with no on-site staff. What should be used?

Domain: Managing and provisioning a solution infrastructure

- A. Use a custom machine type sized to the workload
- B. Run the batch tier on Spot VMs
- C. Use VM Manager for OS patch compliance
- D. Manage the resources with Config Connector

### 83. A migration wave must be reviewed, and the tested build must reach production unchanged. Which two practices apply? Select two.

Domain: Analyzing and optimizing technical and business processes

- A. Roll the change out instance by instance
- B. Rebuild the artifact separately for each environment
- C. Promote the same tested artifact between environments
- D. Set a budget with alert thresholds
- E. Require a reviewed pull request and a passing plan

### 84. A failed wave must be reversed inside a four-hour window. What must be aligned with the vendor?

Domain: Ensuring solution and operations excellence

- A. Put the recovery commitment in the contract
- B. Define an on-call rotation with an escalation path
- C. Match the support plan to the recovery commitment
- D. Publish a runbook per alert

### 85. The CIO wants to know whether each wave actually reduced cost. What should be recorded before wave one?

Domain: Designing and planning a cloud solution architecture

- A. Publish a shared dashboard
- B. Build a three-year total cost of ownership model
- C. Define the baseline and target as a KPI with an owner
- D. Export billing to BigQuery and review it per label

---

## Case study — Cedar Health Cloud

Cedar Health Cloud is consolidating three hospital groups onto one platform. Each group has its own identity provider and its own clinical application, and the clinicians must reach all three without a second login. Patient records must stay in the country of the hospital that created them, and a clinician in one group must see only the patients of that group unless a referral grants temporary access for seventy-two hours. The consolidation must complete before the next accreditation visit in eight months, and the groups refuse to change the clinical applications this year.

The next 5 questions refer to it. Read the scenario once, then answer all 5; each item restates the constraint it tests and is scored individually.

### 86. Three hospital identity providers must be trusted without shared keys. What should be used?

Domain: Designing for security and compliance

- A. Create a service account key file for the pipeline
- B. Use Workload Identity Federation for the external pipeline
- C. Put the credential in an environment variable on the instance
- D. Authenticate the call with an API key

### 87. A consent service on Cloud Run must reach a clinical database privately. What should be attached?

Domain: Managing and provisioning a solution infrastructure

- A. Attach a Serverless VPC Access connector
- B. Deploy Cloud NAT for outbound traffic
- C. Enable Private Google Access on the subnet
- D. Publish the service through Private Service Connect

### 88. Clinical records need a fifteen-minute recovery objective at continuous cost. What fits?

Domain: Analyzing and optimizing technical and business processes

- A. Run a warm standby at reduced capacity
- B. Use backup and restore
- C. Run a pilot-light standby
- D. Run active-active across two regions

### 89. The accreditation visit follows an outage that was never reviewed. What should be produced now?

Domain: Ensuring solution and operations excellence

- A. Publish a shared dashboard
- B. Publish a runbook per alert
- C. Match the support plan to the recovery commitment
- D. Write a blameless postmortem with actions

### 90. The clinical database must fail over without an operator restart. What should be enabled?

Domain: Designing and planning a cloud solution architecture

- A. Use Memorystore
- B. Use Bigtable
- C. Enable Cloud SQL high availability with a standby
- D. Add a read replica and route reads to it

---

## Case study — Nimbus Games

Nimbus Games is launching a multiplayer title in four regions on the same day. The launch is expected to bring 2 million concurrent players in the first hour, and the game servers must be created in the region closest to each player. The studio has committed to a launch date that cannot move, and a previous launch failed because the quota for the region had never been raised. Infrastructure is defined in Terraform, and the team wants to rehearse the whole launch twice before the real one. The finance team has approved spend for launch week only, not for the year.

The next 5 questions refer to it. Read the scenario once, then answer all 5; each item restates the constraint it tests and is scored individually.

### 91. Launch-week capacity is needed for seven days and then not at all. What should be used?

Domain: Managing and provisioning a solution infrastructure

- A. Use sole-tenant nodes
- B. Run the batch tier on Spot VMs
- C. Use VM Manager for OS patch compliance
- D. Buy committed use discounts for the steady baseline

### 92. The studio must rehearse two million concurrent players twice before launch. What should be run?

Domain: Analyzing and optimizing technical and business processes

- A. Run a chaos experiment against a zone
- B. Commission a penetration test
- C. Cover the change with unit, integration, and a few end-to-end tests
- D. Run a load test at the expected peak

### 93. Each region must be watched from the first minute of launch. What should be built first?

Domain: Ensuring solution and operations excellence

- A. Act on the Recommender suggestions
- B. Publish a shared dashboard
- C. Define dashboards and metrics in Cloud Monitoring
- D. Inspect the trace waterfall in Cloud Trace

### 94. Game servers must appear in the closest region and be replaced when unhealthy. What should be used?

Domain: Designing and planning a cloud solution architecture

- A. Use a managed instance group with autoscaling
- B. Deploy the service on Cloud Run
- C. Use GKE Autopilot
- D. Submit the work as a Batch job

### 95. No region may be used that has not been approved for player data. What should be enforced?

Domain: Designing for security and compliance

- A. Create a folder per environment and bind roles there
- B. Create a separate project per environment
- C. Tag the resources with labels for cost reporting
- D. Enforce the control with an organization policy constraint

---

## Case study — Zephyr Payments

Zephyr Payments exposes a payment API to 900 merchants and processes 4 million calls a day. Merchants have different rate limits, and one merchant caused a 40-minute outage last quarter by retrying aggressively after a timeout. The API must never break a merchant integration, so the versioning and deprecation policy has to be explicit. The company wants to release several times a day and to be able to stop a bad release within a minute. Each release must be traceable to a commit and a passing test run, and the security team wants to know which images are running in production at any moment.

The next 5 questions refer to it. Read the scenario once, then answer all 5; each item restates the constraint it tests and is scored individually.

### 96. Nine hundred merchants need individual quotas, and one retried through an outage. What should front the API?

Domain: Managing implementation

- A. Attach a Cloud Armor security policy
- B. Use API Gateway
- C. Publish the API through Apigee
- D. Use Cloud Endpoints

### 97. A bad release must be stopped within a minute without a rebuild. What should the release use?

Domain: Managing implementation

- A. Roll out a canary to a small share of traffic
- B. Put the change behind a feature flag
- C. Deploy blue/green with a traffic switch
- D. Roll the change out instance by instance

### 98. The security team asks what built the running image and from which commit. What should be recorded?

Domain: Designing for security and compliance

- A. Enable Artifact Analysis scanning on the repository
- B. Record build provenance for the artifact
- C. Store the images in Artifact Registry
- D. Enable network policy enforcement

### 99. Merchant success rate is the promise, not processor load. What should be defined?

Domain: Ensuring solution and operations excellence

- A. Add an uptime check from several regions
- B. Publish a shared dashboard
- C. Create an alerting policy on the metric
- D. Define an SLO with an error budget

### 100. Merchants must never be locked into an integration they cannot leave. What must the design include?

Domain: Designing and planning a cloud solution architecture

- A. Build a three-year total cost of ownership model
- B. Document the exit plan and data portability
- C. Tag the resources with labels for cost reporting
- D. Set a budget with alert thresholds

---

## Answer key and explanations

### Question 1 — B

Answer: Define the baseline and target as a KPI with an owner. A measured baseline and a named owner make the outcome testable after the programme. Local study-map skill 1.1 (Business Requirements and Success Metrics), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 1 (designing and planning): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. The model compares run cost, people cost, and exit cost rather than the monthly bill alone. Why the correct answer wins: A measured baseline and a named owner make the outcome testable after the programme.
- **B:** Correct. In this case: A measured baseline and a named owner make the outcome testable after the programme.
- **C:** Incorrect for this question. The export attributes cost to the team and service that caused it. Why the correct answer wins: A measured baseline and a named owner make the outcome testable after the programme.
- **D:** Incorrect for this question. The dashboard gives the team one view of the same signals during an incident. Why the correct answer wins: A measured baseline and a named owner make the outcome testable after the programme.

### Question 2 — C

Answer: Build a three-year total cost of ownership model. The model compares run cost, people cost, and exit cost rather than the monthly bill alone. Local study-map skill 1.1 (Business Requirements and Success Metrics), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 1 (designing and planning): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. A one- or three-year commitment discounts the capacity that runs constantly, not the peaks. Why the correct answer wins: The model compares run cost, people cost, and exit cost rather than the monthly bill alone.
- **B:** Incorrect for this question. A budget alerts on spend but does not stop it. Why the correct answer wins: The model compares run cost, people cost, and exit cost rather than the monthly bill alone.
- **C:** Correct. In this case: The model compares run cost, people cost, and exit cost rather than the monthly bill alone.
- **D:** Incorrect for this question. The export attributes cost to the team and service that caused it. Why the correct answer wins: The model compares run cost, people cost, and exit cost rather than the monthly bill alone.

### Question 3 — D

Answer: Document the exit plan and data portability. An exit plan and data portability keep the migration reversible and bound how proprietary the design may become. The exit plan keeps the migration reversible and constrains how proprietary the design may become. Local study-map skill 1.2 (Non-Functional Requirements and Trade-offs), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 1 (designing and planning): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. A budget alerts on spend but does not stop it. Why the correct answer wins: An exit plan and data portability keep the migration reversible and bound how proprietary the design may become.
- **B:** Incorrect for this question. The model compares run cost, people cost, and exit cost rather than the monthly bill alone. Why the correct answer wins: An exit plan and data portability keep the migration reversible and bound how proprietary the design may become.
- **C:** Incorrect for this question. Labels attribute spend in billing export; they do not grant or restrict access. Why the correct answer wins: An exit plan and data portability keep the migration reversible and bound how proprietary the design may become.
- **D:** Correct. The exit plan keeps the migration reversible and constrains how proprietary the design may become. In this case: An exit plan and data portability keep the migration reversible and bound how proprietary the design may become.

### Question 4 — A

Answer: Keep the data in the region the regulator requires. Residency fixes where storage and processing may happen, which then constrains every service choice. Local study-map skill 1.2 (Non-Functional Requirements and Trade-offs), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 1 (designing and planning): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Correct. In this case: Residency fixes where storage and processing may happen, which then constrains every service choice.
- **B:** Incorrect for this question. The model compares run cost, people cost, and exit cost rather than the monthly bill alone. Why the correct answer wins: Residency fixes where storage and processing may happen, which then constrains every service choice.
- **C:** Incorrect for this question. A measured baseline and a named owner make the outcome testable after the migration. Why the correct answer wins: Residency fixes where storage and processing may happen, which then constrains every service choice.
- **D:** Incorrect for this question. The exit plan keeps the migration reversible and constrains how proprietary the design may become. Why the correct answer wins: Residency fixes where storage and processing may happen, which then constrains every service choice.

### Question 5 — C, E

Answers: Set the RPO and RTO with the business owner; Put the recovery commitment in the contract. The targets quantify the acceptable loss, and the contract attaches a consequence to missing them. The targets come from the business impact of data loss and downtime, not from the technology. The contract converts an internal target into an obligation with a consequence. Local study-map skill 1.2 (Non-Functional Requirements and Trade-offs), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 1 (designing and planning): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. The dashboard gives the team one view of the same signals during an incident. Why the correct answer wins: The targets quantify the acceptable loss, and the contract attaches a consequence to missing them.
- **B:** Incorrect for this question. Recommender reports idle and over-provisioned resources with the estimated saving. Why the correct answer wins: The targets quantify the acceptable loss, and the contract attaches a consequence to missing them.
- **C:** Correct. The contract converts an internal target into an obligation with a consequence. In this case: The targets quantify the acceptable loss, and the contract attaches a consequence to missing them.
- **D:** Incorrect for this question. Labels attribute spend in billing export; they do not grant or restrict access. Why the correct answer wins: The targets quantify the acceptable loss, and the contract attaches a consequence to missing them.
- **E:** Correct. The targets come from the business impact of data loss and downtime, not from the technology. In this case: The targets quantify the acceptable loss, and the contract attaches a consequence to missing them.

### Question 6 — B

Answer: Enable Cloud SQL high availability with a standby. A regional standby takes over automatically when the primary zone fails. Local study-map skill 1.3 (High Availability and Failover Design), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 1 (designing and planning): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. A replica offloads read traffic but lags the primary, so it is not a failover target. Why the correct answer wins: A regional standby takes over automatically when the primary zone fails.
- **B:** Correct. In this case: A regional standby takes over automatically when the primary zone fails.
- **C:** Incorrect for this question. Memorystore provides managed Redis or Memcached for sub-millisecond cache lookups. Why the correct answer wins: A regional standby takes over automatically when the primary zone fails.
- **D:** Incorrect for this question. Bigtable is a wide-column store for high-throughput key reads and writes at low latency. Why the correct answer wins: A regional standby takes over automatically when the primary zone fails.

### Question 7 — C, D

Answers: Run active-active across two regions; Replicate the data to the second region. Both regions serve traffic, and the data must already be in the second region when it is needed. Both regions serve traffic, so a regional loss is absorbed without a failover decision. The data must exist in the second region before any compute there can serve it. Local study-map skill 1.3 (High Availability and Failover Design), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 1 (designing and planning): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. Restoring from backup is the cheapest option and the slowest to recover. Why the correct answer wins: Both regions serve traffic, and the data must already be in the second region when it is needed.
- **B:** Incorrect for this question. CDN caches responses at edge locations, which cuts origin load and latency for repeat reads. Why the correct answer wins: Both regions serve traffic, and the data must already be in the second region when it is needed.
- **C:** Correct. The data must exist in the second region before any compute there can serve it. In this case: Both regions serve traffic, and the data must already be in the second region when it is needed.
- **D:** Correct. Both regions serve traffic, so a regional loss is absorbed without a failover decision. In this case: Both regions serve traffic, and the data must already be in the second region when it is needed.
- **E:** Incorrect for this question. Only the core data and configuration stay warm, so recovery starts the compute and takes minutes. Why the correct answer wins: Both regions serve traffic, and the data must already be in the second region when it is needed.

### Question 8 — C

Answer: Build a Network Connectivity Center hub. Peering is not transitive, so a hub provides the routing the spokes cannot provide themselves. The hub gives transitive routing between spokes, which peering alone cannot provide. Local study-map skill 1.4 (Network Design), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 1 (designing and planning): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. Cloud NAT lets private instances reach the internet without an external address. Why the correct answer wins: Peering is not transitive, so a hub provides the routing the spokes cannot provide themselves.
- **B:** Incorrect for this question. Peering joins two networks at layer three but does not share firewalls or transitive routes. Why the correct answer wins: Peering is not transitive, so a hub provides the routing the spokes cannot provide themselves.
- **C:** Correct. The hub gives transitive routing between spokes, which peering alone cannot provide. In this case: Peering is not transitive, so a hub provides the routing the spokes cannot provide themselves.
- **D:** Incorrect for this question. DNS peering resolves names across networks without transferring zone ownership. Why the correct answer wins: Peering is not transitive, so a hub provides the routing the spokes cannot provide themselves.

### Question 9 — A, C

Answers: Publish the service through Private Service Connect; Peer the two VPC networks. A published endpoint gives a private address, and peering joins the two networks at layer three. A PSC endpoint gives a private IP in the consumer VPC without peering or exposing the service publicly. Peering joins two networks at layer three but does not share firewalls or transitive routes. Local study-map skill 1.4 (Network Design), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 1 (designing and planning): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Correct. A PSC endpoint gives a private IP in the consumer VPC without peering or exposing the service publicly. In this case: A published endpoint gives a private address, and peering joins the two networks at layer three.
- **B:** Incorrect for this question. Cloud NAT lets private instances reach the internet without an external address. Why the correct answer wins: A published endpoint gives a private address, and peering joins the two networks at layer three.
- **C:** Correct. Peering joins two networks at layer three but does not share firewalls or transitive routes. In this case: A published endpoint gives a private address, and peering joins the two networks at layer three.
- **D:** Incorrect for this question. CDN caches responses at edge locations, which cuts origin load and latency for repeat reads. Why the correct answer wins: A published endpoint gives a private address, and peering joins the two networks at layer three.
- **E:** Incorrect for this question. A signed URL grants one object for a fixed time without exposing credentials or making the bucket public. Why the correct answer wins: A published endpoint gives a private address, and peering joins the two networks at layer three.

### Question 10 — D

Answer: Use Bigtable. Bigtable is the wide-column store built for high-throughput key access at low latency. Bigtable is a wide-column store for high-throughput key reads and writes at low latency. Local study-map skill 1.5 (Storage and Data Store Selection), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 1 (designing and planning): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. Cloud SQL is a managed MySQL, PostgreSQL, or SQL Server instance with a familiar connection model. Why the correct answer wins: Bigtable is the wide-column store built for high-throughput key access at low latency.
- **B:** Incorrect for this question. BigQuery is serverless, columnar, and separates storage from compute, so a scan pays for the bytes read. Why the correct answer wins: Bigtable is the wide-column store built for high-throughput key access at low latency.
- **C:** Incorrect for this question. Firestore is a document store with real-time listeners and per-document transactions. Why the correct answer wins: Bigtable is the wide-column store built for high-throughput key access at low latency.
- **D:** Correct. Bigtable is a wide-column store for high-throughput key reads and writes at low latency. In this case: Bigtable is the wide-column store built for high-throughput key access at low latency.

### Question 11 — A, D

Answers: Enable Autoclass on the bucket; Add a lifecycle rule that transitions and then deletes. Autoclass handles the changing temperature, and the lifecycle rule deletes on age. Autoclass moves each object between classes as its access pattern changes, with no lifecycle rules to maintain. A lifecycle rule acts on object age or class, so retention stops depending on a person. Local study-map skill 1.5 (Storage and Data Store Selection), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 1 (designing and planning): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Correct. Autoclass moves each object between classes as its access pattern changes, with no lifecycle rules to maintain. In this case: Autoclass handles the changing temperature, and the lifecycle rule deletes on age.
- **B:** Incorrect for this question. Local SSD is the fastest ephemeral option and loses its data when the VM stops. Why the correct answer wins: Autoclass handles the changing temperature, and the lifecycle rule deletes on age.
- **C:** Incorrect for this question. Nearline suits data read about once a month and charges for early deletion. Why the correct answer wins: Autoclass handles the changing temperature, and the lifecycle rule deletes on age.
- **D:** Correct. A lifecycle rule acts on object age or class, so retention stops depending on a person. In this case: Autoclass handles the changing temperature, and the lifecycle rule deletes on age.
- **E:** Incorrect for this question. Filestore provides a managed NFS export that many clients can mount at once. Why the correct answer wins: Autoclass handles the changing temperature, and the lifecycle rule deletes on age.

### Question 12 — B

Answer: Use GKE Autopilot. Autopilot manages nodes, scaling, and patching, so the team owns only its workloads. Local study-map skill 1.6 (Compute Platform Selection), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 1 (designing and planning): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. Cloud Run runs a stateless container per request and scales to zero when idle. Why the correct answer wins: Autopilot manages nodes, scaling, and patching, so the team owns only its workloads.
- **B:** Correct. In this case: Autopilot manages nodes, scaling, and patching, so the team owns only its workloads.
- **C:** Incorrect for this question. Batch schedules containerised jobs onto managed or existing capacity and retires it when done. Why the correct answer wins: Autopilot manages nodes, scaling, and patching, so the team owns only its workloads.
- **D:** Incorrect for this question. Standard exposes node configuration and patching, which the team must then run itself. Why the correct answer wins: Autopilot manages nodes, scaling, and patching, so the team owns only its workloads.

### Question 13 — D

Answer: Deploy the service on Cloud Run. Cloud Run scales to zero and bills per request, which suits an intermittent receiver. Cloud Run runs a stateless container per request and scales to zero when idle. Local study-map skill 1.6 (Compute Platform Selection), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 1 (designing and planning): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. The group replaces unhealthy instances and adds capacity from a template as load rises. Why the correct answer wins: Cloud Run scales to zero and bills per request, which suits an intermittent receiver.
- **B:** Incorrect for this question. VMware Engine keeps the existing hypervisor and operations model while moving the hardware into Google Cloud. Why the correct answer wins: Cloud Run scales to zero and bills per request, which suits an intermittent receiver.
- **C:** Incorrect for this question. Standard exposes node configuration and patching, which the team must then run itself. Why the correct answer wins: Cloud Run scales to zero and bills per request, which suits an intermittent receiver.
- **D:** Correct. Cloud Run runs a stateless container per request and scales to zero when idle. In this case: Cloud Run scales to zero and bills per request, which suits an intermittent receiver.

### Question 14 — D

Answer: Use Dataflow. Dataflow runs one Apache Beam pipeline with autoscaling in both batch and streaming modes. Local study-map skill 1.7 (Data Processing and Analytics Selection), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 1 (designing and planning): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. A Dataproc cluster runs open-source Spark and Hadoop with jobs that need a persistent cluster. Why the correct answer wins: Dataflow runs one Apache Beam pipeline with autoscaling in both batch and streaming modes.
- **B:** Incorrect for this question. Scheduler fires a job on a cron or App Engine schedule and retries on failure. Why the correct answer wins: Dataflow runs one Apache Beam pipeline with autoscaling in both batch and streaming modes.
- **C:** Incorrect for this question. The service runs scheduled loads from SaaS sources and other clouds into BigQuery. Why the correct answer wins: Dataflow runs one Apache Beam pipeline with autoscaling in both batch and streaming modes.
- **D:** Correct. In this case: Dataflow runs one Apache Beam pipeline with autoscaling in both batch and streaming modes.

### Question 15 — B, D

Answers: Publish events to Pub/Sub; Attach a dead-letter topic. Pub/Sub fans out to every subscription, and the dead-letter topic holds messages that fail repeatedly. Pub/Sub decouples producers from consumers and holds each message until every subscription acknowledges it. Local study-map skill 1.7 (Data Processing and Analytics Selection), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 1 (designing and planning): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. Tasks dispatches HTTP or App Engine requests with rate limits and per-queue retry policy. Why the correct answer wins: Pub/Sub fans out to every subscription, and the dead-letter topic holds messages that fail repeatedly.
- **B:** Correct. In this case: Pub/Sub fans out to every subscription, and the dead-letter topic holds messages that fail repeatedly.
- **C:** Incorrect for this question. Eventarc delivers Google Cloud and custom events to Cloud Run, functions, or Workflows. Why the correct answer wins: Pub/Sub fans out to every subscription, and the dead-letter topic holds messages that fail repeatedly.
- **D:** Correct. Pub/Sub decouples producers from consumers and holds each message until every subscription acknowledges it. In this case: Pub/Sub fans out to every subscription, and the dead-letter topic holds messages that fail repeatedly.
- **E:** Incorrect for this question. Scheduler fires a job on a cron or App Engine schedule and retries on failure. Why the correct answer wins: Pub/Sub fans out to every subscription, and the dead-letter topic holds messages that fail repeatedly.

### Question 16 — B

Answer: Call Gemini through Agent Platform. The managed endpoint adds IAM, audit logging, and regional processing terms. Local study-map skill 1.8 (AI and ML Solution Design), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 1 (designing and planning): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. Vertex AI Search returns grounded, cited results over private documents without a custom index. Why the correct answer wins: The managed endpoint adds IAM, audit logging, and regional processing terms.
- **B:** Correct. In this case: The managed endpoint adds IAM, audit logging, and regional processing terms.
- **C:** Incorrect for this question. Gemini Enterprise adds enterprise search, agents, and governance over the connected corpus. Why the correct answer wins: The managed endpoint adds IAM, audit logging, and regional processing terms.
- **D:** Incorrect for this question. The prebuilt Vision model labels, detects, and reads text without training a model. Why the correct answer wins: The managed endpoint adds IAM, audit logging, and regional processing terms.

### Question 17 — A, D

Answers: Select the model from Model Garden; Deploy to an online prediction endpoint. Model Garden is where the model is chosen, and an endpoint serves it for online predictions. Model Garden lists first-party and open models with deployment options and licensing. An endpoint keeps capacity ready for low-latency per-request predictions. Local study-map skill 1.8 (AI and ML Solution Design), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 1 (designing and planning): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Correct. An endpoint keeps capacity ready for low-latency per-request predictions. In this case: Model Garden is where the model is chosen, and an endpoint serves it for online predictions.
- **B:** Incorrect for this question. Cloud Assist explains configurations and proposes changes inside the console with your permissions. Why the correct answer wins: Model Garden is where the model is chosen, and an endpoint serves it for online predictions.
- **C:** Incorrect for this question. The kit gives code-first control over tools and state when a low-code builder is not enough. Why the correct answer wins: Model Garden is where the model is chosen, and an endpoint serves it for online predictions.
- **D:** Correct. Model Garden lists first-party and open models with deployment options and licensing. In this case: Model Garden is where the model is chosen, and an endpoint serves it for online predictions.
- **E:** Incorrect for this question. Looker keeps one governed semantic definition so every dashboard computes the metric the same way. Why the correct answer wins: Model Garden is where the model is chosen, and an endpoint serves it for online predictions.

### Question 18 — C

Answer: Assess the estate in Migration Center. Migration Center inventories the estate and estimates target size and cost before a plan is funded. Migration Center inventories the servers and estimates the target size and cost. Local study-map skill 1.9 (Migration Planning and Future Improvement), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 1 (designing and planning): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. The service moves object data between buckets or clouds on a schedule. Why the correct answer wins: Migration Center inventories the estate and estimates target size and cost before a plan is funded.
- **B:** Incorrect for this question. The tool rewrites a VM workload into a container image so it can run on GKE. Why the correct answer wins: Migration Center inventories the estate and estimates target size and cost before a plan is funded.
- **C:** Correct. Migration Center inventories the servers and estimates the target size and cost. In this case: Migration Center inventories the estate and estimates target size and cost before a plan is funded.
- **D:** Incorrect for this question. The service moves a database with continuous replication and a short cutover window. Why the correct answer wins: Migration Center inventories the estate and estimates target size and cost before a plan is funded.

### Question 19 — D

Answer: Use a Transfer Appliance for the one-off bulk move. The appliance ships the data physically when the network would take months to carry it. Local study-map skill 1.9 (Migration Planning and Future Improvement), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 1 (designing and planning): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. The service moves object data between buckets or clouds on a schedule. Why the correct answer wins: The appliance ships the data physically when the network would take months to carry it.
- **B:** Incorrect for this question. The storage commands copy and sync objects with resumable, parallel transfers. Why the correct answer wins: The appliance ships the data physically when the network would take months to carry it.
- **C:** Incorrect for this question. The service runs scheduled, filtered transfers from another cloud or an HTTP source. Why the correct answer wins: The appliance ships the data physically when the network would take months to carry it.
- **D:** Correct. In this case: The appliance ships the data physically when the network would take months to carry it.

### Question 20 — A

Answer: Set the RTO and RPO targets → choose the DR pattern that meets them → build and replicate the standby environment → fail over in a game day and record the result. Targets drive the pattern, the pattern drives the build, and only a rehearsal proves the numbers. Local study-map skill 1.9 (Migration Planning and Future Improvement), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 1 (designing and planning): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Correct. In this case: Targets drive the pattern, the pattern drives the build, and only a rehearsal proves the numbers.
- **B:** Incorrect for this question. A failover drill with no targets or standby environment proves nothing. Why the correct answer wins: Targets drive the pattern, the pattern drives the build, and only a rehearsal proves the numbers.
- **C:** Incorrect for this question. The pattern has no basis until the targets exist, and the drill cannot precede the build. Why the correct answer wins: Targets drive the pattern, the pattern drives the build, and only a rehearsal proves the numbers.
- **D:** Incorrect for this question. Building before the targets and pattern are chosen risks an environment that cannot meet either. Why the correct answer wins: Targets drive the pattern, the pattern drives the build, and only a rehearsal proves the numbers.

### Question 21 — D

Answer: Use HA VPN with two tunnels. Two tunnels across two interfaces survive one path failing, and the SLA depends on that. Local study-map skill 2.1 (Hybrid and Multicloud Connectivity), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 2 (managing and provisioning): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. Cloud NAT lets private instances reach the internet without an external address. Why the correct answer wins: Two tunnels across two interfaces survive one path failing, and the SLA depends on that.
- **B:** Incorrect for this question. CDN caches responses at edge locations, which cuts origin load and latency for repeat reads. Why the correct answer wins: Two tunnels across two interfaces survive one path failing, and the SLA depends on that.
- **C:** Incorrect for this question. A dedicated circuit gives predictable bandwidth and a private path at a colocation facility. Why the correct answer wins: Two tunnels across two interfaces survive one path failing, and the SLA depends on that.
- **D:** Correct. In this case: Two tunnels across two interfaces survive one path failing, and the SLA depends on that.

### Question 22 — A, B

Answers: Deploy Cloud NAT for outbound traffic; Enable Private Google Access on the subnet. Cloud NAT carries outbound internet traffic, and Private Google Access reaches the APIs from an internal address. Cloud NAT lets private instances reach the internet without an external address. Private Google Access reaches Google APIs from an internal address without a proxy or a NAT gateway. Local study-map skill 2.1 (Hybrid and Multicloud Connectivity), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 2 (managing and provisioning): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Correct. Private Google Access reaches Google APIs from an internal address without a proxy or a NAT gateway. In this case: Cloud NAT carries outbound internet traffic, and Private Google Access reaches the APIs from an internal address.
- **B:** Correct. Cloud NAT lets private instances reach the internet without an external address. In this case: Cloud NAT carries outbound internet traffic, and Private Google Access reaches the APIs from an internal address.
- **C:** Incorrect for this question. Cloud Armor filters requests at the edge with allow and deny rules and adaptive protection. Why the correct answer wins: Cloud NAT carries outbound internet traffic, and Private Google Access reaches the APIs from an internal address.
- **D:** Incorrect for this question. CDN caches responses at edge locations, which cuts origin load and latency for repeat reads. Why the correct answer wins: Cloud NAT carries outbound internet traffic, and Private Google Access reaches the APIs from an internal address.
- **E:** Incorrect for this question. IAP authenticates and authorises each request before it reaches the backend, with no VPN. Why the correct answer wins: Cloud NAT carries outbound internet traffic, and Private Google Access reaches the APIs from an internal address.

### Question 23 — B

Answer: Apply a bucket retention policy with a locked period. A locked retention policy prevents deletion or a shorter period, which is the evidence an auditor tests. Local study-map skill 2.2 (Storage Configuration and Lifecycle), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 2 (managing and provisioning): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. A lifecycle rule acts on object age or class, so retention stops depending on a person. Why the correct answer wins: A locked retention policy prevents deletion or a shorter period, which is the evidence an auditor tests.
- **B:** Correct. In this case: A locked retention policy prevents deletion or a shorter period, which is the evidence an auditor tests.
- **C:** Incorrect for this question. Versioning keeps a noncurrent copy when an object is overwritten or deleted. Why the correct answer wins: A locked retention policy prevents deletion or a shorter period, which is the evidence an auditor tests.
- **D:** Incorrect for this question. Autoclass moves each object between classes as its access pattern changes, with no lifecycle rules to maintain. Why the correct answer wins: A locked retention policy prevents deletion or a shorter period, which is the evidence an auditor tests.

### Question 24 — B, D

Answers: Partition the table on the date column; Cluster the table on the filter columns. Partitioning limits each query to the dates it names, and clustering sorts within the partition on the filter column. Partitioning limits a query to the date ranges it names, so it scans less. Clustering sorts within partitions so a filtered query reads fewer blocks. Local study-map skill 2.2 (Storage Configuration and Lifecycle), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 2 (managing and provisioning): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. Looker Studio renders the visualisation but inherits whatever query and permissions sit beneath it. Why the correct answer wins: Partitioning limits each query to the dates it names, and clustering sorts within the partition on the filter column.
- **B:** Correct. Clustering sorts within partitions so a filtered query reads fewer blocks. In this case: Partitioning limits each query to the dates it names, and clustering sorts within the partition on the filter column.
- **C:** Incorrect for this question. The view stores the aggregate result and refreshes incrementally as base data arrives. Why the correct answer wins: Partitioning limits each query to the dates it names, and clustering sorts within the partition on the filter column.
- **D:** Correct. Partitioning limits a query to the date ranges it names, so it scans less. In this case: Partitioning limits each query to the dates it names, and clustering sorts within the partition on the filter column.
- **E:** Incorrect for this question. On-demand bills per byte scanned, which is cheap for sparse use and unpredictable at scale. Why the correct answer wins: Partitioning limits each query to the dates it names, and clustering sorts within the partition on the filter column.

### Question 25 — D

Answer: Use VM Manager for OS patch compliance. VM Manager inventories and applies patches across the fleet instead of relying on manual runs. Local study-map skill 2.3 (Compute Provisioning and Patch Management), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 2 (managing and provisioning): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. Spot capacity costs far less but can be reclaimed with 30 seconds of notice. Why the correct answer wins: VM Manager inventories and applies patches across the fleet instead of relying on manual runs.
- **B:** Incorrect for this question. Cloud Build executes the pipeline steps in a managed, isolated worker with recorded provenance. Why the correct answer wins: VM Manager inventories and applies patches across the fleet instead of relying on manual runs.
- **C:** Incorrect for this question. Config Connector reconciles Google Cloud resources from Kubernetes manifests alongside the workloads. Why the correct answer wins: VM Manager inventories and applies patches across the fleet instead of relying on manual runs.
- **D:** Correct. In this case: VM Manager inventories and applies patches across the fleet instead of relying on manual runs.

### Question 26 — C

Answer: Use a custom machine type sized to the workload. Custom vCPU and memory avoid paying for a fixed shape that over-provisions one dimension. Local study-map skill 2.3 (Compute Provisioning and Patch Management), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 2 (managing and provisioning): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. Spot capacity costs far less but can be reclaimed with 30 seconds of notice. Why the correct answer wins: Custom vCPU and memory avoid paying for a fixed shape that over-provisions one dimension.
- **B:** Incorrect for this question. Local SSD is the fastest ephemeral option and loses its data when the VM stops. Why the correct answer wins: Custom vCPU and memory avoid paying for a fixed shape that over-provisions one dimension.
- **C:** Correct. In this case: Custom vCPU and memory avoid paying for a fixed shape that over-provisions one dimension.
- **D:** Incorrect for this question. Sole tenancy keeps the physical host dedicated, which matters for licensing or isolation rules. Why the correct answer wins: Custom vCPU and memory avoid paying for a fixed shape that over-provisions one dimension.

### Question 27 — A

Answer: Enable Workload Identity Federation for GKE. Workload Identity binds the pod identity to IAM, so pods hold no keys. The feature binds a Kubernetes service account to an IAM service account, so pods hold no keys. Local study-map skill 2.4 (Container Orchestration), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 2 (managing and provisioning): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Correct. The feature binds a Kubernetes service account to an IAM service account, so pods hold no keys. In this case: Workload Identity binds the pod identity to IAM, so pods hold no keys.
- **B:** Incorrect for this question. A key file is a long-lived credential that works until it is noticed and revoked. Why the correct answer wins: Workload Identity binds the pod identity to IAM, so pods hold no keys.
- **C:** Incorrect for this question. Federation exchanges an external token for short-lived Google Cloud credentials, so no key leaves the provider. Why the correct answer wins: Workload Identity binds the pod identity to IAM, so pods hold no keys.
- **D:** Incorrect for this question. An environment variable is visible to anything that can read the instance metadata or the process list. Why the correct answer wins: Workload Identity binds the pod identity to IAM, so pods hold no keys.

### Question 28 — A

Answer: Create private nodes with no external IP addresses. Private nodes reach Google APIs through Private Google Access from an internal address. Local study-map skill 2.4 (Container Orchestration), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 2 (managing and provisioning): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Correct. In this case: Private nodes reach Google APIs through Private Google Access from an internal address.
- **B:** Incorrect for this question. Sole tenancy keeps the physical host dedicated, which matters for licensing or isolation rules. Why the correct answer wins: Private nodes reach Google APIs through Private Google Access from an internal address.
- **C:** Incorrect for this question. A zonal cluster keeps its control plane in one zone, so that zone loss takes the cluster with it. Why the correct answer wins: Private nodes reach Google APIs through Private Google Access from an internal address.
- **D:** Incorrect for this question. Cloud NAT lets private instances reach the internet without an external address. Why the correct answer wins: Private nodes reach Google APIs through Private Google Access from an internal address.

### Question 29 — C

Answer: Create the project and enable APIs → build a Shared VPC with private subnets → create a regional private cluster with Workload Identity Federation for GKE → deploy through Binary Authorization. Network and identity exist before the cluster, and the admission policy is enforceable only once the cluster is running. Local study-map skill 2.4 (Container Orchestration), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 2 (managing and provisioning): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. A private cluster needs the shared network first, and the APIs must be enabled before any resource is created. Why the correct answer wins: Network and identity exist before the cluster, and the admission policy is enforceable only once the cluster is running.
- **B:** Incorrect for this question. Admission control cannot run before a cluster exists, and no resource can be created before its project. Why the correct answer wins: Network and identity exist before the cluster, and the admission policy is enforceable only once the cluster is running.
- **C:** Correct. In this case: Network and identity exist before the cluster, and the admission policy is enforceable only once the cluster is running.
- **D:** Incorrect for this question. The project precedes its network, and the deploy step belongs after the cluster rather than in the middle. Why the correct answer wins: Network and identity exist before the cluster, and the admission policy is enforceable only once the cluster is running.

### Question 30 — C

Answer: Set a minimum instance count on the Cloud Run service. A minimum instance count keeps warm capacity ready before the first request arrives. Keeping warm instances removes cold starts at the cost of paying for idle capacity. Local study-map skill 2.5 (Serverless Configuration), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 2 (managing and provisioning): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. Serverless GPU attachment suits bursty inference where a reserved node would idle. Why the correct answer wins: A minimum instance count keeps warm capacity ready before the first request arrives.
- **B:** Incorrect for this question. The flexible environment runs a custom runtime on managed VMs but does not scale to zero. Why the correct answer wins: A minimum instance count keeps warm capacity ready before the first request arrives.
- **C:** Correct. Keeping warm instances removes cold starts at the cost of paying for idle capacity. In this case: A minimum instance count keeps warm capacity ready before the first request arrives.
- **D:** Incorrect for this question. Concurrency packs more simultaneous requests into each instance before another is started. Why the correct answer wins: A minimum instance count keeps warm capacity ready before the first request arrives.

### Question 31 — B, D

Answers: Raise the request concurrency setting; Set a minimum instance count on the Cloud Run service. Warm instances remove the cold start, and higher concurrency fills each instance before scaling. Concurrency packs more simultaneous requests into each instance before another is started. Keeping warm instances removes cold starts at the cost of paying for idle capacity. Local study-map skill 2.5 (Serverless Configuration), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 2 (managing and provisioning): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. Functions bind one small handler to an event source and are the lightest way to react to one. Why the correct answer wins: Warm instances remove the cold start, and higher concurrency fills each instance before scaling.
- **B:** Correct. Concurrency packs more simultaneous requests into each instance before another is started. In this case: Warm instances remove the cold start, and higher concurrency fills each instance before scaling.
- **C:** Incorrect for this question. The flexible environment runs a custom runtime on managed VMs but does not scale to zero. Why the correct answer wins: Warm instances remove the cold start, and higher concurrency fills each instance before scaling.
- **D:** Correct. Keeping warm instances removes cold starts at the cost of paying for idle capacity. In this case: Warm instances remove the cold start, and higher concurrency fills each instance before scaling.
- **E:** Incorrect for this question. Serverless GPU attachment suits bursty inference where a reserved node would idle. Why the correct answer wins: Warm instances remove the cold start, and higher concurrency fills each instance before scaling.

### Question 32 — A

Answer: Manage the resources with Terraform. Terraform holds the desired state and produces a plan that a reviewer can read before apply. Terraform holds desired state in code, plans the diff, and applies it through a provider. Local study-map skill 2.6 (Infrastructure as Code), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 2 (managing and provisioning): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Correct. Terraform holds desired state in code, plans the diff, and applies it through a provider. In this case: Terraform holds the desired state and produces a plan that a reviewer can read before apply.
- **B:** Incorrect for this question. Config Connector reconciles Google Cloud resources from Kubernetes manifests alongside the workloads. Why the correct answer wins: Terraform holds the desired state and produces a plan that a reviewer can read before apply.
- **C:** Incorrect for this question. The CLI exposes every API as a command that can be scripted and logged. Why the correct answer wins: Terraform holds the desired state and produces a plan that a reviewer can read before apply.
- **D:** Incorrect for this question. Deployment Manager is the native but older templating service with no plan step. Why the correct answer wins: Terraform holds the desired state and produces a plan that a reviewer can read before apply.

### Question 33 — A

Answer: Orchestrate the workflow in Agent Platform Pipelines. Pipelines runs each step as a container with lineage and caching, so a rerun is reproducible. Local study-map skill 2.7 (Agent Platform ML Workflows), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 2 (managing and provisioning): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Correct. In this case: Pipelines runs each step as a container with lineage and caching, so a rerun is reproducible.
- **B:** Incorrect for this question. Scheduler fires a job on a cron or App Engine schedule and retries on failure. Why the correct answer wins: Pipelines runs each step as a container with lineage and caching, so a rerun is reproducible.
- **C:** Incorrect for this question. A Dataproc cluster runs open-source Spark and Hadoop with jobs that need a persistent cluster. Why the correct answer wins: Pipelines runs each step as a container with lineage and caching, so a rerun is reproducible.
- **D:** Incorrect for this question. Batch prediction reads a file and writes predictions without holding serving capacity. Why the correct answer wins: Pipelines runs each step as a container with lineage and caching, so a rerun is reproducible.

### Question 34 — B

Answer: Select the model from Model Garden. Model Garden lists first-party and open models with their deployment options and licensing terms. Local study-map skill 2.8 (Prebuilt AI APIs and Model Garden), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 2 (managing and provisioning): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. The kit gives code-first control over tools and state when a low-code builder is not enough. Why the correct answer wins: Model Garden lists first-party and open models with their deployment options and licensing terms.
- **B:** Correct. In this case: Model Garden lists first-party and open models with their deployment options and licensing terms.
- **C:** Incorrect for this question. Cloud Assist explains configurations and proposes changes inside the console with your permissions. Why the correct answer wins: Model Garden lists first-party and open models with their deployment options and licensing terms.
- **D:** Incorrect for this question. Vertex AI Search returns grounded, cited results over private documents without a custom index. Why the correct answer wins: Model Garden lists first-party and open models with their deployment options and licensing terms.

### Question 35 — C

Answer: Create the Pub/Sub topic and subscription → design the Dataflow windowing and allowed lateness → deploy the streaming job with a dead-letter path → monitor watermark lag and backfill from the raw archive. The source exists before the job, the window policy is chosen before deployment, and monitoring follows the running pipeline. Local study-map skill 2.8 (Prebuilt AI APIs and Model Garden), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 2 (managing and provisioning): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. There is nothing to monitor before the job runs, and the job needs a topic. Why the correct answer wins: The source exists before the job, the window policy is chosen before deployment, and monitoring follows the running pipeline.
- **B:** Incorrect for this question. Monitoring before deployment observes nothing, and the topic is created before the job. Why the correct answer wins: The source exists before the job, the window policy is chosen before deployment, and monitoring follows the running pipeline.
- **C:** Correct. In this case: The source exists before the job, the window policy is chosen before deployment, and monitoring follows the running pipeline.
- **D:** Incorrect for this question. A job cannot start without its topic, and the window policy belongs in the design, not after deployment. Why the correct answer wins: The source exists before the job, the window policy is chosen before deployment, and monitoring follows the running pipeline.

### Question 36 — C

Answer: Define a custom role with only the required permissions. A custom role expresses least privilege when no predefined role matches the job exactly. Local study-map skill 3.1 (IAM and Least Privilege), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 3 (security and compliance): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. A predefined role grants the curated permission set for one job at the level it is bound to. Why the correct answer wins: A custom role expresses least privilege when no predefined role matches the job exactly.
- **B:** Incorrect for this question. An API key identifies a project and does not authorise a user, so it cannot express least privilege. Why the correct answer wins: A custom role expresses least privilege when no predefined role matches the job exactly.
- **C:** Correct. In this case: A custom role expresses least privilege when no predefined role matches the job exactly.
- **D:** Incorrect for this question. A bastion is still an internet-facing host that must be patched and watched. Why the correct answer wins: A custom role expresses least privilege when no predefined role matches the job exactly.

### Question 37 — C

Answer: Give each service its own service account. A per-service identity keeps the blast radius of a leaked credential to one workload. Local study-map skill 3.1 (IAM and Least Privilege), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 3 (security and compliance): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. Labels attribute spend in billing export; they do not grant or restrict access. Why the correct answer wins: A per-service identity keeps the blast radius of a leaked credential to one workload.
- **B:** Incorrect for this question. A project is the boundary for quota, billing, and most IAM inheritance. Why the correct answer wins: A per-service identity keeps the blast radius of a leaked credential to one workload.
- **C:** Correct. In this case: A per-service identity keeps the blast radius of a leaked credential to one workload.
- **D:** Incorrect for this question. A key file is a long-lived credential that works until it is noticed and revoked. Why the correct answer wins: A per-service identity keeps the blast radius of a leaked credential to one workload.

### Question 38 — A

Answer: Create a folder per environment and bind roles there. A folder binding inherits to every project beneath it, so new projects start with the right access. Local study-map skill 3.2 (Resource Hierarchy and Organization Policy), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 3 (security and compliance): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Correct. In this case: A folder binding inherits to every project beneath it, so new projects start with the right access.
- **B:** Incorrect for this question. A predefined role grants the curated permission set for one job at the level it is bound to. Why the correct answer wins: A folder binding inherits to every project beneath it, so new projects start with the right access.
- **C:** Incorrect for this question. Labels attribute spend in billing export; they do not grant or restrict access. Why the correct answer wins: A folder binding inherits to every project beneath it, so new projects start with the right access.
- **D:** Incorrect for this question. A project is the boundary for quota, billing, and most IAM inheritance. Why the correct answer wins: A folder binding inherits to every project beneath it, so new projects start with the right access.

### Question 39 — A, C

Answers: Enforce the control with an organization policy constraint; Apply an IAM deny policy. The policy blocks the action across every project, and the deny policy overrides every allow beneath it. An organization policy blocks the action across every project regardless of who holds the role. A deny policy overrides every allow beneath it, which is how an exception is made impossible. Local study-map skill 3.2 (Resource Hierarchy and Organization Policy), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 3 (security and compliance): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Correct. A deny policy overrides every allow beneath it, which is how an exception is made impossible. In this case: The policy blocks the action across every project, and the deny policy overrides every allow beneath it.
- **B:** Incorrect for this question. A condition narrows when a grant applies, for example to a time window or a resource prefix. Why the correct answer wins: The policy blocks the action across every project, and the deny policy overrides every allow beneath it.
- **C:** Correct. An organization policy blocks the action across every project regardless of who holds the role. In this case: The policy blocks the action across every project, and the deny policy overrides every allow beneath it.
- **D:** Incorrect for this question. A folder binding inherits to every project beneath it, so new projects start with the right access. Why the correct answer wins: The policy blocks the action across every project, and the deny policy overrides every allow beneath it.
- **E:** Incorrect for this question. Labels attribute spend in billing export; they do not grant or restrict access. Why the correct answer wins: The policy blocks the action across every project, and the deny policy overrides every allow beneath it.

### Question 40 — D

Answer: Encrypt with a customer-managed key in Cloud KMS. A customer-managed key lets the bank rotate or disable the key and stop decryption at once. CMEK lets you control the key lifecycle, rotation, and the ability to revoke access to the data. Local study-map skill 3.3 (Encryption, CMEK, and Secrets), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 3 (security and compliance): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. Secret Manager versions the secret, controls access by IAM, and can rotate it. Why the correct answer wins: A customer-managed key lets the bank rotate or disable the key and stop decryption at once.
- **B:** Incorrect for this question. Cloud HSM keeps the key material in a hardware module that meets FIPS 140-2 level 3. Why the correct answer wins: A customer-managed key lets the bank rotate or disable the key and stop decryption at once.
- **C:** Incorrect for this question. CSEK is held by the caller and never stored by Google, so losing it loses the object. Why the correct answer wins: A customer-managed key lets the bank rotate or disable the key and stop decryption at once.
- **D:** Correct. CMEK lets you control the key lifecycle, rotation, and the ability to revoke access to the data. In this case: A customer-managed key lets the bank rotate or disable the key and stop decryption at once.

### Question 41 — C, E

Answers: Create the key ring in the same region as the data; Set an automatic rotation period on the key. The key ring's location fixes where the key material lives, and automatic rotation issues a new version on schedule. A regional key cannot encrypt a resource in another region, which is why residency drives key placement. Rotation issues a new key version on schedule and keeps old versions for decryption. Local study-map skill 3.3 (Encryption, CMEK, and Secrets), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 3 (security and compliance): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. Cloud HSM keeps the key material in a hardware module that meets FIPS 140-2 level 3. Why the correct answer wins: The key ring's location fixes where the key material lives, and automatic rotation issues a new version on schedule.
- **B:** Incorrect for this question. CSEK is held by the caller and never stored by Google, so losing it loses the object. Why the correct answer wins: The key ring's location fixes where the key material lives, and automatic rotation issues a new version on schedule.
- **C:** Correct. A regional key cannot encrypt a resource in another region, which is why residency drives key placement. In this case: The key ring's location fixes where the key material lives, and automatic rotation issues a new version on schedule.
- **D:** Incorrect for this question. An environment variable is visible to anything that can read the instance metadata or the process list. Why the correct answer wins: The key ring's location fixes where the key material lives, and automatic rotation issues a new version on schedule.
- **E:** Correct. Rotation issues a new key version on schedule and keeps old versions for decryption. In this case: The key ring's location fixes where the key material lives, and automatic rotation issues a new version on schedule.

### Question 42 — B

Answer: Put the projects inside a VPC Service Controls perimeter. A service perimeter blocks data movement out of the covered services even for a principal with the role. Local study-map skill 3.4 (VPC Service Controls and Network Security), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 3 (security and compliance): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. A deny policy overrides every allow beneath it, which is how an exception is made impossible. Why the correct answer wins: A service perimeter blocks data movement out of the covered services even for a principal with the role.
- **B:** Correct. In this case: A service perimeter blocks data movement out of the covered services even for a principal with the role.
- **C:** Incorrect for this question. Labels attribute spend in billing export; they do not grant or restrict access. Why the correct answer wins: A service perimeter blocks data movement out of the covered services even for a principal with the role.
- **D:** Incorrect for this question. A policy above the project applies to every current and future network beneath it. Why the correct answer wins: A service perimeter blocks data movement out of the covered services even for a principal with the role.

### Question 43 — B

Answer: Put Identity-Aware Proxy in front of the application. Identity-Aware Proxy authenticates and authorises each request before it reaches the backend. Local study-map skill 3.5 (Secure Remote Access and Zero Trust), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 3 (security and compliance): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. Cloud NAT lets private instances reach the internet without an external address. Why the correct answer wins: Identity-Aware Proxy authenticates and authorises each request before it reaches the backend.
- **B:** Correct. In this case: Identity-Aware Proxy authenticates and authorises each request before it reaches the backend.
- **C:** Incorrect for this question. Private Google Access reaches Google APIs from an internal address without a proxy or a NAT gateway. Why the correct answer wins: Identity-Aware Proxy authenticates and authorises each request before it reaches the backend.
- **D:** Incorrect for this question. A bastion is still an internet-facing host that must be patched and watched. Why the correct answer wins: Identity-Aware Proxy authenticates and authorises each request before it reaches the backend.

### Question 44 — A, D

Answers: Use Workload Identity Federation for the external pipeline; Use OS Login for administrative SSH. Federation exchanges an external token for short-lived credentials, and OS Login ties SSH to the IAM account. Federation exchanges an external token for short-lived Google Cloud credentials, so no key leaves the provider. OS Login ties the SSH identity to the IAM account and records the session. Local study-map skill 3.5 (Secure Remote Access and Zero Trust), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 3 (security and compliance): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Correct. OS Login ties the SSH identity to the IAM account and records the session. In this case: Federation exchanges an external token for short-lived credentials, and OS Login ties SSH to the IAM account.
- **B:** Incorrect for this question. An environment variable is visible to anything that can read the instance metadata or the process list. Why the correct answer wins: Federation exchanges an external token for short-lived credentials, and OS Login ties SSH to the IAM account.
- **C:** Incorrect for this question. A key file is a long-lived credential that works until it is noticed and revoked. Why the correct answer wins: Federation exchanges an external token for short-lived credentials, and OS Login ties SSH to the IAM account.
- **D:** Correct. Federation exchanges an external token for short-lived Google Cloud credentials, so no key leaves the provider. In this case: Federation exchanges an external token for short-lived credentials, and OS Login ties SSH to the IAM account.
- **E:** Incorrect for this question. An API key identifies a project and does not authorise a user, so it cannot express least privilege. Why the correct answer wins: Federation exchanges an external token for short-lived credentials, and OS Login ties SSH to the IAM account.

### Question 45 — A

Answer: Require Binary Authorization attestations. The admission controller rejects images without a valid attestation, so an unverified build cannot start. Only images with a valid attestation from a trusted builder may deploy. Local study-map skill 3.6 (Software Supply Chain Security), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 3 (security and compliance): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Correct. Only images with a valid attestation from a trusted builder may deploy. In this case: The admission controller rejects images without a valid attestation, so an unverified build cannot start.
- **B:** Incorrect for this question. Network policy restricts pod-to-pod traffic inside the cluster, which a firewall rule cannot see. Why the correct answer wins: The admission controller rejects images without a valid attestation, so an unverified build cannot start.
- **C:** Incorrect for this question. Artifact Registry holds the image with IAM-scoped access and vulnerability metadata. Why the correct answer wins: The admission controller rejects images without a valid attestation, so an unverified build cannot start.
- **D:** Incorrect for this question. Scanning reports known vulnerabilities in the image layers before deployment. Why the correct answer wins: The admission controller rejects images without a valid attestation, so an unverified build cannot start.

### Question 46 — D

Answer: De-identify the data with Sensitive Data Protection. Sensitive Data Protection finds and redacts or tokenizes the sensitive fields before they are stored. Sensitive Data Protection finds and redacts, tokenizes, or format-preservingly encrypts sensitive fields. Local study-map skill 3.7 (Securing AI Workloads), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 3 (security and compliance): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. The access level adds device and network conditions to the perimeter rule. Why the correct answer wins: Sensitive Data Protection finds and redacts or tokenizes the sensitive fields before they are stored.
- **B:** Incorrect for this question. Model Armor detects prompt injection, jailbreak attempts, and unsafe content before and after the model call. Why the correct answer wins: Sensitive Data Protection finds and redacts or tokenizes the sensitive fields before they are stored.
- **C:** Incorrect for this question. Security Command Center aggregates misconfiguration and threat findings across the organization. Why the correct answer wins: Sensitive Data Protection finds and redacts or tokenizes the sensitive fields before they are stored.
- **D:** Correct. Sensitive Data Protection finds and redacts, tokenizes, or format-preservingly encrypts sensitive fields. In this case: Sensitive Data Protection finds and redacts or tokenizes the sensitive fields before they are stored.

### Question 47 — A

Answer: Enable Data Access audit logs. Data Access logging is off by default and must be enabled before reads and writes are recorded. Local study-map skill 3.8 (Compliance, Residency, and Audit Logging), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 3 (security and compliance): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Correct. In this case: Data Access logging is off by default and must be enabled before reads and writes are recorded.
- **B:** Incorrect for this question. Admin Activity records configuration changes and cannot be disabled. Why the correct answer wins: Data Access logging is off by default and must be enabled before reads and writes are recorded.
- **C:** Incorrect for this question. Access Transparency records when Google staff access your content, which is evidence of oversight, not of user activity. Why the correct answer wins: Data Access logging is off by default and must be enabled before reads and writes are recorded.
- **D:** Incorrect for this question. The metric turns a log pattern into a series that can be alerted on and charted. Why the correct answer wins: Data Access logging is off by default and must be enabled before reads and writes are recorded.

### Question 48 — C

Answer: Use a locked log bucket with a fixed retention. A locked bucket prevents deletion and retention changes for the period the auditor requires. Local study-map skill 3.8 (Compliance, Residency, and Audit Logging), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 3 (security and compliance): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. A locked retention policy prevents deletion or shortening, which is what an auditor tests. Why the correct answer wins: A locked bucket prevents deletion and retention changes for the period the auditor requires.
- **B:** Incorrect for this question. The metric turns a log pattern into a series that can be alerted on and charted. Why the correct answer wins: A locked bucket prevents deletion and retention changes for the period the auditor requires.
- **C:** Correct. In this case: A locked bucket prevents deletion and retention changes for the period the auditor requires.
- **D:** Incorrect for this question. Admin Activity records configuration changes and cannot be disabled. Why the correct answer wins: A locked bucket prevents deletion and retention changes for the period the auditor requires.

### Question 49 — B

Answer: Enable data access audit logs for the services in scope → create a locked log bucket with the required retention → route the logs with an aggregated sink → query and export the evidence for the auditor. Logs must be enabled before they can be routed, and retention is fixed on the bucket before the sink writes to it. Local study-map skill 3.8 (Compliance, Residency, and Audit Logging), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 3 (security and compliance): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. There is no evidence to query before logging and routing exist. Why the correct answer wins: Logs must be enabled before they can be routed, and retention is fixed on the bucket before the sink writes to it.
- **B:** Correct. In this case: Logs must be enabled before they can be routed, and retention is fixed on the bucket before the sink writes to it.
- **C:** Incorrect for this question. A sink without a destination bucket or enabled logs captures nothing. Why the correct answer wins: Logs must be enabled before they can be routed, and retention is fixed on the bucket before the sink writes to it.
- **D:** Incorrect for this question. A sink that is created last is needed before any evidence can be queried from the destination. Why the correct answer wins: Logs must be enabled before they can be routed, and retention is fixed on the bucket before the sink writes to it.

### Question 50 — B

Answer: Require a reviewed pull request and a passing plan. The gate makes a second person check the change and its plan before it can apply. Local study-map skill 4.1 (SDLC and CI/CD Design), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 4 (analyzing and optimizing): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. A rebuild produces a different artifact, so the test result no longer applies to production. Why the correct answer wins: The gate makes a second person check the change and its plan before it can apply.
- **B:** Correct. In this case: The gate makes a second person check the change and its plan before it can apply.
- **C:** Incorrect for this question. Short branches reduce merge conflict and keep the mainline deployable. Why the correct answer wins: The gate makes a second person check the change and its plan before it can apply.
- **D:** Incorrect for this question. A rolling replacement keeps capacity but exposes the whole fleet before the signal is trusted. Why the correct answer wins: The gate makes a second person check the change and its plan before it can apply.

### Question 51 — B

Answer: Adopt trunk-based development with short-lived branches. Short-lived branches reduce merge conflict and keep the mainline deployable. Local study-map skill 4.1 (SDLC and CI/CD Design), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 4 (analyzing and optimizing): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. The flag separates deployment from release, so the code can ship dark and be turned off instantly. Why the correct answer wins: Short-lived branches reduce merge conflict and keep the mainline deployable.
- **B:** Correct. In this case: Short-lived branches reduce merge conflict and keep the mainline deployable.
- **C:** Incorrect for this question. A rebuild produces a different artifact, so the test result no longer applies to production. Why the correct answer wins: Short-lived branches reduce merge conflict and keep the mainline deployable.
- **D:** Incorrect for this question. A rolling replacement keeps capacity but exposes the whole fleet before the signal is trusted. Why the correct answer wins: Short-lived branches reduce merge conflict and keep the mainline deployable.

### Question 52 — D

Answer: Query the entries in Cloud Logging. Logging holds the event text and structured fields that explain what happened at that moment. Local study-map skill 4.2 (Root Cause Analysis), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 4 (analyzing and optimizing): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. Recommender reports idle and over-provisioned resources with the estimated saving. Why the correct answer wins: Logging holds the event text and structured fields that explain what happened at that moment.
- **B:** Incorrect for this question. The dashboard gives the team one view of the same signals during an incident. Why the correct answer wins: Logging holds the event text and structured fields that explain what happened at that moment.
- **C:** Incorrect for this question. Trace shows how one request spent its time across services and calls. Why the correct answer wins: Logging holds the event text and structured fields that explain what happened at that moment.
- **D:** Correct. In this case: Logging holds the event text and structured fields that explain what happened at that moment.

### Question 53 — A, B

Answers: Inspect the trace waterfall in Cloud Trace; Group the exceptions in Error Reporting. Trace shows how one request spent its time, and Error Reporting clusters the recurring stack traces. Trace shows how one request spent its time across services and calls. Error Reporting clusters recurring stack traces so a new failure is not lost in the log volume. Local study-map skill 4.2 (Root Cause Analysis), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 4 (analyzing and optimizing): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Correct. Trace shows how one request spent its time across services and calls. In this case: Trace shows how one request spent its time, and Error Reporting clusters the recurring stack traces.
- **B:** Correct. Error Reporting clusters recurring stack traces so a new failure is not lost in the log volume. In this case: Trace shows how one request spent its time, and Error Reporting clusters the recurring stack traces.
- **C:** Incorrect for this question. The dashboard gives the team one view of the same signals during an incident. Why the correct answer wins: Trace shows how one request spent its time, and Error Reporting clusters the recurring stack traces.
- **D:** Incorrect for this question. The runbook records the diagnostic steps so the response does not depend on who is awake. Why the correct answer wins: Trace shows how one request spent its time, and Error Reporting clusters the recurring stack traces.
- **E:** Incorrect for this question. An SLO ties the alert to the promise the users care about rather than to a raw resource threshold. Why the correct answer wins: Trace shows how one request spent its time, and Error Reporting clusters the recurring stack traces.

### Question 54 — A

Answer: Run a load test at the expected peak. The load test measures the system at the concurrency the business expects, before launch. Local study-map skill 4.3 (Testing and Validation), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 4 (analyzing and optimizing): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Correct. In this case: The load test measures the system at the concurrency the business expects, before launch.
- **B:** Incorrect for this question. An independent test attempts the attack the design claims to prevent. Why the correct answer wins: The load test measures the system at the concurrency the business expects, before launch.
- **C:** Incorrect for this question. The experiment proves the failover path works while the impact is controlled. Why the correct answer wins: The load test measures the system at the concurrency the business expects, before launch.
- **D:** Incorrect for this question. The pyramid puts volume where it is cheap and keeps end-to-end tests for the critical paths. Why the correct answer wins: The load test measures the system at the concurrency the business expects, before launch.

### Question 55 — B

Answer: Add a contract test on the API. The contract test fails the build when a breaking change reaches a consumer. Local study-map skill 4.3 (Testing and Validation), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 4 (analyzing and optimizing): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. The load test measures the system at the concurrency the business expects, before launch. Why the correct answer wins: The contract test fails the build when a breaking change reaches a consumer.
- **B:** Correct. In this case: The contract test fails the build when a breaking change reaches a consumer.
- **C:** Incorrect for this question. The pyramid puts volume where it is cheap and keeps end-to-end tests for the critical paths. Why the correct answer wins: The contract test fails the build when a breaking change reaches a consumer.
- **D:** Incorrect for this question. An independent test attempts the attack the design claims to prevent. Why the correct answer wins: The contract test fails the build when a breaking change reaches a consumer.

### Question 56 — C

Answer: Run a warm standby at reduced capacity. A running but smaller copy recovers in a short window at a continuous cost. Local study-map skill 4.4 (Disaster Recovery and Business Continuity), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 4 (analyzing and optimizing): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. Restoring from backup is the cheapest option and the slowest to recover. Why the correct answer wins: A running but smaller copy recovers in a short window at a continuous cost.
- **B:** Incorrect for this question. Both regions serve traffic, so a regional loss is absorbed without a failover decision. Why the correct answer wins: A running but smaller copy recovers in a short window at a continuous cost.
- **C:** Correct. In this case: A running but smaller copy recovers in a short window at a continuous cost.
- **D:** Incorrect for this question. Only the core data and configuration stay warm, so recovery starts the compute and takes minutes. Why the correct answer wins: A running but smaller copy recovers in a short window at a continuous cost.

### Question 57 — D

Answer: Act on the Recommender suggestions. Recommender reports idle and over-provisioned resources with the estimated saving for each. Local study-map skill 4.5 (Cost Optimization), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 4 (analyzing and optimizing): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. Labels attribute spend in billing export; they do not grant or restrict access. Why the correct answer wins: Recommender reports idle and over-provisioned resources with the estimated saving for each.
- **B:** Incorrect for this question. A budget alerts on spend but does not stop it. Why the correct answer wins: Recommender reports idle and over-provisioned resources with the estimated saving for each.
- **C:** Incorrect for this question. The export attributes cost to the team and service that caused it. Why the correct answer wins: Recommender reports idle and over-provisioned resources with the estimated saving for each.
- **D:** Correct. In this case: Recommender reports idle and over-provisioned resources with the estimated saving for each.

### Question 58 — A

Answer: Inspect the query plan and bytes processed → partition and cluster the table on the filter columns → rewrite the query to prune partitions → measure the new slot time and bytes scanned. The plan identifies the problem, the physical design supports pruning, and only a measurement proves improvement. Local study-map skill 4.5 (Cost Optimization), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 4 (analyzing and optimizing): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Correct. In this case: The plan identifies the problem, the physical design supports pruning, and only a measurement proves improvement.
- **B:** Incorrect for this question. The plan is the evidence that drives both the rewrite and the physical design. Why the correct answer wins: The plan identifies the problem, the physical design supports pruning, and only a measurement proves improvement.
- **C:** Incorrect for this question. Measuring before any change establishes no baseline against the plan. Why the correct answer wins: The plan identifies the problem, the physical design supports pruning, and only a measurement proves improvement.
- **D:** Incorrect for this question. Partitioning last ignores what the plan and the rewrite revealed. Why the correct answer wins: The plan identifies the problem, the physical design supports pruning, and only a measurement proves improvement.

### Question 59 — D

Answer: Agree the decision rights with the stakeholders. Naming who decides each trade-off prevents the design being reopened late in delivery. Local study-map skill 4.6 (Stakeholder and Change Management), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 4 (analyzing and optimizing): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. The runbook records the diagnostic steps so the response does not depend on who is awake. Why the correct answer wins: Naming who decides each trade-off prevents the design being reopened late in delivery.
- **B:** Incorrect for this question. The board reviews risk and timing for changes that affect regulated or shared systems. Why the correct answer wins: Naming who decides each trade-off prevents the design being reopened late in delivery.
- **C:** Incorrect for this question. A catalog entry gives teams a pre-approved, policy-compliant way to request the resource. Why the correct answer wins: Naming who decides each trade-off prevents the design being reopened late in delivery.
- **D:** Correct. In this case: Naming who decides each trade-off prevents the design being reopened late in delivery.

### Question 60 — D

Answer: Publish a service catalog entry with an approved template. A catalog entry gives teams a pre-approved, policy-compliant way to request the resource. Local study-map skill 4.7 (Service Catalog and Provisioning), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 4 (analyzing and optimizing): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. Labels attribute spend in billing export; they do not grant or restrict access. Why the correct answer wins: A catalog entry gives teams a pre-approved, policy-compliant way to request the resource.
- **B:** Incorrect for this question. Terraform holds desired state in code, plans the diff, and applies it through a provider. Why the correct answer wins: A catalog entry gives teams a pre-approved, policy-compliant way to request the resource.
- **C:** Incorrect for this question. An organization policy blocks the action across every project regardless of who holds the role. Why the correct answer wins: A catalog entry gives teams a pre-approved, policy-compliant way to request the resource.
- **D:** Correct. In this case: A catalog entry gives teams a pre-approved, policy-compliant way to request the resource.

### Question 61 — D

Answer: Record the risk and its owner in a risk register. The register keeps the decision visible to the people who carry the consequence. Local study-map skill 4.6 (Stakeholder and Change Management), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 4 (analyzing and optimizing): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. The board reviews risk and timing for changes that affect regulated or shared systems. Why the correct answer wins: The register keeps the decision visible to the people who carry the consequence.
- **B:** Incorrect for this question. A catalog entry gives teams a pre-approved, policy-compliant way to request the resource. Why the correct answer wins: The register keeps the decision visible to the people who carry the consequence.
- **C:** Incorrect for this question. The runbook records the diagnostic steps so the response does not depend on who is awake. Why the correct answer wins: The register keeps the decision visible to the people who carry the consequence.
- **D:** Correct. In this case: The register keeps the decision visible to the people who carry the consequence.

### Question 62 — A

Answer: Put the change behind a feature flag. The flag separates deployment from release, so the code can ship dark and be turned off instantly. Local study-map skill 5.1 (Deployment and Release Strategy), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 5 (managing implementation): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Correct. In this case: The flag separates deployment from release, so the code can ship dark and be turned off instantly.
- **B:** Incorrect for this question. Two identical environments let the switch be reversed instantly if the new one misbehaves. Why the correct answer wins: The flag separates deployment from release, so the code can ship dark and be turned off instantly.
- **C:** Incorrect for this question. A canary limits the blast radius while the error and latency signals are compared. Why the correct answer wins: The flag separates deployment from release, so the code can ship dark and be turned off instantly.
- **D:** Incorrect for this question. A rolling replacement keeps capacity but exposes the whole fleet before the signal is trusted. Why the correct answer wins: The flag separates deployment from release, so the code can ship dark and be turned off instantly.

### Question 63 — C, E

Answers: Deploy blue/green with a traffic switch; Keep the previous image digest ready for rollback. Two environments let the switch be reversed instantly, and a pinned digest restores the exact artifact. Two identical environments let the switch be reversed instantly if the new one misbehaves. A pinned digest restores the exact artifact that was known good, not a rebuild of it. Local study-map skill 5.1 (Deployment and Release Strategy), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 5 (managing implementation): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. A budget alerts on spend but does not stop it. Why the correct answer wins: Two environments let the switch be reversed instantly, and a pinned digest restores the exact artifact.
- **B:** Incorrect for this question. A rebuild produces a different artifact, so the test result no longer applies to production. Why the correct answer wins: Two environments let the switch be reversed instantly, and a pinned digest restores the exact artifact.
- **C:** Correct. A pinned digest restores the exact artifact that was known good, not a rebuild of it. In this case: Two environments let the switch be reversed instantly, and a pinned digest restores the exact artifact.
- **D:** Incorrect for this question. Promotion moves one immutable artifact forward, so what was tested is what runs. Why the correct answer wins: Two environments let the switch be reversed instantly, and a pinned digest restores the exact artifact.
- **E:** Correct. Two identical environments let the switch be reversed instantly if the new one misbehaves. In this case: Two environments let the switch be reversed instantly, and a pinned digest restores the exact artifact.

### Question 64 — A

Answer: Build an immutable image and record its digest → deploy the new revision without traffic → shift a small traffic percentage and watch error and latency signals → promote to full traffic or roll back to the pinned digest. The artifact is fixed before traffic moves, and the decision to promote follows observed signals. Local study-map skill 5.1 (Deployment and Release Strategy), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 5 (managing implementation): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Correct. In this case: The artifact is fixed before traffic moves, and the decision to promote follows observed signals.
- **B:** Incorrect for this question. Promoting before the canary step skips the signal that justifies promotion. Why the correct answer wins: The artifact is fixed before traffic moves, and the decision to promote follows observed signals.
- **C:** Incorrect for this question. Full traffic before any canary step turns the first failure into an outage. Why the correct answer wins: The artifact is fixed before traffic moves, and the decision to promote follows observed signals.
- **D:** Incorrect for this question. Nothing can be watched before the revision exists, and the image precedes the deployment. Why the correct answer wins: The artifact is fixed before traffic moves, and the decision to promote follows observed signals.

### Question 65 — A

Answer: Publish the API through Apigee. Apigee adds quotas, keys, mediation, and analytics at the gateway for each consumer. Local study-map skill 5.2 (API Management), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 5 (managing implementation): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Correct. In this case: Apigee adds quotas, keys, mediation, and analytics at the gateway for each consumer.
- **B:** Incorrect for this question. Cloud Armor filters requests at the edge with allow and deny rules and adaptive protection. Why the correct answer wins: Apigee adds quotas, keys, mediation, and analytics at the gateway for each consumer.
- **C:** Incorrect for this question. Endpoints validates and monitors an API described by an OpenAPI or gRPC spec. Why the correct answer wins: Apigee adds quotas, keys, mediation, and analytics at the gateway for each consumer.
- **D:** Incorrect for this question. API Gateway fronts a Cloud Run or functions backend with a managed OpenAPI definition. Why the correct answer wins: Apigee adds quotas, keys, mediation, and analytics at the gateway for each consumer.

### Question 66 — C

Answer: Use API Gateway. API Gateway fronts a Cloud Run or functions backend with a managed OpenAPI definition. Local study-map skill 5.2 (API Management), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 5 (managing implementation): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. Endpoints validates and monitors an API described by an OpenAPI or gRPC spec. Why the correct answer wins: API Gateway fronts a Cloud Run or functions backend with a managed OpenAPI definition.
- **B:** Incorrect for this question. Cloud Armor filters requests at the edge with allow and deny rules and adaptive protection. Why the correct answer wins: API Gateway fronts a Cloud Run or functions backend with a managed OpenAPI definition.
- **C:** Correct. In this case: API Gateway fronts a Cloud Run or functions backend with a managed OpenAPI definition.
- **D:** Incorrect for this question. Apigee adds quotas, keys, mediation, and analytics at the gateway. Why the correct answer wins: API Gateway fronts a Cloud Run or functions backend with a managed OpenAPI definition.

### Question 67 — B

Answer: Migrate the database with Database Migration Service. The service replicates continuously and cuts over in a short window with the source still running. Local study-map skill 5.3 (Data and System Migration Tooling), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 5 (managing implementation): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. The service runs scheduled loads from SaaS sources and other clouds into BigQuery. Why the correct answer wins: The service replicates continuously and cuts over in a short window with the source still running.
- **B:** Correct. In this case: The service replicates continuously and cuts over in a short window with the source still running.
- **C:** Incorrect for this question. Datastream reads the source log and streams inserts, updates, and deletes with ordering preserved. Why the correct answer wins: The service replicates continuously and cuts over in a short window with the source still running.
- **D:** Incorrect for this question. The service moves object data between buckets or clouds on a schedule. Why the correct answer wins: The service replicates continuously and cuts over in a short window with the source still running.

### Question 68 — A

Answer: Convert the VMs with Migrate to Containers. The tool rewrites a VM workload into a container image so it can run on GKE. Local study-map skill 5.3 (Data and System Migration Tooling), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 5 (managing implementation): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Correct. In this case: The tool rewrites a VM workload into a container image so it can run on GKE.
- **B:** Incorrect for this question. The service moves object data between buckets or clouds on a schedule. Why the correct answer wins: The tool rewrites a VM workload into a container image so it can run on GKE.
- **C:** Incorrect for this question. VMware Engine keeps the existing hypervisor and operations model while moving the hardware into Google Cloud. Why the correct answer wins: The tool rewrites a VM workload into a container image so it can run on GKE.
- **D:** Incorrect for this question. Migration Center inventories the servers and estimates the target size and cost. Why the correct answer wins: The tool rewrites a VM workload into a container image so it can run on GKE.

### Question 69 — C

Answer: Inventory the estate in Migration Center → group servers into dependency-based waves → validate a pilot wave in the target landing zone → cut over wave by wave and decommission the source. Inventory precedes grouping, a pilot proves the landing zone, and decommissioning follows a completed cutover. Local study-map skill 5.3 (Data and System Migration Tooling), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 5 (managing implementation): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. Decommissioning first removes the evidence and the rollback option for every later step. Why the correct answer wins: Inventory precedes grouping, a pilot proves the landing zone, and decommissioning follows a completed cutover.
- **B:** Incorrect for this question. A pilot cannot be chosen before the inventory and the wave grouping. Why the correct answer wins: Inventory precedes grouping, a pilot proves the landing zone, and decommissioning follows a completed cutover.
- **C:** Correct. In this case: Inventory precedes grouping, a pilot proves the landing zone, and decommissioning follows a completed cutover.
- **D:** Incorrect for this question. Waves cannot be grouped before the inventory, and decommissioning before validation destroys the rollback path. Why the correct answer wins: Inventory precedes grouping, a pilot proves the landing zone, and decommissioning follows a completed cutover.

### Question 70 — B

Answer: Run the emulator in the pipeline. The emulator provides a local endpoint for tests without a billable cloud resource. Local study-map skill 5.4 (Programmatic Access and Emulators), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 5 (managing implementation): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. Cloud Build executes the pipeline steps in a managed, isolated worker with recorded provenance. Why the correct answer wins: The emulator provides a local endpoint for tests without a billable cloud resource.
- **B:** Correct. In this case: The emulator provides a local endpoint for tests without a billable cloud resource.
- **C:** Incorrect for this question. The CLI exposes every API as a command that can be scripted and logged. Why the correct answer wins: The emulator provides a local endpoint for tests without a billable cloud resource.
- **D:** Incorrect for this question. Terraform holds desired state in code, plans the diff, and applies it through a provider. Why the correct answer wins: The emulator provides a local endpoint for tests without a billable cloud resource.

### Question 71 — B

Answer: Use the Google API client library with retries. The client library applies the recommended retry and backoff behaviour for the API. Local study-map skill 5.5 (Client Libraries and API Practices), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 5 (managing implementation): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. The CLI exposes every API as a command that can be scripted and logged. Why the correct answer wins: The client library applies the recommended retry and backoff behaviour for the API.
- **B:** Correct. In this case: The client library applies the recommended retry and backoff behaviour for the API.
- **C:** Incorrect for this question. Impersonation issues a short-lived token so the test runs as the real workload identity. Why the correct answer wins: The client library applies the recommended retry and backoff behaviour for the API.
- **D:** Incorrect for this question. An API key identifies a project and does not authorise a user, so it cannot express least privilege. Why the correct answer wins: The client library applies the recommended retry and backoff behaviour for the API.

### Question 72 — B

Answer: Install the Ops Agent on the instances. The Ops Agent ships host metrics and application logs to Monitoring and Logging. Local study-map skill 6.1 (Observability Design), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 6 (solution and operations excellence): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. Trace shows how one request spent its time across services and calls. Why the correct answer wins: The Ops Agent ships host metrics and application logs to Monitoring and Logging.
- **B:** Correct. In this case: The Ops Agent ships host metrics and application logs to Monitoring and Logging.
- **C:** Incorrect for this question. Error Reporting clusters recurring stack traces so a new failure is not lost in the log volume. Why the correct answer wins: The Ops Agent ships host metrics and application logs to Monitoring and Logging.
- **D:** Incorrect for this question. Profiler samples the running code and attributes CPU and heap to the functions responsible. Why the correct answer wins: The Ops Agent ships host metrics and application logs to Monitoring and Logging.

### Question 73 — A

Answer: Define an SLO with an error budget. An SLO ties the alert to the user promise rather than to a raw resource threshold. Local study-map skill 6.2 (Alerting and Service Level Objectives), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 6 (solution and operations excellence): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Correct. In this case: An SLO ties the alert to the user promise rather than to a raw resource threshold.
- **B:** Incorrect for this question. The dashboard gives the team one view of the same signals during an incident. Why the correct answer wins: An SLO ties the alert to the user promise rather than to a raw resource threshold.
- **C:** Incorrect for this question. The check measures availability from outside, which no internal metric can prove. Why the correct answer wins: An SLO ties the alert to the user promise rather than to a raw resource threshold.
- **D:** Incorrect for this question. The policy fires when the series crosses the condition for the stated duration. Why the correct answer wins: An SLO ties the alert to the user promise rather than to a raw resource threshold.

### Question 74 — A, E

Answers: Create an alerting policy on the metric; Create a log-based metric. The metric turns the log pattern into a series, and the policy fires when it crosses the condition. The policy fires when the series crosses the condition for the stated duration. The metric turns a log pattern into a series that can be alerted on and charted. Local study-map skill 6.2 (Alerting and Service Level Objectives), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 6 (solution and operations excellence): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Correct. The policy fires when the series crosses the condition for the stated duration. In this case: The metric turns the log pattern into a series, and the policy fires when it crosses the condition.
- **B:** Incorrect for this question. Recommender reports idle and over-provisioned resources with the estimated saving. Why the correct answer wins: The metric turns the log pattern into a series, and the policy fires when it crosses the condition.
- **C:** Incorrect for this question. An SLO ties the alert to the promise the users care about rather than to a raw resource threshold. Why the correct answer wins: The metric turns the log pattern into a series, and the policy fires when it crosses the condition.
- **D:** Incorrect for this question. The dashboard gives the team one view of the same signals during an incident. Why the correct answer wins: The metric turns the log pattern into a series, and the policy fires when it crosses the condition.
- **E:** Correct. The metric turns a log pattern into a series that can be alerted on and charted. In this case: The metric turns the log pattern into a series, and the policy fires when it crosses the condition.

### Question 75 — D

Answer: Publish a runbook per alert. The runbook records the diagnostic steps so the response does not depend on who is awake. Local study-map skill 6.3 (Release Management and Support), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 6 (solution and operations excellence): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. The support tier sets the response time and the escalation path the business expects. Why the correct answer wins: The runbook records the diagnostic steps so the response does not depend on who is awake.
- **B:** Incorrect for this question. A named rotation turns an alert into a person who is already accountable for it. Why the correct answer wins: The runbook records the diagnostic steps so the response does not depend on who is awake.
- **C:** Incorrect for this question. The dashboard gives the team one view of the same signals during an incident. Why the correct answer wins: The runbook records the diagnostic steps so the response does not depend on who is awake.
- **D:** Correct. In this case: The runbook records the diagnostic steps so the response does not depend on who is awake.

### Question 76 — D

Answer: Define an on-call rotation with an escalation path. A named rotation turns an alert into a person who is already accountable for it. Local study-map skill 6.3 (Release Management and Support), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 6 (solution and operations excellence): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. The contract converts an internal target into an obligation with a consequence. Why the correct answer wins: A named rotation turns an alert into a person who is already accountable for it.
- **B:** Incorrect for this question. The runbook records the diagnostic steps so the response does not depend on who is awake. Why the correct answer wins: A named rotation turns an alert into a person who is already accountable for it.
- **C:** Incorrect for this question. The support tier sets the response time and the escalation path the business expects. Why the correct answer wins: A named rotation turns an alert into a person who is already accountable for it.
- **D:** Correct. In this case: A named rotation turns an alert into a person who is already accountable for it.

### Question 77 — C

Answer: Run a chaos experiment against a zone. The experiment proves the failover path works while the impact is controlled. Local study-map skill 6.4 (Reliability Testing), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 6 (solution and operations excellence): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. An independent test attempts the attack the design claims to prevent. Why the correct answer wins: The experiment proves the failover path works while the impact is controlled.
- **B:** Incorrect for this question. The load test measures the system at the concurrency the business expects, before launch. Why the correct answer wins: The experiment proves the failover path works while the impact is controlled.
- **C:** Correct. In this case: The experiment proves the failover path works while the impact is controlled.
- **D:** Incorrect for this question. A canary limits the blast radius while the error and latency signals are compared. Why the correct answer wins: The experiment proves the failover path works while the impact is controlled.

### Question 78 — C

Answer: Write a blameless postmortem with actions. The postmortem records cause and follow-up work, which is how the same failure is prevented. Local study-map skill 6.5 (Operational Excellence and Quality Control), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 6 (solution and operations excellence): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. The runbook records the diagnostic steps so the response does not depend on who is awake. Why the correct answer wins: The postmortem records cause and follow-up work, which is how the same failure is prevented.
- **B:** Incorrect for this question. The dashboard gives the team one view of the same signals during an incident. Why the correct answer wins: The postmortem records cause and follow-up work, which is how the same failure is prevented.
- **C:** Correct. In this case: The postmortem records cause and follow-up work, which is how the same failure is prevented.
- **D:** Incorrect for this question. The support tier sets the response time and the escalation path the business expects. Why the correct answer wins: The postmortem records cause and follow-up work, which is how the same failure is prevented.

### Question 79 — A

Answer: Match the support plan to the recovery commitment. The support tier sets the response time and the escalation path the business expects. Local study-map skill 6.5 (Operational Excellence and Quality Control), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 6 (solution and operations excellence): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Correct. In this case: The support tier sets the response time and the escalation path the business expects.
- **B:** Incorrect for this question. The contract converts an internal target into an obligation with a consequence. Why the correct answer wins: The support tier sets the response time and the escalation path the business expects.
- **C:** Incorrect for this question. The runbook records the diagnostic steps so the response does not depend on who is awake. Why the correct answer wins: The support tier sets the response time and the escalation path the business expects.
- **D:** Incorrect for this question. A named rotation turns an alert into a person who is already accountable for it. Why the correct answer wins: The support tier sets the response time and the escalation path the business expects.

### Question 80 — B

Answer: Detect the symptom through an alert → contain the impact and restore service → isolate the root cause from logs, traces, and metrics → apply the permanent fix and write the postmortem. Service recovery comes before deep analysis, and the postmortem follows the fix. Local study-map skill 6.5 (Operational Excellence and Quality Control), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 6 (solution and operations excellence): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. Detection precedes analysis, and the postmortem follows restoration rather than preceding it. Why the correct answer wins: Service recovery comes before deep analysis, and the postmortem follows the fix.
- **B:** Correct. In this case: Service recovery comes before deep analysis, and the postmortem follows the fix.
- **C:** Incorrect for this question. Service cannot be restored before the alert fires, and the root cause is isolated before the postmortem. Why the correct answer wins: Service recovery comes before deep analysis, and the postmortem follows the fix.
- **D:** Incorrect for this question. A postmortem cannot be written before the incident has happened and been resolved. Why the correct answer wins: Service recovery comes before deep analysis, and the postmortem follows the fix.

### Question 81 — D

Answer: Assess the estate in Migration Center. Migration Center inventories the estate and estimates target size and cost before a plan is funded. Migration Center inventories the servers and estimates the target size and cost. Local study-map skill 1.9 (Migration Planning and Future Improvement), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 1 (designing and planning): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. The service moves a database with continuous replication and a short cutover window. Why the correct answer wins: Migration Center inventories the estate and estimates target size and cost before a plan is funded.
- **B:** Incorrect for this question. The service moves object data between buckets or clouds on a schedule. Why the correct answer wins: Migration Center inventories the estate and estimates target size and cost before a plan is funded.
- **C:** Incorrect for this question. The tool rewrites a VM workload into a container image so it can run on GKE. Why the correct answer wins: Migration Center inventories the estate and estimates target size and cost before a plan is funded.
- **D:** Correct. Migration Center inventories the servers and estimates the target size and cost. In this case: Migration Center inventories the estate and estimates target size and cost before a plan is funded.

### Question 82 — C

Answer: Use VM Manager for OS patch compliance. VM Manager inventories and applies patches across the fleet instead of relying on manual runs. Local study-map skill 2.3 (Compute Provisioning and Patch Management), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 2 (managing and provisioning): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. Custom vCPU and memory avoid paying for a fixed shape that over-provisions one dimension. Why the correct answer wins: VM Manager inventories and applies patches across the fleet instead of relying on manual runs.
- **B:** Incorrect for this question. Spot capacity costs far less but can be reclaimed with 30 seconds of notice. Why the correct answer wins: VM Manager inventories and applies patches across the fleet instead of relying on manual runs.
- **C:** Correct. In this case: VM Manager inventories and applies patches across the fleet instead of relying on manual runs.
- **D:** Incorrect for this question. Config Connector reconciles Google Cloud resources from Kubernetes manifests alongside the workloads. Why the correct answer wins: VM Manager inventories and applies patches across the fleet instead of relying on manual runs.

### Question 83 — C, E

Answers: Require a reviewed pull request and a passing plan; Promote the same tested artifact between environments. The gate makes review mandatory, and promotion keeps one immutable artifact. The gate makes a second person check the change and its plan before it can apply. Promotion moves one immutable artifact forward, so what was tested is what runs. Local study-map skill 4.1 (SDLC and CI/CD Design), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 4 (analyzing and optimizing): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. A rolling replacement keeps capacity but exposes the whole fleet before the signal is trusted. Why the correct answer wins: The gate makes review mandatory, and promotion keeps one immutable artifact.
- **B:** Incorrect for this question. A rebuild produces a different artifact, so the test result no longer applies to production. Why the correct answer wins: The gate makes review mandatory, and promotion keeps one immutable artifact.
- **C:** Correct. Promotion moves one immutable artifact forward, so what was tested is what runs. In this case: The gate makes review mandatory, and promotion keeps one immutable artifact.
- **D:** Incorrect for this question. A budget alerts on spend but does not stop it. Why the correct answer wins: The gate makes review mandatory, and promotion keeps one immutable artifact.
- **E:** Correct. The gate makes a second person check the change and its plan before it can apply. In this case: The gate makes review mandatory, and promotion keeps one immutable artifact.

### Question 84 — C

Answer: Match the support plan to the recovery commitment. The support tier sets the response time and the escalation path the business expects. Local study-map skill 6.3 (Release Management and Support), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 6 (solution and operations excellence): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. The contract converts an internal target into an obligation with a consequence. Why the correct answer wins: The support tier sets the response time and the escalation path the business expects.
- **B:** Incorrect for this question. A named rotation turns an alert into a person who is already accountable for it. Why the correct answer wins: The support tier sets the response time and the escalation path the business expects.
- **C:** Correct. In this case: The support tier sets the response time and the escalation path the business expects.
- **D:** Incorrect for this question. The runbook records the diagnostic steps so the response does not depend on who is awake. Why the correct answer wins: The support tier sets the response time and the escalation path the business expects.

### Question 85 — C

Answer: Define the baseline and target as a KPI with an owner. A measured baseline and a named owner make the outcome testable after the programme. Local study-map skill 1.1 (Business Requirements and Success Metrics), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 1 (designing and planning): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. The dashboard gives the team one view of the same signals during an incident. Why the correct answer wins: A measured baseline and a named owner make the outcome testable after the programme.
- **B:** Incorrect for this question. The model compares run cost, people cost, and exit cost rather than the monthly bill alone. Why the correct answer wins: A measured baseline and a named owner make the outcome testable after the programme.
- **C:** Correct. In this case: A measured baseline and a named owner make the outcome testable after the programme.
- **D:** Incorrect for this question. The export attributes cost to the team and service that caused it. Why the correct answer wins: A measured baseline and a named owner make the outcome testable after the programme.

### Question 86 — B

Answer: Use Workload Identity Federation for the external pipeline. Federation exchanges an external token for short-lived credentials, so no key leaves the provider. Local study-map skill 3.5 (Secure Remote Access and Zero Trust), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 3 (security and compliance): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. A key file is a long-lived credential that works until it is noticed and revoked. Why the correct answer wins: Federation exchanges an external token for short-lived credentials, so no key leaves the provider.
- **B:** Correct. In this case: Federation exchanges an external token for short-lived credentials, so no key leaves the provider.
- **C:** Incorrect for this question. An environment variable is visible to anything that can read the instance metadata or the process list. Why the correct answer wins: Federation exchanges an external token for short-lived credentials, so no key leaves the provider.
- **D:** Incorrect for this question. An API key identifies a project and does not authorise a user, so it cannot express least privilege. Why the correct answer wins: Federation exchanges an external token for short-lived credentials, so no key leaves the provider.

### Question 87 — A

Answer: Attach a Serverless VPC Access connector. The connector gives serverless workloads a route to internal addresses in the VPC. Local study-map skill 2.5 (Serverless Configuration), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 2 (managing and provisioning): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Correct. In this case: The connector gives serverless workloads a route to internal addresses in the VPC.
- **B:** Incorrect for this question. Cloud NAT lets private instances reach the internet without an external address. Why the correct answer wins: The connector gives serverless workloads a route to internal addresses in the VPC.
- **C:** Incorrect for this question. Private Google Access reaches Google APIs from an internal address without a proxy or a NAT gateway. Why the correct answer wins: The connector gives serverless workloads a route to internal addresses in the VPC.
- **D:** Incorrect for this question. A PSC endpoint gives a private IP in the consumer VPC without peering or exposing the service publicly. Why the correct answer wins: The connector gives serverless workloads a route to internal addresses in the VPC.

### Question 88 — A

Answer: Run a warm standby at reduced capacity. A running but smaller copy recovers in a short window at a continuous cost. Local study-map skill 4.4 (Disaster Recovery and Business Continuity), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 4 (analyzing and optimizing): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Correct. In this case: A running but smaller copy recovers in a short window at a continuous cost.
- **B:** Incorrect for this question. Restoring from backup is the cheapest option and the slowest to recover. Why the correct answer wins: A running but smaller copy recovers in a short window at a continuous cost.
- **C:** Incorrect for this question. Only the core data and configuration stay warm, so recovery starts the compute and takes minutes. Why the correct answer wins: A running but smaller copy recovers in a short window at a continuous cost.
- **D:** Incorrect for this question. Both regions serve traffic, so a regional loss is absorbed without a failover decision. Why the correct answer wins: A running but smaller copy recovers in a short window at a continuous cost.

### Question 89 — D

Answer: Write a blameless postmortem with actions. The postmortem records cause and follow-up work, which is how the same failure is prevented. Local study-map skill 6.5 (Operational Excellence and Quality Control), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 6 (solution and operations excellence): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. The dashboard gives the team one view of the same signals during an incident. Why the correct answer wins: The postmortem records cause and follow-up work, which is how the same failure is prevented.
- **B:** Incorrect for this question. The runbook records the diagnostic steps so the response does not depend on who is awake. Why the correct answer wins: The postmortem records cause and follow-up work, which is how the same failure is prevented.
- **C:** Incorrect for this question. The support tier sets the response time and the escalation path the business expects. Why the correct answer wins: The postmortem records cause and follow-up work, which is how the same failure is prevented.
- **D:** Correct. In this case: The postmortem records cause and follow-up work, which is how the same failure is prevented.

### Question 90 — C

Answer: Enable Cloud SQL high availability with a standby. A regional standby takes over automatically when the primary zone fails. Local study-map skill 1.3 (High Availability and Failover Design), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 1 (designing and planning): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. Memorystore provides managed Redis or Memcached for sub-millisecond cache lookups. Why the correct answer wins: A regional standby takes over automatically when the primary zone fails.
- **B:** Incorrect for this question. Bigtable is a wide-column store for high-throughput key reads and writes at low latency. Why the correct answer wins: A regional standby takes over automatically when the primary zone fails.
- **C:** Correct. In this case: A regional standby takes over automatically when the primary zone fails.
- **D:** Incorrect for this question. A replica offloads read traffic but lags the primary, so it is not a failover target. Why the correct answer wins: A regional standby takes over automatically when the primary zone fails.

### Question 91 — B

Answer: Run the batch tier on Spot VMs. Spot capacity costs far less but can be reclaimed with 30 seconds of notice, which suits short-lived game servers. Local study-map skill 2.3 (Compute Provisioning and Patch Management), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 2 (managing and provisioning): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. Sole tenancy keeps the physical host dedicated, which matters for licensing or isolation rules. Why the correct answer wins: Spot capacity costs far less but can be reclaimed with 30 seconds of notice, which suits short-lived game servers.
- **B:** Correct. In this case: Spot capacity costs far less but can be reclaimed with 30 seconds of notice, which suits short-lived game servers.
- **C:** Incorrect for this question. VM Manager inventories and applies OS patches across a fleet instead of relying on manual runs. Why the correct answer wins: Spot capacity costs far less but can be reclaimed with 30 seconds of notice, which suits short-lived game servers.
- **D:** Incorrect for this question. A one- or three-year commitment discounts the capacity that runs constantly, not the peaks. Why the correct answer wins: Spot capacity costs far less but can be reclaimed with 30 seconds of notice, which suits short-lived game servers.

### Question 92 — D

Answer: Run a load test at the expected peak. The load test measures the system at the concurrency the business expects, before launch. Local study-map skill 4.3 (Testing and Validation), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 4 (analyzing and optimizing): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. The experiment proves the failover path works while the impact is controlled. Why the correct answer wins: The load test measures the system at the concurrency the business expects, before launch.
- **B:** Incorrect for this question. An independent test attempts the attack the design claims to prevent. Why the correct answer wins: The load test measures the system at the concurrency the business expects, before launch.
- **C:** Incorrect for this question. The pyramid puts volume where it is cheap and keeps end-to-end tests for the critical paths. Why the correct answer wins: The load test measures the system at the concurrency the business expects, before launch.
- **D:** Correct. In this case: The load test measures the system at the concurrency the business expects, before launch.

### Question 93 — C

Answer: Define dashboards and metrics in Cloud Monitoring. Monitoring collects the platform and application metrics that the first alert will use. Local study-map skill 6.1 (Observability Design), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 6 (solution and operations excellence): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. Recommender reports idle and over-provisioned resources with the estimated saving. Why the correct answer wins: Monitoring collects the platform and application metrics that the first alert will use.
- **B:** Incorrect for this question. The dashboard gives the team one view of the same signals during an incident. Why the correct answer wins: Monitoring collects the platform and application metrics that the first alert will use.
- **C:** Correct. In this case: Monitoring collects the platform and application metrics that the first alert will use.
- **D:** Incorrect for this question. Trace shows how one request spent its time across services and calls. Why the correct answer wins: Monitoring collects the platform and application metrics that the first alert will use.

### Question 94 — A

Answer: Use a managed instance group with autoscaling. The managed instance group replaces unhealthy instances and adds capacity from a template as load rises. Local study-map skill 1.6 (Compute Platform Selection), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 1 (designing and planning): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Correct. In this case: The managed instance group replaces unhealthy instances and adds capacity from a template as load rises.
- **B:** Incorrect for this question. Cloud Run runs a stateless container per request and scales to zero when idle. Why the correct answer wins: The managed instance group replaces unhealthy instances and adds capacity from a template as load rises.
- **C:** Incorrect for this question. Autopilot manages nodes, scaling, and patching, so the team owns only the workloads. Why the correct answer wins: The managed instance group replaces unhealthy instances and adds capacity from a template as load rises.
- **D:** Incorrect for this question. Batch schedules containerised jobs onto managed or existing capacity and retires it when done. Why the correct answer wins: The managed instance group replaces unhealthy instances and adds capacity from a template as load rises.

### Question 95 — D

Answer: Enforce the control with an organization policy constraint. An organization policy blocks the action across every project regardless of who holds the role. Local study-map skill 3.2 (Resource Hierarchy and Organization Policy), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 3 (security and compliance): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. A folder binding inherits to every project beneath it, so new projects start with the right access. Why the correct answer wins: An organization policy blocks the action across every project regardless of who holds the role.
- **B:** Incorrect for this question. A project is the boundary for quota, billing, and most IAM inheritance. Why the correct answer wins: An organization policy blocks the action across every project regardless of who holds the role.
- **C:** Incorrect for this question. Labels attribute spend in billing export; they do not grant or restrict access. Why the correct answer wins: An organization policy blocks the action across every project regardless of who holds the role.
- **D:** Correct. In this case: An organization policy blocks the action across every project regardless of who holds the role.

### Question 96 — C

Answer: Publish the API through Apigee. Apigee adds quotas, keys, mediation, and analytics at the gateway for each consumer. Local study-map skill 5.2 (API Management), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 5 (managing implementation): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. Cloud Armor filters requests at the edge with allow and deny rules and adaptive protection. Why the correct answer wins: Apigee adds quotas, keys, mediation, and analytics at the gateway for each consumer.
- **B:** Incorrect for this question. API Gateway fronts a Cloud Run or functions backend with a managed OpenAPI definition. Why the correct answer wins: Apigee adds quotas, keys, mediation, and analytics at the gateway for each consumer.
- **C:** Correct. In this case: Apigee adds quotas, keys, mediation, and analytics at the gateway for each consumer.
- **D:** Incorrect for this question. Endpoints validates and monitors an API described by an OpenAPI or gRPC spec. Why the correct answer wins: Apigee adds quotas, keys, mediation, and analytics at the gateway for each consumer.

### Question 97 — A

Answer: Roll out a canary to a small share of traffic. A canary limits the blast radius while the error and latency signals are compared. Local study-map skill 5.1 (Deployment and Release Strategy), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 5 (managing implementation): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Correct. In this case: A canary limits the blast radius while the error and latency signals are compared.
- **B:** Incorrect for this question. The flag separates deployment from release, so the code can ship dark and be turned off instantly. Why the correct answer wins: A canary limits the blast radius while the error and latency signals are compared.
- **C:** Incorrect for this question. Two identical environments let the switch be reversed instantly if the new one misbehaves. Why the correct answer wins: A canary limits the blast radius while the error and latency signals are compared.
- **D:** Incorrect for this question. A rolling replacement keeps capacity but exposes the whole fleet before the signal is trusted. Why the correct answer wins: A canary limits the blast radius while the error and latency signals are compared.

### Question 98 — B

Answer: Record build provenance for the artifact. Provenance states what built the artifact from which source, which is the evidence a supply-chain audit asks for. Local study-map skill 3.6 (Software Supply Chain Security), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 3 (security and compliance): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. Scanning reports known vulnerabilities in the image layers before deployment. Why the correct answer wins: Provenance states what built the artifact from which source, which is the evidence a supply-chain audit asks for.
- **B:** Correct. In this case: Provenance states what built the artifact from which source, which is the evidence a supply-chain audit asks for.
- **C:** Incorrect for this question. Artifact Registry holds the image with IAM-scoped access and vulnerability metadata. Why the correct answer wins: Provenance states what built the artifact from which source, which is the evidence a supply-chain audit asks for.
- **D:** Incorrect for this question. Network policy restricts pod-to-pod traffic inside the cluster, which a firewall rule cannot see. Why the correct answer wins: Provenance states what built the artifact from which source, which is the evidence a supply-chain audit asks for.

### Question 99 — D

Answer: Define an SLO with an error budget. An SLO ties the alert to the user promise rather than to a raw resource threshold. Local study-map skill 6.2 (Alerting and Service Level Objectives), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 6 (solution and operations excellence): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. The check measures availability from outside, which no internal metric can prove. Why the correct answer wins: An SLO ties the alert to the user promise rather than to a raw resource threshold.
- **B:** Incorrect for this question. The dashboard gives the team one view of the same signals during an incident. Why the correct answer wins: An SLO ties the alert to the user promise rather than to a raw resource threshold.
- **C:** Incorrect for this question. The policy fires when the series crosses the condition for the stated duration. Why the correct answer wins: An SLO ties the alert to the user promise rather than to a raw resource threshold.
- **D:** Correct. In this case: An SLO ties the alert to the user promise rather than to a raw resource threshold.

### Question 100 — B

Answer: Document the exit plan and data portability. An exit plan and data portability keep the migration reversible and bound how proprietary the design may become. The exit plan keeps the migration reversible and constrains how proprietary the design may become. Local study-map skill 1.2 (Non-Functional Requirements and Trade-offs), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 1 (designing and planning): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. The model compares run cost, people cost, and exit cost rather than the monthly bill alone. Why the correct answer wins: An exit plan and data portability keep the migration reversible and bound how proprietary the design may become.
- **B:** Correct. The exit plan keeps the migration reversible and constrains how proprietary the design may become. In this case: An exit plan and data portability keep the migration reversible and bound how proprietary the design may become.
- **C:** Incorrect for this question. Labels attribute spend in billing export; they do not grant or restrict access. Why the correct answer wins: An exit plan and data portability keep the migration reversible and bound how proprietary the design may become.
- **D:** Incorrect for this question. A budget alerts on spend but does not stop it. Why the correct answer wins: An exit plan and data portability keep the migration reversible and bound how proprietary the design may become.
