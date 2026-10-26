# Google Cloud Professional Cloud DevOps Engineer — Full-Length Mock Exam 6

Professional Cloud DevOps Engineer · 100 questions · expanded practice bank · passing score not published

Blueprint-weighted mock exam. Item mix: 84 multiple-choice and 16 multiple-select items (the selection count is stated in each multi-select stem). The live exam publishes 50-60 multiple-choice and multiple-select questions and has no case-study component, so this set is larger on purpose and no case-study item is reproduced. The live paper allows two hours for 50-60 items, so this 100-item set is a slower-per-item rehearsal: about 72 seconds per item here against roughly 120-144 seconds live. Use it to build a habit of finishing with time to review. See the README for the exact fidelity boundary.

Original educational content, not actual, recalled, or copied Google exam items.

## Questions

---

## Domain 1 — Bootstrapping and Maintaining a Google Cloud Organization (Hierarchy, Infrastructure as Code, and Pipeline Foundations)

### 1. A holding company wants each brand's projects under one governed branch, separate from its siblings. What fits?

- A. Add an IAM deny policy for the sensitive permission
- B. Apply the constraint separately in each project
- C. Apply the constraint at the organization node
- D. Apply the constraint to the business unit folder

### 2. A policy must already apply to subsidiaries that do not exist yet. Where does it belong?

- A. Apply the constraint to the business unit folder
- B. Apply the constraint separately in each project
- C. Apply the constraint at the organization node
- D. Add an IAM deny policy for the sensitive permission

### 3. A new team must inherit the approved network rather than build one. What fits?

- A. Create a Shared VPC host project and attach the service projects
- B. Publish the service behind a Private Service Connect endpoint
- C. Peer every project VPC with every other project VPC
- D. Give each project its own VPC and Cloud NAT

### 4. A partner must reach one service privately without seeing the rest of the network. What fits?

- A. Give each project its own VPC and Cloud NAT
- B. Publish the service behind a Private Service Connect endpoint
- C. Create a Shared VPC host project and attach the service projects
- D. Peer every project VPC with every other project VPC

### 5. A forensic review must search one place for entries from every project. What should be configured?

- A. Add the projects to one metrics scope
- B. Route the entries to a Pub/Sub topic
- C. Keep one log bucket inside each project
- D. Route every project log to one aggregated sink

### 6. An auditor requires that a specific permission cannot be granted even temporarily. What should be added?

- A. Enforce the restriction with an organization policy constraint
- B. Grant a custom role limited to the required permissions
- C. Grant a predefined role once at the folder
- D. Add an IAM deny policy for the sensitive permission

### 7. A job needs four permissions while the closest predefined role carries thirty. What should be created?

- A. Add an IAM deny policy for the sensitive permission
- B. Grant a predefined role once at the folder
- C. Enforce the restriction with an organization policy constraint
- D. Grant a custom role limited to the required permissions

### 8. A staging identity must not act in production, and engineers must not download keys to act as the deployer. Which two practices apply? Select two.

- A. Create one service account per environment
- B. Download a JSON key file for the service account
- C. Let the workload use the default Compute Engine service account
- D. Grant impersonation of the service account instead of a key
- E. Create one service account per workload

### 9. A contract names the country and forbids processing anywhere else. What governs the deployment?

- A. Create a Shared VPC host project and attach the service projects
- B. Place the resources in a region that satisfies the residency rule
- C. Replicate the data to a second region
- D. Apply the constraint at the organization node

### 10. A network pattern must be reused by teams that cannot read each other's code. What fits?

- A. Package the workload as a Helm chart
- B. Apply the deployment through Infrastructure Manager
- C. Reconcile the resources with Config Connector
- D. Define the estate as Terraform modules held in version control

### 11. Applied changes must show who ran them and what the state became. What fits?

- A. Define the estate as Terraform modules held in version control
- B. Automate the repeated step with a Python script calling the API
- C. Reconcile the resources with Config Connector
- D. Apply the deployment through Infrastructure Manager

### 12. The estate must be compared with its code on a schedule, and a new landing zone must start from a vetted blueprint. Which two practices apply? Select two.

- A. Run the documented gcloud commands by hand for each environment
- B. Schedule a plan that reports drift
- C. Start from the Cloud Foundation Toolkit blueprints
- D. Automate the repeated step with a Python script calling the API
- E. Make the change in the console and note it in the wiki

### 13. A cleanup task must run every night and report what it changed. What should be written?

- A. Automate the repeated step with a Python script calling the API
- B. Run the documented gcloud commands by hand for each environment
- C. Make the change in the console and note it in the wiki
- D. Schedule a plan that reports drift

### 14. An auditor wants a release reproduced from the exact commit that was tagged. What should be configured?

- A. Create a Cloud Build trigger on the release branch
- B. Trigger the pipeline only on a signed tag
- C. Have an engineer build locally and upload the result
- D. Create a trigger that runs the tests on every pull request

### 15. A change must move from build through staging to production under one release record. What fits?

- A. Run Jenkins on a self-managed VM
- B. Use Cloud Build for CI and Cloud Deploy for delivery
- C. Let Argo CD pull the manifests from Git
- D. Bake the machine image with Packer

### 16. The cluster must reconcile from Git without a push credential, and every environment must boot from one signed image. Which two practices apply? Select two.

- A. Run Jenkins on a self-managed VM
- B. Bake the machine image with Packer
- C. Use Cloud Build for CI and Cloud Deploy for delivery
- D. Render the manifests through a kpt function pipeline
- E. Let Argo CD pull the manifests from Git

### 17. A change needs a full environment for four hours and then nothing. What fits?

- A. Keep one shared staging environment for every team
- B. Bake the environment settings into the image
- C. Create a short-lived project per change and delete it after review
- D. Keep one base with a Kustomize overlay per environment

### 18. Upgrades must land after the change freeze, inside a monthly window. What should be configured?

- A. Stand up a second cluster and shift traffic after verification
- B. Put the cluster on a release channel with a maintenance window
- C. Upgrade each node pool by hand whenever an operator is free
- D. Create a short-lived project per change and delete it after review

### 19. An auditor must confirm that code never leaves the project boundary and needs no local setup. What fits?

- A. Let each developer install the tools locally
- B. Give developers Cloud Workstations built from a custom image
- C. Rely on Cloud Shell for every developer
- D. Build a custom image that carries the approved toolchain

### 20. An engineer wants a long command explained before it is allowed to run. What fits?

- A. Let each developer install the tools locally
- B. Ask Gemini Cloud Assist to explain the resource state
- C. Use Gemini CLI for the repetitive script
- D. Use Gemini Code Assist for the suggested change

---

## Domain 2 — Building and Implementing CI/CD Pipelines (Delivery Pipelines and Software Supply Chain)

### 21. Every merge on main must rebuild, and every pull request must run the checks first. Which two triggers apply? Select two.

- A. Create a trigger that runs the tests on every pull request
- B. Have an engineer build locally and upload the result
- C. Create a Cloud Build trigger on the release branch
- D. Add a Cloud Deploy approval gate before production
- E. Trigger the pipeline only on a signed tag

### 22. A signed tag is the only acceptable origin for a customer release. What should be configured?

- A. Trigger the pipeline only on a signed tag
- B. Create a trigger that runs the tests on every pull request
- C. Create a Cloud Build trigger on the release branch
- D. Read Cloud Audit Logs for the release history

### 23. The release cannot be rebuilt because the only machine that produced it was decommissioned. What caused that?

- A. Create a trigger that runs the tests on every pull request
- B. Trigger the pipeline only on a signed tag
- C. Read Cloud Audit Logs for the release history
- D. Have an engineer build locally and upload the result

### 24. A rebuild of the same version must be impossible rather than merely discouraged. What provides that?

- A. Store the build output in Artifact Registry
- B. Inspect the build provenance attestation
- C. Tag each artifact with the commit SHA and forbid overwrite
- D. Reuse the latest tag for every build

### 25. A cleanup policy must remove untagged images from one region automatically. What fits?

- A. Reuse the latest tag for every build
- B. Push the image to Container Registry
- C. Store the build output in Artifact Registry
- D. Tag each artifact with the commit SHA and forbid overwrite

### 26. A cluster in another provider must receive releases from the same pipeline. What fits?

- A. Use a GKE cluster in the pipeline project as the target
- B. Deliver to a Cloud Run service revision
- C. Define the attached cluster as the delivery target
- D. Add a Cloud Deploy approval gate before production

### 27. A cluster in the pipeline project must receive the release with no registration step. What fits?

- A. Define the attached cluster as the delivery target
- B. Use a GKE cluster in the pipeline project as the target
- C. Read Cloud Audit Logs for the release history
- D. Deliver to a Cloud Run service revision

### 28. A regulated target needs a named approver, and the sandbox target must promote without a human. Which two settings apply? Select two.

- A. Promote automatically to every target in the chain
- B. Read Cloud Audit Logs for the release history
- C. Have an engineer build locally and upload the result
- D. Roll the release back to the previous one
- E. Add a Cloud Deploy approval gate before production

### 29. An investigator wants the identity behind a particular promotion. What answers that?

- A. Inspect the build provenance attestation
- B. Describe the build with its supply chain level and signed provenance
- C. Read Cloud Audit Logs for the release history
- D. Tag each artifact with the commit SHA and forbid overwrite

### 30. A customer asks which framework level describes how the artifact was built. What answers that?

- A. Read Cloud Audit Logs for the release history
- B. Describe the build with its supply chain level and signed provenance
- C. Issue and rotate the certificate with Certificate Manager
- D. Inspect the build provenance attestation

### 31. A change must be limited to one region for a day before it spreads further. What fits?

- A. Send ten percent of traffic to the new revision and watch the SLI
- B. Run the new version alongside and switch traffic at once
- C. Stop the old version and then start the new one
- D. Replace the instances in batches

### 32. Ten instances must be replaced two at a time without an outage. What fits?

- A. Replace the instances in batches
- B. Send ten percent of traffic to the new revision and watch the SLI
- C. Stop the old version and then start the new one
- D. Run the new version alongside and switch traffic at once

### 33. A risky pricing rule must ship dark and be enabled per account. What fits?

- A. Run the new version alongside and switch traffic at once
- B. Stop the old version and then start the new one
- C. Put the behaviour behind a feature flag
- D. Send ten percent of traffic to the new revision and watch the SLI

### 34. A rollout must be judged by the objective, so the objective itself must exist first. Which two are needed? Select two.

- A. Set an internal target on that indicator
- B. Add a Cloud Deploy approval gate before production
- C. Create an uptime check against the login flow
- D. Gate the rollout on average CPU alone
- E. Gate the rollout on the error-rate SLI

### 35. A release breaks a downstream consumer although its own health checks pass. What is the first action?

- A. Start from the failed step log in Cloud Build
- B. Make the failed step idempotent and re-run it
- C. Roll the release back to the previous one
- D. Patch production by hand and reconcile later

### 36. The failing step and the command it ran must be identified at a glance. What supplies that?

- A. Start from the failed step log in Cloud Build
- B. Read Cloud Audit Logs for the release history
- C. Make the failed step idempotent and re-run it
- D. Roll the release back to the previous one

### 37. A key must be rotated and every use must be visible to audit. What fits?

- A. Issue and rotate the certificate with Certificate Manager
- B. Encrypt the payload with a Cloud KMS key
- C. Commit the credential to the private repository
- D. Store the credential in Secret Manager with versions

### 38. Certificates must be reissued before expiry without a ticket. What fits?

- A. Store the credential in Secret Manager with versions
- B. Keep the non-secret configuration in Parameter Manager
- C. Encrypt the payload with a Cloud KMS key
- D. Issue and rotate the certificate with Certificate Manager

### 39. A token must be rotated without a redeploy and with an audit trail. What fits?

- A. Pass the secret as a build argument
- B. Keep the non-secret configuration in Parameter Manager
- C. Commit the credential to the private repository
- D. Store the credential in Secret Manager with versions

### 40. Reviewers must see the current limits before the deploy begins. What fits?

- A. Commit the credential to the private repository
- B. Store the credential in Secret Manager with versions
- C. Keep the non-secret configuration in Parameter Manager
- D. Bake the environment settings into the image

### 41. A registry pull secret must never be baked into an artifact that contractors can download. What fits?

- A. Inject the secret at build time into the image layer
- B. Commit the credential to the private repository
- C. Pass the secret as a build argument
- D. Mount the secret at runtime from Secret Manager

### 42. A critical finding must stop the release rather than be reported. What should be configured?

- A. Fail the pipeline on a critical vulnerability finding
- B. Keep the scan report for the monthly review
- C. Enforce Binary Authorization attestations before deploy
- D. Enable Artifact Analysis scanning on the repository

### 43. Only images signed by the approved builder may start in the cluster. What fits?

- A. Fail the pipeline on a critical vulnerability finding
- B. Enforce Binary Authorization attestations before deploy
- C. Enable Artifact Analysis scanning on the repository
- D. Bind deploy permissions only inside the production project

### 44. Every stored image needs a current vulnerability list. What provides that?

- A. Enable Artifact Analysis scanning on the repository
- B. Enforce Binary Authorization attestations before deploy
- C. Keep the scan report for the monthly review
- D. Fail the pipeline on a critical vulnerability finding

### 45. Each environment needs its own deploy identity, and one specific grant must be impossible everywhere. Which two controls apply? Select two.

- A. Download a JSON key file for the service account
- B. Add an IAM deny policy for the sensitive permission
- C. Run the pipeline as the default editor service account
- D. Bind deploy permissions only inside the production project
- E. Use one identity with deploy rights in every environment

---

## Domain 3 — Applying Site Reliability Engineering Practices (Reliability Engineering in Practice)

### 46. The contract must promise something measurable, so the measurement must exist first. Which two elements are those? Select two.

- A. Alert on a fast error-budget burn rate
- B. Publish a contractual promise with a remedy
- C. Track the ratio of good requests to total requests
- D. Choose three nines and spend the difference on features
- E. Set an internal target on that indicator

### 47. The team sets a bar stricter than the contract so breaches surface early. What is that bar?

- A. Publish a contractual promise with a remedy
- B. Alert on a fast error-budget burn rate
- C. Set an internal target on that indicator
- D. Track the ratio of good requests to total requests

### 48. A weekly release cadence is worth more than the next nine to this team. What follows?

- A. Assume five nines for every service
- B. Choose three nines and spend the difference on features
- C. Register the service in the service catalog
- D. Publish a contractual promise with a remedy

### 49. A page must fire on a fast burn, and a target the team can afford must be chosen. Which two practices apply? Select two.

- A. Choose three nines and spend the difference on features
- B. Assume five nines for every service
- C. Alert on a fast error-budget burn rate
- D. Publish a contractual promise with a remedy
- E. Stop feature releases when the error budget is spent

### 50. The allowance is spent, so launches pause for the rest of the quarter. What enforces that?

- A. Stop feature releases when the error budget is spent
- B. Alert on a fast error-budget burn rate
- C. Publish a contractual promise with a remedy
- D. Assume five nines for every service

### 51. One availability target is copied from the payments API to an internal wiki service. What is the flaw?

- A. Assume five nines for every service
- B. Choose three nines and spend the difference on features
- C. Request a quota increase and reserve capacity before the launch
- D. Publish a contractual promise with a remedy

### 52. The team decides the next nine is not worth the features it would delay. What follows?

- A. Publish a contractual promise with a remedy
- B. Register the service in the service catalog
- C. Assume five nines for every service
- D. Choose three nines and spend the difference on features

### 53. Nobody can say who owns the service that pages at night. What should exist?

- A. Announce the retirement date and withdraw traffic gradually
- B. Leave the unused service running for now
- C. Request a quota increase and reserve capacity before the launch
- D. Register the service in the service catalog

### 54. An old endpoint must stop answering on a published date. What should be planned?

- A. Leave the unused service running for now
- B. Add capacity in a second region
- C. Register the service in the service catalog
- D. Announce the retirement date and withdraw traffic gradually

### 55. A launch needs capacity approved before the campaign begins. What should be arranged?

- A. Schedule the batch with Dynamic Workload Scheduler
- B. Add capacity on a fixed calendar schedule
- C. Request a quota increase and reserve capacity before the launch
- D. Assume the default quota will absorb the launch

### 56. The launch assumed the default limit would be enough and stalled on day one. What was the mistake?

- A. Add capacity on a fixed calendar schedule
- B. Schedule the batch with Dynamic Workload Scheduler
- C. Assume the default quota will absorb the launch
- D. Request a quota increase and reserve capacity before the launch

### 57. A message backlog must add workers, and simultaneous requests must add instances. Which two signals apply? Select two.

- A. Scale on queue depth with a horizontal pod autoscaler
- B. Schedule the batch with Dynamic Workload Scheduler
- C. Set Cloud Run concurrency so replicas follow load
- D. Put the instance group behind an autoscaler on CPU
- E. Add capacity on a fixed calendar schedule

### 58. Capacity rises every Monday regardless of the demand curve. What is the flaw?

- A. Set Cloud Run concurrency so replicas follow load
- B. Scale on queue depth with a horizontal pod autoscaler
- C. Add capacity on a fixed calendar schedule
- D. Put the instance group behind an autoscaler on CPU

### 59. A rolling upgrade must not fail the requests already in flight. What must happen first?

- A. Shift traffic with a DNS routing policy
- B. Drain connections before removing the instance
- C. Add capacity in a second region
- D. Use a load balancer failover backend

### 60. A regional shortage needs supply elsewhere within minutes. What should be done?

- A. Drain connections before removing the instance
- B. Shift traffic with a DNS routing policy
- C. Add capacity in a second region
- D. Use a load balancer failover backend

### 61. A failed backend must stop receiving traffic automatically. What fits?

- A. Request a quota increase and reserve capacity before the launch
- B. Drain connections before removing the instance
- C. Shift traffic with a DNS routing policy
- D. Use a load balancer failover backend

### 62. A canary shows errors and the previous build is healthy. What is the fastest safe action?

- A. Reverse the schema change with a tested down migration
- B. Wait for the error rate to settle on its own
- C. Patch production by hand and reconcile later
- D. Redeploy the previous image to the affected service

### 63. Dropping a column broke the nightly export and the change had no reverse path. What was missing?

- A. Wait for the error rate to settle on its own
- B. Redeploy the previous image to the affected service
- C. Reverse the schema change with a tested down migration
- D. Patch production by hand and reconcile later

---

## Domain 4 — Implementing Observability Practices and Troubleshooting (Telemetry, Alerting, and Diagnosis)

### 64. VM memory pressure must be collected without a third-party agent. What fits?

- A. Run an OpenTelemetry Collector in the cluster
- B. Install the Ops Agent on the instances
- C. Turn on VPC Flow Logs for the subnet
- D. Read the Cloud Service Mesh telemetry

### 65. A regulator asks which identity read a patient record. What provides that?

- A. Read the Cloud Service Mesh telemetry
- B. Enable Data Access audit logs for the service
- C. Install the Ops Agent on the instances
- D. Turn on VPC Flow Logs for the subnet

### 66. Half the stored entries are repeated debug lines and errors must stay complete. What should be done?

- A. Sample the high-volume debug entries
- B. Add an exclusion for the health-check entries
- C. Drop the high-cardinality user label from the metric
- D. Measure log volume per service before choosing a retention period

### 67. A retention change must be costed before anyone approves it. What should be done first?

- A. Add an exclusion for the health-check entries
- B. Sample the high-volume debug entries
- C. Set the log bucket retention and lock it
- D. Measure log volume per service before choosing a retention period

### 68. An existing error string must become countable, and the entries around one occurrence must be inspected. Which two capabilities apply? Select two.

- A. Create an uptime check against the login flow
- B. Route the entries to a Cloud Storage bucket
- C. Filter with the Logging query language on the resource label
- D. Open the Logs Explorer and pivot from the error entry
- E. Create a log-based metric for the error string

### 69. Only entries from one namespace and one severity matter. What should be used?

- A. Create a log-based metric for the error string
- B. Open the Logs Explorer and pivot from the error entry
- C. Route the entries to a Cloud Storage bucket
- D. Filter with the Logging query language on the resource label

### 70. An auditor wants old entries retrievable but almost never queried. What fits?

- A. Set the log bucket retention and lock it
- B. Route the entries to a Cloud Storage bucket
- C. Route the entries to a BigQuery dataset
- D. Route the entries to a Pub/Sub topic

### 71. An administrator must not be able to shorten the retention period. What fits?

- A. Measure log volume per service before choosing a retention period
- B. Set the log bucket retention and lock it
- C. Route the entries to a Cloud Storage bucket
- D. Route the entries to a BigQuery dataset

### 72. Card numbers appear in entries that support pastes into tickets. What should be configured?

- A. Add an exclusion for the health-check entries
- B. Ask analysts not to read the sensitive field
- C. Redact the email field with a log processor
- D. Route the entries to a Cloud Storage bucket

### 73. A reviewer wants the dominant span named rather than plotted. What fits?

- A. Ask Gemini Cloud Assist which span dominates the trace
- B. Ask Gemini Cloud Assist to summarise the failing entries
- C. Read the trace waterfall to find the slow span
- D. Ask Gemini Cloud Assist to explain the metric spike

### 74. The service must publish its own queue wait time. What should it do?

- A. Emit a custom metric for the business event
- B. Create a log-based metric for the error string
- C. Scrape the workload with managed collection for Prometheus
- D. Create an uptime check against the login flow

### 75. Traces must be forwarded to two vendors without a code change. What fits?

- A. Install the Ops Agent on the instances
- B. Read the Cloud Service Mesh telemetry
- C. Turn on VPC Flow Logs for the subnet
- D. Run an OpenTelemetry Collector in the cluster

### 76. An existing Prometheus endpoint must be stored without a scrape server, and an existing log string must become countable. Which two capabilities apply? Select two.

- A. Build one dashboard and share it with the on-call rotation
- B. Create a log-based metric for the error string
- C. Emit a custom metric for the business event
- D. Create an uptime check against the login flow
- E. Scrape the workload with managed collection for Prometheus

### 77. A certificate renewal may fail silently, so something outside the project must notice. What fits?

- A. Create an uptime check against the login flow
- B. Create a log-based metric for the error string
- C. Emit a custom metric for the business event
- D. Scrape the workload with managed collection for Prometheus

### 78. Every responder must open the same view of the signals. What should be built?

- A. Attach the remediation playbook to the alert
- B. Alert when CPU stays above ninety percent for ten minutes
- C. Send the alert to PagerDuty through a webhook
- D. Build one dashboard and share it with the on-call rotation

### 79. The first remediation step must appear with the alert itself. What fits?

- A. Build one dashboard and share it with the on-call rotation
- B. Add an email notification channel for the on-call group
- C. Attach the remediation playbook to the alert
- D. Create an alerting policy on the SLO burn rate

### 80. A page must fire when the objective will be missed within two days. What fits?

- A. Alert when CPU stays above ninety percent for ten minutes
- B. Send the alert to PagerDuty through a webhook
- C. Attach the remediation playbook to the alert
- D. Create an alerting policy on the SLO burn rate

### 81. A page fires nightly for a busy batch host and is always ignored. What is the flaw?

- A. Create an uptime check against the login flow
- B. Create an alerting policy on the SLO burn rate
- C. Add an email notification channel for the on-call group
- D. Alert when CPU stays above ninety percent for ten minutes

### 82. The incident tool must be told automatically, and the audit team needs a copy by mail. Which two channels apply? Select two.

- A. Attach the remediation playbook to the alert
- B. Add an email notification channel for the on-call group
- C. Create an uptime check against the login flow
- D. Alert when CPU stays above ninety percent for ten minutes
- E. Send the alert to PagerDuty through a webhook

### 83. A log line must lead to its trace, and the slow span inside that trace must be visible. Which two capabilities apply? Select two.

- A. Read the trace waterfall to find the slow span
- B. Ask Gemini Cloud Assist which span dominates the trace
- C. Put the trace ID in the structured log line
- D. Instrument the service with OpenTelemetry spans
- E. Log a timestamp and correlate by eye later

### 84. A client library must report the duration of each downstream call. What fits?

- A. Put the trace ID in the structured log line
- B. Ask Gemini Cloud Assist which span dominates the trace
- C. Instrument the service with OpenTelemetry spans
- D. Read the trace waterfall to find the slow span

### 85. An engineer matches logs to traces by eyeballing timestamps and picks the wrong request. Why does that fail?

- A. Instrument the service with OpenTelemetry spans
- B. Put the trace ID in the structured log line
- C. Log a timestamp and correlate by eye later
- D. Read the trace waterfall to find the slow span

### 86. Egress fails intermittently from one node pool under load. What should be checked?

- A. Read the firewall rule that hit the denied flow
- B. Check Cloud NAT port exhaustion for the egress range
- C. Check the quota error in the deployment log
- D. Inspect the image pull credential and repository permission

### 87. A pod restarts before it ever serves a single request. What should be checked?

- A. Compare the readiness probe with the application startup time
- B. Check the DNS record and its remaining TTL
- C. Profile the slow endpoint inside the application
- D. Check Cloud NAT port exhaustion for the egress range

### 88. Latency rises whenever the connection pool is full. What analysis explains that?

- A. Instrument the service with OpenTelemetry spans
- B. Compare latency with the saturation metric
- C. Read the trace waterfall to find the slow span
- D. Put the trace ID in the structured log line

---

## Domain 5 — Optimizing Performance and Cost (FinOps and Performance Tuning)

### 89. A quarterly business review needs the reliability picture per service on one page. What fits?

- A. Measure log volume per service before choosing a retention period
- B. Track the service objective on a shared dashboard
- C. Apply the cost recommender suggestion for the idle disks
- D. Measure request latency by endpoint in Cloud Monitoring

### 90. Last week's release is suspected of harming one customer journey. What should be inspected?

- A. Measure request latency by endpoint in Cloud Monitoring
- B. Apply the cost recommender suggestion for the idle disks
- C. Export billing data to BigQuery for the chargeback report
- D. Track the service objective on a shared dashboard

### 91. The team wants the full list of suggestions, and one suggestion concerns headroom that a peak keeps exhausting. Which two should be used? Select two.

- A. Export billing data to BigQuery for the chargeback report
- B. Apply the reliability recommender for the missing quota
- C. Review the Active Assist recommendations for the project
- D. Run the batch on Spot VMs
- E. Apply the cost recommender suggestion for the idle disks

### 92. Half the address reservations are unused and still billed. Which recommendation applies?

- A. Apply the cost recommender suggestion for the idle disks
- B. Apply the reliability recommender for the missing quota
- C. Review the Active Assist recommendations for the project
- D. Run the batch on Spot VMs

### 93. Debug output dominates ingest and nobody reads it. What should be done?

- A. Exclude the debug stream and keep the error stream
- B. Set the log bucket retention and lock it
- C. Measure log volume per service before choosing a retention period
- D. Drop the high-cardinality user label from the metric

### 94. A request identifier label triples the stored series. What caused that?

- A. Serve the bulk export over the Standard network tier
- B. Drop the high-cardinality user label from the metric
- C. Exclude the debug stream and keep the error stream
- D. Measure log volume per service before choosing a retention period

### 95. A stateless consumer pool and a rendering farm both tolerate interruption. Which two placements apply? Select two.

- A. Move the primary database onto Spot capacity
- B. Run the batch on Spot VMs
- C. Buy a committed-use discount for the steady baseline
- D. Put the stateless workers on a Spot node pool
- E. Set a minimum instance count for the latency-critical service

### 96. A design puts the transactional write primary on reclaimable capacity. What is the risk?

- A. Run the batch on Spot VMs
- B. Buy a committed-use discount for the steady baseline
- C. Move the primary database onto Spot capacity
- D. Put the stateless workers on a Spot node pool

### 97. A predictable three-year baseline should carry a discount. What fits?

- A. Serve the bulk export over the Standard network tier
- B. Buy a committed-use discount for the steady baseline
- C. Rely on sustained-use discounts for the steady baseline
- D. Run the batch on Spot VMs

### 98. A nightly backup copy may take longer if it costs less. What fits?

- A. Serve the bulk export over the Standard network tier
- B. Put the stateless workers on a Spot node pool
- C. Keep the interactive traffic on the Premium tier
- D. Buy a committed-use discount for the steady baseline

### 99. A tool nobody uses after six must not bill overnight. What fits?

- A. Keep the minimum instance count at zero for the internal tool
- B. Stop the idle non-production instances on a schedule
- C. Right-size the node pool from the observed requests
- D. Set a minimum instance count for the latency-critical service

### 100. Development hosts run all weekend with no users. What should be done?

- A. Stop the idle non-production instances on a schedule
- B. Right-size the node pool from the observed requests
- C. Buy a committed-use discount for the steady baseline
- D. Keep the minimum instance count at zero for the internal tool

---

## Answer key and explanations

### Question 1 — D

Answer: Apply the constraint to the business unit folder. A folder gives each brand its own governed branch. A constraint attached to one folder and inherited by its projects. Local study-map skill 1.1 (Resource Hierarchy and Project Organization), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 1 (bootstrapping and maintaining a Google Cloud organization): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. An explicit denial that overrides any allow. Why the correct answer wins: A folder gives each brand its own governed branch.
- **B:** Incorrect for this question. A constraint set per project with no inheritance. Why the correct answer wins: A folder gives each brand its own governed branch.
- **C:** Incorrect for this question. An organization-level constraint that every folder and project inherits. Why the correct answer wins: A folder gives each brand its own governed branch.
- **D:** Correct. A constraint attached to one folder and inherited by its projects. In this case: A folder gives each brand its own governed branch.

### Question 2 — C

Answer: Apply the constraint at the organization node. The organization node covers projects that do not exist yet. An organization-level constraint that every folder and project inherits. Local study-map skill 1.1 (Resource Hierarchy and Project Organization), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 1 (bootstrapping and maintaining a Google Cloud organization): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A constraint attached to one folder and inherited by its projects. Why the correct answer wins: The organization node covers projects that do not exist yet.
- **B:** Incorrect for this question. A constraint set per project with no inheritance. Why the correct answer wins: The organization node covers projects that do not exist yet.
- **C:** Correct. An organization-level constraint that every folder and project inherits. In this case: The organization node covers projects that do not exist yet.
- **D:** Incorrect for this question. An explicit denial that overrides any allow. Why the correct answer wins: The organization node covers projects that do not exist yet.

### Question 3 — A

Answer: Create a Shared VPC host project and attach the service projects. Attaching to the host project inherits the approved network. A central network project that lends subnets to other projects. Local study-map skill 1.2 (Shared Networking for Multi-Project Estates), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 1 (bootstrapping and maintaining a Google Cloud organization): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Correct. A central network project that lends subnets to other projects. In this case: Attaching to the host project inherits the approved network.
- **B:** Incorrect for this question. A private endpoint that consumes a published service. Why the correct answer wins: Attaching to the host project inherits the approved network.
- **C:** Incorrect for this question. A mesh of peering links that grows with each new project. Why the correct answer wins: Attaching to the host project inherits the approved network.
- **D:** Incorrect for this question. Duplicate networks with a separately managed egress path. Why the correct answer wins: Attaching to the host project inherits the approved network.

### Question 4 — B

Answer: Publish the service behind a Private Service Connect endpoint. A published endpoint exposes only that service. A private endpoint that consumes a published service. Local study-map skill 1.2 (Shared Networking for Multi-Project Estates), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 1 (bootstrapping and maintaining a Google Cloud organization): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Duplicate networks with a separately managed egress path. Why the correct answer wins: A published endpoint exposes only that service.
- **B:** Correct. A private endpoint that consumes a published service. In this case: A published endpoint exposes only that service.
- **C:** Incorrect for this question. A central network project that lends subnets to other projects. Why the correct answer wins: A published endpoint exposes only that service.
- **D:** Incorrect for this question. A mesh of peering links that grows with each new project. Why the correct answer wins: A published endpoint exposes only that service.

### Question 5 — D

Answer: Route every project log to one aggregated sink. One aggregated destination holds every project's entries. A single destination that collects entries from many projects. Local study-map skill 1.3 (Multi-Project Monitoring and Logging), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 1 (bootstrapping and maintaining a Google Cloud organization): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. An observability scope that spans several projects. Why the correct answer wins: One aggregated destination holds every project's entries.
- **B:** Incorrect for this question. A sink that streams entries to another consumer. Why the correct answer wins: One aggregated destination holds every project's entries.
- **C:** Incorrect for this question. Log storage scoped to the project that produced the entries. Why the correct answer wins: One aggregated destination holds every project's entries.
- **D:** Correct. A single destination that collects entries from many projects. In this case: One aggregated destination holds every project's entries.

### Question 6 — D

Answer: Add an IAM deny policy for the sensitive permission. The deny policy blocks the grant even temporarily. An explicit denial that overrides any allow. Local study-map skill 1.4 (IAM Roles and Organization Policies), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 1 (bootstrapping and maintaining a Google Cloud organization): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A guardrail that holds regardless of the IAM grants. Why the correct answer wins: The deny policy blocks the grant even temporarily.
- **B:** Incorrect for this question. A role defined from an explicit permission list. Why the correct answer wins: The deny policy blocks the grant even temporarily.
- **C:** Incorrect for this question. A Google-managed role bound at folder level. Why the correct answer wins: The deny policy blocks the grant even temporarily.
- **D:** Correct. An explicit denial that overrides any allow. In this case: The deny policy blocks the grant even temporarily.

### Question 7 — D

Answer: Grant a custom role limited to the required permissions. A custom role narrows the grant to four permissions. A role defined from an explicit permission list. Local study-map skill 1.4 (IAM Roles and Organization Policies), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 1 (bootstrapping and maintaining a Google Cloud organization): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. An explicit denial that overrides any allow. Why the correct answer wins: A custom role narrows the grant to four permissions.
- **B:** Incorrect for this question. A Google-managed role bound at folder level. Why the correct answer wins: A custom role narrows the grant to four permissions.
- **C:** Incorrect for this question. A guardrail that holds regardless of the IAM grants. Why the correct answer wins: A custom role narrows the grant to four permissions.
- **D:** Correct. A role defined from an explicit permission list. In this case: A custom role narrows the grant to four permissions.

### Question 8 — A, D

Answers: Create one service account per environment; Grant impersonation of the service account instead of a key. One account per environment blocks the path, and impersonation avoids keys. Separate identities so a staging credential cannot act in production. Short-lived credentials obtained by impersonating the account. Local study-map skill 1.5 (Service Account Management), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 1 (bootstrapping and maintaining a Google Cloud organization): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Correct. Separate identities so a staging credential cannot act in production. In this case: One account per environment blocks the path, and impersonation avoids keys.
- **B:** Incorrect for this question. A long-lived credential stored outside the platform. Why the correct answer wins: One account per environment blocks the path, and impersonation avoids keys.
- **C:** Incorrect for this question. The account created automatically with broad project access. Why the correct answer wins: One account per environment blocks the path, and impersonation avoids keys.
- **D:** Correct. Short-lived credentials obtained by impersonating the account. In this case: One account per environment blocks the path, and impersonation avoids keys.
- **E:** Incorrect for this question. A dedicated identity for each deployed workload. Why the correct answer wins: One account per environment blocks the path, and impersonation avoids keys.

### Question 9 — B

Answer: Place the resources in a region that satisfies the residency rule. The processing location must stay inside that country. A location choice that keeps data inside the required boundary. Local study-map skill 1.6 (Data Residency in the Hierarchy), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 1 (bootstrapping and maintaining a Google Cloud organization): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A central network project that lends subnets to other projects. Why the correct answer wins: The processing location must stay inside that country.
- **B:** Correct. A location choice that keeps data inside the required boundary. In this case: The processing location must stay inside that country.
- **C:** Incorrect for this question. A copy held elsewhere for recovery rather than residency. Why the correct answer wins: The processing location must stay inside that country.
- **D:** Incorrect for this question. An organization-level constraint that every folder and project inherits. Why the correct answer wins: The processing location must stay inside that country.

### Question 10 — D

Answer: Define the estate as Terraform modules held in version control. A module exposes the pattern as a reusable interface. Declarative code that is reviewed before it is applied. Local study-map skill 1.7 (Infrastructure-as-Code Tool Selection), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 1 (bootstrapping and maintaining a Google Cloud organization): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A templated bundle of Kubernetes resources. Why the correct answer wins: A module exposes the pattern as a reusable interface.
- **B:** Incorrect for this question. A managed service that runs Terraform deployments. Why the correct answer wins: A module exposes the pattern as a reusable interface.
- **C:** Incorrect for this question. A controller that keeps Kubernetes manifests and cloud resources aligned. Why the correct answer wins: A module exposes the pattern as a reusable interface.
- **D:** Correct. Declarative code that is reviewed before it is applied. In this case: A module exposes the pattern as a reusable interface.

### Question 11 — D

Answer: Apply the deployment through Infrastructure Manager. Infrastructure Manager records the run and the resulting state. A managed service that runs Terraform deployments. Local study-map skill 1.7 (Infrastructure-as-Code Tool Selection), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 1 (bootstrapping and maintaining a Google Cloud organization): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Declarative code that is reviewed before it is applied. Why the correct answer wins: Infrastructure Manager records the run and the resulting state.
- **B:** Incorrect for this question. Idempotent automation through the client library. Why the correct answer wins: Infrastructure Manager records the run and the resulting state.
- **C:** Incorrect for this question. A controller that keeps Kubernetes manifests and cloud resources aligned. Why the correct answer wins: Infrastructure Manager records the run and the resulting state.
- **D:** Correct. A managed service that runs Terraform deployments. In this case: Infrastructure Manager records the run and the resulting state.

### Question 12 — B, C

Answers: Schedule a plan that reports drift; Start from the Cloud Foundation Toolkit blueprints. The plan job compares code and estate, and the toolkit supplies the blueprint. A recurring comparison of declared and actual state. Google-maintained Terraform templates for common foundations. Local study-map skill 1.8 (Blueprints and Controlled Infrastructure Change), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 1 (bootstrapping and maintaining a Google Cloud organization): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A manual sequence repeated on every occasion. Why the correct answer wins: The plan job compares code and estate, and the toolkit supplies the blueprint.
- **B:** Correct. A recurring comparison of declared and actual state. In this case: The plan job compares code and estate, and the toolkit supplies the blueprint.
- **C:** Correct. Google-maintained Terraform templates for common foundations. In this case: The plan job compares code and estate, and the toolkit supplies the blueprint.
- **D:** Incorrect for this question. Idempotent automation through the client library. Why the correct answer wins: The plan job compares code and estate, and the toolkit supplies the blueprint.
- **E:** Incorrect for this question. An unmanaged change with no enforceable record. Why the correct answer wins: The plan job compares code and estate, and the toolkit supplies the blueprint.

### Question 13 — A

Answer: Automate the repeated step with a Python script calling the API. The script performs and reports the cleanup. Idempotent automation through the client library. Local study-map skill 1.9 (Automation with Scripting and APIs), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 1 (bootstrapping and maintaining a Google Cloud organization): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Correct. Idempotent automation through the client library. In this case: The script performs and reports the cleanup.
- **B:** Incorrect for this question. A manual sequence repeated on every occasion. Why the correct answer wins: The script performs and reports the cleanup.
- **C:** Incorrect for this question. An unmanaged change with no enforceable record. Why the correct answer wins: The script performs and reports the cleanup.
- **D:** Incorrect for this question. A recurring comparison of declared and actual state. Why the correct answer wins: The script performs and reports the cleanup.

### Question 14 — B

Answer: Trigger the pipeline only on a signed tag. The tag fixes the commit that built the release. A release build that a tag alone can start. Local study-map skill 1.10 (CI/CD Architecture Stack Design), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 1 (bootstrapping and maintaining a Google Cloud organization): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A trigger that starts the build on a branch change. Why the correct answer wins: The tag fixes the commit that built the release.
- **B:** Correct. A release build that a tag alone can start. In this case: The tag fixes the commit that built the release.
- **C:** Incorrect for this question. A hand-built artifact with no pipeline record. Why the correct answer wins: The tag fixes the commit that built the release.
- **D:** Incorrect for this question. A pre-merge check that blocks a bad change early. Why the correct answer wins: The tag fixes the commit that built the release.

### Question 15 — B

Answer: Use Cloud Build for CI and Cloud Deploy for delivery. The managed pair carries one release record through the stages. A managed pair that separates building from releasing. Local study-map skill 1.10 (CI/CD Architecture Stack Design), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 1 (bootstrapping and maintaining a Google Cloud organization): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A self-operated CI server whose patching is your problem. Why the correct answer wins: The managed pair carries one release record through the stages.
- **B:** Correct. A managed pair that separates building from releasing. In this case: The managed pair carries one release record through the stages.
- **C:** Incorrect for this question. A pull-based delivery controller. Why the correct answer wins: The managed pair carries one release record through the stages.
- **D:** Incorrect for this question. A reproducible image built before deployment. Why the correct answer wins: The managed pair carries one release record through the stages.

### Question 16 — B, E

Answers: Let Argo CD pull the manifests from Git; Bake the machine image with Packer. Argo CD pulls from Git, and Packer supplies the signed image. A pull-based delivery controller. A reproducible image built before deployment. Local study-map skill 1.11 (Third-Party Tooling in the Pipeline), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 1 (bootstrapping and maintaining a Google Cloud organization): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A self-operated CI server whose patching is your problem. Why the correct answer wins: Argo CD pulls from Git, and Packer supplies the signed image.
- **B:** Correct. A reproducible image built before deployment. In this case: Argo CD pulls from Git, and Packer supplies the signed image.
- **C:** Incorrect for this question. A managed pair that separates building from releasing. Why the correct answer wins: Argo CD pulls from Git, and Packer supplies the signed image.
- **D:** Incorrect for this question. A transformation pipeline that keeps the source declarative. Why the correct answer wins: Argo CD pulls from Git, and Packer supplies the signed image.
- **E:** Correct. A pull-based delivery controller. In this case: Argo CD pulls from Git, and Packer supplies the signed image.

### Question 17 — C

Answer: Create a short-lived project per change and delete it after review. A disposable project serves that four-hour window. An environment that exists only while a change is tested. Local study-map skill 1.12 (Multiple Environment Management), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 1 (bootstrapping and maintaining a Google Cloud organization): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A permanent pre-production environment. Why the correct answer wins: A disposable project serves that four-hour window.
- **B:** Incorrect for this question. One image per environment with the settings compiled in. Why the correct answer wins: A disposable project serves that four-hour window.
- **C:** Correct. An environment that exists only while a change is tested. In this case: A disposable project serves that four-hour window.
- **D:** Incorrect for this question. A base manifest with per-environment patches. Why the correct answer wins: A disposable project serves that four-hour window.

### Question 18 — B

Answer: Put the cluster on a release channel with a maintenance window. The release channel with a window schedules the upgrade. A managed upgrade cadence inside a chosen window. Local study-map skill 1.13 (Fleets, Patching, and Cluster Upgrades), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 1 (bootstrapping and maintaining a Google Cloud organization): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A parallel cluster used to prove the upgrade. Why the correct answer wins: The release channel with a window schedules the upgrade.
- **B:** Correct. A managed upgrade cadence inside a chosen window. In this case: The release channel with a window schedules the upgrade.
- **C:** Incorrect for this question. An operator-driven upgrade with no cadence. Why the correct answer wins: The release channel with a window schedules the upgrade.
- **D:** Incorrect for this question. An environment that exists only while a change is tested. Why the correct answer wins: The release channel with a window schedules the upgrade.

### Question 19 — B

Answer: Give developers Cloud Workstations built from a custom image. Cloud Workstations keeps the environment inside the boundary. A managed IDE that runs inside the project boundary. Local study-map skill 1.14 (Secure Development Environments and AI Assistance), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 1 (bootstrapping and maintaining a Google Cloud organization): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Unmanaged toolchains on unmanaged machines. Why the correct answer wins: Cloud Workstations keeps the environment inside the boundary.
- **B:** Correct. A managed IDE that runs inside the project boundary. In this case: Cloud Workstations keeps the environment inside the boundary.
- **C:** Incorrect for this question. A browser terminal with limited tooling and lifetime. Why the correct answer wins: Cloud Workstations keeps the environment inside the boundary.
- **D:** Incorrect for this question. A pinned toolchain that every workstation starts from. Why the correct answer wins: Cloud Workstations keeps the environment inside the boundary.

### Question 20 — C

Answer: Use Gemini CLI for the repetitive script. Gemini CLI explains the command before it runs. A terminal assistant that drafts and runs commands. Local study-map skill 1.14 (Secure Development Environments and AI Assistance), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 1 (bootstrapping and maintaining a Google Cloud organization): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Unmanaged toolchains on unmanaged machines. Why the correct answer wins: Gemini CLI explains the command before it runs.
- **B:** Incorrect for this question. An assistant that reads telemetry and configuration. Why the correct answer wins: Gemini CLI explains the command before it runs.
- **C:** Correct. A terminal assistant that drafts and runs commands. In this case: Gemini CLI explains the command before it runs.
- **D:** Incorrect for this question. An in-editor assistant that proposes code. Why the correct answer wins: Gemini CLI explains the command before it runs.

### Question 21 — A, C

Answers: Create a Cloud Build trigger on the release branch; Create a trigger that runs the tests on every pull request. The branch trigger rebuilds on merge, and the pull-request trigger runs the checks. A trigger that starts the build on a branch change. A pre-merge check that blocks a bad change early. Local study-map skill 2.1 (Pipeline Triggers and Design), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 2 (building and implementing CI/CD pipelines): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Correct. A pre-merge check that blocks a bad change early. In this case: The branch trigger rebuilds on merge, and the pull-request trigger runs the checks.
- **B:** Incorrect for this question. A hand-built artifact with no pipeline record. Why the correct answer wins: The branch trigger rebuilds on merge, and the pull-request trigger runs the checks.
- **C:** Correct. A trigger that starts the build on a branch change. In this case: The branch trigger rebuilds on merge, and the pull-request trigger runs the checks.
- **D:** Incorrect for this question. A required human approval before the release promotes. Why the correct answer wins: The branch trigger rebuilds on merge, and the pull-request trigger runs the checks.
- **E:** Incorrect for this question. A release build that a tag alone can start. Why the correct answer wins: The branch trigger rebuilds on merge, and the pull-request trigger runs the checks.

### Question 22 — A

Answer: Trigger the pipeline only on a signed tag. The tag trigger limits builds to signed tags. A release build that a tag alone can start. Local study-map skill 2.1 (Pipeline Triggers and Design), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 2 (building and implementing CI/CD pipelines): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Correct. A release build that a tag alone can start. In this case: The tag trigger limits builds to signed tags.
- **B:** Incorrect for this question. A pre-merge check that blocks a bad change early. Why the correct answer wins: The tag trigger limits builds to signed tags.
- **C:** Incorrect for this question. A trigger that starts the build on a branch change. Why the correct answer wins: The tag trigger limits builds to signed tags.
- **D:** Incorrect for this question. The immutable record of who released what. Why the correct answer wins: The tag trigger limits builds to signed tags.

### Question 23 — D

Answer: Have an engineer build locally and upload the result. A hand build cannot be reproduced later. A hand-built artifact with no pipeline record. Local study-map skill 2.1 (Pipeline Triggers and Design), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 2 (building and implementing CI/CD pipelines): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A pre-merge check that blocks a bad change early. Why the correct answer wins: A hand build cannot be reproduced later.
- **B:** Incorrect for this question. A release build that a tag alone can start. Why the correct answer wins: A hand build cannot be reproduced later.
- **C:** Incorrect for this question. The immutable record of who released what. Why the correct answer wins: A hand build cannot be reproduced later.
- **D:** Correct. A hand-built artifact with no pipeline record. In this case: A hand build cannot be reproduced later.

### Question 24 — C

Answer: Tag each artifact with the commit SHA and forbid overwrite. An immutable tag makes the rebuild impossible. An immutable tag that identifies the source revision. Local study-map skill 2.2 (Artifact Management), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 2 (building and implementing CI/CD pipelines): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A regional repository for images and packages. Why the correct answer wins: An immutable tag makes the rebuild impossible.
- **B:** Incorrect for this question. Metadata that ties an artifact to its build inputs. Why the correct answer wins: An immutable tag makes the rebuild impossible.
- **C:** Correct. An immutable tag that identifies the source revision. In this case: An immutable tag makes the rebuild impossible.
- **D:** Incorrect for this question. A moving tag that hides which build is running. Why the correct answer wins: An immutable tag makes the rebuild impossible.

### Question 25 — C

Answer: Store the build output in Artifact Registry. The repository runs the cleanup policy itself. A regional repository for images and packages. Local study-map skill 2.2 (Artifact Management), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 2 (building and implementing CI/CD pipelines): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A moving tag that hides which build is running. Why the correct answer wins: The repository runs the cleanup policy itself.
- **B:** Incorrect for this question. The legacy registry without regional repository controls. Why the correct answer wins: The repository runs the cleanup policy itself.
- **C:** Correct. A regional repository for images and packages. In this case: The repository runs the cleanup policy itself.
- **D:** Incorrect for this question. An immutable tag that identifies the source revision. Why the correct answer wins: The repository runs the cleanup policy itself.

### Question 26 — C

Answer: Define the attached cluster as the delivery target. The attached cluster joins the same pipeline. A target that points at a GKE cluster outside Google Cloud. Local study-map skill 2.3 (Hybrid and Multicloud Deployment Targets), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 2 (building and implementing CI/CD pipelines): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A delivery target that sits inside the same project. Why the correct answer wins: The attached cluster joins the same pipeline.
- **B:** Incorrect for this question. A revision-based target with traffic control. Why the correct answer wins: The attached cluster joins the same pipeline.
- **C:** Correct. A target that points at a GKE cluster outside Google Cloud. In this case: The attached cluster joins the same pipeline.
- **D:** Incorrect for this question. A required human approval before the release promotes. Why the correct answer wins: The attached cluster joins the same pipeline.

### Question 27 — B

Answer: Use a GKE cluster in the pipeline project as the target. A GKE target needs no registration step. A delivery target that sits inside the same project. Local study-map skill 2.3 (Hybrid and Multicloud Deployment Targets), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 2 (building and implementing CI/CD pipelines): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A target that points at a GKE cluster outside Google Cloud. Why the correct answer wins: A GKE target needs no registration step.
- **B:** Correct. A delivery target that sits inside the same project. In this case: A GKE target needs no registration step.
- **C:** Incorrect for this question. The immutable record of who released what. Why the correct answer wins: A GKE target needs no registration step.
- **D:** Incorrect for this question. A revision-based target with traffic control. Why the correct answer wins: A GKE target needs no registration step.

### Question 28 — A, E

Answers: Add a Cloud Deploy approval gate before production; Promote automatically to every target in the chain. The gate covers the regulated target, and automatic promotion frees the sandbox. A required human approval before the release promotes. An unattended path from commit to production. Local study-map skill 2.4 (Approval Flows and Deployment Process), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 2 (building and implementing CI/CD pipelines): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Correct. An unattended path from commit to production. In this case: The gate covers the regulated target, and automatic promotion frees the sandbox.
- **B:** Incorrect for this question. The immutable record of who released what. Why the correct answer wins: The gate covers the regulated target, and automatic promotion frees the sandbox.
- **C:** Incorrect for this question. A hand-built artifact with no pipeline record. Why the correct answer wins: The gate covers the regulated target, and automatic promotion frees the sandbox.
- **D:** Incorrect for this question. A return to the last known good release. Why the correct answer wins: The gate covers the regulated target, and automatic promotion frees the sandbox.
- **E:** Correct. A required human approval before the release promotes. In this case: The gate covers the regulated target, and automatic promotion frees the sandbox.

### Question 29 — C

Answer: Read Cloud Audit Logs for the release history. Audit logs record the identity behind the promotion. The immutable record of who released what. Local study-map skill 2.5 (Deployment Auditing and Tracking), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 2 (building and implementing CI/CD pipelines): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Metadata that ties an artifact to its build inputs. Why the correct answer wins: Audit logs record the identity behind the promotion.
- **B:** Incorrect for this question. A published statement about how the artifact was produced. Why the correct answer wins: Audit logs record the identity behind the promotion.
- **C:** Correct. The immutable record of who released what. In this case: Audit logs record the identity behind the promotion.
- **D:** Incorrect for this question. An immutable tag that identifies the source revision. Why the correct answer wins: Audit logs record the identity behind the promotion.

### Question 30 — B

Answer: Describe the build with its supply chain level and signed provenance. The supply chain level answers that question. A published statement about how the artifact was produced. Local study-map skill 2.5 (Deployment Auditing and Tracking), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 2 (building and implementing CI/CD pipelines): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. The immutable record of who released what. Why the correct answer wins: The supply chain level answers that question.
- **B:** Correct. A published statement about how the artifact was produced. In this case: The supply chain level answers that question.
- **C:** Incorrect for this question. Managed issuance and renewal for the endpoint. Why the correct answer wins: The supply chain level answers that question.
- **D:** Incorrect for this question. Metadata that ties an artifact to its build inputs. Why the correct answer wins: The supply chain level answers that question.

### Question 31 — A

Answer: Send ten percent of traffic to the new revision and watch the SLI. The canary limits the change to one region first. A small traffic slice that bounds the blast radius. Local study-map skill 2.6 (Deployment Strategies), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 2 (building and implementing CI/CD pipelines): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Correct. A small traffic slice that bounds the blast radius. In this case: The canary limits the change to one region first.
- **B:** Incorrect for this question. Two full environments with an instant cutover. Why the correct answer wins: The canary limits the change to one region first.
- **C:** Incorrect for this question. A full outage during the change. Why the correct answer wins: The canary limits the change to one region first.
- **D:** Incorrect for this question. A gradual replacement of the running instances. Why the correct answer wins: The canary limits the change to one region first.

### Question 32 — A

Answer: Replace the instances in batches. Rolling replaces them in batches without an outage. A gradual replacement of the running instances. Local study-map skill 2.6 (Deployment Strategies), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 2 (building and implementing CI/CD pipelines): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Correct. A gradual replacement of the running instances. In this case: Rolling replaces them in batches without an outage.
- **B:** Incorrect for this question. A small traffic slice that bounds the blast radius. Why the correct answer wins: Rolling replaces them in batches without an outage.
- **C:** Incorrect for this question. A full outage during the change. Why the correct answer wins: Rolling replaces them in batches without an outage.
- **D:** Incorrect for this question. Two full environments with an instant cutover. Why the correct answer wins: Rolling replaces them in batches without an outage.

### Question 33 — C

Answer: Put the behaviour behind a feature flag. The flag enables the rule per account. A runtime switch that separates deploy from release. Local study-map skill 2.6 (Deployment Strategies), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 2 (building and implementing CI/CD pipelines): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Two full environments with an instant cutover. Why the correct answer wins: The flag enables the rule per account.
- **B:** Incorrect for this question. A full outage during the change. Why the correct answer wins: The flag enables the rule per account.
- **C:** Correct. A runtime switch that separates deploy from release. In this case: The flag enables the rule per account.
- **D:** Incorrect for this question. A small traffic slice that bounds the blast radius. Why the correct answer wins: The flag enables the rule per account.

### Question 34 — A, E

Answers: Gate the rollout on the error-rate SLI; Set an internal target on that indicator. The objective is defined first, and the gate stops the rollout on it. An automated decision driven by the service objective. An objective the team commits to without a contract. Local study-map skill 2.7 (Deployment Success Metrics), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 2 (building and implementing CI/CD pipelines): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Correct. An objective the team commits to without a contract. In this case: The objective is defined first, and the gate stops the rollout on it.
- **B:** Incorrect for this question. A required human approval before the release promotes. Why the correct answer wins: The objective is defined first, and the gate stops the rollout on it.
- **C:** Incorrect for this question. A probe that exercises the path from outside. Why the correct answer wins: The objective is defined first, and the gate stops the rollout on it.
- **D:** Incorrect for this question. A resource signal that says nothing about user success. Why the correct answer wins: The objective is defined first, and the gate stops the rollout on it.
- **E:** Correct. An automated decision driven by the service objective. In this case: The objective is defined first, and the gate stops the rollout on it.

### Question 35 — C

Answer: Roll the release back to the previous one. Rolling back restores the consumer's working release. A return to the last known good release. Local study-map skill 2.8 (Troubleshooting Deployment Issues), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 2 (building and implementing CI/CD pipelines): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. The step output that names the failing command. Why the correct answer wins: Rolling back restores the consumer's working release.
- **B:** Incorrect for this question. A safe repeat that converges on the same state. Why the correct answer wins: Rolling back restores the consumer's working release.
- **C:** Correct. A return to the last known good release. In this case: Rolling back restores the consumer's working release.
- **D:** Incorrect for this question. An untracked change to the live environment. Why the correct answer wins: Rolling back restores the consumer's working release.

### Question 36 — A

Answer: Start from the failed step log in Cloud Build. The step log identifies the step and the command. The step output that names the failing command. Local study-map skill 2.8 (Troubleshooting Deployment Issues), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 2 (building and implementing CI/CD pipelines): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Correct. The step output that names the failing command. In this case: The step log identifies the step and the command.
- **B:** Incorrect for this question. The immutable record of who released what. Why the correct answer wins: The step log identifies the step and the command.
- **C:** Incorrect for this question. A safe repeat that converges on the same state. Why the correct answer wins: The step log identifies the step and the command.
- **D:** Incorrect for this question. A return to the last known good release. Why the correct answer wins: The step log identifies the step and the command.

### Question 37 — B

Answer: Encrypt the payload with a Cloud KMS key. KMS logs each use of the rotated key. A managed key that wraps the data. Local study-map skill 2.9 (Key Management), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 2 (building and implementing CI/CD pipelines): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Managed issuance and renewal for the endpoint. Why the correct answer wins: KMS logs each use of the rotated key.
- **B:** Correct. A managed key that wraps the data. In this case: KMS logs each use of the rotated key.
- **C:** Incorrect for this question. A secret readable by everyone with repository access. Why the correct answer wins: KMS logs each use of the rotated key.
- **D:** Incorrect for this question. A managed store with immutable versions and audit. Why the correct answer wins: KMS logs each use of the rotated key.

### Question 38 — D

Answer: Issue and rotate the certificate with Certificate Manager. Certificate Manager reissues them before expiry. Managed issuance and renewal for the endpoint. Local study-map skill 2.9 (Key Management), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 2 (building and implementing CI/CD pipelines): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A managed store with immutable versions and audit. Why the correct answer wins: Certificate Manager reissues them before expiry.
- **B:** Incorrect for this question. A store for versioned application parameters. Why the correct answer wins: Certificate Manager reissues them before expiry.
- **C:** Incorrect for this question. A managed key that wraps the data. Why the correct answer wins: Certificate Manager reissues them before expiry.
- **D:** Correct. Managed issuance and renewal for the endpoint. In this case: Certificate Manager reissues them before expiry.

### Question 39 — D

Answer: Store the credential in Secret Manager with versions. The newest version is served and each access is audited. A managed store with immutable versions and audit. Local study-map skill 2.10 (Configuration and Secret Management), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 2 (building and implementing CI/CD pipelines): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A value left visible in the build history. Why the correct answer wins: The newest version is served and each access is audited.
- **B:** Incorrect for this question. A store for versioned application parameters. Why the correct answer wins: The newest version is served and each access is audited.
- **C:** Incorrect for this question. A secret readable by everyone with repository access. Why the correct answer wins: The newest version is served and each access is audited.
- **D:** Correct. A managed store with immutable versions and audit. In this case: The newest version is served and each access is audited.

### Question 40 — C

Answer: Keep the non-secret configuration in Parameter Manager. Parameter Manager shows the limits before the deploy. A store for versioned application parameters. Local study-map skill 2.10 (Configuration and Secret Management), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 2 (building and implementing CI/CD pipelines): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A secret readable by everyone with repository access. Why the correct answer wins: Parameter Manager shows the limits before the deploy.
- **B:** Incorrect for this question. A managed store with immutable versions and audit. Why the correct answer wins: Parameter Manager shows the limits before the deploy.
- **C:** Correct. A store for versioned application parameters. In this case: Parameter Manager shows the limits before the deploy.
- **D:** Incorrect for this question. One image per environment with the settings compiled in. Why the correct answer wins: Parameter Manager shows the limits before the deploy.

### Question 41 — D

Answer: Mount the secret at runtime from Secret Manager. A runtime mount keeps the secret out of the artifact. A credential read only when the workload starts. Local study-map skill 2.11 (Build-Time versus Runtime Secret Injection), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 2 (building and implementing CI/CD pipelines): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A secret baked into an artifact anyone can pull. Why the correct answer wins: A runtime mount keeps the secret out of the artifact.
- **B:** Incorrect for this question. A secret readable by everyone with repository access. Why the correct answer wins: A runtime mount keeps the secret out of the artifact.
- **C:** Incorrect for this question. A value left visible in the build history. Why the correct answer wins: A runtime mount keeps the secret out of the artifact.
- **D:** Correct. A credential read only when the workload starts. In this case: A runtime mount keeps the secret out of the artifact.

### Question 42 — A

Answer: Fail the pipeline on a critical vulnerability finding. The gate stops the release on a critical finding. A policy that blocks the promotion. Local study-map skill 2.12 (Vulnerability Scanning and Artifact Analysis), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 2 (building and implementing CI/CD pipelines): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Correct. A policy that blocks the promotion. In this case: The gate stops the release on a critical finding.
- **B:** Incorrect for this question. A finding that no pipeline blocks on. Why the correct answer wins: The gate stops the release on a critical finding.
- **C:** Incorrect for this question. An admission check that only attested images may run. Why the correct answer wins: The gate stops the release on a critical finding.
- **D:** Incorrect for this question. Vulnerability findings for the stored artifacts. Why the correct answer wins: The gate stops the release on a critical finding.

### Question 43 — B

Answer: Enforce Binary Authorization attestations before deploy. Binary Authorization admits only those images. An admission check that only attested images may run. Local study-map skill 2.13 (Supply Chain Security and Binary Authorization), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 2 (building and implementing CI/CD pipelines): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A policy that blocks the promotion. Why the correct answer wins: Binary Authorization admits only those images.
- **B:** Correct. An admission check that only attested images may run. In this case: Binary Authorization admits only those images.
- **C:** Incorrect for this question. Vulnerability findings for the stored artifacts. Why the correct answer wins: Binary Authorization admits only those images.
- **D:** Incorrect for this question. An identity that cannot promote outside its environment. Why the correct answer wins: Binary Authorization admits only those images.

### Question 44 — A

Answer: Enable Artifact Analysis scanning on the repository. Artifact Analysis keeps that list current. Vulnerability findings for the stored artifacts. Local study-map skill 2.13 (Supply Chain Security and Binary Authorization), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 2 (building and implementing CI/CD pipelines): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Correct. Vulnerability findings for the stored artifacts. In this case: Artifact Analysis keeps that list current.
- **B:** Incorrect for this question. An admission check that only attested images may run. Why the correct answer wins: Artifact Analysis keeps that list current.
- **C:** Incorrect for this question. A finding that no pipeline blocks on. Why the correct answer wins: Artifact Analysis keeps that list current.
- **D:** Incorrect for this question. A policy that blocks the promotion. Why the correct answer wins: Artifact Analysis keeps that list current.

### Question 45 — B, D

Answers: Bind deploy permissions only inside the production project; Add an IAM deny policy for the sensitive permission. The scoped identity stays in its environment, and the deny blocks the grant. An identity that cannot promote outside its environment. An explicit denial that overrides any allow. Local study-map skill 2.14 (Per-Environment IAM Policy), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 2 (building and implementing CI/CD pipelines): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A long-lived credential stored outside the platform. Why the correct answer wins: The scoped identity stays in its environment, and the deny blocks the grant.
- **B:** Correct. An explicit denial that overrides any allow. In this case: The scoped identity stays in its environment, and the deny blocks the grant.
- **C:** Incorrect for this question. A build identity with broad write access. Why the correct answer wins: The scoped identity stays in its environment, and the deny blocks the grant.
- **D:** Correct. An identity that cannot promote outside its environment. In this case: The scoped identity stays in its environment, and the deny blocks the grant.
- **E:** Incorrect for this question. A single broad credential across the whole estate. Why the correct answer wins: The scoped identity stays in its environment, and the deny blocks the grant.

### Question 46 — B, C

Answers: Track the ratio of good requests to total requests; Publish a contractual promise with a remedy. The measurement is the SLI, and the promise is the SLA. A measured indicator of how the service behaves. An external commitment that carries a consequence. Local study-map skill 3.1 (SLIs, SLOs, and SLAs), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 3 (applying site reliability engineering practices): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A signal that the budget is going too quickly. Why the correct answer wins: The measurement is the SLI, and the promise is the SLA.
- **B:** Correct. An external commitment that carries a consequence. In this case: The measurement is the SLI, and the promise is the SLA.
- **C:** Correct. A measured indicator of how the service behaves. In this case: The measurement is the SLI, and the promise is the SLA.
- **D:** Incorrect for this question. An explicit trade between reliability and change. Why the correct answer wins: The measurement is the SLI, and the promise is the SLA.
- **E:** Incorrect for this question. An objective the team commits to without a contract. Why the correct answer wins: The measurement is the SLI, and the promise is the SLA.

### Question 47 — C

Answer: Set an internal target on that indicator. A stricter internal bar warns before the contract breaks. An objective the team commits to without a contract. Local study-map skill 3.1 (SLIs, SLOs, and SLAs), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 3 (applying site reliability engineering practices): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. An external commitment that carries a consequence. Why the correct answer wins: A stricter internal bar warns before the contract breaks.
- **B:** Incorrect for this question. A signal that the budget is going too quickly. Why the correct answer wins: A stricter internal bar warns before the contract breaks.
- **C:** Correct. An objective the team commits to without a contract. In this case: A stricter internal bar warns before the contract breaks.
- **D:** Incorrect for this question. A measured indicator of how the service behaves. Why the correct answer wins: A stricter internal bar warns before the contract breaks.

### Question 48 — B

Answer: Choose three nines and spend the difference on features. The trade values cadence over the extra nine. An explicit trade between reliability and change. Local study-map skill 3.1 (SLIs, SLOs, and SLAs), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 3 (applying site reliability engineering practices): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A uniform promise that most services do not need. Why the correct answer wins: The trade values cadence over the extra nine.
- **B:** Correct. An explicit trade between reliability and change. In this case: The trade values cadence over the extra nine.
- **C:** Incorrect for this question. An owned entry with its tier and dependencies. Why the correct answer wins: The trade values cadence over the extra nine.
- **D:** Incorrect for this question. An external commitment that carries a consequence. Why the correct answer wins: The trade values cadence over the extra nine.

### Question 49 — A, C

Answers: Alert on a fast error-budget burn rate; Choose three nines and spend the difference on features. Burn rate pages early, and three nines keeps the target affordable. A signal that the budget is going too quickly. An explicit trade between reliability and change. Local study-map skill 3.2 (Error Budgets), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 3 (applying site reliability engineering practices): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Correct. An explicit trade between reliability and change. In this case: Burn rate pages early, and three nines keeps the target affordable.
- **B:** Incorrect for this question. A uniform promise that most services do not need. Why the correct answer wins: Burn rate pages early, and three nines keeps the target affordable.
- **C:** Correct. A signal that the budget is going too quickly. In this case: Burn rate pages early, and three nines keeps the target affordable.
- **D:** Incorrect for this question. An external commitment that carries a consequence. Why the correct answer wins: Burn rate pages early, and three nines keeps the target affordable.
- **E:** Incorrect for this question. A rule that trades velocity for reliability. Why the correct answer wins: Burn rate pages early, and three nines keeps the target affordable.

### Question 50 — A

Answer: Stop feature releases when the error budget is spent. A spent allowance pauses the launches until it recovers. A rule that trades velocity for reliability. Local study-map skill 3.2 (Error Budgets), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 3 (applying site reliability engineering practices): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Correct. A rule that trades velocity for reliability. In this case: A spent allowance pauses the launches until it recovers.
- **B:** Incorrect for this question. A signal that the budget is going too quickly. Why the correct answer wins: A spent allowance pauses the launches until it recovers.
- **C:** Incorrect for this question. An external commitment that carries a consequence. Why the correct answer wins: A spent allowance pauses the launches until it recovers.
- **D:** Incorrect for this question. A uniform promise that most services do not need. Why the correct answer wins: A spent allowance pauses the launches until it recovers.

### Question 51 — A

Answer: Assume five nines for every service. Copying one target to unlike services wastes effort. A uniform promise that most services do not need. Local study-map skill 3.3 (Cost of Reliability and Nines), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 3 (applying site reliability engineering practices): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Correct. A uniform promise that most services do not need. In this case: Copying one target to unlike services wastes effort.
- **B:** Incorrect for this question. An explicit trade between reliability and change. Why the correct answer wins: Copying one target to unlike services wastes effort.
- **C:** Incorrect for this question. Capacity arranged ahead of a known peak. Why the correct answer wins: Copying one target to unlike services wastes effort.
- **D:** Incorrect for this question. An external commitment that carries a consequence. Why the correct answer wins: Copying one target to unlike services wastes effort.

### Question 52 — D

Answer: Choose three nines and spend the difference on features. The decision accepts fewer nines for more delivery. An explicit trade between reliability and change. Local study-map skill 3.3 (Cost of Reliability and Nines), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 3 (applying site reliability engineering practices): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. An external commitment that carries a consequence. Why the correct answer wins: The decision accepts fewer nines for more delivery.
- **B:** Incorrect for this question. An owned entry with its tier and dependencies. Why the correct answer wins: The decision accepts fewer nines for more delivery.
- **C:** Incorrect for this question. A uniform promise that most services do not need. Why the correct answer wins: The decision accepts fewer nines for more delivery.
- **D:** Correct. An explicit trade between reliability and change. In this case: The decision accepts fewer nines for more delivery.

### Question 53 — D

Answer: Register the service in the service catalog. The catalog names the owning team for the service. An owned entry with its tier and dependencies. Local study-map skill 3.4 (Service Lifecycle Management), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 3 (applying site reliability engineering practices): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A planned withdrawal with a migration path. Why the correct answer wins: The catalog names the owning team for the service.
- **B:** Incorrect for this question. An unowned workload that still costs money. Why the correct answer wins: The catalog names the owning team for the service.
- **C:** Incorrect for this question. Capacity arranged ahead of a known peak. Why the correct answer wins: The catalog names the owning team for the service.
- **D:** Correct. An owned entry with its tier and dependencies. In this case: The catalog names the owning team for the service.

### Question 54 — D

Answer: Announce the retirement date and withdraw traffic gradually. The retirement plan publishes the date and withdraws traffic. A planned withdrawal with a migration path. Local study-map skill 3.4 (Service Lifecycle Management), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 3 (applying site reliability engineering practices): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. An unowned workload that still costs money. Why the correct answer wins: The retirement plan publishes the date and withdraws traffic.
- **B:** Incorrect for this question. Extra supply in a different location. Why the correct answer wins: The retirement plan publishes the date and withdraws traffic.
- **C:** Incorrect for this question. An owned entry with its tier and dependencies. Why the correct answer wins: The retirement plan publishes the date and withdraws traffic.
- **D:** Correct. A planned withdrawal with a migration path. In this case: The retirement plan publishes the date and withdraws traffic.

### Question 55 — C

Answer: Request a quota increase and reserve capacity before the launch. A reservation secures the capacity before launch. Capacity arranged ahead of a known peak. Local study-map skill 3.5 (Capacity Planning and Quotas), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 3 (applying site reliability engineering practices): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A flexible placement into a cheaper window. Why the correct answer wins: A reservation secures the capacity before launch.
- **B:** Incorrect for this question. Calendar-driven capacity with no feedback loop. Why the correct answer wins: A reservation secures the capacity before launch.
- **C:** Correct. Capacity arranged ahead of a known peak. In this case: A reservation secures the capacity before launch.
- **D:** Incorrect for this question. Limits that throttle at the worst possible moment. Why the correct answer wins: A reservation secures the capacity before launch.

### Question 56 — C

Answer: Assume the default quota will absorb the launch. The default limit rarely matches a launch of this size. Limits that throttle at the worst possible moment. Local study-map skill 3.5 (Capacity Planning and Quotas), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 3 (applying site reliability engineering practices): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Calendar-driven capacity with no feedback loop. Why the correct answer wins: The default limit rarely matches a launch of this size.
- **B:** Incorrect for this question. A flexible placement into a cheaper window. Why the correct answer wins: The default limit rarely matches a launch of this size.
- **C:** Correct. Limits that throttle at the worst possible moment. In this case: The default limit rarely matches a launch of this size.
- **D:** Incorrect for this question. Capacity arranged ahead of a known peak. Why the correct answer wins: The default limit rarely matches a launch of this size.

### Question 57 — A, C

Answers: Scale on queue depth with a horizontal pod autoscaler; Set Cloud Run concurrency so replicas follow load. The backlog scales the workers, and concurrency scales the instances. Replica scaling driven by a work signal. Concurrency-based replica scaling. Local study-map skill 3.6 (Autoscaling), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 3 (applying site reliability engineering practices): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Correct. Replica scaling driven by a work signal. In this case: The backlog scales the workers, and concurrency scales the instances.
- **B:** Incorrect for this question. A flexible placement into a cheaper window. Why the correct answer wins: The backlog scales the workers, and concurrency scales the instances.
- **C:** Correct. Concurrency-based replica scaling. In this case: The backlog scales the workers, and concurrency scales the instances.
- **D:** Incorrect for this question. Managed instance scaling from a resource metric. Why the correct answer wins: The backlog scales the workers, and concurrency scales the instances.
- **E:** Incorrect for this question. Calendar-driven capacity with no feedback loop. Why the correct answer wins: The backlog scales the workers, and concurrency scales the instances.

### Question 58 — C

Answer: Add capacity on a fixed calendar schedule. Calendar scaling ignores the actual demand curve. Calendar-driven capacity with no feedback loop. Local study-map skill 3.6 (Autoscaling), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 3 (applying site reliability engineering practices): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Concurrency-based replica scaling. Why the correct answer wins: Calendar scaling ignores the actual demand curve.
- **B:** Incorrect for this question. Replica scaling driven by a work signal. Why the correct answer wins: Calendar scaling ignores the actual demand curve.
- **C:** Correct. Calendar-driven capacity with no feedback loop. In this case: Calendar scaling ignores the actual demand curve.
- **D:** Incorrect for this question. Managed instance scaling from a resource metric. Why the correct answer wins: Calendar scaling ignores the actual demand curve.

### Question 59 — B

Answer: Drain connections before removing the instance. Draining finishes them before the node is removed. A graceful handover of in-flight requests. Local study-map skill 3.7 (Traffic Draining and Redirection), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 3 (applying site reliability engineering practices): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A name-level redirect to a healthy region. Why the correct answer wins: Draining finishes them before the node is removed.
- **B:** Correct. A graceful handover of in-flight requests. In this case: Draining finishes them before the node is removed.
- **C:** Incorrect for this question. Extra supply in a different location. Why the correct answer wins: Draining finishes them before the node is removed.
- **D:** Incorrect for this question. A health-checked switch between backends. Why the correct answer wins: Draining finishes them before the node is removed.

### Question 60 — C

Answer: Add capacity in a second region. Extra capacity in another region restores supply. Extra supply in a different location. Local study-map skill 3.7 (Traffic Draining and Redirection), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 3 (applying site reliability engineering practices): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A graceful handover of in-flight requests. Why the correct answer wins: Extra capacity in another region restores supply.
- **B:** Incorrect for this question. A name-level redirect to a healthy region. Why the correct answer wins: Extra capacity in another region restores supply.
- **C:** Correct. Extra supply in a different location. In this case: Extra capacity in another region restores supply.
- **D:** Incorrect for this question. A health-checked switch between backends. Why the correct answer wins: Extra capacity in another region restores supply.

### Question 61 — D

Answer: Use a load balancer failover backend. The failover backend reacts to the failed health check. A health-checked switch between backends. Local study-map skill 3.8 (Incident Capacity), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 3 (applying site reliability engineering practices): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Capacity arranged ahead of a known peak. Why the correct answer wins: The failover backend reacts to the failed health check.
- **B:** Incorrect for this question. A graceful handover of in-flight requests. Why the correct answer wins: The failover backend reacts to the failed health check.
- **C:** Incorrect for this question. A name-level redirect to a healthy region. Why the correct answer wins: The failover backend reacts to the failed health check.
- **D:** Correct. A health-checked switch between backends. In this case: The failover backend reacts to the failed health check.

### Question 62 — D

Answer: Redeploy the previous image to the affected service. Redeploying the previous build restores service. A known good artifact restored in place. Local study-map skill 3.9 (Rollback Strategies), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 3 (applying site reliability engineering practices): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A paired migration that can be undone. Why the correct answer wins: Redeploying the previous build restores service.
- **B:** Incorrect for this question. No action while users are still failing. Why the correct answer wins: Redeploying the previous build restores service.
- **C:** Incorrect for this question. An untracked change to the live environment. Why the correct answer wins: Redeploying the previous build restores service.
- **D:** Correct. A known good artifact restored in place. In this case: Redeploying the previous build restores service.

### Question 63 — C

Answer: Reverse the schema change with a tested down migration. A tested down migration would have restored the column. A paired migration that can be undone. Local study-map skill 3.9 (Rollback Strategies), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 3 (applying site reliability engineering practices): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. No action while users are still failing. Why the correct answer wins: A tested down migration would have restored the column.
- **B:** Incorrect for this question. A known good artifact restored in place. Why the correct answer wins: A tested down migration would have restored the column.
- **C:** Correct. A paired migration that can be undone. In this case: A tested down migration would have restored the column.
- **D:** Incorrect for this question. An untracked change to the live environment. Why the correct answer wins: A tested down migration would have restored the column.

### Question 64 — B

Answer: Install the Ops Agent on the instances. The Ops Agent collects that metric. A collector that ships logs and metrics from the VM. Local study-map skill 4.1 (Log Collection and Ingestion), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 4 (implementing observability practices and troubleshooting): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A vendor-neutral pipeline for traces and metrics. Why the correct answer wins: The Ops Agent collects that metric.
- **B:** Correct. A collector that ships logs and metrics from the VM. In this case: The Ops Agent collects that metric.
- **C:** Incorrect for this question. Per-connection records of accepted and denied traffic. Why the correct answer wins: The Ops Agent collects that metric.
- **D:** Incorrect for this question. Request metrics emitted by the sidecar proxies. Why the correct answer wins: The Ops Agent collects that metric.

### Question 65 — B

Answer: Enable Data Access audit logs for the service. Data Access audit logs record those reads. A record of reads and writes on the resource. Local study-map skill 4.1 (Log Collection and Ingestion), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 4 (implementing observability practices and troubleshooting): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Request metrics emitted by the sidecar proxies. Why the correct answer wins: Data Access audit logs record those reads.
- **B:** Correct. A record of reads and writes on the resource. In this case: Data Access audit logs record those reads.
- **C:** Incorrect for this question. A collector that ships logs and metrics from the VM. Why the correct answer wins: Data Access audit logs record those reads.
- **D:** Incorrect for this question. Per-connection records of accepted and denied traffic. Why the correct answer wins: Data Access audit logs record those reads.

### Question 66 — A

Answer: Sample the high-volume debug entries. Sampling cuts the volume but keeps the errors. A fraction kept for diagnosis at lower cost. Local study-map skill 4.2 (Log Optimization and Cost), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 4 (implementing observability practices and troubleshooting): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Correct. A fraction kept for diagnosis at lower cost. In this case: Sampling cuts the volume but keeps the errors.
- **B:** Incorrect for this question. A filter that drops matching entries before storage. Why the correct answer wins: Sampling cuts the volume but keeps the errors.
- **C:** Incorrect for this question. A label removal that cuts the stored series. Why the correct answer wins: Sampling cuts the volume but keeps the errors.
- **D:** Incorrect for this question. A cost estimate driven by actual ingest. Why the correct answer wins: Sampling cuts the volume but keeps the errors.

### Question 67 — D

Answer: Measure log volume per service before choosing a retention period. Measuring the volume is what costs the change. A cost estimate driven by actual ingest. Local study-map skill 4.2 (Log Optimization and Cost), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 4 (implementing observability practices and troubleshooting): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A filter that drops matching entries before storage. Why the correct answer wins: Measuring the volume is what costs the change.
- **B:** Incorrect for this question. A fraction kept for diagnosis at lower cost. Why the correct answer wins: Measuring the volume is what costs the change.
- **C:** Incorrect for this question. A retention period that cannot be shortened. Why the correct answer wins: Measuring the volume is what costs the change.
- **D:** Correct. A cost estimate driven by actual ingest. In this case: Measuring the volume is what costs the change.

### Question 68 — D, E

Answers: Create a log-based metric for the error string; Open the Logs Explorer and pivot from the error entry. The log metric counts the string, and pivoting shows the neighbourhood. A counter derived from matching entries. An interactive view with field filters. Local study-map skill 4.3 (Logs Explorer and Query Language), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 4 (implementing observability practices and troubleshooting): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A probe that exercises the path from outside. Why the correct answer wins: The log metric counts the string, and pivoting shows the neighbourhood.
- **B:** Incorrect for this question. A sink suited to cheap long-term retention. Why the correct answer wins: The log metric counts the string, and pivoting shows the neighbourhood.
- **C:** Incorrect for this question. A precise query over the stored entries. Why the correct answer wins: The log metric counts the string, and pivoting shows the neighbourhood.
- **D:** Correct. An interactive view with field filters. In this case: The log metric counts the string, and pivoting shows the neighbourhood.
- **E:** Correct. A counter derived from matching entries. In this case: The log metric counts the string, and pivoting shows the neighbourhood.

### Question 69 — D

Answer: Filter with the Logging query language on the resource label. The query filters on namespace and severity. A precise query over the stored entries. Local study-map skill 4.3 (Logs Explorer and Query Language), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 4 (implementing observability practices and troubleshooting): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A counter derived from matching entries. Why the correct answer wins: The query filters on namespace and severity.
- **B:** Incorrect for this question. An interactive view with field filters. Why the correct answer wins: The query filters on namespace and severity.
- **C:** Incorrect for this question. A sink suited to cheap long-term retention. Why the correct answer wins: The query filters on namespace and severity.
- **D:** Correct. A precise query over the stored entries. In this case: The query filters on namespace and severity.

### Question 70 — B

Answer: Route the entries to a Cloud Storage bucket. A storage sink keeps old entries retrievable at low cost. A sink suited to cheap long-term retention. Local study-map skill 4.4 (Log Export and Retention), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 4 (implementing observability practices and troubleshooting): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A retention period that cannot be shortened. Why the correct answer wins: A storage sink keeps old entries retrievable at low cost.
- **B:** Correct. A sink suited to cheap long-term retention. In this case: A storage sink keeps old entries retrievable at low cost.
- **C:** Incorrect for this question. A sink that lands logs in a queryable table. Why the correct answer wins: A storage sink keeps old entries retrievable at low cost.
- **D:** Incorrect for this question. A sink that streams entries to another consumer. Why the correct answer wins: A storage sink keeps old entries retrievable at low cost.

### Question 71 — B

Answer: Set the log bucket retention and lock it. The lock prevents any shortening of the period. A retention period that cannot be shortened. Local study-map skill 4.4 (Log Export and Retention), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 4 (implementing observability practices and troubleshooting): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A cost estimate driven by actual ingest. Why the correct answer wins: The lock prevents any shortening of the period.
- **B:** Correct. A retention period that cannot be shortened. In this case: The lock prevents any shortening of the period.
- **C:** Incorrect for this question. A sink suited to cheap long-term retention. Why the correct answer wins: The lock prevents any shortening of the period.
- **D:** Incorrect for this question. A sink that lands logs in a queryable table. Why the correct answer wins: The lock prevents any shortening of the period.

### Question 72 — C

Answer: Redact the email field with a log processor. The processor masks them before storage. A transform that removes the value before storage. Local study-map skill 4.5 (Sensitive Data Redaction), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 4 (implementing observability practices and troubleshooting): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A filter that drops matching entries before storage. Why the correct answer wins: The processor masks them before storage.
- **B:** Incorrect for this question. A procedural promise with no enforcement. Why the correct answer wins: The processor masks them before storage.
- **C:** Correct. A transform that removes the value before storage. In this case: The processor masks them before storage.
- **D:** Incorrect for this question. A sink suited to cheap long-term retention. Why the correct answer wins: The processor masks them before storage.

### Question 73 — A

Answer: Ask Gemini Cloud Assist which span dominates the trace. The assistant names the dominant span. An AI pointer to the expensive span. Local study-map skill 4.6 (Gemini Cloud Assist for Log Analysis), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 4 (implementing observability practices and troubleshooting): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Correct. An AI pointer to the expensive span. In this case: The assistant names the dominant span.
- **B:** Incorrect for this question. An AI summary over the selected log range. Why the correct answer wins: The assistant names the dominant span.
- **C:** Incorrect for this question. A per-span timing view of one request. Why the correct answer wins: The assistant names the dominant span.
- **D:** Incorrect for this question. An AI interpretation of the chart. Why the correct answer wins: The assistant names the dominant span.

### Question 74 — A

Answer: Emit a custom metric for the business event. The service emits the wait time as a metric. A measurement written by the application itself. Local study-map skill 4.7 (Metrics Collection), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 4 (implementing observability practices and troubleshooting): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Correct. A measurement written by the application itself. In this case: The service emits the wait time as a metric.
- **B:** Incorrect for this question. A counter derived from matching entries. Why the correct answer wins: The service emits the wait time as a metric.
- **C:** Incorrect for this question. A metrics store fed by a scrape endpoint. Why the correct answer wins: The service emits the wait time as a metric.
- **D:** Incorrect for this question. A probe that exercises the path from outside. Why the correct answer wins: The service emits the wait time as a metric.

### Question 75 — D

Answer: Run an OpenTelemetry Collector in the cluster. The collector forwards to both vendors. A vendor-neutral pipeline for traces and metrics. Local study-map skill 4.7 (Metrics Collection), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 4 (implementing observability practices and troubleshooting): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A collector that ships logs and metrics from the VM. Why the correct answer wins: The collector forwards to both vendors.
- **B:** Incorrect for this question. Request metrics emitted by the sidecar proxies. Why the correct answer wins: The collector forwards to both vendors.
- **C:** Incorrect for this question. Per-connection records of accepted and denied traffic. Why the correct answer wins: The collector forwards to both vendors.
- **D:** Correct. A vendor-neutral pipeline for traces and metrics. In this case: The collector forwards to both vendors.

### Question 76 — B, E

Answers: Scrape the workload with managed collection for Prometheus; Create a log-based metric for the error string. Managed collection stores the scrape, and the log metric counts the string. A metrics store fed by a scrape endpoint. A counter derived from matching entries. Local study-map skill 4.8 (Custom and Log-Based Metrics), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 4 (implementing observability practices and troubleshooting): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A shared view of the signals that matter. Why the correct answer wins: Managed collection stores the scrape, and the log metric counts the string.
- **B:** Correct. A counter derived from matching entries. In this case: Managed collection stores the scrape, and the log metric counts the string.
- **C:** Incorrect for this question. A measurement written by the application itself. Why the correct answer wins: Managed collection stores the scrape, and the log metric counts the string.
- **D:** Incorrect for this question. A probe that exercises the path from outside. Why the correct answer wins: Managed collection stores the scrape, and the log metric counts the string.
- **E:** Correct. A metrics store fed by a scrape endpoint. In this case: Managed collection stores the scrape, and the log metric counts the string.

### Question 77 — A

Answer: Create an uptime check against the login flow. An external probe fails when the certificate lapses. A probe that exercises the path from outside. Local study-map skill 4.9 (Synthetic Monitors), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 4 (implementing observability practices and troubleshooting): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Correct. A probe that exercises the path from outside. In this case: An external probe fails when the certificate lapses.
- **B:** Incorrect for this question. A counter derived from matching entries. Why the correct answer wins: An external probe fails when the certificate lapses.
- **C:** Incorrect for this question. A measurement written by the application itself. Why the correct answer wins: An external probe fails when the certificate lapses.
- **D:** Incorrect for this question. A metrics store fed by a scrape endpoint. Why the correct answer wins: An external probe fails when the certificate lapses.

### Question 78 — D

Answer: Build one dashboard and share it with the on-call rotation. One shared dashboard gives them that view. A shared view of the signals that matter. Local study-map skill 4.10 (Metrics Explorer and Dashboards), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 4 (implementing observability practices and troubleshooting): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A documented response beside the notification. Why the correct answer wins: One shared dashboard gives them that view.
- **B:** Incorrect for this question. A static threshold on a resource metric. Why the correct answer wins: One shared dashboard gives them that view.
- **C:** Incorrect for this question. A third-party paging integration. Why the correct answer wins: One shared dashboard gives them that view.
- **D:** Correct. A shared view of the signals that matter. In this case: One shared dashboard gives them that view.

### Question 79 — C

Answer: Attach the remediation playbook to the alert. The playbook puts the first step beside the alert. A documented response beside the notification. Local study-map skill 4.10 (Metrics Explorer and Dashboards), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 4 (implementing observability practices and troubleshooting): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A shared view of the signals that matter. Why the correct answer wins: The playbook puts the first step beside the alert.
- **B:** Incorrect for this question. A delivery route for the alert. Why the correct answer wins: The playbook puts the first step beside the alert.
- **C:** Correct. A documented response beside the notification. In this case: The playbook puts the first step beside the alert.
- **D:** Incorrect for this question. A page driven by the objective instead of a raw threshold. Why the correct answer wins: The playbook puts the first step beside the alert.

### Question 80 — D

Answer: Create an alerting policy on the SLO burn rate. The burn-rate policy pages on that projection. A page driven by the objective instead of a raw threshold. Local study-map skill 4.11 (Alerting Policies), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 4 (implementing observability practices and troubleshooting): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A static threshold on a resource metric. Why the correct answer wins: The burn-rate policy pages on that projection.
- **B:** Incorrect for this question. A third-party paging integration. Why the correct answer wins: The burn-rate policy pages on that projection.
- **C:** Incorrect for this question. A documented response beside the notification. Why the correct answer wins: The burn-rate policy pages on that projection.
- **D:** Correct. A page driven by the objective instead of a raw threshold. In this case: The burn-rate policy pages on that projection.

### Question 81 — D

Answer: Alert when CPU stays above ninety percent for ten minutes. An ignored page trains responders to ignore alerts. A static threshold on a resource metric. Local study-map skill 4.11 (Alerting Policies), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 4 (implementing observability practices and troubleshooting): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A probe that exercises the path from outside. Why the correct answer wins: An ignored page trains responders to ignore alerts.
- **B:** Incorrect for this question. A page driven by the objective instead of a raw threshold. Why the correct answer wins: An ignored page trains responders to ignore alerts.
- **C:** Incorrect for this question. A delivery route for the alert. Why the correct answer wins: An ignored page trains responders to ignore alerts.
- **D:** Correct. A static threshold on a resource metric. In this case: An ignored page trains responders to ignore alerts.

### Question 82 — B, E

Answers: Send the alert to PagerDuty through a webhook; Add an email notification channel for the on-call group. The webhook reaches the incident tool, and email copies audit. A third-party paging integration. A delivery route for the alert. Local study-map skill 4.12 (Third-Party Alerting Integration), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 4 (implementing observability practices and troubleshooting): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A documented response beside the notification. Why the correct answer wins: The webhook reaches the incident tool, and email copies audit.
- **B:** Correct. A delivery route for the alert. In this case: The webhook reaches the incident tool, and email copies audit.
- **C:** Incorrect for this question. A probe that exercises the path from outside. Why the correct answer wins: The webhook reaches the incident tool, and email copies audit.
- **D:** Incorrect for this question. A static threshold on a resource metric. Why the correct answer wins: The webhook reaches the incident tool, and email copies audit.
- **E:** Correct. A third-party paging integration. In this case: The webhook reaches the incident tool, and email copies audit.

### Question 83 — A, C

Answers: Put the trace ID in the structured log line; Read the trace waterfall to find the slow span. The trace ID links the log, and the waterfall shows the slow span. A join key between traces and logs. A per-span timing view of one request. Local study-map skill 4.13 (Distributed Tracing with OpenTelemetry), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 4 (implementing observability practices and troubleshooting): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Correct. A per-span timing view of one request. In this case: The trace ID links the log, and the waterfall shows the slow span.
- **B:** Incorrect for this question. An AI pointer to the expensive span. Why the correct answer wins: The trace ID links the log, and the waterfall shows the slow span.
- **C:** Correct. A join key between traces and logs. In this case: The trace ID links the log, and the waterfall shows the slow span.
- **D:** Incorrect for this question. Trace context emitted for each request. Why the correct answer wins: The trace ID links the log, and the waterfall shows the slow span.
- **E:** Incorrect for this question. No shared identifier between the two signals. Why the correct answer wins: The trace ID links the log, and the waterfall shows the slow span.

### Question 84 — C

Answer: Instrument the service with OpenTelemetry spans. Spans record the duration of each call. Trace context emitted for each request. Local study-map skill 4.13 (Distributed Tracing with OpenTelemetry), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 4 (implementing observability practices and troubleshooting): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A join key between traces and logs. Why the correct answer wins: Spans record the duration of each call.
- **B:** Incorrect for this question. An AI pointer to the expensive span. Why the correct answer wins: Spans record the duration of each call.
- **C:** Correct. Trace context emitted for each request. In this case: Spans record the duration of each call.
- **D:** Incorrect for this question. A per-span timing view of one request. Why the correct answer wins: Spans record the duration of each call.

### Question 85 — C

Answer: Log a timestamp and correlate by eye later. Two clocks drift, so eyeballing the times misleads. No shared identifier between the two signals. Local study-map skill 4.14 (Trace Analysis and Log Correlation), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 4 (implementing observability practices and troubleshooting): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Trace context emitted for each request. Why the correct answer wins: Two clocks drift, so eyeballing the times misleads.
- **B:** Incorrect for this question. A join key between traces and logs. Why the correct answer wins: Two clocks drift, so eyeballing the times misleads.
- **C:** Correct. No shared identifier between the two signals. In this case: Two clocks drift, so eyeballing the times misleads.
- **D:** Incorrect for this question. A per-span timing view of one request. Why the correct answer wins: Two clocks drift, so eyeballing the times misleads.

### Question 86 — B

Answer: Check Cloud NAT port exhaustion for the egress range. The shared address has run out of ports. A shared egress resource that runs out of ports. Local study-map skill 4.15 (Infrastructure and Pipeline Troubleshooting), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 4 (implementing observability practices and troubleshooting): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. The rule that blocked the connection. Why the correct answer wins: The shared address has run out of ports.
- **B:** Correct. A shared egress resource that runs out of ports. In this case: The shared address has run out of ports.
- **C:** Incorrect for this question. The limit that refused the resource. Why the correct answer wins: The shared address has run out of ports.
- **D:** Incorrect for this question. The identity the node uses to fetch the image. Why the correct answer wins: The shared address has run out of ports.

### Question 87 — A

Answer: Compare the readiness probe with the application startup time. The probe may run before the application listens. A probe that fails before the app is listening. Local study-map skill 4.16 (Application and Latency Troubleshooting), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 4 (implementing observability practices and troubleshooting): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Correct. A probe that fails before the app is listening. In this case: The probe may run before the application listens.
- **B:** Incorrect for this question. A stale name that still points at the old address. Why the correct answer wins: The probe may run before the application listens.
- **C:** Incorrect for this question. A hotspot found on the request path. Why the correct answer wins: The probe may run before the application listens.
- **D:** Incorrect for this question. A shared egress resource that runs out of ports. Why the correct answer wins: The probe may run before the application listens.

### Question 88 — B

Answer: Compare latency with the saturation metric. Correlating latency with saturation explains the rise. A queueing symptom traced to a full resource. Local study-map skill 4.16 (Application and Latency Troubleshooting), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 4 (implementing observability practices and troubleshooting): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Trace context emitted for each request. Why the correct answer wins: Correlating latency with saturation explains the rise.
- **B:** Correct. A queueing symptom traced to a full resource. In this case: Correlating latency with saturation explains the rise.
- **C:** Incorrect for this question. A per-span timing view of one request. Why the correct answer wins: Correlating latency with saturation explains the rise.
- **D:** Incorrect for this question. A join key between traces and logs. Why the correct answer wins: Correlating latency with saturation explains the rise.

### Question 89 — B

Answer: Track the service objective on a shared dashboard. The objective dashboard gives that per-service picture. A goal-oriented view of performance. Local study-map skill 5.1 (Application Performance Monitoring), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 5 (optimizing performance and cost): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A cost estimate driven by actual ingest. Why the correct answer wins: The objective dashboard gives that per-service picture.
- **B:** Correct. A goal-oriented view of performance. In this case: The objective dashboard gives that per-service picture.
- **C:** Incorrect for this question. A recommendation aimed at spend. Why the correct answer wins: The objective dashboard gives that per-service picture.
- **D:** Incorrect for this question. An application-level view of response time. Why the correct answer wins: The objective dashboard gives that per-service picture.

### Question 90 — A

Answer: Measure request latency by endpoint in Cloud Monitoring. Per-endpoint latency isolates the affected journey. An application-level view of response time. Local study-map skill 5.1 (Application Performance Monitoring), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 5 (optimizing performance and cost): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Correct. An application-level view of response time. In this case: Per-endpoint latency isolates the affected journey.
- **B:** Incorrect for this question. A recommendation aimed at spend. Why the correct answer wins: Per-endpoint latency isolates the affected journey.
- **C:** Incorrect for this question. A queryable record of spend by label. Why the correct answer wins: Per-endpoint latency isolates the affected journey.
- **D:** Incorrect for this question. A goal-oriented view of performance. Why the correct answer wins: Per-endpoint latency isolates the affected journey.

### Question 91 — B, C

Answers: Review the Active Assist recommendations for the project; Apply the reliability recommender for the missing quota. Active Assist lists the suggestions, and the reliability recommender flags the headroom. Suggested changes generated from telemetry. A recommendation aimed at resilience. Local study-map skill 5.2 (Active Assist and Recommenders), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 5 (optimizing performance and cost): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A queryable record of spend by label. Why the correct answer wins: Active Assist lists the suggestions, and the reliability recommender flags the headroom.
- **B:** Correct. A recommendation aimed at resilience. In this case: Active Assist lists the suggestions, and the reliability recommender flags the headroom.
- **C:** Correct. Suggested changes generated from telemetry. In this case: Active Assist lists the suggestions, and the reliability recommender flags the headroom.
- **D:** Incorrect for this question. Discounted capacity that can be reclaimed. Why the correct answer wins: Active Assist lists the suggestions, and the reliability recommender flags the headroom.
- **E:** Incorrect for this question. A recommendation aimed at spend. Why the correct answer wins: Active Assist lists the suggestions, and the reliability recommender flags the headroom.

### Question 92 — A

Answer: Apply the cost recommender suggestion for the idle disks. The cost recommender flags the unused reservations. A recommendation aimed at spend. Local study-map skill 5.2 (Active Assist and Recommenders), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 5 (optimizing performance and cost): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Correct. A recommendation aimed at spend. In this case: The cost recommender flags the unused reservations.
- **B:** Incorrect for this question. A recommendation aimed at resilience. Why the correct answer wins: The cost recommender flags the unused reservations.
- **C:** Incorrect for this question. Suggested changes generated from telemetry. Why the correct answer wins: The cost recommender flags the unused reservations.
- **D:** Incorrect for this question. Discounted capacity that can be reclaimed. Why the correct answer wins: The cost recommender flags the unused reservations.

### Question 93 — A

Answer: Exclude the debug stream and keep the error stream. Excluding the debug stream removes that volume. A reduction that preserves the useful signal. Local study-map skill 5.3 (Observability Cost Management), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 5 (optimizing performance and cost): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Correct. A reduction that preserves the useful signal. In this case: Excluding the debug stream removes that volume.
- **B:** Incorrect for this question. A retention period that cannot be shortened. Why the correct answer wins: Excluding the debug stream removes that volume.
- **C:** Incorrect for this question. A cost estimate driven by actual ingest. Why the correct answer wins: Excluding the debug stream removes that volume.
- **D:** Incorrect for this question. A label removal that cuts the stored series. Why the correct answer wins: Excluding the debug stream removes that volume.

### Question 94 — B

Answer: Drop the high-cardinality user label from the metric. The label multiplies the stored series. A label removal that cuts the stored series. Local study-map skill 5.3 (Observability Cost Management), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 5 (optimizing performance and cost): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A cheaper egress path with different performance. Why the correct answer wins: The label multiplies the stored series.
- **B:** Correct. A label removal that cuts the stored series. In this case: The label multiplies the stored series.
- **C:** Incorrect for this question. A reduction that preserves the useful signal. Why the correct answer wins: The label multiplies the stored series.
- **D:** Incorrect for this question. A cost estimate driven by actual ingest. Why the correct answer wins: The label multiplies the stored series.

### Question 95 — B, D

Answers: Put the stateless workers on a Spot node pool; Run the batch on Spot VMs. The consumer pool runs on Spot nodes, and the farm runs as Spot batches. A pool built from reclaimable capacity. Discounted capacity that can be reclaimed. Local study-map skill 5.4 (Spot Virtual Machines), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 5 (optimizing performance and cost): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Reclaimable capacity under a stateful workload. Why the correct answer wins: The consumer pool runs on Spot nodes, and the farm runs as Spot batches.
- **B:** Correct. Discounted capacity that can be reclaimed. In this case: The consumer pool runs on Spot nodes, and the farm runs as Spot batches.
- **C:** Incorrect for this question. A multi-year commitment at a lower unit price. Why the correct answer wins: The consumer pool runs on Spot nodes, and the farm runs as Spot batches.
- **D:** Correct. A pool built from reclaimable capacity. In this case: The consumer pool runs on Spot nodes, and the farm runs as Spot batches.
- **E:** Incorrect for this question. Warm capacity that avoids cold starts. Why the correct answer wins: The consumer pool runs on Spot nodes, and the farm runs as Spot batches.

### Question 96 — C

Answer: Move the primary database onto Spot capacity. The write primary cannot live on reclaimable capacity. Reclaimable capacity under a stateful workload. Local study-map skill 5.4 (Spot Virtual Machines), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 5 (optimizing performance and cost): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Discounted capacity that can be reclaimed. Why the correct answer wins: The write primary cannot live on reclaimable capacity.
- **B:** Incorrect for this question. A multi-year commitment at a lower unit price. Why the correct answer wins: The write primary cannot live on reclaimable capacity.
- **C:** Correct. Reclaimable capacity under a stateful workload. In this case: The write primary cannot live on reclaimable capacity.
- **D:** Incorrect for this question. A pool built from reclaimable capacity. Why the correct answer wins: The write primary cannot live on reclaimable capacity.

### Question 97 — B

Answer: Buy a committed-use discount for the steady baseline. A commitment discounts the predictable baseline. A multi-year commitment at a lower unit price. Local study-map skill 5.5 (Infrastructure Cost Planning), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 5 (optimizing performance and cost): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A cheaper egress path with different performance. Why the correct answer wins: A commitment discounts the predictable baseline.
- **B:** Correct. A multi-year commitment at a lower unit price. In this case: A commitment discounts the predictable baseline.
- **C:** Incorrect for this question. An automatic discount that accrues with monthly use. Why the correct answer wins: A commitment discounts the predictable baseline.
- **D:** Incorrect for this question. Discounted capacity that can be reclaimed. Why the correct answer wins: A commitment discounts the predictable baseline.

### Question 98 — A

Answer: Serve the bulk export over the Standard network tier. The standard tier costs less for that copy. A cheaper egress path with different performance. Local study-map skill 5.5 (Infrastructure Cost Planning), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 5 (optimizing performance and cost): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Correct. A cheaper egress path with different performance. In this case: The standard tier costs less for that copy.
- **B:** Incorrect for this question. A pool built from reclaimable capacity. Why the correct answer wins: The standard tier costs less for that copy.
- **C:** Incorrect for this question. A lower-latency path for user-facing traffic. Why the correct answer wins: The standard tier costs less for that copy.
- **D:** Incorrect for this question. A multi-year commitment at a lower unit price. Why the correct answer wins: The standard tier costs less for that copy.

### Question 99 — A

Answer: Keep the minimum instance count at zero for the internal tool. A minimum of zero ends the idle bill. Scale to zero for a service nobody uses at night. Local study-map skill 5.6 (Workload-Level Cost Optimization), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 5 (optimizing performance and cost): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Correct. Scale to zero for a service nobody uses at night. In this case: A minimum of zero ends the idle bill.
- **B:** Incorrect for this question. A calendar action that removes idle spend. Why the correct answer wins: A minimum of zero ends the idle bill.
- **C:** Incorrect for this question. A pool sized against measured demand. Why the correct answer wins: A minimum of zero ends the idle bill.
- **D:** Incorrect for this question. Warm capacity that avoids cold starts. Why the correct answer wins: A minimum of zero ends the idle bill.

### Question 100 — A

Answer: Stop the idle non-production instances on a schedule. The scheduled stop removes the weekend spend. A calendar action that removes idle spend. Local study-map skill 5.6 (Workload-Level Cost Optimization), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 5 (optimizing performance and cost): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Correct. A calendar action that removes idle spend. In this case: The scheduled stop removes the weekend spend.
- **B:** Incorrect for this question. A pool sized against measured demand. Why the correct answer wins: The scheduled stop removes the weekend spend.
- **C:** Incorrect for this question. A multi-year commitment at a lower unit price. Why the correct answer wins: The scheduled stop removes the weekend spend.
- **D:** Incorrect for this question. Scale to zero for a service nobody uses at night. Why the correct answer wins: The scheduled stop removes the weekend spend.
