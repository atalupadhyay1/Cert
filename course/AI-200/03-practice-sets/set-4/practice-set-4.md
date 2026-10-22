# Microsoft AI-200 — Full-Length Mock Exam 4

Azure AI Cloud Developer Associate · 50 questions · 120 minutes · passing target 700/1000

Blueprint-weighted mock exam. Item mix: 38 single-choice, 8 multi-select (selection count stated), 4 ordering items rendered as answer choices, and 2 case studies of 3 questions. Hot-area, drag-and-drop UI, labs, and adaptive problem-solution sets cannot be reproduced in a CSV; see the README for the exact fidelity boundary.

Original educational content, not actual, recalled, or copied Microsoft exam items.

## Questions

### 1. Inspection images must be pulled locally at each plant within the same region as the cluster. What should be configured?

Domain: Develop containerized solutions on Azure

- A. Replicate the registry to each deployment region
- B. Run image builds on demand or on a trigger with ACR Tasks
- C. Apply an ACR retention policy to prune old untagged manifests
- D. Deploy the mutable latest tag and let the platform resolve it

### 2. After a year of nightly builds the registry holds thousands of superseded manifests and costs are rising. What should be applied?

Domain: Develop containerized solutions on Azure

- A. Run image builds on demand or on a trigger with ACR Tasks
- B. Apply an ACR retention policy to prune old untagged manifests
- C. Deploy the mutable latest tag and let the platform resolve it
- D. Replicate the registry to each deployment region

### 3. A commit to the inspection repository must produce a new image without any engineer running a build. What should be configured?

Domain: Develop containerized solutions on Azure

- A. Build and store versioned images in Azure Container Registry
- B. Run the batch job in Azure Container Instances
- C. Run image builds on demand or on a trigger with ACR Tasks
- D. Stage the change in a deployment slot and swap after verification

### 4. The same container must run with different defect thresholds at each plant without a rebuild. What supplies those values?

Domain: Develop containerized solutions on Azure

- A. Deploy the image to Azure App Service as a web app
- B. Reference a Key Vault secret from the app configuration instead of storing it
- C. Supply configuration through App Service application settings
- D. Stage the change in a deployment slot and swap after verification

### 5. A new model build must be fully warmed before it replaces the running inspection app, with an instant rollback. What should be used?

Domain: Develop containerized solutions on Azure

- A. Create a new Container Apps revision and shift traffic between revisions
- B. Stage the change in a deployment slot and swap after verification
- C. Deploy the mutable latest tag and let the platform resolve it
- D. Supply configuration through App Service application settings

### 6. A defect-review worker must scale with the number of unprocessed images and drop to zero between shifts. What should drive scaling?

Domain: Develop containerized solutions on Azure

- A. Run the batch job in Azure Container Instances
- B. Scale the container app on an event source with a KEDA scaler
- C. Rely on the horizontal pod autoscaler on CPU
- D. Scale only on CPU utilization without an event scaler

### 7. The cluster deployment must be reproducible from version control and safe to reapply. What should be used?

Domain: Develop containerized solutions on Azure

- A. Rely on the horizontal pod autoscaler on CPU
- B. Run image builds on demand or on a trigger with ACR Tasks
- C. Apply a declarative Kubernetes manifest to the cluster
- D. Add readiness and liveness probes to the pod specification

### 8. Pods restart intermittently and the team needs container logs and platform events in one place. What should be used?

Domain: Develop containerized solutions on Azure

- A. Test end-to-end connectivity from inside the container to each dependency
- B. Enable diagnostic settings to route platform logs to the workspace
- C. Send telemetry to Application Insights and inspect the transaction view
- D. Query container logs and Kubernetes events in Log Analytics

### 9. Images must be traceable to a build and reproducible without a local host. Which two capabilities provide that? Select two.

Domain: Develop containerized solutions on Azure

- A. Build and store versioned images in Azure Container Registry
- B. Deploy the mutable latest tag and let the platform resolve it
- C. Replicate the registry to each deployment region
- D. Stage the change in a deployment slot and swap after verification
- E. Run image builds on demand or on a trigger with ACR Tasks

### 10. A cluster workload must be reproducible and must not take traffic while still initializing. Which two manifest elements are required? Select two.

Domain: Develop containerized solutions on Azure

- A. Add readiness and liveness probes to the pod specification
- B. Tune the scale rule cool-down period and maximum replicas
- C. Run the batch job in Azure Container Instances
- D. Apply a declarative Kubernetes manifest to the cluster
- E. Rely on the horizontal pod autoscaler on CPU

### 11. Which sequence correctly applies a manifest change and proves it works?

Domain: Develop containerized solutions on Azure

- A. Write the manifest → apply it to the cluster → wait for pod readiness → test ingress connectivity
- B. Apply the manifest → write the manifest → test ingress connectivity → wait for pod readiness
- C. Write the manifest → test ingress connectivity → apply it to the cluster → wait for pod readiness
- D. Wait for pod readiness → apply the manifest → write the manifest → test ingress connectivity

### 12. An inspection record must be read by line identifier and shift without scanning all documents. What should the query include?

Domain: Develop AI solutions by using Azure data management services

- A. Store the documents in Azure Cosmos DB for NoSQL
- B. Include the partition key in the query predicate
- C. Query through the Cosmos DB SDK with parameterized queries
- D. Increase provisioned throughput and watch the RU charge per query

### 13. Image metadata writes trigger throttling only during shift changes. What should be inspected alongside throughput?

Domain: Develop AI solutions by using Azure data management services

- A. Index every property by using the default automatic policy
- B. Enable autoscale throughput with a maximum RU limit
- C. Restrict the indexing policy to the paths the queries use
- D. Increase provisioned throughput and watch the RU charge per query

### 14. An inspector must see the defect note they just saved on the next screen, and other screens may lag. Which level fits?

Domain: Develop AI solutions by using Azure data management services

- A. Choose the account consistency level that matches the read requirement
- B. Use session consistency for reads within the same client session
- C. Use eventual consistency to minimize read cost
- D. Use strong consistency for every read in the account

### 15. Reference defect embeddings and their metadata must be queried together for similarity. What should be used?

Domain: Develop AI solutions by using Azure data management services

- A. Scan every document and compute similarity in application code
- B. Use the DiskANN vector index for large collections
- C. Declare the embedding dimensions and vector index type on the container policy
- D. Store embeddings in a vector property and query with VectorDistance

### 16. Several instances must share change feed partitions and resume after a restart. What tracks that progress?

Domain: Develop AI solutions by using Azure data management services

- A. Use a lease container to coordinate change feed readers
- B. Enable duplicate detection on the queue
- C. Batch related writes in a transactional batch within one partition key
- D. Run a change feed processor to react to new and updated items

### 17. Defect measurements must be filtered by line and compared by embedding in one statement. How should the table be modeled?

Domain: Develop AI solutions by using Azure data management services

- A. Add a read replica and send all vector queries to it
- B. Store embeddings in PostgreSQL by using the pgvector extension
- C. Model typed columns for filters and one vector column for the embedding
- D. Scale compute and memory to fit index size and query concurrency

### 18. Reference-image similarity over a large table must return quickly with tunable recall. Which index fits?

Domain: Develop AI solutions by using Azure data management services

- A. Increase maintenance and query memory settings for index builds and sorts
- B. Query without a vector index and let PostgreSQL scan the table
- C. Create an HNSW index for low-latency approximate search
- D. Create an IVFFlat index to save memory on a large table

### 19. Similarity latency spikes and the server reports memory pressure after index growth. What should be adjusted?

Domain: Develop AI solutions by using Azure data management services

- A. Scale compute and memory to fit index size and query concurrency
- B. Increase storage throughput for index builds and bulk loads
- C. Increase maintenance and query memory settings for index builds and sorts
- D. Reuse a bounded connection pool instead of opening a connection per request

### 20. Inspection stations reconnect constantly and the database rejects new sessions. What should be used first?

Domain: Develop AI solutions by using Azure data management services

- A. Reuse a bounded connection pool instead of opening a connection per request
- B. Place a connection pooler in front of PostgreSQL for many short-lived clients
- C. Add a read replica and send all vector queries to it
- D. Use prepared statements and batch round trips

### 21. Cached plant dashboards must never show data older than ten minutes. What should be set?

Domain: Develop AI solutions by using Azure data management services

- A. Flush the database after each deployment to guarantee fresh data
- B. Set a TTL on each cached entry
- C. Rely on the eviction policy and skip explicit TTLs
- D. Invalidate or overwrite the cache entry when the source changes

### 22. Known-defect exemplars must be compared with sub-10-millisecond latency from memory. What should be used?

Domain: Develop AI solutions by using Azure data management services

- A. Cache responses in Azure Managed Redis
- B. Use a distributed lock in Redis to make processing idempotent
- C. Store user session state in Managed Redis with an expiry
- D. Create a vector index in Managed Redis for similarity search

### 23. A NoSQL writer must use the supported SDK and apply related documents atomically within a partition. Which two features are required? Select two.

Domain: Develop AI solutions by using Azure data management services

- A. Query through the Cosmos DB SDK with parameterized queries
- B. Batch related writes in a transactional batch within one partition key
- C. Enable duplicate detection on the queue
- D. Use a lease container to coordinate change feed readers
- E. Enable autoscale throughput with a maximum RU limit

### 24. A memory-limited database must still serve vector search, and large sorts spill to disk. Which two adjustments apply? Select two.

Domain: Develop AI solutions by using Azure data management services

- A. Increase storage throughput for index builds and bulk loads
- B. Increase maintenance and query memory settings for index builds and sorts
- C. Query without a vector index and let PostgreSQL scan the table
- D. Create an HNSW index for low-latency approximate search
- E. Create an IVFFlat index to save memory on a large table

### 25. Which sequence correctly prepares an inspection container for similarity search?

Domain: Develop AI solutions by using Azure data management services

- A. Apply metadata filters → query with VectorDistance → create the container with a vector policy → upsert items with embeddings
- B. Create the container with a vector policy → upsert items with embeddings → query with VectorDistance → apply metadata filters
- C. Query with VectorDistance → upsert items with embeddings → create the container with a vector policy → apply metadata filters
- D. Upsert items with embeddings → create the container with a vector policy → apply metadata filters → query with VectorDistance

### 26. Each captured image must be inspected by exactly one worker, with recovery if a worker crashes. What should be used?

Domain: Connect to and consume Azure services

- A. Stream telemetry through Azure Event Hubs
- B. Use Azure Queue Storage for the work items
- C. Queue the work on a Service Bus queue and process it with a worker
- D. Publish to a Service Bus topic with multiple subscriptions

### 27. Readings for one machine must be handled in order by a single consumer. What should be enabled?

Domain: Connect to and consume Azure services

- A. Set a maximum delivery count and handle the dead-letter path
- B. Enable duplicate detection on the queue
- C. Receive with peek-lock and complete or abandon explicitly
- D. Use Service Bus sessions to keep related messages ordered

### 28. Quality, maintenance, and audit systems must each receive the same defect event independently. What should be used?

Domain: Connect to and consume Azure services

- A. Define a custom event schema for the topic
- B. Use Azure Queue Storage for the work items
- C. Queue the work on a Service Bus queue and process it with a worker
- D. Publish to a Service Bus topic with multiple subscriptions

### 29. A maintenance webhook is briefly unavailable and events must not be lost permanently. What should be configured?

Domain: Connect to and consume Azure services

- A. Filter the Event Grid subscription by subject or event type
- B. Define a custom event schema for the topic
- C. Deliver events by using a managed identity instead of a key
- D. Rely on Event Grid retries with a dead-letter destination

### 30. A function must run when an inspection result is queued, without a polling loop in code. What should be configured?

Domain: Connect to and consume Azure services

- A. Bind a queue or event trigger to the function
- B. Orchestrate the multi-step workflow with Durable Functions
- C. Expose the endpoint through an HTTP trigger
- D. Use input and output bindings instead of hand-written SDK calls

### 31. The function must write its result to Cosmos DB with as little client code as possible. What should be used?

Domain: Connect to and consume Azure services

- A. Host the function app on a premium plan with pre-warmed instances
- B. Bind a queue or event trigger to the function
- C. Use input and output bindings instead of hand-written SDK calls
- D. Orchestrate the multi-step workflow with Durable Functions

### 32. The inspection function must avoid cold starts and reach a private dependency. Which hosting choice fits?

Domain: Connect to and consume Azure services

- A. Host the function app on a premium plan with pre-warmed instances
- B. Use a deployment slot on the function app for staging
- C. Orchestrate the multi-step workflow with Durable Functions
- D. Host the function app on the consumption plan

### 33. Defect events must reach two systems independently, and one of them only wants severe defects. Which two features are required? Select two.

Domain: Connect to and consume Azure services

- A. Publish to a Service Bus topic with multiple subscriptions
- B. Queue the work on a Service Bus queue and process it with a worker
- C. Filter the Event Grid subscription by subject or event type
- D. Add a SQL or correlation filter to a subscription
- E. Use Azure Queue Storage for the work items

### 34. A multi-step rework workflow must resume after a host restart and must start from a queue event. Which two features are required? Select two.

Domain: Connect to and consume Azure services

- A. Expose the endpoint through an HTTP trigger
- B. Host the function app on the consumption plan
- C. Orchestrate the multi-step workflow with Durable Functions
- D. Use input and output bindings instead of hand-written SDK calls
- E. Bind a queue or event trigger to the function

### 35. Which sequence correctly processes an inspection message?

Domain: Connect to and consume Azure services

- A. Receive with peek-lock → publish the message → complete the message → process the work → dead-letter after the delivery limit
- B. Process the work → receive with peek-lock → publish the message → complete the message → dead-letter after the delivery limit
- C. Publish the message → receive with peek-lock → process the work → complete the message → dead-letter after the delivery limit
- D. Publish the message → complete the message → receive with peek-lock → process the work → dead-letter after the delivery limit

### 36. A camera vendor token must be auditable and revocable without an image rebuild. Where should it live?

Domain: Secure, monitor, troubleshoot Azure solutions

- A. Store the secret in Azure Key Vault and read it at runtime
- B. Pin the application to a specific secret version
- C. Store settings and feature flags in Azure App Configuration
- D. Supply configuration through App Service application settings

### 37. The vault reference fails for a workload identity that has no vault role. What should be added?

Domain: Secure, monitor, troubleshoot Azure solutions

- A. Authenticate with a managed identity instead of a stored key
- B. Enable purge protection and soft delete on the vault
- C. Assign a least-privilege role to the application identity
- D. Grant the app identity data-plane access to the vault

### 38. Defect thresholds must change per plant without redeploying the container. What should be used?

Domain: Secure, monitor, troubleshoot Azure solutions

- A. Store settings and feature flags in Azure App Configuration
- B. Enable configuration refresh so changes apply without a restart
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

- A. Enable diagnostic settings to route platform logs to the workspace
- B. Instrument the service with the OpenTelemetry SDK
- C. Send telemetry to Application Insights and inspect the transaction view
- D. Query the workspace with KQL to find the failing operation

### 41. A deployment pipeline identity can change cluster settings but the application only reads secrets. What should be done?

Domain: Secure, monitor, troubleshoot Azure solutions

- A. Reach the data service through a private endpoint
- B. Assign a least-privilege role to the application identity
- C. Authenticate with a managed identity instead of a stored key
- D. Store the secret in Azure Key Vault and read it at runtime

### 42. Traces must connect the API, queue, and function hops and must not lose the correlation across messaging. Which two practices are required? Select two.

Domain: Secure, monitor, troubleshoot Azure solutions

- A. Propagate trace context across every service and queue hop
- B. Use head or tail sampling so trace volume stays within budget
- C. Instrument the service with the OpenTelemetry SDK
- D. Enable diagnostic settings to route platform logs to the workspace
- E. Query the workspace with KQL to find the failing operation

### 43. A secret must be stored centrally and read by the workload with no stored credential. Which two actions should you take? Select two.

Domain: Secure, monitor, troubleshoot Azure solutions

- A. Authenticate with a managed identity instead of a stored key
- B. Use App Configuration labels to separate environments
- C. Store the secret in Azure Key Vault and read it at runtime
- D. Pin the application to a specific secret version
- E. Store settings and feature flags in Azure App Configuration

### 44. Which sequence correctly introduces a rotated camera token?

Domain: Secure, monitor, troubleshoot Azure solutions

- A. Reference the secret from the app → rotate the secret → store the secret in Key Vault → grant the app identity access → the app reads the new version
- B. Grant the app identity access → store the secret in Key Vault → rotate the secret → reference the secret from the app → the app reads the new version
- C. Rotate the secret → reference the secret from the app → store the secret in Key Vault → grant the app identity access → the app reads the new version
- D. Store the secret in Key Vault → grant the app identity access → reference the secret from the app → rotate the secret → the app reads the new version

---

## Case study — Contoso Assembly

The next three questions refer to this scenario. Read the full scenario before answering; case-study items are scored individually.

### 45. Reviewers must see only defects from their own plant while still receiving a full list of matches. What should the query do?

Domain: Develop AI solutions by using Azure data management services

- A. Query without a vector index and let PostgreSQL scan the table
- B. Retrieve nearest neighbours first and discard unauthorized rows in the application
- C. Filter on metadata columns in the same query as the vector search
- D. Create an HNSW index for low-latency approximate search

### 46. A corrupt image reference repeatedly fails inspection and must be preserved for analysis. What should happen to it?

Domain: Connect to and consume Azure services

- A. Set a maximum delivery count and handle the dead-letter path
- B. Inspect the dead-letter queue and resubmit corrected messages
- C. Enable duplicate detection on the queue
- D. Receive in receive-and-delete mode for at-most-once delivery

### 47. The team needs rejection counts per fifteen-minute interval during a shift. Which construct should be used?

Domain: Secure, monitor, troubleshoot Azure solutions

- A. Project only the columns needed and filter by time first
- B. Aggregate with summarize and bin to see the failure rate over time
- C. Store repeated aggregations in a materialized view or update policy
- D. Join the requests and dependencies tables on the operation ID

---

## Case study — Fabrikam Plant

The next three questions refer to this scenario. Read the full scenario before answering; case-study items are scored individually.

### 48. Pods cannot open a connection to the storage account, though the same test succeeds from a workstation. What should be verified?

Domain: Develop containerized solutions on Azure

- A. Reach the data service through a private endpoint
- B. Test end-to-end connectivity from inside the container to each dependency
- C. Add readiness and liveness probes to the pod specification
- D. Link the private DNS zone so the private endpoint name resolves

### 49. Only events for a specific production line should reach the maintenance handler. What should be configured?

Domain: Connect to and consume Azure services

- A. Add a SQL or correlation filter to a subscription
- B. Enable duplicate detection on the queue
- C. Rely on Event Grid retries with a dead-letter destination
- D. Filter the Event Grid subscription by subject or event type

### 50. An operator needs the slowest inspection operations in the last hour with their durations. Which tool should be used?

Domain: Secure, monitor, troubleshoot Azure solutions

- A. Query the workspace with KQL to find the failing operation
- B. Alert on platform metrics rather than only on log queries
- C. Aggregate with summarize and bin to see the failure rate over time
- D. Project only the columns needed and filter by time first

---

## Answer key and explanations

### Question 1 — A

Answer: Replicate the registry to each deployment region. Geo-replication keeps a registry copy in each plant region, so pulls stay local. Geo-replication reduces cross-region pull latency and gives a local copy during a regional failure. It adds cost and replication management. Local study-map skill 1.1 (Container Image Lifecycle in Azure Container Registry), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure container hosting documentation: https://learn.microsoft.com/en-us/azure/container-apps/

- **A:** Correct. Geo-replication reduces cross-region pull latency and gives a local copy during a regional failure. It adds cost and replication management. In this case: Geo-replication keeps a registry copy in each plant region, so pulls stay local.
- **B:** Incorrect for this question. ACR Tasks builds images in Azure on a commit or schedule without a local Docker host. It removes build-host drift but not image review. Why the correct answer wins: Geo-replication keeps a registry copy in each plant region, so pulls stay local.
- **C:** Incorrect for this question. A retention policy controls storage growth and registry clutter. It does not change which image tag a deployment references. Why the correct answer wins: Geo-replication keeps a registry copy in each plant region, so pulls stay local.
- **D:** Incorrect for this question. A floating tag removes the link between a deployed revision and a specific build, so rollback and audit become guesswork. Why the correct answer wins: Geo-replication keeps a registry copy in each plant region, so pulls stay local.

### Question 2 — B

Answer: Apply an ACR retention policy to prune old untagged manifests. A retention policy prunes unused manifests while keeping referenced tags. A retention policy controls storage growth and registry clutter. It does not change which image tag a deployment references. Local study-map skill 1.1 (Container Image Lifecycle in Azure Container Registry), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure container hosting documentation: https://learn.microsoft.com/en-us/azure/container-apps/

- **A:** Incorrect for this question. ACR Tasks builds images in Azure on a commit or schedule without a local Docker host. It removes build-host drift but not image review. Why the correct answer wins: A retention policy prunes unused manifests while keeping referenced tags.
- **B:** Correct. A retention policy controls storage growth and registry clutter. It does not change which image tag a deployment references. In this case: A retention policy prunes unused manifests while keeping referenced tags.
- **C:** Incorrect for this question. A floating tag removes the link between a deployed revision and a specific build, so rollback and audit become guesswork. Why the correct answer wins: A retention policy prunes unused manifests while keeping referenced tags.
- **D:** Incorrect for this question. Geo-replication reduces cross-region pull latency and gives a local copy during a regional failure. It adds cost and replication management. Why the correct answer wins: A retention policy prunes unused manifests while keeping referenced tags.

### Question 3 — C

Answer: Run image builds on demand or on a trigger with ACR Tasks. An ACR Task triggered by the source commit builds the image inside Azure. ACR Tasks builds images in Azure on a commit or schedule without a local Docker host. It removes build-host drift but not image review. Local study-map skill 1.2 (Automated Image Builds with ACR Tasks), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure container hosting documentation: https://learn.microsoft.com/en-us/azure/container-apps/

- **A:** Incorrect for this question. ACR keeps tagged, versioned images next to the deployment target and supports identity-based pulls. Tagging strategy and retention still need a decision. Why the correct answer wins: An ACR Task triggered by the source commit builds the image inside Azure.
- **B:** Incorrect for this question. Container Instances starts a single container group quickly for short tasks. It has no orchestrator-level scaling or revision model. Why the correct answer wins: An ACR Task triggered by the source commit builds the image inside Azure.
- **C:** Correct. ACR Tasks builds images in Azure on a commit or schedule without a local Docker host. It removes build-host drift but not image review. In this case: An ACR Task triggered by the source commit builds the image inside Azure.
- **D:** Incorrect for this question. A slot swap warms the new version before it takes production traffic and makes rollback a second swap. Slot-local settings must be marked sticky. Why the correct answer wins: An ACR Task triggered by the source commit builds the image inside Azure.

### Question 4 — C

Answer: Supply configuration through App Service application settings. Application settings inject per-environment configuration at runtime. Application settings become environment variables for the container and can be swapped per slot. Sensitive values should still reference a vault. Local study-map skill 1.3 (Container Deployment to Azure App Service), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure container hosting documentation: https://learn.microsoft.com/en-us/azure/container-apps/

- **A:** Incorrect for this question. App Service runs a container with managed patching, deployment slots, and built-in authentication options. It is not a Kubernetes control plane. Why the correct answer wins: Application settings inject per-environment configuration at runtime.
- **B:** Incorrect for this question. A Key Vault reference resolves at runtime so the secret is never written into application settings. The app identity still needs permission to read it. Why the correct answer wins: Application settings inject per-environment configuration at runtime.
- **C:** Correct. Application settings become environment variables for the container and can be swapped per slot. Sensitive values should still reference a vault. In this case: Application settings inject per-environment configuration at runtime.
- **D:** Incorrect for this question. A slot swap warms the new version before it takes production traffic and makes rollback a second swap. Slot-local settings must be marked sticky. Why the correct answer wins: Application settings inject per-environment configuration at runtime.

### Question 5 — B

Answer: Stage the change in a deployment slot and swap after verification. A slot swap warms the new version and makes rollback a second swap. A slot swap warms the new version before it takes production traffic and makes rollback a second swap. Slot-local settings must be marked sticky. Local study-map skill 1.3 (Container Deployment to Azure App Service), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure container hosting documentation: https://learn.microsoft.com/en-us/azure/container-apps/

- **A:** Incorrect for this question. Revision-based traffic splitting enables canary and blue-green releases. Revision mode and scale rules must be set deliberately. Why the correct answer wins: A slot swap warms the new version and makes rollback a second swap.
- **B:** Correct. A slot swap warms the new version before it takes production traffic and makes rollback a second swap. Slot-local settings must be marked sticky. In this case: A slot swap warms the new version and makes rollback a second swap.
- **C:** Incorrect for this question. A floating tag removes the link between a deployed revision and a specific build, so rollback and audit become guesswork. Why the correct answer wins: A slot swap warms the new version and makes rollback a second swap.
- **D:** Incorrect for this question. Application settings become environment variables for the container and can be swapped per slot. Sensitive values should still reference a vault. Why the correct answer wins: A slot swap warms the new version and makes rollback a second swap.

### Question 6 — B

Answer: Scale the container app on an event source with a KEDA scaler. A KEDA queue scaler follows backlog depth and can scale to zero. KEDA scalers drive replica count from queue length, lag, or other event metrics, including scale to zero. Cool-down and max replicas bound the behavior. Local study-map skill 1.5 (Event-Driven Scaling with KEDA), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure container hosting documentation: https://learn.microsoft.com/en-us/azure/container-apps/

- **A:** Incorrect for this question. Container Instances starts a single container group quickly for short tasks. It has no orchestrator-level scaling or revision model. Why the correct answer wins: A KEDA queue scaler follows backlog depth and can scale to zero.
- **B:** Correct. KEDA scalers drive replica count from queue length, lag, or other event metrics, including scale to zero. Cool-down and max replicas bound the behavior. In this case: A KEDA queue scaler follows backlog depth and can scale to zero.
- **C:** Incorrect for this question. HPA adjusts replicas from resource metrics but needs metrics-server and enough node capacity. It cannot scale to zero. Why the correct answer wins: A KEDA queue scaler follows backlog depth and can scale to zero.
- **D:** Incorrect for this question. CPU-based scaling reacts after work is already queued and cannot scale to zero on an empty queue. It suits steady request-driven services. Why the correct answer wins: A KEDA queue scaler follows backlog depth and can scale to zero.

### Question 7 — C

Answer: Apply a declarative Kubernetes manifest to the cluster. A declarative manifest describes desired state and is idempotent when reapplied. A manifest declares the desired deployment, service, and probe configuration in version control. Applying it repeatedly is idempotent. Local study-map skill 1.6 (AKS Deployment with Manifests), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure container hosting documentation: https://learn.microsoft.com/en-us/azure/container-apps/

- **A:** Incorrect for this question. HPA adjusts replicas from resource metrics but needs metrics-server and enough node capacity. It cannot scale to zero. Why the correct answer wins: A declarative manifest describes desired state and is idempotent when reapplied.
- **B:** Incorrect for this question. ACR Tasks builds images in Azure on a commit or schedule without a local Docker host. It removes build-host drift but not image review. Why the correct answer wins: A declarative manifest describes desired state and is idempotent when reapplied.
- **C:** Correct. A manifest declares the desired deployment, service, and probe configuration in version control. Applying it repeatedly is idempotent. In this case: A declarative manifest describes desired state and is idempotent when reapplied.
- **D:** Incorrect for this question. Readiness gates traffic until the app can serve it, and liveness restarts a wedged container. Wrong thresholds cause restart loops. Why the correct answer wins: A declarative manifest describes desired state and is idempotent when reapplied.

### Question 8 — D

Answer: Query container logs and Kubernetes events in Log Analytics. Log Analytics collects container logs and platform events for KQL analysis. Container Apps and AKS surface stdout logs and platform events into a workspace for KQL analysis. Verbosity and retention cost money. Local study-map skill 1.7 (Container Logs, Events, and Connectivity), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure container hosting documentation: https://learn.microsoft.com/en-us/azure/container-apps/

- **A:** Incorrect for this question. Reaching a dependency from the pod or replica proves DNS, egress, and firewall paths together. Host-side tests can succeed while the container path fails. Why the correct answer wins: Log Analytics collects container logs and platform events for KQL analysis.
- **B:** Incorrect for this question. Platform logs and metrics must be routed before they can be queried or alerted on. Retention and cost follow the workspace settings. Why the correct answer wins: Log Analytics collects container logs and platform events for KQL analysis.
- **C:** Incorrect for this question. Application Insights correlates requests, dependencies, and exceptions into end-to-end transactions. Sampling can hide rare failures. Why the correct answer wins: Log Analytics collects container logs and platform events for KQL analysis.
- **D:** Correct. Container Apps and AKS surface stdout logs and platform events into a workspace for KQL analysis. Verbosity and retention cost money. In this case: Log Analytics collects container logs and platform events for KQL analysis.

### Question 9 — A, E

Answers: Build and store versioned images in Azure Container Registry; Run image builds on demand or on a trigger with ACR Tasks. Versioned registry tags identify artifacts, and ACR Tasks builds them in Azure on a trigger. ACR keeps tagged, versioned images next to the deployment target and supports identity-based pulls. Tagging strategy and retention still need a decision. ACR Tasks builds images in Azure on a commit or schedule without a local Docker host. It removes build-host drift but not image review. Local study-map skill 1.1 (Container Image Lifecycle in Azure Container Registry), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure container hosting documentation: https://learn.microsoft.com/en-us/azure/container-apps/

- **A:** Correct. ACR keeps tagged, versioned images next to the deployment target and supports identity-based pulls. Tagging strategy and retention still need a decision. In this case: Versioned registry tags identify artifacts, and ACR Tasks builds them in Azure on a trigger.
- **B:** Incorrect for this question. A floating tag removes the link between a deployed revision and a specific build, so rollback and audit become guesswork. Why the correct answer wins: Versioned registry tags identify artifacts, and ACR Tasks builds them in Azure on a trigger.
- **C:** Incorrect for this question. Geo-replication reduces cross-region pull latency and gives a local copy during a regional failure. It adds cost and replication management. Why the correct answer wins: Versioned registry tags identify artifacts, and ACR Tasks builds them in Azure on a trigger.
- **D:** Incorrect for this question. A slot swap warms the new version before it takes production traffic and makes rollback a second swap. Slot-local settings must be marked sticky. Why the correct answer wins: Versioned registry tags identify artifacts, and ACR Tasks builds them in Azure on a trigger.
- **E:** Correct. ACR Tasks builds images in Azure on a commit or schedule without a local Docker host. It removes build-host drift but not image review. In this case: Versioned registry tags identify artifacts, and ACR Tasks builds them in Azure on a trigger.

### Question 10 — A, D

Answers: Apply a declarative Kubernetes manifest to the cluster; Add readiness and liveness probes to the pod specification. The applied manifest makes state reproducible, and a readiness probe holds traffic until the app is ready. A manifest declares the desired deployment, service, and probe configuration in version control. Applying it repeatedly is idempotent. Readiness gates traffic until the app can serve it, and liveness restarts a wedged container. Wrong thresholds cause restart loops. Local study-map skill 1.6 (AKS Deployment with Manifests), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure container hosting documentation: https://learn.microsoft.com/en-us/azure/container-apps/

- **A:** Correct. Readiness gates traffic until the app can serve it, and liveness restarts a wedged container. Wrong thresholds cause restart loops. In this case: The applied manifest makes state reproducible, and a readiness probe holds traffic until the app is ready.
- **B:** Incorrect for this question. Cool-down prevents replica flapping, and a maximum replica cap bounds cost and downstream load. Both are per-rule settings. Why the correct answer wins: The applied manifest makes state reproducible, and a readiness probe holds traffic until the app is ready.
- **C:** Incorrect for this question. Container Instances starts a single container group quickly for short tasks. It has no orchestrator-level scaling or revision model. Why the correct answer wins: The applied manifest makes state reproducible, and a readiness probe holds traffic until the app is ready.
- **D:** Correct. A manifest declares the desired deployment, service, and probe configuration in version control. Applying it repeatedly is idempotent. In this case: The applied manifest makes state reproducible, and a readiness probe holds traffic until the app is ready.
- **E:** Incorrect for this question. HPA adjusts replicas from resource metrics but needs metrics-server and enough node capacity. It cannot scale to zero. Why the correct answer wins: The applied manifest makes state reproducible, and a readiness probe holds traffic until the app is ready.

### Question 11 — A

Answer: Write the manifest → apply it to the cluster → wait for pod readiness → test ingress connectivity. The manifest is authored and applied before readiness is checked, and connectivity is tested last. Readiness must pass before a connectivity test proves anything, and the manifest must exist before it is applied. Local study-map skill 1.6 (AKS Deployment with Manifests), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure container hosting documentation: https://learn.microsoft.com/en-us/azure/container-apps/

- **A:** Correct. Readiness must pass before a connectivity test proves anything, and the manifest must exist before it is applied. In this case: The manifest is authored and applied before readiness is checked, and connectivity is tested last.
- **B:** Incorrect for this question. A manifest is authored before it is applied, and connectivity is meaningless while pods are not ready. Why the correct answer wins: The manifest is authored and applied before readiness is checked, and connectivity is tested last.
- **C:** Incorrect for this question. Ingress cannot be tested before the workload exists in the cluster. Why the correct answer wins: The manifest is authored and applied before readiness is checked, and connectivity is tested last.
- **D:** Incorrect for this question. Pods cannot become ready before the manifest is applied. Why the correct answer wins: The manifest is authored and applied before readiness is checked, and connectivity is tested last.

### Question 12 — A

Answer: Store the documents in Azure Cosmos DB for NoSQL. Including the partition key makes the read single-partition. Cosmos DB gives globally distributed, low-latency document access with tunable consistency. Partition key and RU planning determine the cost profile. Local study-map skill 2.1 (Cosmos DB SDK Access and Queries), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Cosmos DB and PostgreSQL vector documentation: https://learn.microsoft.com/en-us/azure/cosmos-db/

- **A:** Correct. Cosmos DB gives globally distributed, low-latency document access with tunable consistency. Partition key and RU planning determine the cost profile. In this case: Including the partition key makes the read single-partition.
- **B:** Incorrect for this question. A point or single-partition query avoids fan-out across partitions. Cross-partition queries consume more RUs and add latency. Why the correct answer wins: Including the partition key makes the read single-partition.
- **C:** Incorrect for this question. SDK queries keep the client on the supported data plane and parameterization avoids injection and plan churn. Cross-partition queries still cost more. Why the correct answer wins: Including the partition key makes the read single-partition.
- **D:** Incorrect for this question. Request units measure the work a query performs, so tuning the query is often cheaper than adding throughput. Monitor normalized RU consumption. Why the correct answer wins: Including the partition key makes the read single-partition.

### Question 13 — D

Answer: Increase provisioned throughput and watch the RU charge per query. The RU charge per write shows whether indexing or document size is inflating cost before adding throughput. Request units measure the work a query performs, so tuning the query is often cheaper than adding throughput. Monitor normalized RU consumption. Local study-map skill 2.2 (Cosmos DB Indexing Policies and Request Units), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Cosmos DB and PostgreSQL vector documentation: https://learn.microsoft.com/en-us/azure/cosmos-db/

- **A:** Incorrect for this question. Indexing everything is simple and makes ad hoc queries possible, at higher write cost and storage. It is a default, not an optimization. Why the correct answer wins: The RU charge per write shows whether indexing or document size is inflating cost before adding throughput.
- **B:** Incorrect for this question. Autoscale follows demand between a minimum and maximum, avoiding throttling at peak without paying for peak all day. The maximum still caps the bill. Why the correct answer wins: The RU charge per write shows whether indexing or document size is inflating cost before adding throughput.
- **C:** Incorrect for this question. Selective indexing cuts write RU charge and storage for unused paths. Excluded paths cannot be filtered efficiently later. Why the correct answer wins: The RU charge per write shows whether indexing or document size is inflating cost before adding throughput.
- **D:** Correct. Request units measure the work a query performs, so tuning the query is often cheaper than adding throughput. Monitor normalized RU consumption. In this case: The RU charge per write shows whether indexing or document size is inflating cost before adding throughput.

### Question 14 — B

Answer: Use session consistency for reads within the same client session. Session consistency guarantees read-your-writes for that session. Session consistency guarantees monotonic reads for one session and is the common default for user-facing apps. It does not promise global freshness. Local study-map skill 2.3 (Cosmos DB Consistency Levels), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Cosmos DB and PostgreSQL vector documentation: https://learn.microsoft.com/en-us/azure/cosmos-db/

- **A:** Incorrect for this question. Consistency trades freshness against latency, availability, and RU cost. The level is set at the account and can be relaxed per request. Why the correct answer wins: Session consistency guarantees read-your-writes for that session.
- **B:** Correct. Session consistency guarantees monotonic reads for one session and is the common default for user-facing apps. It does not promise global freshness. In this case: Session consistency guarantees read-your-writes for that session.
- **C:** Incorrect for this question. Eventual consistency is the cheapest and most available option but returns possibly stale data. It fits non-critical counters, not balances. Why the correct answer wins: Session consistency guarantees read-your-writes for that session.
- **D:** Incorrect for this question. Strong consistency guarantees the latest committed write globally at the cost of higher latency and reduced availability during partitions. Why the correct answer wins: Session consistency guarantees read-your-writes for that session.

### Question 15 — D

Answer: Store embeddings in a vector property and query with VectorDistance. A vector property plus the distance function keeps embeddings and metadata in one query. Cosmos DB for NoSQL supports vector properties and a distance function for similarity search in the same document store. Dimensions and index type must match the model. Local study-map skill 2.4 (Cosmos DB Vector Search and Embeddings), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Cosmos DB and PostgreSQL vector documentation: https://learn.microsoft.com/en-us/azure/cosmos-db/

- **A:** Incorrect for this question. Application-side scoring works for tiny collections and tests, but it moves all data over the wire and does not scale with corpus size. Why the correct answer wins: A vector property plus the distance function keeps embeddings and metadata in one query.
- **B:** Incorrect for this question. DiskANN trades some recall for memory efficiency on large sets. Recall and latency should be measured on representative queries. Why the correct answer wins: A vector property plus the distance function keeps embeddings and metadata in one query.
- **C:** Incorrect for this question. The container vector policy fixes dimensions, distance function, and index type, so a model change requires a new policy. Mismatched dimensions fail at write time. Why the correct answer wins: A vector property plus the distance function keeps embeddings and metadata in one query.
- **D:** Correct. Cosmos DB for NoSQL supports vector properties and a distance function for similarity search in the same document store. Dimensions and index type must match the model. In this case: A vector property plus the distance function keeps embeddings and metadata in one query.

### Question 16 — A

Answer: Use a lease container to coordinate change feed readers. A lease container records ownership and continuation per partition. Leases track partition ownership so multiple processor instances share work and resume from a continuation token. Lease writes consume RUs too. Local study-map skill 2.5 (Cosmos DB Change Feed Processing), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Cosmos DB and PostgreSQL vector documentation: https://learn.microsoft.com/en-us/azure/cosmos-db/

- **A:** Correct. Leases track partition ownership so multiple processor instances share work and resume from a continuation token. Lease writes consume RUs too. In this case: A lease container records ownership and continuation per partition.
- **B:** Incorrect for this question. A duplicate-detection window drops repeated sends within the window, which helps with at-least-once producers. The window is time-bounded. Why the correct answer wins: A lease container records ownership and continuation per partition.
- **C:** Incorrect for this question. A transactional batch applies all-or-nothing within a single partition key. It cannot span partitions and still consumes RU per operation. Why the correct answer wins: A lease container records ownership and continuation per partition.
- **D:** Incorrect for this question. The change feed delivers an ordered stream of changes per partition for downstream processing. It is not a delete feed, so deletions need a workaround. Why the correct answer wins: A lease container records ownership and continuation per partition.

### Question 17 — C

Answer: Model typed columns for filters and one vector column for the embedding. Typed columns for filters with one vector column enable both in one query. Explicit types keep filters fast and make the embedding contract clear. Storing vectors as text defeats index use. Local study-map skill 2.6 (PostgreSQL Connection and Schema Modeling), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Cosmos DB and PostgreSQL vector documentation: https://learn.microsoft.com/en-us/azure/cosmos-db/

- **A:** Incorrect for this question. A replica offloads read traffic but introduces replication lag, which is dangerous for freshly written evidence. It does not reduce index memory pressure. Why the correct answer wins: Typed columns for filters with one vector column enable both in one query.
- **B:** Incorrect for this question. pgvector keeps vectors beside relational data, so filters and joins run in one query. Index type and parameter tuning decide latency. Why the correct answer wins: Typed columns for filters with one vector column enable both in one query.
- **C:** Correct. Explicit types keep filters fast and make the embedding contract clear. Storing vectors as text defeats index use. In this case: Typed columns for filters with one vector column enable both in one query.
- **D:** Incorrect for this question. Vector indexes are memory-hungry, so undersized compute causes swapping and slow queries. Right-size before tuning index parameters. Why the correct answer wins: Typed columns for filters with one vector column enable both in one query.

### Question 18 — C

Answer: Create an HNSW index for low-latency approximate search. HNSW provides fast approximate search with recall tuned at query time. HNSW gives fast approximate nearest-neighbour queries with a larger memory footprint and slower builds. Recall is tunable at query time. Local study-map skill 2.7 (pgvector Indexing and Query Latency), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Cosmos DB and PostgreSQL vector documentation: https://learn.microsoft.com/en-us/azure/cosmos-db/

- **A:** Incorrect for this question. Index builds and large sorts spill to disk when work memory is too small, stretching maintenance windows and slowing queries. Why the correct answer wins: HNSW provides fast approximate search with recall tuned at query time.
- **B:** Incorrect for this question. An exact scan is accurate but scales linearly and burns compute. It is a baseline for measuring recall, not a production strategy. Why the correct answer wins: HNSW provides fast approximate search with recall tuned at query time.
- **C:** Correct. HNSW gives fast approximate nearest-neighbour queries with a larger memory footprint and slower builds. Recall is tunable at query time. In this case: HNSW provides fast approximate search with recall tuned at query time.
- **D:** Incorrect for this question. IVFFlat uses clustering lists and needs periodic rebuilds as data grows, but costs less memory than HNSW. Probes trade recall for speed. Why the correct answer wins: HNSW provides fast approximate search with recall tuned at query time.

### Question 19 — A

Answer: Scale compute and memory to fit index size and query concurrency. Compute and memory must fit the index working set to avoid swapping. Vector indexes are memory-hungry, so undersized compute causes swapping and slow queries. Right-size before tuning index parameters. Local study-map skill 2.8 (PostgreSQL Compute, Memory, and Storage Sizing), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Cosmos DB and PostgreSQL vector documentation: https://learn.microsoft.com/en-us/azure/cosmos-db/

- **A:** Correct. Vector indexes are memory-hungry, so undersized compute causes swapping and slow queries. Right-size before tuning index parameters. In this case: Compute and memory must fit the index working set to avoid swapping.
- **B:** Incorrect for this question. Index creation and bulk loads are I/O heavy, and throttled storage stretches maintenance windows. Storage limits are separate from compute. Why the correct answer wins: Compute and memory must fit the index working set to avoid swapping.
- **C:** Incorrect for this question. Index builds and large sorts spill to disk when work memory is too small, stretching maintenance windows and slowing queries. Why the correct answer wins: Compute and memory must fit the index working set to avoid swapping.
- **D:** Incorrect for this question. A bounded pool amortizes connection setup and protects the server from connection storms. Pool size must match server limits. Why the correct answer wins: Compute and memory must fit the index working set to avoid swapping.

### Question 20 — A

Answer: Reuse a bounded connection pool instead of opening a connection per request. A bounded connection pool reuses connections instead of opening one per request. A bounded pool amortizes connection setup and protects the server from connection storms. Pool size must match server limits. Local study-map skill 2.10 (PostgreSQL Connection Optimization), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Cosmos DB and PostgreSQL vector documentation: https://learn.microsoft.com/en-us/azure/cosmos-db/

- **A:** Correct. A bounded pool amortizes connection setup and protects the server from connection storms. Pool size must match server limits. In this case: A bounded connection pool reuses connections instead of opening one per request.
- **B:** Incorrect for this question. An external pooler multiplexes server connections for serverless or highly concurrent clients. Session-level features may be unavailable in transaction mode. Why the correct answer wins: A bounded connection pool reuses connections instead of opening one per request.
- **C:** Incorrect for this question. A replica offloads read traffic but introduces replication lag, which is dangerous for freshly written evidence. It does not reduce index memory pressure. Why the correct answer wins: A bounded connection pool reuses connections instead of opening one per request.
- **D:** Incorrect for this question. Prepared statements avoid repeated planning and reduce chatty network calls. They pair well with pooling but can interact with pool modes. Why the correct answer wins: A bounded connection pool reuses connections instead of opening one per request.

### Question 21 — B

Answer: Set a TTL on each cached entry. A TTL bounds staleness independently of invalidation. A TTL bounds staleness and reclaims memory without a manual sweep. Too long a TTL hides source changes; too short wastes the cache. Local study-map skill 2.11 (Azure Managed Redis Caching and Invalidation), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Cosmos DB and PostgreSQL vector documentation: https://learn.microsoft.com/en-us/azure/cosmos-db/

- **A:** Incorrect for this question. Flushing removes all cached content at once, causing a stampede to the origin and a latency cliff. Targeted invalidation is safer. Why the correct answer wins: A TTL bounds staleness independently of invalidation.
- **B:** Correct. A TTL bounds staleness and reclaims memory without a manual sweep. Too long a TTL hides source changes; too short wastes the cache. In this case: A TTL bounds staleness independently of invalidation.
- **C:** Incorrect for this question. Eviction protects memory but evicts unpredictably, so a hot key can vanish before its freshness bound is reached. It is not a substitute for TTL design. Why the correct answer wins: A TTL bounds staleness independently of invalidation.
- **D:** Incorrect for this question. Write-through or explicit invalidation keeps cached answers consistent with the system of record. Without it, TTL is the only bound on staleness. Why the correct answer wins: A TTL bounds staleness independently of invalidation.

### Question 22 — D

Answer: Create a vector index in Managed Redis for similarity search. A Redis vector index performs similarity from memory. Redis vector search serves low-latency similarity queries from memory. The corpus must fit the memory budget and be rebuilt on model change. Local study-map skill 2.12 (Azure Managed Redis Vector Indexing), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Cosmos DB and PostgreSQL vector documentation: https://learn.microsoft.com/en-us/azure/cosmos-db/

- **A:** Incorrect for this question. A cache absorbs repeated reads and cuts latency for hot data. Cache keys, TTLs, and invalidation must match the freshness requirement. Why the correct answer wins: A Redis vector index performs similarity from memory.
- **B:** Incorrect for this question. A lock can serialize work across instances, but correctness under retries still needs idempotency keys in the data store. Locks expire and can be lost. Why the correct answer wins: A Redis vector index performs similarity from memory.
- **C:** Incorrect for this question. Session storage in Redis survives instance restarts and supports distributed instances. Sessions must be scoped and expiring. Why the correct answer wins: A Redis vector index performs similarity from memory.
- **D:** Correct. Redis vector search serves low-latency similarity queries from memory. The corpus must fit the memory budget and be rebuilt on model change. In this case: A Redis vector index performs similarity from memory.

### Question 23 — A, B

Answers: Query through the Cosmos DB SDK with parameterized queries; Batch related writes in a transactional batch within one partition key. SDK calls keep the client supported, and a transactional batch gives all-or-nothing within one partition key. SDK queries keep the client on the supported data plane and parameterization avoids injection and plan churn. Cross-partition queries still cost more. A transactional batch applies all-or-nothing within a single partition key. It cannot span partitions and still consumes RU per operation. Local study-map skill 2.1 (Cosmos DB SDK Access and Queries), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Cosmos DB and PostgreSQL vector documentation: https://learn.microsoft.com/en-us/azure/cosmos-db/

- **A:** Correct. SDK queries keep the client on the supported data plane and parameterization avoids injection and plan churn. Cross-partition queries still cost more. In this case: SDK calls keep the client supported, and a transactional batch gives all-or-nothing within one partition key.
- **B:** Correct. A transactional batch applies all-or-nothing within a single partition key. It cannot span partitions and still consumes RU per operation. In this case: SDK calls keep the client supported, and a transactional batch gives all-or-nothing within one partition key.
- **C:** Incorrect for this question. A duplicate-detection window drops repeated sends within the window, which helps with at-least-once producers. The window is time-bounded. Why the correct answer wins: SDK calls keep the client supported, and a transactional batch gives all-or-nothing within one partition key.
- **D:** Incorrect for this question. Leases track partition ownership so multiple processor instances share work and resume from a continuation token. Lease writes consume RUs too. Why the correct answer wins: SDK calls keep the client supported, and a transactional batch gives all-or-nothing within one partition key.
- **E:** Incorrect for this question. Autoscale follows demand between a minimum and maximum, avoiding throttling at peak without paying for peak all day. The maximum still caps the bill. Why the correct answer wins: SDK calls keep the client supported, and a transactional batch gives all-or-nothing within one partition key.

### Question 24 — B, E

Answers: Create an IVFFlat index to save memory on a large table; Increase maintenance and query memory settings for index builds and sorts. IVFFlat reduces memory use with periodic rebuilds, and adequate work memory prevents spills. IVFFlat uses clustering lists and needs periodic rebuilds as data grows, but costs less memory than HNSW. Probes trade recall for speed. Index builds and large sorts spill to disk when work memory is too small, stretching maintenance windows and slowing queries. Local study-map skill 2.7 (pgvector Indexing and Query Latency), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Cosmos DB and PostgreSQL vector documentation: https://learn.microsoft.com/en-us/azure/cosmos-db/

- **A:** Incorrect for this question. Index creation and bulk loads are I/O heavy, and throttled storage stretches maintenance windows. Storage limits are separate from compute. Why the correct answer wins: IVFFlat reduces memory use with periodic rebuilds, and adequate work memory prevents spills.
- **B:** Correct. Index builds and large sorts spill to disk when work memory is too small, stretching maintenance windows and slowing queries. In this case: IVFFlat reduces memory use with periodic rebuilds, and adequate work memory prevents spills.
- **C:** Incorrect for this question. An exact scan is accurate but scales linearly and burns compute. It is a baseline for measuring recall, not a production strategy. Why the correct answer wins: IVFFlat reduces memory use with periodic rebuilds, and adequate work memory prevents spills.
- **D:** Incorrect for this question. HNSW gives fast approximate nearest-neighbour queries with a larger memory footprint and slower builds. Recall is tunable at query time. Why the correct answer wins: IVFFlat reduces memory use with periodic rebuilds, and adequate work memory prevents spills.
- **E:** Correct. IVFFlat uses clustering lists and needs periodic rebuilds as data grows, but costs less memory than HNSW. Probes trade recall for speed. In this case: IVFFlat reduces memory use with periodic rebuilds, and adequate work memory prevents spills.

### Question 25 — B

Answer: Create the container with a vector policy → upsert items with embeddings → query with VectorDistance → apply metadata filters. The container and its vector policy must exist before embeddings are written, and writes must precede similarity queries. The vector policy fixes dimensions and index type, so it must exist before vector writes and queries. Local study-map skill 2.4 (Cosmos DB Vector Search and Embeddings), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Cosmos DB and PostgreSQL vector documentation: https://learn.microsoft.com/en-us/azure/cosmos-db/

- **A:** Incorrect for this question. Filtering and querying cannot precede the container and its vector data. Why the correct answer wins: The container and its vector policy must exist before embeddings are written, and writes must precede similarity queries.
- **B:** Correct. The vector policy fixes dimensions and index type, so it must exist before vector writes and queries. In this case: The container and its vector policy must exist before embeddings are written, and writes must precede similarity queries.
- **C:** Incorrect for this question. A similarity query needs indexed vectors, which require the container and its policy first. Why the correct answer wins: The container and its vector policy must exist before embeddings are written, and writes must precede similarity queries.
- **D:** Incorrect for this question. Items cannot be written before the container exists with a matching vector policy. Why the correct answer wins: The container and its vector policy must exist before embeddings are written, and writes must precede similarity queries.

### Question 26 — C

Answer: Queue the work on a Service Bus queue and process it with a worker. A queue with peek-lock completion provides at-least-once processing and workload recovery. A queue decouples producers from a single consumer group and smooths bursts. Delivery semantics depend on receive mode and completion. Local study-map skill 3.1 (Service Bus Queues and Sessions), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure messaging and Functions documentation: https://learn.microsoft.com/en-us/azure/service-bus-messaging/

- **A:** Incorrect for this question. Event Hubs ingests high-volume ordered streams with partitions and consumer groups. It is a streaming log, not a task queue. Why the correct answer wins: A queue with peek-lock completion provides at-least-once processing and workload recovery.
- **B:** Incorrect for this question. Queue Storage is simple and cheap for large backlogs with at-least-once delivery. It lacks topics, sessions, and scheduled messages. Why the correct answer wins: A queue with peek-lock completion provides at-least-once processing and workload recovery.
- **C:** Correct. A queue decouples producers from a single consumer group and smooths bursts. Delivery semantics depend on receive mode and completion. In this case: A queue with peek-lock completion provides at-least-once processing and workload recovery.
- **D:** Incorrect for this question. Topics fan out one message to independent subscribers, each with its own filter and dead-letter queue. Subscribers process at their own pace. Why the correct answer wins: A queue with peek-lock completion provides at-least-once processing and workload recovery.

### Question 27 — D

Answer: Use Service Bus sessions to keep related messages ordered. Sessions give ordered, exclusive processing per machine. Sessions give ordered, exclusive processing per session ID across competing consumers. They require session-aware senders and receivers. Local study-map skill 3.1 (Service Bus Queues and Sessions), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure messaging and Functions documentation: https://learn.microsoft.com/en-us/azure/service-bus-messaging/

- **A:** Incorrect for this question. A delivery cap stops infinite retries of a failing message and moves it to the dead-letter queue. The cap must exceed legitimate transient retries. Why the correct answer wins: Sessions give ordered, exclusive processing per machine.
- **B:** Incorrect for this question. A duplicate-detection window drops repeated sends within the window, which helps with at-least-once producers. The window is time-bounded. Why the correct answer wins: Sessions give ordered, exclusive processing per machine.
- **C:** Incorrect for this question. Peek-lock keeps the message locked until the handler completes it, giving at-least-once processing with retry. Lock duration must exceed processing time. Why the correct answer wins: Sessions give ordered, exclusive processing per machine.
- **D:** Correct. Sessions give ordered, exclusive processing per session ID across competing consumers. They require session-aware senders and receivers. In this case: Sessions give ordered, exclusive processing per machine.

### Question 28 — D

Answer: Publish to a Service Bus topic with multiple subscriptions. A topic with separate subscriptions provides fan-out. Topics fan out one message to independent subscribers, each with its own filter and dead-letter queue. Subscribers process at their own pace. Local study-map skill 3.2 (Service Bus Topics, Subscriptions, and Filters), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure messaging and Functions documentation: https://learn.microsoft.com/en-us/azure/service-bus-messaging/

- **A:** Incorrect for this question. A custom schema fits domain events that are not resource lifecycle notifications. Consumers must version the schema contract. Why the correct answer wins: A topic with separate subscriptions provides fan-out.
- **B:** Incorrect for this question. Queue Storage is simple and cheap for large backlogs with at-least-once delivery. It lacks topics, sessions, and scheduled messages. Why the correct answer wins: A topic with separate subscriptions provides fan-out.
- **C:** Incorrect for this question. A queue decouples producers from a single consumer group and smooths bursts. Delivery semantics depend on receive mode and completion. Why the correct answer wins: A topic with separate subscriptions provides fan-out.
- **D:** Correct. Topics fan out one message to independent subscribers, each with its own filter and dead-letter queue. Subscribers process at their own pace. In this case: A topic with separate subscriptions provides fan-out.

### Question 29 — D

Answer: Rely on Event Grid retries with a dead-letter destination. Event Grid retries failed deliveries and can dead-letter what never succeeds. Event Grid retries failed deliveries with backoff and can store undeliverable events. Handlers must still be idempotent. Local study-map skill 3.4 (Event Grid Filters, Custom Events, and Retries), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure messaging and Functions documentation: https://learn.microsoft.com/en-us/azure/service-bus-messaging/

- **A:** Incorrect for this question. Subject and event-type filters keep handlers focused and reduce cost. Filters are evaluated on event metadata, not payload body. Why the correct answer wins: Event Grid retries failed deliveries and can dead-letter what never succeeds.
- **B:** Incorrect for this question. A custom schema fits domain events that are not resource lifecycle notifications. Consumers must version the schema contract. Why the correct answer wins: Event Grid retries failed deliveries and can dead-letter what never succeeds.
- **C:** Incorrect for this question. Identity-based delivery removes a shared key from the subscription. The receiver still validates the caller and payload. Why the correct answer wins: Event Grid retries failed deliveries and can dead-letter what never succeeds.
- **D:** Correct. Event Grid retries failed deliveries with backoff and can store undeliverable events. Handlers must still be idempotent. In this case: Event Grid retries failed deliveries and can dead-letter what never succeeds.

### Question 30 — A

Answer: Bind a queue or event trigger to the function. A queue trigger starts the function and manages the receive loop. A trigger starts the function when work arrives and handles the receive loop for you. Poison-message behavior is configured in host settings. Local study-map skill 3.5 (Azure Functions Triggers and Bindings), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure messaging and Functions documentation: https://learn.microsoft.com/en-us/azure/service-bus-messaging/

- **A:** Correct. A trigger starts the function when work arrives and handles the receive loop for you. Poison-message behavior is configured in host settings. In this case: A queue trigger starts the function and manages the receive loop.
- **B:** Incorrect for this question. Durable Functions provides orchestrations, activities, timers, and retries with checkpointed state. Orchestrator code must stay deterministic. Why the correct answer wins: A queue trigger starts the function and manages the receive loop.
- **C:** Incorrect for this question. An HTTP trigger gives a synchronous API endpoint with route and authorization configuration. Long-running work should hand off to a queue. Why the correct answer wins: A queue trigger starts the function and manages the receive loop.
- **D:** Incorrect for this question. Bindings reduce boilerplate for common inputs and outputs and are configured declaratively. Complex operations still need the SDK. Why the correct answer wins: A queue trigger starts the function and manages the receive loop.

### Question 31 — C

Answer: Use input and output bindings instead of hand-written SDK calls. An output binding declares the write target declaratively. Bindings reduce boilerplate for common inputs and outputs and are configured declaratively. Complex operations still need the SDK. Local study-map skill 3.5 (Azure Functions Triggers and Bindings), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure messaging and Functions documentation: https://learn.microsoft.com/en-us/azure/service-bus-messaging/

- **A:** Incorrect for this question. A premium plan reduces cold starts and supports virtual network integration and longer timeouts. It costs more than consumption. Why the correct answer wins: An output binding declares the write target declaratively.
- **B:** Incorrect for this question. A trigger starts the function when work arrives and handles the receive loop for you. Poison-message behavior is configured in host settings. Why the correct answer wins: An output binding declares the write target declaratively.
- **C:** Correct. Bindings reduce boilerplate for common inputs and outputs and are configured declaratively. Complex operations still need the SDK. In this case: An output binding declares the write target declaratively.
- **D:** Incorrect for this question. Durable Functions provides orchestrations, activities, timers, and retries with checkpointed state. Orchestrator code must stay deterministic. Why the correct answer wins: An output binding declares the write target declaratively.

### Question 32 — A

Answer: Host the function app on a premium plan with pre-warmed instances. A premium plan provides pre-warmed instances and virtual network integration. A premium plan reduces cold starts and supports virtual network integration and longer timeouts. It costs more than consumption. Local study-map skill 3.6 (Function App Configuration and Deployment), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure messaging and Functions documentation: https://learn.microsoft.com/en-us/azure/service-bus-messaging/

- **A:** Correct. A premium plan reduces cold starts and supports virtual network integration and longer timeouts. It costs more than consumption. In this case: A premium plan provides pre-warmed instances and virtual network integration.
- **B:** Incorrect for this question. A staging slot lets a new build warm up and be validated before the swap. Slot settings that must not move are marked sticky. Why the correct answer wins: A premium plan provides pre-warmed instances and virtual network integration.
- **C:** Incorrect for this question. Durable Functions provides orchestrations, activities, timers, and retries with checkpointed state. Orchestrator code must stay deterministic. Why the correct answer wins: A premium plan provides pre-warmed instances and virtual network integration.
- **D:** Incorrect for this question. Consumption bills per execution and scales automatically, with cold starts and a timeout ceiling. It fits spiky, short work. Why the correct answer wins: A premium plan provides pre-warmed instances and virtual network integration.

### Question 33 — A, D

Answers: Publish to a Service Bus topic with multiple subscriptions; Add a SQL or correlation filter to a subscription. A topic provides fan-out, and a subscription filter narrows what one subscriber receives. Topics fan out one message to independent subscribers, each with its own filter and dead-letter queue. Subscribers process at their own pace. Subscription filters route only matching messages to a handler, reducing wasted processing. Filter evaluation happens broker-side on message properties. Local study-map skill 3.2 (Service Bus Topics, Subscriptions, and Filters), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure messaging and Functions documentation: https://learn.microsoft.com/en-us/azure/service-bus-messaging/

- **A:** Correct. Topics fan out one message to independent subscribers, each with its own filter and dead-letter queue. Subscribers process at their own pace. In this case: A topic provides fan-out, and a subscription filter narrows what one subscriber receives.
- **B:** Incorrect for this question. A queue decouples producers from a single consumer group and smooths bursts. Delivery semantics depend on receive mode and completion. Why the correct answer wins: A topic provides fan-out, and a subscription filter narrows what one subscriber receives.
- **C:** Incorrect for this question. Subject and event-type filters keep handlers focused and reduce cost. Filters are evaluated on event metadata, not payload body. Why the correct answer wins: A topic provides fan-out, and a subscription filter narrows what one subscriber receives.
- **D:** Correct. Subscription filters route only matching messages to a handler, reducing wasted processing. Filter evaluation happens broker-side on message properties. In this case: A topic provides fan-out, and a subscription filter narrows what one subscriber receives.
- **E:** Incorrect for this question. Queue Storage is simple and cheap for large backlogs with at-least-once delivery. It lacks topics, sessions, and scheduled messages. Why the correct answer wins: A topic provides fan-out, and a subscription filter narrows what one subscriber receives.

### Question 34 — C, E

Answers: Orchestrate the multi-step workflow with Durable Functions; Bind a queue or event trigger to the function. Durable orchestration checkpoints progress, and a queue trigger starts the workflow. Durable Functions provides orchestrations, activities, timers, and retries with checkpointed state. Orchestrator code must stay deterministic. A trigger starts the function when work arrives and handles the receive loop for you. Poison-message behavior is configured in host settings. Local study-map skill 3.5 (Azure Functions Triggers and Bindings), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure messaging and Functions documentation: https://learn.microsoft.com/en-us/azure/service-bus-messaging/

- **A:** Incorrect for this question. An HTTP trigger gives a synchronous API endpoint with route and authorization configuration. Long-running work should hand off to a queue. Why the correct answer wins: Durable orchestration checkpoints progress, and a queue trigger starts the workflow.
- **B:** Incorrect for this question. Consumption bills per execution and scales automatically, with cold starts and a timeout ceiling. It fits spiky, short work. Why the correct answer wins: Durable orchestration checkpoints progress, and a queue trigger starts the workflow.
- **C:** Correct. Durable Functions provides orchestrations, activities, timers, and retries with checkpointed state. Orchestrator code must stay deterministic. In this case: Durable orchestration checkpoints progress, and a queue trigger starts the workflow.
- **D:** Incorrect for this question. Bindings reduce boilerplate for common inputs and outputs and are configured declaratively. Complex operations still need the SDK. Why the correct answer wins: Durable orchestration checkpoints progress, and a queue trigger starts the workflow.
- **E:** Correct. A trigger starts the function when work arrives and handles the receive loop for you. Poison-message behavior is configured in host settings. In this case: Durable orchestration checkpoints progress, and a queue trigger starts the workflow.

### Question 35 — C

Answer: Publish the message → receive with peek-lock → process the work → complete the message → dead-letter after the delivery limit. Receive, process, complete, and dead-letter only after the limit. Peek-lock keeps the message until the handler succeeds, and only repeated failures should dead-letter it. Local study-map skill 3.1 (Service Bus Queues and Sessions), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure messaging and Functions documentation: https://learn.microsoft.com/en-us/azure/service-bus-messaging/

- **A:** Incorrect for this question. The message cannot be received before it is published, and completion must follow processing. Why the correct answer wins: Receive, process, complete, and dead-letter only after the limit.
- **B:** Incorrect for this question. Work cannot be processed before the message is published and received. Why the correct answer wins: Receive, process, complete, and dead-letter only after the limit.
- **C:** Correct. Peek-lock keeps the message until the handler succeeds, and only repeated failures should dead-letter it. In this case: Receive, process, complete, and dead-letter only after the limit.
- **D:** Incorrect for this question. Completing a message before processing discards the work and defeats at-least-once delivery. Why the correct answer wins: Receive, process, complete, and dead-letter only after the limit.

### Question 36 — A

Answer: Store the secret in Azure Key Vault and read it at runtime. Key Vault stores the token with access control and audit. A vault centralizes secret storage with access control and audit. Retrieval should use an identity, not a copied credential. Local study-map skill 4.1 (Key Vault Secret Storage, Rotation, and Retrieval), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Key Vault, App Configuration, and Monitor documentation: https://learn.microsoft.com/en-us/azure/azure-monitor/

- **A:** Correct. A vault centralizes secret storage with access control and audit. Retrieval should use an identity, not a copied credential. In this case: Key Vault stores the token with access control and audit.
- **B:** Incorrect for this question. Pinning a version makes a rotation invisible to the app until it is redeployed, which is useful for break-glass and dangerous for routine rotation. Why the correct answer wins: Key Vault stores the token with access control and audit.
- **C:** Incorrect for this question. App Configuration separates configuration from code and supports labels, feature flags, and Key Vault references. Change still needs a refresh strategy. Why the correct answer wins: Key Vault stores the token with access control and audit.
- **D:** Incorrect for this question. Application settings become environment variables for the container and can be swapped per slot. Sensitive values should still reference a vault. Why the correct answer wins: Key Vault stores the token with access control and audit.

### Question 37 — D

Answer: Grant the app identity data-plane access to the vault. A data-plane role or policy for that identity is required before the secret can be read. Vault access is a separate authorization decision from the app identity. Without a data-plane role or policy the reference fails at runtime. Local study-map skill 4.1 (Key Vault Secret Storage, Rotation, and Retrieval), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Key Vault, App Configuration, and Monitor documentation: https://learn.microsoft.com/en-us/azure/azure-monitor/

- **A:** Incorrect for this question. A managed identity issues tokens from the platform, removing secret distribution from the app. Role assignment still scopes what it can reach. Why the correct answer wins: A data-plane role or policy for that identity is required before the secret can be read.
- **B:** Incorrect for this question. Soft delete and purge protection stop accidental or malicious permanent loss of secrets. They also constrain how names can be reused. Why the correct answer wins: A data-plane role or policy for that identity is required before the secret can be read.
- **C:** Incorrect for this question. A scoped role grants only the operations the app performs and limits blast radius. Prefer built-in roles over broad contributor grants. Why the correct answer wins: A data-plane role or policy for that identity is required before the secret can be read.
- **D:** Correct. Vault access is a separate authorization decision from the app identity. Without a data-plane role or policy the reference fails at runtime. In this case: A data-plane role or policy for that identity is required before the secret can be read.

### Question 38 — A

Answer: Store settings and feature flags in Azure App Configuration. App Configuration stores per-environment settings with refresh support. App Configuration separates configuration from code and supports labels, feature flags, and Key Vault references. Change still needs a refresh strategy. Local study-map skill 4.2 (App Configuration Settings and Feature Flags), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Key Vault, App Configuration, and Monitor documentation: https://learn.microsoft.com/en-us/azure/azure-monitor/

- **A:** Correct. App Configuration separates configuration from code and supports labels, feature flags, and Key Vault references. Change still needs a refresh strategy. In this case: App Configuration stores per-environment settings with refresh support.
- **B:** Incorrect for this question. Sentinel-key or polling refresh lets a running app pick up new settings. Refresh intervals trade responsiveness against request volume. Why the correct answer wins: App Configuration stores per-environment settings with refresh support.
- **C:** Incorrect for this question. A vault centralizes secret storage with access control and audit. Retrieval should use an identity, not a copied credential. Why the correct answer wins: App Configuration stores per-environment settings with refresh support.
- **D:** Incorrect for this question. Labels keep dev, test, and prod values in one store with one key schema. A misconfigured label selector silently serves the wrong values. Why the correct answer wins: App Configuration stores per-environment settings with refresh support.

### Question 39 — C

Answer: Enable configuration refresh so changes apply without a restart. Configuration refresh lets a running app apply changed values. Sentinel-key or polling refresh lets a running app pick up new settings. Refresh intervals trade responsiveness against request volume. Local study-map skill 4.2 (App Configuration Settings and Feature Flags), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Key Vault, App Configuration, and Monitor documentation: https://learn.microsoft.com/en-us/azure/azure-monitor/

- **A:** Incorrect for this question. Labels keep dev, test, and prod values in one store with one key schema. A misconfigured label selector silently serves the wrong values. Why the correct answer wins: Configuration refresh lets a running app apply changed values.
- **B:** Incorrect for this question. Pinning a version makes a rotation invisible to the app until it is redeployed, which is useful for break-glass and dangerous for routine rotation. Why the correct answer wins: Configuration refresh lets a running app apply changed values.
- **C:** Correct. Sentinel-key or polling refresh lets a running app pick up new settings. Refresh intervals trade responsiveness against request volume. In this case: Configuration refresh lets a running app apply changed values.
- **D:** Incorrect for this question. Pipeline deployment keeps code and configuration versioned together and repeatable. Secrets belong in a vault reference, not in the pipeline file. Why the correct answer wins: Configuration refresh lets a running app apply changed values.

### Question 40 — B

Answer: Instrument the service with the OpenTelemetry SDK. OpenTelemetry instrumentation with context propagation produces one end-to-end trace. OpenTelemetry emits vendor-neutral traces, metrics, and logs with context propagation. Exporters and sampling decide what reaches the backend. Local study-map skill 4.3 (Distributed Tracing with OpenTelemetry), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Key Vault, App Configuration, and Monitor documentation: https://learn.microsoft.com/en-us/azure/azure-monitor/

- **A:** Incorrect for this question. Platform logs and metrics must be routed before they can be queried or alerted on. Retention and cost follow the workspace settings. Why the correct answer wins: OpenTelemetry instrumentation with context propagation produces one end-to-end trace.
- **B:** Correct. OpenTelemetry emits vendor-neutral traces, metrics, and logs with context propagation. Exporters and sampling decide what reaches the backend. In this case: OpenTelemetry instrumentation with context propagation produces one end-to-end trace.
- **C:** Incorrect for this question. Application Insights correlates requests, dependencies, and exceptions into end-to-end transactions. Sampling can hide rare failures. Why the correct answer wins: OpenTelemetry instrumentation with context propagation produces one end-to-end trace.
- **D:** Incorrect for this question. KQL filters, projects, and aggregates log and metric tables in Log Analytics. Start narrow with a time range and a request ID. Why the correct answer wins: OpenTelemetry instrumentation with context propagation produces one end-to-end trace.

### Question 41 — B

Answer: Assign a least-privilege role to the application identity. Split identities and scope the app identity to read-only access. A scoped role grants only the operations the app performs and limits blast radius. Prefer built-in roles over broad contributor grants. Local study-map skill 4.5 (Identity-Based Access for Application Services), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Key Vault, App Configuration, and Monitor documentation: https://learn.microsoft.com/en-us/azure/azure-monitor/

- **A:** Incorrect for this question. A private endpoint keeps traffic on the virtual network and removes public exposure. DNS resolution must be wired to the private zone. Why the correct answer wins: Split identities and scope the app identity to read-only access.
- **B:** Correct. A scoped role grants only the operations the app performs and limits blast radius. Prefer built-in roles over broad contributor grants. In this case: Split identities and scope the app identity to read-only access.
- **C:** Incorrect for this question. A managed identity issues tokens from the platform, removing secret distribution from the app. Role assignment still scopes what it can reach. Why the correct answer wins: Split identities and scope the app identity to read-only access.
- **D:** Incorrect for this question. A vault centralizes secret storage with access control and audit. Retrieval should use an identity, not a copied credential. Why the correct answer wins: Split identities and scope the app identity to read-only access.

### Question 42 — A, C

Answers: Instrument the service with the OpenTelemetry SDK; Propagate trace context across every service and queue hop. SDK instrumentation emits spans, and context propagation in message headers keeps the trace connected. OpenTelemetry emits vendor-neutral traces, metrics, and logs with context propagation. Exporters and sampling decide what reaches the backend. Propagation stitches one trace across HTTP, messaging, and Functions so the whole path is visible. Missing propagation breaks the trace at that hop. Local study-map skill 4.3 (Distributed Tracing with OpenTelemetry), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Key Vault, App Configuration, and Monitor documentation: https://learn.microsoft.com/en-us/azure/azure-monitor/

- **A:** Correct. Propagation stitches one trace across HTTP, messaging, and Functions so the whole path is visible. Missing propagation breaks the trace at that hop. In this case: SDK instrumentation emits spans, and context propagation in message headers keeps the trace connected.
- **B:** Incorrect for this question. Sampling keeps telemetry cost bounded, but aggressive sampling can hide rare failures. Tail sampling can retain errors preferentially. Why the correct answer wins: SDK instrumentation emits spans, and context propagation in message headers keeps the trace connected.
- **C:** Correct. OpenTelemetry emits vendor-neutral traces, metrics, and logs with context propagation. Exporters and sampling decide what reaches the backend. In this case: SDK instrumentation emits spans, and context propagation in message headers keeps the trace connected.
- **D:** Incorrect for this question. Platform logs and metrics must be routed before they can be queried or alerted on. Retention and cost follow the workspace settings. Why the correct answer wins: SDK instrumentation emits spans, and context propagation in message headers keeps the trace connected.
- **E:** Incorrect for this question. KQL filters, projects, and aggregates log and metric tables in Log Analytics. Start narrow with a time range and a request ID. Why the correct answer wins: SDK instrumentation emits spans, and context propagation in message headers keeps the trace connected.

### Question 43 — A, C

Answers: Store the secret in Azure Key Vault and read it at runtime; Authenticate with a managed identity instead of a stored key. Store the value in Key Vault, then let a managed identity read it. A vault centralizes secret storage with access control and audit. Retrieval should use an identity, not a copied credential. A managed identity issues tokens from the platform, removing secret distribution from the app. Role assignment still scopes what it can reach. Local study-map skill 4.1 (Key Vault Secret Storage, Rotation, and Retrieval), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Key Vault, App Configuration, and Monitor documentation: https://learn.microsoft.com/en-us/azure/azure-monitor/

- **A:** Correct. A managed identity issues tokens from the platform, removing secret distribution from the app. Role assignment still scopes what it can reach. In this case: Store the value in Key Vault, then let a managed identity read it.
- **B:** Incorrect for this question. Labels keep dev, test, and prod values in one store with one key schema. A misconfigured label selector silently serves the wrong values. Why the correct answer wins: Store the value in Key Vault, then let a managed identity read it.
- **C:** Correct. A vault centralizes secret storage with access control and audit. Retrieval should use an identity, not a copied credential. In this case: Store the value in Key Vault, then let a managed identity read it.
- **D:** Incorrect for this question. Pinning a version makes a rotation invisible to the app until it is redeployed, which is useful for break-glass and dangerous for routine rotation. Why the correct answer wins: Store the value in Key Vault, then let a managed identity read it.
- **E:** Incorrect for this question. App Configuration separates configuration from code and supports labels, feature flags, and Key Vault references. Change still needs a refresh strategy. Why the correct answer wins: Store the value in Key Vault, then let a managed identity read it.

### Question 44 — D

Answer: Store the secret in Key Vault → grant the app identity access → reference the secret from the app → rotate the secret → the app reads the new version. The secret is stored, access is granted, the app references it, and only then is it rotated. Access must be granted before the reference resolves, and the app must read the current version after rotation. Local study-map skill 4.1 (Key Vault Secret Storage, Rotation, and Retrieval), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Key Vault, App Configuration, and Monitor documentation: https://learn.microsoft.com/en-us/azure/azure-monitor/

- **A:** Incorrect for this question. A reference cannot resolve before the secret and the access grant exist. Why the correct answer wins: The secret is stored, access is granted, the app references it, and only then is it rotated.
- **B:** Incorrect for this question. Access can be granted first, but rotation cannot precede storing the secret. Why the correct answer wins: The secret is stored, access is granted, the app references it, and only then is it rotated.
- **C:** Incorrect for this question. There is nothing to rotate or reference before the secret is stored. Why the correct answer wins: The secret is stored, access is granted, the app references it, and only then is it rotated.
- **D:** Correct. Access must be granted before the reference resolves, and the app must read the current version after rotation. In this case: The secret is stored, access is granted, the app references it, and only then is it rotated.

### Question 45 — C

Answer: Filter on metadata columns in the same query as the vector search. Filtering inside the vector query enforces scope without shrinking the result set after the fact. Combining a WHERE filter with the distance operator keeps retrieval inside the caller's scope and improves relevance. Index the filter columns too. Local study-map skill 2.9 (PostgreSQL RAG with Metadata Filters), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Cosmos DB and PostgreSQL vector documentation: https://learn.microsoft.com/en-us/azure/cosmos-db/

- **A:** Incorrect for this question. An exact scan is accurate but scales linearly and burns compute. It is a baseline for measuring recall, not a production strategy. Why the correct answer wins: Filtering inside the vector query enforces scope without shrinking the result set after the fact.
- **B:** Incorrect for this question. Post-filtering can return fewer results than requested and can leak existence or counts if the filtering is careless. Push authorization into the query. Why the correct answer wins: Filtering inside the vector query enforces scope without shrinking the result set after the fact.
- **C:** Correct. Combining a WHERE filter with the distance operator keeps retrieval inside the caller's scope and improves relevance. Index the filter columns too. In this case: Filtering inside the vector query enforces scope without shrinking the result set after the fact.
- **D:** Incorrect for this question. HNSW gives fast approximate nearest-neighbour queries with a larger memory footprint and slower builds. Recall is tunable at query time. Why the correct answer wins: Filtering inside the vector query enforces scope without shrinking the result set after the fact.

### Question 46 — B

Answer: Inspect the dead-letter queue and resubmit corrected messages. Dead-lettering keeps the failing message out of the active queue for later diagnosis. Dead-lettering preserves poison messages for diagnosis instead of losing them. Resubmission needs a fix and an idempotent handler. Local study-map skill 3.3 (Service Bus Dead-Lettering and Retries), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure messaging and Functions documentation: https://learn.microsoft.com/en-us/azure/service-bus-messaging/

- **A:** Incorrect for this question. A delivery cap stops infinite retries of a failing message and moves it to the dead-letter queue. The cap must exceed legitimate transient retries. Why the correct answer wins: Dead-lettering keeps the failing message out of the active queue for later diagnosis.
- **B:** Correct. Dead-lettering preserves poison messages for diagnosis instead of losing them. Resubmission needs a fix and an idempotent handler. In this case: Dead-lettering keeps the failing message out of the active queue for later diagnosis.
- **C:** Incorrect for this question. A duplicate-detection window drops repeated sends within the window, which helps with at-least-once producers. The window is time-bounded. Why the correct answer wins: Dead-lettering keeps the failing message out of the active queue for later diagnosis.
- **D:** Incorrect for this question. Receive-and-delete removes the message on delivery, so a crash loses work silently. It suits telemetry, not payments. Why the correct answer wins: Dead-lettering keeps the failing message out of the active queue for later diagnosis.

### Question 47 — B

Answer: Aggregate with summarize and bin to see the failure rate over time. Binning with summarize produces per-interval counts. Time-binned aggregation reveals the shape of an incident: a step change, a ramp, or a periodic spike. Averages alone hide short outages. Local study-map skill 4.4 (KQL Queries for Logs and Metrics), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Key Vault, App Configuration, and Monitor documentation: https://learn.microsoft.com/en-us/azure/azure-monitor/

- **A:** Incorrect for this question. Reducing columns and rows early lowers query cost and latency. Broad queries over long ranges are the usual cause of slow KQL. Why the correct answer wins: Binning with summarize produces per-interval counts.
- **B:** Correct. Time-binned aggregation reveals the shape of an incident: a step change, a ramp, or a periodic spike. Averages alone hide short outages. In this case: Binning with summarize produces per-interval counts.
- **C:** Incorrect for this question. Precomputed results avoid recomputing expensive aggregations on every dashboard refresh. The trade-off is storage and freshness lag. Why the correct answer wins: Binning with summarize produces per-interval counts.
- **D:** Incorrect for this question. Joining request and dependency telemetry shows which downstream call fails inside a slow request. Cross-workspace joins need the right scope. Why the correct answer wins: Binning with summarize produces per-interval counts.

### Question 48 — B

Answer: Test end-to-end connectivity from inside the container to each dependency. Testing from inside the pod proves DNS, egress, and network rules that a workstation test bypasses. Reaching a dependency from the pod or replica proves DNS, egress, and firewall paths together. Host-side tests can succeed while the container path fails. Local study-map skill 1.7 (Container Logs, Events, and Connectivity), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure container hosting documentation: https://learn.microsoft.com/en-us/azure/container-apps/

- **A:** Incorrect for this question. A private endpoint keeps traffic on the virtual network and removes public exposure. DNS resolution must be wired to the private zone. Why the correct answer wins: Testing from inside the pod proves DNS, egress, and network rules that a workstation test bypasses.
- **B:** Correct. Reaching a dependency from the pod or replica proves DNS, egress, and firewall paths together. Host-side tests can succeed while the container path fails. In this case: Testing from inside the pod proves DNS, egress, and network rules that a workstation test bypasses.
- **C:** Incorrect for this question. Readiness gates traffic until the app can serve it, and liveness restarts a wedged container. Wrong thresholds cause restart loops. Why the correct answer wins: Testing from inside the pod proves DNS, egress, and network rules that a workstation test bypasses.
- **D:** Incorrect for this question. A private endpoint needs matching name resolution or clients still resolve the public address. The zone must be linked to the workload network. Why the correct answer wins: Testing from inside the pod proves DNS, egress, and network rules that a workstation test bypasses.

### Question 49 — D

Answer: Filter the Event Grid subscription by subject or event type. A subject or property filter narrows delivery to matching events. Subject and event-type filters keep handlers focused and reduce cost. Filters are evaluated on event metadata, not payload body. Local study-map skill 3.4 (Event Grid Filters, Custom Events, and Retries), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure messaging and Functions documentation: https://learn.microsoft.com/en-us/azure/service-bus-messaging/

- **A:** Incorrect for this question. Subscription filters route only matching messages to a handler, reducing wasted processing. Filter evaluation happens broker-side on message properties. Why the correct answer wins: A subject or property filter narrows delivery to matching events.
- **B:** Incorrect for this question. A duplicate-detection window drops repeated sends within the window, which helps with at-least-once producers. The window is time-bounded. Why the correct answer wins: A subject or property filter narrows delivery to matching events.
- **C:** Incorrect for this question. Event Grid retries failed deliveries with backoff and can store undeliverable events. Handlers must still be idempotent. Why the correct answer wins: A subject or property filter narrows delivery to matching events.
- **D:** Correct. Subject and event-type filters keep handlers focused and reduce cost. Filters are evaluated on event metadata, not payload body. In this case: A subject or property filter narrows delivery to matching events.

### Question 50 — A

Answer: Query the workspace with KQL to find the failing operation. A KQL query over request telemetry returns that filtered, ordered list. KQL filters, projects, and aggregates log and metric tables in Log Analytics. Start narrow with a time range and a request ID. Local study-map skill 4.4 (KQL Queries for Logs and Metrics), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Key Vault, App Configuration, and Monitor documentation: https://learn.microsoft.com/en-us/azure/azure-monitor/

- **A:** Correct. KQL filters, projects, and aggregates log and metric tables in Log Analytics. Start narrow with a time range and a request ID. In this case: A KQL query over request telemetry returns that filtered, ordered list.
- **B:** Incorrect for this question. Platform metrics are cheap and near-real-time, so they suit latency and failure-rate alerts. Log-based alerts add latency and query cost. Why the correct answer wins: A KQL query over request telemetry returns that filtered, ordered list.
- **C:** Incorrect for this question. Time-binned aggregation reveals the shape of an incident: a step change, a ramp, or a periodic spike. Averages alone hide short outages. Why the correct answer wins: A KQL query over request telemetry returns that filtered, ordered list.
- **D:** Incorrect for this question. Reducing columns and rows early lowers query cost and latency. Broad queries over long ranges are the usual cause of slow KQL. Why the correct answer wins: A KQL query over request telemetry returns that filtered, ordered list.
