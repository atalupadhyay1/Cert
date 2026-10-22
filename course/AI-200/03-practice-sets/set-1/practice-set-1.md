# Microsoft AI-200 — Full-Length Mock Exam 1

Azure AI Cloud Developer Associate · 50 questions · 120 minutes · passing target 700/1000

Blueprint-weighted mock exam. Item mix: 38 single-choice, 8 multi-select (selection count stated), 4 ordering items rendered as answer choices, and 2 case studies of 3 questions. Hot-area, drag-and-drop UI, labs, and adaptive problem-solution sets cannot be reproduced in a CSV; see the README for the exact fidelity boundary.

Original educational content, not actual, recalled, or copied Microsoft exam items.

## Questions

### 1. A release must be traceable to one built artifact so operations can roll back to the previous version by tag. Which registry practice should be enforced?

Domain: Develop containerized solutions on Azure

- A. Run image builds on demand or on a trigger with ACR Tasks
- B. Build and store versioned images in Azure Container Registry
- C. Deploy the mutable latest tag and let the platform resolve it
- D. Apply an ACR retention policy to prune old untagged manifests

### 2. Builds currently run on a developer workstation, and images differ between machines. Which change removes the local build host?

Domain: Develop containerized solutions on Azure

- A. Stage the change in a deployment slot and swap after verification
- B. Replicate the registry to each deployment region
- C. Run image builds on demand or on a trigger with ACR Tasks
- D. Build and store versioned images in Azure Container Registry

### 3. The same container must run with different log levels and feature toggles per environment without being rebuilt. What should supply those values?

Domain: Develop containerized solutions on Azure

- A. Stage the change in a deployment slot and swap after verification
- B. Supply configuration through App Service application settings
- C. Reference a Key Vault secret from the app configuration instead of storing it
- D. Deploy the image to Azure App Service as a web app

### 4. An internal pricing API must accept calls only from other workloads inside the environment network. What should be configured?

Domain: Develop containerized solutions on Azure

- A. Deploy the service to Azure Container Apps
- B. Scale the container app on an event source with a KEDA scaler
- C. Configure Container Apps ingress for internal-only access
- D. Create a new Container Apps revision and shift traffic between revisions

### 5. The platform team wants the deployment, service, and probes declared in version control and reapplied safely after any drift. What should be used?

Domain: Develop containerized solutions on Azure

- A. Rely on the horizontal pod autoscaler on CPU
- B. Run image builds on demand or on a trigger with ACR Tasks
- C. Run the batch job in Azure Container Instances
- D. Apply a declarative Kubernetes manifest to the cluster

### 6. Pods report ready, but calls to Cosmos DB time out while the same query succeeds from an administrator workstation. What should be verified next?

Domain: Develop containerized solutions on Azure

- A. Enable diagnostic settings to route platform logs to the workspace
- B. Add readiness and liveness probes to the pod specification
- C. Query container logs and Kubernetes events in Log Analytics
- D. Test end-to-end connectivity from inside the container to each dependency

### 7. You need immutable release artifacts and controlled registry growth. Which two actions should you take? Select two.

Domain: Develop containerized solutions on Azure

- A. Deploy the mutable latest tag and let the platform resolve it
- B. Stage the change in a deployment slot and swap after verification
- C. Replicate the registry to each deployment region
- D. Build and store versioned images in Azure Container Registry
- E. Apply an ACR retention policy to prune old untagged manifests

### 8. A Kubernetes deployment must be reproducible and must not receive traffic before it can serve requests. Which two elements belong in the manifest? Select two.

Domain: Develop containerized solutions on Azure

- A. Run the batch job in Azure Container Instances
- B. Add readiness and liveness probes to the pod specification
- C. Rely on the horizontal pod autoscaler on CPU
- D. Scale only on CPU utilization without an event scaler
- E. Apply a declarative Kubernetes manifest to the cluster

### 9. Which sequence correctly releases a new ranking service as a canary revision?

Domain: Develop containerized solutions on Azure

- A. Check metrics → deploy a new revision → build and push the image → shift a small traffic percentage → promote
- B. Shift all traffic to a new revision → deploy the revision → check metrics → build the image → promote
- C. Deploy a new revision → shift all traffic → build and push the image → check metrics → roll back
- D. Build and push the image → deploy a new revision → shift a small traffic percentage → check metrics → promote or roll back

### 10. A point read by order ID returns late and consumes far more request units than expected. Which change addresses the cause?

Domain: Develop AI solutions by using Azure data management services

- A. Include the partition key in the query predicate
- B. Index every property by using the default automatic policy
- C. Increase provisioned throughput and watch the RU charge per query
- D. Choose a high-cardinality partition key that spreads writes

### 11. Write cost is high on a container that only filters on three properties. What should be changed?

Domain: Develop AI solutions by using Azure data management services

- A. Restrict the indexing policy to the paths the queries use
- B. Index every property by using the default automatic policy
- C. Enable autoscale throughput with a maximum RU limit
- D. Choose the account consistency level that matches the read requirement

### 12. A shopping cart must never show a customer an older version of their own update, and global ordering is not required. Which consistency choice fits?

Domain: Develop AI solutions by using Azure data management services

- A. Choose the account consistency level that matches the read requirement
- B. Use strong consistency for every read in the account
- C. Use session consistency for reads within the same client session
- D. Use eventual consistency to minimize read cost

### 13. Product embeddings and product documents must live in one store so filters and similarity search run together. What should be used?

Domain: Develop AI solutions by using Azure data management services

- A. Store embeddings in PostgreSQL by using the pgvector extension
- B. Store embeddings in a vector property and query with VectorDistance
- C. Scan every document and compute similarity in application code
- D. Use the DiskANN vector index for large collections

### 14. Downstream enrichment must run whenever a product document is inserted or updated, without polling the container. What should be implemented?

Domain: Develop AI solutions by using Azure data management services

- A. Run a change feed processor to react to new and updated items
- B. Use a lease container to coordinate change feed readers
- C. Publish the state change as an Event Grid event
- D. Enable duplicate detection on the queue

### 15. A retrieval table must support category filters and a vector column in one query. How should it be modeled?

Domain: Develop AI solutions by using Azure data management services

- A. Scale compute and memory to fit index size and query concurrency
- B. Model typed columns for filters and one vector column for the embedding
- C. Add a read replica and send all vector queries to it
- D. Increase storage throughput for index builds and bulk loads

### 16. Nearest-neighbour queries over two million chunks must return in milliseconds with acceptable recall. Which index type should be created?

Domain: Develop AI solutions by using Azure data management services

- A. Query without a vector index and let PostgreSQL scan the table
- B. Place a connection pooler in front of PostgreSQL for many short-lived clients
- C. Create an IVFFlat index to save memory on a large table
- D. Create an HNSW index for low-latency approximate search

### 17. Every product page recomputes the identical recommendation block for every visitor. What should be added?

Domain: Develop AI solutions by using Azure data management services

- A. Set a TTL on each cached entry
- B. Use Azure Queue Storage for the work items
- C. Cache responses in Azure Managed Redis
- D. Add a read replica and send all vector queries to it

### 18. A burst of short-lived serverless requests opens a new database connection each time and exhausts server slots. What should be used first?

Domain: Develop AI solutions by using Azure data management services

- A. Use prepared statements and batch round trips
- B. Add a read replica and send all vector queries to it
- C. Reuse a bounded connection pool instead of opening a connection per request
- D. Place a connection pooler in front of PostgreSQL for many short-lived clients

### 19. A NoSQL workload must use the supported data-plane SDK for reads and must let several processor instances share change feed work. Which two components are required? Select two.

Domain: Develop AI solutions by using Azure data management services

- A. Enable autoscale throughput with a maximum RU limit
- B. Enable duplicate detection on the queue
- C. Index every property by using the default automatic policy
- D. Query through the Cosmos DB SDK with parameterized queries
- E. Use a lease container to coordinate change feed readers

### 20. A high-concurrency API must limit total database connections and survive many short-lived clients. Which two actions should you take? Select two.

Domain: Develop AI solutions by using Azure data management services

- A. Reuse a bounded connection pool instead of opening a connection per request
- B. Use prepared statements and batch round trips
- C. Add a read replica and send all vector queries to it
- D. Increase storage throughput for index builds and bulk loads
- E. Place a connection pooler in front of PostgreSQL for many short-lived clients

### 21. Which sequence correctly prepares a PostgreSQL table for vector similarity search?

Domain: Develop AI solutions by using Azure data management services

- A. Create the table with a vector column → query nearest neighbours → create the vector extension → build the index
- B. Create the vector extension → create the table with a vector column → build the index → query nearest neighbours with a distance operator
- C. Query nearest neighbours → build the index → create the vector extension → create the table with a vector column
- D. Build the index → create the vector extension → create the table with a vector column → query nearest neighbours

### 22. Events for one order must be processed in order by a single worker even when several workers are running. What should be enabled?

Domain: Connect to and consume Azure services

- A. Receive with peek-lock and complete or abandon explicitly
- B. Set a maximum delivery count and handle the dead-letter path
- C. Use Service Bus sessions to keep related messages ordered
- D. Enable duplicate detection on the queue

### 23. A topic fans out enrichment requests, but one subscriber should see only messages with a specific region property. What should be configured?

Domain: Connect to and consume Azure services

- A. Filter the Event Grid subscription by subject or event type
- B. Enable duplicate detection on the queue
- C. Define a custom event schema for the topic
- D. Add a SQL or correlation filter to a subscription

### 24. A malformed message is retried forever and blocks a worker slot. What should be configured?

Domain: Connect to and consume Azure services

- A. Set a maximum delivery count and handle the dead-letter path
- B. Inspect the dead-letter queue and resubmit corrected messages
- C. Enable duplicate detection on the queue
- D. Receive with peek-lock and complete or abandon explicitly

### 25. The queue delivers at least once, and a duplicate must not create a second order record. What should the handler do?

Domain: Connect to and consume Azure services

- A. Use prepared statements and batch round trips
- B. Orchestrate the multi-step workflow with Durable Functions
- C. Receive in receive-and-delete mode for at-most-once delivery
- D. Make the handler idempotent by using a message or business key

### 26. An event subscription receives every resource change but only blob-created events are relevant. What should be added?

Domain: Connect to and consume Azure services

- A. Enable duplicate detection on the queue
- B. Bind a queue or event trigger to the function
- C. Filter the Event Grid subscription by subject or event type
- D. Add a SQL or correlation filter to a subscription

### 27. A webhook handler is intermittently unavailable and events must not be lost permanently. What should be configured?

Domain: Connect to and consume Azure services

- A. Filter the Event Grid subscription by subject or event type
- B. Define a custom event schema for the topic
- C. Rely on Event Grid retries with a dead-letter destination
- D. Stream telemetry through Azure Event Hubs

### 28. A function must run automatically when a message arrives on a queue, without a polling loop in application code. What should be configured?

Domain: Connect to and consume Azure services

- A. Use input and output bindings instead of hand-written SDK calls
- B. Expose the endpoint through an HTTP trigger
- C. Orchestrate the multi-step workflow with Durable Functions
- D. Bind a queue or event trigger to the function

### 29. An interactive function must avoid cold-start latency and must reach resources over a virtual network. Which hosting choice fits?

Domain: Connect to and consume Azure services

- A. Host the function app on the consumption plan
- B. Host the function app on a premium plan with pre-warmed instances
- C. Expose the endpoint through an HTTP trigger
- D. Orchestrate the multi-step workflow with Durable Functions

### 30. One order event must reach an inventory handler and a billing handler independently, and billing should receive only high-value orders. Which two features are required? Select two.

Domain: Connect to and consume Azure services

- A. Add a SQL or correlation filter to a subscription
- B. Use Azure Queue Storage for the work items
- C. Queue the work on a Service Bus queue and process it with a worker
- D. Publish to a Service Bus topic with multiple subscriptions
- E. Filter the Event Grid subscription by subject or event type

### 31. Poison messages must not be lost and must not loop indefinitely. Which two capabilities address that? Select two.

Domain: Connect to and consume Azure services

- A. Receive in receive-and-delete mode for at-most-once delivery
- B. Inspect the dead-letter queue and resubmit corrected messages
- C. Use prepared statements and batch round trips
- D. Set a maximum delivery count and handle the dead-letter path
- E. Enable duplicate detection on the queue

### 32. A domain event that is not a resource lifecycle notification must be published and routed only to the correct consumer. Which two elements are required? Select two.

Domain: Connect to and consume Azure services

- A. Add a SQL or correlation filter to a subscription
- B. Stream telemetry through Azure Event Hubs
- C. Define a custom event schema for the topic
- D. Filter the Event Grid subscription by subject or event type
- E. Rely on Event Grid retries with a dead-letter destination

### 33. Which sequence correctly processes an enrichment message through Service Bus?

Domain: Connect to and consume Azure services

- A. Publish the message → receive with peek-lock → process the work → complete the message → dead-letter after the delivery limit
- B. Receive with peek-lock → publish the message → complete the message → process the work → dead-letter after the delivery limit
- C. Publish the message → complete the message → receive with peek-lock → process the work → dead-letter after the delivery limit
- D. Process the work → receive with peek-lock → publish the message → complete the message → dead-letter after the delivery limit

### 34. A partner credential must be stored with access control and audit rather than in a container environment variable. Where should it live?

Domain: Secure, monitor, troubleshoot Azure solutions

- A. Supply configuration through App Service application settings
- B. Pin the application to a specific secret version
- C. Store the secret in Azure Key Vault and read it at runtime
- D. Assign a least-privilege role to the application identity

### 35. Credentials must be replaced every 60 days without an application outage or manual redeployment. What should be implemented?

Domain: Secure, monitor, troubleshoot Azure solutions

- A. Rotate the secret on a schedule and let apps resolve the current version
- B. Supply configuration through App Service application settings
- C. Pin the application to a specific secret version
- D. Authenticate with a managed identity instead of a stored key

### 36. Feature flags must be changed per environment without redeploying the service or editing code. What should be used?

Domain: Secure, monitor, troubleshoot Azure solutions

- A. Use App Configuration labels to separate environments
- B. Store settings and feature flags in Azure App Configuration
- C. Store the secret in Azure Key Vault and read it at runtime
- D. Supply configuration through App Service application settings

### 37. A running service still uses yesterday's threshold after the value was changed in the configuration store. What is missing?

Domain: Secure, monitor, troubleshoot Azure solutions

- A. Enable configuration refresh so changes apply without a restart
- B. Deploy the function app through a CI pipeline with app settings applied
- C. Pin the application to a specific secret version
- D. Use App Configuration labels to separate environments

### 38. A request crosses an HTTP API, a queue, and a function, and the team needs one connected trace across all three hops. What should be implemented?

Domain: Secure, monitor, troubleshoot Azure solutions

- A. Query the workspace with KQL to find the failing operation
- B. Instrument the service with the OpenTelemetry SDK
- C. Send telemetry to Application Insights and inspect the transaction view
- D. Enable diagnostic settings to route platform logs to the workspace

### 39. The team needs the failure rate per five-minute window during an incident rather than a single daily average. Which query construct should be used?

Domain: Secure, monitor, troubleshoot Azure solutions

- A. Query the workspace with KQL to find the failing operation
- B. Aggregate with summarize and bin to see the failure rate over time
- C. Create an alert rule on the failure rate or latency metric
- D. Join the requests and dependencies tables on the operation ID

### 40. A request is slow but no exception is logged, and the team suspects one downstream dependency. What should the query do?

Domain: Secure, monitor, troubleshoot Azure solutions

- A. Join the requests and dependencies tables on the operation ID
- B. Create an alert rule on the failure rate or latency metric
- C. Send telemetry to Application Insights and inspect the transaction view
- D. Aggregate with summarize and bin to see the failure rate over time

### 41. On-call must be notified automatically when latency crosses a threshold for ten minutes. What should be configured?

Domain: Secure, monitor, troubleshoot Azure solutions

- A. Aggregate with summarize and bin to see the failure rate over time
- B. Enable diagnostic settings to route platform logs to the workspace
- C. Send telemetry to Application Insights and inspect the transaction view
- D. Create an alert rule on the failure rate or latency metric

### 42. A container must read a secret and a database without any stored credential in its image or settings. What should it use?

Domain: Secure, monitor, troubleshoot Azure solutions

- A. Authenticate with a managed identity instead of a stored key
- B. Supply configuration through App Service application settings
- C. Assign a least-privilege role to the application identity
- D. Store the secret in Azure Key Vault and read it at runtime

### 43. A secret must be held in a managed vault and read without a stored credential. Which two actions should you take? Select two.

Domain: Secure, monitor, troubleshoot Azure solutions

- A. Pin the application to a specific secret version
- B. Supply configuration through App Service application settings
- C. Rotate the secret on a schedule and let apps resolve the current version
- D. Authenticate with a managed identity instead of a stored key
- E. Store the secret in Azure Key Vault and read it at runtime

### 44. Which sequence correctly introduces a rotated secret to a running application?

Domain: Secure, monitor, troubleshoot Azure solutions

- A. Rotate the secret → reference the secret from the app → store the secret in Key Vault → grant the app identity access → the app reads the new version
- B. Grant the app identity access → store the secret in Key Vault → rotate the secret → reference the secret from the app → the app reads the new version
- C. Reference the secret from the app → rotate the secret → store the secret in Key Vault → grant the app identity access → the app reads the new version
- D. Store the secret in Key Vault → grant the app identity access → reference the secret from the app → rotate the secret → the app reads the new version

---

## Case study — Fabrikam catalog

The next three questions refer to this scenario. Read the full scenario before answering; case-study items are scored individually.

### 45. Retrieval must return only chunks the caller is entitled to see while still returning a full result set. What should the query do?

Domain: Develop AI solutions by using Azure data management services

- A. Filter on metadata columns in the same query as the vector search
- B. Create an HNSW index for low-latency approximate search
- C. Retrieve nearest neighbours first and discard unauthorized rows in the application
- D. Create an IVFFlat index to save memory on a large table

### 46. Vector queries became slow after the index grew, and the server shows heavy memory pressure. What should be addressed?

Domain: Develop AI solutions by using Azure data management services

- A. Add a read replica and send all vector queries to it
- B. Scale compute and memory to fit index size and query concurrency
- C. Increase storage throughput for index builds and bulk loads
- D. Place a connection pooler in front of PostgreSQL for many short-lived clients

### 47. A latency-critical similarity lookup must avoid a round trip to the relational database. What should be used?

Domain: Develop AI solutions by using Azure data management services

- A. Use a distributed lock in Redis to make processing idempotent
- B. Cache responses in Azure Managed Redis
- C. Store user session state in Managed Redis with an expiry
- D. Create a vector index in Managed Redis for similarity search

---

## Case study — Northwind catalog

The next three questions refer to this scenario. Read the full scenario before answering; case-study items are scored individually.

### 48. A new ranking service must receive a small share of production traffic while the previous version keeps serving the rest. Which capability provides that split?

Domain: Develop containerized solutions on Azure

- A. Create a new Container Apps revision and shift traffic between revisions
- B. Stage the change in a deployment slot and swap after verification
- C. Rely on the horizontal pod autoscaler on CPU
- D. Replicate the registry to each deployment region

### 49. Workers are idle overnight and back up during promotions, and the queue length is the true measure of work. What should drive replica count?

Domain: Develop containerized solutions on Azure

- A. Scale only on CPU utilization without an event scaler
- B. Scale on the Service Bus queue length with a KEDA Azure Service Bus scaler
- C. Run the batch job in Azure Container Instances
- D. Rely on the horizontal pod autoscaler on CPU

### 50. The container needs a third-party API key, and auditors must confirm it is never stored in deployment settings. What should the app configuration use?

Domain: Develop containerized solutions on Azure

- A. Deploy the mutable latest tag and let the platform resolve it
- B. Pin the application to a specific secret version
- C. Reference a Key Vault secret from the app configuration instead of storing it
- D. Supply configuration through App Service application settings

---

## Answer key and explanations

### Question 1 — B

Answer: Build and store versioned images in Azure Container Registry. Immutable, versioned tags tie a running deployment to a reviewed build and make rollback deterministic. ACR keeps tagged, versioned images next to the deployment target and supports identity-based pulls. Tagging strategy and retention still need a decision. Local study-map skill 1.1 (Container Image Lifecycle in Azure Container Registry), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure container hosting documentation: https://learn.microsoft.com/en-us/azure/container-apps/

- **A:** Incorrect for this question. ACR Tasks builds images in Azure on a commit or schedule without a local Docker host. It removes build-host drift but not image review. Why the correct answer wins: Immutable, versioned tags tie a running deployment to a reviewed build and make rollback deterministic.
- **B:** Correct. ACR keeps tagged, versioned images next to the deployment target and supports identity-based pulls. Tagging strategy and retention still need a decision. In this case: Immutable, versioned tags tie a running deployment to a reviewed build and make rollback deterministic.
- **C:** Incorrect for this question. A floating tag removes the link between a deployed revision and a specific build, so rollback and audit become guesswork. Why the correct answer wins: Immutable, versioned tags tie a running deployment to a reviewed build and make rollback deterministic.
- **D:** Incorrect for this question. A retention policy controls storage growth and registry clutter. It does not change which image tag a deployment references. Why the correct answer wins: Immutable, versioned tags tie a running deployment to a reviewed build and make rollback deterministic.

### Question 2 — C

Answer: Run image builds on demand or on a trigger with ACR Tasks. ACR Tasks builds the image in Azure from source on demand or on a trigger, so the build environment is identical every time. ACR Tasks builds images in Azure on a commit or schedule without a local Docker host. It removes build-host drift but not image review. Local study-map skill 1.2 (Automated Image Builds with ACR Tasks), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure container hosting documentation: https://learn.microsoft.com/en-us/azure/container-apps/

- **A:** Incorrect for this question. A slot swap warms the new version before it takes production traffic and makes rollback a second swap. Slot-local settings must be marked sticky. Why the correct answer wins: ACR Tasks builds the image in Azure from source on demand or on a trigger, so the build environment is identical every time.
- **B:** Incorrect for this question. Geo-replication reduces cross-region pull latency and gives a local copy during a regional failure. It adds cost and replication management. Why the correct answer wins: ACR Tasks builds the image in Azure from source on demand or on a trigger, so the build environment is identical every time.
- **C:** Correct. ACR Tasks builds images in Azure on a commit or schedule without a local Docker host. It removes build-host drift but not image review. In this case: ACR Tasks builds the image in Azure from source on demand or on a trigger, so the build environment is identical every time.
- **D:** Incorrect for this question. ACR keeps tagged, versioned images next to the deployment target and supports identity-based pulls. Tagging strategy and retention still need a decision. Why the correct answer wins: ACR Tasks builds the image in Azure from source on demand or on a trigger, so the build environment is identical every time.

### Question 3 — B

Answer: Supply configuration through App Service application settings. Application settings become environment variables and can differ per slot, so configuration changes do not require a new image. Application settings become environment variables for the container and can be swapped per slot. Sensitive values should still reference a vault. Local study-map skill 1.3 (Container Deployment to Azure App Service), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure container hosting documentation: https://learn.microsoft.com/en-us/azure/container-apps/

- **A:** Incorrect for this question. A slot swap warms the new version before it takes production traffic and makes rollback a second swap. Slot-local settings must be marked sticky. Why the correct answer wins: Application settings become environment variables and can differ per slot, so configuration changes do not require a new image.
- **B:** Correct. Application settings become environment variables for the container and can be swapped per slot. Sensitive values should still reference a vault. In this case: Application settings become environment variables and can differ per slot, so configuration changes do not require a new image.
- **C:** Incorrect for this question. A Key Vault reference resolves at runtime so the secret is never written into application settings. The app identity still needs permission to read it. Why the correct answer wins: Application settings become environment variables and can differ per slot, so configuration changes do not require a new image.
- **D:** Incorrect for this question. App Service runs a container with managed patching, deployment slots, and built-in authentication options. It is not a Kubernetes control plane. Why the correct answer wins: Application settings become environment variables and can differ per slot, so configuration changes do not require a new image.

### Question 4 — C

Answer: Configure Container Apps ingress for internal-only access. Internal ingress keeps the endpoint off the public internet while remaining reachable inside the environment. Internal ingress keeps the endpoint inside the environment virtual network. It is an exposure control, not an authorization control. Local study-map skill 1.4 (Container Apps Deployment and Revisions), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure container hosting documentation: https://learn.microsoft.com/en-us/azure/container-apps/

- **A:** Incorrect for this question. Container Apps provides a managed environment, revisions, and KEDA-based scaling without cluster administration. Platform limits differ from AKS. Why the correct answer wins: Internal ingress keeps the endpoint off the public internet while remaining reachable inside the environment.
- **B:** Incorrect for this question. KEDA scalers drive replica count from queue length, lag, or other event metrics, including scale to zero. Cool-down and max replicas bound the behavior. Why the correct answer wins: Internal ingress keeps the endpoint off the public internet while remaining reachable inside the environment.
- **C:** Correct. Internal ingress keeps the endpoint inside the environment virtual network. It is an exposure control, not an authorization control. In this case: Internal ingress keeps the endpoint off the public internet while remaining reachable inside the environment.
- **D:** Incorrect for this question. Revision-based traffic splitting enables canary and blue-green releases. Revision mode and scale rules must be set deliberately. Why the correct answer wins: Internal ingress keeps the endpoint off the public internet while remaining reachable inside the environment.

### Question 5 — D

Answer: Apply a declarative Kubernetes manifest to the cluster. A declarative manifest describes the desired state and is idempotent when reapplied. A manifest declares the desired deployment, service, and probe configuration in version control. Applying it repeatedly is idempotent. Local study-map skill 1.6 (AKS Deployment with Manifests), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure container hosting documentation: https://learn.microsoft.com/en-us/azure/container-apps/

- **A:** Incorrect for this question. HPA adjusts replicas from resource metrics but needs metrics-server and enough node capacity. It cannot scale to zero. Why the correct answer wins: A declarative manifest describes the desired state and is idempotent when reapplied.
- **B:** Incorrect for this question. ACR Tasks builds images in Azure on a commit or schedule without a local Docker host. It removes build-host drift but not image review. Why the correct answer wins: A declarative manifest describes the desired state and is idempotent when reapplied.
- **C:** Incorrect for this question. Container Instances starts a single container group quickly for short tasks. It has no orchestrator-level scaling or revision model. Why the correct answer wins: A declarative manifest describes the desired state and is idempotent when reapplied.
- **D:** Correct. A manifest declares the desired deployment, service, and probe configuration in version control. Applying it repeatedly is idempotent. In this case: A declarative manifest describes the desired state and is idempotent when reapplied.

### Question 6 — D

Answer: Test end-to-end connectivity from inside the container to each dependency. Testing the path from inside the container proves DNS, egress, and firewall behavior that host-side tests cannot reproduce. Reaching a dependency from the pod or replica proves DNS, egress, and firewall paths together. Host-side tests can succeed while the container path fails. Local study-map skill 1.7 (Container Logs, Events, and Connectivity), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure container hosting documentation: https://learn.microsoft.com/en-us/azure/container-apps/

- **A:** Incorrect for this question. Platform logs and metrics must be routed before they can be queried or alerted on. Retention and cost follow the workspace settings. Why the correct answer wins: Testing the path from inside the container proves DNS, egress, and firewall behavior that host-side tests cannot reproduce.
- **B:** Incorrect for this question. Readiness gates traffic until the app can serve it, and liveness restarts a wedged container. Wrong thresholds cause restart loops. Why the correct answer wins: Testing the path from inside the container proves DNS, egress, and firewall behavior that host-side tests cannot reproduce.
- **C:** Incorrect for this question. Container Apps and AKS surface stdout logs and platform events into a workspace for KQL analysis. Verbosity and retention cost money. Why the correct answer wins: Testing the path from inside the container proves DNS, egress, and firewall behavior that host-side tests cannot reproduce.
- **D:** Correct. Reaching a dependency from the pod or replica proves DNS, egress, and firewall paths together. Host-side tests can succeed while the container path fails. In this case: Testing the path from inside the container proves DNS, egress, and firewall behavior that host-side tests cannot reproduce.

### Question 7 — D, E

Answers: Build and store versioned images in Azure Container Registry; Apply an ACR retention policy to prune old untagged manifests. Versioned tags provide traceable artifacts, and a retention policy prunes stale manifests so storage does not grow without bound. ACR keeps tagged, versioned images next to the deployment target and supports identity-based pulls. Tagging strategy and retention still need a decision. A retention policy controls storage growth and registry clutter. It does not change which image tag a deployment references. Local study-map skill 1.1 (Container Image Lifecycle in Azure Container Registry), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure container hosting documentation: https://learn.microsoft.com/en-us/azure/container-apps/

- **A:** Incorrect for this question. A floating tag removes the link between a deployed revision and a specific build, so rollback and audit become guesswork. Why the correct answer wins: Versioned tags provide traceable artifacts, and a retention policy prunes stale manifests so storage does not grow without bound.
- **B:** Incorrect for this question. A slot swap warms the new version before it takes production traffic and makes rollback a second swap. Slot-local settings must be marked sticky. Why the correct answer wins: Versioned tags provide traceable artifacts, and a retention policy prunes stale manifests so storage does not grow without bound.
- **C:** Incorrect for this question. Geo-replication reduces cross-region pull latency and gives a local copy during a regional failure. It adds cost and replication management. Why the correct answer wins: Versioned tags provide traceable artifacts, and a retention policy prunes stale manifests so storage does not grow without bound.
- **D:** Correct. ACR keeps tagged, versioned images next to the deployment target and supports identity-based pulls. Tagging strategy and retention still need a decision. In this case: Versioned tags provide traceable artifacts, and a retention policy prunes stale manifests so storage does not grow without bound.
- **E:** Correct. A retention policy controls storage growth and registry clutter. It does not change which image tag a deployment references. In this case: Versioned tags provide traceable artifacts, and a retention policy prunes stale manifests so storage does not grow without bound.

### Question 8 — B, E

Answers: Apply a declarative Kubernetes manifest to the cluster; Add readiness and liveness probes to the pod specification. An applied manifest makes the desired state repeatable, and a readiness probe holds traffic until the app is actually serviceable. A manifest declares the desired deployment, service, and probe configuration in version control. Applying it repeatedly is idempotent. Readiness gates traffic until the app can serve it, and liveness restarts a wedged container. Wrong thresholds cause restart loops. Local study-map skill 1.6 (AKS Deployment with Manifests), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure container hosting documentation: https://learn.microsoft.com/en-us/azure/container-apps/

- **A:** Incorrect for this question. Container Instances starts a single container group quickly for short tasks. It has no orchestrator-level scaling or revision model. Why the correct answer wins: An applied manifest makes the desired state repeatable, and a readiness probe holds traffic until the app is actually serviceable.
- **B:** Correct. Readiness gates traffic until the app can serve it, and liveness restarts a wedged container. Wrong thresholds cause restart loops. In this case: An applied manifest makes the desired state repeatable, and a readiness probe holds traffic until the app is actually serviceable.
- **C:** Incorrect for this question. HPA adjusts replicas from resource metrics but needs metrics-server and enough node capacity. It cannot scale to zero. Why the correct answer wins: An applied manifest makes the desired state repeatable, and a readiness probe holds traffic until the app is actually serviceable.
- **D:** Incorrect for this question. CPU-based scaling reacts after work is already queued and cannot scale to zero on an empty queue. It suits steady request-driven services. Why the correct answer wins: An applied manifest makes the desired state repeatable, and a readiness probe holds traffic until the app is actually serviceable.
- **E:** Correct. A manifest declares the desired deployment, service, and probe configuration in version control. Applying it repeatedly is idempotent. In this case: An applied manifest makes the desired state repeatable, and a readiness probe holds traffic until the app is actually serviceable.

### Question 9 — D

Answer: Build and push the image → deploy a new revision → shift a small traffic percentage → check metrics → promote or roll back. The image must exist before the revision, the revision before traffic, and metrics before promotion. A canary revision accepts a small share of traffic so metrics decide promotion rather than optimism. Local study-map skill 1.5 (Event-Driven Scaling with KEDA), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure container hosting documentation: https://learn.microsoft.com/en-us/azure/container-apps/

- **A:** Incorrect for this question. Metrics cannot be checked before the revision serves traffic. Why the correct answer wins: The image must exist before the revision, the revision before traffic, and metrics before promotion.
- **B:** Incorrect for this question. Full traffic cannot move to a revision that does not exist yet, and the image must exist before the revision. Why the correct answer wins: The image must exist before the revision, the revision before traffic, and metrics before promotion.
- **C:** Incorrect for this question. Building after traffic is shifted means the running revision has no reviewed artifact behind it. Why the correct answer wins: The image must exist before the revision, the revision before traffic, and metrics before promotion.
- **D:** Correct. A canary revision accepts a small share of traffic so metrics decide promotion rather than optimism. In this case: The image must exist before the revision, the revision before traffic, and metrics before promotion.

### Question 10 — A

Answer: Include the partition key in the query predicate. Including the partition key makes the query a single-partition read instead of fanning out across partitions. A point or single-partition query avoids fan-out across partitions. Cross-partition queries consume more RUs and add latency. Local study-map skill 2.1 (Cosmos DB SDK Access and Queries), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Cosmos DB and PostgreSQL vector documentation: https://learn.microsoft.com/en-us/azure/cosmos-db/

- **A:** Correct. A point or single-partition query avoids fan-out across partitions. Cross-partition queries consume more RUs and add latency. In this case: Including the partition key makes the query a single-partition read instead of fanning out across partitions.
- **B:** Incorrect for this question. Indexing everything is simple and makes ad hoc queries possible, at higher write cost and storage. It is a default, not an optimization. Why the correct answer wins: Including the partition key makes the query a single-partition read instead of fanning out across partitions.
- **C:** Incorrect for this question. Request units measure the work a query performs, so tuning the query is often cheaper than adding throughput. Monitor normalized RU consumption. Why the correct answer wins: Including the partition key makes the query a single-partition read instead of fanning out across partitions.
- **D:** Incorrect for this question. A good partition key distributes storage and throughput and keeps common queries single-partition. Low cardinality creates hot partitions. Why the correct answer wins: Including the partition key makes the query a single-partition read instead of fanning out across partitions.

### Question 11 — A

Answer: Restrict the indexing policy to the paths the queries use. Restricting the indexing policy to queried paths reduces write RU charge and storage. Selective indexing cuts write RU charge and storage for unused paths. Excluded paths cannot be filtered efficiently later. Local study-map skill 2.2 (Cosmos DB Indexing Policies and Request Units), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Cosmos DB and PostgreSQL vector documentation: https://learn.microsoft.com/en-us/azure/cosmos-db/

- **A:** Correct. Selective indexing cuts write RU charge and storage for unused paths. Excluded paths cannot be filtered efficiently later. In this case: Restricting the indexing policy to queried paths reduces write RU charge and storage.
- **B:** Incorrect for this question. Indexing everything is simple and makes ad hoc queries possible, at higher write cost and storage. It is a default, not an optimization. Why the correct answer wins: Restricting the indexing policy to queried paths reduces write RU charge and storage.
- **C:** Incorrect for this question. Autoscale follows demand between a minimum and maximum, avoiding throttling at peak without paying for peak all day. The maximum still caps the bill. Why the correct answer wins: Restricting the indexing policy to queried paths reduces write RU charge and storage.
- **D:** Incorrect for this question. Consistency trades freshness against latency, availability, and RU cost. The level is set at the account and can be relaxed per request. Why the correct answer wins: Restricting the indexing policy to queried paths reduces write RU charge and storage.

### Question 12 — C

Answer: Use session consistency for reads within the same client session. Session consistency guarantees monotonic reads within a client session at far lower cost than strong consistency. Session consistency guarantees monotonic reads for one session and is the common default for user-facing apps. It does not promise global freshness. Local study-map skill 2.3 (Cosmos DB Consistency Levels), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Cosmos DB and PostgreSQL vector documentation: https://learn.microsoft.com/en-us/azure/cosmos-db/

- **A:** Incorrect for this question. Consistency trades freshness against latency, availability, and RU cost. The level is set at the account and can be relaxed per request. Why the correct answer wins: Session consistency guarantees monotonic reads within a client session at far lower cost than strong consistency.
- **B:** Incorrect for this question. Strong consistency guarantees the latest committed write globally at the cost of higher latency and reduced availability during partitions. Why the correct answer wins: Session consistency guarantees monotonic reads within a client session at far lower cost than strong consistency.
- **C:** Correct. Session consistency guarantees monotonic reads for one session and is the common default for user-facing apps. It does not promise global freshness. In this case: Session consistency guarantees monotonic reads within a client session at far lower cost than strong consistency.
- **D:** Incorrect for this question. Eventual consistency is the cheapest and most available option but returns possibly stale data. It fits non-critical counters, not balances. Why the correct answer wins: Session consistency guarantees monotonic reads within a client session at far lower cost than strong consistency.

### Question 13 — B

Answer: Store embeddings in a vector property and query with VectorDistance. A vector property plus the distance function keeps embeddings and metadata in the same container and query. Cosmos DB for NoSQL supports vector properties and a distance function for similarity search in the same document store. Dimensions and index type must match the model. Local study-map skill 2.4 (Cosmos DB Vector Search and Embeddings), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Cosmos DB and PostgreSQL vector documentation: https://learn.microsoft.com/en-us/azure/cosmos-db/

- **A:** Incorrect for this question. pgvector keeps vectors beside relational data, so filters and joins run in one query. Index type and parameter tuning decide latency. Why the correct answer wins: A vector property plus the distance function keeps embeddings and metadata in the same container and query.
- **B:** Correct. Cosmos DB for NoSQL supports vector properties and a distance function for similarity search in the same document store. Dimensions and index type must match the model. In this case: A vector property plus the distance function keeps embeddings and metadata in the same container and query.
- **C:** Incorrect for this question. Application-side scoring works for tiny collections and tests, but it moves all data over the wire and does not scale with corpus size. Why the correct answer wins: A vector property plus the distance function keeps embeddings and metadata in the same container and query.
- **D:** Incorrect for this question. DiskANN trades some recall for memory efficiency on large sets. Recall and latency should be measured on representative queries. Why the correct answer wins: A vector property plus the distance function keeps embeddings and metadata in the same container and query.

### Question 14 — A

Answer: Run a change feed processor to react to new and updated items. A change feed processor streams inserts and updates in order per partition for downstream work. The change feed delivers an ordered stream of changes per partition for downstream processing. It is not a delete feed, so deletions need a workaround. Local study-map skill 2.5 (Cosmos DB Change Feed Processing), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Cosmos DB and PostgreSQL vector documentation: https://learn.microsoft.com/en-us/azure/cosmos-db/

- **A:** Correct. The change feed delivers an ordered stream of changes per partition for downstream processing. It is not a delete feed, so deletions need a workaround. In this case: A change feed processor streams inserts and updates in order per partition for downstream work.
- **B:** Incorrect for this question. Leases track partition ownership so multiple processor instances share work and resume from a continuation token. Lease writes consume RUs too. Why the correct answer wins: A change feed processor streams inserts and updates in order per partition for downstream work.
- **C:** Incorrect for this question. Event Grid delivers discrete notifications to subscribers with retries and filtering. It carries events, not large payloads or ordered streams. Why the correct answer wins: A change feed processor streams inserts and updates in order per partition for downstream work.
- **D:** Incorrect for this question. A duplicate-detection window drops repeated sends within the window, which helps with at-least-once producers. The window is time-bounded. Why the correct answer wins: A change feed processor streams inserts and updates in order per partition for downstream work.

### Question 15 — B

Answer: Model typed columns for filters and one vector column for the embedding. Typed columns for the filter fields beside one vector column keep filters fast and the embedding contract explicit. Explicit types keep filters fast and make the embedding contract clear. Storing vectors as text defeats index use. Local study-map skill 2.6 (PostgreSQL Connection and Schema Modeling), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Cosmos DB and PostgreSQL vector documentation: https://learn.microsoft.com/en-us/azure/cosmos-db/

- **A:** Incorrect for this question. Vector indexes are memory-hungry, so undersized compute causes swapping and slow queries. Right-size before tuning index parameters. Why the correct answer wins: Typed columns for the filter fields beside one vector column keep filters fast and the embedding contract explicit.
- **B:** Correct. Explicit types keep filters fast and make the embedding contract clear. Storing vectors as text defeats index use. In this case: Typed columns for the filter fields beside one vector column keep filters fast and the embedding contract explicit.
- **C:** Incorrect for this question. A replica offloads read traffic but introduces replication lag, which is dangerous for freshly written evidence. It does not reduce index memory pressure. Why the correct answer wins: Typed columns for the filter fields beside one vector column keep filters fast and the embedding contract explicit.
- **D:** Incorrect for this question. Index creation and bulk loads are I/O heavy, and throttled storage stretches maintenance windows. Storage limits are separate from compute. Why the correct answer wins: Typed columns for the filter fields beside one vector column keep filters fast and the embedding contract explicit.

### Question 16 — D

Answer: Create an HNSW index for low-latency approximate search. HNSW gives low-latency approximate search and lets recall be tuned at query time. HNSW gives fast approximate nearest-neighbour queries with a larger memory footprint and slower builds. Recall is tunable at query time. Local study-map skill 2.7 (pgvector Indexing and Query Latency), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Cosmos DB and PostgreSQL vector documentation: https://learn.microsoft.com/en-us/azure/cosmos-db/

- **A:** Incorrect for this question. An exact scan is accurate but scales linearly and burns compute. It is a baseline for measuring recall, not a production strategy. Why the correct answer wins: HNSW gives low-latency approximate search and lets recall be tuned at query time.
- **B:** Incorrect for this question. An external pooler multiplexes server connections for serverless or highly concurrent clients. Session-level features may be unavailable in transaction mode. Why the correct answer wins: HNSW gives low-latency approximate search and lets recall be tuned at query time.
- **C:** Incorrect for this question. IVFFlat uses clustering lists and needs periodic rebuilds as data grows, but costs less memory than HNSW. Probes trade recall for speed. Why the correct answer wins: HNSW gives low-latency approximate search and lets recall be tuned at query time.
- **D:** Correct. HNSW gives fast approximate nearest-neighbour queries with a larger memory footprint and slower builds. Recall is tunable at query time. In this case: HNSW gives low-latency approximate search and lets recall be tuned at query time.

### Question 17 — C

Answer: Cache responses in Azure Managed Redis. Caching the computed block in Managed Redis avoids repeating the same work for each request. A cache absorbs repeated reads and cuts latency for hot data. Cache keys, TTLs, and invalidation must match the freshness requirement. Local study-map skill 2.11 (Azure Managed Redis Caching and Invalidation), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Cosmos DB and PostgreSQL vector documentation: https://learn.microsoft.com/en-us/azure/cosmos-db/

- **A:** Incorrect for this question. A TTL bounds staleness and reclaims memory without a manual sweep. Too long a TTL hides source changes; too short wastes the cache. Why the correct answer wins: Caching the computed block in Managed Redis avoids repeating the same work for each request.
- **B:** Incorrect for this question. Queue Storage is simple and cheap for large backlogs with at-least-once delivery. It lacks topics, sessions, and scheduled messages. Why the correct answer wins: Caching the computed block in Managed Redis avoids repeating the same work for each request.
- **C:** Correct. A cache absorbs repeated reads and cuts latency for hot data. Cache keys, TTLs, and invalidation must match the freshness requirement. In this case: Caching the computed block in Managed Redis avoids repeating the same work for each request.
- **D:** Incorrect for this question. A replica offloads read traffic but introduces replication lag, which is dangerous for freshly written evidence. It does not reduce index memory pressure. Why the correct answer wins: Caching the computed block in Managed Redis avoids repeating the same work for each request.

### Question 18 — C

Answer: Reuse a bounded connection pool instead of opening a connection per request. A bounded connection pool reuses established connections and protects the server from connection storms. A bounded pool amortizes connection setup and protects the server from connection storms. Pool size must match server limits. Local study-map skill 2.10 (PostgreSQL Connection Optimization), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Cosmos DB and PostgreSQL vector documentation: https://learn.microsoft.com/en-us/azure/cosmos-db/

- **A:** Incorrect for this question. Prepared statements avoid repeated planning and reduce chatty network calls. They pair well with pooling but can interact with pool modes. Why the correct answer wins: A bounded connection pool reuses established connections and protects the server from connection storms.
- **B:** Incorrect for this question. A replica offloads read traffic but introduces replication lag, which is dangerous for freshly written evidence. It does not reduce index memory pressure. Why the correct answer wins: A bounded connection pool reuses established connections and protects the server from connection storms.
- **C:** Correct. A bounded pool amortizes connection setup and protects the server from connection storms. Pool size must match server limits. In this case: A bounded connection pool reuses established connections and protects the server from connection storms.
- **D:** Incorrect for this question. An external pooler multiplexes server connections for serverless or highly concurrent clients. Session-level features may be unavailable in transaction mode. Why the correct answer wins: A bounded connection pool reuses established connections and protects the server from connection storms.

### Question 19 — D, E

Answers: Query through the Cosmos DB SDK with parameterized queries; Use a lease container to coordinate change feed readers. SDK queries keep the client on the supported path, and a lease container coordinates change feed ownership. SDK queries keep the client on the supported data plane and parameterization avoids injection and plan churn. Cross-partition queries still cost more. Leases track partition ownership so multiple processor instances share work and resume from a continuation token. Lease writes consume RUs too. Local study-map skill 2.1 (Cosmos DB SDK Access and Queries), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Cosmos DB and PostgreSQL vector documentation: https://learn.microsoft.com/en-us/azure/cosmos-db/

- **A:** Incorrect for this question. Autoscale follows demand between a minimum and maximum, avoiding throttling at peak without paying for peak all day. The maximum still caps the bill. Why the correct answer wins: SDK queries keep the client on the supported path, and a lease container coordinates change feed ownership.
- **B:** Incorrect for this question. A duplicate-detection window drops repeated sends within the window, which helps with at-least-once producers. The window is time-bounded. Why the correct answer wins: SDK queries keep the client on the supported path, and a lease container coordinates change feed ownership.
- **C:** Incorrect for this question. Indexing everything is simple and makes ad hoc queries possible, at higher write cost and storage. It is a default, not an optimization. Why the correct answer wins: SDK queries keep the client on the supported path, and a lease container coordinates change feed ownership.
- **D:** Correct. SDK queries keep the client on the supported data plane and parameterization avoids injection and plan churn. Cross-partition queries still cost more. In this case: SDK queries keep the client on the supported path, and a lease container coordinates change feed ownership.
- **E:** Correct. Leases track partition ownership so multiple processor instances share work and resume from a continuation token. Lease writes consume RUs too. In this case: SDK queries keep the client on the supported path, and a lease container coordinates change feed ownership.

### Question 20 — A, E

Answers: Reuse a bounded connection pool instead of opening a connection per request; Place a connection pooler in front of PostgreSQL for many short-lived clients. A bounded pool caps per-instance connections, and an external pooler multiplexes many clients onto fewer server connections. A bounded pool amortizes connection setup and protects the server from connection storms. Pool size must match server limits. An external pooler multiplexes server connections for serverless or highly concurrent clients. Session-level features may be unavailable in transaction mode. Local study-map skill 2.10 (PostgreSQL Connection Optimization), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Cosmos DB and PostgreSQL vector documentation: https://learn.microsoft.com/en-us/azure/cosmos-db/

- **A:** Correct. A bounded pool amortizes connection setup and protects the server from connection storms. Pool size must match server limits. In this case: A bounded pool caps per-instance connections, and an external pooler multiplexes many clients onto fewer server connections.
- **B:** Incorrect for this question. Prepared statements avoid repeated planning and reduce chatty network calls. They pair well with pooling but can interact with pool modes. Why the correct answer wins: A bounded pool caps per-instance connections, and an external pooler multiplexes many clients onto fewer server connections.
- **C:** Incorrect for this question. A replica offloads read traffic but introduces replication lag, which is dangerous for freshly written evidence. It does not reduce index memory pressure. Why the correct answer wins: A bounded pool caps per-instance connections, and an external pooler multiplexes many clients onto fewer server connections.
- **D:** Incorrect for this question. Index creation and bulk loads are I/O heavy, and throttled storage stretches maintenance windows. Storage limits are separate from compute. Why the correct answer wins: A bounded pool caps per-instance connections, and an external pooler multiplexes many clients onto fewer server connections.
- **E:** Correct. An external pooler multiplexes server connections for serverless or highly concurrent clients. Session-level features may be unavailable in transaction mode. In this case: A bounded pool caps per-instance connections, and an external pooler multiplexes many clients onto fewer server connections.

### Question 21 — B

Answer: Create the vector extension → create the table with a vector column → build the index → query nearest neighbours with a distance operator. The extension and table must exist before the index, and the index before efficient queries. The extension and typed column must exist before an index can be built, and the index before the query is efficient. Local study-map skill 2.7 (pgvector Indexing and Query Latency), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Cosmos DB and PostgreSQL vector documentation: https://learn.microsoft.com/en-us/azure/cosmos-db/

- **A:** Incorrect for this question. The extension is required for the vector type, and the query should follow index creation for usable latency. Why the correct answer wins: The extension and table must exist before the index, and the index before efficient queries.
- **B:** Correct. The extension and typed column must exist before an index can be built, and the index before the query is efficient. In this case: The extension and table must exist before the index, and the index before efficient queries.
- **C:** Incorrect for this question. Querying before the schema exists cannot succeed, and the index cannot precede the table. Why the correct answer wins: The extension and table must exist before the index, and the index before efficient queries.
- **D:** Incorrect for this question. An index cannot be built before the extension and the table exist. Why the correct answer wins: The extension and table must exist before the index, and the index before efficient queries.

### Question 22 — C

Answer: Use Service Bus sessions to keep related messages ordered. Sessions give exclusive, ordered processing per session ID across competing consumers. Sessions give ordered, exclusive processing per session ID across competing consumers. They require session-aware senders and receivers. Local study-map skill 3.1 (Service Bus Queues and Sessions), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure messaging and Functions documentation: https://learn.microsoft.com/en-us/azure/service-bus-messaging/

- **A:** Incorrect for this question. Peek-lock keeps the message locked until the handler completes it, giving at-least-once processing with retry. Lock duration must exceed processing time. Why the correct answer wins: Sessions give exclusive, ordered processing per session ID across competing consumers.
- **B:** Incorrect for this question. A delivery cap stops infinite retries of a failing message and moves it to the dead-letter queue. The cap must exceed legitimate transient retries. Why the correct answer wins: Sessions give exclusive, ordered processing per session ID across competing consumers.
- **C:** Correct. Sessions give ordered, exclusive processing per session ID across competing consumers. They require session-aware senders and receivers. In this case: Sessions give exclusive, ordered processing per session ID across competing consumers.
- **D:** Incorrect for this question. A duplicate-detection window drops repeated sends within the window, which helps with at-least-once producers. The window is time-bounded. Why the correct answer wins: Sessions give exclusive, ordered processing per session ID across competing consumers.

### Question 23 — D

Answer: Add a SQL or correlation filter to a subscription. A subscription filter evaluates message properties broker-side so only matching messages are delivered. Subscription filters route only matching messages to a handler, reducing wasted processing. Filter evaluation happens broker-side on message properties. Local study-map skill 3.2 (Service Bus Topics, Subscriptions, and Filters), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure messaging and Functions documentation: https://learn.microsoft.com/en-us/azure/service-bus-messaging/

- **A:** Incorrect for this question. Subject and event-type filters keep handlers focused and reduce cost. Filters are evaluated on event metadata, not payload body. Why the correct answer wins: A subscription filter evaluates message properties broker-side so only matching messages are delivered.
- **B:** Incorrect for this question. A duplicate-detection window drops repeated sends within the window, which helps with at-least-once producers. The window is time-bounded. Why the correct answer wins: A subscription filter evaluates message properties broker-side so only matching messages are delivered.
- **C:** Incorrect for this question. A custom schema fits domain events that are not resource lifecycle notifications. Consumers must version the schema contract. Why the correct answer wins: A subscription filter evaluates message properties broker-side so only matching messages are delivered.
- **D:** Correct. Subscription filters route only matching messages to a handler, reducing wasted processing. Filter evaluation happens broker-side on message properties. In this case: A subscription filter evaluates message properties broker-side so only matching messages are delivered.

### Question 24 — A

Answer: Set a maximum delivery count and handle the dead-letter path. A maximum delivery count moves a persistently failing message to the dead-letter queue after a bounded number of attempts. A delivery cap stops infinite retries of a failing message and moves it to the dead-letter queue. The cap must exceed legitimate transient retries. Local study-map skill 3.3 (Service Bus Dead-Lettering and Retries), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure messaging and Functions documentation: https://learn.microsoft.com/en-us/azure/service-bus-messaging/

- **A:** Correct. A delivery cap stops infinite retries of a failing message and moves it to the dead-letter queue. The cap must exceed legitimate transient retries. In this case: A maximum delivery count moves a persistently failing message to the dead-letter queue after a bounded number of attempts.
- **B:** Incorrect for this question. Dead-lettering preserves poison messages for diagnosis instead of losing them. Resubmission needs a fix and an idempotent handler. Why the correct answer wins: A maximum delivery count moves a persistently failing message to the dead-letter queue after a bounded number of attempts.
- **C:** Incorrect for this question. A duplicate-detection window drops repeated sends within the window, which helps with at-least-once producers. The window is time-bounded. Why the correct answer wins: A maximum delivery count moves a persistently failing message to the dead-letter queue after a bounded number of attempts.
- **D:** Incorrect for this question. Peek-lock keeps the message locked until the handler completes it, giving at-least-once processing with retry. Lock duration must exceed processing time. Why the correct answer wins: A maximum delivery count moves a persistently failing message to the dead-letter queue after a bounded number of attempts.

### Question 25 — D

Answer: Make the handler idempotent by using a message or business key. An idempotency key in the data store makes a replayed message a no-op instead of a duplicate write. At-least-once delivery means duplicates will happen, so the write must tolerate replay. A stored key makes the retry safe. Local study-map skill 3.3 (Service Bus Dead-Lettering and Retries), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure messaging and Functions documentation: https://learn.microsoft.com/en-us/azure/service-bus-messaging/

- **A:** Incorrect for this question. Prepared statements avoid repeated planning and reduce chatty network calls. They pair well with pooling but can interact with pool modes. Why the correct answer wins: An idempotency key in the data store makes a replayed message a no-op instead of a duplicate write.
- **B:** Incorrect for this question. Durable Functions provides orchestrations, activities, timers, and retries with checkpointed state. Orchestrator code must stay deterministic. Why the correct answer wins: An idempotency key in the data store makes a replayed message a no-op instead of a duplicate write.
- **C:** Incorrect for this question. Receive-and-delete removes the message on delivery, so a crash loses work silently. It suits telemetry, not payments. Why the correct answer wins: An idempotency key in the data store makes a replayed message a no-op instead of a duplicate write.
- **D:** Correct. At-least-once delivery means duplicates will happen, so the write must tolerate replay. A stored key makes the retry safe. In this case: An idempotency key in the data store makes a replayed message a no-op instead of a duplicate write.

### Question 26 — C

Answer: Filter the Event Grid subscription by subject or event type. Subject and event-type filters narrow delivery to the events the handler actually supports. Subject and event-type filters keep handlers focused and reduce cost. Filters are evaluated on event metadata, not payload body. Local study-map skill 3.4 (Event Grid Filters, Custom Events, and Retries), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure messaging and Functions documentation: https://learn.microsoft.com/en-us/azure/service-bus-messaging/

- **A:** Incorrect for this question. A duplicate-detection window drops repeated sends within the window, which helps with at-least-once producers. The window is time-bounded. Why the correct answer wins: Subject and event-type filters narrow delivery to the events the handler actually supports.
- **B:** Incorrect for this question. A trigger starts the function when work arrives and handles the receive loop for you. Poison-message behavior is configured in host settings. Why the correct answer wins: Subject and event-type filters narrow delivery to the events the handler actually supports.
- **C:** Correct. Subject and event-type filters keep handlers focused and reduce cost. Filters are evaluated on event metadata, not payload body. In this case: Subject and event-type filters narrow delivery to the events the handler actually supports.
- **D:** Incorrect for this question. Subscription filters route only matching messages to a handler, reducing wasted processing. Filter evaluation happens broker-side on message properties. Why the correct answer wins: Subject and event-type filters narrow delivery to the events the handler actually supports.

### Question 27 — C

Answer: Rely on Event Grid retries with a dead-letter destination. Event Grid retries failed deliveries and can dead-letter events that never succeed. Event Grid retries failed deliveries with backoff and can store undeliverable events. Handlers must still be idempotent. Local study-map skill 3.4 (Event Grid Filters, Custom Events, and Retries), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure messaging and Functions documentation: https://learn.microsoft.com/en-us/azure/service-bus-messaging/

- **A:** Incorrect for this question. Subject and event-type filters keep handlers focused and reduce cost. Filters are evaluated on event metadata, not payload body. Why the correct answer wins: Event Grid retries failed deliveries and can dead-letter events that never succeed.
- **B:** Incorrect for this question. A custom schema fits domain events that are not resource lifecycle notifications. Consumers must version the schema contract. Why the correct answer wins: Event Grid retries failed deliveries and can dead-letter events that never succeed.
- **C:** Correct. Event Grid retries failed deliveries with backoff and can store undeliverable events. Handlers must still be idempotent. In this case: Event Grid retries failed deliveries and can dead-letter events that never succeed.
- **D:** Incorrect for this question. Event Hubs ingests high-volume ordered streams with partitions and consumer groups. It is a streaming log, not a task queue. Why the correct answer wins: Event Grid retries failed deliveries and can dead-letter events that never succeed.

### Question 28 — D

Answer: Bind a queue or event trigger to the function. A queue trigger starts the function on arrival and manages the receive loop. A trigger starts the function when work arrives and handles the receive loop for you. Poison-message behavior is configured in host settings. Local study-map skill 3.5 (Azure Functions Triggers and Bindings), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure messaging and Functions documentation: https://learn.microsoft.com/en-us/azure/service-bus-messaging/

- **A:** Incorrect for this question. Bindings reduce boilerplate for common inputs and outputs and are configured declaratively. Complex operations still need the SDK. Why the correct answer wins: A queue trigger starts the function on arrival and manages the receive loop.
- **B:** Incorrect for this question. An HTTP trigger gives a synchronous API endpoint with route and authorization configuration. Long-running work should hand off to a queue. Why the correct answer wins: A queue trigger starts the function on arrival and manages the receive loop.
- **C:** Incorrect for this question. Durable Functions provides orchestrations, activities, timers, and retries with checkpointed state. Orchestrator code must stay deterministic. Why the correct answer wins: A queue trigger starts the function on arrival and manages the receive loop.
- **D:** Correct. A trigger starts the function when work arrives and handles the receive loop for you. Poison-message behavior is configured in host settings. In this case: A queue trigger starts the function on arrival and manages the receive loop.

### Question 29 — B

Answer: Host the function app on a premium plan with pre-warmed instances. A premium plan provides pre-warmed instances and virtual network integration. A premium plan reduces cold starts and supports virtual network integration and longer timeouts. It costs more than consumption. Local study-map skill 3.6 (Function App Configuration and Deployment), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure messaging and Functions documentation: https://learn.microsoft.com/en-us/azure/service-bus-messaging/

- **A:** Incorrect for this question. Consumption bills per execution and scales automatically, with cold starts and a timeout ceiling. It fits spiky, short work. Why the correct answer wins: A premium plan provides pre-warmed instances and virtual network integration.
- **B:** Correct. A premium plan reduces cold starts and supports virtual network integration and longer timeouts. It costs more than consumption. In this case: A premium plan provides pre-warmed instances and virtual network integration.
- **C:** Incorrect for this question. An HTTP trigger gives a synchronous API endpoint with route and authorization configuration. Long-running work should hand off to a queue. Why the correct answer wins: A premium plan provides pre-warmed instances and virtual network integration.
- **D:** Incorrect for this question. Durable Functions provides orchestrations, activities, timers, and retries with checkpointed state. Orchestrator code must stay deterministic. Why the correct answer wins: A premium plan provides pre-warmed instances and virtual network integration.

### Question 30 — A, D

Answers: Publish to a Service Bus topic with multiple subscriptions; Add a SQL or correlation filter to a subscription. A topic with separate subscriptions provides fan-out, and a subscription filter limits billing to matching messages. Topics fan out one message to independent subscribers, each with its own filter and dead-letter queue. Subscribers process at their own pace. Subscription filters route only matching messages to a handler, reducing wasted processing. Filter evaluation happens broker-side on message properties. Local study-map skill 3.2 (Service Bus Topics, Subscriptions, and Filters), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure messaging and Functions documentation: https://learn.microsoft.com/en-us/azure/service-bus-messaging/

- **A:** Correct. Subscription filters route only matching messages to a handler, reducing wasted processing. Filter evaluation happens broker-side on message properties. In this case: A topic with separate subscriptions provides fan-out, and a subscription filter limits billing to matching messages.
- **B:** Incorrect for this question. Queue Storage is simple and cheap for large backlogs with at-least-once delivery. It lacks topics, sessions, and scheduled messages. Why the correct answer wins: A topic with separate subscriptions provides fan-out, and a subscription filter limits billing to matching messages.
- **C:** Incorrect for this question. A queue decouples producers from a single consumer group and smooths bursts. Delivery semantics depend on receive mode and completion. Why the correct answer wins: A topic with separate subscriptions provides fan-out, and a subscription filter limits billing to matching messages.
- **D:** Correct. Topics fan out one message to independent subscribers, each with its own filter and dead-letter queue. Subscribers process at their own pace. In this case: A topic with separate subscriptions provides fan-out, and a subscription filter limits billing to matching messages.
- **E:** Incorrect for this question. Subject and event-type filters keep handlers focused and reduce cost. Filters are evaluated on event metadata, not payload body. Why the correct answer wins: A topic with separate subscriptions provides fan-out, and a subscription filter limits billing to matching messages.

### Question 31 — B, D

Answers: Inspect the dead-letter queue and resubmit corrected messages; Set a maximum delivery count and handle the dead-letter path. Dead-lettering preserves the failing message, and a delivery cap stops endless retries. Dead-lettering preserves poison messages for diagnosis instead of losing them. Resubmission needs a fix and an idempotent handler. A delivery cap stops infinite retries of a failing message and moves it to the dead-letter queue. The cap must exceed legitimate transient retries. Local study-map skill 3.3 (Service Bus Dead-Lettering and Retries), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure messaging and Functions documentation: https://learn.microsoft.com/en-us/azure/service-bus-messaging/

- **A:** Incorrect for this question. Receive-and-delete removes the message on delivery, so a crash loses work silently. It suits telemetry, not payments. Why the correct answer wins: Dead-lettering preserves the failing message, and a delivery cap stops endless retries.
- **B:** Correct. Dead-lettering preserves poison messages for diagnosis instead of losing them. Resubmission needs a fix and an idempotent handler. In this case: Dead-lettering preserves the failing message, and a delivery cap stops endless retries.
- **C:** Incorrect for this question. Prepared statements avoid repeated planning and reduce chatty network calls. They pair well with pooling but can interact with pool modes. Why the correct answer wins: Dead-lettering preserves the failing message, and a delivery cap stops endless retries.
- **D:** Correct. A delivery cap stops infinite retries of a failing message and moves it to the dead-letter queue. The cap must exceed legitimate transient retries. In this case: Dead-lettering preserves the failing message, and a delivery cap stops endless retries.
- **E:** Incorrect for this question. A duplicate-detection window drops repeated sends within the window, which helps with at-least-once producers. The window is time-bounded. Why the correct answer wins: Dead-lettering preserves the failing message, and a delivery cap stops endless retries.

### Question 32 — C, D

Answers: Define a custom event schema for the topic; Filter the Event Grid subscription by subject or event type. A custom event schema carries the domain payload, and a subscription filter routes it to the intended consumer. A custom schema fits domain events that are not resource lifecycle notifications. Consumers must version the schema contract. Subject and event-type filters keep handlers focused and reduce cost. Filters are evaluated on event metadata, not payload body. Local study-map skill 3.4 (Event Grid Filters, Custom Events, and Retries), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure messaging and Functions documentation: https://learn.microsoft.com/en-us/azure/service-bus-messaging/

- **A:** Incorrect for this question. Subscription filters route only matching messages to a handler, reducing wasted processing. Filter evaluation happens broker-side on message properties. Why the correct answer wins: A custom event schema carries the domain payload, and a subscription filter routes it to the intended consumer.
- **B:** Incorrect for this question. Event Hubs ingests high-volume ordered streams with partitions and consumer groups. It is a streaming log, not a task queue. Why the correct answer wins: A custom event schema carries the domain payload, and a subscription filter routes it to the intended consumer.
- **C:** Correct. A custom schema fits domain events that are not resource lifecycle notifications. Consumers must version the schema contract. In this case: A custom event schema carries the domain payload, and a subscription filter routes it to the intended consumer.
- **D:** Correct. Subject and event-type filters keep handlers focused and reduce cost. Filters are evaluated on event metadata, not payload body. In this case: A custom event schema carries the domain payload, and a subscription filter routes it to the intended consumer.
- **E:** Incorrect for this question. Event Grid retries failed deliveries with backoff and can store undeliverable events. Handlers must still be idempotent. Why the correct answer wins: A custom event schema carries the domain payload, and a subscription filter routes it to the intended consumer.

### Question 33 — A

Answer: Publish the message → receive with peek-lock → process the work → complete the message → dead-letter after the delivery limit. Peek-lock, processing, completion, and dead-lettering occur in that order. Peek-lock keeps the message until the handler succeeds, and only repeated failures should dead-letter it. Local study-map skill 3.1 (Service Bus Queues and Sessions), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure messaging and Functions documentation: https://learn.microsoft.com/en-us/azure/service-bus-messaging/

- **A:** Correct. Peek-lock keeps the message until the handler succeeds, and only repeated failures should dead-letter it. In this case: Peek-lock, processing, completion, and dead-lettering occur in that order.
- **B:** Incorrect for this question. The message cannot be received before it is published, and completion must follow processing. Why the correct answer wins: Peek-lock, processing, completion, and dead-lettering occur in that order.
- **C:** Incorrect for this question. Completing a message before processing discards the work and defeats at-least-once delivery. Why the correct answer wins: Peek-lock, processing, completion, and dead-lettering occur in that order.
- **D:** Incorrect for this question. Work cannot be processed before the message is published and received. Why the correct answer wins: Peek-lock, processing, completion, and dead-lettering occur in that order.

### Question 34 — C

Answer: Store the secret in Azure Key Vault and read it at runtime. Key Vault centralizes secret storage with role-based access and audit trails. A vault centralizes secret storage with access control and audit. Retrieval should use an identity, not a copied credential. Local study-map skill 4.1 (Key Vault Secret Storage, Rotation, and Retrieval), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Key Vault, App Configuration, and Monitor documentation: https://learn.microsoft.com/en-us/azure/azure-monitor/

- **A:** Incorrect for this question. Application settings become environment variables for the container and can be swapped per slot. Sensitive values should still reference a vault. Why the correct answer wins: Key Vault centralizes secret storage with role-based access and audit trails.
- **B:** Incorrect for this question. Pinning a version makes a rotation invisible to the app until it is redeployed, which is useful for break-glass and dangerous for routine rotation. Why the correct answer wins: Key Vault centralizes secret storage with role-based access and audit trails.
- **C:** Correct. A vault centralizes secret storage with access control and audit. Retrieval should use an identity, not a copied credential. In this case: Key Vault centralizes secret storage with role-based access and audit trails.
- **D:** Incorrect for this question. A scoped role grants only the operations the app performs and limits blast radius. Prefer built-in roles over broad contributor grants. Why the correct answer wins: Key Vault centralizes secret storage with role-based access and audit trails.

### Question 35 — A

Answer: Rotate the secret on a schedule and let apps resolve the current version. Scheduled rotation with current-version reads lets the app pick up the new secret on its next resolve. Rotation limits the value of a leaked secret, but callers must read the latest version rather than caching an old one forever. Local study-map skill 4.1 (Key Vault Secret Storage, Rotation, and Retrieval), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Key Vault, App Configuration, and Monitor documentation: https://learn.microsoft.com/en-us/azure/azure-monitor/

- **A:** Correct. Rotation limits the value of a leaked secret, but callers must read the latest version rather than caching an old one forever. In this case: Scheduled rotation with current-version reads lets the app pick up the new secret on its next resolve.
- **B:** Incorrect for this question. Application settings become environment variables for the container and can be swapped per slot. Sensitive values should still reference a vault. Why the correct answer wins: Scheduled rotation with current-version reads lets the app pick up the new secret on its next resolve.
- **C:** Incorrect for this question. Pinning a version makes a rotation invisible to the app until it is redeployed, which is useful for break-glass and dangerous for routine rotation. Why the correct answer wins: Scheduled rotation with current-version reads lets the app pick up the new secret on its next resolve.
- **D:** Incorrect for this question. A managed identity issues tokens from the platform, removing secret distribution from the app. Role assignment still scopes what it can reach. Why the correct answer wins: Scheduled rotation with current-version reads lets the app pick up the new secret on its next resolve.

### Question 36 — B

Answer: Store settings and feature flags in Azure App Configuration. App Configuration stores flags and settings with labels per environment and refresh support. App Configuration separates configuration from code and supports labels, feature flags, and Key Vault references. Change still needs a refresh strategy. Local study-map skill 4.2 (App Configuration Settings and Feature Flags), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Key Vault, App Configuration, and Monitor documentation: https://learn.microsoft.com/en-us/azure/azure-monitor/

- **A:** Incorrect for this question. Labels keep dev, test, and prod values in one store with one key schema. A misconfigured label selector silently serves the wrong values. Why the correct answer wins: App Configuration stores flags and settings with labels per environment and refresh support.
- **B:** Correct. App Configuration separates configuration from code and supports labels, feature flags, and Key Vault references. Change still needs a refresh strategy. In this case: App Configuration stores flags and settings with labels per environment and refresh support.
- **C:** Incorrect for this question. A vault centralizes secret storage with access control and audit. Retrieval should use an identity, not a copied credential. Why the correct answer wins: App Configuration stores flags and settings with labels per environment and refresh support.
- **D:** Incorrect for this question. Application settings become environment variables for the container and can be swapped per slot. Sensitive values should still reference a vault. Why the correct answer wins: App Configuration stores flags and settings with labels per environment and refresh support.

### Question 37 — A

Answer: Enable configuration refresh so changes apply without a restart. Configuration refresh is required for a running app to observe a changed value without a restart. Sentinel-key or polling refresh lets a running app pick up new settings. Refresh intervals trade responsiveness against request volume. Local study-map skill 4.2 (App Configuration Settings and Feature Flags), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Key Vault, App Configuration, and Monitor documentation: https://learn.microsoft.com/en-us/azure/azure-monitor/

- **A:** Correct. Sentinel-key or polling refresh lets a running app pick up new settings. Refresh intervals trade responsiveness against request volume. In this case: Configuration refresh is required for a running app to observe a changed value without a restart.
- **B:** Incorrect for this question. Pipeline deployment keeps code and configuration versioned together and repeatable. Secrets belong in a vault reference, not in the pipeline file. Why the correct answer wins: Configuration refresh is required for a running app to observe a changed value without a restart.
- **C:** Incorrect for this question. Pinning a version makes a rotation invisible to the app until it is redeployed, which is useful for break-glass and dangerous for routine rotation. Why the correct answer wins: Configuration refresh is required for a running app to observe a changed value without a restart.
- **D:** Incorrect for this question. Labels keep dev, test, and prod values in one store with one key schema. A misconfigured label selector silently serves the wrong values. Why the correct answer wins: Configuration refresh is required for a running app to observe a changed value without a restart.

### Question 38 — B

Answer: Instrument the service with the OpenTelemetry SDK. OpenTelemetry instrumentation with context propagation produces a single distributed trace across service boundaries. OpenTelemetry emits vendor-neutral traces, metrics, and logs with context propagation. Exporters and sampling decide what reaches the backend. Local study-map skill 4.3 (Distributed Tracing with OpenTelemetry), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Key Vault, App Configuration, and Monitor documentation: https://learn.microsoft.com/en-us/azure/azure-monitor/

- **A:** Incorrect for this question. KQL filters, projects, and aggregates log and metric tables in Log Analytics. Start narrow with a time range and a request ID. Why the correct answer wins: OpenTelemetry instrumentation with context propagation produces a single distributed trace across service boundaries.
- **B:** Correct. OpenTelemetry emits vendor-neutral traces, metrics, and logs with context propagation. Exporters and sampling decide what reaches the backend. In this case: OpenTelemetry instrumentation with context propagation produces a single distributed trace across service boundaries.
- **C:** Incorrect for this question. Application Insights correlates requests, dependencies, and exceptions into end-to-end transactions. Sampling can hide rare failures. Why the correct answer wins: OpenTelemetry instrumentation with context propagation produces a single distributed trace across service boundaries.
- **D:** Incorrect for this question. Platform logs and metrics must be routed before they can be queried or alerted on. Retention and cost follow the workspace settings. Why the correct answer wins: OpenTelemetry instrumentation with context propagation produces a single distributed trace across service boundaries.

### Question 39 — B

Answer: Aggregate with summarize and bin to see the failure rate over time. Binning with summarize produces a time series of failure rates, revealing spikes that averages hide. Time-binned aggregation reveals the shape of an incident: a step change, a ramp, or a periodic spike. Averages alone hide short outages. Local study-map skill 4.4 (KQL Queries for Logs and Metrics), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Key Vault, App Configuration, and Monitor documentation: https://learn.microsoft.com/en-us/azure/azure-monitor/

- **A:** Incorrect for this question. KQL filters, projects, and aggregates log and metric tables in Log Analytics. Start narrow with a time range and a request ID. Why the correct answer wins: Binning with summarize produces a time series of failure rates, revealing spikes that averages hide.
- **B:** Correct. Time-binned aggregation reveals the shape of an incident: a step change, a ramp, or a periodic spike. Averages alone hide short outages. In this case: Binning with summarize produces a time series of failure rates, revealing spikes that averages hide.
- **C:** Incorrect for this question. An alert turns a threshold breach into a notification or action. Thresholds need a baseline, or the alert is noise. Why the correct answer wins: Binning with summarize produces a time series of failure rates, revealing spikes that averages hide.
- **D:** Incorrect for this question. Joining request and dependency telemetry shows which downstream call fails inside a slow request. Cross-workspace joins need the right scope. Why the correct answer wins: Binning with summarize produces a time series of failure rates, revealing spikes that averages hide.

### Question 40 — A

Answer: Join the requests and dependencies tables on the operation ID. Joining requests to dependencies on the operation ID shows which downstream call consumed the time. Joining request and dependency telemetry shows which downstream call fails inside a slow request. Cross-workspace joins need the right scope. Local study-map skill 4.4 (KQL Queries for Logs and Metrics), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Key Vault, App Configuration, and Monitor documentation: https://learn.microsoft.com/en-us/azure/azure-monitor/

- **A:** Correct. Joining request and dependency telemetry shows which downstream call fails inside a slow request. Cross-workspace joins need the right scope. In this case: Joining requests to dependencies on the operation ID shows which downstream call consumed the time.
- **B:** Incorrect for this question. An alert turns a threshold breach into a notification or action. Thresholds need a baseline, or the alert is noise. Why the correct answer wins: Joining requests to dependencies on the operation ID shows which downstream call consumed the time.
- **C:** Incorrect for this question. Application Insights correlates requests, dependencies, and exceptions into end-to-end transactions. Sampling can hide rare failures. Why the correct answer wins: Joining requests to dependencies on the operation ID shows which downstream call consumed the time.
- **D:** Incorrect for this question. Time-binned aggregation reveals the shape of an incident: a step change, a ramp, or a periodic spike. Averages alone hide short outages. Why the correct answer wins: Joining requests to dependencies on the operation ID shows which downstream call consumed the time.

### Question 41 — D

Answer: Create an alert rule on the failure rate or latency metric. An alert rule on the latency metric converts a sustained threshold breach into a notification. An alert turns a threshold breach into a notification or action. Thresholds need a baseline, or the alert is noise. Local study-map skill 4.4 (KQL Queries for Logs and Metrics), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Key Vault, App Configuration, and Monitor documentation: https://learn.microsoft.com/en-us/azure/azure-monitor/

- **A:** Incorrect for this question. Time-binned aggregation reveals the shape of an incident: a step change, a ramp, or a periodic spike. Averages alone hide short outages. Why the correct answer wins: An alert rule on the latency metric converts a sustained threshold breach into a notification.
- **B:** Incorrect for this question. Platform logs and metrics must be routed before they can be queried or alerted on. Retention and cost follow the workspace settings. Why the correct answer wins: An alert rule on the latency metric converts a sustained threshold breach into a notification.
- **C:** Incorrect for this question. Application Insights correlates requests, dependencies, and exceptions into end-to-end transactions. Sampling can hide rare failures. Why the correct answer wins: An alert rule on the latency metric converts a sustained threshold breach into a notification.
- **D:** Correct. An alert turns a threshold breach into a notification or action. Thresholds need a baseline, or the alert is noise. In this case: An alert rule on the latency metric converts a sustained threshold breach into a notification.

### Question 42 — A

Answer: Authenticate with a managed identity instead of a stored key. A managed identity obtains tokens from the platform so no credential is stored in the image or settings. A managed identity issues tokens from the platform, removing secret distribution from the app. Role assignment still scopes what it can reach. Local study-map skill 4.5 (Identity-Based Access for Application Services), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Key Vault, App Configuration, and Monitor documentation: https://learn.microsoft.com/en-us/azure/azure-monitor/

- **A:** Correct. A managed identity issues tokens from the platform, removing secret distribution from the app. Role assignment still scopes what it can reach. In this case: A managed identity obtains tokens from the platform so no credential is stored in the image or settings.
- **B:** Incorrect for this question. Application settings become environment variables for the container and can be swapped per slot. Sensitive values should still reference a vault. Why the correct answer wins: A managed identity obtains tokens from the platform so no credential is stored in the image or settings.
- **C:** Incorrect for this question. A scoped role grants only the operations the app performs and limits blast radius. Prefer built-in roles over broad contributor grants. Why the correct answer wins: A managed identity obtains tokens from the platform so no credential is stored in the image or settings.
- **D:** Incorrect for this question. A vault centralizes secret storage with access control and audit. Retrieval should use an identity, not a copied credential. Why the correct answer wins: A managed identity obtains tokens from the platform so no credential is stored in the image or settings.

### Question 43 — D, E

Answers: Store the secret in Azure Key Vault and read it at runtime; Authenticate with a managed identity instead of a stored key. Storing the secret in Key Vault centralizes control, and a managed identity removes the need for a stored key to read it. A vault centralizes secret storage with access control and audit. Retrieval should use an identity, not a copied credential. A managed identity issues tokens from the platform, removing secret distribution from the app. Role assignment still scopes what it can reach. Local study-map skill 4.1 (Key Vault Secret Storage, Rotation, and Retrieval), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Key Vault, App Configuration, and Monitor documentation: https://learn.microsoft.com/en-us/azure/azure-monitor/

- **A:** Incorrect for this question. Pinning a version makes a rotation invisible to the app until it is redeployed, which is useful for break-glass and dangerous for routine rotation. Why the correct answer wins: Storing the secret in Key Vault centralizes control, and a managed identity removes the need for a stored key to read it.
- **B:** Incorrect for this question. Application settings become environment variables for the container and can be swapped per slot. Sensitive values should still reference a vault. Why the correct answer wins: Storing the secret in Key Vault centralizes control, and a managed identity removes the need for a stored key to read it.
- **C:** Incorrect for this question. Rotation limits the value of a leaked secret, but callers must read the latest version rather than caching an old one forever. Why the correct answer wins: Storing the secret in Key Vault centralizes control, and a managed identity removes the need for a stored key to read it.
- **D:** Correct. A managed identity issues tokens from the platform, removing secret distribution from the app. Role assignment still scopes what it can reach. In this case: Storing the secret in Key Vault centralizes control, and a managed identity removes the need for a stored key to read it.
- **E:** Correct. A vault centralizes secret storage with access control and audit. Retrieval should use an identity, not a copied credential. In this case: Storing the secret in Key Vault centralizes control, and a managed identity removes the need for a stored key to read it.

### Question 44 — D

Answer: Store the secret in Key Vault → grant the app identity access → reference the secret from the app → rotate the secret → the app reads the new version. The secret is stored, access granted, referenced, and then rotated, after which the app reads the current version. Access must be granted before the reference resolves, and the app must read the current version after rotation. Local study-map skill 4.1 (Key Vault Secret Storage, Rotation, and Retrieval), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Key Vault, App Configuration, and Monitor documentation: https://learn.microsoft.com/en-us/azure/azure-monitor/

- **A:** Incorrect for this question. There is nothing to rotate or reference before the secret is stored. Why the correct answer wins: The secret is stored, access granted, referenced, and then rotated, after which the app reads the current version.
- **B:** Incorrect for this question. Access can be granted first, but rotation cannot precede storing the secret. Why the correct answer wins: The secret is stored, access granted, referenced, and then rotated, after which the app reads the current version.
- **C:** Incorrect for this question. A reference cannot resolve before the secret and the access grant exist. Why the correct answer wins: The secret is stored, access granted, referenced, and then rotated, after which the app reads the current version.
- **D:** Correct. Access must be granted before the reference resolves, and the app must read the current version after rotation. In this case: The secret is stored, access granted, referenced, and then rotated, after which the app reads the current version.

### Question 45 — A

Answer: Filter on metadata columns in the same query as the vector search. Filtering on metadata in the same query as the distance operator keeps the result set complete and scoped. Combining a WHERE filter with the distance operator keeps retrieval inside the caller's scope and improves relevance. Index the filter columns too. Local study-map skill 2.9 (PostgreSQL RAG with Metadata Filters), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Cosmos DB and PostgreSQL vector documentation: https://learn.microsoft.com/en-us/azure/cosmos-db/

- **A:** Correct. Combining a WHERE filter with the distance operator keeps retrieval inside the caller's scope and improves relevance. Index the filter columns too. In this case: Filtering on metadata in the same query as the distance operator keeps the result set complete and scoped.
- **B:** Incorrect for this question. HNSW gives fast approximate nearest-neighbour queries with a larger memory footprint and slower builds. Recall is tunable at query time. Why the correct answer wins: Filtering on metadata in the same query as the distance operator keeps the result set complete and scoped.
- **C:** Incorrect for this question. Post-filtering can return fewer results than requested and can leak existence or counts if the filtering is careless. Push authorization into the query. Why the correct answer wins: Filtering on metadata in the same query as the distance operator keeps the result set complete and scoped.
- **D:** Incorrect for this question. IVFFlat uses clustering lists and needs periodic rebuilds as data grows, but costs less memory than HNSW. Probes trade recall for speed. Why the correct answer wins: Filtering on metadata in the same query as the distance operator keeps the result set complete and scoped.

### Question 46 — B

Answer: Scale compute and memory to fit index size and query concurrency. A vector index working set that exceeds memory causes swapping, so compute and memory must fit the index. Vector indexes are memory-hungry, so undersized compute causes swapping and slow queries. Right-size before tuning index parameters. Local study-map skill 2.8 (PostgreSQL Compute, Memory, and Storage Sizing), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Cosmos DB and PostgreSQL vector documentation: https://learn.microsoft.com/en-us/azure/cosmos-db/

- **A:** Incorrect for this question. A replica offloads read traffic but introduces replication lag, which is dangerous for freshly written evidence. It does not reduce index memory pressure. Why the correct answer wins: A vector index working set that exceeds memory causes swapping, so compute and memory must fit the index.
- **B:** Correct. Vector indexes are memory-hungry, so undersized compute causes swapping and slow queries. Right-size before tuning index parameters. In this case: A vector index working set that exceeds memory causes swapping, so compute and memory must fit the index.
- **C:** Incorrect for this question. Index creation and bulk loads are I/O heavy, and throttled storage stretches maintenance windows. Storage limits are separate from compute. Why the correct answer wins: A vector index working set that exceeds memory causes swapping, so compute and memory must fit the index.
- **D:** Incorrect for this question. An external pooler multiplexes server connections for serverless or highly concurrent clients. Session-level features may be unavailable in transaction mode. Why the correct answer wins: A vector index working set that exceeds memory causes swapping, so compute and memory must fit the index.

### Question 47 — D

Answer: Create a vector index in Managed Redis for similarity search. A Redis vector index serves similarity queries from memory at low latency. Redis vector search serves low-latency similarity queries from memory. The corpus must fit the memory budget and be rebuilt on model change. Local study-map skill 2.12 (Azure Managed Redis Vector Indexing), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Cosmos DB and PostgreSQL vector documentation: https://learn.microsoft.com/en-us/azure/cosmos-db/

- **A:** Incorrect for this question. A lock can serialize work across instances, but correctness under retries still needs idempotency keys in the data store. Locks expire and can be lost. Why the correct answer wins: A Redis vector index serves similarity queries from memory at low latency.
- **B:** Incorrect for this question. A cache absorbs repeated reads and cuts latency for hot data. Cache keys, TTLs, and invalidation must match the freshness requirement. Why the correct answer wins: A Redis vector index serves similarity queries from memory at low latency.
- **C:** Incorrect for this question. Session storage in Redis survives instance restarts and supports distributed instances. Sessions must be scoped and expiring. Why the correct answer wins: A Redis vector index serves similarity queries from memory at low latency.
- **D:** Correct. Redis vector search serves low-latency similarity queries from memory. The corpus must fit the memory budget and be rebuilt on model change. In this case: A Redis vector index serves similarity queries from memory at low latency.

### Question 48 — A

Answer: Create a new Container Apps revision and shift traffic between revisions. Container Apps revisions support percentage traffic allocation between versions, which enables a canary release and a fast rollback. Revision-based traffic splitting enables canary and blue-green releases. Revision mode and scale rules must be set deliberately. Local study-map skill 1.4 (Container Apps Deployment and Revisions), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure container hosting documentation: https://learn.microsoft.com/en-us/azure/container-apps/

- **A:** Correct. Revision-based traffic splitting enables canary and blue-green releases. Revision mode and scale rules must be set deliberately. In this case: Container Apps revisions support percentage traffic allocation between versions, which enables a canary release and a fast rollback.
- **B:** Incorrect for this question. A slot swap warms the new version before it takes production traffic and makes rollback a second swap. Slot-local settings must be marked sticky. Why the correct answer wins: Container Apps revisions support percentage traffic allocation between versions, which enables a canary release and a fast rollback.
- **C:** Incorrect for this question. HPA adjusts replicas from resource metrics but needs metrics-server and enough node capacity. It cannot scale to zero. Why the correct answer wins: Container Apps revisions support percentage traffic allocation between versions, which enables a canary release and a fast rollback.
- **D:** Incorrect for this question. Geo-replication reduces cross-region pull latency and gives a local copy during a regional failure. It adds cost and replication management. Why the correct answer wins: Container Apps revisions support percentage traffic allocation between versions, which enables a canary release and a fast rollback.

### Question 49 — B

Answer: Scale on the Service Bus queue length with a KEDA Azure Service Bus scaler. A KEDA Service Bus scaler adds consumers while messages are backed up and scales to zero when the queue is empty. A queue-length scaler adds replicas while work is backed up and removes them when the queue drains. Message lock duration must exceed processing time. Local study-map skill 1.5 (Event-Driven Scaling with KEDA), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure container hosting documentation: https://learn.microsoft.com/en-us/azure/container-apps/

- **A:** Incorrect for this question. CPU-based scaling reacts after work is already queued and cannot scale to zero on an empty queue. It suits steady request-driven services. Why the correct answer wins: A KEDA Service Bus scaler adds consumers while messages are backed up and scales to zero when the queue is empty.
- **B:** Correct. A queue-length scaler adds replicas while work is backed up and removes them when the queue drains. Message lock duration must exceed processing time. In this case: A KEDA Service Bus scaler adds consumers while messages are backed up and scales to zero when the queue is empty.
- **C:** Incorrect for this question. Container Instances starts a single container group quickly for short tasks. It has no orchestrator-level scaling or revision model. Why the correct answer wins: A KEDA Service Bus scaler adds consumers while messages are backed up and scales to zero when the queue is empty.
- **D:** Incorrect for this question. HPA adjusts replicas from resource metrics but needs metrics-server and enough node capacity. It cannot scale to zero. Why the correct answer wins: A KEDA Service Bus scaler adds consumers while messages are backed up and scales to zero when the queue is empty.

### Question 50 — C

Answer: Reference a Key Vault secret from the app configuration instead of storing it. A Key Vault reference resolves the secret at runtime through the app identity, so the value never appears in settings or source control. A Key Vault reference resolves at runtime so the secret is never written into application settings. The app identity still needs permission to read it. Local study-map skill 1.3 (Container Deployment to Azure App Service), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure container hosting documentation: https://learn.microsoft.com/en-us/azure/container-apps/

- **A:** Incorrect for this question. A floating tag removes the link between a deployed revision and a specific build, so rollback and audit become guesswork. Why the correct answer wins: A Key Vault reference resolves the secret at runtime through the app identity, so the value never appears in settings or source control.
- **B:** Incorrect for this question. Pinning a version makes a rotation invisible to the app until it is redeployed, which is useful for break-glass and dangerous for routine rotation. Why the correct answer wins: A Key Vault reference resolves the secret at runtime through the app identity, so the value never appears in settings or source control.
- **C:** Correct. A Key Vault reference resolves at runtime so the secret is never written into application settings. The app identity still needs permission to read it. In this case: A Key Vault reference resolves the secret at runtime through the app identity, so the value never appears in settings or source control.
- **D:** Incorrect for this question. Application settings become environment variables for the container and can be swapped per slot. Sensitive values should still reference a vault. Why the correct answer wins: A Key Vault reference resolves the secret at runtime through the app identity, so the value never appears in settings or source control.
