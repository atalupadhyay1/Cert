# Microsoft AI-200 — Full-Length Mock Exam 2

Azure AI Cloud Developer Associate · 50 questions · 120 minutes · passing target 700/1000

Blueprint-weighted mock exam. Item mix: 38 single-choice, 8 multi-select (selection count stated), 4 ordering items rendered as answer choices, and 2 case studies of 3 questions. Hot-area, drag-and-drop UI, labs, and adaptive problem-solution sets cannot be reproduced in a CSV; see the README for the exact fidelity boundary.

Original educational content, not actual, recalled, or copied Microsoft exam items.

## Questions

### 1. A regulated release must prove exactly which image digest ran in production when an incident is reviewed. What should the pipeline publish and deploy?

Domain: Develop containerized solutions on Azure

- A. Build and store versioned images in Azure Container Registry
- B. Replicate the registry to each deployment region
- C. Run image builds on demand or on a trigger with ACR Tasks
- D. Deploy the mutable latest tag and let the platform resolve it

### 2. A nightly job must rebuild the inference image from the main branch without any developer machine involved. What should be configured?

Domain: Develop containerized solutions on Azure

- A. Run image builds on demand or on a trigger with ACR Tasks
- B. Build and store versioned images in Azure Container Registry
- C. Apply an ACR retention policy to prune old untagged manifests
- D. Stage the change in a deployment slot and swap after verification

### 3. A small internal API must run a container with deployment slots and platform-managed patching, and no Kubernetes expertise is available. What should host it?

Domain: Develop containerized solutions on Azure

- A. Deploy the service to Azure Container Apps
- B. Deploy the image to Azure App Service as a web app
- C. Run the batch job in Azure Container Instances
- D. Deploy the workload to Azure Kubernetes Service

### 4. A new build must be warmed and verified before it receives production traffic, with an instant rollback path. What should be used?

Domain: Develop containerized solutions on Azure

- A. Stage the change in a deployment slot and swap after verification
- B. Supply configuration through App Service application settings
- C. Create a new Container Apps revision and shift traffic between revisions
- D. Deploy the mutable latest tag and let the platform resolve it

### 5. A patient-facing endpoint must respond in under a second on the first request after idle periods. Which Container Apps setting addresses that?

Domain: Develop containerized solutions on Azure

- A. Scale the container app on an event source with a KEDA scaler
- B. Rely on the horizontal pod autoscaler on CPU
- C. Set a minimum replica count above zero for the container app
- D. Create a new Container Apps revision and shift traffic between revisions

### 6. A queue-driven OCR worker must scale to zero when no documents are waiting and grow with the backlog. What should drive scaling?

Domain: Develop containerized solutions on Azure

- A. Run the batch job in Azure Container Instances
- B. Rely on the horizontal pod autoscaler on CPU
- C. Scale only on CPU utilization without an event scaler
- D. Scale the container app on an event source with a KEDA scaler

### 7. A pod is killed repeatedly because the container takes longer to start than the liveness threshold allows. What should be corrected?

Domain: Develop containerized solutions on Azure

- A. Rely on the horizontal pod autoscaler on CPU
- B. Add readiness and liveness probes to the pod specification
- C. Apply a declarative Kubernetes manifest to the cluster
- D. Run the batch job in Azure Container Instances

### 8. A Kubernetes deployment restarts pods intermittently, and the team needs the platform events and container logs in one query. What should be used?

Domain: Develop containerized solutions on Azure

- A. Send telemetry to Application Insights and inspect the transaction view
- B. Test end-to-end connectivity from inside the container to each dependency
- C. Query container logs and Kubernetes events in Log Analytics
- D. Enable diagnostic settings to route platform logs to the workspace

### 9. Which sequence correctly deploys a manifest change and verifies it?

Domain: Develop containerized solutions on Azure

- A. Write the manifest → test ingress connectivity → apply it to the cluster → wait for pod readiness
- B. Apply the manifest → write the manifest → test ingress connectivity → wait for pod readiness
- C. Write the manifest → apply it to the cluster → wait for pod readiness → test ingress connectivity
- D. Wait for pod readiness → apply the manifest → write the manifest → test ingress connectivity

### 10. A service must support a canary release and must not administer a cluster. Which two choices satisfy that? Select two.

Domain: Develop containerized solutions on Azure

- A. Deploy the service to Azure Container Apps
- B. Create a new Container Apps revision and shift traffic between revisions
- C. Run the batch job in Azure Container Instances
- D. Rely on the horizontal pod autoscaler on CPU
- E. Set a minimum replica count above zero for the container app

### 11. A deployment must be reproducible from version control and must not receive traffic before it is ready. Which two elements are required? Select two.

Domain: Develop containerized solutions on Azure

- A. Tune the scale rule cool-down period and maximum replicas
- B. Run image builds on demand or on a trigger with ACR Tasks
- C. Add readiness and liveness probes to the pod specification
- D. Run the batch job in Azure Container Instances
- E. Apply a declarative Kubernetes manifest to the cluster

### 12. Documents with variable, nested shape must be stored and queried by a patient identifier with low latency. Which store fits?

Domain: Develop AI solutions by using Azure data management services

- A. Store embeddings in PostgreSQL by using the pgvector extension
- B. Use Azure Queue Storage for the work items
- C. Store the documents in Azure Cosmos DB for NoSQL
- D. Cache responses in Azure Managed Redis

### 13. A container has a steady baseline with sharp morning peaks, and throttling appears only at peak. Which throughput setting fits best?

Domain: Develop AI solutions by using Azure data management services

- A. Index every property by using the default automatic policy
- B. Choose the account consistency level that matches the read requirement
- C. Increase provisioned throughput and watch the RU charge per query
- D. Enable autoscale throughput with a maximum RU limit

### 14. A NoSQL container holds millions of chunk embeddings and must keep memory use reasonable while serving similarity queries. Which index type should be selected?

Domain: Develop AI solutions by using Azure data management services

- A. Use the DiskANN vector index for large collections
- B. Scan every document and compute similarity in application code
- C. Create an HNSW index for low-latency approximate search
- D. Declare the embedding dimensions and vector index type on the container policy

### 15. Two processor instances must share change feed partitions without processing the same batch twice. What coordinates them?

Domain: Develop AI solutions by using Azure data management services

- A. Enable duplicate detection on the queue
- B. Run a change feed processor to react to new and updated items
- C. Use a lease container to coordinate change feed readers
- D. Enable autoscale throughput with a maximum RU limit

### 16. A memory-constrained database must hold a large vector table, and slight recall loss is acceptable. Which index type fits?

Domain: Develop AI solutions by using Azure data management services

- A. Create an HNSW index for low-latency approximate search
- B. Create an IVFFlat index to save memory on a large table
- C. Query without a vector index and let PostgreSQL scan the table
- D. Increase maintenance and query memory settings for index builds and sorts

### 17. Vector queries became slower after thousands of rows were deleted and reloaded. What maintenance should be reviewed?

Domain: Develop AI solutions by using Azure data management services

- A. Increase maintenance and query memory settings for index builds and sorts
- B. Run VACUUM and ANALYZE after bulk loads and large deletes
- C. Reuse a bounded connection pool instead of opening a connection per request
- D. Increase storage throughput for index builds and bulk loads

### 18. A serverless consumer can open hundreds of connections in a burst and exceeds the server connection limit. What should be placed in front of the database?

Domain: Develop AI solutions by using Azure data management services

- A. Place a connection pooler in front of PostgreSQL for many short-lived clients
- B. Add a read replica and send all vector queries to it
- C. Reuse a bounded connection pool instead of opening a connection per request
- D. Use prepared statements and batch round trips

### 19. Cached summaries must never be older than fifteen minutes even if invalidations fail. What should be set?

Domain: Develop AI solutions by using Azure data management services

- A. Rely on the eviction policy and skip explicit TTLs
- B. Flush the database after each deployment to guarantee fresh data
- C. Set a TTL on each cached entry
- D. Invalidate or overwrite the cache entry when the source changes

### 20. A clinician must see their own just-saved note appear on the next screen, while other screens may lag slightly. Which level fits?

Domain: Develop AI solutions by using Azure data management services

- A. Use strong consistency for every read in the account
- B. Choose the account consistency level that matches the read requirement
- C. Use eventual consistency to minimize read cost
- D. Use session consistency for reads within the same client session

### 21. A retrieval table must have fast typed filters and must not return rows the caller may not see. Which two design choices are required? Select two.

Domain: Develop AI solutions by using Azure data management services

- A. Filter on metadata columns in the same query as the vector search
- B. Add a read replica and send all vector queries to it
- C. Query without a vector index and let PostgreSQL scan the table
- D. Retrieve nearest neighbours first and discard unauthorized rows in the application
- E. Model typed columns for filters and one vector column for the embedding

### 22. Vector latency degrades because the index no longer fits in memory and sorts spill to disk. Which two adjustments address that? Select two.

Domain: Develop AI solutions by using Azure data management services

- A. Increase maintenance and query memory settings for index builds and sorts
- B. Place a connection pooler in front of PostgreSQL for many short-lived clients
- C. Scale compute and memory to fit index size and query concurrency
- D. Increase storage throughput for index builds and bulk loads
- E. Create an IVFFlat index to save memory on a large table

### 23. Which sequence correctly prepares a Cosmos DB container for vector search?

Domain: Develop AI solutions by using Azure data management services

- A. Query with VectorDistance → upsert items with embeddings → create the container with a vector policy → apply metadata filters
- B. Create the container with a vector policy → upsert items with embeddings → query with VectorDistance → apply metadata filters
- C. Apply metadata filters → query with VectorDistance → create the container with a vector policy → upsert items with embeddings
- D. Upsert items with embeddings → create the container with a vector policy → apply metadata filters → query with VectorDistance

### 24. Each intake document must be processed by exactly one worker group with crash recovery. What should be used?

Domain: Connect to and consume Azure services

- A. Queue the work on a Service Bus queue and process it with a worker
- B. Publish to a Service Bus topic with multiple subscriptions
- C. Use Azure Queue Storage for the work items
- D. Stream telemetry through Azure Event Hubs

### 25. Document events must reach indexing, redaction, and audit independently, each at its own pace. What should be used?

Domain: Connect to and consume Azure services

- A. Use Azure Queue Storage for the work items
- B. Define a custom event schema for the topic
- C. Publish to a Service Bus topic with multiple subscriptions
- D. Queue the work on a Service Bus queue and process it with a worker

### 26. Message processing is latency-bound by individual receives, and lock duration comfortably exceeds batch processing time. What can improve throughput?

Domain: Connect to and consume Azure services

- A. Use Service Bus sessions to keep related messages ordered
- B. Increase prefetch count to reduce round trips
- C. Enable duplicate detection on the queue
- D. Set a maximum delivery count and handle the dead-letter path

### 27. A handler must react to blob creation events without polling storage. What should the subscription target?

Domain: Connect to and consume Azure services

- A. Define a custom event schema for the topic
- B. Subscribe to a system topic for resource events
- C. Filter the Event Grid subscription by subject or event type
- D. Rely on Event Grid retries with a dead-letter destination

### 28. A subscription should receive only events whose subject begins with a specific department path. What should be configured?

Domain: Connect to and consume Azure services

- A. Define a custom event schema for the topic
- B. Add a SQL or correlation filter to a subscription
- C. Filter the Event Grid subscription by subject or event type
- D. Rely on Event Grid retries with a dead-letter destination

### 29. A function must write the extracted entity to Cosmos DB with minimal client code. What should be used?

Domain: Connect to and consume Azure services

- A. Bind a queue or event trigger to the function
- B. Use input and output bindings instead of hand-written SDK calls
- C. Expose the endpoint through an HTTP trigger
- D. Orchestrate the multi-step workflow with Durable Functions

### 30. A multi-step redaction workflow must survive a host restart mid-processing and resume where it stopped. What should be used?

Domain: Connect to and consume Azure services

- A. Expose the endpoint through an HTTP trigger
- B. Implement the handler as an Azure Function
- C. Orchestrate the multi-step workflow with Durable Functions
- D. Move long-running work out of the HTTP request into a queue

### 31. A function must start when a document is queued and must persist the result without custom client code. Which two features provide that? Select two.

Domain: Connect to and consume Azure services

- A. Host the function app on a premium plan with pre-warmed instances
- B. Bind a queue or event trigger to the function
- C. Expose the endpoint through an HTTP trigger
- D. Orchestrate the multi-step workflow with Durable Functions
- E. Use input and output bindings instead of hand-written SDK calls

### 32. A function must avoid cold starts and call Key Vault without storing credentials. Which two choices are required? Select two.

Domain: Connect to and consume Azure services

- A. Expose the endpoint through an HTTP trigger
- B. Orchestrate the multi-step workflow with Durable Functions
- C. Host the function app on the consumption plan
- D. Host the function app on a premium plan with pre-warmed instances
- E. Assign a managed identity to the function app and use it for downstream calls

### 33. Which sequence correctly handles a document through the intake queue?

Domain: Connect to and consume Azure services

- A. Publish the message → complete the message → receive with peek-lock → process the work → dead-letter after the delivery limit
- B. Publish the message → receive with peek-lock → process the work → complete the message → dead-letter after the delivery limit
- C. Process the work → receive with peek-lock → publish the message → complete the message → dead-letter after the delivery limit
- D. Receive with peek-lock → publish the message → complete the message → process the work → dead-letter after the delivery limit

### 34. An imaging vendor credential must be auditable, revocable, and never visible in a container image. Where should it be stored?

Domain: Secure, monitor, troubleshoot Azure solutions

- A. Store settings and feature flags in Azure App Configuration
- B. Pin the application to a specific secret version
- C. Supply configuration through App Service application settings
- D. Store the secret in Azure Key Vault and read it at runtime

### 35. Threshold values must change per environment without redeploying and without storing secrets in the store. What should be used?

Domain: Secure, monitor, troubleshoot Azure solutions

- A. Store settings and feature flags in Azure App Configuration
- B. Use App Configuration labels to separate environments
- C. Store the secret in Azure Key Vault and read it at runtime
- D. Reference the Key Vault secret from an App Configuration key value

### 36. A changed feature flag is not observed by the running app until it restarts. What should be enabled?

Domain: Secure, monitor, troubleshoot Azure solutions

- A. Enable configuration refresh so changes apply without a restart
- B. Use head or tail sampling so trace volume stays within budget
- C. Deploy the function app through a CI pipeline with app settings applied
- D. Use App Configuration labels to separate environments

### 37. One intake request crosses an API, a Service Bus queue, and a function, and the team needs the full path with timings. What should be implemented?

Domain: Secure, monitor, troubleshoot Azure solutions

- A. Enable diagnostic settings to route platform logs to the workspace
- B. Query the workspace with KQL to find the failing operation
- C. Send telemetry to Application Insights and inspect the transaction view
- D. Instrument the service with the OpenTelemetry SDK

### 38. A KQL query over thirty days scans every column and takes minutes. What should be changed first?

Domain: Secure, monitor, troubleshoot Azure solutions

- A. Project only the columns needed and filter by time first
- B. Aggregate with summarize and bin to see the failure rate over time
- C. Store repeated aggregations in a materialized view or update policy
- D. Join the requests and dependencies tables on the operation ID

### 39. The team needs p95 intake latency per hour rather than one average for the day. Which construct should be used?

Domain: Secure, monitor, troubleshoot Azure solutions

- A. Project only the columns needed and filter by time first
- B. Aggregate with summarize and bin to see the failure rate over time
- C. Store repeated aggregations in a materialized view or update policy
- D. Create an alert rule on the failure rate or latency metric

### 40. A deployment identity can modify the vault but the application only reads secrets. What should be changed?

Domain: Secure, monitor, troubleshoot Azure solutions

- A. Assign a least-privilege role to the application identity
- B. Store the secret in Azure Key Vault and read it at runtime
- C. Supply configuration through App Service application settings
- D. Authenticate with a managed identity instead of a stored key

### 41. Which sequence correctly delivers a custom document event to a subscriber?

Domain: Secure, monitor, troubleshoot Azure solutions

- A. Evaluate the subscription filter → publish a custom event → dead-letter undeliverable events → deliver to the handler → retry on failure
- B. Publish a custom event → evaluate the subscription filter → deliver to the handler → retry on failure → dead-letter undeliverable events
- C. Publish a custom event → deliver to the handler → evaluate the subscription filter → dead-letter undeliverable events → retry on failure
- D. Deliver to the handler → publish a custom event → evaluate the subscription filter → retry on failure → dead-letter undeliverable events

### 42. A handler receives at-least-once deliveries and must reject replays while still dead-lettering persistent failures. Which two mechanisms are required? Select two.

Domain: Connect to and consume Azure services

- A. Make the handler idempotent by using a message or business key
- B. Enable duplicate detection on the queue
- C. Set a maximum delivery count and handle the dead-letter path
- D. Use Service Bus sessions to keep related messages ordered
- E. Receive in receive-and-delete mode for at-most-once delivery

### 43. A request path spans an API, a queue, and a function, and the team must retain rare failures without unlimited telemetry cost. Which two practices are required? Select two.

Domain: Secure, monitor, troubleshoot Azure solutions

- A. Propagate trace context across every service and queue hop
- B. Query the workspace with KQL to find the failing operation
- C. Use head or tail sampling so trace volume stays within budget
- D. Enable diagnostic settings to route platform logs to the workspace
- E. Instrument the service with the OpenTelemetry SDK

### 44. A storage account used for extraction output must not be reachable from the public internet. What should be configured?

Domain: Secure, monitor, troubleshoot Azure solutions

- A. Authenticate with a managed identity instead of a stored key
- B. Enable diagnostic settings to route platform logs to the workspace
- C. Reach the data service through a private endpoint
- D. Assign a least-privilege role to the application identity

---

## Case study — ClaimsFlow

The next three questions refer to this scenario. Read the full scenario before answering; case-study items are scored individually.

### 45. Inside the cluster, the storage hostname resolves to a public address and connections are refused by the firewall. What should be checked?

Domain: Develop containerized solutions on Azure

- A. Reach the data service through a private endpoint
- B. Query container logs and Kubernetes events in Log Analytics
- C. Link the private DNS zone so the private endpoint name resolves
- D. Test end-to-end connectivity from inside the container to each dependency

### 46. A corrupt document repeatedly fails indexing, and the team must inspect it later without blocking the queue. What should be used?

Domain: Connect to and consume Azure services

- A. Inspect the dead-letter queue and resubmit corrected messages
- B. Receive in receive-and-delete mode for at-most-once delivery
- C. Enable duplicate detection on the queue
- D. Set a maximum delivery count and handle the dead-letter path

### 47. The secret reference fails at runtime even though the secret exists. The app already has a managed identity. What is missing?

Domain: Secure, monitor, troubleshoot Azure solutions

- A. Authenticate with a managed identity instead of a stored key
- B. Assign a least-privilege role to the application identity
- C. Enable purge protection and soft delete on the vault
- D. Grant the app identity data-plane access to the vault

---

## Case study — MedRec intake

The next three questions refer to this scenario. Read the full scenario before answering; case-study items are scored individually.

### 48. Extracted clinical entities must be filtered by site and department and also searched by meaning in one statement. What should be used?

Domain: Develop AI solutions by using Azure data management services

- A. Cache responses in Azure Managed Redis
- B. Scan every document and compute similarity in application code
- C. Store the documents in Azure Cosmos DB for NoSQL
- D. Store embeddings in PostgreSQL by using the pgvector extension

### 49. A retrieval step must return only chunks from sites the caller is assigned to, while still returning a complete result set. Where should the scope condition be applied?

Domain: Develop AI solutions by using Azure data management services

- A. Retrieve nearest neighbours first and discard unauthorized rows in the application
- B. Create an IVFFlat index to save memory on a large table
- C. Create an HNSW index for low-latency approximate search
- D. Filter on metadata columns in the same query as the vector search

### 50. Similar prior cases must be found in single-digit milliseconds, and the case corpus fits in memory. What should be used?

Domain: Develop AI solutions by using Azure data management services

- A. Cache responses in Azure Managed Redis
- B. Store user session state in Managed Redis with an expiry
- C. Use a distributed lock in Redis to make processing idempotent
- D. Create a vector index in Managed Redis for similarity search

---

## Answer key and explanations

### Question 1 — A

Answer: Build and store versioned images in Azure Container Registry. A versioned tag on a specific digest ties the running container to a reviewable artifact. ACR keeps tagged, versioned images next to the deployment target and supports identity-based pulls. Tagging strategy and retention still need a decision. Local study-map skill 1.1 (Container Image Lifecycle in Azure Container Registry), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure container hosting documentation: https://learn.microsoft.com/en-us/azure/container-apps/

- **A:** Correct. ACR keeps tagged, versioned images next to the deployment target and supports identity-based pulls. Tagging strategy and retention still need a decision. In this case: A versioned tag on a specific digest ties the running container to a reviewable artifact.
- **B:** Incorrect for this question. Geo-replication reduces cross-region pull latency and gives a local copy during a regional failure. It adds cost and replication management. Why the correct answer wins: A versioned tag on a specific digest ties the running container to a reviewable artifact.
- **C:** Incorrect for this question. ACR Tasks builds images in Azure on a commit or schedule without a local Docker host. It removes build-host drift but not image review. Why the correct answer wins: A versioned tag on a specific digest ties the running container to a reviewable artifact.
- **D:** Incorrect for this question. A floating tag removes the link between a deployed revision and a specific build, so rollback and audit become guesswork. Why the correct answer wins: A versioned tag on a specific digest ties the running container to a reviewable artifact.

### Question 2 — A

Answer: Run image builds on demand or on a trigger with ACR Tasks. An ACR Task can build on a schedule or source trigger inside Azure, so no local host participates. ACR Tasks builds images in Azure on a commit or schedule without a local Docker host. It removes build-host drift but not image review. Local study-map skill 1.2 (Automated Image Builds with ACR Tasks), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure container hosting documentation: https://learn.microsoft.com/en-us/azure/container-apps/

- **A:** Correct. ACR Tasks builds images in Azure on a commit or schedule without a local Docker host. It removes build-host drift but not image review. In this case: An ACR Task can build on a schedule or source trigger inside Azure, so no local host participates.
- **B:** Incorrect for this question. ACR keeps tagged, versioned images next to the deployment target and supports identity-based pulls. Tagging strategy and retention still need a decision. Why the correct answer wins: An ACR Task can build on a schedule or source trigger inside Azure, so no local host participates.
- **C:** Incorrect for this question. A retention policy controls storage growth and registry clutter. It does not change which image tag a deployment references. Why the correct answer wins: An ACR Task can build on a schedule or source trigger inside Azure, so no local host participates.
- **D:** Incorrect for this question. A slot swap warms the new version before it takes production traffic and makes rollback a second swap. Slot-local settings must be marked sticky. Why the correct answer wins: An ACR Task can build on a schedule or source trigger inside Azure, so no local host participates.

### Question 3 — B

Answer: Deploy the image to Azure App Service as a web app. App Service runs a container with slots and managed platform maintenance without cluster administration. App Service runs a container with managed patching, deployment slots, and built-in authentication options. It is not a Kubernetes control plane. Local study-map skill 1.3 (Container Deployment to Azure App Service), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure container hosting documentation: https://learn.microsoft.com/en-us/azure/container-apps/

- **A:** Incorrect for this question. Container Apps provides a managed environment, revisions, and KEDA-based scaling without cluster administration. Platform limits differ from AKS. Why the correct answer wins: App Service runs a container with slots and managed platform maintenance without cluster administration.
- **B:** Correct. App Service runs a container with managed patching, deployment slots, and built-in authentication options. It is not a Kubernetes control plane. In this case: App Service runs a container with slots and managed platform maintenance without cluster administration.
- **C:** Incorrect for this question. Container Instances starts a single container group quickly for short tasks. It has no orchestrator-level scaling or revision model. Why the correct answer wins: App Service runs a container with slots and managed platform maintenance without cluster administration.
- **D:** Incorrect for this question. AKS gives full Kubernetes control, including custom controllers and networking. You own node pools, upgrades, and manifest hygiene. Why the correct answer wins: App Service runs a container with slots and managed platform maintenance without cluster administration.

### Question 4 — A

Answer: Stage the change in a deployment slot and swap after verification. A slot swap warms the new version and makes rollback a second swap. A slot swap warms the new version before it takes production traffic and makes rollback a second swap. Slot-local settings must be marked sticky. Local study-map skill 1.3 (Container Deployment to Azure App Service), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure container hosting documentation: https://learn.microsoft.com/en-us/azure/container-apps/

- **A:** Correct. A slot swap warms the new version before it takes production traffic and makes rollback a second swap. Slot-local settings must be marked sticky. In this case: A slot swap warms the new version and makes rollback a second swap.
- **B:** Incorrect for this question. Application settings become environment variables for the container and can be swapped per slot. Sensitive values should still reference a vault. Why the correct answer wins: A slot swap warms the new version and makes rollback a second swap.
- **C:** Incorrect for this question. Revision-based traffic splitting enables canary and blue-green releases. Revision mode and scale rules must be set deliberately. Why the correct answer wins: A slot swap warms the new version and makes rollback a second swap.
- **D:** Incorrect for this question. A floating tag removes the link between a deployed revision and a specific build, so rollback and audit become guesswork. Why the correct answer wins: A slot swap warms the new version and makes rollback a second swap.

### Question 5 — C

Answer: Set a minimum replica count above zero for the container app. A minimum replica count above zero keeps an instance warm so the first request avoids a cold start. A warm minimum replica removes scale-to-zero cold starts for latency-critical endpoints. It keeps paying for idle capacity. Local study-map skill 1.4 (Container Apps Deployment and Revisions), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure container hosting documentation: https://learn.microsoft.com/en-us/azure/container-apps/

- **A:** Incorrect for this question. KEDA scalers drive replica count from queue length, lag, or other event metrics, including scale to zero. Cool-down and max replicas bound the behavior. Why the correct answer wins: A minimum replica count above zero keeps an instance warm so the first request avoids a cold start.
- **B:** Incorrect for this question. HPA adjusts replicas from resource metrics but needs metrics-server and enough node capacity. It cannot scale to zero. Why the correct answer wins: A minimum replica count above zero keeps an instance warm so the first request avoids a cold start.
- **C:** Correct. A warm minimum replica removes scale-to-zero cold starts for latency-critical endpoints. It keeps paying for idle capacity. In this case: A minimum replica count above zero keeps an instance warm so the first request avoids a cold start.
- **D:** Incorrect for this question. Revision-based traffic splitting enables canary and blue-green releases. Revision mode and scale rules must be set deliberately. Why the correct answer wins: A minimum replica count above zero keeps an instance warm so the first request avoids a cold start.

### Question 6 — D

Answer: Scale the container app on an event source with a KEDA scaler. A KEDA queue scaler follows backlog depth and can scale to zero. KEDA scalers drive replica count from queue length, lag, or other event metrics, including scale to zero. Cool-down and max replicas bound the behavior. Local study-map skill 1.5 (Event-Driven Scaling with KEDA), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure container hosting documentation: https://learn.microsoft.com/en-us/azure/container-apps/

- **A:** Incorrect for this question. Container Instances starts a single container group quickly for short tasks. It has no orchestrator-level scaling or revision model. Why the correct answer wins: A KEDA queue scaler follows backlog depth and can scale to zero.
- **B:** Incorrect for this question. HPA adjusts replicas from resource metrics but needs metrics-server and enough node capacity. It cannot scale to zero. Why the correct answer wins: A KEDA queue scaler follows backlog depth and can scale to zero.
- **C:** Incorrect for this question. CPU-based scaling reacts after work is already queued and cannot scale to zero on an empty queue. It suits steady request-driven services. Why the correct answer wins: A KEDA queue scaler follows backlog depth and can scale to zero.
- **D:** Correct. KEDA scalers drive replica count from queue length, lag, or other event metrics, including scale to zero. Cool-down and max replicas bound the behavior. In this case: A KEDA queue scaler follows backlog depth and can scale to zero.

### Question 7 — B

Answer: Add readiness and liveness probes to the pod specification. Startup and liveness thresholds must accommodate real initialization time, or the container is restarted before it can become healthy. Readiness gates traffic until the app can serve it, and liveness restarts a wedged container. Wrong thresholds cause restart loops. Local study-map skill 1.6 (AKS Deployment with Manifests), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure container hosting documentation: https://learn.microsoft.com/en-us/azure/container-apps/

- **A:** Incorrect for this question. HPA adjusts replicas from resource metrics but needs metrics-server and enough node capacity. It cannot scale to zero. Why the correct answer wins: Startup and liveness thresholds must accommodate real initialization time, or the container is restarted before it can become healthy.
- **B:** Correct. Readiness gates traffic until the app can serve it, and liveness restarts a wedged container. Wrong thresholds cause restart loops. In this case: Startup and liveness thresholds must accommodate real initialization time, or the container is restarted before it can become healthy.
- **C:** Incorrect for this question. A manifest declares the desired deployment, service, and probe configuration in version control. Applying it repeatedly is idempotent. Why the correct answer wins: Startup and liveness thresholds must accommodate real initialization time, or the container is restarted before it can become healthy.
- **D:** Incorrect for this question. Container Instances starts a single container group quickly for short tasks. It has no orchestrator-level scaling or revision model. Why the correct answer wins: Startup and liveness thresholds must accommodate real initialization time, or the container is restarted before it can become healthy.

### Question 8 — C

Answer: Query container logs and Kubernetes events in Log Analytics. Container logs and platform events flow into Log Analytics where KQL can correlate them. Container Apps and AKS surface stdout logs and platform events into a workspace for KQL analysis. Verbosity and retention cost money. Local study-map skill 1.7 (Container Logs, Events, and Connectivity), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure container hosting documentation: https://learn.microsoft.com/en-us/azure/container-apps/

- **A:** Incorrect for this question. Application Insights correlates requests, dependencies, and exceptions into end-to-end transactions. Sampling can hide rare failures. Why the correct answer wins: Container logs and platform events flow into Log Analytics where KQL can correlate them.
- **B:** Incorrect for this question. Reaching a dependency from the pod or replica proves DNS, egress, and firewall paths together. Host-side tests can succeed while the container path fails. Why the correct answer wins: Container logs and platform events flow into Log Analytics where KQL can correlate them.
- **C:** Correct. Container Apps and AKS surface stdout logs and platform events into a workspace for KQL analysis. Verbosity and retention cost money. In this case: Container logs and platform events flow into Log Analytics where KQL can correlate them.
- **D:** Incorrect for this question. Platform logs and metrics must be routed before they can be queried or alerted on. Retention and cost follow the workspace settings. Why the correct answer wins: Container logs and platform events flow into Log Analytics where KQL can correlate them.

### Question 9 — C

Answer: Write the manifest → apply it to the cluster → wait for pod readiness → test ingress connectivity. The manifest is authored and applied before readiness and connectivity checks are meaningful. Readiness must pass before a connectivity test proves anything, and the manifest must exist before it is applied. Local study-map skill 1.4 (Container Apps Deployment and Revisions), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure container hosting documentation: https://learn.microsoft.com/en-us/azure/container-apps/

- **A:** Incorrect for this question. Ingress cannot be tested before the workload exists in the cluster. Why the correct answer wins: The manifest is authored and applied before readiness and connectivity checks are meaningful.
- **B:** Incorrect for this question. A manifest is authored before it is applied, and connectivity is meaningless while pods are not ready. Why the correct answer wins: The manifest is authored and applied before readiness and connectivity checks are meaningful.
- **C:** Correct. Readiness must pass before a connectivity test proves anything, and the manifest must exist before it is applied. In this case: The manifest is authored and applied before readiness and connectivity checks are meaningful.
- **D:** Incorrect for this question. Pods cannot become ready before the manifest is applied. Why the correct answer wins: The manifest is authored and applied before readiness and connectivity checks are meaningful.

### Question 10 — A, B

Answers: Create a new Container Apps revision and shift traffic between revisions; Deploy the service to Azure Container Apps. Container Apps provides a managed environment, and revisions allow traffic splitting between versions. Revision-based traffic splitting enables canary and blue-green releases. Revision mode and scale rules must be set deliberately. Container Apps provides a managed environment, revisions, and KEDA-based scaling without cluster administration. Platform limits differ from AKS. Local study-map skill 1.4 (Container Apps Deployment and Revisions), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure container hosting documentation: https://learn.microsoft.com/en-us/azure/container-apps/

- **A:** Correct. Container Apps provides a managed environment, revisions, and KEDA-based scaling without cluster administration. Platform limits differ from AKS. In this case: Container Apps provides a managed environment, and revisions allow traffic splitting between versions.
- **B:** Correct. Revision-based traffic splitting enables canary and blue-green releases. Revision mode and scale rules must be set deliberately. In this case: Container Apps provides a managed environment, and revisions allow traffic splitting between versions.
- **C:** Incorrect for this question. Container Instances starts a single container group quickly for short tasks. It has no orchestrator-level scaling or revision model. Why the correct answer wins: Container Apps provides a managed environment, and revisions allow traffic splitting between versions.
- **D:** Incorrect for this question. HPA adjusts replicas from resource metrics but needs metrics-server and enough node capacity. It cannot scale to zero. Why the correct answer wins: Container Apps provides a managed environment, and revisions allow traffic splitting between versions.
- **E:** Incorrect for this question. A warm minimum replica removes scale-to-zero cold starts for latency-critical endpoints. It keeps paying for idle capacity. Why the correct answer wins: Container Apps provides a managed environment, and revisions allow traffic splitting between versions.

### Question 11 — C, E

Answers: Apply a declarative Kubernetes manifest to the cluster; Add readiness and liveness probes to the pod specification. A declarative manifest makes the deployment reproducible, and readiness probes gate traffic. A manifest declares the desired deployment, service, and probe configuration in version control. Applying it repeatedly is idempotent. Readiness gates traffic until the app can serve it, and liveness restarts a wedged container. Wrong thresholds cause restart loops. Local study-map skill 1.6 (AKS Deployment with Manifests), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure container hosting documentation: https://learn.microsoft.com/en-us/azure/container-apps/

- **A:** Incorrect for this question. Cool-down prevents replica flapping, and a maximum replica cap bounds cost and downstream load. Both are per-rule settings. Why the correct answer wins: A declarative manifest makes the deployment reproducible, and readiness probes gate traffic.
- **B:** Incorrect for this question. ACR Tasks builds images in Azure on a commit or schedule without a local Docker host. It removes build-host drift but not image review. Why the correct answer wins: A declarative manifest makes the deployment reproducible, and readiness probes gate traffic.
- **C:** Correct. Readiness gates traffic until the app can serve it, and liveness restarts a wedged container. Wrong thresholds cause restart loops. In this case: A declarative manifest makes the deployment reproducible, and readiness probes gate traffic.
- **D:** Incorrect for this question. Container Instances starts a single container group quickly for short tasks. It has no orchestrator-level scaling or revision model. Why the correct answer wins: A declarative manifest makes the deployment reproducible, and readiness probes gate traffic.
- **E:** Correct. A manifest declares the desired deployment, service, and probe configuration in version control. Applying it repeatedly is idempotent. In this case: A declarative manifest makes the deployment reproducible, and readiness probes gate traffic.

### Question 12 — C

Answer: Store the documents in Azure Cosmos DB for NoSQL. Cosmos DB for NoSQL stores flexible documents and serves low-latency keyed reads. Cosmos DB gives globally distributed, low-latency document access with tunable consistency. Partition key and RU planning determine the cost profile. Local study-map skill 2.1 (Cosmos DB SDK Access and Queries), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Cosmos DB and PostgreSQL vector documentation: https://learn.microsoft.com/en-us/azure/cosmos-db/

- **A:** Incorrect for this question. pgvector keeps vectors beside relational data, so filters and joins run in one query. Index type and parameter tuning decide latency. Why the correct answer wins: Cosmos DB for NoSQL stores flexible documents and serves low-latency keyed reads.
- **B:** Incorrect for this question. Queue Storage is simple and cheap for large backlogs with at-least-once delivery. It lacks topics, sessions, and scheduled messages. Why the correct answer wins: Cosmos DB for NoSQL stores flexible documents and serves low-latency keyed reads.
- **C:** Correct. Cosmos DB gives globally distributed, low-latency document access with tunable consistency. Partition key and RU planning determine the cost profile. In this case: Cosmos DB for NoSQL stores flexible documents and serves low-latency keyed reads.
- **D:** Incorrect for this question. A cache absorbs repeated reads and cuts latency for hot data. Cache keys, TTLs, and invalidation must match the freshness requirement. Why the correct answer wins: Cosmos DB for NoSQL stores flexible documents and serves low-latency keyed reads.

### Question 13 — D

Answer: Enable autoscale throughput with a maximum RU limit. Autoscale follows the peak while keeping the baseline low and caps the maximum spend. Autoscale follows demand between a minimum and maximum, avoiding throttling at peak without paying for peak all day. The maximum still caps the bill. Local study-map skill 2.2 (Cosmos DB Indexing Policies and Request Units), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Cosmos DB and PostgreSQL vector documentation: https://learn.microsoft.com/en-us/azure/cosmos-db/

- **A:** Incorrect for this question. Indexing everything is simple and makes ad hoc queries possible, at higher write cost and storage. It is a default, not an optimization. Why the correct answer wins: Autoscale follows the peak while keeping the baseline low and caps the maximum spend.
- **B:** Incorrect for this question. Consistency trades freshness against latency, availability, and RU cost. The level is set at the account and can be relaxed per request. Why the correct answer wins: Autoscale follows the peak while keeping the baseline low and caps the maximum spend.
- **C:** Incorrect for this question. Request units measure the work a query performs, so tuning the query is often cheaper than adding throughput. Monitor normalized RU consumption. Why the correct answer wins: Autoscale follows the peak while keeping the baseline low and caps the maximum spend.
- **D:** Correct. Autoscale follows demand between a minimum and maximum, avoiding throttling at peak without paying for peak all day. The maximum still caps the bill. In this case: Autoscale follows the peak while keeping the baseline low and caps the maximum spend.

### Question 14 — A

Answer: Use the DiskANN vector index for large collections. DiskANN targets large vector collections with better memory efficiency than an in-memory index. DiskANN trades some recall for memory efficiency on large sets. Recall and latency should be measured on representative queries. Local study-map skill 2.4 (Cosmos DB Vector Search and Embeddings), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Cosmos DB and PostgreSQL vector documentation: https://learn.microsoft.com/en-us/azure/cosmos-db/

- **A:** Correct. DiskANN trades some recall for memory efficiency on large sets. Recall and latency should be measured on representative queries. In this case: DiskANN targets large vector collections with better memory efficiency than an in-memory index.
- **B:** Incorrect for this question. Application-side scoring works for tiny collections and tests, but it moves all data over the wire and does not scale with corpus size. Why the correct answer wins: DiskANN targets large vector collections with better memory efficiency than an in-memory index.
- **C:** Incorrect for this question. HNSW gives fast approximate nearest-neighbour queries with a larger memory footprint and slower builds. Recall is tunable at query time. Why the correct answer wins: DiskANN targets large vector collections with better memory efficiency than an in-memory index.
- **D:** Incorrect for this question. The container vector policy fixes dimensions, distance function, and index type, so a model change requires a new policy. Mismatched dimensions fail at write time. Why the correct answer wins: DiskANN targets large vector collections with better memory efficiency than an in-memory index.

### Question 15 — C

Answer: Use a lease container to coordinate change feed readers. A lease container records partition ownership so instances divide the work and resume from tokens. Leases track partition ownership so multiple processor instances share work and resume from a continuation token. Lease writes consume RUs too. Local study-map skill 2.5 (Cosmos DB Change Feed Processing), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Cosmos DB and PostgreSQL vector documentation: https://learn.microsoft.com/en-us/azure/cosmos-db/

- **A:** Incorrect for this question. A duplicate-detection window drops repeated sends within the window, which helps with at-least-once producers. The window is time-bounded. Why the correct answer wins: A lease container records partition ownership so instances divide the work and resume from tokens.
- **B:** Incorrect for this question. The change feed delivers an ordered stream of changes per partition for downstream processing. It is not a delete feed, so deletions need a workaround. Why the correct answer wins: A lease container records partition ownership so instances divide the work and resume from tokens.
- **C:** Correct. Leases track partition ownership so multiple processor instances share work and resume from a continuation token. Lease writes consume RUs too. In this case: A lease container records partition ownership so instances divide the work and resume from tokens.
- **D:** Incorrect for this question. Autoscale follows demand between a minimum and maximum, avoiding throttling at peak without paying for peak all day. The maximum still caps the bill. Why the correct answer wins: A lease container records partition ownership so instances divide the work and resume from tokens.

### Question 16 — B

Answer: Create an IVFFlat index to save memory on a large table. IVFFlat uses clustering lists and needs periodic rebuilds but has a smaller memory footprint than HNSW. IVFFlat uses clustering lists and needs periodic rebuilds as data grows, but costs less memory than HNSW. Probes trade recall for speed. Local study-map skill 2.7 (pgvector Indexing and Query Latency), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Cosmos DB and PostgreSQL vector documentation: https://learn.microsoft.com/en-us/azure/cosmos-db/

- **A:** Incorrect for this question. HNSW gives fast approximate nearest-neighbour queries with a larger memory footprint and slower builds. Recall is tunable at query time. Why the correct answer wins: IVFFlat uses clustering lists and needs periodic rebuilds but has a smaller memory footprint than HNSW.
- **B:** Correct. IVFFlat uses clustering lists and needs periodic rebuilds as data grows, but costs less memory than HNSW. Probes trade recall for speed. In this case: IVFFlat uses clustering lists and needs periodic rebuilds but has a smaller memory footprint than HNSW.
- **C:** Incorrect for this question. An exact scan is accurate but scales linearly and burns compute. It is a baseline for measuring recall, not a production strategy. Why the correct answer wins: IVFFlat uses clustering lists and needs periodic rebuilds but has a smaller memory footprint than HNSW.
- **D:** Incorrect for this question. Index builds and large sorts spill to disk when work memory is too small, stretching maintenance windows and slowing queries. Why the correct answer wins: IVFFlat uses clustering lists and needs periodic rebuilds but has a smaller memory footprint than HNSW.

### Question 17 — B

Answer: Run VACUUM and ANALYZE after bulk loads and large deletes. Dead tuples and stale statistics degrade index performance until vacuum and analyze run. Statistics and dead-tuple cleanup change plan quality and index performance. Autovacuum tuning matters for churn-heavy vector tables. Local study-map skill 2.7 (pgvector Indexing and Query Latency), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Cosmos DB and PostgreSQL vector documentation: https://learn.microsoft.com/en-us/azure/cosmos-db/

- **A:** Incorrect for this question. Index builds and large sorts spill to disk when work memory is too small, stretching maintenance windows and slowing queries. Why the correct answer wins: Dead tuples and stale statistics degrade index performance until vacuum and analyze run.
- **B:** Correct. Statistics and dead-tuple cleanup change plan quality and index performance. Autovacuum tuning matters for churn-heavy vector tables. In this case: Dead tuples and stale statistics degrade index performance until vacuum and analyze run.
- **C:** Incorrect for this question. A bounded pool amortizes connection setup and protects the server from connection storms. Pool size must match server limits. Why the correct answer wins: Dead tuples and stale statistics degrade index performance until vacuum and analyze run.
- **D:** Incorrect for this question. Index creation and bulk loads are I/O heavy, and throttled storage stretches maintenance windows. Storage limits are separate from compute. Why the correct answer wins: Dead tuples and stale statistics degrade index performance until vacuum and analyze run.

### Question 18 — A

Answer: Place a connection pooler in front of PostgreSQL for many short-lived clients. An external pooler multiplexes many short-lived clients onto a bounded set of server connections. An external pooler multiplexes server connections for serverless or highly concurrent clients. Session-level features may be unavailable in transaction mode. Local study-map skill 2.10 (PostgreSQL Connection Optimization), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Cosmos DB and PostgreSQL vector documentation: https://learn.microsoft.com/en-us/azure/cosmos-db/

- **A:** Correct. An external pooler multiplexes server connections for serverless or highly concurrent clients. Session-level features may be unavailable in transaction mode. In this case: An external pooler multiplexes many short-lived clients onto a bounded set of server connections.
- **B:** Incorrect for this question. A replica offloads read traffic but introduces replication lag, which is dangerous for freshly written evidence. It does not reduce index memory pressure. Why the correct answer wins: An external pooler multiplexes many short-lived clients onto a bounded set of server connections.
- **C:** Incorrect for this question. A bounded pool amortizes connection setup and protects the server from connection storms. Pool size must match server limits. Why the correct answer wins: An external pooler multiplexes many short-lived clients onto a bounded set of server connections.
- **D:** Incorrect for this question. Prepared statements avoid repeated planning and reduce chatty network calls. They pair well with pooling but can interact with pool modes. Why the correct answer wins: An external pooler multiplexes many short-lived clients onto a bounded set of server connections.

### Question 19 — C

Answer: Set a TTL on each cached entry. A TTL bounds staleness independently of invalidation. A TTL bounds staleness and reclaims memory without a manual sweep. Too long a TTL hides source changes; too short wastes the cache. Local study-map skill 2.11 (Azure Managed Redis Caching and Invalidation), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Cosmos DB and PostgreSQL vector documentation: https://learn.microsoft.com/en-us/azure/cosmos-db/

- **A:** Incorrect for this question. Eviction protects memory but evicts unpredictably, so a hot key can vanish before its freshness bound is reached. It is not a substitute for TTL design. Why the correct answer wins: A TTL bounds staleness independently of invalidation.
- **B:** Incorrect for this question. Flushing removes all cached content at once, causing a stampede to the origin and a latency cliff. Targeted invalidation is safer. Why the correct answer wins: A TTL bounds staleness independently of invalidation.
- **C:** Correct. A TTL bounds staleness and reclaims memory without a manual sweep. Too long a TTL hides source changes; too short wastes the cache. In this case: A TTL bounds staleness independently of invalidation.
- **D:** Incorrect for this question. Write-through or explicit invalidation keeps cached answers consistent with the system of record. Without it, TTL is the only bound on staleness. Why the correct answer wins: A TTL bounds staleness independently of invalidation.

### Question 20 — D

Answer: Use session consistency for reads within the same client session. Session consistency guarantees read-your-writes within the session without global strong consistency. Session consistency guarantees monotonic reads for one session and is the common default for user-facing apps. It does not promise global freshness. Local study-map skill 2.3 (Cosmos DB Consistency Levels), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Cosmos DB and PostgreSQL vector documentation: https://learn.microsoft.com/en-us/azure/cosmos-db/

- **A:** Incorrect for this question. Strong consistency guarantees the latest committed write globally at the cost of higher latency and reduced availability during partitions. Why the correct answer wins: Session consistency guarantees read-your-writes within the session without global strong consistency.
- **B:** Incorrect for this question. Consistency trades freshness against latency, availability, and RU cost. The level is set at the account and can be relaxed per request. Why the correct answer wins: Session consistency guarantees read-your-writes within the session without global strong consistency.
- **C:** Incorrect for this question. Eventual consistency is the cheapest and most available option but returns possibly stale data. It fits non-critical counters, not balances. Why the correct answer wins: Session consistency guarantees read-your-writes within the session without global strong consistency.
- **D:** Correct. Session consistency guarantees monotonic reads for one session and is the common default for user-facing apps. It does not promise global freshness. In this case: Session consistency guarantees read-your-writes within the session without global strong consistency.

### Question 21 — A, E

Answers: Model typed columns for filters and one vector column for the embedding; Filter on metadata columns in the same query as the vector search. Typed columns make filters efficient, and filtering inside the vector query enforces scope. Explicit types keep filters fast and make the embedding contract clear. Storing vectors as text defeats index use. Combining a WHERE filter with the distance operator keeps retrieval inside the caller's scope and improves relevance. Index the filter columns too. Local study-map skill 2.6 (PostgreSQL Connection and Schema Modeling), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Cosmos DB and PostgreSQL vector documentation: https://learn.microsoft.com/en-us/azure/cosmos-db/

- **A:** Correct. Combining a WHERE filter with the distance operator keeps retrieval inside the caller's scope and improves relevance. Index the filter columns too. In this case: Typed columns make filters efficient, and filtering inside the vector query enforces scope.
- **B:** Incorrect for this question. A replica offloads read traffic but introduces replication lag, which is dangerous for freshly written evidence. It does not reduce index memory pressure. Why the correct answer wins: Typed columns make filters efficient, and filtering inside the vector query enforces scope.
- **C:** Incorrect for this question. An exact scan is accurate but scales linearly and burns compute. It is a baseline for measuring recall, not a production strategy. Why the correct answer wins: Typed columns make filters efficient, and filtering inside the vector query enforces scope.
- **D:** Incorrect for this question. Post-filtering can return fewer results than requested and can leak existence or counts if the filtering is careless. Push authorization into the query. Why the correct answer wins: Typed columns make filters efficient, and filtering inside the vector query enforces scope.
- **E:** Correct. Explicit types keep filters fast and make the embedding contract clear. Storing vectors as text defeats index use. In this case: Typed columns make filters efficient, and filtering inside the vector query enforces scope.

### Question 22 — A, C

Answers: Scale compute and memory to fit index size and query concurrency; Increase maintenance and query memory settings for index builds and sorts. Sizing compute and memory to the index working set avoids swapping, and adequate work memory stops spills. Vector indexes are memory-hungry, so undersized compute causes swapping and slow queries. Right-size before tuning index parameters. Index builds and large sorts spill to disk when work memory is too small, stretching maintenance windows and slowing queries. Local study-map skill 2.8 (PostgreSQL Compute, Memory, and Storage Sizing), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Cosmos DB and PostgreSQL vector documentation: https://learn.microsoft.com/en-us/azure/cosmos-db/

- **A:** Correct. Index builds and large sorts spill to disk when work memory is too small, stretching maintenance windows and slowing queries. In this case: Sizing compute and memory to the index working set avoids swapping, and adequate work memory stops spills.
- **B:** Incorrect for this question. An external pooler multiplexes server connections for serverless or highly concurrent clients. Session-level features may be unavailable in transaction mode. Why the correct answer wins: Sizing compute and memory to the index working set avoids swapping, and adequate work memory stops spills.
- **C:** Correct. Vector indexes are memory-hungry, so undersized compute causes swapping and slow queries. Right-size before tuning index parameters. In this case: Sizing compute and memory to the index working set avoids swapping, and adequate work memory stops spills.
- **D:** Incorrect for this question. Index creation and bulk loads are I/O heavy, and throttled storage stretches maintenance windows. Storage limits are separate from compute. Why the correct answer wins: Sizing compute and memory to the index working set avoids swapping, and adequate work memory stops spills.
- **E:** Incorrect for this question. IVFFlat uses clustering lists and needs periodic rebuilds as data grows, but costs less memory than HNSW. Probes trade recall for speed. Why the correct answer wins: Sizing compute and memory to the index working set avoids swapping, and adequate work memory stops spills.

### Question 23 — B

Answer: Create the container with a vector policy → upsert items with embeddings → query with VectorDistance → apply metadata filters. The container and vector policy must exist before embeddings are written and queried. The vector policy fixes dimensions and index type, so it must exist before vector writes and queries. Local study-map skill 2.4 (Cosmos DB Vector Search and Embeddings), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Cosmos DB and PostgreSQL vector documentation: https://learn.microsoft.com/en-us/azure/cosmos-db/

- **A:** Incorrect for this question. A similarity query needs indexed vectors, which require the container and its policy first. Why the correct answer wins: The container and vector policy must exist before embeddings are written and queried.
- **B:** Correct. The vector policy fixes dimensions and index type, so it must exist before vector writes and queries. In this case: The container and vector policy must exist before embeddings are written and queried.
- **C:** Incorrect for this question. Filtering and querying cannot precede the container and its vector data. Why the correct answer wins: The container and vector policy must exist before embeddings are written and queried.
- **D:** Incorrect for this question. Items cannot be written before the container exists with a matching vector policy. Why the correct answer wins: The container and vector policy must exist before embeddings are written and queried.

### Question 24 — A

Answer: Queue the work on a Service Bus queue and process it with a worker. A queue with peek-lock completion gives at-least-once processing and recovery after a crash. A queue decouples producers from a single consumer group and smooths bursts. Delivery semantics depend on receive mode and completion. Local study-map skill 3.1 (Service Bus Queues and Sessions), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure messaging and Functions documentation: https://learn.microsoft.com/en-us/azure/service-bus-messaging/

- **A:** Correct. A queue decouples producers from a single consumer group and smooths bursts. Delivery semantics depend on receive mode and completion. In this case: A queue with peek-lock completion gives at-least-once processing and recovery after a crash.
- **B:** Incorrect for this question. Topics fan out one message to independent subscribers, each with its own filter and dead-letter queue. Subscribers process at their own pace. Why the correct answer wins: A queue with peek-lock completion gives at-least-once processing and recovery after a crash.
- **C:** Incorrect for this question. Queue Storage is simple and cheap for large backlogs with at-least-once delivery. It lacks topics, sessions, and scheduled messages. Why the correct answer wins: A queue with peek-lock completion gives at-least-once processing and recovery after a crash.
- **D:** Incorrect for this question. Event Hubs ingests high-volume ordered streams with partitions and consumer groups. It is a streaming log, not a task queue. Why the correct answer wins: A queue with peek-lock completion gives at-least-once processing and recovery after a crash.

### Question 25 — C

Answer: Publish to a Service Bus topic with multiple subscriptions. A topic with separate subscriptions fans out one event to independent consumers. Topics fan out one message to independent subscribers, each with its own filter and dead-letter queue. Subscribers process at their own pace. Local study-map skill 3.2 (Service Bus Topics, Subscriptions, and Filters), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure messaging and Functions documentation: https://learn.microsoft.com/en-us/azure/service-bus-messaging/

- **A:** Incorrect for this question. Queue Storage is simple and cheap for large backlogs with at-least-once delivery. It lacks topics, sessions, and scheduled messages. Why the correct answer wins: A topic with separate subscriptions fans out one event to independent consumers.
- **B:** Incorrect for this question. A custom schema fits domain events that are not resource lifecycle notifications. Consumers must version the schema contract. Why the correct answer wins: A topic with separate subscriptions fans out one event to independent consumers.
- **C:** Correct. Topics fan out one message to independent subscribers, each with its own filter and dead-letter queue. Subscribers process at their own pace. In this case: A topic with separate subscriptions fans out one event to independent consumers.
- **D:** Incorrect for this question. A queue decouples producers from a single consumer group and smooths bursts. Delivery semantics depend on receive mode and completion. Why the correct answer wins: A topic with separate subscriptions fans out one event to independent consumers.

### Question 26 — B

Answer: Increase prefetch count to reduce round trips. Prefetch batches receives to cut round trips when lock duration accommodates the batch. Prefetch reduces latency per message by batching receives, at the cost of holding more locked messages. Lock duration must cover the batch. Local study-map skill 3.2 (Service Bus Topics, Subscriptions, and Filters), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure messaging and Functions documentation: https://learn.microsoft.com/en-us/azure/service-bus-messaging/

- **A:** Incorrect for this question. Sessions give ordered, exclusive processing per session ID across competing consumers. They require session-aware senders and receivers. Why the correct answer wins: Prefetch batches receives to cut round trips when lock duration accommodates the batch.
- **B:** Correct. Prefetch reduces latency per message by batching receives, at the cost of holding more locked messages. Lock duration must cover the batch. In this case: Prefetch batches receives to cut round trips when lock duration accommodates the batch.
- **C:** Incorrect for this question. A duplicate-detection window drops repeated sends within the window, which helps with at-least-once producers. The window is time-bounded. Why the correct answer wins: Prefetch batches receives to cut round trips when lock duration accommodates the batch.
- **D:** Incorrect for this question. A delivery cap stops infinite retries of a failing message and moves it to the dead-letter queue. The cap must exceed legitimate transient retries. Why the correct answer wins: Prefetch batches receives to cut round trips when lock duration accommodates the batch.

### Question 27 — B

Answer: Subscribe to a system topic for resource events. A system topic carries resource lifecycle events such as blob creation. System topics carry Azure resource lifecycle events. Domain events that are not resource changes need a custom topic and schema. Local study-map skill 3.4 (Event Grid Filters, Custom Events, and Retries), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure messaging and Functions documentation: https://learn.microsoft.com/en-us/azure/service-bus-messaging/

- **A:** Incorrect for this question. A custom schema fits domain events that are not resource lifecycle notifications. Consumers must version the schema contract. Why the correct answer wins: A system topic carries resource lifecycle events such as blob creation.
- **B:** Correct. System topics carry Azure resource lifecycle events. Domain events that are not resource changes need a custom topic and schema. In this case: A system topic carries resource lifecycle events such as blob creation.
- **C:** Incorrect for this question. Subject and event-type filters keep handlers focused and reduce cost. Filters are evaluated on event metadata, not payload body. Why the correct answer wins: A system topic carries resource lifecycle events such as blob creation.
- **D:** Incorrect for this question. Event Grid retries failed deliveries with backoff and can store undeliverable events. Handlers must still be idempotent. Why the correct answer wins: A system topic carries resource lifecycle events such as blob creation.

### Question 28 — C

Answer: Filter the Event Grid subscription by subject or event type. A subject filter matches event metadata before delivery. Subject and event-type filters keep handlers focused and reduce cost. Filters are evaluated on event metadata, not payload body. Local study-map skill 3.4 (Event Grid Filters, Custom Events, and Retries), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure messaging and Functions documentation: https://learn.microsoft.com/en-us/azure/service-bus-messaging/

- **A:** Incorrect for this question. A custom schema fits domain events that are not resource lifecycle notifications. Consumers must version the schema contract. Why the correct answer wins: A subject filter matches event metadata before delivery.
- **B:** Incorrect for this question. Subscription filters route only matching messages to a handler, reducing wasted processing. Filter evaluation happens broker-side on message properties. Why the correct answer wins: A subject filter matches event metadata before delivery.
- **C:** Correct. Subject and event-type filters keep handlers focused and reduce cost. Filters are evaluated on event metadata, not payload body. In this case: A subject filter matches event metadata before delivery.
- **D:** Incorrect for this question. Event Grid retries failed deliveries with backoff and can store undeliverable events. Handlers must still be idempotent. Why the correct answer wins: A subject filter matches event metadata before delivery.

### Question 29 — B

Answer: Use input and output bindings instead of hand-written SDK calls. An output binding declares the write target declaratively instead of hand-written SDK calls. Bindings reduce boilerplate for common inputs and outputs and are configured declaratively. Complex operations still need the SDK. Local study-map skill 3.5 (Azure Functions Triggers and Bindings), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure messaging and Functions documentation: https://learn.microsoft.com/en-us/azure/service-bus-messaging/

- **A:** Incorrect for this question. A trigger starts the function when work arrives and handles the receive loop for you. Poison-message behavior is configured in host settings. Why the correct answer wins: An output binding declares the write target declaratively instead of hand-written SDK calls.
- **B:** Correct. Bindings reduce boilerplate for common inputs and outputs and are configured declaratively. Complex operations still need the SDK. In this case: An output binding declares the write target declaratively instead of hand-written SDK calls.
- **C:** Incorrect for this question. An HTTP trigger gives a synchronous API endpoint with route and authorization configuration. Long-running work should hand off to a queue. Why the correct answer wins: An output binding declares the write target declaratively instead of hand-written SDK calls.
- **D:** Incorrect for this question. Durable Functions provides orchestrations, activities, timers, and retries with checkpointed state. Orchestrator code must stay deterministic. Why the correct answer wins: An output binding declares the write target declaratively instead of hand-written SDK calls.

### Question 30 — C

Answer: Orchestrate the multi-step workflow with Durable Functions. Durable Functions checkpoints orchestrator progress so work resumes after a restart. Durable Functions provides orchestrations, activities, timers, and retries with checkpointed state. Orchestrator code must stay deterministic. Local study-map skill 3.6 (Function App Configuration and Deployment), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure messaging and Functions documentation: https://learn.microsoft.com/en-us/azure/service-bus-messaging/

- **A:** Incorrect for this question. An HTTP trigger gives a synchronous API endpoint with route and authorization configuration. Long-running work should hand off to a queue. Why the correct answer wins: Durable Functions checkpoints orchestrator progress so work resumes after a restart.
- **B:** Incorrect for this question. Functions runs small event-driven code without managing a host. Execution limits and cold starts depend on the hosting plan. Why the correct answer wins: Durable Functions checkpoints orchestrator progress so work resumes after a restart.
- **C:** Correct. Durable Functions provides orchestrations, activities, timers, and retries with checkpointed state. Orchestrator code must stay deterministic. In this case: Durable Functions checkpoints orchestrator progress so work resumes after a restart.
- **D:** Incorrect for this question. HTTP requests have platform timeout limits, so long work belongs behind a queue or orchestration with a status endpoint. Why the correct answer wins: Durable Functions checkpoints orchestrator progress so work resumes after a restart.

### Question 31 — B, E

Answers: Bind a queue or event trigger to the function; Use input and output bindings instead of hand-written SDK calls. A queue trigger starts execution on arrival, and an output binding performs the write. A trigger starts the function when work arrives and handles the receive loop for you. Poison-message behavior is configured in host settings. Bindings reduce boilerplate for common inputs and outputs and are configured declaratively. Complex operations still need the SDK. Local study-map skill 3.5 (Azure Functions Triggers and Bindings), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure messaging and Functions documentation: https://learn.microsoft.com/en-us/azure/service-bus-messaging/

- **A:** Incorrect for this question. A premium plan reduces cold starts and supports virtual network integration and longer timeouts. It costs more than consumption. Why the correct answer wins: A queue trigger starts execution on arrival, and an output binding performs the write.
- **B:** Correct. A trigger starts the function when work arrives and handles the receive loop for you. Poison-message behavior is configured in host settings. In this case: A queue trigger starts execution on arrival, and an output binding performs the write.
- **C:** Incorrect for this question. An HTTP trigger gives a synchronous API endpoint with route and authorization configuration. Long-running work should hand off to a queue. Why the correct answer wins: A queue trigger starts execution on arrival, and an output binding performs the write.
- **D:** Incorrect for this question. Durable Functions provides orchestrations, activities, timers, and retries with checkpointed state. Orchestrator code must stay deterministic. Why the correct answer wins: A queue trigger starts execution on arrival, and an output binding performs the write.
- **E:** Correct. Bindings reduce boilerplate for common inputs and outputs and are configured declaratively. Complex operations still need the SDK. In this case: A queue trigger starts execution on arrival, and an output binding performs the write.

### Question 32 — D, E

Answers: Host the function app on a premium plan with pre-warmed instances; Assign a managed identity to the function app and use it for downstream calls. A premium plan provides pre-warmed instances, and a managed identity removes stored credentials. A premium plan reduces cold starts and supports virtual network integration and longer timeouts. It costs more than consumption. A function app can authenticate with a managed identity, so no connection secret is needed in app settings. Local study-map skill 3.6 (Function App Configuration and Deployment), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure messaging and Functions documentation: https://learn.microsoft.com/en-us/azure/service-bus-messaging/

- **A:** Incorrect for this question. An HTTP trigger gives a synchronous API endpoint with route and authorization configuration. Long-running work should hand off to a queue. Why the correct answer wins: A premium plan provides pre-warmed instances, and a managed identity removes stored credentials.
- **B:** Incorrect for this question. Durable Functions provides orchestrations, activities, timers, and retries with checkpointed state. Orchestrator code must stay deterministic. Why the correct answer wins: A premium plan provides pre-warmed instances, and a managed identity removes stored credentials.
- **C:** Incorrect for this question. Consumption bills per execution and scales automatically, with cold starts and a timeout ceiling. It fits spiky, short work. Why the correct answer wins: A premium plan provides pre-warmed instances, and a managed identity removes stored credentials.
- **D:** Correct. A premium plan reduces cold starts and supports virtual network integration and longer timeouts. It costs more than consumption. In this case: A premium plan provides pre-warmed instances, and a managed identity removes stored credentials.
- **E:** Correct. A function app can authenticate with a managed identity, so no connection secret is needed in app settings. In this case: A premium plan provides pre-warmed instances, and a managed identity removes stored credentials.

### Question 33 — B

Answer: Publish the message → receive with peek-lock → process the work → complete the message → dead-letter after the delivery limit. Receive, process, complete, and dead-letter only after the delivery limit is exhausted. Peek-lock keeps the message until the handler succeeds, and only repeated failures should dead-letter it. Local study-map skill 3.1 (Service Bus Queues and Sessions), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure messaging and Functions documentation: https://learn.microsoft.com/en-us/azure/service-bus-messaging/

- **A:** Incorrect for this question. Completing a message before processing discards the work and defeats at-least-once delivery. Why the correct answer wins: Receive, process, complete, and dead-letter only after the delivery limit is exhausted.
- **B:** Correct. Peek-lock keeps the message until the handler succeeds, and only repeated failures should dead-letter it. In this case: Receive, process, complete, and dead-letter only after the delivery limit is exhausted.
- **C:** Incorrect for this question. Work cannot be processed before the message is published and received. Why the correct answer wins: Receive, process, complete, and dead-letter only after the delivery limit is exhausted.
- **D:** Incorrect for this question. The message cannot be received before it is published, and completion must follow processing. Why the correct answer wins: Receive, process, complete, and dead-letter only after the delivery limit is exhausted.

### Question 34 — D

Answer: Store the secret in Azure Key Vault and read it at runtime. Key Vault provides audited, access-controlled secret storage. A vault centralizes secret storage with access control and audit. Retrieval should use an identity, not a copied credential. Local study-map skill 4.1 (Key Vault Secret Storage, Rotation, and Retrieval), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Key Vault, App Configuration, and Monitor documentation: https://learn.microsoft.com/en-us/azure/azure-monitor/

- **A:** Incorrect for this question. App Configuration separates configuration from code and supports labels, feature flags, and Key Vault references. Change still needs a refresh strategy. Why the correct answer wins: Key Vault provides audited, access-controlled secret storage.
- **B:** Incorrect for this question. Pinning a version makes a rotation invisible to the app until it is redeployed, which is useful for break-glass and dangerous for routine rotation. Why the correct answer wins: Key Vault provides audited, access-controlled secret storage.
- **C:** Incorrect for this question. Application settings become environment variables for the container and can be swapped per slot. Sensitive values should still reference a vault. Why the correct answer wins: Key Vault provides audited, access-controlled secret storage.
- **D:** Correct. A vault centralizes secret storage with access control and audit. Retrieval should use an identity, not a copied credential. In this case: Key Vault provides audited, access-controlled secret storage.

### Question 35 — A

Answer: Store settings and feature flags in Azure App Configuration. App Configuration holds non-secret settings with environment labels and refresh. App Configuration separates configuration from code and supports labels, feature flags, and Key Vault references. Change still needs a refresh strategy. Local study-map skill 4.2 (App Configuration Settings and Feature Flags), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Key Vault, App Configuration, and Monitor documentation: https://learn.microsoft.com/en-us/azure/azure-monitor/

- **A:** Correct. App Configuration separates configuration from code and supports labels, feature flags, and Key Vault references. Change still needs a refresh strategy. In this case: App Configuration holds non-secret settings with environment labels and refresh.
- **B:** Incorrect for this question. Labels keep dev, test, and prod values in one store with one key schema. A misconfigured label selector silently serves the wrong values. Why the correct answer wins: App Configuration holds non-secret settings with environment labels and refresh.
- **C:** Incorrect for this question. A vault centralizes secret storage with access control and audit. Retrieval should use an identity, not a copied credential. Why the correct answer wins: App Configuration holds non-secret settings with environment labels and refresh.
- **D:** Incorrect for this question. A Key Vault reference keeps non-secret settings in App Configuration while the value stays in the vault. The app identity needs both sets of permissions. Why the correct answer wins: App Configuration holds non-secret settings with environment labels and refresh.

### Question 36 — A

Answer: Enable configuration refresh so changes apply without a restart. Configuration refresh lets a running app poll and apply changes. Sentinel-key or polling refresh lets a running app pick up new settings. Refresh intervals trade responsiveness against request volume. Local study-map skill 4.2 (App Configuration Settings and Feature Flags), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Key Vault, App Configuration, and Monitor documentation: https://learn.microsoft.com/en-us/azure/azure-monitor/

- **A:** Correct. Sentinel-key or polling refresh lets a running app pick up new settings. Refresh intervals trade responsiveness against request volume. In this case: Configuration refresh lets a running app poll and apply changes.
- **B:** Incorrect for this question. Sampling keeps telemetry cost bounded, but aggressive sampling can hide rare failures. Tail sampling can retain errors preferentially. Why the correct answer wins: Configuration refresh lets a running app poll and apply changes.
- **C:** Incorrect for this question. Pipeline deployment keeps code and configuration versioned together and repeatable. Secrets belong in a vault reference, not in the pipeline file. Why the correct answer wins: Configuration refresh lets a running app poll and apply changes.
- **D:** Incorrect for this question. Labels keep dev, test, and prod values in one store with one key schema. A misconfigured label selector silently serves the wrong values. Why the correct answer wins: Configuration refresh lets a running app poll and apply changes.

### Question 37 — D

Answer: Instrument the service with the OpenTelemetry SDK. OpenTelemetry tracing with propagation across each hop yields one end-to-end trace. OpenTelemetry emits vendor-neutral traces, metrics, and logs with context propagation. Exporters and sampling decide what reaches the backend. Local study-map skill 4.3 (Distributed Tracing with OpenTelemetry), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Key Vault, App Configuration, and Monitor documentation: https://learn.microsoft.com/en-us/azure/azure-monitor/

- **A:** Incorrect for this question. Platform logs and metrics must be routed before they can be queried or alerted on. Retention and cost follow the workspace settings. Why the correct answer wins: OpenTelemetry tracing with propagation across each hop yields one end-to-end trace.
- **B:** Incorrect for this question. KQL filters, projects, and aggregates log and metric tables in Log Analytics. Start narrow with a time range and a request ID. Why the correct answer wins: OpenTelemetry tracing with propagation across each hop yields one end-to-end trace.
- **C:** Incorrect for this question. Application Insights correlates requests, dependencies, and exceptions into end-to-end transactions. Sampling can hide rare failures. Why the correct answer wins: OpenTelemetry tracing with propagation across each hop yields one end-to-end trace.
- **D:** Correct. OpenTelemetry emits vendor-neutral traces, metrics, and logs with context propagation. Exporters and sampling decide what reaches the backend. In this case: OpenTelemetry tracing with propagation across each hop yields one end-to-end trace.

### Question 38 — A

Answer: Project only the columns needed and filter by time first. Filtering by time and projecting only needed columns reduces scanned data. Reducing columns and rows early lowers query cost and latency. Broad queries over long ranges are the usual cause of slow KQL. Local study-map skill 4.4 (KQL Queries for Logs and Metrics), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Key Vault, App Configuration, and Monitor documentation: https://learn.microsoft.com/en-us/azure/azure-monitor/

- **A:** Correct. Reducing columns and rows early lowers query cost and latency. Broad queries over long ranges are the usual cause of slow KQL. In this case: Filtering by time and projecting only needed columns reduces scanned data.
- **B:** Incorrect for this question. Time-binned aggregation reveals the shape of an incident: a step change, a ramp, or a periodic spike. Averages alone hide short outages. Why the correct answer wins: Filtering by time and projecting only needed columns reduces scanned data.
- **C:** Incorrect for this question. Precomputed results avoid recomputing expensive aggregations on every dashboard refresh. The trade-off is storage and freshness lag. Why the correct answer wins: Filtering by time and projecting only needed columns reduces scanned data.
- **D:** Incorrect for this question. Joining request and dependency telemetry shows which downstream call fails inside a slow request. Cross-workspace joins need the right scope. Why the correct answer wins: Filtering by time and projecting only needed columns reduces scanned data.

### Question 39 — B

Answer: Aggregate with summarize and bin to see the failure rate over time. Binning with summarize produces per-window percentiles. Time-binned aggregation reveals the shape of an incident: a step change, a ramp, or a periodic spike. Averages alone hide short outages. Local study-map skill 4.4 (KQL Queries for Logs and Metrics), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Key Vault, App Configuration, and Monitor documentation: https://learn.microsoft.com/en-us/azure/azure-monitor/

- **A:** Incorrect for this question. Reducing columns and rows early lowers query cost and latency. Broad queries over long ranges are the usual cause of slow KQL. Why the correct answer wins: Binning with summarize produces per-window percentiles.
- **B:** Correct. Time-binned aggregation reveals the shape of an incident: a step change, a ramp, or a periodic spike. Averages alone hide short outages. In this case: Binning with summarize produces per-window percentiles.
- **C:** Incorrect for this question. Precomputed results avoid recomputing expensive aggregations on every dashboard refresh. The trade-off is storage and freshness lag. Why the correct answer wins: Binning with summarize produces per-window percentiles.
- **D:** Incorrect for this question. An alert turns a threshold breach into a notification or action. Thresholds need a baseline, or the alert is noise. Why the correct answer wins: Binning with summarize produces per-window percentiles.

### Question 40 — A

Answer: Assign a least-privilege role to the application identity. A separate least-privilege identity or role scope should limit the app to read operations. A scoped role grants only the operations the app performs and limits blast radius. Prefer built-in roles over broad contributor grants. Local study-map skill 4.5 (Identity-Based Access for Application Services), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Key Vault, App Configuration, and Monitor documentation: https://learn.microsoft.com/en-us/azure/azure-monitor/

- **A:** Correct. A scoped role grants only the operations the app performs and limits blast radius. Prefer built-in roles over broad contributor grants. In this case: A separate least-privilege identity or role scope should limit the app to read operations.
- **B:** Incorrect for this question. A vault centralizes secret storage with access control and audit. Retrieval should use an identity, not a copied credential. Why the correct answer wins: A separate least-privilege identity or role scope should limit the app to read operations.
- **C:** Incorrect for this question. Application settings become environment variables for the container and can be swapped per slot. Sensitive values should still reference a vault. Why the correct answer wins: A separate least-privilege identity or role scope should limit the app to read operations.
- **D:** Incorrect for this question. A managed identity issues tokens from the platform, removing secret distribution from the app. Role assignment still scopes what it can reach. Why the correct answer wins: A separate least-privilege identity or role scope should limit the app to read operations.

### Question 41 — B

Answer: Publish a custom event → evaluate the subscription filter → deliver to the handler → retry on failure → dead-letter undeliverable events. Filtering precedes delivery, retries precede dead-lettering, and everything follows publication. Filtering happens before delivery, retries handle transient failures, and dead-lettering preserves what cannot be delivered. Local study-map skill 4.4 (KQL Queries for Logs and Metrics), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Key Vault, App Configuration, and Monitor documentation: https://learn.microsoft.com/en-us/azure/azure-monitor/

- **A:** Incorrect for this question. A filter cannot evaluate an event that has not been published. Why the correct answer wins: Filtering precedes delivery, retries precede dead-lettering, and everything follows publication.
- **B:** Correct. Filtering happens before delivery, retries handle transient failures, and dead-lettering preserves what cannot be delivered. In this case: Filtering precedes delivery, retries precede dead-lettering, and everything follows publication.
- **C:** Incorrect for this question. A filter is evaluated before delivery, and retries must occur before dead-lettering. Why the correct answer wins: Filtering precedes delivery, retries precede dead-lettering, and everything follows publication.
- **D:** Incorrect for this question. Delivery cannot precede publication and filtering. Why the correct answer wins: Filtering precedes delivery, retries precede dead-lettering, and everything follows publication.

### Question 42 — A, C

Answers: Make the handler idempotent by using a message or business key; Set a maximum delivery count and handle the dead-letter path. An idempotency key makes replays harmless, and a delivery limit moves persistent failures to the dead-letter queue. At-least-once delivery means duplicates will happen, so the write must tolerate replay. A stored key makes the retry safe. A delivery cap stops infinite retries of a failing message and moves it to the dead-letter queue. The cap must exceed legitimate transient retries. Local study-map skill 3.3 (Service Bus Dead-Lettering and Retries), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure messaging and Functions documentation: https://learn.microsoft.com/en-us/azure/service-bus-messaging/

- **A:** Correct. At-least-once delivery means duplicates will happen, so the write must tolerate replay. A stored key makes the retry safe. In this case: An idempotency key makes replays harmless, and a delivery limit moves persistent failures to the dead-letter queue.
- **B:** Incorrect for this question. A duplicate-detection window drops repeated sends within the window, which helps with at-least-once producers. The window is time-bounded. Why the correct answer wins: An idempotency key makes replays harmless, and a delivery limit moves persistent failures to the dead-letter queue.
- **C:** Correct. A delivery cap stops infinite retries of a failing message and moves it to the dead-letter queue. The cap must exceed legitimate transient retries. In this case: An idempotency key makes replays harmless, and a delivery limit moves persistent failures to the dead-letter queue.
- **D:** Incorrect for this question. Sessions give ordered, exclusive processing per session ID across competing consumers. They require session-aware senders and receivers. Why the correct answer wins: An idempotency key makes replays harmless, and a delivery limit moves persistent failures to the dead-letter queue.
- **E:** Incorrect for this question. Receive-and-delete removes the message on delivery, so a crash loses work silently. It suits telemetry, not payments. Why the correct answer wins: An idempotency key makes replays harmless, and a delivery limit moves persistent failures to the dead-letter queue.

### Question 43 — A, E

Answers: Instrument the service with the OpenTelemetry SDK; Propagate trace context across every service and queue hop. Context propagation connects the hops into one trace, and sampling keeps volume bounded while retaining errors when tail sampling is used. OpenTelemetry emits vendor-neutral traces, metrics, and logs with context propagation. Exporters and sampling decide what reaches the backend. Propagation stitches one trace across HTTP, messaging, and Functions so the whole path is visible. Missing propagation breaks the trace at that hop. Local study-map skill 4.3 (Distributed Tracing with OpenTelemetry), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Key Vault, App Configuration, and Monitor documentation: https://learn.microsoft.com/en-us/azure/azure-monitor/

- **A:** Correct. Propagation stitches one trace across HTTP, messaging, and Functions so the whole path is visible. Missing propagation breaks the trace at that hop. In this case: Context propagation connects the hops into one trace, and sampling keeps volume bounded while retaining errors when tail sampling is used.
- **B:** Incorrect for this question. KQL filters, projects, and aggregates log and metric tables in Log Analytics. Start narrow with a time range and a request ID. Why the correct answer wins: Context propagation connects the hops into one trace, and sampling keeps volume bounded while retaining errors when tail sampling is used.
- **C:** Incorrect for this question. Sampling keeps telemetry cost bounded, but aggressive sampling can hide rare failures. Tail sampling can retain errors preferentially. Why the correct answer wins: Context propagation connects the hops into one trace, and sampling keeps volume bounded while retaining errors when tail sampling is used.
- **D:** Incorrect for this question. Platform logs and metrics must be routed before they can be queried or alerted on. Retention and cost follow the workspace settings. Why the correct answer wins: Context propagation connects the hops into one trace, and sampling keeps volume bounded while retaining errors when tail sampling is used.
- **E:** Correct. OpenTelemetry emits vendor-neutral traces, metrics, and logs with context propagation. Exporters and sampling decide what reaches the backend. In this case: Context propagation connects the hops into one trace, and sampling keeps volume bounded while retaining errors when tail sampling is used.

### Question 44 — C

Answer: Reach the data service through a private endpoint. A private endpoint with public access disabled keeps traffic on the workload network, provided DNS resolves to the private zone. A private endpoint keeps traffic on the virtual network and removes public exposure. DNS resolution must be wired to the private zone. Local study-map skill 4.5 (Identity-Based Access for Application Services), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Key Vault, App Configuration, and Monitor documentation: https://learn.microsoft.com/en-us/azure/azure-monitor/

- **A:** Incorrect for this question. A managed identity issues tokens from the platform, removing secret distribution from the app. Role assignment still scopes what it can reach. Why the correct answer wins: A private endpoint with public access disabled keeps traffic on the workload network, provided DNS resolves to the private zone.
- **B:** Incorrect for this question. Platform logs and metrics must be routed before they can be queried or alerted on. Retention and cost follow the workspace settings. Why the correct answer wins: A private endpoint with public access disabled keeps traffic on the workload network, provided DNS resolves to the private zone.
- **C:** Correct. A private endpoint keeps traffic on the virtual network and removes public exposure. DNS resolution must be wired to the private zone. In this case: A private endpoint with public access disabled keeps traffic on the workload network, provided DNS resolves to the private zone.
- **D:** Incorrect for this question. A scoped role grants only the operations the app performs and limits blast radius. Prefer built-in roles over broad contributor grants. Why the correct answer wins: A private endpoint with public access disabled keeps traffic on the workload network, provided DNS resolves to the private zone.

### Question 45 — D

Answer: Test end-to-end connectivity from inside the container to each dependency. Name resolution inside the workload network must point at the private endpoint address, otherwise traffic leaves on the wrong path. Reaching a dependency from the pod or replica proves DNS, egress, and firewall paths together. Host-side tests can succeed while the container path fails. Local study-map skill 1.7 (Container Logs, Events, and Connectivity), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure container hosting documentation: https://learn.microsoft.com/en-us/azure/container-apps/

- **A:** Incorrect for this question. A private endpoint keeps traffic on the virtual network and removes public exposure. DNS resolution must be wired to the private zone. Why the correct answer wins: Name resolution inside the workload network must point at the private endpoint address, otherwise traffic leaves on the wrong path.
- **B:** Incorrect for this question. Container Apps and AKS surface stdout logs and platform events into a workspace for KQL analysis. Verbosity and retention cost money. Why the correct answer wins: Name resolution inside the workload network must point at the private endpoint address, otherwise traffic leaves on the wrong path.
- **C:** Incorrect for this question. A private endpoint needs matching name resolution or clients still resolve the public address. The zone must be linked to the workload network. Why the correct answer wins: Name resolution inside the workload network must point at the private endpoint address, otherwise traffic leaves on the wrong path.
- **D:** Correct. Reaching a dependency from the pod or replica proves DNS, egress, and firewall paths together. Host-side tests can succeed while the container path fails. In this case: Name resolution inside the workload network must point at the private endpoint address, otherwise traffic leaves on the wrong path.

### Question 46 — A

Answer: Inspect the dead-letter queue and resubmit corrected messages. Dead-lettering preserves the poison message for diagnosis while the queue keeps moving. Dead-lettering preserves poison messages for diagnosis instead of losing them. Resubmission needs a fix and an idempotent handler. Local study-map skill 3.3 (Service Bus Dead-Lettering and Retries), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure messaging and Functions documentation: https://learn.microsoft.com/en-us/azure/service-bus-messaging/

- **A:** Correct. Dead-lettering preserves poison messages for diagnosis instead of losing them. Resubmission needs a fix and an idempotent handler. In this case: Dead-lettering preserves the poison message for diagnosis while the queue keeps moving.
- **B:** Incorrect for this question. Receive-and-delete removes the message on delivery, so a crash loses work silently. It suits telemetry, not payments. Why the correct answer wins: Dead-lettering preserves the poison message for diagnosis while the queue keeps moving.
- **C:** Incorrect for this question. A duplicate-detection window drops repeated sends within the window, which helps with at-least-once producers. The window is time-bounded. Why the correct answer wins: Dead-lettering preserves the poison message for diagnosis while the queue keeps moving.
- **D:** Incorrect for this question. A delivery cap stops infinite retries of a failing message and moves it to the dead-letter queue. The cap must exceed legitimate transient retries. Why the correct answer wins: Dead-lettering preserves the poison message for diagnosis while the queue keeps moving.

### Question 47 — D

Answer: Grant the app identity data-plane access to the vault. The identity needs a data-plane role or policy on the vault before it can read the secret. Vault access is a separate authorization decision from the app identity. Without a data-plane role or policy the reference fails at runtime. Local study-map skill 4.1 (Key Vault Secret Storage, Rotation, and Retrieval), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Key Vault, App Configuration, and Monitor documentation: https://learn.microsoft.com/en-us/azure/azure-monitor/

- **A:** Incorrect for this question. A managed identity issues tokens from the platform, removing secret distribution from the app. Role assignment still scopes what it can reach. Why the correct answer wins: The identity needs a data-plane role or policy on the vault before it can read the secret.
- **B:** Incorrect for this question. A scoped role grants only the operations the app performs and limits blast radius. Prefer built-in roles over broad contributor grants. Why the correct answer wins: The identity needs a data-plane role or policy on the vault before it can read the secret.
- **C:** Incorrect for this question. Soft delete and purge protection stop accidental or malicious permanent loss of secrets. They also constrain how names can be reused. Why the correct answer wins: The identity needs a data-plane role or policy on the vault before it can read the secret.
- **D:** Correct. Vault access is a separate authorization decision from the app identity. Without a data-plane role or policy the reference fails at runtime. In this case: The identity needs a data-plane role or policy on the vault before it can read the secret.

### Question 48 — D

Answer: Store embeddings in PostgreSQL by using the pgvector extension. pgvector keeps embeddings beside relational columns so filters and similarity run in one query. pgvector keeps vectors beside relational data, so filters and joins run in one query. Index type and parameter tuning decide latency. Local study-map skill 2.6 (PostgreSQL Connection and Schema Modeling), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Cosmos DB and PostgreSQL vector documentation: https://learn.microsoft.com/en-us/azure/cosmos-db/

- **A:** Incorrect for this question. A cache absorbs repeated reads and cuts latency for hot data. Cache keys, TTLs, and invalidation must match the freshness requirement. Why the correct answer wins: pgvector keeps embeddings beside relational columns so filters and similarity run in one query.
- **B:** Incorrect for this question. Application-side scoring works for tiny collections and tests, but it moves all data over the wire and does not scale with corpus size. Why the correct answer wins: pgvector keeps embeddings beside relational columns so filters and similarity run in one query.
- **C:** Incorrect for this question. Cosmos DB gives globally distributed, low-latency document access with tunable consistency. Partition key and RU planning determine the cost profile. Why the correct answer wins: pgvector keeps embeddings beside relational columns so filters and similarity run in one query.
- **D:** Correct. pgvector keeps vectors beside relational data, so filters and joins run in one query. Index type and parameter tuning decide latency. In this case: pgvector keeps embeddings beside relational columns so filters and similarity run in one query.

### Question 49 — D

Answer: Filter on metadata columns in the same query as the vector search. Filtering on metadata in the same query as the distance operator keeps results in scope and the count complete. Combining a WHERE filter with the distance operator keeps retrieval inside the caller's scope and improves relevance. Index the filter columns too. Local study-map skill 2.9 (PostgreSQL RAG with Metadata Filters), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Cosmos DB and PostgreSQL vector documentation: https://learn.microsoft.com/en-us/azure/cosmos-db/

- **A:** Incorrect for this question. Post-filtering can return fewer results than requested and can leak existence or counts if the filtering is careless. Push authorization into the query. Why the correct answer wins: Filtering on metadata in the same query as the distance operator keeps results in scope and the count complete.
- **B:** Incorrect for this question. IVFFlat uses clustering lists and needs periodic rebuilds as data grows, but costs less memory than HNSW. Probes trade recall for speed. Why the correct answer wins: Filtering on metadata in the same query as the distance operator keeps results in scope and the count complete.
- **C:** Incorrect for this question. HNSW gives fast approximate nearest-neighbour queries with a larger memory footprint and slower builds. Recall is tunable at query time. Why the correct answer wins: Filtering on metadata in the same query as the distance operator keeps results in scope and the count complete.
- **D:** Correct. Combining a WHERE filter with the distance operator keeps retrieval inside the caller's scope and improves relevance. Index the filter columns too. In this case: Filtering on metadata in the same query as the distance operator keeps results in scope and the count complete.

### Question 50 — D

Answer: Create a vector index in Managed Redis for similarity search. A Redis vector index serves similarity queries from memory at low latency. Redis vector search serves low-latency similarity queries from memory. The corpus must fit the memory budget and be rebuilt on model change. Local study-map skill 2.12 (Azure Managed Redis Vector Indexing), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Cosmos DB and PostgreSQL vector documentation: https://learn.microsoft.com/en-us/azure/cosmos-db/

- **A:** Incorrect for this question. A cache absorbs repeated reads and cuts latency for hot data. Cache keys, TTLs, and invalidation must match the freshness requirement. Why the correct answer wins: A Redis vector index serves similarity queries from memory at low latency.
- **B:** Incorrect for this question. Session storage in Redis survives instance restarts and supports distributed instances. Sessions must be scoped and expiring. Why the correct answer wins: A Redis vector index serves similarity queries from memory at low latency.
- **C:** Incorrect for this question. A lock can serialize work across instances, but correctness under retries still needs idempotency keys in the data store. Locks expire and can be lost. Why the correct answer wins: A Redis vector index serves similarity queries from memory at low latency.
- **D:** Correct. Redis vector search serves low-latency similarity queries from memory. The corpus must fit the memory budget and be rebuilt on model change. In this case: A Redis vector index serves similarity queries from memory at low latency.
