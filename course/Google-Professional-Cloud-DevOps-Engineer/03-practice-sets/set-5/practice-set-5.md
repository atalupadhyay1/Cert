# Google Cloud Professional Cloud DevOps Engineer — Full-Length Mock Exam 5

Professional Cloud DevOps Engineer · 100 questions · expanded practice bank · passing score not published

Blueprint-weighted mock exam. Item mix: 84 multiple-choice and 16 multiple-select items (the selection count is stated in each multi-select stem). The live exam publishes 50-60 multiple-choice and multiple-select questions and has no case-study component, so this set is larger on purpose and no case-study item is reproduced. The live paper allows two hours for 50-60 items, so this 100-item set is a slower-per-item rehearsal: about 72 seconds per item here against roughly 120-144 seconds live. Use it to build a habit of finishing with time to review. See the README for the exact fidelity boundary.

Original educational content, not actual, recalled, or copied Google exam items.

## Questions

---

## Domain 1 — Bootstrapping and Maintaining a Google Cloud Organization (Hierarchy, Infrastructure as Code, and Pipeline Foundations)

### 1. Finance wants a guardrail that no subsidiary can disable on its own projects. What provides that?

- A. Apply the constraint separately in each project
- B. Apply the constraint at the organization node
- C. Add an IAM deny policy for the sensitive permission
- D. Apply the constraint to the business unit folder

### 2. Support must find an application, its staging project, and its owner in one folder branch. How should the hierarchy be shaped?

- A. Apply the constraint separately in each project
- B. Apply the constraint to the business unit folder
- C. Group projects by environment with applications below
- D. Group projects by application inside each environment folder

### 3. A vendor's managed service must be reached privately, and neither network can be renumbered. What fits?

- A. Publish the service behind a Private Service Connect endpoint
- B. Peer every project VPC with every other project VPC
- C. Create a Shared VPC host project and attach the service projects
- D. Give each project its own VPC and Cloud NAT

### 4. Thirty VPCs each carry their own firewall rules and security cannot review them all. What caused that?

- A. Give each project its own VPC and Cloud NAT
- B. Publish the service behind a Private Service Connect endpoint
- C. Create a Shared VPC host project and attach the service projects
- D. Peer every project VPC with every other project VPC

### 5. One chart must show request errors from five projects that were created last month. What should be configured?

- A. Route the entries to a Pub/Sub topic
- B. Add the projects to one metrics scope
- C. Keep one log bucket inside each project
- D. Route every project log to one aggregated sink

### 6. An engineer must not be able to grant the billing administrator role to anyone, whatever roles they hold. What should be added?

- A. Add an IAM deny policy for the sensitive permission
- B. Grant a custom role limited to the required permissions
- C. Enforce the restriction with an organization policy constraint
- D. Grant a predefined role once at the folder

### 7. New analysts need read-only access to the standard curated datasets. What should be granted?

- A. Enforce the restriction with an organization policy constraint
- B. Add an IAM deny policy for the sensitive permission
- C. Grant a predefined role once at the folder
- D. Grant a custom role limited to the required permissions

### 8. The production pipeline must not be reachable from a staging credential. What should be created?

- A. Create one service account per workload
- B. Create one service account per environment
- C. Download a JSON key file for the service account
- D. Let the workload use the default Compute Engine service account

### 9. A public-sector buyer requires every backup, including disaster copies, inside its own country. What governs that?

- A. Create a Shared VPC host project and attach the service projects
- B. Apply the constraint at the organization node
- C. Replicate the data to a second region
- D. Place the resources in a region that satisfies the residency rule

### 10. The estate must be described once and reused, and any difference between code and reality must be reported. Which two practices apply? Select two.

- A. Define the estate as Terraform modules held in version control
- B. Apply the deployment through Infrastructure Manager
- C. Make the change in the console and note it in the wiki
- D. Package the workload as a Helm chart
- E. Schedule a plan that reports drift

### 11. The deployment must run from a managed service that keeps its own state and audit history. What fits?

- A. Reconcile the resources with Config Connector
- B. Automate the repeated step with a Python script calling the API
- C. Apply the deployment through Infrastructure Manager
- D. Define the estate as Terraform modules held in version control

### 12. An auditor asks which published reference architecture the landing zone came from. What answers that?

- A. Render the manifests through a kpt function pipeline
- B. Define the estate as Terraform modules held in version control
- C. Start from the Cloud Foundation Toolkit blueprints
- D. Schedule a plan that reports drift

### 13. A daily job must delete stale resources and record every removal. What should be written?

- A. Run the documented gcloud commands by hand for each environment
- B. Render the manifests through a kpt function pipeline
- C. Automate the repeated step with a Python script calling the API
- D. Make the change in the console and note it in the wiki

### 14. One release must be traceable from its build through every promotion stage. What fits?

- A. Use Cloud Build for CI and Cloud Deploy for delivery
- B. Bake the machine image with Packer
- C. Run Jenkins on a self-managed VM
- D. Let Argo CD pull the manifests from Git

### 15. A regulator requires builds to stay on hardware the company controls. What fits?

- A. Store the build output in Artifact Registry
- B. Let Argo CD pull the manifests from Git
- C. Run Jenkins on a self-managed VM
- D. Use Cloud Build for CI and Cloud Deploy for delivery

### 16. Every environment must boot from an image that security signed once. What fits?

- A. Render the manifests through a kpt function pipeline
- B. Package the workload as a Helm chart
- C. Define the estate as Terraform modules held in version control
- D. Bake the machine image with Packer

### 17. The base manifests must stay identical, and only the replica count differs per environment. What fits?

- A. Create a short-lived project per change and delete it after review
- B. Bake the environment settings into the image
- C. Keep one shared staging environment for every team
- D. Keep one base with a Kustomize overlay per environment

### 18. Sixty clusters must share one policy and one upgrade cadence. Which two configurations apply? Select two.

- A. Put the cluster on a release channel with a maintenance window
- B. Upgrade each node pool by hand whenever an operator is free
- C. Stand up a second cluster and shift traffic after verification
- D. Create a short-lived project per change and delete it after review
- E. Register the clusters in a fleet

### 19. Every laptop must start from the approved toolchain, and engineers want inline help while editing. Which two fit? Select two.

- A. Build a custom image that carries the approved toolchain
- B. Ask Gemini Cloud Assist to explain the resource state
- C. Let each developer install the tools locally
- D. Rely on Cloud Shell for every developer
- E. Use Gemini Code Assist for the suggested change

### 20. A contractor's environment differs from the team's because they installed their own tooling. What caused that?

- A. Let each developer install the tools locally
- B. Give developers Cloud Workstations built from a custom image
- C. Rely on Cloud Shell for every developer
- D. Build a custom image that carries the approved toolchain

---

## Domain 2 — Building and Implementing CI/CD Pipelines (Delivery Pipelines and Software Supply Chain)

### 21. A pull request that edits a policy file must be checked by the policy test. What should be configured?

- A. Create a Cloud Build trigger on the release branch
- B. Create a trigger that runs the tests on every pull request
- C. Have an engineer build locally and upload the result
- D. Trigger the pipeline only on a signed tag

### 22. Finance must be able to reproduce release 4.2 exactly from the event that created it. What should be configured?

- A. Add a Cloud Deploy approval gate before production
- B. Create a trigger that runs the tests on every pull request
- C. Create a Cloud Build trigger on the release branch
- D. Trigger the pipeline only on a signed tag

### 23. A release cannot be rebuilt because the machine that produced it no longer exists. What caused that?

- A. Have an engineer build locally and upload the result
- B. Create a Cloud Build trigger on the release branch
- C. Trigger the pipeline only on a signed tag
- D. Create a trigger that runs the tests on every pull request

### 24. Images must be retained in the same region as the clusters that pull them. What fits?

- A. Store the build output in Artifact Registry
- B. Push the image to Container Registry
- C. Tag each artifact with the commit SHA and forbid overwrite
- D. Reuse the latest tag for every build

### 25. Two deployments from the same reference behaved differently. What explains that?

- A. Reuse the latest tag for every build
- B. Tag each artifact with the commit SHA and forbid overwrite
- C. Inspect the build provenance attestation
- D. Store the build output in Artifact Registry

### 26. Releases must reach both an on-premises cluster and a cluster in the pipeline project. Which two target types apply? Select two.

- A. Add a Cloud Deploy approval gate before production
- B. Define the attached cluster as the delivery target
- C. Read Cloud Audit Logs for the release history
- D. Use a GKE cluster in the pipeline project as the target
- E. Deliver to a Cloud Run service revision

### 27. A revision-based service must receive its traffic split from the release tool. What fits?

- A. Define the attached cluster as the delivery target
- B. Deliver to a Cloud Run service revision
- C. Read Cloud Audit Logs for the release history
- D. Use a GKE cluster in the pipeline project as the target

### 28. Production receives changes straight from main with no review, and an outage followed. What caused that?

- A. Promote automatically to every target in the chain
- B. Have an engineer build locally and upload the result
- C. Read Cloud Audit Logs for the release history
- D. Add a Cloud Deploy approval gate before production

### 29. An auditor needs the release history, and a customer needs the integrity level of the build. Which two sources apply? Select two.

- A. Add a Cloud Deploy approval gate before production
- B. Tag each artifact with the commit SHA and forbid overwrite
- C. Inspect the build provenance attestation
- D. Describe the build with its supply chain level and signed provenance
- E. Read Cloud Audit Logs for the release history

### 30. The team must prove the artifact came from the reviewed commit rather than a laptop. What provides that?

- A. Inspect the build provenance attestation
- B. Tag each artifact with the commit SHA and forbid overwrite
- C. Describe the build with its supply chain level and signed provenance
- D. Read Cloud Audit Logs for the release history

### 31. Two percent of traffic must prove the change before the rest follows. What fits?

- A. Stop the old version and then start the new one
- B. Replace the instances in batches
- C. Send ten percent of traffic to the new revision and watch the SLI
- D. Run the new version alongside and switch traffic at once

### 32. Both versions must run at once while their weights shift hour by hour. What fits?

- A. Run the new version alongside and switch traffic at once
- B. Stop the old version and then start the new one
- C. Split traffic with a Cloud Service Mesh route
- D. Send ten percent of traffic to the new revision and watch the SLI

### 33. The new pricing engine must ship inside the build and stay off for most accounts. What fits?

- A. Send ten percent of traffic to the new revision and watch the SLI
- B. Run the new version alongside and switch traffic at once
- C. Put the behaviour behind a feature flag
- D. Replace the instances in batches

### 34. The rollout gate watches CPU on a service that stays fast at full saturation, so a bad release is never stopped. What is the flaw?

- A. Gate the rollout on the error-rate SLI
- B. Create an uptime check against the login flow
- C. Add a Cloud Deploy approval gate before production
- D. Gate the rollout on average CPU alone

### 35. A retried step must not create a second bucket. What should the step be?

- A. Patch production by hand and reconcile later
- B. Make the failed step idempotent and re-run it
- C. Roll the release back to the previous one
- D. Start from the failed step log in Cloud Build

### 36. A step times out and the operator needs the command that ran. What supplies it?

- A. Make the failed step idempotent and re-run it
- B. Read Cloud Audit Logs for the release history
- C. Start from the failed step log in Cloud Build
- D. Roll the release back to the previous one

### 37. A customer contract requires the encryption key to live in the company's own key service. What fits?

- A. Issue and rotate the certificate with Certificate Manager
- B. Encrypt the payload with a Cloud KMS key
- C. Commit the credential to the private repository
- D. Store the credential in Secret Manager with versions

### 38. A leaked token must be revoked without redeploying anything. What fits?

- A. Store the credential in Secret Manager with versions
- B. Keep the non-secret configuration in Parameter Manager
- C. Encrypt the payload with a Cloud KMS key
- D. Commit the credential to the private repository

### 39. The on-call engineer must see the current limits without reading the image. What fits?

- A. Commit the credential to the private repository
- B. Keep the non-secret configuration in Parameter Manager
- C. Bake the environment settings into the image
- D. Store the credential in Secret Manager with versions

### 40. Two partners hold the credential because it lives in the shared repository. What caused that?

- A. Store the credential in Secret Manager with versions
- B. Mount the secret at runtime from Secret Manager
- C. Commit the credential to the private repository
- D. Keep the non-secret configuration in Parameter Manager

### 41. One pipeline needs a credential while building to reach a private package index, and the running service needs a database password. Which two injection points apply? Select two.

- A. Commit the credential to the private repository
- B. Mount the secret at runtime from Secret Manager
- C. Keep the non-secret configuration in Parameter Manager
- D. Pass the secret as a build argument
- E. Inject the secret at build time into the image layer

### 42. A registry must keep publishing fresh findings for images built months ago, and a severe new finding must stop the next promotion. Which two capabilities deliver that? Select two.

- A. Fail the pipeline on a critical vulnerability finding
- B. Enable Artifact Analysis scanning on the repository
- C. Bind deploy permissions only inside the production project
- D. Enforce Binary Authorization attestations before deploy
- E. Keep the scan report for the monthly review

### 43. The cluster must refuse any image that lacks an attestation from the approved builder. What fits?

- A. Fail the pipeline on a critical vulnerability finding
- B. Enforce Binary Authorization attestations before deploy
- C. Enable Artifact Analysis scanning on the repository
- D. Bind deploy permissions only inside the production project

### 44. A leaked build credential allowed a release into production from the staging job. What caused that?

- A. Use one identity with deploy rights in every environment
- B. Download a JSON key file for the service account
- C. Bind deploy permissions only inside the production project
- D. Run the pipeline as the default editor service account

### 45. The deploy identity authenticates with one key file that every environment copies to its agent. What is wrong?

- A. Use one identity with deploy rights in every environment
- B. Bind deploy permissions only inside the production project
- C. Run the pipeline as the default editor service account
- D. Download a JSON key file for the service account

---

## Domain 3 — Applying Site Reliability Engineering Practices (Reliability Engineering in Practice)

### 46. Operations and product agree on 99.9 percent internally while the contract says 99.5. What is that arrangement?

- A. Publish a contractual promise with a remedy
- B. Set an internal target on that indicator
- C. Alert on a fast error-budget burn rate
- D. Track the ratio of good requests to total requests

### 47. The team must decide what counts as a successful checkout. What is it defining?

- A. Set an internal target on that indicator
- B. Assume five nines for every service
- C. Publish a contractual promise with a remedy
- D. Track the ratio of good requests to total requests

### 48. The customer's legal team wants the remedy written into the agreement. What does that create?

- A. Choose three nines and spend the difference on features
- B. Publish a contractual promise with a remedy
- C. Set an internal target on that indicator
- D. Track the ratio of good requests to total requests

### 49. When the allowance is spent the team stops launching, and it chose a target it can afford. Which two practices apply? Select two.

- A. Choose three nines and spend the difference on features
- B. Stop feature releases when the error budget is spent
- C. Publish a contractual promise with a remedy
- D. Alert on a fast error-budget burn rate
- E. Assume five nines for every service

### 50. A page fires because at the current rate the allowance ends on Thursday. What produced it?

- A. Publish a contractual promise with a remedy
- B. Alert when CPU stays above ninety percent for ten minutes
- C. Alert on a fast error-budget burn rate
- D. Stop feature releases when the error budget is spent

### 51. A platform template applies 99.999 to a nightly batch job. What is the flaw?

- A. Choose three nines and spend the difference on features
- B. Publish a contractual promise with a remedy
- C. Assume five nines for every service
- D. Request a quota increase and reserve capacity before the launch

### 52. A review decides the fourth nine would delay two features for a year. What follows?

- A. Choose three nines and spend the difference on features
- B. Assume five nines for every service
- C. Register the service in the service catalog
- D. Publish a contractual promise with a remedy

### 53. A legacy endpoint must stop answering on 31 March and its DNS must be withdrawn first. What should be planned?

- A. Announce the retirement date and withdraw traffic gradually
- B. Register the service in the service catalog
- C. Leave the unused service running for now
- D. Drain connections before removing the instance

### 54. A new on-call rotation cannot find the escalation path for a dependency. What should exist?

- A. Request a quota increase and reserve capacity before the launch
- B. Register the service in the service catalog
- C. Announce the retirement date and withdraw traffic gradually
- D. Leave the unused service running for now

### 55. A university enrolment week needs four times the usual quota in one region. What should be arranged?

- A. Schedule the batch with Dynamic Workload Scheduler
- B. Assume the default quota will absorb the launch
- C. Request a quota increase and reserve capacity before the launch
- D. Add capacity on a fixed calendar schedule

### 56. Capacity is doubled every Friday for a workload that peaks on Tuesday. What is the flaw?

- A. Request a quota increase and reserve capacity before the launch
- B. Schedule the batch with Dynamic Workload Scheduler
- C. Put the instance group behind an autoscaler on CPU
- D. Add capacity on a fixed calendar schedule

### 57. Workers must follow the backlog, and the legacy instance group must follow CPU. Which two autoscaling signals apply? Select two.

- A. Set Cloud Run concurrency so replicas follow load
- B. Scale on queue depth with a horizontal pod autoscaler
- C. Add capacity on a fixed calendar schedule
- D. Schedule the batch with Dynamic Workload Scheduler
- E. Put the instance group behind an autoscaler on CPU

### 58. A revision must start another instance once eighty requests share one. What setting decides that?

- A. Add capacity on a fixed calendar schedule
- B. Set Cloud Run concurrency so replicas follow load
- C. Scale on queue depth with a horizontal pod autoscaler
- D. Put the instance group behind an autoscaler on CPU

### 59. In-flight requests must finish before a node leaves, and a regional move must be made at the name. Which two controls apply? Select two.

- A. Drain connections before removing the instance
- B. Use a load balancer failover backend
- C. Add capacity in a second region
- D. Request a quota increase and reserve capacity before the launch
- E. Shift traffic with a DNS routing policy

### 60. A backend that fails its health check must stop receiving traffic within seconds. What fits?

- A. Add capacity in a second region
- B. Shift traffic with a DNS routing policy
- C. Drain connections before removing the instance
- D. Use a load balancer failover backend

### 61. A concert sale doubles demand for forty minutes and the region cannot grow fast enough. What should be done?

- A. Request a quota increase and reserve capacity before the launch
- B. Drain connections before removing the instance
- C. Use a load balancer failover backend
- D. Add capacity in a second region

### 62. A bad build reached ten percent of users and the previous build is healthy. What is the fastest safe action?

- A. Patch production by hand and reconcile later
- B. Reverse the schema change with a tested down migration
- C. Wait for the error rate to settle on its own
- D. Redeploy the previous image to the affected service

### 63. On-call waits for the error rate to fall by itself before taking any action. What is the consequence?

- A. Redeploy the previous image to the affected service
- B. Wait for the error rate to settle on its own
- C. Reverse the schema change with a tested down migration
- D. Patch production by hand and reconcile later

---

## Domain 4 — Implementing Observability Practices and Troubleshooting (Telemetry, Alerting, and Diagnosis)

### 64. Network teams must see denied connections, and service owners must see request rates between services. Which two sources apply? Select two.

- A. Read the Cloud Service Mesh telemetry
- B. Run an OpenTelemetry Collector in the cluster
- C. Turn on VPC Flow Logs for the subnet
- D. Install the Ops Agent on the instances
- E. Enable Data Access audit logs for the service

### 65. A VM must report memory pressure that no current metric exposes. What fits?

- A. Read the Cloud Service Mesh telemetry
- B. Enable Data Access audit logs for the service
- C. Install the Ops Agent on the instances
- D. Turn on VPC Flow Logs for the subnet

### 66. A team must size a log bucket before the finance review. What should be done first?

- A. Measure log volume per service before choosing a retention period
- B. Set the log bucket retention and lock it
- C. Sample the high-volume debug entries
- D. Add an exclusion for the health-check entries

### 67. Every probe writes two entries and six probes run each minute. What should be added?

- A. Route the entries to a Cloud Storage bucket
- B. Add an exclusion for the health-check entries
- C. Sample the high-volume debug entries
- D. Drop the high-cardinality user label from the metric

### 68. A label identifies the tenant and only one tenant is failing. What should be used?

- A. Route the entries to a BigQuery dataset
- B. Open the Logs Explorer and pivot from the error entry
- C. Filter with the Logging query language on the resource label
- D. Create a log-based metric for the error string

### 69. An engineer wants every entry written by the same request identifier. What fits?

- A. Create an uptime check against the login flow
- B. Create a log-based metric for the error string
- C. Open the Logs Explorer and pivot from the error entry
- D. Filter with the Logging query language on the resource label

### 70. A quarterly report joins entries with subscription data. What should the sink target?

- A. Set the log bucket retention and lock it
- B. Route the entries to a Pub/Sub topic
- C. Route the entries to a Cloud Storage bucket
- D. Route the entries to a BigQuery dataset

### 71. An auditor must be shown that the retention period cannot be shortened. What fits?

- A. Route the entries to a Cloud Storage bucket
- B. Route the entries to a BigQuery dataset
- C. Measure log volume per service before choosing a retention period
- D. Set the log bucket retention and lock it

### 72. A date of birth appears in entries that support pastes into tickets. What should be configured?

- A. Route the entries to a Cloud Storage bucket
- B. Ask analysts not to read the sensitive field
- C. Add an exclusion for the health-check entries
- D. Redact the email field with a log processor

### 73. An engineer wants the failing entries and a metric spike both explained in words. Which two capabilities apply? Select two.

- A. Ask Gemini Cloud Assist to summarise the failing entries
- B. Ask Gemini Cloud Assist to explain the metric spike
- C. Filter with the Logging query language on the resource label
- D. Create a log-based metric for the error string
- E. Ask Gemini Cloud Assist which span dominates the trace

### 74. The operations team refuses to maintain a scrape server, yet the exporter metrics must be stored. What fits?

- A. Scrape the workload with managed collection for Prometheus
- B. Emit a custom metric for the business event
- C. Create a log-based metric for the error string
- D. Create an uptime check against the login flow

### 75. The service must report its own queue wait time as a measurement. What should it do?

- A. Create an uptime check against the login flow
- B. Emit a custom metric for the business event
- C. Scrape the workload with managed collection for Prometheus
- D. Create a log-based metric for the error string

### 76. A warning that already appears in logs must page somebody tonight. What fits?

- A. Create a log-based metric for the error string
- B. Scrape the workload with managed collection for Prometheus
- C. Create an uptime check against the login flow
- D. Emit a custom metric for the business event

### 77. A partner endpoint must be probed from outside every minute. What fits?

- A. Scrape the workload with managed collection for Prometheus
- B. Emit a custom metric for the business event
- C. Create an uptime check against the login flow
- D. Create a log-based metric for the error string

### 78. Every responder must see the same signals, and the first step must be visible when an alert fires. Which two should be configured? Select two.

- A. Alert when CPU stays above ninety percent for ten minutes
- B. Add an email notification channel for the on-call group
- C. Attach the remediation playbook to the alert
- D. Build one dashboard and share it with the on-call rotation
- E. Send the alert to PagerDuty through a webhook

### 79. The paging tool must be notified before any human reads email. What fits?

- A. Send the alert to PagerDuty through a webhook
- B. Create an alerting policy on the SLO burn rate
- C. Attach the remediation playbook to the alert
- D. Add an email notification channel for the on-call group

### 80. A nightly page fires for a batch node at ninety percent CPU and nobody acts on it. What is the flaw?

- A. Create an alerting policy on the SLO burn rate
- B. Attach the remediation playbook to the alert
- C. Send the alert to PagerDuty through a webhook
- D. Alert when CPU stays above ninety percent for ten minutes

### 81. The audit team wants every alert archived in a shared mailbox. What fits?

- A. Send the alert to PagerDuty through a webhook
- B. Attach the remediation playbook to the alert
- C. Add an email notification channel for the on-call group
- D. Create an alerting policy on the SLO burn rate

### 82. A vendor tool must receive the alert payload over HTTPS. What fits?

- A. Attach the remediation playbook to the alert
- B. Send the alert to PagerDuty through a webhook
- C. Alert when CPU stays above ninety percent for ten minutes
- D. Add an email notification channel for the on-call group

### 83. Each database call must report its own duration. What fits?

- A. Instrument the service with OpenTelemetry spans
- B. Put the trace ID in the structured log line
- C. Read the trace waterfall to find the slow span
- D. Ask Gemini Cloud Assist which span dominates the trace

### 84. An alert must link to the trace that produced it. What provides that link?

- A. Read the trace waterfall to find the slow span
- B. Instrument the service with OpenTelemetry spans
- C. Log a timestamp and correlate by eye later
- D. Put the trace ID in the structured log line

### 85. An engineer wants the order and duration of the six spans in one request. What fits?

- A. Put the trace ID in the structured log line
- B. Instrument the service with OpenTelemetry spans
- C. Ask Gemini Cloud Assist which span dominates the trace
- D. Read the trace waterfall to find the slow span

### 86. Every new pod in one namespace fails with a repository error. What should be checked?

- A. Read the firewall rule that hit the denied flow
- B. Inspect the image pull credential and repository permission
- C. Check the quota error in the deployment log
- D. Check Cloud NAT port exhaustion for the egress range

### 87. One endpoint is slow while the host is idle, and its latency tracks a full connection pool. Which two analyses apply? Select two.

- A. Check the DNS record and its remaining TTL
- B. Check Cloud NAT port exhaustion for the egress range
- C. Profile the slow endpoint inside the application
- D. Compare latency with the saturation metric
- E. Compare the readiness probe with the application startup time

### 88. A pod is killed during startup although the health endpoint answers on port 8080. What should be checked?

- A. Compare the readiness probe with the application startup time
- B. Check Cloud NAT port exhaustion for the egress range
- C. Check the DNS record and its remaining TTL
- D. Profile the slow endpoint inside the application

---

## Domain 5 — Optimizing Performance and Cost (FinOps and Performance Tuning)

### 89. A team must rank endpoints by the slowest p95 this week. What should be used?

- A. Apply the cost recommender suggestion for the idle disks
- B. Measure request latency by endpoint in Cloud Monitoring
- C. Export billing data to BigQuery for the chargeback report
- D. Track the service objective on a shared dashboard

### 90. The reliability review needs one page per service with the goal and the actual. What fits?

- A. Track the service objective on a shared dashboard
- B. Measure log volume per service before choosing a retention period
- C. Measure request latency by endpoint in Cloud Monitoring
- D. Apply the cost recommender suggestion for the idle disks

### 91. A new owner inherits a project and wants the outstanding suggestions. What should be used?

- A. Export billing data to BigQuery for the chargeback report
- B. Apply the cost recommender suggestion for the idle disks
- C. Review the Active Assist recommendations for the project
- D. Apply the reliability recommender for the missing quota

### 92. A service fails at the top of every hour and one suggestion concerns headroom. Which recommendation applies?

- A. Review the Active Assist recommendations for the project
- B. Apply the cost recommender suggestion for the idle disks
- C. Apply the reliability recommender for the missing quota
- D. Run the batch on Spot VMs

### 93. Verbose debug entries and an over-labelled metric both inflate the observability bill. Which two actions apply? Select two.

- A. Set the log bucket retention and lock it
- B. Serve the bulk export over the Standard network tier
- C. Drop the high-cardinality user label from the metric
- D. Measure log volume per service before choosing a retention period
- E. Exclude the debug stream and keep the error stream

### 94. Finance asks for the projected cost of the proposed retention change. What should be done first?

- A. Exclude the debug stream and keep the error stream
- B. Set the log bucket retention and lock it
- C. Drop the high-cardinality user label from the metric
- D. Measure log volume per service before choosing a retention period

### 95. A media transcoder is idempotent and can restart mid-job without harm. What fits?

- A. Buy a committed-use discount for the steady baseline
- B. Put the stateless workers on a Spot node pool
- C. Move the primary database onto Spot capacity
- D. Run the batch on Spot VMs

### 96. A stateless API pool is the largest compute line and tolerates restarts. What fits?

- A. Buy a committed-use discount for the steady baseline
- B. Put the stateless workers on a Spot node pool
- C. Run the batch on Spot VMs
- D. Move the primary database onto Spot capacity

### 97. A predictable baseline should be discounted by contract, and customer traffic needs the fastest path. Which two choices apply? Select two.

- A. Buy a committed-use discount for the steady baseline
- B. Serve the bulk export over the Standard network tier
- C. Run the batch on Spot VMs
- D. Keep the interactive traffic on the Premium tier
- E. Rely on sustained-use discounts for the steady baseline

### 98. Bulk replication between regions may be slower if it is cheaper. What fits?

- A. Put the stateless workers on a Spot node pool
- B. Buy a committed-use discount for the steady baseline
- C. Serve the bulk export over the Standard network tier
- D. Keep the interactive traffic on the Premium tier

### 99. Pods request a quarter of what their node pool reserves. What should be done?

- A. Set a minimum instance count for the latency-critical service
- B. Right-size the node pool from the observed requests
- C. Keep the minimum instance count at zero for the internal tool
- D. Put the stateless workers on a Spot node pool

### 100. A latency-critical service must never cold-start after a quiet period. What fits?

- A. Keep the minimum instance count at zero for the internal tool
- B. Right-size the node pool from the observed requests
- C. Stop the idle non-production instances on a schedule
- D. Set a minimum instance count for the latency-critical service

---

## Answer key and explanations

### Question 1 — B

Answer: Apply the constraint at the organization node. The organization node sits above every subsidiary project. An organization-level constraint that every folder and project inherits. Local study-map skill 1.1 (Resource Hierarchy and Project Organization), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 1 (bootstrapping and maintaining a Google Cloud organization): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A constraint set per project with no inheritance. Why the correct answer wins: The organization node sits above every subsidiary project.
- **B:** Correct. An organization-level constraint that every folder and project inherits. In this case: The organization node sits above every subsidiary project.
- **C:** Incorrect for this question. An explicit denial that overrides any allow. Why the correct answer wins: The organization node sits above every subsidiary project.
- **D:** Incorrect for this question. A constraint attached to one folder and inherited by its projects. Why the correct answer wins: The organization node sits above every subsidiary project.

### Question 2 — D

Answer: Group projects by application inside each environment folder. Application folders keep a service's projects and owners together. An application-centric layout that keeps one service and its owners together. Local study-map skill 1.1 (Resource Hierarchy and Project Organization), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 1 (bootstrapping and maintaining a Google Cloud organization): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A constraint set per project with no inheritance. Why the correct answer wins: Application folders keep a service's projects and owners together.
- **B:** Incorrect for this question. A constraint attached to one folder and inherited by its projects. Why the correct answer wins: Application folders keep a service's projects and owners together.
- **C:** Incorrect for this question. An environment-centric layout that separates production from staging first. Why the correct answer wins: Application folders keep a service's projects and owners together.
- **D:** Correct. An application-centric layout that keeps one service and its owners together. In this case: Application folders keep a service's projects and owners together.

### Question 3 — A

Answer: Publish the service behind a Private Service Connect endpoint. The published endpoint avoids renumbering either network. A private endpoint that consumes a published service. Local study-map skill 1.2 (Shared Networking for Multi-Project Estates), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 1 (bootstrapping and maintaining a Google Cloud organization): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Correct. A private endpoint that consumes a published service. In this case: The published endpoint avoids renumbering either network.
- **B:** Incorrect for this question. A mesh of peering links that grows with each new project. Why the correct answer wins: The published endpoint avoids renumbering either network.
- **C:** Incorrect for this question. A central network project that lends subnets to other projects. Why the correct answer wins: The published endpoint avoids renumbering either network.
- **D:** Incorrect for this question. Duplicate networks with a separately managed egress path. Why the correct answer wins: The published endpoint avoids renumbering either network.

### Question 4 — A

Answer: Give each project its own VPC and Cloud NAT. Per-project networks multiply the rules under review. Duplicate networks with a separately managed egress path. Local study-map skill 1.2 (Shared Networking for Multi-Project Estates), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 1 (bootstrapping and maintaining a Google Cloud organization): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Correct. Duplicate networks with a separately managed egress path. In this case: Per-project networks multiply the rules under review.
- **B:** Incorrect for this question. A private endpoint that consumes a published service. Why the correct answer wins: Per-project networks multiply the rules under review.
- **C:** Incorrect for this question. A central network project that lends subnets to other projects. Why the correct answer wins: Per-project networks multiply the rules under review.
- **D:** Incorrect for this question. A mesh of peering links that grows with each new project. Why the correct answer wins: Per-project networks multiply the rules under review.

### Question 5 — B

Answer: Add the projects to one metrics scope. Adding the projects to the metrics scope charts them together. An observability scope that spans several projects. Local study-map skill 1.3 (Multi-Project Monitoring and Logging), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 1 (bootstrapping and maintaining a Google Cloud organization): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A sink that streams entries to another consumer. Why the correct answer wins: Adding the projects to the metrics scope charts them together.
- **B:** Correct. An observability scope that spans several projects. In this case: Adding the projects to the metrics scope charts them together.
- **C:** Incorrect for this question. Log storage scoped to the project that produced the entries. Why the correct answer wins: Adding the projects to the metrics scope charts them together.
- **D:** Incorrect for this question. A single destination that collects entries from many projects. Why the correct answer wins: Adding the projects to the metrics scope charts them together.

### Question 6 — A

Answer: Add an IAM deny policy for the sensitive permission. The deny policy stops the grant even for owners. An explicit denial that overrides any allow. Local study-map skill 1.4 (IAM Roles and Organization Policies), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 1 (bootstrapping and maintaining a Google Cloud organization): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Correct. An explicit denial that overrides any allow. In this case: The deny policy stops the grant even for owners.
- **B:** Incorrect for this question. A role defined from an explicit permission list. Why the correct answer wins: The deny policy stops the grant even for owners.
- **C:** Incorrect for this question. A guardrail that holds regardless of the IAM grants. Why the correct answer wins: The deny policy stops the grant even for owners.
- **D:** Incorrect for this question. A Google-managed role bound at folder level. Why the correct answer wins: The deny policy stops the grant even for owners.

### Question 7 — C

Answer: Grant a predefined role once at the folder. A predefined reader role grants exactly that access. A Google-managed role bound at folder level. Local study-map skill 1.4 (IAM Roles and Organization Policies), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 1 (bootstrapping and maintaining a Google Cloud organization): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A guardrail that holds regardless of the IAM grants. Why the correct answer wins: A predefined reader role grants exactly that access.
- **B:** Incorrect for this question. An explicit denial that overrides any allow. Why the correct answer wins: A predefined reader role grants exactly that access.
- **C:** Correct. A Google-managed role bound at folder level. In this case: A predefined reader role grants exactly that access.
- **D:** Incorrect for this question. A role defined from an explicit permission list. Why the correct answer wins: A predefined reader role grants exactly that access.

### Question 8 — B

Answer: Create one service account per environment. Separate identities per environment block that path. Separate identities so a staging credential cannot act in production. Local study-map skill 1.5 (Service Account Management), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 1 (bootstrapping and maintaining a Google Cloud organization): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A dedicated identity for each deployed workload. Why the correct answer wins: Separate identities per environment block that path.
- **B:** Correct. Separate identities so a staging credential cannot act in production. In this case: Separate identities per environment block that path.
- **C:** Incorrect for this question. A long-lived credential stored outside the platform. Why the correct answer wins: Separate identities per environment block that path.
- **D:** Incorrect for this question. The account created automatically with broad project access. Why the correct answer wins: Separate identities per environment block that path.

### Question 9 — D

Answer: Place the resources in a region that satisfies the residency rule. Residency applies to the copies as well as the primary. A location choice that keeps data inside the required boundary. Local study-map skill 1.6 (Data Residency in the Hierarchy), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 1 (bootstrapping and maintaining a Google Cloud organization): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A central network project that lends subnets to other projects. Why the correct answer wins: Residency applies to the copies as well as the primary.
- **B:** Incorrect for this question. An organization-level constraint that every folder and project inherits. Why the correct answer wins: Residency applies to the copies as well as the primary.
- **C:** Incorrect for this question. A copy held elsewhere for recovery rather than residency. Why the correct answer wins: Residency applies to the copies as well as the primary.
- **D:** Correct. A location choice that keeps data inside the required boundary. In this case: Residency applies to the copies as well as the primary.

### Question 10 — A, E

Answers: Define the estate as Terraform modules held in version control; Schedule a plan that reports drift. The module describes the estate, and the plan job reports the drift. Declarative code that is reviewed before it is applied. A recurring comparison of declared and actual state. Local study-map skill 1.7 (Infrastructure-as-Code Tool Selection), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 1 (bootstrapping and maintaining a Google Cloud organization): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Correct. Declarative code that is reviewed before it is applied. In this case: The module describes the estate, and the plan job reports the drift.
- **B:** Incorrect for this question. A managed service that runs Terraform deployments. Why the correct answer wins: The module describes the estate, and the plan job reports the drift.
- **C:** Incorrect for this question. An unmanaged change with no enforceable record. Why the correct answer wins: The module describes the estate, and the plan job reports the drift.
- **D:** Incorrect for this question. A templated bundle of Kubernetes resources. Why the correct answer wins: The module describes the estate, and the plan job reports the drift.
- **E:** Correct. A recurring comparison of declared and actual state. In this case: The module describes the estate, and the plan job reports the drift.

### Question 11 — C

Answer: Apply the deployment through Infrastructure Manager. Infrastructure Manager keeps the state and the history. A managed service that runs Terraform deployments. Local study-map skill 1.7 (Infrastructure-as-Code Tool Selection), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 1 (bootstrapping and maintaining a Google Cloud organization): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A controller that keeps Kubernetes manifests and cloud resources aligned. Why the correct answer wins: Infrastructure Manager keeps the state and the history.
- **B:** Incorrect for this question. Idempotent automation through the client library. Why the correct answer wins: Infrastructure Manager keeps the state and the history.
- **C:** Correct. A managed service that runs Terraform deployments. In this case: Infrastructure Manager keeps the state and the history.
- **D:** Incorrect for this question. Declarative code that is reviewed before it is applied. Why the correct answer wins: Infrastructure Manager keeps the state and the history.

### Question 12 — C

Answer: Start from the Cloud Foundation Toolkit blueprints. The toolkit's blueprints are that published reference. Google-maintained Terraform templates for common foundations. Local study-map skill 1.8 (Blueprints and Controlled Infrastructure Change), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 1 (bootstrapping and maintaining a Google Cloud organization): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A transformation pipeline that keeps the source declarative. Why the correct answer wins: The toolkit's blueprints are that published reference.
- **B:** Incorrect for this question. Declarative code that is reviewed before it is applied. Why the correct answer wins: The toolkit's blueprints are that published reference.
- **C:** Correct. Google-maintained Terraform templates for common foundations. In this case: The toolkit's blueprints are that published reference.
- **D:** Incorrect for this question. A recurring comparison of declared and actual state. Why the correct answer wins: The toolkit's blueprints are that published reference.

### Question 13 — C

Answer: Automate the repeated step with a Python script calling the API. The script deletes and records each removal. Idempotent automation through the client library. Local study-map skill 1.9 (Automation with Scripting and APIs), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 1 (bootstrapping and maintaining a Google Cloud organization): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A manual sequence repeated on every occasion. Why the correct answer wins: The script deletes and records each removal.
- **B:** Incorrect for this question. A transformation pipeline that keeps the source declarative. Why the correct answer wins: The script deletes and records each removal.
- **C:** Correct. Idempotent automation through the client library. In this case: The script deletes and records each removal.
- **D:** Incorrect for this question. An unmanaged change with no enforceable record. Why the correct answer wins: The script deletes and records each removal.

### Question 14 — A

Answer: Use Cloud Build for CI and Cloud Deploy for delivery. The managed pair keeps one release record across stages. A managed pair that separates building from releasing. Local study-map skill 1.10 (CI/CD Architecture Stack Design), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 1 (bootstrapping and maintaining a Google Cloud organization): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Correct. A managed pair that separates building from releasing. In this case: The managed pair keeps one release record across stages.
- **B:** Incorrect for this question. A reproducible image built before deployment. Why the correct answer wins: The managed pair keeps one release record across stages.
- **C:** Incorrect for this question. A self-operated CI server whose patching is your problem. Why the correct answer wins: The managed pair keeps one release record across stages.
- **D:** Incorrect for this question. A pull-based delivery controller. Why the correct answer wins: The managed pair keeps one release record across stages.

### Question 15 — C

Answer: Run Jenkins on a self-managed VM. Self-hosted Jenkins keeps the build on company hardware. A self-operated CI server whose patching is your problem. Local study-map skill 1.10 (CI/CD Architecture Stack Design), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 1 (bootstrapping and maintaining a Google Cloud organization): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A regional repository for images and packages. Why the correct answer wins: Self-hosted Jenkins keeps the build on company hardware.
- **B:** Incorrect for this question. A pull-based delivery controller. Why the correct answer wins: Self-hosted Jenkins keeps the build on company hardware.
- **C:** Correct. A self-operated CI server whose patching is your problem. In this case: Self-hosted Jenkins keeps the build on company hardware.
- **D:** Incorrect for this question. A managed pair that separates building from releasing. Why the correct answer wins: Self-hosted Jenkins keeps the build on company hardware.

### Question 16 — D

Answer: Bake the machine image with Packer. Packer produces the single signed image. A reproducible image built before deployment. Local study-map skill 1.11 (Third-Party Tooling in the Pipeline), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 1 (bootstrapping and maintaining a Google Cloud organization): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A transformation pipeline that keeps the source declarative. Why the correct answer wins: Packer produces the single signed image.
- **B:** Incorrect for this question. A templated bundle of Kubernetes resources. Why the correct answer wins: Packer produces the single signed image.
- **C:** Incorrect for this question. Declarative code that is reviewed before it is applied. Why the correct answer wins: Packer produces the single signed image.
- **D:** Correct. A reproducible image built before deployment. In this case: Packer produces the single signed image.

### Question 17 — D

Answer: Keep one base with a Kustomize overlay per environment. An overlay changes only what differs per environment. A base manifest with per-environment patches. Local study-map skill 1.12 (Multiple Environment Management), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 1 (bootstrapping and maintaining a Google Cloud organization): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. An environment that exists only while a change is tested. Why the correct answer wins: An overlay changes only what differs per environment.
- **B:** Incorrect for this question. One image per environment with the settings compiled in. Why the correct answer wins: An overlay changes only what differs per environment.
- **C:** Incorrect for this question. A permanent pre-production environment. Why the correct answer wins: An overlay changes only what differs per environment.
- **D:** Correct. A base manifest with per-environment patches. In this case: An overlay changes only what differs per environment.

### Question 18 — A, E

Answers: Register the clusters in a fleet; Put the cluster on a release channel with a maintenance window. The fleet shares policy, and the release channel sets the cadence. A group that shares policy and identity across clusters. A managed upgrade cadence inside a chosen window. Local study-map skill 1.13 (Fleets, Patching, and Cluster Upgrades), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 1 (bootstrapping and maintaining a Google Cloud organization): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Correct. A managed upgrade cadence inside a chosen window. In this case: The fleet shares policy, and the release channel sets the cadence.
- **B:** Incorrect for this question. An operator-driven upgrade with no cadence. Why the correct answer wins: The fleet shares policy, and the release channel sets the cadence.
- **C:** Incorrect for this question. A parallel cluster used to prove the upgrade. Why the correct answer wins: The fleet shares policy, and the release channel sets the cadence.
- **D:** Incorrect for this question. An environment that exists only while a change is tested. Why the correct answer wins: The fleet shares policy, and the release channel sets the cadence.
- **E:** Correct. A group that shares policy and identity across clusters. In this case: The fleet shares policy, and the release channel sets the cadence.

### Question 19 — A, E

Answers: Build a custom image that carries the approved toolchain; Use Gemini Code Assist for the suggested change. The custom image pins the toolchain, and Code Assist helps in the editor. A pinned toolchain that every workstation starts from. An in-editor assistant that proposes code. Local study-map skill 1.14 (Secure Development Environments and AI Assistance), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 1 (bootstrapping and maintaining a Google Cloud organization): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Correct. A pinned toolchain that every workstation starts from. In this case: The custom image pins the toolchain, and Code Assist helps in the editor.
- **B:** Incorrect for this question. An assistant that reads telemetry and configuration. Why the correct answer wins: The custom image pins the toolchain, and Code Assist helps in the editor.
- **C:** Incorrect for this question. Unmanaged toolchains on unmanaged machines. Why the correct answer wins: The custom image pins the toolchain, and Code Assist helps in the editor.
- **D:** Incorrect for this question. A browser terminal with limited tooling and lifetime. Why the correct answer wins: The custom image pins the toolchain, and Code Assist helps in the editor.
- **E:** Correct. An in-editor assistant that proposes code. In this case: The custom image pins the toolchain, and Code Assist helps in the editor.

### Question 20 — A

Answer: Let each developer install the tools locally. Locally installed tooling differs on every machine. Unmanaged toolchains on unmanaged machines. Local study-map skill 1.14 (Secure Development Environments and AI Assistance), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 1 (bootstrapping and maintaining a Google Cloud organization): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Correct. Unmanaged toolchains on unmanaged machines. In this case: Locally installed tooling differs on every machine.
- **B:** Incorrect for this question. A managed IDE that runs inside the project boundary. Why the correct answer wins: Locally installed tooling differs on every machine.
- **C:** Incorrect for this question. A browser terminal with limited tooling and lifetime. Why the correct answer wins: Locally installed tooling differs on every machine.
- **D:** Incorrect for this question. A pinned toolchain that every workstation starts from. Why the correct answer wins: Locally installed tooling differs on every machine.

### Question 21 — B

Answer: Create a trigger that runs the tests on every pull request. The pull-request trigger runs the policy test. A pre-merge check that blocks a bad change early. Local study-map skill 2.1 (Pipeline Triggers and Design), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 2 (building and implementing CI/CD pipelines): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A trigger that starts the build on a branch change. Why the correct answer wins: The pull-request trigger runs the policy test.
- **B:** Correct. A pre-merge check that blocks a bad change early. In this case: The pull-request trigger runs the policy test.
- **C:** Incorrect for this question. A hand-built artifact with no pipeline record. Why the correct answer wins: The pull-request trigger runs the policy test.
- **D:** Incorrect for this question. A release build that a tag alone can start. Why the correct answer wins: The pull-request trigger runs the policy test.

### Question 22 — D

Answer: Trigger the pipeline only on a signed tag. The tag identifies the exact commit that built the release. A release build that a tag alone can start. Local study-map skill 2.1 (Pipeline Triggers and Design), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 2 (building and implementing CI/CD pipelines): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A required human approval before the release promotes. Why the correct answer wins: The tag identifies the exact commit that built the release.
- **B:** Incorrect for this question. A pre-merge check that blocks a bad change early. Why the correct answer wins: The tag identifies the exact commit that built the release.
- **C:** Incorrect for this question. A trigger that starts the build on a branch change. Why the correct answer wins: The tag identifies the exact commit that built the release.
- **D:** Correct. A release build that a tag alone can start. In this case: The tag identifies the exact commit that built the release.

### Question 23 — A

Answer: Have an engineer build locally and upload the result. A hand build depends on a machine that has vanished. A hand-built artifact with no pipeline record. Local study-map skill 2.1 (Pipeline Triggers and Design), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 2 (building and implementing CI/CD pipelines): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Correct. A hand-built artifact with no pipeline record. In this case: A hand build depends on a machine that has vanished.
- **B:** Incorrect for this question. A trigger that starts the build on a branch change. Why the correct answer wins: A hand build depends on a machine that has vanished.
- **C:** Incorrect for this question. A release build that a tag alone can start. Why the correct answer wins: A hand build depends on a machine that has vanished.
- **D:** Incorrect for this question. A pre-merge check that blocks a bad change early. Why the correct answer wins: A hand build depends on a machine that has vanished.

### Question 24 — A

Answer: Store the build output in Artifact Registry. A regional repository keeps artifacts next to the clusters. A regional repository for images and packages. Local study-map skill 2.2 (Artifact Management), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 2 (building and implementing CI/CD pipelines): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Correct. A regional repository for images and packages. In this case: A regional repository keeps artifacts next to the clusters.
- **B:** Incorrect for this question. The legacy registry without regional repository controls. Why the correct answer wins: A regional repository keeps artifacts next to the clusters.
- **C:** Incorrect for this question. An immutable tag that identifies the source revision. Why the correct answer wins: A regional repository keeps artifacts next to the clusters.
- **D:** Incorrect for this question. A moving tag that hides which build is running. Why the correct answer wins: A regional repository keeps artifacts next to the clusters.

### Question 25 — A

Answer: Reuse the latest tag for every build. A moving reference hides which build actually ran. A moving tag that hides which build is running. Local study-map skill 2.2 (Artifact Management), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 2 (building and implementing CI/CD pipelines): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Correct. A moving tag that hides which build is running. In this case: A moving reference hides which build actually ran.
- **B:** Incorrect for this question. An immutable tag that identifies the source revision. Why the correct answer wins: A moving reference hides which build actually ran.
- **C:** Incorrect for this question. Metadata that ties an artifact to its build inputs. Why the correct answer wins: A moving reference hides which build actually ran.
- **D:** Incorrect for this question. A regional repository for images and packages. Why the correct answer wins: A moving reference hides which build actually ran.

### Question 26 — B, D

Answers: Define the attached cluster as the delivery target; Use a GKE cluster in the pipeline project as the target. The attached cluster covers on-premises, and the GKE target covers the project. A target that points at a GKE cluster outside Google Cloud. A delivery target that sits inside the same project. Local study-map skill 2.3 (Hybrid and Multicloud Deployment Targets), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 2 (building and implementing CI/CD pipelines): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A required human approval before the release promotes. Why the correct answer wins: The attached cluster covers on-premises, and the GKE target covers the project.
- **B:** Correct. A target that points at a GKE cluster outside Google Cloud. In this case: The attached cluster covers on-premises, and the GKE target covers the project.
- **C:** Incorrect for this question. The immutable record of who released what. Why the correct answer wins: The attached cluster covers on-premises, and the GKE target covers the project.
- **D:** Correct. A delivery target that sits inside the same project. In this case: The attached cluster covers on-premises, and the GKE target covers the project.
- **E:** Incorrect for this question. A revision-based target with traffic control. Why the correct answer wins: The attached cluster covers on-premises, and the GKE target covers the project.

### Question 27 — B

Answer: Deliver to a Cloud Run service revision. A Cloud Run target applies the split to revisions. A revision-based target with traffic control. Local study-map skill 2.3 (Hybrid and Multicloud Deployment Targets), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 2 (building and implementing CI/CD pipelines): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A target that points at a GKE cluster outside Google Cloud. Why the correct answer wins: A Cloud Run target applies the split to revisions.
- **B:** Correct. A revision-based target with traffic control. In this case: A Cloud Run target applies the split to revisions.
- **C:** Incorrect for this question. The immutable record of who released what. Why the correct answer wins: A Cloud Run target applies the split to revisions.
- **D:** Incorrect for this question. A delivery target that sits inside the same project. Why the correct answer wins: A Cloud Run target applies the split to revisions.

### Question 28 — A

Answer: Promote automatically to every target in the chain. Unattended promotion removed the review step. An unattended path from commit to production. Local study-map skill 2.4 (Approval Flows and Deployment Process), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 2 (building and implementing CI/CD pipelines): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Correct. An unattended path from commit to production. In this case: Unattended promotion removed the review step.
- **B:** Incorrect for this question. A hand-built artifact with no pipeline record. Why the correct answer wins: Unattended promotion removed the review step.
- **C:** Incorrect for this question. The immutable record of who released what. Why the correct answer wins: Unattended promotion removed the review step.
- **D:** Incorrect for this question. A required human approval before the release promotes. Why the correct answer wins: Unattended promotion removed the review step.

### Question 29 — D, E

Answers: Read Cloud Audit Logs for the release history; Describe the build with its supply chain level and signed provenance. Audit logs give the history, and the supply chain level states integrity. The immutable record of who released what. A published statement about how the artifact was produced. Local study-map skill 2.5 (Deployment Auditing and Tracking), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 2 (building and implementing CI/CD pipelines): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A required human approval before the release promotes. Why the correct answer wins: Audit logs give the history, and the supply chain level states integrity.
- **B:** Incorrect for this question. An immutable tag that identifies the source revision. Why the correct answer wins: Audit logs give the history, and the supply chain level states integrity.
- **C:** Incorrect for this question. Metadata that ties an artifact to its build inputs. Why the correct answer wins: Audit logs give the history, and the supply chain level states integrity.
- **D:** Correct. A published statement about how the artifact was produced. In this case: Audit logs give the history, and the supply chain level states integrity.
- **E:** Correct. The immutable record of who released what. In this case: Audit logs give the history, and the supply chain level states integrity.

### Question 30 — A

Answer: Inspect the build provenance attestation. Provenance ties the artifact to the reviewed commit. Metadata that ties an artifact to its build inputs. Local study-map skill 2.5 (Deployment Auditing and Tracking), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 2 (building and implementing CI/CD pipelines): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Correct. Metadata that ties an artifact to its build inputs. In this case: Provenance ties the artifact to the reviewed commit.
- **B:** Incorrect for this question. An immutable tag that identifies the source revision. Why the correct answer wins: Provenance ties the artifact to the reviewed commit.
- **C:** Incorrect for this question. A published statement about how the artifact was produced. Why the correct answer wins: Provenance ties the artifact to the reviewed commit.
- **D:** Incorrect for this question. The immutable record of who released what. Why the correct answer wins: Provenance ties the artifact to the reviewed commit.

### Question 31 — C

Answer: Send ten percent of traffic to the new revision and watch the SLI. The canary proves the change on a small slice. A small traffic slice that bounds the blast radius. Local study-map skill 2.6 (Deployment Strategies), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 2 (building and implementing CI/CD pipelines): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A full outage during the change. Why the correct answer wins: The canary proves the change on a small slice.
- **B:** Incorrect for this question. A gradual replacement of the running instances. Why the correct answer wins: The canary proves the change on a small slice.
- **C:** Correct. A small traffic slice that bounds the blast radius. In this case: The canary proves the change on a small slice.
- **D:** Incorrect for this question. Two full environments with an instant cutover. Why the correct answer wins: The canary proves the change on a small slice.

### Question 32 — C

Answer: Split traffic with a Cloud Service Mesh route. The mesh route shifts weights hour by hour. Weighted routing between two service versions. Local study-map skill 2.6 (Deployment Strategies), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 2 (building and implementing CI/CD pipelines): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Two full environments with an instant cutover. Why the correct answer wins: The mesh route shifts weights hour by hour.
- **B:** Incorrect for this question. A full outage during the change. Why the correct answer wins: The mesh route shifts weights hour by hour.
- **C:** Correct. Weighted routing between two service versions. In this case: The mesh route shifts weights hour by hour.
- **D:** Incorrect for this question. A small traffic slice that bounds the blast radius. Why the correct answer wins: The mesh route shifts weights hour by hour.

### Question 33 — C

Answer: Put the behaviour behind a feature flag. The flag keeps the engine off for most accounts. A runtime switch that separates deploy from release. Local study-map skill 2.6 (Deployment Strategies), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 2 (building and implementing CI/CD pipelines): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A small traffic slice that bounds the blast radius. Why the correct answer wins: The flag keeps the engine off for most accounts.
- **B:** Incorrect for this question. Two full environments with an instant cutover. Why the correct answer wins: The flag keeps the engine off for most accounts.
- **C:** Correct. A runtime switch that separates deploy from release. In this case: The flag keeps the engine off for most accounts.
- **D:** Incorrect for this question. A gradual replacement of the running instances. Why the correct answer wins: The flag keeps the engine off for most accounts.

### Question 34 — D

Answer: Gate the rollout on average CPU alone. A CPU gate does not measure what users experience. A resource signal that says nothing about user success. Local study-map skill 2.7 (Deployment Success Metrics), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 2 (building and implementing CI/CD pipelines): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. An automated decision driven by the service objective. Why the correct answer wins: A CPU gate does not measure what users experience.
- **B:** Incorrect for this question. A probe that exercises the path from outside. Why the correct answer wins: A CPU gate does not measure what users experience.
- **C:** Incorrect for this question. A required human approval before the release promotes. Why the correct answer wins: A CPU gate does not measure what users experience.
- **D:** Correct. A resource signal that says nothing about user success. In this case: A CPU gate does not measure what users experience.

### Question 35 — B

Answer: Make the failed step idempotent and re-run it. An idempotent step creates the resource only once. A safe repeat that converges on the same state. Local study-map skill 2.8 (Troubleshooting Deployment Issues), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 2 (building and implementing CI/CD pipelines): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. An untracked change to the live environment. Why the correct answer wins: An idempotent step creates the resource only once.
- **B:** Correct. A safe repeat that converges on the same state. In this case: An idempotent step creates the resource only once.
- **C:** Incorrect for this question. A return to the last known good release. Why the correct answer wins: An idempotent step creates the resource only once.
- **D:** Incorrect for this question. The step output that names the failing command. Why the correct answer wins: An idempotent step creates the resource only once.

### Question 36 — C

Answer: Start from the failed step log in Cloud Build. The step log holds the command that ran. The step output that names the failing command. Local study-map skill 2.8 (Troubleshooting Deployment Issues), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 2 (building and implementing CI/CD pipelines): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A safe repeat that converges on the same state. Why the correct answer wins: The step log holds the command that ran.
- **B:** Incorrect for this question. The immutable record of who released what. Why the correct answer wins: The step log holds the command that ran.
- **C:** Correct. The step output that names the failing command. In this case: The step log holds the command that ran.
- **D:** Incorrect for this question. A return to the last known good release. Why the correct answer wins: The step log holds the command that ran.

### Question 37 — B

Answer: Encrypt the payload with a Cloud KMS key. KMS wraps the data under that customer-controlled key. A managed key that wraps the data. Local study-map skill 2.9 (Key Management), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 2 (building and implementing CI/CD pipelines): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Managed issuance and renewal for the endpoint. Why the correct answer wins: KMS wraps the data under that customer-controlled key.
- **B:** Correct. A managed key that wraps the data. In this case: KMS wraps the data under that customer-controlled key.
- **C:** Incorrect for this question. A secret readable by everyone with repository access. Why the correct answer wins: KMS wraps the data under that customer-controlled key.
- **D:** Incorrect for this question. A managed store with immutable versions and audit. Why the correct answer wins: KMS wraps the data under that customer-controlled key.

### Question 38 — A

Answer: Store the credential in Secret Manager with versions. The newest secret version is read on the next request. A managed store with immutable versions and audit. Local study-map skill 2.9 (Key Management), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 2 (building and implementing CI/CD pipelines): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Correct. A managed store with immutable versions and audit. In this case: The newest secret version is read on the next request.
- **B:** Incorrect for this question. A store for versioned application parameters. Why the correct answer wins: The newest secret version is read on the next request.
- **C:** Incorrect for this question. A managed key that wraps the data. Why the correct answer wins: The newest secret version is read on the next request.
- **D:** Incorrect for this question. A secret readable by everyone with repository access. Why the correct answer wins: The newest secret version is read on the next request.

### Question 39 — B

Answer: Keep the non-secret configuration in Parameter Manager. Parameter Manager shows the current values. A store for versioned application parameters. Local study-map skill 2.10 (Configuration and Secret Management), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 2 (building and implementing CI/CD pipelines): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A secret readable by everyone with repository access. Why the correct answer wins: Parameter Manager shows the current values.
- **B:** Correct. A store for versioned application parameters. In this case: Parameter Manager shows the current values.
- **C:** Incorrect for this question. One image per environment with the settings compiled in. Why the correct answer wins: Parameter Manager shows the current values.
- **D:** Incorrect for this question. A managed store with immutable versions and audit. Why the correct answer wins: Parameter Manager shows the current values.

### Question 40 — C

Answer: Commit the credential to the private repository. A committed secret is readable by every repository member. A secret readable by everyone with repository access. Local study-map skill 2.10 (Configuration and Secret Management), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 2 (building and implementing CI/CD pipelines): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A managed store with immutable versions and audit. Why the correct answer wins: A committed secret is readable by every repository member.
- **B:** Incorrect for this question. A credential read only when the workload starts. Why the correct answer wins: A committed secret is readable by every repository member.
- **C:** Correct. A secret readable by everyone with repository access. In this case: A committed secret is readable by every repository member.
- **D:** Incorrect for this question. A store for versioned application parameters. Why the correct answer wins: A committed secret is readable by every repository member.

### Question 41 — B, E

Answers: Inject the secret at build time into the image layer; Mount the secret at runtime from Secret Manager. The package fetch needs build time, and the service needs a runtime mount. A secret baked into an artifact anyone can pull. A credential read only when the workload starts. Local study-map skill 2.11 (Build-Time versus Runtime Secret Injection), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 2 (building and implementing CI/CD pipelines): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A secret readable by everyone with repository access. Why the correct answer wins: The package fetch needs build time, and the service needs a runtime mount.
- **B:** Correct. A credential read only when the workload starts. In this case: The package fetch needs build time, and the service needs a runtime mount.
- **C:** Incorrect for this question. A store for versioned application parameters. Why the correct answer wins: The package fetch needs build time, and the service needs a runtime mount.
- **D:** Incorrect for this question. A value left visible in the build history. Why the correct answer wins: The package fetch needs build time, and the service needs a runtime mount.
- **E:** Correct. A secret baked into an artifact anyone can pull. In this case: The package fetch needs build time, and the service needs a runtime mount.

### Question 42 — A, B

Answers: Enable Artifact Analysis scanning on the repository; Fail the pipeline on a critical vulnerability finding. Artifact Analysis refreshes the findings, and the gate blocks the promotion. Vulnerability findings for the stored artifacts. A policy that blocks the promotion. Local study-map skill 2.12 (Vulnerability Scanning and Artifact Analysis), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 2 (building and implementing CI/CD pipelines): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Correct. A policy that blocks the promotion. In this case: Artifact Analysis refreshes the findings, and the gate blocks the promotion.
- **B:** Correct. Vulnerability findings for the stored artifacts. In this case: Artifact Analysis refreshes the findings, and the gate blocks the promotion.
- **C:** Incorrect for this question. An identity that cannot promote outside its environment. Why the correct answer wins: Artifact Analysis refreshes the findings, and the gate blocks the promotion.
- **D:** Incorrect for this question. An admission check that only attested images may run. Why the correct answer wins: Artifact Analysis refreshes the findings, and the gate blocks the promotion.
- **E:** Incorrect for this question. A finding that no pipeline blocks on. Why the correct answer wins: Artifact Analysis refreshes the findings, and the gate blocks the promotion.

### Question 43 — B

Answer: Enforce Binary Authorization attestations before deploy. Binary Authorization refuses every image without a valid attestation. An admission check that only attested images may run. Local study-map skill 2.13 (Supply Chain Security and Binary Authorization), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 2 (building and implementing CI/CD pipelines): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A policy that blocks the promotion. Why the correct answer wins: Binary Authorization refuses every image without a valid attestation.
- **B:** Correct. An admission check that only attested images may run. In this case: Binary Authorization refuses every image without a valid attestation.
- **C:** Incorrect for this question. Vulnerability findings for the stored artifacts. Why the correct answer wins: Binary Authorization refuses every image without a valid attestation.
- **D:** Incorrect for this question. An identity that cannot promote outside its environment. Why the correct answer wins: Binary Authorization refuses every image without a valid attestation.

### Question 44 — A

Answer: Use one identity with deploy rights in every environment. One shared identity gave staging rights in production. A single broad credential across the whole estate. Local study-map skill 2.13 (Supply Chain Security and Binary Authorization), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 2 (building and implementing CI/CD pipelines): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Correct. A single broad credential across the whole estate. In this case: One shared identity gave staging rights in production.
- **B:** Incorrect for this question. A long-lived credential stored outside the platform. Why the correct answer wins: One shared identity gave staging rights in production.
- **C:** Incorrect for this question. An identity that cannot promote outside its environment. Why the correct answer wins: One shared identity gave staging rights in production.
- **D:** Incorrect for this question. A build identity with broad write access. Why the correct answer wins: One shared identity gave staging rights in production.

### Question 45 — D

Answer: Download a JSON key file for the service account. A shared key file cannot be scoped to one environment. A long-lived credential stored outside the platform. Local study-map skill 2.14 (Per-Environment IAM Policy), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 2 (building and implementing CI/CD pipelines): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A single broad credential across the whole estate. Why the correct answer wins: A shared key file cannot be scoped to one environment.
- **B:** Incorrect for this question. An identity that cannot promote outside its environment. Why the correct answer wins: A shared key file cannot be scoped to one environment.
- **C:** Incorrect for this question. A build identity with broad write access. Why the correct answer wins: A shared key file cannot be scoped to one environment.
- **D:** Correct. A long-lived credential stored outside the platform. In this case: A shared key file cannot be scoped to one environment.

### Question 46 — B

Answer: Set an internal target on that indicator. The internal target is deliberately stricter than the contract. An objective the team commits to without a contract. Local study-map skill 3.1 (SLIs, SLOs, and SLAs), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 3 (applying site reliability engineering practices): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. An external commitment that carries a consequence. Why the correct answer wins: The internal target is deliberately stricter than the contract.
- **B:** Correct. An objective the team commits to without a contract. In this case: The internal target is deliberately stricter than the contract.
- **C:** Incorrect for this question. A signal that the budget is going too quickly. Why the correct answer wins: The internal target is deliberately stricter than the contract.
- **D:** Incorrect for this question. A measured indicator of how the service behaves. Why the correct answer wins: The internal target is deliberately stricter than the contract.

### Question 47 — D

Answer: Track the ratio of good requests to total requests. The SLI defines what counts as a good request. A measured indicator of how the service behaves. Local study-map skill 3.1 (SLIs, SLOs, and SLAs), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 3 (applying site reliability engineering practices): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. An objective the team commits to without a contract. Why the correct answer wins: The SLI defines what counts as a good request.
- **B:** Incorrect for this question. A uniform promise that most services do not need. Why the correct answer wins: The SLI defines what counts as a good request.
- **C:** Incorrect for this question. An external commitment that carries a consequence. Why the correct answer wins: The SLI defines what counts as a good request.
- **D:** Correct. A measured indicator of how the service behaves. In this case: The SLI defines what counts as a good request.

### Question 48 — B

Answer: Publish a contractual promise with a remedy. The remedy belongs in the service level agreement. An external commitment that carries a consequence. Local study-map skill 3.1 (SLIs, SLOs, and SLAs), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 3 (applying site reliability engineering practices): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. An explicit trade between reliability and change. Why the correct answer wins: The remedy belongs in the service level agreement.
- **B:** Correct. An external commitment that carries a consequence. In this case: The remedy belongs in the service level agreement.
- **C:** Incorrect for this question. An objective the team commits to without a contract. Why the correct answer wins: The remedy belongs in the service level agreement.
- **D:** Incorrect for this question. A measured indicator of how the service behaves. Why the correct answer wins: The remedy belongs in the service level agreement.

### Question 49 — A, B

Answers: Stop feature releases when the error budget is spent; Choose three nines and spend the difference on features. The freeze protects the target, and three nines keeps it affordable. A rule that trades velocity for reliability. An explicit trade between reliability and change. Local study-map skill 3.2 (Error Budgets), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 3 (applying site reliability engineering practices): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Correct. An explicit trade between reliability and change. In this case: The freeze protects the target, and three nines keeps it affordable.
- **B:** Correct. A rule that trades velocity for reliability. In this case: The freeze protects the target, and three nines keeps it affordable.
- **C:** Incorrect for this question. An external commitment that carries a consequence. Why the correct answer wins: The freeze protects the target, and three nines keeps it affordable.
- **D:** Incorrect for this question. A signal that the budget is going too quickly. Why the correct answer wins: The freeze protects the target, and three nines keeps it affordable.
- **E:** Incorrect for this question. A uniform promise that most services do not need. Why the correct answer wins: The freeze protects the target, and three nines keeps it affordable.

### Question 50 — C

Answer: Alert on a fast error-budget burn rate. The projection shows the allowance running out this week. A signal that the budget is going too quickly. Local study-map skill 3.2 (Error Budgets), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 3 (applying site reliability engineering practices): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. An external commitment that carries a consequence. Why the correct answer wins: The projection shows the allowance running out this week.
- **B:** Incorrect for this question. A static threshold on a resource metric. Why the correct answer wins: The projection shows the allowance running out this week.
- **C:** Correct. A signal that the budget is going too quickly. In this case: The projection shows the allowance running out this week.
- **D:** Incorrect for this question. A rule that trades velocity for reliability. Why the correct answer wins: The projection shows the allowance running out this week.

### Question 51 — C

Answer: Assume five nines for every service. One extreme target for every workload spends effort needlessly. A uniform promise that most services do not need. Local study-map skill 3.3 (Cost of Reliability and Nines), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 3 (applying site reliability engineering practices): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. An explicit trade between reliability and change. Why the correct answer wins: One extreme target for every workload spends effort needlessly.
- **B:** Incorrect for this question. An external commitment that carries a consequence. Why the correct answer wins: One extreme target for every workload spends effort needlessly.
- **C:** Correct. A uniform promise that most services do not need. In this case: One extreme target for every workload spends effort needlessly.
- **D:** Incorrect for this question. Capacity arranged ahead of a known peak. Why the correct answer wins: One extreme target for every workload spends effort needlessly.

### Question 52 — A

Answer: Choose three nines and spend the difference on features. The trade keeps the features and accepts fewer nines. An explicit trade between reliability and change. Local study-map skill 3.3 (Cost of Reliability and Nines), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 3 (applying site reliability engineering practices): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Correct. An explicit trade between reliability and change. In this case: The trade keeps the features and accepts fewer nines.
- **B:** Incorrect for this question. A uniform promise that most services do not need. Why the correct answer wins: The trade keeps the features and accepts fewer nines.
- **C:** Incorrect for this question. An owned entry with its tier and dependencies. Why the correct answer wins: The trade keeps the features and accepts fewer nines.
- **D:** Incorrect for this question. An external commitment that carries a consequence. Why the correct answer wins: The trade keeps the features and accepts fewer nines.

### Question 53 — A

Answer: Announce the retirement date and withdraw traffic gradually. The plan sequences the shutdown and the DNS withdrawal. A planned withdrawal with a migration path. Local study-map skill 3.4 (Service Lifecycle Management), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 3 (applying site reliability engineering practices): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Correct. A planned withdrawal with a migration path. In this case: The plan sequences the shutdown and the DNS withdrawal.
- **B:** Incorrect for this question. An owned entry with its tier and dependencies. Why the correct answer wins: The plan sequences the shutdown and the DNS withdrawal.
- **C:** Incorrect for this question. An unowned workload that still costs money. Why the correct answer wins: The plan sequences the shutdown and the DNS withdrawal.
- **D:** Incorrect for this question. A graceful handover of in-flight requests. Why the correct answer wins: The plan sequences the shutdown and the DNS withdrawal.

### Question 54 — B

Answer: Register the service in the service catalog. The catalog holds the escalation path for each service. An owned entry with its tier and dependencies. Local study-map skill 3.4 (Service Lifecycle Management), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 3 (applying site reliability engineering practices): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Capacity arranged ahead of a known peak. Why the correct answer wins: The catalog holds the escalation path for each service.
- **B:** Correct. An owned entry with its tier and dependencies. In this case: The catalog holds the escalation path for each service.
- **C:** Incorrect for this question. A planned withdrawal with a migration path. Why the correct answer wins: The catalog holds the escalation path for each service.
- **D:** Incorrect for this question. An unowned workload that still costs money. Why the correct answer wins: The catalog holds the escalation path for each service.

### Question 55 — C

Answer: Request a quota increase and reserve capacity before the launch. A quota increase covers the enrolment peak. Capacity arranged ahead of a known peak. Local study-map skill 3.5 (Capacity Planning and Quotas), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 3 (applying site reliability engineering practices): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A flexible placement into a cheaper window. Why the correct answer wins: A quota increase covers the enrolment peak.
- **B:** Incorrect for this question. Limits that throttle at the worst possible moment. Why the correct answer wins: A quota increase covers the enrolment peak.
- **C:** Correct. Capacity arranged ahead of a known peak. In this case: A quota increase covers the enrolment peak.
- **D:** Incorrect for this question. Calendar-driven capacity with no feedback loop. Why the correct answer wins: A quota increase covers the enrolment peak.

### Question 56 — D

Answer: Add capacity on a fixed calendar schedule. Calendar capacity is aimed at the wrong day. Calendar-driven capacity with no feedback loop. Local study-map skill 3.5 (Capacity Planning and Quotas), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 3 (applying site reliability engineering practices): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Capacity arranged ahead of a known peak. Why the correct answer wins: Calendar capacity is aimed at the wrong day.
- **B:** Incorrect for this question. A flexible placement into a cheaper window. Why the correct answer wins: Calendar capacity is aimed at the wrong day.
- **C:** Incorrect for this question. Managed instance scaling from a resource metric. Why the correct answer wins: Calendar capacity is aimed at the wrong day.
- **D:** Correct. Calendar-driven capacity with no feedback loop. In this case: Calendar capacity is aimed at the wrong day.

### Question 57 — B, E

Answers: Scale on queue depth with a horizontal pod autoscaler; Put the instance group behind an autoscaler on CPU. The backlog scales the workers, and CPU scales the instance group. Replica scaling driven by a work signal. Managed instance scaling from a resource metric. Local study-map skill 3.6 (Autoscaling), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 3 (applying site reliability engineering practices): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Concurrency-based replica scaling. Why the correct answer wins: The backlog scales the workers, and CPU scales the instance group.
- **B:** Correct. Replica scaling driven by a work signal. In this case: The backlog scales the workers, and CPU scales the instance group.
- **C:** Incorrect for this question. Calendar-driven capacity with no feedback loop. Why the correct answer wins: The backlog scales the workers, and CPU scales the instance group.
- **D:** Incorrect for this question. A flexible placement into a cheaper window. Why the correct answer wins: The backlog scales the workers, and CPU scales the instance group.
- **E:** Correct. Managed instance scaling from a resource metric. In this case: The backlog scales the workers, and CPU scales the instance group.

### Question 58 — B

Answer: Set Cloud Run concurrency so replicas follow load. Concurrency decides when another revision instance starts. Concurrency-based replica scaling. Local study-map skill 3.6 (Autoscaling), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 3 (applying site reliability engineering practices): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Calendar-driven capacity with no feedback loop. Why the correct answer wins: Concurrency decides when another revision instance starts.
- **B:** Correct. Concurrency-based replica scaling. In this case: Concurrency decides when another revision instance starts.
- **C:** Incorrect for this question. Replica scaling driven by a work signal. Why the correct answer wins: Concurrency decides when another revision instance starts.
- **D:** Incorrect for this question. Managed instance scaling from a resource metric. Why the correct answer wins: Concurrency decides when another revision instance starts.

### Question 59 — A, E

Answers: Drain connections before removing the instance; Shift traffic with a DNS routing policy. Draining finishes the requests, and the routing policy moves the name. A graceful handover of in-flight requests. A name-level redirect to a healthy region. Local study-map skill 3.7 (Traffic Draining and Redirection), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 3 (applying site reliability engineering practices): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Correct. A graceful handover of in-flight requests. In this case: Draining finishes the requests, and the routing policy moves the name.
- **B:** Incorrect for this question. A health-checked switch between backends. Why the correct answer wins: Draining finishes the requests, and the routing policy moves the name.
- **C:** Incorrect for this question. Extra supply in a different location. Why the correct answer wins: Draining finishes the requests, and the routing policy moves the name.
- **D:** Incorrect for this question. Capacity arranged ahead of a known peak. Why the correct answer wins: Draining finishes the requests, and the routing policy moves the name.
- **E:** Correct. A name-level redirect to a healthy region. In this case: Draining finishes the requests, and the routing policy moves the name.

### Question 60 — D

Answer: Use a load balancer failover backend. The failover backend reacts to the health check. A health-checked switch between backends. Local study-map skill 3.7 (Traffic Draining and Redirection), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 3 (applying site reliability engineering practices): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Extra supply in a different location. Why the correct answer wins: The failover backend reacts to the health check.
- **B:** Incorrect for this question. A name-level redirect to a healthy region. Why the correct answer wins: The failover backend reacts to the health check.
- **C:** Incorrect for this question. A graceful handover of in-flight requests. Why the correct answer wins: The failover backend reacts to the health check.
- **D:** Correct. A health-checked switch between backends. In this case: The failover backend reacts to the health check.

### Question 61 — D

Answer: Add capacity in a second region. Capacity elsewhere absorbs the forty-minute spike. Extra supply in a different location. Local study-map skill 3.8 (Incident Capacity), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 3 (applying site reliability engineering practices): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Capacity arranged ahead of a known peak. Why the correct answer wins: Capacity elsewhere absorbs the forty-minute spike.
- **B:** Incorrect for this question. A graceful handover of in-flight requests. Why the correct answer wins: Capacity elsewhere absorbs the forty-minute spike.
- **C:** Incorrect for this question. A health-checked switch between backends. Why the correct answer wins: Capacity elsewhere absorbs the forty-minute spike.
- **D:** Correct. Extra supply in a different location. In this case: Capacity elsewhere absorbs the forty-minute spike.

### Question 62 — D

Answer: Redeploy the previous image to the affected service. Redeploying the previous build restores the healthy version. A known good artifact restored in place. Local study-map skill 3.9 (Rollback Strategies), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 3 (applying site reliability engineering practices): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. An untracked change to the live environment. Why the correct answer wins: Redeploying the previous build restores the healthy version.
- **B:** Incorrect for this question. A paired migration that can be undone. Why the correct answer wins: Redeploying the previous build restores the healthy version.
- **C:** Incorrect for this question. No action while users are still failing. Why the correct answer wins: Redeploying the previous build restores the healthy version.
- **D:** Correct. A known good artifact restored in place. In this case: Redeploying the previous build restores the healthy version.

### Question 63 — B

Answer: Wait for the error rate to settle on its own. Waiting leaves users failing while the cause remains. No action while users are still failing. Local study-map skill 3.9 (Rollback Strategies), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 3 (applying site reliability engineering practices): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A known good artifact restored in place. Why the correct answer wins: Waiting leaves users failing while the cause remains.
- **B:** Correct. No action while users are still failing. In this case: Waiting leaves users failing while the cause remains.
- **C:** Incorrect for this question. A paired migration that can be undone. Why the correct answer wins: Waiting leaves users failing while the cause remains.
- **D:** Incorrect for this question. An untracked change to the live environment. Why the correct answer wins: Waiting leaves users failing while the cause remains.

### Question 64 — A, C

Answers: Turn on VPC Flow Logs for the subnet; Read the Cloud Service Mesh telemetry. Flow logs show the denials, and mesh telemetry shows the rates. Per-connection records of accepted and denied traffic. Request metrics emitted by the sidecar proxies. Local study-map skill 4.1 (Log Collection and Ingestion), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 4 (implementing observability practices and troubleshooting): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Correct. Request metrics emitted by the sidecar proxies. In this case: Flow logs show the denials, and mesh telemetry shows the rates.
- **B:** Incorrect for this question. A vendor-neutral pipeline for traces and metrics. Why the correct answer wins: Flow logs show the denials, and mesh telemetry shows the rates.
- **C:** Correct. Per-connection records of accepted and denied traffic. In this case: Flow logs show the denials, and mesh telemetry shows the rates.
- **D:** Incorrect for this question. A collector that ships logs and metrics from the VM. Why the correct answer wins: Flow logs show the denials, and mesh telemetry shows the rates.
- **E:** Incorrect for this question. A record of reads and writes on the resource. Why the correct answer wins: Flow logs show the denials, and mesh telemetry shows the rates.

### Question 65 — C

Answer: Install the Ops Agent on the instances. The Ops Agent exposes the memory metric. A collector that ships logs and metrics from the VM. Local study-map skill 4.1 (Log Collection and Ingestion), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 4 (implementing observability practices and troubleshooting): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Request metrics emitted by the sidecar proxies. Why the correct answer wins: The Ops Agent exposes the memory metric.
- **B:** Incorrect for this question. A record of reads and writes on the resource. Why the correct answer wins: The Ops Agent exposes the memory metric.
- **C:** Correct. A collector that ships logs and metrics from the VM. In this case: The Ops Agent exposes the memory metric.
- **D:** Incorrect for this question. Per-connection records of accepted and denied traffic. Why the correct answer wins: The Ops Agent exposes the memory metric.

### Question 66 — A

Answer: Measure log volume per service before choosing a retention period. Measuring the volume is what sizes the bucket. A cost estimate driven by actual ingest. Local study-map skill 4.2 (Log Optimization and Cost), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 4 (implementing observability practices and troubleshooting): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Correct. A cost estimate driven by actual ingest. In this case: Measuring the volume is what sizes the bucket.
- **B:** Incorrect for this question. A retention period that cannot be shortened. Why the correct answer wins: Measuring the volume is what sizes the bucket.
- **C:** Incorrect for this question. A fraction kept for diagnosis at lower cost. Why the correct answer wins: Measuring the volume is what sizes the bucket.
- **D:** Incorrect for this question. A filter that drops matching entries before storage. Why the correct answer wins: Measuring the volume is what sizes the bucket.

### Question 67 — B

Answer: Add an exclusion for the health-check entries. The exclusion stops those entries being stored. A filter that drops matching entries before storage. Local study-map skill 4.2 (Log Optimization and Cost), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 4 (implementing observability practices and troubleshooting): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A sink suited to cheap long-term retention. Why the correct answer wins: The exclusion stops those entries being stored.
- **B:** Correct. A filter that drops matching entries before storage. In this case: The exclusion stops those entries being stored.
- **C:** Incorrect for this question. A fraction kept for diagnosis at lower cost. Why the correct answer wins: The exclusion stops those entries being stored.
- **D:** Incorrect for this question. A label removal that cuts the stored series. Why the correct answer wins: The exclusion stops those entries being stored.

### Question 68 — C

Answer: Filter with the Logging query language on the resource label. The query filters on the tenant label. A precise query over the stored entries. Local study-map skill 4.3 (Logs Explorer and Query Language), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 4 (implementing observability practices and troubleshooting): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A sink that lands logs in a queryable table. Why the correct answer wins: The query filters on the tenant label.
- **B:** Incorrect for this question. An interactive view with field filters. Why the correct answer wins: The query filters on the tenant label.
- **C:** Correct. A precise query over the stored entries. In this case: The query filters on the tenant label.
- **D:** Incorrect for this question. A counter derived from matching entries. Why the correct answer wins: The query filters on the tenant label.

### Question 69 — C

Answer: Open the Logs Explorer and pivot from the error entry. Pivoting on the field shows all its entries. An interactive view with field filters. Local study-map skill 4.3 (Logs Explorer and Query Language), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 4 (implementing observability practices and troubleshooting): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A probe that exercises the path from outside. Why the correct answer wins: Pivoting on the field shows all its entries.
- **B:** Incorrect for this question. A counter derived from matching entries. Why the correct answer wins: Pivoting on the field shows all its entries.
- **C:** Correct. An interactive view with field filters. In this case: Pivoting on the field shows all its entries.
- **D:** Incorrect for this question. A precise query over the stored entries. Why the correct answer wins: Pivoting on the field shows all its entries.

### Question 70 — D

Answer: Route the entries to a BigQuery dataset. A BigQuery sink allows that join. A sink that lands logs in a queryable table. Local study-map skill 4.4 (Log Export and Retention), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 4 (implementing observability practices and troubleshooting): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A retention period that cannot be shortened. Why the correct answer wins: A BigQuery sink allows that join.
- **B:** Incorrect for this question. A sink that streams entries to another consumer. Why the correct answer wins: A BigQuery sink allows that join.
- **C:** Incorrect for this question. A sink suited to cheap long-term retention. Why the correct answer wins: A BigQuery sink allows that join.
- **D:** Correct. A sink that lands logs in a queryable table. In this case: A BigQuery sink allows that join.

### Question 71 — D

Answer: Set the log bucket retention and lock it. The lock proves the period cannot be shortened. A retention period that cannot be shortened. Local study-map skill 4.4 (Log Export and Retention), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 4 (implementing observability practices and troubleshooting): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A sink suited to cheap long-term retention. Why the correct answer wins: The lock proves the period cannot be shortened.
- **B:** Incorrect for this question. A sink that lands logs in a queryable table. Why the correct answer wins: The lock proves the period cannot be shortened.
- **C:** Incorrect for this question. A cost estimate driven by actual ingest. Why the correct answer wins: The lock proves the period cannot be shortened.
- **D:** Correct. A retention period that cannot be shortened. In this case: The lock proves the period cannot be shortened.

### Question 72 — D

Answer: Redact the email field with a log processor. The processor masks the date before storage. A transform that removes the value before storage. Local study-map skill 4.5 (Sensitive Data Redaction), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 4 (implementing observability practices and troubleshooting): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A sink suited to cheap long-term retention. Why the correct answer wins: The processor masks the date before storage.
- **B:** Incorrect for this question. A procedural promise with no enforcement. Why the correct answer wins: The processor masks the date before storage.
- **C:** Incorrect for this question. A filter that drops matching entries before storage. Why the correct answer wins: The processor masks the date before storage.
- **D:** Correct. A transform that removes the value before storage. In this case: The processor masks the date before storage.

### Question 73 — A, B

Answers: Ask Gemini Cloud Assist to summarise the failing entries; Ask Gemini Cloud Assist to explain the metric spike. The log summary explains entries, and the metric explanation explains the spike. An AI summary over the selected log range. An AI interpretation of the chart. Local study-map skill 4.6 (Gemini Cloud Assist for Log Analysis), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 4 (implementing observability practices and troubleshooting): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Correct. An AI summary over the selected log range. In this case: The log summary explains entries, and the metric explanation explains the spike.
- **B:** Correct. An AI interpretation of the chart. In this case: The log summary explains entries, and the metric explanation explains the spike.
- **C:** Incorrect for this question. A precise query over the stored entries. Why the correct answer wins: The log summary explains entries, and the metric explanation explains the spike.
- **D:** Incorrect for this question. A counter derived from matching entries. Why the correct answer wins: The log summary explains entries, and the metric explanation explains the spike.
- **E:** Incorrect for this question. An AI pointer to the expensive span. Why the correct answer wins: The log summary explains entries, and the metric explanation explains the spike.

### Question 74 — A

Answer: Scrape the workload with managed collection for Prometheus. Managed collection stores those metrics without a scrape server. A metrics store fed by a scrape endpoint. Local study-map skill 4.7 (Metrics Collection), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 4 (implementing observability practices and troubleshooting): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Correct. A metrics store fed by a scrape endpoint. In this case: Managed collection stores those metrics without a scrape server.
- **B:** Incorrect for this question. A measurement written by the application itself. Why the correct answer wins: Managed collection stores those metrics without a scrape server.
- **C:** Incorrect for this question. A counter derived from matching entries. Why the correct answer wins: Managed collection stores those metrics without a scrape server.
- **D:** Incorrect for this question. A probe that exercises the path from outside. Why the correct answer wins: Managed collection stores those metrics without a scrape server.

### Question 75 — B

Answer: Emit a custom metric for the business event. The service emits the wait time as a metric. A measurement written by the application itself. Local study-map skill 4.7 (Metrics Collection), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 4 (implementing observability practices and troubleshooting): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A probe that exercises the path from outside. Why the correct answer wins: The service emits the wait time as a metric.
- **B:** Correct. A measurement written by the application itself. In this case: The service emits the wait time as a metric.
- **C:** Incorrect for this question. A metrics store fed by a scrape endpoint. Why the correct answer wins: The service emits the wait time as a metric.
- **D:** Incorrect for this question. A counter derived from matching entries. Why the correct answer wins: The service emits the wait time as a metric.

### Question 76 — A

Answer: Create a log-based metric for the error string. The log metric counts the warning. A counter derived from matching entries. Local study-map skill 4.8 (Custom and Log-Based Metrics), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 4 (implementing observability practices and troubleshooting): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Correct. A counter derived from matching entries. In this case: The log metric counts the warning.
- **B:** Incorrect for this question. A metrics store fed by a scrape endpoint. Why the correct answer wins: The log metric counts the warning.
- **C:** Incorrect for this question. A probe that exercises the path from outside. Why the correct answer wins: The log metric counts the warning.
- **D:** Incorrect for this question. A measurement written by the application itself. Why the correct answer wins: The log metric counts the warning.

### Question 77 — C

Answer: Create an uptime check against the login flow. The uptime check probes it from outside. A probe that exercises the path from outside. Local study-map skill 4.9 (Synthetic Monitors), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 4 (implementing observability practices and troubleshooting): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A metrics store fed by a scrape endpoint. Why the correct answer wins: The uptime check probes it from outside.
- **B:** Incorrect for this question. A measurement written by the application itself. Why the correct answer wins: The uptime check probes it from outside.
- **C:** Correct. A probe that exercises the path from outside. In this case: The uptime check probes it from outside.
- **D:** Incorrect for this question. A counter derived from matching entries. Why the correct answer wins: The uptime check probes it from outside.

### Question 78 — C, D

Answers: Build one dashboard and share it with the on-call rotation; Attach the remediation playbook to the alert. The shared dashboard shows the signals, and the playbook shows the first step. A shared view of the signals that matter. A documented response beside the notification. Local study-map skill 4.10 (Metrics Explorer and Dashboards), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 4 (implementing observability practices and troubleshooting): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A static threshold on a resource metric. Why the correct answer wins: The shared dashboard shows the signals, and the playbook shows the first step.
- **B:** Incorrect for this question. A delivery route for the alert. Why the correct answer wins: The shared dashboard shows the signals, and the playbook shows the first step.
- **C:** Correct. A documented response beside the notification. In this case: The shared dashboard shows the signals, and the playbook shows the first step.
- **D:** Correct. A shared view of the signals that matter. In this case: The shared dashboard shows the signals, and the playbook shows the first step.
- **E:** Incorrect for this question. A third-party paging integration. Why the correct answer wins: The shared dashboard shows the signals, and the playbook shows the first step.

### Question 79 — A

Answer: Send the alert to PagerDuty through a webhook. The webhook notifies the paging tool first. A third-party paging integration. Local study-map skill 4.10 (Metrics Explorer and Dashboards), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 4 (implementing observability practices and troubleshooting): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Correct. A third-party paging integration. In this case: The webhook notifies the paging tool first.
- **B:** Incorrect for this question. A page driven by the objective instead of a raw threshold. Why the correct answer wins: The webhook notifies the paging tool first.
- **C:** Incorrect for this question. A documented response beside the notification. Why the correct answer wins: The webhook notifies the paging tool first.
- **D:** Incorrect for this question. A delivery route for the alert. Why the correct answer wins: The webhook notifies the paging tool first.

### Question 80 — D

Answer: Alert when CPU stays above ninety percent for ten minutes. The threshold does not reflect user harm. A static threshold on a resource metric. Local study-map skill 4.11 (Alerting Policies), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 4 (implementing observability practices and troubleshooting): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A page driven by the objective instead of a raw threshold. Why the correct answer wins: The threshold does not reflect user harm.
- **B:** Incorrect for this question. A documented response beside the notification. Why the correct answer wins: The threshold does not reflect user harm.
- **C:** Incorrect for this question. A third-party paging integration. Why the correct answer wins: The threshold does not reflect user harm.
- **D:** Correct. A static threshold on a resource metric. In this case: The threshold does not reflect user harm.

### Question 81 — C

Answer: Add an email notification channel for the on-call group. The email channel archives each alert. A delivery route for the alert. Local study-map skill 4.11 (Alerting Policies), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 4 (implementing observability practices and troubleshooting): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A third-party paging integration. Why the correct answer wins: The email channel archives each alert.
- **B:** Incorrect for this question. A documented response beside the notification. Why the correct answer wins: The email channel archives each alert.
- **C:** Correct. A delivery route for the alert. In this case: The email channel archives each alert.
- **D:** Incorrect for this question. A page driven by the objective instead of a raw threshold. Why the correct answer wins: The email channel archives each alert.

### Question 82 — B

Answer: Send the alert to PagerDuty through a webhook. The webhook posts the payload to that endpoint. A third-party paging integration. Local study-map skill 4.12 (Third-Party Alerting Integration), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 4 (implementing observability practices and troubleshooting): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A documented response beside the notification. Why the correct answer wins: The webhook posts the payload to that endpoint.
- **B:** Correct. A third-party paging integration. In this case: The webhook posts the payload to that endpoint.
- **C:** Incorrect for this question. A static threshold on a resource metric. Why the correct answer wins: The webhook posts the payload to that endpoint.
- **D:** Incorrect for this question. A delivery route for the alert. Why the correct answer wins: The webhook posts the payload to that endpoint.

### Question 83 — A

Answer: Instrument the service with OpenTelemetry spans. Spans report the duration of each call. Trace context emitted for each request. Local study-map skill 4.13 (Distributed Tracing with OpenTelemetry), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 4 (implementing observability practices and troubleshooting): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Correct. Trace context emitted for each request. In this case: Spans report the duration of each call.
- **B:** Incorrect for this question. A join key between traces and logs. Why the correct answer wins: Spans report the duration of each call.
- **C:** Incorrect for this question. A per-span timing view of one request. Why the correct answer wins: Spans report the duration of each call.
- **D:** Incorrect for this question. An AI pointer to the expensive span. Why the correct answer wins: Spans report the duration of each call.

### Question 84 — D

Answer: Put the trace ID in the structured log line. The trace ID in the alert links to the trace. A join key between traces and logs. Local study-map skill 4.13 (Distributed Tracing with OpenTelemetry), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 4 (implementing observability practices and troubleshooting): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A per-span timing view of one request. Why the correct answer wins: The trace ID in the alert links to the trace.
- **B:** Incorrect for this question. Trace context emitted for each request. Why the correct answer wins: The trace ID in the alert links to the trace.
- **C:** Incorrect for this question. No shared identifier between the two signals. Why the correct answer wins: The trace ID in the alert links to the trace.
- **D:** Correct. A join key between traces and logs. In this case: The trace ID in the alert links to the trace.

### Question 85 — D

Answer: Read the trace waterfall to find the slow span. The waterfall shows order and duration. A per-span timing view of one request. Local study-map skill 4.14 (Trace Analysis and Log Correlation), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 4 (implementing observability practices and troubleshooting): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A join key between traces and logs. Why the correct answer wins: The waterfall shows order and duration.
- **B:** Incorrect for this question. Trace context emitted for each request. Why the correct answer wins: The waterfall shows order and duration.
- **C:** Incorrect for this question. An AI pointer to the expensive span. Why the correct answer wins: The waterfall shows order and duration.
- **D:** Correct. A per-span timing view of one request. In this case: The waterfall shows order and duration.

### Question 86 — B

Answer: Inspect the image pull credential and repository permission. The pull credential for that namespace is wrong. The identity the node uses to fetch the image. Local study-map skill 4.15 (Infrastructure and Pipeline Troubleshooting), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 4 (implementing observability practices and troubleshooting): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. The rule that blocked the connection. Why the correct answer wins: The pull credential for that namespace is wrong.
- **B:** Correct. The identity the node uses to fetch the image. In this case: The pull credential for that namespace is wrong.
- **C:** Incorrect for this question. The limit that refused the resource. Why the correct answer wins: The pull credential for that namespace is wrong.
- **D:** Incorrect for this question. A shared egress resource that runs out of ports. Why the correct answer wins: The pull credential for that namespace is wrong.

### Question 87 — C, D

Answers: Profile the slow endpoint inside the application; Compare latency with the saturation metric. Profiling finds the slow code, and the saturation comparison explains the pool. A hotspot found on the request path. A queueing symptom traced to a full resource. Local study-map skill 4.16 (Application and Latency Troubleshooting), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 4 (implementing observability practices and troubleshooting): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A stale name that still points at the old address. Why the correct answer wins: Profiling finds the slow code, and the saturation comparison explains the pool.
- **B:** Incorrect for this question. A shared egress resource that runs out of ports. Why the correct answer wins: Profiling finds the slow code, and the saturation comparison explains the pool.
- **C:** Correct. A hotspot found on the request path. In this case: Profiling finds the slow code, and the saturation comparison explains the pool.
- **D:** Correct. A queueing symptom traced to a full resource. In this case: Profiling finds the slow code, and the saturation comparison explains the pool.
- **E:** Incorrect for this question. A probe that fails before the app is listening. Why the correct answer wins: Profiling finds the slow code, and the saturation comparison explains the pool.

### Question 88 — A

Answer: Compare the readiness probe with the application startup time. The probe may be checking the wrong port. A probe that fails before the app is listening. Local study-map skill 4.16 (Application and Latency Troubleshooting), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 4 (implementing observability practices and troubleshooting): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Correct. A probe that fails before the app is listening. In this case: The probe may be checking the wrong port.
- **B:** Incorrect for this question. A shared egress resource that runs out of ports. Why the correct answer wins: The probe may be checking the wrong port.
- **C:** Incorrect for this question. A stale name that still points at the old address. Why the correct answer wins: The probe may be checking the wrong port.
- **D:** Incorrect for this question. A hotspot found on the request path. Why the correct answer wins: The probe may be checking the wrong port.

### Question 89 — B

Answer: Measure request latency by endpoint in Cloud Monitoring. Per-endpoint latency is what ranks them by p95. An application-level view of response time. Local study-map skill 5.1 (Application Performance Monitoring), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 5 (optimizing performance and cost): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A recommendation aimed at spend. Why the correct answer wins: Per-endpoint latency is what ranks them by p95.
- **B:** Correct. An application-level view of response time. In this case: Per-endpoint latency is what ranks them by p95.
- **C:** Incorrect for this question. A queryable record of spend by label. Why the correct answer wins: Per-endpoint latency is what ranks them by p95.
- **D:** Incorrect for this question. A goal-oriented view of performance. Why the correct answer wins: Per-endpoint latency is what ranks them by p95.

### Question 90 — A

Answer: Track the service objective on a shared dashboard. The objective dashboard pairs goal and actual. A goal-oriented view of performance. Local study-map skill 5.1 (Application Performance Monitoring), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 5 (optimizing performance and cost): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Correct. A goal-oriented view of performance. In this case: The objective dashboard pairs goal and actual.
- **B:** Incorrect for this question. A cost estimate driven by actual ingest. Why the correct answer wins: The objective dashboard pairs goal and actual.
- **C:** Incorrect for this question. An application-level view of response time. Why the correct answer wins: The objective dashboard pairs goal and actual.
- **D:** Incorrect for this question. A recommendation aimed at spend. Why the correct answer wins: The objective dashboard pairs goal and actual.

### Question 91 — C

Answer: Review the Active Assist recommendations for the project. Active Assist lists the outstanding suggestions. Suggested changes generated from telemetry. Local study-map skill 5.2 (Active Assist and Recommenders), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 5 (optimizing performance and cost): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A queryable record of spend by label. Why the correct answer wins: Active Assist lists the outstanding suggestions.
- **B:** Incorrect for this question. A recommendation aimed at spend. Why the correct answer wins: Active Assist lists the outstanding suggestions.
- **C:** Correct. Suggested changes generated from telemetry. In this case: Active Assist lists the outstanding suggestions.
- **D:** Incorrect for this question. A recommendation aimed at resilience. Why the correct answer wins: Active Assist lists the outstanding suggestions.

### Question 92 — C

Answer: Apply the reliability recommender for the missing quota. The reliability recommender flags the headroom. A recommendation aimed at resilience. Local study-map skill 5.2 (Active Assist and Recommenders), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 5 (optimizing performance and cost): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Suggested changes generated from telemetry. Why the correct answer wins: The reliability recommender flags the headroom.
- **B:** Incorrect for this question. A recommendation aimed at spend. Why the correct answer wins: The reliability recommender flags the headroom.
- **C:** Correct. A recommendation aimed at resilience. In this case: The reliability recommender flags the headroom.
- **D:** Incorrect for this question. Discounted capacity that can be reclaimed. Why the correct answer wins: The reliability recommender flags the headroom.

### Question 93 — C, E

Answers: Exclude the debug stream and keep the error stream; Drop the high-cardinality user label from the metric. Excluding the debug stream cuts entries, and dropping the label cuts series. A reduction that preserves the useful signal. A label removal that cuts the stored series. Local study-map skill 5.3 (Observability Cost Management), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 5 (optimizing performance and cost): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A retention period that cannot be shortened. Why the correct answer wins: Excluding the debug stream cuts entries, and dropping the label cuts series.
- **B:** Incorrect for this question. A cheaper egress path with different performance. Why the correct answer wins: Excluding the debug stream cuts entries, and dropping the label cuts series.
- **C:** Correct. A label removal that cuts the stored series. In this case: Excluding the debug stream cuts entries, and dropping the label cuts series.
- **D:** Incorrect for this question. A cost estimate driven by actual ingest. Why the correct answer wins: Excluding the debug stream cuts entries, and dropping the label cuts series.
- **E:** Correct. A reduction that preserves the useful signal. In this case: Excluding the debug stream cuts entries, and dropping the label cuts series.

### Question 94 — D

Answer: Measure log volume per service before choosing a retention period. Measuring the volume is what projects the cost. A cost estimate driven by actual ingest. Local study-map skill 5.3 (Observability Cost Management), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 5 (optimizing performance and cost): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A reduction that preserves the useful signal. Why the correct answer wins: Measuring the volume is what projects the cost.
- **B:** Incorrect for this question. A retention period that cannot be shortened. Why the correct answer wins: Measuring the volume is what projects the cost.
- **C:** Incorrect for this question. A label removal that cuts the stored series. Why the correct answer wins: Measuring the volume is what projects the cost.
- **D:** Correct. A cost estimate driven by actual ingest. In this case: Measuring the volume is what projects the cost.

### Question 95 — D

Answer: Run the batch on Spot VMs. Spot capacity suits a transcoder that restarts. Discounted capacity that can be reclaimed. Local study-map skill 5.4 (Spot Virtual Machines), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 5 (optimizing performance and cost): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A multi-year commitment at a lower unit price. Why the correct answer wins: Spot capacity suits a transcoder that restarts.
- **B:** Incorrect for this question. A pool built from reclaimable capacity. Why the correct answer wins: Spot capacity suits a transcoder that restarts.
- **C:** Incorrect for this question. Reclaimable capacity under a stateful workload. Why the correct answer wins: Spot capacity suits a transcoder that restarts.
- **D:** Correct. Discounted capacity that can be reclaimed. In this case: Spot capacity suits a transcoder that restarts.

### Question 96 — B

Answer: Put the stateless workers on a Spot node pool. Spot nodes cut the largest compute line. A pool built from reclaimable capacity. Local study-map skill 5.4 (Spot Virtual Machines), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 5 (optimizing performance and cost): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A multi-year commitment at a lower unit price. Why the correct answer wins: Spot nodes cut the largest compute line.
- **B:** Correct. A pool built from reclaimable capacity. In this case: Spot nodes cut the largest compute line.
- **C:** Incorrect for this question. Discounted capacity that can be reclaimed. Why the correct answer wins: Spot nodes cut the largest compute line.
- **D:** Incorrect for this question. Reclaimable capacity under a stateful workload. Why the correct answer wins: Spot nodes cut the largest compute line.

### Question 97 — A, D

Answers: Buy a committed-use discount for the steady baseline; Keep the interactive traffic on the Premium tier. A commitment discounts the baseline, and the premium tier keeps traffic fast. A multi-year commitment at a lower unit price. A lower-latency path for user-facing traffic. Local study-map skill 5.5 (Infrastructure Cost Planning), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 5 (optimizing performance and cost): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Correct. A multi-year commitment at a lower unit price. In this case: A commitment discounts the baseline, and the premium tier keeps traffic fast.
- **B:** Incorrect for this question. A cheaper egress path with different performance. Why the correct answer wins: A commitment discounts the baseline, and the premium tier keeps traffic fast.
- **C:** Incorrect for this question. Discounted capacity that can be reclaimed. Why the correct answer wins: A commitment discounts the baseline, and the premium tier keeps traffic fast.
- **D:** Correct. A lower-latency path for user-facing traffic. In this case: A commitment discounts the baseline, and the premium tier keeps traffic fast.
- **E:** Incorrect for this question. An automatic discount that accrues with monthly use. Why the correct answer wins: A commitment discounts the baseline, and the premium tier keeps traffic fast.

### Question 98 — C

Answer: Serve the bulk export over the Standard network tier. The standard tier is cheaper for replication. A cheaper egress path with different performance. Local study-map skill 5.5 (Infrastructure Cost Planning), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 5 (optimizing performance and cost): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A pool built from reclaimable capacity. Why the correct answer wins: The standard tier is cheaper for replication.
- **B:** Incorrect for this question. A multi-year commitment at a lower unit price. Why the correct answer wins: The standard tier is cheaper for replication.
- **C:** Correct. A cheaper egress path with different performance. In this case: The standard tier is cheaper for replication.
- **D:** Incorrect for this question. A lower-latency path for user-facing traffic. Why the correct answer wins: The standard tier is cheaper for replication.

### Question 99 — B

Answer: Right-size the node pool from the observed requests. Right-sizing the pool removes the unused reservation. A pool sized against measured demand. Local study-map skill 5.6 (Workload-Level Cost Optimization), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 5 (optimizing performance and cost): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Warm capacity that avoids cold starts. Why the correct answer wins: Right-sizing the pool removes the unused reservation.
- **B:** Correct. A pool sized against measured demand. In this case: Right-sizing the pool removes the unused reservation.
- **C:** Incorrect for this question. Scale to zero for a service nobody uses at night. Why the correct answer wins: Right-sizing the pool removes the unused reservation.
- **D:** Incorrect for this question. A pool built from reclaimable capacity. Why the correct answer wins: Right-sizing the pool removes the unused reservation.

### Question 100 — D

Answer: Set a minimum instance count for the latency-critical service. A warm minimum prevents cold starts. Warm capacity that avoids cold starts. Local study-map skill 5.6 (Workload-Level Cost Optimization), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 5 (optimizing performance and cost): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Scale to zero for a service nobody uses at night. Why the correct answer wins: A warm minimum prevents cold starts.
- **B:** Incorrect for this question. A pool sized against measured demand. Why the correct answer wins: A warm minimum prevents cold starts.
- **C:** Incorrect for this question. A calendar action that removes idle spend. Why the correct answer wins: A warm minimum prevents cold starts.
- **D:** Correct. Warm capacity that avoids cold starts. In this case: A warm minimum prevents cold starts.
