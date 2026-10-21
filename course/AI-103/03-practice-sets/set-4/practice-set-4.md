# Microsoft AI-103 — Full-Length Mock Exam 4

Azure AI Apps and Agents Developer Associate · 50 questions · 120 minutes · passing target 700/1000

Blueprint-weighted mock exam. Item mix: 38 single-choice, 8 multi-select (selection count stated), 4 ordering items rendered as answer choices, and 2 case studies of 3 questions. Hot-area, drag-and-drop UI, labs, and adaptive problem-solution sets cannot be reproduced in a CSV; see the README for the exact fidelity boundary.

Original educational content, not actual, recalled, or copied Microsoft exam items.

## Questions

### 1. A plant wants a vision-capable model available in the same region as its factory data. What should the architects confirm first?

Domain: Plan and manage an Azure AI solution

- A. Compare supported models in the Foundry model catalog
- B. Use a general-purpose large language model for complex reasoning
- C. Train or deploy a task-specific model outside the prebuilt catalog
- D. Use a small language model for a narrow, high-volume task

### 2. Technicians upload a photo of a wiring harness together with a text question. Which model capability handles one request with both inputs?

Domain: Plan and manage an Azure AI solution

- A. Use Foundry Tools for prebuilt vision, speech, language, and extraction needs
- B. Use a multimodal model for combined text, image, or audio input
- C. Train or deploy a task-specific model outside the prebuilt catalog
- D. Use a small language model for a narrow, high-volume task

### 3. A maintenance agent must query the enterprise asset system for the next service date. Which capability performs that lookup?

Domain: Plan and manage an Azure AI solution

- A. Expose an OpenAPI operation as an agent tool
- B. Use managed conversation state or memory for continuity
- C. Expose a typed function as an agent tool
- D. Connect an Azure AI Search index as agent knowledge

### 4. A shift-handover assistant must remember the machines already discussed in the current session. What should be used?

Domain: Plan and manage an Azure AI solution

- A. Use an Azure AI Search indexer to pull source content
- B. Expose a typed function as an agent tool
- C. Use managed conversation state or memory for continuity
- D. Use a vector index for semantic retrieval

### 5. A manufacturer must release the same inspection assistant to three plants reproducibly. Which sequence should the team follow?

Domain: Plan and manage an Azure AI solution

- A. Deploy model → promote → provision resources → evaluate → configure app
- B. Provision resources → deploy model → configure app connection → evaluate → promote
- C. Configure app → provision resources → deploy model → promote → evaluate
- D. Evaluate → provision resources → promote → deploy model → configure app

### 6. Production telemetry must not reach the model endpoint across the public internet. What should be configured?

Domain: Plan and manage an Azure AI solution

- A. Track cost per accepted task, not only per token
- B. Use private endpoints and disable public network access
- C. Plan for model quota expressed in tokens and requests per minute
- D. Manage AI resources with infrastructure as code and CI/CD

### 7. Line-side tablets receive throttling errors at shift change when hundreds of scans start together. What should be adjusted?

Domain: Plan and manage an Azure AI solution

- A. Track cost per accepted task, not only per token
- B. Use provisioned throughput for predictable high-volume workloads
- C. Plan for model quota expressed in tokens and requests per minute
- D. Monitor input and quality drift over time

### 8. Monthly spend grows faster than usage because long manuals are re-sent for every question. Which optimization applies first?

Domain: Plan and manage an Azure AI solution

- A. Plan for model quota expressed in tokens and requests per minute
- B. Track prompt, completion, and cached token usage
- C. Use supported prompt or response caching where appropriate
- D. Track cost per accepted task, not only per token

### 9. Operations needs a single dashboard of model latency, error rate, and refusal rate. What should be enabled?

Domain: Plan and manage an Azure AI solution

- A. Use Azure Monitor and Application Insights for telemetry
- B. Alert on latency, error rate, safety, and cost thresholds
- C. Monitor input and quality drift over time
- D. Preserve audit logs of changes, approvals, and tool actions

### 10. Quality degrades as new equipment is photographed, and engineers must learn quickly. Which two capabilities are needed? Select two.

Domain: Plan and manage an Azure AI solution

- A. Monitor input and quality drift over time
- B. Alert on latency, error rate, safety, and cost thresholds
- C. Track cost per accepted task, not only per token
- D. Plan for model quota expressed in tokens and requests per minute
- E. Use supported prompt or response caching where appropriate

### 11. A plant app must call Foundry without stored secrets and with only read access to one index. Which two actions should you take? Select two.

Domain: Plan and manage an Azure AI solution

- A. Store secrets in Azure Key Vault when keys are unavoidable
- B. Use least-privilege Azure RBAC roles for the workload identity
- C. Use private endpoints and disable public network access
- D. Configure content safety filters for harmful categories
- E. Authenticate with a managed identity instead of keys

### 12. A safety assistant must never propose bypassing a lockout procedure, even if asked directly. Which control applies?

Domain: Plan and manage an Azure AI solution

- A. Enforce constraints in code and platform policy
- B. Require human approval before consequential actions
- C. Set agent oversight mode and tool-access constraints
- D. Preserve audit logs of changes, approvals, and tool actions

### 13. A code assistant reproduces a licensed vendor routine verbatim in suggestions. Which control addresses this?

Domain: Plan and manage an Azure AI solution

- A. Enforce brand and usage rules for generated visuals
- B. Apply watermarks or provenance markers to generated media
- C. Configure content safety filters for harmful categories
- D. Detect protected or copyrighted material in output

### 14. A maintenance assistant must answer from the current approved service bulletins and cite them. Which approach fits?

Domain: Implement generative AI and agentic solutions

- A. Translate every request before retrieval
- B. Ground responses with retrieval-augmented generation
- C. Design multistep workflows with explicit checkpoints
- D. Route requests to different models by task difficulty

### 15. A work-order system needs fixed fields and types from each technician note. What should the model produce?

Domain: Implement generative AI and agentic solutions

- A. Design multistep workflows with explicit checkpoints
- B. Use a versioned prompt template with explicit variables
- C. Use supported prompt or response caching where appropriate
- D. Return a defined JSON schema for downstream systems

### 16. A quality workflow must read a gauge photo, check the reading against limits, then file a deviation. What should the design use?

Domain: Implement generative AI and agentic solutions

- A. Design multistep workflows with explicit checkpoints
- B. Route requests to different models by task difficulty
- C. Limit autonomy with scope, budget, and stop conditions
- D. One model call with no external retrieval or tool use

### 17. A .NET service needs supported authentication and retry handling for Foundry calls. What should it use?

Domain: Implement generative AI and agentic solutions

- A. Use batch processing for latency-tolerant bulk work
- B. Create and run deployments by hand in the portal
- C. Use a Foundry SDK or supported connector from application code
- D. Manage AI resources with infrastructure as code and CI/CD

### 18. An application must call only the deployments approved for one Foundry project. What should it be configured with?

Domain: Implement generative AI and agentic solutions

- A. Use an Azure AI Search indexer to pull source content
- B. Store secrets in Azure Key Vault when keys are unavoidable
- C. Connect the application to the Foundry project endpoint
- D. Compare supported models in the Foundry model catalog

### 19. A team must keep a stable accuracy benchmark and ensure no earlier defect case regresses. Which two practices are required? Select two.

Domain: Implement generative AI and agentic solutions

- A. Build a representative golden dataset from real tasks
- B. Re-run evaluation suites after meaningful changes
- C. Use provisioned throughput for predictable high-volume workloads
- D. Lower temperature for more deterministic extraction
- E. Apply watermarks or provenance markers to generated media

### 20. Two prompt variants must be scored on the same labelled inspection cases before release. What should be run?

Domain: Implement generative AI and agentic solutions

- A. Use evaluators for quality, safety, and groundedness
- B. Alert on latency, error rate, safety, and cost thresholds
- C. Preserve audit logs of changes, approvals, and tool actions
- D. Use Azure Monitor and Application Insights for telemetry

### 21. An agent sends a machine identifier in the wrong format to a scheduling tool. What should be tightened first?

Domain: Implement generative AI and agentic solutions

- A. Define narrow tool schemas with clear descriptions
- B. Put stable behavior rules in the system message
- C. Use managed conversation state or memory for continuity
- D. Use a versioned prompt template with explicit variables

### 22. A shift agent must keep a consistent role and remember the line under discussion. Which two components provide that? Select two.

Domain: Implement generative AI and agentic solutions

- A. Put stable behavior rules in the system message
- B. Use managed conversation state or memory for continuity
- C. Expose an OpenAPI operation as an agent tool
- D. Define narrow tool schemas with clear descriptions
- E. Ground responses with retrieval-augmented generation

### 23. A warehouse agent must call an inventory service that already publishes an OpenAPI contract. Which tool type fits?

Domain: Implement generative AI and agentic solutions

- A. Use managed conversation state or memory for continuity
- B. Expose an OpenAPI operation as an agent tool
- C. Expose a typed function as an agent tool
- D. Ground responses with retrieval-augmented generation

### 24. A deviation must be classified, then escalated, then documented in that fixed order. Which pattern fits?

Domain: Implement generative AI and agentic solutions

- A. Run independent agents concurrently
- B. Use a manager agent to coordinate specialists
- C. Use self-critique or reflection to improve drafts
- D. Run agents in a fixed sequence

### 25. A coordinator must choose among maintenance, quality, and logistics specialists and merge their answers. Which pattern fits?

Domain: Implement generative AI and agentic solutions

- A. Transfer control between agents with explicit context
- B. Use a manager agent to coordinate specialists
- C. Run independent agents concurrently
- D. Use self-critique or reflection to improve drafts

### 26. Which sequence correctly handles an alert about failing defect detection?

Domain: Implement generative AI and agentic solutions

- A. Isolate the failing step → apply fix → detect alert → verify with regression evaluation → inspect traces
- B. Verify with regression evaluation → apply fix → detect alert → isolate the failing step → inspect traces
- C. Detect alert → inspect traces → isolate the failing step → apply fix → verify with regression evaluation
- D. Apply fix → detect alert → inspect traces → isolate the failing step → verify with regression evaluation

### 27. Single-field extraction returns different values on identical repeat requests. Which setting should be lowered first?

Domain: Implement generative AI and agentic solutions

- A. Use supported prompt or response caching where appropriate
- B. Route requests to different models by task difficulty
- C. Adjust top-p to control response diversity
- D. Lower temperature for more deterministic extraction

### 28. A training team needs an original diagram of a safe lockout procedure. Which capability applies?

Domain: Implement computer vision solutions

- A. Generate alt text aligned to accessibility guidance
- B. Edit a region of an image with a mask
- C. Generate video from text or reference media
- D. Generate images from text and reference media

### 29. A photo of a new machine must have an outdated safety label removed while everything else stays intact. What should be used?

Domain: Implement computer vision solutions

- A. Edit generated video segments
- B. Generate concise or detailed image captions
- C. Apply prompt-driven image modifications
- D. Edit a region of an image with a mask

### 30. Investigators must find the timestamp in recorded footage when a conveyor stops. Which capability applies?

Domain: Implement computer vision solutions

- A. Analyze video segments for events and content
- B. Generate concise or detailed image captions
- C. Edit generated video segments
- D. Generate video from text or reference media

### 31. Which sequence correctly processes inspection photos and routes uncertain readings to a person?

Domain: Implement computer vision solutions

- A. Validate format → review → upload image → parse structured fields → send multimodal request
- B. Parse structured fields → send multimodal request → upload image → validate format → review
- C. Upload image → validate format and size → send multimodal request → parse structured fields → route low-confidence values to review
- D. Send multimodal request → upload image → validate format → parse structured fields → review

### 32. A parts catalogue needs accessible image descriptions and answers about gauge values in photos. Which two capabilities apply? Select two.

Domain: Implement computer vision solutions

- A. Generate alt text aligned to accessibility guidance
- B. Lower temperature for more deterministic extraction
- C. Apply watermarks or provenance markers to generated media
- D. Answer questions grounded in visual evidence
- E. Generate concise or detailed image captions

### 33. Inspection packets mix photos, tables, and handwriting across several pages. Which Content Understanding mode should be evaluated?

Domain: Implement computer vision solutions

- A. Use pro mode for complex multimodal content understanding
- B. Use Azure AI Document Intelligence for forms and documents
- C. Use single-task mode for a focused extraction scenario
- D. Train a custom extraction model on labeled documents

### 34. Generated images appear in supplier-facing material and must be safe and on-brand. Which two controls apply? Select two.

Domain: Implement computer vision solutions

- A. Apply watermarks or provenance markers to generated media
- B. Filter unsafe or disallowed visual content
- C. Enforce brand and usage rules for generated visuals
- D. Adjust top-p to control response diversity
- E. Lower temperature for more deterministic extraction

### 35. A quality system requires fixed field names and types from each incident email. What should the prompt request?

Domain: Implement text analysis solutions

- A. Identify topics or key phrases for navigation
- B. Use Azure Translator or a language model for translation
- C. Prompt for JSON that conforms to a supplied schema
- D. Generate summaries with explicit length and audience constraints

### 36. A safety mailbox must detect personal data and rising frustration in reports. Which two analyses apply? Select two.

Domain: Implement text analysis solutions

- A. Analyze sentiment and tone with an appropriate service
- B. Generate summaries with explicit length and audience constraints
- C. Detect and redact sensitive personal data
- D. Apply a custom glossary or terminology list
- E. Identify topics or key phrases for navigation

### 37. Machine translation keeps mistranslating approved part names into another language. What should be configured?

Domain: Implement text analysis solutions

- A. Apply a custom glossary or terminology list
- B. Use Azure Translator or a language model for translation
- C. Extract entities with defined types and boundaries
- D. Detect and redact sensitive personal data

### 38. Recorded shift briefings must become searchable text. Which capability applies?

Domain: Implement text analysis solutions

- A. Use a multimodal model to reason over audio content
- B. Synthesize speech with Azure AI Speech
- C. Translate spoken language with speech translation
- D. Transcribe speech to text with Azure AI Speech

### 39. Hands-free reporting is inaccurate because of plant noise and local product names. What should be trained?

Domain: Implement text analysis solutions

- A. Use a custom speech model for specialized vocabulary
- B. Transcribe speech to text with Azure AI Speech
- C. Synthesize speech with Azure AI Speech
- D. Apply a custom glossary or terminology list

### 40. Supervisors need a short digest of a long incident investigation. Which task applies?

Domain: Implement text analysis solutions

- A. Extract entities with defined types and boundaries
- B. Use Azure Translator or a language model for translation
- C. Generate summaries with explicit length and audience constraints
- D. Identify topics or key phrases for navigation

### 41. Regulated incident summaries must keep required disclosures and understand plant-specific terms. Which two practices help? Select two.

Domain: Implement text analysis solutions

- A. Customize summaries and extraction for compliance needs
- B. Identify topics or key phrases for navigation
- C. Analyze sentiment and tone with an appropriate service
- D. Adapt prompts and models to domain terminology
- E. Use Azure Translator or a language model for translation

### 42. A search index must follow documents added to a storage account without custom code. What should be used?

Domain: Implement information extraction solutions

- A. Add an enrichment skillset to an indexing pipeline
- B. Use an Azure AI Search indexer to pull source content
- C. Push documents to an index through the data-plane API
- D. Apply OCR to convert images and scans into usable text

### 43. Newly generated inspection reports must be searchable within seconds. What should the application use?

Domain: Implement information extraction solutions

- A. Ingest content through supported indexers or APIs
- B. Push documents to an index through the data-plane API
- C. Use an Azure AI Search indexer to pull source content
- D. Propagate source deletions to indexes and caches

### 44. Which sequence correctly builds a citable retrieval pipeline over maintenance manuals?

Domain: Implement information extraction solutions

- A. Ingest → retrieve → chunk → embed → index → cite
- B. Index → retrieve → ingest → chunk → embed → cite
- C. Chunk → embed → ingest → retrieve → index → cite
- D. Ingest → extract text → chunk → embed → index → retrieve with citations

---

## Case study — Fabrikam Plant

The next three questions refer to this scenario. Read the full scenario before answering; case-study items are scored individually.

### 45. The plant uses a proprietary inspection form with no standard equivalent. What should be built?

Domain: Implement information extraction solutions

- A. Use Azure AI Document Intelligence for forms and documents
- B. Configure a Content Understanding analyzer for the content type
- C. Train a custom extraction model on labeled documents
- D. Use a prebuilt document model for common document types

### 46. Contractors must only retrieve documents approved for their plant. What should be enforced?

Domain: Implement information extraction solutions

- A. Apply semantic ranking to reorder search results
- B. Apply document-level security filters at query time
- C. Combine keyword and vector retrieval
- D. Verify index freshness and deletion propagation

### 47. Each indexed manual must gain extracted entities and a generated summary. What performs that work?

Domain: Implement information extraction solutions

- A. Use an Azure AI Search indexer to pull source content
- B. Add enrichment skills for text, image, and layout
- C. Add an enrichment skillset to an indexing pipeline
- D. Apply OCR to convert images and scans into usable text

---

## Case study — LineSight

The next three questions refer to this scenario. Read the full scenario before answering; case-study items are scored individually.

### 48. A plant runs continuous 24-hour inspection inference with steady volume and cannot tolerate throttling. Which capacity option should be evaluated?

Domain: Plan and manage an Azure AI solution

- A. Use a standard pay-as-you-go model deployment for variable demand
- B. Use provisioned throughput for predictable high-volume workloads
- C. Use supported prompt or response caching where appropriate
- D. Use batch processing for latency-tolerant bulk work

### 49. A defect request fails only after the second tool call. What should be inspected first?

Domain: Implement generative AI and agentic solutions

- A. Lower temperature for more deterministic extraction
- B. Apply watermarks or provenance markers to generated media
- C. Use supported prompt or response caching where appropriate
- D. Enable tracing across agent, model, and tool calls

### 50. The agent must keep the work-order number across turns while checking status. Which capability is required?

Domain: Implement generative AI and agentic solutions

- A. Persist conversation history in a thread or session
- B. Choose an embedding model suited to the content and language
- C. Use provisioned throughput for predictable high-volume workloads
- D. Apply watermarks or provenance markers to generated media

---

## Answer key and explanations

### Question 1 — A

Answer: Compare supported models in the Foundry model catalog. The catalog shows which models support vision in each region before design is fixed. The catalog shows supported models with capability, modality, region, and lifecycle details. Verify availability for your subscription and region before designing around one model. Local study-map skill 1.1 (Selecting Foundry Models and Services), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Microsoft Foundry documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/

- **A:** Correct. The catalog shows supported models with capability, modality, region, and lifecycle details. Verify availability for your subscription and region before designing around one model. In this case: The catalog shows which models support vision in each region before design is fixed.
- **B:** Incorrect for this question. Large models handle ambiguity and multi-step reasoning better in many cases, at higher cost and latency. Select with measured evidence rather than brand preference. Why the correct answer wins: The catalog shows which models support vision in each region before design is fixed.
- **C:** Incorrect for this question. A custom model is justified when supported prebuilt options cannot meet a defined requirement. It adds data, evaluation, and lifecycle obligations. Why the correct answer wins: The catalog shows which models support vision in each region before design is fixed.
- **D:** Incorrect for this question. Small models can reduce latency and cost for constrained classification or extraction. Confirm quality on representative data before standardizing. Why the correct answer wins: The catalog shows which models support vision in each region before design is fixed.

### Question 2 — B

Answer: Use a multimodal model for combined text, image, or audio input. A multimodal model accepts image and text in the same request. Multimodal models accept more than one content type in a request. Validate extraction and grounding quality for each modality used. Local study-map skill 1.1 (Selecting Foundry Models and Services), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Microsoft Foundry documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/

- **A:** Incorrect for this question. Prebuilt managed capabilities can reduce custom model work where their behavior and limits fit the task. They are not a substitute for task-specific validation. Why the correct answer wins: A multimodal model accepts image and text in the same request.
- **B:** Correct. Multimodal models accept more than one content type in a request. Validate extraction and grounding quality for each modality used. In this case: A multimodal model accepts image and text in the same request.
- **C:** Incorrect for this question. A custom model is justified when supported prebuilt options cannot meet a defined requirement. It adds data, evaluation, and lifecycle obligations. Why the correct answer wins: A multimodal model accepts image and text in the same request.
- **D:** Incorrect for this question. Small models can reduce latency and cost for constrained classification or extraction. Confirm quality on representative data before standardizing. Why the correct answer wins: A multimodal model accepts image and text in the same request.

### Question 3 — C

Answer: Expose a typed function as an agent tool. A function tool calls the asset system under the application's authorization. Function tools let the agent request a defined operation with structured arguments. Authorization and input validation must be enforced server-side. Local study-map skill 1.2 (Retrieval, Memory, Tool, and Knowledge Services), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Microsoft Foundry documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/

- **A:** Incorrect for this question. OpenAPI tools describe supported HTTP operations for agent use. Narrow operations, validate inputs, and authenticate the caller. Why the correct answer wins: A function tool calls the asset system under the application's authorization.
- **B:** Incorrect for this question. Managed state supports multi-turn continuity without rebuilding history manually. Retention, isolation, and user control still need design. Why the correct answer wins: A function tool calls the asset system under the application's authorization.
- **C:** Correct. Function tools let the agent request a defined operation with structured arguments. Authorization and input validation must be enforced server-side. In this case: A function tool calls the asset system under the application's authorization.
- **D:** Incorrect for this question. An index gives an agent curated, searchable evidence under configured access. Index content and permissions require ongoing ownership. Why the correct answer wins: A function tool calls the asset system under the application's authorization.

### Question 4 — C

Answer: Use managed conversation state or memory for continuity. Managed conversation state keeps prior turns available to the agent. Managed state supports multi-turn continuity without rebuilding history manually. Retention, isolation, and user control still need design. Local study-map skill 1.2 (Retrieval, Memory, Tool, and Knowledge Services), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Microsoft Foundry documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/

- **A:** Incorrect for this question. Indexers automate ingestion and can run on a schedule. Monitor failures, deletions, and field mappings. Why the correct answer wins: Managed conversation state keeps prior turns available to the agent.
- **B:** Incorrect for this question. Function tools let the agent request a defined operation with structured arguments. Authorization and input validation must be enforced server-side. Why the correct answer wins: Managed conversation state keeps prior turns available to the agent.
- **C:** Correct. Managed state supports multi-turn continuity without rebuilding history manually. Retention, isolation, and user control still need design. In this case: Managed conversation state keeps prior turns available to the agent.
- **D:** Incorrect for this question. Embeddings support similarity search over meaning rather than exact terms. Vector search still needs chunking, filtering, and evaluation. Why the correct answer wins: Managed conversation state keeps prior turns available to the agent.

### Question 5 — B

Answer: Provision resources → deploy model → configure app connection → evaluate → promote. Provisioning and deployment precede configuration, and evaluation gates promotion. Provisioning and deployment precede app configuration, and evaluation gates promotion. Local study-map skill 1.3 (Infrastructure, Deployment, and CI/CD), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Microsoft Foundry documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/

- **A:** Incorrect for this question. Promotion before provisioning and evaluation skips the controls that make deployment safe. Why the correct answer wins: Provisioning and deployment precede configuration, and evaluation gates promotion.
- **B:** Correct. Provisioning and deployment precede app configuration, and evaluation gates promotion. In this case: Provisioning and deployment precede configuration, and evaluation gates promotion.
- **C:** Incorrect for this question. Evaluation after promotion cannot gate the release. Why the correct answer wins: Provisioning and deployment precede configuration, and evaluation gates promotion.
- **D:** Incorrect for this question. Evaluation before any deployment or configuration has nothing meaningful to assess. Why the correct answer wins: Provisioning and deployment precede configuration, and evaluation gates promotion.

### Question 6 — B

Answer: Use private endpoints and disable public network access. A private endpoint keeps model traffic on the private network path. Private connectivity keeps service traffic on approved network paths. Pair it with private DNS so clients resolve the private address. Local study-map skill 1.3 (Infrastructure, Deployment, and CI/CD), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Microsoft Foundry documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/

- **A:** Incorrect for this question. Retries, tool calls, evaluation, and review contribute to unit economics. Per-outcome cost supports better optimization. Why the correct answer wins: A private endpoint keeps model traffic on the private network path.
- **B:** Correct. Private connectivity keeps service traffic on approved network paths. Pair it with private DNS so clients resolve the private address. In this case: A private endpoint keeps model traffic on the private network path.
- **C:** Incorrect for this question. Quota limits throughput regardless of application capacity. Request increases in advance and plan graceful degradation. Why the correct answer wins: A private endpoint keeps model traffic on the private network path.
- **D:** Incorrect for this question. Repeatable deployments reduce configuration drift. Include model deployments, indexes, and connections in review and promotion. Why the correct answer wins: A private endpoint keeps model traffic on the private network path.

### Question 7 — C

Answer: Plan for model quota expressed in tokens and requests per minute. Request and token quota must cover the real peak concurrency of each shift. Quota limits throughput regardless of application capacity. Request increases in advance and plan graceful degradation. Local study-map skill 1.4 (Quotas, Scaling, and Cost), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Microsoft Foundry documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/

- **A:** Incorrect for this question. Retries, tool calls, evaluation, and review contribute to unit economics. Per-outcome cost supports better optimization. Why the correct answer wins: Request and token quota must cover the real peak concurrency of each shift.
- **B:** Incorrect for this question. Provisioned capacity reserves throughput at a committed cost. It fits stable demand, not unpredictable spikes. Why the correct answer wins: Request and token quota must cover the real peak concurrency of each shift.
- **C:** Correct. Quota limits throughput regardless of application capacity. Request increases in advance and plan graceful degradation. In this case: Request and token quota must cover the real peak concurrency of each shift.
- **D:** Incorrect for this question. User behavior, data, and models change. Rolling baselines reveal degradation that a one-time evaluation misses. Why the correct answer wins: Request and token quota must cover the real peak concurrency of each shift.

### Question 8 — D

Answer: Track cost per accepted task, not only per token. Caching repeated manual content avoids re-billing identical prefix tokens. Retries, tool calls, evaluation, and review contribute to unit economics. Per-outcome cost supports better optimization. Local study-map skill 1.4 (Quotas, Scaling, and Cost), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Microsoft Foundry documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/

- **A:** Incorrect for this question. Quota limits throughput regardless of application capacity. Request increases in advance and plan graceful degradation. Why the correct answer wins: Caching repeated manual content avoids re-billing identical prefix tokens.
- **B:** Incorrect for this question. Token analytics supports cost and performance tuning. Attribute usage to features and tenants where possible. Why the correct answer wins: Caching repeated manual content avoids re-billing identical prefix tokens.
- **C:** Incorrect for this question. Caching can reduce cost and latency for repeated content. Validate correctness and invalidation behavior. Why the correct answer wins: Caching repeated manual content avoids re-billing identical prefix tokens.
- **D:** Correct. Retries, tool calls, evaluation, and review contribute to unit economics. Per-outcome cost supports better optimization. In this case: Caching repeated manual content avoids re-billing identical prefix tokens.

### Question 9 — A

Answer: Use Azure Monitor and Application Insights for telemetry. Platform monitoring collects metrics and logs for operational visibility. Central telemetry captures latency, errors, dependencies, and custom events. Redact sensitive content before logging. Local study-map skill 1.5 (Monitoring Performance, Drift, Safety, and Grounding), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Microsoft Foundry documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/

- **A:** Correct. Central telemetry captures latency, errors, dependencies, and custom events. Redact sensitive content before logging. In this case: Platform monitoring collects metrics and logs for operational visibility.
- **B:** Incorrect for this question. Alerts turn monitoring into action. Route them to an accountable owner with a runbook. Why the correct answer wins: Platform monitoring collects metrics and logs for operational visibility.
- **C:** Incorrect for this question. User behavior, data, and models change. Rolling baselines reveal degradation that a one-time evaluation misses. Why the correct answer wins: Platform monitoring collects metrics and logs for operational visibility.
- **D:** Incorrect for this question. Audit evidence supports investigation and accountability. Protect log integrity and retention. Why the correct answer wins: Platform monitoring collects metrics and logs for operational visibility.

### Question 10 — A, B

Answers: Monitor input and quality drift over time; Alert on latency, error rate, safety, and cost thresholds. Drift detection identifies distribution change, and alerting notifies the team when it occurs. User behavior, data, and models change. Rolling baselines reveal degradation that a one-time evaluation misses. Alerts turn monitoring into action. Route them to an accountable owner with a runbook. Local study-map skill 1.5 (Monitoring Performance, Drift, Safety, and Grounding), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Microsoft Foundry documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/

- **A:** Correct. User behavior, data, and models change. Rolling baselines reveal degradation that a one-time evaluation misses. In this case: Drift detection identifies distribution change, and alerting notifies the team when it occurs.
- **B:** Correct. Alerts turn monitoring into action. Route them to an accountable owner with a runbook. In this case: Drift detection identifies distribution change, and alerting notifies the team when it occurs.
- **C:** Incorrect for this question. Retries, tool calls, evaluation, and review contribute to unit economics. Per-outcome cost supports better optimization. Why the correct answer wins: Drift detection identifies distribution change, and alerting notifies the team when it occurs.
- **D:** Incorrect for this question. Quota limits throughput regardless of application capacity. Request increases in advance and plan graceful degradation. Why the correct answer wins: Drift detection identifies distribution change, and alerting notifies the team when it occurs.
- **E:** Incorrect for this question. Caching can reduce cost and latency for repeated content. Validate correctness and invalidation behavior. Why the correct answer wins: Drift detection identifies distribution change, and alerting notifies the team when it occurs.

### Question 11 — B, E

Answers: Authenticate with a managed identity instead of keys; Use least-privilege Azure RBAC roles for the workload identity. A managed identity removes stored credentials, and a least-privilege role limits permissions. Managed identities avoid embedded secrets and support role-based access. Assign only required data-plane roles. Roles should match the operations the app or agent performs. Broad contributor access increases blast radius. Local study-map skill 1.6 (Security, Identity, and Networking), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Microsoft Foundry documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/

- **A:** Incorrect for this question. A managed secret store supports rotation and access control. Secrets should never appear in prompts, code, or logs. Why the correct answer wins: A managed identity removes stored credentials, and a least-privilege role limits permissions.
- **B:** Correct. Roles should match the operations the app or agent performs. Broad contributor access increases blast radius. In this case: A managed identity removes stored credentials, and a least-privilege role limits permissions.
- **C:** Incorrect for this question. Private connectivity keeps service traffic on approved network paths. Pair it with private DNS so clients resolve the private address. Why the correct answer wins: A managed identity removes stored credentials, and a least-privilege role limits permissions.
- **D:** Incorrect for this question. Filters assign severity and can block or annotate content. Thresholds should reflect the use case and applicable policy. Why the correct answer wins: A managed identity removes stored credentials, and a least-privilege role limits permissions.
- **E:** Correct. Managed identities avoid embedded secrets and support role-based access. Assign only required data-plane roles. In this case: A managed identity removes stored credentials, and a least-privilege role limits permissions.

### Question 12 — A

Answer: Enforce constraints in code and platform policy. A guardrail constrains the assistant's behaviour for defined prohibited topics. Guardrails are technical controls, not prompt suggestions. Validate inputs, authorize tools, and limit egress. Local study-map skill 1.7 (Responsible AI Controls and Oversight), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Microsoft Foundry documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/

- **A:** Correct. Guardrails are technical controls, not prompt suggestions. Validate inputs, authorize tools, and limit egress. In this case: A guardrail constrains the assistant's behaviour for defined prohibited topics.
- **B:** Incorrect for this question. Approval must occur before the effect and identify who approved what. A model confidence score is not approval. Why the correct answer wins: A guardrail constrains the assistant's behaviour for defined prohibited topics.
- **C:** Incorrect for this question. Oversight settings bound what an agent may do autonomously. They should be tested against realistic misuse and failure. Why the correct answer wins: A guardrail constrains the assistant's behaviour for defined prohibited topics.
- **D:** Incorrect for this question. Audit evidence supports investigation and accountability. Protect log integrity and retention. Why the correct answer wins: A guardrail constrains the assistant's behaviour for defined prohibited topics.

### Question 13 — D

Answer: Detect protected or copyrighted material in output. Protected-material detection flags or blocks known copyrighted output. Detection can reduce distribution risk for generated content. Policy and licensing review still apply. Local study-map skill 1.7 (Responsible AI Controls and Oversight), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Microsoft Foundry documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/

- **A:** Incorrect for this question. Brand controls define permitted logos, styles, and claims. Technical generation must still pass approval. Why the correct answer wins: Protected-material detection flags or blocks known copyrighted output.
- **B:** Incorrect for this question. Watermarks support disclosure and traceability. They do not replace usage policy or review. Why the correct answer wins: Protected-material detection flags or blocks known copyrighted output.
- **C:** Incorrect for this question. Filters assign severity and can block or annotate content. Thresholds should reflect the use case and applicable policy. Why the correct answer wins: Protected-material detection flags or blocks known copyrighted output.
- **D:** Correct. Detection can reduce distribution risk for generated content. Policy and licensing review still apply. In this case: Protected-material detection flags or blocks known copyrighted output.

### Question 14 — B

Answer: Ground responses with retrieval-augmented generation. RAG retrieves current approved evidence and supports citations. RAG supplies selected source content at request time so answers can cite current evidence. It reduces but does not eliminate fabrication. Local study-map skill 2.1 (Building Generative Applications), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Foundry Agent Service documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/agents/

- **A:** Incorrect for this question. Translating the request does not replace retrieval, grounding, or validation, so it cannot satisfy an evidence or citation requirement. Why the correct answer wins: RAG retrieves current approved evidence and supports citations.
- **B:** Correct. RAG supplies selected source content at request time so answers can cite current evidence. It reduces but does not eliminate fabrication. In this case: RAG retrieves current approved evidence and supports citations.
- **C:** Incorrect for this question. Checkpoints validate intermediate results before later steps depend on them. This limits error propagation. Why the correct answer wins: RAG retrieves current approved evidence and supports citations.
- **D:** Incorrect for this question. Routing can balance quality and cost. Fallback and evaluation are required. Why the correct answer wins: RAG retrieves current approved evidence and supports citations.

### Question 15 — D

Answer: Return a defined JSON schema for downstream systems. Schema-constrained output supports automated validation and record creation. Structured output supports validation and automation. Schema validity does not prove semantic correctness. Local study-map skill 2.1 (Building Generative Applications), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Foundry Agent Service documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/agents/

- **A:** Incorrect for this question. Checkpoints validate intermediate results before later steps depend on them. This limits error propagation. Why the correct answer wins: Schema-constrained output supports automated validation and record creation.
- **B:** Incorrect for this question. Templates improve consistency and reviewability. Version them and test changes. Why the correct answer wins: Schema-constrained output supports automated validation and record creation.
- **C:** Incorrect for this question. Caching can reduce cost and latency for repeated content. Validate correctness and invalidation behavior. Why the correct answer wins: Schema-constrained output supports automated validation and record creation.
- **D:** Correct. Structured output supports validation and automation. Schema validity does not prove semantic correctness. In this case: Schema-constrained output supports automated validation and record creation.

### Question 16 — A

Answer: Design multistep workflows with explicit checkpoints. Explicit stages with validation before any downstream action. Checkpoints validate intermediate results before later steps depend on them. This limits error propagation. Local study-map skill 2.1 (Building Generative Applications), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Foundry Agent Service documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/agents/

- **A:** Correct. Checkpoints validate intermediate results before later steps depend on them. This limits error propagation. In this case: Explicit stages with validation before any downstream action.
- **B:** Incorrect for this question. Routing can balance quality and cost. Fallback and evaluation are required. Why the correct answer wins: Explicit stages with validation before any downstream action.
- **C:** Incorrect for this question. Autonomous workflows need bounded actions and escalation. Unbounded loops and broad tools increase risk. Why the correct answer wins: Explicit stages with validation before any downstream action.
- **D:** Incorrect for this question. A single call cannot validate intermediate results or fetch authoritative evidence, so it is unsuitable for multi-stage or grounded workflows. Why the correct answer wins: Explicit stages with validation before any downstream action.

### Question 17 — C

Answer: Use a Foundry SDK or supported connector from application code. A supported Foundry SDK provides maintained client behaviour instead of raw HTTP calls. SDKs provide supported request and response patterns. Pin versions and handle retries, timeouts, and errors explicitly. Local study-map skill 2.2 (Foundry SDK and Project Integration), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Foundry Agent Service documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/agents/

- **A:** Incorrect for this question. Batch deployments can lower cost for large asynchronous jobs. They are unsuitable for interactive agent turns. Why the correct answer wins: A supported Foundry SDK provides maintained client behaviour instead of raw HTTP calls.
- **B:** Incorrect for this question. Manual portal changes work for exploration but are slow, undocumented, and hard to reproduce, so they are a poor fit for governed release processes. Why the correct answer wins: A supported Foundry SDK provides maintained client behaviour instead of raw HTTP calls.
- **C:** Correct. SDKs provide supported request and response patterns. Pin versions and handle retries, timeouts, and errors explicitly. In this case: A supported Foundry SDK provides maintained client behaviour instead of raw HTTP calls.
- **D:** Incorrect for this question. Repeatable deployments reduce configuration drift. Include model deployments, indexes, and connections in review and promotion. Why the correct answer wins: A supported Foundry SDK provides maintained client behaviour instead of raw HTTP calls.

### Question 18 — C

Answer: Connect the application to the Foundry project endpoint. The project endpoint binds the client to that project and its deployments. Project endpoints and SDK clients bind an app to approved models and resources. Use identity-based authentication and environment-specific configuration. Local study-map skill 2.2 (Foundry SDK and Project Integration), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Foundry Agent Service documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/agents/

- **A:** Incorrect for this question. Indexers automate ingestion and can run on a schedule. Monitor failures, deletions, and field mappings. Why the correct answer wins: The project endpoint binds the client to that project and its deployments.
- **B:** Incorrect for this question. A managed secret store supports rotation and access control. Secrets should never appear in prompts, code, or logs. Why the correct answer wins: The project endpoint binds the client to that project and its deployments.
- **C:** Correct. Project endpoints and SDK clients bind an app to approved models and resources. Use identity-based authentication and environment-specific configuration. In this case: The project endpoint binds the client to that project and its deployments.
- **D:** Incorrect for this question. The catalog shows supported models with capability, modality, region, and lifecycle details. Verify availability for your subscription and region before designing around one model. Why the correct answer wins: The project endpoint binds the client to that project and its deployments.

### Question 19 — A, B

Answers: Build a representative golden dataset from real tasks; Re-run evaluation suites after meaningful changes. A golden dataset holds the benchmark, and regression evaluation rechecks known failure cases. A golden set anchors evaluation in expected behavior. Include edge cases and high-risk scenarios. Prompts, models, indexes, and tools all affect behavior. Regression tests catch unintended effects. Local study-map skill 2.3 (Evaluating Models and Applications), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Foundry Agent Service documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/agents/

- **A:** Correct. A golden set anchors evaluation in expected behavior. Include edge cases and high-risk scenarios. In this case: A golden dataset holds the benchmark, and regression evaluation rechecks known failure cases.
- **B:** Correct. Prompts, models, indexes, and tools all affect behavior. Regression tests catch unintended effects. In this case: A golden dataset holds the benchmark, and regression evaluation rechecks known failure cases.
- **C:** Incorrect for this question. Provisioned capacity reserves throughput at a committed cost. It fits stable demand, not unpredictable spikes. Why the correct answer wins: A golden dataset holds the benchmark, and regression evaluation rechecks known failure cases.
- **D:** Incorrect for this question. Lower temperature reduces sampling variability. It does not guarantee factual correctness. Why the correct answer wins: A golden dataset holds the benchmark, and regression evaluation rechecks known failure cases.
- **E:** Incorrect for this question. Watermarks support disclosure and traceability. They do not replace usage policy or review. Why the correct answer wins: A golden dataset holds the benchmark, and regression evaluation rechecks known failure cases.

### Question 20 — A

Answer: Use evaluators for quality, safety, and groundedness. Evaluators produce comparable quality scores across variants. Evaluators provide repeatable signals across models and prompts. They must be calibrated against human judgment for high-impact work. Local study-map skill 2.3 (Evaluating Models and Applications), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Foundry Agent Service documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/agents/

- **A:** Correct. Evaluators provide repeatable signals across models and prompts. They must be calibrated against human judgment for high-impact work. In this case: Evaluators produce comparable quality scores across variants.
- **B:** Incorrect for this question. Alerts turn monitoring into action. Route them to an accountable owner with a runbook. Why the correct answer wins: Evaluators produce comparable quality scores across variants.
- **C:** Incorrect for this question. Audit evidence supports investigation and accountability. Protect log integrity and retention. Why the correct answer wins: Evaluators produce comparable quality scores across variants.
- **D:** Incorrect for this question. Central telemetry captures latency, errors, dependencies, and custom events. Redact sensitive content before logging. Why the correct answer wins: Evaluators produce comparable quality scores across variants.

### Question 21 — A

Answer: Define narrow tool schemas with clear descriptions. A precise tool schema with typed parameters prevents malformed arguments. Precise schemas help the model choose tools and arguments correctly. Broad or ambiguous tools invite unsafe calls. Local study-map skill 2.4 (Agent Roles, Goals, and Tool Schemas), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Foundry Agent Service documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/agents/

- **A:** Correct. Precise schemas help the model choose tools and arguments correctly. Broad or ambiguous tools invite unsafe calls. In this case: A precise tool schema with typed parameters prevents malformed arguments.
- **B:** Incorrect for this question. System messages define role and constraints. They are not a security boundary against injection. Why the correct answer wins: A precise tool schema with typed parameters prevents malformed arguments.
- **C:** Incorrect for this question. Managed state supports multi-turn continuity without rebuilding history manually. Retention, isolation, and user control still need design. Why the correct answer wins: A precise tool schema with typed parameters prevents malformed arguments.
- **D:** Incorrect for this question. Templates improve consistency and reviewability. Version them and test changes. Why the correct answer wins: A precise tool schema with typed parameters prevents malformed arguments.

### Question 22 — A, B

Answers: Put stable behavior rules in the system message; Use managed conversation state or memory for continuity. The system message sets persistent behaviour, and conversation memory retains context. System messages define role and constraints. They are not a security boundary against injection. Managed state supports multi-turn continuity without rebuilding history manually. Retention, isolation, and user control still need design. Local study-map skill 2.4 (Agent Roles, Goals, and Tool Schemas), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Foundry Agent Service documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/agents/

- **A:** Correct. System messages define role and constraints. They are not a security boundary against injection. In this case: The system message sets persistent behaviour, and conversation memory retains context.
- **B:** Correct. Managed state supports multi-turn continuity without rebuilding history manually. Retention, isolation, and user control still need design. In this case: The system message sets persistent behaviour, and conversation memory retains context.
- **C:** Incorrect for this question. OpenAPI tools describe supported HTTP operations for agent use. Narrow operations, validate inputs, and authenticate the caller. Why the correct answer wins: The system message sets persistent behaviour, and conversation memory retains context.
- **D:** Incorrect for this question. Precise schemas help the model choose tools and arguments correctly. Broad or ambiguous tools invite unsafe calls. Why the correct answer wins: The system message sets persistent behaviour, and conversation memory retains context.
- **E:** Incorrect for this question. RAG supplies selected source content at request time so answers can cite current evidence. It reduces but does not eliminate fabrication. Why the correct answer wins: The system message sets persistent behaviour, and conversation memory retains context.

### Question 23 — B

Answer: Expose an OpenAPI operation as an agent tool. An OpenAPI tool reuses the published contract without hand-written wrappers. OpenAPI tools describe supported HTTP operations for agent use. Narrow operations, validate inputs, and authenticate the caller. Local study-map skill 2.5 (Agent Tools, Retrieval, Memory, and Function Calling), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Foundry Agent Service documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/agents/

- **A:** Incorrect for this question. Managed state supports multi-turn continuity without rebuilding history manually. Retention, isolation, and user control still need design. Why the correct answer wins: An OpenAPI tool reuses the published contract without hand-written wrappers.
- **B:** Correct. OpenAPI tools describe supported HTTP operations for agent use. Narrow operations, validate inputs, and authenticate the caller. In this case: An OpenAPI tool reuses the published contract without hand-written wrappers.
- **C:** Incorrect for this question. Function tools let the agent request a defined operation with structured arguments. Authorization and input validation must be enforced server-side. Why the correct answer wins: An OpenAPI tool reuses the published contract without hand-written wrappers.
- **D:** Incorrect for this question. RAG supplies selected source content at request time so answers can cite current evidence. It reduces but does not eliminate fabrication. Why the correct answer wins: An OpenAPI tool reuses the published contract without hand-written wrappers.

### Question 24 — D

Answer: Run agents in a fixed sequence. A sequential pattern runs stages in a defined order, with each stage using the previous output. Sequential orchestration makes dependencies explicit. It may add latency where steps could run concurrently. Local study-map skill 2.6 (Multi-Agent Orchestration and Safeguards), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Foundry Agent Service documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/agents/

- **A:** Incorrect for this question. Parallel execution reduces wall-clock time for independent work. Reconciliation still requires design. Why the correct answer wins: A sequential pattern runs stages in a defined order, with each stage using the previous output.
- **B:** Incorrect for this question. A manager routes tasks and merges results. Clear responsibility and failure handling are required. Why the correct answer wins: A sequential pattern runs stages in a defined order, with each stage using the previous output.
- **C:** Incorrect for this question. Reflection can catch omissions and inconsistencies. It can also reinforce errors, so validate against evidence. Why the correct answer wins: A sequential pattern runs stages in a defined order, with each stage using the previous output.
- **D:** Correct. Sequential orchestration makes dependencies explicit. It may add latency where steps could run concurrently. In this case: A sequential pattern runs stages in a defined order, with each stage using the previous output.

### Question 25 — B

Answer: Use a manager agent to coordinate specialists. A manager agent routes to specialists and consolidates their replies. A manager routes tasks and merges results. Clear responsibility and failure handling are required. Local study-map skill 2.6 (Multi-Agent Orchestration and Safeguards), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Foundry Agent Service documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/agents/

- **A:** Incorrect for this question. Handoffs should carry goal, evidence, permissions, and open questions. Implicit context is easily lost. Why the correct answer wins: A manager agent routes to specialists and consolidates their replies.
- **B:** Correct. A manager routes tasks and merges results. Clear responsibility and failure handling are required. In this case: A manager agent routes to specialists and consolidates their replies.
- **C:** Incorrect for this question. Parallel execution reduces wall-clock time for independent work. Reconciliation still requires design. Why the correct answer wins: A manager agent routes to specialists and consolidates their replies.
- **D:** Incorrect for this question. Reflection can catch omissions and inconsistencies. It can also reinforce errors, so validate against evidence. Why the correct answer wins: A manager agent routes to specialists and consolidates their replies.

### Question 26 — C

Answer: Detect alert → inspect traces → isolate the failing step → apply fix → verify with regression evaluation. Alert, traces, isolation, fix, then regression verification in that order. Triage moves from signal to evidence to a targeted fix, then proves the fix with regression tests. Local study-map skill 2.7 (Agent Monitoring and Error Analysis), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Foundry Agent Service documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/agents/

- **A:** Incorrect for this question. The alert must be detected first, and traces must be inspected before the step is isolated. Why the correct answer wins: Alert, traces, isolation, fix, then regression verification in that order.
- **B:** Incorrect for this question. Verification before a fix and before diagnosis proves nothing. Why the correct answer wins: Alert, traces, isolation, fix, then regression verification in that order.
- **C:** Correct. Triage moves from signal to evidence to a targeted fix, then proves the fix with regression tests. In this case: Alert, traces, isolation, fix, then regression verification in that order.
- **D:** Incorrect for this question. A fix cannot precede detection and diagnosis. Why the correct answer wins: Alert, traces, isolation, fix, then regression verification in that order.

### Question 27 — D

Answer: Lower temperature for more deterministic extraction. Lower temperature reduces sampling variability for deterministic extraction. Lower temperature reduces sampling variability. It does not guarantee factual correctness. Local study-map skill 2.8 (Generation Tuning and Observability), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Foundry Agent Service documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/agents/

- **A:** Incorrect for this question. Caching can reduce cost and latency for repeated content. Validate correctness and invalidation behavior. Why the correct answer wins: Lower temperature reduces sampling variability for deterministic extraction.
- **B:** Incorrect for this question. Routing can balance quality and cost. Fallback and evaluation are required. Why the correct answer wins: Lower temperature reduces sampling variability for deterministic extraction.
- **C:** Incorrect for this question. Top-p narrows or broadens token sampling. Tune with evaluation rather than by intuition. Why the correct answer wins: Lower temperature reduces sampling variability for deterministic extraction.
- **D:** Correct. Lower temperature reduces sampling variability. It does not guarantee factual correctness. In this case: Lower temperature reduces sampling variability for deterministic extraction.

### Question 28 — D

Answer: Generate images from text and reference media. Image generation produces a new illustration from a description. Image generation supports creative and product workflows. Apply policy, watermarking, and provenance controls. Local study-map skill 3.1 (Image Generation and Editing), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Azure AI Vision and Content Understanding documentation: https://learn.microsoft.com/en-us/azure/ai-services/content-understanding/

- **A:** Incorrect for this question. Alt text should convey purpose and essential content, not decorative detail. Human review is still needed for critical pages. Why the correct answer wins: Image generation produces a new illustration from a description.
- **B:** Incorrect for this question. Inpainting changes a selected area while preserving the rest. Validate identity, brand, and safety constraints. Why the correct answer wins: Image generation produces a new illustration from a description.
- **C:** Incorrect for this question. Video generation creates clips from prompts or images. Duration, consistency, and safety require review. Why the correct answer wins: Image generation produces a new illustration from a description.
- **D:** Correct. Image generation supports creative and product workflows. Apply policy, watermarking, and provenance controls. In this case: Image generation produces a new illustration from a description.

### Question 29 — D

Answer: Edit a region of an image with a mask. Mask-based inpainting edits only the selected region. Inpainting changes a selected area while preserving the rest. Validate identity, brand, and safety constraints. Local study-map skill 3.1 (Image Generation and Editing), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Azure AI Vision and Content Understanding documentation: https://learn.microsoft.com/en-us/azure/ai-services/content-understanding/

- **A:** Incorrect for this question. Video editing can revise scenes or timing. Preserve provenance and review for harmful manipulation. Why the correct answer wins: Mask-based inpainting edits only the selected region.
- **B:** Incorrect for this question. Captions describe visual content for users or downstream systems. Match detail to the audience and purpose. Why the correct answer wins: Mask-based inpainting edits only the selected region.
- **C:** Incorrect for this question. Prompt-based edits can alter style or content. Review outputs for unintended changes and policy violations. Why the correct answer wins: Mask-based inpainting edits only the selected region.
- **D:** Correct. Inpainting changes a selected area while preserving the rest. Validate identity, brand, and safety constraints. In this case: Mask-based inpainting edits only the selected region.

### Question 30 — A

Answer: Analyze video segments for events and content. Video analysis locates events and timestamps within existing footage. Video analysis can summarize or detect events across time. Sampling strategy affects coverage and cost. Local study-map skill 3.2 (Video Generation and Editing), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Azure AI Vision and Content Understanding documentation: https://learn.microsoft.com/en-us/azure/ai-services/content-understanding/

- **A:** Correct. Video analysis can summarize or detect events across time. Sampling strategy affects coverage and cost. In this case: Video analysis locates events and timestamps within existing footage.
- **B:** Incorrect for this question. Captions describe visual content for users or downstream systems. Match detail to the audience and purpose. Why the correct answer wins: Video analysis locates events and timestamps within existing footage.
- **C:** Incorrect for this question. Video editing can revise scenes or timing. Preserve provenance and review for harmful manipulation. Why the correct answer wins: Video analysis locates events and timestamps within existing footage.
- **D:** Incorrect for this question. Video generation creates clips from prompts or images. Duration, consistency, and safety require review. Why the correct answer wins: Video analysis locates events and timestamps within existing footage.

### Question 31 — C

Answer: Upload image → validate format and size → send multimodal request → parse structured fields → route low-confidence values to review. Validation brackets the multimodal call, and low-confidence results go to review. Validation and structured parsing bracket the multimodal call, and low-confidence output goes to people. Local study-map skill 3.4 (Visual Extraction and Video Analysis), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Azure AI Vision and Content Understanding documentation: https://learn.microsoft.com/en-us/azure/ai-services/content-understanding/

- **A:** Incorrect for this question. Review cannot precede the request, and parsing must follow the response. Why the correct answer wins: Validation brackets the multimodal call, and low-confidence results go to review.
- **B:** Incorrect for this question. Parsing requires a response, which requires an uploaded and validated image. Why the correct answer wins: Validation brackets the multimodal call, and low-confidence results go to review.
- **C:** Correct. Validation and structured parsing bracket the multimodal call, and low-confidence output goes to people. In this case: Validation brackets the multimodal call, and low-confidence results go to review.
- **D:** Incorrect for this question. A request cannot precede the upload, and validation must come before the call. Why the correct answer wins: Validation brackets the multimodal call, and low-confidence results go to review.

### Question 32 — A, D

Answers: Answer questions grounded in visual evidence; Generate alt text aligned to accessibility guidance. Alt text serves accessibility, and visual question answering grounds answers in image content. Visual question answering should cite the relevant region or content. Avoid answering beyond what the image supports. Alt text should convey purpose and essential content, not decorative detail. Human review is still needed for critical pages. Local study-map skill 3.3 (Multimodal Understanding and Accessibility), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Azure AI Vision and Content Understanding documentation: https://learn.microsoft.com/en-us/azure/ai-services/content-understanding/

- **A:** Correct. Alt text should convey purpose and essential content, not decorative detail. Human review is still needed for critical pages. In this case: Alt text serves accessibility, and visual question answering grounds answers in image content.
- **B:** Incorrect for this question. Lower temperature reduces sampling variability. It does not guarantee factual correctness. Why the correct answer wins: Alt text serves accessibility, and visual question answering grounds answers in image content.
- **C:** Incorrect for this question. Watermarks support disclosure and traceability. They do not replace usage policy or review. Why the correct answer wins: Alt text serves accessibility, and visual question answering grounds answers in image content.
- **D:** Correct. Visual question answering should cite the relevant region or content. Avoid answering beyond what the image supports. In this case: Alt text serves accessibility, and visual question answering grounds answers in image content.
- **E:** Incorrect for this question. Captions describe visual content for users or downstream systems. Match detail to the audience and purpose. Why the correct answer wins: Alt text serves accessibility, and visual question answering grounds answers in image content.

### Question 33 — A

Answer: Use pro mode for complex multimodal content understanding. Pro mode handles complex multi-page multimodal content. Pro mode handles more demanding layouts and multimodal inputs at higher cost. Use it where simpler modes fail requirements. Local study-map skill 3.4 (Visual Extraction and Video Analysis), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Azure AI Vision and Content Understanding documentation: https://learn.microsoft.com/en-us/azure/ai-services/content-understanding/

- **A:** Correct. Pro mode handles more demanding layouts and multimodal inputs at higher cost. Use it where simpler modes fail requirements. In this case: Pro mode handles complex multi-page multimodal content.
- **B:** Incorrect for this question. Document Intelligence provides prebuilt and custom extraction for structured documents. Validate field accuracy on representative samples. Why the correct answer wins: Pro mode handles complex multi-page multimodal content.
- **C:** Incorrect for this question. Single-task analyzers target one content type or objective. They may be simpler and cheaper than general pro-mode pipelines. Why the correct answer wins: Pro mode handles complex multi-page multimodal content.
- **D:** Incorrect for this question. Custom models fit specialized forms not covered by prebuilts. They require representative labels and retraining discipline. Why the correct answer wins: Pro mode handles complex multi-page multimodal content.

### Question 34 — B, C

Answers: Enforce brand and usage rules for generated visuals; Filter unsafe or disallowed visual content. Brand policy constrains approved visual usage, and visual filters block unsafe imagery. Brand controls define permitted logos, styles, and claims. Technical generation must still pass approval. Image and video safety filters reduce exposure to harmful content. Thresholds and human escalation should match policy. Local study-map skill 3.5 (Multimodal Responsible AI), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Azure AI Vision and Content Understanding documentation: https://learn.microsoft.com/en-us/azure/ai-services/content-understanding/

- **A:** Incorrect for this question. Watermarks support disclosure and traceability. They do not replace usage policy or review. Why the correct answer wins: Brand policy constrains approved visual usage, and visual filters block unsafe imagery.
- **B:** Correct. Image and video safety filters reduce exposure to harmful content. Thresholds and human escalation should match policy. In this case: Brand policy constrains approved visual usage, and visual filters block unsafe imagery.
- **C:** Correct. Brand controls define permitted logos, styles, and claims. Technical generation must still pass approval. In this case: Brand policy constrains approved visual usage, and visual filters block unsafe imagery.
- **D:** Incorrect for this question. Top-p narrows or broadens token sampling. Tune with evaluation rather than by intuition. Why the correct answer wins: Brand policy constrains approved visual usage, and visual filters block unsafe imagery.
- **E:** Incorrect for this question. Lower temperature reduces sampling variability. It does not guarantee factual correctness. Why the correct answer wins: Brand policy constrains approved visual usage, and visual filters block unsafe imagery.

### Question 35 — C

Answer: Prompt for JSON that conforms to a supplied schema. Schema-constrained JSON supports validation and automation. Schema-guided generation improves machine readability. Validate values against source evidence and business rules. Local study-map skill 4.1 (Language Model Text Analysis), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Azure AI Language, Speech, and Translator documentation: https://learn.microsoft.com/en-us/azure/ai-services/

- **A:** Incorrect for this question. Topic extraction supports discovery and grouping. It is not a substitute for an authoritative taxonomy. Why the correct answer wins: Schema-constrained JSON supports validation and automation.
- **B:** Incorrect for this question. Translation should preserve meaning, names, and formatting. Evaluate domain terminology and low-resource languages. Why the correct answer wins: Schema-constrained JSON supports validation and automation.
- **C:** Correct. Schema-guided generation improves machine readability. Validate values against source evidence and business rules. In this case: Schema-constrained JSON supports validation and automation.
- **D:** Incorrect for this question. Summaries should preserve required facts and caveats. Fluency does not prove completeness. Why the correct answer wins: Schema-constrained JSON supports validation and automation.

### Question 36 — A, C

Answers: Detect and redact sensitive personal data; Analyze sentiment and tone with an appropriate service. PII detection finds personal data, and sentiment detects frustration. Sensitive Data Protection or language PII detection can identify and mask data. Verify that redaction covers every path where content flows. Sentiment analysis can support triage and monitoring. Domain and language variation require validation. Local study-map skill 4.1 (Language Model Text Analysis), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Azure AI Language, Speech, and Translator documentation: https://learn.microsoft.com/en-us/azure/ai-services/

- **A:** Correct. Sentiment analysis can support triage and monitoring. Domain and language variation require validation. In this case: PII detection finds personal data, and sentiment detects frustration.
- **B:** Incorrect for this question. Summaries should preserve required facts and caveats. Fluency does not prove completeness. Why the correct answer wins: PII detection finds personal data, and sentiment detects frustration.
- **C:** Correct. Sensitive Data Protection or language PII detection can identify and mask data. Verify that redaction covers every path where content flows. In this case: PII detection finds personal data, and sentiment detects frustration.
- **D:** Incorrect for this question. Glossaries keep product and legal terms consistent. Terms still need human validation in context. Why the correct answer wins: PII detection finds personal data, and sentiment detects frustration.
- **E:** Incorrect for this question. Topic extraction supports discovery and grouping. It is not a substitute for an authoritative taxonomy. Why the correct answer wins: PII detection finds personal data, and sentiment detects frustration.

### Question 37 — A

Answer: Apply a custom glossary or terminology list. A glossary enforces approved term mappings. Glossaries keep product and legal terms consistent. Terms still need human validation in context. Local study-map skill 4.2 (Translation), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Azure AI Language, Speech, and Translator documentation: https://learn.microsoft.com/en-us/azure/ai-services/

- **A:** Correct. Glossaries keep product and legal terms consistent. Terms still need human validation in context. In this case: A glossary enforces approved term mappings.
- **B:** Incorrect for this question. Translation should preserve meaning, names, and formatting. Evaluate domain terminology and low-resource languages. Why the correct answer wins: A glossary enforces approved term mappings.
- **C:** Incorrect for this question. Entity extraction turns text into structured facts. Ambiguous mentions need resolution and validation. Why the correct answer wins: A glossary enforces approved term mappings.
- **D:** Incorrect for this question. Sensitive Data Protection or language PII detection can identify and mask data. Verify that redaction covers every path where content flows. Why the correct answer wins: A glossary enforces approved term mappings.

### Question 38 — D

Answer: Transcribe speech to text with Azure AI Speech. Speech-to-text transcribes audio into searchable content. Speech-to-text enables voice agents and transcript analysis. Audio quality, accents, and domain terms affect accuracy. Local study-map skill 4.3 (Speech Solutions), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Azure AI Language, Speech, and Translator documentation: https://learn.microsoft.com/en-us/azure/ai-services/

- **A:** Incorrect for this question. Audio-capable models can summarize or answer questions about recordings. Verify transcription quality and evidence grounding. Why the correct answer wins: Speech-to-text transcribes audio into searchable content.
- **B:** Incorrect for this question. Text-to-speech supports voice responses and accessibility. Voice, prosody, and latency affect usability. Why the correct answer wins: Speech-to-text transcribes audio into searchable content.
- **C:** Incorrect for this question. Speech translation combines recognition and translation. Preserve timing and speaker context where needed. Why the correct answer wins: Speech-to-text transcribes audio into searchable content.
- **D:** Correct. Speech-to-text enables voice agents and transcript analysis. Audio quality, accents, and domain terms affect accuracy. In this case: Speech-to-text transcribes audio into searchable content.

### Question 39 — A

Answer: Use a custom speech model for specialized vocabulary. A custom speech model adapts to the acoustics and vocabulary of the environment. Custom speech can improve recognition of domain terms. It requires representative audio and ongoing evaluation. Local study-map skill 4.3 (Speech Solutions), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Azure AI Language, Speech, and Translator documentation: https://learn.microsoft.com/en-us/azure/ai-services/

- **A:** Correct. Custom speech can improve recognition of domain terms. It requires representative audio and ongoing evaluation. In this case: A custom speech model adapts to the acoustics and vocabulary of the environment.
- **B:** Incorrect for this question. Speech-to-text enables voice agents and transcript analysis. Audio quality, accents, and domain terms affect accuracy. Why the correct answer wins: A custom speech model adapts to the acoustics and vocabulary of the environment.
- **C:** Incorrect for this question. Text-to-speech supports voice responses and accessibility. Voice, prosody, and latency affect usability. Why the correct answer wins: A custom speech model adapts to the acoustics and vocabulary of the environment.
- **D:** Incorrect for this question. Glossaries keep product and legal terms consistent. Terms still need human validation in context. Why the correct answer wins: A custom speech model adapts to the acoustics and vocabulary of the environment.

### Question 40 — C

Answer: Generate summaries with explicit length and audience constraints. Summarization condenses long content into a shorter form. Summaries should preserve required facts and caveats. Fluency does not prove completeness. Local study-map skill 4.4 (Domain Customization), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Azure AI Language, Speech, and Translator documentation: https://learn.microsoft.com/en-us/azure/ai-services/

- **A:** Incorrect for this question. Entity extraction turns text into structured facts. Ambiguous mentions need resolution and validation. Why the correct answer wins: Summarization condenses long content into a shorter form.
- **B:** Incorrect for this question. Translation should preserve meaning, names, and formatting. Evaluate domain terminology and low-resource languages. Why the correct answer wins: Summarization condenses long content into a shorter form.
- **C:** Correct. Summaries should preserve required facts and caveats. Fluency does not prove completeness. In this case: Summarization condenses long content into a shorter form.
- **D:** Incorrect for this question. Topic extraction supports discovery and grouping. It is not a substitute for an authoritative taxonomy. Why the correct answer wins: Summarization condenses long content into a shorter form.

### Question 41 — A, D

Answers: Customize summaries and extraction for compliance needs; Adapt prompts and models to domain terminology. Compliance summarization preserves required disclosures, and a domain lexicon captures local terminology. Compliance work requires precise citation, retention, and review. Generic summarization is insufficient without controls. Domain adaptation improves consistency and recall. Validate against expert-created expected outputs. Local study-map skill 4.4 (Domain Customization), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Azure AI Language, Speech, and Translator documentation: https://learn.microsoft.com/en-us/azure/ai-services/

- **A:** Correct. Compliance work requires precise citation, retention, and review. Generic summarization is insufficient without controls. In this case: Compliance summarization preserves required disclosures, and a domain lexicon captures local terminology.
- **B:** Incorrect for this question. Topic extraction supports discovery and grouping. It is not a substitute for an authoritative taxonomy. Why the correct answer wins: Compliance summarization preserves required disclosures, and a domain lexicon captures local terminology.
- **C:** Incorrect for this question. Sentiment analysis can support triage and monitoring. Domain and language variation require validation. Why the correct answer wins: Compliance summarization preserves required disclosures, and a domain lexicon captures local terminology.
- **D:** Correct. Domain adaptation improves consistency and recall. Validate against expert-created expected outputs. In this case: Compliance summarization preserves required disclosures, and a domain lexicon captures local terminology.
- **E:** Incorrect for this question. Translation should preserve meaning, names, and formatting. Evaluate domain terminology and low-resource languages. Why the correct answer wins: Compliance summarization preserves required disclosures, and a domain lexicon captures local terminology.

### Question 42 — B

Answer: Use an Azure AI Search indexer to pull source content. An indexer pulls source documents and tracks changes on a schedule. Indexers automate ingestion and can run on a schedule. Monitor failures, deletions, and field mappings. Local study-map skill 5.1 (Content Ingestion and Indexing), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Azure AI Search documentation: https://learn.microsoft.com/en-us/azure/search/

- **A:** Incorrect for this question. Skillsets can OCR, split, embed, and extract during indexing. Each skill adds latency, cost, and failure modes. Why the correct answer wins: An indexer pulls source documents and tracks changes on a schedule.
- **B:** Correct. Indexers automate ingestion and can run on a schedule. Monitor failures, deletions, and field mappings. In this case: An indexer pulls source documents and tracks changes on a schedule.
- **C:** Incorrect for this question. Push ingestion supports near-real-time updates from applications. The app owns batching, retries, and deletion. Why the correct answer wins: An indexer pulls source documents and tracks changes on a schedule.
- **D:** Incorrect for this question. OCR unlocks text in scans and screenshots. Layout and table structure may still require specialized extraction. Why the correct answer wins: An indexer pulls source documents and tracks changes on a schedule.

### Question 43 — B

Answer: Push documents to an index through the data-plane API. Push ingestion sends documents to the index as soon as they are created. Push ingestion supports near-real-time updates from applications. The app owns batching, retries, and deletion. Local study-map skill 5.1 (Content Ingestion and Indexing), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Azure AI Search documentation: https://learn.microsoft.com/en-us/azure/search/

- **A:** Incorrect for this question. Ingestion moves source content into a searchable index. Handle failures, updates, and deletions explicitly. Why the correct answer wins: Push ingestion sends documents to the index as soon as they are created.
- **B:** Correct. Push ingestion supports near-real-time updates from applications. The app owns batching, retries, and deletion. In this case: Push ingestion sends documents to the index as soon as they are created.
- **C:** Incorrect for this question. Indexers automate ingestion and can run on a schedule. Monitor failures, deletions, and field mappings. Why the correct answer wins: Push ingestion sends documents to the index as soon as they are created.
- **D:** Incorrect for this question. Removed content must stop appearing in answers. Test deletion propagation explicitly. Why the correct answer wins: Push ingestion sends documents to the index as soon as they are created.

### Question 44 — D

Answer: Ingest → extract text → chunk → embed → index → retrieve with citations. Extraction, chunking, embedding, and indexing precede retrieval and citation. The supported RAG ingestion order produces searchable, citable evidence. Retrieval cannot work before content is extracted, chunked, embedded, and indexed. Local study-map skill 5.4 (RAG Ingestion and OCR), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Azure AI Search documentation: https://learn.microsoft.com/en-us/azure/search/

- **A:** Incorrect for this question. Retrieval before chunking, embedding, and indexing has nothing searchable to return. Why the correct answer wins: Extraction, chunking, embedding, and indexing precede retrieval and citation.
- **B:** Incorrect for this question. Indexing before extraction or embedding creates an empty or unusable index. Why the correct answer wins: Extraction, chunking, embedding, and indexing precede retrieval and citation.
- **C:** Incorrect for this question. Retrieval is attempted before the index exists and source ingestion is incomplete. Why the correct answer wins: Extraction, chunking, embedding, and indexing precede retrieval and citation.
- **D:** Correct. The supported RAG ingestion order produces searchable, citable evidence. Retrieval cannot work before content is extracted, chunked, embedded, and indexed. In this case: Extraction, chunking, embedding, and indexing precede retrieval and citation.

### Question 45 — C

Answer: Train a custom extraction model on labeled documents. A custom extraction model targets a proprietary layout. Custom models fit specialized forms not covered by prebuilts. They require representative labels and retraining discipline. Local study-map skill 5.6 (Document and Content Extraction), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Azure AI Search documentation: https://learn.microsoft.com/en-us/azure/search/

- **A:** Incorrect for this question. Document Intelligence provides prebuilt and custom extraction for structured documents. Validate field accuracy on representative samples. Why the correct answer wins: A custom extraction model targets a proprietary layout.
- **B:** Incorrect for this question. Analyzers define what to extract and how to return it. Version and test them like application code. Why the correct answer wins: A custom extraction model targets a proprietary layout.
- **C:** Correct. Custom models fit specialized forms not covered by prebuilts. They require representative labels and retraining discipline. In this case: A custom extraction model targets a proprietary layout.
- **D:** Incorrect for this question. Prebuilt models cover invoices, receipts, IDs, and similar formats. Check supported locales and field coverage. Why the correct answer wins: A custom extraction model targets a proprietary layout.

### Question 46 — B

Answer: Apply document-level security filters at query time. Document-level security filters restrict results to the caller's authorized scope. Filters restrict results to content the user may see. They must be enforced before content reaches the model. Local study-map skill 5.2 (Search and Grounding Configuration), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Azure AI Search documentation: https://learn.microsoft.com/en-us/azure/search/

- **A:** Incorrect for this question. A semantic ranker can improve relevance for natural-language queries. It adds cost and latency and should be measured against a baseline. Why the correct answer wins: Document-level security filters restrict results to the caller's authorized scope.
- **B:** Correct. Filters restrict results to content the user may see. They must be enforced before content reaches the model. In this case: Document-level security filters restrict results to the caller's authorized scope.
- **C:** Incorrect for this question. Hybrid search covers exact identifiers and paraphrased meaning together. Fusion and ranking need testing on representative queries. Why the correct answer wins: Document-level security filters restrict results to the caller's authorized scope.
- **D:** Incorrect for this question. Stale content produces outdated answers. Define refresh expectations and test deletion behavior. Why the correct answer wins: Document-level security filters restrict results to the caller's authorized scope.

### Question 47 — B

Answer: Add enrichment skills for text, image, and layout. Enrichment adds derived content to documents during indexing. A skillset can extract entities, captions, and structure during indexing. Enrichment adds cost and failure points that need monitoring. Local study-map skill 5.3 (Enrichment Skills), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Azure AI Search documentation: https://learn.microsoft.com/en-us/azure/search/

- **A:** Incorrect for this question. Indexers automate ingestion and can run on a schedule. Monitor failures, deletions, and field mappings. Why the correct answer wins: Enrichment adds derived content to documents during indexing.
- **B:** Correct. A skillset can extract entities, captions, and structure during indexing. Enrichment adds cost and failure points that need monitoring. In this case: Enrichment adds derived content to documents during indexing.
- **C:** Incorrect for this question. Skillsets can OCR, split, embed, and extract during indexing. Each skill adds latency, cost, and failure modes. Why the correct answer wins: Enrichment adds derived content to documents during indexing.
- **D:** Incorrect for this question. OCR unlocks text in scans and screenshots. Layout and table structure may still require specialized extraction. Why the correct answer wins: Enrichment adds derived content to documents during indexing.

### Question 48 — B

Answer: Use provisioned throughput for predictable high-volume workloads. Provisioned throughput reserves capacity for predictable continuous demand. Provisioned capacity reserves throughput at a committed cost. It fits stable demand, not unpredictable spikes. Local study-map skill 1.4 (Quotas, Scaling, and Cost), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Microsoft Foundry documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/

- **A:** Incorrect for this question. Standard deployments bill per token and scale within quota. They suit spiky or early workloads. Why the correct answer wins: Provisioned throughput reserves capacity for predictable continuous demand.
- **B:** Correct. Provisioned capacity reserves throughput at a committed cost. It fits stable demand, not unpredictable spikes. In this case: Provisioned throughput reserves capacity for predictable continuous demand.
- **C:** Incorrect for this question. Caching can reduce cost and latency for repeated content. Validate correctness and invalidation behavior. Why the correct answer wins: Provisioned throughput reserves capacity for predictable continuous demand.
- **D:** Incorrect for this question. Batch deployments can lower cost for large asynchronous jobs. They are unsuitable for interactive agent turns. Why the correct answer wins: Provisioned throughput reserves capacity for predictable continuous demand.

### Question 49 — D

Answer: Enable tracing across agent, model, and tool calls. Traces show each model and tool call in order, locating the failing step. Traces localize failures and latency in multi-step workflows. Correlate them with evaluation results and deployment versions. Local study-map skill 2.7 (Agent Monitoring and Error Analysis), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Foundry Agent Service documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/agents/

- **A:** Incorrect for this question. Lower temperature reduces sampling variability. It does not guarantee factual correctness. Why the correct answer wins: Traces show each model and tool call in order, locating the failing step.
- **B:** Incorrect for this question. Watermarks support disclosure and traceability. They do not replace usage policy or review. Why the correct answer wins: Traces show each model and tool call in order, locating the failing step.
- **C:** Incorrect for this question. Caching can reduce cost and latency for repeated content. Validate correctness and invalidation behavior. Why the correct answer wins: Traces show each model and tool call in order, locating the failing step.
- **D:** Correct. Traces localize failures and latency in multi-step workflows. Correlate them with evaluation results and deployment versions. In this case: Traces show each model and tool call in order, locating the failing step.

### Question 50 — A

Answer: Persist conversation history in a thread or session. Conversation state preserves identifiers across turns without resending everything. Threads support continuity across turns. Apply retention and access controls to stored history. Local study-map skill 2.5 (Agent Tools, Retrieval, Memory, and Function Calling), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Foundry Agent Service documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/agents/

- **A:** Correct. Threads support continuity across turns. Apply retention and access controls to stored history. In this case: Conversation state preserves identifiers across turns without resending everything.
- **B:** Incorrect for this question. Embeddings determine semantic similarity behavior. Evaluate retrieval quality before and after changes. Why the correct answer wins: Conversation state preserves identifiers across turns without resending everything.
- **C:** Incorrect for this question. Provisioned capacity reserves throughput at a committed cost. It fits stable demand, not unpredictable spikes. Why the correct answer wins: Conversation state preserves identifiers across turns without resending everything.
- **D:** Incorrect for this question. Watermarks support disclosure and traceability. They do not replace usage policy or review. Why the correct answer wins: Conversation state preserves identifiers across turns without resending everything.
