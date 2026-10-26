# Google Cloud Professional Cloud DevOps Engineer — Full-Length Mock Exam 2

Professional Cloud DevOps Engineer · 100 questions · expanded practice bank · passing score not published

Blueprint-weighted mock exam. Item mix: 84 multiple-choice and 16 multiple-select items (the selection count is stated in each multi-select stem). The live exam publishes 50-60 multiple-choice and multiple-select questions and has no case-study component, so this set is larger on purpose and no case-study item is reproduced. The live paper allows two hours for 50-60 items, so this 100-item set is a slower-per-item rehearsal: about 72 seconds per item here against roughly 120-144 seconds live. Use it to build a habit of finishing with time to review. See the README for the exact fidelity boundary.

Original educational content, not actual, recalled, or copied Google exam items.

## Questions

---

## Domain 1 — Bootstrapping and Maintaining a Google Cloud Organization (Hierarchy, Infrastructure as Code, and Pipeline Foundations)

### 1. A conglomerate's retail arm may publish public buckets but its banking arm may not. Where should the restriction sit?

- A. Apply the constraint separately in each project
- B. Apply the constraint to the business unit folder
- C. Add an IAM deny policy for the sensitive permission
- D. Apply the constraint at the organization node

### 2. Cost reporting must separate production from everything else before any other split. How should the hierarchy be shaped?

- A. Apply the constraint to the business unit folder
- B. Group projects by environment with applications below
- C. Apply the constraint separately in each project
- D. Group projects by application inside each environment folder

### 3. A central team must own subnets for many projects, and a partner service must be consumed without a public address. Which two fit? Select two.

- A. Apply the constraint at the organization node
- B. Create a Shared VPC host project and attach the service projects
- C. Give each project its own VPC and Cloud NAT
- D. Publish the service behind a Private Service Connect endpoint
- E. Peer every project VPC with every other project VPC

### 4. A network built from pairwise peering now carries forty links and every new project adds more. Which approach caused that growth?

- A. Give each project its own VPC and Cloud NAT
- B. Peer every project VPC with every other project VPC
- C. Publish the service behind a Private Service Connect endpoint
- D. Create a Shared VPC host project and attach the service projects

### 5. SREs need one chart that aggregates latency across twelve projects at once. What should be configured?

- A. Route the entries to a BigQuery dataset
- B. Keep one log bucket inside each project
- C. Route every project log to one aggregated sink
- D. Add the projects to one metrics scope

### 6. A team needs the ordinary database reader permissions and nothing unusual. What should be granted?

- A. Enforce the restriction with an organization policy constraint
- B. Grant a predefined role once at the folder
- C. Grant a custom role limited to the required permissions
- D. Add an IAM deny policy for the sensitive permission

### 7. A security team must guarantee that one specific permission can never be granted, whatever a project owner binds. What should be added?

- A. Add an IAM deny policy for the sensitive permission
- B. Enforce the restriction with an organization policy constraint
- C. Grant a custom role limited to the required permissions
- D. Grant a predefined role once at the folder

### 8. Each deployed workload must have its own identity, and engineers must obtain short-lived credentials rather than keys. Which two practices apply? Select two.

- A. Grant impersonation of the service account instead of a key
- B. Let the workload use the default Compute Engine service account
- C. Download a JSON key file for the service account
- D. Create one service account per environment
- E. Create one service account per workload

### 9. A health insurer may process member records only inside one country. What must the deployment respect?

- A. Create a Shared VPC host project and attach the service projects
- B. Place the resources in a region that satisfies the residency rule
- C. Replicate the data to a second region
- D. Apply the constraint at the organization node

### 10. Infrastructure changes must be reviewed as diffs before anything is applied. What fits?

- A. Define the estate as Terraform modules held in version control
- B. Apply the deployment through Infrastructure Manager
- C. Package the workload as a Helm chart
- D. Reconcile the resources with Config Connector

### 11. A team wants the same Kubernetes-style declarative files to create buckets and datasets. What fits?

- A. Apply the deployment through Infrastructure Manager
- B. Define the estate as Terraform modules held in version control
- C. Reconcile the resources with Config Connector
- D. Package the workload as a Helm chart

### 12. Nobody can say whether the live estate still matches the declared code. What should be scheduled?

- A. Schedule a plan that reports drift
- B. Run the documented gcloud commands by hand for each environment
- C. Start from the Cloud Foundation Toolkit blueprints
- D. Make the change in the console and note it in the wiki

### 13. Test projects older than a week must be deleted every night without human involvement. What should be written?

- A. Run the documented gcloud commands by hand for each environment
- B. Make the change in the console and note it in the wiki
- C. Automate the repeated step with a Python script calling the API
- D. Render the manifests through a kpt function pipeline

### 14. Company policy requires builds to run on its own Jenkins controllers, while artifacts must still land in Google Cloud. What fits?

- A. Store the build output in Artifact Registry
- B. Use Cloud Build for CI and Cloud Deploy for delivery
- C. Run Jenkins on a self-managed VM
- D. Let Argo CD pull the manifests from Git

### 15. A startup wants no build servers to patch and no release tooling to host. What fits?

- A. Bake the machine image with Packer
- B. Let Argo CD pull the manifests from Git
- C. Run Jenkins on a self-managed VM
- D. Use Cloud Build for CI and Cloud Deploy for delivery

### 16. A hardened base image must be byte-identical in every environment. What fits?

- A. Render the manifests through a kpt function pipeline
- B. Define the estate as Terraform modules held in version control
- C. Bake the machine image with Packer
- D. Package the workload as a Helm chart

### 17. Reviewers need a disposable environment per change, and one permanent place must run the integration suite. Which two apply? Select two.

- A. Bake the environment settings into the image
- B. Group projects by environment with applications below
- C. Apply the constraint separately in each project
- D. Create a short-lived project per change and delete it after review
- E. Keep one shared staging environment for every team

### 18. A cluster upgrade must be proven on a parallel cluster before any user is moved. What fits?

- A. Put the cluster on a release channel with a maintenance window
- B. Create a short-lived project per change and delete it after review
- C. Upgrade each node pool by hand whenever an operator is free
- D. Stand up a second cluster and shift traffic after verification

### 19. Every developer machine must start from a pinned toolchain that security has approved. What should be built?

- A. Let each developer install the tools locally
- B. Build a custom image that carries the approved toolchain
- C. Give developers Cloud Workstations built from a custom image
- D. Rely on Cloud Shell for every developer

### 20. An engineer wants help drafting a long command in the terminal. What fits?

- A. Let each developer install the tools locally
- B. Use Gemini Code Assist for the suggested change
- C. Ask Gemini Cloud Assist to explain the resource state
- D. Use Gemini CLI for the repetitive script

---

## Domain 2 — Building and Implementing CI/CD Pipelines (Delivery Pipelines and Software Supply Chain)

### 21. Terraform changes must be validated before a merge request can land. What should be configured?

- A. Create a Cloud Build trigger on the release branch
- B. Trigger the pipeline only on a signed tag
- C. Read Cloud Audit Logs for the release history
- D. Create a trigger that runs the tests on every pull request

### 22. Images may be produced only from a signed version tag, never from a branch. What should be configured?

- A. Create a trigger that runs the tests on every pull request
- B. Create a Cloud Build trigger on the release branch
- C. Trigger the pipeline only on a signed tag
- D. Have an engineer build locally and upload the result

### 23. Every commit landed on main must rebuild and publish the artifact. What should be configured?

- A. Create a Cloud Build trigger on the release branch
- B. Have an engineer build locally and upload the result
- C. Create a trigger that runs the tests on every pull request
- D. Trigger the pipeline only on a signed tag

### 24. A rollback must fetch exactly the artifact that ran last Tuesday. What should have been enforced?

- A. Reuse the latest tag for every build
- B. Tag each artifact with the commit SHA and forbid overwrite
- C. Push the image to Container Registry
- D. Bake the machine image with Packer

### 25. A new region needs repository-level IAM and scanning, but the images sit in the legacy registry. What is the obstacle?

- A. Tag each artifact with the commit SHA and forbid overwrite
- B. Store the build output in Artifact Registry
- C. Inspect the build provenance attestation
- D. Push the image to Container Registry

### 26. A delivery pipeline must promote to a cluster in the same project as the pipeline. What fits?

- A. Define the attached cluster as the delivery target
- B. Add a Cloud Deploy approval gate before production
- C. Use a GKE cluster in the pipeline project as the target
- D. Deliver to a Cloud Run service revision

### 27. A pipeline must release to a cluster that runs in another cloud. What fits?

- A. Deliver to a Cloud Run service revision
- B. Use a GKE cluster in the pipeline project as the target
- C. Define the attached cluster as the delivery target
- D. Read Cloud Audit Logs for the release history

### 28. Staging needs a named approver, while the development target must promote without waiting for a human. Which two settings apply? Select two.

- A. Promote automatically to every target in the chain
- B. Have an engineer build locally and upload the result
- C. Roll the release back to the previous one
- D. Read Cloud Audit Logs for the release history
- E. Add a Cloud Deploy approval gate before production

### 29. An investigator needs the identity and time of every release to a target. What supplies that?

- A. Read Cloud Audit Logs for the release history
- B. Inspect the build provenance attestation
- C. Tag each artifact with the commit SHA and forbid overwrite
- D. Add a Cloud Deploy approval gate before production

### 30. A reviewer must verify which source commit and build steps produced an image. What supplies that?

- A. Read Cloud Audit Logs for the release history
- B. Tag each artifact with the commit SHA and forbid overwrite
- C. Inspect the build provenance attestation
- D. Describe the build with its supply chain level and signed provenance

### 31. Two full environments must allow an instant cutover, and a stateless fleet must be replaced a few instances at a time. Which two strategies apply? Select two.

- A. Replace the instances in batches
- B. Send ten percent of traffic to the new revision and watch the SLI
- C. Run the new version alongside and switch traffic at once
- D. Stop the old version and then start the new one
- E. Split traffic with a Cloud Service Mesh route

### 32. A deployment must keep serving throughout while instances are replaced gradually. What fits?

- A. Stop the old version and then start the new one
- B. Run the new version alongside and switch traffic at once
- C. Send ten percent of traffic to the new revision and watch the SLI
- D. Replace the instances in batches

### 33. Only one percent of sessions may see the new code while the error rate is watched. What fits?

- A. Stop the old version and then start the new one
- B. Send ten percent of traffic to the new revision and watch the SLI
- C. Replace the instances in batches
- D. Run the new version alongside and switch traffic at once

### 34. A team gates rollouts on host CPU and shipped a release that broke checkout without noticing. What went wrong?

- A. Add a Cloud Deploy approval gate before production
- B. Create an uptime check against the login flow
- C. Gate the rollout on the error-rate SLI
- D. Gate the rollout on average CPU alone

### 35. A deployment succeeded but the new behaviour is wrong and the prior release is intact. What is the first action?

- A. Patch production by hand and reconcile later
- B. Roll the release back to the previous one
- C. Make the failed step idempotent and re-run it
- D. Start from the failed step log in Cloud Build

### 36. An engineer fixes production directly during an incident and never records the change. What risk was created?

- A. Patch production by hand and reconcile later
- B. Make the failed step idempotent and re-run it
- C. Roll the release back to the previous one
- D. Schedule a plan that reports drift

### 37. A storage object must be encrypted under a key the team rotates, and public endpoints must present trusted certificates. Which two controls apply? Select two.

- A. Issue and rotate the certificate with Certificate Manager
- B. Encrypt the payload with a Cloud KMS key
- C. Keep the non-secret configuration in Parameter Manager
- D. Commit the credential to the private repository
- E. Store the credential in Secret Manager with versions

### 38. A third-party API token must be rotated on a schedule without redeploying the code. What fits?

- A. Pass the secret as a build argument
- B. Store the credential in Secret Manager with versions
- C. Keep the non-secret configuration in Parameter Manager
- D. Encrypt the payload with a Cloud KMS key

### 39. A feature limit differs per environment and must change without rebuilding the image. What fits?

- A. Bake the environment settings into the image
- B. Store the credential in Secret Manager with versions
- C. Commit the credential to the private repository
- D. Keep the non-secret configuration in Parameter Manager

### 40. The same image must run in three environments, but the settings were compiled in during the build. What is the obstacle?

- A. Bake the environment settings into the image
- B. Commit the credential to the private repository
- C. Store the credential in Secret Manager with versions
- D. Keep the non-secret configuration in Parameter Manager

### 41. A credential was written into an image layer during the build. Why is that worse than mounting it?

- A. Mount the secret at runtime from Secret Manager
- B. Inject the secret at build time into the image layer
- C. Pass the secret as a build argument
- D. Commit the credential to the private repository

### 42. Stored images need continuous vulnerability findings, and promotion must stop when a critical one appears. Which two capabilities deliver that? Select two.

- A. Keep the scan report for the monthly review
- B. Bind deploy permissions only inside the production project
- C. Enable Artifact Analysis scanning on the repository
- D. Fail the pipeline on a critical vulnerability finding
- E. Enforce Binary Authorization attestations before deploy

### 43. Only images built by the approved pipeline may start in the cluster, whatever their tag says. What fits?

- A. Bind deploy permissions only inside the production project
- B. Fail the pipeline on a critical vulnerability finding
- C. Enforce Binary Authorization attestations before deploy
- D. Enable Artifact Analysis scanning on the repository

### 44. One identity deploys to every environment, and a staging compromise released straight to production. Which practice caused that?

- A. Use one identity with deploy rights in every environment
- B. Download a JSON key file for the service account
- C. Run the pipeline as the default editor service account
- D. Bind deploy permissions only inside the production project

### 45. Each environment must have its own deployer identity with rights only inside that project. What should be configured?

- A. Bind deploy permissions only inside the production project
- B. Download a JSON key file for the service account
- C. Run the pipeline as the default editor service account
- D. Use one identity with deploy rights in every environment

---

## Domain 3 — Applying Site Reliability Engineering Practices (Reliability Engineering in Practice)

### 46. An internal commitment guides the team's releases, and an external contract promises the customer a remedy. Which two documents are those? Select two.

- A. Publish a contractual promise with a remedy
- B. Alert on a fast error-budget burn rate
- C. Set an internal target on that indicator
- D. Register the service in the service catalog
- E. Track the ratio of good requests to total requests

### 47. The team must decide whether p95 latency under 300 ms counts as good. What is it deciding?

- A. Assume five nines for every service
- B. Publish a contractual promise with a remedy
- C. Set an internal target on that indicator
- D. Track the ratio of good requests to total requests

### 48. A sales team wants to promise 99.95 percent availability with service credits in writing. What does that produce?

- A. Publish a contractual promise with a remedy
- B. Track the ratio of good requests to total requests
- C. Choose three nines and spend the difference on features
- D. Set an internal target on that indicator

### 49. An operator must learn within an hour that the month's reliability allowance is being consumed too fast. What fits?

- A. Alert on a fast error-budget burn rate
- B. Alert when CPU stays above ninety percent for ten minutes
- C. Publish a contractual promise with a remedy
- D. Stop feature releases when the error budget is spent

### 50. A product owner asks what happens once the service has missed its objective for two weeks. What answers?

- A. Alert on a fast error-budget burn rate
- B. Add an email notification channel for the on-call group
- C. Stop feature releases when the error budget is spent
- D. Assume five nines for every service

### 51. A platform standard demands five nines for a reporting service that staff open once a week. What is wrong with that?

- A. Choose three nines and spend the difference on features
- B. Assume five nines for every service
- C. Request a quota increase and reserve capacity before the launch
- D. Publish a contractual promise with a remedy

### 52. A team accepts a lower target because the next nine costs more than the features it would block. What is that decision?

- A. Choose three nines and spend the difference on features
- B. Assume five nines for every service
- C. Register the service in the service catalog
- D. Publish a contractual promise with a remedy

### 53. An unused service still runs on its own project and its own billing line. Which state is that?

- A. Leave the unused service running for now
- B. Drain connections before removing the instance
- C. Announce the retirement date and withdraw traffic gradually
- D. Register the service in the service catalog

### 54. A replacement launches in eight weeks and the old endpoints must disappear on a date. What should be planned?

- A. Leave the unused service running for now
- B. Add capacity in a second region
- C. Announce the retirement date and withdraw traffic gradually
- D. Register the service in the service catalog

### 55. A launch needs more of a limited regional resource, and a flexible batch should wait for cheaper hours. Which two actions apply? Select two.

- A. Add capacity on a fixed calendar schedule
- B. Assume the default quota will absorb the launch
- C. Schedule the batch with Dynamic Workload Scheduler
- D. Request a quota increase and reserve capacity before the launch
- E. Put the instance group behind an autoscaler on CPU

### 56. A launch is throttled on its first day because the default limit was assumed to be enough. What was the mistake?

- A. Assume the default quota will absorb the launch
- B. Add capacity on a fixed calendar schedule
- C. Schedule the batch with Dynamic Workload Scheduler
- D. Request a quota increase and reserve capacity before the launch

### 57. A worker deployment must add replicas as the pending messages grow. What fits?

- A. Add capacity on a fixed calendar schedule
- B. Put the instance group behind an autoscaler on CPU
- C. Scale on queue depth with a horizontal pod autoscaler
- D. Set Cloud Run concurrency so replicas follow load

### 58. A serverless service must add instances as simultaneous requests rise. What fits?

- A. Set Cloud Run concurrency so replicas follow load
- B. Scale on queue depth with a horizontal pod autoscaler
- C. Put the instance group behind an autoscaler on CPU
- D. Add capacity on a fixed calendar schedule

### 59. An operator must move users to a healthy region by changing what the name resolves to. What fits?

- A. Drain connections before removing the instance
- B. Shift traffic with a DNS routing policy
- C. Use a load balancer failover backend
- D. Add capacity in a second region

### 60. A rolling replacement must finish without 502 errors from terminated pods. What must happen first?

- A. Add capacity in a second region
- B. Drain connections before removing the instance
- C. Shift traffic with a DNS routing policy
- D. Use a load balancer failover backend

### 61. The primary region is over capacity during a viral event and demand cannot be shed. What should be done?

- A. Use a load balancer failover backend
- B. Drain connections before removing the instance
- C. Request a quota increase and reserve capacity before the launch
- D. Add capacity in a second region

### 62. A release must be undone quickly, and a schema change must be reversible without data loss. Which two capabilities are needed? Select two.

- A. Redeploy the previous image to the affected service
- B. Reverse the schema change with a tested down migration
- C. Wait for the error rate to settle on its own
- D. Start from the failed step log in Cloud Build
- E. Patch production by hand and reconcile later

### 63. On-call waits forty minutes while the error rate stays high and takes no action. What is the consequence?

- A. Reverse the schema change with a tested down migration
- B. Wait for the error rate to settle on its own
- C. Redeploy the previous image to the affected service
- D. Patch production by hand and reconcile later

---

## Domain 4 — Implementing Observability Practices and Troubleshooting (Telemetry, Alerting, and Diagnosis)

### 64. Auditors need a record of who read a dataset, and host metrics must be collected from the VMs. Which two sources apply? Select two.

- A. Run an OpenTelemetry Collector in the cluster
- B. Enable Data Access audit logs for the service
- C. Turn on VPC Flow Logs for the subnet
- D. Read the Cloud Service Mesh telemetry
- E. Install the Ops Agent on the instances

### 65. The mesh must report request rate and error codes between services. What supplies that?

- A. Enable Data Access audit logs for the service
- B. Turn on VPC Flow Logs for the subnet
- C. Read the Cloud Service Mesh telemetry
- D. Run an OpenTelemetry Collector in the cluster

### 66. A chatty library logs every cache hit and the volume must fall without hiding errors. What fits?

- A. Sample the high-volume debug entries
- B. Add an exclusion for the health-check entries
- C. Drop the high-cardinality user label from the metric
- D. Measure log volume per service before choosing a retention period

### 67. Probe requests from the load balancer account for most entries and nobody reads them. What should be added?

- A. Add an exclusion for the health-check entries
- B. Route the entries to a Cloud Storage bucket
- C. Sample the high-volume debug entries
- D. Drop the high-cardinality user label from the metric

### 68. An engineer must isolate one service's entries, then inspect the neighbouring entries of a failure. Which two capabilities apply? Select two.

- A. Create an uptime check against the login flow
- B. Filter with the Logging query language on the resource label
- C. Create a log-based metric for the error string
- D. Open the Logs Explorer and pivot from the error entry
- E. Route the entries to a BigQuery dataset

### 69. A recurring error string must drive an alert without any change to application code. What fits?

- A. Create a log-based metric for the error string
- B. Emit a custom metric for the business event
- C. Open the Logs Explorer and pivot from the error entry
- D. Filter with the Logging query language on the resource label

### 70. Seven years of entries must be kept cheaply and almost never queried. What fits?

- A. Route the entries to a BigQuery dataset
- B. Route the entries to a Pub/Sub topic
- C. Set the log bucket retention and lock it
- D. Route the entries to a Cloud Storage bucket

### 71. A third-party SIEM must receive entries in near real time. What fits?

- A. Route the entries to a Cloud Storage bucket
- B. Route the entries to a BigQuery dataset
- C. Set the log bucket retention and lock it
- D. Route the entries to a Pub/Sub topic

### 72. Protected health information appears in request logs and must be removed before storage. What should be configured?

- A. Ask analysts not to read the sensitive field
- B. Route the entries to a Cloud Storage bucket
- C. Redact the email field with a log processor
- D. Sample the high-volume debug entries

### 73. A reviewer wants the sharp step in a latency chart interpreted in words. What fits?

- A. Ask Gemini Cloud Assist to summarise the failing entries
- B. Filter with the Logging query language on the resource label
- C. Ask Gemini Cloud Assist to explain the metric spike
- D. Ask Gemini Cloud Assist which span dominates the trace

### 74. Legacy VMs must report host metrics, and the mesh must report request behaviour between services. Which two sources apply? Select two.

- A. Turn on VPC Flow Logs for the subnet
- B. Install the Ops Agent on the instances
- C. Enable Data Access audit logs for the service
- D. Read the Cloud Service Mesh telemetry
- E. Run an OpenTelemetry Collector in the cluster

### 75. Traces must be collected once and exported to two separate backends. What fits?

- A. Emit a custom metric for the business event
- B. Read the Cloud Service Mesh telemetry
- C. Run an OpenTelemetry Collector in the cluster
- D. Install the Ops Agent on the instances

### 76. A new checkout step must publish its own duration as a measurement. What should the application do?

- A. Emit a custom metric for the business event
- B. Scrape the workload with managed collection for Prometheus
- C. Create an uptime check against the login flow
- D. Create a log-based metric for the error string

### 77. An outage in a third-party redirect must be noticed before customers call support. What fits?

- A. Emit a custom metric for the business event
- B. Scrape the workload with managed collection for Prometheus
- C. Create a log-based metric for the error string
- D. Create an uptime check against the login flow

### 78. Each service needs one page combining its objective, its error rate, and its saturation. What should be built?

- A. Attach the remediation playbook to the alert
- B. Alert when CPU stays above ninety percent for ten minutes
- C. Build one dashboard and share it with the on-call rotation
- D. Send the alert to PagerDuty through a webhook

### 79. An alert arrives at three in the morning with no hint about what the responder should try. What fits?

- A. Build one dashboard and share it with the on-call rotation
- B. Add an email notification channel for the on-call group
- C. Attach the remediation playbook to the alert
- D. Create an alerting policy on the SLO burn rate

### 80. Pages must reflect user-visible reliability, and one host metric must still warn before saturation. Which two policies apply? Select two.

- A. Attach the remediation playbook to the alert
- B. Create an alerting policy on the SLO burn rate
- C. Send the alert to PagerDuty through a webhook
- D. Add an email notification channel for the on-call group
- E. Alert when CPU stays above ninety percent for ten minutes

### 81. Alerts must open a ticket in the incident tool the responders already use. What fits?

- A. Attach the remediation playbook to the alert
- B. Create an alerting policy on the SLO burn rate
- C. Add an email notification channel for the on-call group
- D. Send the alert to PagerDuty through a webhook

### 82. A compliance team must receive a copy of every alert for its audit file. What fits?

- A. Alert when CPU stays above ninety percent for ten minutes
- B. Add an email notification channel for the on-call group
- C. Attach the remediation playbook to the alert
- D. Send the alert to PagerDuty through a webhook

### 83. A service written in Go must emit timing for each downstream call it makes. What fits?

- A. Instrument the service with OpenTelemetry spans
- B. Read the trace waterfall to find the slow span
- C. Ask Gemini Cloud Assist which span dominates the trace
- D. Put the trace ID in the structured log line

### 84. Logs and traces are matched by hand using clock times. Why does that approach fail?

- A. Put the trace ID in the structured log line
- B. Instrument the service with OpenTelemetry spans
- C. Read the trace waterfall to find the slow span
- D. Log a timestamp and correlate by eye later

### 85. A log line must be findable from the trace that produced it. What makes that possible?

- A. Instrument the service with OpenTelemetry spans
- B. Put the trace ID in the structured log line
- C. Log a timestamp and correlate by eye later
- D. Read the trace waterfall to find the slow span

### 86. A health check fails only from one subnet that was rebuilt last week. What should be checked?

- A. Inspect the image pull credential and repository permission
- B. Check the DNS record and its remaining TTL
- C. Check Cloud NAT port exhaustion for the egress range
- D. Read the firewall rule that hit the denied flow

### 87. Latency is high inside one service while its CPU and memory look normal. What fits?

- A. Check the DNS record and its remaining TTL
- B. Profile the slow endpoint inside the application
- C. Check Cloud NAT port exhaustion for the egress range
- D. Compare the readiness probe with the application startup time

### 88. Clients still reach the retired address an hour after the cutover. What explains that?

- A. Read the firewall rule that hit the denied flow
- B. Check Cloud NAT port exhaustion for the egress range
- C. Check the DNS record and its remaining TTL
- D. Profile the slow endpoint inside the application

---

## Domain 5 — Optimizing Performance and Cost (FinOps and Performance Tuning)

### 89. Support tickets say the site is slow, but no chart shows which call degraded. What should be used?

- A. Export billing data to BigQuery for the chargeback report
- B. Right-size the node pool from the observed requests
- C. Track the service objective on a shared dashboard
- D. Measure request latency by endpoint in Cloud Monitoring

### 90. A service owner wants the reliability goal and the current performance visible together. What fits?

- A. Apply the cost recommender suggestion for the idle disks
- B. Measure log volume per service before choosing a retention period
- C. Measure request latency by endpoint in Cloud Monitoring
- D. Track the service objective on a shared dashboard

### 91. Nobody knows which recommendations Google has already generated for the project. What should be done?

- A. Apply the reliability recommender for the missing quota
- B. Apply the cost recommender suggestion for the idle disks
- C. Export billing data to BigQuery for the chargeback report
- D. Review the Active Assist recommendations for the project

### 92. Half the persistent disks are unattached and still being billed. Which recommendation applies?

- A. Review the Active Assist recommendations for the project
- B. Apply the reliability recommender for the missing quota
- C. Run the batch on Spot VMs
- D. Apply the cost recommender suggestion for the idle disks

### 93. Observability spend must be estimated before a retention period is chosen, and noisy debug entries must stop being billed. Which two actions apply? Select two.

- A. Serve the bulk export over the Standard network tier
- B. Drop the high-cardinality user label from the metric
- C. Set the log bucket retention and lock it
- D. Exclude the debug stream and keep the error stream
- E. Measure log volume per service before choosing a retention period

### 94. A per-request identifier was added to a metric label and the series count tripled. What caused that?

- A. Measure log volume per service before choosing a retention period
- B. Exclude the debug stream and keep the error stream
- C. Drop the high-cardinality user label from the metric
- D. Set the log bucket retention and lock it

### 95. A nightly rendering job tolerates interruption and is the largest compute line. What fits?

- A. Run the batch on Spot VMs
- B. Put the stateless workers on a Spot node pool
- C. Buy a committed-use discount for the steady baseline
- D. Move the primary database onto Spot capacity

### 96. A design moves the session store onto reclaimable capacity and sessions start disappearing. What is the cause?

- A. Put the stateless workers on a Spot node pool
- B. Move the primary database onto Spot capacity
- C. Run the batch on Spot VMs
- D. Buy a committed-use discount for the steady baseline

### 97. A three-year baseline is predictable and finance wants the lowest unit price. What fits?

- A. Rely on sustained-use discounts for the steady baseline
- B. Buy a committed-use discount for the steady baseline
- C. Run the batch on Spot VMs
- D. Serve the bulk export over the Standard network tier

### 98. A nightly analytics export between regions may take longer if it costs less. What fits?

- A. Buy a committed-use discount for the steady baseline
- B. Serve the bulk export over the Standard network tier
- C. Keep the interactive traffic on the Premium tier
- D. Put the stateless workers on a Spot node pool

### 99. A pool reserves far more CPU than its pods request, and a development service is idle overnight. Which two actions apply? Select two.

- A. Right-size the node pool from the observed requests
- B. Keep the minimum instance count at zero for the internal tool
- C. Stop the idle non-production instances on a schedule
- D. Move the primary database onto Spot capacity
- E. Set a minimum instance count for the latency-critical service

### 100. Non-production VMs run all weekend with no users at all. What should be done?

- A. Keep the minimum instance count at zero for the internal tool
- B. Buy a committed-use discount for the steady baseline
- C. Stop the idle non-production instances on a schedule
- D. Right-size the node pool from the observed requests

---

## Answer key and explanations

### Question 1 — B

Answer: Apply the constraint to the business unit folder. A folder-level constraint applies only to that business unit subtree. A constraint attached to one folder and inherited by its projects. Local study-map skill 1.1 (Resource Hierarchy and Project Organization), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 1 (bootstrapping and maintaining a Google Cloud organization): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A constraint set per project with no inheritance. Why the correct answer wins: A folder-level constraint applies only to that business unit subtree.
- **B:** Correct. A constraint attached to one folder and inherited by its projects. In this case: A folder-level constraint applies only to that business unit subtree.
- **C:** Incorrect for this question. An explicit denial that overrides any allow. Why the correct answer wins: A folder-level constraint applies only to that business unit subtree.
- **D:** Incorrect for this question. An organization-level constraint that every folder and project inherits. Why the correct answer wins: A folder-level constraint applies only to that business unit subtree.

### Question 2 — B

Answer: Group projects by environment with applications below. An environment-centric layout separates production before anything else. An environment-centric layout that separates production from staging first. Local study-map skill 1.1 (Resource Hierarchy and Project Organization), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 1 (bootstrapping and maintaining a Google Cloud organization): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A constraint attached to one folder and inherited by its projects. Why the correct answer wins: An environment-centric layout separates production before anything else.
- **B:** Correct. An environment-centric layout that separates production from staging first. In this case: An environment-centric layout separates production before anything else.
- **C:** Incorrect for this question. A constraint set per project with no inheritance. Why the correct answer wins: An environment-centric layout separates production before anything else.
- **D:** Incorrect for this question. An application-centric layout that keeps one service and its owners together. Why the correct answer wins: An environment-centric layout separates production before anything else.

### Question 3 — B, D

Answers: Create a Shared VPC host project and attach the service projects; Publish the service behind a Private Service Connect endpoint. Shared VPC centralises the subnets, and Private Service Connect exposes no public address. A central network project that lends subnets to other projects. A private endpoint that consumes a published service. Local study-map skill 1.2 (Shared Networking for Multi-Project Estates), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 1 (bootstrapping and maintaining a Google Cloud organization): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. An organization-level constraint that every folder and project inherits. Why the correct answer wins: Shared VPC centralises the subnets, and Private Service Connect exposes no public address.
- **B:** Correct. A central network project that lends subnets to other projects. In this case: Shared VPC centralises the subnets, and Private Service Connect exposes no public address.
- **C:** Incorrect for this question. Duplicate networks with a separately managed egress path. Why the correct answer wins: Shared VPC centralises the subnets, and Private Service Connect exposes no public address.
- **D:** Correct. A private endpoint that consumes a published service. In this case: Shared VPC centralises the subnets, and Private Service Connect exposes no public address.
- **E:** Incorrect for this question. A mesh of peering links that grows with each new project. Why the correct answer wins: Shared VPC centralises the subnets, and Private Service Connect exposes no public address.

### Question 4 — B

Answer: Peer every project VPC with every other project VPC. Pairwise peering adds a link for every pair of projects. A mesh of peering links that grows with each new project. Local study-map skill 1.2 (Shared Networking for Multi-Project Estates), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 1 (bootstrapping and maintaining a Google Cloud organization): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Duplicate networks with a separately managed egress path. Why the correct answer wins: Pairwise peering adds a link for every pair of projects.
- **B:** Correct. A mesh of peering links that grows with each new project. In this case: Pairwise peering adds a link for every pair of projects.
- **C:** Incorrect for this question. A private endpoint that consumes a published service. Why the correct answer wins: Pairwise peering adds a link for every pair of projects.
- **D:** Incorrect for this question. A central network project that lends subnets to other projects. Why the correct answer wins: Pairwise peering adds a link for every pair of projects.

### Question 5 — D

Answer: Add the projects to one metrics scope. A metrics scope charts series from several projects together. An observability scope that spans several projects. Local study-map skill 1.3 (Multi-Project Monitoring and Logging), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 1 (bootstrapping and maintaining a Google Cloud organization): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A sink that lands logs in a queryable table. Why the correct answer wins: A metrics scope charts series from several projects together.
- **B:** Incorrect for this question. Log storage scoped to the project that produced the entries. Why the correct answer wins: A metrics scope charts series from several projects together.
- **C:** Incorrect for this question. A single destination that collects entries from many projects. Why the correct answer wins: A metrics scope charts series from several projects together.
- **D:** Correct. An observability scope that spans several projects. In this case: A metrics scope charts series from several projects together.

### Question 6 — B

Answer: Grant a predefined role once at the folder. A predefined role already covers the standard permission set. A Google-managed role bound at folder level. Local study-map skill 1.4 (IAM Roles and Organization Policies), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 1 (bootstrapping and maintaining a Google Cloud organization): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A guardrail that holds regardless of the IAM grants. Why the correct answer wins: A predefined role already covers the standard permission set.
- **B:** Correct. A Google-managed role bound at folder level. In this case: A predefined role already covers the standard permission set.
- **C:** Incorrect for this question. A role defined from an explicit permission list. Why the correct answer wins: A predefined role already covers the standard permission set.
- **D:** Incorrect for this question. An explicit denial that overrides any allow. Why the correct answer wins: A predefined role already covers the standard permission set.

### Question 7 — A

Answer: Add an IAM deny policy for the sensitive permission. An IAM deny policy overrides every allow for that permission. An explicit denial that overrides any allow. Local study-map skill 1.4 (IAM Roles and Organization Policies), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 1 (bootstrapping and maintaining a Google Cloud organization): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Correct. An explicit denial that overrides any allow. In this case: An IAM deny policy overrides every allow for that permission.
- **B:** Incorrect for this question. A guardrail that holds regardless of the IAM grants. Why the correct answer wins: An IAM deny policy overrides every allow for that permission.
- **C:** Incorrect for this question. A role defined from an explicit permission list. Why the correct answer wins: An IAM deny policy overrides every allow for that permission.
- **D:** Incorrect for this question. A Google-managed role bound at folder level. Why the correct answer wins: An IAM deny policy overrides every allow for that permission.

### Question 8 — A, E

Answers: Create one service account per workload; Grant impersonation of the service account instead of a key. One account per workload isolates access, and impersonation avoids keys. A dedicated identity for each deployed workload. Short-lived credentials obtained by impersonating the account. Local study-map skill 1.5 (Service Account Management), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 1 (bootstrapping and maintaining a Google Cloud organization): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Correct. Short-lived credentials obtained by impersonating the account. In this case: One account per workload isolates access, and impersonation avoids keys.
- **B:** Incorrect for this question. The account created automatically with broad project access. Why the correct answer wins: One account per workload isolates access, and impersonation avoids keys.
- **C:** Incorrect for this question. A long-lived credential stored outside the platform. Why the correct answer wins: One account per workload isolates access, and impersonation avoids keys.
- **D:** Incorrect for this question. Separate identities so a staging credential cannot act in production. Why the correct answer wins: One account per workload isolates access, and impersonation avoids keys.
- **E:** Correct. A dedicated identity for each deployed workload. In this case: One account per workload isolates access, and impersonation avoids keys.

### Question 9 — B

Answer: Place the resources in a region that satisfies the residency rule. The resource location must satisfy the residency requirement. A location choice that keeps data inside the required boundary. Local study-map skill 1.6 (Data Residency in the Hierarchy), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 1 (bootstrapping and maintaining a Google Cloud organization): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A central network project that lends subnets to other projects. Why the correct answer wins: The resource location must satisfy the residency requirement.
- **B:** Correct. A location choice that keeps data inside the required boundary. In this case: The resource location must satisfy the residency requirement.
- **C:** Incorrect for this question. A copy held elsewhere for recovery rather than residency. Why the correct answer wins: The resource location must satisfy the residency requirement.
- **D:** Incorrect for this question. An organization-level constraint that every folder and project inherits. Why the correct answer wins: The resource location must satisfy the residency requirement.

### Question 10 — A

Answer: Define the estate as Terraform modules held in version control. A Terraform module makes each change visible as a diff. Declarative code that is reviewed before it is applied. Local study-map skill 1.7 (Infrastructure-as-Code Tool Selection), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 1 (bootstrapping and maintaining a Google Cloud organization): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Correct. Declarative code that is reviewed before it is applied. In this case: A Terraform module makes each change visible as a diff.
- **B:** Incorrect for this question. A managed service that runs Terraform deployments. Why the correct answer wins: A Terraform module makes each change visible as a diff.
- **C:** Incorrect for this question. A templated bundle of Kubernetes resources. Why the correct answer wins: A Terraform module makes each change visible as a diff.
- **D:** Incorrect for this question. A controller that keeps Kubernetes manifests and cloud resources aligned. Why the correct answer wins: A Terraform module makes each change visible as a diff.

### Question 11 — C

Answer: Reconcile the resources with Config Connector. Config Connector creates cloud resources from those manifests. A controller that keeps Kubernetes manifests and cloud resources aligned. Local study-map skill 1.7 (Infrastructure-as-Code Tool Selection), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 1 (bootstrapping and maintaining a Google Cloud organization): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A managed service that runs Terraform deployments. Why the correct answer wins: Config Connector creates cloud resources from those manifests.
- **B:** Incorrect for this question. Declarative code that is reviewed before it is applied. Why the correct answer wins: Config Connector creates cloud resources from those manifests.
- **C:** Correct. A controller that keeps Kubernetes manifests and cloud resources aligned. In this case: Config Connector creates cloud resources from those manifests.
- **D:** Incorrect for this question. A templated bundle of Kubernetes resources. Why the correct answer wins: Config Connector creates cloud resources from those manifests.

### Question 12 — A

Answer: Schedule a plan that reports drift. A recurring plan reports the drift between code and reality. A recurring comparison of declared and actual state. Local study-map skill 1.8 (Blueprints and Controlled Infrastructure Change), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 1 (bootstrapping and maintaining a Google Cloud organization): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Correct. A recurring comparison of declared and actual state. In this case: A recurring plan reports the drift between code and reality.
- **B:** Incorrect for this question. A manual sequence repeated on every occasion. Why the correct answer wins: A recurring plan reports the drift between code and reality.
- **C:** Incorrect for this question. Google-maintained Terraform templates for common foundations. Why the correct answer wins: A recurring plan reports the drift between code and reality.
- **D:** Incorrect for this question. An unmanaged change with no enforceable record. Why the correct answer wins: A recurring plan reports the drift between code and reality.

### Question 13 — C

Answer: Automate the repeated step with a Python script calling the API. A script calling the API deletes them identically every night. Idempotent automation through the client library. Local study-map skill 1.9 (Automation with Scripting and APIs), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 1 (bootstrapping and maintaining a Google Cloud organization): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A manual sequence repeated on every occasion. Why the correct answer wins: A script calling the API deletes them identically every night.
- **B:** Incorrect for this question. An unmanaged change with no enforceable record. Why the correct answer wins: A script calling the API deletes them identically every night.
- **C:** Correct. Idempotent automation through the client library. In this case: A script calling the API deletes them identically every night.
- **D:** Incorrect for this question. A transformation pipeline that keeps the source declarative. Why the correct answer wins: A script calling the API deletes them identically every night.

### Question 14 — C

Answer: Run Jenkins on a self-managed VM. Jenkins stays the CI server and the artifacts land in the registry. A self-operated CI server whose patching is your problem. Local study-map skill 1.10 (CI/CD Architecture Stack Design), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 1 (bootstrapping and maintaining a Google Cloud organization): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A regional repository for images and packages. Why the correct answer wins: Jenkins stays the CI server and the artifacts land in the registry.
- **B:** Incorrect for this question. A managed pair that separates building from releasing. Why the correct answer wins: Jenkins stays the CI server and the artifacts land in the registry.
- **C:** Correct. A self-operated CI server whose patching is your problem. In this case: Jenkins stays the CI server and the artifacts land in the registry.
- **D:** Incorrect for this question. A pull-based delivery controller. Why the correct answer wins: Jenkins stays the CI server and the artifacts land in the registry.

### Question 15 — D

Answer: Use Cloud Build for CI and Cloud Deploy for delivery. Managed build and delivery leave nothing for the team to patch. A managed pair that separates building from releasing. Local study-map skill 1.10 (CI/CD Architecture Stack Design), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 1 (bootstrapping and maintaining a Google Cloud organization): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A reproducible image built before deployment. Why the correct answer wins: Managed build and delivery leave nothing for the team to patch.
- **B:** Incorrect for this question. A pull-based delivery controller. Why the correct answer wins: Managed build and delivery leave nothing for the team to patch.
- **C:** Incorrect for this question. A self-operated CI server whose patching is your problem. Why the correct answer wins: Managed build and delivery leave nothing for the team to patch.
- **D:** Correct. A managed pair that separates building from releasing. In this case: Managed build and delivery leave nothing for the team to patch.

### Question 16 — C

Answer: Bake the machine image with Packer. Packer bakes one image that every environment reuses. A reproducible image built before deployment. Local study-map skill 1.11 (Third-Party Tooling in the Pipeline), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 1 (bootstrapping and maintaining a Google Cloud organization): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A transformation pipeline that keeps the source declarative. Why the correct answer wins: Packer bakes one image that every environment reuses.
- **B:** Incorrect for this question. Declarative code that is reviewed before it is applied. Why the correct answer wins: Packer bakes one image that every environment reuses.
- **C:** Correct. A reproducible image built before deployment. In this case: Packer bakes one image that every environment reuses.
- **D:** Incorrect for this question. A templated bundle of Kubernetes resources. Why the correct answer wins: Packer bakes one image that every environment reuses.

### Question 17 — D, E

Answers: Create a short-lived project per change and delete it after review; Keep one shared staging environment for every team. An ephemeral project lives for one change, and staging runs the integration suite. An environment that exists only while a change is tested. A permanent pre-production environment. Local study-map skill 1.12 (Multiple Environment Management), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 1 (bootstrapping and maintaining a Google Cloud organization): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. One image per environment with the settings compiled in. Why the correct answer wins: An ephemeral project lives for one change, and staging runs the integration suite.
- **B:** Incorrect for this question. An environment-centric layout that separates production from staging first. Why the correct answer wins: An ephemeral project lives for one change, and staging runs the integration suite.
- **C:** Incorrect for this question. A constraint set per project with no inheritance. Why the correct answer wins: An ephemeral project lives for one change, and staging runs the integration suite.
- **D:** Correct. An environment that exists only while a change is tested. In this case: An ephemeral project lives for one change, and staging runs the integration suite.
- **E:** Correct. A permanent pre-production environment. In this case: An ephemeral project lives for one change, and staging runs the integration suite.

### Question 18 — D

Answer: Stand up a second cluster and shift traffic after verification. A second cluster proves the upgrade before traffic shifts. A parallel cluster used to prove the upgrade. Local study-map skill 1.13 (Fleets, Patching, and Cluster Upgrades), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 1 (bootstrapping and maintaining a Google Cloud organization): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A managed upgrade cadence inside a chosen window. Why the correct answer wins: A second cluster proves the upgrade before traffic shifts.
- **B:** Incorrect for this question. An environment that exists only while a change is tested. Why the correct answer wins: A second cluster proves the upgrade before traffic shifts.
- **C:** Incorrect for this question. An operator-driven upgrade with no cadence. Why the correct answer wins: A second cluster proves the upgrade before traffic shifts.
- **D:** Correct. A parallel cluster used to prove the upgrade. In this case: A second cluster proves the upgrade before traffic shifts.

### Question 19 — B

Answer: Build a custom image that carries the approved toolchain. A custom image pins the approved toolchain at every start. A pinned toolchain that every workstation starts from. Local study-map skill 1.14 (Secure Development Environments and AI Assistance), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 1 (bootstrapping and maintaining a Google Cloud organization): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Unmanaged toolchains on unmanaged machines. Why the correct answer wins: A custom image pins the approved toolchain at every start.
- **B:** Correct. A pinned toolchain that every workstation starts from. In this case: A custom image pins the approved toolchain at every start.
- **C:** Incorrect for this question. A managed IDE that runs inside the project boundary. Why the correct answer wins: A custom image pins the approved toolchain at every start.
- **D:** Incorrect for this question. A browser terminal with limited tooling and lifetime. Why the correct answer wins: A custom image pins the approved toolchain at every start.

### Question 20 — D

Answer: Use Gemini CLI for the repetitive script. Gemini CLI drafts and explains the terminal command. A terminal assistant that drafts and runs commands. Local study-map skill 1.14 (Secure Development Environments and AI Assistance), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 1 (bootstrapping and maintaining a Google Cloud organization): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Unmanaged toolchains on unmanaged machines. Why the correct answer wins: Gemini CLI drafts and explains the terminal command.
- **B:** Incorrect for this question. An in-editor assistant that proposes code. Why the correct answer wins: Gemini CLI drafts and explains the terminal command.
- **C:** Incorrect for this question. An assistant that reads telemetry and configuration. Why the correct answer wins: Gemini CLI drafts and explains the terminal command.
- **D:** Correct. A terminal assistant that drafts and runs commands. In this case: Gemini CLI drafts and explains the terminal command.

### Question 21 — D

Answer: Create a trigger that runs the tests on every pull request. A pull-request trigger runs the validation before merge. A pre-merge check that blocks a bad change early. Local study-map skill 2.1 (Pipeline Triggers and Design), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 2 (building and implementing CI/CD pipelines): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A trigger that starts the build on a branch change. Why the correct answer wins: A pull-request trigger runs the validation before merge.
- **B:** Incorrect for this question. A release build that a tag alone can start. Why the correct answer wins: A pull-request trigger runs the validation before merge.
- **C:** Incorrect for this question. The immutable record of who released what. Why the correct answer wins: A pull-request trigger runs the validation before merge.
- **D:** Correct. A pre-merge check that blocks a bad change early. In this case: A pull-request trigger runs the validation before merge.

### Question 22 — C

Answer: Trigger the pipeline only on a signed tag. A tag trigger restricts builds to signed releases only. A release build that a tag alone can start. Local study-map skill 2.1 (Pipeline Triggers and Design), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 2 (building and implementing CI/CD pipelines): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A pre-merge check that blocks a bad change early. Why the correct answer wins: A tag trigger restricts builds to signed releases only.
- **B:** Incorrect for this question. A trigger that starts the build on a branch change. Why the correct answer wins: A tag trigger restricts builds to signed releases only.
- **C:** Correct. A release build that a tag alone can start. In this case: A tag trigger restricts builds to signed releases only.
- **D:** Incorrect for this question. A hand-built artifact with no pipeline record. Why the correct answer wins: A tag trigger restricts builds to signed releases only.

### Question 23 — A

Answer: Create a Cloud Build trigger on the release branch. A branch trigger rebuilds on every landed commit. A trigger that starts the build on a branch change. Local study-map skill 2.1 (Pipeline Triggers and Design), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 2 (building and implementing CI/CD pipelines): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Correct. A trigger that starts the build on a branch change. In this case: A branch trigger rebuilds on every landed commit.
- **B:** Incorrect for this question. A hand-built artifact with no pipeline record. Why the correct answer wins: A branch trigger rebuilds on every landed commit.
- **C:** Incorrect for this question. A pre-merge check that blocks a bad change early. Why the correct answer wins: A branch trigger rebuilds on every landed commit.
- **D:** Incorrect for this question. A release build that a tag alone can start. Why the correct answer wins: A branch trigger rebuilds on every landed commit.

### Question 24 — B

Answer: Tag each artifact with the commit SHA and forbid overwrite. An immutable tag still resolves to the same artifact later. An immutable tag that identifies the source revision. Local study-map skill 2.2 (Artifact Management), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 2 (building and implementing CI/CD pipelines): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A moving tag that hides which build is running. Why the correct answer wins: An immutable tag still resolves to the same artifact later.
- **B:** Correct. An immutable tag that identifies the source revision. In this case: An immutable tag still resolves to the same artifact later.
- **C:** Incorrect for this question. The legacy registry without regional repository controls. Why the correct answer wins: An immutable tag still resolves to the same artifact later.
- **D:** Incorrect for this question. A reproducible image built before deployment. Why the correct answer wins: An immutable tag still resolves to the same artifact later.

### Question 25 — D

Answer: Push the image to Container Registry. The legacy registry lacks regional repository controls. Local study-map skill 2.2 (Artifact Management), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 2 (building and implementing CI/CD pipelines): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. An immutable tag that identifies the source revision. Why the correct answer wins: The legacy registry lacks regional repository controls.
- **B:** Incorrect for this question. A regional repository for images and packages. Why the correct answer wins: The legacy registry lacks regional repository controls.
- **C:** Incorrect for this question. Metadata that ties an artifact to its build inputs. Why the correct answer wins: The legacy registry lacks regional repository controls.
- **D:** Correct. In this case: The legacy registry lacks regional repository controls.

### Question 26 — C

Answer: Use a GKE cluster in the pipeline project as the target. A GKE target releases into that project's cluster. A delivery target that sits inside the same project. Local study-map skill 2.3 (Hybrid and Multicloud Deployment Targets), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 2 (building and implementing CI/CD pipelines): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A target that points at a GKE cluster outside Google Cloud. Why the correct answer wins: A GKE target releases into that project's cluster.
- **B:** Incorrect for this question. A required human approval before the release promotes. Why the correct answer wins: A GKE target releases into that project's cluster.
- **C:** Correct. A delivery target that sits inside the same project. In this case: A GKE target releases into that project's cluster.
- **D:** Incorrect for this question. A revision-based target with traffic control. Why the correct answer wins: A GKE target releases into that project's cluster.

### Question 27 — C

Answer: Define the attached cluster as the delivery target. An attached cluster can point outside Google Cloud. A target that points at a GKE cluster outside Google Cloud. Local study-map skill 2.3 (Hybrid and Multicloud Deployment Targets), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 2 (building and implementing CI/CD pipelines): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A revision-based target with traffic control. Why the correct answer wins: An attached cluster can point outside Google Cloud.
- **B:** Incorrect for this question. A delivery target that sits inside the same project. Why the correct answer wins: An attached cluster can point outside Google Cloud.
- **C:** Correct. A target that points at a GKE cluster outside Google Cloud. In this case: An attached cluster can point outside Google Cloud.
- **D:** Incorrect for this question. The immutable record of who released what. Why the correct answer wins: An attached cluster can point outside Google Cloud.

### Question 28 — A, E

Answers: Add a Cloud Deploy approval gate before production; Promote automatically to every target in the chain. The gate blocks staging, and automatic promotion frees development. A required human approval before the release promotes. An unattended path from commit to production. Local study-map skill 2.4 (Approval Flows and Deployment Process), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 2 (building and implementing CI/CD pipelines): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Correct. An unattended path from commit to production. In this case: The gate blocks staging, and automatic promotion frees development.
- **B:** Incorrect for this question. A hand-built artifact with no pipeline record. Why the correct answer wins: The gate blocks staging, and automatic promotion frees development.
- **C:** Incorrect for this question. A return to the last known good release. Why the correct answer wins: The gate blocks staging, and automatic promotion frees development.
- **D:** Incorrect for this question. The immutable record of who released what. Why the correct answer wins: The gate blocks staging, and automatic promotion frees development.
- **E:** Correct. A required human approval before the release promotes. In this case: The gate blocks staging, and automatic promotion frees development.

### Question 29 — A

Answer: Read Cloud Audit Logs for the release history. Cloud Audit Logs record who released what and when. The immutable record of who released what. Local study-map skill 2.5 (Deployment Auditing and Tracking), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 2 (building and implementing CI/CD pipelines): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Correct. The immutable record of who released what. In this case: Cloud Audit Logs record who released what and when.
- **B:** Incorrect for this question. Metadata that ties an artifact to its build inputs. Why the correct answer wins: Cloud Audit Logs record who released what and when.
- **C:** Incorrect for this question. An immutable tag that identifies the source revision. Why the correct answer wins: Cloud Audit Logs record who released what and when.
- **D:** Incorrect for this question. A required human approval before the release promotes. Why the correct answer wins: Cloud Audit Logs record who released what and when.

### Question 30 — C

Answer: Inspect the build provenance attestation. Provenance records the inputs and the steps of the build. Metadata that ties an artifact to its build inputs. Local study-map skill 2.5 (Deployment Auditing and Tracking), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 2 (building and implementing CI/CD pipelines): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. The immutable record of who released what. Why the correct answer wins: Provenance records the inputs and the steps of the build.
- **B:** Incorrect for this question. An immutable tag that identifies the source revision. Why the correct answer wins: Provenance records the inputs and the steps of the build.
- **C:** Correct. Metadata that ties an artifact to its build inputs. In this case: Provenance records the inputs and the steps of the build.
- **D:** Incorrect for this question. A published statement about how the artifact was produced. Why the correct answer wins: Provenance records the inputs and the steps of the build.

### Question 31 — A, C

Answers: Run the new version alongside and switch traffic at once; Replace the instances in batches. Blue/green swaps traffic at once, and rolling replaces instances gradually. Two full environments with an instant cutover. A gradual replacement of the running instances. Local study-map skill 2.6 (Deployment Strategies), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 2 (building and implementing CI/CD pipelines): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Correct. A gradual replacement of the running instances. In this case: Blue/green swaps traffic at once, and rolling replaces instances gradually.
- **B:** Incorrect for this question. A small traffic slice that bounds the blast radius. Why the correct answer wins: Blue/green swaps traffic at once, and rolling replaces instances gradually.
- **C:** Correct. Two full environments with an instant cutover. In this case: Blue/green swaps traffic at once, and rolling replaces instances gradually.
- **D:** Incorrect for this question. A full outage during the change. Why the correct answer wins: Blue/green swaps traffic at once, and rolling replaces instances gradually.
- **E:** Incorrect for this question. Weighted routing between two service versions. Why the correct answer wins: Blue/green swaps traffic at once, and rolling replaces instances gradually.

### Question 32 — D

Answer: Replace the instances in batches. A rolling strategy replaces instances without a full outage. A gradual replacement of the running instances. Local study-map skill 2.6 (Deployment Strategies), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 2 (building and implementing CI/CD pipelines): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A full outage during the change. Why the correct answer wins: A rolling strategy replaces instances without a full outage.
- **B:** Incorrect for this question. Two full environments with an instant cutover. Why the correct answer wins: A rolling strategy replaces instances without a full outage.
- **C:** Incorrect for this question. A small traffic slice that bounds the blast radius. Why the correct answer wins: A rolling strategy replaces instances without a full outage.
- **D:** Correct. A gradual replacement of the running instances. In this case: A rolling strategy replaces instances without a full outage.

### Question 33 — B

Answer: Send ten percent of traffic to the new revision and watch the SLI. A canary holds exposure to a small traffic share. A small traffic slice that bounds the blast radius. Local study-map skill 2.6 (Deployment Strategies), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 2 (building and implementing CI/CD pipelines): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A full outage during the change. Why the correct answer wins: A canary holds exposure to a small traffic share.
- **B:** Correct. A small traffic slice that bounds the blast radius. In this case: A canary holds exposure to a small traffic share.
- **C:** Incorrect for this question. A gradual replacement of the running instances. Why the correct answer wins: A canary holds exposure to a small traffic share.
- **D:** Incorrect for this question. Two full environments with an instant cutover. Why the correct answer wins: A canary holds exposure to a small traffic share.

### Question 34 — D

Answer: Gate the rollout on average CPU alone. CPU says nothing about whether users can finish a purchase. A resource signal that says nothing about user success. Local study-map skill 2.7 (Deployment Success Metrics), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 2 (building and implementing CI/CD pipelines): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A required human approval before the release promotes. Why the correct answer wins: CPU says nothing about whether users can finish a purchase.
- **B:** Incorrect for this question. A probe that exercises the path from outside. Why the correct answer wins: CPU says nothing about whether users can finish a purchase.
- **C:** Incorrect for this question. An automated decision driven by the service objective. Why the correct answer wins: CPU says nothing about whether users can finish a purchase.
- **D:** Correct. A resource signal that says nothing about user success. In this case: CPU says nothing about whether users can finish a purchase.

### Question 35 — B

Answer: Roll the release back to the previous one. Rolling back returns to the release that worked. A return to the last known good release. Local study-map skill 2.8 (Troubleshooting Deployment Issues), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 2 (building and implementing CI/CD pipelines): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. An untracked change to the live environment. Why the correct answer wins: Rolling back returns to the release that worked.
- **B:** Correct. A return to the last known good release. In this case: Rolling back returns to the release that worked.
- **C:** Incorrect for this question. A safe repeat that converges on the same state. Why the correct answer wins: Rolling back returns to the release that worked.
- **D:** Incorrect for this question. The step output that names the failing command. Why the correct answer wins: Rolling back returns to the release that worked.

### Question 36 — A

Answer: Patch production by hand and reconcile later. The hand fix leaves declared code and live state apart. An untracked change to the live environment. Local study-map skill 2.8 (Troubleshooting Deployment Issues), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 2 (building and implementing CI/CD pipelines): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Correct. An untracked change to the live environment. In this case: The hand fix leaves declared code and live state apart.
- **B:** Incorrect for this question. A safe repeat that converges on the same state. Why the correct answer wins: The hand fix leaves declared code and live state apart.
- **C:** Incorrect for this question. A return to the last known good release. Why the correct answer wins: The hand fix leaves declared code and live state apart.
- **D:** Incorrect for this question. A recurring comparison of declared and actual state. Why the correct answer wins: The hand fix leaves declared code and live state apart.

### Question 37 — A, B

Answers: Encrypt the payload with a Cloud KMS key; Issue and rotate the certificate with Certificate Manager. Cloud KMS wraps the object, and Certificate Manager issues the certificates. A managed key that wraps the data. Managed issuance and renewal for the endpoint. Local study-map skill 2.9 (Key Management), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 2 (building and implementing CI/CD pipelines): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Correct. Managed issuance and renewal for the endpoint. In this case: Cloud KMS wraps the object, and Certificate Manager issues the certificates.
- **B:** Correct. A managed key that wraps the data. In this case: Cloud KMS wraps the object, and Certificate Manager issues the certificates.
- **C:** Incorrect for this question. A store for versioned application parameters. Why the correct answer wins: Cloud KMS wraps the object, and Certificate Manager issues the certificates.
- **D:** Incorrect for this question. A secret readable by everyone with repository access. Why the correct answer wins: Cloud KMS wraps the object, and Certificate Manager issues the certificates.
- **E:** Incorrect for this question. A managed store with immutable versions and audit. Why the correct answer wins: Cloud KMS wraps the object, and Certificate Manager issues the certificates.

### Question 38 — B

Answer: Store the credential in Secret Manager with versions. Secret Manager versions the token and serves the newest version. A managed store with immutable versions and audit. Local study-map skill 2.9 (Key Management), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 2 (building and implementing CI/CD pipelines): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A value left visible in the build history. Why the correct answer wins: Secret Manager versions the token and serves the newest version.
- **B:** Correct. A managed store with immutable versions and audit. In this case: Secret Manager versions the token and serves the newest version.
- **C:** Incorrect for this question. A store for versioned application parameters. Why the correct answer wins: Secret Manager versions the token and serves the newest version.
- **D:** Incorrect for this question. A managed key that wraps the data. Why the correct answer wins: Secret Manager versions the token and serves the newest version.

### Question 39 — D

Answer: Keep the non-secret configuration in Parameter Manager. Parameter Manager supplies the value at deploy time. A store for versioned application parameters. Local study-map skill 2.10 (Configuration and Secret Management), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 2 (building and implementing CI/CD pipelines): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. One image per environment with the settings compiled in. Why the correct answer wins: Parameter Manager supplies the value at deploy time.
- **B:** Incorrect for this question. A managed store with immutable versions and audit. Why the correct answer wins: Parameter Manager supplies the value at deploy time.
- **C:** Incorrect for this question. A secret readable by everyone with repository access. Why the correct answer wins: Parameter Manager supplies the value at deploy time.
- **D:** Correct. A store for versioned application parameters. In this case: Parameter Manager supplies the value at deploy time.

### Question 40 — A

Answer: Bake the environment settings into the image. Baking configuration into the image forces one image per environment. One image per environment with the settings compiled in. Local study-map skill 2.10 (Configuration and Secret Management), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 2 (building and implementing CI/CD pipelines): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Correct. One image per environment with the settings compiled in. In this case: Baking configuration into the image forces one image per environment.
- **B:** Incorrect for this question. A secret readable by everyone with repository access. Why the correct answer wins: Baking configuration into the image forces one image per environment.
- **C:** Incorrect for this question. A managed store with immutable versions and audit. Why the correct answer wins: Baking configuration into the image forces one image per environment.
- **D:** Incorrect for this question. A store for versioned application parameters. Why the correct answer wins: Baking configuration into the image forces one image per environment.

### Question 41 — B

Answer: Inject the secret at build time into the image layer. Anyone who pulls the layer can extract the credential. A secret baked into an artifact anyone can pull. Local study-map skill 2.11 (Build-Time versus Runtime Secret Injection), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 2 (building and implementing CI/CD pipelines): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A credential read only when the workload starts. Why the correct answer wins: Anyone who pulls the layer can extract the credential.
- **B:** Correct. A secret baked into an artifact anyone can pull. In this case: Anyone who pulls the layer can extract the credential.
- **C:** Incorrect for this question. A value left visible in the build history. Why the correct answer wins: Anyone who pulls the layer can extract the credential.
- **D:** Incorrect for this question. A secret readable by everyone with repository access. Why the correct answer wins: Anyone who pulls the layer can extract the credential.

### Question 42 — C, D

Answers: Enable Artifact Analysis scanning on the repository; Fail the pipeline on a critical vulnerability finding. Artifact Analysis produces the findings, and the gate blocks promotion. Vulnerability findings for the stored artifacts. A policy that blocks the promotion. Local study-map skill 2.12 (Vulnerability Scanning and Artifact Analysis), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 2 (building and implementing CI/CD pipelines): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A finding that no pipeline blocks on. Why the correct answer wins: Artifact Analysis produces the findings, and the gate blocks promotion.
- **B:** Incorrect for this question. An identity that cannot promote outside its environment. Why the correct answer wins: Artifact Analysis produces the findings, and the gate blocks promotion.
- **C:** Correct. Vulnerability findings for the stored artifacts. In this case: Artifact Analysis produces the findings, and the gate blocks promotion.
- **D:** Correct. A policy that blocks the promotion. In this case: Artifact Analysis produces the findings, and the gate blocks promotion.
- **E:** Incorrect for this question. An admission check that only attested images may run. Why the correct answer wins: Artifact Analysis produces the findings, and the gate blocks promotion.

### Question 43 — C

Answer: Enforce Binary Authorization attestations before deploy. Binary Authorization admits only attested images. An admission check that only attested images may run. Local study-map skill 2.13 (Supply Chain Security and Binary Authorization), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 2 (building and implementing CI/CD pipelines): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. An identity that cannot promote outside its environment. Why the correct answer wins: Binary Authorization admits only attested images.
- **B:** Incorrect for this question. A policy that blocks the promotion. Why the correct answer wins: Binary Authorization admits only attested images.
- **C:** Correct. An admission check that only attested images may run. In this case: Binary Authorization admits only attested images.
- **D:** Incorrect for this question. Vulnerability findings for the stored artifacts. Why the correct answer wins: Binary Authorization admits only attested images.

### Question 44 — A

Answer: Use one identity with deploy rights in every environment. A single broad identity gives staging a path into production. A single broad credential across the whole estate. Local study-map skill 2.13 (Supply Chain Security and Binary Authorization), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 2 (building and implementing CI/CD pipelines): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Correct. A single broad credential across the whole estate. In this case: A single broad identity gives staging a path into production.
- **B:** Incorrect for this question. A long-lived credential stored outside the platform. Why the correct answer wins: A single broad identity gives staging a path into production.
- **C:** Incorrect for this question. A build identity with broad write access. Why the correct answer wins: A single broad identity gives staging a path into production.
- **D:** Incorrect for this question. An identity that cannot promote outside its environment. Why the correct answer wins: A single broad identity gives staging a path into production.

### Question 45 — A

Answer: Bind deploy permissions only inside the production project. One identity per environment bounds the deploy rights. An identity that cannot promote outside its environment. Local study-map skill 2.14 (Per-Environment IAM Policy), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 2 (building and implementing CI/CD pipelines): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Correct. An identity that cannot promote outside its environment. In this case: One identity per environment bounds the deploy rights.
- **B:** Incorrect for this question. A long-lived credential stored outside the platform. Why the correct answer wins: One identity per environment bounds the deploy rights.
- **C:** Incorrect for this question. A build identity with broad write access. Why the correct answer wins: One identity per environment bounds the deploy rights.
- **D:** Incorrect for this question. A single broad credential across the whole estate. Why the correct answer wins: One identity per environment bounds the deploy rights.

### Question 46 — A, C

Answers: Set an internal target on that indicator; Publish a contractual promise with a remedy. The SLO guides the team, and the SLA promises the customer. An objective the team commits to without a contract. An external commitment that carries a consequence. Local study-map skill 3.1 (SLIs, SLOs, and SLAs), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 3 (applying site reliability engineering practices): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Correct. An external commitment that carries a consequence. In this case: The SLO guides the team, and the SLA promises the customer.
- **B:** Incorrect for this question. A signal that the budget is going too quickly. Why the correct answer wins: The SLO guides the team, and the SLA promises the customer.
- **C:** Correct. An objective the team commits to without a contract. In this case: The SLO guides the team, and the SLA promises the customer.
- **D:** Incorrect for this question. An owned entry with its tier and dependencies. Why the correct answer wins: The SLO guides the team, and the SLA promises the customer.
- **E:** Incorrect for this question. A measured indicator of how the service behaves. Why the correct answer wins: The SLO guides the team, and the SLA promises the customer.

### Question 47 — D

Answer: Track the ratio of good requests to total requests. An SLI defines the measured threshold for a good request. A measured indicator of how the service behaves. Local study-map skill 3.1 (SLIs, SLOs, and SLAs), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 3 (applying site reliability engineering practices): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A uniform promise that most services do not need. Why the correct answer wins: An SLI defines the measured threshold for a good request.
- **B:** Incorrect for this question. An external commitment that carries a consequence. Why the correct answer wins: An SLI defines the measured threshold for a good request.
- **C:** Incorrect for this question. An objective the team commits to without a contract. Why the correct answer wins: An SLI defines the measured threshold for a good request.
- **D:** Correct. A measured indicator of how the service behaves. In this case: An SLI defines the measured threshold for a good request.

### Question 48 — A

Answer: Publish a contractual promise with a remedy. That written promise belongs in the service level agreement. An external commitment that carries a consequence. Local study-map skill 3.1 (SLIs, SLOs, and SLAs), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 3 (applying site reliability engineering practices): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Correct. An external commitment that carries a consequence. In this case: That written promise belongs in the service level agreement.
- **B:** Incorrect for this question. A measured indicator of how the service behaves. Why the correct answer wins: That written promise belongs in the service level agreement.
- **C:** Incorrect for this question. An explicit trade between reliability and change. Why the correct answer wins: That written promise belongs in the service level agreement.
- **D:** Incorrect for this question. An objective the team commits to without a contract. Why the correct answer wins: That written promise belongs in the service level agreement.

### Question 49 — A

Answer: Alert on a fast error-budget burn rate. A burn-rate alert fires when the budget is consumed quickly. A signal that the budget is going too quickly. Local study-map skill 3.2 (Error Budgets), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 3 (applying site reliability engineering practices): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Correct. A signal that the budget is going too quickly. In this case: A burn-rate alert fires when the budget is consumed quickly.
- **B:** Incorrect for this question. A static threshold on a resource metric. Why the correct answer wins: A burn-rate alert fires when the budget is consumed quickly.
- **C:** Incorrect for this question. An external commitment that carries a consequence. Why the correct answer wins: A burn-rate alert fires when the budget is consumed quickly.
- **D:** Incorrect for this question. A rule that trades velocity for reliability. Why the correct answer wins: A burn-rate alert fires when the budget is consumed quickly.

### Question 50 — C

Answer: Stop feature releases when the error budget is spent. The release freeze protects reliability once the budget is gone. A rule that trades velocity for reliability. Local study-map skill 3.2 (Error Budgets), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 3 (applying site reliability engineering practices): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A signal that the budget is going too quickly. Why the correct answer wins: The release freeze protects reliability once the budget is gone.
- **B:** Incorrect for this question. A delivery route for the alert. Why the correct answer wins: The release freeze protects reliability once the budget is gone.
- **C:** Correct. A rule that trades velocity for reliability. In this case: The release freeze protects reliability once the budget is gone.
- **D:** Incorrect for this question. A uniform promise that most services do not need. Why the correct answer wins: The release freeze protects reliability once the budget is gone.

### Question 51 — B

Answer: Assume five nines for every service. Matching every service to five nines overspends on the wrong tier. A uniform promise that most services do not need. Local study-map skill 3.3 (Cost of Reliability and Nines), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 3 (applying site reliability engineering practices): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. An explicit trade between reliability and change. Why the correct answer wins: Matching every service to five nines overspends on the wrong tier.
- **B:** Correct. A uniform promise that most services do not need. In this case: Matching every service to five nines overspends on the wrong tier.
- **C:** Incorrect for this question. Capacity arranged ahead of a known peak. Why the correct answer wins: Matching every service to five nines overspends on the wrong tier.
- **D:** Incorrect for this question. An external commitment that carries a consequence. Why the correct answer wins: Matching every service to five nines overspends on the wrong tier.

### Question 52 — A

Answer: Choose three nines and spend the difference on features. Each additional nine costs more than the benefit it adds. An explicit trade between reliability and change. Local study-map skill 3.3 (Cost of Reliability and Nines), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 3 (applying site reliability engineering practices): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Correct. An explicit trade between reliability and change. In this case: Each additional nine costs more than the benefit it adds.
- **B:** Incorrect for this question. A uniform promise that most services do not need. Why the correct answer wins: Each additional nine costs more than the benefit it adds.
- **C:** Incorrect for this question. An owned entry with its tier and dependencies. Why the correct answer wins: Each additional nine costs more than the benefit it adds.
- **D:** Incorrect for this question. An external commitment that carries a consequence. Why the correct answer wins: Each additional nine costs more than the benefit it adds.

### Question 53 — A

Answer: Leave the unused service running for now. An unowned service keeps costing money until it is retired. An unowned workload that still costs money. Local study-map skill 3.4 (Service Lifecycle Management), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 3 (applying site reliability engineering practices): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Correct. An unowned workload that still costs money. In this case: An unowned service keeps costing money until it is retired.
- **B:** Incorrect for this question. A graceful handover of in-flight requests. Why the correct answer wins: An unowned service keeps costing money until it is retired.
- **C:** Incorrect for this question. A planned withdrawal with a migration path. Why the correct answer wins: An unowned service keeps costing money until it is retired.
- **D:** Incorrect for this question. An owned entry with its tier and dependencies. Why the correct answer wins: An unowned service keeps costing money until it is retired.

### Question 54 — C

Answer: Announce the retirement date and withdraw traffic gradually. A retirement date and traffic withdrawal make the cutover orderly. A planned withdrawal with a migration path. Local study-map skill 3.4 (Service Lifecycle Management), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 3 (applying site reliability engineering practices): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. An unowned workload that still costs money. Why the correct answer wins: A retirement date and traffic withdrawal make the cutover orderly.
- **B:** Incorrect for this question. Extra supply in a different location. Why the correct answer wins: A retirement date and traffic withdrawal make the cutover orderly.
- **C:** Correct. A planned withdrawal with a migration path. In this case: A retirement date and traffic withdrawal make the cutover orderly.
- **D:** Incorrect for this question. An owned entry with its tier and dependencies. Why the correct answer wins: A retirement date and traffic withdrawal make the cutover orderly.

### Question 55 — C, D

Answers: Request a quota increase and reserve capacity before the launch; Schedule the batch with Dynamic Workload Scheduler. A quota increase secures the resource, and the scheduler picks the hour. Capacity arranged ahead of a known peak. A flexible placement into a cheaper window. Local study-map skill 3.5 (Capacity Planning and Quotas), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 3 (applying site reliability engineering practices): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Calendar-driven capacity with no feedback loop. Why the correct answer wins: A quota increase secures the resource, and the scheduler picks the hour.
- **B:** Incorrect for this question. Limits that throttle at the worst possible moment. Why the correct answer wins: A quota increase secures the resource, and the scheduler picks the hour.
- **C:** Correct. A flexible placement into a cheaper window. In this case: A quota increase secures the resource, and the scheduler picks the hour.
- **D:** Correct. Capacity arranged ahead of a known peak. In this case: A quota increase secures the resource, and the scheduler picks the hour.
- **E:** Incorrect for this question. Managed instance scaling from a resource metric. Why the correct answer wins: A quota increase secures the resource, and the scheduler picks the hour.

### Question 56 — A

Answer: Assume the default quota will absorb the launch. Default quotas rarely match a sudden production launch. Limits that throttle at the worst possible moment. Local study-map skill 3.5 (Capacity Planning and Quotas), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 3 (applying site reliability engineering practices): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Correct. Limits that throttle at the worst possible moment. In this case: Default quotas rarely match a sudden production launch.
- **B:** Incorrect for this question. Calendar-driven capacity with no feedback loop. Why the correct answer wins: Default quotas rarely match a sudden production launch.
- **C:** Incorrect for this question. A flexible placement into a cheaper window. Why the correct answer wins: Default quotas rarely match a sudden production launch.
- **D:** Incorrect for this question. Capacity arranged ahead of a known peak. Why the correct answer wins: Default quotas rarely match a sudden production launch.

### Question 57 — C

Answer: Scale on queue depth with a horizontal pod autoscaler. Queue depth reflects the work waiting for a worker. Replica scaling driven by a work signal. Local study-map skill 3.6 (Autoscaling), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 3 (applying site reliability engineering practices): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Calendar-driven capacity with no feedback loop. Why the correct answer wins: Queue depth reflects the work waiting for a worker.
- **B:** Incorrect for this question. Managed instance scaling from a resource metric. Why the correct answer wins: Queue depth reflects the work waiting for a worker.
- **C:** Correct. Replica scaling driven by a work signal. In this case: Queue depth reflects the work waiting for a worker.
- **D:** Incorrect for this question. Concurrency-based replica scaling. Why the correct answer wins: Queue depth reflects the work waiting for a worker.

### Question 58 — A

Answer: Set Cloud Run concurrency so replicas follow load. Concurrency per instance decides when another instance starts. Concurrency-based replica scaling. Local study-map skill 3.6 (Autoscaling), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 3 (applying site reliability engineering practices): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Correct. Concurrency-based replica scaling. In this case: Concurrency per instance decides when another instance starts.
- **B:** Incorrect for this question. Replica scaling driven by a work signal. Why the correct answer wins: Concurrency per instance decides when another instance starts.
- **C:** Incorrect for this question. Managed instance scaling from a resource metric. Why the correct answer wins: Concurrency per instance decides when another instance starts.
- **D:** Incorrect for this question. Calendar-driven capacity with no feedback loop. Why the correct answer wins: Concurrency per instance decides when another instance starts.

### Question 59 — B

Answer: Shift traffic with a DNS routing policy. A routing policy changes which region the name returns. A name-level redirect to a healthy region. Local study-map skill 3.7 (Traffic Draining and Redirection), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 3 (applying site reliability engineering practices): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A graceful handover of in-flight requests. Why the correct answer wins: A routing policy changes which region the name returns.
- **B:** Correct. A name-level redirect to a healthy region. In this case: A routing policy changes which region the name returns.
- **C:** Incorrect for this question. A health-checked switch between backends. Why the correct answer wins: A routing policy changes which region the name returns.
- **D:** Incorrect for this question. Extra supply in a different location. Why the correct answer wins: A routing policy changes which region the name returns.

### Question 60 — B

Answer: Drain connections before removing the instance. Draining lets in-flight requests finish before removal. A graceful handover of in-flight requests. Local study-map skill 3.7 (Traffic Draining and Redirection), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 3 (applying site reliability engineering practices): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Extra supply in a different location. Why the correct answer wins: Draining lets in-flight requests finish before removal.
- **B:** Correct. A graceful handover of in-flight requests. In this case: Draining lets in-flight requests finish before removal.
- **C:** Incorrect for this question. A name-level redirect to a healthy region. Why the correct answer wins: Draining lets in-flight requests finish before removal.
- **D:** Incorrect for this question. A health-checked switch between backends. Why the correct answer wins: Draining lets in-flight requests finish before removal.

### Question 61 — D

Answer: Add capacity in a second region. Extra capacity elsewhere absorbs the excess demand. Extra supply in a different location. Local study-map skill 3.8 (Incident Capacity), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 3 (applying site reliability engineering practices): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A health-checked switch between backends. Why the correct answer wins: Extra capacity elsewhere absorbs the excess demand.
- **B:** Incorrect for this question. A graceful handover of in-flight requests. Why the correct answer wins: Extra capacity elsewhere absorbs the excess demand.
- **C:** Incorrect for this question. Capacity arranged ahead of a known peak. Why the correct answer wins: Extra capacity elsewhere absorbs the excess demand.
- **D:** Correct. Extra supply in a different location. In this case: Extra capacity elsewhere absorbs the excess demand.

### Question 62 — A, B

Answers: Redeploy the previous image to the affected service; Reverse the schema change with a tested down migration. Redeploying the prior image restores the build, and the down migration reverses the schema. A known good artifact restored in place. A paired migration that can be undone. Local study-map skill 3.9 (Rollback Strategies), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 3 (applying site reliability engineering practices): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Correct. A known good artifact restored in place. In this case: Redeploying the prior image restores the build, and the down migration reverses the schema.
- **B:** Correct. A paired migration that can be undone. In this case: Redeploying the prior image restores the build, and the down migration reverses the schema.
- **C:** Incorrect for this question. No action while users are still failing. Why the correct answer wins: Redeploying the prior image restores the build, and the down migration reverses the schema.
- **D:** Incorrect for this question. The step output that names the failing command. Why the correct answer wins: Redeploying the prior image restores the build, and the down migration reverses the schema.
- **E:** Incorrect for this question. An untracked change to the live environment. Why the correct answer wins: Redeploying the prior image restores the build, and the down migration reverses the schema.

### Question 63 — B

Answer: Wait for the error rate to settle on its own. Waiting lets users keep failing while the cause persists. No action while users are still failing. Local study-map skill 3.9 (Rollback Strategies), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 3 (applying site reliability engineering practices): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A paired migration that can be undone. Why the correct answer wins: Waiting lets users keep failing while the cause persists.
- **B:** Correct. No action while users are still failing. In this case: Waiting lets users keep failing while the cause persists.
- **C:** Incorrect for this question. A known good artifact restored in place. Why the correct answer wins: Waiting lets users keep failing while the cause persists.
- **D:** Incorrect for this question. An untracked change to the live environment. Why the correct answer wins: Waiting lets users keep failing while the cause persists.

### Question 64 — B, E

Answers: Enable Data Access audit logs for the service; Install the Ops Agent on the instances. Data Access audit logs record reads, and the Ops Agent collects host metrics. A record of reads and writes on the resource. A collector that ships logs and metrics from the VM. Local study-map skill 4.1 (Log Collection and Ingestion), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 4 (implementing observability practices and troubleshooting): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A vendor-neutral pipeline for traces and metrics. Why the correct answer wins: Data Access audit logs record reads, and the Ops Agent collects host metrics.
- **B:** Correct. A record of reads and writes on the resource. In this case: Data Access audit logs record reads, and the Ops Agent collects host metrics.
- **C:** Incorrect for this question. Per-connection records of accepted and denied traffic. Why the correct answer wins: Data Access audit logs record reads, and the Ops Agent collects host metrics.
- **D:** Incorrect for this question. Request metrics emitted by the sidecar proxies. Why the correct answer wins: Data Access audit logs record reads, and the Ops Agent collects host metrics.
- **E:** Correct. A collector that ships logs and metrics from the VM. In this case: Data Access audit logs record reads, and the Ops Agent collects host metrics.

### Question 65 — C

Answer: Read the Cloud Service Mesh telemetry. Mesh telemetry reports per-request service behaviour. Request metrics emitted by the sidecar proxies. Local study-map skill 4.1 (Log Collection and Ingestion), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 4 (implementing observability practices and troubleshooting): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A record of reads and writes on the resource. Why the correct answer wins: Mesh telemetry reports per-request service behaviour.
- **B:** Incorrect for this question. Per-connection records of accepted and denied traffic. Why the correct answer wins: Mesh telemetry reports per-request service behaviour.
- **C:** Correct. Request metrics emitted by the sidecar proxies. In this case: Mesh telemetry reports per-request service behaviour.
- **D:** Incorrect for this question. A vendor-neutral pipeline for traces and metrics. Why the correct answer wins: Mesh telemetry reports per-request service behaviour.

### Question 66 — A

Answer: Sample the high-volume debug entries. Sampling keeps a fraction while errors stay visible. A fraction kept for diagnosis at lower cost. Local study-map skill 4.2 (Log Optimization and Cost), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 4 (implementing observability practices and troubleshooting): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Correct. A fraction kept for diagnosis at lower cost. In this case: Sampling keeps a fraction while errors stay visible.
- **B:** Incorrect for this question. A filter that drops matching entries before storage. Why the correct answer wins: Sampling keeps a fraction while errors stay visible.
- **C:** Incorrect for this question. A label removal that cuts the stored series. Why the correct answer wins: Sampling keeps a fraction while errors stay visible.
- **D:** Incorrect for this question. A cost estimate driven by actual ingest. Why the correct answer wins: Sampling keeps a fraction while errors stay visible.

### Question 67 — A

Answer: Add an exclusion for the health-check entries. An exclusion filter drops those entries at the bucket. A filter that drops matching entries before storage. Local study-map skill 4.2 (Log Optimization and Cost), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 4 (implementing observability practices and troubleshooting): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Correct. A filter that drops matching entries before storage. In this case: An exclusion filter drops those entries at the bucket.
- **B:** Incorrect for this question. A sink suited to cheap long-term retention. Why the correct answer wins: An exclusion filter drops those entries at the bucket.
- **C:** Incorrect for this question. A fraction kept for diagnosis at lower cost. Why the correct answer wins: An exclusion filter drops those entries at the bucket.
- **D:** Incorrect for this question. A label removal that cuts the stored series. Why the correct answer wins: An exclusion filter drops those entries at the bucket.

### Question 68 — B, D

Answers: Filter with the Logging query language on the resource label; Open the Logs Explorer and pivot from the error entry. The query language isolates the service, and pivoting shows the neighbours. A precise query over the stored entries. An interactive view with field filters. Local study-map skill 4.3 (Logs Explorer and Query Language), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 4 (implementing observability practices and troubleshooting): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A probe that exercises the path from outside. Why the correct answer wins: The query language isolates the service, and pivoting shows the neighbours.
- **B:** Correct. A precise query over the stored entries. In this case: The query language isolates the service, and pivoting shows the neighbours.
- **C:** Incorrect for this question. A counter derived from matching entries. Why the correct answer wins: The query language isolates the service, and pivoting shows the neighbours.
- **D:** Correct. An interactive view with field filters. In this case: The query language isolates the service, and pivoting shows the neighbours.
- **E:** Incorrect for this question. A sink that lands logs in a queryable table. Why the correct answer wins: The query language isolates the service, and pivoting shows the neighbours.

### Question 69 — A

Answer: Create a log-based metric for the error string. A log-based metric turns matching entries into a counter. A counter derived from matching entries. Local study-map skill 4.3 (Logs Explorer and Query Language), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 4 (implementing observability practices and troubleshooting): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Correct. A counter derived from matching entries. In this case: A log-based metric turns matching entries into a counter.
- **B:** Incorrect for this question. A measurement written by the application itself. Why the correct answer wins: A log-based metric turns matching entries into a counter.
- **C:** Incorrect for this question. An interactive view with field filters. Why the correct answer wins: A log-based metric turns matching entries into a counter.
- **D:** Incorrect for this question. A precise query over the stored entries. Why the correct answer wins: A log-based metric turns matching entries into a counter.

### Question 70 — D

Answer: Route the entries to a Cloud Storage bucket. A Cloud Storage sink is the cheapest long retention. A sink suited to cheap long-term retention. Local study-map skill 4.4 (Log Export and Retention), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 4 (implementing observability practices and troubleshooting): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A sink that lands logs in a queryable table. Why the correct answer wins: A Cloud Storage sink is the cheapest long retention.
- **B:** Incorrect for this question. A sink that streams entries to another consumer. Why the correct answer wins: A Cloud Storage sink is the cheapest long retention.
- **C:** Incorrect for this question. A retention period that cannot be shortened. Why the correct answer wins: A Cloud Storage sink is the cheapest long retention.
- **D:** Correct. A sink suited to cheap long-term retention. In this case: A Cloud Storage sink is the cheapest long retention.

### Question 71 — D

Answer: Route the entries to a Pub/Sub topic. A Pub/Sub sink streams the entries to the consumer. A sink that streams entries to another consumer. Local study-map skill 4.4 (Log Export and Retention), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 4 (implementing observability practices and troubleshooting): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A sink suited to cheap long-term retention. Why the correct answer wins: A Pub/Sub sink streams the entries to the consumer.
- **B:** Incorrect for this question. A sink that lands logs in a queryable table. Why the correct answer wins: A Pub/Sub sink streams the entries to the consumer.
- **C:** Incorrect for this question. A retention period that cannot be shortened. Why the correct answer wins: A Pub/Sub sink streams the entries to the consumer.
- **D:** Correct. A sink that streams entries to another consumer. In this case: A Pub/Sub sink streams the entries to the consumer.

### Question 72 — C

Answer: Redact the email field with a log processor. A processor redacts the fields on the way into the bucket. A transform that removes the value before storage. Local study-map skill 4.5 (Sensitive Data Redaction), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 4 (implementing observability practices and troubleshooting): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A procedural promise with no enforcement. Why the correct answer wins: A processor redacts the fields on the way into the bucket.
- **B:** Incorrect for this question. A sink suited to cheap long-term retention. Why the correct answer wins: A processor redacts the fields on the way into the bucket.
- **C:** Correct. A transform that removes the value before storage. In this case: A processor redacts the fields on the way into the bucket.
- **D:** Incorrect for this question. A fraction kept for diagnosis at lower cost. Why the correct answer wins: A processor redacts the fields on the way into the bucket.

### Question 73 — C

Answer: Ask Gemini Cloud Assist to explain the metric spike. Gemini Cloud Assist interprets the metric chart for the reviewer. An AI interpretation of the chart. Local study-map skill 4.6 (Gemini Cloud Assist for Log Analysis), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 4 (implementing observability practices and troubleshooting): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. An AI summary over the selected log range. Why the correct answer wins: Gemini Cloud Assist interprets the metric chart for the reviewer.
- **B:** Incorrect for this question. A precise query over the stored entries. Why the correct answer wins: Gemini Cloud Assist interprets the metric chart for the reviewer.
- **C:** Correct. An AI interpretation of the chart. In this case: Gemini Cloud Assist interprets the metric chart for the reviewer.
- **D:** Incorrect for this question. An AI pointer to the expensive span. Why the correct answer wins: Gemini Cloud Assist interprets the metric chart for the reviewer.

### Question 74 — B, D

Answers: Install the Ops Agent on the instances; Read the Cloud Service Mesh telemetry. The Ops Agent covers the VMs, and mesh telemetry covers the requests. A collector that ships logs and metrics from the VM. Request metrics emitted by the sidecar proxies. Local study-map skill 4.7 (Metrics Collection), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 4 (implementing observability practices and troubleshooting): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Per-connection records of accepted and denied traffic. Why the correct answer wins: The Ops Agent covers the VMs, and mesh telemetry covers the requests.
- **B:** Correct. A collector that ships logs and metrics from the VM. In this case: The Ops Agent covers the VMs, and mesh telemetry covers the requests.
- **C:** Incorrect for this question. A record of reads and writes on the resource. Why the correct answer wins: The Ops Agent covers the VMs, and mesh telemetry covers the requests.
- **D:** Correct. Request metrics emitted by the sidecar proxies. In this case: The Ops Agent covers the VMs, and mesh telemetry covers the requests.
- **E:** Incorrect for this question. A vendor-neutral pipeline for traces and metrics. Why the correct answer wins: The Ops Agent covers the VMs, and mesh telemetry covers the requests.

### Question 75 — C

Answer: Run an OpenTelemetry Collector in the cluster. The OpenTelemetry Collector fans out to both backends. A vendor-neutral pipeline for traces and metrics. Local study-map skill 4.7 (Metrics Collection), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 4 (implementing observability practices and troubleshooting): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A measurement written by the application itself. Why the correct answer wins: The OpenTelemetry Collector fans out to both backends.
- **B:** Incorrect for this question. Request metrics emitted by the sidecar proxies. Why the correct answer wins: The OpenTelemetry Collector fans out to both backends.
- **C:** Correct. A vendor-neutral pipeline for traces and metrics. In this case: The OpenTelemetry Collector fans out to both backends.
- **D:** Incorrect for this question. A collector that ships logs and metrics from the VM. Why the correct answer wins: The OpenTelemetry Collector fans out to both backends.

### Question 76 — A

Answer: Emit a custom metric for the business event. The application emits a custom metric with that timing. A measurement written by the application itself. Local study-map skill 4.8 (Custom and Log-Based Metrics), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 4 (implementing observability practices and troubleshooting): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Correct. A measurement written by the application itself. In this case: The application emits a custom metric with that timing.
- **B:** Incorrect for this question. A metrics store fed by a scrape endpoint. Why the correct answer wins: The application emits a custom metric with that timing.
- **C:** Incorrect for this question. A probe that exercises the path from outside. Why the correct answer wins: The application emits a custom metric with that timing.
- **D:** Incorrect for this question. A counter derived from matching entries. Why the correct answer wins: The application emits a custom metric with that timing.

### Question 77 — D

Answer: Create an uptime check against the login flow. An uptime check probes the redirect path from outside. A probe that exercises the path from outside. Local study-map skill 4.9 (Synthetic Monitors), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 4 (implementing observability practices and troubleshooting): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A measurement written by the application itself. Why the correct answer wins: An uptime check probes the redirect path from outside.
- **B:** Incorrect for this question. A metrics store fed by a scrape endpoint. Why the correct answer wins: An uptime check probes the redirect path from outside.
- **C:** Incorrect for this question. A counter derived from matching entries. Why the correct answer wins: An uptime check probes the redirect path from outside.
- **D:** Correct. A probe that exercises the path from outside. In this case: An uptime check probes the redirect path from outside.

### Question 78 — C

Answer: Build one dashboard and share it with the on-call rotation. A curated dashboard gathers the signals for one service. A shared view of the signals that matter. Local study-map skill 4.10 (Metrics Explorer and Dashboards), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 4 (implementing observability practices and troubleshooting): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A documented response beside the notification. Why the correct answer wins: A curated dashboard gathers the signals for one service.
- **B:** Incorrect for this question. A static threshold on a resource metric. Why the correct answer wins: A curated dashboard gathers the signals for one service.
- **C:** Correct. A shared view of the signals that matter. In this case: A curated dashboard gathers the signals for one service.
- **D:** Incorrect for this question. A third-party paging integration. Why the correct answer wins: A curated dashboard gathers the signals for one service.

### Question 79 — C

Answer: Attach the remediation playbook to the alert. The playbook tells the responder what to attempt. A documented response beside the notification. Local study-map skill 4.10 (Metrics Explorer and Dashboards), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 4 (implementing observability practices and troubleshooting): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A shared view of the signals that matter. Why the correct answer wins: The playbook tells the responder what to attempt.
- **B:** Incorrect for this question. A delivery route for the alert. Why the correct answer wins: The playbook tells the responder what to attempt.
- **C:** Correct. A documented response beside the notification. In this case: The playbook tells the responder what to attempt.
- **D:** Incorrect for this question. A page driven by the objective instead of a raw threshold. Why the correct answer wins: The playbook tells the responder what to attempt.

### Question 80 — B, E

Answers: Create an alerting policy on the SLO burn rate; Alert when CPU stays above ninety percent for ten minutes. The burn-rate policy pages on user impact, and CPU warns of saturation. A page driven by the objective instead of a raw threshold. A static threshold on a resource metric. Local study-map skill 4.11 (Alerting Policies), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 4 (implementing observability practices and troubleshooting): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A documented response beside the notification. Why the correct answer wins: The burn-rate policy pages on user impact, and CPU warns of saturation.
- **B:** Correct. A page driven by the objective instead of a raw threshold. In this case: The burn-rate policy pages on user impact, and CPU warns of saturation.
- **C:** Incorrect for this question. A third-party paging integration. Why the correct answer wins: The burn-rate policy pages on user impact, and CPU warns of saturation.
- **D:** Incorrect for this question. A delivery route for the alert. Why the correct answer wins: The burn-rate policy pages on user impact, and CPU warns of saturation.
- **E:** Correct. A static threshold on a resource metric. In this case: The burn-rate policy pages on user impact, and CPU warns of saturation.

### Question 81 — D

Answer: Send the alert to PagerDuty through a webhook. A webhook sends the alert into that incident tool. A third-party paging integration. Local study-map skill 4.11 (Alerting Policies), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 4 (implementing observability practices and troubleshooting): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A documented response beside the notification. Why the correct answer wins: A webhook sends the alert into that incident tool.
- **B:** Incorrect for this question. A page driven by the objective instead of a raw threshold. Why the correct answer wins: A webhook sends the alert into that incident tool.
- **C:** Incorrect for this question. A delivery route for the alert. Why the correct answer wins: A webhook sends the alert into that incident tool.
- **D:** Correct. A third-party paging integration. In this case: A webhook sends the alert into that incident tool.

### Question 82 — B

Answer: Add an email notification channel for the on-call group. An email channel copies each alert to the audit mailbox. A delivery route for the alert. Local study-map skill 4.12 (Third-Party Alerting Integration), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 4 (implementing observability practices and troubleshooting): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A static threshold on a resource metric. Why the correct answer wins: An email channel copies each alert to the audit mailbox.
- **B:** Correct. A delivery route for the alert. In this case: An email channel copies each alert to the audit mailbox.
- **C:** Incorrect for this question. A documented response beside the notification. Why the correct answer wins: An email channel copies each alert to the audit mailbox.
- **D:** Incorrect for this question. A third-party paging integration. Why the correct answer wins: An email channel copies each alert to the audit mailbox.

### Question 83 — A

Answer: Instrument the service with OpenTelemetry spans. OpenTelemetry spans record the timing of each call. Trace context emitted for each request. Local study-map skill 4.13 (Distributed Tracing with OpenTelemetry), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 4 (implementing observability practices and troubleshooting): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Correct. Trace context emitted for each request. In this case: OpenTelemetry spans record the timing of each call.
- **B:** Incorrect for this question. A per-span timing view of one request. Why the correct answer wins: OpenTelemetry spans record the timing of each call.
- **C:** Incorrect for this question. An AI pointer to the expensive span. Why the correct answer wins: OpenTelemetry spans record the timing of each call.
- **D:** Incorrect for this question. A join key between traces and logs. Why the correct answer wins: OpenTelemetry spans record the timing of each call.

### Question 84 — D

Answer: Log a timestamp and correlate by eye later. Two clocks drift, so the timestamps cannot reliably join. No shared identifier between the two signals. Local study-map skill 4.13 (Distributed Tracing with OpenTelemetry), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 4 (implementing observability practices and troubleshooting): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A join key between traces and logs. Why the correct answer wins: Two clocks drift, so the timestamps cannot reliably join.
- **B:** Incorrect for this question. Trace context emitted for each request. Why the correct answer wins: Two clocks drift, so the timestamps cannot reliably join.
- **C:** Incorrect for this question. A per-span timing view of one request. Why the correct answer wins: Two clocks drift, so the timestamps cannot reliably join.
- **D:** Correct. No shared identifier between the two signals. In this case: Two clocks drift, so the timestamps cannot reliably join.

### Question 85 — B

Answer: Put the trace ID in the structured log line. The trace ID in the log makes that join possible. A join key between traces and logs. Local study-map skill 4.14 (Trace Analysis and Log Correlation), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 4 (implementing observability practices and troubleshooting): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Trace context emitted for each request. Why the correct answer wins: The trace ID in the log makes that join possible.
- **B:** Correct. A join key between traces and logs. In this case: The trace ID in the log makes that join possible.
- **C:** Incorrect for this question. No shared identifier between the two signals. Why the correct answer wins: The trace ID in the log makes that join possible.
- **D:** Incorrect for this question. A per-span timing view of one request. Why the correct answer wins: The trace ID in the log makes that join possible.

### Question 86 — D

Answer: Read the firewall rule that hit the denied flow. A firewall rule missing for the new range blocks the probe. The rule that blocked the connection. Local study-map skill 4.15 (Infrastructure and Pipeline Troubleshooting), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 4 (implementing observability practices and troubleshooting): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. The identity the node uses to fetch the image. Why the correct answer wins: A firewall rule missing for the new range blocks the probe.
- **B:** Incorrect for this question. A stale name that still points at the old address. Why the correct answer wins: A firewall rule missing for the new range blocks the probe.
- **C:** Incorrect for this question. A shared egress resource that runs out of ports. Why the correct answer wins: A firewall rule missing for the new range blocks the probe.
- **D:** Correct. The rule that blocked the connection. In this case: A firewall rule missing for the new range blocks the probe.

### Question 87 — B

Answer: Profile the slow endpoint inside the application. Profiling finds the slow code on the request path. A hotspot found on the request path. Local study-map skill 4.16 (Application and Latency Troubleshooting), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 4 (implementing observability practices and troubleshooting): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A stale name that still points at the old address. Why the correct answer wins: Profiling finds the slow code on the request path.
- **B:** Correct. A hotspot found on the request path. In this case: Profiling finds the slow code on the request path.
- **C:** Incorrect for this question. A shared egress resource that runs out of ports. Why the correct answer wins: Profiling finds the slow code on the request path.
- **D:** Incorrect for this question. A probe that fails before the app is listening. Why the correct answer wins: Profiling finds the slow code on the request path.

### Question 88 — C

Answer: Check the DNS record and its remaining TTL. Cached DNS answers live until the record TTL expires. A stale name that still points at the old address. Local study-map skill 4.16 (Application and Latency Troubleshooting), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 4 (implementing observability practices and troubleshooting): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. The rule that blocked the connection. Why the correct answer wins: Cached DNS answers live until the record TTL expires.
- **B:** Incorrect for this question. A shared egress resource that runs out of ports. Why the correct answer wins: Cached DNS answers live until the record TTL expires.
- **C:** Correct. A stale name that still points at the old address. In this case: Cached DNS answers live until the record TTL expires.
- **D:** Incorrect for this question. A hotspot found on the request path. Why the correct answer wins: Cached DNS answers live until the record TTL expires.

### Question 89 — D

Answer: Measure request latency by endpoint in Cloud Monitoring. Per-endpoint latency shows which request path slowed down. An application-level view of response time. Local study-map skill 5.1 (Application Performance Monitoring), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 5 (optimizing performance and cost): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A queryable record of spend by label. Why the correct answer wins: Per-endpoint latency shows which request path slowed down.
- **B:** Incorrect for this question. A pool sized against measured demand. Why the correct answer wins: Per-endpoint latency shows which request path slowed down.
- **C:** Incorrect for this question. A goal-oriented view of performance. Why the correct answer wins: Per-endpoint latency shows which request path slowed down.
- **D:** Correct. An application-level view of response time. In this case: Per-endpoint latency shows which request path slowed down.

### Question 90 — D

Answer: Track the service objective on a shared dashboard. An objective dashboard puts the goal beside current performance. A goal-oriented view of performance. Local study-map skill 5.1 (Application Performance Monitoring), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 5 (optimizing performance and cost): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A recommendation aimed at spend. Why the correct answer wins: An objective dashboard puts the goal beside current performance.
- **B:** Incorrect for this question. A cost estimate driven by actual ingest. Why the correct answer wins: An objective dashboard puts the goal beside current performance.
- **C:** Incorrect for this question. An application-level view of response time. Why the correct answer wins: An objective dashboard puts the goal beside current performance.
- **D:** Correct. A goal-oriented view of performance. In this case: An objective dashboard puts the goal beside current performance.

### Question 91 — D

Answer: Review the Active Assist recommendations for the project. Active Assist lists the recommendations already generated. Suggested changes generated from telemetry. Local study-map skill 5.2 (Active Assist and Recommenders), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 5 (optimizing performance and cost): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A recommendation aimed at resilience. Why the correct answer wins: Active Assist lists the recommendations already generated.
- **B:** Incorrect for this question. A recommendation aimed at spend. Why the correct answer wins: Active Assist lists the recommendations already generated.
- **C:** Incorrect for this question. A queryable record of spend by label. Why the correct answer wins: Active Assist lists the recommendations already generated.
- **D:** Correct. Suggested changes generated from telemetry. In this case: Active Assist lists the recommendations already generated.

### Question 92 — D

Answer: Apply the cost recommender suggestion for the idle disks. The cost recommender flags the unattached disks. A recommendation aimed at spend. Local study-map skill 5.2 (Active Assist and Recommenders), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 5 (optimizing performance and cost): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Suggested changes generated from telemetry. Why the correct answer wins: The cost recommender flags the unattached disks.
- **B:** Incorrect for this question. A recommendation aimed at resilience. Why the correct answer wins: The cost recommender flags the unattached disks.
- **C:** Incorrect for this question. Discounted capacity that can be reclaimed. Why the correct answer wins: The cost recommender flags the unattached disks.
- **D:** Correct. A recommendation aimed at spend. In this case: The cost recommender flags the unattached disks.

### Question 93 — D, E

Answers: Measure log volume per service before choosing a retention period; Exclude the debug stream and keep the error stream. Measuring volume sizes the bill, and excluding debug entries cuts it. A cost estimate driven by actual ingest. A reduction that preserves the useful signal. Local study-map skill 5.3 (Observability Cost Management), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 5 (optimizing performance and cost): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A cheaper egress path with different performance. Why the correct answer wins: Measuring volume sizes the bill, and excluding debug entries cuts it.
- **B:** Incorrect for this question. A label removal that cuts the stored series. Why the correct answer wins: Measuring volume sizes the bill, and excluding debug entries cuts it.
- **C:** Incorrect for this question. A retention period that cannot be shortened. Why the correct answer wins: Measuring volume sizes the bill, and excluding debug entries cuts it.
- **D:** Correct. A reduction that preserves the useful signal. In this case: Measuring volume sizes the bill, and excluding debug entries cuts it.
- **E:** Correct. A cost estimate driven by actual ingest. In this case: Measuring volume sizes the bill, and excluding debug entries cuts it.

### Question 94 — C

Answer: Drop the high-cardinality user label from the metric. High-cardinality labels multiply the stored series. A label removal that cuts the stored series. Local study-map skill 5.3 (Observability Cost Management), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 5 (optimizing performance and cost): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A cost estimate driven by actual ingest. Why the correct answer wins: High-cardinality labels multiply the stored series.
- **B:** Incorrect for this question. A reduction that preserves the useful signal. Why the correct answer wins: High-cardinality labels multiply the stored series.
- **C:** Correct. A label removal that cuts the stored series. In this case: High-cardinality labels multiply the stored series.
- **D:** Incorrect for this question. A retention period that cannot be shortened. Why the correct answer wins: High-cardinality labels multiply the stored series.

### Question 95 — A

Answer: Run the batch on Spot VMs. Spot capacity suits batch work that can restart. Discounted capacity that can be reclaimed. Local study-map skill 5.4 (Spot Virtual Machines), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 5 (optimizing performance and cost): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Correct. Discounted capacity that can be reclaimed. In this case: Spot capacity suits batch work that can restart.
- **B:** Incorrect for this question. A pool built from reclaimable capacity. Why the correct answer wins: Spot capacity suits batch work that can restart.
- **C:** Incorrect for this question. A multi-year commitment at a lower unit price. Why the correct answer wins: Spot capacity suits batch work that can restart.
- **D:** Incorrect for this question. Reclaimable capacity under a stateful workload. Why the correct answer wins: Spot capacity suits batch work that can restart.

### Question 96 — B

Answer: Move the primary database onto Spot capacity. Reclaimable capacity evicts state that was never durable. Reclaimable capacity under a stateful workload. Local study-map skill 5.4 (Spot Virtual Machines), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 5 (optimizing performance and cost): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A pool built from reclaimable capacity. Why the correct answer wins: Reclaimable capacity evicts state that was never durable.
- **B:** Correct. Reclaimable capacity under a stateful workload. In this case: Reclaimable capacity evicts state that was never durable.
- **C:** Incorrect for this question. Discounted capacity that can be reclaimed. Why the correct answer wins: Reclaimable capacity evicts state that was never durable.
- **D:** Incorrect for this question. A multi-year commitment at a lower unit price. Why the correct answer wins: Reclaimable capacity evicts state that was never durable.

### Question 97 — B

Answer: Buy a committed-use discount for the steady baseline. A commitment trades flexibility for a lower unit price. A multi-year commitment at a lower unit price. Local study-map skill 5.5 (Infrastructure Cost Planning), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 5 (optimizing performance and cost): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. An automatic discount that accrues with monthly use. Why the correct answer wins: A commitment trades flexibility for a lower unit price.
- **B:** Correct. A multi-year commitment at a lower unit price. In this case: A commitment trades flexibility for a lower unit price.
- **C:** Incorrect for this question. Discounted capacity that can be reclaimed. Why the correct answer wins: A commitment trades flexibility for a lower unit price.
- **D:** Incorrect for this question. A cheaper egress path with different performance. Why the correct answer wins: A commitment trades flexibility for a lower unit price.

### Question 98 — B

Answer: Serve the bulk export over the Standard network tier. The standard tier is cheaper for bulk transfers. A cheaper egress path with different performance. Local study-map skill 5.5 (Infrastructure Cost Planning), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 5 (optimizing performance and cost): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A multi-year commitment at a lower unit price. Why the correct answer wins: The standard tier is cheaper for bulk transfers.
- **B:** Correct. A cheaper egress path with different performance. In this case: The standard tier is cheaper for bulk transfers.
- **C:** Incorrect for this question. A lower-latency path for user-facing traffic. Why the correct answer wins: The standard tier is cheaper for bulk transfers.
- **D:** Incorrect for this question. A pool built from reclaimable capacity. Why the correct answer wins: The standard tier is cheaper for bulk transfers.

### Question 99 — A, B

Answers: Right-size the node pool from the observed requests; Keep the minimum instance count at zero for the internal tool. Right-sizing removes the reservation, and a minimum of zero ends idle billing. A pool sized against measured demand. Scale to zero for a service nobody uses at night. Local study-map skill 5.6 (Workload-Level Cost Optimization), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 5 (optimizing performance and cost): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Correct. A pool sized against measured demand. In this case: Right-sizing removes the reservation, and a minimum of zero ends idle billing.
- **B:** Correct. Scale to zero for a service nobody uses at night. In this case: Right-sizing removes the reservation, and a minimum of zero ends idle billing.
- **C:** Incorrect for this question. A calendar action that removes idle spend. Why the correct answer wins: Right-sizing removes the reservation, and a minimum of zero ends idle billing.
- **D:** Incorrect for this question. Reclaimable capacity under a stateful workload. Why the correct answer wins: Right-sizing removes the reservation, and a minimum of zero ends idle billing.
- **E:** Incorrect for this question. Warm capacity that avoids cold starts. Why the correct answer wins: Right-sizing removes the reservation, and a minimum of zero ends idle billing.

### Question 100 — C

Answer: Stop the idle non-production instances on a schedule. Scheduling the stop removes the weekend spend. A calendar action that removes idle spend. Local study-map skill 5.6 (Workload-Level Cost Optimization), mapped to the official guide: Google Cloud Professional Cloud DevOps Engineer exam guide (five sections, retrieved October 2026). Primary reference: Professional Cloud DevOps Engineer exam guide section 5 (optimizing performance and cost): https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Scale to zero for a service nobody uses at night. Why the correct answer wins: Scheduling the stop removes the weekend spend.
- **B:** Incorrect for this question. A multi-year commitment at a lower unit price. Why the correct answer wins: Scheduling the stop removes the weekend spend.
- **C:** Correct. A calendar action that removes idle spend. In this case: Scheduling the stop removes the weekend spend.
- **D:** Incorrect for this question. A pool sized against measured demand. Why the correct answer wins: Scheduling the stop removes the weekend spend.
