# Microsoft AI-200 — Full-Length Mock Exam 1

Azure AI Cloud Developer Associate · 100 questions · expanded practice bank · passing target 700/1000

Blueprint-weighted mock exam of 100 items. Item mix: 84 multiple-choice (8 of them sequencing items with four candidate sequences), 16 multi-select (selection count stated), and 4 case studies of 3 questions. Hot-area, drag-and-drop UI, labs, and adaptive problem-solution sets cannot be reproduced in a CSV; see the README for the exact fidelity boundary.

Original educational content, not actual, recalled, or copied Microsoft exam items.

## Questions

### 1. A release must be traceable to one built artifact so operations can roll back to the previous version by tag. Which registry practice should be enforced?

Domain: Develop containerized solutions on Azure

- A. Deploy the mutable latest tag and let the platform resolve it
- B. Run image builds on demand or on a trigger with ACR Tasks
- C. Apply an ACR retention policy to prune old untagged manifests
- D. Build and store versioned images in Azure Container Registry

### 2. Builds currently run on a developer workstation, and images differ between machines. Which change removes the local build host?

Domain: Develop containerized solutions on Azure

- A. Run image builds on demand or on a trigger with ACR Tasks
- B. Stage the change in a deployment slot and swap after verification
- C. Replicate the registry to each deployment region
- D. Build and store versioned images in Azure Container Registry

### 3. The same container must run with different log levels and feature toggles per environment without being rebuilt. What should supply those values?

Domain: Develop containerized solutions on Azure

- A. Reference a Key Vault secret from the app configuration instead of storing it
- B. Stage the change in a deployment slot and swap after verification
- C. Supply configuration through App Service application settings
- D. Deploy the image to Azure App Service as a web app

### 4. An internal pricing API must accept calls only from other workloads inside the environment network. What should be configured?

Domain: Develop containerized solutions on Azure

- A. Deploy the service to Azure Container Apps
- B. Configure Container Apps ingress for internal-only access
- C. Scale the container app on an event source with a KEDA scaler
- D. Create a new Container Apps revision and shift traffic between revisions

### 5. The platform team wants the deployment, service, and probes declared in version control and reapplied safely after any drift. What should be used?

Domain: Develop containerized solutions on Azure

- A. Rely on the horizontal pod autoscaler on CPU
- B. Run the batch job in Azure Container Instances
- C. Apply a declarative Kubernetes manifest to the cluster
- D. Run image builds on demand or on a trigger with ACR Tasks

### 6. Pods report ready, but calls to Cosmos DB time out while the same query succeeds from an administrator workstation. What should be verified next?

Domain: Develop containerized solutions on Azure

- A. Add readiness and liveness probes to the pod specification
- B. Enable diagnostic settings to route platform logs to the workspace
- C. Test end-to-end connectivity from inside the container to each dependency
- D. Query container logs and Kubernetes events in Log Analytics

### 7. You need immutable release artifacts and controlled registry growth. Which two actions should you take? Select two.

Domain: Develop containerized solutions on Azure

- A. Build and store versioned images in Azure Container Registry
- B. Replicate the registry to each deployment region
- C. Deploy the mutable latest tag and let the platform resolve it
- D. Stage the change in a deployment slot and swap after verification
- E. Apply an ACR retention policy to prune old untagged manifests

### 8. A Kubernetes deployment must be reproducible and must not receive traffic before it can serve requests. Which two elements belong in the manifest? Select two.

Domain: Develop containerized solutions on Azure

- A. Apply a declarative Kubernetes manifest to the cluster
- B. Run the batch job in Azure Container Instances
- C. Scale only on CPU utilization without an event scaler
- D. Rely on the horizontal pod autoscaler on CPU
- E. Add readiness and liveness probes to the pod specification

### 9. Which sequence correctly releases a new ranking service as a canary revision?

Domain: Develop containerized solutions on Azure

- A. Shift all traffic to a new revision → deploy the revision → check metrics → build the image → promote
- B. Deploy a new revision → shift all traffic → build and push the image → check metrics → roll back
- C. Check metrics → deploy a new revision → build and push the image → shift a small traffic percentage → promote
- D. Build and push the image → deploy a new revision → shift a small traffic percentage → check metrics → promote or roll back

### 10. A point read by order ID returns late and consumes far more request units than expected. Which change addresses the cause?

Domain: Develop AI solutions by using Azure data management services

- A. Include the partition key in the query predicate
- B. Increase provisioned throughput and watch the RU charge per query
- C. Choose a high-cardinality partition key that spreads writes
- D. Index every property by using the default automatic policy

### 11. Write cost is high on a container that only filters on three properties. What should be changed?

Domain: Develop AI solutions by using Azure data management services

- A. Restrict the indexing policy to the paths the queries use
- B. Enable autoscale throughput with a maximum RU limit
- C. Index every property by using the default automatic policy
- D. Choose the account consistency level that matches the read requirement

### 12. A shopping cart must never show a customer an older version of their own update, and global ordering is not required. Which consistency choice fits?

Domain: Develop AI solutions by using Azure data management services

- A. Use eventual consistency to minimize read cost
- B. Use session consistency for reads within the same client session
- C. Choose the account consistency level that matches the read requirement
- D. Use strong consistency for every read in the account

### 13. Product embeddings and product documents must live in one store so filters and similarity search run together. What should be used?

Domain: Develop AI solutions by using Azure data management services

- A. Use the DiskANN vector index for large collections
- B. Store embeddings in a vector property and query with VectorDistance
- C. Scan every document and compute similarity in application code
- D. Store embeddings in PostgreSQL by using the pgvector extension

### 14. Downstream enrichment must run whenever a product document is inserted or updated, without polling the container. What should be implemented?

Domain: Develop AI solutions by using Azure data management services

- A. Run a change feed processor to react to new and updated items
- B. Use a lease container to coordinate change feed readers
- C. Enable duplicate detection on the queue
- D. Publish the state change as an Event Grid event

### 15. A retrieval table must support category filters and a vector column in one query. How should it be modeled?

Domain: Develop AI solutions by using Azure data management services

- A. Scale compute and memory to fit index size and query concurrency
- B. Add a read replica and send all vector queries to it
- C. Increase storage throughput for index builds and bulk loads
- D. Model typed columns for filters and one vector column for the embedding

### 16. Nearest-neighbour queries over two million chunks must return in milliseconds with acceptable recall. Which index type should be created?

Domain: Develop AI solutions by using Azure data management services

- A. Create an HNSW index for low-latency approximate search
- B. Place a connection pooler in front of PostgreSQL for many short-lived clients
- C. Create an IVFFlat index to save memory on a large table
- D. Query without a vector index and let PostgreSQL scan the table

### 17. Every product page recomputes the identical recommendation block for every visitor. What should be added?

Domain: Develop AI solutions by using Azure data management services

- A. Cache responses in Azure Managed Redis
- B. Add a read replica and send all vector queries to it
- C. Set a TTL on each cached entry
- D. Use Azure Queue Storage for the work items

### 18. A burst of short-lived serverless requests opens a new database connection each time and exhausts server slots. What should be used first?

Domain: Develop AI solutions by using Azure data management services

- A. Add a read replica and send all vector queries to it
- B. Place a connection pooler in front of PostgreSQL for many short-lived clients
- C. Use prepared statements and batch round trips
- D. Reuse a bounded connection pool instead of opening a connection per request

### 19. A NoSQL workload must use the supported data-plane SDK for reads and must let several processor instances share change feed work. Which two components are required? Select two.

Domain: Develop AI solutions by using Azure data management services

- A. Index every property by using the default automatic policy
- B. Use a lease container to coordinate change feed readers
- C. Enable duplicate detection on the queue
- D. Query through the Cosmos DB SDK with parameterized queries
- E. Enable autoscale throughput with a maximum RU limit

### 20. A high-concurrency API must limit total database connections and survive many short-lived clients. Which two actions should you take? Select two.

Domain: Develop AI solutions by using Azure data management services

- A. Use prepared statements and batch round trips
- B. Add a read replica and send all vector queries to it
- C. Increase storage throughput for index builds and bulk loads
- D. Reuse a bounded connection pool instead of opening a connection per request
- E. Place a connection pooler in front of PostgreSQL for many short-lived clients

### 21. Which sequence correctly prepares a PostgreSQL table for vector similarity search?

Domain: Develop AI solutions by using Azure data management services

- A. Build the index → create the vector extension → create the table with a vector column → query nearest neighbours
- B. Create the vector extension → create the table with a vector column → build the index → query nearest neighbours with a distance operator
- C. Query nearest neighbours → build the index → create the vector extension → create the table with a vector column
- D. Create the table with a vector column → query nearest neighbours → create the vector extension → build the index

### 22. Events for one order must be processed in order by a single worker even when several workers are running. What should be enabled?

Domain: Connect to and consume Azure services

- A. Enable duplicate detection on the queue
- B. Receive with peek-lock and complete or abandon explicitly
- C. Use Service Bus sessions to keep related messages ordered
- D. Set a maximum delivery count and handle the dead-letter path

### 23. A topic fans out enrichment requests, but one subscriber should see only messages with a specific region property. What should be configured?

Domain: Connect to and consume Azure services

- A. Define a custom event schema for the topic
- B. Add a SQL or correlation filter to a subscription
- C. Filter the Event Grid subscription by subject or event type
- D. Enable duplicate detection on the queue

### 24. A malformed message is retried forever and blocks a worker slot. What should be configured?

Domain: Connect to and consume Azure services

- A. Set a maximum delivery count and handle the dead-letter path
- B. Enable duplicate detection on the queue
- C. Inspect the dead-letter queue and resubmit corrected messages
- D. Receive with peek-lock and complete or abandon explicitly

### 25. The queue delivers at least once, and a duplicate must not create a second order record. What should the handler do?

Domain: Connect to and consume Azure services

- A. Use prepared statements and batch round trips
- B. Make the handler idempotent by using a message or business key
- C. Orchestrate the multi-step workflow with Durable Functions
- D. Receive in receive-and-delete mode for at-most-once delivery

### 26. An event subscription receives every resource change but only blob-created events are relevant. What should be added?

Domain: Connect to and consume Azure services

- A. Bind a queue or event trigger to the function
- B. Filter the Event Grid subscription by subject or event type
- C. Enable duplicate detection on the queue
- D. Add a SQL or correlation filter to a subscription

### 27. A webhook handler is intermittently unavailable and events must not be lost permanently. What should be configured?

Domain: Connect to and consume Azure services

- A. Rely on Event Grid retries with a dead-letter destination
- B. Filter the Event Grid subscription by subject or event type
- C. Stream telemetry through Azure Event Hubs
- D. Define a custom event schema for the topic

### 28. A function must run automatically when a message arrives on a queue, without a polling loop in application code. What should be configured?

Domain: Connect to and consume Azure services

- A. Use input and output bindings instead of hand-written SDK calls
- B. Expose the endpoint through an HTTP trigger
- C. Bind a queue or event trigger to the function
- D. Orchestrate the multi-step workflow with Durable Functions

### 29. An interactive function must avoid cold-start latency and must reach resources over a virtual network. Which hosting choice fits?

Domain: Connect to and consume Azure services

- A. Orchestrate the multi-step workflow with Durable Functions
- B. Expose the endpoint through an HTTP trigger
- C. Host the function app on the consumption plan
- D. Host the function app on a premium plan with pre-warmed instances

### 30. One order event must reach an inventory handler and a billing handler independently, and billing should receive only high-value orders. Which two features are required? Select two.

Domain: Connect to and consume Azure services

- A. Filter the Event Grid subscription by subject or event type
- B. Queue the work on a Service Bus queue and process it with a worker
- C. Use Azure Queue Storage for the work items
- D. Add a SQL or correlation filter to a subscription
- E. Publish to a Service Bus topic with multiple subscriptions

### 31. Poison messages must not be lost and must not loop indefinitely. Which two capabilities address that? Select two.

Domain: Connect to and consume Azure services

- A. Use prepared statements and batch round trips
- B. Inspect the dead-letter queue and resubmit corrected messages
- C. Enable duplicate detection on the queue
- D. Set a maximum delivery count and handle the dead-letter path
- E. Receive in receive-and-delete mode for at-most-once delivery

### 32. A domain event that is not a resource lifecycle notification must be published and routed only to the correct consumer. Which two elements are required? Select two.

Domain: Connect to and consume Azure services

- A. Add a SQL or correlation filter to a subscription
- B. Define a custom event schema for the topic
- C. Rely on Event Grid retries with a dead-letter destination
- D. Filter the Event Grid subscription by subject or event type
- E. Stream telemetry through Azure Event Hubs

### 33. Which sequence correctly processes an enrichment message through Service Bus?

Domain: Connect to and consume Azure services

- A. Receive with peek-lock → publish the message → complete the message → process the work → dead-letter after the delivery limit
- B. Process the work → receive with peek-lock → publish the message → complete the message → dead-letter after the delivery limit
- C. Publish the message → receive with peek-lock → process the work → complete the message → dead-letter after the delivery limit
- D. Publish the message → complete the message → receive with peek-lock → process the work → dead-letter after the delivery limit

### 34. A partner credential must be stored with access control and audit rather than in a container environment variable. Where should it live?

Domain: Secure, monitor, troubleshoot Azure solutions

- A. Supply configuration through App Service application settings
- B. Assign a least-privilege role to the application identity
- C. Store the secret in Azure Key Vault and read it at runtime
- D. Pin the application to a specific secret version

### 35. Credentials must be replaced every 60 days without an application outage or manual redeployment. What should be implemented?

Domain: Secure, monitor, troubleshoot Azure solutions

- A. Authenticate with a managed identity instead of a stored key
- B. Supply configuration through App Service application settings
- C. Rotate the secret on a schedule and let apps resolve the current version
- D. Pin the application to a specific secret version

### 36. Feature flags must be changed per environment without redeploying the service or editing code. What should be used?

Domain: Secure, monitor, troubleshoot Azure solutions

- A. Supply configuration through App Service application settings
- B. Store the secret in Azure Key Vault and read it at runtime
- C. Store settings and feature flags in Azure App Configuration
- D. Use App Configuration labels to separate environments

### 37. A running service still uses yesterday's threshold after the value was changed in the configuration store. What is missing?

Domain: Secure, monitor, troubleshoot Azure solutions

- A. Deploy the function app through a CI pipeline with app settings applied
- B. Use App Configuration labels to separate environments
- C. Pin the application to a specific secret version
- D. Enable configuration refresh so changes apply without a restart

### 38. A request crosses an HTTP API, a queue, and a function, and the team needs one connected trace across all three hops. What should be implemented?

Domain: Secure, monitor, troubleshoot Azure solutions

- A. Query the workspace with KQL to find the failing operation
- B. Instrument the service with the OpenTelemetry SDK
- C. Enable diagnostic settings to route platform logs to the workspace
- D. Send telemetry to Application Insights and inspect the transaction view

### 39. The team needs the failure rate per five-minute window during an incident rather than a single daily average. Which query construct should be used?

Domain: Secure, monitor, troubleshoot Azure solutions

- A. Join the requests and dependencies tables on the operation ID
- B. Query the workspace with KQL to find the failing operation
- C. Create an alert rule on the failure rate or latency metric
- D. Aggregate with summarize and bin to see the failure rate over time

### 40. A request is slow but no exception is logged, and the team suspects one downstream dependency. What should the query do?

Domain: Secure, monitor, troubleshoot Azure solutions

- A. Send telemetry to Application Insights and inspect the transaction view
- B. Join the requests and dependencies tables on the operation ID
- C. Aggregate with summarize and bin to see the failure rate over time
- D. Create an alert rule on the failure rate or latency metric

### 41. On-call must be notified automatically when latency crosses a threshold for ten minutes. What should be configured?

Domain: Secure, monitor, troubleshoot Azure solutions

- A. Enable diagnostic settings to route platform logs to the workspace
- B. Create an alert rule on the failure rate or latency metric
- C. Send telemetry to Application Insights and inspect the transaction view
- D. Aggregate with summarize and bin to see the failure rate over time

### 42. A container must read a secret and a database without any stored credential in its image or settings. What should it use?

Domain: Secure, monitor, troubleshoot Azure solutions

- A. Store the secret in Azure Key Vault and read it at runtime
- B. Assign a least-privilege role to the application identity
- C. Supply configuration through App Service application settings
- D. Authenticate with a managed identity instead of a stored key

### 43. A secret must be held in a managed vault and read without a stored credential. Which two actions should you take? Select two.

Domain: Secure, monitor, troubleshoot Azure solutions

- A. Rotate the secret on a schedule and let apps resolve the current version
- B. Authenticate with a managed identity instead of a stored key
- C. Supply configuration through App Service application settings
- D. Store the secret in Azure Key Vault and read it at runtime
- E. Pin the application to a specific secret version

### 44. Which sequence correctly introduces a rotated secret to a running application?

Domain: Secure, monitor, troubleshoot Azure solutions

- A. Grant the app identity access → store the secret in Key Vault → rotate the secret → reference the secret from the app → the app reads the new version
- B. Reference the secret from the app → rotate the secret → store the secret in Key Vault → grant the app identity access → the app reads the new version
- C. Store the secret in Key Vault → grant the app identity access → reference the secret from the app → rotate the secret → the app reads the new version
- D. Rotate the secret → reference the secret from the app → store the secret in Key Vault → grant the app identity access → the app reads the new version

### 45. Two environments must run byte-identical storefront images, and a rebuilt tag must never change what production runs. What should the deployment reference?

Domain: Develop containerized solutions on Azure

- A. Apply an ACR retention policy to prune old untagged manifests
- B. Stage the change in a deployment slot and swap after verification
- C. Deploy the image by digest instead of a mutable tag
- D. Deploy the mutable latest tag and let the platform resolve it

### 46. Nightly image builds must run from the main branch without a developer workstation and without a cluster. What should perform the build?

Domain: Develop containerized solutions on Azure

- A. Build and store versioned images in Azure Container Registry
- B. Run image builds on demand or on a trigger with ACR Tasks
- C. Deploy the workload to Azure Kubernetes Service
- D. Deploy the service to Azure Container Apps

### 47. The recommendation API must accept calls only from the storefront inside the same Container Apps environment. What should be configured?

Domain: Develop containerized solutions on Azure

- A. Stage the change in a deployment slot and swap after verification
- B. Create a new Container Apps revision and shift traffic between revisions
- C. Configure Container Apps ingress for internal-only access
- D. Scale the container app on an event source with a KEDA scaler

### 48. Recommendation workers read a Service Bus queue that is empty overnight and thousands deep during a promotion. What should drive replica count?

Domain: Develop containerized solutions on Azure

- A. Rely on the horizontal pod autoscaler on CPU
- B. Scale only on CPU utilization without an event scaler
- C. Set a minimum replica count above zero for the container app
- D. Scale on the Service Bus queue length with a KEDA Azure Service Bus scaler

### 49. Pods must read a catalog secret through an Azure identity, and no connection string may be mounted into the pod. What should be configured?

Domain: Develop containerized solutions on Azure

- A. Reference a Key Vault secret from the app configuration instead of storing it
- B. Federate a Kubernetes service account to a managed identity
- C. Deploy the mutable latest tag and let the platform resolve it
- D. Replicate the registry to each deployment region

### 50. After a private endpoint was added for the recommendations database, only the storefront pods fail to resolve the host name. What should be checked first?

Domain: Develop containerized solutions on Azure

- A. Test end-to-end connectivity from inside the container to each dependency
- B. Query the workspace with KQL to find the failing operation
- C. Link the private DNS zone so the private endpoint name resolves
- D. Enable diagnostic settings to route platform logs to the workspace

### 51. A containerized storefront API must be verified before it takes production traffic, and its log level must differ per slot. Which two actions should you take? Select two.

Domain: Develop containerized solutions on Azure

- A. Scale the container app on an event source with a KEDA scaler
- B. Create a new Container Apps revision and shift traffic between revisions
- C. Apply a declarative Kubernetes manifest to the cluster
- D. Supply configuration through App Service application settings
- E. Stage the change in a deployment slot and swap after verification

### 52. A latency-sensitive container app takes twenty seconds to warm up after idle periods, and customers notice every first request. What should be configured?

Domain: Develop containerized solutions on Azure

- A. Scale only on CPU utilization without an event scaler
- B. Create a new Container Apps revision and shift traffic between revisions
- C. Set a minimum replica count above zero for the container app
- D. Scale the container app on an event source with a KEDA scaler

### 53. Which sequence correctly proves that a Container Apps revision scales on a queue before it is trusted in production?

Domain: Develop containerized solutions on Azure

- A. Confirm replicas grow and drain → deploy the container app with a minimum replica count → attach a KEDA scale rule → run a load test → cap the maximum replicas
- B. Deploy the container app with a minimum replica count → attach a KEDA scale rule that uses the workload identity → cap the maximum replicas → run a load test → confirm replicas grow and drain
- C. Run a load test → deploy the container app with a minimum replica count → attach a KEDA scale rule → cap the maximum replicas → confirm replicas grow and drain
- D. Attach a KEDA scale rule that uses the workload identity → deploy the container app with a minimum replica count → confirm replicas grow and drain → run a load test → cap the maximum replicas

### 54. Clusters in Europe and Asia pull a large storefront image on every scale-out, and pulls add minutes to cold start in Asia. What should be configured?

Domain: Develop containerized solutions on Azure

- A. Run image builds on demand or on a trigger with ACR Tasks
- B. Build and store versioned images in Azure Container Registry
- C. Stage the change in a deployment slot and swap after verification
- D. Replicate the registry to each deployment region

### 55. Replica count oscillates between one and six during a steady promotion, and each swing resets warm connections. What should be adjusted?

Domain: Develop containerized solutions on Azure

- A. Rely on the horizontal pod autoscaler on CPU
- B. Tune the scale rule cool-down period and maximum replicas
- C. Scale the container app on an event source with a KEDA scaler
- D. Scale only on CPU utilization without an event scaler

### 56. A catalog query returns sixty thousand product documents and the client times out while buffering them. What should the client use?

Domain: Develop AI solutions by using Azure data management services

- A. Query through the Cosmos DB SDK with parameterized queries
- B. Increase provisioned throughput and watch the RU charge per query
- C. Page large result sets with the continuation token
- D. Include the partition key in the query predicate

### 57. Queries filter on category and order by popularity, and the request still sorts at runtime with a high request charge. What should be added?

Domain: Develop AI solutions by using Azure data management services

- A. Index every property by using the default automatic policy
- B. Add a composite index for the filtered and ordered properties
- C. Restrict the indexing policy to the paths the queries use
- D. Enable autoscale throughput with a maximum RU limit

### 58. Similarity queries begin failing with a dimension mismatch after the embedding model moved from 1536 to 3072 dimensions. What must change?

Domain: Develop AI solutions by using Azure data management services

- A. Store embeddings in a vector property and query with VectorDistance
- B. Declare the embedding dimensions and vector index type on the container policy
- C. Use the cosine distance function that matches how the embeddings were trained
- D. Create an HNSW index for low-latency approximate search

### 59. Long reporting scans on the chunk table slow the product lookups that share the same primary. What should be introduced?

Domain: Develop AI solutions by using Azure data management services

- A. Increase storage throughput for index builds and bulk loads
- B. Inspect the plan with EXPLAIN ANALYZE before changing indexes
- C. Scale compute and memory to fit index size and query concurrency
- D. Add a read replica and send all vector queries to it

### 60. Eight million embeddings must be indexed on an instance whose memory cannot hold a graph index. What should be created?

Domain: Develop AI solutions by using Azure data management services

- A. Add a composite index for the filtered and ordered properties
- B. Query without a vector index and let PostgreSQL scan the table
- C. Create an IVFFlat index to save memory on a large table
- D. Create an HNSW index for low-latency approximate search

### 61. Similarity queries slowed sharply after a bulk delete of stale chunks even though the query text did not change. What should be run?

Domain: Develop AI solutions by using Azure data management services

- A. Run VACUUM and ANALYZE after bulk loads and large deletes
- B. Increase storage throughput for index builds and bulk loads
- C. Inspect the plan with EXPLAIN ANALYZE before changing indexes
- D. Build the vector index concurrently so writes are not blocked

### 62. A Functions app opens hundreds of short-lived connections during each burst, and PostgreSQL rejects new sessions. What should be added?

Domain: Develop AI solutions by using Azure data management services

- A. Place a connection pooler in front of PostgreSQL for many short-lived clients
- B. Reuse a bounded connection pool instead of opening a connection per request
- C. Increase storage throughput for index builds and bulk loads
- D. Use prepared statements and batch round trips

### 63. Price changes are not visible on the storefront for up to an hour after caching was introduced. What is missing?

Domain: Develop AI solutions by using Azure data management services

- A. Set a TTL on each cached entry
- B. Invalidate or overwrite the cache entry when the source changes
- C. Rely on the eviction policy and skip explicit TTLs
- D. Flush the database after each deployment to guarantee fresh data

### 64. A similar-products strip must answer within five milliseconds, and the embedding set already fits in memory. What should be built?

Domain: Develop AI solutions by using Azure data management services

- A. Create a vector index in Managed Redis for similarity search
- B. Cache responses in Azure Managed Redis
- C. Store user session state in Managed Redis with an expiry
- D. Use a distributed lock in Redis to make processing idempotent

### 65. Entries for retired products are never requested again, yet memory keeps filling until evictions start. What should be configured?

Domain: Develop AI solutions by using Azure data management services

- A. Set a TTL on each cached entry
- B. Invalidate or overwrite the cache entry when the source changes
- C. Rely on the eviction policy and skip explicit TTLs
- D. Flush the database after each deployment to guarantee fresh data

### 66. A catalog reader must use the supported SDK for queries and must not buffer every result in memory. Which two actions should you take? Select two.

Domain: Develop AI solutions by using Azure data management services

- A. Index every property by using the default automatic policy
- B. Page large result sets with the continuation token
- C. Include the partition key in the query predicate
- D. Scan every document and compute similarity in application code
- E. Query through the Cosmos DB SDK with parameterized queries

### 67. Write charge must fall and a filter-plus-order query must stop sorting at runtime. Which two changes should you make? Select two.

Domain: Develop AI solutions by using Azure data management services

- A. Increase provisioned throughput and watch the RU charge per query
- B. Index every property by using the default automatic policy
- C. Enable autoscale throughput with a maximum RU limit
- D. Add a composite index for the filtered and ordered properties
- E. Restrict the indexing policy to the paths the queries use

### 68. Which sequence correctly tunes a Cosmos DB catalog container for a single-partition query?

Domain: Develop AI solutions by using Azure data management services

- A. Choose a high-cardinality partition key → set the indexing policy to the queried paths → choose autoscale throughput → query with the partition key → measure the request charge
- B. Measure the request charge → choose a high-cardinality partition key → set the indexing policy to the queried paths → choose autoscale throughput → query with the partition key
- C. Query with the partition key → set the indexing policy to the queried paths → choose a high-cardinality partition key → choose autoscale throughput → measure the request charge
- D. Set the indexing policy to the queried paths → query with the partition key → choose a high-cardinality partition key → measure the request charge → choose autoscale throughput

### 69. A worker crashes after charging a card but before the message is removed, and the work must not be lost. What should the receive mode be?

Domain: Connect to and consume Azure services

- A. Enable duplicate detection on the queue
- B. Receive in receive-and-delete mode for at-most-once delivery
- C. Receive with peek-lock and complete or abandon explicitly
- D. Use Service Bus sessions to keep related messages ordered

### 70. A publisher retries on timeout, so the same order event can arrive twice within a few minutes. What should be enabled?

Domain: Connect to and consume Azure services

- A. Enable duplicate detection on the queue
- B. Set a maximum delivery count and handle the dead-letter path
- C. Make the handler idempotent by using a message or business key
- D. Inspect the dead-letter queue and resubmit corrected messages

### 71. A recommendation event must wait for a pricing service to recover without consuming delivery attempts in the meantime. What should the handler do?

Domain: Connect to and consume Azure services

- A. Set a maximum delivery count and handle the dead-letter path
- B. Receive with peek-lock and complete or abandon explicitly
- C. Defer the message and retry it after the dependency recovers
- D. Inspect the dead-letter queue and resubmit corrected messages

### 72. A function writes an enriched product to Cosmos DB, and the team wants no hand-written SDK client in the handler. What should be used?

Domain: Connect to and consume Azure services

- A. Bind a queue or event trigger to the function
- B. Expose the endpoint through an HTTP trigger
- C. Orchestrate the multi-step workflow with Durable Functions
- D. Use input and output bindings instead of hand-written SDK calls

### 73. A queue-triggered function pulls so many messages at once that PostgreSQL rejects connections during each burst. What should be tuned?

Domain: Connect to and consume Azure services

- A. Host the function app on a premium plan with pre-warmed instances
- B. Host the function app on the consumption plan
- C. Tune the function app concurrency and batch size
- D. Configure the host retry policy with exponential backoff

### 74. A nightly job must rebuild the recommendation index at 02:00 with no caller anywhere in the system. What should be used?

Domain: Connect to and consume Azure services

- A. Bind a queue or event trigger to the function
- B. Expose the endpoint through an HTTP trigger
- C. Run the scheduled maintenance from a timer trigger
- D. Rely on Event Grid retries with a dead-letter destination

### 75. A function update must be verified against realistic traffic before it replaces the running production version. What should be used?

Domain: Connect to and consume Azure services

- A. Host the function app on a premium plan with pre-warmed instances
- B. Deploy the function app through a CI pipeline with app settings applied
- C. Host the function app on the consumption plan
- D. Use a deployment slot on the function app for staging

### 76. Blob events must be delivered only for the catalog container and must not be lost while the handler is down. Which two features are required? Select two.

Domain: Connect to and consume Azure services

- A. Filter the Event Grid subscription by subject or event type
- B. Add a SQL or correlation filter to a subscription
- C. Stream telemetry through Azure Event Hubs
- D. Define a custom event schema for the topic
- E. Rely on Event Grid retries with a dead-letter destination

### 77. A function must call Cosmos DB without a stored key and must be released through the pipeline with its settings applied. Which two actions should you take? Select two.

Domain: Connect to and consume Azure services

- A. Supply configuration through App Service application settings
- B. Deploy the function app through a CI pipeline with app settings applied
- C. Expose the endpoint through an HTTP trigger
- D. Host the function app on the consumption plan
- E. Assign a managed identity to the function app and use it for downstream calls

### 78. Which sequence correctly handles a recommendation message that must survive a worker failure?

Domain: Connect to and consume Azure services

- A. Publish the message → receive with peek-lock → process the work → complete the message → dead-letter after the delivery limit
- B. Receive with peek-lock → publish the message → complete the message → process the work → dead-letter after the delivery limit
- C. Process the work → receive with peek-lock → publish the message → complete the message → dead-letter after the delivery limit
- D. Publish the message → complete the message → receive with peek-lock → process the work → dead-letter after the delivery limit

### 79. The app reads a vault secret by using its managed identity and receives 403 from the secret endpoint. What is missing?

Domain: Secure, monitor, troubleshoot Azure solutions

- A. Grant the app identity data-plane access to the vault
- B. Reference a Key Vault secret from the app configuration instead of storing it
- C. Store the secret in Azure Key Vault and read it at runtime
- D. Assign a least-privilege role to the application identity

### 80. A storage key must be replaced every thirty days without redeploying the storefront. What should be configured?

Domain: Secure, monitor, troubleshoot Azure solutions

- A. Enable purge protection and soft delete on the vault
- B. Authenticate with a managed identity instead of a stored key
- C. Pin the application to a specific secret version
- D. Rotate the secret on a schedule and let apps resolve the current version

### 81. A risky ranking change must ship to production before it is switched on for shoppers. What should be used?

Domain: Secure, monitor, troubleshoot Azure solutions

- A. Use App Configuration labels to separate environments
- B. Ship the code dark behind a feature flag
- C. Store settings and feature flags in Azure App Configuration
- D. Enable configuration refresh so changes apply without a restart

### 82. A request loses four seconds somewhere between the API and the ranking service, and the transaction view stops at the API. What should be added?

Domain: Secure, monitor, troubleshoot Azure solutions

- A. Correlate logs with the operation or trace identifier
- B. Propagate trace context across every service and queue hop
- C. Instrument the service with the OpenTelemetry SDK
- D. Create a custom span around each downstream call

### 83. The team needs the five-minute failure rate for the ranking endpoint across the last day. What should the query use?

Domain: Secure, monitor, troubleshoot Azure solutions

- A. Aggregate with summarize and bin to see the failure rate over time
- B. Join the requests and dependencies tables on the operation ID
- C. Query the workspace with KQL to find the failing operation
- D. Project only the columns needed and filter by time first

### 84. The workspace bill doubled after verbose container logging was enabled, and only thirty days of history are needed. What should be changed?

Domain: Secure, monitor, troubleshoot Azure solutions

- A. Query container logs and Kubernetes events in Log Analytics
- B. Enable diagnostic settings to route platform logs to the workspace
- C. Alert on platform metrics rather than only on log queries
- D. Set the workspace retention and table plan to control log cost

### 85. A new API must read Cosmos DB and a vault secret with no credential in configuration. Which two actions should you take? Select two.

Domain: Secure, monitor, troubleshoot Azure solutions

- A. Authenticate with a managed identity instead of a stored key
- B. Reference a Key Vault secret from the app configuration instead of storing it
- C. Assign a least-privilege role to the application identity
- D. Enable purge protection and soft delete on the vault
- E. Pin the application to a specific secret version

### 86. One App Configuration store must serve three environments and must not hold a secret value itself. Which two features are required? Select two.

Domain: Secure, monitor, troubleshoot Azure solutions

- A. Ship the code dark behind a feature flag
- B. Use App Configuration labels to separate environments
- C. Reference the Key Vault secret from an App Configuration key value
- D. Pin the application to a specific secret version
- E. Enable configuration refresh so changes apply without a restart

### 87. A vault holding regulated data must survive an accidental deletion and must remain readable by the app identity. Which two actions should you take? Select two.

Domain: Secure, monitor, troubleshoot Azure solutions

- A. Pin the application to a specific secret version
- B. Grant the app identity data-plane access to the vault
- C. Reference a Key Vault secret from the app configuration instead of storing it
- D. Rotate the secret on a schedule and let apps resolve the current version
- E. Enable purge protection and soft delete on the vault

### 88. Which sequence correctly makes a slow downstream dependency visible in distributed traces?

Domain: Secure, monitor, troubleshoot Azure solutions

- A. Alert on the failure rate → instrument the service with the OpenTelemetry SDK → propagate the trace context across queue hops → export spans to the collector → query the transaction view for the slow dependency
- B. Query the transaction view for the slow dependency → export spans to the collector → instrument the service with the OpenTelemetry SDK → alert on the failure rate → propagate the trace context across queue hops
- C. Export spans to the collector → instrument the service with the OpenTelemetry SDK → query the transaction view for the slow dependency → propagate the trace context across queue hops → alert on the failure rate
- D. Instrument the service with the OpenTelemetry SDK → propagate the trace context across queue hops → export spans to the collector → query the transaction view for the slow dependency → alert on the failure rate

---

## Case study — Alpine Outfitters

The next three questions refer to this scenario. Read the full scenario before answering; case-study items are scored individually.

### 89. Four enrichment processors must share change feed work, and each partition must be read by exactly one instance. What coordinates the split?

Domain: Develop AI solutions by using Azure data management services

- A. Run a change feed processor to react to new and updated items
- B. Use a lease container to coordinate change feed readers
- C. Set an item time-to-live on the container
- D. Enable duplicate detection on the queue

### 90. The team must react to blob creation in its catalog storage account without writing and hosting a custom publisher. What should be used?

Domain: Connect to and consume Azure services

- A. Rely on Event Grid retries with a dead-letter destination
- B. Subscribe to a system topic for resource events
- C. Define a custom event schema for the topic
- D. Publish the state change as an Event Grid event

### 91. A feature flag change must reach running instances without a restart or a redeploy during peak season. What should be enabled?

Domain: Secure, monitor, troubleshoot Azure solutions

- A. Enable configuration refresh so changes apply without a restart
- B. Reference the Key Vault secret from an App Configuration key value
- C. Use App Configuration labels to separate environments
- D. Store settings and feature flags in Azure App Configuration

---

## Case study — Fabrikam catalog

The next three questions refer to this scenario. Read the full scenario before answering; case-study items are scored individually.

### 92. Retrieval must return only chunks the caller is entitled to see while still returning a full result set. What should the query do?

Domain: Develop AI solutions by using Azure data management services

- A. Create an HNSW index for low-latency approximate search
- B. Create an IVFFlat index to save memory on a large table
- C. Retrieve nearest neighbours first and discard unauthorized rows in the application
- D. Filter on metadata columns in the same query as the vector search

### 93. Vector queries became slow after the index grew, and the server shows heavy memory pressure. What should be addressed?

Domain: Develop AI solutions by using Azure data management services

- A. Scale compute and memory to fit index size and query concurrency
- B. Place a connection pooler in front of PostgreSQL for many short-lived clients
- C. Increase storage throughput for index builds and bulk loads
- D. Add a read replica and send all vector queries to it

### 94. A latency-critical similarity lookup must avoid a round trip to the relational database. What should be used?

Domain: Develop AI solutions by using Azure data management services

- A. Create a vector index in Managed Redis for similarity search
- B. Store user session state in Managed Redis with an expiry
- C. Use a distributed lock in Redis to make processing idempotent
- D. Cache responses in Azure Managed Redis

---

## Case study — Northwind catalog

The next three questions refer to this scenario. Read the full scenario before answering; case-study items are scored individually.

### 95. A new ranking service must receive a small share of production traffic while the previous version keeps serving the rest. Which capability provides that split?

Domain: Develop containerized solutions on Azure

- A. Rely on the horizontal pod autoscaler on CPU
- B. Stage the change in a deployment slot and swap after verification
- C. Replicate the registry to each deployment region
- D. Create a new Container Apps revision and shift traffic between revisions

### 96. Workers are idle overnight and back up during promotions, and the queue length is the true measure of work. What should drive replica count?

Domain: Develop containerized solutions on Azure

- A. Rely on the horizontal pod autoscaler on CPU
- B. Run the batch job in Azure Container Instances
- C. Scale on the Service Bus queue length with a KEDA Azure Service Bus scaler
- D. Scale only on CPU utilization without an event scaler

### 97. The container needs a third-party API key, and auditors must confirm it is never stored in deployment settings. What should the app configuration use?

Domain: Develop containerized solutions on Azure

- A. Supply configuration through App Service application settings
- B. Pin the application to a specific secret version
- C. Deploy the mutable latest tag and let the platform resolve it
- D. Reference a Key Vault secret from the app configuration instead of storing it

---

## Case study — Tailspin Retail

The next three questions refer to this scenario. Read the full scenario before answering; case-study items are scored individually.

### 98. The storefront container needs a different currency list per environment, and merchandising changes it weekly without a release. What should supply the value?

Domain: Develop containerized solutions on Azure

- A. Pin the application to a specific secret version
- B. Supply configuration through App Service application settings
- C. Mount non-secret configuration from a Kubernetes ConfigMap
- D. Store settings and feature flags in Azure App Configuration

### 99. The fraud check reads pricing documents and must never see a stale value, and the workload is single-region so extra read latency is acceptable. Which consistency choice fits?

Domain: Develop AI solutions by using Azure data management services

- A. Use strong consistency for every read in the account
- B. Use eventual consistency to minimize read cost
- C. Use session consistency for reads within the same client session
- D. Choose the account consistency level that matches the read requirement

### 100. Order events must reach the recommendation, inventory, and loyalty services independently, and each service keeps its own cursor. What should be used?

Domain: Connect to and consume Azure services

- A. Use Azure Queue Storage for the work items
- B. Define a custom event schema for the topic
- C. Queue the work on a Service Bus queue and process it with a worker
- D. Publish to a Service Bus topic with multiple subscriptions

---

## Answer key and explanations

### Question 1 — D

Answer: Build and store versioned images in Azure Container Registry. Immutable, versioned tags tie a running deployment to a reviewed build and make rollback deterministic. ACR keeps tagged, versioned images next to the deployment target and supports identity-based pulls. Tagging strategy and retention still need a decision. Local study-map skill 1.1 (Container Image Lifecycle in Azure Container Registry), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure container hosting documentation: https://learn.microsoft.com/en-us/azure/container-apps/

- **A:** Incorrect for this question. A floating tag removes the link between a deployed revision and a specific build, so rollback and audit become guesswork. Why the correct answer wins: Immutable, versioned tags tie a running deployment to a reviewed build and make rollback deterministic.
- **B:** Incorrect for this question. ACR Tasks builds images in Azure on a commit or schedule without a local Docker host. It removes build-host drift but not image review. Why the correct answer wins: Immutable, versioned tags tie a running deployment to a reviewed build and make rollback deterministic.
- **C:** Incorrect for this question. A retention policy controls storage growth and registry clutter. It does not change which image tag a deployment references. Why the correct answer wins: Immutable, versioned tags tie a running deployment to a reviewed build and make rollback deterministic.
- **D:** Correct. ACR keeps tagged, versioned images next to the deployment target and supports identity-based pulls. Tagging strategy and retention still need a decision. In this case: Immutable, versioned tags tie a running deployment to a reviewed build and make rollback deterministic.

### Question 2 — A

Answer: Run image builds on demand or on a trigger with ACR Tasks. ACR Tasks builds the image in Azure from source on demand or on a trigger, so the build environment is identical every time. ACR Tasks builds images in Azure on a commit or schedule without a local Docker host. It removes build-host drift but not image review. Local study-map skill 1.2 (Automated Image Builds with ACR Tasks), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure container hosting documentation: https://learn.microsoft.com/en-us/azure/container-apps/

- **A:** Correct. ACR Tasks builds images in Azure on a commit or schedule without a local Docker host. It removes build-host drift but not image review. In this case: ACR Tasks builds the image in Azure from source on demand or on a trigger, so the build environment is identical every time.
- **B:** Incorrect for this question. A slot swap warms the new version before it takes production traffic and makes rollback a second swap. Slot-local settings must be marked sticky. Why the correct answer wins: ACR Tasks builds the image in Azure from source on demand or on a trigger, so the build environment is identical every time.
- **C:** Incorrect for this question. Geo-replication reduces cross-region pull latency and gives a local copy during a regional failure. It adds cost and replication management. Why the correct answer wins: ACR Tasks builds the image in Azure from source on demand or on a trigger, so the build environment is identical every time.
- **D:** Incorrect for this question. ACR keeps tagged, versioned images next to the deployment target and supports identity-based pulls. Tagging strategy and retention still need a decision. Why the correct answer wins: ACR Tasks builds the image in Azure from source on demand or on a trigger, so the build environment is identical every time.

### Question 3 — C

Answer: Supply configuration through App Service application settings. Application settings become environment variables and can differ per slot, so configuration changes do not require a new image. Application settings become environment variables for the container and can be swapped per slot. Sensitive values should still reference a vault. Local study-map skill 1.3 (Container Deployment to Azure App Service), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure container hosting documentation: https://learn.microsoft.com/en-us/azure/container-apps/

- **A:** Incorrect for this question. A Key Vault reference resolves at runtime so the secret is never written into application settings. The app identity still needs permission to read it. Why the correct answer wins: Application settings become environment variables and can differ per slot, so configuration changes do not require a new image.
- **B:** Incorrect for this question. A slot swap warms the new version before it takes production traffic and makes rollback a second swap. Slot-local settings must be marked sticky. Why the correct answer wins: Application settings become environment variables and can differ per slot, so configuration changes do not require a new image.
- **C:** Correct. Application settings become environment variables for the container and can be swapped per slot. Sensitive values should still reference a vault. In this case: Application settings become environment variables and can differ per slot, so configuration changes do not require a new image.
- **D:** Incorrect for this question. App Service runs a container with managed patching, deployment slots, and built-in authentication options. It is not a Kubernetes control plane. Why the correct answer wins: Application settings become environment variables and can differ per slot, so configuration changes do not require a new image.

### Question 4 — B

Answer: Configure Container Apps ingress for internal-only access. Internal ingress keeps the endpoint off the public internet while remaining reachable inside the environment. Internal ingress keeps the endpoint inside the environment virtual network. It is an exposure control, not an authorization control. Local study-map skill 1.4 (Container Apps Deployment and Revisions), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure container hosting documentation: https://learn.microsoft.com/en-us/azure/container-apps/

- **A:** Incorrect for this question. Container Apps provides a managed environment, revisions, and KEDA-based scaling without cluster administration. Platform limits differ from AKS. Why the correct answer wins: Internal ingress keeps the endpoint off the public internet while remaining reachable inside the environment.
- **B:** Correct. Internal ingress keeps the endpoint inside the environment virtual network. It is an exposure control, not an authorization control. In this case: Internal ingress keeps the endpoint off the public internet while remaining reachable inside the environment.
- **C:** Incorrect for this question. KEDA scalers drive replica count from queue length, lag, or other event metrics, including scale to zero. Cool-down and max replicas bound the behavior. Why the correct answer wins: Internal ingress keeps the endpoint off the public internet while remaining reachable inside the environment.
- **D:** Incorrect for this question. Revision-based traffic splitting enables canary and blue-green releases. Revision mode and scale rules must be set deliberately. Why the correct answer wins: Internal ingress keeps the endpoint off the public internet while remaining reachable inside the environment.

### Question 5 — C

Answer: Apply a declarative Kubernetes manifest to the cluster. A declarative manifest describes the desired state and is idempotent when reapplied. A manifest declares the desired deployment, service, and probe configuration in version control. Applying it repeatedly is idempotent. Local study-map skill 1.6 (AKS Deployment with Manifests), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure container hosting documentation: https://learn.microsoft.com/en-us/azure/container-apps/

- **A:** Incorrect for this question. HPA adjusts replicas from resource metrics but needs metrics-server and enough node capacity. It cannot scale to zero. Why the correct answer wins: A declarative manifest describes the desired state and is idempotent when reapplied.
- **B:** Incorrect for this question. Container Instances starts a single container group quickly for short tasks. It has no orchestrator-level scaling or revision model. Why the correct answer wins: A declarative manifest describes the desired state and is idempotent when reapplied.
- **C:** Correct. A manifest declares the desired deployment, service, and probe configuration in version control. Applying it repeatedly is idempotent. In this case: A declarative manifest describes the desired state and is idempotent when reapplied.
- **D:** Incorrect for this question. ACR Tasks builds images in Azure on a commit or schedule without a local Docker host. It removes build-host drift but not image review. Why the correct answer wins: A declarative manifest describes the desired state and is idempotent when reapplied.

### Question 6 — C

Answer: Test end-to-end connectivity from inside the container to each dependency. Testing the path from inside the container proves DNS, egress, and firewall behavior that host-side tests cannot reproduce. Reaching a dependency from the pod or replica proves DNS, egress, and firewall paths together. Host-side tests can succeed while the container path fails. Local study-map skill 1.7 (Container Logs, Events, and Connectivity), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure container hosting documentation: https://learn.microsoft.com/en-us/azure/container-apps/

- **A:** Incorrect for this question. Readiness gates traffic until the app can serve it, and liveness restarts a wedged container. Wrong thresholds cause restart loops. Why the correct answer wins: Testing the path from inside the container proves DNS, egress, and firewall behavior that host-side tests cannot reproduce.
- **B:** Incorrect for this question. Platform logs and metrics must be routed before they can be queried or alerted on. Retention and cost follow the workspace settings. Why the correct answer wins: Testing the path from inside the container proves DNS, egress, and firewall behavior that host-side tests cannot reproduce.
- **C:** Correct. Reaching a dependency from the pod or replica proves DNS, egress, and firewall paths together. Host-side tests can succeed while the container path fails. In this case: Testing the path from inside the container proves DNS, egress, and firewall behavior that host-side tests cannot reproduce.
- **D:** Incorrect for this question. Container Apps and AKS surface stdout logs and platform events into a workspace for KQL analysis. Verbosity and retention cost money. Why the correct answer wins: Testing the path from inside the container proves DNS, egress, and firewall behavior that host-side tests cannot reproduce.

### Question 7 — A, E

Answers: Build and store versioned images in Azure Container Registry; Apply an ACR retention policy to prune old untagged manifests. Versioned tags provide traceable artifacts, and a retention policy prunes stale manifests so storage does not grow without bound. ACR keeps tagged, versioned images next to the deployment target and supports identity-based pulls. Tagging strategy and retention still need a decision. A retention policy controls storage growth and registry clutter. It does not change which image tag a deployment references. Local study-map skill 1.1 (Container Image Lifecycle in Azure Container Registry), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure container hosting documentation: https://learn.microsoft.com/en-us/azure/container-apps/

- **A:** Correct. ACR keeps tagged, versioned images next to the deployment target and supports identity-based pulls. Tagging strategy and retention still need a decision. In this case: Versioned tags provide traceable artifacts, and a retention policy prunes stale manifests so storage does not grow without bound.
- **B:** Incorrect for this question. Geo-replication reduces cross-region pull latency and gives a local copy during a regional failure. It adds cost and replication management. Why the correct answer wins: Versioned tags provide traceable artifacts, and a retention policy prunes stale manifests so storage does not grow without bound.
- **C:** Incorrect for this question. A floating tag removes the link between a deployed revision and a specific build, so rollback and audit become guesswork. Why the correct answer wins: Versioned tags provide traceable artifacts, and a retention policy prunes stale manifests so storage does not grow without bound.
- **D:** Incorrect for this question. A slot swap warms the new version before it takes production traffic and makes rollback a second swap. Slot-local settings must be marked sticky. Why the correct answer wins: Versioned tags provide traceable artifacts, and a retention policy prunes stale manifests so storage does not grow without bound.
- **E:** Correct. A retention policy controls storage growth and registry clutter. It does not change which image tag a deployment references. In this case: Versioned tags provide traceable artifacts, and a retention policy prunes stale manifests so storage does not grow without bound.

### Question 8 — A, E

Answers: Apply a declarative Kubernetes manifest to the cluster; Add readiness and liveness probes to the pod specification. An applied manifest makes the desired state repeatable, and a readiness probe holds traffic until the app is actually serviceable. A manifest declares the desired deployment, service, and probe configuration in version control. Applying it repeatedly is idempotent. Readiness gates traffic until the app can serve it, and liveness restarts a wedged container. Wrong thresholds cause restart loops. Local study-map skill 1.6 (AKS Deployment with Manifests), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure container hosting documentation: https://learn.microsoft.com/en-us/azure/container-apps/

- **A:** Correct. A manifest declares the desired deployment, service, and probe configuration in version control. Applying it repeatedly is idempotent. In this case: An applied manifest makes the desired state repeatable, and a readiness probe holds traffic until the app is actually serviceable.
- **B:** Incorrect for this question. Container Instances starts a single container group quickly for short tasks. It has no orchestrator-level scaling or revision model. Why the correct answer wins: An applied manifest makes the desired state repeatable, and a readiness probe holds traffic until the app is actually serviceable.
- **C:** Incorrect for this question. CPU-based scaling reacts after work is already queued and cannot scale to zero on an empty queue. It suits steady request-driven services. Why the correct answer wins: An applied manifest makes the desired state repeatable, and a readiness probe holds traffic until the app is actually serviceable.
- **D:** Incorrect for this question. HPA adjusts replicas from resource metrics but needs metrics-server and enough node capacity. It cannot scale to zero. Why the correct answer wins: An applied manifest makes the desired state repeatable, and a readiness probe holds traffic until the app is actually serviceable.
- **E:** Correct. Readiness gates traffic until the app can serve it, and liveness restarts a wedged container. Wrong thresholds cause restart loops. In this case: An applied manifest makes the desired state repeatable, and a readiness probe holds traffic until the app is actually serviceable.

### Question 9 — D

Answer: Build and push the image → deploy a new revision → shift a small traffic percentage → check metrics → promote or roll back. The image must exist before the revision, the revision before traffic, and metrics before promotion. A canary revision accepts a small share of traffic so metrics decide promotion rather than optimism. Local study-map skill 1.5 (Event-Driven Scaling with KEDA), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure container hosting documentation: https://learn.microsoft.com/en-us/azure/container-apps/

- **A:** Incorrect for this question. Full traffic cannot move to a revision that does not exist yet, and the image must exist before the revision. Why the correct answer wins: The image must exist before the revision, the revision before traffic, and metrics before promotion.
- **B:** Incorrect for this question. Building after traffic is shifted means the running revision has no reviewed artifact behind it. Why the correct answer wins: The image must exist before the revision, the revision before traffic, and metrics before promotion.
- **C:** Incorrect for this question. Metrics cannot be checked before the revision serves traffic. Why the correct answer wins: The image must exist before the revision, the revision before traffic, and metrics before promotion.
- **D:** Correct. A canary revision accepts a small share of traffic so metrics decide promotion rather than optimism. In this case: The image must exist before the revision, the revision before traffic, and metrics before promotion.

### Question 10 — A

Answer: Include the partition key in the query predicate. Including the partition key makes the query a single-partition read instead of fanning out across partitions. A point or single-partition query avoids fan-out across partitions. Cross-partition queries consume more RUs and add latency. Local study-map skill 2.1 (Cosmos DB SDK Access and Queries), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Cosmos DB and PostgreSQL vector documentation: https://learn.microsoft.com/en-us/azure/cosmos-db/

- **A:** Correct. A point or single-partition query avoids fan-out across partitions. Cross-partition queries consume more RUs and add latency. In this case: Including the partition key makes the query a single-partition read instead of fanning out across partitions.
- **B:** Incorrect for this question. Request units measure the work a query performs, so tuning the query is often cheaper than adding throughput. Monitor normalized RU consumption. Why the correct answer wins: Including the partition key makes the query a single-partition read instead of fanning out across partitions.
- **C:** Incorrect for this question. A good partition key distributes storage and throughput and keeps common queries single-partition. Low cardinality creates hot partitions. Why the correct answer wins: Including the partition key makes the query a single-partition read instead of fanning out across partitions.
- **D:** Incorrect for this question. Indexing everything is simple and makes ad hoc queries possible, at higher write cost and storage. It is a default, not an optimization. Why the correct answer wins: Including the partition key makes the query a single-partition read instead of fanning out across partitions.

### Question 11 — A

Answer: Restrict the indexing policy to the paths the queries use. Restricting the indexing policy to queried paths reduces write RU charge and storage. Selective indexing cuts write RU charge and storage for unused paths. Excluded paths cannot be filtered efficiently later. Local study-map skill 2.2 (Cosmos DB Indexing Policies and Request Units), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Cosmos DB and PostgreSQL vector documentation: https://learn.microsoft.com/en-us/azure/cosmos-db/

- **A:** Correct. Selective indexing cuts write RU charge and storage for unused paths. Excluded paths cannot be filtered efficiently later. In this case: Restricting the indexing policy to queried paths reduces write RU charge and storage.
- **B:** Incorrect for this question. Autoscale follows demand between a minimum and maximum, avoiding throttling at peak without paying for peak all day. The maximum still caps the bill. Why the correct answer wins: Restricting the indexing policy to queried paths reduces write RU charge and storage.
- **C:** Incorrect for this question. Indexing everything is simple and makes ad hoc queries possible, at higher write cost and storage. It is a default, not an optimization. Why the correct answer wins: Restricting the indexing policy to queried paths reduces write RU charge and storage.
- **D:** Incorrect for this question. Consistency trades freshness against latency, availability, and RU cost. The level is set at the account and can be relaxed per request. Why the correct answer wins: Restricting the indexing policy to queried paths reduces write RU charge and storage.

### Question 12 — B

Answer: Use session consistency for reads within the same client session. Session consistency guarantees monotonic reads within a client session at far lower cost than strong consistency. Session consistency guarantees monotonic reads for one session and is the common default for user-facing apps. It does not promise global freshness. Local study-map skill 2.3 (Cosmos DB Consistency Levels), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Cosmos DB and PostgreSQL vector documentation: https://learn.microsoft.com/en-us/azure/cosmos-db/

- **A:** Incorrect for this question. Eventual consistency is the cheapest and most available option but returns possibly stale data. It fits non-critical counters, not balances. Why the correct answer wins: Session consistency guarantees monotonic reads within a client session at far lower cost than strong consistency.
- **B:** Correct. Session consistency guarantees monotonic reads for one session and is the common default for user-facing apps. It does not promise global freshness. In this case: Session consistency guarantees monotonic reads within a client session at far lower cost than strong consistency.
- **C:** Incorrect for this question. Consistency trades freshness against latency, availability, and RU cost. The level is set at the account and can be relaxed per request. Why the correct answer wins: Session consistency guarantees monotonic reads within a client session at far lower cost than strong consistency.
- **D:** Incorrect for this question. Strong consistency guarantees the latest committed write globally at the cost of higher latency and reduced availability during partitions. Why the correct answer wins: Session consistency guarantees monotonic reads within a client session at far lower cost than strong consistency.

### Question 13 — B

Answer: Store embeddings in a vector property and query with VectorDistance. A vector property plus the distance function keeps embeddings and metadata in the same container and query. Cosmos DB for NoSQL supports vector properties and a distance function for similarity search in the same document store. Dimensions and index type must match the model. Local study-map skill 2.4 (Cosmos DB Vector Search and Embeddings), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Cosmos DB and PostgreSQL vector documentation: https://learn.microsoft.com/en-us/azure/cosmos-db/

- **A:** Incorrect for this question. DiskANN trades some recall for memory efficiency on large sets. Recall and latency should be measured on representative queries. Why the correct answer wins: A vector property plus the distance function keeps embeddings and metadata in the same container and query.
- **B:** Correct. Cosmos DB for NoSQL supports vector properties and a distance function for similarity search in the same document store. Dimensions and index type must match the model. In this case: A vector property plus the distance function keeps embeddings and metadata in the same container and query.
- **C:** Incorrect for this question. Application-side scoring works for tiny collections and tests, but it moves all data over the wire and does not scale with corpus size. Why the correct answer wins: A vector property plus the distance function keeps embeddings and metadata in the same container and query.
- **D:** Incorrect for this question. pgvector keeps vectors beside relational data, so filters and joins run in one query. Index type and parameter tuning decide latency. Why the correct answer wins: A vector property plus the distance function keeps embeddings and metadata in the same container and query.

### Question 14 — A

Answer: Run a change feed processor to react to new and updated items. A change feed processor streams inserts and updates in order per partition for downstream work. The change feed delivers an ordered stream of changes per partition for downstream processing. It is not a delete feed, so deletions need a workaround. Local study-map skill 2.5 (Cosmos DB Change Feed Processing), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Cosmos DB and PostgreSQL vector documentation: https://learn.microsoft.com/en-us/azure/cosmos-db/

- **A:** Correct. The change feed delivers an ordered stream of changes per partition for downstream processing. It is not a delete feed, so deletions need a workaround. In this case: A change feed processor streams inserts and updates in order per partition for downstream work.
- **B:** Incorrect for this question. Leases track partition ownership so multiple processor instances share work and resume from a continuation token. Lease writes consume RUs too. Why the correct answer wins: A change feed processor streams inserts and updates in order per partition for downstream work.
- **C:** Incorrect for this question. A duplicate-detection window drops repeated sends within the window, which helps with at-least-once producers. The window is time-bounded. Why the correct answer wins: A change feed processor streams inserts and updates in order per partition for downstream work.
- **D:** Incorrect for this question. Event Grid delivers discrete notifications to subscribers with retries and filtering. It carries events, not large payloads or ordered streams. Why the correct answer wins: A change feed processor streams inserts and updates in order per partition for downstream work.

### Question 15 — D

Answer: Model typed columns for filters and one vector column for the embedding. Typed columns for the filter fields beside one vector column keep filters fast and the embedding contract explicit. Explicit types keep filters fast and make the embedding contract clear. Storing vectors as text defeats index use. Local study-map skill 2.6 (PostgreSQL Connection and Schema Modeling), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Cosmos DB and PostgreSQL vector documentation: https://learn.microsoft.com/en-us/azure/cosmos-db/

- **A:** Incorrect for this question. Vector indexes are memory-hungry, so undersized compute causes swapping and slow queries. Right-size before tuning index parameters. Why the correct answer wins: Typed columns for the filter fields beside one vector column keep filters fast and the embedding contract explicit.
- **B:** Incorrect for this question. A replica offloads read traffic but introduces replication lag, which is dangerous for freshly written evidence. It does not reduce index memory pressure. Why the correct answer wins: Typed columns for the filter fields beside one vector column keep filters fast and the embedding contract explicit.
- **C:** Incorrect for this question. Index creation and bulk loads are I/O heavy, and throttled storage stretches maintenance windows. Storage limits are separate from compute. Why the correct answer wins: Typed columns for the filter fields beside one vector column keep filters fast and the embedding contract explicit.
- **D:** Correct. Explicit types keep filters fast and make the embedding contract clear. Storing vectors as text defeats index use. In this case: Typed columns for the filter fields beside one vector column keep filters fast and the embedding contract explicit.

### Question 16 — A

Answer: Create an HNSW index for low-latency approximate search. HNSW gives low-latency approximate search and lets recall be tuned at query time. HNSW gives fast approximate nearest-neighbour queries with a larger memory footprint and slower builds. Recall is tunable at query time. Local study-map skill 2.7 (pgvector Indexing and Query Latency), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Cosmos DB and PostgreSQL vector documentation: https://learn.microsoft.com/en-us/azure/cosmos-db/

- **A:** Correct. HNSW gives fast approximate nearest-neighbour queries with a larger memory footprint and slower builds. Recall is tunable at query time. In this case: HNSW gives low-latency approximate search and lets recall be tuned at query time.
- **B:** Incorrect for this question. An external pooler multiplexes server connections for serverless or highly concurrent clients. Session-level features may be unavailable in transaction mode. Why the correct answer wins: HNSW gives low-latency approximate search and lets recall be tuned at query time.
- **C:** Incorrect for this question. IVFFlat uses clustering lists and needs periodic rebuilds as data grows, but costs less memory than HNSW. Probes trade recall for speed. Why the correct answer wins: HNSW gives low-latency approximate search and lets recall be tuned at query time.
- **D:** Incorrect for this question. An exact scan is accurate but scales linearly and burns compute. It is a baseline for measuring recall, not a production strategy. Why the correct answer wins: HNSW gives low-latency approximate search and lets recall be tuned at query time.

### Question 17 — A

Answer: Cache responses in Azure Managed Redis. Caching the computed block in Managed Redis avoids repeating the same work for each request. A cache absorbs repeated reads and cuts latency for hot data. Cache keys, TTLs, and invalidation must match the freshness requirement. Local study-map skill 2.11 (Azure Managed Redis Caching and Invalidation), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Cosmos DB and PostgreSQL vector documentation: https://learn.microsoft.com/en-us/azure/cosmos-db/

- **A:** Correct. A cache absorbs repeated reads and cuts latency for hot data. Cache keys, TTLs, and invalidation must match the freshness requirement. In this case: Caching the computed block in Managed Redis avoids repeating the same work for each request.
- **B:** Incorrect for this question. A replica offloads read traffic but introduces replication lag, which is dangerous for freshly written evidence. It does not reduce index memory pressure. Why the correct answer wins: Caching the computed block in Managed Redis avoids repeating the same work for each request.
- **C:** Incorrect for this question. A TTL bounds staleness and reclaims memory without a manual sweep. Too long a TTL hides source changes; too short wastes the cache. Why the correct answer wins: Caching the computed block in Managed Redis avoids repeating the same work for each request.
- **D:** Incorrect for this question. Queue Storage is simple and cheap for large backlogs with at-least-once delivery. It lacks topics, sessions, and scheduled messages. Why the correct answer wins: Caching the computed block in Managed Redis avoids repeating the same work for each request.

### Question 18 — D

Answer: Reuse a bounded connection pool instead of opening a connection per request. A bounded connection pool reuses established connections and protects the server from connection storms. A bounded pool amortizes connection setup and protects the server from connection storms. Pool size must match server limits. Local study-map skill 2.10 (PostgreSQL Connection Optimization), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Cosmos DB and PostgreSQL vector documentation: https://learn.microsoft.com/en-us/azure/cosmos-db/

- **A:** Incorrect for this question. A replica offloads read traffic but introduces replication lag, which is dangerous for freshly written evidence. It does not reduce index memory pressure. Why the correct answer wins: A bounded connection pool reuses established connections and protects the server from connection storms.
- **B:** Incorrect for this question. An external pooler multiplexes server connections for serverless or highly concurrent clients. Session-level features may be unavailable in transaction mode. Why the correct answer wins: A bounded connection pool reuses established connections and protects the server from connection storms.
- **C:** Incorrect for this question. Prepared statements avoid repeated planning and reduce chatty network calls. They pair well with pooling but can interact with pool modes. Why the correct answer wins: A bounded connection pool reuses established connections and protects the server from connection storms.
- **D:** Correct. A bounded pool amortizes connection setup and protects the server from connection storms. Pool size must match server limits. In this case: A bounded connection pool reuses established connections and protects the server from connection storms.

### Question 19 — B, D

Answers: Query through the Cosmos DB SDK with parameterized queries; Use a lease container to coordinate change feed readers. SDK queries keep the client on the supported path, and a lease container coordinates change feed ownership. SDK queries keep the client on the supported data plane and parameterization avoids injection and plan churn. Cross-partition queries still cost more. Leases track partition ownership so multiple processor instances share work and resume from a continuation token. Lease writes consume RUs too. Local study-map skill 2.1 (Cosmos DB SDK Access and Queries), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Cosmos DB and PostgreSQL vector documentation: https://learn.microsoft.com/en-us/azure/cosmos-db/

- **A:** Incorrect for this question. Indexing everything is simple and makes ad hoc queries possible, at higher write cost and storage. It is a default, not an optimization. Why the correct answer wins: SDK queries keep the client on the supported path, and a lease container coordinates change feed ownership.
- **B:** Correct. Leases track partition ownership so multiple processor instances share work and resume from a continuation token. Lease writes consume RUs too. In this case: SDK queries keep the client on the supported path, and a lease container coordinates change feed ownership.
- **C:** Incorrect for this question. A duplicate-detection window drops repeated sends within the window, which helps with at-least-once producers. The window is time-bounded. Why the correct answer wins: SDK queries keep the client on the supported path, and a lease container coordinates change feed ownership.
- **D:** Correct. SDK queries keep the client on the supported data plane and parameterization avoids injection and plan churn. Cross-partition queries still cost more. In this case: SDK queries keep the client on the supported path, and a lease container coordinates change feed ownership.
- **E:** Incorrect for this question. Autoscale follows demand between a minimum and maximum, avoiding throttling at peak without paying for peak all day. The maximum still caps the bill. Why the correct answer wins: SDK queries keep the client on the supported path, and a lease container coordinates change feed ownership.

### Question 20 — D, E

Answers: Reuse a bounded connection pool instead of opening a connection per request; Place a connection pooler in front of PostgreSQL for many short-lived clients. A bounded pool caps per-instance connections, and an external pooler multiplexes many clients onto fewer server connections. A bounded pool amortizes connection setup and protects the server from connection storms. Pool size must match server limits. An external pooler multiplexes server connections for serverless or highly concurrent clients. Session-level features may be unavailable in transaction mode. Local study-map skill 2.10 (PostgreSQL Connection Optimization), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Cosmos DB and PostgreSQL vector documentation: https://learn.microsoft.com/en-us/azure/cosmos-db/

- **A:** Incorrect for this question. Prepared statements avoid repeated planning and reduce chatty network calls. They pair well with pooling but can interact with pool modes. Why the correct answer wins: A bounded pool caps per-instance connections, and an external pooler multiplexes many clients onto fewer server connections.
- **B:** Incorrect for this question. A replica offloads read traffic but introduces replication lag, which is dangerous for freshly written evidence. It does not reduce index memory pressure. Why the correct answer wins: A bounded pool caps per-instance connections, and an external pooler multiplexes many clients onto fewer server connections.
- **C:** Incorrect for this question. Index creation and bulk loads are I/O heavy, and throttled storage stretches maintenance windows. Storage limits are separate from compute. Why the correct answer wins: A bounded pool caps per-instance connections, and an external pooler multiplexes many clients onto fewer server connections.
- **D:** Correct. A bounded pool amortizes connection setup and protects the server from connection storms. Pool size must match server limits. In this case: A bounded pool caps per-instance connections, and an external pooler multiplexes many clients onto fewer server connections.
- **E:** Correct. An external pooler multiplexes server connections for serverless or highly concurrent clients. Session-level features may be unavailable in transaction mode. In this case: A bounded pool caps per-instance connections, and an external pooler multiplexes many clients onto fewer server connections.

### Question 21 — B

Answer: Create the vector extension → create the table with a vector column → build the index → query nearest neighbours with a distance operator. The extension and table must exist before the index, and the index before efficient queries. The extension and typed column must exist before an index can be built, and the index before the query is efficient. Local study-map skill 2.7 (pgvector Indexing and Query Latency), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Cosmos DB and PostgreSQL vector documentation: https://learn.microsoft.com/en-us/azure/cosmos-db/

- **A:** Incorrect for this question. An index cannot be built before the extension and the table exist. Why the correct answer wins: The extension and table must exist before the index, and the index before efficient queries.
- **B:** Correct. The extension and typed column must exist before an index can be built, and the index before the query is efficient. In this case: The extension and table must exist before the index, and the index before efficient queries.
- **C:** Incorrect for this question. Querying before the schema exists cannot succeed, and the index cannot precede the table. Why the correct answer wins: The extension and table must exist before the index, and the index before efficient queries.
- **D:** Incorrect for this question. The extension is required for the vector type, and the query should follow index creation for usable latency. Why the correct answer wins: The extension and table must exist before the index, and the index before efficient queries.

### Question 22 — C

Answer: Use Service Bus sessions to keep related messages ordered. Sessions give exclusive, ordered processing per session ID across competing consumers. Sessions give ordered, exclusive processing per session ID across competing consumers. They require session-aware senders and receivers. Local study-map skill 3.1 (Service Bus Queues and Sessions), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure messaging and Functions documentation: https://learn.microsoft.com/en-us/azure/service-bus-messaging/

- **A:** Incorrect for this question. A duplicate-detection window drops repeated sends within the window, which helps with at-least-once producers. The window is time-bounded. Why the correct answer wins: Sessions give exclusive, ordered processing per session ID across competing consumers.
- **B:** Incorrect for this question. Peek-lock keeps the message locked until the handler completes it, giving at-least-once processing with retry. Lock duration must exceed processing time. Why the correct answer wins: Sessions give exclusive, ordered processing per session ID across competing consumers.
- **C:** Correct. Sessions give ordered, exclusive processing per session ID across competing consumers. They require session-aware senders and receivers. In this case: Sessions give exclusive, ordered processing per session ID across competing consumers.
- **D:** Incorrect for this question. A delivery cap stops infinite retries of a failing message and moves it to the dead-letter queue. The cap must exceed legitimate transient retries. Why the correct answer wins: Sessions give exclusive, ordered processing per session ID across competing consumers.

### Question 23 — B

Answer: Add a SQL or correlation filter to a subscription. A subscription filter evaluates message properties broker-side so only matching messages are delivered. Subscription filters route only matching messages to a handler, reducing wasted processing. Filter evaluation happens broker-side on message properties. Local study-map skill 3.2 (Service Bus Topics, Subscriptions, and Filters), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure messaging and Functions documentation: https://learn.microsoft.com/en-us/azure/service-bus-messaging/

- **A:** Incorrect for this question. A custom schema fits domain events that are not resource lifecycle notifications. Consumers must version the schema contract. Why the correct answer wins: A subscription filter evaluates message properties broker-side so only matching messages are delivered.
- **B:** Correct. Subscription filters route only matching messages to a handler, reducing wasted processing. Filter evaluation happens broker-side on message properties. In this case: A subscription filter evaluates message properties broker-side so only matching messages are delivered.
- **C:** Incorrect for this question. Subject and event-type filters keep handlers focused and reduce cost. Filters are evaluated on event metadata, not payload body. Why the correct answer wins: A subscription filter evaluates message properties broker-side so only matching messages are delivered.
- **D:** Incorrect for this question. A duplicate-detection window drops repeated sends within the window, which helps with at-least-once producers. The window is time-bounded. Why the correct answer wins: A subscription filter evaluates message properties broker-side so only matching messages are delivered.

### Question 24 — A

Answer: Set a maximum delivery count and handle the dead-letter path. A maximum delivery count moves a persistently failing message to the dead-letter queue after a bounded number of attempts. A delivery cap stops infinite retries of a failing message and moves it to the dead-letter queue. The cap must exceed legitimate transient retries. Local study-map skill 3.3 (Service Bus Dead-Lettering and Retries), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure messaging and Functions documentation: https://learn.microsoft.com/en-us/azure/service-bus-messaging/

- **A:** Correct. A delivery cap stops infinite retries of a failing message and moves it to the dead-letter queue. The cap must exceed legitimate transient retries. In this case: A maximum delivery count moves a persistently failing message to the dead-letter queue after a bounded number of attempts.
- **B:** Incorrect for this question. A duplicate-detection window drops repeated sends within the window, which helps with at-least-once producers. The window is time-bounded. Why the correct answer wins: A maximum delivery count moves a persistently failing message to the dead-letter queue after a bounded number of attempts.
- **C:** Incorrect for this question. Dead-lettering preserves poison messages for diagnosis instead of losing them. Resubmission needs a fix and an idempotent handler. Why the correct answer wins: A maximum delivery count moves a persistently failing message to the dead-letter queue after a bounded number of attempts.
- **D:** Incorrect for this question. Peek-lock keeps the message locked until the handler completes it, giving at-least-once processing with retry. Lock duration must exceed processing time. Why the correct answer wins: A maximum delivery count moves a persistently failing message to the dead-letter queue after a bounded number of attempts.

### Question 25 — B

Answer: Make the handler idempotent by using a message or business key. An idempotency key in the data store makes a replayed message a no-op instead of a duplicate write. At-least-once delivery means duplicates will happen, so the write must tolerate replay. A stored key makes the retry safe. Local study-map skill 3.3 (Service Bus Dead-Lettering and Retries), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure messaging and Functions documentation: https://learn.microsoft.com/en-us/azure/service-bus-messaging/

- **A:** Incorrect for this question. Prepared statements avoid repeated planning and reduce chatty network calls. They pair well with pooling but can interact with pool modes. Why the correct answer wins: An idempotency key in the data store makes a replayed message a no-op instead of a duplicate write.
- **B:** Correct. At-least-once delivery means duplicates will happen, so the write must tolerate replay. A stored key makes the retry safe. In this case: An idempotency key in the data store makes a replayed message a no-op instead of a duplicate write.
- **C:** Incorrect for this question. Durable Functions provides orchestrations, activities, timers, and retries with checkpointed state. Orchestrator code must stay deterministic. Why the correct answer wins: An idempotency key in the data store makes a replayed message a no-op instead of a duplicate write.
- **D:** Incorrect for this question. Receive-and-delete removes the message on delivery, so a crash loses work silently. It suits telemetry, not payments. Why the correct answer wins: An idempotency key in the data store makes a replayed message a no-op instead of a duplicate write.

### Question 26 — B

Answer: Filter the Event Grid subscription by subject or event type. Subject and event-type filters narrow delivery to the events the handler actually supports. Subject and event-type filters keep handlers focused and reduce cost. Filters are evaluated on event metadata, not payload body. Local study-map skill 3.4 (Event Grid Filters, Custom Events, and Retries), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure messaging and Functions documentation: https://learn.microsoft.com/en-us/azure/service-bus-messaging/

- **A:** Incorrect for this question. A trigger starts the function when work arrives and handles the receive loop for you. Poison-message behavior is configured in host settings. Why the correct answer wins: Subject and event-type filters narrow delivery to the events the handler actually supports.
- **B:** Correct. Subject and event-type filters keep handlers focused and reduce cost. Filters are evaluated on event metadata, not payload body. In this case: Subject and event-type filters narrow delivery to the events the handler actually supports.
- **C:** Incorrect for this question. A duplicate-detection window drops repeated sends within the window, which helps with at-least-once producers. The window is time-bounded. Why the correct answer wins: Subject and event-type filters narrow delivery to the events the handler actually supports.
- **D:** Incorrect for this question. Subscription filters route only matching messages to a handler, reducing wasted processing. Filter evaluation happens broker-side on message properties. Why the correct answer wins: Subject and event-type filters narrow delivery to the events the handler actually supports.

### Question 27 — A

Answer: Rely on Event Grid retries with a dead-letter destination. Event Grid retries failed deliveries and can dead-letter events that never succeed. Event Grid retries failed deliveries with backoff and can store undeliverable events. Handlers must still be idempotent. Local study-map skill 3.4 (Event Grid Filters, Custom Events, and Retries), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure messaging and Functions documentation: https://learn.microsoft.com/en-us/azure/service-bus-messaging/

- **A:** Correct. Event Grid retries failed deliveries with backoff and can store undeliverable events. Handlers must still be idempotent. In this case: Event Grid retries failed deliveries and can dead-letter events that never succeed.
- **B:** Incorrect for this question. Subject and event-type filters keep handlers focused and reduce cost. Filters are evaluated on event metadata, not payload body. Why the correct answer wins: Event Grid retries failed deliveries and can dead-letter events that never succeed.
- **C:** Incorrect for this question. Event Hubs ingests high-volume ordered streams with partitions and consumer groups. It is a streaming log, not a task queue. Why the correct answer wins: Event Grid retries failed deliveries and can dead-letter events that never succeed.
- **D:** Incorrect for this question. A custom schema fits domain events that are not resource lifecycle notifications. Consumers must version the schema contract. Why the correct answer wins: Event Grid retries failed deliveries and can dead-letter events that never succeed.

### Question 28 — C

Answer: Bind a queue or event trigger to the function. A queue trigger starts the function on arrival and manages the receive loop. A trigger starts the function when work arrives and handles the receive loop for you. Poison-message behavior is configured in host settings. Local study-map skill 3.5 (Azure Functions Triggers and Bindings), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure messaging and Functions documentation: https://learn.microsoft.com/en-us/azure/service-bus-messaging/

- **A:** Incorrect for this question. Bindings reduce boilerplate for common inputs and outputs and are configured declaratively. Complex operations still need the SDK. Why the correct answer wins: A queue trigger starts the function on arrival and manages the receive loop.
- **B:** Incorrect for this question. An HTTP trigger gives a synchronous API endpoint with route and authorization configuration. Long-running work should hand off to a queue. Why the correct answer wins: A queue trigger starts the function on arrival and manages the receive loop.
- **C:** Correct. A trigger starts the function when work arrives and handles the receive loop for you. Poison-message behavior is configured in host settings. In this case: A queue trigger starts the function on arrival and manages the receive loop.
- **D:** Incorrect for this question. Durable Functions provides orchestrations, activities, timers, and retries with checkpointed state. Orchestrator code must stay deterministic. Why the correct answer wins: A queue trigger starts the function on arrival and manages the receive loop.

### Question 29 — D

Answer: Host the function app on a premium plan with pre-warmed instances. A premium plan provides pre-warmed instances and virtual network integration. A premium plan reduces cold starts and supports virtual network integration and longer timeouts. It costs more than consumption. Local study-map skill 3.6 (Function App Configuration and Deployment), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure messaging and Functions documentation: https://learn.microsoft.com/en-us/azure/service-bus-messaging/

- **A:** Incorrect for this question. Durable Functions provides orchestrations, activities, timers, and retries with checkpointed state. Orchestrator code must stay deterministic. Why the correct answer wins: A premium plan provides pre-warmed instances and virtual network integration.
- **B:** Incorrect for this question. An HTTP trigger gives a synchronous API endpoint with route and authorization configuration. Long-running work should hand off to a queue. Why the correct answer wins: A premium plan provides pre-warmed instances and virtual network integration.
- **C:** Incorrect for this question. Consumption bills per execution and scales automatically, with cold starts and a timeout ceiling. It fits spiky, short work. Why the correct answer wins: A premium plan provides pre-warmed instances and virtual network integration.
- **D:** Correct. A premium plan reduces cold starts and supports virtual network integration and longer timeouts. It costs more than consumption. In this case: A premium plan provides pre-warmed instances and virtual network integration.

### Question 30 — D, E

Answers: Publish to a Service Bus topic with multiple subscriptions; Add a SQL or correlation filter to a subscription. A topic with separate subscriptions provides fan-out, and a subscription filter limits billing to matching messages. Topics fan out one message to independent subscribers, each with its own filter and dead-letter queue. Subscribers process at their own pace. Subscription filters route only matching messages to a handler, reducing wasted processing. Filter evaluation happens broker-side on message properties. Local study-map skill 3.2 (Service Bus Topics, Subscriptions, and Filters), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure messaging and Functions documentation: https://learn.microsoft.com/en-us/azure/service-bus-messaging/

- **A:** Incorrect for this question. Subject and event-type filters keep handlers focused and reduce cost. Filters are evaluated on event metadata, not payload body. Why the correct answer wins: A topic with separate subscriptions provides fan-out, and a subscription filter limits billing to matching messages.
- **B:** Incorrect for this question. A queue decouples producers from a single consumer group and smooths bursts. Delivery semantics depend on receive mode and completion. Why the correct answer wins: A topic with separate subscriptions provides fan-out, and a subscription filter limits billing to matching messages.
- **C:** Incorrect for this question. Queue Storage is simple and cheap for large backlogs with at-least-once delivery. It lacks topics, sessions, and scheduled messages. Why the correct answer wins: A topic with separate subscriptions provides fan-out, and a subscription filter limits billing to matching messages.
- **D:** Correct. Subscription filters route only matching messages to a handler, reducing wasted processing. Filter evaluation happens broker-side on message properties. In this case: A topic with separate subscriptions provides fan-out, and a subscription filter limits billing to matching messages.
- **E:** Correct. Topics fan out one message to independent subscribers, each with its own filter and dead-letter queue. Subscribers process at their own pace. In this case: A topic with separate subscriptions provides fan-out, and a subscription filter limits billing to matching messages.

### Question 31 — B, D

Answers: Inspect the dead-letter queue and resubmit corrected messages; Set a maximum delivery count and handle the dead-letter path. Dead-lettering preserves the failing message, and a delivery cap stops endless retries. Dead-lettering preserves poison messages for diagnosis instead of losing them. Resubmission needs a fix and an idempotent handler. A delivery cap stops infinite retries of a failing message and moves it to the dead-letter queue. The cap must exceed legitimate transient retries. Local study-map skill 3.3 (Service Bus Dead-Lettering and Retries), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure messaging and Functions documentation: https://learn.microsoft.com/en-us/azure/service-bus-messaging/

- **A:** Incorrect for this question. Prepared statements avoid repeated planning and reduce chatty network calls. They pair well with pooling but can interact with pool modes. Why the correct answer wins: Dead-lettering preserves the failing message, and a delivery cap stops endless retries.
- **B:** Correct. Dead-lettering preserves poison messages for diagnosis instead of losing them. Resubmission needs a fix and an idempotent handler. In this case: Dead-lettering preserves the failing message, and a delivery cap stops endless retries.
- **C:** Incorrect for this question. A duplicate-detection window drops repeated sends within the window, which helps with at-least-once producers. The window is time-bounded. Why the correct answer wins: Dead-lettering preserves the failing message, and a delivery cap stops endless retries.
- **D:** Correct. A delivery cap stops infinite retries of a failing message and moves it to the dead-letter queue. The cap must exceed legitimate transient retries. In this case: Dead-lettering preserves the failing message, and a delivery cap stops endless retries.
- **E:** Incorrect for this question. Receive-and-delete removes the message on delivery, so a crash loses work silently. It suits telemetry, not payments. Why the correct answer wins: Dead-lettering preserves the failing message, and a delivery cap stops endless retries.

### Question 32 — B, D

Answers: Define a custom event schema for the topic; Filter the Event Grid subscription by subject or event type. A custom event schema carries the domain payload, and a subscription filter routes it to the intended consumer. A custom schema fits domain events that are not resource lifecycle notifications. Consumers must version the schema contract. Subject and event-type filters keep handlers focused and reduce cost. Filters are evaluated on event metadata, not payload body. Local study-map skill 3.4 (Event Grid Filters, Custom Events, and Retries), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure messaging and Functions documentation: https://learn.microsoft.com/en-us/azure/service-bus-messaging/

- **A:** Incorrect for this question. Subscription filters route only matching messages to a handler, reducing wasted processing. Filter evaluation happens broker-side on message properties. Why the correct answer wins: A custom event schema carries the domain payload, and a subscription filter routes it to the intended consumer.
- **B:** Correct. A custom schema fits domain events that are not resource lifecycle notifications. Consumers must version the schema contract. In this case: A custom event schema carries the domain payload, and a subscription filter routes it to the intended consumer.
- **C:** Incorrect for this question. Event Grid retries failed deliveries with backoff and can store undeliverable events. Handlers must still be idempotent. Why the correct answer wins: A custom event schema carries the domain payload, and a subscription filter routes it to the intended consumer.
- **D:** Correct. Subject and event-type filters keep handlers focused and reduce cost. Filters are evaluated on event metadata, not payload body. In this case: A custom event schema carries the domain payload, and a subscription filter routes it to the intended consumer.
- **E:** Incorrect for this question. Event Hubs ingests high-volume ordered streams with partitions and consumer groups. It is a streaming log, not a task queue. Why the correct answer wins: A custom event schema carries the domain payload, and a subscription filter routes it to the intended consumer.

### Question 33 — C

Answer: Publish the message → receive with peek-lock → process the work → complete the message → dead-letter after the delivery limit. Peek-lock, processing, completion, and dead-lettering occur in that order. Peek-lock keeps the message until the handler succeeds, and only repeated failures should dead-letter it. Local study-map skill 3.1 (Service Bus Queues and Sessions), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure messaging and Functions documentation: https://learn.microsoft.com/en-us/azure/service-bus-messaging/

- **A:** Incorrect for this question. The message cannot be received before it is published, and completion must follow processing. Why the correct answer wins: Peek-lock, processing, completion, and dead-lettering occur in that order.
- **B:** Incorrect for this question. Work cannot be processed before the message is published and received. Why the correct answer wins: Peek-lock, processing, completion, and dead-lettering occur in that order.
- **C:** Correct. Peek-lock keeps the message until the handler succeeds, and only repeated failures should dead-letter it. In this case: Peek-lock, processing, completion, and dead-lettering occur in that order.
- **D:** Incorrect for this question. Completing a message before processing discards the work and defeats at-least-once delivery. Why the correct answer wins: Peek-lock, processing, completion, and dead-lettering occur in that order.

### Question 34 — C

Answer: Store the secret in Azure Key Vault and read it at runtime. Key Vault centralizes secret storage with role-based access and audit trails. A vault centralizes secret storage with access control and audit. Retrieval should use an identity, not a copied credential. Local study-map skill 4.1 (Key Vault Secret Storage, Rotation, and Retrieval), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Key Vault, App Configuration, and Monitor documentation: https://learn.microsoft.com/en-us/azure/azure-monitor/

- **A:** Incorrect for this question. Application settings become environment variables for the container and can be swapped per slot. Sensitive values should still reference a vault. Why the correct answer wins: Key Vault centralizes secret storage with role-based access and audit trails.
- **B:** Incorrect for this question. A scoped role grants only the operations the app performs and limits blast radius. Prefer built-in roles over broad contributor grants. Why the correct answer wins: Key Vault centralizes secret storage with role-based access and audit trails.
- **C:** Correct. A vault centralizes secret storage with access control and audit. Retrieval should use an identity, not a copied credential. In this case: Key Vault centralizes secret storage with role-based access and audit trails.
- **D:** Incorrect for this question. Pinning a version makes a rotation invisible to the app until it is redeployed, which is useful for break-glass and dangerous for routine rotation. Why the correct answer wins: Key Vault centralizes secret storage with role-based access and audit trails.

### Question 35 — C

Answer: Rotate the secret on a schedule and let apps resolve the current version. Scheduled rotation with current-version reads lets the app pick up the new secret on its next resolve. Rotation limits the value of a leaked secret, but callers must read the latest version rather than caching an old one forever. Local study-map skill 4.1 (Key Vault Secret Storage, Rotation, and Retrieval), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Key Vault, App Configuration, and Monitor documentation: https://learn.microsoft.com/en-us/azure/azure-monitor/

- **A:** Incorrect for this question. A managed identity issues tokens from the platform, removing secret distribution from the app. Role assignment still scopes what it can reach. Why the correct answer wins: Scheduled rotation with current-version reads lets the app pick up the new secret on its next resolve.
- **B:** Incorrect for this question. Application settings become environment variables for the container and can be swapped per slot. Sensitive values should still reference a vault. Why the correct answer wins: Scheduled rotation with current-version reads lets the app pick up the new secret on its next resolve.
- **C:** Correct. Rotation limits the value of a leaked secret, but callers must read the latest version rather than caching an old one forever. In this case: Scheduled rotation with current-version reads lets the app pick up the new secret on its next resolve.
- **D:** Incorrect for this question. Pinning a version makes a rotation invisible to the app until it is redeployed, which is useful for break-glass and dangerous for routine rotation. Why the correct answer wins: Scheduled rotation with current-version reads lets the app pick up the new secret on its next resolve.

### Question 36 — C

Answer: Store settings and feature flags in Azure App Configuration. App Configuration stores flags and settings with labels per environment and refresh support. App Configuration separates configuration from code and supports labels, feature flags, and Key Vault references. Change still needs a refresh strategy. Local study-map skill 4.2 (App Configuration Settings and Feature Flags), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Key Vault, App Configuration, and Monitor documentation: https://learn.microsoft.com/en-us/azure/azure-monitor/

- **A:** Incorrect for this question. Application settings become environment variables for the container and can be swapped per slot. Sensitive values should still reference a vault. Why the correct answer wins: App Configuration stores flags and settings with labels per environment and refresh support.
- **B:** Incorrect for this question. A vault centralizes secret storage with access control and audit. Retrieval should use an identity, not a copied credential. Why the correct answer wins: App Configuration stores flags and settings with labels per environment and refresh support.
- **C:** Correct. App Configuration separates configuration from code and supports labels, feature flags, and Key Vault references. Change still needs a refresh strategy. In this case: App Configuration stores flags and settings with labels per environment and refresh support.
- **D:** Incorrect for this question. Labels keep dev, test, and prod values in one store with one key schema. A misconfigured label selector silently serves the wrong values. Why the correct answer wins: App Configuration stores flags and settings with labels per environment and refresh support.

### Question 37 — D

Answer: Enable configuration refresh so changes apply without a restart. Configuration refresh is required for a running app to observe a changed value without a restart. Sentinel-key or polling refresh lets a running app pick up new settings. Refresh intervals trade responsiveness against request volume. Local study-map skill 4.2 (App Configuration Settings and Feature Flags), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Key Vault, App Configuration, and Monitor documentation: https://learn.microsoft.com/en-us/azure/azure-monitor/

- **A:** Incorrect for this question. Pipeline deployment keeps code and configuration versioned together and repeatable. Secrets belong in a vault reference, not in the pipeline file. Why the correct answer wins: Configuration refresh is required for a running app to observe a changed value without a restart.
- **B:** Incorrect for this question. Labels keep dev, test, and prod values in one store with one key schema. A misconfigured label selector silently serves the wrong values. Why the correct answer wins: Configuration refresh is required for a running app to observe a changed value without a restart.
- **C:** Incorrect for this question. Pinning a version makes a rotation invisible to the app until it is redeployed, which is useful for break-glass and dangerous for routine rotation. Why the correct answer wins: Configuration refresh is required for a running app to observe a changed value without a restart.
- **D:** Correct. Sentinel-key or polling refresh lets a running app pick up new settings. Refresh intervals trade responsiveness against request volume. In this case: Configuration refresh is required for a running app to observe a changed value without a restart.

### Question 38 — B

Answer: Instrument the service with the OpenTelemetry SDK. OpenTelemetry instrumentation with context propagation produces a single distributed trace across service boundaries. OpenTelemetry emits vendor-neutral traces, metrics, and logs with context propagation. Exporters and sampling decide what reaches the backend. Local study-map skill 4.3 (Distributed Tracing with OpenTelemetry), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Key Vault, App Configuration, and Monitor documentation: https://learn.microsoft.com/en-us/azure/azure-monitor/

- **A:** Incorrect for this question. KQL filters, projects, and aggregates log and metric tables in Log Analytics. Start narrow with a time range and a request ID. Why the correct answer wins: OpenTelemetry instrumentation with context propagation produces a single distributed trace across service boundaries.
- **B:** Correct. OpenTelemetry emits vendor-neutral traces, metrics, and logs with context propagation. Exporters and sampling decide what reaches the backend. In this case: OpenTelemetry instrumentation with context propagation produces a single distributed trace across service boundaries.
- **C:** Incorrect for this question. Platform logs and metrics must be routed before they can be queried or alerted on. Retention and cost follow the workspace settings. Why the correct answer wins: OpenTelemetry instrumentation with context propagation produces a single distributed trace across service boundaries.
- **D:** Incorrect for this question. Application Insights correlates requests, dependencies, and exceptions into end-to-end transactions. Sampling can hide rare failures. Why the correct answer wins: OpenTelemetry instrumentation with context propagation produces a single distributed trace across service boundaries.

### Question 39 — D

Answer: Aggregate with summarize and bin to see the failure rate over time. Binning with summarize produces a time series of failure rates, revealing spikes that averages hide. Time-binned aggregation reveals the shape of an incident: a step change, a ramp, or a periodic spike. Averages alone hide short outages. Local study-map skill 4.4 (KQL Queries for Logs and Metrics), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Key Vault, App Configuration, and Monitor documentation: https://learn.microsoft.com/en-us/azure/azure-monitor/

- **A:** Incorrect for this question. Joining request and dependency telemetry shows which downstream call fails inside a slow request. Cross-workspace joins need the right scope. Why the correct answer wins: Binning with summarize produces a time series of failure rates, revealing spikes that averages hide.
- **B:** Incorrect for this question. KQL filters, projects, and aggregates log and metric tables in Log Analytics. Start narrow with a time range and a request ID. Why the correct answer wins: Binning with summarize produces a time series of failure rates, revealing spikes that averages hide.
- **C:** Incorrect for this question. An alert turns a threshold breach into a notification or action. Thresholds need a baseline, or the alert is noise. Why the correct answer wins: Binning with summarize produces a time series of failure rates, revealing spikes that averages hide.
- **D:** Correct. Time-binned aggregation reveals the shape of an incident: a step change, a ramp, or a periodic spike. Averages alone hide short outages. In this case: Binning with summarize produces a time series of failure rates, revealing spikes that averages hide.

### Question 40 — B

Answer: Join the requests and dependencies tables on the operation ID. Joining requests to dependencies on the operation ID shows which downstream call consumed the time. Joining request and dependency telemetry shows which downstream call fails inside a slow request. Cross-workspace joins need the right scope. Local study-map skill 4.4 (KQL Queries for Logs and Metrics), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Key Vault, App Configuration, and Monitor documentation: https://learn.microsoft.com/en-us/azure/azure-monitor/

- **A:** Incorrect for this question. Application Insights correlates requests, dependencies, and exceptions into end-to-end transactions. Sampling can hide rare failures. Why the correct answer wins: Joining requests to dependencies on the operation ID shows which downstream call consumed the time.
- **B:** Correct. Joining request and dependency telemetry shows which downstream call fails inside a slow request. Cross-workspace joins need the right scope. In this case: Joining requests to dependencies on the operation ID shows which downstream call consumed the time.
- **C:** Incorrect for this question. Time-binned aggregation reveals the shape of an incident: a step change, a ramp, or a periodic spike. Averages alone hide short outages. Why the correct answer wins: Joining requests to dependencies on the operation ID shows which downstream call consumed the time.
- **D:** Incorrect for this question. An alert turns a threshold breach into a notification or action. Thresholds need a baseline, or the alert is noise. Why the correct answer wins: Joining requests to dependencies on the operation ID shows which downstream call consumed the time.

### Question 41 — B

Answer: Create an alert rule on the failure rate or latency metric. An alert rule on the latency metric converts a sustained threshold breach into a notification. An alert turns a threshold breach into a notification or action. Thresholds need a baseline, or the alert is noise. Local study-map skill 4.4 (KQL Queries for Logs and Metrics), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Key Vault, App Configuration, and Monitor documentation: https://learn.microsoft.com/en-us/azure/azure-monitor/

- **A:** Incorrect for this question. Platform logs and metrics must be routed before they can be queried or alerted on. Retention and cost follow the workspace settings. Why the correct answer wins: An alert rule on the latency metric converts a sustained threshold breach into a notification.
- **B:** Correct. An alert turns a threshold breach into a notification or action. Thresholds need a baseline, or the alert is noise. In this case: An alert rule on the latency metric converts a sustained threshold breach into a notification.
- **C:** Incorrect for this question. Application Insights correlates requests, dependencies, and exceptions into end-to-end transactions. Sampling can hide rare failures. Why the correct answer wins: An alert rule on the latency metric converts a sustained threshold breach into a notification.
- **D:** Incorrect for this question. Time-binned aggregation reveals the shape of an incident: a step change, a ramp, or a periodic spike. Averages alone hide short outages. Why the correct answer wins: An alert rule on the latency metric converts a sustained threshold breach into a notification.

### Question 42 — D

Answer: Authenticate with a managed identity instead of a stored key. A managed identity obtains tokens from the platform so no credential is stored in the image or settings. A managed identity issues tokens from the platform, removing secret distribution from the app. Role assignment still scopes what it can reach. Local study-map skill 4.5 (Identity-Based Access for Application Services), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Key Vault, App Configuration, and Monitor documentation: https://learn.microsoft.com/en-us/azure/azure-monitor/

- **A:** Incorrect for this question. A vault centralizes secret storage with access control and audit. Retrieval should use an identity, not a copied credential. Why the correct answer wins: A managed identity obtains tokens from the platform so no credential is stored in the image or settings.
- **B:** Incorrect for this question. A scoped role grants only the operations the app performs and limits blast radius. Prefer built-in roles over broad contributor grants. Why the correct answer wins: A managed identity obtains tokens from the platform so no credential is stored in the image or settings.
- **C:** Incorrect for this question. Application settings become environment variables for the container and can be swapped per slot. Sensitive values should still reference a vault. Why the correct answer wins: A managed identity obtains tokens from the platform so no credential is stored in the image or settings.
- **D:** Correct. A managed identity issues tokens from the platform, removing secret distribution from the app. Role assignment still scopes what it can reach. In this case: A managed identity obtains tokens from the platform so no credential is stored in the image or settings.

### Question 43 — B, D

Answers: Store the secret in Azure Key Vault and read it at runtime; Authenticate with a managed identity instead of a stored key. Storing the secret in Key Vault centralizes control, and a managed identity removes the need for a stored key to read it. A vault centralizes secret storage with access control and audit. Retrieval should use an identity, not a copied credential. A managed identity issues tokens from the platform, removing secret distribution from the app. Role assignment still scopes what it can reach. Local study-map skill 4.1 (Key Vault Secret Storage, Rotation, and Retrieval), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Key Vault, App Configuration, and Monitor documentation: https://learn.microsoft.com/en-us/azure/azure-monitor/

- **A:** Incorrect for this question. Rotation limits the value of a leaked secret, but callers must read the latest version rather than caching an old one forever. Why the correct answer wins: Storing the secret in Key Vault centralizes control, and a managed identity removes the need for a stored key to read it.
- **B:** Correct. A managed identity issues tokens from the platform, removing secret distribution from the app. Role assignment still scopes what it can reach. In this case: Storing the secret in Key Vault centralizes control, and a managed identity removes the need for a stored key to read it.
- **C:** Incorrect for this question. Application settings become environment variables for the container and can be swapped per slot. Sensitive values should still reference a vault. Why the correct answer wins: Storing the secret in Key Vault centralizes control, and a managed identity removes the need for a stored key to read it.
- **D:** Correct. A vault centralizes secret storage with access control and audit. Retrieval should use an identity, not a copied credential. In this case: Storing the secret in Key Vault centralizes control, and a managed identity removes the need for a stored key to read it.
- **E:** Incorrect for this question. Pinning a version makes a rotation invisible to the app until it is redeployed, which is useful for break-glass and dangerous for routine rotation. Why the correct answer wins: Storing the secret in Key Vault centralizes control, and a managed identity removes the need for a stored key to read it.

### Question 44 — C

Answer: Store the secret in Key Vault → grant the app identity access → reference the secret from the app → rotate the secret → the app reads the new version. The secret is stored, access granted, referenced, and then rotated, after which the app reads the current version. Access must be granted before the reference resolves, and the app must read the current version after rotation. Local study-map skill 4.1 (Key Vault Secret Storage, Rotation, and Retrieval), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Key Vault, App Configuration, and Monitor documentation: https://learn.microsoft.com/en-us/azure/azure-monitor/

- **A:** Incorrect for this question. Access can be granted first, but rotation cannot precede storing the secret. Why the correct answer wins: The secret is stored, access granted, referenced, and then rotated, after which the app reads the current version.
- **B:** Incorrect for this question. A reference cannot resolve before the secret and the access grant exist. Why the correct answer wins: The secret is stored, access granted, referenced, and then rotated, after which the app reads the current version.
- **C:** Correct. Access must be granted before the reference resolves, and the app must read the current version after rotation. In this case: The secret is stored, access granted, referenced, and then rotated, after which the app reads the current version.
- **D:** Incorrect for this question. There is nothing to rotate or reference before the secret is stored. Why the correct answer wins: The secret is stored, access granted, referenced, and then rotated, after which the app reads the current version.

### Question 45 — C

Answer: Deploy the image by digest instead of a mutable tag. A digest identifies immutable content, so a retagged rebuild cannot silently alter the image that production executes. A digest identifies immutable content, so the same bytes run in every environment. A tag can be reassigned later and silently change what deploys. Local study-map skill 1.1 (Container Image Lifecycle in Azure Container Registry), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure container hosting documentation: https://learn.microsoft.com/en-us/azure/container-apps/

- **A:** Incorrect for this question. A retention policy controls storage growth and registry clutter. It does not change which image tag a deployment references. Why the correct answer wins: A digest identifies immutable content, so a retagged rebuild cannot silently alter the image that production executes.
- **B:** Incorrect for this question. A slot swap warms the new version before it takes production traffic and makes rollback a second swap. Slot-local settings must be marked sticky. Why the correct answer wins: A digest identifies immutable content, so a retagged rebuild cannot silently alter the image that production executes.
- **C:** Correct. A digest identifies immutable content, so the same bytes run in every environment. A tag can be reassigned later and silently change what deploys. In this case: A digest identifies immutable content, so a retagged rebuild cannot silently alter the image that production executes.
- **D:** Incorrect for this question. A floating tag removes the link between a deployed revision and a specific build, so rollback and audit become guesswork. Why the correct answer wins: A digest identifies immutable content, so a retagged rebuild cannot silently alter the image that production executes.

### Question 46 — B

Answer: Run image builds on demand or on a trigger with ACR Tasks. ACR Tasks builds in Azure from a commit or schedule, so the build environment no longer depends on a local Docker host. ACR Tasks builds images in Azure on a commit or schedule without a local Docker host. It removes build-host drift but not image review. Local study-map skill 1.2 (Automated Image Builds with ACR Tasks), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure container hosting documentation: https://learn.microsoft.com/en-us/azure/container-apps/

- **A:** Incorrect for this question. ACR keeps tagged, versioned images next to the deployment target and supports identity-based pulls. Tagging strategy and retention still need a decision. Why the correct answer wins: ACR Tasks builds in Azure from a commit or schedule, so the build environment no longer depends on a local Docker host.
- **B:** Correct. ACR Tasks builds images in Azure on a commit or schedule without a local Docker host. It removes build-host drift but not image review. In this case: ACR Tasks builds in Azure from a commit or schedule, so the build environment no longer depends on a local Docker host.
- **C:** Incorrect for this question. AKS gives full Kubernetes control, including custom controllers and networking. You own node pools, upgrades, and manifest hygiene. Why the correct answer wins: ACR Tasks builds in Azure from a commit or schedule, so the build environment no longer depends on a local Docker host.
- **D:** Incorrect for this question. Container Apps provides a managed environment, revisions, and KEDA-based scaling without cluster administration. Platform limits differ from AKS. Why the correct answer wins: ACR Tasks builds in Azure from a commit or schedule, so the build environment no longer depends on a local Docker host.

### Question 47 — C

Answer: Configure Container Apps ingress for internal-only access. Internal ingress keeps the endpoint inside the environment network and off the public internet without changing authorization. Internal ingress keeps the endpoint inside the environment virtual network. It is an exposure control, not an authorization control. Local study-map skill 1.4 (Container Apps Deployment and Revisions), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure container hosting documentation: https://learn.microsoft.com/en-us/azure/container-apps/

- **A:** Incorrect for this question. A slot swap warms the new version before it takes production traffic and makes rollback a second swap. Slot-local settings must be marked sticky. Why the correct answer wins: Internal ingress keeps the endpoint inside the environment network and off the public internet without changing authorization.
- **B:** Incorrect for this question. Revision-based traffic splitting enables canary and blue-green releases. Revision mode and scale rules must be set deliberately. Why the correct answer wins: Internal ingress keeps the endpoint inside the environment network and off the public internet without changing authorization.
- **C:** Correct. Internal ingress keeps the endpoint inside the environment virtual network. It is an exposure control, not an authorization control. In this case: Internal ingress keeps the endpoint inside the environment network and off the public internet without changing authorization.
- **D:** Incorrect for this question. KEDA scalers drive replica count from queue length, lag, or other event metrics, including scale to zero. Cool-down and max replicas bound the behavior. Why the correct answer wins: Internal ingress keeps the endpoint inside the environment network and off the public internet without changing authorization.

### Question 48 — D

Answer: Scale on the Service Bus queue length with a KEDA Azure Service Bus scaler. A queue-length scaler adds consumers while messages are backed up and scales to zero once the queue drains. A queue-length scaler adds replicas while work is backed up and removes them when the queue drains. Message lock duration must exceed processing time. Local study-map skill 1.5 (Event-Driven Scaling with KEDA), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure container hosting documentation: https://learn.microsoft.com/en-us/azure/container-apps/

- **A:** Incorrect for this question. HPA adjusts replicas from resource metrics but needs metrics-server and enough node capacity. It cannot scale to zero. Why the correct answer wins: A queue-length scaler adds consumers while messages are backed up and scales to zero once the queue drains.
- **B:** Incorrect for this question. CPU-based scaling reacts after work is already queued and cannot scale to zero on an empty queue. It suits steady request-driven services. Why the correct answer wins: A queue-length scaler adds consumers while messages are backed up and scales to zero once the queue drains.
- **C:** Incorrect for this question. A warm minimum replica removes scale-to-zero cold starts for latency-critical endpoints. It keeps paying for idle capacity. Why the correct answer wins: A queue-length scaler adds consumers while messages are backed up and scales to zero once the queue drains.
- **D:** Correct. A queue-length scaler adds replicas while work is backed up and removes them when the queue drains. Message lock duration must exceed processing time. In this case: A queue-length scaler adds consumers while messages are backed up and scales to zero once the queue drains.

### Question 49 — B

Answer: Federate a Kubernetes service account to a managed identity. Federating a Kubernetes service account to a managed identity gives the pod an Azure token without any stored secret. Workload identity lets pods obtain tokens without stored secrets. Each workload should get its own identity and narrow role. Local study-map skill 1.6 (AKS Deployment with Manifests), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure container hosting documentation: https://learn.microsoft.com/en-us/azure/container-apps/

- **A:** Incorrect for this question. A Key Vault reference resolves at runtime so the secret is never written into application settings. The app identity still needs permission to read it. Why the correct answer wins: Federating a Kubernetes service account to a managed identity gives the pod an Azure token without any stored secret.
- **B:** Correct. Workload identity lets pods obtain tokens without stored secrets. Each workload should get its own identity and narrow role. In this case: Federating a Kubernetes service account to a managed identity gives the pod an Azure token without any stored secret.
- **C:** Incorrect for this question. A floating tag removes the link between a deployed revision and a specific build, so rollback and audit become guesswork. Why the correct answer wins: Federating a Kubernetes service account to a managed identity gives the pod an Azure token without any stored secret.
- **D:** Incorrect for this question. Geo-replication reduces cross-region pull latency and gives a local copy during a regional failure. It adds cost and replication management. Why the correct answer wins: Federating a Kubernetes service account to a managed identity gives the pod an Azure token without any stored secret.

### Question 50 — C

Answer: Link the private DNS zone so the private endpoint name resolves. A private endpoint name resolves only when the private DNS zone is linked to the virtual network that hosts the workload. A private endpoint needs matching name resolution or clients still resolve the public address. The zone must be linked to the workload network. Local study-map skill 1.7 (Container Logs, Events, and Connectivity), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure container hosting documentation: https://learn.microsoft.com/en-us/azure/container-apps/

- **A:** Incorrect for this question. Reaching a dependency from the pod or replica proves DNS, egress, and firewall paths together. Host-side tests can succeed while the container path fails. Why the correct answer wins: A private endpoint name resolves only when the private DNS zone is linked to the virtual network that hosts the workload.
- **B:** Incorrect for this question. KQL filters, projects, and aggregates log and metric tables in Log Analytics. Start narrow with a time range and a request ID. Why the correct answer wins: A private endpoint name resolves only when the private DNS zone is linked to the virtual network that hosts the workload.
- **C:** Correct. A private endpoint needs matching name resolution or clients still resolve the public address. The zone must be linked to the workload network. In this case: A private endpoint name resolves only when the private DNS zone is linked to the virtual network that hosts the workload.
- **D:** Incorrect for this question. Platform logs and metrics must be routed before they can be queried or alerted on. Retention and cost follow the workspace settings. Why the correct answer wins: A private endpoint name resolves only when the private DNS zone is linked to the virtual network that hosts the workload.

### Question 51 — D, E

Answers: Supply configuration through App Service application settings; Stage the change in a deployment slot and swap after verification. A staging slot warms and verifies the build before the swap, and slot-scoped settings keep the environment log level out of the swap. Application settings become environment variables for the container and can be swapped per slot. Sensitive values should still reference a vault. A slot swap warms the new version before it takes production traffic and makes rollback a second swap. Slot-local settings must be marked sticky. Local study-map skill 1.3 (Container Deployment to Azure App Service), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure container hosting documentation: https://learn.microsoft.com/en-us/azure/container-apps/

- **A:** Incorrect for this question. KEDA scalers drive replica count from queue length, lag, or other event metrics, including scale to zero. Cool-down and max replicas bound the behavior. Why the correct answer wins: A staging slot warms and verifies the build before the swap, and slot-scoped settings keep the environment log level out of the swap.
- **B:** Incorrect for this question. Revision-based traffic splitting enables canary and blue-green releases. Revision mode and scale rules must be set deliberately. Why the correct answer wins: A staging slot warms and verifies the build before the swap, and slot-scoped settings keep the environment log level out of the swap.
- **C:** Incorrect for this question. A manifest declares the desired deployment, service, and probe configuration in version control. Applying it repeatedly is idempotent. Why the correct answer wins: A staging slot warms and verifies the build before the swap, and slot-scoped settings keep the environment log level out of the swap.
- **D:** Correct. Application settings become environment variables for the container and can be swapped per slot. Sensitive values should still reference a vault. In this case: A staging slot warms and verifies the build before the swap, and slot-scoped settings keep the environment log level out of the swap.
- **E:** Correct. A slot swap warms the new version before it takes production traffic and makes rollback a second swap. Slot-local settings must be marked sticky. In this case: A staging slot warms and verifies the build before the swap, and slot-scoped settings keep the environment log level out of the swap.

### Question 52 — C

Answer: Set a minimum replica count above zero for the container app. A minimum replica count above zero keeps an instance warm, so the first request does not pay cold-start latency. A warm minimum replica removes scale-to-zero cold starts for latency-critical endpoints. It keeps paying for idle capacity. Local study-map skill 1.4 (Container Apps Deployment and Revisions), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure container hosting documentation: https://learn.microsoft.com/en-us/azure/container-apps/

- **A:** Incorrect for this question. CPU-based scaling reacts after work is already queued and cannot scale to zero on an empty queue. It suits steady request-driven services. Why the correct answer wins: A minimum replica count above zero keeps an instance warm, so the first request does not pay cold-start latency.
- **B:** Incorrect for this question. Revision-based traffic splitting enables canary and blue-green releases. Revision mode and scale rules must be set deliberately. Why the correct answer wins: A minimum replica count above zero keeps an instance warm, so the first request does not pay cold-start latency.
- **C:** Correct. A warm minimum replica removes scale-to-zero cold starts for latency-critical endpoints. It keeps paying for idle capacity. In this case: A minimum replica count above zero keeps an instance warm, so the first request does not pay cold-start latency.
- **D:** Incorrect for this question. KEDA scalers drive replica count from queue length, lag, or other event metrics, including scale to zero. Cool-down and max replicas bound the behavior. Why the correct answer wins: A minimum replica count above zero keeps an instance warm, so the first request does not pay cold-start latency.

### Question 53 — B

Answer: Deploy the container app with a minimum replica count → attach a KEDA scale rule that uses the workload identity → cap the maximum replicas → run a load test → confirm replicas grow and drain. The app and its scale rule must exist and be bounded before a load test can demonstrate scaling and drain. The app, the scale rule, and the bound must exist before a load test can prove the scaling behaviour. Local study-map skill 1.5 (Event-Driven Scaling with KEDA), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure container hosting documentation: https://learn.microsoft.com/en-us/azure/container-apps/

- **A:** Incorrect for this question. Verification cannot precede the deployment, the rule, and the test. Why the correct answer wins: The app and its scale rule must exist and be bounded before a load test can demonstrate scaling and drain.
- **B:** Correct. The app, the scale rule, and the bound must exist before a load test can prove the scaling behaviour. In this case: The app and its scale rule must exist and be bounded before a load test can demonstrate scaling and drain.
- **C:** Incorrect for this question. The load test would run against nothing configured to scale. Why the correct answer wins: The app and its scale rule must exist and be bounded before a load test can demonstrate scaling and drain.
- **D:** Incorrect for this question. A scale rule cannot be attached before the app exists, and the cap must exist before the test. Why the correct answer wins: The app and its scale rule must exist and be bounded before a load test can demonstrate scaling and drain.

### Question 54 — D

Answer: Replicate the registry to each deployment region. Geo-replication keeps a local registry copy in each region, which shortens the pull that every new replica performs. Geo-replication reduces cross-region pull latency and gives a local copy during a regional failure. It adds cost and replication management. Local study-map skill 1.2 (Automated Image Builds with ACR Tasks), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure container hosting documentation: https://learn.microsoft.com/en-us/azure/container-apps/

- **A:** Incorrect for this question. ACR Tasks builds images in Azure on a commit or schedule without a local Docker host. It removes build-host drift but not image review. Why the correct answer wins: Geo-replication keeps a local registry copy in each region, which shortens the pull that every new replica performs.
- **B:** Incorrect for this question. ACR keeps tagged, versioned images next to the deployment target and supports identity-based pulls. Tagging strategy and retention still need a decision. Why the correct answer wins: Geo-replication keeps a local registry copy in each region, which shortens the pull that every new replica performs.
- **C:** Incorrect for this question. A slot swap warms the new version before it takes production traffic and makes rollback a second swap. Slot-local settings must be marked sticky. Why the correct answer wins: Geo-replication keeps a local registry copy in each region, which shortens the pull that every new replica performs.
- **D:** Correct. Geo-replication reduces cross-region pull latency and gives a local copy during a regional failure. It adds cost and replication management. In this case: Geo-replication keeps a local registry copy in each region, which shortens the pull that every new replica performs.

### Question 55 — B

Answer: Tune the scale rule cool-down period and maximum replicas. A longer cool-down and a sensible maximum keep a noisy metric from thrashing the replica count. Cool-down prevents replica flapping, and a maximum replica cap bounds cost and downstream load. Both are per-rule settings. Local study-map skill 1.5 (Event-Driven Scaling with KEDA), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure container hosting documentation: https://learn.microsoft.com/en-us/azure/container-apps/

- **A:** Incorrect for this question. HPA adjusts replicas from resource metrics but needs metrics-server and enough node capacity. It cannot scale to zero. Why the correct answer wins: A longer cool-down and a sensible maximum keep a noisy metric from thrashing the replica count.
- **B:** Correct. Cool-down prevents replica flapping, and a maximum replica cap bounds cost and downstream load. Both are per-rule settings. In this case: A longer cool-down and a sensible maximum keep a noisy metric from thrashing the replica count.
- **C:** Incorrect for this question. KEDA scalers drive replica count from queue length, lag, or other event metrics, including scale to zero. Cool-down and max replicas bound the behavior. Why the correct answer wins: A longer cool-down and a sensible maximum keep a noisy metric from thrashing the replica count.
- **D:** Incorrect for this question. CPU-based scaling reacts after work is already queued and cannot scale to zero on an empty queue. It suits steady request-driven services. Why the correct answer wins: A longer cool-down and a sensible maximum keep a noisy metric from thrashing the replica count.

### Question 56 — C

Answer: Page large result sets with the continuation token. A continuation token fetches the next page without reordering the previous one, which bounds response size and charge per call. A continuation token returns the next page without re-sorting the previous one, which bounds response size and request charge per call. It is not a snapshot across pages. Local study-map skill 2.1 (Cosmos DB SDK Access and Queries), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Cosmos DB and PostgreSQL vector documentation: https://learn.microsoft.com/en-us/azure/cosmos-db/

- **A:** Incorrect for this question. SDK queries keep the client on the supported data plane and parameterization avoids injection and plan churn. Cross-partition queries still cost more. Why the correct answer wins: A continuation token fetches the next page without reordering the previous one, which bounds response size and charge per call.
- **B:** Incorrect for this question. Request units measure the work a query performs, so tuning the query is often cheaper than adding throughput. Monitor normalized RU consumption. Why the correct answer wins: A continuation token fetches the next page without reordering the previous one, which bounds response size and charge per call.
- **C:** Correct. A continuation token returns the next page without re-sorting the previous one, which bounds response size and request charge per call. It is not a snapshot across pages. In this case: A continuation token fetches the next page without reordering the previous one, which bounds response size and charge per call.
- **D:** Incorrect for this question. A point or single-partition query avoids fan-out across partitions. Cross-partition queries consume more RUs and add latency. Why the correct answer wins: A continuation token fetches the next page without reordering the previous one, which bounds response size and charge per call.

### Question 57 — B

Answer: Add a composite index for the filtered and ordered properties. A composite index serves the filter and the order together instead of sorting the matched documents at query time. A composite index lets a query filter and order on several paths without a runtime sort. It adds write cost for exactly those paths. Local study-map skill 2.2 (Cosmos DB Indexing Policies and Request Units), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Cosmos DB and PostgreSQL vector documentation: https://learn.microsoft.com/en-us/azure/cosmos-db/

- **A:** Incorrect for this question. Indexing everything is simple and makes ad hoc queries possible, at higher write cost and storage. It is a default, not an optimization. Why the correct answer wins: A composite index serves the filter and the order together instead of sorting the matched documents at query time.
- **B:** Correct. A composite index lets a query filter and order on several paths without a runtime sort. It adds write cost for exactly those paths. In this case: A composite index serves the filter and the order together instead of sorting the matched documents at query time.
- **C:** Incorrect for this question. Selective indexing cuts write RU charge and storage for unused paths. Excluded paths cannot be filtered efficiently later. Why the correct answer wins: A composite index serves the filter and the order together instead of sorting the matched documents at query time.
- **D:** Incorrect for this question. Autoscale follows demand between a minimum and maximum, avoiding throttling at peak without paying for peak all day. The maximum still caps the bill. Why the correct answer wins: A composite index serves the filter and the order together instead of sorting the matched documents at query time.

### Question 58 — B

Answer: Declare the embedding dimensions and vector index type on the container policy. The container vector policy declares the dimensions and index type, so a new model requires a matching policy and re-embedded items. The container vector policy fixes dimensions, distance function, and index type, so a model change requires a new policy. Mismatched dimensions fail at write time. Local study-map skill 2.4 (Cosmos DB Vector Search and Embeddings), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Cosmos DB and PostgreSQL vector documentation: https://learn.microsoft.com/en-us/azure/cosmos-db/

- **A:** Incorrect for this question. Cosmos DB for NoSQL supports vector properties and a distance function for similarity search in the same document store. Dimensions and index type must match the model. Why the correct answer wins: The container vector policy declares the dimensions and index type, so a new model requires a matching policy and re-embedded items.
- **B:** Correct. The container vector policy fixes dimensions, distance function, and index type, so a model change requires a new policy. Mismatched dimensions fail at write time. In this case: The container vector policy declares the dimensions and index type, so a new model requires a matching policy and re-embedded items.
- **C:** Incorrect for this question. Distance function choice must match the embedding model and the normalization used at indexing time. A mismatch degrades recall silently. Why the correct answer wins: The container vector policy declares the dimensions and index type, so a new model requires a matching policy and re-embedded items.
- **D:** Incorrect for this question. HNSW gives fast approximate nearest-neighbour queries with a larger memory footprint and slower builds. Recall is tunable at query time. Why the correct answer wins: The container vector policy declares the dimensions and index type, so a new model requires a matching policy and re-embedded items.

### Question 59 — D

Answer: Add a read replica and send all vector queries to it. A read replica takes the long scans off the primary and leaves vector lookups at their expected latency. A replica offloads read traffic but introduces replication lag, which is dangerous for freshly written evidence. It does not reduce index memory pressure. Local study-map skill 2.6 (PostgreSQL Connection and Schema Modeling), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Cosmos DB and PostgreSQL vector documentation: https://learn.microsoft.com/en-us/azure/cosmos-db/

- **A:** Incorrect for this question. Index creation and bulk loads are I/O heavy, and throttled storage stretches maintenance windows. Storage limits are separate from compute. Why the correct answer wins: A read replica takes the long scans off the primary and leaves vector lookups at their expected latency.
- **B:** Incorrect for this question. The plan shows whether PostgreSQL uses the vector index and where the time goes. Adding indexes without reading the plan often misses the cause. Why the correct answer wins: A read replica takes the long scans off the primary and leaves vector lookups at their expected latency.
- **C:** Incorrect for this question. Vector indexes are memory-hungry, so undersized compute causes swapping and slow queries. Right-size before tuning index parameters. Why the correct answer wins: A read replica takes the long scans off the primary and leaves vector lookups at their expected latency.
- **D:** Correct. A replica offloads read traffic but introduces replication lag, which is dangerous for freshly written evidence. It does not reduce index memory pressure. In this case: A read replica takes the long scans off the primary and leaves vector lookups at their expected latency.

### Question 60 — C

Answer: Create an IVFFlat index to save memory on a large table. IVFFlat partitions the vectors into lists and needs far less memory than a graph index, trading some recall for footprint. IVFFlat uses clustering lists and needs periodic rebuilds as data grows, but costs less memory than HNSW. Probes trade recall for speed. Local study-map skill 2.7 (pgvector Indexing and Query Latency), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Cosmos DB and PostgreSQL vector documentation: https://learn.microsoft.com/en-us/azure/cosmos-db/

- **A:** Incorrect for this question. A composite index lets a query filter and order on several paths without a runtime sort. It adds write cost for exactly those paths. Why the correct answer wins: IVFFlat partitions the vectors into lists and needs far less memory than a graph index, trading some recall for footprint.
- **B:** Incorrect for this question. An exact scan is accurate but scales linearly and burns compute. It is a baseline for measuring recall, not a production strategy. Why the correct answer wins: IVFFlat partitions the vectors into lists and needs far less memory than a graph index, trading some recall for footprint.
- **C:** Correct. IVFFlat uses clustering lists and needs periodic rebuilds as data grows, but costs less memory than HNSW. Probes trade recall for speed. In this case: IVFFlat partitions the vectors into lists and needs far less memory than a graph index, trading some recall for footprint.
- **D:** Incorrect for this question. HNSW gives fast approximate nearest-neighbour queries with a larger memory footprint and slower builds. Recall is tunable at query time. Why the correct answer wins: IVFFlat partitions the vectors into lists and needs far less memory than a graph index, trading some recall for footprint.

### Question 61 — A

Answer: Run VACUUM and ANALYZE after bulk loads and large deletes. Dead tuples and stale statistics make scans and the planner work harder until the table is vacuumed and analyzed. Statistics and dead-tuple cleanup change plan quality and index performance. Autovacuum tuning matters for churn-heavy vector tables. Local study-map skill 2.7 (pgvector Indexing and Query Latency), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Cosmos DB and PostgreSQL vector documentation: https://learn.microsoft.com/en-us/azure/cosmos-db/

- **A:** Correct. Statistics and dead-tuple cleanup change plan quality and index performance. Autovacuum tuning matters for churn-heavy vector tables. In this case: Dead tuples and stale statistics make scans and the planner work harder until the table is vacuumed and analyzed.
- **B:** Incorrect for this question. Index creation and bulk loads are I/O heavy, and throttled storage stretches maintenance windows. Storage limits are separate from compute. Why the correct answer wins: Dead tuples and stale statistics make scans and the planner work harder until the table is vacuumed and analyzed.
- **C:** Incorrect for this question. The plan shows whether PostgreSQL uses the vector index and where the time goes. Adding indexes without reading the plan often misses the cause. Why the correct answer wins: Dead tuples and stale statistics make scans and the planner work harder until the table is vacuumed and analyzed.
- **D:** Incorrect for this question. CREATE INDEX CONCURRENTLY keeps inserts and updates flowing during the build, at the cost of a longer build and extra I/O. A failed build leaves an invalid index to drop. Why the correct answer wins: Dead tuples and stale statistics make scans and the planner work harder until the table is vacuumed and analyzed.

### Question 62 — A

Answer: Place a connection pooler in front of PostgreSQL for many short-lived clients. An external pooler multiplexes many short-lived clients onto a small number of server connections. An external pooler multiplexes server connections for serverless or highly concurrent clients. Session-level features may be unavailable in transaction mode. Local study-map skill 2.10 (PostgreSQL Connection Optimization), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Cosmos DB and PostgreSQL vector documentation: https://learn.microsoft.com/en-us/azure/cosmos-db/

- **A:** Correct. An external pooler multiplexes server connections for serverless or highly concurrent clients. Session-level features may be unavailable in transaction mode. In this case: An external pooler multiplexes many short-lived clients onto a small number of server connections.
- **B:** Incorrect for this question. A bounded pool amortizes connection setup and protects the server from connection storms. Pool size must match server limits. Why the correct answer wins: An external pooler multiplexes many short-lived clients onto a small number of server connections.
- **C:** Incorrect for this question. Index creation and bulk loads are I/O heavy, and throttled storage stretches maintenance windows. Storage limits are separate from compute. Why the correct answer wins: An external pooler multiplexes many short-lived clients onto a small number of server connections.
- **D:** Incorrect for this question. Prepared statements avoid repeated planning and reduce chatty network calls. They pair well with pooling but can interact with pool modes. Why the correct answer wins: An external pooler multiplexes many short-lived clients onto a small number of server connections.

### Question 63 — B

Answer: Invalidate or overwrite the cache entry when the source changes. A TTL alone lets a stale price live until it expires, so the write path must overwrite or remove the entry. Write-through or explicit invalidation keeps cached answers consistent with the system of record. Without it, TTL is the only bound on staleness. Local study-map skill 2.11 (Azure Managed Redis Caching and Invalidation), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Cosmos DB and PostgreSQL vector documentation: https://learn.microsoft.com/en-us/azure/cosmos-db/

- **A:** Incorrect for this question. A TTL bounds staleness and reclaims memory without a manual sweep. Too long a TTL hides source changes; too short wastes the cache. Why the correct answer wins: A TTL alone lets a stale price live until it expires, so the write path must overwrite or remove the entry.
- **B:** Correct. Write-through or explicit invalidation keeps cached answers consistent with the system of record. Without it, TTL is the only bound on staleness. In this case: A TTL alone lets a stale price live until it expires, so the write path must overwrite or remove the entry.
- **C:** Incorrect for this question. Eviction protects memory but evicts unpredictably, so a hot key can vanish before its freshness bound is reached. It is not a substitute for TTL design. Why the correct answer wins: A TTL alone lets a stale price live until it expires, so the write path must overwrite or remove the entry.
- **D:** Incorrect for this question. Flushing removes all cached content at once, causing a stampede to the origin and a latency cliff. Targeted invalidation is safer. Why the correct answer wins: A TTL alone lets a stale price live until it expires, so the write path must overwrite or remove the entry.

### Question 64 — A

Answer: Create a vector index in Managed Redis for similarity search. A Redis vector index serves approximate similarity from memory without a database round trip on the hot path. Redis vector search serves low-latency similarity queries from memory. The corpus must fit the memory budget and be rebuilt on model change. Local study-map skill 2.12 (Azure Managed Redis Vector Indexing), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Cosmos DB and PostgreSQL vector documentation: https://learn.microsoft.com/en-us/azure/cosmos-db/

- **A:** Correct. Redis vector search serves low-latency similarity queries from memory. The corpus must fit the memory budget and be rebuilt on model change. In this case: A Redis vector index serves approximate similarity from memory without a database round trip on the hot path.
- **B:** Incorrect for this question. A cache absorbs repeated reads and cuts latency for hot data. Cache keys, TTLs, and invalidation must match the freshness requirement. Why the correct answer wins: A Redis vector index serves approximate similarity from memory without a database round trip on the hot path.
- **C:** Incorrect for this question. Session storage in Redis survives instance restarts and supports distributed instances. Sessions must be scoped and expiring. Why the correct answer wins: A Redis vector index serves approximate similarity from memory without a database round trip on the hot path.
- **D:** Incorrect for this question. A lock can serialize work across instances, but correctness under retries still needs idempotency keys in the data store. Locks expire and can be lost. Why the correct answer wins: A Redis vector index serves approximate similarity from memory without a database round trip on the hot path.

### Question 65 — A

Answer: Set a TTL on each cached entry. A TTL retires entries that will never be read again, which bounds memory without a manual cleanup job. A TTL bounds staleness and reclaims memory without a manual sweep. Too long a TTL hides source changes; too short wastes the cache. Local study-map skill 2.11 (Azure Managed Redis Caching and Invalidation), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Cosmos DB and PostgreSQL vector documentation: https://learn.microsoft.com/en-us/azure/cosmos-db/

- **A:** Correct. A TTL bounds staleness and reclaims memory without a manual sweep. Too long a TTL hides source changes; too short wastes the cache. In this case: A TTL retires entries that will never be read again, which bounds memory without a manual cleanup job.
- **B:** Incorrect for this question. Write-through or explicit invalidation keeps cached answers consistent with the system of record. Without it, TTL is the only bound on staleness. Why the correct answer wins: A TTL retires entries that will never be read again, which bounds memory without a manual cleanup job.
- **C:** Incorrect for this question. Eviction protects memory but evicts unpredictably, so a hot key can vanish before its freshness bound is reached. It is not a substitute for TTL design. Why the correct answer wins: A TTL retires entries that will never be read again, which bounds memory without a manual cleanup job.
- **D:** Incorrect for this question. Flushing removes all cached content at once, causing a stampede to the origin and a latency cliff. Targeted invalidation is safer. Why the correct answer wins: A TTL retires entries that will never be read again, which bounds memory without a manual cleanup job.

### Question 66 — B, E

Answers: Query through the Cosmos DB SDK with parameterized queries; Page large result sets with the continuation token. SDK parameterized queries stay on the supported data-plane path, and the continuation token pages results with a bounded working set. SDK queries keep the client on the supported data plane and parameterization avoids injection and plan churn. Cross-partition queries still cost more. A continuation token returns the next page without re-sorting the previous one, which bounds response size and request charge per call. It is not a snapshot across pages. Local study-map skill 2.1 (Cosmos DB SDK Access and Queries), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Cosmos DB and PostgreSQL vector documentation: https://learn.microsoft.com/en-us/azure/cosmos-db/

- **A:** Incorrect for this question. Indexing everything is simple and makes ad hoc queries possible, at higher write cost and storage. It is a default, not an optimization. Why the correct answer wins: SDK parameterized queries stay on the supported data-plane path, and the continuation token pages results with a bounded working set.
- **B:** Correct. A continuation token returns the next page without re-sorting the previous one, which bounds response size and request charge per call. It is not a snapshot across pages. In this case: SDK parameterized queries stay on the supported data-plane path, and the continuation token pages results with a bounded working set.
- **C:** Incorrect for this question. A point or single-partition query avoids fan-out across partitions. Cross-partition queries consume more RUs and add latency. Why the correct answer wins: SDK parameterized queries stay on the supported data-plane path, and the continuation token pages results with a bounded working set.
- **D:** Incorrect for this question. Application-side scoring works for tiny collections and tests, but it moves all data over the wire and does not scale with corpus size. Why the correct answer wins: SDK parameterized queries stay on the supported data-plane path, and the continuation token pages results with a bounded working set.
- **E:** Correct. SDK queries keep the client on the supported data plane and parameterization avoids injection and plan churn. Cross-partition queries still cost more. In this case: SDK parameterized queries stay on the supported data-plane path, and the continuation token pages results with a bounded working set.

### Question 67 — D, E

Answers: Restrict the indexing policy to the paths the queries use; Add a composite index for the filtered and ordered properties. Narrowing the indexing policy cuts write charge, and a composite index serves both the filter and the order. Selective indexing cuts write RU charge and storage for unused paths. Excluded paths cannot be filtered efficiently later. A composite index lets a query filter and order on several paths without a runtime sort. It adds write cost for exactly those paths. Local study-map skill 2.2 (Cosmos DB Indexing Policies and Request Units), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Cosmos DB and PostgreSQL vector documentation: https://learn.microsoft.com/en-us/azure/cosmos-db/

- **A:** Incorrect for this question. Request units measure the work a query performs, so tuning the query is often cheaper than adding throughput. Monitor normalized RU consumption. Why the correct answer wins: Narrowing the indexing policy cuts write charge, and a composite index serves both the filter and the order.
- **B:** Incorrect for this question. Indexing everything is simple and makes ad hoc queries possible, at higher write cost and storage. It is a default, not an optimization. Why the correct answer wins: Narrowing the indexing policy cuts write charge, and a composite index serves both the filter and the order.
- **C:** Incorrect for this question. Autoscale follows demand between a minimum and maximum, avoiding throttling at peak without paying for peak all day. The maximum still caps the bill. Why the correct answer wins: Narrowing the indexing policy cuts write charge, and a composite index serves both the filter and the order.
- **D:** Correct. A composite index lets a query filter and order on several paths without a runtime sort. It adds write cost for exactly those paths. In this case: Narrowing the indexing policy cuts write charge, and a composite index serves both the filter and the order.
- **E:** Correct. Selective indexing cuts write RU charge and storage for unused paths. Excluded paths cannot be filtered efficiently later. In this case: Narrowing the indexing policy cuts write charge, and a composite index serves both the filter and the order.

### Question 68 — A

Answer: Choose a high-cardinality partition key → set the indexing policy to the queried paths → choose autoscale throughput → query with the partition key → measure the request charge. Partition key and indexing policy must be decided before the query that relies on them, and charge is measured last. Key and policy decisions come before the query that relies on them, and the charge is measured after the query runs. Local study-map skill 2.7 (pgvector Indexing and Query Latency), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Cosmos DB and PostgreSQL vector documentation: https://learn.microsoft.com/en-us/azure/cosmos-db/

- **A:** Correct. Key and policy decisions come before the query that relies on them, and the charge is measured after the query runs. In this case: Partition key and indexing policy must be decided before the query that relies on them, and charge is measured last.
- **B:** Incorrect for this question. The charge cannot be measured before the query and the model exist. Why the correct answer wins: Partition key and indexing policy must be decided before the query that relies on them, and charge is measured last.
- **C:** Incorrect for this question. The query is written against a key and policy that have not been chosen yet. Why the correct answer wins: Partition key and indexing policy must be decided before the query that relies on them, and charge is measured last.
- **D:** Incorrect for this question. A partition key must be chosen before a query can use it as a predicate. Why the correct answer wins: Partition key and indexing policy must be decided before the query that relies on them, and charge is measured last.

### Question 69 — C

Answer: Receive with peek-lock and complete or abandon explicitly. Peek-lock leaves the message invisible but unremoved until the handler completes it, so a crash causes redelivery instead of loss. Peek-lock keeps the message locked until the handler completes it, giving at-least-once processing with retry. Lock duration must exceed processing time. Local study-map skill 3.1 (Service Bus Queues and Sessions), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure messaging and Functions documentation: https://learn.microsoft.com/en-us/azure/service-bus-messaging/

- **A:** Incorrect for this question. A duplicate-detection window drops repeated sends within the window, which helps with at-least-once producers. The window is time-bounded. Why the correct answer wins: Peek-lock leaves the message invisible but unremoved until the handler completes it, so a crash causes redelivery instead of loss.
- **B:** Incorrect for this question. Receive-and-delete removes the message on delivery, so a crash loses work silently. It suits telemetry, not payments. Why the correct answer wins: Peek-lock leaves the message invisible but unremoved until the handler completes it, so a crash causes redelivery instead of loss.
- **C:** Correct. Peek-lock keeps the message locked until the handler completes it, giving at-least-once processing with retry. Lock duration must exceed processing time. In this case: Peek-lock leaves the message invisible but unremoved until the handler completes it, so a crash causes redelivery instead of loss.
- **D:** Incorrect for this question. Sessions give ordered, exclusive processing per session ID across competing consumers. They require session-aware senders and receivers. Why the correct answer wins: Peek-lock leaves the message invisible but unremoved until the handler completes it, so a crash causes redelivery instead of loss.

### Question 70 — A

Answer: Enable duplicate detection on the queue. Duplicate detection drops a repeated message identifier inside the window before any handler sees it. A duplicate-detection window drops repeated sends within the window, which helps with at-least-once producers. The window is time-bounded. Local study-map skill 3.3 (Service Bus Dead-Lettering and Retries), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure messaging and Functions documentation: https://learn.microsoft.com/en-us/azure/service-bus-messaging/

- **A:** Correct. A duplicate-detection window drops repeated sends within the window, which helps with at-least-once producers. The window is time-bounded. In this case: Duplicate detection drops a repeated message identifier inside the window before any handler sees it.
- **B:** Incorrect for this question. A delivery cap stops infinite retries of a failing message and moves it to the dead-letter queue. The cap must exceed legitimate transient retries. Why the correct answer wins: Duplicate detection drops a repeated message identifier inside the window before any handler sees it.
- **C:** Incorrect for this question. At-least-once delivery means duplicates will happen, so the write must tolerate replay. A stored key makes the retry safe. Why the correct answer wins: Duplicate detection drops a repeated message identifier inside the window before any handler sees it.
- **D:** Incorrect for this question. Dead-lettering preserves poison messages for diagnosis instead of losing them. Resubmission needs a fix and an idempotent handler. Why the correct answer wins: Duplicate detection drops a repeated message identifier inside the window before any handler sees it.

### Question 71 — C

Answer: Defer the message and retry it after the dependency recovers. A deferred message leaves the delivery rotation without counting an attempt until it is received again by sequence number. A deferred message stays in the queue without consuming a delivery attempt until it is received again by sequence number. Deferral does not delay the retry by itself. Local study-map skill 3.3 (Service Bus Dead-Lettering and Retries), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure messaging and Functions documentation: https://learn.microsoft.com/en-us/azure/service-bus-messaging/

- **A:** Incorrect for this question. A delivery cap stops infinite retries of a failing message and moves it to the dead-letter queue. The cap must exceed legitimate transient retries. Why the correct answer wins: A deferred message leaves the delivery rotation without counting an attempt until it is received again by sequence number.
- **B:** Incorrect for this question. Peek-lock keeps the message locked until the handler completes it, giving at-least-once processing with retry. Lock duration must exceed processing time. Why the correct answer wins: A deferred message leaves the delivery rotation without counting an attempt until it is received again by sequence number.
- **C:** Correct. A deferred message stays in the queue without consuming a delivery attempt until it is received again by sequence number. Deferral does not delay the retry by itself. In this case: A deferred message leaves the delivery rotation without counting an attempt until it is received again by sequence number.
- **D:** Incorrect for this question. Dead-lettering preserves poison messages for diagnosis instead of losing them. Resubmission needs a fix and an idempotent handler. Why the correct answer wins: A deferred message leaves the delivery rotation without counting an attempt until it is received again by sequence number.

### Question 72 — D

Answer: Use input and output bindings instead of hand-written SDK calls. An output binding lets the runtime write to the store without constructing a client or handling connections in the handler. Bindings reduce boilerplate for common inputs and outputs and are configured declaratively. Complex operations still need the SDK. Local study-map skill 3.5 (Azure Functions Triggers and Bindings), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure messaging and Functions documentation: https://learn.microsoft.com/en-us/azure/service-bus-messaging/

- **A:** Incorrect for this question. A trigger starts the function when work arrives and handles the receive loop for you. Poison-message behavior is configured in host settings. Why the correct answer wins: An output binding lets the runtime write to the store without constructing a client or handling connections in the handler.
- **B:** Incorrect for this question. An HTTP trigger gives a synchronous API endpoint with route and authorization configuration. Long-running work should hand off to a queue. Why the correct answer wins: An output binding lets the runtime write to the store without constructing a client or handling connections in the handler.
- **C:** Incorrect for this question. Durable Functions provides orchestrations, activities, timers, and retries with checkpointed state. Orchestrator code must stay deterministic. Why the correct answer wins: An output binding lets the runtime write to the store without constructing a client or handling connections in the handler.
- **D:** Correct. Bindings reduce boilerplate for common inputs and outputs and are configured declaratively. Complex operations still need the SDK. In this case: An output binding lets the runtime write to the store without constructing a client or handling connections in the handler.

### Question 73 — C

Answer: Tune the function app concurrency and batch size. Lower concurrency and batch size per instance bound the parallel writes that a burst can push at the database. Concurrency and batch size bound how much work one instance takes at a time, which controls downstream pressure and memory. Too high a value causes throttling and timeouts. Local study-map skill 3.6 (Function App Configuration and Deployment), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure messaging and Functions documentation: https://learn.microsoft.com/en-us/azure/service-bus-messaging/

- **A:** Incorrect for this question. A premium plan reduces cold starts and supports virtual network integration and longer timeouts. It costs more than consumption. Why the correct answer wins: Lower concurrency and batch size per instance bound the parallel writes that a burst can push at the database.
- **B:** Incorrect for this question. Consumption bills per execution and scales automatically, with cold starts and a timeout ceiling. It fits spiky, short work. Why the correct answer wins: Lower concurrency and batch size per instance bound the parallel writes that a burst can push at the database.
- **C:** Correct. Concurrency and batch size bound how much work one instance takes at a time, which controls downstream pressure and memory. Too high a value causes throttling and timeouts. In this case: Lower concurrency and batch size per instance bound the parallel writes that a burst can push at the database.
- **D:** Incorrect for this question. The host retry policy re-executes a failing trigger with bounded attempts and backoff. It cannot make a non-idempotent handler safe to replay. Why the correct answer wins: Lower concurrency and batch size per instance bound the parallel writes that a burst can push at the database.

### Question 74 — C

Answer: Run the scheduled maintenance from a timer trigger. A timer trigger runs on a declared schedule without an external caller and honours an explicit time zone. A timer trigger invokes the function on a schedule without an external caller. Overlapping runs and the time zone must be configured deliberately. Local study-map skill 3.5 (Azure Functions Triggers and Bindings), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure messaging and Functions documentation: https://learn.microsoft.com/en-us/azure/service-bus-messaging/

- **A:** Incorrect for this question. A trigger starts the function when work arrives and handles the receive loop for you. Poison-message behavior is configured in host settings. Why the correct answer wins: A timer trigger runs on a declared schedule without an external caller and honours an explicit time zone.
- **B:** Incorrect for this question. An HTTP trigger gives a synchronous API endpoint with route and authorization configuration. Long-running work should hand off to a queue. Why the correct answer wins: A timer trigger runs on a declared schedule without an external caller and honours an explicit time zone.
- **C:** Correct. A timer trigger invokes the function on a schedule without an external caller. Overlapping runs and the time zone must be configured deliberately. In this case: A timer trigger runs on a declared schedule without an external caller and honours an explicit time zone.
- **D:** Incorrect for this question. Event Grid retries failed deliveries with backoff and can store undeliverable events. Handlers must still be idempotent. Why the correct answer wins: A timer trigger runs on a declared schedule without an external caller and honours an explicit time zone.

### Question 75 — D

Answer: Use a deployment slot on the function app for staging. A deployment slot runs the new build beside production and can be swapped after verification, which keeps rollback quick. A staging slot lets a new build warm up and be validated before the swap. Slot settings that must not move are marked sticky. Local study-map skill 3.6 (Function App Configuration and Deployment), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure messaging and Functions documentation: https://learn.microsoft.com/en-us/azure/service-bus-messaging/

- **A:** Incorrect for this question. A premium plan reduces cold starts and supports virtual network integration and longer timeouts. It costs more than consumption. Why the correct answer wins: A deployment slot runs the new build beside production and can be swapped after verification, which keeps rollback quick.
- **B:** Incorrect for this question. Pipeline deployment keeps code and configuration versioned together and repeatable. Secrets belong in a vault reference, not in the pipeline file. Why the correct answer wins: A deployment slot runs the new build beside production and can be swapped after verification, which keeps rollback quick.
- **C:** Incorrect for this question. Consumption bills per execution and scales automatically, with cold starts and a timeout ceiling. It fits spiky, short work. Why the correct answer wins: A deployment slot runs the new build beside production and can be swapped after verification, which keeps rollback quick.
- **D:** Correct. A staging slot lets a new build warm up and be validated before the swap. Slot settings that must not move are marked sticky. In this case: A deployment slot runs the new build beside production and can be swapped after verification, which keeps rollback quick.

### Question 76 — A, E

Answers: Filter the Event Grid subscription by subject or event type; Rely on Event Grid retries with a dead-letter destination. A subject filter narrows delivery to the container, and retries with a dead-letter destination prevent permanent loss. Subject and event-type filters keep handlers focused and reduce cost. Filters are evaluated on event metadata, not payload body. Event Grid retries failed deliveries with backoff and can store undeliverable events. Handlers must still be idempotent. Local study-map skill 3.4 (Event Grid Filters, Custom Events, and Retries), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure messaging and Functions documentation: https://learn.microsoft.com/en-us/azure/service-bus-messaging/

- **A:** Correct. Subject and event-type filters keep handlers focused and reduce cost. Filters are evaluated on event metadata, not payload body. In this case: A subject filter narrows delivery to the container, and retries with a dead-letter destination prevent permanent loss.
- **B:** Incorrect for this question. Subscription filters route only matching messages to a handler, reducing wasted processing. Filter evaluation happens broker-side on message properties. Why the correct answer wins: A subject filter narrows delivery to the container, and retries with a dead-letter destination prevent permanent loss.
- **C:** Incorrect for this question. Event Hubs ingests high-volume ordered streams with partitions and consumer groups. It is a streaming log, not a task queue. Why the correct answer wins: A subject filter narrows delivery to the container, and retries with a dead-letter destination prevent permanent loss.
- **D:** Incorrect for this question. A custom schema fits domain events that are not resource lifecycle notifications. Consumers must version the schema contract. Why the correct answer wins: A subject filter narrows delivery to the container, and retries with a dead-letter destination prevent permanent loss.
- **E:** Correct. Event Grid retries failed deliveries with backoff and can store undeliverable events. Handlers must still be idempotent. In this case: A subject filter narrows delivery to the container, and retries with a dead-letter destination prevent permanent loss.

### Question 77 — B, E

Answers: Assign a managed identity to the function app and use it for downstream calls; Deploy the function app through a CI pipeline with app settings applied. A managed identity removes the stored key, and a pipeline deployment applies the settings that the function expects. A function app can authenticate with a managed identity, so no connection secret is needed in app settings. Pipeline deployment keeps code and configuration versioned together and repeatable. Secrets belong in a vault reference, not in the pipeline file. Local study-map skill 3.6 (Function App Configuration and Deployment), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure messaging and Functions documentation: https://learn.microsoft.com/en-us/azure/service-bus-messaging/

- **A:** Incorrect for this question. Application settings become environment variables for the container and can be swapped per slot. Sensitive values should still reference a vault. Why the correct answer wins: A managed identity removes the stored key, and a pipeline deployment applies the settings that the function expects.
- **B:** Correct. Pipeline deployment keeps code and configuration versioned together and repeatable. Secrets belong in a vault reference, not in the pipeline file. In this case: A managed identity removes the stored key, and a pipeline deployment applies the settings that the function expects.
- **C:** Incorrect for this question. An HTTP trigger gives a synchronous API endpoint with route and authorization configuration. Long-running work should hand off to a queue. Why the correct answer wins: A managed identity removes the stored key, and a pipeline deployment applies the settings that the function expects.
- **D:** Incorrect for this question. Consumption bills per execution and scales automatically, with cold starts and a timeout ceiling. It fits spiky, short work. Why the correct answer wins: A managed identity removes the stored key, and a pipeline deployment applies the settings that the function expects.
- **E:** Correct. A function app can authenticate with a managed identity, so no connection secret is needed in app settings. In this case: A managed identity removes the stored key, and a pipeline deployment applies the settings that the function expects.

### Question 78 — A

Answer: Publish the message → receive with peek-lock → process the work → complete the message → dead-letter after the delivery limit. Publishing, peek-lock receipt, processing, completion, and dead-lettering after the limit occur in that order. Peek-lock keeps the message until the handler succeeds, and only repeated failures should dead-letter it. Local study-map skill 3.1 (Service Bus Queues and Sessions), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure messaging and Functions documentation: https://learn.microsoft.com/en-us/azure/service-bus-messaging/

- **A:** Correct. Peek-lock keeps the message until the handler succeeds, and only repeated failures should dead-letter it. In this case: Publishing, peek-lock receipt, processing, completion, and dead-lettering after the limit occur in that order.
- **B:** Incorrect for this question. The message cannot be received before it is published, and completion must follow processing. Why the correct answer wins: Publishing, peek-lock receipt, processing, completion, and dead-lettering after the limit occur in that order.
- **C:** Incorrect for this question. Work cannot be processed before the message is published and received. Why the correct answer wins: Publishing, peek-lock receipt, processing, completion, and dead-lettering after the limit occur in that order.
- **D:** Incorrect for this question. Completing a message before processing discards the work and defeats at-least-once delivery. Why the correct answer wins: Publishing, peek-lock receipt, processing, completion, and dead-lettering after the limit occur in that order.

### Question 79 — A

Answer: Grant the app identity data-plane access to the vault. A managed identity still needs a data-plane role assignment on the vault, and the 403 shows that assignment is absent. Vault access is a separate authorization decision from the app identity. Without a data-plane role or policy the reference fails at runtime. Local study-map skill 4.1 (Key Vault Secret Storage, Rotation, and Retrieval), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Key Vault, App Configuration, and Monitor documentation: https://learn.microsoft.com/en-us/azure/azure-monitor/

- **A:** Correct. Vault access is a separate authorization decision from the app identity. Without a data-plane role or policy the reference fails at runtime. In this case: A managed identity still needs a data-plane role assignment on the vault, and the 403 shows that assignment is absent.
- **B:** Incorrect for this question. A Key Vault reference resolves at runtime so the secret is never written into application settings. The app identity still needs permission to read it. Why the correct answer wins: A managed identity still needs a data-plane role assignment on the vault, and the 403 shows that assignment is absent.
- **C:** Incorrect for this question. A vault centralizes secret storage with access control and audit. Retrieval should use an identity, not a copied credential. Why the correct answer wins: A managed identity still needs a data-plane role assignment on the vault, and the 403 shows that assignment is absent.
- **D:** Incorrect for this question. A scoped role grants only the operations the app performs and limits blast radius. Prefer built-in roles over broad contributor grants. Why the correct answer wins: A managed identity still needs a data-plane role assignment on the vault, and the 403 shows that assignment is absent.

### Question 80 — D

Answer: Rotate the secret on a schedule and let apps resolve the current version. Rotation issues a new secret version, and the app resolves the current version, so no deployment is required. Rotation limits the value of a leaked secret, but callers must read the latest version rather than caching an old one forever. Local study-map skill 4.1 (Key Vault Secret Storage, Rotation, and Retrieval), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Key Vault, App Configuration, and Monitor documentation: https://learn.microsoft.com/en-us/azure/azure-monitor/

- **A:** Incorrect for this question. Soft delete and purge protection stop accidental or malicious permanent loss of secrets. They also constrain how names can be reused. Why the correct answer wins: Rotation issues a new secret version, and the app resolves the current version, so no deployment is required.
- **B:** Incorrect for this question. A managed identity issues tokens from the platform, removing secret distribution from the app. Role assignment still scopes what it can reach. Why the correct answer wins: Rotation issues a new secret version, and the app resolves the current version, so no deployment is required.
- **C:** Incorrect for this question. Pinning a version makes a rotation invisible to the app until it is redeployed, which is useful for break-glass and dangerous for routine rotation. Why the correct answer wins: Rotation issues a new secret version, and the app resolves the current version, so no deployment is required.
- **D:** Correct. Rotation limits the value of a leaked secret, but callers must read the latest version rather than caching an old one forever. In this case: Rotation issues a new secret version, and the app resolves the current version, so no deployment is required.

### Question 81 — B

Answer: Ship the code dark behind a feature flag. Code shipped dark behind a flag can be turned on or off without another deployment. A feature flag enables reviewed code in production without a redeploy and lets it be switched off instantly. Flag state still needs ownership and cleanup. Local study-map skill 4.2 (App Configuration Settings and Feature Flags), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Key Vault, App Configuration, and Monitor documentation: https://learn.microsoft.com/en-us/azure/azure-monitor/

- **A:** Incorrect for this question. Labels keep dev, test, and prod values in one store with one key schema. A misconfigured label selector silently serves the wrong values. Why the correct answer wins: Code shipped dark behind a flag can be turned on or off without another deployment.
- **B:** Correct. A feature flag enables reviewed code in production without a redeploy and lets it be switched off instantly. Flag state still needs ownership and cleanup. In this case: Code shipped dark behind a flag can be turned on or off without another deployment.
- **C:** Incorrect for this question. App Configuration separates configuration from code and supports labels, feature flags, and Key Vault references. Change still needs a refresh strategy. Why the correct answer wins: Code shipped dark behind a flag can be turned on or off without another deployment.
- **D:** Incorrect for this question. Sentinel-key or polling refresh lets a running app pick up new settings. Refresh intervals trade responsiveness against request volume. Why the correct answer wins: Code shipped dark behind a flag can be turned on or off without another deployment.

### Question 82 — D

Answer: Create a custom span around each downstream call. A span around the downstream call records its duration and makes the missing hop visible in the trace. A span records the duration and outcome of one operation and nests under the trace. It makes the slow dependency visible in the transaction view. Local study-map skill 4.3 (Distributed Tracing with OpenTelemetry), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Key Vault, App Configuration, and Monitor documentation: https://learn.microsoft.com/en-us/azure/azure-monitor/

- **A:** Incorrect for this question. Including the trace ID in log records lets you pivot from a failed span to its log lines. Without it, logs and traces are separate worlds. Why the correct answer wins: A span around the downstream call records its duration and makes the missing hop visible in the trace.
- **B:** Incorrect for this question. Propagation stitches one trace across HTTP, messaging, and Functions so the whole path is visible. Missing propagation breaks the trace at that hop. Why the correct answer wins: A span around the downstream call records its duration and makes the missing hop visible in the trace.
- **C:** Incorrect for this question. OpenTelemetry emits vendor-neutral traces, metrics, and logs with context propagation. Exporters and sampling decide what reaches the backend. Why the correct answer wins: A span around the downstream call records its duration and makes the missing hop visible in the trace.
- **D:** Correct. A span records the duration and outcome of one operation and nests under the trace. It makes the slow dependency visible in the transaction view. In this case: A span around the downstream call records its duration and makes the missing hop visible in the trace.

### Question 83 — A

Answer: Aggregate with summarize and bin to see the failure rate over time. summarize with bin groups requests into time buckets and computes the failure ratio for each bucket. Time-binned aggregation reveals the shape of an incident: a step change, a ramp, or a periodic spike. Averages alone hide short outages. Local study-map skill 4.4 (KQL Queries for Logs and Metrics), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Key Vault, App Configuration, and Monitor documentation: https://learn.microsoft.com/en-us/azure/azure-monitor/

- **A:** Correct. Time-binned aggregation reveals the shape of an incident: a step change, a ramp, or a periodic spike. Averages alone hide short outages. In this case: summarize with bin groups requests into time buckets and computes the failure ratio for each bucket.
- **B:** Incorrect for this question. Joining request and dependency telemetry shows which downstream call fails inside a slow request. Cross-workspace joins need the right scope. Why the correct answer wins: summarize with bin groups requests into time buckets and computes the failure ratio for each bucket.
- **C:** Incorrect for this question. KQL filters, projects, and aggregates log and metric tables in Log Analytics. Start narrow with a time range and a request ID. Why the correct answer wins: summarize with bin groups requests into time buckets and computes the failure ratio for each bucket.
- **D:** Incorrect for this question. Reducing columns and rows early lowers query cost and latency. Broad queries over long ranges are the usual cause of slow KQL. Why the correct answer wins: summarize with bin groups requests into time buckets and computes the failure ratio for each bucket.

### Question 84 — D

Answer: Set the workspace retention and table plan to control log cost. Shortening retention and choosing the right table plan removes the cost of data that nobody queries. Retention and the table plan determine how long data is queryable and what it costs. Lower retention reduces cost but shortens the investigation window. Local study-map skill 4.4 (KQL Queries for Logs and Metrics), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Key Vault, App Configuration, and Monitor documentation: https://learn.microsoft.com/en-us/azure/azure-monitor/

- **A:** Incorrect for this question. Container Apps and AKS surface stdout logs and platform events into a workspace for KQL analysis. Verbosity and retention cost money. Why the correct answer wins: Shortening retention and choosing the right table plan removes the cost of data that nobody queries.
- **B:** Incorrect for this question. Platform logs and metrics must be routed before they can be queried or alerted on. Retention and cost follow the workspace settings. Why the correct answer wins: Shortening retention and choosing the right table plan removes the cost of data that nobody queries.
- **C:** Incorrect for this question. Platform metrics are cheap and near-real-time, so they suit latency and failure-rate alerts. Log-based alerts add latency and query cost. Why the correct answer wins: Shortening retention and choosing the right table plan removes the cost of data that nobody queries.
- **D:** Correct. Retention and the table plan determine how long data is queryable and what it costs. Lower retention reduces cost but shortens the investigation window. In this case: Shortening retention and choosing the right table plan removes the cost of data that nobody queries.

### Question 85 — A, C

Answers: Authenticate with a managed identity instead of a stored key; Assign a least-privilege role to the application identity. A managed identity supplies the credential, and a least-privilege role grants exactly the access the API needs. A managed identity issues tokens from the platform, removing secret distribution from the app. Role assignment still scopes what it can reach. A scoped role grants only the operations the app performs and limits blast radius. Prefer built-in roles over broad contributor grants. Local study-map skill 4.5 (Identity-Based Access for Application Services), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Key Vault, App Configuration, and Monitor documentation: https://learn.microsoft.com/en-us/azure/azure-monitor/

- **A:** Correct. A managed identity issues tokens from the platform, removing secret distribution from the app. Role assignment still scopes what it can reach. In this case: A managed identity supplies the credential, and a least-privilege role grants exactly the access the API needs.
- **B:** Incorrect for this question. A Key Vault reference resolves at runtime so the secret is never written into application settings. The app identity still needs permission to read it. Why the correct answer wins: A managed identity supplies the credential, and a least-privilege role grants exactly the access the API needs.
- **C:** Correct. A scoped role grants only the operations the app performs and limits blast radius. Prefer built-in roles over broad contributor grants. In this case: A managed identity supplies the credential, and a least-privilege role grants exactly the access the API needs.
- **D:** Incorrect for this question. Soft delete and purge protection stop accidental or malicious permanent loss of secrets. They also constrain how names can be reused. Why the correct answer wins: A managed identity supplies the credential, and a least-privilege role grants exactly the access the API needs.
- **E:** Incorrect for this question. Pinning a version makes a rotation invisible to the app until it is redeployed, which is useful for break-glass and dangerous for routine rotation. Why the correct answer wins: A managed identity supplies the credential, and a least-privilege role grants exactly the access the API needs.

### Question 86 — B, C

Answers: Use App Configuration labels to separate environments; Reference the Key Vault secret from an App Configuration key value. Labels separate environments inside one store, and a Key Vault reference keeps the secret value out of the store. Labels keep dev, test, and prod values in one store with one key schema. A misconfigured label selector silently serves the wrong values. A Key Vault reference keeps non-secret settings in App Configuration while the value stays in the vault. The app identity needs both sets of permissions. Local study-map skill 4.2 (App Configuration Settings and Feature Flags), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Key Vault, App Configuration, and Monitor documentation: https://learn.microsoft.com/en-us/azure/azure-monitor/

- **A:** Incorrect for this question. A feature flag enables reviewed code in production without a redeploy and lets it be switched off instantly. Flag state still needs ownership and cleanup. Why the correct answer wins: Labels separate environments inside one store, and a Key Vault reference keeps the secret value out of the store.
- **B:** Correct. Labels keep dev, test, and prod values in one store with one key schema. A misconfigured label selector silently serves the wrong values. In this case: Labels separate environments inside one store, and a Key Vault reference keeps the secret value out of the store.
- **C:** Correct. A Key Vault reference keeps non-secret settings in App Configuration while the value stays in the vault. The app identity needs both sets of permissions. In this case: Labels separate environments inside one store, and a Key Vault reference keeps the secret value out of the store.
- **D:** Incorrect for this question. Pinning a version makes a rotation invisible to the app until it is redeployed, which is useful for break-glass and dangerous for routine rotation. Why the correct answer wins: Labels separate environments inside one store, and a Key Vault reference keeps the secret value out of the store.
- **E:** Incorrect for this question. Sentinel-key or polling refresh lets a running app pick up new settings. Refresh intervals trade responsiveness against request volume. Why the correct answer wins: Labels separate environments inside one store, and a Key Vault reference keeps the secret value out of the store.

### Question 87 — B, E

Answers: Enable purge protection and soft delete on the vault; Grant the app identity data-plane access to the vault. Soft delete with purge protection preserves the vault, and a data-plane role assignment lets the identity read it. Soft delete and purge protection stop accidental or malicious permanent loss of secrets. They also constrain how names can be reused. Vault access is a separate authorization decision from the app identity. Without a data-plane role or policy the reference fails at runtime. Local study-map skill 4.1 (Key Vault Secret Storage, Rotation, and Retrieval), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Key Vault, App Configuration, and Monitor documentation: https://learn.microsoft.com/en-us/azure/azure-monitor/

- **A:** Incorrect for this question. Pinning a version makes a rotation invisible to the app until it is redeployed, which is useful for break-glass and dangerous for routine rotation. Why the correct answer wins: Soft delete with purge protection preserves the vault, and a data-plane role assignment lets the identity read it.
- **B:** Correct. Vault access is a separate authorization decision from the app identity. Without a data-plane role or policy the reference fails at runtime. In this case: Soft delete with purge protection preserves the vault, and a data-plane role assignment lets the identity read it.
- **C:** Incorrect for this question. A Key Vault reference resolves at runtime so the secret is never written into application settings. The app identity still needs permission to read it. Why the correct answer wins: Soft delete with purge protection preserves the vault, and a data-plane role assignment lets the identity read it.
- **D:** Incorrect for this question. Rotation limits the value of a leaked secret, but callers must read the latest version rather than caching an old one forever. Why the correct answer wins: Soft delete with purge protection preserves the vault, and a data-plane role assignment lets the identity read it.
- **E:** Correct. Soft delete and purge protection stop accidental or malicious permanent loss of secrets. They also constrain how names can be reused. In this case: Soft delete with purge protection preserves the vault, and a data-plane role assignment lets the identity read it.

### Question 88 — D

Answer: Instrument the service with the OpenTelemetry SDK → propagate the trace context across queue hops → export spans to the collector → query the transaction view for the slow dependency → alert on the failure rate. Instrumentation precedes context propagation, export precedes querying, and alerting follows a validated query. Instrumentation precedes context propagation, export precedes querying, and alerting follows a validated query. Local study-map skill 4.3 (Distributed Tracing with OpenTelemetry), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Key Vault, App Configuration, and Monitor documentation: https://learn.microsoft.com/en-us/azure/azure-monitor/

- **A:** Incorrect for this question. An alert cannot be defined before the telemetry it depends on exists. Why the correct answer wins: Instrumentation precedes context propagation, export precedes querying, and alerting follows a validated query.
- **B:** Incorrect for this question. Querying and alerting cannot precede instrumentation and export. Why the correct answer wins: Instrumentation precedes context propagation, export precedes querying, and alerting follows a validated query.
- **C:** Incorrect for this question. There are no spans to export before instrumentation and propagation are in place. Why the correct answer wins: Instrumentation precedes context propagation, export precedes querying, and alerting follows a validated query.
- **D:** Correct. Instrumentation precedes context propagation, export precedes querying, and alerting follows a validated query. In this case: Instrumentation precedes context propagation, export precedes querying, and alerting follows a validated query.

### Question 89 — B

Answer: Use a lease container to coordinate change feed readers. Lease documents record ownership per partition range, so instances divide the feed without processing the same items twice. Leases track partition ownership so multiple processor instances share work and resume from a continuation token. Lease writes consume RUs too. Local study-map skill 2.5 (Cosmos DB Change Feed Processing), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Cosmos DB and PostgreSQL vector documentation: https://learn.microsoft.com/en-us/azure/cosmos-db/

- **A:** Incorrect for this question. The change feed delivers an ordered stream of changes per partition for downstream processing. It is not a delete feed, so deletions need a workaround. Why the correct answer wins: Lease documents record ownership per partition range, so instances divide the feed without processing the same items twice.
- **B:** Correct. Leases track partition ownership so multiple processor instances share work and resume from a continuation token. Lease writes consume RUs too. In this case: Lease documents record ownership per partition range, so instances divide the feed without processing the same items twice.
- **C:** Incorrect for this question. Item TTL expires documents automatically, which controls storage growth and data retention. It does not archive the expired content. Why the correct answer wins: Lease documents record ownership per partition range, so instances divide the feed without processing the same items twice.
- **D:** Incorrect for this question. A duplicate-detection window drops repeated sends within the window, which helps with at-least-once producers. The window is time-bounded. Why the correct answer wins: Lease documents record ownership per partition range, so instances divide the feed without processing the same items twice.

### Question 90 — B

Answer: Subscribe to a system topic for resource events. A system topic carries resource events published by the Azure service itself, so no custom publisher code is needed. System topics carry Azure resource lifecycle events. Domain events that are not resource changes need a custom topic and schema. Local study-map skill 3.4 (Event Grid Filters, Custom Events, and Retries), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure messaging and Functions documentation: https://learn.microsoft.com/en-us/azure/service-bus-messaging/

- **A:** Incorrect for this question. Event Grid retries failed deliveries with backoff and can store undeliverable events. Handlers must still be idempotent. Why the correct answer wins: A system topic carries resource events published by the Azure service itself, so no custom publisher code is needed.
- **B:** Correct. System topics carry Azure resource lifecycle events. Domain events that are not resource changes need a custom topic and schema. In this case: A system topic carries resource events published by the Azure service itself, so no custom publisher code is needed.
- **C:** Incorrect for this question. A custom schema fits domain events that are not resource lifecycle notifications. Consumers must version the schema contract. Why the correct answer wins: A system topic carries resource events published by the Azure service itself, so no custom publisher code is needed.
- **D:** Incorrect for this question. Event Grid delivers discrete notifications to subscribers with retries and filtering. It carries events, not large payloads or ordered streams. Why the correct answer wins: A system topic carries resource events published by the Azure service itself, so no custom publisher code is needed.

### Question 91 — A

Answer: Enable configuration refresh so changes apply without a restart. Refresh pulls changed key-values when the sentinel changes, so running instances pick up the new flag value. Sentinel-key or polling refresh lets a running app pick up new settings. Refresh intervals trade responsiveness against request volume. Local study-map skill 4.2 (App Configuration Settings and Feature Flags), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Key Vault, App Configuration, and Monitor documentation: https://learn.microsoft.com/en-us/azure/azure-monitor/

- **A:** Correct. Sentinel-key or polling refresh lets a running app pick up new settings. Refresh intervals trade responsiveness against request volume. In this case: Refresh pulls changed key-values when the sentinel changes, so running instances pick up the new flag value.
- **B:** Incorrect for this question. A Key Vault reference keeps non-secret settings in App Configuration while the value stays in the vault. The app identity needs both sets of permissions. Why the correct answer wins: Refresh pulls changed key-values when the sentinel changes, so running instances pick up the new flag value.
- **C:** Incorrect for this question. Labels keep dev, test, and prod values in one store with one key schema. A misconfigured label selector silently serves the wrong values. Why the correct answer wins: Refresh pulls changed key-values when the sentinel changes, so running instances pick up the new flag value.
- **D:** Incorrect for this question. App Configuration separates configuration from code and supports labels, feature flags, and Key Vault references. Change still needs a refresh strategy. Why the correct answer wins: Refresh pulls changed key-values when the sentinel changes, so running instances pick up the new flag value.

### Question 92 — D

Answer: Filter on metadata columns in the same query as the vector search. Filtering on metadata in the same query as the distance operator keeps the result set complete and scoped. Combining a WHERE filter with the distance operator keeps retrieval inside the caller's scope and improves relevance. Index the filter columns too. Local study-map skill 2.9 (PostgreSQL RAG with Metadata Filters), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Cosmos DB and PostgreSQL vector documentation: https://learn.microsoft.com/en-us/azure/cosmos-db/

- **A:** Incorrect for this question. HNSW gives fast approximate nearest-neighbour queries with a larger memory footprint and slower builds. Recall is tunable at query time. Why the correct answer wins: Filtering on metadata in the same query as the distance operator keeps the result set complete and scoped.
- **B:** Incorrect for this question. IVFFlat uses clustering lists and needs periodic rebuilds as data grows, but costs less memory than HNSW. Probes trade recall for speed. Why the correct answer wins: Filtering on metadata in the same query as the distance operator keeps the result set complete and scoped.
- **C:** Incorrect for this question. Post-filtering can return fewer results than requested and can leak existence or counts if the filtering is careless. Push authorization into the query. Why the correct answer wins: Filtering on metadata in the same query as the distance operator keeps the result set complete and scoped.
- **D:** Correct. Combining a WHERE filter with the distance operator keeps retrieval inside the caller's scope and improves relevance. Index the filter columns too. In this case: Filtering on metadata in the same query as the distance operator keeps the result set complete and scoped.

### Question 93 — A

Answer: Scale compute and memory to fit index size and query concurrency. A vector index working set that exceeds memory causes swapping, so compute and memory must fit the index. Vector indexes are memory-hungry, so undersized compute causes swapping and slow queries. Right-size before tuning index parameters. Local study-map skill 2.8 (PostgreSQL Compute, Memory, and Storage Sizing), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Cosmos DB and PostgreSQL vector documentation: https://learn.microsoft.com/en-us/azure/cosmos-db/

- **A:** Correct. Vector indexes are memory-hungry, so undersized compute causes swapping and slow queries. Right-size before tuning index parameters. In this case: A vector index working set that exceeds memory causes swapping, so compute and memory must fit the index.
- **B:** Incorrect for this question. An external pooler multiplexes server connections for serverless or highly concurrent clients. Session-level features may be unavailable in transaction mode. Why the correct answer wins: A vector index working set that exceeds memory causes swapping, so compute and memory must fit the index.
- **C:** Incorrect for this question. Index creation and bulk loads are I/O heavy, and throttled storage stretches maintenance windows. Storage limits are separate from compute. Why the correct answer wins: A vector index working set that exceeds memory causes swapping, so compute and memory must fit the index.
- **D:** Incorrect for this question. A replica offloads read traffic but introduces replication lag, which is dangerous for freshly written evidence. It does not reduce index memory pressure. Why the correct answer wins: A vector index working set that exceeds memory causes swapping, so compute and memory must fit the index.

### Question 94 — A

Answer: Create a vector index in Managed Redis for similarity search. A Redis vector index serves similarity queries from memory at low latency. Redis vector search serves low-latency similarity queries from memory. The corpus must fit the memory budget and be rebuilt on model change. Local study-map skill 2.12 (Azure Managed Redis Vector Indexing), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Cosmos DB and PostgreSQL vector documentation: https://learn.microsoft.com/en-us/azure/cosmos-db/

- **A:** Correct. Redis vector search serves low-latency similarity queries from memory. The corpus must fit the memory budget and be rebuilt on model change. In this case: A Redis vector index serves similarity queries from memory at low latency.
- **B:** Incorrect for this question. Session storage in Redis survives instance restarts and supports distributed instances. Sessions must be scoped and expiring. Why the correct answer wins: A Redis vector index serves similarity queries from memory at low latency.
- **C:** Incorrect for this question. A lock can serialize work across instances, but correctness under retries still needs idempotency keys in the data store. Locks expire and can be lost. Why the correct answer wins: A Redis vector index serves similarity queries from memory at low latency.
- **D:** Incorrect for this question. A cache absorbs repeated reads and cuts latency for hot data. Cache keys, TTLs, and invalidation must match the freshness requirement. Why the correct answer wins: A Redis vector index serves similarity queries from memory at low latency.

### Question 95 — D

Answer: Create a new Container Apps revision and shift traffic between revisions. Container Apps revisions support percentage traffic allocation between versions, which enables a canary release and a fast rollback. Revision-based traffic splitting enables canary and blue-green releases. Revision mode and scale rules must be set deliberately. Local study-map skill 1.4 (Container Apps Deployment and Revisions), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure container hosting documentation: https://learn.microsoft.com/en-us/azure/container-apps/

- **A:** Incorrect for this question. HPA adjusts replicas from resource metrics but needs metrics-server and enough node capacity. It cannot scale to zero. Why the correct answer wins: Container Apps revisions support percentage traffic allocation between versions, which enables a canary release and a fast rollback.
- **B:** Incorrect for this question. A slot swap warms the new version before it takes production traffic and makes rollback a second swap. Slot-local settings must be marked sticky. Why the correct answer wins: Container Apps revisions support percentage traffic allocation between versions, which enables a canary release and a fast rollback.
- **C:** Incorrect for this question. Geo-replication reduces cross-region pull latency and gives a local copy during a regional failure. It adds cost and replication management. Why the correct answer wins: Container Apps revisions support percentage traffic allocation between versions, which enables a canary release and a fast rollback.
- **D:** Correct. Revision-based traffic splitting enables canary and blue-green releases. Revision mode and scale rules must be set deliberately. In this case: Container Apps revisions support percentage traffic allocation between versions, which enables a canary release and a fast rollback.

### Question 96 — C

Answer: Scale on the Service Bus queue length with a KEDA Azure Service Bus scaler. A KEDA Service Bus scaler adds consumers while messages are backed up and scales to zero when the queue is empty. A queue-length scaler adds replicas while work is backed up and removes them when the queue drains. Message lock duration must exceed processing time. Local study-map skill 1.5 (Event-Driven Scaling with KEDA), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure container hosting documentation: https://learn.microsoft.com/en-us/azure/container-apps/

- **A:** Incorrect for this question. HPA adjusts replicas from resource metrics but needs metrics-server and enough node capacity. It cannot scale to zero. Why the correct answer wins: A KEDA Service Bus scaler adds consumers while messages are backed up and scales to zero when the queue is empty.
- **B:** Incorrect for this question. Container Instances starts a single container group quickly for short tasks. It has no orchestrator-level scaling or revision model. Why the correct answer wins: A KEDA Service Bus scaler adds consumers while messages are backed up and scales to zero when the queue is empty.
- **C:** Correct. A queue-length scaler adds replicas while work is backed up and removes them when the queue drains. Message lock duration must exceed processing time. In this case: A KEDA Service Bus scaler adds consumers while messages are backed up and scales to zero when the queue is empty.
- **D:** Incorrect for this question. CPU-based scaling reacts after work is already queued and cannot scale to zero on an empty queue. It suits steady request-driven services. Why the correct answer wins: A KEDA Service Bus scaler adds consumers while messages are backed up and scales to zero when the queue is empty.

### Question 97 — D

Answer: Reference a Key Vault secret from the app configuration instead of storing it. A Key Vault reference resolves the secret at runtime through the app identity, so the value never appears in settings or source control. A Key Vault reference resolves at runtime so the secret is never written into application settings. The app identity still needs permission to read it. Local study-map skill 1.3 (Container Deployment to Azure App Service), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure container hosting documentation: https://learn.microsoft.com/en-us/azure/container-apps/

- **A:** Incorrect for this question. Application settings become environment variables for the container and can be swapped per slot. Sensitive values should still reference a vault. Why the correct answer wins: A Key Vault reference resolves the secret at runtime through the app identity, so the value never appears in settings or source control.
- **B:** Incorrect for this question. Pinning a version makes a rotation invisible to the app until it is redeployed, which is useful for break-glass and dangerous for routine rotation. Why the correct answer wins: A Key Vault reference resolves the secret at runtime through the app identity, so the value never appears in settings or source control.
- **C:** Incorrect for this question. A floating tag removes the link between a deployed revision and a specific build, so rollback and audit become guesswork. Why the correct answer wins: A Key Vault reference resolves the secret at runtime through the app identity, so the value never appears in settings or source control.
- **D:** Correct. A Key Vault reference resolves at runtime so the secret is never written into application settings. The app identity still needs permission to read it. In this case: A Key Vault reference resolves the secret at runtime through the app identity, so the value never appears in settings or source control.

### Question 98 — B

Answer: Supply configuration through App Service application settings. Application settings become environment variables per slot, so a value change does not require rebuilding or republishing the image. Application settings become environment variables for the container and can be swapped per slot. Sensitive values should still reference a vault. Local study-map skill 1.3 (Container Deployment to Azure App Service), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure container hosting documentation: https://learn.microsoft.com/en-us/azure/container-apps/

- **A:** Incorrect for this question. Pinning a version makes a rotation invisible to the app until it is redeployed, which is useful for break-glass and dangerous for routine rotation. Why the correct answer wins: Application settings become environment variables per slot, so a value change does not require rebuilding or republishing the image.
- **B:** Correct. Application settings become environment variables for the container and can be swapped per slot. Sensitive values should still reference a vault. In this case: Application settings become environment variables per slot, so a value change does not require rebuilding or republishing the image.
- **C:** Incorrect for this question. A ConfigMap injects settings as environment variables or mounted files without rebuilding the image. Secrets still belong in Key Vault, not in a ConfigMap. Why the correct answer wins: Application settings become environment variables per slot, so a value change does not require rebuilding or republishing the image.
- **D:** Incorrect for this question. App Configuration separates configuration from code and supports labels, feature flags, and Key Vault references. Change still needs a refresh strategy. Why the correct answer wins: Application settings become environment variables per slot, so a value change does not require rebuilding or republishing the image.

### Question 99 — A

Answer: Use strong consistency for every read in the account. Strong consistency returns the most recent committed write for every read, which is what the fraud check requires. Strong consistency guarantees the latest committed write globally at the cost of higher latency and reduced availability during partitions. Local study-map skill 2.3 (Cosmos DB Consistency Levels), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Cosmos DB and PostgreSQL vector documentation: https://learn.microsoft.com/en-us/azure/cosmos-db/

- **A:** Correct. Strong consistency guarantees the latest committed write globally at the cost of higher latency and reduced availability during partitions. In this case: Strong consistency returns the most recent committed write for every read, which is what the fraud check requires.
- **B:** Incorrect for this question. Eventual consistency is the cheapest and most available option but returns possibly stale data. It fits non-critical counters, not balances. Why the correct answer wins: Strong consistency returns the most recent committed write for every read, which is what the fraud check requires.
- **C:** Incorrect for this question. Session consistency guarantees monotonic reads for one session and is the common default for user-facing apps. It does not promise global freshness. Why the correct answer wins: Strong consistency returns the most recent committed write for every read, which is what the fraud check requires.
- **D:** Incorrect for this question. Consistency trades freshness against latency, availability, and RU cost. The level is set at the account and can be relaxed per request. Why the correct answer wins: Strong consistency returns the most recent committed write for every read, which is what the fraud check requires.

### Question 100 — D

Answer: Publish to a Service Bus topic with multiple subscriptions. A topic with separate subscriptions delivers every event to each subscriber and tracks each subscription position separately. Topics fan out one message to independent subscribers, each with its own filter and dead-letter queue. Subscribers process at their own pace. Local study-map skill 3.2 (Service Bus Topics, Subscriptions, and Filters), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure messaging and Functions documentation: https://learn.microsoft.com/en-us/azure/service-bus-messaging/

- **A:** Incorrect for this question. Queue Storage is simple and cheap for large backlogs with at-least-once delivery. It lacks topics, sessions, and scheduled messages. Why the correct answer wins: A topic with separate subscriptions delivers every event to each subscriber and tracks each subscription position separately.
- **B:** Incorrect for this question. A custom schema fits domain events that are not resource lifecycle notifications. Consumers must version the schema contract. Why the correct answer wins: A topic with separate subscriptions delivers every event to each subscriber and tracks each subscription position separately.
- **C:** Incorrect for this question. A queue decouples producers from a single consumer group and smooths bursts. Delivery semantics depend on receive mode and completion. Why the correct answer wins: A topic with separate subscriptions delivers every event to each subscriber and tracks each subscription position separately.
- **D:** Correct. Topics fan out one message to independent subscribers, each with its own filter and dead-letter queue. Subscribers process at their own pace. In this case: A topic with separate subscriptions delivers every event to each subscriber and tracks each subscription position separately.
