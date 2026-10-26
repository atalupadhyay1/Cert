# Google Cloud Professional Cloud DevOps Engineer — Full-Length Mock Exam 3

Professional Cloud DevOps Engineer · 100 questions · expanded practice bank · passing score not published

Blueprint-weighted mock exam. Item mix: 84 multiple-choice and 16 multiple-select items (the selection count is stated in each multi-select stem). The live exam publishes 50-60 multiple-choice and multiple-select questions and has no case-study component, so this set is larger on purpose and no case-study item is reproduced. The live paper allows two hours for 50-60 items, so this 100-item set is a slower-per-item rehearsal: about 72 seconds per item here against roughly 120-144 seconds live. Use it to build a habit of finishing with time to review. See the README for the exact fidelity boundary.

Original educational content, not actual, recalled, or copied Google exam items.

## Questions

---

## Domain 1 — Bootstrapping and Maintaining a Google Cloud Organization (Hierarchy, Infrastructure as Code, and Pipeline Foundations)

### 1. Every project owner sets the same constraint separately, and three projects have already drifted. What caused the drift?

- A. Apply the constraint separately in each project
- B. Add an IAM deny policy for the sensitive permission
- C. Apply the constraint to the business unit folder
- D. Apply the constraint at the organization node

### 2. Chargeback follows the service, and owners must find their own staging and production projects together. How should the hierarchy be shaped?

- A. Group projects by application inside each environment folder
- B. Apply the constraint to the business unit folder
- C. Apply the constraint separately in each project
- D. Group projects by environment with applications below

### 3. A regulated service must be consumed from another project without touching the public internet or sharing a subnet. What fits?

- A. Create a Shared VPC host project and attach the service projects
- B. Publish the service behind a Private Service Connect endpoint
- C. Give each project its own VPC and Cloud NAT
- D. Peer every project VPC with every other project VPC

### 4. Every new project builds its own network, firewall rules, and egress path, and the firewall audit takes a week. What caused that?

- A. Create a Shared VPC host project and attach the service projects
- B. Peer every project VPC with every other project VPC
- C. Publish the service behind a Private Service Connect endpoint
- D. Give each project its own VPC and Cloud NAT

### 5. Audit entries from every project must land in one destination, and latency from those projects must chart together. Which two configurations apply? Select two.

- A. Add the projects to one metrics scope
- B. Route every project log to one aggregated sink
- C. Create a Shared VPC host project and attach the service projects
- D. Route the entries to a Pub/Sub topic
- E. Keep one log bucket inside each project

### 6. A constraint must still apply after a project owner removes every IAM binding. What provides that?

- A. Grant a predefined role once at the folder
- B. Add an IAM deny policy for the sensitive permission
- C. Grant a custom role limited to the required permissions
- D. Enforce the restriction with an organization policy constraint

### 7. A team needs read access to three services and no write permission anywhere. What should be created?

- A. Grant a predefined role once at the folder
- B. Grant a custom role limited to the required permissions
- C. Add an IAM deny policy for the sensitive permission
- D. Enforce the restriction with an organization policy constraint

### 8. Every workload runs as the same automatically created account, and one compromise reached every bucket. What caused that reach?

- A. Let the workload use the default Compute Engine service account
- B. Create one service account per workload
- C. Create one service account per environment
- D. Grant impersonation of the service account instead of a key

### 9. A team copies a dataset to another continent for latency and calls it a residency control. What did it actually do?

- A. Apply the constraint at the organization node
- B. Create a Shared VPC host project and attach the service projects
- C. Place the resources in a region that satisfies the residency rule
- D. Replicate the data to a second region

### 10. Terraform state must live in a managed service with its own audit trail and no laptop apply. What fits?

- A. Define the estate as Terraform modules held in version control
- B. Reconcile the resources with Config Connector
- C. Apply the deployment through Infrastructure Manager
- D. Automate the repeated step with a Python script calling the API

### 11. Manifests for twelve services share their structure and differ only in a handful of values. What fits?

- A. Package the workload as a Helm chart
- B. Render the manifests through a kpt function pipeline
- C. Define the estate as Terraform modules held in version control
- D. Reconcile the resources with Config Connector

### 12. The same transformation must be applied to manifests arriving from three upstream repositories. What fits?

- A. Schedule a plan that reports drift
- B. Render the manifests through a kpt function pipeline
- C. Define the estate as Terraform modules held in version control
- D. Package the workload as a Helm chart

### 13. A repeated task must run identically from a script, and the Terraform it applies must be executed by a managed service. Which two fit? Select two.

- A. Make the change in the console and note it in the wiki
- B. Run the documented gcloud commands by hand for each environment
- C. Schedule a plan that reports drift
- D. Automate the repeated step with a Python script calling the API
- E. Apply the deployment through Infrastructure Manager

### 14. The same release must promote through staging and production with a single record. What fits?

- A. Bake the machine image with Packer
- B. Let Argo CD pull the manifests from Git
- C. Use Cloud Build for CI and Cloud Deploy for delivery
- D. Run Jenkins on a self-managed VM

### 15. Build outputs must be stored per region with IAM scoped to the pipeline. What fits?

- A. Store the build output in Artifact Registry
- B. Tag each artifact with the commit SHA and forbid overwrite
- C. Bake the machine image with Packer
- D. Push the image to Container Registry

### 16. The cluster must reconcile to Git every few minutes without holding a push credential. What fits?

- A. Use Cloud Build for CI and Cloud Deploy for delivery
- B. Bake the machine image with Packer
- C. Run Jenkins on a self-managed VM
- D. Let Argo CD pull the manifests from Git

### 17. Two teams deploy to one staging environment and each release overwrites the other's data. What caused that?

- A. Keep one base with a Kustomize overlay per environment
- B. Bake the environment settings into the image
- C. Create a short-lived project per change and delete it after review
- D. Keep one shared staging environment for every team

### 18. Node pools are three versions behind because upgrades wait for a quiet week that never arrives. What caused that?

- A. Register the clusters in a fleet
- B. Put the cluster on a release channel with a maintenance window
- C. Stand up a second cluster and shift traffic after verification
- D. Upgrade each node pool by hand whenever an operator is free

### 19. Developers must work in a managed IDE, and it must start from the toolchain security approved. Which two fit? Select two.

- A. Rely on Cloud Shell for every developer
- B. Give developers Cloud Workstations built from a custom image
- C. Use Gemini Code Assist for the suggested change
- D. Let each developer install the tools locally
- E. Build a custom image that carries the approved toolchain

### 20. An operator wants the observed configuration explained before changing anything. What fits?

- A. Let each developer install the tools locally
- B. Use Gemini CLI for the repetitive script
- C. Use Gemini Code Assist for the suggested change
- D. Ask Gemini Cloud Assist to explain the resource state

---

## Domain 2 — Building and Implementing CI/CD Pipelines (Delivery Pipelines and Software Supply Chain)

### 21. Pull requests must be validated before merge, and production images must come only from signed tags. Which two triggers apply? Select two.

- A. Have an engineer build locally and upload the result
- B. Create a trigger that runs the tests on every pull request
- C. Trigger the pipeline only on a signed tag
- D. Add a Cloud Deploy approval gate before production
- E. Create a Cloud Build trigger on the release branch

### 22. A branch named release must rebuild artifacts whenever it moves. What should be configured?

- A. Have an engineer build locally and upload the result
- B. Trigger the pipeline only on a signed tag
- C. Create a Cloud Build trigger on the release branch
- D. Create a trigger that runs the tests on every pull request

### 23. A new engineer produces a different binary from identical source because they build it themselves. Why does that happen?

- A. Have an engineer build locally and upload the result
- B. Trigger the pipeline only on a signed tag
- C. Read Cloud Audit Logs for the release history
- D. Create a trigger that runs the tests on every pull request

### 24. Two incidents were traced to a deployment whose image reference pointed somewhere new. What caused that?

- A. Reuse the latest tag for every build
- B. Inspect the build provenance attestation
- C. Store the build output in Artifact Registry
- D. Tag each artifact with the commit SHA and forbid overwrite

### 25. Untagged images must be deleted after thirty days under a policy kept in one region. What fits?

- A. Push the image to Container Registry
- B. Tag each artifact with the commit SHA and forbid overwrite
- C. Reuse the latest tag for every build
- D. Store the build output in Artifact Registry

### 26. Traffic must shift between revisions of a managed serverless service. What fits?

- A. Use a GKE cluster in the pipeline project as the target
- B. Deliver to a Cloud Run service revision
- C. Define the attached cluster as the delivery target
- D. Add a Cloud Deploy approval gate before production

### 27. A cluster in the pipeline project must receive releases without extra registration. What fits?

- A. Use a GKE cluster in the pipeline project as the target
- B. Deliver to a Cloud Run service revision
- C. Define the attached cluster as the delivery target
- D. Read Cloud Audit Logs for the release history

### 28. A change reached production eleven minutes after a developer pushed it, with nobody reviewing it. What allowed that?

- A. Promote automatically to every target in the chain
- B. Read Cloud Audit Logs for the release history
- C. Have an engineer build locally and upload the result
- D. Add a Cloud Deploy approval gate before production

### 29. A procurement questionnaire asks which integrity level the build process achieves. What answers it?

- A. Read Cloud Audit Logs for the release history
- B. Enforce Binary Authorization attestations before deploy
- C. Describe the build with its supply chain level and signed provenance
- D. Inspect the build provenance attestation

### 30. A review must prove that the image which ran is the image that was built. What provides that?

- A. Inspect the build provenance attestation
- B. Read Cloud Audit Logs for the release history
- C. Reuse the latest tag for every build
- D. Tag each artifact with the commit SHA and forbid overwrite

### 31. Customers see connection resets at every deployment because the old version is stopped first. Which strategy is that?

- A. Send ten percent of traffic to the new revision and watch the SLI
- B. Stop the old version and then start the new one
- C. Replace the instances in batches
- D. Run the new version alongside and switch traffic at once

### 32. Five percent must reach the new version as decided by the service mesh route. What fits?

- A. Send ten percent of traffic to the new revision and watch the SLI
- B. Split traffic with a Cloud Service Mesh route
- C. Run the new version alongside and switch traffic at once
- D. Replace the instances in batches

### 33. A migration must be exercised against real traffic on an identical stack before any cutover. What fits?

- A. Send ten percent of traffic to the new revision and watch the SLI
- B. Run the new version alongside and switch traffic at once
- C. Replace the instances in batches
- D. Stop the old version and then start the new one

### 34. A rollout must stop when the success ratio falls below the objective for ten minutes. What should gate it?

- A. Add a Cloud Deploy approval gate before production
- B. Gate the rollout on the error-rate SLI
- C. Gate the rollout on average CPU alone
- D. Create an uptime check against the login flow

### 35. A pipeline step failed halfway, and the eventual fix must be safe to repeat. Which two practices apply? Select two.

- A. Patch production by hand and reconcile later
- B. Make the failed step idempotent and re-run it
- C. Read Cloud Audit Logs for the release history
- D. Roll the release back to the previous one
- E. Start from the failed step log in Cloud Build

### 36. A canary reports a five percent error rate while the previous release stays healthy. What is the right action?

- A. Start from the failed step log in Cloud Build
- B. Patch production by hand and reconcile later
- C. Make the failed step idempotent and re-run it
- D. Roll the release back to the previous one

### 37. A compliance rule requires every use of the encryption key to appear in an audit log. What provides that?

- A. Issue and rotate the certificate with Certificate Manager
- B. Encrypt the payload with a Cloud KMS key
- C. Commit the credential to the private repository
- D. Store the credential in Secret Manager with versions

### 38. A wildcard certificate expires next month and nobody owns the renewal. What fixes that?

- A. Issue and rotate the certificate with Certificate Manager
- B. Encrypt the payload with a Cloud KMS key
- C. Store the credential in Secret Manager with versions
- D. Keep the non-secret configuration in Parameter Manager

### 39. Credentials must be versioned and audited, and non-secret settings must be versioned per environment. Which two services apply? Select two.

- A. Pass the secret as a build argument
- B. Store the credential in Secret Manager with versions
- C. Keep the non-secret configuration in Parameter Manager
- D. Commit the credential to the private repository
- E. Bake the environment settings into the image

### 40. A repository scan finds a service account key committed six months ago. Why is that urgent?

- A. Store the credential in Secret Manager with versions
- B. Keep the non-secret configuration in Parameter Manager
- C. Commit the credential to the private repository
- D. Mount the secret at runtime from Secret Manager

### 41. The image history shows the database password in plain text. What put it there?

- A. Pass the secret as a build argument
- B. Mount the secret at runtime from Secret Manager
- C. Inject the secret at build time into the image layer
- D. Store the credential in Secret Manager with versions

### 42. A critical vulnerability shipped because the scanner only wrote a dashboard line. What was missing?

- A. Fail the pipeline on a critical vulnerability finding
- B. Enable Artifact Analysis scanning on the repository
- C. Keep the scan report for the monthly review
- D. Enforce Binary Authorization attestations before deploy

### 43. Every stored image must be rescanned when new vulnerabilities are published. What provides that?

- A. Keep the scan report for the monthly review
- B. Enforce Binary Authorization attestations before deploy
- C. Enable Artifact Analysis scanning on the repository
- D. Fail the pipeline on a critical vulnerability finding

### 44. A high-severity finding must stop the image before it reaches staging. What should be configured?

- A. Keep the scan report for the monthly review
- B. Enforce Binary Authorization attestations before deploy
- C. Fail the pipeline on a critical vulnerability finding
- D. Bind deploy permissions only inside the production project

### 45. Deploy rights must stay inside each environment, and each environment needs its own application identity. Which two controls apply? Select two.

- A. Create one service account per environment
- B. Use one identity with deploy rights in every environment
- C. Download a JSON key file for the service account
- D. Run the pipeline as the default editor service account
- E. Bind deploy permissions only inside the production project

---

## Domain 3 — Applying Site Reliability Engineering Practices (Reliability Engineering in Practice)

### 46. The team writes down that 99.9 percent of requests must succeed, without promising it to customers. What is that target?

- A. Publish a contractual promise with a remedy
- B. Set an internal target on that indicator
- C. Track the ratio of good requests to total requests
- D. Alert on a fast error-budget burn rate

### 47. A measurement counts requests served in under 400 ms as successes. What is that measurement?

- A. Track the ratio of good requests to total requests
- B. Set an internal target on that indicator
- C. Publish a contractual promise with a remedy
- D. Assume five nines for every service

### 48. A contract attaches service credits to a monthly availability figure. What is that document?

- A. Publish a contractual promise with a remedy
- B. Track the ratio of good requests to total requests
- C. Choose three nines and spend the difference on features
- D. Set an internal target on that indicator

### 49. The product and SRE leads agree in writing that launches pause once the allowance is gone. What is that agreement?

- A. Assume five nines for every service
- B. Stop feature releases when the error budget is spent
- C. Alert on a fast error-budget burn rate
- D. Publish a contractual promise with a remedy

### 50. A page fires because the allowance will be exhausted in three days at the current rate. What produced it?

- A. Stop feature releases when the error budget is spent
- B. Alert when CPU stays above ninety percent for ten minutes
- C. Publish a contractual promise with a remedy
- D. Alert on a fast error-budget burn rate

### 51. A team must pick a target it can afford, and then pause change whenever that target is missed. Which two practices apply? Select two.

- A. Register the service in the service catalog
- B. Stop feature releases when the error budget is spent
- C. Assume five nines for every service
- D. Choose three nines and spend the difference on features
- E. Publish a contractual promise with a remedy

### 52. A vendor standard demands five nines from a service that runs only in office hours. What is the flaw?

- A. Choose three nines and spend the difference on features
- B. Publish a contractual promise with a remedy
- C. Request a quota increase and reserve capacity before the launch
- D. Assume five nines for every service

### 53. Nobody can name the owner of a service, and an obsolete service must disappear on a specific date. Which two practices apply? Select two.

- A. Request a quota increase and reserve capacity before the launch
- B. Leave the unused service running for now
- C. Announce the retirement date and withdraw traffic gradually
- D. Add capacity in a second region
- E. Register the service in the service catalog

### 54. A pilot from two years ago still bills every month and has no users. Which state is that?

- A. Register the service in the service catalog
- B. Announce the retirement date and withdraw traffic gradually
- C. Drain connections before removing the instance
- D. Leave the unused service running for now

### 55. The launch plan shows a regional limit that will be reached in the first week. What should be done?

- A. Assume the default quota will absorb the launch
- B. Add capacity on a fixed calendar schedule
- C. Request a quota increase and reserve capacity before the launch
- D. Schedule the batch with Dynamic Workload Scheduler

### 56. Capacity is added every Monday at nine even when demand never changes. What is wrong with that?

- A. Schedule the batch with Dynamic Workload Scheduler
- B. Put the instance group behind an autoscaler on CPU
- C. Add capacity on a fixed calendar schedule
- D. Request a quota increase and reserve capacity before the launch

### 57. Web servers behind a load balancer must grow as CPU utilisation rises. What fits?

- A. Add capacity on a fixed calendar schedule
- B. Set Cloud Run concurrency so replicas follow load
- C. Scale on queue depth with a horizontal pod autoscaler
- D. Put the instance group behind an autoscaler on CPU

### 58. A new instance must start once concurrent requests per instance pass eighty. What setting decides that?

- A. Add capacity on a fixed calendar schedule
- B. Put the instance group behind an autoscaler on CPU
- C. Scale on queue depth with a horizontal pod autoscaler
- D. Set Cloud Run concurrency so replicas follow load

### 59. Traffic must move to a healthy region at the name level, and also at the load balancer when a backend fails. Which two controls apply? Select two.

- A. Add capacity in a second region
- B. Drain connections before removing the instance
- C. Request a quota increase and reserve capacity before the launch
- D. Use a load balancer failover backend
- E. Shift traffic with a DNS routing policy

### 60. A pod receives a termination signal while it is handling a slow upload. What must happen?

- A. Add capacity in a second region
- B. Use a load balancer failover backend
- C. Drain connections before removing the instance
- D. Shift traffic with a DNS routing policy

### 61. A flash sale exhausts the primary region and buyers must still be served. What should be done?

- A. Request a quota increase and reserve capacity before the launch
- B. Add capacity in a second region
- C. Drain connections before removing the instance
- D. Use a load balancer failover backend

### 62. The new release adds a column that the previous release cannot read. What should have existed?

- A. Patch production by hand and reconcile later
- B. Wait for the error rate to settle on its own
- C. Reverse the schema change with a tested down migration
- D. Redeploy the previous image to the affected service

### 63. A midnight fix was applied to production and never entered the repository. What is the consequence?

- A. Redeploy the previous image to the affected service
- B. Reverse the schema change with a tested down migration
- C. Patch production by hand and reconcile later
- D. Schedule a plan that reports drift

---

## Domain 4 — Implementing Observability Practices and Troubleshooting (Telemetry, Alerting, and Diagnosis)

### 64. A security review wants every accepted and denied connection from one subnet. What provides that?

- A. Read the Cloud Service Mesh telemetry
- B. Turn on VPC Flow Logs for the subnet
- C. Install the Ops Agent on the instances
- D. Enable Data Access audit logs for the service

### 65. An investigation needs to know which identity read a specific object. What provides that?

- A. Enable Data Access audit logs for the service
- B. Install the Ops Agent on the instances
- C. Run an OpenTelemetry Collector in the cluster
- D. Turn on VPC Flow Logs for the subnet

### 66. Verbose tracing statements multiply ingest by five while errors must stay complete. What fits?

- A. Add an exclusion for the health-check entries
- B. Measure log volume per service before choosing a retention period
- C. Sample the high-volume debug entries
- D. Drop the high-cardinality user label from the metric

### 67. Finance asks why observability spend doubled and nobody has the ingest figure. What should be done first?

- A. Set the log bucket retention and lock it
- B. Add an exclusion for the health-check entries
- C. Measure log volume per service before choosing a retention period
- D. Sample the high-volume debug entries

### 68. Only error entries from the payments service matter this morning. What should be used?

- A. Create a log-based metric for the error string
- B. Filter with the Logging query language on the resource label
- C. Open the Logs Explorer and pivot from the error entry
- D. Route the entries to a Cloud Storage bucket

### 69. Entries must be joined with orders to count failures per merchant. What fits?

- A. Set the log bucket retention and lock it
- B. Route the entries to a Cloud Storage bucket
- C. Route the entries to a Pub/Sub topic
- D. Route the entries to a BigQuery dataset

### 70. Seven years of entries must be retained cheaply, and an administrator must not be able to shorten that period. Which two choices apply? Select two.

- A. Measure log volume per service before choosing a retention period
- B. Route the entries to a BigQuery dataset
- C. Route the entries to a Cloud Storage bucket
- D. Route the entries to a Pub/Sub topic
- E. Set the log bucket retention and lock it

### 71. A streaming consumer must act on entries as they arrive. What fits?

- A. Route the entries to a BigQuery dataset
- B. Route the entries to a Cloud Storage bucket
- C. Set the log bucket retention and lock it
- D. Route the entries to a Pub/Sub topic

### 72. Credit card numbers appear in request logs and must not be stored at all. What should be configured?

- A. Ask analysts not to read the sensitive field
- B. Sample the high-volume debug entries
- C. Route the entries to a Cloud Storage bucket
- D. Redact the email field with a log processor

### 73. An engineer wants the failing entries summarised, and the dominant span named. Which two capabilities apply? Select two.

- A. Ask Gemini Cloud Assist which span dominates the trace
- B. Filter with the Logging query language on the resource label
- C. Open the Logs Explorer and pivot from the error entry
- D. Ask Gemini Cloud Assist to summarise the failing entries
- E. Ask Gemini Cloud Assist to explain the metric spike

### 74. A GPU exporter must be scraped without anyone running a Prometheus server. What fits?

- A. Create a log-based metric for the error string
- B. Emit a custom metric for the business event
- C. Scrape the workload with managed collection for Prometheus
- D. Run an OpenTelemetry Collector in the cluster

### 75. A queue consumer must report its own batch size as a measurement. What should it do?

- A. Emit a custom metric for the business event
- B. Create a log-based metric for the error string
- C. Create an uptime check against the login flow
- D. Scrape the workload with managed collection for Prometheus

### 76. A deprecation warning count is needed from logs that already exist, tonight. What fits?

- A. Scrape the workload with managed collection for Prometheus
- B. Create a log-based metric for the error string
- C. Emit a custom metric for the business event
- D. Create an uptime check against the login flow

### 77. A login flow must be probed from outside, and an error string in the logs must become countable. Which two capabilities apply? Select two.

- A. Build one dashboard and share it with the on-call rotation
- B. Scrape the workload with managed collection for Prometheus
- C. Emit a custom metric for the business event
- D. Create an uptime check against the login flow
- E. Create a log-based metric for the error string

### 78. Ten teams want the same service view without rebuilding it every sprint. What should be built?

- A. Build one dashboard and share it with the on-call rotation
- B. Send the alert to PagerDuty through a webhook
- C. Alert when CPU stays above ninety percent for ten minutes
- D. Attach the remediation playbook to the alert

### 79. A runbook link must appear inside the incident for whoever responds. What fits?

- A. Build one dashboard and share it with the on-call rotation
- B. Add an email notification channel for the on-call group
- C. Attach the remediation playbook to the alert
- D. Create an alerting policy on the SLO burn rate

### 80. Alerts fire at eighty percent CPU on a service whose latency is unaffected. What is the problem?

- A. Send the alert to PagerDuty through a webhook
- B. Create an alerting policy on the SLO burn rate
- C. Alert when CPU stays above ninety percent for ten minutes
- D. Attach the remediation playbook to the alert

### 81. A page must fire when the error budget will run out in two days. What fits?

- A. Create an alerting policy on the SLO burn rate
- B. Create an uptime check against the login flow
- C. Alert when CPU stays above ninety percent for ten minutes
- D. Add an email notification channel for the on-call group

### 82. A paging tool outside Google Cloud must receive the alert within seconds of it firing. What fits?

- A. Attach the remediation playbook to the alert
- B. Add an email notification channel for the on-call group
- C. Send the alert to PagerDuty through a webhook
- D. Alert when CPU stays above ninety percent for ten minutes

### 83. A reviewer must see which of nine spans in one request took nine hundred milliseconds. What fits?

- A. Ask Gemini Cloud Assist which span dominates the trace
- B. Put the trace ID in the structured log line
- C. Instrument the service with OpenTelemetry spans
- D. Read the trace waterfall to find the slow span

### 84. A structured log line must link back to the trace that produced it. What provides the link?

- A. Put the trace ID in the structured log line
- B. Instrument the service with OpenTelemetry spans
- C. Log a timestamp and correlate by eye later
- D. Read the trace waterfall to find the slow span

### 85. Latency rises only when the connection pool is full. Which analysis explains that?

- A. Put the trace ID in the structured log line
- B. Compare latency with the saturation metric
- C. Instrument the service with OpenTelemetry spans
- D. Read the trace waterfall to find the slow span

### 86. Outbound calls fail intermittently at peak, and a resource creation request was refused yesterday. Which two should be checked? Select two.

- A. Read the firewall rule that hit the denied flow
- B. Check Cloud NAT port exhaustion for the egress range
- C. Check the quota error in the deployment log
- D. Inspect the image pull credential and repository permission
- E. Check the DNS record and its remaining TTL

### 87. A deployment never becomes ready although the container is running. What should be checked?

- A. Check Cloud NAT port exhaustion for the egress range
- B. Profile the slow endpoint inside the application
- C. Compare the readiness probe with the application startup time
- D. Check the DNS record and its remaining TTL

### 88. One endpoint is slow while its database and host metrics look healthy. What fits?

- A. Check the DNS record and its remaining TTL
- B. Profile the slow endpoint inside the application
- C. Compare the readiness probe with the application startup time
- D. Check Cloud NAT port exhaustion for the egress range

---

## Domain 5 — Optimizing Performance and Cost (FinOps and Performance Tuning)

### 89. A release doubled checkout time and nobody can say which call changed. What should be used?

- A. Measure request latency by endpoint in Cloud Monitoring
- B. Export billing data to BigQuery for the chargeback report
- C. Track the service objective on a shared dashboard
- D. Apply the cost recommender suggestion for the idle disks

### 90. A service page must show whether the reliability goal is currently met. What fits?

- A. Apply the cost recommender suggestion for the idle disks
- B. Track the service objective on a shared dashboard
- C. Measure log volume per service before choosing a retention period
- D. Measure request latency by endpoint in Cloud Monitoring

### 91. A team wants every suggestion Google has generated, and one of them concerns a limit that keeps blocking peaks. Which two should be used? Select two.

- A. Apply the reliability recommender for the missing quota
- B. Apply the cost recommender suggestion for the idle disks
- C. Run the batch on Spot VMs
- D. Review the Active Assist recommendations for the project
- E. Export billing data to BigQuery for the chargeback report

### 92. A project pays for disks that are not attached to anything. Which recommendation applies?

- A. Review the Active Assist recommendations for the project
- B. Apply the cost recommender suggestion for the idle disks
- C. Run the batch on Spot VMs
- D. Apply the reliability recommender for the missing quota

### 93. Ingest is dominated by debug lines that support never opens. What should be done?

- A. Set the log bucket retention and lock it
- B. Drop the high-cardinality user label from the metric
- C. Measure log volume per service before choosing a retention period
- D. Exclude the debug stream and keep the error stream

### 94. A metric carrying a request identifier creates millions of series. What caused that?

- A. Drop the high-cardinality user label from the metric
- B. Exclude the debug stream and keep the error stream
- C. Serve the bulk export over the Standard network tier
- D. Measure log volume per service before choosing a retention period

### 95. Stateless consumers can restart and are the biggest compute cost. What fits?

- A. Put the stateless workers on a Spot node pool
- B. Buy a committed-use discount for the steady baseline
- C. Move the primary database onto Spot capacity
- D. Run the batch on Spot VMs

### 96. A rendering farm may be interrupted at any point without harm. What fits?

- A. Put the stateless workers on a Spot node pool
- B. Move the primary database onto Spot capacity
- C. Buy a committed-use discount for the steady baseline
- D. Run the batch on Spot VMs

### 97. A predictable baseline should be discounted by contract, and bulk transfer should use the cheaper path. Which two choices apply? Select two.

- A. Run the batch on Spot VMs
- B. Buy a committed-use discount for the steady baseline
- C. Serve the bulk export over the Standard network tier
- D. Rely on sustained-use discounts for the steady baseline
- E. Keep the interactive traffic on the Premium tier

### 98. Customer-facing calls need the shortest path between continents. What fits?

- A. Buy a committed-use discount for the steady baseline
- B. Keep the interactive traffic on the Premium tier
- C. Put the stateless workers on a Spot node pool
- D. Serve the bulk export over the Standard network tier

### 99. Requests per pod show that half the reserved CPU is never used. What should be done?

- A. Set a minimum instance count for the latency-critical service
- B. Right-size the node pool from the observed requests
- C. Keep the minimum instance count at zero for the internal tool
- D. Put the stateless workers on a Spot node pool

### 100. Development VMs run overnight with no traffic at all. What should be done?

- A. Buy a committed-use discount for the steady baseline
- B. Keep the minimum instance count at zero for the internal tool
- C. Stop the idle non-production instances on a schedule
- D. Right-size the node pool from the observed requests

---

## Answer key and explanations

### Question 1 — A

Answer: Apply the constraint separately in each project. Per-project settings drift as owners come and go. A constraint set per project with no inheritance. Local study-map skill 1.1 (Resource Hierarchy and Project Organization), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 1 (bootstrapping and maintaining a Google Cloud organization): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Correct. A constraint set per project with no inheritance. In this case: Per-project settings drift as owners come and go.
- **B:** Incorrect for this question. An explicit denial that overrides any allow. Why the correct answer wins: Per-project settings drift as owners come and go.
- **C:** Incorrect for this question. A constraint attached to one folder and inherited by its projects. Why the correct answer wins: Per-project settings drift as owners come and go.
- **D:** Incorrect for this question. An organization-level constraint that every folder and project inherits. Why the correct answer wins: Per-project settings drift as owners come and go.

### Question 2 — A

Answer: Group projects by application inside each environment folder. Grouping by application keeps one service and its owners together. An application-centric layout that keeps one service and its owners together. Local study-map skill 1.1 (Resource Hierarchy and Project Organization), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 1 (bootstrapping and maintaining a Google Cloud organization): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Correct. An application-centric layout that keeps one service and its owners together. In this case: Grouping by application keeps one service and its owners together.
- **B:** Incorrect for this question. A constraint attached to one folder and inherited by its projects. Why the correct answer wins: Grouping by application keeps one service and its owners together.
- **C:** Incorrect for this question. A constraint set per project with no inheritance. Why the correct answer wins: Grouping by application keeps one service and its owners together.
- **D:** Incorrect for this question. An environment-centric layout that separates production from staging first. Why the correct answer wins: Grouping by application keeps one service and its owners together.

### Question 3 — B

Answer: Publish the service behind a Private Service Connect endpoint. A published endpoint keeps the call off the public internet. A private endpoint that consumes a published service. Local study-map skill 1.2 (Shared Networking for Multi-Project Estates), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 1 (bootstrapping and maintaining a Google Cloud organization): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A central network project that lends subnets to other projects. Why the correct answer wins: A published endpoint keeps the call off the public internet.
- **B:** Correct. A private endpoint that consumes a published service. In this case: A published endpoint keeps the call off the public internet.
- **C:** Incorrect for this question. Duplicate networks with a separately managed egress path. Why the correct answer wins: A published endpoint keeps the call off the public internet.
- **D:** Incorrect for this question. A mesh of peering links that grows with each new project. Why the correct answer wins: A published endpoint keeps the call off the public internet.

### Question 4 — D

Answer: Give each project its own VPC and Cloud NAT. Duplicate networks multiply the policy surfaces to audit. Duplicate networks with a separately managed egress path. Local study-map skill 1.2 (Shared Networking for Multi-Project Estates), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 1 (bootstrapping and maintaining a Google Cloud organization): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A central network project that lends subnets to other projects. Why the correct answer wins: Duplicate networks multiply the policy surfaces to audit.
- **B:** Incorrect for this question. A mesh of peering links that grows with each new project. Why the correct answer wins: Duplicate networks multiply the policy surfaces to audit.
- **C:** Incorrect for this question. A private endpoint that consumes a published service. Why the correct answer wins: Duplicate networks multiply the policy surfaces to audit.
- **D:** Correct. Duplicate networks with a separately managed egress path. In this case: Duplicate networks multiply the policy surfaces to audit.

### Question 5 — A, B

Answers: Route every project log to one aggregated sink; Add the projects to one metrics scope. The aggregated sink gathers the entries, and the metrics scope charts them. A single destination that collects entries from many projects. An observability scope that spans several projects. Local study-map skill 1.3 (Multi-Project Monitoring and Logging), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 1 (bootstrapping and maintaining a Google Cloud organization): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Correct. An observability scope that spans several projects. In this case: The aggregated sink gathers the entries, and the metrics scope charts them.
- **B:** Correct. A single destination that collects entries from many projects. In this case: The aggregated sink gathers the entries, and the metrics scope charts them.
- **C:** Incorrect for this question. A central network project that lends subnets to other projects. Why the correct answer wins: The aggregated sink gathers the entries, and the metrics scope charts them.
- **D:** Incorrect for this question. A sink that streams entries to another consumer. Why the correct answer wins: The aggregated sink gathers the entries, and the metrics scope charts them.
- **E:** Incorrect for this question. Log storage scoped to the project that produced the entries. Why the correct answer wins: The aggregated sink gathers the entries, and the metrics scope charts them.

### Question 6 — D

Answer: Enforce the restriction with an organization policy constraint. The org policy applies regardless of the IAM grants. A guardrail that holds regardless of the IAM grants. Local study-map skill 1.4 (IAM Roles and Organization Policies), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 1 (bootstrapping and maintaining a Google Cloud organization): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A Google-managed role bound at folder level. Why the correct answer wins: The org policy applies regardless of the IAM grants.
- **B:** Incorrect for this question. An explicit denial that overrides any allow. Why the correct answer wins: The org policy applies regardless of the IAM grants.
- **C:** Incorrect for this question. A role defined from an explicit permission list. Why the correct answer wins: The org policy applies regardless of the IAM grants.
- **D:** Correct. A guardrail that holds regardless of the IAM grants. In this case: The org policy applies regardless of the IAM grants.

### Question 7 — B

Answer: Grant a custom role limited to the required permissions. A custom role limits the grant to those read permissions. A role defined from an explicit permission list. Local study-map skill 1.4 (IAM Roles and Organization Policies), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 1 (bootstrapping and maintaining a Google Cloud organization): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A Google-managed role bound at folder level. Why the correct answer wins: A custom role limits the grant to those read permissions.
- **B:** Correct. A role defined from an explicit permission list. In this case: A custom role limits the grant to those read permissions.
- **C:** Incorrect for this question. An explicit denial that overrides any allow. Why the correct answer wins: A custom role limits the grant to those read permissions.
- **D:** Incorrect for this question. A guardrail that holds regardless of the IAM grants. Why the correct answer wins: A custom role limits the grant to those read permissions.

### Question 8 — A

Answer: Let the workload use the default Compute Engine service account. The default account's broad access turns one compromise into many. The account created automatically with broad project access. Local study-map skill 1.5 (Service Account Management), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 1 (bootstrapping and maintaining a Google Cloud organization): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Correct. The account created automatically with broad project access. In this case: The default account's broad access turns one compromise into many.
- **B:** Incorrect for this question. A dedicated identity for each deployed workload. Why the correct answer wins: The default account's broad access turns one compromise into many.
- **C:** Incorrect for this question. Separate identities so a staging credential cannot act in production. Why the correct answer wins: The default account's broad access turns one compromise into many.
- **D:** Incorrect for this question. Short-lived credentials obtained by impersonating the account. Why the correct answer wins: The default account's broad access turns one compromise into many.

### Question 9 — D

Answer: Replicate the data to a second region. A second-region copy widens where the data lives. A copy held elsewhere for recovery rather than residency. Local study-map skill 1.6 (Data Residency in the Hierarchy), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 1 (bootstrapping and maintaining a Google Cloud organization): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. An organization-level constraint that every folder and project inherits. Why the correct answer wins: A second-region copy widens where the data lives.
- **B:** Incorrect for this question. A central network project that lends subnets to other projects. Why the correct answer wins: A second-region copy widens where the data lives.
- **C:** Incorrect for this question. A location choice that keeps data inside the required boundary. Why the correct answer wins: A second-region copy widens where the data lives.
- **D:** Correct. A copy held elsewhere for recovery rather than residency. In this case: A second-region copy widens where the data lives.

### Question 10 — C

Answer: Apply the deployment through Infrastructure Manager. Infrastructure Manager keeps the state and the audit trail. A managed service that runs Terraform deployments. Local study-map skill 1.7 (Infrastructure-as-Code Tool Selection), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 1 (bootstrapping and maintaining a Google Cloud organization): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Declarative code that is reviewed before it is applied. Why the correct answer wins: Infrastructure Manager keeps the state and the audit trail.
- **B:** Incorrect for this question. A controller that keeps Kubernetes manifests and cloud resources aligned. Why the correct answer wins: Infrastructure Manager keeps the state and the audit trail.
- **C:** Correct. A managed service that runs Terraform deployments. In this case: Infrastructure Manager keeps the state and the audit trail.
- **D:** Incorrect for this question. Idempotent automation through the client library. Why the correct answer wins: Infrastructure Manager keeps the state and the audit trail.

### Question 11 — A

Answer: Package the workload as a Helm chart. A Helm chart templates the structure and supplies values. A templated bundle of Kubernetes resources. Local study-map skill 1.7 (Infrastructure-as-Code Tool Selection), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 1 (bootstrapping and maintaining a Google Cloud organization): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Correct. A templated bundle of Kubernetes resources. In this case: A Helm chart templates the structure and supplies values.
- **B:** Incorrect for this question. A transformation pipeline that keeps the source declarative. Why the correct answer wins: A Helm chart templates the structure and supplies values.
- **C:** Incorrect for this question. Declarative code that is reviewed before it is applied. Why the correct answer wins: A Helm chart templates the structure and supplies values.
- **D:** Incorrect for this question. A controller that keeps Kubernetes manifests and cloud resources aligned. Why the correct answer wins: A Helm chart templates the structure and supplies values.

### Question 12 — B

Answer: Render the manifests through a kpt function pipeline. A kpt pipeline applies the transform to every source. A transformation pipeline that keeps the source declarative. Local study-map skill 1.8 (Blueprints and Controlled Infrastructure Change), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 1 (bootstrapping and maintaining a Google Cloud organization): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A recurring comparison of declared and actual state. Why the correct answer wins: A kpt pipeline applies the transform to every source.
- **B:** Correct. A transformation pipeline that keeps the source declarative. In this case: A kpt pipeline applies the transform to every source.
- **C:** Incorrect for this question. Declarative code that is reviewed before it is applied. Why the correct answer wins: A kpt pipeline applies the transform to every source.
- **D:** Incorrect for this question. A templated bundle of Kubernetes resources. Why the correct answer wins: A kpt pipeline applies the transform to every source.

### Question 13 — D, E

Answers: Automate the repeated step with a Python script calling the API; Apply the deployment through Infrastructure Manager. The script automates the step, and the managed service applies the code. Idempotent automation through the client library. A managed service that runs Terraform deployments. Local study-map skill 1.9 (Automation with Scripting and APIs), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 1 (bootstrapping and maintaining a Google Cloud organization): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. An unmanaged change with no enforceable record. Why the correct answer wins: The script automates the step, and the managed service applies the code.
- **B:** Incorrect for this question. A manual sequence repeated on every occasion. Why the correct answer wins: The script automates the step, and the managed service applies the code.
- **C:** Incorrect for this question. A recurring comparison of declared and actual state. Why the correct answer wins: The script automates the step, and the managed service applies the code.
- **D:** Correct. Idempotent automation through the client library. In this case: The script automates the step, and the managed service applies the code.
- **E:** Correct. A managed service that runs Terraform deployments. In this case: The script automates the step, and the managed service applies the code.

### Question 14 — C

Answer: Use Cloud Build for CI and Cloud Deploy for delivery. The managed pair carries one release through every target. A managed pair that separates building from releasing. Local study-map skill 1.10 (CI/CD Architecture Stack Design), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 1 (bootstrapping and maintaining a Google Cloud organization): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A reproducible image built before deployment. Why the correct answer wins: The managed pair carries one release through every target.
- **B:** Incorrect for this question. A pull-based delivery controller. Why the correct answer wins: The managed pair carries one release through every target.
- **C:** Correct. A managed pair that separates building from releasing. In this case: The managed pair carries one release through every target.
- **D:** Incorrect for this question. A self-operated CI server whose patching is your problem. Why the correct answer wins: The managed pair carries one release through every target.

### Question 15 — A

Answer: Store the build output in Artifact Registry. A regional repository scopes IAM and storage to that region. A regional repository for images and packages. Local study-map skill 1.10 (CI/CD Architecture Stack Design), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 1 (bootstrapping and maintaining a Google Cloud organization): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Correct. A regional repository for images and packages. In this case: A regional repository scopes IAM and storage to that region.
- **B:** Incorrect for this question. An immutable tag that identifies the source revision. Why the correct answer wins: A regional repository scopes IAM and storage to that region.
- **C:** Incorrect for this question. A reproducible image built before deployment. Why the correct answer wins: A regional repository scopes IAM and storage to that region.
- **D:** Incorrect for this question. The legacy registry without regional repository controls. Why the correct answer wins: A regional repository scopes IAM and storage to that region.

### Question 16 — D

Answer: Let Argo CD pull the manifests from Git. Argo CD pulls and reconciles without a push credential. A pull-based delivery controller. Local study-map skill 1.11 (Third-Party Tooling in the Pipeline), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 1 (bootstrapping and maintaining a Google Cloud organization): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A managed pair that separates building from releasing. Why the correct answer wins: Argo CD pulls and reconciles without a push credential.
- **B:** Incorrect for this question. A reproducible image built before deployment. Why the correct answer wins: Argo CD pulls and reconciles without a push credential.
- **C:** Incorrect for this question. A self-operated CI server whose patching is your problem. Why the correct answer wins: Argo CD pulls and reconciles without a push credential.
- **D:** Correct. A pull-based delivery controller. In this case: Argo CD pulls and reconciles without a push credential.

### Question 17 — D

Answer: Keep one shared staging environment for every team. One shared environment lets releases overwrite each other. A permanent pre-production environment. Local study-map skill 1.12 (Multiple Environment Management), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 1 (bootstrapping and maintaining a Google Cloud organization): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A base manifest with per-environment patches. Why the correct answer wins: One shared environment lets releases overwrite each other.
- **B:** Incorrect for this question. One image per environment with the settings compiled in. Why the correct answer wins: One shared environment lets releases overwrite each other.
- **C:** Incorrect for this question. An environment that exists only while a change is tested. Why the correct answer wins: One shared environment lets releases overwrite each other.
- **D:** Correct. A permanent pre-production environment. In this case: One shared environment lets releases overwrite each other.

### Question 18 — D

Answer: Upgrade each node pool by hand whenever an operator is free. Operator-driven upgrades stall when nobody has time. An operator-driven upgrade with no cadence. Local study-map skill 1.13 (Fleets, Patching, and Cluster Upgrades), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 1 (bootstrapping and maintaining a Google Cloud organization): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A group that shares policy and identity across clusters. Why the correct answer wins: Operator-driven upgrades stall when nobody has time.
- **B:** Incorrect for this question. A managed upgrade cadence inside a chosen window. Why the correct answer wins: Operator-driven upgrades stall when nobody has time.
- **C:** Incorrect for this question. A parallel cluster used to prove the upgrade. Why the correct answer wins: Operator-driven upgrades stall when nobody has time.
- **D:** Correct. An operator-driven upgrade with no cadence. In this case: Operator-driven upgrades stall when nobody has time.

### Question 19 — B, E

Answers: Give developers Cloud Workstations built from a custom image; Build a custom image that carries the approved toolchain. Cloud Workstations runs the IDE, and a custom image pins the toolchain. A managed IDE that runs inside the project boundary. A pinned toolchain that every workstation starts from. Local study-map skill 1.14 (Secure Development Environments and AI Assistance), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 1 (bootstrapping and maintaining a Google Cloud organization): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A browser terminal with limited tooling and lifetime. Why the correct answer wins: Cloud Workstations runs the IDE, and a custom image pins the toolchain.
- **B:** Correct. A managed IDE that runs inside the project boundary. In this case: Cloud Workstations runs the IDE, and a custom image pins the toolchain.
- **C:** Incorrect for this question. An in-editor assistant that proposes code. Why the correct answer wins: Cloud Workstations runs the IDE, and a custom image pins the toolchain.
- **D:** Incorrect for this question. Unmanaged toolchains on unmanaged machines. Why the correct answer wins: Cloud Workstations runs the IDE, and a custom image pins the toolchain.
- **E:** Correct. A pinned toolchain that every workstation starts from. In this case: Cloud Workstations runs the IDE, and a custom image pins the toolchain.

### Question 20 — D

Answer: Ask Gemini Cloud Assist to explain the resource state. Gemini Cloud Assist explains the observed resource state. An assistant that reads telemetry and configuration. Local study-map skill 1.14 (Secure Development Environments and AI Assistance), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 1 (bootstrapping and maintaining a Google Cloud organization): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Unmanaged toolchains on unmanaged machines. Why the correct answer wins: Gemini Cloud Assist explains the observed resource state.
- **B:** Incorrect for this question. A terminal assistant that drafts and runs commands. Why the correct answer wins: Gemini Cloud Assist explains the observed resource state.
- **C:** Incorrect for this question. An in-editor assistant that proposes code. Why the correct answer wins: Gemini Cloud Assist explains the observed resource state.
- **D:** Correct. An assistant that reads telemetry and configuration. In this case: Gemini Cloud Assist explains the observed resource state.

### Question 21 — B, C

Answers: Create a trigger that runs the tests on every pull request; Trigger the pipeline only on a signed tag. The pull-request trigger validates, and the tag trigger gates production. A pre-merge check that blocks a bad change early. A release build that a tag alone can start. Local study-map skill 2.1 (Pipeline Triggers and Design), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 2 (building and implementing CI/CD pipelines): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A hand-built artifact with no pipeline record. Why the correct answer wins: The pull-request trigger validates, and the tag trigger gates production.
- **B:** Correct. A pre-merge check that blocks a bad change early. In this case: The pull-request trigger validates, and the tag trigger gates production.
- **C:** Correct. A release build that a tag alone can start. In this case: The pull-request trigger validates, and the tag trigger gates production.
- **D:** Incorrect for this question. A required human approval before the release promotes. Why the correct answer wins: The pull-request trigger validates, and the tag trigger gates production.
- **E:** Incorrect for this question. A trigger that starts the build on a branch change. Why the correct answer wins: The pull-request trigger validates, and the tag trigger gates production.

### Question 22 — C

Answer: Create a Cloud Build trigger on the release branch. A branch trigger rebuilds when that branch moves. A trigger that starts the build on a branch change. Local study-map skill 2.1 (Pipeline Triggers and Design), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 2 (building and implementing CI/CD pipelines): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A hand-built artifact with no pipeline record. Why the correct answer wins: A branch trigger rebuilds when that branch moves.
- **B:** Incorrect for this question. A release build that a tag alone can start. Why the correct answer wins: A branch trigger rebuilds when that branch moves.
- **C:** Correct. A trigger that starts the build on a branch change. In this case: A branch trigger rebuilds when that branch moves.
- **D:** Incorrect for this question. A pre-merge check that blocks a bad change early. Why the correct answer wins: A branch trigger rebuilds when that branch moves.

### Question 23 — A

Answer: Have an engineer build locally and upload the result. A hand build varies with the engineer's machine. A hand-built artifact with no pipeline record. Local study-map skill 2.1 (Pipeline Triggers and Design), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 2 (building and implementing CI/CD pipelines): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Correct. A hand-built artifact with no pipeline record. In this case: A hand build varies with the engineer's machine.
- **B:** Incorrect for this question. A release build that a tag alone can start. Why the correct answer wins: A hand build varies with the engineer's machine.
- **C:** Incorrect for this question. The immutable record of who released what. Why the correct answer wins: A hand build varies with the engineer's machine.
- **D:** Incorrect for this question. A pre-merge check that blocks a bad change early. Why the correct answer wins: A hand build varies with the engineer's machine.

### Question 24 — A

Answer: Reuse the latest tag for every build. A reused tag silently changes what will be deployed. A moving tag that hides which build is running. Local study-map skill 2.2 (Artifact Management), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 2 (building and implementing CI/CD pipelines): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Correct. A moving tag that hides which build is running. In this case: A reused tag silently changes what will be deployed.
- **B:** Incorrect for this question. Metadata that ties an artifact to its build inputs. Why the correct answer wins: A reused tag silently changes what will be deployed.
- **C:** Incorrect for this question. A regional repository for images and packages. Why the correct answer wins: A reused tag silently changes what will be deployed.
- **D:** Incorrect for this question. An immutable tag that identifies the source revision. Why the correct answer wins: A reused tag silently changes what will be deployed.

### Question 25 — D

Answer: Store the build output in Artifact Registry. The repository applies the cleanup policy automatically. A regional repository for images and packages. Local study-map skill 2.2 (Artifact Management), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 2 (building and implementing CI/CD pipelines): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. The legacy registry without regional repository controls. Why the correct answer wins: The repository applies the cleanup policy automatically.
- **B:** Incorrect for this question. An immutable tag that identifies the source revision. Why the correct answer wins: The repository applies the cleanup policy automatically.
- **C:** Incorrect for this question. A moving tag that hides which build is running. Why the correct answer wins: The repository applies the cleanup policy automatically.
- **D:** Correct. A regional repository for images and packages. In this case: The repository applies the cleanup policy automatically.

### Question 26 — B

Answer: Deliver to a Cloud Run service revision. A Cloud Run target shifts traffic between revisions. A revision-based target with traffic control. Local study-map skill 2.3 (Hybrid and Multicloud Deployment Targets), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 2 (building and implementing CI/CD pipelines): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A delivery target that sits inside the same project. Why the correct answer wins: A Cloud Run target shifts traffic between revisions.
- **B:** Correct. A revision-based target with traffic control. In this case: A Cloud Run target shifts traffic between revisions.
- **C:** Incorrect for this question. A target that points at a GKE cluster outside Google Cloud. Why the correct answer wins: A Cloud Run target shifts traffic between revisions.
- **D:** Incorrect for this question. A required human approval before the release promotes. Why the correct answer wins: A Cloud Run target shifts traffic between revisions.

### Question 27 — A

Answer: Use a GKE cluster in the pipeline project as the target. A GKE target needs no extra cluster registration. A delivery target that sits inside the same project. Local study-map skill 2.3 (Hybrid and Multicloud Deployment Targets), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 2 (building and implementing CI/CD pipelines): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Correct. A delivery target that sits inside the same project. In this case: A GKE target needs no extra cluster registration.
- **B:** Incorrect for this question. A revision-based target with traffic control. Why the correct answer wins: A GKE target needs no extra cluster registration.
- **C:** Incorrect for this question. A target that points at a GKE cluster outside Google Cloud. Why the correct answer wins: A GKE target needs no extra cluster registration.
- **D:** Incorrect for this question. The immutable record of who released what. Why the correct answer wins: A GKE target needs no extra cluster registration.

### Question 28 — A

Answer: Promote automatically to every target in the chain. Unattended promotion removes the review that catches mistakes. An unattended path from commit to production. Local study-map skill 2.4 (Approval Flows and Deployment Process), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 2 (building and implementing CI/CD pipelines): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Correct. An unattended path from commit to production. In this case: Unattended promotion removes the review that catches mistakes.
- **B:** Incorrect for this question. The immutable record of who released what. Why the correct answer wins: Unattended promotion removes the review that catches mistakes.
- **C:** Incorrect for this question. A hand-built artifact with no pipeline record. Why the correct answer wins: Unattended promotion removes the review that catches mistakes.
- **D:** Incorrect for this question. A required human approval before the release promotes. Why the correct answer wins: Unattended promotion removes the review that catches mistakes.

### Question 29 — C

Answer: Describe the build with its supply chain level and signed provenance. The supply chain level answers that questionnaire. A published statement about how the artifact was produced. Local study-map skill 2.5 (Deployment Auditing and Tracking), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 2 (building and implementing CI/CD pipelines): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. The immutable record of who released what. Why the correct answer wins: The supply chain level answers that questionnaire.
- **B:** Incorrect for this question. An admission check that only attested images may run. Why the correct answer wins: The supply chain level answers that questionnaire.
- **C:** Correct. A published statement about how the artifact was produced. In this case: The supply chain level answers that questionnaire.
- **D:** Incorrect for this question. Metadata that ties an artifact to its build inputs. Why the correct answer wins: The supply chain level answers that questionnaire.

### Question 30 — D

Answer: Tag each artifact with the commit SHA and forbid overwrite. An immutable tag keeps the artifact identical to the build. An immutable tag that identifies the source revision. Local study-map skill 2.5 (Deployment Auditing and Tracking), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 2 (building and implementing CI/CD pipelines): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Metadata that ties an artifact to its build inputs. Why the correct answer wins: An immutable tag keeps the artifact identical to the build.
- **B:** Incorrect for this question. The immutable record of who released what. Why the correct answer wins: An immutable tag keeps the artifact identical to the build.
- **C:** Incorrect for this question. A moving tag that hides which build is running. Why the correct answer wins: An immutable tag keeps the artifact identical to the build.
- **D:** Correct. An immutable tag that identifies the source revision. In this case: An immutable tag keeps the artifact identical to the build.

### Question 31 — B

Answer: Stop the old version and then start the new one. Recreate stops the old version before starting the new one. A full outage during the change. Local study-map skill 2.6 (Deployment Strategies), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 2 (building and implementing CI/CD pipelines): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A small traffic slice that bounds the blast radius. Why the correct answer wins: Recreate stops the old version before starting the new one.
- **B:** Correct. A full outage during the change. In this case: Recreate stops the old version before starting the new one.
- **C:** Incorrect for this question. A gradual replacement of the running instances. Why the correct answer wins: Recreate stops the old version before starting the new one.
- **D:** Incorrect for this question. Two full environments with an instant cutover. Why the correct answer wins: Recreate stops the old version before starting the new one.

### Question 32 — B

Answer: Split traffic with a Cloud Service Mesh route. A mesh route splits traffic by weighted destination. Weighted routing between two service versions. Local study-map skill 2.6 (Deployment Strategies), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 2 (building and implementing CI/CD pipelines): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A small traffic slice that bounds the blast radius. Why the correct answer wins: A mesh route splits traffic by weighted destination.
- **B:** Correct. Weighted routing between two service versions. In this case: A mesh route splits traffic by weighted destination.
- **C:** Incorrect for this question. Two full environments with an instant cutover. Why the correct answer wins: A mesh route splits traffic by weighted destination.
- **D:** Incorrect for this question. A gradual replacement of the running instances. Why the correct answer wins: A mesh route splits traffic by weighted destination.

### Question 33 — B

Answer: Run the new version alongside and switch traffic at once. Blue/green keeps an identical stack ready for cutover. Two full environments with an instant cutover. Local study-map skill 2.6 (Deployment Strategies), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 2 (building and implementing CI/CD pipelines): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A small traffic slice that bounds the blast radius. Why the correct answer wins: Blue/green keeps an identical stack ready for cutover.
- **B:** Correct. Two full environments with an instant cutover. In this case: Blue/green keeps an identical stack ready for cutover.
- **C:** Incorrect for this question. A gradual replacement of the running instances. Why the correct answer wins: Blue/green keeps an identical stack ready for cutover.
- **D:** Incorrect for this question. A full outage during the change. Why the correct answer wins: Blue/green keeps an identical stack ready for cutover.

### Question 34 — B

Answer: Gate the rollout on the error-rate SLI. The SLI gate stops the rollout on user-visible failure. An automated decision driven by the service objective. Local study-map skill 2.7 (Deployment Success Metrics), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 2 (building and implementing CI/CD pipelines): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A required human approval before the release promotes. Why the correct answer wins: The SLI gate stops the rollout on user-visible failure.
- **B:** Correct. An automated decision driven by the service objective. In this case: The SLI gate stops the rollout on user-visible failure.
- **C:** Incorrect for this question. A resource signal that says nothing about user success. Why the correct answer wins: The SLI gate stops the rollout on user-visible failure.
- **D:** Incorrect for this question. A probe that exercises the path from outside. Why the correct answer wins: The SLI gate stops the rollout on user-visible failure.

### Question 35 — B, E

Answers: Start from the failed step log in Cloud Build; Make the failed step idempotent and re-run it. The step log names the failure, and an idempotent step repeats safely. The step output that names the failing command. A safe repeat that converges on the same state. Local study-map skill 2.8 (Troubleshooting Deployment Issues), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 2 (building and implementing CI/CD pipelines): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. An untracked change to the live environment. Why the correct answer wins: The step log names the failure, and an idempotent step repeats safely.
- **B:** Correct. A safe repeat that converges on the same state. In this case: The step log names the failure, and an idempotent step repeats safely.
- **C:** Incorrect for this question. The immutable record of who released what. Why the correct answer wins: The step log names the failure, and an idempotent step repeats safely.
- **D:** Incorrect for this question. A return to the last known good release. Why the correct answer wins: The step log names the failure, and an idempotent step repeats safely.
- **E:** Correct. The step output that names the failing command. In this case: The step log names the failure, and an idempotent step repeats safely.

### Question 36 — D

Answer: Roll the release back to the previous one. The rollout returns to the release that was healthy. A return to the last known good release. Local study-map skill 2.8 (Troubleshooting Deployment Issues), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 2 (building and implementing CI/CD pipelines): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. The step output that names the failing command. Why the correct answer wins: The rollout returns to the release that was healthy.
- **B:** Incorrect for this question. An untracked change to the live environment. Why the correct answer wins: The rollout returns to the release that was healthy.
- **C:** Incorrect for this question. A safe repeat that converges on the same state. Why the correct answer wins: The rollout returns to the release that was healthy.
- **D:** Correct. A return to the last known good release. In this case: The rollout returns to the release that was healthy.

### Question 37 — B

Answer: Encrypt the payload with a Cloud KMS key. Cloud KMS logs each use of the key. A managed key that wraps the data. Local study-map skill 2.9 (Key Management), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 2 (building and implementing CI/CD pipelines): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Managed issuance and renewal for the endpoint. Why the correct answer wins: Cloud KMS logs each use of the key.
- **B:** Correct. A managed key that wraps the data. In this case: Cloud KMS logs each use of the key.
- **C:** Incorrect for this question. A secret readable by everyone with repository access. Why the correct answer wins: Cloud KMS logs each use of the key.
- **D:** Incorrect for this question. A managed store with immutable versions and audit. Why the correct answer wins: Cloud KMS logs each use of the key.

### Question 38 — A

Answer: Issue and rotate the certificate with Certificate Manager. Certificate Manager renews the certificate automatically. Managed issuance and renewal for the endpoint. Local study-map skill 2.9 (Key Management), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 2 (building and implementing CI/CD pipelines): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Correct. Managed issuance and renewal for the endpoint. In this case: Certificate Manager renews the certificate automatically.
- **B:** Incorrect for this question. A managed key that wraps the data. Why the correct answer wins: Certificate Manager renews the certificate automatically.
- **C:** Incorrect for this question. A managed store with immutable versions and audit. Why the correct answer wins: Certificate Manager renews the certificate automatically.
- **D:** Incorrect for this question. A store for versioned application parameters. Why the correct answer wins: Certificate Manager renews the certificate automatically.

### Question 39 — B, C

Answers: Store the credential in Secret Manager with versions; Keep the non-secret configuration in Parameter Manager. Secret Manager versions the credentials, and Parameter Manager versions the settings. A managed store with immutable versions and audit. A store for versioned application parameters. Local study-map skill 2.10 (Configuration and Secret Management), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 2 (building and implementing CI/CD pipelines): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A value left visible in the build history. Why the correct answer wins: Secret Manager versions the credentials, and Parameter Manager versions the settings.
- **B:** Correct. A managed store with immutable versions and audit. In this case: Secret Manager versions the credentials, and Parameter Manager versions the settings.
- **C:** Correct. A store for versioned application parameters. In this case: Secret Manager versions the credentials, and Parameter Manager versions the settings.
- **D:** Incorrect for this question. A secret readable by everyone with repository access. Why the correct answer wins: Secret Manager versions the credentials, and Parameter Manager versions the settings.
- **E:** Incorrect for this question. One image per environment with the settings compiled in. Why the correct answer wins: Secret Manager versions the credentials, and Parameter Manager versions the settings.

### Question 40 — C

Answer: Commit the credential to the private repository. A committed secret is readable by everyone with repository access. Local study-map skill 2.10 (Configuration and Secret Management), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 2 (building and implementing CI/CD pipelines): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A managed store with immutable versions and audit. Why the correct answer wins: A committed secret is readable by everyone with repository access.
- **B:** Incorrect for this question. A store for versioned application parameters. Why the correct answer wins: A committed secret is readable by everyone with repository access.
- **C:** Correct. In this case: A committed secret is readable by everyone with repository access.
- **D:** Incorrect for this question. A credential read only when the workload starts. Why the correct answer wins: A committed secret is readable by everyone with repository access.

### Question 41 — A

Answer: Pass the secret as a build argument. A build argument is recorded in the image history. A value left visible in the build history. Local study-map skill 2.11 (Build-Time versus Runtime Secret Injection), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 2 (building and implementing CI/CD pipelines): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Correct. A value left visible in the build history. In this case: A build argument is recorded in the image history.
- **B:** Incorrect for this question. A credential read only when the workload starts. Why the correct answer wins: A build argument is recorded in the image history.
- **C:** Incorrect for this question. A secret baked into an artifact anyone can pull. Why the correct answer wins: A build argument is recorded in the image history.
- **D:** Incorrect for this question. A managed store with immutable versions and audit. Why the correct answer wins: A build argument is recorded in the image history.

### Question 42 — C

Answer: Keep the scan report for the monthly review. A dashboard finding blocks nothing on its own. A finding that no pipeline blocks on. Local study-map skill 2.12 (Vulnerability Scanning and Artifact Analysis), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 2 (building and implementing CI/CD pipelines): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A policy that blocks the promotion. Why the correct answer wins: A dashboard finding blocks nothing on its own.
- **B:** Incorrect for this question. Vulnerability findings for the stored artifacts. Why the correct answer wins: A dashboard finding blocks nothing on its own.
- **C:** Correct. A finding that no pipeline blocks on. In this case: A dashboard finding blocks nothing on its own.
- **D:** Incorrect for this question. An admission check that only attested images may run. Why the correct answer wins: A dashboard finding blocks nothing on its own.

### Question 43 — C

Answer: Enable Artifact Analysis scanning on the repository. Artifact Analysis keeps findings current for stored images. Vulnerability findings for the stored artifacts. Local study-map skill 2.13 (Supply Chain Security and Binary Authorization), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 2 (building and implementing CI/CD pipelines): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A finding that no pipeline blocks on. Why the correct answer wins: Artifact Analysis keeps findings current for stored images.
- **B:** Incorrect for this question. An admission check that only attested images may run. Why the correct answer wins: Artifact Analysis keeps findings current for stored images.
- **C:** Correct. Vulnerability findings for the stored artifacts. In this case: Artifact Analysis keeps findings current for stored images.
- **D:** Incorrect for this question. A policy that blocks the promotion. Why the correct answer wins: Artifact Analysis keeps findings current for stored images.

### Question 44 — C

Answer: Fail the pipeline on a critical vulnerability finding. The gate blocks promotion on that finding. A policy that blocks the promotion. Local study-map skill 2.13 (Supply Chain Security and Binary Authorization), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 2 (building and implementing CI/CD pipelines): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A finding that no pipeline blocks on. Why the correct answer wins: The gate blocks promotion on that finding.
- **B:** Incorrect for this question. An admission check that only attested images may run. Why the correct answer wins: The gate blocks promotion on that finding.
- **C:** Correct. A policy that blocks the promotion. In this case: The gate blocks promotion on that finding.
- **D:** Incorrect for this question. An identity that cannot promote outside its environment. Why the correct answer wins: The gate blocks promotion on that finding.

### Question 45 — A, E

Answers: Bind deploy permissions only inside the production project; Create one service account per environment. The scoped binding limits the deployer, and one account per environment isolates it. An identity that cannot promote outside its environment. Separate identities so a staging credential cannot act in production. Local study-map skill 2.14 (Per-Environment IAM Policy), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 2 (building and implementing CI/CD pipelines): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Correct. Separate identities so a staging credential cannot act in production. In this case: The scoped binding limits the deployer, and one account per environment isolates it.
- **B:** Incorrect for this question. A single broad credential across the whole estate. Why the correct answer wins: The scoped binding limits the deployer, and one account per environment isolates it.
- **C:** Incorrect for this question. A long-lived credential stored outside the platform. Why the correct answer wins: The scoped binding limits the deployer, and one account per environment isolates it.
- **D:** Incorrect for this question. A build identity with broad write access. Why the correct answer wins: The scoped binding limits the deployer, and one account per environment isolates it.
- **E:** Correct. An identity that cannot promote outside its environment. In this case: The scoped binding limits the deployer, and one account per environment isolates it.

### Question 46 — B

Answer: Set an internal target on that indicator. An SLO is the target the team holds itself to. An objective the team commits to without a contract. Local study-map skill 3.1 (SLIs, SLOs, and SLAs), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 3 (applying site reliability engineering practices): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. An external commitment that carries a consequence. Why the correct answer wins: An SLO is the target the team holds itself to.
- **B:** Correct. An objective the team commits to without a contract. In this case: An SLO is the target the team holds itself to.
- **C:** Incorrect for this question. A measured indicator of how the service behaves. Why the correct answer wins: An SLO is the target the team holds itself to.
- **D:** Incorrect for this question. A signal that the budget is going too quickly. Why the correct answer wins: An SLO is the target the team holds itself to.

### Question 47 — A

Answer: Track the ratio of good requests to total requests. An SLI is the measured share of good requests. A measured indicator of how the service behaves. Local study-map skill 3.1 (SLIs, SLOs, and SLAs), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 3 (applying site reliability engineering practices): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Correct. A measured indicator of how the service behaves. In this case: An SLI is the measured share of good requests.
- **B:** Incorrect for this question. An objective the team commits to without a contract. Why the correct answer wins: An SLI is the measured share of good requests.
- **C:** Incorrect for this question. An external commitment that carries a consequence. Why the correct answer wins: An SLI is the measured share of good requests.
- **D:** Incorrect for this question. A uniform promise that most services do not need. Why the correct answer wins: An SLI is the measured share of good requests.

### Question 48 — A

Answer: Publish a contractual promise with a remedy. An SLA attaches a remedy to the promise. An external commitment that carries a consequence. Local study-map skill 3.1 (SLIs, SLOs, and SLAs), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 3 (applying site reliability engineering practices): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Correct. An external commitment that carries a consequence. In this case: An SLA attaches a remedy to the promise.
- **B:** Incorrect for this question. A measured indicator of how the service behaves. Why the correct answer wins: An SLA attaches a remedy to the promise.
- **C:** Incorrect for this question. An explicit trade between reliability and change. Why the correct answer wins: An SLA attaches a remedy to the promise.
- **D:** Incorrect for this question. An objective the team commits to without a contract. Why the correct answer wins: An SLA attaches a remedy to the promise.

### Question 49 — B

Answer: Stop feature releases when the error budget is spent. A written rule pauses launches when the budget is spent. A rule that trades velocity for reliability. Local study-map skill 3.2 (Error Budgets), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 3 (applying site reliability engineering practices): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A uniform promise that most services do not need. Why the correct answer wins: A written rule pauses launches when the budget is spent.
- **B:** Correct. A rule that trades velocity for reliability. In this case: A written rule pauses launches when the budget is spent.
- **C:** Incorrect for this question. A signal that the budget is going too quickly. Why the correct answer wins: A written rule pauses launches when the budget is spent.
- **D:** Incorrect for this question. An external commitment that carries a consequence. Why the correct answer wins: A written rule pauses launches when the budget is spent.

### Question 50 — D

Answer: Alert on a fast error-budget burn rate. Burn rate projects when the budget will run out. A signal that the budget is going too quickly. Local study-map skill 3.2 (Error Budgets), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 3 (applying site reliability engineering practices): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A rule that trades velocity for reliability. Why the correct answer wins: Burn rate projects when the budget will run out.
- **B:** Incorrect for this question. A static threshold on a resource metric. Why the correct answer wins: Burn rate projects when the budget will run out.
- **C:** Incorrect for this question. An external commitment that carries a consequence. Why the correct answer wins: Burn rate projects when the budget will run out.
- **D:** Correct. A signal that the budget is going too quickly. In this case: Burn rate projects when the budget will run out.

### Question 51 — B, D

Answers: Choose three nines and spend the difference on features; Stop feature releases when the error budget is spent. Three nines matches cost to need, and the freeze protects the target. An explicit trade between reliability and change. A rule that trades velocity for reliability. Local study-map skill 3.3 (Cost of Reliability and Nines), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 3 (applying site reliability engineering practices): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. An owned entry with its tier and dependencies. Why the correct answer wins: Three nines matches cost to need, and the freeze protects the target.
- **B:** Correct. A rule that trades velocity for reliability. In this case: Three nines matches cost to need, and the freeze protects the target.
- **C:** Incorrect for this question. A uniform promise that most services do not need. Why the correct answer wins: Three nines matches cost to need, and the freeze protects the target.
- **D:** Correct. An explicit trade between reliability and change. In this case: Three nines matches cost to need, and the freeze protects the target.
- **E:** Incorrect for this question. An external commitment that carries a consequence. Why the correct answer wins: Three nines matches cost to need, and the freeze protects the target.

### Question 52 — D

Answer: Assume five nines for every service. One extreme target for every service overspends on effort. A uniform promise that most services do not need. Local study-map skill 3.3 (Cost of Reliability and Nines), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 3 (applying site reliability engineering practices): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. An explicit trade between reliability and change. Why the correct answer wins: One extreme target for every service overspends on effort.
- **B:** Incorrect for this question. An external commitment that carries a consequence. Why the correct answer wins: One extreme target for every service overspends on effort.
- **C:** Incorrect for this question. Capacity arranged ahead of a known peak. Why the correct answer wins: One extreme target for every service overspends on effort.
- **D:** Correct. A uniform promise that most services do not need. In this case: One extreme target for every service overspends on effort.

### Question 53 — C, E

Answers: Register the service in the service catalog; Announce the retirement date and withdraw traffic gradually. The catalog names the owner, and the retirement plan sets the date. An owned entry with its tier and dependencies. A planned withdrawal with a migration path. Local study-map skill 3.4 (Service Lifecycle Management), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 3 (applying site reliability engineering practices): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Capacity arranged ahead of a known peak. Why the correct answer wins: The catalog names the owner, and the retirement plan sets the date.
- **B:** Incorrect for this question. An unowned workload that still costs money. Why the correct answer wins: The catalog names the owner, and the retirement plan sets the date.
- **C:** Correct. A planned withdrawal with a migration path. In this case: The catalog names the owner, and the retirement plan sets the date.
- **D:** Incorrect for this question. Extra supply in a different location. Why the correct answer wins: The catalog names the owner, and the retirement plan sets the date.
- **E:** Correct. An owned entry with its tier and dependencies. In this case: The catalog names the owner, and the retirement plan sets the date.

### Question 54 — D

Answer: Leave the unused service running for now. An unowned pilot keeps billing until somebody retires it. An unowned workload that still costs money. Local study-map skill 3.4 (Service Lifecycle Management), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 3 (applying site reliability engineering practices): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. An owned entry with its tier and dependencies. Why the correct answer wins: An unowned pilot keeps billing until somebody retires it.
- **B:** Incorrect for this question. A planned withdrawal with a migration path. Why the correct answer wins: An unowned pilot keeps billing until somebody retires it.
- **C:** Incorrect for this question. A graceful handover of in-flight requests. Why the correct answer wins: An unowned pilot keeps billing until somebody retires it.
- **D:** Correct. An unowned workload that still costs money. In this case: An unowned pilot keeps billing until somebody retires it.

### Question 55 — C

Answer: Request a quota increase and reserve capacity before the launch. A quota increase secures headroom before the launch. Capacity arranged ahead of a known peak. Local study-map skill 3.5 (Capacity Planning and Quotas), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 3 (applying site reliability engineering practices): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Limits that throttle at the worst possible moment. Why the correct answer wins: A quota increase secures headroom before the launch.
- **B:** Incorrect for this question. Calendar-driven capacity with no feedback loop. Why the correct answer wins: A quota increase secures headroom before the launch.
- **C:** Correct. Capacity arranged ahead of a known peak. In this case: A quota increase secures headroom before the launch.
- **D:** Incorrect for this question. A flexible placement into a cheaper window. Why the correct answer wins: A quota increase secures headroom before the launch.

### Question 56 — C

Answer: Add capacity on a fixed calendar schedule. Calendar capacity ignores what the service actually needs. Calendar-driven capacity with no feedback loop. Local study-map skill 3.5 (Capacity Planning and Quotas), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 3 (applying site reliability engineering practices): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A flexible placement into a cheaper window. Why the correct answer wins: Calendar capacity ignores what the service actually needs.
- **B:** Incorrect for this question. Managed instance scaling from a resource metric. Why the correct answer wins: Calendar capacity ignores what the service actually needs.
- **C:** Correct. Calendar-driven capacity with no feedback loop. In this case: Calendar capacity ignores what the service actually needs.
- **D:** Incorrect for this question. Capacity arranged ahead of a known peak. Why the correct answer wins: Calendar capacity ignores what the service actually needs.

### Question 57 — D

Answer: Put the instance group behind an autoscaler on CPU. An instance group autoscaler follows the CPU signal. Managed instance scaling from a resource metric. Local study-map skill 3.6 (Autoscaling), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 3 (applying site reliability engineering practices): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Calendar-driven capacity with no feedback loop. Why the correct answer wins: An instance group autoscaler follows the CPU signal.
- **B:** Incorrect for this question. Concurrency-based replica scaling. Why the correct answer wins: An instance group autoscaler follows the CPU signal.
- **C:** Incorrect for this question. Replica scaling driven by a work signal. Why the correct answer wins: An instance group autoscaler follows the CPU signal.
- **D:** Correct. Managed instance scaling from a resource metric. In this case: An instance group autoscaler follows the CPU signal.

### Question 58 — D

Answer: Set Cloud Run concurrency so replicas follow load. Concurrency decides when another instance starts. Concurrency-based replica scaling. Local study-map skill 3.6 (Autoscaling), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 3 (applying site reliability engineering practices): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Calendar-driven capacity with no feedback loop. Why the correct answer wins: Concurrency decides when another instance starts.
- **B:** Incorrect for this question. Managed instance scaling from a resource metric. Why the correct answer wins: Concurrency decides when another instance starts.
- **C:** Incorrect for this question. Replica scaling driven by a work signal. Why the correct answer wins: Concurrency decides when another instance starts.
- **D:** Correct. Concurrency-based replica scaling. In this case: Concurrency decides when another instance starts.

### Question 59 — D, E

Answers: Shift traffic with a DNS routing policy; Use a load balancer failover backend. A routing policy moves the name, and a failover backend moves the traffic. A name-level redirect to a healthy region. A health-checked switch between backends. Local study-map skill 3.7 (Traffic Draining and Redirection), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 3 (applying site reliability engineering practices): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Extra supply in a different location. Why the correct answer wins: A routing policy moves the name, and a failover backend moves the traffic.
- **B:** Incorrect for this question. A graceful handover of in-flight requests. Why the correct answer wins: A routing policy moves the name, and a failover backend moves the traffic.
- **C:** Incorrect for this question. Capacity arranged ahead of a known peak. Why the correct answer wins: A routing policy moves the name, and a failover backend moves the traffic.
- **D:** Correct. A health-checked switch between backends. In this case: A routing policy moves the name, and a failover backend moves the traffic.
- **E:** Correct. A name-level redirect to a healthy region. In this case: A routing policy moves the name, and a failover backend moves the traffic.

### Question 60 — C

Answer: Drain connections before removing the instance. Draining lets the in-flight upload finish first. A graceful handover of in-flight requests. Local study-map skill 3.7 (Traffic Draining and Redirection), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 3 (applying site reliability engineering practices): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Extra supply in a different location. Why the correct answer wins: Draining lets the in-flight upload finish first.
- **B:** Incorrect for this question. A health-checked switch between backends. Why the correct answer wins: Draining lets the in-flight upload finish first.
- **C:** Correct. A graceful handover of in-flight requests. In this case: Draining lets the in-flight upload finish first.
- **D:** Incorrect for this question. A name-level redirect to a healthy region. Why the correct answer wins: Draining lets the in-flight upload finish first.

### Question 61 — B

Answer: Add capacity in a second region. Capacity in a second region serves the excess demand. Extra supply in a different location. Local study-map skill 3.8 (Incident Capacity), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 3 (applying site reliability engineering practices): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Capacity arranged ahead of a known peak. Why the correct answer wins: Capacity in a second region serves the excess demand.
- **B:** Correct. Extra supply in a different location. In this case: Capacity in a second region serves the excess demand.
- **C:** Incorrect for this question. A graceful handover of in-flight requests. Why the correct answer wins: Capacity in a second region serves the excess demand.
- **D:** Incorrect for this question. A health-checked switch between backends. Why the correct answer wins: Capacity in a second region serves the excess demand.

### Question 62 — C

Answer: Reverse the schema change with a tested down migration. A down migration restores compatibility with the older code. A paired migration that can be undone. Local study-map skill 3.9 (Rollback Strategies), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 3 (applying site reliability engineering practices): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. An untracked change to the live environment. Why the correct answer wins: A down migration restores compatibility with the older code.
- **B:** Incorrect for this question. No action while users are still failing. Why the correct answer wins: A down migration restores compatibility with the older code.
- **C:** Correct. A paired migration that can be undone. In this case: A down migration restores compatibility with the older code.
- **D:** Incorrect for this question. A known good artifact restored in place. Why the correct answer wins: A down migration restores compatibility with the older code.

### Question 63 — C

Answer: Patch production by hand and reconcile later. The live state now differs from the declared code. An untracked change to the live environment. Local study-map skill 3.9 (Rollback Strategies), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 3 (applying site reliability engineering practices): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A known good artifact restored in place. Why the correct answer wins: The live state now differs from the declared code.
- **B:** Incorrect for this question. A paired migration that can be undone. Why the correct answer wins: The live state now differs from the declared code.
- **C:** Correct. An untracked change to the live environment. In this case: The live state now differs from the declared code.
- **D:** Incorrect for this question. A recurring comparison of declared and actual state. Why the correct answer wins: The live state now differs from the declared code.

### Question 64 — B

Answer: Turn on VPC Flow Logs for the subnet. Flow logs record each accepted and denied connection. Per-connection records of accepted and denied traffic. Local study-map skill 4.1 (Log Collection and Ingestion), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 4 (implementing observability practices and troubleshooting): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Request metrics emitted by the sidecar proxies. Why the correct answer wins: Flow logs record each accepted and denied connection.
- **B:** Correct. Per-connection records of accepted and denied traffic. In this case: Flow logs record each accepted and denied connection.
- **C:** Incorrect for this question. A collector that ships logs and metrics from the VM. Why the correct answer wins: Flow logs record each accepted and denied connection.
- **D:** Incorrect for this question. A record of reads and writes on the resource. Why the correct answer wins: Flow logs record each accepted and denied connection.

### Question 65 — A

Answer: Enable Data Access audit logs for the service. Data Access audit logs record the reads. A record of reads and writes on the resource. Local study-map skill 4.1 (Log Collection and Ingestion), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 4 (implementing observability practices and troubleshooting): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Correct. A record of reads and writes on the resource. In this case: Data Access audit logs record the reads.
- **B:** Incorrect for this question. A collector that ships logs and metrics from the VM. Why the correct answer wins: Data Access audit logs record the reads.
- **C:** Incorrect for this question. A vendor-neutral pipeline for traces and metrics. Why the correct answer wins: Data Access audit logs record the reads.
- **D:** Incorrect for this question. Per-connection records of accepted and denied traffic. Why the correct answer wins: Data Access audit logs record the reads.

### Question 66 — C

Answer: Sample the high-volume debug entries. Sampling keeps the errors while cutting the volume. A fraction kept for diagnosis at lower cost. Local study-map skill 4.2 (Log Optimization and Cost), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 4 (implementing observability practices and troubleshooting): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A filter that drops matching entries before storage. Why the correct answer wins: Sampling keeps the errors while cutting the volume.
- **B:** Incorrect for this question. A cost estimate driven by actual ingest. Why the correct answer wins: Sampling keeps the errors while cutting the volume.
- **C:** Correct. A fraction kept for diagnosis at lower cost. In this case: Sampling keeps the errors while cutting the volume.
- **D:** Incorrect for this question. A label removal that cuts the stored series. Why the correct answer wins: Sampling keeps the errors while cutting the volume.

### Question 67 — C

Answer: Measure log volume per service before choosing a retention period. Measuring volume is what explains the increase. A cost estimate driven by actual ingest. Local study-map skill 4.2 (Log Optimization and Cost), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 4 (implementing observability practices and troubleshooting): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A retention period that cannot be shortened. Why the correct answer wins: Measuring volume is what explains the increase.
- **B:** Incorrect for this question. A filter that drops matching entries before storage. Why the correct answer wins: Measuring volume is what explains the increase.
- **C:** Correct. A cost estimate driven by actual ingest. In this case: Measuring volume is what explains the increase.
- **D:** Incorrect for this question. A fraction kept for diagnosis at lower cost. Why the correct answer wins: Measuring volume is what explains the increase.

### Question 68 — B

Answer: Filter with the Logging query language on the resource label. The query language filters on severity and label. A precise query over the stored entries. Local study-map skill 4.3 (Logs Explorer and Query Language), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 4 (implementing observability practices and troubleshooting): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A counter derived from matching entries. Why the correct answer wins: The query language filters on severity and label.
- **B:** Correct. A precise query over the stored entries. In this case: The query language filters on severity and label.
- **C:** Incorrect for this question. An interactive view with field filters. Why the correct answer wins: The query language filters on severity and label.
- **D:** Incorrect for this question. A sink suited to cheap long-term retention. Why the correct answer wins: The query language filters on severity and label.

### Question 69 — D

Answer: Route the entries to a BigQuery dataset. A BigQuery sink allows that join. A sink that lands logs in a queryable table. Local study-map skill 4.3 (Logs Explorer and Query Language), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 4 (implementing observability practices and troubleshooting): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A retention period that cannot be shortened. Why the correct answer wins: A BigQuery sink allows that join.
- **B:** Incorrect for this question. A sink suited to cheap long-term retention. Why the correct answer wins: A BigQuery sink allows that join.
- **C:** Incorrect for this question. A sink that streams entries to another consumer. Why the correct answer wins: A BigQuery sink allows that join.
- **D:** Correct. A sink that lands logs in a queryable table. In this case: A BigQuery sink allows that join.

### Question 70 — C, E

Answers: Route the entries to a Cloud Storage bucket; Set the log bucket retention and lock it. A storage sink is cheap, and a locked bucket prevents shortening. A sink suited to cheap long-term retention. A retention period that cannot be shortened. Local study-map skill 4.4 (Log Export and Retention), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 4 (implementing observability practices and troubleshooting): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A cost estimate driven by actual ingest. Why the correct answer wins: A storage sink is cheap, and a locked bucket prevents shortening.
- **B:** Incorrect for this question. A sink that lands logs in a queryable table. Why the correct answer wins: A storage sink is cheap, and a locked bucket prevents shortening.
- **C:** Correct. A sink suited to cheap long-term retention. In this case: A storage sink is cheap, and a locked bucket prevents shortening.
- **D:** Incorrect for this question. A sink that streams entries to another consumer. Why the correct answer wins: A storage sink is cheap, and a locked bucket prevents shortening.
- **E:** Correct. A retention period that cannot be shortened. In this case: A storage sink is cheap, and a locked bucket prevents shortening.

### Question 71 — D

Answer: Route the entries to a Pub/Sub topic. A Pub/Sub sink delivers entries to the consumer. A sink that streams entries to another consumer. Local study-map skill 4.4 (Log Export and Retention), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 4 (implementing observability practices and troubleshooting): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A sink that lands logs in a queryable table. Why the correct answer wins: A Pub/Sub sink delivers entries to the consumer.
- **B:** Incorrect for this question. A sink suited to cheap long-term retention. Why the correct answer wins: A Pub/Sub sink delivers entries to the consumer.
- **C:** Incorrect for this question. A retention period that cannot be shortened. Why the correct answer wins: A Pub/Sub sink delivers entries to the consumer.
- **D:** Correct. A sink that streams entries to another consumer. In this case: A Pub/Sub sink delivers entries to the consumer.

### Question 72 — D

Answer: Redact the email field with a log processor. The processor masks the pattern before storage. A transform that removes the value before storage. Local study-map skill 4.5 (Sensitive Data Redaction), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 4 (implementing observability practices and troubleshooting): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A procedural promise with no enforcement. Why the correct answer wins: The processor masks the pattern before storage.
- **B:** Incorrect for this question. A fraction kept for diagnosis at lower cost. Why the correct answer wins: The processor masks the pattern before storage.
- **C:** Incorrect for this question. A sink suited to cheap long-term retention. Why the correct answer wins: The processor masks the pattern before storage.
- **D:** Correct. A transform that removes the value before storage. In this case: The processor masks the pattern before storage.

### Question 73 — A, D

Answers: Ask Gemini Cloud Assist to summarise the failing entries; Ask Gemini Cloud Assist which span dominates the trace. The log summary explains the entries, and the trace hint names the span. An AI summary over the selected log range. An AI pointer to the expensive span. Local study-map skill 4.6 (Gemini Cloud Assist for Log Analysis), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 4 (implementing observability practices and troubleshooting): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Correct. An AI pointer to the expensive span. In this case: The log summary explains the entries, and the trace hint names the span.
- **B:** Incorrect for this question. A precise query over the stored entries. Why the correct answer wins: The log summary explains the entries, and the trace hint names the span.
- **C:** Incorrect for this question. An interactive view with field filters. Why the correct answer wins: The log summary explains the entries, and the trace hint names the span.
- **D:** Correct. An AI summary over the selected log range. In this case: The log summary explains the entries, and the trace hint names the span.
- **E:** Incorrect for this question. An AI interpretation of the chart. Why the correct answer wins: The log summary explains the entries, and the trace hint names the span.

### Question 74 — C

Answer: Scrape the workload with managed collection for Prometheus. Managed collection scrapes the exporter for you. A metrics store fed by a scrape endpoint. Local study-map skill 4.7 (Metrics Collection), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 4 (implementing observability practices and troubleshooting): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A counter derived from matching entries. Why the correct answer wins: Managed collection scrapes the exporter for you.
- **B:** Incorrect for this question. A measurement written by the application itself. Why the correct answer wins: Managed collection scrapes the exporter for you.
- **C:** Correct. A metrics store fed by a scrape endpoint. In this case: Managed collection scrapes the exporter for you.
- **D:** Incorrect for this question. A vendor-neutral pipeline for traces and metrics. Why the correct answer wins: Managed collection scrapes the exporter for you.

### Question 75 — A

Answer: Emit a custom metric for the business event. The application emits that value as a metric. A measurement written by the application itself. Local study-map skill 4.7 (Metrics Collection), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 4 (implementing observability practices and troubleshooting): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Correct. A measurement written by the application itself. In this case: The application emits that value as a metric.
- **B:** Incorrect for this question. A counter derived from matching entries. Why the correct answer wins: The application emits that value as a metric.
- **C:** Incorrect for this question. A probe that exercises the path from outside. Why the correct answer wins: The application emits that value as a metric.
- **D:** Incorrect for this question. A metrics store fed by a scrape endpoint. Why the correct answer wins: The application emits that value as a metric.

### Question 76 — B

Answer: Create a log-based metric for the error string. A log-based metric counts those entries. A counter derived from matching entries. Local study-map skill 4.8 (Custom and Log-Based Metrics), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 4 (implementing observability practices and troubleshooting): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A metrics store fed by a scrape endpoint. Why the correct answer wins: A log-based metric counts those entries.
- **B:** Correct. A counter derived from matching entries. In this case: A log-based metric counts those entries.
- **C:** Incorrect for this question. A measurement written by the application itself. Why the correct answer wins: A log-based metric counts those entries.
- **D:** Incorrect for this question. A probe that exercises the path from outside. Why the correct answer wins: A log-based metric counts those entries.

### Question 77 — D, E

Answers: Create an uptime check against the login flow; Create a log-based metric for the error string. The uptime check probes the flow, and the log metric counts the string. A probe that exercises the path from outside. A counter derived from matching entries. Local study-map skill 4.9 (Synthetic Monitors), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 4 (implementing observability practices and troubleshooting): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A shared view of the signals that matter. Why the correct answer wins: The uptime check probes the flow, and the log metric counts the string.
- **B:** Incorrect for this question. A metrics store fed by a scrape endpoint. Why the correct answer wins: The uptime check probes the flow, and the log metric counts the string.
- **C:** Incorrect for this question. A measurement written by the application itself. Why the correct answer wins: The uptime check probes the flow, and the log metric counts the string.
- **D:** Correct. A probe that exercises the path from outside. In this case: The uptime check probes the flow, and the log metric counts the string.
- **E:** Correct. A counter derived from matching entries. In this case: The uptime check probes the flow, and the log metric counts the string.

### Question 78 — A

Answer: Build one dashboard and share it with the on-call rotation. One shared dashboard serves every team at once. A shared view of the signals that matter. Local study-map skill 4.10 (Metrics Explorer and Dashboards), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 4 (implementing observability practices and troubleshooting): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Correct. A shared view of the signals that matter. In this case: One shared dashboard serves every team at once.
- **B:** Incorrect for this question. A third-party paging integration. Why the correct answer wins: One shared dashboard serves every team at once.
- **C:** Incorrect for this question. A static threshold on a resource metric. Why the correct answer wins: One shared dashboard serves every team at once.
- **D:** Incorrect for this question. A documented response beside the notification. Why the correct answer wins: One shared dashboard serves every team at once.

### Question 79 — C

Answer: Attach the remediation playbook to the alert. The attached playbook surfaces the steps on the alert. A documented response beside the notification. Local study-map skill 4.10 (Metrics Explorer and Dashboards), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 4 (implementing observability practices and troubleshooting): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A shared view of the signals that matter. Why the correct answer wins: The attached playbook surfaces the steps on the alert.
- **B:** Incorrect for this question. A delivery route for the alert. Why the correct answer wins: The attached playbook surfaces the steps on the alert.
- **C:** Correct. A documented response beside the notification. In this case: The attached playbook surfaces the steps on the alert.
- **D:** Incorrect for this question. A page driven by the objective instead of a raw threshold. Why the correct answer wins: The attached playbook surfaces the steps on the alert.

### Question 80 — C

Answer: Alert when CPU stays above ninety percent for ten minutes. A resource threshold pages without user impact. A static threshold on a resource metric. Local study-map skill 4.11 (Alerting Policies), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 4 (implementing observability practices and troubleshooting): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A third-party paging integration. Why the correct answer wins: A resource threshold pages without user impact.
- **B:** Incorrect for this question. A page driven by the objective instead of a raw threshold. Why the correct answer wins: A resource threshold pages without user impact.
- **C:** Correct. A static threshold on a resource metric. In this case: A resource threshold pages without user impact.
- **D:** Incorrect for this question. A documented response beside the notification. Why the correct answer wins: A resource threshold pages without user impact.

### Question 81 — A

Answer: Create an alerting policy on the SLO burn rate. The burn-rate policy pages on that projection. A page driven by the objective instead of a raw threshold. Local study-map skill 4.11 (Alerting Policies), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 4 (implementing observability practices and troubleshooting): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Correct. A page driven by the objective instead of a raw threshold. In this case: The burn-rate policy pages on that projection.
- **B:** Incorrect for this question. A probe that exercises the path from outside. Why the correct answer wins: The burn-rate policy pages on that projection.
- **C:** Incorrect for this question. A static threshold on a resource metric. Why the correct answer wins: The burn-rate policy pages on that projection.
- **D:** Incorrect for this question. A delivery route for the alert. Why the correct answer wins: The burn-rate policy pages on that projection.

### Question 82 — C

Answer: Send the alert to PagerDuty through a webhook. A webhook delivers the alert to the external paging tool. A third-party paging integration. Local study-map skill 4.12 (Third-Party Alerting Integration), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 4 (implementing observability practices and troubleshooting): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A documented response beside the notification. Why the correct answer wins: A webhook delivers the alert to the external paging tool.
- **B:** Incorrect for this question. A delivery route for the alert. Why the correct answer wins: A webhook delivers the alert to the external paging tool.
- **C:** Correct. A third-party paging integration. In this case: A webhook delivers the alert to the external paging tool.
- **D:** Incorrect for this question. A static threshold on a resource metric. Why the correct answer wins: A webhook delivers the alert to the external paging tool.

### Question 83 — D

Answer: Read the trace waterfall to find the slow span. The waterfall orders the spans by elapsed time. A per-span timing view of one request. Local study-map skill 4.13 (Distributed Tracing with OpenTelemetry), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 4 (implementing observability practices and troubleshooting): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. An AI pointer to the expensive span. Why the correct answer wins: The waterfall orders the spans by elapsed time.
- **B:** Incorrect for this question. A join key between traces and logs. Why the correct answer wins: The waterfall orders the spans by elapsed time.
- **C:** Incorrect for this question. Trace context emitted for each request. Why the correct answer wins: The waterfall orders the spans by elapsed time.
- **D:** Correct. A per-span timing view of one request. In this case: The waterfall orders the spans by elapsed time.

### Question 84 — A

Answer: Put the trace ID in the structured log line. The trace ID in the log provides the link. A join key between traces and logs. Local study-map skill 4.13 (Distributed Tracing with OpenTelemetry), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 4 (implementing observability practices and troubleshooting): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Correct. A join key between traces and logs. In this case: The trace ID in the log provides the link.
- **B:** Incorrect for this question. Trace context emitted for each request. Why the correct answer wins: The trace ID in the log provides the link.
- **C:** Incorrect for this question. No shared identifier between the two signals. Why the correct answer wins: The trace ID in the log provides the link.
- **D:** Incorrect for this question. A per-span timing view of one request. Why the correct answer wins: The trace ID in the log provides the link.

### Question 85 — B

Answer: Compare latency with the saturation metric. Correlating latency with saturation names the cause. A queueing symptom traced to a full resource. Local study-map skill 4.14 (Trace Analysis and Log Correlation), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 4 (implementing observability practices and troubleshooting): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A join key between traces and logs. Why the correct answer wins: Correlating latency with saturation names the cause.
- **B:** Correct. A queueing symptom traced to a full resource. In this case: Correlating latency with saturation names the cause.
- **C:** Incorrect for this question. Trace context emitted for each request. Why the correct answer wins: Correlating latency with saturation names the cause.
- **D:** Incorrect for this question. A per-span timing view of one request. Why the correct answer wins: Correlating latency with saturation names the cause.

### Question 86 — B, C

Answers: Check Cloud NAT port exhaustion for the egress range; Check the quota error in the deployment log. NAT port exhaustion explains the egress failures, and the quota log explains the refusal. A shared egress resource that runs out of ports. The limit that refused the resource. Local study-map skill 4.15 (Infrastructure and Pipeline Troubleshooting), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 4 (implementing observability practices and troubleshooting): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. The rule that blocked the connection. Why the correct answer wins: NAT port exhaustion explains the egress failures, and the quota log explains the refusal.
- **B:** Correct. A shared egress resource that runs out of ports. In this case: NAT port exhaustion explains the egress failures, and the quota log explains the refusal.
- **C:** Correct. The limit that refused the resource. In this case: NAT port exhaustion explains the egress failures, and the quota log explains the refusal.
- **D:** Incorrect for this question. The identity the node uses to fetch the image. Why the correct answer wins: NAT port exhaustion explains the egress failures, and the quota log explains the refusal.
- **E:** Incorrect for this question. A stale name that still points at the old address. Why the correct answer wins: NAT port exhaustion explains the egress failures, and the quota log explains the refusal.

### Question 87 — C

Answer: Compare the readiness probe with the application startup time. The probe may be firing before the app listens. A probe that fails before the app is listening. Local study-map skill 4.16 (Application and Latency Troubleshooting), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 4 (implementing observability practices and troubleshooting): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A shared egress resource that runs out of ports. Why the correct answer wins: The probe may be firing before the app listens.
- **B:** Incorrect for this question. A hotspot found on the request path. Why the correct answer wins: The probe may be firing before the app listens.
- **C:** Correct. A probe that fails before the app is listening. In this case: The probe may be firing before the app listens.
- **D:** Incorrect for this question. A stale name that still points at the old address. Why the correct answer wins: The probe may be firing before the app listens.

### Question 88 — B

Answer: Profile the slow endpoint inside the application. Profiling locates the slow code inside the endpoint. A hotspot found on the request path. Local study-map skill 4.16 (Application and Latency Troubleshooting), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 4 (implementing observability practices and troubleshooting): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A stale name that still points at the old address. Why the correct answer wins: Profiling locates the slow code inside the endpoint.
- **B:** Correct. A hotspot found on the request path. In this case: Profiling locates the slow code inside the endpoint.
- **C:** Incorrect for this question. A probe that fails before the app is listening. Why the correct answer wins: Profiling locates the slow code inside the endpoint.
- **D:** Incorrect for this question. A shared egress resource that runs out of ports. Why the correct answer wins: Profiling locates the slow code inside the endpoint.

### Question 89 — A

Answer: Measure request latency by endpoint in Cloud Monitoring. Per-endpoint latency shows which call changed. An application-level view of response time. Local study-map skill 5.1 (Application Performance Monitoring), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 5 (optimizing performance and cost): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Correct. An application-level view of response time. In this case: Per-endpoint latency shows which call changed.
- **B:** Incorrect for this question. A queryable record of spend by label. Why the correct answer wins: Per-endpoint latency shows which call changed.
- **C:** Incorrect for this question. A goal-oriented view of performance. Why the correct answer wins: Per-endpoint latency shows which call changed.
- **D:** Incorrect for this question. A recommendation aimed at spend. Why the correct answer wins: Per-endpoint latency shows which call changed.

### Question 90 — B

Answer: Track the service objective on a shared dashboard. The objective dashboard shows the goal against reality. A goal-oriented view of performance. Local study-map skill 5.1 (Application Performance Monitoring), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 5 (optimizing performance and cost): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A recommendation aimed at spend. Why the correct answer wins: The objective dashboard shows the goal against reality.
- **B:** Correct. A goal-oriented view of performance. In this case: The objective dashboard shows the goal against reality.
- **C:** Incorrect for this question. A cost estimate driven by actual ingest. Why the correct answer wins: The objective dashboard shows the goal against reality.
- **D:** Incorrect for this question. An application-level view of response time. Why the correct answer wins: The objective dashboard shows the goal against reality.

### Question 91 — A, D

Answers: Review the Active Assist recommendations for the project; Apply the reliability recommender for the missing quota. Active Assist lists the suggestions, and the reliability recommender flags the limit. Suggested changes generated from telemetry. A recommendation aimed at resilience. Local study-map skill 5.2 (Active Assist and Recommenders), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 5 (optimizing performance and cost): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Correct. A recommendation aimed at resilience. In this case: Active Assist lists the suggestions, and the reliability recommender flags the limit.
- **B:** Incorrect for this question. A recommendation aimed at spend. Why the correct answer wins: Active Assist lists the suggestions, and the reliability recommender flags the limit.
- **C:** Incorrect for this question. Discounted capacity that can be reclaimed. Why the correct answer wins: Active Assist lists the suggestions, and the reliability recommender flags the limit.
- **D:** Correct. Suggested changes generated from telemetry. In this case: Active Assist lists the suggestions, and the reliability recommender flags the limit.
- **E:** Incorrect for this question. A queryable record of spend by label. Why the correct answer wins: Active Assist lists the suggestions, and the reliability recommender flags the limit.

### Question 92 — B

Answer: Apply the cost recommender suggestion for the idle disks. The cost recommender points at the idle disks. A recommendation aimed at spend. Local study-map skill 5.2 (Active Assist and Recommenders), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 5 (optimizing performance and cost): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Suggested changes generated from telemetry. Why the correct answer wins: The cost recommender points at the idle disks.
- **B:** Correct. A recommendation aimed at spend. In this case: The cost recommender points at the idle disks.
- **C:** Incorrect for this question. Discounted capacity that can be reclaimed. Why the correct answer wins: The cost recommender points at the idle disks.
- **D:** Incorrect for this question. A recommendation aimed at resilience. Why the correct answer wins: The cost recommender points at the idle disks.

### Question 93 — D

Answer: Exclude the debug stream and keep the error stream. Excluding the debug stream removes the unread volume. A reduction that preserves the useful signal. Local study-map skill 5.3 (Observability Cost Management), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 5 (optimizing performance and cost): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A retention period that cannot be shortened. Why the correct answer wins: Excluding the debug stream removes the unread volume.
- **B:** Incorrect for this question. A label removal that cuts the stored series. Why the correct answer wins: Excluding the debug stream removes the unread volume.
- **C:** Incorrect for this question. A cost estimate driven by actual ingest. Why the correct answer wins: Excluding the debug stream removes the unread volume.
- **D:** Correct. A reduction that preserves the useful signal. In this case: Excluding the debug stream removes the unread volume.

### Question 94 — A

Answer: Drop the high-cardinality user label from the metric. The label multiplies the stored series. A label removal that cuts the stored series. Local study-map skill 5.3 (Observability Cost Management), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 5 (optimizing performance and cost): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Correct. A label removal that cuts the stored series. In this case: The label multiplies the stored series.
- **B:** Incorrect for this question. A reduction that preserves the useful signal. Why the correct answer wins: The label multiplies the stored series.
- **C:** Incorrect for this question. A cheaper egress path with different performance. Why the correct answer wins: The label multiplies the stored series.
- **D:** Incorrect for this question. A cost estimate driven by actual ingest. Why the correct answer wins: The label multiplies the stored series.

### Question 95 — A

Answer: Put the stateless workers on a Spot node pool. Spot nodes cut the cost of restartable consumers. A pool built from reclaimable capacity. Local study-map skill 5.4 (Spot Virtual Machines), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 5 (optimizing performance and cost): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Correct. A pool built from reclaimable capacity. In this case: Spot nodes cut the cost of restartable consumers.
- **B:** Incorrect for this question. A multi-year commitment at a lower unit price. Why the correct answer wins: Spot nodes cut the cost of restartable consumers.
- **C:** Incorrect for this question. Reclaimable capacity under a stateful workload. Why the correct answer wins: Spot nodes cut the cost of restartable consumers.
- **D:** Incorrect for this question. Discounted capacity that can be reclaimed. Why the correct answer wins: Spot nodes cut the cost of restartable consumers.

### Question 96 — D

Answer: Run the batch on Spot VMs. Spot capacity suits interruptible rendering work. Discounted capacity that can be reclaimed. Local study-map skill 5.4 (Spot Virtual Machines), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 5 (optimizing performance and cost): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A pool built from reclaimable capacity. Why the correct answer wins: Spot capacity suits interruptible rendering work.
- **B:** Incorrect for this question. Reclaimable capacity under a stateful workload. Why the correct answer wins: Spot capacity suits interruptible rendering work.
- **C:** Incorrect for this question. A multi-year commitment at a lower unit price. Why the correct answer wins: Spot capacity suits interruptible rendering work.
- **D:** Correct. Discounted capacity that can be reclaimed. In this case: Spot capacity suits interruptible rendering work.

### Question 97 — B, C

Answers: Buy a committed-use discount for the steady baseline; Serve the bulk export over the Standard network tier. A commitment discounts the baseline, and the standard tier lowers transfer cost. A multi-year commitment at a lower unit price. A cheaper egress path with different performance. Local study-map skill 5.5 (Infrastructure Cost Planning), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 5 (optimizing performance and cost): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Discounted capacity that can be reclaimed. Why the correct answer wins: A commitment discounts the baseline, and the standard tier lowers transfer cost.
- **B:** Correct. A multi-year commitment at a lower unit price. In this case: A commitment discounts the baseline, and the standard tier lowers transfer cost.
- **C:** Correct. A cheaper egress path with different performance. In this case: A commitment discounts the baseline, and the standard tier lowers transfer cost.
- **D:** Incorrect for this question. An automatic discount that accrues with monthly use. Why the correct answer wins: A commitment discounts the baseline, and the standard tier lowers transfer cost.
- **E:** Incorrect for this question. A lower-latency path for user-facing traffic. Why the correct answer wins: A commitment discounts the baseline, and the standard tier lowers transfer cost.

### Question 98 — B

Answer: Keep the interactive traffic on the Premium tier. The premium tier keeps the customer path short. A lower-latency path for user-facing traffic. Local study-map skill 5.5 (Infrastructure Cost Planning), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 5 (optimizing performance and cost): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A multi-year commitment at a lower unit price. Why the correct answer wins: The premium tier keeps the customer path short.
- **B:** Correct. A lower-latency path for user-facing traffic. In this case: The premium tier keeps the customer path short.
- **C:** Incorrect for this question. A pool built from reclaimable capacity. Why the correct answer wins: The premium tier keeps the customer path short.
- **D:** Incorrect for this question. A cheaper egress path with different performance. Why the correct answer wins: The premium tier keeps the customer path short.

### Question 99 — B

Answer: Right-size the node pool from the observed requests. Right-sizing follows the observed request pattern. A pool sized against measured demand. Local study-map skill 5.6 (Workload-Level Cost Optimization), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 5 (optimizing performance and cost): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Warm capacity that avoids cold starts. Why the correct answer wins: Right-sizing follows the observed request pattern.
- **B:** Correct. A pool sized against measured demand. In this case: Right-sizing follows the observed request pattern.
- **C:** Incorrect for this question. Scale to zero for a service nobody uses at night. Why the correct answer wins: Right-sizing follows the observed request pattern.
- **D:** Incorrect for this question. A pool built from reclaimable capacity. Why the correct answer wins: Right-sizing follows the observed request pattern.

### Question 100 — C

Answer: Stop the idle non-production instances on a schedule. A scheduled stop removes the idle overnight cost. A calendar action that removes idle spend. Local study-map skill 5.6 (Workload-Level Cost Optimization), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 5 (optimizing performance and cost): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A multi-year commitment at a lower unit price. Why the correct answer wins: A scheduled stop removes the idle overnight cost.
- **B:** Incorrect for this question. Scale to zero for a service nobody uses at night. Why the correct answer wins: A scheduled stop removes the idle overnight cost.
- **C:** Correct. A calendar action that removes idle spend. In this case: A scheduled stop removes the idle overnight cost.
- **D:** Incorrect for this question. A pool sized against measured demand. Why the correct answer wins: A scheduled stop removes the idle overnight cost.
