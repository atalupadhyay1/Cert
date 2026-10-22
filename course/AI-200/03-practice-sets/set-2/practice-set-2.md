# Microsoft AI-200 — Full-Length Mock Exam 2

Azure AI Cloud Developer Associate · 100 questions · expanded practice bank · passing target 700/1000

Blueprint-weighted mock exam of 100 items. Item mix: 76 single-choice, 16 multi-select (selection count stated), 8 ordering items rendered as answer choices, and 4 case studies of 3 questions. Hot-area, drag-and-drop UI, labs, and adaptive problem-solution sets cannot be reproduced in a CSV; see the README for the exact fidelity boundary.

Original educational content, not actual, recalled, or copied Microsoft exam items.

## Questions

### 1. A regulated release must prove exactly which image digest ran in production when an incident is reviewed. What should the pipeline publish and deploy?

Domain: Develop containerized solutions on Azure

- A. Replicate the registry to each deployment region
- B. Build and store versioned images in Azure Container Registry
- C. Deploy the mutable latest tag and let the platform resolve it
- D. Run image builds on demand or on a trigger with ACR Tasks

### 2. A nightly job must rebuild the inference image from the main branch without any developer machine involved. What should be configured?

Domain: Develop containerized solutions on Azure

- A. Run image builds on demand or on a trigger with ACR Tasks
- B. Build and store versioned images in Azure Container Registry
- C. Apply an ACR retention policy to prune old untagged manifests
- D. Stage the change in a deployment slot and swap after verification

### 3. A small internal API must run a container with deployment slots and platform-managed patching, and no Kubernetes expertise is available. What should host it?

Domain: Develop containerized solutions on Azure

- A. Run the batch job in Azure Container Instances
- B. Deploy the service to Azure Container Apps
- C. Deploy the workload to Azure Kubernetes Service
- D. Deploy the image to Azure App Service as a web app

### 4. A new build must be warmed and verified before it receives production traffic, with an instant rollback path. What should be used?

Domain: Develop containerized solutions on Azure

- A. Supply configuration through App Service application settings
- B. Stage the change in a deployment slot and swap after verification
- C. Deploy the mutable latest tag and let the platform resolve it
- D. Create a new Container Apps revision and shift traffic between revisions

### 5. A patient-facing endpoint must respond in under a second on the first request after idle periods. Which Container Apps setting addresses that?

Domain: Develop containerized solutions on Azure

- A. Set a minimum replica count above zero for the container app
- B. Scale the container app on an event source with a KEDA scaler
- C. Rely on the horizontal pod autoscaler on CPU
- D. Create a new Container Apps revision and shift traffic between revisions

### 6. A queue-driven OCR worker must scale to zero when no documents are waiting and grow with the backlog. What should drive scaling?

Domain: Develop containerized solutions on Azure

- A. Rely on the horizontal pod autoscaler on CPU
- B. Scale only on CPU utilization without an event scaler
- C. Scale the container app on an event source with a KEDA scaler
- D. Run the batch job in Azure Container Instances

### 7. A pod is killed repeatedly because the container takes longer to start than the liveness threshold allows. What should be corrected?

Domain: Develop containerized solutions on Azure

- A. Run the batch job in Azure Container Instances
- B. Apply a declarative Kubernetes manifest to the cluster
- C. Rely on the horizontal pod autoscaler on CPU
- D. Add readiness and liveness probes to the pod specification

### 8. A Kubernetes deployment restarts pods intermittently, and the team needs the platform events and container logs in one query. What should be used?

Domain: Develop containerized solutions on Azure

- A. Enable diagnostic settings to route platform logs to the workspace
- B. Query container logs and Kubernetes events in Log Analytics
- C. Test end-to-end connectivity from inside the container to each dependency
- D. Send telemetry to Application Insights and inspect the transaction view

### 9. Which sequence correctly deploys a manifest change and verifies it?

Domain: Develop containerized solutions on Azure

- A. Write the manifest → apply it to the cluster → wait for pod readiness → test ingress connectivity
- B. Apply the manifest → write the manifest → test ingress connectivity → wait for pod readiness
- C. Wait for pod readiness → apply the manifest → write the manifest → test ingress connectivity
- D. Write the manifest → test ingress connectivity → apply it to the cluster → wait for pod readiness

### 10. A service must support a canary release and must not administer a cluster. Which two choices satisfy that? Select two.

Domain: Develop containerized solutions on Azure

- A. Run the batch job in Azure Container Instances
- B. Set a minimum replica count above zero for the container app
- C. Rely on the horizontal pod autoscaler on CPU
- D. Deploy the service to Azure Container Apps
- E. Create a new Container Apps revision and shift traffic between revisions

### 11. A deployment must be reproducible from version control and must not receive traffic before it is ready. Which two elements are required? Select two.

Domain: Develop containerized solutions on Azure

- A. Run the batch job in Azure Container Instances
- B. Add readiness and liveness probes to the pod specification
- C. Apply a declarative Kubernetes manifest to the cluster
- D. Run image builds on demand or on a trigger with ACR Tasks
- E. Tune the scale rule cool-down period and maximum replicas

### 12. Documents with variable, nested shape must be stored and queried by a patient identifier with low latency. Which store fits?

Domain: Develop AI solutions by using Azure data management services

- A. Store the documents in Azure Cosmos DB for NoSQL
- B. Use Azure Queue Storage for the work items
- C. Store embeddings in PostgreSQL by using the pgvector extension
- D. Cache responses in Azure Managed Redis

### 13. A container has a steady baseline with sharp morning peaks, and throttling appears only at peak. Which throughput setting fits best?

Domain: Develop AI solutions by using Azure data management services

- A. Increase provisioned throughput and watch the RU charge per query
- B. Enable autoscale throughput with a maximum RU limit
- C. Index every property by using the default automatic policy
- D. Choose the account consistency level that matches the read requirement

### 14. A NoSQL container holds millions of chunk embeddings and must keep memory use reasonable while serving similarity queries. Which index type should be selected?

Domain: Develop AI solutions by using Azure data management services

- A. Create an HNSW index for low-latency approximate search
- B. Scan every document and compute similarity in application code
- C. Declare the embedding dimensions and vector index type on the container policy
- D. Use the DiskANN vector index for large collections

### 15. Two processor instances must share change feed partitions without processing the same batch twice. What coordinates them?

Domain: Develop AI solutions by using Azure data management services

- A. Run a change feed processor to react to new and updated items
- B. Use a lease container to coordinate change feed readers
- C. Enable autoscale throughput with a maximum RU limit
- D. Enable duplicate detection on the queue

### 16. A memory-constrained database must hold a large vector table, and slight recall loss is acceptable. Which index type fits?

Domain: Develop AI solutions by using Azure data management services

- A. Create an IVFFlat index to save memory on a large table
- B. Create an HNSW index for low-latency approximate search
- C. Query without a vector index and let PostgreSQL scan the table
- D. Increase maintenance and query memory settings for index builds and sorts

### 17. Vector queries became slower after thousands of rows were deleted and reloaded. What maintenance should be reviewed?

Domain: Develop AI solutions by using Azure data management services

- A. Run VACUUM and ANALYZE after bulk loads and large deletes
- B. Reuse a bounded connection pool instead of opening a connection per request
- C. Increase maintenance and query memory settings for index builds and sorts
- D. Increase storage throughput for index builds and bulk loads

### 18. A serverless consumer can open hundreds of connections in a burst and exceeds the server connection limit. What should be placed in front of the database?

Domain: Develop AI solutions by using Azure data management services

- A. Place a connection pooler in front of PostgreSQL for many short-lived clients
- B. Reuse a bounded connection pool instead of opening a connection per request
- C. Use prepared statements and batch round trips
- D. Add a read replica and send all vector queries to it

### 19. Cached summaries must never be older than fifteen minutes even if invalidations fail. What should be set?

Domain: Develop AI solutions by using Azure data management services

- A. Rely on the eviction policy and skip explicit TTLs
- B. Invalidate or overwrite the cache entry when the source changes
- C. Flush the database after each deployment to guarantee fresh data
- D. Set a TTL on each cached entry

### 20. A clinician must see their own just-saved note appear on the next screen, while other screens may lag slightly. Which level fits?

Domain: Develop AI solutions by using Azure data management services

- A. Use eventual consistency to minimize read cost
- B. Use session consistency for reads within the same client session
- C. Choose the account consistency level that matches the read requirement
- D. Use strong consistency for every read in the account

### 21. A retrieval table must have fast typed filters and must not return rows the caller may not see. Which two design choices are required? Select two.

Domain: Develop AI solutions by using Azure data management services

- A. Retrieve nearest neighbours first and discard unauthorized rows in the application
- B. Add a read replica and send all vector queries to it
- C. Model typed columns for filters and one vector column for the embedding
- D. Query without a vector index and let PostgreSQL scan the table
- E. Filter on metadata columns in the same query as the vector search

### 22. Vector latency degrades because the index no longer fits in memory and sorts spill to disk. Which two adjustments address that? Select two.

Domain: Develop AI solutions by using Azure data management services

- A. Place a connection pooler in front of PostgreSQL for many short-lived clients
- B. Increase maintenance and query memory settings for index builds and sorts
- C. Create an IVFFlat index to save memory on a large table
- D. Scale compute and memory to fit index size and query concurrency
- E. Increase storage throughput for index builds and bulk loads

### 23. Which sequence correctly prepares a Cosmos DB container for vector search?

Domain: Develop AI solutions by using Azure data management services

- A. Query with VectorDistance → upsert items with embeddings → create the container with a vector policy → apply metadata filters
- B. Apply metadata filters → query with VectorDistance → create the container with a vector policy → upsert items with embeddings
- C. Create the container with a vector policy → upsert items with embeddings → query with VectorDistance → apply metadata filters
- D. Upsert items with embeddings → create the container with a vector policy → apply metadata filters → query with VectorDistance

### 24. Each intake document must be processed by exactly one worker group with crash recovery. What should be used?

Domain: Connect to and consume Azure services

- A. Queue the work on a Service Bus queue and process it with a worker
- B. Use Azure Queue Storage for the work items
- C. Stream telemetry through Azure Event Hubs
- D. Publish to a Service Bus topic with multiple subscriptions

### 25. Document events must reach indexing, redaction, and audit independently, each at its own pace. What should be used?

Domain: Connect to and consume Azure services

- A. Queue the work on a Service Bus queue and process it with a worker
- B. Define a custom event schema for the topic
- C. Publish to a Service Bus topic with multiple subscriptions
- D. Use Azure Queue Storage for the work items

### 26. Message processing is latency-bound by individual receives, and lock duration comfortably exceeds batch processing time. What can improve throughput?

Domain: Connect to and consume Azure services

- A. Increase prefetch count to reduce round trips
- B. Enable duplicate detection on the queue
- C. Use Service Bus sessions to keep related messages ordered
- D. Set a maximum delivery count and handle the dead-letter path

### 27. A handler must react to blob creation events without polling storage. What should the subscription target?

Domain: Connect to and consume Azure services

- A. Define a custom event schema for the topic
- B. Rely on Event Grid retries with a dead-letter destination
- C. Subscribe to a system topic for resource events
- D. Filter the Event Grid subscription by subject or event type

### 28. A subscription should receive only events whose subject begins with a specific department path. What should be configured?

Domain: Connect to and consume Azure services

- A. Define a custom event schema for the topic
- B. Rely on Event Grid retries with a dead-letter destination
- C. Add a SQL or correlation filter to a subscription
- D. Filter the Event Grid subscription by subject or event type

### 29. A function must write the extracted entity to Cosmos DB with minimal client code. What should be used?

Domain: Connect to and consume Azure services

- A. Bind a queue or event trigger to the function
- B. Use input and output bindings instead of hand-written SDK calls
- C. Expose the endpoint through an HTTP trigger
- D. Orchestrate the multi-step workflow with Durable Functions

### 30. A multi-step redaction workflow must survive a host restart mid-processing and resume where it stopped. What should be used?

Domain: Connect to and consume Azure services

- A. Expose the endpoint through an HTTP trigger
- B. Move long-running work out of the HTTP request into a queue
- C. Orchestrate the multi-step workflow with Durable Functions
- D. Implement the handler as an Azure Function

### 31. A function must start when a document is queued and must persist the result without custom client code. Which two features provide that? Select two.

Domain: Connect to and consume Azure services

- A. Use input and output bindings instead of hand-written SDK calls
- B. Expose the endpoint through an HTTP trigger
- C. Orchestrate the multi-step workflow with Durable Functions
- D. Host the function app on a premium plan with pre-warmed instances
- E. Bind a queue or event trigger to the function

### 32. A function must avoid cold starts and call Key Vault without storing credentials. Which two choices are required? Select two.

Domain: Connect to and consume Azure services

- A. Orchestrate the multi-step workflow with Durable Functions
- B. Host the function app on the consumption plan
- C. Host the function app on a premium plan with pre-warmed instances
- D. Expose the endpoint through an HTTP trigger
- E. Assign a managed identity to the function app and use it for downstream calls

### 33. Which sequence correctly handles a document through the intake queue?

Domain: Connect to and consume Azure services

- A. Publish the message → receive with peek-lock → process the work → complete the message → dead-letter after the delivery limit
- B. Receive with peek-lock → publish the message → complete the message → process the work → dead-letter after the delivery limit
- C. Process the work → receive with peek-lock → publish the message → complete the message → dead-letter after the delivery limit
- D. Publish the message → complete the message → receive with peek-lock → process the work → dead-letter after the delivery limit

### 34. An imaging vendor credential must be auditable, revocable, and never visible in a container image. Where should it be stored?

Domain: Secure, monitor, troubleshoot Azure solutions

- A. Store settings and feature flags in Azure App Configuration
- B. Supply configuration through App Service application settings
- C. Pin the application to a specific secret version
- D. Store the secret in Azure Key Vault and read it at runtime

### 35. Threshold values must change per environment without redeploying and without storing secrets in the store. What should be used?

Domain: Secure, monitor, troubleshoot Azure solutions

- A. Store settings and feature flags in Azure App Configuration
- B. Store the secret in Azure Key Vault and read it at runtime
- C. Use App Configuration labels to separate environments
- D. Reference the Key Vault secret from an App Configuration key value

### 36. A changed feature flag is not observed by the running app until it restarts. What should be enabled?

Domain: Secure, monitor, troubleshoot Azure solutions

- A. Enable configuration refresh so changes apply without a restart
- B. Use App Configuration labels to separate environments
- C. Deploy the function app through a CI pipeline with app settings applied
- D. Use head or tail sampling so trace volume stays within budget

### 37. One intake request crosses an API, a Service Bus queue, and a function, and the team needs the full path with timings. What should be implemented?

Domain: Secure, monitor, troubleshoot Azure solutions

- A. Send telemetry to Application Insights and inspect the transaction view
- B. Enable diagnostic settings to route platform logs to the workspace
- C. Instrument the service with the OpenTelemetry SDK
- D. Query the workspace with KQL to find the failing operation

### 38. A KQL query over thirty days scans every column and takes minutes. What should be changed first?

Domain: Secure, monitor, troubleshoot Azure solutions

- A. Store repeated aggregations in a materialized view or update policy
- B. Join the requests and dependencies tables on the operation ID
- C. Project only the columns needed and filter by time first
- D. Aggregate with summarize and bin to see the failure rate over time

### 39. The team needs p95 intake latency per hour rather than one average for the day. Which construct should be used?

Domain: Secure, monitor, troubleshoot Azure solutions

- A. Create an alert rule on the failure rate or latency metric
- B. Store repeated aggregations in a materialized view or update policy
- C. Aggregate with summarize and bin to see the failure rate over time
- D. Project only the columns needed and filter by time first

### 40. A deployment identity can modify the vault but the application only reads secrets. What should be changed?

Domain: Secure, monitor, troubleshoot Azure solutions

- A. Supply configuration through App Service application settings
- B. Store the secret in Azure Key Vault and read it at runtime
- C. Assign a least-privilege role to the application identity
- D. Authenticate with a managed identity instead of a stored key

### 41. Which sequence correctly delivers a custom document event to a subscriber?

Domain: Secure, monitor, troubleshoot Azure solutions

- A. Publish a custom event → evaluate the subscription filter → deliver to the handler → retry on failure → dead-letter undeliverable events
- B. Deliver to the handler → publish a custom event → evaluate the subscription filter → retry on failure → dead-letter undeliverable events
- C. Publish a custom event → deliver to the handler → evaluate the subscription filter → dead-letter undeliverable events → retry on failure
- D. Evaluate the subscription filter → publish a custom event → dead-letter undeliverable events → deliver to the handler → retry on failure

### 42. A handler receives at-least-once deliveries and must reject replays while still dead-lettering persistent failures. Which two mechanisms are required? Select two.

Domain: Connect to and consume Azure services

- A. Set a maximum delivery count and handle the dead-letter path
- B. Use Service Bus sessions to keep related messages ordered
- C. Receive in receive-and-delete mode for at-most-once delivery
- D. Make the handler idempotent by using a message or business key
- E. Enable duplicate detection on the queue

### 43. A request path spans an API, a queue, and a function, and the team must retain rare failures without unlimited telemetry cost. Which two practices are required? Select two.

Domain: Secure, monitor, troubleshoot Azure solutions

- A. Use head or tail sampling so trace volume stays within budget
- B. Instrument the service with the OpenTelemetry SDK
- C. Query the workspace with KQL to find the failing operation
- D. Propagate trace context across every service and queue hop
- E. Enable diagnostic settings to route platform logs to the workspace

### 44. A storage account used for extraction output must not be reachable from the public internet. What should be configured?

Domain: Secure, monitor, troubleshoot Azure solutions

- A. Reach the data service through a private endpoint
- B. Authenticate with a managed identity instead of a stored key
- C. Assign a least-privilege role to the application identity
- D. Enable diagnostic settings to route platform logs to the workspace

### 45. The clinical imaging registry holds four years of untagged manifests and storage cost keeps climbing, while deployments reference only versioned tags. What should be applied?

Domain: Develop containerized solutions on Azure

- A. Replicate the registry to each deployment region
- B. Deploy the mutable latest tag and let the platform resolve it
- C. Build and store versioned images in Azure Container Registry
- D. Apply an ACR retention policy to prune old untagged manifests

### 46. When the base image receives a security patch, every intake service image must be rebuilt automatically with no workstation involved. What should perform the rebuild?

Domain: Develop containerized solutions on Azure

- A. Deploy the workload to Azure Kubernetes Service
- B. Implement the handler as an Azure Function
- C. Run image builds on demand or on a trigger with ACR Tasks
- D. Build and store versioned images in Azure Container Registry

### 47. The intake API needs a document-intelligence key, and security forbids the value from appearing in deployment settings. What should be configured?

Domain: Develop containerized solutions on Azure

- A. Supply configuration through App Service application settings
- B. Pin the application to a specific secret version
- C. Mount non-secret configuration from a Kubernetes ConfigMap
- D. Reference a Key Vault secret from the app configuration instead of storing it

### 48. A document-intake API must be verified in a staging slot before promotion, and its OCR endpoint must differ per environment. Which two actions should you take? Select two.

Domain: Develop containerized solutions on Azure

- A. Stage the change in a deployment slot and swap after verification
- B. Apply a declarative Kubernetes manifest to the cluster
- C. Scale the container app on an event source with a KEDA scaler
- D. Supply configuration through App Service application settings
- E. Create a new Container Apps revision and shift traffic between revisions

### 49. A small clinical team wants revisions, scale-to-zero, and no cluster to patch or upgrade. Where should the intake API run?

Domain: Develop containerized solutions on Azure

- A. Deploy the workload to Azure Kubernetes Service
- B. Deploy the service to Azure Container Apps
- C. Run the batch job in Azure Container Instances
- D. Deploy the image to Azure App Service as a web app

### 50. Clinical intake must never pay a thirty-second model load on the first request of a shift. What should be configured?

Domain: Develop containerized solutions on Azure

- A. Set a minimum replica count above zero for the container app
- B. Scale the container app on an event source with a KEDA scaler
- C. Scale only on CPU utilization without an event scaler
- D. Tune the scale rule cool-down period and maximum replicas

### 51. A pod accepts traffic before its extraction model finishes loading and returns 503 for the first half minute. What should be added?

Domain: Develop containerized solutions on Azure

- A. Query container logs and Kubernetes events in Log Analytics
- B. Add readiness and liveness probes to the pod specification
- C. Run the batch job in Azure Container Instances
- D. Rely on the horizontal pod autoscaler on CPU

### 52. Only the intake pods fail to reach the cache after a network policy change, while other workloads connect normally. What should be tested?

Domain: Develop containerized solutions on Azure

- A. Add readiness and liveness probes to the pod specification
- B. Test end-to-end connectivity from inside the container to each dependency
- C. Enable diagnostic settings to route platform logs to the workspace
- D. Aggregate with summarize and bin to see the failure rate over time

### 53. A single-container intake API needs deployment slots, managed TLS, and patching handled by the platform with no cluster. Where should it run?

Domain: Develop containerized solutions on Azure

- A. Run the batch job in Azure Container Instances
- B. Deploy the service to Azure Container Apps
- C. Deploy the workload to Azure Kubernetes Service
- D. Deploy the image to Azure App Service as a web app

### 54. Which sequence correctly promotes a new document-extraction revision to full traffic?

Domain: Develop containerized solutions on Azure

- A. Shift all traffic to a new revision → deploy the revision → check metrics → build the image → promote
- B. Check metrics → deploy a new revision → build and push the image → shift a small traffic percentage → promote
- C. Deploy a new revision → shift all traffic → build and push the image → check metrics → roll back
- D. Build and push the image → deploy a new revision → shift a small traffic percentage → check metrics → promote or roll back

### 55. Extracted document metadata must be stored as JSON with per-tenant isolation and single-digit-millisecond point reads. Which store fits?

Domain: Develop AI solutions by using Azure data management services

- A. Include the partition key in the query predicate
- B. Store embeddings in PostgreSQL by using the pgvector extension
- C. Store the documents in Azure Cosmos DB for NoSQL
- D. Use Azure Queue Storage for the work items

### 56. Ingestion bursts trigger 429 responses by day while the nightly baseline is nearly idle. What should be configured?

Domain: Develop AI solutions by using Azure data management services

- A. Index every property by using the default automatic policy
- B. Increase provisioned throughput and watch the RU charge per query
- C. Restrict the indexing policy to the paths the queries use
- D. Enable autoscale throughput with a maximum RU limit

### 57. Every write to a document with forty properties costs far more than expected, and queries touch only three of them. What should be changed?

Domain: Develop AI solutions by using Azure data management services

- A. Restrict the indexing policy to the paths the queries use
- B. Enable autoscale throughput with a maximum RU limit
- C. Index every property by using the default automatic policy
- D. Add a composite index for the filtered and ordered properties

### 58. An overnight analytics read tolerates seconds of lag and the team wants the lowest possible read cost. Which consistency choice fits?

Domain: Develop AI solutions by using Azure data management services

- A. Use session consistency for reads within the same client session
- B. Use eventual consistency to minimize read cost
- C. Choose the account consistency level that matches the read requirement
- D. Use strong consistency for every read in the account

### 59. Clinical notes and their embeddings must be searched together, with department and date filters applied in the same query. What should be used?

Domain: Develop AI solutions by using Azure data management services

- A. Scan every document and compute similarity in application code
- B. Use the DiskANN vector index for large collections
- C. Store embeddings in a vector property and query with VectorDistance
- D. Store embeddings in PostgreSQL by using the pgvector extension

### 60. Audit rows and their embeddings must be queried by patient and date beside a vector predicate in one statement. How should the table be modeled?

Domain: Develop AI solutions by using Azure data management services

- A. Model typed columns for filters and one vector column for the embedding
- B. Add a read replica and send all vector queries to it
- C. Increase storage throughput for index builds and bulk loads
- D. Scale compute and memory to fit index size and query concurrency

### 61. Semantic search over half a million chunks must answer in tens of milliseconds with recall close to exact. Which index fits?

Domain: Develop AI solutions by using Azure data management services

- A. Create an IVFFlat index to save memory on a large table
- B. Place a connection pooler in front of PostgreSQL for many short-lived clients
- C. Create an HNSW index for low-latency approximate search
- D. Query without a vector index and let PostgreSQL scan the table

### 62. The vector index no longer fits in memory and queries spill to disk under load. What should be addressed first?

Domain: Develop AI solutions by using Azure data management services

- A. Run VACUUM and ANALYZE after bulk loads and large deletes
- B. Add a read replica and send all vector queries to it
- C. Increase storage throughput for index builds and bulk loads
- D. Scale compute and memory to fit index size and query concurrency

### 63. The same discharge-summary template is rendered identically for every request to the service. What should be added?

Domain: Develop AI solutions by using Azure data management services

- A. Set a TTL on each cached entry
- B. Cache responses in Azure Managed Redis
- C. Add a read replica and send all vector queries to it
- D. Use Azure Queue Storage for the work items

### 64. Clinician session state must survive an instance restart and a scale-in event. Where should it live?

Domain: Develop AI solutions by using Azure data management services

- A. Cache responses in Azure Managed Redis
- B. Store user session state in Managed Redis with an expiry
- C. Use a distributed lock in Redis to make processing idempotent
- D. Rely on the eviction policy and skip explicit TTLs

### 65. A document store must serve queries through the supported SDK and must avoid cross-partition fan-out for tenant reads. Which two actions should you take? Select two.

Domain: Develop AI solutions by using Azure data management services

- A. Scan every document and compute similarity in application code
- B. Index every property by using the default automatic policy
- C. Include the partition key in the query predicate
- D. Choose a high-cardinality partition key that spreads writes
- E. Query through the Cosmos DB SDK with parameterized queries

### 66. A high-concurrency intake API must bound total database connections and tolerate many short-lived clients. Which two actions should you take? Select two.

Domain: Develop AI solutions by using Azure data management services

- A. Place a connection pooler in front of PostgreSQL for many short-lived clients
- B. Use prepared statements and batch round trips
- C. Reuse a bounded connection pool instead of opening a connection per request
- D. Increase storage throughput for index builds and bulk loads
- E. Add a read replica and send all vector queries to it

### 67. Which sequence correctly prepares an audit table for embedding similarity search?

Domain: Develop AI solutions by using Azure data management services

- A. Query nearest neighbours → build the index → create the vector extension → create the table with a vector column
- B. Create the vector extension → create the table with a vector column → build the index → query nearest neighbours with a distance operator
- C. Create the table with a vector column → query nearest neighbours → create the vector extension → build the index
- D. Build the index → create the vector extension → create the table with a vector column → query nearest neighbours

### 68. Extraction tasks for one patient must be processed in order by a single worker across several competing consumers. What should be enabled?

Domain: Connect to and consume Azure services

- A. Use Service Bus sessions to keep related messages ordered
- B. Enable duplicate detection on the queue
- C. Set a maximum delivery count and handle the dead-letter path
- D. Receive with peek-lock and complete or abandon explicitly

### 69. Poison documents accumulate on a queue and must be preserved for inspection rather than lost or looped. Where should they end up?

Domain: Connect to and consume Azure services

- A. Enable duplicate detection on the queue
- B. Use prepared statements and batch round trips
- C. Receive in receive-and-delete mode for at-most-once delivery
- D. Inspect the dead-letter queue and resubmit corrected messages

### 70. A redelivered message must not create a second extraction record for the same document. What should the handler do?

Domain: Connect to and consume Azure services

- A. Receive with peek-lock and complete or abandon explicitly
- B. Receive in receive-and-delete mode for at-most-once delivery
- C. Make the handler idempotent by using a message or business key
- D. Enable duplicate detection on the queue

### 71. A new blob in the intake container must notify the orchestrator with no polling and no custom publisher for the resource event. What should be used?

Domain: Connect to and consume Azure services

- A. Stream telemetry through Azure Event Hubs
- B. Orchestrate the multi-step workflow with Durable Functions
- C. Use Azure Queue Storage for the work items
- D. Publish the state change as an Event Grid event

### 72. The intake webhook is unavailable during nightly maintenance and events must not be lost permanently. What should be configured?

Domain: Connect to and consume Azure services

- A. Stream telemetry through Azure Event Hubs
- B. Filter the Event Grid subscription by subject or event type
- C. Define a custom event schema for the topic
- D. Rely on Event Grid retries with a dead-letter destination

### 73. A document upload must start extraction automatically without an application polling loop. What should be configured?

Domain: Connect to and consume Azure services

- A. Use input and output bindings instead of hand-written SDK calls
- B. Orchestrate the multi-step workflow with Durable Functions
- C. Bind a queue or event trigger to the function
- D. Expose the endpoint through an HTTP trigger

### 74. Extraction must reach a private endpoint and must not pay cold starts during clinic hours. Which hosting plan fits?

Domain: Connect to and consume Azure services

- A. Expose the endpoint through an HTTP trigger
- B. Orchestrate the multi-step workflow with Durable Functions
- C. Host the function app on the consumption plan
- D. Host the function app on a premium plan with pre-warmed instances

### 75. Function code and its new application settings must reach production in one reviewed step. What should be used?

Domain: Connect to and consume Azure services

- A. Supply configuration through App Service application settings
- B. Expose the endpoint through an HTTP trigger
- C. Deploy the function app through a CI pipeline with app settings applied
- D. Host the function app on the consumption plan

### 76. A queue-triggered function must reach a vault without a stored secret and must stop overwhelming PostgreSQL during bursts. Which two actions should you take? Select two.

Domain: Connect to and consume Azure services

- A. Supply configuration through App Service application settings
- B. Host the function app on a premium plan with pre-warmed instances
- C. Assign a managed identity to the function app and use it for downstream calls
- D. Tune the function app concurrency and batch size
- E. Host the function app on the consumption plan

### 77. One intake event must reach both coding and billing, and billing must receive only claims. Which two features are required? Select two.

Domain: Connect to and consume Azure services

- A. Queue the work on a Service Bus queue and process it with a worker
- B. Publish to a Service Bus topic with multiple subscriptions
- C. Filter the Event Grid subscription by subject or event type
- D. Add a SQL or correlation filter to a subscription
- E. Use Azure Queue Storage for the work items

### 78. Which sequence correctly routes a custom intake event to its subscriber?

Domain: Connect to and consume Azure services

- A. Publish a custom event → deliver to the handler → evaluate the subscription filter → dead-letter undeliverable events → retry on failure
- B. Evaluate the subscription filter → publish a custom event → dead-letter undeliverable events → deliver to the handler → retry on failure
- C. Deliver to the handler → publish a custom event → evaluate the subscription filter → retry on failure → dead-letter undeliverable events
- D. Publish a custom event → evaluate the subscription filter → deliver to the handler → retry on failure → dead-letter undeliverable events

### 79. A document-intelligence key must live in a managed vault with access logging and version history. Where should it be stored?

Domain: Secure, monitor, troubleshoot Azure solutions

- A. Assign a least-privilege role to the application identity
- B. Store the secret in Azure Key Vault and read it at runtime
- C. Reference a Key Vault secret from the app configuration instead of storing it
- D. Store settings and feature flags in Azure App Configuration

### 80. Three intake services need shared settings and feature flags with one place to change them. What should be introduced?

Domain: Secure, monitor, troubleshoot Azure solutions

- A. Enable configuration refresh so changes apply without a restart
- B. Store settings and feature flags in Azure App Configuration
- C. Use App Configuration labels to separate environments
- D. Reference the Key Vault secret from an App Configuration key value

### 81. Traces must follow one document through Functions, Service Bus, and PostgreSQL instead of stopping at the first hop. What should be added?

Domain: Secure, monitor, troubleshoot Azure solutions

- A. Query the workspace with KQL to find the failing operation
- B. Instrument the service with the OpenTelemetry SDK
- C. Correlate logs with the operation or trace identifier
- D. Send telemetry to Application Insights and inspect the transaction view

### 82. The trace identifier disappears as soon as work is handed to a queued message. What must be carried across the hop?

Domain: Secure, monitor, troubleshoot Azure solutions

- A. Correlate logs with the operation or trace identifier
- B. Use head or tail sampling so trace volume stays within budget
- C. Propagate trace context across every service and queue hop
- D. Export telemetry through an OpenTelemetry collector

### 83. Only one hospital reports extraction failures, and the team needs the exact failing operation in the workspace. What should be used?

Domain: Secure, monitor, troubleshoot Azure solutions

- A. Alert on platform metrics rather than only on log queries
- B. Join the requests and dependencies tables on the operation ID
- C. Query the workspace with KQL to find the failing operation
- D. Aggregate with summarize and bin to see the failure rate over time

### 84. The intake app's identity holds owner on the whole subscription, which the security review rejects. What should change?

Domain: Secure, monitor, troubleshoot Azure solutions

- A. Federate a Kubernetes service account to a managed identity
- B. Enable purge protection and soft delete on the vault
- C. Reach the data service through a private endpoint
- D. Assign a least-privilege role to the application identity

### 85. A new extraction worker needs the document key without any stored credential in configuration. Which two components are required? Select two.

Domain: Secure, monitor, troubleshoot Azure solutions

- A. Store settings and feature flags in Azure App Configuration
- B. Authenticate with a managed identity instead of a stored key
- C. Reference a Key Vault secret from the app configuration instead of storing it
- D. Store the secret in Azure Key Vault and read it at runtime
- E. Assign a least-privilege role to the application identity

### 86. One configuration store must serve three clinics and must never hold a secret value directly. Which two features are required? Select two.

Domain: Secure, monitor, troubleshoot Azure solutions

- A. Ship the code dark behind a feature flag
- B. Reference the Key Vault secret from an App Configuration key value
- C. Enable configuration refresh so changes apply without a restart
- D. Pin the application to a specific secret version
- E. Use App Configuration labels to separate environments

### 87. Workspace queries must stay inside the cost budget while on-call is still paged when failures spike. Which two actions should you take? Select two.

Domain: Secure, monitor, troubleshoot Azure solutions

- A. Aggregate with summarize and bin to see the failure rate over time
- B. Store repeated aggregations in a materialized view or update policy
- C. Create an alert rule on the failure rate or latency metric
- D. Project only the columns needed and filter by time first
- E. Alert on platform metrics rather than only on log queries

### 88. Which sequence correctly gives a new intake service access to a rotated secret?

Domain: Secure, monitor, troubleshoot Azure solutions

- A. Rotate the secret → reference the secret from the app → store the secret in Key Vault → grant the app identity access → the app reads the new version
- B. Reference the secret from the app → rotate the secret → store the secret in Key Vault → grant the app identity access → the app reads the new version
- C. Store the secret in Key Vault → grant the app identity access → reference the secret from the app → rotate the secret → the app reads the new version
- D. Grant the app identity access → store the secret in Key Vault → rotate the secret → reference the secret from the app → the app reads the new version

---

## Case study — ClaimsFlow

The next three questions refer to this scenario. Read the full scenario before answering; case-study items are scored individually.

### 89. Inside the cluster, the storage hostname resolves to a public address and connections are refused by the firewall. What should be checked?

Domain: Develop containerized solutions on Azure

- A. Link the private DNS zone so the private endpoint name resolves
- B. Reach the data service through a private endpoint
- C. Query container logs and Kubernetes events in Log Analytics
- D. Test end-to-end connectivity from inside the container to each dependency

### 90. A corrupt document repeatedly fails indexing, and the team must inspect it later without blocking the queue. What should be used?

Domain: Connect to and consume Azure services

- A. Inspect the dead-letter queue and resubmit corrected messages
- B. Receive in receive-and-delete mode for at-most-once delivery
- C. Enable duplicate detection on the queue
- D. Set a maximum delivery count and handle the dead-letter path

### 91. The secret reference fails at runtime even though the secret exists. The app already has a managed identity. What is missing?

Domain: Secure, monitor, troubleshoot Azure solutions

- A. Assign a least-privilege role to the application identity
- B. Grant the app identity data-plane access to the vault
- C. Enable purge protection and soft delete on the vault
- D. Authenticate with a managed identity instead of a stored key

---

## Case study — Lakeview Clinic

The next three questions refer to this scenario. Read the full scenario before answering; case-study items are scored individually.

### 92. A new extraction model must receive one tenth of intake traffic while the current model keeps the rest. What should be used?

Domain: Develop containerized solutions on Azure

- A. Replicate the registry to each deployment region
- B. Create a new Container Apps revision and shift traffic between revisions
- C. Stage the change in a deployment slot and swap after verification
- D. Rely on the horizontal pod autoscaler on CPU

### 93. Intake workers must follow the number of unprocessed documents, and the queue is empty every night. What should drive replicas?

Domain: Develop containerized solutions on Azure

- A. Scale only on CPU utilization without an event scaler
- B. Scale on the Service Bus queue length with a KEDA Azure Service Bus scaler
- C. Run the batch job in Azure Container Instances
- D. Rely on the horizontal pod autoscaler on CPU

### 94. Retrieval must return only chunks from the requesting clinician's department and still fill the result count. What should the query do?

Domain: Develop AI solutions by using Azure data management services

- A. Create an IVFFlat index to save memory on a large table
- B. Retrieve nearest neighbours first and discard unauthorized rows in the application
- C. Create an HNSW index for low-latency approximate search
- D. Filter on metadata columns in the same query as the vector search

---

## Case study — MedRec intake

The next three questions refer to this scenario. Read the full scenario before answering; case-study items are scored individually.

### 95. Extracted clinical entities must be filtered by site and department and also searched by meaning in one statement. What should be used?

Domain: Develop AI solutions by using Azure data management services

- A. Store the documents in Azure Cosmos DB for NoSQL
- B. Scan every document and compute similarity in application code
- C. Store embeddings in PostgreSQL by using the pgvector extension
- D. Cache responses in Azure Managed Redis

### 96. A retrieval step must return only chunks from sites the caller is assigned to, while still returning a complete result set. Where should the scope condition be applied?

Domain: Develop AI solutions by using Azure data management services

- A. Filter on metadata columns in the same query as the vector search
- B. Create an IVFFlat index to save memory on a large table
- C. Retrieve nearest neighbours first and discard unauthorized rows in the application
- D. Create an HNSW index for low-latency approximate search

### 97. Similar prior cases must be found in single-digit milliseconds, and the case corpus fits in memory. What should be used?

Domain: Develop AI solutions by using Azure data management services

- A. Use a distributed lock in Redis to make processing idempotent
- B. Cache responses in Azure Managed Redis
- C. Store user session state in Managed Redis with an expiry
- D. Create a vector index in Managed Redis for similarity search

---

## Case study — Meridian Health

The next three questions refer to this scenario. Read the full scenario before answering; case-study items are scored individually.

### 98. Every newly extracted document must start enrichment immediately without polling the container. What should be implemented?

Domain: Develop AI solutions by using Azure data management services

- A. Publish the state change as an Event Grid event
- B. Use a lease container to coordinate change feed readers
- C. Run a change feed processor to react to new and updated items
- D. Enable duplicate detection on the queue

### 99. The billing subscriber must receive only document events whose type property is claim, while coding receives every document. What should be configured?

Domain: Connect to and consume Azure services

- A. Enable duplicate detection on the queue
- B. Add a SQL or correlation filter to a subscription
- C. Filter the Event Grid subscription by subject or event type
- D. Define a custom event schema for the topic

### 100. Latency must be split between the function itself and its SQL dependency for the same request. What should the query do?

Domain: Secure, monitor, troubleshoot Azure solutions

- A. Join the requests and dependencies tables on the operation ID
- B. Project only the columns needed and filter by time first
- C. Aggregate with summarize and bin to see the failure rate over time
- D. Store repeated aggregations in a materialized view or update policy

---

## Answer key and explanations

### Question 1 — B

Answer: Build and store versioned images in Azure Container Registry. A versioned tag on a specific digest ties the running container to a reviewable artifact. ACR keeps tagged, versioned images next to the deployment target and supports identity-based pulls. Tagging strategy and retention still need a decision. Local study-map skill 1.1 (Container Image Lifecycle in Azure Container Registry), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure container hosting documentation: https://learn.microsoft.com/en-us/azure/container-apps/

- **A:** Incorrect for this question. Geo-replication reduces cross-region pull latency and gives a local copy during a regional failure. It adds cost and replication management. Why the correct answer wins: A versioned tag on a specific digest ties the running container to a reviewable artifact.
- **B:** Correct. ACR keeps tagged, versioned images next to the deployment target and supports identity-based pulls. Tagging strategy and retention still need a decision. In this case: A versioned tag on a specific digest ties the running container to a reviewable artifact.
- **C:** Incorrect for this question. A floating tag removes the link between a deployed revision and a specific build, so rollback and audit become guesswork. Why the correct answer wins: A versioned tag on a specific digest ties the running container to a reviewable artifact.
- **D:** Incorrect for this question. ACR Tasks builds images in Azure on a commit or schedule without a local Docker host. It removes build-host drift but not image review. Why the correct answer wins: A versioned tag on a specific digest ties the running container to a reviewable artifact.

### Question 2 — A

Answer: Run image builds on demand or on a trigger with ACR Tasks. An ACR Task can build on a schedule or source trigger inside Azure, so no local host participates. ACR Tasks builds images in Azure on a commit or schedule without a local Docker host. It removes build-host drift but not image review. Local study-map skill 1.2 (Automated Image Builds with ACR Tasks), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure container hosting documentation: https://learn.microsoft.com/en-us/azure/container-apps/

- **A:** Correct. ACR Tasks builds images in Azure on a commit or schedule without a local Docker host. It removes build-host drift but not image review. In this case: An ACR Task can build on a schedule or source trigger inside Azure, so no local host participates.
- **B:** Incorrect for this question. ACR keeps tagged, versioned images next to the deployment target and supports identity-based pulls. Tagging strategy and retention still need a decision. Why the correct answer wins: An ACR Task can build on a schedule or source trigger inside Azure, so no local host participates.
- **C:** Incorrect for this question. A retention policy controls storage growth and registry clutter. It does not change which image tag a deployment references. Why the correct answer wins: An ACR Task can build on a schedule or source trigger inside Azure, so no local host participates.
- **D:** Incorrect for this question. A slot swap warms the new version before it takes production traffic and makes rollback a second swap. Slot-local settings must be marked sticky. Why the correct answer wins: An ACR Task can build on a schedule or source trigger inside Azure, so no local host participates.

### Question 3 — D

Answer: Deploy the image to Azure App Service as a web app. App Service runs a container with slots and managed platform maintenance without cluster administration. App Service runs a container with managed patching, deployment slots, and built-in authentication options. It is not a Kubernetes control plane. Local study-map skill 1.3 (Container Deployment to Azure App Service), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure container hosting documentation: https://learn.microsoft.com/en-us/azure/container-apps/

- **A:** Incorrect for this question. Container Instances starts a single container group quickly for short tasks. It has no orchestrator-level scaling or revision model. Why the correct answer wins: App Service runs a container with slots and managed platform maintenance without cluster administration.
- **B:** Incorrect for this question. Container Apps provides a managed environment, revisions, and KEDA-based scaling without cluster administration. Platform limits differ from AKS. Why the correct answer wins: App Service runs a container with slots and managed platform maintenance without cluster administration.
- **C:** Incorrect for this question. AKS gives full Kubernetes control, including custom controllers and networking. You own node pools, upgrades, and manifest hygiene. Why the correct answer wins: App Service runs a container with slots and managed platform maintenance without cluster administration.
- **D:** Correct. App Service runs a container with managed patching, deployment slots, and built-in authentication options. It is not a Kubernetes control plane. In this case: App Service runs a container with slots and managed platform maintenance without cluster administration.

### Question 4 — B

Answer: Stage the change in a deployment slot and swap after verification. A slot swap warms the new version and makes rollback a second swap. A slot swap warms the new version before it takes production traffic and makes rollback a second swap. Slot-local settings must be marked sticky. Local study-map skill 1.3 (Container Deployment to Azure App Service), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure container hosting documentation: https://learn.microsoft.com/en-us/azure/container-apps/

- **A:** Incorrect for this question. Application settings become environment variables for the container and can be swapped per slot. Sensitive values should still reference a vault. Why the correct answer wins: A slot swap warms the new version and makes rollback a second swap.
- **B:** Correct. A slot swap warms the new version before it takes production traffic and makes rollback a second swap. Slot-local settings must be marked sticky. In this case: A slot swap warms the new version and makes rollback a second swap.
- **C:** Incorrect for this question. A floating tag removes the link between a deployed revision and a specific build, so rollback and audit become guesswork. Why the correct answer wins: A slot swap warms the new version and makes rollback a second swap.
- **D:** Incorrect for this question. Revision-based traffic splitting enables canary and blue-green releases. Revision mode and scale rules must be set deliberately. Why the correct answer wins: A slot swap warms the new version and makes rollback a second swap.

### Question 5 — A

Answer: Set a minimum replica count above zero for the container app. A minimum replica count above zero keeps an instance warm so the first request avoids a cold start. A warm minimum replica removes scale-to-zero cold starts for latency-critical endpoints. It keeps paying for idle capacity. Local study-map skill 1.4 (Container Apps Deployment and Revisions), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure container hosting documentation: https://learn.microsoft.com/en-us/azure/container-apps/

- **A:** Correct. A warm minimum replica removes scale-to-zero cold starts for latency-critical endpoints. It keeps paying for idle capacity. In this case: A minimum replica count above zero keeps an instance warm so the first request avoids a cold start.
- **B:** Incorrect for this question. KEDA scalers drive replica count from queue length, lag, or other event metrics, including scale to zero. Cool-down and max replicas bound the behavior. Why the correct answer wins: A minimum replica count above zero keeps an instance warm so the first request avoids a cold start.
- **C:** Incorrect for this question. HPA adjusts replicas from resource metrics but needs metrics-server and enough node capacity. It cannot scale to zero. Why the correct answer wins: A minimum replica count above zero keeps an instance warm so the first request avoids a cold start.
- **D:** Incorrect for this question. Revision-based traffic splitting enables canary and blue-green releases. Revision mode and scale rules must be set deliberately. Why the correct answer wins: A minimum replica count above zero keeps an instance warm so the first request avoids a cold start.

### Question 6 — C

Answer: Scale the container app on an event source with a KEDA scaler. A KEDA queue scaler follows backlog depth and can scale to zero. KEDA scalers drive replica count from queue length, lag, or other event metrics, including scale to zero. Cool-down and max replicas bound the behavior. Local study-map skill 1.5 (Event-Driven Scaling with KEDA), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure container hosting documentation: https://learn.microsoft.com/en-us/azure/container-apps/

- **A:** Incorrect for this question. HPA adjusts replicas from resource metrics but needs metrics-server and enough node capacity. It cannot scale to zero. Why the correct answer wins: A KEDA queue scaler follows backlog depth and can scale to zero.
- **B:** Incorrect for this question. CPU-based scaling reacts after work is already queued and cannot scale to zero on an empty queue. It suits steady request-driven services. Why the correct answer wins: A KEDA queue scaler follows backlog depth and can scale to zero.
- **C:** Correct. KEDA scalers drive replica count from queue length, lag, or other event metrics, including scale to zero. Cool-down and max replicas bound the behavior. In this case: A KEDA queue scaler follows backlog depth and can scale to zero.
- **D:** Incorrect for this question. Container Instances starts a single container group quickly for short tasks. It has no orchestrator-level scaling or revision model. Why the correct answer wins: A KEDA queue scaler follows backlog depth and can scale to zero.

### Question 7 — D

Answer: Add readiness and liveness probes to the pod specification. Startup and liveness thresholds must accommodate real initialization time, or the container is restarted before it can become healthy. Readiness gates traffic until the app can serve it, and liveness restarts a wedged container. Wrong thresholds cause restart loops. Local study-map skill 1.6 (AKS Deployment with Manifests), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure container hosting documentation: https://learn.microsoft.com/en-us/azure/container-apps/

- **A:** Incorrect for this question. Container Instances starts a single container group quickly for short tasks. It has no orchestrator-level scaling or revision model. Why the correct answer wins: Startup and liveness thresholds must accommodate real initialization time, or the container is restarted before it can become healthy.
- **B:** Incorrect for this question. A manifest declares the desired deployment, service, and probe configuration in version control. Applying it repeatedly is idempotent. Why the correct answer wins: Startup and liveness thresholds must accommodate real initialization time, or the container is restarted before it can become healthy.
- **C:** Incorrect for this question. HPA adjusts replicas from resource metrics but needs metrics-server and enough node capacity. It cannot scale to zero. Why the correct answer wins: Startup and liveness thresholds must accommodate real initialization time, or the container is restarted before it can become healthy.
- **D:** Correct. Readiness gates traffic until the app can serve it, and liveness restarts a wedged container. Wrong thresholds cause restart loops. In this case: Startup and liveness thresholds must accommodate real initialization time, or the container is restarted before it can become healthy.

### Question 8 — B

Answer: Query container logs and Kubernetes events in Log Analytics. Container logs and platform events flow into Log Analytics where KQL can correlate them. Container Apps and AKS surface stdout logs and platform events into a workspace for KQL analysis. Verbosity and retention cost money. Local study-map skill 1.7 (Container Logs, Events, and Connectivity), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure container hosting documentation: https://learn.microsoft.com/en-us/azure/container-apps/

- **A:** Incorrect for this question. Platform logs and metrics must be routed before they can be queried or alerted on. Retention and cost follow the workspace settings. Why the correct answer wins: Container logs and platform events flow into Log Analytics where KQL can correlate them.
- **B:** Correct. Container Apps and AKS surface stdout logs and platform events into a workspace for KQL analysis. Verbosity and retention cost money. In this case: Container logs and platform events flow into Log Analytics where KQL can correlate them.
- **C:** Incorrect for this question. Reaching a dependency from the pod or replica proves DNS, egress, and firewall paths together. Host-side tests can succeed while the container path fails. Why the correct answer wins: Container logs and platform events flow into Log Analytics where KQL can correlate them.
- **D:** Incorrect for this question. Application Insights correlates requests, dependencies, and exceptions into end-to-end transactions. Sampling can hide rare failures. Why the correct answer wins: Container logs and platform events flow into Log Analytics where KQL can correlate them.

### Question 9 — A

Answer: Write the manifest → apply it to the cluster → wait for pod readiness → test ingress connectivity. The manifest is authored and applied before readiness and connectivity checks are meaningful. Readiness must pass before a connectivity test proves anything, and the manifest must exist before it is applied. Local study-map skill 1.4 (Container Apps Deployment and Revisions), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure container hosting documentation: https://learn.microsoft.com/en-us/azure/container-apps/

- **A:** Correct. Readiness must pass before a connectivity test proves anything, and the manifest must exist before it is applied. In this case: The manifest is authored and applied before readiness and connectivity checks are meaningful.
- **B:** Incorrect for this question. A manifest is authored before it is applied, and connectivity is meaningless while pods are not ready. Why the correct answer wins: The manifest is authored and applied before readiness and connectivity checks are meaningful.
- **C:** Incorrect for this question. Pods cannot become ready before the manifest is applied. Why the correct answer wins: The manifest is authored and applied before readiness and connectivity checks are meaningful.
- **D:** Incorrect for this question. Ingress cannot be tested before the workload exists in the cluster. Why the correct answer wins: The manifest is authored and applied before readiness and connectivity checks are meaningful.

### Question 10 — D, E

Answers: Create a new Container Apps revision and shift traffic between revisions; Deploy the service to Azure Container Apps. Container Apps provides a managed environment, and revisions allow traffic splitting between versions. Revision-based traffic splitting enables canary and blue-green releases. Revision mode and scale rules must be set deliberately. Container Apps provides a managed environment, revisions, and KEDA-based scaling without cluster administration. Platform limits differ from AKS. Local study-map skill 1.4 (Container Apps Deployment and Revisions), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure container hosting documentation: https://learn.microsoft.com/en-us/azure/container-apps/

- **A:** Incorrect for this question. Container Instances starts a single container group quickly for short tasks. It has no orchestrator-level scaling or revision model. Why the correct answer wins: Container Apps provides a managed environment, and revisions allow traffic splitting between versions.
- **B:** Incorrect for this question. A warm minimum replica removes scale-to-zero cold starts for latency-critical endpoints. It keeps paying for idle capacity. Why the correct answer wins: Container Apps provides a managed environment, and revisions allow traffic splitting between versions.
- **C:** Incorrect for this question. HPA adjusts replicas from resource metrics but needs metrics-server and enough node capacity. It cannot scale to zero. Why the correct answer wins: Container Apps provides a managed environment, and revisions allow traffic splitting between versions.
- **D:** Correct. Container Apps provides a managed environment, revisions, and KEDA-based scaling without cluster administration. Platform limits differ from AKS. In this case: Container Apps provides a managed environment, and revisions allow traffic splitting between versions.
- **E:** Correct. Revision-based traffic splitting enables canary and blue-green releases. Revision mode and scale rules must be set deliberately. In this case: Container Apps provides a managed environment, and revisions allow traffic splitting between versions.

### Question 11 — B, C

Answers: Apply a declarative Kubernetes manifest to the cluster; Add readiness and liveness probes to the pod specification. A declarative manifest makes the deployment reproducible, and readiness probes gate traffic. A manifest declares the desired deployment, service, and probe configuration in version control. Applying it repeatedly is idempotent. Readiness gates traffic until the app can serve it, and liveness restarts a wedged container. Wrong thresholds cause restart loops. Local study-map skill 1.6 (AKS Deployment with Manifests), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure container hosting documentation: https://learn.microsoft.com/en-us/azure/container-apps/

- **A:** Incorrect for this question. Container Instances starts a single container group quickly for short tasks. It has no orchestrator-level scaling or revision model. Why the correct answer wins: A declarative manifest makes the deployment reproducible, and readiness probes gate traffic.
- **B:** Correct. Readiness gates traffic until the app can serve it, and liveness restarts a wedged container. Wrong thresholds cause restart loops. In this case: A declarative manifest makes the deployment reproducible, and readiness probes gate traffic.
- **C:** Correct. A manifest declares the desired deployment, service, and probe configuration in version control. Applying it repeatedly is idempotent. In this case: A declarative manifest makes the deployment reproducible, and readiness probes gate traffic.
- **D:** Incorrect for this question. ACR Tasks builds images in Azure on a commit or schedule without a local Docker host. It removes build-host drift but not image review. Why the correct answer wins: A declarative manifest makes the deployment reproducible, and readiness probes gate traffic.
- **E:** Incorrect for this question. Cool-down prevents replica flapping, and a maximum replica cap bounds cost and downstream load. Both are per-rule settings. Why the correct answer wins: A declarative manifest makes the deployment reproducible, and readiness probes gate traffic.

### Question 12 — A

Answer: Store the documents in Azure Cosmos DB for NoSQL. Cosmos DB for NoSQL stores flexible documents and serves low-latency keyed reads. Cosmos DB gives globally distributed, low-latency document access with tunable consistency. Partition key and RU planning determine the cost profile. Local study-map skill 2.1 (Cosmos DB SDK Access and Queries), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Cosmos DB and PostgreSQL vector documentation: https://learn.microsoft.com/en-us/azure/cosmos-db/

- **A:** Correct. Cosmos DB gives globally distributed, low-latency document access with tunable consistency. Partition key and RU planning determine the cost profile. In this case: Cosmos DB for NoSQL stores flexible documents and serves low-latency keyed reads.
- **B:** Incorrect for this question. Queue Storage is simple and cheap for large backlogs with at-least-once delivery. It lacks topics, sessions, and scheduled messages. Why the correct answer wins: Cosmos DB for NoSQL stores flexible documents and serves low-latency keyed reads.
- **C:** Incorrect for this question. pgvector keeps vectors beside relational data, so filters and joins run in one query. Index type and parameter tuning decide latency. Why the correct answer wins: Cosmos DB for NoSQL stores flexible documents and serves low-latency keyed reads.
- **D:** Incorrect for this question. A cache absorbs repeated reads and cuts latency for hot data. Cache keys, TTLs, and invalidation must match the freshness requirement. Why the correct answer wins: Cosmos DB for NoSQL stores flexible documents and serves low-latency keyed reads.

### Question 13 — B

Answer: Enable autoscale throughput with a maximum RU limit. Autoscale follows the peak while keeping the baseline low and caps the maximum spend. Autoscale follows demand between a minimum and maximum, avoiding throttling at peak without paying for peak all day. The maximum still caps the bill. Local study-map skill 2.2 (Cosmos DB Indexing Policies and Request Units), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Cosmos DB and PostgreSQL vector documentation: https://learn.microsoft.com/en-us/azure/cosmos-db/

- **A:** Incorrect for this question. Request units measure the work a query performs, so tuning the query is often cheaper than adding throughput. Monitor normalized RU consumption. Why the correct answer wins: Autoscale follows the peak while keeping the baseline low and caps the maximum spend.
- **B:** Correct. Autoscale follows demand between a minimum and maximum, avoiding throttling at peak without paying for peak all day. The maximum still caps the bill. In this case: Autoscale follows the peak while keeping the baseline low and caps the maximum spend.
- **C:** Incorrect for this question. Indexing everything is simple and makes ad hoc queries possible, at higher write cost and storage. It is a default, not an optimization. Why the correct answer wins: Autoscale follows the peak while keeping the baseline low and caps the maximum spend.
- **D:** Incorrect for this question. Consistency trades freshness against latency, availability, and RU cost. The level is set at the account and can be relaxed per request. Why the correct answer wins: Autoscale follows the peak while keeping the baseline low and caps the maximum spend.

### Question 14 — D

Answer: Use the DiskANN vector index for large collections. DiskANN targets large vector collections with better memory efficiency than an in-memory index. DiskANN trades some recall for memory efficiency on large sets. Recall and latency should be measured on representative queries. Local study-map skill 2.4 (Cosmos DB Vector Search and Embeddings), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Cosmos DB and PostgreSQL vector documentation: https://learn.microsoft.com/en-us/azure/cosmos-db/

- **A:** Incorrect for this question. HNSW gives fast approximate nearest-neighbour queries with a larger memory footprint and slower builds. Recall is tunable at query time. Why the correct answer wins: DiskANN targets large vector collections with better memory efficiency than an in-memory index.
- **B:** Incorrect for this question. Application-side scoring works for tiny collections and tests, but it moves all data over the wire and does not scale with corpus size. Why the correct answer wins: DiskANN targets large vector collections with better memory efficiency than an in-memory index.
- **C:** Incorrect for this question. The container vector policy fixes dimensions, distance function, and index type, so a model change requires a new policy. Mismatched dimensions fail at write time. Why the correct answer wins: DiskANN targets large vector collections with better memory efficiency than an in-memory index.
- **D:** Correct. DiskANN trades some recall for memory efficiency on large sets. Recall and latency should be measured on representative queries. In this case: DiskANN targets large vector collections with better memory efficiency than an in-memory index.

### Question 15 — B

Answer: Use a lease container to coordinate change feed readers. A lease container records partition ownership so instances divide the work and resume from tokens. Leases track partition ownership so multiple processor instances share work and resume from a continuation token. Lease writes consume RUs too. Local study-map skill 2.5 (Cosmos DB Change Feed Processing), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Cosmos DB and PostgreSQL vector documentation: https://learn.microsoft.com/en-us/azure/cosmos-db/

- **A:** Incorrect for this question. The change feed delivers an ordered stream of changes per partition for downstream processing. It is not a delete feed, so deletions need a workaround. Why the correct answer wins: A lease container records partition ownership so instances divide the work and resume from tokens.
- **B:** Correct. Leases track partition ownership so multiple processor instances share work and resume from a continuation token. Lease writes consume RUs too. In this case: A lease container records partition ownership so instances divide the work and resume from tokens.
- **C:** Incorrect for this question. Autoscale follows demand between a minimum and maximum, avoiding throttling at peak without paying for peak all day. The maximum still caps the bill. Why the correct answer wins: A lease container records partition ownership so instances divide the work and resume from tokens.
- **D:** Incorrect for this question. A duplicate-detection window drops repeated sends within the window, which helps with at-least-once producers. The window is time-bounded. Why the correct answer wins: A lease container records partition ownership so instances divide the work and resume from tokens.

### Question 16 — A

Answer: Create an IVFFlat index to save memory on a large table. IVFFlat uses clustering lists and needs periodic rebuilds but has a smaller memory footprint than HNSW. IVFFlat uses clustering lists and needs periodic rebuilds as data grows, but costs less memory than HNSW. Probes trade recall for speed. Local study-map skill 2.7 (pgvector Indexing and Query Latency), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Cosmos DB and PostgreSQL vector documentation: https://learn.microsoft.com/en-us/azure/cosmos-db/

- **A:** Correct. IVFFlat uses clustering lists and needs periodic rebuilds as data grows, but costs less memory than HNSW. Probes trade recall for speed. In this case: IVFFlat uses clustering lists and needs periodic rebuilds but has a smaller memory footprint than HNSW.
- **B:** Incorrect for this question. HNSW gives fast approximate nearest-neighbour queries with a larger memory footprint and slower builds. Recall is tunable at query time. Why the correct answer wins: IVFFlat uses clustering lists and needs periodic rebuilds but has a smaller memory footprint than HNSW.
- **C:** Incorrect for this question. An exact scan is accurate but scales linearly and burns compute. It is a baseline for measuring recall, not a production strategy. Why the correct answer wins: IVFFlat uses clustering lists and needs periodic rebuilds but has a smaller memory footprint than HNSW.
- **D:** Incorrect for this question. Index builds and large sorts spill to disk when work memory is too small, stretching maintenance windows and slowing queries. Why the correct answer wins: IVFFlat uses clustering lists and needs periodic rebuilds but has a smaller memory footprint than HNSW.

### Question 17 — A

Answer: Run VACUUM and ANALYZE after bulk loads and large deletes. Dead tuples and stale statistics degrade index performance until vacuum and analyze run. Statistics and dead-tuple cleanup change plan quality and index performance. Autovacuum tuning matters for churn-heavy vector tables. Local study-map skill 2.7 (pgvector Indexing and Query Latency), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Cosmos DB and PostgreSQL vector documentation: https://learn.microsoft.com/en-us/azure/cosmos-db/

- **A:** Correct. Statistics and dead-tuple cleanup change plan quality and index performance. Autovacuum tuning matters for churn-heavy vector tables. In this case: Dead tuples and stale statistics degrade index performance until vacuum and analyze run.
- **B:** Incorrect for this question. A bounded pool amortizes connection setup and protects the server from connection storms. Pool size must match server limits. Why the correct answer wins: Dead tuples and stale statistics degrade index performance until vacuum and analyze run.
- **C:** Incorrect for this question. Index builds and large sorts spill to disk when work memory is too small, stretching maintenance windows and slowing queries. Why the correct answer wins: Dead tuples and stale statistics degrade index performance until vacuum and analyze run.
- **D:** Incorrect for this question. Index creation and bulk loads are I/O heavy, and throttled storage stretches maintenance windows. Storage limits are separate from compute. Why the correct answer wins: Dead tuples and stale statistics degrade index performance until vacuum and analyze run.

### Question 18 — A

Answer: Place a connection pooler in front of PostgreSQL for many short-lived clients. An external pooler multiplexes many short-lived clients onto a bounded set of server connections. An external pooler multiplexes server connections for serverless or highly concurrent clients. Session-level features may be unavailable in transaction mode. Local study-map skill 2.10 (PostgreSQL Connection Optimization), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Cosmos DB and PostgreSQL vector documentation: https://learn.microsoft.com/en-us/azure/cosmos-db/

- **A:** Correct. An external pooler multiplexes server connections for serverless or highly concurrent clients. Session-level features may be unavailable in transaction mode. In this case: An external pooler multiplexes many short-lived clients onto a bounded set of server connections.
- **B:** Incorrect for this question. A bounded pool amortizes connection setup and protects the server from connection storms. Pool size must match server limits. Why the correct answer wins: An external pooler multiplexes many short-lived clients onto a bounded set of server connections.
- **C:** Incorrect for this question. Prepared statements avoid repeated planning and reduce chatty network calls. They pair well with pooling but can interact with pool modes. Why the correct answer wins: An external pooler multiplexes many short-lived clients onto a bounded set of server connections.
- **D:** Incorrect for this question. A replica offloads read traffic but introduces replication lag, which is dangerous for freshly written evidence. It does not reduce index memory pressure. Why the correct answer wins: An external pooler multiplexes many short-lived clients onto a bounded set of server connections.

### Question 19 — D

Answer: Set a TTL on each cached entry. A TTL bounds staleness independently of invalidation. A TTL bounds staleness and reclaims memory without a manual sweep. Too long a TTL hides source changes; too short wastes the cache. Local study-map skill 2.11 (Azure Managed Redis Caching and Invalidation), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Cosmos DB and PostgreSQL vector documentation: https://learn.microsoft.com/en-us/azure/cosmos-db/

- **A:** Incorrect for this question. Eviction protects memory but evicts unpredictably, so a hot key can vanish before its freshness bound is reached. It is not a substitute for TTL design. Why the correct answer wins: A TTL bounds staleness independently of invalidation.
- **B:** Incorrect for this question. Write-through or explicit invalidation keeps cached answers consistent with the system of record. Without it, TTL is the only bound on staleness. Why the correct answer wins: A TTL bounds staleness independently of invalidation.
- **C:** Incorrect for this question. Flushing removes all cached content at once, causing a stampede to the origin and a latency cliff. Targeted invalidation is safer. Why the correct answer wins: A TTL bounds staleness independently of invalidation.
- **D:** Correct. A TTL bounds staleness and reclaims memory without a manual sweep. Too long a TTL hides source changes; too short wastes the cache. In this case: A TTL bounds staleness independently of invalidation.

### Question 20 — B

Answer: Use session consistency for reads within the same client session. Session consistency guarantees read-your-writes within the session without global strong consistency. Session consistency guarantees monotonic reads for one session and is the common default for user-facing apps. It does not promise global freshness. Local study-map skill 2.3 (Cosmos DB Consistency Levels), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Cosmos DB and PostgreSQL vector documentation: https://learn.microsoft.com/en-us/azure/cosmos-db/

- **A:** Incorrect for this question. Eventual consistency is the cheapest and most available option but returns possibly stale data. It fits non-critical counters, not balances. Why the correct answer wins: Session consistency guarantees read-your-writes within the session without global strong consistency.
- **B:** Correct. Session consistency guarantees monotonic reads for one session and is the common default for user-facing apps. It does not promise global freshness. In this case: Session consistency guarantees read-your-writes within the session without global strong consistency.
- **C:** Incorrect for this question. Consistency trades freshness against latency, availability, and RU cost. The level is set at the account and can be relaxed per request. Why the correct answer wins: Session consistency guarantees read-your-writes within the session without global strong consistency.
- **D:** Incorrect for this question. Strong consistency guarantees the latest committed write globally at the cost of higher latency and reduced availability during partitions. Why the correct answer wins: Session consistency guarantees read-your-writes within the session without global strong consistency.

### Question 21 — C, E

Answers: Model typed columns for filters and one vector column for the embedding; Filter on metadata columns in the same query as the vector search. Typed columns make filters efficient, and filtering inside the vector query enforces scope. Explicit types keep filters fast and make the embedding contract clear. Storing vectors as text defeats index use. Combining a WHERE filter with the distance operator keeps retrieval inside the caller's scope and improves relevance. Index the filter columns too. Local study-map skill 2.6 (PostgreSQL Connection and Schema Modeling), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Cosmos DB and PostgreSQL vector documentation: https://learn.microsoft.com/en-us/azure/cosmos-db/

- **A:** Incorrect for this question. Post-filtering can return fewer results than requested and can leak existence or counts if the filtering is careless. Push authorization into the query. Why the correct answer wins: Typed columns make filters efficient, and filtering inside the vector query enforces scope.
- **B:** Incorrect for this question. A replica offloads read traffic but introduces replication lag, which is dangerous for freshly written evidence. It does not reduce index memory pressure. Why the correct answer wins: Typed columns make filters efficient, and filtering inside the vector query enforces scope.
- **C:** Correct. Explicit types keep filters fast and make the embedding contract clear. Storing vectors as text defeats index use. In this case: Typed columns make filters efficient, and filtering inside the vector query enforces scope.
- **D:** Incorrect for this question. An exact scan is accurate but scales linearly and burns compute. It is a baseline for measuring recall, not a production strategy. Why the correct answer wins: Typed columns make filters efficient, and filtering inside the vector query enforces scope.
- **E:** Correct. Combining a WHERE filter with the distance operator keeps retrieval inside the caller's scope and improves relevance. Index the filter columns too. In this case: Typed columns make filters efficient, and filtering inside the vector query enforces scope.

### Question 22 — B, D

Answers: Scale compute and memory to fit index size and query concurrency; Increase maintenance and query memory settings for index builds and sorts. Sizing compute and memory to the index working set avoids swapping, and adequate work memory stops spills. Vector indexes are memory-hungry, so undersized compute causes swapping and slow queries. Right-size before tuning index parameters. Index builds and large sorts spill to disk when work memory is too small, stretching maintenance windows and slowing queries. Local study-map skill 2.8 (PostgreSQL Compute, Memory, and Storage Sizing), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Cosmos DB and PostgreSQL vector documentation: https://learn.microsoft.com/en-us/azure/cosmos-db/

- **A:** Incorrect for this question. An external pooler multiplexes server connections for serverless or highly concurrent clients. Session-level features may be unavailable in transaction mode. Why the correct answer wins: Sizing compute and memory to the index working set avoids swapping, and adequate work memory stops spills.
- **B:** Correct. Index builds and large sorts spill to disk when work memory is too small, stretching maintenance windows and slowing queries. In this case: Sizing compute and memory to the index working set avoids swapping, and adequate work memory stops spills.
- **C:** Incorrect for this question. IVFFlat uses clustering lists and needs periodic rebuilds as data grows, but costs less memory than HNSW. Probes trade recall for speed. Why the correct answer wins: Sizing compute and memory to the index working set avoids swapping, and adequate work memory stops spills.
- **D:** Correct. Vector indexes are memory-hungry, so undersized compute causes swapping and slow queries. Right-size before tuning index parameters. In this case: Sizing compute and memory to the index working set avoids swapping, and adequate work memory stops spills.
- **E:** Incorrect for this question. Index creation and bulk loads are I/O heavy, and throttled storage stretches maintenance windows. Storage limits are separate from compute. Why the correct answer wins: Sizing compute and memory to the index working set avoids swapping, and adequate work memory stops spills.

### Question 23 — C

Answer: Create the container with a vector policy → upsert items with embeddings → query with VectorDistance → apply metadata filters. The container and vector policy must exist before embeddings are written and queried. The vector policy fixes dimensions and index type, so it must exist before vector writes and queries. Local study-map skill 2.4 (Cosmos DB Vector Search and Embeddings), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Cosmos DB and PostgreSQL vector documentation: https://learn.microsoft.com/en-us/azure/cosmos-db/

- **A:** Incorrect for this question. A similarity query needs indexed vectors, which require the container and its policy first. Why the correct answer wins: The container and vector policy must exist before embeddings are written and queried.
- **B:** Incorrect for this question. Filtering and querying cannot precede the container and its vector data. Why the correct answer wins: The container and vector policy must exist before embeddings are written and queried.
- **C:** Correct. The vector policy fixes dimensions and index type, so it must exist before vector writes and queries. In this case: The container and vector policy must exist before embeddings are written and queried.
- **D:** Incorrect for this question. Items cannot be written before the container exists with a matching vector policy. Why the correct answer wins: The container and vector policy must exist before embeddings are written and queried.

### Question 24 — A

Answer: Queue the work on a Service Bus queue and process it with a worker. A queue with peek-lock completion gives at-least-once processing and recovery after a crash. A queue decouples producers from a single consumer group and smooths bursts. Delivery semantics depend on receive mode and completion. Local study-map skill 3.1 (Service Bus Queues and Sessions), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure messaging and Functions documentation: https://learn.microsoft.com/en-us/azure/service-bus-messaging/

- **A:** Correct. A queue decouples producers from a single consumer group and smooths bursts. Delivery semantics depend on receive mode and completion. In this case: A queue with peek-lock completion gives at-least-once processing and recovery after a crash.
- **B:** Incorrect for this question. Queue Storage is simple and cheap for large backlogs with at-least-once delivery. It lacks topics, sessions, and scheduled messages. Why the correct answer wins: A queue with peek-lock completion gives at-least-once processing and recovery after a crash.
- **C:** Incorrect for this question. Event Hubs ingests high-volume ordered streams with partitions and consumer groups. It is a streaming log, not a task queue. Why the correct answer wins: A queue with peek-lock completion gives at-least-once processing and recovery after a crash.
- **D:** Incorrect for this question. Topics fan out one message to independent subscribers, each with its own filter and dead-letter queue. Subscribers process at their own pace. Why the correct answer wins: A queue with peek-lock completion gives at-least-once processing and recovery after a crash.

### Question 25 — C

Answer: Publish to a Service Bus topic with multiple subscriptions. A topic with separate subscriptions fans out one event to independent consumers. Topics fan out one message to independent subscribers, each with its own filter and dead-letter queue. Subscribers process at their own pace. Local study-map skill 3.2 (Service Bus Topics, Subscriptions, and Filters), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure messaging and Functions documentation: https://learn.microsoft.com/en-us/azure/service-bus-messaging/

- **A:** Incorrect for this question. A queue decouples producers from a single consumer group and smooths bursts. Delivery semantics depend on receive mode and completion. Why the correct answer wins: A topic with separate subscriptions fans out one event to independent consumers.
- **B:** Incorrect for this question. A custom schema fits domain events that are not resource lifecycle notifications. Consumers must version the schema contract. Why the correct answer wins: A topic with separate subscriptions fans out one event to independent consumers.
- **C:** Correct. Topics fan out one message to independent subscribers, each with its own filter and dead-letter queue. Subscribers process at their own pace. In this case: A topic with separate subscriptions fans out one event to independent consumers.
- **D:** Incorrect for this question. Queue Storage is simple and cheap for large backlogs with at-least-once delivery. It lacks topics, sessions, and scheduled messages. Why the correct answer wins: A topic with separate subscriptions fans out one event to independent consumers.

### Question 26 — A

Answer: Increase prefetch count to reduce round trips. Prefetch batches receives to cut round trips when lock duration accommodates the batch. Prefetch reduces latency per message by batching receives, at the cost of holding more locked messages. Lock duration must cover the batch. Local study-map skill 3.2 (Service Bus Topics, Subscriptions, and Filters), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure messaging and Functions documentation: https://learn.microsoft.com/en-us/azure/service-bus-messaging/

- **A:** Correct. Prefetch reduces latency per message by batching receives, at the cost of holding more locked messages. Lock duration must cover the batch. In this case: Prefetch batches receives to cut round trips when lock duration accommodates the batch.
- **B:** Incorrect for this question. A duplicate-detection window drops repeated sends within the window, which helps with at-least-once producers. The window is time-bounded. Why the correct answer wins: Prefetch batches receives to cut round trips when lock duration accommodates the batch.
- **C:** Incorrect for this question. Sessions give ordered, exclusive processing per session ID across competing consumers. They require session-aware senders and receivers. Why the correct answer wins: Prefetch batches receives to cut round trips when lock duration accommodates the batch.
- **D:** Incorrect for this question. A delivery cap stops infinite retries of a failing message and moves it to the dead-letter queue. The cap must exceed legitimate transient retries. Why the correct answer wins: Prefetch batches receives to cut round trips when lock duration accommodates the batch.

### Question 27 — C

Answer: Subscribe to a system topic for resource events. A system topic carries resource lifecycle events such as blob creation. System topics carry Azure resource lifecycle events. Domain events that are not resource changes need a custom topic and schema. Local study-map skill 3.4 (Event Grid Filters, Custom Events, and Retries), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure messaging and Functions documentation: https://learn.microsoft.com/en-us/azure/service-bus-messaging/

- **A:** Incorrect for this question. A custom schema fits domain events that are not resource lifecycle notifications. Consumers must version the schema contract. Why the correct answer wins: A system topic carries resource lifecycle events such as blob creation.
- **B:** Incorrect for this question. Event Grid retries failed deliveries with backoff and can store undeliverable events. Handlers must still be idempotent. Why the correct answer wins: A system topic carries resource lifecycle events such as blob creation.
- **C:** Correct. System topics carry Azure resource lifecycle events. Domain events that are not resource changes need a custom topic and schema. In this case: A system topic carries resource lifecycle events such as blob creation.
- **D:** Incorrect for this question. Subject and event-type filters keep handlers focused and reduce cost. Filters are evaluated on event metadata, not payload body. Why the correct answer wins: A system topic carries resource lifecycle events such as blob creation.

### Question 28 — D

Answer: Filter the Event Grid subscription by subject or event type. A subject filter matches event metadata before delivery. Subject and event-type filters keep handlers focused and reduce cost. Filters are evaluated on event metadata, not payload body. Local study-map skill 3.4 (Event Grid Filters, Custom Events, and Retries), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure messaging and Functions documentation: https://learn.microsoft.com/en-us/azure/service-bus-messaging/

- **A:** Incorrect for this question. A custom schema fits domain events that are not resource lifecycle notifications. Consumers must version the schema contract. Why the correct answer wins: A subject filter matches event metadata before delivery.
- **B:** Incorrect for this question. Event Grid retries failed deliveries with backoff and can store undeliverable events. Handlers must still be idempotent. Why the correct answer wins: A subject filter matches event metadata before delivery.
- **C:** Incorrect for this question. Subscription filters route only matching messages to a handler, reducing wasted processing. Filter evaluation happens broker-side on message properties. Why the correct answer wins: A subject filter matches event metadata before delivery.
- **D:** Correct. Subject and event-type filters keep handlers focused and reduce cost. Filters are evaluated on event metadata, not payload body. In this case: A subject filter matches event metadata before delivery.

### Question 29 — B

Answer: Use input and output bindings instead of hand-written SDK calls. An output binding declares the write target declaratively instead of hand-written SDK calls. Bindings reduce boilerplate for common inputs and outputs and are configured declaratively. Complex operations still need the SDK. Local study-map skill 3.5 (Azure Functions Triggers and Bindings), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure messaging and Functions documentation: https://learn.microsoft.com/en-us/azure/service-bus-messaging/

- **A:** Incorrect for this question. A trigger starts the function when work arrives and handles the receive loop for you. Poison-message behavior is configured in host settings. Why the correct answer wins: An output binding declares the write target declaratively instead of hand-written SDK calls.
- **B:** Correct. Bindings reduce boilerplate for common inputs and outputs and are configured declaratively. Complex operations still need the SDK. In this case: An output binding declares the write target declaratively instead of hand-written SDK calls.
- **C:** Incorrect for this question. An HTTP trigger gives a synchronous API endpoint with route and authorization configuration. Long-running work should hand off to a queue. Why the correct answer wins: An output binding declares the write target declaratively instead of hand-written SDK calls.
- **D:** Incorrect for this question. Durable Functions provides orchestrations, activities, timers, and retries with checkpointed state. Orchestrator code must stay deterministic. Why the correct answer wins: An output binding declares the write target declaratively instead of hand-written SDK calls.

### Question 30 — C

Answer: Orchestrate the multi-step workflow with Durable Functions. Durable Functions checkpoints orchestrator progress so work resumes after a restart. Durable Functions provides orchestrations, activities, timers, and retries with checkpointed state. Orchestrator code must stay deterministic. Local study-map skill 3.6 (Function App Configuration and Deployment), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure messaging and Functions documentation: https://learn.microsoft.com/en-us/azure/service-bus-messaging/

- **A:** Incorrect for this question. An HTTP trigger gives a synchronous API endpoint with route and authorization configuration. Long-running work should hand off to a queue. Why the correct answer wins: Durable Functions checkpoints orchestrator progress so work resumes after a restart.
- **B:** Incorrect for this question. HTTP requests have platform timeout limits, so long work belongs behind a queue or orchestration with a status endpoint. Why the correct answer wins: Durable Functions checkpoints orchestrator progress so work resumes after a restart.
- **C:** Correct. Durable Functions provides orchestrations, activities, timers, and retries with checkpointed state. Orchestrator code must stay deterministic. In this case: Durable Functions checkpoints orchestrator progress so work resumes after a restart.
- **D:** Incorrect for this question. Functions runs small event-driven code without managing a host. Execution limits and cold starts depend on the hosting plan. Why the correct answer wins: Durable Functions checkpoints orchestrator progress so work resumes after a restart.

### Question 31 — A, E

Answers: Bind a queue or event trigger to the function; Use input and output bindings instead of hand-written SDK calls. A queue trigger starts execution on arrival, and an output binding performs the write. A trigger starts the function when work arrives and handles the receive loop for you. Poison-message behavior is configured in host settings. Bindings reduce boilerplate for common inputs and outputs and are configured declaratively. Complex operations still need the SDK. Local study-map skill 3.5 (Azure Functions Triggers and Bindings), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure messaging and Functions documentation: https://learn.microsoft.com/en-us/azure/service-bus-messaging/

- **A:** Correct. Bindings reduce boilerplate for common inputs and outputs and are configured declaratively. Complex operations still need the SDK. In this case: A queue trigger starts execution on arrival, and an output binding performs the write.
- **B:** Incorrect for this question. An HTTP trigger gives a synchronous API endpoint with route and authorization configuration. Long-running work should hand off to a queue. Why the correct answer wins: A queue trigger starts execution on arrival, and an output binding performs the write.
- **C:** Incorrect for this question. Durable Functions provides orchestrations, activities, timers, and retries with checkpointed state. Orchestrator code must stay deterministic. Why the correct answer wins: A queue trigger starts execution on arrival, and an output binding performs the write.
- **D:** Incorrect for this question. A premium plan reduces cold starts and supports virtual network integration and longer timeouts. It costs more than consumption. Why the correct answer wins: A queue trigger starts execution on arrival, and an output binding performs the write.
- **E:** Correct. A trigger starts the function when work arrives and handles the receive loop for you. Poison-message behavior is configured in host settings. In this case: A queue trigger starts execution on arrival, and an output binding performs the write.

### Question 32 — C, E

Answers: Host the function app on a premium plan with pre-warmed instances; Assign a managed identity to the function app and use it for downstream calls. A premium plan provides pre-warmed instances, and a managed identity removes stored credentials. A premium plan reduces cold starts and supports virtual network integration and longer timeouts. It costs more than consumption. A function app can authenticate with a managed identity, so no connection secret is needed in app settings. Local study-map skill 3.6 (Function App Configuration and Deployment), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure messaging and Functions documentation: https://learn.microsoft.com/en-us/azure/service-bus-messaging/

- **A:** Incorrect for this question. Durable Functions provides orchestrations, activities, timers, and retries with checkpointed state. Orchestrator code must stay deterministic. Why the correct answer wins: A premium plan provides pre-warmed instances, and a managed identity removes stored credentials.
- **B:** Incorrect for this question. Consumption bills per execution and scales automatically, with cold starts and a timeout ceiling. It fits spiky, short work. Why the correct answer wins: A premium plan provides pre-warmed instances, and a managed identity removes stored credentials.
- **C:** Correct. A premium plan reduces cold starts and supports virtual network integration and longer timeouts. It costs more than consumption. In this case: A premium plan provides pre-warmed instances, and a managed identity removes stored credentials.
- **D:** Incorrect for this question. An HTTP trigger gives a synchronous API endpoint with route and authorization configuration. Long-running work should hand off to a queue. Why the correct answer wins: A premium plan provides pre-warmed instances, and a managed identity removes stored credentials.
- **E:** Correct. A function app can authenticate with a managed identity, so no connection secret is needed in app settings. In this case: A premium plan provides pre-warmed instances, and a managed identity removes stored credentials.

### Question 33 — A

Answer: Publish the message → receive with peek-lock → process the work → complete the message → dead-letter after the delivery limit. Receive, process, complete, and dead-letter only after the delivery limit is exhausted. Peek-lock keeps the message until the handler succeeds, and only repeated failures should dead-letter it. Local study-map skill 3.1 (Service Bus Queues and Sessions), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure messaging and Functions documentation: https://learn.microsoft.com/en-us/azure/service-bus-messaging/

- **A:** Correct. Peek-lock keeps the message until the handler succeeds, and only repeated failures should dead-letter it. In this case: Receive, process, complete, and dead-letter only after the delivery limit is exhausted.
- **B:** Incorrect for this question. The message cannot be received before it is published, and completion must follow processing. Why the correct answer wins: Receive, process, complete, and dead-letter only after the delivery limit is exhausted.
- **C:** Incorrect for this question. Work cannot be processed before the message is published and received. Why the correct answer wins: Receive, process, complete, and dead-letter only after the delivery limit is exhausted.
- **D:** Incorrect for this question. Completing a message before processing discards the work and defeats at-least-once delivery. Why the correct answer wins: Receive, process, complete, and dead-letter only after the delivery limit is exhausted.

### Question 34 — D

Answer: Store the secret in Azure Key Vault and read it at runtime. Key Vault provides audited, access-controlled secret storage. A vault centralizes secret storage with access control and audit. Retrieval should use an identity, not a copied credential. Local study-map skill 4.1 (Key Vault Secret Storage, Rotation, and Retrieval), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Key Vault, App Configuration, and Monitor documentation: https://learn.microsoft.com/en-us/azure/azure-monitor/

- **A:** Incorrect for this question. App Configuration separates configuration from code and supports labels, feature flags, and Key Vault references. Change still needs a refresh strategy. Why the correct answer wins: Key Vault provides audited, access-controlled secret storage.
- **B:** Incorrect for this question. Application settings become environment variables for the container and can be swapped per slot. Sensitive values should still reference a vault. Why the correct answer wins: Key Vault provides audited, access-controlled secret storage.
- **C:** Incorrect for this question. Pinning a version makes a rotation invisible to the app until it is redeployed, which is useful for break-glass and dangerous for routine rotation. Why the correct answer wins: Key Vault provides audited, access-controlled secret storage.
- **D:** Correct. A vault centralizes secret storage with access control and audit. Retrieval should use an identity, not a copied credential. In this case: Key Vault provides audited, access-controlled secret storage.

### Question 35 — A

Answer: Store settings and feature flags in Azure App Configuration. App Configuration holds non-secret settings with environment labels and refresh. App Configuration separates configuration from code and supports labels, feature flags, and Key Vault references. Change still needs a refresh strategy. Local study-map skill 4.2 (App Configuration Settings and Feature Flags), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Key Vault, App Configuration, and Monitor documentation: https://learn.microsoft.com/en-us/azure/azure-monitor/

- **A:** Correct. App Configuration separates configuration from code and supports labels, feature flags, and Key Vault references. Change still needs a refresh strategy. In this case: App Configuration holds non-secret settings with environment labels and refresh.
- **B:** Incorrect for this question. A vault centralizes secret storage with access control and audit. Retrieval should use an identity, not a copied credential. Why the correct answer wins: App Configuration holds non-secret settings with environment labels and refresh.
- **C:** Incorrect for this question. Labels keep dev, test, and prod values in one store with one key schema. A misconfigured label selector silently serves the wrong values. Why the correct answer wins: App Configuration holds non-secret settings with environment labels and refresh.
- **D:** Incorrect for this question. A Key Vault reference keeps non-secret settings in App Configuration while the value stays in the vault. The app identity needs both sets of permissions. Why the correct answer wins: App Configuration holds non-secret settings with environment labels and refresh.

### Question 36 — A

Answer: Enable configuration refresh so changes apply without a restart. Configuration refresh lets a running app poll and apply changes. Sentinel-key or polling refresh lets a running app pick up new settings. Refresh intervals trade responsiveness against request volume. Local study-map skill 4.2 (App Configuration Settings and Feature Flags), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Key Vault, App Configuration, and Monitor documentation: https://learn.microsoft.com/en-us/azure/azure-monitor/

- **A:** Correct. Sentinel-key or polling refresh lets a running app pick up new settings. Refresh intervals trade responsiveness against request volume. In this case: Configuration refresh lets a running app poll and apply changes.
- **B:** Incorrect for this question. Labels keep dev, test, and prod values in one store with one key schema. A misconfigured label selector silently serves the wrong values. Why the correct answer wins: Configuration refresh lets a running app poll and apply changes.
- **C:** Incorrect for this question. Pipeline deployment keeps code and configuration versioned together and repeatable. Secrets belong in a vault reference, not in the pipeline file. Why the correct answer wins: Configuration refresh lets a running app poll and apply changes.
- **D:** Incorrect for this question. Sampling keeps telemetry cost bounded, but aggressive sampling can hide rare failures. Tail sampling can retain errors preferentially. Why the correct answer wins: Configuration refresh lets a running app poll and apply changes.

### Question 37 — C

Answer: Instrument the service with the OpenTelemetry SDK. OpenTelemetry tracing with propagation across each hop yields one end-to-end trace. OpenTelemetry emits vendor-neutral traces, metrics, and logs with context propagation. Exporters and sampling decide what reaches the backend. Local study-map skill 4.3 (Distributed Tracing with OpenTelemetry), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Key Vault, App Configuration, and Monitor documentation: https://learn.microsoft.com/en-us/azure/azure-monitor/

- **A:** Incorrect for this question. Application Insights correlates requests, dependencies, and exceptions into end-to-end transactions. Sampling can hide rare failures. Why the correct answer wins: OpenTelemetry tracing with propagation across each hop yields one end-to-end trace.
- **B:** Incorrect for this question. Platform logs and metrics must be routed before they can be queried or alerted on. Retention and cost follow the workspace settings. Why the correct answer wins: OpenTelemetry tracing with propagation across each hop yields one end-to-end trace.
- **C:** Correct. OpenTelemetry emits vendor-neutral traces, metrics, and logs with context propagation. Exporters and sampling decide what reaches the backend. In this case: OpenTelemetry tracing with propagation across each hop yields one end-to-end trace.
- **D:** Incorrect for this question. KQL filters, projects, and aggregates log and metric tables in Log Analytics. Start narrow with a time range and a request ID. Why the correct answer wins: OpenTelemetry tracing with propagation across each hop yields one end-to-end trace.

### Question 38 — C

Answer: Project only the columns needed and filter by time first. Filtering by time and projecting only needed columns reduces scanned data. Reducing columns and rows early lowers query cost and latency. Broad queries over long ranges are the usual cause of slow KQL. Local study-map skill 4.4 (KQL Queries for Logs and Metrics), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Key Vault, App Configuration, and Monitor documentation: https://learn.microsoft.com/en-us/azure/azure-monitor/

- **A:** Incorrect for this question. Precomputed results avoid recomputing expensive aggregations on every dashboard refresh. The trade-off is storage and freshness lag. Why the correct answer wins: Filtering by time and projecting only needed columns reduces scanned data.
- **B:** Incorrect for this question. Joining request and dependency telemetry shows which downstream call fails inside a slow request. Cross-workspace joins need the right scope. Why the correct answer wins: Filtering by time and projecting only needed columns reduces scanned data.
- **C:** Correct. Reducing columns and rows early lowers query cost and latency. Broad queries over long ranges are the usual cause of slow KQL. In this case: Filtering by time and projecting only needed columns reduces scanned data.
- **D:** Incorrect for this question. Time-binned aggregation reveals the shape of an incident: a step change, a ramp, or a periodic spike. Averages alone hide short outages. Why the correct answer wins: Filtering by time and projecting only needed columns reduces scanned data.

### Question 39 — C

Answer: Aggregate with summarize and bin to see the failure rate over time. Binning with summarize produces per-window percentiles. Time-binned aggregation reveals the shape of an incident: a step change, a ramp, or a periodic spike. Averages alone hide short outages. Local study-map skill 4.4 (KQL Queries for Logs and Metrics), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Key Vault, App Configuration, and Monitor documentation: https://learn.microsoft.com/en-us/azure/azure-monitor/

- **A:** Incorrect for this question. An alert turns a threshold breach into a notification or action. Thresholds need a baseline, or the alert is noise. Why the correct answer wins: Binning with summarize produces per-window percentiles.
- **B:** Incorrect for this question. Precomputed results avoid recomputing expensive aggregations on every dashboard refresh. The trade-off is storage and freshness lag. Why the correct answer wins: Binning with summarize produces per-window percentiles.
- **C:** Correct. Time-binned aggregation reveals the shape of an incident: a step change, a ramp, or a periodic spike. Averages alone hide short outages. In this case: Binning with summarize produces per-window percentiles.
- **D:** Incorrect for this question. Reducing columns and rows early lowers query cost and latency. Broad queries over long ranges are the usual cause of slow KQL. Why the correct answer wins: Binning with summarize produces per-window percentiles.

### Question 40 — C

Answer: Assign a least-privilege role to the application identity. A separate least-privilege identity or role scope should limit the app to read operations. A scoped role grants only the operations the app performs and limits blast radius. Prefer built-in roles over broad contributor grants. Local study-map skill 4.5 (Identity-Based Access for Application Services), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Key Vault, App Configuration, and Monitor documentation: https://learn.microsoft.com/en-us/azure/azure-monitor/

- **A:** Incorrect for this question. Application settings become environment variables for the container and can be swapped per slot. Sensitive values should still reference a vault. Why the correct answer wins: A separate least-privilege identity or role scope should limit the app to read operations.
- **B:** Incorrect for this question. A vault centralizes secret storage with access control and audit. Retrieval should use an identity, not a copied credential. Why the correct answer wins: A separate least-privilege identity or role scope should limit the app to read operations.
- **C:** Correct. A scoped role grants only the operations the app performs and limits blast radius. Prefer built-in roles over broad contributor grants. In this case: A separate least-privilege identity or role scope should limit the app to read operations.
- **D:** Incorrect for this question. A managed identity issues tokens from the platform, removing secret distribution from the app. Role assignment still scopes what it can reach. Why the correct answer wins: A separate least-privilege identity or role scope should limit the app to read operations.

### Question 41 — A

Answer: Publish a custom event → evaluate the subscription filter → deliver to the handler → retry on failure → dead-letter undeliverable events. Filtering precedes delivery, retries precede dead-lettering, and everything follows publication. Filtering happens before delivery, retries handle transient failures, and dead-lettering preserves what cannot be delivered. Local study-map skill 4.4 (KQL Queries for Logs and Metrics), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Key Vault, App Configuration, and Monitor documentation: https://learn.microsoft.com/en-us/azure/azure-monitor/

- **A:** Correct. Filtering happens before delivery, retries handle transient failures, and dead-lettering preserves what cannot be delivered. In this case: Filtering precedes delivery, retries precede dead-lettering, and everything follows publication.
- **B:** Incorrect for this question. Delivery cannot precede publication and filtering. Why the correct answer wins: Filtering precedes delivery, retries precede dead-lettering, and everything follows publication.
- **C:** Incorrect for this question. A filter is evaluated before delivery, and retries must occur before dead-lettering. Why the correct answer wins: Filtering precedes delivery, retries precede dead-lettering, and everything follows publication.
- **D:** Incorrect for this question. A filter cannot evaluate an event that has not been published. Why the correct answer wins: Filtering precedes delivery, retries precede dead-lettering, and everything follows publication.

### Question 42 — A, D

Answers: Make the handler idempotent by using a message or business key; Set a maximum delivery count and handle the dead-letter path. An idempotency key makes replays harmless, and a delivery limit moves persistent failures to the dead-letter queue. At-least-once delivery means duplicates will happen, so the write must tolerate replay. A stored key makes the retry safe. A delivery cap stops infinite retries of a failing message and moves it to the dead-letter queue. The cap must exceed legitimate transient retries. Local study-map skill 3.3 (Service Bus Dead-Lettering and Retries), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure messaging and Functions documentation: https://learn.microsoft.com/en-us/azure/service-bus-messaging/

- **A:** Correct. A delivery cap stops infinite retries of a failing message and moves it to the dead-letter queue. The cap must exceed legitimate transient retries. In this case: An idempotency key makes replays harmless, and a delivery limit moves persistent failures to the dead-letter queue.
- **B:** Incorrect for this question. Sessions give ordered, exclusive processing per session ID across competing consumers. They require session-aware senders and receivers. Why the correct answer wins: An idempotency key makes replays harmless, and a delivery limit moves persistent failures to the dead-letter queue.
- **C:** Incorrect for this question. Receive-and-delete removes the message on delivery, so a crash loses work silently. It suits telemetry, not payments. Why the correct answer wins: An idempotency key makes replays harmless, and a delivery limit moves persistent failures to the dead-letter queue.
- **D:** Correct. At-least-once delivery means duplicates will happen, so the write must tolerate replay. A stored key makes the retry safe. In this case: An idempotency key makes replays harmless, and a delivery limit moves persistent failures to the dead-letter queue.
- **E:** Incorrect for this question. A duplicate-detection window drops repeated sends within the window, which helps with at-least-once producers. The window is time-bounded. Why the correct answer wins: An idempotency key makes replays harmless, and a delivery limit moves persistent failures to the dead-letter queue.

### Question 43 — B, D

Answers: Instrument the service with the OpenTelemetry SDK; Propagate trace context across every service and queue hop. Context propagation connects the hops into one trace, and sampling keeps volume bounded while retaining errors when tail sampling is used. OpenTelemetry emits vendor-neutral traces, metrics, and logs with context propagation. Exporters and sampling decide what reaches the backend. Propagation stitches one trace across HTTP, messaging, and Functions so the whole path is visible. Missing propagation breaks the trace at that hop. Local study-map skill 4.3 (Distributed Tracing with OpenTelemetry), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Key Vault, App Configuration, and Monitor documentation: https://learn.microsoft.com/en-us/azure/azure-monitor/

- **A:** Incorrect for this question. Sampling keeps telemetry cost bounded, but aggressive sampling can hide rare failures. Tail sampling can retain errors preferentially. Why the correct answer wins: Context propagation connects the hops into one trace, and sampling keeps volume bounded while retaining errors when tail sampling is used.
- **B:** Correct. OpenTelemetry emits vendor-neutral traces, metrics, and logs with context propagation. Exporters and sampling decide what reaches the backend. In this case: Context propagation connects the hops into one trace, and sampling keeps volume bounded while retaining errors when tail sampling is used.
- **C:** Incorrect for this question. KQL filters, projects, and aggregates log and metric tables in Log Analytics. Start narrow with a time range and a request ID. Why the correct answer wins: Context propagation connects the hops into one trace, and sampling keeps volume bounded while retaining errors when tail sampling is used.
- **D:** Correct. Propagation stitches one trace across HTTP, messaging, and Functions so the whole path is visible. Missing propagation breaks the trace at that hop. In this case: Context propagation connects the hops into one trace, and sampling keeps volume bounded while retaining errors when tail sampling is used.
- **E:** Incorrect for this question. Platform logs and metrics must be routed before they can be queried or alerted on. Retention and cost follow the workspace settings. Why the correct answer wins: Context propagation connects the hops into one trace, and sampling keeps volume bounded while retaining errors when tail sampling is used.

### Question 44 — A

Answer: Reach the data service through a private endpoint. A private endpoint with public access disabled keeps traffic on the workload network, provided DNS resolves to the private zone. A private endpoint keeps traffic on the virtual network and removes public exposure. DNS resolution must be wired to the private zone. Local study-map skill 4.5 (Identity-Based Access for Application Services), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Key Vault, App Configuration, and Monitor documentation: https://learn.microsoft.com/en-us/azure/azure-monitor/

- **A:** Correct. A private endpoint keeps traffic on the virtual network and removes public exposure. DNS resolution must be wired to the private zone. In this case: A private endpoint with public access disabled keeps traffic on the workload network, provided DNS resolves to the private zone.
- **B:** Incorrect for this question. A managed identity issues tokens from the platform, removing secret distribution from the app. Role assignment still scopes what it can reach. Why the correct answer wins: A private endpoint with public access disabled keeps traffic on the workload network, provided DNS resolves to the private zone.
- **C:** Incorrect for this question. A scoped role grants only the operations the app performs and limits blast radius. Prefer built-in roles over broad contributor grants. Why the correct answer wins: A private endpoint with public access disabled keeps traffic on the workload network, provided DNS resolves to the private zone.
- **D:** Incorrect for this question. Platform logs and metrics must be routed before they can be queried or alerted on. Retention and cost follow the workspace settings. Why the correct answer wins: A private endpoint with public access disabled keeps traffic on the workload network, provided DNS resolves to the private zone.

### Question 45 — D

Answer: Apply an ACR retention policy to prune old untagged manifests. A retention policy prunes untagged manifests and keeps the versioned tags that deployments actually reference. A retention policy controls storage growth and registry clutter. It does not change which image tag a deployment references. Local study-map skill 1.1 (Container Image Lifecycle in Azure Container Registry), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure container hosting documentation: https://learn.microsoft.com/en-us/azure/container-apps/

- **A:** Incorrect for this question. Geo-replication reduces cross-region pull latency and gives a local copy during a regional failure. It adds cost and replication management. Why the correct answer wins: A retention policy prunes untagged manifests and keeps the versioned tags that deployments actually reference.
- **B:** Incorrect for this question. A floating tag removes the link between a deployed revision and a specific build, so rollback and audit become guesswork. Why the correct answer wins: A retention policy prunes untagged manifests and keeps the versioned tags that deployments actually reference.
- **C:** Incorrect for this question. ACR keeps tagged, versioned images next to the deployment target and supports identity-based pulls. Tagging strategy and retention still need a decision. Why the correct answer wins: A retention policy prunes untagged manifests and keeps the versioned tags that deployments actually reference.
- **D:** Correct. A retention policy controls storage growth and registry clutter. It does not change which image tag a deployment references. In this case: A retention policy prunes untagged manifests and keeps the versioned tags that deployments actually reference.

### Question 46 — C

Answer: Run image builds on demand or on a trigger with ACR Tasks. ACR Tasks can rebuild on a base-image update trigger, so patched dependencies reach every image without a local host. ACR Tasks builds images in Azure on a commit or schedule without a local Docker host. It removes build-host drift but not image review. Local study-map skill 1.2 (Automated Image Builds with ACR Tasks), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure container hosting documentation: https://learn.microsoft.com/en-us/azure/container-apps/

- **A:** Incorrect for this question. AKS gives full Kubernetes control, including custom controllers and networking. You own node pools, upgrades, and manifest hygiene. Why the correct answer wins: ACR Tasks can rebuild on a base-image update trigger, so patched dependencies reach every image without a local host.
- **B:** Incorrect for this question. Functions runs small event-driven code without managing a host. Execution limits and cold starts depend on the hosting plan. Why the correct answer wins: ACR Tasks can rebuild on a base-image update trigger, so patched dependencies reach every image without a local host.
- **C:** Correct. ACR Tasks builds images in Azure on a commit or schedule without a local Docker host. It removes build-host drift but not image review. In this case: ACR Tasks can rebuild on a base-image update trigger, so patched dependencies reach every image without a local host.
- **D:** Incorrect for this question. ACR keeps tagged, versioned images next to the deployment target and supports identity-based pulls. Tagging strategy and retention still need a decision. Why the correct answer wins: ACR Tasks can rebuild on a base-image update trigger, so patched dependencies reach every image without a local host.

### Question 47 — D

Answer: Reference a Key Vault secret from the app configuration instead of storing it. A Key Vault reference resolves the secret at runtime, so the value never lands in settings or source control. A Key Vault reference resolves at runtime so the secret is never written into application settings. The app identity still needs permission to read it. Local study-map skill 1.3 (Container Deployment to Azure App Service), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure container hosting documentation: https://learn.microsoft.com/en-us/azure/container-apps/

- **A:** Incorrect for this question. Application settings become environment variables for the container and can be swapped per slot. Sensitive values should still reference a vault. Why the correct answer wins: A Key Vault reference resolves the secret at runtime, so the value never lands in settings or source control.
- **B:** Incorrect for this question. Pinning a version makes a rotation invisible to the app until it is redeployed, which is useful for break-glass and dangerous for routine rotation. Why the correct answer wins: A Key Vault reference resolves the secret at runtime, so the value never lands in settings or source control.
- **C:** Incorrect for this question. A ConfigMap injects settings as environment variables or mounted files without rebuilding the image. Secrets still belong in Key Vault, not in a ConfigMap. Why the correct answer wins: A Key Vault reference resolves the secret at runtime, so the value never lands in settings or source control.
- **D:** Correct. A Key Vault reference resolves at runtime so the secret is never written into application settings. The app identity still needs permission to read it. In this case: A Key Vault reference resolves the secret at runtime, so the value never lands in settings or source control.

### Question 48 — A, D

Answers: Supply configuration through App Service application settings; Stage the change in a deployment slot and swap after verification. A staging slot verifies the build before the swap, and slot-scoped settings keep the environment-specific endpoint out of the swap. Application settings become environment variables for the container and can be swapped per slot. Sensitive values should still reference a vault. A slot swap warms the new version before it takes production traffic and makes rollback a second swap. Slot-local settings must be marked sticky. Local study-map skill 1.3 (Container Deployment to Azure App Service), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure container hosting documentation: https://learn.microsoft.com/en-us/azure/container-apps/

- **A:** Correct. A slot swap warms the new version before it takes production traffic and makes rollback a second swap. Slot-local settings must be marked sticky. In this case: A staging slot verifies the build before the swap, and slot-scoped settings keep the environment-specific endpoint out of the swap.
- **B:** Incorrect for this question. A manifest declares the desired deployment, service, and probe configuration in version control. Applying it repeatedly is idempotent. Why the correct answer wins: A staging slot verifies the build before the swap, and slot-scoped settings keep the environment-specific endpoint out of the swap.
- **C:** Incorrect for this question. KEDA scalers drive replica count from queue length, lag, or other event metrics, including scale to zero. Cool-down and max replicas bound the behavior. Why the correct answer wins: A staging slot verifies the build before the swap, and slot-scoped settings keep the environment-specific endpoint out of the swap.
- **D:** Correct. Application settings become environment variables for the container and can be swapped per slot. Sensitive values should still reference a vault. In this case: A staging slot verifies the build before the swap, and slot-scoped settings keep the environment-specific endpoint out of the swap.
- **E:** Incorrect for this question. Revision-based traffic splitting enables canary and blue-green releases. Revision mode and scale rules must be set deliberately. Why the correct answer wins: A staging slot verifies the build before the swap, and slot-scoped settings keep the environment-specific endpoint out of the swap.

### Question 49 — B

Answer: Deploy the service to Azure Container Apps. Container Apps provides revisions and event-driven scale-to-zero without exposing a control plane to the team. Container Apps provides a managed environment, revisions, and KEDA-based scaling without cluster administration. Platform limits differ from AKS. Local study-map skill 1.4 (Container Apps Deployment and Revisions), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure container hosting documentation: https://learn.microsoft.com/en-us/azure/container-apps/

- **A:** Incorrect for this question. AKS gives full Kubernetes control, including custom controllers and networking. You own node pools, upgrades, and manifest hygiene. Why the correct answer wins: Container Apps provides revisions and event-driven scale-to-zero without exposing a control plane to the team.
- **B:** Correct. Container Apps provides a managed environment, revisions, and KEDA-based scaling without cluster administration. Platform limits differ from AKS. In this case: Container Apps provides revisions and event-driven scale-to-zero without exposing a control plane to the team.
- **C:** Incorrect for this question. Container Instances starts a single container group quickly for short tasks. It has no orchestrator-level scaling or revision model. Why the correct answer wins: Container Apps provides revisions and event-driven scale-to-zero without exposing a control plane to the team.
- **D:** Incorrect for this question. App Service runs a container with managed patching, deployment slots, and built-in authentication options. It is not a Kubernetes control plane. Why the correct answer wins: Container Apps provides revisions and event-driven scale-to-zero without exposing a control plane to the team.

### Question 50 — A

Answer: Set a minimum replica count above zero for the container app. A minimum replica count above zero keeps a warm instance available so shift start does not pay cold-start latency. A warm minimum replica removes scale-to-zero cold starts for latency-critical endpoints. It keeps paying for idle capacity. Local study-map skill 1.5 (Event-Driven Scaling with KEDA), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure container hosting documentation: https://learn.microsoft.com/en-us/azure/container-apps/

- **A:** Correct. A warm minimum replica removes scale-to-zero cold starts for latency-critical endpoints. It keeps paying for idle capacity. In this case: A minimum replica count above zero keeps a warm instance available so shift start does not pay cold-start latency.
- **B:** Incorrect for this question. KEDA scalers drive replica count from queue length, lag, or other event metrics, including scale to zero. Cool-down and max replicas bound the behavior. Why the correct answer wins: A minimum replica count above zero keeps a warm instance available so shift start does not pay cold-start latency.
- **C:** Incorrect for this question. CPU-based scaling reacts after work is already queued and cannot scale to zero on an empty queue. It suits steady request-driven services. Why the correct answer wins: A minimum replica count above zero keeps a warm instance available so shift start does not pay cold-start latency.
- **D:** Incorrect for this question. Cool-down prevents replica flapping, and a maximum replica cap bounds cost and downstream load. Both are per-rule settings. Why the correct answer wins: A minimum replica count above zero keeps a warm instance available so shift start does not pay cold-start latency.

### Question 51 — B

Answer: Add readiness and liveness probes to the pod specification. A readiness probe withholds traffic until the application reports that the model is loaded and serving. Readiness gates traffic until the app can serve it, and liveness restarts a wedged container. Wrong thresholds cause restart loops. Local study-map skill 1.6 (AKS Deployment with Manifests), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure container hosting documentation: https://learn.microsoft.com/en-us/azure/container-apps/

- **A:** Incorrect for this question. Container Apps and AKS surface stdout logs and platform events into a workspace for KQL analysis. Verbosity and retention cost money. Why the correct answer wins: A readiness probe withholds traffic until the application reports that the model is loaded and serving.
- **B:** Correct. Readiness gates traffic until the app can serve it, and liveness restarts a wedged container. Wrong thresholds cause restart loops. In this case: A readiness probe withholds traffic until the application reports that the model is loaded and serving.
- **C:** Incorrect for this question. Container Instances starts a single container group quickly for short tasks. It has no orchestrator-level scaling or revision model. Why the correct answer wins: A readiness probe withholds traffic until the application reports that the model is loaded and serving.
- **D:** Incorrect for this question. HPA adjusts replicas from resource metrics but needs metrics-server and enough node capacity. It cannot scale to zero. Why the correct answer wins: A readiness probe withholds traffic until the application reports that the model is loaded and serving.

### Question 52 — B

Answer: Test end-to-end connectivity from inside the container to each dependency. Testing the path from inside the pod proves DNS, egress, and policy behaviour that host-side tests cannot reproduce. Reaching a dependency from the pod or replica proves DNS, egress, and firewall paths together. Host-side tests can succeed while the container path fails. Local study-map skill 1.7 (Container Logs, Events, and Connectivity), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure container hosting documentation: https://learn.microsoft.com/en-us/azure/container-apps/

- **A:** Incorrect for this question. Readiness gates traffic until the app can serve it, and liveness restarts a wedged container. Wrong thresholds cause restart loops. Why the correct answer wins: Testing the path from inside the pod proves DNS, egress, and policy behaviour that host-side tests cannot reproduce.
- **B:** Correct. Reaching a dependency from the pod or replica proves DNS, egress, and firewall paths together. Host-side tests can succeed while the container path fails. In this case: Testing the path from inside the pod proves DNS, egress, and policy behaviour that host-side tests cannot reproduce.
- **C:** Incorrect for this question. Platform logs and metrics must be routed before they can be queried or alerted on. Retention and cost follow the workspace settings. Why the correct answer wins: Testing the path from inside the pod proves DNS, egress, and policy behaviour that host-side tests cannot reproduce.
- **D:** Incorrect for this question. Time-binned aggregation reveals the shape of an incident: a step change, a ramp, or a periodic spike. Averages alone hide short outages. Why the correct answer wins: Testing the path from inside the pod proves DNS, egress, and policy behaviour that host-side tests cannot reproduce.

### Question 53 — D

Answer: Deploy the image to Azure App Service as a web app. App Service runs one container per app with managed patching and slots, and it does not expose a Kubernetes control plane. App Service runs a container with managed patching, deployment slots, and built-in authentication options. It is not a Kubernetes control plane. Local study-map skill 1.3 (Container Deployment to Azure App Service), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure container hosting documentation: https://learn.microsoft.com/en-us/azure/container-apps/

- **A:** Incorrect for this question. Container Instances starts a single container group quickly for short tasks. It has no orchestrator-level scaling or revision model. Why the correct answer wins: App Service runs one container per app with managed patching and slots, and it does not expose a Kubernetes control plane.
- **B:** Incorrect for this question. Container Apps provides a managed environment, revisions, and KEDA-based scaling without cluster administration. Platform limits differ from AKS. Why the correct answer wins: App Service runs one container per app with managed patching and slots, and it does not expose a Kubernetes control plane.
- **C:** Incorrect for this question. AKS gives full Kubernetes control, including custom controllers and networking. You own node pools, upgrades, and manifest hygiene. Why the correct answer wins: App Service runs one container per app with managed patching and slots, and it does not expose a Kubernetes control plane.
- **D:** Correct. App Service runs a container with managed patching, deployment slots, and built-in authentication options. It is not a Kubernetes control plane. In this case: App Service runs one container per app with managed patching and slots, and it does not expose a Kubernetes control plane.

### Question 54 — D

Answer: Build and push the image → deploy a new revision → shift a small traffic percentage → check metrics → promote or roll back. Image build and push precede the revision, traffic shift follows the revision, and promotion follows observed metrics. A canary revision accepts a small share of traffic so metrics decide promotion rather than optimism. Local study-map skill 1.4 (Container Apps Deployment and Revisions), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure container hosting documentation: https://learn.microsoft.com/en-us/azure/container-apps/

- **A:** Incorrect for this question. Full traffic cannot move to a revision that does not exist yet, and the image must exist before the revision. Why the correct answer wins: Image build and push precede the revision, traffic shift follows the revision, and promotion follows observed metrics.
- **B:** Incorrect for this question. Metrics cannot be checked before the revision serves traffic. Why the correct answer wins: Image build and push precede the revision, traffic shift follows the revision, and promotion follows observed metrics.
- **C:** Incorrect for this question. Building after traffic is shifted means the running revision has no reviewed artifact behind it. Why the correct answer wins: Image build and push precede the revision, traffic shift follows the revision, and promotion follows observed metrics.
- **D:** Correct. A canary revision accepts a small share of traffic so metrics decide promotion rather than optimism. In this case: Image build and push precede the revision, traffic shift follows the revision, and promotion follows observed metrics.

### Question 55 — C

Answer: Store the documents in Azure Cosmos DB for NoSQL. Cosmos DB for NoSQL keeps JSON documents with a tenant partition key and serves point reads from a single partition. Cosmos DB gives globally distributed, low-latency document access with tunable consistency. Partition key and RU planning determine the cost profile. Local study-map skill 2.1 (Cosmos DB SDK Access and Queries), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Cosmos DB and PostgreSQL vector documentation: https://learn.microsoft.com/en-us/azure/cosmos-db/

- **A:** Incorrect for this question. A point or single-partition query avoids fan-out across partitions. Cross-partition queries consume more RUs and add latency. Why the correct answer wins: Cosmos DB for NoSQL keeps JSON documents with a tenant partition key and serves point reads from a single partition.
- **B:** Incorrect for this question. pgvector keeps vectors beside relational data, so filters and joins run in one query. Index type and parameter tuning decide latency. Why the correct answer wins: Cosmos DB for NoSQL keeps JSON documents with a tenant partition key and serves point reads from a single partition.
- **C:** Correct. Cosmos DB gives globally distributed, low-latency document access with tunable consistency. Partition key and RU planning determine the cost profile. In this case: Cosmos DB for NoSQL keeps JSON documents with a tenant partition key and serves point reads from a single partition.
- **D:** Incorrect for this question. Queue Storage is simple and cheap for large backlogs with at-least-once delivery. It lacks topics, sessions, and scheduled messages. Why the correct answer wins: Cosmos DB for NoSQL keeps JSON documents with a tenant partition key and serves point reads from a single partition.

### Question 56 — D

Answer: Enable autoscale throughput with a maximum RU limit. Autoscale throughput raises the ceiling during bursts and lowers it again when demand falls, instead of paying for peak all day. Autoscale follows demand between a minimum and maximum, avoiding throttling at peak without paying for peak all day. The maximum still caps the bill. Local study-map skill 2.2 (Cosmos DB Indexing Policies and Request Units), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Cosmos DB and PostgreSQL vector documentation: https://learn.microsoft.com/en-us/azure/cosmos-db/

- **A:** Incorrect for this question. Indexing everything is simple and makes ad hoc queries possible, at higher write cost and storage. It is a default, not an optimization. Why the correct answer wins: Autoscale throughput raises the ceiling during bursts and lowers it again when demand falls, instead of paying for peak all day.
- **B:** Incorrect for this question. Request units measure the work a query performs, so tuning the query is often cheaper than adding throughput. Monitor normalized RU consumption. Why the correct answer wins: Autoscale throughput raises the ceiling during bursts and lowers it again when demand falls, instead of paying for peak all day.
- **C:** Incorrect for this question. Selective indexing cuts write RU charge and storage for unused paths. Excluded paths cannot be filtered efficiently later. Why the correct answer wins: Autoscale throughput raises the ceiling during bursts and lowers it again when demand falls, instead of paying for peak all day.
- **D:** Correct. Autoscale follows demand between a minimum and maximum, avoiding throttling at peak without paying for peak all day. The maximum still caps the bill. In this case: Autoscale throughput raises the ceiling during bursts and lowers it again when demand falls, instead of paying for peak all day.

### Question 57 — A

Answer: Restrict the indexing policy to the paths the queries use. Restricting the indexing policy to the queried paths removes write charge and storage for properties nobody filters on. Selective indexing cuts write RU charge and storage for unused paths. Excluded paths cannot be filtered efficiently later. Local study-map skill 2.2 (Cosmos DB Indexing Policies and Request Units), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Cosmos DB and PostgreSQL vector documentation: https://learn.microsoft.com/en-us/azure/cosmos-db/

- **A:** Correct. Selective indexing cuts write RU charge and storage for unused paths. Excluded paths cannot be filtered efficiently later. In this case: Restricting the indexing policy to the queried paths removes write charge and storage for properties nobody filters on.
- **B:** Incorrect for this question. Autoscale follows demand between a minimum and maximum, avoiding throttling at peak without paying for peak all day. The maximum still caps the bill. Why the correct answer wins: Restricting the indexing policy to the queried paths removes write charge and storage for properties nobody filters on.
- **C:** Incorrect for this question. Indexing everything is simple and makes ad hoc queries possible, at higher write cost and storage. It is a default, not an optimization. Why the correct answer wins: Restricting the indexing policy to the queried paths removes write charge and storage for properties nobody filters on.
- **D:** Incorrect for this question. A composite index lets a query filter and order on several paths without a runtime sort. It adds write cost for exactly those paths. Why the correct answer wins: Restricting the indexing policy to the queried paths removes write charge and storage for properties nobody filters on.

### Question 58 — B

Answer: Use eventual consistency to minimize read cost. Eventual consistency returns the cheapest reads when the consumer can accept stale values. Eventual consistency is the cheapest and most available option but returns possibly stale data. It fits non-critical counters, not balances. Local study-map skill 2.3 (Cosmos DB Consistency Levels), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Cosmos DB and PostgreSQL vector documentation: https://learn.microsoft.com/en-us/azure/cosmos-db/

- **A:** Incorrect for this question. Session consistency guarantees monotonic reads for one session and is the common default for user-facing apps. It does not promise global freshness. Why the correct answer wins: Eventual consistency returns the cheapest reads when the consumer can accept stale values.
- **B:** Correct. Eventual consistency is the cheapest and most available option but returns possibly stale data. It fits non-critical counters, not balances. In this case: Eventual consistency returns the cheapest reads when the consumer can accept stale values.
- **C:** Incorrect for this question. Consistency trades freshness against latency, availability, and RU cost. The level is set at the account and can be relaxed per request. Why the correct answer wins: Eventual consistency returns the cheapest reads when the consumer can accept stale values.
- **D:** Incorrect for this question. Strong consistency guarantees the latest committed write globally at the cost of higher latency and reduced availability during partitions. Why the correct answer wins: Eventual consistency returns the cheapest reads when the consumer can accept stale values.

### Question 59 — C

Answer: Store embeddings in a vector property and query with VectorDistance. A vector property on the same document keeps embeddings and metadata together, so filters and similarity run in one query. Cosmos DB for NoSQL supports vector properties and a distance function for similarity search in the same document store. Dimensions and index type must match the model. Local study-map skill 2.4 (Cosmos DB Vector Search and Embeddings), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Cosmos DB and PostgreSQL vector documentation: https://learn.microsoft.com/en-us/azure/cosmos-db/

- **A:** Incorrect for this question. Application-side scoring works for tiny collections and tests, but it moves all data over the wire and does not scale with corpus size. Why the correct answer wins: A vector property on the same document keeps embeddings and metadata together, so filters and similarity run in one query.
- **B:** Incorrect for this question. DiskANN trades some recall for memory efficiency on large sets. Recall and latency should be measured on representative queries. Why the correct answer wins: A vector property on the same document keeps embeddings and metadata together, so filters and similarity run in one query.
- **C:** Correct. Cosmos DB for NoSQL supports vector properties and a distance function for similarity search in the same document store. Dimensions and index type must match the model. In this case: A vector property on the same document keeps embeddings and metadata together, so filters and similarity run in one query.
- **D:** Incorrect for this question. pgvector keeps vectors beside relational data, so filters and joins run in one query. Index type and parameter tuning decide latency. Why the correct answer wins: A vector property on the same document keeps embeddings and metadata together, so filters and similarity run in one query.

### Question 60 — A

Answer: Model typed columns for filters and one vector column for the embedding. Typed columns for the filter fields beside one vector column keep predicates indexable and the embedding contract explicit. Explicit types keep filters fast and make the embedding contract clear. Storing vectors as text defeats index use. Local study-map skill 2.6 (PostgreSQL Connection and Schema Modeling), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Cosmos DB and PostgreSQL vector documentation: https://learn.microsoft.com/en-us/azure/cosmos-db/

- **A:** Correct. Explicit types keep filters fast and make the embedding contract clear. Storing vectors as text defeats index use. In this case: Typed columns for the filter fields beside one vector column keep predicates indexable and the embedding contract explicit.
- **B:** Incorrect for this question. A replica offloads read traffic but introduces replication lag, which is dangerous for freshly written evidence. It does not reduce index memory pressure. Why the correct answer wins: Typed columns for the filter fields beside one vector column keep predicates indexable and the embedding contract explicit.
- **C:** Incorrect for this question. Index creation and bulk loads are I/O heavy, and throttled storage stretches maintenance windows. Storage limits are separate from compute. Why the correct answer wins: Typed columns for the filter fields beside one vector column keep predicates indexable and the embedding contract explicit.
- **D:** Incorrect for this question. Vector indexes are memory-hungry, so undersized compute causes swapping and slow queries. Right-size before tuning index parameters. Why the correct answer wins: Typed columns for the filter fields beside one vector column keep predicates indexable and the embedding contract explicit.

### Question 61 — C

Answer: Create an HNSW index for low-latency approximate search. HNSW gives low-latency approximate search and allows recall to be tuned at query time. HNSW gives fast approximate nearest-neighbour queries with a larger memory footprint and slower builds. Recall is tunable at query time. Local study-map skill 2.7 (pgvector Indexing and Query Latency), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Cosmos DB and PostgreSQL vector documentation: https://learn.microsoft.com/en-us/azure/cosmos-db/

- **A:** Incorrect for this question. IVFFlat uses clustering lists and needs periodic rebuilds as data grows, but costs less memory than HNSW. Probes trade recall for speed. Why the correct answer wins: HNSW gives low-latency approximate search and allows recall to be tuned at query time.
- **B:** Incorrect for this question. An external pooler multiplexes server connections for serverless or highly concurrent clients. Session-level features may be unavailable in transaction mode. Why the correct answer wins: HNSW gives low-latency approximate search and allows recall to be tuned at query time.
- **C:** Correct. HNSW gives fast approximate nearest-neighbour queries with a larger memory footprint and slower builds. Recall is tunable at query time. In this case: HNSW gives low-latency approximate search and allows recall to be tuned at query time.
- **D:** Incorrect for this question. An exact scan is accurate but scales linearly and burns compute. It is a baseline for measuring recall, not a production strategy. Why the correct answer wins: HNSW gives low-latency approximate search and allows recall to be tuned at query time.

### Question 62 — D

Answer: Scale compute and memory to fit index size and query concurrency. A vector index whose working set exceeds memory forces disk reads, so compute and memory must be sized to the index. Vector indexes are memory-hungry, so undersized compute causes swapping and slow queries. Right-size before tuning index parameters. Local study-map skill 2.8 (PostgreSQL Compute, Memory, and Storage Sizing), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Cosmos DB and PostgreSQL vector documentation: https://learn.microsoft.com/en-us/azure/cosmos-db/

- **A:** Incorrect for this question. Statistics and dead-tuple cleanup change plan quality and index performance. Autovacuum tuning matters for churn-heavy vector tables. Why the correct answer wins: A vector index whose working set exceeds memory forces disk reads, so compute and memory must be sized to the index.
- **B:** Incorrect for this question. A replica offloads read traffic but introduces replication lag, which is dangerous for freshly written evidence. It does not reduce index memory pressure. Why the correct answer wins: A vector index whose working set exceeds memory forces disk reads, so compute and memory must be sized to the index.
- **C:** Incorrect for this question. Index creation and bulk loads are I/O heavy, and throttled storage stretches maintenance windows. Storage limits are separate from compute. Why the correct answer wins: A vector index whose working set exceeds memory forces disk reads, so compute and memory must be sized to the index.
- **D:** Correct. Vector indexes are memory-hungry, so undersized compute causes swapping and slow queries. Right-size before tuning index parameters. In this case: A vector index whose working set exceeds memory forces disk reads, so compute and memory must be sized to the index.

### Question 63 — B

Answer: Cache responses in Azure Managed Redis. Caching the rendered template in Redis stops the service from repeating the same work for every caller. A cache absorbs repeated reads and cuts latency for hot data. Cache keys, TTLs, and invalidation must match the freshness requirement. Local study-map skill 2.11 (Azure Managed Redis Caching and Invalidation), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Cosmos DB and PostgreSQL vector documentation: https://learn.microsoft.com/en-us/azure/cosmos-db/

- **A:** Incorrect for this question. A TTL bounds staleness and reclaims memory without a manual sweep. Too long a TTL hides source changes; too short wastes the cache. Why the correct answer wins: Caching the rendered template in Redis stops the service from repeating the same work for every caller.
- **B:** Correct. A cache absorbs repeated reads and cuts latency for hot data. Cache keys, TTLs, and invalidation must match the freshness requirement. In this case: Caching the rendered template in Redis stops the service from repeating the same work for every caller.
- **C:** Incorrect for this question. A replica offloads read traffic but introduces replication lag, which is dangerous for freshly written evidence. It does not reduce index memory pressure. Why the correct answer wins: Caching the rendered template in Redis stops the service from repeating the same work for every caller.
- **D:** Incorrect for this question. Queue Storage is simple and cheap for large backlogs with at-least-once delivery. It lacks topics, sessions, and scheduled messages. Why the correct answer wins: Caching the rendered template in Redis stops the service from repeating the same work for every caller.

### Question 64 — B

Answer: Store user session state in Managed Redis with an expiry. Managed Redis with an expiry keeps session state outside the process, so restarts and scale-in do not lose it. Session storage in Redis survives instance restarts and supports distributed instances. Sessions must be scoped and expiring. Local study-map skill 2.12 (Azure Managed Redis Vector Indexing), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Cosmos DB and PostgreSQL vector documentation: https://learn.microsoft.com/en-us/azure/cosmos-db/

- **A:** Incorrect for this question. A cache absorbs repeated reads and cuts latency for hot data. Cache keys, TTLs, and invalidation must match the freshness requirement. Why the correct answer wins: Managed Redis with an expiry keeps session state outside the process, so restarts and scale-in do not lose it.
- **B:** Correct. Session storage in Redis survives instance restarts and supports distributed instances. Sessions must be scoped and expiring. In this case: Managed Redis with an expiry keeps session state outside the process, so restarts and scale-in do not lose it.
- **C:** Incorrect for this question. A lock can serialize work across instances, but correctness under retries still needs idempotency keys in the data store. Locks expire and can be lost. Why the correct answer wins: Managed Redis with an expiry keeps session state outside the process, so restarts and scale-in do not lose it.
- **D:** Incorrect for this question. Eviction protects memory but evicts unpredictably, so a hot key can vanish before its freshness bound is reached. It is not a substitute for TTL design. Why the correct answer wins: Managed Redis with an expiry keeps session state outside the process, so restarts and scale-in do not lose it.

### Question 65 — D, E

Answers: Query through the Cosmos DB SDK with parameterized queries; Choose a high-cardinality partition key that spreads writes. SDK parameterized queries stay on the supported path, and a high-cardinality tenant key keeps reads inside one partition. SDK queries keep the client on the supported data plane and parameterization avoids injection and plan churn. Cross-partition queries still cost more. A good partition key distributes storage and throughput and keeps common queries single-partition. Low cardinality creates hot partitions. Local study-map skill 2.1 (Cosmos DB SDK Access and Queries), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Cosmos DB and PostgreSQL vector documentation: https://learn.microsoft.com/en-us/azure/cosmos-db/

- **A:** Incorrect for this question. Application-side scoring works for tiny collections and tests, but it moves all data over the wire and does not scale with corpus size. Why the correct answer wins: SDK parameterized queries stay on the supported path, and a high-cardinality tenant key keeps reads inside one partition.
- **B:** Incorrect for this question. Indexing everything is simple and makes ad hoc queries possible, at higher write cost and storage. It is a default, not an optimization. Why the correct answer wins: SDK parameterized queries stay on the supported path, and a high-cardinality tenant key keeps reads inside one partition.
- **C:** Incorrect for this question. A point or single-partition query avoids fan-out across partitions. Cross-partition queries consume more RUs and add latency. Why the correct answer wins: SDK parameterized queries stay on the supported path, and a high-cardinality tenant key keeps reads inside one partition.
- **D:** Correct. A good partition key distributes storage and throughput and keeps common queries single-partition. Low cardinality creates hot partitions. In this case: SDK parameterized queries stay on the supported path, and a high-cardinality tenant key keeps reads inside one partition.
- **E:** Correct. SDK queries keep the client on the supported data plane and parameterization avoids injection and plan churn. Cross-partition queries still cost more. In this case: SDK parameterized queries stay on the supported path, and a high-cardinality tenant key keeps reads inside one partition.

### Question 66 — A, C

Answers: Reuse a bounded connection pool instead of opening a connection per request; Place a connection pooler in front of PostgreSQL for many short-lived clients. A bounded pool caps connections per instance, and an external pooler multiplexes short-lived clients onto fewer sessions. A bounded pool amortizes connection setup and protects the server from connection storms. Pool size must match server limits. An external pooler multiplexes server connections for serverless or highly concurrent clients. Session-level features may be unavailable in transaction mode. Local study-map skill 2.10 (PostgreSQL Connection Optimization), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Cosmos DB and PostgreSQL vector documentation: https://learn.microsoft.com/en-us/azure/cosmos-db/

- **A:** Correct. An external pooler multiplexes server connections for serverless or highly concurrent clients. Session-level features may be unavailable in transaction mode. In this case: A bounded pool caps connections per instance, and an external pooler multiplexes short-lived clients onto fewer sessions.
- **B:** Incorrect for this question. Prepared statements avoid repeated planning and reduce chatty network calls. They pair well with pooling but can interact with pool modes. Why the correct answer wins: A bounded pool caps connections per instance, and an external pooler multiplexes short-lived clients onto fewer sessions.
- **C:** Correct. A bounded pool amortizes connection setup and protects the server from connection storms. Pool size must match server limits. In this case: A bounded pool caps connections per instance, and an external pooler multiplexes short-lived clients onto fewer sessions.
- **D:** Incorrect for this question. Index creation and bulk loads are I/O heavy, and throttled storage stretches maintenance windows. Storage limits are separate from compute. Why the correct answer wins: A bounded pool caps connections per instance, and an external pooler multiplexes short-lived clients onto fewer sessions.
- **E:** Incorrect for this question. A replica offloads read traffic but introduces replication lag, which is dangerous for freshly written evidence. It does not reduce index memory pressure. Why the correct answer wins: A bounded pool caps connections per instance, and an external pooler multiplexes short-lived clients onto fewer sessions.

### Question 67 — B

Answer: Create the vector extension → create the table with a vector column → build the index → query nearest neighbours with a distance operator. Extension and table must exist before the index, and the index before efficient nearest-neighbour queries. The extension and typed column must exist before an index can be built, and the index before the query is efficient. Local study-map skill 2.7 (pgvector Indexing and Query Latency), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Cosmos DB and PostgreSQL vector documentation: https://learn.microsoft.com/en-us/azure/cosmos-db/

- **A:** Incorrect for this question. Querying before the schema exists cannot succeed, and the index cannot precede the table. Why the correct answer wins: Extension and table must exist before the index, and the index before efficient nearest-neighbour queries.
- **B:** Correct. The extension and typed column must exist before an index can be built, and the index before the query is efficient. In this case: Extension and table must exist before the index, and the index before efficient nearest-neighbour queries.
- **C:** Incorrect for this question. The extension is required for the vector type, and the query should follow index creation for usable latency. Why the correct answer wins: Extension and table must exist before the index, and the index before efficient nearest-neighbour queries.
- **D:** Incorrect for this question. An index cannot be built before the extension and the table exist. Why the correct answer wins: Extension and table must exist before the index, and the index before efficient nearest-neighbour queries.

### Question 68 — A

Answer: Use Service Bus sessions to keep related messages ordered. Sessions give exclusive, ordered processing per session identifier across competing consumers. Sessions give ordered, exclusive processing per session ID across competing consumers. They require session-aware senders and receivers. Local study-map skill 3.1 (Service Bus Queues and Sessions), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure messaging and Functions documentation: https://learn.microsoft.com/en-us/azure/service-bus-messaging/

- **A:** Correct. Sessions give ordered, exclusive processing per session ID across competing consumers. They require session-aware senders and receivers. In this case: Sessions give exclusive, ordered processing per session identifier across competing consumers.
- **B:** Incorrect for this question. A duplicate-detection window drops repeated sends within the window, which helps with at-least-once producers. The window is time-bounded. Why the correct answer wins: Sessions give exclusive, ordered processing per session identifier across competing consumers.
- **C:** Incorrect for this question. A delivery cap stops infinite retries of a failing message and moves it to the dead-letter queue. The cap must exceed legitimate transient retries. Why the correct answer wins: Sessions give exclusive, ordered processing per session identifier across competing consumers.
- **D:** Incorrect for this question. Peek-lock keeps the message locked until the handler completes it, giving at-least-once processing with retry. Lock duration must exceed processing time. Why the correct answer wins: Sessions give exclusive, ordered processing per session identifier across competing consumers.

### Question 69 — D

Answer: Inspect the dead-letter queue and resubmit corrected messages. The dead-letter queue holds messages that exhausted delivery attempts so they can be inspected and resubmitted. Dead-lettering preserves poison messages for diagnosis instead of losing them. Resubmission needs a fix and an idempotent handler. Local study-map skill 3.3 (Service Bus Dead-Lettering and Retries), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure messaging and Functions documentation: https://learn.microsoft.com/en-us/azure/service-bus-messaging/

- **A:** Incorrect for this question. A duplicate-detection window drops repeated sends within the window, which helps with at-least-once producers. The window is time-bounded. Why the correct answer wins: The dead-letter queue holds messages that exhausted delivery attempts so they can be inspected and resubmitted.
- **B:** Incorrect for this question. Prepared statements avoid repeated planning and reduce chatty network calls. They pair well with pooling but can interact with pool modes. Why the correct answer wins: The dead-letter queue holds messages that exhausted delivery attempts so they can be inspected and resubmitted.
- **C:** Incorrect for this question. Receive-and-delete removes the message on delivery, so a crash loses work silently. It suits telemetry, not payments. Why the correct answer wins: The dead-letter queue holds messages that exhausted delivery attempts so they can be inspected and resubmitted.
- **D:** Correct. Dead-lettering preserves poison messages for diagnosis instead of losing them. Resubmission needs a fix and an idempotent handler. In this case: The dead-letter queue holds messages that exhausted delivery attempts so they can be inspected and resubmitted.

### Question 70 — C

Answer: Make the handler idempotent by using a message or business key. An idempotency key in the data store turns a replayed message into a no-op instead of a duplicate write. At-least-once delivery means duplicates will happen, so the write must tolerate replay. A stored key makes the retry safe. Local study-map skill 3.3 (Service Bus Dead-Lettering and Retries), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure messaging and Functions documentation: https://learn.microsoft.com/en-us/azure/service-bus-messaging/

- **A:** Incorrect for this question. Peek-lock keeps the message locked until the handler completes it, giving at-least-once processing with retry. Lock duration must exceed processing time. Why the correct answer wins: An idempotency key in the data store turns a replayed message into a no-op instead of a duplicate write.
- **B:** Incorrect for this question. Receive-and-delete removes the message on delivery, so a crash loses work silently. It suits telemetry, not payments. Why the correct answer wins: An idempotency key in the data store turns a replayed message into a no-op instead of a duplicate write.
- **C:** Correct. At-least-once delivery means duplicates will happen, so the write must tolerate replay. A stored key makes the retry safe. In this case: An idempotency key in the data store turns a replayed message into a no-op instead of a duplicate write.
- **D:** Incorrect for this question. A duplicate-detection window drops repeated sends within the window, which helps with at-least-once producers. The window is time-bounded. Why the correct answer wins: An idempotency key in the data store turns a replayed message into a no-op instead of a duplicate write.

### Question 71 — D

Answer: Publish the state change as an Event Grid event. An Event Grid subscription on the storage system topic pushes blob-created events as soon as the resource changes. Event Grid delivers discrete notifications to subscribers with retries and filtering. It carries events, not large payloads or ordered streams. Local study-map skill 3.4 (Event Grid Filters, Custom Events, and Retries), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure messaging and Functions documentation: https://learn.microsoft.com/en-us/azure/service-bus-messaging/

- **A:** Incorrect for this question. Event Hubs ingests high-volume ordered streams with partitions and consumer groups. It is a streaming log, not a task queue. Why the correct answer wins: An Event Grid subscription on the storage system topic pushes blob-created events as soon as the resource changes.
- **B:** Incorrect for this question. Durable Functions provides orchestrations, activities, timers, and retries with checkpointed state. Orchestrator code must stay deterministic. Why the correct answer wins: An Event Grid subscription on the storage system topic pushes blob-created events as soon as the resource changes.
- **C:** Incorrect for this question. Queue Storage is simple and cheap for large backlogs with at-least-once delivery. It lacks topics, sessions, and scheduled messages. Why the correct answer wins: An Event Grid subscription on the storage system topic pushes blob-created events as soon as the resource changes.
- **D:** Correct. Event Grid delivers discrete notifications to subscribers with retries and filtering. It carries events, not large payloads or ordered streams. In this case: An Event Grid subscription on the storage system topic pushes blob-created events as soon as the resource changes.

### Question 72 — D

Answer: Rely on Event Grid retries with a dead-letter destination. Event Grid retries failed deliveries and dead-letters events that never succeed, so maintenance does not drop them. Event Grid retries failed deliveries with backoff and can store undeliverable events. Handlers must still be idempotent. Local study-map skill 3.4 (Event Grid Filters, Custom Events, and Retries), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure messaging and Functions documentation: https://learn.microsoft.com/en-us/azure/service-bus-messaging/

- **A:** Incorrect for this question. Event Hubs ingests high-volume ordered streams with partitions and consumer groups. It is a streaming log, not a task queue. Why the correct answer wins: Event Grid retries failed deliveries and dead-letters events that never succeed, so maintenance does not drop them.
- **B:** Incorrect for this question. Subject and event-type filters keep handlers focused and reduce cost. Filters are evaluated on event metadata, not payload body. Why the correct answer wins: Event Grid retries failed deliveries and dead-letters events that never succeed, so maintenance does not drop them.
- **C:** Incorrect for this question. A custom schema fits domain events that are not resource lifecycle notifications. Consumers must version the schema contract. Why the correct answer wins: Event Grid retries failed deliveries and dead-letters events that never succeed, so maintenance does not drop them.
- **D:** Correct. Event Grid retries failed deliveries with backoff and can store undeliverable events. Handlers must still be idempotent. In this case: Event Grid retries failed deliveries and dead-letters events that never succeed, so maintenance does not drop them.

### Question 73 — C

Answer: Bind a queue or event trigger to the function. A blob trigger starts the function when the document lands and manages the receive loop for the app. A trigger starts the function when work arrives and handles the receive loop for you. Poison-message behavior is configured in host settings. Local study-map skill 3.5 (Azure Functions Triggers and Bindings), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure messaging and Functions documentation: https://learn.microsoft.com/en-us/azure/service-bus-messaging/

- **A:** Incorrect for this question. Bindings reduce boilerplate for common inputs and outputs and are configured declaratively. Complex operations still need the SDK. Why the correct answer wins: A blob trigger starts the function when the document lands and manages the receive loop for the app.
- **B:** Incorrect for this question. Durable Functions provides orchestrations, activities, timers, and retries with checkpointed state. Orchestrator code must stay deterministic. Why the correct answer wins: A blob trigger starts the function when the document lands and manages the receive loop for the app.
- **C:** Correct. A trigger starts the function when work arrives and handles the receive loop for you. Poison-message behavior is configured in host settings. In this case: A blob trigger starts the function when the document lands and manages the receive loop for the app.
- **D:** Incorrect for this question. An HTTP trigger gives a synchronous API endpoint with route and authorization configuration. Long-running work should hand off to a queue. Why the correct answer wins: A blob trigger starts the function when the document lands and manages the receive loop for the app.

### Question 74 — D

Answer: Host the function app on a premium plan with pre-warmed instances. A premium plan provides pre-warmed instances and virtual network integration for private endpoints. A premium plan reduces cold starts and supports virtual network integration and longer timeouts. It costs more than consumption. Local study-map skill 3.6 (Function App Configuration and Deployment), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure messaging and Functions documentation: https://learn.microsoft.com/en-us/azure/service-bus-messaging/

- **A:** Incorrect for this question. An HTTP trigger gives a synchronous API endpoint with route and authorization configuration. Long-running work should hand off to a queue. Why the correct answer wins: A premium plan provides pre-warmed instances and virtual network integration for private endpoints.
- **B:** Incorrect for this question. Durable Functions provides orchestrations, activities, timers, and retries with checkpointed state. Orchestrator code must stay deterministic. Why the correct answer wins: A premium plan provides pre-warmed instances and virtual network integration for private endpoints.
- **C:** Incorrect for this question. Consumption bills per execution and scales automatically, with cold starts and a timeout ceiling. It fits spiky, short work. Why the correct answer wins: A premium plan provides pre-warmed instances and virtual network integration for private endpoints.
- **D:** Correct. A premium plan reduces cold starts and supports virtual network integration and longer timeouts. It costs more than consumption. In this case: A premium plan provides pre-warmed instances and virtual network integration for private endpoints.

### Question 75 — C

Answer: Deploy the function app through a CI pipeline with app settings applied. A pipeline deployment publishes code and applies settings together, so the app never runs against half-applied configuration. Pipeline deployment keeps code and configuration versioned together and repeatable. Secrets belong in a vault reference, not in the pipeline file. Local study-map skill 3.6 (Function App Configuration and Deployment), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure messaging and Functions documentation: https://learn.microsoft.com/en-us/azure/service-bus-messaging/

- **A:** Incorrect for this question. Application settings become environment variables for the container and can be swapped per slot. Sensitive values should still reference a vault. Why the correct answer wins: A pipeline deployment publishes code and applies settings together, so the app never runs against half-applied configuration.
- **B:** Incorrect for this question. An HTTP trigger gives a synchronous API endpoint with route and authorization configuration. Long-running work should hand off to a queue. Why the correct answer wins: A pipeline deployment publishes code and applies settings together, so the app never runs against half-applied configuration.
- **C:** Correct. Pipeline deployment keeps code and configuration versioned together and repeatable. Secrets belong in a vault reference, not in the pipeline file. In this case: A pipeline deployment publishes code and applies settings together, so the app never runs against half-applied configuration.
- **D:** Incorrect for this question. Consumption bills per execution and scales automatically, with cold starts and a timeout ceiling. It fits spiky, short work. Why the correct answer wins: A pipeline deployment publishes code and applies settings together, so the app never runs against half-applied configuration.

### Question 76 — C, D

Answers: Assign a managed identity to the function app and use it for downstream calls; Tune the function app concurrency and batch size. A managed identity replaces the stored secret, and tuned concurrency and batch size bound parallel database writes. A function app can authenticate with a managed identity, so no connection secret is needed in app settings. Concurrency and batch size bound how much work one instance takes at a time, which controls downstream pressure and memory. Too high a value causes throttling and timeouts. Local study-map skill 3.6 (Function App Configuration and Deployment), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure messaging and Functions documentation: https://learn.microsoft.com/en-us/azure/service-bus-messaging/

- **A:** Incorrect for this question. Application settings become environment variables for the container and can be swapped per slot. Sensitive values should still reference a vault. Why the correct answer wins: A managed identity replaces the stored secret, and tuned concurrency and batch size bound parallel database writes.
- **B:** Incorrect for this question. A premium plan reduces cold starts and supports virtual network integration and longer timeouts. It costs more than consumption. Why the correct answer wins: A managed identity replaces the stored secret, and tuned concurrency and batch size bound parallel database writes.
- **C:** Correct. A function app can authenticate with a managed identity, so no connection secret is needed in app settings. In this case: A managed identity replaces the stored secret, and tuned concurrency and batch size bound parallel database writes.
- **D:** Correct. Concurrency and batch size bound how much work one instance takes at a time, which controls downstream pressure and memory. Too high a value causes throttling and timeouts. In this case: A managed identity replaces the stored secret, and tuned concurrency and batch size bound parallel database writes.
- **E:** Incorrect for this question. Consumption bills per execution and scales automatically, with cold starts and a timeout ceiling. It fits spiky, short work. Why the correct answer wins: A managed identity replaces the stored secret, and tuned concurrency and batch size bound parallel database writes.

### Question 77 — B, D

Answers: Publish to a Service Bus topic with multiple subscriptions; Add a SQL or correlation filter to a subscription. A topic with separate subscriptions provides fan-out, and a subscription filter limits billing to matching documents. Topics fan out one message to independent subscribers, each with its own filter and dead-letter queue. Subscribers process at their own pace. Subscription filters route only matching messages to a handler, reducing wasted processing. Filter evaluation happens broker-side on message properties. Local study-map skill 3.2 (Service Bus Topics, Subscriptions, and Filters), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure messaging and Functions documentation: https://learn.microsoft.com/en-us/azure/service-bus-messaging/

- **A:** Incorrect for this question. A queue decouples producers from a single consumer group and smooths bursts. Delivery semantics depend on receive mode and completion. Why the correct answer wins: A topic with separate subscriptions provides fan-out, and a subscription filter limits billing to matching documents.
- **B:** Correct. Topics fan out one message to independent subscribers, each with its own filter and dead-letter queue. Subscribers process at their own pace. In this case: A topic with separate subscriptions provides fan-out, and a subscription filter limits billing to matching documents.
- **C:** Incorrect for this question. Subject and event-type filters keep handlers focused and reduce cost. Filters are evaluated on event metadata, not payload body. Why the correct answer wins: A topic with separate subscriptions provides fan-out, and a subscription filter limits billing to matching documents.
- **D:** Correct. Subscription filters route only matching messages to a handler, reducing wasted processing. Filter evaluation happens broker-side on message properties. In this case: A topic with separate subscriptions provides fan-out, and a subscription filter limits billing to matching documents.
- **E:** Incorrect for this question. Queue Storage is simple and cheap for large backlogs with at-least-once delivery. It lacks topics, sessions, and scheduled messages. Why the correct answer wins: A topic with separate subscriptions provides fan-out, and a subscription filter limits billing to matching documents.

### Question 78 — D

Answer: Publish a custom event → evaluate the subscription filter → deliver to the handler → retry on failure → dead-letter undeliverable events. Publication precedes filter evaluation, delivery precedes retries, and dead-lettering follows exhausted retries. Filtering happens before delivery, retries handle transient failures, and dead-lettering preserves what cannot be delivered. Local study-map skill 3.4 (Event Grid Filters, Custom Events, and Retries), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure messaging and Functions documentation: https://learn.microsoft.com/en-us/azure/service-bus-messaging/

- **A:** Incorrect for this question. A filter is evaluated before delivery, and retries must occur before dead-lettering. Why the correct answer wins: Publication precedes filter evaluation, delivery precedes retries, and dead-lettering follows exhausted retries.
- **B:** Incorrect for this question. A filter cannot evaluate an event that has not been published. Why the correct answer wins: Publication precedes filter evaluation, delivery precedes retries, and dead-lettering follows exhausted retries.
- **C:** Incorrect for this question. Delivery cannot precede publication and filtering. Why the correct answer wins: Publication precedes filter evaluation, delivery precedes retries, and dead-lettering follows exhausted retries.
- **D:** Correct. Filtering happens before delivery, retries handle transient failures, and dead-lettering preserves what cannot be delivered. In this case: Publication precedes filter evaluation, delivery precedes retries, and dead-lettering follows exhausted retries.

### Question 79 — B

Answer: Store the secret in Azure Key Vault and read it at runtime. Key Vault stores the secret with version history and audit logging, and the app reads it at runtime. A vault centralizes secret storage with access control and audit. Retrieval should use an identity, not a copied credential. Local study-map skill 4.1 (Key Vault Secret Storage, Rotation, and Retrieval), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Key Vault, App Configuration, and Monitor documentation: https://learn.microsoft.com/en-us/azure/azure-monitor/

- **A:** Incorrect for this question. A scoped role grants only the operations the app performs and limits blast radius. Prefer built-in roles over broad contributor grants. Why the correct answer wins: Key Vault stores the secret with version history and audit logging, and the app reads it at runtime.
- **B:** Correct. A vault centralizes secret storage with access control and audit. Retrieval should use an identity, not a copied credential. In this case: Key Vault stores the secret with version history and audit logging, and the app reads it at runtime.
- **C:** Incorrect for this question. A Key Vault reference resolves at runtime so the secret is never written into application settings. The app identity still needs permission to read it. Why the correct answer wins: Key Vault stores the secret with version history and audit logging, and the app reads it at runtime.
- **D:** Incorrect for this question. App Configuration separates configuration from code and supports labels, feature flags, and Key Vault references. Change still needs a refresh strategy. Why the correct answer wins: Key Vault stores the secret with version history and audit logging, and the app reads it at runtime.

### Question 80 — B

Answer: Store settings and feature flags in Azure App Configuration. App Configuration centralizes settings and flags for several services while keeping environment separation through labels. App Configuration separates configuration from code and supports labels, feature flags, and Key Vault references. Change still needs a refresh strategy. Local study-map skill 4.2 (App Configuration Settings and Feature Flags), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Key Vault, App Configuration, and Monitor documentation: https://learn.microsoft.com/en-us/azure/azure-monitor/

- **A:** Incorrect for this question. Sentinel-key or polling refresh lets a running app pick up new settings. Refresh intervals trade responsiveness against request volume. Why the correct answer wins: App Configuration centralizes settings and flags for several services while keeping environment separation through labels.
- **B:** Correct. App Configuration separates configuration from code and supports labels, feature flags, and Key Vault references. Change still needs a refresh strategy. In this case: App Configuration centralizes settings and flags for several services while keeping environment separation through labels.
- **C:** Incorrect for this question. Labels keep dev, test, and prod values in one store with one key schema. A misconfigured label selector silently serves the wrong values. Why the correct answer wins: App Configuration centralizes settings and flags for several services while keeping environment separation through labels.
- **D:** Incorrect for this question. A Key Vault reference keeps non-secret settings in App Configuration while the value stays in the vault. The app identity needs both sets of permissions. Why the correct answer wins: App Configuration centralizes settings and flags for several services while keeping environment separation through labels.

### Question 81 — B

Answer: Instrument the service with the OpenTelemetry SDK. OpenTelemetry instrumentation records spans across the workflow so one trace covers every hop. OpenTelemetry emits vendor-neutral traces, metrics, and logs with context propagation. Exporters and sampling decide what reaches the backend. Local study-map skill 4.3 (Distributed Tracing with OpenTelemetry), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Key Vault, App Configuration, and Monitor documentation: https://learn.microsoft.com/en-us/azure/azure-monitor/

- **A:** Incorrect for this question. KQL filters, projects, and aggregates log and metric tables in Log Analytics. Start narrow with a time range and a request ID. Why the correct answer wins: OpenTelemetry instrumentation records spans across the workflow so one trace covers every hop.
- **B:** Correct. OpenTelemetry emits vendor-neutral traces, metrics, and logs with context propagation. Exporters and sampling decide what reaches the backend. In this case: OpenTelemetry instrumentation records spans across the workflow so one trace covers every hop.
- **C:** Incorrect for this question. Including the trace ID in log records lets you pivot from a failed span to its log lines. Without it, logs and traces are separate worlds. Why the correct answer wins: OpenTelemetry instrumentation records spans across the workflow so one trace covers every hop.
- **D:** Incorrect for this question. Application Insights correlates requests, dependencies, and exceptions into end-to-end transactions. Sampling can hide rare failures. Why the correct answer wins: OpenTelemetry instrumentation records spans across the workflow so one trace covers every hop.

### Question 82 — C

Answer: Propagate trace context across every service and queue hop. Trace context must travel with the message, otherwise the consumer starts a new trace and the chain breaks. Propagation stitches one trace across HTTP, messaging, and Functions so the whole path is visible. Missing propagation breaks the trace at that hop. Local study-map skill 4.3 (Distributed Tracing with OpenTelemetry), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Key Vault, App Configuration, and Monitor documentation: https://learn.microsoft.com/en-us/azure/azure-monitor/

- **A:** Incorrect for this question. Including the trace ID in log records lets you pivot from a failed span to its log lines. Without it, logs and traces are separate worlds. Why the correct answer wins: Trace context must travel with the message, otherwise the consumer starts a new trace and the chain breaks.
- **B:** Incorrect for this question. Sampling keeps telemetry cost bounded, but aggressive sampling can hide rare failures. Tail sampling can retain errors preferentially. Why the correct answer wins: Trace context must travel with the message, otherwise the consumer starts a new trace and the chain breaks.
- **C:** Correct. Propagation stitches one trace across HTTP, messaging, and Functions so the whole path is visible. Missing propagation breaks the trace at that hop. In this case: Trace context must travel with the message, otherwise the consumer starts a new trace and the chain breaks.
- **D:** Incorrect for this question. A collector batches, filters, and routes telemetry, and decouples app configuration from the backend. It is another component to run and monitor. Why the correct answer wins: Trace context must travel with the message, otherwise the consumer starts a new trace and the chain breaks.

### Question 83 — C

Answer: Query the workspace with KQL to find the failing operation. KQL over the workspace returns the failing operation and its correlation identifier without a code change. KQL filters, projects, and aggregates log and metric tables in Log Analytics. Start narrow with a time range and a request ID. Local study-map skill 4.4 (KQL Queries for Logs and Metrics), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Key Vault, App Configuration, and Monitor documentation: https://learn.microsoft.com/en-us/azure/azure-monitor/

- **A:** Incorrect for this question. Platform metrics are cheap and near-real-time, so they suit latency and failure-rate alerts. Log-based alerts add latency and query cost. Why the correct answer wins: KQL over the workspace returns the failing operation and its correlation identifier without a code change.
- **B:** Incorrect for this question. Joining request and dependency telemetry shows which downstream call fails inside a slow request. Cross-workspace joins need the right scope. Why the correct answer wins: KQL over the workspace returns the failing operation and its correlation identifier without a code change.
- **C:** Correct. KQL filters, projects, and aggregates log and metric tables in Log Analytics. Start narrow with a time range and a request ID. In this case: KQL over the workspace returns the failing operation and its correlation identifier without a code change.
- **D:** Incorrect for this question. Time-binned aggregation reveals the shape of an incident: a step change, a ramp, or a periodic spike. Averages alone hide short outages. Why the correct answer wins: KQL over the workspace returns the failing operation and its correlation identifier without a code change.

### Question 84 — D

Answer: Assign a least-privilege role to the application identity. A least-privilege role scoped to the resources the app uses replaces the broad owner assignment. A scoped role grants only the operations the app performs and limits blast radius. Prefer built-in roles over broad contributor grants. Local study-map skill 4.5 (Identity-Based Access for Application Services), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Key Vault, App Configuration, and Monitor documentation: https://learn.microsoft.com/en-us/azure/azure-monitor/

- **A:** Incorrect for this question. Workload identity lets pods obtain tokens without stored secrets. Each workload should get its own identity and narrow role. Why the correct answer wins: A least-privilege role scoped to the resources the app uses replaces the broad owner assignment.
- **B:** Incorrect for this question. Soft delete and purge protection stop accidental or malicious permanent loss of secrets. They also constrain how names can be reused. Why the correct answer wins: A least-privilege role scoped to the resources the app uses replaces the broad owner assignment.
- **C:** Incorrect for this question. A private endpoint keeps traffic on the virtual network and removes public exposure. DNS resolution must be wired to the private zone. Why the correct answer wins: A least-privilege role scoped to the resources the app uses replaces the broad owner assignment.
- **D:** Correct. A scoped role grants only the operations the app performs and limits blast radius. Prefer built-in roles over broad contributor grants. In this case: A least-privilege role scoped to the resources the app uses replaces the broad owner assignment.

### Question 85 — B, D

Answers: Store the secret in Azure Key Vault and read it at runtime; Authenticate with a managed identity instead of a stored key. The vault holds the secret, and a managed identity gives the worker a credential that never appears in configuration. A vault centralizes secret storage with access control and audit. Retrieval should use an identity, not a copied credential. A managed identity issues tokens from the platform, removing secret distribution from the app. Role assignment still scopes what it can reach. Local study-map skill 4.1 (Key Vault Secret Storage, Rotation, and Retrieval), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Key Vault, App Configuration, and Monitor documentation: https://learn.microsoft.com/en-us/azure/azure-monitor/

- **A:** Incorrect for this question. App Configuration separates configuration from code and supports labels, feature flags, and Key Vault references. Change still needs a refresh strategy. Why the correct answer wins: The vault holds the secret, and a managed identity gives the worker a credential that never appears in configuration.
- **B:** Correct. A managed identity issues tokens from the platform, removing secret distribution from the app. Role assignment still scopes what it can reach. In this case: The vault holds the secret, and a managed identity gives the worker a credential that never appears in configuration.
- **C:** Incorrect for this question. A Key Vault reference resolves at runtime so the secret is never written into application settings. The app identity still needs permission to read it. Why the correct answer wins: The vault holds the secret, and a managed identity gives the worker a credential that never appears in configuration.
- **D:** Correct. A vault centralizes secret storage with access control and audit. Retrieval should use an identity, not a copied credential. In this case: The vault holds the secret, and a managed identity gives the worker a credential that never appears in configuration.
- **E:** Incorrect for this question. A scoped role grants only the operations the app performs and limits blast radius. Prefer built-in roles over broad contributor grants. Why the correct answer wins: The vault holds the secret, and a managed identity gives the worker a credential that never appears in configuration.

### Question 86 — B, E

Answers: Reference the Key Vault secret from an App Configuration key value; Use App Configuration labels to separate environments. Labels separate clinics inside one store, and a Key Vault reference keeps the secret out of the store. A Key Vault reference keeps non-secret settings in App Configuration while the value stays in the vault. The app identity needs both sets of permissions. Labels keep dev, test, and prod values in one store with one key schema. A misconfigured label selector silently serves the wrong values. Local study-map skill 4.2 (App Configuration Settings and Feature Flags), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Key Vault, App Configuration, and Monitor documentation: https://learn.microsoft.com/en-us/azure/azure-monitor/

- **A:** Incorrect for this question. A feature flag enables reviewed code in production without a redeploy and lets it be switched off instantly. Flag state still needs ownership and cleanup. Why the correct answer wins: Labels separate clinics inside one store, and a Key Vault reference keeps the secret out of the store.
- **B:** Correct. A Key Vault reference keeps non-secret settings in App Configuration while the value stays in the vault. The app identity needs both sets of permissions. In this case: Labels separate clinics inside one store, and a Key Vault reference keeps the secret out of the store.
- **C:** Incorrect for this question. Sentinel-key or polling refresh lets a running app pick up new settings. Refresh intervals trade responsiveness against request volume. Why the correct answer wins: Labels separate clinics inside one store, and a Key Vault reference keeps the secret out of the store.
- **D:** Incorrect for this question. Pinning a version makes a rotation invisible to the app until it is redeployed, which is useful for break-glass and dangerous for routine rotation. Why the correct answer wins: Labels separate clinics inside one store, and a Key Vault reference keeps the secret out of the store.
- **E:** Correct. Labels keep dev, test, and prod values in one store with one key schema. A misconfigured label selector silently serves the wrong values. In this case: Labels separate clinics inside one store, and a Key Vault reference keeps the secret out of the store.

### Question 87 — C, D

Answers: Project only the columns needed and filter by time first; Create an alert rule on the failure rate or latency metric. Projecting only needed columns and filtering by time first cuts scanned data, and an alert rule still pages on-call. Reducing columns and rows early lowers query cost and latency. Broad queries over long ranges are the usual cause of slow KQL. An alert turns a threshold breach into a notification or action. Thresholds need a baseline, or the alert is noise. Local study-map skill 4.4 (KQL Queries for Logs and Metrics), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Key Vault, App Configuration, and Monitor documentation: https://learn.microsoft.com/en-us/azure/azure-monitor/

- **A:** Incorrect for this question. Time-binned aggregation reveals the shape of an incident: a step change, a ramp, or a periodic spike. Averages alone hide short outages. Why the correct answer wins: Projecting only needed columns and filtering by time first cuts scanned data, and an alert rule still pages on-call.
- **B:** Incorrect for this question. Precomputed results avoid recomputing expensive aggregations on every dashboard refresh. The trade-off is storage and freshness lag. Why the correct answer wins: Projecting only needed columns and filtering by time first cuts scanned data, and an alert rule still pages on-call.
- **C:** Correct. An alert turns a threshold breach into a notification or action. Thresholds need a baseline, or the alert is noise. In this case: Projecting only needed columns and filtering by time first cuts scanned data, and an alert rule still pages on-call.
- **D:** Correct. Reducing columns and rows early lowers query cost and latency. Broad queries over long ranges are the usual cause of slow KQL. In this case: Projecting only needed columns and filtering by time first cuts scanned data, and an alert rule still pages on-call.
- **E:** Incorrect for this question. Platform metrics are cheap and near-real-time, so they suit latency and failure-rate alerts. Log-based alerts add latency and query cost. Why the correct answer wins: Projecting only needed columns and filtering by time first cuts scanned data, and an alert rule still pages on-call.

### Question 88 — C

Answer: Store the secret in Key Vault → grant the app identity access → reference the secret from the app → rotate the secret → the app reads the new version. The secret must exist and be granted before it is referenced, and rotation follows a working reference. Access must be granted before the reference resolves, and the app must read the current version after rotation. Local study-map skill 4.1 (Key Vault Secret Storage, Rotation, and Retrieval), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Key Vault, App Configuration, and Monitor documentation: https://learn.microsoft.com/en-us/azure/azure-monitor/

- **A:** Incorrect for this question. There is nothing to rotate or reference before the secret is stored. Why the correct answer wins: The secret must exist and be granted before it is referenced, and rotation follows a working reference.
- **B:** Incorrect for this question. A reference cannot resolve before the secret and the access grant exist. Why the correct answer wins: The secret must exist and be granted before it is referenced, and rotation follows a working reference.
- **C:** Correct. Access must be granted before the reference resolves, and the app must read the current version after rotation. In this case: The secret must exist and be granted before it is referenced, and rotation follows a working reference.
- **D:** Incorrect for this question. Access can be granted first, but rotation cannot precede storing the secret. Why the correct answer wins: The secret must exist and be granted before it is referenced, and rotation follows a working reference.

### Question 89 — D

Answer: Test end-to-end connectivity from inside the container to each dependency. Name resolution inside the workload network must point at the private endpoint address, otherwise traffic leaves on the wrong path. Reaching a dependency from the pod or replica proves DNS, egress, and firewall paths together. Host-side tests can succeed while the container path fails. Local study-map skill 1.7 (Container Logs, Events, and Connectivity), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure container hosting documentation: https://learn.microsoft.com/en-us/azure/container-apps/

- **A:** Incorrect for this question. A private endpoint needs matching name resolution or clients still resolve the public address. The zone must be linked to the workload network. Why the correct answer wins: Name resolution inside the workload network must point at the private endpoint address, otherwise traffic leaves on the wrong path.
- **B:** Incorrect for this question. A private endpoint keeps traffic on the virtual network and removes public exposure. DNS resolution must be wired to the private zone. Why the correct answer wins: Name resolution inside the workload network must point at the private endpoint address, otherwise traffic leaves on the wrong path.
- **C:** Incorrect for this question. Container Apps and AKS surface stdout logs and platform events into a workspace for KQL analysis. Verbosity and retention cost money. Why the correct answer wins: Name resolution inside the workload network must point at the private endpoint address, otherwise traffic leaves on the wrong path.
- **D:** Correct. Reaching a dependency from the pod or replica proves DNS, egress, and firewall paths together. Host-side tests can succeed while the container path fails. In this case: Name resolution inside the workload network must point at the private endpoint address, otherwise traffic leaves on the wrong path.

### Question 90 — A

Answer: Inspect the dead-letter queue and resubmit corrected messages. Dead-lettering preserves the poison message for diagnosis while the queue keeps moving. Dead-lettering preserves poison messages for diagnosis instead of losing them. Resubmission needs a fix and an idempotent handler. Local study-map skill 3.3 (Service Bus Dead-Lettering and Retries), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure messaging and Functions documentation: https://learn.microsoft.com/en-us/azure/service-bus-messaging/

- **A:** Correct. Dead-lettering preserves poison messages for diagnosis instead of losing them. Resubmission needs a fix and an idempotent handler. In this case: Dead-lettering preserves the poison message for diagnosis while the queue keeps moving.
- **B:** Incorrect for this question. Receive-and-delete removes the message on delivery, so a crash loses work silently. It suits telemetry, not payments. Why the correct answer wins: Dead-lettering preserves the poison message for diagnosis while the queue keeps moving.
- **C:** Incorrect for this question. A duplicate-detection window drops repeated sends within the window, which helps with at-least-once producers. The window is time-bounded. Why the correct answer wins: Dead-lettering preserves the poison message for diagnosis while the queue keeps moving.
- **D:** Incorrect for this question. A delivery cap stops infinite retries of a failing message and moves it to the dead-letter queue. The cap must exceed legitimate transient retries. Why the correct answer wins: Dead-lettering preserves the poison message for diagnosis while the queue keeps moving.

### Question 91 — B

Answer: Grant the app identity data-plane access to the vault. The identity needs a data-plane role or policy on the vault before it can read the secret. Vault access is a separate authorization decision from the app identity. Without a data-plane role or policy the reference fails at runtime. Local study-map skill 4.1 (Key Vault Secret Storage, Rotation, and Retrieval), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Key Vault, App Configuration, and Monitor documentation: https://learn.microsoft.com/en-us/azure/azure-monitor/

- **A:** Incorrect for this question. A scoped role grants only the operations the app performs and limits blast radius. Prefer built-in roles over broad contributor grants. Why the correct answer wins: The identity needs a data-plane role or policy on the vault before it can read the secret.
- **B:** Correct. Vault access is a separate authorization decision from the app identity. Without a data-plane role or policy the reference fails at runtime. In this case: The identity needs a data-plane role or policy on the vault before it can read the secret.
- **C:** Incorrect for this question. Soft delete and purge protection stop accidental or malicious permanent loss of secrets. They also constrain how names can be reused. Why the correct answer wins: The identity needs a data-plane role or policy on the vault before it can read the secret.
- **D:** Incorrect for this question. A managed identity issues tokens from the platform, removing secret distribution from the app. Role assignment still scopes what it can reach. Why the correct answer wins: The identity needs a data-plane role or policy on the vault before it can read the secret.

### Question 92 — B

Answer: Create a new Container Apps revision and shift traffic between revisions. Container Apps revisions support percentage traffic allocation, which enables a measured canary and a quick reversal. Revision-based traffic splitting enables canary and blue-green releases. Revision mode and scale rules must be set deliberately. Local study-map skill 1.4 (Container Apps Deployment and Revisions), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure container hosting documentation: https://learn.microsoft.com/en-us/azure/container-apps/

- **A:** Incorrect for this question. Geo-replication reduces cross-region pull latency and gives a local copy during a regional failure. It adds cost and replication management. Why the correct answer wins: Container Apps revisions support percentage traffic allocation, which enables a measured canary and a quick reversal.
- **B:** Correct. Revision-based traffic splitting enables canary and blue-green releases. Revision mode and scale rules must be set deliberately. In this case: Container Apps revisions support percentage traffic allocation, which enables a measured canary and a quick reversal.
- **C:** Incorrect for this question. A slot swap warms the new version before it takes production traffic and makes rollback a second swap. Slot-local settings must be marked sticky. Why the correct answer wins: Container Apps revisions support percentage traffic allocation, which enables a measured canary and a quick reversal.
- **D:** Incorrect for this question. HPA adjusts replicas from resource metrics but needs metrics-server and enough node capacity. It cannot scale to zero. Why the correct answer wins: Container Apps revisions support percentage traffic allocation, which enables a measured canary and a quick reversal.

### Question 93 — B

Answer: Scale on the Service Bus queue length with a KEDA Azure Service Bus scaler. A queue-length scaler adds consumers while documents are waiting and scales to zero when the queue drains. A queue-length scaler adds replicas while work is backed up and removes them when the queue drains. Message lock duration must exceed processing time. Local study-map skill 1.5 (Event-Driven Scaling with KEDA), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure container hosting documentation: https://learn.microsoft.com/en-us/azure/container-apps/

- **A:** Incorrect for this question. CPU-based scaling reacts after work is already queued and cannot scale to zero on an empty queue. It suits steady request-driven services. Why the correct answer wins: A queue-length scaler adds consumers while documents are waiting and scales to zero when the queue drains.
- **B:** Correct. A queue-length scaler adds replicas while work is backed up and removes them when the queue drains. Message lock duration must exceed processing time. In this case: A queue-length scaler adds consumers while documents are waiting and scales to zero when the queue drains.
- **C:** Incorrect for this question. Container Instances starts a single container group quickly for short tasks. It has no orchestrator-level scaling or revision model. Why the correct answer wins: A queue-length scaler adds consumers while documents are waiting and scales to zero when the queue drains.
- **D:** Incorrect for this question. HPA adjusts replicas from resource metrics but needs metrics-server and enough node capacity. It cannot scale to zero. Why the correct answer wins: A queue-length scaler adds consumers while documents are waiting and scales to zero when the queue drains.

### Question 94 — D

Answer: Filter on metadata columns in the same query as the vector search. Filtering on metadata in the same statement as the distance operator keeps the result set both complete and scoped. Combining a WHERE filter with the distance operator keeps retrieval inside the caller's scope and improves relevance. Index the filter columns too. Local study-map skill 2.9 (PostgreSQL RAG with Metadata Filters), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Cosmos DB and PostgreSQL vector documentation: https://learn.microsoft.com/en-us/azure/cosmos-db/

- **A:** Incorrect for this question. IVFFlat uses clustering lists and needs periodic rebuilds as data grows, but costs less memory than HNSW. Probes trade recall for speed. Why the correct answer wins: Filtering on metadata in the same statement as the distance operator keeps the result set both complete and scoped.
- **B:** Incorrect for this question. Post-filtering can return fewer results than requested and can leak existence or counts if the filtering is careless. Push authorization into the query. Why the correct answer wins: Filtering on metadata in the same statement as the distance operator keeps the result set both complete and scoped.
- **C:** Incorrect for this question. HNSW gives fast approximate nearest-neighbour queries with a larger memory footprint and slower builds. Recall is tunable at query time. Why the correct answer wins: Filtering on metadata in the same statement as the distance operator keeps the result set both complete and scoped.
- **D:** Correct. Combining a WHERE filter with the distance operator keeps retrieval inside the caller's scope and improves relevance. Index the filter columns too. In this case: Filtering on metadata in the same statement as the distance operator keeps the result set both complete and scoped.

### Question 95 — C

Answer: Store embeddings in PostgreSQL by using the pgvector extension. pgvector keeps embeddings beside relational columns so filters and similarity run in one query. pgvector keeps vectors beside relational data, so filters and joins run in one query. Index type and parameter tuning decide latency. Local study-map skill 2.6 (PostgreSQL Connection and Schema Modeling), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Cosmos DB and PostgreSQL vector documentation: https://learn.microsoft.com/en-us/azure/cosmos-db/

- **A:** Incorrect for this question. Cosmos DB gives globally distributed, low-latency document access with tunable consistency. Partition key and RU planning determine the cost profile. Why the correct answer wins: pgvector keeps embeddings beside relational columns so filters and similarity run in one query.
- **B:** Incorrect for this question. Application-side scoring works for tiny collections and tests, but it moves all data over the wire and does not scale with corpus size. Why the correct answer wins: pgvector keeps embeddings beside relational columns so filters and similarity run in one query.
- **C:** Correct. pgvector keeps vectors beside relational data, so filters and joins run in one query. Index type and parameter tuning decide latency. In this case: pgvector keeps embeddings beside relational columns so filters and similarity run in one query.
- **D:** Incorrect for this question. A cache absorbs repeated reads and cuts latency for hot data. Cache keys, TTLs, and invalidation must match the freshness requirement. Why the correct answer wins: pgvector keeps embeddings beside relational columns so filters and similarity run in one query.

### Question 96 — A

Answer: Filter on metadata columns in the same query as the vector search. Filtering on metadata in the same query as the distance operator keeps results in scope and the count complete. Combining a WHERE filter with the distance operator keeps retrieval inside the caller's scope and improves relevance. Index the filter columns too. Local study-map skill 2.9 (PostgreSQL RAG with Metadata Filters), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Cosmos DB and PostgreSQL vector documentation: https://learn.microsoft.com/en-us/azure/cosmos-db/

- **A:** Correct. Combining a WHERE filter with the distance operator keeps retrieval inside the caller's scope and improves relevance. Index the filter columns too. In this case: Filtering on metadata in the same query as the distance operator keeps results in scope and the count complete.
- **B:** Incorrect for this question. IVFFlat uses clustering lists and needs periodic rebuilds as data grows, but costs less memory than HNSW. Probes trade recall for speed. Why the correct answer wins: Filtering on metadata in the same query as the distance operator keeps results in scope and the count complete.
- **C:** Incorrect for this question. Post-filtering can return fewer results than requested and can leak existence or counts if the filtering is careless. Push authorization into the query. Why the correct answer wins: Filtering on metadata in the same query as the distance operator keeps results in scope and the count complete.
- **D:** Incorrect for this question. HNSW gives fast approximate nearest-neighbour queries with a larger memory footprint and slower builds. Recall is tunable at query time. Why the correct answer wins: Filtering on metadata in the same query as the distance operator keeps results in scope and the count complete.

### Question 97 — D

Answer: Create a vector index in Managed Redis for similarity search. A Redis vector index serves similarity queries from memory at low latency. Redis vector search serves low-latency similarity queries from memory. The corpus must fit the memory budget and be rebuilt on model change. Local study-map skill 2.12 (Azure Managed Redis Vector Indexing), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Cosmos DB and PostgreSQL vector documentation: https://learn.microsoft.com/en-us/azure/cosmos-db/

- **A:** Incorrect for this question. A lock can serialize work across instances, but correctness under retries still needs idempotency keys in the data store. Locks expire and can be lost. Why the correct answer wins: A Redis vector index serves similarity queries from memory at low latency.
- **B:** Incorrect for this question. A cache absorbs repeated reads and cuts latency for hot data. Cache keys, TTLs, and invalidation must match the freshness requirement. Why the correct answer wins: A Redis vector index serves similarity queries from memory at low latency.
- **C:** Incorrect for this question. Session storage in Redis survives instance restarts and supports distributed instances. Sessions must be scoped and expiring. Why the correct answer wins: A Redis vector index serves similarity queries from memory at low latency.
- **D:** Correct. Redis vector search serves low-latency similarity queries from memory. The corpus must fit the memory budget and be rebuilt on model change. In this case: A Redis vector index serves similarity queries from memory at low latency.

### Question 98 — C

Answer: Run a change feed processor to react to new and updated items. A change feed processor streams inserts and updates in order per partition and pushes them to the enrichment step. The change feed delivers an ordered stream of changes per partition for downstream processing. It is not a delete feed, so deletions need a workaround. Local study-map skill 2.5 (Cosmos DB Change Feed Processing), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Cosmos DB and PostgreSQL vector documentation: https://learn.microsoft.com/en-us/azure/cosmos-db/

- **A:** Incorrect for this question. Event Grid delivers discrete notifications to subscribers with retries and filtering. It carries events, not large payloads or ordered streams. Why the correct answer wins: A change feed processor streams inserts and updates in order per partition and pushes them to the enrichment step.
- **B:** Incorrect for this question. Leases track partition ownership so multiple processor instances share work and resume from a continuation token. Lease writes consume RUs too. Why the correct answer wins: A change feed processor streams inserts and updates in order per partition and pushes them to the enrichment step.
- **C:** Correct. The change feed delivers an ordered stream of changes per partition for downstream processing. It is not a delete feed, so deletions need a workaround. In this case: A change feed processor streams inserts and updates in order per partition and pushes them to the enrichment step.
- **D:** Incorrect for this question. A duplicate-detection window drops repeated sends within the window, which helps with at-least-once producers. The window is time-bounded. Why the correct answer wins: A change feed processor streams inserts and updates in order per partition and pushes them to the enrichment step.

### Question 99 — B

Answer: Add a SQL or correlation filter to a subscription. A subscription filter evaluates message properties broker-side so only matching documents reach that subscriber. Subscription filters route only matching messages to a handler, reducing wasted processing. Filter evaluation happens broker-side on message properties. Local study-map skill 3.2 (Service Bus Topics, Subscriptions, and Filters), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure messaging and Functions documentation: https://learn.microsoft.com/en-us/azure/service-bus-messaging/

- **A:** Incorrect for this question. A duplicate-detection window drops repeated sends within the window, which helps with at-least-once producers. The window is time-bounded. Why the correct answer wins: A subscription filter evaluates message properties broker-side so only matching documents reach that subscriber.
- **B:** Correct. Subscription filters route only matching messages to a handler, reducing wasted processing. Filter evaluation happens broker-side on message properties. In this case: A subscription filter evaluates message properties broker-side so only matching documents reach that subscriber.
- **C:** Incorrect for this question. Subject and event-type filters keep handlers focused and reduce cost. Filters are evaluated on event metadata, not payload body. Why the correct answer wins: A subscription filter evaluates message properties broker-side so only matching documents reach that subscriber.
- **D:** Incorrect for this question. A custom schema fits domain events that are not resource lifecycle notifications. Consumers must version the schema contract. Why the correct answer wins: A subscription filter evaluates message properties broker-side so only matching documents reach that subscriber.

### Question 100 — A

Answer: Join the requests and dependencies tables on the operation ID. Joining the requests and dependencies tables on the operation identifier attributes time to the function and to its dependency. Joining request and dependency telemetry shows which downstream call fails inside a slow request. Cross-workspace joins need the right scope. Local study-map skill 4.4 (KQL Queries for Logs and Metrics), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Key Vault, App Configuration, and Monitor documentation: https://learn.microsoft.com/en-us/azure/azure-monitor/

- **A:** Correct. Joining request and dependency telemetry shows which downstream call fails inside a slow request. Cross-workspace joins need the right scope. In this case: Joining the requests and dependencies tables on the operation identifier attributes time to the function and to its dependency.
- **B:** Incorrect for this question. Reducing columns and rows early lowers query cost and latency. Broad queries over long ranges are the usual cause of slow KQL. Why the correct answer wins: Joining the requests and dependencies tables on the operation identifier attributes time to the function and to its dependency.
- **C:** Incorrect for this question. Time-binned aggregation reveals the shape of an incident: a step change, a ramp, or a periodic spike. Averages alone hide short outages. Why the correct answer wins: Joining the requests and dependencies tables on the operation identifier attributes time to the function and to its dependency.
- **D:** Incorrect for this question. Precomputed results avoid recomputing expensive aggregations on every dashboard refresh. The trade-off is storage and freshness lag. Why the correct answer wins: Joining the requests and dependencies tables on the operation identifier attributes time to the function and to its dependency.
