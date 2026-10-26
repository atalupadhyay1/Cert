# Google Cloud Professional Cloud Developer — Full-Length Mock Exam 4

Professional Cloud Developer · 100 questions · expanded practice bank · passing score not published

Blueprint-weighted mock exam. Item mix: 84 multiple-choice and 16 multiple-select items (the selection count is stated in each multi-select stem). The live exam publishes 50-60 multiple-choice and multiple-select questions and has no case-study component, so this set is larger on purpose and no case-study item is reproduced. The live paper allows two hours for 50-60 items, so this 100-item set is a slower-per-item rehearsal: about 72 seconds per item here against roughly 120-144 seconds live. Use it to build a habit of finishing with time to review. See the README for the exact fidelity boundary.

Original educational content, not actual, recalled, or copied Google exam items.

## Questions

---

## Domain 1 — Designing Highly Scalable, Secure, and Reliable Cloud-Native Applications (Compute Choice, APIs, and Secure Design)

### 1. A maintenance script fires on a bucket event twice a day and nobody wants to manage a server for it. Which platform fits?

- A. Run the application on Compute Engine instances
- B. Deploy the handler as a Cloud Functions function
- C. Deploy the workload to Google Kubernetes Engine
- D. Deploy the service to Cloud Run

### 2. A container image already exists and must serve HTTP while scaling to zero between bursts. Which platform fits?

- A. Deploy to App Engine standard
- B. Deploy the handler as a Cloud Functions function
- C. Deploy the service to Cloud Run
- D. Run the application on Compute Engine instances

### 3. Many product teams must share one cluster with a mesh, custom controllers and namespace quotas. Which platform fits?

- A. Deploy the service to Cloud Run
- B. Deploy to App Engine standard
- C. Deploy the handler as a Cloud Functions function
- D. Deploy the workload to Google Kubernetes Engine

### 4. A legacy app writes uploads to the pod's local disk and reads them on the next request. What must be changed before it scales horizontally?

- A. Cache inside each instance process
- B. Enable session affinity on the backend service
- C. Use a generated cookie for stickiness
- D. Store session state in a shared datastore

### 5. A trading front end must keep serving through the loss of a whole region and stop sending traffic to it. Which two designs fit? Select two.

- A. Deploy the service in two regions behind a global load balancer
- B. Serve static content from Cloud CDN
- C. Add a health check endpoint to the backend service
- D. Place the workload in a single zone
- E. Deploy in one region across multiple zones

### 6. A single database host in one zone took the product down for forty minutes. What was the design mistake?

- A. Deploy in one region across multiple zones
- B. Deploy the service in two regions behind a global load balancer
- C. Place the workload in a single zone
- D. Buy committed use discounts for the steady baseline

### 7. Shoppers on three continents need the nearest front door, and an interim cart view must stay on the instance that built it. Which two fit? Select two.

- A. Serve static content from Cloud CDN
- B. Use a regional load balancer
- C. Put a global external Application Load Balancer in front
- D. Enable session affinity on the backend service
- E. Store session state in a shared datastore

### 8. A load balancer must pin a browser to one backend using a value it issues itself. What should be enabled?

- A. Store session state in a shared datastore
- B. Use a generated cookie for stickiness
- C. Put a global external Application Load Balancer in front
- D. Enable session affinity on the backend service

### 9. Two services must share a distributed lock and acquire it in about a millisecond. What should they use?

- A. Cache inside each instance process
- B. Serve static content from Cloud CDN
- C. Load through a cache-aside pattern
- D. Cache reads in Memorystore

### 10. A price correction is live in the database but shoppers still see yesterday's value. What is missing?

- A. Load through a cache-aside pattern
- B. Invalidate the cache on write
- C. Add a lifecycle rule to the bucket
- D. Serve static content from Cloud CDN

### 11. Internal services need high-throughput typed calls, and a mobile app needs plain HTTP it can cache at the edge. Which two interfaces fit? Select two.

- A. Expose a gRPC service
- B. Serve gRPC-Web for browser clients
- C. Expose a REST API with JSON payloads
- D. Batch many small calls into one request
- E. Publish an OpenAPI specification

### 12. A browser client must speak the binary RPC protocol without a translation proxy in front of it. Which variant fits?

- A. Expose a gRPC service
- B. Serve gRPC-Web for browser clients
- C. Publish an OpenAPI specification
- D. Expose a REST API with JSON payloads

### 13. Each enterprise customer buys a monthly allowance of four million calls. What should be configured?

- A. Set a quota per API key
- B. Introduce a new API version alongside the old one
- C. Apply a rate limit per client key
- D. Use API Gateway for the API

### 14. A client still sends a field the service stopped reading, and the request must not fail. What property is required?

- A. Introduce a new API version alongside the old one
- B. Publish an OpenAPI specification
- C. Request only the fields the caller needs
- D. Add the field in a backward-compatible way

### 15. A build must start when a commit lands in the connected repository. What should route the event?

- A. Orchestrate the steps in Workflows
- B. Schedule the invocation with Cloud Scheduler
- C. Route the event with Eventarc
- D. Queue the work as a Cloud Tasks task

### 16. A nine-step order saga must show where each order stopped and retry only the failed step. What should own it?

- A. Orchestrate the steps in Workflows
- B. Queue the work as a Cloud Tasks task
- C. Schedule the invocation with Cloud Scheduler
- D. Publish the event to a Pub/Sub topic

### 17. Pods reserve triple what they measure, and a stable baseline will run for three years. Which two actions cut the bill? Select two.

- A. Set CPU and memory requests from measured use
- B. Constrain pods to the intended node pool
- C. Run the batch node pool on Spot VMs
- D. Buy committed use discounts for the steady baseline
- E. Raise the container limits above the observed peak

### 18. A rendering job must land only on nodes that carry the accelerator it needs. What should be configured?

- A. Enable node pool autoscaling
- B. Constrain pods to the intended node pool
- C. Run the batch node pool on Spot VMs
- D. Buy committed use discounts for the steady baseline

### 19. A new revision must take a rising share of live traffic on the same hostname. What should be configured?

- A. Split traffic between revisions by percentage
- B. Route by revision tag or header
- C. Shift traffic back to the previous revision
- D. Canary the release at a small percentage first

### 20. A release must be judged on the error rate of a small slice before everyone gets it. Which pattern applies?

- A. Shift traffic back to the previous revision
- B. Canary the release at a small percentage first
- C. Gate the change behind a feature flag
- D. Split traffic between revisions by percentage

### 21. Mutual TLS, retries and timeouts must apply across services without changing their code. What should be introduced?

- A. Orchestrate the steps in Workflows
- B. Queue the work as a Cloud Tasks task
- C. Use Cloud Service Mesh for service-to-service traffic
- D. Use API Gateway for the API

### 22. A regulator requires that archived records cannot be deleted or have their retention shortened for seven years. What should be set?

- A. Lock the bucket retention policy
- B. Make the bucket public
- C. Issue a signed URL with a short expiry
- D. Add a lifecycle rule to the bucket

### 23. Credentials must keep version history, and the stored payloads must be encrypted with a key the team controls. Which two fit? Select two.

- A. Mount the secret as a volume
- B. Store the credential in Secret Manager
- C. Set the credential as an environment variable
- D. Download a service account key file
- E. Use a customer-managed encryption key

### 24. A runtime must read a credential from a file path so it never appears in the environment. What should be configured?

- A. Mount the secret as a volume
- B. Download a service account key file
- C. Use a customer-managed encryption key
- D. Set the credential as an environment variable

### 25. A backend must verify that a request passed the proxy and belongs to the named user. What should it validate?

- A. Use Identity Platform for end-user sign-in
- B. Rely on Application Default Credentials
- C. Give the workload its own service account
- D. Validate the signed JWT from the proxy

### 26. A retailer will not store customer passwords but must issue and refresh tokens for its shopping app. What should it adopt?

- A. Give the workload its own service account
- B. Federate the external identity with Workload Identity Federation
- C. Validate the signed JWT from the proxy
- D. Use Identity Platform for end-user sign-in

### 27. Pods must accept traffic only from the namespace's front end. What should be defined?

- A. Allow unauthenticated invocations
- B. Set a namespace resource quota
- C. Apply a Kubernetes NetworkPolicy
- D. Put Identity-Aware Proxy in front of the service

### 28. A function's identity can delete every bucket in the project. What principle was violated?

- A. Grant the basic editor role
- B. Give the workload its own service account
- C. Define a custom role for the narrow permission set
- D. Grant only the roles the workload needs

### 29. One ledger needs strongly consistent global transactions, and another system needs millions of writes per second looked up by device id. Which two fit? Select two.

- A. Store the ledger in Spanner
- B. Design the row key for the read pattern
- C. Store the objects in Cloud Storage
- D. Cache reads in Memorystore
- E. Use Firestore in Native mode

### 30. A mobile app needs offline writes that sync on reconnect and live queries over documents. Which store fits?

- A. Store the ledger in Spanner
- B. Cache reads in Memorystore
- C. Design the row key for the read pattern
- D. Use Firestore in Native mode

### 31. A marketing site serves logo files to anonymous visitors and needs nothing secret. What fits?

- A. Make the bucket public
- B. Lock the bucket retention policy
- C. Add a lifecycle rule to the bucket
- D. Issue a signed URL with a short expiry

### 32. A nightly scoring job outside Google Cloud needs the whole previous day as files. What should the pipeline do?

- A. Stream the events into BigQuery
- B. Use a BigQuery subscription on the topic
- C. Store the objects in Cloud Storage
- D. Export the batch to BigQuery

---

## Domain 2 — Building and Testing Applications (Development Environments, Builds, and Tests)

### 33. Developers need a local substitute that speaks the message protocol, and a standard image for every laptop. Which two fit? Select two.

- A. Inspect the live process with Cloud Debugger
- B. Use Cloud Shell for the session
- C. Use Cloud Workstations for the environment
- D. Develop with Cloud Code in the IDE
- E. Run the service emulator locally

### 34. On-call needs a shell with the SDK preinstalled during an incident, from any machine. What fits?

- A. Use Cloud Shell for the session
- B. Use Cloud Workstations for the environment
- C. Run the service emulator locally
- D. Develop with Cloud Code in the IDE

### 35. A developer wants an explanation of an unfamiliar stack trace inside the editor. What fits?

- A. Connect the assistant to an MCP server
- B. Ask Gemini Cloud Assist for a diagnosis
- C. Develop with Cloud Code in the IDE
- D. Use an AI coding assistant to draft the tests

### 36. An assistant must query the project's tracker through a documented tool interface instead of pasted text. What should be stood up?

- A. Use Cloud Shell for the session
- B. Develop with Cloud Code in the IDE
- C. Ask Gemini Cloud Assist for a diagnosis
- D. Connect the assistant to an MCP server

### 37. A reviewer with a four-hundred-line diff wants a first pass of review comments. What should be used?

- A. Ask Gemini Cloud Assist for a diagnosis
- B. Connect the assistant to an MCP server
- C. Use Cloud Workstations for the environment
- D. Use an AI coding assistant to draft the tests

### 38. Every merge must build automatically in a clean environment with no laptop involved. Which two fit? Select two.

- A. Package the monolith into a container image
- B. Trigger the build from a repository push
- C. Keep building the image by hand
- D. Build the image with Cloud Build
- E. Deploy a pinned image digest

### 39. A pipeline should build the service from its repository without anyone maintaining a Dockerfile. What should it use?

- A. Deploy a pinned image digest
- B. Deploy from source and let the platform build it
- C. Keep building the image by hand
- D. Package the monolith into a container image

### 40. Staging has been verified, and production must run bit-for-bit the same artifact. What should be promoted?

- A. Package the monolith into a container image
- B. Deploy from source and let the platform build it
- C. Deploy a pinned image digest
- D. Keep building the image by hand

### 41. Images for the EU must sit in an EU region while keeping the same repository name. What should hold them?

- A. Build the image with Cloud Build
- B. Push the image to Artifact Registry
- C. Push the image to Container Registry
- D. Store the objects in Cloud Storage

### 42. Helm charts and threat models must be versioned and pulled by the cluster. Where should they live?

- A. Push the image to Container Registry
- B. Store the objects in Cloud Storage
- C. Build the image with Cloud Build
- D. Push the image to Artifact Registry

### 43. An older cluster still resolves its image paths through the legacy host during a migration. What must stay available?

- A. Push the image to Container Registry
- B. Build the image with Cloud Build
- C. Push the image to Artifact Registry
- D. Store the objects in Cloud Storage

### 44. A customer audit asks for a software bill of materials for a running image. What provides it?

- A. Review the finding in Security Command Center
- B. Generate build provenance in Cloud Build
- C. Scan the image with Artifact Analysis
- D. Enforce admission with Binary Authorization

### 45. An emergency image must be admitted once, by exception, while the policy stays enforced for everyone else. What handles it?

- A. Generate build provenance in Cloud Build
- B. Review the finding in Security Command Center
- C. Scan the image with Artifact Analysis
- D. Enforce admission with Binary Authorization

### 46. An auditor asks which commit and which builder produced a running image. What answers that?

- A. Scan the image with Artifact Analysis
- B. Require a higher supply-chain level before release
- C. Enforce admission with Binary Authorization
- D. Generate build provenance in Cloud Build

### 47. A test fails one run in five and the team must also prove each branch of a parser cheaply. Which two fit? Select two.

- A. Load-test the release before the rollout
- B. Run an integration test against the emulator
- C. Add a unit test with dependencies stubbed
- D. Block the deploy on the test result
- E. Quarantine the flaky test and fix it

### 48. A release must not proceed while the suite is red. What should be added?

- A. Load-test the release before the rollout
- B. Run an integration test against the emulator
- C. Block the deploy on the test result
- D. Quarantine the flaky test and fix it

### 49. A failing assertion must let the developer inspect the variables at that moment. What should be used?

- A. Inspect the live process with Cloud Debugger
- B. Profile the service with Cloud Profiler
- C. Add a unit test with dependencies stubbed
- D. Send the exception to Error Reporting

### 50. The gate must exercise the real broker and prove the holiday peak. Which two runs fit? Select two.

- A. Run an integration test against the emulator
- B. Load-test the release before the rollout
- C. Profile the service with Cloud Profiler
- D. Add a unit test with dependencies stubbed
- E. Run the service emulator locally

### 51. A profile is needed of where a multi-service run spends its CPU, per function. What should be used?

- A. Send the exception to Error Reporting
- B. Load-test the release before the rollout
- C. Instrument a span around the downstream call
- D. Profile the service with Cloud Profiler

### 52. The vendor sandbox is unreachable, and the pipeline still needs a service that speaks the same protocol. What should it start?

- A. Load-test the release before the rollout
- B. Profile the service with Cloud Profiler
- C. Run an integration test against the emulator
- D. Run the service emulator locally

### 53. The suite passes locally but is never executed before an image is promoted. What should the pipeline do?

- A. Quarantine the flaky test and fix it
- B. Block the deploy on the test result
- C. Run the tests as a Cloud Build step
- D. Load-test the release before the rollout

### 54. Two engineers in different countries must pair inside a workspace where the repository already builds. What fits?

- A. Use Cloud Shell for the session
- B. Develop with Cloud Code in the IDE
- C. Run the service emulator locally
- D. Use Cloud Workstations for the environment

### 55. An engineer working directly against the cluster wants each save to rebuild and redeploy. What fits?

- A. Build the image with Cloud Build
- B. Iterate with Skaffold
- C. Deploy a pinned image digest
- D. Keep building the image by hand

---

## Domain 3 — Configuring Cloud-Native Applications for Deployment (Cloud Run and GKE Deployment Configuration)

### 56. A team wants the runtime to build the repository itself, and a declared pipeline to keep that build reproducible. Which two fit? Select two.

- A. Build the image with Cloud Build
- B. Deploy a pinned image digest
- C. Deploy from source and let the platform build it
- D. Package the monolith into a container image
- E. Keep building the image by hand

### 57. A service streaming a large download is throttled part way through once the response has started. What should be configured?

- A. Keep a minimum number of instances warm
- B. Raise the per-instance concurrency limit
- C. Enable CPU boost at startup
- D. Use request-based billing

### 58. A traffic spike quadrupled the fleet and the month's bill with it. What should be set before the next campaign?

- A. Raise the container limits above the observed peak
- B. Cap the maximum instance count
- C. Use request-based billing
- D. Buy committed use discounts for the steady baseline

### 59. A schema backfill takes ninety minutes and must run exactly once rather than answer requests. What fits?

- A. Deploy the service to Cloud Run
- B. Route the event with Eventarc
- C. Run the batch work as a Cloud Run job
- D. Deploy the handler as a Cloud Functions function

### 60. An event receiver returns permission denied although users call the same service successfully. What should be granted?

- A. Allow unauthenticated invocations
- B. Put Identity-Aware Proxy in front of the service
- C. Grant the invoker role to the calling identity
- D. Use API Gateway for the API

### 61. A receiver must fetch messages itself so it never exceeds its own concurrency limit. Which delivery fits?

- A. Route the event with Eventarc
- B. Schedule the invocation with Cloud Scheduler
- C. Deliver to an HTTPS push subscription
- D. Have the worker pull from the subscription

### 62. A receiver must start when an audit-log entry for a resource deletion appears. What should route it?

- A. Schedule the invocation with Cloud Scheduler
- B. Queue the work as a Cloud Tasks task
- C. Route the event with Eventarc
- D. Orchestrate the steps in Workflows

### 63. A partner rejects calls above five per second, and the service must queue the excess with retries. What should it use?

- A. Schedule the invocation with Cloud Scheduler
- B. Orchestrate the steps in Workflows
- C. Publish the event to a Pub/Sub topic
- D. Queue the work as a Cloud Tasks task

### 64. A service needs a warm floor for latency and a hard ceiling for cost. Which two settings fit? Select two.

- A. Raise the per-instance concurrency limit
- B. Use request-based billing
- C. Keep a minimum number of instances warm
- D. Allow unauthenticated invocations
- E. Cap the maximum instance count

### 65. A service must refuse every caller that is not inside the network, at the routing layer. What should be set?

- A. Allow unauthenticated invocations
- B. Put a global external Application Load Balancer in front
- C. Put Identity-Aware Proxy in front of the service
- D. Restrict ingress to internal traffic

### 66. A public status page must answer anonymous callers without a token. What should be allowed?

- A. Restrict ingress to internal traffic
- B. Allow unauthenticated invocations
- C. Grant the invoker role to the calling identity
- D. Put Identity-Aware Proxy in front of the service

### 67. One hostname must front services in two regions with a managed certificate. What should be added?

- A. Restrict ingress to internal traffic
- B. Put a global external Application Load Balancer in front
- C. Use API Gateway for the API
- D. Use a regional load balancer

### 68. A webhook payload shape must change and existing consumers cannot be updated in time. What should the team do?

- A. Add the field in a backward-compatible way
- B. Introduce a new API version alongside the old one
- C. Publish an OpenAPI specification
- D. Put Apigee in front of the API

### 69. A product team wants clusters without sizing or patching nodes themselves. Which mode fits?

- A. Enable node pool autoscaling
- B. Use GKE Autopilot for the cluster
- C. Run the batch node pool on Spot VMs
- D. Constrain pods to the intended node pool

### 70. Pods must call a Google Cloud API without any exported key file. What should the cluster use?

- A. Give the workload its own service account
- B. Download a service account key file
- C. Bind a Kubernetes service account to a Google service account
- D. Federate the external identity with Workload Identity Federation

### 71. A release must replace pods in batches while the service keeps answering. Which strategy fits?

- A. Run the batch node pool on Spot VMs
- B. Tune maxSurge and maxUnavailable
- C. Use a rolling update strategy
- D. Constrain pods to the intended node pool

### 72. A small cluster has no room for surge pods during a release. What should the strategy use?

- A. Tune maxSurge and maxUnavailable
- B. Use a rolling update strategy
- C. Enable node pool autoscaling
- D. Add a PodDisruptionBudget

### 73. A container wedges without exiting, and another must not receive traffic before it can serve. Which two probes fit? Select two.

- A. Configure a readiness probe
- B. Tune maxSurge and maxUnavailable
- C. Add a PodDisruptionBudget
- D. Configure a startup probe
- E. Configure a liveness probe

### 74. A container needs two minutes of initialisation and is restarted every thirty seconds. What should be added?

- A. Configure a liveness probe
- B. Add a PodDisruptionBudget
- C. Configure a readiness probe
- D. Configure a startup probe

### 75. External traffic keeps reaching a node whose pods are unready. What should gate the backend?

- A. Tune maxSurge and maxUnavailable
- B. Configure a readiness probe
- C. Add a PodDisruptionBudget
- D. Add a health check endpoint to the backend service

### 76. A CPU-bound importer must add pods under load and never fall below two pods. Which two settings fit? Select two.

- A. Scale pods on CPU utilization
- B. Set a minimum replica count
- C. Enable node pool autoscaling
- D. Scale pods on a custom or external metric
- E. Add a PodDisruptionBudget

### 77. Workers block on network I/O, so CPU stays flat while the backlog grows. What should the autoscaler follow?

- A. Enable node pool autoscaling
- B. Scale pods on a custom or external metric
- C. Buy committed use discounts for the steady baseline
- D. Scale pods on CPU utilization

### 78. The autoscaler adds pods, but they stay pending with no node to hold them. What is missing?

- A. Enable node pool autoscaling
- B. Add a PodDisruptionBudget
- C. Constrain pods to the intended node pool
- D. Scale pods on CPU utilization

### 79. A service multiplexes thousands of long-lived streams and must pack them onto few instances. What should be raised?

- A. Raise the per-instance concurrency limit
- B. Cap the maximum instance count
- C. Keep a minimum number of instances warm
- D. Use request-based billing

---

## Domain 4 — Integrating Applications with Google Cloud Services (Data, Messaging, APIs, and Observability)

### 80. An application in a language with no client connector must reach the instance over an authorised tunnel. What should be deployed?

- A. Connect over the database private IP
- B. Reach the service through Private Service Connect
- C. Connect through the Cloud SQL Auth Proxy
- D. Use the language connector with IAM

### 81. Request latency includes a fresh session handshake on every database call. What should be added?

- A. Pool and reuse database connections
- B. Reach the service through Private Service Connect
- C. Raise the container limits above the observed peak
- D. Raise the database connection ceiling by flag

### 82. The cluster must accept connections only through an authenticated proxy that manages certificates. What should be deployed?

- A. Connect through the AlloyDB Auth Proxy
- B. Connect through the Cloud SQL Auth Proxy
- C. Reach the service through Private Service Connect
- D. Use the language connector with IAM

### 83. A partner service must be consumed without a public address and without the internet. What should be used?

- A. Connect over the database private IP
- B. Reach the service through Private Service Connect
- C. Connect through the Cloud SQL Auth Proxy
- D. Expose the database on a public address with enforced SSL

### 84. A legacy instance must accept encrypted connections from one allowlisted address until the refactor lands. What fits the interim?

- A. Expose the database on a public address with enforced SSL
- B. Connect over the database private IP
- C. Reach the service through Private Service Connect
- D. Use the language connector with IAM

### 85. Malformed messages block the queue, and redelivered messages create duplicate orders. Which two fit? Select two.

- A. Add a dead-letter topic
- B. Retry with exponential backoff and jitter
- C. Deliver to an HTTPS push subscription
- D. Have the worker pull from the subscription
- E. Make the handler idempotent with a deduplication key

### 86. A vendor runs an HTTPS endpoint and will not run a subscriber of its own. Which delivery fits?

- A. Queue the work as a Cloud Tasks task
- B. Have the worker pull from the subscription
- C. Route the event with Eventarc
- D. Deliver to an HTTPS push subscription

### 87. Seven years of raw events must stay queryable without a pipeline service to maintain. What should be created?

- A. Store the objects in Cloud Storage
- B. Use a BigQuery subscription on the topic
- C. Export the batch to BigQuery
- D. Have the worker pull from the subscription

### 88. A client retries instantly on throttle and burns through its allowed attempts. What should it add?

- A. Retry with exponential backoff and jitter
- B. Raise the container limits above the observed peak
- C. Set a quota per API key
- D. Batch many small calls into one request

### 89. An iteration stops after five hundred records although thousands exist. What is missing?

- A. Cache the response for its freshness window
- B. Batch many small calls into one request
- C. Follow the page token until results are exhausted
- D. Request only the fields the caller needs

### 90. Each list item returns forty kilobytes while the interface shows three values. What should the client request?

- A. Cache the response for its freshness window
- B. Batch many small calls into one request
- C. Request only the fields the caller needs
- D. Follow the page token until results are exhausted

### 91. Reference data that changes weekly is fetched by every request handler. What should the client do?

- A. Retry with exponential backoff and jitter
- B. Cache the response for its freshness window
- C. Follow the page token until results are exhausted
- D. Raise the database connection ceiling by flag

### 92. A job can read every secret because it runs as a broadly scoped identity. What should be created for it?

- A. Let the workload use the default compute service account
- B. Grant the basic editor role
- C. Give the workload its own service account
- D. Define a custom role for the narrow permission set

### 93. A pipeline in another cloud still downloads a service account key at start-up. What should replace it?

- A. Federate the external identity with Workload Identity Federation
- B. Give the workload its own service account
- C. Download a service account key file
- D. Rely on Application Default Credentials

### 94. The team must count server errors from log entries and page past a threshold. Which two fit? Select two.

- A. Emit a custom metric from the code
- B. Alert on the error budget burn rate
- C. Create an alerting policy on the metric
- D. Build a log-based metric
- E. Set the correct severity on each entry

### 95. Pages fire on host CPU while users report slow checkouts. What should drive the paging instead?

- A. Alert on the error budget burn rate
- B. Create an alerting policy on the metric
- C. Set the correct severity on each entry
- D. Emit a custom metric from the code

### 96. Filters must select only errors, and the level must come from the application. What should the code set?

- A. Set the correct severity on each entry
- B. Emit structured JSON logs
- C. Send the exception to Error Reporting
- D. Build a log-based metric

### 97. A null dereference first appeared in one release and the team must see that. What shows it?

- A. Send the exception to Error Reporting
- B. Build a log-based metric
- C. Create an alerting policy on the metric
- D. Inspect the live process with Cloud Debugger

### 98. A support ticket gives a request identifier and every service's log must be found for it. What must the code do?

- A. Instrument a span around the downstream call
- B. Emit structured JSON logs
- C. Propagate the trace ID between services
- D. Set the correct severity on each entry

### 99. An on-call engineer wants the metrics anomaly explained and the likely commit suggested. What should assist?

- A. Ask Gemini Cloud Assist for a diagnosis
- B. Use an AI coding assistant to draft the tests
- C. Connect the assistant to an MCP server
- D. Send the exception to Error Reporting

### 100. A subscriber drops a message when the downstream service is briefly unavailable. What should change?

- A. Make the handler idempotent with a deduplication key
- B. Have the worker pull from the subscription
- C. Retry with exponential backoff and jitter
- D. Add a dead-letter topic

---

## Answer key and explanations

### Question 1 — B

Answer: Deploy the handler as a Cloud Functions function. A function runtime runs the handler only when the event fires. An event-triggered function runtime for a single-purpose handler rather than a long-lived service. Local study-map skill 1.1 (Compute Platform Selection), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 1 (designing highly scalable, secure, and reliable cloud-native applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Virtual machines where the operating system, runtime and scaling group are all managed by the team. Why the correct answer wins: A function runtime runs the handler only when the event fires.
- **B:** Correct. An event-triggered function runtime for a single-purpose handler rather than a long-lived service. In this case: A function runtime runs the handler only when the event fires.
- **C:** Incorrect for this question. A managed Kubernetes control plane where pods, node pools and cluster-scoped policy are yours to configure. Why the correct answer wins: A function runtime runs the handler only when the event fires.
- **D:** Incorrect for this question. A managed container runtime that scales to zero and bills per request while it serves traffic. Why the correct answer wins: A function runtime runs the handler only when the event fires.

### Question 2 — C

Answer: Deploy the service to Cloud Run. A managed container runtime serves HTTP and can scale to zero. A managed container runtime that scales to zero and bills per request while it serves traffic. Local study-map skill 1.1 (Compute Platform Selection), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 1 (designing highly scalable, secure, and reliable cloud-native applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A platform runtime that manages scaling for a supported language version and its sandbox limits. Why the correct answer wins: A managed container runtime serves HTTP and can scale to zero.
- **B:** Incorrect for this question. An event-triggered function runtime for a single-purpose handler rather than a long-lived service. Why the correct answer wins: A managed container runtime serves HTTP and can scale to zero.
- **C:** Correct. A managed container runtime that scales to zero and bills per request while it serves traffic. In this case: A managed container runtime serves HTTP and can scale to zero.
- **D:** Incorrect for this question. Virtual machines where the operating system, runtime and scaling group are all managed by the team. Why the correct answer wins: A managed container runtime serves HTTP and can scale to zero.

### Question 3 — D

Answer: Deploy the workload to Google Kubernetes Engine. A Kubernetes platform gives the shared cluster with those extension points. A managed Kubernetes control plane where pods, node pools and cluster-scoped policy are yours to configure. Local study-map skill 1.1 (Compute Platform Selection), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 1 (designing highly scalable, secure, and reliable cloud-native applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A managed container runtime that scales to zero and bills per request while it serves traffic. Why the correct answer wins: A Kubernetes platform gives the shared cluster with those extension points.
- **B:** Incorrect for this question. A platform runtime that manages scaling for a supported language version and its sandbox limits. Why the correct answer wins: A Kubernetes platform gives the shared cluster with those extension points.
- **C:** Incorrect for this question. An event-triggered function runtime for a single-purpose handler rather than a long-lived service. Why the correct answer wins: A Kubernetes platform gives the shared cluster with those extension points.
- **D:** Correct. A managed Kubernetes control plane where pods, node pools and cluster-scoped policy are yours to configure. In this case: A Kubernetes platform gives the shared cluster with those extension points.

### Question 4 — D

Answer: Store session state in a shared datastore. Moving session data out of the pod makes any instance able to serve the next request. Move the state out of the instance so any instance can serve any request. Local study-map skill 1.2 (Containerizing and Refactoring Applications), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 1 (designing highly scalable, secure, and reliable cloud-native applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A per-instance cache that is fast but not shared between instances. Why the correct answer wins: Moving session data out of the pod makes any instance able to serve the next request.
- **B:** Incorrect for this question. Pin a client to one backend for the life of its session. Why the correct answer wins: Moving session data out of the pod makes any instance able to serve the next request.
- **C:** Incorrect for this question. Route the client by cookie rather than by address or header. Why the correct answer wins: Moving session data out of the pod makes any instance able to serve the next request.
- **D:** Correct. Move the state out of the instance so any instance can serve any request. In this case: Moving session data out of the pod makes any instance able to serve the next request.

### Question 5 — A, C

Answers: Deploy the service in two regions behind a global load balancer; Add a health check endpoint to the backend service. Deploying into two regions keeps capacity after one is lost, and a health-checked load balancer diverts away from the failed region. Serve from two regions so a regional failure leaves capacity elsewhere. Let the load balancer stop sending traffic to an unhealthy instance. Local study-map skill 1.3 (Regional Distribution and Failover), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 1 (designing highly scalable, secure, and reliable cloud-native applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Correct. Serve from two regions so a regional failure leaves capacity elsewhere. In this case: Deploying into two regions keeps capacity after one is lost, and a health-checked load balancer diverts away from the failed region.
- **B:** Incorrect for this question. Cache responses at the edge so repeated requests never reach the origin. Why the correct answer wins: Deploying into two regions keeps capacity after one is lost, and a health-checked load balancer diverts away from the failed region.
- **C:** Correct. Let the load balancer stop sending traffic to an unhealthy instance. In this case: Deploying into two regions keeps capacity after one is lost, and a health-checked load balancer diverts away from the failed region.
- **D:** Incorrect for this question. Run in one zone only, so a zone failure stops the service entirely. Why the correct answer wins: Deploying into two regions keeps capacity after one is lost, and a health-checked load balancer diverts away from the failed region.
- **E:** Incorrect for this question. Spread instances over zones of a single region so a zone failure does not stop the service. Why the correct answer wins: Deploying into two regions keeps capacity after one is lost, and a health-checked load balancer diverts away from the failed region.

### Question 6 — C

Answer: Place the workload in a single zone. Placing the only copy in one zone leaves nothing to fail over to. Run in one zone only, so a zone failure stops the service entirely. Local study-map skill 1.3 (Regional Distribution and Failover), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 1 (designing highly scalable, secure, and reliable cloud-native applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Spread instances over zones of a single region so a zone failure does not stop the service. Why the correct answer wins: Placing the only copy in one zone leaves nothing to fail over to.
- **B:** Incorrect for this question. Serve from two regions so a regional failure leaves capacity elsewhere. Why the correct answer wins: Placing the only copy in one zone leaves nothing to fail over to.
- **C:** Correct. Run in one zone only, so a zone failure stops the service entirely. In this case: Placing the only copy in one zone leaves nothing to fail over to.
- **D:** Incorrect for this question. Trade a term commitment for a lower unit price on capacity that never idles. Why the correct answer wins: Placing the only copy in one zone leaves nothing to fail over to.

### Question 7 — C, D

Answers: Put a global external Application Load Balancer in front; Enable session affinity on the backend service. A global front door routes each shopper to the closest region, and affinity keeps that shopper on one instance. A single anycast address that routes to the nearest healthy backend. Pin a client to one backend for the life of its session. Local study-map skill 1.4 (Load Balancing and Session Affinity), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 1 (designing highly scalable, secure, and reliable cloud-native applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Cache responses at the edge so repeated requests never reach the origin. Why the correct answer wins: A global front door routes each shopper to the closest region, and affinity keeps that shopper on one instance.
- **B:** Incorrect for this question. A load balancer scoped to one region with a regional address. Why the correct answer wins: A global front door routes each shopper to the closest region, and affinity keeps that shopper on one instance.
- **C:** Correct. A single anycast address that routes to the nearest healthy backend. In this case: A global front door routes each shopper to the closest region, and affinity keeps that shopper on one instance.
- **D:** Correct. Pin a client to one backend for the life of its session. In this case: A global front door routes each shopper to the closest region, and affinity keeps that shopper on one instance.
- **E:** Incorrect for this question. Move the state out of the instance so any instance can serve any request. Why the correct answer wins: A global front door routes each shopper to the closest region, and affinity keeps that shopper on one instance.

### Question 8 — B

Answer: Use a generated cookie for stickiness. The cookie the balancer issues identifies the backend for later requests. Route the client by cookie rather than by address or header. Local study-map skill 1.4 (Load Balancing and Session Affinity), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 1 (designing highly scalable, secure, and reliable cloud-native applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Move the state out of the instance so any instance can serve any request. Why the correct answer wins: The cookie the balancer issues identifies the backend for later requests.
- **B:** Correct. Route the client by cookie rather than by address or header. In this case: The cookie the balancer issues identifies the backend for later requests.
- **C:** Incorrect for this question. A single anycast address that routes to the nearest healthy backend. Why the correct answer wins: The cookie the balancer issues identifies the backend for later requests.
- **D:** Incorrect for this question. Pin a client to one backend for the life of its session. Why the correct answer wins: The cookie the balancer issues identifies the backend for later requests.

### Question 9 — D

Answer: Cache reads in Memorystore. A shared in-memory service answers lock operations in about a millisecond. A managed Redis-compatible cache in front of the system of record. Local study-map skill 1.5 (Caching with Memorystore), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 1 (designing highly scalable, secure, and reliable cloud-native applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A per-instance cache that is fast but not shared between instances. Why the correct answer wins: A shared in-memory service answers lock operations in about a millisecond.
- **B:** Incorrect for this question. Cache responses at the edge so repeated requests never reach the origin. Why the correct answer wins: A shared in-memory service answers lock operations in about a millisecond.
- **C:** Incorrect for this question. Read the cache, fall back to the database, and populate the cache on a miss. Why the correct answer wins: A shared in-memory service answers lock operations in about a millisecond.
- **D:** Correct. A managed Redis-compatible cache in front of the system of record. In this case: A shared in-memory service answers lock operations in about a millisecond.

### Question 10 — B

Answer: Invalidate the cache on write. Invalidating the cached entry when the source changes stops the stale read. Remove or refresh the cached value so readers do not see stale data. Local study-map skill 1.5 (Caching with Memorystore), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 1 (designing highly scalable, secure, and reliable cloud-native applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Read the cache, fall back to the database, and populate the cache on a miss. Why the correct answer wins: Invalidating the cached entry when the source changes stops the stale read.
- **B:** Correct. Remove or refresh the cached value so readers do not see stale data. In this case: Invalidating the cached entry when the source changes stops the stale read.
- **C:** Incorrect for this question. Transition or delete objects by age so retention happens without a job. Why the correct answer wins: Invalidating the cached entry when the source changes stops the stale read.
- **D:** Incorrect for this question. Cache responses at the edge so repeated requests never reach the origin. Why the correct answer wins: Invalidating the cached entry when the source changes stops the stale read.

### Question 11 — A, C

Answers: Expose a REST API with JSON payloads; Expose a gRPC service. A binary RPC contract suits the high-throughput internal calls, and a resource-oriented HTTP interface suits the cacheable mobile path. A resource-oriented HTTP interface that browsers and simple clients can call. A binary, schema-driven RPC interface with streaming and generated clients. Local study-map skill 1.6 (API Protocol Choice: REST and gRPC), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 1 (designing highly scalable, secure, and reliable cloud-native applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Correct. A binary, schema-driven RPC interface with streaming and generated clients. In this case: A binary RPC contract suits the high-throughput internal calls, and a resource-oriented HTTP interface suits the cacheable mobile path.
- **B:** Incorrect for this question. A compatibility layer so browser code can call a gRPC service. Why the correct answer wins: A binary RPC contract suits the high-throughput internal calls, and a resource-oriented HTTP interface suits the cacheable mobile path.
- **C:** Correct. A resource-oriented HTTP interface that browsers and simple clients can call. In this case: A binary RPC contract suits the high-throughput internal calls, and a resource-oriented HTTP interface suits the cacheable mobile path.
- **D:** Incorrect for this question. Reduce per-call overhead when the API supports a batch surface. Why the correct answer wins: A binary RPC contract suits the high-throughput internal calls, and a resource-oriented HTTP interface suits the cacheable mobile path.
- **E:** Incorrect for this question. A machine-readable contract that generates clients and validates requests. Why the correct answer wins: A binary RPC contract suits the high-throughput internal calls, and a resource-oriented HTTP interface suits the cacheable mobile path.

### Question 12 — B

Answer: Serve gRPC-Web for browser clients. The browser-compatible variant carries the RPC calls over ordinary HTTP. A compatibility layer so browser code can call a gRPC service. Local study-map skill 1.6 (API Protocol Choice: REST and gRPC), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 1 (designing highly scalable, secure, and reliable cloud-native applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A binary, schema-driven RPC interface with streaming and generated clients. Why the correct answer wins: The browser-compatible variant carries the RPC calls over ordinary HTTP.
- **B:** Correct. A compatibility layer so browser code can call a gRPC service. In this case: The browser-compatible variant carries the RPC calls over ordinary HTTP.
- **C:** Incorrect for this question. A machine-readable contract that generates clients and validates requests. Why the correct answer wins: The browser-compatible variant carries the RPC calls over ordinary HTTP.
- **D:** Incorrect for this question. A resource-oriented HTTP interface that browsers and simple clients can call. Why the correct answer wins: The browser-compatible variant carries the RPC calls over ordinary HTTP.

### Question 13 — A

Answer: Set a quota per API key. A per-key allowance meters each customer against what they bought. Bound how many calls a plan allows in a window. Local study-map skill 1.7 (API Management, Rate Limiting, and Versioning), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 1 (designing highly scalable, secure, and reliable cloud-native applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Correct. Bound how many calls a plan allows in a window. In this case: A per-key allowance meters each customer against what they bought.
- **B:** Incorrect for this question. Keep the old contract working while the new one is adopted. Why the correct answer wins: A per-key allowance meters each customer against what they bought.
- **C:** Incorrect for this question. Reject or queue requests above a threshold so one client cannot exhaust the service. Why the correct answer wins: A per-key allowance meters each customer against what they bought.
- **D:** Incorrect for this question. A lighter managed gateway for routing and key-based quota enforcement. Why the correct answer wins: A per-key allowance meters each customer against what they bought.

### Question 14 — D

Answer: Add the field in a backward-compatible way. Tolerating unknown fields keeps older clients working without a new version. Extend the contract so existing clients keep working unchanged. Local study-map skill 1.7 (API Management, Rate Limiting, and Versioning), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 1 (designing highly scalable, secure, and reliable cloud-native applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Keep the old contract working while the new one is adopted. Why the correct answer wins: Tolerating unknown fields keeps older clients working without a new version.
- **B:** Incorrect for this question. A machine-readable contract that generates clients and validates requests. Why the correct answer wins: Tolerating unknown fields keeps older clients working without a new version.
- **C:** Incorrect for this question. Trim the response payload so latency and cost follow actual use. Why the correct answer wins: Tolerating unknown fields keeps older clients working without a new version.
- **D:** Correct. Extend the contract so existing clients keep working unchanged. In this case: Tolerating unknown fields keeps older clients working without a new version.

### Question 15 — C

Answer: Route the event with Eventarc. An event trigger reacts to the source event without polling. A trigger path that turns a Cloud Audit Log or resource event into a delivery. Local study-map skill 1.8 (Asynchronous and Event-Driven Integration), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 1 (designing highly scalable, secure, and reliable cloud-native applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A stateful sequence of service calls with retries and error branches. Why the correct answer wins: An event trigger reacts to the source event without polling.
- **B:** Incorrect for this question. A cron-style trigger that calls a target on a fixed timetable. Why the correct answer wins: An event trigger reacts to the source event without polling.
- **C:** Correct. A trigger path that turns a Cloud Audit Log or resource event into a delivery. In this case: An event trigger reacts to the source event without polling.
- **D:** Incorrect for this question. A task queue with retries and rate control aimed at a specific target. Why the correct answer wins: An event trigger reacts to the source event without polling.

### Question 16 — A

Answer: Orchestrate the steps in Workflows. A stateful orchestration records each step and retries the one that failed. A stateful sequence of service calls with retries and error branches. Local study-map skill 1.8 (Asynchronous and Event-Driven Integration), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 1 (designing highly scalable, secure, and reliable cloud-native applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Correct. A stateful sequence of service calls with retries and error branches. In this case: A stateful orchestration records each step and retries the one that failed.
- **B:** Incorrect for this question. A task queue with retries and rate control aimed at a specific target. Why the correct answer wins: A stateful orchestration records each step and retries the one that failed.
- **C:** Incorrect for this question. A cron-style trigger that calls a target on a fixed timetable. Why the correct answer wins: A stateful orchestration records each step and retries the one that failed.
- **D:** Incorrect for this question. A durable, at-least-once message channel with independent subscribers. Why the correct answer wins: A stateful orchestration records each step and retries the one that failed.

### Question 17 — A, D

Answers: Set CPU and memory requests from measured use; Buy committed use discounts for the steady baseline. Sizing requests from measurement stops paying for unused capacity, and a commitment discounts the part that never changes. Give the scheduler real numbers so placement and scaling decisions are not guesses. Trade a term commitment for a lower unit price on capacity that never idles. Local study-map skill 1.9 (Resource Requirements and Cost Optimization), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 1 (designing highly scalable, secure, and reliable cloud-native applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Correct. Give the scheduler real numbers so placement and scaling decisions are not guesses. In this case: Sizing requests from measurement stops paying for unused capacity, and a commitment discounts the part that never changes.
- **B:** Incorrect for this question. Place work on nodes whose shape and pricing match the workload. Why the correct answer wins: Sizing requests from measurement stops paying for unused capacity, and a commitment discounts the part that never changes.
- **C:** Incorrect for this question. Use reclaimable capacity for work that can tolerate a node disappearing. Why the correct answer wins: Sizing requests from measurement stops paying for unused capacity, and a commitment discounts the part that never changes.
- **D:** Correct. Trade a term commitment for a lower unit price on capacity that never idles. In this case: Sizing requests from measurement stops paying for unused capacity, and a commitment discounts the part that never changes.
- **E:** Incorrect for this question. Allow the process the headroom it needs so it is not throttled or killed. Why the correct answer wins: Sizing requests from measurement stops paying for unused capacity, and a commitment discounts the part that never changes.

### Question 18 — B

Answer: Constrain pods to the intended node pool. A node selector places the pod on nodes with that capability. Place work on nodes whose shape and pricing match the workload. Local study-map skill 1.9 (Resource Requirements and Cost Optimization), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 1 (designing highly scalable, secure, and reliable cloud-native applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Add or remove nodes as pending pods demand capacity. Why the correct answer wins: A node selector places the pod on nodes with that capability.
- **B:** Correct. Place work on nodes whose shape and pricing match the workload. In this case: A node selector places the pod on nodes with that capability.
- **C:** Incorrect for this question. Use reclaimable capacity for work that can tolerate a node disappearing. Why the correct answer wins: A node selector places the pod on nodes with that capability.
- **D:** Incorrect for this question. Trade a term commitment for a lower unit price on capacity that never idles. Why the correct answer wins: A node selector places the pod on nodes with that capability.

### Question 19 — A

Answer: Split traffic between revisions by percentage. Weighted routing moves traffic onto the new revision in steps. Send a fraction of requests to the new revision while the old one still serves the rest. Local study-map skill 1.10 (Traffic Splitting and Gradual Rollout), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 1 (designing highly scalable, secure, and reliable cloud-native applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Correct. Send a fraction of requests to the new revision while the old one still serves the rest. In this case: Weighted routing moves traffic onto the new revision in steps.
- **B:** Incorrect for this question. Send only tagged requests to the new revision for internal testing. Why the correct answer wins: Weighted routing moves traffic onto the new revision in steps.
- **C:** Incorrect for this question. Return all traffic to the known-good revision when the new one misbehaves. Why the correct answer wins: Weighted routing moves traffic onto the new revision in steps.
- **D:** Incorrect for this question. Expose the new version to a slice of traffic before widening it. Why the correct answer wins: Weighted routing moves traffic onto the new revision in steps.

### Question 20 — B

Answer: Canary the release at a small percentage first. A small canary slice gives the error signal before the wider rollout. Expose the new version to a slice of traffic before widening it. Local study-map skill 1.10 (Traffic Splitting and Gradual Rollout), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 1 (designing highly scalable, secure, and reliable cloud-native applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Return all traffic to the known-good revision when the new one misbehaves. Why the correct answer wins: A small canary slice gives the error signal before the wider rollout.
- **B:** Correct. Expose the new version to a slice of traffic before widening it. In this case: A small canary slice gives the error signal before the wider rollout.
- **C:** Incorrect for this question. Ship the code dark and enable it per cohort without a redeploy. Why the correct answer wins: A small canary slice gives the error signal before the wider rollout.
- **D:** Incorrect for this question. Send a fraction of requests to the new revision while the old one still serves the rest. Why the correct answer wins: A small canary slice gives the error signal before the wider rollout.

### Question 21 — C

Answer: Use Cloud Service Mesh for service-to-service traffic. A mesh applies those policies at the sidecar instead of in each service. Mutual TLS, retries and traffic policy applied without changing application code. Local study-map skill 1.11 (Orchestrating Services), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 1 (designing highly scalable, secure, and reliable cloud-native applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A stateful sequence of service calls with retries and error branches. Why the correct answer wins: A mesh applies those policies at the sidecar instead of in each service.
- **B:** Incorrect for this question. A task queue with retries and rate control aimed at a specific target. Why the correct answer wins: A mesh applies those policies at the sidecar instead of in each service.
- **C:** Correct. Mutual TLS, retries and traffic policy applied without changing application code. In this case: A mesh applies those policies at the sidecar instead of in each service.
- **D:** Incorrect for this question. A lighter managed gateway for routing and key-based quota enforcement. Why the correct answer wins: A mesh applies those policies at the sidecar instead of in each service.

### Question 22 — A

Answer: Lock the bucket retention policy. A retention lock prevents deletion and shortening for the locked period. Make the retention period impossible to shorten, even by an owner. Local study-map skill 1.12 (Data Retention and Organization Policy), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 1 (designing highly scalable, secure, and reliable cloud-native applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Correct. Make the retention period impossible to shorten, even by an owner. In this case: A retention lock prevents deletion and shortening for the locked period.
- **B:** Incorrect for this question. Serve every object to anyone, which removes the need to authorize at all. Why the correct answer wins: A retention lock prevents deletion and shortening for the locked period.
- **C:** Incorrect for this question. A time-limited grant to one object without exposing credentials. Why the correct answer wins: A retention lock prevents deletion and shortening for the locked period.
- **D:** Incorrect for this question. Transition or delete objects by age so retention happens without a job. Why the correct answer wins: A retention lock prevents deletion and shortening for the locked period.

### Question 23 — B, E

Answers: Store the credential in Secret Manager; Use a customer-managed encryption key. A managed secret store keeps the version history, and a customer-managed key encrypts the payloads. A managed secret store with versioning and access audit. A key the customer owns, rotates and can disable. Local study-map skill 1.13 (Secrets, Keys, and Credential Rotation), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 1 (designing highly scalable, secure, and reliable cloud-native applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Present the value as a file that the process reads at runtime. Why the correct answer wins: A managed secret store keeps the version history, and a customer-managed key encrypts the payloads.
- **B:** Correct. A managed secret store with versioning and access audit. In this case: A managed secret store keeps the version history, and a customer-managed key encrypts the payloads.
- **C:** Incorrect for this question. Inject the value into the process environment at start-up. Why the correct answer wins: A managed secret store keeps the version history, and a customer-managed key encrypts the payloads.
- **D:** Incorrect for this question. A long-lived credential that has to be stored and rotated by hand. Why the correct answer wins: A managed secret store keeps the version history, and a customer-managed key encrypts the payloads.
- **E:** Correct. A key the customer owns, rotates and can disable. In this case: A managed secret store keeps the version history, and a customer-managed key encrypts the payloads.

### Question 24 — A

Answer: Mount the secret as a volume. Mounting the secret as a file keeps the value out of the environment. Present the value as a file that the process reads at runtime. Local study-map skill 1.13 (Secrets, Keys, and Credential Rotation), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 1 (designing highly scalable, secure, and reliable cloud-native applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Correct. Present the value as a file that the process reads at runtime. In this case: Mounting the secret as a file keeps the value out of the environment.
- **B:** Incorrect for this question. A long-lived credential that has to be stored and rotated by hand. Why the correct answer wins: Mounting the secret as a file keeps the value out of the environment.
- **C:** Incorrect for this question. A key the customer owns, rotates and can disable. Why the correct answer wins: Mounting the secret as a file keeps the value out of the environment.
- **D:** Incorrect for this question. Inject the value into the process environment at start-up. Why the correct answer wins: Mounting the secret as a file keeps the value out of the environment.

### Question 25 — D

Answer: Validate the signed JWT from the proxy. The signed assertion from the proxy proves both the path and the user. Check the assertion the proxy adds so only proxied requests are trusted. Local study-map skill 1.14 (Application Authentication), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 1 (designing highly scalable, secure, and reliable cloud-native applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A managed identity service for customer accounts and tokens. Why the correct answer wins: The signed assertion from the proxy proves both the path and the user.
- **B:** Incorrect for this question. Let the client library find credentials from the environment. Why the correct answer wins: The signed assertion from the proxy proves both the path and the user.
- **C:** Incorrect for this question. A dedicated identity whose roles can be granted and revoked independently. Why the correct answer wins: The signed assertion from the proxy proves both the path and the user.
- **D:** Correct. Check the assertion the proxy adds so only proxied requests are trusted. In this case: The signed assertion from the proxy proves both the path and the user.

### Question 26 — D

Answer: Use Identity Platform for end-user sign-in. A managed identity service issues and refreshes the tokens for external customers. A managed identity service for customer accounts and tokens. Local study-map skill 1.14 (Application Authentication), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 1 (designing highly scalable, secure, and reliable cloud-native applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A dedicated identity whose roles can be granted and revoked independently. Why the correct answer wins: A managed identity service issues and refreshes the tokens for external customers.
- **B:** Incorrect for this question. Exchange an outside token for a short-lived Google credential. Why the correct answer wins: A managed identity service issues and refreshes the tokens for external customers.
- **C:** Incorrect for this question. Check the assertion the proxy adds so only proxied requests are trusted. Why the correct answer wins: A managed identity service issues and refreshes the tokens for external customers.
- **D:** Correct. A managed identity service for customer accounts and tokens. In this case: A managed identity service issues and refreshes the tokens for external customers.

### Question 27 — C

Answer: Apply a Kubernetes NetworkPolicy. A network policy restricts which sources may reach the pods. Restrict which pods may talk to which pods inside the cluster. Local study-map skill 1.15 (Least Privilege and Service-to-Service Security), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 1 (designing highly scalable, secure, and reliable cloud-native applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Let anyone reach the endpoint, which is only appropriate for public content. Why the correct answer wins: A network policy restricts which sources may reach the pods.
- **B:** Incorrect for this question. Bound the total capacity a namespace may consume. Why the correct answer wins: A network policy restricts which sources may reach the pods.
- **C:** Correct. Restrict which pods may talk to which pods inside the cluster. In this case: A network policy restricts which sources may reach the pods.
- **D:** Incorrect for this question. Authenticate and authorize users before a request reaches the application. Why the correct answer wins: A network policy restricts which sources may reach the pods.

### Question 28 — D

Answer: Grant only the roles the workload needs. Granting only the permissions the function needs would bound the damage. Scope permissions to the actions in use rather than the whole service. Local study-map skill 1.15 (Least Privilege and Service-to-Service Security), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 1 (designing highly scalable, secure, and reliable cloud-native applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A legacy broad role that can change most resources in the project. Why the correct answer wins: Granting only the permissions the function needs would bound the damage.
- **B:** Incorrect for this question. A dedicated identity whose roles can be granted and revoked independently. Why the correct answer wins: Granting only the permissions the function needs would bound the damage.
- **C:** Incorrect for this question. A role built from an explicit permission list. Why the correct answer wins: Granting only the permissions the function needs would bound the damage.
- **D:** Correct. Scope permissions to the actions in use rather than the whole service. In this case: Granting only the permissions the function needs would bound the damage.

### Question 29 — A, B

Answers: Store the ledger in Spanner; Design the row key for the read pattern. A globally consistent relational store suits the ledger, and a wide-column store suits writes keyed by device. A relational database with strongly consistent multi-region transactions. Order the key so the query becomes a contiguous range scan. Local study-map skill 1.16 (Storage and Schema Selection), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 1 (designing highly scalable, secure, and reliable cloud-native applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Correct. A relational database with strongly consistent multi-region transactions. In this case: A globally consistent relational store suits the ledger, and a wide-column store suits writes keyed by device.
- **B:** Correct. Order the key so the query becomes a contiguous range scan. In this case: A globally consistent relational store suits the ledger, and a wide-column store suits writes keyed by device.
- **C:** Incorrect for this question. Durable object storage addressed by name rather than a database row. Why the correct answer wins: A globally consistent relational store suits the ledger, and a wide-column store suits writes keyed by device.
- **D:** Incorrect for this question. A managed Redis-compatible cache in front of the system of record. Why the correct answer wins: A globally consistent relational store suits the ledger, and a wide-column store suits writes keyed by device.
- **E:** Incorrect for this question. A document store with real-time listeners and mobile SDKs. Why the correct answer wins: A globally consistent relational store suits the ledger, and a wide-column store suits writes keyed by device.

### Question 30 — D

Answer: Use Firestore in Native mode. A document store with offline sync gives the mobile app what it needs. A document store with real-time listeners and mobile SDKs. Local study-map skill 1.16 (Storage and Schema Selection), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 1 (designing highly scalable, secure, and reliable cloud-native applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A relational database with strongly consistent multi-region transactions. Why the correct answer wins: A document store with offline sync gives the mobile app what it needs.
- **B:** Incorrect for this question. A managed Redis-compatible cache in front of the system of record. Why the correct answer wins: A document store with offline sync gives the mobile app what it needs.
- **C:** Incorrect for this question. Order the key so the query becomes a contiguous range scan. Why the correct answer wins: A document store with offline sync gives the mobile app what it needs.
- **D:** Correct. A document store with real-time listeners and mobile SDKs. In this case: A document store with offline sync gives the mobile app what it needs.

### Question 31 — A

Answer: Make the bucket public. Anonymous read access suits assets that are meant to be public. Serve every object to anyone, which removes the need to authorize at all. Local study-map skill 1.17 (Signed URLs and Time-Limited Access), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 1 (designing highly scalable, secure, and reliable cloud-native applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Correct. Serve every object to anyone, which removes the need to authorize at all. In this case: Anonymous read access suits assets that are meant to be public.
- **B:** Incorrect for this question. Make the retention period impossible to shorten, even by an owner. Why the correct answer wins: Anonymous read access suits assets that are meant to be public.
- **C:** Incorrect for this question. Transition or delete objects by age so retention happens without a job. Why the correct answer wins: Anonymous read access suits assets that are meant to be public.
- **D:** Incorrect for this question. A time-limited grant to one object without exposing credentials. Why the correct answer wins: Anonymous read access suits assets that are meant to be public.

### Question 32 — D

Answer: Export the batch to BigQuery. Exporting the day's rows to files hands the batch job what it needs. Load a periodic extract rather than a continuous stream. Local study-map skill 1.18 (Analytics and ML Data Handoff), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 1 (designing highly scalable, secure, and reliable cloud-native applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Land analytics rows in the warehouse for SQL and ML use. Why the correct answer wins: Exporting the day's rows to files hands the batch job what it needs.
- **B:** Incorrect for this question. Write topic messages straight into a table without a consumer. Why the correct answer wins: Exporting the day's rows to files hands the batch job what it needs.
- **C:** Incorrect for this question. Durable object storage addressed by name rather than a database row. Why the correct answer wins: Exporting the day's rows to files hands the batch job what it needs.
- **D:** Correct. Load a periodic extract rather than a continuous stream. In this case: Exporting the day's rows to files hands the batch job what it needs.

### Question 33 — C, E

Answers: Run the service emulator locally; Use Cloud Workstations for the environment. A local emulator speaks the protocol without a project, and a standard image gives identical tooling. A local stand-in for a managed service used for unit and integration work. A managed, container-defined development environment behind a private endpoint. Local study-map skill 2.1 (Local Emulation of Cloud Services), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 2 (building and testing applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Read variable state in a running deployment without redeploying. Why the correct answer wins: A local emulator speaks the protocol without a project, and a standard image gives identical tooling.
- **B:** Incorrect for this question. A browser terminal with the SDK and tooling already installed. Why the correct answer wins: A local emulator speaks the protocol without a project, and a standard image gives identical tooling.
- **C:** Correct. A managed, container-defined development environment behind a private endpoint. In this case: A local emulator speaks the protocol without a project, and a standard image gives identical tooling.
- **D:** Incorrect for this question. Editor integration for scaffolding, running and debugging on Google Cloud. Why the correct answer wins: A local emulator speaks the protocol without a project, and a standard image gives identical tooling.
- **E:** Correct. A local stand-in for a managed service used for unit and integration work. In this case: A local emulator speaks the protocol without a project, and a standard image gives identical tooling.

### Question 34 — A

Answer: Use Cloud Shell for the session. A browser shell with the SDK already installed needs no setup. A browser terminal with the SDK and tooling already installed. Local study-map skill 2.1 (Local Emulation of Cloud Services), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 2 (building and testing applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Correct. A browser terminal with the SDK and tooling already installed. In this case: A browser shell with the SDK already installed needs no setup.
- **B:** Incorrect for this question. A managed, container-defined development environment behind a private endpoint. Why the correct answer wins: A browser shell with the SDK already installed needs no setup.
- **C:** Incorrect for this question. A local stand-in for a managed service used for unit and integration work. Why the correct answer wins: A browser shell with the SDK already installed needs no setup.
- **D:** Incorrect for this question. Editor integration for scaffolding, running and debugging on Google Cloud. Why the correct answer wins: A browser shell with the SDK already installed needs no setup.

### Question 35 — B

Answer: Ask Gemini Cloud Assist for a diagnosis. An in-editor assistant explains the trace with surrounding context. An assistant that reads telemetry and proposes a cause and a next step. Local study-map skill 2.2 (Developer Tooling and AI Assistance), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 2 (building and testing applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Give the assistant a defined tool surface instead of pasting context by hand. Why the correct answer wins: An in-editor assistant explains the trace with surrounding context.
- **B:** Correct. An assistant that reads telemetry and proposes a cause and a next step. In this case: An in-editor assistant explains the trace with surrounding context.
- **C:** Incorrect for this question. Editor integration for scaffolding, running and debugging on Google Cloud. Why the correct answer wins: An in-editor assistant explains the trace with surrounding context.
- **D:** Incorrect for this question. Generate a first draft from context, then review and correct it. Why the correct answer wins: An in-editor assistant explains the trace with surrounding context.

### Question 36 — D

Answer: Connect the assistant to an MCP server. An MCP server exposes tools the assistant can call directly. Give the assistant a defined tool surface instead of pasting context by hand. Local study-map skill 2.2 (Developer Tooling and AI Assistance), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 2 (building and testing applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A browser terminal with the SDK and tooling already installed. Why the correct answer wins: An MCP server exposes tools the assistant can call directly.
- **B:** Incorrect for this question. Editor integration for scaffolding, running and debugging on Google Cloud. Why the correct answer wins: An MCP server exposes tools the assistant can call directly.
- **C:** Incorrect for this question. An assistant that reads telemetry and proposes a cause and a next step. Why the correct answer wins: An MCP server exposes tools the assistant can call directly.
- **D:** Correct. Give the assistant a defined tool surface instead of pasting context by hand. In this case: An MCP server exposes tools the assistant can call directly.

### Question 37 — D

Answer: Use an AI coding assistant to draft the tests. A coding assistant drafts the review pass that the human then edits. Generate a first draft from context, then review and correct it. Local study-map skill 2.2 (Developer Tooling and AI Assistance), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 2 (building and testing applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. An assistant that reads telemetry and proposes a cause and a next step. Why the correct answer wins: A coding assistant drafts the review pass that the human then edits.
- **B:** Incorrect for this question. Give the assistant a defined tool surface instead of pasting context by hand. Why the correct answer wins: A coding assistant drafts the review pass that the human then edits.
- **C:** Incorrect for this question. A managed, container-defined development environment behind a private endpoint. Why the correct answer wins: A coding assistant drafts the review pass that the human then edits.
- **D:** Correct. Generate a first draft from context, then review and correct it. In this case: A coding assistant drafts the review pass that the human then edits.

### Question 38 — B, D

Answers: Trigger the build from a repository push; Build the image with Cloud Build. A trigger reacts to the merge, and a managed build service runs the steps in a clean environment. Start the pipeline when the branch changes rather than by hand. A managed build service that runs the steps from a build configuration file. Local study-map skill 2.3 (Container Builds with Cloud Build), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 2 (building and testing applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Wrap the existing process in a portable artifact that a managed runtime can execute. Why the correct answer wins: A trigger reacts to the merge, and a managed build service runs the steps in a clean environment.
- **B:** Correct. Start the pipeline when the branch changes rather than by hand. In this case: A trigger reacts to the merge, and a managed build service runs the steps in a clean environment.
- **C:** Incorrect for this question. Run the build steps locally and push the result when someone remembers. Why the correct answer wins: A trigger reacts to the merge, and a managed build service runs the steps in a clean environment.
- **D:** Correct. A managed build service that runs the steps from a build configuration file. In this case: A trigger reacts to the merge, and a managed build service runs the steps in a clean environment.
- **E:** Incorrect for this question. Release exactly the artifact that was tested rather than a moving tag. Why the correct answer wins: A trigger reacts to the merge, and a managed build service runs the steps in a clean environment.

### Question 39 — B

Answer: Deploy from source and let the platform build it. Source deployment builds from the repository using detected buildpacks. Hand the source to the managed builder instead of shipping an image. Local study-map skill 2.3 (Container Builds with Cloud Build), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 2 (building and testing applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Release exactly the artifact that was tested rather than a moving tag. Why the correct answer wins: Source deployment builds from the repository using detected buildpacks.
- **B:** Correct. Hand the source to the managed builder instead of shipping an image. In this case: Source deployment builds from the repository using detected buildpacks.
- **C:** Incorrect for this question. Run the build steps locally and push the result when someone remembers. Why the correct answer wins: Source deployment builds from the repository using detected buildpacks.
- **D:** Incorrect for this question. Wrap the existing process in a portable artifact that a managed runtime can execute. Why the correct answer wins: Source deployment builds from the repository using detected buildpacks.

### Question 40 — C

Answer: Deploy a pinned image digest. Promoting the identical image keeps production equal to what staging verified. Release exactly the artifact that was tested rather than a moving tag. Local study-map skill 2.3 (Container Builds with Cloud Build), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 2 (building and testing applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Wrap the existing process in a portable artifact that a managed runtime can execute. Why the correct answer wins: Promoting the identical image keeps production equal to what staging verified.
- **B:** Incorrect for this question. Hand the source to the managed builder instead of shipping an image. Why the correct answer wins: Promoting the identical image keeps production equal to what staging verified.
- **C:** Correct. Release exactly the artifact that was tested rather than a moving tag. In this case: Promoting the identical image keeps production equal to what staging verified.
- **D:** Incorrect for this question. Run the build steps locally and push the result when someone remembers. Why the correct answer wins: Promoting the identical image keeps production equal to what staging verified.

### Question 41 — B

Answer: Push the image to Artifact Registry. A regional repository in that region stores the images there. A managed registry with IAM-scoped repositories per environment. Local study-map skill 2.4 (Artifact Registry and Image Storage), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 2 (building and testing applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A managed build service that runs the steps from a build configuration file. Why the correct answer wins: A regional repository in that region stores the images there.
- **B:** Correct. A managed registry with IAM-scoped repositories per environment. In this case: A regional repository in that region stores the images there.
- **C:** Incorrect for this question. The older registry whose access model is project-wide Cloud Storage. Why the correct answer wins: A regional repository in that region stores the images there.
- **D:** Incorrect for this question. Durable object storage addressed by name rather than a database row. Why the correct answer wins: A regional repository in that region stores the images there.

### Question 42 — B

Answer: Store the objects in Cloud Storage. Object storage versions the non-image artifacts the cluster pulls. Durable object storage addressed by name rather than a database row. Local study-map skill 2.4 (Artifact Registry and Image Storage), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 2 (building and testing applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. The older registry whose access model is project-wide Cloud Storage. Why the correct answer wins: Object storage versions the non-image artifacts the cluster pulls.
- **B:** Correct. Durable object storage addressed by name rather than a database row. In this case: Object storage versions the non-image artifacts the cluster pulls.
- **C:** Incorrect for this question. A managed build service that runs the steps from a build configuration file. Why the correct answer wins: Object storage versions the non-image artifacts the cluster pulls.
- **D:** Incorrect for this question. A managed registry with IAM-scoped repositories per environment. Why the correct answer wins: Object storage versions the non-image artifacts the cluster pulls.

### Question 43 — A

Answer: Push the image to Container Registry. The legacy registry host keeps those older pull paths resolving. The older registry whose access model is project-wide Cloud Storage. Local study-map skill 2.4 (Artifact Registry and Image Storage), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 2 (building and testing applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Correct. The older registry whose access model is project-wide Cloud Storage. In this case: The legacy registry host keeps those older pull paths resolving.
- **B:** Incorrect for this question. A managed build service that runs the steps from a build configuration file. Why the correct answer wins: The legacy registry host keeps those older pull paths resolving.
- **C:** Incorrect for this question. A managed registry with IAM-scoped repositories per environment. Why the correct answer wins: The legacy registry host keeps those older pull paths resolving.
- **D:** Incorrect for this question. Durable object storage addressed by name rather than a database row. Why the correct answer wins: The legacy registry host keeps those older pull paths resolving.

### Question 44 — C

Answer: Scan the image with Artifact Analysis. Image analysis records the components that make up the image. Report known vulnerabilities in the image layers and packages. Local study-map skill 2.5 (Build Provenance and Admission Control), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 2 (building and testing applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Aggregate and triage security findings across the project. Why the correct answer wins: Image analysis records the components that make up the image.
- **B:** Incorrect for this question. A signed record of what was built and from which source. Why the correct answer wins: Image analysis records the components that make up the image.
- **C:** Correct. Report known vulnerabilities in the image layers and packages. In this case: Image analysis records the components that make up the image.
- **D:** Incorrect for this question. Only images that satisfy the attestation policy may be deployed. Why the correct answer wins: Image analysis records the components that make up the image.

### Question 45 — D

Answer: Enforce admission with Binary Authorization. An admission exception admits the named image without disabling the policy. Only images that satisfy the attestation policy may be deployed. Local study-map skill 2.5 (Build Provenance and Admission Control), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 2 (building and testing applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A signed record of what was built and from which source. Why the correct answer wins: An admission exception admits the named image without disabling the policy.
- **B:** Incorrect for this question. Aggregate and triage security findings across the project. Why the correct answer wins: An admission exception admits the named image without disabling the policy.
- **C:** Incorrect for this question. Report known vulnerabilities in the image layers and packages. Why the correct answer wins: An admission exception admits the named image without disabling the policy.
- **D:** Correct. Only images that satisfy the attestation policy may be deployed. In this case: An admission exception admits the named image without disabling the policy.

### Question 46 — D

Answer: Generate build provenance in Cloud Build. A provenance record names the source and the builder for the artifact. A signed record of what was built and from which source. Local study-map skill 2.5 (Build Provenance and Admission Control), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 2 (building and testing applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Report known vulnerabilities in the image layers and packages. Why the correct answer wins: A provenance record names the source and the builder for the artifact.
- **B:** Incorrect for this question. Demand a stronger provenance guarantee as a gate on the pipeline. Why the correct answer wins: A provenance record names the source and the builder for the artifact.
- **C:** Incorrect for this question. Only images that satisfy the attestation policy may be deployed. Why the correct answer wins: A provenance record names the source and the builder for the artifact.
- **D:** Correct. A signed record of what was built and from which source. In this case: A provenance record names the source and the builder for the artifact.

### Question 47 — C, E

Answers: Quarantine the flaky test and fix it; Add a unit test with dependencies stubbed. Quarantine removes the unstable signal, and a unit test proves the branches in isolation. Keep the suite trustworthy while the unstable test is repaired. Exercise one unit in isolation with its collaborators replaced. Local study-map skill 2.6 (Unit Testing Practice), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 2 (building and testing applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Measure behaviour under expected peak traffic rather than guessing. Why the correct answer wins: Quarantine removes the unstable signal, and a unit test proves the branches in isolation.
- **B:** Incorrect for this question. Exercise the wire-up between components before deploying. Why the correct answer wins: Quarantine removes the unstable signal, and a unit test proves the branches in isolation.
- **C:** Correct. Exercise one unit in isolation with its collaborators replaced. In this case: Quarantine removes the unstable signal, and a unit test proves the branches in isolation.
- **D:** Incorrect for this question. Make a passing test suite a precondition for release. Why the correct answer wins: Quarantine removes the unstable signal, and a unit test proves the branches in isolation.
- **E:** Correct. Keep the suite trustworthy while the unstable test is repaired. In this case: Quarantine removes the unstable signal, and a unit test proves the branches in isolation.

### Question 48 — C

Answer: Block the deploy on the test result. A gate blocks promotion when the suite fails. Make a passing test suite a precondition for release. Local study-map skill 2.6 (Unit Testing Practice), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 2 (building and testing applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Measure behaviour under expected peak traffic rather than guessing. Why the correct answer wins: A gate blocks promotion when the suite fails.
- **B:** Incorrect for this question. Exercise the wire-up between components before deploying. Why the correct answer wins: A gate blocks promotion when the suite fails.
- **C:** Correct. Make a passing test suite a precondition for release. In this case: A gate blocks promotion when the suite fails.
- **D:** Incorrect for this question. Keep the suite trustworthy while the unstable test is repaired. Why the correct answer wins: A gate blocks promotion when the suite fails.

### Question 49 — A

Answer: Inspect the live process with Cloud Debugger. A debugger pauses at the assertion with the live variables. Read variable state in a running deployment without redeploying. Local study-map skill 2.6 (Unit Testing Practice), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 2 (building and testing applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Correct. Read variable state in a running deployment without redeploying. In this case: A debugger pauses at the assertion with the live variables.
- **B:** Incorrect for this question. Find the function consuming CPU or memory under real traffic. Why the correct answer wins: A debugger pauses at the assertion with the live variables.
- **C:** Incorrect for this question. Exercise one unit in isolation with its collaborators replaced. Why the correct answer wins: A debugger pauses at the assertion with the live variables.
- **D:** Incorrect for this question. Group and count application errors instead of grepping logs. Why the correct answer wins: A debugger pauses at the assertion with the live variables.

### Question 50 — A, B

Answers: Run an integration test against the emulator; Load-test the release before the rollout. An integration run exercises the real broker, and a load run measures the expected peak. Exercise the wire-up between components before deploying. Measure behaviour under expected peak traffic rather than guessing. Local study-map skill 2.7 (Automated Integration Testing), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 2 (building and testing applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Correct. Exercise the wire-up between components before deploying. In this case: An integration run exercises the real broker, and a load run measures the expected peak.
- **B:** Correct. Measure behaviour under expected peak traffic rather than guessing. In this case: An integration run exercises the real broker, and a load run measures the expected peak.
- **C:** Incorrect for this question. Find the function consuming CPU or memory under real traffic. Why the correct answer wins: An integration run exercises the real broker, and a load run measures the expected peak.
- **D:** Incorrect for this question. Exercise one unit in isolation with its collaborators replaced. Why the correct answer wins: An integration run exercises the real broker, and a load run measures the expected peak.
- **E:** Incorrect for this question. A local stand-in for a managed service used for unit and integration work. Why the correct answer wins: An integration run exercises the real broker, and a load run measures the expected peak.

### Question 51 — D

Answer: Profile the service with Cloud Profiler. A profiler attributes the CPU time to the functions inside the service. Find the function consuming CPU or memory under real traffic. Local study-map skill 2.7 (Automated Integration Testing), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 2 (building and testing applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Group and count application errors instead of grepping logs. Why the correct answer wins: A profiler attributes the CPU time to the functions inside the service.
- **B:** Incorrect for this question. Measure behaviour under expected peak traffic rather than guessing. Why the correct answer wins: A profiler attributes the CPU time to the functions inside the service.
- **C:** Incorrect for this question. Show where time goes inside a request that crosses services. Why the correct answer wins: A profiler attributes the CPU time to the functions inside the service.
- **D:** Correct. Find the function consuming CPU or memory under real traffic. In this case: A profiler attributes the CPU time to the functions inside the service.

### Question 52 — D

Answer: Run the service emulator locally. A local substitute speaks the protocol when the vendor sandbox is unreachable. A local stand-in for a managed service used for unit and integration work. Local study-map skill 2.7 (Automated Integration Testing), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 2 (building and testing applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Measure behaviour under expected peak traffic rather than guessing. Why the correct answer wins: A local substitute speaks the protocol when the vendor sandbox is unreachable.
- **B:** Incorrect for this question. Find the function consuming CPU or memory under real traffic. Why the correct answer wins: A local substitute speaks the protocol when the vendor sandbox is unreachable.
- **C:** Incorrect for this question. Exercise the wire-up between components before deploying. Why the correct answer wins: A local substitute speaks the protocol when the vendor sandbox is unreachable.
- **D:** Correct. A local stand-in for a managed service used for unit and integration work. In this case: A local substitute speaks the protocol when the vendor sandbox is unreachable.

### Question 53 — C

Answer: Run the tests as a Cloud Build step. Running the suite as a build step makes it part of promotion. Fail the pipeline at the test stage instead of after deployment. Local study-map skill 2.7 (Automated Integration Testing), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 2 (building and testing applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Keep the suite trustworthy while the unstable test is repaired. Why the correct answer wins: Running the suite as a build step makes it part of promotion.
- **B:** Incorrect for this question. Make a passing test suite a precondition for release. Why the correct answer wins: Running the suite as a build step makes it part of promotion.
- **C:** Correct. Fail the pipeline at the test stage instead of after deployment. In this case: Running the suite as a build step makes it part of promotion.
- **D:** Incorrect for this question. Measure behaviour under expected peak traffic rather than guessing. Why the correct answer wins: Running the suite as a build step makes it part of promotion.

### Question 54 — B

Answer: Develop with Cloud Code in the IDE. A cloud-hosted editor gives both engineers the same building workspace. Editor integration for scaffolding, running and debugging on Google Cloud. Local study-map skill 2.1 (Local Emulation of Cloud Services), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 2 (building and testing applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A browser terminal with the SDK and tooling already installed. Why the correct answer wins: A cloud-hosted editor gives both engineers the same building workspace.
- **B:** Correct. Editor integration for scaffolding, running and debugging on Google Cloud. In this case: A cloud-hosted editor gives both engineers the same building workspace.
- **C:** Incorrect for this question. A local stand-in for a managed service used for unit and integration work. Why the correct answer wins: A cloud-hosted editor gives both engineers the same building workspace.
- **D:** Incorrect for this question. A managed, container-defined development environment behind a private endpoint. Why the correct answer wins: A cloud-hosted editor gives both engineers the same building workspace.

### Question 55 — B

Answer: Iterate with Skaffold. An automatic iteration loop rebuilds and redeploys on each save. A loop that rebuilds and redeploys automatically on a source change. Local study-map skill 2.3 (Container Builds with Cloud Build), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 2 (building and testing applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A managed build service that runs the steps from a build configuration file. Why the correct answer wins: An automatic iteration loop rebuilds and redeploys on each save.
- **B:** Correct. A loop that rebuilds and redeploys automatically on a source change. In this case: An automatic iteration loop rebuilds and redeploys on each save.
- **C:** Incorrect for this question. Release exactly the artifact that was tested rather than a moving tag. Why the correct answer wins: An automatic iteration loop rebuilds and redeploys on each save.
- **D:** Incorrect for this question. Run the build steps locally and push the result when someone remembers. Why the correct answer wins: An automatic iteration loop rebuilds and redeploys on each save.

### Question 56 — A, C

Answers: Deploy from source and let the platform build it; Build the image with Cloud Build. Source deployment builds from the repository, and a declared pipeline keeps the steps reproducible. Hand the source to the managed builder instead of shipping an image. A managed build service that runs the steps from a build configuration file. Local study-map skill 3.1 (Deploying Cloud Run from Source), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 3 (configuring cloud-native applications for deployment): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Correct. A managed build service that runs the steps from a build configuration file. In this case: Source deployment builds from the repository, and a declared pipeline keeps the steps reproducible.
- **B:** Incorrect for this question. Release exactly the artifact that was tested rather than a moving tag. Why the correct answer wins: Source deployment builds from the repository, and a declared pipeline keeps the steps reproducible.
- **C:** Correct. Hand the source to the managed builder instead of shipping an image. In this case: Source deployment builds from the repository, and a declared pipeline keeps the steps reproducible.
- **D:** Incorrect for this question. Wrap the existing process in a portable artifact that a managed runtime can execute. Why the correct answer wins: Source deployment builds from the repository, and a declared pipeline keeps the steps reproducible.
- **E:** Incorrect for this question. Run the build steps locally and push the result when someone remembers. Why the correct answer wins: Source deployment builds from the repository, and a declared pipeline keeps the steps reproducible.

### Question 57 — C

Answer: Enable CPU boost at startup. Keeping CPU allocated beyond the response start lets the stream finish. Give extra CPU during start-up so initialization finishes faster at a small extra charge. Local study-map skill 3.1 (Deploying Cloud Run from Source), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 3 (configuring cloud-native applications for deployment): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Pay for idle capacity so a cold start never appears in the latency percentiles. Why the correct answer wins: Keeping CPU allocated beyond the response start lets the stream finish.
- **B:** Incorrect for this question. Let each instance serve more simultaneous requests before another instance is started. Why the correct answer wins: Keeping CPU allocated beyond the response start lets the stream finish.
- **C:** Correct. Give extra CPU during start-up so initialization finishes faster at a small extra charge. In this case: Keeping CPU allocated beyond the response start lets the stream finish.
- **D:** Incorrect for this question. Charge only while a request is being handled, which suits bursty traffic. Why the correct answer wins: Keeping CPU allocated beyond the response start lets the stream finish.

### Question 58 — B

Answer: Cap the maximum instance count. A ceiling on instances bounds what a spike may spend. Bound the blast radius and the bill at the cost of queueing when the cap is reached. Local study-map skill 3.1 (Deploying Cloud Run from Source), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 3 (configuring cloud-native applications for deployment): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Allow the process the headroom it needs so it is not throttled or killed. Why the correct answer wins: A ceiling on instances bounds what a spike may spend.
- **B:** Correct. Bound the blast radius and the bill at the cost of queueing when the cap is reached. In this case: A ceiling on instances bounds what a spike may spend.
- **C:** Incorrect for this question. Charge only while a request is being handled, which suits bursty traffic. Why the correct answer wins: A ceiling on instances bounds what a spike may spend.
- **D:** Incorrect for this question. Trade a term commitment for a lower unit price on capacity that never idles. Why the correct answer wins: A ceiling on instances bounds what a spike may spend.

### Question 59 — C

Answer: Run the batch work as a Cloud Run job. A job runs the backfill to completion and then exits. A task-shaped execution that runs to completion instead of serving requests. Local study-map skill 3.1 (Deploying Cloud Run from Source), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 3 (configuring cloud-native applications for deployment): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A managed container runtime that scales to zero and bills per request while it serves traffic. Why the correct answer wins: A job runs the backfill to completion and then exits.
- **B:** Incorrect for this question. A trigger path that turns a Cloud Audit Log or resource event into a delivery. Why the correct answer wins: A job runs the backfill to completion and then exits.
- **C:** Correct. A task-shaped execution that runs to completion instead of serving requests. In this case: A job runs the backfill to completion and then exits.
- **D:** Incorrect for this question. An event-triggered function runtime for a single-purpose handler rather than a long-lived service. Why the correct answer wins: A job runs the backfill to completion and then exits.

### Question 60 — C

Answer: Grant the invoker role to the calling identity. The triggering identity needs the invoker role on the service. Control who may call the service with IAM rather than a shared token. Local study-map skill 3.2 (Cloud Run Triggers and Event Receivers), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 3 (configuring cloud-native applications for deployment): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Let anyone reach the endpoint, which is only appropriate for public content. Why the correct answer wins: The triggering identity needs the invoker role on the service.
- **B:** Incorrect for this question. Authenticate and authorize users before a request reaches the application. Why the correct answer wins: The triggering identity needs the invoker role on the service.
- **C:** Correct. Control who may call the service with IAM rather than a shared token. In this case: The triggering identity needs the invoker role on the service.
- **D:** Incorrect for this question. A lighter managed gateway for routing and key-based quota enforcement. Why the correct answer wins: The triggering identity needs the invoker role on the service.

### Question 61 — D

Answer: Have the worker pull from the subscription. Pull delivery lets the receiver choose when to fetch. The consumer controls the pace and acknowledges messages itself. Local study-map skill 3.2 (Cloud Run Triggers and Event Receivers), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 3 (configuring cloud-native applications for deployment): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A trigger path that turns a Cloud Audit Log or resource event into a delivery. Why the correct answer wins: Pull delivery lets the receiver choose when to fetch.
- **B:** Incorrect for this question. A cron-style trigger that calls a target on a fixed timetable. Why the correct answer wins: Pull delivery lets the receiver choose when to fetch.
- **C:** Incorrect for this question. Push each message to an endpoint instead of having the consumer pull. Why the correct answer wins: Pull delivery lets the receiver choose when to fetch.
- **D:** Correct. The consumer controls the pace and acknowledges messages itself. In this case: Pull delivery lets the receiver choose when to fetch.

### Question 62 — C

Answer: Route the event with Eventarc. An event trigger reacts to the audit entry as it is written. A trigger path that turns a Cloud Audit Log or resource event into a delivery. Local study-map skill 3.2 (Cloud Run Triggers and Event Receivers), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 3 (configuring cloud-native applications for deployment): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A cron-style trigger that calls a target on a fixed timetable. Why the correct answer wins: An event trigger reacts to the audit entry as it is written.
- **B:** Incorrect for this question. A task queue with retries and rate control aimed at a specific target. Why the correct answer wins: An event trigger reacts to the audit entry as it is written.
- **C:** Correct. A trigger path that turns a Cloud Audit Log or resource event into a delivery. In this case: An event trigger reacts to the audit entry as it is written.
- **D:** Incorrect for this question. A stateful sequence of service calls with retries and error branches. Why the correct answer wins: An event trigger reacts to the audit entry as it is written.

### Question 63 — D

Answer: Queue the work as a Cloud Tasks task. A task queue dispatches at the rate the partner will accept. A task queue with retries and rate control aimed at a specific target. Local study-map skill 3.2 (Cloud Run Triggers and Event Receivers), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 3 (configuring cloud-native applications for deployment): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A cron-style trigger that calls a target on a fixed timetable. Why the correct answer wins: A task queue dispatches at the rate the partner will accept.
- **B:** Incorrect for this question. A stateful sequence of service calls with retries and error branches. Why the correct answer wins: A task queue dispatches at the rate the partner will accept.
- **C:** Incorrect for this question. A durable, at-least-once message channel with independent subscribers. Why the correct answer wins: A task queue dispatches at the rate the partner will accept.
- **D:** Correct. A task queue with retries and rate control aimed at a specific target. In this case: A task queue dispatches at the rate the partner will accept.

### Question 64 — C, E

Answers: Keep a minimum number of instances warm; Cap the maximum instance count. A minimum count keeps capacity warm, and a maximum count stops the fleet growing past budget. Pay for idle capacity so a cold start never appears in the latency percentiles. Bound the blast radius and the bill at the cost of queueing when the cap is reached. Local study-map skill 3.3 (Cloud Run Service Configuration), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 3 (configuring cloud-native applications for deployment): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Let each instance serve more simultaneous requests before another instance is started. Why the correct answer wins: A minimum count keeps capacity warm, and a maximum count stops the fleet growing past budget.
- **B:** Incorrect for this question. Charge only while a request is being handled, which suits bursty traffic. Why the correct answer wins: A minimum count keeps capacity warm, and a maximum count stops the fleet growing past budget.
- **C:** Correct. Pay for idle capacity so a cold start never appears in the latency percentiles. In this case: A minimum count keeps capacity warm, and a maximum count stops the fleet growing past budget.
- **D:** Incorrect for this question. Let anyone reach the endpoint, which is only appropriate for public content. Why the correct answer wins: A minimum count keeps capacity warm, and a maximum count stops the fleet growing past budget.
- **E:** Correct. Bound the blast radius and the bill at the cost of queueing when the cap is reached. In this case: A minimum count keeps capacity warm, and a maximum count stops the fleet growing past budget.

### Question 65 — D

Answer: Restrict ingress to internal traffic. Internal ingress rejects traffic that did not originate inside the network. Accept only traffic from the VPC and internal load balancers. Local study-map skill 3.3 (Cloud Run Service Configuration), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 3 (configuring cloud-native applications for deployment): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Let anyone reach the endpoint, which is only appropriate for public content. Why the correct answer wins: Internal ingress rejects traffic that did not originate inside the network.
- **B:** Incorrect for this question. A single anycast address that routes to the nearest healthy backend. Why the correct answer wins: Internal ingress rejects traffic that did not originate inside the network.
- **C:** Incorrect for this question. Authenticate and authorize users before a request reaches the application. Why the correct answer wins: Internal ingress rejects traffic that did not originate inside the network.
- **D:** Correct. Accept only traffic from the VPC and internal load balancers. In this case: Internal ingress rejects traffic that did not originate inside the network.

### Question 66 — B

Answer: Allow unauthenticated invocations. Allowing unauthenticated calls lets the public page be read by anyone. Let anyone reach the endpoint, which is only appropriate for public content. Local study-map skill 3.3 (Cloud Run Service Configuration), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 3 (configuring cloud-native applications for deployment): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Accept only traffic from the VPC and internal load balancers. Why the correct answer wins: Allowing unauthenticated calls lets the public page be read by anyone.
- **B:** Correct. Let anyone reach the endpoint, which is only appropriate for public content. In this case: Allowing unauthenticated calls lets the public page be read by anyone.
- **C:** Incorrect for this question. Control who may call the service with IAM rather than a shared token. Why the correct answer wins: Allowing unauthenticated calls lets the public page be read by anyone.
- **D:** Incorrect for this question. Authenticate and authorize users before a request reaches the application. Why the correct answer wins: Allowing unauthenticated calls lets the public page be read by anyone.

### Question 67 — B

Answer: Put a global external Application Load Balancer in front. A global front door gives the single hostname and managed certificate. A single anycast address that routes to the nearest healthy backend. Local study-map skill 3.4 (API Exposure and Versioning), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 3 (configuring cloud-native applications for deployment): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Accept only traffic from the VPC and internal load balancers. Why the correct answer wins: A global front door gives the single hostname and managed certificate.
- **B:** Correct. A single anycast address that routes to the nearest healthy backend. In this case: A global front door gives the single hostname and managed certificate.
- **C:** Incorrect for this question. A lighter managed gateway for routing and key-based quota enforcement. Why the correct answer wins: A global front door gives the single hostname and managed certificate.
- **D:** Incorrect for this question. A load balancer scoped to one region with a regional address. Why the correct answer wins: A global front door gives the single hostname and managed certificate.

### Question 68 — B

Answer: Introduce a new API version alongside the old one. Serving a new version alongside the old keeps unchanged consumers working. Keep the old contract working while the new one is adopted. Local study-map skill 3.4 (API Exposure and Versioning), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 3 (configuring cloud-native applications for deployment): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Extend the contract so existing clients keep working unchanged. Why the correct answer wins: Serving a new version alongside the old keeps unchanged consumers working.
- **B:** Correct. Keep the old contract working while the new one is adopted. In this case: Serving a new version alongside the old keeps unchanged consumers working.
- **C:** Incorrect for this question. A machine-readable contract that generates clients and validates requests. Why the correct answer wins: Serving a new version alongside the old keeps unchanged consumers working.
- **D:** Incorrect for this question. An API management layer for quotas, keys, mediation and analytics. Why the correct answer wins: Serving a new version alongside the old keeps unchanged consumers working.

### Question 69 — B

Answer: Use GKE Autopilot for the cluster. The managed mode provisions and patches the nodes for the team. A cluster mode where node provisioning and sizing are handled for the workload. Local study-map skill 3.5 (Deploying Containers to GKE), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 3 (configuring cloud-native applications for deployment): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Add or remove nodes as pending pods demand capacity. Why the correct answer wins: The managed mode provisions and patches the nodes for the team.
- **B:** Correct. A cluster mode where node provisioning and sizing are handled for the workload. In this case: The managed mode provisions and patches the nodes for the team.
- **C:** Incorrect for this question. Use reclaimable capacity for work that can tolerate a node disappearing. Why the correct answer wins: The managed mode provisions and patches the nodes for the team.
- **D:** Incorrect for this question. Place work on nodes whose shape and pricing match the workload. Why the correct answer wins: The managed mode provisions and patches the nodes for the team.

### Question 70 — C

Answer: Bind a Kubernetes service account to a Google service account. Binding the pod's identity lets it get tokens with no key file. Keyless credential issuance for pods through Workload Identity. Local study-map skill 3.5 (Deploying Containers to GKE), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 3 (configuring cloud-native applications for deployment): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A dedicated identity whose roles can be granted and revoked independently. Why the correct answer wins: Binding the pod's identity lets it get tokens with no key file.
- **B:** Incorrect for this question. A long-lived credential that has to be stored and rotated by hand. Why the correct answer wins: Binding the pod's identity lets it get tokens with no key file.
- **C:** Correct. Keyless credential issuance for pods through Workload Identity. In this case: Binding the pod's identity lets it get tokens with no key file.
- **D:** Incorrect for this question. Exchange an outside token for a short-lived Google credential. Why the correct answer wins: Binding the pod's identity lets it get tokens with no key file.

### Question 71 — C

Answer: Use a rolling update strategy. Replacing pods in batches keeps serving throughout the release. Replace pods gradually so the deployment stays available. Local study-map skill 3.5 (Deploying Containers to GKE), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 3 (configuring cloud-native applications for deployment): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Use reclaimable capacity for work that can tolerate a node disappearing. Why the correct answer wins: Replacing pods in batches keeps serving throughout the release.
- **B:** Incorrect for this question. Control how much capacity may be missing while pods are replaced. Why the correct answer wins: Replacing pods in batches keeps serving throughout the release.
- **C:** Correct. Replace pods gradually so the deployment stays available. In this case: Replacing pods in batches keeps serving throughout the release.
- **D:** Incorrect for this question. Place work on nodes whose shape and pricing match the workload. Why the correct answer wins: Replacing pods in batches keeps serving throughout the release.

### Question 72 — A

Answer: Tune maxSurge and maxUnavailable. Bounding unavailable pods replaces in place without extra capacity. Control how much capacity may be missing while pods are replaced. Local study-map skill 3.5 (Deploying Containers to GKE), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 3 (configuring cloud-native applications for deployment): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Correct. Control how much capacity may be missing while pods are replaced. In this case: Bounding unavailable pods replaces in place without extra capacity.
- **B:** Incorrect for this question. Replace pods gradually so the deployment stays available. Why the correct answer wins: Bounding unavailable pods replaces in place without extra capacity.
- **C:** Incorrect for this question. Add or remove nodes as pending pods demand capacity. Why the correct answer wins: Bounding unavailable pods replaces in place without extra capacity.
- **D:** Incorrect for this question. Limit how many pods may be evicted at once during voluntary disruption. Why the correct answer wins: Bounding unavailable pods replaces in place without extra capacity.

### Question 73 — A, E

Answers: Configure a liveness probe; Configure a readiness probe. A liveness probe restarts the wedged container, and a readiness probe holds traffic until it can serve. Restart the container when it can no longer make progress. Remove the instance from the endpoint list while it cannot serve. Local study-map skill 3.6 (Kubernetes Health Checks), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 3 (configuring cloud-native applications for deployment): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Correct. Remove the instance from the endpoint list while it cannot serve. In this case: A liveness probe restarts the wedged container, and a readiness probe holds traffic until it can serve.
- **B:** Incorrect for this question. Control how much capacity may be missing while pods are replaced. Why the correct answer wins: A liveness probe restarts the wedged container, and a readiness probe holds traffic until it can serve.
- **C:** Incorrect for this question. Limit how many pods may be evicted at once during voluntary disruption. Why the correct answer wins: A liveness probe restarts the wedged container, and a readiness probe holds traffic until it can serve.
- **D:** Incorrect for this question. Hold traffic until the application is actually ready to serve. Why the correct answer wins: A liveness probe restarts the wedged container, and a readiness probe holds traffic until it can serve.
- **E:** Correct. Restart the container when it can no longer make progress. In this case: A liveness probe restarts the wedged container, and a readiness probe holds traffic until it can serve.

### Question 74 — D

Answer: Configure a startup probe. A startup probe allows the long initialisation before any restart. Hold traffic until the application is actually ready to serve. Local study-map skill 3.6 (Kubernetes Health Checks), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 3 (configuring cloud-native applications for deployment): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Restart the container when it can no longer make progress. Why the correct answer wins: A startup probe allows the long initialisation before any restart.
- **B:** Incorrect for this question. Limit how many pods may be evicted at once during voluntary disruption. Why the correct answer wins: A startup probe allows the long initialisation before any restart.
- **C:** Incorrect for this question. Remove the instance from the endpoint list while it cannot serve. Why the correct answer wins: A startup probe allows the long initialisation before any restart.
- **D:** Correct. Hold traffic until the application is actually ready to serve. In this case: A startup probe allows the long initialisation before any restart.

### Question 75 — D

Answer: Add a health check endpoint to the backend service. A health check removes the backend while it cannot serve. Let the load balancer stop sending traffic to an unhealthy instance. Local study-map skill 3.6 (Kubernetes Health Checks), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 3 (configuring cloud-native applications for deployment): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Control how much capacity may be missing while pods are replaced. Why the correct answer wins: A health check removes the backend while it cannot serve.
- **B:** Incorrect for this question. Remove the instance from the endpoint list while it cannot serve. Why the correct answer wins: A health check removes the backend while it cannot serve.
- **C:** Incorrect for this question. Limit how many pods may be evicted at once during voluntary disruption. Why the correct answer wins: A health check removes the backend while it cannot serve.
- **D:** Correct. Let the load balancer stop sending traffic to an unhealthy instance. In this case: A health check removes the backend while it cannot serve.

### Question 76 — A, B

Answers: Scale pods on CPU utilization; Set a minimum replica count. Scaling on utilisation adds pods under load, and a replica floor keeps two available. Add pods when average CPU crosses the target. Keep capacity warm so scale-up does not cost the first requests. Local study-map skill 3.7 (Horizontal Pod Autoscaling), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 3 (configuring cloud-native applications for deployment): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Correct. Add pods when average CPU crosses the target. In this case: Scaling on utilisation adds pods under load, and a replica floor keeps two available.
- **B:** Correct. Keep capacity warm so scale-up does not cost the first requests. In this case: Scaling on utilisation adds pods under load, and a replica floor keeps two available.
- **C:** Incorrect for this question. Add or remove nodes as pending pods demand capacity. Why the correct answer wins: Scaling on utilisation adds pods under load, and a replica floor keeps two available.
- **D:** Incorrect for this question. Add pods on a signal that tracks demand better than CPU. Why the correct answer wins: Scaling on utilisation adds pods under load, and a replica floor keeps two available.
- **E:** Incorrect for this question. Limit how many pods may be evicted at once during voluntary disruption. Why the correct answer wins: Scaling on utilisation adds pods under load, and a replica floor keeps two available.

### Question 77 — B

Answer: Scale pods on a custom or external metric. A custom metric lets scaling follow the backlog instead of CPU. Add pods on a signal that tracks demand better than CPU. Local study-map skill 3.7 (Horizontal Pod Autoscaling), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 3 (configuring cloud-native applications for deployment): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Add or remove nodes as pending pods demand capacity. Why the correct answer wins: A custom metric lets scaling follow the backlog instead of CPU.
- **B:** Correct. Add pods on a signal that tracks demand better than CPU. In this case: A custom metric lets scaling follow the backlog instead of CPU.
- **C:** Incorrect for this question. Trade a term commitment for a lower unit price on capacity that never idles. Why the correct answer wins: A custom metric lets scaling follow the backlog instead of CPU.
- **D:** Incorrect for this question. Add pods when average CPU crosses the target. Why the correct answer wins: A custom metric lets scaling follow the backlog instead of CPU.

### Question 78 — A

Answer: Enable node pool autoscaling. Node pool autoscaling adds the nodes those pods need. Add or remove nodes as pending pods demand capacity. Local study-map skill 3.7 (Horizontal Pod Autoscaling), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 3 (configuring cloud-native applications for deployment): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Correct. Add or remove nodes as pending pods demand capacity. In this case: Node pool autoscaling adds the nodes those pods need.
- **B:** Incorrect for this question. Limit how many pods may be evicted at once during voluntary disruption. Why the correct answer wins: Node pool autoscaling adds the nodes those pods need.
- **C:** Incorrect for this question. Place work on nodes whose shape and pricing match the workload. Why the correct answer wins: Node pool autoscaling adds the nodes those pods need.
- **D:** Incorrect for this question. Add pods when average CPU crosses the target. Why the correct answer wins: Node pool autoscaling adds the nodes those pods need.

### Question 79 — A

Answer: Raise the per-instance concurrency limit. Raising per-instance concurrency packs more streams onto each instance. Let each instance serve more simultaneous requests before another instance is started. Local study-map skill 3.3 (Cloud Run Service Configuration), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 3 (configuring cloud-native applications for deployment): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Correct. Let each instance serve more simultaneous requests before another instance is started. In this case: Raising per-instance concurrency packs more streams onto each instance.
- **B:** Incorrect for this question. Bound the blast radius and the bill at the cost of queueing when the cap is reached. Why the correct answer wins: Raising per-instance concurrency packs more streams onto each instance.
- **C:** Incorrect for this question. Pay for idle capacity so a cold start never appears in the latency percentiles. Why the correct answer wins: Raising per-instance concurrency packs more streams onto each instance.
- **D:** Incorrect for this question. Charge only while a request is being handled, which suits bursty traffic. Why the correct answer wins: Raising per-instance concurrency packs more streams onto each instance.

### Question 80 — C

Answer: Connect through the Cloud SQL Auth Proxy. A proxy sidecar provides the tunnel for languages without a connector. A local proxy that authorizes the connection with IAM and encrypts it. Local study-map skill 4.1 (Connecting to Datastores), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 4 (integrating applications with Google Cloud services): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A private address reachable from the VPC without a proxy process. Why the correct answer wins: A proxy sidecar provides the tunnel for languages without a connector.
- **B:** Incorrect for this question. A private endpoint that consumes a published service without peering. Why the correct answer wins: A proxy sidecar provides the tunnel for languages without a connector.
- **C:** Correct. A local proxy that authorizes the connection with IAM and encrypts it. In this case: A proxy sidecar provides the tunnel for languages without a connector.
- **D:** Incorrect for this question. A client library that resolves and authorizes the instance itself. Why the correct answer wins: A proxy sidecar provides the tunnel for languages without a connector.

### Question 81 — A

Answer: Pool and reuse database connections. Reusing pooled connections removes the per-call handshake. Keep a small set of warm connections instead of opening one per request. Local study-map skill 4.1 (Connecting to Datastores), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 4 (integrating applications with Google Cloud services): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Correct. Keep a small set of warm connections instead of opening one per request. In this case: Reusing pooled connections removes the per-call handshake.
- **B:** Incorrect for this question. A private endpoint that consumes a published service without peering. Why the correct answer wins: Reusing pooled connections removes the per-call handshake.
- **C:** Incorrect for this question. Allow the process the headroom it needs so it is not throttled or killed. Why the correct answer wins: Reusing pooled connections removes the per-call handshake.
- **D:** Incorrect for this question. Change the engine-level connection limit without resizing the machine. Why the correct answer wins: Reusing pooled connections removes the per-call handshake.

### Question 82 — A

Answer: Connect through the AlloyDB Auth Proxy. The proxy authenticates the client and handles the certificates. The equivalent authorized connector for AlloyDB instances. Local study-map skill 4.1 (Connecting to Datastores), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 4 (integrating applications with Google Cloud services): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Correct. The equivalent authorized connector for AlloyDB instances. In this case: The proxy authenticates the client and handles the certificates.
- **B:** Incorrect for this question. A local proxy that authorizes the connection with IAM and encrypts it. Why the correct answer wins: The proxy authenticates the client and handles the certificates.
- **C:** Incorrect for this question. A private endpoint that consumes a published service without peering. Why the correct answer wins: The proxy authenticates the client and handles the certificates.
- **D:** Incorrect for this question. A client library that resolves and authorizes the instance itself. Why the correct answer wins: The proxy authenticates the client and handles the certificates.

### Question 83 — B

Answer: Reach the service through Private Service Connect. A private service endpoint keeps the traffic off the internet. A private endpoint that consumes a published service without peering. Local study-map skill 4.1 (Connecting to Datastores), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 4 (integrating applications with Google Cloud services): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A private address reachable from the VPC without a proxy process. Why the correct answer wins: A private service endpoint keeps the traffic off the internet.
- **B:** Correct. A private endpoint that consumes a published service without peering. In this case: A private service endpoint keeps the traffic off the internet.
- **C:** Incorrect for this question. A local proxy that authorizes the connection with IAM and encrypts it. Why the correct answer wins: A private service endpoint keeps the traffic off the internet.
- **D:** Incorrect for this question. A reachable address that requires encrypted connections from any client. Why the correct answer wins: A private service endpoint keeps the traffic off the internet.

### Question 84 — A

Answer: Expose the database on a public address with enforced SSL. An authorised public address with TLS meets the interim need. A reachable address that requires encrypted connections from any client. Local study-map skill 4.1 (Connecting to Datastores), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 4 (integrating applications with Google Cloud services): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Correct. A reachable address that requires encrypted connections from any client. In this case: An authorised public address with TLS meets the interim need.
- **B:** Incorrect for this question. A private address reachable from the VPC without a proxy process. Why the correct answer wins: An authorised public address with TLS meets the interim need.
- **C:** Incorrect for this question. A private endpoint that consumes a published service without peering. Why the correct answer wins: An authorised public address with TLS meets the interim need.
- **D:** Incorrect for this question. A client library that resolves and authorizes the instance itself. Why the correct answer wins: An authorised public address with TLS meets the interim need.

### Question 85 — A, E

Answers: Add a dead-letter topic; Make the handler idempotent with a deduplication key. A dead-letter topic stops the poison message, and an idempotency key absorbs the duplicate delivery. Hold messages that exhausted their delivery attempts for later inspection. Recognise a repeated delivery and skip the duplicate work. Local study-map skill 4.2 (Publishing and Consuming Messages), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 4 (integrating applications with Google Cloud services): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Correct. Hold messages that exhausted their delivery attempts for later inspection. In this case: A dead-letter topic stops the poison message, and an idempotency key absorbs the duplicate delivery.
- **B:** Incorrect for this question. Space out repeated attempts so a throttled quota can recover instead of being hammered. Why the correct answer wins: A dead-letter topic stops the poison message, and an idempotency key absorbs the duplicate delivery.
- **C:** Incorrect for this question. Push each message to an endpoint instead of having the consumer pull. Why the correct answer wins: A dead-letter topic stops the poison message, and an idempotency key absorbs the duplicate delivery.
- **D:** Incorrect for this question. The consumer controls the pace and acknowledges messages itself. Why the correct answer wins: A dead-letter topic stops the poison message, and an idempotency key absorbs the duplicate delivery.
- **E:** Correct. Recognise a repeated delivery and skip the duplicate work. In this case: A dead-letter topic stops the poison message, and an idempotency key absorbs the duplicate delivery.

### Question 86 — D

Answer: Deliver to an HTTPS push subscription. Push delivery posts each message to the vendor's endpoint. Push each message to an endpoint instead of having the consumer pull. Local study-map skill 4.2 (Publishing and Consuming Messages), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 4 (integrating applications with Google Cloud services): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A task queue with retries and rate control aimed at a specific target. Why the correct answer wins: Push delivery posts each message to the vendor's endpoint.
- **B:** Incorrect for this question. The consumer controls the pace and acknowledges messages itself. Why the correct answer wins: Push delivery posts each message to the vendor's endpoint.
- **C:** Incorrect for this question. A trigger path that turns a Cloud Audit Log or resource event into a delivery. Why the correct answer wins: Push delivery posts each message to the vendor's endpoint.
- **D:** Correct. Push each message to an endpoint instead of having the consumer pull. In this case: Push delivery posts each message to the vendor's endpoint.

### Question 87 — B

Answer: Use a BigQuery subscription on the topic. A subscription that writes to the table removes the service to maintain. Write topic messages straight into a table without a consumer. Local study-map skill 4.2 (Publishing and Consuming Messages), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 4 (integrating applications with Google Cloud services): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Durable object storage addressed by name rather than a database row. Why the correct answer wins: A subscription that writes to the table removes the service to maintain.
- **B:** Correct. Write topic messages straight into a table without a consumer. In this case: A subscription that writes to the table removes the service to maintain.
- **C:** Incorrect for this question. Load a periodic extract rather than a continuous stream. Why the correct answer wins: A subscription that writes to the table removes the service to maintain.
- **D:** Incorrect for this question. The consumer controls the pace and acknowledges messages itself. Why the correct answer wins: A subscription that writes to the table removes the service to maintain.

### Question 88 — A

Answer: Retry with exponential backoff and jitter. Waiting longer between attempts makes retries succeed under throttle. Space out repeated attempts so a throttled quota can recover instead of being hammered. Local study-map skill 4.3 (Calling Google Cloud APIs), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 4 (integrating applications with Google Cloud services): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Correct. Space out repeated attempts so a throttled quota can recover instead of being hammered. In this case: Waiting longer between attempts makes retries succeed under throttle.
- **B:** Incorrect for this question. Allow the process the headroom it needs so it is not throttled or killed. Why the correct answer wins: Waiting longer between attempts makes retries succeed under throttle.
- **C:** Incorrect for this question. Bound how many calls a plan allows in a window. Why the correct answer wins: Waiting longer between attempts makes retries succeed under throttle.
- **D:** Incorrect for this question. Reduce per-call overhead when the API supports a batch surface. Why the correct answer wins: Waiting longer between attempts makes retries succeed under throttle.

### Question 89 — C

Answer: Follow the page token until results are exhausted. Following the page tokens continues past the first page. Request each page in turn so a truncated response is completed rather than assumed whole. Local study-map skill 4.3 (Calling Google Cloud APIs), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 4 (integrating applications with Google Cloud services): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Reuse a result that has not changed, avoiding an identical call. Why the correct answer wins: Following the page tokens continues past the first page.
- **B:** Incorrect for this question. Reduce per-call overhead when the API supports a batch surface. Why the correct answer wins: Following the page tokens continues past the first page.
- **C:** Correct. Request each page in turn so a truncated response is completed rather than assumed whole. In this case: Following the page tokens continues past the first page.
- **D:** Incorrect for this question. Trim the response payload so latency and cost follow actual use. Why the correct answer wins: Following the page tokens continues past the first page.

### Question 90 — C

Answer: Request only the fields the caller needs. A field mask returns only the three values shown. Trim the response payload so latency and cost follow actual use. Local study-map skill 4.3 (Calling Google Cloud APIs), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 4 (integrating applications with Google Cloud services): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Reuse a result that has not changed, avoiding an identical call. Why the correct answer wins: A field mask returns only the three values shown.
- **B:** Incorrect for this question. Reduce per-call overhead when the API supports a batch surface. Why the correct answer wins: A field mask returns only the three values shown.
- **C:** Correct. Trim the response payload so latency and cost follow actual use. In this case: A field mask returns only the three values shown.
- **D:** Incorrect for this question. Request each page in turn so a truncated response is completed rather than assumed whole. Why the correct answer wins: A field mask returns only the three values shown.

### Question 91 — B

Answer: Cache the response for its freshness window. Caching the response avoids repeating a call for stable data. Reuse a result that has not changed, avoiding an identical call. Local study-map skill 4.3 (Calling Google Cloud APIs), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 4 (integrating applications with Google Cloud services): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Space out repeated attempts so a throttled quota can recover instead of being hammered. Why the correct answer wins: Caching the response avoids repeating a call for stable data.
- **B:** Correct. Reuse a result that has not changed, avoiding an identical call. In this case: Caching the response avoids repeating a call for stable data.
- **C:** Incorrect for this question. Request each page in turn so a truncated response is completed rather than assumed whole. Why the correct answer wins: Caching the response avoids repeating a call for stable data.
- **D:** Incorrect for this question. Change the engine-level connection limit without resizing the machine. Why the correct answer wins: Caching the response avoids repeating a call for stable data.

### Question 92 — C

Answer: Give the workload its own service account. A dedicated identity with only the needed role limits what it can read. A dedicated identity whose roles can be granted and revoked independently. Local study-map skill 4.4 (Service Accounts for API Calls), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 4 (integrating applications with Google Cloud services): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. The automatically created identity that usually carries broad project access. Why the correct answer wins: A dedicated identity with only the needed role limits what it can read.
- **B:** Incorrect for this question. A legacy broad role that can change most resources in the project. Why the correct answer wins: A dedicated identity with only the needed role limits what it can read.
- **C:** Correct. A dedicated identity whose roles can be granted and revoked independently. In this case: A dedicated identity with only the needed role limits what it can read.
- **D:** Incorrect for this question. A role built from an explicit permission list. Why the correct answer wins: A dedicated identity with only the needed role limits what it can read.

### Question 93 — A

Answer: Federate the external identity with Workload Identity Federation. Federating the external identity removes the stored key. Exchange an outside token for a short-lived Google credential. Local study-map skill 4.4 (Service Accounts for API Calls), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 4 (integrating applications with Google Cloud services): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Correct. Exchange an outside token for a short-lived Google credential. In this case: Federating the external identity removes the stored key.
- **B:** Incorrect for this question. A dedicated identity whose roles can be granted and revoked independently. Why the correct answer wins: Federating the external identity removes the stored key.
- **C:** Incorrect for this question. A long-lived credential that has to be stored and rotated by hand. Why the correct answer wins: Federating the external identity removes the stored key.
- **D:** Incorrect for this question. Let the client library find credentials from the environment. Why the correct answer wins: Federating the external identity removes the stored key.

### Question 94 — C, D

Answers: Build a log-based metric; Create an alerting policy on the metric. A log-based metric turns matching entries into a number, and an alert policy pages on it. Turn a recurring log pattern into a number that can be charted and alerted on. Notify a human when a threshold is crossed. Local study-map skill 4.5 (Metrics, Logs, and Traces), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 4 (integrating applications with Google Cloud services): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Publish an application signal that infrastructure metrics cannot see. Why the correct answer wins: A log-based metric turns matching entries into a number, and an alert policy pages on it.
- **B:** Incorrect for this question. Page on the rate at which reliability is being spent. Why the correct answer wins: A log-based metric turns matching entries into a number, and an alert policy pages on it.
- **C:** Correct. Notify a human when a threshold is crossed. In this case: A log-based metric turns matching entries into a number, and an alert policy pages on it.
- **D:** Correct. Turn a recurring log pattern into a number that can be charted and alerted on. In this case: A log-based metric turns matching entries into a number, and an alert policy pages on it.
- **E:** Incorrect for this question. Let filters and alerting distinguish routine output from errors. Why the correct answer wins: A log-based metric turns matching entries into a number, and an alert policy pages on it.

### Question 95 — A

Answer: Alert on the error budget burn rate. Alerting on the objective's error budget tracks what users experience. Page on the rate at which reliability is being spent. Local study-map skill 4.5 (Metrics, Logs, and Traces), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 4 (integrating applications with Google Cloud services): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Correct. Page on the rate at which reliability is being spent. In this case: Alerting on the objective's error budget tracks what users experience.
- **B:** Incorrect for this question. Notify a human when a threshold is crossed. Why the correct answer wins: Alerting on the objective's error budget tracks what users experience.
- **C:** Incorrect for this question. Let filters and alerting distinguish routine output from errors. Why the correct answer wins: Alerting on the objective's error budget tracks what users experience.
- **D:** Incorrect for this question. Publish an application signal that infrastructure metrics cannot see. Why the correct answer wins: Alerting on the objective's error budget tracks what users experience.

### Question 96 — A

Answer: Set the correct severity on each entry. Setting the severity field makes level filters work on the entry. Let filters and alerting distinguish routine output from errors. Local study-map skill 4.5 (Metrics, Logs, and Traces), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 4 (integrating applications with Google Cloud services): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Correct. Let filters and alerting distinguish routine output from errors. In this case: Setting the severity field makes level filters work on the entry.
- **B:** Incorrect for this question. Emit fields the log viewer can index so queries and alerts are possible. Why the correct answer wins: Setting the severity field makes level filters work on the entry.
- **C:** Incorrect for this question. Group and count application errors instead of grepping logs. Why the correct answer wins: Setting the severity field makes level filters work on the entry.
- **D:** Incorrect for this question. Turn a recurring log pattern into a number that can be charted and alerted on. Why the correct answer wins: Setting the severity field makes level filters work on the entry.

### Question 97 — A

Answer: Send the exception to Error Reporting. Grouping errors by release shows which version introduced the fault. Group and count application errors instead of grepping logs. Local study-map skill 4.6 (Error Reporting and Trace Correlation), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 4 (integrating applications with Google Cloud services): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Correct. Group and count application errors instead of grepping logs. In this case: Grouping errors by release shows which version introduced the fault.
- **B:** Incorrect for this question. Turn a recurring log pattern into a number that can be charted and alerted on. Why the correct answer wins: Grouping errors by release shows which version introduced the fault.
- **C:** Incorrect for this question. Notify a human when a threshold is crossed. Why the correct answer wins: Grouping errors by release shows which version introduced the fault.
- **D:** Incorrect for this question. Read variable state in a running deployment without redeploying. Why the correct answer wins: Grouping errors by release shows which version introduced the fault.

### Question 98 — C

Answer: Propagate the trace ID between services. Propagating the trace header lets one query find every service's entries. Join spans from different services into one trace. Local study-map skill 4.6 (Error Reporting and Trace Correlation), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 4 (integrating applications with Google Cloud services): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Show where time goes inside a request that crosses services. Why the correct answer wins: Propagating the trace header lets one query find every service's entries.
- **B:** Incorrect for this question. Emit fields the log viewer can index so queries and alerts are possible. Why the correct answer wins: Propagating the trace header lets one query find every service's entries.
- **C:** Correct. Join spans from different services into one trace. In this case: Propagating the trace header lets one query find every service's entries.
- **D:** Incorrect for this question. Let filters and alerting distinguish routine output from errors. Why the correct answer wins: Propagating the trace header lets one query find every service's entries.

### Question 99 — A

Answer: Ask Gemini Cloud Assist for a diagnosis. An AI assistant gathers the anomaly context and points at the likely change. An assistant that reads telemetry and proposes a cause and a next step. Local study-map skill 4.7 (AI-Assisted Observability), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 4 (integrating applications with Google Cloud services): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Correct. An assistant that reads telemetry and proposes a cause and a next step. In this case: An AI assistant gathers the anomaly context and points at the likely change.
- **B:** Incorrect for this question. Generate a first draft from context, then review and correct it. Why the correct answer wins: An AI assistant gathers the anomaly context and points at the likely change.
- **C:** Incorrect for this question. Give the assistant a defined tool surface instead of pasting context by hand. Why the correct answer wins: An AI assistant gathers the anomaly context and points at the likely change.
- **D:** Incorrect for this question. Group and count application errors instead of grepping logs. Why the correct answer wins: An AI assistant gathers the anomaly context and points at the likely change.

### Question 100 — C

Answer: Retry with exponential backoff and jitter. A retry policy with backoff holds the message until the downstream recovers. Space out repeated attempts so a throttled quota can recover instead of being hammered. Local study-map skill 4.2 (Publishing and Consuming Messages), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 4 (integrating applications with Google Cloud services): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Recognise a repeated delivery and skip the duplicate work. Why the correct answer wins: A retry policy with backoff holds the message until the downstream recovers.
- **B:** Incorrect for this question. The consumer controls the pace and acknowledges messages itself. Why the correct answer wins: A retry policy with backoff holds the message until the downstream recovers.
- **C:** Correct. Space out repeated attempts so a throttled quota can recover instead of being hammered. In this case: A retry policy with backoff holds the message until the downstream recovers.
- **D:** Incorrect for this question. Hold messages that exhausted their delivery attempts for later inspection. Why the correct answer wins: A retry policy with backoff holds the message until the downstream recovers.
