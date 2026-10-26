# Google Cloud Professional Cloud Developer — Full-Length Mock Exam 1

Professional Cloud Developer · 100 questions · expanded practice bank · passing score not published

Blueprint-weighted mock exam. Item mix: 84 multiple-choice and 16 multiple-select items (the selection count is stated in each multi-select stem). The live exam publishes 50-60 multiple-choice and multiple-select questions and has no case-study component, so this set is larger on purpose and no case-study item is reproduced. The live paper allows two hours for 50-60 items, so this 100-item set is a slower-per-item rehearsal: about 72 seconds per item here against roughly 120-144 seconds live. Use it to build a habit of finishing with time to review. See the README for the exact fidelity boundary.

Original educational content, not actual, recalled, or copied Google exam items.

## Questions

---

## Domain 1 — Designing Highly Scalable, Secure, and Reliable Cloud-Native Applications (Compute Choice, APIs, and Secure Design)

### 1. A ticket-reservation team has a single stateless HTTP service, traffic arrives in sharp bursts around each on-sale, and nobody wants to manage nodes or an OS. Which platform fits?

- A. Deploy to App Engine standard
- B. Run the application on Compute Engine instances
- C. Deploy the service to Cloud Run
- D. Deploy the workload to Google Kubernetes Engine

### 2. A media platform needs per-pod sidecars, a DaemonSet for log shipping, and fine-grained scheduling across mixed machine shapes. Which two decisions fit? Select two.

- A. Enable node pool autoscaling
- B. Deploy the service to Cloud Run
- C. Deploy the handler as a Cloud Functions function
- D. Deploy to App Engine standard
- E. Deploy the workload to Google Kubernetes Engine

### 3. A legacy service needs a kernel module, a specific Windows build, and a licence bound to the host, and the team accepts managing the machine. Which platform fits?

- A. Run the application on Compute Engine instances
- B. Deploy the workload to Google Kubernetes Engine
- C. Deploy the service to Cloud Run
- D. Deploy the handler as a Cloud Functions function

### 4. A monolith executing as a scheduled script must reach the same environment as production, scale on HTTP, and stop depending on a hand-configured server. What should the team do first?

- A. Deploy the handler as a Cloud Functions function
- B. Package the monolith into a container image
- C. Deploy to App Engine standard
- D. Schedule the invocation with Cloud Scheduler

### 5. A service must survive the loss of a single zone with no operator action and has no regulatory reason to leave the region. Which design fits?

- A. Deploy in one region across multiple zones
- B. Deploy the service in two regions behind a global load balancer
- C. Buy committed use discounts for the steady baseline
- D. Place the workload in a single zone

### 6. A global marketplace must keep serving when an entire region degrades, and the team accepts the cost of a second region. Which design fits?

- A. Enable session affinity on the backend service
- B. Deploy in one region across multiple zones
- C. Deploy the service in two regions behind a global load balancer
- D. Buy committed use discounts for the steady baseline

### 7. A compliance review asks why a stateful reporting service needs sticky sessions, and the team must keep behaviour unchanged this quarter. Which setting fits?

- A. Use a generated cookie for stickiness
- B. Store session state in a shared datastore
- C. Load through a cache-aside pattern
- D. Enable session affinity on the backend service

### 8. A team is rebuilding a service so that any instance can serve any request while one global address still fronts it. Which two changes deliver that? Select two.

- A. Use a generated cookie for stickiness
- B. Serve static content from Cloud CDN
- C. Store session state in a shared datastore
- D. Enable session affinity on the backend service
- E. Put a global external Application Load Balancer in front

### 9. A product catalogue is read-heavy, the same few thousand rows dominate traffic, and every instance must see the same cached value. Which choice fits?

- A. Cache inside each instance process
- B. Serve static content from Cloud CDN
- C. Cache reads in Memorystore
- D. Load through a cache-aside pattern

### 10. Image and JavaScript assets are re-fetched from the origin on every page load in a country far from the region. What should the team add?

- A. Cache inside each instance process
- B. Serve static content from Cloud CDN
- C. Cache reads in Memorystore
- D. Load through a cache-aside pattern

### 11. Two internal services exchange high-frequency binary payloads with streaming and generated client stubs in three languages. Which interface fits?

- A. Expose a gRPC service
- B. Expose a REST API with JSON payloads
- C. Serve gRPC-Web for browser clients
- D. Publish an OpenAPI specification

### 12. A partner integration is contracted with a third party that needs a machine-readable interface description, and the calls are ordinary browser-friendly HTTP. Which artifact should the team publish?

- A. Publish an OpenAPI specification
- B. Expose a gRPC service
- C. Serve gRPC-Web for browser clients
- D. Cache inside each instance process

### 13. One tenant's batch client is saturating a shared API and degrading every other tenant. What should the team add?

- A. Set a quota per API key
- B. Introduce a new API version alongside the old one
- C. Apply a rate limit per client key
- D. Add the field in a backward-compatible way

### 14. A commercial API must meter usage against customer plans, issue keys, and publish usage analytics to the business. Which two capabilities are needed? Select two.

- A. Use API Gateway for the API
- B. Put Apigee in front of the API
- C. Set a quota per API key
- D. Introduce a new API version alongside the old one
- E. Apply a rate limit per client key

### 15. A payment handler receives the same message twice during a retry and charges the customer twice. What must the handler add?

- A. Queue the work as a Cloud Tasks task
- B. Make the handler idempotent with a deduplication key
- C. Add a dead-letter topic
- D. Publish the event to a Pub/Sub topic

### 16. A subscriber fails on a malformed message and retries it forever, blocking the backlog behind it. What should the team configure?

- A. Add a dead-letter topic
- B. Have the worker pull from the subscription
- C. Deliver to an HTTPS push subscription
- D. Make the handler idempotent with a deduplication key

### 17. A Kubernetes deployment asks for four CPUs per pod while measured use peaks at four hundred millicores, and the cluster cannot schedule new pods. What should change?

- A. Buy committed use discounts for the steady baseline
- B. Cap the maximum instance count
- C. Set CPU and memory requests from measured use
- D. Raise the container limits above the observed peak

### 18. A cost review finds a service scaled to two hundred instances during a retry storm and reserving far more CPU than it used. Which two controls address that? Select two.

- A. Set CPU and memory requests from measured use
- B. Cap the maximum instance count
- C. Buy committed use discounts for the steady baseline
- D. Keep a minimum number of instances warm
- E. Raise the container limits above the observed peak

### 19. A team must send five percent of live traffic to a new revision and widen it only if the error rate holds. What should it configure?

- A. Route by revision tag or header
- B. Split traffic between revisions by percentage
- C. Gate the change behind a feature flag
- D. Shift traffic back to the previous revision

### 20. A new revision raises the error rate minutes after a full release and the previous revision is still available. What should the team do?

- A. Split traffic between revisions by percentage
- B. Shift traffic back to the previous revision
- C. Canary the release at a small percentage first
- D. Gate the change behind a feature flag

### 21. A provisioning flow calls four services in order, retries a failed step, and branches when a dependency reports a quota error. Which service fits?

- A. Schedule the invocation with Cloud Scheduler
- B. Publish the event to a Pub/Sub topic
- C. Queue the work as a Cloud Tasks task
- D. Orchestrate the steps in Workflows

### 22. Uploads accumulate in a bucket and older than ninety days is never read again, but deleting it must happen without a job. What should the team add?

- A. Make the bucket public
- B. Lock the bucket retention policy
- C. Add a lifecycle rule to the bucket
- D. Issue a signed URL with a short expiry

### 23. A security review finds a database password baked into an image and unchanged for two years. Which two fixes are required? Select two.

- A. Set the credential as an environment variable
- B. Download a service account key file
- C. Store the credential in Secret Manager
- D. Rotate the secret on a schedule
- E. Grant the basic editor role

### 24. A team must encrypt an application field so that its use is authorized by identity and visible in audit logs. What should it use?

- A. Set the credential as an environment variable
- B. Encrypt with a Cloud KMS key
- C. Make the bucket public
- D. Download a service account key file

### 25. A workload must call a Google Cloud API with an identity whose permissions the team can narrow and revoke. What should it use?

- A. Rely on Application Default Credentials
- B. Give the workload its own service account
- C. Let the workload use the default compute service account
- D. Download a service account key file

### 26. A pod on GKE must call a Google Cloud API with no key file stored anywhere and with credentials issued by the platform. Which mechanism fits?

- A. Download a service account key file
- B. Rely on Application Default Credentials
- C. Set the credential as an environment variable
- D. Bind a Kubernetes service account to a Google service account

### 27. A review of an internal service finds it can reach every pod and holds the editor role. Which two changes reduce that exposure? Select two.

- A. Grant the basic editor role
- B. Grant only the roles the workload needs
- C. Make the bucket public
- D. Apply a Kubernetes NetworkPolicy
- E. Allow unauthenticated invocations

### 28. An internal admin console runs on Cloud Run and must only be reachable by authenticated employees, without code changes. What should the team add?

- A. Allow unauthenticated invocations
- B. Apply a Kubernetes NetworkPolicy
- C. Use Identity Platform for end-user sign-in
- D. Put Identity-Aware Proxy in front of the service

### 29. A settlement ledger needs multi-row transactions that stay consistent across two regions. Which store fits?

- A. Store the objects in Cloud Storage
- B. Store the ledger in Spanner
- C. Use Firestore in Native mode
- D. Design the row key for the read pattern

### 30. A time-series service reads the last hour for one device at a time and writes hundreds of thousands of points per second. What matters most in the design?

- A. Use Firestore in Native mode
- B. Design the row key for the read pattern
- C. Store the ledger in Spanner
- D. Store the objects in Cloud Storage

### 31. A customer must download one receipt for ten minutes without the application proxying the bytes or exposing credentials. What should the service return?

- A. Issue a signed URL with a short expiry
- B. Make the bucket public
- C. Lock the bucket retention policy
- D. Add a lifecycle rule to the bucket

### 32. Product events must be queryable in the warehouse within seconds for a live dashboard. What should the application do?

- A. Store the objects in Cloud Storage
- B. Store the ledger in Spanner
- C. Export the batch to BigQuery
- D. Stream the events into BigQuery

---

## Domain 2 — Building and Testing Applications (Development Environments, Builds, and Tests)

### 33. A team wants to catch a broken Firestore query before deploying and to run the same check in CI. Which two practices are needed? Select two.

- A. Use Cloud Shell for the session
- B. Run an integration test against the emulator
- C. Run the service emulator locally
- D. Develop with Cloud Code in the IDE
- E. Push the image to Artifact Registry

### 34. A developer needs to exercise Pub/Sub publishing logic without a live topic or a bill. What should they use?

- A. Use Cloud Workstations for the environment
- B. Use Cloud Shell for the session
- C. Develop with Cloud Code in the IDE
- D. Run the service emulator locally

### 35. A regulated team must give contractors a identical, container-defined development environment behind a private endpoint. What should they use?

- A. Develop with Cloud Code in the IDE
- B. Use Cloud Workstations for the environment
- C. Deploy from source and let the platform build it
- D. Use Cloud Shell for the session

### 36. A developer wants to run and debug a Cloud Run service from inside their editor with breakpoints. What should they use?

- A. Develop with Cloud Code in the IDE
- B. Use Cloud Workstations for the environment
- C. Use Cloud Shell for the session
- D. Run the service emulator locally

### 37. A team iterating on a GKE service wants each source save to rebuild and redeploy automatically. What should they use?

- A. Build the image with Cloud Build
- B. Deploy from source and let the platform build it
- C. Deploy a pinned image digest
- D. Iterate with Skaffold

### 38. A team wants its coding assistant to query the project's own tooling through defined tools rather than pasted context. What should it connect?

- A. Use an AI coding assistant to draft the tests
- B. Connect the assistant to an MCP server
- C. Ask Gemini Cloud Assist for a diagnosis
- D. Use Cloud Shell for the session

### 39. A team must build an image on every merge and keep an immutable artifact per environment with separate access. Which two services are needed? Select two.

- A. Build the image with Cloud Build
- B. Push the image to Artifact Registry
- C. Develop with Cloud Code in the IDE
- D. Push the image to Container Registry
- E. Use Cloud Shell for the session

### 40. Builds currently start when someone remembers to run a command, so main drifts from the released image. What should the team configure?

- A. Run the tests as a Cloud Build step
- B. Schedule the invocation with Cloud Scheduler
- C. Queue the work as a Cloud Tasks task
- D. Trigger the build from a repository push

### 41. A release must run exactly the artifact that passed the tests, not a rebuild of the branch at deploy time. What should the team deploy?

- A. Deploy from source and let the platform build it
- B. Build the image with Cloud Build
- C. Push the image to Artifact Registry
- D. Deploy a pinned image digest

### 42. Tests exist but run on a developer machine, so broken code reaches the registry. Where should the tests run?

- A. Block the deploy on the test result
- B. Run an integration test against the emulator
- C. Trigger the build from a repository push
- D. Run the tests as a Cloud Build step

### 43. A team needs per-repository IAM so the staging project cannot pull production images. Which registry fits?

- A. Push the image to Container Registry
- B. Push the image to Artifact Registry
- C. Build the image with Cloud Build
- D. Store the objects in Cloud Storage

### 44. A registry must apply a vulnerability scan result as a deploy condition and keep images close to the runtime region. Which service fits?

- A. Develop with Cloud Code in the IDE
- B. Build the image with Cloud Build
- C. Push the image to Artifact Registry
- D. Push the image to Container Registry

### 45. Build logs and test reports must be retained for audit after the registry entry expires. Where should they go?

- A. Push the image to Container Registry
- B. Build the image with Cloud Build
- C. Store the objects in Cloud Storage
- D. Push the image to Artifact Registry

### 46. A bank must refuse to run any image that did not come from its own approved pipeline, and the refusal must happen at admission time. What should the team enforce?

- A. Enforce admission with Binary Authorization
- B. Scan the image with Artifact Analysis
- C. Review the finding in Security Command Center
- D. Generate build provenance in Cloud Build

### 47. A team must know which images in the registry contain a newly disclosed vulnerability. What should they use?

- A. Generate build provenance in Cloud Build
- B. Review the finding in Security Command Center
- C. Enforce admission with Binary Authorization
- D. Scan the image with Artifact Analysis

### 48. A security team wants one place to triage findings from several services rather than per-service consoles. What should they use?

- A. Build a log-based metric
- B. Scan the image with Artifact Analysis
- C. Enforce admission with Binary Authorization
- D. Review the finding in Security Command Center

### 49. A team wants fast tests around one function and wants help drafting the first version of them. Which two choices fit? Select two.

- A. Run an integration test against the emulator
- B. Quarantine the flaky test and fix it
- C. Add a unit test with dependencies stubbed
- D. Use an AI coding assistant to draft the tests
- E. Load-test the release before the rollout

### 50. A pricing function has four branches and its failures must be located precisely in seconds. What should the team add?

- A. Quarantine the flaky test and fix it
- B. Add a unit test with dependencies stubbed
- C. Load-test the release before the rollout
- D. Run an integration test against the emulator

### 51. A test fails roughly one run in ten for timing reasons, so the team has started ignoring red builds. What should they do?

- A. Add a unit test with dependencies stubbed
- B. Run the tests as a Cloud Build step
- C. Quarantine the flaky test and fix it
- D. Load-test the release before the rollout

### 52. A service must be tested against its real message broker contract on every merge. Which two choices fit? Select two.

- A. Load-test the release before the rollout
- B. Run an integration test against the emulator
- C. Run the service emulator locally
- D. Run the tests as a Cloud Build step
- E. Add a unit test with dependencies stubbed

### 53. Two services disagree about a message schema only after deployment. What kind of test would have caught it?

- A. Load-test the release before the rollout
- B. Add a unit test with dependencies stubbed
- C. Quarantine the flaky test and fix it
- D. Run an integration test against the emulator

### 54. A release is scheduled for a sale weekend and no one knows how the new revision behaves at five times normal traffic. What should the team run?

- A. Block the deploy on the test result
- B. Add a unit test with dependencies stubbed
- C. Run an integration test against the emulator
- D. Load-test the release before the rollout

### 55. A team keeps deploying while the test suite is red because nothing blocks the release. What should they add?

- A. Block the deploy on the test result
- B. Run the tests as a Cloud Build step
- C. Load-test the release before the rollout
- D. Quarantine the flaky test and fix it

---

## Domain 3 — Configuring Cloud-Native Applications for Deployment (Cloud Run and GKE Deployment Configuration)

### 56. A prototype must go live in an hour and the team has no Dockerfile yet, but the runtime supports its language. What should it do?

- A. Deploy from source and let the platform build it
- B. Build the image with Cloud Build
- C. Package the monolith into a container image
- D. Deploy a pinned image digest

### 57. A regulated release must run exactly the image digest that passed the tests last Tuesday. What should the team deploy?

- A. Package the monolith into a container image
- B. Deploy from source and let the platform build it
- C. Deploy a pinned image digest
- D. Trigger the build from a repository push

### 58. A service must only accept traffic from inside the VPC and its internal load balancer, never from the internet. What should the team configure?

- A. Allow unauthenticated invocations
- B. Restrict ingress to internal traffic
- C. Put Identity-Aware Proxy in front of the service
- D. Grant the invoker role to the calling identity

### 59. Only one other service may call an internal Cloud Run endpoint, and that service already runs with its own identity. What should the team grant?

- A. Allow unauthenticated invocations
- B. Grant the basic editor role
- C. Put Identity-Aware Proxy in front of the service
- D. Grant the invoker role to the calling identity

### 60. A service must react to a Cloud Storage object being finalized, and the delivery must reach its HTTPS endpoint. Which two components are needed? Select two.

- A. Queue the work as a Cloud Tasks task
- B. Orchestrate the steps in Workflows
- C. Route the event with Eventarc
- D. Deliver to an HTTPS push subscription
- E. Schedule the invocation with Cloud Scheduler

### 61. A batch worker must drain a backlog at its own pace and acknowledge each message when its work commits. What should it use?

- A. Deliver to an HTTPS push subscription
- B. Queue the work as a Cloud Tasks task
- C. Route the event with Eventarc
- D. Have the worker pull from the subscription

### 62. Outbound calls to a slow partner must be retried with backoff and a bounded rate, one task per order. What should the team use?

- A. Schedule the invocation with Cloud Scheduler
- B. Orchestrate the steps in Workflows
- C. Queue the work as a Cloud Tasks task
- D. Publish the event to a Pub/Sub topic

### 63. A nightly job must invoke an endpoint at 02:00 every day with no queueing or retry semantics beyond the call. What should the team use?

- A. Schedule the invocation with Cloud Scheduler
- B. Orchestrate the steps in Workflows
- C. Route the event with Eventarc
- D. Queue the work as a Cloud Tasks task

### 64. A Cloud Run service serves long downloads and must not exhaust memory per instance, while the bill must stay bounded. Which two settings matter? Select two.

- A. Keep a minimum number of instances warm
- B. Raise the per-instance concurrency limit
- C. Use request-based billing
- D. Enable CPU boost at startup
- E. Cap the maximum instance count

### 65. The first request after an idle period takes eight seconds, and the product team refuses any cold start on the checkout path. What should the team configure?

- A. Enable CPU boost at startup
- B. Keep a minimum number of instances warm
- C. Raise the per-instance concurrency limit
- D. Cap the maximum instance count

### 66. A revision receives traffic before its cache warm-up finishes, so early requests fail. What should the team configure?

- A. Configure a readiness probe
- B. Configure a startup probe
- C. Configure a liveness probe
- D. Scale pods on CPU utilization

### 67. A reviewer asks which single setting prevents a Cloud Run service from accepting internet traffic at all. Which setting answers that?

- A. Restrict ingress to internal traffic
- B. Allow unauthenticated invocations
- C. Put Identity-Aware Proxy in front of the service
- D. Grant the invoker role to the calling identity

### 68. A mobile client cannot be updated for six months, and the API contract must change in a way the old client cannot parse. What should the team do?

- A. Publish an OpenAPI specification
- B. Introduce a new API version alongside the old one
- C. Apply a rate limit per client key
- D. Add the field in a backward-compatible way

### 69. A new optional field has to reach clients that ignore unknown fields, with no client change. What should the team do?

- A. Add the field in a backward-compatible way
- B. Set a quota per API key
- C. Introduce a new API version alongside the old one
- D. Publish an OpenAPI specification

### 70. A GKE deployment must stay available while new pods replace old ones on every release. Which two settings control that? Select two.

- A. Use a rolling update strategy
- B. Tune maxSurge and maxUnavailable
- C. Add a PodDisruptionBudget
- D. Run the batch node pool on Spot VMs
- E. Enable node pool autoscaling

### 71. A workload needs a sidecar proxy per pod and a custom scheduler constraint that no managed runtime exposes. Where should it run?

- A. Deploy the workload to Google Kubernetes Engine
- B. Deploy to App Engine standard
- C. Run the application on Compute Engine instances
- D. Deploy the service to Cloud Run

### 72. Batch pods land on the general-purpose node pool and are evicted whenever a deployment scales down. What should the team change?

- A. Constrain pods to the intended node pool
- B. Run the batch node pool on Spot VMs
- C. Enable node pool autoscaling
- D. Scale pods on CPU utilization

### 73. A cluster upgrade evicted every replica of a service at once, and the outage lasted four minutes. What should the team add?

- A. Set a namespace resource quota
- B. Set a minimum replica count
- C. Add a PodDisruptionBudget
- D. Use a rolling update strategy

### 74. A pod keeps its endpoint while its database connection pool is exhausted, so requests fail instead of being routed elsewhere. What should the team configure?

- A. Configure a liveness probe
- B. Scale pods on CPU utilization
- C. Configure a startup probe
- D. Configure a readiness probe

### 75. A pod deadlocks and never recovers, but it still answers its readiness check. What should the team add?

- A. Configure a readiness probe
- B. Add a PodDisruptionBudget
- C. Configure a liveness probe
- D. Configure a startup probe

### 76. A slow-starting container is killed by the liveness probe before it finishes loading its model. What should the team add?

- A. Configure a readiness probe
- B. Configure a liveness probe
- C. Configure a startup probe
- D. Scale pods on a custom or external metric

### 77. A queue-driven worker must scale on backlog depth rather than CPU, and must not drop to zero replicas. Which two settings fit? Select two.

- A. Scale pods on CPU utilization
- B. Set a minimum replica count
- C. Set a namespace resource quota
- D. Scale pods on a custom or external metric
- E. Add a PodDisruptionBudget

### 78. A stateless web tier's only bottleneck is request processing, and demand tracks CPU closely. What should the team enable?

- A. Enable node pool autoscaling
- B. Set a minimum replica count
- C. Scale pods on a custom or external metric
- D. Scale pods on CPU utilization

### 79. One team's runaway job consumed the whole cluster and blocked every other namespace. What should be added?

- A. Add a PodDisruptionBudget
- B. Scale pods on CPU utilization
- C. Set a namespace resource quota
- D. Constrain pods to the intended node pool

---

## Domain 4 — Integrating Applications with Google Cloud Services (Data, Messaging, APIs, and Observability)

### 80. An application on Cloud Run must reach Cloud SQL with IAM authorization and must not open a new connection per request. Which two choices are needed? Select two.

- A. Use the language connector with IAM
- B. Pool and reuse database connections
- C. Connect over the database private IP
- D. Connect through the Cloud SQL Auth Proxy
- E. Download a service account key file

### 81. An instance refuses new connections at peak although the machine is idle, because every request opens and closes a session. What should the team change?

- A. Use the language connector with IAM
- B. Connect over the database private IP
- C. Pool and reuse database connections
- D. Connect through the Cloud SQL Auth Proxy

### 82. A Java service must resolve the database instance and authorize itself with no sidecar process in the container. What should it use?

- A. Connect through the Cloud SQL Auth Proxy
- B. Use the language connector with IAM
- C. Download a service account key file
- D. Connect over the database private IP

### 83. A database and its service already share a VPC, and the team wants no extra process between them. What should it use?

- A. Use the language connector with IAM
- B. Connect through the Cloud SQL Auth Proxy
- C. Connect over the database private IP
- D. Expose the database on a public address with enforced SSL

### 84. A mobile client must receive document updates in real time and work offline when the connection drops. Which store fits?

- A. Store the ledger in Spanner
- B. Design the row key for the read pattern
- C. Use Firestore in Native mode
- D. Connect through the Cloud SQL Auth Proxy

### 85. An order handler is delivered the same event twice after a consumer restart and ships the order twice. What should the handler add?

- A. Make the handler idempotent with a deduplication key
- B. Queue the work as a Cloud Tasks task
- C. Publish the event to a Pub/Sub topic
- D. Add a dead-letter topic

### 86. A poison message is retried forever and the subscription backlog stops advancing. What should be configured?

- A. Have the worker pull from the subscription
- B. Make the handler idempotent with a deduplication key
- C. Add a dead-letter topic
- D. Deliver to an HTTPS push subscription

### 87. Three independent services must all receive an order event without knowing about each other. What should the publisher use?

- A. Publish the event to a Pub/Sub topic
- B. Orchestrate the steps in Workflows
- C. Queue the work as a Cloud Tasks task
- D. Schedule the invocation with Cloud Scheduler

### 88. A single known endpoint must process each order exactly once in its own time, with retries controlled per task. What should the team use?

- A. Orchestrate the steps in Workflows
- B. Publish the event to a Pub/Sub topic
- C. Queue the work as a Cloud Tasks task
- D. Route the event with Eventarc

### 89. A nightly export reads a large Google Cloud API collection that rejects bursts and returns fewer records than expected. Which two practices are needed? Select two.

- A. Cache the response for its freshness window
- B. Follow the page token until results are exhausted
- C. Retry with exponential backoff and jitter
- D. Batch many small calls into one request
- E. Build a log-based metric

### 90. A list call returns two hundred fields per record and the dashboard needs four, so payloads dominate latency. What should the team change?

- A. Request only the fields the caller needs
- B. Follow the page token until results are exhausted
- C. Batch many small calls into one request
- D. Cache the response for its freshness window

### 91. A service re-reads the same slowly changing reference data on every request from every instance. What should the team add?

- A. Follow the page token until results are exhausted
- B. Batch many small calls into one request
- C. Retry with exponential backoff and jitter
- D. Cache the response for its freshness window

### 92. An API returns rate-limit errors at peak, and naive retries make it worse. What should the client do?

- A. Give the workload its own service account
- B. Retry with exponential backoff and jitter
- C. Cache the response for its freshness window
- D. Request only the fields the caller needs

### 93. A backend must call a Google Cloud API under an identity whose permissions can be reviewed and narrowed. What should it use?

- A. Let the workload use the default compute service account
- B. Rely on Application Default Credentials
- C. Give the workload its own service account
- D. Download a service account key file

### 94. A review finds the calling service account holds the editor role for a single read call. What should the team change?

- A. Allow unauthenticated invocations
- B. Grant only the roles the workload needs
- C. Grant the basic editor role
- D. Download a service account key file

### 95. Operators cannot filter request logs by tenant because the value is buried inside a free-text message. What should change?

- A. Emit structured JSON logs
- B. Build a log-based metric
- C. Send the exception to Error Reporting
- D. Set the correct severity on each entry

### 96. A request spends four seconds in a downstream call, but the total latency alone does not show where. What should the team add?

- A. Emit a custom metric from the code
- B. Instrument a span around the downstream call
- C. Send the exception to Error Reporting
- D. Propagate the trace ID between services

### 97. A business signal such as checkout conversion exists only in application code and must be charted. What should the team emit?

- A. Build a log-based metric
- B. Create an alerting policy on the metric
- C. Emit structured JSON logs
- D. Emit a custom metric from the code

### 98. The same exception appears thousands of times with slightly different stack traces and nobody can count the distinct failures. What should the team use?

- A. Emit a custom metric from the code
- B. Emit structured JSON logs
- C. Build a log-based metric
- D. Send the exception to Error Reporting

### 99. Logs from three services for one request cannot be joined because each entry is independent. What should the team add?

- A. Propagate the trace ID between services
- B. Send the exception to Error Reporting
- C. Emit a custom metric from the code
- D. Instrument a span around the downstream call

### 100. An on-call engineer has metrics, logs and traces for a failing service and wants a ranked hypothesis. Which tool fits?

- A. Ask Gemini Cloud Assist for a diagnosis
- B. Connect the assistant to an MCP server
- C. Profile the service with Cloud Profiler
- D. Use an AI coding assistant to draft the tests

---

## Answer key and explanations

### Question 1 — C

Answer: Deploy the service to Cloud Run. Cloud Run serves the burst and scales back down without nodes to patch, where a cluster or virtual machines move operations back to the team. A managed container runtime that scales to zero and bills per request while it serves traffic. Local study-map skill 1.1 (Compute Platform Selection), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 1 (designing highly scalable, secure, and reliable cloud-native applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A platform runtime that manages scaling for a supported language version and its sandbox limits. Why the correct answer wins: Cloud Run serves the burst and scales back down without nodes to patch, where a cluster or virtual machines move operations back to the team.
- **B:** Incorrect for this question. Virtual machines where the operating system, runtime and scaling group are all managed by the team. Why the correct answer wins: Cloud Run serves the burst and scales back down without nodes to patch, where a cluster or virtual machines move operations back to the team.
- **C:** Correct. A managed container runtime that scales to zero and bills per request while it serves traffic. In this case: Cloud Run serves the burst and scales back down without nodes to patch, where a cluster or virtual machines move operations back to the team.
- **D:** Incorrect for this question. A managed Kubernetes control plane where pods, node pools and cluster-scoped policy are yours to configure. Why the correct answer wins: Cloud Run serves the burst and scales back down without nodes to patch, where a cluster or virtual machines move operations back to the team.

### Question 2 — A, E

Answers: Deploy the workload to Google Kubernetes Engine; Enable node pool autoscaling. The requirements are cluster-shaped, so a managed Kubernetes control plane is the fit, and node pool autoscaling supplies capacity as pods are scheduled. A managed Kubernetes control plane where pods, node pools and cluster-scoped policy are yours to configure. Add or remove nodes as pending pods demand capacity. Local study-map skill 1.1 (Compute Platform Selection), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 1 (designing highly scalable, secure, and reliable cloud-native applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Correct. Add or remove nodes as pending pods demand capacity. In this case: The requirements are cluster-shaped, so a managed Kubernetes control plane is the fit, and node pool autoscaling supplies capacity as pods are scheduled.
- **B:** Incorrect for this question. A managed container runtime that scales to zero and bills per request while it serves traffic. Why the correct answer wins: The requirements are cluster-shaped, so a managed Kubernetes control plane is the fit, and node pool autoscaling supplies capacity as pods are scheduled.
- **C:** Incorrect for this question. An event-triggered function runtime for a single-purpose handler rather than a long-lived service. Why the correct answer wins: The requirements are cluster-shaped, so a managed Kubernetes control plane is the fit, and node pool autoscaling supplies capacity as pods are scheduled.
- **D:** Incorrect for this question. A platform runtime that manages scaling for a supported language version and its sandbox limits. Why the correct answer wins: The requirements are cluster-shaped, so a managed Kubernetes control plane is the fit, and node pool autoscaling supplies capacity as pods are scheduled.
- **E:** Correct. A managed Kubernetes control plane where pods, node pools and cluster-scoped policy are yours to configure. In this case: The requirements are cluster-shaped, so a managed Kubernetes control plane is the fit, and node pool autoscaling supplies capacity as pods are scheduled.

### Question 3 — A

Answer: Run the application on Compute Engine instances. Virtual machines are the only option that permits that level of host control, while the managed runtimes do not expose the kernel or the image family. Virtual machines where the operating system, runtime and scaling group are all managed by the team. Local study-map skill 1.1 (Compute Platform Selection), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 1 (designing highly scalable, secure, and reliable cloud-native applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Correct. Virtual machines where the operating system, runtime and scaling group are all managed by the team. In this case: Virtual machines are the only option that permits that level of host control, while the managed runtimes do not expose the kernel or the image family.
- **B:** Incorrect for this question. A managed Kubernetes control plane where pods, node pools and cluster-scoped policy are yours to configure. Why the correct answer wins: Virtual machines are the only option that permits that level of host control, while the managed runtimes do not expose the kernel or the image family.
- **C:** Incorrect for this question. A managed container runtime that scales to zero and bills per request while it serves traffic. Why the correct answer wins: Virtual machines are the only option that permits that level of host control, while the managed runtimes do not expose the kernel or the image family.
- **D:** Incorrect for this question. An event-triggered function runtime for a single-purpose handler rather than a long-lived service. Why the correct answer wins: Virtual machines are the only option that permits that level of host control, while the managed runtimes do not expose the kernel or the image family.

### Question 4 — B

Answer: Package the monolith into a container image. Packaging the process into a container preserves its runtime while giving it a portable artifact that managed platforms can run. Wrap the existing process in a portable artifact that a managed runtime can execute. Local study-map skill 1.2 (Containerizing and Refactoring Applications), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 1 (designing highly scalable, secure, and reliable cloud-native applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. An event-triggered function runtime for a single-purpose handler rather than a long-lived service. Why the correct answer wins: Packaging the process into a container preserves its runtime while giving it a portable artifact that managed platforms can run.
- **B:** Correct. Wrap the existing process in a portable artifact that a managed runtime can execute. In this case: Packaging the process into a container preserves its runtime while giving it a portable artifact that managed platforms can run.
- **C:** Incorrect for this question. A platform runtime that manages scaling for a supported language version and its sandbox limits. Why the correct answer wins: Packaging the process into a container preserves its runtime while giving it a portable artifact that managed platforms can run.
- **D:** Incorrect for this question. A cron-style trigger that calls a target on a fixed timetable. Why the correct answer wins: Packaging the process into a container preserves its runtime while giving it a portable artifact that managed platforms can run.

### Question 5 — A

Answer: Deploy in one region across multiple zones. Spreading instances across the zones of one region survives a zone failure without paying for a second region. Spread instances over zones of a single region so a zone failure does not stop the service. Local study-map skill 1.3 (Regional Distribution and Failover), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 1 (designing highly scalable, secure, and reliable cloud-native applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Correct. Spread instances over zones of a single region so a zone failure does not stop the service. In this case: Spreading instances across the zones of one region survives a zone failure without paying for a second region.
- **B:** Incorrect for this question. Serve from two regions so a regional failure leaves capacity elsewhere. Why the correct answer wins: Spreading instances across the zones of one region survives a zone failure without paying for a second region.
- **C:** Incorrect for this question. Trade a term commitment for a lower unit price on capacity that never idles. Why the correct answer wins: Spreading instances across the zones of one region survives a zone failure without paying for a second region.
- **D:** Incorrect for this question. Run in one zone only, so a zone failure stops the service entirely. Why the correct answer wins: Spreading instances across the zones of one region survives a zone failure without paying for a second region.

### Question 6 — C

Answer: Deploy the service in two regions behind a global load balancer. Serving from two regions behind one global address keeps capacity available after a regional loss, which a single-region design cannot. Serve from two regions so a regional failure leaves capacity elsewhere. Local study-map skill 1.3 (Regional Distribution and Failover), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 1 (designing highly scalable, secure, and reliable cloud-native applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Pin a client to one backend for the life of its session. Why the correct answer wins: Serving from two regions behind one global address keeps capacity available after a regional loss, which a single-region design cannot.
- **B:** Incorrect for this question. Spread instances over zones of a single region so a zone failure does not stop the service. Why the correct answer wins: Serving from two regions behind one global address keeps capacity available after a regional loss, which a single-region design cannot.
- **C:** Correct. Serve from two regions so a regional failure leaves capacity elsewhere. In this case: Serving from two regions behind one global address keeps capacity available after a regional loss, which a single-region design cannot.
- **D:** Incorrect for this question. Trade a term commitment for a lower unit price on capacity that never idles. Why the correct answer wins: Serving from two regions behind one global address keeps capacity available after a regional loss, which a single-region design cannot.

### Question 7 — D

Answer: Enable session affinity on the backend service. Session affinity holds a client to one backend for the life of its session, which is exactly the behaviour the service depends on today. Pin a client to one backend for the life of its session. Local study-map skill 1.4 (Load Balancing and Session Affinity), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 1 (designing highly scalable, secure, and reliable cloud-native applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Route the client by cookie rather than by address or header. Why the correct answer wins: Session affinity holds a client to one backend for the life of its session, which is exactly the behaviour the service depends on today.
- **B:** Incorrect for this question. Move the state out of the instance so any instance can serve any request. Why the correct answer wins: Session affinity holds a client to one backend for the life of its session, which is exactly the behaviour the service depends on today.
- **C:** Incorrect for this question. Read the cache, fall back to the database, and populate the cache on a miss. Why the correct answer wins: Session affinity holds a client to one backend for the life of its session, which is exactly the behaviour the service depends on today.
- **D:** Correct. Pin a client to one backend for the life of its session. In this case: Session affinity holds a client to one backend for the life of its session, which is exactly the behaviour the service depends on today.

### Question 8 — C, E

Answers: Store session state in a shared datastore; Put a global external Application Load Balancer in front. Moving session state to a shared store removes the need for stickiness, and the global load balancer keeps one address to route. Move the state out of the instance so any instance can serve any request. A single anycast address that routes to the nearest healthy backend. Local study-map skill 1.4 (Load Balancing and Session Affinity), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 1 (designing highly scalable, secure, and reliable cloud-native applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Route the client by cookie rather than by address or header. Why the correct answer wins: Moving session state to a shared store removes the need for stickiness, and the global load balancer keeps one address to route.
- **B:** Incorrect for this question. Cache responses at the edge so repeated requests never reach the origin. Why the correct answer wins: Moving session state to a shared store removes the need for stickiness, and the global load balancer keeps one address to route.
- **C:** Correct. Move the state out of the instance so any instance can serve any request. In this case: Moving session state to a shared store removes the need for stickiness, and the global load balancer keeps one address to route.
- **D:** Incorrect for this question. Pin a client to one backend for the life of its session. Why the correct answer wins: Moving session state to a shared store removes the need for stickiness, and the global load balancer keeps one address to route.
- **E:** Correct. A single anycast address that routes to the nearest healthy backend. In this case: Moving session state to a shared store removes the need for stickiness, and the global load balancer keeps one address to route.

### Question 9 — C

Answer: Cache reads in Memorystore. A shared managed cache gives every instance the same values, where a per-process cache diverges between instances. A managed Redis-compatible cache in front of the system of record. Local study-map skill 1.5 (Caching with Memorystore), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 1 (designing highly scalable, secure, and reliable cloud-native applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A per-instance cache that is fast but not shared between instances. Why the correct answer wins: A shared managed cache gives every instance the same values, where a per-process cache diverges between instances.
- **B:** Incorrect for this question. Cache responses at the edge so repeated requests never reach the origin. Why the correct answer wins: A shared managed cache gives every instance the same values, where a per-process cache diverges between instances.
- **C:** Correct. A managed Redis-compatible cache in front of the system of record. In this case: A shared managed cache gives every instance the same values, where a per-process cache diverges between instances.
- **D:** Incorrect for this question. Read the cache, fall back to the database, and populate the cache on a miss. Why the correct answer wins: A shared managed cache gives every instance the same values, where a per-process cache diverges between instances.

### Question 10 — B

Answer: Serve static content from Cloud CDN. Serving static assets from the edge stops the repeated origin fetch and cuts the latency the distance was causing. Cache responses at the edge so repeated requests never reach the origin. Local study-map skill 1.5 (Caching with Memorystore), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 1 (designing highly scalable, secure, and reliable cloud-native applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A per-instance cache that is fast but not shared between instances. Why the correct answer wins: Serving static assets from the edge stops the repeated origin fetch and cuts the latency the distance was causing.
- **B:** Correct. Cache responses at the edge so repeated requests never reach the origin. In this case: Serving static assets from the edge stops the repeated origin fetch and cuts the latency the distance was causing.
- **C:** Incorrect for this question. A managed Redis-compatible cache in front of the system of record. Why the correct answer wins: Serving static assets from the edge stops the repeated origin fetch and cuts the latency the distance was causing.
- **D:** Incorrect for this question. Read the cache, fall back to the database, and populate the cache on a miss. Why the correct answer wins: Serving static assets from the edge stops the repeated origin fetch and cuts the latency the distance was causing.

### Question 11 — A

Answer: Expose a gRPC service. A schema-driven binary RPC interface suits high-frequency streaming traffic and gives generated clients in each language. A binary, schema-driven RPC interface with streaming and generated clients. Local study-map skill 1.6 (API Protocol Choice: REST and gRPC), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 1 (designing highly scalable, secure, and reliable cloud-native applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Correct. A binary, schema-driven RPC interface with streaming and generated clients. In this case: A schema-driven binary RPC interface suits high-frequency streaming traffic and gives generated clients in each language.
- **B:** Incorrect for this question. A resource-oriented HTTP interface that browsers and simple clients can call. Why the correct answer wins: A schema-driven binary RPC interface suits high-frequency streaming traffic and gives generated clients in each language.
- **C:** Incorrect for this question. A compatibility layer so browser code can call a gRPC service. Why the correct answer wins: A schema-driven binary RPC interface suits high-frequency streaming traffic and gives generated clients in each language.
- **D:** Incorrect for this question. A machine-readable contract that generates clients and validates requests. Why the correct answer wins: A schema-driven binary RPC interface suits high-frequency streaming traffic and gives generated clients in each language.

### Question 12 — A

Answer: Publish an OpenAPI specification. A published specification gives the partner a contract that generates clients and validates requests, which a binary RPC interface does not provide. A machine-readable contract that generates clients and validates requests. Local study-map skill 1.6 (API Protocol Choice: REST and gRPC), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 1 (designing highly scalable, secure, and reliable cloud-native applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Correct. A machine-readable contract that generates clients and validates requests. In this case: A published specification gives the partner a contract that generates clients and validates requests, which a binary RPC interface does not provide.
- **B:** Incorrect for this question. A binary, schema-driven RPC interface with streaming and generated clients. Why the correct answer wins: A published specification gives the partner a contract that generates clients and validates requests, which a binary RPC interface does not provide.
- **C:** Incorrect for this question. A compatibility layer so browser code can call a gRPC service. Why the correct answer wins: A published specification gives the partner a contract that generates clients and validates requests, which a binary RPC interface does not provide.
- **D:** Incorrect for this question. A per-instance cache that is fast but not shared between instances. Why the correct answer wins: A published specification gives the partner a contract that generates clients and validates requests, which a binary RPC interface does not provide.

### Question 13 — C

Answer: Apply a rate limit per client key. A per-client rate limit stops one caller from consuming the shared capacity. Reject or queue requests above a threshold so one client cannot exhaust the service. Local study-map skill 1.7 (API Management, Rate Limiting, and Versioning), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 1 (designing highly scalable, secure, and reliable cloud-native applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Bound how many calls a plan allows in a window. Why the correct answer wins: A per-client rate limit stops one caller from consuming the shared capacity.
- **B:** Incorrect for this question. Keep the old contract working while the new one is adopted. Why the correct answer wins: A per-client rate limit stops one caller from consuming the shared capacity.
- **C:** Correct. Reject or queue requests above a threshold so one client cannot exhaust the service. In this case: A per-client rate limit stops one caller from consuming the shared capacity.
- **D:** Incorrect for this question. Extend the contract so existing clients keep working unchanged. Why the correct answer wins: A per-client rate limit stops one caller from consuming the shared capacity.

### Question 14 — B, C

Answers: Put Apigee in front of the API; Set a quota per API key. An API management layer provides mediation and reporting, and per-key quotas enforce the plan each customer bought. An API management layer for quotas, keys, mediation and analytics. Bound how many calls a plan allows in a window. Local study-map skill 1.7 (API Management, Rate Limiting, and Versioning), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 1 (designing highly scalable, secure, and reliable cloud-native applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A lighter managed gateway for routing and key-based quota enforcement. Why the correct answer wins: An API management layer provides mediation and reporting, and per-key quotas enforce the plan each customer bought.
- **B:** Correct. An API management layer for quotas, keys, mediation and analytics. In this case: An API management layer provides mediation and reporting, and per-key quotas enforce the plan each customer bought.
- **C:** Correct. Bound how many calls a plan allows in a window. In this case: An API management layer provides mediation and reporting, and per-key quotas enforce the plan each customer bought.
- **D:** Incorrect for this question. Keep the old contract working while the new one is adopted. Why the correct answer wins: An API management layer provides mediation and reporting, and per-key quotas enforce the plan each customer bought.
- **E:** Incorrect for this question. Reject or queue requests above a threshold so one client cannot exhaust the service. Why the correct answer wins: An API management layer provides mediation and reporting, and per-key quotas enforce the plan each customer bought.

### Question 15 — B

Answer: Make the handler idempotent with a deduplication key. A deduplication key lets the handler recognise a repeat delivery and skip the second charge. Recognise a repeated delivery and skip the duplicate work. Local study-map skill 1.8 (Asynchronous and Event-Driven Integration), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 1 (designing highly scalable, secure, and reliable cloud-native applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A task queue with retries and rate control aimed at a specific target. Why the correct answer wins: A deduplication key lets the handler recognise a repeat delivery and skip the second charge.
- **B:** Correct. Recognise a repeated delivery and skip the duplicate work. In this case: A deduplication key lets the handler recognise a repeat delivery and skip the second charge.
- **C:** Incorrect for this question. Hold messages that exhausted their delivery attempts for later inspection. Why the correct answer wins: A deduplication key lets the handler recognise a repeat delivery and skip the second charge.
- **D:** Incorrect for this question. A durable, at-least-once message channel with independent subscribers. Why the correct answer wins: A deduplication key lets the handler recognise a repeat delivery and skip the second charge.

### Question 16 — A

Answer: Add a dead-letter topic. A dead-letter topic parks messages that exhausted their attempts so the rest of the backlog can move. Hold messages that exhausted their delivery attempts for later inspection. Local study-map skill 1.8 (Asynchronous and Event-Driven Integration), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 1 (designing highly scalable, secure, and reliable cloud-native applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Correct. Hold messages that exhausted their delivery attempts for later inspection. In this case: A dead-letter topic parks messages that exhausted their attempts so the rest of the backlog can move.
- **B:** Incorrect for this question. The consumer controls the pace and acknowledges messages itself. Why the correct answer wins: A dead-letter topic parks messages that exhausted their attempts so the rest of the backlog can move.
- **C:** Incorrect for this question. Push each message to an endpoint instead of having the consumer pull. Why the correct answer wins: A dead-letter topic parks messages that exhausted their attempts so the rest of the backlog can move.
- **D:** Incorrect for this question. Recognise a repeated delivery and skip the duplicate work. Why the correct answer wins: A dead-letter topic parks messages that exhausted their attempts so the rest of the backlog can move.

### Question 17 — C

Answer: Set CPU and memory requests from measured use. Requests drive scheduling, so setting them from measured use frees capacity the pods were reserving without using. Give the scheduler real numbers so placement and scaling decisions are not guesses. Local study-map skill 1.9 (Resource Requirements and Cost Optimization), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 1 (designing highly scalable, secure, and reliable cloud-native applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Trade a term commitment for a lower unit price on capacity that never idles. Why the correct answer wins: Requests drive scheduling, so setting them from measured use frees capacity the pods were reserving without using.
- **B:** Incorrect for this question. Bound the blast radius and the bill at the cost of queueing when the cap is reached. Why the correct answer wins: Requests drive scheduling, so setting them from measured use frees capacity the pods were reserving without using.
- **C:** Correct. Give the scheduler real numbers so placement and scaling decisions are not guesses. In this case: Requests drive scheduling, so setting them from measured use frees capacity the pods were reserving without using.
- **D:** Incorrect for this question. Allow the process the headroom it needs so it is not throttled or killed. Why the correct answer wins: Requests drive scheduling, so setting them from measured use frees capacity the pods were reserving without using.

### Question 18 — A, B

Answers: Cap the maximum instance count; Set CPU and memory requests from measured use. A maximum instance cap bounds the blast radius and the bill, and honest requests stop the pods from reserving capacity they never touch. Bound the blast radius and the bill at the cost of queueing when the cap is reached. Give the scheduler real numbers so placement and scaling decisions are not guesses. Local study-map skill 1.9 (Resource Requirements and Cost Optimization), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 1 (designing highly scalable, secure, and reliable cloud-native applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Correct. Give the scheduler real numbers so placement and scaling decisions are not guesses. In this case: A maximum instance cap bounds the blast radius and the bill, and honest requests stop the pods from reserving capacity they never touch.
- **B:** Correct. Bound the blast radius and the bill at the cost of queueing when the cap is reached. In this case: A maximum instance cap bounds the blast radius and the bill, and honest requests stop the pods from reserving capacity they never touch.
- **C:** Incorrect for this question. Trade a term commitment for a lower unit price on capacity that never idles. Why the correct answer wins: A maximum instance cap bounds the blast radius and the bill, and honest requests stop the pods from reserving capacity they never touch.
- **D:** Incorrect for this question. Pay for idle capacity so a cold start never appears in the latency percentiles. Why the correct answer wins: A maximum instance cap bounds the blast radius and the bill, and honest requests stop the pods from reserving capacity they never touch.
- **E:** Incorrect for this question. Allow the process the headroom it needs so it is not throttled or killed. Why the correct answer wins: A maximum instance cap bounds the blast radius and the bill, and honest requests stop the pods from reserving capacity they never touch.

### Question 19 — B

Answer: Split traffic between revisions by percentage. Percentage-based splitting exposes the new revision to a measured slice of real traffic. Send a fraction of requests to the new revision while the old one still serves the rest. Local study-map skill 1.10 (Traffic Splitting and Gradual Rollout), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 1 (designing highly scalable, secure, and reliable cloud-native applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Send only tagged requests to the new revision for internal testing. Why the correct answer wins: Percentage-based splitting exposes the new revision to a measured slice of real traffic.
- **B:** Correct. Send a fraction of requests to the new revision while the old one still serves the rest. In this case: Percentage-based splitting exposes the new revision to a measured slice of real traffic.
- **C:** Incorrect for this question. Ship the code dark and enable it per cohort without a redeploy. Why the correct answer wins: Percentage-based splitting exposes the new revision to a measured slice of real traffic.
- **D:** Incorrect for this question. Return all traffic to the known-good revision when the new one misbehaves. Why the correct answer wins: Percentage-based splitting exposes the new revision to a measured slice of real traffic.

### Question 20 — B

Answer: Shift traffic back to the previous revision. Shifting traffic back to the known-good revision restores service immediately without a rebuild. Return all traffic to the known-good revision when the new one misbehaves. Local study-map skill 1.10 (Traffic Splitting and Gradual Rollout), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 1 (designing highly scalable, secure, and reliable cloud-native applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Send a fraction of requests to the new revision while the old one still serves the rest. Why the correct answer wins: Shifting traffic back to the known-good revision restores service immediately without a rebuild.
- **B:** Correct. Return all traffic to the known-good revision when the new one misbehaves. In this case: Shifting traffic back to the known-good revision restores service immediately without a rebuild.
- **C:** Incorrect for this question. Expose the new version to a slice of traffic before widening it. Why the correct answer wins: Shifting traffic back to the known-good revision restores service immediately without a rebuild.
- **D:** Incorrect for this question. Ship the code dark and enable it per cohort without a redeploy. Why the correct answer wins: Shifting traffic back to the known-good revision restores service immediately without a rebuild.

### Question 21 — D

Answer: Orchestrate the steps in Workflows. A stateful orchestration keeps the sequence, the retries and the error branches in one definition. A stateful sequence of service calls with retries and error branches. Local study-map skill 1.11 (Orchestrating Services), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 1 (designing highly scalable, secure, and reliable cloud-native applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A cron-style trigger that calls a target on a fixed timetable. Why the correct answer wins: A stateful orchestration keeps the sequence, the retries and the error branches in one definition.
- **B:** Incorrect for this question. A durable, at-least-once message channel with independent subscribers. Why the correct answer wins: A stateful orchestration keeps the sequence, the retries and the error branches in one definition.
- **C:** Incorrect for this question. A task queue with retries and rate control aimed at a specific target. Why the correct answer wins: A stateful orchestration keeps the sequence, the retries and the error branches in one definition.
- **D:** Correct. A stateful sequence of service calls with retries and error branches. In this case: A stateful orchestration keeps the sequence, the retries and the error branches in one definition.

### Question 22 — C

Answer: Add a lifecycle rule to the bucket. A lifecycle rule transitions or deletes objects by age without any scheduled code. Transition or delete objects by age so retention happens without a job. Local study-map skill 1.12 (Data Retention and Organization Policy), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 1 (designing highly scalable, secure, and reliable cloud-native applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Serve every object to anyone, which removes the need to authorize at all. Why the correct answer wins: A lifecycle rule transitions or deletes objects by age without any scheduled code.
- **B:** Incorrect for this question. Make the retention period impossible to shorten, even by an owner. Why the correct answer wins: A lifecycle rule transitions or deletes objects by age without any scheduled code.
- **C:** Correct. Transition or delete objects by age so retention happens without a job. In this case: A lifecycle rule transitions or deletes objects by age without any scheduled code.
- **D:** Incorrect for this question. A time-limited grant to one object without exposing credentials. Why the correct answer wins: A lifecycle rule transitions or deletes objects by age without any scheduled code.

### Question 23 — C, D

Answers: Store the credential in Secret Manager; Rotate the secret on a schedule. A managed secret store keeps the value out of the image, and scheduled rotation bounds how long a leaked value stays valid. A managed secret store with versioning and access audit. Issue a new version and retire the old one so exposure has a bounded life. Local study-map skill 1.13 (Secrets, Keys, and Credential Rotation), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 1 (designing highly scalable, secure, and reliable cloud-native applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Inject the value into the process environment at start-up. Why the correct answer wins: A managed secret store keeps the value out of the image, and scheduled rotation bounds how long a leaked value stays valid.
- **B:** Incorrect for this question. A long-lived credential that has to be stored and rotated by hand. Why the correct answer wins: A managed secret store keeps the value out of the image, and scheduled rotation bounds how long a leaked value stays valid.
- **C:** Correct. A managed secret store with versioning and access audit. In this case: A managed secret store keeps the value out of the image, and scheduled rotation bounds how long a leaked value stays valid.
- **D:** Correct. Issue a new version and retire the old one so exposure has a bounded life. In this case: A managed secret store keeps the value out of the image, and scheduled rotation bounds how long a leaked value stays valid.
- **E:** Incorrect for this question. A legacy broad role that can change most resources in the project. Why the correct answer wins: A managed secret store keeps the value out of the image, and scheduled rotation bounds how long a leaked value stays valid.

### Question 24 — B

Answer: Encrypt with a Cloud KMS key. A managed KMS key authorizes each use through IAM and records it, which a stored credential cannot do. A managed key whose use is authorized by IAM and recorded in audit logs. Local study-map skill 1.13 (Secrets, Keys, and Credential Rotation), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 1 (designing highly scalable, secure, and reliable cloud-native applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Inject the value into the process environment at start-up. Why the correct answer wins: A managed KMS key authorizes each use through IAM and records it, which a stored credential cannot do.
- **B:** Correct. A managed key whose use is authorized by IAM and recorded in audit logs. In this case: A managed KMS key authorizes each use through IAM and records it, which a stored credential cannot do.
- **C:** Incorrect for this question. Serve every object to anyone, which removes the need to authorize at all. Why the correct answer wins: A managed KMS key authorizes each use through IAM and records it, which a stored credential cannot do.
- **D:** Incorrect for this question. A long-lived credential that has to be stored and rotated by hand. Why the correct answer wins: A managed KMS key authorizes each use through IAM and records it, which a stored credential cannot do.

### Question 25 — B

Answer: Give the workload its own service account. A dedicated service account gives the workload its own identity, which the shared default account does not. A dedicated identity whose roles can be granted and revoked independently. Local study-map skill 1.14 (Application Authentication), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 1 (designing highly scalable, secure, and reliable cloud-native applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Let the client library find credentials from the environment. Why the correct answer wins: A dedicated service account gives the workload its own identity, which the shared default account does not.
- **B:** Correct. A dedicated identity whose roles can be granted and revoked independently. In this case: A dedicated service account gives the workload its own identity, which the shared default account does not.
- **C:** Incorrect for this question. The automatically created identity that usually carries broad project access. Why the correct answer wins: A dedicated service account gives the workload its own identity, which the shared default account does not.
- **D:** Incorrect for this question. A long-lived credential that has to be stored and rotated by hand. Why the correct answer wins: A dedicated service account gives the workload its own identity, which the shared default account does not.

### Question 26 — D

Answer: Bind a Kubernetes service account to a Google service account. Workload Identity binds the Kubernetes identity to a Google service account and issues short-lived credentials, so no key file exists. Keyless credential issuance for pods through Workload Identity. Local study-map skill 1.14 (Application Authentication), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 1 (designing highly scalable, secure, and reliable cloud-native applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A long-lived credential that has to be stored and rotated by hand. Why the correct answer wins: Workload Identity binds the Kubernetes identity to a Google service account and issues short-lived credentials, so no key file exists.
- **B:** Incorrect for this question. Let the client library find credentials from the environment. Why the correct answer wins: Workload Identity binds the Kubernetes identity to a Google service account and issues short-lived credentials, so no key file exists.
- **C:** Incorrect for this question. Inject the value into the process environment at start-up. Why the correct answer wins: Workload Identity binds the Kubernetes identity to a Google service account and issues short-lived credentials, so no key file exists.
- **D:** Correct. Keyless credential issuance for pods through Workload Identity. In this case: Workload Identity binds the Kubernetes identity to a Google service account and issues short-lived credentials, so no key file exists.

### Question 27 — B, D

Answers: Grant only the roles the workload needs; Apply a Kubernetes NetworkPolicy. A network policy restricts which pods may talk to it, and least privilege removes permissions the service never exercises. Scope permissions to the actions in use rather than the whole service. Restrict which pods may talk to which pods inside the cluster. Local study-map skill 1.15 (Least Privilege and Service-to-Service Security), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 1 (designing highly scalable, secure, and reliable cloud-native applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A legacy broad role that can change most resources in the project. Why the correct answer wins: A network policy restricts which pods may talk to it, and least privilege removes permissions the service never exercises.
- **B:** Correct. Scope permissions to the actions in use rather than the whole service. In this case: A network policy restricts which pods may talk to it, and least privilege removes permissions the service never exercises.
- **C:** Incorrect for this question. Serve every object to anyone, which removes the need to authorize at all. Why the correct answer wins: A network policy restricts which pods may talk to it, and least privilege removes permissions the service never exercises.
- **D:** Correct. Restrict which pods may talk to which pods inside the cluster. In this case: A network policy restricts which pods may talk to it, and least privilege removes permissions the service never exercises.
- **E:** Incorrect for this question. Let anyone reach the endpoint, which is only appropriate for public content. Why the correct answer wins: A network policy restricts which pods may talk to it, and least privilege removes permissions the service never exercises.

### Question 28 — D

Answer: Put Identity-Aware Proxy in front of the service. Identity-Aware Proxy authenticates and authorizes users before a request reaches the application. Authenticate and authorize users before a request reaches the application. Local study-map skill 1.15 (Least Privilege and Service-to-Service Security), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 1 (designing highly scalable, secure, and reliable cloud-native applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Let anyone reach the endpoint, which is only appropriate for public content. Why the correct answer wins: Identity-Aware Proxy authenticates and authorizes users before a request reaches the application.
- **B:** Incorrect for this question. Restrict which pods may talk to which pods inside the cluster. Why the correct answer wins: Identity-Aware Proxy authenticates and authorizes users before a request reaches the application.
- **C:** Incorrect for this question. A managed identity service for customer accounts and tokens. Why the correct answer wins: Identity-Aware Proxy authenticates and authorizes users before a request reaches the application.
- **D:** Correct. Authenticate and authorize users before a request reaches the application. In this case: Identity-Aware Proxy authenticates and authorizes users before a request reaches the application.

### Question 29 — B

Answer: Store the ledger in Spanner. A strongly consistent relational database provides cross-region transactions, which the document and wide-column stores do not. A relational database with strongly consistent multi-region transactions. Local study-map skill 1.16 (Storage and Schema Selection), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 1 (designing highly scalable, secure, and reliable cloud-native applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Durable object storage addressed by name rather than a database row. Why the correct answer wins: A strongly consistent relational database provides cross-region transactions, which the document and wide-column stores do not.
- **B:** Correct. A relational database with strongly consistent multi-region transactions. In this case: A strongly consistent relational database provides cross-region transactions, which the document and wide-column stores do not.
- **C:** Incorrect for this question. A document store with real-time listeners and mobile SDKs. Why the correct answer wins: A strongly consistent relational database provides cross-region transactions, which the document and wide-column stores do not.
- **D:** Incorrect for this question. Order the key so the query becomes a contiguous range scan. Why the correct answer wins: A strongly consistent relational database provides cross-region transactions, which the document and wide-column stores do not.

### Question 30 — B

Answer: Design the row key for the read pattern. Ordering the row key by device and time turns each read into a contiguous range scan at that write rate. Order the key so the query becomes a contiguous range scan. Local study-map skill 1.16 (Storage and Schema Selection), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 1 (designing highly scalable, secure, and reliable cloud-native applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A document store with real-time listeners and mobile SDKs. Why the correct answer wins: Ordering the row key by device and time turns each read into a contiguous range scan at that write rate.
- **B:** Correct. Order the key so the query becomes a contiguous range scan. In this case: Ordering the row key by device and time turns each read into a contiguous range scan at that write rate.
- **C:** Incorrect for this question. A relational database with strongly consistent multi-region transactions. Why the correct answer wins: Ordering the row key by device and time turns each read into a contiguous range scan at that write rate.
- **D:** Incorrect for this question. Durable object storage addressed by name rather than a database row. Why the correct answer wins: Ordering the row key by device and time turns each read into a contiguous range scan at that write rate.

### Question 31 — A

Answer: Issue a signed URL with a short expiry. A short-lived signed URL grants time-limited access to exactly that object. A time-limited grant to one object without exposing credentials. Local study-map skill 1.17 (Signed URLs and Time-Limited Access), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 1 (designing highly scalable, secure, and reliable cloud-native applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Correct. A time-limited grant to one object without exposing credentials. In this case: A short-lived signed URL grants time-limited access to exactly that object.
- **B:** Incorrect for this question. Serve every object to anyone, which removes the need to authorize at all. Why the correct answer wins: A short-lived signed URL grants time-limited access to exactly that object.
- **C:** Incorrect for this question. Make the retention period impossible to shorten, even by an owner. Why the correct answer wins: A short-lived signed URL grants time-limited access to exactly that object.
- **D:** Incorrect for this question. Transition or delete objects by age so retention happens without a job. Why the correct answer wins: A short-lived signed URL grants time-limited access to exactly that object.

### Question 32 — D

Answer: Stream the events into BigQuery. Streaming the events into the warehouse makes them queryable almost immediately. Land analytics rows in the warehouse for SQL and ML use. Local study-map skill 1.18 (Analytics and ML Data Handoff), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 1 (designing highly scalable, secure, and reliable cloud-native applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Durable object storage addressed by name rather than a database row. Why the correct answer wins: Streaming the events into the warehouse makes them queryable almost immediately.
- **B:** Incorrect for this question. A relational database with strongly consistent multi-region transactions. Why the correct answer wins: Streaming the events into the warehouse makes them queryable almost immediately.
- **C:** Incorrect for this question. Load a periodic extract rather than a continuous stream. Why the correct answer wins: Streaming the events into the warehouse makes them queryable almost immediately.
- **D:** Correct. Land analytics rows in the warehouse for SQL and ML use. In this case: Streaming the events into the warehouse makes them queryable almost immediately.

### Question 33 — B, C

Answers: Run the service emulator locally; Run an integration test against the emulator. A local emulator gives the test a Firestore-compatible target, and an integration test that runs in CI keeps the check in the pipeline rather than on one laptop. A local stand-in for a managed service used for unit and integration work. Exercise the wire-up between components before deploying. Local study-map skill 2.1 (Local Emulation of Cloud Services), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 2 (building and testing applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A browser terminal with the SDK and tooling already installed. Why the correct answer wins: A local emulator gives the test a Firestore-compatible target, and an integration test that runs in CI keeps the check in the pipeline rather than on one laptop.
- **B:** Correct. Exercise the wire-up between components before deploying. In this case: A local emulator gives the test a Firestore-compatible target, and an integration test that runs in CI keeps the check in the pipeline rather than on one laptop.
- **C:** Correct. A local stand-in for a managed service used for unit and integration work. In this case: A local emulator gives the test a Firestore-compatible target, and an integration test that runs in CI keeps the check in the pipeline rather than on one laptop.
- **D:** Incorrect for this question. Editor integration for scaffolding, running and debugging on Google Cloud. Why the correct answer wins: A local emulator gives the test a Firestore-compatible target, and an integration test that runs in CI keeps the check in the pipeline rather than on one laptop.
- **E:** Incorrect for this question. A managed registry with IAM-scoped repositories per environment. Why the correct answer wins: A local emulator gives the test a Firestore-compatible target, and an integration test that runs in CI keeps the check in the pipeline rather than on one laptop.

### Question 34 — D

Answer: Run the service emulator locally. A local emulator stands in for the managed service so the code path runs without any deployed resource. A local stand-in for a managed service used for unit and integration work. Local study-map skill 2.1 (Local Emulation of Cloud Services), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 2 (building and testing applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A managed, container-defined development environment behind a private endpoint. Why the correct answer wins: A local emulator stands in for the managed service so the code path runs without any deployed resource.
- **B:** Incorrect for this question. A browser terminal with the SDK and tooling already installed. Why the correct answer wins: A local emulator stands in for the managed service so the code path runs without any deployed resource.
- **C:** Incorrect for this question. Editor integration for scaffolding, running and debugging on Google Cloud. Why the correct answer wins: A local emulator stands in for the managed service so the code path runs without any deployed resource.
- **D:** Correct. A local stand-in for a managed service used for unit and integration work. In this case: A local emulator stands in for the managed service so the code path runs without any deployed resource.

### Question 35 — B

Answer: Use Cloud Workstations for the environment. A managed workstation configuration gives each contractor the same image with private access and no local state. A managed, container-defined development environment behind a private endpoint. Local study-map skill 2.1 (Local Emulation of Cloud Services), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 2 (building and testing applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Editor integration for scaffolding, running and debugging on Google Cloud. Why the correct answer wins: A managed workstation configuration gives each contractor the same image with private access and no local state.
- **B:** Correct. A managed, container-defined development environment behind a private endpoint. In this case: A managed workstation configuration gives each contractor the same image with private access and no local state.
- **C:** Incorrect for this question. Hand the source to the managed builder instead of shipping an image. Why the correct answer wins: A managed workstation configuration gives each contractor the same image with private access and no local state.
- **D:** Incorrect for this question. A browser terminal with the SDK and tooling already installed. Why the correct answer wins: A managed workstation configuration gives each contractor the same image with private access and no local state.

### Question 36 — A

Answer: Develop with Cloud Code in the IDE. Editor integration runs and debugs the service locally with breakpoints in the same buffer where the code is edited. Editor integration for scaffolding, running and debugging on Google Cloud. Local study-map skill 2.2 (Developer Tooling and AI Assistance), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 2 (building and testing applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Correct. Editor integration for scaffolding, running and debugging on Google Cloud. In this case: Editor integration runs and debugs the service locally with breakpoints in the same buffer where the code is edited.
- **B:** Incorrect for this question. A managed, container-defined development environment behind a private endpoint. Why the correct answer wins: Editor integration runs and debugs the service locally with breakpoints in the same buffer where the code is edited.
- **C:** Incorrect for this question. A browser terminal with the SDK and tooling already installed. Why the correct answer wins: Editor integration runs and debugs the service locally with breakpoints in the same buffer where the code is edited.
- **D:** Incorrect for this question. A local stand-in for a managed service used for unit and integration work. Why the correct answer wins: Editor integration runs and debugs the service locally with breakpoints in the same buffer where the code is edited.

### Question 37 — D

Answer: Iterate with Skaffold. A local iteration loop watches the source and redeploys on change, instead of a manual build-and-apply cycle. A loop that rebuilds and redeploys automatically on a source change. Local study-map skill 2.2 (Developer Tooling and AI Assistance), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 2 (building and testing applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A managed build service that runs the steps from a build configuration file. Why the correct answer wins: A local iteration loop watches the source and redeploys on change, instead of a manual build-and-apply cycle.
- **B:** Incorrect for this question. Hand the source to the managed builder instead of shipping an image. Why the correct answer wins: A local iteration loop watches the source and redeploys on change, instead of a manual build-and-apply cycle.
- **C:** Incorrect for this question. Release exactly the artifact that was tested rather than a moving tag. Why the correct answer wins: A local iteration loop watches the source and redeploys on change, instead of a manual build-and-apply cycle.
- **D:** Correct. A loop that rebuilds and redeploys automatically on a source change. In this case: A local iteration loop watches the source and redeploys on change, instead of a manual build-and-apply cycle.

### Question 38 — B

Answer: Connect the assistant to an MCP server. An MCP server exposes a defined tool surface to the assistant, replacing copy-paste context with calls. Give the assistant a defined tool surface instead of pasting context by hand. Local study-map skill 2.2 (Developer Tooling and AI Assistance), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 2 (building and testing applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Generate a first draft from context, then review and correct it. Why the correct answer wins: An MCP server exposes a defined tool surface to the assistant, replacing copy-paste context with calls.
- **B:** Correct. Give the assistant a defined tool surface instead of pasting context by hand. In this case: An MCP server exposes a defined tool surface to the assistant, replacing copy-paste context with calls.
- **C:** Incorrect for this question. An assistant that reads telemetry and proposes a cause and a next step. Why the correct answer wins: An MCP server exposes a defined tool surface to the assistant, replacing copy-paste context with calls.
- **D:** Incorrect for this question. A browser terminal with the SDK and tooling already installed. Why the correct answer wins: An MCP server exposes a defined tool surface to the assistant, replacing copy-paste context with calls.

### Question 39 — A, B

Answers: Build the image with Cloud Build; Push the image to Artifact Registry. The managed build service runs the steps from a configuration file, and a scoped registry holds the resulting artifact under its own access policy. A managed build service that runs the steps from a build configuration file. A managed registry with IAM-scoped repositories per environment. Local study-map skill 2.3 (Container Builds with Cloud Build), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 2 (building and testing applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Correct. A managed build service that runs the steps from a build configuration file. In this case: The managed build service runs the steps from a configuration file, and a scoped registry holds the resulting artifact under its own access policy.
- **B:** Correct. A managed registry with IAM-scoped repositories per environment. In this case: The managed build service runs the steps from a configuration file, and a scoped registry holds the resulting artifact under its own access policy.
- **C:** Incorrect for this question. Editor integration for scaffolding, running and debugging on Google Cloud. Why the correct answer wins: The managed build service runs the steps from a configuration file, and a scoped registry holds the resulting artifact under its own access policy.
- **D:** Incorrect for this question. The older registry whose access model is project-wide Cloud Storage. Why the correct answer wins: The managed build service runs the steps from a configuration file, and a scoped registry holds the resulting artifact under its own access policy.
- **E:** Incorrect for this question. A browser terminal with the SDK and tooling already installed. Why the correct answer wins: The managed build service runs the steps from a configuration file, and a scoped registry holds the resulting artifact under its own access policy.

### Question 40 — D

Answer: Trigger the build from a repository push. A repository trigger starts the build on every push, so the artifact follows the branch. Start the pipeline when the branch changes rather than by hand. Local study-map skill 2.3 (Container Builds with Cloud Build), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 2 (building and testing applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Fail the pipeline at the test stage instead of after deployment. Why the correct answer wins: A repository trigger starts the build on every push, so the artifact follows the branch.
- **B:** Incorrect for this question. A cron-style trigger that calls a target on a fixed timetable. Why the correct answer wins: A repository trigger starts the build on every push, so the artifact follows the branch.
- **C:** Incorrect for this question. A task queue with retries and rate control aimed at a specific target. Why the correct answer wins: A repository trigger starts the build on every push, so the artifact follows the branch.
- **D:** Correct. Start the pipeline when the branch changes rather than by hand. In this case: A repository trigger starts the build on every push, so the artifact follows the branch.

### Question 41 — D

Answer: Deploy a pinned image digest. Deploying a pinned digest guarantees the tested artifact is the one that runs. Release exactly the artifact that was tested rather than a moving tag. Local study-map skill 2.3 (Container Builds with Cloud Build), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 2 (building and testing applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Hand the source to the managed builder instead of shipping an image. Why the correct answer wins: Deploying a pinned digest guarantees the tested artifact is the one that runs.
- **B:** Incorrect for this question. A managed build service that runs the steps from a build configuration file. Why the correct answer wins: Deploying a pinned digest guarantees the tested artifact is the one that runs.
- **C:** Incorrect for this question. A managed registry with IAM-scoped repositories per environment. Why the correct answer wins: Deploying a pinned digest guarantees the tested artifact is the one that runs.
- **D:** Correct. Release exactly the artifact that was tested rather than a moving tag. In this case: Deploying a pinned digest guarantees the tested artifact is the one that runs.

### Question 42 — D

Answer: Run the tests as a Cloud Build step. Putting the suite in the pipeline runs it on every build and fails the build instead of shipping the defect. Fail the pipeline at the test stage instead of after deployment. Local study-map skill 2.3 (Container Builds with Cloud Build), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 2 (building and testing applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Make a passing test suite a precondition for release. Why the correct answer wins: Putting the suite in the pipeline runs it on every build and fails the build instead of shipping the defect.
- **B:** Incorrect for this question. Exercise the wire-up between components before deploying. Why the correct answer wins: Putting the suite in the pipeline runs it on every build and fails the build instead of shipping the defect.
- **C:** Incorrect for this question. Start the pipeline when the branch changes rather than by hand. Why the correct answer wins: Putting the suite in the pipeline runs it on every build and fails the build instead of shipping the defect.
- **D:** Correct. Fail the pipeline at the test stage instead of after deployment. In this case: Putting the suite in the pipeline runs it on every build and fails the build instead of shipping the defect.

### Question 43 — B

Answer: Push the image to Artifact Registry. A scoped registry applies IAM per repository, which a project-wide bucket-backed registry cannot. A managed registry with IAM-scoped repositories per environment. Local study-map skill 2.4 (Artifact Registry and Image Storage), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 2 (building and testing applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. The older registry whose access model is project-wide Cloud Storage. Why the correct answer wins: A scoped registry applies IAM per repository, which a project-wide bucket-backed registry cannot.
- **B:** Correct. A managed registry with IAM-scoped repositories per environment. In this case: A scoped registry applies IAM per repository, which a project-wide bucket-backed registry cannot.
- **C:** Incorrect for this question. A managed build service that runs the steps from a build configuration file. Why the correct answer wins: A scoped registry applies IAM per repository, which a project-wide bucket-backed registry cannot.
- **D:** Incorrect for this question. Durable object storage addressed by name rather than a database row. Why the correct answer wins: A scoped registry applies IAM per repository, which a project-wide bucket-backed registry cannot.

### Question 44 — C

Answer: Push the image to Artifact Registry. The managed registry integrates scanning and regional storage with the runtimes that pull from it. A managed registry with IAM-scoped repositories per environment. Local study-map skill 2.4 (Artifact Registry and Image Storage), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 2 (building and testing applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Editor integration for scaffolding, running and debugging on Google Cloud. Why the correct answer wins: The managed registry integrates scanning and regional storage with the runtimes that pull from it.
- **B:** Incorrect for this question. A managed build service that runs the steps from a build configuration file. Why the correct answer wins: The managed registry integrates scanning and regional storage with the runtimes that pull from it.
- **C:** Correct. A managed registry with IAM-scoped repositories per environment. In this case: The managed registry integrates scanning and regional storage with the runtimes that pull from it.
- **D:** Incorrect for this question. The older registry whose access model is project-wide Cloud Storage. Why the correct answer wins: The managed registry integrates scanning and regional storage with the runtimes that pull from it.

### Question 45 — C

Answer: Store the objects in Cloud Storage. Object storage is the durable place for artifacts that are not container images. Durable object storage addressed by name rather than a database row. Local study-map skill 2.4 (Artifact Registry and Image Storage), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 2 (building and testing applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. The older registry whose access model is project-wide Cloud Storage. Why the correct answer wins: Object storage is the durable place for artifacts that are not container images.
- **B:** Incorrect for this question. A managed build service that runs the steps from a build configuration file. Why the correct answer wins: Object storage is the durable place for artifacts that are not container images.
- **C:** Correct. Durable object storage addressed by name rather than a database row. In this case: Object storage is the durable place for artifacts that are not container images.
- **D:** Incorrect for this question. A managed registry with IAM-scoped repositories per environment. Why the correct answer wins: Object storage is the durable place for artifacts that are not container images.

### Question 46 — A

Answer: Enforce admission with Binary Authorization. Admission control blocks an image whose attestation does not satisfy the policy, which scanning or a finding review reports but does not prevent. Only images that satisfy the attestation policy may be deployed. Local study-map skill 2.5 (Build Provenance and Admission Control), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 2 (building and testing applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Correct. Only images that satisfy the attestation policy may be deployed. In this case: Admission control blocks an image whose attestation does not satisfy the policy, which scanning or a finding review reports but does not prevent.
- **B:** Incorrect for this question. Report known vulnerabilities in the image layers and packages. Why the correct answer wins: Admission control blocks an image whose attestation does not satisfy the policy, which scanning or a finding review reports but does not prevent.
- **C:** Incorrect for this question. Aggregate and triage security findings across the project. Why the correct answer wins: Admission control blocks an image whose attestation does not satisfy the policy, which scanning or a finding review reports but does not prevent.
- **D:** Incorrect for this question. A signed record of what was built and from which source. Why the correct answer wins: Admission control blocks an image whose attestation does not satisfy the policy, which scanning or a finding review reports but does not prevent.

### Question 47 — D

Answer: Scan the image with Artifact Analysis. Image scanning reports known vulnerabilities per image, which is the question being asked. Report known vulnerabilities in the image layers and packages. Local study-map skill 2.5 (Build Provenance and Admission Control), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 2 (building and testing applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A signed record of what was built and from which source. Why the correct answer wins: Image scanning reports known vulnerabilities per image, which is the question being asked.
- **B:** Incorrect for this question. Aggregate and triage security findings across the project. Why the correct answer wins: Image scanning reports known vulnerabilities per image, which is the question being asked.
- **C:** Incorrect for this question. Only images that satisfy the attestation policy may be deployed. Why the correct answer wins: Image scanning reports known vulnerabilities per image, which is the question being asked.
- **D:** Correct. Report known vulnerabilities in the image layers and packages. In this case: Image scanning reports known vulnerabilities per image, which is the question being asked.

### Question 48 — D

Answer: Review the finding in Security Command Center. The security command centre aggregates and triages findings across the project. Aggregate and triage security findings across the project. Local study-map skill 2.5 (Build Provenance and Admission Control), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 2 (building and testing applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Turn a recurring log pattern into a number that can be charted and alerted on. Why the correct answer wins: The security command centre aggregates and triages findings across the project.
- **B:** Incorrect for this question. Report known vulnerabilities in the image layers and packages. Why the correct answer wins: The security command centre aggregates and triages findings across the project.
- **C:** Incorrect for this question. Only images that satisfy the attestation policy may be deployed. Why the correct answer wins: The security command centre aggregates and triages findings across the project.
- **D:** Correct. Aggregate and triage security findings across the project. In this case: The security command centre aggregates and triages findings across the project.

### Question 49 — C, D

Answers: Add a unit test with dependencies stubbed; Use an AI coding assistant to draft the tests. A unit test exercises one unit with collaborators stubbed, and the assistant produces a draft the team reviews and corrects. Exercise one unit in isolation with its collaborators replaced. Generate a first draft from context, then review and correct it. Local study-map skill 2.6 (Unit Testing Practice), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 2 (building and testing applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Exercise the wire-up between components before deploying. Why the correct answer wins: A unit test exercises one unit with collaborators stubbed, and the assistant produces a draft the team reviews and corrects.
- **B:** Incorrect for this question. Keep the suite trustworthy while the unstable test is repaired. Why the correct answer wins: A unit test exercises one unit with collaborators stubbed, and the assistant produces a draft the team reviews and corrects.
- **C:** Correct. Exercise one unit in isolation with its collaborators replaced. In this case: A unit test exercises one unit with collaborators stubbed, and the assistant produces a draft the team reviews and corrects.
- **D:** Correct. Generate a first draft from context, then review and correct it. In this case: A unit test exercises one unit with collaborators stubbed, and the assistant produces a draft the team reviews and corrects.
- **E:** Incorrect for this question. Measure behaviour under expected peak traffic rather than guessing. Why the correct answer wins: A unit test exercises one unit with collaborators stubbed, and the assistant produces a draft the team reviews and corrects.

### Question 50 — B

Answer: Add a unit test with dependencies stubbed. Unit tests with stubbed dependencies isolate each branch and fail with the exact case. Exercise one unit in isolation with its collaborators replaced. Local study-map skill 2.6 (Unit Testing Practice), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 2 (building and testing applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Keep the suite trustworthy while the unstable test is repaired. Why the correct answer wins: Unit tests with stubbed dependencies isolate each branch and fail with the exact case.
- **B:** Correct. Exercise one unit in isolation with its collaborators replaced. In this case: Unit tests with stubbed dependencies isolate each branch and fail with the exact case.
- **C:** Incorrect for this question. Measure behaviour under expected peak traffic rather than guessing. Why the correct answer wins: Unit tests with stubbed dependencies isolate each branch and fail with the exact case.
- **D:** Incorrect for this question. Exercise the wire-up between components before deploying. Why the correct answer wins: Unit tests with stubbed dependencies isolate each branch and fail with the exact case.

### Question 51 — C

Answer: Quarantine the flaky test and fix it. Quarantining the unstable test and repairing it restores trust in the suite while keeping the signal. Keep the suite trustworthy while the unstable test is repaired. Local study-map skill 2.6 (Unit Testing Practice), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 2 (building and testing applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Exercise one unit in isolation with its collaborators replaced. Why the correct answer wins: Quarantining the unstable test and repairing it restores trust in the suite while keeping the signal.
- **B:** Incorrect for this question. Fail the pipeline at the test stage instead of after deployment. Why the correct answer wins: Quarantining the unstable test and repairing it restores trust in the suite while keeping the signal.
- **C:** Correct. Keep the suite trustworthy while the unstable test is repaired. In this case: Quarantining the unstable test and repairing it restores trust in the suite while keeping the signal.
- **D:** Incorrect for this question. Measure behaviour under expected peak traffic rather than guessing. Why the correct answer wins: Quarantining the unstable test and repairing it restores trust in the suite while keeping the signal.

### Question 52 — B, D

Answers: Run an integration test against the emulator; Run the tests as a Cloud Build step. An integration test exercises the wire-up rather than a stubbed collaborator, and running it as a build step enforces it on every merge. Exercise the wire-up between components before deploying. Fail the pipeline at the test stage instead of after deployment. Local study-map skill 2.7 (Automated Integration Testing), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 2 (building and testing applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Measure behaviour under expected peak traffic rather than guessing. Why the correct answer wins: An integration test exercises the wire-up rather than a stubbed collaborator, and running it as a build step enforces it on every merge.
- **B:** Correct. Exercise the wire-up between components before deploying. In this case: An integration test exercises the wire-up rather than a stubbed collaborator, and running it as a build step enforces it on every merge.
- **C:** Incorrect for this question. A local stand-in for a managed service used for unit and integration work. Why the correct answer wins: An integration test exercises the wire-up rather than a stubbed collaborator, and running it as a build step enforces it on every merge.
- **D:** Correct. Fail the pipeline at the test stage instead of after deployment. In this case: An integration test exercises the wire-up rather than a stubbed collaborator, and running it as a build step enforces it on every merge.
- **E:** Incorrect for this question. Exercise one unit in isolation with its collaborators replaced. Why the correct answer wins: An integration test exercises the wire-up rather than a stubbed collaborator, and running it as a build step enforces it on every merge.

### Question 53 — D

Answer: Run an integration test against the emulator. An integration test runs both sides against the same contract before the release. Exercise the wire-up between components before deploying. Local study-map skill 2.7 (Automated Integration Testing), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 2 (building and testing applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Measure behaviour under expected peak traffic rather than guessing. Why the correct answer wins: An integration test runs both sides against the same contract before the release.
- **B:** Incorrect for this question. Exercise one unit in isolation with its collaborators replaced. Why the correct answer wins: An integration test runs both sides against the same contract before the release.
- **C:** Incorrect for this question. Keep the suite trustworthy while the unstable test is repaired. Why the correct answer wins: An integration test runs both sides against the same contract before the release.
- **D:** Correct. Exercise the wire-up between components before deploying. In this case: An integration test runs both sides against the same contract before the release.

### Question 54 — D

Answer: Load-test the release before the rollout. A load test measures behaviour under expected peak traffic before the release. Measure behaviour under expected peak traffic rather than guessing. Local study-map skill 2.7 (Automated Integration Testing), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 2 (building and testing applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Make a passing test suite a precondition for release. Why the correct answer wins: A load test measures behaviour under expected peak traffic before the release.
- **B:** Incorrect for this question. Exercise one unit in isolation with its collaborators replaced. Why the correct answer wins: A load test measures behaviour under expected peak traffic before the release.
- **C:** Incorrect for this question. Exercise the wire-up between components before deploying. Why the correct answer wins: A load test measures behaviour under expected peak traffic before the release.
- **D:** Correct. Measure behaviour under expected peak traffic rather than guessing. In this case: A load test measures behaviour under expected peak traffic before the release.

### Question 55 — A

Answer: Block the deploy on the test result. Making a passing suite a precondition for release stops defects from shipping when tests fail. Make a passing test suite a precondition for release. Local study-map skill 2.7 (Automated Integration Testing), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 2 (building and testing applications): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Correct. Make a passing test suite a precondition for release. In this case: Making a passing suite a precondition for release stops defects from shipping when tests fail.
- **B:** Incorrect for this question. Fail the pipeline at the test stage instead of after deployment. Why the correct answer wins: Making a passing suite a precondition for release stops defects from shipping when tests fail.
- **C:** Incorrect for this question. Measure behaviour under expected peak traffic rather than guessing. Why the correct answer wins: Making a passing suite a precondition for release stops defects from shipping when tests fail.
- **D:** Incorrect for this question. Keep the suite trustworthy while the unstable test is repaired. Why the correct answer wins: Making a passing suite a precondition for release stops defects from shipping when tests fail.

### Question 56 — A

Answer: Deploy from source and let the platform build it. Deploying from source lets the platform build and run the service without a hand-written build artifact. Hand the source to the managed builder instead of shipping an image. Local study-map skill 3.1 (Deploying Cloud Run from Source), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 3 (configuring cloud-native applications for deployment): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Correct. Hand the source to the managed builder instead of shipping an image. In this case: Deploying from source lets the platform build and run the service without a hand-written build artifact.
- **B:** Incorrect for this question. A managed build service that runs the steps from a build configuration file. Why the correct answer wins: Deploying from source lets the platform build and run the service without a hand-written build artifact.
- **C:** Incorrect for this question. Wrap the existing process in a portable artifact that a managed runtime can execute. Why the correct answer wins: Deploying from source lets the platform build and run the service without a hand-written build artifact.
- **D:** Incorrect for this question. Release exactly the artifact that was tested rather than a moving tag. Why the correct answer wins: Deploying from source lets the platform build and run the service without a hand-written build artifact.

### Question 57 — C

Answer: Deploy a pinned image digest. A pinned digest guarantees that the tested artifact is the one serving traffic. Release exactly the artifact that was tested rather than a moving tag. Local study-map skill 3.1 (Deploying Cloud Run from Source), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 3 (configuring cloud-native applications for deployment): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Wrap the existing process in a portable artifact that a managed runtime can execute. Why the correct answer wins: A pinned digest guarantees that the tested artifact is the one serving traffic.
- **B:** Incorrect for this question. Hand the source to the managed builder instead of shipping an image. Why the correct answer wins: A pinned digest guarantees that the tested artifact is the one serving traffic.
- **C:** Correct. Release exactly the artifact that was tested rather than a moving tag. In this case: A pinned digest guarantees that the tested artifact is the one serving traffic.
- **D:** Incorrect for this question. Start the pipeline when the branch changes rather than by hand. Why the correct answer wins: A pinned digest guarantees that the tested artifact is the one serving traffic.

### Question 58 — B

Answer: Restrict ingress to internal traffic. Internal ingress restricts the network path, leaving public entry impossible even with a valid caller. Accept only traffic from the VPC and internal load balancers. Local study-map skill 3.1 (Deploying Cloud Run from Source), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 3 (configuring cloud-native applications for deployment): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Let anyone reach the endpoint, which is only appropriate for public content. Why the correct answer wins: Internal ingress restricts the network path, leaving public entry impossible even with a valid caller.
- **B:** Correct. Accept only traffic from the VPC and internal load balancers. In this case: Internal ingress restricts the network path, leaving public entry impossible even with a valid caller.
- **C:** Incorrect for this question. Authenticate and authorize users before a request reaches the application. Why the correct answer wins: Internal ingress restricts the network path, leaving public entry impossible even with a valid caller.
- **D:** Incorrect for this question. Control who may call the service with IAM rather than a shared token. Why the correct answer wins: Internal ingress restricts the network path, leaving public entry impossible even with a valid caller.

### Question 59 — D

Answer: Grant the invoker role to the calling identity. The invoker role on the service scopes the call permission to the identity that needs it. Control who may call the service with IAM rather than a shared token. Local study-map skill 3.1 (Deploying Cloud Run from Source), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 3 (configuring cloud-native applications for deployment): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Let anyone reach the endpoint, which is only appropriate for public content. Why the correct answer wins: The invoker role on the service scopes the call permission to the identity that needs it.
- **B:** Incorrect for this question. A legacy broad role that can change most resources in the project. Why the correct answer wins: The invoker role on the service scopes the call permission to the identity that needs it.
- **C:** Incorrect for this question. Authenticate and authorize users before a request reaches the application. Why the correct answer wins: The invoker role on the service scopes the call permission to the identity that needs it.
- **D:** Correct. Control who may call the service with IAM rather than a shared token. In this case: The invoker role on the service scopes the call permission to the identity that needs it.

### Question 60 — C, D

Answers: Route the event with Eventarc; Deliver to an HTTPS push subscription. An eventarc trigger turns the storage event into a delivery, and a push subscription style delivery posts it to the HTTPS endpoint. A trigger path that turns a Cloud Audit Log or resource event into a delivery. Push each message to an endpoint instead of having the consumer pull. Local study-map skill 3.2 (Cloud Run Triggers and Event Receivers), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 3 (configuring cloud-native applications for deployment): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A task queue with retries and rate control aimed at a specific target. Why the correct answer wins: An eventarc trigger turns the storage event into a delivery, and a push subscription style delivery posts it to the HTTPS endpoint.
- **B:** Incorrect for this question. A stateful sequence of service calls with retries and error branches. Why the correct answer wins: An eventarc trigger turns the storage event into a delivery, and a push subscription style delivery posts it to the HTTPS endpoint.
- **C:** Correct. A trigger path that turns a Cloud Audit Log or resource event into a delivery. In this case: An eventarc trigger turns the storage event into a delivery, and a push subscription style delivery posts it to the HTTPS endpoint.
- **D:** Correct. Push each message to an endpoint instead of having the consumer pull. In this case: An eventarc trigger turns the storage event into a delivery, and a push subscription style delivery posts it to the HTTPS endpoint.
- **E:** Incorrect for this question. A cron-style trigger that calls a target on a fixed timetable. Why the correct answer wins: An eventarc trigger turns the storage event into a delivery, and a push subscription style delivery posts it to the HTTPS endpoint.

### Question 61 — D

Answer: Have the worker pull from the subscription. A pulling consumer controls the pace and acknowledges only after the work commits. The consumer controls the pace and acknowledges messages itself. Local study-map skill 3.2 (Cloud Run Triggers and Event Receivers), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 3 (configuring cloud-native applications for deployment): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Push each message to an endpoint instead of having the consumer pull. Why the correct answer wins: A pulling consumer controls the pace and acknowledges only after the work commits.
- **B:** Incorrect for this question. A task queue with retries and rate control aimed at a specific target. Why the correct answer wins: A pulling consumer controls the pace and acknowledges only after the work commits.
- **C:** Incorrect for this question. A trigger path that turns a Cloud Audit Log or resource event into a delivery. Why the correct answer wins: A pulling consumer controls the pace and acknowledges only after the work commits.
- **D:** Correct. The consumer controls the pace and acknowledges messages itself. In this case: A pulling consumer controls the pace and acknowledges only after the work commits.

### Question 62 — C

Answer: Queue the work as a Cloud Tasks task. A task queue retries and rate-limits per task, which a cron trigger or a topic alone does not. A task queue with retries and rate control aimed at a specific target. Local study-map skill 3.2 (Cloud Run Triggers and Event Receivers), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 3 (configuring cloud-native applications for deployment): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A cron-style trigger that calls a target on a fixed timetable. Why the correct answer wins: A task queue retries and rate-limits per task, which a cron trigger or a topic alone does not.
- **B:** Incorrect for this question. A stateful sequence of service calls with retries and error branches. Why the correct answer wins: A task queue retries and rate-limits per task, which a cron trigger or a topic alone does not.
- **C:** Correct. A task queue with retries and rate control aimed at a specific target. In this case: A task queue retries and rate-limits per task, which a cron trigger or a topic alone does not.
- **D:** Incorrect for this question. A durable, at-least-once message channel with independent subscribers. Why the correct answer wins: A task queue retries and rate-limits per task, which a cron trigger or a topic alone does not.

### Question 63 — A

Answer: Schedule the invocation with Cloud Scheduler. A scheduled trigger calls the target on a fixed timetable. Local study-map skill 3.2 (Cloud Run Triggers and Event Receivers), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 3 (configuring cloud-native applications for deployment): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Correct. In this case: A scheduled trigger calls the target on a fixed timetable.
- **B:** Incorrect for this question. A stateful sequence of service calls with retries and error branches. Why the correct answer wins: A scheduled trigger calls the target on a fixed timetable.
- **C:** Incorrect for this question. A trigger path that turns a Cloud Audit Log or resource event into a delivery. Why the correct answer wins: A scheduled trigger calls the target on a fixed timetable.
- **D:** Incorrect for this question. A task queue with retries and rate control aimed at a specific target. Why the correct answer wins: A scheduled trigger calls the target on a fixed timetable.

### Question 64 — B, E

Answers: Raise the per-instance concurrency limit; Cap the maximum instance count. Concurrency limits how many requests share one instance's memory, and a maximum instance cap bounds the bill. Let each instance serve more simultaneous requests before another instance is started. Bound the blast radius and the bill at the cost of queueing when the cap is reached. Local study-map skill 3.3 (Cloud Run Service Configuration), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 3 (configuring cloud-native applications for deployment): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Pay for idle capacity so a cold start never appears in the latency percentiles. Why the correct answer wins: Concurrency limits how many requests share one instance's memory, and a maximum instance cap bounds the bill.
- **B:** Correct. Let each instance serve more simultaneous requests before another instance is started. In this case: Concurrency limits how many requests share one instance's memory, and a maximum instance cap bounds the bill.
- **C:** Incorrect for this question. Charge only while a request is being handled, which suits bursty traffic. Why the correct answer wins: Concurrency limits how many requests share one instance's memory, and a maximum instance cap bounds the bill.
- **D:** Incorrect for this question. Give extra CPU during start-up so initialization finishes faster at a small extra charge. Why the correct answer wins: Concurrency limits how many requests share one instance's memory, and a maximum instance cap bounds the bill.
- **E:** Correct. Bound the blast radius and the bill at the cost of queueing when the cap is reached. In this case: Concurrency limits how many requests share one instance's memory, and a maximum instance cap bounds the bill.

### Question 65 — B

Answer: Keep a minimum number of instances warm. Keeping a minimum number of instances warm removes the cold start from that path. Pay for idle capacity so a cold start never appears in the latency percentiles. Local study-map skill 3.3 (Cloud Run Service Configuration), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 3 (configuring cloud-native applications for deployment): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Give extra CPU during start-up so initialization finishes faster at a small extra charge. Why the correct answer wins: Keeping a minimum number of instances warm removes the cold start from that path.
- **B:** Correct. Pay for idle capacity so a cold start never appears in the latency percentiles. In this case: Keeping a minimum number of instances warm removes the cold start from that path.
- **C:** Incorrect for this question. Let each instance serve more simultaneous requests before another instance is started. Why the correct answer wins: Keeping a minimum number of instances warm removes the cold start from that path.
- **D:** Incorrect for this question. Bound the blast radius and the bill at the cost of queueing when the cap is reached. Why the correct answer wins: Keeping a minimum number of instances warm removes the cold start from that path.

### Question 66 — B

Answer: Configure a startup probe. A startup probe holds traffic until the application reports that it is ready to serve. Hold traffic until the application is actually ready to serve. Local study-map skill 3.3 (Cloud Run Service Configuration), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 3 (configuring cloud-native applications for deployment): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Remove the instance from the endpoint list while it cannot serve. Why the correct answer wins: A startup probe holds traffic until the application reports that it is ready to serve.
- **B:** Correct. Hold traffic until the application is actually ready to serve. In this case: A startup probe holds traffic until the application reports that it is ready to serve.
- **C:** Incorrect for this question. Restart the container when it can no longer make progress. Why the correct answer wins: A startup probe holds traffic until the application reports that it is ready to serve.
- **D:** Incorrect for this question. Add pods when average CPU crosses the target. Why the correct answer wins: A startup probe holds traffic until the application reports that it is ready to serve.

### Question 67 — A

Answer: Restrict ingress to internal traffic. Internal ingress removes the public path entirely, which caller-level checks do not. Accept only traffic from the VPC and internal load balancers. Local study-map skill 3.3 (Cloud Run Service Configuration), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 3 (configuring cloud-native applications for deployment): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Correct. Accept only traffic from the VPC and internal load balancers. In this case: Internal ingress removes the public path entirely, which caller-level checks do not.
- **B:** Incorrect for this question. Let anyone reach the endpoint, which is only appropriate for public content. Why the correct answer wins: Internal ingress removes the public path entirely, which caller-level checks do not.
- **C:** Incorrect for this question. Authenticate and authorize users before a request reaches the application. Why the correct answer wins: Internal ingress removes the public path entirely, which caller-level checks do not.
- **D:** Incorrect for this question. Control who may call the service with IAM rather than a shared token. Why the correct answer wins: Internal ingress removes the public path entirely, which caller-level checks do not.

### Question 68 — B

Answer: Introduce a new API version alongside the old one. A new version alongside the old one keeps existing clients working while the change is adopted. Keep the old contract working while the new one is adopted. Local study-map skill 3.4 (API Exposure and Versioning), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 3 (configuring cloud-native applications for deployment): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A machine-readable contract that generates clients and validates requests. Why the correct answer wins: A new version alongside the old one keeps existing clients working while the change is adopted.
- **B:** Correct. Keep the old contract working while the new one is adopted. In this case: A new version alongside the old one keeps existing clients working while the change is adopted.
- **C:** Incorrect for this question. Reject or queue requests above a threshold so one client cannot exhaust the service. Why the correct answer wins: A new version alongside the old one keeps existing clients working while the change is adopted.
- **D:** Incorrect for this question. Extend the contract so existing clients keep working unchanged. Why the correct answer wins: A new version alongside the old one keeps existing clients working while the change is adopted.

### Question 69 — A

Answer: Add the field in a backward-compatible way. Extending the contract in a backward-compatible way keeps every existing client working. Extend the contract so existing clients keep working unchanged. Local study-map skill 3.4 (API Exposure and Versioning), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 3 (configuring cloud-native applications for deployment): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Correct. Extend the contract so existing clients keep working unchanged. In this case: Extending the contract in a backward-compatible way keeps every existing client working.
- **B:** Incorrect for this question. Bound how many calls a plan allows in a window. Why the correct answer wins: Extending the contract in a backward-compatible way keeps every existing client working.
- **C:** Incorrect for this question. Keep the old contract working while the new one is adopted. Why the correct answer wins: Extending the contract in a backward-compatible way keeps every existing client working.
- **D:** Incorrect for this question. A machine-readable contract that generates clients and validates requests. Why the correct answer wins: Extending the contract in a backward-compatible way keeps every existing client working.

### Question 70 — A, B

Answers: Use a rolling update strategy; Tune maxSurge and maxUnavailable. The rolling update strategy replaces pods gradually, and the surge and unavailability settings bound how much capacity disappears at once. Replace pods gradually so the deployment stays available. Control how much capacity may be missing while pods are replaced. Local study-map skill 3.5 (Deploying Containers to GKE), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 3 (configuring cloud-native applications for deployment): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Correct. Replace pods gradually so the deployment stays available. In this case: The rolling update strategy replaces pods gradually, and the surge and unavailability settings bound how much capacity disappears at once.
- **B:** Correct. Control how much capacity may be missing while pods are replaced. In this case: The rolling update strategy replaces pods gradually, and the surge and unavailability settings bound how much capacity disappears at once.
- **C:** Incorrect for this question. Limit how many pods may be evicted at once during voluntary disruption. Why the correct answer wins: The rolling update strategy replaces pods gradually, and the surge and unavailability settings bound how much capacity disappears at once.
- **D:** Incorrect for this question. Use reclaimable capacity for work that can tolerate a node disappearing. Why the correct answer wins: The rolling update strategy replaces pods gradually, and the surge and unavailability settings bound how much capacity disappears at once.
- **E:** Incorrect for this question. Add or remove nodes as pending pods demand capacity. Why the correct answer wins: The rolling update strategy replaces pods gradually, and the surge and unavailability settings bound how much capacity disappears at once.

### Question 71 — A

Answer: Deploy the workload to Google Kubernetes Engine. A managed Kubernetes control plane exposes pod composition and scheduling, which the simpler runtimes do not. A managed Kubernetes control plane where pods, node pools and cluster-scoped policy are yours to configure. Local study-map skill 3.5 (Deploying Containers to GKE), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 3 (configuring cloud-native applications for deployment): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Correct. A managed Kubernetes control plane where pods, node pools and cluster-scoped policy are yours to configure. In this case: A managed Kubernetes control plane exposes pod composition and scheduling, which the simpler runtimes do not.
- **B:** Incorrect for this question. A platform runtime that manages scaling for a supported language version and its sandbox limits. Why the correct answer wins: A managed Kubernetes control plane exposes pod composition and scheduling, which the simpler runtimes do not.
- **C:** Incorrect for this question. Virtual machines where the operating system, runtime and scaling group are all managed by the team. Why the correct answer wins: A managed Kubernetes control plane exposes pod composition and scheduling, which the simpler runtimes do not.
- **D:** Incorrect for this question. A managed container runtime that scales to zero and bills per request while it serves traffic. Why the correct answer wins: A managed Kubernetes control plane exposes pod composition and scheduling, which the simpler runtimes do not.

### Question 72 — A

Answer: Constrain pods to the intended node pool. Constraining the pods to their own pool keeps them off nodes sized for the interactive service. Place work on nodes whose shape and pricing match the workload. Local study-map skill 3.5 (Deploying Containers to GKE), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 3 (configuring cloud-native applications for deployment): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Correct. Place work on nodes whose shape and pricing match the workload. In this case: Constraining the pods to their own pool keeps them off nodes sized for the interactive service.
- **B:** Incorrect for this question. Use reclaimable capacity for work that can tolerate a node disappearing. Why the correct answer wins: Constraining the pods to their own pool keeps them off nodes sized for the interactive service.
- **C:** Incorrect for this question. Add or remove nodes as pending pods demand capacity. Why the correct answer wins: Constraining the pods to their own pool keeps them off nodes sized for the interactive service.
- **D:** Incorrect for this question. Add pods when average CPU crosses the target. Why the correct answer wins: Constraining the pods to their own pool keeps them off nodes sized for the interactive service.

### Question 73 — C

Answer: Add a PodDisruptionBudget. A disruption budget limits how many pods may be evicted together during voluntary disruption. Limit how many pods may be evicted at once during voluntary disruption. Local study-map skill 3.5 (Deploying Containers to GKE), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 3 (configuring cloud-native applications for deployment): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Bound the total capacity a namespace may consume. Why the correct answer wins: A disruption budget limits how many pods may be evicted together during voluntary disruption.
- **B:** Incorrect for this question. Keep capacity warm so scale-up does not cost the first requests. Why the correct answer wins: A disruption budget limits how many pods may be evicted together during voluntary disruption.
- **C:** Correct. Limit how many pods may be evicted at once during voluntary disruption. In this case: A disruption budget limits how many pods may be evicted together during voluntary disruption.
- **D:** Incorrect for this question. Replace pods gradually so the deployment stays available. Why the correct answer wins: A disruption budget limits how many pods may be evicted together during voluntary disruption.

### Question 74 — D

Answer: Configure a readiness probe. A readiness probe removes the pod from the endpoint list while it cannot serve. Remove the instance from the endpoint list while it cannot serve. Local study-map skill 3.6 (Kubernetes Health Checks), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 3 (configuring cloud-native applications for deployment): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Restart the container when it can no longer make progress. Why the correct answer wins: A readiness probe removes the pod from the endpoint list while it cannot serve.
- **B:** Incorrect for this question. Add pods when average CPU crosses the target. Why the correct answer wins: A readiness probe removes the pod from the endpoint list while it cannot serve.
- **C:** Incorrect for this question. Hold traffic until the application is actually ready to serve. Why the correct answer wins: A readiness probe removes the pod from the endpoint list while it cannot serve.
- **D:** Correct. Remove the instance from the endpoint list while it cannot serve. In this case: A readiness probe removes the pod from the endpoint list while it cannot serve.

### Question 75 — C

Answer: Configure a liveness probe. A liveness probe restarts a container that can no longer make progress. Restart the container when it can no longer make progress. Local study-map skill 3.6 (Kubernetes Health Checks), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 3 (configuring cloud-native applications for deployment): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Remove the instance from the endpoint list while it cannot serve. Why the correct answer wins: A liveness probe restarts a container that can no longer make progress.
- **B:** Incorrect for this question. Limit how many pods may be evicted at once during voluntary disruption. Why the correct answer wins: A liveness probe restarts a container that can no longer make progress.
- **C:** Correct. Restart the container when it can no longer make progress. In this case: A liveness probe restarts a container that can no longer make progress.
- **D:** Incorrect for this question. Hold traffic until the application is actually ready to serve. Why the correct answer wins: A liveness probe restarts a container that can no longer make progress.

### Question 76 — C

Answer: Configure a startup probe. A startup probe gives initialization its own budget before the liveness check applies. Hold traffic until the application is actually ready to serve. Local study-map skill 3.6 (Kubernetes Health Checks), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 3 (configuring cloud-native applications for deployment): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Remove the instance from the endpoint list while it cannot serve. Why the correct answer wins: A startup probe gives initialization its own budget before the liveness check applies.
- **B:** Incorrect for this question. Restart the container when it can no longer make progress. Why the correct answer wins: A startup probe gives initialization its own budget before the liveness check applies.
- **C:** Correct. Hold traffic until the application is actually ready to serve. In this case: A startup probe gives initialization its own budget before the liveness check applies.
- **D:** Incorrect for this question. Add pods on a signal that tracks demand better than CPU. Why the correct answer wins: A startup probe gives initialization its own budget before the liveness check applies.

### Question 77 — B, D

Answers: Scale pods on a custom or external metric; Set a minimum replica count. A custom or external metric tracks the queue rather than the processor, and a minimum replica count keeps workers waiting. Add pods on a signal that tracks demand better than CPU. Keep capacity warm so scale-up does not cost the first requests. Local study-map skill 3.7 (Horizontal Pod Autoscaling), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 3 (configuring cloud-native applications for deployment): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Add pods when average CPU crosses the target. Why the correct answer wins: A custom or external metric tracks the queue rather than the processor, and a minimum replica count keeps workers waiting.
- **B:** Correct. Keep capacity warm so scale-up does not cost the first requests. In this case: A custom or external metric tracks the queue rather than the processor, and a minimum replica count keeps workers waiting.
- **C:** Incorrect for this question. Bound the total capacity a namespace may consume. Why the correct answer wins: A custom or external metric tracks the queue rather than the processor, and a minimum replica count keeps workers waiting.
- **D:** Correct. Add pods on a signal that tracks demand better than CPU. In this case: A custom or external metric tracks the queue rather than the processor, and a minimum replica count keeps workers waiting.
- **E:** Incorrect for this question. Limit how many pods may be evicted at once during voluntary disruption. Why the correct answer wins: A custom or external metric tracks the queue rather than the processor, and a minimum replica count keeps workers waiting.

### Question 78 — D

Answer: Scale pods on CPU utilization. CPU-based autoscaling follows demand directly when the processor is the constraint. Add pods when average CPU crosses the target. Local study-map skill 3.7 (Horizontal Pod Autoscaling), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 3 (configuring cloud-native applications for deployment): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Add or remove nodes as pending pods demand capacity. Why the correct answer wins: CPU-based autoscaling follows demand directly when the processor is the constraint.
- **B:** Incorrect for this question. Keep capacity warm so scale-up does not cost the first requests. Why the correct answer wins: CPU-based autoscaling follows demand directly when the processor is the constraint.
- **C:** Incorrect for this question. Add pods on a signal that tracks demand better than CPU. Why the correct answer wins: CPU-based autoscaling follows demand directly when the processor is the constraint.
- **D:** Correct. Add pods when average CPU crosses the target. In this case: CPU-based autoscaling follows demand directly when the processor is the constraint.

### Question 79 — C

Answer: Set a namespace resource quota. A namespace quota caps total capacity so one team cannot starve the others. Bound the total capacity a namespace may consume. Local study-map skill 3.7 (Horizontal Pod Autoscaling), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 3 (configuring cloud-native applications for deployment): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Limit how many pods may be evicted at once during voluntary disruption. Why the correct answer wins: A namespace quota caps total capacity so one team cannot starve the others.
- **B:** Incorrect for this question. Add pods when average CPU crosses the target. Why the correct answer wins: A namespace quota caps total capacity so one team cannot starve the others.
- **C:** Correct. Bound the total capacity a namespace may consume. In this case: A namespace quota caps total capacity so one team cannot starve the others.
- **D:** Incorrect for this question. Place work on nodes whose shape and pricing match the workload. Why the correct answer wins: A namespace quota caps total capacity so one team cannot starve the others.

### Question 80 — B, D

Answers: Connect through the Cloud SQL Auth Proxy; Pool and reuse database connections. The authorized proxy handles identity and encryption without a network path decision, and pooling keeps the connection count small. A local proxy that authorizes the connection with IAM and encrypts it. Keep a small set of warm connections instead of opening one per request. Local study-map skill 4.1 (Connecting to Datastores), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 4 (integrating applications with Google Cloud services): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A client library that resolves and authorizes the instance itself. Why the correct answer wins: The authorized proxy handles identity and encryption without a network path decision, and pooling keeps the connection count small.
- **B:** Correct. Keep a small set of warm connections instead of opening one per request. In this case: The authorized proxy handles identity and encryption without a network path decision, and pooling keeps the connection count small.
- **C:** Incorrect for this question. A private address reachable from the VPC without a proxy process. Why the correct answer wins: The authorized proxy handles identity and encryption without a network path decision, and pooling keeps the connection count small.
- **D:** Correct. A local proxy that authorizes the connection with IAM and encrypts it. In this case: The authorized proxy handles identity and encryption without a network path decision, and pooling keeps the connection count small.
- **E:** Incorrect for this question. A long-lived credential that has to be stored and rotated by hand. Why the correct answer wins: The authorized proxy handles identity and encryption without a network path decision, and pooling keeps the connection count small.

### Question 81 — C

Answer: Pool and reuse database connections. Reusing a small pool of connections stops the churn that exhausts the ceiling. Keep a small set of warm connections instead of opening one per request. Local study-map skill 4.1 (Connecting to Datastores), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 4 (integrating applications with Google Cloud services): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A client library that resolves and authorizes the instance itself. Why the correct answer wins: Reusing a small pool of connections stops the churn that exhausts the ceiling.
- **B:** Incorrect for this question. A private address reachable from the VPC without a proxy process. Why the correct answer wins: Reusing a small pool of connections stops the churn that exhausts the ceiling.
- **C:** Correct. Keep a small set of warm connections instead of opening one per request. In this case: Reusing a small pool of connections stops the churn that exhausts the ceiling.
- **D:** Incorrect for this question. A local proxy that authorizes the connection with IAM and encrypts it. Why the correct answer wins: Reusing a small pool of connections stops the churn that exhausts the ceiling.

### Question 82 — B

Answer: Use the language connector with IAM. The language connector resolves and authorizes the instance from inside the client library. A client library that resolves and authorizes the instance itself. Local study-map skill 4.1 (Connecting to Datastores), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 4 (integrating applications with Google Cloud services): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A local proxy that authorizes the connection with IAM and encrypts it. Why the correct answer wins: The language connector resolves and authorizes the instance from inside the client library.
- **B:** Correct. A client library that resolves and authorizes the instance itself. In this case: The language connector resolves and authorizes the instance from inside the client library.
- **C:** Incorrect for this question. A long-lived credential that has to be stored and rotated by hand. Why the correct answer wins: The language connector resolves and authorizes the instance from inside the client library.
- **D:** Incorrect for this question. A private address reachable from the VPC without a proxy process. Why the correct answer wins: The language connector resolves and authorizes the instance from inside the client library.

### Question 83 — C

Answer: Connect over the database private IP. A private address on the shared network needs no proxy in the request path. A private address reachable from the VPC without a proxy process. Local study-map skill 4.1 (Connecting to Datastores), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 4 (integrating applications with Google Cloud services): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A client library that resolves and authorizes the instance itself. Why the correct answer wins: A private address on the shared network needs no proxy in the request path.
- **B:** Incorrect for this question. A local proxy that authorizes the connection with IAM and encrypts it. Why the correct answer wins: A private address on the shared network needs no proxy in the request path.
- **C:** Correct. A private address reachable from the VPC without a proxy process. In this case: A private address on the shared network needs no proxy in the request path.
- **D:** Incorrect for this question. A reachable address that requires encrypted connections from any client. Why the correct answer wins: A private address on the shared network needs no proxy in the request path.

### Question 84 — C

Answer: Use Firestore in Native mode. A native document store provides listeners and offline client support, which the other stores do not. A document store with real-time listeners and mobile SDKs. Local study-map skill 4.1 (Connecting to Datastores), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 4 (integrating applications with Google Cloud services): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A relational database with strongly consistent multi-region transactions. Why the correct answer wins: A native document store provides listeners and offline client support, which the other stores do not.
- **B:** Incorrect for this question. Order the key so the query becomes a contiguous range scan. Why the correct answer wins: A native document store provides listeners and offline client support, which the other stores do not.
- **C:** Correct. A document store with real-time listeners and mobile SDKs. In this case: A native document store provides listeners and offline client support, which the other stores do not.
- **D:** Incorrect for this question. A local proxy that authorizes the connection with IAM and encrypts it. Why the correct answer wins: A native document store provides listeners and offline client support, which the other stores do not.

### Question 85 — A

Answer: Make the handler idempotent with a deduplication key. A deduplication key lets the handler skip a repeat delivery of the same event. Recognise a repeated delivery and skip the duplicate work. Local study-map skill 4.2 (Publishing and Consuming Messages), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 4 (integrating applications with Google Cloud services): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Correct. Recognise a repeated delivery and skip the duplicate work. In this case: A deduplication key lets the handler skip a repeat delivery of the same event.
- **B:** Incorrect for this question. A task queue with retries and rate control aimed at a specific target. Why the correct answer wins: A deduplication key lets the handler skip a repeat delivery of the same event.
- **C:** Incorrect for this question. A durable, at-least-once message channel with independent subscribers. Why the correct answer wins: A deduplication key lets the handler skip a repeat delivery of the same event.
- **D:** Incorrect for this question. Hold messages that exhausted their delivery attempts for later inspection. Why the correct answer wins: A deduplication key lets the handler skip a repeat delivery of the same event.

### Question 86 — C

Answer: Add a dead-letter topic. A dead-letter topic parks the message after its attempts so the rest of the backlog can move. Hold messages that exhausted their delivery attempts for later inspection. Local study-map skill 4.2 (Publishing and Consuming Messages), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 4 (integrating applications with Google Cloud services): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. The consumer controls the pace and acknowledges messages itself. Why the correct answer wins: A dead-letter topic parks the message after its attempts so the rest of the backlog can move.
- **B:** Incorrect for this question. Recognise a repeated delivery and skip the duplicate work. Why the correct answer wins: A dead-letter topic parks the message after its attempts so the rest of the backlog can move.
- **C:** Correct. Hold messages that exhausted their delivery attempts for later inspection. In this case: A dead-letter topic parks the message after its attempts so the rest of the backlog can move.
- **D:** Incorrect for this question. Push each message to an endpoint instead of having the consumer pull. Why the correct answer wins: A dead-letter topic parks the message after its attempts so the rest of the backlog can move.

### Question 87 — A

Answer: Publish the event to a Pub/Sub topic. A topic fans one event out to independent subscribers. A durable, at-least-once message channel with independent subscribers. Local study-map skill 4.2 (Publishing and Consuming Messages), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 4 (integrating applications with Google Cloud services): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Correct. A durable, at-least-once message channel with independent subscribers. In this case: A topic fans one event out to independent subscribers.
- **B:** Incorrect for this question. A stateful sequence of service calls with retries and error branches. Why the correct answer wins: A topic fans one event out to independent subscribers.
- **C:** Incorrect for this question. A task queue with retries and rate control aimed at a specific target. Why the correct answer wins: A topic fans one event out to independent subscribers.
- **D:** Incorrect for this question. A cron-style trigger that calls a target on a fixed timetable. Why the correct answer wins: A topic fans one event out to independent subscribers.

### Question 88 — C

Answer: Queue the work as a Cloud Tasks task. A task queue targets one endpoint with per-task retry and rate control. A task queue with retries and rate control aimed at a specific target. Local study-map skill 4.2 (Publishing and Consuming Messages), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 4 (integrating applications with Google Cloud services): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A stateful sequence of service calls with retries and error branches. Why the correct answer wins: A task queue targets one endpoint with per-task retry and rate control.
- **B:** Incorrect for this question. A durable, at-least-once message channel with independent subscribers. Why the correct answer wins: A task queue targets one endpoint with per-task retry and rate control.
- **C:** Correct. A task queue with retries and rate control aimed at a specific target. In this case: A task queue targets one endpoint with per-task retry and rate control.
- **D:** Incorrect for this question. A trigger path that turns a Cloud Audit Log or resource event into a delivery. Why the correct answer wins: A task queue targets one endpoint with per-task retry and rate control.

### Question 89 — B, C

Answers: Retry with exponential backoff and jitter; Follow the page token until results are exhausted. Exponential backoff with jitter survives the throttling, and pagination follows the page tokens until the collection is exhausted. Space out repeated attempts so a throttled quota can recover instead of being hammered. Request each page in turn so a truncated response is completed rather than assumed whole. Local study-map skill 4.3 (Calling Google Cloud APIs), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 4 (integrating applications with Google Cloud services): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Reuse a result that has not changed, avoiding an identical call. Why the correct answer wins: Exponential backoff with jitter survives the throttling, and pagination follows the page tokens until the collection is exhausted.
- **B:** Correct. Request each page in turn so a truncated response is completed rather than assumed whole. In this case: Exponential backoff with jitter survives the throttling, and pagination follows the page tokens until the collection is exhausted.
- **C:** Correct. Space out repeated attempts so a throttled quota can recover instead of being hammered. In this case: Exponential backoff with jitter survives the throttling, and pagination follows the page tokens until the collection is exhausted.
- **D:** Incorrect for this question. Reduce per-call overhead when the API supports a batch surface. Why the correct answer wins: Exponential backoff with jitter survives the throttling, and pagination follows the page tokens until the collection is exhausted.
- **E:** Incorrect for this question. Turn a recurring log pattern into a number that can be charted and alerted on. Why the correct answer wins: Exponential backoff with jitter survives the throttling, and pagination follows the page tokens until the collection is exhausted.

### Question 90 — A

Answer: Request only the fields the caller needs. Restricting returned fields shrinks the payload to what is actually used. Trim the response payload so latency and cost follow actual use. Local study-map skill 4.3 (Calling Google Cloud APIs), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 4 (integrating applications with Google Cloud services): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Correct. Trim the response payload so latency and cost follow actual use. In this case: Restricting returned fields shrinks the payload to what is actually used.
- **B:** Incorrect for this question. Request each page in turn so a truncated response is completed rather than assumed whole. Why the correct answer wins: Restricting returned fields shrinks the payload to what is actually used.
- **C:** Incorrect for this question. Reduce per-call overhead when the API supports a batch surface. Why the correct answer wins: Restricting returned fields shrinks the payload to what is actually used.
- **D:** Incorrect for this question. Reuse a result that has not changed, avoiding an identical call. Why the correct answer wins: Restricting returned fields shrinks the payload to what is actually used.

### Question 91 — D

Answer: Cache the response for its freshness window. Caching the results stops the repeated identical calls. Reuse a result that has not changed, avoiding an identical call. Local study-map skill 4.3 (Calling Google Cloud APIs), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 4 (integrating applications with Google Cloud services): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Request each page in turn so a truncated response is completed rather than assumed whole. Why the correct answer wins: Caching the results stops the repeated identical calls.
- **B:** Incorrect for this question. Reduce per-call overhead when the API supports a batch surface. Why the correct answer wins: Caching the results stops the repeated identical calls.
- **C:** Incorrect for this question. Space out repeated attempts so a throttled quota can recover instead of being hammered. Why the correct answer wins: Caching the results stops the repeated identical calls.
- **D:** Correct. Reuse a result that has not changed, avoiding an identical call. In this case: Caching the results stops the repeated identical calls.

### Question 92 — B

Answer: Retry with exponential backoff and jitter. Exponential backoff with jitter spreads the retries and lets the quota recover. Space out repeated attempts so a throttled quota can recover instead of being hammered. Local study-map skill 4.3 (Calling Google Cloud APIs), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 4 (integrating applications with Google Cloud services): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A dedicated identity whose roles can be granted and revoked independently. Why the correct answer wins: Exponential backoff with jitter spreads the retries and lets the quota recover.
- **B:** Correct. Space out repeated attempts so a throttled quota can recover instead of being hammered. In this case: Exponential backoff with jitter spreads the retries and lets the quota recover.
- **C:** Incorrect for this question. Reuse a result that has not changed, avoiding an identical call. Why the correct answer wins: Exponential backoff with jitter spreads the retries and lets the quota recover.
- **D:** Incorrect for this question. Trim the response payload so latency and cost follow actual use. Why the correct answer wins: Exponential backoff with jitter spreads the retries and lets the quota recover.

### Question 93 — C

Answer: Give the workload its own service account. A dedicated service account gives the backend its own reviewable identity. A dedicated identity whose roles can be granted and revoked independently. Local study-map skill 4.4 (Service Accounts for API Calls), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 4 (integrating applications with Google Cloud services): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. The automatically created identity that usually carries broad project access. Why the correct answer wins: A dedicated service account gives the backend its own reviewable identity.
- **B:** Incorrect for this question. Let the client library find credentials from the environment. Why the correct answer wins: A dedicated service account gives the backend its own reviewable identity.
- **C:** Correct. A dedicated identity whose roles can be granted and revoked independently. In this case: A dedicated service account gives the backend its own reviewable identity.
- **D:** Incorrect for this question. A long-lived credential that has to be stored and rotated by hand. Why the correct answer wins: A dedicated service account gives the backend its own reviewable identity.

### Question 94 — B

Answer: Grant only the roles the workload needs. Least privilege narrows the grant to the one permission in use. Scope permissions to the actions in use rather than the whole service. Local study-map skill 4.4 (Service Accounts for API Calls), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 4 (integrating applications with Google Cloud services): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Let anyone reach the endpoint, which is only appropriate for public content. Why the correct answer wins: Least privilege narrows the grant to the one permission in use.
- **B:** Correct. Scope permissions to the actions in use rather than the whole service. In this case: Least privilege narrows the grant to the one permission in use.
- **C:** Incorrect for this question. A legacy broad role that can change most resources in the project. Why the correct answer wins: Least privilege narrows the grant to the one permission in use.
- **D:** Incorrect for this question. A long-lived credential that has to be stored and rotated by hand. Why the correct answer wins: Least privilege narrows the grant to the one permission in use.

### Question 95 — A

Answer: Emit structured JSON logs. Structured fields make the tenant a queryable dimension instead of prose. Emit fields the log viewer can index so queries and alerts are possible. Local study-map skill 4.5 (Metrics, Logs, and Traces), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 4 (integrating applications with Google Cloud services): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Correct. Emit fields the log viewer can index so queries and alerts are possible. In this case: Structured fields make the tenant a queryable dimension instead of prose.
- **B:** Incorrect for this question. Turn a recurring log pattern into a number that can be charted and alerted on. Why the correct answer wins: Structured fields make the tenant a queryable dimension instead of prose.
- **C:** Incorrect for this question. Group and count application errors instead of grepping logs. Why the correct answer wins: Structured fields make the tenant a queryable dimension instead of prose.
- **D:** Incorrect for this question. Let filters and alerting distinguish routine output from errors. Why the correct answer wins: Structured fields make the tenant a queryable dimension instead of prose.

### Question 96 — B

Answer: Instrument a span around the downstream call. A span around the downstream call shows where the time inside the request is spent. Show where time goes inside a request that crosses services. Local study-map skill 4.5 (Metrics, Logs, and Traces), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 4 (integrating applications with Google Cloud services): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Publish an application signal that infrastructure metrics cannot see. Why the correct answer wins: A span around the downstream call shows where the time inside the request is spent.
- **B:** Correct. Show where time goes inside a request that crosses services. In this case: A span around the downstream call shows where the time inside the request is spent.
- **C:** Incorrect for this question. Group and count application errors instead of grepping logs. Why the correct answer wins: A span around the downstream call shows where the time inside the request is spent.
- **D:** Incorrect for this question. Join spans from different services into one trace. Why the correct answer wins: A span around the downstream call shows where the time inside the request is spent.

### Question 97 — D

Answer: Emit a custom metric from the code. A custom metric publishes the value so it can be charted and alerted on. Publish an application signal that infrastructure metrics cannot see. Local study-map skill 4.5 (Metrics, Logs, and Traces), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 4 (integrating applications with Google Cloud services): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Turn a recurring log pattern into a number that can be charted and alerted on. Why the correct answer wins: A custom metric publishes the value so it can be charted and alerted on.
- **B:** Incorrect for this question. Notify a human when a threshold is crossed. Why the correct answer wins: A custom metric publishes the value so it can be charted and alerted on.
- **C:** Incorrect for this question. Emit fields the log viewer can index so queries and alerts are possible. Why the correct answer wins: A custom metric publishes the value so it can be charted and alerted on.
- **D:** Correct. Publish an application signal that infrastructure metrics cannot see. In this case: A custom metric publishes the value so it can be charted and alerted on.

### Question 98 — D

Answer: Send the exception to Error Reporting. Error grouping collapses the variants so the distinct failures can be counted. Group and count application errors instead of grepping logs. Local study-map skill 4.6 (Error Reporting and Trace Correlation), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 4 (integrating applications with Google Cloud services): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Publish an application signal that infrastructure metrics cannot see. Why the correct answer wins: Error grouping collapses the variants so the distinct failures can be counted.
- **B:** Incorrect for this question. Emit fields the log viewer can index so queries and alerts are possible. Why the correct answer wins: Error grouping collapses the variants so the distinct failures can be counted.
- **C:** Incorrect for this question. Turn a recurring log pattern into a number that can be charted and alerted on. Why the correct answer wins: Error grouping collapses the variants so the distinct failures can be counted.
- **D:** Correct. Group and count application errors instead of grepping logs. In this case: Error grouping collapses the variants so the distinct failures can be counted.

### Question 99 — A

Answer: Propagate the trace ID between services. Propagating the trace identifier gives every entry a shared key to correlate on. Join spans from different services into one trace. Local study-map skill 4.6 (Error Reporting and Trace Correlation), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 4 (integrating applications with Google Cloud services): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Correct. Join spans from different services into one trace. In this case: Propagating the trace identifier gives every entry a shared key to correlate on.
- **B:** Incorrect for this question. Group and count application errors instead of grepping logs. Why the correct answer wins: Propagating the trace identifier gives every entry a shared key to correlate on.
- **C:** Incorrect for this question. Publish an application signal that infrastructure metrics cannot see. Why the correct answer wins: Propagating the trace identifier gives every entry a shared key to correlate on.
- **D:** Incorrect for this question. Show where time goes inside a request that crosses services. Why the correct answer wins: Propagating the trace identifier gives every entry a shared key to correlate on.

### Question 100 — A

Answer: Ask Gemini Cloud Assist for a diagnosis. The cloud assistant summarises telemetry into a cause and a next step. An assistant that reads telemetry and proposes a cause and a next step. Local study-map skill 4.7 (AI-Assisted Observability), mapped to the official guide: Google Cloud Professional Cloud Developer exam guide (four sections, retrieved October 2026). Primary reference: Professional Cloud Developer exam guide section 4 (integrating applications with Google Cloud services): https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf.

- **A:** Correct. An assistant that reads telemetry and proposes a cause and a next step. In this case: The cloud assistant summarises telemetry into a cause and a next step.
- **B:** Incorrect for this question. Give the assistant a defined tool surface instead of pasting context by hand. Why the correct answer wins: The cloud assistant summarises telemetry into a cause and a next step.
- **C:** Incorrect for this question. Find the function consuming CPU or memory under real traffic. Why the correct answer wins: The cloud assistant summarises telemetry into a cause and a next step.
- **D:** Incorrect for this question. Generate a first draft from context, then review and correct it. Why the correct answer wins: The cloud assistant summarises telemetry into a cause and a next step.
