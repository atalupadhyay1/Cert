# Google Cloud Professional Cloud Developer — Full-Length Mock Exam 2

Professional Cloud Developer · 100 questions · expanded practice bank · passing score not published

Blueprint-weighted mock exam. Item mix: 84 multiple-choice and 16 multiple-select items (the selection count is stated in each multi-select stem). The live exam publishes 50-60 multiple-choice and multiple-select questions and has no case-study component, so this set is larger on purpose and no case-study item is reproduced. The live paper allows two hours for 50-60 items, so this 100-item set is a slower-per-item rehearsal: about 72 seconds per item here against roughly 120-144 seconds live. Use it to build a habit of finishing with time to review. See the README for the exact fidelity boundary.

Original educational content, not actual, recalled, or copied Google exam items.

## Questions

---

## Domain 1 — Designing Highly Scalable, Secure, and Reliable Cloud-Native Applications (Compute Choice, APIs, and Secure Design)

### 1. A startup has one containerised HTTP API, a team with no Kubernetes experience, and traffic that is zero most nights. Which platform fits?

- A. Deploy the workload to Google Kubernetes Engine
- B. Deploy the service to Cloud Run
- C. Run the application on Compute Engine instances
- D. Deploy the handler as a Cloud Functions function

### 2. A platform team must run a StatefulSet with persistent volumes and a custom scheduler profile. Which platform fits?

- A. Deploy to App Engine standard
- B. Deploy the service to Cloud Run
- C. Deploy the handler as a Cloud Functions function
- D. Deploy the workload to Google Kubernetes Engine

### 3. A single handler must run whenever a file lands in a bucket, with no server to keep warm. Which runtime fits?

- A. Run the application on Compute Engine instances
- B. Deploy the workload to Google Kubernetes Engine
- C. Deploy the service to Cloud Run
- D. Deploy the handler as a Cloud Functions function

### 4. A service must move between environments with byte-identical dependencies and no rebuild per environment. What should the team produce?

- A. Deploy to App Engine standard
- B. Deploy from source and let the platform build it
- C. Package the monolith into a container image
- D. Deploy the handler as a Cloud Functions function

### 5. A service must survive a zone failure without operator action and must stop sending traffic to an unhealthy instance. Which two measures fit? Select two.

- A. Place the workload in a single zone
- B. Deploy in one region across multiple zones
- C. Deploy the service in two regions behind a global load balancer
- D. Add a health check endpoint to the backend service
- E. Buy committed use discounts for the steady baseline

### 6. Users on three continents report slow first-byte times to a single-region service. What should the team add in front of it?

- A. Buy committed use discounts for the steady baseline
- B. Put a global external Application Load Balancer in front
- C. Serve static content from Cloud CDN
- D. Use a regional load balancer

### 7. An autoscaled tier loses in-flight sessions whenever a scale-in removes an instance. What should the team change?

- A. Use a generated cookie for stickiness
- B. Enable session affinity on the backend service
- C. Cache reads in Memorystore
- D. Store session state in a shared datastore

### 8. A backend instance hangs but keeps its address, and clients keep waiting on it. What should the load balancer be given?

- A. Serve static content from Cloud CDN
- B. Use a regional load balancer
- C. Enable session affinity on the backend service
- D. Add a health check endpoint to the backend service

### 9. Two instances return different prices for the same product after an update, and the product team needs one shared value. What should the team use?

- A. Serve static content from Cloud CDN
- B. Cache reads in Memorystore
- C. Load through a cache-aside pattern
- D. Cache inside each instance process

### 10. Reads are fast after warm-up but every deploy starts cold and the database spikes. What pattern keeps the cache useful across restarts?

- A. Load through a cache-aside pattern
- B. Cache reads in Memorystore
- C. Cache inside each instance process
- D. Serve static content from Cloud CDN

### 11. A public partner needs to call the API from a spreadsheet script with plain HTTP and no client generation. Which interface fits?

- A. Serve gRPC-Web for browser clients
- B. Publish an OpenAPI specification
- C. Expose a gRPC service
- D. Expose a REST API with JSON payloads

### 12. A browser dashboard must call an existing gRPC backend without a proxy service. What should the team serve?

- A. Expose a REST API with JSON payloads
- B. Serve gRPC-Web for browser clients
- C. Publish an OpenAPI specification
- D. Expose a gRPC service

### 13. A public API must support two contract versions at once and apply plan-based quotas per key. Which two capabilities are needed? Select two.

- A. Introduce a new API version alongside the old one
- B. Grant the basic editor role
- C. Put Apigee in front of the API
- D. Apply a rate limit per client key
- E. Use API Gateway for the API

### 14. A small internal API needs routing and key-based quotas with minimal operational overhead. Which service fits?

- A. Apply a rate limit per client key
- B. Use API Gateway for the API
- C. Put Apigee in front of the API
- D. Put Identity-Aware Proxy in front of the service

### 15. A checkout service must notify inventory, email and analytics without waiting on any of them. What should it publish to?

- A. Publish the event to a Pub/Sub topic
- B. Orchestrate the steps in Workflows
- C. Queue the work as a Cloud Tasks task
- D. Schedule the invocation with Cloud Scheduler

### 16. A consumer both reprocesses duplicates and stalls on a poison message. Which two fixes are needed? Select two.

- A. Have the worker pull from the subscription
- B. Route the event with Eventarc
- C. Make the handler idempotent with a deduplication key
- D. Queue the work as a Cloud Tasks task
- E. Add a dead-letter topic

### 17. A service wakes for a few minutes every hour and is otherwise idle, and the bill is dominated by idle time. Which billing mode fits?

- A. Use instance-based billing
- B. Use request-based billing
- C. Buy committed use discounts for the steady baseline
- D. Keep a minimum number of instances warm

### 18. A nightly rendering job can lose a node at any moment, and the queue can retry. What should the job's pool run on?

- A. Enable node pool autoscaling
- B. Buy committed use discounts for the steady baseline
- C. Set CPU and memory requests from measured use
- D. Run the batch node pool on Spot VMs

### 19. A team wants the smallest possible exposure before widening a risky change, with a measurable gate. What should it do first?

- A. Shift traffic back to the previous revision
- B. Split traffic between revisions by percentage
- C. Canary the release at a small percentage first
- D. Gate the change behind a feature flag

### 20. A release must be dark-launched to an internal cohort and later widened without a redeploy. Which two mechanisms fit? Select two.

- A. Canary the release at a small percentage first
- B. Gate the change behind a feature flag
- C. Route by revision tag or header
- D. Split traffic between revisions by percentage
- E. Shift traffic back to the previous revision

### 21. A slow third-party call must be retried on its own schedule without blocking the request that created it. What should the service enqueue?

- A. Queue the work as a Cloud Tasks task
- B. Orchestrate the steps in Workflows
- C. Publish the event to a Pub/Sub topic
- D. Schedule the invocation with Cloud Scheduler

### 22. A regulator requires that stored records cannot be deleted early, not even by a project owner. What should the team configure?

- A. Make the bucket public
- B. Lock the bucket retention policy
- C. Issue a signed URL with a short expiry
- D. Add a lifecycle rule to the bucket

### 23. A container must read a token that never appears in the image or in the process environment. Which two choices fit? Select two.

- A. Store the credential in Secret Manager
- B. Grant the basic editor role
- C. Mount the secret as a volume
- D. Download a service account key file
- E. Set the credential as an environment variable

### 24. A credential is suspected to have leaked and must stop working within the hour. What should the team do?

- A. Rotate the secret on a schedule
- B. Store the credential in Secret Manager
- C. Download a service account key file
- D. Use a customer-managed encryption key

### 25. Two services share the default compute identity, so a role granted to one silently widens the other. What should the team do?

- A. Download a service account key file
- B. Rely on Application Default Credentials
- C. Let the workload use the default compute service account
- D. Give the workload its own service account

### 26. A CI system outside Google Cloud must call the API without storing any Google credential. What should the team use?

- A. Download a service account key file
- B. Rely on Application Default Credentials
- C. Bind a Kubernetes service account to a Google service account
- D. Federate the external identity with Workload Identity Federation

### 27. Inside one cluster, a compromised front-end pod reached a database pod it should never touch. What should the team apply?

- A. Use Cloud Service Mesh for service-to-service traffic
- B. Set a namespace resource quota
- C. Apply a Kubernetes NetworkPolicy
- D. Put Identity-Aware Proxy in front of the service

### 28. A security review wants every service call authenticated and every identity scoped to the calls it makes. Which two measures fit? Select two.

- A. Allow unauthenticated invocations
- B. Apply a Kubernetes NetworkPolicy
- C. Grant only the roles the workload needs
- D. Grant the basic editor role
- E. Use Cloud Service Mesh for service-to-service traffic

### 29. A cross-border settlement system must reject any transfer that would leave two regional balances inconsistent. Which store fits?

- A. Use Firestore in Native mode
- B. Store the ledger in Spanner
- C. Store the objects in Cloud Storage
- D. Design the row key for the read pattern

### 30. A media service stores multi-gigabyte video masters that are read rarely and never queried by field. Which store fits?

- A. Use Firestore in Native mode
- B. Cache reads in Memorystore
- C. Store the ledger in Spanner
- D. Store the objects in Cloud Storage

### 31. A user must upload one file directly to storage for a short window without the service relaying the bytes. What should the service issue?

- A. Make the bucket public
- B. Add a lifecycle rule to the bucket
- C. Issue a signed URL with a short expiry
- D. Lock the bucket retention policy

### 32. A fraud model must score events with the freshest rows, seconds old, in the warehouse. What should the pipeline do?

- A. Stream the events into BigQuery
- B. Export the batch to BigQuery
- C. Store the ledger in Spanner
- D. Store the objects in Cloud Storage

---

## Domain 2 — Building and Testing Applications (Development Environments, Builds, and Tests)

### 33. A team wants to test a Cloud Storage trigger path locally and keep that check running in the pipeline. Which two practices fit? Select two.

- A. Run an integration test against the emulator
- B. Run the service emulator locally
- C. Use Cloud Shell for the session
- D. Push the image to Artifact Registry
- E. Develop with Cloud Code in the IDE

### 34. A developer must reproduce a Pub/Sub acknowledgement bug on a laptop with no network access. What should they use?

- A. Use Cloud Workstations for the environment
- B. Run the service emulator locally
- C. Iterate with Skaffold
- D. Use Cloud Shell for the session

### 35. A new hire needs the SDK and a working build toolchain before their laptop is provisioned. What should they use?

- A. Run the service emulator locally
- B. Develop with Cloud Code in the IDE
- C. Use Cloud Workstations for the environment
- D. Use Cloud Shell for the session

### 36. A developer wants to set a breakpoint and step through a service that would normally run in the cloud. What should they use?

- A. Develop with Cloud Code in the IDE
- B. Use Cloud Workstations for the environment
- C. Connect the assistant to an MCP server
- D. Use Cloud Shell for the session

### 37. Contractors must work in an environment the company defines by image, with no code on their own disks. What should the company provide?

- A. Use Cloud Shell for the session
- B. Run the service emulator locally
- C. Use Cloud Workstations for the environment
- D. Iterate with Skaffold

### 38. A developer wants a rebuild and redeploy on every save while iterating on a cluster service. What should they use?

- A. Deploy a pinned image digest
- B. Deploy from source and let the platform build it
- C. Build the image with Cloud Build
- D. Iterate with Skaffold

### 39. A pipeline must run tests, build an image, and store it where staging and production have separate pull rights. Which two services are needed? Select two.

- A. Develop with Cloud Code in the IDE
- B. Push the image to Artifact Registry
- C. Build the image with Cloud Build
- D. Use Cloud Shell for the session
- E. Push the image to Container Registry

### 40. Two environments must not be able to pull each other's images, and the registry must enforce that at the repository level. Which service fits?

- A. Use Cloud Shell for the session
- B. Push the image to Artifact Registry
- C. Store the objects in Cloud Storage
- D. Push the image to Container Registry

### 41. Audit asks which artifact is serving traffic, and the deployment currently rebuilds from a branch. What should change?

- A. Trigger the build from a repository push
- B. Deploy from source and let the platform build it
- C. Deploy a pinned image digest
- D. Package the monolith into a container image

### 42. Releases are built by hand, so the artifact does not match the commit. What should be added?

- A. Keep building the image by hand
- B. Schedule the invocation with Cloud Scheduler
- C. Trigger the build from a repository push
- D. Queue the work as a Cloud Tasks task

### 43. A registry must serve pulls at low latency from the same region as the runtime. Which service fits?

- A. Build the image with Cloud Build
- B. Push the image to Container Registry
- C. Push the image to Artifact Registry
- D. Store the objects in Cloud Storage

### 44. A team is consolidating legacy registries and asks which one has project-wide rather than repository-scoped access. Which answers that?

- A. Push the image to Container Registry
- B. Build the image with Cloud Build
- C. Store the objects in Cloud Storage
- D. Push the image to Artifact Registry

### 45. Test reports must be readable for seven years after the images are deleted. Where should they go?

- A. Store the objects in Cloud Storage
- B. Build the image with Cloud Build
- C. Push the image to Artifact Registry
- D. Push the image to Container Registry

### 46. An auditor asks which source commit and builder produced the running image. What should the pipeline record?

- A. Generate build provenance in Cloud Build
- B. Enforce admission with Binary Authorization
- C. Review the finding in Security Command Center
- D. Scan the image with Artifact Analysis

### 47. Findings arrive from several services and nobody owns a single queue. What should the team adopt?

- A. Scan the image with Artifact Analysis
- B. Review the finding in Security Command Center
- C. Enforce admission with Binary Authorization
- D. Send the exception to Error Reporting

### 48. A newly published CVE must be matched to the images already in the registry. What should be used?

- A. Generate build provenance in Cloud Build
- B. Scan the image with Artifact Analysis
- C. Review the finding in Security Command Center
- D. Enforce admission with Binary Authorization

### 49. A suite is intermittently red and reviewers have started merging anyway. Which two actions restore trust? Select two.

- A. Quarantine the flaky test and fix it
- B. Block the deploy on the test result
- C. Run an integration test against the emulator
- D. Load-test the release before the rollout
- E. Add a unit test with dependencies stubbed

### 50. A parser has eleven input branches, and a failure must identify the exact branch in seconds. What should the team add?

- A. Run an integration test against the emulator
- B. Add a unit test with dependencies stubbed
- C. Quarantine the flaky test and fix it
- D. Load-test the release before the rollout

### 51. A developer must draft fifty table-driven test cases quickly and then review them. What should they use?

- A. Use an AI coding assistant to draft the tests
- B. Develop with Cloud Code in the IDE
- C. Connect the assistant to an MCP server
- D. Ask Gemini Cloud Assist for a diagnosis

### 52. A team keeps discovering schema mismatches only in production and wants them caught on every merge. Which two choices fit? Select two.

- A. Block the deploy on the test result
- B. Add a unit test with dependencies stubbed
- C. Load-test the release before the rollout
- D. Run an integration test against the emulator
- E. Run the tests as a Cloud Build step

### 53. Tests pass locally and fail after deployment, and nobody notices until users report it. What should move?

- A. Block the deploy on the test result
- B. Load-test the release before the rollout
- C. Run the tests as a Cloud Build step
- D. Quarantine the flaky test and fix it

### 54. A team can still deploy while the suite is red because the pipeline ignores the result. What should change?

- A. Add a unit test with dependencies stubbed
- B. Run the tests as a Cloud Build step
- C. Quarantine the flaky test and fix it
- D. Block the deploy on the test result

### 55. A new revision must be proven at ten times current traffic before a launch. What should the team run?

- A. Add a unit test with dependencies stubbed
- B. Run an integration test against the emulator
- C. Load-test the release before the rollout
- D. Profile the service with Cloud Profiler

---

## Domain 3 — Configuring Cloud-Native Applications for Deployment (Cloud Run and GKE Deployment Configuration)

### 56. A small Node service has no Dockerfile and must be reachable on a public URL within the hour. What should the team do?

- A. Deploy a pinned image digest
- B. Package the monolith into a container image
- C. Build the image with Cloud Build
- D. Deploy from source and let the platform build it

### 57. A back-office service must not be reachable from the internet at all, even by an authenticated user. What should the team configure?

- A. Allow unauthenticated invocations
- B. Put Identity-Aware Proxy in front of the service
- C. Restrict ingress to internal traffic
- D. Grant the invoker role to the calling identity

### 58. A batch job runs under its own identity and must call exactly one Cloud Run service. What should be granted?

- A. Grant the basic editor role
- B. Put Identity-Aware Proxy in front of the service
- C. Grant the invoker role to the calling identity
- D. Allow unauthenticated invocations

### 59. A rollback must restore the exact binary that ran before the incident, byte for byte. What should the team redeploy?

- A. Package the monolith into a container image
- B. Build the image with Cloud Build
- C. Deploy from source and let the platform build it
- D. Deploy a pinned image digest

### 60. A service must be invoked when an audit log entry records a bucket permission change, with no polling. What should the team configure?

- A. Schedule the invocation with Cloud Scheduler
- B. Queue the work as a Cloud Tasks task
- C. Route the event with Eventarc
- D. Publish the event to a Pub/Sub topic

### 61. A worker must process a backlog in priority order and acknowledge after committing its write. What should it use?

- A. Queue the work as a Cloud Tasks task
- B. Deliver to an HTTPS push subscription
- C. Route the event with Eventarc
- D. Have the worker pull from the subscription

### 62. A nightly fan-out must start on a timetable and then call a slow partner once per order with retries. Which two services fit? Select two.

- A. Queue the work as a Cloud Tasks task
- B. Schedule the invocation with Cloud Scheduler
- C. Orchestrate the steps in Workflows
- D. Publish the event to a Pub/Sub topic
- E. Route the event with Eventarc

### 63. A five-step process must branch when one dependency reports a quota error and retry that step later. What should the team use?

- A. Schedule the invocation with Cloud Scheduler
- B. Orchestrate the steps in Workflows
- C. Publish the event to a Pub/Sub topic
- D. Queue the work as a Cloud Tasks task

### 64. A service handling large uploads exhausts memory per instance and its bill spiked last month. Which two settings fit? Select two.

- A. Raise the per-instance concurrency limit
- B. Use instance-based billing
- C. Cap the maximum instance count
- D. Keep a minimum number of instances warm
- E. Enable CPU boost at startup

### 65. The payment path must never pay a cold-start penalty, and the cost of warm capacity is accepted. What should be configured?

- A. Cap the maximum instance count
- B. Enable CPU boost at startup
- C. Keep a minimum number of instances warm
- D. Raise the per-instance concurrency limit

### 66. A revision serves errors for its first twenty seconds because it accepts traffic before loading its cache. What should be added?

- A. Configure a liveness probe
- B. Scale pods on a custom or external metric
- C. Configure a startup probe
- D. Configure a readiness probe

### 67. A service initializes in nine seconds and only the first minute of each instance's life is slow. What should the team enable?

- A. Raise the per-instance concurrency limit
- B. Cap the maximum instance count
- C. Enable CPU boost at startup
- D. Keep a minimum number of instances warm

### 68. A breaking field change cannot wait for the oldest mobile clients to update. What should the team do?

- A. Publish an OpenAPI specification
- B. Apply a rate limit per client key
- C. Add the field in a backward-compatible way
- D. Introduce a new API version alongside the old one

### 69. A partner API must keep one stable contract while the backend is rewritten every quarter. What should front it?

- A. Put Apigee in front of the API
- B. Use API Gateway for the API
- C. Apply a rate limit per client key
- D. Introduce a new API version alongside the old one

### 70. A deployment replaces all pods at once and the service is unavailable for the length of a boot. What should change?

- A. Add a PodDisruptionBudget
- B. Constrain pods to the intended node pool
- C. Set a namespace resource quota
- D. Use a rolling update strategy

### 71. Pods land on the wrong pool and one namespace can consume the whole cluster. Which two settings apply? Select two.

- A. Constrain pods to the intended node pool
- B. Add a PodDisruptionBudget
- C. Run the batch node pool on Spot VMs
- D. Set a namespace resource quota
- E. Set a minimum replica count

### 72. A node upgrade drained every replica of a stateful service at the same moment. What should be added?

- A. Add a PodDisruptionBudget
- B. Use a rolling update strategy
- C. Set a minimum replica count
- D. Set a namespace resource quota

### 73. A stateless transcoding pool can tolerate a node disappearing mid-task. What should its pool use?

- A. Buy committed use discounts for the steady baseline
- B. Set CPU and memory requests from measured use
- C. Enable node pool autoscaling
- D. Run the batch node pool on Spot VMs

### 74. A pod whose database pool is exhausted keeps receiving traffic and returning errors. What should the team configure?

- A. Configure a readiness probe
- B. Add a PodDisruptionBudget
- C. Configure a startup probe
- D. Configure a liveness probe

### 75. A pod spins in a deadlock but still passes its readiness check, so it is never replaced. What should be added?

- A. Configure a liveness probe
- B. Set a namespace resource quota
- C. Configure a startup probe
- D. Configure a readiness probe

### 76. A container whose worker threads are all blocked still answers its readiness check and never restarts. What should be added?

- A. Configure a readiness probe
- B. Configure a liveness probe
- C. Configure a startup probe
- D. Add a PodDisruptionBudget

### 77. Workers sit idle at low CPU while a backlog grows to six hours. What should the scaling metric be?

- A. Enable node pool autoscaling
- B. Scale pods on a custom or external metric
- C. Set a minimum replica count
- D. Scale pods on CPU utilization

### 78. An autoscaled service must never drop below three replicas and must keep quorum during a node drain. Which two settings fit? Select two.

- A. Add a PodDisruptionBudget
- B. Set a minimum replica count
- C. Scale pods on a custom or external metric
- D. Scale pods on CPU utilization
- E. Set a namespace resource quota

### 79. Pods stay pending for twenty minutes during a morning surge because no node has room. What should be enabled?

- A. Set a namespace resource quota
- B. Enable node pool autoscaling
- C. Run the batch node pool on Spot VMs
- D. Scale pods on CPU utilization

---

## Domain 4 — Integrating Applications with Google Cloud Services (Data, Messaging, APIs, and Observability)

### 80. A service must reach a Cloud SQL instance from another network with IAM authorization and no public address. What should it use?

- A. Use the language connector with IAM
- B. Connect over the database private IP
- C. Connect through the Cloud SQL Auth Proxy
- D. Expose the database on a public address with enforced SSL

### 81. A Cloud Run service exhausts database connections at peak and wants no proxy sidecar. Which two choices fit? Select two.

- A. Pool and reuse database connections
- B. Download a service account key file
- C. Connect through the Cloud SQL Auth Proxy
- D. Connect over the database private IP
- E. Use the language connector with IAM

### 82. The database and the service already share a VPC, and the team wants the shortest network path between them. What should it use?

- A. Connect through the Cloud SQL Auth Proxy
- B. Connect over the database private IP
- C. Expose the database on a public address with enforced SSL
- D. Use the language connector with IAM

### 83. A consumer app needs document queries, offline sync and real-time listeners for a few million users. Which store fits?

- A. Design the row key for the read pattern
- B. Store the ledger in Spanner
- C. Use Firestore in Native mode
- D. Store the objects in Cloud Storage

### 84. An IoT fleet writes device readings at very high rate and reads the last hour per device. What decides the design?

- A. Design the row key for the read pattern
- B. Store the ledger in Spanner
- C. Cache reads in Memorystore
- D. Use Firestore in Native mode

### 85. A shipping handler occasionally processes the same release twice after a redelivery. What should the handler add?

- A. Make the handler idempotent with a deduplication key
- B. Publish the event to a Pub/Sub topic
- C. Add a dead-letter topic
- D. Queue the work as a Cloud Tasks task

### 86. Events must land as warehouse rows with no consumer process to operate. What should be configured?

- A. Queue the work as a Cloud Tasks task
- B. Publish the event to a Pub/Sub topic
- C. Route the event with Eventarc
- D. Use a BigQuery subscription on the topic

### 87. One malformed message is retried forever and blocks the subscription. What should be configured?

- A. Add a dead-letter topic
- B. Have the worker pull from the subscription
- C. Deliver to an HTTPS push subscription
- D. Make the handler idempotent with a deduplication key

### 88. A known endpoint must handle each record with its own retry schedule and a rate limit. What should be used?

- A. Queue the work as a Cloud Tasks task
- B. Publish the event to a Pub/Sub topic
- C. Orchestrate the steps in Workflows
- D. Schedule the invocation with Cloud Scheduler

### 89. A dashboard calls the same reference API on every page load and is throttled at peak. Which two practices fit? Select two.

- A. Follow the page token until results are exhausted
- B. Cache the response for its freshness window
- C. Retry with exponential backoff and jitter
- D. Request only the fields the caller needs
- E. Batch many small calls into one request

### 90. An export stops at one thousand records although the collection holds fifty thousand. What should the client do?

- A. Request only the fields the caller needs
- B. Batch many small calls into one request
- C. Cache the response for its freshness window
- D. Follow the page token until results are exhausted

### 91. Response payloads carry hundreds of unused fields and dominate the request time. What should change?

- A. Follow the page token until results are exhausted
- B. Request only the fields the caller needs
- C. Batch many small calls into one request
- D. Cache the response for its freshness window

### 92. A service calling an API must not depend on a key file on disk. What should it use?

- A. Allow unauthenticated invocations
- B. Give the workload its own service account
- C. Download a service account key file
- D. Rely on Application Default Credentials

### 93. A reviewer finds the caller can delete buckets although it only lists objects. What should change?

- A. Grant only the roles the workload needs
- B. Download a service account key file
- C. Apply a Kubernetes NetworkPolicy
- D. Grant the basic editor role

### 94. Pods must obtain API credentials that expire quickly and are never written to disk. What should the team use?

- A. Rely on Application Default Credentials
- B. Set the credential as an environment variable
- C. Bind a Kubernetes service account to a Google service account
- D. Download a service account key file

### 95. Support cannot find a customer's requests because the identifier is inside a message string. What should change?

- A. Build a log-based metric
- B. Set the correct severity on each entry
- C. Emit structured JSON logs
- D. Send the exception to Error Reporting

### 96. A request takes four seconds and the total does not reveal which downstream call is responsible. What should the team add?

- A. Emit a custom metric from the code
- B. Send the exception to Error Reporting
- C. Propagate the trace ID between services
- D. Instrument a span around the downstream call

### 97. Routine output and real errors share one severity, so alerts fire on startup chatter. What should change?

- A. Set the correct severity on each entry
- B. Build a log-based metric
- C. Emit structured JSON logs
- D. Send the exception to Error Reporting

### 98. Thousands of variants of one stack trace must be counted as a single failure. What should be used?

- A. Emit a custom metric from the code
- B. Emit structured JSON logs
- C. Send the exception to Error Reporting
- D. Build a log-based metric

### 99. Log entries from four services for one request cannot be joined. What should be added?

- A. Emit a custom metric from the code
- B. Propagate the trace ID between services
- C. Profile the service with Cloud Profiler
- D. Instrument a span around the downstream call

### 100. An engineer must explain a latency regression from existing telemetry during an incident. Which tool fits?

- A. Ask Gemini Cloud Assist for a diagnosis
- B. Profile the service with Cloud Profiler
- C. Connect the assistant to an MCP server
- D. Use an AI coding assistant to draft the tests

---

## Answer key and explanations

### Question 1 — B

Answer: Deploy the service to Cloud Run. A managed container runtime scales to zero and needs no cluster operations, which matches both the skill and the traffic shape. A managed container runtime that scales to zero and bills per request while it serves traffic. Local study-map skill 1.1 (Compute Platform Selection), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 1 (designing highly scalable, secure, and reliable cloud-native applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A managed Kubernetes control plane where pods, node pools and cluster-scoped policy are yours to configure. Why the correct answer wins: A managed container runtime scales to zero and needs no cluster operations, which matches both the skill and the traffic shape.
- **B:** Correct. A managed container runtime that scales to zero and bills per request while it serves traffic. In this case: A managed container runtime scales to zero and needs no cluster operations, which matches both the skill and the traffic shape.
- **C:** Incorrect for this question. Virtual machines where the operating system, runtime and scaling group are all managed by the team. Why the correct answer wins: A managed container runtime scales to zero and needs no cluster operations, which matches both the skill and the traffic shape.
- **D:** Incorrect for this question. An event-triggered function runtime for a single-purpose handler rather than a long-lived service. Why the correct answer wins: A managed container runtime scales to zero and needs no cluster operations, which matches both the skill and the traffic shape.

### Question 2 — D

Answer: Deploy the workload to Google Kubernetes Engine. Only a managed Kubernetes control plane exposes that workload shape. A managed Kubernetes control plane where pods, node pools and cluster-scoped policy are yours to configure. Local study-map skill 1.1 (Compute Platform Selection), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 1 (designing highly scalable, secure, and reliable cloud-native applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A platform runtime that manages scaling for a supported language version and its sandbox limits. Why the correct answer wins: Only a managed Kubernetes control plane exposes that workload shape.
- **B:** Incorrect for this question. A managed container runtime that scales to zero and bills per request while it serves traffic. Why the correct answer wins: Only a managed Kubernetes control plane exposes that workload shape.
- **C:** Incorrect for this question. An event-triggered function runtime for a single-purpose handler rather than a long-lived service. Why the correct answer wins: Only a managed Kubernetes control plane exposes that workload shape.
- **D:** Correct. A managed Kubernetes control plane where pods, node pools and cluster-scoped policy are yours to configure. In this case: Only a managed Kubernetes control plane exposes that workload shape.

### Question 3 — D

Answer: Deploy the handler as a Cloud Functions function. An event-triggered function runtime suits a single-purpose handler invoked by an event. An event-triggered function runtime for a single-purpose handler rather than a long-lived service. Local study-map skill 1.1 (Compute Platform Selection), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 1 (designing highly scalable, secure, and reliable cloud-native applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Virtual machines where the operating system, runtime and scaling group are all managed by the team. Why the correct answer wins: An event-triggered function runtime suits a single-purpose handler invoked by an event.
- **B:** Incorrect for this question. A managed Kubernetes control plane where pods, node pools and cluster-scoped policy are yours to configure. Why the correct answer wins: An event-triggered function runtime suits a single-purpose handler invoked by an event.
- **C:** Incorrect for this question. A managed container runtime that scales to zero and bills per request while it serves traffic. Why the correct answer wins: An event-triggered function runtime suits a single-purpose handler invoked by an event.
- **D:** Correct. An event-triggered function runtime for a single-purpose handler rather than a long-lived service. In this case: An event-triggered function runtime suits a single-purpose handler invoked by an event.

### Question 4 — C

Answer: Package the monolith into a container image. A container image carries the dependencies with it, so every environment runs the same artifact. Wrap the existing process in a portable artifact that a managed runtime can execute. Local study-map skill 1.2 (Containerizing and Refactoring Applications), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 1 (designing highly scalable, secure, and reliable cloud-native applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A platform runtime that manages scaling for a supported language version and its sandbox limits. Why the correct answer wins: A container image carries the dependencies with it, so every environment runs the same artifact.
- **B:** Incorrect for this question. Hand the source to the managed builder instead of shipping an image. Why the correct answer wins: A container image carries the dependencies with it, so every environment runs the same artifact.
- **C:** Correct. Wrap the existing process in a portable artifact that a managed runtime can execute. In this case: A container image carries the dependencies with it, so every environment runs the same artifact.
- **D:** Incorrect for this question. An event-triggered function runtime for a single-purpose handler rather than a long-lived service. Why the correct answer wins: A container image carries the dependencies with it, so every environment runs the same artifact.

### Question 5 — B, D

Answers: Deploy in one region across multiple zones; Add a health check endpoint to the backend service. Spreading over zones covers the zone failure, and a health check removes the unhealthy instance from rotation. Spread instances over zones of a single region so a zone failure does not stop the service. Let the load balancer stop sending traffic to an unhealthy instance. Local study-map skill 1.3 (Regional Distribution and Failover), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 1 (designing highly scalable, secure, and reliable cloud-native applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Run in one zone only, so a zone failure stops the service entirely. Why the correct answer wins: Spreading over zones covers the zone failure, and a health check removes the unhealthy instance from rotation.
- **B:** Correct. Spread instances over zones of a single region so a zone failure does not stop the service. In this case: Spreading over zones covers the zone failure, and a health check removes the unhealthy instance from rotation.
- **C:** Incorrect for this question. Serve from two regions so a regional failure leaves capacity elsewhere. Why the correct answer wins: Spreading over zones covers the zone failure, and a health check removes the unhealthy instance from rotation.
- **D:** Correct. Let the load balancer stop sending traffic to an unhealthy instance. In this case: Spreading over zones covers the zone failure, and a health check removes the unhealthy instance from rotation.
- **E:** Incorrect for this question. Trade a term commitment for a lower unit price on capacity that never idles. Why the correct answer wins: Spreading over zones covers the zone failure, and a health check removes the unhealthy instance from rotation.

### Question 6 — B

Answer: Put a global external Application Load Balancer in front. A global anycast front door routes each user to a nearby healthy backend. A single anycast address that routes to the nearest healthy backend. Local study-map skill 1.3 (Regional Distribution and Failover), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 1 (designing highly scalable, secure, and reliable cloud-native applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Trade a term commitment for a lower unit price on capacity that never idles. Why the correct answer wins: A global anycast front door routes each user to a nearby healthy backend.
- **B:** Correct. A single anycast address that routes to the nearest healthy backend. In this case: A global anycast front door routes each user to a nearby healthy backend.
- **C:** Incorrect for this question. Cache responses at the edge so repeated requests never reach the origin. Why the correct answer wins: A global anycast front door routes each user to a nearby healthy backend.
- **D:** Incorrect for this question. A load balancer scoped to one region with a regional address. Why the correct answer wins: A global anycast front door routes each user to a nearby healthy backend.

### Question 7 — D

Answer: Store session state in a shared datastore. Moving session state out of the instance means any instance can serve the next request. Move the state out of the instance so any instance can serve any request. Local study-map skill 1.4 (Load Balancing and Session Affinity), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 1 (designing highly scalable, secure, and reliable cloud-native applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Route the client by cookie rather than by address or header. Why the correct answer wins: Moving session state out of the instance means any instance can serve the next request.
- **B:** Incorrect for this question. Pin a client to one backend for the life of its session. Why the correct answer wins: Moving session state out of the instance means any instance can serve the next request.
- **C:** Incorrect for this question. A managed Redis-compatible cache in front of the system of record. Why the correct answer wins: Moving session state out of the instance means any instance can serve the next request.
- **D:** Correct. Move the state out of the instance so any instance can serve any request. In this case: Moving session state out of the instance means any instance can serve the next request.

### Question 8 — D

Answer: Add a health check endpoint to the backend service. A health check stops traffic from reaching an instance that cannot answer. Let the load balancer stop sending traffic to an unhealthy instance. Local study-map skill 1.4 (Load Balancing and Session Affinity), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 1 (designing highly scalable, secure, and reliable cloud-native applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Cache responses at the edge so repeated requests never reach the origin. Why the correct answer wins: A health check stops traffic from reaching an instance that cannot answer.
- **B:** Incorrect for this question. A load balancer scoped to one region with a regional address. Why the correct answer wins: A health check stops traffic from reaching an instance that cannot answer.
- **C:** Incorrect for this question. Pin a client to one backend for the life of its session. Why the correct answer wins: A health check stops traffic from reaching an instance that cannot answer.
- **D:** Correct. Let the load balancer stop sending traffic to an unhealthy instance. In this case: A health check stops traffic from reaching an instance that cannot answer.

### Question 9 — B

Answer: Cache reads in Memorystore. A shared managed cache keeps a single value that every instance reads, where a per-process cache diverges. A managed Redis-compatible cache in front of the system of record. Local study-map skill 1.5 (Caching with Memorystore), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 1 (designing highly scalable, secure, and reliable cloud-native applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Cache responses at the edge so repeated requests never reach the origin. Why the correct answer wins: A shared managed cache keeps a single value that every instance reads, where a per-process cache diverges.
- **B:** Correct. A managed Redis-compatible cache in front of the system of record. In this case: A shared managed cache keeps a single value that every instance reads, where a per-process cache diverges.
- **C:** Incorrect for this question. Read the cache, fall back to the database, and populate the cache on a miss. Why the correct answer wins: A shared managed cache keeps a single value that every instance reads, where a per-process cache diverges.
- **D:** Incorrect for this question. A per-instance cache that is fast but not shared between instances. Why the correct answer wins: A shared managed cache keeps a single value that every instance reads, where a per-process cache diverges.

### Question 10 — A

Answer: Load through a cache-aside pattern. A shared cache-aside layer keeps the values outside the instance, so a restart does not empty them. Read the cache, fall back to the database, and populate the cache on a miss. Local study-map skill 1.5 (Caching with Memorystore), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 1 (designing highly scalable, secure, and reliable cloud-native applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Correct. Read the cache, fall back to the database, and populate the cache on a miss. In this case: A shared cache-aside layer keeps the values outside the instance, so a restart does not empty them.
- **B:** Incorrect for this question. A managed Redis-compatible cache in front of the system of record. Why the correct answer wins: A shared cache-aside layer keeps the values outside the instance, so a restart does not empty them.
- **C:** Incorrect for this question. A per-instance cache that is fast but not shared between instances. Why the correct answer wins: A shared cache-aside layer keeps the values outside the instance, so a restart does not empty them.
- **D:** Incorrect for this question. Cache responses at the edge so repeated requests never reach the origin. Why the correct answer wins: A shared cache-aside layer keeps the values outside the instance, so a restart does not empty them.

### Question 11 — D

Answer: Expose a REST API with JSON payloads. A resource-oriented HTTP interface is callable by simple clients without generated stubs. A resource-oriented HTTP interface that browsers and simple clients can call. Local study-map skill 1.6 (API Protocol Choice: REST and gRPC), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 1 (designing highly scalable, secure, and reliable cloud-native applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A compatibility layer so browser code can call a gRPC service. Why the correct answer wins: A resource-oriented HTTP interface is callable by simple clients without generated stubs.
- **B:** Incorrect for this question. A machine-readable contract that generates clients and validates requests. Why the correct answer wins: A resource-oriented HTTP interface is callable by simple clients without generated stubs.
- **C:** Incorrect for this question. A binary, schema-driven RPC interface with streaming and generated clients. Why the correct answer wins: A resource-oriented HTTP interface is callable by simple clients without generated stubs.
- **D:** Correct. A resource-oriented HTTP interface that browsers and simple clients can call. In this case: A resource-oriented HTTP interface is callable by simple clients without generated stubs.

### Question 12 — B

Answer: Serve gRPC-Web for browser clients. A web-compatible gRPC layer lets browser code reach the existing service. A compatibility layer so browser code can call a gRPC service. Local study-map skill 1.6 (API Protocol Choice: REST and gRPC), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 1 (designing highly scalable, secure, and reliable cloud-native applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A resource-oriented HTTP interface that browsers and simple clients can call. Why the correct answer wins: A web-compatible gRPC layer lets browser code reach the existing service.
- **B:** Correct. A compatibility layer so browser code can call a gRPC service. In this case: A web-compatible gRPC layer lets browser code reach the existing service.
- **C:** Incorrect for this question. A machine-readable contract that generates clients and validates requests. Why the correct answer wins: A web-compatible gRPC layer lets browser code reach the existing service.
- **D:** Incorrect for this question. A binary, schema-driven RPC interface with streaming and generated clients. Why the correct answer wins: A web-compatible gRPC layer lets browser code reach the existing service.

### Question 13 — A, C

Answers: Put Apigee in front of the API; Introduce a new API version alongside the old one. Versioning alongside the old contract keeps existing clients working, and per-key quotas enforce each plan. An API management layer for quotas, keys, mediation and analytics. Keep the old contract working while the new one is adopted. Local study-map skill 1.7 (API Management, Rate Limiting, and Versioning), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 1 (designing highly scalable, secure, and reliable cloud-native applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Correct. Keep the old contract working while the new one is adopted. In this case: Versioning alongside the old contract keeps existing clients working, and per-key quotas enforce each plan.
- **B:** Incorrect for this question. A legacy broad role that can change most resources in the project. Why the correct answer wins: Versioning alongside the old contract keeps existing clients working, and per-key quotas enforce each plan.
- **C:** Correct. An API management layer for quotas, keys, mediation and analytics. In this case: Versioning alongside the old contract keeps existing clients working, and per-key quotas enforce each plan.
- **D:** Incorrect for this question. Reject or queue requests above a threshold so one client cannot exhaust the service. Why the correct answer wins: Versioning alongside the old contract keeps existing clients working, and per-key quotas enforce each plan.
- **E:** Incorrect for this question. A lighter managed gateway for routing and key-based quota enforcement. Why the correct answer wins: Versioning alongside the old contract keeps existing clients working, and per-key quotas enforce each plan.

### Question 14 — B

Answer: Use API Gateway for the API. A light managed gateway provides routing and key quotas without a full mediation platform. A lighter managed gateway for routing and key-based quota enforcement. Local study-map skill 1.7 (API Management, Rate Limiting, and Versioning), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 1 (designing highly scalable, secure, and reliable cloud-native applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Reject or queue requests above a threshold so one client cannot exhaust the service. Why the correct answer wins: A light managed gateway provides routing and key quotas without a full mediation platform.
- **B:** Correct. A lighter managed gateway for routing and key-based quota enforcement. In this case: A light managed gateway provides routing and key quotas without a full mediation platform.
- **C:** Incorrect for this question. An API management layer for quotas, keys, mediation and analytics. Why the correct answer wins: A light managed gateway provides routing and key quotas without a full mediation platform.
- **D:** Incorrect for this question. Authenticate and authorize users before a request reaches the application. Why the correct answer wins: A light managed gateway provides routing and key quotas without a full mediation platform.

### Question 15 — A

Answer: Publish the event to a Pub/Sub topic. A durable topic decouples the publisher from every downstream consumer. A durable, at-least-once message channel with independent subscribers. Local study-map skill 1.8 (Asynchronous and Event-Driven Integration), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 1 (designing highly scalable, secure, and reliable cloud-native applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Correct. A durable, at-least-once message channel with independent subscribers. In this case: A durable topic decouples the publisher from every downstream consumer.
- **B:** Incorrect for this question. A stateful sequence of service calls with retries and error branches. Why the correct answer wins: A durable topic decouples the publisher from every downstream consumer.
- **C:** Incorrect for this question. A task queue with retries and rate control aimed at a specific target. Why the correct answer wins: A durable topic decouples the publisher from every downstream consumer.
- **D:** Incorrect for this question. A cron-style trigger that calls a target on a fixed timetable. Why the correct answer wins: A durable topic decouples the publisher from every downstream consumer.

### Question 16 — C, E

Answers: Add a dead-letter topic; Make the handler idempotent with a deduplication key. A dead-letter topic removes the poison message from the flow, and a deduplication key makes a repeat delivery harmless. Hold messages that exhausted their delivery attempts for later inspection. Recognise a repeated delivery and skip the duplicate work. Local study-map skill 1.8 (Asynchronous and Event-Driven Integration), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 1 (designing highly scalable, secure, and reliable cloud-native applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. The consumer controls the pace and acknowledges messages itself. Why the correct answer wins: A dead-letter topic removes the poison message from the flow, and a deduplication key makes a repeat delivery harmless.
- **B:** Incorrect for this question. A trigger path that turns a Cloud Audit Log or resource event into a delivery. Why the correct answer wins: A dead-letter topic removes the poison message from the flow, and a deduplication key makes a repeat delivery harmless.
- **C:** Correct. Recognise a repeated delivery and skip the duplicate work. In this case: A dead-letter topic removes the poison message from the flow, and a deduplication key makes a repeat delivery harmless.
- **D:** Incorrect for this question. A task queue with retries and rate control aimed at a specific target. Why the correct answer wins: A dead-letter topic removes the poison message from the flow, and a deduplication key makes a repeat delivery harmless.
- **E:** Correct. Hold messages that exhausted their delivery attempts for later inspection. In this case: A dead-letter topic removes the poison message from the flow, and a deduplication key makes a repeat delivery harmless.

### Question 17 — B

Answer: Use request-based billing. Request-based billing charges while requests are handled rather than for the idle hours. Charge only while a request is being handled, which suits bursty traffic. Local study-map skill 1.9 (Resource Requirements and Cost Optimization), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 1 (designing highly scalable, secure, and reliable cloud-native applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Charge for the whole instance lifetime, which suits steady background work. Why the correct answer wins: Request-based billing charges while requests are handled rather than for the idle hours.
- **B:** Correct. Charge only while a request is being handled, which suits bursty traffic. In this case: Request-based billing charges while requests are handled rather than for the idle hours.
- **C:** Incorrect for this question. Trade a term commitment for a lower unit price on capacity that never idles. Why the correct answer wins: Request-based billing charges while requests are handled rather than for the idle hours.
- **D:** Incorrect for this question. Pay for idle capacity so a cold start never appears in the latency percentiles. Why the correct answer wins: Request-based billing charges while requests are handled rather than for the idle hours.

### Question 18 — D

Answer: Run the batch node pool on Spot VMs. Reclaimable capacity suits work that can be retried after a node is taken away. Use reclaimable capacity for work that can tolerate a node disappearing. Local study-map skill 1.9 (Resource Requirements and Cost Optimization), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 1 (designing highly scalable, secure, and reliable cloud-native applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Add or remove nodes as pending pods demand capacity. Why the correct answer wins: Reclaimable capacity suits work that can be retried after a node is taken away.
- **B:** Incorrect for this question. Trade a term commitment for a lower unit price on capacity that never idles. Why the correct answer wins: Reclaimable capacity suits work that can be retried after a node is taken away.
- **C:** Incorrect for this question. Give the scheduler real numbers so placement and scaling decisions are not guesses. Why the correct answer wins: Reclaimable capacity suits work that can be retried after a node is taken away.
- **D:** Correct. Use reclaimable capacity for work that can tolerate a node disappearing. In this case: Reclaimable capacity suits work that can be retried after a node is taken away.

### Question 19 — C

Answer: Canary the release at a small percentage first. A small canary slice measures real behaviour before the change reaches everyone. Expose the new version to a slice of traffic before widening it. Local study-map skill 1.10 (Traffic Splitting and Gradual Rollout), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 1 (designing highly scalable, secure, and reliable cloud-native applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Return all traffic to the known-good revision when the new one misbehaves. Why the correct answer wins: A small canary slice measures real behaviour before the change reaches everyone.
- **B:** Incorrect for this question. Send a fraction of requests to the new revision while the old one still serves the rest. Why the correct answer wins: A small canary slice measures real behaviour before the change reaches everyone.
- **C:** Correct. Expose the new version to a slice of traffic before widening it. In this case: A small canary slice measures real behaviour before the change reaches everyone.
- **D:** Incorrect for this question. Ship the code dark and enable it per cohort without a redeploy. Why the correct answer wins: A small canary slice measures real behaviour before the change reaches everyone.

### Question 20 — B, D

Answers: Split traffic between revisions by percentage; Gate the change behind a feature flag. A percentage split moves a measured share of traffic onto the revision, and a flag enables the change for the cohort before the split widens. Send a fraction of requests to the new revision while the old one still serves the rest. Ship the code dark and enable it per cohort without a redeploy. Local study-map skill 1.10 (Traffic Splitting and Gradual Rollout), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 1 (designing highly scalable, secure, and reliable cloud-native applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Expose the new version to a slice of traffic before widening it. Why the correct answer wins: A percentage split moves a measured share of traffic onto the revision, and a flag enables the change for the cohort before the split widens.
- **B:** Correct. Ship the code dark and enable it per cohort without a redeploy. In this case: A percentage split moves a measured share of traffic onto the revision, and a flag enables the change for the cohort before the split widens.
- **C:** Incorrect for this question. Send only tagged requests to the new revision for internal testing. Why the correct answer wins: A percentage split moves a measured share of traffic onto the revision, and a flag enables the change for the cohort before the split widens.
- **D:** Correct. Send a fraction of requests to the new revision while the old one still serves the rest. In this case: A percentage split moves a measured share of traffic onto the revision, and a flag enables the change for the cohort before the split widens.
- **E:** Incorrect for this question. Return all traffic to the known-good revision when the new one misbehaves. Why the correct answer wins: A percentage split moves a measured share of traffic onto the revision, and a flag enables the change for the cohort before the split widens.

### Question 21 — A

Answer: Queue the work as a Cloud Tasks task. A task queue takes the work out of the request path and retries it separately. A task queue with retries and rate control aimed at a specific target. Local study-map skill 1.11 (Orchestrating Services), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 1 (designing highly scalable, secure, and reliable cloud-native applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Correct. A task queue with retries and rate control aimed at a specific target. In this case: A task queue takes the work out of the request path and retries it separately.
- **B:** Incorrect for this question. A stateful sequence of service calls with retries and error branches. Why the correct answer wins: A task queue takes the work out of the request path and retries it separately.
- **C:** Incorrect for this question. A durable, at-least-once message channel with independent subscribers. Why the correct answer wins: A task queue takes the work out of the request path and retries it separately.
- **D:** Incorrect for this question. A cron-style trigger that calls a target on a fixed timetable. Why the correct answer wins: A task queue takes the work out of the request path and retries it separately.

### Question 22 — B

Answer: Lock the bucket retention policy. A locked retention policy makes shortening the period impossible, which a lifecycle rule cannot guarantee. Make the retention period impossible to shorten, even by an owner. Local study-map skill 1.12 (Data Retention and Organization Policy), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 1 (designing highly scalable, secure, and reliable cloud-native applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Serve every object to anyone, which removes the need to authorize at all. Why the correct answer wins: A locked retention policy makes shortening the period impossible, which a lifecycle rule cannot guarantee.
- **B:** Correct. Make the retention period impossible to shorten, even by an owner. In this case: A locked retention policy makes shortening the period impossible, which a lifecycle rule cannot guarantee.
- **C:** Incorrect for this question. A time-limited grant to one object without exposing credentials. Why the correct answer wins: A locked retention policy makes shortening the period impossible, which a lifecycle rule cannot guarantee.
- **D:** Incorrect for this question. Transition or delete objects by age so retention happens without a job. Why the correct answer wins: A locked retention policy makes shortening the period impossible, which a lifecycle rule cannot guarantee.

### Question 23 — A, C

Answers: Store the credential in Secret Manager; Mount the secret as a volume. A managed secret store keeps the value outside the artifact, and mounting it as a file keeps it out of the environment. A managed secret store with versioning and access audit. Present the value as a file that the process reads at runtime. Local study-map skill 1.13 (Secrets, Keys, and Credential Rotation), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 1 (designing highly scalable, secure, and reliable cloud-native applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Correct. A managed secret store with versioning and access audit. In this case: A managed secret store keeps the value outside the artifact, and mounting it as a file keeps it out of the environment.
- **B:** Incorrect for this question. A legacy broad role that can change most resources in the project. Why the correct answer wins: A managed secret store keeps the value outside the artifact, and mounting it as a file keeps it out of the environment.
- **C:** Correct. Present the value as a file that the process reads at runtime. In this case: A managed secret store keeps the value outside the artifact, and mounting it as a file keeps it out of the environment.
- **D:** Incorrect for this question. A long-lived credential that has to be stored and rotated by hand. Why the correct answer wins: A managed secret store keeps the value outside the artifact, and mounting it as a file keeps it out of the environment.
- **E:** Incorrect for this question. Inject the value into the process environment at start-up. Why the correct answer wins: A managed secret store keeps the value outside the artifact, and mounting it as a file keeps it out of the environment.

### Question 24 — A

Answer: Rotate the secret on a schedule. Rotating the secret issues a new version and retires the exposed one. Issue a new version and retire the old one so exposure has a bounded life. Local study-map skill 1.13 (Secrets, Keys, and Credential Rotation), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 1 (designing highly scalable, secure, and reliable cloud-native applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Correct. Issue a new version and retire the old one so exposure has a bounded life. In this case: Rotating the secret issues a new version and retires the exposed one.
- **B:** Incorrect for this question. A managed secret store with versioning and access audit. Why the correct answer wins: Rotating the secret issues a new version and retires the exposed one.
- **C:** Incorrect for this question. A long-lived credential that has to be stored and rotated by hand. Why the correct answer wins: Rotating the secret issues a new version and retires the exposed one.
- **D:** Incorrect for this question. A key the customer owns, rotates and can disable. Why the correct answer wins: Rotating the secret issues a new version and retires the exposed one.

### Question 25 — D

Answer: Give the workload its own service account. Giving each workload its own service account keeps their permissions independent. A dedicated identity whose roles can be granted and revoked independently. Local study-map skill 1.14 (Application Authentication), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 1 (designing highly scalable, secure, and reliable cloud-native applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A long-lived credential that has to be stored and rotated by hand. Why the correct answer wins: Giving each workload its own service account keeps their permissions independent.
- **B:** Incorrect for this question. Let the client library find credentials from the environment. Why the correct answer wins: Giving each workload its own service account keeps their permissions independent.
- **C:** Incorrect for this question. The automatically created identity that usually carries broad project access. Why the correct answer wins: Giving each workload its own service account keeps their permissions independent.
- **D:** Correct. A dedicated identity whose roles can be granted and revoked independently. In this case: Giving each workload its own service account keeps their permissions independent.

### Question 26 — D

Answer: Federate the external identity with Workload Identity Federation. Federation exchanges the external token for a short-lived Google credential, so nothing is stored. Exchange an outside token for a short-lived Google credential. Local study-map skill 1.14 (Application Authentication), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 1 (designing highly scalable, secure, and reliable cloud-native applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A long-lived credential that has to be stored and rotated by hand. Why the correct answer wins: Federation exchanges the external token for a short-lived Google credential, so nothing is stored.
- **B:** Incorrect for this question. Let the client library find credentials from the environment. Why the correct answer wins: Federation exchanges the external token for a short-lived Google credential, so nothing is stored.
- **C:** Incorrect for this question. Keyless credential issuance for pods through Workload Identity. Why the correct answer wins: Federation exchanges the external token for a short-lived Google credential, so nothing is stored.
- **D:** Correct. Exchange an outside token for a short-lived Google credential. In this case: Federation exchanges the external token for a short-lived Google credential, so nothing is stored.

### Question 27 — C

Answer: Apply a Kubernetes NetworkPolicy. A network policy restricts which pods may talk to which, containing lateral movement. Restrict which pods may talk to which pods inside the cluster. Local study-map skill 1.15 (Least Privilege and Service-to-Service Security), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 1 (designing highly scalable, secure, and reliable cloud-native applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Mutual TLS, retries and traffic policy applied without changing application code. Why the correct answer wins: A network policy restricts which pods may talk to which, containing lateral movement.
- **B:** Incorrect for this question. Bound the total capacity a namespace may consume. Why the correct answer wins: A network policy restricts which pods may talk to which, containing lateral movement.
- **C:** Correct. Restrict which pods may talk to which pods inside the cluster. In this case: A network policy restricts which pods may talk to which, containing lateral movement.
- **D:** Incorrect for this question. Authenticate and authorize users before a request reaches the application. Why the correct answer wins: A network policy restricts which pods may talk to which, containing lateral movement.

### Question 28 — C, E

Answers: Grant only the roles the workload needs; Use Cloud Service Mesh for service-to-service traffic. A service mesh provides authenticated service-to-service traffic, and least privilege scopes each identity to its own calls. Scope permissions to the actions in use rather than the whole service. Mutual TLS, retries and traffic policy applied without changing application code. Local study-map skill 1.15 (Least Privilege and Service-to-Service Security), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 1 (designing highly scalable, secure, and reliable cloud-native applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Let anyone reach the endpoint, which is only appropriate for public content. Why the correct answer wins: A service mesh provides authenticated service-to-service traffic, and least privilege scopes each identity to its own calls.
- **B:** Incorrect for this question. Restrict which pods may talk to which pods inside the cluster. Why the correct answer wins: A service mesh provides authenticated service-to-service traffic, and least privilege scopes each identity to its own calls.
- **C:** Correct. Scope permissions to the actions in use rather than the whole service. In this case: A service mesh provides authenticated service-to-service traffic, and least privilege scopes each identity to its own calls.
- **D:** Incorrect for this question. A legacy broad role that can change most resources in the project. Why the correct answer wins: A service mesh provides authenticated service-to-service traffic, and least privilege scopes each identity to its own calls.
- **E:** Correct. Mutual TLS, retries and traffic policy applied without changing application code. In this case: A service mesh provides authenticated service-to-service traffic, and least privilege scopes each identity to its own calls.

### Question 29 — B

Answer: Store the ledger in Spanner. A strongly consistent relational database refuses the inconsistent commit, which eventually consistent stores cannot promise. A relational database with strongly consistent multi-region transactions. Local study-map skill 1.16 (Storage and Schema Selection), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 1 (designing highly scalable, secure, and reliable cloud-native applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A document store with real-time listeners and mobile SDKs. Why the correct answer wins: A strongly consistent relational database refuses the inconsistent commit, which eventually consistent stores cannot promise.
- **B:** Correct. A relational database with strongly consistent multi-region transactions. In this case: A strongly consistent relational database refuses the inconsistent commit, which eventually consistent stores cannot promise.
- **C:** Incorrect for this question. Durable object storage addressed by name rather than a database row. Why the correct answer wins: A strongly consistent relational database refuses the inconsistent commit, which eventually consistent stores cannot promise.
- **D:** Incorrect for this question. Order the key so the query becomes a contiguous range scan. Why the correct answer wins: A strongly consistent relational database refuses the inconsistent commit, which eventually consistent stores cannot promise.

### Question 30 — D

Answer: Store the objects in Cloud Storage. Object storage is built for large immutable blobs addressed by name. Durable object storage addressed by name rather than a database row. Local study-map skill 1.16 (Storage and Schema Selection), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 1 (designing highly scalable, secure, and reliable cloud-native applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A document store with real-time listeners and mobile SDKs. Why the correct answer wins: Object storage is built for large immutable blobs addressed by name.
- **B:** Incorrect for this question. A managed Redis-compatible cache in front of the system of record. Why the correct answer wins: Object storage is built for large immutable blobs addressed by name.
- **C:** Incorrect for this question. A relational database with strongly consistent multi-region transactions. Why the correct answer wins: Object storage is built for large immutable blobs addressed by name.
- **D:** Correct. Durable object storage addressed by name rather than a database row. In this case: Object storage is built for large immutable blobs addressed by name.

### Question 31 — C

Answer: Issue a signed URL with a short expiry. A short-lived signed URL authorizes exactly that one operation for a bounded time. A time-limited grant to one object without exposing credentials. Local study-map skill 1.17 (Signed URLs and Time-Limited Access), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 1 (designing highly scalable, secure, and reliable cloud-native applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Serve every object to anyone, which removes the need to authorize at all. Why the correct answer wins: A short-lived signed URL authorizes exactly that one operation for a bounded time.
- **B:** Incorrect for this question. Transition or delete objects by age so retention happens without a job. Why the correct answer wins: A short-lived signed URL authorizes exactly that one operation for a bounded time.
- **C:** Correct. A time-limited grant to one object without exposing credentials. In this case: A short-lived signed URL authorizes exactly that one operation for a bounded time.
- **D:** Incorrect for this question. Make the retention period impossible to shorten, even by an owner. Why the correct answer wins: A short-lived signed URL authorizes exactly that one operation for a bounded time.

### Question 32 — A

Answer: Stream the events into BigQuery. Streaming the events lands them in the warehouse almost immediately for scoring. Land analytics rows in the warehouse for SQL and ML use. Local study-map skill 1.18 (Analytics and ML Data Handoff), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 1 (designing highly scalable, secure, and reliable cloud-native applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Correct. Land analytics rows in the warehouse for SQL and ML use. In this case: Streaming the events lands them in the warehouse almost immediately for scoring.
- **B:** Incorrect for this question. Load a periodic extract rather than a continuous stream. Why the correct answer wins: Streaming the events lands them in the warehouse almost immediately for scoring.
- **C:** Incorrect for this question. A relational database with strongly consistent multi-region transactions. Why the correct answer wins: Streaming the events lands them in the warehouse almost immediately for scoring.
- **D:** Incorrect for this question. Durable object storage addressed by name rather than a database row. Why the correct answer wins: Streaming the events lands them in the warehouse almost immediately for scoring.

### Question 33 — A, B

Answers: Run the service emulator locally; Run an integration test against the emulator. A local emulator provides the storage behaviour offline, and the integration test keeps the check enforced in the pipeline. A local stand-in for a managed service used for unit and integration work. Exercise the wire-up between components before deploying. Local study-map skill 2.1 (Local Emulation of Cloud Services), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 2 (building and testing applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Correct. Exercise the wire-up between components before deploying. In this case: A local emulator provides the storage behaviour offline, and the integration test keeps the check enforced in the pipeline.
- **B:** Correct. A local stand-in for a managed service used for unit and integration work. In this case: A local emulator provides the storage behaviour offline, and the integration test keeps the check enforced in the pipeline.
- **C:** Incorrect for this question. A browser terminal with the SDK and tooling already installed. Why the correct answer wins: A local emulator provides the storage behaviour offline, and the integration test keeps the check enforced in the pipeline.
- **D:** Incorrect for this question. A managed registry with IAM-scoped repositories per environment. Why the correct answer wins: A local emulator provides the storage behaviour offline, and the integration test keeps the check enforced in the pipeline.
- **E:** Incorrect for this question. Editor integration for scaffolding, running and debugging on Google Cloud. Why the correct answer wins: A local emulator provides the storage behaviour offline, and the integration test keeps the check enforced in the pipeline.

### Question 34 — B

Answer: Run the service emulator locally. A local emulator runs the messaging behaviour without a deployed resource. A local stand-in for a managed service used for unit and integration work. Local study-map skill 2.1 (Local Emulation of Cloud Services), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 2 (building and testing applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A managed, container-defined development environment behind a private endpoint. Why the correct answer wins: A local emulator runs the messaging behaviour without a deployed resource.
- **B:** Correct. A local stand-in for a managed service used for unit and integration work. In this case: A local emulator runs the messaging behaviour without a deployed resource.
- **C:** Incorrect for this question. A loop that rebuilds and redeploys automatically on a source change. Why the correct answer wins: A local emulator runs the messaging behaviour without a deployed resource.
- **D:** Incorrect for this question. A browser terminal with the SDK and tooling already installed. Why the correct answer wins: A local emulator runs the messaging behaviour without a deployed resource.

### Question 35 — D

Answer: Use Cloud Shell for the session. A browser terminal with the tooling preinstalled removes the provisioning wait. A browser terminal with the SDK and tooling already installed. Local study-map skill 2.1 (Local Emulation of Cloud Services), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 2 (building and testing applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A local stand-in for a managed service used for unit and integration work. Why the correct answer wins: A browser terminal with the tooling preinstalled removes the provisioning wait.
- **B:** Incorrect for this question. Editor integration for scaffolding, running and debugging on Google Cloud. Why the correct answer wins: A browser terminal with the tooling preinstalled removes the provisioning wait.
- **C:** Incorrect for this question. A managed, container-defined development environment behind a private endpoint. Why the correct answer wins: A browser terminal with the tooling preinstalled removes the provisioning wait.
- **D:** Correct. A browser terminal with the SDK and tooling already installed. In this case: A browser terminal with the tooling preinstalled removes the provisioning wait.

### Question 36 — A

Answer: Develop with Cloud Code in the IDE. Editor integration runs and debugs the service locally with working breakpoints. Editor integration for scaffolding, running and debugging on Google Cloud. Local study-map skill 2.2 (Developer Tooling and AI Assistance), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 2 (building and testing applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Correct. Editor integration for scaffolding, running and debugging on Google Cloud. In this case: Editor integration runs and debugs the service locally with working breakpoints.
- **B:** Incorrect for this question. A managed, container-defined development environment behind a private endpoint. Why the correct answer wins: Editor integration runs and debugs the service locally with working breakpoints.
- **C:** Incorrect for this question. Give the assistant a defined tool surface instead of pasting context by hand. Why the correct answer wins: Editor integration runs and debugs the service locally with working breakpoints.
- **D:** Incorrect for this question. A browser terminal with the SDK and tooling already installed. Why the correct answer wins: Editor integration runs and debugs the service locally with working breakpoints.

### Question 37 — C

Answer: Use Cloud Workstations for the environment. A managed workstation gives each contractor the defined image behind a private endpoint. A managed, container-defined development environment behind a private endpoint. Local study-map skill 2.2 (Developer Tooling and AI Assistance), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 2 (building and testing applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A browser terminal with the SDK and tooling already installed. Why the correct answer wins: A managed workstation gives each contractor the defined image behind a private endpoint.
- **B:** Incorrect for this question. A local stand-in for a managed service used for unit and integration work. Why the correct answer wins: A managed workstation gives each contractor the defined image behind a private endpoint.
- **C:** Correct. A managed, container-defined development environment behind a private endpoint. In this case: A managed workstation gives each contractor the defined image behind a private endpoint.
- **D:** Incorrect for this question. A loop that rebuilds and redeploys automatically on a source change. Why the correct answer wins: A managed workstation gives each contractor the defined image behind a private endpoint.

### Question 38 — D

Answer: Iterate with Skaffold. An automatic local iteration loop removes the manual build and deploy cycle. A loop that rebuilds and redeploys automatically on a source change. Local study-map skill 2.2 (Developer Tooling and AI Assistance), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 2 (building and testing applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Release exactly the artifact that was tested rather than a moving tag. Why the correct answer wins: An automatic local iteration loop removes the manual build and deploy cycle.
- **B:** Incorrect for this question. Hand the source to the managed builder instead of shipping an image. Why the correct answer wins: An automatic local iteration loop removes the manual build and deploy cycle.
- **C:** Incorrect for this question. A managed build service that runs the steps from a build configuration file. Why the correct answer wins: An automatic local iteration loop removes the manual build and deploy cycle.
- **D:** Correct. A loop that rebuilds and redeploys automatically on a source change. In this case: An automatic local iteration loop removes the manual build and deploy cycle.

### Question 39 — B, C

Answers: Build the image with Cloud Build; Push the image to Artifact Registry. The managed build service runs the steps in one definition, and the scoped registry holds the image under per-repository IAM. A managed build service that runs the steps from a build configuration file. A managed registry with IAM-scoped repositories per environment. Local study-map skill 2.3 (Container Builds with Cloud Build), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 2 (building and testing applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Editor integration for scaffolding, running and debugging on Google Cloud. Why the correct answer wins: The managed build service runs the steps in one definition, and the scoped registry holds the image under per-repository IAM.
- **B:** Correct. A managed registry with IAM-scoped repositories per environment. In this case: The managed build service runs the steps in one definition, and the scoped registry holds the image under per-repository IAM.
- **C:** Correct. A managed build service that runs the steps from a build configuration file. In this case: The managed build service runs the steps in one definition, and the scoped registry holds the image under per-repository IAM.
- **D:** Incorrect for this question. A browser terminal with the SDK and tooling already installed. Why the correct answer wins: The managed build service runs the steps in one definition, and the scoped registry holds the image under per-repository IAM.
- **E:** Incorrect for this question. The older registry whose access model is project-wide Cloud Storage. Why the correct answer wins: The managed build service runs the steps in one definition, and the scoped registry holds the image under per-repository IAM.

### Question 40 — B

Answer: Push the image to Artifact Registry. Repository-scoped IAM is what separates the two environments' image sets. A managed registry with IAM-scoped repositories per environment. Local study-map skill 2.3 (Container Builds with Cloud Build), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 2 (building and testing applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A browser terminal with the SDK and tooling already installed. Why the correct answer wins: Repository-scoped IAM is what separates the two environments' image sets.
- **B:** Correct. A managed registry with IAM-scoped repositories per environment. In this case: Repository-scoped IAM is what separates the two environments' image sets.
- **C:** Incorrect for this question. Durable object storage addressed by name rather than a database row. Why the correct answer wins: Repository-scoped IAM is what separates the two environments' image sets.
- **D:** Incorrect for this question. The older registry whose access model is project-wide Cloud Storage. Why the correct answer wins: Repository-scoped IAM is what separates the two environments' image sets.

### Question 41 — C

Answer: Deploy a pinned image digest. Deploying a pinned digest makes the running artifact identifiable and reproducible. Release exactly the artifact that was tested rather than a moving tag. Local study-map skill 2.3 (Container Builds with Cloud Build), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 2 (building and testing applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Start the pipeline when the branch changes rather than by hand. Why the correct answer wins: Deploying a pinned digest makes the running artifact identifiable and reproducible.
- **B:** Incorrect for this question. Hand the source to the managed builder instead of shipping an image. Why the correct answer wins: Deploying a pinned digest makes the running artifact identifiable and reproducible.
- **C:** Correct. Release exactly the artifact that was tested rather than a moving tag. In this case: Deploying a pinned digest makes the running artifact identifiable and reproducible.
- **D:** Incorrect for this question. Wrap the existing process in a portable artifact that a managed runtime can execute. Why the correct answer wins: Deploying a pinned digest makes the running artifact identifiable and reproducible.

### Question 42 — C

Answer: Trigger the build from a repository push. A repository trigger builds on every push, keeping the artifact tied to the commit. Start the pipeline when the branch changes rather than by hand. Local study-map skill 2.3 (Container Builds with Cloud Build), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 2 (building and testing applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Run the build steps locally and push the result when someone remembers. Why the correct answer wins: A repository trigger builds on every push, keeping the artifact tied to the commit.
- **B:** Incorrect for this question. A cron-style trigger that calls a target on a fixed timetable. Why the correct answer wins: A repository trigger builds on every push, keeping the artifact tied to the commit.
- **C:** Correct. Start the pipeline when the branch changes rather than by hand. In this case: A repository trigger builds on every push, keeping the artifact tied to the commit.
- **D:** Incorrect for this question. A task queue with retries and rate control aimed at a specific target. Why the correct answer wins: A repository trigger builds on every push, keeping the artifact tied to the commit.

### Question 43 — C

Answer: Push the image to Artifact Registry. A regional managed registry keeps image pulls close to the runtime. A managed registry with IAM-scoped repositories per environment. Local study-map skill 2.4 (Artifact Registry and Image Storage), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 2 (building and testing applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A managed build service that runs the steps from a build configuration file. Why the correct answer wins: A regional managed registry keeps image pulls close to the runtime.
- **B:** Incorrect for this question. The older registry whose access model is project-wide Cloud Storage. Why the correct answer wins: A regional managed registry keeps image pulls close to the runtime.
- **C:** Correct. A managed registry with IAM-scoped repositories per environment. In this case: A regional managed registry keeps image pulls close to the runtime.
- **D:** Incorrect for this question. Durable object storage addressed by name rather than a database row. Why the correct answer wins: A regional managed registry keeps image pulls close to the runtime.

### Question 44 — A

Answer: Push the image to Container Registry. The older registry grants project-wide access, which is why it is being replaced. The older registry whose access model is project-wide Cloud Storage. Local study-map skill 2.4 (Artifact Registry and Image Storage), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 2 (building and testing applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Correct. The older registry whose access model is project-wide Cloud Storage. In this case: The older registry grants project-wide access, which is why it is being replaced.
- **B:** Incorrect for this question. A managed build service that runs the steps from a build configuration file. Why the correct answer wins: The older registry grants project-wide access, which is why it is being replaced.
- **C:** Incorrect for this question. Durable object storage addressed by name rather than a database row. Why the correct answer wins: The older registry grants project-wide access, which is why it is being replaced.
- **D:** Incorrect for this question. A managed registry with IAM-scoped repositories per environment. Why the correct answer wins: The older registry grants project-wide access, which is why it is being replaced.

### Question 45 — A

Answer: Store the objects in Cloud Storage. Object storage is the durable home for non-image artifacts. Durable object storage addressed by name rather than a database row. Local study-map skill 2.4 (Artifact Registry and Image Storage), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 2 (building and testing applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Correct. Durable object storage addressed by name rather than a database row. In this case: Object storage is the durable home for non-image artifacts.
- **B:** Incorrect for this question. A managed build service that runs the steps from a build configuration file. Why the correct answer wins: Object storage is the durable home for non-image artifacts.
- **C:** Incorrect for this question. A managed registry with IAM-scoped repositories per environment. Why the correct answer wins: Object storage is the durable home for non-image artifacts.
- **D:** Incorrect for this question. The older registry whose access model is project-wide Cloud Storage. Why the correct answer wins: Object storage is the durable home for non-image artifacts.

### Question 46 — A

Answer: Generate build provenance in Cloud Build. Provenance records the source and the builder for the artifact. A signed record of what was built and from which source. Local study-map skill 2.5 (Build Provenance and Admission Control), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 2 (building and testing applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Correct. A signed record of what was built and from which source. In this case: Provenance records the source and the builder for the artifact.
- **B:** Incorrect for this question. Only images that satisfy the attestation policy may be deployed. Why the correct answer wins: Provenance records the source and the builder for the artifact.
- **C:** Incorrect for this question. Aggregate and triage security findings across the project. Why the correct answer wins: Provenance records the source and the builder for the artifact.
- **D:** Incorrect for this question. Report known vulnerabilities in the image layers and packages. Why the correct answer wins: Provenance records the source and the builder for the artifact.

### Question 47 — B

Answer: Review the finding in Security Command Center. The security command centre aggregates and triages findings in one place. Aggregate and triage security findings across the project. Local study-map skill 2.5 (Build Provenance and Admission Control), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 2 (building and testing applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Report known vulnerabilities in the image layers and packages. Why the correct answer wins: The security command centre aggregates and triages findings in one place.
- **B:** Correct. Aggregate and triage security findings across the project. In this case: The security command centre aggregates and triages findings in one place.
- **C:** Incorrect for this question. Only images that satisfy the attestation policy may be deployed. Why the correct answer wins: The security command centre aggregates and triages findings in one place.
- **D:** Incorrect for this question. Group and count application errors instead of grepping logs. Why the correct answer wins: The security command centre aggregates and triages findings in one place.

### Question 48 — B

Answer: Scan the image with Artifact Analysis. Image scanning maps the vulnerability to the affected images. Report known vulnerabilities in the image layers and packages. Local study-map skill 2.5 (Build Provenance and Admission Control), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 2 (building and testing applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A signed record of what was built and from which source. Why the correct answer wins: Image scanning maps the vulnerability to the affected images.
- **B:** Correct. Report known vulnerabilities in the image layers and packages. In this case: Image scanning maps the vulnerability to the affected images.
- **C:** Incorrect for this question. Aggregate and triage security findings across the project. Why the correct answer wins: Image scanning maps the vulnerability to the affected images.
- **D:** Incorrect for this question. Only images that satisfy the attestation policy may be deployed. Why the correct answer wins: Image scanning maps the vulnerability to the affected images.

### Question 49 — A, E

Answers: Add a unit test with dependencies stubbed; Quarantine the flaky test and fix it. Quarantining the unstable test removes the noise, and repairing it keeps the coverage rather than deleting it. Exercise one unit in isolation with its collaborators replaced. Keep the suite trustworthy while the unstable test is repaired. Local study-map skill 2.6 (Unit Testing Practice), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 2 (building and testing applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Correct. Keep the suite trustworthy while the unstable test is repaired. In this case: Quarantining the unstable test removes the noise, and repairing it keeps the coverage rather than deleting it.
- **B:** Incorrect for this question. Make a passing test suite a precondition for release. Why the correct answer wins: Quarantining the unstable test removes the noise, and repairing it keeps the coverage rather than deleting it.
- **C:** Incorrect for this question. Exercise the wire-up between components before deploying. Why the correct answer wins: Quarantining the unstable test removes the noise, and repairing it keeps the coverage rather than deleting it.
- **D:** Incorrect for this question. Measure behaviour under expected peak traffic rather than guessing. Why the correct answer wins: Quarantining the unstable test removes the noise, and repairing it keeps the coverage rather than deleting it.
- **E:** Correct. Exercise one unit in isolation with its collaborators replaced. In this case: Quarantining the unstable test removes the noise, and repairing it keeps the coverage rather than deleting it.

### Question 50 — B

Answer: Add a unit test with dependencies stubbed. Unit tests with stubbed collaborators isolate each branch and name it on failure. Exercise one unit in isolation with its collaborators replaced. Local study-map skill 2.6 (Unit Testing Practice), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 2 (building and testing applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Exercise the wire-up between components before deploying. Why the correct answer wins: Unit tests with stubbed collaborators isolate each branch and name it on failure.
- **B:** Correct. Exercise one unit in isolation with its collaborators replaced. In this case: Unit tests with stubbed collaborators isolate each branch and name it on failure.
- **C:** Incorrect for this question. Keep the suite trustworthy while the unstable test is repaired. Why the correct answer wins: Unit tests with stubbed collaborators isolate each branch and name it on failure.
- **D:** Incorrect for this question. Measure behaviour under expected peak traffic rather than guessing. Why the correct answer wins: Unit tests with stubbed collaborators isolate each branch and name it on failure.

### Question 51 — A

Answer: Use an AI coding assistant to draft the tests. The assistant produces the draft from context, which the developer then reviews and corrects. Generate a first draft from context, then review and correct it. Local study-map skill 2.6 (Unit Testing Practice), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 2 (building and testing applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Correct. Generate a first draft from context, then review and correct it. In this case: The assistant produces the draft from context, which the developer then reviews and corrects.
- **B:** Incorrect for this question. Editor integration for scaffolding, running and debugging on Google Cloud. Why the correct answer wins: The assistant produces the draft from context, which the developer then reviews and corrects.
- **C:** Incorrect for this question. Give the assistant a defined tool surface instead of pasting context by hand. Why the correct answer wins: The assistant produces the draft from context, which the developer then reviews and corrects.
- **D:** Incorrect for this question. An assistant that reads telemetry and proposes a cause and a next step. Why the correct answer wins: The assistant produces the draft from context, which the developer then reviews and corrects.

### Question 52 — D, E

Answers: Run an integration test against the emulator; Run the tests as a Cloud Build step. An integration test runs both sides against the same contract, and a build step makes that check unavoidable on every merge. Exercise the wire-up between components before deploying. Fail the pipeline at the test stage instead of after deployment. Local study-map skill 2.7 (Automated Integration Testing), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 2 (building and testing applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Make a passing test suite a precondition for release. Why the correct answer wins: An integration test runs both sides against the same contract, and a build step makes that check unavoidable on every merge.
- **B:** Incorrect for this question. Exercise one unit in isolation with its collaborators replaced. Why the correct answer wins: An integration test runs both sides against the same contract, and a build step makes that check unavoidable on every merge.
- **C:** Incorrect for this question. Measure behaviour under expected peak traffic rather than guessing. Why the correct answer wins: An integration test runs both sides against the same contract, and a build step makes that check unavoidable on every merge.
- **D:** Correct. Exercise the wire-up between components before deploying. In this case: An integration test runs both sides against the same contract, and a build step makes that check unavoidable on every merge.
- **E:** Correct. Fail the pipeline at the test stage instead of after deployment. In this case: An integration test runs both sides against the same contract, and a build step makes that check unavoidable on every merge.

### Question 53 — C

Answer: Run the tests as a Cloud Build step. Running the suite inside the pipeline catches the failure before the artifact is released. Fail the pipeline at the test stage instead of after deployment. Local study-map skill 2.7 (Automated Integration Testing), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 2 (building and testing applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Make a passing test suite a precondition for release. Why the correct answer wins: Running the suite inside the pipeline catches the failure before the artifact is released.
- **B:** Incorrect for this question. Measure behaviour under expected peak traffic rather than guessing. Why the correct answer wins: Running the suite inside the pipeline catches the failure before the artifact is released.
- **C:** Correct. Fail the pipeline at the test stage instead of after deployment. In this case: Running the suite inside the pipeline catches the failure before the artifact is released.
- **D:** Incorrect for this question. Keep the suite trustworthy while the unstable test is repaired. Why the correct answer wins: Running the suite inside the pipeline catches the failure before the artifact is released.

### Question 54 — D

Answer: Block the deploy on the test result. Making the suite a precondition for release stops a failing build from shipping. Make a passing test suite a precondition for release. Local study-map skill 2.7 (Automated Integration Testing), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 2 (building and testing applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Exercise one unit in isolation with its collaborators replaced. Why the correct answer wins: Making the suite a precondition for release stops a failing build from shipping.
- **B:** Incorrect for this question. Fail the pipeline at the test stage instead of after deployment. Why the correct answer wins: Making the suite a precondition for release stops a failing build from shipping.
- **C:** Incorrect for this question. Keep the suite trustworthy while the unstable test is repaired. Why the correct answer wins: Making the suite a precondition for release stops a failing build from shipping.
- **D:** Correct. Make a passing test suite a precondition for release. In this case: Making the suite a precondition for release stops a failing build from shipping.

### Question 55 — C

Answer: Load-test the release before the rollout. A load test measures behaviour at the expected peak before the launch. Measure behaviour under expected peak traffic rather than guessing. Local study-map skill 2.7 (Automated Integration Testing), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 2 (building and testing applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Exercise one unit in isolation with its collaborators replaced. Why the correct answer wins: A load test measures behaviour at the expected peak before the launch.
- **B:** Incorrect for this question. Exercise the wire-up between components before deploying. Why the correct answer wins: A load test measures behaviour at the expected peak before the launch.
- **C:** Correct. Measure behaviour under expected peak traffic rather than guessing. In this case: A load test measures behaviour at the expected peak before the launch.
- **D:** Incorrect for this question. Find the function consuming CPU or memory under real traffic. Why the correct answer wins: A load test measures behaviour at the expected peak before the launch.

### Question 56 — D

Answer: Deploy from source and let the platform build it. Deploying from source lets the platform build and run the service without a written artifact. Hand the source to the managed builder instead of shipping an image. Local study-map skill 3.1 (Deploying Cloud Run from Source), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 3 (configuring cloud-native applications for deployment): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Release exactly the artifact that was tested rather than a moving tag. Why the correct answer wins: Deploying from source lets the platform build and run the service without a written artifact.
- **B:** Incorrect for this question. Wrap the existing process in a portable artifact that a managed runtime can execute. Why the correct answer wins: Deploying from source lets the platform build and run the service without a written artifact.
- **C:** Incorrect for this question. A managed build service that runs the steps from a build configuration file. Why the correct answer wins: Deploying from source lets the platform build and run the service without a written artifact.
- **D:** Correct. Hand the source to the managed builder instead of shipping an image. In this case: Deploying from source lets the platform build and run the service without a written artifact.

### Question 57 — C

Answer: Restrict ingress to internal traffic. Internal ingress removes the public entry path entirely. Accept only traffic from the VPC and internal load balancers. Local study-map skill 3.1 (Deploying Cloud Run from Source), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 3 (configuring cloud-native applications for deployment): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Let anyone reach the endpoint, which is only appropriate for public content. Why the correct answer wins: Internal ingress removes the public entry path entirely.
- **B:** Incorrect for this question. Authenticate and authorize users before a request reaches the application. Why the correct answer wins: Internal ingress removes the public entry path entirely.
- **C:** Correct. Accept only traffic from the VPC and internal load balancers. In this case: Internal ingress removes the public entry path entirely.
- **D:** Incorrect for this question. Control who may call the service with IAM rather than a shared token. Why the correct answer wins: Internal ingress removes the public entry path entirely.

### Question 58 — C

Answer: Grant the invoker role to the calling identity. The invoker role on that service scopes the permission to the one caller. Control who may call the service with IAM rather than a shared token. Local study-map skill 3.1 (Deploying Cloud Run from Source), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 3 (configuring cloud-native applications for deployment): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A legacy broad role that can change most resources in the project. Why the correct answer wins: The invoker role on that service scopes the permission to the one caller.
- **B:** Incorrect for this question. Authenticate and authorize users before a request reaches the application. Why the correct answer wins: The invoker role on that service scopes the permission to the one caller.
- **C:** Correct. Control who may call the service with IAM rather than a shared token. In this case: The invoker role on that service scopes the permission to the one caller.
- **D:** Incorrect for this question. Let anyone reach the endpoint, which is only appropriate for public content. Why the correct answer wins: The invoker role on that service scopes the permission to the one caller.

### Question 59 — D

Answer: Deploy a pinned image digest. The pinned digest of the previous image restores precisely that artifact. Release exactly the artifact that was tested rather than a moving tag. Local study-map skill 3.1 (Deploying Cloud Run from Source), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 3 (configuring cloud-native applications for deployment): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Wrap the existing process in a portable artifact that a managed runtime can execute. Why the correct answer wins: The pinned digest of the previous image restores precisely that artifact.
- **B:** Incorrect for this question. A managed build service that runs the steps from a build configuration file. Why the correct answer wins: The pinned digest of the previous image restores precisely that artifact.
- **C:** Incorrect for this question. Hand the source to the managed builder instead of shipping an image. Why the correct answer wins: The pinned digest of the previous image restores precisely that artifact.
- **D:** Correct. Release exactly the artifact that was tested rather than a moving tag. In this case: The pinned digest of the previous image restores precisely that artifact.

### Question 60 — C

Answer: Route the event with Eventarc. An eventarc trigger turns the audit event into a delivery to the service. A trigger path that turns a Cloud Audit Log or resource event into a delivery. Local study-map skill 3.2 (Cloud Run Triggers and Event Receivers), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 3 (configuring cloud-native applications for deployment): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A cron-style trigger that calls a target on a fixed timetable. Why the correct answer wins: An eventarc trigger turns the audit event into a delivery to the service.
- **B:** Incorrect for this question. A task queue with retries and rate control aimed at a specific target. Why the correct answer wins: An eventarc trigger turns the audit event into a delivery to the service.
- **C:** Correct. A trigger path that turns a Cloud Audit Log or resource event into a delivery. In this case: An eventarc trigger turns the audit event into a delivery to the service.
- **D:** Incorrect for this question. A durable, at-least-once message channel with independent subscribers. Why the correct answer wins: An eventarc trigger turns the audit event into a delivery to the service.

### Question 61 — D

Answer: Have the worker pull from the subscription. A pulling consumer chooses what to take next and acknowledges after the commit. The consumer controls the pace and acknowledges messages itself. Local study-map skill 3.2 (Cloud Run Triggers and Event Receivers), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 3 (configuring cloud-native applications for deployment): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A task queue with retries and rate control aimed at a specific target. Why the correct answer wins: A pulling consumer chooses what to take next and acknowledges after the commit.
- **B:** Incorrect for this question. Push each message to an endpoint instead of having the consumer pull. Why the correct answer wins: A pulling consumer chooses what to take next and acknowledges after the commit.
- **C:** Incorrect for this question. A trigger path that turns a Cloud Audit Log or resource event into a delivery. Why the correct answer wins: A pulling consumer chooses what to take next and acknowledges after the commit.
- **D:** Correct. The consumer controls the pace and acknowledges messages itself. In this case: A pulling consumer chooses what to take next and acknowledges after the commit.

### Question 62 — A, B

Answers: Schedule the invocation with Cloud Scheduler; Queue the work as a Cloud Tasks task. The scheduler provides the timetable, and the task queue handles per-order retries against the partner. A cron-style trigger that calls a target on a fixed timetable. A task queue with retries and rate control aimed at a specific target. Local study-map skill 3.2 (Cloud Run Triggers and Event Receivers), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 3 (configuring cloud-native applications for deployment): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Correct. A task queue with retries and rate control aimed at a specific target. In this case: The scheduler provides the timetable, and the task queue handles per-order retries against the partner.
- **B:** Correct. A cron-style trigger that calls a target on a fixed timetable. In this case: The scheduler provides the timetable, and the task queue handles per-order retries against the partner.
- **C:** Incorrect for this question. A stateful sequence of service calls with retries and error branches. Why the correct answer wins: The scheduler provides the timetable, and the task queue handles per-order retries against the partner.
- **D:** Incorrect for this question. A durable, at-least-once message channel with independent subscribers. Why the correct answer wins: The scheduler provides the timetable, and the task queue handles per-order retries against the partner.
- **E:** Incorrect for this question. A trigger path that turns a Cloud Audit Log or resource event into a delivery. Why the correct answer wins: The scheduler provides the timetable, and the task queue handles per-order retries against the partner.

### Question 63 — B

Answer: Orchestrate the steps in Workflows. A stateful orchestration holds the sequence with error branches and retries. A stateful sequence of service calls with retries and error branches. Local study-map skill 3.2 (Cloud Run Triggers and Event Receivers), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 3 (configuring cloud-native applications for deployment): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A cron-style trigger that calls a target on a fixed timetable. Why the correct answer wins: A stateful orchestration holds the sequence with error branches and retries.
- **B:** Correct. A stateful sequence of service calls with retries and error branches. In this case: A stateful orchestration holds the sequence with error branches and retries.
- **C:** Incorrect for this question. A durable, at-least-once message channel with independent subscribers. Why the correct answer wins: A stateful orchestration holds the sequence with error branches and retries.
- **D:** Incorrect for this question. A task queue with retries and rate control aimed at a specific target. Why the correct answer wins: A stateful orchestration holds the sequence with error branches and retries.

### Question 64 — A, C

Answers: Raise the per-instance concurrency limit; Cap the maximum instance count. Concurrency controls how much work shares an instance's memory, and a maximum instance cap bounds the cost. Let each instance serve more simultaneous requests before another instance is started. Bound the blast radius and the bill at the cost of queueing when the cap is reached. Local study-map skill 3.3 (Cloud Run Service Configuration), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 3 (configuring cloud-native applications for deployment): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Correct. Let each instance serve more simultaneous requests before another instance is started. In this case: Concurrency controls how much work shares an instance's memory, and a maximum instance cap bounds the cost.
- **B:** Incorrect for this question. Charge for the whole instance lifetime, which suits steady background work. Why the correct answer wins: Concurrency controls how much work shares an instance's memory, and a maximum instance cap bounds the cost.
- **C:** Correct. Bound the blast radius and the bill at the cost of queueing when the cap is reached. In this case: Concurrency controls how much work shares an instance's memory, and a maximum instance cap bounds the cost.
- **D:** Incorrect for this question. Pay for idle capacity so a cold start never appears in the latency percentiles. Why the correct answer wins: Concurrency controls how much work shares an instance's memory, and a maximum instance cap bounds the cost.
- **E:** Incorrect for this question. Give extra CPU during start-up so initialization finishes faster at a small extra charge. Why the correct answer wins: Concurrency controls how much work shares an instance's memory, and a maximum instance cap bounds the cost.

### Question 65 — C

Answer: Keep a minimum number of instances warm. A minimum instance count keeps capacity ready so no request waits for start-up. Pay for idle capacity so a cold start never appears in the latency percentiles. Local study-map skill 3.3 (Cloud Run Service Configuration), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 3 (configuring cloud-native applications for deployment): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Bound the blast radius and the bill at the cost of queueing when the cap is reached. Why the correct answer wins: A minimum instance count keeps capacity ready so no request waits for start-up.
- **B:** Incorrect for this question. Give extra CPU during start-up so initialization finishes faster at a small extra charge. Why the correct answer wins: A minimum instance count keeps capacity ready so no request waits for start-up.
- **C:** Correct. Pay for idle capacity so a cold start never appears in the latency percentiles. In this case: A minimum instance count keeps capacity ready so no request waits for start-up.
- **D:** Incorrect for this question. Let each instance serve more simultaneous requests before another instance is started. Why the correct answer wins: A minimum instance count keeps capacity ready so no request waits for start-up.

### Question 66 — C

Answer: Configure a startup probe. A startup probe withholds traffic until the application reports readiness. Hold traffic until the application is actually ready to serve. Local study-map skill 3.3 (Cloud Run Service Configuration), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 3 (configuring cloud-native applications for deployment): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Restart the container when it can no longer make progress. Why the correct answer wins: A startup probe withholds traffic until the application reports readiness.
- **B:** Incorrect for this question. Add pods on a signal that tracks demand better than CPU. Why the correct answer wins: A startup probe withholds traffic until the application reports readiness.
- **C:** Correct. Hold traffic until the application is actually ready to serve. In this case: A startup probe withholds traffic until the application reports readiness.
- **D:** Incorrect for this question. Remove the instance from the endpoint list while it cannot serve. Why the correct answer wins: A startup probe withholds traffic until the application reports readiness.

### Question 67 — C

Answer: Enable CPU boost at startup. Start-up CPU boost shortens initialization without paying for extra CPU afterwards. Give extra CPU during start-up so initialization finishes faster at a small extra charge. Local study-map skill 3.3 (Cloud Run Service Configuration), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 3 (configuring cloud-native applications for deployment): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Let each instance serve more simultaneous requests before another instance is started. Why the correct answer wins: Start-up CPU boost shortens initialization without paying for extra CPU afterwards.
- **B:** Incorrect for this question. Bound the blast radius and the bill at the cost of queueing when the cap is reached. Why the correct answer wins: Start-up CPU boost shortens initialization without paying for extra CPU afterwards.
- **C:** Correct. Give extra CPU during start-up so initialization finishes faster at a small extra charge. In this case: Start-up CPU boost shortens initialization without paying for extra CPU afterwards.
- **D:** Incorrect for this question. Pay for idle capacity so a cold start never appears in the latency percentiles. Why the correct answer wins: Start-up CPU boost shortens initialization without paying for extra CPU afterwards.

### Question 68 — D

Answer: Introduce a new API version alongside the old one. Running a new version alongside the old one keeps existing clients working. Keep the old contract working while the new one is adopted. Local study-map skill 3.4 (API Exposure and Versioning), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 3 (configuring cloud-native applications for deployment): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A machine-readable contract that generates clients and validates requests. Why the correct answer wins: Running a new version alongside the old one keeps existing clients working.
- **B:** Incorrect for this question. Reject or queue requests above a threshold so one client cannot exhaust the service. Why the correct answer wins: Running a new version alongside the old one keeps existing clients working.
- **C:** Incorrect for this question. Extend the contract so existing clients keep working unchanged. Why the correct answer wins: Running a new version alongside the old one keeps existing clients working.
- **D:** Correct. Keep the old contract working while the new one is adopted. In this case: Running a new version alongside the old one keeps existing clients working.

### Question 69 — A

Answer: Put Apigee in front of the API. An API management layer mediates the contract so the backend can change behind it. An API management layer for quotas, keys, mediation and analytics. Local study-map skill 3.4 (API Exposure and Versioning), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 3 (configuring cloud-native applications for deployment): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Correct. An API management layer for quotas, keys, mediation and analytics. In this case: An API management layer mediates the contract so the backend can change behind it.
- **B:** Incorrect for this question. A lighter managed gateway for routing and key-based quota enforcement. Why the correct answer wins: An API management layer mediates the contract so the backend can change behind it.
- **C:** Incorrect for this question. Reject or queue requests above a threshold so one client cannot exhaust the service. Why the correct answer wins: An API management layer mediates the contract so the backend can change behind it.
- **D:** Incorrect for this question. Keep the old contract working while the new one is adopted. Why the correct answer wins: An API management layer mediates the contract so the backend can change behind it.

### Question 70 — D

Answer: Use a rolling update strategy. A rolling update replaces pods gradually so capacity remains throughout. Replace pods gradually so the deployment stays available. Local study-map skill 3.5 (Deploying Containers to GKE), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 3 (configuring cloud-native applications for deployment): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Limit how many pods may be evicted at once during voluntary disruption. Why the correct answer wins: A rolling update replaces pods gradually so capacity remains throughout.
- **B:** Incorrect for this question. Place work on nodes whose shape and pricing match the workload. Why the correct answer wins: A rolling update replaces pods gradually so capacity remains throughout.
- **C:** Incorrect for this question. Bound the total capacity a namespace may consume. Why the correct answer wins: A rolling update replaces pods gradually so capacity remains throughout.
- **D:** Correct. Replace pods gradually so the deployment stays available. In this case: A rolling update replaces pods gradually so capacity remains throughout.

### Question 71 — A, D

Answers: Constrain pods to the intended node pool; Set a namespace resource quota. Affinity keeps the workload on the nodes sized for it, and a namespace quota bounds what one team can take. Place work on nodes whose shape and pricing match the workload. Bound the total capacity a namespace may consume. Local study-map skill 3.5 (Deploying Containers to GKE), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 3 (configuring cloud-native applications for deployment): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Correct. Place work on nodes whose shape and pricing match the workload. In this case: Affinity keeps the workload on the nodes sized for it, and a namespace quota bounds what one team can take.
- **B:** Incorrect for this question. Limit how many pods may be evicted at once during voluntary disruption. Why the correct answer wins: Affinity keeps the workload on the nodes sized for it, and a namespace quota bounds what one team can take.
- **C:** Incorrect for this question. Use reclaimable capacity for work that can tolerate a node disappearing. Why the correct answer wins: Affinity keeps the workload on the nodes sized for it, and a namespace quota bounds what one team can take.
- **D:** Correct. Bound the total capacity a namespace may consume. In this case: Affinity keeps the workload on the nodes sized for it, and a namespace quota bounds what one team can take.
- **E:** Incorrect for this question. Keep capacity warm so scale-up does not cost the first requests. Why the correct answer wins: Affinity keeps the workload on the nodes sized for it, and a namespace quota bounds what one team can take.

### Question 72 — A

Answer: Add a PodDisruptionBudget. A disruption budget limits how many pods may be evicted together. Limit how many pods may be evicted at once during voluntary disruption. Local study-map skill 3.5 (Deploying Containers to GKE), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 3 (configuring cloud-native applications for deployment): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Correct. Limit how many pods may be evicted at once during voluntary disruption. In this case: A disruption budget limits how many pods may be evicted together.
- **B:** Incorrect for this question. Replace pods gradually so the deployment stays available. Why the correct answer wins: A disruption budget limits how many pods may be evicted together.
- **C:** Incorrect for this question. Keep capacity warm so scale-up does not cost the first requests. Why the correct answer wins: A disruption budget limits how many pods may be evicted together.
- **D:** Incorrect for this question. Bound the total capacity a namespace may consume. Why the correct answer wins: A disruption budget limits how many pods may be evicted together.

### Question 73 — D

Answer: Run the batch node pool on Spot VMs. Reclaimable capacity fits work that can be retried after an interruption. Use reclaimable capacity for work that can tolerate a node disappearing. Local study-map skill 3.5 (Deploying Containers to GKE), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 3 (configuring cloud-native applications for deployment): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Trade a term commitment for a lower unit price on capacity that never idles. Why the correct answer wins: Reclaimable capacity fits work that can be retried after an interruption.
- **B:** Incorrect for this question. Give the scheduler real numbers so placement and scaling decisions are not guesses. Why the correct answer wins: Reclaimable capacity fits work that can be retried after an interruption.
- **C:** Incorrect for this question. Add or remove nodes as pending pods demand capacity. Why the correct answer wins: Reclaimable capacity fits work that can be retried after an interruption.
- **D:** Correct. Use reclaimable capacity for work that can tolerate a node disappearing. In this case: Reclaimable capacity fits work that can be retried after an interruption.

### Question 74 — A

Answer: Configure a readiness probe. A readiness probe removes it from the endpoint list while it cannot serve. Remove the instance from the endpoint list while it cannot serve. Local study-map skill 3.6 (Kubernetes Health Checks), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 3 (configuring cloud-native applications for deployment): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Correct. Remove the instance from the endpoint list while it cannot serve. In this case: A readiness probe removes it from the endpoint list while it cannot serve.
- **B:** Incorrect for this question. Limit how many pods may be evicted at once during voluntary disruption. Why the correct answer wins: A readiness probe removes it from the endpoint list while it cannot serve.
- **C:** Incorrect for this question. Hold traffic until the application is actually ready to serve. Why the correct answer wins: A readiness probe removes it from the endpoint list while it cannot serve.
- **D:** Incorrect for this question. Restart the container when it can no longer make progress. Why the correct answer wins: A readiness probe removes it from the endpoint list while it cannot serve.

### Question 75 — A

Answer: Configure a liveness probe. A liveness probe restarts a container that can no longer make progress. Restart the container when it can no longer make progress. Local study-map skill 3.6 (Kubernetes Health Checks), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 3 (configuring cloud-native applications for deployment): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Correct. Restart the container when it can no longer make progress. In this case: A liveness probe restarts a container that can no longer make progress.
- **B:** Incorrect for this question. Bound the total capacity a namespace may consume. Why the correct answer wins: A liveness probe restarts a container that can no longer make progress.
- **C:** Incorrect for this question. Hold traffic until the application is actually ready to serve. Why the correct answer wins: A liveness probe restarts a container that can no longer make progress.
- **D:** Incorrect for this question. Remove the instance from the endpoint list while it cannot serve. Why the correct answer wins: A liveness probe restarts a container that can no longer make progress.

### Question 76 — B

Answer: Configure a liveness probe. A liveness probe restarts a container that can no longer make progress. Restart the container when it can no longer make progress. Local study-map skill 3.6 (Kubernetes Health Checks), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 3 (configuring cloud-native applications for deployment): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Remove the instance from the endpoint list while it cannot serve. Why the correct answer wins: A liveness probe restarts a container that can no longer make progress.
- **B:** Correct. Restart the container when it can no longer make progress. In this case: A liveness probe restarts a container that can no longer make progress.
- **C:** Incorrect for this question. Hold traffic until the application is actually ready to serve. Why the correct answer wins: A liveness probe restarts a container that can no longer make progress.
- **D:** Incorrect for this question. Limit how many pods may be evicted at once during voluntary disruption. Why the correct answer wins: A liveness probe restarts a container that can no longer make progress.

### Question 77 — B

Answer: Scale pods on a custom or external metric. A custom metric on backlog depth tracks the demand the CPU number hides. Add pods on a signal that tracks demand better than CPU. Local study-map skill 3.7 (Horizontal Pod Autoscaling), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 3 (configuring cloud-native applications for deployment): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Add or remove nodes as pending pods demand capacity. Why the correct answer wins: A custom metric on backlog depth tracks the demand the CPU number hides.
- **B:** Correct. Add pods on a signal that tracks demand better than CPU. In this case: A custom metric on backlog depth tracks the demand the CPU number hides.
- **C:** Incorrect for this question. Keep capacity warm so scale-up does not cost the first requests. Why the correct answer wins: A custom metric on backlog depth tracks the demand the CPU number hides.
- **D:** Incorrect for this question. Add pods when average CPU crosses the target. Why the correct answer wins: A custom metric on backlog depth tracks the demand the CPU number hides.

### Question 78 — A, B

Answers: Set a minimum replica count; Add a PodDisruptionBudget. A minimum replica count holds the floor, and a disruption budget protects quorum during voluntary eviction. Keep capacity warm so scale-up does not cost the first requests. Limit how many pods may be evicted at once during voluntary disruption. Local study-map skill 3.7 (Horizontal Pod Autoscaling), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 3 (configuring cloud-native applications for deployment): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Correct. Limit how many pods may be evicted at once during voluntary disruption. In this case: A minimum replica count holds the floor, and a disruption budget protects quorum during voluntary eviction.
- **B:** Correct. Keep capacity warm so scale-up does not cost the first requests. In this case: A minimum replica count holds the floor, and a disruption budget protects quorum during voluntary eviction.
- **C:** Incorrect for this question. Add pods on a signal that tracks demand better than CPU. Why the correct answer wins: A minimum replica count holds the floor, and a disruption budget protects quorum during voluntary eviction.
- **D:** Incorrect for this question. Add pods when average CPU crosses the target. Why the correct answer wins: A minimum replica count holds the floor, and a disruption budget protects quorum during voluntary eviction.
- **E:** Incorrect for this question. Bound the total capacity a namespace may consume. Why the correct answer wins: A minimum replica count holds the floor, and a disruption budget protects quorum during voluntary eviction.

### Question 79 — B

Answer: Enable node pool autoscaling. Node pool autoscaling adds nodes when pods cannot be scheduled. Add or remove nodes as pending pods demand capacity. Local study-map skill 3.7 (Horizontal Pod Autoscaling), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 3 (configuring cloud-native applications for deployment): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Bound the total capacity a namespace may consume. Why the correct answer wins: Node pool autoscaling adds nodes when pods cannot be scheduled.
- **B:** Correct. Add or remove nodes as pending pods demand capacity. In this case: Node pool autoscaling adds nodes when pods cannot be scheduled.
- **C:** Incorrect for this question. Use reclaimable capacity for work that can tolerate a node disappearing. Why the correct answer wins: Node pool autoscaling adds nodes when pods cannot be scheduled.
- **D:** Incorrect for this question. Add pods when average CPU crosses the target. Why the correct answer wins: Node pool autoscaling adds nodes when pods cannot be scheduled.

### Question 80 — C

Answer: Connect through the Cloud SQL Auth Proxy. The authorized proxy supplies identity and encryption without a public path. A local proxy that authorizes the connection with IAM and encrypts it. Local study-map skill 4.1 (Connecting to Datastores), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 4 (integrating applications with Google Cloud services): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A client library that resolves and authorizes the instance itself. Why the correct answer wins: The authorized proxy supplies identity and encryption without a public path.
- **B:** Incorrect for this question. A private address reachable from the VPC without a proxy process. Why the correct answer wins: The authorized proxy supplies identity and encryption without a public path.
- **C:** Correct. A local proxy that authorizes the connection with IAM and encrypts it. In this case: The authorized proxy supplies identity and encryption without a public path.
- **D:** Incorrect for this question. A reachable address that requires encrypted connections from any client. Why the correct answer wins: The authorized proxy supplies identity and encryption without a public path.

### Question 81 — A, E

Answers: Pool and reuse database connections; Use the language connector with IAM. Pooling keeps the session count low, and the language connector authorizes the instance without a sidecar. Keep a small set of warm connections instead of opening one per request. A client library that resolves and authorizes the instance itself. Local study-map skill 4.1 (Connecting to Datastores), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 4 (integrating applications with Google Cloud services): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Correct. Keep a small set of warm connections instead of opening one per request. In this case: Pooling keeps the session count low, and the language connector authorizes the instance without a sidecar.
- **B:** Incorrect for this question. A long-lived credential that has to be stored and rotated by hand. Why the correct answer wins: Pooling keeps the session count low, and the language connector authorizes the instance without a sidecar.
- **C:** Incorrect for this question. A local proxy that authorizes the connection with IAM and encrypts it. Why the correct answer wins: Pooling keeps the session count low, and the language connector authorizes the instance without a sidecar.
- **D:** Incorrect for this question. A private address reachable from the VPC without a proxy process. Why the correct answer wins: Pooling keeps the session count low, and the language connector authorizes the instance without a sidecar.
- **E:** Correct. A client library that resolves and authorizes the instance itself. In this case: Pooling keeps the session count low, and the language connector authorizes the instance without a sidecar.

### Question 82 — B

Answer: Connect over the database private IP. A private address on the shared network avoids an extra hop. A private address reachable from the VPC without a proxy process. Local study-map skill 4.1 (Connecting to Datastores), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 4 (integrating applications with Google Cloud services): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A local proxy that authorizes the connection with IAM and encrypts it. Why the correct answer wins: A private address on the shared network avoids an extra hop.
- **B:** Correct. A private address reachable from the VPC without a proxy process. In this case: A private address on the shared network avoids an extra hop.
- **C:** Incorrect for this question. A reachable address that requires encrypted connections from any client. Why the correct answer wins: A private address on the shared network avoids an extra hop.
- **D:** Incorrect for this question. A client library that resolves and authorizes the instance itself. Why the correct answer wins: A private address on the shared network avoids an extra hop.

### Question 83 — C

Answer: Use Firestore in Native mode. A native document store supplies listeners and offline support with managed scaling. A document store with real-time listeners and mobile SDKs. Local study-map skill 4.1 (Connecting to Datastores), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 4 (integrating applications with Google Cloud services): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Order the key so the query becomes a contiguous range scan. Why the correct answer wins: A native document store supplies listeners and offline support with managed scaling.
- **B:** Incorrect for this question. A relational database with strongly consistent multi-region transactions. Why the correct answer wins: A native document store supplies listeners and offline support with managed scaling.
- **C:** Correct. A document store with real-time listeners and mobile SDKs. In this case: A native document store supplies listeners and offline support with managed scaling.
- **D:** Incorrect for this question. Durable object storage addressed by name rather than a database row. Why the correct answer wins: A native document store supplies listeners and offline support with managed scaling.

### Question 84 — A

Answer: Design the row key for the read pattern. Ordering the row key by device and time makes each read a contiguous range. Order the key so the query becomes a contiguous range scan. Local study-map skill 4.1 (Connecting to Datastores), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 4 (integrating applications with Google Cloud services): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Correct. Order the key so the query becomes a contiguous range scan. In this case: Ordering the row key by device and time makes each read a contiguous range.
- **B:** Incorrect for this question. A relational database with strongly consistent multi-region transactions. Why the correct answer wins: Ordering the row key by device and time makes each read a contiguous range.
- **C:** Incorrect for this question. A managed Redis-compatible cache in front of the system of record. Why the correct answer wins: Ordering the row key by device and time makes each read a contiguous range.
- **D:** Incorrect for this question. A document store with real-time listeners and mobile SDKs. Why the correct answer wins: Ordering the row key by device and time makes each read a contiguous range.

### Question 85 — A

Answer: Make the handler idempotent with a deduplication key. A deduplication key lets the handler ignore a repeated delivery. Recognise a repeated delivery and skip the duplicate work. Local study-map skill 4.2 (Publishing and Consuming Messages), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 4 (integrating applications with Google Cloud services): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Correct. Recognise a repeated delivery and skip the duplicate work. In this case: A deduplication key lets the handler ignore a repeated delivery.
- **B:** Incorrect for this question. A durable, at-least-once message channel with independent subscribers. Why the correct answer wins: A deduplication key lets the handler ignore a repeated delivery.
- **C:** Incorrect for this question. Hold messages that exhausted their delivery attempts for later inspection. Why the correct answer wins: A deduplication key lets the handler ignore a repeated delivery.
- **D:** Incorrect for this question. A task queue with retries and rate control aimed at a specific target. Why the correct answer wins: A deduplication key lets the handler ignore a repeated delivery.

### Question 86 — D

Answer: Use a BigQuery subscription on the topic. A warehouse subscription writes the topic messages straight into a table. Write topic messages straight into a table without a consumer. Local study-map skill 4.2 (Publishing and Consuming Messages), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 4 (integrating applications with Google Cloud services): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A task queue with retries and rate control aimed at a specific target. Why the correct answer wins: A warehouse subscription writes the topic messages straight into a table.
- **B:** Incorrect for this question. A durable, at-least-once message channel with independent subscribers. Why the correct answer wins: A warehouse subscription writes the topic messages straight into a table.
- **C:** Incorrect for this question. A trigger path that turns a Cloud Audit Log or resource event into a delivery. Why the correct answer wins: A warehouse subscription writes the topic messages straight into a table.
- **D:** Correct. Write topic messages straight into a table without a consumer. In this case: A warehouse subscription writes the topic messages straight into a table.

### Question 87 — A

Answer: Add a dead-letter topic. A dead-letter topic removes the message after its attempts so the backlog can advance. Hold messages that exhausted their delivery attempts for later inspection. Local study-map skill 4.2 (Publishing and Consuming Messages), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 4 (integrating applications with Google Cloud services): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Correct. Hold messages that exhausted their delivery attempts for later inspection. In this case: A dead-letter topic removes the message after its attempts so the backlog can advance.
- **B:** Incorrect for this question. The consumer controls the pace and acknowledges messages itself. Why the correct answer wins: A dead-letter topic removes the message after its attempts so the backlog can advance.
- **C:** Incorrect for this question. Push each message to an endpoint instead of having the consumer pull. Why the correct answer wins: A dead-letter topic removes the message after its attempts so the backlog can advance.
- **D:** Incorrect for this question. Recognise a repeated delivery and skip the duplicate work. Why the correct answer wins: A dead-letter topic removes the message after its attempts so the backlog can advance.

### Question 88 — A

Answer: Queue the work as a Cloud Tasks task. A task queue gives per-task retries and rate control against one target. A task queue with retries and rate control aimed at a specific target. Local study-map skill 4.2 (Publishing and Consuming Messages), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 4 (integrating applications with Google Cloud services): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Correct. A task queue with retries and rate control aimed at a specific target. In this case: A task queue gives per-task retries and rate control against one target.
- **B:** Incorrect for this question. A durable, at-least-once message channel with independent subscribers. Why the correct answer wins: A task queue gives per-task retries and rate control against one target.
- **C:** Incorrect for this question. A stateful sequence of service calls with retries and error branches. Why the correct answer wins: A task queue gives per-task retries and rate control against one target.
- **D:** Incorrect for this question. A cron-style trigger that calls a target on a fixed timetable. Why the correct answer wins: A task queue gives per-task retries and rate control against one target.

### Question 89 — B, C

Answers: Retry with exponential backoff and jitter; Cache the response for its freshness window. Caching the response removes the repeated identical call, and backoff with jitter survives the throttling that remains. Space out repeated attempts so a throttled quota can recover instead of being hammered. Reuse a result that has not changed, avoiding an identical call. Local study-map skill 4.3 (Calling Google Cloud APIs), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 4 (integrating applications with Google Cloud services): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Request each page in turn so a truncated response is completed rather than assumed whole. Why the correct answer wins: Caching the response removes the repeated identical call, and backoff with jitter survives the throttling that remains.
- **B:** Correct. Reuse a result that has not changed, avoiding an identical call. In this case: Caching the response removes the repeated identical call, and backoff with jitter survives the throttling that remains.
- **C:** Correct. Space out repeated attempts so a throttled quota can recover instead of being hammered. In this case: Caching the response removes the repeated identical call, and backoff with jitter survives the throttling that remains.
- **D:** Incorrect for this question. Trim the response payload so latency and cost follow actual use. Why the correct answer wins: Caching the response removes the repeated identical call, and backoff with jitter survives the throttling that remains.
- **E:** Incorrect for this question. Reduce per-call overhead when the API supports a batch surface. Why the correct answer wins: Caching the response removes the repeated identical call, and backoff with jitter survives the throttling that remains.

### Question 90 — D

Answer: Follow the page token until results are exhausted. Following the page token retrieves the remaining records. Request each page in turn so a truncated response is completed rather than assumed whole. Local study-map skill 4.3 (Calling Google Cloud APIs), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 4 (integrating applications with Google Cloud services): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Trim the response payload so latency and cost follow actual use. Why the correct answer wins: Following the page token retrieves the remaining records.
- **B:** Incorrect for this question. Reduce per-call overhead when the API supports a batch surface. Why the correct answer wins: Following the page token retrieves the remaining records.
- **C:** Incorrect for this question. Reuse a result that has not changed, avoiding an identical call. Why the correct answer wins: Following the page token retrieves the remaining records.
- **D:** Correct. Request each page in turn so a truncated response is completed rather than assumed whole. In this case: Following the page token retrieves the remaining records.

### Question 91 — B

Answer: Request only the fields the caller needs. Requesting only the needed fields shrinks the payload. Trim the response payload so latency and cost follow actual use. Local study-map skill 4.3 (Calling Google Cloud APIs), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 4 (integrating applications with Google Cloud services): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Request each page in turn so a truncated response is completed rather than assumed whole. Why the correct answer wins: Requesting only the needed fields shrinks the payload.
- **B:** Correct. Trim the response payload so latency and cost follow actual use. In this case: Requesting only the needed fields shrinks the payload.
- **C:** Incorrect for this question. Reduce per-call overhead when the API supports a batch surface. Why the correct answer wins: Requesting only the needed fields shrinks the payload.
- **D:** Incorrect for this question. Reuse a result that has not changed, avoiding an identical call. Why the correct answer wins: Requesting only the needed fields shrinks the payload.

### Question 92 — B

Answer: Give the workload its own service account. Its own service account supplies credentials without a stored key. A dedicated identity whose roles can be granted and revoked independently. Local study-map skill 4.3 (Calling Google Cloud APIs), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 4 (integrating applications with Google Cloud services): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Let anyone reach the endpoint, which is only appropriate for public content. Why the correct answer wins: Its own service account supplies credentials without a stored key.
- **B:** Correct. A dedicated identity whose roles can be granted and revoked independently. In this case: Its own service account supplies credentials without a stored key.
- **C:** Incorrect for this question. A long-lived credential that has to be stored and rotated by hand. Why the correct answer wins: Its own service account supplies credentials without a stored key.
- **D:** Incorrect for this question. Let the client library find credentials from the environment. Why the correct answer wins: Its own service account supplies credentials without a stored key.

### Question 93 — A

Answer: Grant only the roles the workload needs. Least privilege narrows the grant to the operations in use. Scope permissions to the actions in use rather than the whole service. Local study-map skill 4.4 (Service Accounts for API Calls), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 4 (integrating applications with Google Cloud services): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Correct. Scope permissions to the actions in use rather than the whole service. In this case: Least privilege narrows the grant to the operations in use.
- **B:** Incorrect for this question. A long-lived credential that has to be stored and rotated by hand. Why the correct answer wins: Least privilege narrows the grant to the operations in use.
- **C:** Incorrect for this question. Restrict which pods may talk to which pods inside the cluster. Why the correct answer wins: Least privilege narrows the grant to the operations in use.
- **D:** Incorrect for this question. A legacy broad role that can change most resources in the project. Why the correct answer wins: Least privilege narrows the grant to the operations in use.

### Question 94 — C

Answer: Bind a Kubernetes service account to a Google service account. Workload Identity issues short-lived credentials with nothing stored. Keyless credential issuance for pods through Workload Identity. Local study-map skill 4.4 (Service Accounts for API Calls), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 4 (integrating applications with Google Cloud services): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Let the client library find credentials from the environment. Why the correct answer wins: Workload Identity issues short-lived credentials with nothing stored.
- **B:** Incorrect for this question. Inject the value into the process environment at start-up. Why the correct answer wins: Workload Identity issues short-lived credentials with nothing stored.
- **C:** Correct. Keyless credential issuance for pods through Workload Identity. In this case: Workload Identity issues short-lived credentials with nothing stored.
- **D:** Incorrect for this question. A long-lived credential that has to be stored and rotated by hand. Why the correct answer wins: Workload Identity issues short-lived credentials with nothing stored.

### Question 95 — C

Answer: Emit structured JSON logs. Structured fields make the identifier a filterable dimension. Emit fields the log viewer can index so queries and alerts are possible. Local study-map skill 4.5 (Metrics, Logs, and Traces), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 4 (integrating applications with Google Cloud services): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Turn a recurring log pattern into a number that can be charted and alerted on. Why the correct answer wins: Structured fields make the identifier a filterable dimension.
- **B:** Incorrect for this question. Let filters and alerting distinguish routine output from errors. Why the correct answer wins: Structured fields make the identifier a filterable dimension.
- **C:** Correct. Emit fields the log viewer can index so queries and alerts are possible. In this case: Structured fields make the identifier a filterable dimension.
- **D:** Incorrect for this question. Group and count application errors instead of grepping logs. Why the correct answer wins: Structured fields make the identifier a filterable dimension.

### Question 96 — D

Answer: Instrument a span around the downstream call. A span around each downstream call attributes the time to a specific dependency. Show where time goes inside a request that crosses services. Local study-map skill 4.5 (Metrics, Logs, and Traces), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 4 (integrating applications with Google Cloud services): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Publish an application signal that infrastructure metrics cannot see. Why the correct answer wins: A span around each downstream call attributes the time to a specific dependency.
- **B:** Incorrect for this question. Group and count application errors instead of grepping logs. Why the correct answer wins: A span around each downstream call attributes the time to a specific dependency.
- **C:** Incorrect for this question. Join spans from different services into one trace. Why the correct answer wins: A span around each downstream call attributes the time to a specific dependency.
- **D:** Correct. Show where time goes inside a request that crosses services. In this case: A span around each downstream call attributes the time to a specific dependency.

### Question 97 — A

Answer: Set the correct severity on each entry. Correct severity lets filters and alerts tell routine output from failure. Let filters and alerting distinguish routine output from errors. Local study-map skill 4.5 (Metrics, Logs, and Traces), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 4 (integrating applications with Google Cloud services): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Correct. Let filters and alerting distinguish routine output from errors. In this case: Correct severity lets filters and alerts tell routine output from failure.
- **B:** Incorrect for this question. Turn a recurring log pattern into a number that can be charted and alerted on. Why the correct answer wins: Correct severity lets filters and alerts tell routine output from failure.
- **C:** Incorrect for this question. Emit fields the log viewer can index so queries and alerts are possible. Why the correct answer wins: Correct severity lets filters and alerts tell routine output from failure.
- **D:** Incorrect for this question. Group and count application errors instead of grepping logs. Why the correct answer wins: Correct severity lets filters and alerts tell routine output from failure.

### Question 98 — C

Answer: Send the exception to Error Reporting. Error grouping collapses the variants into counted distinct failures. Group and count application errors instead of grepping logs. Local study-map skill 4.6 (Error Reporting and Trace Correlation), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 4 (integrating applications with Google Cloud services): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Publish an application signal that infrastructure metrics cannot see. Why the correct answer wins: Error grouping collapses the variants into counted distinct failures.
- **B:** Incorrect for this question. Emit fields the log viewer can index so queries and alerts are possible. Why the correct answer wins: Error grouping collapses the variants into counted distinct failures.
- **C:** Correct. Group and count application errors instead of grepping logs. In this case: Error grouping collapses the variants into counted distinct failures.
- **D:** Incorrect for this question. Turn a recurring log pattern into a number that can be charted and alerted on. Why the correct answer wins: Error grouping collapses the variants into counted distinct failures.

### Question 99 — B

Answer: Propagate the trace ID between services. Propagating the trace identifier gives every entry a shared key. Join spans from different services into one trace. Local study-map skill 4.6 (Error Reporting and Trace Correlation), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 4 (integrating applications with Google Cloud services): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Publish an application signal that infrastructure metrics cannot see. Why the correct answer wins: Propagating the trace identifier gives every entry a shared key.
- **B:** Correct. Join spans from different services into one trace. In this case: Propagating the trace identifier gives every entry a shared key.
- **C:** Incorrect for this question. Find the function consuming CPU or memory under real traffic. Why the correct answer wins: Propagating the trace identifier gives every entry a shared key.
- **D:** Incorrect for this question. Show where time goes inside a request that crosses services. Why the correct answer wins: Propagating the trace identifier gives every entry a shared key.

### Question 100 — A

Answer: Ask Gemini Cloud Assist for a diagnosis. The cloud assistant summarises telemetry into a likely cause and a next step. An assistant that reads telemetry and proposes a cause and a next step. Local study-map skill 4.7 (AI-Assisted Observability), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 4 (integrating applications with Google Cloud services): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Correct. An assistant that reads telemetry and proposes a cause and a next step. In this case: The cloud assistant summarises telemetry into a likely cause and a next step.
- **B:** Incorrect for this question. Find the function consuming CPU or memory under real traffic. Why the correct answer wins: The cloud assistant summarises telemetry into a likely cause and a next step.
- **C:** Incorrect for this question. Give the assistant a defined tool surface instead of pasting context by hand. Why the correct answer wins: The cloud assistant summarises telemetry into a likely cause and a next step.
- **D:** Incorrect for this question. Generate a first draft from context, then review and correct it. Why the correct answer wins: The cloud assistant summarises telemetry into a likely cause and a next step.
