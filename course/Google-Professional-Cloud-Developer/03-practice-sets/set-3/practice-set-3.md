# Google Cloud Professional Cloud Developer — Full-Length Mock Exam 3

Professional Cloud Developer · 100 questions · expanded practice bank · passing score not published

Blueprint-weighted mock exam. Item mix: 84 multiple-choice and 16 multiple-select items (the selection count is stated in each multi-select stem). The live exam publishes 50-60 multiple-choice and multiple-select questions and has no case-study component, so this set is larger on purpose and no case-study item is reproduced. The live paper allows two hours for 50-60 items, so this 100-item set is a slower-per-item rehearsal: about 72 seconds per item here against roughly 120-144 seconds live. Use it to build a habit of finishing with time to review. See the README for the exact fidelity boundary.

Original educational content, not actual, recalled, or copied Google exam items.

## Questions

---

## Domain 1 — Designing Highly Scalable, Secure, and Reliable Cloud-Native Applications (Compute Choice, APIs, and Secure Design)

### 1. A team must run two services that share a private network and a custom autoscaling policy per service. Which two platforms fit? Select two.

- A. Deploy the handler as a Cloud Functions function
- B. Deploy to App Engine standard
- C. Deploy the service to Cloud Run
- D. Deploy the workload to Google Kubernetes Engine
- E. Run the application on Compute Engine instances

### 2. An existing service already runs on a supported language runtime, and the team wants platform-managed scaling with no container work. Which platform fits?

- A. Deploy to App Engine standard
- B. Deploy the service to Cloud Run
- C. Run the application on Compute Engine instances
- D. Deploy the workload to Google Kubernetes Engine

### 3. A workload needs a GPU-attached driver version the managed runtimes do not control. Which platform fits?

- A. Run the application on Compute Engine instances
- B. Deploy the service to Cloud Run
- C. Deploy to App Engine standard
- D. Deploy the workload to Google Kubernetes Engine

### 4. A team must prove that staging and production run the same dependencies and the same binary. What should be promoted?

- A. Run the application on Compute Engine instances
- B. Package the monolith into a container image
- C. Deploy the handler as a Cloud Functions function
- D. Deploy from source and let the platform build it

### 5. A contract requires the service to keep serving if an entire region becomes unavailable. Which design fits?

- A. Deploy the service in two regions behind a global load balancer
- B. Buy committed use discounts for the steady baseline
- C. Deploy in one region across multiple zones
- D. Place the workload in a single zone

### 6. A workload must tolerate a zone failure but its data cannot leave the country. Which design fits?

- A. Serve static content from Cloud CDN
- B. Deploy in one region across multiple zones
- C. Place the workload in a single zone
- D. Deploy the service in two regions behind a global load balancer

### 7. A legacy service loads a customer's files into instance memory for the duration of a session. What should be enabled until it is refactored?

- A. Store session state in a shared datastore
- B. Serve static content from Cloud CDN
- C. Enable session affinity on the backend service
- D. Use a generated cookie for stickiness

### 8. A service is reachable on three continents and must stop routing to a broken backend. Which two components fit? Select two.

- A. Put a global external Application Load Balancer in front
- B. Add a health check endpoint to the backend service
- C. Use a regional load balancer
- D. Serve static content from Cloud CDN
- E. Enable session affinity on the backend service

### 9. A leaderboard must serve sub-millisecond reads for the same top hundred entries to every user. What should the team add?

- A. Load through a cache-aside pattern
- B. Serve static content from Cloud CDN
- C. Cache reads in Memorystore
- D. Cache inside each instance process

### 10. A single-page app re-downloads the same static bundle on every visit from a distant country. What should be added?

- A. Serve static content from Cloud CDN
- B. Cache inside each instance process
- C. Cache reads in Memorystore
- D. Load through a cache-aside pattern

### 11. An external team needs to call the service over plain HTTP and to generate a client from a published contract. Which two choices fit? Select two.

- A. Batch many small calls into one request
- B. Serve gRPC-Web for browser clients
- C. Expose a gRPC service
- D. Expose a REST API with JSON payloads
- E. Publish an OpenAPI specification

### 12. Two services exchange millions of small binary messages per hour and need generated stubs in four languages. Which interface fits?

- A. Expose a REST API with JSON payloads
- B. Expose a gRPC service
- C. Publish an OpenAPI specification
- D. Serve gRPC-Web for browser clients

### 13. One integration partner's retry loop is consuming most of the API capacity. What should be added?

- A. Use API Gateway for the API
- B. Introduce a new API version alongside the old one
- C. Apply a rate limit per client key
- D. Set a quota per API key

### 14. A field must be renamed, and clients in the wild parse the old name strictly. What should the team do?

- A. Add the field in a backward-compatible way
- B. Publish an OpenAPI specification
- C. Introduce a new API version alongside the old one
- D. Put Apigee in front of the API

### 15. A workflow must start when a database export finishes and must call a slow partner once per row. Which two services fit? Select two.

- A. Publish the event to a Pub/Sub topic
- B. Route the event with Eventarc
- C. Queue the work as a Cloud Tasks task
- D. Schedule the invocation with Cloud Scheduler
- E. Have the worker pull from the subscription

### 16. A service must emit an event that five independent teams consume on their own schedules. What should it publish to?

- A. Orchestrate the steps in Workflows
- B. Schedule the invocation with Cloud Scheduler
- C. Publish the event to a Pub/Sub topic
- D. Queue the work as a Cloud Tasks task

### 17. Pods reserve eight CPUs each while measurement shows six hundred millicores at peak. What should the team change?

- A. Set CPU and memory requests from measured use
- B. Buy committed use discounts for the steady baseline
- C. Cap the maximum instance count
- D. Raise the container limits above the observed peak

### 18. A worker holds an open connection to a queue all day and serves no requests. Which billing mode fits?

- A. Keep a minimum number of instances warm
- B. Buy committed use discounts for the steady baseline
- C. Use instance-based billing
- D. Use request-based billing

### 19. QA must reach the new revision through the production hostname while users stay on the old one. What should the team configure?

- A. Route by revision tag or header
- B. Split traffic between revisions by percentage
- C. Canary the release at a small percentage first
- D. Gate the change behind a feature flag

### 20. A behaviour must be switchable per customer without a deployment. What should the team use?

- A. Split traffic between revisions by percentage
- B. Shift traffic back to the previous revision
- C. Canary the release at a small percentage first
- D. Gate the change behind a feature flag

### 21. Four services must run in a defined order with a compensating step if the third fails. What should the team use?

- A. Orchestrate the steps in Workflows
- B. Queue the work as a Cloud Tasks task
- C. Publish the event to a Pub/Sub topic
- D. Schedule the invocation with Cloud Scheduler

### 22. Temporary exports must disappear after thirty days without a scheduled job. What should be configured?

- A. Add a lifecycle rule to the bucket
- B. Lock the bucket retention policy
- C. Issue a signed URL with a short expiry
- D. Make the bucket public

### 23. A leaked credential must be revocable without rebuilding the image. What should hold the value?

- A. Download a service account key file
- B. Use a customer-managed encryption key
- C. Set the credential as an environment variable
- D. Store the credential in Secret Manager

### 24. A review finds one long-lived key with broad permissions used by three services. Which two changes fix it? Select two.

- A. Grant the basic editor role
- B. Download a service account key file
- C. Rotate the secret on a schedule
- D. Set the credential as an environment variable
- E. Grant only the roles the workload needs

### 25. A consumer app needs sign-up, sign-in and token refresh for its own users. What should the team use?

- A. Use Identity Platform for end-user sign-in
- B. Give the workload its own service account
- C. Rely on Application Default Credentials
- D. Put Identity-Aware Proxy in front of the service

### 26. A developer's local run must pick up their own credentials without any code change. Which mechanism applies?

- A. Federate the external identity with Workload Identity Federation
- B. Bind a Kubernetes service account to a Google service account
- C. Rely on Application Default Credentials
- D. Download a service account key file

### 27. An internal tool must be reachable only by staff with the right group membership, before any request reaches the app. What should be added?

- A. Apply a Kubernetes NetworkPolicy
- B. Put Identity-Aware Proxy in front of the service
- C. Allow unauthenticated invocations
- D. Set a namespace resource quota

### 28. A managed runtime must reach a private database and a published partner service with no internet path. Which two mechanisms fit? Select two.

- A. Reach the service through Private Service Connect
- B. Put Identity-Aware Proxy in front of the service
- C. Send traffic through Direct VPC egress
- D. Allow unauthenticated invocations
- E. Make the bucket public

### 29. A reporting job writes one hundred gigabytes of compressed archives each night that are read rarely. Which store fits?

- A. Store the ledger in Spanner
- B. Store the objects in Cloud Storage
- C. Use Firestore in Native mode
- D. Cache reads in Memorystore

### 30. A session tier must answer lookups in under a millisecond and can rebuild from the source of truth. Which store fits?

- A. Store the objects in Cloud Storage
- B. Design the row key for the read pattern
- C. Cache reads in Memorystore
- D. Store the ledger in Spanner

### 31. A partner must read one object for fifteen minutes and nothing else. What should the service issue?

- A. Make the bucket public
- B. Add a lifecycle rule to the bucket
- C. Lock the bucket retention policy
- D. Issue a signed URL with a short expiry

### 32. A recommendation model must train on rows that include the last five minutes of behaviour. What should the pipeline do?

- A. Store the objects in Cloud Storage
- B. Export the batch to BigQuery
- C. Store the ledger in Spanner
- D. Stream the events into BigQuery

---

## Domain 2 — Building and Testing Applications (Development Environments, Builds, and Tests)

### 33. A developer must validate Firestore security rules and queries with no project and no bill. What should they use?

- A. Use Cloud Shell for the session
- B. Develop with Cloud Code in the IDE
- C. Use Cloud Workstations for the environment
- D. Run the service emulator locally

### 34. A team must give every engineer the same editor, SDK and container tooling from a defined image. What should it provide?

- A. Use Cloud Shell for the session
- B. Run the service emulator locally
- C. Develop with Cloud Code in the IDE
- D. Use Cloud Workstations for the environment

### 35. A message handler must be proven against the broker's acknowledgement semantics, not a stub. What test kind is needed?

- A. Add a unit test with dependencies stubbed
- B. Run an integration test against the emulator
- C. Load-test the release before the rollout
- D. Run the service emulator locally

### 36. A developer wants to debug in the editor and let the assistant call project tools through defined interfaces. Which two fit? Select two.

- A. Connect the assistant to an MCP server
- B. Use Cloud Workstations for the environment
- C. Use Cloud Shell for the session
- D. Develop with Cloud Code in the IDE
- E. Run the service emulator locally

### 37. A team must generate a first draft of forty unit tests for review. What should they use?

- A. Ask Gemini Cloud Assist for a diagnosis
- B. Use an AI coding assistant to draft the tests
- C. Connect the assistant to an MCP server
- D. Develop with Cloud Code in the IDE

### 38. A developer on a cluster service wants the same fast rebuild loop they had locally. What should they use?

- A. Iterate with Skaffold
- B. Deploy a pinned image digest
- C. Keep building the image by hand
- D. Build the image with Cloud Build

### 39. Builds must run in a clean, reproducible environment rather than on someone's laptop. What should the team use?

- A. Build the image with Cloud Build
- B. Use Cloud Shell for the session
- C. Keep building the image by hand
- D. Develop with Cloud Code in the IDE

### 40. A pull request must produce a build that reviewers can inspect before merge. What should be configured?

- A. Keep building the image by hand
- B. Queue the work as a Cloud Tasks task
- C. Schedule the invocation with Cloud Scheduler
- D. Trigger the build from a repository push

### 41. Two deployments were made from the same tag and produced different binaries. What should the team change?

- A. Deploy from source and let the platform build it
- B. Package the monolith into a container image
- C. Deploy a pinned image digest
- D. Build the image with Cloud Build

### 42. A team must store images per environment with separate access and build them from declared steps. Which two fit? Select two.

- A. Build the image with Cloud Build
- B. Use Cloud Shell for the session
- C. Develop with Cloud Code in the IDE
- D. Push the image to Artifact Registry
- E. Push the image to Container Registry

### 43. An audit asks for evidence that image access is scoped per repository rather than per project. Which registry answers that?

- A. Push the image to Artifact Registry
- B. Store the objects in Cloud Storage
- C. Push the image to Container Registry
- D. Build the image with Cloud Build

### 44. A team wants scanning results and regional pulls tied to the repository that holds the image. Which service fits?

- A. Build the image with Cloud Build
- B. Push the image to Artifact Registry
- C. Store the objects in Cloud Storage
- D. Push the image to Container Registry

### 45. Threat-model documents must be versioned beside the release and kept after the images are gone. Where should they live?

- A. Build the image with Cloud Build
- B. Push the image to Container Registry
- C. Store the objects in Cloud Storage
- D. Push the image to Artifact Registry

### 46. A base image gains a critical vulnerability and every dependent image must be identified. What should be used?

- A. Enforce admission with Binary Authorization
- B. Review the finding in Security Command Center
- C. Generate build provenance in Cloud Build
- D. Scan the image with Artifact Analysis

### 47. A cluster must refuse any image that was not built by the approved pipeline. What should be enforced?

- A. Generate build provenance in Cloud Build
- B. Scan the image with Artifact Analysis
- C. Review the finding in Security Command Center
- D. Enforce admission with Binary Authorization

### 48. A customer contract demands a documented, verifiable supply-chain level for each release. What should be required?

- A. Scan the image with Artifact Analysis
- B. Generate build provenance in Cloud Build
- C. Enforce admission with Binary Authorization
- D. Require a higher supply-chain level before release

### 49. A currency formatter has nine edge cases and each must fail with its own name. What should be added?

- A. Add a unit test with dependencies stubbed
- B. Load-test the release before the rollout
- C. Run an integration test against the emulator
- D. Quarantine the flaky test and fix it

### 50. A timing-dependent test fails one run in six and the team has started ignoring red builds. What should be done?

- A. Quarantine the flaky test and fix it
- B. Run an integration test against the emulator
- C. Add a unit test with dependencies stubbed
- D. Block the deploy on the test result

### 51. A team wants fast, isolated tests and a rule that a failing suite blocks the release. Which two choices fit? Select two.

- A. Run an integration test against the emulator
- B. Add a unit test with dependencies stubbed
- C. Load-test the release before the rollout
- D. Block the deploy on the test result
- E. Quarantine the flaky test and fix it

### 52. A producer and consumer disagree about the message envelope only when connected for real. Which test would catch it?

- A. Load-test the release before the rollout
- B. Run the service emulator locally
- C. Add a unit test with dependencies stubbed
- D. Run an integration test against the emulator

### 53. The suite exists but runs only when someone remembers. What should the pipeline do?

- A. Quarantine the flaky test and fix it
- B. Run the tests as a Cloud Build step
- C. Load-test the release before the rollout
- D. Block the deploy on the test result

### 54. A service must be exercised against real broker and storage behaviour on every merge. Which two choices fit? Select two.

- A. Block the deploy on the test result
- B. Add a unit test with dependencies stubbed
- C. Load-test the release before the rollout
- D. Run an integration test against the emulator
- E. Run the tests as a Cloud Build step

### 55. A release must be proven at the traffic expected for the holiday peak. What should the team run?

- A. Add a unit test with dependencies stubbed
- B. Load-test the release before the rollout
- C. Profile the service with Cloud Profiler
- D. Run an integration test against the emulator

---

## Domain 3 — Configuring Cloud-Native Applications for Deployment (Cloud Run and GKE Deployment Configuration)

### 56. A team has a repository without a Dockerfile and a Java service that times out before it answers its first request. Which two settings fit? Select two.

- A. Raise the per-instance concurrency limit
- B. Keep building the image by hand
- C. Package the monolith into a container image
- D. Deploy from source and let the platform build it
- E. Raise CPU during start-up only

### 57. A Cloud Run service reports instance-level interference under load even though CPU stays under the limit. What should be changed?

- A. Cap the maximum instance count
- B. Scale pods on CPU utilization
- C. Raise the container limits above the observed peak
- D. Raise the per-instance concurrency limit

### 58. A nightly batch must run to completion once and then stop consuming resources. Which runtime fits?

- A. Deploy the service to Cloud Run
- B. Schedule the invocation with Cloud Scheduler
- C. Run the batch work as a Cloud Run job
- D. Deploy the handler as a Cloud Functions function

### 59. A service must react when a new object lands in a bucket, without polling. What should it use?

- A. Schedule the invocation with Cloud Scheduler
- B. Route the event with Eventarc
- C. Publish the event to a Pub/Sub topic
- D. Orchestrate the steps in Workflows

### 60. A request handler must receive queued messages at an HTTPS endpoint without running a subscriber loop. Which delivery fits?

- A. Have the worker pull from the subscription
- B. Route the event with Eventarc
- C. Queue the work as a Cloud Tasks task
- D. Deliver to an HTTPS push subscription

### 61. A service must receive a signed request every morning at six. What should be used?

- A. Route the event with Eventarc
- B. Orchestrate the steps in Workflows
- C. Schedule the invocation with Cloud Scheduler
- D. Queue the work as a Cloud Tasks task

### 62. A service must be reachable only from inside the network and must keep each instance to one in-flight request. Which two settings fit? Select two.

- A. Put a global external Application Load Balancer in front
- B. Allow unauthenticated invocations
- C. Cap the maximum instance count
- D. Restrict ingress to internal traffic
- E. Raise the per-instance concurrency limit

### 63. A payment service must answer within two hundred milliseconds after a long idle period. What should be configured?

- A. Raise CPU during start-up only
- B. Keep a minimum number of instances warm
- C. Cap the maximum instance count
- D. Use request-based billing

### 64. A runaway client must not be able to scale the service past the budgeted ceiling. What should be set?

- A. Use instance-based billing
- B. Keep a minimum number of instances warm
- C. Cap the maximum instance count
- D. Raise the container limits above the observed peak

### 65. A small team must publish three internal APIs with key checks and no custom proxy code. Which service fits?

- A. Restrict ingress to internal traffic
- B. Put Apigee in front of the API
- C. Use API Gateway for the API
- D. Put a global external Application Load Balancer in front

### 66. A monetised partner API needs per-developer quotas, analytics and product packaging. Which service fits?

- A. Deploy the service to Cloud Run
- B. Put a global external Application Load Balancer in front
- C. Put Apigee in front of the API
- D. Use API Gateway for the API

### 67. A deployment must keep capacity during a release and never drop more than a quarter of the pods. Which two settings fit? Select two.

- A. Use a rolling update strategy
- B. Constrain pods to the intended node pool
- C. Run the batch node pool on Spot VMs
- D. Add a PodDisruptionBudget
- E. Tune maxSurge and maxUnavailable

### 68. A cluster in another region must pull images without crossing the internet and without project-wide read access. What should it use?

- A. Push the image to Artifact Registry
- B. Push the image to Container Registry
- C. Build the image with Cloud Build
- D. Store the objects in Cloud Storage

### 69. A fault-tolerant batch pool should cost as little as possible per node hour. What should the pool use?

- A. Enable node pool autoscaling
- B. Run the batch node pool on Spot VMs
- C. Constrain pods to the intended node pool
- D. Buy committed use discounts for the steady baseline

### 70. A slow-starting service is restarted in a loop and receives traffic before it is ready. Which two probes fix it? Select two.

- A. Configure a startup probe
- B. Tune maxSurge and maxUnavailable
- C. Configure a readiness probe
- D. Use a rolling update strategy
- E. Configure a liveness probe

### 71. A container hangs without exiting and stops answering while still running. Which probe recovers it?

- A. Add a PodDisruptionBudget
- B. Configure a liveness probe
- C. Configure a readiness probe
- D. Configure a startup probe

### 72. Pods must scale on queue depth rather than CPU, because the work is I/O bound. What should be used?

- A. Scale pods on a custom or external metric
- B. Enable node pool autoscaling
- C. Scale pods on CPU utilization
- D. Buy committed use discounts for the steady baseline

### 73. A service must never scale to zero during business hours even when idle. What should be set?

- A. Set a minimum replica count
- B. Add a PodDisruptionBudget
- C. Cap the maximum instance count
- D. Enable node pool autoscaling

### 74. A CPU-bound parser must add pods as utilisation climbs. Which autoscaler setting fits?

- A. Set a minimum replica count
- B. Enable node pool autoscaling
- C. Scale pods on CPU utilization
- D. Scale pods on a custom or external metric

### 75. A source deploy must run a native compile step that the detected buildpack does not perform. What should the team add?

- A. Raise CPU during start-up only
- B. Raise the per-instance concurrency limit
- C. Build the image with Cloud Build
- D. Cap the maximum instance count

### 76. An event receiver cannot finish the downstream write inside the delivery deadline. What should it do?

- A. Deliver to an HTTPS push subscription
- B. Route the event with Eventarc
- C. Queue the work as a Cloud Tasks task
- D. Schedule the invocation with Cloud Scheduler

### 77. A service does follow-up work after sending the response and is throttled once the response leaves. What should be configured?

- A. Enable CPU boost at startup
- B. Keep a minimum number of instances warm
- C. Use instance-based billing
- D. Raise the per-instance concurrency limit

### 78. Pods stay pending because the cluster has no free node capacity. What should be configured?

- A. Enable node pool autoscaling
- B. Run the batch node pool on Spot VMs
- C. Buy committed use discounts for the steady baseline
- D. Scale pods on CPU utilization

### 79. Nightly node maintenance must never remove more than two of five API pods at once. What should be defined?

- A. Tune maxSurge and maxUnavailable
- B. Configure a startup probe
- C. Configure a liveness probe
- D. Add a PodDisruptionBudget

---

## Domain 4 — Integrating Applications with Google Cloud Services (Data, Messaging, APIs, and Observability)

### 80. A service opens a new database connection per request and reaches the instance over a public address. Which two changes fix it? Select two.

- A. Pool and reuse database connections
- B. Connect through the Cloud SQL Auth Proxy
- C. Connect over the database private IP
- D. Expose the database on a public address with enforced SSL
- E. Use the language connector with IAM

### 81. A Python service must connect with IAM credentials and no sidecar process. What should it use?

- A. Use the language connector with IAM
- B. Connect over the database private IP
- C. Connect through the Cloud SQL Auth Proxy
- D. Raise the database connection ceiling by flag

### 82. A cluster requires connections to arrive through an authenticated proxy with automatic certificate handling. What should be deployed?

- A. Connect through the Cloud SQL Auth Proxy
- B. Connect through the AlloyDB Auth Proxy
- C. Use the language connector with IAM
- D. Reach the service through Private Service Connect

### 83. A compliance rule forbids a database instance from owning a public address. What should the team do?

- A. Reach the service through Private Service Connect
- B. Expose the database on a public address with enforced SSL
- C. Connect over the database private IP
- D. Connect through the Cloud SQL Auth Proxy

### 84. A consumer must control its own pacing and acknowledge in batches. Which delivery fits?

- A. Route the event with Eventarc
- B. Have the worker pull from the subscription
- C. Deliver to an HTTPS push subscription
- D. Queue the work as a Cloud Tasks task

### 85. A malformed message is redelivered forever and blocks the queue. What should be configured?

- A. Lock the bucket retention policy
- B. Add a dead-letter topic
- C. Retry with exponential backoff and jitter
- D. Use a BigQuery subscription on the topic

### 86. Duplicate deliveries are creating two orders for one customer click. What should the consumer use?

- A. Request only the fields the caller needs
- B. Make the handler idempotent with a deduplication key
- C. Have the worker pull from the subscription
- D. Retry with exponential backoff and jitter

### 87. Events must land in an analytics table with no consumer code to run. Which subscription fits?

- A. Deliver to an HTTPS push subscription
- B. Stream the events into BigQuery
- C. Use a BigQuery subscription on the topic
- D. Have the worker pull from the subscription

### 88. An upstream returns resource-exhausted in short bursts and succeeds on a later attempt. What should the client add?

- A. Raise the container limits above the observed peak
- B. Batch many small calls into one request
- C. Set a quota per API key
- D. Retry with exponential backoff and jitter

### 89. A list call returns the first page and the client assumes it has everything. What should it implement?

- A. Batch many small calls into one request
- B. Follow the page token until results are exhausted
- C. Request only the fields the caller needs
- D. Cache the response for its freshness window

### 90. A list call downloads large payloads when only identifiers are needed. What should the client send?

- A. Cache the response for its freshness window
- B. Follow the page token until results are exhausted
- C. Batch many small calls into one request
- D. Request only the fields the caller needs

### 91. An options list changes daily but is fetched on every page load. What should the client do?

- A. Follow the page token until results are exhausted
- B. Request only the fields the caller needs
- C. Retry with exponential backoff and jitter
- D. Cache the response for its freshness window

### 92. The default compute identity holds editor, and a service needs only to write to one bucket. What should be created?

- A. Give the workload its own service account
- B. Let the workload use the default compute service account
- C. Grant the basic editor role
- D. Download a service account key file

### 93. A pipeline outside Google Cloud must call an API without storing a long-lived key. What should be configured?

- A. Download a service account key file
- B. Give the workload its own service account
- C. Rely on Application Default Credentials
- D. Federate the external identity with Workload Identity Federation

### 94. A service's logs cannot be filtered by severity and its latency cannot be attributed to a call. Which two changes fix it? Select two.

- A. Emit structured JSON logs
- B. Instrument a span around the downstream call
- C. Emit a custom metric from the code
- D. Create an alerting policy on the metric
- E. Build a log-based metric

### 95. A business ratio must be charted and alerted on, but nothing in the product emits it today. What should the team add?

- A. Create an alerting policy on the metric
- B. Build a log-based metric
- C. Alert on the error budget burn rate
- D. Emit a custom metric from the code

### 96. Thousands of stack traces arrive and the team cannot tell which are new. What should be enabled?

- A. Build a log-based metric
- B. Create an alerting policy on the metric
- C. Inspect the live process with Cloud Debugger
- D. Send the exception to Error Reporting

### 97. A request crosses four services and the logs cannot be joined into one timeline. What should the code do?

- A. Set the correct severity on each entry
- B. Propagate the trace ID between services
- C. Emit structured JSON logs
- D. Instrument a span around the downstream call

### 98. An on-call engineer must correlate a spike with recent changes and past incidents quickly. What should be used?

- A. Connect the assistant to an MCP server
- B. Ask Gemini Cloud Assist for a diagnosis
- C. Send the exception to Error Reporting
- D. Use an AI coding assistant to draft the tests

### 99. A fleet that scales to forty tasks exhausts the database's connection cap. What should be limited?

- A. Raise the database connection ceiling by flag
- B. Use the language connector with IAM
- C. Connect over the database private IP
- D. Connect through the AlloyDB Auth Proxy

### 100. Operators must be paged on worsening reliability rather than on raw CPU. What should be configured?

- A. Build a log-based metric
- B. Create an alerting policy on the metric
- C. Emit a custom metric from the code
- D. Alert on the error budget burn rate

---

## Answer key and explanations

### Question 1 — C, D

Answers: Deploy the service to Cloud Run; Deploy the workload to Google Kubernetes Engine. A managed container runtime covers the stateless service, and a Kubernetes control plane covers the workload that needs per-workload policy. A managed container runtime that scales to zero and bills per request while it serves traffic. A managed Kubernetes control plane where pods, node pools and cluster-scoped policy are yours to configure. Local study-map skill 1.1 (Compute Platform Selection), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 1 (designing highly scalable, secure, and reliable cloud-native applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. An event-triggered function runtime for a single-purpose handler rather than a long-lived service. Why the correct answer wins: A managed container runtime covers the stateless service, and a Kubernetes control plane covers the workload that needs per-workload policy.
- **B:** Incorrect for this question. A platform runtime that manages scaling for a supported language version and its sandbox limits. Why the correct answer wins: A managed container runtime covers the stateless service, and a Kubernetes control plane covers the workload that needs per-workload policy.
- **C:** Correct. A managed container runtime that scales to zero and bills per request while it serves traffic. In this case: A managed container runtime covers the stateless service, and a Kubernetes control plane covers the workload that needs per-workload policy.
- **D:** Correct. A managed Kubernetes control plane where pods, node pools and cluster-scoped policy are yours to configure. In this case: A managed container runtime covers the stateless service, and a Kubernetes control plane covers the workload that needs per-workload policy.
- **E:** Incorrect for this question. Virtual machines where the operating system, runtime and scaling group are all managed by the team. Why the correct answer wins: A managed container runtime covers the stateless service, and a Kubernetes control plane covers the workload that needs per-workload policy.

### Question 2 — A

Answer: Deploy to App Engine standard. A platform runtime manages scaling for the supported language without a container to build. A platform runtime that manages scaling for a supported language version and its sandbox limits. Local study-map skill 1.1 (Compute Platform Selection), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 1 (designing highly scalable, secure, and reliable cloud-native applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Correct. A platform runtime that manages scaling for a supported language version and its sandbox limits. In this case: A platform runtime manages scaling for the supported language without a container to build.
- **B:** Incorrect for this question. A managed container runtime that scales to zero and bills per request while it serves traffic. Why the correct answer wins: A platform runtime manages scaling for the supported language without a container to build.
- **C:** Incorrect for this question. Virtual machines where the operating system, runtime and scaling group are all managed by the team. Why the correct answer wins: A platform runtime manages scaling for the supported language without a container to build.
- **D:** Incorrect for this question. A managed Kubernetes control plane where pods, node pools and cluster-scoped policy are yours to configure. Why the correct answer wins: A platform runtime manages scaling for the supported language without a container to build.

### Question 3 — A

Answer: Run the application on Compute Engine instances. Virtual machines give the team control of the driver and the image. Virtual machines where the operating system, runtime and scaling group are all managed by the team. Local study-map skill 1.1 (Compute Platform Selection), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 1 (designing highly scalable, secure, and reliable cloud-native applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Correct. Virtual machines where the operating system, runtime and scaling group are all managed by the team. In this case: Virtual machines give the team control of the driver and the image.
- **B:** Incorrect for this question. A managed container runtime that scales to zero and bills per request while it serves traffic. Why the correct answer wins: Virtual machines give the team control of the driver and the image.
- **C:** Incorrect for this question. A platform runtime that manages scaling for a supported language version and its sandbox limits. Why the correct answer wins: Virtual machines give the team control of the driver and the image.
- **D:** Incorrect for this question. A managed Kubernetes control plane where pods, node pools and cluster-scoped policy are yours to configure. Why the correct answer wins: Virtual machines give the team control of the driver and the image.

### Question 4 — B

Answer: Package the monolith into a container image. A container image carries the exact dependencies to every environment. Wrap the existing process in a portable artifact that a managed runtime can execute. Local study-map skill 1.2 (Containerizing and Refactoring Applications), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 1 (designing highly scalable, secure, and reliable cloud-native applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Virtual machines where the operating system, runtime and scaling group are all managed by the team. Why the correct answer wins: A container image carries the exact dependencies to every environment.
- **B:** Correct. Wrap the existing process in a portable artifact that a managed runtime can execute. In this case: A container image carries the exact dependencies to every environment.
- **C:** Incorrect for this question. An event-triggered function runtime for a single-purpose handler rather than a long-lived service. Why the correct answer wins: A container image carries the exact dependencies to every environment.
- **D:** Incorrect for this question. Hand the source to the managed builder instead of shipping an image. Why the correct answer wins: A container image carries the exact dependencies to every environment.

### Question 5 — A

Answer: Deploy the service in two regions behind a global load balancer. Two regions behind one address keep capacity after a regional loss. Serve from two regions so a regional failure leaves capacity elsewhere. Local study-map skill 1.3 (Regional Distribution and Failover), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 1 (designing highly scalable, secure, and reliable cloud-native applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Correct. Serve from two regions so a regional failure leaves capacity elsewhere. In this case: Two regions behind one address keep capacity after a regional loss.
- **B:** Incorrect for this question. Trade a term commitment for a lower unit price on capacity that never idles. Why the correct answer wins: Two regions behind one address keep capacity after a regional loss.
- **C:** Incorrect for this question. Spread instances over zones of a single region so a zone failure does not stop the service. Why the correct answer wins: Two regions behind one address keep capacity after a regional loss.
- **D:** Incorrect for this question. Run in one zone only, so a zone failure stops the service entirely. Why the correct answer wins: Two regions behind one address keep capacity after a regional loss.

### Question 6 — B

Answer: Deploy in one region across multiple zones. Zones of one region provide the tolerance without crossing a border. Spread instances over zones of a single region so a zone failure does not stop the service. Local study-map skill 1.3 (Regional Distribution and Failover), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 1 (designing highly scalable, secure, and reliable cloud-native applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Cache responses at the edge so repeated requests never reach the origin. Why the correct answer wins: Zones of one region provide the tolerance without crossing a border.
- **B:** Correct. Spread instances over zones of a single region so a zone failure does not stop the service. In this case: Zones of one region provide the tolerance without crossing a border.
- **C:** Incorrect for this question. Run in one zone only, so a zone failure stops the service entirely. Why the correct answer wins: Zones of one region provide the tolerance without crossing a border.
- **D:** Incorrect for this question. Serve from two regions so a regional failure leaves capacity elsewhere. Why the correct answer wins: Zones of one region provide the tolerance without crossing a border.

### Question 7 — C

Answer: Enable session affinity on the backend service. Session affinity keeps the customer on the instance that holds their files. Pin a client to one backend for the life of its session. Local study-map skill 1.4 (Load Balancing and Session Affinity), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 1 (designing highly scalable, secure, and reliable cloud-native applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Move the state out of the instance so any instance can serve any request. Why the correct answer wins: Session affinity keeps the customer on the instance that holds their files.
- **B:** Incorrect for this question. Cache responses at the edge so repeated requests never reach the origin. Why the correct answer wins: Session affinity keeps the customer on the instance that holds their files.
- **C:** Correct. Pin a client to one backend for the life of its session. In this case: Session affinity keeps the customer on the instance that holds their files.
- **D:** Incorrect for this question. Route the client by cookie rather than by address or header. Why the correct answer wins: Session affinity keeps the customer on the instance that holds their files.

### Question 8 — A, B

Answers: Put a global external Application Load Balancer in front; Add a health check endpoint to the backend service. A global front door routes to the nearest healthy region, and a health check removes the backend that cannot answer. A single anycast address that routes to the nearest healthy backend. Let the load balancer stop sending traffic to an unhealthy instance. Local study-map skill 1.4 (Load Balancing and Session Affinity), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 1 (designing highly scalable, secure, and reliable cloud-native applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Correct. A single anycast address that routes to the nearest healthy backend. In this case: A global front door routes to the nearest healthy region, and a health check removes the backend that cannot answer.
- **B:** Correct. Let the load balancer stop sending traffic to an unhealthy instance. In this case: A global front door routes to the nearest healthy region, and a health check removes the backend that cannot answer.
- **C:** Incorrect for this question. A load balancer scoped to one region with a regional address. Why the correct answer wins: A global front door routes to the nearest healthy region, and a health check removes the backend that cannot answer.
- **D:** Incorrect for this question. Cache responses at the edge so repeated requests never reach the origin. Why the correct answer wins: A global front door routes to the nearest healthy region, and a health check removes the backend that cannot answer.
- **E:** Incorrect for this question. Pin a client to one backend for the life of its session. Why the correct answer wins: A global front door routes to the nearest healthy region, and a health check removes the backend that cannot answer.

### Question 9 — C

Answer: Cache reads in Memorystore. A shared in-memory cache serves every user the same fast value. A managed Redis-compatible cache in front of the system of record. Local study-map skill 1.5 (Caching with Memorystore), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 1 (designing highly scalable, secure, and reliable cloud-native applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Read the cache, fall back to the database, and populate the cache on a miss. Why the correct answer wins: A shared in-memory cache serves every user the same fast value.
- **B:** Incorrect for this question. Cache responses at the edge so repeated requests never reach the origin. Why the correct answer wins: A shared in-memory cache serves every user the same fast value.
- **C:** Correct. A managed Redis-compatible cache in front of the system of record. In this case: A shared in-memory cache serves every user the same fast value.
- **D:** Incorrect for this question. A per-instance cache that is fast but not shared between instances. Why the correct answer wins: A shared in-memory cache serves every user the same fast value.

### Question 10 — A

Answer: Serve static content from Cloud CDN. Caching the bundle at the edge removes the repeated long-distance fetch. Cache responses at the edge so repeated requests never reach the origin. Local study-map skill 1.5 (Caching with Memorystore), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 1 (designing highly scalable, secure, and reliable cloud-native applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Correct. Cache responses at the edge so repeated requests never reach the origin. In this case: Caching the bundle at the edge removes the repeated long-distance fetch.
- **B:** Incorrect for this question. A per-instance cache that is fast but not shared between instances. Why the correct answer wins: Caching the bundle at the edge removes the repeated long-distance fetch.
- **C:** Incorrect for this question. A managed Redis-compatible cache in front of the system of record. Why the correct answer wins: Caching the bundle at the edge removes the repeated long-distance fetch.
- **D:** Incorrect for this question. Read the cache, fall back to the database, and populate the cache on a miss. Why the correct answer wins: Caching the bundle at the edge removes the repeated long-distance fetch.

### Question 11 — D, E

Answers: Expose a REST API with JSON payloads; Publish an OpenAPI specification. A resource-oriented HTTP interface is what plain HTTP clients call, and a published specification generates their client. A resource-oriented HTTP interface that browsers and simple clients can call. A machine-readable contract that generates clients and validates requests. Local study-map skill 1.6 (API Protocol Choice: REST and gRPC), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 1 (designing highly scalable, secure, and reliable cloud-native applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Reduce per-call overhead when the API supports a batch surface. Why the correct answer wins: A resource-oriented HTTP interface is what plain HTTP clients call, and a published specification generates their client.
- **B:** Incorrect for this question. A compatibility layer so browser code can call a gRPC service. Why the correct answer wins: A resource-oriented HTTP interface is what plain HTTP clients call, and a published specification generates their client.
- **C:** Incorrect for this question. A binary, schema-driven RPC interface with streaming and generated clients. Why the correct answer wins: A resource-oriented HTTP interface is what plain HTTP clients call, and a published specification generates their client.
- **D:** Correct. A resource-oriented HTTP interface that browsers and simple clients can call. In this case: A resource-oriented HTTP interface is what plain HTTP clients call, and a published specification generates their client.
- **E:** Correct. A machine-readable contract that generates clients and validates requests. In this case: A resource-oriented HTTP interface is what plain HTTP clients call, and a published specification generates their client.

### Question 12 — B

Answer: Expose a gRPC service. A schema-driven binary RPC interface suits high-volume small messages with generated clients. A binary, schema-driven RPC interface with streaming and generated clients. Local study-map skill 1.6 (API Protocol Choice: REST and gRPC), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 1 (designing highly scalable, secure, and reliable cloud-native applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A resource-oriented HTTP interface that browsers and simple clients can call. Why the correct answer wins: A schema-driven binary RPC interface suits high-volume small messages with generated clients.
- **B:** Correct. A binary, schema-driven RPC interface with streaming and generated clients. In this case: A schema-driven binary RPC interface suits high-volume small messages with generated clients.
- **C:** Incorrect for this question. A machine-readable contract that generates clients and validates requests. Why the correct answer wins: A schema-driven binary RPC interface suits high-volume small messages with generated clients.
- **D:** Incorrect for this question. A compatibility layer so browser code can call a gRPC service. Why the correct answer wins: A schema-driven binary RPC interface suits high-volume small messages with generated clients.

### Question 13 — C

Answer: Apply a rate limit per client key. A per-client rate limit stops one caller from taking the shared capacity. Reject or queue requests above a threshold so one client cannot exhaust the service. Local study-map skill 1.7 (API Management, Rate Limiting, and Versioning), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 1 (designing highly scalable, secure, and reliable cloud-native applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A lighter managed gateway for routing and key-based quota enforcement. Why the correct answer wins: A per-client rate limit stops one caller from taking the shared capacity.
- **B:** Incorrect for this question. Keep the old contract working while the new one is adopted. Why the correct answer wins: A per-client rate limit stops one caller from taking the shared capacity.
- **C:** Correct. Reject or queue requests above a threshold so one client cannot exhaust the service. In this case: A per-client rate limit stops one caller from taking the shared capacity.
- **D:** Incorrect for this question. Bound how many calls a plan allows in a window. Why the correct answer wins: A per-client rate limit stops one caller from taking the shared capacity.

### Question 14 — C

Answer: Introduce a new API version alongside the old one. Running a new version alongside the old one keeps those clients working. Keep the old contract working while the new one is adopted. Local study-map skill 1.7 (API Management, Rate Limiting, and Versioning), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 1 (designing highly scalable, secure, and reliable cloud-native applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Extend the contract so existing clients keep working unchanged. Why the correct answer wins: Running a new version alongside the old one keeps those clients working.
- **B:** Incorrect for this question. A machine-readable contract that generates clients and validates requests. Why the correct answer wins: Running a new version alongside the old one keeps those clients working.
- **C:** Correct. Keep the old contract working while the new one is adopted. In this case: Running a new version alongside the old one keeps those clients working.
- **D:** Incorrect for this question. An API management layer for quotas, keys, mediation and analytics. Why the correct answer wins: Running a new version alongside the old one keeps those clients working.

### Question 15 — B, C

Answers: Route the event with Eventarc; Queue the work as a Cloud Tasks task. The event trigger reacts to the export completion, and the task queue handles the per-row calls with retries. A trigger path that turns a Cloud Audit Log or resource event into a delivery. A task queue with retries and rate control aimed at a specific target. Local study-map skill 1.8 (Asynchronous and Event-Driven Integration), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 1 (designing highly scalable, secure, and reliable cloud-native applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A durable, at-least-once message channel with independent subscribers. Why the correct answer wins: The event trigger reacts to the export completion, and the task queue handles the per-row calls with retries.
- **B:** Correct. A trigger path that turns a Cloud Audit Log or resource event into a delivery. In this case: The event trigger reacts to the export completion, and the task queue handles the per-row calls with retries.
- **C:** Correct. A task queue with retries and rate control aimed at a specific target. In this case: The event trigger reacts to the export completion, and the task queue handles the per-row calls with retries.
- **D:** Incorrect for this question. A cron-style trigger that calls a target on a fixed timetable. Why the correct answer wins: The event trigger reacts to the export completion, and the task queue handles the per-row calls with retries.
- **E:** Incorrect for this question. The consumer controls the pace and acknowledges messages itself. Why the correct answer wins: The event trigger reacts to the export completion, and the task queue handles the per-row calls with retries.

### Question 16 — C

Answer: Publish the event to a Pub/Sub topic. A topic delivers one event to every subscriber independently. A durable, at-least-once message channel with independent subscribers. Local study-map skill 1.8 (Asynchronous and Event-Driven Integration), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 1 (designing highly scalable, secure, and reliable cloud-native applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A stateful sequence of service calls with retries and error branches. Why the correct answer wins: A topic delivers one event to every subscriber independently.
- **B:** Incorrect for this question. A cron-style trigger that calls a target on a fixed timetable. Why the correct answer wins: A topic delivers one event to every subscriber independently.
- **C:** Correct. A durable, at-least-once message channel with independent subscribers. In this case: A topic delivers one event to every subscriber independently.
- **D:** Incorrect for this question. A task queue with retries and rate control aimed at a specific target. Why the correct answer wins: A topic delivers one event to every subscriber independently.

### Question 17 — A

Answer: Set CPU and memory requests from measured use. Requests sized from measured use stop the pods reserving capacity they never touch. Give the scheduler real numbers so placement and scaling decisions are not guesses. Local study-map skill 1.9 (Resource Requirements and Cost Optimization), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 1 (designing highly scalable, secure, and reliable cloud-native applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Correct. Give the scheduler real numbers so placement and scaling decisions are not guesses. In this case: Requests sized from measured use stop the pods reserving capacity they never touch.
- **B:** Incorrect for this question. Trade a term commitment for a lower unit price on capacity that never idles. Why the correct answer wins: Requests sized from measured use stop the pods reserving capacity they never touch.
- **C:** Incorrect for this question. Bound the blast radius and the bill at the cost of queueing when the cap is reached. Why the correct answer wins: Requests sized from measured use stop the pods reserving capacity they never touch.
- **D:** Incorrect for this question. Allow the process the headroom it needs so it is not throttled or killed. Why the correct answer wins: Requests sized from measured use stop the pods reserving capacity they never touch.

### Question 18 — C

Answer: Use instance-based billing. Instance-based billing charges for the lifetime the worker occupies, which matches a long-lived consumer. Charge for the whole instance lifetime, which suits steady background work. Local study-map skill 1.9 (Resource Requirements and Cost Optimization), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 1 (designing highly scalable, secure, and reliable cloud-native applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Pay for idle capacity so a cold start never appears in the latency percentiles. Why the correct answer wins: Instance-based billing charges for the lifetime the worker occupies, which matches a long-lived consumer.
- **B:** Incorrect for this question. Trade a term commitment for a lower unit price on capacity that never idles. Why the correct answer wins: Instance-based billing charges for the lifetime the worker occupies, which matches a long-lived consumer.
- **C:** Correct. Charge for the whole instance lifetime, which suits steady background work. In this case: Instance-based billing charges for the lifetime the worker occupies, which matches a long-lived consumer.
- **D:** Incorrect for this question. Charge only while a request is being handled, which suits bursty traffic. Why the correct answer wins: Instance-based billing charges for the lifetime the worker occupies, which matches a long-lived consumer.

### Question 19 — A

Answer: Route by revision tag or header. Routing by revision tag sends only tagged requests to the new revision. Send only tagged requests to the new revision for internal testing. Local study-map skill 1.10 (Traffic Splitting and Gradual Rollout), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 1 (designing highly scalable, secure, and reliable cloud-native applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Correct. Send only tagged requests to the new revision for internal testing. In this case: Routing by revision tag sends only tagged requests to the new revision.
- **B:** Incorrect for this question. Send a fraction of requests to the new revision while the old one still serves the rest. Why the correct answer wins: Routing by revision tag sends only tagged requests to the new revision.
- **C:** Incorrect for this question. Expose the new version to a slice of traffic before widening it. Why the correct answer wins: Routing by revision tag sends only tagged requests to the new revision.
- **D:** Incorrect for this question. Ship the code dark and enable it per cohort without a redeploy. Why the correct answer wins: Routing by revision tag sends only tagged requests to the new revision.

### Question 20 — D

Answer: Gate the change behind a feature flag. A flag enables the change for a cohort without touching the deployed artifact. Ship the code dark and enable it per cohort without a redeploy. Local study-map skill 1.10 (Traffic Splitting and Gradual Rollout), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 1 (designing highly scalable, secure, and reliable cloud-native applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Send a fraction of requests to the new revision while the old one still serves the rest. Why the correct answer wins: A flag enables the change for a cohort without touching the deployed artifact.
- **B:** Incorrect for this question. Return all traffic to the known-good revision when the new one misbehaves. Why the correct answer wins: A flag enables the change for a cohort without touching the deployed artifact.
- **C:** Incorrect for this question. Expose the new version to a slice of traffic before widening it. Why the correct answer wins: A flag enables the change for a cohort without touching the deployed artifact.
- **D:** Correct. Ship the code dark and enable it per cohort without a redeploy. In this case: A flag enables the change for a cohort without touching the deployed artifact.

### Question 21 — A

Answer: Orchestrate the steps in Workflows. A stateful orchestration keeps the order and the compensation in one definition. A stateful sequence of service calls with retries and error branches. Local study-map skill 1.11 (Orchestrating Services), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 1 (designing highly scalable, secure, and reliable cloud-native applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Correct. A stateful sequence of service calls with retries and error branches. In this case: A stateful orchestration keeps the order and the compensation in one definition.
- **B:** Incorrect for this question. A task queue with retries and rate control aimed at a specific target. Why the correct answer wins: A stateful orchestration keeps the order and the compensation in one definition.
- **C:** Incorrect for this question. A durable, at-least-once message channel with independent subscribers. Why the correct answer wins: A stateful orchestration keeps the order and the compensation in one definition.
- **D:** Incorrect for this question. A cron-style trigger that calls a target on a fixed timetable. Why the correct answer wins: A stateful orchestration keeps the order and the compensation in one definition.

### Question 22 — A

Answer: Add a lifecycle rule to the bucket. A lifecycle rule deletes objects by age with no code to run. Transition or delete objects by age so retention happens without a job. Local study-map skill 1.12 (Data Retention and Organization Policy), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 1 (designing highly scalable, secure, and reliable cloud-native applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Correct. Transition or delete objects by age so retention happens without a job. In this case: A lifecycle rule deletes objects by age with no code to run.
- **B:** Incorrect for this question. Make the retention period impossible to shorten, even by an owner. Why the correct answer wins: A lifecycle rule deletes objects by age with no code to run.
- **C:** Incorrect for this question. A time-limited grant to one object without exposing credentials. Why the correct answer wins: A lifecycle rule deletes objects by age with no code to run.
- **D:** Incorrect for this question. Serve every object to anyone, which removes the need to authorize at all. Why the correct answer wins: A lifecycle rule deletes objects by age with no code to run.

### Question 23 — D

Answer: Store the credential in Secret Manager. A managed secret store versions the value so a new version can be activated without a rebuild. A managed secret store with versioning and access audit. Local study-map skill 1.13 (Secrets, Keys, and Credential Rotation), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 1 (designing highly scalable, secure, and reliable cloud-native applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A long-lived credential that has to be stored and rotated by hand. Why the correct answer wins: A managed secret store versions the value so a new version can be activated without a rebuild.
- **B:** Incorrect for this question. A key the customer owns, rotates and can disable. Why the correct answer wins: A managed secret store versions the value so a new version can be activated without a rebuild.
- **C:** Incorrect for this question. Inject the value into the process environment at start-up. Why the correct answer wins: A managed secret store versions the value so a new version can be activated without a rebuild.
- **D:** Correct. A managed secret store with versioning and access audit. In this case: A managed secret store versions the value so a new version can be activated without a rebuild.

### Question 24 — C, E

Answers: Rotate the secret on a schedule; Grant only the roles the workload needs. Rotating the credential bounds the exposure, and least privilege stops one identity from holding more than the call needs. Issue a new version and retire the old one so exposure has a bounded life. Scope permissions to the actions in use rather than the whole service. Local study-map skill 1.13 (Secrets, Keys, and Credential Rotation), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 1 (designing highly scalable, secure, and reliable cloud-native applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A legacy broad role that can change most resources in the project. Why the correct answer wins: Rotating the credential bounds the exposure, and least privilege stops one identity from holding more than the call needs.
- **B:** Incorrect for this question. A long-lived credential that has to be stored and rotated by hand. Why the correct answer wins: Rotating the credential bounds the exposure, and least privilege stops one identity from holding more than the call needs.
- **C:** Correct. Issue a new version and retire the old one so exposure has a bounded life. In this case: Rotating the credential bounds the exposure, and least privilege stops one identity from holding more than the call needs.
- **D:** Incorrect for this question. Inject the value into the process environment at start-up. Why the correct answer wins: Rotating the credential bounds the exposure, and least privilege stops one identity from holding more than the call needs.
- **E:** Correct. Scope permissions to the actions in use rather than the whole service. In this case: Rotating the credential bounds the exposure, and least privilege stops one identity from holding more than the call needs.

### Question 25 — A

Answer: Use Identity Platform for end-user sign-in. A managed identity service handles customer accounts and tokens. Local study-map skill 1.14 (Application Authentication), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 1 (designing highly scalable, secure, and reliable cloud-native applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Correct. In this case: A managed identity service handles customer accounts and tokens.
- **B:** Incorrect for this question. A dedicated identity whose roles can be granted and revoked independently. Why the correct answer wins: A managed identity service handles customer accounts and tokens.
- **C:** Incorrect for this question. Let the client library find credentials from the environment. Why the correct answer wins: A managed identity service handles customer accounts and tokens.
- **D:** Incorrect for this question. Authenticate and authorize users before a request reaches the application. Why the correct answer wins: A managed identity service handles customer accounts and tokens.

### Question 26 — C

Answer: Rely on Application Default Credentials. Application Default Credentials let the library find the ambient identity. Let the client library find credentials from the environment. Local study-map skill 1.14 (Application Authentication), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 1 (designing highly scalable, secure, and reliable cloud-native applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Exchange an outside token for a short-lived Google credential. Why the correct answer wins: Application Default Credentials let the library find the ambient identity.
- **B:** Incorrect for this question. Keyless credential issuance for pods through Workload Identity. Why the correct answer wins: Application Default Credentials let the library find the ambient identity.
- **C:** Correct. Let the client library find credentials from the environment. In this case: Application Default Credentials let the library find the ambient identity.
- **D:** Incorrect for this question. A long-lived credential that has to be stored and rotated by hand. Why the correct answer wins: Application Default Credentials let the library find the ambient identity.

### Question 27 — B

Answer: Put Identity-Aware Proxy in front of the service. Identity-Aware Proxy checks the user and group before the request reaches the service. Authenticate and authorize users before a request reaches the application. Local study-map skill 1.15 (Least Privilege and Service-to-Service Security), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 1 (designing highly scalable, secure, and reliable cloud-native applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Restrict which pods may talk to which pods inside the cluster. Why the correct answer wins: Identity-Aware Proxy checks the user and group before the request reaches the service.
- **B:** Correct. Authenticate and authorize users before a request reaches the application. In this case: Identity-Aware Proxy checks the user and group before the request reaches the service.
- **C:** Incorrect for this question. Let anyone reach the endpoint, which is only appropriate for public content. Why the correct answer wins: Identity-Aware Proxy checks the user and group before the request reaches the service.
- **D:** Incorrect for this question. Bound the total capacity a namespace may consume. Why the correct answer wins: Identity-Aware Proxy checks the user and group before the request reaches the service.

### Question 28 — A, C

Answers: Send traffic through Direct VPC egress; Reach the service through Private Service Connect. Direct VPC egress gives the runtime a private path into the network, and a private endpoint consumes the partner service. Give Cloud Run or functions a private path into the VPC. A private endpoint that consumes a published service without peering. Local study-map skill 1.15 (Least Privilege and Service-to-Service Security), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 1 (designing highly scalable, secure, and reliable cloud-native applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Correct. A private endpoint that consumes a published service without peering. In this case: Direct VPC egress gives the runtime a private path into the network, and a private endpoint consumes the partner service.
- **B:** Incorrect for this question. Authenticate and authorize users before a request reaches the application. Why the correct answer wins: Direct VPC egress gives the runtime a private path into the network, and a private endpoint consumes the partner service.
- **C:** Correct. Give Cloud Run or functions a private path into the VPC. In this case: Direct VPC egress gives the runtime a private path into the network, and a private endpoint consumes the partner service.
- **D:** Incorrect for this question. Let anyone reach the endpoint, which is only appropriate for public content. Why the correct answer wins: Direct VPC egress gives the runtime a private path into the network, and a private endpoint consumes the partner service.
- **E:** Incorrect for this question. Serve every object to anyone, which removes the need to authorize at all. Why the correct answer wins: Direct VPC egress gives the runtime a private path into the network, and a private endpoint consumes the partner service.

### Question 29 — B

Answer: Store the objects in Cloud Storage. Object storage holds large immutable blobs cheaply at that volume. Durable object storage addressed by name rather than a database row. Local study-map skill 1.16 (Storage and Schema Selection), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 1 (designing highly scalable, secure, and reliable cloud-native applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A relational database with strongly consistent multi-region transactions. Why the correct answer wins: Object storage holds large immutable blobs cheaply at that volume.
- **B:** Correct. Durable object storage addressed by name rather than a database row. In this case: Object storage holds large immutable blobs cheaply at that volume.
- **C:** Incorrect for this question. A document store with real-time listeners and mobile SDKs. Why the correct answer wins: Object storage holds large immutable blobs cheaply at that volume.
- **D:** Incorrect for this question. A managed Redis-compatible cache in front of the system of record. Why the correct answer wins: Object storage holds large immutable blobs cheaply at that volume.

### Question 30 — C

Answer: Cache reads in Memorystore. An in-memory store serves that latency for rebuildable data. A managed Redis-compatible cache in front of the system of record. Local study-map skill 1.16 (Storage and Schema Selection), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 1 (designing highly scalable, secure, and reliable cloud-native applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Durable object storage addressed by name rather than a database row. Why the correct answer wins: An in-memory store serves that latency for rebuildable data.
- **B:** Incorrect for this question. Order the key so the query becomes a contiguous range scan. Why the correct answer wins: An in-memory store serves that latency for rebuildable data.
- **C:** Correct. A managed Redis-compatible cache in front of the system of record. In this case: An in-memory store serves that latency for rebuildable data.
- **D:** Incorrect for this question. A relational database with strongly consistent multi-region transactions. Why the correct answer wins: An in-memory store serves that latency for rebuildable data.

### Question 31 — D

Answer: Issue a signed URL with a short expiry. A short-lived signed URL authorizes exactly that object for that window. A time-limited grant to one object without exposing credentials. Local study-map skill 1.17 (Signed URLs and Time-Limited Access), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 1 (designing highly scalable, secure, and reliable cloud-native applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Serve every object to anyone, which removes the need to authorize at all. Why the correct answer wins: A short-lived signed URL authorizes exactly that object for that window.
- **B:** Incorrect for this question. Transition or delete objects by age so retention happens without a job. Why the correct answer wins: A short-lived signed URL authorizes exactly that object for that window.
- **C:** Incorrect for this question. Make the retention period impossible to shorten, even by an owner. Why the correct answer wins: A short-lived signed URL authorizes exactly that object for that window.
- **D:** Correct. A time-limited grant to one object without exposing credentials. In this case: A short-lived signed URL authorizes exactly that object for that window.

### Question 32 — D

Answer: Stream the events into BigQuery. Streaming the events makes recent behaviour available to the model almost immediately. Land analytics rows in the warehouse for SQL and ML use. Local study-map skill 1.18 (Analytics and ML Data Handoff), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 1 (designing highly scalable, secure, and reliable cloud-native applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Durable object storage addressed by name rather than a database row. Why the correct answer wins: Streaming the events makes recent behaviour available to the model almost immediately.
- **B:** Incorrect for this question. Load a periodic extract rather than a continuous stream. Why the correct answer wins: Streaming the events makes recent behaviour available to the model almost immediately.
- **C:** Incorrect for this question. A relational database with strongly consistent multi-region transactions. Why the correct answer wins: Streaming the events makes recent behaviour available to the model almost immediately.
- **D:** Correct. Land analytics rows in the warehouse for SQL and ML use. In this case: Streaming the events makes recent behaviour available to the model almost immediately.

### Question 33 — D

Answer: Run the service emulator locally. A local emulator evaluates the rules and queries without any deployed resource. A local stand-in for a managed service used for unit and integration work. Local study-map skill 2.1 (Local Emulation of Cloud Services), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 2 (building and testing applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A browser terminal with the SDK and tooling already installed. Why the correct answer wins: A local emulator evaluates the rules and queries without any deployed resource.
- **B:** Incorrect for this question. Editor integration for scaffolding, running and debugging on Google Cloud. Why the correct answer wins: A local emulator evaluates the rules and queries without any deployed resource.
- **C:** Incorrect for this question. A managed, container-defined development environment behind a private endpoint. Why the correct answer wins: A local emulator evaluates the rules and queries without any deployed resource.
- **D:** Correct. A local stand-in for a managed service used for unit and integration work. In this case: A local emulator evaluates the rules and queries without any deployed resource.

### Question 34 — D

Answer: Use Cloud Workstations for the environment. A managed workstation serves the defined image to each engineer. A managed, container-defined development environment behind a private endpoint. Local study-map skill 2.1 (Local Emulation of Cloud Services), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 2 (building and testing applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A browser terminal with the SDK and tooling already installed. Why the correct answer wins: A managed workstation serves the defined image to each engineer.
- **B:** Incorrect for this question. A local stand-in for a managed service used for unit and integration work. Why the correct answer wins: A managed workstation serves the defined image to each engineer.
- **C:** Incorrect for this question. Editor integration for scaffolding, running and debugging on Google Cloud. Why the correct answer wins: A managed workstation serves the defined image to each engineer.
- **D:** Correct. A managed, container-defined development environment behind a private endpoint. In this case: A managed workstation serves the defined image to each engineer.

### Question 35 — B

Answer: Run an integration test against the emulator. An integration test exercises the real wire-up and its acknowledgement behaviour. Exercise the wire-up between components before deploying. Local study-map skill 2.1 (Local Emulation of Cloud Services), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 2 (building and testing applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Exercise one unit in isolation with its collaborators replaced. Why the correct answer wins: An integration test exercises the real wire-up and its acknowledgement behaviour.
- **B:** Correct. Exercise the wire-up between components before deploying. In this case: An integration test exercises the real wire-up and its acknowledgement behaviour.
- **C:** Incorrect for this question. Measure behaviour under expected peak traffic rather than guessing. Why the correct answer wins: An integration test exercises the real wire-up and its acknowledgement behaviour.
- **D:** Incorrect for this question. A local stand-in for a managed service used for unit and integration work. Why the correct answer wins: An integration test exercises the real wire-up and its acknowledgement behaviour.

### Question 36 — A, D

Answers: Develop with Cloud Code in the IDE; Connect the assistant to an MCP server. Editor integration gives the breakpoint loop, and an MCP server exposes tools to the assistant instead of pasted context. Editor integration for scaffolding, running and debugging on Google Cloud. Give the assistant a defined tool surface instead of pasting context by hand. Local study-map skill 2.2 (Developer Tooling and AI Assistance), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 2 (building and testing applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Correct. Give the assistant a defined tool surface instead of pasting context by hand. In this case: Editor integration gives the breakpoint loop, and an MCP server exposes tools to the assistant instead of pasted context.
- **B:** Incorrect for this question. A managed, container-defined development environment behind a private endpoint. Why the correct answer wins: Editor integration gives the breakpoint loop, and an MCP server exposes tools to the assistant instead of pasted context.
- **C:** Incorrect for this question. A browser terminal with the SDK and tooling already installed. Why the correct answer wins: Editor integration gives the breakpoint loop, and an MCP server exposes tools to the assistant instead of pasted context.
- **D:** Correct. Editor integration for scaffolding, running and debugging on Google Cloud. In this case: Editor integration gives the breakpoint loop, and an MCP server exposes tools to the assistant instead of pasted context.
- **E:** Incorrect for this question. A local stand-in for a managed service used for unit and integration work. Why the correct answer wins: Editor integration gives the breakpoint loop, and an MCP server exposes tools to the assistant instead of pasted context.

### Question 37 — B

Answer: Use an AI coding assistant to draft the tests. A coding assistant drafts the tests from context, which the team then reviews. Generate a first draft from context, then review and correct it. Local study-map skill 2.2 (Developer Tooling and AI Assistance), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 2 (building and testing applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. An assistant that reads telemetry and proposes a cause and a next step. Why the correct answer wins: A coding assistant drafts the tests from context, which the team then reviews.
- **B:** Correct. Generate a first draft from context, then review and correct it. In this case: A coding assistant drafts the tests from context, which the team then reviews.
- **C:** Incorrect for this question. Give the assistant a defined tool surface instead of pasting context by hand. Why the correct answer wins: A coding assistant drafts the tests from context, which the team then reviews.
- **D:** Incorrect for this question. Editor integration for scaffolding, running and debugging on Google Cloud. Why the correct answer wins: A coding assistant drafts the tests from context, which the team then reviews.

### Question 38 — A

Answer: Iterate with Skaffold. An automatic local iteration loop rebuilds and redeploys on each change. A loop that rebuilds and redeploys automatically on a source change. Local study-map skill 2.2 (Developer Tooling and AI Assistance), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 2 (building and testing applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Correct. A loop that rebuilds and redeploys automatically on a source change. In this case: An automatic local iteration loop rebuilds and redeploys on each change.
- **B:** Incorrect for this question. Release exactly the artifact that was tested rather than a moving tag. Why the correct answer wins: An automatic local iteration loop rebuilds and redeploys on each change.
- **C:** Incorrect for this question. Run the build steps locally and push the result when someone remembers. Why the correct answer wins: An automatic local iteration loop rebuilds and redeploys on each change.
- **D:** Incorrect for this question. A managed build service that runs the steps from a build configuration file. Why the correct answer wins: An automatic local iteration loop rebuilds and redeploys on each change.

### Question 39 — A

Answer: Build the image with Cloud Build. A managed build service runs the declared steps in a clean environment. A managed build service that runs the steps from a build configuration file. Local study-map skill 2.3 (Container Builds with Cloud Build), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 2 (building and testing applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Correct. A managed build service that runs the steps from a build configuration file. In this case: A managed build service runs the declared steps in a clean environment.
- **B:** Incorrect for this question. A browser terminal with the SDK and tooling already installed. Why the correct answer wins: A managed build service runs the declared steps in a clean environment.
- **C:** Incorrect for this question. Run the build steps locally and push the result when someone remembers. Why the correct answer wins: A managed build service runs the declared steps in a clean environment.
- **D:** Incorrect for this question. Editor integration for scaffolding, running and debugging on Google Cloud. Why the correct answer wins: A managed build service runs the declared steps in a clean environment.

### Question 40 — D

Answer: Trigger the build from a repository push. A trigger on the branch makes every change produce an inspectable build. Start the pipeline when the branch changes rather than by hand. Local study-map skill 2.3 (Container Builds with Cloud Build), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 2 (building and testing applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Run the build steps locally and push the result when someone remembers. Why the correct answer wins: A trigger on the branch makes every change produce an inspectable build.
- **B:** Incorrect for this question. A task queue with retries and rate control aimed at a specific target. Why the correct answer wins: A trigger on the branch makes every change produce an inspectable build.
- **C:** Incorrect for this question. A cron-style trigger that calls a target on a fixed timetable. Why the correct answer wins: A trigger on the branch makes every change produce an inspectable build.
- **D:** Correct. Start the pipeline when the branch changes rather than by hand. In this case: A trigger on the branch makes every change produce an inspectable build.

### Question 41 — C

Answer: Deploy a pinned image digest. Pinning a digest makes the deployed artifact unambiguous and reproducible. Release exactly the artifact that was tested rather than a moving tag. Local study-map skill 2.3 (Container Builds with Cloud Build), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 2 (building and testing applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Hand the source to the managed builder instead of shipping an image. Why the correct answer wins: Pinning a digest makes the deployed artifact unambiguous and reproducible.
- **B:** Incorrect for this question. Wrap the existing process in a portable artifact that a managed runtime can execute. Why the correct answer wins: Pinning a digest makes the deployed artifact unambiguous and reproducible.
- **C:** Correct. Release exactly the artifact that was tested rather than a moving tag. In this case: Pinning a digest makes the deployed artifact unambiguous and reproducible.
- **D:** Incorrect for this question. A managed build service that runs the steps from a build configuration file. Why the correct answer wins: Pinning a digest makes the deployed artifact unambiguous and reproducible.

### Question 42 — A, D

Answers: Push the image to Artifact Registry; Build the image with Cloud Build. A scoped registry keeps each environment's images separate, and the managed build service produces them reproducibly. A managed registry with IAM-scoped repositories per environment. A managed build service that runs the steps from a build configuration file. Local study-map skill 2.3 (Container Builds with Cloud Build), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 2 (building and testing applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Correct. A managed build service that runs the steps from a build configuration file. In this case: A scoped registry keeps each environment's images separate, and the managed build service produces them reproducibly.
- **B:** Incorrect for this question. A browser terminal with the SDK and tooling already installed. Why the correct answer wins: A scoped registry keeps each environment's images separate, and the managed build service produces them reproducibly.
- **C:** Incorrect for this question. Editor integration for scaffolding, running and debugging on Google Cloud. Why the correct answer wins: A scoped registry keeps each environment's images separate, and the managed build service produces them reproducibly.
- **D:** Correct. A managed registry with IAM-scoped repositories per environment. In this case: A scoped registry keeps each environment's images separate, and the managed build service produces them reproducibly.
- **E:** Incorrect for this question. The older registry whose access model is project-wide Cloud Storage. Why the correct answer wins: A scoped registry keeps each environment's images separate, and the managed build service produces them reproducibly.

### Question 43 — C

Answer: Push the image to Container Registry. Repository-scoped IAM is the model the newer registry uses, unlike the older project-wide one. The older registry whose access model is project-wide Cloud Storage. Local study-map skill 2.4 (Artifact Registry and Image Storage), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 2 (building and testing applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A managed registry with IAM-scoped repositories per environment. Why the correct answer wins: Repository-scoped IAM is the model the newer registry uses, unlike the older project-wide one.
- **B:** Incorrect for this question. Durable object storage addressed by name rather than a database row. Why the correct answer wins: Repository-scoped IAM is the model the newer registry uses, unlike the older project-wide one.
- **C:** Correct. The older registry whose access model is project-wide Cloud Storage. In this case: Repository-scoped IAM is the model the newer registry uses, unlike the older project-wide one.
- **D:** Incorrect for this question. A managed build service that runs the steps from a build configuration file. Why the correct answer wins: Repository-scoped IAM is the model the newer registry uses, unlike the older project-wide one.

### Question 44 — B

Answer: Push the image to Artifact Registry. The managed registry ties scanning and regional storage to the repository. A managed registry with IAM-scoped repositories per environment. Local study-map skill 2.4 (Artifact Registry and Image Storage), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 2 (building and testing applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A managed build service that runs the steps from a build configuration file. Why the correct answer wins: The managed registry ties scanning and regional storage to the repository.
- **B:** Correct. A managed registry with IAM-scoped repositories per environment. In this case: The managed registry ties scanning and regional storage to the repository.
- **C:** Incorrect for this question. Durable object storage addressed by name rather than a database row. Why the correct answer wins: The managed registry ties scanning and regional storage to the repository.
- **D:** Incorrect for this question. The older registry whose access model is project-wide Cloud Storage. Why the correct answer wins: The managed registry ties scanning and regional storage to the repository.

### Question 45 — C

Answer: Store the objects in Cloud Storage. Object storage versions non-image artifacts durably. Durable object storage addressed by name rather than a database row. Local study-map skill 2.4 (Artifact Registry and Image Storage), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 2 (building and testing applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A managed build service that runs the steps from a build configuration file. Why the correct answer wins: Object storage versions non-image artifacts durably.
- **B:** Incorrect for this question. The older registry whose access model is project-wide Cloud Storage. Why the correct answer wins: Object storage versions non-image artifacts durably.
- **C:** Correct. Durable object storage addressed by name rather than a database row. In this case: Object storage versions non-image artifacts durably.
- **D:** Incorrect for this question. A managed registry with IAM-scoped repositories per environment. Why the correct answer wins: Object storage versions non-image artifacts durably.

### Question 46 — D

Answer: Scan the image with Artifact Analysis. Scanning maps the vulnerability to the images that contain it. Report known vulnerabilities in the image layers and packages. Local study-map skill 2.5 (Build Provenance and Admission Control), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 2 (building and testing applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Only images that satisfy the attestation policy may be deployed. Why the correct answer wins: Scanning maps the vulnerability to the images that contain it.
- **B:** Incorrect for this question. Aggregate and triage security findings across the project. Why the correct answer wins: Scanning maps the vulnerability to the images that contain it.
- **C:** Incorrect for this question. A signed record of what was built and from which source. Why the correct answer wins: Scanning maps the vulnerability to the images that contain it.
- **D:** Correct. Report known vulnerabilities in the image layers and packages. In this case: Scanning maps the vulnerability to the images that contain it.

### Question 47 — D

Answer: Enforce admission with Binary Authorization. Admission control rejects an image without a valid attestation. Only images that satisfy the attestation policy may be deployed. Local study-map skill 2.5 (Build Provenance and Admission Control), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 2 (building and testing applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A signed record of what was built and from which source. Why the correct answer wins: Admission control rejects an image without a valid attestation.
- **B:** Incorrect for this question. Report known vulnerabilities in the image layers and packages. Why the correct answer wins: Admission control rejects an image without a valid attestation.
- **C:** Incorrect for this question. Aggregate and triage security findings across the project. Why the correct answer wins: Admission control rejects an image without a valid attestation.
- **D:** Correct. Only images that satisfy the attestation policy may be deployed. In this case: Admission control rejects an image without a valid attestation.

### Question 48 — D

Answer: Require a higher supply-chain level before release. A documented supply-chain level makes the provenance guarantee an explicit gate on the pipeline. Demand a stronger provenance guarantee as a gate on the pipeline. Local study-map skill 2.5 (Build Provenance and Admission Control), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 2 (building and testing applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Report known vulnerabilities in the image layers and packages. Why the correct answer wins: A documented supply-chain level makes the provenance guarantee an explicit gate on the pipeline.
- **B:** Incorrect for this question. A signed record of what was built and from which source. Why the correct answer wins: A documented supply-chain level makes the provenance guarantee an explicit gate on the pipeline.
- **C:** Incorrect for this question. Only images that satisfy the attestation policy may be deployed. Why the correct answer wins: A documented supply-chain level makes the provenance guarantee an explicit gate on the pipeline.
- **D:** Correct. Demand a stronger provenance guarantee as a gate on the pipeline. In this case: A documented supply-chain level makes the provenance guarantee an explicit gate on the pipeline.

### Question 49 — A

Answer: Add a unit test with dependencies stubbed. Unit tests isolate each case and report it by name. Exercise one unit in isolation with its collaborators replaced. Local study-map skill 2.6 (Unit Testing Practice), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 2 (building and testing applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Correct. Exercise one unit in isolation with its collaborators replaced. In this case: Unit tests isolate each case and report it by name.
- **B:** Incorrect for this question. Measure behaviour under expected peak traffic rather than guessing. Why the correct answer wins: Unit tests isolate each case and report it by name.
- **C:** Incorrect for this question. Exercise the wire-up between components before deploying. Why the correct answer wins: Unit tests isolate each case and report it by name.
- **D:** Incorrect for this question. Keep the suite trustworthy while the unstable test is repaired. Why the correct answer wins: Unit tests isolate each case and report it by name.

### Question 50 — A

Answer: Quarantine the flaky test and fix it. Quarantining the unstable test restores trust while it is repaired. Keep the suite trustworthy while the unstable test is repaired. Local study-map skill 2.6 (Unit Testing Practice), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 2 (building and testing applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Correct. Keep the suite trustworthy while the unstable test is repaired. In this case: Quarantining the unstable test restores trust while it is repaired.
- **B:** Incorrect for this question. Exercise the wire-up between components before deploying. Why the correct answer wins: Quarantining the unstable test restores trust while it is repaired.
- **C:** Incorrect for this question. Exercise one unit in isolation with its collaborators replaced. Why the correct answer wins: Quarantining the unstable test restores trust while it is repaired.
- **D:** Incorrect for this question. Make a passing test suite a precondition for release. Why the correct answer wins: Quarantining the unstable test restores trust while it is repaired.

### Question 51 — B, D

Answers: Add a unit test with dependencies stubbed; Block the deploy on the test result. A unit test runs fast and isolates the failure, and a gate makes a red suite stop the release. Exercise one unit in isolation with its collaborators replaced. Make a passing test suite a precondition for release. Local study-map skill 2.6 (Unit Testing Practice), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 2 (building and testing applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Exercise the wire-up between components before deploying. Why the correct answer wins: A unit test runs fast and isolates the failure, and a gate makes a red suite stop the release.
- **B:** Correct. Exercise one unit in isolation with its collaborators replaced. In this case: A unit test runs fast and isolates the failure, and a gate makes a red suite stop the release.
- **C:** Incorrect for this question. Measure behaviour under expected peak traffic rather than guessing. Why the correct answer wins: A unit test runs fast and isolates the failure, and a gate makes a red suite stop the release.
- **D:** Correct. Make a passing test suite a precondition for release. In this case: A unit test runs fast and isolates the failure, and a gate makes a red suite stop the release.
- **E:** Incorrect for this question. Keep the suite trustworthy while the unstable test is repaired. Why the correct answer wins: A unit test runs fast and isolates the failure, and a gate makes a red suite stop the release.

### Question 52 — D

Answer: Run an integration test against the emulator. An integration test runs both sides against the same contract. Exercise the wire-up between components before deploying. Local study-map skill 2.7 (Automated Integration Testing), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 2 (building and testing applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Measure behaviour under expected peak traffic rather than guessing. Why the correct answer wins: An integration test runs both sides against the same contract.
- **B:** Incorrect for this question. A local stand-in for a managed service used for unit and integration work. Why the correct answer wins: An integration test runs both sides against the same contract.
- **C:** Incorrect for this question. Exercise one unit in isolation with its collaborators replaced. Why the correct answer wins: An integration test runs both sides against the same contract.
- **D:** Correct. Exercise the wire-up between components before deploying. In this case: An integration test runs both sides against the same contract.

### Question 53 — B

Answer: Run the tests as a Cloud Build step. A build step runs it on every change without being remembered. Fail the pipeline at the test stage instead of after deployment. Local study-map skill 2.7 (Automated Integration Testing), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 2 (building and testing applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Keep the suite trustworthy while the unstable test is repaired. Why the correct answer wins: A build step runs it on every change without being remembered.
- **B:** Correct. Fail the pipeline at the test stage instead of after deployment. In this case: A build step runs it on every change without being remembered.
- **C:** Incorrect for this question. Measure behaviour under expected peak traffic rather than guessing. Why the correct answer wins: A build step runs it on every change without being remembered.
- **D:** Incorrect for this question. Make a passing test suite a precondition for release. Why the correct answer wins: A build step runs it on every change without being remembered.

### Question 54 — D, E

Answers: Run an integration test against the emulator; Run the tests as a Cloud Build step. An integration test exercises the real dependencies, and a build step makes the check part of every merge. Exercise the wire-up between components before deploying. Fail the pipeline at the test stage instead of after deployment. Local study-map skill 2.7 (Automated Integration Testing), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 2 (building and testing applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Make a passing test suite a precondition for release. Why the correct answer wins: An integration test exercises the real dependencies, and a build step makes the check part of every merge.
- **B:** Incorrect for this question. Exercise one unit in isolation with its collaborators replaced. Why the correct answer wins: An integration test exercises the real dependencies, and a build step makes the check part of every merge.
- **C:** Incorrect for this question. Measure behaviour under expected peak traffic rather than guessing. Why the correct answer wins: An integration test exercises the real dependencies, and a build step makes the check part of every merge.
- **D:** Correct. Exercise the wire-up between components before deploying. In this case: An integration test exercises the real dependencies, and a build step makes the check part of every merge.
- **E:** Correct. Fail the pipeline at the test stage instead of after deployment. In this case: An integration test exercises the real dependencies, and a build step makes the check part of every merge.

### Question 55 — B

Answer: Load-test the release before the rollout. A load test measures behaviour at the expected peak before the release. Measure behaviour under expected peak traffic rather than guessing. Local study-map skill 2.7 (Automated Integration Testing), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 2 (building and testing applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Exercise one unit in isolation with its collaborators replaced. Why the correct answer wins: A load test measures behaviour at the expected peak before the release.
- **B:** Correct. Measure behaviour under expected peak traffic rather than guessing. In this case: A load test measures behaviour at the expected peak before the release.
- **C:** Incorrect for this question. Find the function consuming CPU or memory under real traffic. Why the correct answer wins: A load test measures behaviour at the expected peak before the release.
- **D:** Incorrect for this question. Exercise the wire-up between components before deploying. Why the correct answer wins: A load test measures behaviour at the expected peak before the release.

### Question 56 — D, E

Answers: Deploy from source and let the platform build it; Raise CPU during start-up only. Source deployment builds the repository with detected buildpacks, and startup boost gives the cold start its extra CPU. Hand the source to the managed builder instead of shipping an image. Speed initialization without paying for the extra CPU afterwards. Local study-map skill 3.1 (Deploying Cloud Run from Source), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 3 (configuring cloud-native applications for deployment): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Let each instance serve more simultaneous requests before another instance is started. Why the correct answer wins: Source deployment builds the repository with detected buildpacks, and startup boost gives the cold start its extra CPU.
- **B:** Incorrect for this question. Run the build steps locally and push the result when someone remembers. Why the correct answer wins: Source deployment builds the repository with detected buildpacks, and startup boost gives the cold start its extra CPU.
- **C:** Incorrect for this question. Wrap the existing process in a portable artifact that a managed runtime can execute. Why the correct answer wins: Source deployment builds the repository with detected buildpacks, and startup boost gives the cold start its extra CPU.
- **D:** Correct. Hand the source to the managed builder instead of shipping an image. In this case: Source deployment builds the repository with detected buildpacks, and startup boost gives the cold start its extra CPU.
- **E:** Correct. Speed initialization without paying for the extra CPU afterwards. In this case: Source deployment builds the repository with detected buildpacks, and startup boost gives the cold start its extra CPU.

### Question 57 — D

Answer: Raise the per-instance concurrency limit. Lowering per-instance concurrency keeps fewer requests competing inside an instance. Let each instance serve more simultaneous requests before another instance is started. Local study-map skill 3.1 (Deploying Cloud Run from Source), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 3 (configuring cloud-native applications for deployment): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Bound the blast radius and the bill at the cost of queueing when the cap is reached. Why the correct answer wins: Lowering per-instance concurrency keeps fewer requests competing inside an instance.
- **B:** Incorrect for this question. Add pods when average CPU crosses the target. Why the correct answer wins: Lowering per-instance concurrency keeps fewer requests competing inside an instance.
- **C:** Incorrect for this question. Allow the process the headroom it needs so it is not throttled or killed. Why the correct answer wins: Lowering per-instance concurrency keeps fewer requests competing inside an instance.
- **D:** Correct. Let each instance serve more simultaneous requests before another instance is started. In this case: Lowering per-instance concurrency keeps fewer requests competing inside an instance.

### Question 58 — C

Answer: Run the batch work as a Cloud Run job. A job runs a task to completion and stops rather than serving traffic. A task-shaped execution that runs to completion instead of serving requests. Local study-map skill 3.1 (Deploying Cloud Run from Source), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 3 (configuring cloud-native applications for deployment): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A managed container runtime that scales to zero and bills per request while it serves traffic. Why the correct answer wins: A job runs a task to completion and stops rather than serving traffic.
- **B:** Incorrect for this question. A cron-style trigger that calls a target on a fixed timetable. Why the correct answer wins: A job runs a task to completion and stops rather than serving traffic.
- **C:** Correct. A task-shaped execution that runs to completion instead of serving requests. In this case: A job runs a task to completion and stops rather than serving traffic.
- **D:** Incorrect for this question. An event-triggered function runtime for a single-purpose handler rather than a long-lived service. Why the correct answer wins: A job runs a task to completion and stops rather than serving traffic.

### Question 59 — B

Answer: Route the event with Eventarc. An event trigger delivers the bucket event to the service on arrival. A trigger path that turns a Cloud Audit Log or resource event into a delivery. Local study-map skill 3.2 (Cloud Run Triggers and Event Receivers), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 3 (configuring cloud-native applications for deployment): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A cron-style trigger that calls a target on a fixed timetable. Why the correct answer wins: An event trigger delivers the bucket event to the service on arrival.
- **B:** Correct. A trigger path that turns a Cloud Audit Log or resource event into a delivery. In this case: An event trigger delivers the bucket event to the service on arrival.
- **C:** Incorrect for this question. A durable, at-least-once message channel with independent subscribers. Why the correct answer wins: An event trigger delivers the bucket event to the service on arrival.
- **D:** Incorrect for this question. A stateful sequence of service calls with retries and error branches. Why the correct answer wins: An event trigger delivers the bucket event to the service on arrival.

### Question 60 — D

Answer: Deliver to an HTTPS push subscription. Push delivery posts each message to the endpoint the subscription names. Push each message to an endpoint instead of having the consumer pull. Local study-map skill 3.2 (Cloud Run Triggers and Event Receivers), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 3 (configuring cloud-native applications for deployment): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. The consumer controls the pace and acknowledges messages itself. Why the correct answer wins: Push delivery posts each message to the endpoint the subscription names.
- **B:** Incorrect for this question. A trigger path that turns a Cloud Audit Log or resource event into a delivery. Why the correct answer wins: Push delivery posts each message to the endpoint the subscription names.
- **C:** Incorrect for this question. A task queue with retries and rate control aimed at a specific target. Why the correct answer wins: Push delivery posts each message to the endpoint the subscription names.
- **D:** Correct. Push each message to an endpoint instead of having the consumer pull. In this case: Push delivery posts each message to the endpoint the subscription names.

### Question 61 — C

Answer: Schedule the invocation with Cloud Scheduler. A scheduled job sends the request on the declared timetable. A cron-style trigger that calls a target on a fixed timetable. Local study-map skill 3.2 (Cloud Run Triggers and Event Receivers), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 3 (configuring cloud-native applications for deployment): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A trigger path that turns a Cloud Audit Log or resource event into a delivery. Why the correct answer wins: A scheduled job sends the request on the declared timetable.
- **B:** Incorrect for this question. A stateful sequence of service calls with retries and error branches. Why the correct answer wins: A scheduled job sends the request on the declared timetable.
- **C:** Correct. A cron-style trigger that calls a target on a fixed timetable. In this case: A scheduled job sends the request on the declared timetable.
- **D:** Incorrect for this question. A task queue with retries and rate control aimed at a specific target. Why the correct answer wins: A scheduled job sends the request on the declared timetable.

### Question 62 — D, E

Answers: Raise the per-instance concurrency limit; Restrict ingress to internal traffic. Internal ingress blocks callers outside the network, and concurrency of one keeps a single request per instance. Let each instance serve more simultaneous requests before another instance is started. Accept only traffic from the VPC and internal load balancers. Local study-map skill 3.3 (Cloud Run Service Configuration), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 3 (configuring cloud-native applications for deployment): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A single anycast address that routes to the nearest healthy backend. Why the correct answer wins: Internal ingress blocks callers outside the network, and concurrency of one keeps a single request per instance.
- **B:** Incorrect for this question. Let anyone reach the endpoint, which is only appropriate for public content. Why the correct answer wins: Internal ingress blocks callers outside the network, and concurrency of one keeps a single request per instance.
- **C:** Incorrect for this question. Bound the blast radius and the bill at the cost of queueing when the cap is reached. Why the correct answer wins: Internal ingress blocks callers outside the network, and concurrency of one keeps a single request per instance.
- **D:** Correct. Accept only traffic from the VPC and internal load balancers. In this case: Internal ingress blocks callers outside the network, and concurrency of one keeps a single request per instance.
- **E:** Correct. Let each instance serve more simultaneous requests before another instance is started. In this case: Internal ingress blocks callers outside the network, and concurrency of one keeps a single request per instance.

### Question 63 — B

Answer: Keep a minimum number of instances warm. A minimum instance count keeps capacity warm through the idle period. Pay for idle capacity so a cold start never appears in the latency percentiles. Local study-map skill 3.3 (Cloud Run Service Configuration), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 3 (configuring cloud-native applications for deployment): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Speed initialization without paying for the extra CPU afterwards. Why the correct answer wins: A minimum instance count keeps capacity warm through the idle period.
- **B:** Correct. Pay for idle capacity so a cold start never appears in the latency percentiles. In this case: A minimum instance count keeps capacity warm through the idle period.
- **C:** Incorrect for this question. Bound the blast radius and the bill at the cost of queueing when the cap is reached. Why the correct answer wins: A minimum instance count keeps capacity warm through the idle period.
- **D:** Incorrect for this question. Charge only while a request is being handled, which suits bursty traffic. Why the correct answer wins: A minimum instance count keeps capacity warm through the idle period.

### Question 64 — C

Answer: Cap the maximum instance count. A maximum instance count caps the capacity the service can reach. Bound the blast radius and the bill at the cost of queueing when the cap is reached. Local study-map skill 3.3 (Cloud Run Service Configuration), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 3 (configuring cloud-native applications for deployment): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Charge for the whole instance lifetime, which suits steady background work. Why the correct answer wins: A maximum instance count caps the capacity the service can reach.
- **B:** Incorrect for this question. Pay for idle capacity so a cold start never appears in the latency percentiles. Why the correct answer wins: A maximum instance count caps the capacity the service can reach.
- **C:** Correct. Bound the blast radius and the bill at the cost of queueing when the cap is reached. In this case: A maximum instance count caps the capacity the service can reach.
- **D:** Incorrect for this question. Allow the process the headroom it needs so it is not throttled or killed. Why the correct answer wins: A maximum instance count caps the capacity the service can reach.

### Question 65 — C

Answer: Use API Gateway for the API. A managed gateway applies the key check to the declared API configs. A lighter managed gateway for routing and key-based quota enforcement. Local study-map skill 3.4 (API Exposure and Versioning), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 3 (configuring cloud-native applications for deployment): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Accept only traffic from the VPC and internal load balancers. Why the correct answer wins: A managed gateway applies the key check to the declared API configs.
- **B:** Incorrect for this question. An API management layer for quotas, keys, mediation and analytics. Why the correct answer wins: A managed gateway applies the key check to the declared API configs.
- **C:** Correct. A lighter managed gateway for routing and key-based quota enforcement. In this case: A managed gateway applies the key check to the declared API configs.
- **D:** Incorrect for this question. A single anycast address that routes to the nearest healthy backend. Why the correct answer wins: A managed gateway applies the key check to the declared API configs.

### Question 66 — C

Answer: Put Apigee in front of the API. The full API platform provides the quota, analytics and product layers. An API management layer for quotas, keys, mediation and analytics. Local study-map skill 3.4 (API Exposure and Versioning), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 3 (configuring cloud-native applications for deployment): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A managed container runtime that scales to zero and bills per request while it serves traffic. Why the correct answer wins: The full API platform provides the quota, analytics and product layers.
- **B:** Incorrect for this question. A single anycast address that routes to the nearest healthy backend. Why the correct answer wins: The full API platform provides the quota, analytics and product layers.
- **C:** Correct. An API management layer for quotas, keys, mediation and analytics. In this case: The full API platform provides the quota, analytics and product layers.
- **D:** Incorrect for this question. A lighter managed gateway for routing and key-based quota enforcement. Why the correct answer wins: The full API platform provides the quota, analytics and product layers.

### Question 67 — A, E

Answers: Use a rolling update strategy; Tune maxSurge and maxUnavailable. A rolling strategy replaces pods progressively, and the unavailable bound limits how many go at once. Replace pods gradually so the deployment stays available. Control how much capacity may be missing while pods are replaced. Local study-map skill 3.5 (Deploying Containers to GKE), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 3 (configuring cloud-native applications for deployment): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Correct. Replace pods gradually so the deployment stays available. In this case: A rolling strategy replaces pods progressively, and the unavailable bound limits how many go at once.
- **B:** Incorrect for this question. Place work on nodes whose shape and pricing match the workload. Why the correct answer wins: A rolling strategy replaces pods progressively, and the unavailable bound limits how many go at once.
- **C:** Incorrect for this question. Use reclaimable capacity for work that can tolerate a node disappearing. Why the correct answer wins: A rolling strategy replaces pods progressively, and the unavailable bound limits how many go at once.
- **D:** Incorrect for this question. Limit how many pods may be evicted at once during voluntary disruption. Why the correct answer wins: A rolling strategy replaces pods progressively, and the unavailable bound limits how many go at once.
- **E:** Correct. Control how much capacity may be missing while pods are replaced. In this case: A rolling strategy replaces pods progressively, and the unavailable bound limits how many go at once.

### Question 68 — A

Answer: Push the image to Artifact Registry. A scoped registry repository grants the pull to the cluster's identity only. A managed registry with IAM-scoped repositories per environment. Local study-map skill 3.5 (Deploying Containers to GKE), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 3 (configuring cloud-native applications for deployment): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Correct. A managed registry with IAM-scoped repositories per environment. In this case: A scoped registry repository grants the pull to the cluster's identity only.
- **B:** Incorrect for this question. The older registry whose access model is project-wide Cloud Storage. Why the correct answer wins: A scoped registry repository grants the pull to the cluster's identity only.
- **C:** Incorrect for this question. A managed build service that runs the steps from a build configuration file. Why the correct answer wins: A scoped registry repository grants the pull to the cluster's identity only.
- **D:** Incorrect for this question. Durable object storage addressed by name rather than a database row. Why the correct answer wins: A scoped registry repository grants the pull to the cluster's identity only.

### Question 69 — B

Answer: Run the batch node pool on Spot VMs. Interruptible nodes cost less for work that can restart. Use reclaimable capacity for work that can tolerate a node disappearing. Local study-map skill 3.5 (Deploying Containers to GKE), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 3 (configuring cloud-native applications for deployment): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Add or remove nodes as pending pods demand capacity. Why the correct answer wins: Interruptible nodes cost less for work that can restart.
- **B:** Correct. Use reclaimable capacity for work that can tolerate a node disappearing. In this case: Interruptible nodes cost less for work that can restart.
- **C:** Incorrect for this question. Place work on nodes whose shape and pricing match the workload. Why the correct answer wins: Interruptible nodes cost less for work that can restart.
- **D:** Incorrect for this question. Trade a term commitment for a lower unit price on capacity that never idles. Why the correct answer wins: Interruptible nodes cost less for work that can restart.

### Question 70 — A, C

Answers: Configure a startup probe; Configure a readiness probe. A startup probe gives the container time to boot, and a readiness probe holds traffic until it can serve. Hold traffic until the application is actually ready to serve. Remove the instance from the endpoint list while it cannot serve. Local study-map skill 3.6 (Kubernetes Health Checks), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 3 (configuring cloud-native applications for deployment): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Correct. Hold traffic until the application is actually ready to serve. In this case: A startup probe gives the container time to boot, and a readiness probe holds traffic until it can serve.
- **B:** Incorrect for this question. Control how much capacity may be missing while pods are replaced. Why the correct answer wins: A startup probe gives the container time to boot, and a readiness probe holds traffic until it can serve.
- **C:** Correct. Remove the instance from the endpoint list while it cannot serve. In this case: A startup probe gives the container time to boot, and a readiness probe holds traffic until it can serve.
- **D:** Incorrect for this question. Replace pods gradually so the deployment stays available. Why the correct answer wins: A startup probe gives the container time to boot, and a readiness probe holds traffic until it can serve.
- **E:** Incorrect for this question. Restart the container when it can no longer make progress. Why the correct answer wins: A startup probe gives the container time to boot, and a readiness probe holds traffic until it can serve.

### Question 71 — B

Answer: Configure a liveness probe. A liveness probe restarts a container that is running but unresponsive. Restart the container when it can no longer make progress. Local study-map skill 3.6 (Kubernetes Health Checks), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 3 (configuring cloud-native applications for deployment): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Limit how many pods may be evicted at once during voluntary disruption. Why the correct answer wins: A liveness probe restarts a container that is running but unresponsive.
- **B:** Correct. Restart the container when it can no longer make progress. In this case: A liveness probe restarts a container that is running but unresponsive.
- **C:** Incorrect for this question. Remove the instance from the endpoint list while it cannot serve. Why the correct answer wins: A liveness probe restarts a container that is running but unresponsive.
- **D:** Incorrect for this question. Hold traffic until the application is actually ready to serve. Why the correct answer wins: A liveness probe restarts a container that is running but unresponsive.

### Question 72 — A

Answer: Scale pods on a custom or external metric. A custom metric scales on the signal that actually tracks the backlog. Add pods on a signal that tracks demand better than CPU. Local study-map skill 3.7 (Horizontal Pod Autoscaling), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 3 (configuring cloud-native applications for deployment): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Correct. Add pods on a signal that tracks demand better than CPU. In this case: A custom metric scales on the signal that actually tracks the backlog.
- **B:** Incorrect for this question. Add or remove nodes as pending pods demand capacity. Why the correct answer wins: A custom metric scales on the signal that actually tracks the backlog.
- **C:** Incorrect for this question. Add pods when average CPU crosses the target. Why the correct answer wins: A custom metric scales on the signal that actually tracks the backlog.
- **D:** Incorrect for this question. Trade a term commitment for a lower unit price on capacity that never idles. Why the correct answer wins: A custom metric scales on the signal that actually tracks the backlog.

### Question 73 — A

Answer: Set a minimum replica count. A minimum replica count keeps the service present through idle periods. Keep capacity warm so scale-up does not cost the first requests. Local study-map skill 3.7 (Horizontal Pod Autoscaling), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 3 (configuring cloud-native applications for deployment): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Correct. Keep capacity warm so scale-up does not cost the first requests. In this case: A minimum replica count keeps the service present through idle periods.
- **B:** Incorrect for this question. Limit how many pods may be evicted at once during voluntary disruption. Why the correct answer wins: A minimum replica count keeps the service present through idle periods.
- **C:** Incorrect for this question. Bound the blast radius and the bill at the cost of queueing when the cap is reached. Why the correct answer wins: A minimum replica count keeps the service present through idle periods.
- **D:** Incorrect for this question. Add or remove nodes as pending pods demand capacity. Why the correct answer wins: A minimum replica count keeps the service present through idle periods.

### Question 74 — C

Answer: Scale pods on CPU utilization. Scaling on CPU utilisation follows the signal the parser saturates. Add pods when average CPU crosses the target. Local study-map skill 3.7 (Horizontal Pod Autoscaling), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 3 (configuring cloud-native applications for deployment): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Keep capacity warm so scale-up does not cost the first requests. Why the correct answer wins: Scaling on CPU utilisation follows the signal the parser saturates.
- **B:** Incorrect for this question. Add or remove nodes as pending pods demand capacity. Why the correct answer wins: Scaling on CPU utilisation follows the signal the parser saturates.
- **C:** Correct. Add pods when average CPU crosses the target. In this case: Scaling on CPU utilisation follows the signal the parser saturates.
- **D:** Incorrect for this question. Add pods on a signal that tracks demand better than CPU. Why the correct answer wins: Scaling on CPU utilisation follows the signal the parser saturates.

### Question 75 — C

Answer: Build the image with Cloud Build. A declared build pipeline runs the compile step the buildpack skips. A managed build service that runs the steps from a build configuration file. Local study-map skill 3.1 (Deploying Cloud Run from Source), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 3 (configuring cloud-native applications for deployment): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Speed initialization without paying for the extra CPU afterwards. Why the correct answer wins: A declared build pipeline runs the compile step the buildpack skips.
- **B:** Incorrect for this question. Let each instance serve more simultaneous requests before another instance is started. Why the correct answer wins: A declared build pipeline runs the compile step the buildpack skips.
- **C:** Correct. A managed build service that runs the steps from a build configuration file. In this case: A declared build pipeline runs the compile step the buildpack skips.
- **D:** Incorrect for this question. Bound the blast radius and the bill at the cost of queueing when the cap is reached. Why the correct answer wins: A declared build pipeline runs the compile step the buildpack skips.

### Question 76 — C

Answer: Queue the work as a Cloud Tasks task. Enqueuing the work lets the queue retry it after the deadline. A task queue with retries and rate control aimed at a specific target. Local study-map skill 3.2 (Cloud Run Triggers and Event Receivers), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 3 (configuring cloud-native applications for deployment): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Push each message to an endpoint instead of having the consumer pull. Why the correct answer wins: Enqueuing the work lets the queue retry it after the deadline.
- **B:** Incorrect for this question. A trigger path that turns a Cloud Audit Log or resource event into a delivery. Why the correct answer wins: Enqueuing the work lets the queue retry it after the deadline.
- **C:** Correct. A task queue with retries and rate control aimed at a specific target. In this case: Enqueuing the work lets the queue retry it after the deadline.
- **D:** Incorrect for this question. A cron-style trigger that calls a target on a fixed timetable. Why the correct answer wins: Enqueuing the work lets the queue retry it after the deadline.

### Question 77 — A

Answer: Enable CPU boost at startup. Keeping CPU allocated outside the request lets the follow-up finish. Give extra CPU during start-up so initialization finishes faster at a small extra charge. Local study-map skill 3.3 (Cloud Run Service Configuration), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 3 (configuring cloud-native applications for deployment): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Correct. Give extra CPU during start-up so initialization finishes faster at a small extra charge. In this case: Keeping CPU allocated outside the request lets the follow-up finish.
- **B:** Incorrect for this question. Pay for idle capacity so a cold start never appears in the latency percentiles. Why the correct answer wins: Keeping CPU allocated outside the request lets the follow-up finish.
- **C:** Incorrect for this question. Charge for the whole instance lifetime, which suits steady background work. Why the correct answer wins: Keeping CPU allocated outside the request lets the follow-up finish.
- **D:** Incorrect for this question. Let each instance serve more simultaneous requests before another instance is started. Why the correct answer wins: Keeping CPU allocated outside the request lets the follow-up finish.

### Question 78 — A

Answer: Enable node pool autoscaling. Node pool autoscaling adds nodes when pods cannot be scheduled. Add or remove nodes as pending pods demand capacity. Local study-map skill 3.5 (Deploying Containers to GKE), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 3 (configuring cloud-native applications for deployment): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Correct. Add or remove nodes as pending pods demand capacity. In this case: Node pool autoscaling adds nodes when pods cannot be scheduled.
- **B:** Incorrect for this question. Use reclaimable capacity for work that can tolerate a node disappearing. Why the correct answer wins: Node pool autoscaling adds nodes when pods cannot be scheduled.
- **C:** Incorrect for this question. Trade a term commitment for a lower unit price on capacity that never idles. Why the correct answer wins: Node pool autoscaling adds nodes when pods cannot be scheduled.
- **D:** Incorrect for this question. Add pods when average CPU crosses the target. Why the correct answer wins: Node pool autoscaling adds nodes when pods cannot be scheduled.

### Question 79 — D

Answer: Add a PodDisruptionBudget. A disruption budget bounds how many pods maintenance may evict together. Limit how many pods may be evicted at once during voluntary disruption. Local study-map skill 3.6 (Kubernetes Health Checks), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 3 (configuring cloud-native applications for deployment): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Control how much capacity may be missing while pods are replaced. Why the correct answer wins: A disruption budget bounds how many pods maintenance may evict together.
- **B:** Incorrect for this question. Hold traffic until the application is actually ready to serve. Why the correct answer wins: A disruption budget bounds how many pods maintenance may evict together.
- **C:** Incorrect for this question. Restart the container when it can no longer make progress. Why the correct answer wins: A disruption budget bounds how many pods maintenance may evict together.
- **D:** Correct. Limit how many pods may be evicted at once during voluntary disruption. In this case: A disruption budget bounds how many pods maintenance may evict together.

### Question 80 — A, B

Answers: Connect through the Cloud SQL Auth Proxy; Pool and reuse database connections. A connector pool reuses connections instead of opening one per request, and the connector replaces the public path with an authorised tunnel. A local proxy that authorizes the connection with IAM and encrypts it. Keep a small set of warm connections instead of opening one per request. Local study-map skill 4.1 (Connecting to Datastores), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 4 (integrating applications with Google Cloud services): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Correct. Keep a small set of warm connections instead of opening one per request. In this case: A connector pool reuses connections instead of opening one per request, and the connector replaces the public path with an authorised tunnel.
- **B:** Correct. A local proxy that authorizes the connection with IAM and encrypts it. In this case: A connector pool reuses connections instead of opening one per request, and the connector replaces the public path with an authorised tunnel.
- **C:** Incorrect for this question. A private address reachable from the VPC without a proxy process. Why the correct answer wins: A connector pool reuses connections instead of opening one per request, and the connector replaces the public path with an authorised tunnel.
- **D:** Incorrect for this question. A reachable address that requires encrypted connections from any client. Why the correct answer wins: A connector pool reuses connections instead of opening one per request, and the connector replaces the public path with an authorised tunnel.
- **E:** Incorrect for this question. A client library that resolves and authorizes the instance itself. Why the correct answer wins: A connector pool reuses connections instead of opening one per request, and the connector replaces the public path with an authorised tunnel.

### Question 81 — A

Answer: Use the language connector with IAM. The client connector library authenticates in-process without a separate proxy. A client library that resolves and authorizes the instance itself. Local study-map skill 4.1 (Connecting to Datastores), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 4 (integrating applications with Google Cloud services): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Correct. A client library that resolves and authorizes the instance itself. In this case: The client connector library authenticates in-process without a separate proxy.
- **B:** Incorrect for this question. A private address reachable from the VPC without a proxy process. Why the correct answer wins: The client connector library authenticates in-process without a separate proxy.
- **C:** Incorrect for this question. A local proxy that authorizes the connection with IAM and encrypts it. Why the correct answer wins: The client connector library authenticates in-process without a separate proxy.
- **D:** Incorrect for this question. Change the engine-level connection limit without resizing the machine. Why the correct answer wins: The client connector library authenticates in-process without a separate proxy.

### Question 82 — B

Answer: Connect through the AlloyDB Auth Proxy. The proxy authenticates and terminates TLS for the cluster connection. The equivalent authorized connector for AlloyDB instances. Local study-map skill 4.1 (Connecting to Datastores), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 4 (integrating applications with Google Cloud services): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A local proxy that authorizes the connection with IAM and encrypts it. Why the correct answer wins: The proxy authenticates and terminates TLS for the cluster connection.
- **B:** Correct. The equivalent authorized connector for AlloyDB instances. In this case: The proxy authenticates and terminates TLS for the cluster connection.
- **C:** Incorrect for this question. A client library that resolves and authorizes the instance itself. Why the correct answer wins: The proxy authenticates and terminates TLS for the cluster connection.
- **D:** Incorrect for this question. A private endpoint that consumes a published service without peering. Why the correct answer wins: The proxy authenticates and terminates TLS for the cluster connection.

### Question 83 — C

Answer: Connect over the database private IP. A private address keeps the instance off the public internet entirely. A private address reachable from the VPC without a proxy process. Local study-map skill 4.1 (Connecting to Datastores), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 4 (integrating applications with Google Cloud services): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A private endpoint that consumes a published service without peering. Why the correct answer wins: A private address keeps the instance off the public internet entirely.
- **B:** Incorrect for this question. A reachable address that requires encrypted connections from any client. Why the correct answer wins: A private address keeps the instance off the public internet entirely.
- **C:** Correct. A private address reachable from the VPC without a proxy process. In this case: A private address keeps the instance off the public internet entirely.
- **D:** Incorrect for this question. A local proxy that authorizes the connection with IAM and encrypts it. Why the correct answer wins: A private address keeps the instance off the public internet entirely.

### Question 84 — B

Answer: Have the worker pull from the subscription. Pull delivery lets the consumer choose when to fetch and acknowledge. The consumer controls the pace and acknowledges messages itself. Local study-map skill 4.2 (Publishing and Consuming Messages), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 4 (integrating applications with Google Cloud services): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A trigger path that turns a Cloud Audit Log or resource event into a delivery. Why the correct answer wins: Pull delivery lets the consumer choose when to fetch and acknowledge.
- **B:** Correct. The consumer controls the pace and acknowledges messages itself. In this case: Pull delivery lets the consumer choose when to fetch and acknowledge.
- **C:** Incorrect for this question. Push each message to an endpoint instead of having the consumer pull. Why the correct answer wins: Pull delivery lets the consumer choose when to fetch and acknowledge.
- **D:** Incorrect for this question. A task queue with retries and rate control aimed at a specific target. Why the correct answer wins: Pull delivery lets the consumer choose when to fetch and acknowledge.

### Question 85 — B

Answer: Add a dead-letter topic. A dead-letter topic moves messages that exceed the delivery attempts. Hold messages that exhausted their delivery attempts for later inspection. Local study-map skill 4.2 (Publishing and Consuming Messages), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 4 (integrating applications with Google Cloud services): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Make the retention period impossible to shorten, even by an owner. Why the correct answer wins: A dead-letter topic moves messages that exceed the delivery attempts.
- **B:** Correct. Hold messages that exhausted their delivery attempts for later inspection. In this case: A dead-letter topic moves messages that exceed the delivery attempts.
- **C:** Incorrect for this question. Space out repeated attempts so a throttled quota can recover instead of being hammered. Why the correct answer wins: A dead-letter topic moves messages that exceed the delivery attempts.
- **D:** Incorrect for this question. Write topic messages straight into a table without a consumer. Why the correct answer wins: A dead-letter topic moves messages that exceed the delivery attempts.

### Question 86 — B

Answer: Make the handler idempotent with a deduplication key. An idempotency key lets a repeated delivery be recognised and ignored. Recognise a repeated delivery and skip the duplicate work. Local study-map skill 4.2 (Publishing and Consuming Messages), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 4 (integrating applications with Google Cloud services): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Trim the response payload so latency and cost follow actual use. Why the correct answer wins: An idempotency key lets a repeated delivery be recognised and ignored.
- **B:** Correct. Recognise a repeated delivery and skip the duplicate work. In this case: An idempotency key lets a repeated delivery be recognised and ignored.
- **C:** Incorrect for this question. The consumer controls the pace and acknowledges messages itself. Why the correct answer wins: An idempotency key lets a repeated delivery be recognised and ignored.
- **D:** Incorrect for this question. Space out repeated attempts so a throttled quota can recover instead of being hammered. Why the correct answer wins: An idempotency key lets a repeated delivery be recognised and ignored.

### Question 87 — C

Answer: Use a BigQuery subscription on the topic. A subscription that writes to the table removes the consumer service. Write topic messages straight into a table without a consumer. Local study-map skill 4.2 (Publishing and Consuming Messages), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 4 (integrating applications with Google Cloud services): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Push each message to an endpoint instead of having the consumer pull. Why the correct answer wins: A subscription that writes to the table removes the consumer service.
- **B:** Incorrect for this question. Land analytics rows in the warehouse for SQL and ML use. Why the correct answer wins: A subscription that writes to the table removes the consumer service.
- **C:** Correct. Write topic messages straight into a table without a consumer. In this case: A subscription that writes to the table removes the consumer service.
- **D:** Incorrect for this question. The consumer controls the pace and acknowledges messages itself. Why the correct answer wins: A subscription that writes to the table removes the consumer service.

### Question 88 — D

Answer: Retry with exponential backoff and jitter. Exponential backoff waits longer after each failure instead of retrying immediately. Space out repeated attempts so a throttled quota can recover instead of being hammered. Local study-map skill 4.3 (Calling Google Cloud APIs), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 4 (integrating applications with Google Cloud services): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Allow the process the headroom it needs so it is not throttled or killed. Why the correct answer wins: Exponential backoff waits longer after each failure instead of retrying immediately.
- **B:** Incorrect for this question. Reduce per-call overhead when the API supports a batch surface. Why the correct answer wins: Exponential backoff waits longer after each failure instead of retrying immediately.
- **C:** Incorrect for this question. Bound how many calls a plan allows in a window. Why the correct answer wins: Exponential backoff waits longer after each failure instead of retrying immediately.
- **D:** Correct. Space out repeated attempts so a throttled quota can recover instead of being hammered. In this case: Exponential backoff waits longer after each failure instead of retrying immediately.

### Question 89 — B

Answer: Follow the page token until results are exhausted. Following page tokens retrieves the remaining results. Request each page in turn so a truncated response is completed rather than assumed whole. Local study-map skill 4.3 (Calling Google Cloud APIs), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 4 (integrating applications with Google Cloud services): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Reduce per-call overhead when the API supports a batch surface. Why the correct answer wins: Following page tokens retrieves the remaining results.
- **B:** Correct. Request each page in turn so a truncated response is completed rather than assumed whole. In this case: Following page tokens retrieves the remaining results.
- **C:** Incorrect for this question. Trim the response payload so latency and cost follow actual use. Why the correct answer wins: Following page tokens retrieves the remaining results.
- **D:** Incorrect for this question. Reuse a result that has not changed, avoiding an identical call. Why the correct answer wins: Following page tokens retrieves the remaining results.

### Question 90 — D

Answer: Request only the fields the caller needs. A field mask returns only the named fields. Trim the response payload so latency and cost follow actual use. Local study-map skill 4.3 (Calling Google Cloud APIs), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 4 (integrating applications with Google Cloud services): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Reuse a result that has not changed, avoiding an identical call. Why the correct answer wins: A field mask returns only the named fields.
- **B:** Incorrect for this question. Request each page in turn so a truncated response is completed rather than assumed whole. Why the correct answer wins: A field mask returns only the named fields.
- **C:** Incorrect for this question. Reduce per-call overhead when the API supports a batch surface. Why the correct answer wins: A field mask returns only the named fields.
- **D:** Correct. Trim the response payload so latency and cost follow actual use. In this case: A field mask returns only the named fields.

### Question 91 — D

Answer: Cache the response for its freshness window. Caching the response avoids repeating the call for data that rarely changes. Reuse a result that has not changed, avoiding an identical call. Local study-map skill 4.3 (Calling Google Cloud APIs), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 4 (integrating applications with Google Cloud services): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Request each page in turn so a truncated response is completed rather than assumed whole. Why the correct answer wins: Caching the response avoids repeating the call for data that rarely changes.
- **B:** Incorrect for this question. Trim the response payload so latency and cost follow actual use. Why the correct answer wins: Caching the response avoids repeating the call for data that rarely changes.
- **C:** Incorrect for this question. Space out repeated attempts so a throttled quota can recover instead of being hammered. Why the correct answer wins: Caching the response avoids repeating the call for data that rarely changes.
- **D:** Correct. Reuse a result that has not changed, avoiding an identical call. In this case: Caching the response avoids repeating the call for data that rarely changes.

### Question 92 — A

Answer: Give the workload its own service account. A dedicated identity with the bucket role and nothing more limits the blast radius. A dedicated identity whose roles can be granted and revoked independently. Local study-map skill 4.4 (Service Accounts for API Calls), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 4 (integrating applications with Google Cloud services): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Correct. A dedicated identity whose roles can be granted and revoked independently. In this case: A dedicated identity with the bucket role and nothing more limits the blast radius.
- **B:** Incorrect for this question. The automatically created identity that usually carries broad project access. Why the correct answer wins: A dedicated identity with the bucket role and nothing more limits the blast radius.
- **C:** Incorrect for this question. A legacy broad role that can change most resources in the project. Why the correct answer wins: A dedicated identity with the bucket role and nothing more limits the blast radius.
- **D:** Incorrect for this question. A long-lived credential that has to be stored and rotated by hand. Why the correct answer wins: A dedicated identity with the bucket role and nothing more limits the blast radius.

### Question 93 — D

Answer: Federate the external identity with Workload Identity Federation. Federating the external identity exchanges a short-lived token for access. Exchange an outside token for a short-lived Google credential. Local study-map skill 4.4 (Service Accounts for API Calls), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 4 (integrating applications with Google Cloud services): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A long-lived credential that has to be stored and rotated by hand. Why the correct answer wins: Federating the external identity exchanges a short-lived token for access.
- **B:** Incorrect for this question. A dedicated identity whose roles can be granted and revoked independently. Why the correct answer wins: Federating the external identity exchanges a short-lived token for access.
- **C:** Incorrect for this question. Let the client library find credentials from the environment. Why the correct answer wins: Federating the external identity exchanges a short-lived token for access.
- **D:** Correct. Exchange an outside token for a short-lived Google credential. In this case: Federating the external identity exchanges a short-lived token for access.

### Question 94 — A, B

Answers: Emit structured JSON logs; Instrument a span around the downstream call. Structured logs make severity and labels queryable, and spans show where the time went inside the request. Emit fields the log viewer can index so queries and alerts are possible. Show where time goes inside a request that crosses services. Local study-map skill 4.5 (Metrics, Logs, and Traces), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 4 (integrating applications with Google Cloud services): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Correct. Emit fields the log viewer can index so queries and alerts are possible. In this case: Structured logs make severity and labels queryable, and spans show where the time went inside the request.
- **B:** Correct. Show where time goes inside a request that crosses services. In this case: Structured logs make severity and labels queryable, and spans show where the time went inside the request.
- **C:** Incorrect for this question. Publish an application signal that infrastructure metrics cannot see. Why the correct answer wins: Structured logs make severity and labels queryable, and spans show where the time went inside the request.
- **D:** Incorrect for this question. Notify a human when a threshold is crossed. Why the correct answer wins: Structured logs make severity and labels queryable, and spans show where the time went inside the request.
- **E:** Incorrect for this question. Turn a recurring log pattern into a number that can be charted and alerted on. Why the correct answer wins: Structured logs make severity and labels queryable, and spans show where the time went inside the request.

### Question 95 — D

Answer: Emit a custom metric from the code. A user-defined metric carries the ratio the product does not emit. Publish an application signal that infrastructure metrics cannot see. Local study-map skill 4.5 (Metrics, Logs, and Traces), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 4 (integrating applications with Google Cloud services): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Notify a human when a threshold is crossed. Why the correct answer wins: A user-defined metric carries the ratio the product does not emit.
- **B:** Incorrect for this question. Turn a recurring log pattern into a number that can be charted and alerted on. Why the correct answer wins: A user-defined metric carries the ratio the product does not emit.
- **C:** Incorrect for this question. Page on the rate at which reliability is being spent. Why the correct answer wins: A user-defined metric carries the ratio the product does not emit.
- **D:** Correct. Publish an application signal that infrastructure metrics cannot see. In this case: A user-defined metric carries the ratio the product does not emit.

### Question 96 — D

Answer: Send the exception to Error Reporting. Grouping and tracking makes new error groups visible. Group and count application errors instead of grepping logs. Local study-map skill 4.6 (Error Reporting and Trace Correlation), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 4 (integrating applications with Google Cloud services): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Turn a recurring log pattern into a number that can be charted and alerted on. Why the correct answer wins: Grouping and tracking makes new error groups visible.
- **B:** Incorrect for this question. Notify a human when a threshold is crossed. Why the correct answer wins: Grouping and tracking makes new error groups visible.
- **C:** Incorrect for this question. Read variable state in a running deployment without redeploying. Why the correct answer wins: Grouping and tracking makes new error groups visible.
- **D:** Correct. Group and count application errors instead of grepping logs. In this case: Grouping and tracking makes new error groups visible.

### Question 97 — B

Answer: Propagate the trace ID between services. Passing the trace header joins the services into one trace. Join spans from different services into one trace. Local study-map skill 4.6 (Error Reporting and Trace Correlation), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 4 (integrating applications with Google Cloud services): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Let filters and alerting distinguish routine output from errors. Why the correct answer wins: Passing the trace header joins the services into one trace.
- **B:** Correct. Join spans from different services into one trace. In this case: Passing the trace header joins the services into one trace.
- **C:** Incorrect for this question. Emit fields the log viewer can index so queries and alerts are possible. Why the correct answer wins: Passing the trace header joins the services into one trace.
- **D:** Incorrect for this question. Show where time goes inside a request that crosses services. Why the correct answer wins: Passing the trace header joins the services into one trace.

### Question 98 — B

Answer: Ask Gemini Cloud Assist for a diagnosis. An AI assistant summarises the incident context instead of manual searching. An assistant that reads telemetry and proposes a cause and a next step. Local study-map skill 4.7 (AI-Assisted Observability), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 4 (integrating applications with Google Cloud services): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Give the assistant a defined tool surface instead of pasting context by hand. Why the correct answer wins: An AI assistant summarises the incident context instead of manual searching.
- **B:** Correct. An assistant that reads telemetry and proposes a cause and a next step. In this case: An AI assistant summarises the incident context instead of manual searching.
- **C:** Incorrect for this question. Group and count application errors instead of grepping logs. Why the correct answer wins: An AI assistant summarises the incident context instead of manual searching.
- **D:** Incorrect for this question. Generate a first draft from context, then review and correct it. Why the correct answer wins: An AI assistant summarises the incident context instead of manual searching.

### Question 99 — A

Answer: Raise the database connection ceiling by flag. Capping connections per instance keeps the fleet inside the instance limit. Change the engine-level connection limit without resizing the machine. Local study-map skill 4.1 (Connecting to Datastores), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 4 (integrating applications with Google Cloud services): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Correct. Change the engine-level connection limit without resizing the machine. In this case: Capping connections per instance keeps the fleet inside the instance limit.
- **B:** Incorrect for this question. A client library that resolves and authorizes the instance itself. Why the correct answer wins: Capping connections per instance keeps the fleet inside the instance limit.
- **C:** Incorrect for this question. A private address reachable from the VPC without a proxy process. Why the correct answer wins: Capping connections per instance keeps the fleet inside the instance limit.
- **D:** Incorrect for this question. The equivalent authorized connector for AlloyDB instances. Why the correct answer wins: Capping connections per instance keeps the fleet inside the instance limit.

### Question 100 — D

Answer: Alert on the error budget burn rate. Alerting on the objective's error budget tracks the reliability users feel. Page on the rate at which reliability is being spent. Local study-map skill 4.5 (Metrics, Logs, and Traces), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 4 (integrating applications with Google Cloud services): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Turn a recurring log pattern into a number that can be charted and alerted on. Why the correct answer wins: Alerting on the objective's error budget tracks the reliability users feel.
- **B:** Incorrect for this question. Notify a human when a threshold is crossed. Why the correct answer wins: Alerting on the objective's error budget tracks the reliability users feel.
- **C:** Incorrect for this question. Publish an application signal that infrastructure metrics cannot see. Why the correct answer wins: Alerting on the objective's error budget tracks the reliability users feel.
- **D:** Correct. Page on the rate at which reliability is being spent. In this case: Alerting on the objective's error budget tracks the reliability users feel.
