# Microsoft AI-200 — Full-Length Mock Exam 3

Azure AI Cloud Developer Associate · 50 questions · 120 minutes · passing target 700/1000

Blueprint-weighted mock exam. Item mix: 38 single-choice, 8 multi-select (selection count stated), 4 ordering items rendered as answer choices, and 2 case studies of 3 questions. Hot-area, drag-and-drop UI, labs, and adaptive problem-solution sets cannot be reproduced in a CSV; see the README for the exact fidelity boundary.

Original educational content, not actual, recalled, or copied Microsoft exam items.

## Questions

### 1. A scoring API must pull its image locally in two regions and keep working when one region fails. What should be configured on the registry?

Domain: Develop containerized solutions on Azure

- A. Replicate the registry to each deployment region
- B. Apply an ACR retention policy to prune old untagged manifests
- C. Run image builds on demand or on a trigger with ACR Tasks
- D. Deploy the mutable latest tag and let the platform resolve it

### 2. Images must be rebuilt automatically whenever a base image security patch is published. What should be used?

Domain: Develop containerized solutions on Azure

- A. Apply an ACR retention policy to prune old untagged manifests
- B. Run image builds on demand or on a trigger with ACR Tasks
- C. Replicate the registry to each deployment region
- D. Build and store versioned images in Azure Container Registry

### 3. A small internal scoring endpoint needs platform patching, easy authentication, and deployment slots without cluster operations. What should host it?

Domain: Develop containerized solutions on Azure

- A. Run the batch job in Azure Container Instances
- B. Deploy the service to Azure Container Apps
- C. Deploy the image to Azure App Service as a web app
- D. Deploy the workload to Azure Kubernetes Service

### 4. A connection string with a key must be available to the container but must not appear in the portal settings. What should be used?

Domain: Develop containerized solutions on Azure

- A. Supply configuration through App Service application settings
- B. Reference a Key Vault secret from the app configuration instead of storing it
- C. Deploy the image to Azure App Service as a web app
- D. Stage the change in a deployment slot and swap after verification

### 5. The service must reach a database that is not exposed publicly and must accept only internal callers. What should be configured?

Domain: Develop containerized solutions on Azure

- A. Deploy into a Container Apps environment attached to the workload virtual network
- B. Create a new Container Apps revision and shift traffic between revisions
- C. Scale the container app on an event source with a KEDA scaler
- D. Configure Container Apps ingress for internal-only access

### 6. The queue scaler currently authenticates with a connection string stored in the environment. What should replace it?

Domain: Develop containerized solutions on Azure

- A. Scale the container app on an event source with a KEDA scaler
- B. Scale on the Service Bus queue length with a KEDA Azure Service Bus scaler
- C. Tune the scale rule cool-down period and maximum replicas
- D. Give the KEDA scaler a managed identity to read the event source

### 7. A pod must read a vault secret without a Kubernetes secret or stored credential. What should be configured?

Domain: Develop containerized solutions on Azure

- A. Store the secret in Azure Key Vault and read it at runtime
- B. Add readiness and liveness probes to the pod specification
- C. Authenticate with a managed identity instead of a stored key
- D. Federate a Kubernetes service account to a managed identity

### 8. You must keep release artifacts immutable and stop the registry growing without limit. Which two actions should you take? Select two.

Domain: Develop containerized solutions on Azure

- A. Apply an ACR retention policy to prune old untagged manifests
- B. Build and store versioned images in Azure Container Registry
- C. Deploy the mutable latest tag and let the platform resolve it
- D. Stage the change in a deployment slot and swap after verification
- E. Replicate the registry to each deployment region

### 9. An incident review cannot tell which build produced a faulty deployment. What should be enforced first?

Domain: Develop containerized solutions on Azure

- A. Deploy the mutable latest tag and let the platform resolve it
- B. Build and store versioned images in Azure Container Registry
- C. Run image builds on demand or on a trigger with ACR Tasks
- D. Replicate the registry to each deployment region

### 10. A fraud endpoint must serve a canary release and must stay warm during business hours. Which two settings provide that? Select two.

Domain: Develop containerized solutions on Azure

- A. Run the batch job in Azure Container Instances
- B. Create a new Container Apps revision and shift traffic between revisions
- C. Set a minimum replica count above zero for the container app
- D. Scale the container app on an event source with a KEDA scaler
- E. Rely on the horizontal pod autoscaler on CPU

### 11. Which sequence correctly promotes a scoring revision with a canary?

Domain: Develop containerized solutions on Azure

- A. Check metrics → deploy a new revision → build and push the image → shift a small traffic percentage → promote
- B. Build and push the image → deploy a new revision → shift a small traffic percentage → check metrics → promote or roll back
- C. Deploy a new revision → shift all traffic → build and push the image → check metrics → roll back
- D. Shift all traffic to a new revision → deploy the revision → check metrics → build the image → promote

### 12. A transaction lookup by card token and month must not scan the entire container. What should the query do?

Domain: Develop AI solutions by using Azure data management services

- A. Store the documents in Azure Cosmos DB for NoSQL
- B. Increase provisioned throughput and watch the RU charge per query
- C. Include the partition key in the query predicate
- D. Query through the Cosmos DB SDK with parameterized queries

### 13. A high-write ledger container indexes fields that no query filters on. What should change?

Domain: Develop AI solutions by using Azure data management services

- A. Index every property by using the default automatic policy
- B. Enable autoscale throughput with a maximum RU limit
- C. Set an item time-to-live on the container
- D. Restrict the indexing policy to the paths the queries use

### 14. A customer must see their own submitted payment as pending on the next request. Which level fits at the lowest cost?

Domain: Develop AI solutions by using Azure data management services

- A. Use eventual consistency to minimize read cost
- B. Use session consistency for reads within the same client session
- C. Use strong consistency for every read in the account
- D. Choose the account consistency level that matches the read requirement

### 15. A new embedding model produces different dimensions, and vector writes now fail. What must change?

Domain: Develop AI solutions by using Azure data management services

- A. Declare the embedding dimensions and vector index type on the container policy
- B. Use the DiskANN vector index for large collections
- C. Store embeddings in a vector property and query with VectorDistance
- D. Scan every document and compute similarity in application code

### 16. Each new transaction must be scored asynchronously without querying the whole container. What should be used?

Domain: Develop AI solutions by using Azure data management services

- A. Run a change feed processor to react to new and updated items
- B. Batch related writes in a transactional batch within one partition key
- C. Set an item time-to-live on the container
- D. Use a lease container to coordinate change feed readers

### 17. A transfer must write its debit and credit documents atomically when both share a partition key. What should be used?

Domain: Develop AI solutions by using Azure data management services

- A. Run a change feed processor to react to new and updated items
- B. Set an item time-to-live on the container
- C. Increase provisioned throughput and watch the RU charge per query
- D. Batch related writes in a transactional batch within one partition key

### 18. Fraud features must be filtered by merchant category and matched by embedding in one query. What should the table look like?

Domain: Develop AI solutions by using Azure data management services

- A. Add a read replica and send all vector queries to it
- B. Scale compute and memory to fit index size and query concurrency
- C. Store embeddings in PostgreSQL by using the pgvector extension
- D. Model typed columns for filters and one vector column for the embedding

### 19. A nearest-neighbour query became slow after a data reload, and the team is unsure which index is used. What should be done first?

Domain: Develop AI solutions by using Azure data management services

- A. Create an IVFFlat index to save memory on a large table
- B. Create an HNSW index for low-latency approximate search
- C. Inspect the plan with EXPLAIN ANALYZE before changing indexes
- D. Increase maintenance and query memory settings for index builds and sorts

### 20. Building a large index blocks the maintenance window because storage throughput is exhausted. What should be addressed?

Domain: Develop AI solutions by using Azure data management services

- A. Increase maintenance and query memory settings for index builds and sorts
- B. Reuse a bounded connection pool instead of opening a connection per request
- C. Scale compute and memory to fit index size and query concurrency
- D. Increase storage throughput for index builds and bulk loads

### 21. The API repeats the same three queries thousands of times per minute. What should be used to avoid repeated planning?

Domain: Develop AI solutions by using Azure data management services

- A. Reuse a bounded connection pool instead of opening a connection per request
- B. Use prepared statements and batch round trips
- C. Place a connection pooler in front of PostgreSQL for many short-lived clients
- D. Add a read replica and send all vector queries to it

### 22. A limit change must be reflected in cached decisions immediately, not minutes later. What is required?

Domain: Develop AI solutions by using Azure data management services

- A. Flush the database after each deployment to guarantee fresh data
- B. Rely on the eviction policy and skip explicit TTLs
- C. Invalidate or overwrite the cache entry when the source changes
- D. Set a TTL on each cached entry

### 23. Fraud patterns must be matched against known bad patterns with sub-10-millisecond latency from memory. What should be used?

Domain: Develop AI solutions by using Azure data management services

- A. Create a vector index in Managed Redis for similarity search
- B. Store user session state in Managed Redis with an expiry
- C. Use a distributed lock in Redis to make processing idempotent
- D. Cache responses in Azure Managed Redis

### 24. You must choose a vector index for two different tables. Which two statements should guide the choice? Select two.

Domain: Develop AI solutions by using Azure data management services

- A. Query without a vector index and let PostgreSQL scan the table
- B. Create an IVFFlat index to save memory on a large table
- C. Increase storage throughput for index builds and bulk loads
- D. Increase maintenance and query memory settings for index builds and sorts
- E. Create an HNSW index for low-latency approximate search

### 25. Which sequence correctly builds a vector-enabled container for pattern matching?

Domain: Develop AI solutions by using Azure data management services

- A. Apply metadata filters → query with VectorDistance → create the container with a vector policy → upsert items with embeddings
- B. Upsert items with embeddings → create the container with a vector policy → apply metadata filters → query with VectorDistance
- C. Query with VectorDistance → upsert items with embeddings → create the container with a vector policy → apply metadata filters
- D. Create the container with a vector policy → upsert items with embeddings → query with VectorDistance → apply metadata filters

### 26. Score adjustments for one card must be applied in order by a single consumer. What should be enabled?

Domain: Connect to and consume Azure services

- A. Publish to a Service Bus topic with multiple subscriptions
- B. Receive with peek-lock and complete or abandon explicitly
- C. Queue the work on a Service Bus queue and process it with a worker
- D. Use Service Bus sessions to keep related messages ordered

### 27. Authorisation, fraud review, and audit must each receive the same transaction event independently. What should be used?

Domain: Connect to and consume Azure services

- A. Use Azure Queue Storage for the work items
- B. Define a custom event schema for the topic
- C. Queue the work on a Service Bus queue and process it with a worker
- D. Publish to a Service Bus topic with multiple subscriptions

### 28. A producer retries sends during a network blip, and the consumer sees the same transaction twice within a short window. Which feature helps?

Domain: Connect to and consume Azure services

- A. Make the handler idempotent by using a message or business key
- B. Enable duplicate detection on the queue
- C. Set a maximum delivery count and handle the dead-letter path
- D. Use Service Bus sessions to keep related messages ordered

### 29. Event delivery must not depend on a shared access key. What should be configured?

Domain: Connect to and consume Azure services

- A. Filter the Event Grid subscription by subject or event type
- B. Deliver events by using a managed identity instead of a key
- C. Subscribe to a system topic for resource events
- D. Rely on Event Grid retries with a dead-letter destination

### 30. A dispute workflow must wait for an external decision and resume days later without a running host. What should be used?

Domain: Connect to and consume Azure services

- A. Orchestrate the multi-step workflow with Durable Functions
- B. Bind a queue or event trigger to the function
- C. Expose the endpoint through an HTTP trigger
- D. Move long-running work out of the HTTP request into a queue

### 31. An HTTP-triggered request times out while a long dispute assessment runs. What should change?

Domain: Connect to and consume Azure services

- A. Host the function app on a premium plan with pre-warmed instances
- B. Expose the endpoint through an HTTP trigger
- C. Host the function app on the consumption plan
- D. Move long-running work out of the HTTP request into a queue

### 32. Billing must receive only high-value transactions, and reminders must become visible at a future time. Which two capabilities provide that? Select two.

Domain: Connect to and consume Azure services

- A. Inspect the dead-letter queue and resubmit corrected messages
- B. Schedule the message for future enqueueing
- C. Add a SQL or correlation filter to a subscription
- D. Use Service Bus sessions to keep related messages ordered
- E. Enable duplicate detection on the queue

### 33. A failing message must not loop and must be preserved for investigation. Which two capabilities address that? Select two.

Domain: Connect to and consume Azure services

- A. Enable duplicate detection on the queue
- B. Receive in receive-and-delete mode for at-most-once delivery
- C. Set a maximum delivery count and handle the dead-letter path
- D. Use Service Bus sessions to keep related messages ordered
- E. Inspect the dead-letter queue and resubmit corrected messages

### 34. Which sequence correctly delivers a custom fraud event?

Domain: Connect to and consume Azure services

- A. Deliver to the handler → publish a custom event → evaluate the subscription filter → retry on failure → dead-letter undeliverable events
- B. Publish a custom event → deliver to the handler → evaluate the subscription filter → dead-letter undeliverable events → retry on failure
- C. Publish a custom event → evaluate the subscription filter → deliver to the handler → retry on failure → dead-letter undeliverable events
- D. Evaluate the subscription filter → publish a custom event → dead-letter undeliverable events → deliver to the handler → retry on failure

### 35. An acquirer credential must be auditable and revocable per environment. Where should it live?

Domain: Secure, monitor, troubleshoot Azure solutions

- A. Store settings and feature flags in Azure App Configuration
- B. Supply configuration through App Service application settings
- C. Store the secret in Azure Key Vault and read it at runtime
- D. Pin the application to a specific secret version

### 36. A non-secret threshold lives in App Configuration but its value must stay in the vault. What should be used?

Domain: Secure, monitor, troubleshoot Azure solutions

- A. Store the secret in Azure Key Vault and read it at runtime
- B. Supply configuration through App Service application settings
- C. Reference the Key Vault secret from an App Configuration key value
- D. Store settings and feature flags in Azure App Configuration

### 37. The same keys must hold different values for test and production in one store. What should be used?

Domain: Secure, monitor, troubleshoot Azure solutions

- A. Enable configuration refresh so changes apply without a restart
- B. Store settings and feature flags in Azure App Configuration
- C. Use App Configuration labels to separate environments
- D. Pin the application to a specific secret version

### 38. Trace volume costs more than the service it monitors, but rare failures must still be retained. What should be configured?

Domain: Secure, monitor, troubleshoot Azure solutions

- A. Instrument the service with the OpenTelemetry SDK
- B. Export telemetry through an OpenTelemetry collector
- C. Use head or tail sampling so trace volume stays within budget
- D. Propagate trace context across every service and queue hop

### 39. A dashboard recomputes the same hourly aggregation over millions of rows all day. What should be considered?

Domain: Secure, monitor, troubleshoot Azure solutions

- A. Store repeated aggregations in a materialized view or update policy
- B. Project only the columns needed and filter by time first
- C. Join the requests and dependencies tables on the operation ID
- D. Aggregate with summarize and bin to see the failure rate over time

### 40. The ledger database must not be reachable from the public internet, and the app runs in a Container Apps environment. What should be configured?

Domain: Secure, monitor, troubleshoot Azure solutions

- A. Reach the data service through a private endpoint
- B. Authenticate with a managed identity instead of a stored key
- C. Link the private DNS zone so the private endpoint name resolves
- D. Assign a least-privilege role to the application identity

### 41. Pods must call the data service without stored secrets and with only the operations they need. Which two actions should you take? Select two.

Domain: Secure, monitor, troubleshoot Azure solutions

- A. Federate a Kubernetes service account to a managed identity
- B. Reach the data service through a private endpoint
- C. Alert on platform metrics rather than only on log queries
- D. Assign a least-privilege role to the application identity
- E. Store the secret in Azure Key Vault and read it at runtime

### 42. A secret must be vaulted and readable by the app identity. Which two actions are required? Select two.

Domain: Secure, monitor, troubleshoot Azure solutions

- A. Use App Configuration labels to separate environments
- B. Grant the app identity data-plane access to the vault
- C. Store settings and feature flags in Azure App Configuration
- D. Pin the application to a specific secret version
- E. Store the secret in Azure Key Vault and read it at runtime

### 43. Which sequence correctly rotates a credential used by a deployed service?

Domain: Secure, monitor, troubleshoot Azure solutions

- A. Grant the app identity access → store the secret in Key Vault → rotate the secret → reference the secret from the app → the app reads the new version
- B. Store the secret in Key Vault → grant the app identity access → reference the secret from the app → rotate the secret → the app reads the new version
- C. Reference the secret from the app → rotate the secret → store the secret in Key Vault → grant the app identity access → the app reads the new version
- D. Rotate the secret → reference the secret from the app → store the secret in Key Vault → grant the app identity access → the app reads the new version

### 44. Card events must stay ordered per card, and a crashed consumer must not lose a message it had locked. Which two features are required? Select two.

Domain: Connect to and consume Azure services

- A. Receive in receive-and-delete mode for at-most-once delivery
- B. Use Service Bus sessions to keep related messages ordered
- C. Enable duplicate detection on the queue
- D. Add a SQL or correlation filter to a subscription
- E. Receive with peek-lock and complete or abandon explicitly

---

## Case study — FraudDesk

The next three questions refer to this scenario. Read the full scenario before answering; case-study items are scored individually.

### 45. Only cases the analyst is assigned to may appear in results, and the result count must stay complete. What should the query do?

Domain: Develop AI solutions by using Azure data management services

- A. Filter on metadata columns in the same query as the vector search
- B. Create an HNSW index for low-latency approximate search
- C. Retrieve nearest neighbours first and discard unauthorized rows in the application
- D. Query without a vector index and let PostgreSQL scan the table

### 46. A fraud model update must notify subscribers even though it is not an Azure resource change. What should be published?

Domain: Connect to and consume Azure services

- A. Rely on Event Grid retries with a dead-letter destination
- B. Define a custom event schema for the topic
- C. Filter the Event Grid subscription by subject or event type
- D. Subscribe to a system topic for resource events

### 47. A leaked credential must be replaced with no downtime, and the old value must stop working immediately. What should be done?

Domain: Secure, monitor, troubleshoot Azure solutions

- A. Rotate the secret on a schedule and let apps resolve the current version
- B. Enable purge protection and soft delete on the vault
- C. Pin the application to a specific secret version
- D. Authenticate with a managed identity instead of a stored key

---

## Case study — PaymentsGate

The next three questions refer to this scenario. Read the full scenario before answering; case-study items are scored individually.

### 48. A pod reports ready but cannot reach the Redis cache, and the same test works from a jump host. What should be verified?

Domain: Develop containerized solutions on Azure

- A. Add readiness and liveness probes to the pod specification
- B. Enable diagnostic settings to route platform logs to the workspace
- C. Test end-to-end connectivity from inside the container to each dependency
- D. Query container logs and Kubernetes events in Log Analytics

### 49. A message with an invalid schema is retried indefinitely and starves other work. What should be configured?

Domain: Connect to and consume Azure services

- A. Receive in receive-and-delete mode for at-most-once delivery
- B. Enable duplicate detection on the queue
- C. Set a maximum delivery count and handle the dead-letter path
- D. Receive with peek-lock and complete or abandon explicitly

### 50. On-call needs a fast alert on request failure rate without paying for repeated log scans. What should be used?

Domain: Secure, monitor, troubleshoot Azure solutions

- A. Create an alert rule on the failure rate or latency metric
- B. Alert on platform metrics rather than only on log queries
- C. Aggregate with summarize and bin to see the failure rate over time
- D. Project only the columns needed and filter by time first

---

## Answer key and explanations

### Question 1 — A

Answer: Replicate the registry to each deployment region. Geo-replication puts an image copy in each region, reducing pull latency and surviving a regional outage. Geo-replication reduces cross-region pull latency and gives a local copy during a regional failure. It adds cost and replication management. Local study-map skill 1.1 (Container Image Lifecycle in Azure Container Registry), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure container hosting documentation: https://learn.microsoft.com/en-us/azure/container-apps/

- **A:** Correct. Geo-replication reduces cross-region pull latency and gives a local copy during a regional failure. It adds cost and replication management. In this case: Geo-replication puts an image copy in each region, reducing pull latency and surviving a regional outage.
- **B:** Incorrect for this question. A retention policy controls storage growth and registry clutter. It does not change which image tag a deployment references. Why the correct answer wins: Geo-replication puts an image copy in each region, reducing pull latency and surviving a regional outage.
- **C:** Incorrect for this question. ACR Tasks builds images in Azure on a commit or schedule without a local Docker host. It removes build-host drift but not image review. Why the correct answer wins: Geo-replication puts an image copy in each region, reducing pull latency and surviving a regional outage.
- **D:** Incorrect for this question. A floating tag removes the link between a deployed revision and a specific build, so rollback and audit become guesswork. Why the correct answer wins: Geo-replication puts an image copy in each region, reducing pull latency and surviving a regional outage.

### Question 2 — B

Answer: Run image builds on demand or on a trigger with ACR Tasks. An ACR Task triggered by a base image update rebuilds the affected images without a local build host. ACR Tasks builds images in Azure on a commit or schedule without a local Docker host. It removes build-host drift but not image review. Local study-map skill 1.2 (Automated Image Builds with ACR Tasks), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure container hosting documentation: https://learn.microsoft.com/en-us/azure/container-apps/

- **A:** Incorrect for this question. A retention policy controls storage growth and registry clutter. It does not change which image tag a deployment references. Why the correct answer wins: An ACR Task triggered by a base image update rebuilds the affected images without a local build host.
- **B:** Correct. ACR Tasks builds images in Azure on a commit or schedule without a local Docker host. It removes build-host drift but not image review. In this case: An ACR Task triggered by a base image update rebuilds the affected images without a local build host.
- **C:** Incorrect for this question. Geo-replication reduces cross-region pull latency and gives a local copy during a regional failure. It adds cost and replication management. Why the correct answer wins: An ACR Task triggered by a base image update rebuilds the affected images without a local build host.
- **D:** Incorrect for this question. ACR keeps tagged, versioned images next to the deployment target and supports identity-based pulls. Tagging strategy and retention still need a decision. Why the correct answer wins: An ACR Task triggered by a base image update rebuilds the affected images without a local build host.

### Question 3 — C

Answer: Deploy the image to Azure App Service as a web app. App Service runs the container with managed maintenance and slot support. App Service runs a container with managed patching, deployment slots, and built-in authentication options. It is not a Kubernetes control plane. Local study-map skill 1.3 (Container Deployment to Azure App Service), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure container hosting documentation: https://learn.microsoft.com/en-us/azure/container-apps/

- **A:** Incorrect for this question. Container Instances starts a single container group quickly for short tasks. It has no orchestrator-level scaling or revision model. Why the correct answer wins: App Service runs the container with managed maintenance and slot support.
- **B:** Incorrect for this question. Container Apps provides a managed environment, revisions, and KEDA-based scaling without cluster administration. Platform limits differ from AKS. Why the correct answer wins: App Service runs the container with managed maintenance and slot support.
- **C:** Correct. App Service runs a container with managed patching, deployment slots, and built-in authentication options. It is not a Kubernetes control plane. In this case: App Service runs the container with managed maintenance and slot support.
- **D:** Incorrect for this question. AKS gives full Kubernetes control, including custom controllers and networking. You own node pools, upgrades, and manifest hygiene. Why the correct answer wins: App Service runs the container with managed maintenance and slot support.

### Question 4 — B

Answer: Reference a Key Vault secret from the app configuration instead of storing it. A Key Vault reference resolves the value at runtime through the app identity. A Key Vault reference resolves at runtime so the secret is never written into application settings. The app identity still needs permission to read it. Local study-map skill 1.3 (Container Deployment to Azure App Service), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure container hosting documentation: https://learn.microsoft.com/en-us/azure/container-apps/

- **A:** Incorrect for this question. Application settings become environment variables for the container and can be swapped per slot. Sensitive values should still reference a vault. Why the correct answer wins: A Key Vault reference resolves the value at runtime through the app identity.
- **B:** Correct. A Key Vault reference resolves at runtime so the secret is never written into application settings. The app identity still needs permission to read it. In this case: A Key Vault reference resolves the value at runtime through the app identity.
- **C:** Incorrect for this question. App Service runs a container with managed patching, deployment slots, and built-in authentication options. It is not a Kubernetes control plane. Why the correct answer wins: A Key Vault reference resolves the value at runtime through the app identity.
- **D:** Incorrect for this question. A slot swap warms the new version before it takes production traffic and makes rollback a second swap. Slot-local settings must be marked sticky. Why the correct answer wins: A Key Vault reference resolves the value at runtime through the app identity.

### Question 5 — A

Answer: Deploy into a Container Apps environment attached to the workload virtual network. An environment attached to the workload network supports private dependencies and internal ingress. A virtual-network-attached environment enables private access to dependencies and internal ingress. It also shifts DNS and egress design to you. Local study-map skill 1.4 (Container Apps Deployment and Revisions), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure container hosting documentation: https://learn.microsoft.com/en-us/azure/container-apps/

- **A:** Correct. A virtual-network-attached environment enables private access to dependencies and internal ingress. It also shifts DNS and egress design to you. In this case: An environment attached to the workload network supports private dependencies and internal ingress.
- **B:** Incorrect for this question. Revision-based traffic splitting enables canary and blue-green releases. Revision mode and scale rules must be set deliberately. Why the correct answer wins: An environment attached to the workload network supports private dependencies and internal ingress.
- **C:** Incorrect for this question. KEDA scalers drive replica count from queue length, lag, or other event metrics, including scale to zero. Cool-down and max replicas bound the behavior. Why the correct answer wins: An environment attached to the workload network supports private dependencies and internal ingress.
- **D:** Incorrect for this question. Internal ingress keeps the endpoint inside the environment virtual network. It is an exposure control, not an authorization control. Why the correct answer wins: An environment attached to the workload network supports private dependencies and internal ingress.

### Question 6 — D

Answer: Give the KEDA scaler a managed identity to read the event source. A scaler managed identity removes the stored connection string while still reading queue metrics. A scaler needs permission to read queue metrics; identity-based access avoids a stored connection string. Least privilege still applies to that identity. Local study-map skill 1.5 (Event-Driven Scaling with KEDA), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure container hosting documentation: https://learn.microsoft.com/en-us/azure/container-apps/

- **A:** Incorrect for this question. KEDA scalers drive replica count from queue length, lag, or other event metrics, including scale to zero. Cool-down and max replicas bound the behavior. Why the correct answer wins: A scaler managed identity removes the stored connection string while still reading queue metrics.
- **B:** Incorrect for this question. A queue-length scaler adds replicas while work is backed up and removes them when the queue drains. Message lock duration must exceed processing time. Why the correct answer wins: A scaler managed identity removes the stored connection string while still reading queue metrics.
- **C:** Incorrect for this question. Cool-down prevents replica flapping, and a maximum replica cap bounds cost and downstream load. Both are per-rule settings. Why the correct answer wins: A scaler managed identity removes the stored connection string while still reading queue metrics.
- **D:** Correct. A scaler needs permission to read queue metrics; identity-based access avoids a stored connection string. Least privilege still applies to that identity. In this case: A scaler managed identity removes the stored connection string while still reading queue metrics.

### Question 7 — D

Answer: Federate a Kubernetes service account to a managed identity. Service account federation gives the pod a token from a managed identity. Workload identity lets pods obtain tokens without stored secrets. Each workload should get its own identity and narrow role. Local study-map skill 1.6 (AKS Deployment with Manifests), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure container hosting documentation: https://learn.microsoft.com/en-us/azure/container-apps/

- **A:** Incorrect for this question. A vault centralizes secret storage with access control and audit. Retrieval should use an identity, not a copied credential. Why the correct answer wins: Service account federation gives the pod a token from a managed identity.
- **B:** Incorrect for this question. Readiness gates traffic until the app can serve it, and liveness restarts a wedged container. Wrong thresholds cause restart loops. Why the correct answer wins: Service account federation gives the pod a token from a managed identity.
- **C:** Incorrect for this question. A managed identity issues tokens from the platform, removing secret distribution from the app. Role assignment still scopes what it can reach. Why the correct answer wins: Service account federation gives the pod a token from a managed identity.
- **D:** Correct. Workload identity lets pods obtain tokens without stored secrets. Each workload should get its own identity and narrow role. In this case: Service account federation gives the pod a token from a managed identity.

### Question 8 — A, B

Answers: Build and store versioned images in Azure Container Registry; Apply an ACR retention policy to prune old untagged manifests. Versioned tags identify each artifact, and a retention policy prunes superseded manifests. ACR keeps tagged, versioned images next to the deployment target and supports identity-based pulls. Tagging strategy and retention still need a decision. A retention policy controls storage growth and registry clutter. It does not change which image tag a deployment references. Local study-map skill 1.1 (Container Image Lifecycle in Azure Container Registry), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure container hosting documentation: https://learn.microsoft.com/en-us/azure/container-apps/

- **A:** Correct. A retention policy controls storage growth and registry clutter. It does not change which image tag a deployment references. In this case: Versioned tags identify each artifact, and a retention policy prunes superseded manifests.
- **B:** Correct. ACR keeps tagged, versioned images next to the deployment target and supports identity-based pulls. Tagging strategy and retention still need a decision. In this case: Versioned tags identify each artifact, and a retention policy prunes superseded manifests.
- **C:** Incorrect for this question. A floating tag removes the link between a deployed revision and a specific build, so rollback and audit become guesswork. Why the correct answer wins: Versioned tags identify each artifact, and a retention policy prunes superseded manifests.
- **D:** Incorrect for this question. A slot swap warms the new version before it takes production traffic and makes rollback a second swap. Slot-local settings must be marked sticky. Why the correct answer wins: Versioned tags identify each artifact, and a retention policy prunes superseded manifests.
- **E:** Incorrect for this question. Geo-replication reduces cross-region pull latency and gives a local copy during a regional failure. It adds cost and replication management. Why the correct answer wins: Versioned tags identify each artifact, and a retention policy prunes superseded manifests.

### Question 9 — B

Answer: Build and store versioned images in Azure Container Registry. Versioned tags make the deployed artifact identifiable, which is the prerequisite for any review or rollback. ACR keeps tagged, versioned images next to the deployment target and supports identity-based pulls. Tagging strategy and retention still need a decision. Local study-map skill 1.1 (Container Image Lifecycle in Azure Container Registry), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure container hosting documentation: https://learn.microsoft.com/en-us/azure/container-apps/

- **A:** Incorrect for this question. A floating tag removes the link between a deployed revision and a specific build, so rollback and audit become guesswork. Why the correct answer wins: Versioned tags make the deployed artifact identifiable, which is the prerequisite for any review or rollback.
- **B:** Correct. ACR keeps tagged, versioned images next to the deployment target and supports identity-based pulls. Tagging strategy and retention still need a decision. In this case: Versioned tags make the deployed artifact identifiable, which is the prerequisite for any review or rollback.
- **C:** Incorrect for this question. ACR Tasks builds images in Azure on a commit or schedule without a local Docker host. It removes build-host drift but not image review. Why the correct answer wins: Versioned tags make the deployed artifact identifiable, which is the prerequisite for any review or rollback.
- **D:** Incorrect for this question. Geo-replication reduces cross-region pull latency and gives a local copy during a regional failure. It adds cost and replication management. Why the correct answer wins: Versioned tags make the deployed artifact identifiable, which is the prerequisite for any review or rollback.

### Question 10 — B, C

Answers: Create a new Container Apps revision and shift traffic between revisions; Set a minimum replica count above zero for the container app. Revisions allow traffic splitting between versions, and a minimum replica count avoids cold starts. Revision-based traffic splitting enables canary and blue-green releases. Revision mode and scale rules must be set deliberately. A warm minimum replica removes scale-to-zero cold starts for latency-critical endpoints. It keeps paying for idle capacity. Local study-map skill 1.4 (Container Apps Deployment and Revisions), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure container hosting documentation: https://learn.microsoft.com/en-us/azure/container-apps/

- **A:** Incorrect for this question. Container Instances starts a single container group quickly for short tasks. It has no orchestrator-level scaling or revision model. Why the correct answer wins: Revisions allow traffic splitting between versions, and a minimum replica count avoids cold starts.
- **B:** Correct. Revision-based traffic splitting enables canary and blue-green releases. Revision mode and scale rules must be set deliberately. In this case: Revisions allow traffic splitting between versions, and a minimum replica count avoids cold starts.
- **C:** Correct. A warm minimum replica removes scale-to-zero cold starts for latency-critical endpoints. It keeps paying for idle capacity. In this case: Revisions allow traffic splitting between versions, and a minimum replica count avoids cold starts.
- **D:** Incorrect for this question. KEDA scalers drive replica count from queue length, lag, or other event metrics, including scale to zero. Cool-down and max replicas bound the behavior. Why the correct answer wins: Revisions allow traffic splitting between versions, and a minimum replica count avoids cold starts.
- **E:** Incorrect for this question. HPA adjusts replicas from resource metrics but needs metrics-server and enough node capacity. It cannot scale to zero. Why the correct answer wins: Revisions allow traffic splitting between versions, and a minimum replica count avoids cold starts.

### Question 11 — B

Answer: Build and push the image → deploy a new revision → shift a small traffic percentage → check metrics → promote or roll back. The artifact is built, the revision deployed, partial traffic shifted, and metrics decide promotion. A canary revision accepts a small share of traffic so metrics decide promotion rather than optimism. Local study-map skill 1.4 (Container Apps Deployment and Revisions), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure container hosting documentation: https://learn.microsoft.com/en-us/azure/container-apps/

- **A:** Incorrect for this question. Metrics cannot be checked before the revision serves traffic. Why the correct answer wins: The artifact is built, the revision deployed, partial traffic shifted, and metrics decide promotion.
- **B:** Correct. A canary revision accepts a small share of traffic so metrics decide promotion rather than optimism. In this case: The artifact is built, the revision deployed, partial traffic shifted, and metrics decide promotion.
- **C:** Incorrect for this question. Building after traffic is shifted means the running revision has no reviewed artifact behind it. Why the correct answer wins: The artifact is built, the revision deployed, partial traffic shifted, and metrics decide promotion.
- **D:** Incorrect for this question. Full traffic cannot move to a revision that does not exist yet, and the image must exist before the revision. Why the correct answer wins: The artifact is built, the revision deployed, partial traffic shifted, and metrics decide promotion.

### Question 12 — A

Answer: Store the documents in Azure Cosmos DB for NoSQL. Including the partition key in the predicate turns the read into a single-partition query. Cosmos DB gives globally distributed, low-latency document access with tunable consistency. Partition key and RU planning determine the cost profile. Local study-map skill 2.1 (Cosmos DB SDK Access and Queries), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Cosmos DB and PostgreSQL vector documentation: https://learn.microsoft.com/en-us/azure/cosmos-db/

- **A:** Correct. Cosmos DB gives globally distributed, low-latency document access with tunable consistency. Partition key and RU planning determine the cost profile. In this case: Including the partition key in the predicate turns the read into a single-partition query.
- **B:** Incorrect for this question. Request units measure the work a query performs, so tuning the query is often cheaper than adding throughput. Monitor normalized RU consumption. Why the correct answer wins: Including the partition key in the predicate turns the read into a single-partition query.
- **C:** Incorrect for this question. A point or single-partition query avoids fan-out across partitions. Cross-partition queries consume more RUs and add latency. Why the correct answer wins: Including the partition key in the predicate turns the read into a single-partition query.
- **D:** Incorrect for this question. SDK queries keep the client on the supported data plane and parameterization avoids injection and plan churn. Cross-partition queries still cost more. Why the correct answer wins: Including the partition key in the predicate turns the read into a single-partition query.

### Question 13 — D

Answer: Restrict the indexing policy to the paths the queries use. Restricting indexed paths lowers write cost and storage. Selective indexing cuts write RU charge and storage for unused paths. Excluded paths cannot be filtered efficiently later. Local study-map skill 2.2 (Cosmos DB Indexing Policies and Request Units), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Cosmos DB and PostgreSQL vector documentation: https://learn.microsoft.com/en-us/azure/cosmos-db/

- **A:** Incorrect for this question. Indexing everything is simple and makes ad hoc queries possible, at higher write cost and storage. It is a default, not an optimization. Why the correct answer wins: Restricting indexed paths lowers write cost and storage.
- **B:** Incorrect for this question. Autoscale follows demand between a minimum and maximum, avoiding throttling at peak without paying for peak all day. The maximum still caps the bill. Why the correct answer wins: Restricting indexed paths lowers write cost and storage.
- **C:** Incorrect for this question. Item TTL expires documents automatically, which controls storage growth and data retention. It does not archive the expired content. Why the correct answer wins: Restricting indexed paths lowers write cost and storage.
- **D:** Correct. Selective indexing cuts write RU charge and storage for unused paths. Excluded paths cannot be filtered efficiently later. In this case: Restricting indexed paths lowers write cost and storage.

### Question 14 — B

Answer: Use session consistency for reads within the same client session. Session consistency guarantees read-your-writes within the session. Session consistency guarantees monotonic reads for one session and is the common default for user-facing apps. It does not promise global freshness. Local study-map skill 2.3 (Cosmos DB Consistency Levels), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Cosmos DB and PostgreSQL vector documentation: https://learn.microsoft.com/en-us/azure/cosmos-db/

- **A:** Incorrect for this question. Eventual consistency is the cheapest and most available option but returns possibly stale data. It fits non-critical counters, not balances. Why the correct answer wins: Session consistency guarantees read-your-writes within the session.
- **B:** Correct. Session consistency guarantees monotonic reads for one session and is the common default for user-facing apps. It does not promise global freshness. In this case: Session consistency guarantees read-your-writes within the session.
- **C:** Incorrect for this question. Strong consistency guarantees the latest committed write globally at the cost of higher latency and reduced availability during partitions. Why the correct answer wins: Session consistency guarantees read-your-writes within the session.
- **D:** Incorrect for this question. Consistency trades freshness against latency, availability, and RU cost. The level is set at the account and can be relaxed per request. Why the correct answer wins: Session consistency guarantees read-your-writes within the session.

### Question 15 — A

Answer: Declare the embedding dimensions and vector index type on the container policy. The container vector policy fixes dimensions, so it must be recreated to match the new model. The container vector policy fixes dimensions, distance function, and index type, so a model change requires a new policy. Mismatched dimensions fail at write time. Local study-map skill 2.4 (Cosmos DB Vector Search and Embeddings), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Cosmos DB and PostgreSQL vector documentation: https://learn.microsoft.com/en-us/azure/cosmos-db/

- **A:** Correct. The container vector policy fixes dimensions, distance function, and index type, so a model change requires a new policy. Mismatched dimensions fail at write time. In this case: The container vector policy fixes dimensions, so it must be recreated to match the new model.
- **B:** Incorrect for this question. DiskANN trades some recall for memory efficiency on large sets. Recall and latency should be measured on representative queries. Why the correct answer wins: The container vector policy fixes dimensions, so it must be recreated to match the new model.
- **C:** Incorrect for this question. Cosmos DB for NoSQL supports vector properties and a distance function for similarity search in the same document store. Dimensions and index type must match the model. Why the correct answer wins: The container vector policy fixes dimensions, so it must be recreated to match the new model.
- **D:** Incorrect for this question. Application-side scoring works for tiny collections and tests, but it moves all data over the wire and does not scale with corpus size. Why the correct answer wins: The container vector policy fixes dimensions, so it must be recreated to match the new model.

### Question 16 — A

Answer: Run a change feed processor to react to new and updated items. The change feed streams new items to a downstream scorer. The change feed delivers an ordered stream of changes per partition for downstream processing. It is not a delete feed, so deletions need a workaround. Local study-map skill 2.5 (Cosmos DB Change Feed Processing), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Cosmos DB and PostgreSQL vector documentation: https://learn.microsoft.com/en-us/azure/cosmos-db/

- **A:** Correct. The change feed delivers an ordered stream of changes per partition for downstream processing. It is not a delete feed, so deletions need a workaround. In this case: The change feed streams new items to a downstream scorer.
- **B:** Incorrect for this question. A transactional batch applies all-or-nothing within a single partition key. It cannot span partitions and still consumes RU per operation. Why the correct answer wins: The change feed streams new items to a downstream scorer.
- **C:** Incorrect for this question. Item TTL expires documents automatically, which controls storage growth and data retention. It does not archive the expired content. Why the correct answer wins: The change feed streams new items to a downstream scorer.
- **D:** Incorrect for this question. Leases track partition ownership so multiple processor instances share work and resume from a continuation token. Lease writes consume RUs too. Why the correct answer wins: The change feed streams new items to a downstream scorer.

### Question 17 — D

Answer: Batch related writes in a transactional batch within one partition key. A transactional batch applies all-or-nothing within one partition key. A transactional batch applies all-or-nothing within a single partition key. It cannot span partitions and still consumes RU per operation. Local study-map skill 2.5 (Cosmos DB Change Feed Processing), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Cosmos DB and PostgreSQL vector documentation: https://learn.microsoft.com/en-us/azure/cosmos-db/

- **A:** Incorrect for this question. The change feed delivers an ordered stream of changes per partition for downstream processing. It is not a delete feed, so deletions need a workaround. Why the correct answer wins: A transactional batch applies all-or-nothing within one partition key.
- **B:** Incorrect for this question. Item TTL expires documents automatically, which controls storage growth and data retention. It does not archive the expired content. Why the correct answer wins: A transactional batch applies all-or-nothing within one partition key.
- **C:** Incorrect for this question. Request units measure the work a query performs, so tuning the query is often cheaper than adding throughput. Monitor normalized RU consumption. Why the correct answer wins: A transactional batch applies all-or-nothing within one partition key.
- **D:** Correct. A transactional batch applies all-or-nothing within a single partition key. It cannot span partitions and still consumes RU per operation. In this case: A transactional batch applies all-or-nothing within one partition key.

### Question 18 — D

Answer: Model typed columns for filters and one vector column for the embedding. Typed filter columns beside one vector column keep both parts of the query efficient. Explicit types keep filters fast and make the embedding contract clear. Storing vectors as text defeats index use. Local study-map skill 2.6 (PostgreSQL Connection and Schema Modeling), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Cosmos DB and PostgreSQL vector documentation: https://learn.microsoft.com/en-us/azure/cosmos-db/

- **A:** Incorrect for this question. A replica offloads read traffic but introduces replication lag, which is dangerous for freshly written evidence. It does not reduce index memory pressure. Why the correct answer wins: Typed filter columns beside one vector column keep both parts of the query efficient.
- **B:** Incorrect for this question. Vector indexes are memory-hungry, so undersized compute causes swapping and slow queries. Right-size before tuning index parameters. Why the correct answer wins: Typed filter columns beside one vector column keep both parts of the query efficient.
- **C:** Incorrect for this question. pgvector keeps vectors beside relational data, so filters and joins run in one query. Index type and parameter tuning decide latency. Why the correct answer wins: Typed filter columns beside one vector column keep both parts of the query efficient.
- **D:** Correct. Explicit types keep filters fast and make the embedding contract clear. Storing vectors as text defeats index use. In this case: Typed filter columns beside one vector column keep both parts of the query efficient.

### Question 19 — C

Answer: Inspect the plan with EXPLAIN ANALYZE before changing indexes. EXPLAIN ANALYZE shows whether the index is used and where the time is spent. The plan shows whether PostgreSQL uses the vector index and where the time goes. Adding indexes without reading the plan often misses the cause. Local study-map skill 2.7 (pgvector Indexing and Query Latency), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Cosmos DB and PostgreSQL vector documentation: https://learn.microsoft.com/en-us/azure/cosmos-db/

- **A:** Incorrect for this question. IVFFlat uses clustering lists and needs periodic rebuilds as data grows, but costs less memory than HNSW. Probes trade recall for speed. Why the correct answer wins: EXPLAIN ANALYZE shows whether the index is used and where the time is spent.
- **B:** Incorrect for this question. HNSW gives fast approximate nearest-neighbour queries with a larger memory footprint and slower builds. Recall is tunable at query time. Why the correct answer wins: EXPLAIN ANALYZE shows whether the index is used and where the time is spent.
- **C:** Correct. The plan shows whether PostgreSQL uses the vector index and where the time goes. Adding indexes without reading the plan often misses the cause. In this case: EXPLAIN ANALYZE shows whether the index is used and where the time is spent.
- **D:** Incorrect for this question. Index builds and large sorts spill to disk when work memory is too small, stretching maintenance windows and slowing queries. Why the correct answer wins: EXPLAIN ANALYZE shows whether the index is used and where the time is spent.

### Question 20 — D

Answer: Increase storage throughput for index builds and bulk loads. Index builds are I/O heavy, so storage throughput must support the build window. Index creation and bulk loads are I/O heavy, and throttled storage stretches maintenance windows. Storage limits are separate from compute. Local study-map skill 2.8 (PostgreSQL Compute, Memory, and Storage Sizing), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Cosmos DB and PostgreSQL vector documentation: https://learn.microsoft.com/en-us/azure/cosmos-db/

- **A:** Incorrect for this question. Index builds and large sorts spill to disk when work memory is too small, stretching maintenance windows and slowing queries. Why the correct answer wins: Index builds are I/O heavy, so storage throughput must support the build window.
- **B:** Incorrect for this question. A bounded pool amortizes connection setup and protects the server from connection storms. Pool size must match server limits. Why the correct answer wins: Index builds are I/O heavy, so storage throughput must support the build window.
- **C:** Incorrect for this question. Vector indexes are memory-hungry, so undersized compute causes swapping and slow queries. Right-size before tuning index parameters. Why the correct answer wins: Index builds are I/O heavy, so storage throughput must support the build window.
- **D:** Correct. Index creation and bulk loads are I/O heavy, and throttled storage stretches maintenance windows. Storage limits are separate from compute. In this case: Index builds are I/O heavy, so storage throughput must support the build window.

### Question 21 — B

Answer: Use prepared statements and batch round trips. Prepared statements reuse plans and reduce per-call overhead. Prepared statements avoid repeated planning and reduce chatty network calls. They pair well with pooling but can interact with pool modes. Local study-map skill 2.10 (PostgreSQL Connection Optimization), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Cosmos DB and PostgreSQL vector documentation: https://learn.microsoft.com/en-us/azure/cosmos-db/

- **A:** Incorrect for this question. A bounded pool amortizes connection setup and protects the server from connection storms. Pool size must match server limits. Why the correct answer wins: Prepared statements reuse plans and reduce per-call overhead.
- **B:** Correct. Prepared statements avoid repeated planning and reduce chatty network calls. They pair well with pooling but can interact with pool modes. In this case: Prepared statements reuse plans and reduce per-call overhead.
- **C:** Incorrect for this question. An external pooler multiplexes server connections for serverless or highly concurrent clients. Session-level features may be unavailable in transaction mode. Why the correct answer wins: Prepared statements reuse plans and reduce per-call overhead.
- **D:** Incorrect for this question. A replica offloads read traffic but introduces replication lag, which is dangerous for freshly written evidence. It does not reduce index memory pressure. Why the correct answer wins: Prepared statements reuse plans and reduce per-call overhead.

### Question 22 — C

Answer: Invalidate or overwrite the cache entry when the source changes. Explicit invalidation or overwrite on change removes the stale entry at the moment of the write. Write-through or explicit invalidation keeps cached answers consistent with the system of record. Without it, TTL is the only bound on staleness. Local study-map skill 2.11 (Azure Managed Redis Caching and Invalidation), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Cosmos DB and PostgreSQL vector documentation: https://learn.microsoft.com/en-us/azure/cosmos-db/

- **A:** Incorrect for this question. Flushing removes all cached content at once, causing a stampede to the origin and a latency cliff. Targeted invalidation is safer. Why the correct answer wins: Explicit invalidation or overwrite on change removes the stale entry at the moment of the write.
- **B:** Incorrect for this question. Eviction protects memory but evicts unpredictably, so a hot key can vanish before its freshness bound is reached. It is not a substitute for TTL design. Why the correct answer wins: Explicit invalidation or overwrite on change removes the stale entry at the moment of the write.
- **C:** Correct. Write-through or explicit invalidation keeps cached answers consistent with the system of record. Without it, TTL is the only bound on staleness. In this case: Explicit invalidation or overwrite on change removes the stale entry at the moment of the write.
- **D:** Incorrect for this question. A TTL bounds staleness and reclaims memory without a manual sweep. Too long a TTL hides source changes; too short wastes the cache. Why the correct answer wins: Explicit invalidation or overwrite on change removes the stale entry at the moment of the write.

### Question 23 — A

Answer: Create a vector index in Managed Redis for similarity search. A Redis vector index serves similarity from memory. Redis vector search serves low-latency similarity queries from memory. The corpus must fit the memory budget and be rebuilt on model change. Local study-map skill 2.12 (Azure Managed Redis Vector Indexing), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Cosmos DB and PostgreSQL vector documentation: https://learn.microsoft.com/en-us/azure/cosmos-db/

- **A:** Correct. Redis vector search serves low-latency similarity queries from memory. The corpus must fit the memory budget and be rebuilt on model change. In this case: A Redis vector index serves similarity from memory.
- **B:** Incorrect for this question. Session storage in Redis survives instance restarts and supports distributed instances. Sessions must be scoped and expiring. Why the correct answer wins: A Redis vector index serves similarity from memory.
- **C:** Incorrect for this question. A lock can serialize work across instances, but correctness under retries still needs idempotency keys in the data store. Locks expire and can be lost. Why the correct answer wins: A Redis vector index serves similarity from memory.
- **D:** Incorrect for this question. A cache absorbs repeated reads and cuts latency for hot data. Cache keys, TTLs, and invalidation must match the freshness requirement. Why the correct answer wins: A Redis vector index serves similarity from memory.

### Question 24 — B, E

Answers: Create an HNSW index for low-latency approximate search; Create an IVFFlat index to save memory on a large table. HNSW favors query speed with a larger memory footprint, while IVFFlat saves memory but needs rebuilds as data changes. HNSW gives fast approximate nearest-neighbour queries with a larger memory footprint and slower builds. Recall is tunable at query time. IVFFlat uses clustering lists and needs periodic rebuilds as data grows, but costs less memory than HNSW. Probes trade recall for speed. Local study-map skill 2.7 (pgvector Indexing and Query Latency), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Cosmos DB and PostgreSQL vector documentation: https://learn.microsoft.com/en-us/azure/cosmos-db/

- **A:** Incorrect for this question. An exact scan is accurate but scales linearly and burns compute. It is a baseline for measuring recall, not a production strategy. Why the correct answer wins: HNSW favors query speed with a larger memory footprint, while IVFFlat saves memory but needs rebuilds as data changes.
- **B:** Correct. IVFFlat uses clustering lists and needs periodic rebuilds as data grows, but costs less memory than HNSW. Probes trade recall for speed. In this case: HNSW favors query speed with a larger memory footprint, while IVFFlat saves memory but needs rebuilds as data changes.
- **C:** Incorrect for this question. Index creation and bulk loads are I/O heavy, and throttled storage stretches maintenance windows. Storage limits are separate from compute. Why the correct answer wins: HNSW favors query speed with a larger memory footprint, while IVFFlat saves memory but needs rebuilds as data changes.
- **D:** Incorrect for this question. Index builds and large sorts spill to disk when work memory is too small, stretching maintenance windows and slowing queries. Why the correct answer wins: HNSW favors query speed with a larger memory footprint, while IVFFlat saves memory but needs rebuilds as data changes.
- **E:** Correct. HNSW gives fast approximate nearest-neighbour queries with a larger memory footprint and slower builds. Recall is tunable at query time. In this case: HNSW favors query speed with a larger memory footprint, while IVFFlat saves memory but needs rebuilds as data changes.

### Question 25 — D

Answer: Create the container with a vector policy → upsert items with embeddings → query with VectorDistance → apply metadata filters. Policy and container precede writes; writes precede queries. The vector policy fixes dimensions and index type, so it must exist before vector writes and queries. Local study-map skill 2.5 (Cosmos DB Change Feed Processing), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Cosmos DB and PostgreSQL vector documentation: https://learn.microsoft.com/en-us/azure/cosmos-db/

- **A:** Incorrect for this question. Filtering and querying cannot precede the container and its vector data. Why the correct answer wins: Policy and container precede writes; writes precede queries.
- **B:** Incorrect for this question. Items cannot be written before the container exists with a matching vector policy. Why the correct answer wins: Policy and container precede writes; writes precede queries.
- **C:** Incorrect for this question. A similarity query needs indexed vectors, which require the container and its policy first. Why the correct answer wins: Policy and container precede writes; writes precede queries.
- **D:** Correct. The vector policy fixes dimensions and index type, so it must exist before vector writes and queries. In this case: Policy and container precede writes; writes precede queries.

### Question 26 — D

Answer: Use Service Bus sessions to keep related messages ordered. Sessions give ordered, exclusive processing per session ID. Sessions give ordered, exclusive processing per session ID across competing consumers. They require session-aware senders and receivers. Local study-map skill 3.1 (Service Bus Queues and Sessions), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure messaging and Functions documentation: https://learn.microsoft.com/en-us/azure/service-bus-messaging/

- **A:** Incorrect for this question. Topics fan out one message to independent subscribers, each with its own filter and dead-letter queue. Subscribers process at their own pace. Why the correct answer wins: Sessions give ordered, exclusive processing per session ID.
- **B:** Incorrect for this question. Peek-lock keeps the message locked until the handler completes it, giving at-least-once processing with retry. Lock duration must exceed processing time. Why the correct answer wins: Sessions give ordered, exclusive processing per session ID.
- **C:** Incorrect for this question. A queue decouples producers from a single consumer group and smooths bursts. Delivery semantics depend on receive mode and completion. Why the correct answer wins: Sessions give ordered, exclusive processing per session ID.
- **D:** Correct. Sessions give ordered, exclusive processing per session ID across competing consumers. They require session-aware senders and receivers. In this case: Sessions give ordered, exclusive processing per session ID.

### Question 27 — D

Answer: Publish to a Service Bus topic with multiple subscriptions. A topic with separate subscriptions fans the event out to independent consumers. Topics fan out one message to independent subscribers, each with its own filter and dead-letter queue. Subscribers process at their own pace. Local study-map skill 3.2 (Service Bus Topics, Subscriptions, and Filters), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure messaging and Functions documentation: https://learn.microsoft.com/en-us/azure/service-bus-messaging/

- **A:** Incorrect for this question. Queue Storage is simple and cheap for large backlogs with at-least-once delivery. It lacks topics, sessions, and scheduled messages. Why the correct answer wins: A topic with separate subscriptions fans the event out to independent consumers.
- **B:** Incorrect for this question. A custom schema fits domain events that are not resource lifecycle notifications. Consumers must version the schema contract. Why the correct answer wins: A topic with separate subscriptions fans the event out to independent consumers.
- **C:** Incorrect for this question. A queue decouples producers from a single consumer group and smooths bursts. Delivery semantics depend on receive mode and completion. Why the correct answer wins: A topic with separate subscriptions fans the event out to independent consumers.
- **D:** Correct. Topics fan out one message to independent subscribers, each with its own filter and dead-letter queue. Subscribers process at their own pace. In this case: A topic with separate subscriptions fans the event out to independent consumers.

### Question 28 — B

Answer: Enable duplicate detection on the queue. Duplicate detection drops repeated sends inside its time window. A duplicate-detection window drops repeated sends within the window, which helps with at-least-once producers. The window is time-bounded. Local study-map skill 3.3 (Service Bus Dead-Lettering and Retries), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure messaging and Functions documentation: https://learn.microsoft.com/en-us/azure/service-bus-messaging/

- **A:** Incorrect for this question. At-least-once delivery means duplicates will happen, so the write must tolerate replay. A stored key makes the retry safe. Why the correct answer wins: Duplicate detection drops repeated sends inside its time window.
- **B:** Correct. A duplicate-detection window drops repeated sends within the window, which helps with at-least-once producers. The window is time-bounded. In this case: Duplicate detection drops repeated sends inside its time window.
- **C:** Incorrect for this question. A delivery cap stops infinite retries of a failing message and moves it to the dead-letter queue. The cap must exceed legitimate transient retries. Why the correct answer wins: Duplicate detection drops repeated sends inside its time window.
- **D:** Incorrect for this question. Sessions give ordered, exclusive processing per session ID across competing consumers. They require session-aware senders and receivers. Why the correct answer wins: Duplicate detection drops repeated sends inside its time window.

### Question 29 — B

Answer: Deliver events by using a managed identity instead of a key. Identity-based delivery removes the stored key from the subscription. Identity-based delivery removes a shared key from the subscription. The receiver still validates the caller and payload. Local study-map skill 3.4 (Event Grid Filters, Custom Events, and Retries), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure messaging and Functions documentation: https://learn.microsoft.com/en-us/azure/service-bus-messaging/

- **A:** Incorrect for this question. Subject and event-type filters keep handlers focused and reduce cost. Filters are evaluated on event metadata, not payload body. Why the correct answer wins: Identity-based delivery removes the stored key from the subscription.
- **B:** Correct. Identity-based delivery removes a shared key from the subscription. The receiver still validates the caller and payload. In this case: Identity-based delivery removes the stored key from the subscription.
- **C:** Incorrect for this question. System topics carry Azure resource lifecycle events. Domain events that are not resource changes need a custom topic and schema. Why the correct answer wins: Identity-based delivery removes the stored key from the subscription.
- **D:** Incorrect for this question. Event Grid retries failed deliveries with backoff and can store undeliverable events. Handlers must still be idempotent. Why the correct answer wins: Identity-based delivery removes the stored key from the subscription.

### Question 30 — A

Answer: Orchestrate the multi-step workflow with Durable Functions. Durable Functions checkpoint state and support long timers across restarts. Durable Functions provides orchestrations, activities, timers, and retries with checkpointed state. Orchestrator code must stay deterministic. Local study-map skill 3.5 (Azure Functions Triggers and Bindings), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure messaging and Functions documentation: https://learn.microsoft.com/en-us/azure/service-bus-messaging/

- **A:** Correct. Durable Functions provides orchestrations, activities, timers, and retries with checkpointed state. Orchestrator code must stay deterministic. In this case: Durable Functions checkpoint state and support long timers across restarts.
- **B:** Incorrect for this question. A trigger starts the function when work arrives and handles the receive loop for you. Poison-message behavior is configured in host settings. Why the correct answer wins: Durable Functions checkpoint state and support long timers across restarts.
- **C:** Incorrect for this question. An HTTP trigger gives a synchronous API endpoint with route and authorization configuration. Long-running work should hand off to a queue. Why the correct answer wins: Durable Functions checkpoint state and support long timers across restarts.
- **D:** Incorrect for this question. HTTP requests have platform timeout limits, so long work belongs behind a queue or orchestration with a status endpoint. Why the correct answer wins: Durable Functions checkpoint state and support long timers across restarts.

### Question 31 — D

Answer: Move long-running work out of the HTTP request into a queue. Long work moves behind a queue or orchestration with a status endpoint. HTTP requests have platform timeout limits, so long work belongs behind a queue or orchestration with a status endpoint. Local study-map skill 3.6 (Function App Configuration and Deployment), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure messaging and Functions documentation: https://learn.microsoft.com/en-us/azure/service-bus-messaging/

- **A:** Incorrect for this question. A premium plan reduces cold starts and supports virtual network integration and longer timeouts. It costs more than consumption. Why the correct answer wins: Long work moves behind a queue or orchestration with a status endpoint.
- **B:** Incorrect for this question. An HTTP trigger gives a synchronous API endpoint with route and authorization configuration. Long-running work should hand off to a queue. Why the correct answer wins: Long work moves behind a queue or orchestration with a status endpoint.
- **C:** Incorrect for this question. Consumption bills per execution and scales automatically, with cold starts and a timeout ceiling. It fits spiky, short work. Why the correct answer wins: Long work moves behind a queue or orchestration with a status endpoint.
- **D:** Correct. HTTP requests have platform timeout limits, so long work belongs behind a queue or orchestration with a status endpoint. In this case: Long work moves behind a queue or orchestration with a status endpoint.

### Question 32 — B, C

Answers: Add a SQL or correlation filter to a subscription; Schedule the message for future enqueueing. A subscription filter limits delivery to high-value messages, and a scheduled message enqueues for a later time. Subscription filters route only matching messages to a handler, reducing wasted processing. Filter evaluation happens broker-side on message properties. A scheduled message becomes visible at a set time, which supports reminders and delayed retries. It is not a substitute for a durable timer. Local study-map skill 3.2 (Service Bus Topics, Subscriptions, and Filters), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure messaging and Functions documentation: https://learn.microsoft.com/en-us/azure/service-bus-messaging/

- **A:** Incorrect for this question. Dead-lettering preserves poison messages for diagnosis instead of losing them. Resubmission needs a fix and an idempotent handler. Why the correct answer wins: A subscription filter limits delivery to high-value messages, and a scheduled message enqueues for a later time.
- **B:** Correct. A scheduled message becomes visible at a set time, which supports reminders and delayed retries. It is not a substitute for a durable timer. In this case: A subscription filter limits delivery to high-value messages, and a scheduled message enqueues for a later time.
- **C:** Correct. Subscription filters route only matching messages to a handler, reducing wasted processing. Filter evaluation happens broker-side on message properties. In this case: A subscription filter limits delivery to high-value messages, and a scheduled message enqueues for a later time.
- **D:** Incorrect for this question. Sessions give ordered, exclusive processing per session ID across competing consumers. They require session-aware senders and receivers. Why the correct answer wins: A subscription filter limits delivery to high-value messages, and a scheduled message enqueues for a later time.
- **E:** Incorrect for this question. A duplicate-detection window drops repeated sends within the window, which helps with at-least-once producers. The window is time-bounded. Why the correct answer wins: A subscription filter limits delivery to high-value messages, and a scheduled message enqueues for a later time.

### Question 33 — C, E

Answers: Inspect the dead-letter queue and resubmit corrected messages; Set a maximum delivery count and handle the dead-letter path. Dead-lettering preserves the message, and a delivery cap stops the loop. Dead-lettering preserves poison messages for diagnosis instead of losing them. Resubmission needs a fix and an idempotent handler. A delivery cap stops infinite retries of a failing message and moves it to the dead-letter queue. The cap must exceed legitimate transient retries. Local study-map skill 3.3 (Service Bus Dead-Lettering and Retries), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure messaging and Functions documentation: https://learn.microsoft.com/en-us/azure/service-bus-messaging/

- **A:** Incorrect for this question. A duplicate-detection window drops repeated sends within the window, which helps with at-least-once producers. The window is time-bounded. Why the correct answer wins: Dead-lettering preserves the message, and a delivery cap stops the loop.
- **B:** Incorrect for this question. Receive-and-delete removes the message on delivery, so a crash loses work silently. It suits telemetry, not payments. Why the correct answer wins: Dead-lettering preserves the message, and a delivery cap stops the loop.
- **C:** Correct. A delivery cap stops infinite retries of a failing message and moves it to the dead-letter queue. The cap must exceed legitimate transient retries. In this case: Dead-lettering preserves the message, and a delivery cap stops the loop.
- **D:** Incorrect for this question. Sessions give ordered, exclusive processing per session ID across competing consumers. They require session-aware senders and receivers. Why the correct answer wins: Dead-lettering preserves the message, and a delivery cap stops the loop.
- **E:** Correct. Dead-lettering preserves poison messages for diagnosis instead of losing them. Resubmission needs a fix and an idempotent handler. In this case: Dead-lettering preserves the message, and a delivery cap stops the loop.

### Question 34 — C

Answer: Publish a custom event → evaluate the subscription filter → deliver to the handler → retry on failure → dead-letter undeliverable events. Publish, filter, deliver, retry, then dead-letter. Filtering happens before delivery, retries handle transient failures, and dead-lettering preserves what cannot be delivered. Local study-map skill 3.4 (Event Grid Filters, Custom Events, and Retries), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure messaging and Functions documentation: https://learn.microsoft.com/en-us/azure/service-bus-messaging/

- **A:** Incorrect for this question. Delivery cannot precede publication and filtering. Why the correct answer wins: Publish, filter, deliver, retry, then dead-letter.
- **B:** Incorrect for this question. A filter is evaluated before delivery, and retries must occur before dead-lettering. Why the correct answer wins: Publish, filter, deliver, retry, then dead-letter.
- **C:** Correct. Filtering happens before delivery, retries handle transient failures, and dead-lettering preserves what cannot be delivered. In this case: Publish, filter, deliver, retry, then dead-letter.
- **D:** Incorrect for this question. A filter cannot evaluate an event that has not been published. Why the correct answer wins: Publish, filter, deliver, retry, then dead-letter.

### Question 35 — C

Answer: Store the secret in Azure Key Vault and read it at runtime. Key Vault provides audited, access-controlled storage. A vault centralizes secret storage with access control and audit. Retrieval should use an identity, not a copied credential. Local study-map skill 4.1 (Key Vault Secret Storage, Rotation, and Retrieval), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Key Vault, App Configuration, and Monitor documentation: https://learn.microsoft.com/en-us/azure/azure-monitor/

- **A:** Incorrect for this question. App Configuration separates configuration from code and supports labels, feature flags, and Key Vault references. Change still needs a refresh strategy. Why the correct answer wins: Key Vault provides audited, access-controlled storage.
- **B:** Incorrect for this question. Application settings become environment variables for the container and can be swapped per slot. Sensitive values should still reference a vault. Why the correct answer wins: Key Vault provides audited, access-controlled storage.
- **C:** Correct. A vault centralizes secret storage with access control and audit. Retrieval should use an identity, not a copied credential. In this case: Key Vault provides audited, access-controlled storage.
- **D:** Incorrect for this question. Pinning a version makes a rotation invisible to the app until it is redeployed, which is useful for break-glass and dangerous for routine rotation. Why the correct answer wins: Key Vault provides audited, access-controlled storage.

### Question 36 — C

Answer: Reference the Key Vault secret from an App Configuration key value. A Key Vault reference inside the configuration key keeps the secret out of the store. A Key Vault reference keeps non-secret settings in App Configuration while the value stays in the vault. The app identity needs both sets of permissions. Local study-map skill 4.2 (App Configuration Settings and Feature Flags), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Key Vault, App Configuration, and Monitor documentation: https://learn.microsoft.com/en-us/azure/azure-monitor/

- **A:** Incorrect for this question. A vault centralizes secret storage with access control and audit. Retrieval should use an identity, not a copied credential. Why the correct answer wins: A Key Vault reference inside the configuration key keeps the secret out of the store.
- **B:** Incorrect for this question. Application settings become environment variables for the container and can be swapped per slot. Sensitive values should still reference a vault. Why the correct answer wins: A Key Vault reference inside the configuration key keeps the secret out of the store.
- **C:** Correct. A Key Vault reference keeps non-secret settings in App Configuration while the value stays in the vault. The app identity needs both sets of permissions. In this case: A Key Vault reference inside the configuration key keeps the secret out of the store.
- **D:** Incorrect for this question. App Configuration separates configuration from code and supports labels, feature flags, and Key Vault references. Change still needs a refresh strategy. Why the correct answer wins: A Key Vault reference inside the configuration key keeps the secret out of the store.

### Question 37 — C

Answer: Use App Configuration labels to separate environments. Labels separate environment values under one key schema. Labels keep dev, test, and prod values in one store with one key schema. A misconfigured label selector silently serves the wrong values. Local study-map skill 4.2 (App Configuration Settings and Feature Flags), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Key Vault, App Configuration, and Monitor documentation: https://learn.microsoft.com/en-us/azure/azure-monitor/

- **A:** Incorrect for this question. Sentinel-key or polling refresh lets a running app pick up new settings. Refresh intervals trade responsiveness against request volume. Why the correct answer wins: Labels separate environment values under one key schema.
- **B:** Incorrect for this question. App Configuration separates configuration from code and supports labels, feature flags, and Key Vault references. Change still needs a refresh strategy. Why the correct answer wins: Labels separate environment values under one key schema.
- **C:** Correct. Labels keep dev, test, and prod values in one store with one key schema. A misconfigured label selector silently serves the wrong values. In this case: Labels separate environment values under one key schema.
- **D:** Incorrect for this question. Pinning a version makes a rotation invisible to the app until it is redeployed, which is useful for break-glass and dangerous for routine rotation. Why the correct answer wins: Labels separate environment values under one key schema.

### Question 38 — C

Answer: Use head or tail sampling so trace volume stays within budget. Tail sampling keeps error traces while reducing routine volume. Sampling keeps telemetry cost bounded, but aggressive sampling can hide rare failures. Tail sampling can retain errors preferentially. Local study-map skill 4.3 (Distributed Tracing with OpenTelemetry), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Key Vault, App Configuration, and Monitor documentation: https://learn.microsoft.com/en-us/azure/azure-monitor/

- **A:** Incorrect for this question. OpenTelemetry emits vendor-neutral traces, metrics, and logs with context propagation. Exporters and sampling decide what reaches the backend. Why the correct answer wins: Tail sampling keeps error traces while reducing routine volume.
- **B:** Incorrect for this question. A collector batches, filters, and routes telemetry, and decouples app configuration from the backend. It is another component to run and monitor. Why the correct answer wins: Tail sampling keeps error traces while reducing routine volume.
- **C:** Correct. Sampling keeps telemetry cost bounded, but aggressive sampling can hide rare failures. Tail sampling can retain errors preferentially. In this case: Tail sampling keeps error traces while reducing routine volume.
- **D:** Incorrect for this question. Propagation stitches one trace across HTTP, messaging, and Functions so the whole path is visible. Missing propagation breaks the trace at that hop. Why the correct answer wins: Tail sampling keeps error traces while reducing routine volume.

### Question 39 — A

Answer: Store repeated aggregations in a materialized view or update policy. Materializing the aggregation avoids recomputation on every refresh. Precomputed results avoid recomputing expensive aggregations on every dashboard refresh. The trade-off is storage and freshness lag. Local study-map skill 4.4 (KQL Queries for Logs and Metrics), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Key Vault, App Configuration, and Monitor documentation: https://learn.microsoft.com/en-us/azure/azure-monitor/

- **A:** Correct. Precomputed results avoid recomputing expensive aggregations on every dashboard refresh. The trade-off is storage and freshness lag. In this case: Materializing the aggregation avoids recomputation on every refresh.
- **B:** Incorrect for this question. Reducing columns and rows early lowers query cost and latency. Broad queries over long ranges are the usual cause of slow KQL. Why the correct answer wins: Materializing the aggregation avoids recomputation on every refresh.
- **C:** Incorrect for this question. Joining request and dependency telemetry shows which downstream call fails inside a slow request. Cross-workspace joins need the right scope. Why the correct answer wins: Materializing the aggregation avoids recomputation on every refresh.
- **D:** Incorrect for this question. Time-binned aggregation reveals the shape of an incident: a step change, a ramp, or a periodic spike. Averages alone hide short outages. Why the correct answer wins: Materializing the aggregation avoids recomputation on every refresh.

### Question 40 — A

Answer: Reach the data service through a private endpoint. A private endpoint with public access disabled keeps traffic inside the network. A private endpoint keeps traffic on the virtual network and removes public exposure. DNS resolution must be wired to the private zone. Local study-map skill 4.5 (Identity-Based Access for Application Services), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Key Vault, App Configuration, and Monitor documentation: https://learn.microsoft.com/en-us/azure/azure-monitor/

- **A:** Correct. A private endpoint keeps traffic on the virtual network and removes public exposure. DNS resolution must be wired to the private zone. In this case: A private endpoint with public access disabled keeps traffic inside the network.
- **B:** Incorrect for this question. A managed identity issues tokens from the platform, removing secret distribution from the app. Role assignment still scopes what it can reach. Why the correct answer wins: A private endpoint with public access disabled keeps traffic inside the network.
- **C:** Incorrect for this question. A private endpoint needs matching name resolution or clients still resolve the public address. The zone must be linked to the workload network. Why the correct answer wins: A private endpoint with public access disabled keeps traffic inside the network.
- **D:** Incorrect for this question. A scoped role grants only the operations the app performs and limits blast radius. Prefer built-in roles over broad contributor grants. Why the correct answer wins: A private endpoint with public access disabled keeps traffic inside the network.

### Question 41 — A, D

Answers: Federate a Kubernetes service account to a managed identity; Assign a least-privilege role to the application identity. Workload identity federation removes stored credentials, and a narrow role limits what the pod can do. Workload identity lets pods obtain tokens without stored secrets. Each workload should get its own identity and narrow role. A scoped role grants only the operations the app performs and limits blast radius. Prefer built-in roles over broad contributor grants. Local study-map skill 4.5 (Identity-Based Access for Application Services), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Key Vault, App Configuration, and Monitor documentation: https://learn.microsoft.com/en-us/azure/azure-monitor/

- **A:** Correct. Workload identity lets pods obtain tokens without stored secrets. Each workload should get its own identity and narrow role. In this case: Workload identity federation removes stored credentials, and a narrow role limits what the pod can do.
- **B:** Incorrect for this question. A private endpoint keeps traffic on the virtual network and removes public exposure. DNS resolution must be wired to the private zone. Why the correct answer wins: Workload identity federation removes stored credentials, and a narrow role limits what the pod can do.
- **C:** Incorrect for this question. Platform metrics are cheap and near-real-time, so they suit latency and failure-rate alerts. Log-based alerts add latency and query cost. Why the correct answer wins: Workload identity federation removes stored credentials, and a narrow role limits what the pod can do.
- **D:** Correct. A scoped role grants only the operations the app performs and limits blast radius. Prefer built-in roles over broad contributor grants. In this case: Workload identity federation removes stored credentials, and a narrow role limits what the pod can do.
- **E:** Incorrect for this question. A vault centralizes secret storage with access control and audit. Retrieval should use an identity, not a copied credential. Why the correct answer wins: Workload identity federation removes stored credentials, and a narrow role limits what the pod can do.

### Question 42 — B, E

Answers: Store the secret in Azure Key Vault and read it at runtime; Grant the app identity data-plane access to the vault. Store the secret in the vault, then grant the identity data-plane access. A vault centralizes secret storage with access control and audit. Retrieval should use an identity, not a copied credential. Vault access is a separate authorization decision from the app identity. Without a data-plane role or policy the reference fails at runtime. Local study-map skill 4.1 (Key Vault Secret Storage, Rotation, and Retrieval), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Key Vault, App Configuration, and Monitor documentation: https://learn.microsoft.com/en-us/azure/azure-monitor/

- **A:** Incorrect for this question. Labels keep dev, test, and prod values in one store with one key schema. A misconfigured label selector silently serves the wrong values. Why the correct answer wins: Store the secret in the vault, then grant the identity data-plane access.
- **B:** Correct. Vault access is a separate authorization decision from the app identity. Without a data-plane role or policy the reference fails at runtime. In this case: Store the secret in the vault, then grant the identity data-plane access.
- **C:** Incorrect for this question. App Configuration separates configuration from code and supports labels, feature flags, and Key Vault references. Change still needs a refresh strategy. Why the correct answer wins: Store the secret in the vault, then grant the identity data-plane access.
- **D:** Incorrect for this question. Pinning a version makes a rotation invisible to the app until it is redeployed, which is useful for break-glass and dangerous for routine rotation. Why the correct answer wins: Store the secret in the vault, then grant the identity data-plane access.
- **E:** Correct. A vault centralizes secret storage with access control and audit. Retrieval should use an identity, not a copied credential. In this case: Store the secret in the vault, then grant the identity data-plane access.

### Question 43 — B

Answer: Store the secret in Key Vault → grant the app identity access → reference the secret from the app → rotate the secret → the app reads the new version. Store, grant, reference, rotate, then read the current version. Access must be granted before the reference resolves, and the app must read the current version after rotation. Local study-map skill 4.3 (Distributed Tracing with OpenTelemetry), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Key Vault, App Configuration, and Monitor documentation: https://learn.microsoft.com/en-us/azure/azure-monitor/

- **A:** Incorrect for this question. Access can be granted first, but rotation cannot precede storing the secret. Why the correct answer wins: Store, grant, reference, rotate, then read the current version.
- **B:** Correct. Access must be granted before the reference resolves, and the app must read the current version after rotation. In this case: Store, grant, reference, rotate, then read the current version.
- **C:** Incorrect for this question. A reference cannot resolve before the secret and the access grant exist. Why the correct answer wins: Store, grant, reference, rotate, then read the current version.
- **D:** Incorrect for this question. There is nothing to rotate or reference before the secret is stored. Why the correct answer wins: Store, grant, reference, rotate, then read the current version.

### Question 44 — B, E

Answers: Use Service Bus sessions to keep related messages ordered; Receive with peek-lock and complete or abandon explicitly. Sessions keep per-card ordering, and peek-lock lets an uncompleted message return to the queue. Sessions give ordered, exclusive processing per session ID across competing consumers. They require session-aware senders and receivers. Peek-lock keeps the message locked until the handler completes it, giving at-least-once processing with retry. Lock duration must exceed processing time. Local study-map skill 3.1 (Service Bus Queues and Sessions), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure messaging and Functions documentation: https://learn.microsoft.com/en-us/azure/service-bus-messaging/

- **A:** Incorrect for this question. Receive-and-delete removes the message on delivery, so a crash loses work silently. It suits telemetry, not payments. Why the correct answer wins: Sessions keep per-card ordering, and peek-lock lets an uncompleted message return to the queue.
- **B:** Correct. Sessions give ordered, exclusive processing per session ID across competing consumers. They require session-aware senders and receivers. In this case: Sessions keep per-card ordering, and peek-lock lets an uncompleted message return to the queue.
- **C:** Incorrect for this question. A duplicate-detection window drops repeated sends within the window, which helps with at-least-once producers. The window is time-bounded. Why the correct answer wins: Sessions keep per-card ordering, and peek-lock lets an uncompleted message return to the queue.
- **D:** Incorrect for this question. Subscription filters route only matching messages to a handler, reducing wasted processing. Filter evaluation happens broker-side on message properties. Why the correct answer wins: Sessions keep per-card ordering, and peek-lock lets an uncompleted message return to the queue.
- **E:** Correct. Peek-lock keeps the message locked until the handler completes it, giving at-least-once processing with retry. Lock duration must exceed processing time. In this case: Sessions keep per-card ordering, and peek-lock lets an uncompleted message return to the queue.

### Question 45 — A

Answer: Filter on metadata columns in the same query as the vector search. Filtering inside the vector query keeps scope and result completeness together. Combining a WHERE filter with the distance operator keeps retrieval inside the caller's scope and improves relevance. Index the filter columns too. Local study-map skill 2.9 (PostgreSQL RAG with Metadata Filters), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Cosmos DB and PostgreSQL vector documentation: https://learn.microsoft.com/en-us/azure/cosmos-db/

- **A:** Correct. Combining a WHERE filter with the distance operator keeps retrieval inside the caller's scope and improves relevance. Index the filter columns too. In this case: Filtering inside the vector query keeps scope and result completeness together.
- **B:** Incorrect for this question. HNSW gives fast approximate nearest-neighbour queries with a larger memory footprint and slower builds. Recall is tunable at query time. Why the correct answer wins: Filtering inside the vector query keeps scope and result completeness together.
- **C:** Incorrect for this question. Post-filtering can return fewer results than requested and can leak existence or counts if the filtering is careless. Push authorization into the query. Why the correct answer wins: Filtering inside the vector query keeps scope and result completeness together.
- **D:** Incorrect for this question. An exact scan is accurate but scales linearly and burns compute. It is a baseline for measuring recall, not a production strategy. Why the correct answer wins: Filtering inside the vector query keeps scope and result completeness together.

### Question 46 — B

Answer: Define a custom event schema for the topic. A custom topic with a domain event schema carries the notification. A custom schema fits domain events that are not resource lifecycle notifications. Consumers must version the schema contract. Local study-map skill 3.4 (Event Grid Filters, Custom Events, and Retries), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure messaging and Functions documentation: https://learn.microsoft.com/en-us/azure/service-bus-messaging/

- **A:** Incorrect for this question. Event Grid retries failed deliveries with backoff and can store undeliverable events. Handlers must still be idempotent. Why the correct answer wins: A custom topic with a domain event schema carries the notification.
- **B:** Correct. A custom schema fits domain events that are not resource lifecycle notifications. Consumers must version the schema contract. In this case: A custom topic with a domain event schema carries the notification.
- **C:** Incorrect for this question. Subject and event-type filters keep handlers focused and reduce cost. Filters are evaluated on event metadata, not payload body. Why the correct answer wins: A custom topic with a domain event schema carries the notification.
- **D:** Incorrect for this question. System topics carry Azure resource lifecycle events. Domain events that are not resource changes need a custom topic and schema. Why the correct answer wins: A custom topic with a domain event schema carries the notification.

### Question 47 — A

Answer: Rotate the secret on a schedule and let apps resolve the current version. Rotate to a new version, update the source, and let the app read the current version. Rotation limits the value of a leaked secret, but callers must read the latest version rather than caching an old one forever. Local study-map skill 4.1 (Key Vault Secret Storage, Rotation, and Retrieval), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Key Vault, App Configuration, and Monitor documentation: https://learn.microsoft.com/en-us/azure/azure-monitor/

- **A:** Correct. Rotation limits the value of a leaked secret, but callers must read the latest version rather than caching an old one forever. In this case: Rotate to a new version, update the source, and let the app read the current version.
- **B:** Incorrect for this question. Soft delete and purge protection stop accidental or malicious permanent loss of secrets. They also constrain how names can be reused. Why the correct answer wins: Rotate to a new version, update the source, and let the app read the current version.
- **C:** Incorrect for this question. Pinning a version makes a rotation invisible to the app until it is redeployed, which is useful for break-glass and dangerous for routine rotation. Why the correct answer wins: Rotate to a new version, update the source, and let the app read the current version.
- **D:** Incorrect for this question. A managed identity issues tokens from the platform, removing secret distribution from the app. Role assignment still scopes what it can reach. Why the correct answer wins: Rotate to a new version, update the source, and let the app read the current version.

### Question 48 — C

Answer: Test end-to-end connectivity from inside the container to each dependency. Testing from inside the container proves DNS, network rules, and egress paths the host test never exercised. Reaching a dependency from the pod or replica proves DNS, egress, and firewall paths together. Host-side tests can succeed while the container path fails. Local study-map skill 1.7 (Container Logs, Events, and Connectivity), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure container hosting documentation: https://learn.microsoft.com/en-us/azure/container-apps/

- **A:** Incorrect for this question. Readiness gates traffic until the app can serve it, and liveness restarts a wedged container. Wrong thresholds cause restart loops. Why the correct answer wins: Testing from inside the container proves DNS, network rules, and egress paths the host test never exercised.
- **B:** Incorrect for this question. Platform logs and metrics must be routed before they can be queried or alerted on. Retention and cost follow the workspace settings. Why the correct answer wins: Testing from inside the container proves DNS, network rules, and egress paths the host test never exercised.
- **C:** Correct. Reaching a dependency from the pod or replica proves DNS, egress, and firewall paths together. Host-side tests can succeed while the container path fails. In this case: Testing from inside the container proves DNS, network rules, and egress paths the host test never exercised.
- **D:** Incorrect for this question. Container Apps and AKS surface stdout logs and platform events into a workspace for KQL analysis. Verbosity and retention cost money. Why the correct answer wins: Testing from inside the container proves DNS, network rules, and egress paths the host test never exercised.

### Question 49 — C

Answer: Set a maximum delivery count and handle the dead-letter path. A maximum delivery count dead-letters the message after bounded attempts. A delivery cap stops infinite retries of a failing message and moves it to the dead-letter queue. The cap must exceed legitimate transient retries. Local study-map skill 3.3 (Service Bus Dead-Lettering and Retries), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure messaging and Functions documentation: https://learn.microsoft.com/en-us/azure/service-bus-messaging/

- **A:** Incorrect for this question. Receive-and-delete removes the message on delivery, so a crash loses work silently. It suits telemetry, not payments. Why the correct answer wins: A maximum delivery count dead-letters the message after bounded attempts.
- **B:** Incorrect for this question. A duplicate-detection window drops repeated sends within the window, which helps with at-least-once producers. The window is time-bounded. Why the correct answer wins: A maximum delivery count dead-letters the message after bounded attempts.
- **C:** Correct. A delivery cap stops infinite retries of a failing message and moves it to the dead-letter queue. The cap must exceed legitimate transient retries. In this case: A maximum delivery count dead-letters the message after bounded attempts.
- **D:** Incorrect for this question. Peek-lock keeps the message locked until the handler completes it, giving at-least-once processing with retry. Lock duration must exceed processing time. Why the correct answer wins: A maximum delivery count dead-letters the message after bounded attempts.

### Question 50 — B

Answer: Alert on platform metrics rather than only on log queries. Platform metric alerts are cheap and near-real-time for rate and latency thresholds. Platform metrics are cheap and near-real-time, so they suit latency and failure-rate alerts. Log-based alerts add latency and query cost. Local study-map skill 4.4 (KQL Queries for Logs and Metrics), mapped to the official guide: Microsoft AI-200 study guide, skills measured as of October 7, 2026 Primary reference: Azure Key Vault, App Configuration, and Monitor documentation: https://learn.microsoft.com/en-us/azure/azure-monitor/

- **A:** Incorrect for this question. An alert turns a threshold breach into a notification or action. Thresholds need a baseline, or the alert is noise. Why the correct answer wins: Platform metric alerts are cheap and near-real-time for rate and latency thresholds.
- **B:** Correct. Platform metrics are cheap and near-real-time, so they suit latency and failure-rate alerts. Log-based alerts add latency and query cost. In this case: Platform metric alerts are cheap and near-real-time for rate and latency thresholds.
- **C:** Incorrect for this question. Time-binned aggregation reveals the shape of an incident: a step change, a ramp, or a periodic spike. Averages alone hide short outages. Why the correct answer wins: Platform metric alerts are cheap and near-real-time for rate and latency thresholds.
- **D:** Incorrect for this question. Reducing columns and rows early lowers query cost and latency. Broad queries over long ranges are the usual cause of slow KQL. Why the correct answer wins: Platform metric alerts are cheap and near-real-time for rate and latency thresholds.
