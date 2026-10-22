# Microsoft AI-200 — Full-Length Mock Exam 5

Azure AI Cloud Developer Associate · 50 questions · 120 minutes · passing target 700/1000

Blueprint-weighted mock exam. Item mix: 38 single-choice, 8 multi-select (selection count stated), 4 ordering items rendered as answer choices, and 2 case studies of 3 questions. Hot-area, drag-and-drop UI, labs, and adaptive problem-solution sets cannot be reproduced in a CSV; see the README for the exact fidelity boundary.

Original educational content, not actual, recalled, or copied Microsoft exam items.

## Questions

### 1. Every release must map to one reviewed artifact so an auditor can identify what ran. Which practice should be enforced?

Domain: Develop containerized solutions on Azure

- A. Apply an ACR retention policy to prune old untagged manifests
- B. Build and store versioned images in Azure Container Registry
- C. Run image builds on demand or on a trigger with ACR Tasks
- D. Deploy the mutable latest tag and let the platform resolve it

### 2. A weekly dependency patch must produce a fresh image without a local Docker host. What should be configured?

Domain: Develop containerized solutions on Azure

- A. Build and store versioned images in Azure Container Registry
- B. Stage the change in a deployment slot and swap after verification
- C. Replicate the registry to each deployment region
- D. Run image builds on demand or on a trigger with ACR Tasks

### 3. A small permit-status API needs platform patching, deployment slots, and no cluster administration. What should host it?

Domain: Develop containerized solutions on Azure

- A. Run the batch job in Azure Container Instances
- B. Deploy the service to Azure Container Apps
- C. Deploy the workload to Azure Kubernetes Service
- D. Deploy the image to Azure App Service as a web app

### 4. A registry credential must be usable by the container without appearing in application settings. What should be used?

Domain: Develop containerized solutions on Azure

- A. Reference a Key Vault secret from the app configuration instead of storing it
- B. Supply configuration through App Service application settings
- C. Stage the change in a deployment slot and swap after verification
- D. Deploy the image to Azure App Service as a web app

### 5. A new eligibility service must take a small share of live traffic before full rollout. Which feature provides that?

Domain: Develop containerized solutions on Azure

- A. Stage the change in a deployment slot and swap after verification
- B. Create a new Container Apps revision and shift traffic between revisions
- C. Scale the container app on an event source with a KEDA scaler
- D. Configure Container Apps ingress for internal-only access

### 6. Replica count oscillates every minute during fluctuating load and downstream calls spike on each scale-in. What should be tuned?

Domain: Develop containerized solutions on Azure

- A. Tune the scale rule cool-down period and maximum replicas
- B. Set a minimum replica count above zero for the container app
- C. Scale the container app on an event source with a KEDA scaler
- D. Rely on the horizontal pod autoscaler on CPU

### 7. The deployment must be declared in version control and reapplied safely after manual drift. What should be used?

Domain: Develop containerized solutions on Azure

- A. Apply a declarative Kubernetes manifest to the cluster
- B. Run the batch job in Azure Container Instances
- C. Add readiness and liveness probes to the pod specification
- D. Rely on the horizontal pod autoscaler on CPU

### 8. Operators need container stdout and cluster events searchable together after an incident. What should be used?

Domain: Develop containerized solutions on Azure

- A. Enable diagnostic settings to route platform logs to the workspace
- B. Test end-to-end connectivity from inside the container to each dependency
- C. Query container logs and Kubernetes events in Log Analytics
- D. Send telemetry to Application Insights and inspect the transaction view

### 9. An eligibility endpoint must support a canary and stay warm during office hours. Which two settings provide that? Select two.

Domain: Develop containerized solutions on Azure

- A. Set a minimum replica count above zero for the container app
- B. Create a new Container Apps revision and shift traffic between revisions
- C. Configure Container Apps ingress for internal-only access
- D. Tune the scale rule cool-down period and maximum replicas
- E. Rely on the horizontal pod autoscaler on CPU

### 10. Document conversion must follow queue depth, including scale to zero overnight. Which two elements are required? Select two.

Domain: Develop containerized solutions on Azure

- A. Rely on the horizontal pod autoscaler on CPU
- B. Scale the container app on an event source with a KEDA scaler
- C. Scale only on CPU utilization without an event scaler
- D. Scale on the Service Bus queue length with a KEDA Azure Service Bus scaler
- E. Run the batch job in Azure Container Instances

### 11. Which sequence correctly rolls out a canary revision of the eligibility service?

Domain: Develop containerized solutions on Azure

- A. Deploy a new revision → shift all traffic → build and push the image → check metrics → roll back
- B. Shift all traffic to a new revision → deploy the revision → check metrics → build the image → promote
- C. Build and push the image → deploy a new revision → shift a small traffic percentage → check metrics → promote or roll back
- D. Check metrics → deploy a new revision → build and push the image → shift a small traffic percentage → promote

### 12. An application file must be read by case identifier and year without scanning the container. What should the query include?

Domain: Develop AI solutions by using Azure data management services

- A. Query through the Cosmos DB SDK with parameterized queries
- B. Increase provisioned throughput and watch the RU charge per query
- C. Restrict the indexing policy to the paths the queries use
- D. Include the partition key in the query predicate

### 13. The service must query documents through the officially supported client and reuse connections. What should be used?

Domain: Develop AI solutions by using Azure data management services

- A. Enable autoscale throughput with a maximum RU limit
- B. Query through the Cosmos DB SDK with parameterized queries
- C. Use a lease container to coordinate change feed readers
- D. Batch related writes in a transactional batch within one partition key

### 14. Most properties are never filtered, but every write still pays to index them. What should be changed?

Domain: Develop AI solutions by using Azure data management services

- A. Set an item time-to-live on the container
- B. Increase provisioned throughput and watch the RU charge per query
- C. Index every property by using the default automatic policy
- D. Restrict the indexing policy to the paths the queries use

### 15. A public statistics dashboard can tolerate slightly stale counts at the lowest cost. Which level fits?

Domain: Develop AI solutions by using Azure data management services

- A. Use strong consistency for every read in the account
- B. Choose the account consistency level that matches the read requirement
- C. Use eventual consistency to minimize read cost
- D. Use session consistency for reads within the same client session

### 16. Newly submitted applications must be queued for eligibility checks without polling. What should be implemented?

Domain: Develop AI solutions by using Azure data management services

- A. Use a lease container to coordinate change feed readers
- B. Run a change feed processor to react to new and updated items
- C. Enable duplicate detection on the queue
- D. Batch related writes in a transactional batch within one partition key

### 17. Policy passages must be filtered by program and searched semantically in one statement. What should be used?

Domain: Develop AI solutions by using Azure data management services

- A. Store embeddings in PostgreSQL by using the pgvector extension
- B. Cache responses in Azure Managed Redis
- C. Scan every document and compute similarity in application code
- D. Store the documents in Azure Cosmos DB for NoSQL

### 18. A large vector table must fit a modest memory budget and periodic rebuilds are acceptable. Which index fits?

Domain: Develop AI solutions by using Azure data management services

- A. Query without a vector index and let PostgreSQL scan the table
- B. Create an IVFFlat index to save memory on a large table
- C. Increase storage throughput for index builds and bulk loads
- D. Create an HNSW index for low-latency approximate search

### 19. Index rebuilds exceed the maintenance window because storage throughput is saturated. What should be addressed?

Domain: Develop AI solutions by using Azure data management services

- A. Reuse a bounded connection pool instead of opening a connection per request
- B. Increase maintenance and query memory settings for index builds and sorts
- C. Increase storage throughput for index builds and bulk loads
- D. Scale compute and memory to fit index size and query concurrency

### 20. A burst of short-lived clients exhausts server connection slots despite a per-instance pool. What should be added?

Domain: Develop AI solutions by using Azure data management services

- A. Place a connection pooler in front of PostgreSQL for many short-lived clients
- B. Reuse a bounded connection pool instead of opening a connection per request
- C. Add a read replica and send all vector queries to it
- D. Use prepared statements and batch round trips

### 21. A fee change must be visible in cached eligibility answers immediately. What is required?

Domain: Develop AI solutions by using Azure data management services

- A. Flush the database after each deployment to guarantee fresh data
- B. Rely on the eviction policy and skip explicit TTLs
- C. Set a TTL on each cached entry
- D. Invalidate or overwrite the cache entry when the source changes

### 22. A citizen's multi-step form must keep its progress across instances and restarts. What should be used?

Domain: Develop AI solutions by using Azure data management services

- A. Create a vector index in Managed Redis for similarity search
- B. Cache responses in Azure Managed Redis
- C. Store user session state in Managed Redis with an expiry
- D. Use a distributed lock in Redis to make processing idempotent

### 23. Policy retrieval must filter on program and must not leak other programs' clauses. Which two choices are required? Select two.

Domain: Develop AI solutions by using Azure data management services

- A. Scale compute and memory to fit index size and query concurrency
- B. Model typed columns for filters and one vector column for the embedding
- C. Query without a vector index and let PostgreSQL scan the table
- D. Filter on metadata columns in the same query as the vector search
- E. Retrieve nearest neighbours first and discard unauthorized rows in the application

### 24. A hot lookup must come from memory and a similarity shortcut must avoid the relational database. Which two capabilities are required? Select two.

Domain: Develop AI solutions by using Azure data management services

- A. Use a distributed lock in Redis to make processing idempotent
- B. Cache responses in Azure Managed Redis
- C. Create a vector index in Managed Redis for similarity search
- D. Rely on the eviction policy and skip explicit TTLs
- E. Set a TTL on each cached entry

### 25. Which sequence correctly prepares policy passages for vector search?

Domain: Develop AI solutions by using Azure data management services

- A. Create the table with a vector column → query nearest neighbours → create the vector extension → build the index
- B. Query nearest neighbours → build the index → create the vector extension → create the table with a vector column
- C. Create the vector extension → create the table with a vector column → build the index → query nearest neighbours with a distance operator
- D. Build the index → create the vector extension → create the table with a vector column → query nearest neighbours

### 26. Each uploaded document must be converted by exactly one worker with crash recovery. What should be used?

Domain: Connect to and consume Azure services

- A. Use Azure Queue Storage for the work items
- B. Queue the work on a Service Bus queue and process it with a worker
- C. Stream telemetry through Azure Event Hubs
- D. Publish to a Service Bus topic with multiple subscriptions

### 27. Notification, verification, and archive services must each receive the same submission event. What should be used?

Domain: Connect to and consume Azure services

- A. Use Azure Queue Storage for the work items
- B. Publish to a Service Bus topic with multiple subscriptions
- C. Define a custom event schema for the topic
- D. Queue the work on a Service Bus queue and process it with a worker

### 28. A retried submission must not create a second case number. What should the handler use?

Domain: Connect to and consume Azure services

- A. Make the handler idempotent by using a message or business key
- B. Inspect the dead-letter queue and resubmit corrected messages
- C. Set a maximum delivery count and handle the dead-letter path
- D. Enable duplicate detection on the queue

### 29. A downstream notification endpoint is briefly offline and events must not be dropped permanently. What should be configured?

Domain: Connect to and consume Azure services

- A. Deliver events by using a managed identity instead of a key
- B. Define a custom event schema for the topic
- C. Filter the Event Grid subscription by subject or event type
- D. Rely on Event Grid retries with a dead-letter destination

### 30. A conversion function must start when a queue message arrives. What should be configured?

Domain: Connect to and consume Azure services

- A. Orchestrate the multi-step workflow with Durable Functions
- B. Use input and output bindings instead of hand-written SDK calls
- C. Bind a queue or event trigger to the function
- D. Expose the endpoint through an HTTP trigger

### 31. A spiky, short conversion task must scale automatically and cost little when idle. Which plan fits?

Domain: Connect to and consume Azure services

- A. Host the function app on a premium plan with pre-warmed instances
- B. Host the function app on the consumption plan
- C. Use a deployment slot on the function app for staging
- D. Orchestrate the multi-step workflow with Durable Functions

### 32. Function code and settings must be deployed repeatably from a pipeline with secrets kept out of the file. What should be done?

Domain: Connect to and consume Azure services

- A. Host the function app on a premium plan with pre-warmed instances
- B. Orchestrate the multi-step workflow with Durable Functions
- C. Deploy the function app through a CI pipeline with app settings applied
- D. Use a deployment slot on the function app for staging

### 33. A poison document must not block the queue and must be recoverable later. Which two capabilities provide that? Select two.

Domain: Connect to and consume Azure services

- A. Enable duplicate detection on the queue
- B. Receive in receive-and-delete mode for at-most-once delivery
- C. Set a maximum delivery count and handle the dead-letter path
- D. Use Service Bus sessions to keep related messages ordered
- E. Inspect the dead-letter queue and resubmit corrected messages

### 34. A domain event that is not a resource change must be published and routed only to the correct subscriber. Which two elements are required? Select two.

Domain: Connect to and consume Azure services

- A. Define a custom event schema for the topic
- B. Filter the Event Grid subscription by subject or event type
- C. Add a SQL or correlation filter to a subscription
- D. Deliver events by using a managed identity instead of a key
- E. Rely on Event Grid retries with a dead-letter destination

### 35. Which sequence correctly converts an uploaded document through the queue?

Domain: Connect to and consume Azure services

- A. Publish the message → complete the message → receive with peek-lock → process the work → dead-letter after the delivery limit
- B. Process the work → receive with peek-lock → publish the message → complete the message → dead-letter after the delivery limit
- C. Publish the message → receive with peek-lock → process the work → complete the message → dead-letter after the delivery limit
- D. Receive with peek-lock → publish the message → complete the message → process the work → dead-letter after the delivery limit

### 36. A deleted vault secret would break case processing for days if it were lost permanently. What should be enabled?

Domain: Secure, monitor, troubleshoot Azure solutions

- A. Assign a least-privilege role to the application identity
- B. Store the secret in Azure Key Vault and read it at runtime
- C. Enable purge protection and soft delete on the vault
- D. Pin the application to a specific secret version

### 37. A partner certificate must be replaced on a schedule with no outage. What should be implemented?

Domain: Secure, monitor, troubleshoot Azure solutions

- A. Rotate the secret on a schedule and let apps resolve the current version
- B. Supply configuration through App Service application settings
- C. Pin the application to a specific secret version
- D. Grant the app identity data-plane access to the vault

### 38. Test and production values must share one key schema in a single configuration store. What should be used?

Domain: Secure, monitor, troubleshoot Azure solutions

- A. Pin the application to a specific secret version
- B. Reference the Key Vault secret from an App Configuration key value
- C. Enable configuration refresh so changes apply without a restart
- D. Use App Configuration labels to separate environments

### 39. Telemetry must be batched, filtered, and routed to two backends without changing app code. What should be deployed?

Domain: Secure, monitor, troubleshoot Azure solutions

- A. Instrument the service with the OpenTelemetry SDK
- B. Export telemetry through an OpenTelemetry collector
- C. Use head or tail sampling so trace volume stays within budget
- D. Propagate trace context across every service and queue hop

### 40. The case database must not accept connections from the public internet. What should be configured?

Domain: Secure, monitor, troubleshoot Azure solutions

- A. Authenticate with a managed identity instead of a stored key
- B. Reach the data service through a private endpoint
- C. Enable diagnostic settings to route platform logs to the workspace
- D. Assign a least-privilege role to the application identity

### 41. The container must call storage and the database without any stored credential. What should it use?

Domain: Secure, monitor, troubleshoot Azure solutions

- A. Authenticate with a managed identity instead of a stored key
- B. Store the secret in Azure Key Vault and read it at runtime
- C. Assign a least-privilege role to the application identity
- D. Supply configuration through App Service application settings

### 42. A request path crosses an API, a queue, and a function, and one connected trace is required. Which two practices are essential? Select two.

Domain: Secure, monitor, troubleshoot Azure solutions

- A. Query the workspace with KQL to find the failing operation
- B. Propagate trace context across every service and queue hop
- C. Use head or tail sampling so trace volume stays within budget
- D. Instrument the service with the OpenTelemetry SDK
- E. Export telemetry through an OpenTelemetry collector

### 43. Log queries are slow and costly, and the team must also alert quickly on failures. Which two approaches are appropriate? Select two.

Domain: Secure, monitor, troubleshoot Azure solutions

- A. Create an alert rule on the failure rate or latency metric
- B. Project only the columns needed and filter by time first
- C. Aggregate with summarize and bin to see the failure rate over time
- D. Alert on platform metrics rather than only on log queries
- E. Store repeated aggregations in a materialized view or update policy

### 44. Which sequence correctly introduces a rotated partner secret?

Domain: Secure, monitor, troubleshoot Azure solutions

- A. Rotate the secret → reference the secret from the app → store the secret in Key Vault → grant the app identity access → the app reads the new version
- B. Store the secret in Key Vault → grant the app identity access → reference the secret from the app → rotate the secret → the app reads the new version
- C. Reference the secret from the app → rotate the secret → store the secret in Key Vault → grant the app identity access → the app reads the new version
- D. Grant the app identity access → store the secret in Key Vault → rotate the secret → reference the secret from the app → the app reads the new version

---

## Case study — CampusDesk

The next three questions refer to this scenario. Read the full scenario before answering; case-study items are scored individually.

### 45. A first implementation returns nearest neighbours and then hides rows the caller may not see, and the list comes back short. What is wrong?

Domain: Develop AI solutions by using Azure data management services

- A. Create an HNSW index for low-latency approximate search
- B. Filter on metadata columns in the same query as the vector search
- C. Query without a vector index and let PostgreSQL scan the table
- D. Retrieve nearest neighbours first and discard unauthorized rows in the application

### 46. A document with an unreadable encoding fails repeatedly and must be set aside for support. What should happen?

Domain: Connect to and consume Azure services

- A. Inspect the dead-letter queue and resubmit corrected messages
- B. Receive in receive-and-delete mode for at-most-once delivery
- C. Use Service Bus sessions to keep related messages ordered
- D. Set a maximum delivery count and handle the dead-letter path

### 47. A non-secret setting is stored centrally but its value must remain in the vault. What should be used?

Domain: Secure, monitor, troubleshoot Azure solutions

- A. Reference the Key Vault secret from an App Configuration key value
- B. Supply configuration through App Service application settings
- C. Store the secret in Azure Key Vault and read it at runtime
- D. Store settings and feature flags in Azure App Configuration

---

## Case study — CityPortal

The next three questions refer to this scenario. Read the full scenario before answering; case-study items are scored individually.

### 48. A pod resolves the database hostname to a public address and the connection is refused. What should be checked?

Domain: Develop containerized solutions on Azure

- A. Query container logs and Kubernetes events in Log Analytics
- B. Link the private DNS zone so the private endpoint name resolves
- C. Add readiness and liveness probes to the pod specification
- D. Test end-to-end connectivity from inside the container to each dependency

### 49. A handler must react when an uploaded file is created in storage, with no polling. What should it subscribe to?

Domain: Connect to and consume Azure services

- A. Subscribe to a system topic for resource events
- B. Filter the Event Grid subscription by subject or event type
- C. Rely on Event Grid retries with a dead-letter destination
- D. Define a custom event schema for the topic

### 50. A slow request is logged without an exception, and the team suspects a downstream call. Which query shape helps?

Domain: Secure, monitor, troubleshoot Azure solutions

- A. Create an alert rule on the failure rate or latency metric
- B. Project only the columns needed and filter by time first
- C. Aggregate with summarize and bin to see the failure rate over time
- D. Join the requests and dependencies tables on the operation ID

---

## Answer key and explanations

### Question 1 — B

Answer: Build and store versioned images in Azure Container Registry. Versioned tags tie production to a reviewed build. ACR keeps tagged, versioned images next to the deployment target and supports identity-based pulls. Tagging strategy and retention still need a decision. Local study-map skill 1.1 (Container Image Lifecycle in Azure Container Registry), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure container hosting documentation: https://learn.microsoft.com/en-us/azure/container-apps/

- **A:** Incorrect for this question. A retention policy controls storage growth and registry clutter. It does not change which image tag a deployment references. Why the correct answer wins: Versioned tags tie production to a reviewed build.
- **B:** Correct. ACR keeps tagged, versioned images next to the deployment target and supports identity-based pulls. Tagging strategy and retention still need a decision. In this case: Versioned tags tie production to a reviewed build.
- **C:** Incorrect for this question. ACR Tasks builds images in Azure on a commit or schedule without a local Docker host. It removes build-host drift but not image review. Why the correct answer wins: Versioned tags tie production to a reviewed build.
- **D:** Incorrect for this question. A floating tag removes the link between a deployed revision and a specific build, so rollback and audit become guesswork. Why the correct answer wins: Versioned tags tie production to a reviewed build.

### Question 2 — D

Answer: Run image builds on demand or on a trigger with ACR Tasks. An ACR Task builds on a schedule inside Azure. ACR Tasks builds images in Azure on a commit or schedule without a local Docker host. It removes build-host drift but not image review. Local study-map skill 1.2 (Automated Image Builds with ACR Tasks), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure container hosting documentation: https://learn.microsoft.com/en-us/azure/container-apps/

- **A:** Incorrect for this question. ACR keeps tagged, versioned images next to the deployment target and supports identity-based pulls. Tagging strategy and retention still need a decision. Why the correct answer wins: An ACR Task builds on a schedule inside Azure.
- **B:** Incorrect for this question. A slot swap warms the new version before it takes production traffic and makes rollback a second swap. Slot-local settings must be marked sticky. Why the correct answer wins: An ACR Task builds on a schedule inside Azure.
- **C:** Incorrect for this question. Geo-replication reduces cross-region pull latency and gives a local copy during a regional failure. It adds cost and replication management. Why the correct answer wins: An ACR Task builds on a schedule inside Azure.
- **D:** Correct. ACR Tasks builds images in Azure on a commit or schedule without a local Docker host. It removes build-host drift but not image review. In this case: An ACR Task builds on a schedule inside Azure.

### Question 3 — D

Answer: Deploy the image to Azure App Service as a web app. App Service runs containers with managed maintenance and slots. App Service runs a container with managed patching, deployment slots, and built-in authentication options. It is not a Kubernetes control plane. Local study-map skill 1.3 (Container Deployment to Azure App Service), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure container hosting documentation: https://learn.microsoft.com/en-us/azure/container-apps/

- **A:** Incorrect for this question. Container Instances starts a single container group quickly for short tasks. It has no orchestrator-level scaling or revision model. Why the correct answer wins: App Service runs containers with managed maintenance and slots.
- **B:** Incorrect for this question. Container Apps provides a managed environment, revisions, and KEDA-based scaling without cluster administration. Platform limits differ from AKS. Why the correct answer wins: App Service runs containers with managed maintenance and slots.
- **C:** Incorrect for this question. AKS gives full Kubernetes control, including custom controllers and networking. You own node pools, upgrades, and manifest hygiene. Why the correct answer wins: App Service runs containers with managed maintenance and slots.
- **D:** Correct. App Service runs a container with managed patching, deployment slots, and built-in authentication options. It is not a Kubernetes control plane. In this case: App Service runs containers with managed maintenance and slots.

### Question 4 — A

Answer: Reference a Key Vault secret from the app configuration instead of storing it. A Key Vault reference resolves through the app identity at runtime. A Key Vault reference resolves at runtime so the secret is never written into application settings. The app identity still needs permission to read it. Local study-map skill 1.3 (Container Deployment to Azure App Service), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure container hosting documentation: https://learn.microsoft.com/en-us/azure/container-apps/

- **A:** Correct. A Key Vault reference resolves at runtime so the secret is never written into application settings. The app identity still needs permission to read it. In this case: A Key Vault reference resolves through the app identity at runtime.
- **B:** Incorrect for this question. Application settings become environment variables for the container and can be swapped per slot. Sensitive values should still reference a vault. Why the correct answer wins: A Key Vault reference resolves through the app identity at runtime.
- **C:** Incorrect for this question. A slot swap warms the new version before it takes production traffic and makes rollback a second swap. Slot-local settings must be marked sticky. Why the correct answer wins: A Key Vault reference resolves through the app identity at runtime.
- **D:** Incorrect for this question. App Service runs a container with managed patching, deployment slots, and built-in authentication options. It is not a Kubernetes control plane. Why the correct answer wins: A Key Vault reference resolves through the app identity at runtime.

### Question 5 — B

Answer: Create a new Container Apps revision and shift traffic between revisions. Revisions allow percentage traffic splitting for a canary. Revision-based traffic splitting enables canary and blue-green releases. Revision mode and scale rules must be set deliberately. Local study-map skill 1.4 (Container Apps Deployment and Revisions), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure container hosting documentation: https://learn.microsoft.com/en-us/azure/container-apps/

- **A:** Incorrect for this question. A slot swap warms the new version before it takes production traffic and makes rollback a second swap. Slot-local settings must be marked sticky. Why the correct answer wins: Revisions allow percentage traffic splitting for a canary.
- **B:** Correct. Revision-based traffic splitting enables canary and blue-green releases. Revision mode and scale rules must be set deliberately. In this case: Revisions allow percentage traffic splitting for a canary.
- **C:** Incorrect for this question. KEDA scalers drive replica count from queue length, lag, or other event metrics, including scale to zero. Cool-down and max replicas bound the behavior. Why the correct answer wins: Revisions allow percentage traffic splitting for a canary.
- **D:** Incorrect for this question. Internal ingress keeps the endpoint inside the environment virtual network. It is an exposure control, not an authorization control. Why the correct answer wins: Revisions allow percentage traffic splitting for a canary.

### Question 6 — A

Answer: Tune the scale rule cool-down period and maximum replicas. A cool-down period and a sensible maximum prevent rapid flapping. Cool-down prevents replica flapping, and a maximum replica cap bounds cost and downstream load. Both are per-rule settings. Local study-map skill 1.5 (Event-Driven Scaling with KEDA), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure container hosting documentation: https://learn.microsoft.com/en-us/azure/container-apps/

- **A:** Correct. Cool-down prevents replica flapping, and a maximum replica cap bounds cost and downstream load. Both are per-rule settings. In this case: A cool-down period and a sensible maximum prevent rapid flapping.
- **B:** Incorrect for this question. A warm minimum replica removes scale-to-zero cold starts for latency-critical endpoints. It keeps paying for idle capacity. Why the correct answer wins: A cool-down period and a sensible maximum prevent rapid flapping.
- **C:** Incorrect for this question. KEDA scalers drive replica count from queue length, lag, or other event metrics, including scale to zero. Cool-down and max replicas bound the behavior. Why the correct answer wins: A cool-down period and a sensible maximum prevent rapid flapping.
- **D:** Incorrect for this question. HPA adjusts replicas from resource metrics but needs metrics-server and enough node capacity. It cannot scale to zero. Why the correct answer wins: A cool-down period and a sensible maximum prevent rapid flapping.

### Question 7 — A

Answer: Apply a declarative Kubernetes manifest to the cluster. A manifest declares desired state and can be reapplied idempotently. A manifest declares the desired deployment, service, and probe configuration in version control. Applying it repeatedly is idempotent. Local study-map skill 1.6 (AKS Deployment with Manifests), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure container hosting documentation: https://learn.microsoft.com/en-us/azure/container-apps/

- **A:** Correct. A manifest declares the desired deployment, service, and probe configuration in version control. Applying it repeatedly is idempotent. In this case: A manifest declares desired state and can be reapplied idempotently.
- **B:** Incorrect for this question. Container Instances starts a single container group quickly for short tasks. It has no orchestrator-level scaling or revision model. Why the correct answer wins: A manifest declares desired state and can be reapplied idempotently.
- **C:** Incorrect for this question. Readiness gates traffic until the app can serve it, and liveness restarts a wedged container. Wrong thresholds cause restart loops. Why the correct answer wins: A manifest declares desired state and can be reapplied idempotently.
- **D:** Incorrect for this question. HPA adjusts replicas from resource metrics but needs metrics-server and enough node capacity. It cannot scale to zero. Why the correct answer wins: A manifest declares desired state and can be reapplied idempotently.

### Question 8 — C

Answer: Query container logs and Kubernetes events in Log Analytics. Log Analytics ingests both container logs and platform events. Container Apps and AKS surface stdout logs and platform events into a workspace for KQL analysis. Verbosity and retention cost money. Local study-map skill 1.7 (Container Logs, Events, and Connectivity), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure container hosting documentation: https://learn.microsoft.com/en-us/azure/container-apps/

- **A:** Incorrect for this question. Platform logs and metrics must be routed before they can be queried or alerted on. Retention and cost follow the workspace settings. Why the correct answer wins: Log Analytics ingests both container logs and platform events.
- **B:** Incorrect for this question. Reaching a dependency from the pod or replica proves DNS, egress, and firewall paths together. Host-side tests can succeed while the container path fails. Why the correct answer wins: Log Analytics ingests both container logs and platform events.
- **C:** Correct. Container Apps and AKS surface stdout logs and platform events into a workspace for KQL analysis. Verbosity and retention cost money. In this case: Log Analytics ingests both container logs and platform events.
- **D:** Incorrect for this question. Application Insights correlates requests, dependencies, and exceptions into end-to-end transactions. Sampling can hide rare failures. Why the correct answer wins: Log Analytics ingests both container logs and platform events.

### Question 9 — A, B

Answers: Create a new Container Apps revision and shift traffic between revisions; Set a minimum replica count above zero for the container app. Revisions enable traffic splitting, and a minimum replica count avoids cold starts. Revision-based traffic splitting enables canary and blue-green releases. Revision mode and scale rules must be set deliberately. A warm minimum replica removes scale-to-zero cold starts for latency-critical endpoints. It keeps paying for idle capacity. Local study-map skill 1.4 (Container Apps Deployment and Revisions), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure container hosting documentation: https://learn.microsoft.com/en-us/azure/container-apps/

- **A:** Correct. A warm minimum replica removes scale-to-zero cold starts for latency-critical endpoints. It keeps paying for idle capacity. In this case: Revisions enable traffic splitting, and a minimum replica count avoids cold starts.
- **B:** Correct. Revision-based traffic splitting enables canary and blue-green releases. Revision mode and scale rules must be set deliberately. In this case: Revisions enable traffic splitting, and a minimum replica count avoids cold starts.
- **C:** Incorrect for this question. Internal ingress keeps the endpoint inside the environment virtual network. It is an exposure control, not an authorization control. Why the correct answer wins: Revisions enable traffic splitting, and a minimum replica count avoids cold starts.
- **D:** Incorrect for this question. Cool-down prevents replica flapping, and a maximum replica cap bounds cost and downstream load. Both are per-rule settings. Why the correct answer wins: Revisions enable traffic splitting, and a minimum replica count avoids cold starts.
- **E:** Incorrect for this question. HPA adjusts replicas from resource metrics but needs metrics-server and enough node capacity. It cannot scale to zero. Why the correct answer wins: Revisions enable traffic splitting, and a minimum replica count avoids cold starts.

### Question 10 — B, D

Answers: Scale the container app on an event source with a KEDA scaler; Scale on the Service Bus queue length with a KEDA Azure Service Bus scaler. A KEDA scaler drives replica count from the event source, and the queue-length scaler is the suitable trigger. KEDA scalers drive replica count from queue length, lag, or other event metrics, including scale to zero. Cool-down and max replicas bound the behavior. A queue-length scaler adds replicas while work is backed up and removes them when the queue drains. Message lock duration must exceed processing time. Local study-map skill 1.5 (Event-Driven Scaling with KEDA), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure container hosting documentation: https://learn.microsoft.com/en-us/azure/container-apps/

- **A:** Incorrect for this question. HPA adjusts replicas from resource metrics but needs metrics-server and enough node capacity. It cannot scale to zero. Why the correct answer wins: A KEDA scaler drives replica count from the event source, and the queue-length scaler is the suitable trigger.
- **B:** Correct. KEDA scalers drive replica count from queue length, lag, or other event metrics, including scale to zero. Cool-down and max replicas bound the behavior. In this case: A KEDA scaler drives replica count from the event source, and the queue-length scaler is the suitable trigger.
- **C:** Incorrect for this question. CPU-based scaling reacts after work is already queued and cannot scale to zero on an empty queue. It suits steady request-driven services. Why the correct answer wins: A KEDA scaler drives replica count from the event source, and the queue-length scaler is the suitable trigger.
- **D:** Correct. A queue-length scaler adds replicas while work is backed up and removes them when the queue drains. Message lock duration must exceed processing time. In this case: A KEDA scaler drives replica count from the event source, and the queue-length scaler is the suitable trigger.
- **E:** Incorrect for this question. Container Instances starts a single container group quickly for short tasks. It has no orchestrator-level scaling or revision model. Why the correct answer wins: A KEDA scaler drives replica count from the event source, and the queue-length scaler is the suitable trigger.

### Question 11 — C

Answer: Build and push the image → deploy a new revision → shift a small traffic percentage → check metrics → promote or roll back. The image is built, then the revision is deployed, then partial traffic is shifted, and metrics decide promotion. A canary revision accepts a small share of traffic so metrics decide promotion rather than optimism. Local study-map skill 1.4 (Container Apps Deployment and Revisions), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure container hosting documentation: https://learn.microsoft.com/en-us/azure/container-apps/

- **A:** Incorrect for this question. Building after traffic is shifted means the running revision has no reviewed artifact behind it. Why the correct answer wins: The image is built, then the revision is deployed, then partial traffic is shifted, and metrics decide promotion.
- **B:** Incorrect for this question. Full traffic cannot move to a revision that does not exist yet, and the image must exist before the revision. Why the correct answer wins: The image is built, then the revision is deployed, then partial traffic is shifted, and metrics decide promotion.
- **C:** Correct. A canary revision accepts a small share of traffic so metrics decide promotion rather than optimism. In this case: The image is built, then the revision is deployed, then partial traffic is shifted, and metrics decide promotion.
- **D:** Incorrect for this question. Metrics cannot be checked before the revision serves traffic. Why the correct answer wins: The image is built, then the revision is deployed, then partial traffic is shifted, and metrics decide promotion.

### Question 12 — D

Answer: Include the partition key in the query predicate. Including the partition key keeps the read single-partition. A point or single-partition query avoids fan-out across partitions. Cross-partition queries consume more RUs and add latency. Local study-map skill 2.1 (Cosmos DB SDK Access and Queries), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Cosmos DB and PostgreSQL vector documentation: https://learn.microsoft.com/en-us/azure/cosmos-db/

- **A:** Incorrect for this question. SDK queries keep the client on the supported data plane and parameterization avoids injection and plan churn. Cross-partition queries still cost more. Why the correct answer wins: Including the partition key keeps the read single-partition.
- **B:** Incorrect for this question. Request units measure the work a query performs, so tuning the query is often cheaper than adding throughput. Monitor normalized RU consumption. Why the correct answer wins: Including the partition key keeps the read single-partition.
- **C:** Incorrect for this question. Selective indexing cuts write RU charge and storage for unused paths. Excluded paths cannot be filtered efficiently later. Why the correct answer wins: Including the partition key keeps the read single-partition.
- **D:** Correct. A point or single-partition query avoids fan-out across partitions. Cross-partition queries consume more RUs and add latency. In this case: Including the partition key keeps the read single-partition.

### Question 13 — B

Answer: Query through the Cosmos DB SDK with parameterized queries. SDK query calls keep the client supported and let connections be reused. SDK queries keep the client on the supported data plane and parameterization avoids injection and plan churn. Cross-partition queries still cost more. Local study-map skill 2.1 (Cosmos DB SDK Access and Queries), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Cosmos DB and PostgreSQL vector documentation: https://learn.microsoft.com/en-us/azure/cosmos-db/

- **A:** Incorrect for this question. Autoscale follows demand between a minimum and maximum, avoiding throttling at peak without paying for peak all day. The maximum still caps the bill. Why the correct answer wins: SDK query calls keep the client supported and let connections be reused.
- **B:** Correct. SDK queries keep the client on the supported data plane and parameterization avoids injection and plan churn. Cross-partition queries still cost more. In this case: SDK query calls keep the client supported and let connections be reused.
- **C:** Incorrect for this question. Leases track partition ownership so multiple processor instances share work and resume from a continuation token. Lease writes consume RUs too. Why the correct answer wins: SDK query calls keep the client supported and let connections be reused.
- **D:** Incorrect for this question. A transactional batch applies all-or-nothing within a single partition key. It cannot span partitions and still consumes RU per operation. Why the correct answer wins: SDK query calls keep the client supported and let connections be reused.

### Question 14 — D

Answer: Restrict the indexing policy to the paths the queries use. Restricting indexed paths reduces write cost and storage. Selective indexing cuts write RU charge and storage for unused paths. Excluded paths cannot be filtered efficiently later. Local study-map skill 2.2 (Cosmos DB Indexing Policies and Request Units), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Cosmos DB and PostgreSQL vector documentation: https://learn.microsoft.com/en-us/azure/cosmos-db/

- **A:** Incorrect for this question. Item TTL expires documents automatically, which controls storage growth and data retention. It does not archive the expired content. Why the correct answer wins: Restricting indexed paths reduces write cost and storage.
- **B:** Incorrect for this question. Request units measure the work a query performs, so tuning the query is often cheaper than adding throughput. Monitor normalized RU consumption. Why the correct answer wins: Restricting indexed paths reduces write cost and storage.
- **C:** Incorrect for this question. Indexing everything is simple and makes ad hoc queries possible, at higher write cost and storage. It is a default, not an optimization. Why the correct answer wins: Restricting indexed paths reduces write cost and storage.
- **D:** Correct. Selective indexing cuts write RU charge and storage for unused paths. Excluded paths cannot be filtered efficiently later. In this case: Restricting indexed paths reduces write cost and storage.

### Question 15 — C

Answer: Use eventual consistency to minimize read cost. Eventual consistency is the cheapest and most available option for tolerant reads. Eventual consistency is the cheapest and most available option but returns possibly stale data. It fits non-critical counters, not balances. Local study-map skill 2.3 (Cosmos DB Consistency Levels), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Cosmos DB and PostgreSQL vector documentation: https://learn.microsoft.com/en-us/azure/cosmos-db/

- **A:** Incorrect for this question. Strong consistency guarantees the latest committed write globally at the cost of higher latency and reduced availability during partitions. Why the correct answer wins: Eventual consistency is the cheapest and most available option for tolerant reads.
- **B:** Incorrect for this question. Consistency trades freshness against latency, availability, and RU cost. The level is set at the account and can be relaxed per request. Why the correct answer wins: Eventual consistency is the cheapest and most available option for tolerant reads.
- **C:** Correct. Eventual consistency is the cheapest and most available option but returns possibly stale data. It fits non-critical counters, not balances. In this case: Eventual consistency is the cheapest and most available option for tolerant reads.
- **D:** Incorrect for this question. Session consistency guarantees monotonic reads for one session and is the common default for user-facing apps. It does not promise global freshness. Why the correct answer wins: Eventual consistency is the cheapest and most available option for tolerant reads.

### Question 16 — B

Answer: Run a change feed processor to react to new and updated items. The change feed streams new items to downstream processing. The change feed delivers an ordered stream of changes per partition for downstream processing. It is not a delete feed, so deletions need a workaround. Local study-map skill 2.5 (Cosmos DB Change Feed Processing), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Cosmos DB and PostgreSQL vector documentation: https://learn.microsoft.com/en-us/azure/cosmos-db/

- **A:** Incorrect for this question. Leases track partition ownership so multiple processor instances share work and resume from a continuation token. Lease writes consume RUs too. Why the correct answer wins: The change feed streams new items to downstream processing.
- **B:** Correct. The change feed delivers an ordered stream of changes per partition for downstream processing. It is not a delete feed, so deletions need a workaround. In this case: The change feed streams new items to downstream processing.
- **C:** Incorrect for this question. A duplicate-detection window drops repeated sends within the window, which helps with at-least-once producers. The window is time-bounded. Why the correct answer wins: The change feed streams new items to downstream processing.
- **D:** Incorrect for this question. A transactional batch applies all-or-nothing within a single partition key. It cannot span partitions and still consumes RU per operation. Why the correct answer wins: The change feed streams new items to downstream processing.

### Question 17 — A

Answer: Store embeddings in PostgreSQL by using the pgvector extension. pgvector keeps vectors beside relational filter columns. pgvector keeps vectors beside relational data, so filters and joins run in one query. Index type and parameter tuning decide latency. Local study-map skill 2.6 (PostgreSQL Connection and Schema Modeling), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Cosmos DB and PostgreSQL vector documentation: https://learn.microsoft.com/en-us/azure/cosmos-db/

- **A:** Correct. pgvector keeps vectors beside relational data, so filters and joins run in one query. Index type and parameter tuning decide latency. In this case: pgvector keeps vectors beside relational filter columns.
- **B:** Incorrect for this question. A cache absorbs repeated reads and cuts latency for hot data. Cache keys, TTLs, and invalidation must match the freshness requirement. Why the correct answer wins: pgvector keeps vectors beside relational filter columns.
- **C:** Incorrect for this question. Application-side scoring works for tiny collections and tests, but it moves all data over the wire and does not scale with corpus size. Why the correct answer wins: pgvector keeps vectors beside relational filter columns.
- **D:** Incorrect for this question. Cosmos DB gives globally distributed, low-latency document access with tunable consistency. Partition key and RU planning determine the cost profile. Why the correct answer wins: pgvector keeps vectors beside relational filter columns.

### Question 18 — B

Answer: Create an IVFFlat index to save memory on a large table. IVFFlat uses clustering lists and less memory than HNSW. IVFFlat uses clustering lists and needs periodic rebuilds as data grows, but costs less memory than HNSW. Probes trade recall for speed. Local study-map skill 2.7 (pgvector Indexing and Query Latency), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Cosmos DB and PostgreSQL vector documentation: https://learn.microsoft.com/en-us/azure/cosmos-db/

- **A:** Incorrect for this question. An exact scan is accurate but scales linearly and burns compute. It is a baseline for measuring recall, not a production strategy. Why the correct answer wins: IVFFlat uses clustering lists and less memory than HNSW.
- **B:** Correct. IVFFlat uses clustering lists and needs periodic rebuilds as data grows, but costs less memory than HNSW. Probes trade recall for speed. In this case: IVFFlat uses clustering lists and less memory than HNSW.
- **C:** Incorrect for this question. Index creation and bulk loads are I/O heavy, and throttled storage stretches maintenance windows. Storage limits are separate from compute. Why the correct answer wins: IVFFlat uses clustering lists and less memory than HNSW.
- **D:** Incorrect for this question. HNSW gives fast approximate nearest-neighbour queries with a larger memory footprint and slower builds. Recall is tunable at query time. Why the correct answer wins: IVFFlat uses clustering lists and less memory than HNSW.

### Question 19 — C

Answer: Increase storage throughput for index builds and bulk loads. Index builds depend on storage throughput as well as compute. Index creation and bulk loads are I/O heavy, and throttled storage stretches maintenance windows. Storage limits are separate from compute. Local study-map skill 2.8 (PostgreSQL Compute, Memory, and Storage Sizing), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Cosmos DB and PostgreSQL vector documentation: https://learn.microsoft.com/en-us/azure/cosmos-db/

- **A:** Incorrect for this question. A bounded pool amortizes connection setup and protects the server from connection storms. Pool size must match server limits. Why the correct answer wins: Index builds depend on storage throughput as well as compute.
- **B:** Incorrect for this question. Index builds and large sorts spill to disk when work memory is too small, stretching maintenance windows and slowing queries. Why the correct answer wins: Index builds depend on storage throughput as well as compute.
- **C:** Correct. Index creation and bulk loads are I/O heavy, and throttled storage stretches maintenance windows. Storage limits are separate from compute. In this case: Index builds depend on storage throughput as well as compute.
- **D:** Incorrect for this question. Vector indexes are memory-hungry, so undersized compute causes swapping and slow queries. Right-size before tuning index parameters. Why the correct answer wins: Index builds depend on storage throughput as well as compute.

### Question 20 — A

Answer: Place a connection pooler in front of PostgreSQL for many short-lived clients. An external pooler multiplexes many clients onto fewer server connections. An external pooler multiplexes server connections for serverless or highly concurrent clients. Session-level features may be unavailable in transaction mode. Local study-map skill 2.10 (PostgreSQL Connection Optimization), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Cosmos DB and PostgreSQL vector documentation: https://learn.microsoft.com/en-us/azure/cosmos-db/

- **A:** Correct. An external pooler multiplexes server connections for serverless or highly concurrent clients. Session-level features may be unavailable in transaction mode. In this case: An external pooler multiplexes many clients onto fewer server connections.
- **B:** Incorrect for this question. A bounded pool amortizes connection setup and protects the server from connection storms. Pool size must match server limits. Why the correct answer wins: An external pooler multiplexes many clients onto fewer server connections.
- **C:** Incorrect for this question. A replica offloads read traffic but introduces replication lag, which is dangerous for freshly written evidence. It does not reduce index memory pressure. Why the correct answer wins: An external pooler multiplexes many clients onto fewer server connections.
- **D:** Incorrect for this question. Prepared statements avoid repeated planning and reduce chatty network calls. They pair well with pooling but can interact with pool modes. Why the correct answer wins: An external pooler multiplexes many clients onto fewer server connections.

### Question 21 — D

Answer: Invalidate or overwrite the cache entry when the source changes. Explicit invalidation on write removes the stale entry at once. Write-through or explicit invalidation keeps cached answers consistent with the system of record. Without it, TTL is the only bound on staleness. Local study-map skill 2.11 (Azure Managed Redis Caching and Invalidation), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Cosmos DB and PostgreSQL vector documentation: https://learn.microsoft.com/en-us/azure/cosmos-db/

- **A:** Incorrect for this question. Flushing removes all cached content at once, causing a stampede to the origin and a latency cliff. Targeted invalidation is safer. Why the correct answer wins: Explicit invalidation on write removes the stale entry at once.
- **B:** Incorrect for this question. Eviction protects memory but evicts unpredictably, so a hot key can vanish before its freshness bound is reached. It is not a substitute for TTL design. Why the correct answer wins: Explicit invalidation on write removes the stale entry at once.
- **C:** Incorrect for this question. A TTL bounds staleness and reclaims memory without a manual sweep. Too long a TTL hides source changes; too short wastes the cache. Why the correct answer wins: Explicit invalidation on write removes the stale entry at once.
- **D:** Correct. Write-through or explicit invalidation keeps cached answers consistent with the system of record. Without it, TTL is the only bound on staleness. In this case: Explicit invalidation on write removes the stale entry at once.

### Question 22 — C

Answer: Store user session state in Managed Redis with an expiry. Session state in Managed Redis survives instance changes and supports expiry. Session storage in Redis survives instance restarts and supports distributed instances. Sessions must be scoped and expiring. Local study-map skill 2.12 (Azure Managed Redis Vector Indexing), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Cosmos DB and PostgreSQL vector documentation: https://learn.microsoft.com/en-us/azure/cosmos-db/

- **A:** Incorrect for this question. Redis vector search serves low-latency similarity queries from memory. The corpus must fit the memory budget and be rebuilt on model change. Why the correct answer wins: Session state in Managed Redis survives instance changes and supports expiry.
- **B:** Incorrect for this question. A cache absorbs repeated reads and cuts latency for hot data. Cache keys, TTLs, and invalidation must match the freshness requirement. Why the correct answer wins: Session state in Managed Redis survives instance changes and supports expiry.
- **C:** Correct. Session storage in Redis survives instance restarts and supports distributed instances. Sessions must be scoped and expiring. In this case: Session state in Managed Redis survives instance changes and supports expiry.
- **D:** Incorrect for this question. A lock can serialize work across instances, but correctness under retries still needs idempotency keys in the data store. Locks expire and can be lost. Why the correct answer wins: Session state in Managed Redis survives instance changes and supports expiry.

### Question 23 — B, D

Answers: Model typed columns for filters and one vector column for the embedding; Filter on metadata columns in the same query as the vector search. Typed filter columns make the predicate efficient, and filtering in the query enforces scope. Explicit types keep filters fast and make the embedding contract clear. Storing vectors as text defeats index use. Combining a WHERE filter with the distance operator keeps retrieval inside the caller's scope and improves relevance. Index the filter columns too. Local study-map skill 2.6 (PostgreSQL Connection and Schema Modeling), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Cosmos DB and PostgreSQL vector documentation: https://learn.microsoft.com/en-us/azure/cosmos-db/

- **A:** Incorrect for this question. Vector indexes are memory-hungry, so undersized compute causes swapping and slow queries. Right-size before tuning index parameters. Why the correct answer wins: Typed filter columns make the predicate efficient, and filtering in the query enforces scope.
- **B:** Correct. Explicit types keep filters fast and make the embedding contract clear. Storing vectors as text defeats index use. In this case: Typed filter columns make the predicate efficient, and filtering in the query enforces scope.
- **C:** Incorrect for this question. An exact scan is accurate but scales linearly and burns compute. It is a baseline for measuring recall, not a production strategy. Why the correct answer wins: Typed filter columns make the predicate efficient, and filtering in the query enforces scope.
- **D:** Correct. Combining a WHERE filter with the distance operator keeps retrieval inside the caller's scope and improves relevance. Index the filter columns too. In this case: Typed filter columns make the predicate efficient, and filtering in the query enforces scope.
- **E:** Incorrect for this question. Post-filtering can return fewer results than requested and can leak existence or counts if the filtering is careless. Push authorization into the query. Why the correct answer wins: Typed filter columns make the predicate efficient, and filtering in the query enforces scope.

### Question 24 — B, C

Answers: Cache responses in Azure Managed Redis; Create a vector index in Managed Redis for similarity search. Caching serves repeated lookups, and a Redis vector index serves similarity from memory. A cache absorbs repeated reads and cuts latency for hot data. Cache keys, TTLs, and invalidation must match the freshness requirement. Redis vector search serves low-latency similarity queries from memory. The corpus must fit the memory budget and be rebuilt on model change. Local study-map skill 2.11 (Azure Managed Redis Caching and Invalidation), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Cosmos DB and PostgreSQL vector documentation: https://learn.microsoft.com/en-us/azure/cosmos-db/

- **A:** Incorrect for this question. A lock can serialize work across instances, but correctness under retries still needs idempotency keys in the data store. Locks expire and can be lost. Why the correct answer wins: Caching serves repeated lookups, and a Redis vector index serves similarity from memory.
- **B:** Correct. A cache absorbs repeated reads and cuts latency for hot data. Cache keys, TTLs, and invalidation must match the freshness requirement. In this case: Caching serves repeated lookups, and a Redis vector index serves similarity from memory.
- **C:** Correct. Redis vector search serves low-latency similarity queries from memory. The corpus must fit the memory budget and be rebuilt on model change. In this case: Caching serves repeated lookups, and a Redis vector index serves similarity from memory.
- **D:** Incorrect for this question. Eviction protects memory but evicts unpredictably, so a hot key can vanish before its freshness bound is reached. It is not a substitute for TTL design. Why the correct answer wins: Caching serves repeated lookups, and a Redis vector index serves similarity from memory.
- **E:** Incorrect for this question. A TTL bounds staleness and reclaims memory without a manual sweep. Too long a TTL hides source changes; too short wastes the cache. Why the correct answer wins: Caching serves repeated lookups, and a Redis vector index serves similarity from memory.

### Question 25 — C

Answer: Create the vector extension → create the table with a vector column → build the index → query nearest neighbours with a distance operator. The extension must be installed, the table created, the index built, and only then is the query efficient. The extension and typed column must exist before an index can be built, and the index before the query is efficient. Local study-map skill 2.7 (pgvector Indexing and Query Latency), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Cosmos DB and PostgreSQL vector documentation: https://learn.microsoft.com/en-us/azure/cosmos-db/

- **A:** Incorrect for this question. The extension is required for the vector type, and the query should follow index creation for usable latency. Why the correct answer wins: The extension must be installed, the table created, the index built, and only then is the query efficient.
- **B:** Incorrect for this question. Querying before the schema exists cannot succeed, and the index cannot precede the table. Why the correct answer wins: The extension must be installed, the table created, the index built, and only then is the query efficient.
- **C:** Correct. The extension and typed column must exist before an index can be built, and the index before the query is efficient. In this case: The extension must be installed, the table created, the index built, and only then is the query efficient.
- **D:** Incorrect for this question. An index cannot be built before the extension and the table exist. Why the correct answer wins: The extension must be installed, the table created, the index built, and only then is the query efficient.

### Question 26 — B

Answer: Queue the work on a Service Bus queue and process it with a worker. A queue with peek-lock gives at-least-once processing with recovery. A queue decouples producers from a single consumer group and smooths bursts. Delivery semantics depend on receive mode and completion. Local study-map skill 3.1 (Service Bus Queues and Sessions), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure messaging and Functions documentation: https://learn.microsoft.com/en-us/azure/service-bus-messaging/

- **A:** Incorrect for this question. Queue Storage is simple and cheap for large backlogs with at-least-once delivery. It lacks topics, sessions, and scheduled messages. Why the correct answer wins: A queue with peek-lock gives at-least-once processing with recovery.
- **B:** Correct. A queue decouples producers from a single consumer group and smooths bursts. Delivery semantics depend on receive mode and completion. In this case: A queue with peek-lock gives at-least-once processing with recovery.
- **C:** Incorrect for this question. Event Hubs ingests high-volume ordered streams with partitions and consumer groups. It is a streaming log, not a task queue. Why the correct answer wins: A queue with peek-lock gives at-least-once processing with recovery.
- **D:** Incorrect for this question. Topics fan out one message to independent subscribers, each with its own filter and dead-letter queue. Subscribers process at their own pace. Why the correct answer wins: A queue with peek-lock gives at-least-once processing with recovery.

### Question 27 — B

Answer: Publish to a Service Bus topic with multiple subscriptions. A topic with separate subscriptions fans out the event. Topics fan out one message to independent subscribers, each with its own filter and dead-letter queue. Subscribers process at their own pace. Local study-map skill 3.2 (Service Bus Topics, Subscriptions, and Filters), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure messaging and Functions documentation: https://learn.microsoft.com/en-us/azure/service-bus-messaging/

- **A:** Incorrect for this question. Queue Storage is simple and cheap for large backlogs with at-least-once delivery. It lacks topics, sessions, and scheduled messages. Why the correct answer wins: A topic with separate subscriptions fans out the event.
- **B:** Correct. Topics fan out one message to independent subscribers, each with its own filter and dead-letter queue. Subscribers process at their own pace. In this case: A topic with separate subscriptions fans out the event.
- **C:** Incorrect for this question. A custom schema fits domain events that are not resource lifecycle notifications. Consumers must version the schema contract. Why the correct answer wins: A topic with separate subscriptions fans out the event.
- **D:** Incorrect for this question. A queue decouples producers from a single consumer group and smooths bursts. Delivery semantics depend on receive mode and completion. Why the correct answer wins: A topic with separate subscriptions fans out the event.

### Question 28 — A

Answer: Make the handler idempotent by using a message or business key. An idempotency key in the case store makes a replay a no-op. At-least-once delivery means duplicates will happen, so the write must tolerate replay. A stored key makes the retry safe. Local study-map skill 3.3 (Service Bus Dead-Lettering and Retries), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure messaging and Functions documentation: https://learn.microsoft.com/en-us/azure/service-bus-messaging/

- **A:** Correct. At-least-once delivery means duplicates will happen, so the write must tolerate replay. A stored key makes the retry safe. In this case: An idempotency key in the case store makes a replay a no-op.
- **B:** Incorrect for this question. Dead-lettering preserves poison messages for diagnosis instead of losing them. Resubmission needs a fix and an idempotent handler. Why the correct answer wins: An idempotency key in the case store makes a replay a no-op.
- **C:** Incorrect for this question. A delivery cap stops infinite retries of a failing message and moves it to the dead-letter queue. The cap must exceed legitimate transient retries. Why the correct answer wins: An idempotency key in the case store makes a replay a no-op.
- **D:** Incorrect for this question. A duplicate-detection window drops repeated sends within the window, which helps with at-least-once producers. The window is time-bounded. Why the correct answer wins: An idempotency key in the case store makes a replay a no-op.

### Question 29 — D

Answer: Rely on Event Grid retries with a dead-letter destination. Event Grid retries and can dead-letter events that never succeed. Event Grid retries failed deliveries with backoff and can store undeliverable events. Handlers must still be idempotent. Local study-map skill 3.4 (Event Grid Filters, Custom Events, and Retries), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure messaging and Functions documentation: https://learn.microsoft.com/en-us/azure/service-bus-messaging/

- **A:** Incorrect for this question. Identity-based delivery removes a shared key from the subscription. The receiver still validates the caller and payload. Why the correct answer wins: Event Grid retries and can dead-letter events that never succeed.
- **B:** Incorrect for this question. A custom schema fits domain events that are not resource lifecycle notifications. Consumers must version the schema contract. Why the correct answer wins: Event Grid retries and can dead-letter events that never succeed.
- **C:** Incorrect for this question. Subject and event-type filters keep handlers focused and reduce cost. Filters are evaluated on event metadata, not payload body. Why the correct answer wins: Event Grid retries and can dead-letter events that never succeed.
- **D:** Correct. Event Grid retries failed deliveries with backoff and can store undeliverable events. Handlers must still be idempotent. In this case: Event Grid retries and can dead-letter events that never succeed.

### Question 30 — C

Answer: Bind a queue or event trigger to the function. A queue trigger starts the function and manages receives. A trigger starts the function when work arrives and handles the receive loop for you. Poison-message behavior is configured in host settings. Local study-map skill 3.5 (Azure Functions Triggers and Bindings), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure messaging and Functions documentation: https://learn.microsoft.com/en-us/azure/service-bus-messaging/

- **A:** Incorrect for this question. Durable Functions provides orchestrations, activities, timers, and retries with checkpointed state. Orchestrator code must stay deterministic. Why the correct answer wins: A queue trigger starts the function and manages receives.
- **B:** Incorrect for this question. Bindings reduce boilerplate for common inputs and outputs and are configured declaratively. Complex operations still need the SDK. Why the correct answer wins: A queue trigger starts the function and manages receives.
- **C:** Correct. A trigger starts the function when work arrives and handles the receive loop for you. Poison-message behavior is configured in host settings. In this case: A queue trigger starts the function and manages receives.
- **D:** Incorrect for this question. An HTTP trigger gives a synchronous API endpoint with route and authorization configuration. Long-running work should hand off to a queue. Why the correct answer wins: A queue trigger starts the function and manages receives.

### Question 31 — B

Answer: Host the function app on the consumption plan. Consumption bills per execution and scales to demand. Consumption bills per execution and scales automatically, with cold starts and a timeout ceiling. It fits spiky, short work. Local study-map skill 3.6 (Function App Configuration and Deployment), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure messaging and Functions documentation: https://learn.microsoft.com/en-us/azure/service-bus-messaging/

- **A:** Incorrect for this question. A premium plan reduces cold starts and supports virtual network integration and longer timeouts. It costs more than consumption. Why the correct answer wins: Consumption bills per execution and scales to demand.
- **B:** Correct. Consumption bills per execution and scales automatically, with cold starts and a timeout ceiling. It fits spiky, short work. In this case: Consumption bills per execution and scales to demand.
- **C:** Incorrect for this question. A staging slot lets a new build warm up and be validated before the swap. Slot settings that must not move are marked sticky. Why the correct answer wins: Consumption bills per execution and scales to demand.
- **D:** Incorrect for this question. Durable Functions provides orchestrations, activities, timers, and retries with checkpointed state. Orchestrator code must stay deterministic. Why the correct answer wins: Consumption bills per execution and scales to demand.

### Question 32 — C

Answer: Deploy the function app through a CI pipeline with app settings applied. Pipeline deployment with Key Vault references keeps code and configuration versioned without embedding secrets. Pipeline deployment keeps code and configuration versioned together and repeatable. Secrets belong in a vault reference, not in the pipeline file. Local study-map skill 3.6 (Function App Configuration and Deployment), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure messaging and Functions documentation: https://learn.microsoft.com/en-us/azure/service-bus-messaging/

- **A:** Incorrect for this question. A premium plan reduces cold starts and supports virtual network integration and longer timeouts. It costs more than consumption. Why the correct answer wins: Pipeline deployment with Key Vault references keeps code and configuration versioned without embedding secrets.
- **B:** Incorrect for this question. Durable Functions provides orchestrations, activities, timers, and retries with checkpointed state. Orchestrator code must stay deterministic. Why the correct answer wins: Pipeline deployment with Key Vault references keeps code and configuration versioned without embedding secrets.
- **C:** Correct. Pipeline deployment keeps code and configuration versioned together and repeatable. Secrets belong in a vault reference, not in the pipeline file. In this case: Pipeline deployment with Key Vault references keeps code and configuration versioned without embedding secrets.
- **D:** Incorrect for this question. A staging slot lets a new build warm up and be validated before the swap. Slot settings that must not move are marked sticky. Why the correct answer wins: Pipeline deployment with Key Vault references keeps code and configuration versioned without embedding secrets.

### Question 33 — C, E

Answers: Inspect the dead-letter queue and resubmit corrected messages; Set a maximum delivery count and handle the dead-letter path. Dead-lettering preserves the message, and a delivery cap bounds retries. Dead-lettering preserves poison messages for diagnosis instead of losing them. Resubmission needs a fix and an idempotent handler. A delivery cap stops infinite retries of a failing message and moves it to the dead-letter queue. The cap must exceed legitimate transient retries. Local study-map skill 3.3 (Service Bus Dead-Lettering and Retries), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure messaging and Functions documentation: https://learn.microsoft.com/en-us/azure/service-bus-messaging/

- **A:** Incorrect for this question. A duplicate-detection window drops repeated sends within the window, which helps with at-least-once producers. The window is time-bounded. Why the correct answer wins: Dead-lettering preserves the message, and a delivery cap bounds retries.
- **B:** Incorrect for this question. Receive-and-delete removes the message on delivery, so a crash loses work silently. It suits telemetry, not payments. Why the correct answer wins: Dead-lettering preserves the message, and a delivery cap bounds retries.
- **C:** Correct. A delivery cap stops infinite retries of a failing message and moves it to the dead-letter queue. The cap must exceed legitimate transient retries. In this case: Dead-lettering preserves the message, and a delivery cap bounds retries.
- **D:** Incorrect for this question. Sessions give ordered, exclusive processing per session ID across competing consumers. They require session-aware senders and receivers. Why the correct answer wins: Dead-lettering preserves the message, and a delivery cap bounds retries.
- **E:** Correct. Dead-lettering preserves poison messages for diagnosis instead of losing them. Resubmission needs a fix and an idempotent handler. In this case: Dead-lettering preserves the message, and a delivery cap bounds retries.

### Question 34 — A, B

Answers: Define a custom event schema for the topic; Filter the Event Grid subscription by subject or event type. A custom event schema carries the payload, and a subscription filter routes it. A custom schema fits domain events that are not resource lifecycle notifications. Consumers must version the schema contract. Subject and event-type filters keep handlers focused and reduce cost. Filters are evaluated on event metadata, not payload body. Local study-map skill 3.4 (Event Grid Filters, Custom Events, and Retries), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure messaging and Functions documentation: https://learn.microsoft.com/en-us/azure/service-bus-messaging/

- **A:** Correct. A custom schema fits domain events that are not resource lifecycle notifications. Consumers must version the schema contract. In this case: A custom event schema carries the payload, and a subscription filter routes it.
- **B:** Correct. Subject and event-type filters keep handlers focused and reduce cost. Filters are evaluated on event metadata, not payload body. In this case: A custom event schema carries the payload, and a subscription filter routes it.
- **C:** Incorrect for this question. Subscription filters route only matching messages to a handler, reducing wasted processing. Filter evaluation happens broker-side on message properties. Why the correct answer wins: A custom event schema carries the payload, and a subscription filter routes it.
- **D:** Incorrect for this question. Identity-based delivery removes a shared key from the subscription. The receiver still validates the caller and payload. Why the correct answer wins: A custom event schema carries the payload, and a subscription filter routes it.
- **E:** Incorrect for this question. Event Grid retries failed deliveries with backoff and can store undeliverable events. Handlers must still be idempotent. Why the correct answer wins: A custom event schema carries the payload, and a subscription filter routes it.

### Question 35 — C

Answer: Publish the message → receive with peek-lock → process the work → complete the message → dead-letter after the delivery limit. The message is received, processed, completed, and dead-lettered only after the delivery limit is exhausted. Peek-lock keeps the message until the handler succeeds, and only repeated failures should dead-letter it. Local study-map skill 3.1 (Service Bus Queues and Sessions), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure messaging and Functions documentation: https://learn.microsoft.com/en-us/azure/service-bus-messaging/

- **A:** Incorrect for this question. Completing a message before processing discards the work and defeats at-least-once delivery. Why the correct answer wins: The message is received, processed, completed, and dead-lettered only after the delivery limit is exhausted.
- **B:** Incorrect for this question. Work cannot be processed before the message is published and received. Why the correct answer wins: The message is received, processed, completed, and dead-lettered only after the delivery limit is exhausted.
- **C:** Correct. Peek-lock keeps the message until the handler succeeds, and only repeated failures should dead-letter it. In this case: The message is received, processed, completed, and dead-lettered only after the delivery limit is exhausted.
- **D:** Incorrect for this question. The message cannot be received before it is published, and completion must follow processing. Why the correct answer wins: The message is received, processed, completed, and dead-lettered only after the delivery limit is exhausted.

### Question 36 — C

Answer: Enable purge protection and soft delete on the vault. Soft delete with purge protection prevents permanent loss. Soft delete and purge protection stop accidental or malicious permanent loss of secrets. They also constrain how names can be reused. Local study-map skill 4.1 (Key Vault Secret Storage, Rotation, and Retrieval), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Key Vault, App Configuration, and Monitor documentation: https://learn.microsoft.com/en-us/azure/azure-monitor/

- **A:** Incorrect for this question. A scoped role grants only the operations the app performs and limits blast radius. Prefer built-in roles over broad contributor grants. Why the correct answer wins: Soft delete with purge protection prevents permanent loss.
- **B:** Incorrect for this question. A vault centralizes secret storage with access control and audit. Retrieval should use an identity, not a copied credential. Why the correct answer wins: Soft delete with purge protection prevents permanent loss.
- **C:** Correct. Soft delete and purge protection stop accidental or malicious permanent loss of secrets. They also constrain how names can be reused. In this case: Soft delete with purge protection prevents permanent loss.
- **D:** Incorrect for this question. Pinning a version makes a rotation invisible to the app until it is redeployed, which is useful for break-glass and dangerous for routine rotation. Why the correct answer wins: Soft delete with purge protection prevents permanent loss.

### Question 37 — A

Answer: Rotate the secret on a schedule and let apps resolve the current version. Rotation plus current-version reads keeps the app working across a change. Rotation limits the value of a leaked secret, but callers must read the latest version rather than caching an old one forever. Local study-map skill 4.1 (Key Vault Secret Storage, Rotation, and Retrieval), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Key Vault, App Configuration, and Monitor documentation: https://learn.microsoft.com/en-us/azure/azure-monitor/

- **A:** Correct. Rotation limits the value of a leaked secret, but callers must read the latest version rather than caching an old one forever. In this case: Rotation plus current-version reads keeps the app working across a change.
- **B:** Incorrect for this question. Application settings become environment variables for the container and can be swapped per slot. Sensitive values should still reference a vault. Why the correct answer wins: Rotation plus current-version reads keeps the app working across a change.
- **C:** Incorrect for this question. Pinning a version makes a rotation invisible to the app until it is redeployed, which is useful for break-glass and dangerous for routine rotation. Why the correct answer wins: Rotation plus current-version reads keeps the app working across a change.
- **D:** Incorrect for this question. Vault access is a separate authorization decision from the app identity. Without a data-plane role or policy the reference fails at runtime. Why the correct answer wins: Rotation plus current-version reads keeps the app working across a change.

### Question 38 — D

Answer: Use App Configuration labels to separate environments. Labels separate environment values under the same keys. Labels keep dev, test, and prod values in one store with one key schema. A misconfigured label selector silently serves the wrong values. Local study-map skill 4.2 (App Configuration Settings and Feature Flags), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Key Vault, App Configuration, and Monitor documentation: https://learn.microsoft.com/en-us/azure/azure-monitor/

- **A:** Incorrect for this question. Pinning a version makes a rotation invisible to the app until it is redeployed, which is useful for break-glass and dangerous for routine rotation. Why the correct answer wins: Labels separate environment values under the same keys.
- **B:** Incorrect for this question. A Key Vault reference keeps non-secret settings in App Configuration while the value stays in the vault. The app identity needs both sets of permissions. Why the correct answer wins: Labels separate environment values under the same keys.
- **C:** Incorrect for this question. Sentinel-key or polling refresh lets a running app pick up new settings. Refresh intervals trade responsiveness against request volume. Why the correct answer wins: Labels separate environment values under the same keys.
- **D:** Correct. Labels keep dev, test, and prod values in one store with one key schema. A misconfigured label selector silently serves the wrong values. In this case: Labels separate environment values under the same keys.

### Question 39 — B

Answer: Export telemetry through an OpenTelemetry collector. An OpenTelemetry collector centralizes export and routing. A collector batches, filters, and routes telemetry, and decouples app configuration from the backend. It is another component to run and monitor. Local study-map skill 4.3 (Distributed Tracing with OpenTelemetry), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Key Vault, App Configuration, and Monitor documentation: https://learn.microsoft.com/en-us/azure/azure-monitor/

- **A:** Incorrect for this question. OpenTelemetry emits vendor-neutral traces, metrics, and logs with context propagation. Exporters and sampling decide what reaches the backend. Why the correct answer wins: An OpenTelemetry collector centralizes export and routing.
- **B:** Correct. A collector batches, filters, and routes telemetry, and decouples app configuration from the backend. It is another component to run and monitor. In this case: An OpenTelemetry collector centralizes export and routing.
- **C:** Incorrect for this question. Sampling keeps telemetry cost bounded, but aggressive sampling can hide rare failures. Tail sampling can retain errors preferentially. Why the correct answer wins: An OpenTelemetry collector centralizes export and routing.
- **D:** Incorrect for this question. Propagation stitches one trace across HTTP, messaging, and Functions so the whole path is visible. Missing propagation breaks the trace at that hop. Why the correct answer wins: An OpenTelemetry collector centralizes export and routing.

### Question 40 — B

Answer: Reach the data service through a private endpoint. A private endpoint with public access disabled restricts the path to the workload network. A private endpoint keeps traffic on the virtual network and removes public exposure. DNS resolution must be wired to the private zone. Local study-map skill 4.5 (Identity-Based Access for Application Services), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Key Vault, App Configuration, and Monitor documentation: https://learn.microsoft.com/en-us/azure/azure-monitor/

- **A:** Incorrect for this question. A managed identity issues tokens from the platform, removing secret distribution from the app. Role assignment still scopes what it can reach. Why the correct answer wins: A private endpoint with public access disabled restricts the path to the workload network.
- **B:** Correct. A private endpoint keeps traffic on the virtual network and removes public exposure. DNS resolution must be wired to the private zone. In this case: A private endpoint with public access disabled restricts the path to the workload network.
- **C:** Incorrect for this question. Platform logs and metrics must be routed before they can be queried or alerted on. Retention and cost follow the workspace settings. Why the correct answer wins: A private endpoint with public access disabled restricts the path to the workload network.
- **D:** Incorrect for this question. A scoped role grants only the operations the app performs and limits blast radius. Prefer built-in roles over broad contributor grants. Why the correct answer wins: A private endpoint with public access disabled restricts the path to the workload network.

### Question 41 — A

Answer: Authenticate with a managed identity instead of a stored key. A managed identity provides tokens from the platform. A managed identity issues tokens from the platform, removing secret distribution from the app. Role assignment still scopes what it can reach. Local study-map skill 4.5 (Identity-Based Access for Application Services), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Key Vault, App Configuration, and Monitor documentation: https://learn.microsoft.com/en-us/azure/azure-monitor/

- **A:** Correct. A managed identity issues tokens from the platform, removing secret distribution from the app. Role assignment still scopes what it can reach. In this case: A managed identity provides tokens from the platform.
- **B:** Incorrect for this question. A vault centralizes secret storage with access control and audit. Retrieval should use an identity, not a copied credential. Why the correct answer wins: A managed identity provides tokens from the platform.
- **C:** Incorrect for this question. A scoped role grants only the operations the app performs and limits blast radius. Prefer built-in roles over broad contributor grants. Why the correct answer wins: A managed identity provides tokens from the platform.
- **D:** Incorrect for this question. Application settings become environment variables for the container and can be swapped per slot. Sensitive values should still reference a vault. Why the correct answer wins: A managed identity provides tokens from the platform.

### Question 42 — B, D

Answers: Instrument the service with the OpenTelemetry SDK; Propagate trace context across every service and queue hop. Instrumentation creates spans, and context propagation keeps the trace connected across hops. OpenTelemetry emits vendor-neutral traces, metrics, and logs with context propagation. Exporters and sampling decide what reaches the backend. Propagation stitches one trace across HTTP, messaging, and Functions so the whole path is visible. Missing propagation breaks the trace at that hop. Local study-map skill 4.3 (Distributed Tracing with OpenTelemetry), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Key Vault, App Configuration, and Monitor documentation: https://learn.microsoft.com/en-us/azure/azure-monitor/

- **A:** Incorrect for this question. KQL filters, projects, and aggregates log and metric tables in Log Analytics. Start narrow with a time range and a request ID. Why the correct answer wins: Instrumentation creates spans, and context propagation keeps the trace connected across hops.
- **B:** Correct. Propagation stitches one trace across HTTP, messaging, and Functions so the whole path is visible. Missing propagation breaks the trace at that hop. In this case: Instrumentation creates spans, and context propagation keeps the trace connected across hops.
- **C:** Incorrect for this question. Sampling keeps telemetry cost bounded, but aggressive sampling can hide rare failures. Tail sampling can retain errors preferentially. Why the correct answer wins: Instrumentation creates spans, and context propagation keeps the trace connected across hops.
- **D:** Correct. OpenTelemetry emits vendor-neutral traces, metrics, and logs with context propagation. Exporters and sampling decide what reaches the backend. In this case: Instrumentation creates spans, and context propagation keeps the trace connected across hops.
- **E:** Incorrect for this question. A collector batches, filters, and routes telemetry, and decouples app configuration from the backend. It is another component to run and monitor. Why the correct answer wins: Instrumentation creates spans, and context propagation keeps the trace connected across hops.

### Question 43 — B, D

Answers: Project only the columns needed and filter by time first; Alert on platform metrics rather than only on log queries. Filtering early and projecting fewer columns reduces scanned data, and platform metric alerts are fast and cheap. Reducing columns and rows early lowers query cost and latency. Broad queries over long ranges are the usual cause of slow KQL. Platform metrics are cheap and near-real-time, so they suit latency and failure-rate alerts. Log-based alerts add latency and query cost. Local study-map skill 4.4 (KQL Queries for Logs and Metrics), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Key Vault, App Configuration, and Monitor documentation: https://learn.microsoft.com/en-us/azure/azure-monitor/

- **A:** Incorrect for this question. An alert turns a threshold breach into a notification or action. Thresholds need a baseline, or the alert is noise. Why the correct answer wins: Filtering early and projecting fewer columns reduces scanned data, and platform metric alerts are fast and cheap.
- **B:** Correct. Reducing columns and rows early lowers query cost and latency. Broad queries over long ranges are the usual cause of slow KQL. In this case: Filtering early and projecting fewer columns reduces scanned data, and platform metric alerts are fast and cheap.
- **C:** Incorrect for this question. Time-binned aggregation reveals the shape of an incident: a step change, a ramp, or a periodic spike. Averages alone hide short outages. Why the correct answer wins: Filtering early and projecting fewer columns reduces scanned data, and platform metric alerts are fast and cheap.
- **D:** Correct. Platform metrics are cheap and near-real-time, so they suit latency and failure-rate alerts. Log-based alerts add latency and query cost. In this case: Filtering early and projecting fewer columns reduces scanned data, and platform metric alerts are fast and cheap.
- **E:** Incorrect for this question. Precomputed results avoid recomputing expensive aggregations on every dashboard refresh. The trade-off is storage and freshness lag. Why the correct answer wins: Filtering early and projecting fewer columns reduces scanned data, and platform metric alerts are fast and cheap.

### Question 44 — B

Answer: Store the secret in Key Vault → grant the app identity access → reference the secret from the app → rotate the secret → the app reads the new version. Store the secret, grant access, reference it from the app, rotate it, and read the current version. Access must be granted before the reference resolves, and the app must read the current version after rotation. Local study-map skill 4.1 (Key Vault Secret Storage, Rotation, and Retrieval), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Key Vault, App Configuration, and Monitor documentation: https://learn.microsoft.com/en-us/azure/azure-monitor/

- **A:** Incorrect for this question. There is nothing to rotate or reference before the secret is stored. Why the correct answer wins: Store the secret, grant access, reference it from the app, rotate it, and read the current version.
- **B:** Correct. Access must be granted before the reference resolves, and the app must read the current version after rotation. In this case: Store the secret, grant access, reference it from the app, rotate it, and read the current version.
- **C:** Incorrect for this question. A reference cannot resolve before the secret and the access grant exist. Why the correct answer wins: Store the secret, grant access, reference it from the app, rotate it, and read the current version.
- **D:** Incorrect for this question. Access can be granted first, but rotation cannot precede storing the secret. Why the correct answer wins: Store the secret, grant access, reference it from the app, rotate it, and read the current version.

### Question 45 — D

Answer: Retrieve nearest neighbours first and discard unauthorized rows in the application. Post-filtering removes rows after selection, so the caller receives fewer results than requested. Post-filtering can return fewer results than requested and can leak existence or counts if the filtering is careless. Push authorization into the query. Local study-map skill 2.9 (PostgreSQL RAG with Metadata Filters), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Cosmos DB and PostgreSQL vector documentation: https://learn.microsoft.com/en-us/azure/cosmos-db/

- **A:** Incorrect for this question. HNSW gives fast approximate nearest-neighbour queries with a larger memory footprint and slower builds. Recall is tunable at query time. Why the correct answer wins: Post-filtering removes rows after selection, so the caller receives fewer results than requested.
- **B:** Incorrect for this question. Combining a WHERE filter with the distance operator keeps retrieval inside the caller's scope and improves relevance. Index the filter columns too. Why the correct answer wins: Post-filtering removes rows after selection, so the caller receives fewer results than requested.
- **C:** Incorrect for this question. An exact scan is accurate but scales linearly and burns compute. It is a baseline for measuring recall, not a production strategy. Why the correct answer wins: Post-filtering removes rows after selection, so the caller receives fewer results than requested.
- **D:** Correct. Post-filtering can return fewer results than requested and can leak existence or counts if the filtering is careless. Push authorization into the query. In this case: Post-filtering removes rows after selection, so the caller receives fewer results than requested.

### Question 46 — A

Answer: Inspect the dead-letter queue and resubmit corrected messages. Dead-lettering removes it from the active queue while preserving it. Dead-lettering preserves poison messages for diagnosis instead of losing them. Resubmission needs a fix and an idempotent handler. Local study-map skill 3.3 (Service Bus Dead-Lettering and Retries), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure messaging and Functions documentation: https://learn.microsoft.com/en-us/azure/service-bus-messaging/

- **A:** Correct. Dead-lettering preserves poison messages for diagnosis instead of losing them. Resubmission needs a fix and an idempotent handler. In this case: Dead-lettering removes it from the active queue while preserving it.
- **B:** Incorrect for this question. Receive-and-delete removes the message on delivery, so a crash loses work silently. It suits telemetry, not payments. Why the correct answer wins: Dead-lettering removes it from the active queue while preserving it.
- **C:** Incorrect for this question. Sessions give ordered, exclusive processing per session ID across competing consumers. They require session-aware senders and receivers. Why the correct answer wins: Dead-lettering removes it from the active queue while preserving it.
- **D:** Incorrect for this question. A delivery cap stops infinite retries of a failing message and moves it to the dead-letter queue. The cap must exceed legitimate transient retries. Why the correct answer wins: Dead-lettering removes it from the active queue while preserving it.

### Question 47 — A

Answer: Reference the Key Vault secret from an App Configuration key value. A Key Vault reference inside the App Configuration key keeps the secret out of the store. A Key Vault reference keeps non-secret settings in App Configuration while the value stays in the vault. The app identity needs both sets of permissions. Local study-map skill 4.2 (App Configuration Settings and Feature Flags), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Key Vault, App Configuration, and Monitor documentation: https://learn.microsoft.com/en-us/azure/azure-monitor/

- **A:** Correct. A Key Vault reference keeps non-secret settings in App Configuration while the value stays in the vault. The app identity needs both sets of permissions. In this case: A Key Vault reference inside the App Configuration key keeps the secret out of the store.
- **B:** Incorrect for this question. Application settings become environment variables for the container and can be swapped per slot. Sensitive values should still reference a vault. Why the correct answer wins: A Key Vault reference inside the App Configuration key keeps the secret out of the store.
- **C:** Incorrect for this question. A vault centralizes secret storage with access control and audit. Retrieval should use an identity, not a copied credential. Why the correct answer wins: A Key Vault reference inside the App Configuration key keeps the secret out of the store.
- **D:** Incorrect for this question. App Configuration separates configuration from code and supports labels, feature flags, and Key Vault references. Change still needs a refresh strategy. Why the correct answer wins: A Key Vault reference inside the App Configuration key keeps the secret out of the store.

### Question 48 — D

Answer: Test end-to-end connectivity from inside the container to each dependency. Name resolution must map to the private endpoint address inside the workload network. Reaching a dependency from the pod or replica proves DNS, egress, and firewall paths together. Host-side tests can succeed while the container path fails. Local study-map skill 1.7 (Container Logs, Events, and Connectivity), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure container hosting documentation: https://learn.microsoft.com/en-us/azure/container-apps/

- **A:** Incorrect for this question. Container Apps and AKS surface stdout logs and platform events into a workspace for KQL analysis. Verbosity and retention cost money. Why the correct answer wins: Name resolution must map to the private endpoint address inside the workload network.
- **B:** Incorrect for this question. A private endpoint needs matching name resolution or clients still resolve the public address. The zone must be linked to the workload network. Why the correct answer wins: Name resolution must map to the private endpoint address inside the workload network.
- **C:** Incorrect for this question. Readiness gates traffic until the app can serve it, and liveness restarts a wedged container. Wrong thresholds cause restart loops. Why the correct answer wins: Name resolution must map to the private endpoint address inside the workload network.
- **D:** Correct. Reaching a dependency from the pod or replica proves DNS, egress, and firewall paths together. Host-side tests can succeed while the container path fails. In this case: Name resolution must map to the private endpoint address inside the workload network.

### Question 49 — A

Answer: Subscribe to a system topic for resource events. A system topic carries resource lifecycle events such as blob creation. System topics carry Azure resource lifecycle events. Domain events that are not resource changes need a custom topic and schema. Local study-map skill 3.4 (Event Grid Filters, Custom Events, and Retries), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure messaging and Functions documentation: https://learn.microsoft.com/en-us/azure/service-bus-messaging/

- **A:** Correct. System topics carry Azure resource lifecycle events. Domain events that are not resource changes need a custom topic and schema. In this case: A system topic carries resource lifecycle events such as blob creation.
- **B:** Incorrect for this question. Subject and event-type filters keep handlers focused and reduce cost. Filters are evaluated on event metadata, not payload body. Why the correct answer wins: A system topic carries resource lifecycle events such as blob creation.
- **C:** Incorrect for this question. Event Grid retries failed deliveries with backoff and can store undeliverable events. Handlers must still be idempotent. Why the correct answer wins: A system topic carries resource lifecycle events such as blob creation.
- **D:** Incorrect for this question. A custom schema fits domain events that are not resource lifecycle notifications. Consumers must version the schema contract. Why the correct answer wins: A system topic carries resource lifecycle events such as blob creation.

### Question 50 — D

Answer: Join the requests and dependencies tables on the operation ID. Joining requests to dependencies on the operation identifier isolates the slow call. Joining request and dependency telemetry shows which downstream call fails inside a slow request. Cross-workspace joins need the right scope. Local study-map skill 4.4 (KQL Queries for Logs and Metrics), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Key Vault, App Configuration, and Monitor documentation: https://learn.microsoft.com/en-us/azure/azure-monitor/

- **A:** Incorrect for this question. An alert turns a threshold breach into a notification or action. Thresholds need a baseline, or the alert is noise. Why the correct answer wins: Joining requests to dependencies on the operation identifier isolates the slow call.
- **B:** Incorrect for this question. Reducing columns and rows early lowers query cost and latency. Broad queries over long ranges are the usual cause of slow KQL. Why the correct answer wins: Joining requests to dependencies on the operation identifier isolates the slow call.
- **C:** Incorrect for this question. Time-binned aggregation reveals the shape of an incident: a step change, a ramp, or a periodic spike. Averages alone hide short outages. Why the correct answer wins: Joining requests to dependencies on the operation identifier isolates the slow call.
- **D:** Correct. Joining request and dependency telemetry shows which downstream call fails inside a slow request. Cross-workspace joins need the right scope. In this case: Joining requests to dependencies on the operation identifier isolates the slow call.
