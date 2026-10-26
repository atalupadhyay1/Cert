# Google Cloud Professional Cloud Developer — Full-Length Mock Exam 5

Professional Cloud Developer · 100 questions · expanded practice bank · passing score not published

Blueprint-weighted mock exam. Item mix: 84 multiple-choice and 16 multiple-select items (the selection count is stated in each multi-select stem). The live exam publishes 50-60 multiple-choice and multiple-select questions and has no case-study component, so this set is larger on purpose and no case-study item is reproduced. The live paper allows two hours for 50-60 items, so this 100-item set is a slower-per-item rehearsal: about 72 seconds per item here against roughly 120-144 seconds live. Use it to build a habit of finishing with time to review. See the README for the exact fidelity boundary.

Original educational content, not actual, recalled, or copied Google exam items.

## Questions

---

## Domain 1 — Designing Highly Scalable, Secure, and Reliable Cloud-Native Applications (Compute Choice, APIs, and Secure Design)

### 1. A team has a Dockerfile and wants per-request billing without any cluster to patch. Which platform fits?

- A. Run the application on Compute Engine instances
- B. Deploy the service to Cloud Run
- C. Deploy to App Engine standard
- D. Deploy the handler as a Cloud Functions function

### 2. A servlet-era application should keep its platform services with the smallest possible change. Which platform fits?

- A. Deploy the handler as a Cloud Functions function
- B. Deploy to App Engine standard
- C. Run the application on Compute Engine instances
- D. Deploy the service to Cloud Run

### 3. A licensed desktop application must run on a Windows image with an attached data disk. Which platform fits?

- A. Deploy the workload to Google Kubernetes Engine
- B. Deploy to App Engine standard
- C. Run the application on Compute Engine instances
- D. Deploy the service to Cloud Run

### 4. A monolith already produces a container image and must move without a rewrite. What should the team ship?

- A. Deploy from source and let the platform build it
- B. Package the monolith into a container image
- C. Deploy the handler as a Cloud Functions function
- D. Deploy to App Engine standard

### 5. Three zones of one region meet the resilience target and the latency budget. Which design fits?

- A. Deploy the service in two regions behind a global load balancer
- B. Place the workload in a single zone
- C. Serve static content from Cloud CDN
- D. Deploy in one region across multiple zones

### 6. Traffic must move off a failing region automatically with no operator action. What provides that?

- A. Add a health check endpoint to the backend service
- B. Use a regional load balancer
- C. Put a global external Application Load Balancer in front
- D. Serve static content from Cloud CDN

### 7. A rolling deploy logs every user out because their tokens were held in instance memory. What must change?

- A. Enable session affinity on the backend service
- B. Use a generated cookie for stickiness
- C. Store session state in a shared datastore
- D. Cache inside each instance process

### 8. WebSocket connections are being reassigned mid-conversation by the balancer. What should be enabled?

- A. Enable session affinity on the backend service
- B. Use a generated cookie for stickiness
- C. Store session state in a shared datastore
- D. Put a global external Application Load Balancer in front

### 9. Two services need one shared cache, and a write must not leave a stale entry behind. Which two fit? Select two.

- A. Cache inside each instance process
- B. Invalidate the cache on write
- C. Load through a cache-aside pattern
- D. Cache reads in Memorystore
- E. Serve static content from Cloud CDN

### 10. The application itself must load a missing key and then populate the cache for later readers. Which pattern fits?

- A. Load through a cache-aside pattern
- B. Invalidate the cache on write
- C. Cache inside each instance process
- D. Serve static content from Cloud CDN

### 11. A public dataset interface must be readable with curl and cacheable by intermediary proxies. Which interface fits?

- A. Serve gRPC-Web for browser clients
- B. Expose a REST API with JSON payloads
- C. Publish an OpenAPI specification
- D. Expose a gRPC service

### 12. Two internal services exchange two hundred thousand messages a minute over multiplexed streams. Which interface fits?

- A. Publish an OpenAPI specification
- B. Expose a gRPC service
- C. Expose a REST API with JSON payloads
- D. Serve gRPC-Web for browser clients

### 13. One tenant is flooding the API, and every tenant must also be metered against a contracted allowance. Which two fit? Select two.

- A. Set a quota per API key
- B. Publish an OpenAPI specification
- C. Apply a rate limit per client key
- D. Introduce a new API version alongside the old one
- E. Add the field in a backward-compatible way

### 14. Consumers want generated client libraries from a single published contract. What should the team publish?

- A. Publish an OpenAPI specification
- B. Put Apigee in front of the API
- C. Use API Gateway for the API
- D. Expose a gRPC service

### 15. A new account must notify billing, onboarding and analytics without knowing who they are. What should be published to?

- A. Route the event with Eventarc
- B. Publish the event to a Pub/Sub topic
- C. Orchestrate the steps in Workflows
- D. Queue the work as a Cloud Tasks task

### 16. A finance report must be produced at two in the morning on the first of each month. What should run it?

- A. Queue the work as a Cloud Tasks task
- B. Orchestrate the steps in Workflows
- C. Schedule the invocation with Cloud Scheduler
- D. Route the event with Eventarc

### 17. A steady baseline will run unchanged for three years and should cost less per hour. What fits?

- A. Buy committed use discounts for the steady baseline
- B. Run the batch node pool on Spot VMs
- C. Set a namespace resource quota
- D. Set CPU and memory requests from measured use

### 18. One team's namespace must not consume more than its agreed share of the shared cluster. What enforces that?

- A. Set a namespace resource quota
- B. Set CPU and memory requests from measured use
- C. Constrain pods to the intended node pool
- D. Buy committed use discounts for the steady baseline

### 19. A release shows a regression and the previous revision must serve again within seconds. What should be used?

- A. Shift traffic back to the previous revision
- B. Gate the change behind a feature flag
- C. Split traffic between revisions by percentage
- D. Canary the release at a small percentage first

### 20. A new ranking model must first be judged on one percent of sessions before launch. Which approach fits?

- A. Shift traffic back to the previous revision
- B. Split traffic between revisions by percentage
- C. Route by revision tag or header
- D. Canary the release at a small percentage first

### 21. A long order process must retry one failed step, and a slow partner call must be offloaded with retries. Which two fit? Select two.

- A. Schedule the invocation with Cloud Scheduler
- B. Orchestrate the steps in Workflows
- C. Queue the work as a Cloud Tasks task
- D. Publish the event to a Pub/Sub topic
- E. Route the event with Eventarc

### 22. Records must stay undeletable for seven years, and temporary exports must vanish after thirty days. Which two fit? Select two.

- A. Use a customer-managed encryption key
- B. Make the bucket public
- C. Add a lifecycle rule to the bucket
- D. Issue a signed URL with a short expiry
- E. Lock the bucket retention policy

### 23. A database credential must change every ninety days without a redeploy. What should be configured?

- A. Mount the secret as a volume
- B. Set the credential as an environment variable
- C. Download a service account key file
- D. Rotate the secret on a schedule

### 24. Disk snapshots must be encrypted under a key the security team rotates on its own schedule. What should be used?

- A. Download a service account key file
- B. Use a customer-managed encryption key
- C. Store the credential in Secret Manager
- D. Encrypt with a Cloud KMS key

### 25. An internal console must be gated before the app sees the request, and the app must trust who the caller is. Which two fit? Select two.

- A. Use Identity Platform for end-user sign-in
- B. Give the workload its own service account
- C. Allow unauthenticated invocations
- D. Validate the signed JWT from the proxy
- E. Put Identity-Aware Proxy in front of the service

### 26. A game needs guest accounts that can later be upgraded and linked to a social sign-in. What should it adopt?

- A. Give the workload its own service account
- B. Validate the signed JWT from the proxy
- C. Use Identity Platform for end-user sign-in
- D. Rely on Application Default Credentials

### 27. No predefined role covers exactly the nine permissions a job needs. What should be created?

- A. Grant the basic editor role
- B. Give the workload its own service account
- C. Grant only the roles the workload needs
- D. Define a custom role for the narrow permission set

### 28. Service-to-service calls must be mutually authenticated and authorised without code changes. What should be introduced?

- A. Use Cloud Service Mesh for service-to-service traffic
- B. Grant only the roles the workload needs
- C. Put Identity-Aware Proxy in front of the service
- D. Apply a Kubernetes NetworkPolicy

### 29. Write latency climbs because every new row shares a sequential prefix. What should the key design avoid?

- A. Design the row key for the read pattern
- B. Use Firestore in Native mode
- C. Store the ledger in Spanner
- D. Hash the leading key component to avoid hotspots

### 30. A legacy platform application's entity queries must keep working after the move. Which mode fits?

- A. Use Firestore in Datastore mode
- B. Cache reads in Memorystore
- C. Use Firestore in Native mode
- D. Store the ledger in Spanner

### 31. A partner needs one file for ten minutes, and marketing assets must be readable by anyone. Which two fit? Select two.

- A. Issue a signed URL with a short expiry
- B. Add a lifecycle rule to the bucket
- C. Encrypt with a Cloud KMS key
- D. Lock the bucket retention policy
- E. Make the bucket public

### 32. A fraud model must score a transaction seconds after it happens. How should the events reach the table?

- A. Use a BigQuery subscription on the topic
- B. Stream the events into BigQuery
- C. Export the batch to BigQuery
- D. Store the objects in Cloud Storage

---

## Domain 2 — Building and Testing Applications (Development Environments, Builds, and Tests)

### 33. A race between two consumers must be reproduced during a flight with no project and no bill. What should be used?

- A. Use Cloud Shell for the session
- B. Use Cloud Workstations for the environment
- C. Run the service emulator locally
- D. Develop with Cloud Code in the IDE

### 34. A contractor's laptop cannot be trusted with source, so the code must never land on it. What should be provided?

- A. Run the service emulator locally
- B. Develop with Cloud Code in the IDE
- C. Use Cloud Shell for the session
- D. Use Cloud Workstations for the environment

### 35. An incident responder needs a shell with the SDK from a borrowed machine. What fits?

- A. Run the service emulator locally
- B. Use Cloud Workstations for the environment
- C. Use Cloud Shell for the session
- D. Develop with Cloud Code in the IDE

### 36. A developer investigating a production failure wants the logs explained and the tracker queried by the assistant itself. Which two fit? Select two.

- A. Use Cloud Shell for the session
- B. Ask Gemini Cloud Assist for a diagnosis
- C. Develop with Cloud Code in the IDE
- D. Use an AI coding assistant to draft the tests
- E. Connect the assistant to an MCP server

### 37. A schema change must produce a draft migration script for a human to correct. What should be used?

- A. Develop with Cloud Code in the IDE
- B. Ask Gemini Cloud Assist for a diagnosis
- C. Connect the assistant to an MCP server
- D. Use an AI coding assistant to draft the tests

### 38. A defect only appears with the production data set, and breakpoints are needed inside a hosted editor. What fits?

- A. Inspect the live process with Cloud Debugger
- B. Develop with Cloud Code in the IDE
- C. Use Cloud Workstations for the environment
- D. Use Cloud Shell for the session

### 39. A build must behave identically on an engineer's machine and in the pipeline. What should it be?

- A. Build the image with Cloud Build
- B. Keep building the image by hand
- C. Iterate with Skaffold
- D. Deploy a pinned image digest

### 40. A release tag must produce a build automatically with no one starting it. What should be configured?

- A. Keep building the image by hand
- B. Trigger the build from a repository push
- C. Queue the work as a Cloud Tasks task
- D. Schedule the invocation with Cloud Scheduler

### 41. A private base layer must be combined with the application in a Dockerfile the team controls. What should the pipeline do?

- A. Package the monolith into a container image
- B. Keep building the image by hand
- C. Deploy from source and let the platform build it
- D. Iterate with Skaffold

### 42. The build output must be pushed to a repository the runtime can pull from with only its own identity. What should hold it?

- A. Push the image to Artifact Registry
- B. Store the objects in Cloud Storage
- C. Push the image to Container Registry
- D. Build the image with Cloud Build

### 43. Each environment needs its own image repository, and signed release notes must be kept with the version. Which two fit? Select two.

- A. Push the image to Artifact Registry
- B. Use a customer-managed encryption key
- C. Store the objects in Cloud Storage
- D. Push the image to Container Registry
- E. Build the image with Cloud Build

### 44. Some older automation still pushes to the legacy host name and must keep working. What must stay enabled?

- A. Store the objects in Cloud Storage
- B. Push the image to Artifact Registry
- C. Push the image to Container Registry
- D. Build the image with Cloud Build

### 45. Stored images must be encrypted under a key the security team controls and can revoke. What should be configured?

- A. Push the image to Artifact Registry
- B. Store the objects in Cloud Storage
- C. Build the image with Cloud Build
- D. Use a customer-managed encryption key

### 46. Images must be scanned for known vulnerabilities, and unsigned images must never start in production. Which two fit? Select two.

- A. Review the finding in Security Command Center
- B. Generate build provenance in Cloud Build
- C. Enforce admission with Binary Authorization
- D. Scan the image with Artifact Analysis
- E. Require a higher supply-chain level before release

### 47. Security must pick the level where the build platform itself is hardened and its provenance cannot be forged. What should they require?

- A. Enforce admission with Binary Authorization
- B. Generate build provenance in Cloud Build
- C. Require a higher supply-chain level before release
- D. Scan the image with Artifact Analysis

### 48. An incident review must establish whether a running image came from the reviewed branch or a hotfix. What answers it?

- A. Scan the image with Artifact Analysis
- B. Require a higher supply-chain level before release
- C. Generate build provenance in Cloud Build
- D. Enforce admission with Binary Authorization

### 49. Feedback must arrive in seconds and must run on every change without being remembered. Which two fit? Select two.

- A. Add a unit test with dependencies stubbed
- B. Run the tests as a Cloud Build step
- C. Block the deploy on the test result
- D. Quarantine the flaky test and fix it
- E. Load-test the release before the rollout

### 50. A test reads the wall clock and fails only after midnight. What should be done first?

- A. Quarantine the flaky test and fix it
- B. Block the deploy on the test result
- C. Add a unit test with dependencies stubbed
- D. Run an integration test against the emulator

### 51. A red suite is being merged over because nobody treats it as blocking. What should be added?

- A. Load-test the release before the rollout
- B. Block the deploy on the test result
- C. Run an integration test against the emulator
- D. Quarantine the flaky test and fix it

### 52. A consumer's deserialisation breaks only against the producer's real output. Which test would catch it?

- A. Inspect the live process with Cloud Debugger
- B. Load-test the release before the rollout
- C. Add a unit test with dependencies stubbed
- D. Run an integration test against the emulator

### 53. A release must hold its tail latency at ten times today's volume. What should be run?

- A. Add a unit test with dependencies stubbed
- B. Profile the service with Cloud Profiler
- C. Load-test the release before the rollout
- D. Run an integration test against the emulator

### 54. A realistic replay shows the service slow, and the team needs the hottest allocation site. What should be used?

- A. Load-test the release before the rollout
- B. Inspect the live process with Cloud Debugger
- C. Send the exception to Error Reporting
- D. Profile the service with Cloud Profiler

### 55. A failing end-to-end run must let an engineer inspect state halfway through the flow. What should be used?

- A. Profile the service with Cloud Profiler
- B. Add a unit test with dependencies stubbed
- C. Inspect the live process with Cloud Debugger
- D. Run an integration test against the emulator

---

## Domain 3 — Configuring Cloud-Native Applications for Deployment (Cloud Run and GKE Deployment Configuration)

### 56. An engineer wants to stop maintaining three hundred lines of Dockerfile and let the platform build the app. What should be used?

- A. Iterate with Skaffold
- B. Deploy from source and let the platform build it
- C. Keep building the image by hand
- D. Package the monolith into a container image

### 57. The first requests after each quiet hour take four seconds. What should be configured?

- A. Use request-based billing
- B. Cap the maximum instance count
- C. Raise CPU during start-up only
- D. Keep a minimum number of instances warm

### 58. A service compiles templates at boot and misses its health window every time. What should be enabled?

- A. Keep a minimum number of instances warm
- B. Raise the per-instance concurrency limit
- C. Raise CPU during start-up only
- D. Use request-based billing

### 59. A transcoder must process a batch of files, exit with a status and cost nothing until the next batch. What fits?

- A. Route the event with Eventarc
- B. Run the batch work as a Cloud Run job
- C. Deploy the service to Cloud Run
- D. Deploy the handler as a Cloud Functions function

### 60. A bucket change must start a receiver, and the receiver currently rejects the delivery as unauthorised. Which two fit? Select two.

- A. Orchestrate the steps in Workflows
- B. Schedule the invocation with Cloud Scheduler
- C. Deliver to an HTTPS push subscription
- D. Route the event with Eventarc
- E. Grant the invoker role to the calling identity

### 61. A callback must arrive at a specific future time and must not be delivered twice for the same order. What should be used?

- A. Queue the work as a Cloud Tasks task
- B. Schedule the invocation with Cloud Scheduler
- C. Publish the event to a Pub/Sub topic
- D. Route the event with Eventarc

### 62. A cache warm-up must run every hour on the hour. What should trigger it?

- A. Queue the work as a Cloud Tasks task
- B. Schedule the invocation with Cloud Scheduler
- C. Route the event with Eventarc
- D. Orchestrate the steps in Workflows

### 63. A dev environment must cost nothing while nobody calls it. Which billing behaviour fits?

- A. Use request-based billing
- B. Buy committed use discounts for the steady baseline
- C. Use instance-based billing
- D. Keep a minimum number of instances warm

### 64. A staging service must not answer calls from the public DNS name at all. What should be set?

- A. Put Identity-Aware Proxy in front of the service
- B. Put a global external Application Load Balancer in front
- C. Allow unauthenticated invocations
- D. Restrict ingress to internal traffic

### 65. A partner's webhook cannot present a Google token and must still reach the receiver. What should be allowed?

- A. Restrict ingress to internal traffic
- B. Grant the invoker role to the calling identity
- C. Allow unauthenticated invocations
- D. Put Identity-Aware Proxy in front of the service

### 66. Each instance can hold only so many concurrent requests before memory pressure appears. What should be tuned?

- A. Enable CPU boost at startup
- B. Keep a minimum number of instances warm
- C. Raise the per-instance concurrency limit
- D. Cap the maximum instance count

### 67. Internal APIs need quick key checks, and a partner programme needs plans, quotas and a portal. Which two fit? Select two.

- A. Introduce a new API version alongside the old one
- B. Put Apigee in front of the API
- C. Put a global external Application Load Balancer in front
- D. Use API Gateway for the API
- E. Restrict ingress to internal traffic

### 68. A release must replace pods in batches and never fall below the quorum of replicas. Which two fit? Select two.

- A. Add a PodDisruptionBudget
- B. Constrain pods to the intended node pool
- C. Use a rolling update strategy
- D. Tune maxSurge and maxUnavailable
- E. Run the batch node pool on Spot VMs

### 69. Pods must be placed on nodes in the same zone as the cache they read. What should be configured?

- A. Enable node pool autoscaling
- B. Add a PodDisruptionBudget
- C. Constrain pods to the intended node pool
- D. Run the batch node pool on Spot VMs

### 70. A batch pool may lose up to a fifth of its pods during a release but no more. What should be set?

- A. Enable node pool autoscaling
- B. Add a PodDisruptionBudget
- C. Tune maxSurge and maxUnavailable
- D. Use a rolling update strategy

### 71. A container needs ninety seconds to load a model and is being killed before it finishes. What should be added?

- A. Configure a readiness probe
- B. Add a PodDisruptionBudget
- C. Configure a liveness probe
- D. Configure a startup probe

### 72. A pod keeps receiving requests while its dependency check still fails. What should gate traffic?

- A. Configure a liveness probe
- B. Configure a startup probe
- C. Add a PodDisruptionBudget
- D. Configure a readiness probe

### 73. Draining a node for maintenance must leave at least three of five replicas running. What should be defined?

- A. Tune maxSurge and maxUnavailable
- B. Configure a readiness probe
- C. Add a health check endpoint to the backend service
- D. Add a PodDisruptionBudget

### 74. Pods must scale on utilisation, and the nodes to hold them must be added automatically. Which two fit? Select two.

- A. Enable node pool autoscaling
- B. Scale pods on a custom or external metric
- C. Scale pods on CPU utilization
- D. Set a minimum replica count
- E. Add a PodDisruptionBudget

### 75. A nightly burst at six must find two pods already running. What should be set?

- A. Enable node pool autoscaling
- B. Add a PodDisruptionBudget
- C. Scale pods on a custom or external metric
- D. Set a minimum replica count

### 76. Load is measured by open websocket connections rather than by CPU. What should the autoscaler follow?

- A. Enable node pool autoscaling
- B. Scale pods on a custom or external metric
- C. Buy committed use discounts for the steady baseline
- D. Scale pods on CPU utilization

### 77. A small event handler must run without anyone building or storing a container. What fits?

- A. Deploy the service to Cloud Run
- B. Run the application on Compute Engine instances
- C. Deploy the workload to Google Kubernetes Engine
- D. Deploy the handler as a Cloud Functions function

### 78. An old version must be retired after its consumers have moved. What makes that possible?

- A. Introduce a new API version alongside the old one
- B. Publish an OpenAPI specification
- C. Put Apigee in front of the API
- D. Add the field in a backward-compatible way

### 79. Only workers that checkpoint may be placed on preemptible nodes. What should host them?

- A. Run the batch node pool on Spot VMs
- B. Enable node pool autoscaling
- C. Add a PodDisruptionBudget
- D. Constrain pods to the intended node pool

---

## Domain 4 — Integrating Applications with Google Cloud Services (Data, Messaging, APIs, and Observability)

### 80. A service written in a language without a client connector must still reach the instance privately. What should be deployed?

- A. Connect through the Cloud SQL Auth Proxy
- B. Use the language connector with IAM
- C. Reach the service through Private Service Connect
- D. Connect through the AlloyDB Auth Proxy

### 81. Scaling to forty instances would multiply database sessions beyond what the instance allows. What should be added?

- A. Reach the service through Private Service Connect
- B. Raise the container limits above the observed peak
- C. Raise the database connection ceiling by flag
- D. Pool and reuse database connections

### 82. Certificate rotation on the cluster must not force clients to restart. What handles that?

- A. Use the language connector with IAM
- B. Reach the service through Private Service Connect
- C. Connect through the AlloyDB Auth Proxy
- D. Connect through the Cloud SQL Auth Proxy

### 83. Even administrators must reach the database from inside the network only. What should the instance use?

- A. Expose the database on a public address with enforced SSL
- B. Connect over the database private IP
- C. Reach the service through Private Service Connect
- D. Use the language connector with IAM

### 84. Each task must be limited to ten sessions so one can never monopolise the instance. What should be set?

- A. Raise the container limits above the observed peak
- B. Raise the database connection ceiling by flag
- C. Pool and reuse database connections
- D. Reach the service through Private Service Connect

### 85. The consumer must slow down whenever the downstream starts queueing. Which delivery fits?

- A. Queue the work as a Cloud Tasks task
- B. Deliver to an HTTPS push subscription
- C. Have the worker pull from the subscription
- D. Route the event with Eventarc

### 86. The subscription itself must retry delivery to an HTTPS endpoint that sometimes fails. Which delivery fits?

- A. Queue the work as a Cloud Tasks task
- B. Deliver to an HTTPS push subscription
- C. Route the event with Eventarc
- D. Have the worker pull from the subscription

### 87. Messages that fail ten times must be parked where engineers can inspect them later. What should be configured?

- A. Retry with exponential backoff and jitter
- B. Lock the bucket retention policy
- C. Add a dead-letter topic
- D. Make the handler idempotent with a deduplication key

### 88. One invoice event must reach tax, ledger and mail without the publisher knowing them. What should it publish to?

- A. Publish the event to a Pub/Sub topic
- B. Queue the work as a Cloud Tasks task
- C. Route the event with Eventarc
- D. Orchestrate the steps in Workflows

### 89. A client gives up on the first throttle, and another stops at the first page of results. Which two habits are missing? Select two.

- A. Cache the response for its freshness window
- B. Batch many small calls into one request
- C. Follow the page token until results are exhausted
- D. Retry with exponential backoff and jitter
- E. Request only the fields the caller needs

### 90. Two hundred small lookups per page load must become a handful of calls. What should the client do?

- A. Follow the page token until results are exhausted
- B. Request only the fields the caller needs
- C. Cache the response for its freshness window
- D. Batch many small calls into one request

### 91. The interface needs two fields but each response carries the whole object graph. What should the client request?

- A. Follow the page token until results are exhausted
- B. Request only the fields the caller needs
- C. Batch many small calls into one request
- D. Cache the response for its freshness window

### 92. Six jobs share the default identity, so nobody can tell which job revoked access. What should each job have?

- A. Give the workload its own service account
- B. Let the workload use the default compute service account
- C. Grant the basic editor role
- D. Define a custom role for the narrow permission set

### 93. An OIDC issuer outside Google Cloud must be exchanged for short-lived access. What should be configured?

- A. Download a service account key file
- B. Give the workload its own service account
- C. Federate the external identity with Workload Identity Federation
- D. Rely on Application Default Credentials

### 94. A checkout completion ratio must be charted although nothing emits it today. What should the team add?

- A. Set the correct severity on each entry
- B. Emit a custom metric from the code
- C. Build a log-based metric
- D. Create an alerting policy on the metric

### 95. Entries must be searchable by request id and by user id. What should the code emit?

- A. Build a log-based metric
- B. Emit structured JSON logs
- C. Set the correct severity on each entry
- D. Send the exception to Error Reporting

### 96. Paging should follow the error budget rather than individual host thresholds. What should be configured?

- A. Alert on the error budget burn rate
- B. Create an alerting policy on the metric
- C. Emit a custom metric from the code
- D. Set the correct severity on each entry

### 97. New exception groups must be spotted quickly, and one request's logs must be joinable across services. Which two fit? Select two.

- A. Propagate the trace ID between services
- B. Set the correct severity on each entry
- C. Send the exception to Error Reporting
- D. Create an alerting policy on the metric
- E. Instrument a span around the downstream call

### 98. Each downstream call's share of one request's latency must be visible. What should the code emit?

- A. Build a log-based metric
- B. Create an alerting policy on the metric
- C. Propagate the trace ID between services
- D. Instrument a span around the downstream call

### 99. A noisy alert needs a quick explanation and a suggested query for the on-call engineer. What should assist?

- A. Connect the assistant to an MCP server
- B. Send the exception to Error Reporting
- C. Ask Gemini Cloud Assist for a diagnosis
- D. Use an AI coding assistant to draft the tests

### 100. Reference data that changes hourly is fetched again on every single call. What should the client do?

- A. Batch many small calls into one request
- B. Cache the response for its freshness window
- C. Follow the page token until results are exhausted
- D. Request only the fields the caller needs

---

## Answer key and explanations

### Question 1 — B

Answer: Deploy the service to Cloud Run. A managed container runtime bills per request and patches nothing. A managed container runtime that scales to zero and bills per request while it serves traffic. Local study-map skill 1.1 (Compute Platform Selection), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 1 (designing highly scalable, secure, and reliable cloud-native applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Virtual machines where the operating system, runtime and scaling group are all managed by the team. Why the correct answer wins: A managed container runtime bills per request and patches nothing.
- **B:** Correct. A managed container runtime that scales to zero and bills per request while it serves traffic. In this case: A managed container runtime bills per request and patches nothing.
- **C:** Incorrect for this question. A platform runtime that manages scaling for a supported language version and its sandbox limits. Why the correct answer wins: A managed container runtime bills per request and patches nothing.
- **D:** Incorrect for this question. An event-triggered function runtime for a single-purpose handler rather than a long-lived service. Why the correct answer wins: A managed container runtime bills per request and patches nothing.

### Question 2 — B

Answer: Deploy to App Engine standard. The platform runtime keeps the servlet-era services the application already uses. A platform runtime that manages scaling for a supported language version and its sandbox limits. Local study-map skill 1.1 (Compute Platform Selection), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 1 (designing highly scalable, secure, and reliable cloud-native applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. An event-triggered function runtime for a single-purpose handler rather than a long-lived service. Why the correct answer wins: The platform runtime keeps the servlet-era services the application already uses.
- **B:** Correct. A platform runtime that manages scaling for a supported language version and its sandbox limits. In this case: The platform runtime keeps the servlet-era services the application already uses.
- **C:** Incorrect for this question. Virtual machines where the operating system, runtime and scaling group are all managed by the team. Why the correct answer wins: The platform runtime keeps the servlet-era services the application already uses.
- **D:** Incorrect for this question. A managed container runtime that scales to zero and bills per request while it serves traffic. Why the correct answer wins: The platform runtime keeps the servlet-era services the application already uses.

### Question 3 — C

Answer: Run the application on Compute Engine instances. Virtual machines give the Windows image and the attached disk. Virtual machines where the operating system, runtime and scaling group are all managed by the team. Local study-map skill 1.1 (Compute Platform Selection), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 1 (designing highly scalable, secure, and reliable cloud-native applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A managed Kubernetes control plane where pods, node pools and cluster-scoped policy are yours to configure. Why the correct answer wins: Virtual machines give the Windows image and the attached disk.
- **B:** Incorrect for this question. A platform runtime that manages scaling for a supported language version and its sandbox limits. Why the correct answer wins: Virtual machines give the Windows image and the attached disk.
- **C:** Correct. Virtual machines where the operating system, runtime and scaling group are all managed by the team. In this case: Virtual machines give the Windows image and the attached disk.
- **D:** Incorrect for this question. A managed container runtime that scales to zero and bills per request while it serves traffic. Why the correct answer wins: Virtual machines give the Windows image and the attached disk.

### Question 4 — B

Answer: Package the monolith into a container image. Shipping the existing image moves the monolith without rewriting it. Wrap the existing process in a portable artifact that a managed runtime can execute. Local study-map skill 1.2 (Containerizing and Refactoring Applications), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 1 (designing highly scalable, secure, and reliable cloud-native applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Hand the source to the managed builder instead of shipping an image. Why the correct answer wins: Shipping the existing image moves the monolith without rewriting it.
- **B:** Correct. Wrap the existing process in a portable artifact that a managed runtime can execute. In this case: Shipping the existing image moves the monolith without rewriting it.
- **C:** Incorrect for this question. An event-triggered function runtime for a single-purpose handler rather than a long-lived service. Why the correct answer wins: Shipping the existing image moves the monolith without rewriting it.
- **D:** Incorrect for this question. A platform runtime that manages scaling for a supported language version and its sandbox limits. Why the correct answer wins: Shipping the existing image moves the monolith without rewriting it.

### Question 5 — D

Answer: Deploy in one region across multiple zones. Zones of a single region meet the target without a second region. Spread instances over zones of a single region so a zone failure does not stop the service. Local study-map skill 1.3 (Regional Distribution and Failover), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 1 (designing highly scalable, secure, and reliable cloud-native applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Serve from two regions so a regional failure leaves capacity elsewhere. Why the correct answer wins: Zones of a single region meet the target without a second region.
- **B:** Incorrect for this question. Run in one zone only, so a zone failure stops the service entirely. Why the correct answer wins: Zones of a single region meet the target without a second region.
- **C:** Incorrect for this question. Cache responses at the edge so repeated requests never reach the origin. Why the correct answer wins: Zones of a single region meet the target without a second region.
- **D:** Correct. Spread instances over zones of a single region so a zone failure does not stop the service. In this case: Zones of a single region meet the target without a second region.

### Question 6 — A

Answer: Add a health check endpoint to the backend service. A health-checked front end diverts traffic when a region fails its checks. Let the load balancer stop sending traffic to an unhealthy instance. Local study-map skill 1.3 (Regional Distribution and Failover), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 1 (designing highly scalable, secure, and reliable cloud-native applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Correct. Let the load balancer stop sending traffic to an unhealthy instance. In this case: A health-checked front end diverts traffic when a region fails its checks.
- **B:** Incorrect for this question. A load balancer scoped to one region with a regional address. Why the correct answer wins: A health-checked front end diverts traffic when a region fails its checks.
- **C:** Incorrect for this question. A single anycast address that routes to the nearest healthy backend. Why the correct answer wins: A health-checked front end diverts traffic when a region fails its checks.
- **D:** Incorrect for this question. Cache responses at the edge so repeated requests never reach the origin. Why the correct answer wins: A health-checked front end diverts traffic when a region fails its checks.

### Question 7 — C

Answer: Store session state in a shared datastore. Moving the tokens out of the instance keeps users signed in across deploys. Move the state out of the instance so any instance can serve any request. Local study-map skill 1.4 (Load Balancing and Session Affinity), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 1 (designing highly scalable, secure, and reliable cloud-native applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Pin a client to one backend for the life of its session. Why the correct answer wins: Moving the tokens out of the instance keeps users signed in across deploys.
- **B:** Incorrect for this question. Route the client by cookie rather than by address or header. Why the correct answer wins: Moving the tokens out of the instance keeps users signed in across deploys.
- **C:** Correct. Move the state out of the instance so any instance can serve any request. In this case: Moving the tokens out of the instance keeps users signed in across deploys.
- **D:** Incorrect for this question. A per-instance cache that is fast but not shared between instances. Why the correct answer wins: Moving the tokens out of the instance keeps users signed in across deploys.

### Question 8 — A

Answer: Enable session affinity on the backend service. Affinity keeps each open connection on its backend. Pin a client to one backend for the life of its session. Local study-map skill 1.4 (Load Balancing and Session Affinity), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 1 (designing highly scalable, secure, and reliable cloud-native applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Correct. Pin a client to one backend for the life of its session. In this case: Affinity keeps each open connection on its backend.
- **B:** Incorrect for this question. Route the client by cookie rather than by address or header. Why the correct answer wins: Affinity keeps each open connection on its backend.
- **C:** Incorrect for this question. Move the state out of the instance so any instance can serve any request. Why the correct answer wins: Affinity keeps each open connection on its backend.
- **D:** Incorrect for this question. A single anycast address that routes to the nearest healthy backend. Why the correct answer wins: Affinity keeps each open connection on its backend.

### Question 9 — B, D

Answers: Cache reads in Memorystore; Invalidate the cache on write. A shared in-memory service serves both services, and invalidating on write removes the stale entry. A managed Redis-compatible cache in front of the system of record. Remove or refresh the cached value so readers do not see stale data. Local study-map skill 1.5 (Caching with Memorystore), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 1 (designing highly scalable, secure, and reliable cloud-native applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A per-instance cache that is fast but not shared between instances. Why the correct answer wins: A shared in-memory service serves both services, and invalidating on write removes the stale entry.
- **B:** Correct. Remove or refresh the cached value so readers do not see stale data. In this case: A shared in-memory service serves both services, and invalidating on write removes the stale entry.
- **C:** Incorrect for this question. Read the cache, fall back to the database, and populate the cache on a miss. Why the correct answer wins: A shared in-memory service serves both services, and invalidating on write removes the stale entry.
- **D:** Correct. A managed Redis-compatible cache in front of the system of record. In this case: A shared in-memory service serves both services, and invalidating on write removes the stale entry.
- **E:** Incorrect for this question. Cache responses at the edge so repeated requests never reach the origin. Why the correct answer wins: A shared in-memory service serves both services, and invalidating on write removes the stale entry.

### Question 10 — A

Answer: Load through a cache-aside pattern. The aside pattern loads on a miss and writes the value back. Read the cache, fall back to the database, and populate the cache on a miss. Local study-map skill 1.5 (Caching with Memorystore), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 1 (designing highly scalable, secure, and reliable cloud-native applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Correct. Read the cache, fall back to the database, and populate the cache on a miss. In this case: The aside pattern loads on a miss and writes the value back.
- **B:** Incorrect for this question. Remove or refresh the cached value so readers do not see stale data. Why the correct answer wins: The aside pattern loads on a miss and writes the value back.
- **C:** Incorrect for this question. A per-instance cache that is fast but not shared between instances. Why the correct answer wins: The aside pattern loads on a miss and writes the value back.
- **D:** Incorrect for this question. Cache responses at the edge so repeated requests never reach the origin. Why the correct answer wins: The aside pattern loads on a miss and writes the value back.

### Question 11 — B

Answer: Expose a REST API with JSON payloads. A resource-oriented HTTP interface is what proxies and curl handle natively. A resource-oriented HTTP interface that browsers and simple clients can call. Local study-map skill 1.6 (API Protocol Choice: REST and gRPC), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 1 (designing highly scalable, secure, and reliable cloud-native applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A compatibility layer so browser code can call a gRPC service. Why the correct answer wins: A resource-oriented HTTP interface is what proxies and curl handle natively.
- **B:** Correct. A resource-oriented HTTP interface that browsers and simple clients can call. In this case: A resource-oriented HTTP interface is what proxies and curl handle natively.
- **C:** Incorrect for this question. A machine-readable contract that generates clients and validates requests. Why the correct answer wins: A resource-oriented HTTP interface is what proxies and curl handle natively.
- **D:** Incorrect for this question. A binary, schema-driven RPC interface with streaming and generated clients. Why the correct answer wins: A resource-oriented HTTP interface is what proxies and curl handle natively.

### Question 12 — B

Answer: Expose a gRPC service. A binary RPC interface multiplexes streams efficiently at that rate. A binary, schema-driven RPC interface with streaming and generated clients. Local study-map skill 1.6 (API Protocol Choice: REST and gRPC), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 1 (designing highly scalable, secure, and reliable cloud-native applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A machine-readable contract that generates clients and validates requests. Why the correct answer wins: A binary RPC interface multiplexes streams efficiently at that rate.
- **B:** Correct. A binary, schema-driven RPC interface with streaming and generated clients. In this case: A binary RPC interface multiplexes streams efficiently at that rate.
- **C:** Incorrect for this question. A resource-oriented HTTP interface that browsers and simple clients can call. Why the correct answer wins: A binary RPC interface multiplexes streams efficiently at that rate.
- **D:** Incorrect for this question. A compatibility layer so browser code can call a gRPC service. Why the correct answer wins: A binary RPC interface multiplexes streams efficiently at that rate.

### Question 13 — A, C

Answers: Apply a rate limit per client key; Set a quota per API key. A rate limit stops the flood, and a per-key allowance meters each contract. Reject or queue requests above a threshold so one client cannot exhaust the service. Bound how many calls a plan allows in a window. Local study-map skill 1.7 (API Management, Rate Limiting, and Versioning), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 1 (designing highly scalable, secure, and reliable cloud-native applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Correct. Bound how many calls a plan allows in a window. In this case: A rate limit stops the flood, and a per-key allowance meters each contract.
- **B:** Incorrect for this question. A machine-readable contract that generates clients and validates requests. Why the correct answer wins: A rate limit stops the flood, and a per-key allowance meters each contract.
- **C:** Correct. Reject or queue requests above a threshold so one client cannot exhaust the service. In this case: A rate limit stops the flood, and a per-key allowance meters each contract.
- **D:** Incorrect for this question. Keep the old contract working while the new one is adopted. Why the correct answer wins: A rate limit stops the flood, and a per-key allowance meters each contract.
- **E:** Incorrect for this question. Extend the contract so existing clients keep working unchanged. Why the correct answer wins: A rate limit stops the flood, and a per-key allowance meters each contract.

### Question 14 — A

Answer: Publish an OpenAPI specification. Publishing the specification lets each consumer generate its client. A machine-readable contract that generates clients and validates requests. Local study-map skill 1.7 (API Management, Rate Limiting, and Versioning), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 1 (designing highly scalable, secure, and reliable cloud-native applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Correct. A machine-readable contract that generates clients and validates requests. In this case: Publishing the specification lets each consumer generate its client.
- **B:** Incorrect for this question. An API management layer for quotas, keys, mediation and analytics. Why the correct answer wins: Publishing the specification lets each consumer generate its client.
- **C:** Incorrect for this question. A lighter managed gateway for routing and key-based quota enforcement. Why the correct answer wins: Publishing the specification lets each consumer generate its client.
- **D:** Incorrect for this question. A binary, schema-driven RPC interface with streaming and generated clients. Why the correct answer wins: Publishing the specification lets each consumer generate its client.

### Question 15 — B

Answer: Publish the event to a Pub/Sub topic. A topic delivers the event to each subscriber without the publisher listing them. A durable, at-least-once message channel with independent subscribers. Local study-map skill 1.8 (Asynchronous and Event-Driven Integration), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 1 (designing highly scalable, secure, and reliable cloud-native applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A trigger path that turns a Cloud Audit Log or resource event into a delivery. Why the correct answer wins: A topic delivers the event to each subscriber without the publisher listing them.
- **B:** Correct. A durable, at-least-once message channel with independent subscribers. In this case: A topic delivers the event to each subscriber without the publisher listing them.
- **C:** Incorrect for this question. A stateful sequence of service calls with retries and error branches. Why the correct answer wins: A topic delivers the event to each subscriber without the publisher listing them.
- **D:** Incorrect for this question. A task queue with retries and rate control aimed at a specific target. Why the correct answer wins: A topic delivers the event to each subscriber without the publisher listing them.

### Question 16 — C

Answer: Schedule the invocation with Cloud Scheduler. A scheduled job starts the run on the declared calendar. A cron-style trigger that calls a target on a fixed timetable. Local study-map skill 1.8 (Asynchronous and Event-Driven Integration), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 1 (designing highly scalable, secure, and reliable cloud-native applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A task queue with retries and rate control aimed at a specific target. Why the correct answer wins: A scheduled job starts the run on the declared calendar.
- **B:** Incorrect for this question. A stateful sequence of service calls with retries and error branches. Why the correct answer wins: A scheduled job starts the run on the declared calendar.
- **C:** Correct. A cron-style trigger that calls a target on a fixed timetable. In this case: A scheduled job starts the run on the declared calendar.
- **D:** Incorrect for this question. A trigger path that turns a Cloud Audit Log or resource event into a delivery. Why the correct answer wins: A scheduled job starts the run on the declared calendar.

### Question 17 — A

Answer: Buy committed use discounts for the steady baseline. A commitment discounts capacity the team already knows it will use. Trade a term commitment for a lower unit price on capacity that never idles. Local study-map skill 1.9 (Resource Requirements and Cost Optimization), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 1 (designing highly scalable, secure, and reliable cloud-native applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Correct. Trade a term commitment for a lower unit price on capacity that never idles. In this case: A commitment discounts capacity the team already knows it will use.
- **B:** Incorrect for this question. Use reclaimable capacity for work that can tolerate a node disappearing. Why the correct answer wins: A commitment discounts capacity the team already knows it will use.
- **C:** Incorrect for this question. Bound the total capacity a namespace may consume. Why the correct answer wins: A commitment discounts capacity the team already knows it will use.
- **D:** Incorrect for this question. Give the scheduler real numbers so placement and scaling decisions are not guesses. Why the correct answer wins: A commitment discounts capacity the team already knows it will use.

### Question 18 — A

Answer: Set a namespace resource quota. A quota caps what the namespace may consume. Bound the total capacity a namespace may consume. Local study-map skill 1.9 (Resource Requirements and Cost Optimization), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 1 (designing highly scalable, secure, and reliable cloud-native applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Correct. Bound the total capacity a namespace may consume. In this case: A quota caps what the namespace may consume.
- **B:** Incorrect for this question. Give the scheduler real numbers so placement and scaling decisions are not guesses. Why the correct answer wins: A quota caps what the namespace may consume.
- **C:** Incorrect for this question. Place work on nodes whose shape and pricing match the workload. Why the correct answer wins: A quota caps what the namespace may consume.
- **D:** Incorrect for this question. Trade a term commitment for a lower unit price on capacity that never idles. Why the correct answer wins: A quota caps what the namespace may consume.

### Question 19 — A

Answer: Shift traffic back to the previous revision. Shifting traffic back to the earlier revision restores service immediately. Return all traffic to the known-good revision when the new one misbehaves. Local study-map skill 1.10 (Traffic Splitting and Gradual Rollout), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 1 (designing highly scalable, secure, and reliable cloud-native applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Correct. Return all traffic to the known-good revision when the new one misbehaves. In this case: Shifting traffic back to the earlier revision restores service immediately.
- **B:** Incorrect for this question. Ship the code dark and enable it per cohort without a redeploy. Why the correct answer wins: Shifting traffic back to the earlier revision restores service immediately.
- **C:** Incorrect for this question. Send a fraction of requests to the new revision while the old one still serves the rest. Why the correct answer wins: Shifting traffic back to the earlier revision restores service immediately.
- **D:** Incorrect for this question. Expose the new version to a slice of traffic before widening it. Why the correct answer wins: Shifting traffic back to the earlier revision restores service immediately.

### Question 20 — D

Answer: Canary the release at a small percentage first. A small slice gives evidence from real sessions before the full launch. Expose the new version to a slice of traffic before widening it. Local study-map skill 1.10 (Traffic Splitting and Gradual Rollout), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 1 (designing highly scalable, secure, and reliable cloud-native applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Return all traffic to the known-good revision when the new one misbehaves. Why the correct answer wins: A small slice gives evidence from real sessions before the full launch.
- **B:** Incorrect for this question. Send a fraction of requests to the new revision while the old one still serves the rest. Why the correct answer wins: A small slice gives evidence from real sessions before the full launch.
- **C:** Incorrect for this question. Send only tagged requests to the new revision for internal testing. Why the correct answer wins: A small slice gives evidence from real sessions before the full launch.
- **D:** Correct. Expose the new version to a slice of traffic before widening it. In this case: A small slice gives evidence from real sessions before the full launch.

### Question 21 — B, C

Answers: Orchestrate the steps in Workflows; Queue the work as a Cloud Tasks task. A stateful orchestration retries the single failed step, and a task queue offloads the slow call. A stateful sequence of service calls with retries and error branches. A task queue with retries and rate control aimed at a specific target. Local study-map skill 1.11 (Orchestrating Services), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 1 (designing highly scalable, secure, and reliable cloud-native applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A cron-style trigger that calls a target on a fixed timetable. Why the correct answer wins: A stateful orchestration retries the single failed step, and a task queue offloads the slow call.
- **B:** Correct. A stateful sequence of service calls with retries and error branches. In this case: A stateful orchestration retries the single failed step, and a task queue offloads the slow call.
- **C:** Correct. A task queue with retries and rate control aimed at a specific target. In this case: A stateful orchestration retries the single failed step, and a task queue offloads the slow call.
- **D:** Incorrect for this question. A durable, at-least-once message channel with independent subscribers. Why the correct answer wins: A stateful orchestration retries the single failed step, and a task queue offloads the slow call.
- **E:** Incorrect for this question. A trigger path that turns a Cloud Audit Log or resource event into a delivery. Why the correct answer wins: A stateful orchestration retries the single failed step, and a task queue offloads the slow call.

### Question 22 — C, E

Answers: Lock the bucket retention policy; Add a lifecycle rule to the bucket. A retention lock makes the records undeletable, and a lifecycle rule deletes the exports by age. Make the retention period impossible to shorten, even by an owner. Transition or delete objects by age so retention happens without a job. Local study-map skill 1.12 (Data Retention and Organization Policy), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 1 (designing highly scalable, secure, and reliable cloud-native applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A key the customer owns, rotates and can disable. Why the correct answer wins: A retention lock makes the records undeletable, and a lifecycle rule deletes the exports by age.
- **B:** Incorrect for this question. Serve every object to anyone, which removes the need to authorize at all. Why the correct answer wins: A retention lock makes the records undeletable, and a lifecycle rule deletes the exports by age.
- **C:** Correct. Transition or delete objects by age so retention happens without a job. In this case: A retention lock makes the records undeletable, and a lifecycle rule deletes the exports by age.
- **D:** Incorrect for this question. A time-limited grant to one object without exposing credentials. Why the correct answer wins: A retention lock makes the records undeletable, and a lifecycle rule deletes the exports by age.
- **E:** Correct. Make the retention period impossible to shorten, even by an owner. In this case: A retention lock makes the records undeletable, and a lifecycle rule deletes the exports by age.

### Question 23 — D

Answer: Rotate the secret on a schedule. A rotation schedule creates the new version without touching the deployment. Issue a new version and retire the old one so exposure has a bounded life. Local study-map skill 1.13 (Secrets, Keys, and Credential Rotation), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 1 (designing highly scalable, secure, and reliable cloud-native applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Present the value as a file that the process reads at runtime. Why the correct answer wins: A rotation schedule creates the new version without touching the deployment.
- **B:** Incorrect for this question. Inject the value into the process environment at start-up. Why the correct answer wins: A rotation schedule creates the new version without touching the deployment.
- **C:** Incorrect for this question. A long-lived credential that has to be stored and rotated by hand. Why the correct answer wins: A rotation schedule creates the new version without touching the deployment.
- **D:** Correct. Issue a new version and retire the old one so exposure has a bounded life. In this case: A rotation schedule creates the new version without touching the deployment.

### Question 24 — D

Answer: Encrypt with a Cloud KMS key. A customer-managed key puts the rotation schedule under the team's control. A managed key whose use is authorized by IAM and recorded in audit logs. Local study-map skill 1.13 (Secrets, Keys, and Credential Rotation), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 1 (designing highly scalable, secure, and reliable cloud-native applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A long-lived credential that has to be stored and rotated by hand. Why the correct answer wins: A customer-managed key puts the rotation schedule under the team's control.
- **B:** Incorrect for this question. A key the customer owns, rotates and can disable. Why the correct answer wins: A customer-managed key puts the rotation schedule under the team's control.
- **C:** Incorrect for this question. A managed secret store with versioning and access audit. Why the correct answer wins: A customer-managed key puts the rotation schedule under the team's control.
- **D:** Correct. A managed key whose use is authorized by IAM and recorded in audit logs. In this case: A customer-managed key puts the rotation schedule under the team's control.

### Question 25 — D, E

Answers: Put Identity-Aware Proxy in front of the service; Validate the signed JWT from the proxy. The proxy gates the request first, and the signed assertion tells the app who called. Authenticate and authorize users before a request reaches the application. Check the assertion the proxy adds so only proxied requests are trusted. Local study-map skill 1.14 (Application Authentication), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 1 (designing highly scalable, secure, and reliable cloud-native applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A managed identity service for customer accounts and tokens. Why the correct answer wins: The proxy gates the request first, and the signed assertion tells the app who called.
- **B:** Incorrect for this question. A dedicated identity whose roles can be granted and revoked independently. Why the correct answer wins: The proxy gates the request first, and the signed assertion tells the app who called.
- **C:** Incorrect for this question. Let anyone reach the endpoint, which is only appropriate for public content. Why the correct answer wins: The proxy gates the request first, and the signed assertion tells the app who called.
- **D:** Correct. Check the assertion the proxy adds so only proxied requests are trusted. In this case: The proxy gates the request first, and the signed assertion tells the app who called.
- **E:** Correct. Authenticate and authorize users before a request reaches the application. In this case: The proxy gates the request first, and the signed assertion tells the app who called.

### Question 26 — C

Answer: Use Identity Platform for end-user sign-in. A managed identity service supports guest accounts and later linking. A managed identity service for customer accounts and tokens. Local study-map skill 1.14 (Application Authentication), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 1 (designing highly scalable, secure, and reliable cloud-native applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A dedicated identity whose roles can be granted and revoked independently. Why the correct answer wins: A managed identity service supports guest accounts and later linking.
- **B:** Incorrect for this question. Check the assertion the proxy adds so only proxied requests are trusted. Why the correct answer wins: A managed identity service supports guest accounts and later linking.
- **C:** Correct. A managed identity service for customer accounts and tokens. In this case: A managed identity service supports guest accounts and later linking.
- **D:** Incorrect for this question. Let the client library find credentials from the environment. Why the correct answer wins: A managed identity service supports guest accounts and later linking.

### Question 27 — D

Answer: Define a custom role for the narrow permission set. A custom role names exactly the nine permissions. A role built from an explicit permission list. Local study-map skill 1.15 (Least Privilege and Service-to-Service Security), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 1 (designing highly scalable, secure, and reliable cloud-native applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A legacy broad role that can change most resources in the project. Why the correct answer wins: A custom role names exactly the nine permissions.
- **B:** Incorrect for this question. A dedicated identity whose roles can be granted and revoked independently. Why the correct answer wins: A custom role names exactly the nine permissions.
- **C:** Incorrect for this question. Scope permissions to the actions in use rather than the whole service. Why the correct answer wins: A custom role names exactly the nine permissions.
- **D:** Correct. A role built from an explicit permission list. In this case: A custom role names exactly the nine permissions.

### Question 28 — A

Answer: Use Cloud Service Mesh for service-to-service traffic. A mesh enforces mutual authentication between services at the sidecar. Mutual TLS, retries and traffic policy applied without changing application code. Local study-map skill 1.15 (Least Privilege and Service-to-Service Security), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 1 (designing highly scalable, secure, and reliable cloud-native applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Correct. Mutual TLS, retries and traffic policy applied without changing application code. In this case: A mesh enforces mutual authentication between services at the sidecar.
- **B:** Incorrect for this question. Scope permissions to the actions in use rather than the whole service. Why the correct answer wins: A mesh enforces mutual authentication between services at the sidecar.
- **C:** Incorrect for this question. Authenticate and authorize users before a request reaches the application. Why the correct answer wins: A mesh enforces mutual authentication between services at the sidecar.
- **D:** Incorrect for this question. Restrict which pods may talk to which pods inside the cluster. Why the correct answer wins: A mesh enforces mutual authentication between services at the sidecar.

### Question 29 — D

Answer: Hash the leading key component to avoid hotspots. A monotonic prefix concentrates every write on one tablet. Spread writes so one tablet does not take the whole rate. Local study-map skill 1.16 (Storage and Schema Selection), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 1 (designing highly scalable, secure, and reliable cloud-native applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Order the key so the query becomes a contiguous range scan. Why the correct answer wins: A monotonic prefix concentrates every write on one tablet.
- **B:** Incorrect for this question. A document store with real-time listeners and mobile SDKs. Why the correct answer wins: A monotonic prefix concentrates every write on one tablet.
- **C:** Incorrect for this question. A relational database with strongly consistent multi-region transactions. Why the correct answer wins: A monotonic prefix concentrates every write on one tablet.
- **D:** Correct. Spread writes so one tablet does not take the whole rate. In this case: A monotonic prefix concentrates every write on one tablet.

### Question 30 — A

Answer: Use Firestore in Datastore mode. The legacy compatibility mode keeps those entity queries working. Keep the Datastore API and its strong consistency semantics. Local study-map skill 1.16 (Storage and Schema Selection), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 1 (designing highly scalable, secure, and reliable cloud-native applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Correct. Keep the Datastore API and its strong consistency semantics. In this case: The legacy compatibility mode keeps those entity queries working.
- **B:** Incorrect for this question. A managed Redis-compatible cache in front of the system of record. Why the correct answer wins: The legacy compatibility mode keeps those entity queries working.
- **C:** Incorrect for this question. A document store with real-time listeners and mobile SDKs. Why the correct answer wins: The legacy compatibility mode keeps those entity queries working.
- **D:** Incorrect for this question. A relational database with strongly consistent multi-region transactions. Why the correct answer wins: The legacy compatibility mode keeps those entity queries working.

### Question 31 — A, E

Answers: Issue a signed URL with a short expiry; Make the bucket public. A short-lived signed link authorises the single file, and anonymous read suits the public assets. A time-limited grant to one object without exposing credentials. Serve every object to anyone, which removes the need to authorize at all. Local study-map skill 1.17 (Signed URLs and Time-Limited Access), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 1 (designing highly scalable, secure, and reliable cloud-native applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Correct. A time-limited grant to one object without exposing credentials. In this case: A short-lived signed link authorises the single file, and anonymous read suits the public assets.
- **B:** Incorrect for this question. Transition or delete objects by age so retention happens without a job. Why the correct answer wins: A short-lived signed link authorises the single file, and anonymous read suits the public assets.
- **C:** Incorrect for this question. A managed key whose use is authorized by IAM and recorded in audit logs. Why the correct answer wins: A short-lived signed link authorises the single file, and anonymous read suits the public assets.
- **D:** Incorrect for this question. Make the retention period impossible to shorten, even by an owner. Why the correct answer wins: A short-lived signed link authorises the single file, and anonymous read suits the public assets.
- **E:** Correct. Serve every object to anyone, which removes the need to authorize at all. In this case: A short-lived signed link authorises the single file, and anonymous read suits the public assets.

### Question 32 — B

Answer: Stream the events into BigQuery. Streaming the events makes them queryable within seconds. Land analytics rows in the warehouse for SQL and ML use. Local study-map skill 1.18 (Analytics and ML Data Handoff), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 1 (designing highly scalable, secure, and reliable cloud-native applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Write topic messages straight into a table without a consumer. Why the correct answer wins: Streaming the events makes them queryable within seconds.
- **B:** Correct. Land analytics rows in the warehouse for SQL and ML use. In this case: Streaming the events makes them queryable within seconds.
- **C:** Incorrect for this question. Load a periodic extract rather than a continuous stream. Why the correct answer wins: Streaming the events makes them queryable within seconds.
- **D:** Incorrect for this question. Durable object storage addressed by name rather than a database row. Why the correct answer wins: Streaming the events makes them queryable within seconds.

### Question 33 — C

Answer: Run the service emulator locally. A local emulator reproduces the race without any cloud resource. A local stand-in for a managed service used for unit and integration work. Local study-map skill 2.1 (Local Emulation of Cloud Services), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 2 (building and testing applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A browser terminal with the SDK and tooling already installed. Why the correct answer wins: A local emulator reproduces the race without any cloud resource.
- **B:** Incorrect for this question. A managed, container-defined development environment behind a private endpoint. Why the correct answer wins: A local emulator reproduces the race without any cloud resource.
- **C:** Correct. A local stand-in for a managed service used for unit and integration work. In this case: A local emulator reproduces the race without any cloud resource.
- **D:** Incorrect for this question. Editor integration for scaffolding, running and debugging on Google Cloud. Why the correct answer wins: A local emulator reproduces the race without any cloud resource.

### Question 34 — D

Answer: Use Cloud Workstations for the environment. A managed workstation keeps the source inside the managed environment. A managed, container-defined development environment behind a private endpoint. Local study-map skill 2.1 (Local Emulation of Cloud Services), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 2 (building and testing applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A local stand-in for a managed service used for unit and integration work. Why the correct answer wins: A managed workstation keeps the source inside the managed environment.
- **B:** Incorrect for this question. Editor integration for scaffolding, running and debugging on Google Cloud. Why the correct answer wins: A managed workstation keeps the source inside the managed environment.
- **C:** Incorrect for this question. A browser terminal with the SDK and tooling already installed. Why the correct answer wins: A managed workstation keeps the source inside the managed environment.
- **D:** Correct. A managed, container-defined development environment behind a private endpoint. In this case: A managed workstation keeps the source inside the managed environment.

### Question 35 — C

Answer: Use Cloud Shell for the session. A browser shell needs no installation on the borrowed machine. A browser terminal with the SDK and tooling already installed. Local study-map skill 2.1 (Local Emulation of Cloud Services), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 2 (building and testing applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A local stand-in for a managed service used for unit and integration work. Why the correct answer wins: A browser shell needs no installation on the borrowed machine.
- **B:** Incorrect for this question. A managed, container-defined development environment behind a private endpoint. Why the correct answer wins: A browser shell needs no installation on the borrowed machine.
- **C:** Correct. A browser terminal with the SDK and tooling already installed. In this case: A browser shell needs no installation on the borrowed machine.
- **D:** Incorrect for this question. Editor integration for scaffolding, running and debugging on Google Cloud. Why the correct answer wins: A browser shell needs no installation on the borrowed machine.

### Question 36 — B, E

Answers: Ask Gemini Cloud Assist for a diagnosis; Connect the assistant to an MCP server. An in-editor assistant explains the failure context, and an MCP server lets it query the tracker directly. An assistant that reads telemetry and proposes a cause and a next step. Give the assistant a defined tool surface instead of pasting context by hand. Local study-map skill 2.2 (Developer Tooling and AI Assistance), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 2 (building and testing applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A browser terminal with the SDK and tooling already installed. Why the correct answer wins: An in-editor assistant explains the failure context, and an MCP server lets it query the tracker directly.
- **B:** Correct. An assistant that reads telemetry and proposes a cause and a next step. In this case: An in-editor assistant explains the failure context, and an MCP server lets it query the tracker directly.
- **C:** Incorrect for this question. Editor integration for scaffolding, running and debugging on Google Cloud. Why the correct answer wins: An in-editor assistant explains the failure context, and an MCP server lets it query the tracker directly.
- **D:** Incorrect for this question. Generate a first draft from context, then review and correct it. Why the correct answer wins: An in-editor assistant explains the failure context, and an MCP server lets it query the tracker directly.
- **E:** Correct. Give the assistant a defined tool surface instead of pasting context by hand. In this case: An in-editor assistant explains the failure context, and an MCP server lets it query the tracker directly.

### Question 37 — D

Answer: Use an AI coding assistant to draft the tests. A coding assistant drafts the migration from the schema for review. Generate a first draft from context, then review and correct it. Local study-map skill 2.2 (Developer Tooling and AI Assistance), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 2 (building and testing applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Editor integration for scaffolding, running and debugging on Google Cloud. Why the correct answer wins: A coding assistant drafts the migration from the schema for review.
- **B:** Incorrect for this question. An assistant that reads telemetry and proposes a cause and a next step. Why the correct answer wins: A coding assistant drafts the migration from the schema for review.
- **C:** Incorrect for this question. Give the assistant a defined tool surface instead of pasting context by hand. Why the correct answer wins: A coding assistant drafts the migration from the schema for review.
- **D:** Correct. Generate a first draft from context, then review and correct it. In this case: A coding assistant drafts the migration from the schema for review.

### Question 38 — B

Answer: Develop with Cloud Code in the IDE. A hosted editor with breakpoints lets the defect be stepped through remotely. Editor integration for scaffolding, running and debugging on Google Cloud. Local study-map skill 2.2 (Developer Tooling and AI Assistance), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 2 (building and testing applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Read variable state in a running deployment without redeploying. Why the correct answer wins: A hosted editor with breakpoints lets the defect be stepped through remotely.
- **B:** Correct. Editor integration for scaffolding, running and debugging on Google Cloud. In this case: A hosted editor with breakpoints lets the defect be stepped through remotely.
- **C:** Incorrect for this question. A managed, container-defined development environment behind a private endpoint. Why the correct answer wins: A hosted editor with breakpoints lets the defect be stepped through remotely.
- **D:** Incorrect for this question. A browser terminal with the SDK and tooling already installed. Why the correct answer wins: A hosted editor with breakpoints lets the defect be stepped through remotely.

### Question 39 — A

Answer: Build the image with Cloud Build. Running the declared steps in the managed builder removes the difference. A managed build service that runs the steps from a build configuration file. Local study-map skill 2.3 (Container Builds with Cloud Build), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 2 (building and testing applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Correct. A managed build service that runs the steps from a build configuration file. In this case: Running the declared steps in the managed builder removes the difference.
- **B:** Incorrect for this question. Run the build steps locally and push the result when someone remembers. Why the correct answer wins: Running the declared steps in the managed builder removes the difference.
- **C:** Incorrect for this question. A loop that rebuilds and redeploys automatically on a source change. Why the correct answer wins: Running the declared steps in the managed builder removes the difference.
- **D:** Incorrect for this question. Release exactly the artifact that was tested rather than a moving tag. Why the correct answer wins: Running the declared steps in the managed builder removes the difference.

### Question 40 — B

Answer: Trigger the build from a repository push. A trigger on the tag starts the build on its own. Start the pipeline when the branch changes rather than by hand. Local study-map skill 2.3 (Container Builds with Cloud Build), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 2 (building and testing applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Run the build steps locally and push the result when someone remembers. Why the correct answer wins: A trigger on the tag starts the build on its own.
- **B:** Correct. Start the pipeline when the branch changes rather than by hand. In this case: A trigger on the tag starts the build on its own.
- **C:** Incorrect for this question. A task queue with retries and rate control aimed at a specific target. Why the correct answer wins: A trigger on the tag starts the build on its own.
- **D:** Incorrect for this question. A cron-style trigger that calls a target on a fixed timetable. Why the correct answer wins: A trigger on the tag starts the build on its own.

### Question 41 — A

Answer: Package the monolith into a container image. Building the image from the team's Dockerfile uses the private layer. Wrap the existing process in a portable artifact that a managed runtime can execute. Local study-map skill 2.3 (Container Builds with Cloud Build), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 2 (building and testing applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Correct. Wrap the existing process in a portable artifact that a managed runtime can execute. In this case: Building the image from the team's Dockerfile uses the private layer.
- **B:** Incorrect for this question. Run the build steps locally and push the result when someone remembers. Why the correct answer wins: Building the image from the team's Dockerfile uses the private layer.
- **C:** Incorrect for this question. Hand the source to the managed builder instead of shipping an image. Why the correct answer wins: Building the image from the team's Dockerfile uses the private layer.
- **D:** Incorrect for this question. A loop that rebuilds and redeploys automatically on a source change. Why the correct answer wins: Building the image from the team's Dockerfile uses the private layer.

### Question 42 — A

Answer: Push the image to Artifact Registry. A scoped repository grants the pull to the runtime identity alone. A managed registry with IAM-scoped repositories per environment. Local study-map skill 2.3 (Container Builds with Cloud Build), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 2 (building and testing applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Correct. A managed registry with IAM-scoped repositories per environment. In this case: A scoped repository grants the pull to the runtime identity alone.
- **B:** Incorrect for this question. Durable object storage addressed by name rather than a database row. Why the correct answer wins: A scoped repository grants the pull to the runtime identity alone.
- **C:** Incorrect for this question. The older registry whose access model is project-wide Cloud Storage. Why the correct answer wins: A scoped repository grants the pull to the runtime identity alone.
- **D:** Incorrect for this question. A managed build service that runs the steps from a build configuration file. Why the correct answer wins: A scoped repository grants the pull to the runtime identity alone.

### Question 43 — A, C

Answers: Push the image to Artifact Registry; Store the objects in Cloud Storage. A repository per environment keeps access separate, and object storage versions the release notes. A managed registry with IAM-scoped repositories per environment. Durable object storage addressed by name rather than a database row. Local study-map skill 2.4 (Artifact Registry and Image Storage), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 2 (building and testing applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Correct. A managed registry with IAM-scoped repositories per environment. In this case: A repository per environment keeps access separate, and object storage versions the release notes.
- **B:** Incorrect for this question. A key the customer owns, rotates and can disable. Why the correct answer wins: A repository per environment keeps access separate, and object storage versions the release notes.
- **C:** Correct. Durable object storage addressed by name rather than a database row. In this case: A repository per environment keeps access separate, and object storage versions the release notes.
- **D:** Incorrect for this question. The older registry whose access model is project-wide Cloud Storage. Why the correct answer wins: A repository per environment keeps access separate, and object storage versions the release notes.
- **E:** Incorrect for this question. A managed build service that runs the steps from a build configuration file. Why the correct answer wins: A repository per environment keeps access separate, and object storage versions the release notes.

### Question 44 — C

Answer: Push the image to Container Registry. The legacy host keeps that older automation pushing and pulling. The older registry whose access model is project-wide Cloud Storage. Local study-map skill 2.4 (Artifact Registry and Image Storage), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 2 (building and testing applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Durable object storage addressed by name rather than a database row. Why the correct answer wins: The legacy host keeps that older automation pushing and pulling.
- **B:** Incorrect for this question. A managed registry with IAM-scoped repositories per environment. Why the correct answer wins: The legacy host keeps that older automation pushing and pulling.
- **C:** Correct. The older registry whose access model is project-wide Cloud Storage. In this case: The legacy host keeps that older automation pushing and pulling.
- **D:** Incorrect for this question. A managed build service that runs the steps from a build configuration file. Why the correct answer wins: The legacy host keeps that older automation pushing and pulling.

### Question 45 — D

Answer: Use a customer-managed encryption key. A customer-managed key puts encryption and revocation in the team's hands. A key the customer owns, rotates and can disable. Local study-map skill 2.4 (Artifact Registry and Image Storage), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 2 (building and testing applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A managed registry with IAM-scoped repositories per environment. Why the correct answer wins: A customer-managed key puts encryption and revocation in the team's hands.
- **B:** Incorrect for this question. Durable object storage addressed by name rather than a database row. Why the correct answer wins: A customer-managed key puts encryption and revocation in the team's hands.
- **C:** Incorrect for this question. A managed build service that runs the steps from a build configuration file. Why the correct answer wins: A customer-managed key puts encryption and revocation in the team's hands.
- **D:** Correct. A key the customer owns, rotates and can disable. In this case: A customer-managed key puts encryption and revocation in the team's hands.

### Question 46 — C, D

Answers: Scan the image with Artifact Analysis; Enforce admission with Binary Authorization. Scanning reports the vulnerabilities, and admission control refuses the unsigned image. Report known vulnerabilities in the image layers and packages. Only images that satisfy the attestation policy may be deployed. Local study-map skill 2.5 (Build Provenance and Admission Control), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 2 (building and testing applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Aggregate and triage security findings across the project. Why the correct answer wins: Scanning reports the vulnerabilities, and admission control refuses the unsigned image.
- **B:** Incorrect for this question. A signed record of what was built and from which source. Why the correct answer wins: Scanning reports the vulnerabilities, and admission control refuses the unsigned image.
- **C:** Correct. Only images that satisfy the attestation policy may be deployed. In this case: Scanning reports the vulnerabilities, and admission control refuses the unsigned image.
- **D:** Correct. Report known vulnerabilities in the image layers and packages. In this case: Scanning reports the vulnerabilities, and admission control refuses the unsigned image.
- **E:** Incorrect for this question. Demand a stronger provenance guarantee as a gate on the pipeline. Why the correct answer wins: Scanning reports the vulnerabilities, and admission control refuses the unsigned image.

### Question 47 — C

Answer: Require a higher supply-chain level before release. That level is the one where the builder is hardened and provenance cannot be forged. Demand a stronger provenance guarantee as a gate on the pipeline. Local study-map skill 2.5 (Build Provenance and Admission Control), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 2 (building and testing applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Only images that satisfy the attestation policy may be deployed. Why the correct answer wins: That level is the one where the builder is hardened and provenance cannot be forged.
- **B:** Incorrect for this question. A signed record of what was built and from which source. Why the correct answer wins: That level is the one where the builder is hardened and provenance cannot be forged.
- **C:** Correct. Demand a stronger provenance guarantee as a gate on the pipeline. In this case: That level is the one where the builder is hardened and provenance cannot be forged.
- **D:** Incorrect for this question. Report known vulnerabilities in the image layers and packages. Why the correct answer wins: That level is the one where the builder is hardened and provenance cannot be forged.

### Question 48 — C

Answer: Generate build provenance in Cloud Build. The provenance record names the source revision the image was built from. A signed record of what was built and from which source. Local study-map skill 2.5 (Build Provenance and Admission Control), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 2 (building and testing applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Report known vulnerabilities in the image layers and packages. Why the correct answer wins: The provenance record names the source revision the image was built from.
- **B:** Incorrect for this question. Demand a stronger provenance guarantee as a gate on the pipeline. Why the correct answer wins: The provenance record names the source revision the image was built from.
- **C:** Correct. A signed record of what was built and from which source. In this case: The provenance record names the source revision the image was built from.
- **D:** Incorrect for this question. Only images that satisfy the attestation policy may be deployed. Why the correct answer wins: The provenance record names the source revision the image was built from.

### Question 49 — A, B

Answers: Add a unit test with dependencies stubbed; Run the tests as a Cloud Build step. A unit test returns in seconds, and a build step runs it on every change. Exercise one unit in isolation with its collaborators replaced. Fail the pipeline at the test stage instead of after deployment. Local study-map skill 2.6 (Unit Testing Practice), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 2 (building and testing applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Correct. Exercise one unit in isolation with its collaborators replaced. In this case: A unit test returns in seconds, and a build step runs it on every change.
- **B:** Correct. Fail the pipeline at the test stage instead of after deployment. In this case: A unit test returns in seconds, and a build step runs it on every change.
- **C:** Incorrect for this question. Make a passing test suite a precondition for release. Why the correct answer wins: A unit test returns in seconds, and a build step runs it on every change.
- **D:** Incorrect for this question. Keep the suite trustworthy while the unstable test is repaired. Why the correct answer wins: A unit test returns in seconds, and a build step runs it on every change.
- **E:** Incorrect for this question. Measure behaviour under expected peak traffic rather than guessing. Why the correct answer wins: A unit test returns in seconds, and a build step runs it on every change.

### Question 50 — A

Answer: Quarantine the flaky test and fix it. Quarantining it keeps the suite trustworthy while the test is fixed. Keep the suite trustworthy while the unstable test is repaired. Local study-map skill 2.6 (Unit Testing Practice), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 2 (building and testing applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Correct. Keep the suite trustworthy while the unstable test is repaired. In this case: Quarantining it keeps the suite trustworthy while the test is fixed.
- **B:** Incorrect for this question. Make a passing test suite a precondition for release. Why the correct answer wins: Quarantining it keeps the suite trustworthy while the test is fixed.
- **C:** Incorrect for this question. Exercise one unit in isolation with its collaborators replaced. Why the correct answer wins: Quarantining it keeps the suite trustworthy while the test is fixed.
- **D:** Incorrect for this question. Exercise the wire-up between components before deploying. Why the correct answer wins: Quarantining it keeps the suite trustworthy while the test is fixed.

### Question 51 — B

Answer: Block the deploy on the test result. A gate makes the red suite stop promotion. Make a passing test suite a precondition for release. Local study-map skill 2.6 (Unit Testing Practice), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 2 (building and testing applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Measure behaviour under expected peak traffic rather than guessing. Why the correct answer wins: A gate makes the red suite stop promotion.
- **B:** Correct. Make a passing test suite a precondition for release. In this case: A gate makes the red suite stop promotion.
- **C:** Incorrect for this question. Exercise the wire-up between components before deploying. Why the correct answer wins: A gate makes the red suite stop promotion.
- **D:** Incorrect for this question. Keep the suite trustworthy while the unstable test is repaired. Why the correct answer wins: A gate makes the red suite stop promotion.

### Question 52 — D

Answer: Run an integration test against the emulator. An integration run uses the producer's real output, so the mismatch shows. Exercise the wire-up between components before deploying. Local study-map skill 2.7 (Automated Integration Testing), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 2 (building and testing applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Read variable state in a running deployment without redeploying. Why the correct answer wins: An integration run uses the producer's real output, so the mismatch shows.
- **B:** Incorrect for this question. Measure behaviour under expected peak traffic rather than guessing. Why the correct answer wins: An integration run uses the producer's real output, so the mismatch shows.
- **C:** Incorrect for this question. Exercise one unit in isolation with its collaborators replaced. Why the correct answer wins: An integration run uses the producer's real output, so the mismatch shows.
- **D:** Correct. Exercise the wire-up between components before deploying. In this case: An integration run uses the producer's real output, so the mismatch shows.

### Question 53 — C

Answer: Load-test the release before the rollout. A load run at ten times volume measures the tail before release. Measure behaviour under expected peak traffic rather than guessing. Local study-map skill 2.7 (Automated Integration Testing), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 2 (building and testing applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Exercise one unit in isolation with its collaborators replaced. Why the correct answer wins: A load run at ten times volume measures the tail before release.
- **B:** Incorrect for this question. Find the function consuming CPU or memory under real traffic. Why the correct answer wins: A load run at ten times volume measures the tail before release.
- **C:** Correct. Measure behaviour under expected peak traffic rather than guessing. In this case: A load run at ten times volume measures the tail before release.
- **D:** Incorrect for this question. Exercise the wire-up between components before deploying. Why the correct answer wins: A load run at ten times volume measures the tail before release.

### Question 54 — D

Answer: Profile the service with Cloud Profiler. A profiler attributes the samples to the allocation site. Find the function consuming CPU or memory under real traffic. Local study-map skill 2.7 (Automated Integration Testing), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 2 (building and testing applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Measure behaviour under expected peak traffic rather than guessing. Why the correct answer wins: A profiler attributes the samples to the allocation site.
- **B:** Incorrect for this question. Read variable state in a running deployment without redeploying. Why the correct answer wins: A profiler attributes the samples to the allocation site.
- **C:** Incorrect for this question. Group and count application errors instead of grepping logs. Why the correct answer wins: A profiler attributes the samples to the allocation site.
- **D:** Correct. Find the function consuming CPU or memory under real traffic. In this case: A profiler attributes the samples to the allocation site.

### Question 55 — C

Answer: Inspect the live process with Cloud Debugger. Attaching the debugger pauses the run where the state is wrong. Read variable state in a running deployment without redeploying. Local study-map skill 2.7 (Automated Integration Testing), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 2 (building and testing applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Find the function consuming CPU or memory under real traffic. Why the correct answer wins: Attaching the debugger pauses the run where the state is wrong.
- **B:** Incorrect for this question. Exercise one unit in isolation with its collaborators replaced. Why the correct answer wins: Attaching the debugger pauses the run where the state is wrong.
- **C:** Correct. Read variable state in a running deployment without redeploying. In this case: Attaching the debugger pauses the run where the state is wrong.
- **D:** Incorrect for this question. Exercise the wire-up between components before deploying. Why the correct answer wins: Attaching the debugger pauses the run where the state is wrong.

### Question 56 — B

Answer: Deploy from source and let the platform build it. Building from source removes the Dockerfile the team maintains. Hand the source to the managed builder instead of shipping an image. Local study-map skill 3.1 (Deploying Cloud Run from Source), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 3 (configuring cloud-native applications for deployment): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A loop that rebuilds and redeploys automatically on a source change. Why the correct answer wins: Building from source removes the Dockerfile the team maintains.
- **B:** Correct. Hand the source to the managed builder instead of shipping an image. In this case: Building from source removes the Dockerfile the team maintains.
- **C:** Incorrect for this question. Run the build steps locally and push the result when someone remembers. Why the correct answer wins: Building from source removes the Dockerfile the team maintains.
- **D:** Incorrect for this question. Wrap the existing process in a portable artifact that a managed runtime can execute. Why the correct answer wins: Building from source removes the Dockerfile the team maintains.

### Question 57 — D

Answer: Keep a minimum number of instances warm. A warm minimum count removes the delay after quiet hours. Pay for idle capacity so a cold start never appears in the latency percentiles. Local study-map skill 3.1 (Deploying Cloud Run from Source), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 3 (configuring cloud-native applications for deployment): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Charge only while a request is being handled, which suits bursty traffic. Why the correct answer wins: A warm minimum count removes the delay after quiet hours.
- **B:** Incorrect for this question. Bound the blast radius and the bill at the cost of queueing when the cap is reached. Why the correct answer wins: A warm minimum count removes the delay after quiet hours.
- **C:** Incorrect for this question. Speed initialization without paying for the extra CPU afterwards. Why the correct answer wins: A warm minimum count removes the delay after quiet hours.
- **D:** Correct. Pay for idle capacity so a cold start never appears in the latency percentiles. In this case: A warm minimum count removes the delay after quiet hours.

### Question 58 — C

Answer: Raise CPU during start-up only. Extra CPU during start lets the boot finish inside the window. Speed initialization without paying for the extra CPU afterwards. Local study-map skill 3.1 (Deploying Cloud Run from Source), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 3 (configuring cloud-native applications for deployment): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Pay for idle capacity so a cold start never appears in the latency percentiles. Why the correct answer wins: Extra CPU during start lets the boot finish inside the window.
- **B:** Incorrect for this question. Let each instance serve more simultaneous requests before another instance is started. Why the correct answer wins: Extra CPU during start lets the boot finish inside the window.
- **C:** Correct. Speed initialization without paying for the extra CPU afterwards. In this case: Extra CPU during start lets the boot finish inside the window.
- **D:** Incorrect for this question. Charge only while a request is being handled, which suits bursty traffic. Why the correct answer wins: Extra CPU during start lets the boot finish inside the window.

### Question 59 — B

Answer: Run the batch work as a Cloud Run job. A job processes the batch, exits, and holds no serving capacity. A task-shaped execution that runs to completion instead of serving requests. Local study-map skill 3.1 (Deploying Cloud Run from Source), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 3 (configuring cloud-native applications for deployment): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A trigger path that turns a Cloud Audit Log or resource event into a delivery. Why the correct answer wins: A job processes the batch, exits, and holds no serving capacity.
- **B:** Correct. A task-shaped execution that runs to completion instead of serving requests. In this case: A job processes the batch, exits, and holds no serving capacity.
- **C:** Incorrect for this question. A managed container runtime that scales to zero and bills per request while it serves traffic. Why the correct answer wins: A job processes the batch, exits, and holds no serving capacity.
- **D:** Incorrect for this question. An event-triggered function runtime for a single-purpose handler rather than a long-lived service. Why the correct answer wins: A job processes the batch, exits, and holds no serving capacity.

### Question 60 — D, E

Answers: Route the event with Eventarc; Grant the invoker role to the calling identity. The event trigger delivers the change, and the invoker role lets the trigger call the receiver. A trigger path that turns a Cloud Audit Log or resource event into a delivery. Control who may call the service with IAM rather than a shared token. Local study-map skill 3.2 (Cloud Run Triggers and Event Receivers), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 3 (configuring cloud-native applications for deployment): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A stateful sequence of service calls with retries and error branches. Why the correct answer wins: The event trigger delivers the change, and the invoker role lets the trigger call the receiver.
- **B:** Incorrect for this question. A cron-style trigger that calls a target on a fixed timetable. Why the correct answer wins: The event trigger delivers the change, and the invoker role lets the trigger call the receiver.
- **C:** Incorrect for this question. Push each message to an endpoint instead of having the consumer pull. Why the correct answer wins: The event trigger delivers the change, and the invoker role lets the trigger call the receiver.
- **D:** Correct. A trigger path that turns a Cloud Audit Log or resource event into a delivery. In this case: The event trigger delivers the change, and the invoker role lets the trigger call the receiver.
- **E:** Correct. Control who may call the service with IAM rather than a shared token. In this case: The event trigger delivers the change, and the invoker role lets the trigger call the receiver.

### Question 61 — A

Answer: Queue the work as a Cloud Tasks task. A task scheduled for that time with a stable name is delivered once. A task queue with retries and rate control aimed at a specific target. Local study-map skill 3.2 (Cloud Run Triggers and Event Receivers), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 3 (configuring cloud-native applications for deployment): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Correct. A task queue with retries and rate control aimed at a specific target. In this case: A task scheduled for that time with a stable name is delivered once.
- **B:** Incorrect for this question. A cron-style trigger that calls a target on a fixed timetable. Why the correct answer wins: A task scheduled for that time with a stable name is delivered once.
- **C:** Incorrect for this question. A durable, at-least-once message channel with independent subscribers. Why the correct answer wins: A task scheduled for that time with a stable name is delivered once.
- **D:** Incorrect for this question. A trigger path that turns a Cloud Audit Log or resource event into a delivery. Why the correct answer wins: A task scheduled for that time with a stable name is delivered once.

### Question 62 — B

Answer: Schedule the invocation with Cloud Scheduler. A scheduled job fires on the declared hourly cadence. A cron-style trigger that calls a target on a fixed timetable. Local study-map skill 3.2 (Cloud Run Triggers and Event Receivers), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 3 (configuring cloud-native applications for deployment): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A task queue with retries and rate control aimed at a specific target. Why the correct answer wins: A scheduled job fires on the declared hourly cadence.
- **B:** Correct. A cron-style trigger that calls a target on a fixed timetable. In this case: A scheduled job fires on the declared hourly cadence.
- **C:** Incorrect for this question. A trigger path that turns a Cloud Audit Log or resource event into a delivery. Why the correct answer wins: A scheduled job fires on the declared hourly cadence.
- **D:** Incorrect for this question. A stateful sequence of service calls with retries and error branches. Why the correct answer wins: A scheduled job fires on the declared hourly cadence.

### Question 63 — A

Answer: Use request-based billing. Request-based billing charges only while requests are being served. Charge only while a request is being handled, which suits bursty traffic. Local study-map skill 3.3 (Cloud Run Service Configuration), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 3 (configuring cloud-native applications for deployment): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Correct. Charge only while a request is being handled, which suits bursty traffic. In this case: Request-based billing charges only while requests are being served.
- **B:** Incorrect for this question. Trade a term commitment for a lower unit price on capacity that never idles. Why the correct answer wins: Request-based billing charges only while requests are being served.
- **C:** Incorrect for this question. Charge for the whole instance lifetime, which suits steady background work. Why the correct answer wins: Request-based billing charges only while requests are being served.
- **D:** Incorrect for this question. Pay for idle capacity so a cold start never appears in the latency percentiles. Why the correct answer wins: Request-based billing charges only while requests are being served.

### Question 64 — D

Answer: Restrict ingress to internal traffic. Internal ingress refuses any traffic that arrives from outside the network. Accept only traffic from the VPC and internal load balancers. Local study-map skill 3.3 (Cloud Run Service Configuration), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 3 (configuring cloud-native applications for deployment): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Authenticate and authorize users before a request reaches the application. Why the correct answer wins: Internal ingress refuses any traffic that arrives from outside the network.
- **B:** Incorrect for this question. A single anycast address that routes to the nearest healthy backend. Why the correct answer wins: Internal ingress refuses any traffic that arrives from outside the network.
- **C:** Incorrect for this question. Let anyone reach the endpoint, which is only appropriate for public content. Why the correct answer wins: Internal ingress refuses any traffic that arrives from outside the network.
- **D:** Correct. Accept only traffic from the VPC and internal load balancers. In this case: Internal ingress refuses any traffic that arrives from outside the network.

### Question 65 — C

Answer: Allow unauthenticated invocations. Allowing unauthenticated calls lets the partner post without a token. Let anyone reach the endpoint, which is only appropriate for public content. Local study-map skill 3.3 (Cloud Run Service Configuration), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 3 (configuring cloud-native applications for deployment): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Accept only traffic from the VPC and internal load balancers. Why the correct answer wins: Allowing unauthenticated calls lets the partner post without a token.
- **B:** Incorrect for this question. Control who may call the service with IAM rather than a shared token. Why the correct answer wins: Allowing unauthenticated calls lets the partner post without a token.
- **C:** Correct. Let anyone reach the endpoint, which is only appropriate for public content. In this case: Allowing unauthenticated calls lets the partner post without a token.
- **D:** Incorrect for this question. Authenticate and authorize users before a request reaches the application. Why the correct answer wins: Allowing unauthenticated calls lets the partner post without a token.

### Question 66 — C

Answer: Raise the per-instance concurrency limit. Lowering concurrency per instance keeps memory inside the limit. Let each instance serve more simultaneous requests before another instance is started. Local study-map skill 3.3 (Cloud Run Service Configuration), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 3 (configuring cloud-native applications for deployment): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Give extra CPU during start-up so initialization finishes faster at a small extra charge. Why the correct answer wins: Lowering concurrency per instance keeps memory inside the limit.
- **B:** Incorrect for this question. Pay for idle capacity so a cold start never appears in the latency percentiles. Why the correct answer wins: Lowering concurrency per instance keeps memory inside the limit.
- **C:** Correct. Let each instance serve more simultaneous requests before another instance is started. In this case: Lowering concurrency per instance keeps memory inside the limit.
- **D:** Incorrect for this question. Bound the blast radius and the bill at the cost of queueing when the cap is reached. Why the correct answer wins: Lowering concurrency per instance keeps memory inside the limit.

### Question 67 — B, D

Answers: Use API Gateway for the API; Put Apigee in front of the API. The lightweight gateway covers the internal key checks, and the full platform covers the partner programme. A lighter managed gateway for routing and key-based quota enforcement. An API management layer for quotas, keys, mediation and analytics. Local study-map skill 3.4 (API Exposure and Versioning), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 3 (configuring cloud-native applications for deployment): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Keep the old contract working while the new one is adopted. Why the correct answer wins: The lightweight gateway covers the internal key checks, and the full platform covers the partner programme.
- **B:** Correct. An API management layer for quotas, keys, mediation and analytics. In this case: The lightweight gateway covers the internal key checks, and the full platform covers the partner programme.
- **C:** Incorrect for this question. A single anycast address that routes to the nearest healthy backend. Why the correct answer wins: The lightweight gateway covers the internal key checks, and the full platform covers the partner programme.
- **D:** Correct. A lighter managed gateway for routing and key-based quota enforcement. In this case: The lightweight gateway covers the internal key checks, and the full platform covers the partner programme.
- **E:** Incorrect for this question. Accept only traffic from the VPC and internal load balancers. Why the correct answer wins: The lightweight gateway covers the internal key checks, and the full platform covers the partner programme.

### Question 68 — A, C

Answers: Use a rolling update strategy; Add a PodDisruptionBudget. Batched replacement keeps serving, and a disruption budget protects the quorum. Replace pods gradually so the deployment stays available. Limit how many pods may be evicted at once during voluntary disruption. Local study-map skill 3.5 (Deploying Containers to GKE), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 3 (configuring cloud-native applications for deployment): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Correct. Limit how many pods may be evicted at once during voluntary disruption. In this case: Batched replacement keeps serving, and a disruption budget protects the quorum.
- **B:** Incorrect for this question. Place work on nodes whose shape and pricing match the workload. Why the correct answer wins: Batched replacement keeps serving, and a disruption budget protects the quorum.
- **C:** Correct. Replace pods gradually so the deployment stays available. In this case: Batched replacement keeps serving, and a disruption budget protects the quorum.
- **D:** Incorrect for this question. Control how much capacity may be missing while pods are replaced. Why the correct answer wins: Batched replacement keeps serving, and a disruption budget protects the quorum.
- **E:** Incorrect for this question. Use reclaimable capacity for work that can tolerate a node disappearing. Why the correct answer wins: Batched replacement keeps serving, and a disruption budget protects the quorum.

### Question 69 — C

Answer: Constrain pods to the intended node pool. A selector keeps each pod near the cache it reads. Place work on nodes whose shape and pricing match the workload. Local study-map skill 3.5 (Deploying Containers to GKE), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 3 (configuring cloud-native applications for deployment): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Add or remove nodes as pending pods demand capacity. Why the correct answer wins: A selector keeps each pod near the cache it reads.
- **B:** Incorrect for this question. Limit how many pods may be evicted at once during voluntary disruption. Why the correct answer wins: A selector keeps each pod near the cache it reads.
- **C:** Correct. Place work on nodes whose shape and pricing match the workload. In this case: A selector keeps each pod near the cache it reads.
- **D:** Incorrect for this question. Use reclaimable capacity for work that can tolerate a node disappearing. Why the correct answer wins: A selector keeps each pod near the cache it reads.

### Question 70 — C

Answer: Tune maxSurge and maxUnavailable. An unavailable bound caps the pods removed during the release. Control how much capacity may be missing while pods are replaced. Local study-map skill 3.5 (Deploying Containers to GKE), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 3 (configuring cloud-native applications for deployment): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Add or remove nodes as pending pods demand capacity. Why the correct answer wins: An unavailable bound caps the pods removed during the release.
- **B:** Incorrect for this question. Limit how many pods may be evicted at once during voluntary disruption. Why the correct answer wins: An unavailable bound caps the pods removed during the release.
- **C:** Correct. Control how much capacity may be missing while pods are replaced. In this case: An unavailable bound caps the pods removed during the release.
- **D:** Incorrect for this question. Replace pods gradually so the deployment stays available. Why the correct answer wins: An unavailable bound caps the pods removed during the release.

### Question 71 — D

Answer: Configure a startup probe. A startup probe waits for the model to load before checking health. Hold traffic until the application is actually ready to serve. Local study-map skill 3.6 (Kubernetes Health Checks), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 3 (configuring cloud-native applications for deployment): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Remove the instance from the endpoint list while it cannot serve. Why the correct answer wins: A startup probe waits for the model to load before checking health.
- **B:** Incorrect for this question. Limit how many pods may be evicted at once during voluntary disruption. Why the correct answer wins: A startup probe waits for the model to load before checking health.
- **C:** Incorrect for this question. Restart the container when it can no longer make progress. Why the correct answer wins: A startup probe waits for the model to load before checking health.
- **D:** Correct. Hold traffic until the application is actually ready to serve. In this case: A startup probe waits for the model to load before checking health.

### Question 72 — D

Answer: Configure a readiness probe. A readiness probe withholds traffic until the dependency check passes. Remove the instance from the endpoint list while it cannot serve. Local study-map skill 3.6 (Kubernetes Health Checks), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 3 (configuring cloud-native applications for deployment): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Restart the container when it can no longer make progress. Why the correct answer wins: A readiness probe withholds traffic until the dependency check passes.
- **B:** Incorrect for this question. Hold traffic until the application is actually ready to serve. Why the correct answer wins: A readiness probe withholds traffic until the dependency check passes.
- **C:** Incorrect for this question. Limit how many pods may be evicted at once during voluntary disruption. Why the correct answer wins: A readiness probe withholds traffic until the dependency check passes.
- **D:** Correct. Remove the instance from the endpoint list while it cannot serve. In this case: A readiness probe withholds traffic until the dependency check passes.

### Question 73 — D

Answer: Add a PodDisruptionBudget. A disruption budget guarantees the replicas maintenance may leave running. Limit how many pods may be evicted at once during voluntary disruption. Local study-map skill 3.6 (Kubernetes Health Checks), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 3 (configuring cloud-native applications for deployment): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Control how much capacity may be missing while pods are replaced. Why the correct answer wins: A disruption budget guarantees the replicas maintenance may leave running.
- **B:** Incorrect for this question. Remove the instance from the endpoint list while it cannot serve. Why the correct answer wins: A disruption budget guarantees the replicas maintenance may leave running.
- **C:** Incorrect for this question. Let the load balancer stop sending traffic to an unhealthy instance. Why the correct answer wins: A disruption budget guarantees the replicas maintenance may leave running.
- **D:** Correct. Limit how many pods may be evicted at once during voluntary disruption. In this case: A disruption budget guarantees the replicas maintenance may leave running.

### Question 74 — A, C

Answers: Scale pods on CPU utilization; Enable node pool autoscaling. Scaling on utilisation adds pods, and node autoscaling adds the capacity they need. Add pods when average CPU crosses the target. Add or remove nodes as pending pods demand capacity. Local study-map skill 3.7 (Horizontal Pod Autoscaling), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 3 (configuring cloud-native applications for deployment): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Correct. Add or remove nodes as pending pods demand capacity. In this case: Scaling on utilisation adds pods, and node autoscaling adds the capacity they need.
- **B:** Incorrect for this question. Add pods on a signal that tracks demand better than CPU. Why the correct answer wins: Scaling on utilisation adds pods, and node autoscaling adds the capacity they need.
- **C:** Correct. Add pods when average CPU crosses the target. In this case: Scaling on utilisation adds pods, and node autoscaling adds the capacity they need.
- **D:** Incorrect for this question. Keep capacity warm so scale-up does not cost the first requests. Why the correct answer wins: Scaling on utilisation adds pods, and node autoscaling adds the capacity they need.
- **E:** Incorrect for this question. Limit how many pods may be evicted at once during voluntary disruption. Why the correct answer wins: Scaling on utilisation adds pods, and node autoscaling adds the capacity they need.

### Question 75 — D

Answer: Set a minimum replica count. A replica floor keeps the two pods running before the burst. Keep capacity warm so scale-up does not cost the first requests. Local study-map skill 3.7 (Horizontal Pod Autoscaling), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 3 (configuring cloud-native applications for deployment): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Add or remove nodes as pending pods demand capacity. Why the correct answer wins: A replica floor keeps the two pods running before the burst.
- **B:** Incorrect for this question. Limit how many pods may be evicted at once during voluntary disruption. Why the correct answer wins: A replica floor keeps the two pods running before the burst.
- **C:** Incorrect for this question. Add pods on a signal that tracks demand better than CPU. Why the correct answer wins: A replica floor keeps the two pods running before the burst.
- **D:** Correct. Keep capacity warm so scale-up does not cost the first requests. In this case: A replica floor keeps the two pods running before the burst.

### Question 76 — B

Answer: Scale pods on a custom or external metric. A custom metric lets scaling follow the open connection count. Add pods on a signal that tracks demand better than CPU. Local study-map skill 3.7 (Horizontal Pod Autoscaling), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 3 (configuring cloud-native applications for deployment): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Add or remove nodes as pending pods demand capacity. Why the correct answer wins: A custom metric lets scaling follow the open connection count.
- **B:** Correct. Add pods on a signal that tracks demand better than CPU. In this case: A custom metric lets scaling follow the open connection count.
- **C:** Incorrect for this question. Trade a term commitment for a lower unit price on capacity that never idles. Why the correct answer wins: A custom metric lets scaling follow the open connection count.
- **D:** Incorrect for this question. Add pods when average CPU crosses the target. Why the correct answer wins: A custom metric lets scaling follow the open connection count.

### Question 77 — D

Answer: Deploy the handler as a Cloud Functions function. A function runtime runs the handler with no container to build. An event-triggered function runtime for a single-purpose handler rather than a long-lived service. Local study-map skill 3.2 (Cloud Run Triggers and Event Receivers), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 3 (configuring cloud-native applications for deployment): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A managed container runtime that scales to zero and bills per request while it serves traffic. Why the correct answer wins: A function runtime runs the handler with no container to build.
- **B:** Incorrect for this question. Virtual machines where the operating system, runtime and scaling group are all managed by the team. Why the correct answer wins: A function runtime runs the handler with no container to build.
- **C:** Incorrect for this question. A managed Kubernetes control plane where pods, node pools and cluster-scoped policy are yours to configure. Why the correct answer wins: A function runtime runs the handler with no container to build.
- **D:** Correct. An event-triggered function runtime for a single-purpose handler rather than a long-lived service. In this case: A function runtime runs the handler with no container to build.

### Question 78 — A

Answer: Introduce a new API version alongside the old one. Running the new version alongside lets the old one be retired later. Keep the old contract working while the new one is adopted. Local study-map skill 3.4 (API Exposure and Versioning), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 3 (configuring cloud-native applications for deployment): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Correct. Keep the old contract working while the new one is adopted. In this case: Running the new version alongside lets the old one be retired later.
- **B:** Incorrect for this question. A machine-readable contract that generates clients and validates requests. Why the correct answer wins: Running the new version alongside lets the old one be retired later.
- **C:** Incorrect for this question. An API management layer for quotas, keys, mediation and analytics. Why the correct answer wins: Running the new version alongside lets the old one be retired later.
- **D:** Incorrect for this question. Extend the contract so existing clients keep working unchanged. Why the correct answer wins: Running the new version alongside lets the old one be retired later.

### Question 79 — A

Answer: Run the batch node pool on Spot VMs. Interruptible nodes host the workers that can checkpoint. Use reclaimable capacity for work that can tolerate a node disappearing. Local study-map skill 3.5 (Deploying Containers to GKE), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 3 (configuring cloud-native applications for deployment): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Correct. Use reclaimable capacity for work that can tolerate a node disappearing. In this case: Interruptible nodes host the workers that can checkpoint.
- **B:** Incorrect for this question. Add or remove nodes as pending pods demand capacity. Why the correct answer wins: Interruptible nodes host the workers that can checkpoint.
- **C:** Incorrect for this question. Limit how many pods may be evicted at once during voluntary disruption. Why the correct answer wins: Interruptible nodes host the workers that can checkpoint.
- **D:** Incorrect for this question. Place work on nodes whose shape and pricing match the workload. Why the correct answer wins: Interruptible nodes host the workers that can checkpoint.

### Question 80 — A

Answer: Connect through the Cloud SQL Auth Proxy. A proxy provides the private path for that language. A local proxy that authorizes the connection with IAM and encrypts it. Local study-map skill 4.1 (Connecting to Datastores), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 4 (integrating applications with Google Cloud services): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Correct. A local proxy that authorizes the connection with IAM and encrypts it. In this case: A proxy provides the private path for that language.
- **B:** Incorrect for this question. A client library that resolves and authorizes the instance itself. Why the correct answer wins: A proxy provides the private path for that language.
- **C:** Incorrect for this question. A private endpoint that consumes a published service without peering. Why the correct answer wins: A proxy provides the private path for that language.
- **D:** Incorrect for this question. The equivalent authorized connector for AlloyDB instances. Why the correct answer wins: A proxy provides the private path for that language.

### Question 81 — D

Answer: Pool and reuse database connections. A pool shares a bounded set of sessions across the instances. Keep a small set of warm connections instead of opening one per request. Local study-map skill 4.1 (Connecting to Datastores), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 4 (integrating applications with Google Cloud services): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A private endpoint that consumes a published service without peering. Why the correct answer wins: A pool shares a bounded set of sessions across the instances.
- **B:** Incorrect for this question. Allow the process the headroom it needs so it is not throttled or killed. Why the correct answer wins: A pool shares a bounded set of sessions across the instances.
- **C:** Incorrect for this question. Change the engine-level connection limit without resizing the machine. Why the correct answer wins: A pool shares a bounded set of sessions across the instances.
- **D:** Correct. Keep a small set of warm connections instead of opening one per request. In this case: A pool shares a bounded set of sessions across the instances.

### Question 82 — C

Answer: Connect through the AlloyDB Auth Proxy. The proxy renews certificates without the client restarting. The equivalent authorized connector for AlloyDB instances. Local study-map skill 4.1 (Connecting to Datastores), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 4 (integrating applications with Google Cloud services): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A client library that resolves and authorizes the instance itself. Why the correct answer wins: The proxy renews certificates without the client restarting.
- **B:** Incorrect for this question. A private endpoint that consumes a published service without peering. Why the correct answer wins: The proxy renews certificates without the client restarting.
- **C:** Correct. The equivalent authorized connector for AlloyDB instances. In this case: The proxy renews certificates without the client restarting.
- **D:** Incorrect for this question. A local proxy that authorizes the connection with IAM and encrypts it. Why the correct answer wins: The proxy renews certificates without the client restarting.

### Question 83 — B

Answer: Connect over the database private IP. A private address keeps administrators on the internal path. A private address reachable from the VPC without a proxy process. Local study-map skill 4.1 (Connecting to Datastores), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 4 (integrating applications with Google Cloud services): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A reachable address that requires encrypted connections from any client. Why the correct answer wins: A private address keeps administrators on the internal path.
- **B:** Correct. A private address reachable from the VPC without a proxy process. In this case: A private address keeps administrators on the internal path.
- **C:** Incorrect for this question. A private endpoint that consumes a published service without peering. Why the correct answer wins: A private address keeps administrators on the internal path.
- **D:** Incorrect for this question. A client library that resolves and authorizes the instance itself. Why the correct answer wins: A private address keeps administrators on the internal path.

### Question 84 — B

Answer: Raise the database connection ceiling by flag. Capping sessions per task stops one task taking the instance. Change the engine-level connection limit without resizing the machine. Local study-map skill 4.1 (Connecting to Datastores), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 4 (integrating applications with Google Cloud services): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Allow the process the headroom it needs so it is not throttled or killed. Why the correct answer wins: Capping sessions per task stops one task taking the instance.
- **B:** Correct. Change the engine-level connection limit without resizing the machine. In this case: Capping sessions per task stops one task taking the instance.
- **C:** Incorrect for this question. Keep a small set of warm connections instead of opening one per request. Why the correct answer wins: Capping sessions per task stops one task taking the instance.
- **D:** Incorrect for this question. A private endpoint that consumes a published service without peering. Why the correct answer wins: Capping sessions per task stops one task taking the instance.

### Question 85 — C

Answer: Have the worker pull from the subscription. Pull delivery lets the consumer slow its own fetching. The consumer controls the pace and acknowledges messages itself. Local study-map skill 4.2 (Publishing and Consuming Messages), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 4 (integrating applications with Google Cloud services): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A task queue with retries and rate control aimed at a specific target. Why the correct answer wins: Pull delivery lets the consumer slow its own fetching.
- **B:** Incorrect for this question. Push each message to an endpoint instead of having the consumer pull. Why the correct answer wins: Pull delivery lets the consumer slow its own fetching.
- **C:** Correct. The consumer controls the pace and acknowledges messages itself. In this case: Pull delivery lets the consumer slow its own fetching.
- **D:** Incorrect for this question. A trigger path that turns a Cloud Audit Log or resource event into a delivery. Why the correct answer wins: Pull delivery lets the consumer slow its own fetching.

### Question 86 — B

Answer: Deliver to an HTTPS push subscription. Push delivery retries against the endpoint on the subscription's behalf. Push each message to an endpoint instead of having the consumer pull. Local study-map skill 4.2 (Publishing and Consuming Messages), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 4 (integrating applications with Google Cloud services): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A task queue with retries and rate control aimed at a specific target. Why the correct answer wins: Push delivery retries against the endpoint on the subscription's behalf.
- **B:** Correct. Push each message to an endpoint instead of having the consumer pull. In this case: Push delivery retries against the endpoint on the subscription's behalf.
- **C:** Incorrect for this question. A trigger path that turns a Cloud Audit Log or resource event into a delivery. Why the correct answer wins: Push delivery retries against the endpoint on the subscription's behalf.
- **D:** Incorrect for this question. The consumer controls the pace and acknowledges messages itself. Why the correct answer wins: Push delivery retries against the endpoint on the subscription's behalf.

### Question 87 — C

Answer: Add a dead-letter topic. A dead-letter topic parks the failing messages for inspection. Hold messages that exhausted their delivery attempts for later inspection. Local study-map skill 4.2 (Publishing and Consuming Messages), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 4 (integrating applications with Google Cloud services): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Space out repeated attempts so a throttled quota can recover instead of being hammered. Why the correct answer wins: A dead-letter topic parks the failing messages for inspection.
- **B:** Incorrect for this question. Make the retention period impossible to shorten, even by an owner. Why the correct answer wins: A dead-letter topic parks the failing messages for inspection.
- **C:** Correct. Hold messages that exhausted their delivery attempts for later inspection. In this case: A dead-letter topic parks the failing messages for inspection.
- **D:** Incorrect for this question. Recognise a repeated delivery and skip the duplicate work. Why the correct answer wins: A dead-letter topic parks the failing messages for inspection.

### Question 88 — A

Answer: Publish the event to a Pub/Sub topic. A topic fans the event out to subscribers the publisher never names. A durable, at-least-once message channel with independent subscribers. Local study-map skill 4.2 (Publishing and Consuming Messages), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 4 (integrating applications with Google Cloud services): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Correct. A durable, at-least-once message channel with independent subscribers. In this case: A topic fans the event out to subscribers the publisher never names.
- **B:** Incorrect for this question. A task queue with retries and rate control aimed at a specific target. Why the correct answer wins: A topic fans the event out to subscribers the publisher never names.
- **C:** Incorrect for this question. A trigger path that turns a Cloud Audit Log or resource event into a delivery. Why the correct answer wins: A topic fans the event out to subscribers the publisher never names.
- **D:** Incorrect for this question. A stateful sequence of service calls with retries and error branches. Why the correct answer wins: A topic fans the event out to subscribers the publisher never names.

### Question 89 — C, D

Answers: Retry with exponential backoff and jitter; Follow the page token until results are exhausted. Retrying with backoff survives throttling, and following page tokens reaches every result. Space out repeated attempts so a throttled quota can recover instead of being hammered. Request each page in turn so a truncated response is completed rather than assumed whole. Local study-map skill 4.3 (Calling Google Cloud APIs), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 4 (integrating applications with Google Cloud services): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Reuse a result that has not changed, avoiding an identical call. Why the correct answer wins: Retrying with backoff survives throttling, and following page tokens reaches every result.
- **B:** Incorrect for this question. Reduce per-call overhead when the API supports a batch surface. Why the correct answer wins: Retrying with backoff survives throttling, and following page tokens reaches every result.
- **C:** Correct. Request each page in turn so a truncated response is completed rather than assumed whole. In this case: Retrying with backoff survives throttling, and following page tokens reaches every result.
- **D:** Correct. Space out repeated attempts so a throttled quota can recover instead of being hammered. In this case: Retrying with backoff survives throttling, and following page tokens reaches every result.
- **E:** Incorrect for this question. Trim the response payload so latency and cost follow actual use. Why the correct answer wins: Retrying with backoff survives throttling, and following page tokens reaches every result.

### Question 90 — D

Answer: Batch many small calls into one request. Batching the lookups collapses them into fewer calls. Reduce per-call overhead when the API supports a batch surface. Local study-map skill 4.3 (Calling Google Cloud APIs), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 4 (integrating applications with Google Cloud services): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Request each page in turn so a truncated response is completed rather than assumed whole. Why the correct answer wins: Batching the lookups collapses them into fewer calls.
- **B:** Incorrect for this question. Trim the response payload so latency and cost follow actual use. Why the correct answer wins: Batching the lookups collapses them into fewer calls.
- **C:** Incorrect for this question. Reuse a result that has not changed, avoiding an identical call. Why the correct answer wins: Batching the lookups collapses them into fewer calls.
- **D:** Correct. Reduce per-call overhead when the API supports a batch surface. In this case: Batching the lookups collapses them into fewer calls.

### Question 91 — B

Answer: Request only the fields the caller needs. A field mask limits the response to the fields shown. Trim the response payload so latency and cost follow actual use. Local study-map skill 4.3 (Calling Google Cloud APIs), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 4 (integrating applications with Google Cloud services): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Request each page in turn so a truncated response is completed rather than assumed whole. Why the correct answer wins: A field mask limits the response to the fields shown.
- **B:** Correct. Trim the response payload so latency and cost follow actual use. In this case: A field mask limits the response to the fields shown.
- **C:** Incorrect for this question. Reduce per-call overhead when the API supports a batch surface. Why the correct answer wins: A field mask limits the response to the fields shown.
- **D:** Incorrect for this question. Reuse a result that has not changed, avoiding an identical call. Why the correct answer wins: A field mask limits the response to the fields shown.

### Question 92 — A

Answer: Give the workload its own service account. A dedicated identity per job makes each action attributable. A dedicated identity whose roles can be granted and revoked independently. Local study-map skill 4.4 (Service Accounts for API Calls), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 4 (integrating applications with Google Cloud services): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Correct. A dedicated identity whose roles can be granted and revoked independently. In this case: A dedicated identity per job makes each action attributable.
- **B:** Incorrect for this question. The automatically created identity that usually carries broad project access. Why the correct answer wins: A dedicated identity per job makes each action attributable.
- **C:** Incorrect for this question. A legacy broad role that can change most resources in the project. Why the correct answer wins: A dedicated identity per job makes each action attributable.
- **D:** Incorrect for this question. A role built from an explicit permission list. Why the correct answer wins: A dedicated identity per job makes each action attributable.

### Question 93 — C

Answer: Federate the external identity with Workload Identity Federation. Federating the issuer trades its token for short-lived access. Exchange an outside token for a short-lived Google credential. Local study-map skill 4.4 (Service Accounts for API Calls), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 4 (integrating applications with Google Cloud services): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A long-lived credential that has to be stored and rotated by hand. Why the correct answer wins: Federating the issuer trades its token for short-lived access.
- **B:** Incorrect for this question. A dedicated identity whose roles can be granted and revoked independently. Why the correct answer wins: Federating the issuer trades its token for short-lived access.
- **C:** Correct. Exchange an outside token for a short-lived Google credential. In this case: Federating the issuer trades its token for short-lived access.
- **D:** Incorrect for this question. Let the client library find credentials from the environment. Why the correct answer wins: Federating the issuer trades its token for short-lived access.

### Question 94 — B

Answer: Emit a custom metric from the code. A user-defined metric carries the ratio nothing emits. Publish an application signal that infrastructure metrics cannot see. Local study-map skill 4.5 (Metrics, Logs, and Traces), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 4 (integrating applications with Google Cloud services): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Let filters and alerting distinguish routine output from errors. Why the correct answer wins: A user-defined metric carries the ratio nothing emits.
- **B:** Correct. Publish an application signal that infrastructure metrics cannot see. In this case: A user-defined metric carries the ratio nothing emits.
- **C:** Incorrect for this question. Turn a recurring log pattern into a number that can be charted and alerted on. Why the correct answer wins: A user-defined metric carries the ratio nothing emits.
- **D:** Incorrect for this question. Notify a human when a threshold is crossed. Why the correct answer wins: A user-defined metric carries the ratio nothing emits.

### Question 95 — B

Answer: Emit structured JSON logs. Structured fields make the entries searchable by those values. Emit fields the log viewer can index so queries and alerts are possible. Local study-map skill 4.5 (Metrics, Logs, and Traces), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 4 (integrating applications with Google Cloud services): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Turn a recurring log pattern into a number that can be charted and alerted on. Why the correct answer wins: Structured fields make the entries searchable by those values.
- **B:** Correct. Emit fields the log viewer can index so queries and alerts are possible. In this case: Structured fields make the entries searchable by those values.
- **C:** Incorrect for this question. Let filters and alerting distinguish routine output from errors. Why the correct answer wins: Structured fields make the entries searchable by those values.
- **D:** Incorrect for this question. Group and count application errors instead of grepping logs. Why the correct answer wins: Structured fields make the entries searchable by those values.

### Question 96 — A

Answer: Alert on the error budget burn rate. Alerting on budget burn pages on the reliability users feel. Page on the rate at which reliability is being spent. Local study-map skill 4.5 (Metrics, Logs, and Traces), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 4 (integrating applications with Google Cloud services): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Correct. Page on the rate at which reliability is being spent. In this case: Alerting on budget burn pages on the reliability users feel.
- **B:** Incorrect for this question. Notify a human when a threshold is crossed. Why the correct answer wins: Alerting on budget burn pages on the reliability users feel.
- **C:** Incorrect for this question. Publish an application signal that infrastructure metrics cannot see. Why the correct answer wins: Alerting on budget burn pages on the reliability users feel.
- **D:** Incorrect for this question. Let filters and alerting distinguish routine output from errors. Why the correct answer wins: Alerting on budget burn pages on the reliability users feel.

### Question 97 — A, C

Answers: Send the exception to Error Reporting; Propagate the trace ID between services. Grouping surfaces new exception groups, and propagating the trace header joins the logs. Group and count application errors instead of grepping logs. Join spans from different services into one trace. Local study-map skill 4.6 (Error Reporting and Trace Correlation), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 4 (integrating applications with Google Cloud services): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Correct. Join spans from different services into one trace. In this case: Grouping surfaces new exception groups, and propagating the trace header joins the logs.
- **B:** Incorrect for this question. Let filters and alerting distinguish routine output from errors. Why the correct answer wins: Grouping surfaces new exception groups, and propagating the trace header joins the logs.
- **C:** Correct. Group and count application errors instead of grepping logs. In this case: Grouping surfaces new exception groups, and propagating the trace header joins the logs.
- **D:** Incorrect for this question. Notify a human when a threshold is crossed. Why the correct answer wins: Grouping surfaces new exception groups, and propagating the trace header joins the logs.
- **E:** Incorrect for this question. Show where time goes inside a request that crosses services. Why the correct answer wins: Grouping surfaces new exception groups, and propagating the trace header joins the logs.

### Question 98 — D

Answer: Instrument a span around the downstream call. A span per call records each call's share of the latency. Show where time goes inside a request that crosses services. Local study-map skill 4.6 (Error Reporting and Trace Correlation), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 4 (integrating applications with Google Cloud services): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Turn a recurring log pattern into a number that can be charted and alerted on. Why the correct answer wins: A span per call records each call's share of the latency.
- **B:** Incorrect for this question. Notify a human when a threshold is crossed. Why the correct answer wins: A span per call records each call's share of the latency.
- **C:** Incorrect for this question. Join spans from different services into one trace. Why the correct answer wins: A span per call records each call's share of the latency.
- **D:** Correct. Show where time goes inside a request that crosses services. In this case: A span per call records each call's share of the latency.

### Question 99 — C

Answer: Ask Gemini Cloud Assist for a diagnosis. An AI assistant explains the alert and drafts the query. An assistant that reads telemetry and proposes a cause and a next step. Local study-map skill 4.7 (AI-Assisted Observability), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 4 (integrating applications with Google Cloud services): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Give the assistant a defined tool surface instead of pasting context by hand. Why the correct answer wins: An AI assistant explains the alert and drafts the query.
- **B:** Incorrect for this question. Group and count application errors instead of grepping logs. Why the correct answer wins: An AI assistant explains the alert and drafts the query.
- **C:** Correct. An assistant that reads telemetry and proposes a cause and a next step. In this case: An AI assistant explains the alert and drafts the query.
- **D:** Incorrect for this question. Generate a first draft from context, then review and correct it. Why the correct answer wins: An AI assistant explains the alert and drafts the query.

### Question 100 — B

Answer: Cache the response for its freshness window. Caching the response avoids refetching data that changed an hour ago. Reuse a result that has not changed, avoiding an identical call. Local study-map skill 4.3 (Calling Google Cloud APIs), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 4 (integrating applications with Google Cloud services): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Reduce per-call overhead when the API supports a batch surface. Why the correct answer wins: Caching the response avoids refetching data that changed an hour ago.
- **B:** Correct. Reuse a result that has not changed, avoiding an identical call. In this case: Caching the response avoids refetching data that changed an hour ago.
- **C:** Incorrect for this question. Request each page in turn so a truncated response is completed rather than assumed whole. Why the correct answer wins: Caching the response avoids refetching data that changed an hour ago.
- **D:** Incorrect for this question. Trim the response payload so latency and cost follow actual use. Why the correct answer wins: Caching the response avoids refetching data that changed an hour ago.
