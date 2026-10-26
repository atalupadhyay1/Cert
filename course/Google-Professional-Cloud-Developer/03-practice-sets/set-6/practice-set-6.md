# Google Cloud Professional Cloud Developer — Full-Length Mock Exam 6

Professional Cloud Developer · 100 questions · expanded practice bank · passing score not published

Blueprint-weighted mock exam. Item mix: 84 multiple-choice and 16 multiple-select items (the selection count is stated in each multi-select stem). The live exam publishes 50-60 multiple-choice and multiple-select questions and has no case-study component, so this set is larger on purpose and no case-study item is reproduced. The live paper allows two hours for 50-60 items, so this 100-item set is a slower-per-item rehearsal: about 72 seconds per item here against roughly 120-144 seconds live. Use it to build a habit of finishing with time to review. See the README for the exact fidelity boundary.

Original educational content, not actual, recalled, or copied Google exam items.

## Questions

---

## Domain 1 — Designing Highly Scalable, Secure, and Reliable Cloud-Native Applications (Compute Choice, APIs, and Secure Design)

### 1. A logistics team needs a containerised HTTP API and a tiny handler that reacts to a queue event. Which two platforms fit? Select two.

- A. Deploy to App Engine standard
- B. Deploy the handler as a Cloud Functions function
- C. Deploy the workload to Google Kubernetes Engine
- D. Run the application on Compute Engine instances
- E. Deploy the service to Cloud Run

### 2. An inherited application depends on the platform's memcache and task queue interfaces. Which platform fits?

- A. Deploy the workload to Google Kubernetes Engine
- B. Run the application on Compute Engine instances
- C. Deploy the service to Cloud Run
- D. Deploy to App Engine standard

### 3. A vendor appliance is delivered only as a bootable virtual machine image. Which platform fits?

- A. Deploy the workload to Google Kubernetes Engine
- B. Deploy the service to Cloud Run
- C. Run the application on Compute Engine instances
- D. Deploy to App Engine standard

### 4. A Perl monolith cannot be built by the platform's buildpacks and already ships an image. What should be deployed?

- A. Deploy from source and let the platform build it
- B. Deploy to App Engine standard
- C. Package the monolith into a container image
- D. Deploy the handler as a Cloud Functions function

### 5. An SLA promises service through the loss of a complete region with a stated recovery objective. Which design fits?

- A. Place the workload in a single zone
- B. Deploy in one region across multiple zones
- C. Serve static content from Cloud CDN
- D. Deploy the service in two regions behind a global load balancer

### 6. The disaster plan must survive a zone loss only, and cross-region replication is out of budget. Which design fits?

- A. Deploy the service in two regions behind a global load balancer
- B. Buy committed use discounts for the steady baseline
- C. Place the workload in a single zone
- D. Deploy in one region across multiple zones

### 7. A legacy report generator keeps partial results per instance and cannot be changed yet. What should be enabled?

- A. Use a generated cookie for stickiness
- B. Enable session affinity on the backend service
- C. Store session state in a shared datastore
- D. Serve static content from Cloud CDN

### 8. A service must be runnable in any region at any moment with identical behaviour. What must its state model be?

- A. Cache inside each instance process
- B. Store session state in a shared datastore
- C. Enable session affinity on the backend service
- D. Use a generated cookie for stickiness

### 9. A session store must be shared by two runtimes that both restart often. What should be used?

- A. Cache inside each instance process
- B. Load through a cache-aside pattern
- C. Cache reads in Memorystore
- D. Serve static content from Cloud CDN

### 10. One batch process recomputes the same reference table for every record. What should it add?

- A. Serve static content from Cloud CDN
- B. Load through a cache-aside pattern
- C. Cache reads in Memorystore
- D. Cache inside each instance process

### 11. Internal services already speak the binary protocol, and the browser must call them without a translation proxy. Which two fit? Select two.

- A. Serve gRPC-Web for browser clients
- B. Batch many small calls into one request
- C. Publish an OpenAPI specification
- D. Expose a REST API with JSON payloads
- E. Expose a gRPC service

### 12. An external partner needs a machine-readable contract to generate its own client. What should be published?

- A. Publish an OpenAPI specification
- B. Serve gRPC-Web for browser clients
- C. Expose a REST API with JSON payloads
- D. Expose a gRPC service

### 13. A nightly export client saturates the API for everyone else each evening. What should be added?

- A. Apply a rate limit per client key
- B. Use API Gateway for the API
- C. Introduce a new API version alongside the old one
- D. Set a quota per API key

### 14. An added response field must not break older readers that reject unknown keys. What should the change be?

- A. Publish an OpenAPI specification
- B. Introduce a new API version alongside the old one
- C. Request only the fields the caller needs
- D. Add the field in a backward-compatible way

### 15. A job must be retried after a delay with a stable identifier, and a nightly sweep must start on a clock. Which two fit? Select two.

- A. Publish the event to a Pub/Sub topic
- B. Route the event with Eventarc
- C. Schedule the invocation with Cloud Scheduler
- D. Queue the work as a Cloud Tasks task
- E. Orchestrate the steps in Workflows

### 16. A consumer must hold unacknowledged messages while its downstream is recovering. Which delivery fits?

- A. Have the worker pull from the subscription
- B. Route the event with Eventarc
- C. Deliver to an HTTPS push subscription
- D. Queue the work as a Cloud Tasks task

### 17. Requests were copied from another team and reserve eight times the measured peak. What should be changed?

- A. Buy committed use discounts for the steady baseline
- B. Set CPU and memory requests from measured use
- C. Raise the container limits above the observed peak
- D. Cap the maximum instance count

### 18. A JVM reserves more heap than the pod's limit allows and dies during start-up. What should be changed?

- A. Raise the container limits above the observed peak
- B. Set a namespace resource quota
- C. Set CPU and memory requests from measured use
- D. Run the batch node pool on Spot VMs

### 19. The release process must move traffic in steps and must be able to return to the previous revision at once. Which two fit? Select two.

- A. Canary the release at a small percentage first
- B. Route by revision tag or header
- C. Shift traffic back to the previous revision
- D. Split traffic between revisions by percentage
- E. Gate the change behind a feature flag

### 20. A beta capability must be visible to a named cohort without another deployment. What should be used?

- A. Gate the change behind a feature flag
- B. Canary the release at a small percentage first
- C. Route by revision tag or header
- D. Split traffic between revisions by percentage

### 21. An approval step must pause the process until a human responds and then continue. What fits?

- A. Schedule the invocation with Cloud Scheduler
- B. Use Cloud Service Mesh for service-to-service traffic
- C. Queue the work as a Cloud Tasks task
- D. Orchestrate the steps in Workflows

### 22. Staging exports accumulate forever and only the last week is useful. What should be configured?

- A. Lock the bucket retention policy
- B. Make the bucket public
- C. Add a lifecycle rule to the bucket
- D. Issue a signed URL with a short expiry

### 23. A bad rotation must be reverted to the previous value within minutes. What should hold the credential?

- A. Set the credential as an environment variable
- B. Store the credential in Secret Manager
- C. Mount the secret as a volume
- D. Download a service account key file

### 24. A customer contract requires that their own key protects the stored payloads. What should be configured?

- A. Download a service account key file
- B. Store the credential in Secret Manager
- C. Encrypt with a Cloud KMS key
- D. Use a customer-managed encryption key

### 25. External customers need passwordless sign-in with a one-time code. What should be adopted?

- A. Use Identity Platform for end-user sign-in
- B. Validate the signed JWT from the proxy
- C. Rely on Application Default Credentials
- D. Give the workload its own service account

### 26. A replay of an assertion captured earlier must be rejected by the app. What should it validate?

- A. Validate the signed JWT from the proxy
- B. Allow unauthenticated invocations
- C. Rely on Application Default Credentials
- D. Use Identity Platform for end-user sign-in

### 27. Pod-to-pod traffic must be restricted, and no predefined role fits the job's nine permissions. Which two fit? Select two.

- A. Define a custom role for the narrow permission set
- B. Allow unauthenticated invocations
- C. Grant only the roles the workload needs
- D. Grant the basic editor role
- E. Apply a Kubernetes NetworkPolicy

### 28. A task needs to publish to one topic and read nothing else. What should its grant express?

- A. Grant only the roles the workload needs
- B. Define a custom role for the narrow permission set
- C. Give the workload its own service account
- D. Grant the basic editor role

### 29. Reads scan one customer's readings in time order, and writes arrive from millions of meters. What should the key design support?

- A. Cache reads in Memorystore
- B. Store the ledger in Spanner
- C. Design the row key for the read pattern
- D. Use Firestore in Native mode

### 30. Raw video masters must be kept ten years at the lowest storage cost. Where should they live?

- A. Store the objects in Cloud Storage
- B. Store the ledger in Spanner
- C. Use Firestore in Native mode
- D. Design the row key for the read pattern

### 31. A browser must upload a large file straight to a bucket under a temporary grant. What should the service issue?

- A. Add a lifecycle rule to the bucket
- B. Make the bucket public
- C. Lock the bucket retention policy
- D. Issue a signed URL with a short expiry

### 32. A live dashboard needs events within seconds, and a raw event table must be filled without a service. Which two fit? Select two.

- A. Export the batch to BigQuery
- B. Queue the work as a Cloud Tasks task
- C. Store the objects in Cloud Storage
- D. Use a BigQuery subscription on the topic
- E. Stream the events into BigQuery

---

## Domain 2 — Building and Testing Applications (Development Environments, Builds, and Tests)

### 33. A developer must exercise queue behaviour offline, and a locked-down laptop must run commands with no installation. Which two fit? Select two.

- A. Use Cloud Shell for the session
- B. Use Cloud Workstations for the environment
- C. Run the service emulator locally
- D. Inspect the live process with Cloud Debugger
- E. Develop with Cloud Code in the IDE

### 34. A new hire must be productive on day one with exactly the pinned toolchain. What should be provided?

- A. Run the service emulator locally
- B. Develop with Cloud Code in the IDE
- C. Use Cloud Workstations for the environment
- D. Use Cloud Shell for the session

### 35. A reviewer wants to run the test suite from a browser without cloning anything. What fits?

- A. Develop with Cloud Code in the IDE
- B. Use Cloud Workstations for the environment
- C. Use Cloud Shell for the session
- D. Inspect the live process with Cloud Debugger

### 36. An unfamiliar library's error must be explained next to the line that caused it. What fits?

- A. Use an AI coding assistant to draft the tests
- B. Connect the assistant to an MCP server
- C. Ask Gemini Cloud Assist for a diagnosis
- D. Develop with Cloud Code in the IDE

### 37. Twelve endpoint handlers must be drafted for a human to finish. What should be used?

- A. Ask Gemini Cloud Assist for a diagnosis
- B. Connect the assistant to an MCP server
- C. Use an AI coding assistant to draft the tests
- D. Use Cloud Shell for the session

### 38. The assistant must file and read tickets through a documented interface rather than pasted text. What should be exposed?

- A. Develop with Cloud Code in the IDE
- B. Connect the assistant to an MCP server
- C. Use an AI coding assistant to draft the tests
- D. Ask Gemini Cloud Assist for a diagnosis

### 39. The build must be reproducible, and the artefact that passed staging must be the one promoted. Which two fit? Select two.

- A. Deploy a pinned image digest
- B. Iterate with Skaffold
- C. Keep building the image by hand
- D. Build the image with Cloud Build
- E. Deploy from source and let the platform build it

### 40. A merge into the main branch must start a build by itself. What should be configured?

- A. Schedule the invocation with Cloud Scheduler
- B. Keep building the image by hand
- C. Queue the work as a Cloud Tasks task
- D. Trigger the build from a repository push

### 41. A developer iterating against the dev cluster wants the image rebuilt on each save. What fits?

- A. Build the image with Cloud Build
- B. Keep building the image by hand
- C. Deploy a pinned image digest
- D. Iterate with Skaffold

### 42. The built image must be pushed where the runtime's own identity can pull it. What should hold it?

- A. Store the objects in Cloud Storage
- B. Push the image to Container Registry
- C. Use a customer-managed encryption key
- D. Push the image to Artifact Registry

### 43. Staging and production images must be separated so access can differ. What should hold them?

- A. Store the objects in Cloud Storage
- B. Push the image to Artifact Registry
- C. Push the image to Container Registry
- D. Build the image with Cloud Build

### 44. An old CI job still pushes to the previous host name. What must stay available?

- A. Push the image to Container Registry
- B. Build the image with Cloud Build
- C. Store the objects in Cloud Storage
- D. Push the image to Artifact Registry

### 45. Compliance evidence for each release must be kept after the images are pruned. Where should it live?

- A. Push the image to Container Registry
- B. Store the objects in Cloud Storage
- C. Build the image with Cloud Build
- D. Push the image to Artifact Registry

### 46. Admission must require an attestation, and an auditor must see the source revision behind the image. Which two fit? Select two.

- A. Scan the image with Artifact Analysis
- B. Review the finding in Security Command Center
- C. Enforce admission with Binary Authorization
- D. Require a higher supply-chain level before release
- E. Generate build provenance in Cloud Build

### 47. A library CVE must be traced to the images that ship it. What should be used?

- A. Generate build provenance in Cloud Build
- B. Enforce admission with Binary Authorization
- C. Review the finding in Security Command Center
- D. Scan the image with Artifact Analysis

### 48. Image findings must appear beside the project's other security findings. Where should they surface?

- A. Scan the image with Artifact Analysis
- B. Review the finding in Security Command Center
- C. Enforce admission with Binary Authorization
- D. Generate build provenance in Cloud Build

### 49. A date parser's leap-year and month-end branches must each fail by name. What should be added?

- A. Add a unit test with dependencies stubbed
- B. Load-test the release before the rollout
- C. Run an integration test against the emulator
- D. Quarantine the flaky test and fix it

### 50. A test shares a fixture with another test and fails only in the full run. What should be done first?

- A. Run an integration test against the emulator
- B. Quarantine the flaky test and fix it
- C. Block the deploy on the test result
- D. Add a unit test with dependencies stubbed

### 51. A merge must be refused while the suite fails. What should be added?

- A. Run an integration test against the emulator
- B. Load-test the release before the rollout
- C. Block the deploy on the test result
- D. Quarantine the flaky test and fix it

### 52. The real dependency must be exercised, and the check must run inside the pipeline every time. Which two fit? Select two.

- A. Add a unit test with dependencies stubbed
- B. Run an integration test against the emulator
- C. Profile the service with Cloud Profiler
- D. Run the tests as a Cloud Build step
- E. Load-test the release before the rollout

### 53. A queue drains too slowly once volume doubles, and that must be known before launch. What should be run?

- A. Load-test the release before the rollout
- B. Run an integration test against the emulator
- C. Profile the service with Cloud Profiler
- D. Add a unit test with dependencies stubbed

### 54. Under a realistic replay the service is slow, and the team needs the function burning the CPU. What should be used?

- A. Load-test the release before the rollout
- B. Send the exception to Error Reporting
- C. Profile the service with Cloud Profiler
- D. Inspect the live process with Cloud Debugger

### 55. A multi-step scenario fails only after the third call, and the state at that point must be seen. What should be used?

- A. Inspect the live process with Cloud Debugger
- B. Add a unit test with dependencies stubbed
- C. Profile the service with Cloud Profiler
- D. Run an integration test against the emulator

---

## Domain 3 — Configuring Cloud-Native Applications for Deployment (Cloud Run and GKE Deployment Configuration)

### 56. A repository has no Dockerfile, and the morning traffic must never wait for a cold start. Which two settings fit? Select two.

- A. Keep building the image by hand
- B. Cap the maximum instance count
- C. Keep a minimum number of instances warm
- D. Deploy from source and let the platform build it
- E. Package the monolith into a container image

### 57. A marketing campaign once quadrupled the fleet and the bill. What should bound it now?

- A. Raise the container limits above the observed peak
- B. Cap the maximum instance count
- C. Buy committed use discounts for the steady baseline
- D. Keep a minimum number of instances warm

### 58. A .NET service needs longer than its start window to warm up under the default CPU. What should be enabled?

- A. Raise the per-instance concurrency limit
- B. Raise CPU during start-up only
- C. Keep a minimum number of instances warm
- D. Use request-based billing

### 59. A nightly extract must load a warehouse and then hold no capacity. What fits?

- A. Deploy the handler as a Cloud Functions function
- B. Deploy the service to Cloud Run
- C. Route the event with Eventarc
- D. Run the batch work as a Cloud Run job

### 60. A bucket change must reach an HTTPS collector that retries on failure. Which two fit? Select two.

- A. Orchestrate the steps in Workflows
- B. Deliver to an HTTPS push subscription
- C. Route the event with Eventarc
- D. Have the worker pull from the subscription
- E. Schedule the invocation with Cloud Scheduler

### 61. The collector rejects the trigger with permission denied although it serves users fine. What should be granted?

- A. Put Identity-Aware Proxy in front of the service
- B. Grant the invoker role to the calling identity
- C. Allow unauthenticated invocations
- D. Use API Gateway for the API

### 62. The collector's partner allows five calls a second and must not be flooded. What should queue the calls?

- A. Publish the event to a Pub/Sub topic
- B. Schedule the invocation with Cloud Scheduler
- C. Orchestrate the steps in Workflows
- D. Queue the work as a Cloud Tasks task

### 63. An instance must serve hundreds of idle streams without spawning copies. What should be raised?

- A. Raise the per-instance concurrency limit
- B. Enable CPU boost at startup
- C. Cap the maximum instance count
- D. Keep a minimum number of instances warm

### 64. A test environment must never answer a call from the public name. What should be set?

- A. Allow unauthenticated invocations
- B. Put Identity-Aware Proxy in front of the service
- C. Restrict ingress to internal traffic
- D. Put a global external Application Load Balancer in front

### 65. A payment provider posts webhooks without a Google token. What should be allowed?

- A. Put Identity-Aware Proxy in front of the service
- B. Allow unauthenticated invocations
- C. Grant the invoker role to the calling identity
- D. Restrict ingress to internal traffic

### 66. A prototype must cost nothing overnight when idle. What billing behaviour fits?

- A. Use request-based billing
- B. Buy committed use discounts for the steady baseline
- C. Use instance-based billing
- D. Keep a minimum number of instances warm

### 67. Five services need one shared key check declared in configuration only. What fits?

- A. Use API Gateway for the API
- B. Put Apigee in front of the API
- C. Restrict ingress to internal traffic
- D. Put a global external Application Load Balancer in front

### 68. One hostname with a managed certificate must front both regional deployments. What should be added?

- A. Use a regional load balancer
- B. Restrict ingress to internal traffic
- C. Put a global external Application Load Balancer in front
- D. Use API Gateway for the API

### 69. A release must replace pods gradually and never lose more than a fifth at a time. Which two fit? Select two.

- A. Add a PodDisruptionBudget
- B. Constrain pods to the intended node pool
- C. Use a rolling update strategy
- D. Run the batch node pool on Spot VMs
- E. Tune maxSurge and maxUnavailable

### 70. The team has no one to size or patch nodes and wants that handled. Which mode fits?

- A. Enable node pool autoscaling
- B. Use GKE Autopilot for the cluster
- C. Constrain pods to the intended node pool
- D. Run the batch node pool on Spot VMs

### 71. Pods must call a Google Cloud API with no exported key file on the node. What should be used?

- A. Bind a Kubernetes service account to a Google service account
- B. Download a service account key file
- C. Federate the external identity with Workload Identity Federation
- D. Give the workload its own service account

### 72. New pods stay pending because no node has room for them. What should be enabled?

- A. Scale pods on CPU utilization
- B. Add a PodDisruptionBudget
- C. Enable node pool autoscaling
- D. Set a minimum replica count

### 73. A container hangs without exiting, and another needs a long initialisation before any check should fail. Which two probes fit? Select two.

- A. Add a PodDisruptionBudget
- B. Configure a readiness probe
- C. Configure a liveness probe
- D. Add a health check endpoint to the backend service
- E. Configure a startup probe

### 74. A pod keeps taking requests while its dependency check is failing. What should gate the traffic?

- A. Add a PodDisruptionBudget
- B. Configure a startup probe
- C. Configure a readiness probe
- D. Configure a liveness probe

### 75. Draining a node for repair must leave three of the five replicas serving. What should be defined?

- A. Configure a readiness probe
- B. Configure a liveness probe
- C. Add a health check endpoint to the backend service
- D. Add a PodDisruptionBudget

### 76. A CPU-bound encoder must add pods as utilisation climbs. Which signal fits?

- A. Scale pods on CPU utilization
- B. Scale pods on a custom or external metric
- C. Enable node pool autoscaling
- D. Set a minimum replica count

### 77. Scaling must follow the number of messages waiting rather than CPU. What should be used?

- A. Scale pods on CPU utilization
- B. Enable node pool autoscaling
- C. Scale pods on a custom or external metric
- D. Buy committed use discounts for the steady baseline

### 78. A scheduled burst must find two pods already serving before it begins. What should be set?

- A. Scale pods on CPU utilization
- B. Enable node pool autoscaling
- C. Set a minimum replica count
- D. Add a PodDisruptionBudget

### 79. A nightly reconciliation must run on a fixed clock with no engineer involved. What should start it?

- A. Route the event with Eventarc
- B. Queue the work as a Cloud Tasks task
- C. Schedule the invocation with Cloud Scheduler
- D. Orchestrate the steps in Workflows

---

## Domain 4 — Integrating Applications with Google Cloud Services (Data, Messaging, APIs, and Observability)

### 80. The driver itself must handle the connection, and sessions must be reused across requests. Which two fit? Select two.

- A. Connect through the Cloud SQL Auth Proxy
- B. Reach the service through Private Service Connect
- C. Pool and reuse database connections
- D. Use the language connector with IAM
- E. Connect over the database private IP

### 81. An application in a runtime with no connector library must still connect privately. What should run beside it?

- A. Reach the service through Private Service Connect
- B. Connect through the Cloud SQL Auth Proxy
- C. Connect through the AlloyDB Auth Proxy
- D. Use the language connector with IAM

### 82. The cluster's certificates rotate often and clients must not be restarted. What handles the rotation?

- A. Use the language connector with IAM
- B. Connect through the AlloyDB Auth Proxy
- C. Connect over the database private IP
- D. Connect through the Cloud SQL Auth Proxy

### 83. No client, including administrators, may reach the instance over the internet. What should it use?

- A. Use the language connector with IAM
- B. Connect over the database private IP
- C. Expose the database on a public address with enforced SSL
- D. Reach the service through Private Service Connect

### 84. Sessions opened by one tenant must be capped so the shared instance stays available to others. What should be set?

- A. Raise the container limits above the observed peak
- B. Raise the database connection ceiling by flag
- C. Pool and reuse database connections
- D. Reach the service through Private Service Connect

### 85. A shipment event must reach three different teams without the publisher knowing them. What should it publish to?

- A. Queue the work as a Cloud Tasks task
- B. Orchestrate the steps in Workflows
- C. Route the event with Eventarc
- D. Publish the event to a Pub/Sub topic

### 86. A message that always fails must stop being retried and be kept for study. What should be configured?

- A. Have the worker pull from the subscription
- B. Make the handler idempotent with a deduplication key
- C. Add a dead-letter topic
- D. Retry with exponential backoff and jitter

### 87. A redelivered message must not create a second shipment. What should the consumer use?

- A. Make the handler idempotent with a deduplication key
- B. Deliver to an HTTPS push subscription
- C. Retry with exponential backoff and jitter
- D. Add a dead-letter topic

### 88. Raw events must be queryable for years with no consumer service to run. What should be created?

- A. Have the worker pull from the subscription
- B. Use a BigQuery subscription on the topic
- C. Export the batch to BigQuery
- D. Store the objects in Cloud Storage

### 89. A client retries immediately and exhausts its allowance during a short throttle. What should it add?

- A. Set a quota per API key
- B. Raise the container limits above the observed peak
- C. Retry with exponential backoff and jitter
- D. Batch many small calls into one request

### 90. A listing returns the first hundred rows and the client treats them as all. What is missing?

- A. Request only the fields the caller needs
- B. Batch many small calls into one request
- C. Follow the page token until results are exhausted
- D. Cache the response for its freshness window

### 91. Each item is forty kilobytes while the screen shows two values. What should the client request?

- A. Batch many small calls into one request
- B. Follow the page token until results are exhausted
- C. Cache the response for its freshness window
- D. Request only the fields the caller needs

### 92. The same slowly changing catalogue is requested by every handler. What should the client do?

- A. Raise the database connection ceiling by flag
- B. Retry with exponential backoff and jitter
- C. Follow the page token until results are exhausted
- D. Cache the response for its freshness window

### 93. Jobs need their own identities, and an external pipeline must stop storing a key file. Which two fit? Select two.

- A. Give the workload its own service account
- B. Federate the external identity with Workload Identity Federation
- C. Let the workload use the default compute service account
- D. Grant the basic editor role
- E. Download a service account key file

### 94. A developer's container must use the developer's own identity with no key file. What mechanism applies?

- A. Let the workload use the default compute service account
- B. Give the workload its own service account
- C. Rely on Application Default Credentials
- D. Download a service account key file

### 95. Logs must be filterable by tenant and by request identifier. What should the code emit?

- A. Emit structured JSON logs
- B. Build a log-based metric
- C. Set the correct severity on each entry
- D. Send the exception to Error Reporting

### 96. A ratio the business watches is not emitted anywhere today. What should the team add?

- A. Build a log-based metric
- B. Set the correct severity on each entry
- C. Create an alerting policy on the metric
- D. Emit a custom metric from the code

### 97. A threshold on the new metric must notify the on-call rotation. What should be configured?

- A. Emit a custom metric from the code
- B. Create an alerting policy on the metric
- C. Alert on the error budget burn rate
- D. Set the correct severity on each entry

### 98. The team cannot see which exceptions are new after a release. What should be enabled?

- A. Build a log-based metric
- B. Create an alerting policy on the metric
- C. Inspect the live process with Cloud Debugger
- D. Send the exception to Error Reporting

### 99. One request's entries are spread across four services and must join into one view. What should the code do?

- A. Set the correct severity on each entry
- B. Emit structured JSON logs
- C. Inspect the live process with Cloud Debugger
- D. Propagate the trace ID between services

### 100. An engineer wants an alert explained with the likely cause before the bridge call. What should assist?

- A. Use an AI coding assistant to draft the tests
- B. Ask Gemini Cloud Assist for a diagnosis
- C. Connect the assistant to an MCP server
- D. Send the exception to Error Reporting

---

## Answer key and explanations

### Question 1 — B, E

Answers: Deploy the service to Cloud Run; Deploy the handler as a Cloud Functions function. The managed container runtime serves the API, and the function runtime handles the small event handler. A managed container runtime that scales to zero and bills per request while it serves traffic. An event-triggered function runtime for a single-purpose handler rather than a long-lived service. Local study-map skill 1.1 (Compute Platform Selection), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 1 (designing highly scalable, secure, and reliable cloud-native applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A platform runtime that manages scaling for a supported language version and its sandbox limits. Why the correct answer wins: The managed container runtime serves the API, and the function runtime handles the small event handler.
- **B:** Correct. An event-triggered function runtime for a single-purpose handler rather than a long-lived service. In this case: The managed container runtime serves the API, and the function runtime handles the small event handler.
- **C:** Incorrect for this question. A managed Kubernetes control plane where pods, node pools and cluster-scoped policy are yours to configure. Why the correct answer wins: The managed container runtime serves the API, and the function runtime handles the small event handler.
- **D:** Incorrect for this question. Virtual machines where the operating system, runtime and scaling group are all managed by the team. Why the correct answer wins: The managed container runtime serves the API, and the function runtime handles the small event handler.
- **E:** Correct. A managed container runtime that scales to zero and bills per request while it serves traffic. In this case: The managed container runtime serves the API, and the function runtime handles the small event handler.

### Question 2 — D

Answer: Deploy to App Engine standard. The platform runtime keeps those bundled interfaces available. A platform runtime that manages scaling for a supported language version and its sandbox limits. Local study-map skill 1.1 (Compute Platform Selection), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 1 (designing highly scalable, secure, and reliable cloud-native applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A managed Kubernetes control plane where pods, node pools and cluster-scoped policy are yours to configure. Why the correct answer wins: The platform runtime keeps those bundled interfaces available.
- **B:** Incorrect for this question. Virtual machines where the operating system, runtime and scaling group are all managed by the team. Why the correct answer wins: The platform runtime keeps those bundled interfaces available.
- **C:** Incorrect for this question. A managed container runtime that scales to zero and bills per request while it serves traffic. Why the correct answer wins: The platform runtime keeps those bundled interfaces available.
- **D:** Correct. A platform runtime that manages scaling for a supported language version and its sandbox limits. In this case: The platform runtime keeps those bundled interfaces available.

### Question 3 — C

Answer: Run the application on Compute Engine instances. Virtual machines boot the vendor image as delivered. Virtual machines where the operating system, runtime and scaling group are all managed by the team. Local study-map skill 1.1 (Compute Platform Selection), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 1 (designing highly scalable, secure, and reliable cloud-native applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A managed Kubernetes control plane where pods, node pools and cluster-scoped policy are yours to configure. Why the correct answer wins: Virtual machines boot the vendor image as delivered.
- **B:** Incorrect for this question. A managed container runtime that scales to zero and bills per request while it serves traffic. Why the correct answer wins: Virtual machines boot the vendor image as delivered.
- **C:** Correct. Virtual machines where the operating system, runtime and scaling group are all managed by the team. In this case: Virtual machines boot the vendor image as delivered.
- **D:** Incorrect for this question. A platform runtime that manages scaling for a supported language version and its sandbox limits. Why the correct answer wins: Virtual machines boot the vendor image as delivered.

### Question 4 — C

Answer: Package the monolith into a container image. Deploying the existing image avoids the unsupported buildpack. Wrap the existing process in a portable artifact that a managed runtime can execute. Local study-map skill 1.2 (Containerizing and Refactoring Applications), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 1 (designing highly scalable, secure, and reliable cloud-native applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Hand the source to the managed builder instead of shipping an image. Why the correct answer wins: Deploying the existing image avoids the unsupported buildpack.
- **B:** Incorrect for this question. A platform runtime that manages scaling for a supported language version and its sandbox limits. Why the correct answer wins: Deploying the existing image avoids the unsupported buildpack.
- **C:** Correct. Wrap the existing process in a portable artifact that a managed runtime can execute. In this case: Deploying the existing image avoids the unsupported buildpack.
- **D:** Incorrect for this question. An event-triggered function runtime for a single-purpose handler rather than a long-lived service. Why the correct answer wins: Deploying the existing image avoids the unsupported buildpack.

### Question 5 — D

Answer: Deploy the service in two regions behind a global load balancer. Two active regions meet the promise when either region is lost. Serve from two regions so a regional failure leaves capacity elsewhere. Local study-map skill 1.3 (Regional Distribution and Failover), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 1 (designing highly scalable, secure, and reliable cloud-native applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Run in one zone only, so a zone failure stops the service entirely. Why the correct answer wins: Two active regions meet the promise when either region is lost.
- **B:** Incorrect for this question. Spread instances over zones of a single region so a zone failure does not stop the service. Why the correct answer wins: Two active regions meet the promise when either region is lost.
- **C:** Incorrect for this question. Cache responses at the edge so repeated requests never reach the origin. Why the correct answer wins: Two active regions meet the promise when either region is lost.
- **D:** Correct. Serve from two regions so a regional failure leaves capacity elsewhere. In this case: Two active regions meet the promise when either region is lost.

### Question 6 — D

Answer: Deploy in one region across multiple zones. Zones of one region give the zone tolerance at that budget. Spread instances over zones of a single region so a zone failure does not stop the service. Local study-map skill 1.3 (Regional Distribution and Failover), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 1 (designing highly scalable, secure, and reliable cloud-native applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Serve from two regions so a regional failure leaves capacity elsewhere. Why the correct answer wins: Zones of one region give the zone tolerance at that budget.
- **B:** Incorrect for this question. Trade a term commitment for a lower unit price on capacity that never idles. Why the correct answer wins: Zones of one region give the zone tolerance at that budget.
- **C:** Incorrect for this question. Run in one zone only, so a zone failure stops the service entirely. Why the correct answer wins: Zones of one region give the zone tolerance at that budget.
- **D:** Correct. Spread instances over zones of a single region so a zone failure does not stop the service. In this case: Zones of one region give the zone tolerance at that budget.

### Question 7 — B

Answer: Enable session affinity on the backend service. Affinity keeps the generator's partial results on one instance. Pin a client to one backend for the life of its session. Local study-map skill 1.4 (Load Balancing and Session Affinity), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 1 (designing highly scalable, secure, and reliable cloud-native applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Route the client by cookie rather than by address or header. Why the correct answer wins: Affinity keeps the generator's partial results on one instance.
- **B:** Correct. Pin a client to one backend for the life of its session. In this case: Affinity keeps the generator's partial results on one instance.
- **C:** Incorrect for this question. Move the state out of the instance so any instance can serve any request. Why the correct answer wins: Affinity keeps the generator's partial results on one instance.
- **D:** Incorrect for this question. Cache responses at the edge so repeated requests never reach the origin. Why the correct answer wins: Affinity keeps the generator's partial results on one instance.

### Question 8 — B

Answer: Store session state in a shared datastore. Holding no local state lets any region serve any request. Move the state out of the instance so any instance can serve any request. Local study-map skill 1.4 (Load Balancing and Session Affinity), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 1 (designing highly scalable, secure, and reliable cloud-native applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A per-instance cache that is fast but not shared between instances. Why the correct answer wins: Holding no local state lets any region serve any request.
- **B:** Correct. Move the state out of the instance so any instance can serve any request. In this case: Holding no local state lets any region serve any request.
- **C:** Incorrect for this question. Pin a client to one backend for the life of its session. Why the correct answer wins: Holding no local state lets any region serve any request.
- **D:** Incorrect for this question. Route the client by cookie rather than by address or header. Why the correct answer wins: Holding no local state lets any region serve any request.

### Question 9 — C

Answer: Cache reads in Memorystore. A shared in-memory service keeps the sessions across restarts. A managed Redis-compatible cache in front of the system of record. Local study-map skill 1.5 (Caching with Memorystore), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 1 (designing highly scalable, secure, and reliable cloud-native applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A per-instance cache that is fast but not shared between instances. Why the correct answer wins: A shared in-memory service keeps the sessions across restarts.
- **B:** Incorrect for this question. Read the cache, fall back to the database, and populate the cache on a miss. Why the correct answer wins: A shared in-memory service keeps the sessions across restarts.
- **C:** Correct. A managed Redis-compatible cache in front of the system of record. In this case: A shared in-memory service keeps the sessions across restarts.
- **D:** Incorrect for this question. Cache responses at the edge so repeated requests never reach the origin. Why the correct answer wins: A shared in-memory service keeps the sessions across restarts.

### Question 10 — D

Answer: Cache inside each instance process. An in-process cache reuses the table across the records. A per-instance cache that is fast but not shared between instances. Local study-map skill 1.5 (Caching with Memorystore), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 1 (designing highly scalable, secure, and reliable cloud-native applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Cache responses at the edge so repeated requests never reach the origin. Why the correct answer wins: An in-process cache reuses the table across the records.
- **B:** Incorrect for this question. Read the cache, fall back to the database, and populate the cache on a miss. Why the correct answer wins: An in-process cache reuses the table across the records.
- **C:** Incorrect for this question. A managed Redis-compatible cache in front of the system of record. Why the correct answer wins: An in-process cache reuses the table across the records.
- **D:** Correct. A per-instance cache that is fast but not shared between instances. In this case: An in-process cache reuses the table across the records.

### Question 11 — A, E

Answers: Serve gRPC-Web for browser clients; Expose a gRPC service. The binary RPC interface suits the internal calls, and the browser variant carries them without a proxy. A compatibility layer so browser code can call a gRPC service. A binary, schema-driven RPC interface with streaming and generated clients. Local study-map skill 1.6 (API Protocol Choice: REST and gRPC), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 1 (designing highly scalable, secure, and reliable cloud-native applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Correct. A compatibility layer so browser code can call a gRPC service. In this case: The binary RPC interface suits the internal calls, and the browser variant carries them without a proxy.
- **B:** Incorrect for this question. Reduce per-call overhead when the API supports a batch surface. Why the correct answer wins: The binary RPC interface suits the internal calls, and the browser variant carries them without a proxy.
- **C:** Incorrect for this question. A machine-readable contract that generates clients and validates requests. Why the correct answer wins: The binary RPC interface suits the internal calls, and the browser variant carries them without a proxy.
- **D:** Incorrect for this question. A resource-oriented HTTP interface that browsers and simple clients can call. Why the correct answer wins: The binary RPC interface suits the internal calls, and the browser variant carries them without a proxy.
- **E:** Correct. A binary, schema-driven RPC interface with streaming and generated clients. In this case: The binary RPC interface suits the internal calls, and the browser variant carries them without a proxy.

### Question 12 — A

Answer: Publish an OpenAPI specification. Publishing the specification lets the partner generate its client. A machine-readable contract that generates clients and validates requests. Local study-map skill 1.6 (API Protocol Choice: REST and gRPC), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 1 (designing highly scalable, secure, and reliable cloud-native applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Correct. A machine-readable contract that generates clients and validates requests. In this case: Publishing the specification lets the partner generate its client.
- **B:** Incorrect for this question. A compatibility layer so browser code can call a gRPC service. Why the correct answer wins: Publishing the specification lets the partner generate its client.
- **C:** Incorrect for this question. A resource-oriented HTTP interface that browsers and simple clients can call. Why the correct answer wins: Publishing the specification lets the partner generate its client.
- **D:** Incorrect for this question. A binary, schema-driven RPC interface with streaming and generated clients. Why the correct answer wins: Publishing the specification lets the partner generate its client.

### Question 13 — A

Answer: Apply a rate limit per client key. A per-second limit keeps the export client from saturating the API. Reject or queue requests above a threshold so one client cannot exhaust the service. Local study-map skill 1.7 (API Management, Rate Limiting, and Versioning), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 1 (designing highly scalable, secure, and reliable cloud-native applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Correct. Reject or queue requests above a threshold so one client cannot exhaust the service. In this case: A per-second limit keeps the export client from saturating the API.
- **B:** Incorrect for this question. A lighter managed gateway for routing and key-based quota enforcement. Why the correct answer wins: A per-second limit keeps the export client from saturating the API.
- **C:** Incorrect for this question. Keep the old contract working while the new one is adopted. Why the correct answer wins: A per-second limit keeps the export client from saturating the API.
- **D:** Incorrect for this question. Bound how many calls a plan allows in a window. Why the correct answer wins: A per-second limit keeps the export client from saturating the API.

### Question 14 — D

Answer: Add the field in a backward-compatible way. An optional addition keeps older readers parsing the response. Extend the contract so existing clients keep working unchanged. Local study-map skill 1.7 (API Management, Rate Limiting, and Versioning), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 1 (designing highly scalable, secure, and reliable cloud-native applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A machine-readable contract that generates clients and validates requests. Why the correct answer wins: An optional addition keeps older readers parsing the response.
- **B:** Incorrect for this question. Keep the old contract working while the new one is adopted. Why the correct answer wins: An optional addition keeps older readers parsing the response.
- **C:** Incorrect for this question. Trim the response payload so latency and cost follow actual use. Why the correct answer wins: An optional addition keeps older readers parsing the response.
- **D:** Correct. Extend the contract so existing clients keep working unchanged. In this case: An optional addition keeps older readers parsing the response.

### Question 15 — C, D

Answers: Queue the work as a Cloud Tasks task; Schedule the invocation with Cloud Scheduler. The task queue holds the delayed retry under one identifier, and the scheduler starts the nightly sweep. A task queue with retries and rate control aimed at a specific target. A cron-style trigger that calls a target on a fixed timetable. Local study-map skill 1.8 (Asynchronous and Event-Driven Integration), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 1 (designing highly scalable, secure, and reliable cloud-native applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A durable, at-least-once message channel with independent subscribers. Why the correct answer wins: The task queue holds the delayed retry under one identifier, and the scheduler starts the nightly sweep.
- **B:** Incorrect for this question. A trigger path that turns a Cloud Audit Log or resource event into a delivery. Why the correct answer wins: The task queue holds the delayed retry under one identifier, and the scheduler starts the nightly sweep.
- **C:** Correct. A cron-style trigger that calls a target on a fixed timetable. In this case: The task queue holds the delayed retry under one identifier, and the scheduler starts the nightly sweep.
- **D:** Correct. A task queue with retries and rate control aimed at a specific target. In this case: The task queue holds the delayed retry under one identifier, and the scheduler starts the nightly sweep.
- **E:** Incorrect for this question. A stateful sequence of service calls with retries and error branches. Why the correct answer wins: The task queue holds the delayed retry under one identifier, and the scheduler starts the nightly sweep.

### Question 16 — A

Answer: Have the worker pull from the subscription. Pull delivery leaves the messages unacknowledged until the consumer is ready. The consumer controls the pace and acknowledges messages itself. Local study-map skill 1.8 (Asynchronous and Event-Driven Integration), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 1 (designing highly scalable, secure, and reliable cloud-native applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Correct. The consumer controls the pace and acknowledges messages itself. In this case: Pull delivery leaves the messages unacknowledged until the consumer is ready.
- **B:** Incorrect for this question. A trigger path that turns a Cloud Audit Log or resource event into a delivery. Why the correct answer wins: Pull delivery leaves the messages unacknowledged until the consumer is ready.
- **C:** Incorrect for this question. Push each message to an endpoint instead of having the consumer pull. Why the correct answer wins: Pull delivery leaves the messages unacknowledged until the consumer is ready.
- **D:** Incorrect for this question. A task queue with retries and rate control aimed at a specific target. Why the correct answer wins: Pull delivery leaves the messages unacknowledged until the consumer is ready.

### Question 17 — B

Answer: Set CPU and memory requests from measured use. Sizing from the measured peak stops the over-reservation. Give the scheduler real numbers so placement and scaling decisions are not guesses. Local study-map skill 1.9 (Resource Requirements and Cost Optimization), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 1 (designing highly scalable, secure, and reliable cloud-native applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Trade a term commitment for a lower unit price on capacity that never idles. Why the correct answer wins: Sizing from the measured peak stops the over-reservation.
- **B:** Correct. Give the scheduler real numbers so placement and scaling decisions are not guesses. In this case: Sizing from the measured peak stops the over-reservation.
- **C:** Incorrect for this question. Allow the process the headroom it needs so it is not throttled or killed. Why the correct answer wins: Sizing from the measured peak stops the over-reservation.
- **D:** Incorrect for this question. Bound the blast radius and the bill at the cost of queueing when the cap is reached. Why the correct answer wins: Sizing from the measured peak stops the over-reservation.

### Question 18 — A

Answer: Raise the container limits above the observed peak. Raising the limit above what the runtime reserves lets it start. Allow the process the headroom it needs so it is not throttled or killed. Local study-map skill 1.9 (Resource Requirements and Cost Optimization), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 1 (designing highly scalable, secure, and reliable cloud-native applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Correct. Allow the process the headroom it needs so it is not throttled or killed. In this case: Raising the limit above what the runtime reserves lets it start.
- **B:** Incorrect for this question. Bound the total capacity a namespace may consume. Why the correct answer wins: Raising the limit above what the runtime reserves lets it start.
- **C:** Incorrect for this question. Give the scheduler real numbers so placement and scaling decisions are not guesses. Why the correct answer wins: Raising the limit above what the runtime reserves lets it start.
- **D:** Incorrect for this question. Use reclaimable capacity for work that can tolerate a node disappearing. Why the correct answer wins: Raising the limit above what the runtime reserves lets it start.

### Question 19 — C, D

Answers: Split traffic between revisions by percentage; Shift traffic back to the previous revision. Weighted routing moves traffic in steps, and the previous revision is kept for an immediate return. Send a fraction of requests to the new revision while the old one still serves the rest. Return all traffic to the known-good revision when the new one misbehaves. Local study-map skill 1.10 (Traffic Splitting and Gradual Rollout), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 1 (designing highly scalable, secure, and reliable cloud-native applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Expose the new version to a slice of traffic before widening it. Why the correct answer wins: Weighted routing moves traffic in steps, and the previous revision is kept for an immediate return.
- **B:** Incorrect for this question. Send only tagged requests to the new revision for internal testing. Why the correct answer wins: Weighted routing moves traffic in steps, and the previous revision is kept for an immediate return.
- **C:** Correct. Return all traffic to the known-good revision when the new one misbehaves. In this case: Weighted routing moves traffic in steps, and the previous revision is kept for an immediate return.
- **D:** Correct. Send a fraction of requests to the new revision while the old one still serves the rest. In this case: Weighted routing moves traffic in steps, and the previous revision is kept for an immediate return.
- **E:** Incorrect for this question. Ship the code dark and enable it per cohort without a redeploy. Why the correct answer wins: Weighted routing moves traffic in steps, and the previous revision is kept for an immediate return.

### Question 20 — A

Answer: Gate the change behind a feature flag. A flag exposes the capability to the cohort that was named. Ship the code dark and enable it per cohort without a redeploy. Local study-map skill 1.10 (Traffic Splitting and Gradual Rollout), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 1 (designing highly scalable, secure, and reliable cloud-native applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Correct. Ship the code dark and enable it per cohort without a redeploy. In this case: A flag exposes the capability to the cohort that was named.
- **B:** Incorrect for this question. Expose the new version to a slice of traffic before widening it. Why the correct answer wins: A flag exposes the capability to the cohort that was named.
- **C:** Incorrect for this question. Send only tagged requests to the new revision for internal testing. Why the correct answer wins: A flag exposes the capability to the cohort that was named.
- **D:** Incorrect for this question. Send a fraction of requests to the new revision while the old one still serves the rest. Why the correct answer wins: A flag exposes the capability to the cohort that was named.

### Question 21 — D

Answer: Orchestrate the steps in Workflows. A stateful orchestration can wait on the human response and continue. A stateful sequence of service calls with retries and error branches. Local study-map skill 1.11 (Orchestrating Services), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 1 (designing highly scalable, secure, and reliable cloud-native applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A cron-style trigger that calls a target on a fixed timetable. Why the correct answer wins: A stateful orchestration can wait on the human response and continue.
- **B:** Incorrect for this question. Mutual TLS, retries and traffic policy applied without changing application code. Why the correct answer wins: A stateful orchestration can wait on the human response and continue.
- **C:** Incorrect for this question. A task queue with retries and rate control aimed at a specific target. Why the correct answer wins: A stateful orchestration can wait on the human response and continue.
- **D:** Correct. A stateful sequence of service calls with retries and error branches. In this case: A stateful orchestration can wait on the human response and continue.

### Question 22 — C

Answer: Add a lifecycle rule to the bucket. A lifecycle rule removes the exports once they are a week old. Transition or delete objects by age so retention happens without a job. Local study-map skill 1.12 (Data Retention and Organization Policy), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 1 (designing highly scalable, secure, and reliable cloud-native applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Make the retention period impossible to shorten, even by an owner. Why the correct answer wins: A lifecycle rule removes the exports once they are a week old.
- **B:** Incorrect for this question. Serve every object to anyone, which removes the need to authorize at all. Why the correct answer wins: A lifecycle rule removes the exports once they are a week old.
- **C:** Correct. Transition or delete objects by age so retention happens without a job. In this case: A lifecycle rule removes the exports once they are a week old.
- **D:** Incorrect for this question. A time-limited grant to one object without exposing credentials. Why the correct answer wins: A lifecycle rule removes the exports once they are a week old.

### Question 23 — B

Answer: Store the credential in Secret Manager. A versioned secret store allows the previous version to be restored. A managed secret store with versioning and access audit. Local study-map skill 1.13 (Secrets, Keys, and Credential Rotation), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 1 (designing highly scalable, secure, and reliable cloud-native applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Inject the value into the process environment at start-up. Why the correct answer wins: A versioned secret store allows the previous version to be restored.
- **B:** Correct. A managed secret store with versioning and access audit. In this case: A versioned secret store allows the previous version to be restored.
- **C:** Incorrect for this question. Present the value as a file that the process reads at runtime. Why the correct answer wins: A versioned secret store allows the previous version to be restored.
- **D:** Incorrect for this question. A long-lived credential that has to be stored and rotated by hand. Why the correct answer wins: A versioned secret store allows the previous version to be restored.

### Question 24 — D

Answer: Use a customer-managed encryption key. A customer-supplied key protects the payloads under their control. A key the customer owns, rotates and can disable. Local study-map skill 1.13 (Secrets, Keys, and Credential Rotation), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 1 (designing highly scalable, secure, and reliable cloud-native applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A long-lived credential that has to be stored and rotated by hand. Why the correct answer wins: A customer-supplied key protects the payloads under their control.
- **B:** Incorrect for this question. A managed secret store with versioning and access audit. Why the correct answer wins: A customer-supplied key protects the payloads under their control.
- **C:** Incorrect for this question. A managed key whose use is authorized by IAM and recorded in audit logs. Why the correct answer wins: A customer-supplied key protects the payloads under their control.
- **D:** Correct. A key the customer owns, rotates and can disable. In this case: A customer-supplied key protects the payloads under their control.

### Question 25 — A

Answer: Use Identity Platform for end-user sign-in. A managed identity service supports passwordless sign-in for customers. A managed identity service for customer accounts and tokens. Local study-map skill 1.14 (Application Authentication), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 1 (designing highly scalable, secure, and reliable cloud-native applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Correct. A managed identity service for customer accounts and tokens. In this case: A managed identity service supports passwordless sign-in for customers.
- **B:** Incorrect for this question. Check the assertion the proxy adds so only proxied requests are trusted. Why the correct answer wins: A managed identity service supports passwordless sign-in for customers.
- **C:** Incorrect for this question. Let the client library find credentials from the environment. Why the correct answer wins: A managed identity service supports passwordless sign-in for customers.
- **D:** Incorrect for this question. A dedicated identity whose roles can be granted and revoked independently. Why the correct answer wins: A managed identity service supports passwordless sign-in for customers.

### Question 26 — A

Answer: Validate the signed JWT from the proxy. Checking the assertion's expiry and audience rejects the replay. Check the assertion the proxy adds so only proxied requests are trusted. Local study-map skill 1.14 (Application Authentication), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 1 (designing highly scalable, secure, and reliable cloud-native applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Correct. Check the assertion the proxy adds so only proxied requests are trusted. In this case: Checking the assertion's expiry and audience rejects the replay.
- **B:** Incorrect for this question. Let anyone reach the endpoint, which is only appropriate for public content. Why the correct answer wins: Checking the assertion's expiry and audience rejects the replay.
- **C:** Incorrect for this question. Let the client library find credentials from the environment. Why the correct answer wins: Checking the assertion's expiry and audience rejects the replay.
- **D:** Incorrect for this question. A managed identity service for customer accounts and tokens. Why the correct answer wins: Checking the assertion's expiry and audience rejects the replay.

### Question 27 — A, E

Answers: Apply a Kubernetes NetworkPolicy; Define a custom role for the narrow permission set. A network policy restricts which pods may talk, and a custom role names exactly those permissions. Restrict which pods may talk to which pods inside the cluster. A role built from an explicit permission list. Local study-map skill 1.15 (Least Privilege and Service-to-Service Security), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 1 (designing highly scalable, secure, and reliable cloud-native applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Correct. A role built from an explicit permission list. In this case: A network policy restricts which pods may talk, and a custom role names exactly those permissions.
- **B:** Incorrect for this question. Let anyone reach the endpoint, which is only appropriate for public content. Why the correct answer wins: A network policy restricts which pods may talk, and a custom role names exactly those permissions.
- **C:** Incorrect for this question. Scope permissions to the actions in use rather than the whole service. Why the correct answer wins: A network policy restricts which pods may talk, and a custom role names exactly those permissions.
- **D:** Incorrect for this question. A legacy broad role that can change most resources in the project. Why the correct answer wins: A network policy restricts which pods may talk, and a custom role names exactly those permissions.
- **E:** Correct. Restrict which pods may talk to which pods inside the cluster. In this case: A network policy restricts which pods may talk, and a custom role names exactly those permissions.

### Question 28 — A

Answer: Grant only the roles the workload needs. Granting only that publish expresses what the task actually needs. Scope permissions to the actions in use rather than the whole service. Local study-map skill 1.15 (Least Privilege and Service-to-Service Security), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 1 (designing highly scalable, secure, and reliable cloud-native applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Correct. Scope permissions to the actions in use rather than the whole service. In this case: Granting only that publish expresses what the task actually needs.
- **B:** Incorrect for this question. A role built from an explicit permission list. Why the correct answer wins: Granting only that publish expresses what the task actually needs.
- **C:** Incorrect for this question. A dedicated identity whose roles can be granted and revoked independently. Why the correct answer wins: Granting only that publish expresses what the task actually needs.
- **D:** Incorrect for this question. A legacy broad role that can change most resources in the project. Why the correct answer wins: Granting only that publish expresses what the task actually needs.

### Question 29 — C

Answer: Design the row key for the read pattern. A key starting with the customer makes that ordered scan cheap. Order the key so the query becomes a contiguous range scan. Local study-map skill 1.16 (Storage and Schema Selection), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 1 (designing highly scalable, secure, and reliable cloud-native applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A managed Redis-compatible cache in front of the system of record. Why the correct answer wins: A key starting with the customer makes that ordered scan cheap.
- **B:** Incorrect for this question. A relational database with strongly consistent multi-region transactions. Why the correct answer wins: A key starting with the customer makes that ordered scan cheap.
- **C:** Correct. Order the key so the query becomes a contiguous range scan. In this case: A key starting with the customer makes that ordered scan cheap.
- **D:** Incorrect for this question. A document store with real-time listeners and mobile SDKs. Why the correct answer wins: A key starting with the customer makes that ordered scan cheap.

### Question 30 — A

Answer: Store the objects in Cloud Storage. Object storage with cold classes holds large masters cheaply. Durable object storage addressed by name rather than a database row. Local study-map skill 1.16 (Storage and Schema Selection), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 1 (designing highly scalable, secure, and reliable cloud-native applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Correct. Durable object storage addressed by name rather than a database row. In this case: Object storage with cold classes holds large masters cheaply.
- **B:** Incorrect for this question. A relational database with strongly consistent multi-region transactions. Why the correct answer wins: Object storage with cold classes holds large masters cheaply.
- **C:** Incorrect for this question. A document store with real-time listeners and mobile SDKs. Why the correct answer wins: Object storage with cold classes holds large masters cheaply.
- **D:** Incorrect for this question. Order the key so the query becomes a contiguous range scan. Why the correct answer wins: Object storage with cold classes holds large masters cheaply.

### Question 31 — D

Answer: Issue a signed URL with a short expiry. A signed upload URL grants that one upload for a short time. A time-limited grant to one object without exposing credentials. Local study-map skill 1.17 (Signed URLs and Time-Limited Access), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 1 (designing highly scalable, secure, and reliable cloud-native applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Transition or delete objects by age so retention happens without a job. Why the correct answer wins: A signed upload URL grants that one upload for a short time.
- **B:** Incorrect for this question. Serve every object to anyone, which removes the need to authorize at all. Why the correct answer wins: A signed upload URL grants that one upload for a short time.
- **C:** Incorrect for this question. Make the retention period impossible to shorten, even by an owner. Why the correct answer wins: A signed upload URL grants that one upload for a short time.
- **D:** Correct. A time-limited grant to one object without exposing credentials. In this case: A signed upload URL grants that one upload for a short time.

### Question 32 — D, E

Answers: Stream the events into BigQuery; Use a BigQuery subscription on the topic. Streaming the events feeds the dashboard, and a subscription writing to the table fills it with no service. Land analytics rows in the warehouse for SQL and ML use. Write topic messages straight into a table without a consumer. Local study-map skill 1.18 (Analytics and ML Data Handoff), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 1 (designing highly scalable, secure, and reliable cloud-native applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Load a periodic extract rather than a continuous stream. Why the correct answer wins: Streaming the events feeds the dashboard, and a subscription writing to the table fills it with no service.
- **B:** Incorrect for this question. A task queue with retries and rate control aimed at a specific target. Why the correct answer wins: Streaming the events feeds the dashboard, and a subscription writing to the table fills it with no service.
- **C:** Incorrect for this question. Durable object storage addressed by name rather than a database row. Why the correct answer wins: Streaming the events feeds the dashboard, and a subscription writing to the table fills it with no service.
- **D:** Correct. Write topic messages straight into a table without a consumer. In this case: Streaming the events feeds the dashboard, and a subscription writing to the table fills it with no service.
- **E:** Correct. Land analytics rows in the warehouse for SQL and ML use. In this case: Streaming the events feeds the dashboard, and a subscription writing to the table fills it with no service.

### Question 33 — A, C

Answers: Run the service emulator locally; Use Cloud Shell for the session. The local emulator exercises the queue offline, and the browser shell needs no installation. A local stand-in for a managed service used for unit and integration work. A browser terminal with the SDK and tooling already installed. Local study-map skill 2.1 (Local Emulation of Cloud Services), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 2 (building and testing applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Correct. A browser terminal with the SDK and tooling already installed. In this case: The local emulator exercises the queue offline, and the browser shell needs no installation.
- **B:** Incorrect for this question. A managed, container-defined development environment behind a private endpoint. Why the correct answer wins: The local emulator exercises the queue offline, and the browser shell needs no installation.
- **C:** Correct. A local stand-in for a managed service used for unit and integration work. In this case: The local emulator exercises the queue offline, and the browser shell needs no installation.
- **D:** Incorrect for this question. Read variable state in a running deployment without redeploying. Why the correct answer wins: The local emulator exercises the queue offline, and the browser shell needs no installation.
- **E:** Incorrect for this question. Editor integration for scaffolding, running and debugging on Google Cloud. Why the correct answer wins: The local emulator exercises the queue offline, and the browser shell needs no installation.

### Question 34 — C

Answer: Use Cloud Workstations for the environment. A managed workstation serves the pinned toolchain from the first day. A managed, container-defined development environment behind a private endpoint. Local study-map skill 2.1 (Local Emulation of Cloud Services), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 2 (building and testing applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A local stand-in for a managed service used for unit and integration work. Why the correct answer wins: A managed workstation serves the pinned toolchain from the first day.
- **B:** Incorrect for this question. Editor integration for scaffolding, running and debugging on Google Cloud. Why the correct answer wins: A managed workstation serves the pinned toolchain from the first day.
- **C:** Correct. A managed, container-defined development environment behind a private endpoint. In this case: A managed workstation serves the pinned toolchain from the first day.
- **D:** Incorrect for this question. A browser terminal with the SDK and tooling already installed. Why the correct answer wins: A managed workstation serves the pinned toolchain from the first day.

### Question 35 — A

Answer: Develop with Cloud Code in the IDE. A hosted editor runs the suite against the hosted checkout. Editor integration for scaffolding, running and debugging on Google Cloud. Local study-map skill 2.1 (Local Emulation of Cloud Services), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 2 (building and testing applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Correct. Editor integration for scaffolding, running and debugging on Google Cloud. In this case: A hosted editor runs the suite against the hosted checkout.
- **B:** Incorrect for this question. A managed, container-defined development environment behind a private endpoint. Why the correct answer wins: A hosted editor runs the suite against the hosted checkout.
- **C:** Incorrect for this question. A browser terminal with the SDK and tooling already installed. Why the correct answer wins: A hosted editor runs the suite against the hosted checkout.
- **D:** Incorrect for this question. Read variable state in a running deployment without redeploying. Why the correct answer wins: A hosted editor runs the suite against the hosted checkout.

### Question 36 — C

Answer: Ask Gemini Cloud Assist for a diagnosis. An in-editor assistant explains the error beside the code. An assistant that reads telemetry and proposes a cause and a next step. Local study-map skill 2.2 (Developer Tooling and AI Assistance), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 2 (building and testing applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Generate a first draft from context, then review and correct it. Why the correct answer wins: An in-editor assistant explains the error beside the code.
- **B:** Incorrect for this question. Give the assistant a defined tool surface instead of pasting context by hand. Why the correct answer wins: An in-editor assistant explains the error beside the code.
- **C:** Correct. An assistant that reads telemetry and proposes a cause and a next step. In this case: An in-editor assistant explains the error beside the code.
- **D:** Incorrect for this question. Editor integration for scaffolding, running and debugging on Google Cloud. Why the correct answer wins: An in-editor assistant explains the error beside the code.

### Question 37 — C

Answer: Use an AI coding assistant to draft the tests. A coding assistant drafts the handlers for the developer to finish. Generate a first draft from context, then review and correct it. Local study-map skill 2.2 (Developer Tooling and AI Assistance), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 2 (building and testing applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. An assistant that reads telemetry and proposes a cause and a next step. Why the correct answer wins: A coding assistant drafts the handlers for the developer to finish.
- **B:** Incorrect for this question. Give the assistant a defined tool surface instead of pasting context by hand. Why the correct answer wins: A coding assistant drafts the handlers for the developer to finish.
- **C:** Correct. Generate a first draft from context, then review and correct it. In this case: A coding assistant drafts the handlers for the developer to finish.
- **D:** Incorrect for this question. A browser terminal with the SDK and tooling already installed. Why the correct answer wins: A coding assistant drafts the handlers for the developer to finish.

### Question 38 — B

Answer: Connect the assistant to an MCP server. An MCP server gives the assistant those ticket tools. Give the assistant a defined tool surface instead of pasting context by hand. Local study-map skill 2.2 (Developer Tooling and AI Assistance), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 2 (building and testing applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Editor integration for scaffolding, running and debugging on Google Cloud. Why the correct answer wins: An MCP server gives the assistant those ticket tools.
- **B:** Correct. Give the assistant a defined tool surface instead of pasting context by hand. In this case: An MCP server gives the assistant those ticket tools.
- **C:** Incorrect for this question. Generate a first draft from context, then review and correct it. Why the correct answer wins: An MCP server gives the assistant those ticket tools.
- **D:** Incorrect for this question. An assistant that reads telemetry and proposes a cause and a next step. Why the correct answer wins: An MCP server gives the assistant those ticket tools.

### Question 39 — A, D

Answers: Build the image with Cloud Build; Deploy a pinned image digest. Running the declared steps in the managed builder makes it reproducible, and promoting the digest keeps it identical. A managed build service that runs the steps from a build configuration file. Release exactly the artifact that was tested rather than a moving tag. Local study-map skill 2.3 (Container Builds with Cloud Build), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 2 (building and testing applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Correct. Release exactly the artifact that was tested rather than a moving tag. In this case: Running the declared steps in the managed builder makes it reproducible, and promoting the digest keeps it identical.
- **B:** Incorrect for this question. A loop that rebuilds and redeploys automatically on a source change. Why the correct answer wins: Running the declared steps in the managed builder makes it reproducible, and promoting the digest keeps it identical.
- **C:** Incorrect for this question. Run the build steps locally and push the result when someone remembers. Why the correct answer wins: Running the declared steps in the managed builder makes it reproducible, and promoting the digest keeps it identical.
- **D:** Correct. A managed build service that runs the steps from a build configuration file. In this case: Running the declared steps in the managed builder makes it reproducible, and promoting the digest keeps it identical.
- **E:** Incorrect for this question. Hand the source to the managed builder instead of shipping an image. Why the correct answer wins: Running the declared steps in the managed builder makes it reproducible, and promoting the digest keeps it identical.

### Question 40 — D

Answer: Trigger the build from a repository push. A trigger on the branch starts the build on the merge. Start the pipeline when the branch changes rather than by hand. Local study-map skill 2.3 (Container Builds with Cloud Build), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 2 (building and testing applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A cron-style trigger that calls a target on a fixed timetable. Why the correct answer wins: A trigger on the branch starts the build on the merge.
- **B:** Incorrect for this question. Run the build steps locally and push the result when someone remembers. Why the correct answer wins: A trigger on the branch starts the build on the merge.
- **C:** Incorrect for this question. A task queue with retries and rate control aimed at a specific target. Why the correct answer wins: A trigger on the branch starts the build on the merge.
- **D:** Correct. Start the pipeline when the branch changes rather than by hand. In this case: A trigger on the branch starts the build on the merge.

### Question 41 — D

Answer: Iterate with Skaffold. An automatic loop rebuilds the image on each save. A loop that rebuilds and redeploys automatically on a source change. Local study-map skill 2.3 (Container Builds with Cloud Build), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 2 (building and testing applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A managed build service that runs the steps from a build configuration file. Why the correct answer wins: An automatic loop rebuilds the image on each save.
- **B:** Incorrect for this question. Run the build steps locally and push the result when someone remembers. Why the correct answer wins: An automatic loop rebuilds the image on each save.
- **C:** Incorrect for this question. Release exactly the artifact that was tested rather than a moving tag. Why the correct answer wins: An automatic loop rebuilds the image on each save.
- **D:** Correct. A loop that rebuilds and redeploys automatically on a source change. In this case: An automatic loop rebuilds the image on each save.

### Question 42 — D

Answer: Push the image to Artifact Registry. A scoped repository allows the runtime identity to pull it. A managed registry with IAM-scoped repositories per environment. Local study-map skill 2.3 (Container Builds with Cloud Build), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 2 (building and testing applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Durable object storage addressed by name rather than a database row. Why the correct answer wins: A scoped repository allows the runtime identity to pull it.
- **B:** Incorrect for this question. The older registry whose access model is project-wide Cloud Storage. Why the correct answer wins: A scoped repository allows the runtime identity to pull it.
- **C:** Incorrect for this question. A key the customer owns, rotates and can disable. Why the correct answer wins: A scoped repository allows the runtime identity to pull it.
- **D:** Correct. A managed registry with IAM-scoped repositories per environment. In this case: A scoped repository allows the runtime identity to pull it.

### Question 43 — B

Answer: Push the image to Artifact Registry. A repository per environment separates the access. A managed registry with IAM-scoped repositories per environment. Local study-map skill 2.4 (Artifact Registry and Image Storage), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 2 (building and testing applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Durable object storage addressed by name rather than a database row. Why the correct answer wins: A repository per environment separates the access.
- **B:** Correct. A managed registry with IAM-scoped repositories per environment. In this case: A repository per environment separates the access.
- **C:** Incorrect for this question. The older registry whose access model is project-wide Cloud Storage. Why the correct answer wins: A repository per environment separates the access.
- **D:** Incorrect for this question. A managed build service that runs the steps from a build configuration file. Why the correct answer wins: A repository per environment separates the access.

### Question 44 — A

Answer: Push the image to Container Registry. The previous host name keeps that CI job pushing. The older registry whose access model is project-wide Cloud Storage. Local study-map skill 2.4 (Artifact Registry and Image Storage), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 2 (building and testing applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Correct. The older registry whose access model is project-wide Cloud Storage. In this case: The previous host name keeps that CI job pushing.
- **B:** Incorrect for this question. A managed build service that runs the steps from a build configuration file. Why the correct answer wins: The previous host name keeps that CI job pushing.
- **C:** Incorrect for this question. Durable object storage addressed by name rather than a database row. Why the correct answer wins: The previous host name keeps that CI job pushing.
- **D:** Incorrect for this question. A managed registry with IAM-scoped repositories per environment. Why the correct answer wins: The previous host name keeps that CI job pushing.

### Question 45 — B

Answer: Store the objects in Cloud Storage. Object storage keeps the evidence after the images are pruned. Durable object storage addressed by name rather than a database row. Local study-map skill 2.4 (Artifact Registry and Image Storage), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 2 (building and testing applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. The older registry whose access model is project-wide Cloud Storage. Why the correct answer wins: Object storage keeps the evidence after the images are pruned.
- **B:** Correct. Durable object storage addressed by name rather than a database row. In this case: Object storage keeps the evidence after the images are pruned.
- **C:** Incorrect for this question. A managed build service that runs the steps from a build configuration file. Why the correct answer wins: Object storage keeps the evidence after the images are pruned.
- **D:** Incorrect for this question. A managed registry with IAM-scoped repositories per environment. Why the correct answer wins: Object storage keeps the evidence after the images are pruned.

### Question 46 — C, E

Answers: Enforce admission with Binary Authorization; Generate build provenance in Cloud Build. Admission enforces the attestation, and the provenance record names the source revision. Only images that satisfy the attestation policy may be deployed. A signed record of what was built and from which source. Local study-map skill 2.5 (Build Provenance and Admission Control), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 2 (building and testing applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Report known vulnerabilities in the image layers and packages. Why the correct answer wins: Admission enforces the attestation, and the provenance record names the source revision.
- **B:** Incorrect for this question. Aggregate and triage security findings across the project. Why the correct answer wins: Admission enforces the attestation, and the provenance record names the source revision.
- **C:** Correct. Only images that satisfy the attestation policy may be deployed. In this case: Admission enforces the attestation, and the provenance record names the source revision.
- **D:** Incorrect for this question. Demand a stronger provenance guarantee as a gate on the pipeline. Why the correct answer wins: Admission enforces the attestation, and the provenance record names the source revision.
- **E:** Correct. A signed record of what was built and from which source. In this case: Admission enforces the attestation, and the provenance record names the source revision.

### Question 47 — D

Answer: Scan the image with Artifact Analysis. Image analysis maps the CVE to the images containing it. Report known vulnerabilities in the image layers and packages. Local study-map skill 2.5 (Build Provenance and Admission Control), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 2 (building and testing applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A signed record of what was built and from which source. Why the correct answer wins: Image analysis maps the CVE to the images containing it.
- **B:** Incorrect for this question. Only images that satisfy the attestation policy may be deployed. Why the correct answer wins: Image analysis maps the CVE to the images containing it.
- **C:** Incorrect for this question. Aggregate and triage security findings across the project. Why the correct answer wins: Image analysis maps the CVE to the images containing it.
- **D:** Correct. Report known vulnerabilities in the image layers and packages. In this case: Image analysis maps the CVE to the images containing it.

### Question 48 — B

Answer: Review the finding in Security Command Center. The security command centre shows those findings with the rest. Aggregate and triage security findings across the project. Local study-map skill 2.5 (Build Provenance and Admission Control), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 2 (building and testing applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Report known vulnerabilities in the image layers and packages. Why the correct answer wins: The security command centre shows those findings with the rest.
- **B:** Correct. Aggregate and triage security findings across the project. In this case: The security command centre shows those findings with the rest.
- **C:** Incorrect for this question. Only images that satisfy the attestation policy may be deployed. Why the correct answer wins: The security command centre shows those findings with the rest.
- **D:** Incorrect for this question. A signed record of what was built and from which source. Why the correct answer wins: The security command centre shows those findings with the rest.

### Question 49 — A

Answer: Add a unit test with dependencies stubbed. Unit tests isolate each branch and name the failing one. Exercise one unit in isolation with its collaborators replaced. Local study-map skill 2.6 (Unit Testing Practice), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 2 (building and testing applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Correct. Exercise one unit in isolation with its collaborators replaced. In this case: Unit tests isolate each branch and name the failing one.
- **B:** Incorrect for this question. Measure behaviour under expected peak traffic rather than guessing. Why the correct answer wins: Unit tests isolate each branch and name the failing one.
- **C:** Incorrect for this question. Exercise the wire-up between components before deploying. Why the correct answer wins: Unit tests isolate each branch and name the failing one.
- **D:** Incorrect for this question. Keep the suite trustworthy while the unstable test is repaired. Why the correct answer wins: Unit tests isolate each branch and name the failing one.

### Question 50 — B

Answer: Quarantine the flaky test and fix it. Quarantining it keeps the rest of the suite trustworthy meanwhile. Keep the suite trustworthy while the unstable test is repaired. Local study-map skill 2.6 (Unit Testing Practice), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 2 (building and testing applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Exercise the wire-up between components before deploying. Why the correct answer wins: Quarantining it keeps the rest of the suite trustworthy meanwhile.
- **B:** Correct. Keep the suite trustworthy while the unstable test is repaired. In this case: Quarantining it keeps the rest of the suite trustworthy meanwhile.
- **C:** Incorrect for this question. Make a passing test suite a precondition for release. Why the correct answer wins: Quarantining it keeps the rest of the suite trustworthy meanwhile.
- **D:** Incorrect for this question. Exercise one unit in isolation with its collaborators replaced. Why the correct answer wins: Quarantining it keeps the rest of the suite trustworthy meanwhile.

### Question 51 — C

Answer: Block the deploy on the test result. A gate refuses the merge when the suite fails. Make a passing test suite a precondition for release. Local study-map skill 2.6 (Unit Testing Practice), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 2 (building and testing applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Exercise the wire-up between components before deploying. Why the correct answer wins: A gate refuses the merge when the suite fails.
- **B:** Incorrect for this question. Measure behaviour under expected peak traffic rather than guessing. Why the correct answer wins: A gate refuses the merge when the suite fails.
- **C:** Correct. Make a passing test suite a precondition for release. In this case: A gate refuses the merge when the suite fails.
- **D:** Incorrect for this question. Keep the suite trustworthy while the unstable test is repaired. Why the correct answer wins: A gate refuses the merge when the suite fails.

### Question 52 — B, D

Answers: Run an integration test against the emulator; Run the tests as a Cloud Build step. An integration run exercises the real dependency, and a build step runs it every time. Exercise the wire-up between components before deploying. Fail the pipeline at the test stage instead of after deployment. Local study-map skill 2.7 (Automated Integration Testing), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 2 (building and testing applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Exercise one unit in isolation with its collaborators replaced. Why the correct answer wins: An integration run exercises the real dependency, and a build step runs it every time.
- **B:** Correct. Exercise the wire-up between components before deploying. In this case: An integration run exercises the real dependency, and a build step runs it every time.
- **C:** Incorrect for this question. Find the function consuming CPU or memory under real traffic. Why the correct answer wins: An integration run exercises the real dependency, and a build step runs it every time.
- **D:** Correct. Fail the pipeline at the test stage instead of after deployment. In this case: An integration run exercises the real dependency, and a build step runs it every time.
- **E:** Incorrect for this question. Measure behaviour under expected peak traffic rather than guessing. Why the correct answer wins: An integration run exercises the real dependency, and a build step runs it every time.

### Question 53 — A

Answer: Load-test the release before the rollout. A load run at doubled volume shows the drain before launch. Measure behaviour under expected peak traffic rather than guessing. Local study-map skill 2.7 (Automated Integration Testing), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 2 (building and testing applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Correct. Measure behaviour under expected peak traffic rather than guessing. In this case: A load run at doubled volume shows the drain before launch.
- **B:** Incorrect for this question. Exercise the wire-up between components before deploying. Why the correct answer wins: A load run at doubled volume shows the drain before launch.
- **C:** Incorrect for this question. Find the function consuming CPU or memory under real traffic. Why the correct answer wins: A load run at doubled volume shows the drain before launch.
- **D:** Incorrect for this question. Exercise one unit in isolation with its collaborators replaced. Why the correct answer wins: A load run at doubled volume shows the drain before launch.

### Question 54 — C

Answer: Profile the service with Cloud Profiler. A profiler names the function consuming the CPU. Find the function consuming CPU or memory under real traffic. Local study-map skill 2.7 (Automated Integration Testing), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 2 (building and testing applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Measure behaviour under expected peak traffic rather than guessing. Why the correct answer wins: A profiler names the function consuming the CPU.
- **B:** Incorrect for this question. Group and count application errors instead of grepping logs. Why the correct answer wins: A profiler names the function consuming the CPU.
- **C:** Correct. Find the function consuming CPU or memory under real traffic. In this case: A profiler names the function consuming the CPU.
- **D:** Incorrect for this question. Read variable state in a running deployment without redeploying. Why the correct answer wins: A profiler names the function consuming the CPU.

### Question 55 — A

Answer: Inspect the live process with Cloud Debugger. The debugger pauses after the third call with the state visible. Read variable state in a running deployment without redeploying. Local study-map skill 2.7 (Automated Integration Testing), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 2 (building and testing applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Correct. Read variable state in a running deployment without redeploying. In this case: The debugger pauses after the third call with the state visible.
- **B:** Incorrect for this question. Exercise one unit in isolation with its collaborators replaced. Why the correct answer wins: The debugger pauses after the third call with the state visible.
- **C:** Incorrect for this question. Find the function consuming CPU or memory under real traffic. Why the correct answer wins: The debugger pauses after the third call with the state visible.
- **D:** Incorrect for this question. Exercise the wire-up between components before deploying. Why the correct answer wins: The debugger pauses after the third call with the state visible.

### Question 56 — C, D

Answers: Deploy from source and let the platform build it; Keep a minimum number of instances warm. Building from source removes the Dockerfile, and a warm minimum removes the cold start. Hand the source to the managed builder instead of shipping an image. Pay for idle capacity so a cold start never appears in the latency percentiles. Local study-map skill 3.1 (Deploying Cloud Run from Source), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 3 (configuring cloud-native applications for deployment): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Run the build steps locally and push the result when someone remembers. Why the correct answer wins: Building from source removes the Dockerfile, and a warm minimum removes the cold start.
- **B:** Incorrect for this question. Bound the blast radius and the bill at the cost of queueing when the cap is reached. Why the correct answer wins: Building from source removes the Dockerfile, and a warm minimum removes the cold start.
- **C:** Correct. Pay for idle capacity so a cold start never appears in the latency percentiles. In this case: Building from source removes the Dockerfile, and a warm minimum removes the cold start.
- **D:** Correct. Hand the source to the managed builder instead of shipping an image. In this case: Building from source removes the Dockerfile, and a warm minimum removes the cold start.
- **E:** Incorrect for this question. Wrap the existing process in a portable artifact that a managed runtime can execute. Why the correct answer wins: Building from source removes the Dockerfile, and a warm minimum removes the cold start.

### Question 57 — B

Answer: Cap the maximum instance count. A ceiling on instances bounds the fleet during the campaign. Bound the blast radius and the bill at the cost of queueing when the cap is reached. Local study-map skill 3.1 (Deploying Cloud Run from Source), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 3 (configuring cloud-native applications for deployment): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Allow the process the headroom it needs so it is not throttled or killed. Why the correct answer wins: A ceiling on instances bounds the fleet during the campaign.
- **B:** Correct. Bound the blast radius and the bill at the cost of queueing when the cap is reached. In this case: A ceiling on instances bounds the fleet during the campaign.
- **C:** Incorrect for this question. Trade a term commitment for a lower unit price on capacity that never idles. Why the correct answer wins: A ceiling on instances bounds the fleet during the campaign.
- **D:** Incorrect for this question. Pay for idle capacity so a cold start never appears in the latency percentiles. Why the correct answer wins: A ceiling on instances bounds the fleet during the campaign.

### Question 58 — B

Answer: Raise CPU during start-up only. Extra CPU during start shortens the warm-up inside the window. Speed initialization without paying for the extra CPU afterwards. Local study-map skill 3.1 (Deploying Cloud Run from Source), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 3 (configuring cloud-native applications for deployment): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Let each instance serve more simultaneous requests before another instance is started. Why the correct answer wins: Extra CPU during start shortens the warm-up inside the window.
- **B:** Correct. Speed initialization without paying for the extra CPU afterwards. In this case: Extra CPU during start shortens the warm-up inside the window.
- **C:** Incorrect for this question. Pay for idle capacity so a cold start never appears in the latency percentiles. Why the correct answer wins: Extra CPU during start shortens the warm-up inside the window.
- **D:** Incorrect for this question. Charge only while a request is being handled, which suits bursty traffic. Why the correct answer wins: Extra CPU during start shortens the warm-up inside the window.

### Question 59 — D

Answer: Run the batch work as a Cloud Run job. A job performs the load and holds nothing afterwards. A task-shaped execution that runs to completion instead of serving requests. Local study-map skill 3.1 (Deploying Cloud Run from Source), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 3 (configuring cloud-native applications for deployment): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. An event-triggered function runtime for a single-purpose handler rather than a long-lived service. Why the correct answer wins: A job performs the load and holds nothing afterwards.
- **B:** Incorrect for this question. A managed container runtime that scales to zero and bills per request while it serves traffic. Why the correct answer wins: A job performs the load and holds nothing afterwards.
- **C:** Incorrect for this question. A trigger path that turns a Cloud Audit Log or resource event into a delivery. Why the correct answer wins: A job performs the load and holds nothing afterwards.
- **D:** Correct. A task-shaped execution that runs to completion instead of serving requests. In this case: A job performs the load and holds nothing afterwards.

### Question 60 — B, C

Answers: Route the event with Eventarc; Deliver to an HTTPS push subscription. The event trigger delivers the change, and push delivery retries against the collector. A trigger path that turns a Cloud Audit Log or resource event into a delivery. Push each message to an endpoint instead of having the consumer pull. Local study-map skill 3.2 (Cloud Run Triggers and Event Receivers), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 3 (configuring cloud-native applications for deployment): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A stateful sequence of service calls with retries and error branches. Why the correct answer wins: The event trigger delivers the change, and push delivery retries against the collector.
- **B:** Correct. Push each message to an endpoint instead of having the consumer pull. In this case: The event trigger delivers the change, and push delivery retries against the collector.
- **C:** Correct. A trigger path that turns a Cloud Audit Log or resource event into a delivery. In this case: The event trigger delivers the change, and push delivery retries against the collector.
- **D:** Incorrect for this question. The consumer controls the pace and acknowledges messages itself. Why the correct answer wins: The event trigger delivers the change, and push delivery retries against the collector.
- **E:** Incorrect for this question. A cron-style trigger that calls a target on a fixed timetable. Why the correct answer wins: The event trigger delivers the change, and push delivery retries against the collector.

### Question 61 — B

Answer: Grant the invoker role to the calling identity. The triggering identity needs the invoker role on the collector. Control who may call the service with IAM rather than a shared token. Local study-map skill 3.2 (Cloud Run Triggers and Event Receivers), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 3 (configuring cloud-native applications for deployment): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Authenticate and authorize users before a request reaches the application. Why the correct answer wins: The triggering identity needs the invoker role on the collector.
- **B:** Correct. Control who may call the service with IAM rather than a shared token. In this case: The triggering identity needs the invoker role on the collector.
- **C:** Incorrect for this question. Let anyone reach the endpoint, which is only appropriate for public content. Why the correct answer wins: The triggering identity needs the invoker role on the collector.
- **D:** Incorrect for this question. A lighter managed gateway for routing and key-based quota enforcement. Why the correct answer wins: The triggering identity needs the invoker role on the collector.

### Question 62 — D

Answer: Queue the work as a Cloud Tasks task. A task queue dispatches at the rate the partner permits. A task queue with retries and rate control aimed at a specific target. Local study-map skill 3.2 (Cloud Run Triggers and Event Receivers), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 3 (configuring cloud-native applications for deployment): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A durable, at-least-once message channel with independent subscribers. Why the correct answer wins: A task queue dispatches at the rate the partner permits.
- **B:** Incorrect for this question. A cron-style trigger that calls a target on a fixed timetable. Why the correct answer wins: A task queue dispatches at the rate the partner permits.
- **C:** Incorrect for this question. A stateful sequence of service calls with retries and error branches. Why the correct answer wins: A task queue dispatches at the rate the partner permits.
- **D:** Correct. A task queue with retries and rate control aimed at a specific target. In this case: A task queue dispatches at the rate the partner permits.

### Question 63 — A

Answer: Raise the per-instance concurrency limit. Raising per-instance concurrency serves the streams on fewer instances. Let each instance serve more simultaneous requests before another instance is started. Local study-map skill 3.3 (Cloud Run Service Configuration), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 3 (configuring cloud-native applications for deployment): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Correct. Let each instance serve more simultaneous requests before another instance is started. In this case: Raising per-instance concurrency serves the streams on fewer instances.
- **B:** Incorrect for this question. Give extra CPU during start-up so initialization finishes faster at a small extra charge. Why the correct answer wins: Raising per-instance concurrency serves the streams on fewer instances.
- **C:** Incorrect for this question. Bound the blast radius and the bill at the cost of queueing when the cap is reached. Why the correct answer wins: Raising per-instance concurrency serves the streams on fewer instances.
- **D:** Incorrect for this question. Pay for idle capacity so a cold start never appears in the latency percentiles. Why the correct answer wins: Raising per-instance concurrency serves the streams on fewer instances.

### Question 64 — C

Answer: Restrict ingress to internal traffic. Internal ingress refuses every call from the public name. Accept only traffic from the VPC and internal load balancers. Local study-map skill 3.3 (Cloud Run Service Configuration), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 3 (configuring cloud-native applications for deployment): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Let anyone reach the endpoint, which is only appropriate for public content. Why the correct answer wins: Internal ingress refuses every call from the public name.
- **B:** Incorrect for this question. Authenticate and authorize users before a request reaches the application. Why the correct answer wins: Internal ingress refuses every call from the public name.
- **C:** Correct. Accept only traffic from the VPC and internal load balancers. In this case: Internal ingress refuses every call from the public name.
- **D:** Incorrect for this question. A single anycast address that routes to the nearest healthy backend. Why the correct answer wins: Internal ingress refuses every call from the public name.

### Question 65 — B

Answer: Allow unauthenticated invocations. Allowing unauthenticated calls lets the provider post without a token. Let anyone reach the endpoint, which is only appropriate for public content. Local study-map skill 3.3 (Cloud Run Service Configuration), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 3 (configuring cloud-native applications for deployment): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Authenticate and authorize users before a request reaches the application. Why the correct answer wins: Allowing unauthenticated calls lets the provider post without a token.
- **B:** Correct. Let anyone reach the endpoint, which is only appropriate for public content. In this case: Allowing unauthenticated calls lets the provider post without a token.
- **C:** Incorrect for this question. Control who may call the service with IAM rather than a shared token. Why the correct answer wins: Allowing unauthenticated calls lets the provider post without a token.
- **D:** Incorrect for this question. Accept only traffic from the VPC and internal load balancers. Why the correct answer wins: Allowing unauthenticated calls lets the provider post without a token.

### Question 66 — A

Answer: Use request-based billing. Request-based billing charges nothing while no request arrives. Charge only while a request is being handled, which suits bursty traffic. Local study-map skill 3.3 (Cloud Run Service Configuration), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 3 (configuring cloud-native applications for deployment): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Correct. Charge only while a request is being handled, which suits bursty traffic. In this case: Request-based billing charges nothing while no request arrives.
- **B:** Incorrect for this question. Trade a term commitment for a lower unit price on capacity that never idles. Why the correct answer wins: Request-based billing charges nothing while no request arrives.
- **C:** Incorrect for this question. Charge for the whole instance lifetime, which suits steady background work. Why the correct answer wins: Request-based billing charges nothing while no request arrives.
- **D:** Incorrect for this question. Pay for idle capacity so a cold start never appears in the latency percentiles. Why the correct answer wins: Request-based billing charges nothing while no request arrives.

### Question 67 — A

Answer: Use API Gateway for the API. The managed gateway applies the declared key check in front of all five. A lighter managed gateway for routing and key-based quota enforcement. Local study-map skill 3.4 (API Exposure and Versioning), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 3 (configuring cloud-native applications for deployment): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Correct. A lighter managed gateway for routing and key-based quota enforcement. In this case: The managed gateway applies the declared key check in front of all five.
- **B:** Incorrect for this question. An API management layer for quotas, keys, mediation and analytics. Why the correct answer wins: The managed gateway applies the declared key check in front of all five.
- **C:** Incorrect for this question. Accept only traffic from the VPC and internal load balancers. Why the correct answer wins: The managed gateway applies the declared key check in front of all five.
- **D:** Incorrect for this question. A single anycast address that routes to the nearest healthy backend. Why the correct answer wins: The managed gateway applies the declared key check in front of all five.

### Question 68 — C

Answer: Put a global external Application Load Balancer in front. A global front door supplies the single hostname and certificate. A single anycast address that routes to the nearest healthy backend. Local study-map skill 3.4 (API Exposure and Versioning), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 3 (configuring cloud-native applications for deployment): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A load balancer scoped to one region with a regional address. Why the correct answer wins: A global front door supplies the single hostname and certificate.
- **B:** Incorrect for this question. Accept only traffic from the VPC and internal load balancers. Why the correct answer wins: A global front door supplies the single hostname and certificate.
- **C:** Correct. A single anycast address that routes to the nearest healthy backend. In this case: A global front door supplies the single hostname and certificate.
- **D:** Incorrect for this question. A lighter managed gateway for routing and key-based quota enforcement. Why the correct answer wins: A global front door supplies the single hostname and certificate.

### Question 69 — C, E

Answers: Use a rolling update strategy; Tune maxSurge and maxUnavailable. Gradual replacement keeps the service up, and the unavailable bound caps the loss. Replace pods gradually so the deployment stays available. Control how much capacity may be missing while pods are replaced. Local study-map skill 3.5 (Deploying Containers to GKE), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 3 (configuring cloud-native applications for deployment): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Limit how many pods may be evicted at once during voluntary disruption. Why the correct answer wins: Gradual replacement keeps the service up, and the unavailable bound caps the loss.
- **B:** Incorrect for this question. Place work on nodes whose shape and pricing match the workload. Why the correct answer wins: Gradual replacement keeps the service up, and the unavailable bound caps the loss.
- **C:** Correct. Replace pods gradually so the deployment stays available. In this case: Gradual replacement keeps the service up, and the unavailable bound caps the loss.
- **D:** Incorrect for this question. Use reclaimable capacity for work that can tolerate a node disappearing. Why the correct answer wins: Gradual replacement keeps the service up, and the unavailable bound caps the loss.
- **E:** Correct. Control how much capacity may be missing while pods are replaced. In this case: Gradual replacement keeps the service up, and the unavailable bound caps the loss.

### Question 70 — B

Answer: Use GKE Autopilot for the cluster. The managed mode sizes and patches the nodes for them. A cluster mode where node provisioning and sizing are handled for the workload. Local study-map skill 3.5 (Deploying Containers to GKE), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 3 (configuring cloud-native applications for deployment): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Add or remove nodes as pending pods demand capacity. Why the correct answer wins: The managed mode sizes and patches the nodes for them.
- **B:** Correct. A cluster mode where node provisioning and sizing are handled for the workload. In this case: The managed mode sizes and patches the nodes for them.
- **C:** Incorrect for this question. Place work on nodes whose shape and pricing match the workload. Why the correct answer wins: The managed mode sizes and patches the nodes for them.
- **D:** Incorrect for this question. Use reclaimable capacity for work that can tolerate a node disappearing. Why the correct answer wins: The managed mode sizes and patches the nodes for them.

### Question 71 — A

Answer: Bind a Kubernetes service account to a Google service account. Binding the pod identity yields tokens without any key file. Keyless credential issuance for pods through Workload Identity. Local study-map skill 3.5 (Deploying Containers to GKE), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 3 (configuring cloud-native applications for deployment): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Correct. Keyless credential issuance for pods through Workload Identity. In this case: Binding the pod identity yields tokens without any key file.
- **B:** Incorrect for this question. A long-lived credential that has to be stored and rotated by hand. Why the correct answer wins: Binding the pod identity yields tokens without any key file.
- **C:** Incorrect for this question. Exchange an outside token for a short-lived Google credential. Why the correct answer wins: Binding the pod identity yields tokens without any key file.
- **D:** Incorrect for this question. A dedicated identity whose roles can be granted and revoked independently. Why the correct answer wins: Binding the pod identity yields tokens without any key file.

### Question 72 — C

Answer: Enable node pool autoscaling. Node pool autoscaling adds capacity for the pending pods. Add or remove nodes as pending pods demand capacity. Local study-map skill 3.5 (Deploying Containers to GKE), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 3 (configuring cloud-native applications for deployment): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Add pods when average CPU crosses the target. Why the correct answer wins: Node pool autoscaling adds capacity for the pending pods.
- **B:** Incorrect for this question. Limit how many pods may be evicted at once during voluntary disruption. Why the correct answer wins: Node pool autoscaling adds capacity for the pending pods.
- **C:** Correct. Add or remove nodes as pending pods demand capacity. In this case: Node pool autoscaling adds capacity for the pending pods.
- **D:** Incorrect for this question. Keep capacity warm so scale-up does not cost the first requests. Why the correct answer wins: Node pool autoscaling adds capacity for the pending pods.

### Question 73 — C, E

Answers: Configure a liveness probe; Configure a startup probe. The liveness probe restarts the hung container, and the startup probe covers the long initialisation. Restart the container when it can no longer make progress. Hold traffic until the application is actually ready to serve. Local study-map skill 3.6 (Kubernetes Health Checks), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 3 (configuring cloud-native applications for deployment): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Limit how many pods may be evicted at once during voluntary disruption. Why the correct answer wins: The liveness probe restarts the hung container, and the startup probe covers the long initialisation.
- **B:** Incorrect for this question. Remove the instance from the endpoint list while it cannot serve. Why the correct answer wins: The liveness probe restarts the hung container, and the startup probe covers the long initialisation.
- **C:** Correct. Restart the container when it can no longer make progress. In this case: The liveness probe restarts the hung container, and the startup probe covers the long initialisation.
- **D:** Incorrect for this question. Let the load balancer stop sending traffic to an unhealthy instance. Why the correct answer wins: The liveness probe restarts the hung container, and the startup probe covers the long initialisation.
- **E:** Correct. Hold traffic until the application is actually ready to serve. In this case: The liveness probe restarts the hung container, and the startup probe covers the long initialisation.

### Question 74 — C

Answer: Configure a readiness probe. A readiness probe withholds the traffic until the check passes. Remove the instance from the endpoint list while it cannot serve. Local study-map skill 3.6 (Kubernetes Health Checks), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 3 (configuring cloud-native applications for deployment): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Limit how many pods may be evicted at once during voluntary disruption. Why the correct answer wins: A readiness probe withholds the traffic until the check passes.
- **B:** Incorrect for this question. Hold traffic until the application is actually ready to serve. Why the correct answer wins: A readiness probe withholds the traffic until the check passes.
- **C:** Correct. Remove the instance from the endpoint list while it cannot serve. In this case: A readiness probe withholds the traffic until the check passes.
- **D:** Incorrect for this question. Restart the container when it can no longer make progress. Why the correct answer wins: A readiness probe withholds the traffic until the check passes.

### Question 75 — D

Answer: Add a PodDisruptionBudget. A disruption budget guarantees the three replicas survive the drain. Limit how many pods may be evicted at once during voluntary disruption. Local study-map skill 3.6 (Kubernetes Health Checks), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 3 (configuring cloud-native applications for deployment): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Remove the instance from the endpoint list while it cannot serve. Why the correct answer wins: A disruption budget guarantees the three replicas survive the drain.
- **B:** Incorrect for this question. Restart the container when it can no longer make progress. Why the correct answer wins: A disruption budget guarantees the three replicas survive the drain.
- **C:** Incorrect for this question. Let the load balancer stop sending traffic to an unhealthy instance. Why the correct answer wins: A disruption budget guarantees the three replicas survive the drain.
- **D:** Correct. Limit how many pods may be evicted at once during voluntary disruption. In this case: A disruption budget guarantees the three replicas survive the drain.

### Question 76 — A

Answer: Scale pods on CPU utilization. Scaling on utilisation follows the encoder's CPU demand. Add pods when average CPU crosses the target. Local study-map skill 3.7 (Horizontal Pod Autoscaling), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 3 (configuring cloud-native applications for deployment): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Correct. Add pods when average CPU crosses the target. In this case: Scaling on utilisation follows the encoder's CPU demand.
- **B:** Incorrect for this question. Add pods on a signal that tracks demand better than CPU. Why the correct answer wins: Scaling on utilisation follows the encoder's CPU demand.
- **C:** Incorrect for this question. Add or remove nodes as pending pods demand capacity. Why the correct answer wins: Scaling on utilisation follows the encoder's CPU demand.
- **D:** Incorrect for this question. Keep capacity warm so scale-up does not cost the first requests. Why the correct answer wins: Scaling on utilisation follows the encoder's CPU demand.

### Question 77 — C

Answer: Scale pods on a custom or external metric. A custom metric scales on the waiting message count. Add pods on a signal that tracks demand better than CPU. Local study-map skill 3.7 (Horizontal Pod Autoscaling), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 3 (configuring cloud-native applications for deployment): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Add pods when average CPU crosses the target. Why the correct answer wins: A custom metric scales on the waiting message count.
- **B:** Incorrect for this question. Add or remove nodes as pending pods demand capacity. Why the correct answer wins: A custom metric scales on the waiting message count.
- **C:** Correct. Add pods on a signal that tracks demand better than CPU. In this case: A custom metric scales on the waiting message count.
- **D:** Incorrect for this question. Trade a term commitment for a lower unit price on capacity that never idles. Why the correct answer wins: A custom metric scales on the waiting message count.

### Question 78 — C

Answer: Set a minimum replica count. A replica floor keeps two pods serving before the burst. Keep capacity warm so scale-up does not cost the first requests. Local study-map skill 3.7 (Horizontal Pod Autoscaling), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 3 (configuring cloud-native applications for deployment): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Add pods when average CPU crosses the target. Why the correct answer wins: A replica floor keeps two pods serving before the burst.
- **B:** Incorrect for this question. Add or remove nodes as pending pods demand capacity. Why the correct answer wins: A replica floor keeps two pods serving before the burst.
- **C:** Correct. Keep capacity warm so scale-up does not cost the first requests. In this case: A replica floor keeps two pods serving before the burst.
- **D:** Incorrect for this question. Limit how many pods may be evicted at once during voluntary disruption. Why the correct answer wins: A replica floor keeps two pods serving before the burst.

### Question 79 — C

Answer: Schedule the invocation with Cloud Scheduler. A scheduled job starts the reconciliation on the fixed clock. A cron-style trigger that calls a target on a fixed timetable. Local study-map skill 3.2 (Cloud Run Triggers and Event Receivers), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 3 (configuring cloud-native applications for deployment): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A trigger path that turns a Cloud Audit Log or resource event into a delivery. Why the correct answer wins: A scheduled job starts the reconciliation on the fixed clock.
- **B:** Incorrect for this question. A task queue with retries and rate control aimed at a specific target. Why the correct answer wins: A scheduled job starts the reconciliation on the fixed clock.
- **C:** Correct. A cron-style trigger that calls a target on a fixed timetable. In this case: A scheduled job starts the reconciliation on the fixed clock.
- **D:** Incorrect for this question. A stateful sequence of service calls with retries and error branches. Why the correct answer wins: A scheduled job starts the reconciliation on the fixed clock.

### Question 80 — C, D

Answers: Use the language connector with IAM; Pool and reuse database connections. The connector library handles the connection in process, and a pool reuses the sessions. A client library that resolves and authorizes the instance itself. Keep a small set of warm connections instead of opening one per request. Local study-map skill 4.1 (Connecting to Datastores), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 4 (integrating applications with Google Cloud services): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A local proxy that authorizes the connection with IAM and encrypts it. Why the correct answer wins: The connector library handles the connection in process, and a pool reuses the sessions.
- **B:** Incorrect for this question. A private endpoint that consumes a published service without peering. Why the correct answer wins: The connector library handles the connection in process, and a pool reuses the sessions.
- **C:** Correct. Keep a small set of warm connections instead of opening one per request. In this case: The connector library handles the connection in process, and a pool reuses the sessions.
- **D:** Correct. A client library that resolves and authorizes the instance itself. In this case: The connector library handles the connection in process, and a pool reuses the sessions.
- **E:** Incorrect for this question. A private address reachable from the VPC without a proxy process. Why the correct answer wins: The connector library handles the connection in process, and a pool reuses the sessions.

### Question 81 — B

Answer: Connect through the Cloud SQL Auth Proxy. A proxy sidecar provides the private path for that runtime. A local proxy that authorizes the connection with IAM and encrypts it. Local study-map skill 4.1 (Connecting to Datastores), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 4 (integrating applications with Google Cloud services): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A private endpoint that consumes a published service without peering. Why the correct answer wins: A proxy sidecar provides the private path for that runtime.
- **B:** Correct. A local proxy that authorizes the connection with IAM and encrypts it. In this case: A proxy sidecar provides the private path for that runtime.
- **C:** Incorrect for this question. The equivalent authorized connector for AlloyDB instances. Why the correct answer wins: A proxy sidecar provides the private path for that runtime.
- **D:** Incorrect for this question. A client library that resolves and authorizes the instance itself. Why the correct answer wins: A proxy sidecar provides the private path for that runtime.

### Question 82 — B

Answer: Connect through the AlloyDB Auth Proxy. The proxy renews the certificates the clients use. The equivalent authorized connector for AlloyDB instances. Local study-map skill 4.1 (Connecting to Datastores), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 4 (integrating applications with Google Cloud services): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A client library that resolves and authorizes the instance itself. Why the correct answer wins: The proxy renews the certificates the clients use.
- **B:** Correct. The equivalent authorized connector for AlloyDB instances. In this case: The proxy renews the certificates the clients use.
- **C:** Incorrect for this question. A private address reachable from the VPC without a proxy process. Why the correct answer wins: The proxy renews the certificates the clients use.
- **D:** Incorrect for this question. A local proxy that authorizes the connection with IAM and encrypts it. Why the correct answer wins: The proxy renews the certificates the clients use.

### Question 83 — B

Answer: Connect over the database private IP. A private address keeps every client on the internal path. A private address reachable from the VPC without a proxy process. Local study-map skill 4.1 (Connecting to Datastores), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 4 (integrating applications with Google Cloud services): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A client library that resolves and authorizes the instance itself. Why the correct answer wins: A private address keeps every client on the internal path.
- **B:** Correct. A private address reachable from the VPC without a proxy process. In this case: A private address keeps every client on the internal path.
- **C:** Incorrect for this question. A reachable address that requires encrypted connections from any client. Why the correct answer wins: A private address keeps every client on the internal path.
- **D:** Incorrect for this question. A private endpoint that consumes a published service without peering. Why the correct answer wins: A private address keeps every client on the internal path.

### Question 84 — B

Answer: Raise the database connection ceiling by flag. Capping the tenant's sessions leaves capacity for the other tenants. Change the engine-level connection limit without resizing the machine. Local study-map skill 4.1 (Connecting to Datastores), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 4 (integrating applications with Google Cloud services): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Allow the process the headroom it needs so it is not throttled or killed. Why the correct answer wins: Capping the tenant's sessions leaves capacity for the other tenants.
- **B:** Correct. Change the engine-level connection limit without resizing the machine. In this case: Capping the tenant's sessions leaves capacity for the other tenants.
- **C:** Incorrect for this question. Keep a small set of warm connections instead of opening one per request. Why the correct answer wins: Capping the tenant's sessions leaves capacity for the other tenants.
- **D:** Incorrect for this question. A private endpoint that consumes a published service without peering. Why the correct answer wins: Capping the tenant's sessions leaves capacity for the other tenants.

### Question 85 — D

Answer: Publish the event to a Pub/Sub topic. A topic fans the event to subscribers the publisher never names. A durable, at-least-once message channel with independent subscribers. Local study-map skill 4.2 (Publishing and Consuming Messages), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 4 (integrating applications with Google Cloud services): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A task queue with retries and rate control aimed at a specific target. Why the correct answer wins: A topic fans the event to subscribers the publisher never names.
- **B:** Incorrect for this question. A stateful sequence of service calls with retries and error branches. Why the correct answer wins: A topic fans the event to subscribers the publisher never names.
- **C:** Incorrect for this question. A trigger path that turns a Cloud Audit Log or resource event into a delivery. Why the correct answer wins: A topic fans the event to subscribers the publisher never names.
- **D:** Correct. A durable, at-least-once message channel with independent subscribers. In this case: A topic fans the event to subscribers the publisher never names.

### Question 86 — C

Answer: Add a dead-letter topic. A dead-letter topic parks the message that keeps failing. Hold messages that exhausted their delivery attempts for later inspection. Local study-map skill 4.2 (Publishing and Consuming Messages), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 4 (integrating applications with Google Cloud services): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. The consumer controls the pace and acknowledges messages itself. Why the correct answer wins: A dead-letter topic parks the message that keeps failing.
- **B:** Incorrect for this question. Recognise a repeated delivery and skip the duplicate work. Why the correct answer wins: A dead-letter topic parks the message that keeps failing.
- **C:** Correct. Hold messages that exhausted their delivery attempts for later inspection. In this case: A dead-letter topic parks the message that keeps failing.
- **D:** Incorrect for this question. Space out repeated attempts so a throttled quota can recover instead of being hammered. Why the correct answer wins: A dead-letter topic parks the message that keeps failing.

### Question 87 — A

Answer: Make the handler idempotent with a deduplication key. An idempotency key lets the repeat be recognised and skipped. Recognise a repeated delivery and skip the duplicate work. Local study-map skill 4.2 (Publishing and Consuming Messages), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 4 (integrating applications with Google Cloud services): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Correct. Recognise a repeated delivery and skip the duplicate work. In this case: An idempotency key lets the repeat be recognised and skipped.
- **B:** Incorrect for this question. Push each message to an endpoint instead of having the consumer pull. Why the correct answer wins: An idempotency key lets the repeat be recognised and skipped.
- **C:** Incorrect for this question. Space out repeated attempts so a throttled quota can recover instead of being hammered. Why the correct answer wins: An idempotency key lets the repeat be recognised and skipped.
- **D:** Incorrect for this question. Hold messages that exhausted their delivery attempts for later inspection. Why the correct answer wins: An idempotency key lets the repeat be recognised and skipped.

### Question 88 — B

Answer: Use a BigQuery subscription on the topic. A subscription writing to the table removes the consumer service. Write topic messages straight into a table without a consumer. Local study-map skill 4.2 (Publishing and Consuming Messages), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 4 (integrating applications with Google Cloud services): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. The consumer controls the pace and acknowledges messages itself. Why the correct answer wins: A subscription writing to the table removes the consumer service.
- **B:** Correct. Write topic messages straight into a table without a consumer. In this case: A subscription writing to the table removes the consumer service.
- **C:** Incorrect for this question. Load a periodic extract rather than a continuous stream. Why the correct answer wins: A subscription writing to the table removes the consumer service.
- **D:** Incorrect for this question. Durable object storage addressed by name rather than a database row. Why the correct answer wins: A subscription writing to the table removes the consumer service.

### Question 89 — C

Answer: Retry with exponential backoff and jitter. Waiting longer between attempts survives the short throttle. Space out repeated attempts so a throttled quota can recover instead of being hammered. Local study-map skill 4.3 (Calling Google Cloud APIs), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 4 (integrating applications with Google Cloud services): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Bound how many calls a plan allows in a window. Why the correct answer wins: Waiting longer between attempts survives the short throttle.
- **B:** Incorrect for this question. Allow the process the headroom it needs so it is not throttled or killed. Why the correct answer wins: Waiting longer between attempts survives the short throttle.
- **C:** Correct. Space out repeated attempts so a throttled quota can recover instead of being hammered. In this case: Waiting longer between attempts survives the short throttle.
- **D:** Incorrect for this question. Reduce per-call overhead when the API supports a batch surface. Why the correct answer wins: Waiting longer between attempts survives the short throttle.

### Question 90 — C

Answer: Follow the page token until results are exhausted. Following the page tokens collects the remaining rows. Request each page in turn so a truncated response is completed rather than assumed whole. Local study-map skill 4.3 (Calling Google Cloud APIs), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 4 (integrating applications with Google Cloud services): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Trim the response payload so latency and cost follow actual use. Why the correct answer wins: Following the page tokens collects the remaining rows.
- **B:** Incorrect for this question. Reduce per-call overhead when the API supports a batch surface. Why the correct answer wins: Following the page tokens collects the remaining rows.
- **C:** Correct. Request each page in turn so a truncated response is completed rather than assumed whole. In this case: Following the page tokens collects the remaining rows.
- **D:** Incorrect for this question. Reuse a result that has not changed, avoiding an identical call. Why the correct answer wins: Following the page tokens collects the remaining rows.

### Question 91 — D

Answer: Request only the fields the caller needs. A field mask trims the item to the two values shown. Trim the response payload so latency and cost follow actual use. Local study-map skill 4.3 (Calling Google Cloud APIs), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 4 (integrating applications with Google Cloud services): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Reduce per-call overhead when the API supports a batch surface. Why the correct answer wins: A field mask trims the item to the two values shown.
- **B:** Incorrect for this question. Request each page in turn so a truncated response is completed rather than assumed whole. Why the correct answer wins: A field mask trims the item to the two values shown.
- **C:** Incorrect for this question. Reuse a result that has not changed, avoiding an identical call. Why the correct answer wins: A field mask trims the item to the two values shown.
- **D:** Correct. Trim the response payload so latency and cost follow actual use. In this case: A field mask trims the item to the two values shown.

### Question 92 — D

Answer: Cache the response for its freshness window. Caching the catalogue avoids the repeated request. Reuse a result that has not changed, avoiding an identical call. Local study-map skill 4.3 (Calling Google Cloud APIs), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 4 (integrating applications with Google Cloud services): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Change the engine-level connection limit without resizing the machine. Why the correct answer wins: Caching the catalogue avoids the repeated request.
- **B:** Incorrect for this question. Space out repeated attempts so a throttled quota can recover instead of being hammered. Why the correct answer wins: Caching the catalogue avoids the repeated request.
- **C:** Incorrect for this question. Request each page in turn so a truncated response is completed rather than assumed whole. Why the correct answer wins: Caching the catalogue avoids the repeated request.
- **D:** Correct. Reuse a result that has not changed, avoiding an identical call. In this case: Caching the catalogue avoids the repeated request.

### Question 93 — A, B

Answers: Give the workload its own service account; Federate the external identity with Workload Identity Federation. A dedicated identity per job attributes each action, and federation removes the stored key. A dedicated identity whose roles can be granted and revoked independently. Exchange an outside token for a short-lived Google credential. Local study-map skill 4.4 (Service Accounts for API Calls), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 4 (integrating applications with Google Cloud services): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Correct. A dedicated identity whose roles can be granted and revoked independently. In this case: A dedicated identity per job attributes each action, and federation removes the stored key.
- **B:** Correct. Exchange an outside token for a short-lived Google credential. In this case: A dedicated identity per job attributes each action, and federation removes the stored key.
- **C:** Incorrect for this question. The automatically created identity that usually carries broad project access. Why the correct answer wins: A dedicated identity per job attributes each action, and federation removes the stored key.
- **D:** Incorrect for this question. A legacy broad role that can change most resources in the project. Why the correct answer wins: A dedicated identity per job attributes each action, and federation removes the stored key.
- **E:** Incorrect for this question. A long-lived credential that has to be stored and rotated by hand. Why the correct answer wins: A dedicated identity per job attributes each action, and federation removes the stored key.

### Question 94 — C

Answer: Rely on Application Default Credentials. Application Default Credentials pick up the developer's identity. Let the client library find credentials from the environment. Local study-map skill 4.4 (Service Accounts for API Calls), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 4 (integrating applications with Google Cloud services): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. The automatically created identity that usually carries broad project access. Why the correct answer wins: Application Default Credentials pick up the developer's identity.
- **B:** Incorrect for this question. A dedicated identity whose roles can be granted and revoked independently. Why the correct answer wins: Application Default Credentials pick up the developer's identity.
- **C:** Correct. Let the client library find credentials from the environment. In this case: Application Default Credentials pick up the developer's identity.
- **D:** Incorrect for this question. A long-lived credential that has to be stored and rotated by hand. Why the correct answer wins: Application Default Credentials pick up the developer's identity.

### Question 95 — A

Answer: Emit structured JSON logs. Structured fields make the entries filterable by tenant and request. Emit fields the log viewer can index so queries and alerts are possible. Local study-map skill 4.5 (Metrics, Logs, and Traces), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 4 (integrating applications with Google Cloud services): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Correct. Emit fields the log viewer can index so queries and alerts are possible. In this case: Structured fields make the entries filterable by tenant and request.
- **B:** Incorrect for this question. Turn a recurring log pattern into a number that can be charted and alerted on. Why the correct answer wins: Structured fields make the entries filterable by tenant and request.
- **C:** Incorrect for this question. Let filters and alerting distinguish routine output from errors. Why the correct answer wins: Structured fields make the entries filterable by tenant and request.
- **D:** Incorrect for this question. Group and count application errors instead of grepping logs. Why the correct answer wins: Structured fields make the entries filterable by tenant and request.

### Question 96 — D

Answer: Emit a custom metric from the code. A user-defined metric carries the ratio that nothing emits. Publish an application signal that infrastructure metrics cannot see. Local study-map skill 4.5 (Metrics, Logs, and Traces), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 4 (integrating applications with Google Cloud services): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Turn a recurring log pattern into a number that can be charted and alerted on. Why the correct answer wins: A user-defined metric carries the ratio that nothing emits.
- **B:** Incorrect for this question. Let filters and alerting distinguish routine output from errors. Why the correct answer wins: A user-defined metric carries the ratio that nothing emits.
- **C:** Incorrect for this question. Notify a human when a threshold is crossed. Why the correct answer wins: A user-defined metric carries the ratio that nothing emits.
- **D:** Correct. Publish an application signal that infrastructure metrics cannot see. In this case: A user-defined metric carries the ratio that nothing emits.

### Question 97 — B

Answer: Create an alerting policy on the metric. An alert policy on the metric notifies the rotation at the threshold. Notify a human when a threshold is crossed. Local study-map skill 4.5 (Metrics, Logs, and Traces), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 4 (integrating applications with Google Cloud services): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Publish an application signal that infrastructure metrics cannot see. Why the correct answer wins: An alert policy on the metric notifies the rotation at the threshold.
- **B:** Correct. Notify a human when a threshold is crossed. In this case: An alert policy on the metric notifies the rotation at the threshold.
- **C:** Incorrect for this question. Page on the rate at which reliability is being spent. Why the correct answer wins: An alert policy on the metric notifies the rotation at the threshold.
- **D:** Incorrect for this question. Let filters and alerting distinguish routine output from errors. Why the correct answer wins: An alert policy on the metric notifies the rotation at the threshold.

### Question 98 — D

Answer: Send the exception to Error Reporting. Grouping exceptions makes the new groups visible after the release. Group and count application errors instead of grepping logs. Local study-map skill 4.6 (Error Reporting and Trace Correlation), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 4 (integrating applications with Google Cloud services): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Turn a recurring log pattern into a number that can be charted and alerted on. Why the correct answer wins: Grouping exceptions makes the new groups visible after the release.
- **B:** Incorrect for this question. Notify a human when a threshold is crossed. Why the correct answer wins: Grouping exceptions makes the new groups visible after the release.
- **C:** Incorrect for this question. Read variable state in a running deployment without redeploying. Why the correct answer wins: Grouping exceptions makes the new groups visible after the release.
- **D:** Correct. Group and count application errors instead of grepping logs. In this case: Grouping exceptions makes the new groups visible after the release.

### Question 99 — D

Answer: Propagate the trace ID between services. Propagating the trace header joins the four services into one view. Join spans from different services into one trace. Local study-map skill 4.6 (Error Reporting and Trace Correlation), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 4 (integrating applications with Google Cloud services): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Let filters and alerting distinguish routine output from errors. Why the correct answer wins: Propagating the trace header joins the four services into one view.
- **B:** Incorrect for this question. Emit fields the log viewer can index so queries and alerts are possible. Why the correct answer wins: Propagating the trace header joins the four services into one view.
- **C:** Incorrect for this question. Read variable state in a running deployment without redeploying. Why the correct answer wins: Propagating the trace header joins the four services into one view.
- **D:** Correct. Join spans from different services into one trace. In this case: Propagating the trace header joins the four services into one view.

### Question 100 — B

Answer: Ask Gemini Cloud Assist for a diagnosis. An AI assistant summarises the alert context and likely cause. An assistant that reads telemetry and proposes a cause and a next step. Local study-map skill 4.7 (AI-Assisted Observability), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 4 (integrating applications with Google Cloud services): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Generate a first draft from context, then review and correct it. Why the correct answer wins: An AI assistant summarises the alert context and likely cause.
- **B:** Correct. An assistant that reads telemetry and proposes a cause and a next step. In this case: An AI assistant summarises the alert context and likely cause.
- **C:** Incorrect for this question. Give the assistant a defined tool surface instead of pasting context by hand. Why the correct answer wins: An AI assistant summarises the alert context and likely cause.
- **D:** Incorrect for this question. Group and count application errors instead of grepping logs. Why the correct answer wins: An AI assistant summarises the alert context and likely cause.
