# Microsoft AI-200 — Full-Length Mock Exam 4

Azure AI Cloud Developer Associate · 100 questions · expanded practice bank · passing target 700/1000

Blueprint-weighted mock exam of 100 items. Item mix: 76 single-choice, 16 multi-select (selection count stated), 8 ordering items rendered as answer choices, and 4 case studies of 3 questions. Hot-area, drag-and-drop UI, labs, and adaptive problem-solution sets cannot be reproduced in a CSV; see the README for the exact fidelity boundary.

Original educational content, not actual, recalled, or copied Microsoft exam items.

## Questions

### 1. Inspection images must be pulled locally at each plant within the same region as the cluster. What should be configured?

Domain: Develop containerized solutions on Azure

- A. Deploy the mutable latest tag and let the platform resolve it
- B. Replicate the registry to each deployment region
- C. Apply an ACR retention policy to prune old untagged manifests
- D. Run image builds on demand or on a trigger with ACR Tasks

### 2. After a year of nightly builds the registry holds thousands of superseded manifests and costs are rising. What should be applied?

Domain: Develop containerized solutions on Azure

- A. Run image builds on demand or on a trigger with ACR Tasks
- B. Replicate the registry to each deployment region
- C. Deploy the mutable latest tag and let the platform resolve it
- D. Apply an ACR retention policy to prune old untagged manifests

### 3. A commit to the inspection repository must produce a new image without any engineer running a build. What should be configured?

Domain: Develop containerized solutions on Azure

- A. Run image builds on demand or on a trigger with ACR Tasks
- B. Run the batch job in Azure Container Instances
- C. Stage the change in a deployment slot and swap after verification
- D. Build and store versioned images in Azure Container Registry

### 4. The same container must run with different defect thresholds at each plant without a rebuild. What supplies those values?

Domain: Develop containerized solutions on Azure

- A. Reference a Key Vault secret from the app configuration instead of storing it
- B. Supply configuration through App Service application settings
- C. Stage the change in a deployment slot and swap after verification
- D. Deploy the image to Azure App Service as a web app

### 5. A new model build must be fully warmed before it replaces the running inspection app, with an instant rollback. What should be used?

Domain: Develop containerized solutions on Azure

- A. Create a new Container Apps revision and shift traffic between revisions
- B. Supply configuration through App Service application settings
- C. Deploy the mutable latest tag and let the platform resolve it
- D. Stage the change in a deployment slot and swap after verification

### 6. A defect-review worker must scale with the number of unprocessed images and drop to zero between shifts. What should drive scaling?

Domain: Develop containerized solutions on Azure

- A. Run the batch job in Azure Container Instances
- B. Rely on the horizontal pod autoscaler on CPU
- C. Scale the container app on an event source with a KEDA scaler
- D. Scale only on CPU utilization without an event scaler

### 7. The cluster deployment must be reproducible from version control and safe to reapply. What should be used?

Domain: Develop containerized solutions on Azure

- A. Run image builds on demand or on a trigger with ACR Tasks
- B. Apply a declarative Kubernetes manifest to the cluster
- C. Add readiness and liveness probes to the pod specification
- D. Rely on the horizontal pod autoscaler on CPU

### 8. Pods restart intermittently and the team needs container logs and platform events in one place. What should be used?

Domain: Develop containerized solutions on Azure

- A. Enable diagnostic settings to route platform logs to the workspace
- B. Test end-to-end connectivity from inside the container to each dependency
- C. Query container logs and Kubernetes events in Log Analytics
- D. Send telemetry to Application Insights and inspect the transaction view

### 9. Images must be traceable to a build and reproducible without a local host. Which two capabilities provide that? Select two.

Domain: Develop containerized solutions on Azure

- A. Run image builds on demand or on a trigger with ACR Tasks
- B. Build and store versioned images in Azure Container Registry
- C. Deploy the mutable latest tag and let the platform resolve it
- D. Replicate the registry to each deployment region
- E. Stage the change in a deployment slot and swap after verification

### 10. A cluster workload must be reproducible and must not take traffic while still initializing. Which two manifest elements are required? Select two.

Domain: Develop containerized solutions on Azure

- A. Apply a declarative Kubernetes manifest to the cluster
- B. Add readiness and liveness probes to the pod specification
- C. Run the batch job in Azure Container Instances
- D. Rely on the horizontal pod autoscaler on CPU
- E. Tune the scale rule cool-down period and maximum replicas

### 11. Which sequence correctly applies a manifest change and proves it works?

Domain: Develop containerized solutions on Azure

- A. Write the manifest → test ingress connectivity → apply it to the cluster → wait for pod readiness
- B. Wait for pod readiness → apply the manifest → write the manifest → test ingress connectivity
- C. Write the manifest → apply it to the cluster → wait for pod readiness → test ingress connectivity
- D. Apply the manifest → write the manifest → test ingress connectivity → wait for pod readiness

### 12. An inspection record must be read by line identifier and shift without scanning all documents. What should the query include?

Domain: Develop AI solutions by using Azure data management services

- A. Increase provisioned throughput and watch the RU charge per query
- B. Store the documents in Azure Cosmos DB for NoSQL
- C. Query through the Cosmos DB SDK with parameterized queries
- D. Include the partition key in the query predicate

### 13. Image metadata writes trigger throttling only during shift changes. What should be inspected alongside throughput?

Domain: Develop AI solutions by using Azure data management services

- A. Increase provisioned throughput and watch the RU charge per query
- B. Restrict the indexing policy to the paths the queries use
- C. Index every property by using the default automatic policy
- D. Enable autoscale throughput with a maximum RU limit

### 14. An inspector must see the defect note they just saved on the next screen, and other screens may lag. Which level fits?

Domain: Develop AI solutions by using Azure data management services

- A. Use eventual consistency to minimize read cost
- B. Choose the account consistency level that matches the read requirement
- C. Use session consistency for reads within the same client session
- D. Use strong consistency for every read in the account

### 15. Reference defect embeddings and their metadata must be queried together for similarity. What should be used?

Domain: Develop AI solutions by using Azure data management services

- A. Declare the embedding dimensions and vector index type on the container policy
- B. Use the DiskANN vector index for large collections
- C. Scan every document and compute similarity in application code
- D. Store embeddings in a vector property and query with VectorDistance

### 16. Several instances must share change feed partitions and resume after a restart. What tracks that progress?

Domain: Develop AI solutions by using Azure data management services

- A. Use a lease container to coordinate change feed readers
- B. Batch related writes in a transactional batch within one partition key
- C. Enable duplicate detection on the queue
- D. Run a change feed processor to react to new and updated items

### 17. Defect measurements must be filtered by line and compared by embedding in one statement. How should the table be modeled?

Domain: Develop AI solutions by using Azure data management services

- A. Add a read replica and send all vector queries to it
- B. Store embeddings in PostgreSQL by using the pgvector extension
- C. Model typed columns for filters and one vector column for the embedding
- D. Scale compute and memory to fit index size and query concurrency

### 18. Reference-image similarity over a large table must return quickly with tunable recall. Which index fits?

Domain: Develop AI solutions by using Azure data management services

- A. Query without a vector index and let PostgreSQL scan the table
- B. Create an HNSW index for low-latency approximate search
- C. Increase maintenance and query memory settings for index builds and sorts
- D. Create an IVFFlat index to save memory on a large table

### 19. Similarity latency spikes and the server reports memory pressure after index growth. What should be adjusted?

Domain: Develop AI solutions by using Azure data management services

- A. Increase maintenance and query memory settings for index builds and sorts
- B. Scale compute and memory to fit index size and query concurrency
- C. Increase storage throughput for index builds and bulk loads
- D. Reuse a bounded connection pool instead of opening a connection per request

### 20. Inspection stations reconnect constantly and the database rejects new sessions. What should be used first?

Domain: Develop AI solutions by using Azure data management services

- A. Place a connection pooler in front of PostgreSQL for many short-lived clients
- B. Add a read replica and send all vector queries to it
- C. Reuse a bounded connection pool instead of opening a connection per request
- D. Use prepared statements and batch round trips

### 21. Cached plant dashboards must never show data older than ten minutes. What should be set?

Domain: Develop AI solutions by using Azure data management services

- A. Flush the database after each deployment to guarantee fresh data
- B. Rely on the eviction policy and skip explicit TTLs
- C. Invalidate or overwrite the cache entry when the source changes
- D. Set a TTL on each cached entry

### 22. Known-defect exemplars must be compared with sub-10-millisecond latency from memory. What should be used?

Domain: Develop AI solutions by using Azure data management services

- A. Use a distributed lock in Redis to make processing idempotent
- B. Create a vector index in Managed Redis for similarity search
- C. Store user session state in Managed Redis with an expiry
- D. Cache responses in Azure Managed Redis

### 23. A NoSQL writer must use the supported SDK and apply related documents atomically within a partition. Which two features are required? Select two.

Domain: Develop AI solutions by using Azure data management services

- A. Batch related writes in a transactional batch within one partition key
- B. Enable duplicate detection on the queue
- C. Query through the Cosmos DB SDK with parameterized queries
- D. Enable autoscale throughput with a maximum RU limit
- E. Use a lease container to coordinate change feed readers

### 24. A memory-limited database must still serve vector search, and large sorts spill to disk. Which two adjustments apply? Select two.

Domain: Develop AI solutions by using Azure data management services

- A. Create an HNSW index for low-latency approximate search
- B. Create an IVFFlat index to save memory on a large table
- C. Increase maintenance and query memory settings for index builds and sorts
- D. Increase storage throughput for index builds and bulk loads
- E. Query without a vector index and let PostgreSQL scan the table

### 25. Which sequence correctly prepares an inspection container for similarity search?

Domain: Develop AI solutions by using Azure data management services

- A. Upsert items with embeddings → create the container with a vector policy → apply metadata filters → query with VectorDistance
- B. Query with VectorDistance → upsert items with embeddings → create the container with a vector policy → apply metadata filters
- C. Create the container with a vector policy → upsert items with embeddings → query with VectorDistance → apply metadata filters
- D. Apply metadata filters → query with VectorDistance → create the container with a vector policy → upsert items with embeddings

### 26. Each captured image must be inspected by exactly one worker, with recovery if a worker crashes. What should be used?

Domain: Connect to and consume Azure services

- A. Stream telemetry through Azure Event Hubs
- B. Publish to a Service Bus topic with multiple subscriptions
- C. Queue the work on a Service Bus queue and process it with a worker
- D. Use Azure Queue Storage for the work items

### 27. Readings for one machine must be handled in order by a single consumer. What should be enabled?

Domain: Connect to and consume Azure services

- A. Enable duplicate detection on the queue
- B. Use Service Bus sessions to keep related messages ordered
- C. Receive with peek-lock and complete or abandon explicitly
- D. Set a maximum delivery count and handle the dead-letter path

### 28. Quality, maintenance, and audit systems must each receive the same defect event independently. What should be used?

Domain: Connect to and consume Azure services

- A. Queue the work on a Service Bus queue and process it with a worker
- B. Define a custom event schema for the topic
- C. Use Azure Queue Storage for the work items
- D. Publish to a Service Bus topic with multiple subscriptions

### 29. A maintenance webhook is briefly unavailable and events must not be lost permanently. What should be configured?

Domain: Connect to and consume Azure services

- A. Filter the Event Grid subscription by subject or event type
- B. Rely on Event Grid retries with a dead-letter destination
- C. Deliver events by using a managed identity instead of a key
- D. Define a custom event schema for the topic

### 30. A function must run when an inspection result is queued, without a polling loop in code. What should be configured?

Domain: Connect to and consume Azure services

- A. Expose the endpoint through an HTTP trigger
- B. Bind a queue or event trigger to the function
- C. Use input and output bindings instead of hand-written SDK calls
- D. Orchestrate the multi-step workflow with Durable Functions

### 31. The function must write its result to Cosmos DB with as little client code as possible. What should be used?

Domain: Connect to and consume Azure services

- A. Bind a queue or event trigger to the function
- B. Host the function app on a premium plan with pre-warmed instances
- C. Orchestrate the multi-step workflow with Durable Functions
- D. Use input and output bindings instead of hand-written SDK calls

### 32. The inspection function must avoid cold starts and reach a private dependency. Which hosting choice fits?

Domain: Connect to and consume Azure services

- A. Use a deployment slot on the function app for staging
- B. Orchestrate the multi-step workflow with Durable Functions
- C. Host the function app on a premium plan with pre-warmed instances
- D. Host the function app on the consumption plan

### 33. Defect events must reach two systems independently, and one of them only wants severe defects. Which two features are required? Select two.

Domain: Connect to and consume Azure services

- A. Queue the work on a Service Bus queue and process it with a worker
- B. Use Azure Queue Storage for the work items
- C. Publish to a Service Bus topic with multiple subscriptions
- D. Filter the Event Grid subscription by subject or event type
- E. Add a SQL or correlation filter to a subscription

### 34. A multi-step rework workflow must resume after a host restart and must start from a queue event. Which two features are required? Select two.

Domain: Connect to and consume Azure services

- A. Bind a queue or event trigger to the function
- B. Host the function app on the consumption plan
- C. Expose the endpoint through an HTTP trigger
- D. Orchestrate the multi-step workflow with Durable Functions
- E. Use input and output bindings instead of hand-written SDK calls

### 35. Which sequence correctly processes an inspection message?

Domain: Connect to and consume Azure services

- A. Receive with peek-lock → publish the message → complete the message → process the work → dead-letter after the delivery limit
- B. Publish the message → receive with peek-lock → process the work → complete the message → dead-letter after the delivery limit
- C. Publish the message → complete the message → receive with peek-lock → process the work → dead-letter after the delivery limit
- D. Process the work → receive with peek-lock → publish the message → complete the message → dead-letter after the delivery limit

### 36. A camera vendor token must be auditable and revocable without an image rebuild. Where should it live?

Domain: Secure, monitor, troubleshoot Azure solutions

- A. Store settings and feature flags in Azure App Configuration
- B. Supply configuration through App Service application settings
- C. Store the secret in Azure Key Vault and read it at runtime
- D. Pin the application to a specific secret version

### 37. The vault reference fails for a workload identity that has no vault role. What should be added?

Domain: Secure, monitor, troubleshoot Azure solutions

- A. Assign a least-privilege role to the application identity
- B. Enable purge protection and soft delete on the vault
- C. Grant the app identity data-plane access to the vault
- D. Authenticate with a managed identity instead of a stored key

### 38. Defect thresholds must change per plant without redeploying the container. What should be used?

Domain: Secure, monitor, troubleshoot Azure solutions

- A. Enable configuration refresh so changes apply without a restart
- B. Store settings and feature flags in Azure App Configuration
- C. Store the secret in Azure Key Vault and read it at runtime
- D. Use App Configuration labels to separate environments

### 39. A threshold update is only noticed after a pod restart. What should be enabled?

Domain: Secure, monitor, troubleshoot Azure solutions

- A. Use App Configuration labels to separate environments
- B. Pin the application to a specific secret version
- C. Enable configuration refresh so changes apply without a restart
- D. Deploy the function app through a CI pipeline with app settings applied

### 40. A captured image is processed by an API, a queue, and a function, and the team needs one connected trace. What should be implemented?

Domain: Secure, monitor, troubleshoot Azure solutions

- A. Send telemetry to Application Insights and inspect the transaction view
- B. Enable diagnostic settings to route platform logs to the workspace
- C. Instrument the service with the OpenTelemetry SDK
- D. Query the workspace with KQL to find the failing operation

### 41. A deployment pipeline identity can change cluster settings but the application only reads secrets. What should be done?

Domain: Secure, monitor, troubleshoot Azure solutions

- A. Assign a least-privilege role to the application identity
- B. Store the secret in Azure Key Vault and read it at runtime
- C. Authenticate with a managed identity instead of a stored key
- D. Reach the data service through a private endpoint

### 42. Traces must connect the API, queue, and function hops and must not lose the correlation across messaging. Which two practices are required? Select two.

Domain: Secure, monitor, troubleshoot Azure solutions

- A. Query the workspace with KQL to find the failing operation
- B. Use head or tail sampling so trace volume stays within budget
- C. Enable diagnostic settings to route platform logs to the workspace
- D. Propagate trace context across every service and queue hop
- E. Instrument the service with the OpenTelemetry SDK

### 43. A secret must be stored centrally and read by the workload with no stored credential. Which two actions should you take? Select two.

Domain: Secure, monitor, troubleshoot Azure solutions

- A. Authenticate with a managed identity instead of a stored key
- B. Store settings and feature flags in Azure App Configuration
- C. Store the secret in Azure Key Vault and read it at runtime
- D. Use App Configuration labels to separate environments
- E. Pin the application to a specific secret version

### 44. Which sequence correctly introduces a rotated camera token?

Domain: Secure, monitor, troubleshoot Azure solutions

- A. Store the secret in Key Vault → grant the app identity access → reference the secret from the app → rotate the secret → the app reads the new version
- B. Rotate the secret → reference the secret from the app → store the secret in Key Vault → grant the app identity access → the app reads the new version
- C. Grant the app identity access → store the secret in Key Vault → rotate the secret → reference the secret from the app → the app reads the new version
- D. Reference the secret from the app → rotate the secret → store the secret in Key Vault → grant the app identity access → the app reads the new version

### 45. Base images must be checked for known vulnerabilities before a line-side build can be promoted. What should be added to the pipeline?

Domain: Develop containerized solutions on Azure

- A. Scan images on push and block vulnerable builds in the pipeline
- B. Deploy the mutable latest tag and let the platform resolve it
- C. Apply an ACR retention policy to prune old untagged manifests
- D. Run image builds on demand or on a trigger with ACR Tasks

### 46. A station image must rebuild whenever the inspection model package changes, and no build server may be maintained. What should perform the build?

Domain: Develop containerized solutions on Azure

- A. Run image builds on demand or on a trigger with ACR Tasks
- B. Deploy the workload to Azure Kubernetes Service
- C. Build and store versioned images in Azure Container Registry
- D. Run the batch job in Azure Container Instances

### 47. A single-container inspection portal needs deployment slots and platform-managed patching without a cluster. Where should it run?

Domain: Develop containerized solutions on Azure

- A. Implement the handler as an Azure Function
- B. Deploy the image to Azure App Service as a web app
- C. Run the batch job in Azure Container Instances
- D. Deploy the workload to Azure Kubernetes Service

### 48. The portal must be verified in production configuration and rolled back instantly if the first requests fail. What should be used?

Domain: Develop containerized solutions on Azure

- A. Stage the change in a deployment slot and swap after verification
- B. Replicate the registry to each deployment region
- C. Create a new Container Apps revision and shift traffic between revisions
- D. Rely on the horizontal pod autoscaler on CPU

### 49. Line-side APIs are idle between shifts and need revisions without a cluster to administer. Where should they run?

Domain: Develop containerized solutions on Azure

- A. Deploy the service to Azure Container Apps
- B. Deploy the image to Azure App Service as a web app
- C. Deploy the workload to Azure Kubernetes Service
- D. Run the batch job in Azure Container Instances

### 50. Station names and tolerances change weekly on the cluster and must not require a new image. What should supply them?

Domain: Develop containerized solutions on Azure

- A. Pin the application to a specific secret version
- B. Supply configuration through App Service application settings
- C. Reference a Key Vault secret from the app configuration instead of storing it
- D. Mount non-secret configuration from a Kubernetes ConfigMap

### 51. The application container needs a 900 MB model artifact downloaded before it can start. What should be added?

Domain: Develop containerized solutions on Azure

- A. Apply a declarative Kubernetes manifest to the cluster
- B. Run startup prerequisites in an init container
- C. Rely on the horizontal pod autoscaler on CPU
- D. Add readiness and liveness probes to the pod specification

### 52. Deployments, services, and probes must be declared in Git and reapplied safely after manual drift. What should be used?

Domain: Develop containerized solutions on Azure

- A. Run image builds on demand or on a trigger with ACR Tasks
- B. Apply a declarative Kubernetes manifest to the cluster
- C. Run the batch job in Azure Container Instances
- D. Rely on the horizontal pod autoscaler on CPU

### 53. Inspection pods restart during the night shift and the exit reason is not visible on the node. Where should it be looked up?

Domain: Develop containerized solutions on Azure

- A. Query container logs and Kubernetes events in Log Analytics
- B. Enable diagnostic settings to route platform logs to the workspace
- C. Add readiness and liveness probes to the pod specification
- D. Aggregate with summarize and bin to see the failure rate over time

### 54. A station deployment must be reproducible from Git and must not accept traffic before the model is loaded. Which two elements belong in the manifest? Select two.

Domain: Develop containerized solutions on Azure

- A. Add readiness and liveness probes to the pod specification
- B. Scale only on CPU utilization without an event scaler
- C. Apply a declarative Kubernetes manifest to the cluster
- D. Rely on the horizontal pod autoscaler on CPU
- E. Run the batch job in Azure Container Instances

### 55. Which sequence correctly deploys a station workload from a manifest and proves it is reachable?

Domain: Develop containerized solutions on Azure

- A. Wait for pod readiness → apply the manifest → write the manifest → test ingress connectivity
- B. Apply the manifest → write the manifest → test ingress connectivity → wait for pod readiness
- C. Write the manifest → apply it to the cluster → wait for pod readiness → test ingress connectivity
- D. Write the manifest → test ingress connectivity → apply it to the cluster → wait for pod readiness

### 56. Inspection results must be stored as JSON per station with point reads by result identifier and per-plant isolation. Which store fits?

Domain: Develop AI solutions by using Azure data management services

- A. Use Azure Queue Storage for the work items
- B. Include the partition key in the query predicate
- C. Store embeddings in PostgreSQL by using the pgvector extension
- D. Store the documents in Azure Cosmos DB for NoSQL

### 57. Inspection telemetry writes are expensive, and queries filter on only three of its thirty properties. What should be changed?

Domain: Develop AI solutions by using Azure data management services

- A. Restrict the indexing policy to the paths the queries use
- B. Enable autoscale throughput with a maximum RU limit
- C. Index every property by using the default automatic policy
- D. Add a composite index for the filtered and ordered properties

### 58. A line dashboard tolerates five seconds of lag, and the team wants the read guarantee documented rather than inherited from a default. What should be chosen deliberately?

Domain: Develop AI solutions by using Azure data management services

- A. Choose the account consistency level that matches the read requirement
- B. Use eventual consistency to minimize read cost
- C. Use session consistency for reads within the same client session
- D. Use strong consistency for every read in the account

### 59. Inspection notes and their embeddings must be searched together with line and shift filters in one query. What should be used?

Domain: Develop AI solutions by using Azure data management services

- A. Scan every document and compute similarity in application code
- B. Store embeddings in PostgreSQL by using the pgvector extension
- C. Store embeddings in a vector property and query with VectorDistance
- D. Use the DiskANN vector index for large collections

### 60. Every new defect record must reach the alerting pipeline without polling the container. What should be implemented?

Domain: Develop AI solutions by using Azure data management services

- A. Run a change feed processor to react to new and updated items
- B. Enable duplicate detection on the queue
- C. Set an item time-to-live on the container
- D. Use a lease container to coordinate change feed readers

### 61. Measurements and embeddings must be filtered by station and shift beside a vector predicate in one statement. How should the table be modeled?

Domain: Develop AI solutions by using Azure data management services

- A. Model typed columns for filters and one vector column for the embedding
- B. Increase storage throughput for index builds and bulk loads
- C. Add a read replica and send all vector queries to it
- D. Scale compute and memory to fit index size and query concurrency

### 62. Every station opens a database connection for each image and the server runs out of sessions at shift change. What should the service use?

Domain: Develop AI solutions by using Azure data management services

- A. Reuse a bounded connection pool instead of opening a connection per request
- B. Use prepared statements and batch round trips
- C. Place a connection pooler in front of PostgreSQL for many short-lived clients
- D. Increase storage throughput for index builds and bulk loads

### 63. Every station dashboard request recomputes the same defect aggregates for the current shift. What should be added?

Domain: Develop AI solutions by using Azure data management services

- A. Add a read replica and send all vector queries to it
- B. Set a TTL on each cached entry
- C. Use Azure Queue Storage for the work items
- D. Cache responses in Azure Managed Redis

### 64. Nearest-defect lookup must answer within ten milliseconds and cannot call the relational database on the hot path. What should be built?

Domain: Develop AI solutions by using Azure data management services

- A. Create a vector index in Managed Redis for similarity search
- B. Use a distributed lock in Redis to make processing idempotent
- C. Cache responses in Azure Managed Redis
- D. Store user session state in Managed Redis with an expiry

### 65. A result browser must query through the supported SDK and must not buffer an entire plant's history. Which two actions should you take? Select two.

Domain: Develop AI solutions by using Azure data management services

- A. Page large result sets with the continuation token
- B. Query through the Cosmos DB SDK with parameterized queries
- C. Index every property by using the default automatic policy
- D. Scan every document and compute similarity in application code
- E. Include the partition key in the query predicate

### 66. Cached aggregates must expire on their own and must never survive a completed shift rollover unchanged. Which two settings are required? Select two.

Domain: Develop AI solutions by using Azure data management services

- A. Flush the database after each deployment to guarantee fresh data
- B. Use a distributed lock in Redis to make processing idempotent
- C. Set a TTL on each cached entry
- D. Rely on the eviction policy and skip explicit TTLs
- E. Invalidate or overwrite the cache entry when the source changes

### 67. Which sequence correctly adds a read-through cache for station aggregates?

Domain: Develop AI solutions by using Azure data management services

- A. Invalidate the entry when the source changes → write the value with a TTL → check the cache → serve the next request → on a miss query the source
- B. Write the value with a TTL → check the cache → on a miss query the source → invalidate the entry → serve the next request from the cache
- C. Check the cache → on a miss query the source → write the value with a TTL → invalidate the entry when the source changes → serve the next request from the cache
- D. On a miss query the source → check the cache → write the value with a TTL → serve the next request → invalidate the entry when the source changes

### 68. Only defects with severity high should reach the escalation subscription, while every defect reaches the archive. What should be configured?

Domain: Connect to and consume Azure services

- A. Add a SQL or correlation filter to a subscription
- B. Enable duplicate detection on the queue
- C. Filter the Event Grid subscription by subject or event type
- D. Define a custom event schema for the topic

### 69. Images that cannot be decoded must be preserved for later inspection instead of retried forever. Where should they end up?

Domain: Connect to and consume Azure services

- A. Inspect the dead-letter queue and resubmit corrected messages
- B. Use prepared statements and batch round trips
- C. Enable duplicate detection on the queue
- D. Receive in receive-and-delete mode for at-most-once delivery

### 70. A repeated image event must not create a second defect record for the same capture. What should the handler use?

Domain: Connect to and consume Azure services

- A. Receive in receive-and-delete mode for at-most-once delivery
- B. Receive with peek-lock and complete or abandon explicitly
- C. Enable duplicate detection on the queue
- D. Make the handler idempotent by using a message or business key

### 71. A new image in the station container must start inspection without a polling loop or a custom publisher. What should be used?

Domain: Connect to and consume Azure services

- A. Use Azure Queue Storage for the work items
- B. Publish the state change as an Event Grid event
- C. Stream telemetry through Azure Event Hubs
- D. Orchestrate the multi-step workflow with Durable Functions

### 72. A queued image message must start the inspection function automatically. What should be configured?

Domain: Connect to and consume Azure services

- A. Expose the endpoint through an HTTP trigger
- B. Bind a queue or event trigger to the function
- C. Orchestrate the multi-step workflow with Durable Functions
- D. Use input and output bindings instead of hand-written SDK calls

### 73. The inspection handler must write its result to Cosmos DB without constructing a client or connection in code. What should be used?

Domain: Connect to and consume Azure services

- A. Bind a queue or event trigger to the function
- B. Orchestrate the multi-step workflow with Durable Functions
- C. Use input and output bindings instead of hand-written SDK calls
- D. Expose the endpoint through an HTTP trigger

### 74. Inspection must reach a private model endpoint and must avoid cold starts during shift changes. Which hosting plan fits?

Domain: Connect to and consume Azure services

- A. Host the function app on the consumption plan
- B. Expose the endpoint through an HTTP trigger
- C. Orchestrate the multi-step workflow with Durable Functions
- D. Host the function app on a premium plan with pre-warmed instances

### 75. A queue-triggered inspection function overwhelms the model endpoint during shift changes. What should be tuned?

Domain: Connect to and consume Azure services

- A. Host the function app on a premium plan with pre-warmed instances
- B. Tune the function app concurrency and batch size
- C. Configure the host retry policy with exponential backoff
- D. Host the function app on the consumption plan

### 76. Each defect must reach both the archive and the escalation path, and escalation must receive only severe defects. Which two features are required? Select two.

Domain: Connect to and consume Azure services

- A. Queue the work on a Service Bus queue and process it with a worker
- B. Add a SQL or correlation filter to a subscription
- C. Use Azure Queue Storage for the work items
- D. Filter the Event Grid subscription by subject or event type
- E. Publish to a Service Bus topic with multiple subscriptions

### 77. An inspection function must call Cosmos DB without a stored key and must ship code and settings together. Which two actions should you take? Select two.

Domain: Connect to and consume Azure services

- A. Supply configuration through App Service application settings
- B. Assign a managed identity to the function app and use it for downstream calls
- C. Deploy the function app through a CI pipeline with app settings applied
- D. Expose the endpoint through an HTTP trigger
- E. Host the function app on a premium plan with pre-warmed instances

### 78. Which sequence correctly routes a custom defect event to the escalation handler?

Domain: Connect to and consume Azure services

- A. Publish a custom event → deliver to the handler → evaluate the subscription filter → dead-letter undeliverable events → retry on failure
- B. Evaluate the subscription filter → publish a custom event → dead-letter undeliverable events → deliver to the handler → retry on failure
- C. Deliver to the handler → publish a custom event → evaluate the subscription filter → retry on failure → dead-letter undeliverable events
- D. Publish a custom event → evaluate the subscription filter → deliver to the handler → retry on failure → dead-letter undeliverable events

### 79. The model endpoint key must be stored with version history and access audit in a managed service. Where should it live?

Domain: Secure, monitor, troubleshoot Azure solutions

- A. Assign a least-privilege role to the application identity
- B. Store settings and feature flags in Azure App Configuration
- C. Store the secret in Azure Key Vault and read it at runtime
- D. Reference a Key Vault secret from the app configuration instead of storing it

### 80. The model endpoint key must change every thirty days without redeploying the inspection function. What should be configured?

Domain: Secure, monitor, troubleshoot Azure solutions

- A. Enable purge protection and soft delete on the vault
- B. Pin the application to a specific secret version
- C. Rotate the secret on a schedule and let apps resolve the current version
- D. Authenticate with a managed identity instead of a stored key

### 81. All plants need shared feature flags with one place to change them and a label per plant. What should be introduced?

Domain: Secure, monitor, troubleshoot Azure solutions

- A. Enable configuration refresh so changes apply without a restart
- B. Reference the Key Vault secret from an App Configuration key value
- C. Use App Configuration labels to separate environments
- D. Store settings and feature flags in Azure App Configuration

### 82. One capture must be traceable through the queue, the function, and the model call instead of ending at the first hop. What should be added?

Domain: Secure, monitor, troubleshoot Azure solutions

- A. Query the workspace with KQL to find the failing operation
- B. Send telemetry to Application Insights and inspect the transaction view
- C. Correlate logs with the operation or trace identifier
- D. Instrument the service with the OpenTelemetry SDK

### 83. One station reports intermittent inspection failures and the team needs the exact failing operation. What should be used?

Domain: Secure, monitor, troubleshoot Azure solutions

- A. Aggregate with summarize and bin to see the failure rate over time
- B. Join the requests and dependencies tables on the operation ID
- C. Alert on platform metrics rather than only on log queries
- D. Query the workspace with KQL to find the failing operation

### 84. The function must call Cosmos DB with no key or connection string in configuration. What should be configured?

Domain: Secure, monitor, troubleshoot Azure solutions

- A. Enable purge protection and soft delete on the vault
- B. Reference a Key Vault secret from the app configuration instead of storing it
- C. Authenticate with a managed identity instead of a stored key
- D. Pin the application to a specific secret version

### 85. The team needs the inspection failure rate per five-minute bucket and must keep query cost low. Which two practices should be used? Select two.

Domain: Secure, monitor, troubleshoot Azure solutions

- A. Set the workspace retention and table plan to control log cost
- B. Store repeated aggregations in a materialized view or update policy
- C. Project only the columns needed and filter by time first
- D. Join the requests and dependencies tables on the operation ID
- E. Aggregate with summarize and bin to see the failure rate over time

### 86. A new defect threshold must ship before it is enabled and must apply without restarting the function app. Which two features are required? Select two.

Domain: Secure, monitor, troubleshoot Azure solutions

- A. Enable configuration refresh so changes apply without a restart
- B. Use App Configuration labels to separate environments
- C. Ship the code dark behind a feature flag
- D. Pin the application to a specific secret version
- E. Reference the Key Vault secret from an App Configuration key value

### 87. A function must read plant secrets and the vault must survive accidental deletion. Which two actions should you take? Select two.

Domain: Secure, monitor, troubleshoot Azure solutions

- A. Grant the app identity data-plane access to the vault
- B. Enable purge protection and soft delete on the vault
- C. Pin the application to a specific secret version
- D. Store the secret in Azure Key Vault and read it at runtime
- E. Rotate the secret on a schedule and let apps resolve the current version

### 88. Which sequence correctly gives a new inspection function identity-based vault access and deploys it?

Domain: Secure, monitor, troubleshoot Azure solutions

- A. Grant the identity access to the vault → create the function app with a managed identity → deploy through the pipeline → reference the secret in application settings → verify a queue-triggered invocation
- B. Reference the secret in application settings → verify a queue-triggered invocation → create the function app with a managed identity → grant the identity access to the vault → deploy through the pipeline
- C. Create the function app with a managed identity → grant the identity access to the vault → reference the secret in application settings → deploy through the pipeline → verify a queue-triggered invocation
- D. Deploy through the pipeline → reference the secret in application settings → create the function app with a managed identity → grant the identity access to the vault → verify a queue-triggered invocation

---

## Case study — Apex Motors

The next three questions refer to this scenario. Read the full scenario before answering; case-study items are scored individually.

### 89. Recall collapses when six inspection queries run at once because the index no longer fits in memory. What should be addressed?

Domain: Develop AI solutions by using Azure data management services

- A. Scale compute and memory to fit index size and query concurrency
- B. Run VACUUM and ANALYZE after bulk loads and large deletes
- C. Add a read replica and send all vector queries to it
- D. Increase storage throughput for index builds and bulk loads

### 90. Retrieval must return only chunks from the requesting plant and must still return five passages. What should the query do?

Domain: Develop AI solutions by using Azure data management services

- A. Retrieve nearest neighbours first and discard unauthorized rows in the application
- B. Filter on metadata columns in the same query as the vector search
- C. Create an HNSW index for low-latency approximate search
- D. Create an IVFFlat index to save memory on a large table

### 91. The model call dominates inspection latency, but the transaction view shows no span for it. What should be added?

Domain: Secure, monitor, troubleshoot Azure solutions

- A. Correlate logs with the operation or trace identifier
- B. Propagate trace context across every service and queue hop
- C. Instrument the service with the OpenTelemetry SDK
- D. Create a custom span around each downstream call

---

## Case study — Contoso Assembly

The next three questions refer to this scenario. Read the full scenario before answering; case-study items are scored individually.

### 92. Reviewers must see only defects from their own plant while still receiving a full list of matches. What should the query do?

Domain: Develop AI solutions by using Azure data management services

- A. Retrieve nearest neighbours first and discard unauthorized rows in the application
- B. Query without a vector index and let PostgreSQL scan the table
- C. Create an HNSW index for low-latency approximate search
- D. Filter on metadata columns in the same query as the vector search

### 93. A corrupt image reference repeatedly fails inspection and must be preserved for analysis. What should happen to it?

Domain: Connect to and consume Azure services

- A. Set a maximum delivery count and handle the dead-letter path
- B. Enable duplicate detection on the queue
- C. Receive in receive-and-delete mode for at-most-once delivery
- D. Inspect the dead-letter queue and resubmit corrected messages

### 94. The team needs rejection counts per fifteen-minute interval during a shift. Which construct should be used?

Domain: Secure, monitor, troubleshoot Azure solutions

- A. Project only the columns needed and filter by time first
- B. Aggregate with summarize and bin to see the failure rate over time
- C. Store repeated aggregations in a materialized view or update policy
- D. Join the requests and dependencies tables on the operation ID

---

## Case study — Fabrikam Plant

The next three questions refer to this scenario. Read the full scenario before answering; case-study items are scored individually.

### 95. Pods cannot open a connection to the storage account, though the same test succeeds from a workstation. What should be verified?

Domain: Develop containerized solutions on Azure

- A. Add readiness and liveness probes to the pod specification
- B. Reach the data service through a private endpoint
- C. Link the private DNS zone so the private endpoint name resolves
- D. Test end-to-end connectivity from inside the container to each dependency

### 96. Only events for a specific production line should reach the maintenance handler. What should be configured?

Domain: Connect to and consume Azure services

- A. Enable duplicate detection on the queue
- B. Add a SQL or correlation filter to a subscription
- C. Rely on Event Grid retries with a dead-letter destination
- D. Filter the Event Grid subscription by subject or event type

### 97. An operator needs the slowest inspection operations in the last hour with their durations. Which tool should be used?

Domain: Secure, monitor, troubleshoot Azure solutions

- A. Query the workspace with KQL to find the failing operation
- B. Project only the columns needed and filter by time first
- C. Aggregate with summarize and bin to see the failure rate over time
- D. Alert on platform metrics rather than only on log queries

---

## Case study — Ironworks Plant

The next three questions refer to this scenario. Read the full scenario before answering; case-study items are scored individually.

### 98. Station workers must follow the number of queued images, and the queue is empty between shifts. What should drive replicas?

Domain: Develop containerized solutions on Azure

- A. Rely on the horizontal pod autoscaler on CPU
- B. Scale on the Service Bus queue length with a KEDA Azure Service Bus scaler
- C. Scale only on CPU utilization without an event scaler
- D. Run the batch job in Azure Container Instances

### 99. Similar-defect search across a million historical images must answer in tens of milliseconds. Which index fits?

Domain: Develop AI solutions by using Azure data management services

- A. Create an HNSW index for low-latency approximate search
- B. Query without a vector index and let PostgreSQL scan the table
- C. Create an IVFFlat index to save memory on a large table
- D. Place a connection pooler in front of PostgreSQL for many short-lived clients

### 100. Images from one station must be processed in the order they were captured. What should be enabled?

Domain: Connect to and consume Azure services

- A. Set a maximum delivery count and handle the dead-letter path
- B. Receive with peek-lock and complete or abandon explicitly
- C. Enable duplicate detection on the queue
- D. Use Service Bus sessions to keep related messages ordered

---

## Answer key and explanations

### Question 1 — B

Answer: Replicate the registry to each deployment region. Geo-replication keeps a registry copy in each plant region, so pulls stay local. Geo-replication reduces cross-region pull latency and gives a local copy during a regional failure. It adds cost and replication management. Local study-map skill 1.1 (Container Image Lifecycle in Azure Container Registry), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure container hosting documentation: https://learn.microsoft.com/en-us/azure/container-apps/

- **A:** Incorrect for this question. A floating tag removes the link between a deployed revision and a specific build, so rollback and audit become guesswork. Why the correct answer wins: Geo-replication keeps a registry copy in each plant region, so pulls stay local.
- **B:** Correct. Geo-replication reduces cross-region pull latency and gives a local copy during a regional failure. It adds cost and replication management. In this case: Geo-replication keeps a registry copy in each plant region, so pulls stay local.
- **C:** Incorrect for this question. A retention policy controls storage growth and registry clutter. It does not change which image tag a deployment references. Why the correct answer wins: Geo-replication keeps a registry copy in each plant region, so pulls stay local.
- **D:** Incorrect for this question. ACR Tasks builds images in Azure on a commit or schedule without a local Docker host. It removes build-host drift but not image review. Why the correct answer wins: Geo-replication keeps a registry copy in each plant region, so pulls stay local.

### Question 2 — D

Answer: Apply an ACR retention policy to prune old untagged manifests. A retention policy prunes unused manifests while keeping referenced tags. A retention policy controls storage growth and registry clutter. It does not change which image tag a deployment references. Local study-map skill 1.1 (Container Image Lifecycle in Azure Container Registry), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure container hosting documentation: https://learn.microsoft.com/en-us/azure/container-apps/

- **A:** Incorrect for this question. ACR Tasks builds images in Azure on a commit or schedule without a local Docker host. It removes build-host drift but not image review. Why the correct answer wins: A retention policy prunes unused manifests while keeping referenced tags.
- **B:** Incorrect for this question. Geo-replication reduces cross-region pull latency and gives a local copy during a regional failure. It adds cost and replication management. Why the correct answer wins: A retention policy prunes unused manifests while keeping referenced tags.
- **C:** Incorrect for this question. A floating tag removes the link between a deployed revision and a specific build, so rollback and audit become guesswork. Why the correct answer wins: A retention policy prunes unused manifests while keeping referenced tags.
- **D:** Correct. A retention policy controls storage growth and registry clutter. It does not change which image tag a deployment references. In this case: A retention policy prunes unused manifests while keeping referenced tags.

### Question 3 — A

Answer: Run image builds on demand or on a trigger with ACR Tasks. An ACR Task triggered by the source commit builds the image inside Azure. ACR Tasks builds images in Azure on a commit or schedule without a local Docker host. It removes build-host drift but not image review. Local study-map skill 1.2 (Automated Image Builds with ACR Tasks), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure container hosting documentation: https://learn.microsoft.com/en-us/azure/container-apps/

- **A:** Correct. ACR Tasks builds images in Azure on a commit or schedule without a local Docker host. It removes build-host drift but not image review. In this case: An ACR Task triggered by the source commit builds the image inside Azure.
- **B:** Incorrect for this question. Container Instances starts a single container group quickly for short tasks. It has no orchestrator-level scaling or revision model. Why the correct answer wins: An ACR Task triggered by the source commit builds the image inside Azure.
- **C:** Incorrect for this question. A slot swap warms the new version before it takes production traffic and makes rollback a second swap. Slot-local settings must be marked sticky. Why the correct answer wins: An ACR Task triggered by the source commit builds the image inside Azure.
- **D:** Incorrect for this question. ACR keeps tagged, versioned images next to the deployment target and supports identity-based pulls. Tagging strategy and retention still need a decision. Why the correct answer wins: An ACR Task triggered by the source commit builds the image inside Azure.

### Question 4 — B

Answer: Supply configuration through App Service application settings. Application settings inject per-environment configuration at runtime. Application settings become environment variables for the container and can be swapped per slot. Sensitive values should still reference a vault. Local study-map skill 1.3 (Container Deployment to Azure App Service), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure container hosting documentation: https://learn.microsoft.com/en-us/azure/container-apps/

- **A:** Incorrect for this question. A Key Vault reference resolves at runtime so the secret is never written into application settings. The app identity still needs permission to read it. Why the correct answer wins: Application settings inject per-environment configuration at runtime.
- **B:** Correct. Application settings become environment variables for the container and can be swapped per slot. Sensitive values should still reference a vault. In this case: Application settings inject per-environment configuration at runtime.
- **C:** Incorrect for this question. A slot swap warms the new version before it takes production traffic and makes rollback a second swap. Slot-local settings must be marked sticky. Why the correct answer wins: Application settings inject per-environment configuration at runtime.
- **D:** Incorrect for this question. App Service runs a container with managed patching, deployment slots, and built-in authentication options. It is not a Kubernetes control plane. Why the correct answer wins: Application settings inject per-environment configuration at runtime.

### Question 5 — D

Answer: Stage the change in a deployment slot and swap after verification. A slot swap warms the new version and makes rollback a second swap. A slot swap warms the new version before it takes production traffic and makes rollback a second swap. Slot-local settings must be marked sticky. Local study-map skill 1.3 (Container Deployment to Azure App Service), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure container hosting documentation: https://learn.microsoft.com/en-us/azure/container-apps/

- **A:** Incorrect for this question. Revision-based traffic splitting enables canary and blue-green releases. Revision mode and scale rules must be set deliberately. Why the correct answer wins: A slot swap warms the new version and makes rollback a second swap.
- **B:** Incorrect for this question. Application settings become environment variables for the container and can be swapped per slot. Sensitive values should still reference a vault. Why the correct answer wins: A slot swap warms the new version and makes rollback a second swap.
- **C:** Incorrect for this question. A floating tag removes the link between a deployed revision and a specific build, so rollback and audit become guesswork. Why the correct answer wins: A slot swap warms the new version and makes rollback a second swap.
- **D:** Correct. A slot swap warms the new version before it takes production traffic and makes rollback a second swap. Slot-local settings must be marked sticky. In this case: A slot swap warms the new version and makes rollback a second swap.

### Question 6 — C

Answer: Scale the container app on an event source with a KEDA scaler. A KEDA queue scaler follows backlog depth and can scale to zero. KEDA scalers drive replica count from queue length, lag, or other event metrics, including scale to zero. Cool-down and max replicas bound the behavior. Local study-map skill 1.5 (Event-Driven Scaling with KEDA), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure container hosting documentation: https://learn.microsoft.com/en-us/azure/container-apps/

- **A:** Incorrect for this question. Container Instances starts a single container group quickly for short tasks. It has no orchestrator-level scaling or revision model. Why the correct answer wins: A KEDA queue scaler follows backlog depth and can scale to zero.
- **B:** Incorrect for this question. HPA adjusts replicas from resource metrics but needs metrics-server and enough node capacity. It cannot scale to zero. Why the correct answer wins: A KEDA queue scaler follows backlog depth and can scale to zero.
- **C:** Correct. KEDA scalers drive replica count from queue length, lag, or other event metrics, including scale to zero. Cool-down and max replicas bound the behavior. In this case: A KEDA queue scaler follows backlog depth and can scale to zero.
- **D:** Incorrect for this question. CPU-based scaling reacts after work is already queued and cannot scale to zero on an empty queue. It suits steady request-driven services. Why the correct answer wins: A KEDA queue scaler follows backlog depth and can scale to zero.

### Question 7 — B

Answer: Apply a declarative Kubernetes manifest to the cluster. A declarative manifest describes desired state and is idempotent when reapplied. A manifest declares the desired deployment, service, and probe configuration in version control. Applying it repeatedly is idempotent. Local study-map skill 1.6 (AKS Deployment with Manifests), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure container hosting documentation: https://learn.microsoft.com/en-us/azure/container-apps/

- **A:** Incorrect for this question. ACR Tasks builds images in Azure on a commit or schedule without a local Docker host. It removes build-host drift but not image review. Why the correct answer wins: A declarative manifest describes desired state and is idempotent when reapplied.
- **B:** Correct. A manifest declares the desired deployment, service, and probe configuration in version control. Applying it repeatedly is idempotent. In this case: A declarative manifest describes desired state and is idempotent when reapplied.
- **C:** Incorrect for this question. Readiness gates traffic until the app can serve it, and liveness restarts a wedged container. Wrong thresholds cause restart loops. Why the correct answer wins: A declarative manifest describes desired state and is idempotent when reapplied.
- **D:** Incorrect for this question. HPA adjusts replicas from resource metrics but needs metrics-server and enough node capacity. It cannot scale to zero. Why the correct answer wins: A declarative manifest describes desired state and is idempotent when reapplied.

### Question 8 — C

Answer: Query container logs and Kubernetes events in Log Analytics. Log Analytics collects container logs and platform events for KQL analysis. Container Apps and AKS surface stdout logs and platform events into a workspace for KQL analysis. Verbosity and retention cost money. Local study-map skill 1.7 (Container Logs, Events, and Connectivity), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure container hosting documentation: https://learn.microsoft.com/en-us/azure/container-apps/

- **A:** Incorrect for this question. Platform logs and metrics must be routed before they can be queried or alerted on. Retention and cost follow the workspace settings. Why the correct answer wins: Log Analytics collects container logs and platform events for KQL analysis.
- **B:** Incorrect for this question. Reaching a dependency from the pod or replica proves DNS, egress, and firewall paths together. Host-side tests can succeed while the container path fails. Why the correct answer wins: Log Analytics collects container logs and platform events for KQL analysis.
- **C:** Correct. Container Apps and AKS surface stdout logs and platform events into a workspace for KQL analysis. Verbosity and retention cost money. In this case: Log Analytics collects container logs and platform events for KQL analysis.
- **D:** Incorrect for this question. Application Insights correlates requests, dependencies, and exceptions into end-to-end transactions. Sampling can hide rare failures. Why the correct answer wins: Log Analytics collects container logs and platform events for KQL analysis.

### Question 9 — A, B

Answers: Build and store versioned images in Azure Container Registry; Run image builds on demand or on a trigger with ACR Tasks. Versioned registry tags identify artifacts, and ACR Tasks builds them in Azure on a trigger. ACR keeps tagged, versioned images next to the deployment target and supports identity-based pulls. Tagging strategy and retention still need a decision. ACR Tasks builds images in Azure on a commit or schedule without a local Docker host. It removes build-host drift but not image review. Local study-map skill 1.1 (Container Image Lifecycle in Azure Container Registry), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure container hosting documentation: https://learn.microsoft.com/en-us/azure/container-apps/

- **A:** Correct. ACR Tasks builds images in Azure on a commit or schedule without a local Docker host. It removes build-host drift but not image review. In this case: Versioned registry tags identify artifacts, and ACR Tasks builds them in Azure on a trigger.
- **B:** Correct. ACR keeps tagged, versioned images next to the deployment target and supports identity-based pulls. Tagging strategy and retention still need a decision. In this case: Versioned registry tags identify artifacts, and ACR Tasks builds them in Azure on a trigger.
- **C:** Incorrect for this question. A floating tag removes the link between a deployed revision and a specific build, so rollback and audit become guesswork. Why the correct answer wins: Versioned registry tags identify artifacts, and ACR Tasks builds them in Azure on a trigger.
- **D:** Incorrect for this question. Geo-replication reduces cross-region pull latency and gives a local copy during a regional failure. It adds cost and replication management. Why the correct answer wins: Versioned registry tags identify artifacts, and ACR Tasks builds them in Azure on a trigger.
- **E:** Incorrect for this question. A slot swap warms the new version before it takes production traffic and makes rollback a second swap. Slot-local settings must be marked sticky. Why the correct answer wins: Versioned registry tags identify artifacts, and ACR Tasks builds them in Azure on a trigger.

### Question 10 — A, B

Answers: Apply a declarative Kubernetes manifest to the cluster; Add readiness and liveness probes to the pod specification. The applied manifest makes state reproducible, and a readiness probe holds traffic until the app is ready. A manifest declares the desired deployment, service, and probe configuration in version control. Applying it repeatedly is idempotent. Readiness gates traffic until the app can serve it, and liveness restarts a wedged container. Wrong thresholds cause restart loops. Local study-map skill 1.6 (AKS Deployment with Manifests), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure container hosting documentation: https://learn.microsoft.com/en-us/azure/container-apps/

- **A:** Correct. A manifest declares the desired deployment, service, and probe configuration in version control. Applying it repeatedly is idempotent. In this case: The applied manifest makes state reproducible, and a readiness probe holds traffic until the app is ready.
- **B:** Correct. Readiness gates traffic until the app can serve it, and liveness restarts a wedged container. Wrong thresholds cause restart loops. In this case: The applied manifest makes state reproducible, and a readiness probe holds traffic until the app is ready.
- **C:** Incorrect for this question. Container Instances starts a single container group quickly for short tasks. It has no orchestrator-level scaling or revision model. Why the correct answer wins: The applied manifest makes state reproducible, and a readiness probe holds traffic until the app is ready.
- **D:** Incorrect for this question. HPA adjusts replicas from resource metrics but needs metrics-server and enough node capacity. It cannot scale to zero. Why the correct answer wins: The applied manifest makes state reproducible, and a readiness probe holds traffic until the app is ready.
- **E:** Incorrect for this question. Cool-down prevents replica flapping, and a maximum replica cap bounds cost and downstream load. Both are per-rule settings. Why the correct answer wins: The applied manifest makes state reproducible, and a readiness probe holds traffic until the app is ready.

### Question 11 — C

Answer: Write the manifest → apply it to the cluster → wait for pod readiness → test ingress connectivity. The manifest is authored and applied before readiness is checked, and connectivity is tested last. Readiness must pass before a connectivity test proves anything, and the manifest must exist before it is applied. Local study-map skill 1.6 (AKS Deployment with Manifests), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure container hosting documentation: https://learn.microsoft.com/en-us/azure/container-apps/

- **A:** Incorrect for this question. Ingress cannot be tested before the workload exists in the cluster. Why the correct answer wins: The manifest is authored and applied before readiness is checked, and connectivity is tested last.
- **B:** Incorrect for this question. Pods cannot become ready before the manifest is applied. Why the correct answer wins: The manifest is authored and applied before readiness is checked, and connectivity is tested last.
- **C:** Correct. Readiness must pass before a connectivity test proves anything, and the manifest must exist before it is applied. In this case: The manifest is authored and applied before readiness is checked, and connectivity is tested last.
- **D:** Incorrect for this question. A manifest is authored before it is applied, and connectivity is meaningless while pods are not ready. Why the correct answer wins: The manifest is authored and applied before readiness is checked, and connectivity is tested last.

### Question 12 — B

Answer: Store the documents in Azure Cosmos DB for NoSQL. Including the partition key makes the read single-partition. Cosmos DB gives globally distributed, low-latency document access with tunable consistency. Partition key and RU planning determine the cost profile. Local study-map skill 2.1 (Cosmos DB SDK Access and Queries), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Cosmos DB and PostgreSQL vector documentation: https://learn.microsoft.com/en-us/azure/cosmos-db/

- **A:** Incorrect for this question. Request units measure the work a query performs, so tuning the query is often cheaper than adding throughput. Monitor normalized RU consumption. Why the correct answer wins: Including the partition key makes the read single-partition.
- **B:** Correct. Cosmos DB gives globally distributed, low-latency document access with tunable consistency. Partition key and RU planning determine the cost profile. In this case: Including the partition key makes the read single-partition.
- **C:** Incorrect for this question. SDK queries keep the client on the supported data plane and parameterization avoids injection and plan churn. Cross-partition queries still cost more. Why the correct answer wins: Including the partition key makes the read single-partition.
- **D:** Incorrect for this question. A point or single-partition query avoids fan-out across partitions. Cross-partition queries consume more RUs and add latency. Why the correct answer wins: Including the partition key makes the read single-partition.

### Question 13 — A

Answer: Increase provisioned throughput and watch the RU charge per query. The RU charge per write shows whether indexing or document size is inflating cost before adding throughput. Request units measure the work a query performs, so tuning the query is often cheaper than adding throughput. Monitor normalized RU consumption. Local study-map skill 2.2 (Cosmos DB Indexing Policies and Request Units), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Cosmos DB and PostgreSQL vector documentation: https://learn.microsoft.com/en-us/azure/cosmos-db/

- **A:** Correct. Request units measure the work a query performs, so tuning the query is often cheaper than adding throughput. Monitor normalized RU consumption. In this case: The RU charge per write shows whether indexing or document size is inflating cost before adding throughput.
- **B:** Incorrect for this question. Selective indexing cuts write RU charge and storage for unused paths. Excluded paths cannot be filtered efficiently later. Why the correct answer wins: The RU charge per write shows whether indexing or document size is inflating cost before adding throughput.
- **C:** Incorrect for this question. Indexing everything is simple and makes ad hoc queries possible, at higher write cost and storage. It is a default, not an optimization. Why the correct answer wins: The RU charge per write shows whether indexing or document size is inflating cost before adding throughput.
- **D:** Incorrect for this question. Autoscale follows demand between a minimum and maximum, avoiding throttling at peak without paying for peak all day. The maximum still caps the bill. Why the correct answer wins: The RU charge per write shows whether indexing or document size is inflating cost before adding throughput.

### Question 14 — C

Answer: Use session consistency for reads within the same client session. Session consistency guarantees read-your-writes for that session. Session consistency guarantees monotonic reads for one session and is the common default for user-facing apps. It does not promise global freshness. Local study-map skill 2.3 (Cosmos DB Consistency Levels), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Cosmos DB and PostgreSQL vector documentation: https://learn.microsoft.com/en-us/azure/cosmos-db/

- **A:** Incorrect for this question. Eventual consistency is the cheapest and most available option but returns possibly stale data. It fits non-critical counters, not balances. Why the correct answer wins: Session consistency guarantees read-your-writes for that session.
- **B:** Incorrect for this question. Consistency trades freshness against latency, availability, and RU cost. The level is set at the account and can be relaxed per request. Why the correct answer wins: Session consistency guarantees read-your-writes for that session.
- **C:** Correct. Session consistency guarantees monotonic reads for one session and is the common default for user-facing apps. It does not promise global freshness. In this case: Session consistency guarantees read-your-writes for that session.
- **D:** Incorrect for this question. Strong consistency guarantees the latest committed write globally at the cost of higher latency and reduced availability during partitions. Why the correct answer wins: Session consistency guarantees read-your-writes for that session.

### Question 15 — D

Answer: Store embeddings in a vector property and query with VectorDistance. A vector property plus the distance function keeps embeddings and metadata in one query. Cosmos DB for NoSQL supports vector properties and a distance function for similarity search in the same document store. Dimensions and index type must match the model. Local study-map skill 2.4 (Cosmos DB Vector Search and Embeddings), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Cosmos DB and PostgreSQL vector documentation: https://learn.microsoft.com/en-us/azure/cosmos-db/

- **A:** Incorrect for this question. The container vector policy fixes dimensions, distance function, and index type, so a model change requires a new policy. Mismatched dimensions fail at write time. Why the correct answer wins: A vector property plus the distance function keeps embeddings and metadata in one query.
- **B:** Incorrect for this question. DiskANN trades some recall for memory efficiency on large sets. Recall and latency should be measured on representative queries. Why the correct answer wins: A vector property plus the distance function keeps embeddings and metadata in one query.
- **C:** Incorrect for this question. Application-side scoring works for tiny collections and tests, but it moves all data over the wire and does not scale with corpus size. Why the correct answer wins: A vector property plus the distance function keeps embeddings and metadata in one query.
- **D:** Correct. Cosmos DB for NoSQL supports vector properties and a distance function for similarity search in the same document store. Dimensions and index type must match the model. In this case: A vector property plus the distance function keeps embeddings and metadata in one query.

### Question 16 — A

Answer: Use a lease container to coordinate change feed readers. A lease container records ownership and continuation per partition. Leases track partition ownership so multiple processor instances share work and resume from a continuation token. Lease writes consume RUs too. Local study-map skill 2.5 (Cosmos DB Change Feed Processing), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Cosmos DB and PostgreSQL vector documentation: https://learn.microsoft.com/en-us/azure/cosmos-db/

- **A:** Correct. Leases track partition ownership so multiple processor instances share work and resume from a continuation token. Lease writes consume RUs too. In this case: A lease container records ownership and continuation per partition.
- **B:** Incorrect for this question. A transactional batch applies all-or-nothing within a single partition key. It cannot span partitions and still consumes RU per operation. Why the correct answer wins: A lease container records ownership and continuation per partition.
- **C:** Incorrect for this question. A duplicate-detection window drops repeated sends within the window, which helps with at-least-once producers. The window is time-bounded. Why the correct answer wins: A lease container records ownership and continuation per partition.
- **D:** Incorrect for this question. The change feed delivers an ordered stream of changes per partition for downstream processing. It is not a delete feed, so deletions need a workaround. Why the correct answer wins: A lease container records ownership and continuation per partition.

### Question 17 — C

Answer: Model typed columns for filters and one vector column for the embedding. Typed columns for filters with one vector column enable both in one query. Explicit types keep filters fast and make the embedding contract clear. Storing vectors as text defeats index use. Local study-map skill 2.6 (PostgreSQL Connection and Schema Modeling), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Cosmos DB and PostgreSQL vector documentation: https://learn.microsoft.com/en-us/azure/cosmos-db/

- **A:** Incorrect for this question. A replica offloads read traffic but introduces replication lag, which is dangerous for freshly written evidence. It does not reduce index memory pressure. Why the correct answer wins: Typed columns for filters with one vector column enable both in one query.
- **B:** Incorrect for this question. pgvector keeps vectors beside relational data, so filters and joins run in one query. Index type and parameter tuning decide latency. Why the correct answer wins: Typed columns for filters with one vector column enable both in one query.
- **C:** Correct. Explicit types keep filters fast and make the embedding contract clear. Storing vectors as text defeats index use. In this case: Typed columns for filters with one vector column enable both in one query.
- **D:** Incorrect for this question. Vector indexes are memory-hungry, so undersized compute causes swapping and slow queries. Right-size before tuning index parameters. Why the correct answer wins: Typed columns for filters with one vector column enable both in one query.

### Question 18 — B

Answer: Create an HNSW index for low-latency approximate search. HNSW provides fast approximate search with recall tuned at query time. HNSW gives fast approximate nearest-neighbour queries with a larger memory footprint and slower builds. Recall is tunable at query time. Local study-map skill 2.7 (pgvector Indexing and Query Latency), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Cosmos DB and PostgreSQL vector documentation: https://learn.microsoft.com/en-us/azure/cosmos-db/

- **A:** Incorrect for this question. An exact scan is accurate but scales linearly and burns compute. It is a baseline for measuring recall, not a production strategy. Why the correct answer wins: HNSW provides fast approximate search with recall tuned at query time.
- **B:** Correct. HNSW gives fast approximate nearest-neighbour queries with a larger memory footprint and slower builds. Recall is tunable at query time. In this case: HNSW provides fast approximate search with recall tuned at query time.
- **C:** Incorrect for this question. Index builds and large sorts spill to disk when work memory is too small, stretching maintenance windows and slowing queries. Why the correct answer wins: HNSW provides fast approximate search with recall tuned at query time.
- **D:** Incorrect for this question. IVFFlat uses clustering lists and needs periodic rebuilds as data grows, but costs less memory than HNSW. Probes trade recall for speed. Why the correct answer wins: HNSW provides fast approximate search with recall tuned at query time.

### Question 19 — B

Answer: Scale compute and memory to fit index size and query concurrency. Compute and memory must fit the index working set to avoid swapping. Vector indexes are memory-hungry, so undersized compute causes swapping and slow queries. Right-size before tuning index parameters. Local study-map skill 2.8 (PostgreSQL Compute, Memory, and Storage Sizing), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Cosmos DB and PostgreSQL vector documentation: https://learn.microsoft.com/en-us/azure/cosmos-db/

- **A:** Incorrect for this question. Index builds and large sorts spill to disk when work memory is too small, stretching maintenance windows and slowing queries. Why the correct answer wins: Compute and memory must fit the index working set to avoid swapping.
- **B:** Correct. Vector indexes are memory-hungry, so undersized compute causes swapping and slow queries. Right-size before tuning index parameters. In this case: Compute and memory must fit the index working set to avoid swapping.
- **C:** Incorrect for this question. Index creation and bulk loads are I/O heavy, and throttled storage stretches maintenance windows. Storage limits are separate from compute. Why the correct answer wins: Compute and memory must fit the index working set to avoid swapping.
- **D:** Incorrect for this question. A bounded pool amortizes connection setup and protects the server from connection storms. Pool size must match server limits. Why the correct answer wins: Compute and memory must fit the index working set to avoid swapping.

### Question 20 — C

Answer: Reuse a bounded connection pool instead of opening a connection per request. A bounded connection pool reuses connections instead of opening one per request. A bounded pool amortizes connection setup and protects the server from connection storms. Pool size must match server limits. Local study-map skill 2.10 (PostgreSQL Connection Optimization), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Cosmos DB and PostgreSQL vector documentation: https://learn.microsoft.com/en-us/azure/cosmos-db/

- **A:** Incorrect for this question. An external pooler multiplexes server connections for serverless or highly concurrent clients. Session-level features may be unavailable in transaction mode. Why the correct answer wins: A bounded connection pool reuses connections instead of opening one per request.
- **B:** Incorrect for this question. A replica offloads read traffic but introduces replication lag, which is dangerous for freshly written evidence. It does not reduce index memory pressure. Why the correct answer wins: A bounded connection pool reuses connections instead of opening one per request.
- **C:** Correct. A bounded pool amortizes connection setup and protects the server from connection storms. Pool size must match server limits. In this case: A bounded connection pool reuses connections instead of opening one per request.
- **D:** Incorrect for this question. Prepared statements avoid repeated planning and reduce chatty network calls. They pair well with pooling but can interact with pool modes. Why the correct answer wins: A bounded connection pool reuses connections instead of opening one per request.

### Question 21 — D

Answer: Set a TTL on each cached entry. A TTL bounds staleness independently of invalidation. A TTL bounds staleness and reclaims memory without a manual sweep. Too long a TTL hides source changes; too short wastes the cache. Local study-map skill 2.11 (Azure Managed Redis Caching and Invalidation), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Cosmos DB and PostgreSQL vector documentation: https://learn.microsoft.com/en-us/azure/cosmos-db/

- **A:** Incorrect for this question. Flushing removes all cached content at once, causing a stampede to the origin and a latency cliff. Targeted invalidation is safer. Why the correct answer wins: A TTL bounds staleness independently of invalidation.
- **B:** Incorrect for this question. Eviction protects memory but evicts unpredictably, so a hot key can vanish before its freshness bound is reached. It is not a substitute for TTL design. Why the correct answer wins: A TTL bounds staleness independently of invalidation.
- **C:** Incorrect for this question. Write-through or explicit invalidation keeps cached answers consistent with the system of record. Without it, TTL is the only bound on staleness. Why the correct answer wins: A TTL bounds staleness independently of invalidation.
- **D:** Correct. A TTL bounds staleness and reclaims memory without a manual sweep. Too long a TTL hides source changes; too short wastes the cache. In this case: A TTL bounds staleness independently of invalidation.

### Question 22 — B

Answer: Create a vector index in Managed Redis for similarity search. A Redis vector index performs similarity from memory. Redis vector search serves low-latency similarity queries from memory. The corpus must fit the memory budget and be rebuilt on model change. Local study-map skill 2.12 (Azure Managed Redis Vector Indexing), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Cosmos DB and PostgreSQL vector documentation: https://learn.microsoft.com/en-us/azure/cosmos-db/

- **A:** Incorrect for this question. A lock can serialize work across instances, but correctness under retries still needs idempotency keys in the data store. Locks expire and can be lost. Why the correct answer wins: A Redis vector index performs similarity from memory.
- **B:** Correct. Redis vector search serves low-latency similarity queries from memory. The corpus must fit the memory budget and be rebuilt on model change. In this case: A Redis vector index performs similarity from memory.
- **C:** Incorrect for this question. Session storage in Redis survives instance restarts and supports distributed instances. Sessions must be scoped and expiring. Why the correct answer wins: A Redis vector index performs similarity from memory.
- **D:** Incorrect for this question. A cache absorbs repeated reads and cuts latency for hot data. Cache keys, TTLs, and invalidation must match the freshness requirement. Why the correct answer wins: A Redis vector index performs similarity from memory.

### Question 23 — A, C

Answers: Query through the Cosmos DB SDK with parameterized queries; Batch related writes in a transactional batch within one partition key. SDK calls keep the client supported, and a transactional batch gives all-or-nothing within one partition key. SDK queries keep the client on the supported data plane and parameterization avoids injection and plan churn. Cross-partition queries still cost more. A transactional batch applies all-or-nothing within a single partition key. It cannot span partitions and still consumes RU per operation. Local study-map skill 2.1 (Cosmos DB SDK Access and Queries), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Cosmos DB and PostgreSQL vector documentation: https://learn.microsoft.com/en-us/azure/cosmos-db/

- **A:** Correct. A transactional batch applies all-or-nothing within a single partition key. It cannot span partitions and still consumes RU per operation. In this case: SDK calls keep the client supported, and a transactional batch gives all-or-nothing within one partition key.
- **B:** Incorrect for this question. A duplicate-detection window drops repeated sends within the window, which helps with at-least-once producers. The window is time-bounded. Why the correct answer wins: SDK calls keep the client supported, and a transactional batch gives all-or-nothing within one partition key.
- **C:** Correct. SDK queries keep the client on the supported data plane and parameterization avoids injection and plan churn. Cross-partition queries still cost more. In this case: SDK calls keep the client supported, and a transactional batch gives all-or-nothing within one partition key.
- **D:** Incorrect for this question. Autoscale follows demand between a minimum and maximum, avoiding throttling at peak without paying for peak all day. The maximum still caps the bill. Why the correct answer wins: SDK calls keep the client supported, and a transactional batch gives all-or-nothing within one partition key.
- **E:** Incorrect for this question. Leases track partition ownership so multiple processor instances share work and resume from a continuation token. Lease writes consume RUs too. Why the correct answer wins: SDK calls keep the client supported, and a transactional batch gives all-or-nothing within one partition key.

### Question 24 — B, C

Answers: Create an IVFFlat index to save memory on a large table; Increase maintenance and query memory settings for index builds and sorts. IVFFlat reduces memory use with periodic rebuilds, and adequate work memory prevents spills. IVFFlat uses clustering lists and needs periodic rebuilds as data grows, but costs less memory than HNSW. Probes trade recall for speed. Index builds and large sorts spill to disk when work memory is too small, stretching maintenance windows and slowing queries. Local study-map skill 2.7 (pgvector Indexing and Query Latency), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Cosmos DB and PostgreSQL vector documentation: https://learn.microsoft.com/en-us/azure/cosmos-db/

- **A:** Incorrect for this question. HNSW gives fast approximate nearest-neighbour queries with a larger memory footprint and slower builds. Recall is tunable at query time. Why the correct answer wins: IVFFlat reduces memory use with periodic rebuilds, and adequate work memory prevents spills.
- **B:** Correct. IVFFlat uses clustering lists and needs periodic rebuilds as data grows, but costs less memory than HNSW. Probes trade recall for speed. In this case: IVFFlat reduces memory use with periodic rebuilds, and adequate work memory prevents spills.
- **C:** Correct. Index builds and large sorts spill to disk when work memory is too small, stretching maintenance windows and slowing queries. In this case: IVFFlat reduces memory use with periodic rebuilds, and adequate work memory prevents spills.
- **D:** Incorrect for this question. Index creation and bulk loads are I/O heavy, and throttled storage stretches maintenance windows. Storage limits are separate from compute. Why the correct answer wins: IVFFlat reduces memory use with periodic rebuilds, and adequate work memory prevents spills.
- **E:** Incorrect for this question. An exact scan is accurate but scales linearly and burns compute. It is a baseline for measuring recall, not a production strategy. Why the correct answer wins: IVFFlat reduces memory use with periodic rebuilds, and adequate work memory prevents spills.

### Question 25 — C

Answer: Create the container with a vector policy → upsert items with embeddings → query with VectorDistance → apply metadata filters. The container and its vector policy must exist before embeddings are written, and writes must precede similarity queries. The vector policy fixes dimensions and index type, so it must exist before vector writes and queries. Local study-map skill 2.4 (Cosmos DB Vector Search and Embeddings), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Cosmos DB and PostgreSQL vector documentation: https://learn.microsoft.com/en-us/azure/cosmos-db/

- **A:** Incorrect for this question. Items cannot be written before the container exists with a matching vector policy. Why the correct answer wins: The container and its vector policy must exist before embeddings are written, and writes must precede similarity queries.
- **B:** Incorrect for this question. A similarity query needs indexed vectors, which require the container and its policy first. Why the correct answer wins: The container and its vector policy must exist before embeddings are written, and writes must precede similarity queries.
- **C:** Correct. The vector policy fixes dimensions and index type, so it must exist before vector writes and queries. In this case: The container and its vector policy must exist before embeddings are written, and writes must precede similarity queries.
- **D:** Incorrect for this question. Filtering and querying cannot precede the container and its vector data. Why the correct answer wins: The container and its vector policy must exist before embeddings are written, and writes must precede similarity queries.

### Question 26 — C

Answer: Queue the work on a Service Bus queue and process it with a worker. A queue with peek-lock completion provides at-least-once processing and workload recovery. A queue decouples producers from a single consumer group and smooths bursts. Delivery semantics depend on receive mode and completion. Local study-map skill 3.1 (Service Bus Queues and Sessions), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure messaging and Functions documentation: https://learn.microsoft.com/en-us/azure/service-bus-messaging/

- **A:** Incorrect for this question. Event Hubs ingests high-volume ordered streams with partitions and consumer groups. It is a streaming log, not a task queue. Why the correct answer wins: A queue with peek-lock completion provides at-least-once processing and workload recovery.
- **B:** Incorrect for this question. Topics fan out one message to independent subscribers, each with its own filter and dead-letter queue. Subscribers process at their own pace. Why the correct answer wins: A queue with peek-lock completion provides at-least-once processing and workload recovery.
- **C:** Correct. A queue decouples producers from a single consumer group and smooths bursts. Delivery semantics depend on receive mode and completion. In this case: A queue with peek-lock completion provides at-least-once processing and workload recovery.
- **D:** Incorrect for this question. Queue Storage is simple and cheap for large backlogs with at-least-once delivery. It lacks topics, sessions, and scheduled messages. Why the correct answer wins: A queue with peek-lock completion provides at-least-once processing and workload recovery.

### Question 27 — B

Answer: Use Service Bus sessions to keep related messages ordered. Sessions give ordered, exclusive processing per machine. Sessions give ordered, exclusive processing per session ID across competing consumers. They require session-aware senders and receivers. Local study-map skill 3.1 (Service Bus Queues and Sessions), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure messaging and Functions documentation: https://learn.microsoft.com/en-us/azure/service-bus-messaging/

- **A:** Incorrect for this question. A duplicate-detection window drops repeated sends within the window, which helps with at-least-once producers. The window is time-bounded. Why the correct answer wins: Sessions give ordered, exclusive processing per machine.
- **B:** Correct. Sessions give ordered, exclusive processing per session ID across competing consumers. They require session-aware senders and receivers. In this case: Sessions give ordered, exclusive processing per machine.
- **C:** Incorrect for this question. Peek-lock keeps the message locked until the handler completes it, giving at-least-once processing with retry. Lock duration must exceed processing time. Why the correct answer wins: Sessions give ordered, exclusive processing per machine.
- **D:** Incorrect for this question. A delivery cap stops infinite retries of a failing message and moves it to the dead-letter queue. The cap must exceed legitimate transient retries. Why the correct answer wins: Sessions give ordered, exclusive processing per machine.

### Question 28 — D

Answer: Publish to a Service Bus topic with multiple subscriptions. A topic with separate subscriptions provides fan-out. Topics fan out one message to independent subscribers, each with its own filter and dead-letter queue. Subscribers process at their own pace. Local study-map skill 3.2 (Service Bus Topics, Subscriptions, and Filters), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure messaging and Functions documentation: https://learn.microsoft.com/en-us/azure/service-bus-messaging/

- **A:** Incorrect for this question. A queue decouples producers from a single consumer group and smooths bursts. Delivery semantics depend on receive mode and completion. Why the correct answer wins: A topic with separate subscriptions provides fan-out.
- **B:** Incorrect for this question. A custom schema fits domain events that are not resource lifecycle notifications. Consumers must version the schema contract. Why the correct answer wins: A topic with separate subscriptions provides fan-out.
- **C:** Incorrect for this question. Queue Storage is simple and cheap for large backlogs with at-least-once delivery. It lacks topics, sessions, and scheduled messages. Why the correct answer wins: A topic with separate subscriptions provides fan-out.
- **D:** Correct. Topics fan out one message to independent subscribers, each with its own filter and dead-letter queue. Subscribers process at their own pace. In this case: A topic with separate subscriptions provides fan-out.

### Question 29 — B

Answer: Rely on Event Grid retries with a dead-letter destination. Event Grid retries failed deliveries and can dead-letter what never succeeds. Event Grid retries failed deliveries with backoff and can store undeliverable events. Handlers must still be idempotent. Local study-map skill 3.4 (Event Grid Filters, Custom Events, and Retries), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure messaging and Functions documentation: https://learn.microsoft.com/en-us/azure/service-bus-messaging/

- **A:** Incorrect for this question. Subject and event-type filters keep handlers focused and reduce cost. Filters are evaluated on event metadata, not payload body. Why the correct answer wins: Event Grid retries failed deliveries and can dead-letter what never succeeds.
- **B:** Correct. Event Grid retries failed deliveries with backoff and can store undeliverable events. Handlers must still be idempotent. In this case: Event Grid retries failed deliveries and can dead-letter what never succeeds.
- **C:** Incorrect for this question. Identity-based delivery removes a shared key from the subscription. The receiver still validates the caller and payload. Why the correct answer wins: Event Grid retries failed deliveries and can dead-letter what never succeeds.
- **D:** Incorrect for this question. A custom schema fits domain events that are not resource lifecycle notifications. Consumers must version the schema contract. Why the correct answer wins: Event Grid retries failed deliveries and can dead-letter what never succeeds.

### Question 30 — B

Answer: Bind a queue or event trigger to the function. A queue trigger starts the function and manages the receive loop. A trigger starts the function when work arrives and handles the receive loop for you. Poison-message behavior is configured in host settings. Local study-map skill 3.5 (Azure Functions Triggers and Bindings), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure messaging and Functions documentation: https://learn.microsoft.com/en-us/azure/service-bus-messaging/

- **A:** Incorrect for this question. An HTTP trigger gives a synchronous API endpoint with route and authorization configuration. Long-running work should hand off to a queue. Why the correct answer wins: A queue trigger starts the function and manages the receive loop.
- **B:** Correct. A trigger starts the function when work arrives and handles the receive loop for you. Poison-message behavior is configured in host settings. In this case: A queue trigger starts the function and manages the receive loop.
- **C:** Incorrect for this question. Bindings reduce boilerplate for common inputs and outputs and are configured declaratively. Complex operations still need the SDK. Why the correct answer wins: A queue trigger starts the function and manages the receive loop.
- **D:** Incorrect for this question. Durable Functions provides orchestrations, activities, timers, and retries with checkpointed state. Orchestrator code must stay deterministic. Why the correct answer wins: A queue trigger starts the function and manages the receive loop.

### Question 31 — D

Answer: Use input and output bindings instead of hand-written SDK calls. An output binding declares the write target declaratively. Bindings reduce boilerplate for common inputs and outputs and are configured declaratively. Complex operations still need the SDK. Local study-map skill 3.5 (Azure Functions Triggers and Bindings), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure messaging and Functions documentation: https://learn.microsoft.com/en-us/azure/service-bus-messaging/

- **A:** Incorrect for this question. A trigger starts the function when work arrives and handles the receive loop for you. Poison-message behavior is configured in host settings. Why the correct answer wins: An output binding declares the write target declaratively.
- **B:** Incorrect for this question. A premium plan reduces cold starts and supports virtual network integration and longer timeouts. It costs more than consumption. Why the correct answer wins: An output binding declares the write target declaratively.
- **C:** Incorrect for this question. Durable Functions provides orchestrations, activities, timers, and retries with checkpointed state. Orchestrator code must stay deterministic. Why the correct answer wins: An output binding declares the write target declaratively.
- **D:** Correct. Bindings reduce boilerplate for common inputs and outputs and are configured declaratively. Complex operations still need the SDK. In this case: An output binding declares the write target declaratively.

### Question 32 — C

Answer: Host the function app on a premium plan with pre-warmed instances. A premium plan provides pre-warmed instances and virtual network integration. A premium plan reduces cold starts and supports virtual network integration and longer timeouts. It costs more than consumption. Local study-map skill 3.6 (Function App Configuration and Deployment), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure messaging and Functions documentation: https://learn.microsoft.com/en-us/azure/service-bus-messaging/

- **A:** Incorrect for this question. A staging slot lets a new build warm up and be validated before the swap. Slot settings that must not move are marked sticky. Why the correct answer wins: A premium plan provides pre-warmed instances and virtual network integration.
- **B:** Incorrect for this question. Durable Functions provides orchestrations, activities, timers, and retries with checkpointed state. Orchestrator code must stay deterministic. Why the correct answer wins: A premium plan provides pre-warmed instances and virtual network integration.
- **C:** Correct. A premium plan reduces cold starts and supports virtual network integration and longer timeouts. It costs more than consumption. In this case: A premium plan provides pre-warmed instances and virtual network integration.
- **D:** Incorrect for this question. Consumption bills per execution and scales automatically, with cold starts and a timeout ceiling. It fits spiky, short work. Why the correct answer wins: A premium plan provides pre-warmed instances and virtual network integration.

### Question 33 — C, E

Answers: Publish to a Service Bus topic with multiple subscriptions; Add a SQL or correlation filter to a subscription. A topic provides fan-out, and a subscription filter narrows what one subscriber receives. Topics fan out one message to independent subscribers, each with its own filter and dead-letter queue. Subscribers process at their own pace. Subscription filters route only matching messages to a handler, reducing wasted processing. Filter evaluation happens broker-side on message properties. Local study-map skill 3.2 (Service Bus Topics, Subscriptions, and Filters), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure messaging and Functions documentation: https://learn.microsoft.com/en-us/azure/service-bus-messaging/

- **A:** Incorrect for this question. A queue decouples producers from a single consumer group and smooths bursts. Delivery semantics depend on receive mode and completion. Why the correct answer wins: A topic provides fan-out, and a subscription filter narrows what one subscriber receives.
- **B:** Incorrect for this question. Queue Storage is simple and cheap for large backlogs with at-least-once delivery. It lacks topics, sessions, and scheduled messages. Why the correct answer wins: A topic provides fan-out, and a subscription filter narrows what one subscriber receives.
- **C:** Correct. Topics fan out one message to independent subscribers, each with its own filter and dead-letter queue. Subscribers process at their own pace. In this case: A topic provides fan-out, and a subscription filter narrows what one subscriber receives.
- **D:** Incorrect for this question. Subject and event-type filters keep handlers focused and reduce cost. Filters are evaluated on event metadata, not payload body. Why the correct answer wins: A topic provides fan-out, and a subscription filter narrows what one subscriber receives.
- **E:** Correct. Subscription filters route only matching messages to a handler, reducing wasted processing. Filter evaluation happens broker-side on message properties. In this case: A topic provides fan-out, and a subscription filter narrows what one subscriber receives.

### Question 34 — A, D

Answers: Orchestrate the multi-step workflow with Durable Functions; Bind a queue or event trigger to the function. Durable orchestration checkpoints progress, and a queue trigger starts the workflow. Durable Functions provides orchestrations, activities, timers, and retries with checkpointed state. Orchestrator code must stay deterministic. A trigger starts the function when work arrives and handles the receive loop for you. Poison-message behavior is configured in host settings. Local study-map skill 3.5 (Azure Functions Triggers and Bindings), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure messaging and Functions documentation: https://learn.microsoft.com/en-us/azure/service-bus-messaging/

- **A:** Correct. A trigger starts the function when work arrives and handles the receive loop for you. Poison-message behavior is configured in host settings. In this case: Durable orchestration checkpoints progress, and a queue trigger starts the workflow.
- **B:** Incorrect for this question. Consumption bills per execution and scales automatically, with cold starts and a timeout ceiling. It fits spiky, short work. Why the correct answer wins: Durable orchestration checkpoints progress, and a queue trigger starts the workflow.
- **C:** Incorrect for this question. An HTTP trigger gives a synchronous API endpoint with route and authorization configuration. Long-running work should hand off to a queue. Why the correct answer wins: Durable orchestration checkpoints progress, and a queue trigger starts the workflow.
- **D:** Correct. Durable Functions provides orchestrations, activities, timers, and retries with checkpointed state. Orchestrator code must stay deterministic. In this case: Durable orchestration checkpoints progress, and a queue trigger starts the workflow.
- **E:** Incorrect for this question. Bindings reduce boilerplate for common inputs and outputs and are configured declaratively. Complex operations still need the SDK. Why the correct answer wins: Durable orchestration checkpoints progress, and a queue trigger starts the workflow.

### Question 35 — B

Answer: Publish the message → receive with peek-lock → process the work → complete the message → dead-letter after the delivery limit. Receive, process, complete, and dead-letter only after the limit. Peek-lock keeps the message until the handler succeeds, and only repeated failures should dead-letter it. Local study-map skill 3.1 (Service Bus Queues and Sessions), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure messaging and Functions documentation: https://learn.microsoft.com/en-us/azure/service-bus-messaging/

- **A:** Incorrect for this question. The message cannot be received before it is published, and completion must follow processing. Why the correct answer wins: Receive, process, complete, and dead-letter only after the limit.
- **B:** Correct. Peek-lock keeps the message until the handler succeeds, and only repeated failures should dead-letter it. In this case: Receive, process, complete, and dead-letter only after the limit.
- **C:** Incorrect for this question. Completing a message before processing discards the work and defeats at-least-once delivery. Why the correct answer wins: Receive, process, complete, and dead-letter only after the limit.
- **D:** Incorrect for this question. Work cannot be processed before the message is published and received. Why the correct answer wins: Receive, process, complete, and dead-letter only after the limit.

### Question 36 — C

Answer: Store the secret in Azure Key Vault and read it at runtime. Key Vault stores the token with access control and audit. A vault centralizes secret storage with access control and audit. Retrieval should use an identity, not a copied credential. Local study-map skill 4.1 (Key Vault Secret Storage, Rotation, and Retrieval), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Key Vault, App Configuration, and Monitor documentation: https://learn.microsoft.com/en-us/azure/azure-monitor/

- **A:** Incorrect for this question. App Configuration separates configuration from code and supports labels, feature flags, and Key Vault references. Change still needs a refresh strategy. Why the correct answer wins: Key Vault stores the token with access control and audit.
- **B:** Incorrect for this question. Application settings become environment variables for the container and can be swapped per slot. Sensitive values should still reference a vault. Why the correct answer wins: Key Vault stores the token with access control and audit.
- **C:** Correct. A vault centralizes secret storage with access control and audit. Retrieval should use an identity, not a copied credential. In this case: Key Vault stores the token with access control and audit.
- **D:** Incorrect for this question. Pinning a version makes a rotation invisible to the app until it is redeployed, which is useful for break-glass and dangerous for routine rotation. Why the correct answer wins: Key Vault stores the token with access control and audit.

### Question 37 — C

Answer: Grant the app identity data-plane access to the vault. A data-plane role or policy for that identity is required before the secret can be read. Vault access is a separate authorization decision from the app identity. Without a data-plane role or policy the reference fails at runtime. Local study-map skill 4.1 (Key Vault Secret Storage, Rotation, and Retrieval), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Key Vault, App Configuration, and Monitor documentation: https://learn.microsoft.com/en-us/azure/azure-monitor/

- **A:** Incorrect for this question. A scoped role grants only the operations the app performs and limits blast radius. Prefer built-in roles over broad contributor grants. Why the correct answer wins: A data-plane role or policy for that identity is required before the secret can be read.
- **B:** Incorrect for this question. Soft delete and purge protection stop accidental or malicious permanent loss of secrets. They also constrain how names can be reused. Why the correct answer wins: A data-plane role or policy for that identity is required before the secret can be read.
- **C:** Correct. Vault access is a separate authorization decision from the app identity. Without a data-plane role or policy the reference fails at runtime. In this case: A data-plane role or policy for that identity is required before the secret can be read.
- **D:** Incorrect for this question. A managed identity issues tokens from the platform, removing secret distribution from the app. Role assignment still scopes what it can reach. Why the correct answer wins: A data-plane role or policy for that identity is required before the secret can be read.

### Question 38 — B

Answer: Store settings and feature flags in Azure App Configuration. App Configuration stores per-environment settings with refresh support. App Configuration separates configuration from code and supports labels, feature flags, and Key Vault references. Change still needs a refresh strategy. Local study-map skill 4.2 (App Configuration Settings and Feature Flags), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Key Vault, App Configuration, and Monitor documentation: https://learn.microsoft.com/en-us/azure/azure-monitor/

- **A:** Incorrect for this question. Sentinel-key or polling refresh lets a running app pick up new settings. Refresh intervals trade responsiveness against request volume. Why the correct answer wins: App Configuration stores per-environment settings with refresh support.
- **B:** Correct. App Configuration separates configuration from code and supports labels, feature flags, and Key Vault references. Change still needs a refresh strategy. In this case: App Configuration stores per-environment settings with refresh support.
- **C:** Incorrect for this question. A vault centralizes secret storage with access control and audit. Retrieval should use an identity, not a copied credential. Why the correct answer wins: App Configuration stores per-environment settings with refresh support.
- **D:** Incorrect for this question. Labels keep dev, test, and prod values in one store with one key schema. A misconfigured label selector silently serves the wrong values. Why the correct answer wins: App Configuration stores per-environment settings with refresh support.

### Question 39 — C

Answer: Enable configuration refresh so changes apply without a restart. Configuration refresh lets a running app apply changed values. Sentinel-key or polling refresh lets a running app pick up new settings. Refresh intervals trade responsiveness against request volume. Local study-map skill 4.2 (App Configuration Settings and Feature Flags), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Key Vault, App Configuration, and Monitor documentation: https://learn.microsoft.com/en-us/azure/azure-monitor/

- **A:** Incorrect for this question. Labels keep dev, test, and prod values in one store with one key schema. A misconfigured label selector silently serves the wrong values. Why the correct answer wins: Configuration refresh lets a running app apply changed values.
- **B:** Incorrect for this question. Pinning a version makes a rotation invisible to the app until it is redeployed, which is useful for break-glass and dangerous for routine rotation. Why the correct answer wins: Configuration refresh lets a running app apply changed values.
- **C:** Correct. Sentinel-key or polling refresh lets a running app pick up new settings. Refresh intervals trade responsiveness against request volume. In this case: Configuration refresh lets a running app apply changed values.
- **D:** Incorrect for this question. Pipeline deployment keeps code and configuration versioned together and repeatable. Secrets belong in a vault reference, not in the pipeline file. Why the correct answer wins: Configuration refresh lets a running app apply changed values.

### Question 40 — C

Answer: Instrument the service with the OpenTelemetry SDK. OpenTelemetry instrumentation with context propagation produces one end-to-end trace. OpenTelemetry emits vendor-neutral traces, metrics, and logs with context propagation. Exporters and sampling decide what reaches the backend. Local study-map skill 4.3 (Distributed Tracing with OpenTelemetry), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Key Vault, App Configuration, and Monitor documentation: https://learn.microsoft.com/en-us/azure/azure-monitor/

- **A:** Incorrect for this question. Application Insights correlates requests, dependencies, and exceptions into end-to-end transactions. Sampling can hide rare failures. Why the correct answer wins: OpenTelemetry instrumentation with context propagation produces one end-to-end trace.
- **B:** Incorrect for this question. Platform logs and metrics must be routed before they can be queried or alerted on. Retention and cost follow the workspace settings. Why the correct answer wins: OpenTelemetry instrumentation with context propagation produces one end-to-end trace.
- **C:** Correct. OpenTelemetry emits vendor-neutral traces, metrics, and logs with context propagation. Exporters and sampling decide what reaches the backend. In this case: OpenTelemetry instrumentation with context propagation produces one end-to-end trace.
- **D:** Incorrect for this question. KQL filters, projects, and aggregates log and metric tables in Log Analytics. Start narrow with a time range and a request ID. Why the correct answer wins: OpenTelemetry instrumentation with context propagation produces one end-to-end trace.

### Question 41 — A

Answer: Assign a least-privilege role to the application identity. Split identities and scope the app identity to read-only access. A scoped role grants only the operations the app performs and limits blast radius. Prefer built-in roles over broad contributor grants. Local study-map skill 4.5 (Identity-Based Access for Application Services), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Key Vault, App Configuration, and Monitor documentation: https://learn.microsoft.com/en-us/azure/azure-monitor/

- **A:** Correct. A scoped role grants only the operations the app performs and limits blast radius. Prefer built-in roles over broad contributor grants. In this case: Split identities and scope the app identity to read-only access.
- **B:** Incorrect for this question. A vault centralizes secret storage with access control and audit. Retrieval should use an identity, not a copied credential. Why the correct answer wins: Split identities and scope the app identity to read-only access.
- **C:** Incorrect for this question. A managed identity issues tokens from the platform, removing secret distribution from the app. Role assignment still scopes what it can reach. Why the correct answer wins: Split identities and scope the app identity to read-only access.
- **D:** Incorrect for this question. A private endpoint keeps traffic on the virtual network and removes public exposure. DNS resolution must be wired to the private zone. Why the correct answer wins: Split identities and scope the app identity to read-only access.

### Question 42 — D, E

Answers: Instrument the service with the OpenTelemetry SDK; Propagate trace context across every service and queue hop. SDK instrumentation emits spans, and context propagation in message headers keeps the trace connected. OpenTelemetry emits vendor-neutral traces, metrics, and logs with context propagation. Exporters and sampling decide what reaches the backend. Propagation stitches one trace across HTTP, messaging, and Functions so the whole path is visible. Missing propagation breaks the trace at that hop. Local study-map skill 4.3 (Distributed Tracing with OpenTelemetry), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Key Vault, App Configuration, and Monitor documentation: https://learn.microsoft.com/en-us/azure/azure-monitor/

- **A:** Incorrect for this question. KQL filters, projects, and aggregates log and metric tables in Log Analytics. Start narrow with a time range and a request ID. Why the correct answer wins: SDK instrumentation emits spans, and context propagation in message headers keeps the trace connected.
- **B:** Incorrect for this question. Sampling keeps telemetry cost bounded, but aggressive sampling can hide rare failures. Tail sampling can retain errors preferentially. Why the correct answer wins: SDK instrumentation emits spans, and context propagation in message headers keeps the trace connected.
- **C:** Incorrect for this question. Platform logs and metrics must be routed before they can be queried or alerted on. Retention and cost follow the workspace settings. Why the correct answer wins: SDK instrumentation emits spans, and context propagation in message headers keeps the trace connected.
- **D:** Correct. Propagation stitches one trace across HTTP, messaging, and Functions so the whole path is visible. Missing propagation breaks the trace at that hop. In this case: SDK instrumentation emits spans, and context propagation in message headers keeps the trace connected.
- **E:** Correct. OpenTelemetry emits vendor-neutral traces, metrics, and logs with context propagation. Exporters and sampling decide what reaches the backend. In this case: SDK instrumentation emits spans, and context propagation in message headers keeps the trace connected.

### Question 43 — A, C

Answers: Store the secret in Azure Key Vault and read it at runtime; Authenticate with a managed identity instead of a stored key. Store the value in Key Vault, then let a managed identity read it. A vault centralizes secret storage with access control and audit. Retrieval should use an identity, not a copied credential. A managed identity issues tokens from the platform, removing secret distribution from the app. Role assignment still scopes what it can reach. Local study-map skill 4.1 (Key Vault Secret Storage, Rotation, and Retrieval), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Key Vault, App Configuration, and Monitor documentation: https://learn.microsoft.com/en-us/azure/azure-monitor/

- **A:** Correct. A managed identity issues tokens from the platform, removing secret distribution from the app. Role assignment still scopes what it can reach. In this case: Store the value in Key Vault, then let a managed identity read it.
- **B:** Incorrect for this question. App Configuration separates configuration from code and supports labels, feature flags, and Key Vault references. Change still needs a refresh strategy. Why the correct answer wins: Store the value in Key Vault, then let a managed identity read it.
- **C:** Correct. A vault centralizes secret storage with access control and audit. Retrieval should use an identity, not a copied credential. In this case: Store the value in Key Vault, then let a managed identity read it.
- **D:** Incorrect for this question. Labels keep dev, test, and prod values in one store with one key schema. A misconfigured label selector silently serves the wrong values. Why the correct answer wins: Store the value in Key Vault, then let a managed identity read it.
- **E:** Incorrect for this question. Pinning a version makes a rotation invisible to the app until it is redeployed, which is useful for break-glass and dangerous for routine rotation. Why the correct answer wins: Store the value in Key Vault, then let a managed identity read it.

### Question 44 — A

Answer: Store the secret in Key Vault → grant the app identity access → reference the secret from the app → rotate the secret → the app reads the new version. The secret is stored, access is granted, the app references it, and only then is it rotated. Access must be granted before the reference resolves, and the app must read the current version after rotation. Local study-map skill 4.1 (Key Vault Secret Storage, Rotation, and Retrieval), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Key Vault, App Configuration, and Monitor documentation: https://learn.microsoft.com/en-us/azure/azure-monitor/

- **A:** Correct. Access must be granted before the reference resolves, and the app must read the current version after rotation. In this case: The secret is stored, access is granted, the app references it, and only then is it rotated.
- **B:** Incorrect for this question. There is nothing to rotate or reference before the secret is stored. Why the correct answer wins: The secret is stored, access is granted, the app references it, and only then is it rotated.
- **C:** Incorrect for this question. Access can be granted first, but rotation cannot precede storing the secret. Why the correct answer wins: The secret is stored, access is granted, the app references it, and only then is it rotated.
- **D:** Incorrect for this question. A reference cannot resolve before the secret and the access grant exist. Why the correct answer wins: The secret is stored, access is granted, the app references it, and only then is it rotated.

### Question 45 — A

Answer: Scan images on push and block vulnerable builds in the pipeline. Scanning on push reports vulnerabilities per digest and can gate promotion, which is stricter than a manual review. A scan reports known vulnerabilities per image digest and can gate deployment. It does not patch the base image, so rebuilds are still required. Local study-map skill 1.1 (Container Image Lifecycle in Azure Container Registry), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure container hosting documentation: https://learn.microsoft.com/en-us/azure/container-apps/

- **A:** Correct. A scan reports known vulnerabilities per image digest and can gate deployment. It does not patch the base image, so rebuilds are still required. In this case: Scanning on push reports vulnerabilities per digest and can gate promotion, which is stricter than a manual review.
- **B:** Incorrect for this question. A floating tag removes the link between a deployed revision and a specific build, so rollback and audit become guesswork. Why the correct answer wins: Scanning on push reports vulnerabilities per digest and can gate promotion, which is stricter than a manual review.
- **C:** Incorrect for this question. A retention policy controls storage growth and registry clutter. It does not change which image tag a deployment references. Why the correct answer wins: Scanning on push reports vulnerabilities per digest and can gate promotion, which is stricter than a manual review.
- **D:** Incorrect for this question. ACR Tasks builds images in Azure on a commit or schedule without a local Docker host. It removes build-host drift but not image review. Why the correct answer wins: Scanning on push reports vulnerabilities per digest and can gate promotion, which is stricter than a manual review.

### Question 46 — A

Answer: Run image builds on demand or on a trigger with ACR Tasks. ACR Tasks rebuilds on a source or base-image trigger inside Azure, so no build server has to be patched. ACR Tasks builds images in Azure on a commit or schedule without a local Docker host. It removes build-host drift but not image review. Local study-map skill 1.2 (Automated Image Builds with ACR Tasks), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure container hosting documentation: https://learn.microsoft.com/en-us/azure/container-apps/

- **A:** Correct. ACR Tasks builds images in Azure on a commit or schedule without a local Docker host. It removes build-host drift but not image review. In this case: ACR Tasks rebuilds on a source or base-image trigger inside Azure, so no build server has to be patched.
- **B:** Incorrect for this question. AKS gives full Kubernetes control, including custom controllers and networking. You own node pools, upgrades, and manifest hygiene. Why the correct answer wins: ACR Tasks rebuilds on a source or base-image trigger inside Azure, so no build server has to be patched.
- **C:** Incorrect for this question. ACR keeps tagged, versioned images next to the deployment target and supports identity-based pulls. Tagging strategy and retention still need a decision. Why the correct answer wins: ACR Tasks rebuilds on a source or base-image trigger inside Azure, so no build server has to be patched.
- **D:** Incorrect for this question. Container Instances starts a single container group quickly for short tasks. It has no orchestrator-level scaling or revision model. Why the correct answer wins: ACR Tasks rebuilds on a source or base-image trigger inside Azure, so no build server has to be patched.

### Question 47 — B

Answer: Deploy the image to Azure App Service as a web app. App Service runs one container with slots and managed patching and does not expose a Kubernetes control plane. App Service runs a container with managed patching, deployment slots, and built-in authentication options. It is not a Kubernetes control plane. Local study-map skill 1.3 (Container Deployment to Azure App Service), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure container hosting documentation: https://learn.microsoft.com/en-us/azure/container-apps/

- **A:** Incorrect for this question. Functions runs small event-driven code without managing a host. Execution limits and cold starts depend on the hosting plan. Why the correct answer wins: App Service runs one container with slots and managed patching and does not expose a Kubernetes control plane.
- **B:** Correct. App Service runs a container with managed patching, deployment slots, and built-in authentication options. It is not a Kubernetes control plane. In this case: App Service runs one container with slots and managed patching and does not expose a Kubernetes control plane.
- **C:** Incorrect for this question. Container Instances starts a single container group quickly for short tasks. It has no orchestrator-level scaling or revision model. Why the correct answer wins: App Service runs one container with slots and managed patching and does not expose a Kubernetes control plane.
- **D:** Incorrect for this question. AKS gives full Kubernetes control, including custom controllers and networking. You own node pools, upgrades, and manifest hygiene. Why the correct answer wins: App Service runs one container with slots and managed patching and does not expose a Kubernetes control plane.

### Question 48 — A

Answer: Stage the change in a deployment slot and swap after verification. A slot swap warms the new version before it serves production and makes rollback a second swap. A slot swap warms the new version before it takes production traffic and makes rollback a second swap. Slot-local settings must be marked sticky. Local study-map skill 1.3 (Container Deployment to Azure App Service), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure container hosting documentation: https://learn.microsoft.com/en-us/azure/container-apps/

- **A:** Correct. A slot swap warms the new version before it takes production traffic and makes rollback a second swap. Slot-local settings must be marked sticky. In this case: A slot swap warms the new version before it serves production and makes rollback a second swap.
- **B:** Incorrect for this question. Geo-replication reduces cross-region pull latency and gives a local copy during a regional failure. It adds cost and replication management. Why the correct answer wins: A slot swap warms the new version before it serves production and makes rollback a second swap.
- **C:** Incorrect for this question. Revision-based traffic splitting enables canary and blue-green releases. Revision mode and scale rules must be set deliberately. Why the correct answer wins: A slot swap warms the new version before it serves production and makes rollback a second swap.
- **D:** Incorrect for this question. HPA adjusts replicas from resource metrics but needs metrics-server and enough node capacity. It cannot scale to zero. Why the correct answer wins: A slot swap warms the new version before it serves production and makes rollback a second swap.

### Question 49 — A

Answer: Deploy the service to Azure Container Apps. Container Apps provides revisions and scale-to-zero without exposing the control plane to the plant team. Container Apps provides a managed environment, revisions, and KEDA-based scaling without cluster administration. Platform limits differ from AKS. Local study-map skill 1.4 (Container Apps Deployment and Revisions), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure container hosting documentation: https://learn.microsoft.com/en-us/azure/container-apps/

- **A:** Correct. Container Apps provides a managed environment, revisions, and KEDA-based scaling without cluster administration. Platform limits differ from AKS. In this case: Container Apps provides revisions and scale-to-zero without exposing the control plane to the plant team.
- **B:** Incorrect for this question. App Service runs a container with managed patching, deployment slots, and built-in authentication options. It is not a Kubernetes control plane. Why the correct answer wins: Container Apps provides revisions and scale-to-zero without exposing the control plane to the plant team.
- **C:** Incorrect for this question. AKS gives full Kubernetes control, including custom controllers and networking. You own node pools, upgrades, and manifest hygiene. Why the correct answer wins: Container Apps provides revisions and scale-to-zero without exposing the control plane to the plant team.
- **D:** Incorrect for this question. Container Instances starts a single container group quickly for short tasks. It has no orchestrator-level scaling or revision model. Why the correct answer wins: Container Apps provides revisions and scale-to-zero without exposing the control plane to the plant team.

### Question 50 — D

Answer: Mount non-secret configuration from a Kubernetes ConfigMap. A ConfigMap injects non-secret settings as environment variables or files without rebuilding the image. A ConfigMap injects settings as environment variables or mounted files without rebuilding the image. Secrets still belong in Key Vault, not in a ConfigMap. Local study-map skill 1.6 (AKS Deployment with Manifests), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure container hosting documentation: https://learn.microsoft.com/en-us/azure/container-apps/

- **A:** Incorrect for this question. Pinning a version makes a rotation invisible to the app until it is redeployed, which is useful for break-glass and dangerous for routine rotation. Why the correct answer wins: A ConfigMap injects non-secret settings as environment variables or files without rebuilding the image.
- **B:** Incorrect for this question. Application settings become environment variables for the container and can be swapped per slot. Sensitive values should still reference a vault. Why the correct answer wins: A ConfigMap injects non-secret settings as environment variables or files without rebuilding the image.
- **C:** Incorrect for this question. A Key Vault reference resolves at runtime so the secret is never written into application settings. The app identity still needs permission to read it. Why the correct answer wins: A ConfigMap injects non-secret settings as environment variables or files without rebuilding the image.
- **D:** Correct. A ConfigMap injects settings as environment variables or mounted files without rebuilding the image. Secrets still belong in Key Vault, not in a ConfigMap. In this case: A ConfigMap injects non-secret settings as environment variables or files without rebuilding the image.

### Question 51 — B

Answer: Run startup prerequisites in an init container. An init container runs the download to completion before the application container is started. An init container finishes before the application container starts, so migrations or asset downloads complete first. It lengthens startup and must be fast and repeatable. Local study-map skill 1.6 (AKS Deployment with Manifests), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure container hosting documentation: https://learn.microsoft.com/en-us/azure/container-apps/

- **A:** Incorrect for this question. A manifest declares the desired deployment, service, and probe configuration in version control. Applying it repeatedly is idempotent. Why the correct answer wins: An init container runs the download to completion before the application container is started.
- **B:** Correct. An init container finishes before the application container starts, so migrations or asset downloads complete first. It lengthens startup and must be fast and repeatable. In this case: An init container runs the download to completion before the application container is started.
- **C:** Incorrect for this question. HPA adjusts replicas from resource metrics but needs metrics-server and enough node capacity. It cannot scale to zero. Why the correct answer wins: An init container runs the download to completion before the application container is started.
- **D:** Incorrect for this question. Readiness gates traffic until the app can serve it, and liveness restarts a wedged container. Wrong thresholds cause restart loops. Why the correct answer wins: An init container runs the download to completion before the application container is started.

### Question 52 — B

Answer: Apply a declarative Kubernetes manifest to the cluster. A declarative manifest describes desired state and is idempotent when reapplied to the cluster. A manifest declares the desired deployment, service, and probe configuration in version control. Applying it repeatedly is idempotent. Local study-map skill 1.6 (AKS Deployment with Manifests), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure container hosting documentation: https://learn.microsoft.com/en-us/azure/container-apps/

- **A:** Incorrect for this question. ACR Tasks builds images in Azure on a commit or schedule without a local Docker host. It removes build-host drift but not image review. Why the correct answer wins: A declarative manifest describes desired state and is idempotent when reapplied to the cluster.
- **B:** Correct. A manifest declares the desired deployment, service, and probe configuration in version control. Applying it repeatedly is idempotent. In this case: A declarative manifest describes desired state and is idempotent when reapplied to the cluster.
- **C:** Incorrect for this question. Container Instances starts a single container group quickly for short tasks. It has no orchestrator-level scaling or revision model. Why the correct answer wins: A declarative manifest describes desired state and is idempotent when reapplied to the cluster.
- **D:** Incorrect for this question. HPA adjusts replicas from resource metrics but needs metrics-server and enough node capacity. It cannot scale to zero. Why the correct answer wins: A declarative manifest describes desired state and is idempotent when reapplied to the cluster.

### Question 53 — A

Answer: Query container logs and Kubernetes events in Log Analytics. Container termination reasons and pod events land in the workspace where limits and restarts can be correlated. Container Apps and AKS surface stdout logs and platform events into a workspace for KQL analysis. Verbosity and retention cost money. Local study-map skill 1.7 (Container Logs, Events, and Connectivity), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure container hosting documentation: https://learn.microsoft.com/en-us/azure/container-apps/

- **A:** Correct. Container Apps and AKS surface stdout logs and platform events into a workspace for KQL analysis. Verbosity and retention cost money. In this case: Container termination reasons and pod events land in the workspace where limits and restarts can be correlated.
- **B:** Incorrect for this question. Platform logs and metrics must be routed before they can be queried or alerted on. Retention and cost follow the workspace settings. Why the correct answer wins: Container termination reasons and pod events land in the workspace where limits and restarts can be correlated.
- **C:** Incorrect for this question. Readiness gates traffic until the app can serve it, and liveness restarts a wedged container. Wrong thresholds cause restart loops. Why the correct answer wins: Container termination reasons and pod events land in the workspace where limits and restarts can be correlated.
- **D:** Incorrect for this question. Time-binned aggregation reveals the shape of an incident: a step change, a ramp, or a periodic spike. Averages alone hide short outages. Why the correct answer wins: Container termination reasons and pod events land in the workspace where limits and restarts can be correlated.

### Question 54 — A, C

Answers: Apply a declarative Kubernetes manifest to the cluster; Add readiness and liveness probes to the pod specification. An applied manifest makes the state repeatable, and a readiness probe withholds traffic until the app can serve. A manifest declares the desired deployment, service, and probe configuration in version control. Applying it repeatedly is idempotent. Readiness gates traffic until the app can serve it, and liveness restarts a wedged container. Wrong thresholds cause restart loops. Local study-map skill 1.6 (AKS Deployment with Manifests), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure container hosting documentation: https://learn.microsoft.com/en-us/azure/container-apps/

- **A:** Correct. Readiness gates traffic until the app can serve it, and liveness restarts a wedged container. Wrong thresholds cause restart loops. In this case: An applied manifest makes the state repeatable, and a readiness probe withholds traffic until the app can serve.
- **B:** Incorrect for this question. CPU-based scaling reacts after work is already queued and cannot scale to zero on an empty queue. It suits steady request-driven services. Why the correct answer wins: An applied manifest makes the state repeatable, and a readiness probe withholds traffic until the app can serve.
- **C:** Correct. A manifest declares the desired deployment, service, and probe configuration in version control. Applying it repeatedly is idempotent. In this case: An applied manifest makes the state repeatable, and a readiness probe withholds traffic until the app can serve.
- **D:** Incorrect for this question. HPA adjusts replicas from resource metrics but needs metrics-server and enough node capacity. It cannot scale to zero. Why the correct answer wins: An applied manifest makes the state repeatable, and a readiness probe withholds traffic until the app can serve.
- **E:** Incorrect for this question. Container Instances starts a single container group quickly for short tasks. It has no orchestrator-level scaling or revision model. Why the correct answer wins: An applied manifest makes the state repeatable, and a readiness probe withholds traffic until the app can serve.

### Question 55 — C

Answer: Write the manifest → apply it to the cluster → wait for pod readiness → test ingress connectivity. The manifest is written and applied before readiness is awaited, and connectivity is tested after the pod serves. Readiness must pass before a connectivity test proves anything, and the manifest must exist before it is applied. Local study-map skill 1.6 (AKS Deployment with Manifests), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure container hosting documentation: https://learn.microsoft.com/en-us/azure/container-apps/

- **A:** Incorrect for this question. Pods cannot become ready before the manifest is applied. Why the correct answer wins: The manifest is written and applied before readiness is awaited, and connectivity is tested after the pod serves.
- **B:** Incorrect for this question. A manifest is authored before it is applied, and connectivity is meaningless while pods are not ready. Why the correct answer wins: The manifest is written and applied before readiness is awaited, and connectivity is tested after the pod serves.
- **C:** Correct. Readiness must pass before a connectivity test proves anything, and the manifest must exist before it is applied. In this case: The manifest is written and applied before readiness is awaited, and connectivity is tested after the pod serves.
- **D:** Incorrect for this question. Ingress cannot be tested before the workload exists in the cluster. Why the correct answer wins: The manifest is written and applied before readiness is awaited, and connectivity is tested after the pod serves.

### Question 56 — D

Answer: Store the documents in Azure Cosmos DB for NoSQL. Cosmos DB for NoSQL keeps the JSON result with a plant partition key and serves point reads from one partition. Cosmos DB gives globally distributed, low-latency document access with tunable consistency. Partition key and RU planning determine the cost profile. Local study-map skill 2.1 (Cosmos DB SDK Access and Queries), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Cosmos DB and PostgreSQL vector documentation: https://learn.microsoft.com/en-us/azure/cosmos-db/

- **A:** Incorrect for this question. Queue Storage is simple and cheap for large backlogs with at-least-once delivery. It lacks topics, sessions, and scheduled messages. Why the correct answer wins: Cosmos DB for NoSQL keeps the JSON result with a plant partition key and serves point reads from one partition.
- **B:** Incorrect for this question. A point or single-partition query avoids fan-out across partitions. Cross-partition queries consume more RUs and add latency. Why the correct answer wins: Cosmos DB for NoSQL keeps the JSON result with a plant partition key and serves point reads from one partition.
- **C:** Incorrect for this question. pgvector keeps vectors beside relational data, so filters and joins run in one query. Index type and parameter tuning decide latency. Why the correct answer wins: Cosmos DB for NoSQL keeps the JSON result with a plant partition key and serves point reads from one partition.
- **D:** Correct. Cosmos DB gives globally distributed, low-latency document access with tunable consistency. Partition key and RU planning determine the cost profile. In this case: Cosmos DB for NoSQL keeps the JSON result with a plant partition key and serves point reads from one partition.

### Question 57 — A

Answer: Restrict the indexing policy to the paths the queries use. Restricting the indexing policy to the queried paths removes write charge and storage for unused properties. Selective indexing cuts write RU charge and storage for unused paths. Excluded paths cannot be filtered efficiently later. Local study-map skill 2.2 (Cosmos DB Indexing Policies and Request Units), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Cosmos DB and PostgreSQL vector documentation: https://learn.microsoft.com/en-us/azure/cosmos-db/

- **A:** Correct. Selective indexing cuts write RU charge and storage for unused paths. Excluded paths cannot be filtered efficiently later. In this case: Restricting the indexing policy to the queried paths removes write charge and storage for unused properties.
- **B:** Incorrect for this question. Autoscale follows demand between a minimum and maximum, avoiding throttling at peak without paying for peak all day. The maximum still caps the bill. Why the correct answer wins: Restricting the indexing policy to the queried paths removes write charge and storage for unused properties.
- **C:** Incorrect for this question. Indexing everything is simple and makes ad hoc queries possible, at higher write cost and storage. It is a default, not an optimization. Why the correct answer wins: Restricting the indexing policy to the queried paths removes write charge and storage for unused properties.
- **D:** Incorrect for this question. A composite index lets a query filter and order on several paths without a runtime sort. It adds write cost for exactly those paths. Why the correct answer wins: Restricting the indexing policy to the queried paths removes write charge and storage for unused properties.

### Question 58 — A

Answer: Choose the account consistency level that matches the read requirement. The account consistency level is the single documented setting that must be matched to the read requirement. Consistency trades freshness against latency, availability, and RU cost. The level is set at the account and can be relaxed per request. Local study-map skill 2.3 (Cosmos DB Consistency Levels), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Cosmos DB and PostgreSQL vector documentation: https://learn.microsoft.com/en-us/azure/cosmos-db/

- **A:** Correct. Consistency trades freshness against latency, availability, and RU cost. The level is set at the account and can be relaxed per request. In this case: The account consistency level is the single documented setting that must be matched to the read requirement.
- **B:** Incorrect for this question. Eventual consistency is the cheapest and most available option but returns possibly stale data. It fits non-critical counters, not balances. Why the correct answer wins: The account consistency level is the single documented setting that must be matched to the read requirement.
- **C:** Incorrect for this question. Session consistency guarantees monotonic reads for one session and is the common default for user-facing apps. It does not promise global freshness. Why the correct answer wins: The account consistency level is the single documented setting that must be matched to the read requirement.
- **D:** Incorrect for this question. Strong consistency guarantees the latest committed write globally at the cost of higher latency and reduced availability during partitions. Why the correct answer wins: The account consistency level is the single documented setting that must be matched to the read requirement.

### Question 59 — C

Answer: Store embeddings in a vector property and query with VectorDistance. A vector property on the same document keeps embeddings and metadata together so filters and similarity run together. Cosmos DB for NoSQL supports vector properties and a distance function for similarity search in the same document store. Dimensions and index type must match the model. Local study-map skill 2.4 (Cosmos DB Vector Search and Embeddings), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Cosmos DB and PostgreSQL vector documentation: https://learn.microsoft.com/en-us/azure/cosmos-db/

- **A:** Incorrect for this question. Application-side scoring works for tiny collections and tests, but it moves all data over the wire and does not scale with corpus size. Why the correct answer wins: A vector property on the same document keeps embeddings and metadata together so filters and similarity run together.
- **B:** Incorrect for this question. pgvector keeps vectors beside relational data, so filters and joins run in one query. Index type and parameter tuning decide latency. Why the correct answer wins: A vector property on the same document keeps embeddings and metadata together so filters and similarity run together.
- **C:** Correct. Cosmos DB for NoSQL supports vector properties and a distance function for similarity search in the same document store. Dimensions and index type must match the model. In this case: A vector property on the same document keeps embeddings and metadata together so filters and similarity run together.
- **D:** Incorrect for this question. DiskANN trades some recall for memory efficiency on large sets. Recall and latency should be measured on representative queries. Why the correct answer wins: A vector property on the same document keeps embeddings and metadata together so filters and similarity run together.

### Question 60 — A

Answer: Run a change feed processor to react to new and updated items. A change feed processor streams inserts and updates in order per partition and pushes them downstream. The change feed delivers an ordered stream of changes per partition for downstream processing. It is not a delete feed, so deletions need a workaround. Local study-map skill 2.5 (Cosmos DB Change Feed Processing), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Cosmos DB and PostgreSQL vector documentation: https://learn.microsoft.com/en-us/azure/cosmos-db/

- **A:** Correct. The change feed delivers an ordered stream of changes per partition for downstream processing. It is not a delete feed, so deletions need a workaround. In this case: A change feed processor streams inserts and updates in order per partition and pushes them downstream.
- **B:** Incorrect for this question. A duplicate-detection window drops repeated sends within the window, which helps with at-least-once producers. The window is time-bounded. Why the correct answer wins: A change feed processor streams inserts and updates in order per partition and pushes them downstream.
- **C:** Incorrect for this question. Item TTL expires documents automatically, which controls storage growth and data retention. It does not archive the expired content. Why the correct answer wins: A change feed processor streams inserts and updates in order per partition and pushes them downstream.
- **D:** Incorrect for this question. Leases track partition ownership so multiple processor instances share work and resume from a continuation token. Lease writes consume RUs too. Why the correct answer wins: A change feed processor streams inserts and updates in order per partition and pushes them downstream.

### Question 61 — A

Answer: Model typed columns for filters and one vector column for the embedding. Typed columns for station and shift beside one vector column keep predicates indexable and the embedding contract explicit. Explicit types keep filters fast and make the embedding contract clear. Storing vectors as text defeats index use. Local study-map skill 2.6 (PostgreSQL Connection and Schema Modeling), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Cosmos DB and PostgreSQL vector documentation: https://learn.microsoft.com/en-us/azure/cosmos-db/

- **A:** Correct. Explicit types keep filters fast and make the embedding contract clear. Storing vectors as text defeats index use. In this case: Typed columns for station and shift beside one vector column keep predicates indexable and the embedding contract explicit.
- **B:** Incorrect for this question. Index creation and bulk loads are I/O heavy, and throttled storage stretches maintenance windows. Storage limits are separate from compute. Why the correct answer wins: Typed columns for station and shift beside one vector column keep predicates indexable and the embedding contract explicit.
- **C:** Incorrect for this question. A replica offloads read traffic but introduces replication lag, which is dangerous for freshly written evidence. It does not reduce index memory pressure. Why the correct answer wins: Typed columns for station and shift beside one vector column keep predicates indexable and the embedding contract explicit.
- **D:** Incorrect for this question. Vector indexes are memory-hungry, so undersized compute causes swapping and slow queries. Right-size before tuning index parameters. Why the correct answer wins: Typed columns for station and shift beside one vector column keep predicates indexable and the embedding contract explicit.

### Question 62 — A

Answer: Reuse a bounded connection pool instead of opening a connection per request. A bounded connection pool reuses established sessions instead of opening one per image. A bounded pool amortizes connection setup and protects the server from connection storms. Pool size must match server limits. Local study-map skill 2.10 (PostgreSQL Connection Optimization), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Cosmos DB and PostgreSQL vector documentation: https://learn.microsoft.com/en-us/azure/cosmos-db/

- **A:** Correct. A bounded pool amortizes connection setup and protects the server from connection storms. Pool size must match server limits. In this case: A bounded connection pool reuses established sessions instead of opening one per image.
- **B:** Incorrect for this question. Prepared statements avoid repeated planning and reduce chatty network calls. They pair well with pooling but can interact with pool modes. Why the correct answer wins: A bounded connection pool reuses established sessions instead of opening one per image.
- **C:** Incorrect for this question. An external pooler multiplexes server connections for serverless or highly concurrent clients. Session-level features may be unavailable in transaction mode. Why the correct answer wins: A bounded connection pool reuses established sessions instead of opening one per image.
- **D:** Incorrect for this question. Index creation and bulk loads are I/O heavy, and throttled storage stretches maintenance windows. Storage limits are separate from compute. Why the correct answer wins: A bounded connection pool reuses established sessions instead of opening one per image.

### Question 63 — D

Answer: Cache responses in Azure Managed Redis. Caching the computed aggregate in Managed Redis stops the dashboard from repeating the same work. A cache absorbs repeated reads and cuts latency for hot data. Cache keys, TTLs, and invalidation must match the freshness requirement. Local study-map skill 2.11 (Azure Managed Redis Caching and Invalidation), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Cosmos DB and PostgreSQL vector documentation: https://learn.microsoft.com/en-us/azure/cosmos-db/

- **A:** Incorrect for this question. A replica offloads read traffic but introduces replication lag, which is dangerous for freshly written evidence. It does not reduce index memory pressure. Why the correct answer wins: Caching the computed aggregate in Managed Redis stops the dashboard from repeating the same work.
- **B:** Incorrect for this question. A TTL bounds staleness and reclaims memory without a manual sweep. Too long a TTL hides source changes; too short wastes the cache. Why the correct answer wins: Caching the computed aggregate in Managed Redis stops the dashboard from repeating the same work.
- **C:** Incorrect for this question. Queue Storage is simple and cheap for large backlogs with at-least-once delivery. It lacks topics, sessions, and scheduled messages. Why the correct answer wins: Caching the computed aggregate in Managed Redis stops the dashboard from repeating the same work.
- **D:** Correct. A cache absorbs repeated reads and cuts latency for hot data. Cache keys, TTLs, and invalidation must match the freshness requirement. In this case: Caching the computed aggregate in Managed Redis stops the dashboard from repeating the same work.

### Question 64 — A

Answer: Create a vector index in Managed Redis for similarity search. A Redis vector index serves approximate similarity from memory without a database round trip. Redis vector search serves low-latency similarity queries from memory. The corpus must fit the memory budget and be rebuilt on model change. Local study-map skill 2.12 (Azure Managed Redis Vector Indexing), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Cosmos DB and PostgreSQL vector documentation: https://learn.microsoft.com/en-us/azure/cosmos-db/

- **A:** Correct. Redis vector search serves low-latency similarity queries from memory. The corpus must fit the memory budget and be rebuilt on model change. In this case: A Redis vector index serves approximate similarity from memory without a database round trip.
- **B:** Incorrect for this question. A lock can serialize work across instances, but correctness under retries still needs idempotency keys in the data store. Locks expire and can be lost. Why the correct answer wins: A Redis vector index serves approximate similarity from memory without a database round trip.
- **C:** Incorrect for this question. A cache absorbs repeated reads and cuts latency for hot data. Cache keys, TTLs, and invalidation must match the freshness requirement. Why the correct answer wins: A Redis vector index serves approximate similarity from memory without a database round trip.
- **D:** Incorrect for this question. Session storage in Redis survives instance restarts and supports distributed instances. Sessions must be scoped and expiring. Why the correct answer wins: A Redis vector index serves approximate similarity from memory without a database round trip.

### Question 65 — A, B

Answers: Query through the Cosmos DB SDK with parameterized queries; Page large result sets with the continuation token. SDK parameterized queries stay on the supported path, and the continuation token pages the history with a bounded working set. SDK queries keep the client on the supported data plane and parameterization avoids injection and plan churn. Cross-partition queries still cost more. A continuation token returns the next page without re-sorting the previous one, which bounds response size and request charge per call. It is not a snapshot across pages. Local study-map skill 2.1 (Cosmos DB SDK Access and Queries), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Cosmos DB and PostgreSQL vector documentation: https://learn.microsoft.com/en-us/azure/cosmos-db/

- **A:** Correct. A continuation token returns the next page without re-sorting the previous one, which bounds response size and request charge per call. It is not a snapshot across pages. In this case: SDK parameterized queries stay on the supported path, and the continuation token pages the history with a bounded working set.
- **B:** Correct. SDK queries keep the client on the supported data plane and parameterization avoids injection and plan churn. Cross-partition queries still cost more. In this case: SDK parameterized queries stay on the supported path, and the continuation token pages the history with a bounded working set.
- **C:** Incorrect for this question. Indexing everything is simple and makes ad hoc queries possible, at higher write cost and storage. It is a default, not an optimization. Why the correct answer wins: SDK parameterized queries stay on the supported path, and the continuation token pages the history with a bounded working set.
- **D:** Incorrect for this question. Application-side scoring works for tiny collections and tests, but it moves all data over the wire and does not scale with corpus size. Why the correct answer wins: SDK parameterized queries stay on the supported path, and the continuation token pages the history with a bounded working set.
- **E:** Incorrect for this question. A point or single-partition query avoids fan-out across partitions. Cross-partition queries consume more RUs and add latency. Why the correct answer wins: SDK parameterized queries stay on the supported path, and the continuation token pages the history with a bounded working set.

### Question 66 — C, E

Answers: Set a TTL on each cached entry; Invalidate or overwrite the cache entry when the source changes. A TTL bounds staleness if a write is missed, and invalidation on rollover makes the new shift visible immediately. A TTL bounds staleness and reclaims memory without a manual sweep. Too long a TTL hides source changes; too short wastes the cache. Write-through or explicit invalidation keeps cached answers consistent with the system of record. Without it, TTL is the only bound on staleness. Local study-map skill 2.11 (Azure Managed Redis Caching and Invalidation), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Cosmos DB and PostgreSQL vector documentation: https://learn.microsoft.com/en-us/azure/cosmos-db/

- **A:** Incorrect for this question. Flushing removes all cached content at once, causing a stampede to the origin and a latency cliff. Targeted invalidation is safer. Why the correct answer wins: A TTL bounds staleness if a write is missed, and invalidation on rollover makes the new shift visible immediately.
- **B:** Incorrect for this question. A lock can serialize work across instances, but correctness under retries still needs idempotency keys in the data store. Locks expire and can be lost. Why the correct answer wins: A TTL bounds staleness if a write is missed, and invalidation on rollover makes the new shift visible immediately.
- **C:** Correct. A TTL bounds staleness and reclaims memory without a manual sweep. Too long a TTL hides source changes; too short wastes the cache. In this case: A TTL bounds staleness if a write is missed, and invalidation on rollover makes the new shift visible immediately.
- **D:** Incorrect for this question. Eviction protects memory but evicts unpredictably, so a hot key can vanish before its freshness bound is reached. It is not a substitute for TTL design. Why the correct answer wins: A TTL bounds staleness if a write is missed, and invalidation on rollover makes the new shift visible immediately.
- **E:** Correct. Write-through or explicit invalidation keeps cached answers consistent with the system of record. Without it, TTL is the only bound on staleness. In this case: A TTL bounds staleness if a write is missed, and invalidation on rollover makes the new shift visible immediately.

### Question 67 — C

Answer: Check the cache → on a miss query the source → write the value with a TTL → invalidate the entry when the source changes → serve the next request from the cache. The cache is checked first, misses fall back to the source, values are written with a TTL, and writes invalidate. The sequence is cache-first, source on miss, populate with expiry, invalidate on write, then serve from cache. Local study-map skill 2.11 (Azure Managed Redis Caching and Invalidation), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Cosmos DB and PostgreSQL vector documentation: https://learn.microsoft.com/en-us/azure/cosmos-db/

- **A:** Incorrect for this question. Invalidation precedes the write it is meant to follow, and the read order is reversed. Why the correct answer wins: The cache is checked first, misses fall back to the source, values are written with a TTL, and writes invalidate.
- **B:** Incorrect for this question. A value cannot be written before it has been read, so the ordering is impossible. Why the correct answer wins: The cache is checked first, misses fall back to the source, values are written with a TTL, and writes invalidate.
- **C:** Correct. The sequence is cache-first, source on miss, populate with expiry, invalidate on write, then serve from cache. In this case: The cache is checked first, misses fall back to the source, values are written with a TTL, and writes invalidate.
- **D:** Incorrect for this question. Querying the source before checking the cache defeats the cache and doubles read load. Why the correct answer wins: The cache is checked first, misses fall back to the source, values are written with a TTL, and writes invalidate.

### Question 68 — A

Answer: Add a SQL or correlation filter to a subscription. A subscription filter evaluates message properties broker-side so only matching defects are delivered. Subscription filters route only matching messages to a handler, reducing wasted processing. Filter evaluation happens broker-side on message properties. Local study-map skill 3.2 (Service Bus Topics, Subscriptions, and Filters), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure messaging and Functions documentation: https://learn.microsoft.com/en-us/azure/service-bus-messaging/

- **A:** Correct. Subscription filters route only matching messages to a handler, reducing wasted processing. Filter evaluation happens broker-side on message properties. In this case: A subscription filter evaluates message properties broker-side so only matching defects are delivered.
- **B:** Incorrect for this question. A duplicate-detection window drops repeated sends within the window, which helps with at-least-once producers. The window is time-bounded. Why the correct answer wins: A subscription filter evaluates message properties broker-side so only matching defects are delivered.
- **C:** Incorrect for this question. Subject and event-type filters keep handlers focused and reduce cost. Filters are evaluated on event metadata, not payload body. Why the correct answer wins: A subscription filter evaluates message properties broker-side so only matching defects are delivered.
- **D:** Incorrect for this question. A custom schema fits domain events that are not resource lifecycle notifications. Consumers must version the schema contract. Why the correct answer wins: A subscription filter evaluates message properties broker-side so only matching defects are delivered.

### Question 69 — A

Answer: Inspect the dead-letter queue and resubmit corrected messages. The dead-letter queue holds messages that exhausted delivery attempts so they can be examined and resubmitted. Dead-lettering preserves poison messages for diagnosis instead of losing them. Resubmission needs a fix and an idempotent handler. Local study-map skill 3.3 (Service Bus Dead-Lettering and Retries), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure messaging and Functions documentation: https://learn.microsoft.com/en-us/azure/service-bus-messaging/

- **A:** Correct. Dead-lettering preserves poison messages for diagnosis instead of losing them. Resubmission needs a fix and an idempotent handler. In this case: The dead-letter queue holds messages that exhausted delivery attempts so they can be examined and resubmitted.
- **B:** Incorrect for this question. Prepared statements avoid repeated planning and reduce chatty network calls. They pair well with pooling but can interact with pool modes. Why the correct answer wins: The dead-letter queue holds messages that exhausted delivery attempts so they can be examined and resubmitted.
- **C:** Incorrect for this question. A duplicate-detection window drops repeated sends within the window, which helps with at-least-once producers. The window is time-bounded. Why the correct answer wins: The dead-letter queue holds messages that exhausted delivery attempts so they can be examined and resubmitted.
- **D:** Incorrect for this question. Receive-and-delete removes the message on delivery, so a crash loses work silently. It suits telemetry, not payments. Why the correct answer wins: The dead-letter queue holds messages that exhausted delivery attempts so they can be examined and resubmitted.

### Question 70 — D

Answer: Make the handler idempotent by using a message or business key. An idempotency key derived from the capture identifier turns a replay into a no-op instead of a duplicate write. At-least-once delivery means duplicates will happen, so the write must tolerate replay. A stored key makes the retry safe. Local study-map skill 3.3 (Service Bus Dead-Lettering and Retries), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure messaging and Functions documentation: https://learn.microsoft.com/en-us/azure/service-bus-messaging/

- **A:** Incorrect for this question. Receive-and-delete removes the message on delivery, so a crash loses work silently. It suits telemetry, not payments. Why the correct answer wins: An idempotency key derived from the capture identifier turns a replay into a no-op instead of a duplicate write.
- **B:** Incorrect for this question. Peek-lock keeps the message locked until the handler completes it, giving at-least-once processing with retry. Lock duration must exceed processing time. Why the correct answer wins: An idempotency key derived from the capture identifier turns a replay into a no-op instead of a duplicate write.
- **C:** Incorrect for this question. A duplicate-detection window drops repeated sends within the window, which helps with at-least-once producers. The window is time-bounded. Why the correct answer wins: An idempotency key derived from the capture identifier turns a replay into a no-op instead of a duplicate write.
- **D:** Correct. At-least-once delivery means duplicates will happen, so the write must tolerate replay. A stored key makes the retry safe. In this case: An idempotency key derived from the capture identifier turns a replay into a no-op instead of a duplicate write.

### Question 71 — B

Answer: Publish the state change as an Event Grid event. An Event Grid subscription on the storage system topic pushes blob-created events as soon as the image lands. Event Grid delivers discrete notifications to subscribers with retries and filtering. It carries events, not large payloads or ordered streams. Local study-map skill 3.4 (Event Grid Filters, Custom Events, and Retries), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure messaging and Functions documentation: https://learn.microsoft.com/en-us/azure/service-bus-messaging/

- **A:** Incorrect for this question. Queue Storage is simple and cheap for large backlogs with at-least-once delivery. It lacks topics, sessions, and scheduled messages. Why the correct answer wins: An Event Grid subscription on the storage system topic pushes blob-created events as soon as the image lands.
- **B:** Correct. Event Grid delivers discrete notifications to subscribers with retries and filtering. It carries events, not large payloads or ordered streams. In this case: An Event Grid subscription on the storage system topic pushes blob-created events as soon as the image lands.
- **C:** Incorrect for this question. Event Hubs ingests high-volume ordered streams with partitions and consumer groups. It is a streaming log, not a task queue. Why the correct answer wins: An Event Grid subscription on the storage system topic pushes blob-created events as soon as the image lands.
- **D:** Incorrect for this question. Durable Functions provides orchestrations, activities, timers, and retries with checkpointed state. Orchestrator code must stay deterministic. Why the correct answer wins: An Event Grid subscription on the storage system topic pushes blob-created events as soon as the image lands.

### Question 72 — B

Answer: Bind a queue or event trigger to the function. A queue trigger starts the function when the message arrives and manages the receive loop for the app. A trigger starts the function when work arrives and handles the receive loop for you. Poison-message behavior is configured in host settings. Local study-map skill 3.5 (Azure Functions Triggers and Bindings), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure messaging and Functions documentation: https://learn.microsoft.com/en-us/azure/service-bus-messaging/

- **A:** Incorrect for this question. An HTTP trigger gives a synchronous API endpoint with route and authorization configuration. Long-running work should hand off to a queue. Why the correct answer wins: A queue trigger starts the function when the message arrives and manages the receive loop for the app.
- **B:** Correct. A trigger starts the function when work arrives and handles the receive loop for you. Poison-message behavior is configured in host settings. In this case: A queue trigger starts the function when the message arrives and manages the receive loop for the app.
- **C:** Incorrect for this question. Durable Functions provides orchestrations, activities, timers, and retries with checkpointed state. Orchestrator code must stay deterministic. Why the correct answer wins: A queue trigger starts the function when the message arrives and manages the receive loop for the app.
- **D:** Incorrect for this question. Bindings reduce boilerplate for common inputs and outputs and are configured declaratively. Complex operations still need the SDK. Why the correct answer wins: A queue trigger starts the function when the message arrives and manages the receive loop for the app.

### Question 73 — C

Answer: Use input and output bindings instead of hand-written SDK calls. An output binding lets the runtime write to the store without client construction or connection handling. Bindings reduce boilerplate for common inputs and outputs and are configured declaratively. Complex operations still need the SDK. Local study-map skill 3.5 (Azure Functions Triggers and Bindings), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure messaging and Functions documentation: https://learn.microsoft.com/en-us/azure/service-bus-messaging/

- **A:** Incorrect for this question. A trigger starts the function when work arrives and handles the receive loop for you. Poison-message behavior is configured in host settings. Why the correct answer wins: An output binding lets the runtime write to the store without client construction or connection handling.
- **B:** Incorrect for this question. Durable Functions provides orchestrations, activities, timers, and retries with checkpointed state. Orchestrator code must stay deterministic. Why the correct answer wins: An output binding lets the runtime write to the store without client construction or connection handling.
- **C:** Correct. Bindings reduce boilerplate for common inputs and outputs and are configured declaratively. Complex operations still need the SDK. In this case: An output binding lets the runtime write to the store without client construction or connection handling.
- **D:** Incorrect for this question. An HTTP trigger gives a synchronous API endpoint with route and authorization configuration. Long-running work should hand off to a queue. Why the correct answer wins: An output binding lets the runtime write to the store without client construction or connection handling.

### Question 74 — D

Answer: Host the function app on a premium plan with pre-warmed instances. A premium plan provides pre-warmed instances and virtual network integration for private endpoints. A premium plan reduces cold starts and supports virtual network integration and longer timeouts. It costs more than consumption. Local study-map skill 3.6 (Function App Configuration and Deployment), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure messaging and Functions documentation: https://learn.microsoft.com/en-us/azure/service-bus-messaging/

- **A:** Incorrect for this question. Consumption bills per execution and scales automatically, with cold starts and a timeout ceiling. It fits spiky, short work. Why the correct answer wins: A premium plan provides pre-warmed instances and virtual network integration for private endpoints.
- **B:** Incorrect for this question. An HTTP trigger gives a synchronous API endpoint with route and authorization configuration. Long-running work should hand off to a queue. Why the correct answer wins: A premium plan provides pre-warmed instances and virtual network integration for private endpoints.
- **C:** Incorrect for this question. Durable Functions provides orchestrations, activities, timers, and retries with checkpointed state. Orchestrator code must stay deterministic. Why the correct answer wins: A premium plan provides pre-warmed instances and virtual network integration for private endpoints.
- **D:** Correct. A premium plan reduces cold starts and supports virtual network integration and longer timeouts. It costs more than consumption. In this case: A premium plan provides pre-warmed instances and virtual network integration for private endpoints.

### Question 75 — B

Answer: Tune the function app concurrency and batch size. Lower concurrency and batch size per instance bound the parallel calls that a burst can push at the endpoint. Concurrency and batch size bound how much work one instance takes at a time, which controls downstream pressure and memory. Too high a value causes throttling and timeouts. Local study-map skill 3.6 (Function App Configuration and Deployment), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure messaging and Functions documentation: https://learn.microsoft.com/en-us/azure/service-bus-messaging/

- **A:** Incorrect for this question. A premium plan reduces cold starts and supports virtual network integration and longer timeouts. It costs more than consumption. Why the correct answer wins: Lower concurrency and batch size per instance bound the parallel calls that a burst can push at the endpoint.
- **B:** Correct. Concurrency and batch size bound how much work one instance takes at a time, which controls downstream pressure and memory. Too high a value causes throttling and timeouts. In this case: Lower concurrency and batch size per instance bound the parallel calls that a burst can push at the endpoint.
- **C:** Incorrect for this question. The host retry policy re-executes a failing trigger with bounded attempts and backoff. It cannot make a non-idempotent handler safe to replay. Why the correct answer wins: Lower concurrency and batch size per instance bound the parallel calls that a burst can push at the endpoint.
- **D:** Incorrect for this question. Consumption bills per execution and scales automatically, with cold starts and a timeout ceiling. It fits spiky, short work. Why the correct answer wins: Lower concurrency and batch size per instance bound the parallel calls that a burst can push at the endpoint.

### Question 76 — B, E

Answers: Publish to a Service Bus topic with multiple subscriptions; Add a SQL or correlation filter to a subscription. A topic with separate subscriptions provides fan-out, and a subscription filter limits escalation to severe defects. Topics fan out one message to independent subscribers, each with its own filter and dead-letter queue. Subscribers process at their own pace. Subscription filters route only matching messages to a handler, reducing wasted processing. Filter evaluation happens broker-side on message properties. Local study-map skill 3.2 (Service Bus Topics, Subscriptions, and Filters), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure messaging and Functions documentation: https://learn.microsoft.com/en-us/azure/service-bus-messaging/

- **A:** Incorrect for this question. A queue decouples producers from a single consumer group and smooths bursts. Delivery semantics depend on receive mode and completion. Why the correct answer wins: A topic with separate subscriptions provides fan-out, and a subscription filter limits escalation to severe defects.
- **B:** Correct. Subscription filters route only matching messages to a handler, reducing wasted processing. Filter evaluation happens broker-side on message properties. In this case: A topic with separate subscriptions provides fan-out, and a subscription filter limits escalation to severe defects.
- **C:** Incorrect for this question. Queue Storage is simple and cheap for large backlogs with at-least-once delivery. It lacks topics, sessions, and scheduled messages. Why the correct answer wins: A topic with separate subscriptions provides fan-out, and a subscription filter limits escalation to severe defects.
- **D:** Incorrect for this question. Subject and event-type filters keep handlers focused and reduce cost. Filters are evaluated on event metadata, not payload body. Why the correct answer wins: A topic with separate subscriptions provides fan-out, and a subscription filter limits escalation to severe defects.
- **E:** Correct. Topics fan out one message to independent subscribers, each with its own filter and dead-letter queue. Subscribers process at their own pace. In this case: A topic with separate subscriptions provides fan-out, and a subscription filter limits escalation to severe defects.

### Question 77 — B, C

Answers: Assign a managed identity to the function app and use it for downstream calls; Deploy the function app through a CI pipeline with app settings applied. A managed identity removes the stored key, and a pipeline deployment applies the settings the function needs. A function app can authenticate with a managed identity, so no connection secret is needed in app settings. Pipeline deployment keeps code and configuration versioned together and repeatable. Secrets belong in a vault reference, not in the pipeline file. Local study-map skill 3.6 (Function App Configuration and Deployment), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure messaging and Functions documentation: https://learn.microsoft.com/en-us/azure/service-bus-messaging/

- **A:** Incorrect for this question. Application settings become environment variables for the container and can be swapped per slot. Sensitive values should still reference a vault. Why the correct answer wins: A managed identity removes the stored key, and a pipeline deployment applies the settings the function needs.
- **B:** Correct. A function app can authenticate with a managed identity, so no connection secret is needed in app settings. In this case: A managed identity removes the stored key, and a pipeline deployment applies the settings the function needs.
- **C:** Correct. Pipeline deployment keeps code and configuration versioned together and repeatable. Secrets belong in a vault reference, not in the pipeline file. In this case: A managed identity removes the stored key, and a pipeline deployment applies the settings the function needs.
- **D:** Incorrect for this question. An HTTP trigger gives a synchronous API endpoint with route and authorization configuration. Long-running work should hand off to a queue. Why the correct answer wins: A managed identity removes the stored key, and a pipeline deployment applies the settings the function needs.
- **E:** Incorrect for this question. A premium plan reduces cold starts and supports virtual network integration and longer timeouts. It costs more than consumption. Why the correct answer wins: A managed identity removes the stored key, and a pipeline deployment applies the settings the function needs.

### Question 78 — D

Answer: Publish a custom event → evaluate the subscription filter → deliver to the handler → retry on failure → dead-letter undeliverable events. Publication precedes filtering, delivery precedes retries, and dead-lettering follows exhausted retries. Filtering happens before delivery, retries handle transient failures, and dead-lettering preserves what cannot be delivered. Local study-map skill 3.4 (Event Grid Filters, Custom Events, and Retries), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure messaging and Functions documentation: https://learn.microsoft.com/en-us/azure/service-bus-messaging/

- **A:** Incorrect for this question. A filter is evaluated before delivery, and retries must occur before dead-lettering. Why the correct answer wins: Publication precedes filtering, delivery precedes retries, and dead-lettering follows exhausted retries.
- **B:** Incorrect for this question. A filter cannot evaluate an event that has not been published. Why the correct answer wins: Publication precedes filtering, delivery precedes retries, and dead-lettering follows exhausted retries.
- **C:** Incorrect for this question. Delivery cannot precede publication and filtering. Why the correct answer wins: Publication precedes filtering, delivery precedes retries, and dead-lettering follows exhausted retries.
- **D:** Correct. Filtering happens before delivery, retries handle transient failures, and dead-lettering preserves what cannot be delivered. In this case: Publication precedes filtering, delivery precedes retries, and dead-lettering follows exhausted retries.

### Question 79 — C

Answer: Store the secret in Azure Key Vault and read it at runtime. Key Vault stores the key with version history and audit logging, and the function reads it at runtime. A vault centralizes secret storage with access control and audit. Retrieval should use an identity, not a copied credential. Local study-map skill 4.1 (Key Vault Secret Storage, Rotation, and Retrieval), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Key Vault, App Configuration, and Monitor documentation: https://learn.microsoft.com/en-us/azure/azure-monitor/

- **A:** Incorrect for this question. A scoped role grants only the operations the app performs and limits blast radius. Prefer built-in roles over broad contributor grants. Why the correct answer wins: Key Vault stores the key with version history and audit logging, and the function reads it at runtime.
- **B:** Incorrect for this question. App Configuration separates configuration from code and supports labels, feature flags, and Key Vault references. Change still needs a refresh strategy. Why the correct answer wins: Key Vault stores the key with version history and audit logging, and the function reads it at runtime.
- **C:** Correct. A vault centralizes secret storage with access control and audit. Retrieval should use an identity, not a copied credential. In this case: Key Vault stores the key with version history and audit logging, and the function reads it at runtime.
- **D:** Incorrect for this question. A Key Vault reference resolves at runtime so the secret is never written into application settings. The app identity still needs permission to read it. Why the correct answer wins: Key Vault stores the key with version history and audit logging, and the function reads it at runtime.

### Question 80 — C

Answer: Rotate the secret on a schedule and let apps resolve the current version. Rotation issues a new version, and the function resolves the current version so no deployment is needed. Rotation limits the value of a leaked secret, but callers must read the latest version rather than caching an old one forever. Local study-map skill 4.1 (Key Vault Secret Storage, Rotation, and Retrieval), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Key Vault, App Configuration, and Monitor documentation: https://learn.microsoft.com/en-us/azure/azure-monitor/

- **A:** Incorrect for this question. Soft delete and purge protection stop accidental or malicious permanent loss of secrets. They also constrain how names can be reused. Why the correct answer wins: Rotation issues a new version, and the function resolves the current version so no deployment is needed.
- **B:** Incorrect for this question. Pinning a version makes a rotation invisible to the app until it is redeployed, which is useful for break-glass and dangerous for routine rotation. Why the correct answer wins: Rotation issues a new version, and the function resolves the current version so no deployment is needed.
- **C:** Correct. Rotation limits the value of a leaked secret, but callers must read the latest version rather than caching an old one forever. In this case: Rotation issues a new version, and the function resolves the current version so no deployment is needed.
- **D:** Incorrect for this question. A managed identity issues tokens from the platform, removing secret distribution from the app. Role assignment still scopes what it can reach. Why the correct answer wins: Rotation issues a new version, and the function resolves the current version so no deployment is needed.

### Question 81 — D

Answer: Store settings and feature flags in Azure App Configuration. App Configuration centralizes settings and flags and keeps plant-specific values apart with labels. App Configuration separates configuration from code and supports labels, feature flags, and Key Vault references. Change still needs a refresh strategy. Local study-map skill 4.2 (App Configuration Settings and Feature Flags), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Key Vault, App Configuration, and Monitor documentation: https://learn.microsoft.com/en-us/azure/azure-monitor/

- **A:** Incorrect for this question. Sentinel-key or polling refresh lets a running app pick up new settings. Refresh intervals trade responsiveness against request volume. Why the correct answer wins: App Configuration centralizes settings and flags and keeps plant-specific values apart with labels.
- **B:** Incorrect for this question. A Key Vault reference keeps non-secret settings in App Configuration while the value stays in the vault. The app identity needs both sets of permissions. Why the correct answer wins: App Configuration centralizes settings and flags and keeps plant-specific values apart with labels.
- **C:** Incorrect for this question. Labels keep dev, test, and prod values in one store with one key schema. A misconfigured label selector silently serves the wrong values. Why the correct answer wins: App Configuration centralizes settings and flags and keeps plant-specific values apart with labels.
- **D:** Correct. App Configuration separates configuration from code and supports labels, feature flags, and Key Vault references. Change still needs a refresh strategy. In this case: App Configuration centralizes settings and flags and keeps plant-specific values apart with labels.

### Question 82 — D

Answer: Instrument the service with the OpenTelemetry SDK. OpenTelemetry instrumentation records spans across the workflow so one trace covers every hop. OpenTelemetry emits vendor-neutral traces, metrics, and logs with context propagation. Exporters and sampling decide what reaches the backend. Local study-map skill 4.3 (Distributed Tracing with OpenTelemetry), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Key Vault, App Configuration, and Monitor documentation: https://learn.microsoft.com/en-us/azure/azure-monitor/

- **A:** Incorrect for this question. KQL filters, projects, and aggregates log and metric tables in Log Analytics. Start narrow with a time range and a request ID. Why the correct answer wins: OpenTelemetry instrumentation records spans across the workflow so one trace covers every hop.
- **B:** Incorrect for this question. Application Insights correlates requests, dependencies, and exceptions into end-to-end transactions. Sampling can hide rare failures. Why the correct answer wins: OpenTelemetry instrumentation records spans across the workflow so one trace covers every hop.
- **C:** Incorrect for this question. Including the trace ID in log records lets you pivot from a failed span to its log lines. Without it, logs and traces are separate worlds. Why the correct answer wins: OpenTelemetry instrumentation records spans across the workflow so one trace covers every hop.
- **D:** Correct. OpenTelemetry emits vendor-neutral traces, metrics, and logs with context propagation. Exporters and sampling decide what reaches the backend. In this case: OpenTelemetry instrumentation records spans across the workflow so one trace covers every hop.

### Question 83 — D

Answer: Query the workspace with KQL to find the failing operation. KQL over the workspace returns the failing operation and its correlation identifier without a code change. KQL filters, projects, and aggregates log and metric tables in Log Analytics. Start narrow with a time range and a request ID. Local study-map skill 4.4 (KQL Queries for Logs and Metrics), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Key Vault, App Configuration, and Monitor documentation: https://learn.microsoft.com/en-us/azure/azure-monitor/

- **A:** Incorrect for this question. Time-binned aggregation reveals the shape of an incident: a step change, a ramp, or a periodic spike. Averages alone hide short outages. Why the correct answer wins: KQL over the workspace returns the failing operation and its correlation identifier without a code change.
- **B:** Incorrect for this question. Joining request and dependency telemetry shows which downstream call fails inside a slow request. Cross-workspace joins need the right scope. Why the correct answer wins: KQL over the workspace returns the failing operation and its correlation identifier without a code change.
- **C:** Incorrect for this question. Platform metrics are cheap and near-real-time, so they suit latency and failure-rate alerts. Log-based alerts add latency and query cost. Why the correct answer wins: KQL over the workspace returns the failing operation and its correlation identifier without a code change.
- **D:** Correct. KQL filters, projects, and aggregates log and metric tables in Log Analytics. Start narrow with a time range and a request ID. In this case: KQL over the workspace returns the failing operation and its correlation identifier without a code change.

### Question 84 — C

Answer: Authenticate with a managed identity instead of a stored key. A managed identity gives the function an Azure token, so no key or connection string is stored anywhere. A managed identity issues tokens from the platform, removing secret distribution from the app. Role assignment still scopes what it can reach. Local study-map skill 4.5 (Identity-Based Access for Application Services), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Key Vault, App Configuration, and Monitor documentation: https://learn.microsoft.com/en-us/azure/azure-monitor/

- **A:** Incorrect for this question. Soft delete and purge protection stop accidental or malicious permanent loss of secrets. They also constrain how names can be reused. Why the correct answer wins: A managed identity gives the function an Azure token, so no key or connection string is stored anywhere.
- **B:** Incorrect for this question. A Key Vault reference resolves at runtime so the secret is never written into application settings. The app identity still needs permission to read it. Why the correct answer wins: A managed identity gives the function an Azure token, so no key or connection string is stored anywhere.
- **C:** Correct. A managed identity issues tokens from the platform, removing secret distribution from the app. Role assignment still scopes what it can reach. In this case: A managed identity gives the function an Azure token, so no key or connection string is stored anywhere.
- **D:** Incorrect for this question. Pinning a version makes a rotation invisible to the app until it is redeployed, which is useful for break-glass and dangerous for routine rotation. Why the correct answer wins: A managed identity gives the function an Azure token, so no key or connection string is stored anywhere.

### Question 85 — C, E

Answers: Aggregate with summarize and bin to see the failure rate over time; Project only the columns needed and filter by time first. summarize with bin produces the per-bucket rate, and projecting only needed columns cuts scanned data. Time-binned aggregation reveals the shape of an incident: a step change, a ramp, or a periodic spike. Averages alone hide short outages. Reducing columns and rows early lowers query cost and latency. Broad queries over long ranges are the usual cause of slow KQL. Local study-map skill 4.4 (KQL Queries for Logs and Metrics), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Key Vault, App Configuration, and Monitor documentation: https://learn.microsoft.com/en-us/azure/azure-monitor/

- **A:** Incorrect for this question. Retention and the table plan determine how long data is queryable and what it costs. Lower retention reduces cost but shortens the investigation window. Why the correct answer wins: summarize with bin produces the per-bucket rate, and projecting only needed columns cuts scanned data.
- **B:** Incorrect for this question. Precomputed results avoid recomputing expensive aggregations on every dashboard refresh. The trade-off is storage and freshness lag. Why the correct answer wins: summarize with bin produces the per-bucket rate, and projecting only needed columns cuts scanned data.
- **C:** Correct. Reducing columns and rows early lowers query cost and latency. Broad queries over long ranges are the usual cause of slow KQL. In this case: summarize with bin produces the per-bucket rate, and projecting only needed columns cuts scanned data.
- **D:** Incorrect for this question. Joining request and dependency telemetry shows which downstream call fails inside a slow request. Cross-workspace joins need the right scope. Why the correct answer wins: summarize with bin produces the per-bucket rate, and projecting only needed columns cuts scanned data.
- **E:** Correct. Time-binned aggregation reveals the shape of an incident: a step change, a ramp, or a periodic spike. Averages alone hide short outages. In this case: summarize with bin produces the per-bucket rate, and projecting only needed columns cuts scanned data.

### Question 86 — A, C

Answers: Enable configuration refresh so changes apply without a restart; Ship the code dark behind a feature flag. A feature flag enables the code dark, and refresh delivers the changed value to running instances. Sentinel-key or polling refresh lets a running app pick up new settings. Refresh intervals trade responsiveness against request volume. A feature flag enables reviewed code in production without a redeploy and lets it be switched off instantly. Flag state still needs ownership and cleanup. Local study-map skill 4.2 (App Configuration Settings and Feature Flags), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Key Vault, App Configuration, and Monitor documentation: https://learn.microsoft.com/en-us/azure/azure-monitor/

- **A:** Correct. Sentinel-key or polling refresh lets a running app pick up new settings. Refresh intervals trade responsiveness against request volume. In this case: A feature flag enables the code dark, and refresh delivers the changed value to running instances.
- **B:** Incorrect for this question. Labels keep dev, test, and prod values in one store with one key schema. A misconfigured label selector silently serves the wrong values. Why the correct answer wins: A feature flag enables the code dark, and refresh delivers the changed value to running instances.
- **C:** Correct. A feature flag enables reviewed code in production without a redeploy and lets it be switched off instantly. Flag state still needs ownership and cleanup. In this case: A feature flag enables the code dark, and refresh delivers the changed value to running instances.
- **D:** Incorrect for this question. Pinning a version makes a rotation invisible to the app until it is redeployed, which is useful for break-glass and dangerous for routine rotation. Why the correct answer wins: A feature flag enables the code dark, and refresh delivers the changed value to running instances.
- **E:** Incorrect for this question. A Key Vault reference keeps non-secret settings in App Configuration while the value stays in the vault. The app identity needs both sets of permissions. Why the correct answer wins: A feature flag enables the code dark, and refresh delivers the changed value to running instances.

### Question 87 — A, B

Answers: Grant the app identity data-plane access to the vault; Enable purge protection and soft delete on the vault. A data-plane role assignment lets the identity read the secret, and purge protection keeps the vault recoverable. Vault access is a separate authorization decision from the app identity. Without a data-plane role or policy the reference fails at runtime. Soft delete and purge protection stop accidental or malicious permanent loss of secrets. They also constrain how names can be reused. Local study-map skill 4.1 (Key Vault Secret Storage, Rotation, and Retrieval), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Key Vault, App Configuration, and Monitor documentation: https://learn.microsoft.com/en-us/azure/azure-monitor/

- **A:** Correct. Vault access is a separate authorization decision from the app identity. Without a data-plane role or policy the reference fails at runtime. In this case: A data-plane role assignment lets the identity read the secret, and purge protection keeps the vault recoverable.
- **B:** Correct. Soft delete and purge protection stop accidental or malicious permanent loss of secrets. They also constrain how names can be reused. In this case: A data-plane role assignment lets the identity read the secret, and purge protection keeps the vault recoverable.
- **C:** Incorrect for this question. Pinning a version makes a rotation invisible to the app until it is redeployed, which is useful for break-glass and dangerous for routine rotation. Why the correct answer wins: A data-plane role assignment lets the identity read the secret, and purge protection keeps the vault recoverable.
- **D:** Incorrect for this question. A vault centralizes secret storage with access control and audit. Retrieval should use an identity, not a copied credential. Why the correct answer wins: A data-plane role assignment lets the identity read the secret, and purge protection keeps the vault recoverable.
- **E:** Incorrect for this question. Rotation limits the value of a leaked secret, but callers must read the latest version rather than caching an old one forever. Why the correct answer wins: A data-plane role assignment lets the identity read the secret, and purge protection keeps the vault recoverable.

### Question 88 — C

Answer: Create the function app with a managed identity → grant the identity access to the vault → reference the secret in application settings → deploy through the pipeline → verify a queue-triggered invocation. Identity and permission come before the secret reference, and deployment precedes the verification invocation. Identity, permission, and reference must exist before deployment, and verification follows the deployment. Local study-map skill 4.3 (Distributed Tracing with OpenTelemetry), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Key Vault, App Configuration, and Monitor documentation: https://learn.microsoft.com/en-us/azure/azure-monitor/

- **A:** Incorrect for this question. Permission cannot be granted before the identity exists, and the reference is missing at deploy time. Why the correct answer wins: Identity and permission come before the secret reference, and deployment precedes the verification invocation.
- **B:** Incorrect for this question. Verification cannot precede the deployment it verifies. Why the correct answer wins: Identity and permission come before the secret reference, and deployment precedes the verification invocation.
- **C:** Correct. Identity, permission, and reference must exist before deployment, and verification follows the deployment. In this case: Identity and permission come before the secret reference, and deployment precedes the verification invocation.
- **D:** Incorrect for this question. The deployment would run before the identity and its access exist. Why the correct answer wins: Identity and permission come before the secret reference, and deployment precedes the verification invocation.

### Question 89 — A

Answer: Scale compute and memory to fit index size and query concurrency. Memory must fit the vector working set under concurrency, or the index is read from disk and recall degrades. Vector indexes are memory-hungry, so undersized compute causes swapping and slow queries. Right-size before tuning index parameters. Local study-map skill 2.8 (PostgreSQL Compute, Memory, and Storage Sizing), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Cosmos DB and PostgreSQL vector documentation: https://learn.microsoft.com/en-us/azure/cosmos-db/

- **A:** Correct. Vector indexes are memory-hungry, so undersized compute causes swapping and slow queries. Right-size before tuning index parameters. In this case: Memory must fit the vector working set under concurrency, or the index is read from disk and recall degrades.
- **B:** Incorrect for this question. Statistics and dead-tuple cleanup change plan quality and index performance. Autovacuum tuning matters for churn-heavy vector tables. Why the correct answer wins: Memory must fit the vector working set under concurrency, or the index is read from disk and recall degrades.
- **C:** Incorrect for this question. A replica offloads read traffic but introduces replication lag, which is dangerous for freshly written evidence. It does not reduce index memory pressure. Why the correct answer wins: Memory must fit the vector working set under concurrency, or the index is read from disk and recall degrades.
- **D:** Incorrect for this question. Index creation and bulk loads are I/O heavy, and throttled storage stretches maintenance windows. Storage limits are separate from compute. Why the correct answer wins: Memory must fit the vector working set under concurrency, or the index is read from disk and recall degrades.

### Question 90 — B

Answer: Filter on metadata columns in the same query as the vector search. Filtering on metadata inside the same statement as the distance operator keeps the result scoped and complete. Combining a WHERE filter with the distance operator keeps retrieval inside the caller's scope and improves relevance. Index the filter columns too. Local study-map skill 2.9 (PostgreSQL RAG with Metadata Filters), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Cosmos DB and PostgreSQL vector documentation: https://learn.microsoft.com/en-us/azure/cosmos-db/

- **A:** Incorrect for this question. Post-filtering can return fewer results than requested and can leak existence or counts if the filtering is careless. Push authorization into the query. Why the correct answer wins: Filtering on metadata inside the same statement as the distance operator keeps the result scoped and complete.
- **B:** Correct. Combining a WHERE filter with the distance operator keeps retrieval inside the caller's scope and improves relevance. Index the filter columns too. In this case: Filtering on metadata inside the same statement as the distance operator keeps the result scoped and complete.
- **C:** Incorrect for this question. HNSW gives fast approximate nearest-neighbour queries with a larger memory footprint and slower builds. Recall is tunable at query time. Why the correct answer wins: Filtering on metadata inside the same statement as the distance operator keeps the result scoped and complete.
- **D:** Incorrect for this question. IVFFlat uses clustering lists and needs periodic rebuilds as data grows, but costs less memory than HNSW. Probes trade recall for speed. Why the correct answer wins: Filtering on metadata inside the same statement as the distance operator keeps the result scoped and complete.

### Question 91 — D

Answer: Create a custom span around each downstream call. A custom span around the model call records its duration and makes the dominant hop visible. A span records the duration and outcome of one operation and nests under the trace. It makes the slow dependency visible in the transaction view. Local study-map skill 4.3 (Distributed Tracing with OpenTelemetry), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Key Vault, App Configuration, and Monitor documentation: https://learn.microsoft.com/en-us/azure/azure-monitor/

- **A:** Incorrect for this question. Including the trace ID in log records lets you pivot from a failed span to its log lines. Without it, logs and traces are separate worlds. Why the correct answer wins: A custom span around the model call records its duration and makes the dominant hop visible.
- **B:** Incorrect for this question. Propagation stitches one trace across HTTP, messaging, and Functions so the whole path is visible. Missing propagation breaks the trace at that hop. Why the correct answer wins: A custom span around the model call records its duration and makes the dominant hop visible.
- **C:** Incorrect for this question. OpenTelemetry emits vendor-neutral traces, metrics, and logs with context propagation. Exporters and sampling decide what reaches the backend. Why the correct answer wins: A custom span around the model call records its duration and makes the dominant hop visible.
- **D:** Correct. A span records the duration and outcome of one operation and nests under the trace. It makes the slow dependency visible in the transaction view. In this case: A custom span around the model call records its duration and makes the dominant hop visible.

### Question 92 — D

Answer: Filter on metadata columns in the same query as the vector search. Filtering inside the vector query enforces scope without shrinking the result set after the fact. Combining a WHERE filter with the distance operator keeps retrieval inside the caller's scope and improves relevance. Index the filter columns too. Local study-map skill 2.9 (PostgreSQL RAG with Metadata Filters), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Cosmos DB and PostgreSQL vector documentation: https://learn.microsoft.com/en-us/azure/cosmos-db/

- **A:** Incorrect for this question. Post-filtering can return fewer results than requested and can leak existence or counts if the filtering is careless. Push authorization into the query. Why the correct answer wins: Filtering inside the vector query enforces scope without shrinking the result set after the fact.
- **B:** Incorrect for this question. An exact scan is accurate but scales linearly and burns compute. It is a baseline for measuring recall, not a production strategy. Why the correct answer wins: Filtering inside the vector query enforces scope without shrinking the result set after the fact.
- **C:** Incorrect for this question. HNSW gives fast approximate nearest-neighbour queries with a larger memory footprint and slower builds. Recall is tunable at query time. Why the correct answer wins: Filtering inside the vector query enforces scope without shrinking the result set after the fact.
- **D:** Correct. Combining a WHERE filter with the distance operator keeps retrieval inside the caller's scope and improves relevance. Index the filter columns too. In this case: Filtering inside the vector query enforces scope without shrinking the result set after the fact.

### Question 93 — D

Answer: Inspect the dead-letter queue and resubmit corrected messages. Dead-lettering keeps the failing message out of the active queue for later diagnosis. Dead-lettering preserves poison messages for diagnosis instead of losing them. Resubmission needs a fix and an idempotent handler. Local study-map skill 3.3 (Service Bus Dead-Lettering and Retries), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure messaging and Functions documentation: https://learn.microsoft.com/en-us/azure/service-bus-messaging/

- **A:** Incorrect for this question. A delivery cap stops infinite retries of a failing message and moves it to the dead-letter queue. The cap must exceed legitimate transient retries. Why the correct answer wins: Dead-lettering keeps the failing message out of the active queue for later diagnosis.
- **B:** Incorrect for this question. A duplicate-detection window drops repeated sends within the window, which helps with at-least-once producers. The window is time-bounded. Why the correct answer wins: Dead-lettering keeps the failing message out of the active queue for later diagnosis.
- **C:** Incorrect for this question. Receive-and-delete removes the message on delivery, so a crash loses work silently. It suits telemetry, not payments. Why the correct answer wins: Dead-lettering keeps the failing message out of the active queue for later diagnosis.
- **D:** Correct. Dead-lettering preserves poison messages for diagnosis instead of losing them. Resubmission needs a fix and an idempotent handler. In this case: Dead-lettering keeps the failing message out of the active queue for later diagnosis.

### Question 94 — B

Answer: Aggregate with summarize and bin to see the failure rate over time. Binning with summarize produces per-interval counts. Time-binned aggregation reveals the shape of an incident: a step change, a ramp, or a periodic spike. Averages alone hide short outages. Local study-map skill 4.4 (KQL Queries for Logs and Metrics), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Key Vault, App Configuration, and Monitor documentation: https://learn.microsoft.com/en-us/azure/azure-monitor/

- **A:** Incorrect for this question. Reducing columns and rows early lowers query cost and latency. Broad queries over long ranges are the usual cause of slow KQL. Why the correct answer wins: Binning with summarize produces per-interval counts.
- **B:** Correct. Time-binned aggregation reveals the shape of an incident: a step change, a ramp, or a periodic spike. Averages alone hide short outages. In this case: Binning with summarize produces per-interval counts.
- **C:** Incorrect for this question. Precomputed results avoid recomputing expensive aggregations on every dashboard refresh. The trade-off is storage and freshness lag. Why the correct answer wins: Binning with summarize produces per-interval counts.
- **D:** Incorrect for this question. Joining request and dependency telemetry shows which downstream call fails inside a slow request. Cross-workspace joins need the right scope. Why the correct answer wins: Binning with summarize produces per-interval counts.

### Question 95 — D

Answer: Test end-to-end connectivity from inside the container to each dependency. Testing from inside the pod proves DNS, egress, and network rules that a workstation test bypasses. Reaching a dependency from the pod or replica proves DNS, egress, and firewall paths together. Host-side tests can succeed while the container path fails. Local study-map skill 1.7 (Container Logs, Events, and Connectivity), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure container hosting documentation: https://learn.microsoft.com/en-us/azure/container-apps/

- **A:** Incorrect for this question. Readiness gates traffic until the app can serve it, and liveness restarts a wedged container. Wrong thresholds cause restart loops. Why the correct answer wins: Testing from inside the pod proves DNS, egress, and network rules that a workstation test bypasses.
- **B:** Incorrect for this question. A private endpoint keeps traffic on the virtual network and removes public exposure. DNS resolution must be wired to the private zone. Why the correct answer wins: Testing from inside the pod proves DNS, egress, and network rules that a workstation test bypasses.
- **C:** Incorrect for this question. A private endpoint needs matching name resolution or clients still resolve the public address. The zone must be linked to the workload network. Why the correct answer wins: Testing from inside the pod proves DNS, egress, and network rules that a workstation test bypasses.
- **D:** Correct. Reaching a dependency from the pod or replica proves DNS, egress, and firewall paths together. Host-side tests can succeed while the container path fails. In this case: Testing from inside the pod proves DNS, egress, and network rules that a workstation test bypasses.

### Question 96 — D

Answer: Filter the Event Grid subscription by subject or event type. A subject or property filter narrows delivery to matching events. Subject and event-type filters keep handlers focused and reduce cost. Filters are evaluated on event metadata, not payload body. Local study-map skill 3.4 (Event Grid Filters, Custom Events, and Retries), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure messaging and Functions documentation: https://learn.microsoft.com/en-us/azure/service-bus-messaging/

- **A:** Incorrect for this question. A duplicate-detection window drops repeated sends within the window, which helps with at-least-once producers. The window is time-bounded. Why the correct answer wins: A subject or property filter narrows delivery to matching events.
- **B:** Incorrect for this question. Subscription filters route only matching messages to a handler, reducing wasted processing. Filter evaluation happens broker-side on message properties. Why the correct answer wins: A subject or property filter narrows delivery to matching events.
- **C:** Incorrect for this question. Event Grid retries failed deliveries with backoff and can store undeliverable events. Handlers must still be idempotent. Why the correct answer wins: A subject or property filter narrows delivery to matching events.
- **D:** Correct. Subject and event-type filters keep handlers focused and reduce cost. Filters are evaluated on event metadata, not payload body. In this case: A subject or property filter narrows delivery to matching events.

### Question 97 — A

Answer: Query the workspace with KQL to find the failing operation. A KQL query over request telemetry returns that filtered, ordered list. KQL filters, projects, and aggregates log and metric tables in Log Analytics. Start narrow with a time range and a request ID. Local study-map skill 4.4 (KQL Queries for Logs and Metrics), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Key Vault, App Configuration, and Monitor documentation: https://learn.microsoft.com/en-us/azure/azure-monitor/

- **A:** Correct. KQL filters, projects, and aggregates log and metric tables in Log Analytics. Start narrow with a time range and a request ID. In this case: A KQL query over request telemetry returns that filtered, ordered list.
- **B:** Incorrect for this question. Reducing columns and rows early lowers query cost and latency. Broad queries over long ranges are the usual cause of slow KQL. Why the correct answer wins: A KQL query over request telemetry returns that filtered, ordered list.
- **C:** Incorrect for this question. Time-binned aggregation reveals the shape of an incident: a step change, a ramp, or a periodic spike. Averages alone hide short outages. Why the correct answer wins: A KQL query over request telemetry returns that filtered, ordered list.
- **D:** Incorrect for this question. Platform metrics are cheap and near-real-time, so they suit latency and failure-rate alerts. Log-based alerts add latency and query cost. Why the correct answer wins: A KQL query over request telemetry returns that filtered, ordered list.

### Question 98 — B

Answer: Scale on the Service Bus queue length with a KEDA Azure Service Bus scaler. A queue-length scaler adds consumers while images are waiting and scales to zero when the queue is empty. A queue-length scaler adds replicas while work is backed up and removes them when the queue drains. Message lock duration must exceed processing time. Local study-map skill 1.5 (Event-Driven Scaling with KEDA), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure container hosting documentation: https://learn.microsoft.com/en-us/azure/container-apps/

- **A:** Incorrect for this question. HPA adjusts replicas from resource metrics but needs metrics-server and enough node capacity. It cannot scale to zero. Why the correct answer wins: A queue-length scaler adds consumers while images are waiting and scales to zero when the queue is empty.
- **B:** Correct. A queue-length scaler adds replicas while work is backed up and removes them when the queue drains. Message lock duration must exceed processing time. In this case: A queue-length scaler adds consumers while images are waiting and scales to zero when the queue is empty.
- **C:** Incorrect for this question. CPU-based scaling reacts after work is already queued and cannot scale to zero on an empty queue. It suits steady request-driven services. Why the correct answer wins: A queue-length scaler adds consumers while images are waiting and scales to zero when the queue is empty.
- **D:** Incorrect for this question. Container Instances starts a single container group quickly for short tasks. It has no orchestrator-level scaling or revision model. Why the correct answer wins: A queue-length scaler adds consumers while images are waiting and scales to zero when the queue is empty.

### Question 99 — A

Answer: Create an HNSW index for low-latency approximate search. HNSW gives low-latency approximate search and lets recall be tuned at query time. HNSW gives fast approximate nearest-neighbour queries with a larger memory footprint and slower builds. Recall is tunable at query time. Local study-map skill 2.7 (pgvector Indexing and Query Latency), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Cosmos DB and PostgreSQL vector documentation: https://learn.microsoft.com/en-us/azure/cosmos-db/

- **A:** Correct. HNSW gives fast approximate nearest-neighbour queries with a larger memory footprint and slower builds. Recall is tunable at query time. In this case: HNSW gives low-latency approximate search and lets recall be tuned at query time.
- **B:** Incorrect for this question. An exact scan is accurate but scales linearly and burns compute. It is a baseline for measuring recall, not a production strategy. Why the correct answer wins: HNSW gives low-latency approximate search and lets recall be tuned at query time.
- **C:** Incorrect for this question. IVFFlat uses clustering lists and needs periodic rebuilds as data grows, but costs less memory than HNSW. Probes trade recall for speed. Why the correct answer wins: HNSW gives low-latency approximate search and lets recall be tuned at query time.
- **D:** Incorrect for this question. An external pooler multiplexes server connections for serverless or highly concurrent clients. Session-level features may be unavailable in transaction mode. Why the correct answer wins: HNSW gives low-latency approximate search and lets recall be tuned at query time.

### Question 100 — D

Answer: Use Service Bus sessions to keep related messages ordered. Sessions give exclusive, ordered processing per station identifier across competing workers. Sessions give ordered, exclusive processing per session ID across competing consumers. They require session-aware senders and receivers. Local study-map skill 3.1 (Service Bus Queues and Sessions), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure messaging and Functions documentation: https://learn.microsoft.com/en-us/azure/service-bus-messaging/

- **A:** Incorrect for this question. A delivery cap stops infinite retries of a failing message and moves it to the dead-letter queue. The cap must exceed legitimate transient retries. Why the correct answer wins: Sessions give exclusive, ordered processing per station identifier across competing workers.
- **B:** Incorrect for this question. Peek-lock keeps the message locked until the handler completes it, giving at-least-once processing with retry. Lock duration must exceed processing time. Why the correct answer wins: Sessions give exclusive, ordered processing per station identifier across competing workers.
- **C:** Incorrect for this question. A duplicate-detection window drops repeated sends within the window, which helps with at-least-once producers. The window is time-bounded. Why the correct answer wins: Sessions give exclusive, ordered processing per station identifier across competing workers.
- **D:** Correct. Sessions give ordered, exclusive processing per session ID across competing consumers. They require session-aware senders and receivers. In this case: Sessions give exclusive, ordered processing per station identifier across competing workers.
