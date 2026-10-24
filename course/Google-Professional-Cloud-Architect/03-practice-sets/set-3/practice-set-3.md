# Google Cloud Professional Cloud Architect — Full-Length Mock Exam 3

Professional Cloud Architect · 100 questions · expanded practice bank · passing score not published

Blueprint-weighted mock exam. Item mix: 84 multiple-choice (selection count stated where needed), 16 multi-select, and 4 case studies of 5 questions. 8 of the multiple-choice items ask you to choose the correct candidate sequence. The live exam publishes 50-60 questions and two case studies worth 20-30 per cent of the score; this set is larger on purpose and cannot reproduce the split-screen case-study panel, drag-and-drop ordering, or lab tasks. See the README for the exact fidelity boundary.

Original educational content, not actual, recalled, or copied Google exam items.

## Questions

### 1. A security programme will be judged by the audit committee next year. What should be recorded before it starts?

Domain: Designing and planning a cloud solution architecture

- A. Build a three-year total cost of ownership model
- B. Publish a shared dashboard
- C. Export billing to BigQuery and review it per label
- D. Define the baseline and target as a KPI with an owner

### 2. A regulator asks how the organisation would leave the platform without losing records. What must the design include?

Domain: Designing and planning a cloud solution architecture

- A. Tag the resources with labels for cost reporting
- B. Build a three-year total cost of ownership model
- C. Set a budget with alert thresholds
- D. Document the exit plan and data portability

### 3. A hospital group must state how much record loss is tolerable and who answers for it. Which two artefacts settle that? Select two.

Domain: Designing and planning a cloud solution architecture

- A. Set the RPO and RTO with the business owner
- B. Put the recovery commitment in the contract
- C. Act on the Recommender suggestions
- D. Publish a shared dashboard
- E. Tag the resources with labels for cost reporting

### 4. The clinical database must survive a zone failure without an operator restarting it. What should be enabled?

Domain: Designing and planning a cloud solution architecture

- A. Use Bigtable
- B. Use Memorystore
- C. Add a read replica and route reads to it
- D. Enable Cloud SQL high availability with a standby

### 5. A records portal must keep serving during a regional loss with no failover decision. Which two pieces are required? Select two.

Domain: Designing and planning a cloud solution architecture

- A. Enable Cloud CDN on the backend
- B. Use backup and restore
- C. Run active-active across two regions
- D. Run a pilot-light standby
- E. Replicate the data to the second region

### 6. A partner hospital must call an internal imaging service without an internet path. What should be published?

Domain: Designing and planning a cloud solution architecture

- A. Create a DNS peering zone
- B. Deploy Cloud NAT for outbound traffic
- C. Enable Private Google Access on the subnet
- D. Publish the service through Private Service Connect

### 7. Two research networks must exchange traffic and resolve each other's names privately. Which two choices apply? Select two.

Domain: Designing and planning a cloud solution architecture

- A. Peer the two VPC networks
- B. Deploy Cloud NAT for outbound traffic
- C. Enable Cloud CDN on the backend
- D. Create a DNS peering zone
- E. Issue a short-lived signed URL

### 8. A public portal is being probed with credential-stuffing requests. What should be attached at the edge?

Domain: Designing and planning a cloud solution architecture

- A. Attach a Cloud Armor security policy
- B. Put Identity-Aware Proxy in front of the application
- C. Enable Cloud CDN on the backend
- D. Deploy Cloud NAT for outbound traffic

### 9. A clinical application needs PostgreSQL compatibility plus fast analytical scans on the same data. What should be used?

Domain: Designing and planning a cloud solution architecture

- A. Use AlloyDB for PostgreSQL
- B. Use Cloud SQL
- C. Use Bigtable
- D. Use Firestore

### 10. Twenty years of consent-bound records must be kept cheaply and deleted on a fixed schedule. Which two settings apply? Select two.

Domain: Designing and planning a cloud solution architecture

- A. Use local SSD for the scratch space
- B. Add a lifecycle rule that transitions and then deletes
- C. Mount a Filestore instance for the shared file path
- D. Store the objects in Standard storage class
- E. Store the objects in Archive storage class

### 11. A regulated cluster needs a hardened node image and a fixed patch cycle. What should be chosen?

Domain: Designing and planning a cloud solution architecture

- A. Submit the work as a Batch job
- B. Use GKE Standard with a node pool per workload shape
- C. Use GKE Autopilot
- D. Deploy the service on Cloud Run

### 12. A clinical application cannot be re-platformed this year but its hardware must leave the data centre. What should be used?

Domain: Designing and planning a cloud solution architecture

- A. Deploy the service on Cloud Run
- B. Use a managed instance group with autoscaling
- C. Run the legacy stack on Google Cloud VMware Engine
- D. Use GKE Autopilot

### 13. Changes to a consent register must reach the warehouse within minutes. What should be used?

Domain: Designing and planning a cloud solution architecture

- A. Use Datastream for change data capture
- B. Use Managed Service for Apache Airflow
- C. Use the BigQuery Data Transfer Service
- D. Queue the work in Cloud Tasks

### 14. A consent event must reach several consumers, and a poison message must not block the rest. Which two features apply? Select two.

Domain: Designing and planning a cloud solution architecture

- A. Trigger the job with Cloud Scheduler
- B. Attach a dead-letter topic
- C. Publish events to Pub/Sub
- D. Route the event with Eventarc
- E. Queue the work in Cloud Tasks

### 15. A research team must train a large model across thousands of accelerators. What should the design use?

Domain: Designing and planning a cloud solution architecture

- A. Run batch prediction
- B. Use a Dataproc cluster
- C. Deploy the service on Cloud Run
- D. Size the training on AI Hypercomputer with TPUs

### 16. Scanned referral letters must yield structured fields with layout awareness. What should be used?

Domain: Designing and planning a cloud solution architecture

- A. Use Document AI with a specialised processor
- B. Use the Vision API for the images
- C. Use the Speech-to-Text API
- D. Use the Translation API

### 17. A team must choose between a first-party model and an open-weight model for clinical summarisation. Where should it look?

Domain: Designing and planning a cloud solution architecture

- A. Index the corpus with Vertex AI Search
- B. Use Gemini Cloud Assist for the investigation
- C. Build the agent with the Agent Development Kit
- D. Select the model from Model Garden

### 18. A hospital group must be inventoried before a consolidation plan is approved. What should be used?

Domain: Designing and planning a cloud solution architecture

- A. Use Database Migration Service
- B. Assess the estate in Migration Center
- C. Convert the VMs with Migrate to Containers
- D. Copy the files with Storage Transfer Service

### 19. Ninety terabytes must leave a site whose uplink would take eleven months to carry it. What should be used?

Domain: Designing and planning a cloud solution architecture

- A. Use a Transfer Appliance for the one-off bulk move
- B. Use gcloud storage commands
- C. Use Storage Transfer Service for the recurring copy
- D. Copy the files with Storage Transfer Service

### 20. A clinical platform must demonstrate a recovery objective to an auditor. Which sequence is correct?

Domain: Designing and planning a cloud solution architecture

- A. Choose the DR pattern → fail over in a game day → set the RTO and RPO targets → build the standby environment
- B. Build and replicate the standby environment → choose the DR pattern → set the RTO and RPO targets → fail over in a game day
- C. Set the RTO and RPO targets → choose the DR pattern that meets them → build and replicate the standby environment → fail over in a game day and record the result
- D. Fail over in a game day → set the RTO and RPO targets → choose the DR pattern → build the standby environment

### 21. A clinic has one fibre provider and needs a private path that survives one tunnel. What should be used?

Domain: Managing and provisioning a solution infrastructure

- A. Deploy Cloud NAT for outbound traffic
- B. Use HA VPN with two tunnels
- C. Enable Cloud CDN on the backend
- D. Order a Dedicated Interconnect

### 22. A Cloud Run service must call an internal record store on a private address. What should be attached?

Domain: Managing and provisioning a solution infrastructure

- A. Publish the service through Private Service Connect
- B. Attach a Serverless VPC Access connector
- C. Deploy Cloud NAT for outbound traffic
- D. Enable Private Google Access on the subnet

### 23. Twenty hospital networks must reach a shared services hub, and names must resolve across them. Which two choices apply? Select two.

Domain: Managing and provisioning a solution infrastructure

- A. Peer the two VPC networks
- B. Deploy Cloud NAT for outbound traffic
- C. Attach a Cloud Armor security policy
- D. Create a DNS peering zone
- E. Build a Network Connectivity Center hub

### 24. Consent records must be immutable for the period the agreement states. What should be applied?

Domain: Managing and provisioning a solution infrastructure

- A. Apply a bucket retention policy with a locked period
- B. Add a lifecycle rule that transitions and then deletes
- C. Enable object versioning
- D. Enable Autoclass on the bucket

### 25. A clinical fact table is queried by date, and one aggregate is recomputed for every dashboard tile. Which two choices apply? Select two.

Domain: Managing and provisioning a solution infrastructure

- A. Cluster the table on the filter columns
- B. Partition the table on the date column
- C. Create a materialized view for the repeated aggregate
- D. Build the dashboard in Looker Studio
- E. Leave the project on on-demand pricing

### 26. An on-premises archive must be copied into Cloud Storage every night on a schedule. What should be used?

Domain: Managing and provisioning a solution infrastructure

- A. Use a Transfer Appliance for the one-off bulk move
- B. Issue a short-lived signed URL
- C. Use Storage Transfer Service for the recurring copy
- D. Copy the files with Storage Transfer Service

### 27. A de-identification batch runs for two hours and restarts if a host is reclaimed, while the platform baseline runs all month. Which two purchasing choices apply? Select two.

Domain: Managing and provisioning a solution infrastructure

- A. Buy committed use discounts for the steady baseline
- B. Run the batch tier on Spot VMs
- C. Use VM Manager for OS patch compliance
- D. Use a custom machine type sized to the workload
- E. Use sole-tenant nodes

### 28. Only images signed by the clinical build pipeline may run in the cluster. What should be enforced?

Domain: Managing and provisioning a solution infrastructure

- A. Register the clusters in a fleet
- B. Enable network policy enforcement
- C. Enable node auto-provisioning
- D. Enforce Binary Authorization at admission

### 29. Pods must hold no keys, and no node may have an external address. Which two settings apply? Select two.

Domain: Managing and provisioning a solution infrastructure

- A. Create a service account key file for the pipeline
- B. Deploy Cloud NAT for outbound traffic
- C. Enable Workload Identity Federation for GKE
- D. Use sole-tenant nodes
- E. Create private nodes with no external IP addresses

### 30. A clinical cluster must be built with private nodes, pod identity, and attested images. Which sequence is correct?

Domain: Managing and provisioning a solution infrastructure

- A. Build a Shared VPC → deploy through Binary Authorization → create the project → create the cluster
- B. Create a regional private cluster → build a Shared VPC with private subnets → enable APIs → deploy through Binary Authorization
- C. Deploy through Binary Authorization → create the cluster → build the Shared VPC → create the project
- D. Create the project and enable APIs → build a Shared VPC with private subnets → create a regional private cluster with Workload Identity Federation for GKE → deploy through Binary Authorization

### 31. A consent-check service must answer within 200 ms of the first request after a quiet period. What should be configured?

Domain: Managing and provisioning a solution infrastructure

- A. Deploy the workload on Cloud Run with a GPU
- B. Set a minimum instance count on the Cloud Run service
- C. Deploy on App Engine flexible environment
- D. Raise the request concurrency setting

### 32. Kubernetes manifests and cloud resources must be reconciled from one repository. What should be used?

Domain: Managing and provisioning a solution infrastructure

- A. Manage the resources with Config Connector
- B. Use Deployment Manager templates
- C. Manage the resources with Terraform
- D. Automate the step with the gcloud CLI

### 33. A de-identification model must answer per record with low latency. Where should it be deployed?

Domain: Managing and provisioning a solution infrastructure

- A. Publish events to Pub/Sub
- B. Deploy to an online prediction endpoint
- C. Size the training on AI Hypercomputer with TPUs
- D. Run batch prediction

### 34. A team must compare three open-weight models before committing to one licence. Where should it look?

Domain: Managing and provisioning a solution infrastructure

- A. Index the corpus with Vertex AI Search
- B. Use Gemini Cloud Assist for the investigation
- C. Build the agent with the Agent Development Kit
- D. Select the model from Model Garden

### 35. A de-identification model must reach production with a reproducible lineage. Which sequence is correct?

Domain: Managing and provisioning a solution infrastructure

- A. Curate and version the training data → train and evaluate the model in a pipeline → register the model and record its metrics → deploy to an endpoint with traffic splitting and model monitoring
- B. Register the model → curate the training data → deploy to an endpoint → train the model
- C. Deploy to an endpoint → train the model → register the model → curate the training data
- D. Train the model → deploy to an endpoint → curate the training data → register the model

### 36. A role must allow exactly four read permissions on two datasets. What should be created?

Domain: Designing for security and compliance

- A. Grant a predefined role at the narrowest resource
- B. Define a custom role with only the required permissions
- C. Authenticate the call with an API key
- D. Run a bastion host with a public address

### 37. A new hospital project must inherit the clinical access set on the day it is created. Where should the roles be bound?

Domain: Designing for security and compliance

- A. Create a folder per environment and bind roles there
- B. Grant a predefined role at the narrowest resource
- C. Tag the resources with labels for cost reporting
- D. Create a separate project per environment

### 38. No project may export records outside the country, and one suspended vendor must keep no access. Which two controls apply? Select two.

Domain: Designing for security and compliance

- A. Enforce the control with an organization policy constraint
- B. Apply an IAM deny policy
- C. Create a folder per environment and bind roles there
- D. Add an IAM condition on the binding
- E. Tag the resources with labels for cost reporting

### 39. A regulator requires key material inside a certified hardware module. What should be used?

Domain: Designing for security and compliance

- A. Supply a customer-supplied encryption key
- B. Create the key ring in the same region as the data
- C. Use Cloud HSM for the key
- D. Store the credential in Secret Manager

### 40. The hospital must control its own keys and change them on a published schedule. Which two settings apply? Select two.

Domain: Designing for security and compliance

- A. Store the credential in Secret Manager
- B. Set an automatic rotation period on the key
- C. Put the credential in an environment variable on the instance
- D. Supply a customer-supplied encryption key
- E. Encrypt with a customer-managed key in Cloud KMS

### 41. A perimeter will be enforced on a clinical estate with many integrations. What should happen first?

Domain: Designing for security and compliance

- A. Route the logs with an aggregated sink
- B. Run the perimeter in dry-run mode first
- C. Attach a Cloud Armor security policy
- D. Put the projects inside a VPC Service Controls perimeter

### 42. A managed database must take an internal address inside the clinical network. What should be allocated?

Domain: Designing for security and compliance

- A. Enable Private Google Access on the subnet
- B. Allocate private services access for the peered services
- C. Publish the service through Private Service Connect
- D. Deploy Cloud NAT for outbound traffic

### 43. Workforce access must consider device posture before a clinical application opens. What should be used?

Domain: Designing for security and compliance

- A. Authenticate the call with an API key
- B. Deploy Cloud NAT for outbound traffic
- C. Run a bastion host with a public address
- D. Use Chrome Enterprise Premium for the workforce

### 44. An auditor asks what built the deployed artifact and from which commit. What should be recorded?

Domain: Designing for security and compliance

- A. Enable network policy enforcement
- B. Record build provenance for the artifact
- C. Store the images in Artifact Registry
- D. Enable Artifact Analysis scanning on the repository

### 45. A clinical assistant must resist prompt injection and block unsafe output. What should be added?

Domain: Designing for security and compliance

- A. Screen prompts and responses with Model Armor
- B. Turn on Security Command Center findings
- C. De-identify the data with Sensitive Data Protection
- D. Require an access level in the perimeter

### 46. Audit evidence must remain readable for seven years and cannot be shortened. What should be used?

Domain: Designing for security and compliance

- A. Rely on Admin Activity audit logs
- B. Create a log-based metric
- C. Use a locked log bucket with a fixed retention
- D. Apply a bucket retention policy with a locked period

### 47. An auditor demands proof of who read which record. Which sequence is correct?

Domain: Designing for security and compliance

- A. Create a locked log bucket → enable data access audit logs → query the evidence → route the logs with a sink
- B. Query the evidence → create a locked log bucket → enable audit logs → route the logs
- C. Enable data access audit logs for the services in scope → create a locked log bucket with the required retention → route the logs with an aggregated sink → query and export the evidence for the auditor
- D. Route the logs with a sink → query the evidence → enable audit logs → create a locked bucket

### 48. Clinical teams release monthly and accumulate merge conflicts for weeks. What should change?

Domain: Analyzing and optimizing technical and business processes

- A. Roll the change out instance by instance
- B. Put the change behind a feature flag
- C. Rebuild the artifact separately for each environment
- D. Adopt trunk-based development with short-lived branches

### 49. A clinical integration is released weekly and downstream teams break on schema changes. Which two practices help most? Select two.

Domain: Analyzing and optimizing technical and business processes

- A. Cover the change with unit, integration, and a few end-to-end tests
- B. Run a chaos experiment against a zone
- C. Add a contract test on the API
- D. Run a load test at the expected peak
- E. Commission a penetration test

### 50. A nightly de-identification job uses four times the expected CPU and nobody knows which function. What should be attached?

Domain: Analyzing and optimizing technical and business processes

- A. Add an uptime check from several regions
- B. Attach Cloud Profiler to the service
- C. Inspect the trace waterfall in Cloud Trace
- D. Publish a shared dashboard

### 51. A consent check failed and the team needs both the error text and the call chain. Which two tools apply? Select two.

Domain: Analyzing and optimizing technical and business processes

- A. Publish a shared dashboard
- B. Publish a runbook per alert
- C. Define an SLO with an error budget
- D. Inspect the trace waterfall in Cloud Trace
- E. Query the entries in Cloud Logging

### 52. The design claims a clinical portal cannot be indexed from the internet. How should that claim be tested?

Domain: Analyzing and optimizing technical and business processes

- A. Cover the change with unit, integration, and a few end-to-end tests
- B. Commission a penetration test
- C. Run a chaos experiment against a zone
- D. Run a load test at the expected peak

### 53. A failover path has never carried real traffic. What should be run before the audit?

Domain: Analyzing and optimizing technical and business processes

- A. Roll out a canary to a small share of traffic
- B. Commission a penetration test
- C. Run a load test at the expected peak
- D. Run a chaos experiment against a zone

### 54. A clinical service can accept fifteen minutes of downtime and a smaller running copy. What fits?

Domain: Analyzing and optimizing technical and business processes

- A. Use backup and restore
- B. Run a pilot-light standby
- C. Run a warm standby at reduced capacity
- D. Run active-active across two regions

### 55. The compliance estate is suspected of paying for idle capacity. What should be reviewed first?

Domain: Analyzing and optimizing technical and business processes

- A. Set a budget with alert thresholds
- B. Act on the Recommender suggestions
- C. Export billing to BigQuery and review it per label
- D. Tag the resources with labels for cost reporting

### 56. Legal and clinical leadership disagree about whether a record may leave the country. What should the architect do?

Domain: Analyzing and optimizing technical and business processes

- A. Publish a runbook per alert
- B. Publish a service catalog entry with an approved template
- C. Agree the decision rights with the stakeholders
- D. Route the change through a change advisory board

### 57. Teams need a compliant project without waiting for the security team. What should be published?

Domain: Analyzing and optimizing technical and business processes

- A. Tag the resources with labels for cost reporting
- B. Publish a service catalog entry with an approved template
- C. Enforce the control with an organization policy constraint
- D. Manage the resources with Terraform

### 58. A clinical portal is failing and the team must respond in the agreed order. Which sequence is correct?

Domain: Analyzing and optimizing technical and business processes

- A. Detect the symptom through an alert → contain the impact and restore service → isolate the root cause from logs, traces, and metrics → apply the permanent fix and write the postmortem
- B. Isolate the root cause → detect the symptom → write the postmortem → restore service
- C. Write the postmortem → detect the symptom → isolate the root cause → restore service
- D. Restore service → detect the symptom → write the postmortem → isolate the root cause

### 59. The warehouse bill for the compliance team must fall without changing any control. Which sequence is correct?

Domain: Analyzing and optimizing technical and business processes

- A. Partition and cluster the table → measure slot time → inspect the plan → rewrite the query
- B. Inspect the query plan and bytes processed → partition and cluster the table on the filter columns → rewrite the query to prune partitions → measure the new slot time and bytes scanned
- C. Rewrite the query → partition the table → measure slot time → inspect the plan
- D. Measure slot time → rewrite the query → inspect the plan → partition the table

### 60. A clinical portal release must be reversible in seconds with two full environments available. What should be used?

Domain: Managing implementation

- A. Deploy blue/green with a traffic switch
- B. Roll the change out instance by instance
- C. Put the change behind a feature flag
- D. Roll out a canary to a small share of traffic

### 61. A new consent screen must be visible to one hospital first and withdrawn instantly. What should be used?

Domain: Managing implementation

- A. Put the change behind a feature flag
- B. Deploy blue/green with a traffic switch
- C. Roll the change out instance by instance
- D. Roll out a canary to a small share of traffic

### 62. A release must be measured on a small share of traffic, and the previous build must be exactly restorable. Which two practices apply? Select two.

Domain: Managing implementation

- A. Set a budget with alert thresholds
- B. Keep the previous image digest ready for rollback
- C. Rebuild the artifact separately for each environment
- D. Promote the same tested artifact between environments
- E. Roll out a canary to a small share of traffic

### 63. Hospital partners need per-consumer quotas and mediation on a clinical API. What should be used?

Domain: Managing implementation

- A. Use API Gateway
- B. Attach a Cloud Armor security policy
- C. Use Cloud Endpoints
- D. Publish the API through Apigee

### 64. A partner integration must never break, and each version must have a published end date. Which two practices apply? Select two.

Domain: Managing implementation

- A. Add a contract test on the API
- B. Authenticate the call with an API key
- C. Publish a versioning and deprecation policy
- D. Roll the change out instance by instance
- E. Rebuild the artifact separately for each environment

### 65. A 9 TB clinical database must move with less than two hours of downtime. What should be used?

Domain: Managing implementation

- A. Use the BigQuery Data Transfer Service
- B. Use Datastream for change data capture
- C. Migrate the database with Database Migration Service
- D. Copy the files with Storage Transfer Service

### 66. A legacy imaging application must run on GKE without being rebuilt. What should be used?

Domain: Managing implementation

- A. Convert the VMs with Migrate to Containers
- B. Run the legacy stack on Google Cloud VMware Engine
- C. Copy the files with Storage Transfer Service
- D. Assess the estate in Migration Center

### 67. A nightly evidence export must be scripted so the command is recorded. What should be used?

Domain: Managing implementation

- A. Use Cloud Shell for the one-off task
- B. Use Cloud Code in the IDE
- C. Use the bq command-line tool
- D. Automate the step with the gcloud CLI

### 68. Integration tests must run with no billable resource and no network access. What should be used?

Domain: Managing implementation

- A. Run the build in Cloud Build
- B. Automate the step with the gcloud CLI
- C. Manage the resources with Terraform
- D. Run the emulator in the pipeline

### 69. A consent service must handle quota errors with the recommended backoff. What should it use?

Domain: Managing implementation

- A. Use the Google API client library with retries
- B. Impersonate a service account for a curl test
- C. Authenticate the call with an API key
- D. Automate the step with the gcloud CLI

### 70. An engineer must reproduce a permission failure as the exact workload identity. What should be used?

Domain: Managing implementation

- A. Authenticate the call with an API key
- B. Impersonate a service account for a curl test
- C. Create a service account key file for the pipeline
- D. Put the credential in an environment variable on the instance

### 71. A clinical consolidation must move dependencies together. Which sequence is correct?

Domain: Managing implementation

- A. Group servers into waves → inventory the estate → cut over and decommission → validate a pilot wave
- B. Cut over and decommission → validate a pilot wave → inventory the estate → group servers into waves
- C. Validate a pilot wave → inventory the estate → group servers into waves → cut over and decommission
- D. Inventory the estate in Migration Center → group servers into dependency-based waves → validate a pilot wave in the target landing zone → cut over wave by wave and decommission the source

### 72. A clinical platform must expose the metrics its alerts will later use. What should be configured?

Domain: Ensuring solution and operations excellence

- A. Define an SLO with an error budget
- B. Query the entries in Cloud Logging
- C. Publish a shared dashboard
- D. Define dashboards and metrics in Cloud Monitoring

### 73. The same exception keeps recurring in a service and must be clustered and counted. What should be used?

Domain: Ensuring solution and operations excellence

- A. Add an uptime check from several regions
- B. Attach Cloud Profiler to the service
- C. Group the exceptions in Error Reporting
- D. Inspect the trace waterfall in Cloud Trace

### 74. The clinical board wants an alert tied to record availability, not CPU. What should be defined?

Domain: Ensuring solution and operations excellence

- A. Create an alerting policy on the metric
- B. Define an SLO with an error budget
- C. Add an uptime check from several regions
- D. Publish a shared dashboard

### 75. A specific consent error must be counted and then reported to the on-call engineer. Which two steps apply? Select two.

Domain: Ensuring solution and operations excellence

- A. Create an alerting policy on the metric
- B. Define an SLO with an error budget
- C. Act on the Recommender suggestions
- D. Create a log-based metric
- E. Publish a shared dashboard

### 76. No named person currently answers a clinical alert at night. What should be established?

Domain: Ensuring solution and operations excellence

- A. Match the support plan to the recovery commitment
- B. Publish a runbook per alert
- C. Define an on-call rotation with an escalation path
- D. Put the recovery commitment in the contract

### 77. The hospital expects a one-hour response to a severity-one case. What should be aligned?

Domain: Ensuring solution and operations excellence

- A. Put the recovery commitment in the contract
- B. Publish a runbook per alert
- C. Match the support plan to the recovery commitment
- D. Define an on-call rotation with an escalation path

### 78. A national awareness campaign will multiply portal traffic. What should run before it starts?

Domain: Ensuring solution and operations excellence

- A. Run a load test at the expected peak
- B. Commission a penetration test
- C. Cover the change with unit, integration, and a few end-to-end tests
- D. Run a chaos experiment against a zone

### 79. A consent failure recurred because the follow-up work was never recorded. What should be produced after each incident?

Domain: Ensuring solution and operations excellence

- A. Publish a shared dashboard
- B. Match the support plan to the recovery commitment
- C. Publish a runbook per alert
- D. Write a blameless postmortem with actions

### 80. A clinical release must be reversible within one minute during business hours. Which sequence is correct?

Domain: Ensuring solution and operations excellence

- A. Build an immutable image and record its digest → deploy the new revision without traffic → shift a small traffic percentage and watch error and latency signals → promote to full traffic or roll back to the pinned digest
- B. Watch the error rate → deploy the new revision → shift traffic → build the image
- C. Deploy the new revision → promote to full traffic → shift a small percentage → build the image
- D. Shift full traffic to the new revision → build the image → watch the error rate → promote or roll back

---

## Case study — Beacon Genomics

Beacon Genomics sequences human genomes for research hospitals in three countries. Each genome is about 200 GB and the archive grows by 40 TB a month. Raw reads are analysed for two weeks after sequencing and then kept for twenty years because consent agreements require it. Researchers in different countries must not be able to read each other cohorts, and the consent terms forbid moving data out of the country where it was collected. The research platform runs batch analysis on thousands of cores for a few days each month and is idle between studies.

The next 5 questions refer to it. Read the scenario once, then answer all 5; each item restates the constraint it tests and is scored individually.

### 81. Twenty years of sequence data must be held cheaply after analysis. Which class fits?

Domain: Designing and planning a cloud solution architecture

- A. Store the objects in Standard storage class
- B. Store the objects in Nearline storage class
- C. Mount a Filestore instance for the shared file path
- D. Store the objects in Archive storage class

### 82. A new country cohort must be sized before the platform is extended. What should be used?

Domain: Designing and planning a cloud solution architecture

- A. Assess the estate in Migration Center
- B. Use Database Migration Service
- C. Convert the VMs with Migrate to Containers
- D. Copy the files with Storage Transfer Service

### 83. Researchers must be able to prove they never opened another cohort. What should be enabled?

Domain: Designing for security and compliance

- A. Create a log-based metric
- B. Review Access Transparency logs
- C. Rely on Admin Activity audit logs
- D. Enable Data Access audit logs

### 84. Thousands of cores sit idle between studies. What should be reviewed first?

Domain: Analyzing and optimizing technical and business processes

- A. Act on the Recommender suggestions
- B. Tag the resources with labels for cost reporting
- C. Export billing to BigQuery and review it per label
- D. Set a budget with alert thresholds

### 85. The lab must see whether the last study finished within its window. What should be built first?

Domain: Ensuring solution and operations excellence

- A. Publish a shared dashboard
- B. Define dashboards and metrics in Cloud Monitoring
- C. Inspect the trace waterfall in Cloud Trace
- D. Act on the Recommender suggestions

---

## Case study — Fable Media Group

Fable Media Group runs a subscription news site with 8 million registered readers across the European Union and Brazil. The data protection officer has found that reader records contain email addresses, device identifiers, and in some cases payment details in free-text support notes. Marketing wants to run a churn model on the reader data, and the legal team wants proof that personal data is minimised before it reaches the model. Readers may request deletion, and the request must remove the record everywhere within thirty days. The engineering team uses BigQuery for analytics and Cloud Storage for exports.

The next 5 questions refer to it. Read the scenario once, then answer all 5; each item restates the constraint it tests and is scored individually.

### 86. Marketing must model churn on readers without seeing direct identifiers. What should be applied?

Domain: Designing and planning a cloud solution architecture

- A. Build the dashboard in Looker Studio
- B. Apply column-level data masking policies
- C. Add row-level access policies to the table
- D. Expose the data through an authorized view

### 87. The deletion service on Cloud Run must reach an internal database. What should be attached?

Domain: Managing and provisioning a solution infrastructure

- A. Publish the service through Private Service Connect
- B. Attach a Serverless VPC Access connector
- C. Enable Private Google Access on the subnet
- D. Deploy Cloud NAT for outbound traffic

### 88. A deletion request must complete within thirty days under peak load. What should be run?

Domain: Analyzing and optimizing technical and business processes

- A. Commission a penetration test
- B. Cover the change with unit, integration, and a few end-to-end tests
- C. Run a load test at the expected peak
- D. Run a chaos experiment against a zone

### 89. A missed deletion is a reportable breach. Who must answer it on a Sunday?

Domain: Ensuring solution and operations excellence

- A. Publish a runbook per alert
- B. Put the recovery commitment in the contract
- C. Define an on-call rotation with an escalation path
- D. Match the support plan to the recovery commitment

### 90. Brazilian readers must be processed in Brazil. What must the design fix?

Domain: Designing and planning a cloud solution architecture

- A. Keep the data in the region the regulator requires
- B. Document the exit plan and data portability
- C. Define the baseline and target as a KPI with an owner
- D. Build a three-year total cost of ownership model

---

## Case study — Ironvale Bank

Ironvale Bank processes card payments and is audited against PCI DSS. Card numbers must never be readable by the analytics team, and the encryption keys must be rotated on a schedule the bank controls and must remain in the region where the data lives. A recent penetration test showed that a developer with read access to a bucket could copy a data export to a personal project. The regulators have asked for evidence that data cannot leave the approved services even when a principal has the permission to read it. The bank runs three environments and wants the same controls applied to every new project automatically.

The next 5 questions refer to it. Read the scenario once, then answer all 5; each item restates the constraint it tests and is scored individually.

### 91. Card numbers must be unreadable without a key the bank can revoke. What should be used?

Domain: Designing for security and compliance

- A. Use Cloud HSM for the key
- B. Store the credential in Secret Manager
- C. Encrypt with a customer-managed key in Cloud KMS
- D. Supply a customer-supplied encryption key

### 92. A developer copied an export to a personal project. What would have blocked it?

Domain: Designing for security and compliance

- A. Tag the resources with labels for cost reporting
- B. Apply an IAM deny policy
- C. Apply a hierarchical firewall policy at the organization or folder
- D. Put the projects inside a VPC Service Controls perimeter

### 93. Card data exports must be undeletable for the audit period. What should be applied?

Domain: Managing and provisioning a solution infrastructure

- A. Enable Autoclass on the bucket
- B. Enable object versioning
- C. Apply a bucket retention policy with a locked period
- D. Add a lifecycle rule that transitions and then deletes

### 94. The penetration test found the copy path. What should follow the remediation?

Domain: Ensuring solution and operations excellence

- A. Publish a runbook per alert
- B. Match the support plan to the recovery commitment
- C. Write a blameless postmortem with actions
- D. Publish a shared dashboard

### 95. Every new project must start with the approved controls. What should the pipeline enforce?

Domain: Analyzing and optimizing technical and business processes

- A. Adopt trunk-based development with short-lived branches
- B. Require a reviewed pull request and a passing plan
- C. Roll the change out instance by instance
- D. Rebuild the artifact separately for each environment

---

## Case study — Summit Public Sector

Summit Public Sector delivers a citizen benefits portal for a national government. The workload handles identity documents, tax identifiers, and benefit payments, and the government requires that only personnel who are citizens and who have passed a background check may operate the platform. The portal must be available during a national election, when traffic is thirty times normal, and every administrative action must be attributable to a named individual. The government has its own identity provider, and it will not permit service account keys anywhere in the environment. A separate agency will audit the deployment twice a year.

The next 5 questions refer to it. Read the scenario once, then answer all 5; each item restates the constraint it tests and is scored individually.

### 96. Only vetted staff on managed devices may operate the portal. What should be used?

Domain: Designing for security and compliance

- A. Use Chrome Enterprise Premium for the workforce
- B. Run a bastion host with a public address
- C. Authenticate the call with an API key
- D. Deploy Cloud NAT for outbound traffic

### 97. No project may be created outside the approved region. What should be enforced?

Domain: Designing for security and compliance

- A. Create a separate project per environment
- B. Tag the resources with labels for cost reporting
- C. Enforce the control with an organization policy constraint
- D. Create a folder per environment and bind roles there

### 98. Workloads must hold no service account keys at all. What should be enabled?

Domain: Managing and provisioning a solution infrastructure

- A. Create a service account key file for the pipeline
- B. Put the credential in an environment variable on the instance
- C. Enable Workload Identity Federation for GKE
- D. Use Workload Identity Federation for the external pipeline

### 99. The election-day promise is measured in successful logins. How should it be monitored?

Domain: Ensuring solution and operations excellence

- A. Publish a shared dashboard
- B. Define an SLO with an error budget
- C. Create an alerting policy on the metric
- D. Add an uptime check from several regions

### 100. The platform team is small and cannot patch nodes. What should be chosen?

Domain: Designing and planning a cloud solution architecture

- A. Use GKE Standard with a node pool per workload shape
- B. Deploy the service on Cloud Run
- C. Use GKE Autopilot
- D. Submit the work as a Batch job

---

## Answer key and explanations

### Question 1 — D

Answer: Define the baseline and target as a KPI with an owner. A measured baseline and a named owner make the outcome testable after the programme. Local study-map skill 1.1 (Business Requirements and Success Metrics), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 1 (designing and planning): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. The model compares run cost, people cost, and exit cost rather than the monthly bill alone. Why the correct answer wins: A measured baseline and a named owner make the outcome testable after the programme.
- **B:** Incorrect for this question. The dashboard gives the team one view of the same signals during an incident. Why the correct answer wins: A measured baseline and a named owner make the outcome testable after the programme.
- **C:** Incorrect for this question. The export attributes cost to the team and service that caused it. Why the correct answer wins: A measured baseline and a named owner make the outcome testable after the programme.
- **D:** Correct. In this case: A measured baseline and a named owner make the outcome testable after the programme.

### Question 2 — D

Answer: Document the exit plan and data portability. An exit plan and data portability keep the migration reversible and bound how proprietary the design may become. The exit plan keeps the migration reversible and constrains how proprietary the design may become. Local study-map skill 1.2 (Non-Functional Requirements and Trade-offs), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 1 (designing and planning): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. Labels attribute spend in billing export; they do not grant or restrict access. Why the correct answer wins: An exit plan and data portability keep the migration reversible and bound how proprietary the design may become.
- **B:** Incorrect for this question. The model compares run cost, people cost, and exit cost rather than the monthly bill alone. Why the correct answer wins: An exit plan and data portability keep the migration reversible and bound how proprietary the design may become.
- **C:** Incorrect for this question. A budget alerts on spend but does not stop it. Why the correct answer wins: An exit plan and data portability keep the migration reversible and bound how proprietary the design may become.
- **D:** Correct. The exit plan keeps the migration reversible and constrains how proprietary the design may become. In this case: An exit plan and data portability keep the migration reversible and bound how proprietary the design may become.

### Question 3 — A, B

Answers: Set the RPO and RTO with the business owner; Put the recovery commitment in the contract. The targets quantify the acceptable loss, and the contract attaches a consequence to missing them. The targets come from the business impact of data loss and downtime, not from the technology. The contract converts an internal target into an obligation with a consequence. Local study-map skill 1.2 (Non-Functional Requirements and Trade-offs), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 1 (designing and planning): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Correct. The targets come from the business impact of data loss and downtime, not from the technology. In this case: The targets quantify the acceptable loss, and the contract attaches a consequence to missing them.
- **B:** Correct. The contract converts an internal target into an obligation with a consequence. In this case: The targets quantify the acceptable loss, and the contract attaches a consequence to missing them.
- **C:** Incorrect for this question. Recommender reports idle and over-provisioned resources with the estimated saving. Why the correct answer wins: The targets quantify the acceptable loss, and the contract attaches a consequence to missing them.
- **D:** Incorrect for this question. The dashboard gives the team one view of the same signals during an incident. Why the correct answer wins: The targets quantify the acceptable loss, and the contract attaches a consequence to missing them.
- **E:** Incorrect for this question. Labels attribute spend in billing export; they do not grant or restrict access. Why the correct answer wins: The targets quantify the acceptable loss, and the contract attaches a consequence to missing them.

### Question 4 — D

Answer: Enable Cloud SQL high availability with a standby. A regional standby takes over automatically when the primary zone fails. Local study-map skill 1.3 (High Availability and Failover Design), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 1 (designing and planning): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. Bigtable is a wide-column store for high-throughput key reads and writes at low latency. Why the correct answer wins: A regional standby takes over automatically when the primary zone fails.
- **B:** Incorrect for this question. Memorystore provides managed Redis or Memcached for sub-millisecond cache lookups. Why the correct answer wins: A regional standby takes over automatically when the primary zone fails.
- **C:** Incorrect for this question. A replica offloads read traffic but lags the primary, so it is not a failover target. Why the correct answer wins: A regional standby takes over automatically when the primary zone fails.
- **D:** Correct. In this case: A regional standby takes over automatically when the primary zone fails.

### Question 5 — C, E

Answers: Run active-active across two regions; Replicate the data to the second region. Both regions serve traffic, and the data must already be in the second region when it is needed. Both regions serve traffic, so a regional loss is absorbed without a failover decision. The data must exist in the second region before any compute there can serve it. Local study-map skill 1.3 (High Availability and Failover Design), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 1 (designing and planning): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. CDN caches responses at edge locations, which cuts origin load and latency for repeat reads. Why the correct answer wins: Both regions serve traffic, and the data must already be in the second region when it is needed.
- **B:** Incorrect for this question. Restoring from backup is the cheapest option and the slowest to recover. Why the correct answer wins: Both regions serve traffic, and the data must already be in the second region when it is needed.
- **C:** Correct. Both regions serve traffic, so a regional loss is absorbed without a failover decision. In this case: Both regions serve traffic, and the data must already be in the second region when it is needed.
- **D:** Incorrect for this question. Only the core data and configuration stay warm, so recovery starts the compute and takes minutes. Why the correct answer wins: Both regions serve traffic, and the data must already be in the second region when it is needed.
- **E:** Correct. The data must exist in the second region before any compute there can serve it. In this case: Both regions serve traffic, and the data must already be in the second region when it is needed.

### Question 6 — D

Answer: Publish the service through Private Service Connect. A PSC endpoint gives a private IP in the consumer VPC without peering or exposing the service publicly. Local study-map skill 1.4 (Network Design), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 1 (designing and planning): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. DNS peering resolves names across networks without transferring zone ownership. Why the correct answer wins: A PSC endpoint gives a private IP in the consumer VPC without peering or exposing the service publicly.
- **B:** Incorrect for this question. Cloud NAT lets private instances reach the internet without an external address. Why the correct answer wins: A PSC endpoint gives a private IP in the consumer VPC without peering or exposing the service publicly.
- **C:** Incorrect for this question. Private Google Access reaches Google APIs from an internal address without a proxy or a NAT gateway. Why the correct answer wins: A PSC endpoint gives a private IP in the consumer VPC without peering or exposing the service publicly.
- **D:** Correct. In this case: A PSC endpoint gives a private IP in the consumer VPC without peering or exposing the service publicly.

### Question 7 — A, D

Answers: Peer the two VPC networks; Create a DNS peering zone. Peering joins the networks at layer three, and DNS peering resolves names without transferring the zone. Peering joins two networks at layer three but does not share firewalls or transitive routes. DNS peering resolves names across networks without transferring zone ownership. Local study-map skill 1.4 (Network Design), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 1 (designing and planning): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Correct. Peering joins two networks at layer three but does not share firewalls or transitive routes. In this case: Peering joins the networks at layer three, and DNS peering resolves names without transferring the zone.
- **B:** Incorrect for this question. Cloud NAT lets private instances reach the internet without an external address. Why the correct answer wins: Peering joins the networks at layer three, and DNS peering resolves names without transferring the zone.
- **C:** Incorrect for this question. CDN caches responses at edge locations, which cuts origin load and latency for repeat reads. Why the correct answer wins: Peering joins the networks at layer three, and DNS peering resolves names without transferring the zone.
- **D:** Correct. DNS peering resolves names across networks without transferring zone ownership. In this case: Peering joins the networks at layer three, and DNS peering resolves names without transferring the zone.
- **E:** Incorrect for this question. A signed URL grants one object for a fixed time without exposing credentials or making the bucket public. Why the correct answer wins: Peering joins the networks at layer three, and DNS peering resolves names without transferring the zone.

### Question 8 — A

Answer: Attach a Cloud Armor security policy. Cloud Armor filters requests at the edge with allow and deny rules and adaptive protection. Local study-map skill 1.4 (Network Design), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 1 (designing and planning): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Correct. In this case: Cloud Armor filters requests at the edge with allow and deny rules and adaptive protection.
- **B:** Incorrect for this question. IAP authenticates and authorises each request before it reaches the backend, with no VPN. Why the correct answer wins: Cloud Armor filters requests at the edge with allow and deny rules and adaptive protection.
- **C:** Incorrect for this question. CDN caches responses at edge locations, which cuts origin load and latency for repeat reads. Why the correct answer wins: Cloud Armor filters requests at the edge with allow and deny rules and adaptive protection.
- **D:** Incorrect for this question. Cloud NAT lets private instances reach the internet without an external address. Why the correct answer wins: Cloud Armor filters requests at the edge with allow and deny rules and adaptive protection.

### Question 9 — A

Answer: Use AlloyDB for PostgreSQL. AlloyDB is PostgreSQL-compatible with a columnar engine for mixed transactional and analytical work. Local study-map skill 1.5 (Storage and Data Store Selection), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 1 (designing and planning): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Correct. In this case: AlloyDB is PostgreSQL-compatible with a columnar engine for mixed transactional and analytical work.
- **B:** Incorrect for this question. Cloud SQL is a managed MySQL, PostgreSQL, or SQL Server instance with a familiar connection model. Why the correct answer wins: AlloyDB is PostgreSQL-compatible with a columnar engine for mixed transactional and analytical work.
- **C:** Incorrect for this question. Bigtable is a wide-column store for high-throughput key reads and writes at low latency. Why the correct answer wins: AlloyDB is PostgreSQL-compatible with a columnar engine for mixed transactional and analytical work.
- **D:** Incorrect for this question. Firestore is a document store with real-time listeners and per-document transactions. Why the correct answer wins: AlloyDB is PostgreSQL-compatible with a columnar engine for mixed transactional and analytical work.

### Question 10 — B, E

Answers: Store the objects in Archive storage class; Add a lifecycle rule that transitions and then deletes. Archive is the cheapest class for rarely read data, and the lifecycle rule deletes on age. Archive is cheapest to hold and slowest and most expensive to retrieve. A lifecycle rule acts on object age or class, so retention stops depending on a person. Local study-map skill 1.5 (Storage and Data Store Selection), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 1 (designing and planning): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. Local SSD is the fastest ephemeral option and loses its data when the VM stops. Why the correct answer wins: Archive is the cheapest class for rarely read data, and the lifecycle rule deletes on age.
- **B:** Correct. A lifecycle rule acts on object age or class, so retention stops depending on a person. In this case: Archive is the cheapest class for rarely read data, and the lifecycle rule deletes on age.
- **C:** Incorrect for this question. Filestore provides a managed NFS export that many clients can mount at once. Why the correct answer wins: Archive is the cheapest class for rarely read data, and the lifecycle rule deletes on age.
- **D:** Incorrect for this question. Standard is for data read frequently and has no retrieval fee. Why the correct answer wins: Archive is the cheapest class for rarely read data, and the lifecycle rule deletes on age.
- **E:** Correct. Archive is cheapest to hold and slowest and most expensive to retrieve. In this case: Archive is the cheapest class for rarely read data, and the lifecycle rule deletes on age.

### Question 11 — B

Answer: Use GKE Standard with a node pool per workload shape. Standard exposes node configuration and patching, which the team must then run itself. Local study-map skill 1.6 (Compute Platform Selection), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 1 (designing and planning): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. Batch schedules containerised jobs onto managed or existing capacity and retires it when done. Why the correct answer wins: Standard exposes node configuration and patching, which the team must then run itself.
- **B:** Correct. In this case: Standard exposes node configuration and patching, which the team must then run itself.
- **C:** Incorrect for this question. Autopilot manages nodes, scaling, and patching, so the team owns only the workloads. Why the correct answer wins: Standard exposes node configuration and patching, which the team must then run itself.
- **D:** Incorrect for this question. Cloud Run runs a stateless container per request and scales to zero when idle. Why the correct answer wins: Standard exposes node configuration and patching, which the team must then run itself.

### Question 12 — C

Answer: Run the legacy stack on Google Cloud VMware Engine. VMware Engine keeps the existing hypervisor and operations model while the hardware moves into Google Cloud. Local study-map skill 1.6 (Compute Platform Selection), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 1 (designing and planning): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. Cloud Run runs a stateless container per request and scales to zero when idle. Why the correct answer wins: VMware Engine keeps the existing hypervisor and operations model while the hardware moves into Google Cloud.
- **B:** Incorrect for this question. The group replaces unhealthy instances and adds capacity from a template as load rises. Why the correct answer wins: VMware Engine keeps the existing hypervisor and operations model while the hardware moves into Google Cloud.
- **C:** Correct. In this case: VMware Engine keeps the existing hypervisor and operations model while the hardware moves into Google Cloud.
- **D:** Incorrect for this question. Autopilot manages nodes, scaling, and patching, so the team owns only the workloads. Why the correct answer wins: VMware Engine keeps the existing hypervisor and operations model while the hardware moves into Google Cloud.

### Question 13 — A

Answer: Use Datastream for change data capture. Datastream reads the source log and streams inserts, updates, and deletes with ordering preserved. Local study-map skill 1.7 (Data Processing and Analytics Selection), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 1 (designing and planning): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Correct. In this case: Datastream reads the source log and streams inserts, updates, and deletes with ordering preserved.
- **B:** Incorrect for this question. Airflow expresses dependencies between scheduled jobs and retries a failed task without rerunning the rest. Why the correct answer wins: Datastream reads the source log and streams inserts, updates, and deletes with ordering preserved.
- **C:** Incorrect for this question. The service runs scheduled loads from SaaS sources and other clouds into BigQuery. Why the correct answer wins: Datastream reads the source log and streams inserts, updates, and deletes with ordering preserved.
- **D:** Incorrect for this question. Tasks dispatches HTTP or App Engine requests with rate limits and per-queue retry policy. Why the correct answer wins: Datastream reads the source log and streams inserts, updates, and deletes with ordering preserved.

### Question 14 — B, C

Answers: Publish events to Pub/Sub; Attach a dead-letter topic. Pub/Sub fans out to every subscription, and the dead-letter topic holds messages that fail repeatedly. Pub/Sub decouples producers from consumers and holds each message until every subscription acknowledges it. Local study-map skill 1.7 (Data Processing and Analytics Selection), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 1 (designing and planning): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. Scheduler fires a job on a cron or App Engine schedule and retries on failure. Why the correct answer wins: Pub/Sub fans out to every subscription, and the dead-letter topic holds messages that fail repeatedly.
- **B:** Correct. In this case: Pub/Sub fans out to every subscription, and the dead-letter topic holds messages that fail repeatedly.
- **C:** Correct. Pub/Sub decouples producers from consumers and holds each message until every subscription acknowledges it. In this case: Pub/Sub fans out to every subscription, and the dead-letter topic holds messages that fail repeatedly.
- **D:** Incorrect for this question. Eventarc delivers Google Cloud and custom events to Cloud Run, functions, or Workflows. Why the correct answer wins: Pub/Sub fans out to every subscription, and the dead-letter topic holds messages that fail repeatedly.
- **E:** Incorrect for this question. Tasks dispatches HTTP or App Engine requests with rate limits and per-queue retry policy. Why the correct answer wins: Pub/Sub fans out to every subscription, and the dead-letter topic holds messages that fail repeatedly.

### Question 15 — D

Answer: Size the training on AI Hypercomputer with TPUs. AI Hypercomputer pairs accelerators with a scheduling stack tuned for large distributed training. Local study-map skill 1.8 (AI and ML Solution Design), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 1 (designing and planning): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. Batch prediction reads a file and writes predictions without holding serving capacity. Why the correct answer wins: AI Hypercomputer pairs accelerators with a scheduling stack tuned for large distributed training.
- **B:** Incorrect for this question. A Dataproc cluster runs open-source Spark and Hadoop with jobs that need a persistent cluster. Why the correct answer wins: AI Hypercomputer pairs accelerators with a scheduling stack tuned for large distributed training.
- **C:** Incorrect for this question. Cloud Run runs a stateless container per request and scales to zero when idle. Why the correct answer wins: AI Hypercomputer pairs accelerators with a scheduling stack tuned for large distributed training.
- **D:** Correct. In this case: AI Hypercomputer pairs accelerators with a scheduling stack tuned for large distributed training.

### Question 16 — A

Answer: Use Document AI with a specialised processor. A Document AI processor extracts structured fields from forms with layout awareness. Local study-map skill 1.8 (AI and ML Solution Design), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 1 (designing and planning): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Correct. In this case: A Document AI processor extracts structured fields from forms with layout awareness.
- **B:** Incorrect for this question. The prebuilt Vision model labels, detects, and reads text without training a model. Why the correct answer wins: A Document AI processor extracts structured fields from forms with layout awareness.
- **C:** Incorrect for this question. The prebuilt speech model transcribes audio including domain phrases through adaptation. Why the correct answer wins: A Document AI processor extracts structured fields from forms with layout awareness.
- **D:** Incorrect for this question. The translation model handles 100 or more languages without custom training. Why the correct answer wins: A Document AI processor extracts structured fields from forms with layout awareness.

### Question 17 — D

Answer: Select the model from Model Garden. Model Garden lists first-party and open models with their deployment options and licensing terms. Local study-map skill 1.8 (AI and ML Solution Design), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 1 (designing and planning): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. Vertex AI Search returns grounded, cited results over private documents without a custom index. Why the correct answer wins: Model Garden lists first-party and open models with their deployment options and licensing terms.
- **B:** Incorrect for this question. Cloud Assist explains configurations and proposes changes inside the console with your permissions. Why the correct answer wins: Model Garden lists first-party and open models with their deployment options and licensing terms.
- **C:** Incorrect for this question. The kit gives code-first control over tools and state when a low-code builder is not enough. Why the correct answer wins: Model Garden lists first-party and open models with their deployment options and licensing terms.
- **D:** Correct. In this case: Model Garden lists first-party and open models with their deployment options and licensing terms.

### Question 18 — B

Answer: Assess the estate in Migration Center. Migration Center inventories the estate and estimates target size and cost before a plan is funded. Migration Center inventories the servers and estimates the target size and cost. Local study-map skill 1.9 (Migration Planning and Future Improvement), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 1 (designing and planning): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. The service moves a database with continuous replication and a short cutover window. Why the correct answer wins: Migration Center inventories the estate and estimates target size and cost before a plan is funded.
- **B:** Correct. Migration Center inventories the servers and estimates the target size and cost. In this case: Migration Center inventories the estate and estimates target size and cost before a plan is funded.
- **C:** Incorrect for this question. The tool rewrites a VM workload into a container image so it can run on GKE. Why the correct answer wins: Migration Center inventories the estate and estimates target size and cost before a plan is funded.
- **D:** Incorrect for this question. The service moves object data between buckets or clouds on a schedule. Why the correct answer wins: Migration Center inventories the estate and estimates target size and cost before a plan is funded.

### Question 19 — A

Answer: Use a Transfer Appliance for the one-off bulk move. The appliance ships the data physically when the network would take months to carry it. Local study-map skill 1.9 (Migration Planning and Future Improvement), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 1 (designing and planning): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Correct. In this case: The appliance ships the data physically when the network would take months to carry it.
- **B:** Incorrect for this question. The storage commands copy and sync objects with resumable, parallel transfers. Why the correct answer wins: The appliance ships the data physically when the network would take months to carry it.
- **C:** Incorrect for this question. The service runs scheduled, filtered transfers from another cloud or an HTTP source. Why the correct answer wins: The appliance ships the data physically when the network would take months to carry it.
- **D:** Incorrect for this question. The service moves object data between buckets or clouds on a schedule. Why the correct answer wins: The appliance ships the data physically when the network would take months to carry it.

### Question 20 — C

Answer: Set the RTO and RPO targets → choose the DR pattern that meets them → build and replicate the standby environment → fail over in a game day and record the result. Targets drive the pattern, the pattern drives the build, and only a rehearsal proves the numbers. Local study-map skill 1.3 (High Availability and Failover Design), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 1 (designing and planning): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. The pattern has no basis until the targets exist, and the drill cannot precede the build. Why the correct answer wins: Targets drive the pattern, the pattern drives the build, and only a rehearsal proves the numbers.
- **B:** Incorrect for this question. Building before the targets and pattern are chosen risks an environment that cannot meet either. Why the correct answer wins: Targets drive the pattern, the pattern drives the build, and only a rehearsal proves the numbers.
- **C:** Correct. In this case: Targets drive the pattern, the pattern drives the build, and only a rehearsal proves the numbers.
- **D:** Incorrect for this question. A failover drill with no targets or standby environment proves nothing. Why the correct answer wins: Targets drive the pattern, the pattern drives the build, and only a rehearsal proves the numbers.

### Question 21 — B

Answer: Use HA VPN with two tunnels. Two tunnels across two interfaces survive one path failing, and the SLA depends on that. Local study-map skill 2.1 (Hybrid and Multicloud Connectivity), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 2 (managing and provisioning): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. Cloud NAT lets private instances reach the internet without an external address. Why the correct answer wins: Two tunnels across two interfaces survive one path failing, and the SLA depends on that.
- **B:** Correct. In this case: Two tunnels across two interfaces survive one path failing, and the SLA depends on that.
- **C:** Incorrect for this question. CDN caches responses at edge locations, which cuts origin load and latency for repeat reads. Why the correct answer wins: Two tunnels across two interfaces survive one path failing, and the SLA depends on that.
- **D:** Incorrect for this question. A dedicated circuit gives predictable bandwidth and a private path at a colocation facility. Why the correct answer wins: Two tunnels across two interfaces survive one path failing, and the SLA depends on that.

### Question 22 — B

Answer: Attach a Serverless VPC Access connector. The connector gives serverless workloads a route to internal addresses in the VPC. Local study-map skill 2.1 (Hybrid and Multicloud Connectivity), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 2 (managing and provisioning): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. A PSC endpoint gives a private IP in the consumer VPC without peering or exposing the service publicly. Why the correct answer wins: The connector gives serverless workloads a route to internal addresses in the VPC.
- **B:** Correct. In this case: The connector gives serverless workloads a route to internal addresses in the VPC.
- **C:** Incorrect for this question. Cloud NAT lets private instances reach the internet without an external address. Why the correct answer wins: The connector gives serverless workloads a route to internal addresses in the VPC.
- **D:** Incorrect for this question. Private Google Access reaches Google APIs from an internal address without a proxy or a NAT gateway. Why the correct answer wins: The connector gives serverless workloads a route to internal addresses in the VPC.

### Question 23 — D, E

Answers: Build a Network Connectivity Center hub; Create a DNS peering zone. The hub gives transitive routing between spokes, and DNS peering resolves names without transferring the zone. The hub gives transitive routing between spokes, which peering alone cannot provide. DNS peering resolves names across networks without transferring zone ownership. Local study-map skill 2.1 (Hybrid and Multicloud Connectivity), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 2 (managing and provisioning): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. Peering joins two networks at layer three but does not share firewalls or transitive routes. Why the correct answer wins: The hub gives transitive routing between spokes, and DNS peering resolves names without transferring the zone.
- **B:** Incorrect for this question. Cloud NAT lets private instances reach the internet without an external address. Why the correct answer wins: The hub gives transitive routing between spokes, and DNS peering resolves names without transferring the zone.
- **C:** Incorrect for this question. Cloud Armor filters requests at the edge with allow and deny rules and adaptive protection. Why the correct answer wins: The hub gives transitive routing between spokes, and DNS peering resolves names without transferring the zone.
- **D:** Correct. DNS peering resolves names across networks without transferring zone ownership. In this case: The hub gives transitive routing between spokes, and DNS peering resolves names without transferring the zone.
- **E:** Correct. The hub gives transitive routing between spokes, which peering alone cannot provide. In this case: The hub gives transitive routing between spokes, and DNS peering resolves names without transferring the zone.

### Question 24 — A

Answer: Apply a bucket retention policy with a locked period. A locked retention policy prevents deletion or a shorter period, which is the evidence an auditor tests. Local study-map skill 2.2 (Storage Configuration and Lifecycle), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 2 (managing and provisioning): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Correct. In this case: A locked retention policy prevents deletion or a shorter period, which is the evidence an auditor tests.
- **B:** Incorrect for this question. A lifecycle rule acts on object age or class, so retention stops depending on a person. Why the correct answer wins: A locked retention policy prevents deletion or a shorter period, which is the evidence an auditor tests.
- **C:** Incorrect for this question. Versioning keeps a noncurrent copy when an object is overwritten or deleted. Why the correct answer wins: A locked retention policy prevents deletion or a shorter period, which is the evidence an auditor tests.
- **D:** Incorrect for this question. Autoclass moves each object between classes as its access pattern changes, with no lifecycle rules to maintain. Why the correct answer wins: A locked retention policy prevents deletion or a shorter period, which is the evidence an auditor tests.

### Question 25 — B, C

Answers: Partition the table on the date column; Create a materialized view for the repeated aggregate. Partitioning limits each query to the dates it names, and the materialized view stores the aggregate result. Partitioning limits a query to the date ranges it names, so it scans less. The view stores the aggregate result and refreshes incrementally as base data arrives. Local study-map skill 2.2 (Storage Configuration and Lifecycle), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 2 (managing and provisioning): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. Clustering sorts within partitions so a filtered query reads fewer blocks. Why the correct answer wins: Partitioning limits each query to the dates it names, and the materialized view stores the aggregate result.
- **B:** Correct. Partitioning limits a query to the date ranges it names, so it scans less. In this case: Partitioning limits each query to the dates it names, and the materialized view stores the aggregate result.
- **C:** Correct. The view stores the aggregate result and refreshes incrementally as base data arrives. In this case: Partitioning limits each query to the dates it names, and the materialized view stores the aggregate result.
- **D:** Incorrect for this question. Looker Studio renders the visualisation but inherits whatever query and permissions sit beneath it. Why the correct answer wins: Partitioning limits each query to the dates it names, and the materialized view stores the aggregate result.
- **E:** Incorrect for this question. On-demand bills per byte scanned, which is cheap for sparse use and unpredictable at scale. Why the correct answer wins: Partitioning limits each query to the dates it names, and the materialized view stores the aggregate result.

### Question 26 — C

Answer: Use Storage Transfer Service for the recurring copy. The service runs scheduled, filtered transfers from an on-premises source into a bucket. The service runs scheduled, filtered transfers from another cloud or an HTTP source. Local study-map skill 2.2 (Storage Configuration and Lifecycle), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 2 (managing and provisioning): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. The appliance ships the data physically when the network would take months to carry it. Why the correct answer wins: The service runs scheduled, filtered transfers from an on-premises source into a bucket.
- **B:** Incorrect for this question. A signed URL grants one object for a fixed time without exposing credentials or making the bucket public. Why the correct answer wins: The service runs scheduled, filtered transfers from an on-premises source into a bucket.
- **C:** Correct. The service runs scheduled, filtered transfers from another cloud or an HTTP source. In this case: The service runs scheduled, filtered transfers from an on-premises source into a bucket.
- **D:** Incorrect for this question. The service moves object data between buckets or clouds on a schedule. Why the correct answer wins: The service runs scheduled, filtered transfers from an on-premises source into a bucket.

### Question 27 — A, B

Answers: Run the batch tier on Spot VMs; Buy committed use discounts for the steady baseline. Spot covers the restartable burst, and a commitment discounts the capacity that runs constantly. Spot capacity costs far less but can be reclaimed with 30 seconds of notice. A one- or three-year commitment discounts the capacity that runs constantly, not the peaks. Local study-map skill 2.3 (Compute Provisioning and Patch Management), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 2 (managing and provisioning): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Correct. A one- or three-year commitment discounts the capacity that runs constantly, not the peaks. In this case: Spot covers the restartable burst, and a commitment discounts the capacity that runs constantly.
- **B:** Correct. Spot capacity costs far less but can be reclaimed with 30 seconds of notice. In this case: Spot covers the restartable burst, and a commitment discounts the capacity that runs constantly.
- **C:** Incorrect for this question. VM Manager inventories and applies OS patches across a fleet instead of relying on manual runs. Why the correct answer wins: Spot covers the restartable burst, and a commitment discounts the capacity that runs constantly.
- **D:** Incorrect for this question. Custom vCPU and memory avoid paying for a fixed shape that over-provisions one dimension. Why the correct answer wins: Spot covers the restartable burst, and a commitment discounts the capacity that runs constantly.
- **E:** Incorrect for this question. Sole tenancy keeps the physical host dedicated, which matters for licensing or isolation rules. Why the correct answer wins: Spot covers the restartable burst, and a commitment discounts the capacity that runs constantly.

### Question 28 — D

Answer: Enforce Binary Authorization at admission. The admission controller rejects images without a valid attestation, so an unverified build cannot start. Local study-map skill 2.4 (Container Orchestration), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 2 (managing and provisioning): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. A fleet gives one policy and identity plane across clusters without merging their networks. Why the correct answer wins: The admission controller rejects images without a valid attestation, so an unverified build cannot start.
- **B:** Incorrect for this question. Network policy restricts pod-to-pod traffic inside the cluster, which a firewall rule cannot see. Why the correct answer wins: The admission controller rejects images without a valid attestation, so an unverified build cannot start.
- **C:** Incorrect for this question. Auto-provisioning adds node pools on demand for pending pods instead of pre-sizing them. Why the correct answer wins: The admission controller rejects images without a valid attestation, so an unverified build cannot start.
- **D:** Correct. In this case: The admission controller rejects images without a valid attestation, so an unverified build cannot start.

### Question 29 — C, E

Answers: Enable Workload Identity Federation for GKE; Create private nodes with no external IP addresses. Workload Identity binds the pod identity to IAM, and private nodes remove external addressing. The feature binds a Kubernetes service account to an IAM service account, so pods hold no keys. Private nodes reach Google APIs through Private Google Access and cannot be addressed from the internet. Local study-map skill 2.4 (Container Orchestration), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 2 (managing and provisioning): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. A key file is a long-lived credential that works until it is noticed and revoked. Why the correct answer wins: Workload Identity binds the pod identity to IAM, and private nodes remove external addressing.
- **B:** Incorrect for this question. Cloud NAT lets private instances reach the internet without an external address. Why the correct answer wins: Workload Identity binds the pod identity to IAM, and private nodes remove external addressing.
- **C:** Correct. The feature binds a Kubernetes service account to an IAM service account, so pods hold no keys. In this case: Workload Identity binds the pod identity to IAM, and private nodes remove external addressing.
- **D:** Incorrect for this question. Sole tenancy keeps the physical host dedicated, which matters for licensing or isolation rules. Why the correct answer wins: Workload Identity binds the pod identity to IAM, and private nodes remove external addressing.
- **E:** Correct. Private nodes reach Google APIs through Private Google Access and cannot be addressed from the internet. In this case: Workload Identity binds the pod identity to IAM, and private nodes remove external addressing.

### Question 30 — D

Answer: Create the project and enable APIs → build a Shared VPC with private subnets → create a regional private cluster with Workload Identity Federation for GKE → deploy through Binary Authorization. Network and identity exist before the cluster, and the admission policy is enforceable only once the cluster is running. Local study-map skill 2.4 (Container Orchestration), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 2 (managing and provisioning): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. The project precedes its network, and the deploy step belongs after the cluster rather than in the middle. Why the correct answer wins: Network and identity exist before the cluster, and the admission policy is enforceable only once the cluster is running.
- **B:** Incorrect for this question. A private cluster needs the shared network first, and the APIs must be enabled before any resource is created. Why the correct answer wins: Network and identity exist before the cluster, and the admission policy is enforceable only once the cluster is running.
- **C:** Incorrect for this question. Admission control cannot run before a cluster exists, and no resource can be created before its project. Why the correct answer wins: Network and identity exist before the cluster, and the admission policy is enforceable only once the cluster is running.
- **D:** Correct. In this case: Network and identity exist before the cluster, and the admission policy is enforceable only once the cluster is running.

### Question 31 — B

Answer: Set a minimum instance count on the Cloud Run service. A minimum instance count keeps warm capacity ready before the first request arrives. Keeping warm instances removes cold starts at the cost of paying for idle capacity. Local study-map skill 2.5 (Serverless Configuration), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 2 (managing and provisioning): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. Serverless GPU attachment suits bursty inference where a reserved node would idle. Why the correct answer wins: A minimum instance count keeps warm capacity ready before the first request arrives.
- **B:** Correct. Keeping warm instances removes cold starts at the cost of paying for idle capacity. In this case: A minimum instance count keeps warm capacity ready before the first request arrives.
- **C:** Incorrect for this question. The flexible environment runs a custom runtime on managed VMs but does not scale to zero. Why the correct answer wins: A minimum instance count keeps warm capacity ready before the first request arrives.
- **D:** Incorrect for this question. Concurrency packs more simultaneous requests into each instance before another is started. Why the correct answer wins: A minimum instance count keeps warm capacity ready before the first request arrives.

### Question 32 — A

Answer: Manage the resources with Config Connector. Config Connector reconciles Google Cloud resources from Kubernetes manifests alongside the workloads. Local study-map skill 2.6 (Infrastructure as Code), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 2 (managing and provisioning): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Correct. In this case: Config Connector reconciles Google Cloud resources from Kubernetes manifests alongside the workloads.
- **B:** Incorrect for this question. Deployment Manager is the native but older templating service with no plan step. Why the correct answer wins: Config Connector reconciles Google Cloud resources from Kubernetes manifests alongside the workloads.
- **C:** Incorrect for this question. Terraform holds desired state in code, plans the diff, and applies it through a provider. Why the correct answer wins: Config Connector reconciles Google Cloud resources from Kubernetes manifests alongside the workloads.
- **D:** Incorrect for this question. The CLI exposes every API as a command that can be scripted and logged. Why the correct answer wins: Config Connector reconciles Google Cloud resources from Kubernetes manifests alongside the workloads.

### Question 33 — B

Answer: Deploy to an online prediction endpoint. An endpoint keeps serving capacity ready for low-latency per-request predictions. Local study-map skill 2.7 (Agent Platform ML Workflows), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 2 (managing and provisioning): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. Pub/Sub decouples producers from consumers and holds each message until every subscription acknowledges it. Why the correct answer wins: An endpoint keeps serving capacity ready for low-latency per-request predictions.
- **B:** Correct. In this case: An endpoint keeps serving capacity ready for low-latency per-request predictions.
- **C:** Incorrect for this question. AI Hypercomputer pairs accelerators with a scheduling stack tuned for large distributed training. Why the correct answer wins: An endpoint keeps serving capacity ready for low-latency per-request predictions.
- **D:** Incorrect for this question. Batch prediction reads a file and writes predictions without holding serving capacity. Why the correct answer wins: An endpoint keeps serving capacity ready for low-latency per-request predictions.

### Question 34 — D

Answer: Select the model from Model Garden. Model Garden lists first-party and open models with their deployment options and licensing terms. Local study-map skill 2.8 (Prebuilt AI APIs and Model Garden), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 2 (managing and provisioning): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. Vertex AI Search returns grounded, cited results over private documents without a custom index. Why the correct answer wins: Model Garden lists first-party and open models with their deployment options and licensing terms.
- **B:** Incorrect for this question. Cloud Assist explains configurations and proposes changes inside the console with your permissions. Why the correct answer wins: Model Garden lists first-party and open models with their deployment options and licensing terms.
- **C:** Incorrect for this question. The kit gives code-first control over tools and state when a low-code builder is not enough. Why the correct answer wins: Model Garden lists first-party and open models with their deployment options and licensing terms.
- **D:** Correct. In this case: Model Garden lists first-party and open models with their deployment options and licensing terms.

### Question 35 — A

Answer: Curate and version the training data → train and evaluate the model in a pipeline → register the model and record its metrics → deploy to an endpoint with traffic splitting and model monitoring. Data precedes training, the registry holds the evaluated artifact, and monitoring starts with the serving endpoint. Local study-map skill 2.8 (Prebuilt AI APIs and Model Garden), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 2 (managing and provisioning): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Correct. In this case: Data precedes training, the registry holds the evaluated artifact, and monitoring starts with the serving endpoint.
- **B:** Incorrect for this question. Registration follows training, and training follows the data. Why the correct answer wins: Data precedes training, the registry holds the evaluated artifact, and monitoring starts with the serving endpoint.
- **C:** Incorrect for this question. Serving an untrained, unregistered model has nothing to deploy. Why the correct answer wins: Data precedes training, the registry holds the evaluated artifact, and monitoring starts with the serving endpoint.
- **D:** Incorrect for this question. Training without curated data and deploying without registration both skip a required stage. Why the correct answer wins: Data precedes training, the registry holds the evaluated artifact, and monitoring starts with the serving endpoint.

### Question 36 — B

Answer: Define a custom role with only the required permissions. A custom role expresses least privilege when no predefined role matches the job exactly. Local study-map skill 3.1 (IAM and Least Privilege), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 3 (security and compliance): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. A predefined role grants the curated permission set for one job at the level it is bound to. Why the correct answer wins: A custom role expresses least privilege when no predefined role matches the job exactly.
- **B:** Correct. In this case: A custom role expresses least privilege when no predefined role matches the job exactly.
- **C:** Incorrect for this question. An API key identifies a project and does not authorise a user, so it cannot express least privilege. Why the correct answer wins: A custom role expresses least privilege when no predefined role matches the job exactly.
- **D:** Incorrect for this question. A bastion is still an internet-facing host that must be patched and watched. Why the correct answer wins: A custom role expresses least privilege when no predefined role matches the job exactly.

### Question 37 — A

Answer: Create a folder per environment and bind roles there. A folder binding inherits to every project beneath it, so new projects start with the right access. Local study-map skill 3.2 (Resource Hierarchy and Organization Policy), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 3 (security and compliance): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Correct. In this case: A folder binding inherits to every project beneath it, so new projects start with the right access.
- **B:** Incorrect for this question. A predefined role grants the curated permission set for one job at the level it is bound to. Why the correct answer wins: A folder binding inherits to every project beneath it, so new projects start with the right access.
- **C:** Incorrect for this question. Labels attribute spend in billing export; they do not grant or restrict access. Why the correct answer wins: A folder binding inherits to every project beneath it, so new projects start with the right access.
- **D:** Incorrect for this question. A project is the boundary for quota, billing, and most IAM inheritance. Why the correct answer wins: A folder binding inherits to every project beneath it, so new projects start with the right access.

### Question 38 — A, B

Answers: Enforce the control with an organization policy constraint; Apply an IAM deny policy. The policy blocks the action across every project, and the deny policy overrides every allow beneath it. An organization policy blocks the action across every project regardless of who holds the role. A deny policy overrides every allow beneath it, which is how an exception is made impossible. Local study-map skill 3.2 (Resource Hierarchy and Organization Policy), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 3 (security and compliance): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Correct. An organization policy blocks the action across every project regardless of who holds the role. In this case: The policy blocks the action across every project, and the deny policy overrides every allow beneath it.
- **B:** Correct. A deny policy overrides every allow beneath it, which is how an exception is made impossible. In this case: The policy blocks the action across every project, and the deny policy overrides every allow beneath it.
- **C:** Incorrect for this question. A folder binding inherits to every project beneath it, so new projects start with the right access. Why the correct answer wins: The policy blocks the action across every project, and the deny policy overrides every allow beneath it.
- **D:** Incorrect for this question. A condition narrows when a grant applies, for example to a time window or a resource prefix. Why the correct answer wins: The policy blocks the action across every project, and the deny policy overrides every allow beneath it.
- **E:** Incorrect for this question. Labels attribute spend in billing export; they do not grant or restrict access. Why the correct answer wins: The policy blocks the action across every project, and the deny policy overrides every allow beneath it.

### Question 39 — C

Answer: Use Cloud HSM for the key. Cloud HSM keeps the key material in a hardware module that meets FIPS 140-2 level 3. Local study-map skill 3.3 (Encryption, CMEK, and Secrets), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 3 (security and compliance): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. CSEK is held by the caller and never stored by Google, so losing it loses the object. Why the correct answer wins: Cloud HSM keeps the key material in a hardware module that meets FIPS 140-2 level 3.
- **B:** Incorrect for this question. A regional key cannot encrypt a resource in another region, which is why residency drives key placement. Why the correct answer wins: Cloud HSM keeps the key material in a hardware module that meets FIPS 140-2 level 3.
- **C:** Correct. In this case: Cloud HSM keeps the key material in a hardware module that meets FIPS 140-2 level 3.
- **D:** Incorrect for this question. Secret Manager versions the secret, controls access by IAM, and can rotate it. Why the correct answer wins: Cloud HSM keeps the key material in a hardware module that meets FIPS 140-2 level 3.

### Question 40 — B, E

Answers: Encrypt with a customer-managed key in Cloud KMS; Set an automatic rotation period on the key. A customer-managed key gives the hospital control, and automatic rotation issues a new version on schedule. CMEK lets you control the key lifecycle, rotation, and the ability to revoke access to the data. Rotation issues a new key version on schedule and keeps old versions for decryption. Local study-map skill 3.3 (Encryption, CMEK, and Secrets), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 3 (security and compliance): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. Secret Manager versions the secret, controls access by IAM, and can rotate it. Why the correct answer wins: A customer-managed key gives the hospital control, and automatic rotation issues a new version on schedule.
- **B:** Correct. Rotation issues a new key version on schedule and keeps old versions for decryption. In this case: A customer-managed key gives the hospital control, and automatic rotation issues a new version on schedule.
- **C:** Incorrect for this question. An environment variable is visible to anything that can read the instance metadata or the process list. Why the correct answer wins: A customer-managed key gives the hospital control, and automatic rotation issues a new version on schedule.
- **D:** Incorrect for this question. CSEK is held by the caller and never stored by Google, so losing it loses the object. Why the correct answer wins: A customer-managed key gives the hospital control, and automatic rotation issues a new version on schedule.
- **E:** Correct. CMEK lets you control the key lifecycle, rotation, and the ability to revoke access to the data. In this case: A customer-managed key gives the hospital control, and automatic rotation issues a new version on schedule.

### Question 41 — B

Answer: Run the perimeter in dry-run mode first. Dry-run mode logs the requests that would be blocked without breaking a legitimate flow. Local study-map skill 3.4 (VPC Service Controls and Network Security), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 3 (security and compliance): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. An aggregated sink collects logs from every project in the organization into one destination. Why the correct answer wins: Dry-run mode logs the requests that would be blocked without breaking a legitimate flow.
- **B:** Correct. In this case: Dry-run mode logs the requests that would be blocked without breaking a legitimate flow.
- **C:** Incorrect for this question. Cloud Armor filters requests at the edge with allow and deny rules and adaptive protection. Why the correct answer wins: Dry-run mode logs the requests that would be blocked without breaking a legitimate flow.
- **D:** Incorrect for this question. The perimeter blocks data movement out of the services it covers even for a principal with the role. Why the correct answer wins: Dry-run mode logs the requests that would be blocked without breaking a legitimate flow.

### Question 42 — B

Answer: Allocate private services access for the peered services. The allocated range lets managed services use internal addresses in your network. Local study-map skill 3.4 (VPC Service Controls and Network Security), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 3 (security and compliance): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. Private Google Access reaches Google APIs from an internal address without a proxy or a NAT gateway. Why the correct answer wins: The allocated range lets managed services use internal addresses in your network.
- **B:** Correct. In this case: The allocated range lets managed services use internal addresses in your network.
- **C:** Incorrect for this question. A PSC endpoint gives a private IP in the consumer VPC without peering or exposing the service publicly. Why the correct answer wins: The allocated range lets managed services use internal addresses in your network.
- **D:** Incorrect for this question. Cloud NAT lets private instances reach the internet without an external address. Why the correct answer wins: The allocated range lets managed services use internal addresses in your network.

### Question 43 — D

Answer: Use Chrome Enterprise Premium for the workforce. Context-aware access evaluates device and identity signals for every application, not just the network. Local study-map skill 3.5 (Secure Remote Access and Zero Trust), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 3 (security and compliance): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. An API key identifies a project and does not authorise a user, so it cannot express least privilege. Why the correct answer wins: Context-aware access evaluates device and identity signals for every application, not just the network.
- **B:** Incorrect for this question. Cloud NAT lets private instances reach the internet without an external address. Why the correct answer wins: Context-aware access evaluates device and identity signals for every application, not just the network.
- **C:** Incorrect for this question. A bastion is still an internet-facing host that must be patched and watched. Why the correct answer wins: Context-aware access evaluates device and identity signals for every application, not just the network.
- **D:** Correct. In this case: Context-aware access evaluates device and identity signals for every application, not just the network.

### Question 44 — B

Answer: Record build provenance for the artifact. Provenance states what built the artifact from which source, which is the evidence a supply-chain audit asks for. Local study-map skill 3.6 (Software Supply Chain Security), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 3 (security and compliance): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. Network policy restricts pod-to-pod traffic inside the cluster, which a firewall rule cannot see. Why the correct answer wins: Provenance states what built the artifact from which source, which is the evidence a supply-chain audit asks for.
- **B:** Correct. In this case: Provenance states what built the artifact from which source, which is the evidence a supply-chain audit asks for.
- **C:** Incorrect for this question. Artifact Registry holds the image with IAM-scoped access and vulnerability metadata. Why the correct answer wins: Provenance states what built the artifact from which source, which is the evidence a supply-chain audit asks for.
- **D:** Incorrect for this question. Scanning reports known vulnerabilities in the image layers before deployment. Why the correct answer wins: Provenance states what built the artifact from which source, which is the evidence a supply-chain audit asks for.

### Question 45 — A

Answer: Screen prompts and responses with Model Armor. Model Armor detects prompt injection and unsafe content before and after the model call. Local study-map skill 3.7 (Securing AI Workloads), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 3 (security and compliance): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Correct. In this case: Model Armor detects prompt injection and unsafe content before and after the model call.
- **B:** Incorrect for this question. Security Command Center aggregates misconfiguration and threat findings across the organization. Why the correct answer wins: Model Armor detects prompt injection and unsafe content before and after the model call.
- **C:** Incorrect for this question. Sensitive Data Protection finds and redacts, tokenizes, or format-preservingly encrypts sensitive fields. Why the correct answer wins: Model Armor detects prompt injection and unsafe content before and after the model call.
- **D:** Incorrect for this question. The access level adds device and network conditions to the perimeter rule. Why the correct answer wins: Model Armor detects prompt injection and unsafe content before and after the model call.

### Question 46 — C

Answer: Use a locked log bucket with a fixed retention. A locked bucket prevents deletion and retention changes for the period the auditor requires. Local study-map skill 3.8 (Compliance, Residency, and Audit Logging), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 3 (security and compliance): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. Admin Activity records configuration changes and cannot be disabled. Why the correct answer wins: A locked bucket prevents deletion and retention changes for the period the auditor requires.
- **B:** Incorrect for this question. The metric turns a log pattern into a series that can be alerted on and charted. Why the correct answer wins: A locked bucket prevents deletion and retention changes for the period the auditor requires.
- **C:** Correct. In this case: A locked bucket prevents deletion and retention changes for the period the auditor requires.
- **D:** Incorrect for this question. A locked retention policy prevents deletion or shortening, which is what an auditor tests. Why the correct answer wins: A locked bucket prevents deletion and retention changes for the period the auditor requires.

### Question 47 — C

Answer: Enable data access audit logs for the services in scope → create a locked log bucket with the required retention → route the logs with an aggregated sink → query and export the evidence for the auditor. Logs must be enabled before they can be routed, and retention is fixed on the bucket before the sink writes to it. Local study-map skill 3.8 (Compliance, Residency, and Audit Logging), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 3 (security and compliance): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. A sink that is created last is needed before any evidence can be queried from the destination. Why the correct answer wins: Logs must be enabled before they can be routed, and retention is fixed on the bucket before the sink writes to it.
- **B:** Incorrect for this question. There is no evidence to query before logging and routing exist. Why the correct answer wins: Logs must be enabled before they can be routed, and retention is fixed on the bucket before the sink writes to it.
- **C:** Correct. In this case: Logs must be enabled before they can be routed, and retention is fixed on the bucket before the sink writes to it.
- **D:** Incorrect for this question. A sink without a destination bucket or enabled logs captures nothing. Why the correct answer wins: Logs must be enabled before they can be routed, and retention is fixed on the bucket before the sink writes to it.

### Question 48 — D

Answer: Adopt trunk-based development with short-lived branches. Short-lived branches reduce merge conflict and keep the mainline deployable. Local study-map skill 4.1 (SDLC and CI/CD Design), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 4 (analyzing and optimizing): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. A rolling replacement keeps capacity but exposes the whole fleet before the signal is trusted. Why the correct answer wins: Short-lived branches reduce merge conflict and keep the mainline deployable.
- **B:** Incorrect for this question. The flag separates deployment from release, so the code can ship dark and be turned off instantly. Why the correct answer wins: Short-lived branches reduce merge conflict and keep the mainline deployable.
- **C:** Incorrect for this question. A rebuild produces a different artifact, so the test result no longer applies to production. Why the correct answer wins: Short-lived branches reduce merge conflict and keep the mainline deployable.
- **D:** Correct. In this case: Short-lived branches reduce merge conflict and keep the mainline deployable.

### Question 49 — A, C

Answers: Cover the change with unit, integration, and a few end-to-end tests; Add a contract test on the API. The pyramid puts test volume where it is cheap, and a contract test fails the build on a breaking change. The pyramid puts volume where it is cheap and keeps end-to-end tests for the critical paths. The contract test fails the build when a breaking change reaches a consumer. Local study-map skill 4.1 (SDLC and CI/CD Design), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 4 (analyzing and optimizing): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Correct. The pyramid puts volume where it is cheap and keeps end-to-end tests for the critical paths. In this case: The pyramid puts test volume where it is cheap, and a contract test fails the build on a breaking change.
- **B:** Incorrect for this question. The experiment proves the failover path works while the impact is controlled. Why the correct answer wins: The pyramid puts test volume where it is cheap, and a contract test fails the build on a breaking change.
- **C:** Correct. The contract test fails the build when a breaking change reaches a consumer. In this case: The pyramid puts test volume where it is cheap, and a contract test fails the build on a breaking change.
- **D:** Incorrect for this question. The load test measures the system at the concurrency the business expects, before launch. Why the correct answer wins: The pyramid puts test volume where it is cheap, and a contract test fails the build on a breaking change.
- **E:** Incorrect for this question. An independent test attempts the attack the design claims to prevent. Why the correct answer wins: The pyramid puts test volume where it is cheap, and a contract test fails the build on a breaking change.

### Question 50 — B

Answer: Attach Cloud Profiler to the service. Profiler samples the running code and attributes CPU and heap to the functions responsible. Local study-map skill 4.2 (Root Cause Analysis), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 4 (analyzing and optimizing): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. The check measures availability from outside, which no internal metric can prove. Why the correct answer wins: Profiler samples the running code and attributes CPU and heap to the functions responsible.
- **B:** Correct. In this case: Profiler samples the running code and attributes CPU and heap to the functions responsible.
- **C:** Incorrect for this question. Trace shows how one request spent its time across services and calls. Why the correct answer wins: Profiler samples the running code and attributes CPU and heap to the functions responsible.
- **D:** Incorrect for this question. The dashboard gives the team one view of the same signals during an incident. Why the correct answer wins: Profiler samples the running code and attributes CPU and heap to the functions responsible.

### Question 51 — D, E

Answers: Query the entries in Cloud Logging; Inspect the trace waterfall in Cloud Trace. Logging holds the event text, and Trace shows how one request spent its time across services. Logging holds the event text and structured fields that explain what happened at a moment. Trace shows how one request spent its time across services and calls. Local study-map skill 4.2 (Root Cause Analysis), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 4 (analyzing and optimizing): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. The dashboard gives the team one view of the same signals during an incident. Why the correct answer wins: Logging holds the event text, and Trace shows how one request spent its time across services.
- **B:** Incorrect for this question. The runbook records the diagnostic steps so the response does not depend on who is awake. Why the correct answer wins: Logging holds the event text, and Trace shows how one request spent its time across services.
- **C:** Incorrect for this question. An SLO ties the alert to the promise the users care about rather than to a raw resource threshold. Why the correct answer wins: Logging holds the event text, and Trace shows how one request spent its time across services.
- **D:** Correct. Trace shows how one request spent its time across services and calls. In this case: Logging holds the event text, and Trace shows how one request spent its time across services.
- **E:** Correct. Logging holds the event text and structured fields that explain what happened at a moment. In this case: Logging holds the event text, and Trace shows how one request spent its time across services.

### Question 52 — B

Answer: Commission a penetration test. An independent test attempts the attack the design claims to prevent. Local study-map skill 4.3 (Testing and Validation), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 4 (analyzing and optimizing): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. The pyramid puts volume where it is cheap and keeps end-to-end tests for the critical paths. Why the correct answer wins: An independent test attempts the attack the design claims to prevent.
- **B:** Correct. In this case: An independent test attempts the attack the design claims to prevent.
- **C:** Incorrect for this question. The experiment proves the failover path works while the impact is controlled. Why the correct answer wins: An independent test attempts the attack the design claims to prevent.
- **D:** Incorrect for this question. The load test measures the system at the concurrency the business expects, before launch. Why the correct answer wins: An independent test attempts the attack the design claims to prevent.

### Question 53 — D

Answer: Run a chaos experiment against a zone. The experiment proves the failover path works while the impact is controlled. Local study-map skill 4.3 (Testing and Validation), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 4 (analyzing and optimizing): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. A canary limits the blast radius while the error and latency signals are compared. Why the correct answer wins: The experiment proves the failover path works while the impact is controlled.
- **B:** Incorrect for this question. An independent test attempts the attack the design claims to prevent. Why the correct answer wins: The experiment proves the failover path works while the impact is controlled.
- **C:** Incorrect for this question. The load test measures the system at the concurrency the business expects, before launch. Why the correct answer wins: The experiment proves the failover path works while the impact is controlled.
- **D:** Correct. In this case: The experiment proves the failover path works while the impact is controlled.

### Question 54 — C

Answer: Run a warm standby at reduced capacity. A running but smaller copy recovers in a short window at a continuous cost. Local study-map skill 4.4 (Disaster Recovery and Business Continuity), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 4 (analyzing and optimizing): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. Restoring from backup is the cheapest option and the slowest to recover. Why the correct answer wins: A running but smaller copy recovers in a short window at a continuous cost.
- **B:** Incorrect for this question. Only the core data and configuration stay warm, so recovery starts the compute and takes minutes. Why the correct answer wins: A running but smaller copy recovers in a short window at a continuous cost.
- **C:** Correct. In this case: A running but smaller copy recovers in a short window at a continuous cost.
- **D:** Incorrect for this question. Both regions serve traffic, so a regional loss is absorbed without a failover decision. Why the correct answer wins: A running but smaller copy recovers in a short window at a continuous cost.

### Question 55 — B

Answer: Act on the Recommender suggestions. Recommender reports idle and over-provisioned resources with the estimated saving for each. Local study-map skill 4.5 (Cost Optimization), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 4 (analyzing and optimizing): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. A budget alerts on spend but does not stop it. Why the correct answer wins: Recommender reports idle and over-provisioned resources with the estimated saving for each.
- **B:** Correct. In this case: Recommender reports idle and over-provisioned resources with the estimated saving for each.
- **C:** Incorrect for this question. The export attributes cost to the team and service that caused it. Why the correct answer wins: Recommender reports idle and over-provisioned resources with the estimated saving for each.
- **D:** Incorrect for this question. Labels attribute spend in billing export; they do not grant or restrict access. Why the correct answer wins: Recommender reports idle and over-provisioned resources with the estimated saving for each.

### Question 56 — C

Answer: Agree the decision rights with the stakeholders. Naming who decides each trade-off prevents the design being reopened late in delivery. Local study-map skill 4.6 (Stakeholder and Change Management), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 4 (analyzing and optimizing): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. The runbook records the diagnostic steps so the response does not depend on who is awake. Why the correct answer wins: Naming who decides each trade-off prevents the design being reopened late in delivery.
- **B:** Incorrect for this question. A catalog entry gives teams a pre-approved, policy-compliant way to request the resource. Why the correct answer wins: Naming who decides each trade-off prevents the design being reopened late in delivery.
- **C:** Correct. In this case: Naming who decides each trade-off prevents the design being reopened late in delivery.
- **D:** Incorrect for this question. The board reviews risk and timing for changes that affect regulated or shared systems. Why the correct answer wins: Naming who decides each trade-off prevents the design being reopened late in delivery.

### Question 57 — B

Answer: Publish a service catalog entry with an approved template. A catalog entry gives teams a pre-approved, policy-compliant way to request the resource. Local study-map skill 4.7 (Service Catalog and Provisioning), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 4 (analyzing and optimizing): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. Labels attribute spend in billing export; they do not grant or restrict access. Why the correct answer wins: A catalog entry gives teams a pre-approved, policy-compliant way to request the resource.
- **B:** Correct. In this case: A catalog entry gives teams a pre-approved, policy-compliant way to request the resource.
- **C:** Incorrect for this question. An organization policy blocks the action across every project regardless of who holds the role. Why the correct answer wins: A catalog entry gives teams a pre-approved, policy-compliant way to request the resource.
- **D:** Incorrect for this question. Terraform holds desired state in code, plans the diff, and applies it through a provider. Why the correct answer wins: A catalog entry gives teams a pre-approved, policy-compliant way to request the resource.

### Question 58 — A

Answer: Detect the symptom through an alert → contain the impact and restore service → isolate the root cause from logs, traces, and metrics → apply the permanent fix and write the postmortem. Service recovery comes before deep analysis, and the postmortem follows the fix. Local study-map skill 4.2 (Root Cause Analysis), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 4 (analyzing and optimizing): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Correct. In this case: Service recovery comes before deep analysis, and the postmortem follows the fix.
- **B:** Incorrect for this question. Detection precedes analysis, and the postmortem follows restoration rather than preceding it. Why the correct answer wins: Service recovery comes before deep analysis, and the postmortem follows the fix.
- **C:** Incorrect for this question. A postmortem cannot be written before the incident has happened and been resolved. Why the correct answer wins: Service recovery comes before deep analysis, and the postmortem follows the fix.
- **D:** Incorrect for this question. Service cannot be restored before the alert fires, and the root cause is isolated before the postmortem. Why the correct answer wins: Service recovery comes before deep analysis, and the postmortem follows the fix.

### Question 59 — B

Answer: Inspect the query plan and bytes processed → partition and cluster the table on the filter columns → rewrite the query to prune partitions → measure the new slot time and bytes scanned. The plan identifies the problem, the physical design supports pruning, and only a measurement proves improvement. Local study-map skill 4.5 (Cost Optimization), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 4 (analyzing and optimizing): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. Measuring before any change establishes no baseline against the plan. Why the correct answer wins: The plan identifies the problem, the physical design supports pruning, and only a measurement proves improvement.
- **B:** Correct. In this case: The plan identifies the problem, the physical design supports pruning, and only a measurement proves improvement.
- **C:** Incorrect for this question. The plan is the evidence that drives both the rewrite and the physical design. Why the correct answer wins: The plan identifies the problem, the physical design supports pruning, and only a measurement proves improvement.
- **D:** Incorrect for this question. Partitioning last ignores what the plan and the rewrite revealed. Why the correct answer wins: The plan identifies the problem, the physical design supports pruning, and only a measurement proves improvement.

### Question 60 — A

Answer: Deploy blue/green with a traffic switch. Two identical environments let the switch be reversed instantly if the new one misbehaves. Local study-map skill 5.1 (Deployment and Release Strategy), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 5 (managing implementation): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Correct. In this case: Two identical environments let the switch be reversed instantly if the new one misbehaves.
- **B:** Incorrect for this question. A rolling replacement keeps capacity but exposes the whole fleet before the signal is trusted. Why the correct answer wins: Two identical environments let the switch be reversed instantly if the new one misbehaves.
- **C:** Incorrect for this question. The flag separates deployment from release, so the code can ship dark and be turned off instantly. Why the correct answer wins: Two identical environments let the switch be reversed instantly if the new one misbehaves.
- **D:** Incorrect for this question. A canary limits the blast radius while the error and latency signals are compared. Why the correct answer wins: Two identical environments let the switch be reversed instantly if the new one misbehaves.

### Question 61 — A

Answer: Put the change behind a feature flag. The flag separates deployment from release, so the code can ship dark and be turned off instantly. Local study-map skill 5.1 (Deployment and Release Strategy), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 5 (managing implementation): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Correct. In this case: The flag separates deployment from release, so the code can ship dark and be turned off instantly.
- **B:** Incorrect for this question. Two identical environments let the switch be reversed instantly if the new one misbehaves. Why the correct answer wins: The flag separates deployment from release, so the code can ship dark and be turned off instantly.
- **C:** Incorrect for this question. A rolling replacement keeps capacity but exposes the whole fleet before the signal is trusted. Why the correct answer wins: The flag separates deployment from release, so the code can ship dark and be turned off instantly.
- **D:** Incorrect for this question. A canary limits the blast radius while the error and latency signals are compared. Why the correct answer wins: The flag separates deployment from release, so the code can ship dark and be turned off instantly.

### Question 62 — B, E

Answers: Roll out a canary to a small share of traffic; Keep the previous image digest ready for rollback. A canary limits the blast radius, and a pinned digest restores the exact artifact that was known good. A canary limits the blast radius while the error and latency signals are compared. Local study-map skill 5.1 (Deployment and Release Strategy), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 5 (managing implementation): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. A budget alerts on spend but does not stop it. Why the correct answer wins: A canary limits the blast radius, and a pinned digest restores the exact artifact that was known good.
- **B:** Correct. In this case: A canary limits the blast radius, and a pinned digest restores the exact artifact that was known good.
- **C:** Incorrect for this question. A rebuild produces a different artifact, so the test result no longer applies to production. Why the correct answer wins: A canary limits the blast radius, and a pinned digest restores the exact artifact that was known good.
- **D:** Incorrect for this question. Promotion moves one immutable artifact forward, so what was tested is what runs. Why the correct answer wins: A canary limits the blast radius, and a pinned digest restores the exact artifact that was known good.
- **E:** Correct. A canary limits the blast radius while the error and latency signals are compared. In this case: A canary limits the blast radius, and a pinned digest restores the exact artifact that was known good.

### Question 63 — D

Answer: Publish the API through Apigee. Apigee adds quotas, keys, mediation, and analytics at the gateway for each consumer. Local study-map skill 5.2 (API Management), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 5 (managing implementation): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. API Gateway fronts a Cloud Run or functions backend with a managed OpenAPI definition. Why the correct answer wins: Apigee adds quotas, keys, mediation, and analytics at the gateway for each consumer.
- **B:** Incorrect for this question. Cloud Armor filters requests at the edge with allow and deny rules and adaptive protection. Why the correct answer wins: Apigee adds quotas, keys, mediation, and analytics at the gateway for each consumer.
- **C:** Incorrect for this question. Endpoints validates and monitors an API described by an OpenAPI or gRPC spec. Why the correct answer wins: Apigee adds quotas, keys, mediation, and analytics at the gateway for each consumer.
- **D:** Correct. In this case: Apigee adds quotas, keys, mediation, and analytics at the gateway for each consumer.

### Question 64 — A, C

Answers: Publish a versioning and deprecation policy; Add a contract test on the API. The policy states when a version is removed, and the contract test stops a breaking change reaching consumers. The policy tells consumers how long a version lives and when it is removed. The contract test fails the build when a breaking change reaches a consumer. Local study-map skill 5.2 (API Management), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 5 (managing implementation): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Correct. The contract test fails the build when a breaking change reaches a consumer. In this case: The policy states when a version is removed, and the contract test stops a breaking change reaching consumers.
- **B:** Incorrect for this question. An API key identifies a project and does not authorise a user, so it cannot express least privilege. Why the correct answer wins: The policy states when a version is removed, and the contract test stops a breaking change reaching consumers.
- **C:** Correct. The policy tells consumers how long a version lives and when it is removed. In this case: The policy states when a version is removed, and the contract test stops a breaking change reaching consumers.
- **D:** Incorrect for this question. A rolling replacement keeps capacity but exposes the whole fleet before the signal is trusted. Why the correct answer wins: The policy states when a version is removed, and the contract test stops a breaking change reaching consumers.
- **E:** Incorrect for this question. A rebuild produces a different artifact, so the test result no longer applies to production. Why the correct answer wins: The policy states when a version is removed, and the contract test stops a breaking change reaching consumers.

### Question 65 — C

Answer: Migrate the database with Database Migration Service. The service replicates continuously and cuts over in a short window with the source still running. Local study-map skill 5.3 (Data and System Migration Tooling), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 5 (managing implementation): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. The service runs scheduled loads from SaaS sources and other clouds into BigQuery. Why the correct answer wins: The service replicates continuously and cuts over in a short window with the source still running.
- **B:** Incorrect for this question. Datastream reads the source log and streams inserts, updates, and deletes with ordering preserved. Why the correct answer wins: The service replicates continuously and cuts over in a short window with the source still running.
- **C:** Correct. In this case: The service replicates continuously and cuts over in a short window with the source still running.
- **D:** Incorrect for this question. The service moves object data between buckets or clouds on a schedule. Why the correct answer wins: The service replicates continuously and cuts over in a short window with the source still running.

### Question 66 — A

Answer: Convert the VMs with Migrate to Containers. The tool rewrites a VM workload into a container image so it can run on GKE. Local study-map skill 5.3 (Data and System Migration Tooling), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 5 (managing implementation): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Correct. In this case: The tool rewrites a VM workload into a container image so it can run on GKE.
- **B:** Incorrect for this question. VMware Engine keeps the existing hypervisor and operations model while moving the hardware into Google Cloud. Why the correct answer wins: The tool rewrites a VM workload into a container image so it can run on GKE.
- **C:** Incorrect for this question. The service moves object data between buckets or clouds on a schedule. Why the correct answer wins: The tool rewrites a VM workload into a container image so it can run on GKE.
- **D:** Incorrect for this question. Migration Center inventories the servers and estimates the target size and cost. Why the correct answer wins: The tool rewrites a VM workload into a container image so it can run on GKE.

### Question 67 — D

Answer: Automate the step with the gcloud CLI. The CLI exposes the API as commands that can be scripted and captured in a log. The CLI exposes every API as a command that can be scripted and logged. Local study-map skill 5.4 (Programmatic Access and Emulators), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 5 (managing implementation): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. Cloud Shell provides an authenticated terminal and editor with no local installation. Why the correct answer wins: The CLI exposes the API as commands that can be scripted and captured in a log.
- **B:** Incorrect for this question. Cloud Code gives the editor run, debug, and deploy targets for the cluster without leaving it. Why the correct answer wins: The CLI exposes the API as commands that can be scripted and captured in a log.
- **C:** Incorrect for this question. The bq tool runs jobs and manages datasets from a terminal or a script. Why the correct answer wins: The CLI exposes the API as commands that can be scripted and captured in a log.
- **D:** Correct. The CLI exposes every API as a command that can be scripted and logged. In this case: The CLI exposes the API as commands that can be scripted and captured in a log.

### Question 68 — D

Answer: Run the emulator in the pipeline. The emulator provides a local endpoint for tests without a billable cloud resource. Local study-map skill 5.4 (Programmatic Access and Emulators), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 5 (managing implementation): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. Cloud Build executes the pipeline steps in a managed, isolated worker with recorded provenance. Why the correct answer wins: The emulator provides a local endpoint for tests without a billable cloud resource.
- **B:** Incorrect for this question. The CLI exposes every API as a command that can be scripted and logged. Why the correct answer wins: The emulator provides a local endpoint for tests without a billable cloud resource.
- **C:** Incorrect for this question. Terraform holds desired state in code, plans the diff, and applies it through a provider. Why the correct answer wins: The emulator provides a local endpoint for tests without a billable cloud resource.
- **D:** Correct. In this case: The emulator provides a local endpoint for tests without a billable cloud resource.

### Question 69 — A

Answer: Use the Google API client library with retries. The client library applies the recommended retry and backoff behaviour for the API. Local study-map skill 5.5 (Client Libraries and API Practices), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 5 (managing implementation): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Correct. In this case: The client library applies the recommended retry and backoff behaviour for the API.
- **B:** Incorrect for this question. Impersonation issues a short-lived token so the test runs as the real workload identity. Why the correct answer wins: The client library applies the recommended retry and backoff behaviour for the API.
- **C:** Incorrect for this question. An API key identifies a project and does not authorise a user, so it cannot express least privilege. Why the correct answer wins: The client library applies the recommended retry and backoff behaviour for the API.
- **D:** Incorrect for this question. The CLI exposes every API as a command that can be scripted and logged. Why the correct answer wins: The client library applies the recommended retry and backoff behaviour for the API.

### Question 70 — B

Answer: Impersonate a service account for a curl test. Impersonation issues a short-lived token so the test runs as the real workload identity. Local study-map skill 5.5 (Client Libraries and API Practices), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 5 (managing implementation): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. An API key identifies a project and does not authorise a user, so it cannot express least privilege. Why the correct answer wins: Impersonation issues a short-lived token so the test runs as the real workload identity.
- **B:** Correct. In this case: Impersonation issues a short-lived token so the test runs as the real workload identity.
- **C:** Incorrect for this question. A key file is a long-lived credential that works until it is noticed and revoked. Why the correct answer wins: Impersonation issues a short-lived token so the test runs as the real workload identity.
- **D:** Incorrect for this question. An environment variable is visible to anything that can read the instance metadata or the process list. Why the correct answer wins: Impersonation issues a short-lived token so the test runs as the real workload identity.

### Question 71 — D

Answer: Inventory the estate in Migration Center → group servers into dependency-based waves → validate a pilot wave in the target landing zone → cut over wave by wave and decommission the source. Inventory precedes grouping, a pilot proves the landing zone, and decommissioning follows a completed cutover. Local study-map skill 5.3 (Data and System Migration Tooling), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 5 (managing implementation): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. Waves cannot be grouped before the inventory, and decommissioning before validation destroys the rollback path. Why the correct answer wins: Inventory precedes grouping, a pilot proves the landing zone, and decommissioning follows a completed cutover.
- **B:** Incorrect for this question. Decommissioning first removes the evidence and the rollback option for every later step. Why the correct answer wins: Inventory precedes grouping, a pilot proves the landing zone, and decommissioning follows a completed cutover.
- **C:** Incorrect for this question. A pilot cannot be chosen before the inventory and the wave grouping. Why the correct answer wins: Inventory precedes grouping, a pilot proves the landing zone, and decommissioning follows a completed cutover.
- **D:** Correct. In this case: Inventory precedes grouping, a pilot proves the landing zone, and decommissioning follows a completed cutover.

### Question 72 — D

Answer: Define dashboards and metrics in Cloud Monitoring. Monitoring collects the platform and application metrics that the first alert will use. Local study-map skill 6.1 (Observability Design), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 6 (solution and operations excellence): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. An SLO ties the alert to the promise the users care about rather than to a raw resource threshold. Why the correct answer wins: Monitoring collects the platform and application metrics that the first alert will use.
- **B:** Incorrect for this question. Logging holds the event text and structured fields that explain what happened at a moment. Why the correct answer wins: Monitoring collects the platform and application metrics that the first alert will use.
- **C:** Incorrect for this question. The dashboard gives the team one view of the same signals during an incident. Why the correct answer wins: Monitoring collects the platform and application metrics that the first alert will use.
- **D:** Correct. In this case: Monitoring collects the platform and application metrics that the first alert will use.

### Question 73 — C

Answer: Group the exceptions in Error Reporting. Error Reporting clusters recurring stack traces so a new failure is not lost in the log volume. Local study-map skill 6.1 (Observability Design), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 6 (solution and operations excellence): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. The check measures availability from outside, which no internal metric can prove. Why the correct answer wins: Error Reporting clusters recurring stack traces so a new failure is not lost in the log volume.
- **B:** Incorrect for this question. Profiler samples the running code and attributes CPU and heap to the functions responsible. Why the correct answer wins: Error Reporting clusters recurring stack traces so a new failure is not lost in the log volume.
- **C:** Correct. In this case: Error Reporting clusters recurring stack traces so a new failure is not lost in the log volume.
- **D:** Incorrect for this question. Trace shows how one request spent its time across services and calls. Why the correct answer wins: Error Reporting clusters recurring stack traces so a new failure is not lost in the log volume.

### Question 74 — B

Answer: Define an SLO with an error budget. An SLO ties the alert to the user promise rather than to a raw resource threshold. Local study-map skill 6.2 (Alerting and Service Level Objectives), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 6 (solution and operations excellence): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. The policy fires when the series crosses the condition for the stated duration. Why the correct answer wins: An SLO ties the alert to the user promise rather than to a raw resource threshold.
- **B:** Correct. In this case: An SLO ties the alert to the user promise rather than to a raw resource threshold.
- **C:** Incorrect for this question. The check measures availability from outside, which no internal metric can prove. Why the correct answer wins: An SLO ties the alert to the user promise rather than to a raw resource threshold.
- **D:** Incorrect for this question. The dashboard gives the team one view of the same signals during an incident. Why the correct answer wins: An SLO ties the alert to the user promise rather than to a raw resource threshold.

### Question 75 — A, D

Answers: Create an alerting policy on the metric; Create a log-based metric. The metric turns the log pattern into a series, and the policy fires when it crosses the condition. The policy fires when the series crosses the condition for the stated duration. The metric turns a log pattern into a series that can be alerted on and charted. Local study-map skill 6.2 (Alerting and Service Level Objectives), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 6 (solution and operations excellence): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Correct. The policy fires when the series crosses the condition for the stated duration. In this case: The metric turns the log pattern into a series, and the policy fires when it crosses the condition.
- **B:** Incorrect for this question. An SLO ties the alert to the promise the users care about rather than to a raw resource threshold. Why the correct answer wins: The metric turns the log pattern into a series, and the policy fires when it crosses the condition.
- **C:** Incorrect for this question. Recommender reports idle and over-provisioned resources with the estimated saving. Why the correct answer wins: The metric turns the log pattern into a series, and the policy fires when it crosses the condition.
- **D:** Correct. The metric turns a log pattern into a series that can be alerted on and charted. In this case: The metric turns the log pattern into a series, and the policy fires when it crosses the condition.
- **E:** Incorrect for this question. The dashboard gives the team one view of the same signals during an incident. Why the correct answer wins: The metric turns the log pattern into a series, and the policy fires when it crosses the condition.

### Question 76 — C

Answer: Define an on-call rotation with an escalation path. A named rotation turns an alert into a person who is already accountable for it. Local study-map skill 6.3 (Release Management and Support), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 6 (solution and operations excellence): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. The support tier sets the response time and the escalation path the business expects. Why the correct answer wins: A named rotation turns an alert into a person who is already accountable for it.
- **B:** Incorrect for this question. The runbook records the diagnostic steps so the response does not depend on who is awake. Why the correct answer wins: A named rotation turns an alert into a person who is already accountable for it.
- **C:** Correct. In this case: A named rotation turns an alert into a person who is already accountable for it.
- **D:** Incorrect for this question. The contract converts an internal target into an obligation with a consequence. Why the correct answer wins: A named rotation turns an alert into a person who is already accountable for it.

### Question 77 — C

Answer: Match the support plan to the recovery commitment. The support tier sets the response time and the escalation path the business expects. Local study-map skill 6.3 (Release Management and Support), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 6 (solution and operations excellence): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. The contract converts an internal target into an obligation with a consequence. Why the correct answer wins: The support tier sets the response time and the escalation path the business expects.
- **B:** Incorrect for this question. The runbook records the diagnostic steps so the response does not depend on who is awake. Why the correct answer wins: The support tier sets the response time and the escalation path the business expects.
- **C:** Correct. In this case: The support tier sets the response time and the escalation path the business expects.
- **D:** Incorrect for this question. A named rotation turns an alert into a person who is already accountable for it. Why the correct answer wins: The support tier sets the response time and the escalation path the business expects.

### Question 78 — A

Answer: Run a load test at the expected peak. The load test measures the system at the concurrency the business expects, before launch. Local study-map skill 6.4 (Reliability Testing), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 6 (solution and operations excellence): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Correct. In this case: The load test measures the system at the concurrency the business expects, before launch.
- **B:** Incorrect for this question. An independent test attempts the attack the design claims to prevent. Why the correct answer wins: The load test measures the system at the concurrency the business expects, before launch.
- **C:** Incorrect for this question. The pyramid puts volume where it is cheap and keeps end-to-end tests for the critical paths. Why the correct answer wins: The load test measures the system at the concurrency the business expects, before launch.
- **D:** Incorrect for this question. The experiment proves the failover path works while the impact is controlled. Why the correct answer wins: The load test measures the system at the concurrency the business expects, before launch.

### Question 79 — D

Answer: Write a blameless postmortem with actions. The postmortem records cause and follow-up work, which is how the same failure is prevented. Local study-map skill 6.5 (Operational Excellence and Quality Control), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 6 (solution and operations excellence): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. The dashboard gives the team one view of the same signals during an incident. Why the correct answer wins: The postmortem records cause and follow-up work, which is how the same failure is prevented.
- **B:** Incorrect for this question. The support tier sets the response time and the escalation path the business expects. Why the correct answer wins: The postmortem records cause and follow-up work, which is how the same failure is prevented.
- **C:** Incorrect for this question. The runbook records the diagnostic steps so the response does not depend on who is awake. Why the correct answer wins: The postmortem records cause and follow-up work, which is how the same failure is prevented.
- **D:** Correct. In this case: The postmortem records cause and follow-up work, which is how the same failure is prevented.

### Question 80 — A

Answer: Build an immutable image and record its digest → deploy the new revision without traffic → shift a small traffic percentage and watch error and latency signals → promote to full traffic or roll back to the pinned digest. The artifact is fixed before traffic moves, and the decision to promote follows observed signals. Local study-map skill 6.5 (Operational Excellence and Quality Control), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 6 (solution and operations excellence): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Correct. In this case: The artifact is fixed before traffic moves, and the decision to promote follows observed signals.
- **B:** Incorrect for this question. Nothing can be watched before the revision exists, and the image precedes the deployment. Why the correct answer wins: The artifact is fixed before traffic moves, and the decision to promote follows observed signals.
- **C:** Incorrect for this question. Promoting before the canary step skips the signal that justifies promotion. Why the correct answer wins: The artifact is fixed before traffic moves, and the decision to promote follows observed signals.
- **D:** Incorrect for this question. Full traffic before any canary step turns the first failure into an outage. Why the correct answer wins: The artifact is fixed before traffic moves, and the decision to promote follows observed signals.

### Question 81 — D

Answer: Store the objects in Archive storage class. Archive is the cheapest class to hold for data that is rarely retrieved but must be kept. Archive is cheapest to hold and slowest and most expensive to retrieve. Local study-map skill 1.5 (Storage and Data Store Selection), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 1 (designing and planning): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. Standard is for data read frequently and has no retrieval fee. Why the correct answer wins: Archive is the cheapest class to hold for data that is rarely retrieved but must be kept.
- **B:** Incorrect for this question. Nearline suits data read about once a month and charges for early deletion. Why the correct answer wins: Archive is the cheapest class to hold for data that is rarely retrieved but must be kept.
- **C:** Incorrect for this question. Filestore provides a managed NFS export that many clients can mount at once. Why the correct answer wins: Archive is the cheapest class to hold for data that is rarely retrieved but must be kept.
- **D:** Correct. Archive is cheapest to hold and slowest and most expensive to retrieve. In this case: Archive is the cheapest class to hold for data that is rarely retrieved but must be kept.

### Question 82 — A

Answer: Assess the estate in Migration Center. Migration Center inventories the estate and estimates target size and cost before a plan is funded. Migration Center inventories the servers and estimates the target size and cost. Local study-map skill 1.9 (Migration Planning and Future Improvement), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 1 (designing and planning): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Correct. Migration Center inventories the servers and estimates the target size and cost. In this case: Migration Center inventories the estate and estimates target size and cost before a plan is funded.
- **B:** Incorrect for this question. The service moves a database with continuous replication and a short cutover window. Why the correct answer wins: Migration Center inventories the estate and estimates target size and cost before a plan is funded.
- **C:** Incorrect for this question. The tool rewrites a VM workload into a container image so it can run on GKE. Why the correct answer wins: Migration Center inventories the estate and estimates target size and cost before a plan is funded.
- **D:** Incorrect for this question. The service moves object data between buckets or clouds on a schedule. Why the correct answer wins: Migration Center inventories the estate and estimates target size and cost before a plan is funded.

### Question 83 — D

Answer: Enable Data Access audit logs. Data Access logging is off by default and must be enabled before reads and writes are recorded. Local study-map skill 3.8 (Compliance, Residency, and Audit Logging), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 3 (security and compliance): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. The metric turns a log pattern into a series that can be alerted on and charted. Why the correct answer wins: Data Access logging is off by default and must be enabled before reads and writes are recorded.
- **B:** Incorrect for this question. Access Transparency records when Google staff access your content, which is evidence of oversight, not of user activity. Why the correct answer wins: Data Access logging is off by default and must be enabled before reads and writes are recorded.
- **C:** Incorrect for this question. Admin Activity records configuration changes and cannot be disabled. Why the correct answer wins: Data Access logging is off by default and must be enabled before reads and writes are recorded.
- **D:** Correct. In this case: Data Access logging is off by default and must be enabled before reads and writes are recorded.

### Question 84 — A

Answer: Act on the Recommender suggestions. Recommender reports idle and over-provisioned resources with the estimated saving for each. Local study-map skill 4.5 (Cost Optimization), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 4 (analyzing and optimizing): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Correct. In this case: Recommender reports idle and over-provisioned resources with the estimated saving for each.
- **B:** Incorrect for this question. Labels attribute spend in billing export; they do not grant or restrict access. Why the correct answer wins: Recommender reports idle and over-provisioned resources with the estimated saving for each.
- **C:** Incorrect for this question. The export attributes cost to the team and service that caused it. Why the correct answer wins: Recommender reports idle and over-provisioned resources with the estimated saving for each.
- **D:** Incorrect for this question. A budget alerts on spend but does not stop it. Why the correct answer wins: Recommender reports idle and over-provisioned resources with the estimated saving for each.

### Question 85 — B

Answer: Define dashboards and metrics in Cloud Monitoring. Monitoring collects the platform and application metrics that the first alert will use. Local study-map skill 6.1 (Observability Design), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 6 (solution and operations excellence): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. The dashboard gives the team one view of the same signals during an incident. Why the correct answer wins: Monitoring collects the platform and application metrics that the first alert will use.
- **B:** Correct. In this case: Monitoring collects the platform and application metrics that the first alert will use.
- **C:** Incorrect for this question. Trace shows how one request spent its time across services and calls. Why the correct answer wins: Monitoring collects the platform and application metrics that the first alert will use.
- **D:** Incorrect for this question. Recommender reports idle and over-provisioned resources with the estimated saving. Why the correct answer wins: Monitoring collects the platform and application metrics that the first alert will use.

### Question 86 — C

Answer: Add row-level access policies to the table. Row-level policies filter which rows each principal sees inside BigQuery itself. Local study-map skill 1.7 (Data Processing and Analytics Selection), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 1 (designing and planning): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. Looker Studio renders the visualisation but inherits whatever query and permissions sit beneath it. Why the correct answer wins: Row-level policies filter which rows each principal sees inside BigQuery itself.
- **B:** Incorrect for this question. The policy replaces the column value for unauthorised principals while leaving the column queryable. Why the correct answer wins: Row-level policies filter which rows each principal sees inside BigQuery itself.
- **C:** Correct. In this case: Row-level policies filter which rows each principal sees inside BigQuery itself.
- **D:** Incorrect for this question. The view runs with its own identity, so a consumer reads columns without table access. Why the correct answer wins: Row-level policies filter which rows each principal sees inside BigQuery itself.

### Question 87 — B

Answer: Attach a Serverless VPC Access connector. The connector gives serverless workloads a route to internal addresses in the VPC. Local study-map skill 2.5 (Serverless Configuration), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 2 (managing and provisioning): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. A PSC endpoint gives a private IP in the consumer VPC without peering or exposing the service publicly. Why the correct answer wins: The connector gives serverless workloads a route to internal addresses in the VPC.
- **B:** Correct. In this case: The connector gives serverless workloads a route to internal addresses in the VPC.
- **C:** Incorrect for this question. Private Google Access reaches Google APIs from an internal address without a proxy or a NAT gateway. Why the correct answer wins: The connector gives serverless workloads a route to internal addresses in the VPC.
- **D:** Incorrect for this question. Cloud NAT lets private instances reach the internet without an external address. Why the correct answer wins: The connector gives serverless workloads a route to internal addresses in the VPC.

### Question 88 — C

Answer: Run a load test at the expected peak. The load test measures the system at the concurrency the business expects, before the deadline is promised. Local study-map skill 4.3 (Testing and Validation), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 4 (analyzing and optimizing): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. An independent test attempts the attack the design claims to prevent. Why the correct answer wins: The load test measures the system at the concurrency the business expects, before the deadline is promised.
- **B:** Incorrect for this question. The pyramid puts volume where it is cheap and keeps end-to-end tests for the critical paths. Why the correct answer wins: The load test measures the system at the concurrency the business expects, before the deadline is promised.
- **C:** Correct. In this case: The load test measures the system at the concurrency the business expects, before the deadline is promised.
- **D:** Incorrect for this question. The experiment proves the failover path works while the impact is controlled. Why the correct answer wins: The load test measures the system at the concurrency the business expects, before the deadline is promised.

### Question 89 — C

Answer: Define an on-call rotation with an escalation path. A named rotation turns an alert into a person who is already accountable for it. Local study-map skill 6.3 (Release Management and Support), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 6 (solution and operations excellence): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. The runbook records the diagnostic steps so the response does not depend on who is awake. Why the correct answer wins: A named rotation turns an alert into a person who is already accountable for it.
- **B:** Incorrect for this question. The contract converts an internal target into an obligation with a consequence. Why the correct answer wins: A named rotation turns an alert into a person who is already accountable for it.
- **C:** Correct. In this case: A named rotation turns an alert into a person who is already accountable for it.
- **D:** Incorrect for this question. The support tier sets the response time and the escalation path the business expects. Why the correct answer wins: A named rotation turns an alert into a person who is already accountable for it.

### Question 90 — A

Answer: Keep the data in the region the regulator requires. Residency fixes where storage and processing may happen, which then constrains every service choice. Local study-map skill 1.2 (Non-Functional Requirements and Trade-offs), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 1 (designing and planning): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Correct. In this case: Residency fixes where storage and processing may happen, which then constrains every service choice.
- **B:** Incorrect for this question. The exit plan keeps the migration reversible and constrains how proprietary the design may become. Why the correct answer wins: Residency fixes where storage and processing may happen, which then constrains every service choice.
- **C:** Incorrect for this question. A measured baseline and a named owner make the outcome testable after the migration. Why the correct answer wins: Residency fixes where storage and processing may happen, which then constrains every service choice.
- **D:** Incorrect for this question. The model compares run cost, people cost, and exit cost rather than the monthly bill alone. Why the correct answer wins: Residency fixes where storage and processing may happen, which then constrains every service choice.

### Question 91 — C

Answer: Encrypt with a customer-managed key in Cloud KMS. A customer-managed key lets the bank rotate or disable the key and stop decryption at once. CMEK lets you control the key lifecycle, rotation, and the ability to revoke access to the data. Local study-map skill 3.3 (Encryption, CMEK, and Secrets), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 3 (security and compliance): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. Cloud HSM keeps the key material in a hardware module that meets FIPS 140-2 level 3. Why the correct answer wins: A customer-managed key lets the bank rotate or disable the key and stop decryption at once.
- **B:** Incorrect for this question. Secret Manager versions the secret, controls access by IAM, and can rotate it. Why the correct answer wins: A customer-managed key lets the bank rotate or disable the key and stop decryption at once.
- **C:** Correct. CMEK lets you control the key lifecycle, rotation, and the ability to revoke access to the data. In this case: A customer-managed key lets the bank rotate or disable the key and stop decryption at once.
- **D:** Incorrect for this question. CSEK is held by the caller and never stored by Google, so losing it loses the object. Why the correct answer wins: A customer-managed key lets the bank rotate or disable the key and stop decryption at once.

### Question 92 — D

Answer: Put the projects inside a VPC Service Controls perimeter. A service perimeter blocks data movement out of the covered services even for a principal with the role. Local study-map skill 3.4 (VPC Service Controls and Network Security), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 3 (security and compliance): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. Labels attribute spend in billing export; they do not grant or restrict access. Why the correct answer wins: A service perimeter blocks data movement out of the covered services even for a principal with the role.
- **B:** Incorrect for this question. A deny policy overrides every allow beneath it, which is how an exception is made impossible. Why the correct answer wins: A service perimeter blocks data movement out of the covered services even for a principal with the role.
- **C:** Incorrect for this question. A policy above the project applies to every current and future network beneath it. Why the correct answer wins: A service perimeter blocks data movement out of the covered services even for a principal with the role.
- **D:** Correct. In this case: A service perimeter blocks data movement out of the covered services even for a principal with the role.

### Question 93 — C

Answer: Apply a bucket retention policy with a locked period. A locked retention policy prevents deletion or a shorter period, which is the evidence an auditor tests. Local study-map skill 2.2 (Storage Configuration and Lifecycle), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 2 (managing and provisioning): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. Autoclass moves each object between classes as its access pattern changes, with no lifecycle rules to maintain. Why the correct answer wins: A locked retention policy prevents deletion or a shorter period, which is the evidence an auditor tests.
- **B:** Incorrect for this question. Versioning keeps a noncurrent copy when an object is overwritten or deleted. Why the correct answer wins: A locked retention policy prevents deletion or a shorter period, which is the evidence an auditor tests.
- **C:** Correct. In this case: A locked retention policy prevents deletion or a shorter period, which is the evidence an auditor tests.
- **D:** Incorrect for this question. A lifecycle rule acts on object age or class, so retention stops depending on a person. Why the correct answer wins: A locked retention policy prevents deletion or a shorter period, which is the evidence an auditor tests.

### Question 94 — C

Answer: Write a blameless postmortem with actions. The postmortem records cause and follow-up work, which is how the same failure is prevented. Local study-map skill 6.5 (Operational Excellence and Quality Control), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 6 (solution and operations excellence): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. The runbook records the diagnostic steps so the response does not depend on who is awake. Why the correct answer wins: The postmortem records cause and follow-up work, which is how the same failure is prevented.
- **B:** Incorrect for this question. The support tier sets the response time and the escalation path the business expects. Why the correct answer wins: The postmortem records cause and follow-up work, which is how the same failure is prevented.
- **C:** Correct. In this case: The postmortem records cause and follow-up work, which is how the same failure is prevented.
- **D:** Incorrect for this question. The dashboard gives the team one view of the same signals during an incident. Why the correct answer wins: The postmortem records cause and follow-up work, which is how the same failure is prevented.

### Question 95 — B

Answer: Require a reviewed pull request and a passing plan. The gate makes a second person check the change and its plan before it can apply. Local study-map skill 4.1 (SDLC and CI/CD Design), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 4 (analyzing and optimizing): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. Short branches reduce merge conflict and keep the mainline deployable. Why the correct answer wins: The gate makes a second person check the change and its plan before it can apply.
- **B:** Correct. In this case: The gate makes a second person check the change and its plan before it can apply.
- **C:** Incorrect for this question. A rolling replacement keeps capacity but exposes the whole fleet before the signal is trusted. Why the correct answer wins: The gate makes a second person check the change and its plan before it can apply.
- **D:** Incorrect for this question. A rebuild produces a different artifact, so the test result no longer applies to production. Why the correct answer wins: The gate makes a second person check the change and its plan before it can apply.

### Question 96 — A

Answer: Use Chrome Enterprise Premium for the workforce. Context-aware access evaluates device and identity signals for every application, not just the network. Local study-map skill 3.5 (Secure Remote Access and Zero Trust), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 3 (security and compliance): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Correct. In this case: Context-aware access evaluates device and identity signals for every application, not just the network.
- **B:** Incorrect for this question. A bastion is still an internet-facing host that must be patched and watched. Why the correct answer wins: Context-aware access evaluates device and identity signals for every application, not just the network.
- **C:** Incorrect for this question. An API key identifies a project and does not authorise a user, so it cannot express least privilege. Why the correct answer wins: Context-aware access evaluates device and identity signals for every application, not just the network.
- **D:** Incorrect for this question. Cloud NAT lets private instances reach the internet without an external address. Why the correct answer wins: Context-aware access evaluates device and identity signals for every application, not just the network.

### Question 97 — C

Answer: Enforce the control with an organization policy constraint. An organization policy blocks the action across every project regardless of who holds the role. Local study-map skill 3.2 (Resource Hierarchy and Organization Policy), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 3 (security and compliance): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. A project is the boundary for quota, billing, and most IAM inheritance. Why the correct answer wins: An organization policy blocks the action across every project regardless of who holds the role.
- **B:** Incorrect for this question. Labels attribute spend in billing export; they do not grant or restrict access. Why the correct answer wins: An organization policy blocks the action across every project regardless of who holds the role.
- **C:** Correct. In this case: An organization policy blocks the action across every project regardless of who holds the role.
- **D:** Incorrect for this question. A folder binding inherits to every project beneath it, so new projects start with the right access. Why the correct answer wins: An organization policy blocks the action across every project regardless of who holds the role.

### Question 98 — C

Answer: Enable Workload Identity Federation for GKE. Workload Identity binds the pod identity to IAM, so pods hold no keys. The feature binds a Kubernetes service account to an IAM service account, so pods hold no keys. Local study-map skill 2.4 (Container Orchestration), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 2 (managing and provisioning): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. A key file is a long-lived credential that works until it is noticed and revoked. Why the correct answer wins: Workload Identity binds the pod identity to IAM, so pods hold no keys.
- **B:** Incorrect for this question. An environment variable is visible to anything that can read the instance metadata or the process list. Why the correct answer wins: Workload Identity binds the pod identity to IAM, so pods hold no keys.
- **C:** Correct. The feature binds a Kubernetes service account to an IAM service account, so pods hold no keys. In this case: Workload Identity binds the pod identity to IAM, so pods hold no keys.
- **D:** Incorrect for this question. Federation exchanges an external token for short-lived Google Cloud credentials, so no key leaves the provider. Why the correct answer wins: Workload Identity binds the pod identity to IAM, so pods hold no keys.

### Question 99 — B

Answer: Define an SLO with an error budget. An SLO ties the alert to the user promise rather than to a raw resource threshold. Local study-map skill 6.2 (Alerting and Service Level Objectives), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 6 (solution and operations excellence): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. The dashboard gives the team one view of the same signals during an incident. Why the correct answer wins: An SLO ties the alert to the user promise rather than to a raw resource threshold.
- **B:** Correct. In this case: An SLO ties the alert to the user promise rather than to a raw resource threshold.
- **C:** Incorrect for this question. The policy fires when the series crosses the condition for the stated duration. Why the correct answer wins: An SLO ties the alert to the user promise rather than to a raw resource threshold.
- **D:** Incorrect for this question. The check measures availability from outside, which no internal metric can prove. Why the correct answer wins: An SLO ties the alert to the user promise rather than to a raw resource threshold.

### Question 100 — C

Answer: Use GKE Autopilot. Autopilot manages nodes, scaling, and patching, so the team owns only its workloads. Local study-map skill 1.6 (Compute Platform Selection), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 1 (designing and planning): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. Standard exposes node configuration and patching, which the team must then run itself. Why the correct answer wins: Autopilot manages nodes, scaling, and patching, so the team owns only its workloads.
- **B:** Incorrect for this question. Cloud Run runs a stateless container per request and scales to zero when idle. Why the correct answer wins: Autopilot manages nodes, scaling, and patching, so the team owns only its workloads.
- **C:** Correct. In this case: Autopilot manages nodes, scaling, and patching, so the team owns only its workloads.
- **D:** Incorrect for this question. Batch schedules containerised jobs onto managed or existing capacity and retires it when done. Why the correct answer wins: Autopilot manages nodes, scaling, and patching, so the team owns only its workloads.
