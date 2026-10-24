# Google Cloud Professional Cloud Architect — Full-Length Mock Exam 6

Professional Cloud Architect · 100 questions · expanded practice bank · passing score not published

Blueprint-weighted mock exam. Item mix: 84 multiple-choice (selection count stated where needed), 16 multi-select, and 4 case studies of 5 questions. 8 of the multiple-choice items ask you to choose the correct candidate sequence. The live exam publishes 50-60 questions and two case studies worth 20-30 per cent of the score; this set is larger on purpose and cannot reproduce the split-screen case-study panel, drag-and-drop ordering, or lab tasks. See the README for the exact fidelity boundary.

Original educational content, not actual, recalled, or copied Google exam items.

## Questions

### 1. A reliability programme is proposed and nobody can say whether it helped. What should be recorded now?

Domain: Designing and planning a cloud solution architecture

- A. Build a three-year total cost of ownership model
- B. Export billing to BigQuery and review it per label
- C. Publish a shared dashboard
- D. Define the baseline and target as a KPI with an owner

### 2. Two operating models differ in people cost as well as run cost. What should be produced to compare them?

Domain: Designing and planning a cloud solution architecture

- A. Export billing to BigQuery and review it per label
- B. Set a budget with alert thresholds
- C. Build a three-year total cost of ownership model
- D. Buy committed use discounts for the steady baseline

### 3. An acquisition may end the platform agreement in three years. What must the design include?

Domain: Designing and planning a cloud solution architecture

- A. Tag the resources with labels for cost reporting
- B. Build a three-year total cost of ownership model
- C. Document the exit plan and data portability
- D. Set a budget with alert thresholds

### 4. Two business units disagree about how much data loss is tolerable. Which two artefacts settle it? Select two.

Domain: Designing and planning a cloud solution architecture

- A. Set the RPO and RTO with the business owner
- B. Act on the Recommender suggestions
- C. Put the recovery commitment in the contract
- D. Publish a shared dashboard
- E. Tag the resources with labels for cost reporting

### 5. A regional failure must not require an operator to promote a replica. What should be enabled?

Domain: Designing and planning a cloud solution architecture

- A. Add a read replica and route reads to it
- B. Use Bigtable
- C. Enable Cloud SQL high availability with a standby
- D. Use Memorystore

### 6. Customer-facing services must keep serving through a regional loss with no failover decision. Which two pieces are required? Select two.

Domain: Designing and planning a cloud solution architecture

- A. Run active-active across two regions
- B. Enable Cloud CDN on the backend
- C. Run a pilot-light standby
- D. Replicate the data to the second region
- E. Use backup and restore

### 7. Three business units run separate networks and must reach one shared services hub. What should be built?

Domain: Designing and planning a cloud solution architecture

- A. Build a Network Connectivity Center hub
- B. Create a DNS peering zone
- C. Deploy Cloud NAT for outbound traffic
- D. Peer the two VPC networks

### 8. A partner must reach an internal service privately across two organisations. Which two designs allow that? Select two.

Domain: Designing and planning a cloud solution architecture

- A. Enable Cloud CDN on the backend
- B. Peer the two VPC networks
- C. Publish the service through Private Service Connect
- D. Deploy Cloud NAT for outbound traffic
- E. Issue a short-lived signed URL

### 9. Media assets are hot at publication and cold weeks later, unpredictably. What should be enabled?

Domain: Designing and planning a cloud solution architecture

- A. Enable Autoclass on the bucket
- B. Add a lifecycle rule that transitions and then deletes
- C. Store the objects in Nearline storage class
- D. Store the objects in Standard storage class

### 10. The asset library must survive a region loss and must not lose an overwritten file. Which two settings apply? Select two.

Domain: Designing and planning a cloud solution architecture

- A. Mount a Filestore instance for the shared file path
- B. Store the objects in Archive storage class
- C. Use a dual-region bucket
- D. Enable object versioning
- E. Use local SSD for the scratch space

### 11. A product team wants Kubernetes without owning node patching. What should be chosen?

Domain: Designing and planning a cloud solution architecture

- A. Deploy the service on Cloud Run
- B. Submit the work as a Batch job
- C. Use GKE Standard with a node pool per workload shape
- D. Use GKE Autopilot

### 12. A webhook endpoint is idle most of the night and must return to zero. What should be used?

Domain: Designing and planning a cloud solution architecture

- A. Use GKE Standard with a node pool per workload shape
- B. Run the legacy stack on Google Cloud VMware Engine
- C. Deploy the service on Cloud Run
- D. Use a managed instance group with autoscaling

### 13. A settlement rerun needs 3,000 cores for an hour and nothing afterwards. What should be used?

Domain: Designing and planning a cloud solution architecture

- A. Deploy the service on Cloud Run
- B. Submit the work as a Batch job
- C. Use a managed instance group with autoscaling
- D. Use GKE Standard with a node pool per workload shape

### 14. Analysts must scan petabytes of event data with no cluster to size. What should be used?

Domain: Designing and planning a cloud solution architecture

- A. Use Cloud SQL
- B. Use Bigtable
- C. Load the data into BigQuery
- D. Use Firestore

### 15. Dashboards must answer instantly, and query volume is steady all day. Which two choices apply? Select two.

Domain: Designing and planning a cloud solution architecture

- A. Leave the project on on-demand pricing
- B. Buy BigQuery slot commitments with autoscaling
- C. Reserve BigQuery BI Engine capacity
- D. Stream rows with the legacy insertAll call
- E. Build the dashboard in Looker Studio

### 16. Model calls must be regionally processed and audited for a regulated unit. What should be used?

Domain: Designing and planning a cloud solution architecture

- A. Call Gemini through Agent Platform
- B. Index the corpus with Vertex AI Search
- C. Use Gemini Enterprise for the knowledge assistant
- D. Use the Vision API for the images

### 17. Support agents need cited answers from private runbooks. What should be used?

Domain: Designing and planning a cloud solution architecture

- A. Index the corpus with Vertex AI Search
- B. Use the Vision API for the images
- C. Use the Translation API
- D. Use Document AI with a specialised processor

### 18. A doubling estate must be sized before the acquisition closes. What should be used?

Domain: Designing and planning a cloud solution architecture

- A. Copy the files with Storage Transfer Service
- B. Use Database Migration Service
- C. Assess the estate in Migration Center
- D. Convert the VMs with Migrate to Containers

### 19. Two hundred terabytes must leave a site whose uplink would take a year. What should be used?

Domain: Designing and planning a cloud solution architecture

- A. Use Storage Transfer Service for the recurring copy
- B. Use a Transfer Appliance for the one-off bulk move
- C. Use gcloud storage commands
- D. Copy the files with Storage Transfer Service

### 20. The board must see a rehearsed recovery, not a designed one. Which sequence is correct?

Domain: Designing and planning a cloud solution architecture

- A. Choose the DR pattern → fail over in a game day → set the RTO and RPO targets → build the standby environment
- B. Build and replicate the standby environment → choose the DR pattern → set the RTO and RPO targets → fail over in a game day
- C. Set the RTO and RPO targets → choose the DR pattern that meets them → build and replicate the standby environment → fail over in a game day and record the result
- D. Fail over in a game day → set the RTO and RPO targets → choose the DR pattern → build the standby environment

### 21. A site has one fibre provider and needs a private path that survives one tunnel. What should be used?

Domain: Managing and provisioning a solution infrastructure

- A. Use HA VPN with two tunnels
- B. Order a Dedicated Interconnect
- C. Deploy Cloud NAT for outbound traffic
- D. Enable Cloud CDN on the backend

### 22. Private instances must reach Google APIs without a proxy and still fetch internet updates. Which two settings apply? Select two.

Domain: Managing and provisioning a solution infrastructure

- A. Put Identity-Aware Proxy in front of the application
- B. Deploy Cloud NAT for outbound traffic
- C. Enable Private Google Access on the subnet
- D. Enable Cloud CDN on the backend
- E. Attach a Cloud Armor security policy

### 23. Regulated records must be undeletable for the period the regulator names. What should be applied?

Domain: Managing and provisioning a solution infrastructure

- A. Enable Autoclass on the bucket
- B. Enable object versioning
- C. Add a lifecycle rule that transitions and then deletes
- D. Apply a bucket retention policy with a locked period

### 24. A fact table is filtered by date and by business unit, and every query scans too much. Which two choices apply? Select two.

Domain: Managing and provisioning a solution infrastructure

- A. Partition the table on the date column
- B. Cluster the table on the filter columns
- C. Leave the project on on-demand pricing
- D. Build the dashboard in Looker Studio
- E. Create a materialized view for the repeated aggregate

### 25. A forecast tier runs constantly at a low level and spikes at month end. Which two purchasing choices apply? Select two.

Domain: Managing and provisioning a solution infrastructure

- A. Share the cost view with the engineering teams
- B. Move the steady services to E2 machine types
- C. Run the batch tier on Spot VMs
- D. Use local SSD for the scratch space
- E. Buy committed use discounts for the steady baseline

### 26. A fleet of 600 VMs must be patched on a published schedule. What should be used?

Domain: Managing and provisioning a solution infrastructure

- A. Run the batch tier on Spot VMs
- B. Manage the resources with Config Connector
- C. Use VM Manager for OS patch compliance
- D. Run the build in Cloud Build

### 27. Pods must call Google APIs with no key file present. What should be enabled?

Domain: Managing and provisioning a solution infrastructure

- A. Create a service account key file for the pipeline
- B. Enable Workload Identity Federation for GKE
- C. Use Workload Identity Federation for the external pipeline
- D. Put the credential in an environment variable on the instance

### 28. The capstone cluster must keep every node internal while pods still call Google APIs. What should be configured?

Domain: Managing and provisioning a solution infrastructure

- A. Use sole-tenant nodes
- B. Create private nodes with no external IP addresses
- C. Create a zonal GKE cluster
- D. Deploy Cloud NAT for outbound traffic

### 29. The customer-facing cluster must be rebuilt with private nodes and attested images. Which sequence is correct?

Domain: Managing and provisioning a solution infrastructure

- A. Create the project and enable APIs → build a Shared VPC with private subnets → create a regional private cluster with Workload Identity Federation for GKE → deploy through Binary Authorization
- B. Build a Shared VPC → deploy through Binary Authorization → create the project → create the cluster
- C. Deploy through Binary Authorization → create the cluster → build the Shared VPC → create the project
- D. Create a regional private cluster → build a Shared VPC with private subnets → enable APIs → deploy through Binary Authorization

### 30. A user-facing endpoint must answer within 250 ms after a quiet period. What should be configured?

Domain: Managing and provisioning a solution infrastructure

- A. Set a minimum instance count on the Cloud Run service
- B. Deploy the workload on Cloud Run with a GPU
- C. Raise the request concurrency setting
- D. Deploy on App Engine flexible environment

### 31. A single small handler must react to an object being written. What should be used?

Domain: Managing and provisioning a solution infrastructure

- A. Use a managed instance group with autoscaling
- B. Use Cloud Run functions
- C. Submit the work as a Batch job
- D. Deploy the service on Cloud Run

### 32. Every environment must be rebuilt from code with a reviewable diff. What should be used?

Domain: Managing and provisioning a solution infrastructure

- A. Manage the resources with Config Connector
- B. Manage the resources with Terraform
- C. Use Deployment Manager templates
- D. Automate the step with the gcloud CLI

### 33. Demand-forecast retraining must be reproducible and record lineage per step. What should be used?

Domain: Managing and provisioning a solution infrastructure

- A. Use a Dataproc cluster
- B. Orchestrate the workflow in Agent Platform Pipelines
- C. Run batch prediction
- D. Trigger the job with Cloud Scheduler

### 34. Product photos must be labelled without training a custom model. What should be used?

Domain: Managing and provisioning a solution infrastructure

- A. Use the Vision API for the images
- B. Use the Speech-to-Text API
- C. Use Document AI with a specialised processor
- D. Use the Translation API

### 35. A meter stream must be deployed with windowing and a dead-letter path. Which sequence is correct?

Domain: Managing and provisioning a solution infrastructure

- A. Design the windowing → monitor watermark lag → create the Pub/Sub topic → deploy the job
- B. Deploy the streaming job → create the Pub/Sub topic → design the windowing → monitor watermark lag
- C. Monitor watermark lag → deploy the streaming job → create the topic → design the windowing
- D. Create the Pub/Sub topic and subscription → design the Dataflow windowing and allowed lateness → deploy the streaming job with a dead-letter path → monitor watermark lag and backfill from the raw archive

### 36. A reporting role must allow exactly five permissions on one dataset. What should be created?

Domain: Designing for security and compliance

- A. Run a bastion host with a public address
- B. Grant a predefined role at the narrowest resource
- C. Define a custom role with only the required permissions
- D. Authenticate the call with an API key

### 37. A leaked credential must affect one service rather than the platform. What should be done?

Domain: Designing for security and compliance

- A. Tag the resources with labels for cost reporting
- B. Create a service account key file for the pipeline
- C. Give each service its own service account
- D. Create a separate project per environment

### 38. Support access must be time-limited, and a suspended vendor must keep no access. Which two controls apply? Select two.

Domain: Designing for security and compliance

- A. Add an IAM condition on the binding
- B. Grant a predefined role at the narrowest resource
- C. Tag the resources with labels for cost reporting
- D. Run a bastion host with a public address
- E. Apply an IAM deny policy

### 39. No project may be created outside the approved countries. What should be enforced?

Domain: Designing for security and compliance

- A. Enforce the control with an organization policy constraint
- B. Tag the resources with labels for cost reporting
- C. Create a separate project per environment
- D. Create a folder per environment and bind roles there

### 40. A new country project must inherit access and keep its own quota and billing boundary. Which two constructs provide that? Select two.

Domain: Designing for security and compliance

- A. Grant a predefined role at the narrowest resource
- B. Add an IAM condition on the binding
- C. Tag the resources with labels for cost reporting
- D. Create a folder per environment and bind roles there
- E. Create a separate project per environment

### 41. The company must be able to revoke access to archived records by disabling a key. What should be used?

Domain: Designing for security and compliance

- A. Store the credential in Secret Manager
- B. Use Cloud HSM for the key
- C. Supply a customer-supplied encryption key
- D. Encrypt with a customer-managed key in Cloud KMS

### 42. Keys must stay in the country of the data and must change on a published schedule. Which two settings apply? Select two.

Domain: Designing for security and compliance

- A. Put the credential in an environment variable on the instance
- B. Create the key ring in the same region as the data
- C. Set an automatic rotation period on the key
- D. Supply a customer-supplied encryption key
- E. Use Cloud HSM for the key

### 43. Forecast data must not leave the approved services even for an owner. What should be applied?

Domain: Designing for security and compliance

- A. Apply an IAM deny policy
- B. Apply a hierarchical firewall policy at the organization or folder
- C. Put the projects inside a VPC Service Controls perimeter
- D. Tag the resources with labels for cost reporting

### 44. Partners must reach an internal console with no VPN and no public address. What should be used?

Domain: Designing for security and compliance

- A. Put Identity-Aware Proxy in front of the application
- B. Deploy Cloud NAT for outbound traffic
- C. Run a bastion host with a public address
- D. Enable Private Google Access on the subnet

### 45. Only images from the approved pipeline may start in production. What should be enforced?

Domain: Designing for security and compliance

- A. Enable Artifact Analysis scanning on the repository
- B. Store the images in Artifact Registry
- C. Enable network policy enforcement
- D. Require Binary Authorization attestations

### 46. The forecast assistant is a trade secret and must resist extraction attempts. What should be added?

Domain: Designing for security and compliance

- A. Require an access level in the perimeter
- B. De-identify the data with Sensitive Data Protection
- C. Turn on Security Command Center findings
- D. Screen prompts and responses with Model Armor

### 47. The company must show who read a forecast file. What should be enabled?

Domain: Designing for security and compliance

- A. Create a log-based metric
- B. Rely on Admin Activity audit logs
- C. Review Access Transparency logs
- D. Enable Data Access audit logs

### 48. Evidence must be gathered from every project into one queryable destination. What should be built?

Domain: Designing for security and compliance

- A. Publish a shared dashboard
- B. Publish a runbook per alert
- C. Create a log-based metric
- D. Route the logs with an aggregated sink

### 49. An acquisition audit needs read evidence that cannot be edited. Which sequence is correct?

Domain: Designing for security and compliance

- A. Create a locked log bucket → enable data access audit logs → query the evidence → route the logs with a sink
- B. Enable data access audit logs for the services in scope → create a locked log bucket with the required retention → route the logs with an aggregated sink → query and export the evidence for the auditor
- C. Query the evidence → create a locked log bucket → enable audit logs → route the logs
- D. Route the logs with a sink → query the evidence → enable audit logs → create a locked bucket

### 50. Twelve teams release to one platform and nobody reviews the change plan. What should the pipeline enforce?

Domain: Analyzing and optimizing technical and business processes

- A. Require a reviewed pull request and a passing plan
- B. Roll the change out instance by instance
- C. Adopt trunk-based development with short-lived branches
- D. Rebuild the artifact separately for each environment

### 51. Branch review takes a week and the mainline is rarely deployable. What should change?

Domain: Analyzing and optimizing technical and business processes

- A. Adopt trunk-based development with short-lived branches
- B. Rebuild the artifact separately for each environment
- C. Roll the change out instance by instance
- D. Put the change behind a feature flag

### 52. A cascade started at 11:52 and the team needs the exact error text. Where should it look?

Domain: Analyzing and optimizing technical and business processes

- A. Query the entries in Cloud Logging
- B. Inspect the trace waterfall in Cloud Trace
- C. Publish a shared dashboard
- D. Act on the Recommender suggestions

### 53. One slow service took the site down, and the same exception keeps recurring. Which two tools apply? Select two.

Domain: Analyzing and optimizing technical and business processes

- A. Group the exceptions in Error Reporting
- B. Inspect the trace waterfall in Cloud Trace
- C. Define an SLO with an error budget
- D. Publish a runbook per alert
- E. Publish a shared dashboard

### 54. The holiday peak must be proven before the freeze. What should be run?

Domain: Analyzing and optimizing technical and business processes

- A. Commission a penetration test
- B. Run a chaos experiment against a zone
- C. Cover the change with unit, integration, and a few end-to-end tests
- D. Run a load test at the expected peak

### 55. Booking needs a fifteen-minute recovery objective and can fund a smaller running copy. What fits?

Domain: Analyzing and optimizing technical and business processes

- A. Run a pilot-light standby
- B. Use backup and restore
- C. Run a warm standby at reduced capacity
- D. Run active-active across two regions

### 56. The platform is suspected of paying for idle peak capacity all year. What should be reviewed first?

Domain: Analyzing and optimizing technical and business processes

- A. Act on the Recommender suggestions
- B. Set a budget with alert thresholds
- C. Export billing to BigQuery and review it per label
- D. Tag the resources with labels for cost reporting

### 57. Cost must be attributed per business unit and someone must own it. Which two steps apply? Select two.

Domain: Analyzing and optimizing technical and business processes

- A. Export billing to BigQuery and review it per label
- B. Share the cost view with the engineering teams
- C. Tag the resources with labels for cost reporting
- D. Assign a cost owner to each business unit
- E. Set a budget with alert thresholds

### 58. The annual bill must fall and the worst queries must be identified first. Which sequence is correct?

Domain: Analyzing and optimizing technical and business processes

- A. Measure slot time → rewrite the query → inspect the plan → partition the table
- B. Inspect the query plan and bytes processed → partition and cluster the table on the filter columns → rewrite the query to prune partitions → measure the new slot time and bytes scanned
- C. Rewrite the query → partition the table → measure slot time → inspect the plan
- D. Partition and cluster the table → measure slot time → inspect the plan → rewrite the query

### 59. Two units want opposite trade-offs between cost and resilience. What should the architect do?

Domain: Analyzing and optimizing technical and business processes

- A. Publish a service catalog entry with an approved template
- B. Route the change through a change advisory board
- C. Publish a runbook per alert
- D. Agree the decision rights with the stakeholders

### 60. A new unit must self-serve a compliant platform without a ticket. What should be published?

Domain: Analyzing and optimizing technical and business processes

- A. Tag the resources with labels for cost reporting
- B. Publish a service catalog entry with an approved template
- C. Enforce the control with an organization policy constraint
- D. Manage the resources with Terraform

### 61. A change affects one of seven services and must be measured on real traffic. What should be used?

Domain: Managing implementation

- A. Deploy blue/green with a traffic switch
- B. Put the change behind a feature flag
- C. Roll out a canary to a small share of traffic
- D. Roll the change out instance by instance

### 62. Two identical environments exist, and the previous build must be exactly restorable under pressure. Which two practices apply? Select two.

Domain: Managing implementation

- A. Keep the previous image digest ready for rollback
- B. Deploy blue/green with a traffic switch
- C. Promote the same tested artifact between environments
- D. Set a budget with alert thresholds
- E. Rebuild the artifact separately for each environment

### 63. A holiday freeze means the next release must be reversible at once. Which sequence is correct?

Domain: Managing implementation

- A. Shift full traffic to the new revision → build the image → watch the error rate → promote or roll back
- B. Build an immutable image and record its digest → deploy the new revision without traffic → shift a small traffic percentage and watch error and latency signals → promote to full traffic or roll back to the pinned digest
- C. Watch the error rate → deploy the new revision → shift traffic → build the image
- D. Deploy the new revision → promote to full traffic → shift a small percentage → build the image

### 64. Seven services are exposed to partners who each need their own quota. What should be used?

Domain: Managing implementation

- A. Use API Gateway
- B. Use Cloud Endpoints
- C. Attach a Cloud Armor security policy
- D. Publish the API through Apigee

### 65. One internal service needs a managed OpenAPI front door without a policy engine. What should be used?

Domain: Managing implementation

- A. Use Cloud Endpoints
- B. Attach a Cloud Armor security policy
- C. Publish the API through Apigee
- D. Use API Gateway

### 66. A 4 TB booking database must move during a maintenance window. What should be used?

Domain: Managing implementation

- A. Copy the files with Storage Transfer Service
- B. Migrate the database with Database Migration Service
- C. Use Datastream for change data capture
- D. Use the BigQuery Data Transfer Service

### 67. A legacy service must run on GKE without being rewritten this year. What should be used?

Domain: Managing implementation

- A. Assess the estate in Migration Center
- B. Convert the VMs with Migrate to Containers
- C. Copy the files with Storage Transfer Service
- D. Run the legacy stack on Google Cloud VMware Engine

### 68. An acquisition doubles the estate and dependencies must move together. Which sequence is correct?

Domain: Managing implementation

- A. Cut over and decommission → validate a pilot wave → inventory the estate → group servers into waves
- B. Group servers into waves → inventory the estate → cut over and decommission → validate a pilot wave
- C. Validate a pilot wave → inventory the estate → group servers into waves → cut over and decommission
- D. Inventory the estate in Migration Center → group servers into dependency-based waves → validate a pilot wave in the target landing zone → cut over wave by wave and decommission the source

### 69. The forecast pipeline must be tested locally with no billable resource. What should be used?

Domain: Managing implementation

- A. Run the emulator in the pipeline
- B. Manage the resources with Terraform
- C. Run the build in Cloud Build
- D. Automate the step with the gcloud CLI

### 70. An evidence export must be scripted so the command and output are recorded. What should be used?

Domain: Managing implementation

- A. Automate the step with the gcloud CLI
- B. Use the bq command-line tool
- C. Use Cloud Shell for the one-off task
- D. Use Cloud Code in the IDE

### 71. A consumer must handle quota errors with the recommended backoff. What should it use?

Domain: Managing implementation

- A. Impersonate a service account for a curl test
- B. Use the Google API client library with retries
- C. Authenticate the call with an API key
- D. Automate the step with the gcloud CLI

### 72. Host metrics and application logs must reach Google Cloud from every unit's fleet. What should be installed?

Domain: Ensuring solution and operations excellence

- A. Install the Ops Agent on the instances
- B. Attach Cloud Profiler to the service
- C. Group the exceptions in Error Reporting
- D. Inspect the trace waterfall in Cloud Trace

### 73. One service uses four times the expected CPU and nobody knows which function. What should be attached?

Domain: Ensuring solution and operations excellence

- A. Group the exceptions in Error Reporting
- B. Attach Cloud Profiler to the service
- C. Add an uptime check from several regions
- D. Inspect the trace waterfall in Cloud Trace

### 74. The product team promised article pages under one second for 99 per cent of requests. What should be defined?

Domain: Ensuring solution and operations excellence

- A. Create an alerting policy on the metric
- B. Define an SLO with an error budget
- C. Add an uptime check from several regions
- D. Publish a shared dashboard

### 75. A specific failure must be counted and then reported to the on-call engineer. Which two steps apply? Select two.

Domain: Ensuring solution and operations excellence

- A. Create an alerting policy on the metric
- B. Define an SLO with an error budget
- C. Publish a shared dashboard
- D. Act on the Recommender suggestions
- E. Create a log-based metric

### 76. The last cascade took forty minutes to diagnose because the steps were undocumented. What should be published?

Domain: Ensuring solution and operations excellence

- A. Define an on-call rotation with an escalation path
- B. Match the support plan to the recovery commitment
- C. Publish a runbook per alert
- D. Publish a shared dashboard

### 77. The business expects a thirty-minute response to a severity-one case. What should be aligned?

Domain: Ensuring solution and operations excellence

- A. Publish a runbook per alert
- B. Match the support plan to the recovery commitment
- C. Put the recovery commitment in the contract
- D. Define an on-call rotation with an escalation path

### 78. A regional failure has never been exercised with real traffic. What should be run?

Domain: Ensuring solution and operations excellence

- A. Roll out a canary to a small share of traffic
- B. Run a load test at the expected peak
- C. Commission a penetration test
- D. Run a chaos experiment against a zone

### 79. A cascade recurred because the follow-up work was never recorded. What should be produced after each incident?

Domain: Ensuring solution and operations excellence

- A. Write a blameless postmortem with actions
- B. Match the support plan to the recovery commitment
- C. Publish a runbook per alert
- D. Publish a shared dashboard

### 80. A slow service is taking the site down and the response must follow the agreed order. Which sequence is correct?

Domain: Ensuring solution and operations excellence

- A. Isolate the root cause → detect the symptom → write the postmortem → restore service
- B. Detect the symptom through an alert → contain the impact and restore service → isolate the root cause from logs, traces, and metrics → apply the permanent fix and write the postmortem
- C. Restore service → detect the symptom → write the postmortem → isolate the root cause
- D. Write the postmortem → detect the symptom → isolate the root cause → restore service

---

## Case study — Everline Media

Everline Media publishes a news and video platform that 22 million people use each day. The product team has promised that article pages load in under one second for 99 per cent of requests and that video start time stays under two seconds for 99.5 per cent. Nobody can currently say whether either promise is met, and the last three incidents were found by readers on social media rather than by the team. The engineering organisation has 140 people across twelve teams, each with its own dashboards, and the chief technology officer wants one agreed definition of success per user journey.

The next 5 questions refer to it. Read the scenario once, then answer all 5; each item restates the constraint it tests and is scored individually.

### 81. The team promised load and start-time targets but cannot say whether they are met. What should be defined first?

Domain: Ensuring solution and operations excellence

- A. Add an uptime check from several regions
- B. Publish a shared dashboard
- C. Create an alerting policy on the metric
- D. Define an SLO with an error budget

### 82. The board asks how the platform could be replaced if the vendor relationship ended. What must the design include?

Domain: Designing and planning a cloud solution architecture

- A. Tag the resources with labels for cost reporting
- B. Build a three-year total cost of ownership model
- C. Document the exit plan and data portability
- D. Set a budget with alert thresholds

### 83. Twelve teams deploy to one platform with no shared review gate. What should the pipeline enforce?

Domain: Analyzing and optimizing technical and business processes

- A. Roll the change out instance by instance
- B. Adopt trunk-based development with short-lived branches
- C. Require a reviewed pull request and a passing plan
- D. Rebuild the artifact separately for each environment

### 84. Viewer data must not be copied outside the approved projects. What should be applied?

Domain: Designing for security and compliance

- A. Put the projects inside a VPC Service Controls perimeter
- B. Tag the resources with labels for cost reporting
- C. Apply a hierarchical firewall policy at the organization or folder
- D. Apply an IAM deny policy

### 85. Ad-delivery evidence must be undeletable for the audit period. What should be applied?

Domain: Managing and provisioning a solution infrastructure

- A. Add a lifecycle rule that transitions and then deletes
- B. Enable Autoclass on the bucket
- C. Enable object versioning
- D. Apply a bucket retention policy with a locked period

---

## Case study — Granite Utilities

Granite Utilities operates the electricity distribution network for a region of 3 million homes. Smart meters send a reading every fifteen minutes, and the control room needs a live view of demand with an alert if a substation stops reporting. Regulatory reporting requires a defensible monthly settlement figure, and any correction to a past settlement must be traceable. The platform runs on Google Cloud and the operations team is on call twenty-four hours a day. A previous incident took four hours to diagnose because the alert fired on the wrong metric and the runbook was out of date.

The next 5 questions refer to it. Read the scenario once, then answer all 5; each item restates the constraint it tests and is scored individually.

### 86. The control room must see substation telemetry with one agreed signal set. What should be built first?

Domain: Ensuring solution and operations excellence

- A. Inspect the trace waterfall in Cloud Trace
- B. Publish a shared dashboard
- C. Define dashboards and metrics in Cloud Monitoring
- D. Act on the Recommender suggestions

### 87. Readings arrive late when a concentrator reconnects and must still settle correctly. What should the pipeline use?

Domain: Designing and planning a cloud solution architecture

- A. Use Managed Service for Apache Airflow
- B. Use Dataflow
- C. Use a Dataproc cluster
- D. Trigger the job with Cloud Scheduler

### 88. A four-hour diagnosis followed an alert that fired on the wrong metric. Which two tools would have shortened it? Select two.

Domain: Analyzing and optimizing technical and business processes

- A. Publish a shared dashboard
- B. Publish a runbook per alert
- C. Inspect the trace waterfall in Cloud Trace
- D. Define an SLO with an error budget
- E. Group the exceptions in Error Reporting

### 89. A corrected settlement must show who changed it and when. What should be enabled?

Domain: Designing for security and compliance

- A. Rely on Admin Activity audit logs
- B. Create a log-based metric
- C. Review Access Transparency logs
- D. Enable Data Access audit logs

### 90. Settlement queries always filter by date, and the scan cost is rising. What should be applied first?

Domain: Managing and provisioning a solution infrastructure

- A. Create a materialized view for the repeated aggregate
- B. Leave the project on on-demand pricing
- C. Cluster the table on the filter columns
- D. Partition the table on the date column

---

## Case study — Solstice Travel

Solstice Travel runs a booking platform whose traffic is concentrated into three holiday peaks. Each peak is about eleven times the January baseline, and the company pays for peak capacity all year because the platform team has never had time to change it. The booking flow depends on seven services, and one slow service during the last peak caused a cascade that took the site down for forty minutes. The chief executive has asked for a plan that keeps the peak stable, lowers the annual bill, and shortens the time to diagnose the next cascade.

The next 5 questions refer to it. Read the scenario once, then answer all 5; each item restates the constraint it tests and is scored individually.

### 91. The platform pays for peak capacity all year while the baseline is tiny. What should the architect recommend first?

Domain: Analyzing and optimizing technical and business processes

- A. Buy committed use discounts for the steady baseline
- B. Move the steady services to E2 machine types
- C. Use sole-tenant nodes
- D. Run the batch tier on Spot VMs

### 92. Seven services run on Kubernetes and the team is three engineers. What should be chosen?

Domain: Designing and planning a cloud solution architecture

- A. Submit the work as a Batch job
- B. Deploy the service on Cloud Run
- C. Use GKE Autopilot
- D. Use GKE Standard with a node pool per workload shape

### 93. A regional loss must not stop bookings, and the data must be usable in the other region. What must the design provide?

Domain: Designing and planning a cloud solution architecture

- A. Replicate the data to the second region
- B. Run a pilot-light standby
- C. Use backup and restore
- D. Enable Cloud CDN on the backend

### 94. Booking can accept fifteen minutes of downtime and a smaller running copy. What fits?

Domain: Analyzing and optimizing technical and business processes

- A. Use backup and restore
- B. Run active-active across two regions
- C. Run a warm standby at reduced capacity
- D. Run a pilot-light standby

### 95. One slow service took the site down last peak. What should be run before the next one?

Domain: Ensuring solution and operations excellence

- A. Commission a penetration test
- B. Run a load test at the expected peak
- C. Run a chaos experiment against a zone
- D. Roll out a canary to a small share of traffic

---

## Case study — Union Foundry

Union Foundry runs a mixed estate: a Kubernetes platform for customer-facing services, a warehouse for financial reporting, and a machine learning team that builds demand forecasts. The company is preparing for an acquisition that will double its data volume and add two countries with different data residency rules. Leadership wants one operating model for all three workloads, a cost figure per business unit, and evidence that a regional failure would not stop customer-facing services. The security team has asked how the model weights and training data are protected, because the forecast is now considered a trade secret.

The next 5 questions refer to it. Read the scenario once, then answer all 5; each item restates the constraint it tests and is scored individually.

### 96. The forecast must use the same features in training and serving across two countries. What should be used?

Domain: Designing and planning a cloud solution architecture

- A. Enable model monitoring on the endpoint
- B. Serve features from Agent Platform Feature Store
- C. Orchestrate the workflow in Agent Platform Pipelines
- D. Deploy to an online prediction endpoint

### 97. The forecast model and its weights are a trade secret, and prompts must not leak them. What should be added?

Domain: Designing for security and compliance

- A. De-identify the data with Sensitive Data Protection
- B. Require an access level in the perimeter
- C. Turn on Security Command Center findings
- D. Screen prompts and responses with Model Armor

### 98. Two acquired countries must migrate with a short cutover and no data loss. What should be used?

Domain: Managing implementation

- A. Use the BigQuery Data Transfer Service
- B. Use Datastream for change data capture
- C. Copy the files with Storage Transfer Service
- D. Migrate the database with Database Migration Service

### 99. The acquisition brings new support obligations for customer-facing services. What should be aligned?

Domain: Ensuring solution and operations excellence

- A. Publish a runbook per alert
- B. Define an on-call rotation with an escalation path
- C. Match the support plan to the recovery commitment
- D. Put the recovery commitment in the contract

### 100. The forecast must be reproducible after an audit question about a past demand figure. What should be used?

Domain: Managing and provisioning a solution infrastructure

- A. Orchestrate the workflow in Agent Platform Pipelines
- B. Trigger the job with Cloud Scheduler
- C. Use a Dataproc cluster
- D. Run batch prediction

---

## Answer key and explanations

### Question 1 — D

Answer: Define the baseline and target as a KPI with an owner. A measured baseline and a named owner make the outcome testable after the programme. Local study-map skill 1.1 (Business Requirements and Success Metrics), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 1 (designing and planning): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. The model compares run cost, people cost, and exit cost rather than the monthly bill alone. Why the correct answer wins: A measured baseline and a named owner make the outcome testable after the programme.
- **B:** Incorrect for this question. The export attributes cost to the team and service that caused it. Why the correct answer wins: A measured baseline and a named owner make the outcome testable after the programme.
- **C:** Incorrect for this question. The dashboard gives the team one view of the same signals during an incident. Why the correct answer wins: A measured baseline and a named owner make the outcome testable after the programme.
- **D:** Correct. In this case: A measured baseline and a named owner make the outcome testable after the programme.

### Question 2 — C

Answer: Build a three-year total cost of ownership model. The model compares run cost, people cost, and exit cost rather than the monthly bill alone. Local study-map skill 1.1 (Business Requirements and Success Metrics), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 1 (designing and planning): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. The export attributes cost to the team and service that caused it. Why the correct answer wins: The model compares run cost, people cost, and exit cost rather than the monthly bill alone.
- **B:** Incorrect for this question. A budget alerts on spend but does not stop it. Why the correct answer wins: The model compares run cost, people cost, and exit cost rather than the monthly bill alone.
- **C:** Correct. In this case: The model compares run cost, people cost, and exit cost rather than the monthly bill alone.
- **D:** Incorrect for this question. A one- or three-year commitment discounts the capacity that runs constantly, not the peaks. Why the correct answer wins: The model compares run cost, people cost, and exit cost rather than the monthly bill alone.

### Question 3 — C

Answer: Document the exit plan and data portability. An exit plan and data portability keep the migration reversible and bound how proprietary the design may become. The exit plan keeps the migration reversible and constrains how proprietary the design may become. Local study-map skill 1.2 (Non-Functional Requirements and Trade-offs), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 1 (designing and planning): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. Labels attribute spend in billing export; they do not grant or restrict access. Why the correct answer wins: An exit plan and data portability keep the migration reversible and bound how proprietary the design may become.
- **B:** Incorrect for this question. The model compares run cost, people cost, and exit cost rather than the monthly bill alone. Why the correct answer wins: An exit plan and data portability keep the migration reversible and bound how proprietary the design may become.
- **C:** Correct. The exit plan keeps the migration reversible and constrains how proprietary the design may become. In this case: An exit plan and data portability keep the migration reversible and bound how proprietary the design may become.
- **D:** Incorrect for this question. A budget alerts on spend but does not stop it. Why the correct answer wins: An exit plan and data portability keep the migration reversible and bound how proprietary the design may become.

### Question 4 — A, C

Answers: Set the RPO and RTO with the business owner; Put the recovery commitment in the contract. The targets quantify the acceptable loss, and the contract attaches a consequence to missing them. The targets come from the business impact of data loss and downtime, not from the technology. The contract converts an internal target into an obligation with a consequence. Local study-map skill 1.2 (Non-Functional Requirements and Trade-offs), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 1 (designing and planning): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Correct. The targets come from the business impact of data loss and downtime, not from the technology. In this case: The targets quantify the acceptable loss, and the contract attaches a consequence to missing them.
- **B:** Incorrect for this question. Recommender reports idle and over-provisioned resources with the estimated saving. Why the correct answer wins: The targets quantify the acceptable loss, and the contract attaches a consequence to missing them.
- **C:** Correct. The contract converts an internal target into an obligation with a consequence. In this case: The targets quantify the acceptable loss, and the contract attaches a consequence to missing them.
- **D:** Incorrect for this question. The dashboard gives the team one view of the same signals during an incident. Why the correct answer wins: The targets quantify the acceptable loss, and the contract attaches a consequence to missing them.
- **E:** Incorrect for this question. Labels attribute spend in billing export; they do not grant or restrict access. Why the correct answer wins: The targets quantify the acceptable loss, and the contract attaches a consequence to missing them.

### Question 5 — C

Answer: Enable Cloud SQL high availability with a standby. A regional standby takes over automatically when the primary zone fails. Local study-map skill 1.3 (High Availability and Failover Design), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 1 (designing and planning): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. A replica offloads read traffic but lags the primary, so it is not a failover target. Why the correct answer wins: A regional standby takes over automatically when the primary zone fails.
- **B:** Incorrect for this question. Bigtable is a wide-column store for high-throughput key reads and writes at low latency. Why the correct answer wins: A regional standby takes over automatically when the primary zone fails.
- **C:** Correct. In this case: A regional standby takes over automatically when the primary zone fails.
- **D:** Incorrect for this question. Memorystore provides managed Redis or Memcached for sub-millisecond cache lookups. Why the correct answer wins: A regional standby takes over automatically when the primary zone fails.

### Question 6 — A, D

Answers: Run active-active across two regions; Replicate the data to the second region. Both regions serve traffic, and the data must already be in the second region when it is needed. Both regions serve traffic, so a regional loss is absorbed without a failover decision. The data must exist in the second region before any compute there can serve it. Local study-map skill 1.3 (High Availability and Failover Design), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 1 (designing and planning): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Correct. Both regions serve traffic, so a regional loss is absorbed without a failover decision. In this case: Both regions serve traffic, and the data must already be in the second region when it is needed.
- **B:** Incorrect for this question. CDN caches responses at edge locations, which cuts origin load and latency for repeat reads. Why the correct answer wins: Both regions serve traffic, and the data must already be in the second region when it is needed.
- **C:** Incorrect for this question. Only the core data and configuration stay warm, so recovery starts the compute and takes minutes. Why the correct answer wins: Both regions serve traffic, and the data must already be in the second region when it is needed.
- **D:** Correct. The data must exist in the second region before any compute there can serve it. In this case: Both regions serve traffic, and the data must already be in the second region when it is needed.
- **E:** Incorrect for this question. Restoring from backup is the cheapest option and the slowest to recover. Why the correct answer wins: Both regions serve traffic, and the data must already be in the second region when it is needed.

### Question 7 — A

Answer: Build a Network Connectivity Center hub. Peering is not transitive, so a hub provides the routing the spokes cannot provide themselves. The hub gives transitive routing between spokes, which peering alone cannot provide. Local study-map skill 1.4 (Network Design), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 1 (designing and planning): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Correct. The hub gives transitive routing between spokes, which peering alone cannot provide. In this case: Peering is not transitive, so a hub provides the routing the spokes cannot provide themselves.
- **B:** Incorrect for this question. DNS peering resolves names across networks without transferring zone ownership. Why the correct answer wins: Peering is not transitive, so a hub provides the routing the spokes cannot provide themselves.
- **C:** Incorrect for this question. Cloud NAT lets private instances reach the internet without an external address. Why the correct answer wins: Peering is not transitive, so a hub provides the routing the spokes cannot provide themselves.
- **D:** Incorrect for this question. Peering joins two networks at layer three but does not share firewalls or transitive routes. Why the correct answer wins: Peering is not transitive, so a hub provides the routing the spokes cannot provide themselves.

### Question 8 — B, C

Answers: Publish the service through Private Service Connect; Peer the two VPC networks. A published endpoint gives a private address, and peering joins the two networks at layer three. A PSC endpoint gives a private IP in the consumer VPC without peering or exposing the service publicly. Peering joins two networks at layer three but does not share firewalls or transitive routes. Local study-map skill 1.4 (Network Design), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 1 (designing and planning): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. CDN caches responses at edge locations, which cuts origin load and latency for repeat reads. Why the correct answer wins: A published endpoint gives a private address, and peering joins the two networks at layer three.
- **B:** Correct. Peering joins two networks at layer three but does not share firewalls or transitive routes. In this case: A published endpoint gives a private address, and peering joins the two networks at layer three.
- **C:** Correct. A PSC endpoint gives a private IP in the consumer VPC without peering or exposing the service publicly. In this case: A published endpoint gives a private address, and peering joins the two networks at layer three.
- **D:** Incorrect for this question. Cloud NAT lets private instances reach the internet without an external address. Why the correct answer wins: A published endpoint gives a private address, and peering joins the two networks at layer three.
- **E:** Incorrect for this question. A signed URL grants one object for a fixed time without exposing credentials or making the bucket public. Why the correct answer wins: A published endpoint gives a private address, and peering joins the two networks at layer three.

### Question 9 — A

Answer: Enable Autoclass on the bucket. Autoclass moves each object between classes as its access pattern changes, with no rules to maintain. Local study-map skill 1.5 (Storage and Data Store Selection), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 1 (designing and planning): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Correct. In this case: Autoclass moves each object between classes as its access pattern changes, with no rules to maintain.
- **B:** Incorrect for this question. A lifecycle rule acts on object age or class, so retention stops depending on a person. Why the correct answer wins: Autoclass moves each object between classes as its access pattern changes, with no rules to maintain.
- **C:** Incorrect for this question. Nearline suits data read about once a month and charges for early deletion. Why the correct answer wins: Autoclass moves each object between classes as its access pattern changes, with no rules to maintain.
- **D:** Incorrect for this question. Standard is for data read frequently and has no retrieval fee. Why the correct answer wins: Autoclass moves each object between classes as its access pattern changes, with no rules to maintain.

### Question 10 — C, D

Answers: Use a dual-region bucket; Enable object versioning. The dual-region bucket survives one region loss, and versioning keeps a noncurrent copy on overwrite. A dual-region bucket keeps two replicas in a chosen pair of regions and survives one region loss. Versioning keeps a noncurrent copy when an object is overwritten or deleted. Local study-map skill 1.5 (Storage and Data Store Selection), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 1 (designing and planning): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. Filestore provides a managed NFS export that many clients can mount at once. Why the correct answer wins: The dual-region bucket survives one region loss, and versioning keeps a noncurrent copy on overwrite.
- **B:** Incorrect for this question. Archive is cheapest to hold and slowest and most expensive to retrieve. Why the correct answer wins: The dual-region bucket survives one region loss, and versioning keeps a noncurrent copy on overwrite.
- **C:** Correct. A dual-region bucket keeps two replicas in a chosen pair of regions and survives one region loss. In this case: The dual-region bucket survives one region loss, and versioning keeps a noncurrent copy on overwrite.
- **D:** Correct. Versioning keeps a noncurrent copy when an object is overwritten or deleted. In this case: The dual-region bucket survives one region loss, and versioning keeps a noncurrent copy on overwrite.
- **E:** Incorrect for this question. Local SSD is the fastest ephemeral option and loses its data when the VM stops. Why the correct answer wins: The dual-region bucket survives one region loss, and versioning keeps a noncurrent copy on overwrite.

### Question 11 — D

Answer: Use GKE Autopilot. Autopilot manages nodes, scaling, and patching, so the team owns only its workloads. Local study-map skill 1.6 (Compute Platform Selection), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 1 (designing and planning): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. Cloud Run runs a stateless container per request and scales to zero when idle. Why the correct answer wins: Autopilot manages nodes, scaling, and patching, so the team owns only its workloads.
- **B:** Incorrect for this question. Batch schedules containerised jobs onto managed or existing capacity and retires it when done. Why the correct answer wins: Autopilot manages nodes, scaling, and patching, so the team owns only its workloads.
- **C:** Incorrect for this question. Standard exposes node configuration and patching, which the team must then run itself. Why the correct answer wins: Autopilot manages nodes, scaling, and patching, so the team owns only its workloads.
- **D:** Correct. In this case: Autopilot manages nodes, scaling, and patching, so the team owns only its workloads.

### Question 12 — C

Answer: Deploy the service on Cloud Run. Cloud Run scales to zero and bills per request, which suits an intermittent endpoint. Cloud Run runs a stateless container per request and scales to zero when idle. Local study-map skill 1.6 (Compute Platform Selection), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 1 (designing and planning): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. Standard exposes node configuration and patching, which the team must then run itself. Why the correct answer wins: Cloud Run scales to zero and bills per request, which suits an intermittent endpoint.
- **B:** Incorrect for this question. VMware Engine keeps the existing hypervisor and operations model while moving the hardware into Google Cloud. Why the correct answer wins: Cloud Run scales to zero and bills per request, which suits an intermittent endpoint.
- **C:** Correct. Cloud Run runs a stateless container per request and scales to zero when idle. In this case: Cloud Run scales to zero and bills per request, which suits an intermittent endpoint.
- **D:** Incorrect for this question. The group replaces unhealthy instances and adds capacity from a template as load rises. Why the correct answer wins: Cloud Run scales to zero and bills per request, which suits an intermittent endpoint.

### Question 13 — B

Answer: Submit the work as a Batch job. Batch schedules containerised jobs onto managed capacity and retires it when the work is done. Local study-map skill 1.6 (Compute Platform Selection), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 1 (designing and planning): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. Cloud Run runs a stateless container per request and scales to zero when idle. Why the correct answer wins: Batch schedules containerised jobs onto managed capacity and retires it when the work is done.
- **B:** Correct. In this case: Batch schedules containerised jobs onto managed capacity and retires it when the work is done.
- **C:** Incorrect for this question. The group replaces unhealthy instances and adds capacity from a template as load rises. Why the correct answer wins: Batch schedules containerised jobs onto managed capacity and retires it when the work is done.
- **D:** Incorrect for this question. Standard exposes node configuration and patching, which the team must then run itself. Why the correct answer wins: Batch schedules containerised jobs onto managed capacity and retires it when the work is done.

### Question 14 — C

Answer: Load the data into BigQuery. BigQuery is serverless and separates storage from compute, so a scan pays for the bytes read. Local study-map skill 1.7 (Data Processing and Analytics Selection), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 1 (designing and planning): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. Cloud SQL is a managed MySQL, PostgreSQL, or SQL Server instance with a familiar connection model. Why the correct answer wins: BigQuery is serverless and separates storage from compute, so a scan pays for the bytes read.
- **B:** Incorrect for this question. Bigtable is a wide-column store for high-throughput key reads and writes at low latency. Why the correct answer wins: BigQuery is serverless and separates storage from compute, so a scan pays for the bytes read.
- **C:** Correct. In this case: BigQuery is serverless and separates storage from compute, so a scan pays for the bytes read.
- **D:** Incorrect for this question. Firestore is a document store with real-time listeners and per-document transactions. Why the correct answer wins: BigQuery is serverless and separates storage from compute, so a scan pays for the bytes read.

### Question 15 — B, C

Answers: Reserve BigQuery BI Engine capacity; Buy BigQuery slot commitments with autoscaling. BI Engine holds the working set in memory, and slot commitments price steady query volume. BI Engine holds a working set in memory so dashboards answer without scanning the table each time. Slots are the unit of compute, and autoscaling adds them only while queries queue. Local study-map skill 1.7 (Data Processing and Analytics Selection), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 1 (designing and planning): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. On-demand bills per byte scanned, which is cheap for sparse use and unpredictable at scale. Why the correct answer wins: BI Engine holds the working set in memory, and slot commitments price steady query volume.
- **B:** Correct. Slots are the unit of compute, and autoscaling adds them only while queries queue. In this case: BI Engine holds the working set in memory, and slot commitments price steady query volume.
- **C:** Correct. BI Engine holds a working set in memory so dashboards answer without scanning the table each time. In this case: BI Engine holds the working set in memory, and slot commitments price steady query volume.
- **D:** Incorrect for this question. InsertAll is best-effort and only deduplicates on a provided insert ID, so duplicates can land. Why the correct answer wins: BI Engine holds the working set in memory, and slot commitments price steady query volume.
- **E:** Incorrect for this question. Looker Studio renders the visualisation but inherits whatever query and permissions sit beneath it. Why the correct answer wins: BI Engine holds the working set in memory, and slot commitments price steady query volume.

### Question 16 — A

Answer: Call Gemini through Agent Platform. The managed endpoint adds IAM, audit logging, and regional processing terms. Local study-map skill 1.8 (AI and ML Solution Design), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 1 (designing and planning): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Correct. In this case: The managed endpoint adds IAM, audit logging, and regional processing terms.
- **B:** Incorrect for this question. Vertex AI Search returns grounded, cited results over private documents without a custom index. Why the correct answer wins: The managed endpoint adds IAM, audit logging, and regional processing terms.
- **C:** Incorrect for this question. Gemini Enterprise adds enterprise search, agents, and governance over the connected corpus. Why the correct answer wins: The managed endpoint adds IAM, audit logging, and regional processing terms.
- **D:** Incorrect for this question. The prebuilt Vision model labels, detects, and reads text without training a model. Why the correct answer wins: The managed endpoint adds IAM, audit logging, and regional processing terms.

### Question 17 — A

Answer: Index the corpus with Vertex AI Search. Vertex AI Search returns grounded, cited results over private documents without a custom index. Local study-map skill 1.8 (AI and ML Solution Design), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 1 (designing and planning): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Correct. In this case: Vertex AI Search returns grounded, cited results over private documents without a custom index.
- **B:** Incorrect for this question. The prebuilt Vision model labels, detects, and reads text without training a model. Why the correct answer wins: Vertex AI Search returns grounded, cited results over private documents without a custom index.
- **C:** Incorrect for this question. The translation model handles 100 or more languages without custom training. Why the correct answer wins: Vertex AI Search returns grounded, cited results over private documents without a custom index.
- **D:** Incorrect for this question. A Document AI processor extracts structured fields from forms and invoices with layout awareness. Why the correct answer wins: Vertex AI Search returns grounded, cited results over private documents without a custom index.

### Question 18 — C

Answer: Assess the estate in Migration Center. Migration Center inventories the estate and estimates target size and cost before a plan is funded. Migration Center inventories the servers and estimates the target size and cost. Local study-map skill 1.9 (Migration Planning and Future Improvement), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 1 (designing and planning): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. The service moves object data between buckets or clouds on a schedule. Why the correct answer wins: Migration Center inventories the estate and estimates target size and cost before a plan is funded.
- **B:** Incorrect for this question. The service moves a database with continuous replication and a short cutover window. Why the correct answer wins: Migration Center inventories the estate and estimates target size and cost before a plan is funded.
- **C:** Correct. Migration Center inventories the servers and estimates the target size and cost. In this case: Migration Center inventories the estate and estimates target size and cost before a plan is funded.
- **D:** Incorrect for this question. The tool rewrites a VM workload into a container image so it can run on GKE. Why the correct answer wins: Migration Center inventories the estate and estimates target size and cost before a plan is funded.

### Question 19 — B

Answer: Use a Transfer Appliance for the one-off bulk move. The appliance ships the data physically when the network would take months to carry it. Local study-map skill 1.9 (Migration Planning and Future Improvement), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 1 (designing and planning): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. The service runs scheduled, filtered transfers from another cloud or an HTTP source. Why the correct answer wins: The appliance ships the data physically when the network would take months to carry it.
- **B:** Correct. In this case: The appliance ships the data physically when the network would take months to carry it.
- **C:** Incorrect for this question. The storage commands copy and sync objects with resumable, parallel transfers. Why the correct answer wins: The appliance ships the data physically when the network would take months to carry it.
- **D:** Incorrect for this question. The service moves object data between buckets or clouds on a schedule. Why the correct answer wins: The appliance ships the data physically when the network would take months to carry it.

### Question 20 — C

Answer: Set the RTO and RPO targets → choose the DR pattern that meets them → build and replicate the standby environment → fail over in a game day and record the result. Targets drive the pattern, the pattern drives the build, and only a rehearsal proves the numbers. Local study-map skill 1.9 (Migration Planning and Future Improvement), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 1 (designing and planning): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. The pattern has no basis until the targets exist, and the drill cannot precede the build. Why the correct answer wins: Targets drive the pattern, the pattern drives the build, and only a rehearsal proves the numbers.
- **B:** Incorrect for this question. Building before the targets and pattern are chosen risks an environment that cannot meet either. Why the correct answer wins: Targets drive the pattern, the pattern drives the build, and only a rehearsal proves the numbers.
- **C:** Correct. In this case: Targets drive the pattern, the pattern drives the build, and only a rehearsal proves the numbers.
- **D:** Incorrect for this question. A failover drill with no targets or standby environment proves nothing. Why the correct answer wins: Targets drive the pattern, the pattern drives the build, and only a rehearsal proves the numbers.

### Question 21 — A

Answer: Use HA VPN with two tunnels. Two tunnels across two interfaces survive one path failing, and the SLA depends on that. Local study-map skill 2.1 (Hybrid and Multicloud Connectivity), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 2 (managing and provisioning): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Correct. In this case: Two tunnels across two interfaces survive one path failing, and the SLA depends on that.
- **B:** Incorrect for this question. A dedicated circuit gives predictable bandwidth and a private path at a colocation facility. Why the correct answer wins: Two tunnels across two interfaces survive one path failing, and the SLA depends on that.
- **C:** Incorrect for this question. Cloud NAT lets private instances reach the internet without an external address. Why the correct answer wins: Two tunnels across two interfaces survive one path failing, and the SLA depends on that.
- **D:** Incorrect for this question. CDN caches responses at edge locations, which cuts origin load and latency for repeat reads. Why the correct answer wins: Two tunnels across two interfaces survive one path failing, and the SLA depends on that.

### Question 22 — B, C

Answers: Deploy Cloud NAT for outbound traffic; Enable Private Google Access on the subnet. Private Google Access reaches the APIs from an internal address, and Cloud NAT carries outbound internet traffic. Cloud NAT lets private instances reach the internet without an external address. Private Google Access reaches Google APIs from an internal address without a proxy or a NAT gateway. Local study-map skill 2.1 (Hybrid and Multicloud Connectivity), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 2 (managing and provisioning): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. IAP authenticates and authorises each request before it reaches the backend, with no VPN. Why the correct answer wins: Private Google Access reaches the APIs from an internal address, and Cloud NAT carries outbound internet traffic.
- **B:** Correct. Cloud NAT lets private instances reach the internet without an external address. In this case: Private Google Access reaches the APIs from an internal address, and Cloud NAT carries outbound internet traffic.
- **C:** Correct. Private Google Access reaches Google APIs from an internal address without a proxy or a NAT gateway. In this case: Private Google Access reaches the APIs from an internal address, and Cloud NAT carries outbound internet traffic.
- **D:** Incorrect for this question. CDN caches responses at edge locations, which cuts origin load and latency for repeat reads. Why the correct answer wins: Private Google Access reaches the APIs from an internal address, and Cloud NAT carries outbound internet traffic.
- **E:** Incorrect for this question. Cloud Armor filters requests at the edge with allow and deny rules and adaptive protection. Why the correct answer wins: Private Google Access reaches the APIs from an internal address, and Cloud NAT carries outbound internet traffic.

### Question 23 — D

Answer: Apply a bucket retention policy with a locked period. A locked retention policy prevents deletion or a shorter period, which is the evidence an auditor tests. Local study-map skill 2.2 (Storage Configuration and Lifecycle), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 2 (managing and provisioning): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. Autoclass moves each object between classes as its access pattern changes, with no lifecycle rules to maintain. Why the correct answer wins: A locked retention policy prevents deletion or a shorter period, which is the evidence an auditor tests.
- **B:** Incorrect for this question. Versioning keeps a noncurrent copy when an object is overwritten or deleted. Why the correct answer wins: A locked retention policy prevents deletion or a shorter period, which is the evidence an auditor tests.
- **C:** Incorrect for this question. A lifecycle rule acts on object age or class, so retention stops depending on a person. Why the correct answer wins: A locked retention policy prevents deletion or a shorter period, which is the evidence an auditor tests.
- **D:** Correct. In this case: A locked retention policy prevents deletion or a shorter period, which is the evidence an auditor tests.

### Question 24 — A, B

Answers: Partition the table on the date column; Cluster the table on the filter columns. Partitioning limits each query to the dates it names, and clustering sorts within the partition on the filter column. Partitioning limits a query to the date ranges it names, so it scans less. Clustering sorts within partitions so a filtered query reads fewer blocks. Local study-map skill 2.2 (Storage Configuration and Lifecycle), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 2 (managing and provisioning): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Correct. Partitioning limits a query to the date ranges it names, so it scans less. In this case: Partitioning limits each query to the dates it names, and clustering sorts within the partition on the filter column.
- **B:** Correct. Clustering sorts within partitions so a filtered query reads fewer blocks. In this case: Partitioning limits each query to the dates it names, and clustering sorts within the partition on the filter column.
- **C:** Incorrect for this question. On-demand bills per byte scanned, which is cheap for sparse use and unpredictable at scale. Why the correct answer wins: Partitioning limits each query to the dates it names, and clustering sorts within the partition on the filter column.
- **D:** Incorrect for this question. Looker Studio renders the visualisation but inherits whatever query and permissions sit beneath it. Why the correct answer wins: Partitioning limits each query to the dates it names, and clustering sorts within the partition on the filter column.
- **E:** Incorrect for this question. The view stores the aggregate result and refreshes incrementally as base data arrives. Why the correct answer wins: Partitioning limits each query to the dates it names, and clustering sorts within the partition on the filter column.

### Question 25 — C, E

Answers: Run the batch tier on Spot VMs; Buy committed use discounts for the steady baseline. Spot capacity covers the spike, and a commitment discounts the capacity that runs constantly. Spot capacity costs far less but can be reclaimed with 30 seconds of notice. A one- or three-year commitment discounts the capacity that runs constantly, not the peaks. Local study-map skill 2.3 (Compute Provisioning and Patch Management), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 2 (managing and provisioning): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. Showing owners their own spend changes behaviour more reliably than a central report. Why the correct answer wins: Spot capacity covers the spike, and a commitment discounts the capacity that runs constantly.
- **B:** Incorrect for this question. E2 shapes trade peak performance for a lower price on workloads that do not need it. Why the correct answer wins: Spot capacity covers the spike, and a commitment discounts the capacity that runs constantly.
- **C:** Correct. Spot capacity costs far less but can be reclaimed with 30 seconds of notice. In this case: Spot capacity covers the spike, and a commitment discounts the capacity that runs constantly.
- **D:** Incorrect for this question. Local SSD is the fastest ephemeral option and loses its data when the VM stops. Why the correct answer wins: Spot capacity covers the spike, and a commitment discounts the capacity that runs constantly.
- **E:** Correct. A one- or three-year commitment discounts the capacity that runs constantly, not the peaks. In this case: Spot capacity covers the spike, and a commitment discounts the capacity that runs constantly.

### Question 26 — C

Answer: Use VM Manager for OS patch compliance. VM Manager inventories and applies patches across the fleet instead of relying on manual runs. Local study-map skill 2.3 (Compute Provisioning and Patch Management), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 2 (managing and provisioning): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. Spot capacity costs far less but can be reclaimed with 30 seconds of notice. Why the correct answer wins: VM Manager inventories and applies patches across the fleet instead of relying on manual runs.
- **B:** Incorrect for this question. Config Connector reconciles Google Cloud resources from Kubernetes manifests alongside the workloads. Why the correct answer wins: VM Manager inventories and applies patches across the fleet instead of relying on manual runs.
- **C:** Correct. In this case: VM Manager inventories and applies patches across the fleet instead of relying on manual runs.
- **D:** Incorrect for this question. Cloud Build executes the pipeline steps in a managed, isolated worker with recorded provenance. Why the correct answer wins: VM Manager inventories and applies patches across the fleet instead of relying on manual runs.

### Question 27 — B

Answer: Enable Workload Identity Federation for GKE. Workload Identity binds the pod identity to IAM, so pods hold no keys. The feature binds a Kubernetes service account to an IAM service account, so pods hold no keys. Local study-map skill 2.4 (Container Orchestration), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 2 (managing and provisioning): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. A key file is a long-lived credential that works until it is noticed and revoked. Why the correct answer wins: Workload Identity binds the pod identity to IAM, so pods hold no keys.
- **B:** Correct. The feature binds a Kubernetes service account to an IAM service account, so pods hold no keys. In this case: Workload Identity binds the pod identity to IAM, so pods hold no keys.
- **C:** Incorrect for this question. Federation exchanges an external token for short-lived Google Cloud credentials, so no key leaves the provider. Why the correct answer wins: Workload Identity binds the pod identity to IAM, so pods hold no keys.
- **D:** Incorrect for this question. An environment variable is visible to anything that can read the instance metadata or the process list. Why the correct answer wins: Workload Identity binds the pod identity to IAM, so pods hold no keys.

### Question 28 — B

Answer: Create private nodes with no external IP addresses. Private nodes reach Google APIs through Private Google Access from an internal address. Local study-map skill 2.4 (Container Orchestration), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 2 (managing and provisioning): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. Sole tenancy keeps the physical host dedicated, which matters for licensing or isolation rules. Why the correct answer wins: Private nodes reach Google APIs through Private Google Access from an internal address.
- **B:** Correct. In this case: Private nodes reach Google APIs through Private Google Access from an internal address.
- **C:** Incorrect for this question. A zonal cluster keeps its control plane in one zone, so that zone loss takes the cluster with it. Why the correct answer wins: Private nodes reach Google APIs through Private Google Access from an internal address.
- **D:** Incorrect for this question. Cloud NAT lets private instances reach the internet without an external address. Why the correct answer wins: Private nodes reach Google APIs through Private Google Access from an internal address.

### Question 29 — A

Answer: Create the project and enable APIs → build a Shared VPC with private subnets → create a regional private cluster with Workload Identity Federation for GKE → deploy through Binary Authorization. Network and identity exist before the cluster, and the admission policy is enforceable only once the cluster is running. Local study-map skill 2.4 (Container Orchestration), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 2 (managing and provisioning): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Correct. In this case: Network and identity exist before the cluster, and the admission policy is enforceable only once the cluster is running.
- **B:** Incorrect for this question. The project precedes its network, and the deploy step belongs after the cluster rather than in the middle. Why the correct answer wins: Network and identity exist before the cluster, and the admission policy is enforceable only once the cluster is running.
- **C:** Incorrect for this question. Admission control cannot run before a cluster exists, and no resource can be created before its project. Why the correct answer wins: Network and identity exist before the cluster, and the admission policy is enforceable only once the cluster is running.
- **D:** Incorrect for this question. A private cluster needs the shared network first, and the APIs must be enabled before any resource is created. Why the correct answer wins: Network and identity exist before the cluster, and the admission policy is enforceable only once the cluster is running.

### Question 30 — A

Answer: Set a minimum instance count on the Cloud Run service. A minimum instance count keeps warm capacity ready before the first request arrives. Keeping warm instances removes cold starts at the cost of paying for idle capacity. Local study-map skill 2.5 (Serverless Configuration), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 2 (managing and provisioning): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Correct. Keeping warm instances removes cold starts at the cost of paying for idle capacity. In this case: A minimum instance count keeps warm capacity ready before the first request arrives.
- **B:** Incorrect for this question. Serverless GPU attachment suits bursty inference where a reserved node would idle. Why the correct answer wins: A minimum instance count keeps warm capacity ready before the first request arrives.
- **C:** Incorrect for this question. Concurrency packs more simultaneous requests into each instance before another is started. Why the correct answer wins: A minimum instance count keeps warm capacity ready before the first request arrives.
- **D:** Incorrect for this question. The flexible environment runs a custom runtime on managed VMs but does not scale to zero. Why the correct answer wins: A minimum instance count keeps warm capacity ready before the first request arrives.

### Question 31 — B

Answer: Use Cloud Run functions. Functions bind one small handler to an event source and are the lightest way to react to one. Local study-map skill 2.5 (Serverless Configuration), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 2 (managing and provisioning): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. The group replaces unhealthy instances and adds capacity from a template as load rises. Why the correct answer wins: Functions bind one small handler to an event source and are the lightest way to react to one.
- **B:** Correct. In this case: Functions bind one small handler to an event source and are the lightest way to react to one.
- **C:** Incorrect for this question. Batch schedules containerised jobs onto managed or existing capacity and retires it when done. Why the correct answer wins: Functions bind one small handler to an event source and are the lightest way to react to one.
- **D:** Incorrect for this question. Cloud Run runs a stateless container per request and scales to zero when idle. Why the correct answer wins: Functions bind one small handler to an event source and are the lightest way to react to one.

### Question 32 — B

Answer: Manage the resources with Terraform. Terraform holds the desired state and produces a plan that a reviewer can read before apply. Terraform holds desired state in code, plans the diff, and applies it through a provider. Local study-map skill 2.6 (Infrastructure as Code), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 2 (managing and provisioning): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. Config Connector reconciles Google Cloud resources from Kubernetes manifests alongside the workloads. Why the correct answer wins: Terraform holds the desired state and produces a plan that a reviewer can read before apply.
- **B:** Correct. Terraform holds desired state in code, plans the diff, and applies it through a provider. In this case: Terraform holds the desired state and produces a plan that a reviewer can read before apply.
- **C:** Incorrect for this question. Deployment Manager is the native but older templating service with no plan step. Why the correct answer wins: Terraform holds the desired state and produces a plan that a reviewer can read before apply.
- **D:** Incorrect for this question. The CLI exposes every API as a command that can be scripted and logged. Why the correct answer wins: Terraform holds the desired state and produces a plan that a reviewer can read before apply.

### Question 33 — B

Answer: Orchestrate the workflow in Agent Platform Pipelines. Pipelines runs each step as a container with lineage and caching, so a rerun is reproducible. Local study-map skill 2.7 (Agent Platform ML Workflows), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 2 (managing and provisioning): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. A Dataproc cluster runs open-source Spark and Hadoop with jobs that need a persistent cluster. Why the correct answer wins: Pipelines runs each step as a container with lineage and caching, so a rerun is reproducible.
- **B:** Correct. In this case: Pipelines runs each step as a container with lineage and caching, so a rerun is reproducible.
- **C:** Incorrect for this question. Batch prediction reads a file and writes predictions without holding serving capacity. Why the correct answer wins: Pipelines runs each step as a container with lineage and caching, so a rerun is reproducible.
- **D:** Incorrect for this question. Scheduler fires a job on a cron or App Engine schedule and retries on failure. Why the correct answer wins: Pipelines runs each step as a container with lineage and caching, so a rerun is reproducible.

### Question 34 — A

Answer: Use the Vision API for the images. The prebuilt Vision model labels, detects, and reads text without training a model. Local study-map skill 2.8 (Prebuilt AI APIs and Model Garden), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 2 (managing and provisioning): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Correct. In this case: The prebuilt Vision model labels, detects, and reads text without training a model.
- **B:** Incorrect for this question. The prebuilt speech model transcribes audio including domain phrases through adaptation. Why the correct answer wins: The prebuilt Vision model labels, detects, and reads text without training a model.
- **C:** Incorrect for this question. A Document AI processor extracts structured fields from forms and invoices with layout awareness. Why the correct answer wins: The prebuilt Vision model labels, detects, and reads text without training a model.
- **D:** Incorrect for this question. The translation model handles 100 or more languages without custom training. Why the correct answer wins: The prebuilt Vision model labels, detects, and reads text without training a model.

### Question 35 — D

Answer: Create the Pub/Sub topic and subscription → design the Dataflow windowing and allowed lateness → deploy the streaming job with a dead-letter path → monitor watermark lag and backfill from the raw archive. The source exists before the job, the window policy is chosen before deployment, and monitoring follows the running pipeline. Local study-map skill 2.8 (Prebuilt AI APIs and Model Garden), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 2 (managing and provisioning): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. Monitoring before deployment observes nothing, and the topic is created before the job. Why the correct answer wins: The source exists before the job, the window policy is chosen before deployment, and monitoring follows the running pipeline.
- **B:** Incorrect for this question. A job cannot start without its topic, and the window policy belongs in the design, not after deployment. Why the correct answer wins: The source exists before the job, the window policy is chosen before deployment, and monitoring follows the running pipeline.
- **C:** Incorrect for this question. There is nothing to monitor before the job runs, and the job needs a topic. Why the correct answer wins: The source exists before the job, the window policy is chosen before deployment, and monitoring follows the running pipeline.
- **D:** Correct. In this case: The source exists before the job, the window policy is chosen before deployment, and monitoring follows the running pipeline.

### Question 36 — C

Answer: Define a custom role with only the required permissions. A custom role expresses least privilege when no predefined role matches the job exactly. Local study-map skill 3.1 (IAM and Least Privilege), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 3 (security and compliance): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. A bastion is still an internet-facing host that must be patched and watched. Why the correct answer wins: A custom role expresses least privilege when no predefined role matches the job exactly.
- **B:** Incorrect for this question. A predefined role grants the curated permission set for one job at the level it is bound to. Why the correct answer wins: A custom role expresses least privilege when no predefined role matches the job exactly.
- **C:** Correct. In this case: A custom role expresses least privilege when no predefined role matches the job exactly.
- **D:** Incorrect for this question. An API key identifies a project and does not authorise a user, so it cannot express least privilege. Why the correct answer wins: A custom role expresses least privilege when no predefined role matches the job exactly.

### Question 37 — C

Answer: Give each service its own service account. A per-service identity keeps the blast radius of a leaked credential to one workload. Local study-map skill 3.1 (IAM and Least Privilege), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 3 (security and compliance): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. Labels attribute spend in billing export; they do not grant or restrict access. Why the correct answer wins: A per-service identity keeps the blast radius of a leaked credential to one workload.
- **B:** Incorrect for this question. A key file is a long-lived credential that works until it is noticed and revoked. Why the correct answer wins: A per-service identity keeps the blast radius of a leaked credential to one workload.
- **C:** Correct. In this case: A per-service identity keeps the blast radius of a leaked credential to one workload.
- **D:** Incorrect for this question. A project is the boundary for quota, billing, and most IAM inheritance. Why the correct answer wins: A per-service identity keeps the blast radius of a leaked credential to one workload.

### Question 38 — A, E

Answers: Add an IAM condition on the binding; Apply an IAM deny policy. The condition narrows when the grant applies, and the deny policy overrides every allow beneath it. A condition narrows when a grant applies, for example to a time window or a resource prefix. A deny policy overrides every allow beneath it, which is how an exception is made impossible. Local study-map skill 3.1 (IAM and Least Privilege), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 3 (security and compliance): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Correct. A condition narrows when a grant applies, for example to a time window or a resource prefix. In this case: The condition narrows when the grant applies, and the deny policy overrides every allow beneath it.
- **B:** Incorrect for this question. A predefined role grants the curated permission set for one job at the level it is bound to. Why the correct answer wins: The condition narrows when the grant applies, and the deny policy overrides every allow beneath it.
- **C:** Incorrect for this question. Labels attribute spend in billing export; they do not grant or restrict access. Why the correct answer wins: The condition narrows when the grant applies, and the deny policy overrides every allow beneath it.
- **D:** Incorrect for this question. A bastion is still an internet-facing host that must be patched and watched. Why the correct answer wins: The condition narrows when the grant applies, and the deny policy overrides every allow beneath it.
- **E:** Correct. A deny policy overrides every allow beneath it, which is how an exception is made impossible. In this case: The condition narrows when the grant applies, and the deny policy overrides every allow beneath it.

### Question 39 — A

Answer: Enforce the control with an organization policy constraint. An organization policy blocks the action across every project regardless of who holds the role. Local study-map skill 3.2 (Resource Hierarchy and Organization Policy), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 3 (security and compliance): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Correct. In this case: An organization policy blocks the action across every project regardless of who holds the role.
- **B:** Incorrect for this question. Labels attribute spend in billing export; they do not grant or restrict access. Why the correct answer wins: An organization policy blocks the action across every project regardless of who holds the role.
- **C:** Incorrect for this question. A project is the boundary for quota, billing, and most IAM inheritance. Why the correct answer wins: An organization policy blocks the action across every project regardless of who holds the role.
- **D:** Incorrect for this question. A folder binding inherits to every project beneath it, so new projects start with the right access. Why the correct answer wins: An organization policy blocks the action across every project regardless of who holds the role.

### Question 40 — D, E

Answers: Create a folder per environment and bind roles there; Create a separate project per environment. A folder binding inherits to every project beneath it, and a project is the boundary for quota and billing. A folder binding inherits to every project beneath it, so new projects start with the right access. A project is the boundary for quota, billing, and most IAM inheritance. Local study-map skill 3.2 (Resource Hierarchy and Organization Policy), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 3 (security and compliance): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. A predefined role grants the curated permission set for one job at the level it is bound to. Why the correct answer wins: A folder binding inherits to every project beneath it, and a project is the boundary for quota and billing.
- **B:** Incorrect for this question. A condition narrows when a grant applies, for example to a time window or a resource prefix. Why the correct answer wins: A folder binding inherits to every project beneath it, and a project is the boundary for quota and billing.
- **C:** Incorrect for this question. Labels attribute spend in billing export; they do not grant or restrict access. Why the correct answer wins: A folder binding inherits to every project beneath it, and a project is the boundary for quota and billing.
- **D:** Correct. A folder binding inherits to every project beneath it, so new projects start with the right access. In this case: A folder binding inherits to every project beneath it, and a project is the boundary for quota and billing.
- **E:** Correct. A project is the boundary for quota, billing, and most IAM inheritance. In this case: A folder binding inherits to every project beneath it, and a project is the boundary for quota and billing.

### Question 41 — D

Answer: Encrypt with a customer-managed key in Cloud KMS. A customer-managed key lets the company disable the key and stop decryption at once. CMEK lets you control the key lifecycle, rotation, and the ability to revoke access to the data. Local study-map skill 3.3 (Encryption, CMEK, and Secrets), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 3 (security and compliance): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. Secret Manager versions the secret, controls access by IAM, and can rotate it. Why the correct answer wins: A customer-managed key lets the company disable the key and stop decryption at once.
- **B:** Incorrect for this question. Cloud HSM keeps the key material in a hardware module that meets FIPS 140-2 level 3. Why the correct answer wins: A customer-managed key lets the company disable the key and stop decryption at once.
- **C:** Incorrect for this question. CSEK is held by the caller and never stored by Google, so losing it loses the object. Why the correct answer wins: A customer-managed key lets the company disable the key and stop decryption at once.
- **D:** Correct. CMEK lets you control the key lifecycle, rotation, and the ability to revoke access to the data. In this case: A customer-managed key lets the company disable the key and stop decryption at once.

### Question 42 — B, C

Answers: Create the key ring in the same region as the data; Set an automatic rotation period on the key. The key ring's location fixes where the key material lives, and automatic rotation issues a new version on schedule. A regional key cannot encrypt a resource in another region, which is why residency drives key placement. Rotation issues a new key version on schedule and keeps old versions for decryption. Local study-map skill 3.3 (Encryption, CMEK, and Secrets), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 3 (security and compliance): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. An environment variable is visible to anything that can read the instance metadata or the process list. Why the correct answer wins: The key ring's location fixes where the key material lives, and automatic rotation issues a new version on schedule.
- **B:** Correct. A regional key cannot encrypt a resource in another region, which is why residency drives key placement. In this case: The key ring's location fixes where the key material lives, and automatic rotation issues a new version on schedule.
- **C:** Correct. Rotation issues a new key version on schedule and keeps old versions for decryption. In this case: The key ring's location fixes where the key material lives, and automatic rotation issues a new version on schedule.
- **D:** Incorrect for this question. CSEK is held by the caller and never stored by Google, so losing it loses the object. Why the correct answer wins: The key ring's location fixes where the key material lives, and automatic rotation issues a new version on schedule.
- **E:** Incorrect for this question. Cloud HSM keeps the key material in a hardware module that meets FIPS 140-2 level 3. Why the correct answer wins: The key ring's location fixes where the key material lives, and automatic rotation issues a new version on schedule.

### Question 43 — C

Answer: Put the projects inside a VPC Service Controls perimeter. A service perimeter blocks data movement out of the covered services even for a principal with the role. Local study-map skill 3.4 (VPC Service Controls and Network Security), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 3 (security and compliance): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. A deny policy overrides every allow beneath it, which is how an exception is made impossible. Why the correct answer wins: A service perimeter blocks data movement out of the covered services even for a principal with the role.
- **B:** Incorrect for this question. A policy above the project applies to every current and future network beneath it. Why the correct answer wins: A service perimeter blocks data movement out of the covered services even for a principal with the role.
- **C:** Correct. In this case: A service perimeter blocks data movement out of the covered services even for a principal with the role.
- **D:** Incorrect for this question. Labels attribute spend in billing export; they do not grant or restrict access. Why the correct answer wins: A service perimeter blocks data movement out of the covered services even for a principal with the role.

### Question 44 — A

Answer: Put Identity-Aware Proxy in front of the application. Identity-Aware Proxy authenticates and authorises each request before it reaches the backend. Local study-map skill 3.5 (Secure Remote Access and Zero Trust), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 3 (security and compliance): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Correct. In this case: Identity-Aware Proxy authenticates and authorises each request before it reaches the backend.
- **B:** Incorrect for this question. Cloud NAT lets private instances reach the internet without an external address. Why the correct answer wins: Identity-Aware Proxy authenticates and authorises each request before it reaches the backend.
- **C:** Incorrect for this question. A bastion is still an internet-facing host that must be patched and watched. Why the correct answer wins: Identity-Aware Proxy authenticates and authorises each request before it reaches the backend.
- **D:** Incorrect for this question. Private Google Access reaches Google APIs from an internal address without a proxy or a NAT gateway. Why the correct answer wins: Identity-Aware Proxy authenticates and authorises each request before it reaches the backend.

### Question 45 — D

Answer: Require Binary Authorization attestations. The admission controller rejects images without a valid attestation, so an unverified build cannot start. Only images with a valid attestation from a trusted builder may deploy. Local study-map skill 3.6 (Software Supply Chain Security), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 3 (security and compliance): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. Scanning reports known vulnerabilities in the image layers before deployment. Why the correct answer wins: The admission controller rejects images without a valid attestation, so an unverified build cannot start.
- **B:** Incorrect for this question. Artifact Registry holds the image with IAM-scoped access and vulnerability metadata. Why the correct answer wins: The admission controller rejects images without a valid attestation, so an unverified build cannot start.
- **C:** Incorrect for this question. Network policy restricts pod-to-pod traffic inside the cluster, which a firewall rule cannot see. Why the correct answer wins: The admission controller rejects images without a valid attestation, so an unverified build cannot start.
- **D:** Correct. Only images with a valid attestation from a trusted builder may deploy. In this case: The admission controller rejects images without a valid attestation, so an unverified build cannot start.

### Question 46 — D

Answer: Screen prompts and responses with Model Armor. Model Armor detects prompt injection and unsafe content before and after the model call. Local study-map skill 3.7 (Securing AI Workloads), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 3 (security and compliance): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. The access level adds device and network conditions to the perimeter rule. Why the correct answer wins: Model Armor detects prompt injection and unsafe content before and after the model call.
- **B:** Incorrect for this question. Sensitive Data Protection finds and redacts, tokenizes, or format-preservingly encrypts sensitive fields. Why the correct answer wins: Model Armor detects prompt injection and unsafe content before and after the model call.
- **C:** Incorrect for this question. Security Command Center aggregates misconfiguration and threat findings across the organization. Why the correct answer wins: Model Armor detects prompt injection and unsafe content before and after the model call.
- **D:** Correct. In this case: Model Armor detects prompt injection and unsafe content before and after the model call.

### Question 47 — D

Answer: Enable Data Access audit logs. Data Access logging is off by default and must be enabled before reads and writes are recorded. Local study-map skill 3.8 (Compliance, Residency, and Audit Logging), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 3 (security and compliance): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. The metric turns a log pattern into a series that can be alerted on and charted. Why the correct answer wins: Data Access logging is off by default and must be enabled before reads and writes are recorded.
- **B:** Incorrect for this question. Admin Activity records configuration changes and cannot be disabled. Why the correct answer wins: Data Access logging is off by default and must be enabled before reads and writes are recorded.
- **C:** Incorrect for this question. Access Transparency records when Google staff access your content, which is evidence of oversight, not of user activity. Why the correct answer wins: Data Access logging is off by default and must be enabled before reads and writes are recorded.
- **D:** Correct. In this case: Data Access logging is off by default and must be enabled before reads and writes are recorded.

### Question 48 — D

Answer: Route the logs with an aggregated sink. An aggregated sink collects logs from every project into one destination. Local study-map skill 3.8 (Compliance, Residency, and Audit Logging), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 3 (security and compliance): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. The dashboard gives the team one view of the same signals during an incident. Why the correct answer wins: An aggregated sink collects logs from every project into one destination.
- **B:** Incorrect for this question. The runbook records the diagnostic steps so the response does not depend on who is awake. Why the correct answer wins: An aggregated sink collects logs from every project into one destination.
- **C:** Incorrect for this question. The metric turns a log pattern into a series that can be alerted on and charted. Why the correct answer wins: An aggregated sink collects logs from every project into one destination.
- **D:** Correct. In this case: An aggregated sink collects logs from every project into one destination.

### Question 49 — B

Answer: Enable data access audit logs for the services in scope → create a locked log bucket with the required retention → route the logs with an aggregated sink → query and export the evidence for the auditor. Logs must be enabled before they can be routed, and retention is fixed on the bucket before the sink writes to it. Local study-map skill 3.8 (Compliance, Residency, and Audit Logging), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 3 (security and compliance): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. A sink that is created last is needed before any evidence can be queried from the destination. Why the correct answer wins: Logs must be enabled before they can be routed, and retention is fixed on the bucket before the sink writes to it.
- **B:** Correct. In this case: Logs must be enabled before they can be routed, and retention is fixed on the bucket before the sink writes to it.
- **C:** Incorrect for this question. There is no evidence to query before logging and routing exist. Why the correct answer wins: Logs must be enabled before they can be routed, and retention is fixed on the bucket before the sink writes to it.
- **D:** Incorrect for this question. A sink without a destination bucket or enabled logs captures nothing. Why the correct answer wins: Logs must be enabled before they can be routed, and retention is fixed on the bucket before the sink writes to it.

### Question 50 — A

Answer: Require a reviewed pull request and a passing plan. The gate makes a second person check the change and its plan before it can apply. Local study-map skill 4.1 (SDLC and CI/CD Design), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 4 (analyzing and optimizing): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Correct. In this case: The gate makes a second person check the change and its plan before it can apply.
- **B:** Incorrect for this question. A rolling replacement keeps capacity but exposes the whole fleet before the signal is trusted. Why the correct answer wins: The gate makes a second person check the change and its plan before it can apply.
- **C:** Incorrect for this question. Short branches reduce merge conflict and keep the mainline deployable. Why the correct answer wins: The gate makes a second person check the change and its plan before it can apply.
- **D:** Incorrect for this question. A rebuild produces a different artifact, so the test result no longer applies to production. Why the correct answer wins: The gate makes a second person check the change and its plan before it can apply.

### Question 51 — A

Answer: Adopt trunk-based development with short-lived branches. Short-lived branches reduce merge conflict and keep the mainline deployable. Local study-map skill 4.1 (SDLC and CI/CD Design), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 4 (analyzing and optimizing): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Correct. In this case: Short-lived branches reduce merge conflict and keep the mainline deployable.
- **B:** Incorrect for this question. A rebuild produces a different artifact, so the test result no longer applies to production. Why the correct answer wins: Short-lived branches reduce merge conflict and keep the mainline deployable.
- **C:** Incorrect for this question. A rolling replacement keeps capacity but exposes the whole fleet before the signal is trusted. Why the correct answer wins: Short-lived branches reduce merge conflict and keep the mainline deployable.
- **D:** Incorrect for this question. The flag separates deployment from release, so the code can ship dark and be turned off instantly. Why the correct answer wins: Short-lived branches reduce merge conflict and keep the mainline deployable.

### Question 52 — A

Answer: Query the entries in Cloud Logging. Logging holds the event text and structured fields that explain what happened at that moment. Local study-map skill 4.2 (Root Cause Analysis), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 4 (analyzing and optimizing): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Correct. In this case: Logging holds the event text and structured fields that explain what happened at that moment.
- **B:** Incorrect for this question. Trace shows how one request spent its time across services and calls. Why the correct answer wins: Logging holds the event text and structured fields that explain what happened at that moment.
- **C:** Incorrect for this question. The dashboard gives the team one view of the same signals during an incident. Why the correct answer wins: Logging holds the event text and structured fields that explain what happened at that moment.
- **D:** Incorrect for this question. Recommender reports idle and over-provisioned resources with the estimated saving. Why the correct answer wins: Logging holds the event text and structured fields that explain what happened at that moment.

### Question 53 — A, B

Answers: Inspect the trace waterfall in Cloud Trace; Group the exceptions in Error Reporting. Trace shows how one request spent its time, and Error Reporting clusters the recurring stack traces. Trace shows how one request spent its time across services and calls. Error Reporting clusters recurring stack traces so a new failure is not lost in the log volume. Local study-map skill 4.2 (Root Cause Analysis), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 4 (analyzing and optimizing): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Correct. Error Reporting clusters recurring stack traces so a new failure is not lost in the log volume. In this case: Trace shows how one request spent its time, and Error Reporting clusters the recurring stack traces.
- **B:** Correct. Trace shows how one request spent its time across services and calls. In this case: Trace shows how one request spent its time, and Error Reporting clusters the recurring stack traces.
- **C:** Incorrect for this question. An SLO ties the alert to the promise the users care about rather than to a raw resource threshold. Why the correct answer wins: Trace shows how one request spent its time, and Error Reporting clusters the recurring stack traces.
- **D:** Incorrect for this question. The runbook records the diagnostic steps so the response does not depend on who is awake. Why the correct answer wins: Trace shows how one request spent its time, and Error Reporting clusters the recurring stack traces.
- **E:** Incorrect for this question. The dashboard gives the team one view of the same signals during an incident. Why the correct answer wins: Trace shows how one request spent its time, and Error Reporting clusters the recurring stack traces.

### Question 54 — D

Answer: Run a load test at the expected peak. The load test measures the system at the concurrency the business expects, before the peak. Local study-map skill 4.3 (Testing and Validation), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 4 (analyzing and optimizing): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. An independent test attempts the attack the design claims to prevent. Why the correct answer wins: The load test measures the system at the concurrency the business expects, before the peak.
- **B:** Incorrect for this question. The experiment proves the failover path works while the impact is controlled. Why the correct answer wins: The load test measures the system at the concurrency the business expects, before the peak.
- **C:** Incorrect for this question. The pyramid puts volume where it is cheap and keeps end-to-end tests for the critical paths. Why the correct answer wins: The load test measures the system at the concurrency the business expects, before the peak.
- **D:** Correct. In this case: The load test measures the system at the concurrency the business expects, before the peak.

### Question 55 — C

Answer: Run a warm standby at reduced capacity. A running but smaller copy recovers in a short window at a continuous cost. Local study-map skill 4.4 (Disaster Recovery and Business Continuity), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 4 (analyzing and optimizing): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. Only the core data and configuration stay warm, so recovery starts the compute and takes minutes. Why the correct answer wins: A running but smaller copy recovers in a short window at a continuous cost.
- **B:** Incorrect for this question. Restoring from backup is the cheapest option and the slowest to recover. Why the correct answer wins: A running but smaller copy recovers in a short window at a continuous cost.
- **C:** Correct. In this case: A running but smaller copy recovers in a short window at a continuous cost.
- **D:** Incorrect for this question. Both regions serve traffic, so a regional loss is absorbed without a failover decision. Why the correct answer wins: A running but smaller copy recovers in a short window at a continuous cost.

### Question 56 — A

Answer: Act on the Recommender suggestions. Recommender reports idle and over-provisioned resources with the estimated saving for each. Local study-map skill 4.5 (Cost Optimization), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 4 (analyzing and optimizing): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Correct. In this case: Recommender reports idle and over-provisioned resources with the estimated saving for each.
- **B:** Incorrect for this question. A budget alerts on spend but does not stop it. Why the correct answer wins: Recommender reports idle and over-provisioned resources with the estimated saving for each.
- **C:** Incorrect for this question. The export attributes cost to the team and service that caused it. Why the correct answer wins: Recommender reports idle and over-provisioned resources with the estimated saving for each.
- **D:** Incorrect for this question. Labels attribute spend in billing export; they do not grant or restrict access. Why the correct answer wins: Recommender reports idle and over-provisioned resources with the estimated saving for each.

### Question 57 — A, D

Answers: Export billing to BigQuery and review it per label; Assign a cost owner to each business unit. The export attributes spend to labels, and a named owner is what makes the report change behaviour. The export attributes cost to the team and service that caused it. A named owner per unit is what makes a cost report change behaviour. Local study-map skill 4.5 (Cost Optimization), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 4 (analyzing and optimizing): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Correct. The export attributes cost to the team and service that caused it. In this case: The export attributes spend to labels, and a named owner is what makes the report change behaviour.
- **B:** Incorrect for this question. Showing owners their own spend changes behaviour more reliably than a central report. Why the correct answer wins: The export attributes spend to labels, and a named owner is what makes the report change behaviour.
- **C:** Incorrect for this question. Labels attribute spend in billing export; they do not grant or restrict access. Why the correct answer wins: The export attributes spend to labels, and a named owner is what makes the report change behaviour.
- **D:** Correct. A named owner per unit is what makes a cost report change behaviour. In this case: The export attributes spend to labels, and a named owner is what makes the report change behaviour.
- **E:** Incorrect for this question. A budget alerts on spend but does not stop it. Why the correct answer wins: The export attributes spend to labels, and a named owner is what makes the report change behaviour.

### Question 58 — B

Answer: Inspect the query plan and bytes processed → partition and cluster the table on the filter columns → rewrite the query to prune partitions → measure the new slot time and bytes scanned. The plan identifies the problem, the physical design supports pruning, and only a measurement proves improvement. Local study-map skill 4.5 (Cost Optimization), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 4 (analyzing and optimizing): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. Partitioning last ignores what the plan and the rewrite revealed. Why the correct answer wins: The plan identifies the problem, the physical design supports pruning, and only a measurement proves improvement.
- **B:** Correct. In this case: The plan identifies the problem, the physical design supports pruning, and only a measurement proves improvement.
- **C:** Incorrect for this question. The plan is the evidence that drives both the rewrite and the physical design. Why the correct answer wins: The plan identifies the problem, the physical design supports pruning, and only a measurement proves improvement.
- **D:** Incorrect for this question. Measuring before any change establishes no baseline against the plan. Why the correct answer wins: The plan identifies the problem, the physical design supports pruning, and only a measurement proves improvement.

### Question 59 — D

Answer: Agree the decision rights with the stakeholders. Naming who decides each trade-off prevents the design being reopened late in delivery. Local study-map skill 4.6 (Stakeholder and Change Management), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 4 (analyzing and optimizing): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. A catalog entry gives teams a pre-approved, policy-compliant way to request the resource. Why the correct answer wins: Naming who decides each trade-off prevents the design being reopened late in delivery.
- **B:** Incorrect for this question. The board reviews risk and timing for changes that affect regulated or shared systems. Why the correct answer wins: Naming who decides each trade-off prevents the design being reopened late in delivery.
- **C:** Incorrect for this question. The runbook records the diagnostic steps so the response does not depend on who is awake. Why the correct answer wins: Naming who decides each trade-off prevents the design being reopened late in delivery.
- **D:** Correct. In this case: Naming who decides each trade-off prevents the design being reopened late in delivery.

### Question 60 — B

Answer: Publish a service catalog entry with an approved template. A catalog entry gives teams a pre-approved, policy-compliant way to request the resource. Local study-map skill 4.7 (Service Catalog and Provisioning), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 4 (analyzing and optimizing): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. Labels attribute spend in billing export; they do not grant or restrict access. Why the correct answer wins: A catalog entry gives teams a pre-approved, policy-compliant way to request the resource.
- **B:** Correct. In this case: A catalog entry gives teams a pre-approved, policy-compliant way to request the resource.
- **C:** Incorrect for this question. An organization policy blocks the action across every project regardless of who holds the role. Why the correct answer wins: A catalog entry gives teams a pre-approved, policy-compliant way to request the resource.
- **D:** Incorrect for this question. Terraform holds desired state in code, plans the diff, and applies it through a provider. Why the correct answer wins: A catalog entry gives teams a pre-approved, policy-compliant way to request the resource.

### Question 61 — C

Answer: Roll out a canary to a small share of traffic. A canary limits the blast radius while the error and latency signals are compared. Local study-map skill 5.1 (Deployment and Release Strategy), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 5 (managing implementation): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. Two identical environments let the switch be reversed instantly if the new one misbehaves. Why the correct answer wins: A canary limits the blast radius while the error and latency signals are compared.
- **B:** Incorrect for this question. The flag separates deployment from release, so the code can ship dark and be turned off instantly. Why the correct answer wins: A canary limits the blast radius while the error and latency signals are compared.
- **C:** Correct. In this case: A canary limits the blast radius while the error and latency signals are compared.
- **D:** Incorrect for this question. A rolling replacement keeps capacity but exposes the whole fleet before the signal is trusted. Why the correct answer wins: A canary limits the blast radius while the error and latency signals are compared.

### Question 62 — A, B

Answers: Deploy blue/green with a traffic switch; Keep the previous image digest ready for rollback. Two environments let the switch be reversed instantly, and a pinned digest restores the exact artifact. Two identical environments let the switch be reversed instantly if the new one misbehaves. A pinned digest restores the exact artifact that was known good, not a rebuild of it. Local study-map skill 5.1 (Deployment and Release Strategy), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 5 (managing implementation): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Correct. A pinned digest restores the exact artifact that was known good, not a rebuild of it. In this case: Two environments let the switch be reversed instantly, and a pinned digest restores the exact artifact.
- **B:** Correct. Two identical environments let the switch be reversed instantly if the new one misbehaves. In this case: Two environments let the switch be reversed instantly, and a pinned digest restores the exact artifact.
- **C:** Incorrect for this question. Promotion moves one immutable artifact forward, so what was tested is what runs. Why the correct answer wins: Two environments let the switch be reversed instantly, and a pinned digest restores the exact artifact.
- **D:** Incorrect for this question. A budget alerts on spend but does not stop it. Why the correct answer wins: Two environments let the switch be reversed instantly, and a pinned digest restores the exact artifact.
- **E:** Incorrect for this question. A rebuild produces a different artifact, so the test result no longer applies to production. Why the correct answer wins: Two environments let the switch be reversed instantly, and a pinned digest restores the exact artifact.

### Question 63 — B

Answer: Build an immutable image and record its digest → deploy the new revision without traffic → shift a small traffic percentage and watch error and latency signals → promote to full traffic or roll back to the pinned digest. The artifact is fixed before traffic moves, and the decision to promote follows observed signals. Local study-map skill 5.1 (Deployment and Release Strategy), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 5 (managing implementation): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. Full traffic before any canary step turns the first failure into an outage. Why the correct answer wins: The artifact is fixed before traffic moves, and the decision to promote follows observed signals.
- **B:** Correct. In this case: The artifact is fixed before traffic moves, and the decision to promote follows observed signals.
- **C:** Incorrect for this question. Nothing can be watched before the revision exists, and the image precedes the deployment. Why the correct answer wins: The artifact is fixed before traffic moves, and the decision to promote follows observed signals.
- **D:** Incorrect for this question. Promoting before the canary step skips the signal that justifies promotion. Why the correct answer wins: The artifact is fixed before traffic moves, and the decision to promote follows observed signals.

### Question 64 — D

Answer: Publish the API through Apigee. Apigee adds quotas, keys, mediation, and analytics at the gateway for each consumer. Local study-map skill 5.2 (API Management), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 5 (managing implementation): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. API Gateway fronts a Cloud Run or functions backend with a managed OpenAPI definition. Why the correct answer wins: Apigee adds quotas, keys, mediation, and analytics at the gateway for each consumer.
- **B:** Incorrect for this question. Endpoints validates and monitors an API described by an OpenAPI or gRPC spec. Why the correct answer wins: Apigee adds quotas, keys, mediation, and analytics at the gateway for each consumer.
- **C:** Incorrect for this question. Cloud Armor filters requests at the edge with allow and deny rules and adaptive protection. Why the correct answer wins: Apigee adds quotas, keys, mediation, and analytics at the gateway for each consumer.
- **D:** Correct. In this case: Apigee adds quotas, keys, mediation, and analytics at the gateway for each consumer.

### Question 65 — D

Answer: Use API Gateway. API Gateway fronts a Cloud Run or functions backend with a managed OpenAPI definition. Local study-map skill 5.2 (API Management), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 5 (managing implementation): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. Endpoints validates and monitors an API described by an OpenAPI or gRPC spec. Why the correct answer wins: API Gateway fronts a Cloud Run or functions backend with a managed OpenAPI definition.
- **B:** Incorrect for this question. Cloud Armor filters requests at the edge with allow and deny rules and adaptive protection. Why the correct answer wins: API Gateway fronts a Cloud Run or functions backend with a managed OpenAPI definition.
- **C:** Incorrect for this question. Apigee adds quotas, keys, mediation, and analytics at the gateway. Why the correct answer wins: API Gateway fronts a Cloud Run or functions backend with a managed OpenAPI definition.
- **D:** Correct. In this case: API Gateway fronts a Cloud Run or functions backend with a managed OpenAPI definition.

### Question 66 — B

Answer: Migrate the database with Database Migration Service. The service replicates continuously and cuts over in a short window with the source still running. Local study-map skill 5.3 (Data and System Migration Tooling), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 5 (managing implementation): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. The service moves object data between buckets or clouds on a schedule. Why the correct answer wins: The service replicates continuously and cuts over in a short window with the source still running.
- **B:** Correct. In this case: The service replicates continuously and cuts over in a short window with the source still running.
- **C:** Incorrect for this question. Datastream reads the source log and streams inserts, updates, and deletes with ordering preserved. Why the correct answer wins: The service replicates continuously and cuts over in a short window with the source still running.
- **D:** Incorrect for this question. The service runs scheduled loads from SaaS sources and other clouds into BigQuery. Why the correct answer wins: The service replicates continuously and cuts over in a short window with the source still running.

### Question 67 — B

Answer: Convert the VMs with Migrate to Containers. The tool rewrites a VM workload into a container image so it can run on GKE. Local study-map skill 5.3 (Data and System Migration Tooling), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 5 (managing implementation): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. Migration Center inventories the servers and estimates the target size and cost. Why the correct answer wins: The tool rewrites a VM workload into a container image so it can run on GKE.
- **B:** Correct. In this case: The tool rewrites a VM workload into a container image so it can run on GKE.
- **C:** Incorrect for this question. The service moves object data between buckets or clouds on a schedule. Why the correct answer wins: The tool rewrites a VM workload into a container image so it can run on GKE.
- **D:** Incorrect for this question. VMware Engine keeps the existing hypervisor and operations model while moving the hardware into Google Cloud. Why the correct answer wins: The tool rewrites a VM workload into a container image so it can run on GKE.

### Question 68 — D

Answer: Inventory the estate in Migration Center → group servers into dependency-based waves → validate a pilot wave in the target landing zone → cut over wave by wave and decommission the source. Inventory precedes grouping, a pilot proves the landing zone, and decommissioning follows a completed cutover. Local study-map skill 5.3 (Data and System Migration Tooling), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 5 (managing implementation): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. Decommissioning first removes the evidence and the rollback option for every later step. Why the correct answer wins: Inventory precedes grouping, a pilot proves the landing zone, and decommissioning follows a completed cutover.
- **B:** Incorrect for this question. Waves cannot be grouped before the inventory, and decommissioning before validation destroys the rollback path. Why the correct answer wins: Inventory precedes grouping, a pilot proves the landing zone, and decommissioning follows a completed cutover.
- **C:** Incorrect for this question. A pilot cannot be chosen before the inventory and the wave grouping. Why the correct answer wins: Inventory precedes grouping, a pilot proves the landing zone, and decommissioning follows a completed cutover.
- **D:** Correct. In this case: Inventory precedes grouping, a pilot proves the landing zone, and decommissioning follows a completed cutover.

### Question 69 — A

Answer: Run the emulator in the pipeline. The emulator provides a local endpoint for tests without a billable cloud resource. Local study-map skill 5.4 (Programmatic Access and Emulators), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 5 (managing implementation): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Correct. In this case: The emulator provides a local endpoint for tests without a billable cloud resource.
- **B:** Incorrect for this question. Terraform holds desired state in code, plans the diff, and applies it through a provider. Why the correct answer wins: The emulator provides a local endpoint for tests without a billable cloud resource.
- **C:** Incorrect for this question. Cloud Build executes the pipeline steps in a managed, isolated worker with recorded provenance. Why the correct answer wins: The emulator provides a local endpoint for tests without a billable cloud resource.
- **D:** Incorrect for this question. The CLI exposes every API as a command that can be scripted and logged. Why the correct answer wins: The emulator provides a local endpoint for tests without a billable cloud resource.

### Question 70 — A

Answer: Automate the step with the gcloud CLI. The CLI exposes the API as commands that can be scripted and captured in a log. The CLI exposes every API as a command that can be scripted and logged. Local study-map skill 5.4 (Programmatic Access and Emulators), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 5 (managing implementation): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Correct. The CLI exposes every API as a command that can be scripted and logged. In this case: The CLI exposes the API as commands that can be scripted and captured in a log.
- **B:** Incorrect for this question. The bq tool runs jobs and manages datasets from a terminal or a script. Why the correct answer wins: The CLI exposes the API as commands that can be scripted and captured in a log.
- **C:** Incorrect for this question. Cloud Shell provides an authenticated terminal and editor with no local installation. Why the correct answer wins: The CLI exposes the API as commands that can be scripted and captured in a log.
- **D:** Incorrect for this question. Cloud Code gives the editor run, debug, and deploy targets for the cluster without leaving it. Why the correct answer wins: The CLI exposes the API as commands that can be scripted and captured in a log.

### Question 71 — B

Answer: Use the Google API client library with retries. The client library applies the recommended retry and backoff behaviour for the API. Local study-map skill 5.5 (Client Libraries and API Practices), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 5 (managing implementation): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. Impersonation issues a short-lived token so the test runs as the real workload identity. Why the correct answer wins: The client library applies the recommended retry and backoff behaviour for the API.
- **B:** Correct. In this case: The client library applies the recommended retry and backoff behaviour for the API.
- **C:** Incorrect for this question. An API key identifies a project and does not authorise a user, so it cannot express least privilege. Why the correct answer wins: The client library applies the recommended retry and backoff behaviour for the API.
- **D:** Incorrect for this question. The CLI exposes every API as a command that can be scripted and logged. Why the correct answer wins: The client library applies the recommended retry and backoff behaviour for the API.

### Question 72 — A

Answer: Install the Ops Agent on the instances. The Ops Agent ships host metrics and application logs to Monitoring and Logging. Local study-map skill 6.1 (Observability Design), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 6 (solution and operations excellence): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Correct. In this case: The Ops Agent ships host metrics and application logs to Monitoring and Logging.
- **B:** Incorrect for this question. Profiler samples the running code and attributes CPU and heap to the functions responsible. Why the correct answer wins: The Ops Agent ships host metrics and application logs to Monitoring and Logging.
- **C:** Incorrect for this question. Error Reporting clusters recurring stack traces so a new failure is not lost in the log volume. Why the correct answer wins: The Ops Agent ships host metrics and application logs to Monitoring and Logging.
- **D:** Incorrect for this question. Trace shows how one request spent its time across services and calls. Why the correct answer wins: The Ops Agent ships host metrics and application logs to Monitoring and Logging.

### Question 73 — B

Answer: Attach Cloud Profiler to the service. Profiler samples the running code and attributes CPU and heap to the functions responsible. Local study-map skill 6.1 (Observability Design), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 6 (solution and operations excellence): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. Error Reporting clusters recurring stack traces so a new failure is not lost in the log volume. Why the correct answer wins: Profiler samples the running code and attributes CPU and heap to the functions responsible.
- **B:** Correct. In this case: Profiler samples the running code and attributes CPU and heap to the functions responsible.
- **C:** Incorrect for this question. The check measures availability from outside, which no internal metric can prove. Why the correct answer wins: Profiler samples the running code and attributes CPU and heap to the functions responsible.
- **D:** Incorrect for this question. Trace shows how one request spent its time across services and calls. Why the correct answer wins: Profiler samples the running code and attributes CPU and heap to the functions responsible.

### Question 74 — B

Answer: Define an SLO with an error budget. An SLO ties the alert to the user promise rather than to a raw resource threshold. Local study-map skill 6.2 (Alerting and Service Level Objectives), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 6 (solution and operations excellence): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. The policy fires when the series crosses the condition for the stated duration. Why the correct answer wins: An SLO ties the alert to the user promise rather than to a raw resource threshold.
- **B:** Correct. In this case: An SLO ties the alert to the user promise rather than to a raw resource threshold.
- **C:** Incorrect for this question. The check measures availability from outside, which no internal metric can prove. Why the correct answer wins: An SLO ties the alert to the user promise rather than to a raw resource threshold.
- **D:** Incorrect for this question. The dashboard gives the team one view of the same signals during an incident. Why the correct answer wins: An SLO ties the alert to the user promise rather than to a raw resource threshold.

### Question 75 — A, E

Answers: Create an alerting policy on the metric; Create a log-based metric. The metric turns the log pattern into a series, and the policy fires when it crosses the condition. The policy fires when the series crosses the condition for the stated duration. The metric turns a log pattern into a series that can be alerted on and charted. Local study-map skill 6.2 (Alerting and Service Level Objectives), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 6 (solution and operations excellence): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Correct. The policy fires when the series crosses the condition for the stated duration. In this case: The metric turns the log pattern into a series, and the policy fires when it crosses the condition.
- **B:** Incorrect for this question. An SLO ties the alert to the promise the users care about rather than to a raw resource threshold. Why the correct answer wins: The metric turns the log pattern into a series, and the policy fires when it crosses the condition.
- **C:** Incorrect for this question. The dashboard gives the team one view of the same signals during an incident. Why the correct answer wins: The metric turns the log pattern into a series, and the policy fires when it crosses the condition.
- **D:** Incorrect for this question. Recommender reports idle and over-provisioned resources with the estimated saving. Why the correct answer wins: The metric turns the log pattern into a series, and the policy fires when it crosses the condition.
- **E:** Correct. The metric turns a log pattern into a series that can be alerted on and charted. In this case: The metric turns the log pattern into a series, and the policy fires when it crosses the condition.

### Question 76 — C

Answer: Publish a runbook per alert. The runbook records the diagnostic steps so the response does not depend on who is awake. Local study-map skill 6.3 (Release Management and Support), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 6 (solution and operations excellence): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. A named rotation turns an alert into a person who is already accountable for it. Why the correct answer wins: The runbook records the diagnostic steps so the response does not depend on who is awake.
- **B:** Incorrect for this question. The support tier sets the response time and the escalation path the business expects. Why the correct answer wins: The runbook records the diagnostic steps so the response does not depend on who is awake.
- **C:** Correct. In this case: The runbook records the diagnostic steps so the response does not depend on who is awake.
- **D:** Incorrect for this question. The dashboard gives the team one view of the same signals during an incident. Why the correct answer wins: The runbook records the diagnostic steps so the response does not depend on who is awake.

### Question 77 — B

Answer: Match the support plan to the recovery commitment. The support tier sets the response time and the escalation path the business expects. Local study-map skill 6.3 (Release Management and Support), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 6 (solution and operations excellence): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. The runbook records the diagnostic steps so the response does not depend on who is awake. Why the correct answer wins: The support tier sets the response time and the escalation path the business expects.
- **B:** Correct. In this case: The support tier sets the response time and the escalation path the business expects.
- **C:** Incorrect for this question. The contract converts an internal target into an obligation with a consequence. Why the correct answer wins: The support tier sets the response time and the escalation path the business expects.
- **D:** Incorrect for this question. A named rotation turns an alert into a person who is already accountable for it. Why the correct answer wins: The support tier sets the response time and the escalation path the business expects.

### Question 78 — D

Answer: Run a chaos experiment against a zone. The experiment proves the failover path works while the impact is controlled. Local study-map skill 6.4 (Reliability Testing), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 6 (solution and operations excellence): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. A canary limits the blast radius while the error and latency signals are compared. Why the correct answer wins: The experiment proves the failover path works while the impact is controlled.
- **B:** Incorrect for this question. The load test measures the system at the concurrency the business expects, before launch. Why the correct answer wins: The experiment proves the failover path works while the impact is controlled.
- **C:** Incorrect for this question. An independent test attempts the attack the design claims to prevent. Why the correct answer wins: The experiment proves the failover path works while the impact is controlled.
- **D:** Correct. In this case: The experiment proves the failover path works while the impact is controlled.

### Question 79 — A

Answer: Write a blameless postmortem with actions. The postmortem records cause and follow-up work, which is how the same failure is prevented. Local study-map skill 6.5 (Operational Excellence and Quality Control), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 6 (solution and operations excellence): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Correct. In this case: The postmortem records cause and follow-up work, which is how the same failure is prevented.
- **B:** Incorrect for this question. The support tier sets the response time and the escalation path the business expects. Why the correct answer wins: The postmortem records cause and follow-up work, which is how the same failure is prevented.
- **C:** Incorrect for this question. The runbook records the diagnostic steps so the response does not depend on who is awake. Why the correct answer wins: The postmortem records cause and follow-up work, which is how the same failure is prevented.
- **D:** Incorrect for this question. The dashboard gives the team one view of the same signals during an incident. Why the correct answer wins: The postmortem records cause and follow-up work, which is how the same failure is prevented.

### Question 80 — B

Answer: Detect the symptom through an alert → contain the impact and restore service → isolate the root cause from logs, traces, and metrics → apply the permanent fix and write the postmortem. Service recovery comes before deep analysis, and the postmortem follows the fix. Local study-map skill 6.5 (Operational Excellence and Quality Control), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 6 (solution and operations excellence): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. Detection precedes analysis, and the postmortem follows restoration rather than preceding it. Why the correct answer wins: Service recovery comes before deep analysis, and the postmortem follows the fix.
- **B:** Correct. In this case: Service recovery comes before deep analysis, and the postmortem follows the fix.
- **C:** Incorrect for this question. Service cannot be restored before the alert fires, and the root cause is isolated before the postmortem. Why the correct answer wins: Service recovery comes before deep analysis, and the postmortem follows the fix.
- **D:** Incorrect for this question. A postmortem cannot be written before the incident has happened and been resolved. Why the correct answer wins: Service recovery comes before deep analysis, and the postmortem follows the fix.

### Question 81 — D

Answer: Define an SLO with an error budget. An SLO ties the alert to the user promise rather than to a raw resource threshold. Local study-map skill 6.2 (Alerting and Service Level Objectives), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 6 (solution and operations excellence): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. The check measures availability from outside, which no internal metric can prove. Why the correct answer wins: An SLO ties the alert to the user promise rather than to a raw resource threshold.
- **B:** Incorrect for this question. The dashboard gives the team one view of the same signals during an incident. Why the correct answer wins: An SLO ties the alert to the user promise rather than to a raw resource threshold.
- **C:** Incorrect for this question. The policy fires when the series crosses the condition for the stated duration. Why the correct answer wins: An SLO ties the alert to the user promise rather than to a raw resource threshold.
- **D:** Correct. In this case: An SLO ties the alert to the user promise rather than to a raw resource threshold.

### Question 82 — C

Answer: Document the exit plan and data portability. An exit plan and data portability keep the migration reversible and bound how proprietary the design may become. The exit plan keeps the migration reversible and constrains how proprietary the design may become. Local study-map skill 1.2 (Non-Functional Requirements and Trade-offs), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 1 (designing and planning): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. Labels attribute spend in billing export; they do not grant or restrict access. Why the correct answer wins: An exit plan and data portability keep the migration reversible and bound how proprietary the design may become.
- **B:** Incorrect for this question. The model compares run cost, people cost, and exit cost rather than the monthly bill alone. Why the correct answer wins: An exit plan and data portability keep the migration reversible and bound how proprietary the design may become.
- **C:** Correct. The exit plan keeps the migration reversible and constrains how proprietary the design may become. In this case: An exit plan and data portability keep the migration reversible and bound how proprietary the design may become.
- **D:** Incorrect for this question. A budget alerts on spend but does not stop it. Why the correct answer wins: An exit plan and data portability keep the migration reversible and bound how proprietary the design may become.

### Question 83 — C

Answer: Require a reviewed pull request and a passing plan. The gate makes a second person check the change and its plan before it can apply. Local study-map skill 4.1 (SDLC and CI/CD Design), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 4 (analyzing and optimizing): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. A rolling replacement keeps capacity but exposes the whole fleet before the signal is trusted. Why the correct answer wins: The gate makes a second person check the change and its plan before it can apply.
- **B:** Incorrect for this question. Short branches reduce merge conflict and keep the mainline deployable. Why the correct answer wins: The gate makes a second person check the change and its plan before it can apply.
- **C:** Correct. In this case: The gate makes a second person check the change and its plan before it can apply.
- **D:** Incorrect for this question. A rebuild produces a different artifact, so the test result no longer applies to production. Why the correct answer wins: The gate makes a second person check the change and its plan before it can apply.

### Question 84 — A

Answer: Put the projects inside a VPC Service Controls perimeter. A service perimeter blocks data movement out of the covered services even for a principal with the role. Local study-map skill 3.4 (VPC Service Controls and Network Security), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 3 (security and compliance): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Correct. In this case: A service perimeter blocks data movement out of the covered services even for a principal with the role.
- **B:** Incorrect for this question. Labels attribute spend in billing export; they do not grant or restrict access. Why the correct answer wins: A service perimeter blocks data movement out of the covered services even for a principal with the role.
- **C:** Incorrect for this question. A policy above the project applies to every current and future network beneath it. Why the correct answer wins: A service perimeter blocks data movement out of the covered services even for a principal with the role.
- **D:** Incorrect for this question. A deny policy overrides every allow beneath it, which is how an exception is made impossible. Why the correct answer wins: A service perimeter blocks data movement out of the covered services even for a principal with the role.

### Question 85 — D

Answer: Apply a bucket retention policy with a locked period. A locked retention policy prevents deletion or a shorter period, which is the evidence an auditor tests. Local study-map skill 2.2 (Storage Configuration and Lifecycle), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 2 (managing and provisioning): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. A lifecycle rule acts on object age or class, so retention stops depending on a person. Why the correct answer wins: A locked retention policy prevents deletion or a shorter period, which is the evidence an auditor tests.
- **B:** Incorrect for this question. Autoclass moves each object between classes as its access pattern changes, with no lifecycle rules to maintain. Why the correct answer wins: A locked retention policy prevents deletion or a shorter period, which is the evidence an auditor tests.
- **C:** Incorrect for this question. Versioning keeps a noncurrent copy when an object is overwritten or deleted. Why the correct answer wins: A locked retention policy prevents deletion or a shorter period, which is the evidence an auditor tests.
- **D:** Correct. In this case: A locked retention policy prevents deletion or a shorter period, which is the evidence an auditor tests.

### Question 86 — C

Answer: Define dashboards and metrics in Cloud Monitoring. Monitoring collects the platform metrics that the first alert will use. Local study-map skill 6.1 (Observability Design), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 6 (solution and operations excellence): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. Trace shows how one request spent its time across services and calls. Why the correct answer wins: Monitoring collects the platform metrics that the first alert will use.
- **B:** Incorrect for this question. The dashboard gives the team one view of the same signals during an incident. Why the correct answer wins: Monitoring collects the platform metrics that the first alert will use.
- **C:** Correct. In this case: Monitoring collects the platform metrics that the first alert will use.
- **D:** Incorrect for this question. Recommender reports idle and over-provisioned resources with the estimated saving. Why the correct answer wins: Monitoring collects the platform metrics that the first alert will use.

### Question 87 — B

Answer: Use Dataflow. Streaming Beam applies windowing and allowed lateness so late readings still settle into the correct window. Dataflow runs an Apache Beam pipeline with autoscaling and a single programming model for batch and streaming. Local study-map skill 1.7 (Data Processing and Analytics Selection), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 1 (designing and planning): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. Airflow expresses dependencies between scheduled jobs and retries a failed task without rerunning the rest. Why the correct answer wins: Streaming Beam applies windowing and allowed lateness so late readings still settle into the correct window.
- **B:** Correct. Dataflow runs an Apache Beam pipeline with autoscaling and a single programming model for batch and streaming. In this case: Streaming Beam applies windowing and allowed lateness so late readings still settle into the correct window.
- **C:** Incorrect for this question. A Dataproc cluster runs open-source Spark and Hadoop with jobs that need a persistent cluster. Why the correct answer wins: Streaming Beam applies windowing and allowed lateness so late readings still settle into the correct window.
- **D:** Incorrect for this question. Scheduler fires a job on a cron or App Engine schedule and retries on failure. Why the correct answer wins: Streaming Beam applies windowing and allowed lateness so late readings still settle into the correct window.

### Question 88 — C, E

Answers: Inspect the trace waterfall in Cloud Trace; Group the exceptions in Error Reporting. Trace shows how one request spent its time, and Error Reporting clusters the recurring exceptions. Trace shows how one request spent its time across services and calls. Error Reporting clusters recurring stack traces so a new failure is not lost in the log volume. Local study-map skill 4.2 (Root Cause Analysis), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 4 (analyzing and optimizing): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. The dashboard gives the team one view of the same signals during an incident. Why the correct answer wins: Trace shows how one request spent its time, and Error Reporting clusters the recurring exceptions.
- **B:** Incorrect for this question. The runbook records the diagnostic steps so the response does not depend on who is awake. Why the correct answer wins: Trace shows how one request spent its time, and Error Reporting clusters the recurring exceptions.
- **C:** Correct. Trace shows how one request spent its time across services and calls. In this case: Trace shows how one request spent its time, and Error Reporting clusters the recurring exceptions.
- **D:** Incorrect for this question. An SLO ties the alert to the promise the users care about rather than to a raw resource threshold. Why the correct answer wins: Trace shows how one request spent its time, and Error Reporting clusters the recurring exceptions.
- **E:** Correct. Error Reporting clusters recurring stack traces so a new failure is not lost in the log volume. In this case: Trace shows how one request spent its time, and Error Reporting clusters the recurring exceptions.

### Question 89 — D

Answer: Enable Data Access audit logs. Data Access logging is off by default and must be enabled before reads and writes are recorded. Local study-map skill 3.8 (Compliance, Residency, and Audit Logging), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 3 (security and compliance): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. Admin Activity records configuration changes and cannot be disabled. Why the correct answer wins: Data Access logging is off by default and must be enabled before reads and writes are recorded.
- **B:** Incorrect for this question. The metric turns a log pattern into a series that can be alerted on and charted. Why the correct answer wins: Data Access logging is off by default and must be enabled before reads and writes are recorded.
- **C:** Incorrect for this question. Access Transparency records when Google staff access your content, which is evidence of oversight, not of user activity. Why the correct answer wins: Data Access logging is off by default and must be enabled before reads and writes are recorded.
- **D:** Correct. In this case: Data Access logging is off by default and must be enabled before reads and writes are recorded.

### Question 90 — D

Answer: Partition the table on the date column. Partitioning limits each query to the date ranges it names, so it scans less. Local study-map skill 2.2 (Storage Configuration and Lifecycle), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 2 (managing and provisioning): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. The view stores the aggregate result and refreshes incrementally as base data arrives. Why the correct answer wins: Partitioning limits each query to the date ranges it names, so it scans less.
- **B:** Incorrect for this question. On-demand bills per byte scanned, which is cheap for sparse use and unpredictable at scale. Why the correct answer wins: Partitioning limits each query to the date ranges it names, so it scans less.
- **C:** Incorrect for this question. Clustering sorts within partitions so a filtered query reads fewer blocks. Why the correct answer wins: Partitioning limits each query to the date ranges it names, so it scans less.
- **D:** Correct. In this case: Partitioning limits each query to the date ranges it names, so it scans less.

### Question 91 — B

Answer: Move the steady services to E2 machine types. A cheaper shape for the steady service lowers the bill without committing to peak capacity all year. E2 shapes trade peak performance for a lower price on workloads that do not need it. Local study-map skill 4.5 (Cost Optimization), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 4 (analyzing and optimizing): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. A one- or three-year commitment discounts the capacity that runs constantly, not the peaks. Why the correct answer wins: A cheaper shape for the steady service lowers the bill without committing to peak capacity all year.
- **B:** Correct. E2 shapes trade peak performance for a lower price on workloads that do not need it. In this case: A cheaper shape for the steady service lowers the bill without committing to peak capacity all year.
- **C:** Incorrect for this question. Sole tenancy keeps the physical host dedicated, which matters for licensing or isolation rules. Why the correct answer wins: A cheaper shape for the steady service lowers the bill without committing to peak capacity all year.
- **D:** Incorrect for this question. Spot capacity costs far less but can be reclaimed with 30 seconds of notice. Why the correct answer wins: A cheaper shape for the steady service lowers the bill without committing to peak capacity all year.

### Question 92 — C

Answer: Use GKE Autopilot. Autopilot manages nodes, scaling, and patching, so the team owns only its workloads. Local study-map skill 1.6 (Compute Platform Selection), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 1 (designing and planning): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. Batch schedules containerised jobs onto managed or existing capacity and retires it when done. Why the correct answer wins: Autopilot manages nodes, scaling, and patching, so the team owns only its workloads.
- **B:** Incorrect for this question. Cloud Run runs a stateless container per request and scales to zero when idle. Why the correct answer wins: Autopilot manages nodes, scaling, and patching, so the team owns only its workloads.
- **C:** Correct. In this case: Autopilot manages nodes, scaling, and patching, so the team owns only its workloads.
- **D:** Incorrect for this question. Standard exposes node configuration and patching, which the team must then run itself. Why the correct answer wins: Autopilot manages nodes, scaling, and patching, so the team owns only its workloads.

### Question 93 — A

Answer: Replicate the data to the second region. The data must exist in the second region before any compute there can serve it. Local study-map skill 1.3 (High Availability and Failover Design), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 1 (designing and planning): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Correct. In this case: The data must exist in the second region before any compute there can serve it.
- **B:** Incorrect for this question. Only the core data and configuration stay warm, so recovery starts the compute and takes minutes. Why the correct answer wins: The data must exist in the second region before any compute there can serve it.
- **C:** Incorrect for this question. Restoring from backup is the cheapest option and the slowest to recover. Why the correct answer wins: The data must exist in the second region before any compute there can serve it.
- **D:** Incorrect for this question. CDN caches responses at edge locations, which cuts origin load and latency for repeat reads. Why the correct answer wins: The data must exist in the second region before any compute there can serve it.

### Question 94 — C

Answer: Run a warm standby at reduced capacity. A running but smaller copy recovers in a short window at a continuous cost. Local study-map skill 4.4 (Disaster Recovery and Business Continuity), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 4 (analyzing and optimizing): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. Restoring from backup is the cheapest option and the slowest to recover. Why the correct answer wins: A running but smaller copy recovers in a short window at a continuous cost.
- **B:** Incorrect for this question. Both regions serve traffic, so a regional loss is absorbed without a failover decision. Why the correct answer wins: A running but smaller copy recovers in a short window at a continuous cost.
- **C:** Correct. In this case: A running but smaller copy recovers in a short window at a continuous cost.
- **D:** Incorrect for this question. Only the core data and configuration stay warm, so recovery starts the compute and takes minutes. Why the correct answer wins: A running but smaller copy recovers in a short window at a continuous cost.

### Question 95 — C

Answer: Run a chaos experiment against a zone. The experiment proves the failure path works while the impact is controlled. Local study-map skill 6.4 (Reliability Testing), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 6 (solution and operations excellence): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. An independent test attempts the attack the design claims to prevent. Why the correct answer wins: The experiment proves the failure path works while the impact is controlled.
- **B:** Incorrect for this question. The load test measures the system at the concurrency the business expects, before launch. Why the correct answer wins: The experiment proves the failure path works while the impact is controlled.
- **C:** Correct. In this case: The experiment proves the failure path works while the impact is controlled.
- **D:** Incorrect for this question. A canary limits the blast radius while the error and latency signals are compared. Why the correct answer wins: The experiment proves the failure path works while the impact is controlled.

### Question 96 — B

Answer: Serve features from Agent Platform Feature Store. Feature Store keeps one definition for training and serving, which prevents training-serving skew. Local study-map skill 1.8 (AI and ML Solution Design), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 1 (designing and planning): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. Monitoring compares live traffic against the training baseline and reports skew and drift. Why the correct answer wins: Feature Store keeps one definition for training and serving, which prevents training-serving skew.
- **B:** Correct. In this case: Feature Store keeps one definition for training and serving, which prevents training-serving skew.
- **C:** Incorrect for this question. Pipelines runs each step as a container with lineage and caching, so the run is reproducible. Why the correct answer wins: Feature Store keeps one definition for training and serving, which prevents training-serving skew.
- **D:** Incorrect for this question. An endpoint keeps capacity ready for low-latency per-request predictions. Why the correct answer wins: Feature Store keeps one definition for training and serving, which prevents training-serving skew.

### Question 97 — D

Answer: Screen prompts and responses with Model Armor. Model Armor detects prompt injection and unsafe content before and after the model call. Local study-map skill 3.7 (Securing AI Workloads), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 3 (security and compliance): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. Sensitive Data Protection finds and redacts, tokenizes, or format-preservingly encrypts sensitive fields. Why the correct answer wins: Model Armor detects prompt injection and unsafe content before and after the model call.
- **B:** Incorrect for this question. The access level adds device and network conditions to the perimeter rule. Why the correct answer wins: Model Armor detects prompt injection and unsafe content before and after the model call.
- **C:** Incorrect for this question. Security Command Center aggregates misconfiguration and threat findings across the organization. Why the correct answer wins: Model Armor detects prompt injection and unsafe content before and after the model call.
- **D:** Correct. In this case: Model Armor detects prompt injection and unsafe content before and after the model call.

### Question 98 — D

Answer: Migrate the database with Database Migration Service. The service replicates continuously and cuts over in a short window with the source still running. Local study-map skill 5.3 (Data and System Migration Tooling), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 5 (managing implementation): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. The service runs scheduled loads from SaaS sources and other clouds into BigQuery. Why the correct answer wins: The service replicates continuously and cuts over in a short window with the source still running.
- **B:** Incorrect for this question. Datastream reads the source log and streams inserts, updates, and deletes with ordering preserved. Why the correct answer wins: The service replicates continuously and cuts over in a short window with the source still running.
- **C:** Incorrect for this question. The service moves object data between buckets or clouds on a schedule. Why the correct answer wins: The service replicates continuously and cuts over in a short window with the source still running.
- **D:** Correct. In this case: The service replicates continuously and cuts over in a short window with the source still running.

### Question 99 — C

Answer: Match the support plan to the recovery commitment. The support tier sets the response time and the escalation path the business expects. Local study-map skill 6.3 (Release Management and Support), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 6 (solution and operations excellence): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. The runbook records the diagnostic steps so the response does not depend on who is awake. Why the correct answer wins: The support tier sets the response time and the escalation path the business expects.
- **B:** Incorrect for this question. A named rotation turns an alert into a person who is already accountable for it. Why the correct answer wins: The support tier sets the response time and the escalation path the business expects.
- **C:** Correct. In this case: The support tier sets the response time and the escalation path the business expects.
- **D:** Incorrect for this question. The contract converts an internal target into an obligation with a consequence. Why the correct answer wins: The support tier sets the response time and the escalation path the business expects.

### Question 100 — A

Answer: Orchestrate the workflow in Agent Platform Pipelines. Pipelines runs each step as a container with lineage and caching, so a rerun is reproducible. Local study-map skill 2.7 (Agent Platform ML Workflows), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 2 (managing and provisioning): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Correct. In this case: Pipelines runs each step as a container with lineage and caching, so a rerun is reproducible.
- **B:** Incorrect for this question. Scheduler fires a job on a cron or App Engine schedule and retries on failure. Why the correct answer wins: Pipelines runs each step as a container with lineage and caching, so a rerun is reproducible.
- **C:** Incorrect for this question. A Dataproc cluster runs open-source Spark and Hadoop with jobs that need a persistent cluster. Why the correct answer wins: Pipelines runs each step as a container with lineage and caching, so a rerun is reproducible.
- **D:** Incorrect for this question. Batch prediction reads a file and writes predictions without holding serving capacity. Why the correct answer wins: Pipelines runs each step as a container with lineage and caching, so a rerun is reproducible.
