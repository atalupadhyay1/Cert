# Microsoft AI-103 — Full-Length Mock Exam 6

Azure AI Apps and Agents Developer Associate · 50 questions · 120 minutes · passing target 700/1000

Blueprint-weighted mock exam. Item mix: 38 single-choice, 8 multi-select (selection count stated), 4 ordering items rendered as answer choices, and 2 case studies of 3 questions. Hot-area, drag-and-drop UI, labs, and adaptive problem-solution sets cannot be reproduced in a CSV; see the README for the exact fidelity boundary.

Original educational content, not actual, recalled, or copied Microsoft exam items.

## Questions

### 1. A group must standardize on one model that supports text, image, and audio in every operating region. What should be checked first?

Domain: Plan and manage an Azure AI solution

- A. Train or deploy a task-specific model outside the prebuilt catalog
- B. Compare supported models in the Foundry model catalog
- C. Use a small language model for a narrow, high-volume task
- D. Use a general-purpose large language model for complex reasoning

### 2. A business unit wants a model adapted to its own ticket history while keeping the weights under its control. Which option applies?

Domain: Plan and manage an Azure AI solution

- A. Use a general-purpose large language model for complex reasoning
- B. Use a small language model for a narrow, high-volume task
- C. Use a multimodal model for combined text, image, or audio input
- D. Train or deploy a task-specific model outside the prebuilt catalog

### 3. A service desk agent must remember the asset tag discussed earlier in the session. What should be used?

Domain: Plan and manage an Azure AI solution

- A. Use managed conversation state or memory for continuity
- B. Expose a typed function as an agent tool
- C. Use an Azure AI Search indexer to pull source content
- D. Use a vector index for semantic retrieval

### 4. A group must release the same assistant to four subsidiaries with reproducible infrastructure. Which sequence should the team follow?

Domain: Plan and manage an Azure AI solution

- A. Evaluate → provision resources → promote → deploy model → configure app
- B. Configure app → provision resources → deploy model → promote → evaluate
- C. Deploy model → promote → provision resources → evaluate → configure app
- D. Provision resources → deploy model → configure app connection → evaluate → promote

### 5. Regulated subsidiaries require that model traffic never uses the public internet. What should be configured?

Domain: Plan and manage an Azure AI solution

- A. Plan for model quota expressed in tokens and requests per minute
- B. Track cost per accepted task, not only per token
- C. Manage AI resources with infrastructure as code and CI/CD
- D. Use private endpoints and disable public network access

### 6. The assistant is throttled at the start of each business day when every subsidiary logs in. What should be re-planned?

Domain: Plan and manage an Azure AI solution

- A. Plan for model quota expressed in tokens and requests per minute
- B. Monitor input and quality drift over time
- C. Use provisioned throughput for predictable high-volume workloads
- D. Track cost per accepted task, not only per token

### 7. A long, unchanged corporate policy block is resent with every request and dominates spend. What should be enabled?

Domain: Plan and manage an Azure AI solution

- A. Track cost per accepted task, not only per token
- B. Plan for model quota expressed in tokens and requests per minute
- C. Use supported prompt or response caching where appropriate
- D. Monitor input and quality drift over time

### 8. One operations team must see latency, errors, and refusals across all subsidiaries. What should be enabled?

Domain: Plan and manage an Azure AI solution

- A. Preserve audit logs of changes, approvals, and tool actions
- B. Use Azure Monitor and Application Insights for telemetry
- C. Alert on latency, error rate, safety, and cost thresholds
- D. Monitor input and quality drift over time

### 9. A shared model upgrade must not break cases that failed in the last release. What should be run first?

Domain: Plan and manage an Azure AI solution

- A. Compare variants with controlled traffic and shared metrics
- B. Re-run evaluation suites after meaningful changes
- C. Use evaluators for quality, safety, and groundedness
- D. Build a representative golden dataset from real tasks

### 10. Every subsidiary app must authenticate to Foundry without stored secrets. What should each app use?

Domain: Plan and manage an Azure AI solution

- A. Long-lived API key pasted into configuration
- B. Store secrets in Azure Key Vault when keys are unavoidable
- C. Shared connection string with an embedded secret
- D. Authenticate with a managed identity instead of keys

### 11. Consequential customer decisions may not be delegated entirely to the model. Which principle applies?

Domain: Plan and manage an Azure AI solution

- A. Require human approval before consequential actions
- B. Set agent oversight mode and tool-access constraints
- C. Preserve audit logs of changes, approvals, and tool actions
- D. Enforce constraints in code and platform policy

### 12. Each subsidiary must see only its own data and must reach Foundry privately. Which two actions should you take? Select two.

Domain: Plan and manage an Azure AI solution

- A. Use supported prompt or response caching where appropriate
- B. Configure content safety filters for harmful categories
- C. Use private endpoints and disable public network access
- D. Use least-privilege Azure RBAC roles for the workload identity
- E. Store secrets in Azure Key Vault when keys are unavoidable

### 13. A shared customer agent can issue goodwill credits. Which two controls belong in the design? Select two.

Domain: Plan and manage an Azure AI solution

- A. Configure content safety filters for harmful categories
- B. Require human approval before consequential actions
- C. Use a small language model for a narrow, high-volume task
- D. Adjust top-p to control response diversity
- E. Lower temperature for more deterministic extraction

### 14. The assistant must answer from current approved group policies and cite them. Which approach fits?

Domain: Implement generative AI and agentic solutions

- A. Route requests to different models by task difficulty
- B. Ground responses with retrieval-augmented generation
- C. Design multistep workflows with explicit checkpoints
- D. Translate every request before retrieval

### 15. A downstream system needs fixed fields and types from each answer before it can act. What should the model produce?

Domain: Implement generative AI and agentic solutions

- A. Return a defined JSON schema for downstream systems
- B. Use a versioned prompt template with explicit variables
- C. Use supported prompt or response caching where appropriate
- D. Design multistep workflows with explicit checkpoints

### 16. A workflow must classify a request, check entitlement, then respond, in that order. What should the design use?

Domain: Implement generative AI and agentic solutions

- A. One model call with no external retrieval or tool use
- B. Design multistep workflows with explicit checkpoints
- C. Route requests to different models by task difficulty
- D. Limit autonomy with scope, budget, and stop conditions

### 17. Four apps in different languages need supported authentication and retries for Foundry. What should they share?

Domain: Implement generative AI and agentic solutions

- A. Create and run deployments by hand in the portal
- B. Use batch processing for latency-tolerant bulk work
- C. Use a Foundry SDK or supported connector from application code
- D. Manage AI resources with infrastructure as code and CI/CD

### 18. Each subsidiary must call only the deployments approved for its own project. What should each app be configured with?

Domain: Implement generative AI and agentic solutions

- A. Compare supported models in the Foundry model catalog
- B. Use an Azure AI Search indexer to pull source content
- C. Store secrets in Azure Key Vault when keys are unavoidable
- D. Connect the application to the Foundry project endpoint

### 19. The group must compare two prompt designs fairly and keep a stable benchmark. Which two practices are required? Select two.

Domain: Implement generative AI and agentic solutions

- A. Build a representative golden dataset from real tasks
- B. Compare variants with controlled traffic and shared metrics
- C. Lower temperature for more deterministic extraction
- D. Apply watermarks or provenance markers to generated media
- E. Use provisioned throughput for predictable high-volume workloads

### 20. An answer is fluent and on topic but asserts a policy that was never retrieved. Which failure should be measured?

Domain: Implement generative AI and agentic solutions

- A. Measure whether retrieved content and answers address the question
- B. Detect fabricated or unsupported statements
- C. Evaluate structure and logical consistency of responses
- D. Detect tone and sentiment appropriate to the audience

### 21. Every turn must follow the same corporate tone and refusal policy. Where should that guidance live?

Domain: Implement generative AI and agentic solutions

- A. Put stable behavior rules in the system message
- B. Enforce constraints in code and platform policy
- C. Configure content safety filters for harmful categories
- D. Use least-privilege Azure RBAC roles for the workload identity

### 22. Which sequence correctly describes a governed tool call from the group service agent?

Domain: Implement generative AI and agentic solutions

- A. App authorizes → model executes tool → result returns → app validates → model responds
- B. Model responds → app authorizes → tool executes → result returns → app validates
- C. Model requests tool → app validates and authorizes → tool executes → result returns → model responds
- D. Model executes tool → app validates → tool returns result → app authorizes → model responds

### 23. An agent must read a customer's open incidents from a line-of-business API. Which capability performs that lookup?

Domain: Implement generative AI and agentic solutions

- A. Expose a typed function as an agent tool
- B. Ground responses with retrieval-augmented generation
- C. Expose an OpenAPI operation as an agent tool
- D. Use managed conversation state or memory for continuity

### 24. A coordinator must choose among billing, technical, and account specialists and merge their answers. Which pattern fits?

Domain: Implement generative AI and agentic solutions

- A. Transfer control between agents with explicit context
- B. Use self-critique or reflection to improve drafts
- C. Run independent agents concurrently
- D. Use a manager agent to coordinate specialists

### 25. An agent fails only when a request needs two sequential tool calls. What should be inspected?

Domain: Implement generative AI and agentic solutions

- A. Lower temperature for more deterministic extraction
- B. Use supported prompt or response caching where appropriate
- C. Apply watermarks or provenance markers to generated media
- D. Enable tracing across agent, model, and tool calls

### 26. The intent router returns different categories for the same submitted message on retry. Which setting should be lowered?

Domain: Implement generative AI and agentic solutions

- A. Adjust top-p to control response diversity
- B. Use supported prompt or response caching where appropriate
- C. Lower temperature for more deterministic extraction
- D. Route requests to different models by task difficulty

### 27. Operations must learn within minutes when refusal rates spike. What should be configured?

Domain: Implement generative AI and agentic solutions

- A. Monitor input and quality drift over time
- B. Alert on latency, error rate, safety, and cost thresholds
- C. Preserve audit logs of changes, approvals, and tool actions
- D. Use Azure Monitor and Application Insights for telemetry

### 28. A group needs an original illustration for a safety campaign. Which capability applies?

Domain: Implement computer vision solutions

- A. Edit a region of an image with a mask
- B. Generate alt text aligned to accessibility guidance
- C. Generate video from text or reference media
- D. Generate images from text and reference media

### 29. A photograph must have an outdated sign replaced while the people in it stay unchanged. What should be used?

Domain: Implement computer vision solutions

- A. Apply prompt-driven image modifications
- B. Edit a region of an image with a mask
- C. Generate concise or detailed image captions
- D. Edit generated video segments

### 30. A team must find the timestamp in recorded footage when a queue exceeds a threshold. Which capability applies?

Domain: Implement computer vision solutions

- A. Generate concise or detailed image captions
- B. Edit generated video segments
- C. Analyze video segments for events and content
- D. Generate video from text or reference media

### 31. The corporate site needs image descriptions for search and for screen readers. Which two capabilities apply? Select two.

Domain: Implement computer vision solutions

- A. Use provisioned throughput for predictable high-volume workloads
- B. Lower temperature for more deterministic extraction
- C. Generate concise or detailed image captions
- D. Generate alt text aligned to accessibility guidance
- E. Apply watermarks or provenance markers to generated media

### 32. Mixed supplier packets contain photos, tables, and handwriting across many pages. Which Content Understanding mode should be evaluated?

Domain: Implement computer vision solutions

- A. Train a custom extraction model on labeled documents
- B. Use single-task mode for a focused extraction scenario
- C. Use pro mode for complex multimodal content understanding
- D. Use Azure AI Document Intelligence for forms and documents

### 33. Generated images appear in external communications and must be identifiable and on-brand. Which two controls apply? Select two.

Domain: Implement computer vision solutions

- A. Apply watermarks or provenance markers to generated media
- B. Lower temperature for more deterministic extraction
- C. Use supported prompt or response caching where appropriate
- D. Adjust top-p to control response diversity
- E. Enforce brand and usage rules for generated visuals

### 34. An assistant reads scanned letters, one of which instructs it to reveal another customer's contract. What risk is this?

Domain: Implement computer vision solutions

- A. Apply watermarks or provenance markers to generated media
- B. Treat text embedded in images as untrusted input
- C. Filter unsafe or disallowed visual content
- D. Generate concise or detailed image captions

### 35. A ticketing system requires fixed field names and types from each complaint. What should the prompt request?

Domain: Implement text analysis solutions

- A. Prompt for JSON that conforms to a supplied schema
- B. Generate summaries with explicit length and audience constraints
- C. Identify topics or key phrases for navigation
- D. Use Azure Translator or a language model for translation

### 36. A shared mailbox must find personal data and detect rising frustration. Which two analyses apply? Select two.

Domain: Implement text analysis solutions

- A. Generate summaries with explicit length and audience constraints
- B. Analyze sentiment and tone with an appropriate service
- C. Detect and redact sensitive personal data
- D. Apply a custom glossary or terminology list
- E. Identify topics or key phrases for navigation

### 37. Translations keep mangling approved product and legal names. What should be configured?

Domain: Implement text analysis solutions

- A. Apply a custom glossary or terminology list
- B. Use Azure Translator or a language model for translation
- C. Extract entities with defined types and boundaries
- D. Detect and redact sensitive personal data

### 38. Notices must appear in ten languages while retaining statutory wording. Which two practices help? Select two.

Domain: Implement text analysis solutions

- A. Customize summaries and extraction for compliance needs
- B. Use Azure Translator or a language model for translation
- C. Generate summaries with explicit length and audience constraints
- D. Extract entities with defined types and boundaries
- E. Identify topics or key phrases for navigation

### 39. A customer speaks Portuguese and must hear an answer in Portuguese. Which sequence is correct?

Domain: Implement text analysis solutions

- A. Capture audio → synthesize speech → transcribe → translate → return audio
- B. Transcribe → synthesize speech → capture audio → translate → return audio
- C. Capture audio → transcribe → translate text → synthesize speech → return audio
- D. Translate audio → transcribe → capture audio → synthesize → return audio

### 40. Recorded service calls must become searchable transcripts. Which capability applies?

Domain: Implement text analysis solutions

- A. Generate concise or detailed image captions
- B. Transcribe speech to text with Azure AI Speech
- C. Translate spoken language with speech translation
- D. Synthesize speech with Azure AI Speech

### 41. Extraction misses internal abbreviations used by only one subsidiary. What should be added?

Domain: Implement text analysis solutions

- A. Use Azure Translator or a language model for translation
- B. Detect and redact sensitive personal data
- C. Apply a custom glossary or terminology list
- D. Adapt prompts and models to domain terminology

### 42. An index must follow documents added to storage without custom code. What should be used?

Domain: Implement information extraction solutions

- A. Apply OCR to convert images and scans into usable text
- B. Add an enrichment skillset to an indexing pipeline
- C. Use an Azure AI Search indexer to pull source content
- D. Push documents to an index through the data-plane API

### 43. Subsidiaries share one index, and each must see only its own approved documents. What must be enforced?

Domain: Implement information extraction solutions

- A. Apply semantic ranking to reorder search results
- B. Verify index freshness and deletion propagation
- C. Apply document-level security filters at query time
- D. Combine keyword and vector retrieval

### 44. Which sequence correctly builds a citable retrieval pipeline over group policies?

Domain: Implement information extraction solutions

- A. Ingest → extract text → chunk → embed → index → retrieve with citations
- B. Chunk → embed → ingest → retrieve → index → cite
- C. Ingest → retrieve → chunk → embed → index → cite
- D. Index → retrieve → ingest → chunk → embed → cite

---

## Case study — GroupAssist

The next three questions refer to this scenario. Read the full scenario before answering; case-study items are scored individually.

### 45. One subsidiary runs continuous, predictable volume and cannot tolerate throttling. Which capacity option should be evaluated?

Domain: Plan and manage an Azure AI solution

- A. Use supported prompt or response caching where appropriate
- B. Use a standard pay-as-you-go model deployment for variable demand
- C. Use provisioned throughput for predictable high-volume workloads
- D. Use batch processing for latency-tolerant bulk work

### 46. Auditors must verify each answer against an approved policy page. Which capability makes that possible?

Domain: Implement generative AI and agentic solutions

- A. Apply watermarks or provenance markers to generated media
- B. Use supported prompt or response caching where appropriate
- C. Lower temperature for more deterministic extraction
- D. Require citations tied to retrieved evidence

### 47. Long policy evidence crowds out the question and the model starts drifting. What should be configured?

Domain: Implement information extraction solutions

- A. Rerank retrieved passages before generation
- B. Select evidence within the model's usable context
- C. Remove near-duplicate evidence before ranking
- D. Use a vector index for semantic retrieval

---

## Case study — WarrantyDesk

The next three questions refer to this scenario. Read the full scenario before answering; case-study items are scored individually.

### 48. A warranty agent must keep a case number across turns and check it in a claims system. Which two capabilities are required? Select two.

Domain: Implement generative AI and agentic solutions

- A. Persist conversation history in a thread or session
- B. Expose a typed function as an agent tool
- C. Apply watermarks or provenance markers to generated media
- D. Use provisioned throughput for predictable high-volume workloads
- E. Choose an embedding model suited to the content and language

### 49. One subsidiary uses a proprietary claim form that no prebuilt model covers. What should be built?

Domain: Implement information extraction solutions

- A. Configure a Content Understanding analyzer for the content type
- B. Use Azure AI Document Intelligence for forms and documents
- C. Train a custom extraction model on labeled documents
- D. Use a prebuilt document model for common document types

### 50. Every indexed policy must gain extracted entities and a summary during ingestion. Which component defines those steps?

Domain: Implement information extraction solutions

- A. Add an enrichment skillset to an indexing pipeline
- B. Add enrichment skills for text, image, and layout
- C. Apply OCR to convert images and scans into usable text
- D. Push documents to an index through the data-plane API

---

## Answer key and explanations

### Question 1 — B

Answer: Compare supported models in the Foundry model catalog. The catalog records modality support, regional availability, and lifecycle for each model. The catalog shows supported models with capability, modality, region, and lifecycle details. Verify availability for your subscription and region before designing around one model. Local study-map skill 1.1 (Selecting Foundry Models and Services), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Microsoft Foundry documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/

- **A:** Incorrect for this question. A custom model is justified when supported prebuilt options cannot meet a defined requirement. It adds data, evaluation, and lifecycle obligations. Why the correct answer wins: The catalog records modality support, regional availability, and lifecycle for each model.
- **B:** Correct. The catalog shows supported models with capability, modality, region, and lifecycle details. Verify availability for your subscription and region before designing around one model. In this case: The catalog records modality support, regional availability, and lifecycle for each model.
- **C:** Incorrect for this question. Small models can reduce latency and cost for constrained classification or extraction. Confirm quality on representative data before standardizing. Why the correct answer wins: The catalog records modality support, regional availability, and lifecycle for each model.
- **D:** Incorrect for this question. Large models handle ambiguity and multi-step reasoning better in many cases, at higher cost and latency. Select with measured evidence rather than brand preference. Why the correct answer wins: The catalog records modality support, regional availability, and lifecycle for each model.

### Question 2 — D

Answer: Train or deploy a task-specific model outside the prebuilt catalog. A custom or fine-tuned model is trained on organization data under its governance. A custom model is justified when supported prebuilt options cannot meet a defined requirement. It adds data, evaluation, and lifecycle obligations. Local study-map skill 1.1 (Selecting Foundry Models and Services), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Microsoft Foundry documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/

- **A:** Incorrect for this question. Large models handle ambiguity and multi-step reasoning better in many cases, at higher cost and latency. Select with measured evidence rather than brand preference. Why the correct answer wins: A custom or fine-tuned model is trained on organization data under its governance.
- **B:** Incorrect for this question. Small models can reduce latency and cost for constrained classification or extraction. Confirm quality on representative data before standardizing. Why the correct answer wins: A custom or fine-tuned model is trained on organization data under its governance.
- **C:** Incorrect for this question. Multimodal models accept more than one content type in a request. Validate extraction and grounding quality for each modality used. Why the correct answer wins: A custom or fine-tuned model is trained on organization data under its governance.
- **D:** Correct. A custom model is justified when supported prebuilt options cannot meet a defined requirement. It adds data, evaluation, and lifecycle obligations. In this case: A custom or fine-tuned model is trained on organization data under its governance.

### Question 3 — A

Answer: Use managed conversation state or memory for continuity. Conversation state keeps previous turns available to the agent. Managed state supports multi-turn continuity without rebuilding history manually. Retention, isolation, and user control still need design. Local study-map skill 1.2 (Retrieval, Memory, Tool, and Knowledge Services), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Microsoft Foundry documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/

- **A:** Correct. Managed state supports multi-turn continuity without rebuilding history manually. Retention, isolation, and user control still need design. In this case: Conversation state keeps previous turns available to the agent.
- **B:** Incorrect for this question. Function tools let the agent request a defined operation with structured arguments. Authorization and input validation must be enforced server-side. Why the correct answer wins: Conversation state keeps previous turns available to the agent.
- **C:** Incorrect for this question. Indexers automate ingestion and can run on a schedule. Monitor failures, deletions, and field mappings. Why the correct answer wins: Conversation state keeps previous turns available to the agent.
- **D:** Incorrect for this question. Embeddings support similarity search over meaning rather than exact terms. Vector search still needs chunking, filtering, and evaluation. Why the correct answer wins: Conversation state keeps previous turns available to the agent.

### Question 4 — D

Answer: Provision resources → deploy model → configure app connection → evaluate → promote. Provisioning and deployment come first, configuration follows, and evaluation gates promotion. Provisioning and deployment precede app configuration, and evaluation gates promotion. Local study-map skill 1.3 (Infrastructure, Deployment, and CI/CD), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Microsoft Foundry documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/

- **A:** Incorrect for this question. Evaluation before any deployment or configuration has nothing meaningful to assess. Why the correct answer wins: Provisioning and deployment come first, configuration follows, and evaluation gates promotion.
- **B:** Incorrect for this question. Evaluation after promotion cannot gate the release. Why the correct answer wins: Provisioning and deployment come first, configuration follows, and evaluation gates promotion.
- **C:** Incorrect for this question. Promotion before provisioning and evaluation skips the controls that make deployment safe. Why the correct answer wins: Provisioning and deployment come first, configuration follows, and evaluation gates promotion.
- **D:** Correct. Provisioning and deployment precede app configuration, and evaluation gates promotion. In this case: Provisioning and deployment come first, configuration follows, and evaluation gates promotion.

### Question 5 — D

Answer: Use private endpoints and disable public network access. A private endpoint keeps model traffic on the private network path. Private connectivity keeps service traffic on approved network paths. Pair it with private DNS so clients resolve the private address. Local study-map skill 1.3 (Infrastructure, Deployment, and CI/CD), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Microsoft Foundry documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/

- **A:** Incorrect for this question. Quota limits throughput regardless of application capacity. Request increases in advance and plan graceful degradation. Why the correct answer wins: A private endpoint keeps model traffic on the private network path.
- **B:** Incorrect for this question. Retries, tool calls, evaluation, and review contribute to unit economics. Per-outcome cost supports better optimization. Why the correct answer wins: A private endpoint keeps model traffic on the private network path.
- **C:** Incorrect for this question. Repeatable deployments reduce configuration drift. Include model deployments, indexes, and connections in review and promotion. Why the correct answer wins: A private endpoint keeps model traffic on the private network path.
- **D:** Correct. Private connectivity keeps service traffic on approved network paths. Pair it with private DNS so clients resolve the private address. In this case: A private endpoint keeps model traffic on the private network path.

### Question 6 — A

Answer: Plan for model quota expressed in tokens and requests per minute. Request and token quota must cover the real peak concurrency. Quota limits throughput regardless of application capacity. Request increases in advance and plan graceful degradation. Local study-map skill 1.4 (Quotas, Scaling, and Cost), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Microsoft Foundry documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/

- **A:** Correct. Quota limits throughput regardless of application capacity. Request increases in advance and plan graceful degradation. In this case: Request and token quota must cover the real peak concurrency.
- **B:** Incorrect for this question. User behavior, data, and models change. Rolling baselines reveal degradation that a one-time evaluation misses. Why the correct answer wins: Request and token quota must cover the real peak concurrency.
- **C:** Incorrect for this question. Provisioned capacity reserves throughput at a committed cost. It fits stable demand, not unpredictable spikes. Why the correct answer wins: Request and token quota must cover the real peak concurrency.
- **D:** Incorrect for this question. Retries, tool calls, evaluation, and review contribute to unit economics. Per-outcome cost supports better optimization. Why the correct answer wins: Request and token quota must cover the real peak concurrency.

### Question 7 — A

Answer: Track cost per accepted task, not only per token. Prompt caching reuses the repeated policy prefix instead of re-billing it. Retries, tool calls, evaluation, and review contribute to unit economics. Per-outcome cost supports better optimization. Local study-map skill 1.4 (Quotas, Scaling, and Cost), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Microsoft Foundry documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/

- **A:** Correct. Retries, tool calls, evaluation, and review contribute to unit economics. Per-outcome cost supports better optimization. In this case: Prompt caching reuses the repeated policy prefix instead of re-billing it.
- **B:** Incorrect for this question. Quota limits throughput regardless of application capacity. Request increases in advance and plan graceful degradation. Why the correct answer wins: Prompt caching reuses the repeated policy prefix instead of re-billing it.
- **C:** Incorrect for this question. Caching can reduce cost and latency for repeated content. Validate correctness and invalidation behavior. Why the correct answer wins: Prompt caching reuses the repeated policy prefix instead of re-billing it.
- **D:** Incorrect for this question. User behavior, data, and models change. Rolling baselines reveal degradation that a one-time evaluation misses. Why the correct answer wins: Prompt caching reuses the repeated policy prefix instead of re-billing it.

### Question 8 — B

Answer: Use Azure Monitor and Application Insights for telemetry. Platform monitoring centralizes metrics and logs for operations. Central telemetry captures latency, errors, dependencies, and custom events. Redact sensitive content before logging. Local study-map skill 1.5 (Monitoring Performance, Drift, Safety, and Grounding), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Microsoft Foundry documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/

- **A:** Incorrect for this question. Audit evidence supports investigation and accountability. Protect log integrity and retention. Why the correct answer wins: Platform monitoring centralizes metrics and logs for operations.
- **B:** Correct. Central telemetry captures latency, errors, dependencies, and custom events. Redact sensitive content before logging. In this case: Platform monitoring centralizes metrics and logs for operations.
- **C:** Incorrect for this question. Alerts turn monitoring into action. Route them to an accountable owner with a runbook. Why the correct answer wins: Platform monitoring centralizes metrics and logs for operations.
- **D:** Incorrect for this question. User behavior, data, and models change. Rolling baselines reveal degradation that a one-time evaluation misses. Why the correct answer wins: Platform monitoring centralizes metrics and logs for operations.

### Question 9 — B

Answer: Re-run evaluation suites after meaningful changes. Regression evaluation re-runs known failure cases against the candidate. Prompts, models, indexes, and tools all affect behavior. Regression tests catch unintended effects. Local study-map skill 1.5 (Monitoring Performance, Drift, Safety, and Grounding), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Microsoft Foundry documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/

- **A:** Incorrect for this question. Controlled comparison supports evidence-based change. Avoid changing several variables at once. Why the correct answer wins: Regression evaluation re-runs known failure cases against the candidate.
- **B:** Correct. Prompts, models, indexes, and tools all affect behavior. Regression tests catch unintended effects. In this case: Regression evaluation re-runs known failure cases against the candidate.
- **C:** Incorrect for this question. Evaluators provide repeatable signals across models and prompts. They must be calibrated against human judgment for high-impact work. Why the correct answer wins: Regression evaluation re-runs known failure cases against the candidate.
- **D:** Incorrect for this question. A golden set anchors evaluation in expected behavior. Include edge cases and high-risk scenarios. Why the correct answer wins: Regression evaluation re-runs known failure cases against the candidate.

### Question 10 — D

Answer: Authenticate with a managed identity instead of keys. A managed identity obtains Entra ID tokens without stored credentials. Managed identities avoid embedded secrets and support role-based access. Assign only required data-plane roles. Local study-map skill 1.6 (Security, Identity, and Networking), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Microsoft Foundry documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/

- **A:** Incorrect for this question. Static keys are easily leaked, hard to rotate across services, and provide no per-identity authorization. Why the correct answer wins: A managed identity obtains Entra ID tokens without stored credentials.
- **B:** Incorrect for this question. A managed secret store supports rotation and access control. Secrets should never appear in prompts, code, or logs. Why the correct answer wins: A managed identity obtains Entra ID tokens without stored credentials.
- **C:** Incorrect for this question. A shared secret grants broad access, cannot be scoped per workload, and complicates rotation and auditing. Why the correct answer wins: A managed identity obtains Entra ID tokens without stored credentials.
- **D:** Correct. Managed identities avoid embedded secrets and support role-based access. Assign only required data-plane roles. In this case: A managed identity obtains Entra ID tokens without stored credentials.

### Question 11 — B

Answer: Set agent oversight mode and tool-access constraints. Human oversight keeps consequential decisions accountable to people. Oversight settings bound what an agent may do autonomously. They should be tested against realistic misuse and failure. Local study-map skill 1.7 (Responsible AI Controls and Oversight), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Microsoft Foundry documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/

- **A:** Incorrect for this question. Approval must occur before the effect and identify who approved what. A model confidence score is not approval. Why the correct answer wins: Human oversight keeps consequential decisions accountable to people.
- **B:** Correct. Oversight settings bound what an agent may do autonomously. They should be tested against realistic misuse and failure. In this case: Human oversight keeps consequential decisions accountable to people.
- **C:** Incorrect for this question. Audit evidence supports investigation and accountability. Protect log integrity and retention. Why the correct answer wins: Human oversight keeps consequential decisions accountable to people.
- **D:** Incorrect for this question. Guardrails are technical controls, not prompt suggestions. Validate inputs, authorize tools, and limit egress. Why the correct answer wins: Human oversight keeps consequential decisions accountable to people.

### Question 12 — C, D

Answers: Use least-privilege Azure RBAC roles for the workload identity; Use private endpoints and disable public network access. Least-privilege role assignment scopes access, and private endpoints remove public exposure. Roles should match the operations the app or agent performs. Broad contributor access increases blast radius. Private connectivity keeps service traffic on approved network paths. Pair it with private DNS so clients resolve the private address. Local study-map skill 1.6 (Security, Identity, and Networking), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Microsoft Foundry documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/

- **A:** Incorrect for this question. Caching can reduce cost and latency for repeated content. Validate correctness and invalidation behavior. Why the correct answer wins: Least-privilege role assignment scopes access, and private endpoints remove public exposure.
- **B:** Incorrect for this question. Filters assign severity and can block or annotate content. Thresholds should reflect the use case and applicable policy. Why the correct answer wins: Least-privilege role assignment scopes access, and private endpoints remove public exposure.
- **C:** Correct. Private connectivity keeps service traffic on approved network paths. Pair it with private DNS so clients resolve the private address. In this case: Least-privilege role assignment scopes access, and private endpoints remove public exposure.
- **D:** Correct. Roles should match the operations the app or agent performs. Broad contributor access increases blast radius. In this case: Least-privilege role assignment scopes access, and private endpoints remove public exposure.
- **E:** Incorrect for this question. A managed secret store supports rotation and access control. Secrets should never appear in prompts, code, or logs. Why the correct answer wins: Least-privilege role assignment scopes access, and private endpoints remove public exposure.

### Question 13 — A, B

Answers: Configure content safety filters for harmful categories; Require human approval before consequential actions. Content filters reduce harmful output, and approval gates control credit issuance. Filters assign severity and can block or annotate content. Thresholds should reflect the use case and applicable policy. Approval must occur before the effect and identify who approved what. A model confidence score is not approval. Local study-map skill 1.7 (Responsible AI Controls and Oversight), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Microsoft Foundry documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/

- **A:** Correct. Filters assign severity and can block or annotate content. Thresholds should reflect the use case and applicable policy. In this case: Content filters reduce harmful output, and approval gates control credit issuance.
- **B:** Correct. Approval must occur before the effect and identify who approved what. A model confidence score is not approval. In this case: Content filters reduce harmful output, and approval gates control credit issuance.
- **C:** Incorrect for this question. Small models can reduce latency and cost for constrained classification or extraction. Confirm quality on representative data before standardizing. Why the correct answer wins: Content filters reduce harmful output, and approval gates control credit issuance.
- **D:** Incorrect for this question. Top-p narrows or broadens token sampling. Tune with evaluation rather than by intuition. Why the correct answer wins: Content filters reduce harmful output, and approval gates control credit issuance.
- **E:** Incorrect for this question. Lower temperature reduces sampling variability. It does not guarantee factual correctness. Why the correct answer wins: Content filters reduce harmful output, and approval gates control credit issuance.

### Question 14 — B

Answer: Ground responses with retrieval-augmented generation. RAG retrieves current approved evidence and supports citations. RAG supplies selected source content at request time so answers can cite current evidence. It reduces but does not eliminate fabrication. Local study-map skill 2.1 (Building Generative Applications), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Foundry Agent Service documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/agents/

- **A:** Incorrect for this question. Routing can balance quality and cost. Fallback and evaluation are required. Why the correct answer wins: RAG retrieves current approved evidence and supports citations.
- **B:** Correct. RAG supplies selected source content at request time so answers can cite current evidence. It reduces but does not eliminate fabrication. In this case: RAG retrieves current approved evidence and supports citations.
- **C:** Incorrect for this question. Checkpoints validate intermediate results before later steps depend on them. This limits error propagation. Why the correct answer wins: RAG retrieves current approved evidence and supports citations.
- **D:** Incorrect for this question. Translating the request does not replace retrieval, grounding, or validation, so it cannot satisfy an evidence or citation requirement. Why the correct answer wins: RAG retrieves current approved evidence and supports citations.

### Question 15 — A

Answer: Return a defined JSON schema for downstream systems. Schema-constrained output supports validation and automation. Structured output supports validation and automation. Schema validity does not prove semantic correctness. Local study-map skill 2.1 (Building Generative Applications), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Foundry Agent Service documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/agents/

- **A:** Correct. Structured output supports validation and automation. Schema validity does not prove semantic correctness. In this case: Schema-constrained output supports validation and automation.
- **B:** Incorrect for this question. Templates improve consistency and reviewability. Version them and test changes. Why the correct answer wins: Schema-constrained output supports validation and automation.
- **C:** Incorrect for this question. Caching can reduce cost and latency for repeated content. Validate correctness and invalidation behavior. Why the correct answer wins: Schema-constrained output supports validation and automation.
- **D:** Incorrect for this question. Checkpoints validate intermediate results before later steps depend on them. This limits error propagation. Why the correct answer wins: Schema-constrained output supports validation and automation.

### Question 16 — B

Answer: Design multistep workflows with explicit checkpoints. Explicit stages with checkpoints keep unverified steps from completing. Checkpoints validate intermediate results before later steps depend on them. This limits error propagation. Local study-map skill 2.1 (Building Generative Applications), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Foundry Agent Service documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/agents/

- **A:** Incorrect for this question. A single call cannot validate intermediate results or fetch authoritative evidence, so it is unsuitable for multi-stage or grounded workflows. Why the correct answer wins: Explicit stages with checkpoints keep unverified steps from completing.
- **B:** Correct. Checkpoints validate intermediate results before later steps depend on them. This limits error propagation. In this case: Explicit stages with checkpoints keep unverified steps from completing.
- **C:** Incorrect for this question. Routing can balance quality and cost. Fallback and evaluation are required. Why the correct answer wins: Explicit stages with checkpoints keep unverified steps from completing.
- **D:** Incorrect for this question. Autonomous workflows need bounded actions and escalation. Unbounded loops and broad tools increase risk. Why the correct answer wins: Explicit stages with checkpoints keep unverified steps from completing.

### Question 17 — C

Answer: Use a Foundry SDK or supported connector from application code. A supported Foundry SDK provides maintained client behaviour per language. SDKs provide supported request and response patterns. Pin versions and handle retries, timeouts, and errors explicitly. Local study-map skill 2.2 (Foundry SDK and Project Integration), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Foundry Agent Service documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/agents/

- **A:** Incorrect for this question. Manual portal changes work for exploration but are slow, undocumented, and hard to reproduce, so they are a poor fit for governed release processes. Why the correct answer wins: A supported Foundry SDK provides maintained client behaviour per language.
- **B:** Incorrect for this question. Batch deployments can lower cost for large asynchronous jobs. They are unsuitable for interactive agent turns. Why the correct answer wins: A supported Foundry SDK provides maintained client behaviour per language.
- **C:** Correct. SDKs provide supported request and response patterns. Pin versions and handle retries, timeouts, and errors explicitly. In this case: A supported Foundry SDK provides maintained client behaviour per language.
- **D:** Incorrect for this question. Repeatable deployments reduce configuration drift. Include model deployments, indexes, and connections in review and promotion. Why the correct answer wins: A supported Foundry SDK provides maintained client behaviour per language.

### Question 18 — D

Answer: Connect the application to the Foundry project endpoint. The project endpoint binds the client to that project and its deployments. Project endpoints and SDK clients bind an app to approved models and resources. Use identity-based authentication and environment-specific configuration. Local study-map skill 2.2 (Foundry SDK and Project Integration), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Foundry Agent Service documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/agents/

- **A:** Incorrect for this question. The catalog shows supported models with capability, modality, region, and lifecycle details. Verify availability for your subscription and region before designing around one model. Why the correct answer wins: The project endpoint binds the client to that project and its deployments.
- **B:** Incorrect for this question. Indexers automate ingestion and can run on a schedule. Monitor failures, deletions, and field mappings. Why the correct answer wins: The project endpoint binds the client to that project and its deployments.
- **C:** Incorrect for this question. A managed secret store supports rotation and access control. Secrets should never appear in prompts, code, or logs. Why the correct answer wins: The project endpoint binds the client to that project and its deployments.
- **D:** Correct. Project endpoints and SDK clients bind an app to approved models and resources. Use identity-based authentication and environment-specific configuration. In this case: The project endpoint binds the client to that project and its deployments.

### Question 19 — A, B

Answers: Build a representative golden dataset from real tasks; Compare variants with controlled traffic and shared metrics. A golden dataset holds the benchmark, and an A/B test compares variants against it. A golden set anchors evaluation in expected behavior. Include edge cases and high-risk scenarios. Controlled comparison supports evidence-based change. Avoid changing several variables at once. Local study-map skill 2.3 (Evaluating Models and Applications), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Foundry Agent Service documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/agents/

- **A:** Correct. A golden set anchors evaluation in expected behavior. Include edge cases and high-risk scenarios. In this case: A golden dataset holds the benchmark, and an A/B test compares variants against it.
- **B:** Correct. Controlled comparison supports evidence-based change. Avoid changing several variables at once. In this case: A golden dataset holds the benchmark, and an A/B test compares variants against it.
- **C:** Incorrect for this question. Lower temperature reduces sampling variability. It does not guarantee factual correctness. Why the correct answer wins: A golden dataset holds the benchmark, and an A/B test compares variants against it.
- **D:** Incorrect for this question. Watermarks support disclosure and traceability. They do not replace usage policy or review. Why the correct answer wins: A golden dataset holds the benchmark, and an A/B test compares variants against it.
- **E:** Incorrect for this question. Provisioned capacity reserves throughput at a committed cost. It fits stable demand, not unpredictable spikes. Why the correct answer wins: A golden dataset holds the benchmark, and an A/B test compares variants against it.

### Question 20 — B

Answer: Detect fabricated or unsupported statements. Fabrication measures claims unsupported by evidence. Fabrication checks compare claims with evidence. Fluency and confidence are not evidence of accuracy. Local study-map skill 2.3 (Evaluating Models and Applications), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Foundry Agent Service documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/agents/

- **A:** Incorrect for this question. Relevance covers both retrieval and response usefulness. A correct but off-topic answer still fails. Why the correct answer wins: Fabrication measures claims unsupported by evidence.
- **B:** Correct. Fabrication checks compare claims with evidence. Fluency and confidence are not evidence of accuracy. In this case: Fabrication measures claims unsupported by evidence.
- **C:** Incorrect for this question. Coherence checks readability and internal consistency. It does not establish factual accuracy. Why the correct answer wins: Fabrication measures claims unsupported by evidence.
- **D:** Incorrect for this question. Tone analysis supports brand and customer communication. Context and culture affect interpretation. Why the correct answer wins: Fabrication measures claims unsupported by evidence.

### Question 21 — A

Answer: Put stable behavior rules in the system message. The system message carries persistent behavioural guidance. System messages define role and constraints. They are not a security boundary against injection. Local study-map skill 2.4 (Agent Roles, Goals, and Tool Schemas), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Foundry Agent Service documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/agents/

- **A:** Correct. System messages define role and constraints. They are not a security boundary against injection. In this case: The system message carries persistent behavioural guidance.
- **B:** Incorrect for this question. Guardrails are technical controls, not prompt suggestions. Validate inputs, authorize tools, and limit egress. Why the correct answer wins: The system message carries persistent behavioural guidance.
- **C:** Incorrect for this question. Filters assign severity and can block or annotate content. Thresholds should reflect the use case and applicable policy. Why the correct answer wins: The system message carries persistent behavioural guidance.
- **D:** Incorrect for this question. Roles should match the operations the app or agent performs. Broad contributor access increases blast radius. Why the correct answer wins: The system message carries persistent behavioural guidance.

### Question 22 — C

Answer: Model requests tool → app validates and authorizes → tool executes → result returns → model responds. The application validates and authorizes the call before any tool executes. Tool execution authority belongs to the application, which validates and authorizes before acting. Local study-map skill 2.5 (Agent Tools, Retrieval, Memory, and Function Calling), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Foundry Agent Service documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/agents/

- **A:** Incorrect for this question. Execution must follow validation, and the model is not the execution boundary. Why the correct answer wins: The application validates and authorizes the call before any tool executes.
- **B:** Incorrect for this question. The response cannot precede the tool action and validation. Why the correct answer wins: The application validates and authorizes the call before any tool executes.
- **C:** Correct. Tool execution authority belongs to the application, which validates and authorizes before acting. In this case: The application validates and authorizes the call before any tool executes.
- **D:** Incorrect for this question. The model cannot execute the tool, and authorization after execution is too late. Why the correct answer wins: The application validates and authorizes the call before any tool executes.

### Question 23 — A

Answer: Expose a typed function as an agent tool. A function tool calls the business API under application authorization. Function tools let the agent request a defined operation with structured arguments. Authorization and input validation must be enforced server-side. Local study-map skill 2.5 (Agent Tools, Retrieval, Memory, and Function Calling), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Foundry Agent Service documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/agents/

- **A:** Correct. Function tools let the agent request a defined operation with structured arguments. Authorization and input validation must be enforced server-side. In this case: A function tool calls the business API under application authorization.
- **B:** Incorrect for this question. RAG supplies selected source content at request time so answers can cite current evidence. It reduces but does not eliminate fabrication. Why the correct answer wins: A function tool calls the business API under application authorization.
- **C:** Incorrect for this question. OpenAPI tools describe supported HTTP operations for agent use. Narrow operations, validate inputs, and authenticate the caller. Why the correct answer wins: A function tool calls the business API under application authorization.
- **D:** Incorrect for this question. Managed state supports multi-turn continuity without rebuilding history manually. Retention, isolation, and user control still need design. Why the correct answer wins: A function tool calls the business API under application authorization.

### Question 24 — D

Answer: Use a manager agent to coordinate specialists. A manager agent routes to specialists and consolidates their replies. A manager routes tasks and merges results. Clear responsibility and failure handling are required. Local study-map skill 2.6 (Multi-Agent Orchestration and Safeguards), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Foundry Agent Service documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/agents/

- **A:** Incorrect for this question. Handoffs should carry goal, evidence, permissions, and open questions. Implicit context is easily lost. Why the correct answer wins: A manager agent routes to specialists and consolidates their replies.
- **B:** Incorrect for this question. Reflection can catch omissions and inconsistencies. It can also reinforce errors, so validate against evidence. Why the correct answer wins: A manager agent routes to specialists and consolidates their replies.
- **C:** Incorrect for this question. Parallel execution reduces wall-clock time for independent work. Reconciliation still requires design. Why the correct answer wins: A manager agent routes to specialists and consolidates their replies.
- **D:** Correct. A manager routes tasks and merges results. Clear responsibility and failure handling are required. In this case: A manager agent routes to specialists and consolidates their replies.

### Question 25 — D

Answer: Enable tracing across agent, model, and tool calls. Traces show the ordered model and tool calls so the failing step can be found. Traces localize failures and latency in multi-step workflows. Correlate them with evaluation results and deployment versions. Local study-map skill 2.7 (Agent Monitoring and Error Analysis), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Foundry Agent Service documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/agents/

- **A:** Incorrect for this question. Lower temperature reduces sampling variability. It does not guarantee factual correctness. Why the correct answer wins: Traces show the ordered model and tool calls so the failing step can be found.
- **B:** Incorrect for this question. Caching can reduce cost and latency for repeated content. Validate correctness and invalidation behavior. Why the correct answer wins: Traces show the ordered model and tool calls so the failing step can be found.
- **C:** Incorrect for this question. Watermarks support disclosure and traceability. They do not replace usage policy or review. Why the correct answer wins: Traces show the ordered model and tool calls so the failing step can be found.
- **D:** Correct. Traces localize failures and latency in multi-step workflows. Correlate them with evaluation results and deployment versions. In this case: Traces show the ordered model and tool calls so the failing step can be found.

### Question 26 — C

Answer: Lower temperature for more deterministic extraction. A lower temperature reduces sampling variability so identical prompts return stable labels. Lower temperature reduces sampling variability. It does not guarantee factual correctness. Local study-map skill 2.8 (Generation Tuning and Observability), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Foundry Agent Service documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/agents/

- **A:** Incorrect for this question. Top-p narrows or broadens token sampling. Tune with evaluation rather than by intuition. Why the correct answer wins: A lower temperature reduces sampling variability so identical prompts return stable labels.
- **B:** Incorrect for this question. Caching can reduce cost and latency for repeated content. Validate correctness and invalidation behavior. Why the correct answer wins: A lower temperature reduces sampling variability so identical prompts return stable labels.
- **C:** Correct. Lower temperature reduces sampling variability. It does not guarantee factual correctness. In this case: A lower temperature reduces sampling variability so identical prompts return stable labels.
- **D:** Incorrect for this question. Routing can balance quality and cost. Fallback and evaluation are required. Why the correct answer wins: A lower temperature reduces sampling variability so identical prompts return stable labels.

### Question 27 — B

Answer: Alert on latency, error rate, safety, and cost thresholds. Alert rules notify the team when a monitored metric crosses a threshold. Alerts turn monitoring into action. Route them to an accountable owner with a runbook. Local study-map skill 2.7 (Agent Monitoring and Error Analysis), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Foundry Agent Service documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/agents/

- **A:** Incorrect for this question. User behavior, data, and models change. Rolling baselines reveal degradation that a one-time evaluation misses. Why the correct answer wins: Alert rules notify the team when a monitored metric crosses a threshold.
- **B:** Correct. Alerts turn monitoring into action. Route them to an accountable owner with a runbook. In this case: Alert rules notify the team when a monitored metric crosses a threshold.
- **C:** Incorrect for this question. Audit evidence supports investigation and accountability. Protect log integrity and retention. Why the correct answer wins: Alert rules notify the team when a monitored metric crosses a threshold.
- **D:** Incorrect for this question. Central telemetry captures latency, errors, dependencies, and custom events. Redact sensitive content before logging. Why the correct answer wins: Alert rules notify the team when a monitored metric crosses a threshold.

### Question 28 — D

Answer: Generate images from text and reference media. Image generation produces a new illustration from a description. Image generation supports creative and product workflows. Apply policy, watermarking, and provenance controls. Local study-map skill 3.1 (Image Generation and Editing), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Azure AI Vision and Content Understanding documentation: https://learn.microsoft.com/en-us/azure/ai-services/content-understanding/

- **A:** Incorrect for this question. Inpainting changes a selected area while preserving the rest. Validate identity, brand, and safety constraints. Why the correct answer wins: Image generation produces a new illustration from a description.
- **B:** Incorrect for this question. Alt text should convey purpose and essential content, not decorative detail. Human review is still needed for critical pages. Why the correct answer wins: Image generation produces a new illustration from a description.
- **C:** Incorrect for this question. Video generation creates clips from prompts or images. Duration, consistency, and safety require review. Why the correct answer wins: Image generation produces a new illustration from a description.
- **D:** Correct. Image generation supports creative and product workflows. Apply policy, watermarking, and provenance controls. In this case: Image generation produces a new illustration from a description.

### Question 29 — A

Answer: Apply prompt-driven image modifications. Targeted image editing changes the selected element only. Prompt-based edits can alter style or content. Review outputs for unintended changes and policy violations. Local study-map skill 3.1 (Image Generation and Editing), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Azure AI Vision and Content Understanding documentation: https://learn.microsoft.com/en-us/azure/ai-services/content-understanding/

- **A:** Correct. Prompt-based edits can alter style or content. Review outputs for unintended changes and policy violations. In this case: Targeted image editing changes the selected element only.
- **B:** Incorrect for this question. Inpainting changes a selected area while preserving the rest. Validate identity, brand, and safety constraints. Why the correct answer wins: Targeted image editing changes the selected element only.
- **C:** Incorrect for this question. Captions describe visual content for users or downstream systems. Match detail to the audience and purpose. Why the correct answer wins: Targeted image editing changes the selected element only.
- **D:** Incorrect for this question. Video editing can revise scenes or timing. Preserve provenance and review for harmful manipulation. Why the correct answer wins: Targeted image editing changes the selected element only.

### Question 30 — C

Answer: Analyze video segments for events and content. Video analysis locates events and timestamps in existing footage. Video analysis can summarize or detect events across time. Sampling strategy affects coverage and cost. Local study-map skill 3.2 (Video Generation and Editing), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Azure AI Vision and Content Understanding documentation: https://learn.microsoft.com/en-us/azure/ai-services/content-understanding/

- **A:** Incorrect for this question. Captions describe visual content for users or downstream systems. Match detail to the audience and purpose. Why the correct answer wins: Video analysis locates events and timestamps in existing footage.
- **B:** Incorrect for this question. Video editing can revise scenes or timing. Preserve provenance and review for harmful manipulation. Why the correct answer wins: Video analysis locates events and timestamps in existing footage.
- **C:** Correct. Video analysis can summarize or detect events across time. Sampling strategy affects coverage and cost. In this case: Video analysis locates events and timestamps in existing footage.
- **D:** Incorrect for this question. Video generation creates clips from prompts or images. Duration, consistency, and safety require review. Why the correct answer wins: Video analysis locates events and timestamps in existing footage.

### Question 31 — C, D

Answers: Generate concise or detailed image captions; Generate alt text aligned to accessibility guidance. Captions help discovery, and alt text supports assistive technology. Captions describe visual content for users or downstream systems. Match detail to the audience and purpose. Alt text should convey purpose and essential content, not decorative detail. Human review is still needed for critical pages. Local study-map skill 3.3 (Multimodal Understanding and Accessibility), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Azure AI Vision and Content Understanding documentation: https://learn.microsoft.com/en-us/azure/ai-services/content-understanding/

- **A:** Incorrect for this question. Provisioned capacity reserves throughput at a committed cost. It fits stable demand, not unpredictable spikes. Why the correct answer wins: Captions help discovery, and alt text supports assistive technology.
- **B:** Incorrect for this question. Lower temperature reduces sampling variability. It does not guarantee factual correctness. Why the correct answer wins: Captions help discovery, and alt text supports assistive technology.
- **C:** Correct. Captions describe visual content for users or downstream systems. Match detail to the audience and purpose. In this case: Captions help discovery, and alt text supports assistive technology.
- **D:** Correct. Alt text should convey purpose and essential content, not decorative detail. Human review is still needed for critical pages. In this case: Captions help discovery, and alt text supports assistive technology.
- **E:** Incorrect for this question. Watermarks support disclosure and traceability. They do not replace usage policy or review. Why the correct answer wins: Captions help discovery, and alt text supports assistive technology.

### Question 32 — C

Answer: Use pro mode for complex multimodal content understanding. Pro mode handles complex multi-page multimodal documents. Pro mode handles more demanding layouts and multimodal inputs at higher cost. Use it where simpler modes fail requirements. Local study-map skill 3.4 (Visual Extraction and Video Analysis), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Azure AI Vision and Content Understanding documentation: https://learn.microsoft.com/en-us/azure/ai-services/content-understanding/

- **A:** Incorrect for this question. Custom models fit specialized forms not covered by prebuilts. They require representative labels and retraining discipline. Why the correct answer wins: Pro mode handles complex multi-page multimodal documents.
- **B:** Incorrect for this question. Single-task analyzers target one content type or objective. They may be simpler and cheaper than general pro-mode pipelines. Why the correct answer wins: Pro mode handles complex multi-page multimodal documents.
- **C:** Correct. Pro mode handles more demanding layouts and multimodal inputs at higher cost. Use it where simpler modes fail requirements. In this case: Pro mode handles complex multi-page multimodal documents.
- **D:** Incorrect for this question. Document Intelligence provides prebuilt and custom extraction for structured documents. Validate field accuracy on representative samples. Why the correct answer wins: Pro mode handles complex multi-page multimodal documents.

### Question 33 — A, E

Answers: Enforce brand and usage rules for generated visuals; Apply watermarks or provenance markers to generated media. Brand policy constrains approved visual usage, and watermarking identifies synthetic media. Brand controls define permitted logos, styles, and claims. Technical generation must still pass approval. Watermarks support disclosure and traceability. They do not replace usage policy or review. Local study-map skill 3.5 (Multimodal Responsible AI), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Azure AI Vision and Content Understanding documentation: https://learn.microsoft.com/en-us/azure/ai-services/content-understanding/

- **A:** Correct. Watermarks support disclosure and traceability. They do not replace usage policy or review. In this case: Brand policy constrains approved visual usage, and watermarking identifies synthetic media.
- **B:** Incorrect for this question. Lower temperature reduces sampling variability. It does not guarantee factual correctness. Why the correct answer wins: Brand policy constrains approved visual usage, and watermarking identifies synthetic media.
- **C:** Incorrect for this question. Caching can reduce cost and latency for repeated content. Validate correctness and invalidation behavior. Why the correct answer wins: Brand policy constrains approved visual usage, and watermarking identifies synthetic media.
- **D:** Incorrect for this question. Top-p narrows or broadens token sampling. Tune with evaluation rather than by intuition. Why the correct answer wins: Brand policy constrains approved visual usage, and watermarking identifies synthetic media.
- **E:** Correct. Brand controls define permitted logos, styles, and claims. Technical generation must still pass approval. In this case: Brand policy constrains approved visual usage, and watermarking identifies synthetic media.

### Question 34 — B

Answer: Treat text embedded in images as untrusted input. Text embedded in a document is an indirect prompt injection attempt. Visible instructions in images can attempt to manipulate an agent. Isolate, detect, and never let image text grant authority. Local study-map skill 3.5 (Multimodal Responsible AI), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Azure AI Vision and Content Understanding documentation: https://learn.microsoft.com/en-us/azure/ai-services/content-understanding/

- **A:** Incorrect for this question. Watermarks support disclosure and traceability. They do not replace usage policy or review. Why the correct answer wins: Text embedded in a document is an indirect prompt injection attempt.
- **B:** Correct. Visible instructions in images can attempt to manipulate an agent. Isolate, detect, and never let image text grant authority. In this case: Text embedded in a document is an indirect prompt injection attempt.
- **C:** Incorrect for this question. Image and video safety filters reduce exposure to harmful content. Thresholds and human escalation should match policy. Why the correct answer wins: Text embedded in a document is an indirect prompt injection attempt.
- **D:** Incorrect for this question. Captions describe visual content for users or downstream systems. Match detail to the audience and purpose. Why the correct answer wins: Text embedded in a document is an indirect prompt injection attempt.

### Question 35 — A

Answer: Prompt for JSON that conforms to a supplied schema. Schema-constrained JSON supports validation and automation. Schema-guided generation improves machine readability. Validate values against source evidence and business rules. Local study-map skill 4.1 (Language Model Text Analysis), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Azure AI Language, Speech, and Translator documentation: https://learn.microsoft.com/en-us/azure/ai-services/

- **A:** Correct. Schema-guided generation improves machine readability. Validate values against source evidence and business rules. In this case: Schema-constrained JSON supports validation and automation.
- **B:** Incorrect for this question. Summaries should preserve required facts and caveats. Fluency does not prove completeness. Why the correct answer wins: Schema-constrained JSON supports validation and automation.
- **C:** Incorrect for this question. Topic extraction supports discovery and grouping. It is not a substitute for an authoritative taxonomy. Why the correct answer wins: Schema-constrained JSON supports validation and automation.
- **D:** Incorrect for this question. Translation should preserve meaning, names, and formatting. Evaluate domain terminology and low-resource languages. Why the correct answer wins: Schema-constrained JSON supports validation and automation.

### Question 36 — B, C

Answers: Detect and redact sensitive personal data; Analyze sentiment and tone with an appropriate service. PII detection finds personal data, and sentiment detects frustration. Sensitive Data Protection or language PII detection can identify and mask data. Verify that redaction covers every path where content flows. Sentiment analysis can support triage and monitoring. Domain and language variation require validation. Local study-map skill 4.1 (Language Model Text Analysis), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Azure AI Language, Speech, and Translator documentation: https://learn.microsoft.com/en-us/azure/ai-services/

- **A:** Incorrect for this question. Summaries should preserve required facts and caveats. Fluency does not prove completeness. Why the correct answer wins: PII detection finds personal data, and sentiment detects frustration.
- **B:** Correct. Sentiment analysis can support triage and monitoring. Domain and language variation require validation. In this case: PII detection finds personal data, and sentiment detects frustration.
- **C:** Correct. Sensitive Data Protection or language PII detection can identify and mask data. Verify that redaction covers every path where content flows. In this case: PII detection finds personal data, and sentiment detects frustration.
- **D:** Incorrect for this question. Glossaries keep product and legal terms consistent. Terms still need human validation in context. Why the correct answer wins: PII detection finds personal data, and sentiment detects frustration.
- **E:** Incorrect for this question. Topic extraction supports discovery and grouping. It is not a substitute for an authoritative taxonomy. Why the correct answer wins: PII detection finds personal data, and sentiment detects frustration.

### Question 37 — A

Answer: Apply a custom glossary or terminology list. A glossary enforces approved term mappings across languages. Glossaries keep product and legal terms consistent. Terms still need human validation in context. Local study-map skill 4.2 (Translation), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Azure AI Language, Speech, and Translator documentation: https://learn.microsoft.com/en-us/azure/ai-services/

- **A:** Correct. Glossaries keep product and legal terms consistent. Terms still need human validation in context. In this case: A glossary enforces approved term mappings across languages.
- **B:** Incorrect for this question. Translation should preserve meaning, names, and formatting. Evaluate domain terminology and low-resource languages. Why the correct answer wins: A glossary enforces approved term mappings across languages.
- **C:** Incorrect for this question. Entity extraction turns text into structured facts. Ambiguous mentions need resolution and validation. Why the correct answer wins: A glossary enforces approved term mappings across languages.
- **D:** Incorrect for this question. Sensitive Data Protection or language PII detection can identify and mask data. Verify that redaction covers every path where content flows. Why the correct answer wins: A glossary enforces approved term mappings across languages.

### Question 38 — A, B

Answers: Use Azure Translator or a language model for translation; Customize summaries and extraction for compliance needs. Translation localizes content, and compliance framing preserves required wording. Translation should preserve meaning, names, and formatting. Evaluate domain terminology and low-resource languages. Compliance work requires precise citation, retention, and review. Generic summarization is insufficient without controls. Local study-map skill 4.2 (Translation), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Azure AI Language, Speech, and Translator documentation: https://learn.microsoft.com/en-us/azure/ai-services/

- **A:** Correct. Compliance work requires precise citation, retention, and review. Generic summarization is insufficient without controls. In this case: Translation localizes content, and compliance framing preserves required wording.
- **B:** Correct. Translation should preserve meaning, names, and formatting. Evaluate domain terminology and low-resource languages. In this case: Translation localizes content, and compliance framing preserves required wording.
- **C:** Incorrect for this question. Summaries should preserve required facts and caveats. Fluency does not prove completeness. Why the correct answer wins: Translation localizes content, and compliance framing preserves required wording.
- **D:** Incorrect for this question. Entity extraction turns text into structured facts. Ambiguous mentions need resolution and validation. Why the correct answer wins: Translation localizes content, and compliance framing preserves required wording.
- **E:** Incorrect for this question. Topic extraction supports discovery and grouping. It is not a substitute for an authoritative taxonomy. Why the correct answer wins: Translation localizes content, and compliance framing preserves required wording.

### Question 39 — C

Answer: Capture audio → transcribe → translate text → synthesize speech → return audio. Speech translation transcribes, translates, then synthesizes the target-language reply. Speech translation transcribes first, translates the text, then synthesizes the target-language audio. Local study-map skill 4.3 (Speech Solutions), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Azure AI Language, Speech, and Translator documentation: https://learn.microsoft.com/en-us/azure/ai-services/

- **A:** Incorrect for this question. Synthesis cannot precede transcription and translation. Why the correct answer wins: Speech translation transcribes, translates, then synthesizes the target-language reply.
- **B:** Incorrect for this question. Capture must come first, and synthesis must follow translation. Why the correct answer wins: Speech translation transcribes, translates, then synthesizes the target-language reply.
- **C:** Correct. Speech translation transcribes first, translates the text, then synthesizes the target-language audio. In this case: Speech translation transcribes, translates, then synthesizes the target-language reply.
- **D:** Incorrect for this question. Audio must be captured before it can be transcribed or translated. Why the correct answer wins: Speech translation transcribes, translates, then synthesizes the target-language reply.

### Question 40 — B

Answer: Transcribe speech to text with Azure AI Speech. Speech-to-text transcribes audio into searchable text. Speech-to-text enables voice agents and transcript analysis. Audio quality, accents, and domain terms affect accuracy. Local study-map skill 4.3 (Speech Solutions), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Azure AI Language, Speech, and Translator documentation: https://learn.microsoft.com/en-us/azure/ai-services/

- **A:** Incorrect for this question. Captions describe visual content for users or downstream systems. Match detail to the audience and purpose. Why the correct answer wins: Speech-to-text transcribes audio into searchable text.
- **B:** Correct. Speech-to-text enables voice agents and transcript analysis. Audio quality, accents, and domain terms affect accuracy. In this case: Speech-to-text transcribes audio into searchable text.
- **C:** Incorrect for this question. Speech translation combines recognition and translation. Preserve timing and speaker context where needed. Why the correct answer wins: Speech-to-text transcribes audio into searchable text.
- **D:** Incorrect for this question. Text-to-speech supports voice responses and accessibility. Voice, prosody, and latency affect usability. Why the correct answer wins: Speech-to-text transcribes audio into searchable text.

### Question 41 — D

Answer: Adapt prompts and models to domain terminology. A validated domain lexicon teaches local terminology to the extraction step. Domain adaptation improves consistency and recall. Validate against expert-created expected outputs. Local study-map skill 4.4 (Domain Customization), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Azure AI Language, Speech, and Translator documentation: https://learn.microsoft.com/en-us/azure/ai-services/

- **A:** Incorrect for this question. Translation should preserve meaning, names, and formatting. Evaluate domain terminology and low-resource languages. Why the correct answer wins: A validated domain lexicon teaches local terminology to the extraction step.
- **B:** Incorrect for this question. Sensitive Data Protection or language PII detection can identify and mask data. Verify that redaction covers every path where content flows. Why the correct answer wins: A validated domain lexicon teaches local terminology to the extraction step.
- **C:** Incorrect for this question. Glossaries keep product and legal terms consistent. Terms still need human validation in context. Why the correct answer wins: A validated domain lexicon teaches local terminology to the extraction step.
- **D:** Correct. Domain adaptation improves consistency and recall. Validate against expert-created expected outputs. In this case: A validated domain lexicon teaches local terminology to the extraction step.

### Question 42 — C

Answer: Use an Azure AI Search indexer to pull source content. An indexer pulls source documents and tracks changes. Indexers automate ingestion and can run on a schedule. Monitor failures, deletions, and field mappings. Local study-map skill 5.1 (Content Ingestion and Indexing), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Azure AI Search documentation: https://learn.microsoft.com/en-us/azure/search/

- **A:** Incorrect for this question. OCR unlocks text in scans and screenshots. Layout and table structure may still require specialized extraction. Why the correct answer wins: An indexer pulls source documents and tracks changes.
- **B:** Incorrect for this question. Skillsets can OCR, split, embed, and extract during indexing. Each skill adds latency, cost, and failure modes. Why the correct answer wins: An indexer pulls source documents and tracks changes.
- **C:** Correct. Indexers automate ingestion and can run on a schedule. Monitor failures, deletions, and field mappings. In this case: An indexer pulls source documents and tracks changes.
- **D:** Incorrect for this question. Push ingestion supports near-real-time updates from applications. The app owns batching, retries, and deletion. Why the correct answer wins: An indexer pulls source documents and tracks changes.

### Question 43 — C

Answer: Apply document-level security filters at query time. Document-level security filters restrict results before content reaches the model. Filters restrict results to content the user may see. They must be enforced before content reaches the model. Local study-map skill 5.2 (Search and Grounding Configuration), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Azure AI Search documentation: https://learn.microsoft.com/en-us/azure/search/

- **A:** Incorrect for this question. A semantic ranker can improve relevance for natural-language queries. It adds cost and latency and should be measured against a baseline. Why the correct answer wins: Document-level security filters restrict results before content reaches the model.
- **B:** Incorrect for this question. Stale content produces outdated answers. Define refresh expectations and test deletion behavior. Why the correct answer wins: Document-level security filters restrict results before content reaches the model.
- **C:** Correct. Filters restrict results to content the user may see. They must be enforced before content reaches the model. In this case: Document-level security filters restrict results before content reaches the model.
- **D:** Incorrect for this question. Hybrid search covers exact identifiers and paraphrased meaning together. Fusion and ranking need testing on representative queries. Why the correct answer wins: Document-level security filters restrict results before content reaches the model.

### Question 44 — A

Answer: Ingest → extract text → chunk → embed → index → retrieve with citations. Extraction, chunking, embedding, and indexing precede retrieval and citation. The supported RAG ingestion order produces searchable, citable evidence. Retrieval cannot work before content is extracted, chunked, embedded, and indexed. Local study-map skill 5.4 (RAG Ingestion and OCR), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Azure AI Search documentation: https://learn.microsoft.com/en-us/azure/search/

- **A:** Correct. The supported RAG ingestion order produces searchable, citable evidence. Retrieval cannot work before content is extracted, chunked, embedded, and indexed. In this case: Extraction, chunking, embedding, and indexing precede retrieval and citation.
- **B:** Incorrect for this question. Retrieval is attempted before the index exists and source ingestion is incomplete. Why the correct answer wins: Extraction, chunking, embedding, and indexing precede retrieval and citation.
- **C:** Incorrect for this question. Retrieval before chunking, embedding, and indexing has nothing searchable to return. Why the correct answer wins: Extraction, chunking, embedding, and indexing precede retrieval and citation.
- **D:** Incorrect for this question. Indexing before extraction or embedding creates an empty or unusable index. Why the correct answer wins: Extraction, chunking, embedding, and indexing precede retrieval and citation.

### Question 45 — C

Answer: Use provisioned throughput for predictable high-volume workloads. Provisioned throughput reserves capacity for predictable continuous demand. Provisioned capacity reserves throughput at a committed cost. It fits stable demand, not unpredictable spikes. Local study-map skill 1.4 (Quotas, Scaling, and Cost), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Microsoft Foundry documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/

- **A:** Incorrect for this question. Caching can reduce cost and latency for repeated content. Validate correctness and invalidation behavior. Why the correct answer wins: Provisioned throughput reserves capacity for predictable continuous demand.
- **B:** Incorrect for this question. Standard deployments bill per token and scale within quota. They suit spiky or early workloads. Why the correct answer wins: Provisioned throughput reserves capacity for predictable continuous demand.
- **C:** Correct. Provisioned capacity reserves throughput at a committed cost. It fits stable demand, not unpredictable spikes. In this case: Provisioned throughput reserves capacity for predictable continuous demand.
- **D:** Incorrect for this question. Batch deployments can lower cost for large asynchronous jobs. They are unsuitable for interactive agent turns. Why the correct answer wins: Provisioned throughput reserves capacity for predictable continuous demand.

### Question 46 — D

Answer: Require citations tied to retrieved evidence. Citations tie each answer to the evidence that supports it. Citations let users verify claims and support auditing. Preserve source and chunk identifiers through the pipeline. Local study-map skill 2.3 (Evaluating Models and Applications), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Foundry Agent Service documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/agents/

- **A:** Incorrect for this question. Watermarks support disclosure and traceability. They do not replace usage policy or review. Why the correct answer wins: Citations tie each answer to the evidence that supports it.
- **B:** Incorrect for this question. Caching can reduce cost and latency for repeated content. Validate correctness and invalidation behavior. Why the correct answer wins: Citations tie each answer to the evidence that supports it.
- **C:** Incorrect for this question. Lower temperature reduces sampling variability. It does not guarantee factual correctness. Why the correct answer wins: Citations tie each answer to the evidence that supports it.
- **D:** Correct. Citations let users verify claims and support auditing. Preserve source and chunk identifiers through the pipeline. In this case: Citations tie each answer to the evidence that supports it.

### Question 47 — B

Answer: Select evidence within the model's usable context. The context budget limits how much retrieved evidence enters the prompt. More retrieved text is not always better. Order and compress evidence to preserve decisive facts. Local study-map skill 5.5 (Retrieval Integration with Agents), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Azure AI Search documentation: https://learn.microsoft.com/en-us/azure/search/

- **A:** Incorrect for this question. Reranking improves precision after broad recall. It adds latency and must be evaluated. Why the correct answer wins: The context budget limits how much retrieved evidence enters the prompt.
- **B:** Correct. More retrieved text is not always better. Order and compress evidence to preserve decisive facts. In this case: The context budget limits how much retrieved evidence enters the prompt.
- **C:** Incorrect for this question. De-duplication frees context space that duplicates would otherwise consume, so the most informative evidence survives the budget. Why the correct answer wins: The context budget limits how much retrieved evidence enters the prompt.
- **D:** Incorrect for this question. Embeddings support similarity search over meaning rather than exact terms. Vector search still needs chunking, filtering, and evaluation. Why the correct answer wins: The context budget limits how much retrieved evidence enters the prompt.

### Question 48 — A, B

Answers: Persist conversation history in a thread or session; Expose a typed function as an agent tool. Conversation state preserves the case number, and a function tool performs the lookup. Threads support continuity across turns. Apply retention and access controls to stored history. Function tools let the agent request a defined operation with structured arguments. Authorization and input validation must be enforced server-side. Local study-map skill 2.5 (Agent Tools, Retrieval, Memory, and Function Calling), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Foundry Agent Service documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/agents/

- **A:** Correct. Threads support continuity across turns. Apply retention and access controls to stored history. In this case: Conversation state preserves the case number, and a function tool performs the lookup.
- **B:** Correct. Function tools let the agent request a defined operation with structured arguments. Authorization and input validation must be enforced server-side. In this case: Conversation state preserves the case number, and a function tool performs the lookup.
- **C:** Incorrect for this question. Watermarks support disclosure and traceability. They do not replace usage policy or review. Why the correct answer wins: Conversation state preserves the case number, and a function tool performs the lookup.
- **D:** Incorrect for this question. Provisioned capacity reserves throughput at a committed cost. It fits stable demand, not unpredictable spikes. Why the correct answer wins: Conversation state preserves the case number, and a function tool performs the lookup.
- **E:** Incorrect for this question. Embeddings determine semantic similarity behavior. Evaluate retrieval quality before and after changes. Why the correct answer wins: Conversation state preserves the case number, and a function tool performs the lookup.

### Question 49 — C

Answer: Train a custom extraction model on labeled documents. A custom extraction model targets a proprietary layout. Custom models fit specialized forms not covered by prebuilts. They require representative labels and retraining discipline. Local study-map skill 5.6 (Document and Content Extraction), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Azure AI Search documentation: https://learn.microsoft.com/en-us/azure/search/

- **A:** Incorrect for this question. Analyzers define what to extract and how to return it. Version and test them like application code. Why the correct answer wins: A custom extraction model targets a proprietary layout.
- **B:** Incorrect for this question. Document Intelligence provides prebuilt and custom extraction for structured documents. Validate field accuracy on representative samples. Why the correct answer wins: A custom extraction model targets a proprietary layout.
- **C:** Correct. Custom models fit specialized forms not covered by prebuilts. They require representative labels and retraining discipline. In this case: A custom extraction model targets a proprietary layout.
- **D:** Incorrect for this question. Prebuilt models cover invoices, receipts, IDs, and similar formats. Check supported locales and field coverage. Why the correct answer wins: A custom extraction model targets a proprietary layout.

### Question 50 — A

Answer: Add an enrichment skillset to an indexing pipeline. A skillset defines the enrichment steps applied during indexing. Skillsets can OCR, split, embed, and extract during indexing. Each skill adds latency, cost, and failure modes. Local study-map skill 5.3 (Enrichment Skills), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Azure AI Search documentation: https://learn.microsoft.com/en-us/azure/search/

- **A:** Correct. Skillsets can OCR, split, embed, and extract during indexing. Each skill adds latency, cost, and failure modes. In this case: A skillset defines the enrichment steps applied during indexing.
- **B:** Incorrect for this question. A skillset can extract entities, captions, and structure during indexing. Enrichment adds cost and failure points that need monitoring. Why the correct answer wins: A skillset defines the enrichment steps applied during indexing.
- **C:** Incorrect for this question. OCR unlocks text in scans and screenshots. Layout and table structure may still require specialized extraction. Why the correct answer wins: A skillset defines the enrichment steps applied during indexing.
- **D:** Incorrect for this question. Push ingestion supports near-real-time updates from applications. The app owns batching, retries, and deletion. Why the correct answer wins: A skillset defines the enrichment steps applied during indexing.
