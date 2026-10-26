# Google Cloud Professional Cloud DevOps Engineer — Full-Length Mock Exam 1

Professional Cloud DevOps Engineer · 100 questions · expanded practice bank · passing score not published

Blueprint-weighted mock exam. Item mix: 84 multiple-choice and 16 multiple-select items (the selection count is stated in each multi-select stem). The live exam publishes 50-60 multiple-choice and multiple-select questions and has no case-study component, so this set is larger on purpose and no case-study item is reproduced. The live paper allows two hours for 50-60 items, so this 100-item set is a slower-per-item rehearsal: about 72 seconds per item here against roughly 120-144 seconds live. Use it to build a habit of finishing with time to review. See the README for the exact fidelity boundary.

Original educational content, not actual, recalled, or copied Google exam items.

## Questions

---

## Domain 1 — Bootstrapping and Maintaining a Google Cloud Organization (Hierarchy, Infrastructure as Code, and Pipeline Foundations)

### 1. A regulated bank must forbid public buckets in every project it will ever create, including subsidiaries added years later. What should the platform team do?

- A. Add an IAM deny policy for the sensitive permission
- B. Apply the constraint separately in each project
- C. Apply the constraint at the organization node
- D. Apply the constraint to the business unit folder

### 2. Each delivery team owns one service across staging and production, and reviewers must see that service's projects side by side. How should the hierarchy be organized?

- A. Apply the constraint separately in each project
- B. Apply the constraint to the business unit folder
- C. Group projects by environment with applications below
- D. Group projects by application inside each environment folder

### 3. Thirty service projects must consume subnets and firewall policy administered by a central network team. What fits?

- A. Give each project its own VPC and Cloud NAT
- B. Publish the service behind a Private Service Connect endpoint
- C. Create a Shared VPC host project and attach the service projects
- D. Peer every project VPC with every other project VPC

### 4. A partner publishes a service that must be consumed privately even though both networks use overlapping address ranges. What fits?

- A. Give each project its own VPC and Cloud NAT
- B. Publish the service behind a Private Service Connect endpoint
- C. Create a Shared VPC host project and attach the service projects
- D. Peer every project VPC with every other project VPC

### 5. Security needs one read-only destination to query audit entries from forty projects at once. What should be configured?

- A. Keep one log bucket inside each project
- B. Route every project log to one aggregated sink
- C. Route the entries to a Pub/Sub topic
- D. Add the projects to one metrics scope

### 6. An auditor requires a hard guardrail on resource location, and one sensitive permission must stay unusable even for project owners. Which two controls apply? Select two.

- A. Create one service account per environment
- B. Add an IAM deny policy for the sensitive permission
- C. Grant a custom role limited to the required permissions
- D. Grant a predefined role once at the folder
- E. Enforce the restriction with an organization policy constraint

### 7. A pipeline needs six specific permissions and no predefined role matches that set exactly. What should be created?

- A. Enforce the restriction with an organization policy constraint
- B. Add an IAM deny policy for the sensitive permission
- C. Grant a predefined role once at the folder
- D. Grant a custom role limited to the required permissions

### 8. A staging identity must never be able to act on production resources. What should be created first?

- A. Download a JSON key file for the service account
- B. Let the workload use the default Compute Engine service account
- C. Create one service account per workload
- D. Create one service account per environment

### 9. A contract forbids storing customer records outside the European Union. What should constrain the deployment?

- A. Apply the constraint at the organization node
- B. Create a Shared VPC host project and attach the service projects
- C. Place the resources in a region that satisfies the residency rule
- D. Replicate the data to a second region

### 10. Infrastructure must be reviewed as code before it is applied, and a Kubernetes-native team wants manifests to reconcile cloud resources. Which two approaches apply? Select two.

- A. Reconcile the resources with Config Connector
- B. Start from the Cloud Foundation Toolkit blueprints
- C. Package the workload as a Helm chart
- D. Define the estate as Terraform modules held in version control
- E. Apply the deployment through Infrastructure Manager

### 11. The same Terraform must run repeatably from a managed service that keeps its own state and audit trail. What fits?

- A. Apply the deployment through Infrastructure Manager
- B. Reconcile the resources with Config Connector
- C. Define the estate as Terraform modules held in version control
- D. Automate the repeated step with a Python script calling the API

### 12. A new landing zone should start from Google-maintained templates instead of hand-written modules. What should be used?

- A. Start from the Cloud Foundation Toolkit blueprints
- B. Package the workload as a Helm chart
- C. Render the manifests through a kpt function pipeline
- D. Schedule a plan that reports drift

### 13. A project-creation step runs hundreds of times a year and must produce the same result when repeated. What should the team write?

- A. Make the change in the console and note it in the wiki
- B. Run the documented gcloud commands by hand for each environment
- C. Schedule a plan that reports drift
- D. Automate the repeated step with a Python script calling the API

### 14. Builds must run as a managed service, and images must land in a regional repository that scans them. Which two should be adopted? Select two.

- A. Push the image to Container Registry
- B. Run Jenkins on a self-managed VM
- C. Store the build output in Artifact Registry
- D. Use Cloud Build for CI and Cloud Deploy for delivery
- E. Bake the machine image with Packer

### 15. A reviewer must see the tests run before any change is merged. What should be created?

- A. Create a Cloud Build trigger on the release branch
- B. Have an engineer build locally and upload the result
- C. Create a trigger that runs the tests on every pull request
- D. Trigger the pipeline only on a signed tag

### 16. A platform team wants the cluster to keep itself aligned with the Git repository it reads. What fits?

- A. Use Cloud Build for CI and Cloud Deploy for delivery
- B. Run Jenkins on a self-managed VM
- C. Bake the machine image with Packer
- D. Let Argo CD pull the manifests from Git

### 17. Staging and production differ only in replica count and one endpoint, and a single base must serve both. What fits?

- A. Bake the environment settings into the image
- B. Keep one shared staging environment for every team
- C. Keep one base with a Kustomize overlay per environment
- D. Create a short-lived project per change and delete it after review

### 18. Cluster upgrades must follow a managed cadence and land only inside a weekend window. What should be configured?

- A. Stand up a second cluster and shift traffic after verification
- B. Upgrade each node pool by hand whenever an operator is free
- C. Create a short-lived project per change and delete it after review
- D. Put the cluster on a release channel with a maintenance window

### 19. Contractors need a consistent IDE inside the project boundary with no laptop setup. What fits?

- A. Let each developer install the tools locally
- B. Rely on Cloud Shell for every developer
- C. Give developers Cloud Workstations built from a custom image
- D. Build a custom image that carries the approved toolchain

### 20. An engineer wants inline suggestions while editing a service in the editor. What fits?

- A. Ask Gemini Cloud Assist to explain the resource state
- B. Use Gemini Code Assist for the suggested change
- C. Let each developer install the tools locally
- D. Use Gemini CLI for the repetitive script

---

## Domain 2 — Building and Implementing CI/CD Pipelines (Delivery Pipelines and Software Supply Chain)

### 21. A release must start only after a version tag is pushed to the repository. What should be configured?

- A. Have an engineer build locally and upload the result
- B. Create a trigger that runs the tests on every pull request
- C. Create a Cloud Build trigger on the release branch
- D. Trigger the pipeline only on a signed tag

### 22. Every merge to the main branch must produce a new image automatically. What should be configured?

- A. Create a Cloud Build trigger on the release branch
- B. Create a trigger that runs the tests on every pull request
- C. Have an engineer build locally and upload the result
- D. Trigger the pipeline only on a signed tag

### 23. An auditor finds artifacts with no record of which commit produced them. Which practice explains the gap?

- A. Have an engineer build locally and upload the result
- B. Create a Cloud Build trigger on the release branch
- C. Create a trigger that runs the tests on every pull request
- D. Trigger the pipeline only on a signed tag

### 24. Each build must be traceable to a commit, and re-pushing an existing version must fail. Which two practices deliver that? Select two.

- A. Tag each artifact with the commit SHA and forbid overwrite
- B. Reuse the latest tag for every build
- C. Push the image to Container Registry
- D. Bake the machine image with Packer
- E. Store the build output in Artifact Registry

### 25. Operators cannot tell which build is running because the deployed reference never changes. Which practice caused that?

- A. Tag each artifact with the commit SHA and forbid overwrite
- B. Inspect the build provenance attestation
- C. Reuse the latest tag for every build
- D. Store the build output in Artifact Registry

### 26. A Cloud Deploy pipeline must release to a GKE cluster in the company data centre. What should the target be?

- A. Deliver to a Cloud Run service revision
- B. Define the attached cluster as the delivery target
- C. Add a Cloud Deploy approval gate before production
- D. Use a GKE cluster in the pipeline project as the target

### 27. A serverless service must be released as revisions with controlled traffic. What should the target be?

- A. Use a GKE cluster in the pipeline project as the target
- B. Read Cloud Audit Logs for the release history
- C. Deliver to a Cloud Run service revision
- D. Define the attached cluster as the delivery target

### 28. Promotion to production must wait for a named approver. What should be added?

- A. Add a Cloud Deploy approval gate before production
- B. Have an engineer build locally and upload the result
- C. Read Cloud Audit Logs for the release history
- D. Promote automatically to every target in the chain

### 29. An investigator needs who released what, and a reviewer needs proof of which inputs produced the artifact. Which two sources apply? Select two.

- A. Tag each artifact with the commit SHA and forbid overwrite
- B. Describe the build with its supply chain level and signed provenance
- C. Inspect the build provenance attestation
- D. Add a Cloud Deploy approval gate before production
- E. Read Cloud Audit Logs for the release history

### 30. A customer asks how the integrity of the build process is described in public. What should the team show?

- A. Enforce Binary Authorization attestations before deploy
- B. Inspect the build provenance attestation
- C. Describe the build with its supply chain level and signed provenance
- D. Read Cloud Audit Logs for the release history

### 31. Only ten percent of traffic may reach the new version, and the split must follow weights between versions. Which two fulfil that? Select two.

- A. Split traffic with a Cloud Service Mesh route
- B. Send ten percent of traffic to the new revision and watch the SLI
- C. Replace the instances in batches
- D. Stop the old version and then start the new one
- E. Run the new version alongside and switch traffic at once

### 32. The code must ship now, but the behaviour must stay dark until marketing approves. What fits?

- A. Put the behaviour behind a feature flag
- B. Send ten percent of traffic to the new revision and watch the SLI
- C. Stop the old version and then start the new one
- D. Run the new version alongside and switch traffic at once

### 33. A release takes the service completely offline for two minutes every time. Which strategy caused that?

- A. Send ten percent of traffic to the new revision and watch the SLI
- B. Replace the instances in batches
- C. Stop the old version and then start the new one
- D. Run the new version alongside and switch traffic at once

### 34. A rollout must stop automatically when user-facing success drops. What should gate it?

- A. Gate the rollout on average CPU alone
- B. Add a Cloud Deploy approval gate before production
- C. Gate the rollout on the error-rate SLI
- D. Inspect the build provenance attestation

### 35. A Cloud Build run fails and the engineer needs the first command that broke. Where should they look?

- A. Start from the failed step log in Cloud Build
- B. Read Cloud Audit Logs for the release history
- C. Make the failed step idempotent and re-run it
- D. Roll the release back to the previous one

### 36. A step created a resource before failing, and the run must be repeated safely. What should be done?

- A. Roll the release back to the previous one
- B. Make the failed step idempotent and re-run it
- C. Patch production by hand and reconcile later
- D. Start from the failed step log in Cloud Build

### 37. A payload must be encrypted with a key whose use is logged and rotated centrally. What fits?

- A. Store the credential in Secret Manager with versions
- B. Encrypt the payload with a Cloud KMS key
- C. Issue and rotate the certificate with Certificate Manager
- D. Commit the credential to the private repository

### 38. Dozens of public endpoints need certificates issued and renewed without tickets. What fits?

- A. Keep the non-secret configuration in Parameter Manager
- B. Issue and rotate the certificate with Certificate Manager
- C. Store the credential in Secret Manager with versions
- D. Encrypt the payload with a Cloud KMS key

### 39. A database password must be versioned, audited, and rotated without rebuilding the image. What fits?

- A. Keep the non-secret configuration in Parameter Manager
- B. Store the credential in Secret Manager with versions
- C. Pass the secret as a build argument
- D. Commit the credential to the private repository

### 40. Non-secret environment settings must be versioned and read at deploy time. What fits?

- A. Bake the environment settings into the image
- B. Store the credential in Secret Manager with versions
- C. Commit the credential to the private repository
- D. Keep the non-secret configuration in Parameter Manager

### 41. Anyone who can pull the image must not be able to read the credential. What should be done?

- A. Mount the secret at runtime from Secret Manager
- B. Commit the credential to the private repository
- C. Inject the secret at build time into the image layer
- D. Pass the secret as a build argument

### 42. A critical vulnerability must prevent promotion instead of appearing in a monthly report. What should be configured?

- A. Enable Artifact Analysis scanning on the repository
- B. Keep the scan report for the monthly review
- C. Fail the pipeline on a critical vulnerability finding
- D. Enforce Binary Authorization attestations before deploy

### 43. Only attested images may run in the cluster, and every stored image must be scanned for known vulnerabilities. Which two capabilities apply? Select two.

- A. Keep the scan report for the monthly review
- B. Fail the pipeline on a critical vulnerability finding
- C. Enable Artifact Analysis scanning on the repository
- D. Enforce Binary Authorization attestations before deploy
- E. Bind deploy permissions only inside the production project

### 44. A vulnerable image reached production even though the scan had already flagged it. Which practice explains that?

- A. Enforce Binary Authorization attestations before deploy
- B. Keep the scan report for the monthly review
- C. Fail the pipeline on a critical vulnerability finding
- D. Enable Artifact Analysis scanning on the repository

### 45. A compromised pipeline identity must not be able to release into production. What should be configured?

- A. Use one identity with deploy rights in every environment
- B. Run the pipeline as the default editor service account
- C. Download a JSON key file for the service account
- D. Bind deploy permissions only inside the production project

---

## Domain 3 — Applying Site Reliability Engineering Practices (Reliability Engineering in Practice)

### 46. The team must define what it measures and what target it commits to internally. Which two elements are those? Select two.

- A. Alert on a fast error-budget burn rate
- B. Publish a contractual promise with a remedy
- C. Register the service in the service catalog
- D. Track the ratio of good requests to total requests
- E. Set an internal target on that indicator

### 47. A customer contract promises a credit when availability falls below 99.9 percent. What is that promise?

- A. Track the ratio of good requests to total requests
- B. Alert on a fast error-budget burn rate
- C. Set an internal target on that indicator
- D. Publish a contractual promise with a remedy

### 48. A dashboard shows the share of requests answered successfully. What is that measure?

- A. Set an internal target on that indicator
- B. Publish a contractual promise with a remedy
- C. Track the ratio of good requests to total requests
- D. Alert on a fast error-budget burn rate

### 49. A policy must halt risky releases when the reliability allowance is gone, and page before the month's allowance runs out. Which two mechanisms apply? Select two.

- A. Choose three nines and spend the difference on features
- B. Alert on a fast error-budget burn rate
- C. Stop feature releases when the error budget is spent
- D. Assume five nines for every service
- E. Publish a contractual promise with a remedy

### 50. Leadership wants feature work paused whenever the service has used up its reliability allowance. What enforces that?

- A. Alert on a fast error-budget burn rate
- B. Assume five nines for every service
- C. Stop feature releases when the error budget is spent
- D. Publish a contractual promise with a remedy

### 51. A team argues for a modest availability target so features keep shipping. Which position is that?

- A. Choose three nines and spend the difference on features
- B. Publish a contractual promise with a remedy
- C. Assume five nines for every service
- D. Stop feature releases when the error budget is spent

### 52. A design demands the same extreme availability for an internal report that staff open weekly. What is the flaw?

- A. Choose three nines and spend the difference on features
- B. Assume five nines for every service
- C. Publish a contractual promise with a remedy
- D. Register the service in the service catalog

### 53. Nobody can say who owns a service or what it depends on. What should be created?

- A. Request a quota increase and reserve capacity before the launch
- B. Register the service in the service catalog
- C. Announce the retirement date and withdraw traffic gradually
- D. Leave the unused service running for now

### 54. A service is being replaced next quarter and its traffic must taper away safely. What should be planned?

- A. Announce the retirement date and withdraw traffic gradually
- B. Leave the unused service running for now
- C. Add capacity in a second region
- D. Register the service in the service catalog

### 55. A launch will triple consumption of a limited regional resource. What should be arranged first?

- A. Schedule the batch with Dynamic Workload Scheduler
- B. Add capacity on a fixed calendar schedule
- C. Assume the default quota will absorb the launch
- D. Request a quota increase and reserve capacity before the launch

### 56. A nightly batch is flexible about when it starts and wants the cheapest window. What fits?

- A. Add capacity on a fixed calendar schedule
- B. Request a quota increase and reserve capacity before the launch
- C. Schedule the batch with Dynamic Workload Scheduler
- D. Put the instance group behind an autoscaler on CPU

### 57. A worker fleet must grow with the work waiting, and a serverless API must grow with concurrent requests. Which two settings apply? Select two.

- A. Add capacity on a fixed calendar schedule
- B. Assume the default quota will absorb the launch
- C. Set Cloud Run concurrency so replicas follow load
- D. Put the instance group behind an autoscaler on CPU
- E. Scale on queue depth with a horizontal pod autoscaler

### 58. A group of identical web servers must grow as CPU rises. What fits?

- A. Put the instance group behind an autoscaler on CPU
- B. Add capacity on a fixed calendar schedule
- C. Scale on queue depth with a horizontal pod autoscaler
- D. Schedule the batch with Dynamic Workload Scheduler

### 59. A node must be removed without dropping the requests already in flight. What must happen first?

- A. Drain connections before removing the instance
- B. Add capacity in a second region
- C. Shift traffic with a DNS routing policy
- D. Use a load balancer failover backend

### 60. A regional backend is failing and traffic must move without waiting for DNS to expire. What fits?

- A. Shift traffic with a DNS routing policy
- B. Add capacity in a second region
- C. Drain connections before removing the instance
- D. Use a load balancer failover backend

### 61. An incident has saturated the primary region and supply must be added elsewhere. What should be done?

- A. Request a quota increase and reserve capacity before the launch
- B. Add capacity in a second region
- C. Drain connections before removing the instance
- D. Use a load balancer failover backend

### 62. A new build misbehaves and an identical earlier image is known to be good. What is the fastest safe action?

- A. Redeploy the previous image to the affected service
- B. Wait for the error rate to settle on its own
- C. Patch production by hand and reconcile later
- D. Reverse the schema change with a tested down migration

### 63. A schema change broke reads and the earlier image cannot read the new schema. What should have existed?

- A. Reverse the schema change with a tested down migration
- B. Wait for the error rate to settle on its own
- C. Patch production by hand and reconcile later
- D. Redeploy the previous image to the affected service

---

## Domain 4 — Implementing Observability Practices and Troubleshooting (Telemetry, Alerting, and Diagnosis)

### 64. A VM fleet must ship system logs, and the network team needs connection records from a subnet. Which two sources apply? Select two.

- A. Turn on VPC Flow Logs for the subnet
- B. Install the Ops Agent on the instances
- C. Read the Cloud Service Mesh telemetry
- D. Run an OpenTelemetry Collector in the cluster
- E. Enable Data Access audit logs for the service

### 65. Traces must be emitted in a vendor-neutral way from the cluster. What fits?

- A. Install the Ops Agent on the instances
- B. Read the Cloud Service Mesh telemetry
- C. Run an OpenTelemetry Collector in the cluster
- D. Enable Data Access audit logs for the service

### 66. A load balancer floods the log with probe entries, and debug output dwarfs every other entry. Which two optimisations apply? Select two.

- A. Set the log bucket retention and lock it
- B. Add an exclusion for the health-check entries
- C. Sample the high-volume debug entries
- D. Enable Data Access audit logs for the service
- E. Route the entries to a BigQuery dataset

### 67. A metric label holding a user identifier explodes the stored series and the bill. What should be done?

- A. Measure log volume per service before choosing a retention period
- B. Drop the high-cardinality user label from the metric
- C. Add an exclusion for the health-check entries
- D. Sample the high-volume debug entries

### 68. An engineer needs only the entries whose resource label matches one service. What should be used?

- A. Filter with the Logging query language on the resource label
- B. Open the Logs Explorer and pivot from the error entry
- C. Create a log-based metric for the error string
- D. Route the entries to a Cloud Storage bucket

### 69. An engineer has one error entry and wants every related entry around it. What fits?

- A. Filter with the Logging query language on the resource label
- B. Create a log-based metric for the error string
- C. Open the Logs Explorer and pivot from the error entry
- D. Create an uptime check against the login flow

### 70. Analysts must join audit entries with business tables using SQL. What should the sink target?

- A. Set the log bucket retention and lock it
- B. Route the entries to a Cloud Storage bucket
- C. Route the entries to a Pub/Sub topic
- D. Route the entries to a BigQuery dataset

### 71. A regulator requires that the retention period cannot be shortened even by an administrator. What fits?

- A. Set the log bucket retention and lock it
- B. Measure log volume per service before choosing a retention period
- C. Route the entries to a Cloud Storage bucket
- D. Route the entries to a Pub/Sub topic

### 72. Log entries contain email addresses that must never be stored at all. What should be configured?

- A. Add an exclusion for the health-check entries
- B. Ask analysts not to read the sensitive field
- C. Sample the high-volume debug entries
- D. Redact the email field with a log processor

### 73. An on-call engineer wants the failing entries explained in plain language. What fits?

- A. Filter with the Logging query language on the resource label
- B. Ask Gemini Cloud Assist to summarise the failing entries
- C. Open the Logs Explorer and pivot from the error entry
- D. Ask Gemini Cloud Assist to explain the metric spike

### 74. A workload already exposes a Prometheus endpoint that must be scraped without running a server. What fits?

- A. Run an OpenTelemetry Collector in the cluster
- B. Scrape the workload with managed collection for Prometheus
- C. Create a log-based metric for the error string
- D. Emit a custom metric for the business event

### 75. Business events such as completed orders must appear as measurements. What should the application do?

- A. Scrape the workload with managed collection for Prometheus
- B. Emit a custom metric for the business event
- C. Create an uptime check against the login flow
- D. Create a log-based metric for the error string

### 76. A count is needed for an error string already present in the logs, and no code change is possible. What fits?

- A. Create a log-based metric for the error string
- B. Create an uptime check against the login flow
- C. Scrape the workload with managed collection for Prometheus
- D. Emit a custom metric for the business event

### 77. A login flow must be exercised from outside the project every minute. What fits?

- A. Scrape the workload with managed collection for Prometheus
- B. Create a log-based metric for the error string
- C. Create an uptime check against the login flow
- D. Emit a custom metric for the business event

### 78. Fifty responders need the same filtered view of the key signals. What should be built?

- A. Create an uptime check against the login flow
- B. Attach the remediation playbook to the alert
- C. Alert when CPU stays above ninety percent for ten minutes
- D. Build one dashboard and share it with the on-call rotation

### 79. A responder should see the remediation steps at the moment the alert fires. What fits?

- A. Build one dashboard and share it with the on-call rotation
- B. Send the alert to PagerDuty through a webhook
- C. Attach the remediation playbook to the alert
- D. Alert when CPU stays above ninety percent for ten minutes

### 80. Paging must follow the service objective, and the notification must reach the paging tool. Which two should be configured? Select two.

- A. Add an email notification channel for the on-call group
- B. Send the alert to PagerDuty through a webhook
- C. Attach the remediation playbook to the alert
- D. Create an alerting policy on the SLO burn rate
- E. Alert when CPU stays above ninety percent for ten minutes

### 81. Pages fire whenever CPU is high although users are unaffected, and real slowdowns are missed. Which policy is at fault?

- A. Create an uptime check against the login flow
- B. Create an alerting policy on the SLO burn rate
- C. Send the alert to PagerDuty through a webhook
- D. Alert when CPU stays above ninety percent for ten minutes

### 82. The on-call group wants a written record of every alert in a shared inbox. What fits?

- A. Alert when CPU stays above ninety percent for ten minutes
- B. Attach the remediation playbook to the alert
- C. Add an email notification channel for the on-call group
- D. Send the alert to PagerDuty through a webhook

### 83. Each request must emit timing for its downstream calls, and its logs must be joinable to those traces. Which two practices apply? Select two.

- A. Ask Gemini Cloud Assist which span dominates the trace
- B. Instrument the service with OpenTelemetry spans
- C. Read the trace waterfall to find the slow span
- D. Log a timestamp and correlate by eye later
- E. Put the trace ID in the structured log line

### 84. An engineer needs to see which downstream call consumed most of a slow request. What fits?

- A. Read the trace waterfall to find the slow span
- B. Instrument the service with OpenTelemetry spans
- C. Put the trace ID in the structured log line
- D. Ask Gemini Cloud Assist which span dominates the trace

### 85. A reviewer asks which span dominates a long trace and wants that stated rather than plotted. What fits?

- A. Read the trace waterfall to find the slow span
- B. Put the trace ID in the structured log line
- C. Instrument the service with OpenTelemetry spans
- D. Ask Gemini Cloud Assist which span dominates the trace

### 86. Pods stay in ImagePullBackOff after the team moved to a new repository. What should be checked first?

- A. Check Cloud NAT port exhaustion for the egress range
- B. Read the firewall rule that hit the denied flow
- C. Check the quota error in the deployment log
- D. Inspect the image pull credential and repository permission

### 87. A new revision restarts before it ever serves traffic, and its log shows a slow startup. What should be checked?

- A. Check the DNS record and its remaining TTL
- B. Compare the readiness probe with the application startup time
- C. Check Cloud NAT port exhaustion for the egress range
- D. Profile the slow endpoint inside the application

### 88. Outbound calls from many pods fail intermittently while inbound traffic is healthy. What should be checked?

- A. Check Cloud NAT port exhaustion for the egress range
- B. Check the quota error in the deployment log
- C. Read the firewall rule that hit the denied flow
- D. Inspect the image pull credential and repository permission

---

## Domain 5 — Optimizing Performance and Cost (FinOps and Performance Tuning)

### 89. A team must show which endpoint became slower after a release. What should be used?

- A. Measure request latency by endpoint in Cloud Monitoring
- B. Export billing data to BigQuery for the chargeback report
- C. Measure log volume per service before choosing a retention period
- D. Move the primary database onto Spot capacity

### 90. An operator wants each service's objective visible on one page. What fits?

- A. Right-size the node pool from the observed requests
- B. Apply the cost recommender suggestion for the idle disks
- C. Track the service objective on a shared dashboard
- D. Measure log volume per service before choosing a retention period

### 91. Finance wants idle spend found, and engineering wants the recommendation that improves resilience. Which two should be reviewed? Select two.

- A. Export billing data to BigQuery for the chargeback report
- B. Apply the reliability recommender for the missing quota
- C. Apply the cost recommender suggestion for the idle disks
- D. Move the primary database onto Spot capacity
- E. Review the Active Assist recommendations for the project

### 92. A service keeps failing during peaks because a limit was never raised. Which recommendation addresses that?

- A. Apply the cost recommender suggestion for the idle disks
- B. Move the primary database onto Spot capacity
- C. Review the Active Assist recommendations for the project
- D. Apply the reliability recommender for the missing quota

### 93. Before choosing a retention period, the team must know how much it would store. What should it do first?

- A. Serve the bulk export over the Standard network tier
- B. Measure log volume per service before choosing a retention period
- C. Exclude the debug stream and keep the error stream
- D. Drop the high-cardinality user label from the metric

### 94. Debug entries dominate ingest while error entries are the only ones anyone reads. What should be done?

- A. Drop the high-cardinality user label from the metric
- B. Exclude the debug stream and keep the error stream
- C. Set the log bucket retention and lock it
- D. Measure log volume per service before choosing a retention period

### 95. Stateless workers can restart at any time and are the largest compute cost. What fits?

- A. Buy a committed-use discount for the steady baseline
- B. Put the stateless workers on a Spot node pool
- C. Move the primary database onto Spot capacity
- D. Set a minimum instance count for the latency-critical service

### 96. A design proposes running the primary transactional database on reclaimable capacity. What is the risk?

- A. Buy a committed-use discount for the steady baseline
- B. Move the primary database onto Spot capacity
- C. Run the batch on Spot VMs
- D. Put the stateless workers on a Spot node pool

### 97. A steady baseline runs all year, and a bulk export can trade latency for a cheaper path. Which two choices apply? Select two.

- A. Rely on sustained-use discounts for the steady baseline
- B. Run the batch on Spot VMs
- C. Keep the interactive traffic on the Premium tier
- D. Serve the bulk export over the Standard network tier
- E. Buy a committed-use discount for the steady baseline

### 98. Interactive traffic needs the lowest latency between continents. What fits?

- A. Run the batch on Spot VMs
- B. Buy a committed-use discount for the steady baseline
- C. Serve the bulk export over the Standard network tier
- D. Keep the interactive traffic on the Premium tier

### 99. A node pool reserves four times the CPU its pods ever request. What should be done?

- A. Put the stateless workers on a Spot node pool
- B. Keep the minimum instance count at zero for the internal tool
- C. Set a minimum instance count for the latency-critical service
- D. Right-size the node pool from the observed requests

### 100. An internal tool is unused outside office hours and must cost nothing then. What fits?

- A. Keep the minimum instance count at zero for the internal tool
- B. Stop the idle non-production instances on a schedule
- C. Set a minimum instance count for the latency-critical service
- D. Right-size the node pool from the observed requests

---

## Answer key and explanations

### Question 1 — C

Answer: Apply the constraint at the organization node. An organization-level constraint reaches every current and future project. An organization-level constraint that every folder and project inherits. Local study-map skill 1.1 (Resource Hierarchy and Project Organization), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 1 (bootstrapping and maintaining a Google Cloud organization): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. An explicit denial that overrides any allow. Why the correct answer wins: An organization-level constraint reaches every current and future project.
- **B:** Incorrect for this question. A constraint set per project with no inheritance. Why the correct answer wins: An organization-level constraint reaches every current and future project.
- **C:** Correct. An organization-level constraint that every folder and project inherits. In this case: An organization-level constraint reaches every current and future project.
- **D:** Incorrect for this question. A constraint attached to one folder and inherited by its projects. Why the correct answer wins: An organization-level constraint reaches every current and future project.

### Question 2 — D

Answer: Group projects by application inside each environment folder. An application-centric layout keeps one service and its owners together. Local study-map skill 1.1 (Resource Hierarchy and Project Organization), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 1 (bootstrapping and maintaining a Google Cloud organization): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A constraint set per project with no inheritance. Why the correct answer wins: An application-centric layout keeps one service and its owners together.
- **B:** Incorrect for this question. A constraint attached to one folder and inherited by its projects. Why the correct answer wins: An application-centric layout keeps one service and its owners together.
- **C:** Incorrect for this question. An environment-centric layout that separates production from staging first. Why the correct answer wins: An application-centric layout keeps one service and its owners together.
- **D:** Correct. In this case: An application-centric layout keeps one service and its owners together.

### Question 3 — C

Answer: Create a Shared VPC host project and attach the service projects. A Shared VPC host project lends centrally managed subnets to services. A central network project that lends subnets to other projects. Local study-map skill 1.2 (Shared Networking for Multi-Project Estates), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 1 (bootstrapping and maintaining a Google Cloud organization): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Duplicate networks with a separately managed egress path. Why the correct answer wins: A Shared VPC host project lends centrally managed subnets to services.
- **B:** Incorrect for this question. A private endpoint that consumes a published service. Why the correct answer wins: A Shared VPC host project lends centrally managed subnets to services.
- **C:** Correct. A central network project that lends subnets to other projects. In this case: A Shared VPC host project lends centrally managed subnets to services.
- **D:** Incorrect for this question. A mesh of peering links that grows with each new project. Why the correct answer wins: A Shared VPC host project lends centrally managed subnets to services.

### Question 4 — B

Answer: Publish the service behind a Private Service Connect endpoint. Private Service Connect consumes a published service without address overlap. A private endpoint that consumes a published service. Local study-map skill 1.2 (Shared Networking for Multi-Project Estates), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 1 (bootstrapping and maintaining a Google Cloud organization): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Duplicate networks with a separately managed egress path. Why the correct answer wins: Private Service Connect consumes a published service without address overlap.
- **B:** Correct. A private endpoint that consumes a published service. In this case: Private Service Connect consumes a published service without address overlap.
- **C:** Incorrect for this question. A central network project that lends subnets to other projects. Why the correct answer wins: Private Service Connect consumes a published service without address overlap.
- **D:** Incorrect for this question. A mesh of peering links that grows with each new project. Why the correct answer wins: Private Service Connect consumes a published service without address overlap.

### Question 5 — B

Answer: Route every project log to one aggregated sink. An aggregated sink collects entries from many projects into one destination. A single destination that collects entries from many projects. Local study-map skill 1.3 (Multi-Project Monitoring and Logging), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 1 (bootstrapping and maintaining a Google Cloud organization): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Log storage scoped to the project that produced the entries. Why the correct answer wins: An aggregated sink collects entries from many projects into one destination.
- **B:** Correct. A single destination that collects entries from many projects. In this case: An aggregated sink collects entries from many projects into one destination.
- **C:** Incorrect for this question. A sink that streams entries to another consumer. Why the correct answer wins: An aggregated sink collects entries from many projects into one destination.
- **D:** Incorrect for this question. An observability scope that spans several projects. Why the correct answer wins: An aggregated sink collects entries from many projects into one destination.

### Question 6 — B, E

Answers: Enforce the restriction with an organization policy constraint; Add an IAM deny policy for the sensitive permission. The org policy constrains the resource, and the deny policy overrides allows. A guardrail that holds regardless of the IAM grants. An explicit denial that overrides any allow. Local study-map skill 1.4 (IAM Roles and Organization Policies), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 1 (bootstrapping and maintaining a Google Cloud organization): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Separate identities so a staging credential cannot act in production. Why the correct answer wins: The org policy constrains the resource, and the deny policy overrides allows.
- **B:** Correct. An explicit denial that overrides any allow. In this case: The org policy constrains the resource, and the deny policy overrides allows.
- **C:** Incorrect for this question. A role defined from an explicit permission list. Why the correct answer wins: The org policy constrains the resource, and the deny policy overrides allows.
- **D:** Incorrect for this question. A Google-managed role bound at folder level. Why the correct answer wins: The org policy constrains the resource, and the deny policy overrides allows.
- **E:** Correct. A guardrail that holds regardless of the IAM grants. In this case: The org policy constrains the resource, and the deny policy overrides allows.

### Question 7 — D

Answer: Grant a custom role limited to the required permissions. A custom role lists exactly the permissions the pipeline needs. A role defined from an explicit permission list. Local study-map skill 1.4 (IAM Roles and Organization Policies), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 1 (bootstrapping and maintaining a Google Cloud organization): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A guardrail that holds regardless of the IAM grants. Why the correct answer wins: A custom role lists exactly the permissions the pipeline needs.
- **B:** Incorrect for this question. An explicit denial that overrides any allow. Why the correct answer wins: A custom role lists exactly the permissions the pipeline needs.
- **C:** Incorrect for this question. A Google-managed role bound at folder level. Why the correct answer wins: A custom role lists exactly the permissions the pipeline needs.
- **D:** Correct. A role defined from an explicit permission list. In this case: A custom role lists exactly the permissions the pipeline needs.

### Question 8 — D

Answer: Create one service account per environment. One service account per environment blocks cross-environment action. Separate identities so a staging credential cannot act in production. Local study-map skill 1.5 (Service Account Management), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 1 (bootstrapping and maintaining a Google Cloud organization): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A long-lived credential stored outside the platform. Why the correct answer wins: One service account per environment blocks cross-environment action.
- **B:** Incorrect for this question. The account created automatically with broad project access. Why the correct answer wins: One service account per environment blocks cross-environment action.
- **C:** Incorrect for this question. A dedicated identity for each deployed workload. Why the correct answer wins: One service account per environment blocks cross-environment action.
- **D:** Correct. Separate identities so a staging credential cannot act in production. In this case: One service account per environment blocks cross-environment action.

### Question 9 — C

Answer: Place the resources in a region that satisfies the residency rule. The location of the resources must satisfy the residency clause. A location choice that keeps data inside the required boundary. Local study-map skill 1.6 (Data Residency in the Hierarchy), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 1 (bootstrapping and maintaining a Google Cloud organization): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. An organization-level constraint that every folder and project inherits. Why the correct answer wins: The location of the resources must satisfy the residency clause.
- **B:** Incorrect for this question. A central network project that lends subnets to other projects. Why the correct answer wins: The location of the resources must satisfy the residency clause.
- **C:** Correct. A location choice that keeps data inside the required boundary. In this case: The location of the resources must satisfy the residency clause.
- **D:** Incorrect for this question. A copy held elsewhere for recovery rather than residency. Why the correct answer wins: The location of the resources must satisfy the residency clause.

### Question 10 — A, D

Answers: Define the estate as Terraform modules held in version control; Reconcile the resources with Config Connector. Terraform modules are reviewed as code, and Config Connector reconciles manifests. Declarative code that is reviewed before it is applied. A controller that keeps Kubernetes manifests and cloud resources aligned. Local study-map skill 1.7 (Infrastructure-as-Code Tool Selection), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 1 (bootstrapping and maintaining a Google Cloud organization): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Correct. A controller that keeps Kubernetes manifests and cloud resources aligned. In this case: Terraform modules are reviewed as code, and Config Connector reconciles manifests.
- **B:** Incorrect for this question. Google-maintained Terraform templates for common foundations. Why the correct answer wins: Terraform modules are reviewed as code, and Config Connector reconciles manifests.
- **C:** Incorrect for this question. A templated bundle of Kubernetes resources. Why the correct answer wins: Terraform modules are reviewed as code, and Config Connector reconciles manifests.
- **D:** Correct. Declarative code that is reviewed before it is applied. In this case: Terraform modules are reviewed as code, and Config Connector reconciles manifests.
- **E:** Incorrect for this question. A managed service that runs Terraform deployments. Why the correct answer wins: Terraform modules are reviewed as code, and Config Connector reconciles manifests.

### Question 11 — A

Answer: Apply the deployment through Infrastructure Manager. Infrastructure Manager runs the deployment as a managed service. A managed service that runs Terraform deployments. Local study-map skill 1.7 (Infrastructure-as-Code Tool Selection), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 1 (bootstrapping and maintaining a Google Cloud organization): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Correct. A managed service that runs Terraform deployments. In this case: Infrastructure Manager runs the deployment as a managed service.
- **B:** Incorrect for this question. A controller that keeps Kubernetes manifests and cloud resources aligned. Why the correct answer wins: Infrastructure Manager runs the deployment as a managed service.
- **C:** Incorrect for this question. Declarative code that is reviewed before it is applied. Why the correct answer wins: Infrastructure Manager runs the deployment as a managed service.
- **D:** Incorrect for this question. Idempotent automation through the client library. Why the correct answer wins: Infrastructure Manager runs the deployment as a managed service.

### Question 12 — A

Answer: Start from the Cloud Foundation Toolkit blueprints. The Cloud Foundation Toolkit supplies maintained foundation blueprints. Google-maintained Terraform templates for common foundations. Local study-map skill 1.8 (Blueprints and Controlled Infrastructure Change), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 1 (bootstrapping and maintaining a Google Cloud organization): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Correct. Google-maintained Terraform templates for common foundations. In this case: The Cloud Foundation Toolkit supplies maintained foundation blueprints.
- **B:** Incorrect for this question. A templated bundle of Kubernetes resources. Why the correct answer wins: The Cloud Foundation Toolkit supplies maintained foundation blueprints.
- **C:** Incorrect for this question. A transformation pipeline that keeps the source declarative. Why the correct answer wins: The Cloud Foundation Toolkit supplies maintained foundation blueprints.
- **D:** Incorrect for this question. A recurring comparison of declared and actual state. Why the correct answer wins: The Cloud Foundation Toolkit supplies maintained foundation blueprints.

### Question 13 — D

Answer: Automate the repeated step with a Python script calling the API. A script calling the API repeats safely and identically. Idempotent automation through the client library. Local study-map skill 1.9 (Automation with Scripting and APIs), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 1 (bootstrapping and maintaining a Google Cloud organization): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. An unmanaged change with no enforceable record. Why the correct answer wins: A script calling the API repeats safely and identically.
- **B:** Incorrect for this question. A manual sequence repeated on every occasion. Why the correct answer wins: A script calling the API repeats safely and identically.
- **C:** Incorrect for this question. A recurring comparison of declared and actual state. Why the correct answer wins: A script calling the API repeats safely and identically.
- **D:** Correct. Idempotent automation through the client library. In this case: A script calling the API repeats safely and identically.

### Question 14 — C, D

Answers: Use Cloud Build for CI and Cloud Deploy for delivery; Store the build output in Artifact Registry. Cloud Build runs the build, and Artifact Registry stores the images. A managed pair that separates building from releasing. A regional repository for images and packages. Local study-map skill 1.10 (CI/CD Architecture Stack Design), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 1 (bootstrapping and maintaining a Google Cloud organization): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. The legacy registry without regional repository controls. Why the correct answer wins: Cloud Build runs the build, and Artifact Registry stores the images.
- **B:** Incorrect for this question. A self-operated CI server whose patching is your problem. Why the correct answer wins: Cloud Build runs the build, and Artifact Registry stores the images.
- **C:** Correct. A regional repository for images and packages. In this case: Cloud Build runs the build, and Artifact Registry stores the images.
- **D:** Correct. A managed pair that separates building from releasing. In this case: Cloud Build runs the build, and Artifact Registry stores the images.
- **E:** Incorrect for this question. A reproducible image built before deployment. Why the correct answer wins: Cloud Build runs the build, and Artifact Registry stores the images.

### Question 15 — C

Answer: Create a trigger that runs the tests on every pull request. A trigger on pull requests runs the tests before merge. A pre-merge check that blocks a bad change early. Local study-map skill 1.10 (CI/CD Architecture Stack Design), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 1 (bootstrapping and maintaining a Google Cloud organization): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A trigger that starts the build on a branch change. Why the correct answer wins: A trigger on pull requests runs the tests before merge.
- **B:** Incorrect for this question. A hand-built artifact with no pipeline record. Why the correct answer wins: A trigger on pull requests runs the tests before merge.
- **C:** Correct. A pre-merge check that blocks a bad change early. In this case: A trigger on pull requests runs the tests before merge.
- **D:** Incorrect for this question. A release build that a tag alone can start. Why the correct answer wins: A trigger on pull requests runs the tests before merge.

### Question 16 — D

Answer: Let Argo CD pull the manifests from Git. Argo CD pulls the manifests and reconciles the cluster state. A pull-based delivery controller. Local study-map skill 1.11 (Third-Party Tooling in the Pipeline), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 1 (bootstrapping and maintaining a Google Cloud organization): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A managed pair that separates building from releasing. Why the correct answer wins: Argo CD pulls the manifests and reconciles the cluster state.
- **B:** Incorrect for this question. A self-operated CI server whose patching is your problem. Why the correct answer wins: Argo CD pulls the manifests and reconciles the cluster state.
- **C:** Incorrect for this question. A reproducible image built before deployment. Why the correct answer wins: Argo CD pulls the manifests and reconciles the cluster state.
- **D:** Correct. A pull-based delivery controller. In this case: Argo CD pulls the manifests and reconciles the cluster state.

### Question 17 — C

Answer: Keep one base with a Kustomize overlay per environment. A Kustomize overlay patches one base for each environment. A base manifest with per-environment patches. Local study-map skill 1.12 (Multiple Environment Management), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 1 (bootstrapping and maintaining a Google Cloud organization): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. One image per environment with the settings compiled in. Why the correct answer wins: A Kustomize overlay patches one base for each environment.
- **B:** Incorrect for this question. A permanent pre-production environment. Why the correct answer wins: A Kustomize overlay patches one base for each environment.
- **C:** Correct. A base manifest with per-environment patches. In this case: A Kustomize overlay patches one base for each environment.
- **D:** Incorrect for this question. An environment that exists only while a change is tested. Why the correct answer wins: A Kustomize overlay patches one base for each environment.

### Question 18 — D

Answer: Put the cluster on a release channel with a maintenance window. A release channel with a maintenance window sets the cadence. A managed upgrade cadence inside a chosen window. Local study-map skill 1.13 (Fleets, Patching, and Cluster Upgrades), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 1 (bootstrapping and maintaining a Google Cloud organization): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A parallel cluster used to prove the upgrade. Why the correct answer wins: A release channel with a maintenance window sets the cadence.
- **B:** Incorrect for this question. An operator-driven upgrade with no cadence. Why the correct answer wins: A release channel with a maintenance window sets the cadence.
- **C:** Incorrect for this question. An environment that exists only while a change is tested. Why the correct answer wins: A release channel with a maintenance window sets the cadence.
- **D:** Correct. A managed upgrade cadence inside a chosen window. In this case: A release channel with a maintenance window sets the cadence.

### Question 19 — C

Answer: Give developers Cloud Workstations built from a custom image. Cloud Workstations runs the managed IDE inside the project boundary. Local study-map skill 1.14 (Secure Development Environments and AI Assistance), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 1 (bootstrapping and maintaining a Google Cloud organization): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Unmanaged toolchains on unmanaged machines. Why the correct answer wins: Cloud Workstations runs the managed IDE inside the project boundary.
- **B:** Incorrect for this question. A browser terminal with limited tooling and lifetime. Why the correct answer wins: Cloud Workstations runs the managed IDE inside the project boundary.
- **C:** Correct. In this case: Cloud Workstations runs the managed IDE inside the project boundary.
- **D:** Incorrect for this question. A pinned toolchain that every workstation starts from. Why the correct answer wins: Cloud Workstations runs the managed IDE inside the project boundary.

### Question 20 — B

Answer: Use Gemini Code Assist for the suggested change. Gemini Code Assist suggests code inside the editor. An in-editor assistant that proposes code. Local study-map skill 1.14 (Secure Development Environments and AI Assistance), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 1 (bootstrapping and maintaining a Google Cloud organization): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. An assistant that reads telemetry and configuration. Why the correct answer wins: Gemini Code Assist suggests code inside the editor.
- **B:** Correct. An in-editor assistant that proposes code. In this case: Gemini Code Assist suggests code inside the editor.
- **C:** Incorrect for this question. Unmanaged toolchains on unmanaged machines. Why the correct answer wins: Gemini Code Assist suggests code inside the editor.
- **D:** Incorrect for this question. A terminal assistant that drafts and runs commands. Why the correct answer wins: Gemini Code Assist suggests code inside the editor.

### Question 21 — D

Answer: Trigger the pipeline only on a signed tag. A tag trigger starts the release build. A release build that a tag alone can start. Local study-map skill 2.1 (Pipeline Triggers and Design), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 2 (building and implementing CI/CD pipelines): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A hand-built artifact with no pipeline record. Why the correct answer wins: A tag trigger starts the release build.
- **B:** Incorrect for this question. A pre-merge check that blocks a bad change early. Why the correct answer wins: A tag trigger starts the release build.
- **C:** Incorrect for this question. A trigger that starts the build on a branch change. Why the correct answer wins: A tag trigger starts the release build.
- **D:** Correct. A release build that a tag alone can start. In this case: A tag trigger starts the release build.

### Question 22 — A

Answer: Create a Cloud Build trigger on the release branch. A branch trigger builds on each merge to that branch. A trigger that starts the build on a branch change. Local study-map skill 2.1 (Pipeline Triggers and Design), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 2 (building and implementing CI/CD pipelines): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Correct. A trigger that starts the build on a branch change. In this case: A branch trigger builds on each merge to that branch.
- **B:** Incorrect for this question. A pre-merge check that blocks a bad change early. Why the correct answer wins: A branch trigger builds on each merge to that branch.
- **C:** Incorrect for this question. A hand-built artifact with no pipeline record. Why the correct answer wins: A branch trigger builds on each merge to that branch.
- **D:** Incorrect for this question. A release build that a tag alone can start. Why the correct answer wins: A branch trigger builds on each merge to that branch.

### Question 23 — A

Answer: Have an engineer build locally and upload the result. A local build leaves no pipeline record of its inputs. A hand-built artifact with no pipeline record. Local study-map skill 2.1 (Pipeline Triggers and Design), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 2 (building and implementing CI/CD pipelines): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Correct. A hand-built artifact with no pipeline record. In this case: A local build leaves no pipeline record of its inputs.
- **B:** Incorrect for this question. A trigger that starts the build on a branch change. Why the correct answer wins: A local build leaves no pipeline record of its inputs.
- **C:** Incorrect for this question. A pre-merge check that blocks a bad change early. Why the correct answer wins: A local build leaves no pipeline record of its inputs.
- **D:** Incorrect for this question. A release build that a tag alone can start. Why the correct answer wins: A local build leaves no pipeline record of its inputs.

### Question 24 — A, E

Answers: Store the build output in Artifact Registry; Tag each artifact with the commit SHA and forbid overwrite. Artifact Registry stores the image, and an immutable tag blocks re-push. A regional repository for images and packages. An immutable tag that identifies the source revision. Local study-map skill 2.2 (Artifact Management), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 2 (building and implementing CI/CD pipelines): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Correct. An immutable tag that identifies the source revision. In this case: Artifact Registry stores the image, and an immutable tag blocks re-push.
- **B:** Incorrect for this question. A moving tag that hides which build is running. Why the correct answer wins: Artifact Registry stores the image, and an immutable tag blocks re-push.
- **C:** Incorrect for this question. The legacy registry without regional repository controls. Why the correct answer wins: Artifact Registry stores the image, and an immutable tag blocks re-push.
- **D:** Incorrect for this question. A reproducible image built before deployment. Why the correct answer wins: Artifact Registry stores the image, and an immutable tag blocks re-push.
- **E:** Correct. A regional repository for images and packages. In this case: Artifact Registry stores the image, and an immutable tag blocks re-push.

### Question 25 — C

Answer: Reuse the latest tag for every build. A moving tag hides which build is actually deployed. A moving tag that hides which build is running. Local study-map skill 2.2 (Artifact Management), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 2 (building and implementing CI/CD pipelines): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. An immutable tag that identifies the source revision. Why the correct answer wins: A moving tag hides which build is actually deployed.
- **B:** Incorrect for this question. Metadata that ties an artifact to its build inputs. Why the correct answer wins: A moving tag hides which build is actually deployed.
- **C:** Correct. A moving tag that hides which build is running. In this case: A moving tag hides which build is actually deployed.
- **D:** Incorrect for this question. A regional repository for images and packages. Why the correct answer wins: A moving tag hides which build is actually deployed.

### Question 26 — B

Answer: Define the attached cluster as the delivery target. An attached cluster registers the external cluster as a target. A target that points at a GKE cluster outside Google Cloud. Local study-map skill 2.3 (Hybrid and Multicloud Deployment Targets), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 2 (building and implementing CI/CD pipelines): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A revision-based target with traffic control. Why the correct answer wins: An attached cluster registers the external cluster as a target.
- **B:** Correct. A target that points at a GKE cluster outside Google Cloud. In this case: An attached cluster registers the external cluster as a target.
- **C:** Incorrect for this question. A required human approval before the release promotes. Why the correct answer wins: An attached cluster registers the external cluster as a target.
- **D:** Incorrect for this question. A delivery target that sits inside the same project. Why the correct answer wins: An attached cluster registers the external cluster as a target.

### Question 27 — C

Answer: Deliver to a Cloud Run service revision. A Cloud Run target delivers revisions with traffic control. A revision-based target with traffic control. Local study-map skill 2.3 (Hybrid and Multicloud Deployment Targets), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 2 (building and implementing CI/CD pipelines): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A delivery target that sits inside the same project. Why the correct answer wins: A Cloud Run target delivers revisions with traffic control.
- **B:** Incorrect for this question. The immutable record of who released what. Why the correct answer wins: A Cloud Run target delivers revisions with traffic control.
- **C:** Correct. A revision-based target with traffic control. In this case: A Cloud Run target delivers revisions with traffic control.
- **D:** Incorrect for this question. A target that points at a GKE cluster outside Google Cloud. Why the correct answer wins: A Cloud Run target delivers revisions with traffic control.

### Question 28 — A

Answer: Add a Cloud Deploy approval gate before production. An approval gate blocks the promotion until someone approves. A required human approval before the release promotes. Local study-map skill 2.4 (Approval Flows and Deployment Process), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 2 (building and implementing CI/CD pipelines): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Correct. A required human approval before the release promotes. In this case: An approval gate blocks the promotion until someone approves.
- **B:** Incorrect for this question. A hand-built artifact with no pipeline record. Why the correct answer wins: An approval gate blocks the promotion until someone approves.
- **C:** Incorrect for this question. The immutable record of who released what. Why the correct answer wins: An approval gate blocks the promotion until someone approves.
- **D:** Incorrect for this question. An unattended path from commit to production. Why the correct answer wins: An approval gate blocks the promotion until someone approves.

### Question 29 — C, E

Answers: Read Cloud Audit Logs for the release history; Inspect the build provenance attestation. Audit logs record the release, and provenance ties artifact to inputs. The immutable record of who released what. Metadata that ties an artifact to its build inputs. Local study-map skill 2.5 (Deployment Auditing and Tracking), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 2 (building and implementing CI/CD pipelines): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. An immutable tag that identifies the source revision. Why the correct answer wins: Audit logs record the release, and provenance ties artifact to inputs.
- **B:** Incorrect for this question. A published statement about how the artifact was produced. Why the correct answer wins: Audit logs record the release, and provenance ties artifact to inputs.
- **C:** Correct. Metadata that ties an artifact to its build inputs. In this case: Audit logs record the release, and provenance ties artifact to inputs.
- **D:** Incorrect for this question. A required human approval before the release promotes. Why the correct answer wins: Audit logs record the release, and provenance ties artifact to inputs.
- **E:** Correct. The immutable record of who released what. In this case: Audit logs record the release, and provenance ties artifact to inputs.

### Question 30 — C

Answer: Describe the build with its supply chain level and signed provenance. The supply chain level states how the artifact was built. A published statement about how the artifact was produced. Local study-map skill 2.5 (Deployment Auditing and Tracking), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 2 (building and implementing CI/CD pipelines): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. An admission check that only attested images may run. Why the correct answer wins: The supply chain level states how the artifact was built.
- **B:** Incorrect for this question. Metadata that ties an artifact to its build inputs. Why the correct answer wins: The supply chain level states how the artifact was built.
- **C:** Correct. A published statement about how the artifact was produced. In this case: The supply chain level states how the artifact was built.
- **D:** Incorrect for this question. The immutable record of who released what. Why the correct answer wins: The supply chain level states how the artifact was built.

### Question 31 — A, B

Answers: Send ten percent of traffic to the new revision and watch the SLI; Split traffic with a Cloud Service Mesh route. A canary bounds exposure, and the mesh splits traffic by weight. A small traffic slice that bounds the blast radius. Weighted routing between two service versions. Local study-map skill 2.6 (Deployment Strategies), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 2 (building and implementing CI/CD pipelines): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Correct. Weighted routing between two service versions. In this case: A canary bounds exposure, and the mesh splits traffic by weight.
- **B:** Correct. A small traffic slice that bounds the blast radius. In this case: A canary bounds exposure, and the mesh splits traffic by weight.
- **C:** Incorrect for this question. A gradual replacement of the running instances. Why the correct answer wins: A canary bounds exposure, and the mesh splits traffic by weight.
- **D:** Incorrect for this question. A full outage during the change. Why the correct answer wins: A canary bounds exposure, and the mesh splits traffic by weight.
- **E:** Incorrect for this question. Two full environments with an instant cutover. Why the correct answer wins: A canary bounds exposure, and the mesh splits traffic by weight.

### Question 32 — A

Answer: Put the behaviour behind a feature flag. A feature flag separates deployment from release. A runtime switch that separates deploy from release. Local study-map skill 2.6 (Deployment Strategies), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 2 (building and implementing CI/CD pipelines): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Correct. A runtime switch that separates deploy from release. In this case: A feature flag separates deployment from release.
- **B:** Incorrect for this question. A small traffic slice that bounds the blast radius. Why the correct answer wins: A feature flag separates deployment from release.
- **C:** Incorrect for this question. A full outage during the change. Why the correct answer wins: A feature flag separates deployment from release.
- **D:** Incorrect for this question. Two full environments with an instant cutover. Why the correct answer wins: A feature flag separates deployment from release.

### Question 33 — C

Answer: Stop the old version and then start the new one. Recreate stops the old version before starting the new one. A full outage during the change. Local study-map skill 2.6 (Deployment Strategies), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 2 (building and implementing CI/CD pipelines): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A small traffic slice that bounds the blast radius. Why the correct answer wins: Recreate stops the old version before starting the new one.
- **B:** Incorrect for this question. A gradual replacement of the running instances. Why the correct answer wins: Recreate stops the old version before starting the new one.
- **C:** Correct. A full outage during the change. In this case: Recreate stops the old version before starting the new one.
- **D:** Incorrect for this question. Two full environments with an instant cutover. Why the correct answer wins: Recreate stops the old version before starting the new one.

### Question 34 — C

Answer: Gate the rollout on the error-rate SLI. An error-rate SLI gate stops the rollout on user failure. An automated decision driven by the service objective. Local study-map skill 2.7 (Deployment Success Metrics), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 2 (building and implementing CI/CD pipelines): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A resource signal that says nothing about user success. Why the correct answer wins: An error-rate SLI gate stops the rollout on user failure.
- **B:** Incorrect for this question. A required human approval before the release promotes. Why the correct answer wins: An error-rate SLI gate stops the rollout on user failure.
- **C:** Correct. An automated decision driven by the service objective. In this case: An error-rate SLI gate stops the rollout on user failure.
- **D:** Incorrect for this question. Metadata that ties an artifact to its build inputs. Why the correct answer wins: An error-rate SLI gate stops the rollout on user failure.

### Question 35 — A

Answer: Start from the failed step log in Cloud Build. The failed step log names the command that broke. The step output that names the failing command. Local study-map skill 2.8 (Troubleshooting Deployment Issues), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 2 (building and implementing CI/CD pipelines): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Correct. The step output that names the failing command. In this case: The failed step log names the command that broke.
- **B:** Incorrect for this question. The immutable record of who released what. Why the correct answer wins: The failed step log names the command that broke.
- **C:** Incorrect for this question. A safe repeat that converges on the same state. Why the correct answer wins: The failed step log names the command that broke.
- **D:** Incorrect for this question. A return to the last known good release. Why the correct answer wins: The failed step log names the command that broke.

### Question 36 — B

Answer: Make the failed step idempotent and re-run it. An idempotent step converges on the same state when repeated. A safe repeat that converges on the same state. Local study-map skill 2.8 (Troubleshooting Deployment Issues), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 2 (building and implementing CI/CD pipelines): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A return to the last known good release. Why the correct answer wins: An idempotent step converges on the same state when repeated.
- **B:** Correct. A safe repeat that converges on the same state. In this case: An idempotent step converges on the same state when repeated.
- **C:** Incorrect for this question. An untracked change to the live environment. Why the correct answer wins: An idempotent step converges on the same state when repeated.
- **D:** Incorrect for this question. The step output that names the failing command. Why the correct answer wins: An idempotent step converges on the same state when repeated.

### Question 37 — B

Answer: Encrypt the payload with a Cloud KMS key. A Cloud KMS key wraps the payload and logs its use. A managed key that wraps the data. Local study-map skill 2.9 (Key Management), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 2 (building and implementing CI/CD pipelines): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A managed store with immutable versions and audit. Why the correct answer wins: A Cloud KMS key wraps the payload and logs its use.
- **B:** Correct. A managed key that wraps the data. In this case: A Cloud KMS key wraps the payload and logs its use.
- **C:** Incorrect for this question. Managed issuance and renewal for the endpoint. Why the correct answer wins: A Cloud KMS key wraps the payload and logs its use.
- **D:** Incorrect for this question. A secret readable by everyone with repository access. Why the correct answer wins: A Cloud KMS key wraps the payload and logs its use.

### Question 38 — B

Answer: Issue and rotate the certificate with Certificate Manager. Certificate Manager issues and renews the certificates. Managed issuance and renewal for the endpoint. Local study-map skill 2.9 (Key Management), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 2 (building and implementing CI/CD pipelines): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A store for versioned application parameters. Why the correct answer wins: Certificate Manager issues and renews the certificates.
- **B:** Correct. Managed issuance and renewal for the endpoint. In this case: Certificate Manager issues and renews the certificates.
- **C:** Incorrect for this question. A managed store with immutable versions and audit. Why the correct answer wins: Certificate Manager issues and renews the certificates.
- **D:** Incorrect for this question. A managed key that wraps the data. Why the correct answer wins: Certificate Manager issues and renews the certificates.

### Question 39 — B

Answer: Store the credential in Secret Manager with versions. Secret Manager versions and audits the credential. A managed store with immutable versions and audit. Local study-map skill 2.10 (Configuration and Secret Management), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 2 (building and implementing CI/CD pipelines): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A store for versioned application parameters. Why the correct answer wins: Secret Manager versions and audits the credential.
- **B:** Correct. A managed store with immutable versions and audit. In this case: Secret Manager versions and audits the credential.
- **C:** Incorrect for this question. A value left visible in the build history. Why the correct answer wins: Secret Manager versions and audits the credential.
- **D:** Incorrect for this question. A secret readable by everyone with repository access. Why the correct answer wins: Secret Manager versions and audits the credential.

### Question 40 — D

Answer: Keep the non-secret configuration in Parameter Manager. Parameter Manager stores the versioned, non-secret configuration. A store for versioned application parameters. Local study-map skill 2.10 (Configuration and Secret Management), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 2 (building and implementing CI/CD pipelines): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. One image per environment with the settings compiled in. Why the correct answer wins: Parameter Manager stores the versioned, non-secret configuration.
- **B:** Incorrect for this question. A managed store with immutable versions and audit. Why the correct answer wins: Parameter Manager stores the versioned, non-secret configuration.
- **C:** Incorrect for this question. A secret readable by everyone with repository access. Why the correct answer wins: Parameter Manager stores the versioned, non-secret configuration.
- **D:** Correct. A store for versioned application parameters. In this case: Parameter Manager stores the versioned, non-secret configuration.

### Question 41 — A

Answer: Mount the secret at runtime from Secret Manager. A runtime mount reads the secret only when the workload starts. A credential read only when the workload starts. Local study-map skill 2.11 (Build-Time versus Runtime Secret Injection), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 2 (building and implementing CI/CD pipelines): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Correct. A credential read only when the workload starts. In this case: A runtime mount reads the secret only when the workload starts.
- **B:** Incorrect for this question. A secret readable by everyone with repository access. Why the correct answer wins: A runtime mount reads the secret only when the workload starts.
- **C:** Incorrect for this question. A secret baked into an artifact anyone can pull. Why the correct answer wins: A runtime mount reads the secret only when the workload starts.
- **D:** Incorrect for this question. A value left visible in the build history. Why the correct answer wins: A runtime mount reads the secret only when the workload starts.

### Question 42 — C

Answer: Fail the pipeline on a critical vulnerability finding. A gate fails the pipeline on the critical finding. A policy that blocks the promotion. Local study-map skill 2.12 (Vulnerability Scanning and Artifact Analysis), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 2 (building and implementing CI/CD pipelines): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Vulnerability findings for the stored artifacts. Why the correct answer wins: A gate fails the pipeline on the critical finding.
- **B:** Incorrect for this question. A finding that no pipeline blocks on. Why the correct answer wins: A gate fails the pipeline on the critical finding.
- **C:** Correct. A policy that blocks the promotion. In this case: A gate fails the pipeline on the critical finding.
- **D:** Incorrect for this question. An admission check that only attested images may run. Why the correct answer wins: A gate fails the pipeline on the critical finding.

### Question 43 — C, D

Answers: Enforce Binary Authorization attestations before deploy; Enable Artifact Analysis scanning on the repository. Binary Authorization enforces attestation, and Artifact Analysis scans images. An admission check that only attested images may run. Vulnerability findings for the stored artifacts. Local study-map skill 2.13 (Supply Chain Security and Binary Authorization), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 2 (building and implementing CI/CD pipelines): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A finding that no pipeline blocks on. Why the correct answer wins: Binary Authorization enforces attestation, and Artifact Analysis scans images.
- **B:** Incorrect for this question. A policy that blocks the promotion. Why the correct answer wins: Binary Authorization enforces attestation, and Artifact Analysis scans images.
- **C:** Correct. Vulnerability findings for the stored artifacts. In this case: Binary Authorization enforces attestation, and Artifact Analysis scans images.
- **D:** Correct. An admission check that only attested images may run. In this case: Binary Authorization enforces attestation, and Artifact Analysis scans images.
- **E:** Incorrect for this question. An identity that cannot promote outside its environment. Why the correct answer wins: Binary Authorization enforces attestation, and Artifact Analysis scans images.

### Question 44 — B

Answer: Keep the scan report for the monthly review. A report alone blocks nothing on the promotion path. A finding that no pipeline blocks on. Local study-map skill 2.13 (Supply Chain Security and Binary Authorization), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 2 (building and implementing CI/CD pipelines): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. An admission check that only attested images may run. Why the correct answer wins: A report alone blocks nothing on the promotion path.
- **B:** Correct. A finding that no pipeline blocks on. In this case: A report alone blocks nothing on the promotion path.
- **C:** Incorrect for this question. A policy that blocks the promotion. Why the correct answer wins: A report alone blocks nothing on the promotion path.
- **D:** Incorrect for this question. Vulnerability findings for the stored artifacts. Why the correct answer wins: A report alone blocks nothing on the promotion path.

### Question 45 — D

Answer: Bind deploy permissions only inside the production project. Binding deploy rights inside one project limits the blast radius. An identity that cannot promote outside its environment. Local study-map skill 2.14 (Per-Environment IAM Policy), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 2 (building and implementing CI/CD pipelines): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A single broad credential across the whole estate. Why the correct answer wins: Binding deploy rights inside one project limits the blast radius.
- **B:** Incorrect for this question. A build identity with broad write access. Why the correct answer wins: Binding deploy rights inside one project limits the blast radius.
- **C:** Incorrect for this question. A long-lived credential stored outside the platform. Why the correct answer wins: Binding deploy rights inside one project limits the blast radius.
- **D:** Correct. An identity that cannot promote outside its environment. In this case: Binding deploy rights inside one project limits the blast radius.

### Question 46 — D, E

Answers: Track the ratio of good requests to total requests; Set an internal target on that indicator. The SLI is the measurement, and the SLO is the internal target. A measured indicator of how the service behaves. An objective the team commits to without a contract. Local study-map skill 3.1 (SLIs, SLOs, and SLAs), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 3 (applying site reliability engineering practices): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A signal that the budget is going too quickly. Why the correct answer wins: The SLI is the measurement, and the SLO is the internal target.
- **B:** Incorrect for this question. An external commitment that carries a consequence. Why the correct answer wins: The SLI is the measurement, and the SLO is the internal target.
- **C:** Incorrect for this question. An owned entry with its tier and dependencies. Why the correct answer wins: The SLI is the measurement, and the SLO is the internal target.
- **D:** Correct. A measured indicator of how the service behaves. In this case: The SLI is the measurement, and the SLO is the internal target.
- **E:** Correct. An objective the team commits to without a contract. In this case: The SLI is the measurement, and the SLO is the internal target.

### Question 47 — D

Answer: Publish a contractual promise with a remedy. An SLA carries a contractual consequence when it is missed. An external commitment that carries a consequence. Local study-map skill 3.1 (SLIs, SLOs, and SLAs), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 3 (applying site reliability engineering practices): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A measured indicator of how the service behaves. Why the correct answer wins: An SLA carries a contractual consequence when it is missed.
- **B:** Incorrect for this question. A signal that the budget is going too quickly. Why the correct answer wins: An SLA carries a contractual consequence when it is missed.
- **C:** Incorrect for this question. An objective the team commits to without a contract. Why the correct answer wins: An SLA carries a contractual consequence when it is missed.
- **D:** Correct. An external commitment that carries a consequence. In this case: An SLA carries a contractual consequence when it is missed.

### Question 48 — C

Answer: Track the ratio of good requests to total requests. An SLI is the measured ratio of good outcomes. A measured indicator of how the service behaves. Local study-map skill 3.1 (SLIs, SLOs, and SLAs), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 3 (applying site reliability engineering practices): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. An objective the team commits to without a contract. Why the correct answer wins: An SLI is the measured ratio of good outcomes.
- **B:** Incorrect for this question. An external commitment that carries a consequence. Why the correct answer wins: An SLI is the measured ratio of good outcomes.
- **C:** Correct. A measured indicator of how the service behaves. In this case: An SLI is the measured ratio of good outcomes.
- **D:** Incorrect for this question. A signal that the budget is going too quickly. Why the correct answer wins: An SLI is the measured ratio of good outcomes.

### Question 49 — B, C

Answers: Stop feature releases when the error budget is spent; Alert on a fast error-budget burn rate. Spending the budget stops releases, and burn rate predicts exhaustion. A rule that trades velocity for reliability. A signal that the budget is going too quickly. Local study-map skill 3.2 (Error Budgets), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 3 (applying site reliability engineering practices): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. An explicit trade between reliability and change. Why the correct answer wins: Spending the budget stops releases, and burn rate predicts exhaustion.
- **B:** Correct. A signal that the budget is going too quickly. In this case: Spending the budget stops releases, and burn rate predicts exhaustion.
- **C:** Correct. A rule that trades velocity for reliability. In this case: Spending the budget stops releases, and burn rate predicts exhaustion.
- **D:** Incorrect for this question. A uniform promise that most services do not need. Why the correct answer wins: Spending the budget stops releases, and burn rate predicts exhaustion.
- **E:** Incorrect for this question. An external commitment that carries a consequence. Why the correct answer wins: Spending the budget stops releases, and burn rate predicts exhaustion.

### Question 50 — C

Answer: Stop feature releases when the error budget is spent. A budget rule pauses releases once the allowance is spent. A rule that trades velocity for reliability. Local study-map skill 3.2 (Error Budgets), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 3 (applying site reliability engineering practices): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A signal that the budget is going too quickly. Why the correct answer wins: A budget rule pauses releases once the allowance is spent.
- **B:** Incorrect for this question. A uniform promise that most services do not need. Why the correct answer wins: A budget rule pauses releases once the allowance is spent.
- **C:** Correct. A rule that trades velocity for reliability. In this case: A budget rule pauses releases once the allowance is spent.
- **D:** Incorrect for this question. An external commitment that carries a consequence. Why the correct answer wins: A budget rule pauses releases once the allowance is spent.

### Question 51 — A

Answer: Choose three nines and spend the difference on features. Three nines trades some reliability for delivery speed. An explicit trade between reliability and change. Local study-map skill 3.3 (Cost of Reliability and Nines), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 3 (applying site reliability engineering practices): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Correct. An explicit trade between reliability and change. In this case: Three nines trades some reliability for delivery speed.
- **B:** Incorrect for this question. An external commitment that carries a consequence. Why the correct answer wins: Three nines trades some reliability for delivery speed.
- **C:** Incorrect for this question. A uniform promise that most services do not need. Why the correct answer wins: Three nines trades some reliability for delivery speed.
- **D:** Incorrect for this question. A rule that trades velocity for reliability. Why the correct answer wins: Three nines trades some reliability for delivery speed.

### Question 52 — B

Answer: Assume five nines for every service. A uniform five-nines promise spends effort where it is not needed. A uniform promise that most services do not need. Local study-map skill 3.3 (Cost of Reliability and Nines), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 3 (applying site reliability engineering practices): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. An explicit trade between reliability and change. Why the correct answer wins: A uniform five-nines promise spends effort where it is not needed.
- **B:** Correct. A uniform promise that most services do not need. In this case: A uniform five-nines promise spends effort where it is not needed.
- **C:** Incorrect for this question. An external commitment that carries a consequence. Why the correct answer wins: A uniform five-nines promise spends effort where it is not needed.
- **D:** Incorrect for this question. An owned entry with its tier and dependencies. Why the correct answer wins: A uniform five-nines promise spends effort where it is not needed.

### Question 53 — B

Answer: Register the service in the service catalog. A catalog entry records the owner and the dependencies. An owned entry with its tier and dependencies. Local study-map skill 3.4 (Service Lifecycle Management), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 3 (applying site reliability engineering practices): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Capacity arranged ahead of a known peak. Why the correct answer wins: A catalog entry records the owner and the dependencies.
- **B:** Correct. An owned entry with its tier and dependencies. In this case: A catalog entry records the owner and the dependencies.
- **C:** Incorrect for this question. A planned withdrawal with a migration path. Why the correct answer wins: A catalog entry records the owner and the dependencies.
- **D:** Incorrect for this question. An unowned workload that still costs money. Why the correct answer wins: A catalog entry records the owner and the dependencies.

### Question 54 — A

Answer: Announce the retirement date and withdraw traffic gradually. Announcing retirement and withdrawing traffic gives users a path. A planned withdrawal with a migration path. Local study-map skill 3.4 (Service Lifecycle Management), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 3 (applying site reliability engineering practices): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Correct. A planned withdrawal with a migration path. In this case: Announcing retirement and withdrawing traffic gives users a path.
- **B:** Incorrect for this question. An unowned workload that still costs money. Why the correct answer wins: Announcing retirement and withdrawing traffic gives users a path.
- **C:** Incorrect for this question. Extra supply in a different location. Why the correct answer wins: Announcing retirement and withdrawing traffic gives users a path.
- **D:** Incorrect for this question. An owned entry with its tier and dependencies. Why the correct answer wins: Announcing retirement and withdrawing traffic gives users a path.

### Question 55 — D

Answer: Request a quota increase and reserve capacity before the launch. A quota increase and reservation secure capacity before the launch. Capacity arranged ahead of a known peak. Local study-map skill 3.5 (Capacity Planning and Quotas), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 3 (applying site reliability engineering practices): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A flexible placement into a cheaper window. Why the correct answer wins: A quota increase and reservation secure capacity before the launch.
- **B:** Incorrect for this question. Calendar-driven capacity with no feedback loop. Why the correct answer wins: A quota increase and reservation secure capacity before the launch.
- **C:** Incorrect for this question. Limits that throttle at the worst possible moment. Why the correct answer wins: A quota increase and reservation secure capacity before the launch.
- **D:** Correct. Capacity arranged ahead of a known peak. In this case: A quota increase and reservation secure capacity before the launch.

### Question 56 — C

Answer: Schedule the batch with Dynamic Workload Scheduler. Dynamic Workload Scheduler places the batch in a cheaper window. A flexible placement into a cheaper window. Local study-map skill 3.5 (Capacity Planning and Quotas), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 3 (applying site reliability engineering practices): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Calendar-driven capacity with no feedback loop. Why the correct answer wins: Dynamic Workload Scheduler places the batch in a cheaper window.
- **B:** Incorrect for this question. Capacity arranged ahead of a known peak. Why the correct answer wins: Dynamic Workload Scheduler places the batch in a cheaper window.
- **C:** Correct. A flexible placement into a cheaper window. In this case: Dynamic Workload Scheduler places the batch in a cheaper window.
- **D:** Incorrect for this question. Managed instance scaling from a resource metric. Why the correct answer wins: Dynamic Workload Scheduler places the batch in a cheaper window.

### Question 57 — C, E

Answers: Scale on queue depth with a horizontal pod autoscaler; Set Cloud Run concurrency so replicas follow load. Queue depth scales the workers, and concurrency scales the revisions. Replica scaling driven by a work signal. Concurrency-based replica scaling. Local study-map skill 3.6 (Autoscaling), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 3 (applying site reliability engineering practices): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Calendar-driven capacity with no feedback loop. Why the correct answer wins: Queue depth scales the workers, and concurrency scales the revisions.
- **B:** Incorrect for this question. Limits that throttle at the worst possible moment. Why the correct answer wins: Queue depth scales the workers, and concurrency scales the revisions.
- **C:** Correct. Concurrency-based replica scaling. In this case: Queue depth scales the workers, and concurrency scales the revisions.
- **D:** Incorrect for this question. Managed instance scaling from a resource metric. Why the correct answer wins: Queue depth scales the workers, and concurrency scales the revisions.
- **E:** Correct. Replica scaling driven by a work signal. In this case: Queue depth scales the workers, and concurrency scales the revisions.

### Question 58 — A

Answer: Put the instance group behind an autoscaler on CPU. An autoscaler on the instance group follows CPU. Managed instance scaling from a resource metric. Local study-map skill 3.6 (Autoscaling), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 3 (applying site reliability engineering practices): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Correct. Managed instance scaling from a resource metric. In this case: An autoscaler on the instance group follows CPU.
- **B:** Incorrect for this question. Calendar-driven capacity with no feedback loop. Why the correct answer wins: An autoscaler on the instance group follows CPU.
- **C:** Incorrect for this question. Replica scaling driven by a work signal. Why the correct answer wins: An autoscaler on the instance group follows CPU.
- **D:** Incorrect for this question. A flexible placement into a cheaper window. Why the correct answer wins: An autoscaler on the instance group follows CPU.

### Question 59 — A

Answer: Drain connections before removing the instance. Draining hands the in-flight requests over gracefully. A graceful handover of in-flight requests. Local study-map skill 3.7 (Traffic Draining and Redirection), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 3 (applying site reliability engineering practices): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Correct. A graceful handover of in-flight requests. In this case: Draining hands the in-flight requests over gracefully.
- **B:** Incorrect for this question. Extra supply in a different location. Why the correct answer wins: Draining hands the in-flight requests over gracefully.
- **C:** Incorrect for this question. A name-level redirect to a healthy region. Why the correct answer wins: Draining hands the in-flight requests over gracefully.
- **D:** Incorrect for this question. A health-checked switch between backends. Why the correct answer wins: Draining hands the in-flight requests over gracefully.

### Question 60 — D

Answer: Use a load balancer failover backend. A failover backend moves traffic when health checks fail. A health-checked switch between backends. Local study-map skill 3.7 (Traffic Draining and Redirection), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 3 (applying site reliability engineering practices): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A name-level redirect to a healthy region. Why the correct answer wins: A failover backend moves traffic when health checks fail.
- **B:** Incorrect for this question. Extra supply in a different location. Why the correct answer wins: A failover backend moves traffic when health checks fail.
- **C:** Incorrect for this question. A graceful handover of in-flight requests. Why the correct answer wins: A failover backend moves traffic when health checks fail.
- **D:** Correct. A health-checked switch between backends. In this case: A failover backend moves traffic when health checks fail.

### Question 61 — B

Answer: Add capacity in a second region. Adding capacity in a second region restores supply. Extra supply in a different location. Local study-map skill 3.8 (Incident Capacity), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 3 (applying site reliability engineering practices): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Capacity arranged ahead of a known peak. Why the correct answer wins: Adding capacity in a second region restores supply.
- **B:** Correct. Extra supply in a different location. In this case: Adding capacity in a second region restores supply.
- **C:** Incorrect for this question. A graceful handover of in-flight requests. Why the correct answer wins: Adding capacity in a second region restores supply.
- **D:** Incorrect for this question. A health-checked switch between backends. Why the correct answer wins: Adding capacity in a second region restores supply.

### Question 62 — A

Answer: Redeploy the previous image to the affected service. Redeploying the previous image restores a known good build. A known good artifact restored in place. Local study-map skill 3.9 (Rollback Strategies), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 3 (applying site reliability engineering practices): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Correct. A known good artifact restored in place. In this case: Redeploying the previous image restores a known good build.
- **B:** Incorrect for this question. No action while users are still failing. Why the correct answer wins: Redeploying the previous image restores a known good build.
- **C:** Incorrect for this question. An untracked change to the live environment. Why the correct answer wins: Redeploying the previous image restores a known good build.
- **D:** Incorrect for this question. A paired migration that can be undone. Why the correct answer wins: Redeploying the previous image restores a known good build.

### Question 63 — A

Answer: Reverse the schema change with a tested down migration. A tested down migration reverses the incompatible schema change. A paired migration that can be undone. Local study-map skill 3.9 (Rollback Strategies), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 3 (applying site reliability engineering practices): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Correct. A paired migration that can be undone. In this case: A tested down migration reverses the incompatible schema change.
- **B:** Incorrect for this question. No action while users are still failing. Why the correct answer wins: A tested down migration reverses the incompatible schema change.
- **C:** Incorrect for this question. An untracked change to the live environment. Why the correct answer wins: A tested down migration reverses the incompatible schema change.
- **D:** Incorrect for this question. A known good artifact restored in place. Why the correct answer wins: A tested down migration reverses the incompatible schema change.

### Question 64 — A, B

Answers: Install the Ops Agent on the instances; Turn on VPC Flow Logs for the subnet. The Ops Agent ships host telemetry, and flow logs record connections. A collector that ships logs and metrics from the VM. Per-connection records of accepted and denied traffic. Local study-map skill 4.1 (Log Collection and Ingestion), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 4 (implementing observability practices and troubleshooting): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Correct. Per-connection records of accepted and denied traffic. In this case: The Ops Agent ships host telemetry, and flow logs record connections.
- **B:** Correct. A collector that ships logs and metrics from the VM. In this case: The Ops Agent ships host telemetry, and flow logs record connections.
- **C:** Incorrect for this question. Request metrics emitted by the sidecar proxies. Why the correct answer wins: The Ops Agent ships host telemetry, and flow logs record connections.
- **D:** Incorrect for this question. A vendor-neutral pipeline for traces and metrics. Why the correct answer wins: The Ops Agent ships host telemetry, and flow logs record connections.
- **E:** Incorrect for this question. A record of reads and writes on the resource. Why the correct answer wins: The Ops Agent ships host telemetry, and flow logs record connections.

### Question 65 — C

Answer: Run an OpenTelemetry Collector in the cluster. An OpenTelemetry Collector receives and forwards the trace data. A vendor-neutral pipeline for traces and metrics. Local study-map skill 4.1 (Log Collection and Ingestion), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 4 (implementing observability practices and troubleshooting): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A collector that ships logs and metrics from the VM. Why the correct answer wins: An OpenTelemetry Collector receives and forwards the trace data.
- **B:** Incorrect for this question. Request metrics emitted by the sidecar proxies. Why the correct answer wins: An OpenTelemetry Collector receives and forwards the trace data.
- **C:** Correct. A vendor-neutral pipeline for traces and metrics. In this case: An OpenTelemetry Collector receives and forwards the trace data.
- **D:** Incorrect for this question. A record of reads and writes on the resource. Why the correct answer wins: An OpenTelemetry Collector receives and forwards the trace data.

### Question 66 — B, C

Answers: Add an exclusion for the health-check entries; Sample the high-volume debug entries. An exclusion drops the probe entries, and sampling keeps a fraction. A filter that drops matching entries before storage. A fraction kept for diagnosis at lower cost. Local study-map skill 4.2 (Log Optimization and Cost), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 4 (implementing observability practices and troubleshooting): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A retention period that cannot be shortened. Why the correct answer wins: An exclusion drops the probe entries, and sampling keeps a fraction.
- **B:** Correct. A filter that drops matching entries before storage. In this case: An exclusion drops the probe entries, and sampling keeps a fraction.
- **C:** Correct. A fraction kept for diagnosis at lower cost. In this case: An exclusion drops the probe entries, and sampling keeps a fraction.
- **D:** Incorrect for this question. A record of reads and writes on the resource. Why the correct answer wins: An exclusion drops the probe entries, and sampling keeps a fraction.
- **E:** Incorrect for this question. A sink that lands logs in a queryable table. Why the correct answer wins: An exclusion drops the probe entries, and sampling keeps a fraction.

### Question 67 — B

Answer: Drop the high-cardinality user label from the metric. Dropping the high-cardinality label shrinks the stored series. A label removal that cuts the stored series. Local study-map skill 4.2 (Log Optimization and Cost), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 4 (implementing observability practices and troubleshooting): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A cost estimate driven by actual ingest. Why the correct answer wins: Dropping the high-cardinality label shrinks the stored series.
- **B:** Correct. A label removal that cuts the stored series. In this case: Dropping the high-cardinality label shrinks the stored series.
- **C:** Incorrect for this question. A filter that drops matching entries before storage. Why the correct answer wins: Dropping the high-cardinality label shrinks the stored series.
- **D:** Incorrect for this question. A fraction kept for diagnosis at lower cost. Why the correct answer wins: Dropping the high-cardinality label shrinks the stored series.

### Question 68 — A

Answer: Filter with the Logging query language on the resource label. The query language filters precisely on the resource label. A precise query over the stored entries. Local study-map skill 4.3 (Logs Explorer and Query Language), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 4 (implementing observability practices and troubleshooting): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Correct. A precise query over the stored entries. In this case: The query language filters precisely on the resource label.
- **B:** Incorrect for this question. An interactive view with field filters. Why the correct answer wins: The query language filters precisely on the resource label.
- **C:** Incorrect for this question. A counter derived from matching entries. Why the correct answer wins: The query language filters precisely on the resource label.
- **D:** Incorrect for this question. A sink suited to cheap long-term retention. Why the correct answer wins: The query language filters precisely on the resource label.

### Question 69 — C

Answer: Open the Logs Explorer and pivot from the error entry. Pivoting in the Logs Explorer shows the surrounding entries. An interactive view with field filters. Local study-map skill 4.3 (Logs Explorer and Query Language), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 4 (implementing observability practices and troubleshooting): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A precise query over the stored entries. Why the correct answer wins: Pivoting in the Logs Explorer shows the surrounding entries.
- **B:** Incorrect for this question. A counter derived from matching entries. Why the correct answer wins: Pivoting in the Logs Explorer shows the surrounding entries.
- **C:** Correct. An interactive view with field filters. In this case: Pivoting in the Logs Explorer shows the surrounding entries.
- **D:** Incorrect for this question. A probe that exercises the path from outside. Why the correct answer wins: Pivoting in the Logs Explorer shows the surrounding entries.

### Question 70 — D

Answer: Route the entries to a BigQuery dataset. A BigQuery sink makes the entries queryable in SQL. A sink that lands logs in a queryable table. Local study-map skill 4.4 (Log Export and Retention), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 4 (implementing observability practices and troubleshooting): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A retention period that cannot be shortened. Why the correct answer wins: A BigQuery sink makes the entries queryable in SQL.
- **B:** Incorrect for this question. A sink suited to cheap long-term retention. Why the correct answer wins: A BigQuery sink makes the entries queryable in SQL.
- **C:** Incorrect for this question. A sink that streams entries to another consumer. Why the correct answer wins: A BigQuery sink makes the entries queryable in SQL.
- **D:** Correct. A sink that lands logs in a queryable table. In this case: A BigQuery sink makes the entries queryable in SQL.

### Question 71 — A

Answer: Set the log bucket retention and lock it. A locked retention policy cannot be reduced afterwards. A retention period that cannot be shortened. Local study-map skill 4.4 (Log Export and Retention), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 4 (implementing observability practices and troubleshooting): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Correct. A retention period that cannot be shortened. In this case: A locked retention policy cannot be reduced afterwards.
- **B:** Incorrect for this question. A cost estimate driven by actual ingest. Why the correct answer wins: A locked retention policy cannot be reduced afterwards.
- **C:** Incorrect for this question. A sink suited to cheap long-term retention. Why the correct answer wins: A locked retention policy cannot be reduced afterwards.
- **D:** Incorrect for this question. A sink that streams entries to another consumer. Why the correct answer wins: A locked retention policy cannot be reduced afterwards.

### Question 72 — D

Answer: Redact the email field with a log processor. A processor redacts the field before the entry is stored. A transform that removes the value before storage. Local study-map skill 4.5 (Sensitive Data Redaction), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 4 (implementing observability practices and troubleshooting): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A filter that drops matching entries before storage. Why the correct answer wins: A processor redacts the field before the entry is stored.
- **B:** Incorrect for this question. A procedural promise with no enforcement. Why the correct answer wins: A processor redacts the field before the entry is stored.
- **C:** Incorrect for this question. A fraction kept for diagnosis at lower cost. Why the correct answer wins: A processor redacts the field before the entry is stored.
- **D:** Correct. A transform that removes the value before storage. In this case: A processor redacts the field before the entry is stored.

### Question 73 — B

Answer: Ask Gemini Cloud Assist to summarise the failing entries. Gemini Cloud Assist summarises the selected log range. An AI summary over the selected log range. Local study-map skill 4.6 (Gemini Cloud Assist for Log Analysis), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 4 (implementing observability practices and troubleshooting): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A precise query over the stored entries. Why the correct answer wins: Gemini Cloud Assist summarises the selected log range.
- **B:** Correct. An AI summary over the selected log range. In this case: Gemini Cloud Assist summarises the selected log range.
- **C:** Incorrect for this question. An interactive view with field filters. Why the correct answer wins: Gemini Cloud Assist summarises the selected log range.
- **D:** Incorrect for this question. An AI interpretation of the chart. Why the correct answer wins: Gemini Cloud Assist summarises the selected log range.

### Question 74 — B

Answer: Scrape the workload with managed collection for Prometheus. Managed collection scrapes and stores the Prometheus data. A metrics store fed by a scrape endpoint. Local study-map skill 4.7 (Metrics Collection), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 4 (implementing observability practices and troubleshooting): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A vendor-neutral pipeline for traces and metrics. Why the correct answer wins: Managed collection scrapes and stores the Prometheus data.
- **B:** Correct. A metrics store fed by a scrape endpoint. In this case: Managed collection scrapes and stores the Prometheus data.
- **C:** Incorrect for this question. A counter derived from matching entries. Why the correct answer wins: Managed collection scrapes and stores the Prometheus data.
- **D:** Incorrect for this question. A measurement written by the application itself. Why the correct answer wins: Managed collection scrapes and stores the Prometheus data.

### Question 75 — B

Answer: Emit a custom metric for the business event. The application writes a custom metric for the event. A measurement written by the application itself. Local study-map skill 4.7 (Metrics Collection), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 4 (implementing observability practices and troubleshooting): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A metrics store fed by a scrape endpoint. Why the correct answer wins: The application writes a custom metric for the event.
- **B:** Correct. A measurement written by the application itself. In this case: The application writes a custom metric for the event.
- **C:** Incorrect for this question. A probe that exercises the path from outside. Why the correct answer wins: The application writes a custom metric for the event.
- **D:** Incorrect for this question. A counter derived from matching entries. Why the correct answer wins: The application writes a custom metric for the event.

### Question 76 — A

Answer: Create a log-based metric for the error string. A log-based metric counts the matching entries. A counter derived from matching entries. Local study-map skill 4.8 (Custom and Log-Based Metrics), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 4 (implementing observability practices and troubleshooting): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Correct. A counter derived from matching entries. In this case: A log-based metric counts the matching entries.
- **B:** Incorrect for this question. A probe that exercises the path from outside. Why the correct answer wins: A log-based metric counts the matching entries.
- **C:** Incorrect for this question. A metrics store fed by a scrape endpoint. Why the correct answer wins: A log-based metric counts the matching entries.
- **D:** Incorrect for this question. A measurement written by the application itself. Why the correct answer wins: A log-based metric counts the matching entries.

### Question 77 — C

Answer: Create an uptime check against the login flow. An uptime check probes the flow from outside. A probe that exercises the path from outside. Local study-map skill 4.9 (Synthetic Monitors), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 4 (implementing observability practices and troubleshooting): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A metrics store fed by a scrape endpoint. Why the correct answer wins: An uptime check probes the flow from outside.
- **B:** Incorrect for this question. A counter derived from matching entries. Why the correct answer wins: An uptime check probes the flow from outside.
- **C:** Correct. A probe that exercises the path from outside. In this case: An uptime check probes the flow from outside.
- **D:** Incorrect for this question. A measurement written by the application itself. Why the correct answer wins: An uptime check probes the flow from outside.

### Question 78 — D

Answer: Build one dashboard and share it with the on-call rotation. One shared dashboard gives every responder the same view. A shared view of the signals that matter. Local study-map skill 4.10 (Metrics Explorer and Dashboards), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 4 (implementing observability practices and troubleshooting): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A probe that exercises the path from outside. Why the correct answer wins: One shared dashboard gives every responder the same view.
- **B:** Incorrect for this question. A documented response beside the notification. Why the correct answer wins: One shared dashboard gives every responder the same view.
- **C:** Incorrect for this question. A static threshold on a resource metric. Why the correct answer wins: One shared dashboard gives every responder the same view.
- **D:** Correct. A shared view of the signals that matter. In this case: One shared dashboard gives every responder the same view.

### Question 79 — C

Answer: Attach the remediation playbook to the alert. Attaching the playbook puts the steps beside the alert. A documented response beside the notification. Local study-map skill 4.10 (Metrics Explorer and Dashboards), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 4 (implementing observability practices and troubleshooting): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A shared view of the signals that matter. Why the correct answer wins: Attaching the playbook puts the steps beside the alert.
- **B:** Incorrect for this question. A third-party paging integration. Why the correct answer wins: Attaching the playbook puts the steps beside the alert.
- **C:** Correct. A documented response beside the notification. In this case: Attaching the playbook puts the steps beside the alert.
- **D:** Incorrect for this question. A static threshold on a resource metric. Why the correct answer wins: Attaching the playbook puts the steps beside the alert.

### Question 80 — B, D

Answers: Create an alerting policy on the SLO burn rate; Send the alert to PagerDuty through a webhook. A burn-rate policy pages on the objective, and a webhook reaches the pager. A page driven by the objective instead of a raw threshold. A third-party paging integration. Local study-map skill 4.11 (Alerting Policies), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 4 (implementing observability practices and troubleshooting): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A delivery route for the alert. Why the correct answer wins: A burn-rate policy pages on the objective, and a webhook reaches the pager.
- **B:** Correct. A third-party paging integration. In this case: A burn-rate policy pages on the objective, and a webhook reaches the pager.
- **C:** Incorrect for this question. A documented response beside the notification. Why the correct answer wins: A burn-rate policy pages on the objective, and a webhook reaches the pager.
- **D:** Correct. A page driven by the objective instead of a raw threshold. In this case: A burn-rate policy pages on the objective, and a webhook reaches the pager.
- **E:** Incorrect for this question. A static threshold on a resource metric. Why the correct answer wins: A burn-rate policy pages on the objective, and a webhook reaches the pager.

### Question 81 — D

Answer: Alert when CPU stays above ninety percent for ten minutes. A static CPU threshold ignores whether users are succeeding. A static threshold on a resource metric. Local study-map skill 4.11 (Alerting Policies), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 4 (implementing observability practices and troubleshooting): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A probe that exercises the path from outside. Why the correct answer wins: A static CPU threshold ignores whether users are succeeding.
- **B:** Incorrect for this question. A page driven by the objective instead of a raw threshold. Why the correct answer wins: A static CPU threshold ignores whether users are succeeding.
- **C:** Incorrect for this question. A third-party paging integration. Why the correct answer wins: A static CPU threshold ignores whether users are succeeding.
- **D:** Correct. A static threshold on a resource metric. In this case: A static CPU threshold ignores whether users are succeeding.

### Question 82 — C

Answer: Add an email notification channel for the on-call group. An email channel delivers the alert to the shared inbox. A delivery route for the alert. Local study-map skill 4.12 (Third-Party Alerting Integration), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 4 (implementing observability practices and troubleshooting): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A static threshold on a resource metric. Why the correct answer wins: An email channel delivers the alert to the shared inbox.
- **B:** Incorrect for this question. A documented response beside the notification. Why the correct answer wins: An email channel delivers the alert to the shared inbox.
- **C:** Correct. A delivery route for the alert. In this case: An email channel delivers the alert to the shared inbox.
- **D:** Incorrect for this question. A third-party paging integration. Why the correct answer wins: An email channel delivers the alert to the shared inbox.

### Question 83 — B, E

Answers: Instrument the service with OpenTelemetry spans; Put the trace ID in the structured log line. Spans give the per-call timing, and the trace ID joins the logs. Trace context emitted for each request. A join key between traces and logs. Local study-map skill 4.13 (Distributed Tracing with OpenTelemetry), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 4 (implementing observability practices and troubleshooting): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. An AI pointer to the expensive span. Why the correct answer wins: Spans give the per-call timing, and the trace ID joins the logs.
- **B:** Correct. Trace context emitted for each request. In this case: Spans give the per-call timing, and the trace ID joins the logs.
- **C:** Incorrect for this question. A per-span timing view of one request. Why the correct answer wins: Spans give the per-call timing, and the trace ID joins the logs.
- **D:** Incorrect for this question. No shared identifier between the two signals. Why the correct answer wins: Spans give the per-call timing, and the trace ID joins the logs.
- **E:** Correct. A join key between traces and logs. In this case: Spans give the per-call timing, and the trace ID joins the logs.

### Question 84 — A

Answer: Read the trace waterfall to find the slow span. The trace waterfall shows the slow span in order. A per-span timing view of one request. Local study-map skill 4.13 (Distributed Tracing with OpenTelemetry), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 4 (implementing observability practices and troubleshooting): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Correct. A per-span timing view of one request. In this case: The trace waterfall shows the slow span in order.
- **B:** Incorrect for this question. Trace context emitted for each request. Why the correct answer wins: The trace waterfall shows the slow span in order.
- **C:** Incorrect for this question. A join key between traces and logs. Why the correct answer wins: The trace waterfall shows the slow span in order.
- **D:** Incorrect for this question. An AI pointer to the expensive span. Why the correct answer wins: The trace waterfall shows the slow span in order.

### Question 85 — D

Answer: Ask Gemini Cloud Assist which span dominates the trace. Gemini Cloud Assist names the span that dominates. An AI pointer to the expensive span. Local study-map skill 4.14 (Trace Analysis and Log Correlation), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 4 (implementing observability practices and troubleshooting): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A per-span timing view of one request. Why the correct answer wins: Gemini Cloud Assist names the span that dominates.
- **B:** Incorrect for this question. A join key between traces and logs. Why the correct answer wins: Gemini Cloud Assist names the span that dominates.
- **C:** Incorrect for this question. Trace context emitted for each request. Why the correct answer wins: Gemini Cloud Assist names the span that dominates.
- **D:** Correct. An AI pointer to the expensive span. In this case: Gemini Cloud Assist names the span that dominates.

### Question 86 — D

Answer: Inspect the image pull credential and repository permission. The node identity must be allowed to pull from the repository. The identity the node uses to fetch the image. Local study-map skill 4.15 (Infrastructure and Pipeline Troubleshooting), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 4 (implementing observability practices and troubleshooting): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A shared egress resource that runs out of ports. Why the correct answer wins: The node identity must be allowed to pull from the repository.
- **B:** Incorrect for this question. The rule that blocked the connection. Why the correct answer wins: The node identity must be allowed to pull from the repository.
- **C:** Incorrect for this question. The limit that refused the resource. Why the correct answer wins: The node identity must be allowed to pull from the repository.
- **D:** Correct. The identity the node uses to fetch the image. In this case: The node identity must be allowed to pull from the repository.

### Question 87 — B

Answer: Compare the readiness probe with the application startup time. A readiness probe that fires too early restarts a starting app. A probe that fails before the app is listening. Local study-map skill 4.16 (Application and Latency Troubleshooting), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 4 (implementing observability practices and troubleshooting): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A stale name that still points at the old address. Why the correct answer wins: A readiness probe that fires too early restarts a starting app.
- **B:** Correct. A probe that fails before the app is listening. In this case: A readiness probe that fires too early restarts a starting app.
- **C:** Incorrect for this question. A shared egress resource that runs out of ports. Why the correct answer wins: A readiness probe that fires too early restarts a starting app.
- **D:** Incorrect for this question. A hotspot found on the request path. Why the correct answer wins: A readiness probe that fires too early restarts a starting app.

### Question 88 — A

Answer: Check Cloud NAT port exhaustion for the egress range. A shared Cloud NAT range can run out of ports. A shared egress resource that runs out of ports. Local study-map skill 4.16 (Application and Latency Troubleshooting), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 4 (implementing observability practices and troubleshooting): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Correct. A shared egress resource that runs out of ports. In this case: A shared Cloud NAT range can run out of ports.
- **B:** Incorrect for this question. The limit that refused the resource. Why the correct answer wins: A shared Cloud NAT range can run out of ports.
- **C:** Incorrect for this question. The rule that blocked the connection. Why the correct answer wins: A shared Cloud NAT range can run out of ports.
- **D:** Incorrect for this question. The identity the node uses to fetch the image. Why the correct answer wins: A shared Cloud NAT range can run out of ports.

### Question 89 — A

Answer: Measure request latency by endpoint in Cloud Monitoring. Per-endpoint latency shows which request path degraded. An application-level view of response time. Local study-map skill 5.1 (Application Performance Monitoring), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 5 (optimizing performance and cost): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Correct. An application-level view of response time. In this case: Per-endpoint latency shows which request path degraded.
- **B:** Incorrect for this question. A queryable record of spend by label. Why the correct answer wins: Per-endpoint latency shows which request path degraded.
- **C:** Incorrect for this question. A cost estimate driven by actual ingest. Why the correct answer wins: Per-endpoint latency shows which request path degraded.
- **D:** Incorrect for this question. Reclaimable capacity under a stateful workload. Why the correct answer wins: Per-endpoint latency shows which request path degraded.

### Question 90 — C

Answer: Track the service objective on a shared dashboard. A shared objective dashboard tracks the goal per service. A goal-oriented view of performance. Local study-map skill 5.1 (Application Performance Monitoring), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 5 (optimizing performance and cost): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A pool sized against measured demand. Why the correct answer wins: A shared objective dashboard tracks the goal per service.
- **B:** Incorrect for this question. A recommendation aimed at spend. Why the correct answer wins: A shared objective dashboard tracks the goal per service.
- **C:** Correct. A goal-oriented view of performance. In this case: A shared objective dashboard tracks the goal per service.
- **D:** Incorrect for this question. A cost estimate driven by actual ingest. Why the correct answer wins: A shared objective dashboard tracks the goal per service.

### Question 91 — C, E

Answers: Review the Active Assist recommendations for the project; Apply the cost recommender suggestion for the idle disks. Active Assist surfaces the suggestions, and the cost recommender targets idle spend. Suggested changes generated from telemetry. A recommendation aimed at spend. Local study-map skill 5.2 (Active Assist and Recommenders), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 5 (optimizing performance and cost): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A queryable record of spend by label. Why the correct answer wins: Active Assist surfaces the suggestions, and the cost recommender targets idle spend.
- **B:** Incorrect for this question. A recommendation aimed at resilience. Why the correct answer wins: Active Assist surfaces the suggestions, and the cost recommender targets idle spend.
- **C:** Correct. A recommendation aimed at spend. In this case: Active Assist surfaces the suggestions, and the cost recommender targets idle spend.
- **D:** Incorrect for this question. Reclaimable capacity under a stateful workload. Why the correct answer wins: Active Assist surfaces the suggestions, and the cost recommender targets idle spend.
- **E:** Correct. Suggested changes generated from telemetry. In this case: Active Assist surfaces the suggestions, and the cost recommender targets idle spend.

### Question 92 — D

Answer: Apply the reliability recommender for the missing quota. The reliability recommender flags the missing headroom. A recommendation aimed at resilience. Local study-map skill 5.2 (Active Assist and Recommenders), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 5 (optimizing performance and cost): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A recommendation aimed at spend. Why the correct answer wins: The reliability recommender flags the missing headroom.
- **B:** Incorrect for this question. Reclaimable capacity under a stateful workload. Why the correct answer wins: The reliability recommender flags the missing headroom.
- **C:** Incorrect for this question. Suggested changes generated from telemetry. Why the correct answer wins: The reliability recommender flags the missing headroom.
- **D:** Correct. A recommendation aimed at resilience. In this case: The reliability recommender flags the missing headroom.

### Question 93 — B

Answer: Measure log volume per service before choosing a retention period. Measuring ingest volume grounds the retention decision in data. A cost estimate driven by actual ingest. Local study-map skill 5.3 (Observability Cost Management), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 5 (optimizing performance and cost): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A cheaper egress path with different performance. Why the correct answer wins: Measuring ingest volume grounds the retention decision in data.
- **B:** Correct. A cost estimate driven by actual ingest. In this case: Measuring ingest volume grounds the retention decision in data.
- **C:** Incorrect for this question. A reduction that preserves the useful signal. Why the correct answer wins: Measuring ingest volume grounds the retention decision in data.
- **D:** Incorrect for this question. A label removal that cuts the stored series. Why the correct answer wins: Measuring ingest volume grounds the retention decision in data.

### Question 94 — B

Answer: Exclude the debug stream and keep the error stream. Excluding the debug stream keeps the useful error signal. A reduction that preserves the useful signal. Local study-map skill 5.3 (Observability Cost Management), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 5 (optimizing performance and cost): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A label removal that cuts the stored series. Why the correct answer wins: Excluding the debug stream keeps the useful error signal.
- **B:** Correct. A reduction that preserves the useful signal. In this case: Excluding the debug stream keeps the useful error signal.
- **C:** Incorrect for this question. A retention period that cannot be shortened. Why the correct answer wins: Excluding the debug stream keeps the useful error signal.
- **D:** Incorrect for this question. A cost estimate driven by actual ingest. Why the correct answer wins: Excluding the debug stream keeps the useful error signal.

### Question 95 — B

Answer: Put the stateless workers on a Spot node pool. A Spot node pool cuts cost for reclaimable workers. A pool built from reclaimable capacity. Local study-map skill 5.4 (Spot Virtual Machines), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 5 (optimizing performance and cost): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A multi-year commitment at a lower unit price. Why the correct answer wins: A Spot node pool cuts cost for reclaimable workers.
- **B:** Correct. A pool built from reclaimable capacity. In this case: A Spot node pool cuts cost for reclaimable workers.
- **C:** Incorrect for this question. Reclaimable capacity under a stateful workload. Why the correct answer wins: A Spot node pool cuts cost for reclaimable workers.
- **D:** Incorrect for this question. Warm capacity that avoids cold starts. Why the correct answer wins: A Spot node pool cuts cost for reclaimable workers.

### Question 96 — B

Answer: Move the primary database onto Spot capacity. Reclaimable capacity can vanish under a stateful workload. Local study-map skill 5.4 (Spot Virtual Machines), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 5 (optimizing performance and cost): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A multi-year commitment at a lower unit price. Why the correct answer wins: Reclaimable capacity can vanish under a stateful workload.
- **B:** Correct. In this case: Reclaimable capacity can vanish under a stateful workload.
- **C:** Incorrect for this question. Discounted capacity that can be reclaimed. Why the correct answer wins: Reclaimable capacity can vanish under a stateful workload.
- **D:** Incorrect for this question. A pool built from reclaimable capacity. Why the correct answer wins: Reclaimable capacity can vanish under a stateful workload.

### Question 97 — D, E

Answers: Buy a committed-use discount for the steady baseline; Serve the bulk export over the Standard network tier. A commitment discounts the baseline, and the standard tier lowers egress cost. A multi-year commitment at a lower unit price. A cheaper egress path with different performance. Local study-map skill 5.5 (Infrastructure Cost Planning), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 5 (optimizing performance and cost): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. An automatic discount that accrues with monthly use. Why the correct answer wins: A commitment discounts the baseline, and the standard tier lowers egress cost.
- **B:** Incorrect for this question. Discounted capacity that can be reclaimed. Why the correct answer wins: A commitment discounts the baseline, and the standard tier lowers egress cost.
- **C:** Incorrect for this question. A lower-latency path for user-facing traffic. Why the correct answer wins: A commitment discounts the baseline, and the standard tier lowers egress cost.
- **D:** Correct. A cheaper egress path with different performance. In this case: A commitment discounts the baseline, and the standard tier lowers egress cost.
- **E:** Correct. A multi-year commitment at a lower unit price. In this case: A commitment discounts the baseline, and the standard tier lowers egress cost.

### Question 98 — D

Answer: Keep the interactive traffic on the Premium tier. The premium tier keeps the interactive path short. A lower-latency path for user-facing traffic. Local study-map skill 5.5 (Infrastructure Cost Planning), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 5 (optimizing performance and cost): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Discounted capacity that can be reclaimed. Why the correct answer wins: The premium tier keeps the interactive path short.
- **B:** Incorrect for this question. A multi-year commitment at a lower unit price. Why the correct answer wins: The premium tier keeps the interactive path short.
- **C:** Incorrect for this question. A cheaper egress path with different performance. Why the correct answer wins: The premium tier keeps the interactive path short.
- **D:** Correct. A lower-latency path for user-facing traffic. In this case: The premium tier keeps the interactive path short.

### Question 99 — D

Answer: Right-size the node pool from the observed requests. Right-sizing the pool matches capacity to observed demand. A pool sized against measured demand. Local study-map skill 5.6 (Workload-Level Cost Optimization), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 5 (optimizing performance and cost): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A pool built from reclaimable capacity. Why the correct answer wins: Right-sizing the pool matches capacity to observed demand.
- **B:** Incorrect for this question. Scale to zero for a service nobody uses at night. Why the correct answer wins: Right-sizing the pool matches capacity to observed demand.
- **C:** Incorrect for this question. Warm capacity that avoids cold starts. Why the correct answer wins: Right-sizing the pool matches capacity to observed demand.
- **D:** Correct. A pool sized against measured demand. In this case: Right-sizing the pool matches capacity to observed demand.

### Question 100 — A

Answer: Keep the minimum instance count at zero for the internal tool. A minimum of zero lets the service scale down completely. Scale to zero for a service nobody uses at night. Local study-map skill 5.6 (Workload-Level Cost Optimization), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 5 (optimizing performance and cost): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Correct. Scale to zero for a service nobody uses at night. In this case: A minimum of zero lets the service scale down completely.
- **B:** Incorrect for this question. A calendar action that removes idle spend. Why the correct answer wins: A minimum of zero lets the service scale down completely.
- **C:** Incorrect for this question. Warm capacity that avoids cold starts. Why the correct answer wins: A minimum of zero lets the service scale down completely.
- **D:** Incorrect for this question. A pool sized against measured demand. Why the correct answer wins: A minimum of zero lets the service scale down completely.
