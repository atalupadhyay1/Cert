# Microsoft AI-200 — Full-Length Mock Exam 5

Azure AI Cloud Developer Associate · 100 questions · expanded practice bank · passing target 700/1000

Blueprint-weighted mock exam of 100 items. Item mix: 84 multiple-choice (8 of them sequencing items with four candidate sequences), 16 multi-select (selection count stated), and 4 case studies of 3 questions. Hot-area, drag-and-drop UI, labs, and adaptive problem-solution sets cannot be reproduced in a CSV; see the README for the exact fidelity boundary.

Original educational content, not actual, recalled, or copied Microsoft exam items.

## Questions

### 1. Every release must map to one reviewed artifact so an auditor can identify what ran. Which practice should be enforced?

Domain: Develop containerized solutions on Azure

- A. Run image builds on demand or on a trigger with ACR Tasks
- B. Apply an ACR retention policy to prune old untagged manifests
- C. Deploy the mutable latest tag and let the platform resolve it
- D. Build and store versioned images in Azure Container Registry

### 2. A weekly dependency patch must produce a fresh image without a local Docker host. What should be configured?

Domain: Develop containerized solutions on Azure

- A. Build and store versioned images in Azure Container Registry
- B. Stage the change in a deployment slot and swap after verification
- C. Replicate the registry to each deployment region
- D. Run image builds on demand or on a trigger with ACR Tasks

### 3. A small permit-status API needs platform patching, deployment slots, and no cluster administration. What should host it?

Domain: Develop containerized solutions on Azure

- A. Deploy the service to Azure Container Apps
- B. Deploy the workload to Azure Kubernetes Service
- C. Run the batch job in Azure Container Instances
- D. Deploy the image to Azure App Service as a web app

### 4. A registry credential must be usable by the container without appearing in application settings. What should be used?

Domain: Develop containerized solutions on Azure

- A. Reference a Key Vault secret from the app configuration instead of storing it
- B. Stage the change in a deployment slot and swap after verification
- C. Deploy the image to Azure App Service as a web app
- D. Supply configuration through App Service application settings

### 5. A new eligibility service must take a small share of live traffic before full rollout. Which feature provides that?

Domain: Develop containerized solutions on Azure

- A. Configure Container Apps ingress for internal-only access
- B. Stage the change in a deployment slot and swap after verification
- C. Scale the container app on an event source with a KEDA scaler
- D. Create a new Container Apps revision and shift traffic between revisions

### 6. Replica count oscillates every minute during fluctuating load and downstream calls spike on each scale-in. What should be tuned?

Domain: Develop containerized solutions on Azure

- A. Tune the scale rule cool-down period and maximum replicas
- B. Rely on the horizontal pod autoscaler on CPU
- C. Scale the container app on an event source with a KEDA scaler
- D. Set a minimum replica count above zero for the container app

### 7. The deployment must be declared in version control and reapplied safely after manual drift. What should be used?

Domain: Develop containerized solutions on Azure

- A. Rely on the horizontal pod autoscaler on CPU
- B. Apply a declarative Kubernetes manifest to the cluster
- C. Add readiness and liveness probes to the pod specification
- D. Run the batch job in Azure Container Instances

### 8. Operators need container stdout and cluster events searchable together after an incident. What should be used?

Domain: Develop containerized solutions on Azure

- A. Enable diagnostic settings to route platform logs to the workspace
- B. Query container logs and Kubernetes events in Log Analytics
- C. Test end-to-end connectivity from inside the container to each dependency
- D. Send telemetry to Application Insights and inspect the transaction view

### 9. An eligibility endpoint must support a canary and stay warm during office hours. Which two settings provide that? Select two.

Domain: Develop containerized solutions on Azure

- A. Tune the scale rule cool-down period and maximum replicas
- B. Rely on the horizontal pod autoscaler on CPU
- C. Create a new Container Apps revision and shift traffic between revisions
- D. Set a minimum replica count above zero for the container app
- E. Configure Container Apps ingress for internal-only access

### 10. Document conversion must follow queue depth, including scale to zero overnight. Which two elements are required? Select two.

Domain: Develop containerized solutions on Azure

- A. Scale only on CPU utilization without an event scaler
- B. Rely on the horizontal pod autoscaler on CPU
- C. Scale the container app on an event source with a KEDA scaler
- D. Run the batch job in Azure Container Instances
- E. Scale on the Service Bus queue length with a KEDA Azure Service Bus scaler

### 11. Which sequence correctly rolls out a canary revision of the eligibility service?

Domain: Develop containerized solutions on Azure

- A. Deploy a new revision → shift all traffic → build and push the image → check metrics → roll back
- B. Build and push the image → deploy a new revision → shift a small traffic percentage → check metrics → promote or roll back
- C. Shift all traffic to a new revision → deploy the revision → check metrics → build the image → promote
- D. Check metrics → deploy a new revision → build and push the image → shift a small traffic percentage → promote

### 12. An application file must be read by case identifier and year without scanning the container. What should the query include?

Domain: Develop AI solutions by using Azure data management services

- A. Query through the Cosmos DB SDK with parameterized queries
- B. Increase provisioned throughput and watch the RU charge per query
- C. Include the partition key in the query predicate
- D. Restrict the indexing policy to the paths the queries use

### 13. The service must query documents through the officially supported client and reuse connections. What should be used?

Domain: Develop AI solutions by using Azure data management services

- A. Enable autoscale throughput with a maximum RU limit
- B. Batch related writes in a transactional batch within one partition key
- C. Query through the Cosmos DB SDK with parameterized queries
- D. Use a lease container to coordinate change feed readers

### 14. Most properties are never filtered, but every write still pays to index them. What should be changed?

Domain: Develop AI solutions by using Azure data management services

- A. Index every property by using the default automatic policy
- B. Restrict the indexing policy to the paths the queries use
- C. Set an item time-to-live on the container
- D. Increase provisioned throughput and watch the RU charge per query

### 15. A public statistics dashboard can tolerate slightly stale counts at the lowest cost. Which level fits?

Domain: Develop AI solutions by using Azure data management services

- A. Choose the account consistency level that matches the read requirement
- B. Use eventual consistency to minimize read cost
- C. Use session consistency for reads within the same client session
- D. Use strong consistency for every read in the account

### 16. Newly submitted applications must be queued for eligibility checks without polling. What should be implemented?

Domain: Develop AI solutions by using Azure data management services

- A. Run a change feed processor to react to new and updated items
- B. Batch related writes in a transactional batch within one partition key
- C. Enable duplicate detection on the queue
- D. Use a lease container to coordinate change feed readers

### 17. Policy passages must be filtered by program and searched semantically in one statement. What should be used?

Domain: Develop AI solutions by using Azure data management services

- A. Scan every document and compute similarity in application code
- B. Store the documents in Azure Cosmos DB for NoSQL
- C. Cache responses in Azure Managed Redis
- D. Store embeddings in PostgreSQL by using the pgvector extension

### 18. A large vector table must fit a modest memory budget and periodic rebuilds are acceptable. Which index fits?

Domain: Develop AI solutions by using Azure data management services

- A. Create an HNSW index for low-latency approximate search
- B. Create an IVFFlat index to save memory on a large table
- C. Increase storage throughput for index builds and bulk loads
- D. Query without a vector index and let PostgreSQL scan the table

### 19. Index rebuilds exceed the maintenance window because storage throughput is saturated. What should be addressed?

Domain: Develop AI solutions by using Azure data management services

- A. Scale compute and memory to fit index size and query concurrency
- B. Increase maintenance and query memory settings for index builds and sorts
- C. Reuse a bounded connection pool instead of opening a connection per request
- D. Increase storage throughput for index builds and bulk loads

### 20. A burst of short-lived clients exhausts server connection slots despite a per-instance pool. What should be added?

Domain: Develop AI solutions by using Azure data management services

- A. Place a connection pooler in front of PostgreSQL for many short-lived clients
- B. Use prepared statements and batch round trips
- C. Add a read replica and send all vector queries to it
- D. Reuse a bounded connection pool instead of opening a connection per request

### 21. A fee change must be visible in cached eligibility answers immediately. What is required?

Domain: Develop AI solutions by using Azure data management services

- A. Rely on the eviction policy and skip explicit TTLs
- B. Set a TTL on each cached entry
- C. Invalidate or overwrite the cache entry when the source changes
- D. Flush the database after each deployment to guarantee fresh data

### 22. A citizen's multi-step form must keep its progress across instances and restarts. What should be used?

Domain: Develop AI solutions by using Azure data management services

- A. Create a vector index in Managed Redis for similarity search
- B. Cache responses in Azure Managed Redis
- C. Use a distributed lock in Redis to make processing idempotent
- D. Store user session state in Managed Redis with an expiry

### 23. Policy retrieval must filter on program and must not leak other programs' clauses. Which two choices are required? Select two.

Domain: Develop AI solutions by using Azure data management services

- A. Query without a vector index and let PostgreSQL scan the table
- B. Filter on metadata columns in the same query as the vector search
- C. Scale compute and memory to fit index size and query concurrency
- D. Retrieve nearest neighbours first and discard unauthorized rows in the application
- E. Model typed columns for filters and one vector column for the embedding

### 24. A hot lookup must come from memory and a similarity shortcut must avoid the relational database. Which two capabilities are required? Select two.

Domain: Develop AI solutions by using Azure data management services

- A. Rely on the eviction policy and skip explicit TTLs
- B. Use a distributed lock in Redis to make processing idempotent
- C. Set a TTL on each cached entry
- D. Create a vector index in Managed Redis for similarity search
- E. Cache responses in Azure Managed Redis

### 25. Which sequence correctly prepares policy passages for vector search?

Domain: Develop AI solutions by using Azure data management services

- A. Build the index → create the vector extension → create the table with a vector column → query nearest neighbours
- B. Create the vector extension → create the table with a vector column → build the index → query nearest neighbours with a distance operator
- C. Query nearest neighbours → build the index → create the vector extension → create the table with a vector column
- D. Create the table with a vector column → query nearest neighbours → create the vector extension → build the index

### 26. Each uploaded document must be converted by exactly one worker with crash recovery. What should be used?

Domain: Connect to and consume Azure services

- A. Queue the work on a Service Bus queue and process it with a worker
- B. Stream telemetry through Azure Event Hubs
- C. Use Azure Queue Storage for the work items
- D. Publish to a Service Bus topic with multiple subscriptions

### 27. Notification, verification, and archive services must each receive the same submission event. What should be used?

Domain: Connect to and consume Azure services

- A. Use Azure Queue Storage for the work items
- B. Queue the work on a Service Bus queue and process it with a worker
- C. Publish to a Service Bus topic with multiple subscriptions
- D. Define a custom event schema for the topic

### 28. A retried submission must not create a second case number. What should the handler use?

Domain: Connect to and consume Azure services

- A. Inspect the dead-letter queue and resubmit corrected messages
- B. Make the handler idempotent by using a message or business key
- C. Set a maximum delivery count and handle the dead-letter path
- D. Enable duplicate detection on the queue

### 29. A downstream notification endpoint is briefly offline and events must not be dropped permanently. What should be configured?

Domain: Connect to and consume Azure services

- A. Define a custom event schema for the topic
- B. Rely on Event Grid retries with a dead-letter destination
- C. Filter the Event Grid subscription by subject or event type
- D. Deliver events by using a managed identity instead of a key

### 30. A conversion function must start when a queue message arrives. What should be configured?

Domain: Connect to and consume Azure services

- A. Expose the endpoint through an HTTP trigger
- B. Bind a queue or event trigger to the function
- C. Use input and output bindings instead of hand-written SDK calls
- D. Orchestrate the multi-step workflow with Durable Functions

### 31. A spiky, short conversion task must scale automatically and cost little when idle. Which plan fits?

Domain: Connect to and consume Azure services

- A. Use a deployment slot on the function app for staging
- B. Orchestrate the multi-step workflow with Durable Functions
- C. Host the function app on a premium plan with pre-warmed instances
- D. Host the function app on the consumption plan

### 32. Function code and settings must be deployed repeatably from a pipeline with secrets kept out of the file. What should be done?

Domain: Connect to and consume Azure services

- A. Host the function app on a premium plan with pre-warmed instances
- B. Orchestrate the multi-step workflow with Durable Functions
- C. Deploy the function app through a CI pipeline with app settings applied
- D. Use a deployment slot on the function app for staging

### 33. A poison document must not block the queue and must be recoverable later. Which two capabilities provide that? Select two.

Domain: Connect to and consume Azure services

- A. Receive in receive-and-delete mode for at-most-once delivery
- B. Use Service Bus sessions to keep related messages ordered
- C. Inspect the dead-letter queue and resubmit corrected messages
- D. Set a maximum delivery count and handle the dead-letter path
- E. Enable duplicate detection on the queue

### 34. A domain event that is not a resource change must be published and routed only to the correct subscriber. Which two elements are required? Select two.

Domain: Connect to and consume Azure services

- A. Add a SQL or correlation filter to a subscription
- B. Deliver events by using a managed identity instead of a key
- C. Rely on Event Grid retries with a dead-letter destination
- D. Define a custom event schema for the topic
- E. Filter the Event Grid subscription by subject or event type

### 35. Which sequence correctly converts an uploaded document through the queue?

Domain: Connect to and consume Azure services

- A. Receive with peek-lock → publish the message → complete the message → process the work → dead-letter after the delivery limit
- B. Publish the message → complete the message → receive with peek-lock → process the work → dead-letter after the delivery limit
- C. Publish the message → receive with peek-lock → process the work → complete the message → dead-letter after the delivery limit
- D. Process the work → receive with peek-lock → publish the message → complete the message → dead-letter after the delivery limit

### 36. A deleted vault secret would break case processing for days if it were lost permanently. What should be enabled?

Domain: Secure, monitor, troubleshoot Azure solutions

- A. Enable purge protection and soft delete on the vault
- B. Pin the application to a specific secret version
- C. Store the secret in Azure Key Vault and read it at runtime
- D. Assign a least-privilege role to the application identity

### 37. A partner certificate must be replaced on a schedule with no outage. What should be implemented?

Domain: Secure, monitor, troubleshoot Azure solutions

- A. Rotate the secret on a schedule and let apps resolve the current version
- B. Pin the application to a specific secret version
- C. Grant the app identity data-plane access to the vault
- D. Supply configuration through App Service application settings

### 38. Test and production values must share one key schema in a single configuration store. What should be used?

Domain: Secure, monitor, troubleshoot Azure solutions

- A. Reference the Key Vault secret from an App Configuration key value
- B. Use App Configuration labels to separate environments
- C. Pin the application to a specific secret version
- D. Enable configuration refresh so changes apply without a restart

### 39. Telemetry must be batched, filtered, and routed to two backends without changing app code. What should be deployed?

Domain: Secure, monitor, troubleshoot Azure solutions

- A. Instrument the service with the OpenTelemetry SDK
- B. Use head or tail sampling so trace volume stays within budget
- C. Propagate trace context across every service and queue hop
- D. Export telemetry through an OpenTelemetry collector

### 40. The case database must not accept connections from the public internet. What should be configured?

Domain: Secure, monitor, troubleshoot Azure solutions

- A. Authenticate with a managed identity instead of a stored key
- B. Reach the data service through a private endpoint
- C. Enable diagnostic settings to route platform logs to the workspace
- D. Assign a least-privilege role to the application identity

### 41. The container must call storage and the database without any stored credential. What should it use?

Domain: Secure, monitor, troubleshoot Azure solutions

- A. Supply configuration through App Service application settings
- B. Authenticate with a managed identity instead of a stored key
- C. Assign a least-privilege role to the application identity
- D. Store the secret in Azure Key Vault and read it at runtime

### 42. A request path crosses an API, a queue, and a function, and one connected trace is required. Which two practices are essential? Select two.

Domain: Secure, monitor, troubleshoot Azure solutions

- A. Propagate trace context across every service and queue hop
- B. Instrument the service with the OpenTelemetry SDK
- C. Query the workspace with KQL to find the failing operation
- D. Export telemetry through an OpenTelemetry collector
- E. Use head or tail sampling so trace volume stays within budget

### 43. Log queries are slow and costly, and the team must also alert quickly on failures. Which two approaches are appropriate? Select two.

Domain: Secure, monitor, troubleshoot Azure solutions

- A. Project only the columns needed and filter by time first
- B. Create an alert rule on the failure rate or latency metric
- C. Aggregate with summarize and bin to see the failure rate over time
- D. Alert on platform metrics rather than only on log queries
- E. Store repeated aggregations in a materialized view or update policy

### 44. Which sequence correctly introduces a rotated partner secret?

Domain: Secure, monitor, troubleshoot Azure solutions

- A. Store the secret in Key Vault → grant the app identity access → reference the secret from the app → rotate the secret → the app reads the new version
- B. Reference the secret from the app → rotate the secret → store the secret in Key Vault → grant the app identity access → the app reads the new version
- C. Grant the app identity access → store the secret in Key Vault → rotate the secret → reference the secret from the app → the app reads the new version
- D. Rotate the secret → reference the secret from the app → store the secret in Key Vault → grant the app identity access → the app reads the new version

### 45. A permit service release must be reproducible years later for an audit, and a retagged rebuild must not change what ran. What should the deployment reference?

Domain: Develop containerized solutions on Azure

- A. Deploy the image by digest instead of a mutable tag
- B. Stage the change in a deployment slot and swap after verification
- C. Deploy the mutable latest tag and let the platform resolve it
- D. Apply an ACR retention policy to prune old untagged manifests

### 46. The permit service image must be rebuilt nightly from the main branch without any build server on the network. What should perform the build?

Domain: Develop containerized solutions on Azure

- A. Deploy the workload to Azure Kubernetes Service
- B. Implement the handler as an Azure Function
- C. Run image builds on demand or on a trigger with ACR Tasks
- D. Build and store versioned images in Azure Container Registry

### 47. Each regional portal needs a different fee table, and the table must change without a new image. What should supply it?

Domain: Develop containerized solutions on Azure

- A. Mount non-secret configuration from a Kubernetes ConfigMap
- B. Store settings and feature flags in Azure App Configuration
- C. Pin the application to a specific secret version
- D. Supply configuration through App Service application settings

### 48. The citizen registry key must never be stored in deployment settings or in the repository. What should the configuration use?

Domain: Develop containerized solutions on Azure

- A. Supply configuration through App Service application settings
- B. Reference a Key Vault secret from the app configuration instead of storing it
- C. Mount non-secret configuration from a Kubernetes ConfigMap
- D. Pin the application to a specific secret version

### 49. A single-container permit portal needs slots and platform-managed patching with no cluster to operate. Where should it run?

Domain: Develop containerized solutions on Azure

- A. Run the batch job in Azure Container Instances
- B. Deploy the service to Azure Container Apps
- C. Deploy the workload to Azure Kubernetes Service
- D. Deploy the image to Azure App Service as a web app

### 50. The OCR review API is idle overnight and needs revisions without a cluster, but the agency has no platform team. Where should it run?

Domain: Develop containerized solutions on Azure

- A. Deploy the workload to Azure Kubernetes Service
- B. Deploy the service to Azure Container Apps
- C. Run the batch job in Azure Container Instances
- D. Deploy the image to Azure App Service as a web app

### 51. Pods must read the registry key from the vault as an Azure identity, and no secret may be mounted. What should be configured?

Domain: Develop containerized solutions on Azure

- A. Replicate the registry to each deployment region
- B. Federate a Kubernetes service account to a managed identity
- C. Reference a Key Vault secret from the app configuration instead of storing it
- D. Deploy the mutable latest tag and let the platform resolve it

### 52. Only the OCR pods fail to reach the storage account after a firewall rule change, while other workloads still connect. What should be tested?

Domain: Develop containerized solutions on Azure

- A. Test end-to-end connectivity from inside the container to each dependency
- B. Aggregate with summarize and bin to see the failure rate over time
- C. Add readiness and liveness probes to the pod specification
- D. Enable diagnostic settings to route platform logs to the workspace

### 53. A permit portal must be verified in a warm slot before promotion, and its registry endpoint must differ per environment. Which two actions should you take? Select two.

Domain: Develop containerized solutions on Azure

- A. Stage the change in a deployment slot and swap after verification
- B. Supply configuration through App Service application settings
- C. Create a new Container Apps revision and shift traffic between revisions
- D. Apply a declarative Kubernetes manifest to the cluster
- E. Scale the container app on an event source with a KEDA scaler

### 54. Which sequence correctly promotes a new OCR review revision at a controlled percentage?

Domain: Develop containerized solutions on Azure

- A. Check metrics → deploy a new revision → build and push the image → shift a small traffic percentage → promote
- B. Shift all traffic to a new revision → deploy the revision → check metrics → build the image → promote
- C. Build and push the image → deploy a new revision → shift a small traffic percentage → check metrics → promote or roll back
- D. Deploy a new revision → shift all traffic → build and push the image → check metrics → roll back

### 55. Permit applications must be stored as JSON per applicant with point reads and residency-based isolation. Which store fits?

Domain: Develop AI solutions by using Azure data management services

- A. Store the documents in Azure Cosmos DB for NoSQL
- B. Include the partition key in the query predicate
- C. Use Azure Queue Storage for the work items
- D. Store embeddings in PostgreSQL by using the pgvector extension

### 56. A caseworker export of ninety thousand applications runs out of memory in the client. What should the client use?

Domain: Develop AI solutions by using Azure data management services

- A. Page large result sets with the continuation token
- B. Scan every document and compute similarity in application code
- C. Include the partition key in the query predicate
- D. Index every property by using the default automatic policy

### 57. Filing traffic peaks sharply at the statutory deadline and is nearly idle otherwise. What should be configured?

Domain: Develop AI solutions by using Azure data management services

- A. Restrict the indexing policy to the paths the queries use
- B. Index every property by using the default automatic policy
- C. Increase provisioned throughput and watch the RU charge per query
- D. Enable autoscale throughput with a maximum RU limit

### 58. A citizen must immediately see the application they just submitted, and cross-region ordering is irrelevant. Which consistency choice fits?

Domain: Develop AI solutions by using Azure data management services

- A. Use session consistency for reads within the same client session
- B. Choose the account consistency level that matches the read requirement
- C. Use eventual consistency to minimize read cost
- D. Use strong consistency for every read in the account

### 59. Policy documents and their embeddings must stay together so department and year filters apply in the same search. What should be used?

Domain: Develop AI solutions by using Azure data management services

- A. Use the DiskANN vector index for large collections
- B. Scan every document and compute similarity in application code
- C. Store embeddings in a vector property and query with VectorDistance
- D. Store embeddings in PostgreSQL by using the pgvector extension

### 60. Three processors must share the change feed for new applications, and no application may be processed twice. What coordinates them?

Domain: Develop AI solutions by using Azure data management services

- A. Run a change feed processor to react to new and updated items
- B. Set an item time-to-live on the container
- C. Enable duplicate detection on the queue
- D. Use a lease container to coordinate change feed readers

### 61. Four million archive chunks must be indexed on an instance whose memory cannot hold a graph index. What should be created?

Domain: Develop AI solutions by using Azure data management services

- A. Create an IVFFlat index to save memory on a large table
- B. Place a connection pooler in front of PostgreSQL for many short-lived clients
- C. Create an HNSW index for low-latency approximate search
- D. Query without a vector index and let PostgreSQL scan the table

### 62. The vector index build spills to disk and takes hours longer than the maintenance window allows. What should be increased?

Domain: Develop AI solutions by using Azure data management services

- A. Increase storage throughput for index builds and bulk loads
- B. Increase maintenance and query memory settings for index builds and sorts
- C. Run VACUUM and ANALYZE after bulk loads and large deletes
- D. Add a read replica and send all vector queries to it

### 63. A revised fee schedule is not visible on the portal until the cache entry expires an hour later. What is missing?

Domain: Develop AI solutions by using Azure data management services

- A. Invalidate or overwrite the cache entry when the source changes
- B. Flush the database after each deployment to guarantee fresh data
- C. Set a TTL on each cached entry
- D. Rely on the eviction policy and skip explicit TTLs

### 64. Public notice entries are viewed for a week and then never requested again, yet cache memory keeps growing. What should be configured?

Domain: Develop AI solutions by using Azure data management services

- A. Set a TTL on each cached entry
- B. Rely on the eviction policy and skip explicit TTLs
- C. Flush the database after each deployment to guarantee fresh data
- D. Invalidate or overwrite the cache entry when the source changes

### 65. An application store must query through the supported SDK and must keep applicant reads inside one partition. Which two actions should you take? Select two.

Domain: Develop AI solutions by using Azure data management services

- A. Query through the Cosmos DB SDK with parameterized queries
- B. Include the partition key in the query predicate
- C. Choose a high-cardinality partition key that spreads writes
- D. Index every property by using the default automatic policy
- E. Scan every document and compute similarity in application code

### 66. Policy search must answer in milliseconds and the index must stay resident under concurrent queries. Which two actions should you take? Select two.

Domain: Develop AI solutions by using Azure data management services

- A. Increase storage throughput for index builds and bulk loads
- B. Create an IVFFlat index to save memory on a large table
- C. Create an HNSW index for low-latency approximate search
- D. Query without a vector index and let PostgreSQL scan the table
- E. Scale compute and memory to fit index size and query concurrency

### 67. Which sequence correctly prepares an archive table for embedding search?

Domain: Develop AI solutions by using Azure data management services

- A. Query nearest neighbours → build the index → create the vector extension → create the table with a vector column
- B. Build the index → create the vector extension → create the table with a vector column → query nearest neighbours
- C. Create the table with a vector column → query nearest neighbours → create the vector extension → build the index
- D. Create the vector extension → create the table with a vector column → build the index → query nearest neighbours with a distance operator

### 68. Scanned pages for one application must be processed in page order by a single worker. What should be enabled?

Domain: Connect to and consume Azure services

- A. Set a maximum delivery count and handle the dead-letter path
- B. Receive with peek-lock and complete or abandon explicitly
- C. Use Service Bus sessions to keep related messages ordered
- D. Enable duplicate detection on the queue

### 69. The legal-review subscription must receive only applications whose type property is variance, while the archive sees every application. What should be configured?

Domain: Connect to and consume Azure services

- A. Define a custom event schema for the topic
- B. Enable duplicate detection on the queue
- C. Add a SQL or correlation filter to a subscription
- D. Filter the Event Grid subscription by subject or event type

### 70. A scanner retries on timeout, so the same page event can be published twice within minutes. What should be enabled?

Domain: Connect to and consume Azure services

- A. Set a maximum delivery count and handle the dead-letter path
- B. Inspect the dead-letter queue and resubmit corrected messages
- C. Make the handler idempotent by using a message or business key
- D. Enable duplicate detection on the queue

### 71. A scanned file landing in storage must start OCR with no polling and no custom publisher for the resource event. What should be used?

Domain: Connect to and consume Azure services

- A. Orchestrate the multi-step workflow with Durable Functions
- B. Use Azure Queue Storage for the work items
- C. Stream telemetry through Azure Event Hubs
- D. Publish the state change as an Event Grid event

### 72. A retention sweep must delete expired drafts every night at 01:00 with no caller. What should be used?

Domain: Connect to and consume Azure services

- A. Expose the endpoint through an HTTP trigger
- B. Rely on Event Grid retries with a dead-letter destination
- C. Run the scheduled maintenance from a timer trigger
- D. Bind a queue or event trigger to the function

### 73. A residency application requires three sequential approvals that arrive hours apart and must survive restarts. What should be used?

Domain: Connect to and consume Azure services

- A. Orchestrate the multi-step workflow with Durable Functions
- B. Bind a queue or event trigger to the function
- C. Expose the endpoint through an HTTP trigger
- D. Use input and output bindings instead of hand-written SDK calls

### 74. A queue-triggered OCR function saturates the shared model endpoint whenever a batch lands. What should be tuned?

Domain: Connect to and consume Azure services

- A. Configure the host retry policy with exponential backoff
- B. Host the function app on the consumption plan
- C. Tune the function app concurrency and batch size
- D. Host the function app on a premium plan with pre-warmed instances

### 75. Function code and its new settings must reach production together in one reviewed change. What should be used?

Domain: Connect to and consume Azure services

- A. Host the function app on a premium plan with pre-warmed instances
- B. Deploy the function app through a CI pipeline with app settings applied
- C. Expose the endpoint through an HTTP trigger
- D. Supply configuration through App Service application settings

### 76. Page events must be processed in order and the worker must stop round-tripping for one message at a time. Which two settings should you apply? Select two.

Domain: Connect to and consume Azure services

- A. Inspect the dead-letter queue and resubmit corrected messages
- B. Receive with peek-lock and complete or abandon explicitly
- C. Increase prefetch count to reduce round trips
- D. Receive in receive-and-delete mode for at-most-once delivery
- E. Use Service Bus sessions to keep related messages ordered

### 77. A domain event that is not a resource change must carry the agency's payload and must not be lost when the handler fails. Which two features are required? Select two.

Domain: Connect to and consume Azure services

- A. Stream telemetry through Azure Event Hubs
- B. Add a SQL or correlation filter to a subscription
- C. Rely on Event Grid retries with a dead-letter destination
- D. Filter the Event Grid subscription by subject or event type
- E. Define a custom event schema for the topic

### 78. Which sequence correctly processes a variance application message through Service Bus?

Domain: Connect to and consume Azure services

- A. Publish the message → receive with peek-lock → process the work → complete the message → dead-letter after the delivery limit
- B. Publish the message → complete the message → receive with peek-lock → process the work → dead-letter after the delivery limit
- C. Receive with peek-lock → publish the message → complete the message → process the work → dead-letter after the delivery limit
- D. Process the work → receive with peek-lock → publish the message → complete the message → dead-letter after the delivery limit

### 79. The portal reads a vault secret with its managed identity and receives 403 from the secret endpoint. What is missing?

Domain: Secure, monitor, troubleshoot Azure solutions

- A. Grant the app identity data-plane access to the vault
- B. Assign a least-privilege role to the application identity
- C. Store the secret in Azure Key Vault and read it at runtime
- D. Reference a Key Vault secret from the app configuration instead of storing it

### 80. A residency key must be replaced every sixty days without redeploying the portal. What should be configured?

Domain: Secure, monitor, troubleshoot Azure solutions

- A. Authenticate with a managed identity instead of a stored key
- B. Enable purge protection and soft delete on the vault
- C. Pin the application to a specific secret version
- D. Rotate the secret on a schedule and let apps resolve the current version

### 81. Four agency portals need shared flags with a single place to change them. What should be introduced?

Domain: Secure, monitor, troubleshoot Azure solutions

- A. Enable configuration refresh so changes apply without a restart
- B. Use App Configuration labels to separate environments
- C. Store settings and feature flags in Azure App Configuration
- D. Reference the Key Vault secret from an App Configuration key value

### 82. Operations needs the per-hour failure count for the upload endpoint across the last week. What should the query use?

Domain: Secure, monitor, troubleshoot Azure solutions

- A. Project only the columns needed and filter by time first
- B. Query the workspace with KQL to find the failing operation
- C. Aggregate with summarize and bin to see the failure rate over time
- D. Join the requests and dependencies tables on the operation ID

### 83. Verbose function logging doubled the workspace bill, and policy requires ninety days of retention only for audit tables. What should be tuned?

Domain: Secure, monitor, troubleshoot Azure solutions

- A. Query container logs and Kubernetes events in Log Analytics
- B. Alert on platform metrics rather than only on log queries
- C. Set the workspace retention and table plan to control log cost
- D. Enable diagnostic settings to route platform logs to the workspace

### 84. Residency data must never traverse the public internet between the portal and its database. What should be configured?

Domain: Secure, monitor, troubleshoot Azure solutions

- A. Reach the data service through a private endpoint
- B. Enable diagnostic settings to route platform logs to the workspace
- C. Link the private DNS zone so the private endpoint name resolves
- D. Test end-to-end connectivity from inside the container to each dependency

### 85. A new portal must read residency data with no stored credential and no broad subscription role. Which two actions should you take? Select two.

Domain: Secure, monitor, troubleshoot Azure solutions

- A. Reference a Key Vault secret from the app configuration instead of storing it
- B. Enable purge protection and soft delete on the vault
- C. Authenticate with a managed identity instead of a stored key
- D. Pin the application to a specific secret version
- E. Assign a least-privilege role to the application identity

### 86. One configuration store must serve four agencies and must not hold a secret value directly. Which two features are required? Select two.

Domain: Secure, monitor, troubleshoot Azure solutions

- A. Reference the Key Vault secret from an App Configuration key value
- B. Ship the code dark behind a feature flag
- C. Pin the application to a specific secret version
- D. Use App Configuration labels to separate environments
- E. Enable configuration refresh so changes apply without a restart

### 87. Telemetry must be vendor-portable and must reach the agency's approved backend without another code change. Which two components are required? Select two.

Domain: Secure, monitor, troubleshoot Azure solutions

- A. Export telemetry through an OpenTelemetry collector
- B. Send telemetry to Application Insights and inspect the transaction view
- C. Correlate logs with the operation or trace identifier
- D. Use head or tail sampling so trace volume stays within budget
- E. Instrument the service with the OpenTelemetry SDK

### 88. Which sequence correctly releases a permit feature flag to running portals?

Domain: Secure, monitor, troubleshoot Azure solutions

- A. Change the feature flag without redeploying → create the App Configuration store → add key-values with an environment label → enable refresh in the application → reference the vault secret from a key value
- B. Enable refresh in the application → create the App Configuration store → add key-values with an environment label → change the feature flag without redeploying → reference the vault secret from a key value
- C. Create the App Configuration store → add key-values with an environment label → reference the vault secret from a key value → enable refresh in the application → change the feature flag without redeploying
- D. Add key-values with an environment label → reference the vault secret from a key value → create the App Configuration store → enable refresh in the application → change the feature flag without redeploying

---

## Case study — CampusDesk

The next three questions refer to this scenario. Read the full scenario before answering; case-study items are scored individually.

### 89. A first implementation returns nearest neighbours and then hides rows the caller may not see, and the list comes back short. What is wrong?

Domain: Develop AI solutions by using Azure data management services

- A. Create an HNSW index for low-latency approximate search
- B. Retrieve nearest neighbours first and discard unauthorized rows in the application
- C. Filter on metadata columns in the same query as the vector search
- D. Query without a vector index and let PostgreSQL scan the table

### 90. A document with an unreadable encoding fails repeatedly and must be set aside for support. What should happen?

Domain: Connect to and consume Azure services

- A. Set a maximum delivery count and handle the dead-letter path
- B. Receive in receive-and-delete mode for at-most-once delivery
- C. Inspect the dead-letter queue and resubmit corrected messages
- D. Use Service Bus sessions to keep related messages ordered

### 91. A non-secret setting is stored centrally but its value must remain in the vault. What should be used?

Domain: Secure, monitor, troubleshoot Azure solutions

- A. Store the secret in Azure Key Vault and read it at runtime
- B. Reference the Key Vault secret from an App Configuration key value
- C. Store settings and feature flags in Azure App Configuration
- D. Supply configuration through App Service application settings

---

## Case study — CityPortal

The next three questions refer to this scenario. Read the full scenario before answering; case-study items are scored individually.

### 92. A pod resolves the database hostname to a public address and the connection is refused. What should be checked?

Domain: Develop containerized solutions on Azure

- A. Query container logs and Kubernetes events in Log Analytics
- B. Link the private DNS zone so the private endpoint name resolves
- C. Add readiness and liveness probes to the pod specification
- D. Test end-to-end connectivity from inside the container to each dependency

### 93. A handler must react when an uploaded file is created in storage, with no polling. What should it subscribe to?

Domain: Connect to and consume Azure services

- A. Filter the Event Grid subscription by subject or event type
- B. Define a custom event schema for the topic
- C. Rely on Event Grid retries with a dead-letter destination
- D. Subscribe to a system topic for resource events

### 94. A slow request is logged without an exception, and the team suspects a downstream call. Which query shape helps?

Domain: Secure, monitor, troubleshoot Azure solutions

- A. Project only the columns needed and filter by time first
- B. Create an alert rule on the failure rate or latency metric
- C. Aggregate with summarize and bin to see the failure rate over time
- D. Join the requests and dependencies tables on the operation ID

---

## Case study — CityWorks Permits

The next three questions refer to this scenario. Read the full scenario before answering; case-study items are scored individually.

### 95. A new OCR model must take one tenth of review traffic before it replaces the current model. What should be used?

Domain: Develop containerized solutions on Azure

- A. Rely on the horizontal pod autoscaler on CPU
- B. Stage the change in a deployment slot and swap after verification
- C. Create a new Container Apps revision and shift traffic between revisions
- D. Replicate the registry to each deployment region

### 96. Review workers must follow the number of pending scanned forms and must shrink to zero at night. What should drive replicas?

Domain: Develop containerized solutions on Azure

- A. Rely on the horizontal pod autoscaler on CPU
- B. Scale the container app on an event source with a KEDA scaler
- C. Scale only on CPU utilization without an event scaler
- D. Run the batch job in Azure Container Instances

### 97. Retrieval must return only documents the requester may see and must still return five passages. What should the query do?

Domain: Develop AI solutions by using Azure data management services

- A. Retrieve nearest neighbours first and discard unauthorized rows in the application
- B. Create an HNSW index for low-latency approximate search
- C. Filter on metadata columns in the same query as the vector search
- D. Create an IVFFlat index to save memory on a large table

---

## Case study — StateLibrary

The next three questions refer to this scenario. Read the full scenario before answering; case-study items are scored individually.

### 98. Catalog records and embeddings must be filtered by collection and language beside a vector predicate. How should the table be modeled?

Domain: Develop AI solutions by using Azure data management services

- A. Add a read replica and send all vector queries to it
- B. Increase storage throughput for index builds and bulk loads
- C. Model typed columns for filters and one vector column for the embedding
- D. Scale compute and memory to fit index size and query concurrency

### 99. A catalogue event must wait for the registry service to recover without burning delivery attempts. What should the handler do?

Domain: Connect to and consume Azure services

- A. Defer the message and retry it after the dependency recovers
- B. Receive with peek-lock and complete or abandon explicitly
- C. Inspect the dead-letter queue and resubmit corrected messages
- D. Set a maximum delivery count and handle the dead-letter path

### 100. A request loses its trace identifier the moment work is queued for OCR. What must cross the hop?

Domain: Secure, monitor, troubleshoot Azure solutions

- A. Correlate logs with the operation or trace identifier
- B. Use head or tail sampling so trace volume stays within budget
- C. Export telemetry through an OpenTelemetry collector
- D. Propagate trace context across every service and queue hop

---

## Answer key and explanations

### Question 1 — D

Answer: Build and store versioned images in Azure Container Registry. Versioned tags tie production to a reviewed build. ACR keeps tagged, versioned images next to the deployment target and supports identity-based pulls. Tagging strategy and retention still need a decision. Local study-map skill 1.1 (Container Image Lifecycle in Azure Container Registry), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure container hosting documentation: https://learn.microsoft.com/en-us/azure/container-apps/

- **A:** Incorrect for this question. ACR Tasks builds images in Azure on a commit or schedule without a local Docker host. It removes build-host drift but not image review. Why the correct answer wins: Versioned tags tie production to a reviewed build.
- **B:** Incorrect for this question. A retention policy controls storage growth and registry clutter. It does not change which image tag a deployment references. Why the correct answer wins: Versioned tags tie production to a reviewed build.
- **C:** Incorrect for this question. A floating tag removes the link between a deployed revision and a specific build, so rollback and audit become guesswork. Why the correct answer wins: Versioned tags tie production to a reviewed build.
- **D:** Correct. ACR keeps tagged, versioned images next to the deployment target and supports identity-based pulls. Tagging strategy and retention still need a decision. In this case: Versioned tags tie production to a reviewed build.

### Question 2 — D

Answer: Run image builds on demand or on a trigger with ACR Tasks. An ACR Task builds on a schedule inside Azure. ACR Tasks builds images in Azure on a commit or schedule without a local Docker host. It removes build-host drift but not image review. Local study-map skill 1.2 (Automated Image Builds with ACR Tasks), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure container hosting documentation: https://learn.microsoft.com/en-us/azure/container-apps/

- **A:** Incorrect for this question. ACR keeps tagged, versioned images next to the deployment target and supports identity-based pulls. Tagging strategy and retention still need a decision. Why the correct answer wins: An ACR Task builds on a schedule inside Azure.
- **B:** Incorrect for this question. A slot swap warms the new version before it takes production traffic and makes rollback a second swap. Slot-local settings must be marked sticky. Why the correct answer wins: An ACR Task builds on a schedule inside Azure.
- **C:** Incorrect for this question. Geo-replication reduces cross-region pull latency and gives a local copy during a regional failure. It adds cost and replication management. Why the correct answer wins: An ACR Task builds on a schedule inside Azure.
- **D:** Correct. ACR Tasks builds images in Azure on a commit or schedule without a local Docker host. It removes build-host drift but not image review. In this case: An ACR Task builds on a schedule inside Azure.

### Question 3 — D

Answer: Deploy the image to Azure App Service as a web app. App Service runs containers with managed maintenance and slots. App Service runs a container with managed patching, deployment slots, and built-in authentication options. It is not a Kubernetes control plane. Local study-map skill 1.3 (Container Deployment to Azure App Service), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure container hosting documentation: https://learn.microsoft.com/en-us/azure/container-apps/

- **A:** Incorrect for this question. Container Apps provides a managed environment, revisions, and KEDA-based scaling without cluster administration. Platform limits differ from AKS. Why the correct answer wins: App Service runs containers with managed maintenance and slots.
- **B:** Incorrect for this question. AKS gives full Kubernetes control, including custom controllers and networking. You own node pools, upgrades, and manifest hygiene. Why the correct answer wins: App Service runs containers with managed maintenance and slots.
- **C:** Incorrect for this question. Container Instances starts a single container group quickly for short tasks. It has no orchestrator-level scaling or revision model. Why the correct answer wins: App Service runs containers with managed maintenance and slots.
- **D:** Correct. App Service runs a container with managed patching, deployment slots, and built-in authentication options. It is not a Kubernetes control plane. In this case: App Service runs containers with managed maintenance and slots.

### Question 4 — A

Answer: Reference a Key Vault secret from the app configuration instead of storing it. A Key Vault reference resolves through the app identity at runtime. A Key Vault reference resolves at runtime so the secret is never written into application settings. The app identity still needs permission to read it. Local study-map skill 1.3 (Container Deployment to Azure App Service), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure container hosting documentation: https://learn.microsoft.com/en-us/azure/container-apps/

- **A:** Correct. A Key Vault reference resolves at runtime so the secret is never written into application settings. The app identity still needs permission to read it. In this case: A Key Vault reference resolves through the app identity at runtime.
- **B:** Incorrect for this question. A slot swap warms the new version before it takes production traffic and makes rollback a second swap. Slot-local settings must be marked sticky. Why the correct answer wins: A Key Vault reference resolves through the app identity at runtime.
- **C:** Incorrect for this question. App Service runs a container with managed patching, deployment slots, and built-in authentication options. It is not a Kubernetes control plane. Why the correct answer wins: A Key Vault reference resolves through the app identity at runtime.
- **D:** Incorrect for this question. Application settings become environment variables for the container and can be swapped per slot. Sensitive values should still reference a vault. Why the correct answer wins: A Key Vault reference resolves through the app identity at runtime.

### Question 5 — D

Answer: Create a new Container Apps revision and shift traffic between revisions. Revisions allow percentage traffic splitting for a canary. Revision-based traffic splitting enables canary and blue-green releases. Revision mode and scale rules must be set deliberately. Local study-map skill 1.4 (Container Apps Deployment and Revisions), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure container hosting documentation: https://learn.microsoft.com/en-us/azure/container-apps/

- **A:** Incorrect for this question. Internal ingress keeps the endpoint inside the environment virtual network. It is an exposure control, not an authorization control. Why the correct answer wins: Revisions allow percentage traffic splitting for a canary.
- **B:** Incorrect for this question. A slot swap warms the new version before it takes production traffic and makes rollback a second swap. Slot-local settings must be marked sticky. Why the correct answer wins: Revisions allow percentage traffic splitting for a canary.
- **C:** Incorrect for this question. KEDA scalers drive replica count from queue length, lag, or other event metrics, including scale to zero. Cool-down and max replicas bound the behavior. Why the correct answer wins: Revisions allow percentage traffic splitting for a canary.
- **D:** Correct. Revision-based traffic splitting enables canary and blue-green releases. Revision mode and scale rules must be set deliberately. In this case: Revisions allow percentage traffic splitting for a canary.

### Question 6 — A

Answer: Tune the scale rule cool-down period and maximum replicas. A cool-down period and a sensible maximum prevent rapid flapping. Cool-down prevents replica flapping, and a maximum replica cap bounds cost and downstream load. Both are per-rule settings. Local study-map skill 1.5 (Event-Driven Scaling with KEDA), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure container hosting documentation: https://learn.microsoft.com/en-us/azure/container-apps/

- **A:** Correct. Cool-down prevents replica flapping, and a maximum replica cap bounds cost and downstream load. Both are per-rule settings. In this case: A cool-down period and a sensible maximum prevent rapid flapping.
- **B:** Incorrect for this question. HPA adjusts replicas from resource metrics but needs metrics-server and enough node capacity. It cannot scale to zero. Why the correct answer wins: A cool-down period and a sensible maximum prevent rapid flapping.
- **C:** Incorrect for this question. KEDA scalers drive replica count from queue length, lag, or other event metrics, including scale to zero. Cool-down and max replicas bound the behavior. Why the correct answer wins: A cool-down period and a sensible maximum prevent rapid flapping.
- **D:** Incorrect for this question. A warm minimum replica removes scale-to-zero cold starts for latency-critical endpoints. It keeps paying for idle capacity. Why the correct answer wins: A cool-down period and a sensible maximum prevent rapid flapping.

### Question 7 — B

Answer: Apply a declarative Kubernetes manifest to the cluster. A manifest declares desired state and can be reapplied idempotently. A manifest declares the desired deployment, service, and probe configuration in version control. Applying it repeatedly is idempotent. Local study-map skill 1.6 (AKS Deployment with Manifests), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure container hosting documentation: https://learn.microsoft.com/en-us/azure/container-apps/

- **A:** Incorrect for this question. HPA adjusts replicas from resource metrics but needs metrics-server and enough node capacity. It cannot scale to zero. Why the correct answer wins: A manifest declares desired state and can be reapplied idempotently.
- **B:** Correct. A manifest declares the desired deployment, service, and probe configuration in version control. Applying it repeatedly is idempotent. In this case: A manifest declares desired state and can be reapplied idempotently.
- **C:** Incorrect for this question. Readiness gates traffic until the app can serve it, and liveness restarts a wedged container. Wrong thresholds cause restart loops. Why the correct answer wins: A manifest declares desired state and can be reapplied idempotently.
- **D:** Incorrect for this question. Container Instances starts a single container group quickly for short tasks. It has no orchestrator-level scaling or revision model. Why the correct answer wins: A manifest declares desired state and can be reapplied idempotently.

### Question 8 — B

Answer: Query container logs and Kubernetes events in Log Analytics. Log Analytics ingests both container logs and platform events. Container Apps and AKS surface stdout logs and platform events into a workspace for KQL analysis. Verbosity and retention cost money. Local study-map skill 1.7 (Container Logs, Events, and Connectivity), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure container hosting documentation: https://learn.microsoft.com/en-us/azure/container-apps/

- **A:** Incorrect for this question. Platform logs and metrics must be routed before they can be queried or alerted on. Retention and cost follow the workspace settings. Why the correct answer wins: Log Analytics ingests both container logs and platform events.
- **B:** Correct. Container Apps and AKS surface stdout logs and platform events into a workspace for KQL analysis. Verbosity and retention cost money. In this case: Log Analytics ingests both container logs and platform events.
- **C:** Incorrect for this question. Reaching a dependency from the pod or replica proves DNS, egress, and firewall paths together. Host-side tests can succeed while the container path fails. Why the correct answer wins: Log Analytics ingests both container logs and platform events.
- **D:** Incorrect for this question. Application Insights correlates requests, dependencies, and exceptions into end-to-end transactions. Sampling can hide rare failures. Why the correct answer wins: Log Analytics ingests both container logs and platform events.

### Question 9 — C, D

Answers: Create a new Container Apps revision and shift traffic between revisions; Set a minimum replica count above zero for the container app. Revisions enable traffic splitting, and a minimum replica count avoids cold starts. Revision-based traffic splitting enables canary and blue-green releases. Revision mode and scale rules must be set deliberately. A warm minimum replica removes scale-to-zero cold starts for latency-critical endpoints. It keeps paying for idle capacity. Local study-map skill 1.4 (Container Apps Deployment and Revisions), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure container hosting documentation: https://learn.microsoft.com/en-us/azure/container-apps/

- **A:** Incorrect for this question. Cool-down prevents replica flapping, and a maximum replica cap bounds cost and downstream load. Both are per-rule settings. Why the correct answer wins: Revisions enable traffic splitting, and a minimum replica count avoids cold starts.
- **B:** Incorrect for this question. HPA adjusts replicas from resource metrics but needs metrics-server and enough node capacity. It cannot scale to zero. Why the correct answer wins: Revisions enable traffic splitting, and a minimum replica count avoids cold starts.
- **C:** Correct. Revision-based traffic splitting enables canary and blue-green releases. Revision mode and scale rules must be set deliberately. In this case: Revisions enable traffic splitting, and a minimum replica count avoids cold starts.
- **D:** Correct. A warm minimum replica removes scale-to-zero cold starts for latency-critical endpoints. It keeps paying for idle capacity. In this case: Revisions enable traffic splitting, and a minimum replica count avoids cold starts.
- **E:** Incorrect for this question. Internal ingress keeps the endpoint inside the environment virtual network. It is an exposure control, not an authorization control. Why the correct answer wins: Revisions enable traffic splitting, and a minimum replica count avoids cold starts.

### Question 10 — C, E

Answers: Scale the container app on an event source with a KEDA scaler; Scale on the Service Bus queue length with a KEDA Azure Service Bus scaler. A KEDA scaler drives replica count from the event source, and the queue-length scaler is the suitable trigger. KEDA scalers drive replica count from queue length, lag, or other event metrics, including scale to zero. Cool-down and max replicas bound the behavior. A queue-length scaler adds replicas while work is backed up and removes them when the queue drains. Message lock duration must exceed processing time. Local study-map skill 1.5 (Event-Driven Scaling with KEDA), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure container hosting documentation: https://learn.microsoft.com/en-us/azure/container-apps/

- **A:** Incorrect for this question. CPU-based scaling reacts after work is already queued and cannot scale to zero on an empty queue. It suits steady request-driven services. Why the correct answer wins: A KEDA scaler drives replica count from the event source, and the queue-length scaler is the suitable trigger.
- **B:** Incorrect for this question. HPA adjusts replicas from resource metrics but needs metrics-server and enough node capacity. It cannot scale to zero. Why the correct answer wins: A KEDA scaler drives replica count from the event source, and the queue-length scaler is the suitable trigger.
- **C:** Correct. KEDA scalers drive replica count from queue length, lag, or other event metrics, including scale to zero. Cool-down and max replicas bound the behavior. In this case: A KEDA scaler drives replica count from the event source, and the queue-length scaler is the suitable trigger.
- **D:** Incorrect for this question. Container Instances starts a single container group quickly for short tasks. It has no orchestrator-level scaling or revision model. Why the correct answer wins: A KEDA scaler drives replica count from the event source, and the queue-length scaler is the suitable trigger.
- **E:** Correct. A queue-length scaler adds replicas while work is backed up and removes them when the queue drains. Message lock duration must exceed processing time. In this case: A KEDA scaler drives replica count from the event source, and the queue-length scaler is the suitable trigger.

### Question 11 — B

Answer: Build and push the image → deploy a new revision → shift a small traffic percentage → check metrics → promote or roll back. The image is built, then the revision is deployed, then partial traffic is shifted, and metrics decide promotion. A canary revision accepts a small share of traffic so metrics decide promotion rather than optimism. Local study-map skill 1.4 (Container Apps Deployment and Revisions), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure container hosting documentation: https://learn.microsoft.com/en-us/azure/container-apps/

- **A:** Incorrect for this question. Building after traffic is shifted means the running revision has no reviewed artifact behind it. Why the correct answer wins: The image is built, then the revision is deployed, then partial traffic is shifted, and metrics decide promotion.
- **B:** Correct. A canary revision accepts a small share of traffic so metrics decide promotion rather than optimism. In this case: The image is built, then the revision is deployed, then partial traffic is shifted, and metrics decide promotion.
- **C:** Incorrect for this question. Full traffic cannot move to a revision that does not exist yet, and the image must exist before the revision. Why the correct answer wins: The image is built, then the revision is deployed, then partial traffic is shifted, and metrics decide promotion.
- **D:** Incorrect for this question. Metrics cannot be checked before the revision serves traffic. Why the correct answer wins: The image is built, then the revision is deployed, then partial traffic is shifted, and metrics decide promotion.

### Question 12 — C

Answer: Include the partition key in the query predicate. Including the partition key keeps the read single-partition. A point or single-partition query avoids fan-out across partitions. Cross-partition queries consume more RUs and add latency. Local study-map skill 2.1 (Cosmos DB SDK Access and Queries), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Cosmos DB and PostgreSQL vector documentation: https://learn.microsoft.com/en-us/azure/cosmos-db/

- **A:** Incorrect for this question. SDK queries keep the client on the supported data plane and parameterization avoids injection and plan churn. Cross-partition queries still cost more. Why the correct answer wins: Including the partition key keeps the read single-partition.
- **B:** Incorrect for this question. Request units measure the work a query performs, so tuning the query is often cheaper than adding throughput. Monitor normalized RU consumption. Why the correct answer wins: Including the partition key keeps the read single-partition.
- **C:** Correct. A point or single-partition query avoids fan-out across partitions. Cross-partition queries consume more RUs and add latency. In this case: Including the partition key keeps the read single-partition.
- **D:** Incorrect for this question. Selective indexing cuts write RU charge and storage for unused paths. Excluded paths cannot be filtered efficiently later. Why the correct answer wins: Including the partition key keeps the read single-partition.

### Question 13 — C

Answer: Query through the Cosmos DB SDK with parameterized queries. SDK query calls keep the client supported and let connections be reused. SDK queries keep the client on the supported data plane and parameterization avoids injection and plan churn. Cross-partition queries still cost more. Local study-map skill 2.1 (Cosmos DB SDK Access and Queries), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Cosmos DB and PostgreSQL vector documentation: https://learn.microsoft.com/en-us/azure/cosmos-db/

- **A:** Incorrect for this question. Autoscale follows demand between a minimum and maximum, avoiding throttling at peak without paying for peak all day. The maximum still caps the bill. Why the correct answer wins: SDK query calls keep the client supported and let connections be reused.
- **B:** Incorrect for this question. A transactional batch applies all-or-nothing within a single partition key. It cannot span partitions and still consumes RU per operation. Why the correct answer wins: SDK query calls keep the client supported and let connections be reused.
- **C:** Correct. SDK queries keep the client on the supported data plane and parameterization avoids injection and plan churn. Cross-partition queries still cost more. In this case: SDK query calls keep the client supported and let connections be reused.
- **D:** Incorrect for this question. Leases track partition ownership so multiple processor instances share work and resume from a continuation token. Lease writes consume RUs too. Why the correct answer wins: SDK query calls keep the client supported and let connections be reused.

### Question 14 — B

Answer: Restrict the indexing policy to the paths the queries use. Restricting indexed paths reduces write cost and storage. Selective indexing cuts write RU charge and storage for unused paths. Excluded paths cannot be filtered efficiently later. Local study-map skill 2.2 (Cosmos DB Indexing Policies and Request Units), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Cosmos DB and PostgreSQL vector documentation: https://learn.microsoft.com/en-us/azure/cosmos-db/

- **A:** Incorrect for this question. Indexing everything is simple and makes ad hoc queries possible, at higher write cost and storage. It is a default, not an optimization. Why the correct answer wins: Restricting indexed paths reduces write cost and storage.
- **B:** Correct. Selective indexing cuts write RU charge and storage for unused paths. Excluded paths cannot be filtered efficiently later. In this case: Restricting indexed paths reduces write cost and storage.
- **C:** Incorrect for this question. Item TTL expires documents automatically, which controls storage growth and data retention. It does not archive the expired content. Why the correct answer wins: Restricting indexed paths reduces write cost and storage.
- **D:** Incorrect for this question. Request units measure the work a query performs, so tuning the query is often cheaper than adding throughput. Monitor normalized RU consumption. Why the correct answer wins: Restricting indexed paths reduces write cost and storage.

### Question 15 — B

Answer: Use eventual consistency to minimize read cost. Eventual consistency is the cheapest and most available option for tolerant reads. Eventual consistency is the cheapest and most available option but returns possibly stale data. It fits non-critical counters, not balances. Local study-map skill 2.3 (Cosmos DB Consistency Levels), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Cosmos DB and PostgreSQL vector documentation: https://learn.microsoft.com/en-us/azure/cosmos-db/

- **A:** Incorrect for this question. Consistency trades freshness against latency, availability, and RU cost. The level is set at the account and can be relaxed per request. Why the correct answer wins: Eventual consistency is the cheapest and most available option for tolerant reads.
- **B:** Correct. Eventual consistency is the cheapest and most available option but returns possibly stale data. It fits non-critical counters, not balances. In this case: Eventual consistency is the cheapest and most available option for tolerant reads.
- **C:** Incorrect for this question. Session consistency guarantees monotonic reads for one session and is the common default for user-facing apps. It does not promise global freshness. Why the correct answer wins: Eventual consistency is the cheapest and most available option for tolerant reads.
- **D:** Incorrect for this question. Strong consistency guarantees the latest committed write globally at the cost of higher latency and reduced availability during partitions. Why the correct answer wins: Eventual consistency is the cheapest and most available option for tolerant reads.

### Question 16 — A

Answer: Run a change feed processor to react to new and updated items. The change feed streams new items to downstream processing. The change feed delivers an ordered stream of changes per partition for downstream processing. It is not a delete feed, so deletions need a workaround. Local study-map skill 2.5 (Cosmos DB Change Feed Processing), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Cosmos DB and PostgreSQL vector documentation: https://learn.microsoft.com/en-us/azure/cosmos-db/

- **A:** Correct. The change feed delivers an ordered stream of changes per partition for downstream processing. It is not a delete feed, so deletions need a workaround. In this case: The change feed streams new items to downstream processing.
- **B:** Incorrect for this question. A transactional batch applies all-or-nothing within a single partition key. It cannot span partitions and still consumes RU per operation. Why the correct answer wins: The change feed streams new items to downstream processing.
- **C:** Incorrect for this question. A duplicate-detection window drops repeated sends within the window, which helps with at-least-once producers. The window is time-bounded. Why the correct answer wins: The change feed streams new items to downstream processing.
- **D:** Incorrect for this question. Leases track partition ownership so multiple processor instances share work and resume from a continuation token. Lease writes consume RUs too. Why the correct answer wins: The change feed streams new items to downstream processing.

### Question 17 — D

Answer: Store embeddings in PostgreSQL by using the pgvector extension. pgvector keeps vectors beside relational filter columns. pgvector keeps vectors beside relational data, so filters and joins run in one query. Index type and parameter tuning decide latency. Local study-map skill 2.6 (PostgreSQL Connection and Schema Modeling), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Cosmos DB and PostgreSQL vector documentation: https://learn.microsoft.com/en-us/azure/cosmos-db/

- **A:** Incorrect for this question. Application-side scoring works for tiny collections and tests, but it moves all data over the wire and does not scale with corpus size. Why the correct answer wins: pgvector keeps vectors beside relational filter columns.
- **B:** Incorrect for this question. Cosmos DB gives globally distributed, low-latency document access with tunable consistency. Partition key and RU planning determine the cost profile. Why the correct answer wins: pgvector keeps vectors beside relational filter columns.
- **C:** Incorrect for this question. A cache absorbs repeated reads and cuts latency for hot data. Cache keys, TTLs, and invalidation must match the freshness requirement. Why the correct answer wins: pgvector keeps vectors beside relational filter columns.
- **D:** Correct. pgvector keeps vectors beside relational data, so filters and joins run in one query. Index type and parameter tuning decide latency. In this case: pgvector keeps vectors beside relational filter columns.

### Question 18 — B

Answer: Create an IVFFlat index to save memory on a large table. IVFFlat uses clustering lists and less memory than HNSW. IVFFlat uses clustering lists and needs periodic rebuilds as data grows, but costs less memory than HNSW. Probes trade recall for speed. Local study-map skill 2.7 (pgvector Indexing and Query Latency), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Cosmos DB and PostgreSQL vector documentation: https://learn.microsoft.com/en-us/azure/cosmos-db/

- **A:** Incorrect for this question. HNSW gives fast approximate nearest-neighbour queries with a larger memory footprint and slower builds. Recall is tunable at query time. Why the correct answer wins: IVFFlat uses clustering lists and less memory than HNSW.
- **B:** Correct. IVFFlat uses clustering lists and needs periodic rebuilds as data grows, but costs less memory than HNSW. Probes trade recall for speed. In this case: IVFFlat uses clustering lists and less memory than HNSW.
- **C:** Incorrect for this question. Index creation and bulk loads are I/O heavy, and throttled storage stretches maintenance windows. Storage limits are separate from compute. Why the correct answer wins: IVFFlat uses clustering lists and less memory than HNSW.
- **D:** Incorrect for this question. An exact scan is accurate but scales linearly and burns compute. It is a baseline for measuring recall, not a production strategy. Why the correct answer wins: IVFFlat uses clustering lists and less memory than HNSW.

### Question 19 — D

Answer: Increase storage throughput for index builds and bulk loads. Index builds depend on storage throughput as well as compute. Index creation and bulk loads are I/O heavy, and throttled storage stretches maintenance windows. Storage limits are separate from compute. Local study-map skill 2.8 (PostgreSQL Compute, Memory, and Storage Sizing), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Cosmos DB and PostgreSQL vector documentation: https://learn.microsoft.com/en-us/azure/cosmos-db/

- **A:** Incorrect for this question. Vector indexes are memory-hungry, so undersized compute causes swapping and slow queries. Right-size before tuning index parameters. Why the correct answer wins: Index builds depend on storage throughput as well as compute.
- **B:** Incorrect for this question. Index builds and large sorts spill to disk when work memory is too small, stretching maintenance windows and slowing queries. Why the correct answer wins: Index builds depend on storage throughput as well as compute.
- **C:** Incorrect for this question. A bounded pool amortizes connection setup and protects the server from connection storms. Pool size must match server limits. Why the correct answer wins: Index builds depend on storage throughput as well as compute.
- **D:** Correct. Index creation and bulk loads are I/O heavy, and throttled storage stretches maintenance windows. Storage limits are separate from compute. In this case: Index builds depend on storage throughput as well as compute.

### Question 20 — A

Answer: Place a connection pooler in front of PostgreSQL for many short-lived clients. An external pooler multiplexes many clients onto fewer server connections. An external pooler multiplexes server connections for serverless or highly concurrent clients. Session-level features may be unavailable in transaction mode. Local study-map skill 2.10 (PostgreSQL Connection Optimization), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Cosmos DB and PostgreSQL vector documentation: https://learn.microsoft.com/en-us/azure/cosmos-db/

- **A:** Correct. An external pooler multiplexes server connections for serverless or highly concurrent clients. Session-level features may be unavailable in transaction mode. In this case: An external pooler multiplexes many clients onto fewer server connections.
- **B:** Incorrect for this question. Prepared statements avoid repeated planning and reduce chatty network calls. They pair well with pooling but can interact with pool modes. Why the correct answer wins: An external pooler multiplexes many clients onto fewer server connections.
- **C:** Incorrect for this question. A replica offloads read traffic but introduces replication lag, which is dangerous for freshly written evidence. It does not reduce index memory pressure. Why the correct answer wins: An external pooler multiplexes many clients onto fewer server connections.
- **D:** Incorrect for this question. A bounded pool amortizes connection setup and protects the server from connection storms. Pool size must match server limits. Why the correct answer wins: An external pooler multiplexes many clients onto fewer server connections.

### Question 21 — C

Answer: Invalidate or overwrite the cache entry when the source changes. Explicit invalidation on write removes the stale entry at once. Write-through or explicit invalidation keeps cached answers consistent with the system of record. Without it, TTL is the only bound on staleness. Local study-map skill 2.11 (Azure Managed Redis Caching and Invalidation), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Cosmos DB and PostgreSQL vector documentation: https://learn.microsoft.com/en-us/azure/cosmos-db/

- **A:** Incorrect for this question. Eviction protects memory but evicts unpredictably, so a hot key can vanish before its freshness bound is reached. It is not a substitute for TTL design. Why the correct answer wins: Explicit invalidation on write removes the stale entry at once.
- **B:** Incorrect for this question. A TTL bounds staleness and reclaims memory without a manual sweep. Too long a TTL hides source changes; too short wastes the cache. Why the correct answer wins: Explicit invalidation on write removes the stale entry at once.
- **C:** Correct. Write-through or explicit invalidation keeps cached answers consistent with the system of record. Without it, TTL is the only bound on staleness. In this case: Explicit invalidation on write removes the stale entry at once.
- **D:** Incorrect for this question. Flushing removes all cached content at once, causing a stampede to the origin and a latency cliff. Targeted invalidation is safer. Why the correct answer wins: Explicit invalidation on write removes the stale entry at once.

### Question 22 — D

Answer: Store user session state in Managed Redis with an expiry. Session state in Managed Redis survives instance changes and supports expiry. Session storage in Redis survives instance restarts and supports distributed instances. Sessions must be scoped and expiring. Local study-map skill 2.12 (Azure Managed Redis Vector Indexing), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Cosmos DB and PostgreSQL vector documentation: https://learn.microsoft.com/en-us/azure/cosmos-db/

- **A:** Incorrect for this question. Redis vector search serves low-latency similarity queries from memory. The corpus must fit the memory budget and be rebuilt on model change. Why the correct answer wins: Session state in Managed Redis survives instance changes and supports expiry.
- **B:** Incorrect for this question. A cache absorbs repeated reads and cuts latency for hot data. Cache keys, TTLs, and invalidation must match the freshness requirement. Why the correct answer wins: Session state in Managed Redis survives instance changes and supports expiry.
- **C:** Incorrect for this question. A lock can serialize work across instances, but correctness under retries still needs idempotency keys in the data store. Locks expire and can be lost. Why the correct answer wins: Session state in Managed Redis survives instance changes and supports expiry.
- **D:** Correct. Session storage in Redis survives instance restarts and supports distributed instances. Sessions must be scoped and expiring. In this case: Session state in Managed Redis survives instance changes and supports expiry.

### Question 23 — B, E

Answers: Model typed columns for filters and one vector column for the embedding; Filter on metadata columns in the same query as the vector search. Typed filter columns make the predicate efficient, and filtering in the query enforces scope. Explicit types keep filters fast and make the embedding contract clear. Storing vectors as text defeats index use. Combining a WHERE filter with the distance operator keeps retrieval inside the caller's scope and improves relevance. Index the filter columns too. Local study-map skill 2.6 (PostgreSQL Connection and Schema Modeling), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Cosmos DB and PostgreSQL vector documentation: https://learn.microsoft.com/en-us/azure/cosmos-db/

- **A:** Incorrect for this question. An exact scan is accurate but scales linearly and burns compute. It is a baseline for measuring recall, not a production strategy. Why the correct answer wins: Typed filter columns make the predicate efficient, and filtering in the query enforces scope.
- **B:** Correct. Combining a WHERE filter with the distance operator keeps retrieval inside the caller's scope and improves relevance. Index the filter columns too. In this case: Typed filter columns make the predicate efficient, and filtering in the query enforces scope.
- **C:** Incorrect for this question. Vector indexes are memory-hungry, so undersized compute causes swapping and slow queries. Right-size before tuning index parameters. Why the correct answer wins: Typed filter columns make the predicate efficient, and filtering in the query enforces scope.
- **D:** Incorrect for this question. Post-filtering can return fewer results than requested and can leak existence or counts if the filtering is careless. Push authorization into the query. Why the correct answer wins: Typed filter columns make the predicate efficient, and filtering in the query enforces scope.
- **E:** Correct. Explicit types keep filters fast and make the embedding contract clear. Storing vectors as text defeats index use. In this case: Typed filter columns make the predicate efficient, and filtering in the query enforces scope.

### Question 24 — D, E

Answers: Cache responses in Azure Managed Redis; Create a vector index in Managed Redis for similarity search. Caching serves repeated lookups, and a Redis vector index serves similarity from memory. A cache absorbs repeated reads and cuts latency for hot data. Cache keys, TTLs, and invalidation must match the freshness requirement. Redis vector search serves low-latency similarity queries from memory. The corpus must fit the memory budget and be rebuilt on model change. Local study-map skill 2.11 (Azure Managed Redis Caching and Invalidation), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Cosmos DB and PostgreSQL vector documentation: https://learn.microsoft.com/en-us/azure/cosmos-db/

- **A:** Incorrect for this question. Eviction protects memory but evicts unpredictably, so a hot key can vanish before its freshness bound is reached. It is not a substitute for TTL design. Why the correct answer wins: Caching serves repeated lookups, and a Redis vector index serves similarity from memory.
- **B:** Incorrect for this question. A lock can serialize work across instances, but correctness under retries still needs idempotency keys in the data store. Locks expire and can be lost. Why the correct answer wins: Caching serves repeated lookups, and a Redis vector index serves similarity from memory.
- **C:** Incorrect for this question. A TTL bounds staleness and reclaims memory without a manual sweep. Too long a TTL hides source changes; too short wastes the cache. Why the correct answer wins: Caching serves repeated lookups, and a Redis vector index serves similarity from memory.
- **D:** Correct. Redis vector search serves low-latency similarity queries from memory. The corpus must fit the memory budget and be rebuilt on model change. In this case: Caching serves repeated lookups, and a Redis vector index serves similarity from memory.
- **E:** Correct. A cache absorbs repeated reads and cuts latency for hot data. Cache keys, TTLs, and invalidation must match the freshness requirement. In this case: Caching serves repeated lookups, and a Redis vector index serves similarity from memory.

### Question 25 — B

Answer: Create the vector extension → create the table with a vector column → build the index → query nearest neighbours with a distance operator. The extension must be installed, the table created, the index built, and only then is the query efficient. The extension and typed column must exist before an index can be built, and the index before the query is efficient. Local study-map skill 2.7 (pgvector Indexing and Query Latency), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Cosmos DB and PostgreSQL vector documentation: https://learn.microsoft.com/en-us/azure/cosmos-db/

- **A:** Incorrect for this question. An index cannot be built before the extension and the table exist. Why the correct answer wins: The extension must be installed, the table created, the index built, and only then is the query efficient.
- **B:** Correct. The extension and typed column must exist before an index can be built, and the index before the query is efficient. In this case: The extension must be installed, the table created, the index built, and only then is the query efficient.
- **C:** Incorrect for this question. Querying before the schema exists cannot succeed, and the index cannot precede the table. Why the correct answer wins: The extension must be installed, the table created, the index built, and only then is the query efficient.
- **D:** Incorrect for this question. The extension is required for the vector type, and the query should follow index creation for usable latency. Why the correct answer wins: The extension must be installed, the table created, the index built, and only then is the query efficient.

### Question 26 — A

Answer: Queue the work on a Service Bus queue and process it with a worker. A queue with peek-lock gives at-least-once processing with recovery. A queue decouples producers from a single consumer group and smooths bursts. Delivery semantics depend on receive mode and completion. Local study-map skill 3.1 (Service Bus Queues and Sessions), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure messaging and Functions documentation: https://learn.microsoft.com/en-us/azure/service-bus-messaging/

- **A:** Correct. A queue decouples producers from a single consumer group and smooths bursts. Delivery semantics depend on receive mode and completion. In this case: A queue with peek-lock gives at-least-once processing with recovery.
- **B:** Incorrect for this question. Event Hubs ingests high-volume ordered streams with partitions and consumer groups. It is a streaming log, not a task queue. Why the correct answer wins: A queue with peek-lock gives at-least-once processing with recovery.
- **C:** Incorrect for this question. Queue Storage is simple and cheap for large backlogs with at-least-once delivery. It lacks topics, sessions, and scheduled messages. Why the correct answer wins: A queue with peek-lock gives at-least-once processing with recovery.
- **D:** Incorrect for this question. Topics fan out one message to independent subscribers, each with its own filter and dead-letter queue. Subscribers process at their own pace. Why the correct answer wins: A queue with peek-lock gives at-least-once processing with recovery.

### Question 27 — C

Answer: Publish to a Service Bus topic with multiple subscriptions. A topic with separate subscriptions fans out the event. Topics fan out one message to independent subscribers, each with its own filter and dead-letter queue. Subscribers process at their own pace. Local study-map skill 3.2 (Service Bus Topics, Subscriptions, and Filters), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure messaging and Functions documentation: https://learn.microsoft.com/en-us/azure/service-bus-messaging/

- **A:** Incorrect for this question. Queue Storage is simple and cheap for large backlogs with at-least-once delivery. It lacks topics, sessions, and scheduled messages. Why the correct answer wins: A topic with separate subscriptions fans out the event.
- **B:** Incorrect for this question. A queue decouples producers from a single consumer group and smooths bursts. Delivery semantics depend on receive mode and completion. Why the correct answer wins: A topic with separate subscriptions fans out the event.
- **C:** Correct. Topics fan out one message to independent subscribers, each with its own filter and dead-letter queue. Subscribers process at their own pace. In this case: A topic with separate subscriptions fans out the event.
- **D:** Incorrect for this question. A custom schema fits domain events that are not resource lifecycle notifications. Consumers must version the schema contract. Why the correct answer wins: A topic with separate subscriptions fans out the event.

### Question 28 — B

Answer: Make the handler idempotent by using a message or business key. An idempotency key in the case store makes a replay a no-op. At-least-once delivery means duplicates will happen, so the write must tolerate replay. A stored key makes the retry safe. Local study-map skill 3.3 (Service Bus Dead-Lettering and Retries), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure messaging and Functions documentation: https://learn.microsoft.com/en-us/azure/service-bus-messaging/

- **A:** Incorrect for this question. Dead-lettering preserves poison messages for diagnosis instead of losing them. Resubmission needs a fix and an idempotent handler. Why the correct answer wins: An idempotency key in the case store makes a replay a no-op.
- **B:** Correct. At-least-once delivery means duplicates will happen, so the write must tolerate replay. A stored key makes the retry safe. In this case: An idempotency key in the case store makes a replay a no-op.
- **C:** Incorrect for this question. A delivery cap stops infinite retries of a failing message and moves it to the dead-letter queue. The cap must exceed legitimate transient retries. Why the correct answer wins: An idempotency key in the case store makes a replay a no-op.
- **D:** Incorrect for this question. A duplicate-detection window drops repeated sends within the window, which helps with at-least-once producers. The window is time-bounded. Why the correct answer wins: An idempotency key in the case store makes a replay a no-op.

### Question 29 — B

Answer: Rely on Event Grid retries with a dead-letter destination. Event Grid retries and can dead-letter events that never succeed. Event Grid retries failed deliveries with backoff and can store undeliverable events. Handlers must still be idempotent. Local study-map skill 3.4 (Event Grid Filters, Custom Events, and Retries), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure messaging and Functions documentation: https://learn.microsoft.com/en-us/azure/service-bus-messaging/

- **A:** Incorrect for this question. A custom schema fits domain events that are not resource lifecycle notifications. Consumers must version the schema contract. Why the correct answer wins: Event Grid retries and can dead-letter events that never succeed.
- **B:** Correct. Event Grid retries failed deliveries with backoff and can store undeliverable events. Handlers must still be idempotent. In this case: Event Grid retries and can dead-letter events that never succeed.
- **C:** Incorrect for this question. Subject and event-type filters keep handlers focused and reduce cost. Filters are evaluated on event metadata, not payload body. Why the correct answer wins: Event Grid retries and can dead-letter events that never succeed.
- **D:** Incorrect for this question. Identity-based delivery removes a shared key from the subscription. The receiver still validates the caller and payload. Why the correct answer wins: Event Grid retries and can dead-letter events that never succeed.

### Question 30 — B

Answer: Bind a queue or event trigger to the function. A queue trigger starts the function and manages receives. A trigger starts the function when work arrives and handles the receive loop for you. Poison-message behavior is configured in host settings. Local study-map skill 3.5 (Azure Functions Triggers and Bindings), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure messaging and Functions documentation: https://learn.microsoft.com/en-us/azure/service-bus-messaging/

- **A:** Incorrect for this question. An HTTP trigger gives a synchronous API endpoint with route and authorization configuration. Long-running work should hand off to a queue. Why the correct answer wins: A queue trigger starts the function and manages receives.
- **B:** Correct. A trigger starts the function when work arrives and handles the receive loop for you. Poison-message behavior is configured in host settings. In this case: A queue trigger starts the function and manages receives.
- **C:** Incorrect for this question. Bindings reduce boilerplate for common inputs and outputs and are configured declaratively. Complex operations still need the SDK. Why the correct answer wins: A queue trigger starts the function and manages receives.
- **D:** Incorrect for this question. Durable Functions provides orchestrations, activities, timers, and retries with checkpointed state. Orchestrator code must stay deterministic. Why the correct answer wins: A queue trigger starts the function and manages receives.

### Question 31 — D

Answer: Host the function app on the consumption plan. Consumption bills per execution and scales to demand. Consumption bills per execution and scales automatically, with cold starts and a timeout ceiling. It fits spiky, short work. Local study-map skill 3.6 (Function App Configuration and Deployment), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure messaging and Functions documentation: https://learn.microsoft.com/en-us/azure/service-bus-messaging/

- **A:** Incorrect for this question. A staging slot lets a new build warm up and be validated before the swap. Slot settings that must not move are marked sticky. Why the correct answer wins: Consumption bills per execution and scales to demand.
- **B:** Incorrect for this question. Durable Functions provides orchestrations, activities, timers, and retries with checkpointed state. Orchestrator code must stay deterministic. Why the correct answer wins: Consumption bills per execution and scales to demand.
- **C:** Incorrect for this question. A premium plan reduces cold starts and supports virtual network integration and longer timeouts. It costs more than consumption. Why the correct answer wins: Consumption bills per execution and scales to demand.
- **D:** Correct. Consumption bills per execution and scales automatically, with cold starts and a timeout ceiling. It fits spiky, short work. In this case: Consumption bills per execution and scales to demand.

### Question 32 — C

Answer: Deploy the function app through a CI pipeline with app settings applied. Pipeline deployment with Key Vault references keeps code and configuration versioned without embedding secrets. Pipeline deployment keeps code and configuration versioned together and repeatable. Secrets belong in a vault reference, not in the pipeline file. Local study-map skill 3.6 (Function App Configuration and Deployment), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure messaging and Functions documentation: https://learn.microsoft.com/en-us/azure/service-bus-messaging/

- **A:** Incorrect for this question. A premium plan reduces cold starts and supports virtual network integration and longer timeouts. It costs more than consumption. Why the correct answer wins: Pipeline deployment with Key Vault references keeps code and configuration versioned without embedding secrets.
- **B:** Incorrect for this question. Durable Functions provides orchestrations, activities, timers, and retries with checkpointed state. Orchestrator code must stay deterministic. Why the correct answer wins: Pipeline deployment with Key Vault references keeps code and configuration versioned without embedding secrets.
- **C:** Correct. Pipeline deployment keeps code and configuration versioned together and repeatable. Secrets belong in a vault reference, not in the pipeline file. In this case: Pipeline deployment with Key Vault references keeps code and configuration versioned without embedding secrets.
- **D:** Incorrect for this question. A staging slot lets a new build warm up and be validated before the swap. Slot settings that must not move are marked sticky. Why the correct answer wins: Pipeline deployment with Key Vault references keeps code and configuration versioned without embedding secrets.

### Question 33 — C, D

Answers: Inspect the dead-letter queue and resubmit corrected messages; Set a maximum delivery count and handle the dead-letter path. Dead-lettering preserves the message, and a delivery cap bounds retries. Dead-lettering preserves poison messages for diagnosis instead of losing them. Resubmission needs a fix and an idempotent handler. A delivery cap stops infinite retries of a failing message and moves it to the dead-letter queue. The cap must exceed legitimate transient retries. Local study-map skill 3.3 (Service Bus Dead-Lettering and Retries), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure messaging and Functions documentation: https://learn.microsoft.com/en-us/azure/service-bus-messaging/

- **A:** Incorrect for this question. Receive-and-delete removes the message on delivery, so a crash loses work silently. It suits telemetry, not payments. Why the correct answer wins: Dead-lettering preserves the message, and a delivery cap bounds retries.
- **B:** Incorrect for this question. Sessions give ordered, exclusive processing per session ID across competing consumers. They require session-aware senders and receivers. Why the correct answer wins: Dead-lettering preserves the message, and a delivery cap bounds retries.
- **C:** Correct. Dead-lettering preserves poison messages for diagnosis instead of losing them. Resubmission needs a fix and an idempotent handler. In this case: Dead-lettering preserves the message, and a delivery cap bounds retries.
- **D:** Correct. A delivery cap stops infinite retries of a failing message and moves it to the dead-letter queue. The cap must exceed legitimate transient retries. In this case: Dead-lettering preserves the message, and a delivery cap bounds retries.
- **E:** Incorrect for this question. A duplicate-detection window drops repeated sends within the window, which helps with at-least-once producers. The window is time-bounded. Why the correct answer wins: Dead-lettering preserves the message, and a delivery cap bounds retries.

### Question 34 — D, E

Answers: Define a custom event schema for the topic; Filter the Event Grid subscription by subject or event type. A custom event schema carries the payload, and a subscription filter routes it. A custom schema fits domain events that are not resource lifecycle notifications. Consumers must version the schema contract. Subject and event-type filters keep handlers focused and reduce cost. Filters are evaluated on event metadata, not payload body. Local study-map skill 3.4 (Event Grid Filters, Custom Events, and Retries), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure messaging and Functions documentation: https://learn.microsoft.com/en-us/azure/service-bus-messaging/

- **A:** Incorrect for this question. Subscription filters route only matching messages to a handler, reducing wasted processing. Filter evaluation happens broker-side on message properties. Why the correct answer wins: A custom event schema carries the payload, and a subscription filter routes it.
- **B:** Incorrect for this question. Identity-based delivery removes a shared key from the subscription. The receiver still validates the caller and payload. Why the correct answer wins: A custom event schema carries the payload, and a subscription filter routes it.
- **C:** Incorrect for this question. Event Grid retries failed deliveries with backoff and can store undeliverable events. Handlers must still be idempotent. Why the correct answer wins: A custom event schema carries the payload, and a subscription filter routes it.
- **D:** Correct. A custom schema fits domain events that are not resource lifecycle notifications. Consumers must version the schema contract. In this case: A custom event schema carries the payload, and a subscription filter routes it.
- **E:** Correct. Subject and event-type filters keep handlers focused and reduce cost. Filters are evaluated on event metadata, not payload body. In this case: A custom event schema carries the payload, and a subscription filter routes it.

### Question 35 — C

Answer: Publish the message → receive with peek-lock → process the work → complete the message → dead-letter after the delivery limit. The message is received, processed, completed, and dead-lettered only after the delivery limit is exhausted. Peek-lock keeps the message until the handler succeeds, and only repeated failures should dead-letter it. Local study-map skill 3.1 (Service Bus Queues and Sessions), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure messaging and Functions documentation: https://learn.microsoft.com/en-us/azure/service-bus-messaging/

- **A:** Incorrect for this question. The message cannot be received before it is published, and completion must follow processing. Why the correct answer wins: The message is received, processed, completed, and dead-lettered only after the delivery limit is exhausted.
- **B:** Incorrect for this question. Completing a message before processing discards the work and defeats at-least-once delivery. Why the correct answer wins: The message is received, processed, completed, and dead-lettered only after the delivery limit is exhausted.
- **C:** Correct. Peek-lock keeps the message until the handler succeeds, and only repeated failures should dead-letter it. In this case: The message is received, processed, completed, and dead-lettered only after the delivery limit is exhausted.
- **D:** Incorrect for this question. Work cannot be processed before the message is published and received. Why the correct answer wins: The message is received, processed, completed, and dead-lettered only after the delivery limit is exhausted.

### Question 36 — A

Answer: Enable purge protection and soft delete on the vault. Soft delete with purge protection prevents permanent loss. Soft delete and purge protection stop accidental or malicious permanent loss of secrets. They also constrain how names can be reused. Local study-map skill 4.1 (Key Vault Secret Storage, Rotation, and Retrieval), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Key Vault, App Configuration, and Monitor documentation: https://learn.microsoft.com/en-us/azure/azure-monitor/

- **A:** Correct. Soft delete and purge protection stop accidental or malicious permanent loss of secrets. They also constrain how names can be reused. In this case: Soft delete with purge protection prevents permanent loss.
- **B:** Incorrect for this question. Pinning a version makes a rotation invisible to the app until it is redeployed, which is useful for break-glass and dangerous for routine rotation. Why the correct answer wins: Soft delete with purge protection prevents permanent loss.
- **C:** Incorrect for this question. A vault centralizes secret storage with access control and audit. Retrieval should use an identity, not a copied credential. Why the correct answer wins: Soft delete with purge protection prevents permanent loss.
- **D:** Incorrect for this question. A scoped role grants only the operations the app performs and limits blast radius. Prefer built-in roles over broad contributor grants. Why the correct answer wins: Soft delete with purge protection prevents permanent loss.

### Question 37 — A

Answer: Rotate the secret on a schedule and let apps resolve the current version. Rotation plus current-version reads keeps the app working across a change. Rotation limits the value of a leaked secret, but callers must read the latest version rather than caching an old one forever. Local study-map skill 4.1 (Key Vault Secret Storage, Rotation, and Retrieval), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Key Vault, App Configuration, and Monitor documentation: https://learn.microsoft.com/en-us/azure/azure-monitor/

- **A:** Correct. Rotation limits the value of a leaked secret, but callers must read the latest version rather than caching an old one forever. In this case: Rotation plus current-version reads keeps the app working across a change.
- **B:** Incorrect for this question. Pinning a version makes a rotation invisible to the app until it is redeployed, which is useful for break-glass and dangerous for routine rotation. Why the correct answer wins: Rotation plus current-version reads keeps the app working across a change.
- **C:** Incorrect for this question. Vault access is a separate authorization decision from the app identity. Without a data-plane role or policy the reference fails at runtime. Why the correct answer wins: Rotation plus current-version reads keeps the app working across a change.
- **D:** Incorrect for this question. Application settings become environment variables for the container and can be swapped per slot. Sensitive values should still reference a vault. Why the correct answer wins: Rotation plus current-version reads keeps the app working across a change.

### Question 38 — B

Answer: Use App Configuration labels to separate environments. Labels separate environment values under the same keys. Labels keep dev, test, and prod values in one store with one key schema. A misconfigured label selector silently serves the wrong values. Local study-map skill 4.2 (App Configuration Settings and Feature Flags), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Key Vault, App Configuration, and Monitor documentation: https://learn.microsoft.com/en-us/azure/azure-monitor/

- **A:** Incorrect for this question. A Key Vault reference keeps non-secret settings in App Configuration while the value stays in the vault. The app identity needs both sets of permissions. Why the correct answer wins: Labels separate environment values under the same keys.
- **B:** Correct. Labels keep dev, test, and prod values in one store with one key schema. A misconfigured label selector silently serves the wrong values. In this case: Labels separate environment values under the same keys.
- **C:** Incorrect for this question. Pinning a version makes a rotation invisible to the app until it is redeployed, which is useful for break-glass and dangerous for routine rotation. Why the correct answer wins: Labels separate environment values under the same keys.
- **D:** Incorrect for this question. Sentinel-key or polling refresh lets a running app pick up new settings. Refresh intervals trade responsiveness against request volume. Why the correct answer wins: Labels separate environment values under the same keys.

### Question 39 — D

Answer: Export telemetry through an OpenTelemetry collector. An OpenTelemetry collector centralizes export and routing. A collector batches, filters, and routes telemetry, and decouples app configuration from the backend. It is another component to run and monitor. Local study-map skill 4.3 (Distributed Tracing with OpenTelemetry), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Key Vault, App Configuration, and Monitor documentation: https://learn.microsoft.com/en-us/azure/azure-monitor/

- **A:** Incorrect for this question. OpenTelemetry emits vendor-neutral traces, metrics, and logs with context propagation. Exporters and sampling decide what reaches the backend. Why the correct answer wins: An OpenTelemetry collector centralizes export and routing.
- **B:** Incorrect for this question. Sampling keeps telemetry cost bounded, but aggressive sampling can hide rare failures. Tail sampling can retain errors preferentially. Why the correct answer wins: An OpenTelemetry collector centralizes export and routing.
- **C:** Incorrect for this question. Propagation stitches one trace across HTTP, messaging, and Functions so the whole path is visible. Missing propagation breaks the trace at that hop. Why the correct answer wins: An OpenTelemetry collector centralizes export and routing.
- **D:** Correct. A collector batches, filters, and routes telemetry, and decouples app configuration from the backend. It is another component to run and monitor. In this case: An OpenTelemetry collector centralizes export and routing.

### Question 40 — B

Answer: Reach the data service through a private endpoint. A private endpoint with public access disabled restricts the path to the workload network. A private endpoint keeps traffic on the virtual network and removes public exposure. DNS resolution must be wired to the private zone. Local study-map skill 4.5 (Identity-Based Access for Application Services), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Key Vault, App Configuration, and Monitor documentation: https://learn.microsoft.com/en-us/azure/azure-monitor/

- **A:** Incorrect for this question. A managed identity issues tokens from the platform, removing secret distribution from the app. Role assignment still scopes what it can reach. Why the correct answer wins: A private endpoint with public access disabled restricts the path to the workload network.
- **B:** Correct. A private endpoint keeps traffic on the virtual network and removes public exposure. DNS resolution must be wired to the private zone. In this case: A private endpoint with public access disabled restricts the path to the workload network.
- **C:** Incorrect for this question. Platform logs and metrics must be routed before they can be queried or alerted on. Retention and cost follow the workspace settings. Why the correct answer wins: A private endpoint with public access disabled restricts the path to the workload network.
- **D:** Incorrect for this question. A scoped role grants only the operations the app performs and limits blast radius. Prefer built-in roles over broad contributor grants. Why the correct answer wins: A private endpoint with public access disabled restricts the path to the workload network.

### Question 41 — B

Answer: Authenticate with a managed identity instead of a stored key. A managed identity provides tokens from the platform. A managed identity issues tokens from the platform, removing secret distribution from the app. Role assignment still scopes what it can reach. Local study-map skill 4.5 (Identity-Based Access for Application Services), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Key Vault, App Configuration, and Monitor documentation: https://learn.microsoft.com/en-us/azure/azure-monitor/

- **A:** Incorrect for this question. Application settings become environment variables for the container and can be swapped per slot. Sensitive values should still reference a vault. Why the correct answer wins: A managed identity provides tokens from the platform.
- **B:** Correct. A managed identity issues tokens from the platform, removing secret distribution from the app. Role assignment still scopes what it can reach. In this case: A managed identity provides tokens from the platform.
- **C:** Incorrect for this question. A scoped role grants only the operations the app performs and limits blast radius. Prefer built-in roles over broad contributor grants. Why the correct answer wins: A managed identity provides tokens from the platform.
- **D:** Incorrect for this question. A vault centralizes secret storage with access control and audit. Retrieval should use an identity, not a copied credential. Why the correct answer wins: A managed identity provides tokens from the platform.

### Question 42 — A, B

Answers: Instrument the service with the OpenTelemetry SDK; Propagate trace context across every service and queue hop. Instrumentation creates spans, and context propagation keeps the trace connected across hops. OpenTelemetry emits vendor-neutral traces, metrics, and logs with context propagation. Exporters and sampling decide what reaches the backend. Propagation stitches one trace across HTTP, messaging, and Functions so the whole path is visible. Missing propagation breaks the trace at that hop. Local study-map skill 4.3 (Distributed Tracing with OpenTelemetry), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Key Vault, App Configuration, and Monitor documentation: https://learn.microsoft.com/en-us/azure/azure-monitor/

- **A:** Correct. Propagation stitches one trace across HTTP, messaging, and Functions so the whole path is visible. Missing propagation breaks the trace at that hop. In this case: Instrumentation creates spans, and context propagation keeps the trace connected across hops.
- **B:** Correct. OpenTelemetry emits vendor-neutral traces, metrics, and logs with context propagation. Exporters and sampling decide what reaches the backend. In this case: Instrumentation creates spans, and context propagation keeps the trace connected across hops.
- **C:** Incorrect for this question. KQL filters, projects, and aggregates log and metric tables in Log Analytics. Start narrow with a time range and a request ID. Why the correct answer wins: Instrumentation creates spans, and context propagation keeps the trace connected across hops.
- **D:** Incorrect for this question. A collector batches, filters, and routes telemetry, and decouples app configuration from the backend. It is another component to run and monitor. Why the correct answer wins: Instrumentation creates spans, and context propagation keeps the trace connected across hops.
- **E:** Incorrect for this question. Sampling keeps telemetry cost bounded, but aggressive sampling can hide rare failures. Tail sampling can retain errors preferentially. Why the correct answer wins: Instrumentation creates spans, and context propagation keeps the trace connected across hops.

### Question 43 — A, D

Answers: Project only the columns needed and filter by time first; Alert on platform metrics rather than only on log queries. Filtering early and projecting fewer columns reduces scanned data, and platform metric alerts are fast and cheap. Reducing columns and rows early lowers query cost and latency. Broad queries over long ranges are the usual cause of slow KQL. Platform metrics are cheap and near-real-time, so they suit latency and failure-rate alerts. Log-based alerts add latency and query cost. Local study-map skill 4.4 (KQL Queries for Logs and Metrics), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Key Vault, App Configuration, and Monitor documentation: https://learn.microsoft.com/en-us/azure/azure-monitor/

- **A:** Correct. Reducing columns and rows early lowers query cost and latency. Broad queries over long ranges are the usual cause of slow KQL. In this case: Filtering early and projecting fewer columns reduces scanned data, and platform metric alerts are fast and cheap.
- **B:** Incorrect for this question. An alert turns a threshold breach into a notification or action. Thresholds need a baseline, or the alert is noise. Why the correct answer wins: Filtering early and projecting fewer columns reduces scanned data, and platform metric alerts are fast and cheap.
- **C:** Incorrect for this question. Time-binned aggregation reveals the shape of an incident: a step change, a ramp, or a periodic spike. Averages alone hide short outages. Why the correct answer wins: Filtering early and projecting fewer columns reduces scanned data, and platform metric alerts are fast and cheap.
- **D:** Correct. Platform metrics are cheap and near-real-time, so they suit latency and failure-rate alerts. Log-based alerts add latency and query cost. In this case: Filtering early and projecting fewer columns reduces scanned data, and platform metric alerts are fast and cheap.
- **E:** Incorrect for this question. Precomputed results avoid recomputing expensive aggregations on every dashboard refresh. The trade-off is storage and freshness lag. Why the correct answer wins: Filtering early and projecting fewer columns reduces scanned data, and platform metric alerts are fast and cheap.

### Question 44 — A

Answer: Store the secret in Key Vault → grant the app identity access → reference the secret from the app → rotate the secret → the app reads the new version. Store the secret, grant access, reference it from the app, rotate it, and read the current version. Access must be granted before the reference resolves, and the app must read the current version after rotation. Local study-map skill 4.1 (Key Vault Secret Storage, Rotation, and Retrieval), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Key Vault, App Configuration, and Monitor documentation: https://learn.microsoft.com/en-us/azure/azure-monitor/

- **A:** Correct. Access must be granted before the reference resolves, and the app must read the current version after rotation. In this case: Store the secret, grant access, reference it from the app, rotate it, and read the current version.
- **B:** Incorrect for this question. A reference cannot resolve before the secret and the access grant exist. Why the correct answer wins: Store the secret, grant access, reference it from the app, rotate it, and read the current version.
- **C:** Incorrect for this question. Access can be granted first, but rotation cannot precede storing the secret. Why the correct answer wins: Store the secret, grant access, reference it from the app, rotate it, and read the current version.
- **D:** Incorrect for this question. There is nothing to rotate or reference before the secret is stored. Why the correct answer wins: Store the secret, grant access, reference it from the app, rotate it, and read the current version.

### Question 45 — A

Answer: Deploy the image by digest instead of a mutable tag. A digest identifies immutable content, so an auditor can prove which bytes ran for a given decision. A digest identifies immutable content, so the same bytes run in every environment. A tag can be reassigned later and silently change what deploys. Local study-map skill 1.1 (Container Image Lifecycle in Azure Container Registry), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure container hosting documentation: https://learn.microsoft.com/en-us/azure/container-apps/

- **A:** Correct. A digest identifies immutable content, so the same bytes run in every environment. A tag can be reassigned later and silently change what deploys. In this case: A digest identifies immutable content, so an auditor can prove which bytes ran for a given decision.
- **B:** Incorrect for this question. A slot swap warms the new version before it takes production traffic and makes rollback a second swap. Slot-local settings must be marked sticky. Why the correct answer wins: A digest identifies immutable content, so an auditor can prove which bytes ran for a given decision.
- **C:** Incorrect for this question. A floating tag removes the link between a deployed revision and a specific build, so rollback and audit become guesswork. Why the correct answer wins: A digest identifies immutable content, so an auditor can prove which bytes ran for a given decision.
- **D:** Incorrect for this question. A retention policy controls storage growth and registry clutter. It does not change which image tag a deployment references. Why the correct answer wins: A digest identifies immutable content, so an auditor can prove which bytes ran for a given decision.

### Question 46 — C

Answer: Run image builds on demand or on a trigger with ACR Tasks. ACR Tasks runs the build inside Azure on a schedule, so no build server needs patching or network access. ACR Tasks builds images in Azure on a commit or schedule without a local Docker host. It removes build-host drift but not image review. Local study-map skill 1.2 (Automated Image Builds with ACR Tasks), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure container hosting documentation: https://learn.microsoft.com/en-us/azure/container-apps/

- **A:** Incorrect for this question. AKS gives full Kubernetes control, including custom controllers and networking. You own node pools, upgrades, and manifest hygiene. Why the correct answer wins: ACR Tasks runs the build inside Azure on a schedule, so no build server needs patching or network access.
- **B:** Incorrect for this question. Functions runs small event-driven code without managing a host. Execution limits and cold starts depend on the hosting plan. Why the correct answer wins: ACR Tasks runs the build inside Azure on a schedule, so no build server needs patching or network access.
- **C:** Correct. ACR Tasks builds images in Azure on a commit or schedule without a local Docker host. It removes build-host drift but not image review. In this case: ACR Tasks runs the build inside Azure on a schedule, so no build server needs patching or network access.
- **D:** Incorrect for this question. ACR keeps tagged, versioned images next to the deployment target and supports identity-based pulls. Tagging strategy and retention still need a decision. Why the correct answer wins: ACR Tasks runs the build inside Azure on a schedule, so no build server needs patching or network access.

### Question 47 — D

Answer: Supply configuration through App Service application settings. Application settings become environment variables per slot, so a fee table change does not require a rebuild. Application settings become environment variables for the container and can be swapped per slot. Sensitive values should still reference a vault. Local study-map skill 1.3 (Container Deployment to Azure App Service), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure container hosting documentation: https://learn.microsoft.com/en-us/azure/container-apps/

- **A:** Incorrect for this question. A ConfigMap injects settings as environment variables or mounted files without rebuilding the image. Secrets still belong in Key Vault, not in a ConfigMap. Why the correct answer wins: Application settings become environment variables per slot, so a fee table change does not require a rebuild.
- **B:** Incorrect for this question. App Configuration separates configuration from code and supports labels, feature flags, and Key Vault references. Change still needs a refresh strategy. Why the correct answer wins: Application settings become environment variables per slot, so a fee table change does not require a rebuild.
- **C:** Incorrect for this question. Pinning a version makes a rotation invisible to the app until it is redeployed, which is useful for break-glass and dangerous for routine rotation. Why the correct answer wins: Application settings become environment variables per slot, so a fee table change does not require a rebuild.
- **D:** Correct. Application settings become environment variables for the container and can be swapped per slot. Sensitive values should still reference a vault. In this case: Application settings become environment variables per slot, so a fee table change does not require a rebuild.

### Question 48 — B

Answer: Reference a Key Vault secret from the app configuration instead of storing it. A Key Vault reference resolves the secret at runtime through the app identity, so no value is stored in settings. A Key Vault reference resolves at runtime so the secret is never written into application settings. The app identity still needs permission to read it. Local study-map skill 1.3 (Container Deployment to Azure App Service), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure container hosting documentation: https://learn.microsoft.com/en-us/azure/container-apps/

- **A:** Incorrect for this question. Application settings become environment variables for the container and can be swapped per slot. Sensitive values should still reference a vault. Why the correct answer wins: A Key Vault reference resolves the secret at runtime through the app identity, so no value is stored in settings.
- **B:** Correct. A Key Vault reference resolves at runtime so the secret is never written into application settings. The app identity still needs permission to read it. In this case: A Key Vault reference resolves the secret at runtime through the app identity, so no value is stored in settings.
- **C:** Incorrect for this question. A ConfigMap injects settings as environment variables or mounted files without rebuilding the image. Secrets still belong in Key Vault, not in a ConfigMap. Why the correct answer wins: A Key Vault reference resolves the secret at runtime through the app identity, so no value is stored in settings.
- **D:** Incorrect for this question. Pinning a version makes a rotation invisible to the app until it is redeployed, which is useful for break-glass and dangerous for routine rotation. Why the correct answer wins: A Key Vault reference resolves the secret at runtime through the app identity, so no value is stored in settings.

### Question 49 — D

Answer: Deploy the image to Azure App Service as a web app. App Service runs one container per app with slots and managed patching and no control plane to maintain. App Service runs a container with managed patching, deployment slots, and built-in authentication options. It is not a Kubernetes control plane. Local study-map skill 1.3 (Container Deployment to Azure App Service), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure container hosting documentation: https://learn.microsoft.com/en-us/azure/container-apps/

- **A:** Incorrect for this question. Container Instances starts a single container group quickly for short tasks. It has no orchestrator-level scaling or revision model. Why the correct answer wins: App Service runs one container per app with slots and managed patching and no control plane to maintain.
- **B:** Incorrect for this question. Container Apps provides a managed environment, revisions, and KEDA-based scaling without cluster administration. Platform limits differ from AKS. Why the correct answer wins: App Service runs one container per app with slots and managed patching and no control plane to maintain.
- **C:** Incorrect for this question. AKS gives full Kubernetes control, including custom controllers and networking. You own node pools, upgrades, and manifest hygiene. Why the correct answer wins: App Service runs one container per app with slots and managed patching and no control plane to maintain.
- **D:** Correct. App Service runs a container with managed patching, deployment slots, and built-in authentication options. It is not a Kubernetes control plane. In this case: App Service runs one container per app with slots and managed patching and no control plane to maintain.

### Question 50 — B

Answer: Deploy the service to Azure Container Apps. Container Apps provides revisions and scale-to-zero without exposing a control plane to the team. Container Apps provides a managed environment, revisions, and KEDA-based scaling without cluster administration. Platform limits differ from AKS. Local study-map skill 1.4 (Container Apps Deployment and Revisions), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure container hosting documentation: https://learn.microsoft.com/en-us/azure/container-apps/

- **A:** Incorrect for this question. AKS gives full Kubernetes control, including custom controllers and networking. You own node pools, upgrades, and manifest hygiene. Why the correct answer wins: Container Apps provides revisions and scale-to-zero without exposing a control plane to the team.
- **B:** Correct. Container Apps provides a managed environment, revisions, and KEDA-based scaling without cluster administration. Platform limits differ from AKS. In this case: Container Apps provides revisions and scale-to-zero without exposing a control plane to the team.
- **C:** Incorrect for this question. Container Instances starts a single container group quickly for short tasks. It has no orchestrator-level scaling or revision model. Why the correct answer wins: Container Apps provides revisions and scale-to-zero without exposing a control plane to the team.
- **D:** Incorrect for this question. App Service runs a container with managed patching, deployment slots, and built-in authentication options. It is not a Kubernetes control plane. Why the correct answer wins: Container Apps provides revisions and scale-to-zero without exposing a control plane to the team.

### Question 51 — B

Answer: Federate a Kubernetes service account to a managed identity. Federating the Kubernetes service account to a managed identity gives the pod an Azure token with no stored secret. Workload identity lets pods obtain tokens without stored secrets. Each workload should get its own identity and narrow role. Local study-map skill 1.6 (AKS Deployment with Manifests), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure container hosting documentation: https://learn.microsoft.com/en-us/azure/container-apps/

- **A:** Incorrect for this question. Geo-replication reduces cross-region pull latency and gives a local copy during a regional failure. It adds cost and replication management. Why the correct answer wins: Federating the Kubernetes service account to a managed identity gives the pod an Azure token with no stored secret.
- **B:** Correct. Workload identity lets pods obtain tokens without stored secrets. Each workload should get its own identity and narrow role. In this case: Federating the Kubernetes service account to a managed identity gives the pod an Azure token with no stored secret.
- **C:** Incorrect for this question. A Key Vault reference resolves at runtime so the secret is never written into application settings. The app identity still needs permission to read it. Why the correct answer wins: Federating the Kubernetes service account to a managed identity gives the pod an Azure token with no stored secret.
- **D:** Incorrect for this question. A floating tag removes the link between a deployed revision and a specific build, so rollback and audit become guesswork. Why the correct answer wins: Federating the Kubernetes service account to a managed identity gives the pod an Azure token with no stored secret.

### Question 52 — A

Answer: Test end-to-end connectivity from inside the container to each dependency. Testing the path from inside the pod proves DNS, egress, and firewall behaviour that host-side tests cannot reproduce. Reaching a dependency from the pod or replica proves DNS, egress, and firewall paths together. Host-side tests can succeed while the container path fails. Local study-map skill 1.7 (Container Logs, Events, and Connectivity), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure container hosting documentation: https://learn.microsoft.com/en-us/azure/container-apps/

- **A:** Correct. Reaching a dependency from the pod or replica proves DNS, egress, and firewall paths together. Host-side tests can succeed while the container path fails. In this case: Testing the path from inside the pod proves DNS, egress, and firewall behaviour that host-side tests cannot reproduce.
- **B:** Incorrect for this question. Time-binned aggregation reveals the shape of an incident: a step change, a ramp, or a periodic spike. Averages alone hide short outages. Why the correct answer wins: Testing the path from inside the pod proves DNS, egress, and firewall behaviour that host-side tests cannot reproduce.
- **C:** Incorrect for this question. Readiness gates traffic until the app can serve it, and liveness restarts a wedged container. Wrong thresholds cause restart loops. Why the correct answer wins: Testing the path from inside the pod proves DNS, egress, and firewall behaviour that host-side tests cannot reproduce.
- **D:** Incorrect for this question. Platform logs and metrics must be routed before they can be queried or alerted on. Retention and cost follow the workspace settings. Why the correct answer wins: Testing the path from inside the pod proves DNS, egress, and firewall behaviour that host-side tests cannot reproduce.

### Question 53 — A, B

Answers: Supply configuration through App Service application settings; Stage the change in a deployment slot and swap after verification. A staging slot verifies the build before the swap, and slot-scoped settings keep the environment endpoint out of the swap. Application settings become environment variables for the container and can be swapped per slot. Sensitive values should still reference a vault. A slot swap warms the new version before it takes production traffic and makes rollback a second swap. Slot-local settings must be marked sticky. Local study-map skill 1.3 (Container Deployment to Azure App Service), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure container hosting documentation: https://learn.microsoft.com/en-us/azure/container-apps/

- **A:** Correct. A slot swap warms the new version before it takes production traffic and makes rollback a second swap. Slot-local settings must be marked sticky. In this case: A staging slot verifies the build before the swap, and slot-scoped settings keep the environment endpoint out of the swap.
- **B:** Correct. Application settings become environment variables for the container and can be swapped per slot. Sensitive values should still reference a vault. In this case: A staging slot verifies the build before the swap, and slot-scoped settings keep the environment endpoint out of the swap.
- **C:** Incorrect for this question. Revision-based traffic splitting enables canary and blue-green releases. Revision mode and scale rules must be set deliberately. Why the correct answer wins: A staging slot verifies the build before the swap, and slot-scoped settings keep the environment endpoint out of the swap.
- **D:** Incorrect for this question. A manifest declares the desired deployment, service, and probe configuration in version control. Applying it repeatedly is idempotent. Why the correct answer wins: A staging slot verifies the build before the swap, and slot-scoped settings keep the environment endpoint out of the swap.
- **E:** Incorrect for this question. KEDA scalers drive replica count from queue length, lag, or other event metrics, including scale to zero. Cool-down and max replicas bound the behavior. Why the correct answer wins: A staging slot verifies the build before the swap, and slot-scoped settings keep the environment endpoint out of the swap.

### Question 54 — C

Answer: Build and push the image → deploy a new revision → shift a small traffic percentage → check metrics → promote or roll back. Build and push precede the revision, the traffic shift follows it, and promotion follows the observed metrics. A canary revision accepts a small share of traffic so metrics decide promotion rather than optimism. Local study-map skill 1.4 (Container Apps Deployment and Revisions), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure container hosting documentation: https://learn.microsoft.com/en-us/azure/container-apps/

- **A:** Incorrect for this question. Metrics cannot be checked before the revision serves traffic. Why the correct answer wins: Build and push precede the revision, the traffic shift follows it, and promotion follows the observed metrics.
- **B:** Incorrect for this question. Full traffic cannot move to a revision that does not exist yet, and the image must exist before the revision. Why the correct answer wins: Build and push precede the revision, the traffic shift follows it, and promotion follows the observed metrics.
- **C:** Correct. A canary revision accepts a small share of traffic so metrics decide promotion rather than optimism. In this case: Build and push precede the revision, the traffic shift follows it, and promotion follows the observed metrics.
- **D:** Incorrect for this question. Building after traffic is shifted means the running revision has no reviewed artifact behind it. Why the correct answer wins: Build and push precede the revision, the traffic shift follows it, and promotion follows the observed metrics.

### Question 55 — A

Answer: Store the documents in Azure Cosmos DB for NoSQL. Cosmos DB for NoSQL keeps the application document with an applicant partition key and serves point reads in one partition. Cosmos DB gives globally distributed, low-latency document access with tunable consistency. Partition key and RU planning determine the cost profile. Local study-map skill 2.1 (Cosmos DB SDK Access and Queries), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Cosmos DB and PostgreSQL vector documentation: https://learn.microsoft.com/en-us/azure/cosmos-db/

- **A:** Correct. Cosmos DB gives globally distributed, low-latency document access with tunable consistency. Partition key and RU planning determine the cost profile. In this case: Cosmos DB for NoSQL keeps the application document with an applicant partition key and serves point reads in one partition.
- **B:** Incorrect for this question. A point or single-partition query avoids fan-out across partitions. Cross-partition queries consume more RUs and add latency. Why the correct answer wins: Cosmos DB for NoSQL keeps the application document with an applicant partition key and serves point reads in one partition.
- **C:** Incorrect for this question. Queue Storage is simple and cheap for large backlogs with at-least-once delivery. It lacks topics, sessions, and scheduled messages. Why the correct answer wins: Cosmos DB for NoSQL keeps the application document with an applicant partition key and serves point reads in one partition.
- **D:** Incorrect for this question. pgvector keeps vectors beside relational data, so filters and joins run in one query. Index type and parameter tuning decide latency. Why the correct answer wins: Cosmos DB for NoSQL keeps the application document with an applicant partition key and serves point reads in one partition.

### Question 56 — A

Answer: Page large result sets with the continuation token. A continuation token pages the export without buffering the whole result set in memory. A continuation token returns the next page without re-sorting the previous one, which bounds response size and request charge per call. It is not a snapshot across pages. Local study-map skill 2.1 (Cosmos DB SDK Access and Queries), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Cosmos DB and PostgreSQL vector documentation: https://learn.microsoft.com/en-us/azure/cosmos-db/

- **A:** Correct. A continuation token returns the next page without re-sorting the previous one, which bounds response size and request charge per call. It is not a snapshot across pages. In this case: A continuation token pages the export without buffering the whole result set in memory.
- **B:** Incorrect for this question. Application-side scoring works for tiny collections and tests, but it moves all data over the wire and does not scale with corpus size. Why the correct answer wins: A continuation token pages the export without buffering the whole result set in memory.
- **C:** Incorrect for this question. A point or single-partition query avoids fan-out across partitions. Cross-partition queries consume more RUs and add latency. Why the correct answer wins: A continuation token pages the export without buffering the whole result set in memory.
- **D:** Incorrect for this question. Indexing everything is simple and makes ad hoc queries possible, at higher write cost and storage. It is a default, not an optimization. Why the correct answer wins: A continuation token pages the export without buffering the whole result set in memory.

### Question 57 — D

Answer: Enable autoscale throughput with a maximum RU limit. Autoscale throughput raises the ceiling during the filing peak and lowers it once demand falls. Autoscale follows demand between a minimum and maximum, avoiding throttling at peak without paying for peak all day. The maximum still caps the bill. Local study-map skill 2.2 (Cosmos DB Indexing Policies and Request Units), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Cosmos DB and PostgreSQL vector documentation: https://learn.microsoft.com/en-us/azure/cosmos-db/

- **A:** Incorrect for this question. Selective indexing cuts write RU charge and storage for unused paths. Excluded paths cannot be filtered efficiently later. Why the correct answer wins: Autoscale throughput raises the ceiling during the filing peak and lowers it once demand falls.
- **B:** Incorrect for this question. Indexing everything is simple and makes ad hoc queries possible, at higher write cost and storage. It is a default, not an optimization. Why the correct answer wins: Autoscale throughput raises the ceiling during the filing peak and lowers it once demand falls.
- **C:** Incorrect for this question. Request units measure the work a query performs, so tuning the query is often cheaper than adding throughput. Monitor normalized RU consumption. Why the correct answer wins: Autoscale throughput raises the ceiling during the filing peak and lowers it once demand falls.
- **D:** Correct. Autoscale follows demand between a minimum and maximum, avoiding throttling at peak without paying for peak all day. The maximum still caps the bill. In this case: Autoscale throughput raises the ceiling during the filing peak and lowers it once demand falls.

### Question 58 — A

Answer: Use session consistency for reads within the same client session. Session consistency guarantees the submitting client sees its own write at far lower cost than strong consistency. Session consistency guarantees monotonic reads for one session and is the common default for user-facing apps. It does not promise global freshness. Local study-map skill 2.3 (Cosmos DB Consistency Levels), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Cosmos DB and PostgreSQL vector documentation: https://learn.microsoft.com/en-us/azure/cosmos-db/

- **A:** Correct. Session consistency guarantees monotonic reads for one session and is the common default for user-facing apps. It does not promise global freshness. In this case: Session consistency guarantees the submitting client sees its own write at far lower cost than strong consistency.
- **B:** Incorrect for this question. Consistency trades freshness against latency, availability, and RU cost. The level is set at the account and can be relaxed per request. Why the correct answer wins: Session consistency guarantees the submitting client sees its own write at far lower cost than strong consistency.
- **C:** Incorrect for this question. Eventual consistency is the cheapest and most available option but returns possibly stale data. It fits non-critical counters, not balances. Why the correct answer wins: Session consistency guarantees the submitting client sees its own write at far lower cost than strong consistency.
- **D:** Incorrect for this question. Strong consistency guarantees the latest committed write globally at the cost of higher latency and reduced availability during partitions. Why the correct answer wins: Session consistency guarantees the submitting client sees its own write at far lower cost than strong consistency.

### Question 59 — C

Answer: Store embeddings in a vector property and query with VectorDistance. A vector property on the same document keeps embeddings and metadata together so filters and similarity run together. Cosmos DB for NoSQL supports vector properties and a distance function for similarity search in the same document store. Dimensions and index type must match the model. Local study-map skill 2.4 (Cosmos DB Vector Search and Embeddings), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Cosmos DB and PostgreSQL vector documentation: https://learn.microsoft.com/en-us/azure/cosmos-db/

- **A:** Incorrect for this question. DiskANN trades some recall for memory efficiency on large sets. Recall and latency should be measured on representative queries. Why the correct answer wins: A vector property on the same document keeps embeddings and metadata together so filters and similarity run together.
- **B:** Incorrect for this question. Application-side scoring works for tiny collections and tests, but it moves all data over the wire and does not scale with corpus size. Why the correct answer wins: A vector property on the same document keeps embeddings and metadata together so filters and similarity run together.
- **C:** Correct. Cosmos DB for NoSQL supports vector properties and a distance function for similarity search in the same document store. Dimensions and index type must match the model. In this case: A vector property on the same document keeps embeddings and metadata together so filters and similarity run together.
- **D:** Incorrect for this question. pgvector keeps vectors beside relational data, so filters and joins run in one query. Index type and parameter tuning decide latency. Why the correct answer wins: A vector property on the same document keeps embeddings and metadata together so filters and similarity run together.

### Question 60 — D

Answer: Use a lease container to coordinate change feed readers. Lease documents record partition ownership so instances divide the feed without processing the same item twice. Leases track partition ownership so multiple processor instances share work and resume from a continuation token. Lease writes consume RUs too. Local study-map skill 2.5 (Cosmos DB Change Feed Processing), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Cosmos DB and PostgreSQL vector documentation: https://learn.microsoft.com/en-us/azure/cosmos-db/

- **A:** Incorrect for this question. The change feed delivers an ordered stream of changes per partition for downstream processing. It is not a delete feed, so deletions need a workaround. Why the correct answer wins: Lease documents record partition ownership so instances divide the feed without processing the same item twice.
- **B:** Incorrect for this question. Item TTL expires documents automatically, which controls storage growth and data retention. It does not archive the expired content. Why the correct answer wins: Lease documents record partition ownership so instances divide the feed without processing the same item twice.
- **C:** Incorrect for this question. A duplicate-detection window drops repeated sends within the window, which helps with at-least-once producers. The window is time-bounded. Why the correct answer wins: Lease documents record partition ownership so instances divide the feed without processing the same item twice.
- **D:** Correct. Leases track partition ownership so multiple processor instances share work and resume from a continuation token. Lease writes consume RUs too. In this case: Lease documents record partition ownership so instances divide the feed without processing the same item twice.

### Question 61 — A

Answer: Create an IVFFlat index to save memory on a large table. IVFFlat needs far less memory than a graph index and trades some recall for that footprint. IVFFlat uses clustering lists and needs periodic rebuilds as data grows, but costs less memory than HNSW. Probes trade recall for speed. Local study-map skill 2.7 (pgvector Indexing and Query Latency), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Cosmos DB and PostgreSQL vector documentation: https://learn.microsoft.com/en-us/azure/cosmos-db/

- **A:** Correct. IVFFlat uses clustering lists and needs periodic rebuilds as data grows, but costs less memory than HNSW. Probes trade recall for speed. In this case: IVFFlat needs far less memory than a graph index and trades some recall for that footprint.
- **B:** Incorrect for this question. An external pooler multiplexes server connections for serverless or highly concurrent clients. Session-level features may be unavailable in transaction mode. Why the correct answer wins: IVFFlat needs far less memory than a graph index and trades some recall for that footprint.
- **C:** Incorrect for this question. HNSW gives fast approximate nearest-neighbour queries with a larger memory footprint and slower builds. Recall is tunable at query time. Why the correct answer wins: IVFFlat needs far less memory than a graph index and trades some recall for that footprint.
- **D:** Incorrect for this question. An exact scan is accurate but scales linearly and burns compute. It is a baseline for measuring recall, not a production strategy. Why the correct answer wins: IVFFlat needs far less memory than a graph index and trades some recall for that footprint.

### Question 62 — B

Answer: Increase maintenance and query memory settings for index builds and sorts. Raising maintenance and query memory lets the build sort and batch in memory instead of spilling. Index builds and large sorts spill to disk when work memory is too small, stretching maintenance windows and slowing queries. Local study-map skill 2.8 (PostgreSQL Compute, Memory, and Storage Sizing), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Cosmos DB and PostgreSQL vector documentation: https://learn.microsoft.com/en-us/azure/cosmos-db/

- **A:** Incorrect for this question. Index creation and bulk loads are I/O heavy, and throttled storage stretches maintenance windows. Storage limits are separate from compute. Why the correct answer wins: Raising maintenance and query memory lets the build sort and batch in memory instead of spilling.
- **B:** Correct. Index builds and large sorts spill to disk when work memory is too small, stretching maintenance windows and slowing queries. In this case: Raising maintenance and query memory lets the build sort and batch in memory instead of spilling.
- **C:** Incorrect for this question. Statistics and dead-tuple cleanup change plan quality and index performance. Autovacuum tuning matters for churn-heavy vector tables. Why the correct answer wins: Raising maintenance and query memory lets the build sort and batch in memory instead of spilling.
- **D:** Incorrect for this question. A replica offloads read traffic but introduces replication lag, which is dangerous for freshly written evidence. It does not reduce index memory pressure. Why the correct answer wins: Raising maintenance and query memory lets the build sort and batch in memory instead of spilling.

### Question 63 — A

Answer: Invalidate or overwrite the cache entry when the source changes. A TTL alone leaves a stale fee schedule until expiry, so the write path must overwrite or remove the entry. Write-through or explicit invalidation keeps cached answers consistent with the system of record. Without it, TTL is the only bound on staleness. Local study-map skill 2.11 (Azure Managed Redis Caching and Invalidation), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Cosmos DB and PostgreSQL vector documentation: https://learn.microsoft.com/en-us/azure/cosmos-db/

- **A:** Correct. Write-through or explicit invalidation keeps cached answers consistent with the system of record. Without it, TTL is the only bound on staleness. In this case: A TTL alone leaves a stale fee schedule until expiry, so the write path must overwrite or remove the entry.
- **B:** Incorrect for this question. Flushing removes all cached content at once, causing a stampede to the origin and a latency cliff. Targeted invalidation is safer. Why the correct answer wins: A TTL alone leaves a stale fee schedule until expiry, so the write path must overwrite or remove the entry.
- **C:** Incorrect for this question. A TTL bounds staleness and reclaims memory without a manual sweep. Too long a TTL hides source changes; too short wastes the cache. Why the correct answer wins: A TTL alone leaves a stale fee schedule until expiry, so the write path must overwrite or remove the entry.
- **D:** Incorrect for this question. Eviction protects memory but evicts unpredictably, so a hot key can vanish before its freshness bound is reached. It is not a substitute for TTL design. Why the correct answer wins: A TTL alone leaves a stale fee schedule until expiry, so the write path must overwrite or remove the entry.

### Question 64 — A

Answer: Set a TTL on each cached entry. A TTL retires entries that will never be requested again, which keeps memory bounded without manual cleanup. A TTL bounds staleness and reclaims memory without a manual sweep. Too long a TTL hides source changes; too short wastes the cache. Local study-map skill 2.11 (Azure Managed Redis Caching and Invalidation), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Cosmos DB and PostgreSQL vector documentation: https://learn.microsoft.com/en-us/azure/cosmos-db/

- **A:** Correct. A TTL bounds staleness and reclaims memory without a manual sweep. Too long a TTL hides source changes; too short wastes the cache. In this case: A TTL retires entries that will never be requested again, which keeps memory bounded without manual cleanup.
- **B:** Incorrect for this question. Eviction protects memory but evicts unpredictably, so a hot key can vanish before its freshness bound is reached. It is not a substitute for TTL design. Why the correct answer wins: A TTL retires entries that will never be requested again, which keeps memory bounded without manual cleanup.
- **C:** Incorrect for this question. Flushing removes all cached content at once, causing a stampede to the origin and a latency cliff. Targeted invalidation is safer. Why the correct answer wins: A TTL retires entries that will never be requested again, which keeps memory bounded without manual cleanup.
- **D:** Incorrect for this question. Write-through or explicit invalidation keeps cached answers consistent with the system of record. Without it, TTL is the only bound on staleness. Why the correct answer wins: A TTL retires entries that will never be requested again, which keeps memory bounded without manual cleanup.

### Question 65 — A, C

Answers: Query through the Cosmos DB SDK with parameterized queries; Choose a high-cardinality partition key that spreads writes. SDK parameterized queries stay on the supported path, and a high-cardinality applicant key avoids cross-partition fan-out. SDK queries keep the client on the supported data plane and parameterization avoids injection and plan churn. Cross-partition queries still cost more. A good partition key distributes storage and throughput and keeps common queries single-partition. Low cardinality creates hot partitions. Local study-map skill 2.1 (Cosmos DB SDK Access and Queries), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Cosmos DB and PostgreSQL vector documentation: https://learn.microsoft.com/en-us/azure/cosmos-db/

- **A:** Correct. SDK queries keep the client on the supported data plane and parameterization avoids injection and plan churn. Cross-partition queries still cost more. In this case: SDK parameterized queries stay on the supported path, and a high-cardinality applicant key avoids cross-partition fan-out.
- **B:** Incorrect for this question. A point or single-partition query avoids fan-out across partitions. Cross-partition queries consume more RUs and add latency. Why the correct answer wins: SDK parameterized queries stay on the supported path, and a high-cardinality applicant key avoids cross-partition fan-out.
- **C:** Correct. A good partition key distributes storage and throughput and keeps common queries single-partition. Low cardinality creates hot partitions. In this case: SDK parameterized queries stay on the supported path, and a high-cardinality applicant key avoids cross-partition fan-out.
- **D:** Incorrect for this question. Indexing everything is simple and makes ad hoc queries possible, at higher write cost and storage. It is a default, not an optimization. Why the correct answer wins: SDK parameterized queries stay on the supported path, and a high-cardinality applicant key avoids cross-partition fan-out.
- **E:** Incorrect for this question. Application-side scoring works for tiny collections and tests, but it moves all data over the wire and does not scale with corpus size. Why the correct answer wins: SDK parameterized queries stay on the supported path, and a high-cardinality applicant key avoids cross-partition fan-out.

### Question 66 — C, E

Answers: Create an HNSW index for low-latency approximate search; Scale compute and memory to fit index size and query concurrency. HNSW provides low-latency approximate search, and sizing compute and memory keeps the index resident. HNSW gives fast approximate nearest-neighbour queries with a larger memory footprint and slower builds. Recall is tunable at query time. Vector indexes are memory-hungry, so undersized compute causes swapping and slow queries. Right-size before tuning index parameters. Local study-map skill 2.7 (pgvector Indexing and Query Latency), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Cosmos DB and PostgreSQL vector documentation: https://learn.microsoft.com/en-us/azure/cosmos-db/

- **A:** Incorrect for this question. Index creation and bulk loads are I/O heavy, and throttled storage stretches maintenance windows. Storage limits are separate from compute. Why the correct answer wins: HNSW provides low-latency approximate search, and sizing compute and memory keeps the index resident.
- **B:** Incorrect for this question. IVFFlat uses clustering lists and needs periodic rebuilds as data grows, but costs less memory than HNSW. Probes trade recall for speed. Why the correct answer wins: HNSW provides low-latency approximate search, and sizing compute and memory keeps the index resident.
- **C:** Correct. HNSW gives fast approximate nearest-neighbour queries with a larger memory footprint and slower builds. Recall is tunable at query time. In this case: HNSW provides low-latency approximate search, and sizing compute and memory keeps the index resident.
- **D:** Incorrect for this question. An exact scan is accurate but scales linearly and burns compute. It is a baseline for measuring recall, not a production strategy. Why the correct answer wins: HNSW provides low-latency approximate search, and sizing compute and memory keeps the index resident.
- **E:** Correct. Vector indexes are memory-hungry, so undersized compute causes swapping and slow queries. Right-size before tuning index parameters. In this case: HNSW provides low-latency approximate search, and sizing compute and memory keeps the index resident.

### Question 67 — D

Answer: Create the vector extension → create the table with a vector column → build the index → query nearest neighbours with a distance operator. The extension and table exist before the index, and the index exists before efficient nearest-neighbour queries. The extension and typed column must exist before an index can be built, and the index before the query is efficient. Local study-map skill 2.7 (pgvector Indexing and Query Latency), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Cosmos DB and PostgreSQL vector documentation: https://learn.microsoft.com/en-us/azure/cosmos-db/

- **A:** Incorrect for this question. Querying before the schema exists cannot succeed, and the index cannot precede the table. Why the correct answer wins: The extension and table exist before the index, and the index exists before efficient nearest-neighbour queries.
- **B:** Incorrect for this question. An index cannot be built before the extension and the table exist. Why the correct answer wins: The extension and table exist before the index, and the index exists before efficient nearest-neighbour queries.
- **C:** Incorrect for this question. The extension is required for the vector type, and the query should follow index creation for usable latency. Why the correct answer wins: The extension and table exist before the index, and the index exists before efficient nearest-neighbour queries.
- **D:** Correct. The extension and typed column must exist before an index can be built, and the index before the query is efficient. In this case: The extension and table exist before the index, and the index exists before efficient nearest-neighbour queries.

### Question 68 — C

Answer: Use Service Bus sessions to keep related messages ordered. Sessions give exclusive, ordered processing per application identifier across competing consumers. Sessions give ordered, exclusive processing per session ID across competing consumers. They require session-aware senders and receivers. Local study-map skill 3.1 (Service Bus Queues and Sessions), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure messaging and Functions documentation: https://learn.microsoft.com/en-us/azure/service-bus-messaging/

- **A:** Incorrect for this question. A delivery cap stops infinite retries of a failing message and moves it to the dead-letter queue. The cap must exceed legitimate transient retries. Why the correct answer wins: Sessions give exclusive, ordered processing per application identifier across competing consumers.
- **B:** Incorrect for this question. Peek-lock keeps the message locked until the handler completes it, giving at-least-once processing with retry. Lock duration must exceed processing time. Why the correct answer wins: Sessions give exclusive, ordered processing per application identifier across competing consumers.
- **C:** Correct. Sessions give ordered, exclusive processing per session ID across competing consumers. They require session-aware senders and receivers. In this case: Sessions give exclusive, ordered processing per application identifier across competing consumers.
- **D:** Incorrect for this question. A duplicate-detection window drops repeated sends within the window, which helps with at-least-once producers. The window is time-bounded. Why the correct answer wins: Sessions give exclusive, ordered processing per application identifier across competing consumers.

### Question 69 — C

Answer: Add a SQL or correlation filter to a subscription. A subscription filter evaluates message properties broker-side so only matching applications are delivered. Subscription filters route only matching messages to a handler, reducing wasted processing. Filter evaluation happens broker-side on message properties. Local study-map skill 3.2 (Service Bus Topics, Subscriptions, and Filters), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure messaging and Functions documentation: https://learn.microsoft.com/en-us/azure/service-bus-messaging/

- **A:** Incorrect for this question. A custom schema fits domain events that are not resource lifecycle notifications. Consumers must version the schema contract. Why the correct answer wins: A subscription filter evaluates message properties broker-side so only matching applications are delivered.
- **B:** Incorrect for this question. A duplicate-detection window drops repeated sends within the window, which helps with at-least-once producers. The window is time-bounded. Why the correct answer wins: A subscription filter evaluates message properties broker-side so only matching applications are delivered.
- **C:** Correct. Subscription filters route only matching messages to a handler, reducing wasted processing. Filter evaluation happens broker-side on message properties. In this case: A subscription filter evaluates message properties broker-side so only matching applications are delivered.
- **D:** Incorrect for this question. Subject and event-type filters keep handlers focused and reduce cost. Filters are evaluated on event metadata, not payload body. Why the correct answer wins: A subscription filter evaluates message properties broker-side so only matching applications are delivered.

### Question 70 — D

Answer: Enable duplicate detection on the queue. Duplicate detection drops a repeated message identifier inside the window before a handler sees it. A duplicate-detection window drops repeated sends within the window, which helps with at-least-once producers. The window is time-bounded. Local study-map skill 3.3 (Service Bus Dead-Lettering and Retries), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure messaging and Functions documentation: https://learn.microsoft.com/en-us/azure/service-bus-messaging/

- **A:** Incorrect for this question. A delivery cap stops infinite retries of a failing message and moves it to the dead-letter queue. The cap must exceed legitimate transient retries. Why the correct answer wins: Duplicate detection drops a repeated message identifier inside the window before a handler sees it.
- **B:** Incorrect for this question. Dead-lettering preserves poison messages for diagnosis instead of losing them. Resubmission needs a fix and an idempotent handler. Why the correct answer wins: Duplicate detection drops a repeated message identifier inside the window before a handler sees it.
- **C:** Incorrect for this question. At-least-once delivery means duplicates will happen, so the write must tolerate replay. A stored key makes the retry safe. Why the correct answer wins: Duplicate detection drops a repeated message identifier inside the window before a handler sees it.
- **D:** Correct. A duplicate-detection window drops repeated sends within the window, which helps with at-least-once producers. The window is time-bounded. In this case: Duplicate detection drops a repeated message identifier inside the window before a handler sees it.

### Question 71 — D

Answer: Publish the state change as an Event Grid event. An Event Grid subscription on the storage system topic pushes blob-created events when the file lands. Event Grid delivers discrete notifications to subscribers with retries and filtering. It carries events, not large payloads or ordered streams. Local study-map skill 3.4 (Event Grid Filters, Custom Events, and Retries), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure messaging and Functions documentation: https://learn.microsoft.com/en-us/azure/service-bus-messaging/

- **A:** Incorrect for this question. Durable Functions provides orchestrations, activities, timers, and retries with checkpointed state. Orchestrator code must stay deterministic. Why the correct answer wins: An Event Grid subscription on the storage system topic pushes blob-created events when the file lands.
- **B:** Incorrect for this question. Queue Storage is simple and cheap for large backlogs with at-least-once delivery. It lacks topics, sessions, and scheduled messages. Why the correct answer wins: An Event Grid subscription on the storage system topic pushes blob-created events when the file lands.
- **C:** Incorrect for this question. Event Hubs ingests high-volume ordered streams with partitions and consumer groups. It is a streaming log, not a task queue. Why the correct answer wins: An Event Grid subscription on the storage system topic pushes blob-created events when the file lands.
- **D:** Correct. Event Grid delivers discrete notifications to subscribers with retries and filtering. It carries events, not large payloads or ordered streams. In this case: An Event Grid subscription on the storage system topic pushes blob-created events when the file lands.

### Question 72 — C

Answer: Run the scheduled maintenance from a timer trigger. A timer trigger runs on a declared schedule without an external caller and honours an explicit time zone. A timer trigger invokes the function on a schedule without an external caller. Overlapping runs and the time zone must be configured deliberately. Local study-map skill 3.5 (Azure Functions Triggers and Bindings), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure messaging and Functions documentation: https://learn.microsoft.com/en-us/azure/service-bus-messaging/

- **A:** Incorrect for this question. An HTTP trigger gives a synchronous API endpoint with route and authorization configuration. Long-running work should hand off to a queue. Why the correct answer wins: A timer trigger runs on a declared schedule without an external caller and honours an explicit time zone.
- **B:** Incorrect for this question. Event Grid retries failed deliveries with backoff and can store undeliverable events. Handlers must still be idempotent. Why the correct answer wins: A timer trigger runs on a declared schedule without an external caller and honours an explicit time zone.
- **C:** Correct. A timer trigger invokes the function on a schedule without an external caller. Overlapping runs and the time zone must be configured deliberately. In this case: A timer trigger runs on a declared schedule without an external caller and honours an explicit time zone.
- **D:** Incorrect for this question. A trigger starts the function when work arrives and handles the receive loop for you. Poison-message behavior is configured in host settings. Why the correct answer wins: A timer trigger runs on a declared schedule without an external caller and honours an explicit time zone.

### Question 73 — A

Answer: Orchestrate the multi-step workflow with Durable Functions. Durable Functions checkpoint progress and wait for external events without holding a process open. Durable Functions provides orchestrations, activities, timers, and retries with checkpointed state. Orchestrator code must stay deterministic. Local study-map skill 3.6 (Function App Configuration and Deployment), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure messaging and Functions documentation: https://learn.microsoft.com/en-us/azure/service-bus-messaging/

- **A:** Correct. Durable Functions provides orchestrations, activities, timers, and retries with checkpointed state. Orchestrator code must stay deterministic. In this case: Durable Functions checkpoint progress and wait for external events without holding a process open.
- **B:** Incorrect for this question. A trigger starts the function when work arrives and handles the receive loop for you. Poison-message behavior is configured in host settings. Why the correct answer wins: Durable Functions checkpoint progress and wait for external events without holding a process open.
- **C:** Incorrect for this question. An HTTP trigger gives a synchronous API endpoint with route and authorization configuration. Long-running work should hand off to a queue. Why the correct answer wins: Durable Functions checkpoint progress and wait for external events without holding a process open.
- **D:** Incorrect for this question. Bindings reduce boilerplate for common inputs and outputs and are configured declaratively. Complex operations still need the SDK. Why the correct answer wins: Durable Functions checkpoint progress and wait for external events without holding a process open.

### Question 74 — C

Answer: Tune the function app concurrency and batch size. Lower concurrency and batch size per instance bound the parallel calls that a batch can send. Concurrency and batch size bound how much work one instance takes at a time, which controls downstream pressure and memory. Too high a value causes throttling and timeouts. Local study-map skill 3.6 (Function App Configuration and Deployment), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure messaging and Functions documentation: https://learn.microsoft.com/en-us/azure/service-bus-messaging/

- **A:** Incorrect for this question. The host retry policy re-executes a failing trigger with bounded attempts and backoff. It cannot make a non-idempotent handler safe to replay. Why the correct answer wins: Lower concurrency and batch size per instance bound the parallel calls that a batch can send.
- **B:** Incorrect for this question. Consumption bills per execution and scales automatically, with cold starts and a timeout ceiling. It fits spiky, short work. Why the correct answer wins: Lower concurrency and batch size per instance bound the parallel calls that a batch can send.
- **C:** Correct. Concurrency and batch size bound how much work one instance takes at a time, which controls downstream pressure and memory. Too high a value causes throttling and timeouts. In this case: Lower concurrency and batch size per instance bound the parallel calls that a batch can send.
- **D:** Incorrect for this question. A premium plan reduces cold starts and supports virtual network integration and longer timeouts. It costs more than consumption. Why the correct answer wins: Lower concurrency and batch size per instance bound the parallel calls that a batch can send.

### Question 75 — B

Answer: Deploy the function app through a CI pipeline with app settings applied. A pipeline deployment publishes code and applies settings together, so the app never runs half-configured. Pipeline deployment keeps code and configuration versioned together and repeatable. Secrets belong in a vault reference, not in the pipeline file. Local study-map skill 3.6 (Function App Configuration and Deployment), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure messaging and Functions documentation: https://learn.microsoft.com/en-us/azure/service-bus-messaging/

- **A:** Incorrect for this question. A premium plan reduces cold starts and supports virtual network integration and longer timeouts. It costs more than consumption. Why the correct answer wins: A pipeline deployment publishes code and applies settings together, so the app never runs half-configured.
- **B:** Correct. Pipeline deployment keeps code and configuration versioned together and repeatable. Secrets belong in a vault reference, not in the pipeline file. In this case: A pipeline deployment publishes code and applies settings together, so the app never runs half-configured.
- **C:** Incorrect for this question. An HTTP trigger gives a synchronous API endpoint with route and authorization configuration. Long-running work should hand off to a queue. Why the correct answer wins: A pipeline deployment publishes code and applies settings together, so the app never runs half-configured.
- **D:** Incorrect for this question. Application settings become environment variables for the container and can be swapped per slot. Sensitive values should still reference a vault. Why the correct answer wins: A pipeline deployment publishes code and applies settings together, so the app never runs half-configured.

### Question 76 — C, E

Answers: Use Service Bus sessions to keep related messages ordered; Increase prefetch count to reduce round trips. Sessions provide ordered processing per application, and prefetch reduces the receive round trips per batch. Sessions give ordered, exclusive processing per session ID across competing consumers. They require session-aware senders and receivers. Prefetch reduces latency per message by batching receives, at the cost of holding more locked messages. Lock duration must cover the batch. Local study-map skill 3.1 (Service Bus Queues and Sessions), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure messaging and Functions documentation: https://learn.microsoft.com/en-us/azure/service-bus-messaging/

- **A:** Incorrect for this question. Dead-lettering preserves poison messages for diagnosis instead of losing them. Resubmission needs a fix and an idempotent handler. Why the correct answer wins: Sessions provide ordered processing per application, and prefetch reduces the receive round trips per batch.
- **B:** Incorrect for this question. Peek-lock keeps the message locked until the handler completes it, giving at-least-once processing with retry. Lock duration must exceed processing time. Why the correct answer wins: Sessions provide ordered processing per application, and prefetch reduces the receive round trips per batch.
- **C:** Correct. Prefetch reduces latency per message by batching receives, at the cost of holding more locked messages. Lock duration must cover the batch. In this case: Sessions provide ordered processing per application, and prefetch reduces the receive round trips per batch.
- **D:** Incorrect for this question. Receive-and-delete removes the message on delivery, so a crash loses work silently. It suits telemetry, not payments. Why the correct answer wins: Sessions provide ordered processing per application, and prefetch reduces the receive round trips per batch.
- **E:** Correct. Sessions give ordered, exclusive processing per session ID across competing consumers. They require session-aware senders and receivers. In this case: Sessions provide ordered processing per application, and prefetch reduces the receive round trips per batch.

### Question 77 — C, E

Answers: Define a custom event schema for the topic; Rely on Event Grid retries with a dead-letter destination. A custom event schema carries the domain payload, and retries with dead-lettering prevent permanent loss. A custom schema fits domain events that are not resource lifecycle notifications. Consumers must version the schema contract. Event Grid retries failed deliveries with backoff and can store undeliverable events. Handlers must still be idempotent. Local study-map skill 3.4 (Event Grid Filters, Custom Events, and Retries), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure messaging and Functions documentation: https://learn.microsoft.com/en-us/azure/service-bus-messaging/

- **A:** Incorrect for this question. Event Hubs ingests high-volume ordered streams with partitions and consumer groups. It is a streaming log, not a task queue. Why the correct answer wins: A custom event schema carries the domain payload, and retries with dead-lettering prevent permanent loss.
- **B:** Incorrect for this question. Subscription filters route only matching messages to a handler, reducing wasted processing. Filter evaluation happens broker-side on message properties. Why the correct answer wins: A custom event schema carries the domain payload, and retries with dead-lettering prevent permanent loss.
- **C:** Correct. Event Grid retries failed deliveries with backoff and can store undeliverable events. Handlers must still be idempotent. In this case: A custom event schema carries the domain payload, and retries with dead-lettering prevent permanent loss.
- **D:** Incorrect for this question. Subject and event-type filters keep handlers focused and reduce cost. Filters are evaluated on event metadata, not payload body. Why the correct answer wins: A custom event schema carries the domain payload, and retries with dead-lettering prevent permanent loss.
- **E:** Correct. A custom schema fits domain events that are not resource lifecycle notifications. Consumers must version the schema contract. In this case: A custom event schema carries the domain payload, and retries with dead-lettering prevent permanent loss.

### Question 78 — A

Answer: Publish the message → receive with peek-lock → process the work → complete the message → dead-letter after the delivery limit. Publish precedes peek-lock receipt, processing precedes completion, and dead-lettering follows the delivery limit. Peek-lock keeps the message until the handler succeeds, and only repeated failures should dead-letter it. Local study-map skill 3.3 (Service Bus Dead-Lettering and Retries), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure messaging and Functions documentation: https://learn.microsoft.com/en-us/azure/service-bus-messaging/

- **A:** Correct. Peek-lock keeps the message until the handler succeeds, and only repeated failures should dead-letter it. In this case: Publish precedes peek-lock receipt, processing precedes completion, and dead-lettering follows the delivery limit.
- **B:** Incorrect for this question. Completing a message before processing discards the work and defeats at-least-once delivery. Why the correct answer wins: Publish precedes peek-lock receipt, processing precedes completion, and dead-lettering follows the delivery limit.
- **C:** Incorrect for this question. The message cannot be received before it is published, and completion must follow processing. Why the correct answer wins: Publish precedes peek-lock receipt, processing precedes completion, and dead-lettering follows the delivery limit.
- **D:** Incorrect for this question. Work cannot be processed before the message is published and received. Why the correct answer wins: Publish precedes peek-lock receipt, processing precedes completion, and dead-lettering follows the delivery limit.

### Question 79 — A

Answer: Grant the app identity data-plane access to the vault. A managed identity still needs a data-plane role on the vault, and the 403 shows that assignment is absent. Vault access is a separate authorization decision from the app identity. Without a data-plane role or policy the reference fails at runtime. Local study-map skill 4.1 (Key Vault Secret Storage, Rotation, and Retrieval), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Key Vault, App Configuration, and Monitor documentation: https://learn.microsoft.com/en-us/azure/azure-monitor/

- **A:** Correct. Vault access is a separate authorization decision from the app identity. Without a data-plane role or policy the reference fails at runtime. In this case: A managed identity still needs a data-plane role on the vault, and the 403 shows that assignment is absent.
- **B:** Incorrect for this question. A scoped role grants only the operations the app performs and limits blast radius. Prefer built-in roles over broad contributor grants. Why the correct answer wins: A managed identity still needs a data-plane role on the vault, and the 403 shows that assignment is absent.
- **C:** Incorrect for this question. A vault centralizes secret storage with access control and audit. Retrieval should use an identity, not a copied credential. Why the correct answer wins: A managed identity still needs a data-plane role on the vault, and the 403 shows that assignment is absent.
- **D:** Incorrect for this question. A Key Vault reference resolves at runtime so the secret is never written into application settings. The app identity still needs permission to read it. Why the correct answer wins: A managed identity still needs a data-plane role on the vault, and the 403 shows that assignment is absent.

### Question 80 — D

Answer: Rotate the secret on a schedule and let apps resolve the current version. Rotation issues a new secret version, and the app resolves the current version so no deployment is needed. Rotation limits the value of a leaked secret, but callers must read the latest version rather than caching an old one forever. Local study-map skill 4.1 (Key Vault Secret Storage, Rotation, and Retrieval), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Key Vault, App Configuration, and Monitor documentation: https://learn.microsoft.com/en-us/azure/azure-monitor/

- **A:** Incorrect for this question. A managed identity issues tokens from the platform, removing secret distribution from the app. Role assignment still scopes what it can reach. Why the correct answer wins: Rotation issues a new secret version, and the app resolves the current version so no deployment is needed.
- **B:** Incorrect for this question. Soft delete and purge protection stop accidental or malicious permanent loss of secrets. They also constrain how names can be reused. Why the correct answer wins: Rotation issues a new secret version, and the app resolves the current version so no deployment is needed.
- **C:** Incorrect for this question. Pinning a version makes a rotation invisible to the app until it is redeployed, which is useful for break-glass and dangerous for routine rotation. Why the correct answer wins: Rotation issues a new secret version, and the app resolves the current version so no deployment is needed.
- **D:** Correct. Rotation limits the value of a leaked secret, but callers must read the latest version rather than caching an old one forever. In this case: Rotation issues a new secret version, and the app resolves the current version so no deployment is needed.

### Question 81 — C

Answer: Store settings and feature flags in Azure App Configuration. App Configuration centralizes settings and feature flags while labels keep agency-specific values apart. App Configuration separates configuration from code and supports labels, feature flags, and Key Vault references. Change still needs a refresh strategy. Local study-map skill 4.2 (App Configuration Settings and Feature Flags), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Key Vault, App Configuration, and Monitor documentation: https://learn.microsoft.com/en-us/azure/azure-monitor/

- **A:** Incorrect for this question. Sentinel-key or polling refresh lets a running app pick up new settings. Refresh intervals trade responsiveness against request volume. Why the correct answer wins: App Configuration centralizes settings and feature flags while labels keep agency-specific values apart.
- **B:** Incorrect for this question. Labels keep dev, test, and prod values in one store with one key schema. A misconfigured label selector silently serves the wrong values. Why the correct answer wins: App Configuration centralizes settings and feature flags while labels keep agency-specific values apart.
- **C:** Correct. App Configuration separates configuration from code and supports labels, feature flags, and Key Vault references. Change still needs a refresh strategy. In this case: App Configuration centralizes settings and feature flags while labels keep agency-specific values apart.
- **D:** Incorrect for this question. A Key Vault reference keeps non-secret settings in App Configuration while the value stays in the vault. The app identity needs both sets of permissions. Why the correct answer wins: App Configuration centralizes settings and feature flags while labels keep agency-specific values apart.

### Question 82 — C

Answer: Aggregate with summarize and bin to see the failure rate over time. summarize with bin groups requests into time buckets and counts the failures in each bucket. Time-binned aggregation reveals the shape of an incident: a step change, a ramp, or a periodic spike. Averages alone hide short outages. Local study-map skill 4.4 (KQL Queries for Logs and Metrics), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Key Vault, App Configuration, and Monitor documentation: https://learn.microsoft.com/en-us/azure/azure-monitor/

- **A:** Incorrect for this question. Reducing columns and rows early lowers query cost and latency. Broad queries over long ranges are the usual cause of slow KQL. Why the correct answer wins: summarize with bin groups requests into time buckets and counts the failures in each bucket.
- **B:** Incorrect for this question. KQL filters, projects, and aggregates log and metric tables in Log Analytics. Start narrow with a time range and a request ID. Why the correct answer wins: summarize with bin groups requests into time buckets and counts the failures in each bucket.
- **C:** Correct. Time-binned aggregation reveals the shape of an incident: a step change, a ramp, or a periodic spike. Averages alone hide short outages. In this case: summarize with bin groups requests into time buckets and counts the failures in each bucket.
- **D:** Incorrect for this question. Joining request and dependency telemetry shows which downstream call fails inside a slow request. Cross-workspace joins need the right scope. Why the correct answer wins: summarize with bin groups requests into time buckets and counts the failures in each bucket.

### Question 83 — C

Answer: Set the workspace retention and table plan to control log cost. Adjusting retention and the table plan per table removes cost from data that policy does not require. Retention and the table plan determine how long data is queryable and what it costs. Lower retention reduces cost but shortens the investigation window. Local study-map skill 4.4 (KQL Queries for Logs and Metrics), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Key Vault, App Configuration, and Monitor documentation: https://learn.microsoft.com/en-us/azure/azure-monitor/

- **A:** Incorrect for this question. Container Apps and AKS surface stdout logs and platform events into a workspace for KQL analysis. Verbosity and retention cost money. Why the correct answer wins: Adjusting retention and the table plan per table removes cost from data that policy does not require.
- **B:** Incorrect for this question. Platform metrics are cheap and near-real-time, so they suit latency and failure-rate alerts. Log-based alerts add latency and query cost. Why the correct answer wins: Adjusting retention and the table plan per table removes cost from data that policy does not require.
- **C:** Correct. Retention and the table plan determine how long data is queryable and what it costs. Lower retention reduces cost but shortens the investigation window. In this case: Adjusting retention and the table plan per table removes cost from data that policy does not require.
- **D:** Incorrect for this question. Platform logs and metrics must be routed before they can be queried or alerted on. Retention and cost follow the workspace settings. Why the correct answer wins: Adjusting retention and the table plan per table removes cost from data that policy does not require.

### Question 84 — A

Answer: Reach the data service through a private endpoint. A private endpoint places the database on a private address inside the virtual network. A private endpoint keeps traffic on the virtual network and removes public exposure. DNS resolution must be wired to the private zone. Local study-map skill 4.5 (Identity-Based Access for Application Services), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Key Vault, App Configuration, and Monitor documentation: https://learn.microsoft.com/en-us/azure/azure-monitor/

- **A:** Correct. A private endpoint keeps traffic on the virtual network and removes public exposure. DNS resolution must be wired to the private zone. In this case: A private endpoint places the database on a private address inside the virtual network.
- **B:** Incorrect for this question. Platform logs and metrics must be routed before they can be queried or alerted on. Retention and cost follow the workspace settings. Why the correct answer wins: A private endpoint places the database on a private address inside the virtual network.
- **C:** Incorrect for this question. A private endpoint needs matching name resolution or clients still resolve the public address. The zone must be linked to the workload network. Why the correct answer wins: A private endpoint places the database on a private address inside the virtual network.
- **D:** Incorrect for this question. Reaching a dependency from the pod or replica proves DNS, egress, and firewall paths together. Host-side tests can succeed while the container path fails. Why the correct answer wins: A private endpoint places the database on a private address inside the virtual network.

### Question 85 — C, E

Answers: Authenticate with a managed identity instead of a stored key; Assign a least-privilege role to the application identity. A managed identity supplies the credential, and a scoped least-privilege role grants only the access needed. A managed identity issues tokens from the platform, removing secret distribution from the app. Role assignment still scopes what it can reach. A scoped role grants only the operations the app performs and limits blast radius. Prefer built-in roles over broad contributor grants. Local study-map skill 4.5 (Identity-Based Access for Application Services), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Key Vault, App Configuration, and Monitor documentation: https://learn.microsoft.com/en-us/azure/azure-monitor/

- **A:** Incorrect for this question. A Key Vault reference resolves at runtime so the secret is never written into application settings. The app identity still needs permission to read it. Why the correct answer wins: A managed identity supplies the credential, and a scoped least-privilege role grants only the access needed.
- **B:** Incorrect for this question. Soft delete and purge protection stop accidental or malicious permanent loss of secrets. They also constrain how names can be reused. Why the correct answer wins: A managed identity supplies the credential, and a scoped least-privilege role grants only the access needed.
- **C:** Correct. A managed identity issues tokens from the platform, removing secret distribution from the app. Role assignment still scopes what it can reach. In this case: A managed identity supplies the credential, and a scoped least-privilege role grants only the access needed.
- **D:** Incorrect for this question. Pinning a version makes a rotation invisible to the app until it is redeployed, which is useful for break-glass and dangerous for routine rotation. Why the correct answer wins: A managed identity supplies the credential, and a scoped least-privilege role grants only the access needed.
- **E:** Correct. A scoped role grants only the operations the app performs and limits blast radius. Prefer built-in roles over broad contributor grants. In this case: A managed identity supplies the credential, and a scoped least-privilege role grants only the access needed.

### Question 86 — A, D

Answers: Use App Configuration labels to separate environments; Reference the Key Vault secret from an App Configuration key value. Labels separate agencies in one store, and a Key Vault reference keeps the secret out of the store. Labels keep dev, test, and prod values in one store with one key schema. A misconfigured label selector silently serves the wrong values. A Key Vault reference keeps non-secret settings in App Configuration while the value stays in the vault. The app identity needs both sets of permissions. Local study-map skill 4.2 (App Configuration Settings and Feature Flags), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Key Vault, App Configuration, and Monitor documentation: https://learn.microsoft.com/en-us/azure/azure-monitor/

- **A:** Correct. A Key Vault reference keeps non-secret settings in App Configuration while the value stays in the vault. The app identity needs both sets of permissions. In this case: Labels separate agencies in one store, and a Key Vault reference keeps the secret out of the store.
- **B:** Incorrect for this question. A feature flag enables reviewed code in production without a redeploy and lets it be switched off instantly. Flag state still needs ownership and cleanup. Why the correct answer wins: Labels separate agencies in one store, and a Key Vault reference keeps the secret out of the store.
- **C:** Incorrect for this question. Pinning a version makes a rotation invisible to the app until it is redeployed, which is useful for break-glass and dangerous for routine rotation. Why the correct answer wins: Labels separate agencies in one store, and a Key Vault reference keeps the secret out of the store.
- **D:** Correct. Labels keep dev, test, and prod values in one store with one key schema. A misconfigured label selector silently serves the wrong values. In this case: Labels separate agencies in one store, and a Key Vault reference keeps the secret out of the store.
- **E:** Incorrect for this question. Sentinel-key or polling refresh lets a running app pick up new settings. Refresh intervals trade responsiveness against request volume. Why the correct answer wins: Labels separate agencies in one store, and a Key Vault reference keeps the secret out of the store.

### Question 87 — A, E

Answers: Instrument the service with the OpenTelemetry SDK; Export telemetry through an OpenTelemetry collector. The OpenTelemetry SDK produces portable spans, and a collector forwards them to the approved backend. OpenTelemetry emits vendor-neutral traces, metrics, and logs with context propagation. Exporters and sampling decide what reaches the backend. A collector batches, filters, and routes telemetry, and decouples app configuration from the backend. It is another component to run and monitor. Local study-map skill 4.3 (Distributed Tracing with OpenTelemetry), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Key Vault, App Configuration, and Monitor documentation: https://learn.microsoft.com/en-us/azure/azure-monitor/

- **A:** Correct. A collector batches, filters, and routes telemetry, and decouples app configuration from the backend. It is another component to run and monitor. In this case: The OpenTelemetry SDK produces portable spans, and a collector forwards them to the approved backend.
- **B:** Incorrect for this question. Application Insights correlates requests, dependencies, and exceptions into end-to-end transactions. Sampling can hide rare failures. Why the correct answer wins: The OpenTelemetry SDK produces portable spans, and a collector forwards them to the approved backend.
- **C:** Incorrect for this question. Including the trace ID in log records lets you pivot from a failed span to its log lines. Without it, logs and traces are separate worlds. Why the correct answer wins: The OpenTelemetry SDK produces portable spans, and a collector forwards them to the approved backend.
- **D:** Incorrect for this question. Sampling keeps telemetry cost bounded, but aggressive sampling can hide rare failures. Tail sampling can retain errors preferentially. Why the correct answer wins: The OpenTelemetry SDK produces portable spans, and a collector forwards them to the approved backend.
- **E:** Correct. OpenTelemetry emits vendor-neutral traces, metrics, and logs with context propagation. Exporters and sampling decide what reaches the backend. In this case: The OpenTelemetry SDK produces portable spans, and a collector forwards them to the approved backend.

### Question 88 — C

Answer: Create the App Configuration store → add key-values with an environment label → reference the vault secret from a key value → enable refresh in the application → change the feature flag without redeploying. The store and its labelled keys exist before the secret reference, and refresh precedes a flag change without redeploy. The store, labels, and secret reference must exist before refresh can deliver a flag change without a deployment. Local study-map skill 4.2 (App Configuration Settings and Feature Flags), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Key Vault, App Configuration, and Monitor documentation: https://learn.microsoft.com/en-us/azure/azure-monitor/

- **A:** Incorrect for this question. The flag cannot change before the store holds it and the app refreshes from it. Why the correct answer wins: The store and its labelled keys exist before the secret reference, and refresh precedes a flag change without redeploy.
- **B:** Incorrect for this question. Refresh cannot be enabled against a store that does not exist yet. Why the correct answer wins: The store and its labelled keys exist before the secret reference, and refresh precedes a flag change without redeploy.
- **C:** Correct. The store, labels, and secret reference must exist before refresh can deliver a flag change without a deployment. In this case: The store and its labelled keys exist before the secret reference, and refresh precedes a flag change without redeploy.
- **D:** Incorrect for this question. Key-values must be added to a store that already exists. Why the correct answer wins: The store and its labelled keys exist before the secret reference, and refresh precedes a flag change without redeploy.

### Question 89 — B

Answer: Retrieve nearest neighbours first and discard unauthorized rows in the application. Post-filtering removes rows after selection, so the caller receives fewer results than requested. Post-filtering can return fewer results than requested and can leak existence or counts if the filtering is careless. Push authorization into the query. Local study-map skill 2.9 (PostgreSQL RAG with Metadata Filters), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Cosmos DB and PostgreSQL vector documentation: https://learn.microsoft.com/en-us/azure/cosmos-db/

- **A:** Incorrect for this question. HNSW gives fast approximate nearest-neighbour queries with a larger memory footprint and slower builds. Recall is tunable at query time. Why the correct answer wins: Post-filtering removes rows after selection, so the caller receives fewer results than requested.
- **B:** Correct. Post-filtering can return fewer results than requested and can leak existence or counts if the filtering is careless. Push authorization into the query. In this case: Post-filtering removes rows after selection, so the caller receives fewer results than requested.
- **C:** Incorrect for this question. Combining a WHERE filter with the distance operator keeps retrieval inside the caller's scope and improves relevance. Index the filter columns too. Why the correct answer wins: Post-filtering removes rows after selection, so the caller receives fewer results than requested.
- **D:** Incorrect for this question. An exact scan is accurate but scales linearly and burns compute. It is a baseline for measuring recall, not a production strategy. Why the correct answer wins: Post-filtering removes rows after selection, so the caller receives fewer results than requested.

### Question 90 — C

Answer: Inspect the dead-letter queue and resubmit corrected messages. Dead-lettering removes it from the active queue while preserving it. Dead-lettering preserves poison messages for diagnosis instead of losing them. Resubmission needs a fix and an idempotent handler. Local study-map skill 3.3 (Service Bus Dead-Lettering and Retries), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure messaging and Functions documentation: https://learn.microsoft.com/en-us/azure/service-bus-messaging/

- **A:** Incorrect for this question. A delivery cap stops infinite retries of a failing message and moves it to the dead-letter queue. The cap must exceed legitimate transient retries. Why the correct answer wins: Dead-lettering removes it from the active queue while preserving it.
- **B:** Incorrect for this question. Receive-and-delete removes the message on delivery, so a crash loses work silently. It suits telemetry, not payments. Why the correct answer wins: Dead-lettering removes it from the active queue while preserving it.
- **C:** Correct. Dead-lettering preserves poison messages for diagnosis instead of losing them. Resubmission needs a fix and an idempotent handler. In this case: Dead-lettering removes it from the active queue while preserving it.
- **D:** Incorrect for this question. Sessions give ordered, exclusive processing per session ID across competing consumers. They require session-aware senders and receivers. Why the correct answer wins: Dead-lettering removes it from the active queue while preserving it.

### Question 91 — B

Answer: Reference the Key Vault secret from an App Configuration key value. A Key Vault reference inside the App Configuration key keeps the secret out of the store. A Key Vault reference keeps non-secret settings in App Configuration while the value stays in the vault. The app identity needs both sets of permissions. Local study-map skill 4.2 (App Configuration Settings and Feature Flags), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Key Vault, App Configuration, and Monitor documentation: https://learn.microsoft.com/en-us/azure/azure-monitor/

- **A:** Incorrect for this question. A vault centralizes secret storage with access control and audit. Retrieval should use an identity, not a copied credential. Why the correct answer wins: A Key Vault reference inside the App Configuration key keeps the secret out of the store.
- **B:** Correct. A Key Vault reference keeps non-secret settings in App Configuration while the value stays in the vault. The app identity needs both sets of permissions. In this case: A Key Vault reference inside the App Configuration key keeps the secret out of the store.
- **C:** Incorrect for this question. App Configuration separates configuration from code and supports labels, feature flags, and Key Vault references. Change still needs a refresh strategy. Why the correct answer wins: A Key Vault reference inside the App Configuration key keeps the secret out of the store.
- **D:** Incorrect for this question. Application settings become environment variables for the container and can be swapped per slot. Sensitive values should still reference a vault. Why the correct answer wins: A Key Vault reference inside the App Configuration key keeps the secret out of the store.

### Question 92 — D

Answer: Test end-to-end connectivity from inside the container to each dependency. Name resolution must map to the private endpoint address inside the workload network. Reaching a dependency from the pod or replica proves DNS, egress, and firewall paths together. Host-side tests can succeed while the container path fails. Local study-map skill 1.7 (Container Logs, Events, and Connectivity), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure container hosting documentation: https://learn.microsoft.com/en-us/azure/container-apps/

- **A:** Incorrect for this question. Container Apps and AKS surface stdout logs and platform events into a workspace for KQL analysis. Verbosity and retention cost money. Why the correct answer wins: Name resolution must map to the private endpoint address inside the workload network.
- **B:** Incorrect for this question. A private endpoint needs matching name resolution or clients still resolve the public address. The zone must be linked to the workload network. Why the correct answer wins: Name resolution must map to the private endpoint address inside the workload network.
- **C:** Incorrect for this question. Readiness gates traffic until the app can serve it, and liveness restarts a wedged container. Wrong thresholds cause restart loops. Why the correct answer wins: Name resolution must map to the private endpoint address inside the workload network.
- **D:** Correct. Reaching a dependency from the pod or replica proves DNS, egress, and firewall paths together. Host-side tests can succeed while the container path fails. In this case: Name resolution must map to the private endpoint address inside the workload network.

### Question 93 — D

Answer: Subscribe to a system topic for resource events. A system topic carries resource lifecycle events such as blob creation. System topics carry Azure resource lifecycle events. Domain events that are not resource changes need a custom topic and schema. Local study-map skill 3.4 (Event Grid Filters, Custom Events, and Retries), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure messaging and Functions documentation: https://learn.microsoft.com/en-us/azure/service-bus-messaging/

- **A:** Incorrect for this question. Subject and event-type filters keep handlers focused and reduce cost. Filters are evaluated on event metadata, not payload body. Why the correct answer wins: A system topic carries resource lifecycle events such as blob creation.
- **B:** Incorrect for this question. A custom schema fits domain events that are not resource lifecycle notifications. Consumers must version the schema contract. Why the correct answer wins: A system topic carries resource lifecycle events such as blob creation.
- **C:** Incorrect for this question. Event Grid retries failed deliveries with backoff and can store undeliverable events. Handlers must still be idempotent. Why the correct answer wins: A system topic carries resource lifecycle events such as blob creation.
- **D:** Correct. System topics carry Azure resource lifecycle events. Domain events that are not resource changes need a custom topic and schema. In this case: A system topic carries resource lifecycle events such as blob creation.

### Question 94 — D

Answer: Join the requests and dependencies tables on the operation ID. Joining requests to dependencies on the operation identifier isolates the slow call. Joining request and dependency telemetry shows which downstream call fails inside a slow request. Cross-workspace joins need the right scope. Local study-map skill 4.4 (KQL Queries for Logs and Metrics), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Key Vault, App Configuration, and Monitor documentation: https://learn.microsoft.com/en-us/azure/azure-monitor/

- **A:** Incorrect for this question. Reducing columns and rows early lowers query cost and latency. Broad queries over long ranges are the usual cause of slow KQL. Why the correct answer wins: Joining requests to dependencies on the operation identifier isolates the slow call.
- **B:** Incorrect for this question. An alert turns a threshold breach into a notification or action. Thresholds need a baseline, or the alert is noise. Why the correct answer wins: Joining requests to dependencies on the operation identifier isolates the slow call.
- **C:** Incorrect for this question. Time-binned aggregation reveals the shape of an incident: a step change, a ramp, or a periodic spike. Averages alone hide short outages. Why the correct answer wins: Joining requests to dependencies on the operation identifier isolates the slow call.
- **D:** Correct. Joining request and dependency telemetry shows which downstream call fails inside a slow request. Cross-workspace joins need the right scope. In this case: Joining requests to dependencies on the operation identifier isolates the slow call.

### Question 95 — C

Answer: Create a new Container Apps revision and shift traffic between revisions. Container Apps revisions support percentage traffic allocation, which gives a measured canary and a quick reversal. Revision-based traffic splitting enables canary and blue-green releases. Revision mode and scale rules must be set deliberately. Local study-map skill 1.4 (Container Apps Deployment and Revisions), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure container hosting documentation: https://learn.microsoft.com/en-us/azure/container-apps/

- **A:** Incorrect for this question. HPA adjusts replicas from resource metrics but needs metrics-server and enough node capacity. It cannot scale to zero. Why the correct answer wins: Container Apps revisions support percentage traffic allocation, which gives a measured canary and a quick reversal.
- **B:** Incorrect for this question. A slot swap warms the new version before it takes production traffic and makes rollback a second swap. Slot-local settings must be marked sticky. Why the correct answer wins: Container Apps revisions support percentage traffic allocation, which gives a measured canary and a quick reversal.
- **C:** Correct. Revision-based traffic splitting enables canary and blue-green releases. Revision mode and scale rules must be set deliberately. In this case: Container Apps revisions support percentage traffic allocation, which gives a measured canary and a quick reversal.
- **D:** Incorrect for this question. Geo-replication reduces cross-region pull latency and gives a local copy during a regional failure. It adds cost and replication management. Why the correct answer wins: Container Apps revisions support percentage traffic allocation, which gives a measured canary and a quick reversal.

### Question 96 — B

Answer: Scale the container app on an event source with a KEDA scaler. A KEDA scaler drives replicas from the event source, so pending forms add workers and an empty queue removes them. KEDA scalers drive replica count from queue length, lag, or other event metrics, including scale to zero. Cool-down and max replicas bound the behavior. Local study-map skill 1.5 (Event-Driven Scaling with KEDA), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure container hosting documentation: https://learn.microsoft.com/en-us/azure/container-apps/

- **A:** Incorrect for this question. HPA adjusts replicas from resource metrics but needs metrics-server and enough node capacity. It cannot scale to zero. Why the correct answer wins: A KEDA scaler drives replicas from the event source, so pending forms add workers and an empty queue removes them.
- **B:** Correct. KEDA scalers drive replica count from queue length, lag, or other event metrics, including scale to zero. Cool-down and max replicas bound the behavior. In this case: A KEDA scaler drives replicas from the event source, so pending forms add workers and an empty queue removes them.
- **C:** Incorrect for this question. CPU-based scaling reacts after work is already queued and cannot scale to zero on an empty queue. It suits steady request-driven services. Why the correct answer wins: A KEDA scaler drives replicas from the event source, so pending forms add workers and an empty queue removes them.
- **D:** Incorrect for this question. Container Instances starts a single container group quickly for short tasks. It has no orchestrator-level scaling or revision model. Why the correct answer wins: A KEDA scaler drives replicas from the event source, so pending forms add workers and an empty queue removes them.

### Question 97 — C

Answer: Filter on metadata columns in the same query as the vector search. Filtering on metadata in the same statement as the distance operator keeps the result scoped and complete. Combining a WHERE filter with the distance operator keeps retrieval inside the caller's scope and improves relevance. Index the filter columns too. Local study-map skill 2.9 (PostgreSQL RAG with Metadata Filters), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Cosmos DB and PostgreSQL vector documentation: https://learn.microsoft.com/en-us/azure/cosmos-db/

- **A:** Incorrect for this question. Post-filtering can return fewer results than requested and can leak existence or counts if the filtering is careless. Push authorization into the query. Why the correct answer wins: Filtering on metadata in the same statement as the distance operator keeps the result scoped and complete.
- **B:** Incorrect for this question. HNSW gives fast approximate nearest-neighbour queries with a larger memory footprint and slower builds. Recall is tunable at query time. Why the correct answer wins: Filtering on metadata in the same statement as the distance operator keeps the result scoped and complete.
- **C:** Correct. Combining a WHERE filter with the distance operator keeps retrieval inside the caller's scope and improves relevance. Index the filter columns too. In this case: Filtering on metadata in the same statement as the distance operator keeps the result scoped and complete.
- **D:** Incorrect for this question. IVFFlat uses clustering lists and needs periodic rebuilds as data grows, but costs less memory than HNSW. Probes trade recall for speed. Why the correct answer wins: Filtering on metadata in the same statement as the distance operator keeps the result scoped and complete.

### Question 98 — C

Answer: Model typed columns for filters and one vector column for the embedding. Typed columns for collection and language beside one vector column keep predicates indexable and the contract explicit. Explicit types keep filters fast and make the embedding contract clear. Storing vectors as text defeats index use. Local study-map skill 2.6 (PostgreSQL Connection and Schema Modeling), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Cosmos DB and PostgreSQL vector documentation: https://learn.microsoft.com/en-us/azure/cosmos-db/

- **A:** Incorrect for this question. A replica offloads read traffic but introduces replication lag, which is dangerous for freshly written evidence. It does not reduce index memory pressure. Why the correct answer wins: Typed columns for collection and language beside one vector column keep predicates indexable and the contract explicit.
- **B:** Incorrect for this question. Index creation and bulk loads are I/O heavy, and throttled storage stretches maintenance windows. Storage limits are separate from compute. Why the correct answer wins: Typed columns for collection and language beside one vector column keep predicates indexable and the contract explicit.
- **C:** Correct. Explicit types keep filters fast and make the embedding contract clear. Storing vectors as text defeats index use. In this case: Typed columns for collection and language beside one vector column keep predicates indexable and the contract explicit.
- **D:** Incorrect for this question. Vector indexes are memory-hungry, so undersized compute causes swapping and slow queries. Right-size before tuning index parameters. Why the correct answer wins: Typed columns for collection and language beside one vector column keep predicates indexable and the contract explicit.

### Question 99 — A

Answer: Defer the message and retry it after the dependency recovers. A deferred message leaves the delivery rotation without counting an attempt until it is received by sequence number. A deferred message stays in the queue without consuming a delivery attempt until it is received again by sequence number. Deferral does not delay the retry by itself. Local study-map skill 3.3 (Service Bus Dead-Lettering and Retries), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure messaging and Functions documentation: https://learn.microsoft.com/en-us/azure/service-bus-messaging/

- **A:** Correct. A deferred message stays in the queue without consuming a delivery attempt until it is received again by sequence number. Deferral does not delay the retry by itself. In this case: A deferred message leaves the delivery rotation without counting an attempt until it is received by sequence number.
- **B:** Incorrect for this question. Peek-lock keeps the message locked until the handler completes it, giving at-least-once processing with retry. Lock duration must exceed processing time. Why the correct answer wins: A deferred message leaves the delivery rotation without counting an attempt until it is received by sequence number.
- **C:** Incorrect for this question. Dead-lettering preserves poison messages for diagnosis instead of losing them. Resubmission needs a fix and an idempotent handler. Why the correct answer wins: A deferred message leaves the delivery rotation without counting an attempt until it is received by sequence number.
- **D:** Incorrect for this question. A delivery cap stops infinite retries of a failing message and moves it to the dead-letter queue. The cap must exceed legitimate transient retries. Why the correct answer wins: A deferred message leaves the delivery rotation without counting an attempt until it is received by sequence number.

### Question 100 — D

Answer: Propagate trace context across every service and queue hop. Trace context must travel with the message, or the consumer starts a new trace and the chain breaks. Propagation stitches one trace across HTTP, messaging, and Functions so the whole path is visible. Missing propagation breaks the trace at that hop. Local study-map skill 4.3 (Distributed Tracing with OpenTelemetry), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Key Vault, App Configuration, and Monitor documentation: https://learn.microsoft.com/en-us/azure/azure-monitor/

- **A:** Incorrect for this question. Including the trace ID in log records lets you pivot from a failed span to its log lines. Without it, logs and traces are separate worlds. Why the correct answer wins: Trace context must travel with the message, or the consumer starts a new trace and the chain breaks.
- **B:** Incorrect for this question. Sampling keeps telemetry cost bounded, but aggressive sampling can hide rare failures. Tail sampling can retain errors preferentially. Why the correct answer wins: Trace context must travel with the message, or the consumer starts a new trace and the chain breaks.
- **C:** Incorrect for this question. A collector batches, filters, and routes telemetry, and decouples app configuration from the backend. It is another component to run and monitor. Why the correct answer wins: Trace context must travel with the message, or the consumer starts a new trace and the chain breaks.
- **D:** Correct. Propagation stitches one trace across HTTP, messaging, and Functions so the whole path is visible. Missing propagation breaks the trace at that hop. In this case: Trace context must travel with the message, or the consumer starts a new trace and the chain breaks.
