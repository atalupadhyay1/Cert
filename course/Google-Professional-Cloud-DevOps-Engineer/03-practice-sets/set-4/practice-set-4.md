# Google Cloud Professional Cloud DevOps Engineer — Full-Length Mock Exam 4

Professional Cloud DevOps Engineer · 100 questions · expanded practice bank · passing score not published

Blueprint-weighted mock exam. Item mix: 84 multiple-choice and 16 multiple-select items (the selection count is stated in each multi-select stem). The live exam publishes 50-60 multiple-choice and multiple-select questions and has no case-study component, so this set is larger on purpose and no case-study item is reproduced. The live paper allows two hours for 50-60 items, so this 100-item set is a slower-per-item rehearsal: about 72 seconds per item here against roughly 120-144 seconds live. Use it to build a habit of finishing with time to review. See the README for the exact fidelity boundary.

Original educational content, not actual, recalled, or copied Google exam items.

## Questions

---

## Domain 1 — Bootstrapping and Maintaining a Google Cloud Organization (Hierarchy, Infrastructure as Code, and Pipeline Foundations)

### 1. A newly acquired subsidiary must inherit the parent's constraints while keeping its own folders. What fits?

- A. Add an IAM deny policy for the sensitive permission
- B. Apply the constraint to the business unit folder
- C. Apply the constraint separately in each project
- D. Apply the constraint at the organization node

### 2. Regulatory evidence is produced per environment, and production must sit in its own folder tree. How should the hierarchy be shaped?

- A. Group projects by application inside each environment folder
- B. Apply the constraint to the business unit folder
- C. Group projects by environment with applications below
- D. Apply the constraint separately in each project

### 3. Network security must change once for forty workloads instead of forty times. What fits?

- A. Publish the service behind a Private Service Connect endpoint
- B. Peer every project VPC with every other project VPC
- C. Give each project its own VPC and Cloud NAT
- D. Create a Shared VPC host project and attach the service projects

### 4. Two teams need direct routing between their projects for a short pilot. What fits?

- A. Give each project its own VPC and Cloud NAT
- B. Create a Shared VPC host project and attach the service projects
- C. Publish the service behind a Private Service Connect endpoint
- D. Peer every project VPC with every other project VPC

### 5. Each team owns its own log bucket and an audit query now needs fifteen consoles. What caused that?

- A. Route the entries to a BigQuery dataset
- B. Keep one log bucket inside each project
- C. Route every project log to one aggregated sink
- D. Add the projects to one metrics scope

### 6. A location guardrail must bind every project, and a standard read role must be granted without inventing permissions. Which two choices apply? Select two.

- A. Grant a custom role limited to the required permissions
- B. Enforce the restriction with an organization policy constraint
- C. Create one service account per environment
- D. Grant a predefined role once at the folder
- E. Add an IAM deny policy for the sensitive permission

### 7. The job calls exactly four APIs and must be granted nothing else. What should be created?

- A. Enforce the restriction with an organization policy constraint
- B. Add an IAM deny policy for the sensitive permission
- C. Grant a predefined role once at the folder
- D. Grant a custom role limited to the required permissions

### 8. Engineers must act as the pipeline account without downloading any credential. What fits?

- A. Create one service account per workload
- B. Let the workload use the default Compute Engine service account
- C. Download a JSON key file for the service account
- D. Grant impersonation of the service account instead of a key

### 9. Two regions satisfy the latency target and only one satisfies the contract. What decides the choice?

- A. Create a Shared VPC host project and attach the service projects
- B. Place the resources in a region that satisfies the residency rule
- C. Replicate the data to a second region
- D. Apply the constraint at the organization node

### 10. Twenty teams need the same network pattern with their own names. What fits?

- A. Define the estate as Terraform modules held in version control
- B. Apply the deployment through Infrastructure Manager
- C. Reconcile the resources with Config Connector
- D. Package the workload as a Helm chart

### 11. A team already writes Kubernetes manifests and wants them to create SQL instances. What fits?

- A. Reconcile the resources with Config Connector
- B. Render the manifests through a kpt function pipeline
- C. Define the estate as Terraform modules held in version control
- D. Package the workload as a Helm chart

### 12. A regulated landing zone must begin from a vetted blueprint rather than a bespoke module. What fits?

- A. Define the estate as Terraform modules held in version control
- B. Schedule a plan that reports drift
- C. Start from the Cloud Foundation Toolkit blueprints
- D. Render the manifests through a kpt function pipeline

### 13. The same ten commands are retyped for each new environment and one was mistyped. What caused that?

- A. Automate the repeated step with a Python script calling the API
- B. Run the documented gcloud commands by hand for each environment
- C. Make the change in the console and note it in the wiki
- D. Schedule a plan that reports drift

### 14. The build must be managed, and the cluster must reconcile from Git without a push credential. Which two should be adopted? Select two.

- A. Store the build output in Artifact Registry
- B. Bake the machine image with Packer
- C. Use Cloud Build for CI and Cloud Deploy for delivery
- D. Let Argo CD pull the manifests from Git
- E. Run Jenkins on a self-managed VM

### 15. The hardened base image must be rebuilt whenever a base-operating-system CVE lands. What fits?

- A. Bake the machine image with Packer
- B. Define the estate as Terraform modules held in version control
- C. Store the build output in Artifact Registry
- D. Package the workload as a Helm chart

### 16. Three upstream repositories must be normalised to one platform convention. What fits?

- A. Render the manifests through a kpt function pipeline
- B. Package the workload as a Helm chart
- C. Schedule a plan that reports drift
- D. Define the estate as Terraform modules held in version control

### 17. A disposable environment must exist per merge request, and the same manifests must serve it with a small patch. Which two fit? Select two.

- A. Keep one base with a Kustomize overlay per environment
- B. Create a short-lived project per change and delete it after review
- C. Apply the constraint to the business unit folder
- D. Bake the environment settings into the image
- E. Keep one shared staging environment for every team

### 18. Sixty clusters across ten teams need one policy and one debugging identity. What fits?

- A. Register the clusters in a fleet
- B. Create a short-lived project per change and delete it after review
- C. Upgrade each node pool by hand whenever an operator is free
- D. Stand up a second cluster and shift traffic after verification

### 19. Developers lose their tooling whenever the browser session ends. What caused that?

- A. Build a custom image that carries the approved toolchain
- B. Give developers Cloud Workstations built from a custom image
- C. Let each developer install the tools locally
- D. Rely on Cloud Shell for every developer

### 20. A reviewer wants a function explained while reading the diff. What fits?

- A. Build a custom image that carries the approved toolchain
- B. Use Gemini CLI for the repetitive script
- C. Use Gemini Code Assist for the suggested change
- D. Ask Gemini Cloud Assist to explain the resource state

---

## Domain 2 — Building and Implementing CI/CD Pipelines (Delivery Pipelines and Software Supply Chain)

### 21. Documentation builds must rerun whenever a file under docs changes. What should be configured?

- A. Have an engineer build locally and upload the result
- B. Create a Cloud Build trigger on the release branch
- C. Create a trigger that runs the tests on every pull request
- D. Trigger the pipeline only on a signed tag

### 22. A vendor release must correspond to a signed tag rather than a branch head. What should be configured?

- A. Create a Cloud Build trigger on the release branch
- B. Trigger the pipeline only on a signed tag
- C. Create a trigger that runs the tests on every pull request
- D. Add a Cloud Deploy approval gate before production

### 23. Two engineers get different results from the same commit because each builds on their own machine. What caused that?

- A. Trigger the pipeline only on a signed tag
- B. Create a trigger that runs the tests on every pull request
- C. Have an engineer build locally and upload the result
- D. Read Cloud Audit Logs for the release history

### 24. Images must be stored in a regional repository, and a published version must never be overwritten. Which two provide that? Select two.

- A. Store the build output in Artifact Registry
- B. Reuse the latest tag for every build
- C. Bake the machine image with Packer
- D. Tag each artifact with the commit SHA and forbid overwrite
- E. Push the image to Container Registry

### 25. A build pushed the same version twice and the second push replaced the first. What allowed that?

- A. Store the build output in Artifact Registry
- B. Tag each artifact with the commit SHA and forbid overwrite
- C. Reuse the latest tag for every build
- D. Inspect the build provenance attestation

### 26. A cluster registered from another cloud must receive releases from the pipeline. What fits?

- A. Deliver to a Cloud Run service revision
- B. Define the attached cluster as the delivery target
- C. Add a Cloud Deploy approval gate before production
- D. Use a GKE cluster in the pipeline project as the target

### 27. A serverless service needs traffic percentages per revision from the pipeline. What fits?

- A. Deliver to a Cloud Run service revision
- B. Define the attached cluster as the delivery target
- C. Read Cloud Audit Logs for the release history
- D. Use a GKE cluster in the pipeline project as the target

### 28. Legal requires a human sign-off before any release reaches customers. What should be added?

- A. Read Cloud Audit Logs for the release history
- B. Add a Cloud Deploy approval gate before production
- C. Promote automatically to every target in the chain
- D. Have an engineer build locally and upload the result

### 29. An auditor asks who promoted release forty-two and at what time. What answers that?

- A. Tag each artifact with the commit SHA and forbid overwrite
- B. Describe the build with its supply chain level and signed provenance
- C. Read Cloud Audit Logs for the release history
- D. Inspect the build provenance attestation

### 30. The team must show which builder produced the artifact and from which commit. What provides that?

- A. Inspect the build provenance attestation
- B. Describe the build with its supply chain level and signed provenance
- C. Read Cloud Audit Logs for the release history
- D. Tag each artifact with the commit SHA and forbid overwrite

### 31. One percent of users must see the change first, and the behaviour must be switchable off without a deploy. Which two fit? Select two.

- A. Stop the old version and then start the new one
- B. Put the behaviour behind a feature flag
- C. Send ten percent of traffic to the new revision and watch the SLI
- D. Replace the instances in batches
- E. Run the new version alongside and switch traffic at once

### 32. A fleet of ten instances must be replaced two at a time while still serving traffic. What fits?

- A. Send ten percent of traffic to the new revision and watch the SLI
- B. Run the new version alongside and switch traffic at once
- C. Stop the old version and then start the new one
- D. Replace the instances in batches

### 33. A rollback must be immediate because the old stack is still running. Which strategy is that?

- A. Stop the old version and then start the new one
- B. Send ten percent of traffic to the new revision and watch the SLI
- C. Run the new version alongside and switch traffic at once
- D. Replace the instances in batches

### 34. The pipeline must abandon a release when the objective is burning too fast. What should gate it?

- A. Create an uptime check against the login flow
- B. Add a Cloud Deploy approval gate before production
- C. Gate the rollout on average CPU alone
- D. Gate the rollout on the error-rate SLI

### 35. A deployment passes its health checks and then breaks a downstream consumer. What is the first action?

- A. Patch production by hand and reconcile later
- B. Make the failed step idempotent and re-run it
- C. Roll the release back to the previous one
- D. Start from the failed step log in Cloud Build

### 36. A Cloud Build run shows one red step and the engineer needs the exact command. What supplies it?

- A. Roll the release back to the previous one
- B. Make the failed step idempotent and re-run it
- C. Read Cloud Audit Logs for the release history
- D. Start from the failed step log in Cloud Build

### 37. Object data must be encrypted under a key the team controls, and an API token must be versioned and audited. Which two services apply? Select two.

- A. Keep the non-secret configuration in Parameter Manager
- B. Encrypt the payload with a Cloud KMS key
- C. Store the credential in Secret Manager with versions
- D. Commit the credential to the private repository
- E. Issue and rotate the certificate with Certificate Manager

### 38. Workloads must receive short-lived certificates from an internal authority. What fits?

- A. Issue and rotate the certificate with Certificate Manager
- B. Keep the non-secret configuration in Parameter Manager
- C. Store the credential in Secret Manager with versions
- D. Encrypt the payload with a Cloud KMS key

### 39. Limits differ per environment and must be reviewable before a deploy. What fits?

- A. Commit the credential to the private repository
- B. Store the credential in Secret Manager with versions
- C. Keep the non-secret configuration in Parameter Manager
- D. Bake the environment settings into the image

### 40. Changing one timeout in staging requires a full rebuild. What caused that?

- A. Commit the credential to the private repository
- B. Keep the non-secret configuration in Parameter Manager
- C. Bake the environment settings into the image
- D. Store the credential in Secret Manager with versions

### 41. The same image must run in development and production against different credentials. What fits?

- A. Mount the secret at runtime from Secret Manager
- B. Inject the secret at build time into the image layer
- C. Commit the credential to the private repository
- D. Pass the secret as a build argument

### 42. Security wants a vulnerability list for every image currently in the registry. What provides that?

- A. Enforce Binary Authorization attestations before deploy
- B. Enable Artifact Analysis scanning on the repository
- C. Keep the scan report for the monthly review
- D. Fail the pipeline on a critical vulnerability finding

### 43. Only attested images may run, and the deployer identity must be unable to act outside its environment. Which two controls apply? Select two.

- A. Enforce Binary Authorization attestations before deploy
- B. Bind deploy permissions only inside the production project
- C. Keep the scan report for the monthly review
- D. Enable Artifact Analysis scanning on the repository
- E. Fail the pipeline on a critical vulnerability finding

### 44. Any image carrying a critical finding must fail the build rather than warn. What should be configured?

- A. Keep the scan report for the monthly review
- B. Enable Artifact Analysis scanning on the repository
- C. Enforce Binary Authorization attestations before deploy
- D. Fail the pipeline on a critical vulnerability finding

### 45. The build identity can edit every service in the project because it holds a familiar broad role. What is the problem?

- A. Run the pipeline as the default editor service account
- B. Use one identity with deploy rights in every environment
- C. Create one service account per environment
- D. Bind deploy permissions only inside the production project

---

## Domain 3 — Applying Site Reliability Engineering Practices (Reliability Engineering in Practice)

### 46. One document promises money back, and one number measures what users actually experience. Which two are they? Select two.

- A. Set an internal target on that indicator
- B. Alert on a fast error-budget burn rate
- C. Choose three nines and spend the difference on features
- D. Track the ratio of good requests to total requests
- E. Publish a contractual promise with a remedy

### 47. The team adopts 99.5 percent as its own bar, below the contractual 99.9. What is that bar?

- A. Set an internal target on that indicator
- B. Track the ratio of good requests to total requests
- C. Publish a contractual promise with a remedy
- D. Alert on a fast error-budget burn rate

### 48. A review accepts a lower target to protect the release cadence. Which position is that?

- A. Stop feature releases when the error budget is spent
- B. Publish a contractual promise with a remedy
- C. Assume five nines for every service
- D. Choose three nines and spend the difference on features

### 49. A slow leak is detected across six hours and paged before the allowance is gone. What produced the page?

- A. Alert when CPU stays above ninety percent for ten minutes
- B. Publish a contractual promise with a remedy
- C. Stop feature releases when the error budget is spent
- D. Alert on a fast error-budget burn rate

### 50. The team stops launching features for the quarter after two missed objectives. What enforces that?

- A. Stop feature releases when the error budget is spent
- B. Alert on a fast error-budget burn rate
- C. Publish a contractual promise with a remedy
- D. Assume five nines for every service

### 51. Every service in the estate carries the same 99.999 target whatever its use. What is the flaw?

- A. Choose three nines and spend the difference on features
- B. Request a quota increase and reserve capacity before the launch
- C. Publish a contractual promise with a remedy
- D. Assume five nines for every service

### 52. A review finds the extra availability would cost more than the revenue it protects. What follows?

- A. Assume five nines for every service
- B. Register the service in the service catalog
- C. Choose three nines and spend the difference on features
- D. Publish a contractual promise with a remedy

### 53. A service must declare an owner before it can page anyone, and support cannot find that owner. What should be created?

- A. Announce the retirement date and withdraw traffic gradually
- B. Leave the unused service running for now
- C. Register the service in the service catalog
- D. Add capacity in a second region

### 54. A service with no traffic still holds a project and a billing line. Which state is that?

- A. Announce the retirement date and withdraw traffic gradually
- B. Leave the unused service running for now
- C. Register the service in the service catalog
- D. Drain connections before removing the instance

### 55. An annual event needs twice the usual instances in one region for two days. What should be arranged?

- A. Assume the default quota will absorb the launch
- B. Request a quota increase and reserve capacity before the launch
- C. Add capacity on a fixed calendar schedule
- D. Schedule the batch with Dynamic Workload Scheduler

### 56. A backfill may run anywhere in a twelve-hour window and should cost the least. What fits?

- A. Add capacity on a fixed calendar schedule
- B. Schedule the batch with Dynamic Workload Scheduler
- C. Request a quota increase and reserve capacity before the launch
- D. Put the instance group behind an autoscaler on CPU

### 57. A subscription backlog is the only signal that more workers are needed. What fits?

- A. Add capacity on a fixed calendar schedule
- B. Put the instance group behind an autoscaler on CPU
- C. Set Cloud Run concurrency so replicas follow load
- D. Scale on queue depth with a horizontal pod autoscaler

### 58. A request-heavy service must not queue behind a single instance. What setting helps?

- A. Put the instance group behind an autoscaler on CPU
- B. Add capacity on a fixed calendar schedule
- C. Set Cloud Run concurrency so replicas follow load
- D. Scale on queue depth with a horizontal pod autoscaler

### 59. A node pool upgrade must not fail requests that are mid-flight. What must happen first?

- A. Use a load balancer failover backend
- B. Add capacity in a second region
- C. Shift traffic with a DNS routing policy
- D. Drain connections before removing the instance

### 60. A regional failure must be diverted by changing the answer the name returns. What fits?

- A. Drain connections before removing the instance
- B. Use a load balancer failover backend
- C. Shift traffic with a DNS routing policy
- D. Add capacity in a second region

### 61. An incident needs more supply, and users must be moved onto it while it comes up. Which two actions apply? Select two.

- A. Request a quota increase and reserve capacity before the launch
- B. Use a load balancer failover backend
- C. Drain connections before removing the instance
- D. Add capacity in a second region
- E. Shift traffic with a DNS routing policy

### 62. A bad release must be undone in minutes, and its risky code path should have been disabled without a deploy. Which two capabilities apply? Select two.

- A. Redeploy the previous image to the affected service
- B. Patch production by hand and reconcile later
- C. Reverse the schema change with a tested down migration
- D. Wait for the error rate to settle on its own
- E. Put the behaviour behind a feature flag

### 63. A column drop cannot be undone once the migration has run. What should have existed?

- A. Redeploy the previous image to the affected service
- B. Patch production by hand and reconcile later
- C. Wait for the error rate to settle on its own
- D. Reverse the schema change with a tested down migration

---

## Domain 4 — Implementing Observability Practices and Troubleshooting (Telemetry, Alerting, and Diagnosis)

### 64. An ageing VM fleet must send its syslog without installing a third-party agent. What fits?

- A. Install the Ops Agent on the instances
- B. Read the Cloud Service Mesh telemetry
- C. Turn on VPC Flow Logs for the subnet
- D. Run an OpenTelemetry Collector in the cluster

### 65. An application already emits OpenTelemetry and must be routed elsewhere without a code change. What fits?

- A. Read the Cloud Service Mesh telemetry
- B. Install the Ops Agent on the instances
- C. Run an OpenTelemetry Collector in the cluster
- D. Enable Data Access audit logs for the service

### 66. A metric label must be trimmed because it multiplies series, and the ingest rate must be known before retention is chosen. Which two actions apply? Select two.

- A. Measure log volume per service before choosing a retention period
- B. Add an exclusion for the health-check entries
- C. Drop the high-cardinality user label from the metric
- D. Set the log bucket retention and lock it
- E. Sample the high-volume debug entries

### 67. A service logs every request body and the bucket fills within a day. What should be done?

- A. Sample the high-volume debug entries
- B. Measure log volume per service before choosing a retention period
- C. Drop the high-cardinality user label from the metric
- D. Add an exclusion for the health-check entries

### 68. One timeout entry must lead straight to the entries written around it. What fits?

- A. Create a log-based metric for the error string
- B. Open the Logs Explorer and pivot from the error entry
- C. Route the entries to a BigQuery dataset
- D. Filter with the Logging query language on the resource label

### 69. An engineer must exclude one namespace from an otherwise broad query. What fits?

- A. Create a log-based metric for the error string
- B. Filter with the Logging query language on the resource label
- C. Create an uptime check against the login flow
- D. Open the Logs Explorer and pivot from the error entry

### 70. Legal wants proof that nobody can delete last year's entries. What fits?

- A. Route the entries to a BigQuery dataset
- B. Measure log volume per service before choosing a retention period
- C. Route the entries to a Cloud Storage bucket
- D. Set the log bucket retention and lock it

### 71. Cold entries must be kept for years at the lowest storage cost. What fits?

- A. Route the entries to a Pub/Sub topic
- B. Route the entries to a Cloud Storage bucket
- C. Route the entries to a BigQuery dataset
- D. Set the log bucket retention and lock it

### 72. A national identifier must never reach the log bucket at all. What should be configured?

- A. Redact the email field with a log processor
- B. Route the entries to a Cloud Storage bucket
- C. Sample the high-volume debug entries
- D. Ask analysts not to read the sensitive field

### 73. An operator wants the step change in a chart explained in words. What fits?

- A. Ask Gemini Cloud Assist which span dominates the trace
- B. Ask Gemini Cloud Assist to explain the metric spike
- C. Filter with the Logging query language on the resource label
- D. Ask Gemini Cloud Assist to summarise the failing entries

### 74. Host metrics must come from the VMs, and accepted connections must be recorded per subnet. Which two sources apply? Select two.

- A. Turn on VPC Flow Logs for the subnet
- B. Read the Cloud Service Mesh telemetry
- C. Enable Data Access audit logs for the service
- D. Install the Ops Agent on the instances
- E. Run an OpenTelemetry Collector in the cluster

### 75. A compliance officer needs a record of reads on a dataset. What provides it?

- A. Enable Data Access audit logs for the service
- B. Install the Ops Agent on the instances
- C. Read the Cloud Service Mesh telemetry
- D. Turn on VPC Flow Logs for the subnet

### 76. A pricing service must publish how many quotes it served. What should it do?

- A. Create a log-based metric for the error string
- B. Create an uptime check against the login flow
- C. Emit a custom metric for the business event
- D. Scrape the workload with managed collection for Prometheus

### 77. An expired certificate on a public endpoint must be caught before users meet it. What fits?

- A. Create a log-based metric for the error string
- B. Create an uptime check against the login flow
- C. Emit a custom metric for the business event
- D. Scrape the workload with managed collection for Prometheus

### 78. Responders keep asking where the runbook lives during an incident. What fits?

- A. Create an alerting policy on the SLO burn rate
- B. Build one dashboard and share it with the on-call rotation
- C. Add an email notification channel for the on-call group
- D. Attach the remediation playbook to the alert

### 79. A new team must see the same golden signals as everyone else on day one. What should be built?

- A. Send the alert to PagerDuty through a webhook
- B. Build one dashboard and share it with the on-call rotation
- C. Attach the remediation playbook to the alert
- D. Alert when CPU stays above ninety percent for ten minutes

### 80. Pages must follow user-visible reliability, and the audit team needs a copy by mail. Which two should be configured? Select two.

- A. Add an email notification channel for the on-call group
- B. Send the alert to PagerDuty through a webhook
- C. Attach the remediation playbook to the alert
- D. Create an alerting policy on the SLO burn rate
- E. Alert when CPU stays above ninety percent for ten minutes

### 81. A threshold page fires nightly for a batch host that is meant to be busy. What is the flaw?

- A. Create an alerting policy on the SLO burn rate
- B. Alert when CPU stays above ninety percent for ten minutes
- C. Send the alert to PagerDuty through a webhook
- D. Attach the remediation playbook to the alert

### 82. The on-call tool must be told automatically rather than by email. What fits?

- A. Send the alert to PagerDuty through a webhook
- B. Add an email notification channel for the on-call group
- C. Attach the remediation playbook to the alert
- D. Create an alerting policy on the SLO burn rate

### 83. A trace shows a wide gap before the first span appears. What explains it?

- A. Put the trace ID in the structured log line
- B. Ask Gemini Cloud Assist which span dominates the trace
- C. Instrument the service with OpenTelemetry spans
- D. Read the trace waterfall to find the slow span

### 84. Support pastes a log line and an engineer must fetch the whole trace. What makes that possible?

- A. Log a timestamp and correlate by eye later
- B. Put the trace ID in the structured log line
- C. Instrument the service with OpenTelemetry spans
- D. Read the trace waterfall to find the slow span

### 85. A reviewer wants the dominant span named, and the latency compared with saturation. Which two approaches apply? Select two.

- A. Put the trace ID in the structured log line
- B. Read the trace waterfall to find the slow span
- C. Instrument the service with OpenTelemetry spans
- D. Compare latency with the saturation metric
- E. Ask Gemini Cloud Assist which span dominates the trace

### 86. A deployment stopped creating instances and the error mentions a limit. What should be checked?

- A. Check the DNS record and its remaining TTL
- B. Inspect the image pull credential and repository permission
- C. Read the firewall rule that hit the denied flow
- D. Check the quota error in the deployment log

### 87. External calls from one node fail only under heavy load. What should be checked?

- A. Check the quota error in the deployment log
- B. Read the firewall rule that hit the denied flow
- C. Check Cloud NAT port exhaustion for the egress range
- D. Inspect the image pull credential and repository permission

### 88. A cutover appears complete, yet a fraction of users still reach the old host. What explains it?

- A. Check the DNS record and its remaining TTL
- B. Check Cloud NAT port exhaustion for the egress range
- C. Profile the slow endpoint inside the application
- D. Read the firewall rule that hit the denied flow

---

## Domain 5 — Optimizing Performance and Cost (FinOps and Performance Tuning)

### 89. A migration claims to have halved p99 latency and nobody can verify the claim. What should be used?

- A. Apply the cost recommender suggestion for the idle disks
- B. Measure request latency by endpoint in Cloud Monitoring
- C. Track the service objective on a shared dashboard
- D. Export billing data to BigQuery for the chargeback report

### 90. An executive asks monthly whether each service met its reliability goal. What answers that?

- A. Apply the cost recommender suggestion for the idle disks
- B. Measure request latency by endpoint in Cloud Monitoring
- C. Track the service objective on a shared dashboard
- D. Measure log volume per service before choosing a retention period

### 91. Idle resources must be found, and the fix for a recurring peak failure must be found. Which two recommenders apply? Select two.

- A. Run the batch on Spot VMs
- B. Export billing data to BigQuery for the chargeback report
- C. Apply the reliability recommender for the missing quota
- D. Review the Active Assist recommendations for the project
- E. Apply the cost recommender suggestion for the idle disks

### 92. A team does not know the recommendations exist until somebody opens the console. What fits?

- A. Apply the cost recommender suggestion for the idle disks
- B. Apply the reliability recommender for the missing quota
- C. Export billing data to BigQuery for the chargeback report
- D. Review the Active Assist recommendations for the project

### 93. A retention proposal must be priced before anyone approves it. What should be done first?

- A. Set the log bucket retention and lock it
- B. Exclude the debug stream and keep the error stream
- C. Measure log volume per service before choosing a retention period
- D. Drop the high-cardinality user label from the metric

### 94. Warnings and errors must stay while verbose output goes. What should be done?

- A. Serve the bulk export over the Standard network tier
- B. Drop the high-cardinality user label from the metric
- C. Exclude the debug stream and keep the error stream
- D. Measure log volume per service before choosing a retention period

### 95. A queue worker pool survives interruptions and dominates the compute bill. What fits?

- A. Put the stateless workers on a Spot node pool
- B. Move the primary database onto Spot capacity
- C. Run the batch on Spot VMs
- D. Buy a committed-use discount for the steady baseline

### 96. A proposal puts the write primary on reclaimable capacity to save money. What is the risk?

- A. Put the stateless workers on a Spot node pool
- B. Buy a committed-use discount for the steady baseline
- C. Move the primary database onto Spot capacity
- D. Run the batch on Spot VMs

### 97. A steady two-year baseline should carry a discount on its unit price. What fits?

- A. Run the batch on Spot VMs
- B. Serve the bulk export over the Standard network tier
- C. Rely on sustained-use discounts for the steady baseline
- D. Buy a committed-use discount for the steady baseline

### 98. A nightly cross-region backup copy may use the slower path. What fits?

- A. Serve the bulk export over the Standard network tier
- B. Buy a committed-use discount for the steady baseline
- C. Keep the interactive traffic on the Premium tier
- D. Put the stateless workers on a Spot node pool

### 99. The pool reserves more CPU than it uses, and non-production hosts sit idle overnight. Which two actions apply? Select two.

- A. Stop the idle non-production instances on a schedule
- B. Right-size the node pool from the observed requests
- C. Set a minimum instance count for the latency-critical service
- D. Buy a committed-use discount for the steady baseline
- E. Keep the minimum instance count at zero for the internal tool

### 100. A developer tool is unused after six in the evening and must not bill overnight. What fits?

- A. Keep the minimum instance count at zero for the internal tool
- B. Set a minimum instance count for the latency-critical service
- C. Right-size the node pool from the observed requests
- D. Buy a committed-use discount for the steady baseline

---

## Answer key and explanations

### Question 1 — B

Answer: Apply the constraint to the business unit folder. A folder under the parent inherits the parent's constraints. A constraint attached to one folder and inherited by its projects. Local study-map skill 1.1 (Resource Hierarchy and Project Organization), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 1 (bootstrapping and maintaining a Google Cloud organization): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. An explicit denial that overrides any allow. Why the correct answer wins: A folder under the parent inherits the parent's constraints.
- **B:** Correct. A constraint attached to one folder and inherited by its projects. In this case: A folder under the parent inherits the parent's constraints.
- **C:** Incorrect for this question. A constraint set per project with no inheritance. Why the correct answer wins: A folder under the parent inherits the parent's constraints.
- **D:** Incorrect for this question. An organization-level constraint that every folder and project inherits. Why the correct answer wins: A folder under the parent inherits the parent's constraints.

### Question 2 — C

Answer: Group projects by environment with applications below. Environment-first folders make production isolation explicit. An environment-centric layout that separates production from staging first. Local study-map skill 1.1 (Resource Hierarchy and Project Organization), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 1 (bootstrapping and maintaining a Google Cloud organization): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. An application-centric layout that keeps one service and its owners together. Why the correct answer wins: Environment-first folders make production isolation explicit.
- **B:** Incorrect for this question. A constraint attached to one folder and inherited by its projects. Why the correct answer wins: Environment-first folders make production isolation explicit.
- **C:** Correct. An environment-centric layout that separates production from staging first. In this case: Environment-first folders make production isolation explicit.
- **D:** Incorrect for this question. A constraint set per project with no inheritance. Why the correct answer wins: Environment-first folders make production isolation explicit.

### Question 3 — D

Answer: Create a Shared VPC host project and attach the service projects. One host project applies the change to every attached service. A central network project that lends subnets to other projects. Local study-map skill 1.2 (Shared Networking for Multi-Project Estates), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 1 (bootstrapping and maintaining a Google Cloud organization): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A private endpoint that consumes a published service. Why the correct answer wins: One host project applies the change to every attached service.
- **B:** Incorrect for this question. A mesh of peering links that grows with each new project. Why the correct answer wins: One host project applies the change to every attached service.
- **C:** Incorrect for this question. Duplicate networks with a separately managed egress path. Why the correct answer wins: One host project applies the change to every attached service.
- **D:** Correct. A central network project that lends subnets to other projects. In this case: One host project applies the change to every attached service.

### Question 4 — D

Answer: Peer every project VPC with every other project VPC. Peering connects the two networks for that pilot. A mesh of peering links that grows with each new project. Local study-map skill 1.2 (Shared Networking for Multi-Project Estates), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 1 (bootstrapping and maintaining a Google Cloud organization): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Duplicate networks with a separately managed egress path. Why the correct answer wins: Peering connects the two networks for that pilot.
- **B:** Incorrect for this question. A central network project that lends subnets to other projects. Why the correct answer wins: Peering connects the two networks for that pilot.
- **C:** Incorrect for this question. A private endpoint that consumes a published service. Why the correct answer wins: Peering connects the two networks for that pilot.
- **D:** Correct. A mesh of peering links that grows with each new project. In this case: Peering connects the two networks for that pilot.

### Question 5 — B

Answer: Keep one log bucket inside each project. Per-project buckets scatter the evidence across teams. Log storage scoped to the project that produced the entries. Local study-map skill 1.3 (Multi-Project Monitoring and Logging), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 1 (bootstrapping and maintaining a Google Cloud organization): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A sink that lands logs in a queryable table. Why the correct answer wins: Per-project buckets scatter the evidence across teams.
- **B:** Correct. Log storage scoped to the project that produced the entries. In this case: Per-project buckets scatter the evidence across teams.
- **C:** Incorrect for this question. A single destination that collects entries from many projects. Why the correct answer wins: Per-project buckets scatter the evidence across teams.
- **D:** Incorrect for this question. An observability scope that spans several projects. Why the correct answer wins: Per-project buckets scatter the evidence across teams.

### Question 6 — B, D

Answers: Enforce the restriction with an organization policy constraint; Grant a predefined role once at the folder. The org policy binds the guardrail, and the predefined role covers the reads. A guardrail that holds regardless of the IAM grants. A Google-managed role bound at folder level. Local study-map skill 1.4 (IAM Roles and Organization Policies), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 1 (bootstrapping and maintaining a Google Cloud organization): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A role defined from an explicit permission list. Why the correct answer wins: The org policy binds the guardrail, and the predefined role covers the reads.
- **B:** Correct. A guardrail that holds regardless of the IAM grants. In this case: The org policy binds the guardrail, and the predefined role covers the reads.
- **C:** Incorrect for this question. Separate identities so a staging credential cannot act in production. Why the correct answer wins: The org policy binds the guardrail, and the predefined role covers the reads.
- **D:** Correct. A Google-managed role bound at folder level. In this case: The org policy binds the guardrail, and the predefined role covers the reads.
- **E:** Incorrect for this question. An explicit denial that overrides any allow. Why the correct answer wins: The org policy binds the guardrail, and the predefined role covers the reads.

### Question 7 — D

Answer: Grant a custom role limited to the required permissions. A custom role lists exactly those four permissions. A role defined from an explicit permission list. Local study-map skill 1.4 (IAM Roles and Organization Policies), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 1 (bootstrapping and maintaining a Google Cloud organization): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A guardrail that holds regardless of the IAM grants. Why the correct answer wins: A custom role lists exactly those four permissions.
- **B:** Incorrect for this question. An explicit denial that overrides any allow. Why the correct answer wins: A custom role lists exactly those four permissions.
- **C:** Incorrect for this question. A Google-managed role bound at folder level. Why the correct answer wins: A custom role lists exactly those four permissions.
- **D:** Correct. A role defined from an explicit permission list. In this case: A custom role lists exactly those four permissions.

### Question 8 — D

Answer: Grant impersonation of the service account instead of a key. Impersonation issues short-lived credentials instead of a key. Short-lived credentials obtained by impersonating the account. Local study-map skill 1.5 (Service Account Management), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 1 (bootstrapping and maintaining a Google Cloud organization): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A dedicated identity for each deployed workload. Why the correct answer wins: Impersonation issues short-lived credentials instead of a key.
- **B:** Incorrect for this question. The account created automatically with broad project access. Why the correct answer wins: Impersonation issues short-lived credentials instead of a key.
- **C:** Incorrect for this question. A long-lived credential stored outside the platform. Why the correct answer wins: Impersonation issues short-lived credentials instead of a key.
- **D:** Correct. Short-lived credentials obtained by impersonating the account. In this case: Impersonation issues short-lived credentials instead of a key.

### Question 9 — B

Answer: Place the resources in a region that satisfies the residency rule. The contract narrows the choice to the permitted location. A location choice that keeps data inside the required boundary. Local study-map skill 1.6 (Data Residency in the Hierarchy), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 1 (bootstrapping and maintaining a Google Cloud organization): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A central network project that lends subnets to other projects. Why the correct answer wins: The contract narrows the choice to the permitted location.
- **B:** Correct. A location choice that keeps data inside the required boundary. In this case: The contract narrows the choice to the permitted location.
- **C:** Incorrect for this question. A copy held elsewhere for recovery rather than residency. Why the correct answer wins: The contract narrows the choice to the permitted location.
- **D:** Incorrect for this question. An organization-level constraint that every folder and project inherits. Why the correct answer wins: The contract narrows the choice to the permitted location.

### Question 10 — A

Answer: Define the estate as Terraform modules held in version control. A module parameterises the pattern for each team. Declarative code that is reviewed before it is applied. Local study-map skill 1.7 (Infrastructure-as-Code Tool Selection), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 1 (bootstrapping and maintaining a Google Cloud organization): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Correct. Declarative code that is reviewed before it is applied. In this case: A module parameterises the pattern for each team.
- **B:** Incorrect for this question. A managed service that runs Terraform deployments. Why the correct answer wins: A module parameterises the pattern for each team.
- **C:** Incorrect for this question. A controller that keeps Kubernetes manifests and cloud resources aligned. Why the correct answer wins: A module parameterises the pattern for each team.
- **D:** Incorrect for this question. A templated bundle of Kubernetes resources. Why the correct answer wins: A module parameterises the pattern for each team.

### Question 11 — A

Answer: Reconcile the resources with Config Connector. Config Connector maps manifests onto cloud resources. A controller that keeps Kubernetes manifests and cloud resources aligned. Local study-map skill 1.7 (Infrastructure-as-Code Tool Selection), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 1 (bootstrapping and maintaining a Google Cloud organization): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Correct. A controller that keeps Kubernetes manifests and cloud resources aligned. In this case: Config Connector maps manifests onto cloud resources.
- **B:** Incorrect for this question. A transformation pipeline that keeps the source declarative. Why the correct answer wins: Config Connector maps manifests onto cloud resources.
- **C:** Incorrect for this question. Declarative code that is reviewed before it is applied. Why the correct answer wins: Config Connector maps manifests onto cloud resources.
- **D:** Incorrect for this question. A templated bundle of Kubernetes resources. Why the correct answer wins: Config Connector maps manifests onto cloud resources.

### Question 12 — C

Answer: Start from the Cloud Foundation Toolkit blueprints. The toolkit ships vetted foundation blueprints. Google-maintained Terraform templates for common foundations. Local study-map skill 1.8 (Blueprints and Controlled Infrastructure Change), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 1 (bootstrapping and maintaining a Google Cloud organization): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Declarative code that is reviewed before it is applied. Why the correct answer wins: The toolkit ships vetted foundation blueprints.
- **B:** Incorrect for this question. A recurring comparison of declared and actual state. Why the correct answer wins: The toolkit ships vetted foundation blueprints.
- **C:** Correct. Google-maintained Terraform templates for common foundations. In this case: The toolkit ships vetted foundation blueprints.
- **D:** Incorrect for this question. A transformation pipeline that keeps the source declarative. Why the correct answer wins: The toolkit ships vetted foundation blueprints.

### Question 13 — B

Answer: Run the documented gcloud commands by hand for each environment. Typing the commands by hand invites transcription errors. A manual sequence repeated on every occasion. Local study-map skill 1.9 (Automation with Scripting and APIs), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 1 (bootstrapping and maintaining a Google Cloud organization): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Idempotent automation through the client library. Why the correct answer wins: Typing the commands by hand invites transcription errors.
- **B:** Correct. A manual sequence repeated on every occasion. In this case: Typing the commands by hand invites transcription errors.
- **C:** Incorrect for this question. An unmanaged change with no enforceable record. Why the correct answer wins: Typing the commands by hand invites transcription errors.
- **D:** Incorrect for this question. A recurring comparison of declared and actual state. Why the correct answer wins: Typing the commands by hand invites transcription errors.

### Question 14 — C, D

Answers: Use Cloud Build for CI and Cloud Deploy for delivery; Let Argo CD pull the manifests from Git. Cloud Build runs the build, and Argo CD reconciles from Git. A managed pair that separates building from releasing. A pull-based delivery controller. Local study-map skill 1.10 (CI/CD Architecture Stack Design), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 1 (bootstrapping and maintaining a Google Cloud organization): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A regional repository for images and packages. Why the correct answer wins: Cloud Build runs the build, and Argo CD reconciles from Git.
- **B:** Incorrect for this question. A reproducible image built before deployment. Why the correct answer wins: Cloud Build runs the build, and Argo CD reconciles from Git.
- **C:** Correct. A managed pair that separates building from releasing. In this case: Cloud Build runs the build, and Argo CD reconciles from Git.
- **D:** Correct. A pull-based delivery controller. In this case: Cloud Build runs the build, and Argo CD reconciles from Git.
- **E:** Incorrect for this question. A self-operated CI server whose patching is your problem. Why the correct answer wins: Cloud Build runs the build, and Argo CD reconciles from Git.

### Question 15 — A

Answer: Bake the machine image with Packer. Packer rebuilds the image from the patched base. A reproducible image built before deployment. Local study-map skill 1.10 (CI/CD Architecture Stack Design), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 1 (bootstrapping and maintaining a Google Cloud organization): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Correct. A reproducible image built before deployment. In this case: Packer rebuilds the image from the patched base.
- **B:** Incorrect for this question. Declarative code that is reviewed before it is applied. Why the correct answer wins: Packer rebuilds the image from the patched base.
- **C:** Incorrect for this question. A regional repository for images and packages. Why the correct answer wins: Packer rebuilds the image from the patched base.
- **D:** Incorrect for this question. A templated bundle of Kubernetes resources. Why the correct answer wins: Packer rebuilds the image from the patched base.

### Question 16 — A

Answer: Render the manifests through a kpt function pipeline. The pipeline normalises each source to one convention. A transformation pipeline that keeps the source declarative. Local study-map skill 1.11 (Third-Party Tooling in the Pipeline), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 1 (bootstrapping and maintaining a Google Cloud organization): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Correct. A transformation pipeline that keeps the source declarative. In this case: The pipeline normalises each source to one convention.
- **B:** Incorrect for this question. A templated bundle of Kubernetes resources. Why the correct answer wins: The pipeline normalises each source to one convention.
- **C:** Incorrect for this question. A recurring comparison of declared and actual state. Why the correct answer wins: The pipeline normalises each source to one convention.
- **D:** Incorrect for this question. Declarative code that is reviewed before it is applied. Why the correct answer wins: The pipeline normalises each source to one convention.

### Question 17 — A, B

Answers: Create a short-lived project per change and delete it after review; Keep one base with a Kustomize overlay per environment. The disposable project holds the review build, and the overlay patches the manifests. An environment that exists only while a change is tested. A base manifest with per-environment patches. Local study-map skill 1.12 (Multiple Environment Management), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 1 (bootstrapping and maintaining a Google Cloud organization): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Correct. A base manifest with per-environment patches. In this case: The disposable project holds the review build, and the overlay patches the manifests.
- **B:** Correct. An environment that exists only while a change is tested. In this case: The disposable project holds the review build, and the overlay patches the manifests.
- **C:** Incorrect for this question. A constraint attached to one folder and inherited by its projects. Why the correct answer wins: The disposable project holds the review build, and the overlay patches the manifests.
- **D:** Incorrect for this question. One image per environment with the settings compiled in. Why the correct answer wins: The disposable project holds the review build, and the overlay patches the manifests.
- **E:** Incorrect for this question. A permanent pre-production environment. Why the correct answer wins: The disposable project holds the review build, and the overlay patches the manifests.

### Question 18 — A

Answer: Register the clusters in a fleet. A fleet applies policy and identity across its clusters. A group that shares policy and identity across clusters. Local study-map skill 1.13 (Fleets, Patching, and Cluster Upgrades), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 1 (bootstrapping and maintaining a Google Cloud organization): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Correct. A group that shares policy and identity across clusters. In this case: A fleet applies policy and identity across its clusters.
- **B:** Incorrect for this question. An environment that exists only while a change is tested. Why the correct answer wins: A fleet applies policy and identity across its clusters.
- **C:** Incorrect for this question. An operator-driven upgrade with no cadence. Why the correct answer wins: A fleet applies policy and identity across its clusters.
- **D:** Incorrect for this question. A parallel cluster used to prove the upgrade. Why the correct answer wins: A fleet applies policy and identity across its clusters.

### Question 19 — D

Answer: Rely on Cloud Shell for every developer. A browser terminal does not persist the toolchain. A browser terminal with limited tooling and lifetime. Local study-map skill 1.14 (Secure Development Environments and AI Assistance), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 1 (bootstrapping and maintaining a Google Cloud organization): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A pinned toolchain that every workstation starts from. Why the correct answer wins: A browser terminal does not persist the toolchain.
- **B:** Incorrect for this question. A managed IDE that runs inside the project boundary. Why the correct answer wins: A browser terminal does not persist the toolchain.
- **C:** Incorrect for this question. Unmanaged toolchains on unmanaged machines. Why the correct answer wins: A browser terminal does not persist the toolchain.
- **D:** Correct. A browser terminal with limited tooling and lifetime. In this case: A browser terminal does not persist the toolchain.

### Question 20 — C

Answer: Use Gemini Code Assist for the suggested change. Gemini Code Assist explains the code in the editor. An in-editor assistant that proposes code. Local study-map skill 1.14 (Secure Development Environments and AI Assistance), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 1 (bootstrapping and maintaining a Google Cloud organization): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A pinned toolchain that every workstation starts from. Why the correct answer wins: Gemini Code Assist explains the code in the editor.
- **B:** Incorrect for this question. A terminal assistant that drafts and runs commands. Why the correct answer wins: Gemini Code Assist explains the code in the editor.
- **C:** Correct. An in-editor assistant that proposes code. In this case: Gemini Code Assist explains the code in the editor.
- **D:** Incorrect for this question. An assistant that reads telemetry and configuration. Why the correct answer wins: Gemini Code Assist explains the code in the editor.

### Question 21 — B

Answer: Create a Cloud Build trigger on the release branch. A branch trigger runs when those files change. A trigger that starts the build on a branch change. Local study-map skill 2.1 (Pipeline Triggers and Design), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 2 (building and implementing CI/CD pipelines): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A hand-built artifact with no pipeline record. Why the correct answer wins: A branch trigger runs when those files change.
- **B:** Correct. A trigger that starts the build on a branch change. In this case: A branch trigger runs when those files change.
- **C:** Incorrect for this question. A pre-merge check that blocks a bad change early. Why the correct answer wins: A branch trigger runs when those files change.
- **D:** Incorrect for this question. A release build that a tag alone can start. Why the correct answer wins: A branch trigger runs when those files change.

### Question 22 — B

Answer: Trigger the pipeline only on a signed tag. The tag trigger builds only from the signed tag. A release build that a tag alone can start. Local study-map skill 2.1 (Pipeline Triggers and Design), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 2 (building and implementing CI/CD pipelines): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A trigger that starts the build on a branch change. Why the correct answer wins: The tag trigger builds only from the signed tag.
- **B:** Correct. A release build that a tag alone can start. In this case: The tag trigger builds only from the signed tag.
- **C:** Incorrect for this question. A pre-merge check that blocks a bad change early. Why the correct answer wins: The tag trigger builds only from the signed tag.
- **D:** Incorrect for this question. A required human approval before the release promotes. Why the correct answer wins: The tag trigger builds only from the signed tag.

### Question 23 — C

Answer: Have an engineer build locally and upload the result. Building locally lets machine differences change the result. A hand-built artifact with no pipeline record. Local study-map skill 2.1 (Pipeline Triggers and Design), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 2 (building and implementing CI/CD pipelines): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A release build that a tag alone can start. Why the correct answer wins: Building locally lets machine differences change the result.
- **B:** Incorrect for this question. A pre-merge check that blocks a bad change early. Why the correct answer wins: Building locally lets machine differences change the result.
- **C:** Correct. A hand-built artifact with no pipeline record. In this case: Building locally lets machine differences change the result.
- **D:** Incorrect for this question. The immutable record of who released what. Why the correct answer wins: Building locally lets machine differences change the result.

### Question 24 — A, D

Answers: Store the build output in Artifact Registry; Tag each artifact with the commit SHA and forbid overwrite. The registry stores regionally, and the immutable tag prevents overwrite. A regional repository for images and packages. An immutable tag that identifies the source revision. Local study-map skill 2.2 (Artifact Management), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 2 (building and implementing CI/CD pipelines): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Correct. A regional repository for images and packages. In this case: The registry stores regionally, and the immutable tag prevents overwrite.
- **B:** Incorrect for this question. A moving tag that hides which build is running. Why the correct answer wins: The registry stores regionally, and the immutable tag prevents overwrite.
- **C:** Incorrect for this question. A reproducible image built before deployment. Why the correct answer wins: The registry stores regionally, and the immutable tag prevents overwrite.
- **D:** Correct. An immutable tag that identifies the source revision. In this case: The registry stores regionally, and the immutable tag prevents overwrite.
- **E:** Incorrect for this question. The legacy registry without regional repository controls. Why the correct answer wins: The registry stores regionally, and the immutable tag prevents overwrite.

### Question 25 — C

Answer: Reuse the latest tag for every build. Re-pushing the same tag replaced the artifact silently. A moving tag that hides which build is running. Local study-map skill 2.2 (Artifact Management), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 2 (building and implementing CI/CD pipelines): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A regional repository for images and packages. Why the correct answer wins: Re-pushing the same tag replaced the artifact silently.
- **B:** Incorrect for this question. An immutable tag that identifies the source revision. Why the correct answer wins: Re-pushing the same tag replaced the artifact silently.
- **C:** Correct. A moving tag that hides which build is running. In this case: Re-pushing the same tag replaced the artifact silently.
- **D:** Incorrect for this question. Metadata that ties an artifact to its build inputs. Why the correct answer wins: Re-pushing the same tag replaced the artifact silently.

### Question 26 — B

Answer: Define the attached cluster as the delivery target. The attached cluster is registered as a delivery target. A target that points at a GKE cluster outside Google Cloud. Local study-map skill 2.3 (Hybrid and Multicloud Deployment Targets), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 2 (building and implementing CI/CD pipelines): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A revision-based target with traffic control. Why the correct answer wins: The attached cluster is registered as a delivery target.
- **B:** Correct. A target that points at a GKE cluster outside Google Cloud. In this case: The attached cluster is registered as a delivery target.
- **C:** Incorrect for this question. A required human approval before the release promotes. Why the correct answer wins: The attached cluster is registered as a delivery target.
- **D:** Incorrect for this question. A delivery target that sits inside the same project. Why the correct answer wins: The attached cluster is registered as a delivery target.

### Question 27 — A

Answer: Deliver to a Cloud Run service revision. A Cloud Run target handles the traffic split. A revision-based target with traffic control. Local study-map skill 2.3 (Hybrid and Multicloud Deployment Targets), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 2 (building and implementing CI/CD pipelines): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Correct. A revision-based target with traffic control. In this case: A Cloud Run target handles the traffic split.
- **B:** Incorrect for this question. A target that points at a GKE cluster outside Google Cloud. Why the correct answer wins: A Cloud Run target handles the traffic split.
- **C:** Incorrect for this question. The immutable record of who released what. Why the correct answer wins: A Cloud Run target handles the traffic split.
- **D:** Incorrect for this question. A delivery target that sits inside the same project. Why the correct answer wins: A Cloud Run target handles the traffic split.

### Question 28 — B

Answer: Add a Cloud Deploy approval gate before production. An approval gate requires that human sign-off. A required human approval before the release promotes. Local study-map skill 2.4 (Approval Flows and Deployment Process), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 2 (building and implementing CI/CD pipelines): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. The immutable record of who released what. Why the correct answer wins: An approval gate requires that human sign-off.
- **B:** Correct. A required human approval before the release promotes. In this case: An approval gate requires that human sign-off.
- **C:** Incorrect for this question. An unattended path from commit to production. Why the correct answer wins: An approval gate requires that human sign-off.
- **D:** Incorrect for this question. A hand-built artifact with no pipeline record. Why the correct answer wins: An approval gate requires that human sign-off.

### Question 29 — C

Answer: Read Cloud Audit Logs for the release history. Cloud Audit Logs name the identity and the time. The immutable record of who released what. Local study-map skill 2.5 (Deployment Auditing and Tracking), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 2 (building and implementing CI/CD pipelines): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. An immutable tag that identifies the source revision. Why the correct answer wins: Cloud Audit Logs name the identity and the time.
- **B:** Incorrect for this question. A published statement about how the artifact was produced. Why the correct answer wins: Cloud Audit Logs name the identity and the time.
- **C:** Correct. The immutable record of who released what. In this case: Cloud Audit Logs name the identity and the time.
- **D:** Incorrect for this question. Metadata that ties an artifact to its build inputs. Why the correct answer wins: Cloud Audit Logs name the identity and the time.

### Question 30 — A

Answer: Inspect the build provenance attestation. Provenance records the builder and the commit. Metadata that ties an artifact to its build inputs. Local study-map skill 2.5 (Deployment Auditing and Tracking), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 2 (building and implementing CI/CD pipelines): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Correct. Metadata that ties an artifact to its build inputs. In this case: Provenance records the builder and the commit.
- **B:** Incorrect for this question. A published statement about how the artifact was produced. Why the correct answer wins: Provenance records the builder and the commit.
- **C:** Incorrect for this question. The immutable record of who released what. Why the correct answer wins: Provenance records the builder and the commit.
- **D:** Incorrect for this question. An immutable tag that identifies the source revision. Why the correct answer wins: Provenance records the builder and the commit.

### Question 31 — B, C

Answers: Send ten percent of traffic to the new revision and watch the SLI; Put the behaviour behind a feature flag. The canary limits exposure, and the flag switches behaviour off. A small traffic slice that bounds the blast radius. A runtime switch that separates deploy from release. Local study-map skill 2.6 (Deployment Strategies), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 2 (building and implementing CI/CD pipelines): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A full outage during the change. Why the correct answer wins: The canary limits exposure, and the flag switches behaviour off.
- **B:** Correct. A runtime switch that separates deploy from release. In this case: The canary limits exposure, and the flag switches behaviour off.
- **C:** Correct. A small traffic slice that bounds the blast radius. In this case: The canary limits exposure, and the flag switches behaviour off.
- **D:** Incorrect for this question. A gradual replacement of the running instances. Why the correct answer wins: The canary limits exposure, and the flag switches behaviour off.
- **E:** Incorrect for this question. Two full environments with an instant cutover. Why the correct answer wins: The canary limits exposure, and the flag switches behaviour off.

### Question 32 — D

Answer: Replace the instances in batches. Rolling replaces the instances in small batches. A gradual replacement of the running instances. Local study-map skill 2.6 (Deployment Strategies), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 2 (building and implementing CI/CD pipelines): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A small traffic slice that bounds the blast radius. Why the correct answer wins: Rolling replaces the instances in small batches.
- **B:** Incorrect for this question. Two full environments with an instant cutover. Why the correct answer wins: Rolling replaces the instances in small batches.
- **C:** Incorrect for this question. A full outage during the change. Why the correct answer wins: Rolling replaces the instances in small batches.
- **D:** Correct. A gradual replacement of the running instances. In this case: Rolling replaces the instances in small batches.

### Question 33 — C

Answer: Run the new version alongside and switch traffic at once. Blue/green keeps the old stack warm for an instant return. Two full environments with an instant cutover. Local study-map skill 2.6 (Deployment Strategies), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 2 (building and implementing CI/CD pipelines): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A full outage during the change. Why the correct answer wins: Blue/green keeps the old stack warm for an instant return.
- **B:** Incorrect for this question. A small traffic slice that bounds the blast radius. Why the correct answer wins: Blue/green keeps the old stack warm for an instant return.
- **C:** Correct. Two full environments with an instant cutover. In this case: Blue/green keeps the old stack warm for an instant return.
- **D:** Incorrect for this question. A gradual replacement of the running instances. Why the correct answer wins: Blue/green keeps the old stack warm for an instant return.

### Question 34 — D

Answer: Gate the rollout on the error-rate SLI. The SLI gate abandons the release on budget burn. An automated decision driven by the service objective. Local study-map skill 2.7 (Deployment Success Metrics), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 2 (building and implementing CI/CD pipelines): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A probe that exercises the path from outside. Why the correct answer wins: The SLI gate abandons the release on budget burn.
- **B:** Incorrect for this question. A required human approval before the release promotes. Why the correct answer wins: The SLI gate abandons the release on budget burn.
- **C:** Incorrect for this question. A resource signal that says nothing about user success. Why the correct answer wins: The SLI gate abandons the release on budget burn.
- **D:** Correct. An automated decision driven by the service objective. In this case: The SLI gate abandons the release on budget burn.

### Question 35 — C

Answer: Roll the release back to the previous one. Rolling back returns the consumer to a working release. A return to the last known good release. Local study-map skill 2.8 (Troubleshooting Deployment Issues), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 2 (building and implementing CI/CD pipelines): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. An untracked change to the live environment. Why the correct answer wins: Rolling back returns the consumer to a working release.
- **B:** Incorrect for this question. A safe repeat that converges on the same state. Why the correct answer wins: Rolling back returns the consumer to a working release.
- **C:** Correct. A return to the last known good release. In this case: Rolling back returns the consumer to a working release.
- **D:** Incorrect for this question. The step output that names the failing command. Why the correct answer wins: Rolling back returns the consumer to a working release.

### Question 36 — D

Answer: Start from the failed step log in Cloud Build. The step log contains the exact command. The step output that names the failing command. Local study-map skill 2.8 (Troubleshooting Deployment Issues), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 2 (building and implementing CI/CD pipelines): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A return to the last known good release. Why the correct answer wins: The step log contains the exact command.
- **B:** Incorrect for this question. A safe repeat that converges on the same state. Why the correct answer wins: The step log contains the exact command.
- **C:** Incorrect for this question. The immutable record of who released what. Why the correct answer wins: The step log contains the exact command.
- **D:** Correct. The step output that names the failing command. In this case: The step log contains the exact command.

### Question 37 — B, C

Answers: Encrypt the payload with a Cloud KMS key; Store the credential in Secret Manager with versions. KMS wraps the object, and Secret Manager versions the token. A managed key that wraps the data. A managed store with immutable versions and audit. Local study-map skill 2.9 (Key Management), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 2 (building and implementing CI/CD pipelines): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A store for versioned application parameters. Why the correct answer wins: KMS wraps the object, and Secret Manager versions the token.
- **B:** Correct. A managed key that wraps the data. In this case: KMS wraps the object, and Secret Manager versions the token.
- **C:** Correct. A managed store with immutable versions and audit. In this case: KMS wraps the object, and Secret Manager versions the token.
- **D:** Incorrect for this question. A secret readable by everyone with repository access. Why the correct answer wins: KMS wraps the object, and Secret Manager versions the token.
- **E:** Incorrect for this question. Managed issuance and renewal for the endpoint. Why the correct answer wins: KMS wraps the object, and Secret Manager versions the token.

### Question 38 — A

Answer: Issue and rotate the certificate with Certificate Manager. Certificate Manager issues those workload certificates. Managed issuance and renewal for the endpoint. Local study-map skill 2.9 (Key Management), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 2 (building and implementing CI/CD pipelines): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Correct. Managed issuance and renewal for the endpoint. In this case: Certificate Manager issues those workload certificates.
- **B:** Incorrect for this question. A store for versioned application parameters. Why the correct answer wins: Certificate Manager issues those workload certificates.
- **C:** Incorrect for this question. A managed store with immutable versions and audit. Why the correct answer wins: Certificate Manager issues those workload certificates.
- **D:** Incorrect for this question. A managed key that wraps the data. Why the correct answer wins: Certificate Manager issues those workload certificates.

### Question 39 — C

Answer: Keep the non-secret configuration in Parameter Manager. Parameter Manager keeps the values visible and versioned. A store for versioned application parameters. Local study-map skill 2.10 (Configuration and Secret Management), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 2 (building and implementing CI/CD pipelines): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A secret readable by everyone with repository access. Why the correct answer wins: Parameter Manager keeps the values visible and versioned.
- **B:** Incorrect for this question. A managed store with immutable versions and audit. Why the correct answer wins: Parameter Manager keeps the values visible and versioned.
- **C:** Correct. A store for versioned application parameters. In this case: Parameter Manager keeps the values visible and versioned.
- **D:** Incorrect for this question. One image per environment with the settings compiled in. Why the correct answer wins: Parameter Manager keeps the values visible and versioned.

### Question 40 — C

Answer: Bake the environment settings into the image. Settings in the image force a rebuild for each change. One image per environment with the settings compiled in. Local study-map skill 2.10 (Configuration and Secret Management), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 2 (building and implementing CI/CD pipelines): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A secret readable by everyone with repository access. Why the correct answer wins: Settings in the image force a rebuild for each change.
- **B:** Incorrect for this question. A store for versioned application parameters. Why the correct answer wins: Settings in the image force a rebuild for each change.
- **C:** Correct. One image per environment with the settings compiled in. In this case: Settings in the image force a rebuild for each change.
- **D:** Incorrect for this question. A managed store with immutable versions and audit. Why the correct answer wins: Settings in the image force a rebuild for each change.

### Question 41 — A

Answer: Mount the secret at runtime from Secret Manager. A runtime mount supplies the credential per environment. A credential read only when the workload starts. Local study-map skill 2.11 (Build-Time versus Runtime Secret Injection), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 2 (building and implementing CI/CD pipelines): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Correct. A credential read only when the workload starts. In this case: A runtime mount supplies the credential per environment.
- **B:** Incorrect for this question. A secret baked into an artifact anyone can pull. Why the correct answer wins: A runtime mount supplies the credential per environment.
- **C:** Incorrect for this question. A secret readable by everyone with repository access. Why the correct answer wins: A runtime mount supplies the credential per environment.
- **D:** Incorrect for this question. A value left visible in the build history. Why the correct answer wins: A runtime mount supplies the credential per environment.

### Question 42 — B

Answer: Enable Artifact Analysis scanning on the repository. Artifact Analysis keeps that list per image. Vulnerability findings for the stored artifacts. Local study-map skill 2.12 (Vulnerability Scanning and Artifact Analysis), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 2 (building and implementing CI/CD pipelines): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. An admission check that only attested images may run. Why the correct answer wins: Artifact Analysis keeps that list per image.
- **B:** Correct. Vulnerability findings for the stored artifacts. In this case: Artifact Analysis keeps that list per image.
- **C:** Incorrect for this question. A finding that no pipeline blocks on. Why the correct answer wins: Artifact Analysis keeps that list per image.
- **D:** Incorrect for this question. A policy that blocks the promotion. Why the correct answer wins: Artifact Analysis keeps that list per image.

### Question 43 — A, B

Answers: Enforce Binary Authorization attestations before deploy; Bind deploy permissions only inside the production project. Binary Authorization admits attested images, and the scoped identity stays local. An admission check that only attested images may run. An identity that cannot promote outside its environment. Local study-map skill 2.13 (Supply Chain Security and Binary Authorization), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 2 (building and implementing CI/CD pipelines): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Correct. An admission check that only attested images may run. In this case: Binary Authorization admits attested images, and the scoped identity stays local.
- **B:** Correct. An identity that cannot promote outside its environment. In this case: Binary Authorization admits attested images, and the scoped identity stays local.
- **C:** Incorrect for this question. A finding that no pipeline blocks on. Why the correct answer wins: Binary Authorization admits attested images, and the scoped identity stays local.
- **D:** Incorrect for this question. Vulnerability findings for the stored artifacts. Why the correct answer wins: Binary Authorization admits attested images, and the scoped identity stays local.
- **E:** Incorrect for this question. A policy that blocks the promotion. Why the correct answer wins: Binary Authorization admits attested images, and the scoped identity stays local.

### Question 44 — D

Answer: Fail the pipeline on a critical vulnerability finding. The gate fails the build on that finding. A policy that blocks the promotion. Local study-map skill 2.13 (Supply Chain Security and Binary Authorization), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 2 (building and implementing CI/CD pipelines): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A finding that no pipeline blocks on. Why the correct answer wins: The gate fails the build on that finding.
- **B:** Incorrect for this question. Vulnerability findings for the stored artifacts. Why the correct answer wins: The gate fails the build on that finding.
- **C:** Incorrect for this question. An admission check that only attested images may run. Why the correct answer wins: The gate fails the build on that finding.
- **D:** Correct. A policy that blocks the promotion. In this case: The gate fails the build on that finding.

### Question 45 — A

Answer: Run the pipeline as the default editor service account. A broad editor role gives the pipeline far more than it needs. A build identity with broad write access. Local study-map skill 2.14 (Per-Environment IAM Policy), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 2 (building and implementing CI/CD pipelines): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Correct. A build identity with broad write access. In this case: A broad editor role gives the pipeline far more than it needs.
- **B:** Incorrect for this question. A single broad credential across the whole estate. Why the correct answer wins: A broad editor role gives the pipeline far more than it needs.
- **C:** Incorrect for this question. Separate identities so a staging credential cannot act in production. Why the correct answer wins: A broad editor role gives the pipeline far more than it needs.
- **D:** Incorrect for this question. An identity that cannot promote outside its environment. Why the correct answer wins: A broad editor role gives the pipeline far more than it needs.

### Question 46 — D, E

Answers: Publish a contractual promise with a remedy; Track the ratio of good requests to total requests. The SLA promises the remedy, and the SLI measures the experience. An external commitment that carries a consequence. A measured indicator of how the service behaves. Local study-map skill 3.1 (SLIs, SLOs, and SLAs), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 3 (applying site reliability engineering practices): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. An objective the team commits to without a contract. Why the correct answer wins: The SLA promises the remedy, and the SLI measures the experience.
- **B:** Incorrect for this question. A signal that the budget is going too quickly. Why the correct answer wins: The SLA promises the remedy, and the SLI measures the experience.
- **C:** Incorrect for this question. An explicit trade between reliability and change. Why the correct answer wins: The SLA promises the remedy, and the SLI measures the experience.
- **D:** Correct. A measured indicator of how the service behaves. In this case: The SLA promises the remedy, and the SLI measures the experience.
- **E:** Correct. An external commitment that carries a consequence. In this case: The SLA promises the remedy, and the SLI measures the experience.

### Question 47 — A

Answer: Set an internal target on that indicator. The SLO is the internal bar the team adopts. An objective the team commits to without a contract. Local study-map skill 3.1 (SLIs, SLOs, and SLAs), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 3 (applying site reliability engineering practices): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Correct. An objective the team commits to without a contract. In this case: The SLO is the internal bar the team adopts.
- **B:** Incorrect for this question. A measured indicator of how the service behaves. Why the correct answer wins: The SLO is the internal bar the team adopts.
- **C:** Incorrect for this question. An external commitment that carries a consequence. Why the correct answer wins: The SLO is the internal bar the team adopts.
- **D:** Incorrect for this question. A signal that the budget is going too quickly. Why the correct answer wins: The SLO is the internal bar the team adopts.

### Question 48 — D

Answer: Choose three nines and spend the difference on features. Choosing three nines keeps the cadence affordable. An explicit trade between reliability and change. Local study-map skill 3.1 (SLIs, SLOs, and SLAs), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 3 (applying site reliability engineering practices): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A rule that trades velocity for reliability. Why the correct answer wins: Choosing three nines keeps the cadence affordable.
- **B:** Incorrect for this question. An external commitment that carries a consequence. Why the correct answer wins: Choosing three nines keeps the cadence affordable.
- **C:** Incorrect for this question. A uniform promise that most services do not need. Why the correct answer wins: Choosing three nines keeps the cadence affordable.
- **D:** Correct. An explicit trade between reliability and change. In this case: Choosing three nines keeps the cadence affordable.

### Question 49 — D

Answer: Alert on a fast error-budget burn rate. A multi-window burn rate catches the slow leak. A signal that the budget is going too quickly. Local study-map skill 3.2 (Error Budgets), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 3 (applying site reliability engineering practices): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A static threshold on a resource metric. Why the correct answer wins: A multi-window burn rate catches the slow leak.
- **B:** Incorrect for this question. An external commitment that carries a consequence. Why the correct answer wins: A multi-window burn rate catches the slow leak.
- **C:** Incorrect for this question. A rule that trades velocity for reliability. Why the correct answer wins: A multi-window burn rate catches the slow leak.
- **D:** Correct. A signal that the budget is going too quickly. In this case: A multi-window burn rate catches the slow leak.

### Question 50 — A

Answer: Stop feature releases when the error budget is spent. A spent budget stops launches until it recovers. A rule that trades velocity for reliability. Local study-map skill 3.2 (Error Budgets), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 3 (applying site reliability engineering practices): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Correct. A rule that trades velocity for reliability. In this case: A spent budget stops launches until it recovers.
- **B:** Incorrect for this question. A signal that the budget is going too quickly. Why the correct answer wins: A spent budget stops launches until it recovers.
- **C:** Incorrect for this question. An external commitment that carries a consequence. Why the correct answer wins: A spent budget stops launches until it recovers.
- **D:** Incorrect for this question. A uniform promise that most services do not need. Why the correct answer wins: A spent budget stops launches until it recovers.

### Question 51 — D

Answer: Assume five nines for every service. A uniform extreme target spends effort where it is not needed. A uniform promise that most services do not need. Local study-map skill 3.3 (Cost of Reliability and Nines), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 3 (applying site reliability engineering practices): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. An explicit trade between reliability and change. Why the correct answer wins: A uniform extreme target spends effort where it is not needed.
- **B:** Incorrect for this question. Capacity arranged ahead of a known peak. Why the correct answer wins: A uniform extreme target spends effort where it is not needed.
- **C:** Incorrect for this question. An external commitment that carries a consequence. Why the correct answer wins: A uniform extreme target spends effort where it is not needed.
- **D:** Correct. A uniform promise that most services do not need. In this case: A uniform extreme target spends effort where it is not needed.

### Question 52 — C

Answer: Choose three nines and spend the difference on features. The trade-off favours fewer nines and more delivery. An explicit trade between reliability and change. Local study-map skill 3.3 (Cost of Reliability and Nines), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 3 (applying site reliability engineering practices): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A uniform promise that most services do not need. Why the correct answer wins: The trade-off favours fewer nines and more delivery.
- **B:** Incorrect for this question. An owned entry with its tier and dependencies. Why the correct answer wins: The trade-off favours fewer nines and more delivery.
- **C:** Correct. An explicit trade between reliability and change. In this case: The trade-off favours fewer nines and more delivery.
- **D:** Incorrect for this question. An external commitment that carries a consequence. Why the correct answer wins: The trade-off favours fewer nines and more delivery.

### Question 53 — C

Answer: Register the service in the service catalog. The catalog declares the owning team for each service. An owned entry with its tier and dependencies. Local study-map skill 3.4 (Service Lifecycle Management), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 3 (applying site reliability engineering practices): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A planned withdrawal with a migration path. Why the correct answer wins: The catalog declares the owning team for each service.
- **B:** Incorrect for this question. An unowned workload that still costs money. Why the correct answer wins: The catalog declares the owning team for each service.
- **C:** Correct. An owned entry with its tier and dependencies. In this case: The catalog declares the owning team for each service.
- **D:** Incorrect for this question. Extra supply in a different location. Why the correct answer wins: The catalog declares the owning team for each service.

### Question 54 — B

Answer: Leave the unused service running for now. An unowned service keeps billing until it is retired. An unowned workload that still costs money. Local study-map skill 3.4 (Service Lifecycle Management), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 3 (applying site reliability engineering practices): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A planned withdrawal with a migration path. Why the correct answer wins: An unowned service keeps billing until it is retired.
- **B:** Correct. An unowned workload that still costs money. In this case: An unowned service keeps billing until it is retired.
- **C:** Incorrect for this question. An owned entry with its tier and dependencies. Why the correct answer wins: An unowned service keeps billing until it is retired.
- **D:** Incorrect for this question. A graceful handover of in-flight requests. Why the correct answer wins: An unowned service keeps billing until it is retired.

### Question 55 — B

Answer: Request a quota increase and reserve capacity before the launch. A quota increase covers the two-day peak. Capacity arranged ahead of a known peak. Local study-map skill 3.5 (Capacity Planning and Quotas), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 3 (applying site reliability engineering practices): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Limits that throttle at the worst possible moment. Why the correct answer wins: A quota increase covers the two-day peak.
- **B:** Correct. Capacity arranged ahead of a known peak. In this case: A quota increase covers the two-day peak.
- **C:** Incorrect for this question. Calendar-driven capacity with no feedback loop. Why the correct answer wins: A quota increase covers the two-day peak.
- **D:** Incorrect for this question. A flexible placement into a cheaper window. Why the correct answer wins: A quota increase covers the two-day peak.

### Question 56 — B

Answer: Schedule the batch with Dynamic Workload Scheduler. The scheduler places it in the cheapest hour. A flexible placement into a cheaper window. Local study-map skill 3.5 (Capacity Planning and Quotas), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 3 (applying site reliability engineering practices): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Calendar-driven capacity with no feedback loop. Why the correct answer wins: The scheduler places it in the cheapest hour.
- **B:** Correct. A flexible placement into a cheaper window. In this case: The scheduler places it in the cheapest hour.
- **C:** Incorrect for this question. Capacity arranged ahead of a known peak. Why the correct answer wins: The scheduler places it in the cheapest hour.
- **D:** Incorrect for this question. Managed instance scaling from a resource metric. Why the correct answer wins: The scheduler places it in the cheapest hour.

### Question 57 — D

Answer: Scale on queue depth with a horizontal pod autoscaler. The backlog size tells the autoscaler to add workers. Replica scaling driven by a work signal. Local study-map skill 3.6 (Autoscaling), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 3 (applying site reliability engineering practices): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Calendar-driven capacity with no feedback loop. Why the correct answer wins: The backlog size tells the autoscaler to add workers.
- **B:** Incorrect for this question. Managed instance scaling from a resource metric. Why the correct answer wins: The backlog size tells the autoscaler to add workers.
- **C:** Incorrect for this question. Concurrency-based replica scaling. Why the correct answer wins: The backlog size tells the autoscaler to add workers.
- **D:** Correct. Replica scaling driven by a work signal. In this case: The backlog size tells the autoscaler to add workers.

### Question 58 — C

Answer: Set Cloud Run concurrency so replicas follow load. Concurrency lets one instance serve several requests. Concurrency-based replica scaling. Local study-map skill 3.6 (Autoscaling), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 3 (applying site reliability engineering practices): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Managed instance scaling from a resource metric. Why the correct answer wins: Concurrency lets one instance serve several requests.
- **B:** Incorrect for this question. Calendar-driven capacity with no feedback loop. Why the correct answer wins: Concurrency lets one instance serve several requests.
- **C:** Correct. Concurrency-based replica scaling. In this case: Concurrency lets one instance serve several requests.
- **D:** Incorrect for this question. Replica scaling driven by a work signal. Why the correct answer wins: Concurrency lets one instance serve several requests.

### Question 59 — D

Answer: Drain connections before removing the instance. Draining finishes those requests before the node goes. A graceful handover of in-flight requests. Local study-map skill 3.7 (Traffic Draining and Redirection), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 3 (applying site reliability engineering practices): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A health-checked switch between backends. Why the correct answer wins: Draining finishes those requests before the node goes.
- **B:** Incorrect for this question. Extra supply in a different location. Why the correct answer wins: Draining finishes those requests before the node goes.
- **C:** Incorrect for this question. A name-level redirect to a healthy region. Why the correct answer wins: Draining finishes those requests before the node goes.
- **D:** Correct. A graceful handover of in-flight requests. In this case: Draining finishes those requests before the node goes.

### Question 60 — C

Answer: Shift traffic with a DNS routing policy. The routing policy changes the returned answer. A name-level redirect to a healthy region. Local study-map skill 3.7 (Traffic Draining and Redirection), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 3 (applying site reliability engineering practices): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A graceful handover of in-flight requests. Why the correct answer wins: The routing policy changes the returned answer.
- **B:** Incorrect for this question. A health-checked switch between backends. Why the correct answer wins: The routing policy changes the returned answer.
- **C:** Correct. A name-level redirect to a healthy region. In this case: The routing policy changes the returned answer.
- **D:** Incorrect for this question. Extra supply in a different location. Why the correct answer wins: The routing policy changes the returned answer.

### Question 61 — B, D

Answers: Add capacity in a second region; Use a load balancer failover backend. The second region adds supply, and the failover backend moves traffic. Extra supply in a different location. A health-checked switch between backends. Local study-map skill 3.8 (Incident Capacity), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 3 (applying site reliability engineering practices): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Capacity arranged ahead of a known peak. Why the correct answer wins: The second region adds supply, and the failover backend moves traffic.
- **B:** Correct. A health-checked switch between backends. In this case: The second region adds supply, and the failover backend moves traffic.
- **C:** Incorrect for this question. A graceful handover of in-flight requests. Why the correct answer wins: The second region adds supply, and the failover backend moves traffic.
- **D:** Correct. Extra supply in a different location. In this case: The second region adds supply, and the failover backend moves traffic.
- **E:** Incorrect for this question. A name-level redirect to a healthy region. Why the correct answer wins: The second region adds supply, and the failover backend moves traffic.

### Question 62 — A, E

Answers: Put the behaviour behind a feature flag; Redeploy the previous image to the affected service. The flag disables the path, and the redeploy restores the old build. A runtime switch that separates deploy from release. A known good artifact restored in place. Local study-map skill 3.9 (Rollback Strategies), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 3 (applying site reliability engineering practices): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Correct. A known good artifact restored in place. In this case: The flag disables the path, and the redeploy restores the old build.
- **B:** Incorrect for this question. An untracked change to the live environment. Why the correct answer wins: The flag disables the path, and the redeploy restores the old build.
- **C:** Incorrect for this question. A paired migration that can be undone. Why the correct answer wins: The flag disables the path, and the redeploy restores the old build.
- **D:** Incorrect for this question. No action while users are still failing. Why the correct answer wins: The flag disables the path, and the redeploy restores the old build.
- **E:** Correct. A runtime switch that separates deploy from release. In this case: The flag disables the path, and the redeploy restores the old build.

### Question 63 — D

Answer: Reverse the schema change with a tested down migration. A tested down migration would restore the column. A paired migration that can be undone. Local study-map skill 3.9 (Rollback Strategies), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 3 (applying site reliability engineering practices): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A known good artifact restored in place. Why the correct answer wins: A tested down migration would restore the column.
- **B:** Incorrect for this question. An untracked change to the live environment. Why the correct answer wins: A tested down migration would restore the column.
- **C:** Incorrect for this question. No action while users are still failing. Why the correct answer wins: A tested down migration would restore the column.
- **D:** Correct. A paired migration that can be undone. In this case: A tested down migration would restore the column.

### Question 64 — A

Answer: Install the Ops Agent on the instances. The Ops Agent ships the syslog from each VM. A collector that ships logs and metrics from the VM. Local study-map skill 4.1 (Log Collection and Ingestion), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 4 (implementing observability practices and troubleshooting): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Correct. A collector that ships logs and metrics from the VM. In this case: The Ops Agent ships the syslog from each VM.
- **B:** Incorrect for this question. Request metrics emitted by the sidecar proxies. Why the correct answer wins: The Ops Agent ships the syslog from each VM.
- **C:** Incorrect for this question. Per-connection records of accepted and denied traffic. Why the correct answer wins: The Ops Agent ships the syslog from each VM.
- **D:** Incorrect for this question. A vendor-neutral pipeline for traces and metrics. Why the correct answer wins: The Ops Agent ships the syslog from each VM.

### Question 65 — C

Answer: Run an OpenTelemetry Collector in the cluster. The collector receives and routes the existing signal. A vendor-neutral pipeline for traces and metrics. Local study-map skill 4.1 (Log Collection and Ingestion), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 4 (implementing observability practices and troubleshooting): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Request metrics emitted by the sidecar proxies. Why the correct answer wins: The collector receives and routes the existing signal.
- **B:** Incorrect for this question. A collector that ships logs and metrics from the VM. Why the correct answer wins: The collector receives and routes the existing signal.
- **C:** Correct. A vendor-neutral pipeline for traces and metrics. In this case: The collector receives and routes the existing signal.
- **D:** Incorrect for this question. A record of reads and writes on the resource. Why the correct answer wins: The collector receives and routes the existing signal.

### Question 66 — A, C

Answers: Drop the high-cardinality user label from the metric; Measure log volume per service before choosing a retention period. Trimming the label shrinks the series, and measuring volume informs retention. A label removal that cuts the stored series. A cost estimate driven by actual ingest. Local study-map skill 4.2 (Log Optimization and Cost), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 4 (implementing observability practices and troubleshooting): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Correct. A cost estimate driven by actual ingest. In this case: Trimming the label shrinks the series, and measuring volume informs retention.
- **B:** Incorrect for this question. A filter that drops matching entries before storage. Why the correct answer wins: Trimming the label shrinks the series, and measuring volume informs retention.
- **C:** Correct. A label removal that cuts the stored series. In this case: Trimming the label shrinks the series, and measuring volume informs retention.
- **D:** Incorrect for this question. A retention period that cannot be shortened. Why the correct answer wins: Trimming the label shrinks the series, and measuring volume informs retention.
- **E:** Incorrect for this question. A fraction kept for diagnosis at lower cost. Why the correct answer wins: Trimming the label shrinks the series, and measuring volume informs retention.

### Question 67 — A

Answer: Sample the high-volume debug entries. Sampling cuts the stored fraction of those entries. A fraction kept for diagnosis at lower cost. Local study-map skill 4.2 (Log Optimization and Cost), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 4 (implementing observability practices and troubleshooting): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Correct. A fraction kept for diagnosis at lower cost. In this case: Sampling cuts the stored fraction of those entries.
- **B:** Incorrect for this question. A cost estimate driven by actual ingest. Why the correct answer wins: Sampling cuts the stored fraction of those entries.
- **C:** Incorrect for this question. A label removal that cuts the stored series. Why the correct answer wins: Sampling cuts the stored fraction of those entries.
- **D:** Incorrect for this question. A filter that drops matching entries before storage. Why the correct answer wins: Sampling cuts the stored fraction of those entries.

### Question 68 — B

Answer: Open the Logs Explorer and pivot from the error entry. Pivoting shows the entries around the failure. An interactive view with field filters. Local study-map skill 4.3 (Logs Explorer and Query Language), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 4 (implementing observability practices and troubleshooting): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A counter derived from matching entries. Why the correct answer wins: Pivoting shows the entries around the failure.
- **B:** Correct. An interactive view with field filters. In this case: Pivoting shows the entries around the failure.
- **C:** Incorrect for this question. A sink that lands logs in a queryable table. Why the correct answer wins: Pivoting shows the entries around the failure.
- **D:** Incorrect for this question. A precise query over the stored entries. Why the correct answer wins: Pivoting shows the entries around the failure.

### Question 69 — B

Answer: Filter with the Logging query language on the resource label. The query language supports that exclusion. A precise query over the stored entries. Local study-map skill 4.3 (Logs Explorer and Query Language), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 4 (implementing observability practices and troubleshooting): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A counter derived from matching entries. Why the correct answer wins: The query language supports that exclusion.
- **B:** Correct. A precise query over the stored entries. In this case: The query language supports that exclusion.
- **C:** Incorrect for this question. A probe that exercises the path from outside. Why the correct answer wins: The query language supports that exclusion.
- **D:** Incorrect for this question. An interactive view with field filters. Why the correct answer wins: The query language supports that exclusion.

### Question 70 — D

Answer: Set the log bucket retention and lock it. A locked bucket cannot be shortened or emptied. A retention period that cannot be shortened. Local study-map skill 4.4 (Log Export and Retention), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 4 (implementing observability practices and troubleshooting): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A sink that lands logs in a queryable table. Why the correct answer wins: A locked bucket cannot be shortened or emptied.
- **B:** Incorrect for this question. A cost estimate driven by actual ingest. Why the correct answer wins: A locked bucket cannot be shortened or emptied.
- **C:** Incorrect for this question. A sink suited to cheap long-term retention. Why the correct answer wins: A locked bucket cannot be shortened or emptied.
- **D:** Correct. A retention period that cannot be shortened. In this case: A locked bucket cannot be shortened or emptied.

### Question 71 — B

Answer: Route the entries to a Cloud Storage bucket. A storage sink is the cheapest long retention. A sink suited to cheap long-term retention. Local study-map skill 4.4 (Log Export and Retention), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 4 (implementing observability practices and troubleshooting): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A sink that streams entries to another consumer. Why the correct answer wins: A storage sink is the cheapest long retention.
- **B:** Correct. A sink suited to cheap long-term retention. In this case: A storage sink is the cheapest long retention.
- **C:** Incorrect for this question. A sink that lands logs in a queryable table. Why the correct answer wins: A storage sink is the cheapest long retention.
- **D:** Incorrect for this question. A retention period that cannot be shortened. Why the correct answer wins: A storage sink is the cheapest long retention.

### Question 72 — A

Answer: Redact the email field with a log processor. The processor removes it before the entry is written. A transform that removes the value before storage. Local study-map skill 4.5 (Sensitive Data Redaction), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 4 (implementing observability practices and troubleshooting): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Correct. A transform that removes the value before storage. In this case: The processor removes it before the entry is written.
- **B:** Incorrect for this question. A sink suited to cheap long-term retention. Why the correct answer wins: The processor removes it before the entry is written.
- **C:** Incorrect for this question. A fraction kept for diagnosis at lower cost. Why the correct answer wins: The processor removes it before the entry is written.
- **D:** Incorrect for this question. A procedural promise with no enforcement. Why the correct answer wins: The processor removes it before the entry is written.

### Question 73 — B

Answer: Ask Gemini Cloud Assist to explain the metric spike. Gemini Cloud Assist explains the step change. An AI interpretation of the chart. Local study-map skill 4.6 (Gemini Cloud Assist for Log Analysis), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 4 (implementing observability practices and troubleshooting): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. An AI pointer to the expensive span. Why the correct answer wins: Gemini Cloud Assist explains the step change.
- **B:** Correct. An AI interpretation of the chart. In this case: Gemini Cloud Assist explains the step change.
- **C:** Incorrect for this question. A precise query over the stored entries. Why the correct answer wins: Gemini Cloud Assist explains the step change.
- **D:** Incorrect for this question. An AI summary over the selected log range. Why the correct answer wins: Gemini Cloud Assist explains the step change.

### Question 74 — A, D

Answers: Install the Ops Agent on the instances; Turn on VPC Flow Logs for the subnet. The Ops Agent covers the hosts, and flow logs cover the connections. A collector that ships logs and metrics from the VM. Per-connection records of accepted and denied traffic. Local study-map skill 4.7 (Metrics Collection), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 4 (implementing observability practices and troubleshooting): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Correct. Per-connection records of accepted and denied traffic. In this case: The Ops Agent covers the hosts, and flow logs cover the connections.
- **B:** Incorrect for this question. Request metrics emitted by the sidecar proxies. Why the correct answer wins: The Ops Agent covers the hosts, and flow logs cover the connections.
- **C:** Incorrect for this question. A record of reads and writes on the resource. Why the correct answer wins: The Ops Agent covers the hosts, and flow logs cover the connections.
- **D:** Correct. A collector that ships logs and metrics from the VM. In this case: The Ops Agent covers the hosts, and flow logs cover the connections.
- **E:** Incorrect for this question. A vendor-neutral pipeline for traces and metrics. Why the correct answer wins: The Ops Agent covers the hosts, and flow logs cover the connections.

### Question 75 — A

Answer: Enable Data Access audit logs for the service. Data Access audit logs record those reads. A record of reads and writes on the resource. Local study-map skill 4.7 (Metrics Collection), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 4 (implementing observability practices and troubleshooting): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Correct. A record of reads and writes on the resource. In this case: Data Access audit logs record those reads.
- **B:** Incorrect for this question. A collector that ships logs and metrics from the VM. Why the correct answer wins: Data Access audit logs record those reads.
- **C:** Incorrect for this question. Request metrics emitted by the sidecar proxies. Why the correct answer wins: Data Access audit logs record those reads.
- **D:** Incorrect for this question. Per-connection records of accepted and denied traffic. Why the correct answer wins: Data Access audit logs record those reads.

### Question 76 — C

Answer: Emit a custom metric for the business event. The service emits that count as a metric. A measurement written by the application itself. Local study-map skill 4.8 (Custom and Log-Based Metrics), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 4 (implementing observability practices and troubleshooting): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A counter derived from matching entries. Why the correct answer wins: The service emits that count as a metric.
- **B:** Incorrect for this question. A probe that exercises the path from outside. Why the correct answer wins: The service emits that count as a metric.
- **C:** Correct. A measurement written by the application itself. In this case: The service emits that count as a metric.
- **D:** Incorrect for this question. A metrics store fed by a scrape endpoint. Why the correct answer wins: The service emits that count as a metric.

### Question 77 — B

Answer: Create an uptime check against the login flow. The uptime check fails when the certificate is invalid. A probe that exercises the path from outside. Local study-map skill 4.9 (Synthetic Monitors), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 4 (implementing observability practices and troubleshooting): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A counter derived from matching entries. Why the correct answer wins: The uptime check fails when the certificate is invalid.
- **B:** Correct. A probe that exercises the path from outside. In this case: The uptime check fails when the certificate is invalid.
- **C:** Incorrect for this question. A measurement written by the application itself. Why the correct answer wins: The uptime check fails when the certificate is invalid.
- **D:** Incorrect for this question. A metrics store fed by a scrape endpoint. Why the correct answer wins: The uptime check fails when the certificate is invalid.

### Question 78 — D

Answer: Attach the remediation playbook to the alert. Attaching it to the alert answers that question. A documented response beside the notification. Local study-map skill 4.10 (Metrics Explorer and Dashboards), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 4 (implementing observability practices and troubleshooting): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A page driven by the objective instead of a raw threshold. Why the correct answer wins: Attaching it to the alert answers that question.
- **B:** Incorrect for this question. A shared view of the signals that matter. Why the correct answer wins: Attaching it to the alert answers that question.
- **C:** Incorrect for this question. A delivery route for the alert. Why the correct answer wins: Attaching it to the alert answers that question.
- **D:** Correct. A documented response beside the notification. In this case: Attaching it to the alert answers that question.

### Question 79 — B

Answer: Build one dashboard and share it with the on-call rotation. A shared dashboard gives them the standard view. A shared view of the signals that matter. Local study-map skill 4.10 (Metrics Explorer and Dashboards), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 4 (implementing observability practices and troubleshooting): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A third-party paging integration. Why the correct answer wins: A shared dashboard gives them the standard view.
- **B:** Correct. A shared view of the signals that matter. In this case: A shared dashboard gives them the standard view.
- **C:** Incorrect for this question. A documented response beside the notification. Why the correct answer wins: A shared dashboard gives them the standard view.
- **D:** Incorrect for this question. A static threshold on a resource metric. Why the correct answer wins: A shared dashboard gives them the standard view.

### Question 80 — A, D

Answers: Create an alerting policy on the SLO burn rate; Add an email notification channel for the on-call group. The burn-rate policy pages on impact, and the email channel copies audit. A page driven by the objective instead of a raw threshold. A delivery route for the alert. Local study-map skill 4.11 (Alerting Policies), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 4 (implementing observability practices and troubleshooting): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Correct. A delivery route for the alert. In this case: The burn-rate policy pages on impact, and the email channel copies audit.
- **B:** Incorrect for this question. A third-party paging integration. Why the correct answer wins: The burn-rate policy pages on impact, and the email channel copies audit.
- **C:** Incorrect for this question. A documented response beside the notification. Why the correct answer wins: The burn-rate policy pages on impact, and the email channel copies audit.
- **D:** Correct. A page driven by the objective instead of a raw threshold. In this case: The burn-rate policy pages on impact, and the email channel copies audit.
- **E:** Incorrect for this question. A static threshold on a resource metric. Why the correct answer wins: The burn-rate policy pages on impact, and the email channel copies audit.

### Question 81 — B

Answer: Alert when CPU stays above ninety percent for ten minutes. A resource threshold cannot tell intended load from harm. A static threshold on a resource metric. Local study-map skill 4.11 (Alerting Policies), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 4 (implementing observability practices and troubleshooting): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A page driven by the objective instead of a raw threshold. Why the correct answer wins: A resource threshold cannot tell intended load from harm.
- **B:** Correct. A static threshold on a resource metric. In this case: A resource threshold cannot tell intended load from harm.
- **C:** Incorrect for this question. A third-party paging integration. Why the correct answer wins: A resource threshold cannot tell intended load from harm.
- **D:** Incorrect for this question. A documented response beside the notification. Why the correct answer wins: A resource threshold cannot tell intended load from harm.

### Question 82 — A

Answer: Send the alert to PagerDuty through a webhook. A webhook reaches the on-call tool directly. A third-party paging integration. Local study-map skill 4.12 (Third-Party Alerting Integration), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 4 (implementing observability practices and troubleshooting): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Correct. A third-party paging integration. In this case: A webhook reaches the on-call tool directly.
- **B:** Incorrect for this question. A delivery route for the alert. Why the correct answer wins: A webhook reaches the on-call tool directly.
- **C:** Incorrect for this question. A documented response beside the notification. Why the correct answer wins: A webhook reaches the on-call tool directly.
- **D:** Incorrect for this question. A page driven by the objective instead of a raw threshold. Why the correct answer wins: A webhook reaches the on-call tool directly.

### Question 83 — D

Answer: Read the trace waterfall to find the slow span. The waterfall shows where the request waited before work started. A per-span timing view of one request. Local study-map skill 4.13 (Distributed Tracing with OpenTelemetry), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 4 (implementing observability practices and troubleshooting): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A join key between traces and logs. Why the correct answer wins: The waterfall shows where the request waited before work started.
- **B:** Incorrect for this question. An AI pointer to the expensive span. Why the correct answer wins: The waterfall shows where the request waited before work started.
- **C:** Incorrect for this question. Trace context emitted for each request. Why the correct answer wins: The waterfall shows where the request waited before work started.
- **D:** Correct. A per-span timing view of one request. In this case: The waterfall shows where the request waited before work started.

### Question 84 — B

Answer: Put the trace ID in the structured log line. The trace ID in the line fetches that trace. A join key between traces and logs. Local study-map skill 4.13 (Distributed Tracing with OpenTelemetry), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 4 (implementing observability practices and troubleshooting): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. No shared identifier between the two signals. Why the correct answer wins: The trace ID in the line fetches that trace.
- **B:** Correct. A join key between traces and logs. In this case: The trace ID in the line fetches that trace.
- **C:** Incorrect for this question. Trace context emitted for each request. Why the correct answer wins: The trace ID in the line fetches that trace.
- **D:** Incorrect for this question. A per-span timing view of one request. Why the correct answer wins: The trace ID in the line fetches that trace.

### Question 85 — D, E

Answers: Ask Gemini Cloud Assist which span dominates the trace; Compare latency with the saturation metric. The assistant names the span, and saturation correlation explains it. An AI pointer to the expensive span. A queueing symptom traced to a full resource. Local study-map skill 4.14 (Trace Analysis and Log Correlation), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 4 (implementing observability practices and troubleshooting): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A join key between traces and logs. Why the correct answer wins: The assistant names the span, and saturation correlation explains it.
- **B:** Incorrect for this question. A per-span timing view of one request. Why the correct answer wins: The assistant names the span, and saturation correlation explains it.
- **C:** Incorrect for this question. Trace context emitted for each request. Why the correct answer wins: The assistant names the span, and saturation correlation explains it.
- **D:** Correct. A queueing symptom traced to a full resource. In this case: The assistant names the span, and saturation correlation explains it.
- **E:** Correct. An AI pointer to the expensive span. In this case: The assistant names the span, and saturation correlation explains it.

### Question 86 — D

Answer: Check the quota error in the deployment log. The quota log shows which limit was reached. The limit that refused the resource. Local study-map skill 4.15 (Infrastructure and Pipeline Troubleshooting), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 4 (implementing observability practices and troubleshooting): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A stale name that still points at the old address. Why the correct answer wins: The quota log shows which limit was reached.
- **B:** Incorrect for this question. The identity the node uses to fetch the image. Why the correct answer wins: The quota log shows which limit was reached.
- **C:** Incorrect for this question. The rule that blocked the connection. Why the correct answer wins: The quota log shows which limit was reached.
- **D:** Correct. The limit that refused the resource. In this case: The quota log shows which limit was reached.

### Question 87 — C

Answer: Check Cloud NAT port exhaustion for the egress range. Port exhaustion on the shared address shows up under load. A shared egress resource that runs out of ports. Local study-map skill 4.16 (Application and Latency Troubleshooting), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 4 (implementing observability practices and troubleshooting): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. The limit that refused the resource. Why the correct answer wins: Port exhaustion on the shared address shows up under load.
- **B:** Incorrect for this question. The rule that blocked the connection. Why the correct answer wins: Port exhaustion on the shared address shows up under load.
- **C:** Correct. A shared egress resource that runs out of ports. In this case: Port exhaustion on the shared address shows up under load.
- **D:** Incorrect for this question. The identity the node uses to fetch the image. Why the correct answer wins: Port exhaustion on the shared address shows up under load.

### Question 88 — A

Answer: Check the DNS record and its remaining TTL. Cached answers keep sending users to the old host. A stale name that still points at the old address. Local study-map skill 4.16 (Application and Latency Troubleshooting), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 4 (implementing observability practices and troubleshooting): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Correct. A stale name that still points at the old address. In this case: Cached answers keep sending users to the old host.
- **B:** Incorrect for this question. A shared egress resource that runs out of ports. Why the correct answer wins: Cached answers keep sending users to the old host.
- **C:** Incorrect for this question. A hotspot found on the request path. Why the correct answer wins: Cached answers keep sending users to the old host.
- **D:** Incorrect for this question. The rule that blocked the connection. Why the correct answer wins: Cached answers keep sending users to the old host.

### Question 89 — B

Answer: Measure request latency by endpoint in Cloud Monitoring. Per-endpoint latency is what verifies that claim. An application-level view of response time. Local study-map skill 5.1 (Application Performance Monitoring), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 5 (optimizing performance and cost): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A recommendation aimed at spend. Why the correct answer wins: Per-endpoint latency is what verifies that claim.
- **B:** Correct. An application-level view of response time. In this case: Per-endpoint latency is what verifies that claim.
- **C:** Incorrect for this question. A goal-oriented view of performance. Why the correct answer wins: Per-endpoint latency is what verifies that claim.
- **D:** Incorrect for this question. A queryable record of spend by label. Why the correct answer wins: Per-endpoint latency is what verifies that claim.

### Question 90 — C

Answer: Track the service objective on a shared dashboard. The objective dashboard answers that monthly question. A goal-oriented view of performance. Local study-map skill 5.1 (Application Performance Monitoring), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 5 (optimizing performance and cost): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A recommendation aimed at spend. Why the correct answer wins: The objective dashboard answers that monthly question.
- **B:** Incorrect for this question. An application-level view of response time. Why the correct answer wins: The objective dashboard answers that monthly question.
- **C:** Correct. A goal-oriented view of performance. In this case: The objective dashboard answers that monthly question.
- **D:** Incorrect for this question. A cost estimate driven by actual ingest. Why the correct answer wins: The objective dashboard answers that monthly question.

### Question 91 — C, E

Answers: Apply the cost recommender suggestion for the idle disks; Apply the reliability recommender for the missing quota. The cost recommender finds idle resources, and the reliability one finds the peak fix. A recommendation aimed at spend. A recommendation aimed at resilience. Local study-map skill 5.2 (Active Assist and Recommenders), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 5 (optimizing performance and cost): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Discounted capacity that can be reclaimed. Why the correct answer wins: The cost recommender finds idle resources, and the reliability one finds the peak fix.
- **B:** Incorrect for this question. A queryable record of spend by label. Why the correct answer wins: The cost recommender finds idle resources, and the reliability one finds the peak fix.
- **C:** Correct. A recommendation aimed at resilience. In this case: The cost recommender finds idle resources, and the reliability one finds the peak fix.
- **D:** Incorrect for this question. Suggested changes generated from telemetry. Why the correct answer wins: The cost recommender finds idle resources, and the reliability one finds the peak fix.
- **E:** Correct. A recommendation aimed at spend. In this case: The cost recommender finds idle resources, and the reliability one finds the peak fix.

### Question 92 — D

Answer: Review the Active Assist recommendations for the project. Active Assist lists them in one place. Suggested changes generated from telemetry. Local study-map skill 5.2 (Active Assist and Recommenders), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 5 (optimizing performance and cost): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A recommendation aimed at spend. Why the correct answer wins: Active Assist lists them in one place.
- **B:** Incorrect for this question. A recommendation aimed at resilience. Why the correct answer wins: Active Assist lists them in one place.
- **C:** Incorrect for this question. A queryable record of spend by label. Why the correct answer wins: Active Assist lists them in one place.
- **D:** Correct. Suggested changes generated from telemetry. In this case: Active Assist lists them in one place.

### Question 93 — C

Answer: Measure log volume per service before choosing a retention period. Measuring the volume is what prices the proposal. A cost estimate driven by actual ingest. Local study-map skill 5.3 (Observability Cost Management), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 5 (optimizing performance and cost): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A retention period that cannot be shortened. Why the correct answer wins: Measuring the volume is what prices the proposal.
- **B:** Incorrect for this question. A reduction that preserves the useful signal. Why the correct answer wins: Measuring the volume is what prices the proposal.
- **C:** Correct. A cost estimate driven by actual ingest. In this case: Measuring the volume is what prices the proposal.
- **D:** Incorrect for this question. A label removal that cuts the stored series. Why the correct answer wins: Measuring the volume is what prices the proposal.

### Question 94 — C

Answer: Exclude the debug stream and keep the error stream. Excluding the debug stream keeps the useful remainder. A reduction that preserves the useful signal. Local study-map skill 5.3 (Observability Cost Management), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 5 (optimizing performance and cost): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A cheaper egress path with different performance. Why the correct answer wins: Excluding the debug stream keeps the useful remainder.
- **B:** Incorrect for this question. A label removal that cuts the stored series. Why the correct answer wins: Excluding the debug stream keeps the useful remainder.
- **C:** Correct. A reduction that preserves the useful signal. In this case: Excluding the debug stream keeps the useful remainder.
- **D:** Incorrect for this question. A cost estimate driven by actual ingest. Why the correct answer wins: Excluding the debug stream keeps the useful remainder.

### Question 95 — A

Answer: Put the stateless workers on a Spot node pool. Spot nodes cut the dominant compute line. A pool built from reclaimable capacity. Local study-map skill 5.4 (Spot Virtual Machines), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 5 (optimizing performance and cost): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Correct. A pool built from reclaimable capacity. In this case: Spot nodes cut the dominant compute line.
- **B:** Incorrect for this question. Reclaimable capacity under a stateful workload. Why the correct answer wins: Spot nodes cut the dominant compute line.
- **C:** Incorrect for this question. Discounted capacity that can be reclaimed. Why the correct answer wins: Spot nodes cut the dominant compute line.
- **D:** Incorrect for this question. A multi-year commitment at a lower unit price. Why the correct answer wins: Spot nodes cut the dominant compute line.

### Question 96 — C

Answer: Move the primary database onto Spot capacity. Reclaimable capacity cannot hold the write primary. Reclaimable capacity under a stateful workload. Local study-map skill 5.4 (Spot Virtual Machines), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 5 (optimizing performance and cost): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A pool built from reclaimable capacity. Why the correct answer wins: Reclaimable capacity cannot hold the write primary.
- **B:** Incorrect for this question. A multi-year commitment at a lower unit price. Why the correct answer wins: Reclaimable capacity cannot hold the write primary.
- **C:** Correct. Reclaimable capacity under a stateful workload. In this case: Reclaimable capacity cannot hold the write primary.
- **D:** Incorrect for this question. Discounted capacity that can be reclaimed. Why the correct answer wins: Reclaimable capacity cannot hold the write primary.

### Question 97 — D

Answer: Buy a committed-use discount for the steady baseline. A commitment discounts the predictable baseline. A multi-year commitment at a lower unit price. Local study-map skill 5.5 (Infrastructure Cost Planning), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 5 (optimizing performance and cost): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Discounted capacity that can be reclaimed. Why the correct answer wins: A commitment discounts the predictable baseline.
- **B:** Incorrect for this question. A cheaper egress path with different performance. Why the correct answer wins: A commitment discounts the predictable baseline.
- **C:** Incorrect for this question. An automatic discount that accrues with monthly use. Why the correct answer wins: A commitment discounts the predictable baseline.
- **D:** Correct. A multi-year commitment at a lower unit price. In this case: A commitment discounts the predictable baseline.

### Question 98 — A

Answer: Serve the bulk export over the Standard network tier. The standard tier costs less for that copy. A cheaper egress path with different performance. Local study-map skill 5.5 (Infrastructure Cost Planning), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 5 (optimizing performance and cost): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Correct. A cheaper egress path with different performance. In this case: The standard tier costs less for that copy.
- **B:** Incorrect for this question. A multi-year commitment at a lower unit price. Why the correct answer wins: The standard tier costs less for that copy.
- **C:** Incorrect for this question. A lower-latency path for user-facing traffic. Why the correct answer wins: The standard tier costs less for that copy.
- **D:** Incorrect for this question. A pool built from reclaimable capacity. Why the correct answer wins: The standard tier costs less for that copy.

### Question 99 — A, B

Answers: Right-size the node pool from the observed requests; Stop the idle non-production instances on a schedule. Right-sizing removes the reservation, and the scheduled stop ends the idle time. A pool sized against measured demand. A calendar action that removes idle spend. Local study-map skill 5.6 (Workload-Level Cost Optimization), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 5 (optimizing performance and cost): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Correct. A calendar action that removes idle spend. In this case: Right-sizing removes the reservation, and the scheduled stop ends the idle time.
- **B:** Correct. A pool sized against measured demand. In this case: Right-sizing removes the reservation, and the scheduled stop ends the idle time.
- **C:** Incorrect for this question. Warm capacity that avoids cold starts. Why the correct answer wins: Right-sizing removes the reservation, and the scheduled stop ends the idle time.
- **D:** Incorrect for this question. A multi-year commitment at a lower unit price. Why the correct answer wins: Right-sizing removes the reservation, and the scheduled stop ends the idle time.
- **E:** Incorrect for this question. Scale to zero for a service nobody uses at night. Why the correct answer wins: Right-sizing removes the reservation, and the scheduled stop ends the idle time.

### Question 100 — A

Answer: Keep the minimum instance count at zero for the internal tool. A minimum of zero removes the idle bill. Scale to zero for a service nobody uses at night. Local study-map skill 5.6 (Workload-Level Cost Optimization), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 5 (optimizing performance and cost): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Correct. Scale to zero for a service nobody uses at night. In this case: A minimum of zero removes the idle bill.
- **B:** Incorrect for this question. Warm capacity that avoids cold starts. Why the correct answer wins: A minimum of zero removes the idle bill.
- **C:** Incorrect for this question. A pool sized against measured demand. Why the correct answer wins: A minimum of zero removes the idle bill.
- **D:** Incorrect for this question. A multi-year commitment at a lower unit price. Why the correct answer wins: A minimum of zero removes the idle bill.
