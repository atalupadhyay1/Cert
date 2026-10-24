# Google Cloud Professional Cloud Architect — Full-Length Mock Exam 1

Professional Cloud Architect · 100 questions · expanded practice bank · passing score not published

Blueprint-weighted mock exam. Item mix: 84 multiple-choice (selection count stated where needed), 16 multi-select, and 4 case studies of 5 questions. 8 of the multiple-choice items ask you to choose the correct candidate sequence. The live exam publishes 50-60 questions and two case studies worth 20-30 per cent of the score; this set is larger on purpose and cannot reproduce the split-screen case-study panel, drag-and-drop ordering, or lab tasks. See the README for the exact fidelity boundary.

Original educational content, not actual, recalled, or copied Google exam items.

## Questions

### 1. The board wants to know whether moving checkout to Google Cloud succeeded. What must the design define first?

Domain: Designing and planning a cloud solution architecture

- A. Build a three-year total cost of ownership model
- B. Act on the Recommender suggestions
- C. Define the baseline and target as a KPI with an owner
- D. Publish a shared dashboard

### 2. Procurement asks whether the cloud design is cheaper than the data centre over five years. What should be produced?

Domain: Designing and planning a cloud solution architecture

- A. Buy committed use discounts for the steady baseline
- B. Set a budget with alert thresholds
- C. Export billing to BigQuery and review it per label
- D. Build a three-year total cost of ownership model

### 3. A payments team cannot agree on how much downtime is acceptable. Which two artefacts turn the discussion into a requirement? Select two.

Domain: Designing and planning a cloud solution architecture

- A. Put the recovery commitment in the contract
- B. Tag the resources with labels for cost reporting
- C. Set the RPO and RTO with the business owner
- D. Export billing to BigQuery and review it per label
- E. Publish a shared dashboard

### 4. The chief financial officer is worried about being locked into one provider. What should the design include from the start?

Domain: Designing and planning a cloud solution architecture

- A. Build a three-year total cost of ownership model
- B. Document the exit plan and data portability
- C. Define the baseline and target as a KPI with an owner
- D. Run a limited pilot with a success criterion agreed in advance

### 5. A cluster must survive the loss of one zone without anyone rescheduling pods by hand. What should be created?

Domain: Designing and planning a cloud solution architecture

- A. Use a managed instance group with autoscaling
- B. Create a regional GKE cluster
- C. Create a zonal GKE cluster
- D. Deploy the service on Cloud Run

### 6. Traffic must leave a failing region automatically when health checks fail. What should the design use?

Domain: Designing and planning a cloud solution architecture

- A. Manage the zone in Cloud DNS
- B. Add global load balancing with failover
- C. Enable Cloud CDN on the backend
- D. Create a DNS peering zone

### 7. An application has a two-minute database recovery objective and a standby in a second region. Which two pieces are required? Select two.

Domain: Designing and planning a cloud solution architecture

- A. Enable Cloud CDN on the backend
- B. Enable Cloud SQL high availability with a standby
- C. Replicate the data to the second region
- D. Use Memorystore
- E. Create a materialized view for the repeated aggregate

### 8. A team must prove its recovery objective in a rehearsal before the board meeting. Which sequence is correct?

Domain: Designing and planning a cloud solution architecture

- A. Choose the DR pattern → fail over in a game day → set the RTO and RPO targets → build the standby environment
- B. Build and replicate the standby environment → choose the DR pattern → set the RTO and RPO targets → fail over in a game day
- C. Set the RTO and RPO targets → choose the DR pattern that meets them → build and replicate the standby environment → fail over in a game day and record the result
- D. Fail over in a game day → set the RTO and RPO targets → choose the DR pattern → build the standby environment

### 9. Six teams need separate projects but one centrally managed subnet and firewall set. What should be used?

Domain: Designing and planning a cloud solution architecture

- A. Peer the two VPC networks
- B. Deploy Cloud NAT for outbound traffic
- C. Build a Network Connectivity Center hub
- D. Use Shared VPC with host and service projects

### 10. A partner must reach a service in your project privately, with no internet path. Which two designs provide that? Select two.

Domain: Designing and planning a cloud solution architecture

- A. Peer the two VPC networks
- B. Publish the service through Private Service Connect
- C. Deploy Cloud NAT for outbound traffic
- D. Enable Cloud CDN on the backend
- E. Issue a short-lived signed URL

### 11. Forty VPC networks must talk through a central hub with transitive routing. What should be built?

Domain: Designing and planning a cloud solution architecture

- A. Peer the two VPC networks
- B. Build a Network Connectivity Center hub
- C. Create a DNS peering zone
- D. Deploy Cloud NAT for outbound traffic

### 12. Serverless services must reach internal addresses, and every new network must inherit the same deny rules. Which two controls apply? Select two.

Domain: Designing and planning a cloud solution architecture

- A. Attach a Cloud Armor security policy
- B. Attach a Serverless VPC Access connector
- C. Apply a hierarchical firewall policy at the organization or folder
- D. Enable Cloud CDN on the backend
- E. Issue a short-lived signed URL

### 13. Access patterns are unknown and change from month to month across millions of objects. What should be enabled?

Domain: Designing and planning a cloud solution architecture

- A. Store the objects in Nearline storage class
- B. Enable Autoclass on the bucket
- C. Store the objects in Standard storage class
- D. Add a lifecycle rule that transitions and then deletes

### 14. A workload needs 500,000 key lookups per second at single-digit millisecond latency. What should be used?

Domain: Designing and planning a cloud solution architecture

- A. Use Firestore
- B. Use Bigtable
- C. Use Cloud SQL
- D. Load the data into BigQuery

### 15. Analysts must query files in Cloud Storage while each team sees only its own rows. Which two choices are needed? Select two.

Domain: Designing and planning a cloud solution architecture

- A. Query the files as an external table
- B. Build the dashboard in Looker Studio
- C. Store the objects in Standard storage class
- D. Add row-level access policies to the table
- E. Create a BigLake table over the Cloud Storage files

### 16. A team wants the Kubernetes API without managing nodes or patching them. What should be chosen?

Domain: Designing and planning a cloud solution architecture

- A. Use GKE Standard with a node pool per workload shape
- B. Deploy the service on Cloud Run
- C. Use GKE Autopilot
- D. Submit the work as a Batch job

### 17. An internal API is idle at night and must scale to zero between requests. What should be used?

Domain: Designing and planning a cloud solution architecture

- A. Deploy the service on Cloud Run
- B. Run the legacy stack on Google Cloud VMware Engine
- C. Use a managed instance group with autoscaling
- D. Use GKE Standard with a node pool per workload shape

### 18. Support agents need grounded answers with citations drawn from 40,000 policy documents. What should be used?

Domain: Designing and planning a cloud solution architecture

- A. Use Gemini Enterprise for the knowledge assistant
- B. Use the Vision API for the images
- C. Use Document AI with a specialised processor
- D. Index the corpus with Vertex AI Search

### 19. 1,800 servers must be inventoried and sized before any migration wave is planned. What should be used?

Domain: Designing and planning a cloud solution architecture

- A. Copy the files with Storage Transfer Service
- B. Assess the estate in Migration Center
- C. Convert the VMs with Migrate to Containers
- D. Use Database Migration Service

### 20. Two data centres need a predictable 20 Gbps private path into one region. What should be ordered?

Domain: Managing and provisioning a solution infrastructure

- A. Use HA VPN with two tunnels
- B. Order Partner Interconnect
- C. Order a Dedicated Interconnect
- D. Deploy Cloud NAT for outbound traffic

### 21. A regulator requires that an archive cannot be deleted for seven years. What should be applied?

Domain: Managing and provisioning a solution infrastructure

- A. Add a lifecycle rule that transitions and then deletes
- B. Apply a bucket retention policy with a locked period
- C. Enable Autoclass on the bucket
- D. Enable object versioning

### 22. A bucket receives 4 TB a day and only the last thirty days are ever read. What should be configured?

Domain: Managing and provisioning a solution infrastructure

- A. Use a Transfer Appliance for the one-off bulk move
- B. Store the objects in Nearline storage class
- C. Enable Autoclass on the bucket
- D. Add a lifecycle rule that transitions and then deletes

### 23. An orders database must feed BigQuery continuously, and analysts query by order date. Which two choices apply? Select two.

Domain: Managing and provisioning a solution infrastructure

- A. Stream rows with the legacy insertAll call
- B. Use Datastream for change data capture
- C. Add a read replica and route reads to it
- D. Partition the table on the date column
- E. Use a Dataproc cluster

### 24. A fleet of 400 virtual machines is missing operating system patches. What should be used?

Domain: Managing and provisioning a solution infrastructure

- A. Use VM Manager for OS patch compliance
- B. Run the batch tier on Spot VMs
- C. Manage the resources with Config Connector
- D. Run the build in Cloud Build

### 25. A batch tier runs a constant baseline and spikes for a few hours each week. Which two purchasing choices apply? Select two.

Domain: Managing and provisioning a solution infrastructure

- A. Run the batch tier on Spot VMs
- B. Use local SSD for the scratch space
- C. Buy committed use discounts for the steady baseline
- D. Share the cost view with the engineering teams
- E. Move the steady services to E2 machine types

### 26. Pods must call Cloud Storage without any key file on disk. What should be enabled?

Domain: Managing and provisioning a solution infrastructure

- A. Put the credential in an environment variable on the instance
- B. Create a service account key file for the pipeline
- C. Use Workload Identity Federation for the external pipeline
- D. Enable Workload Identity Federation for GKE

### 27. Nodes must have no external address yet still reach Google APIs. What should be done?

Domain: Managing and provisioning a solution infrastructure

- A. Deploy Cloud NAT for outbound traffic
- B. Create private nodes with no external IP addresses
- C. Create a zonal GKE cluster
- D. Use sole-tenant nodes

### 28. A latency-sensitive service suffers cold starts at the start of every shift. What should be configured?

Domain: Managing and provisioning a solution infrastructure

- A. Deploy on App Engine flexible environment
- B. Deploy the workload on Cloud Run with a GPU
- C. Set a minimum instance count on the Cloud Run service
- D. Raise the request concurrency setting

### 29. A Cloud Run service must call an internal database and hold its credential securely. Which two changes are required? Select two.

Domain: Managing and provisioning a solution infrastructure

- A. Store the credential in Secret Manager
- B. Deploy Cloud NAT for outbound traffic
- C. Put the credential in an environment variable on the instance
- D. Attach a Serverless VPC Access connector
- E. Create a service account key file for the pipeline

### 30. Three environments must be created identically and reviewed before anything is applied. What should be used?

Domain: Managing and provisioning a solution infrastructure

- A. Use Deployment Manager templates
- B. Manage the resources with Terraform
- C. Automate the step with the gcloud CLI
- D. Manage the resources with Config Connector

### 31. A platform team is setting up Terraform delivery for the first time. Which sequence is correct?

Domain: Managing and provisioning a solution infrastructure

- A. Run a plan in CI → apply through the pipeline → define modules → create the remote state bucket
- B. Define modules → apply through the pipeline → run a plan in CI → create the remote state bucket
- C. Apply through the pipeline → create the remote state bucket → define modules → run a plan in CI
- D. Create a remote state bucket with versioning → define modules per environment → run a plan in CI and require review → apply through the pipeline with a scoped service account

### 32. A training workflow must rerun reproducibly and record the lineage of every step. What should be used?

Domain: Managing and provisioning a solution infrastructure

- A. Orchestrate the workflow in Agent Platform Pipelines
- B. Use a Dataproc cluster
- C. Run batch prediction
- D. Trigger the job with Cloud Scheduler

### 33. A model must move from an experiment to a monitored production endpoint. Which sequence is correct?

Domain: Managing and provisioning a solution infrastructure

- A. Register the model → curate the training data → deploy to an endpoint → train the model
- B. Train the model → deploy to an endpoint → curate the training data → register the model
- C. Curate and version the training data → train and evaluate the model in a pipeline → register the model and record its metrics → deploy to an endpoint with traffic splitting and model monitoring
- D. Deploy to an endpoint → train the model → register the model → curate the training data

### 34. A team wants to evaluate an open-weight model alongside a first-party model. Where should it look?

Domain: Managing and provisioning a solution infrastructure

- A. Index the corpus with Vertex AI Search
- B. Use Gemini Cloud Assist for the investigation
- C. Select the model from Model Garden
- D. Build the agent with the Agent Development Kit

### 35. No predefined role matches a job that needs exactly four permissions. What should be created?

Domain: Designing for security and compliance

- A. Add an IAM condition on the binding
- B. Grant a predefined role at the narrowest resource
- C. Define a custom role with only the required permissions
- D. Create a service account key file for the pipeline

### 36. Engineers must reproduce a pipeline failure without holding a long-lived credential. What should be granted?

Domain: Designing for security and compliance

- A. Create a service account key file for the pipeline
- B. Put the credential in an environment variable on the instance
- C. Grant service account impersonation instead of a key
- D. Use Workload Identity Federation for the external pipeline

### 37. Access must work only during business hours, and one contractor must never regain access. Which two controls apply? Select two.

Domain: Designing for security and compliance

- A. Apply an IAM deny policy
- B. Run a bastion host with a public address
- C. Grant a predefined role at the narrowest resource
- D. Add an IAM condition on the binding
- E. Tag the resources with labels for cost reporting

### 38. No one may create a virtual machine with an external address, in any project. What should be enforced?

Domain: Designing for security and compliance

- A. Create a separate project per environment
- B. Create a folder per environment and bind roles there
- C. Enforce the control with an organization policy constraint
- D. Tag the resources with labels for cost reporting

### 39. A bank must be able to revoke its own key and stop all decryption immediately. What should be used?

Domain: Designing for security and compliance

- A. Encrypt with a customer-managed key in Cloud KMS
- B. Supply a customer-supplied encryption key
- C. Store the credential in Secret Manager
- D. Use Cloud HSM for the key

### 40. Keys must stay in the country where the data lives and must change on a schedule. Which two settings apply? Select two.

Domain: Designing for security and compliance

- A. Create the key ring in the same region as the data
- B. Put the credential in an environment variable on the instance
- C. Set an automatic rotation period on the key
- D. Use Cloud HSM for the key
- E. Supply a customer-supplied encryption key

### 41. A developer with read permission must not be able to copy an export to a personal project. What should be applied?

Domain: Designing for security and compliance

- A. Put the projects inside a VPC Service Controls perimeter
- B. Apply a hierarchical firewall policy at the organization or folder
- C. Apply an IAM deny policy
- D. Tag the resources with labels for cost reporting

### 42. A perimeter is about to be enforced on a busy organisation. What should be done first?

Domain: Designing for security and compliance

- A. Put the projects inside a VPC Service Controls perimeter
- B. Route the logs with an aggregated sink
- C. Run the perimeter in dry-run mode first
- D. Attach a Cloud Armor security policy

### 43. Clinicians must reach an internal portal from any device without a VPN. What should be used?

Domain: Designing for security and compliance

- A. Run a bastion host with a public address
- B. Put Identity-Aware Proxy in front of the application
- C. Enable Private Google Access on the subnet
- D. Deploy Cloud NAT for outbound traffic

### 44. Administrators must not hold public addresses, and workforce access must judge the device. Which two controls apply? Select two.

Domain: Designing for security and compliance

- A. Create a service account key file for the pipeline
- B. Deploy Cloud NAT for outbound traffic
- C. Use OS Login for administrative SSH
- D. Use Chrome Enterprise Premium for the workforce
- E. Run a bastion host with a public address

### 45. Only images built by the approved pipeline may start in the cluster. What should be enforced?

Domain: Designing for security and compliance

- A. Enable Artifact Analysis scanning on the repository
- B. Store the images in Artifact Registry
- C. Require Binary Authorization attestations
- D. Enable network policy enforcement

### 46. An assistant must resist prompt injection and block unsafe responses. What should be added?

Domain: Designing for security and compliance

- A. De-identify the data with Sensitive Data Protection
- B. Screen prompts and responses with Model Armor
- C. Require an access level in the perimeter
- D. Turn on Security Command Center findings

### 47. Free-text support notes contain payment details that must not reach the analytics table. What should be used?

Domain: Designing for security and compliance

- A. Screen prompts and responses with Model Armor
- B. Select the model from Model Garden
- C. Index the corpus with Vertex AI Search
- D. De-identify the data with Sensitive Data Protection

### 48. An auditor asks for evidence of who read which patient record. Which sequence is correct?

Domain: Designing for security and compliance

- A. Create a locked log bucket → enable data access audit logs → query the evidence → route the logs with a sink
- B. Route the logs with a sink → query the evidence → enable audit logs → create a locked bucket
- C. Enable data access audit logs for the services in scope → create a locked log bucket with the required retention → route the logs with an aggregated sink → query and export the evidence for the auditor
- D. Query the evidence → create a locked log bucket → enable audit logs → route the logs

### 49. A team merges twice a week and suffers long-lived conflicts. What should change?

Domain: Analyzing and optimizing technical and business processes

- A. Roll the change out instance by instance
- B. Put the change behind a feature flag
- C. Rebuild the artifact separately for each environment
- D. Adopt trunk-based development with short-lived branches

### 50. A service is released several times a day and consumers break on schema changes. Which two practices help most? Select two.

Domain: Analyzing and optimizing technical and business processes

- A. Run a load test at the expected peak
- B. Cover the change with unit, integration, and a few end-to-end tests
- C. Run a chaos experiment against a zone
- D. Add a contract test on the API
- E. Commission a penetration test

### 51. What was tested must be exactly what runs in production. What should the pipeline do?

Domain: Analyzing and optimizing technical and business processes

- A. Set a budget with alert thresholds
- B. Roll the change out instance by instance
- C. Rebuild the artifact separately for each environment
- D. Promote the same tested artifact between environments

### 52. A request failed at 14:07 and the team needs the exact error text and fields. Where should they look?

Domain: Analyzing and optimizing technical and business processes

- A. Publish a shared dashboard
- B. Act on the Recommender suggestions
- C. Inspect the trace waterfall in Cloud Trace
- D. Query the entries in Cloud Logging

### 53. A launch is expected to bring twelve times the normal concurrency. What should be run first?

Domain: Analyzing and optimizing technical and business processes

- A. Cover the change with unit, integration, and a few end-to-end tests
- B. Commission a penetration test
- C. Run a chaos experiment against a zone
- D. Run a load test at the expected peak

### 54. A service can accept an hour of recovery time but must not pay for a running copy. What pattern fits?

Domain: Analyzing and optimizing technical and business processes

- A. Run a warm standby at reduced capacity
- B. Use backup and restore
- C. Run active-active across two regions
- D. Run a pilot-light standby

### 55. A service is failing in production and the team must respond in order. Which sequence is correct?

Domain: Analyzing and optimizing technical and business processes

- A. Write the postmortem → detect the symptom → isolate the root cause → restore service
- B. Detect the symptom through an alert → contain the impact and restore service → isolate the root cause from logs, traces, and metrics → apply the permanent fix and write the postmortem
- C. Restore service → detect the symptom → write the postmortem → isolate the root cause
- D. Isolate the root cause → detect the symptom → write the postmortem → restore service

### 56. Finance asks whether the design will cost less in year three. What should the architect produce?

Domain: Analyzing and optimizing technical and business processes

- A. Act on the Recommender suggestions
- B. Set a budget with alert thresholds
- C. Build a three-year total cost of ownership model
- D. Export billing to BigQuery and review it per label

### 57. A team suspects it is paying for idle resources. What should be reviewed first?

Domain: Analyzing and optimizing technical and business processes

- A. Raise the quota before the peak
- B. Act on the Recommender suggestions
- C. Export billing to BigQuery and review it per label
- D. Tag the resources with labels for cost reporting

### 58. BigQuery cost must come down without guessing what to change. Which sequence is correct?

Domain: Analyzing and optimizing technical and business processes

- A. Measure slot time → rewrite the query → inspect the plan → partition the table
- B. Rewrite the query → partition the table → measure slot time → inspect the plan
- C. Inspect the query plan and bytes processed → partition and cluster the table on the filter columns → rewrite the query to prune partitions → measure the new slot time and bytes scanned
- D. Partition and cluster the table → measure slot time → inspect the plan → rewrite the query

### 59. Two directors disagree about whether to build or buy the identity service. What should the architect do?

Domain: Analyzing and optimizing technical and business processes

- A. Agree the decision rights with the stakeholders
- B. Publish a service catalog entry with an approved template
- C. Publish a runbook per alert
- D. Route the change through a change advisory board

### 60. Teams need a compliant project without waiting for the platform team. What should be published?

Domain: Analyzing and optimizing technical and business processes

- A. Publish a service catalog entry with an approved template
- B. Enforce the control with an organization policy constraint
- C. Manage the resources with Terraform
- D. Tag the resources with labels for cost reporting

### 61. A new revision must be exposed to five per cent of traffic before any commitment. What should be used?

Domain: Managing implementation

- A. Roll out a canary to a small share of traffic
- B. Deploy blue/green with a traffic switch
- C. Roll the change out instance by instance
- D. Put the change behind a feature flag

### 62. Two identical environments are affordable and the switch must be reversible in seconds. What should be used?

Domain: Managing implementation

- A. Roll the change out instance by instance
- B. Roll out a canary to a small share of traffic
- C. Put the change behind a feature flag
- D. Deploy blue/green with a traffic switch

### 63. A release must return to the known-good build, not a rebuild of it. What should be kept?

Domain: Managing implementation

- A. Rebuild the artifact separately for each environment
- B. Promote the same tested artifact between environments
- C. Set a budget with alert thresholds
- D. Keep the previous image digest ready for rollback

### 64. A canary release must be planned end to end. Which sequence is correct?

Domain: Managing implementation

- A. Watch the error rate → deploy the new revision → shift traffic → build the image
- B. Shift full traffic to the new revision → build the image → watch the error rate → promote or roll back
- C. Build an immutable image and record its digest → deploy the new revision without traffic → shift a small traffic percentage and watch error and latency signals → promote to full traffic or roll back to the pinned digest
- D. Deploy the new revision → promote to full traffic → shift a small percentage → build the image

### 65. Different merchants need their own quotas, keys, and analytics at the gateway. What should be used?

Domain: Managing implementation

- A. Attach a Cloud Armor security policy
- B. Use API Gateway
- C. Publish the API through Apigee
- D. Use Cloud Endpoints

### 66. Merchants must never be broken by a change, and each version must have a known end. Which two practices apply? Select two.

Domain: Managing implementation

- A. Rebuild the artifact separately for each environment
- B. Add a contract test on the API
- C. Authenticate the call with an API key
- D. Publish a versioning and deprecation policy
- E. Roll the change out instance by instance

### 67. Twelve terabytes of files must be copied from another cloud on a weekly schedule. What should be used?

Domain: Managing implementation

- A. Assess the estate in Migration Center
- B. Convert the VMs with Migrate to Containers
- C. Copy the files with Storage Transfer Service
- D. Use a Transfer Appliance for the one-off bulk move

### 68. A 12 TB Oracle database must cut over with less than four hours of downtime. What should be used?

Domain: Managing implementation

- A. Copy the files with Storage Transfer Service
- B. Use Datastream for change data capture
- C. Migrate the database with Database Migration Service
- D. Use the BigQuery Data Transfer Service

### 69. A migration plan must be sequenced so dependencies move together. Which sequence is correct?

Domain: Managing implementation

- A. Cut over and decommission → validate a pilot wave → inventory the estate → group servers into waves
- B. Validate a pilot wave → inventory the estate → group servers into waves → cut over and decommission
- C. Group servers into waves → inventory the estate → cut over and decommission → validate a pilot wave
- D. Inventory the estate in Migration Center → group servers into dependency-based waves → validate a pilot wave in the target landing zone → cut over wave by wave and decommission the source

### 70. A pipeline must run integration tests without creating billable resources. What should be used?

Domain: Managing implementation

- A. Automate the step with the gcloud CLI
- B. Use the bq command-line tool
- C. Run the emulator in the pipeline
- D. Use Cloud Shell for the one-off task

### 71. An application must retry a quota error with the recommended backoff. What should it use?

Domain: Managing implementation

- A. Use the Google API client library with retries
- B. Authenticate the call with an API key
- C. Impersonate a service account for a curl test
- D. Automate the step with the gcloud CLI

### 72. The team needs the platform metrics that an alert will later use. What should be configured?

Domain: Ensuring solution and operations excellence

- A. Query the entries in Cloud Logging
- B. Define an SLO with an error budget
- C. Publish a shared dashboard
- D. Define dashboards and metrics in Cloud Monitoring

### 73. Host-level memory and application log lines must reach Google Cloud from the instances. What should be installed?

Domain: Ensuring solution and operations excellence

- A. Install the Ops Agent on the instances
- B. Inspect the trace waterfall in Cloud Trace
- C. Attach Cloud Profiler to the service
- D. Group the exceptions in Error Reporting

### 74. Availability must be measured from outside and one slow request must be broken down by service. Which two tools apply? Select two.

Domain: Ensuring solution and operations excellence

- A. Add an uptime check from several regions
- B. Publish a shared dashboard
- C. Act on the Recommender suggestions
- D. Inspect the trace waterfall in Cloud Trace
- E. Define an SLO with an error budget

### 75. The team wants an alert tied to the promise users care about, not to CPU. What should be defined?

Domain: Ensuring solution and operations excellence

- A. Define an SLO with an error budget
- B. Publish a shared dashboard
- C. Add an uptime check from several regions
- D. Create an alerting policy on the metric

### 76. A metric exists and someone must be told when it crosses a threshold for ten minutes. What should be created?

Domain: Ensuring solution and operations excellence

- A. Create a log-based metric
- B. Create an alerting policy on the metric
- C. Define an SLO with an error budget
- D. Publish a shared dashboard

### 77. The last incident took four hours because nobody knew the diagnostic steps. What should be published?

Domain: Ensuring solution and operations excellence

- A. Define an on-call rotation with an escalation path
- B. Publish a runbook per alert
- C. Match the support plan to the recovery commitment
- D. Publish a shared dashboard

### 78. The business expects a two-hour response to a severity-one case. What should be aligned?

Domain: Ensuring solution and operations excellence

- A. Match the support plan to the recovery commitment
- B. Define an on-call rotation with an escalation path
- C. Publish a runbook per alert
- D. Put the recovery commitment in the contract

### 79. The design claims a zone loss is survivable and nobody has tested it. What should be run?

Domain: Ensuring solution and operations excellence

- A. Roll out a canary to a small share of traffic
- B. Run a chaos experiment against a zone
- C. Commission a penetration test
- D. Run a load test at the expected peak

### 80. The same outage has now happened three times in a quarter. What should be produced after each incident?

Domain: Ensuring solution and operations excellence

- A. Write a blameless postmortem with actions
- B. Publish a runbook per alert
- C. Match the support plan to the recovery commitment
- D. Publish a shared dashboard

---

## Case study — Cobalt Retail Group

Cobalt Retail Group operates 640 stores and a checkout service that must respond in under 300 ms. Traffic is predictable Monday to Saturday and spikes on Black Friday to twelve times the normal rate. The current system runs on virtual machines in two on-premises data centres, and the board wants the peak moved to Google Cloud without rebuilding the applications. Store systems must reach the checkout service over a private path, and the chief financial officer has asked for a cost comparison between paying for peak capacity all year and paying for it four weeks a year. The company has no dedicated network engineers and relies on a small platform team.

The next 5 questions refer to it. Read the scenario once, then answer all 5; each item restates the constraint it tests and is scored individually.

### 81. The board asks what success looks like before the peak moves to Google Cloud. What should be agreed first?

Domain: Designing and planning a cloud solution architecture

- A. Export billing to BigQuery and review it per label
- B. Publish a shared dashboard
- C. Build a three-year total cost of ownership model
- D. Define the baseline and target as a KPI with an owner

### 82. The checkout service must scale for four weeks a year without rebuilding the application. What should be used?

Domain: Designing and planning a cloud solution architecture

- A. Use a managed instance group with autoscaling
- B. Use GKE Autopilot
- C. Submit the work as a Batch job
- D. Deploy the service on Cloud Run

### 83. Peak capacity is needed for four weeks and idle for the rest of the year. What should the architect recommend?

Domain: Analyzing and optimizing technical and business processes

- A. Run the batch tier on Spot VMs
- B. Move the steady services to E2 machine types
- C. Use sole-tenant nodes
- D. Buy committed use discounts for the steady baseline

### 84. A new checkout version must be proven on real traffic before Black Friday. What should be used?

Domain: Managing implementation

- A. Roll out a canary to a small share of traffic
- B. Deploy blue/green with a traffic switch
- C. Put the change behind a feature flag
- D. Roll the change out instance by instance

### 85. Nobody knows whether the design survives twelve times normal concurrency. What should be run?

Domain: Ensuring solution and operations excellence

- A. Run a load test at the expected peak
- B. Commission a penetration test
- C. Cover the change with unit, integration, and a few end-to-end tests
- D. Run a chaos experiment against a zone

---

## Case study — Helios Broadcasting

Helios Broadcasting streams live sport to 30 million viewers across Europe and North America. A premiere can raise concurrent viewers from 200,000 to 9 million in ten minutes, and the company is contractually required to keep the stream running through the loss of a single region. Video segments are written to a bucket in us-central1 and served to a global audience, and the packager runs on GKE. Advertising revenue is billed per delivered segment, so an outage has a direct financial cost. The board has asked for a design that survives one region failing without a manual decision, and finance has asked what the extra resilience costs per month.

The next 5 questions refer to it. Read the scenario once, then answer all 5; each item restates the constraint it tests and is scored individually.

### 86. The stream must not stop when a region is lost, and no manual decision is allowed. What should the architecture provide?

Domain: Designing and planning a cloud solution architecture

- A. Run active-active across two regions
- B. Run a pilot-light standby
- C. Run a warm standby at reduced capacity
- D. Use backup and restore

### 87. Segments are written once in us-central1 and fetched by a global audience. What should sit in front of the bucket?

Domain: Designing and planning a cloud solution architecture

- A. Use an internal passthrough load balancer
- B. Deploy Cloud NAT for outbound traffic
- C. Use gcloud storage commands
- D. Enable Cloud CDN on the backend

### 88. The segment archive must stay readable when one region is lost. Which bucket configuration meets that?

Domain: Managing and provisioning a solution infrastructure

- A. Store the objects in Standard storage class
- B. Use a dual-region bucket
- C. Store the objects in Nearline storage class
- D. Store the objects in Archive storage class

### 89. The board will fund regional resilience only if the target is explicit and achievable. Which two inputs are required? Select two.

Domain: Analyzing and optimizing technical and business processes

- A. Replicate the data to the second region
- B. Act on the Recommender suggestions
- C. Publish a shared dashboard
- D. Set the RPO and RTO with the business owner
- E. Tag the resources with labels for cost reporting

### 90. The team must know whether viewers actually received a stable stream. What should be defined per region?

Domain: Ensuring solution and operations excellence

- A. Publish a shared dashboard
- B. Define an SLO with an error budget
- C. Create an alerting policy on the metric
- D. Add an uptime check from several regions

---

## Case study — Meridian Health Systems

Meridian Health Systems runs a patient portal for 4.5 million members and must comply with HIPAA. Clinicians in twelve hospitals need single sign-on, and patients need to reach the portal from any device without a VPN. A recent audit found that one administrator could read every patient record, and the remediation plan must show that access is limited to the hospital a clinician works for. The portal runs on Cloud Run and reads records from Cloud SQL. The security team wants every administrative action recorded with the identity that performed it, retained for six years, and available to an auditor without a support ticket.

The next 5 questions refer to it. Read the scenario once, then answer all 5; each item restates the constraint it tests and is scored individually.

### 91. An administrator can currently read every patient record. What should replace the broad grant?

Domain: Designing for security and compliance

- A. Define a custom role with only the required permissions
- B. Grant a predefined role at the narrowest resource
- C. Run a bastion host with a public address
- D. Create a service account key file for the pipeline

### 92. Clinicians need single sign-on without a VPN, and device posture must be judged. Which two controls apply? Select two.

Domain: Designing for security and compliance

- A. Use Chrome Enterprise Premium for the workforce
- B. Deploy Cloud NAT for outbound traffic
- C. Run a bastion host with a public address
- D. Put Identity-Aware Proxy in front of the application
- E. Create a service account key file for the pipeline

### 93. Administrative actions must be attributable and retained for six years. What should be enabled?

Domain: Designing for security and compliance

- A. Review Access Transparency logs
- B. Enable Data Access audit logs
- C. Rely on Admin Activity audit logs
- D. Create a log-based metric

### 94. The portal runs on Cloud Run and must reach a database on a private address. What should be attached?

Domain: Managing and provisioning a solution infrastructure

- A. Enable Private Google Access on the subnet
- B. Deploy Cloud NAT for outbound traffic
- C. Publish the service through Private Service Connect
- D. Attach a Serverless VPC Access connector

### 95. An auditor must obtain the evidence without opening a support ticket. What should be built?

Domain: Ensuring solution and operations excellence

- A. Publish a runbook per alert
- B. Publish a shared dashboard
- C. Create a log-based metric
- D. Route the logs with an aggregated sink

---

## Case study — Vantage Logistics

Vantage Logistics tracks 90,000 vehicles across South America. Each vehicle emits a position every five seconds, which is about 18,000 messages per second at peak, and the operations team needs a live map no more than fifteen seconds behind. Telemetry must be kept for five years for accident investigation, but only the last ninety days are queried frequently. Vehicle identifiers arrive out of order when a truck leaves coverage for several hours, and duplicate readings are common at cell boundaries. The company is opening in two new countries next year and wants the same pipeline to serve them without a redesign.

The next 5 questions refer to it. Read the scenario once, then answer all 5; each item restates the constraint it tests and is scored individually.

### 96. 18,000 position messages per second must reach the live map within fifteen seconds. What should the producer publish to?

Domain: Designing and planning a cloud solution architecture

- A. Queue the work in Cloud Tasks
- B. Use the BigQuery Data Transfer Service
- C. Publish events to Pub/Sub
- D. Use Managed Service for Apache Airflow

### 97. Five years of telemetry must be retained cheaply after the hot window. What should hold it?

Domain: Designing and planning a cloud solution architecture

- A. Store the objects in Archive storage class
- B. Store the objects in Standard storage class
- C. Store the objects in Nearline storage class
- D. Use local SSD for the scratch space

### 98. Collectors at ninety depots will become VMs that are idle between shifts. How should they be provisioned?

Domain: Managing and provisioning a solution infrastructure

- A. Use a managed instance group with autoscaling
- B. Use VM Manager for OS patch compliance
- C. Run the batch tier on Spot VMs
- D. Use a custom machine type sized to the workload

### 99. Before two new countries go live, the map must keep up under their message rate. What should be run?

Domain: Analyzing and optimizing technical and business processes

- A. Run a load test at the expected peak
- B. Cover the change with unit, integration, and a few end-to-end tests
- C. Run a chaos experiment against a zone
- D. Commission a penetration test

### 100. Operations cannot see per-depot lag today. What should be built first?

Domain: Ensuring solution and operations excellence

- A. Act on the Recommender suggestions
- B. Publish a shared dashboard
- C. Inspect the trace waterfall in Cloud Trace
- D. Define dashboards and metrics in Cloud Monitoring

---

## Answer key and explanations

### Question 1 — C

Answer: Define the baseline and target as a KPI with an owner. Without a measured baseline and a named owner nobody can say afterwards whether the move worked. A measured baseline and a named owner make the outcome testable after the migration. Local study-map skill 1.1 (Business Requirements and Success Metrics), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 1 (designing and planning): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. The model compares run cost, people cost, and exit cost rather than the monthly bill alone. Why the correct answer wins: Without a measured baseline and a named owner nobody can say afterwards whether the move worked.
- **B:** Incorrect for this question. Recommender reports idle and over-provisioned resources with the estimated saving. Why the correct answer wins: Without a measured baseline and a named owner nobody can say afterwards whether the move worked.
- **C:** Correct. A measured baseline and a named owner make the outcome testable after the migration. In this case: Without a measured baseline and a named owner nobody can say afterwards whether the move worked.
- **D:** Incorrect for this question. The dashboard gives the team one view of the same signals during an incident. Why the correct answer wins: Without a measured baseline and a named owner nobody can say afterwards whether the move worked.

### Question 2 — D

Answer: Build a three-year total cost of ownership model. Run cost alone ignores people, licences, and exit cost, so the comparison has to be a total cost model. The model compares run cost, people cost, and exit cost rather than the monthly bill alone. Local study-map skill 1.1 (Business Requirements and Success Metrics), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 1 (designing and planning): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. A one- or three-year commitment discounts the capacity that runs constantly, not the peaks. Why the correct answer wins: Run cost alone ignores people, licences, and exit cost, so the comparison has to be a total cost model.
- **B:** Incorrect for this question. A budget alerts on spend but does not stop it. Why the correct answer wins: Run cost alone ignores people, licences, and exit cost, so the comparison has to be a total cost model.
- **C:** Incorrect for this question. The export attributes cost to the team and service that caused it. Why the correct answer wins: Run cost alone ignores people, licences, and exit cost, so the comparison has to be a total cost model.
- **D:** Correct. The model compares run cost, people cost, and exit cost rather than the monthly bill alone. In this case: Run cost alone ignores people, licences, and exit cost, so the comparison has to be a total cost model.

### Question 3 — A, C

Answers: Set the RPO and RTO with the business owner; Put the recovery commitment in the contract. The targets quantify the loss, and the contract attaches a consequence to missing them. The targets come from the business impact of data loss and downtime, not from the technology. The contract converts an internal target into an obligation with a consequence. Local study-map skill 1.2 (Non-Functional Requirements and Trade-offs), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 1 (designing and planning): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Correct. The contract converts an internal target into an obligation with a consequence. In this case: The targets quantify the loss, and the contract attaches a consequence to missing them.
- **B:** Incorrect for this question. Labels attribute spend in billing export; they do not grant or restrict access. Why the correct answer wins: The targets quantify the loss, and the contract attaches a consequence to missing them.
- **C:** Correct. The targets come from the business impact of data loss and downtime, not from the technology. In this case: The targets quantify the loss, and the contract attaches a consequence to missing them.
- **D:** Incorrect for this question. The export attributes cost to the team and service that caused it. Why the correct answer wins: The targets quantify the loss, and the contract attaches a consequence to missing them.
- **E:** Incorrect for this question. The dashboard gives the team one view of the same signals during an incident. Why the correct answer wins: The targets quantify the loss, and the contract attaches a consequence to missing them.

### Question 4 — B

Answer: Document the exit plan and data portability. An exit plan and data portability keep the migration reversible and bound how proprietary the design may become. The exit plan keeps the migration reversible and constrains how proprietary the design may become. Local study-map skill 1.2 (Non-Functional Requirements and Trade-offs), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 1 (designing and planning): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. The model compares run cost, people cost, and exit cost rather than the monthly bill alone. Why the correct answer wins: An exit plan and data portability keep the migration reversible and bound how proprietary the design may become.
- **B:** Correct. The exit plan keeps the migration reversible and constrains how proprietary the design may become. In this case: An exit plan and data portability keep the migration reversible and bound how proprietary the design may become.
- **C:** Incorrect for this question. A measured baseline and a named owner make the outcome testable after the migration. Why the correct answer wins: An exit plan and data portability keep the migration reversible and bound how proprietary the design may become.
- **D:** Incorrect for this question. The pilot produces evidence on the real workload before the whole estate commits. Why the correct answer wins: An exit plan and data portability keep the migration reversible and bound how proprietary the design may become.

### Question 5 — B

Answer: Create a regional GKE cluster. A regional cluster replicates the control plane across zones, so a zone loss does not stop scheduling. Local study-map skill 1.3 (High Availability and Failover Design), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 1 (designing and planning): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. The group replaces unhealthy instances and adds capacity from a template as load rises. Why the correct answer wins: A regional cluster replicates the control plane across zones, so a zone loss does not stop scheduling.
- **B:** Correct. In this case: A regional cluster replicates the control plane across zones, so a zone loss does not stop scheduling.
- **C:** Incorrect for this question. A zonal cluster keeps its control plane in one zone, so that zone loss takes the cluster with it. Why the correct answer wins: A regional cluster replicates the control plane across zones, so a zone loss does not stop scheduling.
- **D:** Incorrect for this question. Cloud Run runs a stateless container per request and scales to zero when idle. Why the correct answer wins: A regional cluster replicates the control plane across zones, so a zone loss does not stop scheduling.

### Question 6 — B

Answer: Add global load balancing with failover. Health-checked global load balancing moves traffic without waiting for a DNS record to expire. Health-checked failover moves traffic to the surviving region instead of waiting for DNS to expire. Local study-map skill 1.3 (High Availability and Failover Design), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 1 (designing and planning): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. Cloud DNS serves the records with anycast resolution and health-checked routing policies. Why the correct answer wins: Health-checked global load balancing moves traffic without waiting for a DNS record to expire.
- **B:** Correct. Health-checked failover moves traffic to the surviving region instead of waiting for DNS to expire. In this case: Health-checked global load balancing moves traffic without waiting for a DNS record to expire.
- **C:** Incorrect for this question. CDN caches responses at edge locations, which cuts origin load and latency for repeat reads. Why the correct answer wins: Health-checked global load balancing moves traffic without waiting for a DNS record to expire.
- **D:** Incorrect for this question. DNS peering resolves names across networks without transferring zone ownership. Why the correct answer wins: Health-checked global load balancing moves traffic without waiting for a DNS record to expire.

### Question 7 — B, C

Answers: Enable Cloud SQL high availability with a standby; Replicate the data to the second region. The standby has to take over the database, and the data must already exist in the region where it takes over. A regional standby takes over automatically when the primary zone fails. The data must exist in the second region before any compute there can serve it. Local study-map skill 1.3 (High Availability and Failover Design), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 1 (designing and planning): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. CDN caches responses at edge locations, which cuts origin load and latency for repeat reads. Why the correct answer wins: The standby has to take over the database, and the data must already exist in the region where it takes over.
- **B:** Correct. A regional standby takes over automatically when the primary zone fails. In this case: The standby has to take over the database, and the data must already exist in the region where it takes over.
- **C:** Correct. The data must exist in the second region before any compute there can serve it. In this case: The standby has to take over the database, and the data must already exist in the region where it takes over.
- **D:** Incorrect for this question. Memorystore provides managed Redis or Memcached for sub-millisecond cache lookups. Why the correct answer wins: The standby has to take over the database, and the data must already exist in the region where it takes over.
- **E:** Incorrect for this question. The view stores the aggregate result and refreshes incrementally as base data arrives. Why the correct answer wins: The standby has to take over the database, and the data must already exist in the region where it takes over.

### Question 8 — C

Answer: Set the RTO and RPO targets → choose the DR pattern that meets them → build and replicate the standby environment → fail over in a game day and record the result. Targets drive the pattern, the pattern drives the build, and only a rehearsal proves the numbers. Local study-map skill 1.3 (High Availability and Failover Design), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 1 (designing and planning): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. The pattern has no basis until the targets exist, and the drill cannot precede the build. Why the correct answer wins: Targets drive the pattern, the pattern drives the build, and only a rehearsal proves the numbers.
- **B:** Incorrect for this question. Building before the targets and pattern are chosen risks an environment that cannot meet either. Why the correct answer wins: Targets drive the pattern, the pattern drives the build, and only a rehearsal proves the numbers.
- **C:** Correct. In this case: Targets drive the pattern, the pattern drives the build, and only a rehearsal proves the numbers.
- **D:** Incorrect for this question. A failover drill with no targets or standby environment proves nothing. Why the correct answer wins: Targets drive the pattern, the pattern drives the build, and only a rehearsal proves the numbers.

### Question 9 — D

Answer: Use Shared VPC with host and service projects. A Shared VPC keeps the network in a host project while each team keeps its own service project. One host project owns the subnets and firewall rules while each team keeps its own service project. Local study-map skill 1.4 (Network Design), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 1 (designing and planning): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. Peering joins two networks at layer three but does not share firewalls or transitive routes. Why the correct answer wins: A Shared VPC keeps the network in a host project while each team keeps its own service project.
- **B:** Incorrect for this question. Cloud NAT lets private instances reach the internet without an external address. Why the correct answer wins: A Shared VPC keeps the network in a host project while each team keeps its own service project.
- **C:** Incorrect for this question. The hub gives transitive routing between spokes, which peering alone cannot provide. Why the correct answer wins: A Shared VPC keeps the network in a host project while each team keeps its own service project.
- **D:** Correct. One host project owns the subnets and firewall rules while each team keeps its own service project. In this case: A Shared VPC keeps the network in a host project while each team keeps its own service project.

### Question 10 — A, B

Answers: Publish the service through Private Service Connect; Peer the two VPC networks. A published endpoint gives a private address, and peering joins the two networks at layer three. A PSC endpoint gives a private IP in the consumer VPC without peering or exposing the service publicly. Peering joins two networks at layer three but does not share firewalls or transitive routes. Local study-map skill 1.4 (Network Design), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 1 (designing and planning): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Correct. Peering joins two networks at layer three but does not share firewalls or transitive routes. In this case: A published endpoint gives a private address, and peering joins the two networks at layer three.
- **B:** Correct. A PSC endpoint gives a private IP in the consumer VPC without peering or exposing the service publicly. In this case: A published endpoint gives a private address, and peering joins the two networks at layer three.
- **C:** Incorrect for this question. Cloud NAT lets private instances reach the internet without an external address. Why the correct answer wins: A published endpoint gives a private address, and peering joins the two networks at layer three.
- **D:** Incorrect for this question. CDN caches responses at edge locations, which cuts origin load and latency for repeat reads. Why the correct answer wins: A published endpoint gives a private address, and peering joins the two networks at layer three.
- **E:** Incorrect for this question. A signed URL grants one object for a fixed time without exposing credentials or making the bucket public. Why the correct answer wins: A published endpoint gives a private address, and peering joins the two networks at layer three.

### Question 11 — B

Answer: Build a Network Connectivity Center hub. Peering is not transitive, so a hub provides the routing that the spokes cannot provide themselves. The hub gives transitive routing between spokes, which peering alone cannot provide. Local study-map skill 1.4 (Network Design), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 1 (designing and planning): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. Peering joins two networks at layer three but does not share firewalls or transitive routes. Why the correct answer wins: Peering is not transitive, so a hub provides the routing that the spokes cannot provide themselves.
- **B:** Correct. The hub gives transitive routing between spokes, which peering alone cannot provide. In this case: Peering is not transitive, so a hub provides the routing that the spokes cannot provide themselves.
- **C:** Incorrect for this question. DNS peering resolves names across networks without transferring zone ownership. Why the correct answer wins: Peering is not transitive, so a hub provides the routing that the spokes cannot provide themselves.
- **D:** Incorrect for this question. Cloud NAT lets private instances reach the internet without an external address. Why the correct answer wins: Peering is not transitive, so a hub provides the routing that the spokes cannot provide themselves.

### Question 12 — B, C

Answers: Apply a hierarchical firewall policy at the organization or folder; Attach a Serverless VPC Access connector. The connector gives a route into the VPC, and a policy above the project applies to every future network. A policy above the project applies to every current and future network beneath it. The connector gives serverless workloads a route to internal addresses in the VPC. Local study-map skill 1.4 (Network Design), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 1 (designing and planning): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. Cloud Armor filters requests at the edge with allow and deny rules and adaptive protection. Why the correct answer wins: The connector gives a route into the VPC, and a policy above the project applies to every future network.
- **B:** Correct. The connector gives serverless workloads a route to internal addresses in the VPC. In this case: The connector gives a route into the VPC, and a policy above the project applies to every future network.
- **C:** Correct. A policy above the project applies to every current and future network beneath it. In this case: The connector gives a route into the VPC, and a policy above the project applies to every future network.
- **D:** Incorrect for this question. CDN caches responses at edge locations, which cuts origin load and latency for repeat reads. Why the correct answer wins: The connector gives a route into the VPC, and a policy above the project applies to every future network.
- **E:** Incorrect for this question. A signed URL grants one object for a fixed time without exposing credentials or making the bucket public. Why the correct answer wins: The connector gives a route into the VPC, and a policy above the project applies to every future network.

### Question 13 — B

Answer: Enable Autoclass on the bucket. Autoclass moves each object between classes as its access pattern changes, with no rules to maintain. Local study-map skill 1.5 (Storage and Data Store Selection), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 1 (designing and planning): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. Nearline suits data read about once a month and charges for early deletion. Why the correct answer wins: Autoclass moves each object between classes as its access pattern changes, with no rules to maintain.
- **B:** Correct. In this case: Autoclass moves each object between classes as its access pattern changes, with no rules to maintain.
- **C:** Incorrect for this question. Standard is for data read frequently and has no retrieval fee. Why the correct answer wins: Autoclass moves each object between classes as its access pattern changes, with no rules to maintain.
- **D:** Incorrect for this question. A lifecycle rule acts on object age or class, so retention stops depending on a person. Why the correct answer wins: Autoclass moves each object between classes as its access pattern changes, with no rules to maintain.

### Question 14 — B

Answer: Use Bigtable. Bigtable is the wide-column store built for high-throughput key access at low latency. Bigtable is a wide-column store for high-throughput key reads and writes at low latency. Local study-map skill 1.5 (Storage and Data Store Selection), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 1 (designing and planning): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. Firestore is a document store with real-time listeners and per-document transactions. Why the correct answer wins: Bigtable is the wide-column store built for high-throughput key access at low latency.
- **B:** Correct. Bigtable is a wide-column store for high-throughput key reads and writes at low latency. In this case: Bigtable is the wide-column store built for high-throughput key access at low latency.
- **C:** Incorrect for this question. Cloud SQL is a managed MySQL, PostgreSQL, or SQL Server instance with a familiar connection model. Why the correct answer wins: Bigtable is the wide-column store built for high-throughput key access at low latency.
- **D:** Incorrect for this question. BigQuery is serverless, columnar, and separates storage from compute, so a scan pays for the bytes read. Why the correct answer wins: Bigtable is the wide-column store built for high-throughput key access at low latency.

### Question 15 — D, E

Answers: Create a BigLake table over the Cloud Storage files; Add row-level access policies to the table. BigLake adds fine-grained governance over data that stays in the bucket, and row policies enforce the split. BigLake adds fine-grained access and row and column controls to data that stays in object storage. Row-level policies filter which rows each principal sees inside BigQuery itself. Local study-map skill 1.5 (Storage and Data Store Selection), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 1 (designing and planning): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. An external table reads the files in place, so governance depends on the underlying bucket. Why the correct answer wins: BigLake adds fine-grained governance over data that stays in the bucket, and row policies enforce the split.
- **B:** Incorrect for this question. Looker Studio renders the visualisation but inherits whatever query and permissions sit beneath it. Why the correct answer wins: BigLake adds fine-grained governance over data that stays in the bucket, and row policies enforce the split.
- **C:** Incorrect for this question. Standard is for data read frequently and has no retrieval fee. Why the correct answer wins: BigLake adds fine-grained governance over data that stays in the bucket, and row policies enforce the split.
- **D:** Correct. Row-level policies filter which rows each principal sees inside BigQuery itself. In this case: BigLake adds fine-grained governance over data that stays in the bucket, and row policies enforce the split.
- **E:** Correct. BigLake adds fine-grained access and row and column controls to data that stays in object storage. In this case: BigLake adds fine-grained governance over data that stays in the bucket, and row policies enforce the split.

### Question 16 — C

Answer: Use GKE Autopilot. Autopilot manages nodes, scaling, and patching, so the team owns only its workloads. Local study-map skill 1.6 (Compute Platform Selection), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 1 (designing and planning): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. Standard exposes node configuration and patching, which the team must then run itself. Why the correct answer wins: Autopilot manages nodes, scaling, and patching, so the team owns only its workloads.
- **B:** Incorrect for this question. Cloud Run runs a stateless container per request and scales to zero when idle. Why the correct answer wins: Autopilot manages nodes, scaling, and patching, so the team owns only its workloads.
- **C:** Correct. In this case: Autopilot manages nodes, scaling, and patching, so the team owns only its workloads.
- **D:** Incorrect for this question. Batch schedules containerised jobs onto managed or existing capacity and retires it when done. Why the correct answer wins: Autopilot manages nodes, scaling, and patching, so the team owns only its workloads.

### Question 17 — A

Answer: Deploy the service on Cloud Run. Cloud Run scales to zero and bills per request, which suits an intermittent internal API. Cloud Run runs a stateless container per request and scales to zero when idle. Local study-map skill 1.6 (Compute Platform Selection), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 1 (designing and planning): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Correct. Cloud Run runs a stateless container per request and scales to zero when idle. In this case: Cloud Run scales to zero and bills per request, which suits an intermittent internal API.
- **B:** Incorrect for this question. VMware Engine keeps the existing hypervisor and operations model while moving the hardware into Google Cloud. Why the correct answer wins: Cloud Run scales to zero and bills per request, which suits an intermittent internal API.
- **C:** Incorrect for this question. The group replaces unhealthy instances and adds capacity from a template as load rises. Why the correct answer wins: Cloud Run scales to zero and bills per request, which suits an intermittent internal API.
- **D:** Incorrect for this question. Standard exposes node configuration and patching, which the team must then run itself. Why the correct answer wins: Cloud Run scales to zero and bills per request, which suits an intermittent internal API.

### Question 18 — D

Answer: Index the corpus with Vertex AI Search. Vertex AI Search returns grounded, cited results over private documents without a custom index. Local study-map skill 1.8 (AI and ML Solution Design), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 1 (designing and planning): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. Gemini Enterprise adds enterprise search, agents, and governance over the connected corpus. Why the correct answer wins: Vertex AI Search returns grounded, cited results over private documents without a custom index.
- **B:** Incorrect for this question. The prebuilt Vision model labels, detects, and reads text without training a model. Why the correct answer wins: Vertex AI Search returns grounded, cited results over private documents without a custom index.
- **C:** Incorrect for this question. A Document AI processor extracts structured fields from forms and invoices with layout awareness. Why the correct answer wins: Vertex AI Search returns grounded, cited results over private documents without a custom index.
- **D:** Correct. In this case: Vertex AI Search returns grounded, cited results over private documents without a custom index.

### Question 19 — B

Answer: Assess the estate in Migration Center. Migration Center inventories the estate and estimates the target size and cost before a wave is chosen. Migration Center inventories the servers and estimates the target size and cost. Local study-map skill 1.9 (Migration Planning and Future Improvement), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 1 (designing and planning): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. The service moves object data between buckets or clouds on a schedule. Why the correct answer wins: Migration Center inventories the estate and estimates the target size and cost before a wave is chosen.
- **B:** Correct. Migration Center inventories the servers and estimates the target size and cost. In this case: Migration Center inventories the estate and estimates the target size and cost before a wave is chosen.
- **C:** Incorrect for this question. The tool rewrites a VM workload into a container image so it can run on GKE. Why the correct answer wins: Migration Center inventories the estate and estimates the target size and cost before a wave is chosen.
- **D:** Incorrect for this question. The service moves a database with continuous replication and a short cutover window. Why the correct answer wins: Migration Center inventories the estate and estimates the target size and cost before a wave is chosen.

### Question 20 — C

Answer: Order a Dedicated Interconnect. A dedicated circuit gives predictable bandwidth over a private path at the colocation facility. Local study-map skill 2.1 (Hybrid and Multicloud Connectivity), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 2 (managing and provisioning): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. Two tunnels across two interfaces survive one path failing, and the SLA depends on that. Why the correct answer wins: A dedicated circuit gives predictable bandwidth over a private path at the colocation facility.
- **B:** Incorrect for this question. A partner circuit reaches Google Cloud through a provider when the site is not in a colocation facility. Why the correct answer wins: A dedicated circuit gives predictable bandwidth over a private path at the colocation facility.
- **C:** Correct. In this case: A dedicated circuit gives predictable bandwidth over a private path at the colocation facility.
- **D:** Incorrect for this question. Cloud NAT lets private instances reach the internet without an external address. Why the correct answer wins: A dedicated circuit gives predictable bandwidth over a private path at the colocation facility.

### Question 21 — B

Answer: Apply a bucket retention policy with a locked period. A locked retention policy prevents deletion or a shorter period, which is the evidence an auditor tests. Local study-map skill 2.2 (Storage Configuration and Lifecycle), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 2 (managing and provisioning): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. A lifecycle rule acts on object age or class, so retention stops depending on a person. Why the correct answer wins: A locked retention policy prevents deletion or a shorter period, which is the evidence an auditor tests.
- **B:** Correct. In this case: A locked retention policy prevents deletion or a shorter period, which is the evidence an auditor tests.
- **C:** Incorrect for this question. Autoclass moves each object between classes as its access pattern changes, with no lifecycle rules to maintain. Why the correct answer wins: A locked retention policy prevents deletion or a shorter period, which is the evidence an auditor tests.
- **D:** Incorrect for this question. Versioning keeps a noncurrent copy when an object is overwritten or deleted. Why the correct answer wins: A locked retention policy prevents deletion or a shorter period, which is the evidence an auditor tests.

### Question 22 — D

Answer: Add a lifecycle rule that transitions and then deletes. A lifecycle rule transitions and then deletes on age, so retention stops depending on a person. A lifecycle rule acts on object age or class, so retention stops depending on a person. Local study-map skill 2.2 (Storage Configuration and Lifecycle), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 2 (managing and provisioning): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. The appliance ships the data physically when the network would take months to carry it. Why the correct answer wins: A lifecycle rule transitions and then deletes on age, so retention stops depending on a person.
- **B:** Incorrect for this question. Nearline suits data read about once a month and charges for early deletion. Why the correct answer wins: A lifecycle rule transitions and then deletes on age, so retention stops depending on a person.
- **C:** Incorrect for this question. Autoclass moves each object between classes as its access pattern changes, with no lifecycle rules to maintain. Why the correct answer wins: A lifecycle rule transitions and then deletes on age, so retention stops depending on a person.
- **D:** Correct. A lifecycle rule acts on object age or class, so retention stops depending on a person. In this case: A lifecycle rule transitions and then deletes on age, so retention stops depending on a person.

### Question 23 — B, D

Answers: Use Datastream for change data capture; Partition the table on the date column. Change data capture carries the ongoing changes, and partitioning limits each query to the dates it names. Datastream reads the source log and streams inserts, updates, and deletes with ordering preserved. Partitioning limits a query to the date ranges it names, so it scans less. Local study-map skill 2.2 (Storage Configuration and Lifecycle), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 2 (managing and provisioning): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. InsertAll is best-effort and only deduplicates on a provided insert ID, so duplicates can land. Why the correct answer wins: Change data capture carries the ongoing changes, and partitioning limits each query to the dates it names.
- **B:** Correct. Datastream reads the source log and streams inserts, updates, and deletes with ordering preserved. In this case: Change data capture carries the ongoing changes, and partitioning limits each query to the dates it names.
- **C:** Incorrect for this question. A replica offloads read traffic but lags the primary, so it is not a failover target. Why the correct answer wins: Change data capture carries the ongoing changes, and partitioning limits each query to the dates it names.
- **D:** Correct. Partitioning limits a query to the date ranges it names, so it scans less. In this case: Change data capture carries the ongoing changes, and partitioning limits each query to the dates it names.
- **E:** Incorrect for this question. A Dataproc cluster runs open-source Spark and Hadoop with jobs that need a persistent cluster. Why the correct answer wins: Change data capture carries the ongoing changes, and partitioning limits each query to the dates it names.

### Question 24 — A

Answer: Use VM Manager for OS patch compliance. VM Manager inventories and applies operating system patches across the fleet instead of manual runs. Local study-map skill 2.3 (Compute Provisioning and Patch Management), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 2 (managing and provisioning): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Correct. In this case: VM Manager inventories and applies operating system patches across the fleet instead of manual runs.
- **B:** Incorrect for this question. Spot capacity costs far less but can be reclaimed with 30 seconds of notice. Why the correct answer wins: VM Manager inventories and applies operating system patches across the fleet instead of manual runs.
- **C:** Incorrect for this question. Config Connector reconciles Google Cloud resources from Kubernetes manifests alongside the workloads. Why the correct answer wins: VM Manager inventories and applies operating system patches across the fleet instead of manual runs.
- **D:** Incorrect for this question. Cloud Build executes the pipeline steps in a managed, isolated worker with recorded provenance. Why the correct answer wins: VM Manager inventories and applies operating system patches across the fleet instead of manual runs.

### Question 25 — A, C

Answers: Run the batch tier on Spot VMs; Buy committed use discounts for the steady baseline. Spot capacity covers the burst, and a commitment discounts the capacity that runs constantly. Spot capacity costs far less but can be reclaimed with 30 seconds of notice. A one- or three-year commitment discounts the capacity that runs constantly, not the peaks. Local study-map skill 2.3 (Compute Provisioning and Patch Management), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 2 (managing and provisioning): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Correct. Spot capacity costs far less but can be reclaimed with 30 seconds of notice. In this case: Spot capacity covers the burst, and a commitment discounts the capacity that runs constantly.
- **B:** Incorrect for this question. Local SSD is the fastest ephemeral option and loses its data when the VM stops. Why the correct answer wins: Spot capacity covers the burst, and a commitment discounts the capacity that runs constantly.
- **C:** Correct. A one- or three-year commitment discounts the capacity that runs constantly, not the peaks. In this case: Spot capacity covers the burst, and a commitment discounts the capacity that runs constantly.
- **D:** Incorrect for this question. Showing owners their own spend changes behaviour more reliably than a central report. Why the correct answer wins: Spot capacity covers the burst, and a commitment discounts the capacity that runs constantly.
- **E:** Incorrect for this question. E2 shapes trade peak performance for a lower price on workloads that do not need it. Why the correct answer wins: Spot capacity covers the burst, and a commitment discounts the capacity that runs constantly.

### Question 26 — D

Answer: Enable Workload Identity Federation for GKE. Workload Identity binds a Kubernetes service account to an IAM identity, so pods hold no keys. Local study-map skill 2.4 (Container Orchestration), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 2 (managing and provisioning): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. An environment variable is visible to anything that can read the instance metadata or the process list. Why the correct answer wins: Workload Identity binds a Kubernetes service account to an IAM identity, so pods hold no keys.
- **B:** Incorrect for this question. A key file is a long-lived credential that works until it is noticed and revoked. Why the correct answer wins: Workload Identity binds a Kubernetes service account to an IAM identity, so pods hold no keys.
- **C:** Incorrect for this question. Federation exchanges an external token for short-lived Google Cloud credentials, so no key leaves the provider. Why the correct answer wins: Workload Identity binds a Kubernetes service account to an IAM identity, so pods hold no keys.
- **D:** Correct. In this case: Workload Identity binds a Kubernetes service account to an IAM identity, so pods hold no keys.

### Question 27 — B

Answer: Create private nodes with no external IP addresses. Private nodes reach Google APIs through Private Google Access from an internal address. Local study-map skill 2.4 (Container Orchestration), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 2 (managing and provisioning): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. Cloud NAT lets private instances reach the internet without an external address. Why the correct answer wins: Private nodes reach Google APIs through Private Google Access from an internal address.
- **B:** Correct. In this case: Private nodes reach Google APIs through Private Google Access from an internal address.
- **C:** Incorrect for this question. A zonal cluster keeps its control plane in one zone, so that zone loss takes the cluster with it. Why the correct answer wins: Private nodes reach Google APIs through Private Google Access from an internal address.
- **D:** Incorrect for this question. Sole tenancy keeps the physical host dedicated, which matters for licensing or isolation rules. Why the correct answer wins: Private nodes reach Google APIs through Private Google Access from an internal address.

### Question 28 — C

Answer: Set a minimum instance count on the Cloud Run service. A minimum instance count keeps warm capacity ready before the first request arrives. Keeping warm instances removes cold starts at the cost of paying for idle capacity. Local study-map skill 2.5 (Serverless Configuration), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 2 (managing and provisioning): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. The flexible environment runs a custom runtime on managed VMs but does not scale to zero. Why the correct answer wins: A minimum instance count keeps warm capacity ready before the first request arrives.
- **B:** Incorrect for this question. Serverless GPU attachment suits bursty inference where a reserved node would idle. Why the correct answer wins: A minimum instance count keeps warm capacity ready before the first request arrives.
- **C:** Correct. Keeping warm instances removes cold starts at the cost of paying for idle capacity. In this case: A minimum instance count keeps warm capacity ready before the first request arrives.
- **D:** Incorrect for this question. Concurrency packs more simultaneous requests into each instance before another is started. Why the correct answer wins: A minimum instance count keeps warm capacity ready before the first request arrives.

### Question 29 — A, D

Answers: Attach a Serverless VPC Access connector; Store the credential in Secret Manager. The connector gives a route to internal addresses, and Secret Manager holds and rotates the credential. The connector gives serverless workloads a route to internal addresses in the VPC. Secret Manager versions the secret, controls access by IAM, and can rotate it. Local study-map skill 2.5 (Serverless Configuration), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 2 (managing and provisioning): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Correct. Secret Manager versions the secret, controls access by IAM, and can rotate it. In this case: The connector gives a route to internal addresses, and Secret Manager holds and rotates the credential.
- **B:** Incorrect for this question. Cloud NAT lets private instances reach the internet without an external address. Why the correct answer wins: The connector gives a route to internal addresses, and Secret Manager holds and rotates the credential.
- **C:** Incorrect for this question. An environment variable is visible to anything that can read the instance metadata or the process list. Why the correct answer wins: The connector gives a route to internal addresses, and Secret Manager holds and rotates the credential.
- **D:** Correct. The connector gives serverless workloads a route to internal addresses in the VPC. In this case: The connector gives a route to internal addresses, and Secret Manager holds and rotates the credential.
- **E:** Incorrect for this question. A key file is a long-lived credential that works until it is noticed and revoked. Why the correct answer wins: The connector gives a route to internal addresses, and Secret Manager holds and rotates the credential.

### Question 30 — B

Answer: Manage the resources with Terraform. Terraform holds the desired state and produces a plan that a reviewer can read before apply. Terraform holds desired state in code, plans the diff, and applies it through a provider. Local study-map skill 2.6 (Infrastructure as Code), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 2 (managing and provisioning): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. Deployment Manager is the native but older templating service with no plan step. Why the correct answer wins: Terraform holds the desired state and produces a plan that a reviewer can read before apply.
- **B:** Correct. Terraform holds desired state in code, plans the diff, and applies it through a provider. In this case: Terraform holds the desired state and produces a plan that a reviewer can read before apply.
- **C:** Incorrect for this question. The CLI exposes every API as a command that can be scripted and logged. Why the correct answer wins: Terraform holds the desired state and produces a plan that a reviewer can read before apply.
- **D:** Incorrect for this question. Config Connector reconciles Google Cloud resources from Kubernetes manifests alongside the workloads. Why the correct answer wins: Terraform holds the desired state and produces a plan that a reviewer can read before apply.

### Question 31 — D

Answer: Create a remote state bucket with versioning → define modules per environment → run a plan in CI and require review → apply through the pipeline with a scoped service account. State is centralised before modules depend on it, plan review gates the apply, and the pipeline uses the least-privileged identity. Local study-map skill 2.6 (Infrastructure as Code), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 2 (managing and provisioning): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. Nothing can be planned before the modules and the state bucket exist. Why the correct answer wins: State is centralised before modules depend on it, plan review gates the apply, and the pipeline uses the least-privileged identity.
- **B:** Incorrect for this question. State must be created before the first apply, and review must precede it as well. Why the correct answer wins: State is centralised before modules depend on it, plan review gates the apply, and the pipeline uses the least-privileged identity.
- **C:** Incorrect for this question. Applying before state exists duplicates infrastructure, and a plan cannot gate an apply that already happened. Why the correct answer wins: State is centralised before modules depend on it, plan review gates the apply, and the pipeline uses the least-privileged identity.
- **D:** Correct. In this case: State is centralised before modules depend on it, plan review gates the apply, and the pipeline uses the least-privileged identity.

### Question 32 — A

Answer: Orchestrate the workflow in Agent Platform Pipelines. Agent Platform Pipelines runs each step as a container with lineage and caching, so a rerun is reproducible. Local study-map skill 2.7 (Agent Platform ML Workflows), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 2 (managing and provisioning): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Correct. In this case: Agent Platform Pipelines runs each step as a container with lineage and caching, so a rerun is reproducible.
- **B:** Incorrect for this question. A Dataproc cluster runs open-source Spark and Hadoop with jobs that need a persistent cluster. Why the correct answer wins: Agent Platform Pipelines runs each step as a container with lineage and caching, so a rerun is reproducible.
- **C:** Incorrect for this question. Batch prediction reads a file and writes predictions without holding serving capacity. Why the correct answer wins: Agent Platform Pipelines runs each step as a container with lineage and caching, so a rerun is reproducible.
- **D:** Incorrect for this question. Scheduler fires a job on a cron or App Engine schedule and retries on failure. Why the correct answer wins: Agent Platform Pipelines runs each step as a container with lineage and caching, so a rerun is reproducible.

### Question 33 — C

Answer: Curate and version the training data → train and evaluate the model in a pipeline → register the model and record its metrics → deploy to an endpoint with traffic splitting and model monitoring. Data precedes training, the registry holds the evaluated artifact, and monitoring starts with the serving endpoint. Local study-map skill 2.7 (Agent Platform ML Workflows), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 2 (managing and provisioning): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. Registration follows training, and training follows the data. Why the correct answer wins: Data precedes training, the registry holds the evaluated artifact, and monitoring starts with the serving endpoint.
- **B:** Incorrect for this question. Training without curated data and deploying without registration both skip a required stage. Why the correct answer wins: Data precedes training, the registry holds the evaluated artifact, and monitoring starts with the serving endpoint.
- **C:** Correct. In this case: Data precedes training, the registry holds the evaluated artifact, and monitoring starts with the serving endpoint.
- **D:** Incorrect for this question. Serving an untrained, unregistered model has nothing to deploy. Why the correct answer wins: Data precedes training, the registry holds the evaluated artifact, and monitoring starts with the serving endpoint.

### Question 34 — C

Answer: Select the model from Model Garden. Model Garden lists first-party and open models with their deployment options and licensing terms. Local study-map skill 2.8 (Prebuilt AI APIs and Model Garden), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 2 (managing and provisioning): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. Vertex AI Search returns grounded, cited results over private documents without a custom index. Why the correct answer wins: Model Garden lists first-party and open models with their deployment options and licensing terms.
- **B:** Incorrect for this question. Cloud Assist explains configurations and proposes changes inside the console with your permissions. Why the correct answer wins: Model Garden lists first-party and open models with their deployment options and licensing terms.
- **C:** Correct. In this case: Model Garden lists first-party and open models with their deployment options and licensing terms.
- **D:** Incorrect for this question. The kit gives code-first control over tools and state when a low-code builder is not enough. Why the correct answer wins: Model Garden lists first-party and open models with their deployment options and licensing terms.

### Question 35 — C

Answer: Define a custom role with only the required permissions. A custom role expresses least privilege when no predefined role matches the job exactly. Local study-map skill 3.1 (IAM and Least Privilege), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 3 (security and compliance): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. A condition narrows when a grant applies, for example to a time window or a resource prefix. Why the correct answer wins: A custom role expresses least privilege when no predefined role matches the job exactly.
- **B:** Incorrect for this question. A predefined role grants the curated permission set for one job at the level it is bound to. Why the correct answer wins: A custom role expresses least privilege when no predefined role matches the job exactly.
- **C:** Correct. In this case: A custom role expresses least privilege when no predefined role matches the job exactly.
- **D:** Incorrect for this question. A key file is a long-lived credential that works until it is noticed and revoked. Why the correct answer wins: A custom role expresses least privilege when no predefined role matches the job exactly.

### Question 36 — C

Answer: Grant service account impersonation instead of a key. Impersonation issues short-lived credentials and records who used the identity. Local study-map skill 3.1 (IAM and Least Privilege), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 3 (security and compliance): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. A key file is a long-lived credential that works until it is noticed and revoked. Why the correct answer wins: Impersonation issues short-lived credentials and records who used the identity.
- **B:** Incorrect for this question. An environment variable is visible to anything that can read the instance metadata or the process list. Why the correct answer wins: Impersonation issues short-lived credentials and records who used the identity.
- **C:** Correct. In this case: Impersonation issues short-lived credentials and records who used the identity.
- **D:** Incorrect for this question. Federation exchanges an external token for short-lived Google Cloud credentials, so no key leaves the provider. Why the correct answer wins: Impersonation issues short-lived credentials and records who used the identity.

### Question 37 — A, D

Answers: Add an IAM condition on the binding; Apply an IAM deny policy. The condition narrows when the grant applies, and the deny policy overrides every allow beneath it. A condition narrows when a grant applies, for example to a time window or a resource prefix. A deny policy overrides every allow beneath it, which is how an exception is made impossible. Local study-map skill 3.1 (IAM and Least Privilege), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 3 (security and compliance): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Correct. A deny policy overrides every allow beneath it, which is how an exception is made impossible. In this case: The condition narrows when the grant applies, and the deny policy overrides every allow beneath it.
- **B:** Incorrect for this question. A bastion is still an internet-facing host that must be patched and watched. Why the correct answer wins: The condition narrows when the grant applies, and the deny policy overrides every allow beneath it.
- **C:** Incorrect for this question. A predefined role grants the curated permission set for one job at the level it is bound to. Why the correct answer wins: The condition narrows when the grant applies, and the deny policy overrides every allow beneath it.
- **D:** Correct. A condition narrows when a grant applies, for example to a time window or a resource prefix. In this case: The condition narrows when the grant applies, and the deny policy overrides every allow beneath it.
- **E:** Incorrect for this question. Labels attribute spend in billing export; they do not grant or restrict access. Why the correct answer wins: The condition narrows when the grant applies, and the deny policy overrides every allow beneath it.

### Question 38 — C

Answer: Enforce the control with an organization policy constraint. An organization policy blocks the action across every project regardless of who holds the role. Local study-map skill 3.2 (Resource Hierarchy and Organization Policy), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 3 (security and compliance): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. A project is the boundary for quota, billing, and most IAM inheritance. Why the correct answer wins: An organization policy blocks the action across every project regardless of who holds the role.
- **B:** Incorrect for this question. A folder binding inherits to every project beneath it, so new projects start with the right access. Why the correct answer wins: An organization policy blocks the action across every project regardless of who holds the role.
- **C:** Correct. In this case: An organization policy blocks the action across every project regardless of who holds the role.
- **D:** Incorrect for this question. Labels attribute spend in billing export; they do not grant or restrict access. Why the correct answer wins: An organization policy blocks the action across every project regardless of who holds the role.

### Question 39 — A

Answer: Encrypt with a customer-managed key in Cloud KMS. A customer-managed key lets the bank rotate or disable the key and stop decryption at once. CMEK lets you control the key lifecycle, rotation, and the ability to revoke access to the data. Local study-map skill 3.3 (Encryption, CMEK, and Secrets), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 3 (security and compliance): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Correct. CMEK lets you control the key lifecycle, rotation, and the ability to revoke access to the data. In this case: A customer-managed key lets the bank rotate or disable the key and stop decryption at once.
- **B:** Incorrect for this question. CSEK is held by the caller and never stored by Google, so losing it loses the object. Why the correct answer wins: A customer-managed key lets the bank rotate or disable the key and stop decryption at once.
- **C:** Incorrect for this question. Secret Manager versions the secret, controls access by IAM, and can rotate it. Why the correct answer wins: A customer-managed key lets the bank rotate or disable the key and stop decryption at once.
- **D:** Incorrect for this question. Cloud HSM keeps the key material in a hardware module that meets FIPS 140-2 level 3. Why the correct answer wins: A customer-managed key lets the bank rotate or disable the key and stop decryption at once.

### Question 40 — A, C

Answers: Create the key ring in the same region as the data; Set an automatic rotation period on the key. The key ring's location fixes where the key material lives, and automatic rotation issues a new version on schedule. A regional key cannot encrypt a resource in another region, which is why residency drives key placement. Rotation issues a new key version on schedule and keeps old versions for decryption. Local study-map skill 3.3 (Encryption, CMEK, and Secrets), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 3 (security and compliance): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Correct. A regional key cannot encrypt a resource in another region, which is why residency drives key placement. In this case: The key ring's location fixes where the key material lives, and automatic rotation issues a new version on schedule.
- **B:** Incorrect for this question. An environment variable is visible to anything that can read the instance metadata or the process list. Why the correct answer wins: The key ring's location fixes where the key material lives, and automatic rotation issues a new version on schedule.
- **C:** Correct. Rotation issues a new key version on schedule and keeps old versions for decryption. In this case: The key ring's location fixes where the key material lives, and automatic rotation issues a new version on schedule.
- **D:** Incorrect for this question. Cloud HSM keeps the key material in a hardware module that meets FIPS 140-2 level 3. Why the correct answer wins: The key ring's location fixes where the key material lives, and automatic rotation issues a new version on schedule.
- **E:** Incorrect for this question. CSEK is held by the caller and never stored by Google, so losing it loses the object. Why the correct answer wins: The key ring's location fixes where the key material lives, and automatic rotation issues a new version on schedule.

### Question 41 — A

Answer: Put the projects inside a VPC Service Controls perimeter. A service perimeter blocks data movement out of the covered services even for a principal with the role. Local study-map skill 3.4 (VPC Service Controls and Network Security), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 3 (security and compliance): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Correct. In this case: A service perimeter blocks data movement out of the covered services even for a principal with the role.
- **B:** Incorrect for this question. A policy above the project applies to every current and future network beneath it. Why the correct answer wins: A service perimeter blocks data movement out of the covered services even for a principal with the role.
- **C:** Incorrect for this question. A deny policy overrides every allow beneath it, which is how an exception is made impossible. Why the correct answer wins: A service perimeter blocks data movement out of the covered services even for a principal with the role.
- **D:** Incorrect for this question. Labels attribute spend in billing export; they do not grant or restrict access. Why the correct answer wins: A service perimeter blocks data movement out of the covered services even for a principal with the role.

### Question 42 — C

Answer: Run the perimeter in dry-run mode first. Dry-run mode logs the requests that would be blocked without breaking a legitimate flow. Local study-map skill 3.4 (VPC Service Controls and Network Security), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 3 (security and compliance): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. The perimeter blocks data movement out of the services it covers even for a principal with the role. Why the correct answer wins: Dry-run mode logs the requests that would be blocked without breaking a legitimate flow.
- **B:** Incorrect for this question. An aggregated sink collects logs from every project in the organization into one destination. Why the correct answer wins: Dry-run mode logs the requests that would be blocked without breaking a legitimate flow.
- **C:** Correct. In this case: Dry-run mode logs the requests that would be blocked without breaking a legitimate flow.
- **D:** Incorrect for this question. Cloud Armor filters requests at the edge with allow and deny rules and adaptive protection. Why the correct answer wins: Dry-run mode logs the requests that would be blocked without breaking a legitimate flow.

### Question 43 — B

Answer: Put Identity-Aware Proxy in front of the application. Identity-Aware Proxy authenticates and authorises each request before it reaches the backend. Local study-map skill 3.5 (Secure Remote Access and Zero Trust), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 3 (security and compliance): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. A bastion is still an internet-facing host that must be patched and watched. Why the correct answer wins: Identity-Aware Proxy authenticates and authorises each request before it reaches the backend.
- **B:** Correct. In this case: Identity-Aware Proxy authenticates and authorises each request before it reaches the backend.
- **C:** Incorrect for this question. Private Google Access reaches Google APIs from an internal address without a proxy or a NAT gateway. Why the correct answer wins: Identity-Aware Proxy authenticates and authorises each request before it reaches the backend.
- **D:** Incorrect for this question. Cloud NAT lets private instances reach the internet without an external address. Why the correct answer wins: Identity-Aware Proxy authenticates and authorises each request before it reaches the backend.

### Question 44 — C, D

Answers: Use OS Login for administrative SSH; Use Chrome Enterprise Premium for the workforce. OS Login ties the SSH identity to the IAM account, and context-aware access evaluates the device. OS Login ties the SSH identity to the IAM account and records the session. Context-aware access evaluates device and identity signals for every application, not just the network. Local study-map skill 3.5 (Secure Remote Access and Zero Trust), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 3 (security and compliance): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. A key file is a long-lived credential that works until it is noticed and revoked. Why the correct answer wins: OS Login ties the SSH identity to the IAM account, and context-aware access evaluates the device.
- **B:** Incorrect for this question. Cloud NAT lets private instances reach the internet without an external address. Why the correct answer wins: OS Login ties the SSH identity to the IAM account, and context-aware access evaluates the device.
- **C:** Correct. OS Login ties the SSH identity to the IAM account and records the session. In this case: OS Login ties the SSH identity to the IAM account, and context-aware access evaluates the device.
- **D:** Correct. Context-aware access evaluates device and identity signals for every application, not just the network. In this case: OS Login ties the SSH identity to the IAM account, and context-aware access evaluates the device.
- **E:** Incorrect for this question. A bastion is still an internet-facing host that must be patched and watched. Why the correct answer wins: OS Login ties the SSH identity to the IAM account, and context-aware access evaluates the device.

### Question 45 — C

Answer: Require Binary Authorization attestations. The admission controller rejects images without a valid attestation, so an unverified build cannot start. Only images with a valid attestation from a trusted builder may deploy. Local study-map skill 3.6 (Software Supply Chain Security), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 3 (security and compliance): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. Scanning reports known vulnerabilities in the image layers before deployment. Why the correct answer wins: The admission controller rejects images without a valid attestation, so an unverified build cannot start.
- **B:** Incorrect for this question. Artifact Registry holds the image with IAM-scoped access and vulnerability metadata. Why the correct answer wins: The admission controller rejects images without a valid attestation, so an unverified build cannot start.
- **C:** Correct. Only images with a valid attestation from a trusted builder may deploy. In this case: The admission controller rejects images without a valid attestation, so an unverified build cannot start.
- **D:** Incorrect for this question. Network policy restricts pod-to-pod traffic inside the cluster, which a firewall rule cannot see. Why the correct answer wins: The admission controller rejects images without a valid attestation, so an unverified build cannot start.

### Question 46 — B

Answer: Screen prompts and responses with Model Armor. Model Armor detects prompt injection and unsafe content before and after the model call. Local study-map skill 3.7 (Securing AI Workloads), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 3 (security and compliance): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. Sensitive Data Protection finds and redacts, tokenizes, or format-preservingly encrypts sensitive fields. Why the correct answer wins: Model Armor detects prompt injection and unsafe content before and after the model call.
- **B:** Correct. In this case: Model Armor detects prompt injection and unsafe content before and after the model call.
- **C:** Incorrect for this question. The access level adds device and network conditions to the perimeter rule. Why the correct answer wins: Model Armor detects prompt injection and unsafe content before and after the model call.
- **D:** Incorrect for this question. Security Command Center aggregates misconfiguration and threat findings across the organization. Why the correct answer wins: Model Armor detects prompt injection and unsafe content before and after the model call.

### Question 47 — D

Answer: De-identify the data with Sensitive Data Protection. Sensitive Data Protection finds and redacts or tokenizes the sensitive fields before they are stored. Sensitive Data Protection finds and redacts, tokenizes, or format-preservingly encrypts sensitive fields. Local study-map skill 3.7 (Securing AI Workloads), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 3 (security and compliance): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. Model Armor detects prompt injection, jailbreak attempts, and unsafe content before and after the model call. Why the correct answer wins: Sensitive Data Protection finds and redacts or tokenizes the sensitive fields before they are stored.
- **B:** Incorrect for this question. Model Garden lists first-party and open models with deployment options and licensing. Why the correct answer wins: Sensitive Data Protection finds and redacts or tokenizes the sensitive fields before they are stored.
- **C:** Incorrect for this question. Vertex AI Search returns grounded, cited results over private documents without a custom index. Why the correct answer wins: Sensitive Data Protection finds and redacts or tokenizes the sensitive fields before they are stored.
- **D:** Correct. Sensitive Data Protection finds and redacts, tokenizes, or format-preservingly encrypts sensitive fields. In this case: Sensitive Data Protection finds and redacts or tokenizes the sensitive fields before they are stored.

### Question 48 — C

Answer: Enable data access audit logs for the services in scope → create a locked log bucket with the required retention → route the logs with an aggregated sink → query and export the evidence for the auditor. Logs must be enabled before they can be routed, and retention is fixed on the bucket before the sink writes to it. Local study-map skill 3.8 (Compliance, Residency, and Audit Logging), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 3 (security and compliance): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. A sink that is created last is needed before any evidence can be queried from the destination. Why the correct answer wins: Logs must be enabled before they can be routed, and retention is fixed on the bucket before the sink writes to it.
- **B:** Incorrect for this question. A sink without a destination bucket or enabled logs captures nothing. Why the correct answer wins: Logs must be enabled before they can be routed, and retention is fixed on the bucket before the sink writes to it.
- **C:** Correct. In this case: Logs must be enabled before they can be routed, and retention is fixed on the bucket before the sink writes to it.
- **D:** Incorrect for this question. There is no evidence to query before logging and routing exist. Why the correct answer wins: Logs must be enabled before they can be routed, and retention is fixed on the bucket before the sink writes to it.

### Question 49 — D

Answer: Adopt trunk-based development with short-lived branches. Short-lived branches reduce merge conflict and keep the mainline deployable. Local study-map skill 4.1 (SDLC and CI/CD Design), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 4 (analyzing and optimizing): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. A rolling replacement keeps capacity but exposes the whole fleet before the signal is trusted. Why the correct answer wins: Short-lived branches reduce merge conflict and keep the mainline deployable.
- **B:** Incorrect for this question. The flag separates deployment from release, so the code can ship dark and be turned off instantly. Why the correct answer wins: Short-lived branches reduce merge conflict and keep the mainline deployable.
- **C:** Incorrect for this question. A rebuild produces a different artifact, so the test result no longer applies to production. Why the correct answer wins: Short-lived branches reduce merge conflict and keep the mainline deployable.
- **D:** Correct. In this case: Short-lived branches reduce merge conflict and keep the mainline deployable.

### Question 50 — B, D

Answers: Cover the change with unit, integration, and a few end-to-end tests; Add a contract test on the API. The pyramid puts test volume where it is cheap, and a contract test fails the build on a breaking change. The pyramid puts volume where it is cheap and keeps end-to-end tests for the critical paths. The contract test fails the build when a breaking change reaches a consumer. Local study-map skill 4.1 (SDLC and CI/CD Design), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 4 (analyzing and optimizing): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. The load test measures the system at the concurrency the business expects, before launch. Why the correct answer wins: The pyramid puts test volume where it is cheap, and a contract test fails the build on a breaking change.
- **B:** Correct. The pyramid puts volume where it is cheap and keeps end-to-end tests for the critical paths. In this case: The pyramid puts test volume where it is cheap, and a contract test fails the build on a breaking change.
- **C:** Incorrect for this question. The experiment proves the failover path works while the impact is controlled. Why the correct answer wins: The pyramid puts test volume where it is cheap, and a contract test fails the build on a breaking change.
- **D:** Correct. The contract test fails the build when a breaking change reaches a consumer. In this case: The pyramid puts test volume where it is cheap, and a contract test fails the build on a breaking change.
- **E:** Incorrect for this question. An independent test attempts the attack the design claims to prevent. Why the correct answer wins: The pyramid puts test volume where it is cheap, and a contract test fails the build on a breaking change.

### Question 51 — D

Answer: Promote the same tested artifact between environments. Promotion moves one immutable artifact forward, so the tested build is the deployed build. Promotion moves one immutable artifact forward, so what was tested is what runs. Local study-map skill 4.1 (SDLC and CI/CD Design), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 4 (analyzing and optimizing): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. A budget alerts on spend but does not stop it. Why the correct answer wins: Promotion moves one immutable artifact forward, so the tested build is the deployed build.
- **B:** Incorrect for this question. A rolling replacement keeps capacity but exposes the whole fleet before the signal is trusted. Why the correct answer wins: Promotion moves one immutable artifact forward, so the tested build is the deployed build.
- **C:** Incorrect for this question. A rebuild produces a different artifact, so the test result no longer applies to production. Why the correct answer wins: Promotion moves one immutable artifact forward, so the tested build is the deployed build.
- **D:** Correct. Promotion moves one immutable artifact forward, so what was tested is what runs. In this case: Promotion moves one immutable artifact forward, so the tested build is the deployed build.

### Question 52 — D

Answer: Query the entries in Cloud Logging. Logging holds the event text and structured fields that explain what happened at that moment. Local study-map skill 4.2 (Root Cause Analysis), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 4 (analyzing and optimizing): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. The dashboard gives the team one view of the same signals during an incident. Why the correct answer wins: Logging holds the event text and structured fields that explain what happened at that moment.
- **B:** Incorrect for this question. Recommender reports idle and over-provisioned resources with the estimated saving. Why the correct answer wins: Logging holds the event text and structured fields that explain what happened at that moment.
- **C:** Incorrect for this question. Trace shows how one request spent its time across services and calls. Why the correct answer wins: Logging holds the event text and structured fields that explain what happened at that moment.
- **D:** Correct. In this case: Logging holds the event text and structured fields that explain what happened at that moment.

### Question 53 — D

Answer: Run a load test at the expected peak. The load test measures the system at the concurrency the business expects, before launch. Local study-map skill 4.3 (Testing and Validation), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 4 (analyzing and optimizing): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. The pyramid puts volume where it is cheap and keeps end-to-end tests for the critical paths. Why the correct answer wins: The load test measures the system at the concurrency the business expects, before launch.
- **B:** Incorrect for this question. An independent test attempts the attack the design claims to prevent. Why the correct answer wins: The load test measures the system at the concurrency the business expects, before launch.
- **C:** Incorrect for this question. The experiment proves the failover path works while the impact is controlled. Why the correct answer wins: The load test measures the system at the concurrency the business expects, before launch.
- **D:** Correct. In this case: The load test measures the system at the concurrency the business expects, before launch.

### Question 54 — D

Answer: Run a pilot-light standby. Only core data and configuration stay warm, so recovery starts the compute and takes minutes. Local study-map skill 4.4 (Disaster Recovery and Business Continuity), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 4 (analyzing and optimizing): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. A running but smaller copy recovers in a short window at a continuous cost. Why the correct answer wins: Only core data and configuration stay warm, so recovery starts the compute and takes minutes.
- **B:** Incorrect for this question. Restoring from backup is the cheapest option and the slowest to recover. Why the correct answer wins: Only core data and configuration stay warm, so recovery starts the compute and takes minutes.
- **C:** Incorrect for this question. Both regions serve traffic, so a regional loss is absorbed without a failover decision. Why the correct answer wins: Only core data and configuration stay warm, so recovery starts the compute and takes minutes.
- **D:** Correct. In this case: Only core data and configuration stay warm, so recovery starts the compute and takes minutes.

### Question 55 — B

Answer: Detect the symptom through an alert → contain the impact and restore service → isolate the root cause from logs, traces, and metrics → apply the permanent fix and write the postmortem. Service recovery comes before deep analysis, and the postmortem follows the fix. Local study-map skill 4.4 (Disaster Recovery and Business Continuity), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 4 (analyzing and optimizing): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. A postmortem cannot be written before the incident has happened and been resolved. Why the correct answer wins: Service recovery comes before deep analysis, and the postmortem follows the fix.
- **B:** Correct. In this case: Service recovery comes before deep analysis, and the postmortem follows the fix.
- **C:** Incorrect for this question. Service cannot be restored before the alert fires, and the root cause is isolated before the postmortem. Why the correct answer wins: Service recovery comes before deep analysis, and the postmortem follows the fix.
- **D:** Incorrect for this question. Detection precedes analysis, and the postmortem follows restoration rather than preceding it. Why the correct answer wins: Service recovery comes before deep analysis, and the postmortem follows the fix.

### Question 56 — C

Answer: Build a three-year total cost of ownership model. The model compares run cost, people cost, and exit cost rather than the monthly bill alone. Local study-map skill 4.5 (Cost Optimization), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 4 (analyzing and optimizing): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. Recommender reports idle and over-provisioned resources with the estimated saving. Why the correct answer wins: The model compares run cost, people cost, and exit cost rather than the monthly bill alone.
- **B:** Incorrect for this question. A budget alerts on spend but does not stop it. Why the correct answer wins: The model compares run cost, people cost, and exit cost rather than the monthly bill alone.
- **C:** Correct. In this case: The model compares run cost, people cost, and exit cost rather than the monthly bill alone.
- **D:** Incorrect for this question. The export attributes cost to the team and service that caused it. Why the correct answer wins: The model compares run cost, people cost, and exit cost rather than the monthly bill alone.

### Question 57 — B

Answer: Act on the Recommender suggestions. Recommender reports idle and over-provisioned resources with the estimated saving for each. Local study-map skill 4.5 (Cost Optimization), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 4 (analyzing and optimizing): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. A quota limit is a hard ceiling that no autoscaler can exceed. Why the correct answer wins: Recommender reports idle and over-provisioned resources with the estimated saving for each.
- **B:** Correct. In this case: Recommender reports idle and over-provisioned resources with the estimated saving for each.
- **C:** Incorrect for this question. The export attributes cost to the team and service that caused it. Why the correct answer wins: Recommender reports idle and over-provisioned resources with the estimated saving for each.
- **D:** Incorrect for this question. Labels attribute spend in billing export; they do not grant or restrict access. Why the correct answer wins: Recommender reports idle and over-provisioned resources with the estimated saving for each.

### Question 58 — C

Answer: Inspect the query plan and bytes processed → partition and cluster the table on the filter columns → rewrite the query to prune partitions → measure the new slot time and bytes scanned. The plan identifies the problem, the physical design supports pruning, and only a measurement proves improvement. Local study-map skill 4.5 (Cost Optimization), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 4 (analyzing and optimizing): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. Partitioning last ignores what the plan and the rewrite revealed. Why the correct answer wins: The plan identifies the problem, the physical design supports pruning, and only a measurement proves improvement.
- **B:** Incorrect for this question. The plan is the evidence that drives both the rewrite and the physical design. Why the correct answer wins: The plan identifies the problem, the physical design supports pruning, and only a measurement proves improvement.
- **C:** Correct. In this case: The plan identifies the problem, the physical design supports pruning, and only a measurement proves improvement.
- **D:** Incorrect for this question. Measuring before any change establishes no baseline against the plan. Why the correct answer wins: The plan identifies the problem, the physical design supports pruning, and only a measurement proves improvement.

### Question 59 — A

Answer: Agree the decision rights with the stakeholders. Naming who decides each trade-off prevents the design being reopened late in delivery. Local study-map skill 4.6 (Stakeholder and Change Management), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 4 (analyzing and optimizing): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Correct. In this case: Naming who decides each trade-off prevents the design being reopened late in delivery.
- **B:** Incorrect for this question. A catalog entry gives teams a pre-approved, policy-compliant way to request the resource. Why the correct answer wins: Naming who decides each trade-off prevents the design being reopened late in delivery.
- **C:** Incorrect for this question. The runbook records the diagnostic steps so the response does not depend on who is awake. Why the correct answer wins: Naming who decides each trade-off prevents the design being reopened late in delivery.
- **D:** Incorrect for this question. The board reviews risk and timing for changes that affect regulated or shared systems. Why the correct answer wins: Naming who decides each trade-off prevents the design being reopened late in delivery.

### Question 60 — A

Answer: Publish a service catalog entry with an approved template. A catalog entry gives teams a pre-approved, policy-compliant way to request the resource. Local study-map skill 4.7 (Service Catalog and Provisioning), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 4 (analyzing and optimizing): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Correct. In this case: A catalog entry gives teams a pre-approved, policy-compliant way to request the resource.
- **B:** Incorrect for this question. An organization policy blocks the action across every project regardless of who holds the role. Why the correct answer wins: A catalog entry gives teams a pre-approved, policy-compliant way to request the resource.
- **C:** Incorrect for this question. Terraform holds desired state in code, plans the diff, and applies it through a provider. Why the correct answer wins: A catalog entry gives teams a pre-approved, policy-compliant way to request the resource.
- **D:** Incorrect for this question. Labels attribute spend in billing export; they do not grant or restrict access. Why the correct answer wins: A catalog entry gives teams a pre-approved, policy-compliant way to request the resource.

### Question 61 — A

Answer: Roll out a canary to a small share of traffic. A canary limits the blast radius while the error and latency signals are compared. Local study-map skill 5.1 (Deployment and Release Strategy), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 5 (managing implementation): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Correct. In this case: A canary limits the blast radius while the error and latency signals are compared.
- **B:** Incorrect for this question. Two identical environments let the switch be reversed instantly if the new one misbehaves. Why the correct answer wins: A canary limits the blast radius while the error and latency signals are compared.
- **C:** Incorrect for this question. A rolling replacement keeps capacity but exposes the whole fleet before the signal is trusted. Why the correct answer wins: A canary limits the blast radius while the error and latency signals are compared.
- **D:** Incorrect for this question. The flag separates deployment from release, so the code can ship dark and be turned off instantly. Why the correct answer wins: A canary limits the blast radius while the error and latency signals are compared.

### Question 62 — D

Answer: Deploy blue/green with a traffic switch. Two identical environments let the switch be reversed instantly if the new one misbehaves. Local study-map skill 5.1 (Deployment and Release Strategy), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 5 (managing implementation): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. A rolling replacement keeps capacity but exposes the whole fleet before the signal is trusted. Why the correct answer wins: Two identical environments let the switch be reversed instantly if the new one misbehaves.
- **B:** Incorrect for this question. A canary limits the blast radius while the error and latency signals are compared. Why the correct answer wins: Two identical environments let the switch be reversed instantly if the new one misbehaves.
- **C:** Incorrect for this question. The flag separates deployment from release, so the code can ship dark and be turned off instantly. Why the correct answer wins: Two identical environments let the switch be reversed instantly if the new one misbehaves.
- **D:** Correct. In this case: Two identical environments let the switch be reversed instantly if the new one misbehaves.

### Question 63 — D

Answer: Keep the previous image digest ready for rollback. A pinned digest restores the exact artifact that was known good rather than a fresh build. Local study-map skill 5.1 (Deployment and Release Strategy), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 5 (managing implementation): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. A rebuild produces a different artifact, so the test result no longer applies to production. Why the correct answer wins: A pinned digest restores the exact artifact that was known good rather than a fresh build.
- **B:** Incorrect for this question. Promotion moves one immutable artifact forward, so what was tested is what runs. Why the correct answer wins: A pinned digest restores the exact artifact that was known good rather than a fresh build.
- **C:** Incorrect for this question. A budget alerts on spend but does not stop it. Why the correct answer wins: A pinned digest restores the exact artifact that was known good rather than a fresh build.
- **D:** Correct. In this case: A pinned digest restores the exact artifact that was known good rather than a fresh build.

### Question 64 — C

Answer: Build an immutable image and record its digest → deploy the new revision without traffic → shift a small traffic percentage and watch error and latency signals → promote to full traffic or roll back to the pinned digest. The artifact is fixed before traffic moves, and the decision to promote follows observed signals. Local study-map skill 5.1 (Deployment and Release Strategy), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 5 (managing implementation): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. Nothing can be watched before the revision exists, and the image precedes the deployment. Why the correct answer wins: The artifact is fixed before traffic moves, and the decision to promote follows observed signals.
- **B:** Incorrect for this question. Full traffic before any canary step turns the first failure into an outage. Why the correct answer wins: The artifact is fixed before traffic moves, and the decision to promote follows observed signals.
- **C:** Correct. In this case: The artifact is fixed before traffic moves, and the decision to promote follows observed signals.
- **D:** Incorrect for this question. Promoting before the canary step skips the signal that justifies promotion. Why the correct answer wins: The artifact is fixed before traffic moves, and the decision to promote follows observed signals.

### Question 65 — C

Answer: Publish the API through Apigee. Apigee adds quotas, keys, mediation, and analytics at the gateway for each consumer. Local study-map skill 5.2 (API Management), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 5 (managing implementation): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. Cloud Armor filters requests at the edge with allow and deny rules and adaptive protection. Why the correct answer wins: Apigee adds quotas, keys, mediation, and analytics at the gateway for each consumer.
- **B:** Incorrect for this question. API Gateway fronts a Cloud Run or functions backend with a managed OpenAPI definition. Why the correct answer wins: Apigee adds quotas, keys, mediation, and analytics at the gateway for each consumer.
- **C:** Correct. In this case: Apigee adds quotas, keys, mediation, and analytics at the gateway for each consumer.
- **D:** Incorrect for this question. Endpoints validates and monitors an API described by an OpenAPI or gRPC spec. Why the correct answer wins: Apigee adds quotas, keys, mediation, and analytics at the gateway for each consumer.

### Question 66 — B, D

Answers: Publish a versioning and deprecation policy; Add a contract test on the API. The policy states when a version is removed, and the contract test stops a breaking change reaching consumers. The policy tells consumers how long a version lives and when it is removed. The contract test fails the build when a breaking change reaches a consumer. Local study-map skill 5.2 (API Management), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 5 (managing implementation): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. A rebuild produces a different artifact, so the test result no longer applies to production. Why the correct answer wins: The policy states when a version is removed, and the contract test stops a breaking change reaching consumers.
- **B:** Correct. The contract test fails the build when a breaking change reaches a consumer. In this case: The policy states when a version is removed, and the contract test stops a breaking change reaching consumers.
- **C:** Incorrect for this question. An API key identifies a project and does not authorise a user, so it cannot express least privilege. Why the correct answer wins: The policy states when a version is removed, and the contract test stops a breaking change reaching consumers.
- **D:** Correct. The policy tells consumers how long a version lives and when it is removed. In this case: The policy states when a version is removed, and the contract test stops a breaking change reaching consumers.
- **E:** Incorrect for this question. A rolling replacement keeps capacity but exposes the whole fleet before the signal is trusted. Why the correct answer wins: The policy states when a version is removed, and the contract test stops a breaking change reaching consumers.

### Question 67 — C

Answer: Copy the files with Storage Transfer Service. The service runs scheduled, filtered transfers from another cloud or an HTTP source. The service moves object data between buckets or clouds on a schedule. Local study-map skill 5.3 (Data and System Migration Tooling), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 5 (managing implementation): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. Migration Center inventories the servers and estimates the target size and cost. Why the correct answer wins: The service runs scheduled, filtered transfers from another cloud or an HTTP source.
- **B:** Incorrect for this question. The tool rewrites a VM workload into a container image so it can run on GKE. Why the correct answer wins: The service runs scheduled, filtered transfers from another cloud or an HTTP source.
- **C:** Correct. The service moves object data between buckets or clouds on a schedule. In this case: The service runs scheduled, filtered transfers from another cloud or an HTTP source.
- **D:** Incorrect for this question. The appliance ships the data physically when the network would take months to carry it. Why the correct answer wins: The service runs scheduled, filtered transfers from another cloud or an HTTP source.

### Question 68 — C

Answer: Migrate the database with Database Migration Service. The service replicates continuously and cuts over in a short window with the source still running. Local study-map skill 5.3 (Data and System Migration Tooling), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 5 (managing implementation): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. The service moves object data between buckets or clouds on a schedule. Why the correct answer wins: The service replicates continuously and cuts over in a short window with the source still running.
- **B:** Incorrect for this question. Datastream reads the source log and streams inserts, updates, and deletes with ordering preserved. Why the correct answer wins: The service replicates continuously and cuts over in a short window with the source still running.
- **C:** Correct. In this case: The service replicates continuously and cuts over in a short window with the source still running.
- **D:** Incorrect for this question. The service runs scheduled loads from SaaS sources and other clouds into BigQuery. Why the correct answer wins: The service replicates continuously and cuts over in a short window with the source still running.

### Question 69 — D

Answer: Inventory the estate in Migration Center → group servers into dependency-based waves → validate a pilot wave in the target landing zone → cut over wave by wave and decommission the source. Inventory precedes grouping, a pilot proves the landing zone, and decommissioning follows a completed cutover. Local study-map skill 5.3 (Data and System Migration Tooling), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 5 (managing implementation): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. Decommissioning first removes the evidence and the rollback option for every later step. Why the correct answer wins: Inventory precedes grouping, a pilot proves the landing zone, and decommissioning follows a completed cutover.
- **B:** Incorrect for this question. A pilot cannot be chosen before the inventory and the wave grouping. Why the correct answer wins: Inventory precedes grouping, a pilot proves the landing zone, and decommissioning follows a completed cutover.
- **C:** Incorrect for this question. Waves cannot be grouped before the inventory, and decommissioning before validation destroys the rollback path. Why the correct answer wins: Inventory precedes grouping, a pilot proves the landing zone, and decommissioning follows a completed cutover.
- **D:** Correct. In this case: Inventory precedes grouping, a pilot proves the landing zone, and decommissioning follows a completed cutover.

### Question 70 — C

Answer: Run the emulator in the pipeline. The emulator provides a local endpoint for tests without a billable cloud resource. Local study-map skill 5.4 (Programmatic Access and Emulators), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 5 (managing implementation): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. The CLI exposes every API as a command that can be scripted and logged. Why the correct answer wins: The emulator provides a local endpoint for tests without a billable cloud resource.
- **B:** Incorrect for this question. The bq tool runs jobs and manages datasets from a terminal or a script. Why the correct answer wins: The emulator provides a local endpoint for tests without a billable cloud resource.
- **C:** Correct. In this case: The emulator provides a local endpoint for tests without a billable cloud resource.
- **D:** Incorrect for this question. Cloud Shell provides an authenticated terminal and editor with no local installation. Why the correct answer wins: The emulator provides a local endpoint for tests without a billable cloud resource.

### Question 71 — A

Answer: Use the Google API client library with retries. The client library applies the recommended retry and backoff behaviour for the API. Local study-map skill 5.5 (Client Libraries and API Practices), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 5 (managing implementation): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Correct. In this case: The client library applies the recommended retry and backoff behaviour for the API.
- **B:** Incorrect for this question. An API key identifies a project and does not authorise a user, so it cannot express least privilege. Why the correct answer wins: The client library applies the recommended retry and backoff behaviour for the API.
- **C:** Incorrect for this question. Impersonation issues a short-lived token so the test runs as the real workload identity. Why the correct answer wins: The client library applies the recommended retry and backoff behaviour for the API.
- **D:** Incorrect for this question. The CLI exposes every API as a command that can be scripted and logged. Why the correct answer wins: The client library applies the recommended retry and backoff behaviour for the API.

### Question 72 — D

Answer: Define dashboards and metrics in Cloud Monitoring. Monitoring collects the platform and application metrics that the first alert will use. Local study-map skill 6.1 (Observability Design), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 6 (solution and operations excellence): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. Logging holds the event text and structured fields that explain what happened at a moment. Why the correct answer wins: Monitoring collects the platform and application metrics that the first alert will use.
- **B:** Incorrect for this question. An SLO ties the alert to the promise the users care about rather than to a raw resource threshold. Why the correct answer wins: Monitoring collects the platform and application metrics that the first alert will use.
- **C:** Incorrect for this question. The dashboard gives the team one view of the same signals during an incident. Why the correct answer wins: Monitoring collects the platform and application metrics that the first alert will use.
- **D:** Correct. In this case: Monitoring collects the platform and application metrics that the first alert will use.

### Question 73 — A

Answer: Install the Ops Agent on the instances. The Ops Agent ships host metrics and application logs to Monitoring and Logging. Local study-map skill 6.1 (Observability Design), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 6 (solution and operations excellence): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Correct. In this case: The Ops Agent ships host metrics and application logs to Monitoring and Logging.
- **B:** Incorrect for this question. Trace shows how one request spent its time across services and calls. Why the correct answer wins: The Ops Agent ships host metrics and application logs to Monitoring and Logging.
- **C:** Incorrect for this question. Profiler samples the running code and attributes CPU and heap to the functions responsible. Why the correct answer wins: The Ops Agent ships host metrics and application logs to Monitoring and Logging.
- **D:** Incorrect for this question. Error Reporting clusters recurring stack traces so a new failure is not lost in the log volume. Why the correct answer wins: The Ops Agent ships host metrics and application logs to Monitoring and Logging.

### Question 74 — A, D

Answers: Add an uptime check from several regions; Inspect the trace waterfall in Cloud Trace. The uptime check measures availability externally, and the trace shows where the request spent its time. The check measures availability from outside, which no internal metric can prove. Trace shows how one request spent its time across services and calls. Local study-map skill 6.1 (Observability Design), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 6 (solution and operations excellence): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Correct. The check measures availability from outside, which no internal metric can prove. In this case: The uptime check measures availability externally, and the trace shows where the request spent its time.
- **B:** Incorrect for this question. The dashboard gives the team one view of the same signals during an incident. Why the correct answer wins: The uptime check measures availability externally, and the trace shows where the request spent its time.
- **C:** Incorrect for this question. Recommender reports idle and over-provisioned resources with the estimated saving. Why the correct answer wins: The uptime check measures availability externally, and the trace shows where the request spent its time.
- **D:** Correct. Trace shows how one request spent its time across services and calls. In this case: The uptime check measures availability externally, and the trace shows where the request spent its time.
- **E:** Incorrect for this question. An SLO ties the alert to the promise the users care about rather than to a raw resource threshold. Why the correct answer wins: The uptime check measures availability externally, and the trace shows where the request spent its time.

### Question 75 — A

Answer: Define an SLO with an error budget. An SLO ties the alert to the user promise rather than to a raw resource threshold. Local study-map skill 6.2 (Alerting and Service Level Objectives), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 6 (solution and operations excellence): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Correct. In this case: An SLO ties the alert to the user promise rather than to a raw resource threshold.
- **B:** Incorrect for this question. The dashboard gives the team one view of the same signals during an incident. Why the correct answer wins: An SLO ties the alert to the user promise rather than to a raw resource threshold.
- **C:** Incorrect for this question. The check measures availability from outside, which no internal metric can prove. Why the correct answer wins: An SLO ties the alert to the user promise rather than to a raw resource threshold.
- **D:** Incorrect for this question. The policy fires when the series crosses the condition for the stated duration. Why the correct answer wins: An SLO ties the alert to the user promise rather than to a raw resource threshold.

### Question 76 — B

Answer: Create an alerting policy on the metric. The policy fires when the series crosses the condition for the stated duration. Local study-map skill 6.2 (Alerting and Service Level Objectives), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 6 (solution and operations excellence): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. The metric turns a log pattern into a series that can be alerted on and charted. Why the correct answer wins: The policy fires when the series crosses the condition for the stated duration.
- **B:** Correct. In this case: The policy fires when the series crosses the condition for the stated duration.
- **C:** Incorrect for this question. An SLO ties the alert to the promise the users care about rather than to a raw resource threshold. Why the correct answer wins: The policy fires when the series crosses the condition for the stated duration.
- **D:** Incorrect for this question. The dashboard gives the team one view of the same signals during an incident. Why the correct answer wins: The policy fires when the series crosses the condition for the stated duration.

### Question 77 — B

Answer: Publish a runbook per alert. The runbook records the diagnostic steps so the response does not depend on who is awake. Local study-map skill 6.3 (Release Management and Support), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 6 (solution and operations excellence): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. A named rotation turns an alert into a person who is already accountable for it. Why the correct answer wins: The runbook records the diagnostic steps so the response does not depend on who is awake.
- **B:** Correct. In this case: The runbook records the diagnostic steps so the response does not depend on who is awake.
- **C:** Incorrect for this question. The support tier sets the response time and the escalation path the business expects. Why the correct answer wins: The runbook records the diagnostic steps so the response does not depend on who is awake.
- **D:** Incorrect for this question. The dashboard gives the team one view of the same signals during an incident. Why the correct answer wins: The runbook records the diagnostic steps so the response does not depend on who is awake.

### Question 78 — A

Answer: Match the support plan to the recovery commitment. The support tier sets the response time and the escalation path the business expects. Local study-map skill 6.3 (Release Management and Support), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 6 (solution and operations excellence): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Correct. In this case: The support tier sets the response time and the escalation path the business expects.
- **B:** Incorrect for this question. A named rotation turns an alert into a person who is already accountable for it. Why the correct answer wins: The support tier sets the response time and the escalation path the business expects.
- **C:** Incorrect for this question. The runbook records the diagnostic steps so the response does not depend on who is awake. Why the correct answer wins: The support tier sets the response time and the escalation path the business expects.
- **D:** Incorrect for this question. The contract converts an internal target into an obligation with a consequence. Why the correct answer wins: The support tier sets the response time and the escalation path the business expects.

### Question 79 — B

Answer: Run a chaos experiment against a zone. The experiment proves the failover path works while the impact is controlled. Local study-map skill 6.4 (Reliability Testing), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 6 (solution and operations excellence): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. A canary limits the blast radius while the error and latency signals are compared. Why the correct answer wins: The experiment proves the failover path works while the impact is controlled.
- **B:** Correct. In this case: The experiment proves the failover path works while the impact is controlled.
- **C:** Incorrect for this question. An independent test attempts the attack the design claims to prevent. Why the correct answer wins: The experiment proves the failover path works while the impact is controlled.
- **D:** Incorrect for this question. The load test measures the system at the concurrency the business expects, before launch. Why the correct answer wins: The experiment proves the failover path works while the impact is controlled.

### Question 80 — A

Answer: Write a blameless postmortem with actions. The postmortem records cause and follow-up work, which is how the same failure is prevented. Local study-map skill 6.5 (Operational Excellence and Quality Control), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 6 (solution and operations excellence): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Correct. In this case: The postmortem records cause and follow-up work, which is how the same failure is prevented.
- **B:** Incorrect for this question. The runbook records the diagnostic steps so the response does not depend on who is awake. Why the correct answer wins: The postmortem records cause and follow-up work, which is how the same failure is prevented.
- **C:** Incorrect for this question. The support tier sets the response time and the escalation path the business expects. Why the correct answer wins: The postmortem records cause and follow-up work, which is how the same failure is prevented.
- **D:** Incorrect for this question. The dashboard gives the team one view of the same signals during an incident. Why the correct answer wins: The postmortem records cause and follow-up work, which is how the same failure is prevented.

### Question 81 — D

Answer: Define the baseline and target as a KPI with an owner. A measured baseline and a named owner make the outcome testable after the migration. Local study-map skill 1.1 (Business Requirements and Success Metrics), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 1 (designing and planning): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. The export attributes cost to the team and service that caused it. Why the correct answer wins: A measured baseline and a named owner make the outcome testable after the migration.
- **B:** Incorrect for this question. The dashboard gives the team one view of the same signals during an incident. Why the correct answer wins: A measured baseline and a named owner make the outcome testable after the migration.
- **C:** Incorrect for this question. The model compares run cost, people cost, and exit cost rather than the monthly bill alone. Why the correct answer wins: A measured baseline and a named owner make the outcome testable after the migration.
- **D:** Correct. In this case: A measured baseline and a named owner make the outcome testable after the migration.

### Question 82 — A

Answer: Use a managed instance group with autoscaling. The managed instance group replaces unhealthy instances and adds capacity from a template as load rises. Local study-map skill 1.6 (Compute Platform Selection), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 1 (designing and planning): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Correct. In this case: The managed instance group replaces unhealthy instances and adds capacity from a template as load rises.
- **B:** Incorrect for this question. Autopilot manages nodes, scaling, and patching, so the team owns only the workloads. Why the correct answer wins: The managed instance group replaces unhealthy instances and adds capacity from a template as load rises.
- **C:** Incorrect for this question. Batch schedules containerised jobs onto managed or existing capacity and retires it when done. Why the correct answer wins: The managed instance group replaces unhealthy instances and adds capacity from a template as load rises.
- **D:** Incorrect for this question. Cloud Run runs a stateless container per request and scales to zero when idle. Why the correct answer wins: The managed instance group replaces unhealthy instances and adds capacity from a template as load rises.

### Question 83 — B

Answer: Move the steady services to E2 machine types. A cheaper shape for the steady service lowers the bill without committing to peak capacity all year. E2 shapes trade peak performance for a lower price on workloads that do not need it. Local study-map skill 4.5 (Cost Optimization), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 4 (analyzing and optimizing): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. Spot capacity costs far less but can be reclaimed with 30 seconds of notice. Why the correct answer wins: A cheaper shape for the steady service lowers the bill without committing to peak capacity all year.
- **B:** Correct. E2 shapes trade peak performance for a lower price on workloads that do not need it. In this case: A cheaper shape for the steady service lowers the bill without committing to peak capacity all year.
- **C:** Incorrect for this question. Sole tenancy keeps the physical host dedicated, which matters for licensing or isolation rules. Why the correct answer wins: A cheaper shape for the steady service lowers the bill without committing to peak capacity all year.
- **D:** Incorrect for this question. A one- or three-year commitment discounts the capacity that runs constantly, not the peaks. Why the correct answer wins: A cheaper shape for the steady service lowers the bill without committing to peak capacity all year.

### Question 84 — A

Answer: Roll out a canary to a small share of traffic. A canary limits the blast radius while the error and latency signals are compared. Local study-map skill 5.1 (Deployment and Release Strategy), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 5 (managing implementation): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Correct. In this case: A canary limits the blast radius while the error and latency signals are compared.
- **B:** Incorrect for this question. Two identical environments let the switch be reversed instantly if the new one misbehaves. Why the correct answer wins: A canary limits the blast radius while the error and latency signals are compared.
- **C:** Incorrect for this question. The flag separates deployment from release, so the code can ship dark and be turned off instantly. Why the correct answer wins: A canary limits the blast radius while the error and latency signals are compared.
- **D:** Incorrect for this question. A rolling replacement keeps capacity but exposes the whole fleet before the signal is trusted. Why the correct answer wins: A canary limits the blast radius while the error and latency signals are compared.

### Question 85 — A

Answer: Run a load test at the expected peak. The load test measures the system at the concurrency the business expects, before the peak. Local study-map skill 6.4 (Reliability Testing), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 6 (solution and operations excellence): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Correct. In this case: The load test measures the system at the concurrency the business expects, before the peak.
- **B:** Incorrect for this question. An independent test attempts the attack the design claims to prevent. Why the correct answer wins: The load test measures the system at the concurrency the business expects, before the peak.
- **C:** Incorrect for this question. The pyramid puts volume where it is cheap and keeps end-to-end tests for the critical paths. Why the correct answer wins: The load test measures the system at the concurrency the business expects, before the peak.
- **D:** Incorrect for this question. The experiment proves the failover path works while the impact is controlled. Why the correct answer wins: The load test measures the system at the concurrency the business expects, before the peak.

### Question 86 — A

Answer: Run active-active across two regions. Both regions serve traffic, so a regional loss is absorbed without a failover decision. Local study-map skill 1.3 (High Availability and Failover Design), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 1 (designing and planning): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Correct. In this case: Both regions serve traffic, so a regional loss is absorbed without a failover decision.
- **B:** Incorrect for this question. Only the core data and configuration stay warm, so recovery starts the compute and takes minutes. Why the correct answer wins: Both regions serve traffic, so a regional loss is absorbed without a failover decision.
- **C:** Incorrect for this question. A running but smaller copy recovers in a short window at a continuous cost. Why the correct answer wins: Both regions serve traffic, so a regional loss is absorbed without a failover decision.
- **D:** Incorrect for this question. Restoring from backup is the cheapest option and the slowest to recover. Why the correct answer wins: Both regions serve traffic, so a regional loss is absorbed without a failover decision.

### Question 87 — D

Answer: Enable Cloud CDN on the backend. CDN caches responses at edge locations, which cuts origin load and latency for repeat reads. Local study-map skill 1.4 (Network Design), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 1 (designing and planning): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. An internal load balancer distributes traffic inside the VPC without exposing it to the internet. Why the correct answer wins: CDN caches responses at edge locations, which cuts origin load and latency for repeat reads.
- **B:** Incorrect for this question. Cloud NAT lets private instances reach the internet without an external address. Why the correct answer wins: CDN caches responses at edge locations, which cuts origin load and latency for repeat reads.
- **C:** Incorrect for this question. The storage commands copy and sync objects with resumable, parallel transfers. Why the correct answer wins: CDN caches responses at edge locations, which cuts origin load and latency for repeat reads.
- **D:** Correct. In this case: CDN caches responses at edge locations, which cuts origin load and latency for repeat reads.

### Question 88 — B

Answer: Use a dual-region bucket. A dual-region bucket keeps two replicas in a chosen pair of regions and survives one region loss. Local study-map skill 2.2 (Storage Configuration and Lifecycle), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 2 (managing and provisioning): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. Standard is for data read frequently and has no retrieval fee. Why the correct answer wins: A dual-region bucket keeps two replicas in a chosen pair of regions and survives one region loss.
- **B:** Correct. In this case: A dual-region bucket keeps two replicas in a chosen pair of regions and survives one region loss.
- **C:** Incorrect for this question. Nearline suits data read about once a month and charges for early deletion. Why the correct answer wins: A dual-region bucket keeps two replicas in a chosen pair of regions and survives one region loss.
- **D:** Incorrect for this question. Archive is cheapest to hold and slowest and most expensive to retrieve. Why the correct answer wins: A dual-region bucket keeps two replicas in a chosen pair of regions and survives one region loss.

### Question 89 — A, D

Answers: Set the RPO and RTO with the business owner; Replicate the data to the second region. The targets quantify the acceptable loss, and the data must already be in the second region when it is needed. The targets come from the business impact of data loss and downtime, not from the technology. The data must exist in the second region before any compute there can serve it. Local study-map skill 4.4 (Disaster Recovery and Business Continuity), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 4 (analyzing and optimizing): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Correct. The data must exist in the second region before any compute there can serve it. In this case: The targets quantify the acceptable loss, and the data must already be in the second region when it is needed.
- **B:** Incorrect for this question. Recommender reports idle and over-provisioned resources with the estimated saving. Why the correct answer wins: The targets quantify the acceptable loss, and the data must already be in the second region when it is needed.
- **C:** Incorrect for this question. The dashboard gives the team one view of the same signals during an incident. Why the correct answer wins: The targets quantify the acceptable loss, and the data must already be in the second region when it is needed.
- **D:** Correct. The targets come from the business impact of data loss and downtime, not from the technology. In this case: The targets quantify the acceptable loss, and the data must already be in the second region when it is needed.
- **E:** Incorrect for this question. Labels attribute spend in billing export; they do not grant or restrict access. Why the correct answer wins: The targets quantify the acceptable loss, and the data must already be in the second region when it is needed.

### Question 90 — B

Answer: Define an SLO with an error budget. An SLO expresses the user-visible promise that the region can be judged against. An SLO ties the alert to the promise the users care about rather than to a raw resource threshold. Local study-map skill 6.2 (Alerting and Service Level Objectives), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 6 (solution and operations excellence): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. The dashboard gives the team one view of the same signals during an incident. Why the correct answer wins: An SLO expresses the user-visible promise that the region can be judged against.
- **B:** Correct. An SLO ties the alert to the promise the users care about rather than to a raw resource threshold. In this case: An SLO expresses the user-visible promise that the region can be judged against.
- **C:** Incorrect for this question. The policy fires when the series crosses the condition for the stated duration. Why the correct answer wins: An SLO expresses the user-visible promise that the region can be judged against.
- **D:** Incorrect for this question. The check measures availability from outside, which no internal metric can prove. Why the correct answer wins: An SLO expresses the user-visible promise that the region can be judged against.

### Question 91 — A

Answer: Define a custom role with only the required permissions. A custom role expresses least privilege when no predefined role matches the job exactly. Local study-map skill 3.1 (IAM and Least Privilege), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 3 (security and compliance): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Correct. In this case: A custom role expresses least privilege when no predefined role matches the job exactly.
- **B:** Incorrect for this question. A predefined role grants the curated permission set for one job at the level it is bound to. Why the correct answer wins: A custom role expresses least privilege when no predefined role matches the job exactly.
- **C:** Incorrect for this question. A bastion is still an internet-facing host that must be patched and watched. Why the correct answer wins: A custom role expresses least privilege when no predefined role matches the job exactly.
- **D:** Incorrect for this question. A key file is a long-lived credential that works until it is noticed and revoked. Why the correct answer wins: A custom role expresses least privilege when no predefined role matches the job exactly.

### Question 92 — A, D

Answers: Put Identity-Aware Proxy in front of the application; Use Chrome Enterprise Premium for the workforce. The proxy authorises each request, and context-aware access evaluates the device and identity signals. IAP authenticates and authorises each request before it reaches the backend, with no VPN. Context-aware access evaluates device and identity signals for every application, not just the network. Local study-map skill 3.5 (Secure Remote Access and Zero Trust), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 3 (security and compliance): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Correct. Context-aware access evaluates device and identity signals for every application, not just the network. In this case: The proxy authorises each request, and context-aware access evaluates the device and identity signals.
- **B:** Incorrect for this question. Cloud NAT lets private instances reach the internet without an external address. Why the correct answer wins: The proxy authorises each request, and context-aware access evaluates the device and identity signals.
- **C:** Incorrect for this question. A bastion is still an internet-facing host that must be patched and watched. Why the correct answer wins: The proxy authorises each request, and context-aware access evaluates the device and identity signals.
- **D:** Correct. IAP authenticates and authorises each request before it reaches the backend, with no VPN. In this case: The proxy authorises each request, and context-aware access evaluates the device and identity signals.
- **E:** Incorrect for this question. A key file is a long-lived credential that works until it is noticed and revoked. Why the correct answer wins: The proxy authorises each request, and context-aware access evaluates the device and identity signals.

### Question 93 — B

Answer: Enable Data Access audit logs. Data Access logging is off by default and must be enabled before reads and writes are recorded. Local study-map skill 3.8 (Compliance, Residency, and Audit Logging), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 3 (security and compliance): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. Access Transparency records when Google staff access your content, which is evidence of oversight, not of user activity. Why the correct answer wins: Data Access logging is off by default and must be enabled before reads and writes are recorded.
- **B:** Correct. In this case: Data Access logging is off by default and must be enabled before reads and writes are recorded.
- **C:** Incorrect for this question. Admin Activity records configuration changes and cannot be disabled. Why the correct answer wins: Data Access logging is off by default and must be enabled before reads and writes are recorded.
- **D:** Incorrect for this question. The metric turns a log pattern into a series that can be alerted on and charted. Why the correct answer wins: Data Access logging is off by default and must be enabled before reads and writes are recorded.

### Question 94 — D

Answer: Attach a Serverless VPC Access connector. The connector gives serverless workloads a route to internal addresses in the VPC. Local study-map skill 2.5 (Serverless Configuration), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 2 (managing and provisioning): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. Private Google Access reaches Google APIs from an internal address without a proxy or a NAT gateway. Why the correct answer wins: The connector gives serverless workloads a route to internal addresses in the VPC.
- **B:** Incorrect for this question. Cloud NAT lets private instances reach the internet without an external address. Why the correct answer wins: The connector gives serverless workloads a route to internal addresses in the VPC.
- **C:** Incorrect for this question. A PSC endpoint gives a private IP in the consumer VPC without peering or exposing the service publicly. Why the correct answer wins: The connector gives serverless workloads a route to internal addresses in the VPC.
- **D:** Correct. In this case: The connector gives serverless workloads a route to internal addresses in the VPC.

### Question 95 — D

Answer: Route the logs with an aggregated sink. An aggregated sink collects logs from every project into one destination the auditor can query. Local study-map skill 6.3 (Release Management and Support), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 6 (solution and operations excellence): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. The runbook records the diagnostic steps so the response does not depend on who is awake. Why the correct answer wins: An aggregated sink collects logs from every project into one destination the auditor can query.
- **B:** Incorrect for this question. The dashboard gives the team one view of the same signals during an incident. Why the correct answer wins: An aggregated sink collects logs from every project into one destination the auditor can query.
- **C:** Incorrect for this question. The metric turns a log pattern into a series that can be alerted on and charted. Why the correct answer wins: An aggregated sink collects logs from every project into one destination the auditor can query.
- **D:** Correct. In this case: An aggregated sink collects logs from every project into one destination the auditor can query.

### Question 96 — C

Answer: Publish events to Pub/Sub. Pub/Sub decouples producers from consumers and holds each message until every subscription acknowledges it. Local study-map skill 1.7 (Data Processing and Analytics Selection), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 1 (designing and planning): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. Tasks dispatches HTTP or App Engine requests with rate limits and per-queue retry policy. Why the correct answer wins: Pub/Sub decouples producers from consumers and holds each message until every subscription acknowledges it.
- **B:** Incorrect for this question. The service runs scheduled loads from SaaS sources and other clouds into BigQuery. Why the correct answer wins: Pub/Sub decouples producers from consumers and holds each message until every subscription acknowledges it.
- **C:** Correct. In this case: Pub/Sub decouples producers from consumers and holds each message until every subscription acknowledges it.
- **D:** Incorrect for this question. Airflow expresses dependencies between scheduled jobs and retries a failed task without rerunning the rest. Why the correct answer wins: Pub/Sub decouples producers from consumers and holds each message until every subscription acknowledges it.

### Question 97 — A

Answer: Store the objects in Archive storage class. Archive is the cheapest class to hold for data that is rarely retrieved but must be kept. Archive is cheapest to hold and slowest and most expensive to retrieve. Local study-map skill 1.5 (Storage and Data Store Selection), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 1 (designing and planning): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Correct. Archive is cheapest to hold and slowest and most expensive to retrieve. In this case: Archive is the cheapest class to hold for data that is rarely retrieved but must be kept.
- **B:** Incorrect for this question. Standard is for data read frequently and has no retrieval fee. Why the correct answer wins: Archive is the cheapest class to hold for data that is rarely retrieved but must be kept.
- **C:** Incorrect for this question. Nearline suits data read about once a month and charges for early deletion. Why the correct answer wins: Archive is the cheapest class to hold for data that is rarely retrieved but must be kept.
- **D:** Incorrect for this question. Local SSD is the fastest ephemeral option and loses its data when the VM stops. Why the correct answer wins: Archive is the cheapest class to hold for data that is rarely retrieved but must be kept.

### Question 98 — A

Answer: Use a managed instance group with autoscaling. The managed instance group replaces unhealthy instances and adds capacity from a template as load rises. Local study-map skill 2.3 (Compute Provisioning and Patch Management), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 2 (managing and provisioning): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Correct. In this case: The managed instance group replaces unhealthy instances and adds capacity from a template as load rises.
- **B:** Incorrect for this question. VM Manager inventories and applies OS patches across a fleet instead of relying on manual runs. Why the correct answer wins: The managed instance group replaces unhealthy instances and adds capacity from a template as load rises.
- **C:** Incorrect for this question. Spot capacity costs far less but can be reclaimed with 30 seconds of notice. Why the correct answer wins: The managed instance group replaces unhealthy instances and adds capacity from a template as load rises.
- **D:** Incorrect for this question. Custom vCPU and memory avoid paying for a fixed shape that over-provisions one dimension. Why the correct answer wins: The managed instance group replaces unhealthy instances and adds capacity from a template as load rises.

### Question 99 — A

Answer: Run a load test at the expected peak. The load test measures the system at the concurrency the business expects, before launch. Local study-map skill 4.3 (Testing and Validation), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 4 (analyzing and optimizing): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Correct. In this case: The load test measures the system at the concurrency the business expects, before launch.
- **B:** Incorrect for this question. The pyramid puts volume where it is cheap and keeps end-to-end tests for the critical paths. Why the correct answer wins: The load test measures the system at the concurrency the business expects, before launch.
- **C:** Incorrect for this question. The experiment proves the failover path works while the impact is controlled. Why the correct answer wins: The load test measures the system at the concurrency the business expects, before launch.
- **D:** Incorrect for this question. An independent test attempts the attack the design claims to prevent. Why the correct answer wins: The load test measures the system at the concurrency the business expects, before launch.

### Question 100 — D

Answer: Define dashboards and metrics in Cloud Monitoring. Monitoring collects the platform and application metrics that the first alert will use. Local study-map skill 6.1 (Observability Design), mapped to the official guide: Google Cloud Professional Cloud Architect exam guide (English), retrieved October 2026 Primary reference: Professional Cloud Architect exam guide, section 6 (solution and operations excellence): https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf

- **A:** Incorrect for this question. Recommender reports idle and over-provisioned resources with the estimated saving. Why the correct answer wins: Monitoring collects the platform and application metrics that the first alert will use.
- **B:** Incorrect for this question. The dashboard gives the team one view of the same signals during an incident. Why the correct answer wins: Monitoring collects the platform and application metrics that the first alert will use.
- **C:** Incorrect for this question. Trace shows how one request spent its time across services and calls. Why the correct answer wins: Monitoring collects the platform and application metrics that the first alert will use.
- **D:** Correct. In this case: Monitoring collects the platform and application metrics that the first alert will use.
