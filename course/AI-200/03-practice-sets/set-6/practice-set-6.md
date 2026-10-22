# Microsoft AI-200 — Full-Length Mock Exam 6

Azure AI Cloud Developer Associate · 100 questions · expanded practice bank · passing target 700/1000

Blueprint-weighted mock exam of 100 items. Item mix: 76 single-choice, 16 multi-select (selection count stated), 8 ordering items rendered as answer choices, and 4 case studies of 3 questions. Hot-area, drag-and-drop UI, labs, and adaptive problem-solution sets cannot be reproduced in a CSV; see the README for the exact fidelity boundary.

Original educational content, not actual, recalled, or copied Microsoft exam items.

## Questions

### 1. The same recommendation container must deploy to three continents with local pulls and regional resilience. What should the registry provide?

Domain: Develop containerized solutions on Azure

- A. Deploy the mutable latest tag and let the platform resolve it
- B. Run image builds on demand or on a trigger with ACR Tasks
- C. Apply an ACR retention policy to prune old untagged manifests
- D. Replicate the registry to each deployment region

### 2. A rollback during a peak event needs the exact previous artifact, not whatever the tag points to now. What should the pipeline guarantee?

Domain: Develop containerized solutions on Azure

- A. Build and store versioned images in Azure Container Registry
- B. Run image builds on demand or on a trigger with ACR Tasks
- C. Deploy the mutable latest tag and let the platform resolve it
- D. Replicate the registry to each deployment region

### 3. Base images must be rebuilt automatically whenever an upstream patch is published. What should be used?

Domain: Develop containerized solutions on Azure

- A. Build and store versioned images in Azure Container Registry
- B. Stage the change in a deployment slot and swap after verification
- C. Apply an ACR retention policy to prune old untagged manifests
- D. Run image builds on demand or on a trigger with ACR Tasks

### 4. A regional storefront API needs platform patching and slots without cluster operations. What should host it?

Domain: Develop containerized solutions on Azure

- A. Deploy the service to Azure Container Apps
- B. Run the batch job in Azure Container Instances
- C. Deploy the image to Azure App Service as a web app
- D. Deploy the workload to Azure Kubernetes Service

### 5. A new storefront build must be warmed and verified before it receives any customer traffic. What should be used?

Domain: Develop containerized solutions on Azure

- A. Supply configuration through App Service application settings
- B. Reference a Key Vault secret from the app configuration instead of storing it
- C. Stage the change in a deployment slot and swap after verification
- D. Create a new Container Apps revision and shift traffic between revisions

### 6. Order enrichment must scale with backlog and drop to zero between campaigns. Which scaler fits?

Domain: Develop containerized solutions on Azure

- A. Scale the container app on an event source with a KEDA scaler
- B. Scale on the Service Bus queue length with a KEDA Azure Service Bus scaler
- C. Scale only on CPU utilization without an event scaler
- D. Rely on the horizontal pod autoscaler on CPU

### 7. Each cluster workload must obtain tokens for its own narrow permissions rather than share a credential. What should be configured?

Domain: Develop containerized solutions on Azure

- A. Authenticate with a managed identity instead of a stored key
- B. Federate a Kubernetes service account to a managed identity
- C. Store the secret in Azure Key Vault and read it at runtime
- D. Add readiness and liveness probes to the pod specification

### 8. Platform logs from several regional clusters must be queryable together during an incident. What should be configured?

Domain: Develop containerized solutions on Azure

- A. Query container logs and Kubernetes events in Log Analytics
- B. Send telemetry to Application Insights and inspect the transaction view
- C. Alert on platform metrics rather than only on log queries
- D. Enable diagnostic settings to route platform logs to the workspace

### 9. Artifacts must be traceable and pulls must be local in every deployment region. Which two capabilities provide that? Select two.

Domain: Develop containerized solutions on Azure

- A. Deploy the mutable latest tag and let the platform resolve it
- B. Run image builds on demand or on a trigger with ACR Tasks
- C. Apply an ACR retention policy to prune old untagged manifests
- D. Build and store versioned images in Azure Container Registry
- E. Replicate the registry to each deployment region

### 10. A storefront service must support progressive delivery and stay warm for first requests. Which two settings provide that? Select two.

Domain: Develop containerized solutions on Azure

- A. Set a minimum replica count above zero for the container app
- B. Stage the change in a deployment slot and swap after verification
- C. Create a new Container Apps revision and shift traffic between revisions
- D. Scale the container app on an event source with a KEDA scaler
- E. Rely on the horizontal pod autoscaler on CPU

### 11. Which sequence correctly releases a canary revision across the storefront?

Domain: Develop containerized solutions on Azure

- A. Shift all traffic to a new revision → deploy the revision → check metrics → build the image → promote
- B. Check metrics → deploy a new revision → build and push the image → shift a small traffic percentage → promote
- C. Deploy a new revision → shift all traffic → build and push the image → check metrics → roll back
- D. Build and push the image → deploy a new revision → shift a small traffic percentage → check metrics → promote or roll back

### 12. The catalogue client must use the supported SDK and avoid chatty per-property fetches. What should be used?

Domain: Develop AI solutions by using Azure data management services

- A. Increase provisioned throughput and watch the RU charge per query
- B. Include the partition key in the query predicate
- C. Batch related writes in a transactional batch within one partition key
- D. Query through the Cosmos DB SDK with parameterized queries

### 13. Write latency rises as more unused properties are indexed. What should be reviewed?

Domain: Develop AI solutions by using Azure data management services

- A. Increase provisioned throughput and watch the RU charge per query
- B. Restrict the indexing policy to the paths the queries use
- C. Set an item time-to-live on the container
- D. Index every property by using the default automatic policy

### 14. A single account must choose one consistency level that suits both a cart and a recommendation feed. What can be done per request?

Domain: Develop AI solutions by using Azure data management services

- A. Use session consistency for reads within the same client session
- B. Use eventual consistency to minimize read cost
- C. Choose the account consistency level that matches the read requirement
- D. Use strong consistency for every read in the account

### 15. A product-embedding container has grown into millions of rows and memory is the constraint. Which index type should be selected?

Domain: Develop AI solutions by using Azure data management services

- A. Use the DiskANN vector index for large collections
- B. Use the cosine distance function that matches how the embeddings were trained
- C. Store embeddings in a vector property and query with VectorDistance
- D. Scan every document and compute similarity in application code

### 16. Price changes must propagate to a search index without scanning the container. What should be used?

Domain: Develop AI solutions by using Azure data management services

- A. Enable duplicate detection on the queue
- B. Use a lease container to coordinate change feed readers
- C. Batch related writes in a transactional batch within one partition key
- D. Run a change feed processor to react to new and updated items

### 17. Which sequence correctly prepares the product container for similarity search?

Domain: Develop AI solutions by using Azure data management services

- A. Apply metadata filters → query with VectorDistance → create the container with a vector policy → upsert items with embeddings
- B. Query with VectorDistance → upsert items with embeddings → create the container with a vector policy → apply metadata filters
- C. Create the container with a vector policy → upsert items with embeddings → query with VectorDistance → apply metadata filters
- D. Upsert items with embeddings → create the container with a vector policy → apply metadata filters → query with VectorDistance

### 18. Support transcripts must be filtered by market and matched semantically in a single statement. What should be used?

Domain: Develop AI solutions by using Azure data management services

- A. Store embeddings in PostgreSQL by using the pgvector extension
- B. Scan every document and compute similarity in application code
- C. Store the documents in Azure Cosmos DB for NoSQL
- D. Cache responses in Azure Managed Redis

### 19. Semantic support search must return in milliseconds with recall tuned per query. Which index fits?

Domain: Develop AI solutions by using Azure data management services

- A. Create an HNSW index for low-latency approximate search
- B. Increase maintenance and query memory settings for index builds and sorts
- C. Query without a vector index and let PostgreSQL scan the table
- D. Create an IVFFlat index to save memory on a large table

### 20. Support search slows sharply when the vector index no longer fits in memory. What should be adjusted?

Domain: Develop AI solutions by using Azure data management services

- A. Increase maintenance and query memory settings for index builds and sorts
- B. Scale compute and memory to fit index size and query concurrency
- C. Reuse a bounded connection pool instead of opening a connection per request
- D. Increase storage throughput for index builds and bulk loads

### 21. Regional APIs each keep a small pool, but total connections still exceed the server limit. What should be added?

Domain: Develop AI solutions by using Azure data management services

- A. Use prepared statements and batch round trips
- B. Reuse a bounded connection pool instead of opening a connection per request
- C. Place a connection pooler in front of PostgreSQL for many short-lived clients
- D. Add a read replica and send all vector queries to it

### 22. Cached price tiles must never be older than five minutes. What should be set?

Domain: Develop AI solutions by using Azure data management services

- A. Invalidate or overwrite the cache entry when the source changes
- B. Flush the database after each deployment to guarantee fresh data
- C. Rely on the eviction policy and skip explicit TTLs
- D. Set a TTL on each cached entry

### 23. Cart reads must reflect the shopper's own update, while banner counts may lag. Which two levels suit those paths? Select two.

Domain: Develop AI solutions by using Azure data management services

- A. Choose the account consistency level that matches the read requirement
- B. Use eventual consistency to minimize read cost
- C. Use session consistency for reads within the same client session
- D. Increase provisioned throughput and watch the RU charge per query
- E. Use strong consistency for every read in the account

### 24. A memory-bound database must still serve vectors, and index builds spill to disk. Which two adjustments help? Select two.

Domain: Develop AI solutions by using Azure data management services

- A. Create an IVFFlat index to save memory on a large table
- B. Query without a vector index and let PostgreSQL scan the table
- C. Increase maintenance and query memory settings for index builds and sorts
- D. Increase storage throughput for index builds and bulk loads
- E. Create an HNSW index for low-latency approximate search

### 25. Each order confirmation must be processed by exactly one worker, with recovery after failure. What should be used?

Domain: Connect to and consume Azure services

- A. Queue the work on a Service Bus queue and process it with a worker
- B. Use Azure Queue Storage for the work items
- C. Publish to a Service Bus topic with multiple subscriptions
- D. Stream telemetry through Azure Event Hubs

### 26. Inventory updates for one SKU must be applied in order across competing consumers. What should be enabled?

Domain: Connect to and consume Azure services

- A. Receive with peek-lock and complete or abandon explicitly
- B. Use Service Bus sessions to keep related messages ordered
- C. Set a maximum delivery count and handle the dead-letter path
- D. Enable duplicate detection on the queue

### 27. A loyalty subscriber should receive only orders above a threshold. What should be configured?

Domain: Connect to and consume Azure services

- A. Add a SQL or correlation filter to a subscription
- B. Publish to a Service Bus topic with multiple subscriptions
- C. Enable duplicate detection on the queue
- D. Filter the Event Grid subscription by subject or event type

### 28. Replayed order messages must not create duplicate fulfilment records. What should the handler use?

Domain: Connect to and consume Azure services

- A. Set a maximum delivery count and handle the dead-letter path
- B. Make the handler idempotent by using a message or business key
- C. Enable duplicate detection on the queue
- D. Inspect the dead-letter queue and resubmit corrected messages

### 29. Only image-processing events from one store region should reach the handler. What should be configured?

Domain: Connect to and consume Azure services

- A. Rely on Event Grid retries with a dead-letter destination
- B. Define a custom event schema for the topic
- C. Filter the Event Grid subscription by subject or event type
- D. Add a SQL or correlation filter to a subscription

### 30. The pricing function must persist its result to the catalogue with minimal client code. What should be used?

Domain: Connect to and consume Azure services

- A. Orchestrate the multi-step workflow with Durable Functions
- B. Host the function app on a premium plan with pre-warmed instances
- C. Use input and output bindings instead of hand-written SDK calls
- D. Bind a queue or event trigger to the function

### 31. The pricing function must avoid cold starts and reach a private database. Which hosting plan fits?

Domain: Connect to and consume Azure services

- A. Orchestrate the multi-step workflow with Durable Functions
- B. Host the function app on the consumption plan
- C. Host the function app on a premium plan with pre-warmed instances
- D. Use a deployment slot on the function app for staging

### 32. Order events must reach fulfilment and analytics independently, and analytics only wants large orders. Which two features are required? Select two.

Domain: Connect to and consume Azure services

- A. Publish to a Service Bus topic with multiple subscriptions
- B. Use Azure Queue Storage for the work items
- C. Filter the Event Grid subscription by subject or event type
- D. Add a SQL or correlation filter to a subscription
- E. Queue the work on a Service Bus queue and process it with a worker

### 33. A long returns workflow must survive host restarts and must not run inside an HTTP request. Which two choices are required? Select two.

Domain: Connect to and consume Azure services

- A. Orchestrate the multi-step workflow with Durable Functions
- B. Host the function app on the consumption plan
- C. Move long-running work out of the HTTP request into a queue
- D. Expose the endpoint through an HTTP trigger
- E. Use input and output bindings instead of hand-written SDK calls

### 34. Which sequence correctly processes an order confirmation message?

Domain: Connect to and consume Azure services

- A. Process the work → receive with peek-lock → publish the message → complete the message → dead-letter after the delivery limit
- B. Publish the message → complete the message → receive with peek-lock → process the work → dead-letter after the delivery limit
- C. Publish the message → receive with peek-lock → process the work → complete the message → dead-letter after the delivery limit
- D. Receive with peek-lock → publish the message → complete the message → process the work → dead-letter after the delivery limit

### 35. Payment provider credentials must be auditable and revocable per region. Where should they live?

Domain: Secure, monitor, troubleshoot Azure solutions

- A. Store settings and feature flags in Azure App Configuration
- B. Store the secret in Azure Key Vault and read it at runtime
- C. Pin the application to a specific secret version
- D. Supply configuration through App Service application settings

### 36. A credential must be replaced every 30 days with no outage and no redeploy. What should be implemented?

Domain: Secure, monitor, troubleshoot Azure solutions

- A. Grant the app identity data-plane access to the vault
- B. Enable purge protection and soft delete on the vault
- C. Pin the application to a specific secret version
- D. Rotate the secret on a schedule and let apps resolve the current version

### 37. A changed shipping threshold is only applied after a redeploy. What should be enabled?

Domain: Secure, monitor, troubleshoot Azure solutions

- A. Enable configuration refresh so changes apply without a restart
- B. Deploy the function app through a CI pipeline with app settings applied
- C. Use App Configuration labels to separate environments
- D. Pin the application to a specific secret version

### 38. One configuration store must hold per-market values under one key schema. What should be used?

Domain: Secure, monitor, troubleshoot Azure solutions

- A. Pin the application to a specific secret version
- B. Store settings and feature flags in Azure App Configuration
- C. Reference the Key Vault secret from an App Configuration key value
- D. Use App Configuration labels to separate environments

### 39. Tracing every checkout would exceed the telemetry budget, but failed checkouts must remain traceable. What should be configured?

Domain: Secure, monitor, troubleshoot Azure solutions

- A. Propagate trace context across every service and queue hop
- B. Export telemetry through an OpenTelemetry collector
- C. Use head or tail sampling so trace volume stays within budget
- D. Instrument the service with the OpenTelemetry SDK

### 40. Executive dashboards recompute the same daily aggregation on every refresh. What should be considered?

Domain: Secure, monitor, troubleshoot Azure solutions

- A. Store repeated aggregations in a materialized view or update policy
- B. Project only the columns needed and filter by time first
- C. Create an alert rule on the failure rate or latency metric
- D. Aggregate with summarize and bin to see the failure rate over time

### 41. The deployment pipeline can alter data but the storefront only reads it. What should be done?

Domain: Secure, monitor, troubleshoot Azure solutions

- A. Enable diagnostic settings to route platform logs to the workspace
- B. Assign a least-privilege role to the application identity
- C. Authenticate with a managed identity instead of a stored key
- D. Reach the data service through a private endpoint

### 42. Telemetry must be vendor-neutral and must not require app changes to add a second backend. Which two practices are required? Select two.

Domain: Secure, monitor, troubleshoot Azure solutions

- A. Use head or tail sampling so trace volume stays within budget
- B. Instrument the service with the OpenTelemetry SDK
- C. Enable diagnostic settings to route platform logs to the workspace
- D. Export telemetry through an OpenTelemetry collector
- E. Query the workspace with KQL to find the failing operation

### 43. The database must be unreachable from the internet and the workload must authenticate without secrets. Which two actions should you take? Select two.

Domain: Secure, monitor, troubleshoot Azure solutions

- A. Federate a Kubernetes service account to a managed identity
- B. Store the secret in Azure Key Vault and read it at runtime
- C. Reach the data service through a private endpoint
- D. Assign a least-privilege role to the application identity
- E. Alert on platform metrics rather than only on log queries

### 44. Which sequence correctly rotates a regional payment credential?

Domain: Secure, monitor, troubleshoot Azure solutions

- A. Reference the secret from the app → rotate the secret → store the secret in Key Vault → grant the app identity access → the app reads the new version
- B. Grant the app identity access → store the secret in Key Vault → rotate the secret → reference the secret from the app → the app reads the new version
- C. Store the secret in Key Vault → grant the app identity access → reference the secret from the app → rotate the secret → the app reads the new version
- D. Rotate the secret → reference the secret from the app → store the secret in Key Vault → grant the app identity access → the app reads the new version

### 45. Continuous integration produces thousands of untagged manifests a month and registry storage cost keeps rising. What should be applied?

Domain: Develop containerized solutions on Azure

- A. Deploy the mutable latest tag and let the platform resolve it
- B. Apply an ACR retention policy to prune old untagged manifests
- C. Build and store versioned images in Azure Container Registry
- D. Replicate the registry to each deployment region

### 46. Images for three architectures must rebuild on every commit without a build farm to maintain. What should perform the build?

Domain: Develop containerized solutions on Azure

- A. Build and store versioned images in Azure Container Registry
- B. Deploy the workload to Azure Kubernetes Service
- C. Deploy the service to Azure Container Apps
- D. Run image builds on demand or on a trigger with ACR Tasks

### 47. Each region needs its own tax endpoint, and the value must change without rebuilding the storefront image. What should supply it?

Domain: Develop containerized solutions on Azure

- A. Mount non-secret configuration from a Kubernetes ConfigMap
- B. Store settings and feature flags in Azure App Configuration
- C. Pin the application to a specific secret version
- D. Supply configuration through App Service application settings

### 48. The storefront API must reach its database and cache over private addresses inside the workload network. What should be configured?

Domain: Develop containerized solutions on Azure

- A. Create a new Container Apps revision and shift traffic between revisions
- B. Configure Container Apps ingress for internal-only access
- C. Deploy into a Container Apps environment attached to the workload virtual network
- D. Scale the container app on an event source with a KEDA scaler

### 49. A nightly price export runs for twenty minutes and then exits, and the team wants it beside the storefront in Container Apps. What should be used?

Domain: Develop containerized solutions on Azure

- A. Deploy the service to Azure Container Apps
- B. Run the batch work as a Container Apps job
- C. Create a new Container Apps revision and shift traffic between revisions
- D. Run the batch job in Azure Container Instances

### 50. Order workers must follow the number of queued fulfilment messages and must shrink to zero when the queues drain. What should drive replicas?

Domain: Develop containerized solutions on Azure

- A. Run the batch job in Azure Container Instances
- B. Scale on the Service Bus queue length with a KEDA Azure Service Bus scaler
- C. Rely on the horizontal pod autoscaler on CPU
- D. Scale only on CPU utilization without an event scaler

### 51. Pods must pull from the private registry by using an Azure identity instead of an image-pull secret. What should be configured?

Domain: Develop containerized solutions on Azure

- A. Deploy the mutable latest tag and let the platform resolve it
- B. Replicate the registry to each deployment region
- C. Reference a Key Vault secret from the app configuration instead of storing it
- D. Federate a Kubernetes service account to a managed identity

### 52. Platform logs from the cluster and its dependencies must land in the central workspace beside application telemetry. What should be enabled?

Domain: Develop containerized solutions on Azure

- A. Enable diagnostic settings to route platform logs to the workspace
- B. Project only the columns needed and filter by time first
- C. Query container logs and Kubernetes events in Log Analytics
- D. Alert on platform metrics rather than only on log queries

### 53. A new storefront service must be wired to its database with identity-based configuration instead of pasted connection strings. What should be used?

Domain: Develop containerized solutions on Azure

- A. Supply configuration through App Service application settings
- B. Create an Azure service connector binding between the app and the dependency
- C. Mount non-secret configuration from a Kubernetes ConfigMap
- D. Reference a Key Vault secret from the app configuration instead of storing it

### 54. A storefront revision must scale from queue depth and must not thrash between one and ten replicas. Which two actions should you take? Select two.

Domain: Develop containerized solutions on Azure

- A. Run the batch job in Azure Container Instances
- B. Tune the scale rule cool-down period and maximum replicas
- C. Scale only on CPU utilization without an event scaler
- D. Rely on the horizontal pod autoscaler on CPU
- E. Scale the container app on an event source with a KEDA scaler

### 55. Which sequence correctly releases a storefront revision to a small share of global traffic?

Domain: Develop containerized solutions on Azure

- A. Build and push the image → deploy a new revision → shift a small traffic percentage → check metrics → promote or roll back
- B. Check metrics → deploy a new revision → build and push the image → shift a small traffic percentage → promote
- C. Deploy a new revision → shift all traffic → build and push the image → check metrics → roll back
- D. Shift all traffic to a new revision → deploy the revision → check metrics → build the image → promote

### 56. Product documents must be stored as JSON with point reads by product identifier and per-market isolation. Which store fits?

Domain: Develop AI solutions by using Azure data management services

- A. Store the documents in Azure Cosmos DB for NoSQL
- B. Store embeddings in PostgreSQL by using the pgvector extension
- C. Use Azure Queue Storage for the work items
- D. Include the partition key in the query predicate

### 57. Order events arrive from every market and writes must not concentrate on a single logical partition. What should the container use?

Domain: Develop AI solutions by using Azure data management services

- A. Index every property by using the default automatic policy
- B. Include the partition key in the query predicate
- C. Increase provisioned throughput and watch the RU charge per query
- D. Choose a high-cardinality partition key that spreads writes

### 58. Storefront writes cost far more than the query volume justifies, and only four of forty properties are ever filtered. What should be changed?

Domain: Develop AI solutions by using Azure data management services

- A. Index every property by using the default automatic policy
- B. Restrict the indexing policy to the paths the queries use
- C. Enable autoscale throughput with a maximum RU limit
- D. Add a composite index for the filtered and ordered properties

### 59. A global catalog read tolerates seconds of lag, but the team wants the guarantee stated rather than inherited. What should be chosen deliberately?

Domain: Develop AI solutions by using Azure data management services

- A. Choose the account consistency level that matches the read requirement
- B. Use eventual consistency to minimize read cost
- C. Use strong consistency for every read in the account
- D. Use session consistency for reads within the same client session

### 60. Visual search starts returning errors after the embedding model changed from 1536 to 3072 dimensions. What must be updated?

Domain: Develop AI solutions by using Azure data management services

- A. Create an HNSW index for low-latency approximate search
- B. Use the cosine distance function that matches how the embeddings were trained
- C. Store embeddings in a vector property and query with VectorDistance
- D. Declare the embedding dimensions and vector index type on the container policy

### 61. A new vector container returns weak matches even though the embeddings are correct. What should be verified?

Domain: Develop AI solutions by using Azure data management services

- A. Match the vector index type and dimensions to the embedding model
- B. Store embeddings in a vector property and query with VectorDistance
- C. Use the cosine distance function that matches how the embeddings were trained
- D. Use the DiskANN vector index for large collections

### 62. Every product update must propagate to the search index without polling the container. What should be implemented?

Domain: Develop AI solutions by using Azure data management services

- A. Set an item time-to-live on the container
- B. Enable duplicate detection on the queue
- C. Use a lease container to coordinate change feed readers
- D. Run a change feed processor to react to new and updated items

### 63. Review chunks and embeddings must be filtered by market and language beside a vector predicate in one statement. How should the table be modeled?

Domain: Develop AI solutions by using Azure data management services

- A. Scale compute and memory to fit index size and query concurrency
- B. Increase storage throughput for index builds and bulk loads
- C. Model typed columns for filters and one vector column for the embedding
- D. Add a read replica and send all vector queries to it

### 64. Serverless storefront functions open hundreds of short-lived connections per region and exhaust PostgreSQL sessions. What should be added?

Domain: Develop AI solutions by using Azure data management services

- A. Increase storage throughput for index builds and bulk loads
- B. Place a connection pooler in front of PostgreSQL for many short-lived clients
- C. Use prepared statements and batch round trips
- D. Reuse a bounded connection pool instead of opening a connection per request

### 65. Every storefront request recomputes the same regional promotion block. What should be added?

Domain: Develop AI solutions by using Azure data management services

- A. Set a TTL on each cached entry
- B. Add a read replica and send all vector queries to it
- C. Cache responses in Azure Managed Redis
- D. Use Azure Queue Storage for the work items

### 66. Product updates must reach the indexer in order and several processor instances must share the work. Which two components are required? Select two.

Domain: Develop AI solutions by using Azure data management services

- A. Enable duplicate detection on the queue
- B. Set an item time-to-live on the container
- C. Use a lease container to coordinate change feed readers
- D. Run a change feed processor to react to new and updated items
- E. Index every property by using the default automatic policy

### 67. Embeddings must live beside product metadata and similarity must use the metric the model was trained with. Which two choices are required? Select two.

Domain: Develop AI solutions by using Azure data management services

- A. Store embeddings in a vector property and query with VectorDistance
- B. Store embeddings in PostgreSQL by using the pgvector extension
- C. Scan every document and compute similarity in application code
- D. Use the cosine distance function that matches how the embeddings were trained
- E. Use the DiskANN vector index for large collections

### 68. Which sequence correctly creates a product container that supports filtered vector search?

Domain: Develop AI solutions by using Azure data management services

- A. Upsert items with embeddings → create the container with a vector policy → apply metadata filters → query with VectorDistance
- B. Apply metadata filters → query with VectorDistance → create the container with a vector policy → upsert items with embeddings
- C. Query with VectorDistance → upsert items with embeddings → create the container with a vector policy → apply metadata filters
- D. Create the container with a vector policy → upsert items with embeddings → query with VectorDistance → apply metadata filters

### 69. Fulfilment messages for one order must be processed in order by a single worker across regions. What should be enabled?

Domain: Connect to and consume Azure services

- A. Use Service Bus sessions to keep related messages ordered
- B. Receive with peek-lock and complete or abandon explicitly
- C. Set a maximum delivery count and handle the dead-letter path
- D. Enable duplicate detection on the queue

### 70. Malformed supplier feeds must be preserved for investigation instead of being retried until they expire. Where should they end up?

Domain: Connect to and consume Azure services

- A. Receive in receive-and-delete mode for at-most-once delivery
- B. Inspect the dead-letter queue and resubmit corrected messages
- C. Enable duplicate detection on the queue
- D. Use prepared statements and batch round trips

### 71. New product images must trigger resizing from the storage account without a custom publisher. What should be used?

Domain: Connect to and consume Azure services

- A. Rely on Event Grid retries with a dead-letter destination
- B. Subscribe to a system topic for resource events
- C. Define a custom event schema for the topic
- D. Stream telemetry through Azure Event Hubs

### 72. Event delivery must authenticate with an Azure identity instead of a webhook key. What should be configured?

Domain: Connect to and consume Azure services

- A. Deliver events by using a managed identity instead of a key
- B. Define a custom event schema for the topic
- C. Rely on Event Grid retries with a dead-letter destination
- D. Stream telemetry through Azure Event Hubs

### 73. An inventory handler must write its result to Cosmos DB without building a client in code. What should be used?

Domain: Connect to and consume Azure services

- A. Use input and output bindings instead of hand-written SDK calls
- B. Orchestrate the multi-step workflow with Durable Functions
- C. Expose the endpoint through an HTTP trigger
- D. Bind a queue or event trigger to the function

### 74. Order enrichment must reach private endpoints and must avoid cold starts during flash sales. Which hosting plan fits?

Domain: Connect to and consume Azure services

- A. Host the function app on a premium plan with pre-warmed instances
- B. Orchestrate the multi-step workflow with Durable Functions
- C. Expose the endpoint through an HTTP trigger
- D. Host the function app on the consumption plan

### 75. The tax service returns 503 in short bursts, and immediate retries deepen the outage. What should be configured?

Domain: Connect to and consume Azure services

- A. Configure the host retry policy with exponential backoff
- B. Host the function app on a premium plan with pre-warmed instances
- C. Tune the function app concurrency and batch size
- D. Deploy the function app through a CI pipeline with app settings applied

### 76. Every product event must reach both pricing and loyalty, and loyalty must receive only members-only changes. Which two features are required? Select two.

Domain: Connect to and consume Azure services

- A. Queue the work on a Service Bus queue and process it with a worker
- B. Publish to a Service Bus topic with multiple subscriptions
- C. Filter the Event Grid subscription by subject or event type
- D. Use Azure Queue Storage for the work items
- E. Add a SQL or correlation filter to a subscription

### 77. A poison supplier message must stop looping and must remain available for replay. Which two capabilities are required? Select two.

Domain: Connect to and consume Azure services

- A. Receive with peek-lock and complete or abandon explicitly
- B. Inspect the dead-letter queue and resubmit corrected messages
- C. Set a maximum delivery count and handle the dead-letter path
- D. Receive in receive-and-delete mode for at-most-once delivery
- E. Enable duplicate detection on the queue

### 78. Which sequence correctly delivers a custom product event to a regional subscriber?

Domain: Connect to and consume Azure services

- A. Evaluate the subscription filter → publish a custom event → dead-letter undeliverable events → deliver to the handler → retry on failure
- B. Publish a custom event → deliver to the handler → evaluate the subscription filter → dead-letter undeliverable events → retry on failure
- C. Publish a custom event → evaluate the subscription filter → deliver to the handler → retry on failure → dead-letter undeliverable events
- D. Deliver to the handler → publish a custom event → evaluate the subscription filter → retry on failure → dead-letter undeliverable events

### 79. The supplier API key must be stored with version history and access audit in a managed service. Where should it live?

Domain: Secure, monitor, troubleshoot Azure solutions

- A. Assign a least-privilege role to the application identity
- B. Reference a Key Vault secret from the app configuration instead of storing it
- C. Store settings and feature flags in Azure App Configuration
- D. Store the secret in Azure Key Vault and read it at runtime

### 80. A deleted vault must remain recoverable through the regulated retention window. What should be enabled?

Domain: Secure, monitor, troubleshoot Azure solutions

- A. Rotate the secret on a schedule and let apps resolve the current version
- B. Store the secret in Azure Key Vault and read it at runtime
- C. Enable purge protection and soft delete on the vault
- D. Grant the app identity data-plane access to the vault

### 81. Market-specific settings and shared flags need one place to change them across four regions. What should be introduced?

Domain: Secure, monitor, troubleshoot Azure solutions

- A. Enable configuration refresh so changes apply without a restart
- B. Reference the Key Vault secret from an App Configuration key value
- C. Store settings and feature flags in Azure App Configuration
- D. Use App Configuration labels to separate environments

### 82. Logs and traces must be joinable so one order can be followed from any query. What must be emitted and joined on?

Domain: Secure, monitor, troubleshoot Azure solutions

- A. Propagate trace context across every service and queue hop
- B. Instrument the service with the OpenTelemetry SDK
- C. Query the workspace with KQL to find the failing operation
- D. Correlate logs with the operation or trace identifier

### 83. Peak sale traffic exceeds the trace budget, yet failed checkouts must always be captured. What should be configured?

Domain: Secure, monitor, troubleshoot Azure solutions

- A. Create a custom span around each downstream call
- B. Use head or tail sampling so trace volume stays within budget
- C. Export telemetry through an OpenTelemetry collector
- D. Propagate trace context across every service and queue hop

### 84. The storefront identity holds contributor on the whole subscription, which the security review rejected. What should change?

Domain: Secure, monitor, troubleshoot Azure solutions

- A. Assign a least-privilege role to the application identity
- B. Enable purge protection and soft delete on the vault
- C. Federate a Kubernetes service account to a managed identity
- D. Reach the data service through a private endpoint

### 85. An app must read the current supplier key and that key must change on a schedule. Which two actions should you take? Select two.

Domain: Secure, monitor, troubleshoot Azure solutions

- A. Pin the application to a specific secret version
- B. Rotate the secret on a schedule and let apps resolve the current version
- C. Grant the app identity data-plane access to the vault
- D. Reference a Key Vault secret from the app configuration instead of storing it
- E. Store settings and feature flags in Azure App Configuration

### 86. A new checkout ranking must ship before it is enabled and must apply without a restart. Which two features are required? Select two.

Domain: Secure, monitor, troubleshoot Azure solutions

- A. Pin the application to a specific secret version
- B. Use App Configuration labels to separate environments
- C. Ship the code dark behind a feature flag
- D. Enable configuration refresh so changes apply without a restart
- E. Reference the Key Vault secret from an App Configuration key value

### 87. Operations needs the failure rate per five-minute bucket and must be paged when it spikes. Which two components are required? Select two.

Domain: Secure, monitor, troubleshoot Azure solutions

- A. Aggregate with summarize and bin to see the failure rate over time
- B. Set the workspace retention and table plan to control log cost
- C. Store repeated aggregations in a materialized view or update policy
- D. Project only the columns needed and filter by time first
- E. Create an alert rule on the failure rate or latency metric

### 88. Which sequence correctly makes a slow checkout dependency visible across every hop?

Domain: Secure, monitor, troubleshoot Azure solutions

- A. Instrument the service with the OpenTelemetry SDK → propagate the trace context across queue hops → export spans to the collector → query the transaction view for the slow dependency → alert on the failure rate
- B. Query the transaction view for the slow dependency → export spans to the collector → instrument the service with the OpenTelemetry SDK → alert on the failure rate → propagate the trace context across queue hops
- C. Alert on the failure rate → instrument the service with the OpenTelemetry SDK → propagate the trace context across queue hops → export spans to the collector → query the transaction view for the slow dependency
- D. Export spans to the collector → instrument the service with the OpenTelemetry SDK → query the transaction view for the slow dependency → propagate the trace context across queue hops → alert on the failure rate

---

## Case study — GlobalMart

The next three questions refer to this scenario. Read the full scenario before answering; case-study items are scored individually.

### 89. Storefront clusters in four regions pull the same large image on every scale-out, and pulls dominate cold start outside the primary region. What should be configured?

Domain: Develop containerized solutions on Azure

- A. Build and store versioned images in Azure Container Registry
- B. Replicate the registry to each deployment region
- C. Stage the change in a deployment slot and swap after verification
- D. Run image builds on demand or on a trigger with ACR Tasks

### 90. Retrieval must return only chunks for the caller's market and must still fill the result count. What should the query do?

Domain: Develop AI solutions by using Azure data management services

- A. Create an IVFFlat index to save memory on a large table
- B. Retrieve nearest neighbours first and discard unauthorized rows in the application
- C. Create an HNSW index for low-latency approximate search
- D. Filter on metadata columns in the same query as the vector search

### 91. Pricing, inventory, and loyalty must each receive every product event with their own cursor. What should be used?

Domain: Connect to and consume Azure services

- A. Define a custom event schema for the topic
- B. Queue the work on a Service Bus queue and process it with a worker
- C. Use Azure Queue Storage for the work items
- D. Publish to a Service Bus topic with multiple subscriptions

---

## Case study — GroupRetail

The next three questions refer to this scenario. Read the full scenario before answering; case-study items are scored individually.

### 92. Each market may see only its own policy text, and the result list must stay complete. What should the query do?

Domain: Develop AI solutions by using Azure data management services

- A. Filter on metadata columns in the same query as the vector search
- B. Retrieve nearest neighbours first and discard unauthorized rows in the application
- C. Create an HNSW index for low-latency approximate search
- D. Query without a vector index and let PostgreSQL scan the table

### 93. Visual product similarity must return from memory without a database round trip. What should be used?

Domain: Develop AI solutions by using Azure data management services

- A. Cache responses in Azure Managed Redis
- B. Use a distributed lock in Redis to make processing idempotent
- C. Create a vector index in Managed Redis for similarity search
- D. Store user session state in Managed Redis with an expiry

### 94. A price-rule change must notify subscribers even though it is not an Azure resource event. What should be published?

Domain: Connect to and consume Azure services

- A. Filter the Event Grid subscription by subject or event type
- B. Define a custom event schema for the topic
- C. Rely on Event Grid retries with a dead-letter destination
- D. Subscribe to a system topic for resource events

---

## Case study — NovaRetail

The next three questions refer to this scenario. Read the full scenario before answering; case-study items are scored individually.

### 95. Similar-product search across two million chunks must answer in tens of milliseconds. Which index fits?

Domain: Develop AI solutions by using Azure data management services

- A. Place a connection pooler in front of PostgreSQL for many short-lived clients
- B. Create an HNSW index for low-latency approximate search
- C. Query without a vector index and let PostgreSQL scan the table
- D. Create an IVFFlat index to save memory on a large table

### 96. A replayed payment event must never create a second fulfilment record. What should the handler use?

Domain: Connect to and consume Azure services

- A. Enable duplicate detection on the queue
- B. Receive with peek-lock and complete or abandon explicitly
- C. Make the handler idempotent by using a message or business key
- D. Receive in receive-and-delete mode for at-most-once delivery

### 97. A ninety-day revenue-by-market aggregation times out whenever the dashboard refreshes. What should be used?

Domain: Secure, monitor, troubleshoot Azure solutions

- A. Store repeated aggregations in a materialized view or update policy
- B. Project only the columns needed and filter by time first
- C. Join the requests and dependencies tables on the operation ID
- D. Aggregate with summarize and bin to see the failure rate over time

---

## Case study — StoreOps

The next three questions refer to this scenario. Read the full scenario before answering; case-study items are scored individually.

### 98. Pods in one region fail to reach the cache while pods in another region succeed. What should be checked first on the failing side?

Domain: Develop containerized solutions on Azure

- A. Link the private DNS zone so the private endpoint name resolves
- B. Query container logs and Kubernetes events in Log Analytics
- C. Add readiness and liveness probes to the pod specification
- D. Test end-to-end connectivity from inside the container to each dependency

### 99. A message with a bad address repeatedly fails fulfilment and must be preserved for investigation. What should happen?

Domain: Connect to and consume Azure services

- A. Receive in receive-and-delete mode for at-most-once delivery
- B. Inspect the dead-letter queue and resubmit corrected messages
- C. Use Service Bus sessions to keep related messages ordered
- D. Set a maximum delivery count and handle the dead-letter path

### 100. An incident query over seven days is slow and expensive. What should be changed first?

Domain: Secure, monitor, troubleshoot Azure solutions

- A. Alert on platform metrics rather than only on log queries
- B. Join the requests and dependencies tables on the operation ID
- C. Project only the columns needed and filter by time first
- D. Aggregate with summarize and bin to see the failure rate over time

---

## Answer key and explanations

### Question 1 — D

Answer: Replicate the registry to each deployment region. Geo-replication keeps a copy per region for latency and outage tolerance. Geo-replication reduces cross-region pull latency and gives a local copy during a regional failure. It adds cost and replication management. Local study-map skill 1.1 (Container Image Lifecycle in Azure Container Registry), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure container hosting documentation: https://learn.microsoft.com/en-us/azure/container-apps/

- **A:** Incorrect for this question. A floating tag removes the link between a deployed revision and a specific build, so rollback and audit become guesswork. Why the correct answer wins: Geo-replication keeps a copy per region for latency and outage tolerance.
- **B:** Incorrect for this question. ACR Tasks builds images in Azure on a commit or schedule without a local Docker host. It removes build-host drift but not image review. Why the correct answer wins: Geo-replication keeps a copy per region for latency and outage tolerance.
- **C:** Incorrect for this question. A retention policy controls storage growth and registry clutter. It does not change which image tag a deployment references. Why the correct answer wins: Geo-replication keeps a copy per region for latency and outage tolerance.
- **D:** Correct. Geo-replication reduces cross-region pull latency and gives a local copy during a regional failure. It adds cost and replication management. In this case: Geo-replication keeps a copy per region for latency and outage tolerance.

### Question 2 — C

Answer: Deploy the mutable latest tag and let the platform resolve it. Immutable versioned tags keep the previous artifact identifiable and deployable. A floating tag removes the link between a deployed revision and a specific build, so rollback and audit become guesswork. Local study-map skill 1.1 (Container Image Lifecycle in Azure Container Registry), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure container hosting documentation: https://learn.microsoft.com/en-us/azure/container-apps/

- **A:** Incorrect for this question. ACR keeps tagged, versioned images next to the deployment target and supports identity-based pulls. Tagging strategy and retention still need a decision. Why the correct answer wins: Immutable versioned tags keep the previous artifact identifiable and deployable.
- **B:** Incorrect for this question. ACR Tasks builds images in Azure on a commit or schedule without a local Docker host. It removes build-host drift but not image review. Why the correct answer wins: Immutable versioned tags keep the previous artifact identifiable and deployable.
- **C:** Correct. A floating tag removes the link between a deployed revision and a specific build, so rollback and audit become guesswork. In this case: Immutable versioned tags keep the previous artifact identifiable and deployable.
- **D:** Incorrect for this question. Geo-replication reduces cross-region pull latency and gives a local copy during a regional failure. It adds cost and replication management. Why the correct answer wins: Immutable versioned tags keep the previous artifact identifiable and deployable.

### Question 3 — D

Answer: Run image builds on demand or on a trigger with ACR Tasks. An ACR Task on a base image update trigger rebuilds dependent images. ACR Tasks builds images in Azure on a commit or schedule without a local Docker host. It removes build-host drift but not image review. Local study-map skill 1.2 (Automated Image Builds with ACR Tasks), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure container hosting documentation: https://learn.microsoft.com/en-us/azure/container-apps/

- **A:** Incorrect for this question. ACR keeps tagged, versioned images next to the deployment target and supports identity-based pulls. Tagging strategy and retention still need a decision. Why the correct answer wins: An ACR Task on a base image update trigger rebuilds dependent images.
- **B:** Incorrect for this question. A slot swap warms the new version before it takes production traffic and makes rollback a second swap. Slot-local settings must be marked sticky. Why the correct answer wins: An ACR Task on a base image update trigger rebuilds dependent images.
- **C:** Incorrect for this question. A retention policy controls storage growth and registry clutter. It does not change which image tag a deployment references. Why the correct answer wins: An ACR Task on a base image update trigger rebuilds dependent images.
- **D:** Correct. ACR Tasks builds images in Azure on a commit or schedule without a local Docker host. It removes build-host drift but not image review. In this case: An ACR Task on a base image update trigger rebuilds dependent images.

### Question 4 — C

Answer: Deploy the image to Azure App Service as a web app. App Service runs the container with managed maintenance and slots. App Service runs a container with managed patching, deployment slots, and built-in authentication options. It is not a Kubernetes control plane. Local study-map skill 1.3 (Container Deployment to Azure App Service), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure container hosting documentation: https://learn.microsoft.com/en-us/azure/container-apps/

- **A:** Incorrect for this question. Container Apps provides a managed environment, revisions, and KEDA-based scaling without cluster administration. Platform limits differ from AKS. Why the correct answer wins: App Service runs the container with managed maintenance and slots.
- **B:** Incorrect for this question. Container Instances starts a single container group quickly for short tasks. It has no orchestrator-level scaling or revision model. Why the correct answer wins: App Service runs the container with managed maintenance and slots.
- **C:** Correct. App Service runs a container with managed patching, deployment slots, and built-in authentication options. It is not a Kubernetes control plane. In this case: App Service runs the container with managed maintenance and slots.
- **D:** Incorrect for this question. AKS gives full Kubernetes control, including custom controllers and networking. You own node pools, upgrades, and manifest hygiene. Why the correct answer wins: App Service runs the container with managed maintenance and slots.

### Question 5 — C

Answer: Stage the change in a deployment slot and swap after verification. A slot swap warms the new version and allows a fast rollback. A slot swap warms the new version before it takes production traffic and makes rollback a second swap. Slot-local settings must be marked sticky. Local study-map skill 1.3 (Container Deployment to Azure App Service), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure container hosting documentation: https://learn.microsoft.com/en-us/azure/container-apps/

- **A:** Incorrect for this question. Application settings become environment variables for the container and can be swapped per slot. Sensitive values should still reference a vault. Why the correct answer wins: A slot swap warms the new version and allows a fast rollback.
- **B:** Incorrect for this question. A Key Vault reference resolves at runtime so the secret is never written into application settings. The app identity still needs permission to read it. Why the correct answer wins: A slot swap warms the new version and allows a fast rollback.
- **C:** Correct. A slot swap warms the new version before it takes production traffic and makes rollback a second swap. Slot-local settings must be marked sticky. In this case: A slot swap warms the new version and allows a fast rollback.
- **D:** Incorrect for this question. Revision-based traffic splitting enables canary and blue-green releases. Revision mode and scale rules must be set deliberately. Why the correct answer wins: A slot swap warms the new version and allows a fast rollback.

### Question 6 — B

Answer: Scale on the Service Bus queue length with a KEDA Azure Service Bus scaler. A queue-length KEDA scaler follows backlog and can scale to zero. A queue-length scaler adds replicas while work is backed up and removes them when the queue drains. Message lock duration must exceed processing time. Local study-map skill 1.5 (Event-Driven Scaling with KEDA), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure container hosting documentation: https://learn.microsoft.com/en-us/azure/container-apps/

- **A:** Incorrect for this question. KEDA scalers drive replica count from queue length, lag, or other event metrics, including scale to zero. Cool-down and max replicas bound the behavior. Why the correct answer wins: A queue-length KEDA scaler follows backlog and can scale to zero.
- **B:** Correct. A queue-length scaler adds replicas while work is backed up and removes them when the queue drains. Message lock duration must exceed processing time. In this case: A queue-length KEDA scaler follows backlog and can scale to zero.
- **C:** Incorrect for this question. CPU-based scaling reacts after work is already queued and cannot scale to zero on an empty queue. It suits steady request-driven services. Why the correct answer wins: A queue-length KEDA scaler follows backlog and can scale to zero.
- **D:** Incorrect for this question. HPA adjusts replicas from resource metrics but needs metrics-server and enough node capacity. It cannot scale to zero. Why the correct answer wins: A queue-length KEDA scaler follows backlog and can scale to zero.

### Question 7 — B

Answer: Federate a Kubernetes service account to a managed identity. Workload identity federation gives each workload its own federated identity. Workload identity lets pods obtain tokens without stored secrets. Each workload should get its own identity and narrow role. Local study-map skill 1.6 (AKS Deployment with Manifests), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure container hosting documentation: https://learn.microsoft.com/en-us/azure/container-apps/

- **A:** Incorrect for this question. A managed identity issues tokens from the platform, removing secret distribution from the app. Role assignment still scopes what it can reach. Why the correct answer wins: Workload identity federation gives each workload its own federated identity.
- **B:** Correct. Workload identity lets pods obtain tokens without stored secrets. Each workload should get its own identity and narrow role. In this case: Workload identity federation gives each workload its own federated identity.
- **C:** Incorrect for this question. A vault centralizes secret storage with access control and audit. Retrieval should use an identity, not a copied credential. Why the correct answer wins: Workload identity federation gives each workload its own federated identity.
- **D:** Incorrect for this question. Readiness gates traffic until the app can serve it, and liveness restarts a wedged container. Wrong thresholds cause restart loops. Why the correct answer wins: Workload identity federation gives each workload its own federated identity.

### Question 8 — D

Answer: Enable diagnostic settings to route platform logs to the workspace. Diagnostic settings route platform logs into a shared workspace for querying. Platform logs and metrics must be routed before they can be queried or alerted on. Retention and cost follow the workspace settings. Local study-map skill 1.7 (Container Logs, Events, and Connectivity), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure container hosting documentation: https://learn.microsoft.com/en-us/azure/container-apps/

- **A:** Incorrect for this question. Container Apps and AKS surface stdout logs and platform events into a workspace for KQL analysis. Verbosity and retention cost money. Why the correct answer wins: Diagnostic settings route platform logs into a shared workspace for querying.
- **B:** Incorrect for this question. Application Insights correlates requests, dependencies, and exceptions into end-to-end transactions. Sampling can hide rare failures. Why the correct answer wins: Diagnostic settings route platform logs into a shared workspace for querying.
- **C:** Incorrect for this question. Platform metrics are cheap and near-real-time, so they suit latency and failure-rate alerts. Log-based alerts add latency and query cost. Why the correct answer wins: Diagnostic settings route platform logs into a shared workspace for querying.
- **D:** Correct. Platform logs and metrics must be routed before they can be queried or alerted on. Retention and cost follow the workspace settings. In this case: Diagnostic settings route platform logs into a shared workspace for querying.

### Question 9 — D, E

Answers: Build and store versioned images in Azure Container Registry; Replicate the registry to each deployment region. Versioned tags identify each artifact, and geo-replication keeps local copies. ACR keeps tagged, versioned images next to the deployment target and supports identity-based pulls. Tagging strategy and retention still need a decision. Geo-replication reduces cross-region pull latency and gives a local copy during a regional failure. It adds cost and replication management. Local study-map skill 1.1 (Container Image Lifecycle in Azure Container Registry), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure container hosting documentation: https://learn.microsoft.com/en-us/azure/container-apps/

- **A:** Incorrect for this question. A floating tag removes the link between a deployed revision and a specific build, so rollback and audit become guesswork. Why the correct answer wins: Versioned tags identify each artifact, and geo-replication keeps local copies.
- **B:** Incorrect for this question. ACR Tasks builds images in Azure on a commit or schedule without a local Docker host. It removes build-host drift but not image review. Why the correct answer wins: Versioned tags identify each artifact, and geo-replication keeps local copies.
- **C:** Incorrect for this question. A retention policy controls storage growth and registry clutter. It does not change which image tag a deployment references. Why the correct answer wins: Versioned tags identify each artifact, and geo-replication keeps local copies.
- **D:** Correct. ACR keeps tagged, versioned images next to the deployment target and supports identity-based pulls. Tagging strategy and retention still need a decision. In this case: Versioned tags identify each artifact, and geo-replication keeps local copies.
- **E:** Correct. Geo-replication reduces cross-region pull latency and gives a local copy during a regional failure. It adds cost and replication management. In this case: Versioned tags identify each artifact, and geo-replication keeps local copies.

### Question 10 — A, C

Answers: Create a new Container Apps revision and shift traffic between revisions; Set a minimum replica count above zero for the container app. Revisions enable traffic shifting, and a minimum replica count keeps instances warm. Revision-based traffic splitting enables canary and blue-green releases. Revision mode and scale rules must be set deliberately. A warm minimum replica removes scale-to-zero cold starts for latency-critical endpoints. It keeps paying for idle capacity. Local study-map skill 1.4 (Container Apps Deployment and Revisions), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure container hosting documentation: https://learn.microsoft.com/en-us/azure/container-apps/

- **A:** Correct. A warm minimum replica removes scale-to-zero cold starts for latency-critical endpoints. It keeps paying for idle capacity. In this case: Revisions enable traffic shifting, and a minimum replica count keeps instances warm.
- **B:** Incorrect for this question. A slot swap warms the new version before it takes production traffic and makes rollback a second swap. Slot-local settings must be marked sticky. Why the correct answer wins: Revisions enable traffic shifting, and a minimum replica count keeps instances warm.
- **C:** Correct. Revision-based traffic splitting enables canary and blue-green releases. Revision mode and scale rules must be set deliberately. In this case: Revisions enable traffic shifting, and a minimum replica count keeps instances warm.
- **D:** Incorrect for this question. KEDA scalers drive replica count from queue length, lag, or other event metrics, including scale to zero. Cool-down and max replicas bound the behavior. Why the correct answer wins: Revisions enable traffic shifting, and a minimum replica count keeps instances warm.
- **E:** Incorrect for this question. HPA adjusts replicas from resource metrics but needs metrics-server and enough node capacity. It cannot scale to zero. Why the correct answer wins: Revisions enable traffic shifting, and a minimum replica count keeps instances warm.

### Question 11 — D

Answer: Build and push the image → deploy a new revision → shift a small traffic percentage → check metrics → promote or roll back. The artifact is built, the revision deployed, partial traffic shifted, and metrics decide promotion. A canary revision accepts a small share of traffic so metrics decide promotion rather than optimism. Local study-map skill 1.4 (Container Apps Deployment and Revisions), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure container hosting documentation: https://learn.microsoft.com/en-us/azure/container-apps/

- **A:** Incorrect for this question. Full traffic cannot move to a revision that does not exist yet, and the image must exist before the revision. Why the correct answer wins: The artifact is built, the revision deployed, partial traffic shifted, and metrics decide promotion.
- **B:** Incorrect for this question. Metrics cannot be checked before the revision serves traffic. Why the correct answer wins: The artifact is built, the revision deployed, partial traffic shifted, and metrics decide promotion.
- **C:** Incorrect for this question. Building after traffic is shifted means the running revision has no reviewed artifact behind it. Why the correct answer wins: The artifact is built, the revision deployed, partial traffic shifted, and metrics decide promotion.
- **D:** Correct. A canary revision accepts a small share of traffic so metrics decide promotion rather than optimism. In this case: The artifact is built, the revision deployed, partial traffic shifted, and metrics decide promotion.

### Question 12 — D

Answer: Query through the Cosmos DB SDK with parameterized queries. SDK queries keep the client supported and return the shaped documents in fewer calls. SDK queries keep the client on the supported data plane and parameterization avoids injection and plan churn. Cross-partition queries still cost more. Local study-map skill 2.1 (Cosmos DB SDK Access and Queries), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Cosmos DB and PostgreSQL vector documentation: https://learn.microsoft.com/en-us/azure/cosmos-db/

- **A:** Incorrect for this question. Request units measure the work a query performs, so tuning the query is often cheaper than adding throughput. Monitor normalized RU consumption. Why the correct answer wins: SDK queries keep the client supported and return the shaped documents in fewer calls.
- **B:** Incorrect for this question. A point or single-partition query avoids fan-out across partitions. Cross-partition queries consume more RUs and add latency. Why the correct answer wins: SDK queries keep the client supported and return the shaped documents in fewer calls.
- **C:** Incorrect for this question. A transactional batch applies all-or-nothing within a single partition key. It cannot span partitions and still consumes RU per operation. Why the correct answer wins: SDK queries keep the client supported and return the shaped documents in fewer calls.
- **D:** Correct. SDK queries keep the client on the supported data plane and parameterization avoids injection and plan churn. Cross-partition queries still cost more. In this case: SDK queries keep the client supported and return the shaped documents in fewer calls.

### Question 13 — B

Answer: Restrict the indexing policy to the paths the queries use. An indexing policy limited to queried paths reduces write charge and storage. Selective indexing cuts write RU charge and storage for unused paths. Excluded paths cannot be filtered efficiently later. Local study-map skill 2.2 (Cosmos DB Indexing Policies and Request Units), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Cosmos DB and PostgreSQL vector documentation: https://learn.microsoft.com/en-us/azure/cosmos-db/

- **A:** Incorrect for this question. Request units measure the work a query performs, so tuning the query is often cheaper than adding throughput. Monitor normalized RU consumption. Why the correct answer wins: An indexing policy limited to queried paths reduces write charge and storage.
- **B:** Correct. Selective indexing cuts write RU charge and storage for unused paths. Excluded paths cannot be filtered efficiently later. In this case: An indexing policy limited to queried paths reduces write charge and storage.
- **C:** Incorrect for this question. Item TTL expires documents automatically, which controls storage growth and data retention. It does not archive the expired content. Why the correct answer wins: An indexing policy limited to queried paths reduces write charge and storage.
- **D:** Incorrect for this question. Indexing everything is simple and makes ad hoc queries possible, at higher write cost and storage. It is a default, not an optimization. Why the correct answer wins: An indexing policy limited to queried paths reduces write charge and storage.

### Question 14 — C

Answer: Choose the account consistency level that matches the read requirement. The account level is a ceiling, and individual reads can relax it toward eventual consistency. Consistency trades freshness against latency, availability, and RU cost. The level is set at the account and can be relaxed per request. Local study-map skill 2.3 (Cosmos DB Consistency Levels), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Cosmos DB and PostgreSQL vector documentation: https://learn.microsoft.com/en-us/azure/cosmos-db/

- **A:** Incorrect for this question. Session consistency guarantees monotonic reads for one session and is the common default for user-facing apps. It does not promise global freshness. Why the correct answer wins: The account level is a ceiling, and individual reads can relax it toward eventual consistency.
- **B:** Incorrect for this question. Eventual consistency is the cheapest and most available option but returns possibly stale data. It fits non-critical counters, not balances. Why the correct answer wins: The account level is a ceiling, and individual reads can relax it toward eventual consistency.
- **C:** Correct. Consistency trades freshness against latency, availability, and RU cost. The level is set at the account and can be relaxed per request. In this case: The account level is a ceiling, and individual reads can relax it toward eventual consistency.
- **D:** Incorrect for this question. Strong consistency guarantees the latest committed write globally at the cost of higher latency and reduced availability during partitions. Why the correct answer wins: The account level is a ceiling, and individual reads can relax it toward eventual consistency.

### Question 15 — A

Answer: Use the DiskANN vector index for large collections. DiskANN targets large collections with better memory efficiency. DiskANN trades some recall for memory efficiency on large sets. Recall and latency should be measured on representative queries. Local study-map skill 2.4 (Cosmos DB Vector Search and Embeddings), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Cosmos DB and PostgreSQL vector documentation: https://learn.microsoft.com/en-us/azure/cosmos-db/

- **A:** Correct. DiskANN trades some recall for memory efficiency on large sets. Recall and latency should be measured on representative queries. In this case: DiskANN targets large collections with better memory efficiency.
- **B:** Incorrect for this question. Distance function choice must match the embedding model and the normalization used at indexing time. A mismatch degrades recall silently. Why the correct answer wins: DiskANN targets large collections with better memory efficiency.
- **C:** Incorrect for this question. Cosmos DB for NoSQL supports vector properties and a distance function for similarity search in the same document store. Dimensions and index type must match the model. Why the correct answer wins: DiskANN targets large collections with better memory efficiency.
- **D:** Incorrect for this question. Application-side scoring works for tiny collections and tests, but it moves all data over the wire and does not scale with corpus size. Why the correct answer wins: DiskANN targets large collections with better memory efficiency.

### Question 16 — D

Answer: Run a change feed processor to react to new and updated items. The change feed streams item changes to a downstream writer. The change feed delivers an ordered stream of changes per partition for downstream processing. It is not a delete feed, so deletions need a workaround. Local study-map skill 2.5 (Cosmos DB Change Feed Processing), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Cosmos DB and PostgreSQL vector documentation: https://learn.microsoft.com/en-us/azure/cosmos-db/

- **A:** Incorrect for this question. A duplicate-detection window drops repeated sends within the window, which helps with at-least-once producers. The window is time-bounded. Why the correct answer wins: The change feed streams item changes to a downstream writer.
- **B:** Incorrect for this question. Leases track partition ownership so multiple processor instances share work and resume from a continuation token. Lease writes consume RUs too. Why the correct answer wins: The change feed streams item changes to a downstream writer.
- **C:** Incorrect for this question. A transactional batch applies all-or-nothing within a single partition key. It cannot span partitions and still consumes RU per operation. Why the correct answer wins: The change feed streams item changes to a downstream writer.
- **D:** Correct. The change feed delivers an ordered stream of changes per partition for downstream processing. It is not a delete feed, so deletions need a workaround. In this case: The change feed streams item changes to a downstream writer.

### Question 17 — C

Answer: Create the container with a vector policy → upsert items with embeddings → query with VectorDistance → apply metadata filters. The container and vector policy are created, then embeddings are written, and only then are similarity queries valid. The vector policy fixes dimensions and index type, so it must exist before vector writes and queries. Local study-map skill 2.5 (Cosmos DB Change Feed Processing), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Cosmos DB and PostgreSQL vector documentation: https://learn.microsoft.com/en-us/azure/cosmos-db/

- **A:** Incorrect for this question. Filtering and querying cannot precede the container and its vector data. Why the correct answer wins: The container and vector policy are created, then embeddings are written, and only then are similarity queries valid.
- **B:** Incorrect for this question. A similarity query needs indexed vectors, which require the container and its policy first. Why the correct answer wins: The container and vector policy are created, then embeddings are written, and only then are similarity queries valid.
- **C:** Correct. The vector policy fixes dimensions and index type, so it must exist before vector writes and queries. In this case: The container and vector policy are created, then embeddings are written, and only then are similarity queries valid.
- **D:** Incorrect for this question. Items cannot be written before the container exists with a matching vector policy. Why the correct answer wins: The container and vector policy are created, then embeddings are written, and only then are similarity queries valid.

### Question 18 — A

Answer: Store embeddings in PostgreSQL by using the pgvector extension. pgvector keeps embeddings beside relational filter columns. pgvector keeps vectors beside relational data, so filters and joins run in one query. Index type and parameter tuning decide latency. Local study-map skill 2.6 (PostgreSQL Connection and Schema Modeling), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Cosmos DB and PostgreSQL vector documentation: https://learn.microsoft.com/en-us/azure/cosmos-db/

- **A:** Correct. pgvector keeps vectors beside relational data, so filters and joins run in one query. Index type and parameter tuning decide latency. In this case: pgvector keeps embeddings beside relational filter columns.
- **B:** Incorrect for this question. Application-side scoring works for tiny collections and tests, but it moves all data over the wire and does not scale with corpus size. Why the correct answer wins: pgvector keeps embeddings beside relational filter columns.
- **C:** Incorrect for this question. Cosmos DB gives globally distributed, low-latency document access with tunable consistency. Partition key and RU planning determine the cost profile. Why the correct answer wins: pgvector keeps embeddings beside relational filter columns.
- **D:** Incorrect for this question. A cache absorbs repeated reads and cuts latency for hot data. Cache keys, TTLs, and invalidation must match the freshness requirement. Why the correct answer wins: pgvector keeps embeddings beside relational filter columns.

### Question 19 — A

Answer: Create an HNSW index for low-latency approximate search. HNSW provides fast approximate search with tunable recall. HNSW gives fast approximate nearest-neighbour queries with a larger memory footprint and slower builds. Recall is tunable at query time. Local study-map skill 2.7 (pgvector Indexing and Query Latency), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Cosmos DB and PostgreSQL vector documentation: https://learn.microsoft.com/en-us/azure/cosmos-db/

- **A:** Correct. HNSW gives fast approximate nearest-neighbour queries with a larger memory footprint and slower builds. Recall is tunable at query time. In this case: HNSW provides fast approximate search with tunable recall.
- **B:** Incorrect for this question. Index builds and large sorts spill to disk when work memory is too small, stretching maintenance windows and slowing queries. Why the correct answer wins: HNSW provides fast approximate search with tunable recall.
- **C:** Incorrect for this question. An exact scan is accurate but scales linearly and burns compute. It is a baseline for measuring recall, not a production strategy. Why the correct answer wins: HNSW provides fast approximate search with tunable recall.
- **D:** Incorrect for this question. IVFFlat uses clustering lists and needs periodic rebuilds as data grows, but costs less memory than HNSW. Probes trade recall for speed. Why the correct answer wins: HNSW provides fast approximate search with tunable recall.

### Question 20 — B

Answer: Scale compute and memory to fit index size and query concurrency. Compute and memory must match the index working set. Vector indexes are memory-hungry, so undersized compute causes swapping and slow queries. Right-size before tuning index parameters. Local study-map skill 2.8 (PostgreSQL Compute, Memory, and Storage Sizing), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Cosmos DB and PostgreSQL vector documentation: https://learn.microsoft.com/en-us/azure/cosmos-db/

- **A:** Incorrect for this question. Index builds and large sorts spill to disk when work memory is too small, stretching maintenance windows and slowing queries. Why the correct answer wins: Compute and memory must match the index working set.
- **B:** Correct. Vector indexes are memory-hungry, so undersized compute causes swapping and slow queries. Right-size before tuning index parameters. In this case: Compute and memory must match the index working set.
- **C:** Incorrect for this question. A bounded pool amortizes connection setup and protects the server from connection storms. Pool size must match server limits. Why the correct answer wins: Compute and memory must match the index working set.
- **D:** Incorrect for this question. Index creation and bulk loads are I/O heavy, and throttled storage stretches maintenance windows. Storage limits are separate from compute. Why the correct answer wins: Compute and memory must match the index working set.

### Question 21 — C

Answer: Place a connection pooler in front of PostgreSQL for many short-lived clients. An external pooler multiplexes many client connections. An external pooler multiplexes server connections for serverless or highly concurrent clients. Session-level features may be unavailable in transaction mode. Local study-map skill 2.10 (PostgreSQL Connection Optimization), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Cosmos DB and PostgreSQL vector documentation: https://learn.microsoft.com/en-us/azure/cosmos-db/

- **A:** Incorrect for this question. Prepared statements avoid repeated planning and reduce chatty network calls. They pair well with pooling but can interact with pool modes. Why the correct answer wins: An external pooler multiplexes many client connections.
- **B:** Incorrect for this question. A bounded pool amortizes connection setup and protects the server from connection storms. Pool size must match server limits. Why the correct answer wins: An external pooler multiplexes many client connections.
- **C:** Correct. An external pooler multiplexes server connections for serverless or highly concurrent clients. Session-level features may be unavailable in transaction mode. In this case: An external pooler multiplexes many client connections.
- **D:** Incorrect for this question. A replica offloads read traffic but introduces replication lag, which is dangerous for freshly written evidence. It does not reduce index memory pressure. Why the correct answer wins: An external pooler multiplexes many client connections.

### Question 22 — D

Answer: Set a TTL on each cached entry. A TTL bounds how stale a cached price tile can become, independently of invalidation. A TTL bounds staleness and reclaims memory without a manual sweep. Too long a TTL hides source changes; too short wastes the cache. Local study-map skill 2.11 (Azure Managed Redis Caching and Invalidation), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Cosmos DB and PostgreSQL vector documentation: https://learn.microsoft.com/en-us/azure/cosmos-db/

- **A:** Incorrect for this question. Write-through or explicit invalidation keeps cached answers consistent with the system of record. Without it, TTL is the only bound on staleness. Why the correct answer wins: A TTL bounds how stale a cached price tile can become, independently of invalidation.
- **B:** Incorrect for this question. Flushing removes all cached content at once, causing a stampede to the origin and a latency cliff. Targeted invalidation is safer. Why the correct answer wins: A TTL bounds how stale a cached price tile can become, independently of invalidation.
- **C:** Incorrect for this question. Eviction protects memory but evicts unpredictably, so a hot key can vanish before its freshness bound is reached. It is not a substitute for TTL design. Why the correct answer wins: A TTL bounds how stale a cached price tile can become, independently of invalidation.
- **D:** Correct. A TTL bounds staleness and reclaims memory without a manual sweep. Too long a TTL hides source changes; too short wastes the cache. In this case: A TTL bounds how stale a cached price tile can become, independently of invalidation.

### Question 23 — B, C

Answers: Use session consistency for reads within the same client session; Use eventual consistency to minimize read cost. Session consistency covers read-your-writes, and eventual consistency is acceptable for tolerant counters. Session consistency guarantees monotonic reads for one session and is the common default for user-facing apps. It does not promise global freshness. Eventual consistency is the cheapest and most available option but returns possibly stale data. It fits non-critical counters, not balances. Local study-map skill 2.3 (Cosmos DB Consistency Levels), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Cosmos DB and PostgreSQL vector documentation: https://learn.microsoft.com/en-us/azure/cosmos-db/

- **A:** Incorrect for this question. Consistency trades freshness against latency, availability, and RU cost. The level is set at the account and can be relaxed per request. Why the correct answer wins: Session consistency covers read-your-writes, and eventual consistency is acceptable for tolerant counters.
- **B:** Correct. Eventual consistency is the cheapest and most available option but returns possibly stale data. It fits non-critical counters, not balances. In this case: Session consistency covers read-your-writes, and eventual consistency is acceptable for tolerant counters.
- **C:** Correct. Session consistency guarantees monotonic reads for one session and is the common default for user-facing apps. It does not promise global freshness. In this case: Session consistency covers read-your-writes, and eventual consistency is acceptable for tolerant counters.
- **D:** Incorrect for this question. Request units measure the work a query performs, so tuning the query is often cheaper than adding throughput. Monitor normalized RU consumption. Why the correct answer wins: Session consistency covers read-your-writes, and eventual consistency is acceptable for tolerant counters.
- **E:** Incorrect for this question. Strong consistency guarantees the latest committed write globally at the cost of higher latency and reduced availability during partitions. Why the correct answer wins: Session consistency covers read-your-writes, and eventual consistency is acceptable for tolerant counters.

### Question 24 — A, C

Answers: Create an IVFFlat index to save memory on a large table; Increase maintenance and query memory settings for index builds and sorts. IVFFlat reduces memory pressure, and adequate work memory avoids spills. IVFFlat uses clustering lists and needs periodic rebuilds as data grows, but costs less memory than HNSW. Probes trade recall for speed. Index builds and large sorts spill to disk when work memory is too small, stretching maintenance windows and slowing queries. Local study-map skill 2.7 (pgvector Indexing and Query Latency), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Cosmos DB and PostgreSQL vector documentation: https://learn.microsoft.com/en-us/azure/cosmos-db/

- **A:** Correct. IVFFlat uses clustering lists and needs periodic rebuilds as data grows, but costs less memory than HNSW. Probes trade recall for speed. In this case: IVFFlat reduces memory pressure, and adequate work memory avoids spills.
- **B:** Incorrect for this question. An exact scan is accurate but scales linearly and burns compute. It is a baseline for measuring recall, not a production strategy. Why the correct answer wins: IVFFlat reduces memory pressure, and adequate work memory avoids spills.
- **C:** Correct. Index builds and large sorts spill to disk when work memory is too small, stretching maintenance windows and slowing queries. In this case: IVFFlat reduces memory pressure, and adequate work memory avoids spills.
- **D:** Incorrect for this question. Index creation and bulk loads are I/O heavy, and throttled storage stretches maintenance windows. Storage limits are separate from compute. Why the correct answer wins: IVFFlat reduces memory pressure, and adequate work memory avoids spills.
- **E:** Incorrect for this question. HNSW gives fast approximate nearest-neighbour queries with a larger memory footprint and slower builds. Recall is tunable at query time. Why the correct answer wins: IVFFlat reduces memory pressure, and adequate work memory avoids spills.

### Question 25 — A

Answer: Queue the work on a Service Bus queue and process it with a worker. A queue with peek-lock completion gives at-least-once processing with recovery. A queue decouples producers from a single consumer group and smooths bursts. Delivery semantics depend on receive mode and completion. Local study-map skill 3.1 (Service Bus Queues and Sessions), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure messaging and Functions documentation: https://learn.microsoft.com/en-us/azure/service-bus-messaging/

- **A:** Correct. A queue decouples producers from a single consumer group and smooths bursts. Delivery semantics depend on receive mode and completion. In this case: A queue with peek-lock completion gives at-least-once processing with recovery.
- **B:** Incorrect for this question. Queue Storage is simple and cheap for large backlogs with at-least-once delivery. It lacks topics, sessions, and scheduled messages. Why the correct answer wins: A queue with peek-lock completion gives at-least-once processing with recovery.
- **C:** Incorrect for this question. Topics fan out one message to independent subscribers, each with its own filter and dead-letter queue. Subscribers process at their own pace. Why the correct answer wins: A queue with peek-lock completion gives at-least-once processing with recovery.
- **D:** Incorrect for this question. Event Hubs ingests high-volume ordered streams with partitions and consumer groups. It is a streaming log, not a task queue. Why the correct answer wins: A queue with peek-lock completion gives at-least-once processing with recovery.

### Question 26 — B

Answer: Use Service Bus sessions to keep related messages ordered. Sessions provide ordered, exclusive processing per session ID. Sessions give ordered, exclusive processing per session ID across competing consumers. They require session-aware senders and receivers. Local study-map skill 3.1 (Service Bus Queues and Sessions), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure messaging and Functions documentation: https://learn.microsoft.com/en-us/azure/service-bus-messaging/

- **A:** Incorrect for this question. Peek-lock keeps the message locked until the handler completes it, giving at-least-once processing with retry. Lock duration must exceed processing time. Why the correct answer wins: Sessions provide ordered, exclusive processing per session ID.
- **B:** Correct. Sessions give ordered, exclusive processing per session ID across competing consumers. They require session-aware senders and receivers. In this case: Sessions provide ordered, exclusive processing per session ID.
- **C:** Incorrect for this question. A delivery cap stops infinite retries of a failing message and moves it to the dead-letter queue. The cap must exceed legitimate transient retries. Why the correct answer wins: Sessions provide ordered, exclusive processing per session ID.
- **D:** Incorrect for this question. A duplicate-detection window drops repeated sends within the window, which helps with at-least-once producers. The window is time-bounded. Why the correct answer wins: Sessions provide ordered, exclusive processing per session ID.

### Question 27 — A

Answer: Add a SQL or correlation filter to a subscription. A subscription filter evaluates message properties before delivery. Subscription filters route only matching messages to a handler, reducing wasted processing. Filter evaluation happens broker-side on message properties. Local study-map skill 3.2 (Service Bus Topics, Subscriptions, and Filters), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure messaging and Functions documentation: https://learn.microsoft.com/en-us/azure/service-bus-messaging/

- **A:** Correct. Subscription filters route only matching messages to a handler, reducing wasted processing. Filter evaluation happens broker-side on message properties. In this case: A subscription filter evaluates message properties before delivery.
- **B:** Incorrect for this question. Topics fan out one message to independent subscribers, each with its own filter and dead-letter queue. Subscribers process at their own pace. Why the correct answer wins: A subscription filter evaluates message properties before delivery.
- **C:** Incorrect for this question. A duplicate-detection window drops repeated sends within the window, which helps with at-least-once producers. The window is time-bounded. Why the correct answer wins: A subscription filter evaluates message properties before delivery.
- **D:** Incorrect for this question. Subject and event-type filters keep handlers focused and reduce cost. Filters are evaluated on event metadata, not payload body. Why the correct answer wins: A subscription filter evaluates message properties before delivery.

### Question 28 — B

Answer: Make the handler idempotent by using a message or business key. An idempotency key makes a replayed message a no-op. At-least-once delivery means duplicates will happen, so the write must tolerate replay. A stored key makes the retry safe. Local study-map skill 3.3 (Service Bus Dead-Lettering and Retries), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure messaging and Functions documentation: https://learn.microsoft.com/en-us/azure/service-bus-messaging/

- **A:** Incorrect for this question. A delivery cap stops infinite retries of a failing message and moves it to the dead-letter queue. The cap must exceed legitimate transient retries. Why the correct answer wins: An idempotency key makes a replayed message a no-op.
- **B:** Correct. At-least-once delivery means duplicates will happen, so the write must tolerate replay. A stored key makes the retry safe. In this case: An idempotency key makes a replayed message a no-op.
- **C:** Incorrect for this question. A duplicate-detection window drops repeated sends within the window, which helps with at-least-once producers. The window is time-bounded. Why the correct answer wins: An idempotency key makes a replayed message a no-op.
- **D:** Incorrect for this question. Dead-lettering preserves poison messages for diagnosis instead of losing them. Resubmission needs a fix and an idempotent handler. Why the correct answer wins: An idempotency key makes a replayed message a no-op.

### Question 29 — C

Answer: Filter the Event Grid subscription by subject or event type. A subject or property filter narrows delivery. Subject and event-type filters keep handlers focused and reduce cost. Filters are evaluated on event metadata, not payload body. Local study-map skill 3.4 (Event Grid Filters, Custom Events, and Retries), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure messaging and Functions documentation: https://learn.microsoft.com/en-us/azure/service-bus-messaging/

- **A:** Incorrect for this question. Event Grid retries failed deliveries with backoff and can store undeliverable events. Handlers must still be idempotent. Why the correct answer wins: A subject or property filter narrows delivery.
- **B:** Incorrect for this question. A custom schema fits domain events that are not resource lifecycle notifications. Consumers must version the schema contract. Why the correct answer wins: A subject or property filter narrows delivery.
- **C:** Correct. Subject and event-type filters keep handlers focused and reduce cost. Filters are evaluated on event metadata, not payload body. In this case: A subject or property filter narrows delivery.
- **D:** Incorrect for this question. Subscription filters route only matching messages to a handler, reducing wasted processing. Filter evaluation happens broker-side on message properties. Why the correct answer wins: A subject or property filter narrows delivery.

### Question 30 — C

Answer: Use input and output bindings instead of hand-written SDK calls. An output binding declares the write target. Bindings reduce boilerplate for common inputs and outputs and are configured declaratively. Complex operations still need the SDK. Local study-map skill 3.5 (Azure Functions Triggers and Bindings), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure messaging and Functions documentation: https://learn.microsoft.com/en-us/azure/service-bus-messaging/

- **A:** Incorrect for this question. Durable Functions provides orchestrations, activities, timers, and retries with checkpointed state. Orchestrator code must stay deterministic. Why the correct answer wins: An output binding declares the write target.
- **B:** Incorrect for this question. A premium plan reduces cold starts and supports virtual network integration and longer timeouts. It costs more than consumption. Why the correct answer wins: An output binding declares the write target.
- **C:** Correct. Bindings reduce boilerplate for common inputs and outputs and are configured declaratively. Complex operations still need the SDK. In this case: An output binding declares the write target.
- **D:** Incorrect for this question. A trigger starts the function when work arrives and handles the receive loop for you. Poison-message behavior is configured in host settings. Why the correct answer wins: An output binding declares the write target.

### Question 31 — C

Answer: Host the function app on a premium plan with pre-warmed instances. A premium plan provides pre-warmed instances and network integration. A premium plan reduces cold starts and supports virtual network integration and longer timeouts. It costs more than consumption. Local study-map skill 3.6 (Function App Configuration and Deployment), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure messaging and Functions documentation: https://learn.microsoft.com/en-us/azure/service-bus-messaging/

- **A:** Incorrect for this question. Durable Functions provides orchestrations, activities, timers, and retries with checkpointed state. Orchestrator code must stay deterministic. Why the correct answer wins: A premium plan provides pre-warmed instances and network integration.
- **B:** Incorrect for this question. Consumption bills per execution and scales automatically, with cold starts and a timeout ceiling. It fits spiky, short work. Why the correct answer wins: A premium plan provides pre-warmed instances and network integration.
- **C:** Correct. A premium plan reduces cold starts and supports virtual network integration and longer timeouts. It costs more than consumption. In this case: A premium plan provides pre-warmed instances and network integration.
- **D:** Incorrect for this question. A staging slot lets a new build warm up and be validated before the swap. Slot settings that must not move are marked sticky. Why the correct answer wins: A premium plan provides pre-warmed instances and network integration.

### Question 32 — A, D

Answers: Publish to a Service Bus topic with multiple subscriptions; Add a SQL or correlation filter to a subscription. A topic provides fan-out, and a subscription filter narrows the analytics feed. Topics fan out one message to independent subscribers, each with its own filter and dead-letter queue. Subscribers process at their own pace. Subscription filters route only matching messages to a handler, reducing wasted processing. Filter evaluation happens broker-side on message properties. Local study-map skill 3.2 (Service Bus Topics, Subscriptions, and Filters), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure messaging and Functions documentation: https://learn.microsoft.com/en-us/azure/service-bus-messaging/

- **A:** Correct. Topics fan out one message to independent subscribers, each with its own filter and dead-letter queue. Subscribers process at their own pace. In this case: A topic provides fan-out, and a subscription filter narrows the analytics feed.
- **B:** Incorrect for this question. Queue Storage is simple and cheap for large backlogs with at-least-once delivery. It lacks topics, sessions, and scheduled messages. Why the correct answer wins: A topic provides fan-out, and a subscription filter narrows the analytics feed.
- **C:** Incorrect for this question. Subject and event-type filters keep handlers focused and reduce cost. Filters are evaluated on event metadata, not payload body. Why the correct answer wins: A topic provides fan-out, and a subscription filter narrows the analytics feed.
- **D:** Correct. Subscription filters route only matching messages to a handler, reducing wasted processing. Filter evaluation happens broker-side on message properties. In this case: A topic provides fan-out, and a subscription filter narrows the analytics feed.
- **E:** Incorrect for this question. A queue decouples producers from a single consumer group and smooths bursts. Delivery semantics depend on receive mode and completion. Why the correct answer wins: A topic provides fan-out, and a subscription filter narrows the analytics feed.

### Question 33 — A, C

Answers: Orchestrate the multi-step workflow with Durable Functions; Move long-running work out of the HTTP request into a queue. Durable orchestration checkpoints progress, and long work is moved out of the HTTP request path. Durable Functions provides orchestrations, activities, timers, and retries with checkpointed state. Orchestrator code must stay deterministic. HTTP requests have platform timeout limits, so long work belongs behind a queue or orchestration with a status endpoint. Local study-map skill 3.5 (Azure Functions Triggers and Bindings), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure messaging and Functions documentation: https://learn.microsoft.com/en-us/azure/service-bus-messaging/

- **A:** Correct. Durable Functions provides orchestrations, activities, timers, and retries with checkpointed state. Orchestrator code must stay deterministic. In this case: Durable orchestration checkpoints progress, and long work is moved out of the HTTP request path.
- **B:** Incorrect for this question. Consumption bills per execution and scales automatically, with cold starts and a timeout ceiling. It fits spiky, short work. Why the correct answer wins: Durable orchestration checkpoints progress, and long work is moved out of the HTTP request path.
- **C:** Correct. HTTP requests have platform timeout limits, so long work belongs behind a queue or orchestration with a status endpoint. In this case: Durable orchestration checkpoints progress, and long work is moved out of the HTTP request path.
- **D:** Incorrect for this question. An HTTP trigger gives a synchronous API endpoint with route and authorization configuration. Long-running work should hand off to a queue. Why the correct answer wins: Durable orchestration checkpoints progress, and long work is moved out of the HTTP request path.
- **E:** Incorrect for this question. Bindings reduce boilerplate for common inputs and outputs and are configured declaratively. Complex operations still need the SDK. Why the correct answer wins: Durable orchestration checkpoints progress, and long work is moved out of the HTTP request path.

### Question 34 — C

Answer: Publish the message → receive with peek-lock → process the work → complete the message → dead-letter after the delivery limit. The message is received, processed, completed, and dead-lettered only after the delivery limit is exhausted. Peek-lock keeps the message until the handler succeeds, and only repeated failures should dead-letter it. Local study-map skill 3.1 (Service Bus Queues and Sessions), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure messaging and Functions documentation: https://learn.microsoft.com/en-us/azure/service-bus-messaging/

- **A:** Incorrect for this question. Work cannot be processed before the message is published and received. Why the correct answer wins: The message is received, processed, completed, and dead-lettered only after the delivery limit is exhausted.
- **B:** Incorrect for this question. Completing a message before processing discards the work and defeats at-least-once delivery. Why the correct answer wins: The message is received, processed, completed, and dead-lettered only after the delivery limit is exhausted.
- **C:** Correct. Peek-lock keeps the message until the handler succeeds, and only repeated failures should dead-letter it. In this case: The message is received, processed, completed, and dead-lettered only after the delivery limit is exhausted.
- **D:** Incorrect for this question. The message cannot be received before it is published, and completion must follow processing. Why the correct answer wins: The message is received, processed, completed, and dead-lettered only after the delivery limit is exhausted.

### Question 35 — B

Answer: Store the secret in Azure Key Vault and read it at runtime. Key Vault centralizes secret storage with audit and access control. A vault centralizes secret storage with access control and audit. Retrieval should use an identity, not a copied credential. Local study-map skill 4.1 (Key Vault Secret Storage, Rotation, and Retrieval), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Key Vault, App Configuration, and Monitor documentation: https://learn.microsoft.com/en-us/azure/azure-monitor/

- **A:** Incorrect for this question. App Configuration separates configuration from code and supports labels, feature flags, and Key Vault references. Change still needs a refresh strategy. Why the correct answer wins: Key Vault centralizes secret storage with audit and access control.
- **B:** Correct. A vault centralizes secret storage with access control and audit. Retrieval should use an identity, not a copied credential. In this case: Key Vault centralizes secret storage with audit and access control.
- **C:** Incorrect for this question. Pinning a version makes a rotation invisible to the app until it is redeployed, which is useful for break-glass and dangerous for routine rotation. Why the correct answer wins: Key Vault centralizes secret storage with audit and access control.
- **D:** Incorrect for this question. Application settings become environment variables for the container and can be swapped per slot. Sensitive values should still reference a vault. Why the correct answer wins: Key Vault centralizes secret storage with audit and access control.

### Question 36 — D

Answer: Rotate the secret on a schedule and let apps resolve the current version. Scheduled rotation with current-version reads keeps the service working. Rotation limits the value of a leaked secret, but callers must read the latest version rather than caching an old one forever. Local study-map skill 4.1 (Key Vault Secret Storage, Rotation, and Retrieval), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Key Vault, App Configuration, and Monitor documentation: https://learn.microsoft.com/en-us/azure/azure-monitor/

- **A:** Incorrect for this question. Vault access is a separate authorization decision from the app identity. Without a data-plane role or policy the reference fails at runtime. Why the correct answer wins: Scheduled rotation with current-version reads keeps the service working.
- **B:** Incorrect for this question. Soft delete and purge protection stop accidental or malicious permanent loss of secrets. They also constrain how names can be reused. Why the correct answer wins: Scheduled rotation with current-version reads keeps the service working.
- **C:** Incorrect for this question. Pinning a version makes a rotation invisible to the app until it is redeployed, which is useful for break-glass and dangerous for routine rotation. Why the correct answer wins: Scheduled rotation with current-version reads keeps the service working.
- **D:** Correct. Rotation limits the value of a leaked secret, but callers must read the latest version rather than caching an old one forever. In this case: Scheduled rotation with current-version reads keeps the service working.

### Question 37 — A

Answer: Enable configuration refresh so changes apply without a restart. Configuration refresh lets a running service apply changes. Sentinel-key or polling refresh lets a running app pick up new settings. Refresh intervals trade responsiveness against request volume. Local study-map skill 4.2 (App Configuration Settings and Feature Flags), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Key Vault, App Configuration, and Monitor documentation: https://learn.microsoft.com/en-us/azure/azure-monitor/

- **A:** Correct. Sentinel-key or polling refresh lets a running app pick up new settings. Refresh intervals trade responsiveness against request volume. In this case: Configuration refresh lets a running service apply changes.
- **B:** Incorrect for this question. Pipeline deployment keeps code and configuration versioned together and repeatable. Secrets belong in a vault reference, not in the pipeline file. Why the correct answer wins: Configuration refresh lets a running service apply changes.
- **C:** Incorrect for this question. Labels keep dev, test, and prod values in one store with one key schema. A misconfigured label selector silently serves the wrong values. Why the correct answer wins: Configuration refresh lets a running service apply changes.
- **D:** Incorrect for this question. Pinning a version makes a rotation invisible to the app until it is redeployed, which is useful for break-glass and dangerous for routine rotation. Why the correct answer wins: Configuration refresh lets a running service apply changes.

### Question 38 — D

Answer: Use App Configuration labels to separate environments. Labels separate environment or market values under the same keys. Labels keep dev, test, and prod values in one store with one key schema. A misconfigured label selector silently serves the wrong values. Local study-map skill 4.2 (App Configuration Settings and Feature Flags), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Key Vault, App Configuration, and Monitor documentation: https://learn.microsoft.com/en-us/azure/azure-monitor/

- **A:** Incorrect for this question. Pinning a version makes a rotation invisible to the app until it is redeployed, which is useful for break-glass and dangerous for routine rotation. Why the correct answer wins: Labels separate environment or market values under the same keys.
- **B:** Incorrect for this question. App Configuration separates configuration from code and supports labels, feature flags, and Key Vault references. Change still needs a refresh strategy. Why the correct answer wins: Labels separate environment or market values under the same keys.
- **C:** Incorrect for this question. A Key Vault reference keeps non-secret settings in App Configuration while the value stays in the vault. The app identity needs both sets of permissions. Why the correct answer wins: Labels separate environment or market values under the same keys.
- **D:** Correct. Labels keep dev, test, and prod values in one store with one key schema. A misconfigured label selector silently serves the wrong values. In this case: Labels separate environment or market values under the same keys.

### Question 39 — C

Answer: Use head or tail sampling so trace volume stays within budget. Tail sampling retains failures while reducing routine volume. Sampling keeps telemetry cost bounded, but aggressive sampling can hide rare failures. Tail sampling can retain errors preferentially. Local study-map skill 4.3 (Distributed Tracing with OpenTelemetry), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Key Vault, App Configuration, and Monitor documentation: https://learn.microsoft.com/en-us/azure/azure-monitor/

- **A:** Incorrect for this question. Propagation stitches one trace across HTTP, messaging, and Functions so the whole path is visible. Missing propagation breaks the trace at that hop. Why the correct answer wins: Tail sampling retains failures while reducing routine volume.
- **B:** Incorrect for this question. A collector batches, filters, and routes telemetry, and decouples app configuration from the backend. It is another component to run and monitor. Why the correct answer wins: Tail sampling retains failures while reducing routine volume.
- **C:** Correct. Sampling keeps telemetry cost bounded, but aggressive sampling can hide rare failures. Tail sampling can retain errors preferentially. In this case: Tail sampling retains failures while reducing routine volume.
- **D:** Incorrect for this question. OpenTelemetry emits vendor-neutral traces, metrics, and logs with context propagation. Exporters and sampling decide what reaches the backend. Why the correct answer wins: Tail sampling retains failures while reducing routine volume.

### Question 40 — A

Answer: Store repeated aggregations in a materialized view or update policy. Materializing the aggregation avoids repeated computation. Precomputed results avoid recomputing expensive aggregations on every dashboard refresh. The trade-off is storage and freshness lag. Local study-map skill 4.4 (KQL Queries for Logs and Metrics), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Key Vault, App Configuration, and Monitor documentation: https://learn.microsoft.com/en-us/azure/azure-monitor/

- **A:** Correct. Precomputed results avoid recomputing expensive aggregations on every dashboard refresh. The trade-off is storage and freshness lag. In this case: Materializing the aggregation avoids repeated computation.
- **B:** Incorrect for this question. Reducing columns and rows early lowers query cost and latency. Broad queries over long ranges are the usual cause of slow KQL. Why the correct answer wins: Materializing the aggregation avoids repeated computation.
- **C:** Incorrect for this question. An alert turns a threshold breach into a notification or action. Thresholds need a baseline, or the alert is noise. Why the correct answer wins: Materializing the aggregation avoids repeated computation.
- **D:** Incorrect for this question. Time-binned aggregation reveals the shape of an incident: a step change, a ramp, or a periodic spike. Averages alone hide short outages. Why the correct answer wins: Materializing the aggregation avoids repeated computation.

### Question 41 — B

Answer: Assign a least-privilege role to the application identity. Scope a separate read-only identity for the storefront. A scoped role grants only the operations the app performs and limits blast radius. Prefer built-in roles over broad contributor grants. Local study-map skill 4.5 (Identity-Based Access for Application Services), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Key Vault, App Configuration, and Monitor documentation: https://learn.microsoft.com/en-us/azure/azure-monitor/

- **A:** Incorrect for this question. Platform logs and metrics must be routed before they can be queried or alerted on. Retention and cost follow the workspace settings. Why the correct answer wins: Scope a separate read-only identity for the storefront.
- **B:** Correct. A scoped role grants only the operations the app performs and limits blast radius. Prefer built-in roles over broad contributor grants. In this case: Scope a separate read-only identity for the storefront.
- **C:** Incorrect for this question. A managed identity issues tokens from the platform, removing secret distribution from the app. Role assignment still scopes what it can reach. Why the correct answer wins: Scope a separate read-only identity for the storefront.
- **D:** Incorrect for this question. A private endpoint keeps traffic on the virtual network and removes public exposure. DNS resolution must be wired to the private zone. Why the correct answer wins: Scope a separate read-only identity for the storefront.

### Question 42 — B, D

Answers: Instrument the service with the OpenTelemetry SDK; Export telemetry through an OpenTelemetry collector. OpenTelemetry instrumentation is vendor-neutral, and a collector routes telemetry to backends. OpenTelemetry emits vendor-neutral traces, metrics, and logs with context propagation. Exporters and sampling decide what reaches the backend. A collector batches, filters, and routes telemetry, and decouples app configuration from the backend. It is another component to run and monitor. Local study-map skill 4.3 (Distributed Tracing with OpenTelemetry), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Key Vault, App Configuration, and Monitor documentation: https://learn.microsoft.com/en-us/azure/azure-monitor/

- **A:** Incorrect for this question. Sampling keeps telemetry cost bounded, but aggressive sampling can hide rare failures. Tail sampling can retain errors preferentially. Why the correct answer wins: OpenTelemetry instrumentation is vendor-neutral, and a collector routes telemetry to backends.
- **B:** Correct. OpenTelemetry emits vendor-neutral traces, metrics, and logs with context propagation. Exporters and sampling decide what reaches the backend. In this case: OpenTelemetry instrumentation is vendor-neutral, and a collector routes telemetry to backends.
- **C:** Incorrect for this question. Platform logs and metrics must be routed before they can be queried or alerted on. Retention and cost follow the workspace settings. Why the correct answer wins: OpenTelemetry instrumentation is vendor-neutral, and a collector routes telemetry to backends.
- **D:** Correct. A collector batches, filters, and routes telemetry, and decouples app configuration from the backend. It is another component to run and monitor. In this case: OpenTelemetry instrumentation is vendor-neutral, and a collector routes telemetry to backends.
- **E:** Incorrect for this question. KQL filters, projects, and aggregates log and metric tables in Log Analytics. Start narrow with a time range and a request ID. Why the correct answer wins: OpenTelemetry instrumentation is vendor-neutral, and a collector routes telemetry to backends.

### Question 43 — A, C

Answers: Reach the data service through a private endpoint; Federate a Kubernetes service account to a managed identity. A private endpoint removes the public path, and workload identity removes stored credentials. A private endpoint keeps traffic on the virtual network and removes public exposure. DNS resolution must be wired to the private zone. Workload identity lets pods obtain tokens without stored secrets. Each workload should get its own identity and narrow role. Local study-map skill 4.5 (Identity-Based Access for Application Services), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Key Vault, App Configuration, and Monitor documentation: https://learn.microsoft.com/en-us/azure/azure-monitor/

- **A:** Correct. Workload identity lets pods obtain tokens without stored secrets. Each workload should get its own identity and narrow role. In this case: A private endpoint removes the public path, and workload identity removes stored credentials.
- **B:** Incorrect for this question. A vault centralizes secret storage with access control and audit. Retrieval should use an identity, not a copied credential. Why the correct answer wins: A private endpoint removes the public path, and workload identity removes stored credentials.
- **C:** Correct. A private endpoint keeps traffic on the virtual network and removes public exposure. DNS resolution must be wired to the private zone. In this case: A private endpoint removes the public path, and workload identity removes stored credentials.
- **D:** Incorrect for this question. A scoped role grants only the operations the app performs and limits blast radius. Prefer built-in roles over broad contributor grants. Why the correct answer wins: A private endpoint removes the public path, and workload identity removes stored credentials.
- **E:** Incorrect for this question. Platform metrics are cheap and near-real-time, so they suit latency and failure-rate alerts. Log-based alerts add latency and query cost. Why the correct answer wins: A private endpoint removes the public path, and workload identity removes stored credentials.

### Question 44 — C

Answer: Store the secret in Key Vault → grant the app identity access → reference the secret from the app → rotate the secret → the app reads the new version. Store the secret, grant access, reference it from the app, rotate it, and read the current version. Access must be granted before the reference resolves, and the app must read the current version after rotation. Local study-map skill 4.1 (Key Vault Secret Storage, Rotation, and Retrieval), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Key Vault, App Configuration, and Monitor documentation: https://learn.microsoft.com/en-us/azure/azure-monitor/

- **A:** Incorrect for this question. A reference cannot resolve before the secret and the access grant exist. Why the correct answer wins: Store the secret, grant access, reference it from the app, rotate it, and read the current version.
- **B:** Incorrect for this question. Access can be granted first, but rotation cannot precede storing the secret. Why the correct answer wins: Store the secret, grant access, reference it from the app, rotate it, and read the current version.
- **C:** Correct. Access must be granted before the reference resolves, and the app must read the current version after rotation. In this case: Store the secret, grant access, reference it from the app, rotate it, and read the current version.
- **D:** Incorrect for this question. There is nothing to rotate or reference before the secret is stored. Why the correct answer wins: Store the secret, grant access, reference it from the app, rotate it, and read the current version.

### Question 45 — B

Answer: Apply an ACR retention policy to prune old untagged manifests. A retention policy prunes untagged manifests while leaving the versioned tags that deployments reference. A retention policy controls storage growth and registry clutter. It does not change which image tag a deployment references. Local study-map skill 1.1 (Container Image Lifecycle in Azure Container Registry), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure container hosting documentation: https://learn.microsoft.com/en-us/azure/container-apps/

- **A:** Incorrect for this question. A floating tag removes the link between a deployed revision and a specific build, so rollback and audit become guesswork. Why the correct answer wins: A retention policy prunes untagged manifests while leaving the versioned tags that deployments reference.
- **B:** Correct. A retention policy controls storage growth and registry clutter. It does not change which image tag a deployment references. In this case: A retention policy prunes untagged manifests while leaving the versioned tags that deployments reference.
- **C:** Incorrect for this question. ACR keeps tagged, versioned images next to the deployment target and supports identity-based pulls. Tagging strategy and retention still need a decision. Why the correct answer wins: A retention policy prunes untagged manifests while leaving the versioned tags that deployments reference.
- **D:** Incorrect for this question. Geo-replication reduces cross-region pull latency and gives a local copy during a regional failure. It adds cost and replication management. Why the correct answer wins: A retention policy prunes untagged manifests while leaving the versioned tags that deployments reference.

### Question 46 — D

Answer: Run image builds on demand or on a trigger with ACR Tasks. ACR Tasks runs multi-step and multi-platform builds in Azure on a commit trigger, so no build farm is maintained. ACR Tasks builds images in Azure on a commit or schedule without a local Docker host. It removes build-host drift but not image review. Local study-map skill 1.2 (Automated Image Builds with ACR Tasks), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure container hosting documentation: https://learn.microsoft.com/en-us/azure/container-apps/

- **A:** Incorrect for this question. ACR keeps tagged, versioned images next to the deployment target and supports identity-based pulls. Tagging strategy and retention still need a decision. Why the correct answer wins: ACR Tasks runs multi-step and multi-platform builds in Azure on a commit trigger, so no build farm is maintained.
- **B:** Incorrect for this question. AKS gives full Kubernetes control, including custom controllers and networking. You own node pools, upgrades, and manifest hygiene. Why the correct answer wins: ACR Tasks runs multi-step and multi-platform builds in Azure on a commit trigger, so no build farm is maintained.
- **C:** Incorrect for this question. Container Apps provides a managed environment, revisions, and KEDA-based scaling without cluster administration. Platform limits differ from AKS. Why the correct answer wins: ACR Tasks runs multi-step and multi-platform builds in Azure on a commit trigger, so no build farm is maintained.
- **D:** Correct. ACR Tasks builds images in Azure on a commit or schedule without a local Docker host. It removes build-host drift but not image review. In this case: ACR Tasks runs multi-step and multi-platform builds in Azure on a commit trigger, so no build farm is maintained.

### Question 47 — D

Answer: Supply configuration through App Service application settings. Application settings become environment variables per slot, so a regional endpoint change needs no new image. Application settings become environment variables for the container and can be swapped per slot. Sensitive values should still reference a vault. Local study-map skill 1.3 (Container Deployment to Azure App Service), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure container hosting documentation: https://learn.microsoft.com/en-us/azure/container-apps/

- **A:** Incorrect for this question. A ConfigMap injects settings as environment variables or mounted files without rebuilding the image. Secrets still belong in Key Vault, not in a ConfigMap. Why the correct answer wins: Application settings become environment variables per slot, so a regional endpoint change needs no new image.
- **B:** Incorrect for this question. App Configuration separates configuration from code and supports labels, feature flags, and Key Vault references. Change still needs a refresh strategy. Why the correct answer wins: Application settings become environment variables per slot, so a regional endpoint change needs no new image.
- **C:** Incorrect for this question. Pinning a version makes a rotation invisible to the app until it is redeployed, which is useful for break-glass and dangerous for routine rotation. Why the correct answer wins: Application settings become environment variables per slot, so a regional endpoint change needs no new image.
- **D:** Correct. Application settings become environment variables for the container and can be swapped per slot. Sensitive values should still reference a vault. In this case: Application settings become environment variables per slot, so a regional endpoint change needs no new image.

### Question 48 — C

Answer: Deploy into a Container Apps environment attached to the workload virtual network. Attaching the Container Apps environment to the workload virtual network gives private routing to its dependencies. A virtual-network-attached environment enables private access to dependencies and internal ingress. It also shifts DNS and egress design to you. Local study-map skill 1.4 (Container Apps Deployment and Revisions), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure container hosting documentation: https://learn.microsoft.com/en-us/azure/container-apps/

- **A:** Incorrect for this question. Revision-based traffic splitting enables canary and blue-green releases. Revision mode and scale rules must be set deliberately. Why the correct answer wins: Attaching the Container Apps environment to the workload virtual network gives private routing to its dependencies.
- **B:** Incorrect for this question. Internal ingress keeps the endpoint inside the environment virtual network. It is an exposure control, not an authorization control. Why the correct answer wins: Attaching the Container Apps environment to the workload virtual network gives private routing to its dependencies.
- **C:** Correct. A virtual-network-attached environment enables private access to dependencies and internal ingress. It also shifts DNS and egress design to you. In this case: Attaching the Container Apps environment to the workload virtual network gives private routing to its dependencies.
- **D:** Incorrect for this question. KEDA scalers drive replica count from queue length, lag, or other event metrics, including scale to zero. Cool-down and max replicas bound the behavior. Why the correct answer wins: Attaching the Container Apps environment to the workload virtual network gives private routing to its dependencies.

### Question 49 — B

Answer: Run the batch work as a Container Apps job. A Container Apps job runs to completion and exits, which suits batch work that should not serve traffic. Container Apps jobs run to completion with their own trigger and retry semantics, unlike a long-lived revision. They fit scheduled or queue-driven batches. Local study-map skill 1.4 (Container Apps Deployment and Revisions), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure container hosting documentation: https://learn.microsoft.com/en-us/azure/container-apps/

- **A:** Incorrect for this question. Container Apps provides a managed environment, revisions, and KEDA-based scaling without cluster administration. Platform limits differ from AKS. Why the correct answer wins: A Container Apps job runs to completion and exits, which suits batch work that should not serve traffic.
- **B:** Correct. Container Apps jobs run to completion with their own trigger and retry semantics, unlike a long-lived revision. They fit scheduled or queue-driven batches. In this case: A Container Apps job runs to completion and exits, which suits batch work that should not serve traffic.
- **C:** Incorrect for this question. Revision-based traffic splitting enables canary and blue-green releases. Revision mode and scale rules must be set deliberately. Why the correct answer wins: A Container Apps job runs to completion and exits, which suits batch work that should not serve traffic.
- **D:** Incorrect for this question. Container Instances starts a single container group quickly for short tasks. It has no orchestrator-level scaling or revision model. Why the correct answer wins: A Container Apps job runs to completion and exits, which suits batch work that should not serve traffic.

### Question 50 — B

Answer: Scale on the Service Bus queue length with a KEDA Azure Service Bus scaler. A queue-length scaler adds consumers while messages are waiting and scales to zero once the queue empties. A queue-length scaler adds replicas while work is backed up and removes them when the queue drains. Message lock duration must exceed processing time. Local study-map skill 1.5 (Event-Driven Scaling with KEDA), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure container hosting documentation: https://learn.microsoft.com/en-us/azure/container-apps/

- **A:** Incorrect for this question. Container Instances starts a single container group quickly for short tasks. It has no orchestrator-level scaling or revision model. Why the correct answer wins: A queue-length scaler adds consumers while messages are waiting and scales to zero once the queue empties.
- **B:** Correct. A queue-length scaler adds replicas while work is backed up and removes them when the queue drains. Message lock duration must exceed processing time. In this case: A queue-length scaler adds consumers while messages are waiting and scales to zero once the queue empties.
- **C:** Incorrect for this question. HPA adjusts replicas from resource metrics but needs metrics-server and enough node capacity. It cannot scale to zero. Why the correct answer wins: A queue-length scaler adds consumers while messages are waiting and scales to zero once the queue empties.
- **D:** Incorrect for this question. CPU-based scaling reacts after work is already queued and cannot scale to zero on an empty queue. It suits steady request-driven services. Why the correct answer wins: A queue-length scaler adds consumers while messages are waiting and scales to zero once the queue empties.

### Question 51 — D

Answer: Federate a Kubernetes service account to a managed identity. Federating the service account to a managed identity lets the kubelet authenticate to the registry without a stored secret. Workload identity lets pods obtain tokens without stored secrets. Each workload should get its own identity and narrow role. Local study-map skill 1.6 (AKS Deployment with Manifests), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure container hosting documentation: https://learn.microsoft.com/en-us/azure/container-apps/

- **A:** Incorrect for this question. A floating tag removes the link between a deployed revision and a specific build, so rollback and audit become guesswork. Why the correct answer wins: Federating the service account to a managed identity lets the kubelet authenticate to the registry without a stored secret.
- **B:** Incorrect for this question. Geo-replication reduces cross-region pull latency and gives a local copy during a regional failure. It adds cost and replication management. Why the correct answer wins: Federating the service account to a managed identity lets the kubelet authenticate to the registry without a stored secret.
- **C:** Incorrect for this question. A Key Vault reference resolves at runtime so the secret is never written into application settings. The app identity still needs permission to read it. Why the correct answer wins: Federating the service account to a managed identity lets the kubelet authenticate to the registry without a stored secret.
- **D:** Correct. Workload identity lets pods obtain tokens without stored secrets. Each workload should get its own identity and narrow role. In this case: Federating the service account to a managed identity lets the kubelet authenticate to the registry without a stored secret.

### Question 52 — A

Answer: Enable diagnostic settings to route platform logs to the workspace. Diagnostic settings forward platform logs and metrics to the workspace where application telemetry already lives. Platform logs and metrics must be routed before they can be queried or alerted on. Retention and cost follow the workspace settings. Local study-map skill 1.7 (Container Logs, Events, and Connectivity), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure container hosting documentation: https://learn.microsoft.com/en-us/azure/container-apps/

- **A:** Correct. Platform logs and metrics must be routed before they can be queried or alerted on. Retention and cost follow the workspace settings. In this case: Diagnostic settings forward platform logs and metrics to the workspace where application telemetry already lives.
- **B:** Incorrect for this question. Reducing columns and rows early lowers query cost and latency. Broad queries over long ranges are the usual cause of slow KQL. Why the correct answer wins: Diagnostic settings forward platform logs and metrics to the workspace where application telemetry already lives.
- **C:** Incorrect for this question. Container Apps and AKS surface stdout logs and platform events into a workspace for KQL analysis. Verbosity and retention cost money. Why the correct answer wins: Diagnostic settings forward platform logs and metrics to the workspace where application telemetry already lives.
- **D:** Incorrect for this question. Platform metrics are cheap and near-real-time, so they suit latency and failure-rate alerts. Log-based alerts add latency and query cost. Why the correct answer wins: Diagnostic settings forward platform logs and metrics to the workspace where application telemetry already lives.

### Question 53 — B

Answer: Create an Azure service connector binding between the app and the dependency. A service connector binding generates the identity-based configuration between the app and the dependency. A service connector writes connection details and can provision identity-based access. The resulting configuration should still be reviewed. Local study-map skill 1.3 (Container Deployment to Azure App Service), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure container hosting documentation: https://learn.microsoft.com/en-us/azure/container-apps/

- **A:** Incorrect for this question. Application settings become environment variables for the container and can be swapped per slot. Sensitive values should still reference a vault. Why the correct answer wins: A service connector binding generates the identity-based configuration between the app and the dependency.
- **B:** Correct. A service connector writes connection details and can provision identity-based access. The resulting configuration should still be reviewed. In this case: A service connector binding generates the identity-based configuration between the app and the dependency.
- **C:** Incorrect for this question. A ConfigMap injects settings as environment variables or mounted files without rebuilding the image. Secrets still belong in Key Vault, not in a ConfigMap. Why the correct answer wins: A service connector binding generates the identity-based configuration between the app and the dependency.
- **D:** Incorrect for this question. A Key Vault reference resolves at runtime so the secret is never written into application settings. The app identity still needs permission to read it. Why the correct answer wins: A service connector binding generates the identity-based configuration between the app and the dependency.

### Question 54 — B, E

Answers: Scale the container app on an event source with a KEDA scaler; Tune the scale rule cool-down period and maximum replicas. A KEDA scaler drives replicas from queue depth, and a bounded cool-down and maximum stop the thrashing. KEDA scalers drive replica count from queue length, lag, or other event metrics, including scale to zero. Cool-down and max replicas bound the behavior. Cool-down prevents replica flapping, and a maximum replica cap bounds cost and downstream load. Both are per-rule settings. Local study-map skill 1.5 (Event-Driven Scaling with KEDA), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure container hosting documentation: https://learn.microsoft.com/en-us/azure/container-apps/

- **A:** Incorrect for this question. Container Instances starts a single container group quickly for short tasks. It has no orchestrator-level scaling or revision model. Why the correct answer wins: A KEDA scaler drives replicas from queue depth, and a bounded cool-down and maximum stop the thrashing.
- **B:** Correct. Cool-down prevents replica flapping, and a maximum replica cap bounds cost and downstream load. Both are per-rule settings. In this case: A KEDA scaler drives replicas from queue depth, and a bounded cool-down and maximum stop the thrashing.
- **C:** Incorrect for this question. CPU-based scaling reacts after work is already queued and cannot scale to zero on an empty queue. It suits steady request-driven services. Why the correct answer wins: A KEDA scaler drives replicas from queue depth, and a bounded cool-down and maximum stop the thrashing.
- **D:** Incorrect for this question. HPA adjusts replicas from resource metrics but needs metrics-server and enough node capacity. It cannot scale to zero. Why the correct answer wins: A KEDA scaler drives replicas from queue depth, and a bounded cool-down and maximum stop the thrashing.
- **E:** Correct. KEDA scalers drive replica count from queue length, lag, or other event metrics, including scale to zero. Cool-down and max replicas bound the behavior. In this case: A KEDA scaler drives replicas from queue depth, and a bounded cool-down and maximum stop the thrashing.

### Question 55 — A

Answer: Build and push the image → deploy a new revision → shift a small traffic percentage → check metrics → promote or roll back. The image is built and pushed before the revision, traffic shifts after it, and promotion follows metrics. A canary revision accepts a small share of traffic so metrics decide promotion rather than optimism. Local study-map skill 1.4 (Container Apps Deployment and Revisions), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure container hosting documentation: https://learn.microsoft.com/en-us/azure/container-apps/

- **A:** Correct. A canary revision accepts a small share of traffic so metrics decide promotion rather than optimism. In this case: The image is built and pushed before the revision, traffic shifts after it, and promotion follows metrics.
- **B:** Incorrect for this question. Metrics cannot be checked before the revision serves traffic. Why the correct answer wins: The image is built and pushed before the revision, traffic shifts after it, and promotion follows metrics.
- **C:** Incorrect for this question. Building after traffic is shifted means the running revision has no reviewed artifact behind it. Why the correct answer wins: The image is built and pushed before the revision, traffic shifts after it, and promotion follows metrics.
- **D:** Incorrect for this question. Full traffic cannot move to a revision that does not exist yet, and the image must exist before the revision. Why the correct answer wins: The image is built and pushed before the revision, traffic shifts after it, and promotion follows metrics.

### Question 56 — A

Answer: Store the documents in Azure Cosmos DB for NoSQL. Cosmos DB for NoSQL keeps the document with a market partition key and serves point reads from one partition. Cosmos DB gives globally distributed, low-latency document access with tunable consistency. Partition key and RU planning determine the cost profile. Local study-map skill 2.1 (Cosmos DB SDK Access and Queries), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Cosmos DB and PostgreSQL vector documentation: https://learn.microsoft.com/en-us/azure/cosmos-db/

- **A:** Correct. Cosmos DB gives globally distributed, low-latency document access with tunable consistency. Partition key and RU planning determine the cost profile. In this case: Cosmos DB for NoSQL keeps the document with a market partition key and serves point reads from one partition.
- **B:** Incorrect for this question. pgvector keeps vectors beside relational data, so filters and joins run in one query. Index type and parameter tuning decide latency. Why the correct answer wins: Cosmos DB for NoSQL keeps the document with a market partition key and serves point reads from one partition.
- **C:** Incorrect for this question. Queue Storage is simple and cheap for large backlogs with at-least-once delivery. It lacks topics, sessions, and scheduled messages. Why the correct answer wins: Cosmos DB for NoSQL keeps the document with a market partition key and serves point reads from one partition.
- **D:** Incorrect for this question. A point or single-partition query avoids fan-out across partitions. Cross-partition queries consume more RUs and add latency. Why the correct answer wins: Cosmos DB for NoSQL keeps the document with a market partition key and serves point reads from one partition.

### Question 57 — D

Answer: Choose a high-cardinality partition key that spreads writes. A high-cardinality key such as the order identifier spreads writes evenly across physical partitions. A good partition key distributes storage and throughput and keeps common queries single-partition. Low cardinality creates hot partitions. Local study-map skill 2.1 (Cosmos DB SDK Access and Queries), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Cosmos DB and PostgreSQL vector documentation: https://learn.microsoft.com/en-us/azure/cosmos-db/

- **A:** Incorrect for this question. Indexing everything is simple and makes ad hoc queries possible, at higher write cost and storage. It is a default, not an optimization. Why the correct answer wins: A high-cardinality key such as the order identifier spreads writes evenly across physical partitions.
- **B:** Incorrect for this question. A point or single-partition query avoids fan-out across partitions. Cross-partition queries consume more RUs and add latency. Why the correct answer wins: A high-cardinality key such as the order identifier spreads writes evenly across physical partitions.
- **C:** Incorrect for this question. Request units measure the work a query performs, so tuning the query is often cheaper than adding throughput. Monitor normalized RU consumption. Why the correct answer wins: A high-cardinality key such as the order identifier spreads writes evenly across physical partitions.
- **D:** Correct. A good partition key distributes storage and throughput and keeps common queries single-partition. Low cardinality creates hot partitions. In this case: A high-cardinality key such as the order identifier spreads writes evenly across physical partitions.

### Question 58 — B

Answer: Restrict the indexing policy to the paths the queries use. Restricting the indexing policy to the queried paths removes write charge for properties nobody queries. Selective indexing cuts write RU charge and storage for unused paths. Excluded paths cannot be filtered efficiently later. Local study-map skill 2.2 (Cosmos DB Indexing Policies and Request Units), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Cosmos DB and PostgreSQL vector documentation: https://learn.microsoft.com/en-us/azure/cosmos-db/

- **A:** Incorrect for this question. Indexing everything is simple and makes ad hoc queries possible, at higher write cost and storage. It is a default, not an optimization. Why the correct answer wins: Restricting the indexing policy to the queried paths removes write charge for properties nobody queries.
- **B:** Correct. Selective indexing cuts write RU charge and storage for unused paths. Excluded paths cannot be filtered efficiently later. In this case: Restricting the indexing policy to the queried paths removes write charge for properties nobody queries.
- **C:** Incorrect for this question. Autoscale follows demand between a minimum and maximum, avoiding throttling at peak without paying for peak all day. The maximum still caps the bill. Why the correct answer wins: Restricting the indexing policy to the queried paths removes write charge for properties nobody queries.
- **D:** Incorrect for this question. A composite index lets a query filter and order on several paths without a runtime sort. It adds write cost for exactly those paths. Why the correct answer wins: Restricting the indexing policy to the queried paths removes write charge for properties nobody queries.

### Question 59 — A

Answer: Choose the account consistency level that matches the read requirement. The account consistency level is the documented setting that must match the read requirement of every consumer. Consistency trades freshness against latency, availability, and RU cost. The level is set at the account and can be relaxed per request. Local study-map skill 2.3 (Cosmos DB Consistency Levels), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Cosmos DB and PostgreSQL vector documentation: https://learn.microsoft.com/en-us/azure/cosmos-db/

- **A:** Correct. Consistency trades freshness against latency, availability, and RU cost. The level is set at the account and can be relaxed per request. In this case: The account consistency level is the documented setting that must match the read requirement of every consumer.
- **B:** Incorrect for this question. Eventual consistency is the cheapest and most available option but returns possibly stale data. It fits non-critical counters, not balances. Why the correct answer wins: The account consistency level is the documented setting that must match the read requirement of every consumer.
- **C:** Incorrect for this question. Strong consistency guarantees the latest committed write globally at the cost of higher latency and reduced availability during partitions. Why the correct answer wins: The account consistency level is the documented setting that must match the read requirement of every consumer.
- **D:** Incorrect for this question. Session consistency guarantees monotonic reads for one session and is the common default for user-facing apps. It does not promise global freshness. Why the correct answer wins: The account consistency level is the documented setting that must match the read requirement of every consumer.

### Question 60 — D

Answer: Declare the embedding dimensions and vector index type on the container policy. The container vector policy declares dimensions and index type, so a new model needs a matching policy and re-embedded items. The container vector policy fixes dimensions, distance function, and index type, so a model change requires a new policy. Mismatched dimensions fail at write time. Local study-map skill 2.4 (Cosmos DB Vector Search and Embeddings), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Cosmos DB and PostgreSQL vector documentation: https://learn.microsoft.com/en-us/azure/cosmos-db/

- **A:** Incorrect for this question. HNSW gives fast approximate nearest-neighbour queries with a larger memory footprint and slower builds. Recall is tunable at query time. Why the correct answer wins: The container vector policy declares dimensions and index type, so a new model needs a matching policy and re-embedded items.
- **B:** Incorrect for this question. Distance function choice must match the embedding model and the normalization used at indexing time. A mismatch degrades recall silently. Why the correct answer wins: The container vector policy declares dimensions and index type, so a new model needs a matching policy and re-embedded items.
- **C:** Incorrect for this question. Cosmos DB for NoSQL supports vector properties and a distance function for similarity search in the same document store. Dimensions and index type must match the model. Why the correct answer wins: The container vector policy declares dimensions and index type, so a new model needs a matching policy and re-embedded items.
- **D:** Correct. The container vector policy fixes dimensions, distance function, and index type, so a model change requires a new policy. Mismatched dimensions fail at write time. In this case: The container vector policy declares dimensions and index type, so a new model needs a matching policy and re-embedded items.

### Question 61 — A

Answer: Match the vector index type and dimensions to the embedding model. The declared index type and dimensions must match the embedding model, or similarity results degrade silently. The container vector policy is fixed at creation, so a model or dimension change needs a new container and a re-index. Local study-map skill 2.4 (Cosmos DB Vector Search and Embeddings), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Cosmos DB and PostgreSQL vector documentation: https://learn.microsoft.com/en-us/azure/cosmos-db/

- **A:** Correct. The container vector policy is fixed at creation, so a model or dimension change needs a new container and a re-index. In this case: The declared index type and dimensions must match the embedding model, or similarity results degrade silently.
- **B:** Incorrect for this question. Cosmos DB for NoSQL supports vector properties and a distance function for similarity search in the same document store. Dimensions and index type must match the model. Why the correct answer wins: The declared index type and dimensions must match the embedding model, or similarity results degrade silently.
- **C:** Incorrect for this question. Distance function choice must match the embedding model and the normalization used at indexing time. A mismatch degrades recall silently. Why the correct answer wins: The declared index type and dimensions must match the embedding model, or similarity results degrade silently.
- **D:** Incorrect for this question. DiskANN trades some recall for memory efficiency on large sets. Recall and latency should be measured on representative queries. Why the correct answer wins: The declared index type and dimensions must match the embedding model, or similarity results degrade silently.

### Question 62 — D

Answer: Run a change feed processor to react to new and updated items. A change feed processor streams inserts and updates in order per partition and pushes them to the indexer. The change feed delivers an ordered stream of changes per partition for downstream processing. It is not a delete feed, so deletions need a workaround. Local study-map skill 2.5 (Cosmos DB Change Feed Processing), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Cosmos DB and PostgreSQL vector documentation: https://learn.microsoft.com/en-us/azure/cosmos-db/

- **A:** Incorrect for this question. Item TTL expires documents automatically, which controls storage growth and data retention. It does not archive the expired content. Why the correct answer wins: A change feed processor streams inserts and updates in order per partition and pushes them to the indexer.
- **B:** Incorrect for this question. A duplicate-detection window drops repeated sends within the window, which helps with at-least-once producers. The window is time-bounded. Why the correct answer wins: A change feed processor streams inserts and updates in order per partition and pushes them to the indexer.
- **C:** Incorrect for this question. Leases track partition ownership so multiple processor instances share work and resume from a continuation token. Lease writes consume RUs too. Why the correct answer wins: A change feed processor streams inserts and updates in order per partition and pushes them to the indexer.
- **D:** Correct. The change feed delivers an ordered stream of changes per partition for downstream processing. It is not a delete feed, so deletions need a workaround. In this case: A change feed processor streams inserts and updates in order per partition and pushes them to the indexer.

### Question 63 — C

Answer: Model typed columns for filters and one vector column for the embedding. Typed columns for market and language beside one vector column keep predicates indexable and the contract explicit. Explicit types keep filters fast and make the embedding contract clear. Storing vectors as text defeats index use. Local study-map skill 2.6 (PostgreSQL Connection and Schema Modeling), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Cosmos DB and PostgreSQL vector documentation: https://learn.microsoft.com/en-us/azure/cosmos-db/

- **A:** Incorrect for this question. Vector indexes are memory-hungry, so undersized compute causes swapping and slow queries. Right-size before tuning index parameters. Why the correct answer wins: Typed columns for market and language beside one vector column keep predicates indexable and the contract explicit.
- **B:** Incorrect for this question. Index creation and bulk loads are I/O heavy, and throttled storage stretches maintenance windows. Storage limits are separate from compute. Why the correct answer wins: Typed columns for market and language beside one vector column keep predicates indexable and the contract explicit.
- **C:** Correct. Explicit types keep filters fast and make the embedding contract clear. Storing vectors as text defeats index use. In this case: Typed columns for market and language beside one vector column keep predicates indexable and the contract explicit.
- **D:** Incorrect for this question. A replica offloads read traffic but introduces replication lag, which is dangerous for freshly written evidence. It does not reduce index memory pressure. Why the correct answer wins: Typed columns for market and language beside one vector column keep predicates indexable and the contract explicit.

### Question 64 — B

Answer: Place a connection pooler in front of PostgreSQL for many short-lived clients. An external pooler multiplexes short-lived clients onto a small number of server connections. An external pooler multiplexes server connections for serverless or highly concurrent clients. Session-level features may be unavailable in transaction mode. Local study-map skill 2.10 (PostgreSQL Connection Optimization), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Cosmos DB and PostgreSQL vector documentation: https://learn.microsoft.com/en-us/azure/cosmos-db/

- **A:** Incorrect for this question. Index creation and bulk loads are I/O heavy, and throttled storage stretches maintenance windows. Storage limits are separate from compute. Why the correct answer wins: An external pooler multiplexes short-lived clients onto a small number of server connections.
- **B:** Correct. An external pooler multiplexes server connections for serverless or highly concurrent clients. Session-level features may be unavailable in transaction mode. In this case: An external pooler multiplexes short-lived clients onto a small number of server connections.
- **C:** Incorrect for this question. Prepared statements avoid repeated planning and reduce chatty network calls. They pair well with pooling but can interact with pool modes. Why the correct answer wins: An external pooler multiplexes short-lived clients onto a small number of server connections.
- **D:** Incorrect for this question. A bounded pool amortizes connection setup and protects the server from connection storms. Pool size must match server limits. Why the correct answer wins: An external pooler multiplexes short-lived clients onto a small number of server connections.

### Question 65 — C

Answer: Cache responses in Azure Managed Redis. Caching the computed block in Managed Redis stops the service from repeating identical work per request. A cache absorbs repeated reads and cuts latency for hot data. Cache keys, TTLs, and invalidation must match the freshness requirement. Local study-map skill 2.11 (Azure Managed Redis Caching and Invalidation), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Cosmos DB and PostgreSQL vector documentation: https://learn.microsoft.com/en-us/azure/cosmos-db/

- **A:** Incorrect for this question. A TTL bounds staleness and reclaims memory without a manual sweep. Too long a TTL hides source changes; too short wastes the cache. Why the correct answer wins: Caching the computed block in Managed Redis stops the service from repeating identical work per request.
- **B:** Incorrect for this question. A replica offloads read traffic but introduces replication lag, which is dangerous for freshly written evidence. It does not reduce index memory pressure. Why the correct answer wins: Caching the computed block in Managed Redis stops the service from repeating identical work per request.
- **C:** Correct. A cache absorbs repeated reads and cuts latency for hot data. Cache keys, TTLs, and invalidation must match the freshness requirement. In this case: Caching the computed block in Managed Redis stops the service from repeating identical work per request.
- **D:** Incorrect for this question. Queue Storage is simple and cheap for large backlogs with at-least-once delivery. It lacks topics, sessions, and scheduled messages. Why the correct answer wins: Caching the computed block in Managed Redis stops the service from repeating identical work per request.

### Question 66 — C, D

Answers: Run a change feed processor to react to new and updated items; Use a lease container to coordinate change feed readers. The change feed supplies ordered inserts and updates, and leases coordinate ownership between processor instances. The change feed delivers an ordered stream of changes per partition for downstream processing. It is not a delete feed, so deletions need a workaround. Leases track partition ownership so multiple processor instances share work and resume from a continuation token. Lease writes consume RUs too. Local study-map skill 2.5 (Cosmos DB Change Feed Processing), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Cosmos DB and PostgreSQL vector documentation: https://learn.microsoft.com/en-us/azure/cosmos-db/

- **A:** Incorrect for this question. A duplicate-detection window drops repeated sends within the window, which helps with at-least-once producers. The window is time-bounded. Why the correct answer wins: The change feed supplies ordered inserts and updates, and leases coordinate ownership between processor instances.
- **B:** Incorrect for this question. Item TTL expires documents automatically, which controls storage growth and data retention. It does not archive the expired content. Why the correct answer wins: The change feed supplies ordered inserts and updates, and leases coordinate ownership between processor instances.
- **C:** Correct. Leases track partition ownership so multiple processor instances share work and resume from a continuation token. Lease writes consume RUs too. In this case: The change feed supplies ordered inserts and updates, and leases coordinate ownership between processor instances.
- **D:** Correct. The change feed delivers an ordered stream of changes per partition for downstream processing. It is not a delete feed, so deletions need a workaround. In this case: The change feed supplies ordered inserts and updates, and leases coordinate ownership between processor instances.
- **E:** Incorrect for this question. Indexing everything is simple and makes ad hoc queries possible, at higher write cost and storage. It is a default, not an optimization. Why the correct answer wins: The change feed supplies ordered inserts and updates, and leases coordinate ownership between processor instances.

### Question 67 — A, D

Answers: Store embeddings in a vector property and query with VectorDistance; Use the cosine distance function that matches how the embeddings were trained. A vector property keeps embeddings beside the metadata, and the matching distance function preserves ranking quality. Cosmos DB for NoSQL supports vector properties and a distance function for similarity search in the same document store. Dimensions and index type must match the model. Distance function choice must match the embedding model and the normalization used at indexing time. A mismatch degrades recall silently. Local study-map skill 2.4 (Cosmos DB Vector Search and Embeddings), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Cosmos DB and PostgreSQL vector documentation: https://learn.microsoft.com/en-us/azure/cosmos-db/

- **A:** Correct. Cosmos DB for NoSQL supports vector properties and a distance function for similarity search in the same document store. Dimensions and index type must match the model. In this case: A vector property keeps embeddings beside the metadata, and the matching distance function preserves ranking quality.
- **B:** Incorrect for this question. pgvector keeps vectors beside relational data, so filters and joins run in one query. Index type and parameter tuning decide latency. Why the correct answer wins: A vector property keeps embeddings beside the metadata, and the matching distance function preserves ranking quality.
- **C:** Incorrect for this question. Application-side scoring works for tiny collections and tests, but it moves all data over the wire and does not scale with corpus size. Why the correct answer wins: A vector property keeps embeddings beside the metadata, and the matching distance function preserves ranking quality.
- **D:** Correct. Distance function choice must match the embedding model and the normalization used at indexing time. A mismatch degrades recall silently. In this case: A vector property keeps embeddings beside the metadata, and the matching distance function preserves ranking quality.
- **E:** Incorrect for this question. DiskANN trades some recall for memory efficiency on large sets. Recall and latency should be measured on representative queries. Why the correct answer wins: A vector property keeps embeddings beside the metadata, and the matching distance function preserves ranking quality.

### Question 68 — D

Answer: Create the container with a vector policy → upsert items with embeddings → query with VectorDistance → apply metadata filters. The container policy precedes upserts, upserts precede queries, and metadata filters are applied with the search. The vector policy fixes dimensions and index type, so it must exist before vector writes and queries. Local study-map skill 2.5 (Cosmos DB Change Feed Processing), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Cosmos DB and PostgreSQL vector documentation: https://learn.microsoft.com/en-us/azure/cosmos-db/

- **A:** Incorrect for this question. Items cannot be written before the container exists with a matching vector policy. Why the correct answer wins: The container policy precedes upserts, upserts precede queries, and metadata filters are applied with the search.
- **B:** Incorrect for this question. Filtering and querying cannot precede the container and its vector data. Why the correct answer wins: The container policy precedes upserts, upserts precede queries, and metadata filters are applied with the search.
- **C:** Incorrect for this question. A similarity query needs indexed vectors, which require the container and its policy first. Why the correct answer wins: The container policy precedes upserts, upserts precede queries, and metadata filters are applied with the search.
- **D:** Correct. The vector policy fixes dimensions and index type, so it must exist before vector writes and queries. In this case: The container policy precedes upserts, upserts precede queries, and metadata filters are applied with the search.

### Question 69 — A

Answer: Use Service Bus sessions to keep related messages ordered. Sessions give exclusive, ordered processing per order identifier across competing consumers. Sessions give ordered, exclusive processing per session ID across competing consumers. They require session-aware senders and receivers. Local study-map skill 3.1 (Service Bus Queues and Sessions), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure messaging and Functions documentation: https://learn.microsoft.com/en-us/azure/service-bus-messaging/

- **A:** Correct. Sessions give ordered, exclusive processing per session ID across competing consumers. They require session-aware senders and receivers. In this case: Sessions give exclusive, ordered processing per order identifier across competing consumers.
- **B:** Incorrect for this question. Peek-lock keeps the message locked until the handler completes it, giving at-least-once processing with retry. Lock duration must exceed processing time. Why the correct answer wins: Sessions give exclusive, ordered processing per order identifier across competing consumers.
- **C:** Incorrect for this question. A delivery cap stops infinite retries of a failing message and moves it to the dead-letter queue. The cap must exceed legitimate transient retries. Why the correct answer wins: Sessions give exclusive, ordered processing per order identifier across competing consumers.
- **D:** Incorrect for this question. A duplicate-detection window drops repeated sends within the window, which helps with at-least-once producers. The window is time-bounded. Why the correct answer wins: Sessions give exclusive, ordered processing per order identifier across competing consumers.

### Question 70 — B

Answer: Inspect the dead-letter queue and resubmit corrected messages. The dead-letter queue holds messages that exhausted delivery attempts so they can be examined and resubmitted. Dead-lettering preserves poison messages for diagnosis instead of losing them. Resubmission needs a fix and an idempotent handler. Local study-map skill 3.3 (Service Bus Dead-Lettering and Retries), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure messaging and Functions documentation: https://learn.microsoft.com/en-us/azure/service-bus-messaging/

- **A:** Incorrect for this question. Receive-and-delete removes the message on delivery, so a crash loses work silently. It suits telemetry, not payments. Why the correct answer wins: The dead-letter queue holds messages that exhausted delivery attempts so they can be examined and resubmitted.
- **B:** Correct. Dead-lettering preserves poison messages for diagnosis instead of losing them. Resubmission needs a fix and an idempotent handler. In this case: The dead-letter queue holds messages that exhausted delivery attempts so they can be examined and resubmitted.
- **C:** Incorrect for this question. A duplicate-detection window drops repeated sends within the window, which helps with at-least-once producers. The window is time-bounded. Why the correct answer wins: The dead-letter queue holds messages that exhausted delivery attempts so they can be examined and resubmitted.
- **D:** Incorrect for this question. Prepared statements avoid repeated planning and reduce chatty network calls. They pair well with pooling but can interact with pool modes. Why the correct answer wins: The dead-letter queue holds messages that exhausted delivery attempts so they can be examined and resubmitted.

### Question 71 — B

Answer: Subscribe to a system topic for resource events. A system topic carries events that the storage service publishes itself, so no custom publisher is needed. System topics carry Azure resource lifecycle events. Domain events that are not resource changes need a custom topic and schema. Local study-map skill 3.4 (Event Grid Filters, Custom Events, and Retries), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure messaging and Functions documentation: https://learn.microsoft.com/en-us/azure/service-bus-messaging/

- **A:** Incorrect for this question. Event Grid retries failed deliveries with backoff and can store undeliverable events. Handlers must still be idempotent. Why the correct answer wins: A system topic carries events that the storage service publishes itself, so no custom publisher is needed.
- **B:** Correct. System topics carry Azure resource lifecycle events. Domain events that are not resource changes need a custom topic and schema. In this case: A system topic carries events that the storage service publishes itself, so no custom publisher is needed.
- **C:** Incorrect for this question. A custom schema fits domain events that are not resource lifecycle notifications. Consumers must version the schema contract. Why the correct answer wins: A system topic carries events that the storage service publishes itself, so no custom publisher is needed.
- **D:** Incorrect for this question. Event Hubs ingests high-volume ordered streams with partitions and consumer groups. It is a streaming log, not a task queue. Why the correct answer wins: A system topic carries events that the storage service publishes itself, so no custom publisher is needed.

### Question 72 — A

Answer: Deliver events by using a managed identity instead of a key. Delivering events with a managed identity removes the shared key from the subscription configuration. Identity-based delivery removes a shared key from the subscription. The receiver still validates the caller and payload. Local study-map skill 3.4 (Event Grid Filters, Custom Events, and Retries), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure messaging and Functions documentation: https://learn.microsoft.com/en-us/azure/service-bus-messaging/

- **A:** Correct. Identity-based delivery removes a shared key from the subscription. The receiver still validates the caller and payload. In this case: Delivering events with a managed identity removes the shared key from the subscription configuration.
- **B:** Incorrect for this question. A custom schema fits domain events that are not resource lifecycle notifications. Consumers must version the schema contract. Why the correct answer wins: Delivering events with a managed identity removes the shared key from the subscription configuration.
- **C:** Incorrect for this question. Event Grid retries failed deliveries with backoff and can store undeliverable events. Handlers must still be idempotent. Why the correct answer wins: Delivering events with a managed identity removes the shared key from the subscription configuration.
- **D:** Incorrect for this question. Event Hubs ingests high-volume ordered streams with partitions and consumer groups. It is a streaming log, not a task queue. Why the correct answer wins: Delivering events with a managed identity removes the shared key from the subscription configuration.

### Question 73 — A

Answer: Use input and output bindings instead of hand-written SDK calls. An output binding lets the runtime write to the store without client construction or connection handling. Bindings reduce boilerplate for common inputs and outputs and are configured declaratively. Complex operations still need the SDK. Local study-map skill 3.5 (Azure Functions Triggers and Bindings), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure messaging and Functions documentation: https://learn.microsoft.com/en-us/azure/service-bus-messaging/

- **A:** Correct. Bindings reduce boilerplate for common inputs and outputs and are configured declaratively. Complex operations still need the SDK. In this case: An output binding lets the runtime write to the store without client construction or connection handling.
- **B:** Incorrect for this question. Durable Functions provides orchestrations, activities, timers, and retries with checkpointed state. Orchestrator code must stay deterministic. Why the correct answer wins: An output binding lets the runtime write to the store without client construction or connection handling.
- **C:** Incorrect for this question. An HTTP trigger gives a synchronous API endpoint with route and authorization configuration. Long-running work should hand off to a queue. Why the correct answer wins: An output binding lets the runtime write to the store without client construction or connection handling.
- **D:** Incorrect for this question. A trigger starts the function when work arrives and handles the receive loop for you. Poison-message behavior is configured in host settings. Why the correct answer wins: An output binding lets the runtime write to the store without client construction or connection handling.

### Question 74 — A

Answer: Host the function app on a premium plan with pre-warmed instances. A premium plan provides pre-warmed instances and virtual network integration for private endpoints. A premium plan reduces cold starts and supports virtual network integration and longer timeouts. It costs more than consumption. Local study-map skill 3.6 (Function App Configuration and Deployment), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure messaging and Functions documentation: https://learn.microsoft.com/en-us/azure/service-bus-messaging/

- **A:** Correct. A premium plan reduces cold starts and supports virtual network integration and longer timeouts. It costs more than consumption. In this case: A premium plan provides pre-warmed instances and virtual network integration for private endpoints.
- **B:** Incorrect for this question. Durable Functions provides orchestrations, activities, timers, and retries with checkpointed state. Orchestrator code must stay deterministic. Why the correct answer wins: A premium plan provides pre-warmed instances and virtual network integration for private endpoints.
- **C:** Incorrect for this question. An HTTP trigger gives a synchronous API endpoint with route and authorization configuration. Long-running work should hand off to a queue. Why the correct answer wins: A premium plan provides pre-warmed instances and virtual network integration for private endpoints.
- **D:** Incorrect for this question. Consumption bills per execution and scales automatically, with cold starts and a timeout ceiling. It fits spiky, short work. Why the correct answer wins: A premium plan provides pre-warmed instances and virtual network integration for private endpoints.

### Question 75 — A

Answer: Configure the host retry policy with exponential backoff. A host retry policy with exponential backoff spaces attempts so the dependency can recover. The host retry policy re-executes a failing trigger with bounded attempts and backoff. It cannot make a non-idempotent handler safe to replay. Local study-map skill 3.6 (Function App Configuration and Deployment), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure messaging and Functions documentation: https://learn.microsoft.com/en-us/azure/service-bus-messaging/

- **A:** Correct. The host retry policy re-executes a failing trigger with bounded attempts and backoff. It cannot make a non-idempotent handler safe to replay. In this case: A host retry policy with exponential backoff spaces attempts so the dependency can recover.
- **B:** Incorrect for this question. A premium plan reduces cold starts and supports virtual network integration and longer timeouts. It costs more than consumption. Why the correct answer wins: A host retry policy with exponential backoff spaces attempts so the dependency can recover.
- **C:** Incorrect for this question. Concurrency and batch size bound how much work one instance takes at a time, which controls downstream pressure and memory. Too high a value causes throttling and timeouts. Why the correct answer wins: A host retry policy with exponential backoff spaces attempts so the dependency can recover.
- **D:** Incorrect for this question. Pipeline deployment keeps code and configuration versioned together and repeatable. Secrets belong in a vault reference, not in the pipeline file. Why the correct answer wins: A host retry policy with exponential backoff spaces attempts so the dependency can recover.

### Question 76 — B, E

Answers: Publish to a Service Bus topic with multiple subscriptions; Add a SQL or correlation filter to a subscription. A topic with separate subscriptions fans out the event, and a subscription filter limits loyalty to matching changes. Topics fan out one message to independent subscribers, each with its own filter and dead-letter queue. Subscribers process at their own pace. Subscription filters route only matching messages to a handler, reducing wasted processing. Filter evaluation happens broker-side on message properties. Local study-map skill 3.2 (Service Bus Topics, Subscriptions, and Filters), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure messaging and Functions documentation: https://learn.microsoft.com/en-us/azure/service-bus-messaging/

- **A:** Incorrect for this question. A queue decouples producers from a single consumer group and smooths bursts. Delivery semantics depend on receive mode and completion. Why the correct answer wins: A topic with separate subscriptions fans out the event, and a subscription filter limits loyalty to matching changes.
- **B:** Correct. Topics fan out one message to independent subscribers, each with its own filter and dead-letter queue. Subscribers process at their own pace. In this case: A topic with separate subscriptions fans out the event, and a subscription filter limits loyalty to matching changes.
- **C:** Incorrect for this question. Subject and event-type filters keep handlers focused and reduce cost. Filters are evaluated on event metadata, not payload body. Why the correct answer wins: A topic with separate subscriptions fans out the event, and a subscription filter limits loyalty to matching changes.
- **D:** Incorrect for this question. Queue Storage is simple and cheap for large backlogs with at-least-once delivery. It lacks topics, sessions, and scheduled messages. Why the correct answer wins: A topic with separate subscriptions fans out the event, and a subscription filter limits loyalty to matching changes.
- **E:** Correct. Subscription filters route only matching messages to a handler, reducing wasted processing. Filter evaluation happens broker-side on message properties. In this case: A topic with separate subscriptions fans out the event, and a subscription filter limits loyalty to matching changes.

### Question 77 — B, C

Answers: Set a maximum delivery count and handle the dead-letter path; Inspect the dead-letter queue and resubmit corrected messages. A delivery cap ends the retry loop, and dead-lettering preserves the message for later inspection. A delivery cap stops infinite retries of a failing message and moves it to the dead-letter queue. The cap must exceed legitimate transient retries. Dead-lettering preserves poison messages for diagnosis instead of losing them. Resubmission needs a fix and an idempotent handler. Local study-map skill 3.3 (Service Bus Dead-Lettering and Retries), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure messaging and Functions documentation: https://learn.microsoft.com/en-us/azure/service-bus-messaging/

- **A:** Incorrect for this question. Peek-lock keeps the message locked until the handler completes it, giving at-least-once processing with retry. Lock duration must exceed processing time. Why the correct answer wins: A delivery cap ends the retry loop, and dead-lettering preserves the message for later inspection.
- **B:** Correct. Dead-lettering preserves poison messages for diagnosis instead of losing them. Resubmission needs a fix and an idempotent handler. In this case: A delivery cap ends the retry loop, and dead-lettering preserves the message for later inspection.
- **C:** Correct. A delivery cap stops infinite retries of a failing message and moves it to the dead-letter queue. The cap must exceed legitimate transient retries. In this case: A delivery cap ends the retry loop, and dead-lettering preserves the message for later inspection.
- **D:** Incorrect for this question. Receive-and-delete removes the message on delivery, so a crash loses work silently. It suits telemetry, not payments. Why the correct answer wins: A delivery cap ends the retry loop, and dead-lettering preserves the message for later inspection.
- **E:** Incorrect for this question. A duplicate-detection window drops repeated sends within the window, which helps with at-least-once producers. The window is time-bounded. Why the correct answer wins: A delivery cap ends the retry loop, and dead-lettering preserves the message for later inspection.

### Question 78 — C

Answer: Publish a custom event → evaluate the subscription filter → deliver to the handler → retry on failure → dead-letter undeliverable events. Publication precedes subscription filtering, delivery precedes retries, and dead-lettering follows exhausted attempts. Filtering happens before delivery, retries handle transient failures, and dead-lettering preserves what cannot be delivered. Local study-map skill 3.4 (Event Grid Filters, Custom Events, and Retries), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure messaging and Functions documentation: https://learn.microsoft.com/en-us/azure/service-bus-messaging/

- **A:** Incorrect for this question. A filter cannot evaluate an event that has not been published. Why the correct answer wins: Publication precedes subscription filtering, delivery precedes retries, and dead-lettering follows exhausted attempts.
- **B:** Incorrect for this question. A filter is evaluated before delivery, and retries must occur before dead-lettering. Why the correct answer wins: Publication precedes subscription filtering, delivery precedes retries, and dead-lettering follows exhausted attempts.
- **C:** Correct. Filtering happens before delivery, retries handle transient failures, and dead-lettering preserves what cannot be delivered. In this case: Publication precedes subscription filtering, delivery precedes retries, and dead-lettering follows exhausted attempts.
- **D:** Incorrect for this question. Delivery cannot precede publication and filtering. Why the correct answer wins: Publication precedes subscription filtering, delivery precedes retries, and dead-lettering follows exhausted attempts.

### Question 79 — D

Answer: Store the secret in Azure Key Vault and read it at runtime. Key Vault stores the key with version history and audit logging, and the app reads it at runtime. A vault centralizes secret storage with access control and audit. Retrieval should use an identity, not a copied credential. Local study-map skill 4.1 (Key Vault Secret Storage, Rotation, and Retrieval), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Key Vault, App Configuration, and Monitor documentation: https://learn.microsoft.com/en-us/azure/azure-monitor/

- **A:** Incorrect for this question. A scoped role grants only the operations the app performs and limits blast radius. Prefer built-in roles over broad contributor grants. Why the correct answer wins: Key Vault stores the key with version history and audit logging, and the app reads it at runtime.
- **B:** Incorrect for this question. A Key Vault reference resolves at runtime so the secret is never written into application settings. The app identity still needs permission to read it. Why the correct answer wins: Key Vault stores the key with version history and audit logging, and the app reads it at runtime.
- **C:** Incorrect for this question. App Configuration separates configuration from code and supports labels, feature flags, and Key Vault references. Change still needs a refresh strategy. Why the correct answer wins: Key Vault stores the key with version history and audit logging, and the app reads it at runtime.
- **D:** Correct. A vault centralizes secret storage with access control and audit. Retrieval should use an identity, not a copied credential. In this case: Key Vault stores the key with version history and audit logging, and the app reads it at runtime.

### Question 80 — C

Answer: Enable purge protection and soft delete on the vault. Soft delete with purge protection keeps a deleted vault recoverable for the retention period. Soft delete and purge protection stop accidental or malicious permanent loss of secrets. They also constrain how names can be reused. Local study-map skill 4.1 (Key Vault Secret Storage, Rotation, and Retrieval), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Key Vault, App Configuration, and Monitor documentation: https://learn.microsoft.com/en-us/azure/azure-monitor/

- **A:** Incorrect for this question. Rotation limits the value of a leaked secret, but callers must read the latest version rather than caching an old one forever. Why the correct answer wins: Soft delete with purge protection keeps a deleted vault recoverable for the retention period.
- **B:** Incorrect for this question. A vault centralizes secret storage with access control and audit. Retrieval should use an identity, not a copied credential. Why the correct answer wins: Soft delete with purge protection keeps a deleted vault recoverable for the retention period.
- **C:** Correct. Soft delete and purge protection stop accidental or malicious permanent loss of secrets. They also constrain how names can be reused. In this case: Soft delete with purge protection keeps a deleted vault recoverable for the retention period.
- **D:** Incorrect for this question. Vault access is a separate authorization decision from the app identity. Without a data-plane role or policy the reference fails at runtime. Why the correct answer wins: Soft delete with purge protection keeps a deleted vault recoverable for the retention period.

### Question 81 — C

Answer: Store settings and feature flags in Azure App Configuration. App Configuration centralizes settings and flags, and labels keep market-specific values apart. App Configuration separates configuration from code and supports labels, feature flags, and Key Vault references. Change still needs a refresh strategy. Local study-map skill 4.2 (App Configuration Settings and Feature Flags), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Key Vault, App Configuration, and Monitor documentation: https://learn.microsoft.com/en-us/azure/azure-monitor/

- **A:** Incorrect for this question. Sentinel-key or polling refresh lets a running app pick up new settings. Refresh intervals trade responsiveness against request volume. Why the correct answer wins: App Configuration centralizes settings and flags, and labels keep market-specific values apart.
- **B:** Incorrect for this question. A Key Vault reference keeps non-secret settings in App Configuration while the value stays in the vault. The app identity needs both sets of permissions. Why the correct answer wins: App Configuration centralizes settings and flags, and labels keep market-specific values apart.
- **C:** Correct. App Configuration separates configuration from code and supports labels, feature flags, and Key Vault references. Change still needs a refresh strategy. In this case: App Configuration centralizes settings and flags, and labels keep market-specific values apart.
- **D:** Incorrect for this question. Labels keep dev, test, and prod values in one store with one key schema. A misconfigured label selector silently serves the wrong values. Why the correct answer wins: App Configuration centralizes settings and flags, and labels keep market-specific values apart.

### Question 82 — D

Answer: Correlate logs with the operation or trace identifier. Emitting the operation or trace identifier in logs makes the two telemetry types joinable. Including the trace ID in log records lets you pivot from a failed span to its log lines. Without it, logs and traces are separate worlds. Local study-map skill 4.3 (Distributed Tracing with OpenTelemetry), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Key Vault, App Configuration, and Monitor documentation: https://learn.microsoft.com/en-us/azure/azure-monitor/

- **A:** Incorrect for this question. Propagation stitches one trace across HTTP, messaging, and Functions so the whole path is visible. Missing propagation breaks the trace at that hop. Why the correct answer wins: Emitting the operation or trace identifier in logs makes the two telemetry types joinable.
- **B:** Incorrect for this question. OpenTelemetry emits vendor-neutral traces, metrics, and logs with context propagation. Exporters and sampling decide what reaches the backend. Why the correct answer wins: Emitting the operation or trace identifier in logs makes the two telemetry types joinable.
- **C:** Incorrect for this question. KQL filters, projects, and aggregates log and metric tables in Log Analytics. Start narrow with a time range and a request ID. Why the correct answer wins: Emitting the operation or trace identifier in logs makes the two telemetry types joinable.
- **D:** Correct. Including the trace ID in log records lets you pivot from a failed span to its log lines. Without it, logs and traces are separate worlds. In this case: Emitting the operation or trace identifier in logs makes the two telemetry types joinable.

### Question 83 — B

Answer: Use head or tail sampling so trace volume stays within budget. Sampling keeps volume within budget, and tail sampling retains failed and slow traces regardless. Sampling keeps telemetry cost bounded, but aggressive sampling can hide rare failures. Tail sampling can retain errors preferentially. Local study-map skill 4.3 (Distributed Tracing with OpenTelemetry), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Key Vault, App Configuration, and Monitor documentation: https://learn.microsoft.com/en-us/azure/azure-monitor/

- **A:** Incorrect for this question. A span records the duration and outcome of one operation and nests under the trace. It makes the slow dependency visible in the transaction view. Why the correct answer wins: Sampling keeps volume within budget, and tail sampling retains failed and slow traces regardless.
- **B:** Correct. Sampling keeps telemetry cost bounded, but aggressive sampling can hide rare failures. Tail sampling can retain errors preferentially. In this case: Sampling keeps volume within budget, and tail sampling retains failed and slow traces regardless.
- **C:** Incorrect for this question. A collector batches, filters, and routes telemetry, and decouples app configuration from the backend. It is another component to run and monitor. Why the correct answer wins: Sampling keeps volume within budget, and tail sampling retains failed and slow traces regardless.
- **D:** Incorrect for this question. Propagation stitches one trace across HTTP, messaging, and Functions so the whole path is visible. Missing propagation breaks the trace at that hop. Why the correct answer wins: Sampling keeps volume within budget, and tail sampling retains failed and slow traces regardless.

### Question 84 — A

Answer: Assign a least-privilege role to the application identity. A least-privilege role scoped to the resources in use replaces the broad subscription assignment. A scoped role grants only the operations the app performs and limits blast radius. Prefer built-in roles over broad contributor grants. Local study-map skill 4.5 (Identity-Based Access for Application Services), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Key Vault, App Configuration, and Monitor documentation: https://learn.microsoft.com/en-us/azure/azure-monitor/

- **A:** Correct. A scoped role grants only the operations the app performs and limits blast radius. Prefer built-in roles over broad contributor grants. In this case: A least-privilege role scoped to the resources in use replaces the broad subscription assignment.
- **B:** Incorrect for this question. Soft delete and purge protection stop accidental or malicious permanent loss of secrets. They also constrain how names can be reused. Why the correct answer wins: A least-privilege role scoped to the resources in use replaces the broad subscription assignment.
- **C:** Incorrect for this question. Workload identity lets pods obtain tokens without stored secrets. Each workload should get its own identity and narrow role. Why the correct answer wins: A least-privilege role scoped to the resources in use replaces the broad subscription assignment.
- **D:** Incorrect for this question. A private endpoint keeps traffic on the virtual network and removes public exposure. DNS resolution must be wired to the private zone. Why the correct answer wins: A least-privilege role scoped to the resources in use replaces the broad subscription assignment.

### Question 85 — B, C

Answers: Grant the app identity data-plane access to the vault; Rotate the secret on a schedule and let apps resolve the current version. A data-plane role lets the identity read the secret, and rotation issues new versions the app resolves automatically. Vault access is a separate authorization decision from the app identity. Without a data-plane role or policy the reference fails at runtime. Rotation limits the value of a leaked secret, but callers must read the latest version rather than caching an old one forever. Local study-map skill 4.1 (Key Vault Secret Storage, Rotation, and Retrieval), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Key Vault, App Configuration, and Monitor documentation: https://learn.microsoft.com/en-us/azure/azure-monitor/

- **A:** Incorrect for this question. Pinning a version makes a rotation invisible to the app until it is redeployed, which is useful for break-glass and dangerous for routine rotation. Why the correct answer wins: A data-plane role lets the identity read the secret, and rotation issues new versions the app resolves automatically.
- **B:** Correct. Rotation limits the value of a leaked secret, but callers must read the latest version rather than caching an old one forever. In this case: A data-plane role lets the identity read the secret, and rotation issues new versions the app resolves automatically.
- **C:** Correct. Vault access is a separate authorization decision from the app identity. Without a data-plane role or policy the reference fails at runtime. In this case: A data-plane role lets the identity read the secret, and rotation issues new versions the app resolves automatically.
- **D:** Incorrect for this question. A Key Vault reference resolves at runtime so the secret is never written into application settings. The app identity still needs permission to read it. Why the correct answer wins: A data-plane role lets the identity read the secret, and rotation issues new versions the app resolves automatically.
- **E:** Incorrect for this question. App Configuration separates configuration from code and supports labels, feature flags, and Key Vault references. Change still needs a refresh strategy. Why the correct answer wins: A data-plane role lets the identity read the secret, and rotation issues new versions the app resolves automatically.

### Question 86 — C, D

Answers: Enable configuration refresh so changes apply without a restart; Ship the code dark behind a feature flag. A feature flag enables the code dark, and refresh delivers the changed value to running instances. Sentinel-key or polling refresh lets a running app pick up new settings. Refresh intervals trade responsiveness against request volume. A feature flag enables reviewed code in production without a redeploy and lets it be switched off instantly. Flag state still needs ownership and cleanup. Local study-map skill 4.2 (App Configuration Settings and Feature Flags), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Key Vault, App Configuration, and Monitor documentation: https://learn.microsoft.com/en-us/azure/azure-monitor/

- **A:** Incorrect for this question. Pinning a version makes a rotation invisible to the app until it is redeployed, which is useful for break-glass and dangerous for routine rotation. Why the correct answer wins: A feature flag enables the code dark, and refresh delivers the changed value to running instances.
- **B:** Incorrect for this question. Labels keep dev, test, and prod values in one store with one key schema. A misconfigured label selector silently serves the wrong values. Why the correct answer wins: A feature flag enables the code dark, and refresh delivers the changed value to running instances.
- **C:** Correct. A feature flag enables reviewed code in production without a redeploy and lets it be switched off instantly. Flag state still needs ownership and cleanup. In this case: A feature flag enables the code dark, and refresh delivers the changed value to running instances.
- **D:** Correct. Sentinel-key or polling refresh lets a running app pick up new settings. Refresh intervals trade responsiveness against request volume. In this case: A feature flag enables the code dark, and refresh delivers the changed value to running instances.
- **E:** Incorrect for this question. A Key Vault reference keeps non-secret settings in App Configuration while the value stays in the vault. The app identity needs both sets of permissions. Why the correct answer wins: A feature flag enables the code dark, and refresh delivers the changed value to running instances.

### Question 87 — A, E

Answers: Aggregate with summarize and bin to see the failure rate over time; Create an alert rule on the failure rate or latency metric. summarize with bin produces the per-bucket rate, and an alert rule pages on-call when it crosses the threshold. Time-binned aggregation reveals the shape of an incident: a step change, a ramp, or a periodic spike. Averages alone hide short outages. An alert turns a threshold breach into a notification or action. Thresholds need a baseline, or the alert is noise. Local study-map skill 4.4 (KQL Queries for Logs and Metrics), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Key Vault, App Configuration, and Monitor documentation: https://learn.microsoft.com/en-us/azure/azure-monitor/

- **A:** Correct. Time-binned aggregation reveals the shape of an incident: a step change, a ramp, or a periodic spike. Averages alone hide short outages. In this case: summarize with bin produces the per-bucket rate, and an alert rule pages on-call when it crosses the threshold.
- **B:** Incorrect for this question. Retention and the table plan determine how long data is queryable and what it costs. Lower retention reduces cost but shortens the investigation window. Why the correct answer wins: summarize with bin produces the per-bucket rate, and an alert rule pages on-call when it crosses the threshold.
- **C:** Incorrect for this question. Precomputed results avoid recomputing expensive aggregations on every dashboard refresh. The trade-off is storage and freshness lag. Why the correct answer wins: summarize with bin produces the per-bucket rate, and an alert rule pages on-call when it crosses the threshold.
- **D:** Incorrect for this question. Reducing columns and rows early lowers query cost and latency. Broad queries over long ranges are the usual cause of slow KQL. Why the correct answer wins: summarize with bin produces the per-bucket rate, and an alert rule pages on-call when it crosses the threshold.
- **E:** Correct. An alert turns a threshold breach into a notification or action. Thresholds need a baseline, or the alert is noise. In this case: summarize with bin produces the per-bucket rate, and an alert rule pages on-call when it crosses the threshold.

### Question 88 — A

Answer: Instrument the service with the OpenTelemetry SDK → propagate the trace context across queue hops → export spans to the collector → query the transaction view for the slow dependency → alert on the failure rate. Instrumentation precedes propagation, export precedes querying, and alerting follows a validated query. Instrumentation precedes context propagation, export precedes querying, and alerting follows a validated query. Local study-map skill 4.3 (Distributed Tracing with OpenTelemetry), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Key Vault, App Configuration, and Monitor documentation: https://learn.microsoft.com/en-us/azure/azure-monitor/

- **A:** Correct. Instrumentation precedes context propagation, export precedes querying, and alerting follows a validated query. In this case: Instrumentation precedes propagation, export precedes querying, and alerting follows a validated query.
- **B:** Incorrect for this question. Querying and alerting cannot precede instrumentation and export. Why the correct answer wins: Instrumentation precedes propagation, export precedes querying, and alerting follows a validated query.
- **C:** Incorrect for this question. An alert cannot be defined before the telemetry it depends on exists. Why the correct answer wins: Instrumentation precedes propagation, export precedes querying, and alerting follows a validated query.
- **D:** Incorrect for this question. There are no spans to export before instrumentation and propagation are in place. Why the correct answer wins: Instrumentation precedes propagation, export precedes querying, and alerting follows a validated query.

### Question 89 — B

Answer: Replicate the registry to each deployment region. Geo-replication keeps a local registry copy in each region, which shortens the pull that every new replica performs. Geo-replication reduces cross-region pull latency and gives a local copy during a regional failure. It adds cost and replication management. Local study-map skill 1.1 (Container Image Lifecycle in Azure Container Registry), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure container hosting documentation: https://learn.microsoft.com/en-us/azure/container-apps/

- **A:** Incorrect for this question. ACR keeps tagged, versioned images next to the deployment target and supports identity-based pulls. Tagging strategy and retention still need a decision. Why the correct answer wins: Geo-replication keeps a local registry copy in each region, which shortens the pull that every new replica performs.
- **B:** Correct. Geo-replication reduces cross-region pull latency and gives a local copy during a regional failure. It adds cost and replication management. In this case: Geo-replication keeps a local registry copy in each region, which shortens the pull that every new replica performs.
- **C:** Incorrect for this question. A slot swap warms the new version before it takes production traffic and makes rollback a second swap. Slot-local settings must be marked sticky. Why the correct answer wins: Geo-replication keeps a local registry copy in each region, which shortens the pull that every new replica performs.
- **D:** Incorrect for this question. ACR Tasks builds images in Azure on a commit or schedule without a local Docker host. It removes build-host drift but not image review. Why the correct answer wins: Geo-replication keeps a local registry copy in each region, which shortens the pull that every new replica performs.

### Question 90 — D

Answer: Filter on metadata columns in the same query as the vector search. Filtering on metadata in the same statement as the distance operator keeps the result scoped and complete. Combining a WHERE filter with the distance operator keeps retrieval inside the caller's scope and improves relevance. Index the filter columns too. Local study-map skill 2.9 (PostgreSQL RAG with Metadata Filters), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Cosmos DB and PostgreSQL vector documentation: https://learn.microsoft.com/en-us/azure/cosmos-db/

- **A:** Incorrect for this question. IVFFlat uses clustering lists and needs periodic rebuilds as data grows, but costs less memory than HNSW. Probes trade recall for speed. Why the correct answer wins: Filtering on metadata in the same statement as the distance operator keeps the result scoped and complete.
- **B:** Incorrect for this question. Post-filtering can return fewer results than requested and can leak existence or counts if the filtering is careless. Push authorization into the query. Why the correct answer wins: Filtering on metadata in the same statement as the distance operator keeps the result scoped and complete.
- **C:** Incorrect for this question. HNSW gives fast approximate nearest-neighbour queries with a larger memory footprint and slower builds. Recall is tunable at query time. Why the correct answer wins: Filtering on metadata in the same statement as the distance operator keeps the result scoped and complete.
- **D:** Correct. Combining a WHERE filter with the distance operator keeps retrieval inside the caller's scope and improves relevance. Index the filter columns too. In this case: Filtering on metadata in the same statement as the distance operator keeps the result scoped and complete.

### Question 91 — D

Answer: Publish to a Service Bus topic with multiple subscriptions. A topic with separate subscriptions delivers each event to every consumer and tracks each position separately. Topics fan out one message to independent subscribers, each with its own filter and dead-letter queue. Subscribers process at their own pace. Local study-map skill 3.2 (Service Bus Topics, Subscriptions, and Filters), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure messaging and Functions documentation: https://learn.microsoft.com/en-us/azure/service-bus-messaging/

- **A:** Incorrect for this question. A custom schema fits domain events that are not resource lifecycle notifications. Consumers must version the schema contract. Why the correct answer wins: A topic with separate subscriptions delivers each event to every consumer and tracks each position separately.
- **B:** Incorrect for this question. A queue decouples producers from a single consumer group and smooths bursts. Delivery semantics depend on receive mode and completion. Why the correct answer wins: A topic with separate subscriptions delivers each event to every consumer and tracks each position separately.
- **C:** Incorrect for this question. Queue Storage is simple and cheap for large backlogs with at-least-once delivery. It lacks topics, sessions, and scheduled messages. Why the correct answer wins: A topic with separate subscriptions delivers each event to every consumer and tracks each position separately.
- **D:** Correct. Topics fan out one message to independent subscribers, each with its own filter and dead-letter queue. Subscribers process at their own pace. In this case: A topic with separate subscriptions delivers each event to every consumer and tracks each position separately.

### Question 92 — A

Answer: Filter on metadata columns in the same query as the vector search. Filtering inside the vector query enforces scope and preserves result completeness. Combining a WHERE filter with the distance operator keeps retrieval inside the caller's scope and improves relevance. Index the filter columns too. Local study-map skill 2.9 (PostgreSQL RAG with Metadata Filters), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Cosmos DB and PostgreSQL vector documentation: https://learn.microsoft.com/en-us/azure/cosmos-db/

- **A:** Correct. Combining a WHERE filter with the distance operator keeps retrieval inside the caller's scope and improves relevance. Index the filter columns too. In this case: Filtering inside the vector query enforces scope and preserves result completeness.
- **B:** Incorrect for this question. Post-filtering can return fewer results than requested and can leak existence or counts if the filtering is careless. Push authorization into the query. Why the correct answer wins: Filtering inside the vector query enforces scope and preserves result completeness.
- **C:** Incorrect for this question. HNSW gives fast approximate nearest-neighbour queries with a larger memory footprint and slower builds. Recall is tunable at query time. Why the correct answer wins: Filtering inside the vector query enforces scope and preserves result completeness.
- **D:** Incorrect for this question. An exact scan is accurate but scales linearly and burns compute. It is a baseline for measuring recall, not a production strategy. Why the correct answer wins: Filtering inside the vector query enforces scope and preserves result completeness.

### Question 93 — C

Answer: Create a vector index in Managed Redis for similarity search. A Redis vector index performs in-memory similarity search. Redis vector search serves low-latency similarity queries from memory. The corpus must fit the memory budget and be rebuilt on model change. Local study-map skill 2.12 (Azure Managed Redis Vector Indexing), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Cosmos DB and PostgreSQL vector documentation: https://learn.microsoft.com/en-us/azure/cosmos-db/

- **A:** Incorrect for this question. A cache absorbs repeated reads and cuts latency for hot data. Cache keys, TTLs, and invalidation must match the freshness requirement. Why the correct answer wins: A Redis vector index performs in-memory similarity search.
- **B:** Incorrect for this question. A lock can serialize work across instances, but correctness under retries still needs idempotency keys in the data store. Locks expire and can be lost. Why the correct answer wins: A Redis vector index performs in-memory similarity search.
- **C:** Correct. Redis vector search serves low-latency similarity queries from memory. The corpus must fit the memory budget and be rebuilt on model change. In this case: A Redis vector index performs in-memory similarity search.
- **D:** Incorrect for this question. Session storage in Redis survives instance restarts and supports distributed instances. Sessions must be scoped and expiring. Why the correct answer wins: A Redis vector index performs in-memory similarity search.

### Question 94 — B

Answer: Define a custom event schema for the topic. A custom topic event carries the domain notification. A custom schema fits domain events that are not resource lifecycle notifications. Consumers must version the schema contract. Local study-map skill 3.4 (Event Grid Filters, Custom Events, and Retries), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure messaging and Functions documentation: https://learn.microsoft.com/en-us/azure/service-bus-messaging/

- **A:** Incorrect for this question. Subject and event-type filters keep handlers focused and reduce cost. Filters are evaluated on event metadata, not payload body. Why the correct answer wins: A custom topic event carries the domain notification.
- **B:** Correct. A custom schema fits domain events that are not resource lifecycle notifications. Consumers must version the schema contract. In this case: A custom topic event carries the domain notification.
- **C:** Incorrect for this question. Event Grid retries failed deliveries with backoff and can store undeliverable events. Handlers must still be idempotent. Why the correct answer wins: A custom topic event carries the domain notification.
- **D:** Incorrect for this question. System topics carry Azure resource lifecycle events. Domain events that are not resource changes need a custom topic and schema. Why the correct answer wins: A custom topic event carries the domain notification.

### Question 95 — B

Answer: Create an HNSW index for low-latency approximate search. HNSW gives low-latency approximate search and allows recall to be tuned at query time. HNSW gives fast approximate nearest-neighbour queries with a larger memory footprint and slower builds. Recall is tunable at query time. Local study-map skill 2.7 (pgvector Indexing and Query Latency), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Cosmos DB and PostgreSQL vector documentation: https://learn.microsoft.com/en-us/azure/cosmos-db/

- **A:** Incorrect for this question. An external pooler multiplexes server connections for serverless or highly concurrent clients. Session-level features may be unavailable in transaction mode. Why the correct answer wins: HNSW gives low-latency approximate search and allows recall to be tuned at query time.
- **B:** Correct. HNSW gives fast approximate nearest-neighbour queries with a larger memory footprint and slower builds. Recall is tunable at query time. In this case: HNSW gives low-latency approximate search and allows recall to be tuned at query time.
- **C:** Incorrect for this question. An exact scan is accurate but scales linearly and burns compute. It is a baseline for measuring recall, not a production strategy. Why the correct answer wins: HNSW gives low-latency approximate search and allows recall to be tuned at query time.
- **D:** Incorrect for this question. IVFFlat uses clustering lists and needs periodic rebuilds as data grows, but costs less memory than HNSW. Probes trade recall for speed. Why the correct answer wins: HNSW gives low-latency approximate search and allows recall to be tuned at query time.

### Question 96 — C

Answer: Make the handler idempotent by using a message or business key. An idempotency key derived from the payment identifier turns a replay into a no-op instead of a duplicate write. At-least-once delivery means duplicates will happen, so the write must tolerate replay. A stored key makes the retry safe. Local study-map skill 3.3 (Service Bus Dead-Lettering and Retries), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure messaging and Functions documentation: https://learn.microsoft.com/en-us/azure/service-bus-messaging/

- **A:** Incorrect for this question. A duplicate-detection window drops repeated sends within the window, which helps with at-least-once producers. The window is time-bounded. Why the correct answer wins: An idempotency key derived from the payment identifier turns a replay into a no-op instead of a duplicate write.
- **B:** Incorrect for this question. Peek-lock keeps the message locked until the handler completes it, giving at-least-once processing with retry. Lock duration must exceed processing time. Why the correct answer wins: An idempotency key derived from the payment identifier turns a replay into a no-op instead of a duplicate write.
- **C:** Correct. At-least-once delivery means duplicates will happen, so the write must tolerate replay. A stored key makes the retry safe. In this case: An idempotency key derived from the payment identifier turns a replay into a no-op instead of a duplicate write.
- **D:** Incorrect for this question. Receive-and-delete removes the message on delivery, so a crash loses work silently. It suits telemetry, not payments. Why the correct answer wins: An idempotency key derived from the payment identifier turns a replay into a no-op instead of a duplicate write.

### Question 97 — A

Answer: Store repeated aggregations in a materialized view or update policy. A materialized view or update policy stores the repeated aggregation so the dashboard no longer scans raw data. Precomputed results avoid recomputing expensive aggregations on every dashboard refresh. The trade-off is storage and freshness lag. Local study-map skill 4.4 (KQL Queries for Logs and Metrics), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Key Vault, App Configuration, and Monitor documentation: https://learn.microsoft.com/en-us/azure/azure-monitor/

- **A:** Correct. Precomputed results avoid recomputing expensive aggregations on every dashboard refresh. The trade-off is storage and freshness lag. In this case: A materialized view or update policy stores the repeated aggregation so the dashboard no longer scans raw data.
- **B:** Incorrect for this question. Reducing columns and rows early lowers query cost and latency. Broad queries over long ranges are the usual cause of slow KQL. Why the correct answer wins: A materialized view or update policy stores the repeated aggregation so the dashboard no longer scans raw data.
- **C:** Incorrect for this question. Joining request and dependency telemetry shows which downstream call fails inside a slow request. Cross-workspace joins need the right scope. Why the correct answer wins: A materialized view or update policy stores the repeated aggregation so the dashboard no longer scans raw data.
- **D:** Incorrect for this question. Time-binned aggregation reveals the shape of an incident: a step change, a ramp, or a periodic spike. Averages alone hide short outages. Why the correct answer wins: A materialized view or update policy stores the repeated aggregation so the dashboard no longer scans raw data.

### Question 98 — D

Answer: Test end-to-end connectivity from inside the container to each dependency. Name resolution and network rules are region-specific, so resolve and test from inside the pod. Reaching a dependency from the pod or replica proves DNS, egress, and firewall paths together. Host-side tests can succeed while the container path fails. Local study-map skill 1.7 (Container Logs, Events, and Connectivity), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure container hosting documentation: https://learn.microsoft.com/en-us/azure/container-apps/

- **A:** Incorrect for this question. A private endpoint needs matching name resolution or clients still resolve the public address. The zone must be linked to the workload network. Why the correct answer wins: Name resolution and network rules are region-specific, so resolve and test from inside the pod.
- **B:** Incorrect for this question. Container Apps and AKS surface stdout logs and platform events into a workspace for KQL analysis. Verbosity and retention cost money. Why the correct answer wins: Name resolution and network rules are region-specific, so resolve and test from inside the pod.
- **C:** Incorrect for this question. Readiness gates traffic until the app can serve it, and liveness restarts a wedged container. Wrong thresholds cause restart loops. Why the correct answer wins: Name resolution and network rules are region-specific, so resolve and test from inside the pod.
- **D:** Correct. Reaching a dependency from the pod or replica proves DNS, egress, and firewall paths together. Host-side tests can succeed while the container path fails. In this case: Name resolution and network rules are region-specific, so resolve and test from inside the pod.

### Question 99 — B

Answer: Inspect the dead-letter queue and resubmit corrected messages. Dead-lettering preserves the message outside the active queue. Dead-lettering preserves poison messages for diagnosis instead of losing them. Resubmission needs a fix and an idempotent handler. Local study-map skill 3.3 (Service Bus Dead-Lettering and Retries), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure messaging and Functions documentation: https://learn.microsoft.com/en-us/azure/service-bus-messaging/

- **A:** Incorrect for this question. Receive-and-delete removes the message on delivery, so a crash loses work silently. It suits telemetry, not payments. Why the correct answer wins: Dead-lettering preserves the message outside the active queue.
- **B:** Correct. Dead-lettering preserves poison messages for diagnosis instead of losing them. Resubmission needs a fix and an idempotent handler. In this case: Dead-lettering preserves the message outside the active queue.
- **C:** Incorrect for this question. Sessions give ordered, exclusive processing per session ID across competing consumers. They require session-aware senders and receivers. Why the correct answer wins: Dead-lettering preserves the message outside the active queue.
- **D:** Incorrect for this question. A delivery cap stops infinite retries of a failing message and moves it to the dead-letter queue. The cap must exceed legitimate transient retries. Why the correct answer wins: Dead-lettering preserves the message outside the active queue.

### Question 100 — C

Answer: Project only the columns needed and filter by time first. Filtering by time and projecting fewer columns reduces scanned data. Reducing columns and rows early lowers query cost and latency. Broad queries over long ranges are the usual cause of slow KQL. Local study-map skill 4.4 (KQL Queries for Logs and Metrics), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Key Vault, App Configuration, and Monitor documentation: https://learn.microsoft.com/en-us/azure/azure-monitor/

- **A:** Incorrect for this question. Platform metrics are cheap and near-real-time, so they suit latency and failure-rate alerts. Log-based alerts add latency and query cost. Why the correct answer wins: Filtering by time and projecting fewer columns reduces scanned data.
- **B:** Incorrect for this question. Joining request and dependency telemetry shows which downstream call fails inside a slow request. Cross-workspace joins need the right scope. Why the correct answer wins: Filtering by time and projecting fewer columns reduces scanned data.
- **C:** Correct. Reducing columns and rows early lowers query cost and latency. Broad queries over long ranges are the usual cause of slow KQL. In this case: Filtering by time and projecting fewer columns reduces scanned data.
- **D:** Incorrect for this question. Time-binned aggregation reveals the shape of an incident: a step change, a ramp, or a periodic spike. Averages alone hide short outages. Why the correct answer wins: Filtering by time and projecting fewer columns reduces scanned data.
