# Microsoft AI-200 — Full-Length Mock Exam 3

Azure AI Cloud Developer Associate · 100 questions · expanded practice bank · passing target 700/1000

Blueprint-weighted mock exam of 100 items. Item mix: 84 multiple-choice (8 of them sequencing items with four candidate sequences), 16 multi-select (selection count stated), and 4 case studies of 3 questions. Hot-area, drag-and-drop UI, labs, and adaptive problem-solution sets cannot be reproduced in a CSV; see the README for the exact fidelity boundary.

Original educational content, not actual, recalled, or copied Microsoft exam items.

## Questions

### 1. A scoring API must pull its image locally in two regions and keep working when one region fails. What should be configured on the registry?

Domain: Develop containerized solutions on Azure

- A. Replicate the registry to each deployment region
- B. Run image builds on demand or on a trigger with ACR Tasks
- C. Deploy the mutable latest tag and let the platform resolve it
- D. Apply an ACR retention policy to prune old untagged manifests

### 2. Images must be rebuilt automatically whenever a base image security patch is published. What should be used?

Domain: Develop containerized solutions on Azure

- A. Replicate the registry to each deployment region
- B. Apply an ACR retention policy to prune old untagged manifests
- C. Run image builds on demand or on a trigger with ACR Tasks
- D. Build and store versioned images in Azure Container Registry

### 3. A small internal scoring endpoint needs platform patching, easy authentication, and deployment slots without cluster operations. What should host it?

Domain: Develop containerized solutions on Azure

- A. Deploy the image to Azure App Service as a web app
- B. Deploy the workload to Azure Kubernetes Service
- C. Deploy the service to Azure Container Apps
- D. Run the batch job in Azure Container Instances

### 4. A connection string with a key must be available to the container but must not appear in the portal settings. What should be used?

Domain: Develop containerized solutions on Azure

- A. Deploy the image to Azure App Service as a web app
- B. Stage the change in a deployment slot and swap after verification
- C. Supply configuration through App Service application settings
- D. Reference a Key Vault secret from the app configuration instead of storing it

### 5. The service must reach a database that is not exposed publicly and must accept only internal callers. What should be configured?

Domain: Develop containerized solutions on Azure

- A. Configure Container Apps ingress for internal-only access
- B. Deploy into a Container Apps environment attached to the workload virtual network
- C. Create a new Container Apps revision and shift traffic between revisions
- D. Scale the container app on an event source with a KEDA scaler

### 6. The queue scaler currently authenticates with a connection string stored in the environment. What should replace it?

Domain: Develop containerized solutions on Azure

- A. Scale on the Service Bus queue length with a KEDA Azure Service Bus scaler
- B. Tune the scale rule cool-down period and maximum replicas
- C. Scale the container app on an event source with a KEDA scaler
- D. Give the KEDA scaler a managed identity to read the event source

### 7. A pod must read a vault secret without a Kubernetes secret or stored credential. What should be configured?

Domain: Develop containerized solutions on Azure

- A. Store the secret in Azure Key Vault and read it at runtime
- B. Add readiness and liveness probes to the pod specification
- C. Federate a Kubernetes service account to a managed identity
- D. Authenticate with a managed identity instead of a stored key

### 8. You must keep release artifacts immutable and stop the registry growing without limit. Which two actions should you take? Select two.

Domain: Develop containerized solutions on Azure

- A. Deploy the mutable latest tag and let the platform resolve it
- B. Apply an ACR retention policy to prune old untagged manifests
- C. Stage the change in a deployment slot and swap after verification
- D. Replicate the registry to each deployment region
- E. Build and store versioned images in Azure Container Registry

### 9. An incident review cannot tell which build produced a faulty deployment. What should be enforced first?

Domain: Develop containerized solutions on Azure

- A. Run image builds on demand or on a trigger with ACR Tasks
- B. Deploy the mutable latest tag and let the platform resolve it
- C. Replicate the registry to each deployment region
- D. Build and store versioned images in Azure Container Registry

### 10. A fraud endpoint must serve a canary release and must stay warm during business hours. Which two settings provide that? Select two.

Domain: Develop containerized solutions on Azure

- A. Scale the container app on an event source with a KEDA scaler
- B. Set a minimum replica count above zero for the container app
- C. Rely on the horizontal pod autoscaler on CPU
- D. Run the batch job in Azure Container Instances
- E. Create a new Container Apps revision and shift traffic between revisions

### 11. Which sequence correctly promotes a scoring revision with a canary?

Domain: Develop containerized solutions on Azure

- A. Check metrics → deploy a new revision → build and push the image → shift a small traffic percentage → promote
- B. Shift all traffic to a new revision → deploy the revision → check metrics → build the image → promote
- C. Deploy a new revision → shift all traffic → build and push the image → check metrics → roll back
- D. Build and push the image → deploy a new revision → shift a small traffic percentage → check metrics → promote or roll back

### 12. A transaction lookup by card token and month must not scan the entire container. What should the query do?

Domain: Develop AI solutions by using Azure data management services

- A. Include the partition key in the query predicate
- B. Increase provisioned throughput and watch the RU charge per query
- C. Store the documents in Azure Cosmos DB for NoSQL
- D. Query through the Cosmos DB SDK with parameterized queries

### 13. A high-write ledger container indexes fields that no query filters on. What should change?

Domain: Develop AI solutions by using Azure data management services

- A. Restrict the indexing policy to the paths the queries use
- B. Index every property by using the default automatic policy
- C. Enable autoscale throughput with a maximum RU limit
- D. Set an item time-to-live on the container

### 14. A customer must see their own submitted payment as pending on the next request. Which level fits at the lowest cost?

Domain: Develop AI solutions by using Azure data management services

- A. Choose the account consistency level that matches the read requirement
- B. Use strong consistency for every read in the account
- C. Use session consistency for reads within the same client session
- D. Use eventual consistency to minimize read cost

### 15. A new embedding model produces different dimensions, and vector writes now fail. What must change?

Domain: Develop AI solutions by using Azure data management services

- A. Store embeddings in a vector property and query with VectorDistance
- B. Scan every document and compute similarity in application code
- C. Use the DiskANN vector index for large collections
- D. Declare the embedding dimensions and vector index type on the container policy

### 16. Each new transaction must be scored asynchronously without querying the whole container. What should be used?

Domain: Develop AI solutions by using Azure data management services

- A. Use a lease container to coordinate change feed readers
- B. Set an item time-to-live on the container
- C. Run a change feed processor to react to new and updated items
- D. Batch related writes in a transactional batch within one partition key

### 17. A transfer must write its debit and credit documents atomically when both share a partition key. What should be used?

Domain: Develop AI solutions by using Azure data management services

- A. Set an item time-to-live on the container
- B. Increase provisioned throughput and watch the RU charge per query
- C. Batch related writes in a transactional batch within one partition key
- D. Run a change feed processor to react to new and updated items

### 18. Fraud features must be filtered by merchant category and matched by embedding in one query. What should the table look like?

Domain: Develop AI solutions by using Azure data management services

- A. Store embeddings in PostgreSQL by using the pgvector extension
- B. Add a read replica and send all vector queries to it
- C. Scale compute and memory to fit index size and query concurrency
- D. Model typed columns for filters and one vector column for the embedding

### 19. A nearest-neighbour query became slow after a data reload, and the team is unsure which index is used. What should be done first?

Domain: Develop AI solutions by using Azure data management services

- A. Create an HNSW index for low-latency approximate search
- B. Create an IVFFlat index to save memory on a large table
- C. Inspect the plan with EXPLAIN ANALYZE before changing indexes
- D. Increase maintenance and query memory settings for index builds and sorts

### 20. Building a large index blocks the maintenance window because storage throughput is exhausted. What should be addressed?

Domain: Develop AI solutions by using Azure data management services

- A. Reuse a bounded connection pool instead of opening a connection per request
- B. Increase storage throughput for index builds and bulk loads
- C. Increase maintenance and query memory settings for index builds and sorts
- D. Scale compute and memory to fit index size and query concurrency

### 21. The API repeats the same three queries thousands of times per minute. What should be used to avoid repeated planning?

Domain: Develop AI solutions by using Azure data management services

- A. Place a connection pooler in front of PostgreSQL for many short-lived clients
- B. Add a read replica and send all vector queries to it
- C. Reuse a bounded connection pool instead of opening a connection per request
- D. Use prepared statements and batch round trips

### 22. A limit change must be reflected in cached decisions immediately, not minutes later. What is required?

Domain: Develop AI solutions by using Azure data management services

- A. Set a TTL on each cached entry
- B. Invalidate or overwrite the cache entry when the source changes
- C. Flush the database after each deployment to guarantee fresh data
- D. Rely on the eviction policy and skip explicit TTLs

### 23. Fraud patterns must be matched against known bad patterns with sub-10-millisecond latency from memory. What should be used?

Domain: Develop AI solutions by using Azure data management services

- A. Cache responses in Azure Managed Redis
- B. Store user session state in Managed Redis with an expiry
- C. Use a distributed lock in Redis to make processing idempotent
- D. Create a vector index in Managed Redis for similarity search

### 24. You must choose a vector index for two different tables. Which two statements should guide the choice? Select two.

Domain: Develop AI solutions by using Azure data management services

- A. Create an IVFFlat index to save memory on a large table
- B. Increase maintenance and query memory settings for index builds and sorts
- C. Create an HNSW index for low-latency approximate search
- D. Increase storage throughput for index builds and bulk loads
- E. Query without a vector index and let PostgreSQL scan the table

### 25. Which sequence correctly builds a vector-enabled container for pattern matching?

Domain: Develop AI solutions by using Azure data management services

- A. Apply metadata filters → query with VectorDistance → create the container with a vector policy → upsert items with embeddings
- B. Create the container with a vector policy → upsert items with embeddings → query with VectorDistance → apply metadata filters
- C. Upsert items with embeddings → create the container with a vector policy → apply metadata filters → query with VectorDistance
- D. Query with VectorDistance → upsert items with embeddings → create the container with a vector policy → apply metadata filters

### 26. Score adjustments for one card must be applied in order by a single consumer. What should be enabled?

Domain: Connect to and consume Azure services

- A. Queue the work on a Service Bus queue and process it with a worker
- B. Publish to a Service Bus topic with multiple subscriptions
- C. Use Service Bus sessions to keep related messages ordered
- D. Receive with peek-lock and complete or abandon explicitly

### 27. Authorisation, fraud review, and audit must each receive the same transaction event independently. What should be used?

Domain: Connect to and consume Azure services

- A. Use Azure Queue Storage for the work items
- B. Publish to a Service Bus topic with multiple subscriptions
- C. Define a custom event schema for the topic
- D. Queue the work on a Service Bus queue and process it with a worker

### 28. A producer retries sends during a network blip, and the consumer sees the same transaction twice within a short window. Which feature helps?

Domain: Connect to and consume Azure services

- A. Set a maximum delivery count and handle the dead-letter path
- B. Use Service Bus sessions to keep related messages ordered
- C. Enable duplicate detection on the queue
- D. Make the handler idempotent by using a message or business key

### 29. Event delivery must not depend on a shared access key. What should be configured?

Domain: Connect to and consume Azure services

- A. Filter the Event Grid subscription by subject or event type
- B. Deliver events by using a managed identity instead of a key
- C. Rely on Event Grid retries with a dead-letter destination
- D. Subscribe to a system topic for resource events

### 30. A dispute workflow must wait for an external decision and resume days later without a running host. What should be used?

Domain: Connect to and consume Azure services

- A. Move long-running work out of the HTTP request into a queue
- B. Expose the endpoint through an HTTP trigger
- C. Orchestrate the multi-step workflow with Durable Functions
- D. Bind a queue or event trigger to the function

### 31. An HTTP-triggered request times out while a long dispute assessment runs. What should change?

Domain: Connect to and consume Azure services

- A. Host the function app on the consumption plan
- B. Move long-running work out of the HTTP request into a queue
- C. Expose the endpoint through an HTTP trigger
- D. Host the function app on a premium plan with pre-warmed instances

### 32. Billing must receive only high-value transactions, and reminders must become visible at a future time. Which two capabilities provide that? Select two.

Domain: Connect to and consume Azure services

- A. Use Service Bus sessions to keep related messages ordered
- B. Schedule the message for future enqueueing
- C. Enable duplicate detection on the queue
- D. Add a SQL or correlation filter to a subscription
- E. Inspect the dead-letter queue and resubmit corrected messages

### 33. A failing message must not loop and must be preserved for investigation. Which two capabilities address that? Select two.

Domain: Connect to and consume Azure services

- A. Enable duplicate detection on the queue
- B. Receive in receive-and-delete mode for at-most-once delivery
- C. Inspect the dead-letter queue and resubmit corrected messages
- D. Set a maximum delivery count and handle the dead-letter path
- E. Use Service Bus sessions to keep related messages ordered

### 34. Which sequence correctly delivers a custom fraud event?

Domain: Connect to and consume Azure services

- A. Publish a custom event → evaluate the subscription filter → deliver to the handler → retry on failure → dead-letter undeliverable events
- B. Evaluate the subscription filter → publish a custom event → dead-letter undeliverable events → deliver to the handler → retry on failure
- C. Deliver to the handler → publish a custom event → evaluate the subscription filter → retry on failure → dead-letter undeliverable events
- D. Publish a custom event → deliver to the handler → evaluate the subscription filter → dead-letter undeliverable events → retry on failure

### 35. An acquirer credential must be auditable and revocable per environment. Where should it live?

Domain: Secure, monitor, troubleshoot Azure solutions

- A. Store settings and feature flags in Azure App Configuration
- B. Pin the application to a specific secret version
- C. Store the secret in Azure Key Vault and read it at runtime
- D. Supply configuration through App Service application settings

### 36. A non-secret threshold lives in App Configuration but its value must stay in the vault. What should be used?

Domain: Secure, monitor, troubleshoot Azure solutions

- A. Supply configuration through App Service application settings
- B. Store settings and feature flags in Azure App Configuration
- C. Reference the Key Vault secret from an App Configuration key value
- D. Store the secret in Azure Key Vault and read it at runtime

### 37. The same keys must hold different values for test and production in one store. What should be used?

Domain: Secure, monitor, troubleshoot Azure solutions

- A. Pin the application to a specific secret version
- B. Use App Configuration labels to separate environments
- C. Store settings and feature flags in Azure App Configuration
- D. Enable configuration refresh so changes apply without a restart

### 38. Trace volume costs more than the service it monitors, but rare failures must still be retained. What should be configured?

Domain: Secure, monitor, troubleshoot Azure solutions

- A. Use head or tail sampling so trace volume stays within budget
- B. Propagate trace context across every service and queue hop
- C. Export telemetry through an OpenTelemetry collector
- D. Instrument the service with the OpenTelemetry SDK

### 39. A dashboard recomputes the same hourly aggregation over millions of rows all day. What should be considered?

Domain: Secure, monitor, troubleshoot Azure solutions

- A. Store repeated aggregations in a materialized view or update policy
- B. Project only the columns needed and filter by time first
- C. Aggregate with summarize and bin to see the failure rate over time
- D. Join the requests and dependencies tables on the operation ID

### 40. The ledger database must not be reachable from the public internet, and the app runs in a Container Apps environment. What should be configured?

Domain: Secure, monitor, troubleshoot Azure solutions

- A. Reach the data service through a private endpoint
- B. Link the private DNS zone so the private endpoint name resolves
- C. Authenticate with a managed identity instead of a stored key
- D. Assign a least-privilege role to the application identity

### 41. Pods must call the data service without stored secrets and with only the operations they need. Which two actions should you take? Select two.

Domain: Secure, monitor, troubleshoot Azure solutions

- A. Reach the data service through a private endpoint
- B. Store the secret in Azure Key Vault and read it at runtime
- C. Assign a least-privilege role to the application identity
- D. Federate a Kubernetes service account to a managed identity
- E. Alert on platform metrics rather than only on log queries

### 42. A secret must be vaulted and readable by the app identity. Which two actions are required? Select two.

Domain: Secure, monitor, troubleshoot Azure solutions

- A. Store the secret in Azure Key Vault and read it at runtime
- B. Grant the app identity data-plane access to the vault
- C. Pin the application to a specific secret version
- D. Use App Configuration labels to separate environments
- E. Store settings and feature flags in Azure App Configuration

### 43. Which sequence correctly rotates a credential used by a deployed service?

Domain: Secure, monitor, troubleshoot Azure solutions

- A. Reference the secret from the app → rotate the secret → store the secret in Key Vault → grant the app identity access → the app reads the new version
- B. Rotate the secret → reference the secret from the app → store the secret in Key Vault → grant the app identity access → the app reads the new version
- C. Grant the app identity access → store the secret in Key Vault → rotate the secret → reference the secret from the app → the app reads the new version
- D. Store the secret in Key Vault → grant the app identity access → reference the secret from the app → rotate the secret → the app reads the new version

### 44. Card events must stay ordered per card, and a crashed consumer must not lose a message it had locked. Which two features are required? Select two.

Domain: Connect to and consume Azure services

- A. Receive with peek-lock and complete or abandon explicitly
- B. Add a SQL or correlation filter to a subscription
- C. Enable duplicate detection on the queue
- D. Receive in receive-and-delete mode for at-most-once delivery
- E. Use Service Bus sessions to keep related messages ordered

### 45. Fraud-scoring images must be built and stored in a private registry that the cluster can pull from with its own identity. What should be used?

Domain: Develop containerized solutions on Azure

- A. Deploy the image to Azure App Service as a web app
- B. Deploy the mutable latest tag and let the platform resolve it
- C. Run the batch job in Azure Container Instances
- D. Build and store versioned images in Azure Container Registry

### 46. Every commit to the scoring repository must produce a rebuilt, tagged image with no build agent to maintain. What should perform the build?

Domain: Develop containerized solutions on Azure

- A. Deploy the service to Azure Container Apps
- B. Build and store versioned images in Azure Container Registry
- C. Run image builds on demand or on a trigger with ACR Tasks
- D. Deploy the workload to Azure Kubernetes Service

### 47. Each environment needs a different fraud score threshold, and the value must change without rebuilding the image. What should supply it?

Domain: Develop containerized solutions on Azure

- A. Supply configuration through App Service application settings
- B. Store settings and feature flags in Azure App Configuration
- C. Pin the application to a specific secret version
- D. Mount non-secret configuration from a Kubernetes ConfigMap

### 48. The payment processor key must never appear in deployment settings or in the repository. What should the app configuration use?

Domain: Develop containerized solutions on Azure

- A. Reference a Key Vault secret from the app configuration instead of storing it
- B. Pin the application to a specific secret version
- C. Supply configuration through App Service application settings
- D. Mount non-secret configuration from a Kubernetes ConfigMap

### 49. The scoring API must accept calls only from the settlement service in the same Container Apps environment. What should be configured?

Domain: Develop containerized solutions on Azure

- A. Stage the change in a deployment slot and swap after verification
- B. Configure Container Apps ingress for internal-only access
- C. Create a new Container Apps revision and shift traffic between revisions
- D. Scale the container app on an event source with a KEDA scaler

### 50. A new scoring model must take five percent of live decisions while the incumbent keeps the rest. What should be used?

Domain: Develop containerized solutions on Azure

- A. Stage the change in a deployment slot and swap after verification
- B. Create a new Container Apps revision and shift traffic between revisions
- C. Rely on the horizontal pod autoscaler on CPU
- D. Replicate the registry to each deployment region

### 51. A batch scoring deployment on AKS must add pods when average CPU exceeds seventy percent. What should be configured?

Domain: Develop containerized solutions on Azure

- A. Rely on the horizontal pod autoscaler on CPU
- B. Apply a declarative Kubernetes manifest to the cluster
- C. Add readiness and liveness probes to the pod specification
- D. Run the batch job in Azure Container Instances

### 52. Scoring pods restart several times a day with exit code 137 during peak settlement. Where should the memory evidence be gathered?

Domain: Develop containerized solutions on Azure

- A. Aggregate with summarize and bin to see the failure rate over time
- B. Add readiness and liveness probes to the pod specification
- C. Enable diagnostic settings to route platform logs to the workspace
- D. Query container logs and Kubernetes events in Log Analytics

### 53. The platform team wants control-plane and cluster-level logs routed to the central workspace. What should be enabled?

Domain: Develop containerized solutions on Azure

- A. Enable diagnostic settings to route platform logs to the workspace
- B. Alert on platform metrics rather than only on log queries
- C. Project only the columns needed and filter by time first
- D. Query container logs and Kubernetes events in Log Analytics

### 54. Scoring images must be traceable to one build and must pull quickly in two regions. Which two actions should you take? Select two.

Domain: Develop containerized solutions on Azure

- A. Replicate the registry to each deployment region
- B. Deploy the mutable latest tag and let the platform resolve it
- C. Build and store versioned images in Azure Container Registry
- D. Apply an ACR retention policy to prune old untagged manifests
- E. Stage the change in a deployment slot and swap after verification

### 55. Which sequence correctly builds and releases a scoring image to the cluster?

Domain: Develop containerized solutions on Azure

- A. Build the image → deploy the latest tag → scan it → push a versioned tag → verify health
- B. Push a versioned tag to ACR → build the image → deploy that tag → scan it → verify health
- C. Build the image → scan it → push a versioned tag to ACR → deploy that tag → verify health
- D. Scan the image → build the image → verify health → push a versioned tag → deploy that tag

### 56. Transaction events are queried by transaction identifier and writes must spread evenly across partitions. What should the container use?

Domain: Develop AI solutions by using Azure data management services

- A. Index every property by using the default automatic policy
- B. Include the partition key in the query predicate
- C. Choose a high-cardinality partition key that spreads writes
- D. Increase provisioned throughput and watch the RU charge per query

### 57. Scoring lookups must use the supported SDK with parameters instead of string-built queries. What should be implemented?

Domain: Develop AI solutions by using Azure data management services

- A. Query through the Cosmos DB SDK with parameterized queries
- B. Scan every document and compute similarity in application code
- C. Include the partition key in the query predicate
- D. Enable duplicate detection on the queue

### 58. A lookup by transaction identifier consumes far more request charge than the document size implies. What should be corrected?

Domain: Develop AI solutions by using Azure data management services

- A. Include the partition key in the query predicate
- B. Choose a high-cardinality partition key that spreads writes
- C. Increase provisioned throughput and watch the RU charge per query
- D. Restrict the indexing policy to the paths the queries use

### 59. Twenty related ledger writes for one account holder must succeed or fail together. What should be used?

Domain: Develop AI solutions by using Azure data management services

- A. Enable autoscale throughput with a maximum RU limit
- B. Index every property by using the default automatic policy
- C. Increase provisioned throughput and watch the RU charge per query
- D. Batch related writes in a transactional batch within one partition key

### 60. A cardholder must immediately see the transaction they just submitted, and global ordering across regions is not required. Which consistency choice fits?

Domain: Develop AI solutions by using Azure data management services

- A. Choose the account consistency level that matches the read requirement
- B. Use session consistency for reads within the same client session
- C. Use strong consistency for every read in the account
- D. Use eventual consistency to minimize read cost

### 61. The fraud model compares every transaction against a vector set too large to hold in memory. Which index fits?

Domain: Develop AI solutions by using Azure data management services

- A. Scan every document and compute similarity in application code
- B. Use the DiskANN vector index for large collections
- C. Store embeddings in PostgreSQL by using the pgvector extension
- D. Create a vector index in Managed Redis for similarity search

### 62. A ledger query became slow after a new filter was added, and the index choice is unclear. What should be inspected first?

Domain: Develop AI solutions by using Azure data management services

- A. Inspect the plan with EXPLAIN ANALYZE before changing indexes
- B. Add a read replica and send all vector queries to it
- C. Run VACUUM and ANALYZE after bulk loads and large deletes
- D. Increase storage throughput for index builds and bulk loads

### 63. A forty-million-row ledger load is limited by disk throughput rather than CPU or memory. What should be increased?

Domain: Develop AI solutions by using Azure data management services

- A. Add a read replica and send all vector queries to it
- B. Scale compute and memory to fit index size and query concurrency
- C. Inspect the plan with EXPLAIN ANALYZE before changing indexes
- D. Increase storage throughput for index builds and bulk loads

### 64. A single scoring call issues six sequential round trips to PostgreSQL for the same shape of query. What should be used?

Domain: Develop AI solutions by using Azure data management services

- A. Add a read replica and send all vector queries to it
- B. Use prepared statements and batch round trips
- C. Reuse a bounded connection pool instead of opening a connection per request
- D. Place a connection pooler in front of PostgreSQL for many short-lived clients

### 65. Two settlement workers occasionally process the same transaction because a redelivery arrives mid-flight. What should be added?

Domain: Develop AI solutions by using Azure data management services

- A. Use a distributed lock in Redis to make processing idempotent
- B. Flush the database after each deployment to guarantee fresh data
- C. Rely on the eviction policy and skip explicit TTLs
- D. Set a TTL on each cached entry

### 66. Fraud similarity search must answer in milliseconds and the index must stay resident in memory. Which two actions should you take? Select two.

Domain: Develop AI solutions by using Azure data management services

- A. Query without a vector index and let PostgreSQL scan the table
- B. Scale compute and memory to fit index size and query concurrency
- C. Create an IVFFlat index to save memory on a large table
- D. Increase storage throughput for index builds and bulk loads
- E. Create an HNSW index for low-latency approximate search

### 67. A scoring API must bound its database connections and must stop repeating identical round trips. Which two actions should you take? Select two.

Domain: Develop AI solutions by using Azure data management services

- A. Reuse a bounded connection pool instead of opening a connection per request
- B. Add a read replica and send all vector queries to it
- C. Place a connection pooler in front of PostgreSQL for many short-lived clients
- D. Increase storage throughput for index builds and bulk loads
- E. Use prepared statements and batch round trips

### 68. Which sequence correctly starts a change feed processor on the fraud ledger?

Domain: Develop AI solutions by using Azure data management services

- A. Enable the change feed on the container → create a lease container → start the processor with a unique instance name → read inserts and updates in order → checkpoint the continuation
- B. Read inserts and updates in order → start the processor → create a lease container → enable the change feed → checkpoint the continuation
- C. Create a lease container → enable the change feed → checkpoint the continuation → start the processor → read inserts and updates in order
- D. Start the processor with a unique instance name → read inserts and updates → enable the change feed → create a lease container → checkpoint the continuation

### 69. Settlement messages for one cardholder must be handled in order by a single worker. What should be enabled?

Domain: Connect to and consume Azure services

- A. Receive with peek-lock and complete or abandon explicitly
- B. Use Service Bus sessions to keep related messages ordered
- C. Set a maximum delivery count and handle the dead-letter path
- D. Enable duplicate detection on the queue

### 70. A worker fails after taking a payment but before the message is removed, and the work must not vanish. Which receive mode should be used?

Domain: Connect to and consume Azure services

- A. Enable duplicate detection on the queue
- B. Receive with peek-lock and complete or abandon explicitly
- C. Receive in receive-and-delete mode for at-most-once delivery
- D. Use prepared statements and batch round trips

### 71. Only payment events above ten thousand dollars should reach the enhanced-review subscription. What should be configured?

Domain: Connect to and consume Azure services

- A. Define a custom event schema for the topic
- B. Add a SQL or correlation filter to a subscription
- C. Filter the Event Grid subscription by subject or event type
- D. Stream telemetry through Azure Event Hubs

### 72. A domain event that is not a resource lifecycle change must be published with a schema the bank controls. What should be used?

Domain: Connect to and consume Azure services

- A. Rely on Event Grid retries with a dead-letter destination
- B. Subscribe to a system topic for resource events
- C. Define a custom event schema for the topic
- D. Stream telemetry through Azure Event Hubs

### 73. A fraud review must pause for a human decision for up to two days and survive function restarts. What should be used?

Domain: Connect to and consume Azure services

- A. Expose the endpoint through an HTTP trigger
- B. Orchestrate the multi-step workflow with Durable Functions
- C. Bind a queue or event trigger to the function
- D. Use input and output bindings instead of hand-written SDK calls

### 74. A nightly reconciliation job runs for ten minutes a day and cost must stay minimal. Which hosting plan fits?

Domain: Connect to and consume Azure services

- A. Host the function app on the consumption plan
- B. Host the function app on a premium plan with pre-warmed instances
- C. Run the scheduled maintenance from a timer trigger
- D. Orchestrate the multi-step workflow with Durable Functions

### 75. The payment gateway intermittently returns 429, and an immediate retry makes the throttling worse. What should be configured?

Domain: Connect to and consume Azure services

- A. Deploy the function app through a CI pipeline with app settings applied
- B. Tune the function app concurrency and batch size
- C. Host the function app on a premium plan with pre-warmed instances
- D. Configure the host retry policy with exponential backoff

### 76. Per-cardholder ordering is required and repeated publishes must not create double settlement. Which two features should you enable? Select two.

Domain: Connect to and consume Azure services

- A. Receive with peek-lock and complete or abandon explicitly
- B. Receive in receive-and-delete mode for at-most-once delivery
- C. Enable duplicate detection on the queue
- D. Inspect the dead-letter queue and resubmit corrected messages
- E. Use Service Bus sessions to keep related messages ordered

### 77. Poison messages must stop looping and must remain available for investigation. Which two capabilities are required? Select two.

Domain: Connect to and consume Azure services

- A. Enable duplicate detection on the queue
- B. Receive with peek-lock and complete or abandon explicitly
- C. Inspect the dead-letter queue and resubmit corrected messages
- D. Receive in receive-and-delete mode for at-most-once delivery
- E. Set a maximum delivery count and handle the dead-letter path

### 78. Which sequence correctly settles one payment message without losing it on failure?

Domain: Connect to and consume Azure services

- A. Publish the message → complete the message → receive with peek-lock → process the work → dead-letter after the delivery limit
- B. Receive with peek-lock → publish the message → complete the message → process the work → dead-letter after the delivery limit
- C. Publish the message → receive with peek-lock → process the work → complete the message → dead-letter after the delivery limit
- D. Process the work → receive with peek-lock → publish the message → complete the message → dead-letter after the delivery limit

### 79. An audit must reproduce a decision with the exact secret version that was used at the time. What should the app use?

Domain: Secure, monitor, troubleshoot Azure solutions

- A. Authenticate with a managed identity instead of a stored key
- B. Rotate the secret on a schedule and let apps resolve the current version
- C. Enable purge protection and soft delete on the vault
- D. Pin the application to a specific secret version

### 80. An accidental vault deletion must remain recoverable for the regulated retention window. What should be enabled?

Domain: Secure, monitor, troubleshoot Azure solutions

- A. Enable purge protection and soft delete on the vault
- B. Rotate the secret on a schedule and let apps resolve the current version
- C. Store the secret in Azure Key Vault and read it at runtime
- D. Grant the app identity data-plane access to the vault

### 81. Development, test, and production settings must share one store without colliding. What should separate them?

Domain: Secure, monitor, troubleshoot Azure solutions

- A. Store settings and feature flags in Azure App Configuration
- B. Use App Configuration labels to separate environments
- C. Enable configuration refresh so changes apply without a restart
- D. Pin the application to a specific secret version

### 82. Spans must be forwarded to the bank's existing observability backend without changing application code again. What should be added?

Domain: Secure, monitor, troubleshoot Azure solutions

- A. Correlate logs with the operation or trace identifier
- B. Send telemetry to Application Insights and inspect the transaction view
- C. Instrument the service with the OpenTelemetry SDK
- D. Export telemetry through an OpenTelemetry collector

### 83. Peak traffic produces more traces than the observability budget allows, yet slow transactions must still be captured. What should be configured?

Domain: Secure, monitor, troubleshoot Azure solutions

- A. Correlate logs with the operation or trace identifier
- B. Use head or tail sampling so trace volume stays within budget
- C. Create a custom span around each downstream call
- D. Propagate trace context across every service and queue hop

### 84. The scoring service must reach the ledger without traversing the public internet. What should be configured?

Domain: Secure, monitor, troubleshoot Azure solutions

- A. Enable diagnostic settings to route platform logs to the workspace
- B. Link the private DNS zone so the private endpoint name resolves
- C. Test end-to-end connectivity from inside the container to each dependency
- D. Reach the data service through a private endpoint

### 85. Logs must be joinable to traces and the trace must survive a queue hop. Which two actions should you take? Select two.

Domain: Secure, monitor, troubleshoot Azure solutions

- A. Send telemetry to Application Insights and inspect the transaction view
- B. Correlate logs with the operation or trace identifier
- C. Propagate trace context across every service and queue hop
- D. Create a custom span around each downstream call
- E. Use head or tail sampling so trace volume stays within budget

### 86. On-call must be paged when the decline rate spikes and the page must reach a named team. Which two components are required? Select two.

Domain: Secure, monitor, troubleshoot Azure solutions

- A. Create an alert rule on the failure rate or latency metric
- B. Project only the columns needed and filter by time first
- C. Route the alert to an action group with a named owner
- D. Set the workspace retention and table plan to control log cost
- E. Alert on platform metrics rather than only on log queries

### 87. A new scoring threshold must ship in code before it is enabled and must be changeable without a deploy. Which two features are required? Select two.

Domain: Secure, monitor, troubleshoot Azure solutions

- A. Store settings and feature flags in Azure App Configuration
- B. Enable configuration refresh so changes apply without a restart
- C. Reference the Key Vault secret from an App Configuration key value
- D. Use App Configuration labels to separate environments
- E. Ship the code dark behind a feature flag

### 88. Which sequence correctly moves a scoring app from a stored key to identity-based private access?

Domain: Secure, monitor, troubleshoot Azure solutions

- A. Move the credential into Key Vault → disable public network access → verify the call from inside the app → assign a managed identity to the app → grant the least-privilege data-plane role
- B. Assign a managed identity to the app → grant the least-privilege data-plane role → move the credential into Key Vault → disable public network access behind a private endpoint → verify the call from inside the app
- C. Verify the call from inside the app → assign a managed identity to the app → move the credential into Key Vault → disable public network access → grant the least-privilege data-plane role
- D. Disable public network access behind a private endpoint → assign a managed identity to the app → grant the least-privilege data-plane role → verify the call from inside the app → move the credential into Key Vault

---

## Case study — FraudDesk

The next three questions refer to this scenario. Read the full scenario before answering; case-study items are scored individually.

### 89. Only cases the analyst is assigned to may appear in results, and the result count must stay complete. What should the query do?

Domain: Develop AI solutions by using Azure data management services

- A. Retrieve nearest neighbours first and discard unauthorized rows in the application
- B. Query without a vector index and let PostgreSQL scan the table
- C. Create an HNSW index for low-latency approximate search
- D. Filter on metadata columns in the same query as the vector search

### 90. A fraud model update must notify subscribers even though it is not an Azure resource change. What should be published?

Domain: Connect to and consume Azure services

- A. Filter the Event Grid subscription by subject or event type
- B. Subscribe to a system topic for resource events
- C. Rely on Event Grid retries with a dead-letter destination
- D. Define a custom event schema for the topic

### 91. A leaked credential must be replaced with no downtime, and the old value must stop working immediately. What should be done?

Domain: Secure, monitor, troubleshoot Azure solutions

- A. Enable purge protection and soft delete on the vault
- B. Pin the application to a specific secret version
- C. Rotate the secret on a schedule and let apps resolve the current version
- D. Authenticate with a managed identity instead of a stored key

---

## Case study — LedgerOne

The next three questions refer to this scenario. Read the full scenario before answering; case-study items are scored individually.

### 92. After the connection string was removed, the container app stopped scaling and its scale rule reports an authorization failure. What should be granted?

Domain: Develop containerized solutions on Azure

- A. Give the KEDA scaler a managed identity to read the event source
- B. Scale only on CPU utilization without an event scaler
- C. Rely on the horizontal pod autoscaler on CPU
- D. Scale on the Service Bus queue length with a KEDA Azure Service Bus scaler

### 93. Retrieval must return only chunks belonging to the calling bank and must still return five results. What should the query do?

Domain: Develop AI solutions by using Azure data management services

- A. Place a connection pooler in front of PostgreSQL for many short-lived clients
- B. Filter on metadata columns in the same query as the vector search
- C. Retrieve nearest neighbours first and discard unauthorized rows in the application
- D. Create an HNSW index for low-latency approximate search

### 94. Settlement, fraud, and notification must each receive every payment event with their own cursor. What should be used?

Domain: Connect to and consume Azure services

- A. Publish to a Service Bus topic with multiple subscriptions
- B. Use Azure Queue Storage for the work items
- C. Define a custom event schema for the topic
- D. Queue the work on a Service Bus queue and process it with a worker

---

## Case study — PaymentsGate

The next three questions refer to this scenario. Read the full scenario before answering; case-study items are scored individually.

### 95. A pod reports ready but cannot reach the Redis cache, and the same test works from a jump host. What should be verified?

Domain: Develop containerized solutions on Azure

- A. Enable diagnostic settings to route platform logs to the workspace
- B. Add readiness and liveness probes to the pod specification
- C. Test end-to-end connectivity from inside the container to each dependency
- D. Query container logs and Kubernetes events in Log Analytics

### 96. A message with an invalid schema is retried indefinitely and starves other work. What should be configured?

Domain: Connect to and consume Azure services

- A. Receive in receive-and-delete mode for at-most-once delivery
- B. Enable duplicate detection on the queue
- C. Set a maximum delivery count and handle the dead-letter path
- D. Receive with peek-lock and complete or abandon explicitly

### 97. On-call needs a fast alert on request failure rate without paying for repeated log scans. What should be used?

Domain: Secure, monitor, troubleshoot Azure solutions

- A. Aggregate with summarize and bin to see the failure rate over time
- B. Alert on platform metrics rather than only on log queries
- C. Create an alert rule on the failure rate or latency metric
- D. Project only the columns needed and filter by time first

---

## Case study — VaultTrust

The next three questions refer to this scenario. Read the full scenario before answering; case-study items are scored individually.

### 98. Rebuilding the fraud vector index on the ledger table blocks settlement writes for forty minutes. What should the build use?

Domain: Develop AI solutions by using Azure data management services

- A. Build the vector index concurrently so writes are not blocked
- B. Increase storage throughput for index builds and bulk loads
- C. Run VACUUM and ANALYZE after bulk loads and large deletes
- D. Scale compute and memory to fit index size and query concurrency

### 99. A poisoned settlement message is redelivered forever and occupies a worker each time. What should be configured?

Domain: Connect to and consume Azure services

- A. Receive with peek-lock and complete or abandon explicitly
- B. Enable duplicate detection on the queue
- C. Inspect the dead-letter queue and resubmit corrected messages
- D. Set a maximum delivery count and handle the dead-letter path

### 100. The daily settlement dashboard aggregates ninety days of ledger logs and times out on every refresh. What should be used?

Domain: Secure, monitor, troubleshoot Azure solutions

- A. Join the requests and dependencies tables on the operation ID
- B. Aggregate with summarize and bin to see the failure rate over time
- C. Project only the columns needed and filter by time first
- D. Store repeated aggregations in a materialized view or update policy

---

## Answer key and explanations

### Question 1 — A

Answer: Replicate the registry to each deployment region. Geo-replication puts an image copy in each region, reducing pull latency and surviving a regional outage. Geo-replication reduces cross-region pull latency and gives a local copy during a regional failure. It adds cost and replication management. Local study-map skill 1.1 (Container Image Lifecycle in Azure Container Registry), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure container hosting documentation: https://learn.microsoft.com/en-us/azure/container-apps/

- **A:** Correct. Geo-replication reduces cross-region pull latency and gives a local copy during a regional failure. It adds cost and replication management. In this case: Geo-replication puts an image copy in each region, reducing pull latency and surviving a regional outage.
- **B:** Incorrect for this question. ACR Tasks builds images in Azure on a commit or schedule without a local Docker host. It removes build-host drift but not image review. Why the correct answer wins: Geo-replication puts an image copy in each region, reducing pull latency and surviving a regional outage.
- **C:** Incorrect for this question. A floating tag removes the link between a deployed revision and a specific build, so rollback and audit become guesswork. Why the correct answer wins: Geo-replication puts an image copy in each region, reducing pull latency and surviving a regional outage.
- **D:** Incorrect for this question. A retention policy controls storage growth and registry clutter. It does not change which image tag a deployment references. Why the correct answer wins: Geo-replication puts an image copy in each region, reducing pull latency and surviving a regional outage.

### Question 2 — C

Answer: Run image builds on demand or on a trigger with ACR Tasks. An ACR Task triggered by a base image update rebuilds the affected images without a local build host. ACR Tasks builds images in Azure on a commit or schedule without a local Docker host. It removes build-host drift but not image review. Local study-map skill 1.2 (Automated Image Builds with ACR Tasks), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure container hosting documentation: https://learn.microsoft.com/en-us/azure/container-apps/

- **A:** Incorrect for this question. Geo-replication reduces cross-region pull latency and gives a local copy during a regional failure. It adds cost and replication management. Why the correct answer wins: An ACR Task triggered by a base image update rebuilds the affected images without a local build host.
- **B:** Incorrect for this question. A retention policy controls storage growth and registry clutter. It does not change which image tag a deployment references. Why the correct answer wins: An ACR Task triggered by a base image update rebuilds the affected images without a local build host.
- **C:** Correct. ACR Tasks builds images in Azure on a commit or schedule without a local Docker host. It removes build-host drift but not image review. In this case: An ACR Task triggered by a base image update rebuilds the affected images without a local build host.
- **D:** Incorrect for this question. ACR keeps tagged, versioned images next to the deployment target and supports identity-based pulls. Tagging strategy and retention still need a decision. Why the correct answer wins: An ACR Task triggered by a base image update rebuilds the affected images without a local build host.

### Question 3 — A

Answer: Deploy the image to Azure App Service as a web app. App Service runs the container with managed maintenance and slot support. App Service runs a container with managed patching, deployment slots, and built-in authentication options. It is not a Kubernetes control plane. Local study-map skill 1.3 (Container Deployment to Azure App Service), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure container hosting documentation: https://learn.microsoft.com/en-us/azure/container-apps/

- **A:** Correct. App Service runs a container with managed patching, deployment slots, and built-in authentication options. It is not a Kubernetes control plane. In this case: App Service runs the container with managed maintenance and slot support.
- **B:** Incorrect for this question. AKS gives full Kubernetes control, including custom controllers and networking. You own node pools, upgrades, and manifest hygiene. Why the correct answer wins: App Service runs the container with managed maintenance and slot support.
- **C:** Incorrect for this question. Container Apps provides a managed environment, revisions, and KEDA-based scaling without cluster administration. Platform limits differ from AKS. Why the correct answer wins: App Service runs the container with managed maintenance and slot support.
- **D:** Incorrect for this question. Container Instances starts a single container group quickly for short tasks. It has no orchestrator-level scaling or revision model. Why the correct answer wins: App Service runs the container with managed maintenance and slot support.

### Question 4 — D

Answer: Reference a Key Vault secret from the app configuration instead of storing it. A Key Vault reference resolves the value at runtime through the app identity. A Key Vault reference resolves at runtime so the secret is never written into application settings. The app identity still needs permission to read it. Local study-map skill 1.3 (Container Deployment to Azure App Service), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure container hosting documentation: https://learn.microsoft.com/en-us/azure/container-apps/

- **A:** Incorrect for this question. App Service runs a container with managed patching, deployment slots, and built-in authentication options. It is not a Kubernetes control plane. Why the correct answer wins: A Key Vault reference resolves the value at runtime through the app identity.
- **B:** Incorrect for this question. A slot swap warms the new version before it takes production traffic and makes rollback a second swap. Slot-local settings must be marked sticky. Why the correct answer wins: A Key Vault reference resolves the value at runtime through the app identity.
- **C:** Incorrect for this question. Application settings become environment variables for the container and can be swapped per slot. Sensitive values should still reference a vault. Why the correct answer wins: A Key Vault reference resolves the value at runtime through the app identity.
- **D:** Correct. A Key Vault reference resolves at runtime so the secret is never written into application settings. The app identity still needs permission to read it. In this case: A Key Vault reference resolves the value at runtime through the app identity.

### Question 5 — B

Answer: Deploy into a Container Apps environment attached to the workload virtual network. An environment attached to the workload network supports private dependencies and internal ingress. A virtual-network-attached environment enables private access to dependencies and internal ingress. It also shifts DNS and egress design to you. Local study-map skill 1.4 (Container Apps Deployment and Revisions), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure container hosting documentation: https://learn.microsoft.com/en-us/azure/container-apps/

- **A:** Incorrect for this question. Internal ingress keeps the endpoint inside the environment virtual network. It is an exposure control, not an authorization control. Why the correct answer wins: An environment attached to the workload network supports private dependencies and internal ingress.
- **B:** Correct. A virtual-network-attached environment enables private access to dependencies and internal ingress. It also shifts DNS and egress design to you. In this case: An environment attached to the workload network supports private dependencies and internal ingress.
- **C:** Incorrect for this question. Revision-based traffic splitting enables canary and blue-green releases. Revision mode and scale rules must be set deliberately. Why the correct answer wins: An environment attached to the workload network supports private dependencies and internal ingress.
- **D:** Incorrect for this question. KEDA scalers drive replica count from queue length, lag, or other event metrics, including scale to zero. Cool-down and max replicas bound the behavior. Why the correct answer wins: An environment attached to the workload network supports private dependencies and internal ingress.

### Question 6 — D

Answer: Give the KEDA scaler a managed identity to read the event source. A scaler managed identity removes the stored connection string while still reading queue metrics. A scaler needs permission to read queue metrics; identity-based access avoids a stored connection string. Least privilege still applies to that identity. Local study-map skill 1.5 (Event-Driven Scaling with KEDA), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure container hosting documentation: https://learn.microsoft.com/en-us/azure/container-apps/

- **A:** Incorrect for this question. A queue-length scaler adds replicas while work is backed up and removes them when the queue drains. Message lock duration must exceed processing time. Why the correct answer wins: A scaler managed identity removes the stored connection string while still reading queue metrics.
- **B:** Incorrect for this question. Cool-down prevents replica flapping, and a maximum replica cap bounds cost and downstream load. Both are per-rule settings. Why the correct answer wins: A scaler managed identity removes the stored connection string while still reading queue metrics.
- **C:** Incorrect for this question. KEDA scalers drive replica count from queue length, lag, or other event metrics, including scale to zero. Cool-down and max replicas bound the behavior. Why the correct answer wins: A scaler managed identity removes the stored connection string while still reading queue metrics.
- **D:** Correct. A scaler needs permission to read queue metrics; identity-based access avoids a stored connection string. Least privilege still applies to that identity. In this case: A scaler managed identity removes the stored connection string while still reading queue metrics.

### Question 7 — C

Answer: Federate a Kubernetes service account to a managed identity. Service account federation gives the pod a token from a managed identity. Workload identity lets pods obtain tokens without stored secrets. Each workload should get its own identity and narrow role. Local study-map skill 1.6 (AKS Deployment with Manifests), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure container hosting documentation: https://learn.microsoft.com/en-us/azure/container-apps/

- **A:** Incorrect for this question. A vault centralizes secret storage with access control and audit. Retrieval should use an identity, not a copied credential. Why the correct answer wins: Service account federation gives the pod a token from a managed identity.
- **B:** Incorrect for this question. Readiness gates traffic until the app can serve it, and liveness restarts a wedged container. Wrong thresholds cause restart loops. Why the correct answer wins: Service account federation gives the pod a token from a managed identity.
- **C:** Correct. Workload identity lets pods obtain tokens without stored secrets. Each workload should get its own identity and narrow role. In this case: Service account federation gives the pod a token from a managed identity.
- **D:** Incorrect for this question. A managed identity issues tokens from the platform, removing secret distribution from the app. Role assignment still scopes what it can reach. Why the correct answer wins: Service account federation gives the pod a token from a managed identity.

### Question 8 — B, E

Answers: Build and store versioned images in Azure Container Registry; Apply an ACR retention policy to prune old untagged manifests. Versioned tags identify each artifact, and a retention policy prunes superseded manifests. ACR keeps tagged, versioned images next to the deployment target and supports identity-based pulls. Tagging strategy and retention still need a decision. A retention policy controls storage growth and registry clutter. It does not change which image tag a deployment references. Local study-map skill 1.1 (Container Image Lifecycle in Azure Container Registry), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure container hosting documentation: https://learn.microsoft.com/en-us/azure/container-apps/

- **A:** Incorrect for this question. A floating tag removes the link between a deployed revision and a specific build, so rollback and audit become guesswork. Why the correct answer wins: Versioned tags identify each artifact, and a retention policy prunes superseded manifests.
- **B:** Correct. A retention policy controls storage growth and registry clutter. It does not change which image tag a deployment references. In this case: Versioned tags identify each artifact, and a retention policy prunes superseded manifests.
- **C:** Incorrect for this question. A slot swap warms the new version before it takes production traffic and makes rollback a second swap. Slot-local settings must be marked sticky. Why the correct answer wins: Versioned tags identify each artifact, and a retention policy prunes superseded manifests.
- **D:** Incorrect for this question. Geo-replication reduces cross-region pull latency and gives a local copy during a regional failure. It adds cost and replication management. Why the correct answer wins: Versioned tags identify each artifact, and a retention policy prunes superseded manifests.
- **E:** Correct. ACR keeps tagged, versioned images next to the deployment target and supports identity-based pulls. Tagging strategy and retention still need a decision. In this case: Versioned tags identify each artifact, and a retention policy prunes superseded manifests.

### Question 9 — D

Answer: Build and store versioned images in Azure Container Registry. Versioned tags make the deployed artifact identifiable, which is the prerequisite for any review or rollback. ACR keeps tagged, versioned images next to the deployment target and supports identity-based pulls. Tagging strategy and retention still need a decision. Local study-map skill 1.1 (Container Image Lifecycle in Azure Container Registry), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure container hosting documentation: https://learn.microsoft.com/en-us/azure/container-apps/

- **A:** Incorrect for this question. ACR Tasks builds images in Azure on a commit or schedule without a local Docker host. It removes build-host drift but not image review. Why the correct answer wins: Versioned tags make the deployed artifact identifiable, which is the prerequisite for any review or rollback.
- **B:** Incorrect for this question. A floating tag removes the link between a deployed revision and a specific build, so rollback and audit become guesswork. Why the correct answer wins: Versioned tags make the deployed artifact identifiable, which is the prerequisite for any review or rollback.
- **C:** Incorrect for this question. Geo-replication reduces cross-region pull latency and gives a local copy during a regional failure. It adds cost and replication management. Why the correct answer wins: Versioned tags make the deployed artifact identifiable, which is the prerequisite for any review or rollback.
- **D:** Correct. ACR keeps tagged, versioned images next to the deployment target and supports identity-based pulls. Tagging strategy and retention still need a decision. In this case: Versioned tags make the deployed artifact identifiable, which is the prerequisite for any review or rollback.

### Question 10 — B, E

Answers: Create a new Container Apps revision and shift traffic between revisions; Set a minimum replica count above zero for the container app. Revisions allow traffic splitting between versions, and a minimum replica count avoids cold starts. Revision-based traffic splitting enables canary and blue-green releases. Revision mode and scale rules must be set deliberately. A warm minimum replica removes scale-to-zero cold starts for latency-critical endpoints. It keeps paying for idle capacity. Local study-map skill 1.4 (Container Apps Deployment and Revisions), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure container hosting documentation: https://learn.microsoft.com/en-us/azure/container-apps/

- **A:** Incorrect for this question. KEDA scalers drive replica count from queue length, lag, or other event metrics, including scale to zero. Cool-down and max replicas bound the behavior. Why the correct answer wins: Revisions allow traffic splitting between versions, and a minimum replica count avoids cold starts.
- **B:** Correct. A warm minimum replica removes scale-to-zero cold starts for latency-critical endpoints. It keeps paying for idle capacity. In this case: Revisions allow traffic splitting between versions, and a minimum replica count avoids cold starts.
- **C:** Incorrect for this question. HPA adjusts replicas from resource metrics but needs metrics-server and enough node capacity. It cannot scale to zero. Why the correct answer wins: Revisions allow traffic splitting between versions, and a minimum replica count avoids cold starts.
- **D:** Incorrect for this question. Container Instances starts a single container group quickly for short tasks. It has no orchestrator-level scaling or revision model. Why the correct answer wins: Revisions allow traffic splitting between versions, and a minimum replica count avoids cold starts.
- **E:** Correct. Revision-based traffic splitting enables canary and blue-green releases. Revision mode and scale rules must be set deliberately. In this case: Revisions allow traffic splitting between versions, and a minimum replica count avoids cold starts.

### Question 11 — D

Answer: Build and push the image → deploy a new revision → shift a small traffic percentage → check metrics → promote or roll back. The artifact is built, the revision deployed, partial traffic shifted, and metrics decide promotion. A canary revision accepts a small share of traffic so metrics decide promotion rather than optimism. Local study-map skill 1.4 (Container Apps Deployment and Revisions), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure container hosting documentation: https://learn.microsoft.com/en-us/azure/container-apps/

- **A:** Incorrect for this question. Metrics cannot be checked before the revision serves traffic. Why the correct answer wins: The artifact is built, the revision deployed, partial traffic shifted, and metrics decide promotion.
- **B:** Incorrect for this question. Full traffic cannot move to a revision that does not exist yet, and the image must exist before the revision. Why the correct answer wins: The artifact is built, the revision deployed, partial traffic shifted, and metrics decide promotion.
- **C:** Incorrect for this question. Building after traffic is shifted means the running revision has no reviewed artifact behind it. Why the correct answer wins: The artifact is built, the revision deployed, partial traffic shifted, and metrics decide promotion.
- **D:** Correct. A canary revision accepts a small share of traffic so metrics decide promotion rather than optimism. In this case: The artifact is built, the revision deployed, partial traffic shifted, and metrics decide promotion.

### Question 12 — C

Answer: Store the documents in Azure Cosmos DB for NoSQL. Including the partition key in the predicate turns the read into a single-partition query. Cosmos DB gives globally distributed, low-latency document access with tunable consistency. Partition key and RU planning determine the cost profile. Local study-map skill 2.1 (Cosmos DB SDK Access and Queries), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Cosmos DB and PostgreSQL vector documentation: https://learn.microsoft.com/en-us/azure/cosmos-db/

- **A:** Incorrect for this question. A point or single-partition query avoids fan-out across partitions. Cross-partition queries consume more RUs and add latency. Why the correct answer wins: Including the partition key in the predicate turns the read into a single-partition query.
- **B:** Incorrect for this question. Request units measure the work a query performs, so tuning the query is often cheaper than adding throughput. Monitor normalized RU consumption. Why the correct answer wins: Including the partition key in the predicate turns the read into a single-partition query.
- **C:** Correct. Cosmos DB gives globally distributed, low-latency document access with tunable consistency. Partition key and RU planning determine the cost profile. In this case: Including the partition key in the predicate turns the read into a single-partition query.
- **D:** Incorrect for this question. SDK queries keep the client on the supported data plane and parameterization avoids injection and plan churn. Cross-partition queries still cost more. Why the correct answer wins: Including the partition key in the predicate turns the read into a single-partition query.

### Question 13 — A

Answer: Restrict the indexing policy to the paths the queries use. Restricting indexed paths lowers write cost and storage. Selective indexing cuts write RU charge and storage for unused paths. Excluded paths cannot be filtered efficiently later. Local study-map skill 2.2 (Cosmos DB Indexing Policies and Request Units), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Cosmos DB and PostgreSQL vector documentation: https://learn.microsoft.com/en-us/azure/cosmos-db/

- **A:** Correct. Selective indexing cuts write RU charge and storage for unused paths. Excluded paths cannot be filtered efficiently later. In this case: Restricting indexed paths lowers write cost and storage.
- **B:** Incorrect for this question. Indexing everything is simple and makes ad hoc queries possible, at higher write cost and storage. It is a default, not an optimization. Why the correct answer wins: Restricting indexed paths lowers write cost and storage.
- **C:** Incorrect for this question. Autoscale follows demand between a minimum and maximum, avoiding throttling at peak without paying for peak all day. The maximum still caps the bill. Why the correct answer wins: Restricting indexed paths lowers write cost and storage.
- **D:** Incorrect for this question. Item TTL expires documents automatically, which controls storage growth and data retention. It does not archive the expired content. Why the correct answer wins: Restricting indexed paths lowers write cost and storage.

### Question 14 — C

Answer: Use session consistency for reads within the same client session. Session consistency guarantees read-your-writes within the session. Session consistency guarantees monotonic reads for one session and is the common default for user-facing apps. It does not promise global freshness. Local study-map skill 2.3 (Cosmos DB Consistency Levels), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Cosmos DB and PostgreSQL vector documentation: https://learn.microsoft.com/en-us/azure/cosmos-db/

- **A:** Incorrect for this question. Consistency trades freshness against latency, availability, and RU cost. The level is set at the account and can be relaxed per request. Why the correct answer wins: Session consistency guarantees read-your-writes within the session.
- **B:** Incorrect for this question. Strong consistency guarantees the latest committed write globally at the cost of higher latency and reduced availability during partitions. Why the correct answer wins: Session consistency guarantees read-your-writes within the session.
- **C:** Correct. Session consistency guarantees monotonic reads for one session and is the common default for user-facing apps. It does not promise global freshness. In this case: Session consistency guarantees read-your-writes within the session.
- **D:** Incorrect for this question. Eventual consistency is the cheapest and most available option but returns possibly stale data. It fits non-critical counters, not balances. Why the correct answer wins: Session consistency guarantees read-your-writes within the session.

### Question 15 — D

Answer: Declare the embedding dimensions and vector index type on the container policy. The container vector policy fixes dimensions, so it must be recreated to match the new model. The container vector policy fixes dimensions, distance function, and index type, so a model change requires a new policy. Mismatched dimensions fail at write time. Local study-map skill 2.4 (Cosmos DB Vector Search and Embeddings), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Cosmos DB and PostgreSQL vector documentation: https://learn.microsoft.com/en-us/azure/cosmos-db/

- **A:** Incorrect for this question. Cosmos DB for NoSQL supports vector properties and a distance function for similarity search in the same document store. Dimensions and index type must match the model. Why the correct answer wins: The container vector policy fixes dimensions, so it must be recreated to match the new model.
- **B:** Incorrect for this question. Application-side scoring works for tiny collections and tests, but it moves all data over the wire and does not scale with corpus size. Why the correct answer wins: The container vector policy fixes dimensions, so it must be recreated to match the new model.
- **C:** Incorrect for this question. DiskANN trades some recall for memory efficiency on large sets. Recall and latency should be measured on representative queries. Why the correct answer wins: The container vector policy fixes dimensions, so it must be recreated to match the new model.
- **D:** Correct. The container vector policy fixes dimensions, distance function, and index type, so a model change requires a new policy. Mismatched dimensions fail at write time. In this case: The container vector policy fixes dimensions, so it must be recreated to match the new model.

### Question 16 — C

Answer: Run a change feed processor to react to new and updated items. The change feed streams new items to a downstream scorer. The change feed delivers an ordered stream of changes per partition for downstream processing. It is not a delete feed, so deletions need a workaround. Local study-map skill 2.5 (Cosmos DB Change Feed Processing), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Cosmos DB and PostgreSQL vector documentation: https://learn.microsoft.com/en-us/azure/cosmos-db/

- **A:** Incorrect for this question. Leases track partition ownership so multiple processor instances share work and resume from a continuation token. Lease writes consume RUs too. Why the correct answer wins: The change feed streams new items to a downstream scorer.
- **B:** Incorrect for this question. Item TTL expires documents automatically, which controls storage growth and data retention. It does not archive the expired content. Why the correct answer wins: The change feed streams new items to a downstream scorer.
- **C:** Correct. The change feed delivers an ordered stream of changes per partition for downstream processing. It is not a delete feed, so deletions need a workaround. In this case: The change feed streams new items to a downstream scorer.
- **D:** Incorrect for this question. A transactional batch applies all-or-nothing within a single partition key. It cannot span partitions and still consumes RU per operation. Why the correct answer wins: The change feed streams new items to a downstream scorer.

### Question 17 — C

Answer: Batch related writes in a transactional batch within one partition key. A transactional batch applies all-or-nothing within one partition key. A transactional batch applies all-or-nothing within a single partition key. It cannot span partitions and still consumes RU per operation. Local study-map skill 2.5 (Cosmos DB Change Feed Processing), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Cosmos DB and PostgreSQL vector documentation: https://learn.microsoft.com/en-us/azure/cosmos-db/

- **A:** Incorrect for this question. Item TTL expires documents automatically, which controls storage growth and data retention. It does not archive the expired content. Why the correct answer wins: A transactional batch applies all-or-nothing within one partition key.
- **B:** Incorrect for this question. Request units measure the work a query performs, so tuning the query is often cheaper than adding throughput. Monitor normalized RU consumption. Why the correct answer wins: A transactional batch applies all-or-nothing within one partition key.
- **C:** Correct. A transactional batch applies all-or-nothing within a single partition key. It cannot span partitions and still consumes RU per operation. In this case: A transactional batch applies all-or-nothing within one partition key.
- **D:** Incorrect for this question. The change feed delivers an ordered stream of changes per partition for downstream processing. It is not a delete feed, so deletions need a workaround. Why the correct answer wins: A transactional batch applies all-or-nothing within one partition key.

### Question 18 — D

Answer: Model typed columns for filters and one vector column for the embedding. Typed filter columns beside one vector column keep both parts of the query efficient. Explicit types keep filters fast and make the embedding contract clear. Storing vectors as text defeats index use. Local study-map skill 2.6 (PostgreSQL Connection and Schema Modeling), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Cosmos DB and PostgreSQL vector documentation: https://learn.microsoft.com/en-us/azure/cosmos-db/

- **A:** Incorrect for this question. pgvector keeps vectors beside relational data, so filters and joins run in one query. Index type and parameter tuning decide latency. Why the correct answer wins: Typed filter columns beside one vector column keep both parts of the query efficient.
- **B:** Incorrect for this question. A replica offloads read traffic but introduces replication lag, which is dangerous for freshly written evidence. It does not reduce index memory pressure. Why the correct answer wins: Typed filter columns beside one vector column keep both parts of the query efficient.
- **C:** Incorrect for this question. Vector indexes are memory-hungry, so undersized compute causes swapping and slow queries. Right-size before tuning index parameters. Why the correct answer wins: Typed filter columns beside one vector column keep both parts of the query efficient.
- **D:** Correct. Explicit types keep filters fast and make the embedding contract clear. Storing vectors as text defeats index use. In this case: Typed filter columns beside one vector column keep both parts of the query efficient.

### Question 19 — C

Answer: Inspect the plan with EXPLAIN ANALYZE before changing indexes. EXPLAIN ANALYZE shows whether the index is used and where the time is spent. The plan shows whether PostgreSQL uses the vector index and where the time goes. Adding indexes without reading the plan often misses the cause. Local study-map skill 2.7 (pgvector Indexing and Query Latency), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Cosmos DB and PostgreSQL vector documentation: https://learn.microsoft.com/en-us/azure/cosmos-db/

- **A:** Incorrect for this question. HNSW gives fast approximate nearest-neighbour queries with a larger memory footprint and slower builds. Recall is tunable at query time. Why the correct answer wins: EXPLAIN ANALYZE shows whether the index is used and where the time is spent.
- **B:** Incorrect for this question. IVFFlat uses clustering lists and needs periodic rebuilds as data grows, but costs less memory than HNSW. Probes trade recall for speed. Why the correct answer wins: EXPLAIN ANALYZE shows whether the index is used and where the time is spent.
- **C:** Correct. The plan shows whether PostgreSQL uses the vector index and where the time goes. Adding indexes without reading the plan often misses the cause. In this case: EXPLAIN ANALYZE shows whether the index is used and where the time is spent.
- **D:** Incorrect for this question. Index builds and large sorts spill to disk when work memory is too small, stretching maintenance windows and slowing queries. Why the correct answer wins: EXPLAIN ANALYZE shows whether the index is used and where the time is spent.

### Question 20 — B

Answer: Increase storage throughput for index builds and bulk loads. Index builds are I/O heavy, so storage throughput must support the build window. Index creation and bulk loads are I/O heavy, and throttled storage stretches maintenance windows. Storage limits are separate from compute. Local study-map skill 2.8 (PostgreSQL Compute, Memory, and Storage Sizing), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Cosmos DB and PostgreSQL vector documentation: https://learn.microsoft.com/en-us/azure/cosmos-db/

- **A:** Incorrect for this question. A bounded pool amortizes connection setup and protects the server from connection storms. Pool size must match server limits. Why the correct answer wins: Index builds are I/O heavy, so storage throughput must support the build window.
- **B:** Correct. Index creation and bulk loads are I/O heavy, and throttled storage stretches maintenance windows. Storage limits are separate from compute. In this case: Index builds are I/O heavy, so storage throughput must support the build window.
- **C:** Incorrect for this question. Index builds and large sorts spill to disk when work memory is too small, stretching maintenance windows and slowing queries. Why the correct answer wins: Index builds are I/O heavy, so storage throughput must support the build window.
- **D:** Incorrect for this question. Vector indexes are memory-hungry, so undersized compute causes swapping and slow queries. Right-size before tuning index parameters. Why the correct answer wins: Index builds are I/O heavy, so storage throughput must support the build window.

### Question 21 — D

Answer: Use prepared statements and batch round trips. Prepared statements reuse plans and reduce per-call overhead. Prepared statements avoid repeated planning and reduce chatty network calls. They pair well with pooling but can interact with pool modes. Local study-map skill 2.10 (PostgreSQL Connection Optimization), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Cosmos DB and PostgreSQL vector documentation: https://learn.microsoft.com/en-us/azure/cosmos-db/

- **A:** Incorrect for this question. An external pooler multiplexes server connections for serverless or highly concurrent clients. Session-level features may be unavailable in transaction mode. Why the correct answer wins: Prepared statements reuse plans and reduce per-call overhead.
- **B:** Incorrect for this question. A replica offloads read traffic but introduces replication lag, which is dangerous for freshly written evidence. It does not reduce index memory pressure. Why the correct answer wins: Prepared statements reuse plans and reduce per-call overhead.
- **C:** Incorrect for this question. A bounded pool amortizes connection setup and protects the server from connection storms. Pool size must match server limits. Why the correct answer wins: Prepared statements reuse plans and reduce per-call overhead.
- **D:** Correct. Prepared statements avoid repeated planning and reduce chatty network calls. They pair well with pooling but can interact with pool modes. In this case: Prepared statements reuse plans and reduce per-call overhead.

### Question 22 — B

Answer: Invalidate or overwrite the cache entry when the source changes. Explicit invalidation or overwrite on change removes the stale entry at the moment of the write. Write-through or explicit invalidation keeps cached answers consistent with the system of record. Without it, TTL is the only bound on staleness. Local study-map skill 2.11 (Azure Managed Redis Caching and Invalidation), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Cosmos DB and PostgreSQL vector documentation: https://learn.microsoft.com/en-us/azure/cosmos-db/

- **A:** Incorrect for this question. A TTL bounds staleness and reclaims memory without a manual sweep. Too long a TTL hides source changes; too short wastes the cache. Why the correct answer wins: Explicit invalidation or overwrite on change removes the stale entry at the moment of the write.
- **B:** Correct. Write-through or explicit invalidation keeps cached answers consistent with the system of record. Without it, TTL is the only bound on staleness. In this case: Explicit invalidation or overwrite on change removes the stale entry at the moment of the write.
- **C:** Incorrect for this question. Flushing removes all cached content at once, causing a stampede to the origin and a latency cliff. Targeted invalidation is safer. Why the correct answer wins: Explicit invalidation or overwrite on change removes the stale entry at the moment of the write.
- **D:** Incorrect for this question. Eviction protects memory but evicts unpredictably, so a hot key can vanish before its freshness bound is reached. It is not a substitute for TTL design. Why the correct answer wins: Explicit invalidation or overwrite on change removes the stale entry at the moment of the write.

### Question 23 — D

Answer: Create a vector index in Managed Redis for similarity search. A Redis vector index serves similarity from memory. Redis vector search serves low-latency similarity queries from memory. The corpus must fit the memory budget and be rebuilt on model change. Local study-map skill 2.12 (Azure Managed Redis Vector Indexing), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Cosmos DB and PostgreSQL vector documentation: https://learn.microsoft.com/en-us/azure/cosmos-db/

- **A:** Incorrect for this question. A cache absorbs repeated reads and cuts latency for hot data. Cache keys, TTLs, and invalidation must match the freshness requirement. Why the correct answer wins: A Redis vector index serves similarity from memory.
- **B:** Incorrect for this question. Session storage in Redis survives instance restarts and supports distributed instances. Sessions must be scoped and expiring. Why the correct answer wins: A Redis vector index serves similarity from memory.
- **C:** Incorrect for this question. A lock can serialize work across instances, but correctness under retries still needs idempotency keys in the data store. Locks expire and can be lost. Why the correct answer wins: A Redis vector index serves similarity from memory.
- **D:** Correct. Redis vector search serves low-latency similarity queries from memory. The corpus must fit the memory budget and be rebuilt on model change. In this case: A Redis vector index serves similarity from memory.

### Question 24 — A, C

Answers: Create an HNSW index for low-latency approximate search; Create an IVFFlat index to save memory on a large table. HNSW favors query speed with a larger memory footprint, while IVFFlat saves memory but needs rebuilds as data changes. HNSW gives fast approximate nearest-neighbour queries with a larger memory footprint and slower builds. Recall is tunable at query time. IVFFlat uses clustering lists and needs periodic rebuilds as data grows, but costs less memory than HNSW. Probes trade recall for speed. Local study-map skill 2.7 (pgvector Indexing and Query Latency), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Cosmos DB and PostgreSQL vector documentation: https://learn.microsoft.com/en-us/azure/cosmos-db/

- **A:** Correct. IVFFlat uses clustering lists and needs periodic rebuilds as data grows, but costs less memory than HNSW. Probes trade recall for speed. In this case: HNSW favors query speed with a larger memory footprint, while IVFFlat saves memory but needs rebuilds as data changes.
- **B:** Incorrect for this question. Index builds and large sorts spill to disk when work memory is too small, stretching maintenance windows and slowing queries. Why the correct answer wins: HNSW favors query speed with a larger memory footprint, while IVFFlat saves memory but needs rebuilds as data changes.
- **C:** Correct. HNSW gives fast approximate nearest-neighbour queries with a larger memory footprint and slower builds. Recall is tunable at query time. In this case: HNSW favors query speed with a larger memory footprint, while IVFFlat saves memory but needs rebuilds as data changes.
- **D:** Incorrect for this question. Index creation and bulk loads are I/O heavy, and throttled storage stretches maintenance windows. Storage limits are separate from compute. Why the correct answer wins: HNSW favors query speed with a larger memory footprint, while IVFFlat saves memory but needs rebuilds as data changes.
- **E:** Incorrect for this question. An exact scan is accurate but scales linearly and burns compute. It is a baseline for measuring recall, not a production strategy. Why the correct answer wins: HNSW favors query speed with a larger memory footprint, while IVFFlat saves memory but needs rebuilds as data changes.

### Question 25 — B

Answer: Create the container with a vector policy → upsert items with embeddings → query with VectorDistance → apply metadata filters. Policy and container precede writes; writes precede queries. The vector policy fixes dimensions and index type, so it must exist before vector writes and queries. Local study-map skill 2.5 (Cosmos DB Change Feed Processing), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Cosmos DB and PostgreSQL vector documentation: https://learn.microsoft.com/en-us/azure/cosmos-db/

- **A:** Incorrect for this question. Filtering and querying cannot precede the container and its vector data. Why the correct answer wins: Policy and container precede writes; writes precede queries.
- **B:** Correct. The vector policy fixes dimensions and index type, so it must exist before vector writes and queries. In this case: Policy and container precede writes; writes precede queries.
- **C:** Incorrect for this question. Items cannot be written before the container exists with a matching vector policy. Why the correct answer wins: Policy and container precede writes; writes precede queries.
- **D:** Incorrect for this question. A similarity query needs indexed vectors, which require the container and its policy first. Why the correct answer wins: Policy and container precede writes; writes precede queries.

### Question 26 — C

Answer: Use Service Bus sessions to keep related messages ordered. Sessions give ordered, exclusive processing per session ID. Sessions give ordered, exclusive processing per session ID across competing consumers. They require session-aware senders and receivers. Local study-map skill 3.1 (Service Bus Queues and Sessions), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure messaging and Functions documentation: https://learn.microsoft.com/en-us/azure/service-bus-messaging/

- **A:** Incorrect for this question. A queue decouples producers from a single consumer group and smooths bursts. Delivery semantics depend on receive mode and completion. Why the correct answer wins: Sessions give ordered, exclusive processing per session ID.
- **B:** Incorrect for this question. Topics fan out one message to independent subscribers, each with its own filter and dead-letter queue. Subscribers process at their own pace. Why the correct answer wins: Sessions give ordered, exclusive processing per session ID.
- **C:** Correct. Sessions give ordered, exclusive processing per session ID across competing consumers. They require session-aware senders and receivers. In this case: Sessions give ordered, exclusive processing per session ID.
- **D:** Incorrect for this question. Peek-lock keeps the message locked until the handler completes it, giving at-least-once processing with retry. Lock duration must exceed processing time. Why the correct answer wins: Sessions give ordered, exclusive processing per session ID.

### Question 27 — B

Answer: Publish to a Service Bus topic with multiple subscriptions. A topic with separate subscriptions fans the event out to independent consumers. Topics fan out one message to independent subscribers, each with its own filter and dead-letter queue. Subscribers process at their own pace. Local study-map skill 3.2 (Service Bus Topics, Subscriptions, and Filters), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure messaging and Functions documentation: https://learn.microsoft.com/en-us/azure/service-bus-messaging/

- **A:** Incorrect for this question. Queue Storage is simple and cheap for large backlogs with at-least-once delivery. It lacks topics, sessions, and scheduled messages. Why the correct answer wins: A topic with separate subscriptions fans the event out to independent consumers.
- **B:** Correct. Topics fan out one message to independent subscribers, each with its own filter and dead-letter queue. Subscribers process at their own pace. In this case: A topic with separate subscriptions fans the event out to independent consumers.
- **C:** Incorrect for this question. A custom schema fits domain events that are not resource lifecycle notifications. Consumers must version the schema contract. Why the correct answer wins: A topic with separate subscriptions fans the event out to independent consumers.
- **D:** Incorrect for this question. A queue decouples producers from a single consumer group and smooths bursts. Delivery semantics depend on receive mode and completion. Why the correct answer wins: A topic with separate subscriptions fans the event out to independent consumers.

### Question 28 — C

Answer: Enable duplicate detection on the queue. Duplicate detection drops repeated sends inside its time window. A duplicate-detection window drops repeated sends within the window, which helps with at-least-once producers. The window is time-bounded. Local study-map skill 3.3 (Service Bus Dead-Lettering and Retries), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure messaging and Functions documentation: https://learn.microsoft.com/en-us/azure/service-bus-messaging/

- **A:** Incorrect for this question. A delivery cap stops infinite retries of a failing message and moves it to the dead-letter queue. The cap must exceed legitimate transient retries. Why the correct answer wins: Duplicate detection drops repeated sends inside its time window.
- **B:** Incorrect for this question. Sessions give ordered, exclusive processing per session ID across competing consumers. They require session-aware senders and receivers. Why the correct answer wins: Duplicate detection drops repeated sends inside its time window.
- **C:** Correct. A duplicate-detection window drops repeated sends within the window, which helps with at-least-once producers. The window is time-bounded. In this case: Duplicate detection drops repeated sends inside its time window.
- **D:** Incorrect for this question. At-least-once delivery means duplicates will happen, so the write must tolerate replay. A stored key makes the retry safe. Why the correct answer wins: Duplicate detection drops repeated sends inside its time window.

### Question 29 — B

Answer: Deliver events by using a managed identity instead of a key. Identity-based delivery removes the stored key from the subscription. Identity-based delivery removes a shared key from the subscription. The receiver still validates the caller and payload. Local study-map skill 3.4 (Event Grid Filters, Custom Events, and Retries), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure messaging and Functions documentation: https://learn.microsoft.com/en-us/azure/service-bus-messaging/

- **A:** Incorrect for this question. Subject and event-type filters keep handlers focused and reduce cost. Filters are evaluated on event metadata, not payload body. Why the correct answer wins: Identity-based delivery removes the stored key from the subscription.
- **B:** Correct. Identity-based delivery removes a shared key from the subscription. The receiver still validates the caller and payload. In this case: Identity-based delivery removes the stored key from the subscription.
- **C:** Incorrect for this question. Event Grid retries failed deliveries with backoff and can store undeliverable events. Handlers must still be idempotent. Why the correct answer wins: Identity-based delivery removes the stored key from the subscription.
- **D:** Incorrect for this question. System topics carry Azure resource lifecycle events. Domain events that are not resource changes need a custom topic and schema. Why the correct answer wins: Identity-based delivery removes the stored key from the subscription.

### Question 30 — C

Answer: Orchestrate the multi-step workflow with Durable Functions. Durable Functions checkpoint state and support long timers across restarts. Durable Functions provides orchestrations, activities, timers, and retries with checkpointed state. Orchestrator code must stay deterministic. Local study-map skill 3.5 (Azure Functions Triggers and Bindings), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure messaging and Functions documentation: https://learn.microsoft.com/en-us/azure/service-bus-messaging/

- **A:** Incorrect for this question. HTTP requests have platform timeout limits, so long work belongs behind a queue or orchestration with a status endpoint. Why the correct answer wins: Durable Functions checkpoint state and support long timers across restarts.
- **B:** Incorrect for this question. An HTTP trigger gives a synchronous API endpoint with route and authorization configuration. Long-running work should hand off to a queue. Why the correct answer wins: Durable Functions checkpoint state and support long timers across restarts.
- **C:** Correct. Durable Functions provides orchestrations, activities, timers, and retries with checkpointed state. Orchestrator code must stay deterministic. In this case: Durable Functions checkpoint state and support long timers across restarts.
- **D:** Incorrect for this question. A trigger starts the function when work arrives and handles the receive loop for you. Poison-message behavior is configured in host settings. Why the correct answer wins: Durable Functions checkpoint state and support long timers across restarts.

### Question 31 — B

Answer: Move long-running work out of the HTTP request into a queue. Long work moves behind a queue or orchestration with a status endpoint. HTTP requests have platform timeout limits, so long work belongs behind a queue or orchestration with a status endpoint. Local study-map skill 3.6 (Function App Configuration and Deployment), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure messaging and Functions documentation: https://learn.microsoft.com/en-us/azure/service-bus-messaging/

- **A:** Incorrect for this question. Consumption bills per execution and scales automatically, with cold starts and a timeout ceiling. It fits spiky, short work. Why the correct answer wins: Long work moves behind a queue or orchestration with a status endpoint.
- **B:** Correct. HTTP requests have platform timeout limits, so long work belongs behind a queue or orchestration with a status endpoint. In this case: Long work moves behind a queue or orchestration with a status endpoint.
- **C:** Incorrect for this question. An HTTP trigger gives a synchronous API endpoint with route and authorization configuration. Long-running work should hand off to a queue. Why the correct answer wins: Long work moves behind a queue or orchestration with a status endpoint.
- **D:** Incorrect for this question. A premium plan reduces cold starts and supports virtual network integration and longer timeouts. It costs more than consumption. Why the correct answer wins: Long work moves behind a queue or orchestration with a status endpoint.

### Question 32 — B, D

Answers: Add a SQL or correlation filter to a subscription; Schedule the message for future enqueueing. A subscription filter limits delivery to high-value messages, and a scheduled message enqueues for a later time. Subscription filters route only matching messages to a handler, reducing wasted processing. Filter evaluation happens broker-side on message properties. A scheduled message becomes visible at a set time, which supports reminders and delayed retries. It is not a substitute for a durable timer. Local study-map skill 3.2 (Service Bus Topics, Subscriptions, and Filters), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure messaging and Functions documentation: https://learn.microsoft.com/en-us/azure/service-bus-messaging/

- **A:** Incorrect for this question. Sessions give ordered, exclusive processing per session ID across competing consumers. They require session-aware senders and receivers. Why the correct answer wins: A subscription filter limits delivery to high-value messages, and a scheduled message enqueues for a later time.
- **B:** Correct. A scheduled message becomes visible at a set time, which supports reminders and delayed retries. It is not a substitute for a durable timer. In this case: A subscription filter limits delivery to high-value messages, and a scheduled message enqueues for a later time.
- **C:** Incorrect for this question. A duplicate-detection window drops repeated sends within the window, which helps with at-least-once producers. The window is time-bounded. Why the correct answer wins: A subscription filter limits delivery to high-value messages, and a scheduled message enqueues for a later time.
- **D:** Correct. Subscription filters route only matching messages to a handler, reducing wasted processing. Filter evaluation happens broker-side on message properties. In this case: A subscription filter limits delivery to high-value messages, and a scheduled message enqueues for a later time.
- **E:** Incorrect for this question. Dead-lettering preserves poison messages for diagnosis instead of losing them. Resubmission needs a fix and an idempotent handler. Why the correct answer wins: A subscription filter limits delivery to high-value messages, and a scheduled message enqueues for a later time.

### Question 33 — C, D

Answers: Inspect the dead-letter queue and resubmit corrected messages; Set a maximum delivery count and handle the dead-letter path. Dead-lettering preserves the message, and a delivery cap stops the loop. Dead-lettering preserves poison messages for diagnosis instead of losing them. Resubmission needs a fix and an idempotent handler. A delivery cap stops infinite retries of a failing message and moves it to the dead-letter queue. The cap must exceed legitimate transient retries. Local study-map skill 3.3 (Service Bus Dead-Lettering and Retries), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure messaging and Functions documentation: https://learn.microsoft.com/en-us/azure/service-bus-messaging/

- **A:** Incorrect for this question. A duplicate-detection window drops repeated sends within the window, which helps with at-least-once producers. The window is time-bounded. Why the correct answer wins: Dead-lettering preserves the message, and a delivery cap stops the loop.
- **B:** Incorrect for this question. Receive-and-delete removes the message on delivery, so a crash loses work silently. It suits telemetry, not payments. Why the correct answer wins: Dead-lettering preserves the message, and a delivery cap stops the loop.
- **C:** Correct. Dead-lettering preserves poison messages for diagnosis instead of losing them. Resubmission needs a fix and an idempotent handler. In this case: Dead-lettering preserves the message, and a delivery cap stops the loop.
- **D:** Correct. A delivery cap stops infinite retries of a failing message and moves it to the dead-letter queue. The cap must exceed legitimate transient retries. In this case: Dead-lettering preserves the message, and a delivery cap stops the loop.
- **E:** Incorrect for this question. Sessions give ordered, exclusive processing per session ID across competing consumers. They require session-aware senders and receivers. Why the correct answer wins: Dead-lettering preserves the message, and a delivery cap stops the loop.

### Question 34 — A

Answer: Publish a custom event → evaluate the subscription filter → deliver to the handler → retry on failure → dead-letter undeliverable events. Publish, filter, deliver, retry, then dead-letter. Filtering happens before delivery, retries handle transient failures, and dead-lettering preserves what cannot be delivered. Local study-map skill 3.4 (Event Grid Filters, Custom Events, and Retries), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure messaging and Functions documentation: https://learn.microsoft.com/en-us/azure/service-bus-messaging/

- **A:** Correct. Filtering happens before delivery, retries handle transient failures, and dead-lettering preserves what cannot be delivered. In this case: Publish, filter, deliver, retry, then dead-letter.
- **B:** Incorrect for this question. A filter cannot evaluate an event that has not been published. Why the correct answer wins: Publish, filter, deliver, retry, then dead-letter.
- **C:** Incorrect for this question. Delivery cannot precede publication and filtering. Why the correct answer wins: Publish, filter, deliver, retry, then dead-letter.
- **D:** Incorrect for this question. A filter is evaluated before delivery, and retries must occur before dead-lettering. Why the correct answer wins: Publish, filter, deliver, retry, then dead-letter.

### Question 35 — C

Answer: Store the secret in Azure Key Vault and read it at runtime. Key Vault provides audited, access-controlled storage. A vault centralizes secret storage with access control and audit. Retrieval should use an identity, not a copied credential. Local study-map skill 4.1 (Key Vault Secret Storage, Rotation, and Retrieval), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Key Vault, App Configuration, and Monitor documentation: https://learn.microsoft.com/en-us/azure/azure-monitor/

- **A:** Incorrect for this question. App Configuration separates configuration from code and supports labels, feature flags, and Key Vault references. Change still needs a refresh strategy. Why the correct answer wins: Key Vault provides audited, access-controlled storage.
- **B:** Incorrect for this question. Pinning a version makes a rotation invisible to the app until it is redeployed, which is useful for break-glass and dangerous for routine rotation. Why the correct answer wins: Key Vault provides audited, access-controlled storage.
- **C:** Correct. A vault centralizes secret storage with access control and audit. Retrieval should use an identity, not a copied credential. In this case: Key Vault provides audited, access-controlled storage.
- **D:** Incorrect for this question. Application settings become environment variables for the container and can be swapped per slot. Sensitive values should still reference a vault. Why the correct answer wins: Key Vault provides audited, access-controlled storage.

### Question 36 — C

Answer: Reference the Key Vault secret from an App Configuration key value. A Key Vault reference inside the configuration key keeps the secret out of the store. A Key Vault reference keeps non-secret settings in App Configuration while the value stays in the vault. The app identity needs both sets of permissions. Local study-map skill 4.2 (App Configuration Settings and Feature Flags), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Key Vault, App Configuration, and Monitor documentation: https://learn.microsoft.com/en-us/azure/azure-monitor/

- **A:** Incorrect for this question. Application settings become environment variables for the container and can be swapped per slot. Sensitive values should still reference a vault. Why the correct answer wins: A Key Vault reference inside the configuration key keeps the secret out of the store.
- **B:** Incorrect for this question. App Configuration separates configuration from code and supports labels, feature flags, and Key Vault references. Change still needs a refresh strategy. Why the correct answer wins: A Key Vault reference inside the configuration key keeps the secret out of the store.
- **C:** Correct. A Key Vault reference keeps non-secret settings in App Configuration while the value stays in the vault. The app identity needs both sets of permissions. In this case: A Key Vault reference inside the configuration key keeps the secret out of the store.
- **D:** Incorrect for this question. A vault centralizes secret storage with access control and audit. Retrieval should use an identity, not a copied credential. Why the correct answer wins: A Key Vault reference inside the configuration key keeps the secret out of the store.

### Question 37 — B

Answer: Use App Configuration labels to separate environments. Labels separate environment values under one key schema. Labels keep dev, test, and prod values in one store with one key schema. A misconfigured label selector silently serves the wrong values. Local study-map skill 4.2 (App Configuration Settings and Feature Flags), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Key Vault, App Configuration, and Monitor documentation: https://learn.microsoft.com/en-us/azure/azure-monitor/

- **A:** Incorrect for this question. Pinning a version makes a rotation invisible to the app until it is redeployed, which is useful for break-glass and dangerous for routine rotation. Why the correct answer wins: Labels separate environment values under one key schema.
- **B:** Correct. Labels keep dev, test, and prod values in one store with one key schema. A misconfigured label selector silently serves the wrong values. In this case: Labels separate environment values under one key schema.
- **C:** Incorrect for this question. App Configuration separates configuration from code and supports labels, feature flags, and Key Vault references. Change still needs a refresh strategy. Why the correct answer wins: Labels separate environment values under one key schema.
- **D:** Incorrect for this question. Sentinel-key or polling refresh lets a running app pick up new settings. Refresh intervals trade responsiveness against request volume. Why the correct answer wins: Labels separate environment values under one key schema.

### Question 38 — A

Answer: Use head or tail sampling so trace volume stays within budget. Tail sampling keeps error traces while reducing routine volume. Sampling keeps telemetry cost bounded, but aggressive sampling can hide rare failures. Tail sampling can retain errors preferentially. Local study-map skill 4.3 (Distributed Tracing with OpenTelemetry), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Key Vault, App Configuration, and Monitor documentation: https://learn.microsoft.com/en-us/azure/azure-monitor/

- **A:** Correct. Sampling keeps telemetry cost bounded, but aggressive sampling can hide rare failures. Tail sampling can retain errors preferentially. In this case: Tail sampling keeps error traces while reducing routine volume.
- **B:** Incorrect for this question. Propagation stitches one trace across HTTP, messaging, and Functions so the whole path is visible. Missing propagation breaks the trace at that hop. Why the correct answer wins: Tail sampling keeps error traces while reducing routine volume.
- **C:** Incorrect for this question. A collector batches, filters, and routes telemetry, and decouples app configuration from the backend. It is another component to run and monitor. Why the correct answer wins: Tail sampling keeps error traces while reducing routine volume.
- **D:** Incorrect for this question. OpenTelemetry emits vendor-neutral traces, metrics, and logs with context propagation. Exporters and sampling decide what reaches the backend. Why the correct answer wins: Tail sampling keeps error traces while reducing routine volume.

### Question 39 — A

Answer: Store repeated aggregations in a materialized view or update policy. Materializing the aggregation avoids recomputation on every refresh. Precomputed results avoid recomputing expensive aggregations on every dashboard refresh. The trade-off is storage and freshness lag. Local study-map skill 4.4 (KQL Queries for Logs and Metrics), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Key Vault, App Configuration, and Monitor documentation: https://learn.microsoft.com/en-us/azure/azure-monitor/

- **A:** Correct. Precomputed results avoid recomputing expensive aggregations on every dashboard refresh. The trade-off is storage and freshness lag. In this case: Materializing the aggregation avoids recomputation on every refresh.
- **B:** Incorrect for this question. Reducing columns and rows early lowers query cost and latency. Broad queries over long ranges are the usual cause of slow KQL. Why the correct answer wins: Materializing the aggregation avoids recomputation on every refresh.
- **C:** Incorrect for this question. Time-binned aggregation reveals the shape of an incident: a step change, a ramp, or a periodic spike. Averages alone hide short outages. Why the correct answer wins: Materializing the aggregation avoids recomputation on every refresh.
- **D:** Incorrect for this question. Joining request and dependency telemetry shows which downstream call fails inside a slow request. Cross-workspace joins need the right scope. Why the correct answer wins: Materializing the aggregation avoids recomputation on every refresh.

### Question 40 — A

Answer: Reach the data service through a private endpoint. A private endpoint with public access disabled keeps traffic inside the network. A private endpoint keeps traffic on the virtual network and removes public exposure. DNS resolution must be wired to the private zone. Local study-map skill 4.5 (Identity-Based Access for Application Services), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Key Vault, App Configuration, and Monitor documentation: https://learn.microsoft.com/en-us/azure/azure-monitor/

- **A:** Correct. A private endpoint keeps traffic on the virtual network and removes public exposure. DNS resolution must be wired to the private zone. In this case: A private endpoint with public access disabled keeps traffic inside the network.
- **B:** Incorrect for this question. A private endpoint needs matching name resolution or clients still resolve the public address. The zone must be linked to the workload network. Why the correct answer wins: A private endpoint with public access disabled keeps traffic inside the network.
- **C:** Incorrect for this question. A managed identity issues tokens from the platform, removing secret distribution from the app. Role assignment still scopes what it can reach. Why the correct answer wins: A private endpoint with public access disabled keeps traffic inside the network.
- **D:** Incorrect for this question. A scoped role grants only the operations the app performs and limits blast radius. Prefer built-in roles over broad contributor grants. Why the correct answer wins: A private endpoint with public access disabled keeps traffic inside the network.

### Question 41 — C, D

Answers: Federate a Kubernetes service account to a managed identity; Assign a least-privilege role to the application identity. Workload identity federation removes stored credentials, and a narrow role limits what the pod can do. Workload identity lets pods obtain tokens without stored secrets. Each workload should get its own identity and narrow role. A scoped role grants only the operations the app performs and limits blast radius. Prefer built-in roles over broad contributor grants. Local study-map skill 4.5 (Identity-Based Access for Application Services), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Key Vault, App Configuration, and Monitor documentation: https://learn.microsoft.com/en-us/azure/azure-monitor/

- **A:** Incorrect for this question. A private endpoint keeps traffic on the virtual network and removes public exposure. DNS resolution must be wired to the private zone. Why the correct answer wins: Workload identity federation removes stored credentials, and a narrow role limits what the pod can do.
- **B:** Incorrect for this question. A vault centralizes secret storage with access control and audit. Retrieval should use an identity, not a copied credential. Why the correct answer wins: Workload identity federation removes stored credentials, and a narrow role limits what the pod can do.
- **C:** Correct. A scoped role grants only the operations the app performs and limits blast radius. Prefer built-in roles over broad contributor grants. In this case: Workload identity federation removes stored credentials, and a narrow role limits what the pod can do.
- **D:** Correct. Workload identity lets pods obtain tokens without stored secrets. Each workload should get its own identity and narrow role. In this case: Workload identity federation removes stored credentials, and a narrow role limits what the pod can do.
- **E:** Incorrect for this question. Platform metrics are cheap and near-real-time, so they suit latency and failure-rate alerts. Log-based alerts add latency and query cost. Why the correct answer wins: Workload identity federation removes stored credentials, and a narrow role limits what the pod can do.

### Question 42 — A, B

Answers: Store the secret in Azure Key Vault and read it at runtime; Grant the app identity data-plane access to the vault. Store the secret in the vault, then grant the identity data-plane access. A vault centralizes secret storage with access control and audit. Retrieval should use an identity, not a copied credential. Vault access is a separate authorization decision from the app identity. Without a data-plane role or policy the reference fails at runtime. Local study-map skill 4.1 (Key Vault Secret Storage, Rotation, and Retrieval), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Key Vault, App Configuration, and Monitor documentation: https://learn.microsoft.com/en-us/azure/azure-monitor/

- **A:** Correct. A vault centralizes secret storage with access control and audit. Retrieval should use an identity, not a copied credential. In this case: Store the secret in the vault, then grant the identity data-plane access.
- **B:** Correct. Vault access is a separate authorization decision from the app identity. Without a data-plane role or policy the reference fails at runtime. In this case: Store the secret in the vault, then grant the identity data-plane access.
- **C:** Incorrect for this question. Pinning a version makes a rotation invisible to the app until it is redeployed, which is useful for break-glass and dangerous for routine rotation. Why the correct answer wins: Store the secret in the vault, then grant the identity data-plane access.
- **D:** Incorrect for this question. Labels keep dev, test, and prod values in one store with one key schema. A misconfigured label selector silently serves the wrong values. Why the correct answer wins: Store the secret in the vault, then grant the identity data-plane access.
- **E:** Incorrect for this question. App Configuration separates configuration from code and supports labels, feature flags, and Key Vault references. Change still needs a refresh strategy. Why the correct answer wins: Store the secret in the vault, then grant the identity data-plane access.

### Question 43 — D

Answer: Store the secret in Key Vault → grant the app identity access → reference the secret from the app → rotate the secret → the app reads the new version. Store, grant, reference, rotate, then read the current version. Access must be granted before the reference resolves, and the app must read the current version after rotation. Local study-map skill 4.3 (Distributed Tracing with OpenTelemetry), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Key Vault, App Configuration, and Monitor documentation: https://learn.microsoft.com/en-us/azure/azure-monitor/

- **A:** Incorrect for this question. A reference cannot resolve before the secret and the access grant exist. Why the correct answer wins: Store, grant, reference, rotate, then read the current version.
- **B:** Incorrect for this question. There is nothing to rotate or reference before the secret is stored. Why the correct answer wins: Store, grant, reference, rotate, then read the current version.
- **C:** Incorrect for this question. Access can be granted first, but rotation cannot precede storing the secret. Why the correct answer wins: Store, grant, reference, rotate, then read the current version.
- **D:** Correct. Access must be granted before the reference resolves, and the app must read the current version after rotation. In this case: Store, grant, reference, rotate, then read the current version.

### Question 44 — A, E

Answers: Use Service Bus sessions to keep related messages ordered; Receive with peek-lock and complete or abandon explicitly. Sessions keep per-card ordering, and peek-lock lets an uncompleted message return to the queue. Sessions give ordered, exclusive processing per session ID across competing consumers. They require session-aware senders and receivers. Peek-lock keeps the message locked until the handler completes it, giving at-least-once processing with retry. Lock duration must exceed processing time. Local study-map skill 3.1 (Service Bus Queues and Sessions), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure messaging and Functions documentation: https://learn.microsoft.com/en-us/azure/service-bus-messaging/

- **A:** Correct. Peek-lock keeps the message locked until the handler completes it, giving at-least-once processing with retry. Lock duration must exceed processing time. In this case: Sessions keep per-card ordering, and peek-lock lets an uncompleted message return to the queue.
- **B:** Incorrect for this question. Subscription filters route only matching messages to a handler, reducing wasted processing. Filter evaluation happens broker-side on message properties. Why the correct answer wins: Sessions keep per-card ordering, and peek-lock lets an uncompleted message return to the queue.
- **C:** Incorrect for this question. A duplicate-detection window drops repeated sends within the window, which helps with at-least-once producers. The window is time-bounded. Why the correct answer wins: Sessions keep per-card ordering, and peek-lock lets an uncompleted message return to the queue.
- **D:** Incorrect for this question. Receive-and-delete removes the message on delivery, so a crash loses work silently. It suits telemetry, not payments. Why the correct answer wins: Sessions keep per-card ordering, and peek-lock lets an uncompleted message return to the queue.
- **E:** Correct. Sessions give ordered, exclusive processing per session ID across competing consumers. They require session-aware senders and receivers. In this case: Sessions keep per-card ordering, and peek-lock lets an uncompleted message return to the queue.

### Question 45 — D

Answer: Build and store versioned images in Azure Container Registry. ACR stores tagged, versioned images next to the deployment target and supports identity-based pulls. ACR keeps tagged, versioned images next to the deployment target and supports identity-based pulls. Tagging strategy and retention still need a decision. Local study-map skill 1.1 (Container Image Lifecycle in Azure Container Registry), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure container hosting documentation: https://learn.microsoft.com/en-us/azure/container-apps/

- **A:** Incorrect for this question. App Service runs a container with managed patching, deployment slots, and built-in authentication options. It is not a Kubernetes control plane. Why the correct answer wins: ACR stores tagged, versioned images next to the deployment target and supports identity-based pulls.
- **B:** Incorrect for this question. A floating tag removes the link between a deployed revision and a specific build, so rollback and audit become guesswork. Why the correct answer wins: ACR stores tagged, versioned images next to the deployment target and supports identity-based pulls.
- **C:** Incorrect for this question. Container Instances starts a single container group quickly for short tasks. It has no orchestrator-level scaling or revision model. Why the correct answer wins: ACR stores tagged, versioned images next to the deployment target and supports identity-based pulls.
- **D:** Correct. ACR keeps tagged, versioned images next to the deployment target and supports identity-based pulls. Tagging strategy and retention still need a decision. In this case: ACR stores tagged, versioned images next to the deployment target and supports identity-based pulls.

### Question 46 — C

Answer: Run image builds on demand or on a trigger with ACR Tasks. ACR Tasks builds from the repository on a commit trigger, so no developer workstation or build agent is involved. ACR Tasks builds images in Azure on a commit or schedule without a local Docker host. It removes build-host drift but not image review. Local study-map skill 1.2 (Automated Image Builds with ACR Tasks), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure container hosting documentation: https://learn.microsoft.com/en-us/azure/container-apps/

- **A:** Incorrect for this question. Container Apps provides a managed environment, revisions, and KEDA-based scaling without cluster administration. Platform limits differ from AKS. Why the correct answer wins: ACR Tasks builds from the repository on a commit trigger, so no developer workstation or build agent is involved.
- **B:** Incorrect for this question. ACR keeps tagged, versioned images next to the deployment target and supports identity-based pulls. Tagging strategy and retention still need a decision. Why the correct answer wins: ACR Tasks builds from the repository on a commit trigger, so no developer workstation or build agent is involved.
- **C:** Correct. ACR Tasks builds images in Azure on a commit or schedule without a local Docker host. It removes build-host drift but not image review. In this case: ACR Tasks builds from the repository on a commit trigger, so no developer workstation or build agent is involved.
- **D:** Incorrect for this question. AKS gives full Kubernetes control, including custom controllers and networking. You own node pools, upgrades, and manifest hygiene. Why the correct answer wins: ACR Tasks builds from the repository on a commit trigger, so no developer workstation or build agent is involved.

### Question 47 — A

Answer: Supply configuration through App Service application settings. Application settings become environment variables per slot, so a threshold change does not require a new image. Application settings become environment variables for the container and can be swapped per slot. Sensitive values should still reference a vault. Local study-map skill 1.3 (Container Deployment to Azure App Service), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure container hosting documentation: https://learn.microsoft.com/en-us/azure/container-apps/

- **A:** Correct. Application settings become environment variables for the container and can be swapped per slot. Sensitive values should still reference a vault. In this case: Application settings become environment variables per slot, so a threshold change does not require a new image.
- **B:** Incorrect for this question. App Configuration separates configuration from code and supports labels, feature flags, and Key Vault references. Change still needs a refresh strategy. Why the correct answer wins: Application settings become environment variables per slot, so a threshold change does not require a new image.
- **C:** Incorrect for this question. Pinning a version makes a rotation invisible to the app until it is redeployed, which is useful for break-glass and dangerous for routine rotation. Why the correct answer wins: Application settings become environment variables per slot, so a threshold change does not require a new image.
- **D:** Incorrect for this question. A ConfigMap injects settings as environment variables or mounted files without rebuilding the image. Secrets still belong in Key Vault, not in a ConfigMap. Why the correct answer wins: Application settings become environment variables per slot, so a threshold change does not require a new image.

### Question 48 — A

Answer: Reference a Key Vault secret from the app configuration instead of storing it. A Key Vault reference resolves the secret through the app identity at runtime, so the value stays out of settings. A Key Vault reference resolves at runtime so the secret is never written into application settings. The app identity still needs permission to read it. Local study-map skill 1.3 (Container Deployment to Azure App Service), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure container hosting documentation: https://learn.microsoft.com/en-us/azure/container-apps/

- **A:** Correct. A Key Vault reference resolves at runtime so the secret is never written into application settings. The app identity still needs permission to read it. In this case: A Key Vault reference resolves the secret through the app identity at runtime, so the value stays out of settings.
- **B:** Incorrect for this question. Pinning a version makes a rotation invisible to the app until it is redeployed, which is useful for break-glass and dangerous for routine rotation. Why the correct answer wins: A Key Vault reference resolves the secret through the app identity at runtime, so the value stays out of settings.
- **C:** Incorrect for this question. Application settings become environment variables for the container and can be swapped per slot. Sensitive values should still reference a vault. Why the correct answer wins: A Key Vault reference resolves the secret through the app identity at runtime, so the value stays out of settings.
- **D:** Incorrect for this question. A ConfigMap injects settings as environment variables or mounted files without rebuilding the image. Secrets still belong in Key Vault, not in a ConfigMap. Why the correct answer wins: A Key Vault reference resolves the secret through the app identity at runtime, so the value stays out of settings.

### Question 49 — B

Answer: Configure Container Apps ingress for internal-only access. Internal ingress keeps the endpoint inside the environment network instead of publishing it to the internet. Internal ingress keeps the endpoint inside the environment virtual network. It is an exposure control, not an authorization control. Local study-map skill 1.4 (Container Apps Deployment and Revisions), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure container hosting documentation: https://learn.microsoft.com/en-us/azure/container-apps/

- **A:** Incorrect for this question. A slot swap warms the new version before it takes production traffic and makes rollback a second swap. Slot-local settings must be marked sticky. Why the correct answer wins: Internal ingress keeps the endpoint inside the environment network instead of publishing it to the internet.
- **B:** Correct. Internal ingress keeps the endpoint inside the environment virtual network. It is an exposure control, not an authorization control. In this case: Internal ingress keeps the endpoint inside the environment network instead of publishing it to the internet.
- **C:** Incorrect for this question. Revision-based traffic splitting enables canary and blue-green releases. Revision mode and scale rules must be set deliberately. Why the correct answer wins: Internal ingress keeps the endpoint inside the environment network instead of publishing it to the internet.
- **D:** Incorrect for this question. KEDA scalers drive replica count from queue length, lag, or other event metrics, including scale to zero. Cool-down and max replicas bound the behavior. Why the correct answer wins: Internal ingress keeps the endpoint inside the environment network instead of publishing it to the internet.

### Question 50 — B

Answer: Create a new Container Apps revision and shift traffic between revisions. Container Apps revisions support percentage traffic allocation, which gives a measured canary and a fast reversal. Revision-based traffic splitting enables canary and blue-green releases. Revision mode and scale rules must be set deliberately. Local study-map skill 1.4 (Container Apps Deployment and Revisions), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure container hosting documentation: https://learn.microsoft.com/en-us/azure/container-apps/

- **A:** Incorrect for this question. A slot swap warms the new version before it takes production traffic and makes rollback a second swap. Slot-local settings must be marked sticky. Why the correct answer wins: Container Apps revisions support percentage traffic allocation, which gives a measured canary and a fast reversal.
- **B:** Correct. Revision-based traffic splitting enables canary and blue-green releases. Revision mode and scale rules must be set deliberately. In this case: Container Apps revisions support percentage traffic allocation, which gives a measured canary and a fast reversal.
- **C:** Incorrect for this question. HPA adjusts replicas from resource metrics but needs metrics-server and enough node capacity. It cannot scale to zero. Why the correct answer wins: Container Apps revisions support percentage traffic allocation, which gives a measured canary and a fast reversal.
- **D:** Incorrect for this question. Geo-replication reduces cross-region pull latency and gives a local copy during a regional failure. It adds cost and replication management. Why the correct answer wins: Container Apps revisions support percentage traffic allocation, which gives a measured canary and a fast reversal.

### Question 51 — A

Answer: Rely on the horizontal pod autoscaler on CPU. The horizontal pod autoscaler changes replica count from observed CPU or memory utilisation against a declared target. HPA adjusts replicas from resource metrics but needs metrics-server and enough node capacity. It cannot scale to zero. Local study-map skill 1.6 (AKS Deployment with Manifests), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure container hosting documentation: https://learn.microsoft.com/en-us/azure/container-apps/

- **A:** Correct. HPA adjusts replicas from resource metrics but needs metrics-server and enough node capacity. It cannot scale to zero. In this case: The horizontal pod autoscaler changes replica count from observed CPU or memory utilisation against a declared target.
- **B:** Incorrect for this question. A manifest declares the desired deployment, service, and probe configuration in version control. Applying it repeatedly is idempotent. Why the correct answer wins: The horizontal pod autoscaler changes replica count from observed CPU or memory utilisation against a declared target.
- **C:** Incorrect for this question. Readiness gates traffic until the app can serve it, and liveness restarts a wedged container. Wrong thresholds cause restart loops. Why the correct answer wins: The horizontal pod autoscaler changes replica count from observed CPU or memory utilisation against a declared target.
- **D:** Incorrect for this question. Container Instances starts a single container group quickly for short tasks. It has no orchestrator-level scaling or revision model. Why the correct answer wins: The horizontal pod autoscaler changes replica count from observed CPU or memory utilisation against a declared target.

### Question 52 — D

Answer: Query container logs and Kubernetes events in Log Analytics. Container termination reasons and pod events are recorded in the workspace, where limits and restarts can be correlated. Container Apps and AKS surface stdout logs and platform events into a workspace for KQL analysis. Verbosity and retention cost money. Local study-map skill 1.7 (Container Logs, Events, and Connectivity), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure container hosting documentation: https://learn.microsoft.com/en-us/azure/container-apps/

- **A:** Incorrect for this question. Time-binned aggregation reveals the shape of an incident: a step change, a ramp, or a periodic spike. Averages alone hide short outages. Why the correct answer wins: Container termination reasons and pod events are recorded in the workspace, where limits and restarts can be correlated.
- **B:** Incorrect for this question. Readiness gates traffic until the app can serve it, and liveness restarts a wedged container. Wrong thresholds cause restart loops. Why the correct answer wins: Container termination reasons and pod events are recorded in the workspace, where limits and restarts can be correlated.
- **C:** Incorrect for this question. Platform logs and metrics must be routed before they can be queried or alerted on. Retention and cost follow the workspace settings. Why the correct answer wins: Container termination reasons and pod events are recorded in the workspace, where limits and restarts can be correlated.
- **D:** Correct. Container Apps and AKS surface stdout logs and platform events into a workspace for KQL analysis. Verbosity and retention cost money. In this case: Container termination reasons and pod events are recorded in the workspace, where limits and restarts can be correlated.

### Question 53 — A

Answer: Enable diagnostic settings to route platform logs to the workspace. Diagnostic settings forward platform logs and metrics to the workspace so they sit beside application telemetry. Platform logs and metrics must be routed before they can be queried or alerted on. Retention and cost follow the workspace settings. Local study-map skill 1.7 (Container Logs, Events, and Connectivity), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure container hosting documentation: https://learn.microsoft.com/en-us/azure/container-apps/

- **A:** Correct. Platform logs and metrics must be routed before they can be queried or alerted on. Retention and cost follow the workspace settings. In this case: Diagnostic settings forward platform logs and metrics to the workspace so they sit beside application telemetry.
- **B:** Incorrect for this question. Platform metrics are cheap and near-real-time, so they suit latency and failure-rate alerts. Log-based alerts add latency and query cost. Why the correct answer wins: Diagnostic settings forward platform logs and metrics to the workspace so they sit beside application telemetry.
- **C:** Incorrect for this question. Reducing columns and rows early lowers query cost and latency. Broad queries over long ranges are the usual cause of slow KQL. Why the correct answer wins: Diagnostic settings forward platform logs and metrics to the workspace so they sit beside application telemetry.
- **D:** Incorrect for this question. Container Apps and AKS surface stdout logs and platform events into a workspace for KQL analysis. Verbosity and retention cost money. Why the correct answer wins: Diagnostic settings forward platform logs and metrics to the workspace so they sit beside application telemetry.

### Question 54 — A, C

Answers: Build and store versioned images in Azure Container Registry; Replicate the registry to each deployment region. Versioned images in the registry tie a deployment to one build, and geo-replication keeps a local copy for each region. ACR keeps tagged, versioned images next to the deployment target and supports identity-based pulls. Tagging strategy and retention still need a decision. Geo-replication reduces cross-region pull latency and gives a local copy during a regional failure. It adds cost and replication management. Local study-map skill 1.1 (Container Image Lifecycle in Azure Container Registry), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure container hosting documentation: https://learn.microsoft.com/en-us/azure/container-apps/

- **A:** Correct. Geo-replication reduces cross-region pull latency and gives a local copy during a regional failure. It adds cost and replication management. In this case: Versioned images in the registry tie a deployment to one build, and geo-replication keeps a local copy for each region.
- **B:** Incorrect for this question. A floating tag removes the link between a deployed revision and a specific build, so rollback and audit become guesswork. Why the correct answer wins: Versioned images in the registry tie a deployment to one build, and geo-replication keeps a local copy for each region.
- **C:** Correct. ACR keeps tagged, versioned images next to the deployment target and supports identity-based pulls. Tagging strategy and retention still need a decision. In this case: Versioned images in the registry tie a deployment to one build, and geo-replication keeps a local copy for each region.
- **D:** Incorrect for this question. A retention policy controls storage growth and registry clutter. It does not change which image tag a deployment references. Why the correct answer wins: Versioned images in the registry tie a deployment to one build, and geo-replication keeps a local copy for each region.
- **E:** Incorrect for this question. A slot swap warms the new version before it takes production traffic and makes rollback a second swap. Slot-local settings must be marked sticky. Why the correct answer wins: Versioned images in the registry tie a deployment to one build, and geo-replication keeps a local copy for each region.

### Question 55 — C

Answer: Build the image → scan it → push a versioned tag to ACR → deploy that tag → verify health. Build precedes scan, scan precedes the versioned push, and deployment follows the tag with a health check after it. A build is scanned and versioned before deployment so the deployed artifact is the reviewed one and can be rolled back by tag. Local study-map skill 1.2 (Automated Image Builds with ACR Tasks), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure container hosting documentation: https://learn.microsoft.com/en-us/azure/container-apps/

- **A:** Incorrect for this question. Deploying an unversioned tag severs the link between what runs and what was built and scanned. Why the correct answer wins: Build precedes scan, scan precedes the versioned push, and deployment follows the tag with a health check after it.
- **B:** Incorrect for this question. The image cannot be pushed before it is built, and scanning after deployment leaves a window of unreviewed runtime. Why the correct answer wins: Build precedes scan, scan precedes the versioned push, and deployment follows the tag with a health check after it.
- **C:** Correct. A build is scanned and versioned before deployment so the deployed artifact is the reviewed one and can be rolled back by tag. In this case: Build precedes scan, scan precedes the versioned push, and deployment follows the tag with a health check after it.
- **D:** Incorrect for this question. Scanning requires a built image, and health verification cannot precede deployment. Why the correct answer wins: Build precedes scan, scan precedes the versioned push, and deployment follows the tag with a health check after it.

### Question 56 — C

Answer: Choose a high-cardinality partition key that spreads writes. A high-cardinality key such as the transaction identifier spreads writes and keeps point reads inside one partition. A good partition key distributes storage and throughput and keeps common queries single-partition. Low cardinality creates hot partitions. Local study-map skill 2.1 (Cosmos DB SDK Access and Queries), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Cosmos DB and PostgreSQL vector documentation: https://learn.microsoft.com/en-us/azure/cosmos-db/

- **A:** Incorrect for this question. Indexing everything is simple and makes ad hoc queries possible, at higher write cost and storage. It is a default, not an optimization. Why the correct answer wins: A high-cardinality key such as the transaction identifier spreads writes and keeps point reads inside one partition.
- **B:** Incorrect for this question. A point or single-partition query avoids fan-out across partitions. Cross-partition queries consume more RUs and add latency. Why the correct answer wins: A high-cardinality key such as the transaction identifier spreads writes and keeps point reads inside one partition.
- **C:** Correct. A good partition key distributes storage and throughput and keeps common queries single-partition. Low cardinality creates hot partitions. In this case: A high-cardinality key such as the transaction identifier spreads writes and keeps point reads inside one partition.
- **D:** Incorrect for this question. Request units measure the work a query performs, so tuning the query is often cheaper than adding throughput. Monitor normalized RU consumption. Why the correct answer wins: A high-cardinality key such as the transaction identifier spreads writes and keeps point reads inside one partition.

### Question 57 — A

Answer: Query through the Cosmos DB SDK with parameterized queries. Parameterized SDK queries stay on the supported data-plane path and avoid injection through string concatenation. SDK queries keep the client on the supported data plane and parameterization avoids injection and plan churn. Cross-partition queries still cost more. Local study-map skill 2.1 (Cosmos DB SDK Access and Queries), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Cosmos DB and PostgreSQL vector documentation: https://learn.microsoft.com/en-us/azure/cosmos-db/

- **A:** Correct. SDK queries keep the client on the supported data plane and parameterization avoids injection and plan churn. Cross-partition queries still cost more. In this case: Parameterized SDK queries stay on the supported data-plane path and avoid injection through string concatenation.
- **B:** Incorrect for this question. Application-side scoring works for tiny collections and tests, but it moves all data over the wire and does not scale with corpus size. Why the correct answer wins: Parameterized SDK queries stay on the supported data-plane path and avoid injection through string concatenation.
- **C:** Incorrect for this question. A point or single-partition query avoids fan-out across partitions. Cross-partition queries consume more RUs and add latency. Why the correct answer wins: Parameterized SDK queries stay on the supported data-plane path and avoid injection through string concatenation.
- **D:** Incorrect for this question. A duplicate-detection window drops repeated sends within the window, which helps with at-least-once producers. The window is time-bounded. Why the correct answer wins: Parameterized SDK queries stay on the supported data-plane path and avoid injection through string concatenation.

### Question 58 — A

Answer: Include the partition key in the query predicate. Including the partition key in the predicate turns the read into a single-partition operation instead of a fan-out. A point or single-partition query avoids fan-out across partitions. Cross-partition queries consume more RUs and add latency. Local study-map skill 2.2 (Cosmos DB Indexing Policies and Request Units), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Cosmos DB and PostgreSQL vector documentation: https://learn.microsoft.com/en-us/azure/cosmos-db/

- **A:** Correct. A point or single-partition query avoids fan-out across partitions. Cross-partition queries consume more RUs and add latency. In this case: Including the partition key in the predicate turns the read into a single-partition operation instead of a fan-out.
- **B:** Incorrect for this question. A good partition key distributes storage and throughput and keeps common queries single-partition. Low cardinality creates hot partitions. Why the correct answer wins: Including the partition key in the predicate turns the read into a single-partition operation instead of a fan-out.
- **C:** Incorrect for this question. Request units measure the work a query performs, so tuning the query is often cheaper than adding throughput. Monitor normalized RU consumption. Why the correct answer wins: Including the partition key in the predicate turns the read into a single-partition operation instead of a fan-out.
- **D:** Incorrect for this question. Selective indexing cuts write RU charge and storage for unused paths. Excluded paths cannot be filtered efficiently later. Why the correct answer wins: Including the partition key in the predicate turns the read into a single-partition operation instead of a fan-out.

### Question 59 — D

Answer: Batch related writes in a transactional batch within one partition key. A transactional batch within one partition key applies the writes atomically or not at all. A transactional batch applies all-or-nothing within a single partition key. It cannot span partitions and still consumes RU per operation. Local study-map skill 2.2 (Cosmos DB Indexing Policies and Request Units), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Cosmos DB and PostgreSQL vector documentation: https://learn.microsoft.com/en-us/azure/cosmos-db/

- **A:** Incorrect for this question. Autoscale follows demand between a minimum and maximum, avoiding throttling at peak without paying for peak all day. The maximum still caps the bill. Why the correct answer wins: A transactional batch within one partition key applies the writes atomically or not at all.
- **B:** Incorrect for this question. Indexing everything is simple and makes ad hoc queries possible, at higher write cost and storage. It is a default, not an optimization. Why the correct answer wins: A transactional batch within one partition key applies the writes atomically or not at all.
- **C:** Incorrect for this question. Request units measure the work a query performs, so tuning the query is often cheaper than adding throughput. Monitor normalized RU consumption. Why the correct answer wins: A transactional batch within one partition key applies the writes atomically or not at all.
- **D:** Correct. A transactional batch applies all-or-nothing within a single partition key. It cannot span partitions and still consumes RU per operation. In this case: A transactional batch within one partition key applies the writes atomically or not at all.

### Question 60 — B

Answer: Use session consistency for reads within the same client session. Session consistency guarantees monotonic reads for that client at a fraction of the cost of strong consistency. Session consistency guarantees monotonic reads for one session and is the common default for user-facing apps. It does not promise global freshness. Local study-map skill 2.3 (Cosmos DB Consistency Levels), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Cosmos DB and PostgreSQL vector documentation: https://learn.microsoft.com/en-us/azure/cosmos-db/

- **A:** Incorrect for this question. Consistency trades freshness against latency, availability, and RU cost. The level is set at the account and can be relaxed per request. Why the correct answer wins: Session consistency guarantees monotonic reads for that client at a fraction of the cost of strong consistency.
- **B:** Correct. Session consistency guarantees monotonic reads for one session and is the common default for user-facing apps. It does not promise global freshness. In this case: Session consistency guarantees monotonic reads for that client at a fraction of the cost of strong consistency.
- **C:** Incorrect for this question. Strong consistency guarantees the latest committed write globally at the cost of higher latency and reduced availability during partitions. Why the correct answer wins: Session consistency guarantees monotonic reads for that client at a fraction of the cost of strong consistency.
- **D:** Incorrect for this question. Eventual consistency is the cheapest and most available option but returns possibly stale data. It fits non-critical counters, not balances. Why the correct answer wins: Session consistency guarantees monotonic reads for that client at a fraction of the cost of strong consistency.

### Question 61 — B

Answer: Use the DiskANN vector index for large collections. DiskANN keeps the graph on local SSD with a memory-resident subset, which suits collections larger than memory. DiskANN trades some recall for memory efficiency on large sets. Recall and latency should be measured on representative queries. Local study-map skill 2.4 (Cosmos DB Vector Search and Embeddings), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Cosmos DB and PostgreSQL vector documentation: https://learn.microsoft.com/en-us/azure/cosmos-db/

- **A:** Incorrect for this question. Application-side scoring works for tiny collections and tests, but it moves all data over the wire and does not scale with corpus size. Why the correct answer wins: DiskANN keeps the graph on local SSD with a memory-resident subset, which suits collections larger than memory.
- **B:** Correct. DiskANN trades some recall for memory efficiency on large sets. Recall and latency should be measured on representative queries. In this case: DiskANN keeps the graph on local SSD with a memory-resident subset, which suits collections larger than memory.
- **C:** Incorrect for this question. pgvector keeps vectors beside relational data, so filters and joins run in one query. Index type and parameter tuning decide latency. Why the correct answer wins: DiskANN keeps the graph on local SSD with a memory-resident subset, which suits collections larger than memory.
- **D:** Incorrect for this question. Redis vector search serves low-latency similarity queries from memory. The corpus must fit the memory budget and be rebuilt on model change. Why the correct answer wins: DiskANN keeps the graph on local SSD with a memory-resident subset, which suits collections larger than memory.

### Question 62 — A

Answer: Inspect the plan with EXPLAIN ANALYZE before changing indexes. EXPLAIN ANALYZE shows the chosen plan, row estimates, and where the time is actually spent. The plan shows whether PostgreSQL uses the vector index and where the time goes. Adding indexes without reading the plan often misses the cause. Local study-map skill 2.6 (PostgreSQL Connection and Schema Modeling), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Cosmos DB and PostgreSQL vector documentation: https://learn.microsoft.com/en-us/azure/cosmos-db/

- **A:** Correct. The plan shows whether PostgreSQL uses the vector index and where the time goes. Adding indexes without reading the plan often misses the cause. In this case: EXPLAIN ANALYZE shows the chosen plan, row estimates, and where the time is actually spent.
- **B:** Incorrect for this question. A replica offloads read traffic but introduces replication lag, which is dangerous for freshly written evidence. It does not reduce index memory pressure. Why the correct answer wins: EXPLAIN ANALYZE shows the chosen plan, row estimates, and where the time is actually spent.
- **C:** Incorrect for this question. Statistics and dead-tuple cleanup change plan quality and index performance. Autovacuum tuning matters for churn-heavy vector tables. Why the correct answer wins: EXPLAIN ANALYZE shows the chosen plan, row estimates, and where the time is actually spent.
- **D:** Incorrect for this question. Index creation and bulk loads are I/O heavy, and throttled storage stretches maintenance windows. Storage limits are separate from compute. Why the correct answer wins: EXPLAIN ANALYZE shows the chosen plan, row estimates, and where the time is actually spent.

### Question 63 — D

Answer: Increase storage throughput for index builds and bulk loads. Storage throughput governs bulk load and index build speed when CPU and memory are not the bottleneck. Index creation and bulk loads are I/O heavy, and throttled storage stretches maintenance windows. Storage limits are separate from compute. Local study-map skill 2.8 (PostgreSQL Compute, Memory, and Storage Sizing), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Cosmos DB and PostgreSQL vector documentation: https://learn.microsoft.com/en-us/azure/cosmos-db/

- **A:** Incorrect for this question. A replica offloads read traffic but introduces replication lag, which is dangerous for freshly written evidence. It does not reduce index memory pressure. Why the correct answer wins: Storage throughput governs bulk load and index build speed when CPU and memory are not the bottleneck.
- **B:** Incorrect for this question. Vector indexes are memory-hungry, so undersized compute causes swapping and slow queries. Right-size before tuning index parameters. Why the correct answer wins: Storage throughput governs bulk load and index build speed when CPU and memory are not the bottleneck.
- **C:** Incorrect for this question. The plan shows whether PostgreSQL uses the vector index and where the time goes. Adding indexes without reading the plan often misses the cause. Why the correct answer wins: Storage throughput governs bulk load and index build speed when CPU and memory are not the bottleneck.
- **D:** Correct. Index creation and bulk loads are I/O heavy, and throttled storage stretches maintenance windows. Storage limits are separate from compute. In this case: Storage throughput governs bulk load and index build speed when CPU and memory are not the bottleneck.

### Question 64 — B

Answer: Use prepared statements and batch round trips. Prepared statements with batched parameters collapse repeated round trips into fewer, cheaper calls. Prepared statements avoid repeated planning and reduce chatty network calls. They pair well with pooling but can interact with pool modes. Local study-map skill 2.10 (PostgreSQL Connection Optimization), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Cosmos DB and PostgreSQL vector documentation: https://learn.microsoft.com/en-us/azure/cosmos-db/

- **A:** Incorrect for this question. A replica offloads read traffic but introduces replication lag, which is dangerous for freshly written evidence. It does not reduce index memory pressure. Why the correct answer wins: Prepared statements with batched parameters collapse repeated round trips into fewer, cheaper calls.
- **B:** Correct. Prepared statements avoid repeated planning and reduce chatty network calls. They pair well with pooling but can interact with pool modes. In this case: Prepared statements with batched parameters collapse repeated round trips into fewer, cheaper calls.
- **C:** Incorrect for this question. A bounded pool amortizes connection setup and protects the server from connection storms. Pool size must match server limits. Why the correct answer wins: Prepared statements with batched parameters collapse repeated round trips into fewer, cheaper calls.
- **D:** Incorrect for this question. An external pooler multiplexes server connections for serverless or highly concurrent clients. Session-level features may be unavailable in transaction mode. Why the correct answer wins: Prepared statements with batched parameters collapse repeated round trips into fewer, cheaper calls.

### Question 65 — A

Answer: Use a distributed lock in Redis to make processing idempotent. A distributed lock keyed on the transaction identifier makes concurrent processing of the same work impossible. A lock can serialize work across instances, but correctness under retries still needs idempotency keys in the data store. Locks expire and can be lost. Local study-map skill 2.11 (Azure Managed Redis Caching and Invalidation), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Cosmos DB and PostgreSQL vector documentation: https://learn.microsoft.com/en-us/azure/cosmos-db/

- **A:** Correct. A lock can serialize work across instances, but correctness under retries still needs idempotency keys in the data store. Locks expire and can be lost. In this case: A distributed lock keyed on the transaction identifier makes concurrent processing of the same work impossible.
- **B:** Incorrect for this question. Flushing removes all cached content at once, causing a stampede to the origin and a latency cliff. Targeted invalidation is safer. Why the correct answer wins: A distributed lock keyed on the transaction identifier makes concurrent processing of the same work impossible.
- **C:** Incorrect for this question. Eviction protects memory but evicts unpredictably, so a hot key can vanish before its freshness bound is reached. It is not a substitute for TTL design. Why the correct answer wins: A distributed lock keyed on the transaction identifier makes concurrent processing of the same work impossible.
- **D:** Incorrect for this question. A TTL bounds staleness and reclaims memory without a manual sweep. Too long a TTL hides source changes; too short wastes the cache. Why the correct answer wins: A distributed lock keyed on the transaction identifier makes concurrent processing of the same work impossible.

### Question 66 — B, E

Answers: Create an HNSW index for low-latency approximate search; Scale compute and memory to fit index size and query concurrency. HNSW provides low-latency approximate search, and sizing compute and memory to the index keeps it resident. HNSW gives fast approximate nearest-neighbour queries with a larger memory footprint and slower builds. Recall is tunable at query time. Vector indexes are memory-hungry, so undersized compute causes swapping and slow queries. Right-size before tuning index parameters. Local study-map skill 2.7 (pgvector Indexing and Query Latency), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Cosmos DB and PostgreSQL vector documentation: https://learn.microsoft.com/en-us/azure/cosmos-db/

- **A:** Incorrect for this question. An exact scan is accurate but scales linearly and burns compute. It is a baseline for measuring recall, not a production strategy. Why the correct answer wins: HNSW provides low-latency approximate search, and sizing compute and memory to the index keeps it resident.
- **B:** Correct. Vector indexes are memory-hungry, so undersized compute causes swapping and slow queries. Right-size before tuning index parameters. In this case: HNSW provides low-latency approximate search, and sizing compute and memory to the index keeps it resident.
- **C:** Incorrect for this question. IVFFlat uses clustering lists and needs periodic rebuilds as data grows, but costs less memory than HNSW. Probes trade recall for speed. Why the correct answer wins: HNSW provides low-latency approximate search, and sizing compute and memory to the index keeps it resident.
- **D:** Incorrect for this question. Index creation and bulk loads are I/O heavy, and throttled storage stretches maintenance windows. Storage limits are separate from compute. Why the correct answer wins: HNSW provides low-latency approximate search, and sizing compute and memory to the index keeps it resident.
- **E:** Correct. HNSW gives fast approximate nearest-neighbour queries with a larger memory footprint and slower builds. Recall is tunable at query time. In this case: HNSW provides low-latency approximate search, and sizing compute and memory to the index keeps it resident.

### Question 67 — A, E

Answers: Reuse a bounded connection pool instead of opening a connection per request; Use prepared statements and batch round trips. A bounded pool caps connections per instance, and prepared statements remove repeated parse and bind round trips. A bounded pool amortizes connection setup and protects the server from connection storms. Pool size must match server limits. Prepared statements avoid repeated planning and reduce chatty network calls. They pair well with pooling but can interact with pool modes. Local study-map skill 2.10 (PostgreSQL Connection Optimization), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Cosmos DB and PostgreSQL vector documentation: https://learn.microsoft.com/en-us/azure/cosmos-db/

- **A:** Correct. A bounded pool amortizes connection setup and protects the server from connection storms. Pool size must match server limits. In this case: A bounded pool caps connections per instance, and prepared statements remove repeated parse and bind round trips.
- **B:** Incorrect for this question. A replica offloads read traffic but introduces replication lag, which is dangerous for freshly written evidence. It does not reduce index memory pressure. Why the correct answer wins: A bounded pool caps connections per instance, and prepared statements remove repeated parse and bind round trips.
- **C:** Incorrect for this question. An external pooler multiplexes server connections for serverless or highly concurrent clients. Session-level features may be unavailable in transaction mode. Why the correct answer wins: A bounded pool caps connections per instance, and prepared statements remove repeated parse and bind round trips.
- **D:** Incorrect for this question. Index creation and bulk loads are I/O heavy, and throttled storage stretches maintenance windows. Storage limits are separate from compute. Why the correct answer wins: A bounded pool caps connections per instance, and prepared statements remove repeated parse and bind round trips.
- **E:** Correct. Prepared statements avoid repeated planning and reduce chatty network calls. They pair well with pooling but can interact with pool modes. In this case: A bounded pool caps connections per instance, and prepared statements remove repeated parse and bind round trips.

### Question 68 — A

Answer: Enable the change feed on the container → create a lease container → start the processor with a unique instance name → read inserts and updates in order → checkpoint the continuation. The feed and its leases must exist before a processor can own partitions, read in order, and checkpoint. The feed must be enabled and leases available before a processor can own partitions and checkpoint progress. Local study-map skill 2.5 (Cosmos DB Change Feed Processing), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Cosmos DB and PostgreSQL vector documentation: https://learn.microsoft.com/en-us/azure/cosmos-db/

- **A:** Correct. The feed must be enabled and leases available before a processor can own partitions and checkpoint progress. In this case: The feed and its leases must exist before a processor can own partitions, read in order, and checkpoint.
- **B:** Incorrect for this question. Reading events before the processor exists and before leases are created cannot work. Why the correct answer wins: The feed and its leases must exist before a processor can own partitions, read in order, and checkpoint.
- **C:** Incorrect for this question. A checkpoint is written by a running processor, so it cannot precede the processor start. Why the correct answer wins: The feed and its leases must exist before a processor can own partitions, read in order, and checkpoint.
- **D:** Incorrect for this question. Enabling the feed and creating leases must happen before any processor reads or checkpoints. Why the correct answer wins: The feed and its leases must exist before a processor can own partitions, read in order, and checkpoint.

### Question 69 — B

Answer: Use Service Bus sessions to keep related messages ordered. Sessions give exclusive, ordered processing per session identifier across competing consumers. Sessions give ordered, exclusive processing per session ID across competing consumers. They require session-aware senders and receivers. Local study-map skill 3.1 (Service Bus Queues and Sessions), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure messaging and Functions documentation: https://learn.microsoft.com/en-us/azure/service-bus-messaging/

- **A:** Incorrect for this question. Peek-lock keeps the message locked until the handler completes it, giving at-least-once processing with retry. Lock duration must exceed processing time. Why the correct answer wins: Sessions give exclusive, ordered processing per session identifier across competing consumers.
- **B:** Correct. Sessions give ordered, exclusive processing per session ID across competing consumers. They require session-aware senders and receivers. In this case: Sessions give exclusive, ordered processing per session identifier across competing consumers.
- **C:** Incorrect for this question. A delivery cap stops infinite retries of a failing message and moves it to the dead-letter queue. The cap must exceed legitimate transient retries. Why the correct answer wins: Sessions give exclusive, ordered processing per session identifier across competing consumers.
- **D:** Incorrect for this question. A duplicate-detection window drops repeated sends within the window, which helps with at-least-once producers. The window is time-bounded. Why the correct answer wins: Sessions give exclusive, ordered processing per session identifier across competing consumers.

### Question 70 — B

Answer: Receive with peek-lock and complete or abandon explicitly. Peek-lock keeps the message invisible but unremoved until completion, so a crash leads to redelivery rather than loss. Peek-lock keeps the message locked until the handler completes it, giving at-least-once processing with retry. Lock duration must exceed processing time. Local study-map skill 3.3 (Service Bus Dead-Lettering and Retries), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure messaging and Functions documentation: https://learn.microsoft.com/en-us/azure/service-bus-messaging/

- **A:** Incorrect for this question. A duplicate-detection window drops repeated sends within the window, which helps with at-least-once producers. The window is time-bounded. Why the correct answer wins: Peek-lock keeps the message invisible but unremoved until completion, so a crash leads to redelivery rather than loss.
- **B:** Correct. Peek-lock keeps the message locked until the handler completes it, giving at-least-once processing with retry. Lock duration must exceed processing time. In this case: Peek-lock keeps the message invisible but unremoved until completion, so a crash leads to redelivery rather than loss.
- **C:** Incorrect for this question. Receive-and-delete removes the message on delivery, so a crash loses work silently. It suits telemetry, not payments. Why the correct answer wins: Peek-lock keeps the message invisible but unremoved until completion, so a crash leads to redelivery rather than loss.
- **D:** Incorrect for this question. Prepared statements avoid repeated planning and reduce chatty network calls. They pair well with pooling but can interact with pool modes. Why the correct answer wins: Peek-lock keeps the message invisible but unremoved until completion, so a crash leads to redelivery rather than loss.

### Question 71 — C

Answer: Filter the Event Grid subscription by subject or event type. A subscription filter evaluates event properties broker-side so only matching events are delivered. Subject and event-type filters keep handlers focused and reduce cost. Filters are evaluated on event metadata, not payload body. Local study-map skill 3.4 (Event Grid Filters, Custom Events, and Retries), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure messaging and Functions documentation: https://learn.microsoft.com/en-us/azure/service-bus-messaging/

- **A:** Incorrect for this question. A custom schema fits domain events that are not resource lifecycle notifications. Consumers must version the schema contract. Why the correct answer wins: A subscription filter evaluates event properties broker-side so only matching events are delivered.
- **B:** Incorrect for this question. Subscription filters route only matching messages to a handler, reducing wasted processing. Filter evaluation happens broker-side on message properties. Why the correct answer wins: A subscription filter evaluates event properties broker-side so only matching events are delivered.
- **C:** Correct. Subject and event-type filters keep handlers focused and reduce cost. Filters are evaluated on event metadata, not payload body. In this case: A subscription filter evaluates event properties broker-side so only matching events are delivered.
- **D:** Incorrect for this question. Event Hubs ingests high-volume ordered streams with partitions and consumer groups. It is a streaming log, not a task queue. Why the correct answer wins: A subscription filter evaluates event properties broker-side so only matching events are delivered.

### Question 72 — C

Answer: Define a custom event schema for the topic. A custom event schema carries the domain payload for events that Azure resources do not publish themselves. A custom schema fits domain events that are not resource lifecycle notifications. Consumers must version the schema contract. Local study-map skill 3.4 (Event Grid Filters, Custom Events, and Retries), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure messaging and Functions documentation: https://learn.microsoft.com/en-us/azure/service-bus-messaging/

- **A:** Incorrect for this question. Event Grid retries failed deliveries with backoff and can store undeliverable events. Handlers must still be idempotent. Why the correct answer wins: A custom event schema carries the domain payload for events that Azure resources do not publish themselves.
- **B:** Incorrect for this question. System topics carry Azure resource lifecycle events. Domain events that are not resource changes need a custom topic and schema. Why the correct answer wins: A custom event schema carries the domain payload for events that Azure resources do not publish themselves.
- **C:** Correct. A custom schema fits domain events that are not resource lifecycle notifications. Consumers must version the schema contract. In this case: A custom event schema carries the domain payload for events that Azure resources do not publish themselves.
- **D:** Incorrect for this question. Event Hubs ingests high-volume ordered streams with partitions and consumer groups. It is a streaming log, not a task queue. Why the correct answer wins: A custom event schema carries the domain payload for events that Azure resources do not publish themselves.

### Question 73 — B

Answer: Orchestrate the multi-step workflow with Durable Functions. Durable Functions checkpoint orchestration state and can wait for an external event without holding a process open. Durable Functions provides orchestrations, activities, timers, and retries with checkpointed state. Orchestrator code must stay deterministic. Local study-map skill 3.5 (Azure Functions Triggers and Bindings), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure messaging and Functions documentation: https://learn.microsoft.com/en-us/azure/service-bus-messaging/

- **A:** Incorrect for this question. An HTTP trigger gives a synchronous API endpoint with route and authorization configuration. Long-running work should hand off to a queue. Why the correct answer wins: Durable Functions checkpoint orchestration state and can wait for an external event without holding a process open.
- **B:** Correct. Durable Functions provides orchestrations, activities, timers, and retries with checkpointed state. Orchestrator code must stay deterministic. In this case: Durable Functions checkpoint orchestration state and can wait for an external event without holding a process open.
- **C:** Incorrect for this question. A trigger starts the function when work arrives and handles the receive loop for you. Poison-message behavior is configured in host settings. Why the correct answer wins: Durable Functions checkpoint orchestration state and can wait for an external event without holding a process open.
- **D:** Incorrect for this question. Bindings reduce boilerplate for common inputs and outputs and are configured declaratively. Complex operations still need the SDK. Why the correct answer wins: Durable Functions checkpoint orchestration state and can wait for an external event without holding a process open.

### Question 74 — A

Answer: Host the function app on the consumption plan. The consumption plan bills per execution and scales to zero, which suits a short daily job. Consumption bills per execution and scales automatically, with cold starts and a timeout ceiling. It fits spiky, short work. Local study-map skill 3.6 (Function App Configuration and Deployment), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure messaging and Functions documentation: https://learn.microsoft.com/en-us/azure/service-bus-messaging/

- **A:** Correct. Consumption bills per execution and scales automatically, with cold starts and a timeout ceiling. It fits spiky, short work. In this case: The consumption plan bills per execution and scales to zero, which suits a short daily job.
- **B:** Incorrect for this question. A premium plan reduces cold starts and supports virtual network integration and longer timeouts. It costs more than consumption. Why the correct answer wins: The consumption plan bills per execution and scales to zero, which suits a short daily job.
- **C:** Incorrect for this question. A timer trigger invokes the function on a schedule without an external caller. Overlapping runs and the time zone must be configured deliberately. Why the correct answer wins: The consumption plan bills per execution and scales to zero, which suits a short daily job.
- **D:** Incorrect for this question. Durable Functions provides orchestrations, activities, timers, and retries with checkpointed state. Orchestrator code must stay deterministic. Why the correct answer wins: The consumption plan bills per execution and scales to zero, which suits a short daily job.

### Question 75 — D

Answer: Configure the host retry policy with exponential backoff. A host retry policy with exponential backoff spaces attempts so a throttled dependency can recover. The host retry policy re-executes a failing trigger with bounded attempts and backoff. It cannot make a non-idempotent handler safe to replay. Local study-map skill 3.6 (Function App Configuration and Deployment), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure messaging and Functions documentation: https://learn.microsoft.com/en-us/azure/service-bus-messaging/

- **A:** Incorrect for this question. Pipeline deployment keeps code and configuration versioned together and repeatable. Secrets belong in a vault reference, not in the pipeline file. Why the correct answer wins: A host retry policy with exponential backoff spaces attempts so a throttled dependency can recover.
- **B:** Incorrect for this question. Concurrency and batch size bound how much work one instance takes at a time, which controls downstream pressure and memory. Too high a value causes throttling and timeouts. Why the correct answer wins: A host retry policy with exponential backoff spaces attempts so a throttled dependency can recover.
- **C:** Incorrect for this question. A premium plan reduces cold starts and supports virtual network integration and longer timeouts. It costs more than consumption. Why the correct answer wins: A host retry policy with exponential backoff spaces attempts so a throttled dependency can recover.
- **D:** Correct. The host retry policy re-executes a failing trigger with bounded attempts and backoff. It cannot make a non-idempotent handler safe to replay. In this case: A host retry policy with exponential backoff spaces attempts so a throttled dependency can recover.

### Question 76 — C, E

Answers: Use Service Bus sessions to keep related messages ordered; Enable duplicate detection on the queue. Sessions provide ordered processing per cardholder, and duplicate detection removes repeated message identifiers. Sessions give ordered, exclusive processing per session ID across competing consumers. They require session-aware senders and receivers. A duplicate-detection window drops repeated sends within the window, which helps with at-least-once producers. The window is time-bounded. Local study-map skill 3.1 (Service Bus Queues and Sessions), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure messaging and Functions documentation: https://learn.microsoft.com/en-us/azure/service-bus-messaging/

- **A:** Incorrect for this question. Peek-lock keeps the message locked until the handler completes it, giving at-least-once processing with retry. Lock duration must exceed processing time. Why the correct answer wins: Sessions provide ordered processing per cardholder, and duplicate detection removes repeated message identifiers.
- **B:** Incorrect for this question. Receive-and-delete removes the message on delivery, so a crash loses work silently. It suits telemetry, not payments. Why the correct answer wins: Sessions provide ordered processing per cardholder, and duplicate detection removes repeated message identifiers.
- **C:** Correct. A duplicate-detection window drops repeated sends within the window, which helps with at-least-once producers. The window is time-bounded. In this case: Sessions provide ordered processing per cardholder, and duplicate detection removes repeated message identifiers.
- **D:** Incorrect for this question. Dead-lettering preserves poison messages for diagnosis instead of losing them. Resubmission needs a fix and an idempotent handler. Why the correct answer wins: Sessions provide ordered processing per cardholder, and duplicate detection removes repeated message identifiers.
- **E:** Correct. Sessions give ordered, exclusive processing per session ID across competing consumers. They require session-aware senders and receivers. In this case: Sessions provide ordered processing per cardholder, and duplicate detection removes repeated message identifiers.

### Question 77 — C, E

Answers: Set a maximum delivery count and handle the dead-letter path; Inspect the dead-letter queue and resubmit corrected messages. A delivery cap stops the endless retry, and dead-lettering preserves the message for inspection. A delivery cap stops infinite retries of a failing message and moves it to the dead-letter queue. The cap must exceed legitimate transient retries. Dead-lettering preserves poison messages for diagnosis instead of losing them. Resubmission needs a fix and an idempotent handler. Local study-map skill 3.3 (Service Bus Dead-Lettering and Retries), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure messaging and Functions documentation: https://learn.microsoft.com/en-us/azure/service-bus-messaging/

- **A:** Incorrect for this question. A duplicate-detection window drops repeated sends within the window, which helps with at-least-once producers. The window is time-bounded. Why the correct answer wins: A delivery cap stops the endless retry, and dead-lettering preserves the message for inspection.
- **B:** Incorrect for this question. Peek-lock keeps the message locked until the handler completes it, giving at-least-once processing with retry. Lock duration must exceed processing time. Why the correct answer wins: A delivery cap stops the endless retry, and dead-lettering preserves the message for inspection.
- **C:** Correct. Dead-lettering preserves poison messages for diagnosis instead of losing them. Resubmission needs a fix and an idempotent handler. In this case: A delivery cap stops the endless retry, and dead-lettering preserves the message for inspection.
- **D:** Incorrect for this question. Receive-and-delete removes the message on delivery, so a crash loses work silently. It suits telemetry, not payments. Why the correct answer wins: A delivery cap stops the endless retry, and dead-lettering preserves the message for inspection.
- **E:** Correct. A delivery cap stops infinite retries of a failing message and moves it to the dead-letter queue. The cap must exceed legitimate transient retries. In this case: A delivery cap stops the endless retry, and dead-lettering preserves the message for inspection.

### Question 78 — C

Answer: Publish the message → receive with peek-lock → process the work → complete the message → dead-letter after the delivery limit. Peek-lock receipt precedes processing, completion follows success, and dead-lettering happens only after the limit. Peek-lock keeps the message until the handler succeeds, and only repeated failures should dead-letter it. Local study-map skill 3.1 (Service Bus Queues and Sessions), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure messaging and Functions documentation: https://learn.microsoft.com/en-us/azure/service-bus-messaging/

- **A:** Incorrect for this question. Completing a message before processing discards the work and defeats at-least-once delivery. Why the correct answer wins: Peek-lock receipt precedes processing, completion follows success, and dead-lettering happens only after the limit.
- **B:** Incorrect for this question. The message cannot be received before it is published, and completion must follow processing. Why the correct answer wins: Peek-lock receipt precedes processing, completion follows success, and dead-lettering happens only after the limit.
- **C:** Correct. Peek-lock keeps the message until the handler succeeds, and only repeated failures should dead-letter it. In this case: Peek-lock receipt precedes processing, completion follows success, and dead-lettering happens only after the limit.
- **D:** Incorrect for this question. Work cannot be processed before the message is published and received. Why the correct answer wins: Peek-lock receipt precedes processing, completion follows success, and dead-lettering happens only after the limit.

### Question 79 — D

Answer: Pin the application to a specific secret version. Pinning to a specific secret version makes the decision reproducible even after later rotations. Pinning a version makes a rotation invisible to the app until it is redeployed, which is useful for break-glass and dangerous for routine rotation. Local study-map skill 4.1 (Key Vault Secret Storage, Rotation, and Retrieval), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Key Vault, App Configuration, and Monitor documentation: https://learn.microsoft.com/en-us/azure/azure-monitor/

- **A:** Incorrect for this question. A managed identity issues tokens from the platform, removing secret distribution from the app. Role assignment still scopes what it can reach. Why the correct answer wins: Pinning to a specific secret version makes the decision reproducible even after later rotations.
- **B:** Incorrect for this question. Rotation limits the value of a leaked secret, but callers must read the latest version rather than caching an old one forever. Why the correct answer wins: Pinning to a specific secret version makes the decision reproducible even after later rotations.
- **C:** Incorrect for this question. Soft delete and purge protection stop accidental or malicious permanent loss of secrets. They also constrain how names can be reused. Why the correct answer wins: Pinning to a specific secret version makes the decision reproducible even after later rotations.
- **D:** Correct. Pinning a version makes a rotation invisible to the app until it is redeployed, which is useful for break-glass and dangerous for routine rotation. In this case: Pinning to a specific secret version makes the decision reproducible even after later rotations.

### Question 80 — A

Answer: Enable purge protection and soft delete on the vault. Soft delete with purge protection keeps a deleted vault recoverable for the retention period. Soft delete and purge protection stop accidental or malicious permanent loss of secrets. They also constrain how names can be reused. Local study-map skill 4.1 (Key Vault Secret Storage, Rotation, and Retrieval), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Key Vault, App Configuration, and Monitor documentation: https://learn.microsoft.com/en-us/azure/azure-monitor/

- **A:** Correct. Soft delete and purge protection stop accidental or malicious permanent loss of secrets. They also constrain how names can be reused. In this case: Soft delete with purge protection keeps a deleted vault recoverable for the retention period.
- **B:** Incorrect for this question. Rotation limits the value of a leaked secret, but callers must read the latest version rather than caching an old one forever. Why the correct answer wins: Soft delete with purge protection keeps a deleted vault recoverable for the retention period.
- **C:** Incorrect for this question. A vault centralizes secret storage with access control and audit. Retrieval should use an identity, not a copied credential. Why the correct answer wins: Soft delete with purge protection keeps a deleted vault recoverable for the retention period.
- **D:** Incorrect for this question. Vault access is a separate authorization decision from the app identity. Without a data-plane role or policy the reference fails at runtime. Why the correct answer wins: Soft delete with purge protection keeps a deleted vault recoverable for the retention period.

### Question 81 — B

Answer: Use App Configuration labels to separate environments. App Configuration labels separate environments inside one store while keeping a single place to manage keys. Labels keep dev, test, and prod values in one store with one key schema. A misconfigured label selector silently serves the wrong values. Local study-map skill 4.2 (App Configuration Settings and Feature Flags), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Key Vault, App Configuration, and Monitor documentation: https://learn.microsoft.com/en-us/azure/azure-monitor/

- **A:** Incorrect for this question. App Configuration separates configuration from code and supports labels, feature flags, and Key Vault references. Change still needs a refresh strategy. Why the correct answer wins: App Configuration labels separate environments inside one store while keeping a single place to manage keys.
- **B:** Correct. Labels keep dev, test, and prod values in one store with one key schema. A misconfigured label selector silently serves the wrong values. In this case: App Configuration labels separate environments inside one store while keeping a single place to manage keys.
- **C:** Incorrect for this question. Sentinel-key or polling refresh lets a running app pick up new settings. Refresh intervals trade responsiveness against request volume. Why the correct answer wins: App Configuration labels separate environments inside one store while keeping a single place to manage keys.
- **D:** Incorrect for this question. Pinning a version makes a rotation invisible to the app until it is redeployed, which is useful for break-glass and dangerous for routine rotation. Why the correct answer wins: App Configuration labels separate environments inside one store while keeping a single place to manage keys.

### Question 82 — D

Answer: Export telemetry through an OpenTelemetry collector. An OpenTelemetry collector receives spans from the app and forwards them to the approved backend. A collector batches, filters, and routes telemetry, and decouples app configuration from the backend. It is another component to run and monitor. Local study-map skill 4.3 (Distributed Tracing with OpenTelemetry), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Key Vault, App Configuration, and Monitor documentation: https://learn.microsoft.com/en-us/azure/azure-monitor/

- **A:** Incorrect for this question. Including the trace ID in log records lets you pivot from a failed span to its log lines. Without it, logs and traces are separate worlds. Why the correct answer wins: An OpenTelemetry collector receives spans from the app and forwards them to the approved backend.
- **B:** Incorrect for this question. Application Insights correlates requests, dependencies, and exceptions into end-to-end transactions. Sampling can hide rare failures. Why the correct answer wins: An OpenTelemetry collector receives spans from the app and forwards them to the approved backend.
- **C:** Incorrect for this question. OpenTelemetry emits vendor-neutral traces, metrics, and logs with context propagation. Exporters and sampling decide what reaches the backend. Why the correct answer wins: An OpenTelemetry collector receives spans from the app and forwards them to the approved backend.
- **D:** Correct. A collector batches, filters, and routes telemetry, and decouples app configuration from the backend. It is another component to run and monitor. In this case: An OpenTelemetry collector receives spans from the app and forwards them to the approved backend.

### Question 83 — B

Answer: Use head or tail sampling so trace volume stays within budget. Sampling keeps trace volume inside budget, and tail sampling can retain the slow and failed transactions. Sampling keeps telemetry cost bounded, but aggressive sampling can hide rare failures. Tail sampling can retain errors preferentially. Local study-map skill 4.3 (Distributed Tracing with OpenTelemetry), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Key Vault, App Configuration, and Monitor documentation: https://learn.microsoft.com/en-us/azure/azure-monitor/

- **A:** Incorrect for this question. Including the trace ID in log records lets you pivot from a failed span to its log lines. Without it, logs and traces are separate worlds. Why the correct answer wins: Sampling keeps trace volume inside budget, and tail sampling can retain the slow and failed transactions.
- **B:** Correct. Sampling keeps telemetry cost bounded, but aggressive sampling can hide rare failures. Tail sampling can retain errors preferentially. In this case: Sampling keeps trace volume inside budget, and tail sampling can retain the slow and failed transactions.
- **C:** Incorrect for this question. A span records the duration and outcome of one operation and nests under the trace. It makes the slow dependency visible in the transaction view. Why the correct answer wins: Sampling keeps trace volume inside budget, and tail sampling can retain the slow and failed transactions.
- **D:** Incorrect for this question. Propagation stitches one trace across HTTP, messaging, and Functions so the whole path is visible. Missing propagation breaks the trace at that hop. Why the correct answer wins: Sampling keeps trace volume inside budget, and tail sampling can retain the slow and failed transactions.

### Question 84 — D

Answer: Reach the data service through a private endpoint. A private endpoint places the service on a private address inside the virtual network instead of a public one. A private endpoint keeps traffic on the virtual network and removes public exposure. DNS resolution must be wired to the private zone. Local study-map skill 4.5 (Identity-Based Access for Application Services), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Key Vault, App Configuration, and Monitor documentation: https://learn.microsoft.com/en-us/azure/azure-monitor/

- **A:** Incorrect for this question. Platform logs and metrics must be routed before they can be queried or alerted on. Retention and cost follow the workspace settings. Why the correct answer wins: A private endpoint places the service on a private address inside the virtual network instead of a public one.
- **B:** Incorrect for this question. A private endpoint needs matching name resolution or clients still resolve the public address. The zone must be linked to the workload network. Why the correct answer wins: A private endpoint places the service on a private address inside the virtual network instead of a public one.
- **C:** Incorrect for this question. Reaching a dependency from the pod or replica proves DNS, egress, and firewall paths together. Host-side tests can succeed while the container path fails. Why the correct answer wins: A private endpoint places the service on a private address inside the virtual network instead of a public one.
- **D:** Correct. A private endpoint keeps traffic on the virtual network and removes public exposure. DNS resolution must be wired to the private zone. In this case: A private endpoint places the service on a private address inside the virtual network instead of a public one.

### Question 85 — B, C

Answers: Correlate logs with the operation or trace identifier; Propagate trace context across every service and queue hop. Emitting the operation identifier in logs makes them joinable, and carrying trace context across the hop keeps one trace. Including the trace ID in log records lets you pivot from a failed span to its log lines. Without it, logs and traces are separate worlds. Propagation stitches one trace across HTTP, messaging, and Functions so the whole path is visible. Missing propagation breaks the trace at that hop. Local study-map skill 4.3 (Distributed Tracing with OpenTelemetry), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Key Vault, App Configuration, and Monitor documentation: https://learn.microsoft.com/en-us/azure/azure-monitor/

- **A:** Incorrect for this question. Application Insights correlates requests, dependencies, and exceptions into end-to-end transactions. Sampling can hide rare failures. Why the correct answer wins: Emitting the operation identifier in logs makes them joinable, and carrying trace context across the hop keeps one trace.
- **B:** Correct. Including the trace ID in log records lets you pivot from a failed span to its log lines. Without it, logs and traces are separate worlds. In this case: Emitting the operation identifier in logs makes them joinable, and carrying trace context across the hop keeps one trace.
- **C:** Correct. Propagation stitches one trace across HTTP, messaging, and Functions so the whole path is visible. Missing propagation breaks the trace at that hop. In this case: Emitting the operation identifier in logs makes them joinable, and carrying trace context across the hop keeps one trace.
- **D:** Incorrect for this question. A span records the duration and outcome of one operation and nests under the trace. It makes the slow dependency visible in the transaction view. Why the correct answer wins: Emitting the operation identifier in logs makes them joinable, and carrying trace context across the hop keeps one trace.
- **E:** Incorrect for this question. Sampling keeps telemetry cost bounded, but aggressive sampling can hide rare failures. Tail sampling can retain errors preferentially. Why the correct answer wins: Emitting the operation identifier in logs makes them joinable, and carrying trace context across the hop keeps one trace.

### Question 86 — A, C

Answers: Create an alert rule on the failure rate or latency metric; Route the alert to an action group with a named owner. An alert rule evaluates the metric or query, and an action group defines who is notified when it fires. An alert turns a threshold breach into a notification or action. Thresholds need a baseline, or the alert is noise. An action group defines who is notified and which automation runs when an alert fires. An alert with no action group is only a record in the portal. Local study-map skill 4.4 (KQL Queries for Logs and Metrics), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Key Vault, App Configuration, and Monitor documentation: https://learn.microsoft.com/en-us/azure/azure-monitor/

- **A:** Correct. An alert turns a threshold breach into a notification or action. Thresholds need a baseline, or the alert is noise. In this case: An alert rule evaluates the metric or query, and an action group defines who is notified when it fires.
- **B:** Incorrect for this question. Reducing columns and rows early lowers query cost and latency. Broad queries over long ranges are the usual cause of slow KQL. Why the correct answer wins: An alert rule evaluates the metric or query, and an action group defines who is notified when it fires.
- **C:** Correct. An action group defines who is notified and which automation runs when an alert fires. An alert with no action group is only a record in the portal. In this case: An alert rule evaluates the metric or query, and an action group defines who is notified when it fires.
- **D:** Incorrect for this question. Retention and the table plan determine how long data is queryable and what it costs. Lower retention reduces cost but shortens the investigation window. Why the correct answer wins: An alert rule evaluates the metric or query, and an action group defines who is notified when it fires.
- **E:** Incorrect for this question. Platform metrics are cheap and near-real-time, so they suit latency and failure-rate alerts. Log-based alerts add latency and query cost. Why the correct answer wins: An alert rule evaluates the metric or query, and an action group defines who is notified when it fires.

### Question 87 — A, E

Answers: Store settings and feature flags in Azure App Configuration; Ship the code dark behind a feature flag. App Configuration centralizes the value, and a feature flag turns the behaviour on or off without a release. App Configuration separates configuration from code and supports labels, feature flags, and Key Vault references. Change still needs a refresh strategy. A feature flag enables reviewed code in production without a redeploy and lets it be switched off instantly. Flag state still needs ownership and cleanup. Local study-map skill 4.2 (App Configuration Settings and Feature Flags), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Key Vault, App Configuration, and Monitor documentation: https://learn.microsoft.com/en-us/azure/azure-monitor/

- **A:** Correct. App Configuration separates configuration from code and supports labels, feature flags, and Key Vault references. Change still needs a refresh strategy. In this case: App Configuration centralizes the value, and a feature flag turns the behaviour on or off without a release.
- **B:** Incorrect for this question. Sentinel-key or polling refresh lets a running app pick up new settings. Refresh intervals trade responsiveness against request volume. Why the correct answer wins: App Configuration centralizes the value, and a feature flag turns the behaviour on or off without a release.
- **C:** Incorrect for this question. A Key Vault reference keeps non-secret settings in App Configuration while the value stays in the vault. The app identity needs both sets of permissions. Why the correct answer wins: App Configuration centralizes the value, and a feature flag turns the behaviour on or off without a release.
- **D:** Incorrect for this question. Labels keep dev, test, and prod values in one store with one key schema. A misconfigured label selector silently serves the wrong values. Why the correct answer wins: App Configuration centralizes the value, and a feature flag turns the behaviour on or off without a release.
- **E:** Correct. A feature flag enables reviewed code in production without a redeploy and lets it be switched off instantly. Flag state still needs ownership and cleanup. In this case: App Configuration centralizes the value, and a feature flag turns the behaviour on or off without a release.

### Question 88 — B

Answer: Assign a managed identity to the app → grant the least-privilege data-plane role → move the credential into Key Vault → disable public network access behind a private endpoint → verify the call from inside the app. Identity and permission come before the credential is retired, and the network lockdown is verified from the workload. Identity and permission come before removing the old credential, and the network lockdown is verified from the workload itself. Local study-map skill 4.1 (Key Vault Secret Storage, Rotation, and Retrieval), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Key Vault, App Configuration, and Monitor documentation: https://learn.microsoft.com/en-us/azure/azure-monitor/

- **A:** Incorrect for this question. The app loses its credential and its route before any replacement access is granted. Why the correct answer wins: Identity and permission come before the credential is retired, and the network lockdown is verified from the workload.
- **B:** Correct. Identity and permission come before removing the old credential, and the network lockdown is verified from the workload itself. In this case: Identity and permission come before the credential is retired, and the network lockdown is verified from the workload.
- **C:** Incorrect for this question. Verification cannot happen before the access model is changed and permission is granted. Why the correct answer wins: Identity and permission come before the credential is retired, and the network lockdown is verified from the workload.
- **D:** Incorrect for this question. Closing the network first breaks the app before identity-based access exists. Why the correct answer wins: Identity and permission come before the credential is retired, and the network lockdown is verified from the workload.

### Question 89 — D

Answer: Filter on metadata columns in the same query as the vector search. Filtering inside the vector query keeps scope and result completeness together. Combining a WHERE filter with the distance operator keeps retrieval inside the caller's scope and improves relevance. Index the filter columns too. Local study-map skill 2.9 (PostgreSQL RAG with Metadata Filters), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Cosmos DB and PostgreSQL vector documentation: https://learn.microsoft.com/en-us/azure/cosmos-db/

- **A:** Incorrect for this question. Post-filtering can return fewer results than requested and can leak existence or counts if the filtering is careless. Push authorization into the query. Why the correct answer wins: Filtering inside the vector query keeps scope and result completeness together.
- **B:** Incorrect for this question. An exact scan is accurate but scales linearly and burns compute. It is a baseline for measuring recall, not a production strategy. Why the correct answer wins: Filtering inside the vector query keeps scope and result completeness together.
- **C:** Incorrect for this question. HNSW gives fast approximate nearest-neighbour queries with a larger memory footprint and slower builds. Recall is tunable at query time. Why the correct answer wins: Filtering inside the vector query keeps scope and result completeness together.
- **D:** Correct. Combining a WHERE filter with the distance operator keeps retrieval inside the caller's scope and improves relevance. Index the filter columns too. In this case: Filtering inside the vector query keeps scope and result completeness together.

### Question 90 — D

Answer: Define a custom event schema for the topic. A custom topic with a domain event schema carries the notification. A custom schema fits domain events that are not resource lifecycle notifications. Consumers must version the schema contract. Local study-map skill 3.4 (Event Grid Filters, Custom Events, and Retries), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure messaging and Functions documentation: https://learn.microsoft.com/en-us/azure/service-bus-messaging/

- **A:** Incorrect for this question. Subject and event-type filters keep handlers focused and reduce cost. Filters are evaluated on event metadata, not payload body. Why the correct answer wins: A custom topic with a domain event schema carries the notification.
- **B:** Incorrect for this question. System topics carry Azure resource lifecycle events. Domain events that are not resource changes need a custom topic and schema. Why the correct answer wins: A custom topic with a domain event schema carries the notification.
- **C:** Incorrect for this question. Event Grid retries failed deliveries with backoff and can store undeliverable events. Handlers must still be idempotent. Why the correct answer wins: A custom topic with a domain event schema carries the notification.
- **D:** Correct. A custom schema fits domain events that are not resource lifecycle notifications. Consumers must version the schema contract. In this case: A custom topic with a domain event schema carries the notification.

### Question 91 — C

Answer: Rotate the secret on a schedule and let apps resolve the current version. Rotate to a new version, update the source, and let the app read the current version. Rotation limits the value of a leaked secret, but callers must read the latest version rather than caching an old one forever. Local study-map skill 4.1 (Key Vault Secret Storage, Rotation, and Retrieval), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Key Vault, App Configuration, and Monitor documentation: https://learn.microsoft.com/en-us/azure/azure-monitor/

- **A:** Incorrect for this question. Soft delete and purge protection stop accidental or malicious permanent loss of secrets. They also constrain how names can be reused. Why the correct answer wins: Rotate to a new version, update the source, and let the app read the current version.
- **B:** Incorrect for this question. Pinning a version makes a rotation invisible to the app until it is redeployed, which is useful for break-glass and dangerous for routine rotation. Why the correct answer wins: Rotate to a new version, update the source, and let the app read the current version.
- **C:** Correct. Rotation limits the value of a leaked secret, but callers must read the latest version rather than caching an old one forever. In this case: Rotate to a new version, update the source, and let the app read the current version.
- **D:** Incorrect for this question. A managed identity issues tokens from the platform, removing secret distribution from the app. Role assignment still scopes what it can reach. Why the correct answer wins: Rotate to a new version, update the source, and let the app read the current version.

### Question 92 — A

Answer: Give the KEDA scaler a managed identity to read the event source. A KEDA scaler that authenticates with a managed identity needs that identity to have read access on the event source. A scaler needs permission to read queue metrics; identity-based access avoids a stored connection string. Least privilege still applies to that identity. Local study-map skill 1.5 (Event-Driven Scaling with KEDA), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure container hosting documentation: https://learn.microsoft.com/en-us/azure/container-apps/

- **A:** Correct. A scaler needs permission to read queue metrics; identity-based access avoids a stored connection string. Least privilege still applies to that identity. In this case: A KEDA scaler that authenticates with a managed identity needs that identity to have read access on the event source.
- **B:** Incorrect for this question. CPU-based scaling reacts after work is already queued and cannot scale to zero on an empty queue. It suits steady request-driven services. Why the correct answer wins: A KEDA scaler that authenticates with a managed identity needs that identity to have read access on the event source.
- **C:** Incorrect for this question. HPA adjusts replicas from resource metrics but needs metrics-server and enough node capacity. It cannot scale to zero. Why the correct answer wins: A KEDA scaler that authenticates with a managed identity needs that identity to have read access on the event source.
- **D:** Incorrect for this question. A queue-length scaler adds replicas while work is backed up and removes them when the queue drains. Message lock duration must exceed processing time. Why the correct answer wins: A KEDA scaler that authenticates with a managed identity needs that identity to have read access on the event source.

### Question 93 — B

Answer: Filter on metadata columns in the same query as the vector search. Filtering on metadata in the same statement as the distance operator keeps the result both scoped and complete. Combining a WHERE filter with the distance operator keeps retrieval inside the caller's scope and improves relevance. Index the filter columns too. Local study-map skill 2.9 (PostgreSQL RAG with Metadata Filters), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Cosmos DB and PostgreSQL vector documentation: https://learn.microsoft.com/en-us/azure/cosmos-db/

- **A:** Incorrect for this question. An external pooler multiplexes server connections for serverless or highly concurrent clients. Session-level features may be unavailable in transaction mode. Why the correct answer wins: Filtering on metadata in the same statement as the distance operator keeps the result both scoped and complete.
- **B:** Correct. Combining a WHERE filter with the distance operator keeps retrieval inside the caller's scope and improves relevance. Index the filter columns too. In this case: Filtering on metadata in the same statement as the distance operator keeps the result both scoped and complete.
- **C:** Incorrect for this question. Post-filtering can return fewer results than requested and can leak existence or counts if the filtering is careless. Push authorization into the query. Why the correct answer wins: Filtering on metadata in the same statement as the distance operator keeps the result both scoped and complete.
- **D:** Incorrect for this question. HNSW gives fast approximate nearest-neighbour queries with a larger memory footprint and slower builds. Recall is tunable at query time. Why the correct answer wins: Filtering on metadata in the same statement as the distance operator keeps the result both scoped and complete.

### Question 94 — A

Answer: Publish to a Service Bus topic with multiple subscriptions. A topic with separate subscriptions fans out one event to every consumer and tracks each position independently. Topics fan out one message to independent subscribers, each with its own filter and dead-letter queue. Subscribers process at their own pace. Local study-map skill 3.2 (Service Bus Topics, Subscriptions, and Filters), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure messaging and Functions documentation: https://learn.microsoft.com/en-us/azure/service-bus-messaging/

- **A:** Correct. Topics fan out one message to independent subscribers, each with its own filter and dead-letter queue. Subscribers process at their own pace. In this case: A topic with separate subscriptions fans out one event to every consumer and tracks each position independently.
- **B:** Incorrect for this question. Queue Storage is simple and cheap for large backlogs with at-least-once delivery. It lacks topics, sessions, and scheduled messages. Why the correct answer wins: A topic with separate subscriptions fans out one event to every consumer and tracks each position independently.
- **C:** Incorrect for this question. A custom schema fits domain events that are not resource lifecycle notifications. Consumers must version the schema contract. Why the correct answer wins: A topic with separate subscriptions fans out one event to every consumer and tracks each position independently.
- **D:** Incorrect for this question. A queue decouples producers from a single consumer group and smooths bursts. Delivery semantics depend on receive mode and completion. Why the correct answer wins: A topic with separate subscriptions fans out one event to every consumer and tracks each position independently.

### Question 95 — C

Answer: Test end-to-end connectivity from inside the container to each dependency. Testing from inside the container proves DNS, network rules, and egress paths the host test never exercised. Reaching a dependency from the pod or replica proves DNS, egress, and firewall paths together. Host-side tests can succeed while the container path fails. Local study-map skill 1.7 (Container Logs, Events, and Connectivity), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure container hosting documentation: https://learn.microsoft.com/en-us/azure/container-apps/

- **A:** Incorrect for this question. Platform logs and metrics must be routed before they can be queried or alerted on. Retention and cost follow the workspace settings. Why the correct answer wins: Testing from inside the container proves DNS, network rules, and egress paths the host test never exercised.
- **B:** Incorrect for this question. Readiness gates traffic until the app can serve it, and liveness restarts a wedged container. Wrong thresholds cause restart loops. Why the correct answer wins: Testing from inside the container proves DNS, network rules, and egress paths the host test never exercised.
- **C:** Correct. Reaching a dependency from the pod or replica proves DNS, egress, and firewall paths together. Host-side tests can succeed while the container path fails. In this case: Testing from inside the container proves DNS, network rules, and egress paths the host test never exercised.
- **D:** Incorrect for this question. Container Apps and AKS surface stdout logs and platform events into a workspace for KQL analysis. Verbosity and retention cost money. Why the correct answer wins: Testing from inside the container proves DNS, network rules, and egress paths the host test never exercised.

### Question 96 — C

Answer: Set a maximum delivery count and handle the dead-letter path. A maximum delivery count dead-letters the message after bounded attempts. A delivery cap stops infinite retries of a failing message and moves it to the dead-letter queue. The cap must exceed legitimate transient retries. Local study-map skill 3.3 (Service Bus Dead-Lettering and Retries), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure messaging and Functions documentation: https://learn.microsoft.com/en-us/azure/service-bus-messaging/

- **A:** Incorrect for this question. Receive-and-delete removes the message on delivery, so a crash loses work silently. It suits telemetry, not payments. Why the correct answer wins: A maximum delivery count dead-letters the message after bounded attempts.
- **B:** Incorrect for this question. A duplicate-detection window drops repeated sends within the window, which helps with at-least-once producers. The window is time-bounded. Why the correct answer wins: A maximum delivery count dead-letters the message after bounded attempts.
- **C:** Correct. A delivery cap stops infinite retries of a failing message and moves it to the dead-letter queue. The cap must exceed legitimate transient retries. In this case: A maximum delivery count dead-letters the message after bounded attempts.
- **D:** Incorrect for this question. Peek-lock keeps the message locked until the handler completes it, giving at-least-once processing with retry. Lock duration must exceed processing time. Why the correct answer wins: A maximum delivery count dead-letters the message after bounded attempts.

### Question 97 — B

Answer: Alert on platform metrics rather than only on log queries. Platform metric alerts are cheap and near-real-time for rate and latency thresholds. Platform metrics are cheap and near-real-time, so they suit latency and failure-rate alerts. Log-based alerts add latency and query cost. Local study-map skill 4.4 (KQL Queries for Logs and Metrics), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Key Vault, App Configuration, and Monitor documentation: https://learn.microsoft.com/en-us/azure/azure-monitor/

- **A:** Incorrect for this question. Time-binned aggregation reveals the shape of an incident: a step change, a ramp, or a periodic spike. Averages alone hide short outages. Why the correct answer wins: Platform metric alerts are cheap and near-real-time for rate and latency thresholds.
- **B:** Correct. Platform metrics are cheap and near-real-time, so they suit latency and failure-rate alerts. Log-based alerts add latency and query cost. In this case: Platform metric alerts are cheap and near-real-time for rate and latency thresholds.
- **C:** Incorrect for this question. An alert turns a threshold breach into a notification or action. Thresholds need a baseline, or the alert is noise. Why the correct answer wins: Platform metric alerts are cheap and near-real-time for rate and latency thresholds.
- **D:** Incorrect for this question. Reducing columns and rows early lowers query cost and latency. Broad queries over long ranges are the usual cause of slow KQL. Why the correct answer wins: Platform metric alerts are cheap and near-real-time for rate and latency thresholds.

### Question 98 — A

Answer: Build the vector index concurrently so writes are not blocked. CREATE INDEX CONCURRENTLY keeps reads and writes flowing during the build at the cost of a longer runtime. CREATE INDEX CONCURRENTLY keeps inserts and updates flowing during the build, at the cost of a longer build and extra I/O. A failed build leaves an invalid index to drop. Local study-map skill 2.7 (pgvector Indexing and Query Latency), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Cosmos DB and PostgreSQL vector documentation: https://learn.microsoft.com/en-us/azure/cosmos-db/

- **A:** Correct. CREATE INDEX CONCURRENTLY keeps inserts and updates flowing during the build, at the cost of a longer build and extra I/O. A failed build leaves an invalid index to drop. In this case: CREATE INDEX CONCURRENTLY keeps reads and writes flowing during the build at the cost of a longer runtime.
- **B:** Incorrect for this question. Index creation and bulk loads are I/O heavy, and throttled storage stretches maintenance windows. Storage limits are separate from compute. Why the correct answer wins: CREATE INDEX CONCURRENTLY keeps reads and writes flowing during the build at the cost of a longer runtime.
- **C:** Incorrect for this question. Statistics and dead-tuple cleanup change plan quality and index performance. Autovacuum tuning matters for churn-heavy vector tables. Why the correct answer wins: CREATE INDEX CONCURRENTLY keeps reads and writes flowing during the build at the cost of a longer runtime.
- **D:** Incorrect for this question. Vector indexes are memory-hungry, so undersized compute causes swapping and slow queries. Right-size before tuning index parameters. Why the correct answer wins: CREATE INDEX CONCURRENTLY keeps reads and writes flowing during the build at the cost of a longer runtime.

### Question 99 — D

Answer: Set a maximum delivery count and handle the dead-letter path. A maximum delivery count moves a persistently failing message to the dead-letter queue after bounded attempts. A delivery cap stops infinite retries of a failing message and moves it to the dead-letter queue. The cap must exceed legitimate transient retries. Local study-map skill 3.3 (Service Bus Dead-Lettering and Retries), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure messaging and Functions documentation: https://learn.microsoft.com/en-us/azure/service-bus-messaging/

- **A:** Incorrect for this question. Peek-lock keeps the message locked until the handler completes it, giving at-least-once processing with retry. Lock duration must exceed processing time. Why the correct answer wins: A maximum delivery count moves a persistently failing message to the dead-letter queue after bounded attempts.
- **B:** Incorrect for this question. A duplicate-detection window drops repeated sends within the window, which helps with at-least-once producers. The window is time-bounded. Why the correct answer wins: A maximum delivery count moves a persistently failing message to the dead-letter queue after bounded attempts.
- **C:** Incorrect for this question. Dead-lettering preserves poison messages for diagnosis instead of losing them. Resubmission needs a fix and an idempotent handler. Why the correct answer wins: A maximum delivery count moves a persistently failing message to the dead-letter queue after bounded attempts.
- **D:** Correct. A delivery cap stops infinite retries of a failing message and moves it to the dead-letter queue. The cap must exceed legitimate transient retries. In this case: A maximum delivery count moves a persistently failing message to the dead-letter queue after bounded attempts.

### Question 100 — D

Answer: Store repeated aggregations in a materialized view or update policy. A materialized view or update policy stores the repeated aggregation so the dashboard no longer scans raw data. Precomputed results avoid recomputing expensive aggregations on every dashboard refresh. The trade-off is storage and freshness lag. Local study-map skill 4.4 (KQL Queries for Logs and Metrics), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Key Vault, App Configuration, and Monitor documentation: https://learn.microsoft.com/en-us/azure/azure-monitor/

- **A:** Incorrect for this question. Joining request and dependency telemetry shows which downstream call fails inside a slow request. Cross-workspace joins need the right scope. Why the correct answer wins: A materialized view or update policy stores the repeated aggregation so the dashboard no longer scans raw data.
- **B:** Incorrect for this question. Time-binned aggregation reveals the shape of an incident: a step change, a ramp, or a periodic spike. Averages alone hide short outages. Why the correct answer wins: A materialized view or update policy stores the repeated aggregation so the dashboard no longer scans raw data.
- **C:** Incorrect for this question. Reducing columns and rows early lowers query cost and latency. Broad queries over long ranges are the usual cause of slow KQL. Why the correct answer wins: A materialized view or update policy stores the repeated aggregation so the dashboard no longer scans raw data.
- **D:** Correct. Precomputed results avoid recomputing expensive aggregations on every dashboard refresh. The trade-off is storage and freshness lag. In this case: A materialized view or update policy stores the repeated aggregation so the dashboard no longer scans raw data.
